# Eigenius contact points: a whole-system witness for the verification-locus theory

Working note. Eigenius (local clone at `related-systems/eigenius/`, gitignored) is an open-source typed knowledge-graph platform for verifiable AI in science: content-addressed immutable layers, four enforced epistemic categories (Declared / Observed / Derived / Verified), commit-time gates, replayable derivations, Lean 4 proof checking. Its method docs (`docs/method/reasoning.md`, `docs/method/grounding.md`) and design docs (D39 justification logic, D54 lemma citation, D58 obligation graphs, D61 grounding discovery, D62 encoding pipeline) run this workshop's problem list from the far end of the constraining axis. It belongs beside Build Systems à la Carte, PROV, and in-toto as a literature anchor — roughly those three unified in one substrate, with justification logic on top.

Clone paths below are repo-local pointers, not durable links; promotion (source ingest or an `kb/agentic-systems/` review) is a separate decision.

## Against the kernel: both bridges at once

The verification-locus kernel names two bridges from history to checkable state: records (attestation) and re-derivability (reproducibility). Eigenius is a bet on operating both simultaneously, with the epistemic category recording which bridge a claim crossed:

- **Re-derivability bridge** — Derived and Verified. Typed pipelines over content-addressed inputs make derivations replayable; per-category factivity (D54 §5.2) states Derived as "true relative to the *content-addressed* data + deterministic method" — the reproducibility bridge with its trust condition made explicit.
- **Record bridge** — Declared and Observed. Declared is "explicitly non-factive"; Observed is defeasible measurement-with-provenance. Both are testimony: trust the recorder.

So their four categories are a **graded factivity vocabulary for the checkable/credence witness split** — finer than our binary regime, and attached to claims rather than to witness fields. Candidate borrow for the carried-witness family: a witness's regime is not just checkable-vs-credence but sits on a factivity grade that names its trust condition.

## Trace vs warrant — a distinction our ladder mixes

D39 §12: "reasoning traces describe *what happened* … justification terms describe *with what warrant*." In our terms: a trace is reified history (an L1 record; journal entry, non-recomputable), while a justification term is a carried witness that makes a state check bounded. Eigenius separates the two structurally; our review reports and event-ledger discussions currently mix execution record and warrant in one artifact. Worth naming when the ladder notes are extracted: L1 records answer *what happened*; carried witnesses answer *why believe it* — different consumers, different invalidation.

## They solve both flagged gaps

The two gaps in [verification-locus-and-provenance-theory.md](./verification-locus-and-provenance-theory.md) ("write down, don't build") both have working Eigenius counterparts:

- **Gap: radius-1 assay results have unhashed inputs.** Their dependency invalidation is total: every derivation pins content-addressed inputs, so "which downstream analyses need revalidation" is a query ("This is a query, not a meeting" — `docs/design/vision.md`). This is the factored `(note, cited-target)` pair escalation carried to every edge. The cost profile is the reason we don't: they pay full codification of all content to get it.
- **Gap: link text is a checkable witness that nothing checks.** D54 lemma citation is title-as-claim traversal-as-reasoning with a mechanical drift guard: a committed sentence is cited by typed reference, and "a wrong restatement fails to type-check, never silently unsound" (D54 §4.1). Confirms the gap is real and the fix is a check on the *carried text*, not on link health; our cheap-join validator candidate is the natural-language analogue.

Also on citation semantics: "cite the proposition-bearer, never the Verdict" (D54 §4.3) — their verdicts attest "the gate ran and reached this verdict," not the proposition. Independent confirmation of our result-kind stance that review outcomes are execution state, not citable knowledge.

## Against the ladder: the no-L0 bet, plus a monotonicity rule

Eigenius has no untracked rung: every claim is watched (our L3/L4) by commit-time gates, and the manifesto refuses to weaken this ("we will not compromise the type system for adoption"). Our graduated ladder is precisely the opposing bet — assign rungs by retroactive reach because total watching is unaffordable over natural-language artifacts. Two things transfer anyway:

