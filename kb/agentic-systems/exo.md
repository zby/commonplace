---
description: "Exo as a running reflective self-improvement harness: a protected Rust substrate under a fully rewritable executor, allowlisted host control, and a rewind that preserves the record of what was tried"
type: kb/types/note.md
traits: [has-external-sources]
tags: [computational-model, tool-loop, self-improving-systems]
---

# Exo

**Evidence basis:** first-hand reading of the `exoharness/exo` checkout at commit [baa07f67](https://github.com/exoharness/exo/commit/baa07f6785547080d99bd2a7d3eab6d76b984e35) (2026-07-26), covering `README.md`, `docs/RSI.md`, `examples/exo/docs/SELF-CONTROL.md`, `crates/exoharness`, `typescript/harness`, and `examples/exo`. I did not run a live instance.

Exo is an MIT-licensed long-running personal agent and harness framework whose design goal is stated outright: give the agent maximum freedom to rewrite itself while supplying the minimum scaffolding needed to do that safely ([docs/RSI.md](https://github.com/exoharness/exo/blob/baa07f6785547080d99bd2a7d3eab6d76b984e35/docs/RSI.md)). Its memory subsystem is reviewed separately; this analysis covers the self-modification loop and the control surfaces built around it.

The project distinguishes *recursive* from *autocatalytic* self-improvement — using a complete version of a thing to build another complete version, as against merely using a technology to speed its own development — and argues that recursion "requires the system to carry its own state forward and to do so safely." That framing explains the architecture: nearly everything is mutable, and the machinery that carries state across a failed rewrite is the part that is not.

## A protected substrate under a rewritable executor

The Rust `exoharness` crate owns identity, ordered events, versioned artifacts, bindings, secrets, and sandbox lifecycle. The TypeScript executor owns prompt assembly, model calls, tool policy, memory, and compaction. The agent may rewrite the executor, its prompts, its tools, and its adapters; the harness is off-limits.

That boundary is a policy setting rather than an architectural necessity — "the system technically allows it, but to provide safer standard usage, it's disallowed on the default configuration" ([docs/RSI.md](https://github.com/exoharness/exo/blob/baa07f6785547080d99bd2a7d3eab6d76b984e35/docs/RSI.md)). A system that states where its mutable boundary falls *and* makes it configurable is unusual; most either freeze the boundary or leave it implicit.

## The self-modification loop

`SELF-CONTROL.md` enumerates eight capability areas and, for each, what exists versus what is missing ([examples/exo/docs/SELF-CONTROL.md](https://github.com/exoharness/exo/blob/baa07f6785547080d99bd2a7d3eab6d76b984e35/examples/exo/docs/SELF-CONTROL.md)). The loop they compose:

- **See.** The repository is mounted into the sandbox at `/workspace/exo`. `examples/exo/SELF.md` is a checked-in navigational self map whose path is injected each turn as `EXO_SELF_MAP`.
- **Edit.** Through the shell tool against the repo mount, with git as both change history and rollback mechanism.
- **Build and rerun.** The `guardian_action` tool wraps a host supervisor behind a strict allowlist — `status`, `build`, `start_services`, `stop_services`, `restart_services`, `restart_adapters`, `restart_scheduler`, `restart_all`, `logs` — and accepts no arbitrary shell. Restarts are deferred to a detached process so the requesting turn can finish and announce the reboot before it happens.
- **Validate.** Build, run the relevant tests, then restart and observe through `status`, logs, the reboot wakeup, and the event log.
- **Adopt.** Commit to git; restart services on the new build using a drain-and-marker flow rather than a blind kill.
- **Roll back.** `git revert`/`restore` for code, `rewind_sandbox` for filesystem state, `uninstall_agent_tool` for tools, `disable_adapter` for adapters.

Exo characterises this honestly as existing "as practice and primitives rather than as a single tool." The design principle behind it is that durable mutations go through named tools with clear schemas, because "a mutation path that bypasses the tools also bypasses the record."

## The rewind preserves the record of what was tried

Every message, tool request and result, lifecycle change, and artifact write becomes a UUIDv7-ordered event file. Sandbox rewind restores filesystem state and deliberately leaves that log intact, so "an agent that breaks itself, rewinds, and tries again can see what it already tried, instead of repeating the same mistake in a loop."

This is the most transferable idea in the system: separating the substrate that gets reverted from the record of the attempt that failed. A rollback that also erases the evidence converts a failed experiment into a repeatable one. The [memory-subsystem review](../agent-memory-systems/reviews/exo.md) develops the Commonplace version — keeping source snapshots and accepted review evidence outside any agent-authored projection that may be replaced. The append-only property here is API and storage discipline rather than cryptographic tamper-proofing.

## Control surfaces

Beyond `guardian_action`: `snapshot_sandbox`, `rewind_sandbox`, and `list_sandbox_snapshots` for environment control; `schedule_sandbox_task` plus list/cancel/delete for the scheduler; `list_conversation_events` and `list_adapter_events` for introspection over its own history; `install_agent_tool`/`uninstall_agent_tool` and `shell` for capability extension.

The turn loop bounds tool round-trips per turn via `maxToolRoundTrips`, but materialises all conversation events in order on every model round with no history window, token budget, or implemented compaction — a notable tension with the long-running ambition, and the [memory-subsystem review](../agent-memory-systems/reviews/exo.md) works through what it costs.

## Where the acceptance gate stops

The evaluation stage is genuinely reject-capable: a build failure or failing test blocks adoption. But its oracles are build success, test outcomes, and behaviour observed after restart, so a change that degrades the agent's judgment without breaking anything mechanical passes. The [memory-subsystem review](../agent-memory-systems/reviews/exo.md) traces the same shortfall per promotion target and finds the gradient runs the wrong way — the strongest promotions carry the lightest checks, with executable tools validated for module shape rather than for doing anything useful.

Exo names the missing piece itself:

> Gap worth closing eventually: a canary path — run the changed build against a cloned sandbox or forked conversation and compare behavior before adopting it on the live instance, instead of validating on the only copy of itself.

Validating on the only copy of itself is precisely the position a self-hosting compiler occupies. The compiler at least has a fixed-point check — recompile with itself, compare outputs — and Ken Thompson showed even that can be fooled. Here there is no analogue at all, which makes the canary less a refinement than the first tripwire.

## Placement

By the criteria in [self-improving systems](../notes/self-improving-systems-README.md), Exo is a running instance of a combination the casebook otherwise lacks: reflective, cumulative, and computationally autonomous at once. Its self-representation is unusually literal — the source tree it edits is the organisation that determines its behaviour, and the wire from artifact to behaviour is rebuild-and-restart. Its warrant is bounded by build, test, and immediate-behaviour oracles.

`docs/RSI.md` also stakes a position on the bitter lesson: "the hand-engineered harness is the next thing to fall, as models get smarter, they should have largely unfettered ability to modify their own harnesses rather than living inside one we froze for them." Read through [what scale actually selects against](../notes/bitter-lesson-selects-against-unearned-reach-not-against-structure.md), the architecture is a bet about *which* structure was earned: harness policy — how to assemble a prompt, which tools to expose, when to compact — is a set of design theories whose scope was asserted rather than tested, so Exo hands them to the agent. Canonical state, secrets, and sandbox lifecycle are kept because they have nothing left to be wrong about. Whether the protected set is drawn in the right place is the bet, and the default policy protecting `exoharness` is where it is currently drawn.

## What to watch

- Cloning and migration are documented as not yet built, and both the canary path and the rewind-and-retry story lean on them.
- Where the protected set settles. It is currently drawn by default policy rather than architecture, so the boundary can move in either direction — an agent granted harness access, or a substrate that grows as failures reveal what should not have been mutable.

---

Relevant Notes:

- [Exo agent memory system review](../agent-memory-systems/reviews/exo.md) — contains: the memory, skills, and context-assembly subsystem of this same system at the same revision
- [Theory-mediated self-improvement needs both interpretation and retention from one substrate](../notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md) — rationale: the substrate conditions this system supplies, and the evaluation condition its acceptance gate leaves to the model
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — rationale: the three stages this loop is read against
- [Warranted autonomy is bounded by oracle domain](../notes/warranted-autonomy-is-bounded-by-oracle-domain.md) — rationale: why build-and-test oracles bound which self-modifications this system can adopt unattended
- [Reflective system](../notes/definitions/reflective-system.md) — see-also: the declared-boundary requirement Exo's harness/executor split satisfies
