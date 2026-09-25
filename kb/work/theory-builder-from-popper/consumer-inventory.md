# Consumer inventory: theory-builder migration

Step 2 of this workshop. Nothing in the library changes until the operator
approves an edit plan built from this list.

## How this was built

Scan of 2026-09-25 over `kb/` and `AGENTS.md`, excluding
`kb/reports/cache/**`, `kb/reports/state/**`, `kb/sources/.snapshots/**`, and
this workshop:

```bash
rg -l -i -e 'theory[- ]builders?' -e 'conjectural[- ]learn' \
   -e 'theory-builder\.md' -e 'conjectural-learning' kb AGENTS.md \
   --glob '!kb/reports/cache/**' --glob '!kb/reports/state/**' \
   --glob '!kb/sources/.snapshots/**' --glob '!kb/work/theory-builder-from-popper/**'
```

- **198 files** matched at scan time.
- Links to the target definitions, counted as files that link to each:

  | File | Linking files |
  |---|---|
  | `conjectural-learning.md` | 131 (86 ingests, 17 reviews, 1 retained result, 27 others) |
  | `theory-builder.md` | 14 |
  | `externally-tested-theory-builder.md` | 9 |
  | `reflective-theory-builder.md` | 7 |
  | `autonomous-theory-builder.md` | 7 |
  | `conjectural-learning-checks.md` | 1 (the definition itself) |

- **Moving target.** Another session is running an `analyse-agentic-system`
  batch. Most of its outputs are untracked (`??`): about 24 reviews and their
  retained results. The reviews directory grew from 24 to 25 matching files
  during this scan (`aide2.md` appeared). Rerun the scan before applying.
- Three files outside the scan scope also carry the old terms:
  `tests/scenarios/ingest-a-source.md` (names `conjectural-learning.md` as a
  required read), `properdocs.yml` (redirects), and the root `README.md` (links
  the bootstrapping article by path).

Category codes: **F** frozen or historical, **L** link-only, **S**
substantive, **N** no edit needed, **R** a target definition itself.

## Semantic shifts every rewrite must check

Each substantive consumer rests on one or more of these shifts.

1. **Criticism becomes required.** The old builder did not require
   criticism. A consumer that calls a system a builder only because it is
   persistent and responsible for theories may now be wrong.
2. **No success condition.** The old conjectural learning required improved
   capacity. The new builder does not. A system with formulated, consumed,
   criticized, retained, and addressable theories but no shown improvement
   was "conjectural learning not established". Under the new definition it
   *is* a theory builder, and whether it learned stays open. Verdicts can
   therefore flip toward membership as well as away from it.
3. **Retention and addressability become conditions.** The old conjectural
   learning admitted whole replacement, reconstruction from retained
   criticisms, and theories built during reasoning and then discarded. The new
   builder excludes whole replacement (condition 5) and single runs without
   retention (condition 4). Many consumers say the opposite in so many words:
   "a condition of conjectural learning", "whole replacement can qualify",
   "reconstruction can support".
4. **"Learning" becomes ordinary English** in Simon's sense. Where a
   consumer says "does not establish conjectural learning", the rewrite must
   say which claim failed. If membership failed, name the builder condition.
   If only the improvement failed, the claim is "does not establish
   learning".
5. **Reflective and autonomous become qualifiers.** The old definitions
   treated them as builder conditions, independent of learning. The new
   reflective qualifier puts the causal connection through consumption and
   criticism (conditions 2 and 3). It states that the connection is not kept
   up automatically. The old definition required a two-way connection where
   "changes in the machinery update the theory". Consumers that rely on the
   two-way wording are the analyse skill's Reflection bullet, the result
   type, and `a-complete-theory-path…`. Check them.
6. **Seed, extension, evidence interface, and intervention accounting leave
   the definition.** Consumers that cite them by definition anchor must
   repoint to their new home.

Old checks cases that flip under the draft (from
`conjectural-learning-checks.md`):

| Case | Old class | New class |
|---|---|---|
| 2: prose theory replaced whole | Inside | Outside (condition 5) |
| 3: theory rebuilt from retained criticisms | Inside | Unclear. Condition 4 retains "theories and the record of their criticism"; see decision D3 |
| 6: theory built while reasoning, then discarded | Inside if capacity improved | Outside (condition 4) |
| any inside case without improvement | "Attempt to learn" | Inside; learning is a separate claim |

Cases 1, 5, 7, 9, 10, 12, and 14 keep their class. Cases 11, 15, and 16 stay
inside only if condition 3's "working process" covers a process that has not
yet run (case 15).

## Target definitions (R)

| Path | Action |
|---|---|
| `kb/notes/definitions/theory-builder.md` | Replace with the draft, in place. The path is unchanged, so its 14 inbound links survive. Review each link's anchor and label (see L rows). |
| `kb/notes/definitions/conjectural-learning.md` | Retire (delete) and add a redirect to `theory-builder.md` |
| `kb/notes/definitions/conjectural-learning-checks.md` | Retire, or rewrite as `theory-builder-checks.md`. Decision D4. |
| `kb/notes/definitions/reflective-theory-builder.md` | Retire; redirect to `theory-builder.md` |
| `kb/notes/definitions/autonomous-theory-builder.md` | Retire; redirect to `theory-builder.md` |
| `kb/notes/definitions/externally-tested-theory-builder.md` | Retire; redirect to the section that receives it (D5) |

