---
description: Staged trajectory-to-rule pipeline with ADD/EDIT/REMOVE/AGREE rule updates and eval-time prompt injection; all inspectable artifacts, no weights
type: ../types/agent-memory-system-review.md
traits: [has-comparison, has-external-sources]
tags: [related-systems, trace-derived]
status: current
last-checked: "2026-04-12"
---

# ExpeL

ExpeL is the AAAI 2024 research implementation of an LLM-agent learning loop that turns benchmark trajectories into a maintained rule list plus a retrievable trajectory store. The repo splits the work into three scripted stages — `train.py` gathers reflexion-style attempts, `insight_extraction.py` folds those attempts into rules, and `eval.py` runs agents with both rules and retrieved trajectories available at prompt time. Authored by Andrew Zhao, Daniel Huang, Quentin Xu, Matthieu Lin, Yong-Jin Liu, and Gao Huang at LeapLab, THU.

**Repository:** https://github.com/LeapLabTHU/ExpeL

## Core Ideas

**The learning pipeline is explicitly staged, not inline.** Three separate Hydra-configured entry points run in sequence: `train.py` drives the reflexion loop over benchmark tasks and saves trajectories and dicts to `logs/<benchmark>/expel/`; `insight_extraction.py` loads those pickled trajectories, runs cross-validation folds, and calls `create_rules(...)` to produce an insight pack; `eval.py` loads the insight pack and runs evaluation with the rule list injected via `rule_template` and trajectories retrieved via a FAISS vectorstore. Gathering and generalization never interleave within one run.

**`create_rules` is the heart of the system.** In `agent/expel.py`, this method walks training folds and calls `extend_rules(...)` with four distinct critique modes: compare-success-vs-failure per task, critique-all-successes-in-chunks, critique-all-failures-per-task, and critique-over-prior-reflections. Each LLM response is parsed by `parse_rules(...)` looking for `ADD`, `EDIT`, `REMOVE`, and `AGREE` operations, and `update_rules(...)` applies them to a list of `(text, count)` tuples.

**Rules have an explicit lifecycle with integer counters.** `update_rules` is concrete about semantics: `AGREE` increments the counter by 1; `EDIT` rewrites text and adds 1; `ADD` inserts a new rule at count 2; `REMOVE` decrements by 1 normally and by 3 when the list is over-full. Rules whose counter reaches zero are dropped; rules are then sorted by count descending. Operations referring to nonexistent rules are silently deleted, and attempts to `ADD` a rule whose text already matches an existing rule are also deleted — so the LLM cannot poison the list by repeating existing content.

**Episodic retrieval uses multiple query slices.** `setup_vectorstore` in `agent/expel.py` breaks succeeded trajectories and benchmark fewshots into typed Documents — `task`, `thought`, `step`, `action`, `reflection` — each tagged with env_name. `update_dynamic_prompt_components` then builds a FAISS store over one slice type selected by `fewshot_strategy` (`task_similarity`, `thought_similarity`, `step_similarity`, `action_similarity`, `rotation`, or `task_thought_similarity`), retrieves `num_fewshots * buffer_retrieve_ratio` candidates, and optionally reranks by `len`, `thought`, or `task`. Short trajectory variants are preferred, duplicates and self-matches are skipped, and the selected fewshots are spliced into the existing prompt message that contained the old fewshots.

**Reflexion is the inner engine, not the learning artifact.** `agent/reflect.py` still performs per-attempt verbal reflection between failed trials within a single task, exactly in the Reflexion style. Those reflections feed the next retry and are stored on the Trajectory object. ExpeL's contribution is what happens afterward: the `insight_extraction.py` pass consolidates all trajectories and reflections across tasks into a persistent rule set, so per-trial reflections become the input to a later cross-task generalizer rather than the final output.

**Persistence is pickled checkpoints, not a knowledge-base.** State lives in Python dicts pickled via `save_trajectories_log` and resumed via `load_trajectories_log`. The learned artifact is `rule_items_with_count` (a list of tuples) plus `cache_rules` keyed by cross-validation fold. There is no database, no markdown store, no typed notes — just pickle files plus prompt-time text rendering via `RULE_TEMPLATE`.

