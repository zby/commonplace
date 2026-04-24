---
description: Three-role generator-reflector-curator loop that grows a sectioned playbook of ID-tagged bullets with helpful/harmful counters; curator prompt now only solicits ADD, with optional embedding-based merge
type: ../types/agent-memory-system-review.md
tags: [related-systems, trace-derived]
status: current
last-checked: "2026-04-12"
---

# ACE

ACE (Agentic Context Engineering) is a Python framework that teaches a language model by evolving a sectioned text "playbook" rather than by fine-tuning. A generator answers tasks using the current playbook, a reflector diagnoses the attempt and tags the bullets it consumed, and a curator proposes operations that grow the playbook. Built by the `ace-agent` group and released with the arXiv paper 2510.04618; the repo runs offline training, online adaptation, and eval-only modes over AppWorld, FiNER, and XBRL Formula benchmarks.

**Repository:** https://github.com/ace-agent/ace

## Core Ideas

**The learned substrate is a sectioned text playbook of ID-tagged bullets.** An empty playbook (`ace/ace.py`) seeds fixed sections — `STRATEGIES & INSIGHTS`, `FORMULAS & CALCULATIONS`, `CODE SNIPPETS & TEMPLATES`, `COMMON MISTAKES TO AVOID`, `PROBLEM-SOLVING HEURISTICS`, `CONTEXT CLUES & INDICATORS`, `OTHERS`. Each bullet is one line: `[slug-00001] helpful=4 harmful=0 :: content`. Bullet IDs are stable across the run, letting the reflector reference exactly which bullets were used and letting the curator reason about existing inventory.

**Three roles are wired as separate LLM calls with distinct prompts.** `ace/core/generator.py` embeds the playbook and any prior reflection into the prompt, generates an answer, and regex-extracts the bullet IDs the model claimed to use (`\[([a-z]{3,}-\d{5})\]`). `ace/core/reflector.py` receives question, reasoning trace, prediction, environment feedback, and the subset of bullets actually referenced, then emits diagnosis fields plus `bullet_tags: [{id, tag}]` with tag in `{helpful, harmful, neutral}`. `ace/core/curator.py` receives the reflection plus playbook stats and emits `operations` in JSON. This is a real separation: three prompt files, three LLM calls, and the reflector is run on both correct and incorrect attempts.

**Counters move one layer; bullet writes move another.** `playbook_utils.update_bullet_counts` applies the reflector's tags by incrementing `helpful` or `harmful` on existing lines in place — this is deterministic code, no LLM. `apply_curator_operations` handles the curator's structured operations. The two paths never collide, which is what makes counter updates cheap and safe while still letting the curator add genuinely new content.

**The curator prompt now advertises only `ADD`.** Both `CURATOR_PROMPT` and `CURATOR_PROMPT_NO_GT` in `ace/prompts/curator.py` list a single available operation — `ADD` with `section` and `content` — and the example output emits only an `ADD`. The operation validator in `ace/core/curator.py` still tolerates `UPDATE`, `MERGE`, `DELETE`, and `CREATE_META` as legal types (with a "may not be fully supported" warning), but the code in `apply_curator_operations` has TODO-commented branches only for those; `ADD` is the sole implemented mutation. So the in-code behavior is append-plus-tag, with any UPDATE/DELETE the model proposes silently dropped.

**Grow-and-refine is a two-stage loop, with semantic merge gated off by default.** At `curator_frequency` steps, the orchestrator calls the curator to propose ADDs, then optionally calls `BulletpointAnalyzer.analyze` when `use_bulletpoint_analyzer=True` (default `False`). The analyzer embeds bullets with `all-mpnet-base-v2`, finds groups whose cosine similarity exceeds a threshold (default 0.90), and either deduplicates or calls the LLM with a merge prompt that fuses counts and content. Merge preserves the first bullet's ID and sums the counters. Without that flag the playbook monotonically accretes ADDs, subject only to the generator's token budget.

**Offline and online modes share the single-sample learning loop.** `_train_single_sample` handles one item: generate, check correctness, iterate up to `max_num_rounds` reflection-regenerate cycles if wrong (tagging bullets each round), run the reflector once more on correct attempts for positive tagging, run the curator every `curator_frequency` steps, then regenerate post-curator for logging. Offline mode wraps this in epochs with validation gating on a best-playbook. Online mode drives the same sample loop while also testing on the data it is adapting to. The learning pipeline is the same; only the orchestration around it differs.

## Comparison with Our System

