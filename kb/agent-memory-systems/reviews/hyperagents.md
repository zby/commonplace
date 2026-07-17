---
description: "HyperAgents review: self-improving agent harness where trace-learning benchmark feedback promotes executable patch lineages"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-learning]
last-checked: "2026-06-04"
---

# HyperAgents

HyperAgents is Facebook Research's code release for self-referential self-improving agents. At the reviewed commit, it runs a meta agent inside Docker, lets that agent edit the agent codebase, saves the resulting git diff, evaluates the patched task agent on benchmark domains, records generation metadata and archive state, and replays selected parent lineages into later generations. It is best read as an outer-loop trace-to-code learning harness rather than as a semantic memory API, note store, or retrieval database.

**Repository:** https://github.com/facebookresearch/Hyperagents

**Reviewed commit:** [59a68f672dfb92c74aeb7e61535d776fb36e172d](https://github.com/facebookresearch/Hyperagents/commit/59a68f672dfb92c74aeb7e61535d776fb36e172d)

**Source directory:** `related-systems/Hyperagents`

## Core Ideas

**The durable memory is executable lineage.** Each generation creates a `gen_<id>/` folder, runs the meta agent, copies back `agent_output/model_patch.diff`, stores patch paths in `metadata.json`, and appends the generation id to `archive.jsonl` ([generate_loop.py](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/generate_loop.py), [utils/gl_utils.py](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/utils/gl_utils.py)). Later generations call `get_patch_files(...)` on the selected parent and apply the full patch chain before invoking or evaluating the next agent. The behavior-shaping memory is therefore a replayable diff lineage, not a recalled prose lesson.

**The meta agent edits the system that produces future agents.** `MetaAgent.forward(...)` gives the model the instruction to modify the supplied repository path with all local tools enabled; `run_meta_agent.py` then resets `domains/` edits and writes the diff against the base commit as `model_patch.diff` ([meta_agent.py](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/meta_agent.py), [agent/llm_withtools.py](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/agent/llm_withtools.py), [run_meta_agent.py](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/run_meta_agent.py), [utils/git_utils.py](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/utils/git_utils.py)). This makes code the promoted memory artifact.

**Evaluation supplies the promotion pressure.** The generic harness imports a candidate `TaskAgent`, runs it over domain datasets, writes per-task chat histories and `predictions.csv`, and reports scores such as accuracy; other domains add environment-specific reporting and Polyglot container tests ([domains/harness.py](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/domains/harness.py), [domains/report.py](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/domains/report.py), [domains/polyglot/harness.py](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/domains/polyglot/harness.py)). The generation is marked `valid_parent` only when evaluation ran and produced scores, except for the seed-patch case.

**Parent selection is archive-level routing.** The default selector can choose `random`, `latest`, `best`, `score_prop`, or `score_child_prop`; the default CLI setting is `score_child_prop`, which samples from valid candidates with score and child-count weighting ([utils/gl_utils.py](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/utils/gl_utils.py), [generate_loop.py](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/generate_loop.py)). The optional editable selector path runs `select_next_parent.py` inside a container, but that checked-in selector currently returns a random valid candidate after computing scores ([select_next_parent.py](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/select_next_parent.py), [utils/run_select_next_parent.py](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/utils/run_select_next_parent.py)).

**Context efficiency is filesystem pruning plus patch replay.** The system does not build a vector store, summary ladder, or relevance-gated memory prompt. It controls context volume by copying a reduced initial repo, pruning previous-output directories before container handoff, and applying selected patches as code state rather than concatenating the whole archive into the prompt ([utils/gl_utils.py](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/utils/gl_utils.py), [generate_loop.py](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/generate_loop.py)). One implementation wrinkle: `run_meta_agent.py` accepts an `--evals_folder` argument, but the checked-in `MetaAgent.forward(...)` does not include that path in its prompt, so prior outputs are present in the container but not explicitly surfaced to the meta agent by that argument.

**The ensemble mode reads saved outputs directly.** When ensemble optimization is enabled, `ensemble.py` loads `archive.jsonl`, picks the best-scoring generation for the requested domain/split, and returns that generation's saved prediction for the current question id ([ensemble.py](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/ensemble.py)). This is a retained-output read path, but it is not agent prompt memory.

## Artifact analysis

- **Storage substrate:** `files` — The central retained artifacts are output-directory files: `archive.jsonl`, per-generation `metadata.json`, patch files, chat histories, predictions, reports, copied repo trees, plots, and logs.
- **Representational form:** `prose` `symbolic` — Chat histories, prompts, reports, and generated README text are prose; patches, Python code, JSON metadata, CSV predictions, archive records, score fields, parent ids, and Docker/git commands are symbolic. The reviewed repo does not retain learned model weights or embeddings as its memory substrate.
- **Lineage:** `authored` `trace-extracted` — The starting code, domain harnesses, tools, prompts, and selectors are authored; meta-agent chat histories, task-agent histories, predictions, reports, generated diffs, archive state, and selected patch lineages are derived from agent runs and benchmark feedback.
- **Behavioral authority:** `knowledge` `instruction` `routing` `validation` `ranking` `learning` `enforcement` — Histories and reports are evidence; patches and edited code instruct future execution; parent ids, patch paths, score keys, and domain adapters route runs; reports and import checks validate candidates; scores and child counts rank candidate parents; the generation loop learns by turning trace/eval evidence into future executable code; Docker reset/clean, domain reset, and patch filtering enforce some boundaries.

**Patch chains.** `model_patch.diff` files are the strongest retained artifacts: they are replayed through `apply_diffs_container(...)`, committed inside the container, and become the code state seen by subsequent meta agents and evaluators ([utils/gl_utils.py](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/utils/gl_utils.py)). Their authority is system-definition authority over future behavior, but their provenance is coarse: the patch is tied to a generation, not to a specific source trace or failure span.

**Archive and metadata.** `archive.jsonl` records the evolving set of generations, while each `metadata.json` records parent id, previous and current patch files, evaluation flags, validity, optimize mode, and selectable status ([utils/gl_utils.py](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/utils/gl_utils.py), [generate_loop.py](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/generate_loop.py)). These symbolic records route future runs and determine which artifacts are eligible for selection.

**Evaluation artifacts.** Prediction CSVs, report JSON files, Polyglot per-instance outputs, and generated plots are knowledge artifacts for humans and ranking/validation artifacts for the loop ([domains/harness.py](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/domains/harness.py), [domains/report.py](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/domains/report.py), [analysis/visualize_archive.py](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/analysis/visualize_archive.py)). They can influence later parent choice and, if inspected by a meta agent, future edits.

**Promotion path.** HyperAgents promotes from raw traces and benchmark outputs to symbolic patches, then from patches to executable code state by parent selection and lineage replay. It does not promote traces into reviewed prose lessons, semantic indexes, validators with per-claim provenance, or model weights.

## Comparison with Our System

| Dimension | HyperAgents | Commonplace |
|---|---|---|
| Primary retained artifact | Generated patch lineage plus archive metadata | Typed Markdown notes, sources, instructions, indexes, and validators |
| Learning loop | Meta-agent edits code, benchmark evaluates, archive selects parents | Agents/humans write and revise artifacts, validation and reviews check them |
| Read-back | Selected patches are applied into future executable code | Agents search, load, and follow retained prose/symbolic artifacts |
| Context control | Filesystem pruning, reduced repo copies, patch replay | `rg`, indexes, links, collection contracts, review bundles |
| Governance | Import checks, benchmark scores, Docker cleanup, path filtering | Type specs, collection rules, deterministic validation, semantic review, git history |

HyperAgents is stronger than Commonplace at closed-loop mutation when a task has a cheap evaluator. The retained artifact does not just advise a future agent; it changes the code the future agent runs. That is a powerful form of memory when evaluation is reliable.

Commonplace is stronger at legibility and source-grounded governance. HyperAgents separates patches, metadata, reports, predictions, and histories, but it does not attach review status, source spans, or semantic rationale to individual patch changes. Commonplace keeps weaker automatic mutation, but the retained claims and instructions are easier to audit and invalidate.

### Borrowable Ideas

**Patch lineage as replayable memory.** Commonplace could use explicit patch-chain artifacts for any future automated maintenance loop, with each candidate mutation tied to the validation and review results that admitted it. Ready for narrow tooling experiments.

**Separate trace evidence from promoted authority.** HyperAgents keeps chat histories, predictions, reports, and patches on different surfaces. Commonplace trace-derived workflows should preserve that split: logs are evidence, candidate edits are proposals, accepted notes/instructions are authority. Ready now.

**Score-gated parent selection only transfers where the oracle is real.** HyperAgents can rank descendants because benchmark reports are cheap. Commonplace should borrow this only for operations with deterministic or reviewable success criteria, such as index regeneration, quote grounding, or schema validation.

**Avoid broad self-editing for KB work.** The meta agent can edit almost anything outside filtered `domains/` paths. Commonplace needs narrower file ownership and artifact contracts because note quality and instruction authority are not reducible to one score.

## Write side

**Write agency:** `manual` `automatic` — Users manually configure runs, domains, seed patches, and baseline modes; automatic paths create generation folders, run meta agents, write chat histories and diffs, evaluate candidates, update metadata, append archive entries, mark failed parents invalid, and write analysis outputs.

**Curation operations:** `synthesize` `invalidate` `promote` — The meta agent synthesizes new code patches from the current repo state and run context; failed parent-agent runs can invalidate a parent by setting `valid_parent: false`; selected/evaluated patches are promoted into future behavior when their lineages are replayed into later containers. I did not find code-grounded evidence for durable memory deduplication, consolidation, decay, or in-place evolution of existing memory entries.

### Trace-learning

**Trace source:** `session-logs` `tool-traces` `event-streams` `trajectories` — The raw signal includes meta-agent chat histories, task-agent chat histories, tool-mediated code edits, generated diffs, benchmark predictions, reports, environment/test outputs, generation logs, and archive trajectories.

**Learning scope:** `per-project` `cross-task` — A run is scoped to a generated project/output directory and selected domains, while the resulting code changes can transfer across later generations and across supported task domains when the same lineage is reused.

**Learning timing:** `offline` `staged` — Meta-agent editing, staged evaluation, full evaluation, archive append, parent selection, ensemble evaluation, and plotting are separate outer-loop stages. The checked-in task agent does not update a memory store online while solving a single task.

**Distilled form:** `symbolic` — The durable learned object is a git diff plus metadata and selection state. Chat histories and reports remain prose/symbolic evidence, but the behavior-changing distilled artifact is executable symbolic code.

**Extraction.** Extraction is mediated by the meta agent and benchmark oracle: the agent edits repository files; `run_meta_agent.py` captures the resulting diff; harnesses evaluate the patched agent; report files expose scores; metadata and selection policies decide whether the lineage remains selectable ([run_meta_agent.py](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/run_meta_agent.py), [generate_loop.py](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/generate_loop.py), [utils/gl_utils.py](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/utils/gl_utils.py)).

**Survey fit.** HyperAgents belongs with trace-derived artifact-learning systems: it turns agent/evaluation traces into executable system-definition patches rather than prose memories, vector indexes, or parametric weights. It strengthens the split between raw trace retention and promoted authority.

## Read-back

**Read-back:** `push` — The selected retained lineage reaches future agents by being applied into the repository before the next meta-agent run or evaluation; the receiving agent does not perform a memory lookup. The ensemble path reads archive predictions, but the ordinary self-improvement loop's behavior-changing memory is pushed as code state.

**Read-back signal:** `identifier` — Parent ids, metadata patch paths, archive entries, domain/split keys, and saved prediction ids determine which retained lineage or output is loaded. Applying the whole selected lineage is broad scope, not a separate coarse trigger.

**Faithfulness tested:** `no` — HyperAgents evaluates patched agents and ranks/selects candidates from reports, but I did not find a with/without lineage ablation or per-memory perturbation test proving that a particular replayed patch or trace-derived change caused the downstream behavior.

**Direction edge case.** Previous outputs are copied into the container and can be inspected as files, but the checked-in `MetaAgent.forward(...)` ignores the `eval_path` argument, so evaluation-history read-back is not reliably pushed into the prompt. Patch replay is the code-grounded read-back path.

**Selection, scope, and complexity.** Selection is generation-level rather than instance-level: parent selection chooses a lineage from valid archive candidates, and all patches in that lineage are applied. This avoids prompt bloat, but it can also hide stale or irrelevant inherited changes inside executable code.

**Authority at consumption.** Replayed patches have strong instruction/routing authority because they modify the code and prompts used by future agents. Evaluation reports and histories are advisory evidence unless a selector or meta agent consumes them. Docker cleanup and path filtering enforce some operational boundaries, not semantic truth.

**Other consumers.** Humans consume reports, plots, chat histories, predictions, patches, and archive visualizations. The ensemble path consumes saved predictions directly, and parent-selection utilities consume score reports and metadata.

## Curiosity Pass

**The `--evals_folder` argument is weaker than the architecture suggests.** The loop copies prior outputs and passes an eval folder to `run_meta_agent.py`, but the base `MetaAgent` prompt does not mention it. The system may still learn from prior outputs when a generated meta agent discovers them, but the checked-in prompt wiring is not a strong read-back channel.

**The memory is executable but not explanatory.** Patches are compact and behavior-changing, yet they do not say why they worked. A later agent can inherit a successful change without inheriting a reviewed rationale.

**The archive includes failed attempts.** Every attempted generation is appended before the next parent selection, while `valid_parent` controls eligibility. This is useful exploration history, but it means archive membership alone is not promotion.

**The editable parent selector is currently less selective than the default helper.** The main helper implements score-weighted choices; the editable `select_next_parent.py` computes candidates and scores but returns a random valid generation. That makes "selection policy can evolve" true as a capability, not as strong checked-in behavior.

## What to Watch

- Whether `MetaAgent.forward(...)` starts explicitly receiving and using the previous evaluation/archive path; that would strengthen trace read-back beyond patch replay.
- Whether patch files gain provenance links to chat-history turns, report failures, or benchmark examples; that would make trace-derived code changes auditable.
- Whether parent selection begins using explicit diversity, novelty, or child-count logic in the editable selector path rather than random valid choice.
- Whether evaluation adds lineage ablations, such as replayed-patch vs parent-patch baselines, to test faithfulness of pushed executable memory.
- Whether the system narrows meta-agent edit authority with stronger file contracts; broad self-editing is useful for research but risky for KB-like maintenance.

Relevant Notes:

- [Trace-learning techniques in related systems](../trace-learning-techniques-in-related-systems.md) - places: HyperAgents turns session/evaluation traces into executable patch lineages.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: HyperAgents activates memory through code-state replay rather than semantic prompt retrieval.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: patches, reports, metadata, histories, and selectors carry different forms and authority.
- [Use trace-derived extraction as meta-learning](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - frames: HyperAgents uses benchmark feedback and agent traces as an outer-loop learning signal.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: generated patches and selection code configure future agent behavior.
- [Behavioral authority](../../notes/definitions/behavioral-authority.md) - frames: replayed patches have stronger authority than advisory reports or chat histories.