**The promotion target is text at prompt time.** Rules are rendered as a numbered list and prepended to the eval prompt via `insert_before_task_prompt()`; retrieved trajectories replace the static fewshots in the prompt history. Nothing in the reviewed source writes back into model weights or fine-tunes anything — the LLM is treated as a fixed oracle, called only through `langchain.chat_models.ChatOpenAI`.

## Comparison with Our System

ExpeL and commonplace both commit to inspectable text promotion, but operate at very different levels of structure. ExpeL maintains a single flat rule list tied to one benchmark; commonplace maintains a typed graph of notes with links, indexes, and workshop-vs-library layering.

| Dimension | ExpeL | Commonplace |
|---|---|---|
| Trace source | Repeated benchmark task attempts with success/failure outcomes | Human+agent editing, notes, links, workshop artifacts |
| Learned substrate | Numbered rule list + FAISS-indexed trajectory pool | Typed notes, links, ADRs, indexes, instructions |
| Update style | LLM-proposed `ADD`/`EDIT`/`REMOVE`/`AGREE` with integer counters | Human-directed edits with validation and review bundles |
| Oracle strength | Hard benchmark success/failure per task | Weak human judgment + local validation |
| Scope | Cross-task within one benchmark family | Cross-domain methodology KB |
| Persistence | Pickled checkpoints per run | Git-tracked markdown with structured frontmatter |
| Retrieval | FAISS over typed trajectory slices (task/thought/step/action/reflection) | Grep over frontmatter and links |

ExpeL is the stronger reference for automated consolidation with a cheap lifecycle. The four mutation verbs plus counters do real lifecycle work: recurring rules accumulate strength, weak ones decay out when counter hits zero, and repeated LLM assertions cannot trivially inflate the list because `ADD` of an existing rule is dropped.

Commonplace is the stronger reference for compositional knowledge. ExpeL's rules cannot link to each other, cannot cite sources, and cannot mature into typed artifacts — a rule is a free-text sentence with a counter, and that is all.

**Trace-derived learning placement.** The trace source is completed benchmark-task trajectories: `train.py` records success, failure, and reflection traces across HotpotQA, ALFWorld, WebShop, and FEVER, with trigger boundaries at per-task-attempt (for reflection) and per-cross-validation-fold (for rule extraction). Extraction pulls out per-task critiques that name specific mistakes or heuristics, and the oracle is the benchmark environment's success signal; the LLM also acts as a judge when generating `ADD`/`EDIT`/`REMOVE`/`AGREE` operations. The promotion target stays entirely in inspectable artifacts — the numbered rule list plus vectorstore-retrievable trajectories — with no path into model weights in the reviewed source. Scope is cross-task within one benchmark family; rule sets are not claimed to generalize across benchmarks, and each benchmark has its own `RULE_TEMPLATE`. Timing is strictly offline and staged: gather first, extract second, evaluate third, with explicit resume support in each stage. On [the survey's axes](../trace-derived-learning-techniques-in-related-systems.md), ExpeL sits in the trajectory-run pattern on axis 1 and in symbolic-artifact learning on axis 2, with "scored flat rules" as its artifact-structure subtype and "explicit CRUD verbs" as its maintenance path. The review reinforces the survey's existing placement rather than splitting a claim; no new subtype is warranted, though ExpeL remains the cleanest CRUD-verb example alongside G-Memory.

## Borrowable Ideas

**Separate gathering from generalization.** Ready now as a workshop pattern. ExpeL's three-script split maps cleanly onto a commonplace workflow: raw workshop notes during a task, a later consolidation pass that mines them into durable artifacts. This is cleaner than trying to decide promotion inline during a run.

**Mutation verbs with strength counters.** Ready now as a design pattern for any commonplace artifact that accumulates LLM-proposed updates. `ADD`/`EDIT`/`REMOVE`/`AGREE` is more auditable than whole-document synthesis, and the simple integer counter is enough to create real decay behavior without a full reputation system. The specific asymmetry — `REMOVE` removes 3 when the list is full but 1 otherwise — is a useful bit of pragmatic engineering worth remembering.

