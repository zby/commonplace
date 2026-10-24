import * as fs from "node:fs";
import * as os from "node:os";
import * as path from "node:path";
import { fileURLToPath } from "node:url";
import type { ThinkingLevel } from "@earendil-works/pi-agent-core";
import type { Message } from "@earendil-works/pi-ai";
import { withFileMutationQueue } from "@earendil-works/pi-coding-agent";
import type { AgentConfig } from "./agents.ts";
import { runProcess } from "./process.ts";
import { acquireSessionLock, resumeSession, SessionAudit, type SessionReference } from "./sessions.ts";

export interface LaunchConfig { model?: string; thinkingLevel?: ThinkingLevel }
export interface SingleResult {
	agent: string;
	agentSource: "user" | "project" | "unknown";
	task: string;
	cwd: string;
	exitCode: number;
	messages: Message[];
	stderr: string;
	usage: { input: number; output: number; cacheRead: number; cacheWrite: number;
		cost: number; contextTokens: number; turns: number };
	model?: string;
	/** Requested level, not independent verification of effective effort. */
	thinkingLevel?: ThinkingLevel;
	sessionId?: string;
	sessionFile?: string;
	executionDir?: string;
	stopReason?: string;
	errorMessage?: string;
}

export function failed(result: SingleResult): boolean {
	return result.exitCode !== 0 || Boolean(result.errorMessage) || ["error", "aborted"].includes(result.stopReason ?? "");
}
export function output(result: SingleResult): string {
	if (failed(result) && (result.errorMessage || result.stderr.trim())) return result.errorMessage || result.stderr;
	for (const message of [...result.messages].reverse()) {
		if (message.role !== "assistant") continue;
		const text = message.content.filter(part => part.type === "text").map(part => part.text).join("\n");
		if (text) return text;
	}
	return "(no output)";
}
export function summary(text: string): string {
	const cap = 50 * 1024;
	if (Buffer.byteLength(text) <= cap) return text;
	let truncated = text.slice(0, cap);
	while (Buffer.byteLength(truncated) > cap) truncated = truncated.slice(0, -1);
	return truncated + "\n[Output truncated; full output preserved in tool details.]";
}
function invocation(args: string[]) {
	const script = process.argv[1];
	if (script && !script.startsWith("/$bunfs/root/") && fs.existsSync(script))
		return { command: process.execPath, args: [script, ...args] };
	if (!/^(node|bun)(\.exe)?$/.test(path.basename(process.execPath).toLowerCase()))
		return { command: process.execPath, args };
	return { command: "pi", args };
}

