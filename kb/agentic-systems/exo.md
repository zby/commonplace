---
description: "Exo as a running reflective self-improvement harness: a protected Rust substrate under a fully rewritable executor, allowlisted host control, and a rewind that preserves the record of what was tried"
type: kb/types/note.md
traits: [has-external-sources]
tags: [computational-model, tool-loop, self-improving-systems]
---

# Exo

**Evidence basis:** first-hand reading of the `exoharness/exo` checkout at commit [ef4cfe05](https://github.com/exoharness/exo/commit/ef4cfe057af02955a73c85beb6ab79e253253114) (2026-07-29), covering `README.md`, `docs/RSI.md`, `docs/Tools_and_Adapters.md`, `examples/exo/docs/SELF-CONTROL.md`, `crates/exoharness`, `crates/executor`, `typescript/harness`, and `examples/exo`. I did not run a live instance. Originally written against `baa07f67` (2026-07-26) and refreshed for the managed-tool, profile, adapter-delivery, and self-update surfaces added since.

Exo is an MIT-licensed long-running personal agent and harness framework whose design goal is stated outright: give the agent maximum freedom to rewrite itself while supplying the minimum scaffolding needed to do that safely ([docs/RSI.md](https://github.com/exoharness/exo/blob/ef4cfe057af02955a73c85beb6ab79e253253114/docs/RSI.md)). Its memory subsystem is reviewed separately; this analysis covers the self-modification loop and the control surfaces built around it.

The project distinguishes *recursive* from *autocatalytic* self-improvement — using a complete version of a thing to build another complete version, as against merely using a technology to speed its own development — and argues that recursion "requires the system to carry its own state forward and to do so safely." That framing explains the architecture: nearly everything is mutable, and the machinery that carries state across a failed rewrite is the part that is not.

## A protected substrate under a rewritable executor

The Rust `exoharness` crate owns identity, ordered events, versioned artifacts, bindings, secrets, and sandbox lifecycle. The TypeScript executor owns prompt assembly, model calls, tool policy, memory, and compaction. The agent may rewrite the executor, its prompts, its tools, and its adapters; the harness is off-limits.

That boundary is a policy setting rather than an architectural necessity — "the system technically allows it, but to provide safer standard usage, it's disallowed on the default configuration" ([docs/RSI.md](https://github.com/exoharness/exo/blob/ef4cfe057af02955a73c85beb6ab79e253253114/docs/RSI.md)). A system that states where its mutable boundary falls *and* makes it configurable is unusual; most either freeze the boundary or leave it implicit.

## The self-modification loop

`SELF-CONTROL.md` enumerates eight capability areas and, for each, what exists versus what is missing ([examples/exo/docs/SELF-CONTROL.md](https://github.com/exoharness/exo/blob/ef4cfe057af02955a73c85beb6ab79e253253114/examples/exo/docs/SELF-CONTROL.md)). The loop they compose:

- **See.** The repository is mounted into the sandbox at `/workspace/exo`. `examples/exo/SELF.md` is a checked-in navigational self map whose path is injected each turn as `EXO_SELF_MAP`.
- **Edit.** Through the shell tool against the repo mount, with git as both change history and rollback mechanism.
- **Build and rerun.** A single fixed-operation tool, `rebuild_and_restart_exo(reason)`, validates and builds, then defers restart to a detached guardian process so the requesting turn can finish and announce the reboot. Each call writes a durable update record — id, status, timestamps, agent and conversation identity, and a free-text reason — and its completion (succeeded or failed, with exit code) is appended to the canonical event log. The finer-grained `guardian_action` allowlist this replaced (`status`, `logs`, per-service restarts) moved to an operator-only CLI; if the rebuild fails, the record is durable and the previous binary keeps running.
- **Validate.** Build, run the relevant tests, then restart and observe through `status`, logs, the reboot wakeup, and the event log.
- **Adopt.** Commit to git; restart services on the new build using a drain-and-marker flow rather than a blind kill.
- **Roll back.** `git revert`/`restore` for code, `rewind_sandbox` for filesystem state, `manage_tool` removal for registry-installed tools, `disable_adapter` for adapters.

Exo characterises this honestly as existing "as practice and primitives rather than as a single tool." The design principle behind it is that durable mutations go through named tools with clear schemas, because "a mutation path that bypasses the tools also bypasses the record."

## The rewind preserves the record of what was tried

Every message, tool request and result, lifecycle change, and artifact write becomes a UUIDv7-ordered event file. Sandbox rewind restores filesystem state and deliberately leaves that log intact, so "an agent that breaks itself, rewinds, and tries again can see what it already tried, instead of repeating the same mistake in a loop."

This is the most transferable idea in the system: separating the substrate that gets reverted from the record of the attempt that failed. A rollback that also erases the evidence converts a failed experiment into a repeatable one. The [memory-subsystem review](../agent-memory-systems/reviews/exo.md) develops the Commonplace version — keeping source snapshots and accepted review evidence outside any agent-authored projection that may be replaced. The append-only property here is API and storage discipline rather than cryptographic tamper-proofing.

## Control surfaces

Beyond the rebuild tool: `snapshot_sandbox`, `rewind_sandbox`, and `list_sandbox_snapshots` for environment control; `schedule_sandbox_task` plus list/cancel/delete for the scheduler; `list_conversation_events` and `list_adapter_events` for introspection over its own history; and `shell` plus a managed tool registry for capability extension.

The registry (added at `ef4cfe0`) replaces free-form tool installation. `manage_tool` is the only write surface — install or remove — with `inspect_tools` as its read-only counterpart. A source is either a workspace-relative directory or a git repository pinned to an exact commit hash; installs are staged and validated — manifest, module load, schema, name collisions — before the lockfile is touched, replacements are atomic, and failed installs leave no partial state. The legacy `install_agent_tool`/`uninstall_agent_tool` pair survives behind a default-off flag. The docs state the boundary plainly: "Loading a tool is a trust decision, not a security boundary."

Which tools the model sees at all is now a **profile**: `bootstrap` exposes just `shell`, `inspect_tools`, `manage_tool`, and the rebuild tool — "enough to inspect, extend, and repair the system" — while the default `practical` adds the scheduler, adapter, sandbox, memory, todo, skill, and web modules. Profiles are curated tool sets, not trust levels. Outbound adapter messages also gained durable delivery states — queued, in-flight, delivered or failed, with up to three retries and retained failure records — and a conversation can attach an externally created sandbox through CLI-only attach/detach commands that record lifecycle events.

The turn loop bounds tool round-trips per turn via `maxToolRoundTrips`, but materialises all conversation events in order on every model round with no history window, token budget, or implemented compaction — a notable tension with the long-running ambition, and the [memory-subsystem review](../agent-memory-systems/reviews/exo.md) works through what it costs.

## Where the acceptance gate stops

The evaluation stage is genuinely reject-capable: a build failure or failing test blocks adoption. But its oracles are build success, test outcomes, and behaviour observed after restart, so a change that degrades the agent's judgment without breaking anything mechanical passes. The [memory-subsystem review](../agent-memory-systems/reviews/exo.md) traces the same shortfall per promotion target and finds the gradient runs the wrong way — the strongest promotions carry the lightest checks, with executable tools validated for module shape rather than for doing anything useful. The `ef4cfe0` registry strengthens the install-time mechanics — manifest, module load, schema, collisions — without changing that: these are shape oracles, not usefulness oracles.

Exo names the missing piece itself:

> Gap worth closing eventually: a canary path — run the changed build against a cloned sandbox or forked conversation and compare behavior before adopting it on the live instance, instead of validating on the only copy of itself.

Validating on the only copy of itself is precisely the position a self-hosting compiler occupies. The compiler at least has a fixed-point check — recompile with itself, compare outputs — and Ken Thompson showed even that can be fooled. Here there is no analogue at all, which makes the canary less a refinement than the first tripwire.

## Recursive, autocatalytic, reflective

`docs/RSI.md` opens by rejecting the loose use of "recursive self improvement" for what is really **autocatalysis** — a technology speeding its own development, as computers, the steam engine, and the Internet all did, and as an LLM writing GPU kernels for the next training run does. **Recursion** is reserved for the strong form: a complete version of a thing producing another complete version, "with minimal outside involvement."

That axis is not ours. Their distinction is about the *production relation* — what the loop emits, and how much of the system it constitutes. [Reflective](../notes/definitions/reflective-system.md) is about the *change pathway* — whether change routes through a causally connected representation of the system available to the system's own processes. The two come apart at their own paradigm case:

| | Not reflective | Reflective |
|---|---|---|
| **Autocatalytic** | a model writing kernels for the next training run | an agent mining its traces to speed one stage of its pipeline |
| **Recursive** | the self-hosting compiler | Exo |

The compiler regenerates itself completely and holds no representation of itself at all — it never analyses its own source, and every change through its history was searched for and judged by humans. So recursion in their sense does not imply reflection in ours, and reflection does not imply recursion: an agent that revises one of its own instruction files routes change through a self-representation without emitting a complete successor to anything.

"Recursive" also bundles two things our vocabulary keeps apart. *Complete version* corresponds, within reflective systems, to total coverage of the behaviour-determining organization; *minimal outside involvement* is actor allocation, reported per function rather than as a score. Exo is unusual in scoring well on both at once, which is what makes it a clean placement rather than a partial one.

Each vocabulary omits what the other carries. Theirs has no improvement criterion: read the definition literally and a system that regenerates itself into something worse is still recursive, which is why `SELF-CONTROL.md` has to reintroduce the requirement operationally as "self-modification needs a verification loop, or failed changes accumulate as corruption." Ours has no axis for completeness of regeneration — rebuilding an entire executor and editing one prompt sit in the same cell of the pathway profile.

The deeper difference is which variable is the objective. Exo asks how to give the agent maximum freedom to evolve itself while supplying minimal scaffolding to do it safely: autonomy is maximized, safety is the floor. Commonplace inverts the control direction, [since warranted autonomy is bounded by oracle domain](../notes/warranted-autonomy-is-bounded-by-oracle-domain.md) — warrant is the constraint and autonomy is whatever warrant licenses. That single difference predicts where each system spends its effort, and it explains why Exo's acknowledged gap is an oracle gap — build and test oracles do not reach judgment quality, and no further harness engineering makes them.

The comparison flatters Exo in one respect worth naming. Treating autonomy as a scalar to maximize makes its progress legible; [refusing the scalar](../notes/measuring-autonomy-well-enough-to-see-it-improve-is-an-open-problem.md) leaves Commonplace unable to demonstrate it is moving along the axis it claims to care about.

## Placement

By the criteria in [self-improving systems](../notes/self-improving-systems-README.md), Exo is a running instance of a combination the casebook otherwise lacks: reflective, cumulative, and computationally autonomous at once. Its self-representation is unusually literal — the source tree it edits is the organisation that determines its behaviour, and the wire from artifact to behaviour is rebuild-and-restart. Its warrant is bounded by build, test, and immediate-behaviour oracles.

`docs/RSI.md` also stakes a position on the bitter lesson: "the hand-engineered harness is the next thing to fall, as models get smarter, they should have largely unfettered ability to modify their own harnesses rather than living inside one we froze for them." Read through [the case-level conjecture that a structured method may lose when a requirement-to-objective proxy is used beyond its assessed scope](../notes/bitter-lesson-selects-against-unearned-reach-not-against-structure.md), the architecture is a bet about *which* structure has assessed scope: harness policy — how to assemble a prompt, which tools to expose, when to compact — is a set of design theories whose scope was asserted rather than tested, so Exo hands them to the agent. Canonical state, secrets, and sandbox lifecycle are kept because they have nothing left to be wrong about. Whether the protected set is drawn in the right place is the bet, and the default policy protecting `exoharness` is where it is currently drawn.

## What to watch

- Cloning and migration remain documented but not built — reverified at `ef4cfe0`. The overview documents still describe them as shipped: the [README](https://github.com/exoharness/exo/blob/ef4cfe057af02955a73c85beb6ab79e253253114/README.md) says Exo "can clone itself, and even manage a lineage of clones," and `docs/RSI.md` says canonical state "maintains full lineage across clones" — while `SELF-CONTROL.md` marks area 7 "*(not yet built)*" and records that even sandbox cloning, its prerequisite, is missing. No clone or spawn tool is registered in `typescript/harness`, and the new sandbox attach/detach is not this: it binds one existing external container to a conversation, bring-your-own environment rather than cloning-from-snapshot. The capability tables are the load-bearing documents here; watch whether the gap closes or the overview claim simply stands.
- Where the protected set settles. It is currently drawn by default policy rather than architecture, so the boundary can move in either direction — an agent granted harness access, or a substrate that grows as failures reveal what should not have been mutable.

---

Relevant Notes:

- [Exo agent memory system review](../agent-memory-systems/reviews/exo.md) — contains: the memory, skills, and context-assembly subsystem of this same system, still pinned to the earlier `baa07f67`
- [Theory-mediated self-improvement needs interpretation, retention, and independent read-back](../notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md) — rests-on: the operative-path functions Exo partly supplies and the independent evaluation its acceptance gate leaves to the model
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — rests-on: the three stages this loop is read against
- [Warranted autonomy is bounded by oracle domain](../notes/warranted-autonomy-is-bounded-by-oracle-domain.md) — rests-on: why build-and-test oracles bound which self-modifications this system can adopt unattended
- [Reflective system](../notes/definitions/reflective-system.md) — rests-on: the change-pathway criterion their production-relation vocabulary does not track, and the declared-boundary requirement their harness/executor split satisfies
- [Measuring autonomy well enough to see it improve is an open problem](../notes/measuring-autonomy-well-enough-to-see-it-improve-is-an-open-problem.md) — rests-on: why their scalar reading of autonomy is legible where our per-function profile is not
- [Increasing computational autonomy relocates human effort to the frontier](../notes/increasing-computational-autonomy-relocates-human-effort.md) — see-also: why raising autonomy is not, on our account, a path to removing the human
