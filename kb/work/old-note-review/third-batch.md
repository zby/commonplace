# Third batch: five historical paths, six current destinations

Applied the [triage prompt](./triage-prompt.md) at `0fe7d4a9e`. One note split, one index was absorbed into another, and none of the six destinations was counted in the first two batches. Verdicts record recommendations; execution is noted separately below. Historical source reviews, trial packets and workshop records are not live endorsements and are not proposed for narrative edits. Inventory rows are given together at the end.

### `kb/notes/backlinks.md` → `kb/theory/inbound-and-outbound-links-serve-asymmetric-reader-needs.md`

- **Lineage:** `ffc7c00fa` split the theory from the delivery proposal; `9c7563bf7` moved the theory to its [current address](../../theory/inbound-and-outbound-links-serve-asymmetric-reader-needs.md).
- **Verdict:** `targeted-update` (high).
- **Execution:** Revised the theory note in place after operator approval. It now tells readers to inspect citing passages for reliance, evidence and impact; the delivery example distinguishes whole-file loading from selective access. A checklist/policy example distinguishes the authored citation from the clickable return link on the displayed page.
- **KB role & goal fit:** Before changing a claim, a maintainer needs to find what readers are being sent there to learn. The target’s own outbound links cannot enumerate later uses; inverting the authored links can. That is a design argument, not a feature request.
- **Relevance to current gaps:** Direct input to valuing notes and safely removing accumulated material. Citations show where to investigate, not what deserves retention.
- **Evidence & reasoning:** The grounding bullet says incoming links show *how well-grounded* the claim is. Several sources can mention the same unsupported idea. Likewise a note labeled as an example is not automatically safe from a change in scope. The [access-cost comparison](../../theory/design-for-the-first-time-human-except-on-access-cost.md) also makes the cost depend on the interface: an agent can query for a slice rather than reading every byte.
- **Keep / cut:** Keep inversion, optional reciprocal links and the read-time versus batch distinction. Narrow “only” in the four-needs heading and replace the grounding and impact verdicts with questions to check in the citing passages. Scope the linear-read claim to whole-file loading.
- **Live dependents affected:** ADR 020 and *Links encode conditional possibilities* need the inverse-view argument, which survives. The Links tag head and *Backlink surfacing* use the four needs; preserve those needs without treating citation counts or labels as warrants. No ADR reversal or proposal redesign required.
- **Not checked:** Whether displaying inbound links changes readers’ judgments or saves time.

### `kb/notes/backlinks.md` → `kb/reference/proposals/backlink-surfacing.md`

- **Execution:** Clarified the proposed web display and which links the builder would index. Refreshed the baseline on 2026-11-28: filename search finds candidates, review resolves citing passages, and only the proposed site feature would display the return links. Scoped the ADR 025 precedent to complete generated indexes. No feature was implemented.
- **Lineage:** The second file created by `ffc7c00fa` is still the [proposal](../../reference/proposals/backlink-surfacing.md); `c11699844` clarified reciprocal links. Same historical inventory row, different judgment.
- **Verdict:** `targeted-update` (normal).
- **KB role & goal fit:** Gives a site maintainer a choice between rendering incoming citations beside a page and looking them up when needed. An unadopted interface belongs in proposals, not Theory.
- **Relevance to current gaps:** Supports impact inspection; does not itself solve assessment of note value.
- **Evidence & reasoning:** The theory sibling establishes why the inverse is useful, not that a web panel or new CLI is warranted. The dated current-state section is not a current baseline: `src/commonplace/lib/review_workflows/inbound.py` already collects inbound passages automatically for review workflows. That is not a reader-facing backlink browser.
- **Keep / cut:** Keep the June date or refresh the baseline explicitly; distinguish review-time collection, interactive repo search and proposed web rendering. Replace the blanket “nothing generated is committed” with ADR 025’s narrower rule for complete generated indexes. Keep a new command contingent on an observed need.
- **Live dependents affected:** The Links tag head and the theory sibling point here for *options*, not shipped behavior. No premise repair.
- **Not checked:** Rendered-site behavior, demand for the feature, or latency. No implementation recommended by this pass.

### `kb/notes/bitter-lesson-boundary.md` → `kb/theory/exact-implementation-does-not-validate-a-requirement.md`

