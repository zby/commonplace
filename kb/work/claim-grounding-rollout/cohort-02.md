# Cleanup cohort 02 — frozen 2026-08-24

Frozen at repository `6cdb3c10`. Cohort 01 was the claim-pull rollout's own run
(`agents-navigate-by-deciding-what-to-read-next`, `linking-theory`); this is the
first cohort under [the restored procedure](./procedure.md).

Blob revisions are recorded so a later session can tell whether a target moved
under it. Verify with `git rev-parse --short HEAD:<path>`.

## Selection basis

Not alphabetical and not "most ingests." Three criteria, in order:

1. **Load-bearing** — a defect in a heavily cited note propagates, so grounding
   it returns the most per unit of work.
2. **Groundable now** — the named snapshot verifies by checksum, except where a
   blocked item is included deliberately to exercise that path.
3. **Exercises disposition variety** — the procedure requires a cohort that can
   produce narrowing or contradiction, not only missing citations. Two items
   below are selected because they are *likely to fail*.

Five targets, 16 note-to-ingest pairs. Small enough to finish; wide enough to
test the procedure's disposition vocabulary.

## Cohort-specific note

**One target is contaminated.** [claim-inventory.md](../literature-disposition/claim-inventory.md)
already publishes recalled claims and tradition placements for
`knowledge-storage-does-not-imply-contextual-activation`. Inventory that note
from the note itself first; then treat those placements as reading assignments,
never as findings. They were recalled, not read.

## Pre-source claim inventory — recorded 2026-08-24

Recorded from the five frozen notes before opening any source snapshot, ingest
analysis, or `claim-inventory.md`. A row is one load-bearing claim use. Rows whose
source-side need is `local` are included because source comparison must not turn
the note's own synthesis or definition into an attribution after the fact.

The manifest's selection summary says 16 note-to-ingest pairs, but the target
lists and frozen notes name 18: 5 + 1 + 5 + 4 + 3. They cover 17 distinct
ingests because the J-space ingest serves two notes. The later Gao pull creates
one additional comparison against an open question, but it was not a frozen
citation and is recorded separately as `KSA-8`.

