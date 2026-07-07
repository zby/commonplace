# Investigation: ephemeral-helper-script substrate

## The claim/gap under test

`kb/log.md` line 19 (verbatim in the assignment): agents run stdlib throwaway scripts as inline heredocs and discard them; a designated home for ephemeral helper code would create the accumulation substrate that `ephemeral-computation-prevents-accumulation.md` predicts is otherwise lost, and a recurring script is spec-mining input for a future `commonplace-*` command per progressive-constraining. The triage README flagged this "bigger than a note, more like a small ADR," with four open design questions: location (workshop-style scratch dir vs `scripts/`), committed vs gitignored, lifecycle/expiry (substrate vs junk drawer), and the recurrence signal that trips promotion to a real command.

## What I read

- `AGENTS.md` (root), Development section: `Use python3 for stdlib-only throwaway tooling. Commonplace runtime code lives in the Python package as commonplace-* commands.` This is the entire rule — it names two tiers (throwaway python3, and the installed package) and does not mention any directory for code that is neither.
- `kb/notes/ephemeral-computation-prevents-accumulation.md` — the ephemeral/accumulating fork and its costs (no learning across runs, no testing, no review, no reuse) and benefits (no approval problem, no state management, no maintenance burden). Frames ephemerality as anti-codification.
- `kb/notes/spec-mining-as-codification.md` — the mechanism: watch behavior, identify repeated micro-actions, extract into deterministic artifacts, re-run. Names the general trigger ("a pattern has emerged from repeated execution") and includes the Codex harness-engineering precedent (manual observation → structural tests → automated monitoring).
- `kb/notes/progressive-constraining-commits-only-after-patterns-stabilize.md` — commit to symbolic media only where a pattern has proven itself across runs, not where a single run's projection admits it; version both spec and artifact.
- `kb/reference/proposals/README.md` — proposal contract: plain `note` type + `design-proposal` trait, no decision required, transferable requirements cited from theory via `rationale`, dated "Current state" anchor, description leads with "Proposal:".
- All 9 files in `kb/reference/proposals/` (titles/scope) and a repo-wide search for existing coverage of "scratch dir," "scripts/," "throwaway," "ephemeral script," or "helper script" in `kb/reference/proposals/` and `kb/work/` — no existing proposal or workshop covers this ground. (Several `kb/work/` hits were false positives: generic use of the word "scratch" in unrelated notes, or literal script files inside unrelated workshops.)

## What I found that the log item didn't anticipate: `scripts/` already exists and already does this

The repo root has a git-tracked `scripts/` directory, present since the very first commit (`195822b0`, "Initial commit: commonplace knowledge base framework") and still active today — 89 commits touch it. It is **not** gitignored (`.gitignore` has no `scripts/` entry). Its history shows exactly the accumulate-then-promote lifecycle the log item was asking someone to design:

- Early on, essentially the entire Commonplace CLI/review toolchain lived in `scripts/` as a flat collection of one-off and evolving Python files (`validate_notes.py`, `review_db.py`, `notes_selector.py`, etc.).
- `kb/reference/adr/014-scripts-as-python-package-one-tree-model.md` documents the promotion event: once the review system's DB helpers, schema loading, and multi-script pipelines could no longer be reliably invoked "from a sibling-import script layout across project boundaries," that whole cluster was extracted into the installable `commonplace` package with `commonplace-*` entry points. `git log --diff-filter=D -- scripts/` shows ~37 files removed from `scripts/` in that migration and its lead-up refactors — i.e., promotion-then-delete-the-scratch-copy already happened, at scale, once.
- Post-migration, `scripts/` did not go empty or disappear. It currently holds 6 files, all added or last touched between 2026-04-12 and 2026-06-30: `analyze_matrix.py`, `build_systems_matrix.py`, `render_systems_table.py` (the `kb/agent-memory-systems/systems.csv` analysis/build/render pipeline — genuinely reused across the comparative-review work), `review-problems-for-note.py` (self-described in its own docstring as "a temporary fixing aid around the review-store database"), `session-tools.py` (a general Claude Code session-log inspection tool), and `move-reviews-to-subdir.py` (self-described as "One-off").

