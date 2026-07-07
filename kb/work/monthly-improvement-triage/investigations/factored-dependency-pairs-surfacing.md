# Investigation: factored dependency pairs for review freshness (surfacing check)

## Item under test

From the triage README, Big-potential list:

> `kb/reference/proposals/factored-dependency-pairs-for-review-freshness.md` — not a triage candidate itself (already a finished design proposal), but it's the most recently touched file in the whole survey (edited 2026-07-04 and 2026-07-06) and worth surfacing: it generalizes the type-conformance-pairs pattern (ADR 038) to COLLECTION.md-as-gate and source-as-gate dependencies.

Scope, per the assignment: this is not a raw-log synthesis to judge for note-worthiness. It's a finished proposal already sitting correctly in the proposal lifecycle. The question is narrower — does anything further need to happen, or is "surfaced" the complete action.

## What I read

- The proposal in full (`kb/reference/proposals/factored-dependency-pairs-for-review-freshness.md`).
- Its full git history: `git log --follow -p` and `git log --all` for the path.
- `kb/reference/adr/038-type-conformance-reviews-use-the-type-spec-as-the-gate.md` in full, plus its own git history (three commits: created 2026-07-04, amended twice 2026-07-06).
- `kb/reference/proposals/README.md` — the proposal lifecycle contract.
- Working-tree state (`git status`, `git diff HEAD`) for the proposal file — clean, no pending edits.
- `src/commonplace/` for any implementation of `COLLECTION.md`-as-gate, source-as-gate, or cohort-scoped ack (grep across `src/commonplace/`, focused on `ack_gate_review.py`, `ack_trivial_note_changes.py`, `resolve_gates.py`).
- `kb/log.md` and `git log --all --grep` for any mention of "cohort-scoped ack," "source-as-gate," or "collection-as-gate" — none found.
- `kb/work/lineage-mechanisms/` — still an active, open workshop (the proposal cites `general-lineage-refresh-state-design.md` there by path, not link, per the no-workshop-links convention); it has not concluded or superseded this proposal.
- Existing notes searched for a companion generalized-pattern claim: `link-graph-plus-timestamps-enables-make-like-staleness-detection.md` (the make-analogy foundation, already generic), `a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md` (the derived-copy rule, already cited by the proposal as rationale), and a grep for "factor," "N-ary," "irreducibly," "pairwise" across `kb/notes/`.

## Finding 1: the "edited 2026-07-04 and 2026-07-06" premise is a filesystem-mtime artifact, not a git fact

`git log --follow -p` for the proposal file shows exactly one commit ever touching it: `c895e2bc` (2026-07-04), which *created* the file as part of shipping ADR 038 (type-conformance pairs). `git log --all` confirms no second commit. `git status` / `git diff HEAD` show no uncommitted edits either — the working tree matches HEAD exactly.

The file's on-disk mtime is 2026-07-06 07:33:58, which is what a plain `find`/`ls`-by-mtime sweep (as the triage README's method section describes: "a quick mtime check of `kb/reference/proposals/` for anything freshly touched") would surface. That mtime almost certainly reflects a checkout/worktree operation, not a content edit — checkouts stamp mtimes at checkout time regardless of the commit that last changed the content. The two 2026-07-06 commits that *are* real (`55a50cd2`, `07fa06a6`) touched the closely related `ADR 038` file (amending its wrapper-mechanics and `--all-gates` semantics text) — not this proposal.

So the recency signal that triggered this item's inclusion in the triage is not evidence of an actual edit needing a fresh look. This is worth noting as a methods correction for future triage passes (mtime sweeps over `kb/reference/proposals/` can false-positive on checkout noise; `git log` is the reliable signal), but it does not itself require a KB write — it's an observation for the coordinating session, not a new artifact.

## Finding 2: the 2026-07-06 ADR 038 amendments don't stale the proposal's current-state anchor

The two 2026-07-06 amendments to ADR 038 were:

1. `55a50cd2` — the type-spec-as-gate wrapper now *references* the type spec (names its path, worker reads from disk) instead of *embedding* its text in the prompt.
2. `07fa06a6` — `--all-gates` now includes the type-conformance cohort uniformly, instead of staying catalog-only/opt-in.

