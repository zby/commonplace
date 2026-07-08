# Workshop: epistack-framework-additions

Brainstorm of framework additions to Commonplace that would make **epistemic casework** — tasks like the FLF Epistemic Case Study Competition's lab-leak / black-hole / egg cases — easier, plus a recommended personal-epistemology stance for the person running such casework.

This is the *design-thinking* companion to [`epistack-competition`](../epistack-competition/README.md), which is only the framework-side pointer to the sibling `epistack-casebooks` repo and the `backlog-to-commonplace.md` protocol. This workshop holds the menu of candidate additions; the sibling repo is where any of them get built and proven.

## Framing

- **Goal.** Enumerate candidate Commonplace additions that lower the cost of building source-grounded, contestation-preserving casebooks, and pick a coherent epistemological stance for them to serve.
- **What closes it.** Each candidate has either (a) become a build-local-first experiment queued in `epistack-casebooks` and logged to its backlog, or (b) been rejected with a reason. Anything that survives a worked case gets promoted here as a proposal/type/note; then this workshop is deleted.
- **Boundary.** No framework code is written from this workshop. The discipline is **build-local-first in the casebook repo, upstream what survives** — application casework does not belong in this repo. This file is a design menu, not an implementation plan.
- **Source caveat.** The competition pages (`flf.org`, EA Forum, GreaterWrong, Oliver Sourbut's "A Full Epistemic Stack") were unfetchable from the authoring environment (403 via network policy). The competition framing below is assembled from search snippets plus the sibling-repo summary in `epistack-competition`; verify against the primary sources before relying on specifics.

## The core tension to design around

The competition wants AI workflows that produce **trustworthy knowledge bases grounded in real cases** — making the *provenance, structure, and assessment* of knowledge transparent and traversable, across cases like COVID lab-leak origins, LHC/black-hole safety, and the egg/cholesterol nutrition literature. The sibling repo's own goal statement: expose "what is known, what is contested, what depends on what, and where the gaps are — *without adjudicating truth*."

That last clause points opposite to Commonplace-as-built. Commonplace is optimized to distill **transferable, committed methodology** for agents: `title-as-claim`, "do I still believe this?", the whole Popperian maintenance loop assumes the KB *takes positions and defends them*. Casework instead needs a mode that **represents contestation faithfully and refuses to average it away**. [Mechanistic constraints make Popperian KB recommendations actionable](../../notes/mechanistic-constraints-make-popperian-kb-recommendations-actionable.md) warns why this matters: contradictions loaded into one context "aren't flagged; they're silently averaged." A casebook's value is keeping the disagreement structurally distinct instead of letting the model launder it into one confident answer.

So the highest-leverage additions are not gadgets but a **register and a type surface for stance-neutral evidence maps**, plus provenance strong enough to survive review. The menu below is organized by the competition's three layers.

## Ingestion / provenance layer

- **Source-span citations, not file-level links.** This is already the first queued experiment in `epistack-competition` ("does file-level linking suffice, or do claims need a source-span locator type?"). [ADR 023](../../reference/adr/023-quote-anchored-citations-for-code-grounded-reviews.md) already built *quote-anchored citations* for code-grounded reviews — the precedent to generalize into a `claim → source-span` locator, so a claim points at the exact passage it rests on and review can verify the quote still says what the claim says.
- **A richer `source` type.** `kb/sources/` exists, but casework needs capture metadata as first-class fields: retrieval date, author/institution, medium, an archived snapshot hash, and known credibility signals. Rationale: [history has one chance to become checkable](../../notes/history-has-one-chance-to-become-checkable.md) — production history is only convertible to checkable form at capture time.
- **Traversable provenance chains.** Derived claim → intermediate synthesis → source-span, walkable both ways, so "if this source is retracted, what claims fall?" is a graph query, not a manual audit.

## Structure layer

- **A `claim` type distinct from [`structured-claim`](../../notes/types/structured-claim.md).** `structured-claim` is *an argument for a position* (Evidence / Reasoning / Caveats). Casework needs a claim as a *node in a disagreement graph*: the proposition, who asserts it, its support, its rebuttals, and a status (`contested` / `settled` / `open`), with the proposition deliberately decoupled from any verdict.
- **A dialectical/evidential link vocabulary.** [ADR 009](../../reference/adr/009-link-relationship-semantics.md) and [ADR 019](../../reference/adr/019-collection-owned-link-vocabulary.md) give collection-owned link semantics; casework wants the argument-mapping set — `supports`, `rebuts`, `undercuts`, `is-evidence-for`, `depends-on` (Toulmin/IBIS-flavored). The LHC case is largely a *dependency chain* of safety arguments; "what does this claim rest on" needs to be a typed edge.
- **Party/position attribution.** A claim must carry "asserted by Rootclaim" vs "asserted by Miller" as structure, separate from truth. This is the field that lets the map stay neutral.
- **A first-class gap register.** The competition explicitly wants "where the gaps are." Make *what is not known* a typed artifact (an open question with its blockers), not an implicit absence — otherwise gaps are invisible to retrieval.

## Assessment layer

- **Confidence must be attributed, never a mark.** From the mark discipline in [`kb/types/tag-readme.md`](../../types/tag-readme.md) (ADR 026): a mark is a cache *recomputable from ground truth and validated by code*. A credence is not recomputable — a bare `confidence: 0.7` field would be exactly the "stale trusted cache is a trap" failure the mark rule forbids. Represent credences only as *attributed, sourced assessments* ("Rootclaim's aggregate: 96% zoonotic") — claims about who-believes-what, not KB-blessed truth.
- **Epistemic review gates, reusing existing machinery.** The review subsystem (note-gate pairs, freshness, acceptance state) supports new gates without new plumbing. Candidates: *every claim has a source-span*; *every `contested` claim shows at least one rebuttal edge*; *every gap is linked from the claim it blocks*. [Reasoning production is not reasoning evaluation](../../notes/reasoning-production-is-not-reasoning-evaluation.md) argues the rebuttal check needs a *decorrelated* reviewer — don't let the pass that wrote the support also grade it.
- **Adjudication as a separate, labeled, downstream layer.** If a verdict is wanted (Rootclaim-style Bayesian aggregation), it should be its own artifact that reads the neutral map as input and is never merged into it. The map is the durable, defensible object; the verdict is a replaceable opinion computed over it.

## The biggest single addition: a fourth register

Register is core to Commonplace, and the three today (theoretical / descriptive / prescriptive) are all **first-person-committed**: their quality bar is "is this claim true / accurate / correct?" Casework fits none. It needs a **dialectical/evidential [register](../../notes/definitions/register.md)** whose quality bar is *"does this faithfully represent the state of contestation, with every position sourced and attributed?"* Defining this register (its `COLLECTION.md` contract, its title conventions — likely *not* title-as-claim, since a casebook node shouldn't assert — and its link rules) is the piece most likely to "change how FLF thinks about the problem," because it is the methodological move, not a feature.

## Recommended personal-epistemology stance

A deliberately **two-layer stance**. The failure mode to avoid is a single monolithic epistemology that collapses *mapping the debate* into *winning the debate*.

1. **For the map: fallibilist + dialectical.** Be a neutral cartographer. Represent every position, attribute it, and *keep contradictions structurally separate* rather than resolving them — bounded-context theory says an agent will otherwise silently average them. Keep the Popperian backbone Commonplace already has (falsifier blocks, contradiction-first connection) but repoint it: each claim carries "what would defeat this," authored so criticism is externalized structure, not the model's vibe on re-read.
2. **For the verdict (only when one is wanted): explicitly Bayesian, and separable.** Rootclaim's probabilistic aggregation is a reasonable engine, but it belongs in a clearly-labeled downstream artifact whose priors and likelihoods each trace to sourced claims on the map. Never fuse it into the map.
3. **Convergence mechanism: adversarial / decorrelated review.** From [error correction works with above-chance oracles and decorrelated checks](../../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — a claim's rebuttal and its support should come from *different* passes/agents, because a model checking its own claim under the same prompt is a correlated, weak oracle. Steelman-then-attack, with the two roles held by different context.

One line: **be a fallibilist, argument-mapping steward of the debate; be a Bayesian only in a separate, sourced, clearly-labeled verdict layer; and make convergence come from adversarial decorrelated review, not from a single agent's confidence.**

## Suggested first experiments (for the sibling repo, not here)

- Prototype the **source-span locator** and the **dialectical/evidential register** first — everything else hangs off those two.
- Run them against one worked case (the black-hole/LHC case is the cleanest dependency chain) before generalizing.
- Log outcomes to `epistack-casebooks/backlog-to-commonplace.md`; promote to this repo only what survives.

## Candidates imported from a second opinion (ChatGPT)

A ChatGPT analysis of the same problem independently re-derived the core of this menu — thin layer over Commonplace, an atomic claim type distinct from `structured-claim`, source-span provenance, assessment as a separate downstream artifact, epistemic review gates, an argument-mapping link vocabulary, and update-propagation over provenance chains. That convergence corroborates the architecture above. Below are only the pieces it added that this menu lacked (kept, as candidates for the sibling repo) and the pieces that conflict with the two load-bearing design rules here (rejected, with reasons), per this workshop's closing contract.

### Kept as candidates (queue in the sibling repo)

- **Independence clustering of evidence.** Tag each evidence item with an `independence_cluster` and its shared dependencies (dataset, method, authorship, citation lineage), so reviews and dashboards can flag "12 items, 3 plausibly independent clusters." FLF explicitly calls out correlated evidence treated as independent; this menu was silent on it. It is the evidence-side analogue of the reviewer-side logic in [error correction works with above-chance oracles and decorrelated checks](../../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — probably the highest-value import. Its link-level expression is `correlated-with` / `independent-of` edges.
- **A `crux` type, distinct from the gap register.** A gap is *what is not known* (a neutral map-layer artifact); a crux is *what would move the bottom line* — necessarily verdict-relative, since `would_change_assessment_if` presumes an assessment. Under the two-layer stance both belong, in different layers: gaps on the neutral map, cruxes attached to assessment artifacts. This is a clean split of what could otherwise be conflated.
- **Semantic (judgment) review gates**, complementing the structural ones above. The three gates proposed earlier are deterministically checkable (has-a-span, contested-claim-has-a-rebuttal-edge, gap-linked-from-blocked-claim). ChatGPT's `scope-creep`, `rhetorical-overweighting`, `missing-countercase`, `settlement-illusion`, and `source-span-fidelity` are judgment calls that fit the *semantic* review system, not the validator. Keep them separate from the deterministic gates.
- **Model/calculation artifacts** with explicit variables, assumptions, and sensitivity analysis — directly useful for the LHC safety-case dependency chain. Prove on that case before generalizing.
- **Multi-method assessment comparison** (run 2+ assessment methodologies on the same subquestions, then a compare artifact naming where they agree, diverge, and which cruxes are method-sensitive). This tracks FLF's "stepping-stone entry" framing. Pure verdict-layer work, so it lives entirely in `epistack-casebooks`.
- **Derived per-inquiry dashboards** and a **`commonplace-source-impact <source>`** command — consistent with the compiled-index philosophy (derived, never source of truth) and the traversable-provenance idea above. Navigation surfaces, built once a case has enough claims to need them.
- **A "belief ledger" practice** for the verdict layer (previous confidence / current confidence / main update / evidence responsible / what would reverse this) — a concrete articulation the personal-epistemology stance above did not name.

### Rejected (with reasons)

- **An inquiry "control room" that carries the verdict.** ChatGPT's inquiry frontmatter holds `current_answer` and `confidence`, with body sections "Current Bottom Line" / "What Would Change My Mind." That fuses the verdict into the map — exactly what "Adjudication as a separate, labeled, downstream layer" forbids, for the mechanistic reason that contradictions loaded into one context get silently averaged. An inquiry/case-root artifact is fine, but it should hold the question, scope, hypotheses, and pointers to the map; the bottom line lives in a linked assessment artifact.
- **Bare confidence fields** (`confidence: low-to-medium`, `extraction_confidence: high`, `status: disputed`). A credence is not recomputable from ground truth, so as a frontmatter field it is precisely the "stale trusted cache is a trap" failure the mark discipline forbids (see the assessment-layer rule above and [`kb/types/tag-readme.md`](../../types/tag-readme.md)). Represent credences only as attributed, sourced assessments.
- **Implementing the full list directly in the framework.** ChatGPT's build order reads as a Commonplace roadmap; the boundary here is build-local-first in `epistack-casebooks` with collection-local types, upstream only what survives a worked case. Read its build order as a sequencing of *experiments in the sibling repo*.
- **Enumerating ~15 link labels up front.** Defer to collection-owned vocabulary (ADR 019) grown from need, guarded by the articulation test — except `correlated-with` / `independent-of`, kept above because they carry the independence-clustering idea.
- **Stance-carrying fields on the claim artifact** (`polarity: supports`, `status: disputed`). These smuggle a verdict into what should be a neutral node; the dialectical register's contract is what keeps the claim proposition decoupled from any verdict. Support/rebuttal belong on *edges*, attributed to a party, not as a scalar on the claim.

## Open questions

- Does the dialectical register warrant a new top-level collection, or can it be a `COLLECTION.md` variant inside the casebook repo until it proves out?
- Is `claim` a genuinely new type or a trait profile over `note` plus the new link vocabulary?
- Where does the gap register live — per-case, or a cross-case index — and does it need its own freshness signal?
- Can attributed-credence assessments be validated at all (e.g. "every credence cites its source and method"), or are they purely prose?

---

Relevant Notes:

- [epistack-competition](../epistack-competition/README.md) — see-also: the framework-side pointer and the `backlog-to-commonplace.md` interface this workshop feeds
- [mechanistic-constraints-make-popperian-kb-recommendations-actionable](../../notes/mechanistic-constraints-make-popperian-kb-recommendations-actionable.md) — grounds: why criticism must be externalized structure, and why contradictions get silently averaged
- [register](../../notes/definitions/register.md) — defined-in: the concept the proposed fourth register extends
- [ADR 023: quote-anchored citations](../../reference/adr/023-quote-anchored-citations-for-code-grounded-reviews.md) — draws-on: precedent for source-span citations
- [error correction works with above-chance oracles and decorrelated checks](../../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — rationale: why adversarial review must be decorrelated
