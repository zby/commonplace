import * as fs from "node:fs";
import * as path from "node:path";
import { randomUUID } from "node:crypto";
import type { AgentConfig } from "./agents.ts";
import type { LaunchConfig } from "./launcher.ts";

export interface SessionReference { sessionId: string; sessionFile: string; executionDir?: string }
interface WorkerRecord extends LaunchConfig { sessionId: string; profile: string }

function profile(agent: AgentConfig, cwd: string): string {
	return JSON.stringify([fs.realpathSync(cwd), agent.name, agent.source, agent.filePath,
		agent.systemPrompt, agent.tools, agent.model]);
}
function directory(file: string): string { return file + ".subagent"; }
function saveJSON(file: string, value: unknown) {
	const temp = file + ".new";
	try {
		fs.writeFileSync(temp, JSON.stringify(value, null, 2) + "\n", { mode: 0o600 });
		fs.renameSync(temp, file);
	} finally { fs.rmSync(temp, { force: true }); }
}
export function acquireSessionLock(file: string): () => void {
	fs.mkdirSync(directory(file), { recursive: true, mode: 0o700 });
	const target = path.join(directory(file), "active");
	try { fs.mkdirSync(target, { mode: 0o700 }); }
	catch (error) {
		if ((error as NodeJS.ErrnoException).code === "EEXIST")
			throw new Error(`Worker session is active or has a stale lock: ${target}. Reconcile process ownership before removing it.`);
		throw error;
	}
	try { fs.writeFileSync(path.join(target, "owner.json"), JSON.stringify({ pid: process.pid, startedAt: new Date().toISOString() }), { mode: 0o600 }); }
	catch (error) { fs.rmSync(target, { recursive: true }); throw error; }
	let released = false;
	return () => { if (!released) { released = true; fs.rmSync(target, { recursive: true }); } };
}

/** Only explicitly recorded worker sessions can be resumed; never guess or create. */
export function resumeSession(file: string, agent: AgentConfig, cwd: string) {
	const sessionFile = fs.realpathSync(path.resolve(cwd, file));
	const read = () => {
		const header = JSON.parse(fs.readFileSync(sessionFile, "utf8").split("\n")[0]);
		const record = JSON.parse(fs.readFileSync(path.join(directory(sessionFile), "worker.json"), "utf8")) as WorkerRecord;
		if (header.type !== "session" || typeof header.id !== "string" || header.id !== record.sessionId ||
			fs.realpathSync(header.cwd) !== fs.realpathSync(cwd) || record.profile !== profile(agent, cwd))
			throw new Error("Worker session identity, working directory or agent definition does not match");
		return { sessionId: header.id as string, sessionFile, record };
	};
	read();
	const release = acquireSessionLock(sessionFile);
	try { return { ...read(), release }; }
	catch (error) { release(); throw error; }
}

/** Per-execution evidence lives beside the native session, not in temporary storage. */
export class SessionAudit {
	readonly executionDir: string;
	private metadata: Record<string, unknown> = {};
	constructor(
		readonly reference: SessionReference, agent: AgentConfig, cwd: string, config: LaunchConfig,
		task: string, args: string[],
	) {
		this.executionDir = path.join(directory(reference.sessionFile), randomUUID());
		fs.mkdirSync(this.executionDir, { mode: 0o700 });
		this.metadata = { startedAt: new Date().toISOString(), pid: process.pid, agent: agent.name,
			agentSource: agent.source, agentFile: agent.filePath, systemPrompt: agent.systemPrompt,
			tools: agent.tools, cwd, task, args, ...config, ...reference };
		for (const name of ["events.jsonl", "stderr.log"]) fs.writeFileSync(path.join(this.executionDir, name), "", { mode: 0o600 });
		this.save();
		this.saveWorker(agent, cwd, config);
	}
	append(name: "events.jsonl" | "stderr.log", text: string) {
		fs.appendFileSync(path.join(this.executionDir, name), text);
	}
	finish(outcome: Record<string, unknown>, agent: AgentConfig, cwd: string, config: LaunchConfig) {
		this.metadata = { ...this.metadata, endedAt: new Date().toISOString(), ...outcome };
		this.save();
		this.saveWorker(agent, cwd, config);
	}
	private saveWorker(agent: AgentConfig, cwd: string, config: LaunchConfig) {
		saveJSON(path.join(directory(this.reference.sessionFile), "worker.json"),
			{ sessionId: this.reference.sessionId, profile: profile(agent, cwd), ...config });
	}
	private save() {
		saveJSON(path.join(this.executionDir, "execution.json"), this.metadata);
	}
}
