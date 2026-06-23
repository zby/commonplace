# Workshop: epistack-competition

Summary of the sibling **`epistack-casebooks`** repo and how the two repos exchange ideas. The deliberation that produced this (framing, tooling build list, case strategy) now lives in that repo's `AGENTS.md` and `kb/work/casebook-build/README.md`; this workshop is just the framework-side pointer.

## What the sibling repo is for

`../../../../epistack-casebooks/` (sibling of this repo under `/home/zby/llm/`) is a **consuming project** of Commonplace — a candidate entry to the FLF Epistemic Case Study Competition. It builds **agent-operated epistemic casebooks**: turning messy sources into source-grounded, typed, reviewable notes that expose what is known, what is contested, what depends on what, and where the gaps are — *without adjudicating truth*.

It exists separately, not as work inside this repo, so the entry demonstrates Commonplace's method **transferring to a real consuming project** rather than only documenting itself. It also keeps this repo's scope clean: application-specific casework belongs in consuming projects, not here.

Structure there: three isolated top-level case namespaces (`kb/lhc/`, `kb/eggs/`, `kb/covid/`), each with a `sources/` collection (captured material) and a `notes/` collection (the casebook, plain `note` type), plus a global `kb/notes/` for transferable theory. The sibling editable-installs this repo's `llm-commonplace` package, so framework changes here are live there without reinstall.

## How we move ideas between the repos

The single channel is **`epistack-casebooks/backlog-to-commonplace.md`**. The rule is one-directional with a clean boundary:

- **Casework → framework.** The sibling repo never edits its `kb/commonplace/` mirror (read-only installed framework). When casework reveals a framework need — a missing type, a validator/gate gap, a methodology insight — it **builds a local version first** (collection-local types), proves it on a worked case, and **logs the upstream need to the backlog**, classified: bug / type gap / instruction gap / validator gap / review-gate gap / methodology note.
- **Framework side (this repo).** We **watch that backlog** and promote upstream only the primitives that survived contact with a worked case. Build-local-first, upstream-what-survives keeps this repo from accumulating speculative machinery.

So this repo stays the framework; the sibling stays the casework; the backlog is the interface. The competition entry's value to Commonplace is whatever lands back here through that backlog.

## Status

Sibling repo scaffolded with a filled-in control plane and a kickoff briefing for its agent. First experiment queued there: provenance with plain notes on the black-hole case (does file-level linking suffice, or do claims need a source-span locator type?). Watch the backlog for the result.