Redirects: `commonplace-relocate-note` writes a ProperDocs redirect only when
it moves a note. Deletion is not a relocation, so the five retirements need
hand-added `redirect_maps` entries in `properdocs.yml`. The precedent is
643508db, which retired `theory-refinement.md`. Three existing entries point
at `conjectural-learning.md`: `learning-by-theory-refinement`,
`theory-mediated-learning`, and `theory-refinement`. They must be retargeted,
because the map must stay flat. Any retitle below goes through
`commonplace-relocate-note`, which adds its own redirect. Existing chains
into a retitled path must also be flattened, for example the 22 article
redirects to the four article paths named for conjectural learning and the
5 note redirects to the precedents and evidence notes. Check with `commonplace-validate redirects`.
Redirects cover only the published site. `kb/reports/**` is not published,
except `agentic-system-analysis/**/result.md`, and the local link checker
does not follow redirects.

Freshness baselines keyed to the retired definitions should be retired too,
as 643508db did.

## System-definition artifacts (drive ingest and review usage)

| Path | Uses | Cat | Proposed edit |
|---|---|---|---|
| `AGENTS.md` | Vocabulary: *Conjectural learning*, *Externally tested theory builder*, *Theory builder*; *Addressable theory* says "conjectural learning does not require it, a theory builder does" | S | Delete the conjectural-learning and externally-tested entries. Replace the theory-builder entry with the five conditions, no success condition, and the two qualifiers. In *Addressable theory*, drop the conjectural-learning clause (a builder requires it: condition 5). The conjectural-learning entry records the 2026-09-21 replacement; this migration reverses that, and the commit body should say so. |
| `kb/instructions/assess-learning-claims-during-ingest.md` | Loads `conjectural-learning.md` as "the current comparison basis for learning membership" | S | Load `theory-builder.md` instead. Procedure step 3 gains one sentence: judge the source condition by condition against the five conditions, each at its own evidence strength, and judge learning (improved capacity, Simon) as a separate empirical claim. Keep "leave unresolved mappings explicit". The addressable-theory read becomes conditional only on depth, since addressability is now condition 5. |
| `kb/instructions/analyse-agentic-system/SKILL.md` | Step-3 bullets: *Criticism*, *Conjectural learning*, *Addressability and retention*, *Reflection* ("a reflective theory builder additionally…"); completion check (l. 530); footer `rests-on` link | S | Map as below. |
| `kb/types/agentic-system-analysis-result.md` | ll. 250–285 mirror the skill: "conjectural-learning claim", "Whole replacement and reconstruction do not by themselves exclude learning", "reflective-builder claim" | S | Same mapping as the skill; keep the `trace_learning` axis text, retargeting "does not establish conjectural learning" to "does not establish learning". |
| `kb/agentic-systems/COLLECTION.md` | l. 62: "These establish conjectural learning…"; "whole replacement or reconstruction can qualify" | S | Say that the pathway findings establish builder conditions 1–3, that retention and addressability are conditions 4–5, and that improved capacity is a separate learning claim. Delete "whole replacement or reconstruction can qualify". |
| `tests/scenarios/ingest-a-source.md` (outside scope) | Names `conjectural-learning.md` as required read | S | Follow the ingest instruction. This is a test-scenario file, so run `uv run pytest` afterwards. |

**Skill and type mapping onto the five conditions.** The skill already
records a theory route claim by claim. The change regroups those claims
rather than adding work.

| Current skill finding | New home |
|---|---|
| Formulation ("formulated in natural or formal language") | Condition 1, objective knowledge |
| Operative use ("which decisions depend on that content") | Condition 2, consumption |
| Criticism (content-directed; a score selecting variants does not count) | Condition 3; unchanged wording |
| Retention ("record separately what persists") | Condition 4. It becomes a membership condition. "Reconstruction can support" is deleted (pending D3). |
| Addressability (degree and boundary) | Condition 5. It becomes a membership condition, still recorded as a degree with a boundary. "Whole replacement … can support conjectural learning" is deleted. |
| *Conjectural learning* bullet (improved capacity, attribution, persistence) | Split. **Theory-builder membership** is the conjunction of 1–5, each with its own conclusion status and never inferred from neighbours. **Learning** is the improved-capacity claim, kept as is (capacity, assessment boundary, evidence, attribution, persistence), in ordinary words. |
| *Reflection* bullet, "reflective theory builder additionally revises a self-theory" | Reflective qualifier: method texts meet 1–5 and criticism tests them against records of the builder's own operation. Keep the separate `reflective-system` finding (causal self-representation) as is. Add the autonomous qualifier as a role-by-role record, which the skill already keeps under "decision roles". |
| "Rationale and criticism are separate"; opacity rule; "revision selection prefers reach" | Unchanged |

The retained results already use conclusion-status labels such as
"Conjectural learning has conclusion status uninspected" and "Reflective
theory-builder conclusion status". New runs would instead report
"theory-builder conditions 1–5" plus "learning". No schema field names
change. The type has no enumerated field for these claims; they are
free-text labels.

## Definitions and notes