| ID | target | claim as frozen | source-side need |
|---|---|---|---|
| KSA-1 | `knowledge-storage-does-not-imply-contextual-activation` | Knowledge can exist in storage or live context without changing the next answer or action; contextual activation is the stronger transition in which it changes what the agent notices, says, checks, or does without the user naming it directly. | Literature outside the listed LLM ingests: the nearest established distinction between stored or available knowledge and knowledge that is accessible or brought to bear. The search must be reported as bounded, not exhaustive. |
| KSA-2 | `knowledge-storage-does-not-imply-contextual-activation` | Read-back is retained memory accumulated from use returning to a later action through pull or push; shipped static documentation injected at runtime is excluded, and read-back is necessary but not sufficient for activation. | `local`: determine whether this is an explicitly local operational definition rather than a source-derived claim, and whether its boundary remains coherent after the source comparisons. |
| KSA-3 | `knowledge-storage-does-not-imply-contextual-activation` | The Second Brain Trap is a practitioner case in which abundant stored notes still left the author starting from zero because the material was absent from working context. | `the-second-brain-trap-2041486539067154753`: whether the author reports stored notes failing to enter working context, with the first-person scope and causal limits preserved. |
| KSA-4 | `knowledge-storage-does-not-imply-contextual-activation` | In AppWorld solution-injection experiments, agents discovered explicit environmental solutions above 90% of the time but exploited them below 7%, separating visible information from action. | `agents-explore-but-agents-ignore-llms-lack-environmental`: the exact discovery and exploitation results, task and agent conditions, and whether discovery establishes that the solution was visible in context rather than merely encountered by the system. |
| KSA-5 | `knowledge-storage-does-not-imply-contextual-activation` | Condensed experience can be present, read, and semantically plausible yet steer an agent less than the raw traces it replaced. | `llm-agents-are-not-always-faithful-self-evolvers`: whether condensed experience underperforms raw experience behaviorally despite semantic preservation, and under which methods and evaluations. |
| KSA-6 | `knowledge-storage-does-not-imply-contextual-activation` | The J-space experiments distinguish information available to a model, information loaded into a task-engaged verbalizable workspace, and workspace content that causally mediates reporting or flexible computation. | `verbalizable-representations-global-workspace-llms`: the intervention-supported distinctions among availability, task engagement, verbalizability, and causal mediation, including what the experiments do not establish about agent context use. |
| KSA-7 | `knowledge-storage-does-not-imply-contextual-activation` | On Machine Studying's literature task, two models retrieve the same gold papers but the older model discards the right papers after reading them, isolating selection or use failure with retrieval held constant. | `machine-studying`: whether retrieval is actually controlled across models, what “discard after reading” means operationally, and whether the result licenses a context-to-action interpretation. |
| KSA-8 | `knowledge-storage-does-not-imply-contextual-activation` | Open question: how often does context-to-action failure occur in ordinary agent workflows outside artificial solution-injection benchmarks? | `from-agent-behaviour-to-agent-friendly-documentation`: whether explicitly consulted documentation is followed by implementation and verification in observed coding-agent traces. This can inform the question but cannot by itself establish a general frequency or identify consultation with activation. |
| AAA-1 | `axes-of-artifact-analysis` | Artifact analysis should classify an operative part or consumption path by storage substrate, representational form, lineage, and behavioral authority; substrate alone does not determine form, lineage, or force. | `local`: test whether the external example actually instantiates the four-axis analysis without treating that example as the source of the local taxonomy. |
| AAA-2 | `axes-of-artifact-analysis` | In the inspected Intern-S2-Mobius release, decoder layers select among four shared MoE blocks by layer index, a learned top-k router selects eight of 256 experts by default, and a per-layer shared expert is combined with the routed output; the paper's “Memory” and “Reasoners” labels name different roles but not different representational forms or claim-level governance. | `intern-s2-mobius-arxiv-v1`: the released architecture, defaults, and paper labels; separate paper/code facts from the note's inference that both paths remain distributed-parametric and do not provide localized governance. |
| SDB-1 | `soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits` | For quality-sensitive agent work whose required evidence fits the provider window, performance degradation from volume, relevance/interference, and complexity often constrains usable context before the hard acceptance cap. | Composition across the five listed ingests: whether their bounded results jointly support an “often binds first” workload-level claim, or only establish separate existence cases under different tasks and models. |
| SDB-2 | `soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits` | Maximum Effective Context Window results suggest usable context may be far below the advertised window and varies by task. | `paulsen-maximum-effective-context-window-mecw`: the defined metric, evaluated tasks/models, observed gap from advertised windows, and limits on generalizing it to agent work. |
| SDB-3 | `soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits` | In GSM-DC, errors grow by a power law as synthetic distractors increase; greater reasoning depth strengthens the effect, which harms both path selection and arithmetic execution. | `gsm-dc-llm-reasoning-distracted-irrelevant-context`: the reported scaling relation, interaction with reasoning depth, error decomposition, benchmark conditions, and model scope. |
| SDB-4 | `soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits` | Injecting irrelevant task sequences into a web-agent benchmark reduces success from roughly 40–50% to under 10%, produces loops and stale-state use, and remains only modestly improved by retrieval after loading. | `llm-webagents-long-context-reasoning-benchmark`: the exact experimental contrast and rates, observed failure behaviors, retrieval condition, and whether the histories were irrelevant rather than merely long or conflicting. |
| SDB-5 | `soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits` | ConvexBench performance falls from F1 1.0 at depth 2 to about 0.2 at depth 100 even though the depth-100 prompt is only 5,331 tokens, so token count alone does not predict usable capacity. | `convexbench-can-llms-recognize-convex-functions`: the depth, token, and F1 measurements and benchmark/model scope; distinguish observed compositional failure from the note's possible context-management explanation. |
| SDB-6 | `soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits` | A selectively engaged verbalizable J-space broadcasts intermediate representations; ablating it disproportionately harms flexible multi-step tasks while leaving much automatic computation intact, making workspace competition a candidate—not established—mechanism for soft degradation. | `verbalizable-representations-global-workspace-llms`: the task-engagement and ablation results plus their measurement limits; determine whether the long-context competition transfer remains explicitly conjectural. |
| EIR-1 | `exact-implementation-does-not-validate-a-requirement` | Exactness belongs to an artifact–requirement link, while proxyhood belongs to the requirement–objective link; passing local conformance cannot validate an upstream link it does not test. | `local`: determine whether the cited empirical cases serve only as examples and bounds for this local requirement-chain synthesis rather than as its attributed source. |
| EIR-2 | `exact-implementation-does-not-validate-a-requirement` | Fiscal-period normalization is a constitutive, calculator-like requirement inside an otherwise judgment-heavy financial agent system. | `lessons-from-building-ai-agents-for-financial-services`: whether the report describes this normalization as deterministic or constitutive, its role in the system, and the limits of the note's classification. |
| EIR-3 | `exact-implementation-does-not-validate-a-requirement` | Hard per-step checks support reliable composition in MAKER's formally specified Towers of Hanoi task. | `meyerson-maker-million-step-llm-zero-errors`: the task specification, checker or verification mechanism, composition result, and limits on transfer beyond that formal task. |
| EIR-4 | `exact-implementation-does-not-validate-a-requirement` | Purpose-built machinery outperforms frontier LLMs on SuperARC's formal, mechanically scored compression benchmark. | `superarc-ait-benchmark-llm-compression-abstraction`: the benchmark objective and scoring, compared systems, result, and whether it demonstrates local conformance, upstream target validity, or only a bounded performance comparison. |
| EIR-5 | `exact-implementation-does-not-validate-a-requirement` | More than 190,000 runs show large data-efficiency gains from recurrent structure on algebraic state tracking, within small-model and no-scale-closure limits. | `induction-bias-sequence-models-ebrahimi-2026`: the run count, task and architecture comparison, data-efficiency result, and stated model/scale limits. |
| BLS-1 | `bitter-lesson-selects-against-unearned-reach-not-against-structure` | The bitter lesson is better read as selecting against structure whose claimed scope was not tested, rather than against structure or human origin as such; exact specifications and earned structure are not thereby condemned. | `wikipedia-bitter-lesson`: what Sutton's argument actually contrasts and predicts. Keep the note's earned-versus-unearned reinterpretation separate unless the source states it. |
| BLS-2 | `bitter-lesson-selects-against-unearned-reach-not-against-structure` | DomainBed tested nine domain-generalization algorithms on seven multi-domain datasets under a declared model-selection protocol, and tuned ERM matched or beat them; the note interprets each algorithm as making an explicit reach claim defeated when selection was controlled. | `in-search-of-lost-domain-generalization`: the algorithm/dataset counts, selection protocol, ERM comparison, and whether “explicit reach claim” and “declaring the procedure dissolved the advantage” are source statements or target-side interpretations. |
| BLS-3 | `bitter-lesson-selects-against-unearned-reach-not-against-structure` | Rosenfeld, Ravikumar, and Risteski construct a predictor that satisfies IRM's invariance objective and is indistinguishable from the invariant predictor on training data but reverts to ERM under test-environment drift. | `the-risks-of-invariant-risk-minimization`: the construction, training-data indistinguishability, drift conditions, and precise sense in which the objective is satisfied while out-of-distribution behavior fails. |

