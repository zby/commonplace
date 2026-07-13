# Workshop: rebuild casebooks from scratch

Status: **ready to execute** (2026-07-13; freshness section updated 2026-07-13)

> **Origin:** This file is maintained in the Commonplace framework repo at `kb/work/epistack-examples-rebuild/epistack-rebuild-plan.md` and copied here to drive casework. Edit the copy in this repo during execution; promote durable changes back through `backlog-to-commonplace.md`, not by editing `kb/commonplace/`.

Rebuild the three FLF casebook demonstrations from **retained sources upward** on the current Commonplace surface — not patch the first build.

## Goal

Produce conformance demonstrations for LHC, COVID, and eggs that:

- carry `genre` on every snapshot and no `source_type` on ingest reports (ADR 045)
- pass `commonplace-validate` with zero failures on all six case collections
- pass `commonplace-verify-quotes` with zero mismatches on all casebook notes (ADR 046)
- satisfy collection-conformance review against each case's `notes/COLLECTION.md` (ADR 041)
- demonstrate review freshness on the general store (ADR 052): baselines in `kb/reports/commonplace-store.sqlite`, global status, staleness on edit
- carry no global `status` field and no inferred `user-verified: true` (ADR 044)

## Why rebuild, not repair

The first build was co-developed with the contract and upgraded in place. That left:

- **Stale scaffold** — `kb/types/` still has pre-ADR-045 snapshot and ingest schemas (`tags` required, no `genre`; `source_type` on ingests).
- **Quote failures** — 14 casebook notes: 63 match, 18 mismatch, 6 unresolved (`commonplace-verify-quotes`). ADR 046 deferred fixing these so the rebuild lands machine-checked.
- **Ingest decay** — Track B found all 26 `Connections Found` sections describing empty casebooks while every source was already cited. Fixed in prose, but the pattern shows why downstream artifacts must be rewritten, not spot-repaired.
- **Conformance drift** — the calibrated neutrality gate warned on 14/14 live notes; many failures were real uncited glosses, not gate bugs.

Keep captured sources (markdown snapshots, PDF siblings, methodology notes). Delete and rewrite ingests, casebook notes, and review artifacts tied to the old bodies.

## Evaluation boundary

- **Do not edit `kb/commonplace/`** — read-only mirror of the framework.
- **Do not adjudicate** any of the three controversies.
- **Do not repair old notes in place** — delete them from the working tree; git history retains the first build.
- **Do not reopen** `kb/work/post-commonplace-upgrade/track-a/factorial/` — preserved as failed-preparation evidence.
- **Do not infer `user-verified: true`** from validation or review results.
- Log framework gaps in `backlog-to-commonplace.md`; do not edit `../commonplace` directly.

## Current-state audit

| Layer | Count | Problem |
|---|---|---|
| Source snapshots | 26 | No `genre`; family duplicated in `tags` |
| Ingest reports | 26 | Still carry `source_type` (rejected by current schema) |
| Casebook notes | 14 | Quote verification failures on every collection |
| Review / freshness store | `kb/reports/review-jobs/`, `review-store.sqlite`, `commonplace-store.sqlite` | Tied to old note bodies; pre-ADR-052 layout if only `review-store.sqlite` exists |

Sources validate clean today only because the scaffolded schema is stale. After `commonplace-init`, the source layer will fail until migrated.

## Phase 0 — Refresh install surface

```bash
command -v commonplace-validate   # must resolve; if not, check ../commonplace is present and direnv is loaded
commonplace-init                  # regen kb/types/, skills, kb/commonplace/ mirror
```

Confirm after init:

- `kb/sources/types/snapshot.schema.yaml` requires `genre`
- `kb/sources/types/ingest-report.schema.yaml` rejects `source_type` (`source_type: false`)

Read before writing:

- `kb/commonplace/reference/adr/045-source-genre-is-a-single-open-field-on-the-snapshot.md`
- `kb/commonplace/reference/adr/046-verbatim-quotes-are-validated-against-their-cited-source.md`
- `kb/commonplace/reference/adr/052-general-freshness-store-review-first-migration.md`
- `kb/commonplace/reference/freshness-architecture.md`

Confirm the freshness commands resolve:

```bash
command -v commonplace-freshness-status
```

**Store on a from-scratch rebuild:** do not migrate old evidence. Phase 1 removes both `kb/reports/review-store.sqlite` and `kb/reports/commonplace-store.sqlite` if present. The operational store is created fresh on the first review command. (Migration via `scripts/migrate-review-db-v7-to-commonplace-store.py` lives in the framework repo and applies only when retaining baselines — not this rebuild.)

## Phase 1 — Pin contracts and archive downstream artifacts

### Frozen for this rebuild

