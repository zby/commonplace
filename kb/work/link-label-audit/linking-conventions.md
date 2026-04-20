# Linking conventions — compressed section for embedding

> Staging ground. This file is the compressed vocabulary section that will be embedded inside `cp-skill-write/SKILL.md` (and potentially other link-authoring skills later). It is not a library doc and does not land under `kb/instructions/`. The ADRs (009, 018) and `linking-theory.md` remain the canonical source; this is the operational distillation.
>
> Target: ~700 tokens. Cut prose elaboration; keep tables and tests. Re-sync this file whenever ADR 009 or ADR 018 changes.

---

Every typed link uses one of seven canonical labels. Labels appear inline as prose connectors (`since [title](./path.md)`, `because [title](./path.md)`, `but [title](./path.md)`) or as footer annotations (`- [title](./path.md) — label: context phrase`). "Related" is not a relationship; if you can't name one, the link may not be worth making.

Per-KB edge rules live in each `COLLECTION.md` outbound table. See ADR 009 and ADR 018 for the vocabulary's decision history and theory.

## Seven labels

**Asymmetric — forward-authored, backward-derived.** Target is upstream (more fundamental or general); don't write a reverse edge. One target typically has many incoming links; the backlinks view is auto-computed.

| label | semantics | alias | test |
|---|---|---|---|
| `extends` | source builds on target; adds a dimension, refines | — | does source treat target as a premise it develops? |
| `grounds` | target is source's theoretical or evidential base | `foundation` | would a reader follow it to *verify* the claim? |
| `enables` | target is source's operational prerequisite | — | would source fail if target weren't true? |
| `exemplifies` | source is a concrete instance of target | `example` | is source a specific case of target's general? |
| `mechanism` | target is the operational engine for source's claim | — | would a reader follow it to understand *how* it works? |

**Symmetric — self-dual, either end may author.** Peer-level relationships; both ends may mark them but don't duplicate.

| label | semantics | test |
|---|---|---|
| `contradicts` | A conflicts with B; one is wrong or scope must narrow | follow to *resolve a disagreement* |
| `contrasts` | A and B differ on a named axis; neither is wrong | follow to *understand the neighbour's shape* |

## Boundary tests

- **`contrasts` vs `contradicts`.** Does the reader arrive expecting to resolve conflict (`contradicts`) or see parallel design (`contrasts`)?
- **`mechanism` vs `grounds`.** Epistemic question → `grounds`. Operational question → `mechanism`.
- **`grounds` vs `enables`.** Evidential base → `grounds`. Operational prerequisite → `enables`.

## Directional rule

Don't write a reverse-edge backlink for any asymmetric label. If `A — mechanism: B`, the backlinks view makes the inverse visible on B; writing both doubles maintenance and misleads scanners.

*Selective curation allowed.* An upstream note may link down to pin a canonical example or index a class of applications — editorial choice, not duty.

For symmetric labels, either end may author; don't duplicate the same pair.

## Drift redirects

| if drifting toward | use |
|---|---|
| `sharpens`, `refines`, `clarifies` | `extends` |
| `motivates`, `rationale`, `justification` | `grounds` |
| `applies`, `instance`, `application` | `exemplifies` |
| `complements`, `consequence`, `sibling` | `extends`, or no label |
| `tension`, `challenges` | `contradicts` |

If none of the seven fits, prefer prose without a label over inventing one. New labels require an ADR.

## Articulation test

Every typed link must complete: **"[source] connects to [target] because [specific reason]."** Reject merely "related", keyword-matched, or too-obvious links.

## Position and strength

- **Inline prose** — `since / because / but [title](./path.md)`. Strongest commitment; the target's claim is a premise of the source's argument. Connector implies the label.
- **Footer annotation** — `- [title](./path.md) — label: context phrase`. Requires explicit label and a context phrase that passes the articulation test.
