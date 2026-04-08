---
description: Python CLI that mines Claude Code transcripts into weighted user/guard profiles, benchmarks guards with per-model ablations, and compiles the result into assistant memory files
type: related-system
traits: [has-comparison, has-external-sources]
tags: [related-systems]
status: current
last-checked: 2026-04-07
---

# Synapptic

A Python CLI by Sorin Gheata / appcuarium that mines Claude Code session logs into a persistent user profile, synthesizes that profile into an archetype document, benchmarks extracted guards, and writes the result into assistant-specific memory surfaces such as Claude memory files, Cursor rules, Copilot instructions, and `AGENTS.md`. MIT licensed, beta-stage, with real implementation across filtering, extraction, profile merging, synthesis, output writing, and benchmarking rather than a README-only concept.

**Repository:** https://github.com/appcuarium/synapptic

## Core Ideas

**Heuristic transcript filtering before LLM extraction.** `filter.py` stream-parses Claude Code JSONL files, strips progress/system/tool/thinking records, keeps only user and assistant text, boosts likely correction/preference turns via keyword and short-reply heuristics, then truncates to a budget while preserving boosted turns plus adjacent context. This is a real preprocessing stage, not just "send the whole transcript to the model." The claimed property is signal concentration: cheaper extraction prompts and more pressure toward corrective moments rather than tool noise.

**Two-level weighted profile with dimension routing.** The durable learning substrate is not the final markdown archetype but the YAML profile store under `~/.synapptic/`: global profile, per-project profiles, per-session observations, and profile history snapshots. `config.py` defines nine dimensions; `profile.py` routes some to global, some to project-local, and promotes mixed dimensions globally once they recur across multiple projects. Similar observations reinforce via sequence-matching, old ones decay by merge cycle and wall-clock age, and low-weight items fall out. This is closer to a scored policy accumulator than to a note system.

**Narrative compilation into always-loaded context surfaces.** `synthesize.py` turns the weighted store into a three-part markdown artifact: `User Archetype`, `Guards`, and `Known Weaknesses`. `integrate.py` and `outputs.py` then compile that one internal representation into multiple assistant-specific files: Claude memory, Cursor MDC, Copilot instructions, Gemini styleguide, Codex `AGENTS.md`, and others. The important mechanism is not just "write markdown somewhere" but "compile one learned policy into several always-loaded surfaces with target-specific formatting."

**Per-guard ablation as the curation loop.** The strongest mechanism in the repo is the benchmark path. `benchmark.py` selects guards from the profile, generates adversarial test scenarios, compares WITH and WITHOUT conditions, runs controls, majority-votes across runs, and classifies each guard as effective, redundant, backfire, ineffective, untestable, or unclear. The result is not just a report: `record_model_verdicts(...)` writes per-model verdicts back into the profile, and `exclude_guards(...)` can mark guards as excluded so later synthesis omits them. This closes the loop between trace mining and prompt-policy maintenance.

**Automatic incremental processing plus a separate session-browser layer.** `install` copies a Claude skill, registers a SessionEnd hook, and writes a shell script that extracts the closed session, merges, and synthesizes in the background with PID locking. Separately, the optional `relay`/`index`/`run` commands add a local dashboard, SQLite index, WebSocket streaming, and token/cost tracking. These are real features, but they are adjacent to the learning loop rather than the learning loop itself. The repo is partly a memory compiler and partly a visibility sidecar for Claude sessions.

## Comparison with Our System

| Dimension | Synapptic | Commonplace |
|---|---|---|
| Learning trigger | Automatic SessionEnd hook or manual `ingest` | Human-authored notes plus explicit review/ingest workflows |
| Raw source | Claude Code JSONL session transcripts | Notes, sources, workshop artifacts, and explicit human judgment |
| Durable intermediate store | Weighted YAML profiles + per-session JSON observations | Markdown notes, sources, indexes, and workshop documents |
| Main promotion target | Prompt-policy artifacts (`user_archetype.md`, `AGENTS.md`, rules files) | Curated knowledge artifacts for navigation, reasoning, and reuse |
| Evaluation loop | LLM-judge guard ablation with per-model exclusion | Semantic review, deterministic validation, and human curation |
| Scope of learned knowledge | User preferences, AI failure patterns, behavioral guards | Broader conceptual, design, methodological, and comparative knowledge |
| Integration surface | Multi-assistant output writers | Repo-native KB plus agent navigation conventions |

**Where Synapptic is stronger.** Zero-friction behavioral learning. It is much closer to "the system notices and updates itself" than Commonplace is. The benchmark feedback path is especially strong: most memory systems extract rules and stop there, while Synapptic tests whether an extracted guard actually earns scarce prompt budget for a specific model. The multi-output compilation layer is also more operationally mature than our current always-loaded-context story.

**Where Commonplace is stronger.** Knowledge depth, inspectable reasoning, and verification quality. Synapptic compresses interaction traces into prompt policy; it does not build arguments, preserve evidence chains, connect ideas across domains, or separate naming from explanation. Its benchmark is a useful curation heuristic, but still an LLM-judge loop over generated scenarios, not a strong oracle. Commonplace's value lies in understanding and composable reasoning; Synapptic's value lies in automatic behavioral adaptation.

**The key difference is what gets promoted.** Commonplace promotes traces and sources into library artifacts meant to be traversed and recombined. Synapptic promotes traces into deployment-time behavior policy meant to shape the next session immediately. That makes it a much closer sibling to Pi Self-Learning than to our broader note system, but with a more explicit compilation and pruning loop.

## Borrowable Ideas

