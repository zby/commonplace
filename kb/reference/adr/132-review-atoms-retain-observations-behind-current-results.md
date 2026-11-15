---
description: "Keep review observations and exact inputs behind replaceable current results; bound the admitted atoms, typed acceptance, freshness and independently reconstructed fixture trials"
type: reference/types/adr.md
status: accepted
---

# 132 — Review atoms retain observations behind current results

**Status:** accepted; implemented under the operator's bounded review commission.
**Date:** 2026-11-15
**Amends:** [ADR 127](./127-review-runs-as-workflows-over-result-files.md), for review-result ownership, acceptance, freshness and fixture execution. Its workflow, approval and publication boundaries remain.

## Context

A replaceable result answers what the current review says. It cannot alone preserve independent repeated judgments, rejected outputs or the exact uncommitted text assessed. Consumers also need mechanically readable findings and a way to test one review operation without changing its criterion identity or invoking a larger procedure.

Ordinary execution and controlled reconstruction have different retention costs. Capturing every ambient configuration in every ordinary run is disproportionate; reconstructing a trial from a commit alone loses dirty content, selected library bytes and the installed executor's identity.

## Decision

**Admit a bounded subset through one existing execution route.** Catalog gates, type and collection conformance, the four compression checks, and the critique, friction, premise-decomposition and compression-synthesis reports use `commonplace-review` over Workjig. Explicit draft gates use that same machinery without catalog publication. Sharing execution does not choose operation order, combine judgments or redesign full-pass/revise. Further admission needs explicit inputs, a result contract, deterministic acceptance and a justified freshness policy or an explicit unassessed state.

Each compression check is a verdict criterion, requested by its own id, such as `compression/detail-overhang`. Its local INFO is a `pass` outcome with `info` findings. Its freshness follows its `watches: [body]` and `staleness: changed` declaration. No request selects the four checks together, and `--all-gates` leaves them out. The compression bundle and the full pass keep running the checks in their own single report.

Friction, premise decomposition and compression synthesis are `report` criteria, selected as `friction`, `premises` and `compression-synthesis`. The review-result schema keys each report's shape to its criterion. Only critique supplies `attack-outcome` and critique's sections. Friction findings are ranked joints with an `UNSUPPORTED`, `THIN` or `HOLDS` reason, beside a filter line. Premise findings carry `HOLDS`, `DOUBTFUL` or `DEFEATED` with local or global routing. Neither is an overall verdict. Both use ordinary freshness over the whole note, the instruction and the output contract.

The synthesis judges compression findings supplied as `--input` files and launches no check. It runs alone on one note and publishes no current result. No hash covers its supplied findings, so its freshness is unassessed and its result stays a retained observation. The compression bundle and the full pass keep running friction, premises, the checks and the synthesis in their own reports, which are not result files.

Connect retains its route: its product is a connect report, and its candidates depend on the corpus, not on the note and criterion alone. Higher-order wordings remain experimental.

**Use one typed envelope without forcing one judgment.** The [review-result type](../../types/review-result.md) owns findings, verdict/report distinctions and the worker/controller field split. Workers supply assessment content; code supplies provenance and validates the completed artifact. Critique completion is not a favorable verdict. Structural acceptance does not endorse the judgment.

**Retain observations separately from current views.** A run owns exact target, criterion, prompt, contract and explicitly selected operational captures, raw launch outputs and completed results. A current result may be replaced without deleting that evidence. Retries and replay remain within an observation; independent fixture invocations have separate run roots. An observation's short identifier is run-qualified, not a globally unique execution identity. Improvement runs keep ownership of their edit-produced texts; removing their existing copies is not part of this decision.

**Keep execution inputs explicit.** Provenance references do not authorize browsing other runs or recursive dependency capture. Ordinary reviews may read authorized authored context; their whole environment is not frozen. Missing operational substance requires another explicitly supplied input or a contract repair. Capture hashes preserve exact bytes; normalized watched-part hashes retain their freshness semantics.