ACE is one of the most structurally explicit artifact-learning systems in the survey. Its playbook is closer to a scored rule list than to our workshop-heavy note library: flat lines, fixed sections, stable IDs, counters. Commonplace by contrast has typed notes, frontmatter, links, an index layer, a workshop layer, and no automated promotion.

| Dimension | ACE | Commonplace |
|---|---|---|
| Trace source | Task attempts, reasoning traces, environment feedback, bullet-usage IDs | Human+agent editing traces, notes, links, workshop artifacts |
| Learned substrate | Sectioned plain-text playbook of counter-tagged bullets | Typed markdown notes with frontmatter and links |
| Promotion target | Inspectable text playbook only (no weight path in repo) | Inspectable text notes only |
| Write path | Reflector increments counters; curator emits ADD ops; optional embedding merge | Human+agent edits with validate/connect/mature conventions |
| Oracle | `data_processor.answer_is_correct` against ground truth, or environment feedback | Mostly human judgment and `commonplace-validate` |
| Governance | Token budget, sectioned layout, optional similarity-merge | Type system, validation commands, link checks, review bundle |
| Retrieval | Whole playbook concatenated to generator prompt; reflector gets only used-bullet subset | Agent navigation over linked files |

The closest neighbors in our survey are [Dynamic Cheatsheet](./dynamic-cheatsheet.md), which also carries a single evolving text artifact across task attempts but rewrites rather than accumulates scored bullets, and [ExpeL](./expel.md), which has richer mutation verbs than ACE implements. [Autocontext](./autocontext.md) extends toward weight export; ACE does not. Within the artifact-only lane, ACE's distinguishing feature is not the three-role decomposition — plenty of systems separate reflection from curation — but the combination of stable bullet IDs, in-place counter updates, and a curator whose written output is narrowed to ADDs while an orthogonal embedding merge handles cleanup.

**Trace-derived learning placement.** The **trace source** is a structured bundle per sample: question, reasoning trace, prediction, environment feedback string, and the bullet IDs the generator claimed to use; trigger boundary is per sample for reflection and every `curator_frequency` samples for curation. **Extraction** is two-staged — the reflector emits structured reflection JSON plus per-bullet tags (`helpful`/`harmful`/`neutral`); the curator emits ADD operations with `section` and `content`; the oracle that gates both is `data_processor.answer_is_correct` in labeled settings or the environment-feedback string in unlabeled settings. **Promotion target** is an inspectable playbook file; no weights are produced in this repo. The memory is ephemeral to a run directory unless the operator reuses `best_playbook.txt` via `--initial_playbook_path`. **Scope** is per-task in practice — playbook sections and bullet slugs are general, but the empirically useful content ties to the task's answer format. **Timing** is staged: offline mode trains then tests; online mode interleaves training and testing on the same stream; both are batched-per-sample rather than continuous. On the [survey's axes](../trace-derived-learning-techniques-in-related-systems.md), ACE sits on **axis 1** as **trajectory-run** (repeated evaluated attempts, not a live session mined at end) and on **axis 2** as pure **artifact-learning**. The system does not warrant a new subtype; it remains the clearest "scored flat rules with ID-level feedback" example and still anchors the **counter-based** maintenance column. The one detail worth tightening in the survey is that ACE's maintenance path is actually **append-plus-counters with optional embedding-merge**, not append-plus-CRUD — the CRUD verbs exist only in the schema validator.

## Borrowable Ideas

**Split tagging from mutation.** Ready now. ACE applies the reflector's helpful/harmful tags through deterministic code, not through an LLM rewrite. Any scoring-or-counting signal we attach to notes or workshop observations should flow through code after the diagnosis LLM call, not inside it. This keeps the mutation audit-able and cheap.

**Stable IDs on learnable units.** Ready now. Bullet IDs let ACE reference exactly what was used, tag what was useful, and compare playbook state across checkpoints. Workshop-derived learnings and review findings in our system would benefit from stable IDs with a per-section slug, especially if we want to track which items get reinforced across sessions.

**Narrow the curator's prompt to the operation you implement.** Ready now. ACE's current curator prompt offers only `ADD`; the schema still tolerates more, but the prompt's vocabulary shapes what the model tries to propose. Our equivalent is to tell review-bundle fixers exactly which edit verbs the pipeline actually applies, rather than advertising a richer set and silently discarding unsupported operations.

