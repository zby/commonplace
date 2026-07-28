# Mixed-form learning

## Question

For which class of systems do localized natural-language and symbolic learning layers persist under model scaling — and which of the conjectures proposed for that claim deserve notes, which are revisions of notes we already have, and which fail?

Origin: a second external review round (2026-07-28) proposed conditionalizing the bitter-lesson defense on a system class — long-lived, composite, tool-acting systems persisting across sessions and model versions — with an umbrella conjecture and eight named sub-conjectures. This workshop holds the program while pieces are verified, named, and promoted. The first promotion is already out: [scaling absorbs scaffolding at fixed difficulty, not at the frontier](../../notes/scaling-absorbs-scaffolding-at-fixed-difficulty-not-at-the-frontier.md).

## Umbrella conjecture (working formulation)

> For long-lived, composite, resource-bounded agent systems under continual heterogeneous change, the efficient frontier of adaptation, reliability, cost, and governability is occupied by architectures that learn through multiple [representational forms](../../notes/definitions/representational-form.md): distributed-parametric state carrying broad amortized competence, natural-language state carrying not-yet-formalized theories and policies, symbolic state carrying exact transitions and checkable invariants — with mature systems moving commitments between forms as evidence, formalization, and model capability change.

Provenance discipline: the three-form triangle is representational-form's carve, which is *derived* (two axes, forced cells), so the umbrella inherits that derivation rather than being a fresh free choice — [rationale](../../notes/provenance-warrants-a-decompositions-scope-claim-use-earns-it.md). "Need" means worse-frontier, not computational impossibility; a learned architecture with stable semantic modules, explicit scope, and localized update paths would confirm the conjecture in a different substrate, not refute it.

## Conjecture inventory and dispositions

| Conjecture (review's name) | Status | Disposition |
|---|---|---|
| Moving-frontier | **promoted** | New note (link above). Second independent arrival — first surfaced in the closed scaffolding-relaxation workshop as "recedes, then reappears at the new edge." |
| Validation radius (under "deployment-tempo") | **landed** (2026-07-28) | Applied: the [readable-artifact loop](../../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) now factors by deployment-pace updates *plus bounded validation radius* rather than update cost, with the falsifier stated and the scoped/attributable/regression-checked condition cross-linked to the authoritative-record note; [deploy-time learning](../../notes/deploy-time-learning-is-the-missing-middle.md) names the two reasons of different durability. |
| Symbolic-layer writability bridge | **landed** (2026-07-28) | Applied to [scheduler-LLM separation](../../notes/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md): bias claims relativized to the implemented transition function with the wrong-spec case delegated to the relational [fixed-artifacts split](../../notes/fixed-artifacts-split-into-exact-specs-and-proxy-theories.md), plus the bridge paragraph — the symbolic layer is a learning target and codification is the write path into it. The general form of the bridge stays reserved for the central note. |
| Oracle accumulation | **promoted** (2026-07-28) | Overlap check done: [oracle strength spectrum](../../notes/oracle-strength-spectrum.md) owns per-component hardening (including failures→regression tests); the loop-level consequence was unowned and is now [a note](../../notes/oracle-accumulation-improves-the-selection-environment.md) — two retention channels on different wires (lessons ride retrieval, enforced checks ride the exhaustive wire), the movable warranted-autonomy boundary, and amortized validation radius. |
| Change-topology matching | **promoted** (2026-07-28) | New note: [localized retention pays where change is sparse in a matching decomposition](../../notes/localized-retention-pays-where-change-is-sparse-in-a-matching.md) — chosen over folding because the claim inherits Parnas's information-hiding criterion (held source, bridge stated) and is cited as a premise by the radius and addressability arguments. Mechanism edge added to [reflection buys addressability](../../notes/reflection-buys-addressability.md); the dense-change converse (gradient descent as the matched medium for diffuse drift) feeds the central note's mixed-form argument. |
| Preformalization | mostly owned | [Theory-mediated learning](../../notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md) and [codification](../../notes/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) carry it. Residue worth adding: the load-bearing requirement is a writable, semantically open metalanguage — not English prose specifically. |
| Deployment-tempo | owned | [Deploy-time learning](../../notes/deploy-time-learning-is-the-missing-middle.md), pending the validation-radius upgrade above. |
| Governed autonomy | owned | [Warranted autonomy](../../notes/warranted-autonomy-is-bounded-by-oracle-domain.md) plus the article's legibility passage. Framing worth stealing: mixed-form systems are more *deployable*, not more intelligent — a deployment-selection claim. |
| Institutional continuity | owned | The commitment/authority arc: [commitment creates ground truth](../../notes/commitment-not-derivation-creates-new-ground-truth.md), [parametric reproduction cannot replace an authoritative record](../../notes/parametric-reproduction-cannot-replace-an-authoritative-record.md). |
| Bidirectional codification | promotion | [Codification and relaxing](../../notes/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) reads as design guidance; promote to a comparative conjecture. Its four-arm experiment (NL-only / symbolic-only / one-way promotion / bidirectional) belongs beside the ablation-baselines proposal in `kb/reference/proposals/`. |

## Vocabulary tasks

- **Done (2026-07-28):** retitled to [treat continual learning as representational-form coevolution](../../notes/treat-continual-learning-as-representational-form-coevolution.md) via `commonplace-relocate-note` (28 files rewritten, ProperDocs redirect added).
- The review proposes "localized operative representations" for what natural-language and symbolic forms share (addressability plus a stable causal route into behavior). Expect naming rounds; scrutinize for hidden dichotomies before adopting.

## Source verification list

Held (citable now): [OpenAI harness engineering](../../sources/harness-engineering-leveraging-codex-agent-first-world.ingest.md), [Claude Workstream Kit](../../sources/claude-workstream-kit-fable-agent-scaffolding.ingest.md), [vertical-agent context engineering](../../sources/building-a-good-vertical-agent-2065190286519906657.ingest.md), [KSI](../../sources/knowledge-centric-self-improvement-2607.19592.ingest.md), ACE (agent-memory review), [Meta-Harness](../../agent-memory-systems/reviews/meta-harness.md) (code-grounded review plus ingest).

To snapshot and verify before anything cites them: Anthropic long-running-agents engineering post; Co-Harness preprint (reported 2026-07-17, harness/fine-tune alternation); ToolGate (arXiv 2601.04688); Memento-Skills; Agent Symbolic Learning (arXiv 2406.18532).

## What would close this workshop

- Every inventory row dispositioned: note written, revision landed, or rejected with a reason.
- The umbrella promoted to one central note (candidate title: "Heterogeneous change favors mixed-form learning") linking the specialized conjectures — or a recorded decision that the existing cluster already carries it.
- The article's bitter-lesson section updated with the fixed-task/moving-frontier distinction, after the notes exist.
- The source list resolved: snapshotted or dropped.

## Next useful step

The vocabulary tasks (substrate→representational-form retitle first) and source snapshots; then the central note, which now has its three legs promoted (moving-frontier, oracle-accumulation, change-topology matching).
