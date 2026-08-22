# Case 01: a workshop experiment design passed as a theory note

## Case record

On 2026-08-21, the full-improvement instruction was run on [`kb/work/causal-impact-selective-evaluation/experiment-design.md`](../explanatory-theories-deployment-time-learning/experiment-design.md).

| Field | Value |
|---|---|
| Pass | `20260821T103329Z-b7aa20` |
| Pass-start source SHA-256 | `3ff4cbb996d917d93b9a4561b8105e9674de4d64a49c0a93a6a3deb8d367cb16` |
| Final target SHA-256 | `60c16413a9f100f18e551f5f490db5af71c460c481af56854f1f1e2f5010c16b` |
| Starting collection/type | `kb/work/`; implicit `text` |
| Working function | proposed experiment design inside an exploratory workshop |
| Governing local frame | [`causal-impact-selective-evaluation/README.md`](../explanatory-theories-deployment-time-learning/README.md) |
| Procedure used | [`run-full-improvement-pass-on-note.md`](../../instructions/run-full-improvement-pass-on-note.md) |
| First commit containing the final target | `dc379e97` |

The ignored local evidence packet remains at `kb/reports/full-pass/experiment-design/20260821T103329Z-b7aa20/`. Its `source.txt` is the exact pass-start input. This case file records the material observations so the workshop does not depend on that ignored packet being available in another checkout.

At pass start, the artifact explicitly said it was a proposed comparison rather than a completed experiment or implementation plan. It proposed broad comparison arms and measurements. The surrounding workshop explicitly left the calibration protocol, final acceptance rule, materiality threshold, selection objective, and several other design parameters unchosen.

## Observable outcome

| Dimension | Pass-start artifact | Resulting artifact | Observation |
|---|---|---|---|
| Organizing point | The selector comparison appeared after a long SPADE account. | The offline comparison, online comparison, and separate generation factor became the top-level structure. | The main purpose became easier to recover. |
| Local readability | Imported `M`, `C`, and `Delta` notation carried meaning from a neighboring model. | The design uses plain noun phrases and local definitions. | Reader burden fell without an apparent loss of the intended distinction. |
| Source proportion | SPADE mechanics occupied most of the artifact. | SPADE became a shorter architectural example after the general design. | The artifact became more about its workshop task than its source recap. |
| Epistemic status | The opening disclaimed completed results and implementation status. | The opening still disclaims completed results and adds boundaries on deployment claims. | The proposal/result boundary remained visible. |
| Artifact representation | Plain Markdown with no frontmatter, permitted by the workshop contract. | Frontmatter declares `type: kb/types/note.md` and adds a retrieval description. | The pass changed type even though its packet first judged the implicit `text` type to fit. |
| Experimental commitments | The source named candidate arms, broad measures, cost categories, and a separate online comparison. | The result prescribes seeded effects, held-out human-audited obligations, continuing random omitted-obligation audits, two coverage definitions, a harmful-miss definition, and a predeclared advance rule. | The revision did more than clarify the source; it selected or narrowed substantive design choices. Exact thresholds remain open. |
| Reviewer interpretation | No single artifact mode was declared by the source. | Initial critique used `claim`; closing critique used `procedure`; closing premise decomposition again treated it as a claim. | The review family did not maintain a stable account of what kind of artifact it was evaluating. |
| Closing result | Not applicable before editing. | The new structure passed or largely satisfied the closing note-oriented checks; closing critique retained the audit-oracle/cost tradeoff. | Closing review tested coherence and defensibility inside the revised frame, not whether adopting that frame was authorized. |

## What worked

The run was mechanically disciplined. It captured and hashed the input, isolated review roles, retained initial and closing evidence, guarded the edit against concurrent changes, and reassessed the final bytes. Those properties remain useful independently of collection adaptation.

Several methods found real editorial problems:

- compression identified the buried comparison and excessive SPADE recap;
- structural review put the general experiment design before the specific source example;
- accessibility and prose reviews removed imported notation and improved local definitions; and
- closing critique showed that a polished design still faced an unresolved tradeoff between audit authority and the cost savings being tested.

