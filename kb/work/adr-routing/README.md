# How does a change run find the decisions that bind it?

## Governing question

Commonplace holds 72 ADRs and nothing routes a self-improvement run into them.
Before designing a mechanism: **when is consultation actually needed, when has
it proved useful, and when should it have happened and did not?**

This is deliberately an observation workshop first. The set is not yet large —
511 KB, and its description layer is only 17 KB — so the pressure that would
justify building something may not have arrived. Past sessions appear to have
consulted ADRs exhaustively; if that is still workable, the missing piece is an
instruction, not a routing surface. Build nothing until observation says what
is failing.

Reasoning so far: [trigger analysis](./trigger-analysis.md).

## The gap, as measured 2026-08-23

- `kb/reference/adr/` has **no index** — no README, no INDEX.
- **No instruction routes to them.** The two instruction files matching `adr/`
  cite specific ADRs as sources for a claim; neither tells anyone to consult
  the ADR set before changing something.
- **The change loop is the only loop without an instruction.** Write, review,
  revise, critique, ingest, connect, validate, migrate, retire, publish, fix,
  and triage all have one. Changing the system has none.
- `AGENTS.md` names the directory as a navigation entry point, which is
  discovery by listing.

So ADRs are pointed *at* by artifacts and never routed *to* from a task. They
are consulted by luck: full maintenance cost, unreliable consumption.

## Why this is the right frame

An ADR is data, not a system-definition artifact. It asserts what was decided
and why; it binds nothing by itself. Getting a constraint out of one requires
defeasible reasoning, and an agent may legitimately conclude the ADR should be
superseded. The binding force would live in whatever instruction consults them
— and that instruction does not exist.

That makes this a routing problem, not a volume problem. Reduction would not
help: the constraint is that 71 ADRs cannot fit in a bounded context beside
the code and the task.

## Constraints a solution must respect

**A partial index is worse than none.** [Stale indexes reduce discovery when
they suppress fallback search](../../notes/indexes-lower-recall-when-they-suppress-retrieval-that-would-find-more.md):
an agent that finds three relevant ADRs stops looking for the fourth. Any
index either carries a completeness guarantee it can keep, or must not read as
complete.

**Enforce or omit.** If a routing surface caches anything recomputable from the
ADR set, [it must be machine-checked or absent](../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md).
The `complete`/`covered_by` marks on tag-READMEs are the shipped precedent for
how that can work.

**Retention is cheap; standing search surface is not.** `proposals/README.md`
already applies this — archived proposals are named in prose rather than
linked, so they stay retrievable without diluting what a reader sweeps. The
same reasoning applies to superseded ADRs and has not been applied to them.

## What a later session should not assume

Do not start by building. The first tasks are observational: partition the
ADRs by whether their decision already has an enforcement trace elsewhere, and
test whether the existing `description` layer is discriminating enough to route
on. Both are cheaper than any mechanism and either could dissolve the problem.

The shape, if a mechanism is eventually warranted, is open. An ADR index, a change-loop instruction, subsystem-keyed
routing, frontmatter that lets a routing query be computed, per-ADR scope
declarations, or something else entirely. Two or three of these may compose;
the measured gap does not select among them.

Nor should it assume the ADR set partitions cleanly by subsystem. Whether a
change-target-keyed head is even well-formed is an open question — the ADRs
may smear across targets, which would rule out the most obvious design.

## Downstream consumer

[The seven-case documentation disposition
evidence](../../notes/evidence/seven-documentation-cases-left-routing-and-synthesis.md)
retained curated routing where live lookup requires a name, but did not measure
consultation frequency. If a change-target-keyed mapping lands here, future
reference audits can use it to test whether descriptions are actually served
instead of inferring their value from plausible use.

## What closes this workshop

Observed evidence exists about when consultation helped, when it was skipped
and should not have been, and what the actual failure rate looks like — enough
that a decision to build or not to build rests on something.

If a mechanism is warranted, a change run can reliably reach the decisions that
constrain it, with completeness properties stated and, where claimed, enforced.
Concluding that none is warranted closes the workshop equally well, provided
the reason and the evidence are written down. Whatever is decided is recorded
as an ADR; reasoning that generalizes is promoted.
