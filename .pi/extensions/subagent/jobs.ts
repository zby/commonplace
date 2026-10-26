import { randomUUID } from "node:crypto";

export interface Job<T> {
	handle: string;
	label: string;
	slots: number;
	state: "running" | "cancelling" | "completed" | "failed" | "cancelled";
	result?: T;
	error?: string;
	order?: number;
	controller: AbortController;
	done: Promise<void>;
}

/** Session-local ownership. Settlements never reject; waiters own only their wait. */
export class Jobs<T> {
	private jobs = new Map<string, Job<T>>();
	private listeners = new Set<() => void>();
	private sequence = 0;
	private closed = false;

	constructor(readonly capacity = 4) {
		if (!Number.isSafeInteger(capacity) || capacity < 0 || capacity > 4) throw new Error("Worker capacity must be an integer from zero to four");
	}
	private activeSlots() { return this.select().filter(job => !job.order).reduce((sum, job) => sum + job.slots, 0); }
	private validateSlots(slots: number) {
		if (!Number.isSafeInteger(slots) || slots < 1 || slots > this.capacity)
			throw new Error(`Job requires ${slots} slots but worker capacity is ${this.capacity}`);
	}
	start(run: (signal: AbortSignal) => Promise<T>, failed: (result: T) => boolean, label = "subagent", slots = 1): Job<T> {
		if (this.closed) throw new Error("Subagent session is shutting down");
		if (this.jobs.size >= 128) throw new Error("128 retained handles; forget completed jobs before starting more");
		this.validateSlots(slots);
		if (this.activeSlots() + slots > this.capacity) throw new Error(`Worker capacity exhausted: ${this.activeSlots()}/${this.capacity} slots in use; job needs ${slots}`);
		const job: Job<T> = { handle: randomUUID(), label, slots, state: "running", controller: new AbortController(), done: Promise.resolve() };
		this.jobs.set(job.handle, job);
		job.done = Promise.resolve().then(() => run(job.controller.signal)).then(result => {
			job.result = result;
			job.state = job.controller.signal.aborted ? "cancelled" : failed(result) ? "failed" : "completed";
		}).catch(error => {
			job.error = String(error);
			job.state = job.controller.signal.aborted ? "cancelled" : "failed";
		}).then(() => {
			job.order = ++this.sequence;
			for (const notify of this.listeners) notify();
		});
		return job;
	}

	/** Blocking calls share ownership/capacity; interruption cancels their child. */
	async execute(run: (signal: AbortSignal) => Promise<T>, failed: (result: T) => boolean,
		label: string, signal?: AbortSignal, slots = 1): Promise<T> {
		this.validateSlots(slots);
		while (true) {
			if (this.closed) throw new Error("Subagent session is shutting down");
			if (signal?.aborted) throw new Error("Subagent call aborted");
			const active = this.select().filter(job => !job.order);
			if (this.activeSlots() + slots <= this.capacity) break;
			await this.wait(active, signal);
		}
		const job = this.start(run, failed, label, slots);
		const abort = () => this.cancel([job]);
		signal?.addEventListener("abort", abort, { once: true });
		if (signal?.aborted) abort();
		try {
			await job.done;
			if (job.error) throw new Error(job.error);
			if (job.result === undefined) throw new Error("Subagent returned no result");
			return job.result;
		} finally {
			signal?.removeEventListener("abort", abort);
			this.forget([job]);
		}
	}

	select(handles?: string[]): Job<T>[] {
		if (!handles) return [...this.jobs.values()];
		if (!handles.length || new Set(handles).size !== handles.length) throw new Error("Provide nonempty, distinct handles");
		return handles.map(handle => {
			const job = this.jobs.get(handle);
			if (!job) throw new Error(`Unknown subagent handle: ${handle} (handles do not survive reload/restart)`);
			return job;
		});
	}

	cancel(jobs: Job<T>[]) {
		for (const job of jobs) if (!job.order) {
			job.state = "cancelling";
			job.controller.abort();
		}
	}

	forget(jobs: Job<T>[]) {
		if (jobs.some(job => !job.order)) throw new Error("Cannot forget active jobs; cancel and wait first");
		for (const job of jobs) this.jobs.delete(job.handle);
	}

	async wait(jobs: Job<T>[], signal?: AbortSignal): Promise<Job<T>> {
		if (!jobs.length) throw new Error("No handles to wait for");
		return new Promise((resolve, reject) => {
			const cleanup = () => {
				this.listeners.delete(check);
				signal?.removeEventListener("abort", abort);
			};
			const abort = () => { cleanup(); reject(new Error("Subagent wait aborted; jobs continue running")); };
			const check = () => {
				const ready = jobs.filter(j => j.order).sort((a, b) => a.order! - b.order!)[0];
				if (ready) { cleanup(); resolve(ready); }
			};
			this.listeners.add(check);
			signal?.addEventListener("abort", abort, { once: true });
			if (signal?.aborted) abort(); else check();
		});
	}

	async shutdown() {
		this.closed = true;
		const jobs = this.select();
		this.cancel(jobs);
		await Promise.all(jobs.map(job => job.done));
		this.jobs.clear();
	}
}