**Per-guard ablation before prompt promotion.** The most borrowable idea here. If we ever generate candidate behavioral rules or always-loaded memory artifacts from traces, we should not assume every extracted rule deserves budget. Synapptic's WITH/WITHOUT test shape is the clearest mechanism in this repo for deciding what survives. *Ready to borrow once we have a candidate rule-generation path.*

**One canonical profile compiling into many harness-specific outputs.** Keep one internal representation, then emit Claude memory, Cursor rules, Copilot instructions, or `AGENTS.md` as render targets rather than maintaining separate memories per tool. This fits our [always-loaded context](../always-loaded-context-mechanisms-in-agent-harnesses.md) note directly. *Ready to borrow if we ever build generated memory artifacts.*

**Cross-project promotion as a thresholded global-policy heuristic.** Synapptic's mixed dimensions become global only after recurrence across 2+ projects. That is a concrete answer to "when does local operational experience become portable policy?" for live-session learning. *Needs a use case first* — we do not yet mine enough project-specific operational traces for this threshold to matter.

**Cheap transcript filtering before expensive interpretation.** The filter stage is simple, inspectable, and aggressively targeted at corrective signal. If we ever mine agent transcripts, pre-filtering with correction/preference heuristics is a better starting point than feeding raw JSONL into a model. *Needs a use case first* — worthwhile only if we actually adopt transcript mining.

**Session-end hook as a bounded automation surface.** The hook is small, detached, PID-locked, and only processes the just-closed session. This is a pragmatic automation boundary: narrow enough to reason about, useful enough to remove friction. *Interesting pattern but low priority* — valuable if we automate workshop capture, not for the KB core today.

## Curiosity Pass

**The real learning substrate is the weighted profile, not the archetype prose.** The README emphasizes the final archetype document, but the code shows the durable mechanism lives in `profile.yaml` plus `model_verdicts` and exclusion flags. The markdown output is a compiled view over that store. This matters because the impressive-sounding "living profile" claim is partly real and partly rhetorical: the profile does evolve, but the final prose mostly rephrases already-scored observations into a friendlier format for prompt injection.

**The benchmark is stronger than most memory systems, but weaker than the repo framing suggests.** What property does it claim to produce? Reliable selection of guards that actually change behavior. It does partly achieve that. But the oracle is still soft: generated adversarial scenarios plus LLM-as-judge, not hard verification or a human-verified target. So the benchmark is best understood as policy pruning, not proof that the guard is objectively correct or universally useful.

**The simpler alternative is a hand-written `AGENTS.md` plus occasional cleanup.** That simpler path would capture much of the value for users who already understand their own preferences. Synapptic's extra complexity only earns its keep if the hidden-pattern discovery and model-specific exclusion loop actually surface things the user would not have written or would have written badly. The code supports that possibility, but does not by itself prove how often it happens.

**Even if it works perfectly, the ceiling is deploy-time behavior shaping, not deeper learning.** Synapptic can improve how an assistant works with a specific user, compress repeated mistakes into guards, and tune the prompt policy per model family. It cannot improve the model's base coding ability, derive deep conceptual knowledge, or guarantee cross-assistant transfer from a single input substrate. The current implementation still ingests only Claude Code transcripts, so the "works with everything" claim is output-universal more than input-universal.

**The relay/browser layer is a separate product vector.** The local dashboard, SQLite indexing, and relay-wrapped launches are useful and implemented, but they are orthogonal to the trace-to-policy learning loop. The repo may eventually split conceptually into two products: session observability and session-derived policy compilation. Right now they coexist, but the learning mechanism would still make sense without the browser, while the browser would still make sense without the learning loop.

## What to Watch

- **Does the input side catch up with the output side?** Right now Synapptic writes to many assistant surfaces but only mines Claude Code transcripts. The broader claim strengthens only if Cursor/Copilot/Codex traces become first-class inputs.
- **Do model-specific verdicts stay stable enough to trust?** If guard classifications swing heavily across provider, model version, or benchmark reruns, the per-model filtering story may become brittle.
- **Does archetype synthesis remain useful as the profile store grows?** The weighted YAML can scale better than the generated prose. If the prose becomes bloated or repetitive, the synthesis step may turn into prompt sludge over a good underlying store.
- **Does the browser/relay become the dominant use case?** If users adopt Synapptic mainly for session observability and token tracking, the learning loop may end up secondary despite being the repo's most novel mechanism today.

---

Relevant Notes:

- [Pi Self-Learning](./pi-self-learning.md) — closest sibling: both mine coding-session traces into future-session behavioral guidance, but Synapptic adds broader profile compilation and benchmark-based pruning
- [ClawVault](./clawvault.md) — another trace-to-artifact system, but centered on workshop artifacts and observation promotion rather than compiled prompt policy
- [Prompt ablation converts human insight into deployable agent framing](../prompt-ablation-converts-human-insight-to-deployable-framing.md) — Synapptic's WITH/WITHOUT guard benchmark is the clearest production-shaped ablation loop in this area
- [Always-loaded context mechanisms in agent harnesses](../always-loaded-context-mechanisms-in-agent-harnesses.md) — Synapptic is the strongest current example of compiling one learned profile into many always-loaded surfaces
- [Constraining during deployment is continuous learning](../constraining-during-deployment-is-continuous-learning.md) — Synapptic is a concrete example of deployment traces becoming durable symbolic behavior constraints
- [Session history should not be the default next context](../session-history-should-not-be-the-default-next-context.md) — Synapptic's filter/extract/merge path is a practical alternative to raw transcript inheritance
- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) — Synapptic likely belongs in the survey as a prompt-policy trace-mining system with an unusually explicit curation loop
