# Cleanup cohort 09b — frozen 2026-08-24

**Status: complete.** Executed on 2026-08-25 after verifying every target's
frozen blob and all eleven exact name-paired snapshot identities. Frozen at
repository `a91ed377`. Split from cohort 09 on 2026-08-24 to bound one agent's
context; the original manifest's scope was 15 targets over 20 ingests.

**Run sequentially with [cohort 09a](./cohort-09a.md), never concurrently.**
Cohort 09 is a single connected component — every target shares an ingest with
another — so no parallel split of it exists. This cut minimizes the bridge to
**2 shared ingests**, but two agents appending to the same `Claims`
section can still lose an entry, since V1 ships no locking. The pair is disjoint
from every other cohort on both mutation axes.

Bridge ingests, shared with cohort 09a: `co-harness-co-evolving-harness-and-model-weights`, `meta-harness-end-to-end-optimization-of-model-harnesses`.
Whichever half runs second will find incumbent entries there; reuse an adequate
one rather than appending a near-duplicate.

Scope: 8 targets, 11 ingests, 18 note-to-ingest pairs,
0.30 MB of snapshots. 1 ingests already carry Claims entries; the rest
are empty. An existing entry is a candidate for exact reuse, not a presumption
that a target use is supported.

## Targets

| Target | Blob | Ingests |
|---|---|---|
| `evaluation-automation-is-phase-gated-by-comprehension` | `ae340da3` | `meta-harness-end-to-end-optimization-of-model-harnesses` |
| `frontloading-spares-execution-context` | `d116e1b4` | `machine-studying` |
| `instantiation-alone-cannot-model-agent-learning-across-sessions` | `4525afe5` | `erlang-compilation-and-code-loading`<br>`erlang-release-handling`<br>`fast-properties-in-v8`<br>`machine-studying`<br>`metaobject-protocols-why-we-want-them-and-what-else-they-can-do`<br>`monkey-patch` |
| `learning-inside-a-fixed-decomposition-inherits-its-mistakes` | `8a525199` | `acm-agentic-context-management-for-long-horizon-tasks`<br>`co-harness-co-evolving-harness-and-model-weights` |
| `measuring-autonomy-well-enough-to-see-it-improve-is-an-open-problem` | `344a3ce7` | `position-ai-agents-in-scientific-teams-as-human-agent-systems` |
| `memory-design-adds-operational-axes-to-artifact-analysis` | `51cf0d71` | `machine-studying` |
| `retained-artifacts-enable-persistent-deployment-time-adaptation` | `c858696e` | `machine-studying`<br>`openclaw-rl-train-any-agent-simply-by-talking` |
| `the-deployed-system-not-the-model-is-the-unit-of-learning` | `d239761d` | `co-harness-co-evolving-harness-and-model-weights`<br>`machine-studying`<br>`meta-harness-end-to-end-optimization-of-model-harnesses`<br>`position-ai-agents-in-scientific-teams-as-human-agent-systems` |

## Source-blind claim inventory

