# Analysis: deriving the routing table

Draft, 2026-08-25. Sections 1–3 derive the criteria; section 4 is the table;
section 5 lists the changes the table implies; section 6 records what the
derivation does not settle.

## 1. What Naur's theory contains, and what the interpreter re-derives

Naur's theory is not about the program and not about the world; it is "a
theory of how certain affairs of the world will be handled by, or supported
by, a computer program" — the mapping. He names three capabilities a holder
has that documentation does not carry:

| Capability | Content | Why the artifact underdetermines it |
|---|---|---|
| **Map** — explain, for each part of the program, what aspect of the world it matches, and conversely | relevance decisions: which world affairs the system tracks and why | "the decision that a part of the world is relevant can only be made by someone who understands the whole world" — the artifact shows what was included, not why the boundary sits there |
| **Justify** — explain why each part is what it is | purposes (intents), forces, and the alternatives not taken | qualities such as simplicity "characterize the actual program text in relation to such program texts that might have been written" — the counterfactual design space leaves no trace in the chosen text |
| **Modify** — respond to a new demand by perceiving its similarity to what the design already handles | applicability conditions of the design; what counts as a natural extension versus a patch | "the kind of similarity that has to be perceived is one between aspects of the world" — it is judged against scope, not against code structure |

The KB's move ([theory-mediated self-improvement](../../notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md))
is to split the theory-holder into an interpreter and a retained text. Naur's
programmer regenerates most of the theory from the artifact plus their
knowledge of the world each time they read it. An LLM interpreter does the
same over the implementation, git history, and its own world knowledge. So
the retention question is not "what is the theory" but **which parts of the
theory the interpreter cannot regenerate at read time from what is already
there**. Retaining anything else is a cache, judged by the cache economics in
[opposed recompute factors](../../notes/opposed-recompute-factors-do-not-decide-documentation-segmentation.md),
not by whether it is true or useful.

Three sources are "already there" for a source-checkout operator:

- **the implementation** — code, contracts, validators, type specs, the
  artifacts themselves; the default read path for exact facts
  (`kb/reference/COLLECTION.md`);
- **git** — what changed, when, in what order, and the transition performed
  (ADR 074);
- **the world** — the interpreter's own knowledge, sufficient for ordinary
  similarity judgments but not for this project's particular relevance
  decisions.

What none of the three carries is the residue Naur identifies: relevance
decisions, intents, forces, rejected alternatives, and applicability scope.
That residue is what must be retained in tracked artifacts. It is also the
content the earlier documentation-disposition sweep found does not recover:
"no running system regenerates a decision, its rejected alternatives, or the
reason a boundary sits where it is."

## 2. Why intents are the high-leverage part