## Grounded entries written

Sixteen demand-driven entries were appended. The wording below is the exact
`Claim (paraphrase)` field; scope and limitation remain in each linked ingest.

- **E1 — Second Brain Trap:** In a first-person report about a year-long
  “second brain,” the author says a large, organized note collection did not
  affect writing, building, or decisions because the material was not
  accessible in context, leading him to start from zero and rethink it.
- **E2 — Faithful Self-Evolvers:** Across four self-evolving-agent frameworks,
  thirteen LLM backbones, and nine environments, causal perturbations changed
  behavior more consistently for raw trajectory experience than for condensed
  summaries or heuristics; weak dependence on condensed experience persisted
  when it was the only experience supplied.
- **E3 — J-space, task distinction:** In controlled language-identification and
  character-counting tasks, the same underlying information could support
  automatic computation without causally routing through the measured J-space,
  while explicit report and flexible inference depended on J-space
  representations; task demands could surface otherwise absent information
  into that space.
- **E4 — Machine Studying:** In StudyBench's literature-review analysis, when
  evaluation was restricted to must-cite papers that both GPT-5.1 and GPT-5.5
  had encountered, GPT-5.1 retained markedly fewer papers from 2023 onward—including
  only 65.6% of reached 2025 must-cites versus 89.3% for GPT-5.5—so the later
  gap occurred after retrieval.