| Path | Uses | Cat | Proposed edit |
|---|---|---|---|
| `kb/notes/definitions/addressable-theory.md` | "Conjectural learning does not require it"; footer `extends` | S | Say a theory builder requires it (condition 5), and that the expected benefit of localization is still an empirical claim. Repoint the footer to `theory-builder.md` (`defined-in` or `extends`). |
| `kb/notes/definitions/tentative-theory.md` | "Conjectural learning covers only the formulated ones"; footer | L | Change to "a theory builder's theories are the formulated ones (condition 1)"; repoint the footer |
| `kb/notes/commonplace-studies-conjectural-learning-through-retained-theories.md` | Title; "The definition states when the term applies"; "does not add a membership condition"; "The broader definition also admits reconstruction… Our choice is one arrangement within it"; Three conjectures ("Both arrangements can be conjectural learning") | S **DECISION** | The note's frame, a research choice inside a broader definition, reverses: retention and addressability are now definitional. Rewrite so that Commonplace studies whether a theory builder learns. Recast the addressability and efficiency conjectures as builder vs named non-builder baselines (whole-replacement, trace-reconstruction). The draft's Exclusions already name these baselines. Retitle (D1). |
| `kb/notes/conjectural-learning-has-distinct-precedents.md` | Title; "Conjectural learning names…"; footer | S **DECISION** | Restate as precedents for the theory builder's operations. Check whether any precedent was admitted only because whole replacement or discard counted (EBG, FORTE, Rainbow). Retitle (D1). |
| `kb/notes/evidence/rules-weights-and-missing-rationale-do-not-settle-conjectural-learning.md` | Title and description | S **DECISION** | The claim survives: missing rationale or parametric storage alone does not settle membership. Retarget it to "do not settle theory-builder membership". Retitle (D1). |
| `kb/notes/retained-theories-may-improve-sample-efficiency.md` | "Retention and addressability are chosen treatments…"; "Conjectural learning also admits whole replacement…"; footer "membership does not require retained addressable theories" | S | The contrast reverses. The retained-theory arm is now what a builder is; the conjecture is that a builder beats named non-builder arrangements. Rewrite those sentences and the footer. |
| `kb/notes/proposals/retained-theories-compared-with-retained-traces-under-resource-limits.md` | "The reconstruction may itself be conjectural learning"; footer | S | The trace-reconstruction arm is a named non-builder baseline (condition 4) that may still learn in the ordinary sense. Rewrite those lines. The proposal's comparison is unchanged. |
| `kb/notes/a-complete-theory-path-does-not-establish-improved-capacity.md` | Opening defines the further result as conjectural learning; l. 161 "Retaining an addressable theory is … not a condition of conjectural learning"; reflective paragraph | S | Keep the claim: a complete path does not establish improved capacity. Say "learning" for the improvement. Delete or reverse l. 161, since retention and addressability are builder conditions. Check the reflective paragraph against shift 5. |
| `kb/notes/open-ended-theory-learning-and-factory-learning-close-the-same.md` | "retention and recurrence are not universal conditions of conjectural learning"; proof-only case | S | Reverse: retention is a builder condition, and learning is the separate claim. Proof-only: "does not establish a theory builder (condition 3)". |
| `kb/notes/a-claim-without-external-assessment-carries-three-obligations.md` | Opens by contrast with the externally tested theory builder; footer grounds on the evidence interface and the lineage question | S | Repoint to the new home of the externally tested case (D5). If D5 picks this note as the home of the three supplied items and the "what remains" table, fold them in here. The lineage question survives only as the draft's short identity paragraph. |
| `kb/notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md` | Section "comparison with a theory builder"; table column; "develops and revises tentative theories of external subjects and of its own machinery" | S | Light. "Of its own machinery" is now the reflective qualifier, so say "a reflective theory builder". The classification stays open, as in the draft. |
| `kb/notes/theory-and-capacity-building-make-the-same-kind-of-commitment.md` | Heading "Conjectural learning is one causal path…"; body | S | Light. Retitle the heading as "Theory building is one causal path…"; the claim holds. |
| `kb/notes/disconnected-witnesses-do-not-establish-a-causal-path-through-theory.md` | "establishes conjectural learning only when … improves capacity"; footer | L | Change to "establishes learning only when…"; repoint the footer to `theory-builder.md` |
| `kb/notes/an-optimal-long-run-learning-strategy-invests-in-its-own-machinery.md` | Links reflective and autonomous definitions | L | Repoint to `theory-builder.md#qualifiers`. "Reflection separated from successful learning" still holds. |
| `kb/notes/factory-construction-does-not-establish-knowledge-acquisition.md` | "can be driven by conjectural learning, program search…" | L | Say "by a theory builder's conjecture and criticism"; repoint |
| `kb/notes/bitter-lesson-selects-against-unearned-reach-not-against-structure.md` | Links the definition and the companion by title | L | Repoint; follow the companion retitle |
| `kb/notes/learning-theory-README.md` | Index entry for the conjectural-learning definition and the companion | L | Replace with a theory-builder entry; follow retitles |
| `kb/notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md`, `kb/notes/factory-learning-mechanisms-should-be-compared-on-the-same-causal-job.md` | Companion link only | L | Follow the retitle |
| `kb/notes/a-fixed-model-house-must-retain-missing-procedures-for-theory-use.md`, `kb/notes/an-open-domain-theory-builder-becomes-a-software-house-when-new-domains-require-production-machinery-changes.md` | "theory builder" in a title or description only; the sense fits the new definition | N | none |

