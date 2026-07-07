---
description: "Proposal: formalize the existing scripts/ directory as ad hoc tooling's committed home — name it in AGENTS.md, adopt a lightweight cleanup norm, and name an individual-script promotion signal"
type: kb/types/note.md
traits: [design-proposal]
tags: [kb-maintenance]
status: seedling
---

# Formalize `scripts/` as the accumulation substrate for ad hoc tooling

`AGENTS.md`'s Development section currently names two tiers of code: `python3` for "stdlib-only throwaway tooling," and the installed `commonplace` package for shipped commands. In practice a third tier already exists and has existed since the repository's first commit — the git-tracked `scripts/` directory, which holds ad hoc Python tooling that is committed (not thrown away) but hasn't (yet, or ever) earned a `commonplace-*` entry point. Nothing documents this tier or its lifecycle. This proposal names it explicitly and resolves the small set of choices that remain undecided about how it should be maintained.

## Current state (as of 2026-07-07)

- `scripts/` has been git-tracked since the initial commit (`195822b0`) and has 89 commits touching it.
- For most of the project's early history, `scripts/` held essentially the entire Commonplace CLI/review toolchain as a flat collection of files, evolving through direct edits. [ADR-014](../adr/014-scripts-as-python-package-one-tree-model.md) documents the promotion event: once the review system's DB helpers and multi-script pipelines could no longer be reliably invoked "from a sibling-import script layout across project boundaries," that cluster was extracted into the installable `commonplace` package with `commonplace-*` entry points. `git log --diff-filter=D -- scripts/` shows roughly 37 files removed from `scripts/` across that migration and its lead-up refactors.
- Post-migration, `scripts/` did not empty out. It currently holds 6 files, all last touched between 2026-04-12 and 2026-06-30:
  - `analyze_matrix.py`, `build_systems_matrix.py`, `render_systems_table.py` — a genuinely reused build/analyze/render pipeline over `kb/agent-memory-systems/systems.csv`, actively used across the comparative-review work.
  - `review-problems-for-note.py` — self-described in its own docstring as "a temporary fixing aid around the review-store database."
  - `session-tools.py` — a general Claude Code session-log inspection tool.
  - `move-reviews-to-subdir.py` — self-described as "One-off," last touched 2026-04-12 (the migration of `kb/notes/related-systems/` into `kb/agent-memory-systems/`), and unused since — a live instance of a stale script nobody has cleaned up.
- `AGENTS.md`'s python3 rule does not mention `scripts/`. Nothing in `kb/reference/` or `kb/instructions/` documents its role, contents policy, or expected lifecycle.
- No existing proposal or workshop (`kb/reference/proposals/`, `kb/work/`) covers this ground.

## The design

`scripts/` is the accumulation substrate the log item asked for — it already exists, is already committed, and already has one documented promotion event (ADR-014) at the subsystem scale. What's missing is not the substrate itself but three small pieces of formalization:

1. **Name it in `AGENTS.md`.** Extend the python3 rule so an agent deciding between a heredoc and a saved file has a documented decision point: if the code is expected to be reused (by this agent later in the session, or by a future agent), save it to `scripts/` instead of discarding it; if it's genuinely one-shot, a heredoc is still correct and cheaper.
2. **A lightweight cleanup norm.** `move-reviews-to-subdir.py` is the concrete evidence that scripts silently outlive their purpose. A norm should say roughly: when a script's docstring says "one-off" or "temporary," whoever finishes using it deletes it in the same session (or the same commit series) rather than leaving it for someone else to notice later. This keeps `scripts/` a substrate rather than a junk drawer without requiring a scheduled sweep or expiry timestamp machinery.
3. **A promotion signal at the individual-script grain.** ADR-014's signal was subsystem-scale ("sibling-import layout breaks down"). Nothing names when a single small script (like `review-problems-for-note.py`, which already self-identifies as a fixing aid) should graduate to a `commonplace-*` command instead of just persisting as a script indefinitely. Per [spec mining is codification's operational mechanism](../../notes/spec-mining-as-codification.md) and [progressive constraining commits only after patterns stabilize](../../notes/progressive-constraining-commits-only-after-patterns-stabilize.md), the natural signal is repetition-with-stable-interface: the script has been invoked, unmodified in its core logic, across multiple unrelated sessions or triage passes. A script whose interface is still changing every time it's used hasn't stabilized enough to promote yet, no matter how many times it's been touched.

## Free choices

- **Where the rule lives.** A short addition to `AGENTS.md`'s Development section (visible to every agent immediately) vs. a dedicated `scripts/README.md` (visible only to an agent that thinks to look inside `scripts/`, but affords more detail without bloating `AGENTS.md`). Likely both: a one-line pointer in `AGENTS.md`, detail in `scripts/README.md`.
- **How strict the cleanup norm is.** "Delete one-off scripts when done" (informal, relies on the finishing agent remembering) vs. a periodic sweep (e.g., during monthly triage, check `scripts/` for files untouched for N months and flag them for review). The evidence here is one stale file in 15 months — thin enough that informal-norm-only is probably sufficient for now; a scheduled sweep is over-engineering until there's more drift.
- **How the promotion signal is operationalized.** Left as a judgment call for whoever notices the recurrence (as this triage workshop's method already does for KB notes) vs. a mechanical rule (e.g., "3rd session invoking a script unchanged triggers a promotion candidate note"). A mechanical trigger risks the same one-shot-projection problem progressive constraining warns against; a judgment call, exercised periodically (e.g., at monthly triage), fits the existing triage cadence better.

## Adoption criteria

Adopt when:

- `AGENTS.md`'s python3 rule (or a linked `scripts/README.md`) explicitly names `scripts/` as the destination for reuse-expected ad hoc tooling, distinct from both heredoc-and-discard and the installed package;
- a cleanup norm is stated somewhere an agent finishing a one-off script would actually see it (the script's own docstring convention, or the rule itself);
- the promotion signal is named clearly enough that a future triage pass reviewing `scripts/` contents can apply it without re-deriving it from ADR-014 or the two theory notes cited above.

## Risks

- **Formalizing too much of what already works.** `scripts/` has functioned for 15 months without a written rule. The risk of this proposal is adding process weight to something informal practice already handles adequately — mitigated by keeping the adopted version to the minimum stated above (a rule line, a norm sentence, a named signal) rather than building tooling (expiry timestamps, automated sweeps) nothing has asked for yet.
- **The one drift instance is thin evidence.** One stale script in six is not strong evidence of a systemic junk-drawer problem. If this proposal is adopted, it should be adopted at the lightweight end of its free choices; if a future review finds `scripts/` has genuinely become cluttered, that's the point to escalate toward a scheduled-sweep norm.

---

Relevant Notes:

- [Ephemeral computation prevents accumulation](../../notes/ephemeral-computation-prevents-accumulation.md) — motivation: names the fork this substrate resolves in the accumulating direction, and the costs (no learning, no testing, no review, no reuse) `scripts/` avoids by existing
- [Spec mining is codification's operational mechanism](../../notes/spec-mining-as-codification.md) — mechanism: the promotion signal proposed here (repetition-with-stable-interface) is spec mining's general trigger applied to individual scripts rather than system behavior
- [Progressive constraining commits only after patterns stabilize](../../notes/progressive-constraining-commits-only-after-patterns-stabilize.md) — rationale: why the promotion signal should be stabilization-across-uses rather than a first-use or fixed-count trigger
- [014-scripts-as-python-package-one-tree-model](../adr/014-scripts-as-python-package-one-tree-model.md) — precedent: the one documented promotion event from `scripts/` to the installed package, at the subsystem scale
