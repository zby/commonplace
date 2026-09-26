# Tag head review B (11 heads)

Read-only. Membership from `tag-members.txt`. "Unreached" means not reachable in one hop from the head's current links (direct link, or a member of any linked head), computed mechanically. Recency note: `git log -1` gives 2026-09-25/26 for every sampled member (the ADR 089/086 sweeps touched all files), so "most recent" could not be separated by date; I sampled across collections and clusters instead.

## foundations

1. Opening: weak. "Core theory that the rest of the KB builds on. These notes define the quality criteria, the design methodology, and the fundamental constraints that shape every other decision." This describes rank, not topic; no one searches for "foundations". The description leads with "contextual competence", which is not a registered term (it appears in only 7 notes).
2. Defining note: none exists, and none can: "foundational" is a status, not a concept. The closest thing to an anchor is `definitions/actionable-methodology.md`, which is foundations-only.
3. Boundary: none stated, and there is no `## Related Tags` section. The confusable tag is self-improving-systems (81 of 118 members shared). The head links it as a subsection without saying whether it is a child or a neighbour. methodology is a full subset and is not linked.
4. Fit: the 81 shared members are the self-improving/software-factory program (`definitions/software-house.md`, `definitions/software-factory.md`, `factory-learning-is-experience-responsive-retention-that-improves.md`, `backtracking-keeps-lightweight-search-control-provisional.md`). They were given this tag on purpose (for example commit f00d5359, 2026-09-02), but they fit self-improving-systems alone. `reference/source-adoption-policy.md` and `definitions/actionable-methodology.md` belong under methodology.
5. Staleness: it links 2 non-members (`agent-memory-needs-discoverable-composable-trusted-knowledge-under.md`, `reference/design-rationale-management.md`). The heading "## Notes" covers reference items. One pick has a blank line in front of it and no group. "Self-improving systems" is used as a section heading, not a tag relation.
6. Shape: 21 members are unreached. The only coherent residue outside self-improving-systems is a design-method cluster: `borrowed-patterns-transfer-only-over-shared-mechanism`, `problem-matches-guide-method-search…`, `first-principles-analysis-maps-design-space…`, `human-analogies-suggest-functions…`, `derivation-and-inheritance-give-starting-warrant…`, `a-framework-rule-with-a-boundary-preserving-rival…`, `a-universal-knowledge-framework-demotes…`, `source-adoption-policy`, and `alexander-patterns…`. The other residue is scattered: context-efficiency and soft-degradation (context-engineering), and fluid-resolution (links/navigation). With self-improving-systems holding 69% of the members, foundations works as a second name for that program plus a reading list.
7. Verdict: **retire** as a membership tag. Move the design-method residue into a topical tag (it could absorb methodology), and keep a hand-curated "start here" list on the `kb/tags/README.md` landing. Reason: the tag names a rank rather than a searchable subject, and its members are already covered by self-improving-systems.

## kb-maintenance

1. Opening: partly adequate. "How an agent-operated KB stays healthy as it grows. Detection, operations, and the dynamics that govern quality over time." It lacks the words members actually use: review, gate, grounding, freshness/staleness, validation, supersession/retirement, index/tag maintenance.
2. Defining note: none is named. The closest anchor is `maintenance-capacity-must-match-harmful-artifact-inflow.md`, which is listed first under Dynamics but not presented as the anchor.
3. Boundary: the nearest confusable tag, observability (8 of its 11 members are shared), is not named in this head. document-system and links are named.
4. Fit:
   - `reference/proposals/per-artifact-write-briefs.md` and `deterministic-write-context-assembly.md` are writing-context design, so context-engineering or document-system.
   - `notes/evidence/single-artifact-review-bundles-still-cut-claude-costs-substantially.md` is cost evidence, so evaluation.
   - `title-as-claim-makes-overlap-between-notes-visible.md` belongs under links or document-system.
   - `reference/proposals/model-partition-registry.md` and `review-configuration-object.md` are review-system configuration, so architecture.
5. Staleness:
   - "For how the KB is *built*, see [tags](./README.md)" and the Related entry "[tags] — parent area: architecture and design of the KB itself" are stale: `kb/tags/README.md` is now the tag landing, not a kb-design area.
   - The link text "traversal-improves-the-graph" does not match the note title ("Traversal improvements should be deferred via logging…").
   - It links non-member `an-accepted-edit-verifies-the-change-not-the-rule.md`.