- **Lineage:** `76b94b045` deleted the old file, added `fixed-artifacts-split-into-exact-specs-and-proxy-theories.md` and retargeted the arithmetic/vision comparison in its citers. `1506fead5` rewrote the successor; `ffb243552` renamed it; `9c7563bf7` moved it to [Theory](../../theory/exact-implementation-does-not-validate-a-requirement.md). The similarly titled Bitter Lesson notes are neighbors, not the historical successor.
- **Verdict:** `keep-unchanged` (high).
- **KB role & goal fit:** Helps a maintainer decide whether to fix a failing implementation or reconsider what a passing check was supposed to establish. A validator can enforce the required headings without establishing that those headings improve the argument.
- **Relevance to current gaps:** Debugging credit assignment and deciding when to revise an acceptance criterion. Local success and whole-system benefit need different evidence.
- **Evidence & reasoning:** The current note already assigns exactness to a particular implementation–requirement relation, not to an entire artifact. It also names interface errors and resource limits as rival explanations for failure when components are combined. [The proximate-target note](../../theory/a-proximate-target-is-checked-for-achievement-not-for-warrant.md) extends the question to choosing targets; it does not replace the artifact-level diagnosis.
- **Keep / cut:** Keep the current note and its title. No new source synthesis needed to establish the logical distinction.
- **Live dependents affected:** No change required by this verdict, but some citations still import the *previous* claim. Prioritize *Oracle strength spectrum*, *Operational signals that a component is a relaxing candidate*, *Spec mining as codification*, *The boundary of automation is the boundary of verification*, and *Theory and methodology form a two-layer execution system*: do not divide artifacts into two kinds or equate checkability with objective fit. *A proximate target is checked for achievement* should not present composition failure alone as diagnostic. The current Bitter Lesson comparison, codification definition and code/LLM decision heuristics already distinguish the relations in their body text.
- **Not checked:** Did not reproduce the vision history or benchmark results. Those examples do not supply the logical warrant for the claim.

### `kb/notes/claim-notes-should-use-toulmin-derived-sections-for-structured-argument.md` → `kb/theory/claim-notes-should-use-toulmin-derived-sections-for-structured.md`

- **Lineage:** `2566f6964` shortened the filename; `9c7563bf7` relocated it; `f698aa90d` updated contract references, not the [argument](../../theory/an-assumption-worth-disputing-is-worth-stating.md).
- **Verdict:** `rebuild-in-place` (high).
- **Execution:** Rewritten in place as *An assumption worth disputing is worth stating*. A checklist example shows when a writer should state an assumption or narrow the conclusion. The note uses ordinary prose and points to the type contract for cases where separate sections help; it retains the readability observation. Filename relocation and dependent citation repairs have not been carried out.
- **KB role & goal fit:** A reviewer needs to distinguish “the observation is wrong” from “the observation is right but does not support this claim.” That distinction remains useful outside Commonplace. Choosing a document type is a separate, already documented decision.
- **Relevance to current gaps:** Faithful local judgment: the first criticism calls for checking the evidence; the second calls for testing the inference. Mandatory sections also impose the very prose cost the bloat question asks us to justify.
- **Evidence & reasoning:** The pinned [Purdue source](../../sources/purdue-owl-toulmin-argument.ingest.md) distinguishes grounds from the warrant connecting them to a claim (snapshot lines 17–19; hash matches the ingest). It does not prescribe Markdown headings or establish better outcomes from them. The [type contract](../../theory/types/structured-claim.md) already owns Evidence, Reasoning and optional Caveats; the note itself reports demotions when the scaffold harmed flow.
- **Keep / cut:** Keep the two review questions and the readability counterexample, not a universal section prescription. Cut the duplicated template, migration counts and naming history. A title such as *Evidence can be correct without warranting the claim* would need a matching filename: use `commonplace-relocate-note` in a separate commit if approved.
- **Live dependents affected:** Route the Type System tag and *Wikiwiki principle* to the contract for section requirements. *Linking theory* and *Human writing structures transfer* need the grounds/warrant distinction, not proof that sectioning improves LLM output. *Learning is not only about generality* uses the local adoption decision; retain a historical reference for that. *Skills derive from methodology* claims the connect test came from Toulmin: verify that lineage or present it as a comparison. *Two rewrites exposed a syntax or repetition tradeoff* relies on the demotion observation; preserve it as an observation, not a frequency estimate.
- **Not checked:** Independent historical convergence of three traditions, the lineage of the connect test, and comparative review outcomes.

### `kb/notes/claw-design.md` → `kb/tags/README.md` (merged navigation)

