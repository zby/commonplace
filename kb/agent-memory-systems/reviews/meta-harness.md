---
description: "Meta-Harness review: trace-learning harness search that uses logs, evaluations, proposer skills, and generated code to evolve memory and agent scaffolds"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
last-checked: "2026-06-04"
tags: [trace-learning]
---

# Meta-Harness

Meta-Harness, from Stanford IRIS Lab's `stanford-iris-lab/meta-harness` repository, is an end-to-end search framework for task-specific model harnesses: the code around a fixed base model that decides what to store, retrieve, present, and execute over repeated evaluation episodes. At the reviewed commit, the public release contains onboarding guidance plus two reference experiments: a text-classification memory-system evolution loop and a Terminal-Bench 2 agent-scaffold evolution loop.

**Repository:** https://github.com/stanford-iris-lab/meta-harness

**Reviewed commit:** [95175f70c758dd1145b395edfe8b67e6f9d80fbd](https://github.com/stanford-iris-lab/meta-harness/commit/95175f70c758dd1145b395edfe8b67e6f9d80fbd)

**Last checked:** 2026-06-04

## Core Ideas

**The memory unit is a harness candidate, not a user-facing note.** The README defines the search target as "task-specific model harnesses" that decide what to store, retrieve, and show while a fixed model works; the text-classification example makes that literal with generated `agents/*.py` memory systems implementing `predict`, `learn_from_batch`, `get_state`, and `set_state` ([README.md](https://github.com/stanford-iris-lab/meta-harness/blob/95175f70c758dd1145b395edfe8b67e6f9d80fbd/README.md), [reference_examples/text_classification/memory_system.py](https://github.com/stanford-iris-lab/meta-harness/blob/95175f70c758dd1145b395edfe8b67e6f9d80fbd/reference_examples/text_classification/memory_system.py), [reference_examples/text_classification/.claude/skills/meta-harness/SKILL.md](https://github.com/stanford-iris-lab/meta-harness/blob/95175f70c758dd1145b395edfe8b67e6f9d80fbd/reference_examples/text_classification/.claude/skills/meta-harness/SKILL.md)).

**A proposer agent writes code from retained run evidence.** Each `meta_harness.py` builds a prompt pointing to `evolution_summary.jsonl`, `frontier_val.json`, reports, and `pending_eval.json`, then calls Claude Code with a domain-specific skill. The skill tells the proposer to read prior results and traces, formulate hypotheses, implement candidates, and write a pending-evaluation manifest ([reference_examples/text_classification/meta_harness.py](https://github.com/stanford-iris-lab/meta-harness/blob/95175f70c758dd1145b395edfe8b67e6f9d80fbd/reference_examples/text_classification/meta_harness.py), [reference_examples/terminal_bench_2/meta_harness.py](https://github.com/stanford-iris-lab/meta-harness/blob/95175f70c758dd1145b395edfe8b67e6f9d80fbd/reference_examples/terminal_bench_2/meta_harness.py), [reference_examples/terminal_bench_2/.claude/skills/meta-harness-terminal-bench-2/SKILL.md](https://github.com/stanford-iris-lab/meta-harness/blob/95175f70c758dd1145b395edfe8b67e6f9d80fbd/reference_examples/terminal_bench_2/.claude/skills/meta-harness-terminal-bench-2/SKILL.md)).

**The write path is evaluation-gated.** Text-classification candidates are import-checked, benchmarked against validation splits, appended to an evolution summary, and compared on a Pareto frontier over accuracy and context length; Terminal-Bench candidates are import-checked, smoke-tested, benchmarked on Harbor jobs, and recorded with rollout metrics before the frontier is updated ([reference_examples/text_classification/benchmark.py](https://github.com/stanford-iris-lab/meta-harness/blob/95175f70c758dd1145b395edfe8b67e6f9d80fbd/reference_examples/text_classification/benchmark.py), [reference_examples/terminal_bench_2/meta_harness.py](https://github.com/stanford-iris-lab/meta-harness/blob/95175f70c758dd1145b395edfe8b67e6f9d80fbd/reference_examples/terminal_bench_2/meta_harness.py), [reference_examples/terminal_bench_2/scripts/run_eval.sh](https://github.com/stanford-iris-lab/meta-harness/blob/95175f70c758dd1145b395edfe8b67e6f9d80fbd/reference_examples/terminal_bench_2/scripts/run_eval.sh)).

**Context efficiency is an objective, not just a guardrail.** The text-classification benchmark measures `memory_context_chars` and computes a Pareto frontier for accuracy versus context length; the LLM wrapper truncates overly long prompts. Terminal-Bench tracks tokens, cost, turns, and context summarization behavior, but its frontier is pass-rate centered rather than context-budget centered ([reference_examples/text_classification/benchmark.py](https://github.com/stanford-iris-lab/meta-harness/blob/95175f70c758dd1145b395edfe8b67e6f9d80fbd/reference_examples/text_classification/benchmark.py), [reference_examples/text_classification/llm.py](https://github.com/stanford-iris-lab/meta-harness/blob/95175f70c758dd1145b395edfe8b67e6f9d80fbd/reference_examples/text_classification/llm.py), [reference_examples/terminal_bench_2/agents/baseline_kira.py](https://github.com/stanford-iris-lab/meta-harness/blob/95175f70c758dd1145b395edfe8b67e6f9d80fbd/reference_examples/terminal_bench_2/agents/baseline_kira.py)).

**The shipped examples are reference loops, not a generalized package API.** The root README calls this a cleaned-up paper-code release; the reusable path is an onboarding prompt that asks a coding assistant to produce a `domain_spec.md`, not a pip-installable framework with stable modules ([README.md](https://github.com/stanford-iris-lab/meta-harness/blob/95175f70c758dd1145b395edfe8b67e6f9d80fbd/README.md), [ONBOARDING.md](https://github.com/stanford-iris-lab/meta-harness/blob/95175f70c758dd1145b395edfe8b67e6f9d80fbd/ONBOARDING.md)).

## Artifact analysis

- **Storage substrate:** `files` `repo` - The durable behavior-shaping state is ordinary files in the example repositories: generated Python candidates under `agents/`, skills under `.claude/skills/`, prompt templates, JSON/JSONL logs, Harbor job directories, result files, frontiers, summaries, and config files.
- **Representational form:** `prose` `symbolic` - Skills, onboarding guidance, reports, hypotheses, prompts, and candidate descriptions are prose; Python harness code, configs, JSON manifests, results, frontier records, trajectory rows, and import paths are symbolic. I found no retained embeddings, fine-tuned weights, or other parametric memory artifacts in this release.
- **Lineage:** `authored` `imported` `trace-extracted` - Baseline harnesses, skills, prompts, configs, and onboarding rules are authored; benchmark datasets and Terminal-Bench tasks are imported; proposer sessions derive new code and manifests from evaluation traces, tool-call logs, predictions, rewards, costs, and prior frontier summaries.
- **Behavioral authority:** `knowledge` `instruction` `routing` `validation` `ranking` `learning` `enforcement` - Logs and reports provide evidence; skills and prompt templates instruct proposer and evaluated agents; `pending_eval.json`, import paths, and config route candidate evaluation; import checks, smoke tests, benchmark metrics, held-out/test splits, and Harbor verifiers validate or enforce eligibility; frontiers rank candidates; the outer loop learns by writing new harness code from retained traces.

**Candidate harness code.** In text classification, a generated candidate is a Python `MemorySystem` subclass. Its standing state can be serialized with `get_state`, restored with `set_state`, and read back during `predict`; the baseline `FewShotMemory` accumulates labeled examples in `learn_from_batch` and injects examples into later prompts ([reference_examples/text_classification/memory_system.py](https://github.com/stanford-iris-lab/meta-harness/blob/95175f70c758dd1145b395edfe8b67e6f9d80fbd/reference_examples/text_classification/memory_system.py), [reference_examples/text_classification/agents/fewshot_memory.py](https://github.com/stanford-iris-lab/meta-harness/blob/95175f70c758dd1145b395edfe8b67e6f9d80fbd/reference_examples/text_classification/agents/fewshot_memory.py)).

**Evolution history.** `evolution_summary.jsonl`, `frontier_val.json`, validation/test result files, reports, and Claude session logs are trace-extracted knowledge artifacts for the proposer. They do not directly bind the task model, but they determine what evidence the next proposer is told to inspect and which candidates are considered frontier systems ([reference_examples/text_classification/meta_harness.py](https://github.com/stanford-iris-lab/meta-harness/blob/95175f70c758dd1145b395edfe8b67e6f9d80fbd/reference_examples/text_classification/meta_harness.py), [reference_examples/text_classification/benchmark.py](https://github.com/stanford-iris-lab/meta-harness/blob/95175f70c758dd1145b395edfe8b67e6f9d80fbd/reference_examples/text_classification/benchmark.py)).

**Proposer skills and onboarding prompt.** The `.claude/skills/` files are high-authority prose instructions: they constrain what the proposer must read, how many candidates to produce, what overfitting to avoid, and how to write `pending_eval.json`. `ONBOARDING.md` is a reusable domain-spec elicitation prompt for adapting the framework to a new domain ([ONBOARDING.md](https://github.com/stanford-iris-lab/meta-harness/blob/95175f70c758dd1145b395edfe8b67e6f9d80fbd/ONBOARDING.md), [reference_examples/text_classification/.claude/skills/meta-harness/SKILL.md](https://github.com/stanford-iris-lab/meta-harness/blob/95175f70c758dd1145b395edfe8b67e6f9d80fbd/reference_examples/text_classification/.claude/skills/meta-harness/SKILL.md), [reference_examples/terminal_bench_2/.claude/skills/meta-harness-terminal-bench-2/SKILL.md](https://github.com/stanford-iris-lab/meta-harness/blob/95175f70c758dd1145b395edfe8b67e6f9d80fbd/reference_examples/terminal_bench_2/.claude/skills/meta-harness-terminal-bench-2/SKILL.md)).

**Terminal-Bench agent scaffold.** The KIRA baseline is a retained system-definition artifact: a full Python agent harness plus prompt template that changes tool calling, terminal execution, completion confirmation, image reading, context summarization, and trajectory recording for later evaluation ([reference_examples/terminal_bench_2/agents/baseline_kira.py](https://github.com/stanford-iris-lab/meta-harness/blob/95175f70c758dd1145b395edfe8b67e6f9d80fbd/reference_examples/terminal_bench_2/agents/baseline_kira.py), [reference_examples/terminal_bench_2/prompt-templates/terminus-kira.txt](https://github.com/stanford-iris-lab/meta-harness/blob/95175f70c758dd1145b395edfe8b67e6f9d80fbd/reference_examples/terminal_bench_2/prompt-templates/terminus-kira.txt)).

**Promotion path.** Meta-Harness promotes raw episode evidence into evaluation summaries, frontier records, pending-candidate manifests, generated code, and eventually optional final test evaluation. The strongest promotion crosses from trace-extracted knowledge artifacts into symbolic system-definition artifacts: a new memory system or agent scaffold that future model calls actually run.

## Comparison with Our System

Meta-Harness and Commonplace both treat files as behavior-shaping artifacts, but their centers differ. Commonplace writes durable, reviewable knowledge artifacts with collection contracts and validation. Meta-Harness writes executable harness variants and lets repeated task evaluation decide which retained system-definition artifacts survive.

Commonplace's trust model is source grounding and review; Meta-Harness's trust model is held-out performance. That makes Meta-Harness more directly optimization-oriented: it can discover unintuitive harness improvements if the evaluation loop is good. It also inherits benchmark risk: leakage, noisy metrics, expensive runs, and overfitting become the main governance problems.

The closest Commonplace analogue is not a note-writing workflow; it is a future review/agent-workflow optimizer that reads prior run traces, proposes changes to instructions or retrieval surfaces, and gates them through deterministic and semantic tests before promotion.

### Borrowable Ideas

**Candidate manifests as a review boundary.** Commonplace could require generated instruction or skill candidates to land first in a pending manifest with hypothesis, changed mechanism, and expected efficiency. Ready for workflows that already produce competing candidates.

**Pareto frontiers over quality and context cost.** The text-classification example records context length next to score. Commonplace could apply the same pattern to generated session briefs or retrieval bundles: better recall is not enough if context cost explodes. Ready once a repeatable retrieval eval exists.

**Trace-to-code promotion with explicit benchmarks.** Meta-Harness cleanly separates proposer creativity from evaluator authority. Commonplace should borrow that separation before allowing trace-extracted edits to instructions, validators, or routing rules. Needs a concrete benchmark target.

**Onboarding as a domain-fit gate.** `ONBOARDING.md` asks for task unit, fixed components, metrics, leakage risks, traces, and budget before implementation. Commonplace could use the same shape for deciding whether a proposed automation belongs in the KB or remains workshop research. Ready now.

**Do not borrow unrestricted proposer authority.** The text-classification proposer skill allows broad file and shell tools, and the Terminal-Bench proposer can create arbitrary agent code. Commonplace should keep generated system-definition artifacts behind narrower file ownership and review gates.

## Write side

**Write agency:** `manual` `automatic` - Humans author the baseline code, skills, configs, onboarding prompt, and initial domain setup; the automated loop asks a proposer agent to write new candidate code and manifests, then benchmark scripts update logs, summaries, result files, and frontier records.

**Curation operations:** `synthesize` `promote` - The proposer synthesizes new harness artifacts from prior stored traces, results, and hypotheses; the benchmark/frontier logic promotes candidates by validation score, pass rate, context length, smoke-test success, and optional final evaluation.

### Trace-learning

**Trace source:** `session-logs` `tool-traces` `event-streams` `trajectories` - Text classification records prediction traces, train/eval JSONL rows, prompt lengths, prompt hashes, memory states, validation/test results, frontier summaries, and Claude proposer sessions. Terminal-Bench records Harbor job trials, verifier rewards, agent metrics, costs, turns, trajectories, Claude proposer logs, and per-task frontier state.

**Extraction** - Extraction is split between deterministic scripts and the proposer agent. Deterministic code parses result directories into accuracy, pass-rate, cost, token, turn, and frontier summaries; the proposer skill instructs Claude to inspect the state files and traces, infer failure modes, prototype mechanisms, and write new code plus `pending_eval.json`.

**Learning scope:** `per-project` `cross-task` - Each reference experiment has its own run directories and candidates, but the retained evidence is reused across later iterations, datasets, tasks, candidates, and final evaluations within that experiment.

**Learning timing:** `staged` `offline` - The loop stages candidate creation, validation, benchmarking, frontier update, and optional final evaluation. It is not an online per-turn learner inside a live user conversation, even when an evaluated text-classification memory system has an online `learn_from_batch` mode.

**Distilled form:** `prose` `symbolic` - The durable distilled artifacts are hypotheses, reports, skill-following proposer outputs, JSON manifests/summaries/frontiers, Python candidate harnesses, and prompt templates.

On the trace-learning survey axes, Meta-Harness is a trace-to-system-definition optimizer. It is stronger than ordinary log summarization because the distilled artifact is executable harness code, but weaker as a general memory product because the release delegates much of the reasoning to Claude Code and domain-specific skills rather than exposing a reusable typed learning engine.

## Read-back

**Read-back:** `both` - The proposer pulls retained run history by reading the paths named in its prompt and skill, while evaluated memory/scaffold harnesses can push retained state into model invocations, such as few-shot examples in text-classification prompts or summarized Terminal-Bench handoff prompts after context compression.

**Read-back signal:** `coarse` `identifier` - Coarse push appears when a harness always injects its current stored examples or summarized state during prediction/continuation. Identifier-scoped pull appears in run-specific paths, candidate names, import paths, dataset/task directories, and frontier files that the proposer is instructed to inspect.

**Faithfulness tested:** `yes` - The system's central loop evaluates candidate harness behavior end to end against baselines, validation splits, smoke tasks, verifier rewards, context length, cost, and optional test results. This tests harness-level read-back effectiveness, though it does not attribute causal effect to individual remembered examples or trace-extracted code edits.

The important direction edge case is the proposer loop. `meta_harness.py` pushes only pointers and operating instructions into Claude Code; the actual retained evidence remains in files that the proposer must read. From the proposer agent's perspective, this is pull machinery guided by instruction, not automatic memory injection.

The evaluated harnesses are different. In text classification, `FewShotMemory.predict` formats stored examples into the prompt before the task model answers. Generated candidates can implement other storage and retrieval policies behind the same `MemorySystem` interface. In Terminal-Bench, the KIRA scaffold pushes chat history, terminal observations, completion checks, and summarization handoffs into subsequent model calls, but the outer evolution history is not automatically injected into evaluated agents.

Selection is mostly simple and inspectable in the shipped baselines: recent/all examples with a character cap for few-shot memory, run-name and file-path scoping for evolution state, and benchmark-frontier ranking for candidate selection. Precision, context dilution, and whether a generated candidate's memory mechanism is actually useful are runtime findings, not guaranteed by the framework.

## Curiosity Pass

**This is a memory-system generator as much as a memory system.** The most durable learned artifact is not a stored fact; it is a new piece of code that changes future storage and read-back behavior.

**The strongest safety boundary is the benchmark split.** Meta-Harness spends more design energy on leakage, held-out tests, and validation than on human review metadata. That is appropriate for repeated benchmark tasks but weaker for open-ended knowledge-base maintenance.

**The proposer has broad authority in the examples.** The text-classification skill explicitly allows writing three new systems and running prototype scripts; the Terminal-Bench skill delegates analysis and implementation to subagents. This is powerful, but it makes prompt discipline and file ownership part of the memory system's trust base.

**Context efficiency is observable but not deeply governed.** Text classification measures average memory context characters; Terminal-Bench records token/cost/turn metrics. Neither example has a typed context budget contract comparable to a KB collection/type system.

## What to Watch

- Whether the repository grows a reusable core package instead of per-example scripts; that would change the review from reference-experiment coverage to framework coverage.
- Whether future examples add source-grounded provenance for generated candidate mechanisms; that would make trace-to-code promotion more auditable.
- Whether proposer outputs are sandboxed to explicit file ownership; current example skills grant enough latitude that accidental edits are a real operational risk.
- Whether context-cost frontiers become standard across domains, including Terminal-Bench; that would make efficiency a first-class optimization target rather than an auxiliary metric.
- Whether generated candidates gain automatic ablations over individual memory components; that would strengthen the faithfulness claim beyond harness-level evaluation.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: Meta-Harness stores extensive run history, but much of it is pulled by the proposer rather than automatically injected.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: generated harness code, logs, skills, frontiers, and prompt templates carry different forms and authorities.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: logs, reports, evaluation summaries, and traces are evidence for later proposer decisions.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: generated Python harnesses, proposer skills, prompt templates, benchmark configs, and validation scripts shape future behavior directly.
- [Use trace extraction as meta-learning](../../notes/agent-memory-requirements/use-trace-extraction-as-meta-learning.md) - exemplifies: Meta-Harness converts prior run traces into revised harness code.
