# Plan: epistack examples rebuild (two-repo)

Status: **ready to execute** (2026-07-13)

The rebuild spans two repos. **Part I** is framework-side work in this repository. **Part II** is casework executed in the sibling [`epistack-casebooks`](../../../../epistack-casebooks/) repo — copy [epistack-rebuild-plan.md](./epistack-rebuild-plan.md) there to drive it.

```
commonplace (this repo)          epistack-casebooks (sibling)
─────────────────────────        ────────────────────────────
Part I: prerequisites      →     Part II: init → migrate → rebuild
         watch backlog    ←     backlog-to-commonplace.md
         close workshop            (evidence flows one way)
```

---

## Part I — Commonplace (this repo)

Framework-side coordination. No casebook prose is written here.

### I.0 Why the framework side has work at all

The sibling editable-installs `llm-commonplace` from `../commonplace`. The rebuild is blocked or confounded if upstream is not in a known-good state, or if framework docs still describe the old surface the first build used.

### I.1 Prerequisites before copying Part II

Confirm the following **in this repo** before telling the sibling operator to run Phase 0:

| Prerequisite | Check |
|---|---|
| Package installable | `cd ../epistack-casebooks && command -v commonplace-validate` resolves against current checkout |
| ADR 045 shipped | `genre` required on snapshot schema; `source_type` rejected on ingest schema in `kb/sources/types/` |
| ADR 046 shipped | `commonplace-verify-quotes` exists; `commonplace-validate` runs verbatim quote check |
| ADR 044 shipped | Base note schema rejects global `status` |
| ADR 041/042 shipped | Collection-conformance gate reads `## Review` from `COLLECTION.md`; dialectical profile in `kb/reference/text-contract-profiles.md` |
| ADR 052 shipped | General freshness in `commonplace-store.sqlite`; `commonplace-freshness-{status,accept,ack,retire}`; review adapter over `review-pair` + `file-text` inputs ([freshness-architecture.md](../../reference/freshness-architecture.md)) |
| `commonplace-init` output current | `AGENTS.md.template` paths correct (review system README name, no dangling `kb/reference/README.md` bullet unless scaffold creates it) |
| Tests green | `pytest` passes on this checkout (includes freshness migration and store parity tests) |

If uncommitted framework changes in this repo affect validation, review, or init output, **commit or explicitly scope them** before the sibling rebuild starts — otherwise the sibling will be rebuilding against a moving target.

### I.2 Framework-side actions during rebuild

While Part II runs in the sibling:

1. **Watch `backlog-to-commonplace.md`.** New entries mean casework found a gap. Promote upstream only what survived contact with the rebuild; append Outcome lines when framework already has the answer.
2. **Do not edit the sibling repo from here.** The backlog is the channel.
3. **Do not fix the 18 quote mismatches in ADR 046 prose** by patching sibling notes — that ADR already says the rebuild owns them.
4. **Hold framework feature work** that would change schemas or contracts mid-rebuild unless the sibling operator agrees to a scope reset.

### I.3 Framework-side actions after sibling completion

When Part II closure criteria are met:

| Action | Where |
|---|---|
| Update competition pointer status | [epistack-competition](../epistack-competition/README.md) |
| Note conformance-clean demonstrations | [epistack-submission](../epistack-submission/README.md) if submission is still open |
| Promote any earned framework gaps | proposals, ADRs, types — driven by backlog entries with worked-case evidence |
| Close this workshop | delete `kb/work/epistack-examples-rebuild/`; remove from [kb/work/README.md](../README.md) |

### I.4 What does not belong in Part I

- Snapshot `genre` migration
- Ingest rewrites
- Casebook note authoring
- Collection-conformance runs on case material

Those are Part II only.

### I.5 Framework-side effort

| Task | Rough effort |
|---|---|
| I.1 prerequisite audit | 1–2 hours |
| I.2 backlog watching during rebuild | passive; respond to entries as they arrive |
| I.3 post-rebuild doc updates | 1–2 hours |

---

## Part II — epistack-casebooks (sibling repo)

All casework. **Copy** [epistack-rebuild-plan.md](./epistack-rebuild-plan.md) into the sibling repo before executing.

### Where to put the copy

```bash
cp ../commonplace/kb/work/epistack-examples-rebuild/epistack-rebuild-plan.md \
   kb/work/rebuild-from-scratch/README.md
```

Add a one-line entry to sibling `kb/work/README.md` if that file exists, and point `AGENTS.md` "current work" at `kb/work/rebuild-from-scratch/README.md`.

The copy is the **execution authority** in the sibling repo. If execution diverges from the canonical file here, update the sibling copy and log the delta in `backlog-to-commonplace.md` — do not silently fork.

### Part II summary (detail in the copyable file)

| Phase | What |
|---|---|
| 0 | `commonplace-init`; confirm ADR 045/046 schemas; confirm ADR 052 store commands |
| 1 | Archive old notes, ingests, review artifacts; reset operational store; keep sources |
| 2 | Declare tracked local source types (Phase 2.0); migrate 26 snapshots (`genre`, capture fidelity); rewrite ingests |
| 3 | Rebuild casebooks LHC → eggs → COVID with per-note quote gates |
| 4 | Corpus-wide validate + verify-quotes + conformance reviews + freshness demonstration |
| 5 | Backlog Outcomes; retire `post-commonplace-upgrade`; update `AGENTS.md` |

Closure criteria (both repos agree these are the bar):

1. Zero `commonplace-validate` failures on all six case collections.
2. Zero `commonplace-verify-quotes` mismatches.
3. Collection-conformance sweep documented.
4. Review freshness on `commonplace-store.sqlite` demonstrated (baselines registered, status fresh, edit surfaces staleness).

**Freshness scope note:** ADR 052 ships repository-wide freshness for registered `review-pair` targets. [`collection-maintenance`](../../reference/proposals/collection-as-artifact-freshness.md) targets (the Epistack-motivated ingest↔casebook membership check) remain a proposal — the rebuild demonstrates per-pair review freshness, not collection-wide membership staleness. Fresh ingests still must not claim empty casebooks.

### Part II effort

~5–7 working days for one careful operator. See the copyable file for per-phase breakdown.

---

## Shared constraints (both parts)

- Preserve captured sources; rebuild downstream only.
- Contracts frozen before casebook writing begins.
- No adjudication of the three controversies.
- Not the replication-plan clean-room experiment ([epistack-submission/replication-plan.md](../epistack-submission/replication-plan.md)).
- Track A factorial in sibling `post-commonplace-upgrade` stays archived, not relaunched.

## Optional follow-ons (neither part)

- Replication-plan independent-builder experiment
- Track A neutrality factorial redesign
- Framework promotion of epistack local source types (`epistack-snapshot`, `epistack-ingest-report`) — only after Phase 2.0 proves them on the rebuilt corpus and backlog entries ask for it
- Framework promotion of COVID `standing` block — local ingest schema first (Phase 2.0); upstream only if rebuild proves it
- `casebook-claim` collection-local note type — deferred until a second consuming project needs it
- Adopt and register `collection-maintenance` targets per [collection-as-artifact-freshness](../../reference/proposals/collection-as-artifact-freshness.md) — closes the ingest empty-collection validator gap at the freshness layer