An intent — what the artifact is for, what ought to become true — sits at the
top of the justify capability. Given the intent and the implementation, an
interpreter can regenerate most per-part justifications ("this check exists
because the purpose requires X"), most relevance decisions ("that world
affair matters because the purpose needs it tracked"), and the similarity
judgment for a new demand ("does this serve the same purpose or a different
one?"). Without the intent, each of those must be retained separately or is
lost. The leverage is the ratio of justifications regenerable to tokens
retained, and for intents it is high because one sentence stands upstream of
many.

Three existing notes say this from different sides:

- [Fix what the executor can't determine](../../notes/fix-what-the-executor-cant-determine-not-what-it-will.md):
  goals, constraints, and done-conditions are the author-side residue that
  survives staleness; situational detail does not.
- [A goal-holding interpreter fails soft](../../notes/a-goal-holding-interpreter-fails-soft-workarounds-tax-a-bounded-budget.md):
  a procedure compiles its goal away, so a blocked step fails hard; an
  interpreter that holds the goal re-routes.
- The *Intention Is All You Need* ingest bounds the claim: intention
  "constrains the theory but is not itself the theory, a plan, or a
  sufficient control mechanism." An intent is an input to theory building, so
  retaining it does not retain the theory; it retains the part with the
  highest regeneration yield.

Two consequences for routing. First, an intent belongs *at* the artifact it
governs, not in a separate rationale store: it is read on every use, and
[memory-backed personalization](../../notes/memory-backed-personalization-can-look-like-model-improvement.md)
gives the record shape when the intent comes from a person — source,
subject, scope, status. Second, the instructions contract's rule to cut the
*why* of each step is compatible with retaining the *goal* of the procedure:
per-step rationale is regenerable from the goal plus the step; the goal is
not regenerable from the steps.

### The limit of intents

Leverage is a property of the intent–interpreter pair, not of intents alone.
The stronger the interpreter, the more of the theory it regenerates from
artifact plus intent, so the retained residue shrinks toward intents. The
current concentration on intentions is a bet on interpreter strength — the
bitter-lesson direction applied to documentation — and under that bet it is
the right thing to retain first.

Some of the residue is not regenerable at any interpreter strength, because it
is contingent fact rather than inference:

- **The actual choice and its rejected alternatives** (rows 4–5). Many designs
  serve one intent. Given intent and implementation, an interpreter can say
  why each part exists; it cannot say why *this* design rather than an
  equally intent-serving other. Naur's qualities are relative to "program
  texts that might have been written," and reversal by accident happens
  exactly here.
- **World-side forces particular to this project** (row 3). The intent "a
  simple credits-only billing system" does not contain "Indian cards cannot
  complete off-session top-ups"
  ([why LLMs can't make your code simpler](../../sources/why-llms-cant-make-your-code-simpler.ingest.md));
  that is a fact about the world that had to be learned and kept.
- **Applicability scope** (row 6). An intent says what ought to become true,
  not where the design stops working. Modification competence — is the new
  demand similar to what the design already handles? — is judged against
  limits, and an intent carries none.
- **Arbitrary conventions** (row 8). A choice made only because one had to be
  made is regenerable from nothing.

So the full picture is: intents are the highest-yield *inference seed*, and
the other kinds are *facts the seed cannot produce*. An intent-only retention
strategy fails where a change reverses a decision, meets an unrecorded world
constraint, or extends past an unrecorded limit — the failure modes Naur's two
cases describe.

## 3. Consumer and force decide the destination among retained kinds

Retention is necessary but not sufficient for a destination. ADR 074's
criterion — a passage earns its place by naming the operation that must read
it — and [operative change](../../notes/definitions/operative-change.md)
— an artifact without a consumer is stored, not operative — sort retained
content by who reads it and with what force:

| Force on the reader | Destination | Loaded when |
|---|---|---|
| binding: the reader executes it | `kb/instructions/`, `COLLECTION.md`, type specs, validators, code | on every matching operation |
| premise: the reader must know it before changing the system | `kb/reference/` | when performing a named change operation |
| decision: the reader must not silently reverse it | `kb/reference/adr/` | when revising or superseding a decision, and (gap) when a change touches what it binds |
| theory: the reader reasons with it | `kb/notes/` | on demand, via routing and links |
| audit: the reader reconstructs what happened | git | when an instruction declares the read path |
| observation: nobody consumes it yet | `kb/log.md` | on triage |
| in-flight: consumed by the work that produced it | `kb/work/` | during the workshop; deleted at close |

The [adr-routing](../adr-routing/README.md) finding that ADRs are "consulted
by luck" is a force gap, not a placement gap: the decision kind has the right
home and no declared consumer for most operations. The table below therefore
routes decision content to ADRs and lists the consumer gap as a change.

## 4. Draft routing table

Columns: the content kind; which Naur capability it belongs to (or *none* for
non-theory content); what already carries it, if anything; the operation
that consumes it; the destination; and the shape it takes there.

| # | Content kind | Capability | Regenerable from | Consumed by | Destination | Shape |
|---|---|---|---|---|---|---|
| 1 | **Purpose / intent** of an artifact, collection, procedure, or the KB | justify | nothing — implementation underdetermines it | every read and every change of the artifact; the interpreter's goal-holding | the artifact itself: `description` and first paragraph of a note or instruction; `## Purpose` of a `COLLECTION.md`; `## KB Goals` of `AGENTS.md`; an ADR's Decision when a decision sets it | one or two sentences at the top; for a person-supplied intent, the source/subject/scope/status record |
| 2 | **Relevance decision** — why this world affair is tracked and that one is out of scope | map | nothing | scope changes; ingest and connect operations | `COLLECTION.md` scope sections; `AGENTS.md` "In scope / Out of scope"; a note's scope section when the decision is about the theory's reach | explicit in/out lists, with the reason when it is not obvious from the purpose |
| 3 | **Force / constraint from the world** — why a boundary sits where it does, a non-obvious constraint, a rejected refactor | justify, map | nothing | revising the decision; changing the constrained site | if decision-level: ADR Context (forces that would recur if reverted); if code-level: the site it constrains — a test if enforceable, else a comment or docstring (`kb/reference/COLLECTION.md` site rule); if transferable: a note | decision-shaped ("because X, not Y"), captured when made ([capture at the decision surface](../../notes/structure-inference-needs-capture-at-the-decision-surface.md)) |
| 4 | **The decision itself** | justify | the implementation carries the choice; the ADR is its addressable handle | revise / supersede; any change touching what it binds | ADR Decision; the implementation is primary | the choice stated so it can be reversed on purpose, not by accident |
| 5 | **Rejected alternatives** and the forces that decided | justify | nothing — an unchosen branch leaves no trace | revise / supersede | ADR Considered alternatives; `kb/reference/proposals/` while undecided | a paragraph per option and why it lost; "none developed" is admissible |
| 6 | **Applicability conditions / scope** of a rule, decision, or theory | modify | nothing | rescoping after a failure; judging whether a new demand is similar | a separately addressable section of the artifact that holds the claim: a note's Caveats/Scope, an ADR's Consequences, an instruction's stated preconditions | separable from the claim so it can be narrowed without deleting the claim (retention condition 3) |
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
| 17 | **Self-directed theory** — a claim about the system's own operation ("this step surfaces the wrong artifact when …") | modify (applied to itself) | nothing | reflective improvement; the instruction it would change | `kb/notes/` with scope separable (row 6), plus the instruction or validator change it licenses, linked | claim, scope, and the change it produced, each addressable |

Reconciliation with the existing table in
`kb/reference/design-rationale-management.md` (`Rationale state → surface`):
that table is organized by lifecycle state of a rationale; this one by content
kind. They agree on every shared cell (exploration → work; undecided →
proposals; implemented → ADR; local contract → `COLLECTION.md`/type;
displaced → ADR consequences and git). This table adds the kinds that are not
rationale states: intents, scope, implementation facts, change narrative,
observations, sources.

## 5. Candidate changes the table implies

Each names the consumer and channel that would make it operative. None is
adopted here.

**C1. Instructions carry their goal.** Row 1 versus the instructions
contract's "cut the why". Proposal: the instruction type requires one
sentence of purpose ("This procedure exists so that …") at the top, distinct
from per-step rationale, which stays cut. Consumer: every agent executing the
instruction; the goal-holding interpreter argument says this is what lets a
blocked step re-route instead of failing hard. Channel: `kb/types/instruction.md`
and `kb/instructions/COLLECTION.md`; validator check optional. Cheap; the
`description` field already approximates it for skills.

**C2. Commit bodies state the intent of the change when the subject does not.**
Row 11. `AGENTS.md` `## Git` already asks for the narrative and the trailers;
add: the first body sentence states what the change is meant to make true
when the diff does not show it. Consumer: the next changer, via `git log` on
the site, and ADR revision via `git log --grep`. Channel: `AGENTS.md`;
unenforced, like the rest of the convention. The cost is one sentence at the
decision surface, where it is cheapest.

**C3. Scope is a separately addressable section.** Row 6. Check whether the
note and ADR type specs already make applicability conditions addressable
(notes: Caveats / Open Questions; ADRs: Consequences). If not, add a
lightweight expectation, not a required section: when a claim has known
limits, state them under their own heading so a rescoping edit can touch the
limit without the claim. Consumer: the revise operation and the
`semantic/*` gates that judge reach. Channel: `kb/notes/types/*.md`,
`kb/reference/types/adr.md`.

**C4. Decisions get a consumer.** Row 4's force gap, owned by
`kb/work/adr-routing/`. The change-operations catalogue is the natural
channel: each operation lists the ADRs that bind it, and the instruction for
that operation names them. Not designed here; the table only records that
without it, ADR content is retained but inert for most operations.

**C5. Retained-intent record for person-supplied intents.** Row 1's second
shape. Where an operator's intent enters the system (KB goals, a workshop's
question, a proposal's problem statement), the record should say who set it,
what it is about, what it covers, and whether it still applies. Check
whether `AGENTS.md` `## KB Goals` and `kb/work/COLLECTION.md` framing rules
already satisfy this; likely only partially (no status). Channel: those two
contracts.

**C6. Cut-test for reference passages gains a column.** Row 9. The economy
tests in `kb/reference/COLLECTION.md` already ask "premise or record?"; they
could name the regenerability source explicitly (implementation / git /
interpreter's world knowledge) so a writer can say which one makes the
passage redundant. Small wording change; channel: that contract.

**C7. Where the table lives.** The table itself is reference content by its
own criterion (a premise of every write operation). Candidate home:
`kb/reference/design-rationale-management.md`, merged with its lifecycle
table, or a new `kb/reference/content-routing.md` linked from `AGENTS.md`
Collection Routing. The theory in sections 1–2 is a note (row 7)
holding both halves: retain intents as the highest-yield inference seed, and
retain the facts the seed cannot regenerate — the choice among alternatives,
project-particular world forces, applicability limits, arbitrary conventions.

## 6. What this pass does not settle

- **Whether the intent-leverage claim holds empirically, and where it stops.**
  The prediction has two halves: an agent given an artifact plus its intent
  reconstructs per-part *justifications* better than one given the artifact
  plus the same tokens of per-part rationale; and it does *worse* at avoiding
  reversal of a recorded decision, recovering a world-side constraint, and
  respecting an unrecorded limit — the non-intent rows. Losing the second
  half is the evidence those rows need. The
  `explanatory-theories-deployment-time-learning` workshop's experimental
  frame fits; not run here.
- **Grain.** Rows 1 and 6 say "the artifact"; for a collection or the KB the
  intent lives one level up. The rule "at the smallest artifact whose purpose
  it is" is the intended reading and needs a worked case.
- **Human theory that is never externalized.** Naur's guided transfer has no
  row: the operator's unstated judgments are the part of the theory the KB
  does not hold. Row 5 (rejected alternatives) and row 11 (change intent) are
  where that judgment most often surfaces in writing; the table can only
  make the surface cheap, not make the transfer complete.
- **Installed projects.** The git rows assume a source-checkout operator with
  history. ADR 074's boundary rule applies: anything a reader install or
  shallow clone must know stays in tracked artifacts. The table does not
  re-derive that boundary.