- **No silent downgrade.** "A derived result can be promoted to verified by attaching a proof, but a verified result cannot be silently downgraded" (`vision.md`). Candidate explicit rule for freshness baselines and for L2 batch decisions: status transitions are monotone or recorded, never silent.
- **Production-time enforcement of process contracts.** Their Discovered gate (D61/D58) blocks a conclusion from committing while a named competency question is ungrounded — a history property ("did the author consult the right prior knowledge?") enforced at the only time it is enforceable. This is Corollary 1's "push out to the skill" exit, institutionalized in a kernel; same move as pre-registration/registered reports in the phil-sci anchors.

## The two-oracle architecture matches the three-layer sieve

D61 names the limit of their own codification: "checker-passing ≠ faithful" — the kernel (oracle #1) proves a claim follows from admitted evidence, never that the formalization captures intent (oracle #2). Their measured LLM-judge inflation (~97% judge vs ~66% human agreement) makes them cap mechanized faithfulness checks at Derived, "never auto-Verified"; only human spot-check or proof-level correspondence elevates further. Mapped to the sieve:

| sieve layer | Eigenius counterpart |
|---|---|
| structure → deterministic validator | kernel type/gate checking (oracle #1) |
| semantic contract → LLM reviewer | faithfulness backstop, grade-capped at Derived (oracle #2) |
| process → producer at production time | Discovered gate; two-phase vocabulary-first authoring (D39 §4.5) |

The convergence is the finding: a maximally codified system arrives at the same three-way partition from the formal side, and concedes the semantic layer to judged reading exactly where our review system lives. Their grade cap is our PASS-verdicts-are-not-endorsements stance stated as an epistemic rule.

## Non-retrofittability, corroborated

D58: "a separate 'formalize what we built' pass at the end is the anti-pattern — by then the grading is archaeology, not method." And `reasoning.md`: the chain is "the working memory of the reasoning, not a write-up made afterward." Both restate the workshop's one non-deferrable rule — history can only be recorded at the time — as authoring method rather than storage policy.

## Model provenance

Their LLM calls are recorded per invocation as typed trace resources carrying prompt, response, and provider configuration — provenance on the *derivation event*, while the produced resource carries only its warrant. Supports [model-provenance.md](./model-provenance.md)'s position: model identity is L1/L2 event-record territory, not canonical-artifact frontmatter.

## What to take (candidates, for extraction rounds)

1. Add Eigenius to the literature anchors of the verification-locus file when the seedlings grow — it is the only anchor that is itself an *agent-operated* provenance system rather than a build/supply-chain one.
2. Graded factivity as vocabulary for witness regimes (checkable/credence → factive / conditionally factive / defeasible / non-factive).
3. The trace-vs-warrant distinction, named, in the ladder extraction.
4. No-silent-downgrade as an explicit baseline/L2 rule.
5. The Discovered gate as the worked example that some process contracts are enforceable — but only at production time (strengthens Corollary 1 rather than contradicting it).

---

Relevant notes:

- [verification-locus-and-provenance-theory.md](./verification-locus-and-provenance-theory.md) — grounds: the theoretical spine these contact points map onto
- [model-provenance.md](./model-provenance.md) — is-evidence-for: event-side model recording
- [history has one chance to become checkable](../../notes/history-has-one-chance-to-become-checkable.md) — is-evidence-for: their authoring-time chain discipline is the claim practiced as method
- [criteria edits invalidate verdicts; process edits invalidate artifacts](../../notes/criteria-edits-invalidate-verdicts-process-edits-invalidate-artifacts.md) — is-evidence-for: their total dependency invalidation is the verdict half carried to every edge
- [a derived copy of recomputable truth must be checked or absent](../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — see-also: their drift detectors (D35) enforce the same rule at load time
