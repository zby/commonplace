# Multistage write: prototype standing is revision cost (binding plus lost investment)

Run of `cp-skill-write-multistage`, opened 2026-08-27 on the operator's direction.

- **Immutable run key:** `kb/notes/a-natural-language-theory-is-a-prototype-codified-or-rejected.md`
- **Current target (promoted 2026-08-27):** `kb/notes/prototype-standing-is-revision-cost-binding-plus-lost-investment.md` — written from `candidate.md` at the run-key path, validated clean, relocated with `commonplace-relocate-note --apply` (ProperDocs redirect added in `properdocs.yml`; three gitignored connect reports rewritten), validated clean again at the new path.
- **Mode:** edit
- **Collection:** `kb/notes/` (`kb/notes/COLLECTION.md`)
- **Type:** `kb/types/note.md`

## Incumbent recovery (recorded)

At run start the incumbent was absent from the working tree and had never been committed (`git log` shows no history at the path; the only repository mention outside `kb/reports/` is `kb/work/theory-mediated-methodology-article/README.md`). The full-pass packet's closing SHA-256 `a58b8fadad82…` matched `artifact_snapshots` row 958 in `kb/reports/state/commonplace-store.sqlite`. That snapshot was written byte-exact to `original.md` here and restored to the target path (verified SHA-256 `a58b8fadad8208008508970b2b2b53b90e210d79d6e11dd08f95f907c3f38b52`). The packet's `source.txt` (pre-pass, `97c331e8…`) is the earlier version and was not used as the incumbent.

## Inputs

- User brief (authoritative direction): recorded in `brief.md`.
- Incumbent: `original.md` (post-pass text, see above).
- Full-pass packet (review conclusions; for orchestrator, architect after source-first, auditor — not for reconstruction): `kb/reports/state/full-pass/a-natural-language-theory-is-a-prototype-codified-or-rejected/20260826T111746Z-e1ae52/full-pass-report.md`, `closing/critique.md`, `closing/premises.md`.
- Evidence paths: listed in `brief.md`.
- Backlinks lookup (2026-08-27): no library artifact links the incumbent path. `kb/notes/the-bitter-lesson-defense-portfolio-has-one-load-bearing-member.md` (named in the brief as the only library citer) currently cites `unformalized-improvements-need-a-pre-formal-stage-in-the-loop.md` for the cheap-formalization objection, not this note. Only `kb/work/theory-mediated-methodology-article/README.md` mentions the slug.

## Checklist

- [x] `brief.md`
- [x] `reconstruction.md` (completed 2026-08-27; markers carried to disposition: DEFINE expected-revision-cost combination; DECISION on coordination-value exception to the warrant rule; form scope fixed by the brief to natural-language vs symbolic; portfolio citer is a handoff, not a target edit)
- [x] `claim-disposition.md` (source-first saved 2026-08-27 before the incumbent was revealed; incumbent reconciliation appended by a second fresh architect after the first did not write phase 2). One central contribution: C1. Non-support dispositions: fold C9 into `formal-systems-assess-…`; cite existing C10, C12, C13, C14; omit C11, I14, I21, I24, I39.
- [x] `claim-skeleton.md` (no blocking markers; C8 → published open question; C2 correlation clause omittable)
- [x] `draft.md` (no NEW COMMITMENT lines; ~1380 body words; C2 correlation clause included with refuter)
- [x] `audit.md` (31 findings: keep 6, remove 4, clarify 20, ask user 1 — all resolved)
- [x] `candidate.md` (reconciled 2026-08-27)
- [x] `acceptance.md` — round 1 BLOCK (3 blockers, archived as `acceptance-round1.md`), fixed in `candidate.md`; round 2 PASS, 0 blockers
- [x] promotion — target written, validated, relocated, revalidated (see Current target). Citer reconcile: `the-bitter-lesson-defense-portfolio-…` does not link this note (its cheap-formalization row cites the pre-formal-stage note and its assertion is consistent with the rebuilt paragraph 8), so no citer edit was made; see handoffs.

## Unresolved human decisions and blockers

- F4 (audit): bounded operative trials vs the warrant rule — the brief keeps rule (b) and is silent on trials; treated by keeping the rule and publishing the trial case as an Open Question. User to confirm or redirect at handoff.
- Reconstruction markers routed to the architect: correspondence-branch home (recommendation: extend `formal-systems-assess-…`), coordination-value exception scoping, `expected revision cost` definition, unsourced illustrative examples (safety case, certification, training).

## Pending handoffs

- **C9 fold** (user authorization needed before execution): extend `kb/notes/formal-systems-assess-explanatory-reach-through-causal-and-proof.md` § "The formalization boundary" with (i) one sentence that codification relocates interpretation to the correspondence boundary (inline link `semantic-work-can-be-relocated-but-not-eliminated.md`), (ii) the purely-formal exception as the bound, with the authority criterion (natural language only an informal presentation of an authoritative formal definition), (iii) footer `evidenced-by` edges to `kb/agentic-systems/eigenius.md` and `kb/sources/discoverphysics-benchmarking-llms-out-of-the-box-scientific.ingest.md`. Scheduler example stays in the pre-formal note. Do not import the incumbent's "allowlisted axiom set" detail without checking the Eigenius artifact.
- **Defense-portfolio citer**: `the-bitter-lesson-defense-portfolio-…` cites the pre-formal note, not this note; whether it should gain a link to the rebuilt note is a portfolio edit under its role-classification rule (user decision).
- **Pre-formal note wording check**: `unformalized-improvements-need-a-pre-formal-stage-in-the-loop.md` defines the prototype by binding alone; align wording with the two-component claim (wording alignment, not a claim change).

- Correspondence branch ("Formal checking moves, but does not erase, interpretation"): disposition to be recorded in `claim-disposition.md` — either a new note (working title "Codification relocates interpretation to the correspondence boundary") or an extension to `kb/notes/formal-systems-assess-explanatory-reach-through-causal-and-proof.md`. Not to be silently deleted. Executing the chosen disposition is a separate handoff unless the user authorizes it inside this run.

## Acceptance review

Complete: PASS on round 2 (0 blockers).

## State

**Retained** after promotion because user-authorized decisions remain unexecuted (handoffs below). Nothing committed. Remove this directory and its `kb/work/README.md` entry once the handoffs are declined or completed.

## Index note

`kb/work/README.md` carried unrelated uncommitted edits at run start; the one-line entry for this run was added without staging anything (nothing is committed by this run).