6. Shape: 50 members, 32 unreached. The 19 reference proposals are almost entirely absent from the head (one is linked). Natural children:
   - review and gate machinery: calibrating-semantic-gates, gate-learning, structured-output-codec, criteria-edits-invalidate-verdicts, full-improvement-pass-closure
   - grounding: quotes-route rollout, Pirolli verdicts, five-link cap, linked-note-discharges-its-own-grounding, routine-bilateral-isolation
   - freshness/staleness: link-graph-plus-timestamps, collection-as-artifact-freshness, factored-dependency-pairs
   - retirement/supersession: superseded-choices, cheap-adoption-and-weak-retirement
   - indexes and tags: indexes-lower-recall, index-completeness, enforced-tag-readme, derived-copy, tag-maintenance proposal, keyword-tags proposal

   `complete: true` is not achievable at the current size without children.
7. Verdict: **split**. At minimum carve out review/grounding and index/tag-maintenance children, then rewrite the opening. Reason: the head covers only the older notes, and the reference proposals that make up most of the recent membership have no route.

## learning-theory

1. Opening: moderate. "How systems learn, verify, and improve. These notes define learning mechanisms, verification gradients, and memory architecture…" It lacks the words readers now use: continual learning (3 member titles), theory builder (appears only under Start here), self-improvement.
2. Defining note: split. The opening names deploy-time learning ("the unifying framework") and Simon via `learning-is-not-only-about-generality.md`, but Start here puts `definitions/theory-builder.md` first. The head does not say which is the anchor.
3. Boundary: the confusable tags, self-improving-systems (47 shared members) and deploy-time-learning, are routed as children. No sentence says what separates plain learning-theory from them.
4. Fit: `warranted-reader-update-is-the-objective-of-substantive-writing.md` is writing theory (context-engineering/discovery). `commitment-not-derivation-creates-new-ground-truth.md` fits constraining/kb-maintenance better. The other sampled members fit.
5. Staleness:
   - "These notes" is inaccurate: members include agent-memory-systems.
   - "[tags](./README.md) — the hub; applies learning theory to KB architecture and evaluation" is stale (the landing is not a kb-design hub).
   - The self-improving-systems child phrase "theory builders and their warrant: systems that revise their own theories" narrows that tag: the self-improving-systems head defines it as operative, evidence-responsive change, which includes gradient learners.
   - `kb/tags/README.md` says "covered by six child tags"; the head links seven.
6. Shape: `complete: true` holds (0 unreached) through 7 child heads plus 4 direct entries. Leave the shape as it is.
7. Verdict: **rewrite opening**. Reason: the completeness structure is sound, but the opening uses older anchors and lacks "continual learning" and "theory builder".

## links

1. Opening: weak. "Links are the edges of the knowledge graph. Every link is a decision point for the reader…" This is a claim, not a statement of what the tag gathers. Missing words: link labels, backlinks, navigation, lineage, pointers.
2. Defining note: `linking-theory.md` exists but sits near the bottom under "## Theory". The current shipped approach, `kb/reference/link-vocabulary.md` (collection-owned rules, reader-need labels), is neither tagged links nor linked.
3. Boundary: none stated. The confusable tags are context-engineering (navigation, progressive disclosure) and kb-maintenance (lineage/staleness).
4. Fit: `a-linked-note-discharges-its-own-grounding-so-a-citing-note-owes.md` is grounding and fits kb-maintenance better (it carries both tags). `pointer-design-tradeoffs-in-progressive-disclosure.md` is retrieval pointers and fits context-engineering better.
5. Staleness:
   - "TODO: This survey is from the agent's training data" is left in the head.
   - "(now in [maintenance])" is an old migration note.
   - The link text "two-kinds-of-navigation" does not match the note title.
   - "Our link semantics (extends, grounds, contradicts, exemplifies)" plus ADR 009 as the only Decision leaves out the current `link-vocabulary.md` and ADR 054 lineage labels.
   - It links non-member `indexes-lower-recall…`.
6. Shape: 11 members, 2 unreached (`links-encode-conditional-possibilities-not-obligations.md`, `pointer-design-tradeoffs…`). `complete: true` is achievable with 2 additions. The Prior work and Reference material sections are the bulk of the page and do not route to members.
7. Verdict: **rewrite opening**. Reason: the tag is small and coherent, but the head leads with a claim and a training-data survey, and the current link-vocabulary doc is missing.

## llm-reliability

