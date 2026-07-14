---
description: "Where a self-representation is retained artifacts, retrieval is the wire it acts along — a search that misses a represented constraint breaks the causal connection, not just convenience"
type: kb/types/note.md
traits: [title-as-claim]
tags: [foundations, computational-model, self-improving-systems]
---

# Retrieval failure is reflection failure

A [reflective system](./definitions/reflective-system.md)'s causal connection need not be an interpreter or a compiler. Where the self-representation is a body of retained artifacts, the connection runs through **discovery**: a process searches the artifacts, finds the ones bearing on the change it is making, and derives its behavior from what it found. Editing an artifact then reaches later behavior without anyone deciding to re-derive — provided the retrieval procedure surfaces it.

That proviso is load-bearing, and it puts retrieval *inside* the reflective architecture rather than alongside it. The search recipes, the frontmatter fields that make an artifact findable, and the indexes that shortcut the search are the wire along which the self-representation acts. A represented constraint that no process can find is inert: it is written, it is true, and it changes nothing. So a retrieval miss is not a missed convenience — it is a broken causal connection, the analogue of a compiler silently dropping a declaration.

## The failure is worst where the wire is trusted

The sharpest case is a membership claim that is asserted rather than enforced, [since stale indexes are worse than no indexes](./stale-indexes-are-worse-than-no-indexes.md). A head that says *this lists every note with the tag* tells an exhaustive consumer to stop looking. If members are missing, the claim cuts the wire precisely where a process was relying on it — and the process cannot tell, because the whole point of trusting the claim was to skip the check that would have caught it.

This is why Commonplace's `complete` and `covered_by` marks are validator-enforced or absent, never written as prose. The unenforced prose version of a completeness claim is not a weaker version of the same thing; it is the trap the enforced version exists to prevent.

## Best-effort, not by construction

Retrieval-mediated connection is weaker than procedural reflection in one specific way: it is best-effort. A compiler consumes a *declared* input set, and over that set it is exhaustive — every change to an input it was told about reaches the output. A search has no declared input set. It consumes what its query happens to surface, and relevance is a guess. The contrast is not perfection against fallibility — a compiler can also miss, if the input set is declared wrong — but enumeration against discovery, and only one of the two can be made exhaustive by construction.

A system can strengthen the wire — enforcing a membership claim rather than asserting it, adding a field that makes an artifact findable, correcting a search recipe observed to miss a member. It cannot assume the wire holds by construction, and the difference shows up as a class of silent failure that procedural reflection does not have.

Commonplace has run the strengthening loop at least once and can show the seam. Adopting `covered_by` on the `learning-theory` head, the new symbolic check caught a member the documented `rg` recipe had missed — a note using block-style YAML tags, invisible to the prose pattern. The recipe in `kb/reference/navigation.md` was then corrected. The wire had been broken for exactly as long as the blind spot existed, and nothing but a stronger check revealed it.

## Scope

- The claim concerns systems whose causal connection is retrieval-mediated. Where a self-representation is consumed by an interpreter or compiler that reads all of it, retrieval is not the wire and this failure mode does not arise.
- It says retrieval failure *is* reflection failure, not that retrieval is the only way reflection fails. A found artifact can still be misread, ignored, or overridden — [behavioral authority](./definitions/behavioral-authority.md) names the consumer, channel, and force that have to hold downstream of discovery.

---

Relevant Notes:

- [Reflective system](./definitions/reflective-system.md) — grounds: supplies the causal-connection criterion this note shows retrieval realizing, and failing
- [Stale indexes are worse than no indexes](./stale-indexes-are-worse-than-no-indexes.md) — mechanism: why a trusted-but-incomplete membership claim is the sharpest form of the failure
- [Behavioral authority](./definitions/behavioral-authority.md) — extends: the consumer, channel, and force that must hold after an artifact is found
- [Commonplace as a reflective system](../reference/commonplace-as-a-reflective-system.md) — evidence: the observed trace where a symbolic check corrected the prose search recipe that had been missing a member
