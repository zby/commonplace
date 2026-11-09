---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "SIGN workflow account: caller-authored canon through compilation, rejection and artifact delivery, bounded before external agent consumption."
run-id: AAS-2026-11-09-sign-lang-379ffbdd642c-01
reviewed-boundary: "f4eb1a82b114615754bbe5c2e6f4255a4ec1eeba"
---

# sign-lang workflow report

## Workflow account

### Selection and evidence boundary

The representative workflow is **prepare a knowledge corpus for an agent: supply source, compile it, then expose the index and full documents**. It is selected because the README presents these steps together as its Quick Start, and compilation has a shipped implementation. This establishes a multi-step preparation workflow and a declared agent-facing continuation, not a complete multi-step agent execution. There is no established delegated-agent task, model decision, verification of an agent's answer, or final user-result delivery within this inspected path. The analysis stops at the external host boundary rather than joining the separate maintenance and import commands into an invented orchestration loop (SRC-1, `README.md`, `validator/src/compile.js`; [RT-CLM-agent-contract](runtime.md#rt-clm-agent-contract)).

The boundary remains complete artifact, partial loop as established in [boundary](boundary.md#boundary-and-evidence). Evidence is implementation for compilation and CLI control flow, and doctrine/design for the host continuation. Source inspected for this account: SRC-1, `validator/src/compile.js`, `validator/bin/sign.js` compilation/result/exception branches, `README.md` Two-Layer Delivery and Quick Start, and `spec/skill-reference.md`. The skill reference was read in full; it adds governance and delivery intent, not a frozen implementation of the external sign-draft skill. These are within the registered source at the reviewed commit, not additional sources. No execution trace was supplied, and no target code was run. Delivery and rejection below describe wired paths, not observed successes or failures.

### 1. The caller supplies a corpus and an output destination

The principal is the invoking caller. It chooses the source and output paths; the CLI passes them to `compile`. The workflow does not establish whether the author is human or computational. Supplying a source directory is not evidence that a human approved every document. The operative handoff is local filesystem content plus CLI arguments to deterministic JavaScript, not a natural-language assignment to a worker (SRC-1, `validator/bin/sign.js`; [RT-CMP-validator](runtime.md#rt-cmp-validator), [RT-RTE-compile-canon](runtime.md#rt-rte-compile-canon)).

The README starts with Markdown frontmatter, but the shipped parser's directory path discovers `.sign` sources. Consequently this account uses the implemented SIGN-source compilation route; it does not assert that the README's Markdown authoring example is translated by this compiler. The missing Markdown conversion is not filled in with the external importer ([RT-RTE-compile-canon](runtime.md#rt-rte-compile-canon), [RT-RTE-import-delegation](runtime.md#rt-rte-import-delegation); SRC-1, `README.md`, `validator/src/parse.js`).

### 2. Compilation performs a pre-write check

The compiler takes ownership of progression: parse the selected files, aggregate parse diagnostics, and run rules with strict links. The rule consumer receives parsed document/file pairs, not a model's interpretation of the whole knowledge corpus. Recognized errors veto compilation before artifact writing; warnings do not. This is structural checking, not verification that domain rules are true, human-authorized or obeyed by a future agent. There is no expected agent answer or reference outcome serving as an answer oracle here ([RT-RTE-compile-canon](runtime.md#rt-rte-compile-canon); SRC-1, `validator/src/compile.js`, `validator/src/rules.js`).

A separate `sign validate` pass is neither required by this CLI branch nor an equivalent acceptance gate. Its non-strict links and zero-document early success differ from compilation. The compiler's own error check is the relevant veto for this workflow, even if a caller previously obtained a validation success ([RT-RTE-validate-source](runtime.md#rt-rte-validate-source); SRC-1, `validator/src/validate.js`).

### 3. Selection changes what is handed onward

After admission, the compiler selects identified active documents for the index and manifest. It emits identity, links, a summary and optionally a compressed anchor, while omitting full rule bodies. Anchor exclusions are omitted and include patterns are capped at four distinct entries. A recipient of only the index therefore does not receive the complete domain guidance or complete coverage binding. This is static context preparation, not a model-driven retrieval decision or an isolated sub-agent context ([RT-RTE-compile-canon](runtime.md#rt-rte-compile-canon); SRC-1, `validator/src/compile.js`).

The full bundle uses a different selection granularity: it rereads and copies each entire file contributing any active document. A mixed-status file can therefore deliver inactive document text alongside active text. Strict link checking also occurs before active selection. Neither an active-only full bundle nor successful resolution by a later active-only host follows from the compiler's success. Rereading raw files further requires stable source inputs if the bundle is to correspond to the earlier parsed checks ([RT-RTE-compile-canon](runtime.md#rt-rte-compile-canon); SRC-1, `validator/src/compile.js`).

### 4. Delivery is a filesystem result, followed by a host responsibility

The compiler hashes the assembled bundle and writes the index, full bundle, JSON manifest and checksum. A successful return reaches the CLI, which prints diagnostics/summary and exits zero. At this boundary, “delivered” means these artifacts were written for a filesystem consumer; it does not mean an agent received or acted on them ([RT-RTE-compile-canon](runtime.md#rt-rte-compile-canon); SRC-1, `validator/src/compile.js`, `validator/bin/sign.js`).

The README's next handoff is an integration sketch: host code reads the index into a system prompt and provides `get_canon_doc(id)` through an externally supplied `canonBundle.getDoc(id)`. The index requests retrieval when full rule text is needed, leaving that choice to the consuming agent. The sketch does not implement a provider call, resolver, retrieval-failure recovery or downstream answer acceptance. Full rule delivery and compliance remain unobserved; no user-facing final answer can be traced through this boundary ([RT-BAP-canon-guidance](runtime.md#rt-bap-canon-guidance), [RT-CLM-agent-contract](runtime.md#rt-clm-agent-contract); SRC-1, `README.md`).

### Rejection, recovery and maintenance

The supported rejection path is a compile invocation with recognized parse/rule errors: compilation returns `ok: false` before the write stage, the CLI emits diagnostics and exits one. A source-read failure similarly returns a failed result. Output-directory creation failure is caught and returned; an exception during sequential artifact writes instead reaches the CLI's top-level catch and exits two. The source expresses this terminal exception behavior directly (SRC-1, `validator/bin/sign.js`):

> main().catch(err => {
>   console.error(err.message);
>   process.exit(2);
> });
> --- `validator/bin/sign.js`

No automatic repair, retry or transactional rollback follows in this path. The caller owns correcting source/path problems and invoking compilation again. Pre-write rejection can leave prior artifacts untouched but does not mark them current; failure after an earlier successful write can leave a partially updated artifact set. A checksum identifies bundle bytes, not successful deployment or a recovery protocol ([RT-RTE-compile-canon](runtime.md#rt-rte-compile-canon); SRC-1, `validator/src/compile.js`).

Governance doctrine assigns further obligations outside that check. In particular, human review is required to promote model-estimated facts to asserted authority (SRC-1, `spec/skill-reference.md`):

> LLM-estimated facts must carry `confidence: derived` or `confidence: estimated`
> and cannot be promoted to `confidence: asserted` without human review.
> --- `spec/skill-reference.md`

This is an authored rule, not evidence that this compilation path delegates to a human or records a human veto. Likewise, breaking-change revalidation is a requested downstream obligation, while diff and drift produce caller-visible signals rather than performing a review, source repair or production promotion ([RT-RTE-corpus-diff](runtime.md#rt-rte-corpus-diff), [RT-RTE-source-signals](runtime.md#rt-rte-source-signals); SRC-1, `spec/skill-reference.md`, `validator/src/drift.js`). These mechanisms can inform an enclosing workflow, but the inspected source does not connect them into a completed agent review-and-recovery loop.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

none declared in this member

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-compile-canon](runtime.md#rt-rte-compile-canon)

Workflow role: preparation and software admission, not delegated agent execution. The caller owns request initiation and recovery; code owns parse/check/select/write progression. Its successful terminal result delivers artifacts, not an accepted agent answer. The workflow must distinguish pre-write rejection from partial-write failure when deciding whether prior output is usable.

#### On [RT-BAP-canon-guidance](runtime.md#rt-bap-canon-guidance)

Workflow role: declared continuation beyond artifact delivery. The enclosing host must supply prompt assembly, document resolution, model invocation and any action/result acceptance. The described retrieval request does not establish that full guidance reaches the consumer or that it controls the final result.

#### On [RT-RTE-source-signals](runtime.md#rt-rte-source-signals)

Workflow role: optional maintenance input to an external review owner, not a required compilation predecessor or an implemented repair step. A drift signal supplies a reason to investigate; it does not complete a review or determine the corrected rule text.
