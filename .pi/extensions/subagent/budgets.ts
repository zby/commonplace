/** Static subtree budgets. Missing environment means a root, never a shared counter. */
export const DEPTH_ENV = "PI_SUBAGENT_DEPTH";
export const WORKERS_ENV = "PI_SUBAGENT_WORKERS";
export interface Budgets { maxDepth: number; maxWorkers: number }
export interface Limits { depth: number | null; workers: number; error?: string }

function integer(value: unknown, name: string): number {
	if (typeof value !== "number" || !Number.isSafeInteger(value) || value < 0)
		throw new Error(`${name} must be a nonnegative safe integer`);
	return value;
}
function environment(value: string, name: string): number {
	if (!/^(0|[1-9][0-9]*)$/.test(value)) throw new Error(`Invalid ${name}: expected a nonnegative integer`);
	return integer(Number(value), name);
}
export function readLimits(env = process.env): Limits {
	try {
		const depth = env[DEPTH_ENV];
		const workers = env[WORKERS_ENV];
		if (depth === undefined && workers === undefined) return { depth: null, workers: 4 };
		if (depth === undefined || workers === undefined) throw new Error("Subagent depth and worker environment budgets must both be present");
		const limits = { depth: environment(depth, DEPTH_ENV), workers: environment(workers, WORKERS_ENV) };
		if (limits.workers > 4) throw new Error(`${WORKERS_ENV} cannot exceed four slots`);
		return limits;
	} catch (error) { return { depth: 0, workers: 0, error: String(error) }; }
}
export function assertCanLaunch(limits: Limits) {
	if (limits.error) throw new Error(`Subagent launch refused: invalid inherited budget: ${limits.error}`);
	if (limits.depth === 0) throw new Error("Subagent launch refused: remaining depth is 0");
	if (limits.workers === 0) throw new Error("Subagent launch refused: remaining worker capacity is 0");
}
export function grant(limits: Limits, requested: Partial<Budgets>): Budgets {
	assertCanLaunch(limits);
	const depth = integer(requested.maxDepth ?? 0, "maxDepth");
	const workers = integer(requested.maxWorkers ?? 0, "maxWorkers");
	return {
		maxDepth: limits.depth === null ? depth : Math.min(depth, limits.depth - 1),
		maxWorkers: Math.min(workers, limits.workers - 1),
	};
}
