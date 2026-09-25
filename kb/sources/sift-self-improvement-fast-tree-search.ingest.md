---
description: "SIFT uses cheap pairwise code judgments to guide asynchronous harness search; its experiments distinguish search guidance, final selection, and the cost of stronger evaluation."
type: kb/sources/types/ingest-report.md
source: https://arxiv.org/abs/2609.19526
captured: "2026-09-24"
ingested: "2026-09-25"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: eb90e9a9482059b114863cc1aebf7b2c013030b6a5319715361598245fdb759a
domains: [self-improving-systems, evaluation, search-control]
learning_claims: true
---

# Ingest: Self Improvement via Fast Tree-search

## Classification

Scientific preprint by Xinghong Fu, Aravinth Kulanthaivelu, and Yutaro Yamada, affiliated with MIT and Sakana AI. The authors introduce SIFT and report coding-agent benchmarks, judge ablations, repeated candidate evaluations, implementation excerpts, and idealized ranking arguments. These are the system authors' experiments, not an independent replication.

## Summary

[SIFT](https://arxiv.org/abs/2609.19526) searches over coding-agent implementations while using inexpensive pairwise code judgments to allocate further search before benchmark evaluations finish. Bradley–Terry aggregation turns preferences into ranks, which combine with benchmark-accuracy ranks and visit counts to select parents and prioritize evaluation. The Polyglot setup fixes a four-task failure gate, a 50-task search subset, and comparisons against up to ten strong incumbents; pending candidates temporarily inherit their parent's accuracy. Within this arrangement, the paper reports improved full-benchmark performance and lower resource use than several earlier systems, though asynchronous execution accounts for most measured speedup. TerminalBench's one-search-per-condition comparison supplies a sharper distinction: the judge-selected candidate averages 36.7% over three full evaluations, versus 29.2% for the no-judge selection, while selecting the judged run's highest search accuracy yields only 28.1%. The useful contribution is evidence that cheap judgments can guide search and sometimes final choice, with those two uses requiring separate evaluation.

## Quotes

No source quotes have been retained yet.

## Connections Found

SIFT supplies bounded evidence for [testing a search controller by what it brings to stronger evaluation](../notes/a-search-controller-is-tested-by-what-it-brings-to-stronger-evaluation.md). The judge/no-judge comparisons test whether code preferences improve the candidates reached within an otherwise specified harness-search loop. Repeating selected candidates strengthens the outcome estimate; it does not measure variation across independent searches. The broader resource comparisons also vary scheduling and sometimes models, so they cannot assign all gains to judging.

Its speculative expansions exemplify [lightweight search control](../notes/lightweight-search-control-does-not-license-adoption.md): a candidate that passes an easy gate may receive further search while its measured performance remains unknown. The inherited parent accuracy is scheduling state, not an observation of the child. Judge-based final selection is a separate use, tested in the paper alongside selection by benchmark accuracy; Algorithm 1 itself returns the highest measured accuracy.

For the [pairwise-comparison test plan](../notes/brainstorming-how-to-test-whether-pairwise-comparison-can-harden.md), SIFT contributes representation ablations and a distinction between archive-wide ranking and ordering the strongest candidates. It does not compare pairwise judging with scalar judging under matched resources, so it leaves that note's central interface question open.

## Learning Claims (our opinion)

SIFT's adaptation persists in modified harness code, prompts, and tools. A diagnosis and self-improvement model reads the current implementation and available evaluation logs or failure traces, then proposes a child. A separate judge reads competing implementations without benchmark tasks or outcomes. Its preferences affect parent sampling and evaluation priority; downstream executions provide behavioral feedback. The coding, improvement, and judging models can differ. The reported improvements therefore concern the compound system, not a model improving its own weights or judging itself unaided.

Against the [theory-builder definition](../notes/definitions/theory-builder.md), conditions 1 and 2 are met: harness code, prompts, and tools are stated units that govern the coding agent. Condition 3 is plausibly met beyond outcome-only selection. The judge explains its ranking first, and reported explanations criticize particular implementation commitments: a verifier disabled by default, or a tool that claims persistent shell state while starting a fresh shell on each call. Those criticisms bear on what the program says, though they act mainly through preference ranks that allocate search. Condition 4 (iteration) is met: each child is proposed from its parent with evaluation logs and failure traces, and the judge's criticisms steer which parent is expanded next. SIFT is therefore inside the term, with condition 3 carrying the remaining uncertainty. Each search builds one tree of harness variants against one benchmark subset, so the persistence grade reached is across rounds of one run on one task. Full-benchmark evaluation and transfer to other coding models reuse the selected product, and freezing it ends the builder; nothing takes the archive or the judge's criticisms up in later work on other problems. As a separate learning claim, retained prompt and tool revisions improve task behavior within the search, but the paper does not isolate formulated criticism from proposing, scoring, and selecting variants.

The editable code and prompts expose parts for selective revision, consistent with [addressability](../notes/definitions/addressable-theory.md). The example adding a test runner and an instruction to use it is a concrete operative change. Its larger descendant adds a test analyzer without improving subset accuracy and scores lower on the full benchmark. This illustrates that retaining more machinery need not improve behavior; it does not establish a general preference for smaller revisions or confirm every rationale behind the original patch.

The effective update space includes harness behavior and tools but holds the search controller, judge interface, scalar aggregation, evaluation tasks, and permitted-file boundary outside candidate revision. This is [learning within a fixed decomposition](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md). The judge-input ablation tests one of those external choices by comparing file and diff representations. The successful search does not independently vindicate the remaining fixed choices or show that one scalar ranking preserves every useful task distinction.

## Extractable Value

1. **Evaluate routing and final selection separately.** Within SIFT's fixed harness-search setup, a judge can bring promising candidates forward even when a noisy search score chooses the wrong final candidate. The TerminalBench result is evidence from one search per condition, followed by repeated evaluations, rather than a distribution over independent searches. This is a concrete case for the search-controller note. [quick-win]

2. **Measure discrimination near the decision boundary.** The two TerminalBench judges have similar archive-wide rank correlations, 0.72 and 0.71, but agreement with the measured ordering inside their respective top-five sets differs, 1.00 versus 0.50. These are separate search archives and small frontiers. They nevertheless show why a global correlation alone cannot establish reliable final selection. [experiment]

3. **Test how candidates are represented to the judge.** On the reported Polyglot archive, rendering final files raises Spearman correlation from 0.40 for diff chains to 0.68; swapping presentation order changes these to 0.43 and 0.67 while roughly doubling cost. This supports the tested representation choice, not a general claim that pairwise judgment is superior to scalar scoring. The file view still omits identical files and truncates long files. [experiment]

4. **Keep resource attribution separate from signal quality.** The paper's five-run speed analysis assigns most speedup to asynchronous expansion and evaluation, with judged speculative expansion adding further benefit. A Commonplace experiment should retain separate comparisons for scheduling, search guidance, and acceptance quality before attributing a cheaper improvement loop to its critic. [experiment]

## Limitations (our opinion)

**Search replication and selection effects.** TerminalBench has one search per condition. Three repeats of a selected agent estimate that agent's performance, not the expected quality of the search method. SWE-60 repeats use the same 60 tasks as search, and the reported means include the search observation plus three repeats. Polyglot's full 225-task evaluation includes the 50-task search subset, so it is not wholly disjoint held-out evidence. Transfer to other coding models remains within Polyglot.

**Unmatched resource comparisons.** Some baseline comparisons use different models and resource protocols. The o3-mini narrative describes 30 expansions, 42 CPU-hours, and about $150, while Table 3 reports 20 expansions, 59 CPU-hours, and $86.8. These figures should not be merged into one reproducible run specification. The text extracted from figures also does not supply every plotted numeric value.

**Judge scope and failure modes.** Full-file judging means the differing runtime files, with 30,000-character truncation, rather than unrestricted whole-program inspection. Static preferences can miss execution behavior, and the source acknowledges conservative judging that reverses the measured order of its two selected SWE-60 descendants. A scalar Bradley–Terry strength can hide tradeoffs between task families. The tests vary judge presence, model, input representation, and some search settings; they do not compare alternative multidimensional evaluation schemes or demonstrate pairwise superiority over scalar judgments.

**Theory and implementation boundaries.** The top-K argument assumes random, non-adaptive comparisons and latent judge utilities, unlike SIFT's adaptive incumbent comparisons. The no-starvation proposition concerns a fixed finite archive, not the growing search tree. Neither certifies downstream correctness. The paper describes restricted writable files and blocked evaluation-harness edits, but this ingest inspected no repository and executed no code. Mechanism and integrity claims remain paper-reported, and benchmark or cost results were not reproduced.

## Recommended Next Action

Update [A search controller is tested by what it brings to stronger evaluation](../notes/a-search-controller-is-tested-by-what-it-brings-to-stronger-evaluation.md) with SIFT as a bounded empirical example, preserving the separation between routing, final selection, and independent-search replication.
