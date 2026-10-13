/** Fresh-process delegation with one session-local owner for every launch. */
import * as path from "node:path";
import { StringEnum } from "@earendil-works/pi-ai";
import type { ExtensionAPI } from "@earendil-works/pi-coding-agent";
import { Text } from "@earendil-works/pi-tui";
import { Type } from "typebox";
import { discoverAgents, type AgentScope } from "./agents.ts";
import { Jobs, type Job } from "./jobs.ts";
import { launch, failed, output, summary, type SingleResult } from "./launcher.ts";

const overrides = {
	model: Type.Optional(Type.String({ minLength: 1, description: "Model override; otherwise inherit agent or parent model" })),
	thinkingLevel: Type.Optional(StringEnum(["off", "minimal", "low", "medium", "high", "xhigh", "max"] as const)),
};
const taskFields = {
	...overrides,
	agent: Type.String({ description: "Agent definition name" }),
	task: Type.String({ description: "Isolated worker handoff" }),
	cwd: Type.Optional(Type.String({ description: "Child working directory and project agent discovery root" })),
};
const parameters = Type.Object({
	...overrides,
	action: Type.Optional(StringEnum(["start", "status", "wait", "cancel", "forget"] as const)),
	handles: Type.Optional(Type.Array(Type.String(), { minItems: 1 })),
	agent: Type.Optional(taskFields.agent), task: Type.Optional(taskFields.task), cwd: taskFields.cwd,
	tasks: Type.Optional(Type.Array(Type.Object(taskFields), { minItems: 1, maxItems: 8 })),
	agentScope: Type.Optional(StringEnum(["user", "project", "both"] as const, { default: "user" })),
});

function jobReply(selected: Job<SingleResult>[], includeOutput = false) {
	return {
		content: [{ type: "text" as const, text: selected.map(job =>
			`${job.handle}: ${job.state} — ${job.label}${includeOutput ? `\n${summary(job.error ?? (job.result ? output(job.result) : "(still running)"))}` : ""}`,
		).join("\n\n") || "No active or retained jobs." }],
		details: { jobs: selected.map(({ handle, label, state, result, error }) =>
			({ handle, label, state, ...(includeOutput ? { result, error } : {}) })) },
		isError: includeOutput && selected.some(job => job.state === "failed" || job.state === "cancelled"),
	};
}

