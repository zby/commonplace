# Computational-model placement: execution versus assessment

## Boundary applied

On 2026-09-26 the next cleanup pass checked all twelve remaining
computational-model findings against the current head. Its subject is how
LLM-based programs execute: instruction interpretation, scoping, state,
tool-call loops, and orchestration of bounded calls, including computational
limits of those mechanisms. Its scope is unchanged.

A formal model, a computational evaluator, an improvement loop, or an LLM
component does not by itself meet that condition. A secondary execution
argument can qualify, but the twelve notes below instead develop search
policy, assessment warrant, learning, or content selection. All twelve
assignments are removed; the notes' arguments are unchanged.

## Assignment decisions

| Finding | Note | Reason |
| --- | --- | --- |
| TP-004 | [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) | The three functions define candidate search, reject-capable evaluation, and operative retention across human and computational systems. They do not explain bounded-call execution. Keep improvement-loop and its parent areas. |
| TP-013 | [Backtracking keeps lightweight search control provisional](../../notes/backtracking-keeps-lightweight-search-control-provisional.md) | The return path preserves a provisional search choice across artifacts, plans, or theories; it supplies no LLM execution or scheduling mechanism. Keep improvement-loop and its parent areas. |
| TP-024 | [Reach-assessment](../../notes/definitions/reach-assessment.md) | The definition compares what semantic, formal, and predictive assessment can establish. The prompt-length example tests a generalization, not call execution. Add evaluation and retain theory-builder with its parents. |
| TP-030 | [Commonplace as a reflective self-improving system](../../notes/evidence/commonplace-as-a-reflective-system.md) | The Commonplace trace establishes reflective coverage and actor allocation through a retained change. It does not develop LLM execution semantics. Add improvement-loop for the documented search, evaluation, and retention mapping. |
| TP-033 | [Causal and proof obligations are two formal routes to assessing explanatory-reach](../../notes/formal-systems-assess-explanatory-reach-through-causal-and-proof.md) | Causal and proof obligations assess a claim inside a formalized domain and expose the translation boundary. That is theory assessment, not an LLM computational limit. Add evaluation and discovery. |
| TP-035 | [Gödel machines are a proof-governed case of reflective self-modification](../../notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md) | The proof-gated self-rewrite construction is not an LLM execution model. The prompt-editing comparison concerns admission warrant, without developing instruction interpretation or bounded-call orchestration. Add improvement-loop for the explicit change-function mapping. |
| TP-037 | [Lightweight search control allocates further search without licensing adoption](../../notes/lightweight-search-control-does-not-license-adoption.md) | The claim distinguishes authority to allocate search from authority to adopt. It explicitly leaves the allocation mechanism unspecified. Keep improvement-loop and its parent areas. |
| TP-041 | [Memory-backed personalization can look like model improvement](../../notes/memory-backed-personalization-can-look-like-model-improvement.md) | The note separates retained intent, activation, and use, then designs crossed model/memory comparisons. It diagnoses missing information and intervention effects without developing interpreter semantics or call execution. Add context-engineering and evaluation; retain agent-memory and llm-reliability. |
| TP-048 | [Pointer design tradeoffs in progressive disclosure](../../notes/pointer-design-tradeoffs-in-progressive-disclosure.md) | The comparison explains which pointer helps select content for loading, with availability and accuracy tradeoffs. It does not explain the execution of the retrieval pipeline or surrounding calls. Replace computational-model with context-engineering and keep links. |
| TP-061 | [Task families and product families classify different things](../../notes/task-families-and-product-families-classify-different-things.md) | Task and product families classify different reuse and assessment scopes. Map-reduce is a single example of a task grouping, not an execution analysis. Add evaluation for the declared sampling and acceptance frame. |
| TP-064 | [Universal software factory needs a declared universality axis](../../notes/universal-software-factory-needs-a-declared-universality-axis.md) | The four universality axes constrain what factory capability claims and their evidence mean. Generic compiler expressivity is a contrast, not an LLM execution analysis. Add evaluation for the required evidence and resource frame. |
| TP-067 | [World models assess explanatory-reach through action-conditioned prediction](../../notes/world-models-assess-explanatory-reach-through-action-conditioned.md) | The note compares predictive, symbolic, and natural-language assessment and selective correction. World-model planning is not bounded LLM-call execution. Add discovery and learning-theory while retaining the theory-builder boundary assignment. |