The final text is clearer and more usable as an experiment-design discussion. This case is therefore not a simple bad-output example.

## Where contract fidelity became doubtful

The pass's synthesis packet stated that the artifact fit `kb/work/` as implicit `text`. The same packet then converted it to a `note` because a frontmatter gate found that raw text lacked a retrieval description. The local collection contract says plain Markdown is valid and warns against fixing workshop files merely to make them look like notes. A generally useful retrieval improvement therefore overrode the target's valid representation without a separate type-conversion decision.

The larger change concerned substantive authority. Reviewers correctly noticed that the proposed comparison lacked an independent adjudication surface and operational success criteria. Synthesis converted their repair ideas into body edits. In a claim note, adding the condition that makes a claim defensible may be an ordinary warrant repair. In a design artifact, choosing seeded effects, held-out audits, random omitted-region audits, and particular metric decompositions selects among workable designs. The pass had authority to improve the text, but neither the instruction nor the workshop frame established that it could make those selections.

The closing cycle then evaluated the artifact after those selections had become its premises. A pass on the resulting prose could show that the new design was coherent, clear, and still contestable. It could not show that the transformation from the old design to the new one preserved the artifact's decision boundary.

## Provisional diagnoses

These are hypotheses for later cases, not workshop decisions:

1. **Applicability is decided too late.** The current procedure runs note-shaped methods before its synthesis step judges collection/type fit, so early reviewers have already framed the target as a note.
2. **Method vocabulary supplies an implicit ontology.** “Central commitment,” premise decomposition, warranted contribution, title overreach, and claim modality make a truth-apt argument the default object even when the source is a design.
3. **Applicable gates can still be contract-inappropriate in combination.** A frontmatter gate can accurately report that a note lacks a description while the higher-level error is treating valid workshop text as a note at all.
4. **Synthesis conflates repair with selection.** It has rules for reconciling findings into edits, but no explicit boundary between clarifying an existing choice and choosing a new free parameter.
5. **Final-state review is not transformation review.** The closing cycle checks the final artifact but does not compare the edit against the source's allowed semantic and authority delta.

Further cases may defeat or narrow any of these explanations.

## Design responses still open

This case does not choose among at least four plausible responses:

- keep the current instruction strictly limited to eligible theory notes and reject other targets before starting;
- let it diagnose other artifacts but make non-theoretical or workshop cases report-only by default;
- introduce a common versioning/orchestration shell that routes to artifact-specific review and synthesis adapters; or
- build separate full-improvement procedures only when a collection or artifact family has enough worked cases to justify one.

Any of these could prevent this failure. They differ in complexity, reuse, and how much classification burden they place on the preflight.

## Questions carried forward

- What evidence distinguishes an editorial clarification from selection among a design's free parameters?
- Which source wins when collection, declared type, local framing, and inferred artifact function point in different directions?
- Can a pass safely infer artifact function, or must the function and mutation authority be declared for non-theoretical work?
- Should type conversion always be a separate authorized operation, even when frontmatter would improve retrieval?
- Which existing methods can review a design on problem, forces, free choices, and adoption criteria without turning recommendations into adopted design?
- What closing check can detect an unauthorized semantic or authority expansion across source and final versions?

## Relevant context

- [Workshop collection contract](../COLLECTION.md) — permits implicit text and defines progress, not note conformity, as the quality goal.
- [Artifact classification separates profile, content kind, lineage, and authority](../../notes/a-knowledge-base-holds-theories-descriptions-and-prescriptions-with.md) — supplies the region-level distinction exposed here: the design contained beliefs and candidate selections, while adopting those selections required separate authority.
- [Full improvement pass closure](../../reference/full-improvement-pass-closure.md) — says its reassessment evidence is local to the shipped note workflow and should not be generalized automatically.
- [Original note-improvement workshop](../agent-note-improvement/README.md) — shows that the pass was derived and calibrated on library-note cases.
