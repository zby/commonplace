---
description: "Proposal: improve notes by running focused single-aspect review passes — each constraining attention to one failure mode so the lens actually engages — drawn from an open-ended catalogue we never expect to complete, applied while marginal improvement beats the pass's budget cost. Organizes review around marginal value, not coverage; contrasts with the maintained-converging-checklist model"
type: kb/types/note.md
traits: [design-proposal]
tags: [kb-maintenance]
status: seedling
---

# Focused single-aspect review passes from an open-ended catalogue

A note accrues defects across many independent dimensions — logical validity, grounding, internal consistency, readability, accessibility, structure. A single undifferentiated "review this note" pass spreads attention across all of them at once, and the reviewing agent then reads past defects the same way a fluent reader does: carried by the prose. The proposal: improve a note by running **focused single-aspect passes**, each constraining attention to one failure mode so the lens actually fires, drawn from a catalogue we treat as **permanently open-ended**, and applied **while the expected improvement of the next pass exceeds its budget cost**. The organizing target is marginal value, not coverage.

The design rests on three commitments, only the first of which is a transferable claim (cited below as `rationale`):

1. **Focus gives a pass teeth.** A reviewer evaluating "everything" is subject to the same fluency-smoothing as the writer and reader — it reads over a weak "because." Constraining the pass to one aspect, ideally in a fresh/separate context, forces the lens to engage and reconstructs a signal the diffuse pass would miss.
2. **The catalogue is irreducibly open-ended.** We will never enumerate every way a note can fail. So this is a generative practice — spin up whatever lens seems at risk — not a fixed checklist or a completeness target.
3. **The stopping rule is marginal value, not completeness.** Run lenses while each one's expected accepted-edit yield beats its token cost. "Did we cover everything" is unreachable and the wrong question.

## Current state (as of 2026-06-15)

The shipped review subsystem already supplies focused passes and budget-bounded loading; what it lacks is the explicit anti-completeness stance and ad-hoc (non-registry) lenses.

- **Atomic gates** under `kb/instructions/review-gates/{lens}/{name}.md` are exactly single-aspect lenses; bundles group them by lens (accessibility, complexity, frontmatter, prose, semantic, sentence, structural).
- **Hand-run focused passes** exist outside the registry: `kb/instructions/critique-note.md` (attack the central commitment) and `kb/instructions/composition-friction-gate.md` (audit inferential joints, default-skeptical). Both are report-only and route attention rather than deciding.
- **Budget-bounded gate loading** is already proposed in [gate-learning-from-accepted-edits](./gate-learning-from-accepted-edits.md) ("a fixed token budget beats a fixed gate count").

Direct evidence from one note this session: three independent modes ran on `llm-generation-relaxes-goals-where-human-writing-stalls.md` — the critique gate (thesis-level steelman), the composition-friction gate (joint-level), and seven review bundles. The joint-level gate caught an `UNSUPPORTED` inference the thesis-level critique passed over; the sentence and accessibility bundles caught readability and reference debt the logic-focused gates ignored. **No single lens subsumed the others** — direct support for commitments 1 and 2.

## The free choice: open-ended vs maintained-converging

The sharp design fork is against the existing theory. [Elicitation requires maintained question-generation systems](../../notes/elicitation-requires-maintained-question-generation-systems.md) prescribes a maintenance loop that *converges* toward coverage (discover → codify → prune stale). This proposal takes the opposite stance: do not try to converge; accept permanent incompleteness and bound by budget instead. The options:

- **A — Pure opportunistic.** No fixed catalogue; choose each lens ad hoc by what the note seems at risk of. Maximally flexible; risks systematic blind spots a checklist would cover.
- **B — Maintained-converging checklist.** The elicitation model: a registry that grows toward coverage and prunes stale entries.
- **C — Hybrid (leaning).** A small always-on base set (cheap, high-precision) plus opportunistic ad-hoc lenses spent against a budget. This is roughly what the gate selector already gestures at; the proposal's addition is *first-class support for ad-hoc lenses outside the registry*.

The proposal does not decide between these; it argues only that the marginal-value framing should govern whichever is chosen.

## Adoption criteria

The design earns adoption if, measured against a single comprehensive pass of equal cost:

- focused passes yield more accepted edits per token;
- ad-hoc lenses (ones in no fixed catalogue) regularly produce accepted edits — evidence the open-endedness pays;
- a budget stopping rule beats a fixed-count rule on accepted edits per token.

## Risks

- **Over-flagging.** A lens primed to find X finds X even when absent (the friction gate's `default to UNSUPPORTED` trades false positives for teeth). Output must route attention to a human, never auto-apply.
- **Lens proliferation / diminishing returns.** The budget rule bounds total spend, but *which lens next* is itself a judgment with no oracle — the meta-selection problem.
- **Blind spots from no catalogue.** The anti-completeness stance's cost: systematic failure families a maintained checklist would reliably cover may go unprobed if no one thinks to spin up the lens.

## Open questions

- How to choose the next lens cheaply, given no oracle for "what is this note most at risk of"?
- Should lenses be chosen for mutual *decorrelation* to maximize combined signal (see the decorrelated-oracles rationale)?
- Is this materially different from the shipped gate selector, or just "permit ad-hoc lenses + adopt the marginal-value framing"?
- Should commitment 1 ("focus gives teeth") be promoted to its own theory note rather than living only as a rationale edge from here?

---

Relevant Notes:

- [LLM generation relaxes a goal it can't satisfy and hides the constraint a human writer stalls on](../../notes/llm-generation-relaxes-goals-where-human-writing-stalls.md) — rationale: why focus gives teeth — a diffuse reviewer is subject to the same fluency-smoothing as the writer, and a separate focused pass reconstructs the stalled joint it would otherwise read past
- [Semantic review catches content errors that structural validation cannot](../../notes/semantic-review-catches-content-errors-that-structural-validation.md) — precedent: a fixed set of focused semantic checks; this proposal generalizes the catalogue to open-ended and budget-bounded
- [Elicitation requires maintained question-generation systems](../../notes/elicitation-requires-maintained-question-generation-systems.md) — tension: the maintained-converging-checklist model this proposal's anti-completeness stance pushes against
- [error correction works above chance with decorrelated checks](../../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — rationale: each focused lens is a weak, decorrelated oracle; combining decorrelated lenses amplifies discriminative power
- [review architecture](../review-architecture.md) — part-of: the shipped review subsystem (gates, bundles, selector) this practice would extend