So three of the log item's four open questions are not actually open — they're already settled by 15 months of revealed practice:

- **Location**: `scripts/`, not a workshop-style scratch dir.
- **Committed vs gitignored**: committed.
- **Promotion signal (at the subsystem scale)**: ADR-014 is a real, documented precedent — a cluster of scripts outgrows sibling-import invocation and gets extracted into the package. This is the "recurring script is spec-mining input" mechanism already fully instantiated once, not merely predicted.

## What's actually still open

1. **AGENTS.md's python3 rule doesn't mention `scripts/` at all.** As written, it describes only two tiers — heredoc-and-discard, or the installed package — which misdescribes what the project's own agents actually do (write a script into `scripts/` when reuse is expected). An agent reading only the rule has no way to discover the existing substrate or know when to use it over a heredoc.
2. **No lifecycle/expiry convention, and there's already one visible instance of drift.** `move-reviews-to-subdir.py` is explicitly self-labeled "One-off" in its own docstring, was last touched 2026-04-12 (relocating notes from `kb/notes/related-systems/` to `kb/agent-memory-systems/`, per its docstring and the corresponding commit), and has sat unused and uncleaned for close to three months. This is a small, concrete instance of exactly the "junk drawer" risk the triage README worried about — real, but thin (one stale file out of six).
3. **No named promotion signal at the small-script scale.** ADR-014 documents promotion when a *cluster* of scripts becomes an unmaintainable subsystem. It says nothing about when a single small recurring helper (e.g., if `review-problems-for-note.py`'s "temporary fixing aid" role turned out to recur indefinitely) should graduate to a `commonplace-*` command versus just staying a script. No signal is named for that smaller-grained case.

## Assessment

**Not note-worthy as a mechanism claim.** `ephemeral-computation-prevents-accumulation.md` and `spec-mining-as-codification.md`, read together, already give the complete "why": ephemeral computation forfeits the artifact that spec mining would otherwise operate on, and progressive constraining says the artifact should only be codified once it's proven stable across runs. This investigation didn't surface any transferable mechanism beyond what those two notes already establish — the interesting content here is Commonplace-specific practice, not a generalizable claim.

**Not a from-scratch design gap either.** The log item was written as though the accumulation substrate needed to be invented. It doesn't — `scripts/` has been serving exactly this role, committed, for the project's entire history, and ADR-014 already demonstrates the promotion pathway working once at the subsystem scale. Framing this as "needs design before adopting" overstates how much is actually undecided; most of what the triage README asked for is already decided by practice, just never written down as a rule.

**What's left is real but small: a documentation/formalization gap, not a from-scratch design problem.** Two things remain genuinely open — connecting AGENTS.md's python3 rule to the existing substrate, and naming a lifecycle/expiry norm plus a promotion signal at the individual-script scale — and there is concrete (if thin: one file) evidence of drift risk. This is narrower and lower-effort than "a small ADR"; it fits the proposal contract's "problem stated, forces stated, free choices marked, adoption criteria named" shape better than a note, because the remaining questions are unresolved *choices* about an already-mostly-decided piece of infrastructure, not a claim to assert.

## Verdict: WRITE-PROPOSAL

Scope: a narrowly-targeted proposal — not "design an accumulation substrate," but "formalize the informal `scripts/` convention that already exists": (a) whether/how to update `AGENTS.md`'s python3 rule to name `scripts/` as the reuse-expected destination, (b) a lightweight lifecycle/cleanup norm (using `move-reviews-to-subdir.py` as the concrete worked example of drift), and (c) a promotion signal for individual scripts at a smaller grain than ADR-014's subsystem-level trigger. The proposal's "Current state" section leans on the evidence gathered here (git history, ADR-014, the six current files) rather than re-deriving it.
