# Premise and mechanism implementation packet

**Date:** 2026-07-29

**Status:** phase A is ready for maintainer approval; phase B is semantically settled except for one prerequisite-family hold and must not execute yet. No durable catalogue, contract, ADR, or corpus change has been made.

## Recommended implementation split

Use two atomic directional-label migrations rather than one 374-row edit:

1. **Phase A — retire `mechanism`.** Adopt `explained-by` and `operates-through`, update current guidance, and migrate all 82 active `mechanism` tuples. This phase is complete and independently executable: 81 tuples have exact successor labels and one is removed.
2. **Phase B — retire `grounds`.** Adopt `premised-on`, add the demonstrated notes→notes `is-evidence-for` pairing, and migrate the 292 active `grounds` tuples. Do not execute this phase until `F094` receives an exact label from the `enables` / `precondition` family review; `prerequisite-hold` is a disposition, not a registered identifier.

This split lets `mechanism` reach zero without preserving a synonym or inventing a temporary prerequisite label. It also keeps an accepted ADR truthful: phase A can describe implemented behavior while phase B remains workshop state until every active `grounds` tuple has a successor or removal.

## Live planning baseline

The [live disposition manifest](./premise-mechanism-live-disposition-manifest.tsv) freezes the current active mutable surface with exact source and target identities, source/destination collections, current line and line digest, decision provenance, action, and authorization status.

| current label | live tuples | relabel | remove | hold |
|---|---:|---:|---:|---:|
| `mechanism` | 82 | 81 | 1 | 0 |
| `grounds` | 292 | 287 | 4 | 1 |
| **total** | **374** | **368** | **5** | **1** |

The active pairings are 366 notes→notes, seven sources→notes, and one reference→notes. Generated reports, workshop history, archived proposals, immutable snapshots, quotations, and ordinary prose are outside this active registered-edge baseline.

The full accepted disposition is:

| disposition | rows |
|---|---:|
| `premised-on` | 168 |
| `explained-by` | 73 |
| `extends` | 34 |
| `operates-through` | 33 |
| `exemplifies` | 21 |
| `defined-in` | 15 |
| `evidenced-by` | 11 |
| `is-evidence-for` | 10 |
| remove | 5 |
| `contrasts` | 2 |
| `rests-on` | 1 |
| `prerequisite-hold` | 1 |
| **total** | **374** |

The decision provenance reconciles exactly: 87 accepted mechanism-core rows, 42 mechanism-boundary rows, 155 surviving original premise rows, 69 surviving grounds-boundary rows, and 21 accepted drift rows.

## Registered semantics

All three proposed identifiers are asymmetric, source-as-subject, and have no required inverse. Target artifact type is not sufficient to choose between them; the source's assertion and revision consequence decide.

### `premised-on`

> theoretical assertion source `premised-on` premise target

- **Follow:** verify a proposition on which the source's truth or applicability depends.
- **Skip:** when looking for a causal account, actual operating path, corroborating case, or merely prior operational availability.
- **Revision consequence:** rejecting or materially revising the target reopens whether the source assertion holds or applies.
- **Boundary test:** the source imports the target proposition as a condition of its argument. If the target instead accounts for why/how the source occurs, use `explained-by`; if it participates in producing the effect, use `operates-through`; if it corroborates the claim without being required by it, use `evidenced-by`.

### `explained-by`

> source claim or effect `explained-by` target account or principle

- **Follow:** understand why or how the source occurs or holds.
- **Skip:** when the task is to inspect the actual component, control path, artifact, process, or operational rule used to produce it.
- **Revision consequence:** rejecting or materially revising the target reopens the source's explanatory account, but does not by itself assert that an implemented path changed.
- **Boundary test:** the target functions as an account of the source. A process-shaped target can still be explanatory when the source does not literally use it as its operative path.

### `operates-through`

> source effect or behavior `operates-through` target process, component, control path, artifact, or operational rule

