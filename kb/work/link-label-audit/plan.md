# Plan — Link-label vocabulary rollout

## Context

The audit ([`findings.md`](./findings.md)) validated the ADR 009 core and surfaced two genuine gaps (`contrasts`, `mechanism`), plus a directional-asymmetry principle that's load-bearing but previously implicit. Most off-vocabulary drift folds into existing ADR 009 aliases.

The drafts in this workshop realise the conclusions:

- [`adr-018-draft.md`](./adr-018-draft.md) — ADR that promotes the two new labels and states the asymmetry principle.
- [`linking-conventions.md`](./linking-conventions.md) — compressed vocabulary section (~700 tokens) staged for embedding inside `cp-skill-write/SKILL.md`. Not a library doc.
- [`extract_labels.py`](./extract_labels.py) — audit script (rerun to measure convergence).

## Architecture

Two layers, no intermediate distillation file:

1. **Canonical — ADRs 009 + 018 + `linking-theory.md`.** Decision records and theory. Source of truth. Consulted when the vocabulary changes.
2. **Operational — compressed section embedded inside `cp-skill-write/SKILL.md`.** Loaded when writing. Updated as part of any ADR vocabulary edit.

No `kb/instructions/linking-conventions.md`. An intermediate doc that exists only to be copy-distilled from ADRs is a drift trap — authors touch it without touching the ADR, and the "canonical" version quietly diverges.

Reading links needs no instructions: labels like `grounds`, `extends`, `contrasts` are transparent English for a competent LLM. Only *authoring* links needs the compressed vocabulary.

## Steps

### 1. Land ADR 018

Pre-action gate: confirm target path.

- Move `adr-018-draft.md` → `kb/reference/adr/018-link-vocabulary-add-contrasts-mechanism-and-directional-asymmetry.md`.
- Refix relative paths (workshop `../../reference/` → ADR-local `./`; `./findings.md` → `../../work/link-label-audit/findings.md`).
- Keep status `proposed` until step 5.

### 2. Update `COLLECTION.md` outbound tables

Pre-action gate: show per-file diff.

- `kb/agent-memory-systems/COLLECTION.md` — add `contrasts` to descriptive→descriptive and descriptive→theoretical; prune labels with near-zero corpus use.
- `kb/notes/COLLECTION.md` — add `contrasts` and `mechanism` to theoretical→theoretical; prune `since`/`because` (inline grammar, not footer labels) and matrix-only labels absent from corpus (`qualifies`, `derived-from`).
- `kb/reference/COLLECTION.md` — add `contrasts` to descriptive→descriptive; prune `rationale`/`justification` if near-zero.
- `kb/instructions/COLLECTION.md` — review outbound labels; prune if unused.

Each edit is local and reversible; batch the review but apply per file.

### 3. Recompile the topology

Run `cp-skill-compile-collections` to regenerate `kb/reports/collection-topology.md` from the updated COLLECTION.md files. The topology stays as a compiled cache for cross-register tooling (connect, audit); its role in writing is dropped.

Note: the compile skill does not yet emit vocabulary definitions and does not need to. Definitions live in the write skill's embedded section; topology carries only collections + per-edge labels.

### 4. Embed compressed vocabulary inside `cp-skill-write`

Pre-action gate: review embedding location within SKILL.md.

- Copy the current `linking-conventions.md` body (this workshop's compressed section) into `kb/instructions/cp-skill-write/SKILL.md`, most likely as a new top-level section before "Universal mechanics" or folded into it. Title the section `Linking conventions`.
- Delete the previous inline "Links" paragraph if it now duplicates anything.
- Do NOT also create `kb/instructions/linking-conventions.md`.

Other link-authoring skills (`cp-skill-connect`, `cp-skill-revise-*`, `cp-skill-ingest`, review skills) are deferred. Each will either embed its own short section or adopt a shared pattern when we get to it. The write skill is the priority author and the immediate target.

### 5. Accept ADR 018

After steps 1–4 are in place and self-consistent, flip ADR 018 status from `proposed` → `accepted`. Update `**Date:**` if it moves across days.

### 6. Measure convergence

Rerun `extract_labels.py` after a period of authoring under the new rules (say, two weeks of normal work). Compare label distribution to the current baseline. Expect: off-vocab counts shrink as drift-labels fold into canonicals; `contrasts`/`mechanism` usage stays stable where it fires now; `contradicts` remains rare (possibly confirming the KB is low-conflict, possibly surfacing a hygiene issue for a separate workshop).

## Update discipline

Any change to ADR 009 or ADR 018 that touches the vocabulary **must** re-sync the compressed section inside `cp-skill-write/SKILL.md`. Add this to ADR 018's "Not changing" section so future edits don't drop it.

## Deferred / out of scope

- **Unlabelled 32%.** Sample the prose-only footer links to see whether the prose itself carries decision-relevant content, or whether authors are genuinely skipping labels. Separate analysis.
- **`contradicts` under-use.** One use on the biggest edge is striking. May be a hygiene issue (contradictions getting buried as `tension` or hedged phrasing) or a converged KB. Worth a dedicated workshop, not this one.
- **Workshop / source / managed register vocabularies.** The current COLLECTION.md tables declare these edges permissive or blank. The audit shows the same ADR core works across them; a separate pass could formalise, but it's not urgent.
- **Other link-authoring skills** (connect, revise, ingest, review). Each will need either an embedded section or a shared pattern; figure out per skill when we get there.

## Success criteria

- Agent loading `cp-skill-write` makes correct label choices without consulting ADRs or the audit.
- Drift-labels (`sharpens`, `applies`, `motivates`, `compares`, etc.) decline in the next audit.
- No drift between ADR 018 and the embedded section (because updates touch both as a single change).
- Topology stays tight as the per-KB edge cache for connect-path use; it doesn't try to carry vocabulary definitions.