## Suggested additions

| Entry | Result | Reason |
| --- | --- | --- |
| ADD-042 | Duplicate removal, closed | This entry contains a removal recommendation, not a proposed addition. Close it as a duplicate of TP-013; no additional tag change is needed. |
| ADD-062 | evaluation | The definition states what an assessment must test to distinguish genuine explanatory reach from fitted correlation. |
| ADD-074 | improvement-loop | The observed change traces candidate framing, evaluation, operative retention, and later dependence on the result. |
| ADD-087 | evaluation, discovery | Formal consequences test the reach of a proposed commitment; the note explains what those tests warrant and where formalization leaves judgment. |
| ADD-092 | improvement-loop | The change-loop table maps search, evaluation, authority, and retention under a proof gate. |
| ADD-121 | context-engineering, evaluation | Activation determines whether retained intent reaches the call; crossed model/memory interventions bound which effects can be attributed. |
| ADD-142 | context-engineering | The pointer comparison guides content selection and progressive loading, including the cost and availability of the routing information. |
| ADD-171 | evaluation | The task-family frame specifies prospective sampling, acceptance, permitted interactions, resource limits, and failure accounting. |
| ADD-195 | evaluation | Each universality claim needs a declared axis, covered class, inputs, adequacy relation, and resource bounds. |
| ADD-205 | learning-theory, discovery | Action-conditioned prediction and shift tests assess a commitment's explanatory reach; comparison with addressable theories explains different learning and correction paths. |

Nine entries are accepted. ADD-042 was a removal accidentally filed among
addition suggestions; it duplicates TP-013 rather than adding a tag. Discovery's
complete head now links its two new members. The two new improvement-loop
members are already reached through the reflection head linked from it.
Other affected complete parents reach these notes through their child heads.

## Parent checks

Learning-theory is restored on eleven notes. The fit checks are semantic,
not just a consequence of finding an existing child label:

| Findings | Child fit supporting the parent | Inventory entries |
| --- | --- | --- |
| TP-004, TP-013, TP-037 | Improvement-loop: required functions, recovery of provisional branches, and the authority boundary between search and adoption. | PG-015, PG-036, PG-079 |
| TP-024, TP-033, TP-067 | Theory-builder: assessment of stated commitments and the boundary with non-addressable predictors; the world-model note explicitly develops selective revision of localized theory as the contrast. | PG-051, PG-073, PG-125 |
| TP-030, TP-035 | Reflection: causally connected self-representation and changes to operative organization, in the Commonplace trace and the proof-governed construction. | PG-060, PG-074 |
| TP-061, TP-064 | Software-factory: the product-family boundary and what a factory universality claim can establish. | PG-113, PG-120 |
| TP-041 | Agent-memory: retention and activation of user intent, with authority and scope controls. LLM-reliability independently fits the diagnosis of absent, stale, or unused intent versus interpreter failure. | PG-084 |

The first four groups retain self-improving-systems through their named child;
that area is itself a learning-theory child. The memory note reaches
learning-theory through agent-memory and llm-reliability. The pointer note has
no declared parent requiring an addition. Initial inventory hashes and counts
remain historical; only disposition statuses changed. Twelve PG entries are
now resolved including the earlier PG-035 removal, leaving 117 open.

## Verification and limits

Explicit validation of all twelve edited notes, the discovery head, workshop
files, and workshop index passed with zero failures and zero warnings.
`commonplace-validate tags` also passed. Input hashes, metadata-only edits,
status counts, and eleven resolved parent entries were checked;
`git diff --check` passed. No pytest rerun is required for this Markdown-only
pass.

This pass removes twelve computational-model assignments
and adds 22 assignments: eleven learning-theory parents and eleven other
accepted additions. It resolves twelve assignment findings, nine actual
addition entries, one duplicate-removal entry, and eleven parent gaps.
Stored review results and the frozen placement baseline remain unchanged.
This is a placement judgment, not a factual re-review of the cited external
systems or a fresh independent assay. No inclusion rule was broadened.

## Input versions

SHA-256 of the twelve resulting notes and the heads used to judge their
existing children, additions, and parent membership.