| ID | target | claim as frozen | source-side need |
|---|---|---|---|
| 09B-01 | `evaluation-automation-is-phase-gated-by-comprehension` | Meta-Harness qualifies the human-led comprehension gate: in a hard-oracle harness search, a proposer with raw execution traces, prior harness code, and scores can infer failures before proposing again; its ablation suggests a fixed summary without traces may lose that diagnostic content. | Does Meta-Harness give its proposer raw traces, prior harness code, and scores, and does its ablation show the fixed summary-without-traces treatment underperforming raw-trace access? |
| 09B-02 | `frontloading-spares-execution-context` | Machine Studying's corpus-derived cheatsheet gains concentrate at low inference budgets and are recovered by forced search at high budgets, so one study pass replaces per-question rediscovery where budget is scarce. | Does Machine Studying report that a corpus-derived cheatsheet helps chiefly at low inference budgets and that forced search recovers the benefit at higher budgets? |
| 09B-03 | `instantiation-alone-cannot-model-agent-learning-across-sessions` | Erlang/OTP compilation and code loading supplies the current/old-version mechanism behind a governed live definition transition. | Does Erlang/OTP code loading retain current and old module versions, and what transition behavior does that mechanism permit? |
| 09B-04 | `instantiation-alone-cannot-model-agent-learning-across-sessions` | Erlang/OTP treats live definition change as versioned release work with migration and rollback. | Does Erlang/OTP release handling govern live code change through release versions, state migration, and rollback? |
| 09B-05 | `instantiation-alone-cannot-model-agent-learning-across-sessions` | V8 can deoptimize optimized code when object-layout assumptions stop holding, attesting a runtime cost for crossing an optimized definition boundary. | Does V8 optimize around object-layout assumptions and deoptimize when those assumptions are invalidated? |
| 09B-06 | `instantiation-alone-cannot-model-agent-learning-across-sessions` | Machine Studying changes an agent before later inference by writing a reusable repository map; its gain is concentrated where an unprepared session cannot afford equivalent exploration. | Does Machine Studying describe studying as changing the agent through a reusable repository artifact before inference, with gains concentrated at low inference budgets? |
| 09B-07 | `instantiation-alone-cannot-model-agent-learning-across-sessions` | A metaobject protocol marks definition change with an explicit base/meta separation and protocol entry points for changing language organization. | Does the metaobject-protocol source distinguish base-level behavior from a meta-level protocol that exposes and changes language organization? |
| 09B-08 | `instantiation-alone-cannot-model-agent-learning-across-sessions` | “Monkey patch” is warning vocabulary for runtime modification and its documented coordination risks. | Does the monkey-patch source define runtime modification under that warning-marked name and identify coordination or compatibility risks? |
| 09B-09 | `learning-inside-a-fixed-decomposition-inherits-its-mistakes` | ACM learns when to invoke or abstain from a supplied two-operation scheme—summarize and archive an earlier chronological prefix, then query archived messages by identifier—but cannot choose a different state representation; its benchmark gains test the compound system, not rival decompositions. | What context-management operations does ACM fix, what policy does it learn over them, and do its experiments compare that operation set with rival decompositions? |
| 09B-10 | `learning-inside-a-fixed-decomposition-inherits-its-mistakes` | Co-Harness broadens the effective update space across prompts, tools, skills, middleware, memory, and model weights. | Which harness components and model parameters does Co-Harness actually expose to co-evolution? |
| 09B-11 | `measuring-autonomy-well-enough-to-see-it-improve-is-an-open-problem` | The scientific human-agent-systems position paper calls for measuring human-agent synergy, but its abstract-page capture supplies neither a commensurable function decomposition nor a resolution of scalar contribution attribution. | Does the captured abstract call for measuring scientific human-agent synergy, and does it specify a commensurable function decomposition or scalar attribution method? |
| 09B-12 | `memory-design-adds-operational-axes-to-artifact-analysis` | Machine Studying isolates corpus-only preparation before any downstream task, reward, demonstration, or execution trace, making it a pre-task capture-policy case. | Does Machine Studying's study phase use only the target corpus before downstream questions, rewards, demonstrations, or execution traces are available? |
| 09B-13 | `retained-artifacts-enable-persistent-deployment-time-adaptation` | In preliminary small-scale Machine Studying runs, a corpus-derived note was the only studied intervention that raised agent expertise, outperforming continual pre-training and synthetic fine-tuning in one of two domains. | What did Machine Studying's repository-note, continual-pre-training, and synthetic-fine-tuning interventions change, and on which domains and metric did the repository note improve results? |
| 09B-14 | `retained-artifacts-enable-persistent-deployment-time-adaptation` | OpenClaw-RL is an existing case of model weights being updated through live reinforcement learning during deployment, while leaving validation and rollback tradeoffs visible. | Does OpenClaw-RL update an acting agent's model weights online from live interaction, and what validation or rollback boundary does the source establish? |
| 09B-15 | `the-deployed-system-not-the-model-is-the-unit-of-learning` | Co-Harness is a bounded attempt to co-evolve model weights with prompts, tools, skills, memory, and middleware. | Does Co-Harness jointly optimize model weights and those named harness components, and what bounds apply to the demonstrated system? |
| 09B-16 | `the-deployed-system-not-the-model-is-the-unit-of-learning` | Machine Studying independently defines the learning unit as the pair `(model, harness)`, with studying allowed to change weights, prompts, tools, indexes, or notes. | Does Machine Studying explicitly define the agent as a model-harness pair and allow studying to alter each of weights, prompts, tools, indexes, and notes? |
| 09B-17 | `the-deployed-system-not-the-model-is-the-unit-of-learning` | Meta-Harness demonstrates end-to-end search over a task-specific harness around fixed model weights. | Does Meta-Harness optimize the complete task-specific harness while holding the underlying model fixed, and what harness surface is in scope? |
| 09B-18 | `the-deployed-system-not-the-model-is-the-unit-of-learning` | The scientific human-agent-systems position paper independently applies a human-inclusive evaluation boundary to scientific agents, although the abstract-page capture does not advance measurement of that boundary. | Does the captured abstract argue that scientific AI agents should be evaluated as parts of human-agent systems, and what measurement detail does the capture actually provide? |

