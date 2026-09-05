# C09 acceptance — placements read a tracked main review

Executed locally on 2026-09-05 against
[`place-external-systems`](../../instructions/simplification-passes/place-external-systems.md).
Its catalog was updated; its orchestration packet still supplies the artifact,
purpose, preserved claims, and write scope without an interface change.

## Bounded artifact and evidence

The trial artifact consists of these fixed criteria: distinguish an implemented
retention route, an implemented later-retrieval route, observed delivery to a
model, observed behavioral activation, and measured downstream benefit. These
are evaluation criteria for this trial; they do not claim that any target meets
them. Write scope is this acceptance record only.

The sole system-characterization input was the generated
[Pond review](../../agentic-systems/reviews/pond.md), read directly:

- Path: `kb/agentic-systems/reviews/pond.md`.
- SHA-256: `4f7dff6046723b9b7e11e526293a2f1849e53ad780426e391df4dbc0b24deb35`.
- Run: `AAS-2026-09-04-pond-01`.
- Source identity: `https://github.com/tenequm/pond`.
- Reviewed revision: `bb4f791ba1be6d4a70cf007e1bee9eb8008d9334`.
- Evidence basis: source and design inspection, without a live corpus or host run.

No exact local result, completion state, legacy review, source ingest, or new
source inspection was needed for these placements. The public review's frozen
findings can support them independently of the current run-state schema defect
recorded in C08. This does not claim that a new run completed successfully.

## Returned paragraph

[Pond](../../agentic-systems/reviews/pond.md) wires session retention and
caller-triggered retrieval; its ingestion validator checks canonical event
structure, identities, and provenance. This places it at implemented storage
and retrieval mechanisms, while observed model delivery, behavioral activation,
and downstream benefit remain uninspected in the review's source-only boundary.

The selected example therefore separates implemented mechanisms from their
unmeasured use and effect. It supplies no operational or causal test of the
later criteria.

## Support and withheld placements

| Placement | Supporting location or reason for withholding |
|---|---|
| Ingest admission checks structure and provenance | Runtime progression: the validator checks event order, identities, parent coherence, part provenance, and Pond-owned ingest metadata. |
| Caller-triggered retrieval is wired | Runtime progression: “The ordinary read path is explicit.” The following sentences describe caller-selected search and bounded transcript expansion. |
| Behavioral effect remains uninspected | Host integrations and authority: “No behavioral-effect claim is observed or causally supported by this source-only analysis.” |
| Withheld: first-party integrations automatically push recalled session content | Canonical fidelity and context selection explicitly says no first-party integration automatically selects retained session content for a model. Static routing instructions are distinguished from recalled memory. |
| Withheld: retrieval demonstrably improves later answers | Architectural assessment lists retrieval quality, actual model activation, and behavioral improvement outside the demonstrated boundary. |

The contestable boundary is the phrase “implemented storage and retrieval”:
it describes inspected wiring, not observed durability or successful recall in
a deployment. The paragraph preserves that qualification. No missing detail
was treated as evidence of absence, and no withheld placement was filled from
the legacy review.

## Acceptance

The input hash was rechecked before retaining this paragraph and matched.
The changed instruction, catalog, and acceptance record validated with zero
failures and zero warnings. Semantic verification was local.

C09's reader migration is accepted. This trial uses a public review that
contains sufficient evidence and checks unsupported-claim rejection; it does not test a newly retained
exact-result publication or broaden the system population. The procedure now
withholds library insertions whose support exists only in ignored state.
