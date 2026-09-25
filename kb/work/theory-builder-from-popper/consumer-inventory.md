# Consumer inventory: theory-builder migration

Step 2 of this workshop, refreshed against the four-condition draft and the
settled decisions D1–D8. Nothing in the library changes until the operator
approves this plan, including the titles and the new decisions at the end.

## How this was built

Scan at 2026-09-25T08:34+02:00 over `kb/` and `AGENTS.md`, excluding
`kb/reports/cache/**`, `kb/reports/state/**`, `kb/sources/.snapshots/**`, and
this workshop:

```bash
rg -l -i -e 'theory[- ]builders?' -e 'conjectural[- ]learn' \
   -e 'theory-builder\.md' -e 'conjectural-learning' kb AGENTS.md \
   --glob '!kb/reports/cache/**' --glob '!kb/reports/state/**' \
   --glob '!kb/sources/.snapshots/**' --glob '!kb/work/theory-builder-from-popper/**'
```

- **201 files** matched (198 in the first pass). The additions are all
  frozen output of the concurrent analysis batch plus one staged work file
  (`kb/work/framework-delivery/staged/files/README.md`).
- The ingest set is unchanged: 93 files, the same names as the first pass.
- Files linking each target definition:

  | File | Linking files |
  |---|---|
  | `conjectural-learning.md` | 130 (86 ingests, 17 reviews, 1 retained result, 26 others) |
  | `theory-builder.md` | 14 |
  | `externally-tested-theory-builder.md` | 9 |
  | `reflective-theory-builder.md` | 7 |
  | `autonomous-theory-builder.md` | 7 |
  | `conjectural-learning-checks.md` | 1 (the definition itself) |

- **Concurrent batch, frozen per D6.** At scan time
  `kb/agentic-systems/reviews/` holds 46 files, 25 matching (17 link
  `conjectural-learning.md`); `agentic-system-analysis/` holds 36 result
  directories, 27 matching (1 links `conjectural-learning.md`). Most are
  untracked. Anything the batch adds after this scan is frozen too; rerun the
  scan before step 4 only to update counts, not to plan edits for them.
- Outside the scan scope: `tests/scenarios/ingest-a-source.md` (names
  `conjectural-learning.md` as a required read), `properdocs.yml`
  (redirects), and the root `README.md` (links the bootstrapping article by
  path; unaffected unless that file is renamed).

Category codes: **F** frozen, **L** link or wording only, **S** substantive,
**N** no edit, **R** a target definition.

## What changes for consumers

The consumers were written against two library definitions: conjectural
learning (formulated, operative, open to criticism, improves capacity) and
the old theory builder (persistent, responsible for theories, no criticism
required). The draft differs from them as follows.

1. **Criticism is required.** The old builder did not require it. A consumer
   that calls a system a builder only because it keeps and develops theories
   may now be wrong.
2. **No success condition.** Old conjectural learning required improved
   capacity. A system that meets the four conditions without shown
   improvement was "not established"; it is now a theory builder whose
   learning is untested. Verdicts can flip toward membership.
3. **Retention is required.** Old conjectural learning admitted a theory built
   in a run and then discarded (old checks case 6). The draft puts this
   outside (condition 4), along with one invocation of a refinement
   procedure such as FORTE. Where a run ends is not settled by the draft;
   see decision N1.
4. **Addressability stays graded.** Condition 1 needs only localized
   content. Finer addressability is a design commitment, as it already was
   for conjectural learning. Consumers that say "addressability is separate
   from membership" stay right. Consumers that say "a theory builder
   requires addressability" (the `AGENTS.md` entry) must say it requires
   only the minimum.
5. **Whole replacement and reconstruction stay inside** (D3). Reconstruction
   from retained criticisms counts; reconstruction from records of inputs and
   outcomes only does not (checks case 4). "Whole replacement or
   reconstruction can qualify" survives with that narrowing.
6. **Weights.** A system whose only change is weight adaptation is outside
   (conditions 1 and 3). Weights changing together with a stated, retained,
   criticized theory are inside (case 8). Criticism applied through weights
   is outside (case 28). "Weight changes do not exclude conjectural learning"
   survives only in the case-8 sense.
7. **"Learning" is ordinary English** in Simon's sense. "Does not establish
   conjectural learning" must say which claim failed: a named builder
   condition, or learning (improvement or its attribution), or both.
8. **Reflective and autonomous are qualifiers.** The reflective connection
   runs through consumption and criticism and is not kept up automatically.
   The separate `reflective-system` definition and its two-way wording stay;
   the skill's *Reflection* bullet, the result type, and
   `a-complete-theory-path…` keep that finding and add the qualifier.
9. **Apparatus leaves the definition.** Seed, extension, evidence interface,
   and intervention accounting move (relocation map below).

Old checks cases that change class, from `conjectural-learning-checks.md` to
`theory-builder-checks.md`:

| Case | Old class | New class |
|---|---|---|
| 6: theory built while reasoning, then discarded | Inside if capacity improved | Outside (condition 4) |
| 15: consumed theory not yet criticized | Inside, premised on improvement | Inside; improvement not needed |
| 4, 5, 7, 9: named baselines | "Comparison" | "Outside", same grounds |
| any inside case without improvement | Attempt to learn | Inside; learning is a separate claim (case 17) |

Cases 1–3, 8, 10–14, and 16 keep their class.

## Target definitions (R)

| Path | Action |
|---|---|
| `kb/notes/definitions/theory-builder.md` | Replace with the draft in place; its 14 inbound links survive. Check each link's anchor and label (L rows). |
| `kb/notes/definitions/conjectural-learning.md` | Delete; redirect to `theory-builder.md` |
| `kb/notes/definitions/conjectural-learning-checks.md` | Delete; promote `theory-builder-checks.md` beside the definition (D4); redirect |
| `kb/notes/definitions/reflective-theory-builder.md` | Delete; redirect to `theory-builder.md` |
| `kb/notes/definitions/autonomous-theory-builder.md` | Delete; redirect to `theory-builder.md` |
| `kb/notes/definitions/externally-tested-theory-builder.md` | Delete; redirect to the obligations note, the concept's main home under D5 |