## Articles and hubs

| Path | Uses | Cat | Proposed edit |
|---|---|---|---|
| `kb/articles/testing-the-conjectural-learning-program.md` | Title; `source_notes` lists all five target definitions; "this conjectural learning rather than caching"; links the externally tested definition as "externally fixed answer" and the autonomous one as "external role"; "The hypotheses" section defines builder, seed, and extension | S **DECISION** | Receives the apparatus (map below). Replace the in-article builder definition ("the persistent system responsible for…") with the new one. Keep the three hypotheses verbatim, since they are quoted "as adopted" 2026-09-17. Check that "builder" in them still reads correctly now that criticism is required. Update `source_notes`. Title per D2. |
| `kb/articles/conjectural-learning-with-fixed-models.md` | Title; "We call a system that implements this cycle a conjectural learner"; "The knowledge base … calls the process conjectural learning and the persistent system … a theory builder"; links the autonomous definition; final "definition states exactly what the paradigm requires" | S **DECISION** | The article's informal learner already matches the new builder: it formulates, criticizes, retains, and changes later behaviour. Rewrite the mapping sentence to "the knowledge base calls this system a theory builder". Point the autonomous link to the qualifier and the closing sentence to `theory-builder.md`. "Conjectural learning is a distinct learning paradigm" can stay as informal wording or go (D2). |
| `kb/articles/bootstrapping-an-autonomous-theory-builder.md` | Description "fully automated conjectural learner"; links the reflective and autonomous definitions; `source_notes` | S | Light. Repoint to `#qualifiers`. The wording follows D2. The filename already says "theory builder". |
| `kb/articles/nearest-existing-constructions-to-a-witness-house.md` | Title "How existing self-improving systems relate to conjectural learning"; "What the comparison asks" restates the old definition, including "can persist … in criticisms from which the theory is reconstructed"; "Establishing conjectural learning additionally requires…" | S **DECISION** | Replace the criterion paragraph with the five conditions plus the separate learning claim. Re-check the placement of each of the 18 systems for shift 2 (members without shown gains) and shift 3 (whole replacement, reconstruction). Title per D2. |
| `kb/articles/an-automated-software-house-as-a-second-test-of-conjectural-learning.md` | Rewrite plan; frontmatter lists the externally tested definition; "Why it is a test of conjectural learning" | S | Light. Retarget the frontmatter input to the externally tested case's new home. The title follows D2. It is a plan, so its "open choices" can absorb the rest. |
| `kb/articles/what-an-automated-reviewer-should-measure.md` | `source_notes` lists `conjectural-learning.md`; links the lead by title | L | Swap the source note for `theory-builder.md`; follow the lead's title |
| `kb/articles/README.md` | Entries describe the "conjectural learner" and the series titles | S | Light. Follows D2 and the retitles. |
| `kb/index.md` | Links three articles by path and text | L | Follow retitles |
| `kb/log.md` | Historical entries name the lead's path and the closed workshop | F | Leave as is; it is a log |

## Workshops (in flight; edits allowed, owners unaffected otherwise)

| Path | Uses | Cat | Proposed edit |
|---|---|---|---|
| `kb/work/ideal-interpreter/resource-bounded-ideal-interpreter.md` | Rests on the old builder: "interpretation as a role inside the builder, and retention as the builder's rather than the interpreter's" | S | Light. Interpretation survives in the draft's list of operations ("deriving what it implies"). "Retention is the builder's, not the interpreter's" is dropped from the draft; either restore one sentence in the Boundary or restate it in the workshop. |
| `kb/work/theory-refinement-interface/README.md`, `…/theory-refinement-interface.md` | "interface separate from conjectural-learning membership"; definition links | S | Light. Say "separate from theory-builder membership"; repoint |
| `kb/work/first-downstream-run/commonplace-evidence-protocol.md` | Links the externally tested definition; testing article by path | L | Repoint to the externally tested case's new home (D5); follow D2 |
| `kb/work/first-downstream-run/README.md` | Links `testing-…#the-first-arrangement-and-its-protocol`, an anchor that does not exist in the current article; the boundary report; the hypotheses | L | Follow D2. Fix the dead anchor while there. |
| `kb/work/ideal-interpreter/README.md` | Links `theory-builder.md` for "records a…" | L | Check the anchor still fits the new text |
| `kb/work/operator-led-article-clarification/README.md`, `kb/work/explanatory-theories-deployment-time-learning/exo-case.md` | Lead link by title; "do not establish conjectural learning or improved capacity" | L | Follow D2; say "learning" |
| `kb/work/commonplace-nearest-constructions/{README,landscape}.md`, `kb/work/README.md`, `kb/work/unattended-processing-failure-modes/catalogue.md` | "human-inclusive" and "computational theory builder", which match the new qualifiers; the article path as a record | N | none, unless D2 retitles; the catalogue records a historical path |

## Source ingests (93 files: 86 link the definition, 7 do not)

