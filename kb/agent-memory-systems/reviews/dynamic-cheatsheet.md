---
description: Test-time adaptive memory where the core stateful cheatsheet variants rewrite a carried-forward cheatsheet string; v2.0 adds a hybrid cumulative-plus-retrieval approach and server-side code execution, but curation is still full-document rewrite with no enforced invariants
type: agent-memory-system-review
tags: [related-systems, trace-derived]
status: current
last-checked: "2026-04-12"
---

# Dynamic Cheatsheet

Dynamic Cheatsheet is a research framework for test-time learning in black-box language models. A generator answers each query with the current cheatsheet injected into its prompt; a second curator call then rewrites the stateful cheatsheet variants for the next query. The v2.0 release broadens the approach set to six variants: four stateful cheatsheet variants plus two baselines (full-history appending, retrieval-only), wires up a unified multi-provider client (OpenAI, Anthropic, Gemini, xAI, Together, DeepSeek, Ollama), and adds a code-execution path that can run either as a local subprocess or server-side through OpenAI containers or Claude's native code tool. Built by Mirac Suzgun and collaborators around the arXiv:2504.07952 paper; research code rather than a production memory service.

**Repository:** https://github.com/suzgunmirac/dynamic-cheatsheet

## Core Ideas

**The learned state is still one carried-forward cheatsheet string for the stateful variants.** In `language_model.py`, every stateful approach returns `final_cheatsheet` as a single text blob, and `run_benchmark.py` reassigns `cheatsheet = output_dict["final_cheatsheet"]` at the end of each example. There is no structured index, typed memory store, or separately addressable note — the unit of memory remains one document that is replayed into the next prompt. The `initialize_cheatsheet_path` flag lets a run boot from a pre-written cheatsheet file, which is the only place persistent structure leaks in.

**Curation is still XML-tag extract-and-replace, not operation-based editing.** `extract_cheatsheet(response, old_cheatsheet)` in `utils/extractor.py` looks for a `<cheatsheet>...</cheatsheet>` block in the curator's output; if found, it returns that block verbatim and replaces the prior cheatsheet wholesale, otherwise it returns the old cheatsheet unchanged. The curator prompts ask the model to preserve content, maintain a version number, and track `** Count:` fields on each `<memory_item>`, but no code parses, diffs, or enforces any of this. The whole maintenance policy lives inside one LLM call's rewrite quality.

**A genuine new option in v2.0: the cumulative+retrieval hybrid.** `DynamicCheatsheet_CumulativeRetrieval` is implemented as a distinct branch that (1) builds a `retrieved_section` with the top-k cosine-similar previous examples, (2) concatenates it after the cumulative cheatsheet into a `combined_cheatsheet` for the generator, and (3) runs the curator only on the cumulative half, so retrieved examples feed generation but do not accumulate into the persistent blob. This is the clearest architectural move since the prior review: it splits stable meta-knowledge from task-local precedents, which the prior variants conflated.

**The trace source is an ordered benchmark pass, not a live session.** `run_benchmark.py` iterates a shuffled dataset (GameOf24, AIME, GPQA-Diamond, MMLU-Pro, MathEquationBalancer), passes each `input` through the selected approach, and feeds the returned cheatsheet and output forward. Retrieval variants require a pre-computed `embeddings/{task}.csv` indexed by input string; there is no online embedder or live session log. The system learns from repeated problem attempts in a benchmark, not from assistant tool traces or event streams.

**Code execution is now a real closed loop, including server-side variants.** The `generate(...)` recursion in `language_model.py` detects a code block followed by an `EXECUTE CODE!` flag, runs it via `extract_and_run_python_code`, appends the output, and recurses up to `max_depth_num_rounds`. New in v2.0: `use_code_interpreter=True` routes instead to OpenAI's Responses API with a persistent container (`generate_with_code_interpreter(...)`) or Claude's native code-execution tool (`generate_with_code_interpreter_claude(...)`), with a `_NATIVE_CODE_EXECUTION_ID` sentinel so Claude doesn't need a container handle. Code execution is orthogonal to memory but it is the main path by which the Game-of-24-style accuracy claims become real: the cheatsheet accumulates Python recipes, and the generator actually runs them.

**Counts and version numbers remain prompt-level conventions only.** The curator prompts demand `** Count:` on every memory item and a `Version: [N]` header, but grep of the source finds no code that reads, increments, or validates either. The counter story is a prompt contract that the LLM is trusted to honour during each wholesale rewrite. That is the same state as the prior review — the v2.0 changes do not introduce enforced state transitions.

## Comparison with Our System

