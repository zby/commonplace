# Workshop: Life-cycle Management

## Question

What life-cycle does a KB artifact travel — from workshop intake through promotion, maturation, and eventual retirement — and where do current conventions under-specify the transitions?

## Why this workshop exists

The KB has strong conventions for the two poles: workshops (temporal, value-consumed) and the library (durable, value-accumulated). The transitions between and within them are only sketched. [A functioning knowledge base needs a workshop layer, not just a library](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) names the bridges but leaves the mechanics open.

Concrete trigger: some workshops — `agent-memory-design` was the clearest case — feel like coherent wholes rather than a pile of extractable claims. The current closure protocol in [kb/work/COLLECTION.md](../COLLECTION.md) ("extract durable conclusions, delete the workshop") assumes atomization works. When a workshop reads as a monograph, atomization would destroy the structure that makes it useful. Where does such a workshop land?

**Resolution for `agent-memory-design` (2026-04-23):** promoted as a single `kb/notes/designing-agent-memory-systems.md` carrying the new `synthesis` trait. The trait waives `kb/notes/`'s default body-composability rule for the note (cite as unit; extract component claims into their own notes if they need to be cited as premises). The four `explore-*` workshop files were folded into an "Alternatives considered" section within the promoted note and then deleted. This exercises one closure pathway — whole-thing promotion via a trait — and leaves the broader map below still to complete.

We start from workshops because that is where we have the most active practice. The aim is a map of stages and transitions across the whole KB, not just workshop intake.

## Stages in scope

- **Intake** — workshop creation, framing, initial direction.
- **In-flight work** — mid-workshop evolution: split, merge, rename, partial extraction, retirement without closure.
- **Promotion** — workshop → library. Atomized extraction vs. whole-thing promotion.
- **Maturation** — seedling → current within the library. What earns the gate.
- **Decay / retirement** — staleness signals, revise vs. deprecate vs. delete.
- **Extraction bridges** — pulling durable claims out of a still-running workshop without closing it.

## What this workshop needs to resolve

1. **Closure pathways.** The current protocol is atomize-then-delete. What are the other legitimate end states? Candidates: abandoned, absorbed into an existing note, promoted whole, partially extracted with a residual that keeps running.

2. **Whole-thing promotion.** When a workshop is too coherent to atomize, where does it go? Options to evaluate:
   - `kb/notes/<workshop-name>/` as a sub-directory (precedent: `notes/definitions/`, `notes/research/`). Theoretical register applies; atomic parts still expected to be note-shaped.
   - A new sibling collection (precedent: `kb/agent-memory-systems/` — but that is a descriptive register for external systems; promoted workshops are typically theoretical, so the precedent fits only partly).
   - A new collection type for extended theoretical artifacts — "monographs," "design studies," "theory bundles." Would need its own `COLLECTION.md`, register, and linking rules.
   - Something else.

   `agent-memory-design` was the concrete test case. It landed as option (d): **single-file promotion with a `synthesis` trait** — neither a sub-directory nor a new collection, because the workshop reduced to one durable artifact once the explore-* files were folded into an "Alternatives considered" section.

   That resolution is n=1. Whether the pattern generalizes depends on the shape of the next monograph-style workshop. If a future case has multiple durable artifacts that must stay together, the sub-directory option or a monograph collection returns to the table.

   **Sketch of how a monograph collection would work, kept for reference:**
   - *Location.* `kb/monographs/<name>/` — one collection, many monographs as subdirectories; one `COLLECTION.md` governs all.
   - *Register.* Not a new register. Theoretical, same quality bar as `kb/notes/`. The monograph is a **container**, not a new content mode.
   - *Contents.* Normal typed files inside — `note`, `structured-claim`, `definition`, `index` — plus a required landing `README.md` that reads as the entry point and narrates the argument.
   - *Promotion from workshop.* `kb/work/<name>/` → `kb/monographs/<name>/`. Rename the directory, fix frontmatter on files that lack it, validate links. Internal structure preserved.
   - *Linking in.* Landing page always a valid citation target. Individual files also citable under their normal type rules. Outbound-link guidance in other `COLLECTION.md` files would prefer the landing page when the cite is about the whole argument.
   - *Linking out.* Files follow their type's normal rules. Landing page has README/index conventions.
   - *Extraction.* A claim inside a monograph that turns out to have independent reach can be lifted to `kb/notes/`, with the monograph file becoming a stub that links out.
   - *Key unresolved design choice.* Do individual monograph files count as first-class library citations, or do we only cite the landing page? First-class keeps the theoretical register consistent but allows duplication across granularities. Landing-page-only preserves the monograph as a unit but weakens discoverability.
   - *Why a real collection, not a `kb/notes/<name>/` sub-dir.* A collection gets a `COLLECTION.md` and validation rules that enforce structure (landing page required, directory coherent); a sub-dir under notes has no such handle and will drift. This is the main argument the sub-dir experiment has to survive.

3. **Seedling maturation.** When does a seedling become current? Today this is intuitive. Is there an operable gate — number of inbound links, citation by a structured-claim, review pass, something else?

   **Overtaken by [ADR 044](../../reference/adr/044-user-verification-replaces-global-note-status.md):** the global `status` enum — and with it seedling/current — was removed; optional committed user verification replaced it. The maturation question this workshop posed no longer has a field to answer for; what remains of it is owned by the verification and review-freshness contracts, not here.

