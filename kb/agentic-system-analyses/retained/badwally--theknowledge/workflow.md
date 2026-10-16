---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "TheKnowledge workflow: source ingestion with model-proposed multi-page authorship, bounded repair, local admission and CLI delivery."
run-id: AAS-2026-10-14-theknowledge-319a64927ee3-01
reviewed-boundary: aca6e29e69c6a72b697b8178841d03e6296ee3fc
---

# TheKnowledge workflow report

## Workflow account

### Selection and evidence boundary

This account selects `wiki ingest <input> --domain <domain> --with-plan`, with a registered domain, without dry-run and without the caller's draft flag. This does not select uniformly strict page admission: returned page frontmatter can independently enable draft validation. It is representative because one shipped invocation combines source admission, retained-page context selection, model authorship, software verification and delivery. It is not a general-purpose delegated-agent team. The same code owns progression through both model calls and file application; the model returns proposals rather than independently writing pages. The existing route is [RT-RTE-ingest-authorship](runtime.md#rt-rte-ingest-authorship), with admission payload [RT-OBJ-plan](runtime.md#rt-obj-plan) and guidance path [RT-BAP-authorship-prompt](runtime.md#rt-bap-authorship-prompt).

Evidence is SRC-1 implementation and doctrine/design at the frozen revision in [boundary](boundary.md#source-register). Workflow inspection additionally checked `src/gateway/cli.py` result emission and ingest dispatch; `src/gateway/ops/ingest.py` source-write and authorship branches; `src/gateway/ops/apply_plan.py` application/recovery; `src/gateway/plan.py` repair-prompt construction; and `.claude/skills/wiki-ingest-triage/SKILL.md`. Correction inspection additionally traced returned markdown in `src/gateway/plan.py`, per-update draft selection in `src/gateway/ops/apply_plan.py`, and section/citation downgrade in `src/gateway/validator.py`. These are SRC-1 implementation anchors. No target execution, test run, provider interaction or successful delivered artifact was observed. The account establishes shipped coordination, not reliability or factual quality.

### Request and source admission

A caller supplies input, domain and flags. CLI dispatch refuses authored ingestion with an explicit domain lacking a policy, then calls `ingest` and passes its result to `_emit_result`. Initiation supplies the task; it is not per-page human approval. Caller identity does not establish whether a human or foreground agent initiated it. SRC-1: `src/gateway/cli.py`.

The shipped triage skill describes a foreground-agent procedure: assess fit, select an active domain, ask the user when ambiguous, announce planned pages, invoke ingest, then inspect created frontmatter and report the source ID. This is instruction, not proof of compliance. Its displayed command does **not** include `--with-plan`; therefore this report does not silently treat skill invocation as activation of multi-page authorship. SRC-1: `.claude/skills/wiki-ingest-triage/SKILL.md`.

> 4. **Plan before ingest** (hard rule — WIKI.md § 9): State which pages will be
>    created before running any command.
> --- `.claude/skills/wiki-ingest-triage/SKILL.md`

Conversion and canonical-source checks precede the per-source locked admission described in [RT-RTE-ingest-authorship](runtime.md#rt-rte-ingest-authorship). The filter model proposes score/rationale using domain guidance; code thresholds decide inclusion. Raw text persists independently of wiki-source admission. On the new-source path, multi-page authorship runs only if a source page was written. A rejected/review source can thus produce a successful source-ingest result without authored wiki pages. Force inclusion bypasses the filter, not subsequent plan validation. SRC-1: `src/gateway/ops/ingest.py`.

> if with_plan and wiki_written:
>     plan_result = _invoke_plan_and_apply(
> --- `src/gateway/ops/ingest.py`

### Model handoff and return

The orchestration code constructs a system prompt, formatted source text and selected existing pages, then calls the plan client. The baseline record retains the bounded source/body selection, whole-page context budget and default tool-free client. The model's assignment is full-page creation/update proposal, including citations and preservation of existing claims; its authority stops at returned text. Existing-page selection may omit relevant knowledge, so it does not establish complete reconciliation with the vault. SRC-1: `src/gateway/ops/ingest.py`, `src/gateway/plan.py`; [RT-BAP-authorship-prompt](runtime.md#rt-bap-authorship-prompt).

Code parses the returned text against the expected source ID and structured update shape. The symbolic Plan envelope names targets and operations; markdown bodies carry proposed knowledge and frontmatter. The parser preserves the model's full markdown content, so returned metadata reaches page admission rather than being replaced by the caller's flags. SRC-1: `src/gateway/plan.py`.

> content = item.get("content", "")
> --- `src/gateway/plan.py`

No supervisor model or separate critic agent decides the next step. There is no expected-answer oracle: validators supply structural and citation constraints, not a reference account of what the source proves. SRC-1: `src/gateway/ops/ingest.py`; [RT-OBJ-plan](runtime.md#rt-obj-plan).

### Verification, rejection and recovery

`apply_plan` validates all updates before writing. The baseline identifies schema/citation checks, citation-loss and shrink guards; these can veto proposed changes, but do not establish factual entailment. Admission mode is computed per update from parsed frontmatter **or** the caller flag. Model-supplied truthy `draft` metadata can therefore enable draft validation even in this selected invocation. A plan can mix strict and draft updates; strict validation of a processed page additionally requires its parsed `draft` value to be absent or falsey. The invocation alone does not enforce that condition. SRC-1: `src/gateway/ops/apply_plan.py`, `src/gateway/validator.py`; [RT-RTE-ingest-authorship](runtime.md#rt-rte-ingest-authorship).

> is_draft = bool(front.get("draft")) or draft
> --- `src/gateway/ops/apply_plan.py`

Missing required sections and detected uncited claims become warnings for draft updates, not rejection errors. Other checks remain active: the citation-loss and body-shrink guards run before draft selection, and draft mode does not bypass all schema/integrity validation. Draft updates also receive retained draft-start and unresolved-claim metadata. Thus the model proposes both knowledge and metadata that changes specific vetoes; code still owns admission, but the caller has not guaranteed strict citation vetoes. SRC-1: `src/gateway/ops/apply_plan.py`, `src/gateway/validator.py`.

> Draft mode (`--draft` ingest, `draft: true` frontmatter) downgrades the
> rule from rejection to a warning so partial work can be committed.
> --- `src/gateway/validator.py`

Parsing or application failure returns to the same orchestrator. Draft-downgraded warnings alone do not trigger repair; the loop tests application success rather than requiring warning-free strict validation. SRC-1: `src/gateway/ops/ingest.py`.

> errors = [] if result.success else list(result.errors)
> --- `src/gateway/ops/ingest.py`

One corrective attempt is allowed: the static system prompt remains, while the new user payload contains original source/context, previous response and errors. Repair construction caps the prior response at 20,000 characters, so the repair model need not receive the complete rejected proposal. A client-call exception instead returns immediate failure; it does not traverse the error-fed repair branch. SRC-1: `src/gateway/ops/ingest.py`, `src/gateway/plan.py`.

> user = build_plan_repair_prompt(
>     source_text, existing_pages, prior_response=raw, errors=errors
> )
> --- `src/gateway/ops/ingest.py`

> prior_response=prior_response.replace("\x00", "")[:20000],
> --- `src/gateway/plan.py`

On exhausted unsuccessful parsing/application, code best-effort saves the last response and errors under `.knowledge/rejected-plans/`. This is operator repair material, not an accepted page or an automatic next authorship round. A subtle delivery limit follows: the failed plan result can contain the saved-path warning, but the new-source outer branch forwards only its errors into an authorship-failure warning. The saved artifact can therefore exist without its path being exposed in the CLI warning. SRC-1: `src/gateway/ops/ingest.py`.

Accepted plans enter the `wiki-author` lock. Code snapshots prior page text, replaces each file, and restores snapshots on write exceptions. This is best-effort exception recovery, not crash-atomic multi-page delivery: restore errors are suppressed, validation precedes the lock, and subsequent backlinks, contradiction logging and operation logging are separate bookkeeping. A failure in authored updates does not undo the already-written raw/source page. The baseline supplies the rollback passage and limit in [RT-RTE-ingest-authorship](runtime.md#rt-rte-ingest-authorship). SRC-1: `src/gateway/ops/apply_plan.py`, `src/gateway/ops/ingest.py`.

### Delivery and later use

Delivery has two boundaries. Page delivery is accepted local filesystem updates plus the authorship report; accepted output may include drafts with section/citation warnings even without a caller draft flag. Application success is not strict finalization or proof of grounding. This route does not establish a CommitGate Git commit. Caller delivery is the CLI's printed result, touched paths, available report and warnings. An empty or already-current plan can return a successful no-op without creating new pages. If authorship fails after source admission, the outer result remains successful and CLI exits zero while printing a warning. Thus an `ok` line is not proof of completed multi-page authorship. SRC-1: `src/gateway/cli.py`, `src/gateway/ops/ingest.py`, `src/gateway/ops/apply_plan.py`.

> for w in result.warnings:
>     print(f"warning: {w}", file=sys.stderr)
> return 0
> --- `src/gateway/cli.py`

Retained accepted pages, including drafts, can reach later authorship and retrieval calls; default retrieval does not require strict finalization. This is a distinct later consumer, not part of the present workflow's verification: [RT-RTE-retrieve-answer](runtime.md#rt-rte-retrieve-answer) explains selection and answer-generation limits. No execution evidence establishes that a later consumer received these particular pages, complied with their contents or improved because of them.

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

#### On [RT-RTE-ingest-authorship](runtime.md#rt-rte-ingest-authorship)

Workflow selection: authored ingestion of a new source into a registered domain without the caller draft flag. This is not a guaranteed strict path: model-returned full markdown includes frontmatter, and a truthy `draft` value enables per-update draft validation. Strict section/citation checks additionally require absent or falsey returned draft metadata. The caller supplies input/domain/flags; orchestration code hands selected source/page context to the plan model, consumes returned JSON and owns repair/application. Validators can veto, but draft section/citation failures become warnings while other checks remain active. There is no compulsory human approval of generated pages or expected semantic answer oracle.

Workflow recovery: one error-fed corrective attempt for parse/application failure; draft-downgraded warnings alone do not trigger it. Immediate failure for a client-call exception. Repair carries at most 20,000 characters of the prior response. Exhaustion can save rejected-plan scratch, but the outer new-source failure result does not forward the saved-path warning. Source admission survives authorship failure.

Workflow terminal condition: successful application (possibly admitting drafts with section/citation warnings) or a successful no-op returns through the CLI; source-only success can also return zero with an authorship warning. Neither caller flag omission nor application success establishes strict finalization. Local page application, CLI success and Git commit are not interchangeable delivery conditions. Evidence and checked passages are in the Workflow account; no operational success is inferred.