**Validate the full captured contract before asking workers.** It includes the library result type/schema closure and the applicable project collection contract. Controller-input or evidence-integrity failures stop rather than entering model correction. Correction stops when it would repeat an already rejected request. Completed bytes receive consistent validation at retained and current-result paths, including a result named `COLLECTION.md` in the review state tree.

**Freshness includes the output-contract fingerprint.** Note and criterion hashes alone are insufficient when the acceptance contract changes. Result reads also check retained evidence. One status operation shares immutable contract setup and current-input reads, not cached result or evidence bytes across operations. Named-note status reads only the selected pairs; whole-store status and project review summaries retain orphan inspection. Prompt and ambient reading context remain outside freshness, so freshness is not complete execution equivalence.

**Fixtures retain content, not an assertion of environmental identity.** Keep the committed tree, exact recoverable dirty content, selected inputs, library and executable source. Missing historical bytes block preparation or require an exact-hash repair. The current executor is an explicit substitute baseline, not a recovered historical executor. Each trial owns independent mutable files and Git state, bypasses freshness skips and publishes no live result. Resume continues only that trial.

The library inventory includes tracked and non-ignored authored files in Git, or visible package files in an installed library without Git. Hidden paths and report state are excluded from that inventory. Ignored operational files enter only as explicit input copies. A recorded inventory policy prevents silent reinterpretation of historical digests. Old result formats, run namespaces and unsupported fixture policies are not migrated through compatibility parsers.

## Considered alternatives

**A new operation framework or second state repository.** Rejected for this slice. Existing Workjig execution and run-owned records provide the needed boundary without another scheduler, storage authority or consumer migration.

**Only current results, or a new criterion ID for every trial.** Rejected. Replacement destroys comparison evidence, while changed IDs confuse execution identity with criterion identity and can alter worker-visible inputs.

**One universal verdict or merged adversarial methods.** Rejected. Critique tests an opposing case, friction tests concretization and inferential joints, premises tests assumptions, and higher-order review asks whether the artifact should change or exist separately. Similar findings do not establish substitutability. Likewise, prominence is not sentence simplicity; proportional development is not compressibility of useful detail; section-boundary repetition is not marginal contribution; structural collapse is not loss beyond a parent artifact. No criterion is retired merely because another can flag the same passage.

**Expose only combined compression or immediately register every report.** Deferred. Independent checks need independent inputs and acceptance; synthesis consumes a finding set rather than launching checks implicitly. Connect's corpus dependence and run-relative links need their own policy. Existing skill/full-pass routes remain; this decision does not admit them to `--all-gates`.

**Comprehensive ordinary snapshots or ambient recursive copying.** Rejected. Ordinary provenance stays lightweight; stronger retention belongs to fixtures. Neither route grants access through arbitrary evidence links or silently includes ignored source caches.

**Automatic migration or dual result writers.** Rejected. They would maintain competing acceptance paths and reinterpret old evidence. Historical runs remain evidence, not answers or approvals for new execution.

## Consequences

The operative consumers are the review CLI, typed acceptance and freshness readers, full-pass result consumers, project status, relocation and fixture creation/trials. Python enforces capture integrity, schema acceptance and publication boundaries; the type and operating instructions bind worker content and reading scope. The [review architecture](../review-architecture.md) and [operating guide](../README-REVIEW-SYSTEM.md) describe the supported interface.

Repeated trials and replacements now remain inspectable, and installed-project tests exercise separate library ownership. Contract edits can stale results; missing retained evidence can prevent inspection. A fixture may be refused even when the current note still exists, because exact historical content or its inventory policy is unavailable. There is no automatic evidence garbage collector.

Limits: the [acceptance record](../../reports/retained/review-atom-acceptance-20261115/README.md) supports the bounded machinery, not calibrated judgments. The live fixture reconstructed content but differed in advertised tools, MCP connectivity and workspace trust; automatic recovered-tool-error reporting, dependency artifacts, user configuration and provider internals remain gaps. No OS sandbox, environment equivalence, new composition, edit operation or stop operation is established by this decision.
