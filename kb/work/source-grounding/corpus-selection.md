# Wider source-corpus selection

Date: 2026-08-26

This is the dated disposition of the source-blind reading assignments in the
[literature claim inventory](../literature-disposition/claim-inventory.md). It
selects sources against claims that remain in the live notes, not against the
opening information-seeking reading list. Selection is decided for the
2026-08-26 cohort: every accepted source has an ingest with exact retained
quotes, and every considered source not selected now has a deferral reason.
Target-side repair and grounding checks are downstream work. They reopen source
selection only if comparison with a target exposes a support gap.

## Baseline already complete

| Source | Local claim | Decision | Transfer boundary | Downstream state |
|---|---|---|---|---|
| Pirolli, proximal information scent and distal content | Proximal cues can guide a choice among distal information sources | Accepted and ingested at [Pirolli](../../sources/pirolli-proximal-information-scent-distal-content.ingest.md) | Human Web-navigation structure transfers; the target owns the LLM cue, token, and tool-call account | `agents-navigate-by-deciding-what-to-read-next` was repaired and kept on 2026-08-26 |

## Batch 1: activation

The two sources are jointly necessary for the live note's historical analogy.
Tulving and Pearlstone isolate storage from retrieval. Gick and Holyoak reach
task use after a relevance hint. Neither establishes the LLM mechanism, and the
second experiment does not distinguish retrieval from post-retrieval salience.

| Source | Exact local claim adjudicated | Authority | Decision and evidence state | Downstream artifact |
|---|---|---|---|---|
| Tulving and Pearlstone, *Availability Versus Accessibility of Information in Memory* (1966) | Category cues recover information that was available in memory but not accessible in uncued immediate recall | Original controlled experiment | Accepted; [ingest](../../sources/tulving-pearlstone-availability-versus-accessibility.ingest.md) now retains the exact abstract passage needed by the target | [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md), storage-to-retrieval paragraph |
| Gick and Holyoak, *Analogical Problem Solving* (1980) | In Experiment IV, a relevance hint sharply changed analogical solution use despite no significant group difference in gist recall | Original experimental report | Accepted; [ingest](../../sources/gick-holyoak-analogical-problem-solving.ingest.md) now retains the hint manipulation, solution counts, and recall comparison | Same target, retrieval/context-to-use paragraph |

The target states the transfer boundary explicitly: these are human antecedents,
not direct evidence about LLM activation. Both ingests and the target pass
deterministic validation. The target-side `semantic/grounding-alignment` assay
remains the landing gate for the edited bytes.

## Batch 2: navigation and pointer surrogates

| Source | Exact local claim adjudicated | Authority | Decision and evidence state | Transfer boundary and downstream artifact |
|---|---|---|---|---|
| Teevan, Alvarado, Ackerman, and Karger, *The Perfect Search Engine Is Not Enough* (2004) | Human known-item seeking can proceed by contextual local steps rather than direct keyword jumps | Original CHI diary study | Accepted; the [ingest](../../sources/teevan-perfect-search-engine-orienteering.ingest.md) retains the abstract's observed local-step/direct-jump contrast | Human file/email/Web behavior bears on [link-following and search impose different metadata requirements](../../notes/link-following-and-search-impose-different-metadata-requirements.md); that note must own the transfer to LLM-agent KB navigation and its metadata prescription |
| Tombros and Sanderson, *Advantages of Query Biased Summaries in Information Retrieval* (1998) | A query-specific document surrogate can improve relevance judgment relative to a static title-plus-leading-sentences baseline | Original SIGIR evaluation comparing the two surrogate conditions | Accepted; the [ingest](../../sources/tombros-sanderson-query-biased-summaries.ingest.md) retains the experimental contrast, relevance-judgment result, and same-length appendix result | Human relevance judgments do not establish LLM context cost or the complete fixed/query-time/crafted taxonomy. The same-length rerun supports the accuracy contrast while limiting a speed claim. The source bears on the query-specific branch in [pointer design tradeoffs](../../notes/pointer-design-tradeoffs-in-progressive-disclosure.md) |

Teevan is preferred over Marchionini for the first claim because it directly
observes the local-step/direct-jump contrast assigned by the inventory.
Marchionini remains a broader synthesis candidate only if the live claim later
needs a browse-versus-analytic-search taxonomy that Teevan does not supply.

