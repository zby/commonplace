---
description: "Routing table from content kind to destination — instructions and contracts, reference, ADRs, notes, commit messages, log, workshop — with the regeneration source and consuming operation that justify each row"
type: kb/types/note.md
---

# Content routing

Where a piece of content goes once it is worth keeping. A row is justified by
two facts: what already carries the content (the implementation, git, or the
reader's own general knowledge), and which operation consumes it and with what
force. Content those sources do not carry must be retained. Content they do
carry is a cache question, unless the passage also has an independent
authority, cross-check, provenance, activation, or exact-record role. The
derivation is in
[design rationale must preserve decision premises its interpreter cannot regenerate](../notes/design-rationale-must-preserve-unregenerable-decision-premises.md)
and [a specific intent may out-yield local rationales, but contingent facts stay separate](../notes/specific-intent-may-out-yield-local-rationales-facts-stay-separate.md);
this page is the premise a write operation reads.

Force decides the destination among retained kinds:

| Force on the reader | Destination | Loaded when |
|---|---|---|
| binding: the reader executes it | `kb/instructions/`, `COLLECTION.md`, type specs, validators, code | on every matching operation |
| premise: the reader must know it before changing the system | `kb/reference/` | when performing a named change operation |
| decision: the reader must not silently reverse it | `kb/reference/adr/` | when revising or superseding a decision |
| theory: the reader reasons with it | `kb/notes/` | on demand, via routing and links |
| audit: the reader reconstructs what happened | git | through an instruction that declares the read path |
| observation: nobody consumes it yet | `kb/log.md` | on triage |
| in-flight: consumed by the work that produced it | `kb/work/` | during the workshop; deleted at close |

## Routing table

| # | Content kind | Capability | Regenerable from | Consumed by | Destination | Shape |
|---|---|---|---|---|---|---|
| 1 | **Purpose / intent** of an artifact, collection, procedure, or the KB | justify | nothing, unless a contract or commit already states it; implementation alone underdetermines it | every read and every change of the artifact; the interpreter's goal-holding | the artifact itself: `description` and first paragraph of a note or instruction; `## Purpose` of a `COLLECTION.md`; `## KB Goals` of `AGENTS.md`; an ADR's Decision when a decision sets it | one or two sentences at the top; for a person-supplied intent, who posed it and in what role — its currency is read from the container's lifecycle position (workshop open or deleted, proposal in the frontier or archived, `AGENTS.md` current), not from a status field |
| 2 | **Relevance decision** — why this world affair is tracked and that one is out of scope | map | nothing | scope changes; ingest and connect operations | `COLLECTION.md` scope sections; `AGENTS.md` "In scope / Out of scope"; a note's scope section when the decision is about the theory's reach | explicit in/out lists, with the reason when it is not obvious from the purpose |
| 3 | **Force / constraint from the world** — why a boundary sits where it does, a non-obvious constraint, a rejected refactor | justify, map | nothing, unless a contract, test, or commit already records the force | revising the decision; changing the constrained site | if decision-level: ADR Context (forces that would recur if reverted); if code-level: the site it constrains — a test if enforceable, else a comment or docstring (`kb/reference/COLLECTION.md` site rule); if transferable: a note | decision-shaped ("because X, not Y"), captured when made ([capture at the decision surface](../notes/structure-inference-needs-capture-at-the-decision-surface.md)) |
| 4 | **The decision itself** | justify | the implementation carries the choice; the ADR is retained as its exact record and addressable handle | revise / supersede; any change touching what it binds | ADR Decision; the implementation is primary | the choice stated so it can be reversed on purpose, not by accident |
| 5 | **Rejected alternatives** and the forces that decided | justify | nothing, unless a commit or proposal recorded it; an unchosen branch otherwise leaves no trace | revise / supersede | ADR Considered alternatives; `kb/reference/proposals/` while undecided | a paragraph per option and why it lost; "none developed" is admissible |
| 6 | **Applicability conditions / scope** of a rule, decision, or theory | modify | nothing, unless a contract already states the limit | rescoping after a failure; judging whether a new demand is similar | a separately addressable section of the artifact that holds the claim: a note's Caveats/Scope, an ADR's Consequences, an instruction's stated preconditions | separable from the claim so it can be narrowed without deleting the claim (retention condition 3) |
| 7 | **Transferable mechanism** — why something works beyond the case that produced it | justify (general) | nothing | reasoning about any similar design | `kb/notes/` | explanatory-reach claim; the notes placement test: after every system choice is scoped, does a design-space claim remain? |
| 8 | **Procedure steps, conventions, arbitrary choices** the executor cannot determine | none (system definition) | nothing for the arbitrary part; the goal regenerates the rest | executing the operation | `kb/instructions/`, `COLLECTION.md`, type specs, validators | imperative, first-read executable; per-step *why* cut and linked `rests-on` to a note; the procedure's goal kept (row 1) |
| 9 | **Exact implementation facts** — structure, parameters, current values, module ownership | none | the implementation | any | not retained; live implementation is the read path; `kb/reference/` keeps only the orientation premises a change operation needs and cannot cheaply recover | a symbol or path as a search key, never a restated body |
| 10 | **Change narrative** — what moved, when, in what order, migration steps, files touched, counts kept/cut/deferred | none | git | audit; ADR revision via `git log --grep` | commit message body, with `Decision:` / `Workshop:` trailers naming what it implements | subject: imperative summary; body: the narrative |
| 11 | **Intent of a specific change** — what this commit is meant to make true, when the diff does not show it | modify (the similarity judgment at change grain) | nothing; the diff shows what, not what for | the next changer of the same site; ADR revision | commit message body, first sentence; promoted to ADR Context when it is a recurring force | one sentence; the commit is the decision surface for change-grain intent |
| 12 | **Observation** — something worked or failed, first occurrence, mechanism not yet understood | none yet | nothing | triage | `kb/log.md`; a note once the mechanism is understood | dated entry; no explanation demanded |
| 13 | **Measurement / evidence** behind a decision | justify | the implementing commits hold the full data | decision audit; any durable artifact that cites it | compressed warrant in the ADR (the numbers as reasons); full data in git; `kb/notes/evidence/` when a durable artifact cites it | numbers with the reason they mattered |
| 14 | **Identified gap not being done now** | justify (deferred) | nothing | the adoption decision | `kb/reference/proposals/` (system gap) or `kb/notes/` (insight) — the YAGNI rule | problem, option space, forces, free choices; no implementation detail |
| 15 | **In-flight reasoning, drafts, traces** | any, unfinished | nothing, but consumed once | the work producing it | `kb/work/`; deleted at close after extraction | free form |
| 16 | **Source-side claim and its evidence** | map (external world) | the pinned snapshot | grounding gate; any note citing the source | ingest `## Quotes` via `cp-skill-ground`; snapshot when bounded quotes cannot carry it | verbatim extract plus locator |
| 17 | **Self-directed theory** — a claim about the system's own operation, such as a retrieval step surfacing the wrong artifact for one kind of query | modify (applied to itself) | nothing | reflective improvement; the instruction it would change | `kb/notes/` with scope separable (row 6), plus the instruction or validator change it licenses, linked | claim, scope, and the change it produced, each addressable |

## Relation to other placement rules

- `kb/reference/COLLECTION.md` — the economy tests decide whether a reference
  passage exists at all; row 9 restates their regeneration sources.
- `kb/notes/COLLECTION.md` — the placement test between notes and reference;
  row 7.
- `kb/instructions/COLLECTION.md` — the reasoning constraint; rows 1 and 8.
- [`types/adr.md`](./types/adr.md) — the ADR retention rule; rows 3–5, 13.
- `AGENTS.md` `## Git` — the commit-message convention; rows 10–11.
- [Design rationale management](./design-rationale-management.md) — the same
  surfaces organized by lifecycle state of a rationale rather than by content
  kind; the two tables agree on every shared cell.

Row 6 lands in a section the artifact's type names for it: `## Scope` (or
`## Caveats`) in a note, its own paragraph of `## Consequences` in an ADR,
stated preconditions in an instruction. Row 4 names a consumer the system
does not yet route reliably: most change operations do not consult the ADRs
that bind them (`kb/work/adr-routing/`). That is a recorded gap, not a
placement rule.