**Two-stage grow-and-refine with a gated semantic merge.** Needs a use case first. The split between a write-heavy curator and an opt-in embedding-merge pass is a usable pattern for our library, but we do not yet have the semantic-duplicate problem at a scale that would justify running sentence-transformers over the note corpus. Worth remembering when we decide how to consolidate overlapping notes.

**Run the reflector on correct attempts, not only failures.** Ready now as a pattern. ACE calls the reflector on successes to tag helpful bullets even when the answer was right. That gives the counter mechanism positive evidence, not just negative, and avoids a drift where only failures ever influence the playbook.

## Curiosity Pass

The three-role architecture in isolation is not the mechanism that matters — any reflection-memory system could be described as generator/reflector/curator. The actual engines in ACE are (1) the stable bullet IDs that make counter updates a local in-place edit, and (2) the narrow append-only curator that keeps the growth loop simple. The `BulletpointAnalyzer` is advertised as the "grow-and-refine" counterpart to growth, but it is off by default and depends on optional dependencies — in a default run, refinement means "helpful/harmful counts change," not "bullets are edited or retired."

For each strong claim:

1. **"Incremental delta updates that preserve prior knowledge."** This does transform the data, but only in one direction: `ADD` inserts new bullets and the counter layer mutates an integer per line. Real UPDATE/MERGE/DELETE would be transformations; they are not present. The simpler alternative — "rewrite the whole playbook each turn" — is what the paper pushes against, and ACE does genuinely avoid that. But the mechanism that preserves prior knowledge is primarily that nothing gets deleted, not that edits are localized.

2. **"Scored bullets steer future generation."** This does transform: counter values let the model downweight bullets with many harmful tags without an explicit DELETE. But the transformation is weak — the counters are displayed but not enforced, and the generator prompt does not take them as structured inputs. A simpler alternative is to hard-prune bullets whose harmful exceeds helpful by some margin; ACE has the stats (`get_playbook_stats` classifies `problematic`) but does not act on them.

3. **"Separation of reflector and curator improves quality."** This is a real separation in the code. The claim that it improves downstream performance is an empirical question for the paper; structurally, it lets us isolate diagnosis from mutation, which is a pattern we can borrow regardless of whether it improves accuracy in ACE's benchmarks.

4. **"Grow-and-refine via semantic merge."** Only half-real in default runs. The growth path is live; the refine path is an opt-in code path that requires sentence-transformers and faiss. If someone reading the README assumes refinement happens automatically, the code will disappoint them.

The ceiling is still maintenance. `apply_curator_operations` carries TODO comments for UPDATE, MERGE, and DELETE. `get_playbook_stats` computes `unused`, `problematic`, and `high_performing` counts but no code prunes on them. The playbook token budget is surfaced in prompts but not enforced in code. Under enough samples, the playbook grows, and the only genuine retirement mechanism is the optional embedding merge.

## What to Watch

- Whether UPDATE, MERGE, DELETE, or CREATE_META move from TODO comments into implemented operations in `playbook_utils.apply_curator_operations`
- Whether the token budget is ever enforced in code rather than just inserted into prompts
- Whether `get_playbook_stats` categories (`problematic`, `unused`) start gating actual pruning
- Whether the `BulletpointAnalyzer` becomes default-on, which would materially change the grow-and-refine framing
- Whether ACE grows a weight-promotion export, which would move it toward [Autocontext](./autocontext.md)'s mixed position on axis 2
- Whether additional task domains beyond AppWorld and finance benchmarks test the architecture against weaker oracles

---

Relevant Notes:

- [trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) — extends: ACE anchors the scored-flat-rule, counter-based, artifact-only cell and still fits the trajectory-run ingestion pattern
- [Dynamic Cheatsheet](./dynamic-cheatsheet.md) — compares: both evolve a single text artifact across attempts, but Dynamic Cheatsheet rewrites the whole cheatsheet while ACE appends ID-tagged bullets with helpful/harmful counters
- [ExpeL](./expel.md) — compares: both produce scored rule lists from task outcomes, but ExpeL implements explicit mutation verbs that ACE's curator prompt no longer exposes
- [memory management policy is learnable but oracle-dependent](../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md) — sharpens: ACE's counter updates and curator operations depend on the correctness oracle; without ground-truth or environment feedback the tagging signal is thin
- [automating KB learning is an open problem](../../notes/automating-kb-learning-is-an-open-problem.md) — contrasts: ACE narrows the problem to benchmark tasks with verifiable answers, which is exactly where automated promotion is tractable — the hard case is open-ended KB curation
