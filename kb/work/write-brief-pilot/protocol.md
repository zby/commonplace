# Write-brief pilot: protocol

**Status: DRAFT** — awaiting operator review. Changes are free until the commit that sets this line to `frozen`; after it, changes go to `deviations.md`.

The fixed parts below are fixed for comparability, not because the executor could not choose them: results must compare across arms, and a choice made after seeing outputs would let the data pick the hypothesis.

## Conjectures and refutation conditions

A *commission item* is one requirement a brief places on the target: a governing claim, an intended reader update, an exclusion, a passage to preserve because another artifact relies on it, a claim-mode or scope limit. The item kinds follow the split that the [directive-text rule](../../instructions/cp-skill-write/SKILL.md#universal-mechanics) of `cp-skill-write` borrows from mission command: intent (governing claim, reader update), then boundaries — constraints (must-keep, scope) and restraints (exclusions) — with the means left to the writer. An item is *recoverable* if a reader holding only the incumbent artifact, its backlinks, and the target's type spec and collection contract would keep it without being told; otherwise it is *non-recoverable*. The type spec and collection contract count because `cp-skill-write` loads both for every write. Recoverability is classified before any run (Phase 0).

**H1 — The value of a brief is concentrated in non-recoverable items.**
Prediction: across all pressure runs, the no-brief arm violates at least 5 more non-recoverable items than the original-brief arm, and the gap between the arms' violation *rates* is larger on non-recoverable items than on recoverable items.
Refuted if the no-brief arm violates fewer than 3 more non-recoverable items than the original-brief arm, or the rate gap on recoverable items is at least as large. Rates are used for the comparison because recoverable items outnumber non-recoverable ones about five to one. Refutation favors Options 1 or 2 of the proposal: the artifact, or the artifact plus its body, already carries what matters.

**H2 — A brief adds less where the title states the governing claim.**
Prediction: the per-target violation gap (no-brief minus original-brief, non-recoverable items, normalized by item count) is smaller on average for the five claim-titled notes than for the five non-claim documents.
Refuted if the average gap is equal or larger for the claim-titled notes. See Limits for what the non-claim class mixes.

**H3 — A brief written before drafting holds information that cannot be rebuilt from the finished artifact.**
Prediction: the rebuilt-brief arm violates at least 3 more non-recoverable items than the original-brief arm, summed over all pressure runs.
Refuted if the rebuilt-brief arm is within 1 violation of the original-brief arm. Refutation removes the proposal's argument for storing briefs independently: a brief could be generated on demand.

**H4 — A brief does not silently over-constrain.**
Prediction: in every override run with a brief, the writer either follows the request and states which commission item it amends, or asks the user, as `cp-skill-write` Step 4 requires.
Refuted if any brief-arm override run silently preserves the conflicting item against the request, or silently drops it without naming the amendment.

**H5 — A one-line brief carries the claim and reader update but not the exclusions or dependencies.**
Prediction: the one-line arm (D) is within 2 violations of the original-brief arm on items of kind *governing claim* and *reader update*, and violates at least 3 more items than the original-brief arm on items of kind *exclusion* and *must-keep*, summed over all pressure runs.
Refuted in the direction of "one line is enough" if D is within 1 violation of B on exclusion and must-keep items as well. Refuted in the other direction if D is no better than the no-brief arm on claim and reader-update items. The first refutation would argue for one-line briefs; the second, that a one-line brief adds nothing to the title.

**Compliance guard.** A run that does not carry out its edit request scores as a failed run in every conjecture, not as preservation. Without this guard a brief arm could win by refusing to edit.

The thresholds are set for n = 10 targets with 2 replicates and are coarse by design. Against the commissioned versions, about 40 items are non-recoverable and present (roughly 4 per target), so each arm has about 80 non-recoverable item-runs across its 20 pressure runs; a gap of 5 is about 6 percentage points. A result between the prediction and the refutation line is recorded as undecided, not rounded either way.

## Targets

| # | Target | Class | Commission source (commit) |
|---|---|---|---|
| 1 | `kb/notes/context-operation-interface-bounds-context-policy.md` | claim-titled note | `multistage-write-context-operation-interface-20260827` (`d7615fea`) |
| 2 | `kb/notes/current-task-fit-alone-does-not-warrant-costly-entrenchment.md` | claim-titled note | `multistage-write-costly-entrenchment-options-20260828` (`16be19f9`) |
| 3 | `kb/notes/prototype-standing-is-revision-cost-binding-plus-lost-investment.md` | claim-titled note | `multistage-write-prototype-standing-revision-cost-20260827` (`db995fab`) |
| 4 | `kb/notes/the-bitter-lesson-defense-portfolio-has-one-load-bearing-member.md` | claim-titled note | `kb/work/theory-mediated-self-improvement-series/gradual-compatibility-brief.md` (`2c8b2268`) |
| 5 | `kb/notes/adversarial-loop-can-reconstruct-the-writing-is-thinking-filter.md` | claim-titled note | `kb/work/written-artifacts-in-learning-loops/pilot-adversarial-loop/brief.md` (`ce45b282`) |
| 6 | `kb/instructions/analyse-agentic-system/SKILL.md` | instruction | `multistage-write-analyse-agentic-system-20260820` (`303e20b0`) |
| 7 | `kb/instructions/analyse-external-system-epistemic-architecture.md` | instruction | `multistage-write-analyse-epistemic-architecture-20260820` (`303e20b0`) |
| 8 | `kb/articles/can-a-theory-builder-running-on-fixed-weight-llms-learn.md` | article | `kb/work/theory-builder-article-series/README.md` (`b0d98aa8`), the entry for this article |
| 9 | `kb/articles/an-automated-software-house-as-a-second-test-of-a-theory-builder.md` | article | `kb/work/theory-builder-article-series/README.md` (`b0d98aa8`), the entry for this article |
| 10 | `kb/notes/designing-agent-memory-systems.md` | synthesis note | `kb/work/agent-memory-design/framing.md` (`c4cd0bd7`) |

Class is by whether the title states the governing claim, not by the `title-as-claim` trait (target 2 lacks the trait but has a claim title). For targets 1–3, 6, and 7 the brief is `kb/work/multistage/<run>/brief.md` at the listed commit. Targets 4, 5, and 8–10 come from a search of git history on 2026-09-26 for commissions written before the target's final draft that name or clearly identify one existing target and state more than its title. Their sources are workshop framings or briefs in other formats; Phase 0 stripping extracts the part that commissions the target. Target 10's source implies the target through the workshop goal rather than naming its path. Target 8 has a second, independent commission (`kb/work/lead-article-learning-first/README.md` at `e7e28fa6`); this pilot uses only the first, and a two-commission comparison is deferred.

The operator capped the pilot at ten targets. Before any run, three qualifying candidates were dropped to reach five claim-titled and five non-claim targets:

- `kb/notes/any-symbolic-program-with-llm-calls-is-a-select-call-program.md` (`multistage-write-select-call-cordis-20260814`): its commission is mainly a source integration, so stripping source-bound items would leave little commission;
- `kb/work/epistemic-architectures/arc-skill-reading.md` (`multistage-write-arc-skill-reading-20260820`): a workshop file, which the workshop lifecycle consumes, so a durable brief does not apply to it;
- `kb/instructions/premise-decomposition-gate.md` (`b2b8e2a3`): the thinnest non-claim commission, and a third instruction would add to the instruction confound (see Limits).

Excluded from the search results by the selection criteria: the theory-builder definition, whose commission was committed with its first draft; the bootstrapping article, whose commission is an edit-and-relocate order; the testing article and the two-layer execution note, whose commissions are thin or ambiguous about their target.

**Incumbent.** Each run starts from the target's *commissioned version*: the version the commissioned write produced, so that every brief item was, as far as the commission's own acceptance route could tell, realized in it. A first labelling pass against today's documents (kept in `drift-at-head/`) showed that several targets have since moved away from their briefs, some deliberately; testing preservation against a document that no longer contains the commissioned content would test nothing. The commissioned versions are copied to `incumbents/<n>.md`, with the backlinks that existed at that commit listed in `incumbents/<n>.backlinks.md`.

| # | Commissioned version | Path at that commit | Why this commit |
|---|---|---|---|
| 1 | `d7615fea` | same as today | promotion of the multistage run |
| 2 | `16be19f9` | same as today | promotion of the multistage run |
| 3 | `db995fab` | same as today | promotion and relocation of the multistage run |
| 4 | `69cbae6a` | same as today | the commissioned row landed; removed on 2026-08-30 by `2b406eea` |
| 5 | `ce45b282` | `kb/work/written-artifacts-in-learning-loops/pilot-adversarial-loop/candidate.md` | accepted candidate (acceptance PASS, blind comparison 3–0 over the incumbent), never promoted; the workshop closed at `c7484bea` |
| 6 | `b23f1e07` | same as today | promotion of the multistage run |
| 7 | `40c26509` | same as today | promotion of the multistage run |
| 8 | `ae705f52` | `kb/articles/learning-by-theory-refinement-with-fixed-models.md` | last commit of the same-day review the commission required before listing |
| 9 | `a7159d47` | `kb/articles/an-automated-software-house-as-an-alternative-test.md` | the operator's claim decisions applied, before retitle and relocation |
| 10 | `ba536434` | same as today | promotion of the workshop synthesis into `kb/notes/` |

For targets 1–3 the brief and the promoted note share one commit because multistage runs commit on promotion; the brief was written first inside the run.

## Arms

- **A — no brief.** The writer receives the edit request and the incumbent, as in ordinary `cp-skill-write` use today.
- **B — original brief.** As A, plus the stripped original brief from `briefs/`.
- **C — rebuilt brief.** As A, plus a brief written by a fresh agent from the incumbent and its backlinks only, in the same format and length budget as B, and stripped by the same rule.
- **D — one-line brief.** As A, plus one sentence of at most 250 characters condensed from the stripped original brief by a fresh agent told to keep what matters most for a later editor. It tests brief length, not a frontmatter field: it is delivered as a retained-intent block like B and C.

Arms B, C, and D present the brief as a retained-intent block in the form `cp-skill-write` Step 4 accepts: source, subject, scope, and force (authoritative for intent). B, C, and D carry identical labels, so the writer cannot tell an original brief from a rebuilt or condensed one.

Deferred, not part of this pilot: a frontmatter `goal:` field (set aside by the operator on 2026-09-26: it is edited in the same write as the artifact, so it is not independent of drift, and it would compete with `description`), an arm with the brief's content moved into the artifact body (Option 2), and a replay of the fifth Popperian maintenance episode with the operator's sentence as a brief.

## Phase 0 — materials (before freeze)

1. **Strip the original commissions.** Remove items that bind only the original run: review findings to address, evidence and source lists, workshop mechanics, commit instructions, relocation steps already done. Keep the governing question, audience and reader update, target claim, must-keep and must-exclude items, scope, terminology, and reserved decisions. Write the result to `briefs/<n>.md`, recording each removed item and why in a trailing list. The operator reviews all ten before freeze.
2. **Extract commission items.** A fresh agent lists the commission items of each stripped brief in `rubric/<n>.md`, one line each, numbered.
3. **Classify recoverability.** A second fresh agent, given the incumbent and a list of its backlinks but not the brief, receives each item and answers: does the artifact state or clearly imply this, so a careful editor would keep it without being told? Mark recoverable or non-recoverable. The operator may spot-check but does not reclassify after freeze.
4. **Write the edit requests.** For each target, one **pressure** request that invites drift on at least two non-recoverable items without naming them (such as "cut this to 60% of its length", "generalize the claim", "fold in neighbor X", "rewrite for a newcomer"), and for targets 2, 3, 4, 6, and 8 one **override** request that legitimately conflicts with one named commission item. Requests are written from the rubric, before any run, and are identical across arms.
5. **Build the rebuilt briefs (arm C) and one-line briefs (arm D).** Done now, not during runs, so every run of a cell uses the same brief.
6. **Label item kinds.** In `rubric/<n>.md`, tag each commission item with one kind: governing claim, reader update, constraint (must-keep, must-include, required distinction), restraint (exclusion), scope (modality, applicability, terminology, length), or reserved decision. H5 reads its result by kind; where H5 says *exclusion* and *must-keep* it means `restraint` and `constraint`.

## Phase 1 — runs (after freeze)

- **Cells.** 10 targets × 4 arms × 2 replicates of the pressure request = 80 runs. Override runs: 5 targets × arms B, C, and D × 1 = 15 runs. Total 95.
- **Worker.** A fresh sub-agent per run, on the session's Opus model (record the concrete model id), following `cp-skill-write` in edit mode with these deviations: it writes its candidate to `runs/<target>-<arm>-<replicate>/candidate.md`, never to the target path; it skips Step 7 source grounding and Step 9 validation, and adds no new source dependency; it does not invoke `cp-skill-connect` or ask the user a question it could not ask in a real run. If it would ask the user (Step 4 conflict), it writes the question to `question.md` and stops; that is a valid outcome and scores as *flagged*.
- **Order.** Randomize run order across cells; record the order.
- **Isolation.** Workers get no access to this workshop beyond their own run directory and input packet.

## Phase 2 — blind scoring

- For each run, strip arm identifiers and assign an opaque id. The mapping stays in `scores/key.md`, unread by scorers.
- A fresh scorer per target receives: the incumbent, the edit request, the numbered commission items (without the recoverable/non-recoverable label), and the candidate or `question.md`.
- The scorer may also read any file a commission item names (for example another article whose comparison section must agree, or a collection contract), and the incumbent's backlinks.
- It scores:
  - **compliance** with the edit request: done, partial, or not done;
  - each **commission item**: kept, violated, flagged (the writer named a conflict or asked), or amended-with-notice (override runs only: changed as requested, and the change is stated).
- "The incumbent" in worker and scorer packets means `incumbents/<n>.md`, never today's target.
- Two scorers per target on different model families if available; otherwise two independent Opus scorers. Record disagreements. Resolve them by a third scorer, not by the operator.

## Drift study (observational)

Alongside the experiment, trace each commission item from the commissioned version to the target at the freeze commit. Classify it as *survived*, *removed by recorded decision* (a commit body, ADR, or workshop record names the change or its reason), or *removed without record*. A fresh agent does the tracing from git history; the operator adjudicates any item it cannot place.

This study is not pre-registered in the strict sense: before it was designed, the first labelling pass and the target-4 and target-5 histories had already shown that some commissioned content was lost, some of it without record. It reports a denominator (how many commissioned items were lost, and how many of those silently) rather than testing a prediction. Its bearing on the proposal runs both ways: silent removals are the drift a brief could catch; recorded removals are cases where a brief left unamended would have gone stale.

## Analysis

- **Conflicting items.** Items the rubric marks `(conflicts with <k>)` cannot all be kept in one candidate. They are scored but excluded from the H1, H3, and H5 tallies, and reported separately as evidence for H4-style handling: did the writer notice the conflict, follow the later item, or silently pick one.
- **Undelivered items.** Items labelled `(absent)` in `recoverability/` were never realized in the commissioned version, so a pressure run cannot keep or violate them. They are excluded from the H1, H3, and H5 tallies. Scorers still score them, and the analysis reports separately whether any arm *added* an absent item: a brief arm restoring commissioned content that the original write never delivered is a result the conjectures did not predict.
- **Undecidable items.** A scorer may mark an item *undecidable* when the candidate text cannot settle it (for example a requirement on how two trial agents behave). Undecidable scores are counted and reported but excluded from tallies. If both scorers mark more than a third of a target's items undecidable, report that target separately.


Tally per arm, per class, and per item-recoverability, then read each conjecture against its frozen refutation line. Report every run in a table, including partial-compliance and failed runs. Record anything the conjectures did not predict under **Unpredicted** before interpreting it; that section is where the surprise the operator asked about will show up, if any.

## Limits (to state in the evidence note)

- Ten targets, two replicates: the pilot can refute the stronger predictions, but it cannot estimate effect sizes.
- The original commissions are careful, operator-directed texts made inside multistage runs or workshops. Ordinary briefs would likely be thinner. Targets 4, 5, and 8–10 were selected after the pilot was designed, from a search that knew what the pilot needed (non-claim targets); selection was by the stated criteria, before any run.
- The non-claim class mixes kinds: two instructions, two articles, one synthesis note. Instructions fall under the directive-text rule, so they already open with their intent; for them the brief partly repeats the artifact, which is an Option 2 effect, not the claim-title effect alone. Report H2 with and without the instructions.
- Writers, rebuilders, and scorers are all Claude models. Shared biases may inflate agreement.
- The pressure requests are written by someone who has seen the briefs. They are designed to test the items, which is the point of a severe test, but they do not measure how often ordinary edits threaten a commission.

---

- [Per-artifact write briefs](../../reference/proposals/per-artifact-write-briefs.md) — tests: Options 1–3 and the pre-draft independence force
- [cp-skill-write](../../instructions/cp-skill-write/SKILL.md) — depends-on: the writing procedure and its Step 4 retained-intent input used in every arm
- [Warranted reader update is the objective of substantive writing](../../notes/warranted-reader-update-is-the-objective-of-substantive-writing.md) — draws-on: the reader update as a commission item distinct from the title claim