- **E5 — J-space, ablation and broadcast:** In the paper's Sonnet 4.5
  experiments, J-space ablation selectively impaired multi-hop and
  context-dependent flexible generation while leaving many shallow
  classification, extraction, and ordinary next-token predictions largely
  intact; the measured J-space carried a small share of activation variance and
  its contents were preferentially relayed across layers and token positions.
- **E6 — Mobius:** The Mobius-v0 paper proposes a globally shared feed-forward
  “Memory” queried by multiple self-attention “Reasoners” through hidden states,
  and at larger scales partitions the shared FFN into sparsely activated
  MoE-like blocks.
- **E7 — MECW:** Across eleven tested models and four synthetic retrieval,
  aggregation, and sorting question types, Paulsen reports that measured Maximum
  Effective Context Windows fell well below providers' maximum accepted windows
  and shifted with question type, with some measured gaps exceeding 99%.
- **E8 — GSM-DC:** In GSM-DC's controlled synthetic math problems, increasing
  injected irrelevant context reduced reasoning accuracy across six tested
  instruction models; error grew roughly as a power law in distractor count
  with a steeper exponent at greater reasoning depth, and the disruption
  affected both correct path selection and arithmetic execution.
- **E9 — long-context web agents:** In a web-agent benchmark that inserted
  irrelevant task sequences between dependent subtasks to create
  25,000–150,000-token histories, four tested models' success fell from roughly
  40–50% in baseline conditions to below 10% in long-context conditions; loops
  and loss of the original objective were prominent, and task-relevant summary
  retrieval produced only modest improvement.
- **E10 — ConvexBench:** On ConvexBench's deeply composed symbolic-function
  tasks, one-shot reasoning fell from F1 1.0 at depth 2 to about 0.2 at depth
  100 even though the depth-100 input was 5,331 tokens; agentic reasoning with
  focused context reached F1 1.0 across the evaluated depths.
- **E11 — MAKER:** In a 20-disk Towers of Hanoi demonstration, MAKER completed
  more than one million LLM-generated steps with zero observed errors by
  decomposing execution into one-move microagent calls and applying
  first-to-ahead-by-three voting plus format- and length-based red-flagging.
- **E12 — SuperARC:** On SuperARC-seq's 100 binary-sequence compression tasks,
  the benchmark's AIXI/BDM/CTM baseline scored φ = 1.000, while the best listed
  frontier LLM scored 0.042 and most scored about 0.007–0.008, largely by
  printing target sequences rather than compressing them.
- **E13 — induction bias:** In more than 190,000 training runs on synthetic
  modular-addition state tracking, small recurrent models learned higher-modulus
  and longer-sequence configurations with orders of magnitude fewer samples
  than small transformers in the outcome-supervision regime, while the compared
  architectures favored different intermediate-supervision formats.