## Batch 3: the MOC inheritance claim

| Source | Exact local claim adjudicated | Authority | Decision and evidence state | Transfer boundary and downstream artifact |
|---|---|---|---|---|
| Niklas Luhmann Archive, *Schlagwortregister* | Luhmann's own keyword registers made no claim to complete term locations and named only relevant entry points into the collection | Institutional archive maintained from Luhmann's estate and research project | Accepted; the user supplied the rendered JavaScript page for a manual snapshot, and the [ingest](../../sources/luhmann-archive-schlagwortregister.ingest.md) retains the Archive's exact German sentence | Supports a Luhmann-specific non-exhaustive-register statement in [an enforced tag-README is a MOC with a machine-checked contract](../../notes/an-enforced-tag-readme-is-a-moc-with-a-machine-checked-contract.md). It does not show that the registers were MOCs or establish claims about other practitioners, readers, or maintainers |
| Nick Milo, *MOCs (defn)* | Milo defines an MOC as a cluster that maps things in context, helps gather, develop, and navigate ideas, and can take the form of a note whose links are clustered into groups | First-party articulation by the practitioner whose terminology the note invokes | Accepted; the [ingest](../../sources/nick-milo-mocs-definition.ingest.md) retains the definition, index comparison, and grouped-link example | Supports the bounded LYT/MOC description. It does not establish that MOCs are annotated or selective by design, that tag-READMEs are exactly equivalent, or that no practitioner promises completeness |

The live MOC note must narrow or separately support its universal historical
negative. Two positive descriptions of practice cannot prove that nobody in
either tradition ever made a completeness promise.

## Candidates not selected for the current live claims

These are deferrals, not findings that the traditions are irrelevant. They are
not reading assignments for this workshop's current cohort unless the named
local claim returns or the accepted source proves insufficient.

| Candidate | Disposition | Reason |
|---|---|---|
| Marchionini, browse versus analytical search | Deferred | Broader than the live local-step/direct-jump claim; Teevan is the direct first source |
| Bates berrypicking and Belkin ASK | Deferred | The former brainstorming artifact was rebuilt as an explicit local end-to-end architecture synthesis; neither tradition is currently a load-bearing premise |
| Shneiderman's visual-information-seeking mantra | Deferred | The live resolution-switching note now presents a qualitative KB criterion, not an empirical measurement claim, and the visual-interface mantra is only adjacent |
| Ranganathan, Broughton, Hearst/Yee, Scatter/Gather, and adaptive hypermedia | Deferred | The source-blind inventory identified no exact surviving cohort claim for which one of these is the authoritative adjudicator |
| Skitka, Mosier, and Burdick; Parasuraman and Riley; materialized-view maintenance | Deferred | The stale-index note now states a conditional control-flow mechanism and explicitly disclaims prevalence; its maintenance account is analytic rather than an empirical automation-bias claim |
| DITA, docs-as-code, and single-source publishing | Deferred | The live note's contribution is the access-mode transfer and per-consumer materialization; single-source publishing is an analogy, not a premise needed to establish that transfer |
| Selinger, storage read amplification, and passage retrieval | Deferred | The addressability note now states a conditional matched-unit relation and grounds its two orderings in local measurements; it does not depend on a database cost model |

## Completed source work

The current cohort has seven accepted source cases: Pirolli; Tulving and
Pearlstone; Gick and Holyoak; Teevan et al.; Tombros and Sanderson; the Niklas
Luhmann Archive; and Nick Milo. Each has a tracked ingest and retained exact
quotes. The table above records why the remaining candidate traditions were
deferred rather than silently omitted.

## Downstream handoff

1. Run the pending target-side grounding assay for the activation note.
2. Add the bounded Teevan and Tombros evidence to the navigation targets, keep
   the human-to-LLM transfer local, and run their grounding assays.
3. Rewrite the MOC note as two source-bounded historical statements: Milo for
   the MOC definition and the Archive for Luhmann's non-exhaustive keyword
   registers. Do not identify the registers as MOCs or retain the unsupported
   universal negative about practitioner completeness promises.
4. Send the resulting artifact dispositions to the sibling workshop.

A target-side comparison can reopen the corpus if it finds a concrete support
gap. A famous source list is not residual work by itself.