export default function (pi: ExtensionAPI) {
	let jobs = new Jobs<SingleResult>();
	pi.on("session_shutdown", async () => { await jobs.shutdown(); });
	pi.on("session_start", async () => { await jobs.shutdown(); jobs = new Jobs<SingleResult>(); });
	pi.registerTool({
		name: "subagent", label: "Subagent", parameters,
		description: "Delegate isolated tasks to fresh agents. Omit action for blocking single (agent/task) or parallel (tasks, max 8) calls. " +
			"action=start launches one job immediately and returns a handle. All modes share four active slots per session; nested coordinators own separate pools. " +
			"action=wait with handles returns the first finished selected result; remove its handle before waiting again. Interrupted waits leave jobs running. " +
			"status lists jobs; cancel requests termination; forget releases terminal results. Handle operations accept only action and handles; status may omit handles. " +
			"Shutdown/reload cancels jobs and loses handles. Project definitions are discovered from each child's cwd; select agentScope=project for Commonplace. " +
			"Model/thinking overrides apply per call or per task. There is no chain mode or automatic forwarding of outputs.",
		async execute(_id, params, signal, onUpdate, ctx) {
			const registry = jobs;
			if ("chain" in params) throw new Error("Chain mode is not supported; use explicit isolated handoffs");
			if (params.action && params.action !== "start") {
				if (Object.keys(params).some(key => !["action", "handles"].includes(key)))
					throw new Error("Handle operations accept only action and handles");
				if (params.action !== "status" && !params.handles) throw new Error("This action requires handles");
				const selected = registry.select(params.handles);
				if (params.action === "wait") return jobReply([await registry.wait(selected, signal)], true);
				if (params.action === "cancel") registry.cancel(selected);
				if (params.action === "forget") {
					registry.forget(selected);
					return { content: [{ type: "text", text: "Forgot handles: " + params.handles!.join(", ") }], details: undefined };
				}
				return jobReply(selected);
			}
			if (params.handles) throw new Error("Launches do not accept handles");
			if (params.action === "start" && (!params.agent || !params.task || params.tasks))
				throw new Error("Async start requires agent and task only, not tasks");
			const parallel = params.tasks !== undefined;
			if (parallel ? Boolean(params.agent || params.task) || !params.tasks!.length || params.tasks!.length > 8 : !params.agent || !params.task)
				throw new Error("Provide exactly one single job or one to eight parallel tasks");
			const scope: AgentScope = params.agentScope ?? "user";
			const requested = params.tasks ?? [{ agent: params.agent!, task: params.task!, cwd: params.cwd,
				model: params.model, thinkingLevel: params.thinkingLevel }];
			const prepared = requested.map(item => {
				const cwd = path.resolve(ctx.cwd, item.cwd ?? params.cwd ?? ctx.cwd);
				const discovery = discoverAgents(cwd, scope);
				const agent = discovery.agents.find(a => a.name === item.agent);
				if (agent?.configurationError) throw new Error(agent.configurationError);
				return { item, cwd, discovery, agent };
			});
			if (signal?.aborted) throw new Error("Subagent start aborted");
			const defaults = { model: ctx.model ? `${ctx.model.provider}/${ctx.model.id}` : undefined, thinkingLevel: ctx.thinkingLevel };
			const mode = parallel ? "parallel" : "single";
			const details = (results: SingleResult[]) => ({ mode, agentScope: scope,
				projectAgentsDir: prepared[0].discovery.projectAgentsDir, results });
			const run = (p: typeof prepared[number], jobSignal: AbortSignal, update?: (r: SingleResult) => void) => {
				if (!p.agent) throw new Error(`Unknown agent: "${p.item.agent}". Available agents: ${p.discovery.agents.map(a => a.name).join(", ") || "none"}.`);
				return launch(p.agent, p.item.task, p.cwd, defaults, {
					model: p.item.model ?? params.model, thinkingLevel: p.item.thinkingLevel ?? params.thinkingLevel,
				}, jobSignal, update);
			};
			const label = (p: typeof prepared[number]) => `${p.item.agent} @ ${p.cwd}`;
			if (params.action === "start") {
				const p = prepared[0];
				const job = registry.start(s => run(p, s), failed, label(p));
				if (ctx.hasUI) void job.done.then(() => ctx.ui.notify(
					`Subagent ${job.label}: ${job.state} (${job.handle})`, job.state === "completed" ? "info" : "warning",
				)).catch(() => { /* Disposed UI cannot reject background work. */ });
				return jobReply([job]);
			}
			const results = prepared.map(p => ({ agent: p.item.agent, agentSource: p.agent?.source ?? "unknown",
				task: p.item.task, cwd: p.cwd, exitCode: -1, messages: [], stderr: "",
				usage: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0, cost: 0, contextTokens: 0, turns: 0 },
			} as SingleResult));
			const emit = () => onUpdate?.({ content: [{ type: "text", text: parallel
				? `Parallel: ${results.filter(r => r.exitCode !== -1).length}/${results.length} done`
				: `${label(prepared[0])}: running` }], details: details([...results]) });
			await Promise.all(prepared.map(async (p, i) => {
				try {
					results[i] = await registry.execute(s => run(p, s, r => { results[i] = { ...r, exitCode: -1 }; emit(); }), failed, label(p), signal);
				} catch (error) {
					results[i] = { ...results[i], exitCode: 1, errorMessage: String(error) };
				}
				emit();
			}));
			return {
				content: [{ type: "text", text: results.map(r => `${r.agent} @ ${r.cwd}: ${failed(r) ? "failed" : "completed"}\n${summary(output(r))}`).join("\n\n") }],
				details: details(results), ...(results.some(failed) ? { isError: true } : {}),
			};
		},
		renderCall(args) {
			return new Text(`subagent ${args.action ?? (args.tasks ? "parallel" : "single")} ${args.agent ?? args.handles?.join(", ") ?? args.tasks?.map(t => t.agent).join(", ") ?? "all"}`, 0, 0);
		},
		renderResult(result, { expanded, isPartial }) {
			const data = result.details as { results?: SingleResult[]; jobs?: { result?: SingleResult }[] } | undefined;
			const results = data?.results ?? data?.jobs?.flatMap(j => j.result ? [j.result] : []) ?? [];
			const text = result.content.filter(c => c.type === "text").map(c => c.text).join("\n");
			const usage = results.map(r => `${r.agent}: ${r.usage.turns} turns, ↑${r.usage.input} ↓${r.usage.output}, $${r.usage.cost.toFixed(4)} ${r.model ?? ""}`).join("\n");
			const body = expanded ? text : text.split("\n").slice(0, 12).join("\n");
			return new Text(`${isPartial ? "Running\n" : ""}${body}${!expanded && text.split("\n").length > 12 ? "\n(expand for summary; full messages in tool details)" : ""}${usage ? `\n${usage}` : ""}`, 0, 0);
		},
	});
}