- **E14 — Wikipedia bitter-lesson summary:** Wikipedia summarizes the bitter
  lesson as the long-run tendency for approaches that scale with computation—such
  as search and statistical learning—to outperform approaches based on
  domain-specific understanding, and says Sutton recommends simple scalable
  methods over increasingly elaborate human insight.
- **E15 — DomainBed:** DomainBed evaluates nine baseline domain-generalization
  algorithms on seven multi-domain datasets under three explicit model-selection
  criteria, and reports that carefully implemented empirical risk minimization
  achieves state-of-the-art performance across the tested datasets.
- **E16 — IRM risk:** For non-linear featurizers in the paper's Gaussian
  latent-variable model, Rosenfeld, Ravikumar, and Risteski construct a predictor
  that is near-optimal for the penalized IRM objective and near-identical to the
  invariant predictor on the training distribution, yet uses the ERM solution
  on most test points when the test environment's mean is sufficiently far from
  the training means.

The Gao and Chen ingest already contained the exact normalized claim used for
`KSA-8`; it was checksum- and extract-verified and reused rather than duplicated.

## Targets

### 1. `knowledge-storage-does-not-imply-contextual-activation` — blob `2438659f`

190 inbound references, the highest in the corpus. Five cited ingests, four
groundable, one blocked.

- `agents-explore-but-agents-ignore-llms-lack-environmental` — **blocked**, needs re-ingest
- `llm-agents-are-not-always-faithful-self-evolvers`
- `machine-studying`
- `the-second-brain-trap-2041486539067154753`
- `verbalizable-representations-global-workspace-llms`

**Expected to be the hardest item, and chosen for it.** The
[claim inventory](../literature-disposition/claim-inventory.md) found its two halves disjoint: the famous
claim — knowledge present without affecting the next action — is recalled as
Tulving's availability/accessibility distinction and cited to nobody, while the
half 158 reviews and a type spec actually consume is the wholly local `read-back`
definition. All five cited ingests are LLM-side. So grounding should surface a
**corpus gap** rather than a claim: the source that would settle its central
proposition is not captured, and is cognitive psychology rather than anything in
the current corpus. That outcome is a `literature handoff`, and it is a direct
test of whether the procedure reports a missing tradition instead of grounding
the claim in whatever ingest is nearest.