## Source-demand plan and grounding record

All eleven exact name-paired snapshots passed canonical-source and SHA-256
checks before source reading. Work then proceeded one ingest at a time.

| ingest | inventory rows | selected Claim and action | identity and validation |
|---|---|---|---|
| `meta-harness-end-to-end-optimization-of-model-harnesses` | 09B-01 | **Reused incumbent:** “In Meta-Harness's online text-classification ablation, all proposer arms could inspect scores and code; Scores Only reached 34.6% median and 41.3% best accuracy, Scores + Summary reached 34.9% median and 38.7% best without traces, and the full arm reached 50.0% median and 56.7% best with traces. The experiment shows that the fixed summary-only feedback arm did not recover the full trace-access arm's performance in this setup.” | Canonical source matched; SHA-256 `95fd47e4603f8c6975cc4fa0df12fc349f730f82715557087a6ffcf0f5d2fa0f`; incumbent preserved byte-for-byte. |
| `meta-harness-end-to-end-optimization-of-model-harnesses` | 09B-17 | **Added:** “Meta-Harness searches over task-specific executable harnesses that modify prompting, retrieval, memory, and orchestration while keeping the domain's base language model frozen.” | Same verified pair; ingest PASS clean with all seven extracts resolved. |
| `co-harness-co-evolving-harness-and-model-weights` | 09B-10, 09B-15 | **Reused one incumbent for both:** “Co-Harness alternates validated edits to a harness comprising prompts, tool schemas, skills, middleware, and memory with model fine-tuning on verified trajectories generated under the improved harness; the updated model then enters the next harness round. Its core experiment combines one HarnessCritic pass and one SFT pass in each of two rounds, while the Round 0 baseline already has an evolved harness but no SFT.” | Canonical source matched; SHA-256 `83c4f1716060cbdb060c50f8a0223e6e8c49f1bee4d2fe7d0b5ffdbd84bb0f45`; ingest PASS clean with all four incumbent extracts resolved and incumbent preserved byte-for-byte. |
| `machine-studying` | 09B-12 | **Added:** “Machine Studying defines studying as an agent changing itself from a corpus before information about downstream evaluation, task distribution, or reward is known.” | Canonical source matched; SHA-256 `a1e2d70a966db1cd1d47ec45a6f0c0db498a1b0b023166cf73263a9d5911f320`. |
| `machine-studying` | 09B-16 | **Added:** “Machine Studying defines an agent as a model–harness pair and allows a studying algorithm to change model weights, prompts, tools, and environment-maintained indexes or notes.” | Same verified pair. |
| `machine-studying` | 09B-02, 09B-06 | **Added once; selected for both:** “In the preliminary Qwen3.5-9B Studying-DSPy experiment, a pre-inference study pass explored the repository and wrote a note that was prepended to later questions; its gains concentrated at low inference budgets, while forced 20-iteration search let the unmodified agent catch up. The source reports no corresponding effect on Studying-OpenClaw.” | Same verified pair. |
| `machine-studying` | 09B-13 | **Added:** “In preliminary Qwen3.5-9B runs, the cheatsheet produced 9.65 lenient-WAUC expertise on Studying-DSPy versus 6.49 for the base agent, 3.29 for synthetic SFT plus on-policy distillation, and 3.71 or 3.92 for continual-pre-training variants; the source calls it the only tested procedure to develop noticeable expertise in one of the two domains.” | Same verified pair; final ingest PASS clean with all fourteen incumbent and new extracts resolved. |
| `erlang-compilation-and-code-loading` | 09B-03 | **Added:** “During Erlang runtime module replacement, current and old code variants may execute concurrently; a process moves to current code through a fully qualified call, while loading a third version purges the old variant and terminates processes still in it.” | Canonical source matched; SHA-256 `a6a0711854629a3ca085a052271a4c040182f2963a92e68e0e55ca9aba5f7574`; all three extracts resolved; ingest PASS with its pre-existing off-vocabulary `technical-documentation` genre warning. |
| `erlang-release-handling` | 09B-04 | **Added:** “Erlang/OTP release handling uses versioned application and release plans for live upgrades and downgrades; advanced module updates can transform process state, failed installation reboots into the old release, and an installed release can be explicitly downgraded.” | Canonical source matched; SHA-256 `a4a1c18c7d4575f917f40504d2a2009660ea34aa2207bee802f877a60e177e9a`; all four extracts resolved; ingest PASS with its pre-existing off-vocabulary `technical-documentation` genre warning. |
| `fast-properties-in-v8` | 09B-05 | **Added narrower source proposition:** “V8 uses dynamically updated HiddenClasses to identify object shapes; its optimizing compiler can inline property access when a HiddenClass ensures a compatible structure, while shape or property-type changes create different HiddenClasses and can prevent generation of optimal code through type pollution.” | Canonical source matched; SHA-256 `be22144fed223513ce79e4d1d49cb9580d6355112f1df1499e3e896232ef3e53`; ingest PASS clean with all three extracts resolved. The snapshot does not establish the frozen deoptimization wording. |
| `metaobject-protocols-why-we-want-them-and-what-else-they-can-do` | 09B-07 | **Added:** “The CLOS metaobject protocol opens selected language semantics and implementation strategies to programmer control through explicit generic-function entry points on metaobjects, while base programs opt particular classes into an alternative metaobject class.” | Canonical source matched; SHA-256 `02cfee9ebe676ff495272a2ed6717b26fd61f907ea70d37deb217d78fdcab957`; ingest PASS clean with all three extracts resolved. |
| `monkey-patch` | 09B-08 | **Added:** “Wikipedia defines monkey patching as dynamically modifying runtime code in a dynamic language and records risks including incompatibility after upstream releases, last-writer overwrite of competing patches, and confusion between source code and actual behavior.” | Canonical source matched; SHA-256 `1474a84a716fd4bb84d49465755b24d5c15649db5e66098550cbdc4a7414ac45`; ingest PASS clean with all four extracts resolved. |
| `acm-agentic-context-management-for-long-horizon-tasks` | 09B-09 | **Added:** “ACM supplies two context-management tools—`manage_context` summarizes all messages up to the previous summary boundary while archiving their raw text under an identifier, and `query_memory` retrieves from the identified archive—and its post-training objective teaches when to invoke or refrain from those tools.” | Canonical source matched; SHA-256 `56d2f596d4bbb9ce785b0de456982a2dfff80af7a50d4f1f4ef16778d79d5de2`; ingest PASS clean with all four extracts resolved. The limitation records that system-level baselines do not search over ACM's action basis or train matched rival representations. |
| `acm-agentic-context-management-for-long-horizon-tasks` | 09B-09 | **Added after target comparison exposed the distinct outcome need:** “In the Qwen3.5-9B training ablation, adding ACM training data raised Pass@1 from 0.635 to 0.727 on BrowseComp-Plus, from 0.405 to 0.425 on DeepSearchQA, and from 0.508 to 0.530 on SWE-Bench Verified.” | Same verified pair; final ingest PASS clean with all seven extracts resolved. The limitation keeps the outcome at compound-treatment grain inside the fixed decomposition. |
| `position-ai-agents-in-scientific-teams-as-human-agent-systems` | 09B-18 | **Added:** “The position paper argues that scientific AI agents should be studied as human-agent systems whose unit of analysis is the human-agent pair, rather than only through agents' autonomous capabilities.” | Canonical source matched; SHA-256 `1230de7b14abcd6d7e701adfcabf585220d87e52952e2efd0af9c358f79bd977`. |
| `position-ai-agents-in-scientific-teams-as-human-agent-systems` | 09B-11 | **Added:** “The position paper calls for new research using a human-agent-systems lens to develop mathematical frameworks for understanding and fostering human–AI synergy in scientific discovery.” | Same verified abstract-page pair; final ingest PASS clean with both extracts resolved. The limitation binds absent decomposition and scalar-attribution detail to the captured authors' abstract, not the uncaptured full paper. |
| `openclaw-rl-train-any-agent-simply-by-talking` | 09B-14 | **Added:** “OpenClaw-RL converts next-state signals from live user, tool, terminal, GUI, software-engineering, and tool-call interactions into rewards or token-level supervision for training a single policy through decoupled serving and training loops.” | Canonical source matched; SHA-256 `402ab2b7ad33eefce675641afb7c32fec9c363cf3c0fcd0d20638498d381c32b`; ingest PASS clean with all four extracts resolved. The snapshot does not establish checkpoint installation, persistence, acceptance validation, or rollback. |