Redirects: deletion is not a relocation, so the five retirements need
hand-added `redirect_maps` entries in `properdocs.yml` (precedent 643508db,
which retired `theory-refinement.md`). Retarget the three existing entries
that point at `conjectural-learning.md` (`learning-by-theory-refinement`,
`theory-mediated-learning`, `theory-refinement`) so the map stays flat.
Retitles go through `commonplace-relocate-note`, which adds its own
redirect. Flatten existing chains into a retitled path: 22 article redirects
point at the article paths named for conjectural learning, and 5 note
redirects at the precedents and evidence notes. Check with
`commonplace-validate redirects`. Redirects cover only the published site;
`kb/reports/**` is unpublished except `agentic-system-analysis/**/result.md`,
and the local link checker does not follow redirects. Retire freshness
baselines keyed to the deleted definitions, as 643508db did.

## System-definition artifacts

| Path | Uses | Cat | Proposed edit |
|---|---|---|---|
| `AGENTS.md` | Vocabulary: *Conjectural learning*, *Externally tested theory builder*, *Theory builder*; *Addressable theory* says "conjectural learning does not require it, a theory builder does" | S | Delete the conjectural-learning and externally-tested entries. Replace the theory-builder entry: four conditions, no success condition, two qualifiers. In *Addressable theory*: a theory builder requires only its minimum, localized content; finer grades are a design commitment. The commit body says this reverses the 2026-09-21 decisions. |
| `kb/instructions/assess-learning-claims-during-ingest.md` | Loads `conjectural-learning.md` as "the current comparison basis for learning membership" | S | Load `theory-builder.md`. Step 3 judges the source condition by condition, each at its own evidence strength, and judges learning (improved capacity) as a separate claim. State the run-scope reading chosen in N1. Keep "leave unresolved mappings explicit". The addressable-theory read stays conditional. |
| `kb/instructions/analyse-agentic-system/SKILL.md` | Step-3 bullets *Formulated tentative theories*, *Criticism*, *Conjectural learning*, *Addressability and retention*, *Reflection*; l. 236; completion check l. 530; footer `rests-on` | S | Map as below. |
| `kb/types/agentic-system-analysis-result.md` | ll. 245–275 mirror the skill: "conjectural-learning claim", "Whole replacement and reconstruction do not by themselves exclude learning" | S | Same mapping. Keep the `trace_learning` sentence, saying "does not establish learning". |
| `kb/agentic-systems/COLLECTION.md` | l. 62 "These establish conjectural learning…"; "whole replacement or reconstruction can qualify" | S | Pathway findings establish builder conditions 1–3; retention is condition 4; improved capacity is a separate learning claim. Keep "whole replacement or reconstruction can qualify", narrowed to reconstruction from retained criticism. |
| `tests/scenarios/ingest-a-source.md` (outside scope) | Required read | S | Follow the ingest instruction; run `uv run pytest` after. |

**Skill and type mapping.** The skill already records a theory route claim by
claim; the change regroups the claims.

| Current skill finding | New home |
|---|---|
| Formulation ("stated in natural or formal language") | Condition 1, localized content |
| Operative use ("which decisions depend on that content") | Condition 2, consumption |
| Criticism (content-directed; a score selecting variants does not count) | Condition 3, unchanged. Add: a criticism is itself stated and can blame the test, data, or an auxiliary. |
| Retention ("record separately what persists") | Condition 4, now a membership condition. Reconstruction from retained criticisms counts; input/outcome records alone do not. |
| Addressability (degree and boundary) | Stays a separate graded finding above condition 1. "Whole replacement … can support" stays, reworded to builder membership. |
| *Conjectural learning* bullet | Split. **Theory-builder membership**: conditions 1–4, each with its own conclusion status, never inferred from neighbours. **Learning**: the improved-capacity claim as now worded (capacity, assessment boundary, evidence, attribution, persistence). |
| *Reflection* bullet, "a reflective theory builder additionally revises a self-theory" | Keep the `reflective-system` finding. The reflective qualifier: method texts meet conditions 1–4 and are criticized against records of the builder's own operation. Add the autonomous qualifier as a role-by-role record; the skill already records decision roles. |
| Rationale vs criticism; opacity rule; revision selection prefers reach | Unchanged |

New runs report "theory-builder conditions 1–4" plus "learning" as free-text
conclusion-status labels. No schema field changes.

## Definitions and notes

