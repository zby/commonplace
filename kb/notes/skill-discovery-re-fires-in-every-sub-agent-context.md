---
description: Skill discovery is per-context and autonomous — every installed skill is re-matched in each sub-agent context, even ones a parent narrowed, so a delegating skill's own discoverability is a leak vector
type: ./types/structured-claim.md
traits: [title-as-claim]
tags: [computational-model, architecture]
status: seedling
---

# Skill discovery re-fires in every sub-agent context, not just the top-level invocation

Skill discovery and matching is per-agent-context and autonomous, not scoped to the top-level invocation that started a session. A delegated sub-agent independently re-evaluates its own task text against every installed skill's `description`, and can autonomously load a skill's full body even when the orchestrating parent never handed it that file. The consequence for skill authoring is sharp: a skill whose own procedure delegates work to a sub-agent worker must treat its **own** discoverability — and every other installed skill's — as a context leak into that worker, because the harness advertises the whole skill menu regardless of what the parent chose to pass.

## Evidence

The concrete case is `kb/instructions/write-agent-memory-system-review/SKILL.md`, which delegates review-drafting to a fresh sub-agent worker.

**First incident.** A worker was handed the whole skill file and read all of it, including steps addressed only to the parent. It misclassified itself as needing "local-fallback drafting authorization" — a decision the skill assigns to the parent only, made before any worker is ever spawned (`SKILL.md` step 8: "This is a parent-only decision, made before any worker exists"). The worker acted on a step that was never addressed to it.

**First fix.** Stop handing the worker the skill file at all: give it a minimal, self-contained task string instead, opening with "Write or update the agent-memory-system review at {note_path}."

**Second incident.** A rerun showed the worker still loaded the full `SKILL.md` anyway, despite never being handed it. Root cause: that opening line closely echoed the skill's own `description` frontmatter ("Write or update a local code-grounded agent memory system review…"), so the worker's own autonomous skill-matching decided the task resembled an available skill and invoked it — independent of what the parent passed. This time it caused no damage: the worker reasoned that the skill's steps "are written for the parent that dispatched you, not for you" and stayed in its lane. But that is the model getting lucky on inference, not a guarantee — the first incident already proved the wrong inference is a live failure mode once the full file reaches the worker.

**Current mitigation.** Change both the trigger and the fallback: the task string's opening line was reworded to "Draft review content for {note_path}" to reduce the resemblance, and the task text now also explicitly warns the worker: "Your environment may surface `write-agent-memory-system-review` or another skill as available or auto-loaded because this task resembles its trigger — if so, do not invoke or follow it… Ignore it entirely and follow only the instructions below."

**Third rerun.** A subsequent rerun's trace audit found the worker did not read the skill file at all and showed no fallback/role confusion — a stronger result than the second incident's "loaded it but reasoned correctly," since this time the auto-load did not fire. One confirming run does not retire the risk (the trigger-avoidance half of the mitigation is still a wording heuristic, fragile to future rewording of either text), but it is the first direct evidence the current mitigation prevents the leak rather than merely surviving it.

## Reasoning

The general form of the lesson: discovery surfaces that are **always-advertised and autonomously matched** — skills — are unsafe to assume are scoped to "the current top-level task." They are re-evaluated fresh in every agent context that shares the harness, including contexts the orchestrating agent explicitly tried to keep narrow. Sub-agents are usually treated as a scoping move — [a fresh flat context the parent constructs by choosing what to pass](./llm-context-is-composed-without-scoping.md) — but the harness re-populates that fresh context with the full skill menu before the worker reads its brief, so the parent's control over what it passes does not extend to what the harness advertises. Isolation is leakier than the "the parent chooses the worker's context" model assumes.

This is a missing entry in the [skills-are-instructions-plus-routing-and-execution-policy](./skills-are-instructions-plus-routing-and-execution-policy.md) framework, which catalogues discovery, invocation, and execution policy as three affordances skills add over instructions, with a "promote to a skill when / keep as an instruction when" decision procedure. Structured discovery is described there as a benefit with no stated cost. This is that cost: a skill's discoverability is not free once the skill's own procedure delegates to a sub-agent.