## Completion record

| ID | disposition | target change | validation and source-review result |
|---|---|---|---|
| 09B-01 | narrowed | Replaced the general suggestion that summaries may lose diagnostic content with the exact online text-classification contrast: the fixed summary-without-traces arm reached 34.9% median accuracy versus 50.0% with full traces. The phase-gate implication remains target-side analysis. | Note and ingest PASS clean; source pair PASS in review job 8043; follow-up selector empty. |
| 09B-02 | narrowed | Scoped the repository-cheatsheet result to preliminary Qwen3.5-9B Studying-DSPy runs, named the forced 20-iteration catch-up, recorded the absent OpenClaw effect, and labeled the frontloading reading as the note's bounded transfer. | Note and ingest PASS clean; source pair PASS in review job 8044; follow-up selector empty. |
| 09B-03 | grounded | Expanded the governed-transition mechanism: current and old Erlang code may execute concurrently, a fully qualified call moves a process to current code, and loading a third version purges the old variant and terminates processes still using it. | Note PASS clean; ingest PASS with its pre-existing off-vocabulary `technical-documentation` genre warning; source pair PASS in review job 8045; follow-up selector empty. |
| 09B-04 | grounded | Replaced generic migration and rollback wording with versioned upgrade and downgrade plans, process-state migration, reboot into the old release after failed installation, and explicit downgrade. | Note PASS clean; ingest PASS with its pre-existing off-vocabulary `technical-documentation` genre warning; source pair PASS in review job 8045; follow-up selector empty. |
| 09B-05 | narrowed | Replaced the unsupported deoptimization claim with the captured V8 mechanism: dynamically updated HiddenClasses support shape-sensitive property optimization, while type pollution can prevent optimal-code generation. The footer now states that the capture does not establish deoptimization of already optimized code. | Note and ingest PASS clean; source pair PASS in review job 8045; follow-up selector empty. |
| 09B-06 | narrowed | Scoped the changed-agent example to the preliminary Qwen3.5-9B Studying-DSPy cheatsheet, low-budget gains, forced 20-iteration catch-up, and the absent OpenClaw effect. | Note and ingest PASS clean; source pair PASS in review job 8045; follow-up selector empty. |
| 09B-07 | grounded | Clarified that the MOP exposes selected language semantics through explicit generic-function entry points on metaobjects and that base classes opt into an alternative metaobject class. | Note and ingest PASS clean; source pair PASS in review job 8045; follow-up selector empty. |
| 09B-08 | grounded | Added the source's exact runtime-modification definition and its incompatibility, last-writer-overwrite, and source-versus-runtime-behavior risks. | Note and ingest PASS clean; source pair PASS in review job 8045; follow-up selector empty. |
| 09B-09 | retained local delta | Named ACM's summary-boundary/archive and identifier-query operations, added the three Qwen3.5-9B Pass@1 changes, and stated that the comparisons neither search the action basis nor train matched rival state representations. The fixed-update-space consequence remains the note's analysis. | Note and ingest PASS clean; source pair PASS in review job 8046; follow-up selector empty. |
| 09B-10 | retained local delta | Scoped Co-Harness to its two-round Qwen tool-integrated mathematical-reasoning experiment and named every mutable harness surface. The footer explicitly labels the broader-effective-update-space reading as the note's transfer. | Note and ingest PASS clean; source pair PASS in review job 8046; follow-up selector empty. |
| 09B-11 | narrowed | Replaced generic measurement language with the captured abstract's call for mathematical frameworks to understand and foster human–AI synergy. The absent decomposition and contribution-attribution detail is now bounded to that abstract, not inferred about the uncaptured paper. | Note and ingest PASS clean; source pair PASS in review job 8047; follow-up selector empty. |
| 09B-12 | narrowed | Replaced the absolute task/reward/demonstration/trace exclusion with the source's declared timing boundary: studying precedes information about downstream evaluation, task distribution, or reward, permits corpus-derived questions and rubrics, and does not separately audit every incidental setup signal. | Note and ingest PASS clean; source pair PASS in review job 8048; follow-up selector empty. |
| 09B-13 | grounded | Added the exact preliminary Qwen3.5-9B Studying-DSPy expertise values for the cheatsheet, base, synthetic-fine-tuning, and continual-pre-training arms, while retaining the one-of-two-domains and missing-uncertainty limits. | Note and ingest PASS clean; source pair PASS in review job 8049; follow-up selector empty. |
| 09B-14 | narrowed | Replaced a deployed weight-update lifecycle claim with what the capture establishes: live-interaction signals train one policy through decoupled serving and training loops. The note now denies evidence about checkpoint installation, persistence, acceptance validation, or rollback. | Note and ingest PASS clean; source pair PASS in review job 8049; follow-up selector empty. |
| 09B-15 | grounded | Added the two-round Qwen mathematical-reasoning scope, exact harness surfaces, verified-trajectory fine-tuning, and the missing isolation between additional harness search and training. | Note and ingest PASS clean; source pair PASS in review job 8050; follow-up selector empty. |
| 09B-16 | grounded | Retained the model–harness pair and exact mutable surfaces while stating that this is a conceptual boundary, not evidence of joint optimization or an exhaustive deployed-system definition. | Note and ingest PASS clean; source pair PASS in review job 8050; follow-up selector empty. |
| 09B-17 | grounded | Replaced loose end-to-end wording with the task-specific single-file Python harness surface—prompting, retrieval, memory, and orchestration—under frozen base weights, and named the fixed objective, proposer, and evaluation function outside that boundary. | Note and ingest PASS clean; source pair PASS in review job 8050; follow-up selector empty. |
| 09B-18 | grounded | Restated the paper's advocated human-agent pair as the unit of analysis for scientific collaboration and confined the absent decomposition and attribution detail to the captured abstract without inferring full-paper contents. | Note and ingest PASS clean; source pair PASS in review job 8050; follow-up selector empty. |

