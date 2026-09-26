---
description: "A tag head carries one mark, complete, meaning every member is linked from the head or carries a tag whose head is linked from it; covered_by and its typed child list are retired"
type: reference/types/adr.md
tags: []
status: accepted
---

# 090-One completeness mark reaches members in one hop

**Status:** accepted
**Date:** 2026-09-26
**Amends:** [ADR 026](./026-tag-readme-type-with-completeness-and-coverage-marks.md) (retires `covered_by`, redefines `complete`) and [ADR 089](./089-tags-are-one-namespace-per-kb-with-heads-in-kb-tags.md) (point 6, which kept both marks)

## Context

ADR 026 gave a tag head two validator-enforced marks. `complete: true` claimed the head links every member. `covered_by: [children]` claimed every member carries at least one listed child tag, and made that list the only typed tag-to-tag relation. Both answer one reader question, whether the head is a place to stop looking, at two granularities: the member, or the child head one hop away.

Practice did not fit either alone. The one head that declared `covered_by` dropped it twice because a few members fit no child and forcing a weak child tag was refused; the same head lists those members by hand, which under the two-mark contract earns no mark at all. Four heads carry `complete`; none carries `covered_by`. A survey of about 6,800 agent sessions found no use of the child list as a typed relation. Both marks are enforced or omitted, so an honest head with children and a few direct picks, the common shape, was left unmarked and its readers sent to a search the head had already made unnecessary.

## Decision

1. **One mark.** A tag head may declare `complete: true`. It means: every artifact carrying the tag is linked from this head, or carries a tag whose head is linked from this head. The head reaches every member in at most one hop.

2. **Children are the heads the body links.** No frontmatter list names them. Which linked heads are children and which are neighbours is what each link's context phrase says, as it already did for "Related Tags".

3. **The validator checks the hop.** It resolves the head's links, takes those that are heads, unions their memberships with the directly linked members, and fails the mark for any member outside that set, naming it. The fan-out warning on the child list is retired; the weight gate bounds what a head can link.

4. **Everything else in ADR 026 stands.** Marks are validated caches of membership, recomputable and never load-bearing, enforced or omitted. A mark that cannot be made true without a weak child tag or a tag created to hold a few notes is dropped and the members are listed by hand, which now also satisfies the mark.

## Considered alternatives

**Keep both marks and add a third for the mixed case.** Three marks for one question. Rejected: the mixed case is the general case, and the other two are its special cases.

**Keep `covered_by` as the child list and let `complete` count its children.** Keeps the typed relation at the cost of two places that must agree, the list and the links. Rejected: nothing consumes the relation, and a list that duplicates the body's links is the drift the marks exist to prevent.

**A new mark name.** `exhaustive` or `closed` for the one-hop meaning, retiring `complete`. Rejected: the four existing marks stay true under the new meaning, so renaming would churn heads for no reader gain.

**Recursive closure.** Count a member as reached when any chain of linked heads leads to it. Rejected: a reader follows one hop from a head and then searches or reads; a multi-hop promise is not one they can check or use, and it lets a large tag hide members behind a chain.

**Left open.** Whether a complete head should warn when it links more heads than a reader can hold at once; the retired fan-out limit was a guess and nothing has shown the need.

## Consequences

**Operativity path.** The tag-readme type rule in the validator consumes the mark and fails a false one; that is the force. The type spec and `kb/tags/COLLECTION.md` state the meaning for authors. Doctrine and navigation state the reader rule: a complete head reaches every member in one hop, so skip the by-tag search. The schema rejects `covered_by` so a stale copy cannot claim the old relation. `cp-skill-connect` keeps its skip rule unchanged.

**Easier.** A head with children and direct picks can be marked. Learning-theory carries the mark again in the implementing change. Authors maintain links, not a list beside them. The reader rule is one sentence.

**Harder or riskier.** The check reads the body's links, so a link to a head that is a neighbour rather than a child counts as covering: a member reachable only through a neighbour is still reachable, but the head's structure is less explicit than a list made it. A member added to a child tag silently stays covered; a member added with only the parent tag fails the parent's mark, as before.

**No longer possible.** A typed child list. A coverage claim without the links that carry it.

**Limits.** Tested on this checkout's heads, all under the weight gate, with at most seven linked child heads. Not tested with heads that link many neighbours, or in a host project.