**Operation-level validation before applying updates.** Ready now as a defensive pattern. ExpeL silently drops `ADD` operations whose text matches an existing rule and drops `EDIT`/`REMOVE`/`AGREE` operations whose target rule doesn't exist. That is a lightweight way to harden an LLM-driven maintenance loop against degenerate proposals — worth mirroring anywhere we let an LLM mutate a structured list.

**Typed retrieval slices over one trace pool.** Needs a use case first. ExpeL's `task`/`thought`/`step`/`action`/`reflection` document types are all indexed together but filtered at query time. The pattern — one unified Document store, metadata-filtered per retrieval mode — is reusable anywhere we want multiple views over the same trace.

## Curiosity Pass

The headline claim is "LLM agents are experiential learners." Re-read against the code, the mechanism is narrower: ExpeL learns a *prompt prefix* from experience. The rule list and retrieved fewshots are both just strings concatenated into the eval-time prompt. Nothing about the agent's parameters, tool set, or reasoning procedure is changed by experience; what is changed is what the agent reads at the top of each turn.

That reframing matters because it bounds what the mechanism can achieve even if it worked perfectly. A maximally good rule list is bounded by the context it consumes and by the downstream LLM's ability to attend to it — which is why the follow-up "Not Always Faithful Self-Evolvers" paper finds that raw trajectories remain more behaviorally active than condensed rules. Compression into inspectable text is not the same as compression into behavior.

A simpler alternative worth noting: much of the counter-based lifecycle would work just as well as AGREE-only with periodic truncation. The asymmetric `REMOVE` weights and the banned-words filter in `parse_rules` hint that the team hit real robustness problems with LLM-generated operations, which is useful evidence for anyone tempted to let an LLM propose structured mutations without guardrails.

The genuine achievement is not that rules are learned — Reflexion already did verbal learning — but that ExpeL gives rules an *explicit maintenance protocol with inspectable state transitions*. That is rarer than it sounds.

## What to Watch

- Whether anyone extends ExpeL's rule-mutation protocol beyond benchmarks with clean success signals — the counter lifecycle depends on a strong oracle
- Whether the multi-slice retrieval surface (task/thought/step/action/reflection) matters in ablations, or collapses to task-similarity alone
- Whether later descendants keep the explicit CRUD verbs or drift back to full-document rewrites (as Dynamic Cheatsheet does)
- Whether flat rule lists eventually hit a ceiling and demand richer structure — typed rules, rule-to-rule links, or rule-to-trajectory provenance
- Whether the pickled-checkpoint persistence model shows up in any production descendant, or only survives in research code

---

Relevant Notes:

- [trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) — extends: ExpeL is the clearest trajectory-run CRUD-verb artifact-learning example and anchors the "scored flat rules" subtype
- [Reflexion](./reflexion.md) — sharpens: ExpeL embeds the Reflexion retry loop but adds a cross-task consolidation pass and explicit rule maintenance on top
- [trajectory-informed-memory-generation-self-improving-agents ingest](https://arxiv.org/html/2603.10600v1) — compares: both extract durable guidance from trajectories, but ExpeL exposes a concrete CRUD protocol in code
- [openclaw-rl: train any agent simply by talking ingest](https://arxiv.org/html/2603.10165v1) — contrasts: similar trace-ingestion instinct, opposite promotion target — OpenClaw-RL trains weights, ExpeL stays in prompt-visible text
- [deploy-time learning](../../notes/deploy-time-learning-is-the-missing-middle.md) — sharpens: ExpeL is a close non-weight artifact-learning analogue to deploy-time learning, although the repo packages it as an offline benchmark train/extract/eval pipeline
- [memory management policy is learnable but oracle-dependent](../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md) — sharpens: ExpeL's rule lifecycle depends on benchmark success as a strong oracle; the same mechanism would degrade under weaker signals
- [Ingest: Large Language Model Agents Are Not Always Faithful Self-Evolvers](https://arxiv.org/html/2601.22436v2) — evidence: evaluates ExpeL directly and finds raw trajectories remain more behaviorally binding than the condensed rule list
