---
type: types/note.md
description: "Napkin's file-based retrieval, skill-directed memory revision and externally hosted consumer loop at a frozen source boundary"
generated-by: analyse-agentic-system
analysis-run: AAS-2026-09-27-napkin-01
source-identity: https://github.com/Michaelliv/napkin
reviewed-revision: "7582d6a46f5a11995956e60a59c41a5b242109f1"
analysis-result: kb/reports/retained/agentic-system-analysis/AAS-2026-09-27-napkin-01/result.md
analysis-result-sha256: "8484f622335c134237968326c9971d8fbb1e71f97128e411f96b8d46ccba41db"
---

# Napkin

**Evidence basis:** source code, shipped skills and design documents, plus attributed benchmark reports at commit `7582d6a46f5a11995956e60a59c41a5b242109f1`, inspected on 2026-09-27. No live execution or causal experiment was performed.

Napkin gives agents persistent files and progressively more detailed access to them. Its CLI and SDK return an overview, ranked snippets or full notes. The surrounding agent host owns model calls, tool selection and context assembly. This review covers the package, shipped distill/tend skills and documented or benchmark consumer paths: a complete artifact with a partial enclosing loop. The [exact result](../../reports/retained/agentic-system-analysis/AAS-2026-09-27-napkin-01/result.md) retains canonical records, quotations, limitations and all fourteen memory-comparison axes.

## Runtime and memory

The ordinary path is overview → search → read. Napkin compiles lexical indexes and overview caches, combines search scores with backlink and recency signals, then returns selected content. Those operations are wired; the external agent's use of the returned information is an afforded consumer path. A separate documented session integration supplies the whole `NAPKIN.md` context note, but its implementation is outside the frozen repository. A requested overview containing that note remains a pull response. See exact-result records RTE-7 and RTE-11, supported by [search implementation](https://github.com/Michaelliv/napkin/blob/7582d6a46f5a11995956e60a59c41a5b242109f1/src/core/search.ts) and [progressive-disclosure design](https://github.com/Michaelliv/napkin/blob/7582d6a46f5a11995956e60a59c41a5b242109f1/docs/agent-memory-progressive-disclosure.md).

Durable memory is principally Markdown and structured files. SQLite also appears as a transient, in-memory access structure for base queries; it is not the durable note store. Context-size figures are writing targets: full reads and the complete overview do not have an enforced aggregate token budget. Cache fingerprints use paths and modification times, so they do not establish semantic freshness. These distinctions are recorded in OBJ-6, OBJ-7, OBJ-8 and OBJ-9 and RTE-7 of the exact result.

The shipped **distill** skill directs an external agent to turn useful session findings into notes, search before creating, merge new information, retain reasons and mark new generalizations as inferred. **Tend** directs conservative upkeep, duplicate merging and withdrawal of superseded notes; template changes remain the user's choice. File writes are wired, while executing these semantic workflows is afforded. The separate timer-driven distillation described in documentation belongs to an external pi extension. See RTE-6, RTE-8, RTE-9 and CLM-3, with the [distill skill](https://github.com/Michaelliv/napkin/blob/7582d6a46f5a11995956e60a59c41a5b242109f1/skills/distill/SKILL.md), [tend skill](https://github.com/Michaelliv/napkin/blob/7582d6a46f5a11995956e60a59c41a5b242109f1/skills/tend/SKILL.md) and [external distillation design](https://github.com/Michaelliv/napkin/blob/7582d6a46f5a11995956e60a59c41a5b242109f1/docs/distill.md).

## What the evidence supports

Napkin supplies a concrete path for edits to retained files to change later retrieval. The distill workflow further affords localized solution statements, content-guided revision, explicit contradiction handling and persistence into a later round. These separately support an afforded [theory-builder](../../notes/definitions/theory-builder.md) pathway; actual membership of a running enclosing system is uninspected. Retaining useful solutions and reasons is its strongest supported contribution toward learning. Improved future capacity attributable to criticism remains unestablished. The normalized `trace_learning: yes` value describes the afforded extraction route, not observed improvement.

The agent can also use a representation of its memory organization to guide maintenance, an afforded [reflective](../../notes/definitions/reflective-system.md) path at that limited boundary. A complete causal host loop, criticism of its own method, all-computational execution of every builder role, and occurring [self-improvement](../../notes/definitions/self-improving-system.md) are uninspected. A global package update selects npm's `latest`; it is not an evidence-directed improvement loop.

Benchmark sources report 91% on LongMemEval S and 83% on M for a pi-plus-Napkin/Sonnet sample. These are attributed bundle results, not independently reproduced measurements or isolated Napkin effects. The driver uses reference answers, substring shortcuts, a model judge and a token-F1 fallback; retained access metrics do not test dependence on recalled content. See CLM-1 and RTE-2, the [reported results](https://github.com/Michaelliv/napkin/blob/7582d6a46f5a11995956e60a59c41a5b242109f1/bench/README.md) and [evaluation code](https://github.com/Michaelliv/napkin/blob/7582d6a46f5a11995956e60a59c41a5b242109f1/bench/longmemeval-eval.ts).

## Scope

External pi/extension implementations, providers, downloaded datasets and real deployment histories were inaccessible. The referenced benchmark extension is absent from the frozen tree. Consequently, this account establishes package wiring and documented consumer affordances, not deployed permissions, actual context activation or recall faithfulness. The native search dependency is inspected only at Napkin's interface; ancillary UI/workflows are not exhaustively reviewed.

Pinned host code and linked session → note → later-action traces would resolve the consumer boundary. Criticism/revision records and controlled future-task comparisons would be needed to establish learning. No cross-system ranking or transfer recommendation follows from this analysis.