1. Opening: good. "LLM output deviates from what the user intended for three distinct reasons — underspecification…, error by the interpreter, and indeterminism…". Missing words used by newer members: confidence, contamination, soundness, verification of reasoning.
2. Defining note: yes. `llm-output-deviation-requires-three-way-diagnosis.md` is first under "The Taxonomy".
3. Boundary: learning-theory and computational-model are named. The confusable tags that are missing are evaluation (for example `verifiable-subroles-before-reviewer-identity.md` and `reasoning-production-is-not-reasoning-evaluation.md` carry both) and failure-modes.
4. Fit: `memory-backed-personalization-can-look-like-model-improvement.md` fits agent-memory/evaluation better. `cheap-generation-breaks-text-volume-as-an-effort-signal.md` is a reviewer-economics claim (evaluation). Going the other way, `agentic-systems-interpret-underspecified-instructions.md` is presented as "source 1" of the taxonomy but is not tagged llm-reliability.
5. Staleness:
   - "(kb-design, learning-theory)" names a tag that no longer exists.
   - It links 4 non-members, including the "source 1" pillar note.
   - Newer members are absent (generation-confidence, goal-holding interpreter, bare writing prompt, context contamination).
6. Shape: 31 members, 5 unreached. Most are reached only because the Related link to learning-theory brings in its 136 members. The head is at 7.9 KB, so adding the 5 needs trimming of "Related notes in other areas" and Sources. No split is needed.
7. Verdict: **keep**. Refresh the picks, tag the source-1 note, and name evaluation as the boundary. Reason: the opening and defining note are strong, and the defects are stale annotations and missing recent members.

## methodology

1. Opening: good. "How an agent comes to work by a method: which of many known approaches it selects, how an external methodology becomes operative…, how a stated intent controls its local choices, and how far a method transfers".
2. Defining note: `definitions/actionable-methodology.md` defines the KB's methodology term, but it carries only `foundations`, so the head neither includes nor names it.
3. Boundary: yes. "What a methodology is relative to a theory… lives under learning-theory". The other confusable tag, foundations, is named only as a superset.
4. Fit: `definitions/actionable-methodology.md`, `reference/source-adoption-policy.md` (borrowing policy), and `a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md` belong here. `reviewers-share-the-fields-prior-so-interpret-findings-by-stance.md` is review interpretation and fits evaluation better.
5. Staleness: "[foundations] — every note here also carries it" is true today but unenforced and will decay. No stale terms.
6. Shape: 6 members, `complete: true` holds by direct links. If foundations is retired, this tag is the natural home for the design-method residue (borrowing, transfer, first-principles).
7. Verdict: **keep**. Reason: the opening and boundary are clear; only the definition and two borrowing items are mis-tagged outside it.

## observability

1. Opening: adequate. "Observability is about recovering signals that would otherwise stay hidden: execution paths that differ from the intended one, quality drift…". It could add "fallback", "path health", "staleness", "inspectability".
2. Defining note: none among members. `final-task-success-does-not-establish-intended-path-health.md` functions as the anchor but is not named as one.
3. Boundary: kb-maintenance is named only under Related ("maintenance consumes the signals"), even though it shares 8 of 11 members. The opening needs one sentence saying that observability is making hidden things visible, while kb-maintenance is acting on what becomes visible.
4. Fit: `notes/evidence/single-artifact-review-bundles-still-cut-claude-costs-substantially.md` is cost evidence, so evaluation. `agent-memory-systems/trace-learning-techniques-in-related-systems.md` belongs under trace-learning; it is the survey the trace-learning head calls its anchor, yet it is not tagged trace-learning.
5. Staleness: it links non-member `designing-agent-memory-systems.md`. No retired terms.
6. Shape: 11 members, 0 unreached, but only because the Related links to kb-maintenance (50 members) and tool-loop satisfy the hop. `complete: true` is therefore declarable now and would carry no routing value; 4 direct additions would make it honest. Merging into kb-maintenance would lose the runtime-path notes (final-task-success, silent-disambiguation, inspectable-artifact), which are not maintenance.
7. Verdict: **keep**, after removing the 2 misfits and stating the kb-maintenance boundary in the opening. Reason: the tag is small, coherent, and uses a word operators search for.

## self-improving-systems

