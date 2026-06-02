---
description: "Self-improving agent harness that stores generated code patches, evaluation reports, archive metadata, and replays selected lineages into later agents"
type: ../types/agent-memory-system-review.md
tags: [trace-derived]
status: current
last-checked: "2026-06-02"
---

# HyperAgents

HyperAgents is Facebook Research's code release for self-referential self-improving agents. The inspected repository implements a generation loop that lets a meta agent edit the agent codebase, saves the resulting git diff as a patch artifact, evaluates the patched task agent across benchmark domains, records per-generation metadata and archive state, and later replays selected parent lineages into fresh containers. It is therefore best read as an experimental trace-to-code self-improvement harness, not as a general memory API or note store.

**Repository:** https://github.com/facebookresearch/Hyperagents

**Reviewed commit:** [59a68f672dfb92c74aeb7e61535d776fb36e172d](https://github.com/facebookresearch/Hyperagents/commit/59a68f672dfb92c74aeb7e61535d776fb36e172d)

## Core Ideas

**The durable memory is mostly patches plus archive metadata.** Each generation creates a `gen_<id>/` output directory, runs the meta agent in a Docker container, copies back `agent_output/model_patch.diff`, stores that path in `metadata["curr_patch_files"]`, evaluates the resulting task agent, and appends the generation id to `archive.jsonl` ([generate_loop.py](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/generate_loop.py), [utils/gl_utils.py](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/utils/gl_utils.py)). Later generations call `get_patch_files(...)` over the selected parent lineage and apply those patches before invoking or evaluating a new agent. The operative behavior-shaping artifact is the patch chain, not the saved chat log by itself.

**The meta agent can edit the system that produces future agents.** `MetaAgent.forward(...)` invokes `chat_with_agent(...)` with editing tools enabled and the instruction to modify the codebase at the supplied repository path ([meta_agent.py](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/meta_agent.py), [agent/llm_withtools.py](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/agent/llm_withtools.py), [agent/tools/edit.py](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/agent/tools/edit.py)). `run_meta_agent.py` then resets unwanted `domains/` edits and writes the diff against the base commit to `model_patch.diff` ([run_meta_agent.py](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/run_meta_agent.py), [utils/git_utils.py](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/utils/git_utils.py)). This makes code, not prose reflection, the main promoted artifact.

**Evaluation is the promotion signal, but promotion is permissive.** For ordinary domains, `domains.harness` imports the candidate `TaskAgent`, runs it over a dataset, writes `predictions.csv`, and `domains.report` derives accuracy and label reports ([domains/harness.py](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/domains/harness.py), [domains/report.py](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/domains/report.py)). For Polyglot, the harness copies the generated task agent into per-instance containers, captures patches against target repositories, runs tests, and writes per-instance JSON plus an aggregate report ([domains/polyglot/harness.py](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/domains/polyglot/harness.py), [domains/polyglot/report.py](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/domains/polyglot/report.py)). The generation is marked `valid_parent` only if evaluation ran and produced scores or if seed meta patches are present, but every attempted generation is still appended to the archive before the next parent is selected.

**Parent selection is score-mediated lineage replay.** The default parent selector filters invalid parents, reads validation or training scores from report files, optionally discounts staged evaluations, penalizes heavily explored parents, and samples a parent by score/child-count weighting ([utils/gl_utils.py](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/utils/gl_utils.py)). The optional editable selector path runs `select_next_parent.py` inside a container after applying the latest selectable lineage, allowing the parent-selection policy itself to become part of the evolving system ([generate_loop.py](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/generate_loop.py), [select_next_parent.py](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/select_next_parent.py), [utils/run_select_next_parent.py](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/utils/run_select_next_parent.py)).

**Context efficiency is mostly filesystem pruning and patch replay, not semantic retrieval.** Before invoking a meta agent, the loop copies previous generation outputs into the container and prunes current-generation folders, validation/test outputs, copied worktrees, compiled files, and selected val/test files ([generate_loop.py](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/generate_loop.py)). `setup_initial_gen(...)` also copies a reduced repository into `gen_initial/`, excluding large or irrelevant directories and writing a compact README that describes the self-improvement objective ([utils/gl_utils.py](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/utils/gl_utils.py)). There is no vector store, top-k memory search, summarizer, or relevance-gated prompt injection; the system controls volume by pruning files and controls behavior by applying selected patches.

**The ensemble path treats archive outputs as a prediction store.** When ensemble optimization is enabled, `ensemble.py` loads `archive.jsonl`, finds the best-scoring generation for the requested domain/split, and returns that generation's saved prediction for the current question id ([ensemble.py](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/ensemble.py), [utils/run_ensemble.py](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/utils/run_ensemble.py)). This is another behavior-shaping read path over retained artifacts, but it is selection over saved predictions rather than agent memory loaded into an LLM context.

## Artifact analysis

- **Storage substrate:** `files` — Filesystem patch files under generation output directories, referenced from per-generation `metadata.json`
- **Representational form:** `symbolic` — Symbolic unified diffs over the Python/code repository

**Generated patch files.** Storage substrate: filesystem patch files under generation output directories, referenced from per-generation `metadata.json`. Representational form: symbolic unified diffs over the Python/code repository. Lineage: generated by a meta-agent editing session, filtered by `reset_paths_to_commit(...)` for `domains/`, extracted by git diff against the lineage base commit, and later filtered again before patch application. Behavioral authority: system-definition artifacts with direct code authority; when replayed into a container they define the task agent, meta agent, ensemble code, or optional parent selector that future runs execute.

**Archive and metadata.** Storage substrate: `archive.jsonl` and `gen_<id>/metadata.json` files in the generation output directory. Representational form: symbolic JSON. Lineage: produced by the generation loop from run configuration, patch paths, parent ids, evaluation status, and score availability. Behavioral authority: system-definition artifacts for routing and ranking because parent selection, lineage patch replay, validity filtering, staged-evaluation adjustment, and ensemble selection read them before deciding what code or prediction receives future authority.

**Evaluation outputs.** Storage substrate: per-generation evaluation directories containing `predictions.csv`, `report.json`, Polyglot per-instance JSON, eval logs, and chat histories. Representational form: mixed symbolic tables/JSON and prose logs. Lineage: produced by benchmark harnesses from candidate task-agent executions and domain-specific graders or tests. Behavioral authority: knowledge artifacts when used as evidence about a generation; system-definition artifacts when report scores drive parent selection or ensemble routing.

**Meta-agent and task-agent chat histories.** Storage substrate: Markdown files copied from container output directories, including `meta_agent_chat_history.md` and per-task histories. Representational form: prose/tool transcript. Lineage: raw session traces from LLM calls and tool outputs. Behavioral authority: mostly knowledge artifacts for audit and debugging at this commit. The code copies prior generation outputs into the next container, but the default `MetaAgent.forward(...)` instruction does not explicitly name `eval_path`, and no implemented retriever selects chat-history snippets into the prompt, so their effective future authority is not established from code.

**Generated README and copied working repository.** Storage substrate: copied git worktrees under generation output directories. Representational form: mixed prose README plus symbolic source files. Lineage: assembled by `setup_initial_gen(...)` from the current repository with exclusion rules and generated README text. Behavioral authority: system-definition artifacts for the meta agent because the copied repository is the code substrate it edits and the README tells an inspecting agent what the self-improvement task is.

Promotion path: HyperAgents promotes from raw session/evaluation traces to symbolic patches, then from patches to executable code through lineage replay. It has a weak governance path from evaluation reports to `valid_parent` and score-based selection, but no explicit reviewer state, patch rationale schema, lineage pointer from each diff hunk to the inducing trace, or retirement/supersession model beyond parent selection and git history.

## Comparison with Our System

| Dimension | HyperAgents | Commonplace |
|---|---|---|
| Primary substrate | Generation output directory plus copied git worktrees and Docker containers | Git-tracked Markdown KB with typed notes, instructions, reviews, sources, ADRs, indexes, scripts |
| Main retained artifact | Generated code patches referenced by archive metadata | Typed knowledge artifacts and system-definition artifacts |
| Raw evidence | Chat histories, predictions, report files, per-instance test/eval outputs, logs | Source snapshots, notes, review reports, validation output, workshop artifacts |
| Representational form | Symbolic diffs/JSON/CSV plus prose transcripts | Mostly prose with structured frontmatter, links, schemas, commands, validators |
| Activation | Score-selected parent lineage patches replay into a fresh executable codebase | Agent navigation, explicit instructions, validation, review gates, generated indexes |
| Context control | Filesystem pruning, copied archives, staged evaluation, patch chains | Lexical search, directory indexes, authored links, type contracts, scoped skills |
| Governance | Evaluation score gates and valid-parent flags | Status, validation, source grounding, review comments, explicit archival conventions |

HyperAgents is stronger than Commonplace on closed-loop behavior mutation. It does not merely remember that an approach worked; it can convert a meta-agent editing session into a patch, evaluate that patch, and replay selected lineages into new executable agents. Commonplace's retained artifacts usually advise or constrain future agents; HyperAgents makes the retained artifact executable by default.

Commonplace is stronger on retained-artifact legibility and governance. HyperAgents has good operational separation between patches, metadata, reports, predictions, chat histories, and plots, but the durable patch artifact does not carry an embedded rationale, source-trace pointer, reviewer state, confidence, supersession relation, or invalidation rule. In Commonplace vocabulary, HyperAgents gives system-definition authority to diffs whose lineage is visible procedurally in output directories but not encoded as a durable artifact contract.

The central design divergence is read-back. Commonplace generally asks an agent to navigate stored knowledge. HyperAgents reconstitutes a selected parent by applying patch files before the agent runs. That is behavior activation through code substrate, not prompt-time memory retrieval. It avoids prompt dilution, but it also makes patch quality and evaluation coverage load-bearing.

**Read-back:** `push` — For selected code lineage replay, weak pull affordance for copied archive evidence, and no implemented relevance-gated memory injection into a receiving agent context

### Borrowable Ideas

**Patch chains as executable memory.** Ready as a comparison pattern, not a default KB mechanism. Commonplace could treat successful repeated procedures as candidates for promotion into scripts, validators, or skills, but only with explicit source evidence, review status, and rollback.

**Keep raw traces, reports, patches, and route metadata separate.** Ready now. HyperAgents is most understandable when chat histories, evaluation reports, `model_patch.diff`, `metadata.json`, and `archive.jsonl` are classified as different retained artifacts with different authority.

**Score-mediated parent selection as a retrieval analogue.** Needs a use case first. Commonplace could borrow the idea that not every retained behavior should remain equally likely to generate successors, but KB methodology probably needs review quality, source freshness, and authority class as ranking signals rather than benchmark score alone.

**Staged evaluation before expensive full activation.** Ready as an operational pattern. HyperAgents runs smaller checks before fuller evaluation in several paths. Commonplace already has deterministic validation and semantic review; a similar staged budget could decide when an artifact earns stronger routing or instruction authority.

**Do not borrow patch authority without artifact contracts.** HyperAgents shows why executable memory needs explicit lineage and governance. Before Commonplace lets generated code or instructions mutate future behavior automatically, the promoted artifact should record the source trace, oracle, reviewer, validity scope, supersession state, and rollback path.

## Trace-derived learning placement

**Trace source.** HyperAgents qualifies as trace-derived learning. The raw signals are meta-agent editing sessions, task-agent chat histories, benchmark predictions, domain reports, Polyglot test outcomes, generation logs, parent-selection metadata, and archive trajectories. The trigger boundary is one generation: select a parent, replay its lineage patches, run the meta agent, capture a new diff, evaluate it, and update metadata/archive state.

**Extraction.** The extraction step is code-oriented. `run_meta_agent.py` captures the repository diff after the meta agent edits the codebase; `generate(...)` records the patch path and evaluates it; `domains.report`, Polyglot reports, and `get_score(...)` convert run outputs into scalar scores; `select_parent(...)` or `select_next_parent_container(...)` chooses which lineage will seed the next generation. The oracle is therefore a mix of benchmark score availability, staged/full evaluation, valid-parent metadata, and parent-selection policy.

**Storage substrate.** Raw and derived artifacts live in the filesystem under `outputs/generate_<run_id>/`: generation folders, copied worktrees, `agent_output/`, chat histories, patch files, evaluation directories, reports, `metadata.json`, `archive.jsonl`, plots, and optional ensemble outputs. The active code substrate for a future generation is a Docker container with selected patches applied to a copied repository.

**Representational form.** Raw traces are prose/tool transcripts and logs. Predictions and reports are symbolic CSV/JSON. Archive and metadata are symbolic JSON. Generated patches are symbolic diffs. The copied repository is mixed prose and symbolic code. There is no distributed-parametric memory store in the inspected implementation; LLM calls produce artifacts, but no retained weights, embeddings, adapters, or learned rankers are stored by the system.

**Lineage.** The implemented lineage is parent id -> previous patch files -> patched container repository -> meta-agent editing session -> `model_patch.diff` -> evaluation report -> metadata/archive update -> future parent selection. This lineage is recoverable from generation directories and metadata, but it is not strongly encoded inside each patch: a diff does not itself name the source chat-history span, evaluation result, domain subset, scorer version, or reason it was accepted.

**Behavioral authority.** Raw chat histories and logs are knowledge artifacts at rest. Evaluation reports are knowledge artifacts when inspected, and system-definition artifacts when their scores route parent selection or ensemble choice. Patch files are system-definition artifacts because replaying them changes executable future behavior. Archive and metadata files have routing and ranking authority because they decide which patch lineage is activated.

**Scope and timing.** Scope is experiment-local and generation-local. Learning occurs between generations, not within a single task-agent answer. A selected lineage can transfer across domains only insofar as the patched code generalizes and the copied/evaluated domain set includes it. Polyglot adds nested per-instance software-engineering traces inside each generation, but those traces are summarized into result JSON and aggregate reports before influencing the outer loop.

**Survey placement.** On the [trace-derived survey](../trace-derived-learning-techniques-in-related-systems.md), HyperAgents is a trajectory-to-executable-code system. It strengthens the survey's distinction between raw traces and behavior-shaping distilled artifacts: chat histories and reports matter, but the durable learned object is the generated diff plus archive metadata that allows later patch replay. It also adds a non-prompt activation case: memory acts by reconstructing an executable codebase rather than by inserting text into the next LLM context.

## Curiosity Pass

**The meta agent's documented archive awareness is weaker in code than in concept.** `run_meta_agent.py` passes `evals_folder` into `MetaAgent.forward(...)`, but the inspected `MetaAgent.forward(...)` instruction only names the code repository path. The generated README inside copied worktrees says the system should look at previous agents and evaluation results, and the previous outputs are copied into the container, so archive use is afforded. It is not explicitly injected into the meta-agent prompt at this commit.

**The archive appends attempted generations before selection quality is fully clear.** The loop appends each generation id to `archive.jsonl`, then later parent selection filters by `valid_parent` and score availability. That keeps the exploration trace, but it means the archive is both a historical log and a candidate pool whose active subset is defined by metadata.

**Patches are powerful but thinly explained.** The system can preserve an executable improvement as a compact diff, which is far more behavior-direct than a lesson note. The cost is that the retained artifact is hard to audit without reconstructing the source trace and evaluation context.

**Context efficiency is externalized to the filesystem.** HyperAgents avoids a large prompt-memory subsystem by pruning copied directories and replaying patches into code. That is a practical context-engineering choice: the LLM sees a repository state, not a long concatenated memory. It also means invisible filesystem omissions and stale copied artifacts can shape what the meta agent can discover.

**The ensemble path is a memory system without agent reflection.** Selecting a saved prediction from the best archive member is a retained behavior surface, even though no LLM reads a memory item. It is a useful reminder that memory can act through routing and lookup, not only through prompt text.

## What to Watch

- Whether future versions explicitly pass archive paths, score summaries, or selected prior traces into the meta-agent prompt rather than relying on repository/README discovery.
- Whether patch artifacts gain source-trace lineage, acceptance rationale, domain/subset scope, scorer version, and supersession metadata.
- Whether the editable parent selector matures from an optional random baseline into a governed routing artifact with its own evaluation and rollback.
- Whether staged evaluation thresholds become domain-specific promotion gates rather than generic score availability checks.
- Whether generated patches are tested with ablations or lineage replay comparisons to identify which retained artifact actually caused improvement.
- Whether the safety warning around untrusted generated code turns into concrete sandbox, policy, or review gates before patch replay receives future authority.

---

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - extends: HyperAgents turns agent/evaluation traces into executable patch chains and archive routing metadata.
- [Designing agent memory systems](../../notes/designing-agent-memory-systems.md) - exemplifies: retained artifacts matter because they change future action, whether through prompt context, routing, or executable code replay.
- [Activate behavior-changing memory](../../notes/agent-memory-requirements/activate-behavior-changing-memory.md) - contrasts: HyperAgents activates memory through selected code lineage replay rather than relevance-gated prompt injection.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - grounds: HyperAgents requires separating patches, metadata, reports, chat histories, and copied repositories by substrate, form, lineage, and authority.
- [Deploy-time learning is the missing middle](../../notes/deploy-time-learning-is-the-missing-middle.md) - exemplifies: the system changes deployed behavior by mutating inspectable code artifacts without fine-tuning the base LLM.