Amend only if a worked case proves the contract cannot be followed — log amendments in `kb/log.md` and `backlog-to-commonplace.md`.

- Each case's `notes/COLLECTION.md` (dialectical/evidential contract, three-part citation convention, v2 `## Review` anti-rationalisation wording)
- Each case's `sources/COLLECTION.md`
- `kb/instructions/capture-long-documents.md`
- Dialectical profile: `kb/commonplace/reference/text-contract-profiles.md`

### Archive commit

On a dedicated branch:

1. Delete all `kb/{lhc,covid,eggs}/notes/*.md` except each `COLLECTION.md`.
2. Delete all `kb/{lhc,covid,eggs}/sources/*.ingest.md`.
3. Delete `kb/reports/review-jobs/`.
4. Remove `kb/reports/review-store.sqlite` and `kb/reports/commonplace-store.sqlite` if present (fresh store on first review use).
5. **Keep** all snapshots, PDF siblings, and `kb/notes/` methodology notes.

```bash
git add -A && git commit -m "rebuild: clear downstream artifacts, retain sources"
```

## Phase 2 — Source-layer migration

Use genre decisions from `kb/work/post-commonplace-upgrade/track-b/source-type-inventory.md` as the default mapping.

### Per snapshot (`kb/{case}/sources/<slug>.md`)

1. Add `genre: <value>` from the inventory **now** column.
2. Strip content-family entries from `tags` (`academic-paper`, `official-statement`, etc.). Keep topical tags only, or omit `tags`.
3. Leave `capture_note` intact unless it contradicts the new genre.
4. Re-read PDFs only when `capture_note` flags unread load-bearing regions.

Off-list genres the inventory named as load-bearing (`commissioned-safety-review`, `meta-analysis`, `government-report`, `intelligence-assessment`, etc.) should be used as off-list `genre` values. ADR 045 warns on unknown values — preferable to nearest-fit false confidence.

### Rewrite ingests

For each snapshot, fresh `.ingest.md` via `cp-skill-ingest`:

- No `source_type` in frontmatter.
- Classification prose names the snapshot's `genre`; explain any off-list value.
- `Connections Found` states the source's durable role against the **current** casebook — never "collection is empty".
- `Recommended Next Action` states real capture debt only.

**COVID standing block:** carry forward the pilot from `kb/covid/sources/COLLECTION.md` for the institutional cluster. Split `disclosed_interests` into `not-disclosed-in-document` vs `not-captured` where Track B found conflation. Remains collection-local — do not treat as framework-shipped.

### Gate

```bash
commonplace-validate kb/lhc/sources
commonplace-validate kb/covid/sources
commonplace-validate kb/eggs/sources
```

Zero failures before Phase 3. Off-list `genre` warnings are expected and should match the inventory.

## Phase 3 — Casebook rebuild

Order: **LHC → eggs → COVID**. LHC is the contract's first proof; eggs tests transfer to a different dispute shape; COVID is richest and most structurally ambiguous.

### Per-case procedure

1. Read `notes/COLLECTION.md`.
2. Use git history of deleted notes as a **coverage checklist**, not a structural template.
3. Write root orientation note plus notes for each major contested joint / dependency chain / institutional layer.
4. After each note: `commonplace-validate` and `commonplace-verify-quotes`.
5. After each case: collection-conformance review on all notes in that case; finalize jobs; record warns.

### Citation discipline (main failure mode of the first build)

- `verbatim` only when quoted characters appear in the linked snapshot (or its declared verbatim abstract/quotes).
- PDF-sibling captures: `paraphrase layer`; name the PDF in the locator; no quotation marks on paraphrase text.
- Press/court chains: `second-hand`; name the intermediary.
- Ellipses (`...`) and bracketed substitutions are **not** verbatim — shorten the quote or downgrade the marker.

### Neutrality discipline

Apply v2 `## Review` bullets while writing. No uncited evaluative glosses beside citations ("narrows but does not close", "answers the objection", etc.).

### Coverage anchors

**LHC** — dependency chain

- Root safety-dispute map
- LSAG cosmic-ray argument and dependency chain
- Plaga / Giddings–Mangano metastable black-hole dispute
- Strangelet branch
- Micro black-hole stability branch
- Wagner/Sancho lawsuit and court disposition
- Ord–Hillerbrand–Sandberg reliability critique of commissioned safety reviews

**Eggs** — competing syntheses

- Root dietary cholesterol / egg risk map
- 2015 guideline reversal (DGAC vs final Guidelines vs AHA)
- Zhong pooled analysis vs null meta-analyses
- Diabetic subgroup contested joint

**COVID** — parallel structures + institutional layer