1. Opening: weak. "Selective head: membership, update architectures, and the four-part pathway profile, with one note per claim." This describes the page, not the tag. The searchable definition only arrives in the second paragraph.
2. Defining note: yes, `definitions/self-improving-system.md`, linked in the second paragraph under "## Membership" rather than at the top.
3. Boundary: not stated. The confusable tags are learning-theory (47 shared), foundations (81 shared), and deploy-time-learning. Related Tags lists foundations as "the broader core theory this sits inside", which reverses the real containment. learning-theory and trace-learning are not linked, although trace-learning calls this tag its casebook.
4. Fit: sampled members fit the definition. Clusters that fit here but are invisible in the head:
   - software factory/house (13 titles: `definitions/software-factory.md`, `agentic-substrate-needs-family-specific-machinery-to-be-a-factory.md`)
   - search control (13: `lightweight-search-control-does-not-license-adoption.md`)
   - theory builder / program theory (12: `definitions/theory-builder.md`, `program-theory-sustains-search-under-delayed-feedback.md`)
   - Bitter Lesson (4)
5. Staleness:
   - The words "theory builder", "factory", "software house", "continual learning", "Bitter Lesson", and "search control" each appear 0 times in the head. These are exactly the vocabulary misses the operator reported.
   - The sentence "Membership settles the category; [deploy-time-learning] is the demand they most naturally take over from human maintainers; not definitional." is garbled.
   - It links non-member `definitions/behavioral-authority.md`.
6. Shape: 124 members, 24 unreached, and the head is at 8181 bytes (at the 8 KB warn). Curating harder cannot add the missing clusters. **Split with overlap** into children such as `software-factory`, `theory-builder`, and `search-control` (possibly `autonomy`/human-allocation, about 10 titles). With those plus current links, `complete` becomes reachable.
7. Verdict: **split**, and rewrite the opening while doing so. Reason: the head spends its full weight on the pathway-profile theory and has no room to name the three largest member clusters, which are what readers search for.

## tool-loop

1. Opening: weak. "Many LLM applications share a common operational core: construct a task frame, give the model tools, and loop until it stops." Then a code block. The description says "Index for the tool-loop argument". The page is an essay, not a head that says what the tag gathers.
2. Defining note: `llm-frameworks-should-keep-the-tool-loop-optional.md` is the thesis and `agent-is-a-tool-loop.md` the convention. Both are linked, but neither is called the anchor at the top. The foundation, `bounded-context-orchestration-model.md`, is not a member.
3. Boundary: computational-model (86% overlap) is mentioned only inside prose and a "Relevant Notes" footer, with no difference sentence. computational-model's own head treats tool-loop as a child area.
4. Fit: these agentic-systems reviews are tagged tool-loop without being about loop exposure:
   - `compound-engineering-plugin.md` (a compounding claim) fits self-improving-systems.
   - `ai-agent-book.md` (whole-book comparison) fits computational-model or context-engineering.
   - `beads-rust.md` (a coordination substrate) fits agent-memory or context-engineering.

   `orchestration-needs-privilege-quarantine-not-permission-scope.md` is security and fits computational-model. `the-chat-history-model-trades-context-efficiency…` fits context-engineering (though it is adjacent to session-history).
5. Staleness:
   - The frontmatter carries `tags: [computational-model, context-engineering, tool-loop]` (self-tagging), and COLLECTION.md says "Heads carry no `tags:` of their own".
   - It has an old-style `---` / "Relevant Notes:" footer instead of `## Related Tags`.
   - "('Expose the loop' was the earlier name…)" is migration residue.
   - It links 7 non-members, including core-argument notes such as `bounded-context-orchestration-model.md`, `rlm-has-the-model-write-ephemeral-orchestrators…`, and `silent-disambiguation…`. The tagged set and the argument the head presents have diverged.
6. Shape: 22 members, 11 unreached (8 agentic-systems reviews plus 3 notes). The head is at 7.6 KB, so `complete` needs the essay cut down. A merge into computational-model is plausible given the overlap, but the loop-exposure cluster has its own searchable name.
7. Verdict: **rewrite opening** (and shrink the essay into picks). Reason: the page argues a thesis instead of saying what the tag gathers, and its membership has drifted to harness reviews the page never mentions.

## trace-learning

1. Opening: good. "Systems that learn from their own agent traces… raw traces accumulate as episodes, logs, or transcripts, then a distillation step… produces… a memory entry, a rule, a prompt, a route, or a fine-tune." It could add "memory extraction", "session capture", "skill library", "self-evolution", which are words used in member descriptions.
2. Defining note: yes. `trace-learning-techniques-in-related-systems.md` and the review type's rule are named under "Start here". The survey itself is tagged `learning-theory, observability`, not trace-learning.
3. Boundary: good. agent-memory and self-improving-systems are named with one-line differences.
4. Fit: all 105 members carry the required `### Trace-learning` subsection, so tagging is rule-consistent. Borderline cases where the distillation is mostly fact extraction: `supermemory.md`, `pond.md` ("session archive… scheduled trace acquisition"), `nao.md`. These are still valid under the type rule. The misplacement runs the other way: the survey should carry the tag.
5. Staleness:
   - "found that loop" by "a code-grounded read" is false for the 5 `agent-memory-systems/lightweight/` members, which are doc-grounded (for example `trajectory-informed-memory-generation.md`, "not inspected code").
   - "Membership is nearly all reviews" overstates: about 100 of about 159 review files are tagged, roughly two-thirds.
