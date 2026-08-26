# Source-backed target dispositions: navigation, pointers, and MOCs

Date: 2026-08-26

The source-corpus handoff in commit `18c6adf1` supplied retained exact quotes
for Teevan, Tombros and Sanderson, the Niklas Luhmann Archive, and Nick Milo.
Commit `ae1ce1dd` applied those sources to three targets after separating the
source-side result from the Commonplace-side transfer or synthesis. All three
targets now have final dispositions below. The fifth disposition, contextual
activation, is recorded separately in
[activation-disposition.md](./activation-disposition.md).

## Sixth dated artifact disposition — link-following and search

**Disposition: Keep as an agent-KB metadata transfer. Decided and executed
2026-08-26.**

| Test | Finding |
|---|---|
| Source overlap | Teevan and colleagues observed human searchers reaching known targets through contextual local steps rather than direct keyword jumps. The study also reports that stepping reduced how much of the need participants had to specify and supplied context for understanding results. It does not establish an exhaustive two-mode taxonomy, LLM-agent behavior, or metadata requirements for an agent KB. |
| Commonplace remainder | The [note](../../notes/link-following-and-search-impose-different-metadata-requirements.md) transfers the structural contrast to an agent's decision context: a followed link arrives inside a source argument, while a corpus-wide result has task or query context but no surrounding source argument. It derives distinct metadata needs and explains why an index combines both conditions. |
| Recovery and shape | A direct source route would lose the human-to-agent transfer and every local metadata consequence. Merging into the more general navigation-decision note would make that premise carry a separate mode-specific design argument. The current note remains one citable transfer. |
| Graph role | Nine tracked library artifacts link to the note. Six are note or reference consumers using the mode distinction for shipped navigation, titles, resolution switching, and search design; three source ingests connect bounded evidence or comparison cases. The path and title remain accurate, so no rewiring is needed. |
| Execution | Commit `ae1ce1dd` added the Teevan route, changed the opening from an exhaustive taxonomy to two recurring modes, and stated the transfer boundary. Deterministic validation passed and the targeted `semantic/grounding-alignment` pair is fresh with outcome `pass` in the `codex` partition. |

## Seventh dated artifact disposition — pointer design

**Disposition: Keep after grounding one branch and repairing the worked
comparison. Decided and executed 2026-08-26.**

| Test | Finding |
|---|---|
| Source overlap | Tombros and Sanderson found that query-biased summaries improved human relevance judgments against a static title-plus-leading-lines baseline. Their same-length follow-up attributes the difference to query bias rather than displayed-text amount. The experiment does not establish LLM-agent performance, production cost, or the note's fixed/query-time/crafted taxonomy. |
| Commonplace remainder | The [note](../../notes/pointer-design-tradeoffs-in-progressive-disclosure.md) compares pointers across specificity, cost, availability, and accuracy; identifies crafted link phrases as a separate authoring-time form; and shows how one architecture can mix fixed and query-time forms. Those relations are not conclusions of the human experiment. |
| Recovery and shape | A source pointer would cover only the query-time branch. Splitting that branch would leave the four-axis comparison and mixed-architecture conclusion without their contrast case. The note remains the smallest existing unit that lets a consumer compare the three pointer forms together. |
| Graph role | Ten tracked library artifacts link to the note. Six note, reference, review, or type consumers use the tier or trade-off model; four source ingests connect evidence and adjacent cases. The path and title remain accurate. |
| Execution | The first grounding run caught an older contradiction: the note denied OpenViking query-time pointers while defining scores and rerankers as such. It also found unsupported token estimates and relation-field details. Commit `ae1ce1dd` removed those claims, replaced them with the supported fixed-plus-query-time example, narrowed two footer annotations, and added the Tombros route. Deterministic validation passed; the final targeted grounding pair is fresh with outcome `pass` in the `codex` partition. |

## Eighth dated artifact disposition — enforced tag-README

**Disposition: Keep after a source-bounded multistage rewrite. Decided and
executed 2026-08-26.**

| Test | Finding |
|---|---|
| Source overlap | Milo defines an MOC as a contextual map and gives a grouped-link note as one form. The Luhmann Archive says Luhmann's own keyword registers made no completeness claim and named relevant entry points. Neither source says the registers were MOCs, that all MOCs are selective or annotated, or that no practitioner promises completeness. |
| Commonplace remainder | The [note](../../notes/an-enforced-tag-readme-is-a-moc-with-a-machine-checked-contract.md) applies Milo's contextual-map pattern to a tag-README, then states the exact local delta: `complete` and `covered_by` are validator-rederived membership predicates whose success authorizes bounded stopping shortcuts. Grouping, priorities, context phrases, reading order, and map quality remain editorial. |
| Recovery and shape | The two source routes cannot replace the note because neither describes Commonplace's marks or relates them to the inherited mapping function. The local type spec owns the mark semantics, but it does not supply the historical comparison or the bounded map-plus-checked-membership composition. The accepted note keeps that one composition while citing its independent premises. |
| Graph role | Five tracked library artifacts link to the note: the tag-README type contract, one supporting methodology note, one proposal, and the two source ingests. The count estimates rewiring cost; the type contract's use of the note as PKM grounding shows why neither source ingest is a substitute. The fixed path remains accurate, so no rewiring is needed. |
| Execution | Commit `ae1ce1dd` first removed the unsupported universal negative and added the two direct source routes. The multistage run then independently reconstructed the claim, omitted the unsupported adoption-history, universal MOC, broad human–LLM, model-economics, and general-transfer branches, and promoted a smaller one-claim artifact in `37de2baf`. The target and both ingests validate cleanly. Review job `8462` finalized the targeted `semantic/grounding-alignment` pair with outcome `pass`; the pair is fresh in the `codex` partition. |

All three final dispositions are keeps, but the source relation differs in each
case: human
navigation supplies a transfer premise, a human IR experiment grounds one
branch of a local taxonomy, and two practitioner-history sources bound an
old-plus-new synthesis. This diversity is evidence for claim-level comparison.
It is not yet a general keep rule.
