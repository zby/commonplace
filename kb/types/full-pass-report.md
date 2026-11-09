---
type: types/type-spec.md
name: full-pass-report
description: Packet of one full improvement pass over a note, holding its disposition, closing status and the resolution of a pending hand-back
schema: ./full-pass-report.schema.yaml
---

# Full-pass report

## Authoring Instructions

The `commonplace-review run full-pass` workflow writes this packet; nobody
authors one by hand. It keeps one current packet per note at
`kb/reports/state/review/packets/<note-path>` and a copy in the run's
`artifact/packet.md`. A later pass over the same note replaces the current
packet; the run directory keeps the earlier one.

Code writes the frontmatter. `note` is the repository path the pass ran on.
`start-sha256` hashes the note's text when the pass started, and
`final-sha256` the text the pass left: the accepted edit after `ready`, the
start text otherwise. `run` names the run directory. `disposition`,
`update` and `merge-target` are the packet worker's decision;
`merge-target-sha256` hashes the merge target's text when the packet was
written. `closing-status` is `ready`, `hand-back` (the start text was
restored) or null when the pass stopped at the packet. `repaired` records
whether the one bounded repair was spent. Hashes are SHA-256 of the UTF-8
text, as review result files use.

`resolution` starts `not-required` for an accepted `keep` and `pending`
otherwise. Only the resolution fields change after the run, under
[resolve a full-pass disposition](../instructions/resolve-full-pass-disposition.md):
`accepted`, `rejected` or `alternative-applied` with `user` authority, or
`superseded` with `version-guard` authority when `commonplace-review packet`
finds a changed input. Quote `resolved-at` so YAML keeps it a string.

The body is the packet worker's text under an H1 naming the note, then one
`## Closing cycle: <cycle>` section per closing decision. It names files as
repository paths in code spans, because relative links would resolve from
the packet's directory, not the note's.

## Template

```markdown
---
description: Packet of a full improvement pass over kb/theory/example.md, with its disposition and resolution
type: types/full-pass-report.md
note: kb/theory/example.md
start-sha256: <lowercase SHA-256>
final-sha256: <lowercase SHA-256>
run: kb/reports/state/review/runs/<stamp>
disposition: keep
update: determined
merge-target: null
merge-target-sha256: null
closing-status: ready
repaired: false
resolution: not-required
resolved-at: null
resolution-authority: null
resolution-summary: null
resolution-rationale: null
resulting-paths: []
---

# Full Improvement Pass: <note title>

## Warranted contribution
...

## Closing cycle: closing
...
```
