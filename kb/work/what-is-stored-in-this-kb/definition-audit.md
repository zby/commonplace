# Initial audit of `kb/notes/definitions/`

This audit asks whether each definition supplies vocabulary required by transferable theories or instead specifies Commonplace machinery. It is a first disposition, not authorization to move or retire anything.

Direct-backlink counts are included only as migration-cost evidence. High use does not make a term theoretical, and low use does not make it wrong.

## Disposition test

- **Theory vocabulary:** theories need a stable distinction whose applicability can be contested across possible systems.
- **Machinery vocabulary:** the term is true or binding because Commonplace chose, implemented, or stipulated a system boundary, contract, workflow, or catalogue.
- **Mixed:** independent propositions have different homes and should be split or folded separately.
- **Retire candidate:** ordinary wording or an existing concept can do the work without a separate canonical term.

A definition can describe machinery and remain theoretical. `behavioral authority`, for example, is a general way to analyse consumers, channels, and force across systems. Conversely, `text contract` is machinery vocabulary because its canonical meaning is constituted by Commonplace's chosen `COLLECTION.md` architecture.

## Strong theory-vocabulary candidates

| Definition | Inbound files | Initial disposition |
|---|---:|---|
| [Behavior-determining organization](../../notes/definitions/behavior-determining-organization.md) | 19 | Keep in theory. It supplies the cross-system object changed by self-improvement and excludes work products and environment changes. |
| [Behavioral authority](../../notes/definitions/behavioral-authority.md) | 71 | Keep in theory. Consumer, channel, and force are an analytical relation rather than a Commonplace configuration. |
| [Codification](../../notes/definitions/codification.md) | 114 | Keep in theory. It names the natural-language-to-symbolic crossing within the general constraining mechanism. |
| [Constraining](../../notes/definitions/constraining.md) | 129 | Keep in theory. Semantic narrowing is a transferable mechanism; Commonplace conventions are examples. |
| [Context engineering](../../notes/definitions/context-engineering.md) | 75 | Keep in theory. The bounded-context routing/loading/scoping/maintenance problem applies beyond this repository. |
| [Coordination value](../../notes/definitions/coordination-value.md) | 2 | Keep provisionally. Its claim about value created by shared commitment is theoretical despite low use; test whether an ordinary theory note would be a better shape. |
| [Evidence bearing on an improvement objective](../../notes/definitions/evidence-bearing-on-an-improvement-objective.md) | 7 | Keep in theory. It sharpens a causal condition in the cross-system self-improvement definition. |
| [Lineage](../../notes/definitions/lineage.md) | 37 | Keep in theory. Review-relevant source dependency is a general architectural field, narrower than full provenance. |
| [Operative change](../../notes/definitions/operative-change.md) | 20 | Keep in theory. Horizon-relative persistence plus an authority path is a general condition, not a local workflow state. |
| [Operative part](../../notes/definitions/operative-part.md) | 9 | Keep provisionally. The sub-artifact unit is useful to several analytical axes; test whether the term remains necessary after the content model settles. |
| [Reflective system](../../notes/definitions/reflective-system.md) | 68 | Keep in theory. It explicates inherited computational-reflection concepts and names Commonplace's declared departures. |
| [Representational form](../../notes/definitions/representational-form.md) | 72 | Keep in theory. The natural-language/symbolic/distributed-parametric carve is a contestable cross-system model. |
| [Retained artifact](../../notes/definitions/retained-artifact.md) | 17 | Keep provisionally. It names behavior-shaping persistence across substrates, but its boundary should be retested against archival and source artifacts. |
| [Self-improving system](../../notes/definitions/self-improving-system.md) | 43 | Keep in theory. It is an architecture-neutral, frame-indexed explication supported and tested across systems. |
| [Storage substrate](../../notes/definitions/storage-substrate.md) | 21 | Keep provisionally. It separates operational location from form, lineage, and authority across systems. |

## Theory candidates with a secondary shape or redundancy question

| Definition | Inbound files | Initial disposition |
|---|---:|---|
| [Actionable methodology](../../notes/definitions/actionable-methodology.md) | 9 | Keep the operator-relative relation in theory. Move the rule requiring every technical occurrence to link here into vocabulary machinery or instructions; that rule is not part of the theory. |
| [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) | 158 | The authority-family distinction is theoretical, but test whether this shorthand remains necessary now that behavioral authority owns the precise path. High use makes retirement expensive, not conceptually wrong. |
| [System-definition artifact](../../notes/definitions/system-definition-artifact.md) | 174 | Same as `knowledge artifact`: theoretical as a path-family shorthand, but potentially redundant after the path-relative reformulation. Do not mistake its machinery subject matter for machinery status. |
| [Reach-assessment](../../notes/definitions/reach-assessment.md) | 36 | Keep in theory, but reassess artifact shape. The file develops several causal, proof, and learned-world-model claims and may be an ordinary theory or synthesis rather than a cheap definition. |

## Machinery-first candidates

| Definition | Inbound files | Initial disposition |
|---|---:|---|
| [Answerability](../../notes/definitions/answerability.md) | 2 | Move, fold, or split. It explicitly calls itself a domain invariant that Commonplace stipulates for admission as knowledge. The general relation may support theory, but the current central force is a framework boundary and collection-contract obligation. |
| [Text contract](../../notes/definitions/text-contract.md) | 22 | Move to reference or retire as a standalone artifact. It names adopted collection machinery and repeats the reference profile catalogue, ADR history, and live collection contracts. See the [dedicated task](./tasks/text-contract-and-profiles.md). |

## Mixed and retirement candidates

| Definition | Inbound files | Initial disposition |
|---|---:|---|
| [Discovery lifecycle](../../notes/definitions/discovery-lifecycle.md) | 28 | Split or reframe. Peircean conjecture/consequence/test relations and the process/product distinction can support theory; the chosen six-phase evaluation, routing, acceptance, and integration sequence may be Commonplace methodology rather than a belief. |
| [Directed reading](../../notes/definitions/directed-reading.md) | 1 | Likely retire or move operational residue into instructions. It mostly names a task-contract pattern, has one external inbound file, and already records that ordinary reading-and-reshaping language may suffice. |

## Cross-cutting findings

1. `type: kb/types/definition.md` is structural and does not imply the theoretical profile. [The reference collection's `collection` definition](../../reference/definitions/collection.md) is the existing counterexample.
2. The blanket rule in `kb/notes/COLLECTION.md`—“Definitions of KB vocabulary belong under `kb/notes/definitions/`”—is too broad if vocabulary can name implemented machinery. Placement needs a contribution test.
3. The `AGENTS.md` vocabulary list is an always-loaded glossary for operating the repository. Membership there says a term is operationally important, not that its canonical artifact belongs in theory.
4. A definition's theoretical eligibility and its need for a standalone file are different questions. Several high-degree authority terms may be theoretically legitimate but redundant after the four-question classifier.
5. The current `kb/notes/README.md` still describes the definitions directory with the retired term “register” and links a missing `definitions/dir-index.md`. Navigation repair should follow, not precede, the dispositions.

## Next audit passes

- Test the strong theory candidates against external-system counterexamples and the “would this survive a different Commonplace design?” question.
- Inspect every material proposition in the mixed candidates instead of moving whole files by dominant theme.
- For machinery-first candidates, choose between a reference definition, folding into an existing reference surface, or retirement.
- Reassess the standalone value of `knowledge artifact`, `system-definition artifact`, `operative part`, `retained artifact`, and `storage substrate` after the content model settles.
- Only then revise collection contracts, backlinks, indexes, and the definition-type guidance.