- **Follow:** inspect the actual pathway or machinery producing the source effect.
- **Skip:** when the target only supplies a principle or causal account, or is merely required beforehand.
- **Revision consequence:** changing the target prompts interface, behavior, delivery, or operational-fit review at the source.
- **Boundary test:** the source literally uses or is realized through the target. Availability alone is a prerequisite relation; an account without operational participation is `explained-by`.

## Exact authorization audit

| source → destination | disposition | current rows | current authorization | required decision |
|---|---|---:|---|---|
| notes → notes | `explained-by` | 73 | absent | register label and pairing |
| notes → notes | `operates-through` | 33 | absent | register label and pairing |
| notes → notes | `premised-on` | 168 | absent | register label and pairing in phase B |
| notes → notes | `is-evidence-for` | 3 | absent | add pairing in phase B |
| sources → notes | `is-evidence-for` | 7 | authorized | no change |
| reference → notes | `rests-on` | 1 | authorized | no change |
| notes → notes | all other exact labels | 83 | authorized | no change |
| notes → notes | removal | 5 | not applicable | delete exact footer rows |
| notes → notes | prerequisite hold | 1 | unresolved | family review before phase B |

No notes→notes `see-also` authorization is needed. The five weak-adjacency rows are removals. No reference→notes authorization is needed for either new mechanism successor: the sole reference row is exactly `rests-on`.

## Phase A — executable `mechanism` migration

### Corpus disposition

| successor/action | active `mechanism` rows |
|---|---:|
| `explained-by` | 39 |
| `operates-through` | 28 |
| `exemplifies` | 6 |
| `extends` | 3 |
| `defined-in` | 2 |
| `evidenced-by` | 1 |
| `contrasts` | 1 |
| `rests-on` | 1 |
| remove | 1 |
| **total** | **82** |

The notes source owns 81 rows; the one reference→notes row becomes the already-authorized `rests-on`. The removed row is `F043`, the notes→notes weak companion the maintainer directed us to drop.

### Proposed ADR 061

Target: `kb/reference/adr/061-mechanism-splits-into-explained-by-and-operates-through.md`.

The implemented ADR should:

- amend ADRs 009, 020, and 058;
- record the 129-row k=3 replacement evidence, the 87-row accepted core, the 42-row exact-boundary adjudication, and the current 82-row active-`mechanism` execution baseline;
- retire `mechanism` as a registered identifier rather than retain it as a broad alias;
- adopt the `explained-by` and `operates-through` assertions, follow/skip decisions, revision consequences, and boundary tests above;
- state that a process-shaped target does not force `operates-through`: literal source use, not target ontology, is decisive;
- record the exact 82-row disposition table above and the no-reciprocal-authoring rule;
- scope ADR 009's five labels as the original theoretical-profile seed rather than a global closed vocabulary under ADR 019's collection-owned architecture;
- name the operativity path: collection authors consult the catalogue, `cp-skill-write` and `cp-skill-connect` load `kb/notes/COLLECTION.md` with binding force, and current footer examples teach the same semantics;
- reject a rename-only migration to either successor, retention of `mechanism` as a synonym, target-role or ontology signatures, and weak `see-also` preservation.

The ADR is created only in the implementation commit, after the corpus and authoritative surfaces match it. Its status must not become `accepted` while it describes unimplemented behavior.

### Proposed durable surface edits

Apply these together with the 82-row corpus migration:

1. `kb/reference/link-vocabulary.md`
   - replace the current `mechanism` catalogue row with `explained-by` and `operates-through` entries carrying the registered semantics above;
   - add ADR 061 to the decision links;
   - leave historical discussion of `mechanism` in ADR 020 intact.
2. `kb/notes/COLLECTION.md`
   - replace the notes→notes `mechanism` authorization with separate `explained-by` and `operates-through` rows and their reader needs;
   - leave `grounds` unchanged until phase B.
3. `kb/work/COLLECTION.md`
   - replace `mechanism` in the loose theoretical-label suggestions with `explained-by` and `operates-through` so new workshops do not teach the retired identifier.
