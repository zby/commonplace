---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Antinomia workflow account: user-requested Hunter scan through bounded model comparison, result delivery and persistent false-positive rejection."
run-id: AAS-2026-11-08-antinomia-19694628edc2-01
reviewed-boundary: "6fafd01082fbecb2a18803500a1abe70a2bdc9f4"
---

# Antinomia workflow report

## Workflow account

### Selection and evidence boundary

The representative workflow is **Hunter scan → displayed contradiction candidates → optional human false-positive dismissal → suppression on a later scan**. It was selected because it connects retained knowledge, bounded model context, structural verification, an explicit rejection decision and later consumption of that decision in one shipped path. Delivery means displaying reflective suggestions, not resolving the contradictions. The path is already declared in [RT-RTE-hunter-scan](runtime.md#rt-rte-hunter-scan) and [RT-RTE-pair-dismissal](runtime.md#rt-rte-pair-dismissal); this member adds workflow interpretation rather than duplicate identities.

All evidence is SRC-1 at the frozen revision. Implementation establishes wired progression; prompt/UI wording establishes requested behavior and warnings. No supplied execution trace establishes a successful scan, actual user scrutiny or accuracy. Added detailed inspection covers `flows/hunter.ts`, `views/HunterResultsView.ts`, Hunter normalization in `ai/parseResponse.ts`, and Hunter command/abort hooks in `main.ts`. These are included paths under the existing boundary, not new sources. Provider execution and Obsidian rendering/storage remain external dependencies, as stated in [the boundary](boundary.md#boundary-and-evidence).

### 1. Request and context handoff

The human starts Hunter from the command palette or the result view's Run Hunter button. The focused command checks that the active Markdown note is an open tension or substrate before passing it as the focus. Code, not the model, owns progression. Missing profile credentials or fewer than two eligible notes produces a notice and returns before inference (SRC-1, `main.ts`, `flows/hunter.ts`, `views/HunterResultsView.ts`; [RT-RTE-hunter-scan](runtime.md#rt-rte-hunter-scan)).

The flow reads cached type/status metadata, sorts candidates by modification time and applies the configured note cap. Focus mode places the focus first and fills the remaining slots with other candidates. For each selected note, code strips frontmatter, trims the body and sends only its bounded prefix, labeled by basename and type. The model therefore does not receive the whole vault, omitted body tails, or the dismissal metadata. Omitted text remains in the vault, but this request has no automatic retrieval step to fetch it. This is deterministic selection and truncation, not a delegated worker frame or model-generated compaction ([RT-RTE-hunter-scan](runtime.md#rt-rte-hunter-scan), SRC-1, `flows/hunter.ts`).

The backend receives one assembled user message plus the Hunter system prompt and optional friction suffix through [RT-RTE-model-request](runtime.md#rt-rte-model-request). The request asks for pairwise comparison or focus-only pairs and structured JSON; that instruction does not establish that all pairs were considered. The configured model is a returning text computation, not a worker with authority to edit the vault. No child agents, task queue or tool-execution handoff occur in this traced chain ([RT-CMP-model](runtime.md#rt-cmp-model), [RT-BAP-prompt-policy](runtime.md#rt-bap-prompt-policy)).

### 2. Response verification and recovery

Code accepts an extracted `pairs` array or legacy `contraddizioni` array. A structurally unparseable first answer triggers exactly one new request with a stricter system suffix and the same assembled note context. The second call does not receive the previous answer as conversational history; the suffix describes the format failure. An empty array is a usable structure and stops retrying. Network errors and aborts return immediately rather than entering the format-repair retry (SRC-1, `flows/hunter.ts`; [RT-RTE-hunter-scan](runtime.md#rt-rte-hunter-scan)).

> if (rawPairs) break; // got a structure — stop retrying
> --- `flows/hunter.ts`

If both answers lack the expected array, the flow clears loading state, opens an error modal and returns without replacing the view's prior run. An optional Open raw response action writes a debug note through `createNote`; it is not admission of a verified contradiction. Recovery beyond that bounded retry belongs to the user, who can inspect the raw output, fix backend configuration or rerun. The failure branch explicitly returns after the error UI (SRC-1, `flows/hunter.ts`).

> "The AI replied but didn't return a valid pairs[] structure, even after a stricter retry. This often happens with local reasoning models that spend all tokens on internal <think> blocks, or with very strict JSON-mode responses.",
> --- `flows/hunter.ts`

Normalization maps English/legacy field names and confidence labels. Unknown confidence becomes undefined, which the result view displays and sorts as medium; this is a presentation default, not a new assessment. Verification checks nonempty distinct note names, selected-basename membership, nonempty descriptions and focus involvement where applicable. It then removes pairs matching retained dismissal keys. It does not test whether the prose describes a real contradiction. There is no answer oracle or automatic semantic acceptance test; the human remains the substantive judge ([RT-RTE-hunter-scan](runtime.md#rt-rte-hunter-scan), SRC-1, `ai/parseResponse.ts`, `flows/hunter.ts`, `views/HunterResultsView.ts`).

> const confidence = c.confidence ?? "medium";
> --- `views/HunterResultsView.ts`

Stop signals the plugin abort controller; the flow races the provider call against an abort rejection and returns to idle when that rejection wins. This is a local recovery/control path, not a universal provider cancellation guarantee. The transport-dependent distinction is retained in [RT-RTE-model-request](runtime.md#rt-rte-model-request). Prior results may remain visible after an error or stop; they are not evidence of completion of the newly attempted scan (SRC-1, `main.ts`, `flows/hunter.ts`, `views/HunterResultsView.ts`).

### 3. Delivery and its limits

For a parsed response, code constructs run metadata and the filtered pair array, updates last-run settings, builds friction metadata and calls the results view's `setRun` when a compatible view was obtained. `setRun` stores the run and renders it. The flow also emits a pair-count notice. Because the call to the view is optional, reaching the final notice alone does not prove that the result was rendered in a live host (SRC-1, `flows/hunter.ts`, `views/HunterResultsView.ts`).

> hunterView?.setRun(run);
> --- `flows/hunter.ts`

The view displays timestamp, selected/candidate counts, model and duration, warns about excluded notes, and renders pairs sorted by reported confidence and note name. Its empty-result message means no surviving candidates in that run, not a proof that the vault has no contradictions. A permanent disclaimer frames the result as reflective material. The friction card is displayed, but it does not establish that the user read it or validated the pairs ([RT-RTE-hunter-scan](runtime.md#rt-rte-hunter-scan), SRC-1, `views/HunterResultsView.ts`).

> "⚠ Reflective prompts, not truths. The AI can hallucinate. Do not use to decide in real situations."
> --- `views/HunterResultsView.ts`

Result links and action rows resolve basenames against current vault files. For a currently open tension, the row offers Elevate and Resolved; eligible typed notes also offer Defeated. These are separate human-triggered operations, not automatic continuations chosen by Hunter. In particular, elevation opens an editable form under [RT-RTE-rule-admission](runtime.md#rt-rte-rule-admission); the displayed pair does not itself produce or admit a principle. Duplicate basenames, renames and intervening edits limit identity and freshness. Metadata/vault events rerender the existing run rather than performing a new model comparison (SRC-1, `views/HunterResultsView.ts`).

### 4. Human rejection and later effect

The × control marks a displayed pair false positive. Its callback awaits the dismissal write, removes that pair in either orientation from the current in-memory result and rerenders. The write helper finds notes by basename and adds reciprocal entries to `hunter_false_positives`. These are sequential host writes, not a two-note transaction. A missing file is skipped, so completion of the callback is not an assurance that both notes received an entry. No automatic rollback is shown; explicit undismiss removes the peer entries ([RT-RTE-pair-dismissal](runtime.md#rt-rte-pair-dismissal), SRC-1, `flows/hunter.ts`, `views/HunterResultsView.ts`).

> await this.plugin.dismissContradiction(c.note_a, c.note_b);
> --- `views/HunterResultsView.ts`

On a later scan, the same notes may still be selected and sent to the model. Code reads dismissal arrays from selected notes, builds sorted pair keys and filters matching returned suggestions. Thus the retained rejection reaches a deterministic output consumer, not the model's reasoning context. The human supplies the judgment; code gives it exclusion force while identities and retained metadata match. It is reversible display suppression, not demonstrated learning by the model or measured improvement in contradiction detection ([RT-BAP-dismissal-filter](runtime.md#rt-bap-dismissal-filter), [RT-RTE-pair-dismissal](runtime.md#rt-rte-pair-dismissal)).

The workflow ends at candidate delivery unless the human chooses an action. Rejection changes later filtering; elevation/resolution/archive require new explicit decisions. The code supplies a bounded comparison-and-review mechanism, not evidence of successful resolution or autonomous criticism-led iteration.

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

#### On [RT-RTE-hunter-scan](runtime.md#rt-rte-hunter-scan)

Workflow role: bounded proposal generation and candidate delivery. Code owns selection, retry, structural rejection and view handoff; the model supplies comparison prose; the human judges substance. Successful construction of the run object is not host-observed delivery, semantic acceptance or contradiction resolution. A stale prior run can remain after an unsuccessful new attempt.

#### On [RT-RTE-pair-dismissal](runtime.md#rt-rte-pair-dismissal)

Workflow role: explicit human rejection with a reversible later output effect. Current-view removal follows the awaited persistence callback, but callback completion does not establish reciprocal-write atomicity. Future suppression depends on metadata being read and pair identities still matching; the selected notes remain visible to inference.
