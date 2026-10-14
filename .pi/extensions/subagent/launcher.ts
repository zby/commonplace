import * as fs from "node:fs";
import * as os from "node:os";
import * as path from "node:path";
import type { ThinkingLevel } from "@earendil-works/pi-agent-core";
import type { Message } from "@earendil-works/pi-ai";
import { withFileMutationQueue } from "@earendil-works/pi-coding-agent";
import type { AgentConfig } from "./agents.ts";
import { runProcess } from "./process.ts";

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
	stopReason?: string;
	errorMessage?: string;
}

export function failed(result: SingleResult): boolean {
	return result.exitCode !== 0 || Boolean(result.errorMessage) || ["error", "aborted"].includes(result.stopReason ?? "");
}
export function output(result: SingleResult): string {
	if (failed(result) && (result.errorMessage || result.stderr)) return result.errorMessage || result.stderr;
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

/** One fresh non-persisted Pi conversation. Discovery/trust and ownership are callers' responsibilities. */
export async function launch(
	agent: AgentConfig, task: string, cwd: string, defaults: LaunchConfig, overrides: LaunchConfig,
	signal: AbortSignal, onUpdate?: (result: SingleResult) => void,
): Promise<SingleResult> {
	if (agent.configurationError) throw new Error(agent.configurationError);
	const model = overrides.model ?? agent.model ?? defaults.model;
	const thinkingLevel = overrides.thinkingLevel ??
		(overrides.model !== undefined || !agent.model ? defaults.thinkingLevel : undefined);
	const args = ["--mode", "json", "-p", "--no-session"];
	if (model) args.push("--model", model);
	if (thinkingLevel !== undefined) args.push("--thinking", thinkingLevel);
	if (agent.tools) args.push("--tools", agent.tools.join(","));
	const result: SingleResult = {
		agent: agent.name, agentSource: agent.source, task, cwd, exitCode: -1, messages: [], stderr: "",
		usage: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0, cost: 0, contextTokens: 0, turns: 0 },
		model, thinkingLevel,
	};
	let temp: string | undefined;
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
		const closed = await runProcess(cmd.command, cmd.args, cwd, signal, text => {
			buffer += text;
			const lines = buffer.split("\n");
			buffer = lines.pop() || "";
			for (const text of lines) line(text);
		}, text => { result.stderr += text; });
		if (buffer.trim()) line(buffer);
		result.exitCode = closed.exitCode;
		if (closed.error) result.errorMessage = closed.error;
		if (closed.exitCode === 0 && !result.messages.some(m => m.role === "assistant"))
			result.errorMessage = "Subagent exited without an assistant result";
		if (closed.aborted) {
			result.stopReason = "aborted";
			result.errorMessage = "Subagent was aborted";
		}
		return result;
	} finally {
		if (temp) await fs.promises.rm(temp, { recursive: true, force: true });
	}
}
