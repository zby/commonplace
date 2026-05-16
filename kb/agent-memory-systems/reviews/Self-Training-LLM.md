---
description: "Wikipedia self-training pipeline that turns generated QA samples and hallucination scores into SFT/DPO datasets for weight updates, with no persistent memory artifact"
type: ../types/agent-memory-system-review.md
tags: [related-systems, trace-derived]
status: current
last-checked: "2026-04-20"
---

# Self-Training-LLM

[Self-Training-LLM](https://github.com/wj210/Self-Training-LLM) is a research codebase for factual self-training over Wikipedia. It generates or loads Wikipedia-grounded questions, asks a base or tuned model for answers, scores answer samples with NLI-style uncertainty and hallucination detectors, then turns filtered examples into SFT and DPO training data. It is useful for Commonplace as a trace-derived distributed-parametric learning contrast: the learned form is model weights, while the intermediate files are staging data rather than durable memory.

**Repository:** https://github.com/wj210/Self-Training-LLM  
**Reviewed commit:** https://github.com/wj210/Self-Training-LLM/commit/97839b29d0fd8bb474f5549fa3e9d6ca504732e0

## Core Ideas

### The learned form is weights, not memory

The README frames the project around dataset generation, SFT training, DPO training, response generation, and testing scripts rather than a deploy-time memory store ([README.md](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/README.md)). The training entrypoint loads answer pickles, filters examples, constructs SFT or DPO records, and delegates to TRL trainers ([uncertainty/train.py](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/uncertainty/train.py)). The training wrapper saves model checkpoints and optional merged adapters ([uncertainty/self_learning_training.py](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/uncertainty/self_learning_training.py)).

For Commonplace, this makes the system a negative example for agent memory and a positive example for trace-derived learning. The promotion target is a model checkpoint. The pickles, JSONL files, response logs, and caches are not maintained as a readable long-term knowledge base.

### The loop starts with corpus-grounded question manufacture

The generation script loads Wikipedia, filters article text, selects predefined topics, and asks OpenAI models to generate questions from document chunks ([uncertainty/wiki_generation.py](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/uncertainty/wiki_generation.py), [uncertainty/topic_generator.py](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/uncertainty/topic_generator.py), [uncertainty/templates.py](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/uncertainty/templates.py)). The default data config points at the Wikimedia Wikipedia snapshot ([configs/data/wiki.yaml](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/configs/data/wiki.yaml)).

This is not autonomous curiosity in the strong sense. The system does not discover open-ended goals from task execution. It manufactures factual QA opportunities from an external corpus and prompt templates, then uses model uncertainty to decide which opportunities are worth training on.

### Unknown selection is an oracle problem

The code's "unknown" signal is a scored relationship between a question, a reference or context answer, and sampled model answers. `NLIScorer` supports several scoring modes, including semantic consistency, SelfCheckGPT-style contradiction scoring, and a BSDetector path that combines NLI with optional self-reflection ([uncertainty/scorer.py](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/uncertainty/scorer.py)). Training then filters examples with `question_filtering_threshold` and `unknown_threshold` before constructing SFT or DPO datasets ([uncertainty/train.py](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/uncertainty/train.py)).

The useful abstraction is not the specific hallucination score. It is the separation between prompt validity and learning target selection. One threshold asks whether the question/answer pair is usable; another asks whether the model appears weak enough on that item to justify training.

### Preference data is built from answer consistency

For DPO, `get_dpo_sample` selects chosen and rejected answers from scored samples. With `ref_as_chosen`, the context or reference answer can anchor the chosen side. Without it, the system can choose among model samples based on hallucination or consistency scores; with multiple preference mode, it emits capped sets of chosen/rejected pairs ([uncertainty/scorer.py](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/uncertainty/scorer.py)). The supplied training script runs SFT then DPO with question filtering and reference-as-chosen enabled ([script/train.sh](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/script/train.sh)).

This resembles a memory operation only at the level of selection pressure. The system is deciding which generated traces become learning examples. It is not deciding what to store, link, retrieve, expire, or expose as context.

### Evaluation is pairwise LLM judging

The response script generates baseline, SFT, DPO, RAG, or DoLa-style outputs and writes JSONL response files ([uncertainty/generate_response.py](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/uncertainty/generate_response.py)). Pairwise evaluation compares baseline and post-training answers with a GPT-4o judge in both answer orders, then aggregates win/tie/lose counts and cost ([uncertainty/pairwise_eval.py](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/uncertainty/pairwise_eval.py)).

The project therefore uses soft judgment rather than a hard verifier. That is a reasonable fit for factual answer quality experiments, but it limits what Commonplace should borrow. A KB should not silently promote durable claims based only on pairwise LLM preference unless the result is explicitly marked as judged, reviewable, and reversible.

### The implementation is research glue with brittle defaults

The code is concrete enough to study, but it is not packaged as a robust reusable system. The default `--scoring_method` spelling in `wiki_generation.py` appears to be `SelCheckGPT`, while the scorer map uses `SelfCheckGPT` ([uncertainty/wiki_generation.py](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/uncertainty/wiki_generation.py), [uncertainty/scorer.py](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/uncertainty/scorer.py)). The testing script references shell variables that are not defined in the file ([script/testing.sh](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/script/testing.sh)). The FAISS path is partly commented in the topic generator while predefined topics are the active path ([uncertainty/topic_generator.py](https://github.com/wj210/Self-Training-LLM/blob/97839b29d0fd8bb474f5549fa3e9d6ca504732e0/uncertainty/topic_generator.py)).

Those rough edges do not invalidate the mechanism, but they matter for review interpretation. The repo is best treated as inspectable experiment code for a paper pipeline, not an off-the-shelf memory or continual-learning product.

## Comparison with Our System

| Dimension | Self-Training-LLM | Commonplace implication |
| --- | --- | --- |
| Source signal | Generated Wikipedia questions, reference answers, sampled model answers, hallucination or consistency scores | Useful contrast for trace-derived learning from batch generation rather than human note work |
| Learned form | SFT/DPO model checkpoints | Weight updates are not a substitute for inspectable KB artifacts |
| Oracle | NLI models, SelfCheck-style scoring, OpenAI-generated questions, GPT-4o pairwise judging | Promotion quality depends on oracle quality; weak oracles need reversible artifacts |
| Scope | Factual QA over Wikipedia-style documents | Much narrower than methodology synthesis, linking, and abstraction maintenance |
| Inspectability | Pickles, JSONL response files, caches, and checkpoints | Commonplace should prefer durable Markdown claims, links, and review trails |
| Timing | Offline staged pipeline | More like periodic batch review than online memory retrieval |

The main design lesson is that "what should be learned?" is the hard part. Self-Training-LLM answers with uncertainty thresholds over generated QA samples. Commonplace needs a different oracle: one that can identify missing abstractions, bad links, stale claims, underdeveloped notes, and synthesis opportunities.

## Borrowable Ideas

- Keep separate gates for input validity and learning value. Self-Training-LLM's question filtering and unknown filtering are a useful pattern even though the exact scores are domain-specific.
- Generate a held-out test set before training. For KB operations, an analogous pattern would reserve prompts or retrieval tasks before revising an index or note family.
- Preserve raw candidates and scores before promotion. The project keeps answer samples and scores before using them for SFT/DPO; a KB workflow should likewise keep rejected note candidates or failed review evidence when it explains later choices.
- Use paired before/after judging when hard metrics are unavailable. The pairwise baseline-vs-post setup is borrowable for small KB workflow experiments, provided judgments remain auditable.
- Cap generated preference pairs per item. The multiple-preference path limits how many chosen/rejected pairs a question contributes, which helps prevent a single source item from dominating training.

## Trace-derived learning placement

Self-Training-LLM is trace-derived learning, but not agent-memory learning.

**Trace source and extraction.** Its training traces are offline generation records: generated questions, context documents, reference answers, raw model answer samples, and NLI/self-check scores. Its extraction step filters and ranks those traces into SFT examples and DPO preference pairs. Pairwise judge outcomes are evaluation traces rather than training inputs.

**Storage substrate, form, and lineage.** Raw and intermediate traces persist as pickles, JSONL files, response logs, and caches; the promoted behavior-changing artifact is a distributed-parametric model checkpoint produced by SFT and DPO. The lineage is corpus chunk -> generated QA opportunity -> model answer samples -> uncertainty/hallucination scores -> filtered SFT/DPO records -> checkpoint.

**Behavioral authority.** The intermediate files have knowledge-artifact and audit use; the checkpoint has system-definition-artifact authority because future behavior is changed through model weights rather than retrieved context.

This places it beside systems like Agent-R only at the broad "trace to model update" level. Agent-R learns from agent trajectories through MCTS and preference optimization. Self-Training-LLM learns from corpus-grounded QA generation traces. The difference matters because generated factual QA traces do not carry the same action, tool, and task-state structure as autonomous agent trajectories.

## Curiosity Pass

- The repository is more concrete than a method-only paper, but narrower than broad self-learning language. It is a Wikipedia factual QA training pipeline.
- "Unknown" means model-answer disagreement or contradiction under a scoring procedure, not general epistemic absence.
- OpenAI is part of the loop for question generation and pairwise evaluation, so the system is not fully self-contained self-learning.
- The strongest contribution for KB design is the dataset-construction decomposition: generate opportunities, score uncertainty, filter candidates, construct preferences, then promote.
- The weakest fit for KB design is the final substrate. Weight updates erase most of the structure that a maintainable knowledge base needs to expose.

## What to Watch

- Whether the project publishes data, checkpoints, or result tables that make the claimed training effect easier to inspect.
- Whether brittle defaults and script variables are repaired.
- Whether question generation and judging move from OpenAI calls into the trained model or a local judge.
- Whether the loop becomes iterative across multiple self-training rounds rather than a staged one-shot pipeline.
- Whether the method expands beyond Wikipedia factual QA into arbitrary corpora or task traces.
- Whether it adds an interpretable artifact layer before weight promotion.

## Relevant Notes

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md)
- [Into the Unknown ingest](https://arxiv.org/html/2402.09147v4)
- [Automating KB learning is an open problem](../../notes/automating-kb-learning-is-an-open-problem.md)
- [Memory management policy is learnable but oracle-dependent](../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md)
- [Treat continual learning as substrate coevolution](../../notes/treat-continual-learning-as-substrate-coevolution.md)
- [Continual learning's open problem is behaviour, not knowledge](../../notes/continual-learning-open-problem-is-behaviour-not-knowledge.md)
- [Oracle strength spectrum](../../notes/oracle-strength-spectrum.md)
- [The boundary of automation is the boundary of verification](../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md)
- [Continual Learning in Token Space](https://www.letta.com/blog/continual-learning)
- [Agent-R](./agent-r.md)
- [Autocontext](./autocontext.md)