/** Fresh persistent conversation by default; explicit continuation never guesses a session. */
export async function launch(
	agent: AgentConfig, task: string, cwd: string, defaults: LaunchConfig, overrides: LaunchConfig,
	signal: AbortSignal, onUpdate?: (result: SingleResult) => void, sessionFile?: string,
): Promise<SingleResult> {
	if (agent.configurationError) throw new Error(agent.configurationError);
	const resumed = sessionFile ? resumeSession(sessionFile, agent, cwd) : undefined;
	const model = overrides.model ?? (resumed ? resumed.record.model : agent.model ?? defaults.model);
	const thinkingLevel = overrides.thinkingLevel ?? (resumed ? resumed.record.thinkingLevel :
		(overrides.model !== undefined || !agent.model ? defaults.thinkingLevel : undefined));
	const config = { model, thinkingLevel };
	const args = ["--mode", "json", "-p", "--extension", fileURLToPath(new URL("./session-info.ts", import.meta.url))];
	if (resumed) args.push("--session", resumed.sessionFile);
	if (model) args.push("--model", model);
	if (thinkingLevel !== undefined) args.push("--thinking", thinkingLevel);
	if (agent.tools) args.push("--tools", agent.tools.join(","));
	const result: SingleResult = {
		agent: agent.name, agentSource: agent.source, task, cwd, exitCode: -1, messages: [], stderr: "",
		usage: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0, cost: 0, contextTokens: 0, turns: 0 },
		model, thinkingLevel,
		...(resumed ? { sessionId: resumed.sessionId, sessionFile: resumed.sessionFile } : {}),
	};
	let temp: string | undefined;
	let audit: SessionAudit | undefined;
	let releaseSession = resumed?.release;
	let auditError: string | undefined;
	let prelude = "";
	let stderrPrelude = "";
	let stderrBuffer = "";
	const recordingAbort = new AbortController();
	const recordError = (error: unknown) => { auditError = `Session recording failed: ${error}`; recordingAbort.abort(); };
	const append = (name: "events.jsonl" | "stderr.log", text: string) => {
		try { if (!auditError) audit?.append(name, text); } catch (error) { recordError(error); }
	};
	const stderrLine = (text: string) => {
		if (text.startsWith("PI_SUBAGENT_SESSION ")) {
			try {
				const event = JSON.parse(text.slice("PI_SUBAGENT_SESSION ".length));
				if (audit || typeof event.sessionId !== "string" || typeof event.sessionFile !== "string" ||
					fs.realpathSync(event.cwd) !== fs.realpathSync(cwd)) throw new Error("Invalid worker session reference");
				const reference: SessionReference = { sessionId: event.sessionId, sessionFile: path.resolve(cwd, event.sessionFile) };
				if (resumed && (reference.sessionId !== resumed.sessionId || reference.sessionFile !== resumed.sessionFile))
					throw new Error("Pi opened a different session than requested");
				Object.assign(result, reference);
				releaseSession ??= acquireSessionLock(reference.sessionFile);
				audit = new SessionAudit(reference, agent, cwd, config, task, args);
				result.executionDir = audit.executionDir;
				append("events.jsonl", prelude); prelude = "";
				append("stderr.log", stderrPrelude); stderrPrelude = "";
				onUpdate?.(result);
			} catch (error) { recordError(error); }
			return;
		}
		result.stderr += text;
	};
	let buffer = "";
	const line = (text: string) => {
		let event;
		try { event = JSON.parse(text); } catch { return; }
		if (!["message_end", "tool_result_end"].includes(event.type) || !event.message) return;
		const message = event.message as Message;
		result.messages.push(message);
		if (message.role === "assistant") {
			result.usage.turns++;
			if (message.usage) {
				for (const key of ["input", "output", "cacheRead", "cacheWrite"] as const)
					result.usage[key] += message.usage[key] || 0;
				result.usage.cost += message.usage.cost?.total || 0;
				result.usage.contextTokens = message.usage.totalTokens || 0;
			}
			if (!result.model && message.model) result.model = message.model;
			// Pi can recover an earlier assistant error within this process. Keep its
			// message as evidence, but classify the latest assistant response.
			result.stopReason = message.stopReason;
			result.errorMessage = message.errorMessage;
		}
		onUpdate?.(result);
	};
	try {
		if (agent.systemPrompt.trim()) {
			temp = await fs.promises.mkdtemp(path.join(os.tmpdir(), "pi-subagent-"));
			const prompt = path.join(temp, "prompt.md");
			await withFileMutationQueue(prompt, () => fs.promises.writeFile(prompt, agent.systemPrompt, { mode: 0o600 }));
			args.push("--append-system-prompt", prompt);
		}
		args.push(`Task: ${task}`);
		const cmd = invocation(args);
		const closed = await runProcess(cmd.command, cmd.args, cwd,
			AbortSignal.any(signal ? [signal, recordingAbort.signal] : [recordingAbort.signal]), text => {
			if (audit) append("events.jsonl", text); else prelude += text;
			buffer += text;
			const lines = buffer.split("\n");
			buffer = lines.pop() || "";
			for (const text of lines) line(text);
		}, text => {
			if (audit) append("stderr.log", text); else stderrPrelude += text;
			stderrBuffer += text;
			const lines = stderrBuffer.split("\n");
			stderrBuffer = lines.pop() || "";
			for (const text of lines) stderrLine(text + "\n");
		});
		if (buffer.trim()) line(buffer);
		if (stderrBuffer) stderrLine(stderrBuffer);
		result.exitCode = closed.exitCode;
		if (closed.error) result.errorMessage = closed.error;
		if (closed.exitCode === 0 && !result.messages.some(m => m.role === "assistant"))
			result.errorMessage = "Subagent exited without an assistant result";
		if (closed.aborted) {
			result.stopReason = "aborted";
			result.errorMessage = "Subagent was aborted";
		}
	} catch (error) {
		result.exitCode = 1;
		result.errorMessage = String(error);
	} finally {
		if (!audit && !result.errorMessage) result.errorMessage = "Worker did not report its persistent session" +
			(result.stderr.trim() ? `: ${result.stderr.trim()}` : "");
		if (auditError) result.errorMessage = auditError;
		const finalizeError = (error: unknown) => {
			result.errorMessage = [result.errorMessage, `Session finalization failed: ${error}`].filter(Boolean).join("; ");
		};
		if (temp) {
			try { await fs.promises.rm(temp, { recursive: true, force: true }); }
			catch (error) { finalizeError(error); }
		}
		const saveOutcome = () => audit?.finish({ exitCode: result.exitCode, stopReason: result.stopReason,
			errorMessage: result.errorMessage, usage: result.usage }, agent, cwd, config);
		try { saveOutcome(); } catch (error) { finalizeError(error); }
		try { releaseSession?.(); }
		catch (error) {
			finalizeError(error);
			try { saveOutcome(); } catch (error) { finalizeError(error); }
		}
	}
	return result;
}
