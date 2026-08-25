---
description: "Accepted decision that commit messages keep the practiced imperative subject, carry migration narrative in the body, and use optional Decision, Workshop, and Model trailers derived from named git read paths"
type: ../types/adr.md
tags: []
status: accepted
---

# 075-Commit messages carry read-path trailers

**Status:** accepted
**Date:** 2026-08-25

## Context

[ADR 074](./074-git-is-the-change-history-layer.md) made git the change-history
layer of the source checkout and declared its first read path: revising an ADR
reads `git log --grep` for the commits that implemented it. It asked commit
bodies to name the ADR, deferred a formal trailer until drift was observed, and
moved migration narrative out of ADRs into commits.

The history at that point held 2,950 commits. Subjects were already uniform
without a written rule: imperative sentences, median 47 characters, 90th
percentile 71. Bodies were not. About 230 commits named an ADR, in mixed forms
(`ADR 074`, `ADR-074`, a bare number), including commits made in the same
session that declared the read path. A `--grep` over the corpus therefore
returned an unreliable subset. One trailer already existed de facto:
`Claude-Session:` on 364 harness-made commits, parseable by
`git interpret-trailers` though nobody had chosen it as a structured slot.

Three further read paths were live or wanted. Reconstructing a sweep or
episode had been done by hand three times from `git log`. `kb/work/lineage-mechanisms/`
names the commit message as the carrier for which model performed a
merge-back edit when volume is low. And `git log --follow` on one artifact had
broken where a relocation commit also carried content edits.

## Decision

Conventions are admitted only when a named read path consumes them. Four are
adopted; `AGENTS.md` `## Git` is the operative surface.

**Subject.** Keep the practiced form and write it down: an imperative sentence
under about 72 characters that says what changed. No type prefixes or scopes.

**Body carries what the ADR no longer does.** A commit that performs a sweep,
migration, retirement, or relocation states in its body what moved, how many,
and what was kept, cut, or deferred. This is the counterpart of ADR 074's ADR
trimming: the narrative has one home, and a bare-subject sweep commit loses it.

**Trailers, each conditional.** Written in the standard trailer block so
`git interpret-trailers` and `--grep` read them:

- `Decision: ADR 0NN` — only when the commit implements, amends, or revises
  that ADR. Most commits do not qualify and carry no `Decision:` line.
- `Workshop: kb/work/<name>` — when the commit advances a workshop.
- `Model: <model id>` — when an agent made the commit.

`Claude-Session:` continues as the harness supplies it. The fixed `ADR 0NN`
form makes both `git log --grep='ADR 0NN'` and the exact
`--grep='^Decision: ADR 0NN'` reliable going forward; older loose forms are not
rewritten.

**Relocation commits are pure.** A `commonplace-relocate-*` result is committed
alone — the move and the link rewrites it performs, no content edits — so
`git log --follow` keeps tracking the artifact across the rename.

This revises ADR 074's deferral of trailers: the drift it waited for was
observed in the session that declared the read path.

## Considered alternatives

**Conventional Commits prefixes (`feat:`, `fix:`, `chore:`).** Rejected. The
subjects are already sentences, the categories describe software releases
rather than KB operations, and no read path here filters by them.

**An `Operation:` trailer keyed on the change-operations catalogue.** The
natural next structured field, since the catalogue names the operations
ADR 074 routes on. Rejected for now: the catalogue is a first-pass working list
that admits entries by observation and claims no completeness, and a trailer
keyed on it would present it as settled vocabulary. Revisit if the catalogue
promotes.

**Mandatory trailers on every commit.** Rejected. Only a fraction of commits
implement a decision or advance a workshop; requiring the lines would produce
empty or invented values, which defeats the grep.

**A committed `.gitmessage` template.** Would prompt for the fields on each
commit. Deferred: agents compose messages from `AGENTS.md`, and the template
adds a second surface to keep in sync for a convention of four lines.

**Separate code commits from KB-content commits.** Would aid bisecting
package behavior. Rejected: mixed work is committed together here by standing
preference, and none of the named read paths needs the split.

## Consequences

Operativity path: `AGENTS.md` `## Git`, loaded by every agent in this checkout;
the ADR type spec's revision read path already greps for `ADR 0NN`. Force is an
authoring convention; nothing validates a commit message. A commit-msg hook
could check trailer shape if drift recurs.

`git log --grep='^Decision: ADR 0NN'` becomes an exact query for commits
implementing a decision, and `git log --grep='^Workshop: kb/work/<name>'`
recovers a workshop's commits without reconstructing them from paths.

Bodies get longer on migration commits and stay short elsewhere. The narrative
that ADRs used to carry is now findable only through git, which the ADR 074
boundary already limits to source-checkout operators.

Older commits keep their loose forms; queries over pre-2026-08-25 history
still need the loose `ADR 0NN` grep and manual filtering.