Dynamic Cheatsheet is still the loosest artifact-learning system in the review set: persistent across queries, but the substrate is one prompt-shaped document rather than separately addressable artifacts. The v2.0 additions (hybrid retrieval, server-side code exec, multi-provider) broaden the execution surface without changing the memory substrate.

| Dimension | Dynamic Cheatsheet (v2.0) | Commonplace |
|---|---|---|
| Trace source | Ordered benchmark queries, answers, optional retrieved prior examples | Human+agent editing traces, notes, links, workshop artifacts |
| Learned substrate | One evolving cheatsheet text blob | Notes, links, instructions, workshop artifacts |
| Addressable unit | None — everything is one document | Individual markdown files with frontmatter |
| Promotion target | Inspectable text only | Inspectable text only |
| Update style | Full cheatsheet rewrite each step | Manual curation and targeted file edits |
| Retrieval model | Pre-computed embeddings (CSV) + cosine over prior examples | Agent-driven navigation over linked markdown |
| Oracle | Implicit task success inside benchmark evaluators | Weak, mostly human judgment |
| Storage | Result JSONL, embeddings CSV, no file per memory item | Files in git with types and validators |
| Code execution | Local subprocess or server-side container/native tool | None in the KB itself |

**Where Dynamic Cheatsheet is stronger.** The closed rewrite loop is simple and genuinely ends in measurable accuracy gains on benchmark tasks. The v2.0 hybrid cleanly separates two roles we often conflate: stable meta-knowledge versus task-local precedents. Code execution lets the cheatsheet accumulate executable recipes, which is a stronger learning surface than notes alone.

**Where commonplace is stronger.** Separately addressable artifacts, enforced structure (frontmatter, types, link contracts, validators), and explicit maintenance operations. Dynamic Cheatsheet cannot say "update item 7" — it can only rewrite the whole document. That is fine for 2000-word test-time memory, but it does not scale to cross-project or multi-domain knowledge.

## Borrowable Ideas

**Split stable meta-knowledge from task-local precedents.** Ready to borrow as a concept. The hybrid variant is the first design in this review set to admit that one substrate cannot do both. Our analogue already exists — notes (stable) versus workshop artifacts (task-local) — but the hybrid reinforces that injecting both into context at once, with clear labels, is the correct move. Useful as evidence for the workshop-versus-library split.

**Carry-forward artifact as a minimum-viable learning loop.** Ready as a framing. If we ever prototype automated KB capture, the Dynamic Cheatsheet loop (current artifact in, revised artifact out, feed forward) is the floor against which richer designs must justify their complexity.

**Pre-computed embeddings keyed by canonical input.** Needs a use case first. The CSV-per-task embeddings indexed by input string is a lightweight pattern for retrieval in a fixed-corpus setting. Our KB is not fixed-corpus, so the direct pattern does not apply, but it is a reminder that not every retrieval problem needs a live vector store.

**Optional pre-existing cheatsheet as boot state.** Ready to borrow. `initialize_cheatsheet_path` is a small but real concession that learned memory should be inspectable and editable — it lets an operator hand-write the starting state and then let the loop refine it. Our CLAUDE.md routing table is the closest analogue.

## Curiosity Pass

**What property does the rewrite loop claim to produce?** A cheatsheet whose content improves monotonically with more queries — a test-time scratchpad that concentrates strategies and Python recipes into a reusable resource.

**Does the mechanism transform the data, or just relocate it?** The curator call does transform: a conversation trace plus an old cheatsheet become a new cheatsheet with (hopefully) consolidated entries. But the transformation is opaque — the code only slices the `<cheatsheet>` block and swaps it in. The model is doing all the work of merging, counting, and pruning inside one rewrite; the system around it has no way to detect silent regressions. The hybrid variant is a genuine structural transformation: it fuses a general playbook with retrieved nearby examples into a combined prompt context.

**What is the simpler alternative?** For the cumulative variant: append-only list of `(query, answer)` pairs, truncated to fit the context. The `FullHistoryAppending` baseline in this repo is almost exactly that. The paper's benchmarks will tell whether the curator step earns its keep against that baseline on tasks where code execution isn't the dominant factor.

**What could this mechanism achieve even if it worked perfectly?** It can concentrate solution strategies for a single benchmark family into a reusable prompt-state artifact. It cannot: connect across domains, recognise that a stored strategy is wrong once it has been written in (the version counter is LLM-maintained, not enforced), or survive a bad rewrite — one poor curator call can silently evict correct knowledge. The follow-up paper [Large Language Model Agents Are Not Always Faithful Self-Evolvers](../../sources/large-language-model-agents-are-not-always-faithful-self-evolvers.ingest.md) measures exactly this risk: cheatsheet-style condensed experience often has limited causal influence under intervention.

