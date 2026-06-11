# Workshop: What the theory register admits

## Goal

Brainstorm the theoretical register's admission policy. `kb/notes/` is built around contestable claims, but at least three kinds of artifact want to live there with different epistemic standing: **claims with support**, **hypotheses** (claim-shaped, low commitment), and **design proposals** (not claim-shaped at all — free parameters, evaluated by usefulness). Decide how the register should treat each, and how much of that needs codifying now versus deferring.

## Trigger case

`kb/notes/trace-derived-memory-matures-through-an-epistemic-authority-ladder.md` (uncommitted at workshop start) carries `title-as-claim` but is a design proposal: the five-rung factoring, the verification-coverage metric, and the operating-point stance are arbitrary choices whose consequences are hard to isolate. The contestability test doesn't fail for it — it doesn't *apply*. Resolving that note under whatever policy emerges is part of closing this workshop.

## Ideas established in discussion (2026-06-11)

1. **Arbitrary choices are the discriminator.** A hypothesis is a claim with the commitment dial turned down — truth-apt, contestable, handled today by claim title + `status: speculative`. A design proposal has design degrees of freedom: it can't be false, only unhelpful or unadopted. Treating one as the other is a category error, not a weak claim.

2. **The existential-theory recast.** A design proposal is not a good *universal* theory — too many arbitrary choices, consequences hard to isolate. But it might stand as an **existential claim**: "There exists a system that meets requirements R — for example, [the arbitrary choices construct one]." The construction is the witness; arbitrary choices are legitimate inside a witness, since any witness proves an existential. This may be the move that lets design proposals into a claims register honestly. Open: what the requirements R must look like for the existential to be contestable rather than vacuous, and whether the witness's choices then need marking as non-load-bearing.

3. **Hypotheses may want a distinct marker — but maybe not yet.** Candidate: an optional `epistemic-status` frontmatter field separating "conjectured" from "supported" independently of the commitment dial (`status`). YAGNI guard from discussion: defer until we actually start confusing hypotheses with supported theories. Part of this workshop's job is deciding whether that confusion is already happening (see squatters below).

4. **De facto squatters under `status: speculative`.** The status currently shelters both kinds. Claim-shaped hypotheses: `flat-memory-predicts-specific-cross-contamination-failures…`, `topology-isolation-and-verification-form-a-causal-chain…`. Design proposals with hedged or topic titles: `selector-loaded-review-gates-could…` ("Brainstorm on…"), `backlinks.md` (four design options), `quality-signals-for-kb-evaluation.md` (signal catalogue). Whatever policy emerges should be checked against these.

5. **Structural reading of the gap.** A design proposal is the immature form of a *prescriptive* artifact, as a hypothesis is the immature form of a theoretical claim — but the prescriptive surface only admits adopted artifacts (instructions are operative, ADRs record decisions made). Proposals squat in the theory register because there is no pre-adoption prescriptive state, `kb/work/` closes rather than waits, and the YAGNI rule explicitly routes identified gaps to `kb/notes/`. The existential recast (idea 2) and a pre-adoption prescriptive state are competing answers to the same gap.

## What would close this workshop

- A decision on how the theory register treats design proposals — existential-claim recast, a `design-proposal` trait/status with its own quality test, a pre-adoption prescriptive home, or an explicit decision to keep the current hedged-title practice — codified where it binds (`kb/notes/COLLECTION.md`, `kb/types/note.md`, or an ADR), or an explicit deferral note.
- A decision on hypothesis marking (`epistemic-status` field or equivalent), including "not yet" with the trigger condition that would revisit it.
- The trigger-case note resolved under the new policy.

---

Relevant Notes:

- [trace-derived memory matures through an epistemic-authority ladder](../../notes/trace-derived-memory-matures-through-an-epistemic-authority-ladder.md) — tests: the trigger case the policy must resolve
- [alexander patterns and knowledge system design](../../notes/alexander-patterns-and-knowledge-system-design.md) — draws-on: Context/Problem/Forces/Solution is prior art for what a design-proposal quality test could check
- [register](../../notes/definitions/register.md) — defined-in: the three-register model whose theoretical slot this workshop re-examines