The precedent is f4dc912d. The earlier migration rewrote the Commonplace
commentary in 43 ingests and repaired links in 18 more. It kept source-native
terms, summaries, provenance, and quotes unchanged. The same rule applies
here. Edits touch only the `Learning Claims (our opinion)` section, the
footer links, and follow-up lines. The `snapshot_sha256` never changes.

**Group A: precedent or companion link only (6, L).** These follow the
retitles (D1) and need no change of meaning:
`explanation-based-generalization-unifying-view`,
`explanation-based-generalization-unifying-view-2026-09-08`,
`rainbow-architecture-based-self-adaptation`,
`requirements-aware-systems-research-agenda`,
`requirements-reflection-runtime-entities`,
`theory-refinement-analytical-empirical-methods`.

**Group N: negative or unestablished verdict (40, S, templated).** The
pattern is "X does not establish conjectural learning because …" or "only a
partial mapping", plus a footer `defined-in` link. Rewrite rule: split the
reason. If it names missing formulation, consumption, or criticism, write
"does not establish a theory builder (condition n)". If it names missing
improvement or attribution, write "does not establish learning". If it
names both, write both. Watch for shift 2: a system that failed only on
improvement may now meet all five conditions. These are the files where that
is possible (the gap named is attribution or improvement, not criticism):
`merchantbench`, `aide2`, `swarmworld`, `contextpilot`; the same holds for
`procedural-graphs` and `sift` in group P and for the `gbrain-garrytan`
review. The list is a sample; confirm per file at edit time. Files:
agent-memory-endogenous-authorization-laundering, aide2-recursive-self-improvement-research-agents,
ai-scientists-results-without-scientific-reasoning, aspire-self-evolution-from-vague-goals,
chaff-engineering-an-efficient-sat-solver, competing-biases-llm-confidence,
concept-bottleneck-models-paper-v3, contextpilot-proactive-context-management,
driven-by-compression-progress, dual-nature-generalization-on-policy-distillation,
form-not-content-placebo-controlled-self-repair, gepa-reflective-prompt-evolution,
gwern-design-of-this-website, introspective-multistrategy-learning,
jepa-anything-predictive-models, lifefuse-mem-lifecycle-aware-state-fusion,
locating-hidden-failures, locating-hidden-failures-paper,
logic-of-theory-change-partial-meet-contraction,
longmemeval-benchmarking-chat-assistants-long-term-memory,
memorylace-lifecycle-aware-consolidation-evidence-retrieval,
merchantbench-long-term-coherence, optimal-ordered-problem-solver,
past-bench-personal-agents-pdf, primescientist-research-effort-allocation,
recursive-self-improvement, recursive-self-improvement-since-1987,
reflective-architecture-llm-based-systems-abstract,
reinforcement-learning-self-modifying-policies, rulemem-active-rule-memory,
scaffold-not-vocabulary-popperian-code-generation-skill,
selection-without-signal-recovery-through-expression,
shifting-inductive-bias-success-story-algorithm,
skill-acquisition-compilation-weak-method-solutions, skill-and-working-memory,
space-skill-guided-adaptive-action-chunking,
swarmworld-stigmergic-technological-evolution,
unexpected-benefits-self-modeling-neural-systems,
upml-framework-for-knowledge-system-reuse, why-am-and-eurisko-appear-to-work.

**Group P: positive or plausible verdict (30, S).** The pattern is "a
plausible instance of", "consistent with", "fits the mechanism of", or
"ingredients of" conjectural learning. Rewrite rule: say which builder
conditions the source shows, keeping the evidence level, and keep the
learning claim separate. Shift 3 can flip these. Condition 4 fails when the
conjecture and criticism happen inside one run or episode with nothing
retained for later work. Condition 5 fails when theories are only replaced
whole. Likely re-verdicts, to confirm at edit time: `prove2me` (one proof
episode), `crux-open-ended-ai-research-paper` (trajectories within runs),
`metr-hugging-face-incident-investigation` (one investigation),
`falsifybench-rule-discovery-games-full-text` (in-game hypotheses),
`gavel-graph-world-models` (plan revision in a run), and
`socratic-agents-autonomous-scientific-discovery` (one experimental
campaign). Files:
wikiskill-persistent-knowledge-for-skill-evolution, skillglow-procedural-family-consolidation,
reflexion-verbal-reinforcement-learning, harnessevolve-reference-trajectories,
stellar-colosseum-many-agent-research-harness, prove2me-collaborative-math-formalization,
meta-agent-challenge-autonomous-agent-development,
i-reverse-engineered-instinct-s-memory-here-2101745550752428340,
procedural-graphs-self-evolving-execution, evoontology-self-evolving-ontology,
dualgraph-knowledge-exploration-outline-structure, rsiagent-autonomous-exploration,
repo-to-skill-disco-ai4ai-skills, ecdysis-training-runtime-harnesses,
sol-pi-efficient-agent-harness, design-docs-are-all-you-need,
crux-open-ended-ai-research-paper, modularrsi-generalizable-harness-self-improvement,
meta-n-recursive-self-improvement, sift-self-improvement-fast-tree-search,
skilllift-dense-rubrics-sparse-oracles, metr-hugging-face-incident-investigation,
accelerating-scientific-research-gemini-real-world, flywheel-encoding-the-scientific-method,
hypothesis-evolution-protocol-auditable-ai-scientists,
falsifybench-rule-discovery-games-full-text, gavel-graph-world-models,
bounded-recursive-self-improvement, eurisko-learns-new-heuristics-and-domain-concepts,
world-models-life-mind-continuity.