- **Lineage:** `682b8d575` → `kb-design.md`; `fd0b8fb01` → `kb-design-index.md`. `2cc208c7d` deleted the nearly all-inclusive tag but moved curated sections to `tags-index.md`. `9976a0811` renamed that index; `96b9b2664` moved it to [Tags](../../tags/README.md). Not a retired theory note; not every old entry survives.
- **Verdict:** `targeted-update` (low), on the landing only.
- **KB role & goal fit:** A reader chooses a topic before choosing a note. The former KB-design tag could scarcely narrow the search; the current landing routes to narrower heads and standing questions. That is navigation, not an explanatory claim.
- **Relevance to current gaps:** Makes the standing questions discoverable; does not answer them.
- **Evidence & reasoning:** `2cc208c7d` records the original tag covering about 50 of 70 notes. The current [collection contract](../../tags/COLLECTION.md) distinguishes curated heads from complete generated membership lists. One link calls Theory Builder “an earlier definition, due for rewriting,” whereas [its head](../../tags/theory-builder-README.md) now states which systems and claims it covers. The maintenance remark does not tell a reader when to follow the link.
- **Keep / cut:** Keep the landing and its existing address. Replace just the Theory Builder gloss with its inclusion criterion; do not recreate the catch-all tag.
- **Live dependents affected:** None for this text-only fix. The library skill, index-maintenance instruction, Theory and Reference landings, and site/command docs rely on topic browsing, not that particular gloss. Preserve the route specified by ADR 089. Archived proposals are historical records.
- **Not checked:** No site build or navigation usability test; no claim that every entry from the historical index deserves reinstatement.

### `kb/notes/claw-learning-is-broader-than-retrieval.md` → `kb/theory/claw-learning-loops-must-improve-action-capacity-not-just-retrieval.md`

- **Lineage:** `d1d69393d` created the revised successor; `d75d9de1d` removed the leftover old path; `9c7563bf7` relocated the [successor](../../theory/claw-learning-loops-must-improve-action-capacity-not-just-retrieval.md). `b8a0db382` refreshed its system comparisons, and `ca891bfa1` retargeted its learning-loop link.
- **Verdict:** `keep-unchanged` (high).
- **KB role & goal fit:** Helps someone evaluating an agent’s memory decide whether a failed task implicates retrieval, the retained advice, or something else such as permissions. Finding a procedure and acting on it are different events.
- **Relevance to current gaps:** Directly addresses credit assignment and whole-loop payoff. It identifies what a useful test must distinguish; it does not already supply a general causal test.
- **Evidence & reasoning:** The opening restricts the claim to agents that retain context for later tasks. The [behavioral study’s retained quotes](../../sources/llm-agents-are-not-always-faithful-self-evolvers.ingest.md) distinguish supplying condensed experience from sensitivity to changing its content. The [neighbor on discoverability and trust](../../theory/agent-memory-needs-discoverable-composable-trusted-knowledge-under.md) asks what makes an item usable, not whether changing it affected an action. The Personal Brain example is identified as one self-report, not proof of benefit.
- **Keep / cut:** Keep the distinction between access, uptake and outcome, including the warning against blaming the KB for every unsuccessful action. No new taxonomy or empirical claim needed.
- **Live dependents affected:** No change required. The Tags landing, *Agent memory needs discoverable…*, *Agent memory is a crosscutting concern*, *Brainstorming how to enrich web search* and *Quality signals for KB evaluation* use the action-versus-retrieval distinction. *Flat memory predicts specific cross-contamination failures* goes further: this note alone does not establish that a flat store caused a particular failure.
- **Not checked:** Did not rerun the interventions, Agent Workflow Memory or Voyager; no estimate of prevalence or effectiveness across deployed agents.

## Inventory updates

```tsv
historical_path	coverage	located_path_or_successor
kb/notes/backlinks.md	traced-and-triaged	kb/theory/inbound-and-outbound-links-serve-asymmetric-reader-needs.md;kb/reference/proposals/backlink-surfacing.md
kb/notes/bitter-lesson-boundary.md	traced-and-triaged	kb/theory/exact-implementation-does-not-validate-a-requirement.md
kb/notes/claim-notes-should-use-toulmin-derived-sections-for-structured-argument.md	traced-and-triaged	kb/theory/claim-notes-should-use-toulmin-derived-sections-for-structured.md
kb/notes/claw-design.md	traced-and-triaged	kb/tags/README.md
kb/notes/claw-learning-is-broader-than-retrieval.md	traced-and-triaged	kb/theory/claw-learning-loops-must-improve-action-capacity-not-just-retrieval.md
```