**The retrieval-plus-synthesis variant hides a subtle trust choice.** `DynamicCheatsheet_RetrievalSynthesis` runs the curator over a freshly retrieved block and replaces the carried-forward cheatsheet with the curator's output (stored as `curated_cheatsheet`). So the per-query retrieval pipeline writes to the same state that the cumulative pipeline does. Whether that is desirable depends on whether you want the persistent memory to reflect "what I just synthesised for this query" — a subtle leak that the README does not foreground.

**Trace-derived learning placement.** Trace source: ordered benchmark queries, model answers, and (for retrieval variants) pre-computed embeddings over prior questions; the trigger boundary is one benchmark sample. Extraction: a second LLM call reads the query, answer, and prior cheatsheet and emits a `<cheatsheet>` block that replaces the old one wholesale; there is no oracle other than the benchmark-wide evaluator, which never feeds back into the curator prompt. Promotion target: one evolving text blob, optionally plus retrieved examples — always inspectable text, never weights, never a separately addressable store. Scope: one benchmark run; `initialize_cheatsheet_path` is the only portability seam. Timing: online during a benchmark pass, sequential, one curator call per query. On the [survey's](../trace-derived-learning-techniques-in-related-systems.md) axis 1, Dynamic Cheatsheet fits the **trajectory-run pattern** — repeated problem attempts in a benchmark, not a single live session. On axis 2, it is firmly **artifact-learning**, the most structure-light case: whole-document rewrite rather than mutation verbs (ExpeL) or bullet counters (ACE). The v2.0 hybrid does not move it across axes; it adds a second injected context stream but the persisted artifact is still one rewritten blob. The entry sharpens the survey's claim that artifact structure varies widely within the symbolic-artifact branch — Dynamic Cheatsheet remains the low-structure anchor, and the v2.0 hybrid is evidence that the single-blob design benefits from an auxiliary task-local context stream, even though the persistent memory was not restructured.

## What to Watch

- Whether v3.0 or later moves from full-document rewrite to any form of operation-based editing (diff, patch, bullet ID, mutation verb).
- Whether the `** Count:` and `Version:` conventions ever get code-level enforcement, or stay LLM-trusted.
- Whether the hybrid cumulative+retrieval variant outperforms cumulative-only outside narrow benchmark settings — if so, it is evidence that the stable/task-local split is the right structural move.
- Whether the server-side code-execution path (OpenAI container, Claude native tool) becomes the default, and whether it changes what the curator chooses to store in the cheatsheet.
- Whether the project grows any cross-run, cross-task memory portability beyond `initialize_cheatsheet_path`.

---

Relevant Notes:

- [trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) — extends: Dynamic Cheatsheet is the low-structure anchor among artifact-learning systems, with v2.0's hybrid now layering retrieval on top of a still-unstructured persistent blob
- [Pi Self-Learning](./pi-self-learning.md) — contrasts: both carry forward textual learnings, but Pi Self-Learning uses a scored index with frequency/recency mechanics while Dynamic Cheatsheet relies on freeform whole-document rewrites
- [ACE](./ace.md) — contrasts: ACE performs bullet-level operations with helpful/harmful counters on an addressable playbook; Dynamic Cheatsheet performs whole-document rewrite on an unaddressable blob, one rung lower on the structure axis
- [ExpeL](./expel.md) — contrasts: ExpeL parses explicit `ADD`/`EDIT`/`REMOVE`/`AGREE` operations with strength counters; Dynamic Cheatsheet has no operation language at all
- [Autocontext](./autocontext.md) — contrasts: both learn across runs, but Autocontext bridges to weight distillation through JSONL exports while Dynamic Cheatsheet stays at prompt-state artifacts
- [memory management policy is learnable but oracle-dependent](../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md) — sharpens: Dynamic Cheatsheet's maintenance policy lives entirely in one LLM call, with no oracle feeding the curator — the cleanest instance of oracle-free artifact curation
- [deploy-time learning](../../notes/deploy-time-learning-is-the-missing-middle.md) — sharpens: sits squarely in the deploy-time artifact-update space, using persistent prompt-state rather than weights
- [a functioning KB needs a workshop layer, not just a library](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — sharpens: the v2.0 hybrid's split between cumulative playbook and retrieved examples is structural evidence that stable and task-local memory need different substrates
- [Large Language Model Agents Are Not Always Faithful Self-Evolvers](../../sources/large-language-model-agents-are-not-always-faithful-self-evolvers.ingest.md) — evidence: evaluates Dynamic Cheatsheet directly and finds condensed cheatsheet-style experience has limited causal influence under intervention