4. **Retirement protocol.** What signals a note is stale? What is the action — revise in place, mark deprecated, delete? How do inbound links get handled?

   **Answered for proposals, shipped 2026-07-25** — [ADR 056](../../reference/adr/056-adopted-and-retired-proposals-archive-out-of-the-frontier.md). A decided proposal is extracted, then moved to [`kb/reference/proposals/archive/`](../../reference/proposals/archive/README.md), which is a link sink: nothing outside it links in (exceptions: its own README and `kb/work/`), incomplete extraction is repaired by re-extraction rather than by a live link, and an ADR names its proposal by title rather than by path. Because that demotes the pointer, ADRs dated 2026-07-25 or later must carry `## Considered alternatives`. The operating rules live in [proposals/README.md](../../reference/proposals/README.md), [archive/README.md](../../reference/proposals/archive/README.md), and [types/adr.md](../../reference/types/adr.md); [lifecycle-model.md](./lifecycle-model.md) keeps the reasoning that produced them.

   **Generalized to a polymorphic operation, 2026-07-27.** [retire-artifact.md](../../instructions/retire-artifact.md) is now the single procedure for every kind, branching on a destination each type spec declares: `design-proposal` archives, everything else deletes. The two branches differ in only two respects — inbound links retarget under delete and must *not* under archive, and the disposal command differs — so the polymorphic surface is one line in one type spec. The archive-versus-delete test is "what survives a complete extraction": irreproducible observation archives, claims delete. Deriving that test also exposed a false premise carried twice in ADR 056's own body, since amended; see [the disposal survey](./disposal-and-retirement-survey.md#the-archive-versus-delete-test-2026-07-27) and the follow-up section of [lifecycle-model.md](./lifecycle-model.md).

   **Still open: the trigger, not the operation.** Notes now have a disposal procedure but no eligibility rule — nothing routes a staleness signal to it, where proposals have a crisp "adopted or retired." That is the last piece of question 4. Source snapshots came off the list on 2026-07-27: they are standing inputs to a fail-severity quote check, so retention is load-bearing rather than residual. The framing the proposals case established carries forward: the operative retention cost is the search surface, not storage, so the axis is "in the frontier vs. out of it, and still citable vs. not."

5. **Extraction during a workshop.** Can durable claims be promoted mid-workshop without closing it? What convention keeps the workshop useful after partial extraction, and what stops it from becoming a permanent shadow library?

## Current grounding

- [A functioning knowledge base needs a workshop layer, not just a library](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — library/workshop distinction, extraction and composition bridges, open questions this workshop inherits.
- [Workshop COLLECTION.md](../COLLECTION.md) — current closure protocol (extract-and-delete), and the sinks-not-sources rule ADR 056 extended to a second, retained sink layer.
- [ADR 056](../../reference/adr/056-adopted-and-retired-proposals-archive-out-of-the-frontier.md) with [proposals/README.md](../../reference/proposals/README.md) and [archive/README.md](../../reference/proposals/archive/README.md) — the one disposal operation this workshop has shipped, and the model the remaining kinds are decided against.
- [kb/reference/types/adr.md](../../reference/types/adr.md) — the `## Considered alternatives` requirement that pays for tag-not-pointer provenance.
- [kb/reference/types/design-proposal.md](../../reference/types/design-proposal.md) — the collection-local type that replaced the `design-proposal` trait; carries the archived-proposal description form.
- [designing-agent-memory-systems](../../notes/designing-agent-memory-systems.md) — the promoted artifact from the `agent-memory-design` workshop; first instance of the `synthesis` trait.
- [kb/agent-memory-systems/COLLECTION.md](../../agent-memory-systems/COLLECTION.md) — one precedent for a sibling collection with its own register.
- [kb/notes/COLLECTION.md](../../notes/COLLECTION.md) — theoretical-register conventions a promoted workshop would have to satisfy.

## Working hypotheses

- Closure is not a single protocol. There are several legitimate end states; the current conventions only describe one.
- Some workshops are monographs, not piles of claims. Preserving their internal structure is part of the value.
- Maturation and retirement need lighter machinery than intake — less workflow, more signals.

## What would close this workshop

An updated life-cycle map (probably a note) naming each stage, its valid transitions, and its conventions, and an updated `kb/work/COLLECTION.md` closure section that reflects the richer set of pathways. The `agent-memory-design` landing is resolved (single-file promotion with `synthesis` trait) and can serve as one worked example in the map.

**Done (2026-07-25):** the disposal clause for `kb/reference/proposals/`, shipped as ADR 056 together with the ADR type contract's `## Considered alternatives` requirement — dated prose rather than the intended schema check, because 4 of 56 existing ADRs carry alternatives prose and none as a heading. Two proposals migrated as worked cases (ADR 044's and ADR 045's), with their inbound frontier links re-extracted or demoted to title mentions.

**Done (2026-07-27):** retirement became one polymorphic procedure with a type-declared destination, and the retirement instructions were consolidated under a contract/procedure split — one archiving rule that had been stated in four places now sits in one contract site, one procedure, and one type-spec declaration.

**Blocking the map now:** one thing — an eligibility rule for note retirement. The operation exists, so the map can describe the transition; what it cannot yet say is what triggers it. Beyond that, the claims worth promoting to `kb/notes/` still want a second worked case: the archive-versus-delete test (strongest, but no second candidate kind currently exists, so it waits for a real one rather than a manufactured one) and tiers-as-coordinates. The workshop deletion bet is no longer a separate candidate — it falls out of the archive-versus-delete test (see "Still open" in [lifecycle-model.md](./lifecycle-model.md)).