| Path | Uses | Cat | Proposed edit |
|---|---|---|---|
| `kb/notes/definitions/addressable-theory.md` | l. 17 "Conjectural learning does not require it"; footer `extends` | S | A theory builder requires only localized content (condition 1); finer grades are a design commitment whose payoff is conjectured. Footer to `theory-builder.md`. |
| `kb/notes/definitions/tentative-theory.md` | l. 43 "Conjectural learning covers only the formulated ones"; footer | L | "A theory builder's theories are the stated ones (condition 1)"; repoint the footer. |
| `kb/notes/commonplace-studies-conjectural-learning-through-retained-theories.md` | Title; "The definition states when the term applies"; l. 92 "does not add a membership condition"; l. 131 "can be conjectural learning" | S | Retitle (D1). The frame reverses: Commonplace builds a theory builder and tests whether it learns. Retention is now definitional; fine-grained addressability stays a chosen treatment. The addressability conjecture compares against a whole-replacement builder (checks case 26); the retention and efficiency conjectures compare against the trace-only baseline (case 4). |
| `kb/notes/conjectural-learning-has-distinct-precedents.md` | Title; "Conjectural learning names the learning process"; "Commonplace adds the conditions… must improve capacity" | S | Retitle (D1). Restate as precedents for the builder's operations; the "Commonplace adds" paragraph lists the four conditions and drops improvement. Check whether a precedent (EBG, FORTE, Rainbow) was admitted only because a discarded theory counted; FORTE now sits in Exclusions. |
| `kb/notes/evidence/rules-weights-and-missing-rationale-do-not-settle-conjectural-learning.md` | Title, description, synthesis paragraph | S | Retitle (D1). The rules half survives: missing rationale does not settle membership (Prime Agent, Recuris). **The weights half flips:** Apodex retains only weights and nothing revisable survives the run, so it is outside (conditions 1 and 4). Drop "learning … before a temporary theory is discarded". |
| `kb/notes/retained-theories-may-improve-sample-efficiency.md` | ll. 20–22 "Retention and addressability are chosen treatments … Conjectural learning also admits whole replacement…"; l. 40; l. 104; footer l. 215 | S | Retention becomes a builder condition; fine-grained addressability stays the chosen treatment; whole replacement and reconstruction from criticism remain inside. The conjecture: a builder with finer addressability beats a coarser builder and the trace-only baseline. Footer: "membership requires retention, not fine-grained addressability". |
| `kb/notes/proposals/retained-theories-compared-with-retained-traces-under-resource-limits.md` | l. 127–137 "reconstructed from criticism"; "The reconstruction may itself be conjectural learning"; footer | S | The trace arm is the case-4 baseline, outside the builder, and may still learn in the ordinary sense. Reconstruction from criticism is inside. The comparison itself is unchanged. |
| `kb/notes/a-complete-theory-path-does-not-establish-improved-capacity.md` | Opening; ll. 160–161 "Retaining an addressable theory is … not a condition of conjectural learning"; l. 172; reflective paragraph | S | Keep the claim. Say "learning" for improvement. Rewrite ll. 160–161: retention is a builder condition; fine-grained addressability remains the arrangement's premise. Keep the l. 172 question. Check the reflective paragraph against shift 8. |
| `kb/notes/open-ended-theory-learning-and-factory-learning-close-the-same.md` | l. 34; "retention and recurrence are not universal conditions of conjectural learning"; proof-only case l. 150 | S | Retention is a builder condition; recurrence and improvement are learning claims. Proof-only: "not a theory builder (condition 3)". |
| `kb/notes/a-claim-without-external-assessment-carries-three-obligations.md` | Opens by contrast with the externally tested builder; footer | S | Receives the concept (D5); see the relocation map. The opening defines the externally supplied falsifier, objective, and outcome level directly instead of linking the retired definition. |
| `kb/notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md` | Section comparing with a theory builder; "theories of external subjects and of its own machinery" | S | Light: "of its own machinery" is the reflective qualifier. Classification stays open, as in the draft. |
| `kb/notes/theory-and-capacity-building-make-the-same-kind-of-commitment.md` | Heading "Conjectural learning is one causal path…" | S | Light: "Theory building is one causal path…"; the claim holds. |
| `kb/notes/disconnected-witnesses-do-not-establish-a-causal-path-through-theory.md` | "establishes conjectural learning only when … improves capacity" | L | "establishes learning only when…"; repoint |
| `kb/notes/an-optimal-long-run-learning-strategy-invests-in-its-own-machinery.md` | Links the reflective and autonomous definitions | L | Repoint to `theory-builder.md#qualifiers` |
| `kb/notes/factory-construction-does-not-establish-knowledge-acquisition.md` | "can be driven by conjectural learning, program search…" | L | "by a theory builder's conjecture and criticism"; repoint |
| `kb/notes/bitter-lesson-selects-against-unearned-reach-not-against-structure.md` | Definition and companion links | L | Repoint; follow D1 |
| `kb/notes/learning-theory-README.md` | Index entries for the definition and companion | L | Theory-builder entry; follow D1 |
| `kb/notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md`, `kb/notes/factory-learning-mechanisms-should-be-compared-on-the-same-causal-job.md` | Companion link | L | Follow D1 |
| `kb/notes/a-fixed-model-house-must-retain-missing-procedures-for-theory-use.md`, `kb/notes/an-open-domain-theory-builder-becomes-a-software-house-when-new-domains-require-production-machinery-changes.md` | "theory builder" in title or description; sense fits | N | none |

## Articles and hubs

| Path | Uses | Cat | Proposed edit |
|---|---|---|---|
| `kb/articles/testing-the-conjectural-learning-program.md` | Title; `source_notes` lists all five target definitions; links the externally tested and autonomous definitions; "The hypotheses" defines builder, seed, extension | S | Retitle (D2). Receives the evaluation protocol, seed, extension, and intervention accounting (map below). Replace the in-article builder definition with the new one. Keep the three hypotheses verbatim (adopted 2026-09-17); check that "builder" in them still reads right now criticism is required. Update `source_notes`. |
| `kb/articles/conjectural-learning-with-fixed-models.md` | Title; "We call a system that implements this cycle a conjectural learner"; mapping sentence; autonomous link; closing sentence | S | Retitle (D2). Its informal learner already matches the new builder. "The knowledge base calls this system a theory builder"; replace "conjectural learner" throughout; autonomous link to `#qualifiers`; closing sentence to `theory-builder.md`. |
| `kb/articles/bootstrapping-an-autonomous-theory-builder.md` | Description "fully automated conjectural learner"; reflective and autonomous links; `source_notes` | S | Light: "fully automated theory builder"; repoint to `#qualifiers`. Headline optional (D2 table). |
| `kb/articles/nearest-existing-constructions-to-a-witness-house.md` | Headline "How existing self-improving systems relate to conjectural learning"; "What the comparison asks" restates the old definition; "Establishing conjectural learning additionally requires…" | S | Retitle (D2; path unchanged). Replace the criterion paragraph with the four conditions plus the separate learning claim. Re-place each of the 18 systems for shift 2 (members without shown gains) and shift 3 (single-run retention, per N1). Several overlap the hinge ingests below. |
| `kb/articles/an-automated-software-house-as-a-second-test-of-conjectural-learning.md` | Rewrite plan; frontmatter lists the externally tested definition | S | Light. Retitle (D2). Repoint the input to the obligations note and the testing article. |
| `kb/articles/what-an-automated-reviewer-should-measure.md` | `source_notes` lists `conjectural-learning.md`; lead link by title | L | Swap for `theory-builder.md`; follow D2 |
| `kb/articles/README.md` | Series entries, "conjectural learner" | S | Light; follow D2 |
| `kb/index.md` | Three article links | L | Follow D2 |
| `kb/log.md` | Historical entries | F | Leave |