4. `kb/reference/text-contract-profiles.md`
   - replace `mechanism` in the theoretical profile's inference-label list with the two successors.
5. `kb/reference/adr/009-link-relationship-semantics.md`
   - add an explicit scope note naming it as the initial theoretical seed and pointing to ADR 019 plus ADR 061 for current ownership and successor semantics; preserve its historical decision text.
6. `kb/reference/adr/020-theoretical-default-contrasts-mechanism.md`
   - add ADR 061 to `Amended by`; preserve the historical evidence and decision.
7. `kb/reference/adr/058-directional-identifiers-use-source-as-subject.md`
   - add ADR 061 to `Amended by` as resolution of the `mechanism` debt.
8. `kb/reference/README.md`
   - add ADR 061 to decision-history navigation and describe ADR 020 as the historical origin of the now-split relation.

No source contract, reference contract, instruction, schema, validator, or code change is required in phase A.

### Phase A execution and reconciliation

1. Re-scan the active surface immediately before editing. Require exactly 82 `mechanism` tuples and compare `(current label, source, resolved target)` against the manifest. Stop for additions, removals, or target movement; line-number movement alone is refreshed after identity checks.
2. Stage the ADR and authoritative-surface edits in the same working change as the corpus migration.
3. Apply only manifest rows whose `current_label` is `mechanism`: relabel 81 exact rows and delete the complete footer row for the one removal. Preserve targets and context phrases for every relabel.
4. Independently reconcile:
   - baseline tuples = 82;
   - exact successors = 81;
   - removals = 1;
   - active registered `mechanism` = 0;
   - active `grounds` remains exactly the fresh pre-edit count;
   - every resulting source→destination pairing is authorized;
   - historical ADR/workshop evidence remains historical rather than being lexically rewritten.
5. Validate every changed KB artifact, run `git diff --check`, inspect the complete diff, and write the phase retrospective before committing.

## Phase B — `grounds` migration, one dependency outstanding

The current 292-row `grounds` surface is otherwise fully classified:

| successor/action | active `grounds` rows |
|---|---:|
| `premised-on` | 168 |
| `explained-by` | 34 |
| `extends` | 31 |
| `exemplifies` | 15 |
| `defined-in` | 13 |
| `evidenced-by` | 10 |
| `is-evidence-for` | 10 |
| `operates-through` | 5 |
| `contrasts` | 1 |
| remove | 4 |
| `prerequisite-hold` | 1 |
| **total** | **292** |

`F094` is the only blocker:

`kb/notes/an-outcome-check-licenses-replay-a-rule-needs-the-process-verified.md:40 → kb/notes/diagnostic-richness-constrains-outer-loop-learning-quality.md`

Two of three exact classifiers found a prerequisite relation; one found `explained-by`. The accepted `prerequisite-hold` says the target must be available or true before the source works, but deliberately withholds a spelling until `enables` and `precondition` are reviewed together. Carrying `grounds` as a one-row legacy authorization would keep the retired ambiguity authorable; inventing a temporary label would create unreviewed vocabulary. Both are worse than resolving the family first.

After that review, phase B should receive its own final rebaseline, ADR, and approval. Its already-settled durable changes are:

- replace `grounds` with `premised-on` in the shared catalogue, notes contract, workshop suggestions, and theoretical text-contract profile;
- add notes→notes `is-evidence-for` to `kb/notes/COLLECTION.md` for the three demonstrated evidence-note rows;
- amend ADRs 009, 020, 058, and 060 with the final premise and prerequisite outcomes;
- migrate every fresh `grounds` tuple by the refreshed manifest, including the four accepted removals and no notes→notes `see-also` edges.

## Maintainer gate

Recommended next authorization:

1. approve phase A exactly as scoped above; and
2. authorize the read-only `enables` / `precondition` family review needed to replace `F094`'s hold before a separate phase-B approval.

Neither authorization permits phase-B corpus mutation. Any phase-A corpus edit still starts with a fresh tuple rebaseline and stops on drift.