Neither contradicts anything in the proposal's "Current state (as of 2026-07-04)" bullets. The proposal already describes the wrapper generically ("neither `COLLECTION.md` nor a source snapshot is written as a Failure mode / Test procedure, so each needs a mechanical wrapper... or an authored review section") — a description that's if anything *more* consistent with the amended reference-not-embed mechanics than the original embed approach was. The `--all-gates` semantics change is a selection-flag detail the proposal doesn't depend on. The proposal's dated anchor does not need refreshing.

## Finding 3: adoption criteria are not met

The proposal names three adoption triggers. Checked each against current repo state:

- **Cohort-scoped ack** — "when the first real type or collection edit stales more pairs than per-note acking comfortably clears." No such edit has occurred: `ack_gate_review.py` / `ack_trivial_note_changes.py` show no cohort-scoped ack surface (no by-gate or by-type batch-ack option beyond the existing per-note `qualifying_pairs` path), and no commit or log entry mentions building one.
- **`COLLECTION.md`-as-gate or source-as-gate** — "when a note's conformance to its collection, or consistency with a distilled source, is first wanted as a reviewable judgment." Grepped `src/commonplace/` for any second/third gate source beyond the shipped `type` one (`resolve_gates.py`, `review_target_selector.py` area) — none exists. No commit implements it.
- **N-ary input-set model** — "only if a judgment appears that genuinely needs a third text in one prompt." No such judgment has surfaced; the `general-lineage-refresh-state-design.md` workshop item (the fuller lineage design this proposal deliberately narrows) is still open/in-flight, not concluded in a way that would force this.

No evidence anyone has acted on the proposal's remainder since 2026-07-06 — no commits, no log entries, no workshop notes reference it.

## Finding 4: no missing companion theoretical note

Checked whether "factor a new N-ary dependency into its own two-input pair, with the dependency as the gate, rather than widening one pair's input set" is a transferable claim currently absent from `kb/notes/`. It is not simply restated by existing notes — `link-graph-plus-timestamps-enables-make-like-staleness-detection.md` states the general link-graph/timestamp mechanism but not the pairwise-vs-N-ary factoring choice; `a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md` is about copy-enforcement, a different axis; `decomposition-heuristics-for-bounded-context-scheduling.md`'s "separate selection from joint reasoning" is adjacent (prefer narrow calls over wide joint ones) but is about LLM call scheduling, not dependency/staleness-tracking structure.

That said, the pattern as it currently exists is stated at exactly the altitude it's needed: once, precisely, in ADR 038's Consequences section ("The pattern generalizes by factoring: a new review dependency becomes a new two-input pair... instead of widening one pair's input set to N"), and expanded once in this proposal. It is currently scoped to one system (review-freshness gates) with exactly one shipped instance (type-conformance) and zero further instances. Generalizing it into a standalone `kb/notes/` claim now would mean asserting a transferable design principle from a sample size of one shipped instance plus zero adoptions of its stated generalizations — exactly the kind of premature synthesis the reach test in `kb/notes/COLLECTION.md` warns against (could someone say how it's wrong, not just incomplete? not yet testable with only one instance). If a second instance ships (`COLLECTION.md`-as-gate or source-as-gate), that would be the point to write the generalized note, grounded in two real instances rather than one instance plus a plan.

## Verdict: DISMISS-NO-ACTION-NEEDED

The proposal is exactly where it should be in its lifecycle: a dated, honest "not yet adopted, here's why" document, sitting in `kb/reference/proposals/` per ADR 028's contract, with accurate current-state anchoring and unmet adoption criteria correctly named as unmet. Nothing changed in the underlying system on 2026-07-06 that the proposal fails to reflect. No adoption trigger has fired. No generalized theoretical note is separable from the proposal yet without over-claiming from a single instance.

The triage README's "worth surfacing" note is itself the complete and correct action — it flagged the proposal for a human/agent to notice, and this investigation confirms there's nothing further to do. The one correction worth carrying back to the coordinating session: the "edited 2026-07-04 and 2026-07-06" framing overstates what happened (one creation commit, no subsequent edits to this file; the 07-06 activity was on the related ADR) — future mtime sweeps of `kb/reference/proposals/` should cross-check against `git log`, not raw file mtimes, before treating a file as freshly touched.

## Disposition

No note written. No compression-gate review run (out of scope per the DISMISS branch — see assignment step 7, which conditions the note-writing/review steps on a WRITE-NOTE verdict). This investigation report is the only artifact produced.