## Workshops

| Path | Uses | Cat | Proposed edit |
|---|---|---|---|
| `kb/work/ideal-interpreter/resource-bounded-ideal-interpreter.md` | "retention as the builder's rather than the interpreter's" | L | D8 restored the sentence in the draft's Boundary; check the link and anchor. |
| `kb/work/ideal-interpreter/README.md` | Links `theory-builder.md` | L | Check the anchor |
| `kb/work/theory-refinement-interface/README.md`, `…/theory-refinement-interface.md` | "interface separate from conjectural-learning membership"; definition links | S | Light: "separate from theory-builder membership"; repoint |
| `kb/work/first-downstream-run/commonplace-evidence-protocol.md` | Externally tested definition; testing article by path | L | Obligations note for the concept, testing article for the protocol; follow D2 |
| `kb/work/first-downstream-run/README.md` | Testing article anchor `#the-first-arrangement-and-its-protocol`, which does not exist | L | Follow D2; fix the dead anchor |
| `kb/work/operator-led-article-clarification/README.md`, `kb/work/explanatory-theories-deployment-time-learning/exo-case.md` | Lead link by title; "do not establish conjectural learning or improved capacity" | L | Follow D2; say "learning" |
| `kb/work/commonplace-nearest-constructions/landscape.md` | Software-house article path (ll. 49, 113); "human-inclusive" and "computational theory builder" | L | Follow D2 for the software-house path; the builder wording fits the qualifiers |
| `kb/work/commonplace-nearest-constructions/README.md`, `kb/work/README.md`, `kb/work/unattended-processing-failure-modes/catalogue.md`, `kb/work/framework-delivery/staged/files/README.md` | Wording that fits; historical path; bootstrapping path | N | none unless the bootstrapping file is renamed; `kb/work/README.md`'s entry for this workshop describes the five-condition draft — update it with the close |

## Source ingests (93 files)

The precedent is f4dc912d: rewrite only `Learning Claims (our opinion)`,
footer links, and follow-up lines; keep source-native terms, summaries,
provenance, quotes, and `snapshot_sha256`. Per D7, each substantive ingest is
re-judged condition by condition.

**Method.** I read the full `Learning Claims` section of all 86 ingests that
have one, and checked the 7 without one. Predictions are mine; each batch
confirms or corrects them.

**Rewrite rule.** State each builder condition the source shows or fails, at
its evidence strength; name the deciding condition for a negative verdict;
state learning (improvement, attribution) separately. Do not infer a missing
condition from its neighbours. Opacity leaves a condition unestablished.

### Verdict predictions

Condition numbers: 1 localized content, 2 consumption, 3 criticism,
4 retention.

| Group | Files | Deciding condition | Verdict change |
|---|---|---|---|
| V1. Flips out under either reading of N1 | 2 | 4 | Old positive becomes outside |
| V2. Weakens | 1 | 3 | Old positive becomes unestablished |
| V3. Hinges on N1, old positive | 20 | 4 | Outside under reading A; stays positive under B |
| V4. Hinges on N1, old negative | 6 | 3, then 4 | Stays negative under A; flips toward membership under B |
| V5. Positive under either reading | 9 | — | No flip; restate by condition |
| V6. Outside or unestablished, no flip | 49 | 1, 3, or 4 | Reason restated as a condition |
| V7. Link only | 6 | — | Follow D1 |

**Flip count.** Settled by the draft: 3 (V1, V2). Dependent on N1: 26 (V3
under A, V4 under B). No verdict change: 58 (V5, V6). Link only: 6. Shift 2
(no success condition) causes most V4 candidates; shift 3 (retention) causes
V1 and V3.