## Disposition distribution

| disposition | count | inventory rows |
|---|---:|---|
| grounded | 9 | 09B-03, 09B-04, 09B-07, 09B-08, 09B-13, 09B-15, 09B-16, 09B-17, 09B-18 |
| narrowed | 7 | 09B-01, 09B-02, 09B-05, 09B-06, 09B-11, 09B-12, 09B-14 |
| retained local delta | 2 | 09B-09, 09B-10 |

All 18 inventory rows have terminal dispositions. Source-as-gate review ran
under the `codex` partition in jobs 8043–8050. Because the cohort forbids
delegated writers, the review prompts were executed by the mutation owner and
finalized with runner `local-review-fallback`; all 18 pairs passed. The final
source selector is empty for all eight target notes. All target-note validations
are clean. Every ingest validation passes; the two Erlang documentation ingests
retain only their pre-existing off-vocabulary genre warnings.

## Identity and accumulation observation

The 18 demands produced 15 appended Claims entries across ten ingests and
reused two bridge incumbents from cohort 09a. The incumbent Meta-Harness
ablation entry serves 09B-01. The incumbent Co-Harness architecture entry
serves both 09B-10 and 09B-15. One new Machine Studying cheatsheet entry serves
09B-02 and 09B-06. This was deliberate reuse of the same source-side
proposition, not ambiguous selection.

The densest accumulation remained readable without claim IDs. Machine Studying
now separates the signal-timing definition, model–harness boundary, cheatsheet
budget pattern, and expertise-point comparison; protocol, timing, and metric
make each entry distinct. ACM needed two entries for one inventory row because
the target uses both the intervention mechanism and its reported outcomes.
Position's two entries separate an advocated unit of analysis from a future
framework call. Neither case created a near duplicate or competing identity.

No entry was disputed, no reconciliation was needed, and no ambiguous selector
or claim-ID pressure appeared. The recurring pressure was target-side scope,
not Claims identity: V8's capture omitted deoptimization; OpenClaw-RL omitted
checkpoint lifecycle; Machine Studying required domain, budget, timing, and
non-generalization bounds; the position-paper capture supported only
abstract-page negatives; and the ACM and Co-Harness experiments left important
decomposition choices or causal contributions unisolated.