6. Shape: 105 members, 99 unreached, declared selective, and the size fits that. A split by distilled form (memory facts / skills-prompts / harness code-weights) is possible but not needed, since the survey does that job. `complete` is not worth pursuing.
7. Verdict: **keep**, after fixing the two inaccurate sentences and tagging the survey. Reason: the opening, anchor, and boundary are all present and the selective stance is correct.

## type-system

1. Opening: adequate. "Why documents have types, what the type system does, and how structured writing improves quality." Missing words: type spec, schema, frontmatter, validation, traits, collection-local types.
2. Defining note: `why-notes-have-types.md` is first under Overview but is not named as the anchor in the opening.
3. Boundary: document-system is named as parent ("Sub-area of document-system"), but there is no difference sentence. For example: document-system covers writing conventions and validation broadly; type-system covers why and how artifacts declare contracts.
4. Fit: `reference/proposals/generalized-validation-invalidation-and-imperative-extension.md` and `reference/validation-contract.md` are validation machinery and fit document-system or architecture better. `wikiwiki-principle…` is equally a constraining (learning-theory) example, which the head acknowledges.
5. Staleness:
   - The frontmatter carries `tags: [document-system]`, which a head must not have.
   - The directory-scoped pick says "global types tax every session; local types load only when working in that directory". The note's current description says "path pointers load either kind on demand", so the gloss is superseded.
   - It links non-member `reference/collections-and-types.md`.
6. Shape: 15 members, 3 unreached (validation-contract, generalized-validation proposal, artifact-function proposal). `complete: true` is achievable with 3 additions.
7. Verdict: **keep**. Remove the frontmatter tag, refresh the directory-scoped gloss, and add the 3 links plus the complete mark. Reason: the tag is small and coherent with a clear anchor, and only local staleness needs fixing.

## Cross-cutting

- **Vocabulary gaps sit in the big heads.** self-improving-systems, foundations, and learning-theory never say "software factory", "software house", "search control", "Bitter Lesson", or "continual learning". Each is a cluster of 3 to 13 member titles. This matches the operator's failure pattern: the notes are there, but the head words are not. The heads are organized around the theory's internal structure (pathway profile, accumulation) rather than the nouns in member titles.
- **Link text has drifted from note titles.** Examples: "traversal-improves-the-graph", "two-kinds-of-navigation", and the directory-scoped gloss. Link text frozen from older slugs hides the current title words from `rg` over heads.
- **Related-Tags links make `complete` pass without routing.** observability reaches 100% only through kb-maintenance, and llm-reliability reaches 26 of 31 only through learning-theory. Under ADR 090 any linked head counts, so a neighbour link to a large head can make `complete` pass mechanically with no routing value. Consider requiring that a child link's context phrase say "child", or excluding links under `## Related Tags` from the hop.
- **Heads link non-members as if they were members.** tool-loop links 7, llm-reliability 4, and foundations 2. A head's argument often depends on untagged notes; either tag those notes or label them as neighbours.
- **Pre-ADR 089 residue remains.**
  - `tags:` frontmatter on tool-loop and type-system.
  - `[tags](./README.md)` described as a "parent area"/"hub" in kb-maintenance and learning-theory.
  - The retired tag name `kb-design` in llm-reliability.
  - Migration notes such as "(now in maintenance)" and "'Expose the loop' was the earlier name".
  - "These notes" in heads whose members span reference/ and agent-memory-systems/.
- **Rank tags versus topic tags.** foundations (and to a lesser degree methodology as its subset) is a status label that duplicates self-improving-systems membership. Topic tags route better, and retiring or narrowing foundations removes most of the 69% overlap.
- **Reference-proposal members are unrouted.** In kb-maintenance (19 outside notes) and type-system, `reference/proposals/*` members are almost never linked, even though they are the most recent additions. Recent members in general are absent from heads curated before the sweep (llm-reliability, kb-maintenance, tool-loop's agentic-systems reviews).
- **Anchors are placed below the fold.** Where a defining note exists (self-improving-systems, links, type-system, learning-theory), it appears in the second paragraph or lower rather than in the first sentence.