**V1 (2).** `gavel-graph-world-models` (plans and beliefs change within one
run; its premises are never revised), `falsifybench-rule-discovery-games-full-text`
(hypotheses live in one game's conversation; nothing crosses games).

**V2 (1).** `reflexion-verbal-reinforcement-learning`: the old positive rested
on improvement from reflections; the source does not show criticism of what
a retained reflection says (condition 3).

**V3 (20): bounded-run positives.** Each shows stated theories, consumption,
and content-directed criticism with a retained record inside one
optimization run, research project, or investigation, and freezes or hands
off the product at the end.
`accelerating-scientific-research-gemini-real-world`,
`ecdysis-training-runtime-harnesses`, `harnessevolve-reference-trajectories`,
`modularrsi-generalizable-harness-self-improvement`,
`skillglow-procedural-family-consolidation`,
`skilllift-dense-rubrics-sparse-oracles`, `meta-n-recursive-self-improvement`,
`sift-self-improvement-fast-tree-search`, `repo-to-skill-disco-ai4ai-skills`,
`evoontology-self-evolving-ontology`, `sol-pi-efficient-agent-harness`,
`wikiskill-persistent-knowledge-for-skill-evolution`,
`meta-agent-challenge-autonomous-agent-development`,
`stellar-colosseum-many-agent-research-harness`,
`crux-open-ended-ai-research-paper`,
`dualgraph-knowledge-exploration-outline-structure`,
`hypothesis-evolution-protocol-auditable-ai-scientists`,
`socratic-agents-autonomous-scientific-discovery`,
`scientisttwo-autonomous-ai-research`,
`metr-hugging-face-incident-investigation`.

**V4 (6): old negatives whose gap was improvement or attribution.** Under
reading B, conditions 1, 2, and 4 hold and condition 3 is plausible, so the
verdict moves to "builder, at condition 3's evidence strength; learning
untested".
`aide2-recursive-self-improvement-research-agents` (evaluator repair and
stated reasons),
`primescientist-research-effort-allocation` (reflector states diagnosis and
rationale),
`merchantbench-long-term-coherence` (validated and rejected hypotheses in
memory),
`aspire-self-evolution-from-vague-goals` (harness arm only; the weight arm
fails condition 1),
`swarmworld-stigmergic-technological-evolution` (recorded hypotheses and a
tested controller change),
`combinatorial-sketching-finite-programs` (retained counterexamples refute
stated hole assignments; under B this would make counterexample-guided
synthesis a builder inside its run, which is a test of reading B).

**V5 (9): positive under either reading.** Retention reaches later tasks or
continuing practice.
`design-docs-are-all-you-need` (human document revision),
`prove2me-collaborative-math-formalization` (the platform's shared theorem
library; confirm it persists past the mission),
`eurisko-learns-new-heuristics-and-domain-concepts` (partial: much retention
runs on worth values),
`bounded-recursive-self-improvement` (AERA's continuing model set; now
stronger, since improvement no longer carries the verdict),
`long-horizon-agents-levels-ticks-cascaded-intelligence` (briefs and guards
across the campaign's tasks; confirm),
`discovery-foundation-models` (cross-task skills),
`rsiagent-autonomous-exploration` (memory bank across practice and target
tasks),
`flywheel-encoding-the-scientific-method` (conditional: a researcher's
practice), `introspective-multistrategy-learning` (partial).

**V6 (49): no flip.** Grouped by deciding condition.

- *Condition 1, weights or no localized content (11):*
  `concept-bottleneck-models-paper-v3` (concepts are partly localized, case
  29), `contextpilot-proactive-context-management`,
  `driven-by-compression-progress`,
  `dual-nature-generalization-on-policy-distillation`,
  `jepa-anything-predictive-models`,
  `lifefuse-mem-lifecycle-aware-state-fusion`, `locating-hidden-failures`,
  `locating-hidden-failures-paper`,
  `unexpected-benefits-self-modeling-neural-systems`,
  `reinforcement-learning-self-modifying-policies`,
  `shifting-inductive-bias-success-story-algorithm`.
- *Condition 3, criticism of content not shown, or a fixed theory (25):*
  `agent-memory-endogenous-authorization-laundering`,
  `chaff-engineering-an-efficient-sat-solver` (fixed theory, case 9),
  `gepa-reflective-prompt-evolution`, `gwern-design-of-this-website`,
  `longmemeval-benchmarking-chat-assistants-long-term-memory`,
  `memorylace-lifecycle-aware-consolidation-evidence-retrieval`,
  `optimal-ordered-problem-solver`,
  `procedural-graphs-self-evolving-execution`, `recursive-self-improvement`,
  `recursive-self-improvement-since-1987`, `rulemem-active-rule-memory`,
  `space-skill-guided-adaptive-action-chunking`,
  `upml-framework-for-knowledge-system-reuse`,
  `why-am-and-eurisko-appear-to-work`,
  `skill-acquisition-compilation-weak-method-solutions`,
  `form-not-content-placebo-controlled-self-repair`,
  `contextleak-agent-context-exfiltration`,
  `s3gym-self-testing-self-judging-self-improvement`,
  `i-reverse-engineered-instinct-s-memory-here-2101745550752428340`,
  `world-models-life-mind-continuity`, `skill-and-working-memory`,
  `past-bench-personal-agents-pdf`,
  `reflective-architecture-llm-based-systems-abstract`,
  `think-before-you-act-popperian-expectations-abstract`,
  `logic-of-theory-change-partial-meet-contraction`.
- *Condition 4, nothing retained past the episode (7):*
  `ai-scientists-results-without-scientific-reasoning`,
  `automated-hypothesis-validation-sequential-falsifications`,
  `competing-biases-llm-confidence`,
  `scaffold-not-vocabulary-popperian-code-generation-skill`,
  `selection-without-signal-recovery-through-expression`,
  `sound-agentic-science-requires-adversarial-experiments`,
  `automated-refinement-first-order-horn-clause-domain-theories` (FORTE, the
  draft's own exclusion).
- *No system verdict; commentary only (6):*
  `popper-conjectures-and-refutations`,
  `popper-epistemology-without-a-knowing-subject-1968`,
  `in-defense-of-base-contraction`,
  `error-centric-intelligence-beyond-observational-learning`,
  `generalization-adaptive-data-analysis-holdout-reuse`,
  `llms-scientific-method-hypothesis-to-discovery`.

Changes from the first inventory's predictions: `prove2me` does not flip
(shared library); `procedural-graphs` and `contextpilot` do not flip toward
membership (condition 3 and condition 1 decide); `s3gym` does not flip
(its tips are retained theories; its raw history is the case-4 baseline);
`in-defense-of-base-contraction` and the 1968 Popper ingest do not reverse,
because finer addressability is still not a condition.

**V7 (6): link only.** Follow D1 for the precedents and companion links:
`explanation-based-generalization-unifying-view`,
`explanation-based-generalization-unifying-view-2026-09-08`,
`rainbow-architecture-based-self-adaptation`,
`requirements-aware-systems-research-agenda`,
`requirements-reflection-runtime-entities`,
`theory-refinement-analytical-empirical-methods`.

### Ingests with specific edits beyond the verdict

| Ingest | Edit |
|---|---|
| `popper-conjectures-and-refutations` | Grounds condition 3 (critical method vs trial and error) and the Addressability section (locating the refuted hypothesis). Rewrite "supports a critical standard for conjectural learning" against the four conditions. |
| `popper-epistemology-without-a-knowing-subject-1968` | Now grounds condition 1 (descriptive language as a condition of criticism), condition 2, and the reflective qualifier. "Separating tentative status and conjectural learning from addressability" survives as "tentative status and builder membership from finer addressability". Retarget the follow-up. The open question about internal criticism without retained artifacts is answered by conditions 1 and 4. |
| `in-defense-of-base-contraction` | "Not a condition of conjectural learning" becomes "a design commitment above condition 1". No reversal. |
| `error-centric-intelligence-beyond-observational-learning` | Rewrite the description of the old definition; close the follow-up, which the reflective qualifier answers. |
| `s3gym-self-testing-self-judging-self-improvement` | Narrow "raw history can support reconstruction": trajectories alone are the case-4 baseline; the tips are the retained theories. |
| `contextleak-agent-context-exfiltration` | "Weight changes do not exclude" becomes the case-8 sense; recency replacement bears on condition 3. |
| `long-horizon-agents-levels-ticks-cascaded-intelligence` | The human-inside boundary wording survives (draft Boundary). |
| `discovery-foundation-models` | Keep the declared-boundary comparison with `theory-builder.md`. |
| `sound-agentic-science-requires-adversarial-experiments` | Repoint the externally tested link to the obligations note (D5). |
| `scientisttwo-autonomous-ai-research` | Frontmatter `domains: [… conjectural-learning …]` becomes `theory-building` (follows D2). |
| `llms-scientific-method-hypothesis-to-discovery` | "Reflective theory builder" per the qualifier; close or retarget the follow-up. |
| `automated-refinement-first-order-horn-clause-domain-theories` | Repoint "our account of theory use" to `theory-builder.md#exclusions`. |
| `socratic-agents-autonomous-scientific-discovery`, `automated-hypothesis-validation-sequential-falsifications` | Retarget their follow-ups ("review the definition against …") to `theory-builder.md` or close them. |
| `generalization-adaptive-data-analysis-holdout-reuse` | "Guide conjectural learning" becomes "guide a theory builder's criticism". The externally tested definition's citation of it moves with the protocol to the testing article. |

## Frozen and workflow-owned records (F)

Per D6: keep bytes, rely on redirects; the concurrent batch runs on and its
output counts as frozen under the old wording.

| Path / set | Handling |
|---|---|
| `kb/reports/retained/theory-builder-boundary-cases-20260917.md` | Keep content. Repoint the links to the four retired definitions (unpublished, so no redirect helps). Its status sentence becomes historical. |
| `kb/reports/retained/README.md` | N |
| 27 matching `agentic-system-analysis/*/result.md` (one, `AAS-2026-09-23-arsumbris-02`, links `conjectural-learning.md`) | Byte-frozen; reviews pin them by hash. The redirect covers the one published link; the local checker will warn, as after 643508db. |
| 25 matching `kb/agentic-systems/reviews/*.md` (17 link `conjectural-learning.md`) | Keep bytes; the redirect covers the links. The old term stays until each system is re-analysed. |
| `kb/log.md` | Leave |

## Totals by category

At scan time (201 in scope, plus 1 test scenario outside):

| Category | Files | Contents |
|---|---|---|
| R | 6 | 1 replaced in place, 5 retired |
| S | 112 | 6 system-definition (incl. the test scenario), 1 definition, 10 notes, 6 articles and hubs, 2 workshop files, 87 ingests (V1–V6) |
| L | 23 | 1 definition, 7 notes, 2 articles and hubs (incl. `kb/index.md`), 7 workshop files, 6 ingests (V7) |
| F | 55 | 1 boundary report, 27 retained results, 25 reviews, `kb/log.md`, the retained README |
| N | 6 | 2 notes, 4 workshop files |

Ingest subtotal: 87 re-judged (V1–V6) plus 6 link only.

## Relocation map

| Retired section | Destination |
|---|---|
| old theory-builder: definition and contradictable consequences | Draft conditions 1–4; condition 3 ("tests of stated consequences") |
| old theory-builder: revision mode open, reconstruction, first theory | Draft condition 3 (whole rejection, large revision) and condition 4 (rebuilding from criticism) |
| old theory-builder: Boundary | Draft Boundary |
| old theory-builder: machinery list; WikiSkill three-layer instance | Dropped; the WikiSkill ingest keeps the example |
| old theory-builder: Seed | Testing article, "The hypotheses" (already defines seed) |
| old theory-builder: Evidence interface | Testing article, a short section with the evaluation protocol |
| old theory-builder: Persistence (lineage, intervention, total replacement) | Draft Boundary, identity paragraph. Intervention accounting: testing article, "Record what people contribute". The lineage question: obligations note, Open Questions (already there). |
| old theory-builder: "Persistence establishes neither retention nor learning"; regenerating builder | Dropped: condition 4 and "attempted, not guaranteed" cover them |
| old theory-builder: Extension (matched baseline, PAST-Bench) | Testing article, "The hypotheses"; add the matched-baseline rule |
| old theory-builder: Scope bullets on evaluation and interpretation | Testing article. "Deriving what it implies" stays a draft operation. |
| old theory-builder: exclusions on installation, use, improvement, outcome vs fidelity | Testing article; `an-action-model-matters-only-through-its-consumption-path` already carries consumption |
| old theory-builder: boundary cases FORTE, Gödel, note-review loop, total replacement | Draft Exclusions (FORTE), Boundary cases (Gödel, note-review loop), Boundary identity paragraph |
| old theory-builder: KB for a consuming project | Testing article, with the externally tested case's boundary cases |
| externally-tested: the three supplied items and why they matter | Obligations note, rewritten opening (D5): what a claim without external assessment must supply for itself, stated against the three items directly |
| externally-tested: "What remains for the general case" table | Obligations note (it is the note's own subject) |
| externally-tested: Scope (credit assignment, practical limits, degrees) | Obligations note, "Attribution beyond the observed outcome" and a short degrees paragraph |
| externally-tested: Exclusions and Misuse (internal review is not external; adaptable fixed benchmark; objective preservation; rejection is not refutation) | Obligations note; the adaptable-benchmark line goes to the testing article's protocol |
| externally-tested: Evaluation protocol (reserve, adaptive reuse, controls, no-retention condition) | Testing article, merged into "Start with controlled task families" (D5) |
| externally-tested: Investigation stays inside the main path | Obligations note, "What stays inside the main path" (already there); drop the duplicate |
| externally-tested: boundary cases (DGM, note-review loop, KB for a consuming project, Gödel) | Testing article, condensed; Gödel to the draft's Boundary cases |
| reflective: definition | Draft Qualifiers, Reflective |
| reflective: Evidence (connected path, matched interventions) | Testing article, before the Reflection hypothesis |
| reflective: Scope (independence from learning, autonomy, extension) | Draft "qualifiers are independent" and "attempted, not guaranteed"; extension to the testing article |
| reflective: "a self-theory's acceptance is not warrant" | `machinery-persists-by-warrant-not-position-in-a-reflective-loop.md` (already says it) |
| reflective: boundary cases | Draft Qualifiers closing line; Boundary cases |
| autonomous: definition, users outside | Draft Qualifiers, Autonomous; Boundary |
| autonomous: per-role reporting, seed vs interventions | Testing article, "Record what people contribute" |
| autonomous: not reliability | One line in the draft; the warranted-autonomy note |
| autonomous: not objective governance | Obligations note, second obligation |
| conjectural-learning: conditions | Draft conditions 1–3 |
| conjectural-learning: Simon's criterion, attempt vs learning | Draft "Error elimination is attempted"; `learning-is-not-only-about-generality.md` |
| conjectural-learning: persistence; reconstruction from criticisms | Draft condition 4 (D3) |
| conjectural-learning: Relation to Popper table | Dropped; the draft speaks in Popper's terms, and the amoeba contrast is its gradient-descent paragraph |
| conjectural-learning: Scope bullets | Observer access and persistence: skill, type, ingest instruction (already there). Faultless theory: `a-complete-theory-path…`. Addressability: draft Addressability section. "Revision need not be small": draft condition 3 (D8, done). Subject and machinery: reflective qualifier. |
| conjectural-learning: Exclusions | Draft Exclusions. Research community: Boundary cases. Proof-only: Gödel note. Input/outcome records: companion and proposal notes as the case-4 baseline. |
| conjectural-learning: Misuse (criticism vs selection) | Draft Exclusions, black-box line |
| conjectural-learning-checks | Replaced by `theory-builder-checks.md` (D4) |
| (ideal-interpreter) "retention is the builder's, not the interpreter's" | Draft Boundary (D8, done) |

## Candidate titles

**D1, three notes** (claim titles; `kb/notes/COLLECTION.md`). All retitles go
through `commonplace-relocate-note`, one pure commit each.

| Current | Proposed | Alternative |
|---|---|---|
| Commonplace studies conjectural learning through retained theories | Commonplace builds a theory builder and tests whether it learns | Commonplace tests whether a theory builder learns |
| Conjectural learning has distinct epistemic, structural, and implementation precedents | Theory building has distinct epistemic, structural, and implementation precedents | A theory builder has distinct epistemic, structural, and implementation precedents |
| Rules, weights, and missing rationale do not settle conjectural learning | Missing rationale does not exclude a theory builder, but weight-only retention does | Rules without rationale can meet the theory-builder conditions; retained weights alone cannot |

The first reverses the companion's claim, as the README expects. The third
records the Apodex flip in the title.

**D2, article series** (headlines, not claims; `kb/articles/COLLECTION.md`).
Renamed paths get redirects through `commonplace-relocate-note`.

| Path | Current headline | Proposed headline | Proposed path |
|---|---|---|---|
| `conjectural-learning-with-fixed-models.md` | Conjectural Learning with Today's LLMs | Building a Theory Builder from Today's LLMs | `theory-builders-with-fixed-models.md` |
| `testing-the-conjectural-learning-program.md` | Testing Conjectural Learning | Testing Whether a Theory Builder Learns | `testing-whether-a-theory-builder-learns.md` |
| `an-automated-software-house-as-a-second-test-of-conjectural-learning.md` | An Automated Software House as a Second Test of Conjectural Learning | An Automated Software House as a Second Test of a Theory Builder | `an-automated-software-house-as-a-second-test-of-a-theory-builder.md` |
| `nearest-existing-constructions-to-a-witness-house.md` | How existing self-improving systems relate to conjectural learning | Which Existing Self-Improving Systems Are Theory Builders | unchanged |
| `bootstrapping-an-autonomous-theory-builder.md` | Bootstrapping a Fully Automated Learner with Commonplace | Bootstrapping an Autonomous Theory Builder with Commonplace (optional; description changes either way) | unchanged |

The `scientisttwo` domain tag becomes `theory-building`.

## Edit order (README step 4)

1. **Receiving sections.** Add to the testing article: evidence interface
   and evaluation protocol, seed and extension with the matched-baseline
   rule, intervention accounting, reflective evidence, and the condensed
   boundary cases. Rewrite the obligations note's opening and add the
   externally tested items it now owns (D5). Everything retired has a home
   before anything is deleted.
2. **Definitions.** Install the draft as `theory-builder.md` and promote
   `theory-builder-checks.md` (D4). Edit `addressable-theory.md` and
   `tentative-theory.md`.
3. **Skills and types.** `AGENTS.md`, the ingest instruction (with the N1
   reading), the analyse skill, the result type, the agentic-systems
   `COLLECTION.md`, and the test scenario; run `uv run pytest`. The
   concurrent batch keeps running (D6).
4. **Notes and articles.** Content edits to the D1 notes, the other S notes,
   the series articles, and the hubs, at their current paths.
5. **Ingest re-judging (D7).** Batches below; B1 first, since the Popper
   ingests ground the definition.
6. **Links and redirects.** Run `commonplace-relocate-note` for the D1 and D2
   retitles, one pure commit each. Then the L rows, `kb/index.md`, and the
   workshops. Delete the five retired definitions, add their redirects,
   retarget the three existing entries, flatten chains, and retire their
   freshness baselines.
7. **Frozen records last.** Repoint the boundary report's links. Leave reviews
   and retained results byte-frozen (D6).
8. **Validate.** `commonplace-validate` on the touched collections,
   `commonplace-validate redirects`, and the scan above. Remaining hits
   should be F records only.

### Delegation batches for ingest re-judging

Each batch is one sub-agent (Opus per the bulk fan-out convention), with
disjoint files. Each gets: the draft definition and checks, this section's
rewrite rule, the f4dc912d edit boundary, the N1 reading chosen, and its
predicted verdicts to confirm or correct. Each returns a per-file line:
conditions met, deciding condition, learning claim, flip or not. B1 runs
first; B2–B7 can run in parallel. B5–B7 wait for N1.

| Batch | Focus | Files |
|---|---|---|
| B1 (11) | Grounding, frameworks, surveys, abstracts | `popper-conjectures-and-refutations`, `popper-epistemology-without-a-knowing-subject-1968`, `in-defense-of-base-contraction`, `error-centric-intelligence-beyond-observational-learning`, `generalization-adaptive-data-analysis-holdout-reuse`, `llms-scientific-method-hypothesis-to-discovery`, `logic-of-theory-change-partial-meet-contraction`, `recursive-self-improvement`, `recursive-self-improvement-since-1987`, `think-before-you-act-popperian-expectations-abstract`, `reflective-architecture-llm-based-systems-abstract` |
| B2 (12) | Weights and non-localized state (condition 1) | `concept-bottleneck-models-paper-v3`, `contextpilot-proactive-context-management`, `driven-by-compression-progress`, `dual-nature-generalization-on-policy-distillation`, `jepa-anything-predictive-models`, `lifefuse-mem-lifecycle-aware-state-fusion`, `locating-hidden-failures`, `locating-hidden-failures-paper`, `unexpected-benefits-self-modeling-neural-systems`, `reinforcement-learning-self-modifying-policies`, `shifting-inductive-bias-success-story-algorithm`, `competing-biases-llm-confidence` |
| B3 (13) | Memory and rule stores (condition 3) | `agent-memory-endogenous-authorization-laundering`, `chaff-engineering-an-efficient-sat-solver`, `longmemeval-benchmarking-chat-assistants-long-term-memory`, `memorylace-lifecycle-aware-consolidation-evidence-retrieval`, `rulemem-active-rule-memory`, `i-reverse-engineered-instinct-s-memory-here-2101745550752428340`, `past-bench-personal-agents-pdf`, `gwern-design-of-this-website`, `upml-framework-for-knowledge-system-reuse`, `contextleak-agent-context-exfiltration`, `s3gym-self-testing-self-judging-self-improvement`, `skill-and-working-memory`, `skill-acquisition-compilation-weak-method-solutions` |
| B4 (13) | Program and prompt search, episode-bound agents (conditions 3 and 4) | `gepa-reflective-prompt-evolution`, `optimal-ordered-problem-solver`, `procedural-graphs-self-evolving-execution`, `space-skill-guided-adaptive-action-chunking`, `why-am-and-eurisko-appear-to-work`, `form-not-content-placebo-controlled-self-repair`, `world-models-life-mind-continuity`, `scaffold-not-vocabulary-popperian-code-generation-skill`, `selection-without-signal-recovery-through-expression`, `ai-scientists-results-without-scientific-reasoning`, `automated-hypothesis-validation-sequential-falsifications`, `sound-agentic-science-requires-adversarial-experiments`, `automated-refinement-first-order-horn-clause-domain-theories` |
| B5 (12) | Bounded-run optimizers (V3, part 1) | `accelerating-scientific-research-gemini-real-world`, `ecdysis-training-runtime-harnesses`, `harnessevolve-reference-trajectories`, `modularrsi-generalizable-harness-self-improvement`, `skillglow-procedural-family-consolidation`, `skilllift-dense-rubrics-sparse-oracles`, `meta-n-recursive-self-improvement`, `sift-self-improvement-fast-tree-search`, `repo-to-skill-disco-ai4ai-skills`, `evoontology-self-evolving-ontology`, `sol-pi-efficient-agent-harness`, `wikiskill-persistent-knowledge-for-skill-evolution` |
| B6 (11) | Bounded-run research agents (V3 part 2, V1, V2) | `meta-agent-challenge-autonomous-agent-development`, `stellar-colosseum-many-agent-research-harness`, `crux-open-ended-ai-research-paper`, `dualgraph-knowledge-exploration-outline-structure`, `hypothesis-evolution-protocol-auditable-ai-scientists`, `socratic-agents-autonomous-scientific-discovery`, `scientisttwo-autonomous-ai-research`, `metr-hugging-face-incident-investigation`, `gavel-graph-world-models`, `falsifybench-rule-discovery-games-full-text`, `reflexion-verbal-reinforcement-learning` |
| B7 (15) | Flip-in candidates and continuing positives (V4, V5) | `aide2-recursive-self-improvement-research-agents`, `primescientist-research-effort-allocation`, `merchantbench-long-term-coherence`, `aspire-self-evolution-from-vague-goals`, `swarmworld-stigmergic-technological-evolution`, `combinatorial-sketching-finite-programs`, `design-docs-are-all-you-need`, `prove2me-collaborative-math-formalization`, `eurisko-learns-new-heuristics-and-domain-concepts`, `bounded-recursive-self-improvement`, `long-horizon-agents-levels-ticks-cascaded-intelligence`, `discovery-foundation-models`, `rsiagent-autonomous-exploration`, `flywheel-encoding-the-scientific-method`, `introspective-multistrategy-learning` |

The 6 V7 ingests go with the link pass in step 6.

## Decisions for the operator

D1–D8 are settled and appear above as plan steps. New:

- **N1. Where does a run end for condition 4?** The draft excludes "one
  invocation of a refinement procedure such as FORTE" and a theory discarded
  after reasoning. It does not say whether rounds inside one bounded run
  count as later work. FORTE also iterates over a retained theory, so the
  exclusion cannot rest on iteration alone. 26 ingests (V3, V4), several
  survey systems, and the skill's guidance depend on the answer.
  - *Reading A (literal):* retention must outlast the run that produced it
    and be consumed by the system's later criticism. Bounded optimizers and
    single research runs are "a builder-shaped procedure run once"; a system
    that carries their archive into later runs would be inside. V3 flips
    out (20). Consistent with case 6 and FORTE as written.
  - *Reading B (record-based):* a run meets condition 4 when later rounds
    consume a retained store of theories and criticisms (an archive,
    library, or files), not merely a reasoning context or conversation
    history. FORTE stays outside because it keeps only its current theory,
    no record of criticism. V4 flips in (6). The draft's FORTE sentence
    and case 24 would state that ground. Counterexample-guided synthesis
    (`combinatorial-sketching`) then counts as a builder within its run.
  - Either way the draft's Exclusions and checks case 24 should state the
    chosen reading.
- **N2. Approve the D1 titles** (table above), including the evidence note's
  Apodex flip, which follows from the draft's weight-only exclusion.
- **N3. Approve the D2 headlines and paths** (table above), including
  whether the bootstrapping headline changes.
