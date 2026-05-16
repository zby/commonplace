# Workshop: auditable-llm-editing

Goal: test whether explicit, sparse writing state can make LLM-assisted editing more convergent by preventing accidental claim drift while still allowing useful prose improvements.

**Status: active.** Initial phase is protocol design plus small manual trials on real drafts.

## Starting claim

Many LLM editing operations are locally improving but not convergent. Repeated prompts such as "make it clearer", "make it more concise", or "make it more professional" can improve a draft for a few passes, then start smoothing away meaning, changing emphasis, weakening voice, or replacing specific claims with generic prose.

The proposed control surface is a structured writing state:

```text
S = (text, claim_ledger, presentation_spec, rubric, gap_policy)
```

Edits are typed:

- **Text edit** — changes wording, organization, transitions, or local emphasis while preserving the claim ledger.
- **Claim edit** — explicitly adds, removes, merges, splits, weakens, strengthens, or reanchors a claim.
- **Presentation-spec edit** — changes how the piece should sound, frame its claims, or preserve its rhetorical constraints.
- **Rubric edit** — changes what counts as improvement for this piece.
- **Gap-policy edit** — changes how unsupported theory bridges are marked, closed in text, or extracted as note candidates.

The first invariant to test: claims should not change accidentally. They may change, but only through an explicit claim-revision step.

## Why this needs a workshop

The obvious expansion is a richer state object: evidence, assumptions, definitions, caveats, examples, discourse roles, target reader, argumentative dependencies, and so on. That may help, but it can also create a new failure mode: the model over-extracts structure, invents obligations, or turns tentative interpretations into false invariants.

This workshop therefore starts with lazy extraction:

1. Extract only a minimal claim ledger.
2. Anchor each claim to text spans.
3. Mark claims by status.
4. Add new structure only when a real editing failure shows the existing state was insufficient.

The experiment is not to build a complete handcrafted ontology of writing. The structure is a human-facing control surface for auditability and intervention. The scalable substrate should be search, comparison, learned evaluators, preference feedback, and accumulated edit history.

## Initial artifacts

- [protocol](./protocol.md) — trial design, prompts, measures, and stop conditions.
- [v0-two-loop-algorithm](./v0-two-loop-algorithm.md) — first operational loop: select one tuple part, write a complete candidate state, verify against the frozen rest.
- [editor-prompt](./editor-prompt.md) — sub-agent prompt for producing complete candidate states.
- [verifier-prompt](./verifier-prompt.md) — sub-agent prompt for independently checking candidates.
- [state-template](./state-template.md) — minimal writing-state schema for trials.
- [failure-log](./failure-log.md) — place to record drift, over-extraction, rubric failure, and presentation damage.
- [experiment-conclusion](./experiment-conclusion.md) — current takeaway from the first two trials.

## Experiments

- [experiment-01-memory-derivation](./experiment-01-memory-derivation/README.md) — first trial using a copied agent-memory design derivation draft.
- [experiment-02-full-memory-article](./experiment-02-full-memory-article/README.md) — second trial freezing the accepted derivation prelude while refactoring the concrete memory-needs list below an explicit boundary.

## Experimental question

Does a sparse, anchored claim ledger reduce semantic drift across repeated LLM editing passes compared with ordinary edit prompts, without freezing useful revision?

Secondary questions:

- Which failures remain after claim anchoring?
- Which extra structures are justified by observed failures?
- When does the structure become too expensive or too brittle?
- What parts should become reusable review gates, instructions, or learned evaluators?

## What would close this workshop

The workshop closes when it produces one of:

- A negative result: claim-ledger editing does not reduce drift enough to justify the overhead.
- A narrow procedure: a reusable instruction for stateful editing with a minimal claim ledger.
- A broader methodology note: when sparse writing-state control surfaces are useful, where they fail, and how they fit the bitter-lesson boundary.
- Candidate review gates or validator checks derived from repeated failure patterns.

## Relevant local context

- [review-revise-gated](../review-revise-gated/README.md) — prior workshop for scoring review/revision arrangements against accepted edits.
- [Semantic review catches content errors that structural validation cannot](../../notes/semantic-review-catches-content-errors-that-structural-validation.md) — background: semantic checks need structured rubrics but remain judgment-dependent.
- [Selector-loaded review gates could let review-revise learn from accepted edits](../../notes/selector-loaded-review-gates-could-let-review-revise-learn-from.md) — possible maturation path for recurring editing failures.
- [Codification and relaxing navigate the bitter lesson boundary](../../notes/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) — framing: codify control surfaces for current leverage while watching for structures that should relax into learned mechanisms.
- [Human writing structures transfer to LLMs because failure modes overlap](../../notes/human-writing-structures-transfer-to-llms-because-failure-modes.md) — rationale for testing specific writing structures against specific LLM failure modes.
- [Writing styles are strategies for managing underspecification](../../notes/writing-styles-are-strategies-for-managing-underspecification.md) — style is not cosmetic only; it allocates autonomy and constraint.