| Input | SHA-256 |
| --- | --- |
| `kb/notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md` | `04e59697e5ed2b83efb4508527d00118f9bcf59f45951dde47bf5170a6351ec0` |
| `kb/notes/backtracking-keeps-lightweight-search-control-provisional.md` | `133b5688a795c005d7064cf320e7c30f60ed103afb1d330712e0a148d5e746dc` |
| `kb/notes/definitions/reach-assessment.md` | `b2fb5e05b0c2ca9cd4b7370c54dd69b6b88770494bea55ef6c07929a375c0230` |
| `kb/notes/evidence/commonplace-as-a-reflective-system.md` | `54e2d80ac58a4e7f1b10f22b09e3f5782200c53045255b8af73bffa47a1bc30f` |
| `kb/notes/formal-systems-assess-explanatory-reach-through-causal-and-proof.md` | `87266e4b741a0eecad6db4d4f9e65e48115cf01787f5bc29d43a9204a25704d5` |
| `kb/notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md` | `5bca385ba0d29c8b6c0dd550c870292e43a30fc21c8fc53e1025aba7338a09dd` |
| `kb/notes/lightweight-search-control-does-not-license-adoption.md` | `09ff4f2eda00467311881f048bc7057bcdc6cb08da0061a47a3de3ee326f4278` |
| `kb/notes/memory-backed-personalization-can-look-like-model-improvement.md` | `ee98102b1f2825c7bdea441e40e20ed3fdadada6186ae2c33e1f5852bcb31296` |
| `kb/notes/pointer-design-tradeoffs-in-progressive-disclosure.md` | `3fd54918e787bc9c5c214d9e5ca0a0e71059257216e5c864c3f780576491aee1` |
| `kb/notes/task-families-and-product-families-classify-different-things.md` | `764d39b8a72c5f69405368f9c6425a172e8377aef221b2f8e9176ded8d7e16b4` |
| `kb/notes/universal-software-factory-needs-a-declared-universality-axis.md` | `a452133a73d4935d0a57a3ec08a5adae2fd380229bf42c43b1911ad9968afc53` |
| `kb/notes/world-models-assess-explanatory-reach-through-action-conditioned.md` | `eac948f015373388bca4c626de5d88a7343c932f88f74308c0a288500719f526` |
| `kb/tags/computational-model-README.md` | `482d1626ac250dae25eb0247e4136d3ab9bbb06bcd9220d1ea68ff0a08d33bf8` |
| `kb/tags/evaluation-README.md` | `1268a09409705248434d19441ad1d3cc49b387e7b0ed39b76a4057c0cd31e669` |
| `kb/tags/discovery-README.md` | `5b05975bf985c4b3a0f7e395782714d83b1cce5e3474150c990939f6d3d0cf4d` |
| `kb/tags/improvement-loop-README.md` | `ea2f7ea2282c6caf80527cff91387552c4dc0e7d2406bc215052cbaaa45b35a5` |
| `kb/tags/self-improving-systems-README.md` | `81bb084cc147d4c7e4df574f2d339c30da1c58205b772b5bc7a8eb81da13e718` |
| `kb/tags/theory-builder-README.md` | `43c6f4adc99c4c1647b1fd813cabeef3cd1f2df1ff2f1bab3bd1961845860dc8` |
| `kb/tags/reflection-README.md` | `03069f68fe3c0324959e9193e99d32cbd88872bd212486368f798f47a83a4996` |
| `kb/tags/software-factory-README.md` | `ac2a805abefaf3be3233c994ed88140d4484e3c9174f0da0aa282166b54a9a8f` |
| `kb/tags/learning-theory-README.md` | `3effa98ce3c2d9db6a1aaf30769a3b179f994691a90e8222318e5f115305b5cf` |
| `kb/tags/agent-memory-README.md` | `d5d29a14971f9ef2cf4e623a1a5ac96b357061522d45990841018c1c557677e2` |
| `kb/tags/llm-reliability-README.md` | `b66bc38d119eab7dcf51d2e795e736467a0933c24807bb856a21aded79763da5` |
| `kb/tags/context-engineering-README.md` | `fa3e8c4eedfc0e222b21c5137986a296815ed881012447e8a2132460cc2d9955` |