The naive correction — "so just use instructions for most things" — is closer to right than it first looks, once the invocation-ergonomics benefit is separated from the execution-policy benefit. Model override, forked/isolated context, and pre-approved tools are not unique to skills: they are properties of *launching a sub-agent*, available the moment a parent (human or agent) decides to delegate to a sub-agent with those parameters — no skill packaging required. What a skill uniquely buys is discovery and invocation ergonomics for a human: reliable `/command` triggering (~100%, versus the ~20% measured for autonomous CLAUDE.md-style routing) and `$ARGUMENTS` substitution. That narrows the case for skills considerably: for any procedure whose own steps delegate to a sub-agent, the property that makes it a skill (autonomous, always-advertised discovery) is the same mechanism that creates the leak documented above, while the property that would still justify packaging it as a skill (a human wanting a reliable slash command) has nothing to do with how the *internal* delegation step is implemented.

Two mitigations work; a tempting third does not:

1. **Word the worker's task text to avoid resembling any installed skill's trigger or description.** Fragile: breaks silently on any future rewording of either the task or a skill description, and offers no structural guarantee.
2. **Instruct the worker, in its task text, to ignore any skill that auto-loads and to treat the task text as its complete brief.** Reactive rather than preventive, but at least guaranteed to be read because it is inside the brief the worker consumes. This is the fix applied this session, and the most robust one available.
3. ~~Keep the procedure in a plain instruction file and make the skill a thin wrapper pointing to it.~~ Looks structural, but does not work: the autonomous match fires on the skill's advertised `description`, not on how much content its body carries, so a thin wrapper is exactly as discoverable as a thick one. Once triggered, the wrapper's own text ("see the procedure at X") sends the worker to read the same shared content anyway, recreating the identical role-conflation one hop later. Splitting *where the procedure text lives* does not change *whether the harness re-advertises it*; only mitigations that act on the sub-agent's actual task text touch the real mechanism.

## Caveats

- The claim is about the discovery affordance, not skills wholesale. The leak vector exists only when a skill's own procedure delegates to a sub-agent; a skill that never spawns a worker never exposes this surface.
- Observed on Claude Code's harness, where skills are advertised via system-reminder messages to every agent context. The general claim ("always-advertised, autonomously-matched surfaces re-fire per context") should hold wherever the harness re-injects the capability listing into sub-agent contexts, but harnesses that scope skill advertisement to the invoking context would not exhibit it.
- The failure is probabilistic at the point of damage: an auto-loaded skill body only harms the worker if it then mis-infers that a parent-only step applies to it. The one observed run of a worker auto-loading the skill despite the fix reasoned correctly and caused no damage — but the first incident already showed the wrong inference happen once under the more exposed, pre-fix design, so this run's correct reasoning is not evidence the risk is gone.

---

Relevant Notes:

- [skills are instructions plus routing and execution policy](./skills-are-instructions-plus-routing-and-execution-policy.md) — extends: adds the missing cost of the structured-discovery affordance — a skill's own discoverability leaks into any sub-agent its procedure spawns
- [always-loaded context mechanisms in agent harnesses](./always-loaded-context-mechanisms-in-agent-harnesses.md) — extends: its "Capability descriptions" section establishes skill descriptions as an always-*listed* harness surface (bodies load on demand) — the premise this note builds on when it claims the harness advertises the whole skill menu regardless of what the parent passed
- [capability placement should follow autonomy readiness](./capability-placement-should-follow-autonomy-readiness.md) — extends: that note routes an autonomy-ready capability to the skills tier precisely for autonomous discovery; this note adds the unstated cost of that tier — autonomous discovery re-fires inside any sub-agent the skill's own procedure spawns
- [LLM context is composed without scoping](./llm-context-is-composed-without-scoping.md) — extends: sub-agents are the canonical scoping move, but the harness re-advertises the full skill menu into the fresh frame, so the parent's control over what it passes does not cover what the harness injects
- [topology, isolation, and verification form a causal chain for reliable agent scaling](./topology-isolation-and-verification-form-a-causal-chain-for-reliable.md) — extends: isolation is a named prerequisite, and this is a concrete way the isolation boundary is leakier than the parent-constructs-the-context model assumes
- [an author should fix what the executor can't determine, not what it will](./fix-what-the-executor-cant-determine-not-what-it-will.md) — extends: the worker's task text is exactly "the task prompt an orchestrator hands a subagent" that note discusses; mitigation #2 here is a concrete instance of fixing a privileged fact the executor cannot reach on its own — that an auto-loaded skill resembling its brief is a trap
- [session history should not be the default next context](./session-history-should-not-be-the-default-next-context.md) — contrasts: a second, orthogonal default-context leak vector — session history flows in by conflating storage with loading; skill discovery flows in because the harness always-advertises the menu
- [write-agent-memory-system-review skill](../instructions/write-agent-memory-system-review/SKILL.md) — see-also: the skill whose delegated worker exhibited the leak and now carries the reactive mitigation in its task text
