# Source-backed target dispositions: navigation, pointers, and MOCs

Date: 2026-08-26

The source-corpus handoff in commit `18c6adf1` supplied retained exact quotes
for Teevan, Tombros and Sanderson, the Niklas Luhmann Archive, and Nick Milo.
Commit `ae1ce1dd` applied those sources to three targets after separating the
source-side result from the Commonplace-side transfer or synthesis.
Link-following/search and pointer design have final dispositions below. The MOC
target repair is recorded as pending because a separately opened multistage
acceptance run still owns its final artifact judgment. The fifth disposition,
contextual activation, is recorded separately in
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

## Pending eighth artifact disposition — enforced tag-README

**Candidate disposition: Keep after a source-bounded historical rewrite. Target
repair executed 2026-08-26; final disposition pending multistage acceptance.**

| Test | Finding |
|---|---|
| Source overlap | Milo defines an MOC as a contextual map and gives a grouped-link note as one form. The Luhmann Archive says Luhmann's own keyword registers made no completeness claim and named relevant entry points. Neither source says the registers were MOCs, that all MOCs are selective or annotated, or that no practitioner promises completeness. |
| Commonplace remainder | The [note](../../notes/an-enforced-tag-readme-is-a-moc-with-a-machine-checked-contract.md) maps Milo's positive grouped-link pattern onto a tag-README, then explains the local machine-checked delta: a useful stopping rule and a recomputable membership check are jointly necessary, while editorial orientation remains outside the contract. |
| Recovery and shape | The two source routes cannot replace the note because neither describes Commonplace's marks or derives their consumer-facing role. The local type spec supplies the implementation witness, but not the historical comparison or the map-plus-contract synthesis. |
| Graph role | Five tracked library artifacts link to the note, including the tag-README type contract, one supporting methodology note, one proposal, and the two source ingests. The type contract uses the note as rationale for the inherited-map-plus-enforcement distinction. |
| Execution | Commit `ae1ce1dd` removed the unsupported universal negative and the causal story about what all human readers and maintainers needed or could afford. It kept only the two bounded historical statements, added the direct ingest routes, and restated the machine-checked delta locally. Deterministic validation and the targeted grounding assay both passed. The active run at `kb/work/multistage/multistage-write-enforced-tag-readme-moc-20260826/` must still reconstruct, audit, accept, and either promote or revise this candidate before the workshop counts it as final. |

The two final dispositions are keeps, and the pending MOC judgment currently
points the same way, but the source relation differs in each case: human
navigation supplies a transfer premise, a human IR experiment grounds one
branch of a local taxonomy, and two practitioner-history sources bound an
old-plus-new synthesis. This diversity is evidence for claim-level comparison.
It is not yet a general keep rule, and the pending case is not counted as one.