**Outliers (17, S), listed individually:**

| Ingest | Why it is an outlier | Proposed edit |
|---|---|---|
| `popper-conjectures-and-refutations` | Grounding source of the new definition; says the book "supports a critical standard for conjectural learning" and that the definition already identifies the interpretation gap | Rewrite the commentary against the five conditions. Its quotes already ground conditions 3 and 5. |
| `popper-epistemology-without-a-knowing-subject-1968` | Grounding source; "The essay supports separating tentative status and conjectural learning from addressability"; follow-up "Maintain the separation among tentative theory, conjectural learning, and addressable theory" | **Reverses.** Addressability is now a builder condition. Rewrite the commentary and the follow-up; objective knowledge now maps to condition 1. |
| `in-defense-of-base-contraction` | "Separately editable commitments are an addressability property, not a condition of conjectural learning" | Reverse: condition 5 |
| `error-centric-intelligence-beyond-observational-learning` | Describes the old definition ("the KB requires only that the theory be open to criticism…"); cites the builder boundary; follow-up asks whether the paradigm requires revisable machinery "for each theory builder" | Rewrite the comparison against the new definition. The reflective qualifier answers the follow-up, so close it. |
| `s3gym-self-testing-self-judging-self-improvement` | "Raw history can support reconstruction of theories … lack of a separate theory document does not establish absence of conjectural learning" | Shift 3. Reconstruction from raw history does not meet condition 4. Keep the opacity point: "does not establish absence". |
| `contextleak-agent-context-exfiltration` | "replacement by recency"; "Weight changes do not exclude conjectural learning" | Say that weights fail condition 1 while models can be components (as the draft's Exclusions say), and that recency replacement bears on condition 3 |
| `long-horizon-agents-levels-ticks-cascaded-intelligence` | "Under conjectural learning, fixed model weights do not exclude learning by the whole system, including its participating human"; "suggestive cases … within the campaign" | Boundary and human-inside wording survive (the draft's Boundary). Check condition 4 across the campaign. |
| `discovery-foundation-models` | Links `theory-builder.md` for its declared-system boundary; "suggestive evidence for conjectural learning by the coupled system" | The boundary comparison survives. Split the verdict into conditions and learning. |
| `sound-agentic-science-requires-adversarial-experiments` | Links the externally tested definition ("the distinction between an agent's internal assessment and an independently assessed outcome") | Repoint to the new home of the externally tested case (D5); the comparison holds |
| `scientisttwo-autonomous-ai-research` | Frontmatter `domains: [… conjectural-learning …]` | Change the domain tag to `theory-building`, or drop it; operator's call (see D2) |
| `llms-scientific-method-hypothesis-to-discovery` | "does not establish a reliable, persistent self-revising theory builder"; follow-up "Review conjectural learning against this perspective" | Reword as "a reflective theory builder"; close or retarget the follow-up |
| `automated-refinement-first-order-horn-clause-domain-theories` | FORTE; links "our account of theory use" to `conjectural-learning.md` | Repoint to `theory-builder.md`. FORTE's single-run exclusion now lives there (condition 4). |
| `think-before-you-act-popperian-expectations-abstract` | Popperian "expectations"; "membership also needs evidence that the system would criticize…" | Expectations may be dispositions (they fail condition 1) or formulated. Keep the question open and restate it against condition 1 and condition 3. |
| `combinatorial-sketching-finite-programs` | Already excludes it for in-run conjectures, "not theories retained for later action" | Now simply condition 4; say so and repoint |
| `socratic-agents-autonomous-scientific-discovery` | Follow-up "Review the existing conjectural-learning definition against AHOIS" | Retarget or close the follow-up; also in group P's re-verdict list |
| `automated-hypothesis-validation-sequential-falsifications` | Follow-up "Review Conjectural learning against POPPER as a boundary case" | Retarget the follow-up to `theory-builder.md` or close it |
| `generalization-adaptive-data-analysis-holdout-reuse` | "qualifies how empirical cases can guide conjectural learning" (no link); the externally tested definition cites this ingest | Say "a theory builder's criticism". Its input role moves with the evaluation protocol (D5). |

## Frozen and workflow-owned records (F)

| Path / set | Uses | Proposed handling |
|---|---|---|
| `kb/reports/retained/theory-builder-boundary-cases-20260917.md` | Status block links all four builder definitions and says their boundary cases restate this report | Keep the content. Repoint the three retired links, which the workshop README allows. The report is not published, so a redirect does not help, and without repointing the local links break. Its status sentence becomes historically true only; leave it. |
| `kb/reports/retained/README.md` | Links the boundary report by title | N |
| 26 retained `agentic-system-analysis/*/result.md` | Text such as "Conjectural learning … uninspected" and "reflective theory builder not established". One (`AAS-2026-09-23-arsumbris-02`) links `conjectural-learning.md`. | Byte-frozen: reviews pin them by `analysis-result-sha256`, so they cannot be edited. They are published, so the new redirect covers the one link on the site; the local checker will warn, as in precedent 643508db. Most are untracked output of the concurrent batch. |
| `kb/agentic-systems/reviews/*.md` (25 matching: 17 link `conjectural-learning.md`, 8 text only) | "defined-in: the stronger learning claim…", "Conjectural learning remains uninspected" | Workflow-owned projections; the collection forbids substantive hand-edits. Options: keep the bytes and rely on the redirect (precedent: the WikiSkill projection), or make a link-only repoint (not substantive). The text keeps the old term either way until each system is re-run. Decision D6. |
| `kb/log.md` | Historical entries | Leave as is |
| `kb/messages/**` | none matched | — |

## Totals by category

At scan time (198 files in scope, plus 1 test-scenario file outside it):

| Category | Files | Notes |
|---|---|---|
| R: target definitions | 6 | 1 replaced in place, 5 retired |
| S: substantive | 112 | 5 system-definition (incl. the test scenario), 1 definition, 10 notes, 6 articles/hubs, 3 workshop files, 87 ingests (17 outliers, 30 group P, 40 group N) |
| L: link-only / wording | 22 | 1 definition, 8 notes, 2 articles/hubs, 5 workshop files, 6 ingests |
| F: frozen / workflow-owned | 54 | 1 boundary report, 26 retained results, 25 reviews, `kb/log.md`, and the retained README (N in effect) |
| N: no edit | 6 | 2 notes, 4 workshop files |

The counts overlap slightly with the moving review set; rerun the scan
before applying. `properdocs.yml` and the root `README.md` are extra
mechanical touches outside the scope (redirects; one path link if the
bootstrapping article is retitled).

## Decisions for the operator

- **D1. Retitle the three notes named for conjectural learning:**
  the companion (`commonplace-studies-conjectural-learning-…`), the
  precedents note, and the evidence note `rules-weights-…-conjectural-learning`.
  Proposed: retitle all three through `commonplace-relocate-note`, as pure
  commits, to theory-builder wording. The companion's frame also changes
  (see its row); the operator should approve the new claim title.
- **D2. The article series keeps "conjectural learning" as informal wording,
  or is retitled.** This is the README's open item. It affects four article
  titles and paths (lead, testing, software house, survey), their 22
  inbound redirects, `kb/index.md`, the articles README, the survey article's
  title, the bootstrapping description, and the `scientisttwo` domain tag.
  Option A: keep "conjectural learner" as the articles' plain name for a
  theory builder, with one sentence mapping it. Option B: retitle to "theory
  builder" wording.
- **D3. Does retaining criticisms from which a theory is rebuilt satisfy
  condition 4?** The old checks case 3 was inside. The draft's condition 4
  ("retains its theories and the record of their criticism") reads as no.
  This sets how the skill, the type, `s3gym`, the proposal note, and the
  survey article treat reconstruction.
- **D4. `conjectural-learning-checks.md`.** Retire it outright, or rewrite
  it as `theory-builder-checks.md`. Its test 1 ("Kind, not degree") classes
  addressability and retention as conjectures, so it contradicts the new
  definition as written. A rewrite would need a new test 1 and a re-run of
  the 16 cases (flips listed above).
- **D5. Home of the externally tested case.** Proposed: the testing article,
  with the evaluation protocol, investigation-inside-main-path, and boundary
  cases (DGM, Commonplace for a consuming project). Alternative split: move
  the three supplied items and the "what remains for the general case" table
  into `a-claim-without-external-assessment-carries-three-obligations.md`,
  which is already their complement. Only the protocol would then go to the
  article. Notes, ingests, and the first-downstream-run protocol would link
  to the note for the concept and to the article for the protocol.
- **D6. Generated reviews.** Keep the link bytes and rely on the redirect
  (the precedent), or allow a link-only repoint on projections.
  Also: sequence the skill and type edit with the concurrent analysis batch.
  Either pause the batch or accept that its in-flight runs finish under the
  old vocabulary.
- **D7. Ingest migration depth.** Proposed: follow f4dc912d and re-verdict
  all 87 substantive ingests condition by condition. That is the only way to
  catch shift-2 and shift-3 flips (group P re-verdicts, group N members that
  now qualify). The cheaper option is to repoint the links and replace
  "conjectural learning" with "learning", but that leaves wrong verdicts
  wherever shift 3 applies.
- **D8. Two small losses from the draft.** "Retention is the builder's, not
  the interpreter's" (used by the ideal-interpreter workshop) and "Revision
  need not be small" (old scope bullet). Restore one sentence each in the
  new definition, or let them go.

## Apparatus relocation map

| Retired section | Destination |
|---|---|
| theory-builder (old): addressability + contradictable consequences | New condition 5; condition 3 ("tests of stated consequences") |
| theory-builder: revision mode left open, reconstruction, first theory in scope | Dropped (reconstruction per D3) |
| theory-builder: Boundary (roles, users outside, role not person) | New Boundary (short) |
| theory-builder: machinery list; WikiSkill as a three-layer instance | Dropped; the WikiSkill ingest and review keep the example |
| theory-builder: Seed | Testing article, "The hypotheses" (it already defines seed) |
| theory-builder: Evidence interface | Testing article, new short section (D5) |
| theory-builder: Persistence (lineage, intervention, total replacement) | New Boundary paragraph 2 (identity, intervention). Intervention accounting goes to the testing article, "Record what people contribute". |
| theory-builder: "Persistence establishes neither retention nor learning"; regenerating builder | Dropped: retention is now condition 4, and learning is left to test |
| theory-builder: Extension (matched baseline, PAST-Bench) | Testing article, "The hypotheses" (it already defines extension; add the matched-baseline rule) |
| theory-builder: Scope, evaluation and interpretation bullets | Testing article (evaluation limits; interpretation vs theory error). The draft keeps "deriving what it implies" as an operation. |
| theory-builder: Exclusions on installation/use/improvement and outcome vs fidelity | Testing article; `an-action-model-matters-only-through-its-consumption-path` already carries the consumption part |
| theory-builder: boundary cases FORTE, Gödel, note-review loop, total replacement | New Exclusions (FORTE), new Boundary cases (Gödel, note-review loop), new Boundary paragraph 2 (total replacement) |
| theory-builder: KB for a consuming project | Testing article, externally tested case |
| externally-tested: the three supplied items and why | Testing article, or the obligations note (D5) |
| externally-tested: Evaluation protocol (reserve, adaptive reuse, controls, no-retention condition) | Testing article, merged into "Start with controlled task families" |
| externally-tested: Investigation stays inside the main path | Testing article |
| externally-tested: What remains for the general case (table) | `a-claim-without-external-assessment-carries-three-obligations.md` |
| externally-tested: Scope, Exclusions, Misuse, boundary cases (DGM, note-review, KB for consuming project) | Testing article, condensed |
| reflective: definition | New Qualifiers, Reflective |
| reflective: Evidence (4-step connected path, matched interventions) | Testing article, before the Reflection hypothesis |
| reflective: Scope, independence from learning / autonomy / extension; inside the externally tested case | Covered by "no success condition" and "qualifiers are independent"; the extension point goes to the testing article |
| reflective: "a self-theory's acceptance is not warrant" | `machinery-persists-by-warrant-not-position-in-a-reflective-loop.md` (already says it) |
| reflective: boundary cases (Commonplace today, Gödel) | New Qualifiers closing line; new Boundary cases |
| autonomous: definition, users outside | New Qualifiers, Autonomous; new Boundary |
| autonomous: per-role human/computational/joint reporting, seed vs interventions | Testing article, "Record what people contribute" |
| autonomous: not reliability (warranted autonomy) | One line already in the draft; the warranted-autonomy note |
| autonomous: not objective governance | Obligations note (its second obligation) |
| conjectural-learning: conditions 1–2 | New conditions 1, 2, 3 |
| conjectural-learning: Simon's criterion, attempt vs learning | New "Error elimination is attempted" paragraph; `learning-is-not-only-about-generality.md` |
| conjectural-learning: persistence of the effect; reconstruction from criticisms | Condition 4 (D3) |
| conjectural-learning: Relation to Popper table | Dropped. The new definition speaks in Popper's terms and lists the KB's addition (condition 5). The amoeba contrast moves to condition 3. |
| conjectural-learning: Scope bullets | Persistence and observer access go to the skill, the type, and the ingest instruction (already there). Faultless theory goes to `a-complete-theory-path…`. Addressability is reversed (condition 5). "Revision need not be small" per D8. Subject and machinery go to the reflective qualifier. |
| conjectural-learning: Exclusions | New Exclusions (fixed theory, discard, black-box, weights, stored-not-consumed). Research community goes to new Boundary cases. Proof-only goes to the Gödel note. Records of inputs and outcomes go to the companion and proposal notes as a named baseline. Whole replacement and reconstruction are reversed. |
| conjectural-learning: Misuse (criticism vs selection) | New Exclusions, black-box line; optionally one misuse line |
| conjectural-learning-checks | D4 |

## Proposed edit order

1. **Definitions.** Install the new `theory-builder.md`. Add the receiving
   sections to the testing article (and the obligations note, per D5), so
   the apparatus has a home before anything is deleted. Then edit
   `addressable-theory.md` and `tentative-theory.md`, and settle D4.
2. **System-definition artifacts.** Edit `AGENTS.md`, the ingest
   instruction, the analyse skill, the result type, the agentic-systems
   `COLLECTION.md`, and the test scenario; run `uv run pytest`. Coordinate
   with the concurrent analysis batch (D6).
3. **Notes and articles.** Edit the companion, precedents, and evidence
   notes, the other S notes, the lead, testing, and survey articles, the
   bootstrapping article and software-house plan, and the hubs
   (`learning-theory-README`, `kb/articles/README.md`).
4. **Ingests.** Outliers first (the Popper ingests ground the new
   definition), then group P, then group N, then group A.
5. **Retitles.** Run `commonplace-relocate-note` for D1 and D2, one pure
   commit each. Then run the title-following link edits (L rows, `kb/index.md`,
   workshops).
6. **Retire.** Delete the five definition files. Add their redirects and
   retarget the three existing entries in `properdocs.yml`. Retire the
   freshness baselines keyed to them.
7. **Frozen records last.** Repoint the links in the boundary report; handle
   the reviews per D6; leave the retained results byte-frozen.
8. **Validate.** Run `commonplace-validate` on the touched collections and
   `commonplace-validate redirects`, then rerun the scan above. Remaining
   hits should be only F records and deliberate informal uses (D2).