- Root zoonosis vs lab-incident map
- Official assessments (WHO-China, SAGO, ODNI 2021/2023)
- Huanan market epicenter contested joint
- Furin cleavage / genomic features contested joint
- `standing.independence` on the zoonotic paper cluster

Target note counts from the first build (~6 LHC, ~4 eggs, ~4 COVID) are guides, not constraints.

## Phase 4 — Corpus verification and freshness demonstration

### Deterministic checks

```bash
commonplace-validate kb/lhc/sources
commonplace-validate kb/lhc/notes
commonplace-validate kb/covid/sources
commonplace-validate kb/covid/notes
commonplace-validate kb/eggs/sources
commonplace-validate kb/eggs/notes
commonplace-verify-quotes kb/lhc/notes kb/covid/notes kb/eggs/notes
```

| Check | Target |
|---|---|
| Validation failures | 0 |
| Quote mismatches | 0 |
| Quote unresolved | 0 (or relabel to paraphrase/second-hand) |
| Collection-conformance | Documented sweep; compare to old 14/14 warn rate |

### Review freshness (ADR 052 — shipped v1)

v1 registers **`review-pair`** targets with **`file-text`** inputs (`note` + `criterion` paths). Collection-wide membership staleness (`collection-maintenance` / `collection-text`) is **not** shipped — see `kb/commonplace/reference/proposals/collection-as-artifact-freshness.md`. Ingest `Connections Found` prose must stay correct by authoring discipline, not by an automatic membership check.

After collection-conformance jobs are finalized for the rebuilt corpus:

```bash
commonplace-freshness-status --json
```

Expect registered targets fresh (exit 0) once all finalized pairs match current file text.

**Staleness demonstration** (one note is enough; record which):

1. Edit a load-bearing sentence in a reviewed note without re-running review.
2. Confirm staleness surfaces:

```bash
commonplace-review-target-selector --json    # pair should appear stale
commonplace-freshness-status --json          # same target stale in global status
```

3. Optionally ack trivial mechanical fixes via `commonplace-ack-review` or re-run and finalize review for substantive edits.

Document: target count registered, fresh/stale counts before and after the edit, and which command surfaced the stale pair first.

### Freshness gate

| Check | Target |
|---|---|
| Operational store | `kb/reports/commonplace-store.sqlite` exists after first finalized review |
| Registered baselines | At least one finalized collection-conformance pair per case (or document why a case deferred) |
| Global status | `commonplace-freshness-status --json` exit 0 when corpus is current |
| Staleness on edit | Deliberate note edit → selector or global status reports stale |

## Phase 5 — Close out

### Backlog

Append **Outcome** lines to `backlog-to-commonplace.md` where this rebuild settles open entries. Do not rewrite earlier entries. Report at minimum:

- PDF-as-artifact / extraction-layer — still unstructured in capture, or earned a pattern?
- Standing block — survived rebuild? `disclosed_interests` split applied?
- Empty-collection validator gap — should not recur on fresh ingests; note ADR 052 v1 does **not** yet implement `collection-maintenance` (proposal only) — per-pair review freshness is demonstrated, membership staleness remains authoring discipline until that proposal lands

### Workshops and control plane

- Retire `kb/work/post-commonplace-upgrade/` once Track B findings live in the backlog and Track A factorial stays archived.
- Update `AGENTS.md` status paragraph when rebuild completes.
- Log operator interventions and any contract amendments in `kb/log.md`.

## What not to do

- Repair old notes in place.
- Re-capture sources unless fidelity is wrong for a load-bearing passage.
- Add framework types (claim type, link ontology, standing promotion) during rebuild.
- Launch Track A factorial or replication-plan clean-room arms from this pass.
- Block rebuild closure on adopting `collection-maintenance` targets — that is a follow-on proposal, not ADR 052 v1.

## Effort estimate

| Phase | Rough effort |
|---|---|
| 0 — init + confirm schemas | 1–2 hours |
| 1 — archive | 1 hour |
| 2 — 26 snapshots + ingests | 1 day |
| 3 — LHC (~6 notes) | 1–2 days |
| 3 — eggs (~4 notes) | 1 day |
| 3 — COVID (~4 notes) | 1–2 days |
| 4 — verification + freshness demo | half day |
| 5 — backlog + close | 2–3 hours |

**Total: ~5–7 working days** for one careful operator.

## What closes this workshop

1. All six case collections validate with zero failures.
2. Quote verification: zero mismatches.
3. Collection-conformance sweep documented.
4. Review freshness demonstrated on `commonplace-store.sqlite` (baselines, global status, edit → stale).
5. Backlog Outcome lines appended; `post-commonplace-upgrade` retired.

Delete this workshop directory when done, or leave a one-line pointer in `AGENTS.md`.