**Early progress record, 2026-08-24.** The target's context-to-action discussion supplied this source-side
need: whether explicitly consulted documentation is consistently followed by
implementation and verification in observed coding-agent traces. [Gao and
Chen's trace study](../../sources/from-agent-behaviour-to-agent-friendly-documentation.ingest.md)
was captured and ingested, then received one demand-driven Claims entry:
"In Gao and Chen's observational coding-agent traces, explicit documentation
consultation was not consistently coupled to immediate implementation and
verification: the code-edit association depended on statistical adjustment,
while test and build actions were less frequent within the next three events in
both unadjusted and adjusted analyses." All three retained extracts matched the
checksum-verified primary snapshot, and the populated ingest passed
`commonplace-validate` cleanly.

This grounds only the paper's short-horizon observational result. It does not
establish the note's general proposition, identify consultation with contextual
activation, or replace the cognitive-psychology source assignment above. The
completed comparison and disposition below preserve those limits.

### 2. `axes-of-artifact-analysis` — blob `85748ef0`

178 inbound, one cited ingest (`intern-s2-mobius-arxiv-v1`). The clean
high-dependency, single-source case — the control against which the harder items
read.

### 3. `soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits` — blob `53c418cd`

15 inbound, five cited ingests, all groundable.

- `convexbench-can-llms-recognize-convex-functions`
- `gsm-dc-llm-reasoning-distracted-irrelevant-context`
- `llm-webagents-long-context-reasoning-benchmark`
- `paulsen-maximum-effective-context-window-mecw`
- `verbalizable-representations-global-workspace-llms`

**Tests multi-source composition.** Whether five separately grounded claims
compose into one local claim, or whether the note leans on a composite no single
source supports — the exact defect found in the Pirolli case, where two separate
results were merged into a pointer-level tradeoff the source never makes. Also
shares an ingest with target 1, so it tests whether one ingest serves two
different demands without entry conflict.

### 4. `exact-implementation-does-not-validate-a-requirement` — blob `c32dc467`

19 inbound, four cited ingests, three groundable, one blocked
(`lessons-from-building-ai-agents-for-financial-services`).

**Deliberately includes a blocked item** so the run exercises re-ingest routing
and the `unavailable` disposition rather than discovering that path mid-sweep.

### 5. `bitter-lesson-selects-against-unearned-reach-not-against-structure` — blob `3e9c4546`

13 inbound, three cited ingests, all groundable.

- `in-search-of-lost-domain-generalization`
- `the-risks-of-invariant-risk-minimization`
- `wikipedia-bitter-lesson`

**Selected as the most likely contradiction.** The bitter lesson is a widely
paraphrased claim, one of its sources is a Wikipedia article rather than Sutton's
text, and the note asserts a *reading* of it. If any item in this cohort returns
`contradicted/repaired` or `narrowed`, this is the one.

## Recording

Per target: claim as stated before source reading, disposition, resulting
`Claims` entries, note repair if any, validation result, and source-lens verdict.
Record candidate precision and unavailable sources; make no corpus-recall claim.

## Expected distribution

Recorded before the run, and **sealed** in
[cohort-02-prediction.md](./cohort-02-prediction.md). Do not open that
file while executing this cohort: a stated distribution is an anchor, and an
executor who knows the prediction will tend to produce it — the same charitable
bias this procedure exists to defeat, in a new costume. Open it when judging the
finished run.

## Completion record — 2026-08-24

All five targets pass `commonplace-validate` cleanly. Source conformance ran in
the `codex` model partition. After the recorded repairs, the stale selector
returned `targets: []` for the complete final source scope.

| Target | Validation | Final source-conformance result |
|---|---|---|
| `knowledge-storage-does-not-imply-contextual-activation` | PASS clean | Five linked pairs PASS. The unavailable Agents Explore pair first returned FAIL because its Claims section is empty; the source-specific body use and footer were then removed. |
| `axes-of-artifact-analysis` | PASS clean | One pair PASS after an initial FAIL caused removal of unsupported conversion, training-lineage, and paper-outcome details. |
| `soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits` | PASS clean | Five pairs PASS after an initial WARN caused the web-agent interaction sentence to be separated from the benchmark's combined length/content intervention. |
| `exact-implementation-does-not-validate-a-requirement` | PASS clean | Three linked pairs PASS. The unavailable Fintool use was removed before review, so no final pair exists for it. |
| `bitter-lesson-selects-against-unearned-reach-not-against-structure` | PASS clean | Three pairs PASS. The contribution-level rewrite also received a fresh-context blind acceptance verdict of PASS before promotion. |

The final claim-use dispositions are:

| ID | Disposition | Target change and basis |
|---|---|---|
| KSA-1 | literature handoff | Kept the activation distinction as Commonplace theory. The contaminated inventory supplied only reading assignments to Tulving and Pearlstone's availability/accessibility work and Gick and Holyoak's spontaneous-transfer work; a bounded lexical search of the local KB found no matching primary capture. No broader literature or corpus-recall claim is made. |
| KSA-2 | retained local delta | Kept `read-back` as an explicitly local operational definition with its accumulated-from-use boundary. None of the external comparisons turned it into an attributed claim. |
| KSA-3 | grounded | Reworded the Second Brain case to the normalized first-person claim and added its single-report limits; the frozen storage-to-context use was supported. |
| KSA-4 | unavailable | The exact name-paired snapshot is absent. A differently named snapshot has the expected checksum, but the pairing rule forbids substitution. The Claims-empty pair returned FAIL, after which the AppWorld rates, interpretation, source link, and footer were removed. |
| KSA-5 | narrowed | Replaced “present, read, and semantically plausible yet steers less” with the supported causal-perturbation comparison. The note now denies that the experiment establishes semantic preservation or a general performance loss from condensation. |
| KSA-6 | grounded | Normalized the footer to the controlled task result: automatic computation can bypass measured J-space while explicit report and flexible inference depend on or surface information there. |
| KSA-7 | narrowed | Replaced “same gold papers,” “discarded after reading,” and a cause-isolating interpretation with the intersected must-cite, post-retrieval retention comparison and its two-model causal limit. |
| KSA-8 | retained local delta | Kept the frequency question unresolved and added Gao and Chen's short-horizon observational result as a bounded adjacent observation; it neither answers the question nor equates consultation with activation. |
| AAA-1 | retained local delta | Kept the four-axis taxonomy as local theory. Mobius remains only a bounded instance used to apply, not source, that classification. |
| AAA-2 | narrowed | Kept the primary paper's shared-FFN/Reasoner architecture and the local distributed-parametric inference. Removed code defaults, conversion/training lineage, and named outcome claims that the primary Claims entry did not establish. |
| SDB-1 | narrowed | Changed the prevalence claim from “often binds first” to “can bind first” and states that the cited studies provide existence cases, not a representative-workload rate. |
| SDB-2 | grounded | Retained the task-dependent MECW claim with eleven-model, four-synthetic-task scope and the limitation that these records do not represent ordinary agent work. |
| SDB-3 | narrowed | Changed the relation to roughly power-law growth and bounded it to the tested templated problems, distractor range, depths, and six models. |
| SDB-4 | narrowed | Removed unsupported stale-state use, preserved the measured success collapse and failure behaviors, and made the joint length/intervening-content intervention explicit. |
| SDB-5 | grounded | Retained the depth, F1, and 5,331-token comparison within ConvexBench, added the focused-context agentic result, and kept context management versus missing procedure open. |
| SDB-6 | grounded | Retained J-space competition only as a candidate mechanism. The note states that the study did not vary long-context load against workspace occupancy. |
| EIR-1 | retained local delta | Kept the artifact–requirement–objective distinction as local synthesis; the empirical cases only exemplify or bound it. |
| EIR-2 | unavailable | The exact name-paired snapshot is absent. A differently named checksum match was not substituted. Fiscal-period normalization and the Fintool link were removed, leaving no source pair. |
| EIR-3 | contradicted/repaired | Replaced “hard per-step checks” with the demonstrated one-move decomposition, first-to-ahead-by-three voting, and format/length red-flagging; the note now says the source does not attribute the result to hard semantic checks. |
| EIR-4 | grounded | Retained the bounded SuperARC comparison with the exact task count and scores, plus the limit that the benchmark metric is not thereby validated as general abstraction. |
| EIR-5 | grounded | Retained the recurrent-model sample-efficiency result with its synthetic modular-addition, small-model, outcome-supervision, and no-scale-closure bounds. |
| BLS-1 | contradicted/repaired | Rebuilt the artifact through source-first reconstruction, incumbent reconciliation, drafting, audit, and blind acceptance. Wikipedia now supplies only a secondary production-method contrast; unsupported proxy scope is an explicit case-level Commonplace conjecture, not Sutton's thesis or a general selection law. |
| BLS-2 | narrowed | Kept DomainBed's nine algorithms, seven datasets, three selection criteria, and bounded ERM result. Removed the claims that every algorithm asserted reach, that declared selection caused the outcome, or that DomainBed instantiates the conjectured mechanism. |
| BLS-3 | narrowed | Replaced exact objective discharge, indistinguishability, and unqualified drift with the non-linear Gaussian-model construction's near-optimal, near-identical, and sufficiently-shifted conditions. It witnesses only one link in the local mechanism. |

**Distribution:** seven grounded, eight narrowed, two contradicted/repaired,
four retained local deltas, two unavailable, one literature handoff, and zero
false positives.

## Source and identity observations

- Sixteen new Claims entries were appended across fifteen ingests. The existing
  Gao and Chen entry was reused unchanged. Exact snapshot checksums and every
  retained verbatim extract were mechanically rechecked after writing.
- Thirteen changed ingests validate cleanly. The Faithful Self-Evolvers and
  Paulsen ingests pass with, respectively, four and one pre-existing warnings
  for the missing `../notes/definitions/distillation.md` target; this cohort did
  not edit unrelated analysis prose to repair them.
- The two unavailable cases reveal **snapshot-pair identity pressure**, not
  missing bytes: each expected checksum exists under another slug, but V1's
  exact name-pairing rule correctly prevented silent substitution.
- The J-space ingest accumulated two distinct entries and served two target
  demands without ambiguous selection. Every other newly grounded ingest has
  one entry. No claim-ID, merge, or intermediate-node pressure appeared in this
  cohort.
- The frozen manifest summary understated its own list: it named 18 frozen
  note-to-ingest pairs, not 16, over 17 distinct ingests. Adding Gao produced a
  nineteenth comparison. Removing the two unavailable uses leaves 17 linked
  source pairs in the final five targets.

## Handoffs

The KSA literature handoff is deliberately bounded: inspect the primary work on
availability/accessibility and spontaneous analogical transfer before deciding
whether either tradition grounds the note's agent-facing activation claim.

A targeted backlink scan also found out-of-cohort consumers that still import
the repaired bitter-lesson note with categorical “scale selects” or survivor
language. The clearest named follow-ups are:

- `kb/notes/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md`
- `kb/notes/machinery-persists-by-warrant-not-position-in-a-reflective-loop.md`
- `kb/notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md`
- `kb/notes/the-bitter-lesson-selects-production-methods-not-representational.md`
- `kb/notes/scaling-absorbs-scaffolding-at-fixed-difficulty-not-at-the-frontier.md`
- `kb/notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md`
- `kb/notes/treat-continual-learning-as-representational-form-coevolution.md`
- `kb/notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md`
- `kb/notes/oracle-strength-spectrum.md`
- `kb/agentic-systems/exo.md`

The in-cohort backlink in `exact-implementation-does-not-validate-a-requirement`
was repaired. The list above is a bounded handoff, not an exhaustive backlink
or semantic audit, and those artifacts were not edited in this run.

## Prediction check

The sealed file was opened only after all 24 rows had terminal dispositions,
all targets validated, and the final source selector was empty.

The prediction had three clauses:

1. **At most one grounded as written:** missed under the procedure's declared
   claim-use unit. Seven of 24 frozen uses were supported within their stated
   bounds: KSA-3, KSA-6, SDB-2, SDB-5, SDB-6, EIR-4, and EIR-5. This was not a
   clean-target result: every one of the five target artifacts also contained a
   narrowed, contradicted, unavailable, or handoff item.
2. **At least two narrowed or contradicted/repaired:** met. Eight uses were
   narrowed and two were contradicted/repaired.
3. **At least one literature handoff in target 1:** met. KSA-1 remains a bounded
   handoff to the availability/accessibility and spontaneous-transfer
   traditions.

The sealed warning about “five clean groundings” did not fire: zero of five
targets survived unchanged at artifact level. Step 1's ordering also checked
out—the 24-row inventory was saved before any source or contaminated assignment
was read, and all five frozen blob hashes matched. The first clause therefore
appears to have mixed target-level cleanliness with claim-use disposition and
to have been too pessimistic about already bounded empirical footers. Future
sealed predictions should name the unit and define whether “grounded as written”
means no wording change, source-side support for the frozen proposition, or a
whole target needing no repair.
