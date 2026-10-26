import { spawn } from "node:child_process";

/** Own one process until close, including cancellation escalation and pipe drain. */
export async function runProcess(
	command: string, args: string[], cwd: string, signal: AbortSignal | undefined,
	onStdout: (text: string) => void, onStderr: (text: string) => void,
	environment: NodeJS.ProcessEnv = {},
): Promise<{ exitCode: number; aborted: boolean; error?: string }> {
	if (signal?.aborted) throw new Error("Subagent was aborted before spawn");
	return new Promise((resolve) => {
		// Nested workers stay in their root coordinator's process group.
		const ownsGroup = process.platform !== "win32" && !process.env.PI_SUBAGENT_PROCESS_GROUP;
		const proc = spawn(command, args, {
			cwd, shell: false, stdio: ["ignore", "pipe", "pipe"], detached: ownsGroup,
			env: { ...process.env, ...environment, ...(ownsGroup ? { PI_SUBAGENT_PROCESS_GROUP: "1" } : {}) },
		});
		let closed = false;
		let aborted = false;
		let error: string | undefined;
		let timer: ReturnType<typeof setTimeout> | undefined;
		const kill = (kind: NodeJS.Signals) => {
			try {
				if (ownsGroup && proc.pid) process.kill(-proc.pid, kind);
				else proc.kill(kind);
			} catch (err) {
				if ((err as NodeJS.ErrnoException).code !== "ESRCH") onStderr(`\nCancellation: ${err}`);
			}
		};
		const abort = () => {
			if (closed || aborted) return;
			aborted = true;
			kill("SIGTERM");
			timer = setTimeout(() => { if (!closed) kill("SIGKILL"); }, 5000);
		};
		proc.stdout.setEncoding("utf8");
		proc.stderr.setEncoding("utf8");
		proc.stdout.on("data", onStdout);
		proc.stderr.on("data", onStderr);
		proc.on("error", err => { error = err.message; });
		proc.on("close", (code, exitSignal) => {
			if (closed) return;
			closed = true;
			if (timer) clearTimeout(timer);
			signal?.removeEventListener("abort", abort);
			if (aborted && ownsGroup && proc.pid) kill("SIGKILL");
			if (exitSignal) onStderr(`\nSubagent exited on ${exitSignal}`);
			resolve({ exitCode: code ?? 1, aborted, error });
		});
		if (signal?.aborted) abort();
		else signal?.addEventListener("abort", abort, { once: true });
	});
}
