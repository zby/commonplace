# Cleanup cohort 10b — frozen 2026-08-24

**Status: complete (2026-08-25).** Frozen at repository `a91ed377`. Split from cohort 10
on 2026-08-24 to bound one agent's context; the original manifest's scope was
18 targets over 36 ingests.

This run uses the accepted direct-source design. Ingests retain only exact
source/location pairs in `## Quotes`. An ordinary ingest link declares those
quotes sufficient for that source use; a link whose visible text contains
`(snapshot required)` declares a dependency on the verified exact name-paired
snapshot. Target claims are checked directly against the selected source
material by `semantic/grounding-alignment`.

Scope: 9 targets, 18 ingests, 27 note-to-ingest pairs, and 1.41 MB of local
snapshots. The two bridge ingests shared historically with cohort 10a are
`goedel-machines-schmidhuber` and
`language-models-like-humans-show-content-effects-on-reasoning`; current quotes
in either file are preserved and judged before any append.

## Targets

| Target | Blob | Ingests |
|---|---|---|
| `a-proposal-selection-loop-requires-search-evaluation-and-retention` | `5c6cfc0e` | `goedel-machines-schmidhuber` |
| `an-omitted-loop-function-and-a-frozen-one-need-different-repairs` | `f32b01bd` | `autogenesis-a-self-evolving-agent-protocol`<br>`continual-harness-online-adaptation-foundation-agents`<br>`darwin-godel-machine-open-ended-evolution-self-improving-agents`<br>`huxley-godel-machine-human-level-coding-agent-development`<br>`hyperagents`<br>`self-harness-harnesses-that-improve-themselves`<br>`self-improving-ai-coding-agents-through-accumulated-rules` |
| `brainstorming-maintainability-oracles-for-agentic-development` | `9c3a8378` | `agentic-code-reasoning`<br>`huxley-godel-machine-human-level-coding-agent-development`<br>`towards-automating-eval-engineering-2079976006644072796`<br>`why-software-factories-fail-slopcodebench-2081797628552270027` |
| `compounding-is-tested-in-later-improvement-not-by-the-accepting-metric` | `68fdead9` | `agent-optimizers-compound-terminal-bench`<br>`harness-updating-is-not-harness-benefit`<br>`hyperagents`<br>`poetiq-perspective-on-recursive-self-improvement` |
| `computationally-directed-self-improvement-is-a-reallocation` | `933f5793` | `poetiq-perspective-on-recursive-self-improvement` |
| `epiplexity-by-example-what-entropy-and-complexity-miss` | `ae35ffc9` | `from-entropy-to-epiplexity-rethinking-information-computational` |
| `goedel-machines-are-a-proof-governed-case-of-self-modification` | `1b97b5ed` | `darwin-godel-machine-open-ended-evolution-self-improving-agents`<br>`goedel-machines-schmidhuber`<br>`huxley-godel-machine-human-level-coding-agent-development` |
| `structured-prompt-gains-do-not-establish-distribution-selection` | `1605d875` | `agentic-code-reasoning`<br>`from-entropy-to-epiplexity-rethinking-information-computational`<br>`language-models-like-humans-show-content-effects-on-reasoning` |
| `verifiable-subroles-before-reviewer-identity` | `2a43d52a` | `agentic-code-reasoning`<br>`beyond-not-novel-enough-llm-assisted-scholarly-critique`<br>`towards-automating-scientific-review-google-paper-assistant` |

## Source-blind claim inventory

Recorded from all nine frozen targets before opening any listed ingest or
snapshot.

| ID | target | claim as frozen | source-side need |
|---|---|---|---|
| PS-1 | `a-proposal-selection-loop-requires-search-evaluation-and-retention` | Gödel machines sit inside proposal selection at its formal extreme because a proof-mediated gate separates adoption from candidate generation and makes the three functions operative. | Whether Schmidhuber's construction searches for self-rewrites, rejects them unless a switching proof succeeds, and installs an accepted rewrite. |
| PS-2 | `a-proposal-selection-loop-requires-search-evaluation-and-retention` | Ashby's Homeostat responds to an out-of-bounds essential variable by randomly changing parameters; the same transition displaces the incumbent and generates its successor, while restored viability persists without a distinct acceptance operation. | The Homeostat's out-of-bounds trigger, random parameter changes, and persistence after essential variables return to viable bounds. |
| PS-3 | `a-proposal-selection-loop-requires-search-evaluation-and-retention` | The Homeostat also admits an analyst's variation–selection–retention reconstruction in which random variation, a one-bit viability boundary, and survival through non-displacement mark the functional floor of the three roles. | Whether Ashby's mechanism supplies repeated random configurations, viability-governed continuation, and persistence through equilibrium, while leaving the functional reconstruction as target-side analysis. |
| PS-4 | `a-proposal-selection-loop-requires-search-evaluation-and-retention` | Online gradient descent adopts each update dictated by revealed cost without a reject-capable evaluator, and Zinkevich's Greedy Projection/GIGA result is a technical counterexample to treating an acceptance gate as universal. | Zinkevich's update rule and result, especially whether the algorithm exposes any independently rejectable proposal. |
| PS-5 | `a-proposal-selection-loop-requires-search-evaluation-and-retention` | MAPE-K originates in Kephart and Chess's autonomic-computing vision without a membership test, and neighboring work treats it and related loops as engineering reference models rather than definitions of adaptation. | What Kephart and Chess introduce, whether their vision supplies a membership test, and how Weyns characterizes self-adaptive loop models. |
| PS-6 | `a-proposal-selection-loop-requires-search-evaluation-and-retention` | A systematic review finds no settled formal definition of self-adaptive systems from which one loop architecture follows. | The scope and conclusion of Petrovska, Erjiage, and Kugele's review about formal definitions in the self-adaptive-systems literature. |
| OF-1 | `an-omitted-loop-function-and-a-frozen-one-need-different-repairs` | Self-Harness is proposal selection: one model mines failure signatures and proposes several bounded harness edits, while a fixed two-split pass-count rule can reject them and repeatedly consults its nominally held-out split. | Self-Harness's candidate-generation procedure and exact two-split admission rule, including reuse of the held-out split. |
| OF-2 | `an-omitted-loop-function-and-a-frozen-one-need-different-repairs` | Gate-passing Self-Harness edits are merged and exercised later, but no criterion-driven retirement path is reported. | What happens to accepted edits in later evaluations and whether the reported lifecycle includes retirement. |
| OF-3 | `an-omitted-loop-function-and-a-frozen-one-need-different-repairs` | Continual Harness is direct update: a Refiner reads recent trajectory windows and directly determines edits to prompts, sub-agents, skills, and memory; no independently rejectable candidate is exposed, and edits enter the next step. | The Refiner's inputs, editable surfaces, update/install timing, and whether a separate accept/reject stage exists. |
| OF-4 | `an-omitted-loop-function-and-a-frozen-one-need-different-repairs` | Continual Harness exercises prompt and harness changes, but memory reuse is sparse, most authored skills go unused, and limited deletion and demotion do not establish system-wide retirement. | Reported later use of each artifact type and the scope of deletion or demotion mechanisms. |
| OF-5 | `an-omitted-loop-function-and-a-frozen-one-need-different-repairs` | Autogenesis exposes typed Reflect/Select/Improve operations and a reject-capable Evaluate operation, but its objective, acceptance rule, and learnability mask remain protocol state outside the loop's update space. | Autogenesis's typed operators, rejection behavior, learnability mask, and which governing protocol fields the loop can revise. |
| OF-6 | `an-omitted-loop-function-and-a-frozen-one-need-different-repairs` | Autogenesis supplies versioned commit, lineage, and rollback; these establish recoverability but not criterion-driven retirement. | The reported versioning, lineage, rollback, and any distinct retirement mechanism. |
| OF-7 | `an-omitted-loop-function-and-a-frozen-one-need-different-repairs` | In Accumulated Behavioral Rules, an engineer turns an accepted code-review correction into a candidate reusable rule and decides whether the instance generalizes, leaving the acceptance judgment frozen at the instance level. | Who proposes and approves a generalized rule, from what review event, and what automated or human gate applies. |
| OF-8 | `an-omitted-loop-function-and-a-frozen-one-need-different-repairs` | The paper reports rule loading through two interfaces and no recurrence across 74 post-rule exposures, without a control that isolates causal uptake. | The two loading interfaces, the 74-exposure result, and whether a matched condition isolates the retained rule's causal effect. |
| OF-9 | `an-omitted-loop-function-and-a-frozen-one-need-different-repairs` | The rule file is append-friendly and supports in-place refinement, while removal is described inconsistently as rare and as prohibited. | The permitted rule-file operations and every statement about refinement or removal. |
| OF-10 | `an-omitted-loop-function-and-a-frozen-one-need-different-repairs` | Darwin Gödel Machine uses a fixed external model to read an archive agent's logs and propose a descendant edit, while benchmark score steers parent sampling. | The proposer, its inputs, descendant construction, archive-parent sampling, and benchmark score's role. |
| OF-11 | `an-omitted-loop-function-and-a-frozen-one-need-different-repairs` | Darwin Gödel Machine admits children through a fixed viability filter requiring compilation and retained code-editing ability even when benchmark score regresses. | The exact archive-admission conditions and whether benchmark improvement is required for admission. |
| OF-12 | `an-omitted-loop-function-and-a-frozen-one-need-different-repairs` | Darwin Gödel Machine's archive is monotonic by design; its greedy variant falls from 50.0% to 39.7%, making non-retirement part of the stepping-stone search mechanism rather than an oversight. | The archive retention policy, rationale for retaining regressions, and the reported greedy-variant scores. |
| OF-13 | `an-omitted-loop-function-and-a-frozen-one-need-different-repairs` | Darwin Gödel Machine hides a hallucination evaluator to defend against objective hacking and freezes its exploration controller as a compute compromise; those defenses do not establish that the ordinary viability gate should remain fixed. | Which components are hidden or fixed, the stated objective-hacking and compute rationales, and the distinction from the ordinary viability gate. |
| OF-14 | `an-omitted-loop-function-and-a-frozen-one-need-different-repairs` | HyperAgents uses a selected hyperagent to rewrite a unified task/meta-agent program that generates later descendants, making the main pathway proposal selection. | HyperAgents's editable program, descendant-generation mechanism, and selection/install path. |
| OF-15 | `an-omitted-loop-function-and-a-frozen-one-need-different-repairs` | Main HyperAgents experiments hold viability checks, evaluators, and a handcrafted parent selector fixed; an appendix makes parent selection editable but leaves evaluation and the outer archive fixed. The learned selector does not significantly beat random and remains below the handcrafted selector. | Fixed versus editable outer-loop components in main and appendix experiments, plus learned-, random-, and handcrafted-selector results and significance. |
| OF-16 | `an-omitted-loop-function-and-a-frozen-one-need-different-repairs` | HyperAgents replays selected patch lineages into later generations and preserves archive variants, but reports no system-wide semantic retirement path. | How selected patches become inputs to later generations, what the archive retains, and whether semantic retirement exists. |
| OF-17 | `an-omitted-loop-function-and-a-frozen-one-need-different-repairs` | Huxley-Gödel Machine substitutes a benchmark estimate for the original utility proof, and immediate benchmark score can be a weak selector for long-run lineage productivity. | Huxley's acceptance or selection mechanism and evidence comparing immediate agent score with descendant-lineage productivity. |
| OF-18 | `an-omitted-loop-function-and-a-frozen-one-need-different-repairs` | HyperAgents reports one cross-domain contribution by retained improvement machinery but does not establish sustained compounding. | The cross-domain transfer design and result, plus the later-evolution comparison needed to assess sustained compounding. |
| MO-1 | `brainstorming-maintainability-oracles-for-agentic-development` | Huxley-Gödel Machine shows that immediate benchmark performance can mis-rank long-run lineage productivity. | The experiment relating an agent's immediate benchmark score to the later productivity of its lineage. |
| MO-2 | `brainstorming-maintainability-oracles-for-agentic-development` | Part II of Why Software Factories Fail places human judgment at pre-implementation and program-design decision surfaces. | The exact workflow surfaces and human responsibilities asserted in the cited Part II post. |
| MO-3 | `brainstorming-maintainability-oracles-for-agentic-development` | Agentic Code Reasoning suggests semi-formal premises and execution traces improve soft, execution-free code verification while leaving a nontrivial error rate. | The prompt intervention, verification task, comparative gains, and residual error or failure rate. |
| MO-4 | `brainstorming-maintainability-oracles-for-agentic-development` | SlopCodeBench incrementally reveals requirements and uses held-out black-box tests to expose accumulated defects; Horthy's small run distinguishes development trajectories but does not show that strict pass or static slop metrics are sufficient maintainability oracles. | Benchmark construction, metrics, sample/run scope, trajectory results, and the limits of any maintainability interpretation. |
| MO-5 | `brainstorming-maintainability-oracles-for-agentic-development` | Eval Engineering mines production traces into reproducible tasks, inspects verifier trajectories, and keeps the user involved while the evaluation target is still being specified. | The workflow stages, trace inputs, verifier inspection, and user's role in target specification. |
| CP-1 | `compounding-is-tested-in-later-improvement-not-by-the-accepting-metric` | HyperAgents transfers whole implementations from joint paper-review and robotics runs into unseen math grading, freezes each transferred meta-agent component for 50 later generation steps, and reports median Improvement@50 of 0.630 with a 95% bootstrap interval of 0.540–0.630 across five runs. | The transfer sources and target, frozen components, number of steps and runs, metric, estimate, interval, and comparison with the initial hyperagent. |
| CP-2 | `compounding-is-tested-in-later-improvement-not-by-the-accepting-metric` | Direct use of the transferred procedure establishes one cross-domain contribution, but it does not isolate bundled task/meta changes; continued evolution reaches 0.640 versus 0.610 without statistical significance, so sustained compounding remains unestablished. | Whether the transferred procedure directly generates later agents, what is bundled, and the continued-evolution comparison with its statistical result. |
| CP-3 | `compounding-is-tested-in-later-improvement-not-by-the-accepting-metric` | Agent Optimizers defines a two-phase test requiring first-round gains to transfer and an equal-budget second round to improve the retained agent without erasing old successes; only RELAI-VCL shows both, at 79.2%, 72.7%, and 77.3% across the stated checkpoints. | The two-phase protocol, budgets, task sets, method comparison, and exact RELAI-VCL results. |
| CP-4 | `compounding-is-tested-in-later-improvement-not-by-the-accepting-metric` | The Agent Optimizers design lacks an equal-budget fresh start on the combined task set and an observed reinvestment trace; fixed 200-rollout phases therefore do not show that Phase 1 made Phase 2 more productive. | Starting states and controls for Phase 2, rollout budgets, and any measured path by which retained competence saves and reallocates resources. |
| CP-5 | `compounding-is-tested-in-later-improvement-not-by-the-accepting-metric` | Harness Updating Is Not Harness Benefit separates update production, persistent retention, artifact loading, judged procedural match, and task benefit; the ladder localizes shortfalls but does not itself establish causal uptake or feedback into later improvement. | The study's separately reported update and benefit stages and which causal links its measurements do or do not test. |
| CP-6 | `compounding-is-tested-in-later-improvement-not-by-the-accepting-metric` | Controlled evolver–agent cross-pairing supports the outcome comparison, while SkillsBench adherence is assigned by a Sonnet 4.6 rubric judge without a matched condition withholding or replacing the target skill; prompts, editable surfaces, streams, and anchors remain fixed. | Cross-pairing design, SkillsBench loading/adherence measurement, judge and rubric, controls, and fixed experimental boundaries. |
| CP-7 | `compounding-is-tested-in-later-improvement-not-by-the-accepting-metric` | Poetiq describes sequential benchmark wins and retained cross-task strategies as compounding without a removal, fresh-start, or displaced later-episode comparison. | Poetiq's reported sequential gains and retained strategies, its use of “compounding,” and whether any removal, fresh-start, or displaced comparison is run. |
| CR-1 | `computationally-directed-self-improvement-is-a-reallocation` | Poetiq's zero-human-intervention result is scoped to harness construction after people choose the task, data, objective, evaluator, and outer process. | The exact interval counted as zero-human-intervention and the decisions or machinery humans supply before and around that interval. |
| EP-1 | `epiplexity-by-example-what-entropy-and-complexity-miss` | Epiplexity is the area under a bounded learner's loss curve above final loss and therefore measures observer-relative extractable structure, unlike surprisal, entropy, or Kolmogorov complexity once each formal setup is fixed. | Finzi et al.'s definition, learner and budget dependence, prequential measurement, and contrast with entropy or description complexity. |
| EP-2 | `epiplexity-by-example-what-entropy-and-complexity-miss` | For `AB` repeated eight times, a stylized bounded learner's loss drops from roughly 1 to 0 and yields about 2.6 bits of epiplexity; a random sequence's flat loss gives zero area above final loss. | Whether the formal measure licenses this illustrative calculation and the conditions under which flat irreducible loss has zero epiplexity. |
| EP-3 | `epiplexity-by-example-what-entropy-and-complexity-miss` | AES ciphertext can have different epiplexity for a key-holding observer and one without the key because cheap preprocessing and side information belong to the observer; acquiring the key changes extractability without changing the bytes. | Whether keys, side information, and bounded preprocessing are part of the observer and whether the encrypted-message example is supplied or licensed by the formalism. |
| EP-4 | `epiplexity-by-example-what-entropy-and-complexity-miss` | Shuffling a textbook can preserve symbol statistics and near-preserve description complexity while reducing extractable structure for a student more than for an expert. | Whether ordering and prior expertise may change epiplexity for fixed data content, and whether this textbook example is source-supplied or target-side extrapolation. |
| EP-5 | `epiplexity-by-example-what-entropy-and-complexity-miss` | Bounded observers extract no useful structure from CSPRNG output, whereas a decompressor can expose rich structure in a compressed file that also looks statistically random; regeneration alone is not hidden meaning. | Finzi et al.'s CSPRNG result and the extent to which the CSPRNG/compressed-file contrast follows from it. |
| EP-6 | `epiplexity-by-example-what-entropy-and-complexity-miss` | Chess notation has different epiplexity for non-player, beginner, club player, and grandmaster observers because their rules, pattern knowledge, and computational capacity differ. | Whether the observer-relative formalism licenses expertise-graded extraction and whether the chess example is source-supplied or target-side extrapolation. |
| GM-1 | `goedel-machines-are-a-proof-governed-case-of-self-modification` | A Gödel machine can rewrite all of its code, including its proof searcher, but executes a rewrite only after proving that switching now has greater expected utility than continuing search under axioms for hardware, initial code, environment, and utility. | The rewritable surface, target theorem, switch behavior, and contents of the formal axiomatization. |
| GM-2 | `goedel-machines-are-a-proof-governed-case-of-self-modification` | The construction realizes proposal search, reject-capable proof evaluation, proof-checker authority, and operative retention; passing the checker invokes and installs the replacement as subsequent code. | The proof-technique enumeration, proof checking, invocation path, and persistence of the replacement program. |
| GM-3 | `goedel-machines-are-a-proof-governed-case-of-self-modification` | The Global Optimality Theorem compares switching now with continuing a search that includes possible later rewrites, applies “no local maxima” to the self-modification sequence, and accounts for later self-modifications without a separate meta-level regress. | The theorem's comparison, scope of the optimality/no-local-maxima claim, and treatment of later self-modifications. |
| GM-4 | `goedel-machines-are-a-proof-governed-case-of-self-modification` | A Gödel machine must ignore improvements whose effectiveness it cannot prove; its guarantee is conditional on the encoded axioms and utility, and consistency is assumed rather than proved. | The paper's stated unprovability limitation and assumptions about consistency, soundness, and utility formalization. |
| GM-5 | `goedel-machines-are-a-proof-governed-case-of-self-modification` | Schmidhuber describes a theoretical construction and reports neither an implementation nor experiments. | Whether the cited work implements or empirically evaluates a Gödel machine. |
| GM-6 | `goedel-machines-are-a-proof-governed-case-of-self-modification` | Darwin Gödel Machine explicitly replaces utility proof with empirical search pressure: viability decides archive admission and benchmark score weights later reproduction rather than acceptance. | The paper's stated relation to the original Gödel machine and the distinct roles of viability and benchmark score. |
| GM-7 | `goedel-machines-are-a-proof-governed-case-of-self-modification` | Huxley-Gödel Machine estimates a lineage's future value from benchmark evidence. | Huxley's estimated quantity, benchmark evidence, and role of that estimate in selecting agents or lineages. |
| GM-8 | `goedel-machines-are-a-proof-governed-case-of-self-modification` | Incremental Self-Improvement retains policy changes using reward history and rollback as acceptance evidence. | The exact retention and rollback rule in the cited local system review and its underlying source. |
| SP-1 | `structured-prompt-gains-do-not-establish-distribution-selection` | Agentic Code Reasoning reports 5–12 percentage-point gains from semi-formal reasoning templates on code-verification tasks but no Claude Sonnet gain on code QA: 84.8% with the template versus 85.3% without. | The intervention, models and tasks, reported gain range, exact Claude comparison, and study scope. |
| SP-2 | `structured-prompt-gains-do-not-establish-distribution-selection` | Lampinen et al. find that chain-of-thought partly reduces content bias on abstract or unfamiliar reasoning without degrading familiar-condition performance; content effects nevertheless persist across tested scaling and tuning conditions. | The reasoning tasks and conditions, chain-of-thought intervention, content-effect direction, and how effects vary with model scale or tuning. |
| SP-3 | `structured-prompt-gains-do-not-establish-distribution-selection` | Epiplexity shows that data arrangement can change what a bounded learner extracts, but the formal result concerns learning from ordered data rather than inference-time prompts or activation of pretraining subsets. | Finzi et al.'s arrangement/order result, learning setting, and any stated connection or absence of connection to inference-time prompting. |
| VS-1 | `verifiable-subroles-before-reviewer-identity` | Google's Paper Assistant Tool segments manuscripts, sends logical sections to specialized deeper-review agents, then grounds, deduplicates, and synthesizes their findings. | PAT's manuscript decomposition, agent roles, grounding, deduplication, and synthesis pipeline. |
| VS-2 | `verifiable-subroles-before-reviewer-identity` | PAT's strongest evaluation surface is a filtered SPOT subset of equation and proof errors backed by verified errata or retractions, making technical-error detection narrower and more verifiable than generic peer review. | Construction and verification of the SPOT subset, error types, labels, and evaluation scope. |
| VS-3 | `verifiable-subroles-before-reviewer-identity` | Repeated independent PAT calls can raise recall while lowering precision, so pass@k-style expansion can enlarge the human inspection burden. | The repeated-call aggregation experiment and its reported recall/precision tradeoff. |
| VS-4 | `verifiable-subroles-before-reviewer-identity` | Beyond “Not Novel Enough” studies human novelty reviews, extracts reviewer patterns, retrieves related work, builds landscape and novelty-delta structures, and evaluates reasoning alignment separately from conclusion agreement. | The pipeline stages and distinct evaluation measures for novelty reasoning and conclusions. |
| VS-5 | `verifiable-subroles-before-reviewer-identity` | Agentic Code Reasoning's semi-formal process templates improve execution-free verification by forcing premises, traces, and conclusions into inspectable form. | The template fields, execution-free verification setup, comparative performance, and limits. |


## Source-demand plan and grounding record

All 18 exact name-paired snapshots passed canonical-source equality and
exact-byte SHA-256 verification before source reading. Each route below is
selected per source-dependent use. Only exact source quotes or the verified
snapshot supply source support.

| Ingest | Inventory IDs | Route and result | Snapshot identity | Validation |
|---|---|---|---|---|
| `goedel-machines-schmidhuber` | PS-1, GM-1–GM-5 | PS-1: `quotes sufficient` from the three incumbent passages. GM-1–GM-5: `snapshot required`; the combined use spans axiomatization, proof machinery, provability limits, later rewrites, and the paper's theoretical status, so a bounded retained set would omit material context. | `d70201102d8f00e7e65cf36a8a89733256d8f163b6b6439941662c47c51fc1f7` verified. | Direct snapshot judgment completed; target marker required for GM-1–GM-5. |
| `autogenesis-a-self-evolving-agent-protocol` | OF-5–OF-6 | OF-5: `quotes added`; the 5 recovered passages cover the typed operators, reject-capable Evaluate step, learnability mask, commit gate, lineage, and rollback. OF-6: `snapshot required`; distinguishing rollback from a distinct criterion-driven retirement mechanism requires checking the protocol as a whole. | `631aa4f497520508eed673a06de7d7bc4bd001e92f6823a633bbbac2b835e613` verified. | PASS; 5 quotes resolve OF-5; target marker required for OF-6. |
| `continual-harness-online-adaptation-foundation-agents` | OF-3–OF-4 | OF-3: `quotes added`; the 7 recovered passages cover the Refiner, editable surfaces, direct next-step installation, and component operations. OF-4: `snapshot required`; the system-wide negative about retirement and uneven use across artifact types depends on the full reported lifecycle. | `a4730b3e25827c12c1ac3cb1734d9095669c2fabb1d51a62047e5b1bbbe38b07` verified. | PASS; 7 quotes resolve OF-3 and the positive parts of OF-4; target marker required for OF-4. |
| `darwin-godel-machine-open-ended-evolution-self-improving-agents` | OF-10–OF-13, GM-6 | `quotes added`: recovered 12 exact pairs for all five uses. | `9ce2d857b213c66107e0b81be2f281bf691f6812d5146c89a83542e8041aa086` verified. | PASS; 12 quotes resolve. |
| `hyperagents` | OF-14–OF-16, OF-18, CP-1–CP-2 | OF-14–OF-15, OF-18, and CP-1: `quotes added`; 13 recovered passages cover the unified editable program, fixed and appendix-modified parent selection, archive behavior, transfer protocol, and reported results. OF-16: `snapshot required` for the system-wide negative about semantic retirement. CP-2: `snapshot required` because the bundled transfer and the absence of a significant sustained-compounding result depend on the experiment-level comparison. | `bfb5c4f6723cfeed3410392c7fdd2c390fa29406efd390fc4af61b0ead5d5c25` verified. | PASS; 13 quotes resolve four uses; target markers required for OF-16 and CP-2. |
| `self-harness-harnesses-that-improve-themselves` | OF-1–OF-2 | OF-1: `quotes added`; the 6 recovered passages cover candidate generation, the two-split admission rule, accepted-edit merging, and later evaluation. OF-2: `snapshot required`; the protocol-wide absence of criterion-driven retirement cannot be established from a bounded positive extract set. | `28b4792629559f4ffd2bb587a64ee281d5f13a561cc0b49b1d36358cc1d63b11` verified. | PASS; 6 quotes resolve OF-1 and the positive part of OF-2; target marker required for OF-2. |
| `self-improving-ai-coding-agents-through-accumulated-rules` | OF-7–OF-9 | `quotes added`: recovered 8 exact pairs for all three uses. | `485cd1c053eef5f1717c2c6309d109500b0dfa1564efb9d8b347a438923684ff` verified. | PASS; 8 quotes resolve. |
| `huxley-godel-machine-human-level-coding-agent-development` | OF-17, MO-1, GM-7 | `snapshot required` for all three uses after the recovery request failed. The snapshot establishes empirical clade-metaproductivity, DGM/HGM correlation results, and HGM's estimated-CMP expansion policy. | `bd3815e8d12e57a57c26c0976ba6f778fea3da45fe3f9edc4f56cfd38eb9482a` verified. | Direct snapshot judgment completed; target markers required; ingest remains clean. |
| `agentic-code-reasoning` | MO-3, SP-1, VS-5 | `quotes added`: 6 bounded passages cover the semi-formal intervention, execution-free setup, task gains, residual error, exact Sonnet comparison, and inspectable template. | `acd2639d1e6041491cf9130a7d308cd5d69b8b735011991594f9d5f7d0a1a7ad` verified. | PASS; 6 quotes resolve. |
| `towards-automating-eval-engineering-2079976006644072796` | MO-5 | `quotes added`: 4 passages cover repository/trace mining, user selection, production-contract reconstruction, and inspection of both agent and verifier trajectories. | `0a5c82a3ca1c324cf77cc76c56794f09c8dcc680e6d747fd0dc268fb7a54a46f` verified. | PASS; 4 quotes resolve. |
| `why-software-factories-fail-slopcodebench-2081797628552270027` | MO-4 | `quotes added`: 6 passages cover incremental disclosure, the 3-problem/17-checkpoint/9-run scope, inherited held-out tests, results, and the author's limit on static quality metrics. | `bf4776cc6b2ddc1e8494dd21481e3ba2b7fe5a96483affefe115ebf17d30dd7c` verified. | PASS; 6 quotes resolve. |
| `agent-optimizers-compound-terminal-bench` | CP-3–CP-4 | CP-3: `quotes added`, with 4 passages covering the two-phase test, budgets, task expansion, and exact results. CP-4: `snapshot required`; the absence of a fresh combined-task start and of a measured reinvestment path is a protocol-wide negative claim. | `08b1a1e55d05498fd3e71b2407df86bec90dce73ca7b6ce244c325f3854a0847` verified. | PASS; 4 quotes resolve; target marker required for CP-4. |
| `harness-updating-is-not-harness-benefit` | CP-5–CP-6 | CP-5: `quotes added`, with 6 passages separating persistent update, next-step reuse, skill loading, rubric-judged adherence, and pass-when-loaded. CP-6: `snapshot required`; its controlled-boundary and missing matched-withholding claims depend on the experiment and appendices together. | `453897c0e4c13dd6cb076cb2d33fc83fcd3d8bd4348633f4f0d554beb0dbe4cd` verified. | PASS; 6 quotes resolve; target marker required for CP-6. |
| `poetiq-perspective-on-recursive-self-improvement` | CP-7, CR-1 | `snapshot required` for both uses. CP-7 combines a vendor's sequential-result narrative with a protocol-wide negative-control check; CR-1 scopes “zero human intervention” against human-selected problems, datasets, objectives, and the surrounding process. Neither is soundly judgeable from a few excerpts. | `25a04abaa343d73ba6f395caf537472ede25f923bbd0b3754479e2722317970d` verified. | Direct snapshot judgment completed; target markers required. |
| `from-entropy-to-epiplexity-rethinking-information-computational` | EP-1–EP-6, SP-3 | `quotes added`: 6 passages cover the computationally bounded observer, time-bounded MDL, the prequential area heuristic, CSPRNG result, ordering effect, and observer dependence. The snapshot does not contain the target's AB, AES, textbook, compressed-file, or chess examples; those may remain only as explicit local worked examples, not source-supplied cases. SP-3's prompt transfer is likewise local analysis. | `26b4a18ec4bb6d004541946818245bd10a588d9e006c80356ea7171d0cc4c7e2` verified. | PASS with two pre-existing missing-link warnings for `../notes/definitions/distillation.md`; 6 quotes resolve; target attribution must be repaired. |
| `language-models-like-humans-show-content-effects-on-reasoning` | SP-2 | `quotes added`: 3 passages supplement the 3 incumbent quotes with the Wason chain-of-thought improvement, its bounded “can, in some cases” interpretation, and persistence across model size/tuning. The snapshot does not establish the frozen no-degradation clause, which must be removed. | `cfd34d847c87ad80812295940b4ea41c8a5c49f1b09ba25c1edaf69ce09e9faa` verified. | PASS; all 6 quotes resolve; target narrowing required. |
| `beyond-not-novel-enough-llm-assisted-scholarly-critique` | VS-4 | `snapshot required`. One 6-pair append request failed atomically because its final extract joined the separately bulleted Reasoning Alignment and Decision Alignment items; the incumbent was restored and no repair append was attempted. The verified snapshot contains the complete pipeline and evaluation context. | `8cea8bd658eba13a6a21e20e260bc91a1013ce7dfc911cd563254e870143288c` verified. | Restored ingest PASS (clean); target marker required. |
| `towards-automating-scientific-review-google-paper-assistant` | VS-1–VS-3 | `snapshot required`. One 6-pair append request failed atomically because the Pass@k extract capitalized source-internal lowercase “while”; the incumbent was restored and no repair append was attempted. The verified snapshot contains the full pipeline, SPOT construction, and repeated-call result. | `f59fc1c24f3f7bbd5b8aa8683a2e94872a6d41c4c844714ddce054449f0a5cb0` verified. | Restored ingest PASS (clean); target marker required. |

Literature handoffs outside the owned source manifest are terminal for this
cohort: PS-2–PS-3 (Ashby), PS-4 (Zinkevich), PS-5 (Kephart and Chess plus
Weyns), PS-6 (Petrovska, Erjiage, and Kugele), MO-2 (Why Software Factories
Fail Part II), and GM-8 (the source underlying the local Incremental
Self-Improvement review).

### Mechanical quote recovery

| Ingest | Expected | Incumbent exact pairs | Appended | Rejected | Result |
|---|---:|---:|---:|---:|---|
| `autogenesis-a-self-evolving-agent-protocol` | 5 | 0 | 5 | 0 | Added in one verified request; PASS. |
| `continual-harness-online-adaptation-foundation-agents` | 7 | 0 | 7 | 0 | Added in one verified request; PASS. |
| `darwin-godel-machine-open-ended-evolution-self-improving-agents` | 12 | 0 | 12 | 0 | Added in one verified request; PASS. |
| `hyperagents` | 13 | 0 | 13 | 0 | Added in one verified request; PASS. |
| `self-harness-harnesses-that-improve-themselves` | 6 | 0 | 6 | 0 | Added in one verified request; PASS. |
| `self-improving-ai-coding-agents-through-accumulated-rules` | 8 | 0 | 8 | 0 | Added in one verified request; PASS. |
| `huxley-godel-machine-human-level-coding-agent-development` | 3 | 0 | 0 | 3 | Atomic request rejected before write: pairs 1 and 2 matched but were not appended; pair 3 did not match because the recovered text silently joined snapshot bytes `SWE-Verified-\n60` as `SWE-Verified-60`. No repair append was attempted. |
| **Total** | **54** | **0** | **51** | **3** | All recovered pairs accounted for; six requests passed and one request failed closed. |

## Completion record

Each frozen use now has a terminal target disposition. Deterministic validation
and the fresh operational review are recorded below rather than repeated in
every row.

| ID | Disposition | Source route | Target repair |
|---|---|---|---|
| PS-1 | grounded | quotes sufficient | Retained the Gödel-machine limit case and its ordinary ingest link. |
| PS-2 | literature handoff | linked local source review; primary source outside manifest | Attributed the mechanism to the local Ashby review and marked the loop classification as this note's analysis. |
| PS-3 | literature handoff | linked local source review; primary source outside manifest | Retained the variation–selection–retention reading explicitly as an analyst's reconstruction. |
| PS-4 | literature handoff | Zinkevich source outside manifest | Removed the online-gradient-descent and GIGA source claim. |
| PS-5 | literature handoff | Kephart/Chess and Weyns sources outside manifest | Removed the MAPE-K field-characterization claim. |
| PS-6 | literature handoff | Petrovska et al. source outside manifest | Removed the systematic-review claim while retaining the note's locally scoped conclusion. |
| OF-1 | grounded | quotes added | Retained the Self-Harness proposal and two-split gate reading with an ordinary ingest link. |
| OF-2 | grounded | snapshot required | Added a marked Self-Harness lifecycle link for later use and the protocol-wide retirement negative. |
| OF-3 | grounded | quotes added | Retained the Continual Harness direct-update classification with an ordinary ingest link. |
| OF-4 | grounded | snapshot required | Added a marked Continual Harness lifecycle link for uneven use and system-wide retirement scope. |
| OF-5 | grounded | quotes added | Retained the Autogenesis operators, rejection, and frozen protocol fields with an ordinary link. |
| OF-6 | grounded | snapshot required | Added a marked Autogenesis lifecycle link to distinguish rollback from retirement. |
| OF-7 | grounded | quotes added | Retained the engineer-mediated rule proposal and acceptance reading. |
| OF-8 | grounded | quotes added | Retained the two loading interfaces, 74-exposure result, and missing-control qualification. |
| OF-9 | grounded | quotes added | Retained the refinement and inconsistent-removal reading. |
| OF-10 | grounded | quotes added | Retained the DGM proposer, archive-parent, and benchmark-score roles. |
| OF-11 | grounded | quotes added | Retained the compile-and-edit viability filter and score-regression qualification. |
| OF-12 | grounded | quotes added | Retained monotonic archive behavior, stepping-stone rationale, and greedy scores. |
| OF-13 | grounded | quotes added | Retained the distinct protective and affordable freeze rationales. |
| OF-14 | grounded | quotes added | Retained the HyperAgents editable-program and descendant-generation reading. |
| OF-15 | grounded | quotes added | Retained the main/appendix edit-boundary comparison and selector results. |
| OF-16 | grounded | snapshot required | Added a marked HyperAgents lifecycle link for archive behavior and the retirement negative. |
| OF-17 | grounded | snapshot required | Marked the Huxley ingest link used for empirical utility substitution and lineage-productivity evidence. |
| OF-18 | grounded | quotes added | Retained the bounded cross-domain contribution and no-sustained-compounding qualification. |
| MO-1 | grounded | snapshot required | Marked the Huxley link supporting immediate-score and lineage-productivity mis-ranking. |
| MO-2 | literature handoff | Why Software Factories Fail Part II outside manifest | Removed the source attribution and retained the decision surfaces as this note's proposal. |
| MO-3 | grounded | quotes added | Retained the semi-formal, execution-free verification result and residual-error qualification. |
| MO-4 | grounded | quotes added | Retained the SlopCodeBench protocol, small-run result, and oracle-scope limit. |
| MO-5 | grounded | quotes added | Retained the trace-mining, verifier-inspection, and user-specification workflow. |
| CP-1 | grounded | quotes added | Retained the HyperAgents transfer protocol, five-run scope, and Improvement@50 result. |
| CP-2 | grounded | snapshot required | Added a marked experiment link for bundled transfer and the nonsignificant continued-evolution comparison. |
| CP-3 | grounded | quotes added | Retained the Agent Optimizers two-phase protocol, budgets, and RELAI-VCL results. |
| CP-4 | grounded | snapshot required | Added a marked protocol link for the missing fresh-start control and reinvestment trace. |
| CP-5 | grounded | quotes added | Retained the Harness Updating measurement ladder and missing feedback edge. |
| CP-6 | grounded | snapshot required | Added a marked experiment link for cross-pairing, rubric judgment, controls, and fixed boundaries. |
| CP-7 | grounded | snapshot required | Marked the Poetiq source link for its broad sequential-compounding and missing-control use. |
| CR-1 | grounded | snapshot required | Marked the Poetiq source link for the bounded zero-human-intervention scope. |
| EP-1 | contradicted/repaired | quotes added | Corrected the definition from the prequential area heuristic to time-bounded MDL and labeled the area method as heuristic. |
| EP-2 | retained local delta | quotes added for the framework | Labeled the `AB` calculation and 2.6-bit value as a toy proxy, not a paper result. |
| EP-3 | retained local delta | quotes added for observer dependence | Labeled the AES/key example as this note's worked extrapolation under a stipulated toolkit. |
| EP-4 | retained local delta | quotes added for ordering dependence | Labeled the textbook example as a local extrapolation rather than a source-supplied case. |
| EP-5 | narrowed | quotes added | Kept the source's negligible-CSPRNG result, narrowed its wording, and identified the compressed-file contrast as local. |
| EP-6 | retained local delta | quotes added for observer dependence | Labeled the expertise-graded chess example as a local extrapolation. |
| GM-1 | grounded | snapshot required | Marked the Schmidhuber links covering the rewritable surface, target theorem, and axiomatization. |
| GM-2 | grounded | snapshot required | Used the same marked source route for proof search, checker authority, invocation, and retention. |
| GM-3 | grounded | snapshot required | Used the marked source route for the Global Optimality Theorem and later rewrites. |
| GM-4 | grounded | snapshot required | Marked the source citation for unprovable improvements and formalization assumptions. |
| GM-5 | grounded | snapshot required | Used the marked source route for the paper's theoretical, non-empirical status. |
| GM-6 | grounded | quotes added | Retained the DGM viability-admission and benchmark-reproduction distinction with an ordinary link. |
| GM-7 | grounded | snapshot required | Marked the Huxley link for estimated future lineage value. |
| GM-8 | literature handoff | linked local system review; underlying source outside manifest | Narrowed attribution to what the local Incremental Self-Improvement review describes. |
| SP-1 | grounded | quotes added | Retained the 5–12-point range and exact Claude Sonnet comparison. |
| SP-2 | narrowed | quotes added | Removed the unsupported no-degradation clause and bounded the chain-of-thought effect to some tested conditions. |
| SP-3 | retained local delta | quotes added for the ordering result | Retained the prompt connection explicitly as analogy and local transfer, not source identification. |
| VS-1 | grounded | snapshot required | Marked the PAT link for decomposition, specialized agents, grounding, deduplication, and synthesis. |
| VS-2 | grounded | snapshot required | Used the marked PAT route for the filtered SPOT construction and technical-error scope. |
| VS-3 | grounded | snapshot required | Added a marked PAT experiment link for the repeated-call recall/precision tradeoff. |
| VS-4 | grounded | snapshot required | Marked the Beyond Not Novel Enough link for the full novelty-review pipeline and evaluation split. |
| VS-5 | grounded | quotes added | Retained the Agentic Code Reasoning process-template use with an ordinary ingest link. |

Disposition totals: 44 `grounded`, 7 `literature handoff`, 5 `retained local
delta`, 2 `narrowed`, and 1 `contradicted/repaired`. Route totals across the 59
uses: 1 `quotes sufficient`, 30 `quotes added`, 21 `snapshot required`, and 7
outside-manifest literature handoffs.

### Operational semantic review

The selected model partition was `codex`. Each isolated worker was launched as
the concrete harness model `gpt-5.4`; finalization recorded that model and the
worker runner, with no invented effort value.

| Job | Scope | Runner | Initial result |
|---|---|---|---|
| 8052 | `verifiable-subroles-before-reviewer-identity` | `review_8052` | PASS. |
| 8053 | Five targets from proposal selection through computational reallocation | `review_8053` | Four PASS; `an-omitted-loop-function-and-a-frozen-one-need-different-repairs` WARN. |
| 8054 | Epiplexity, Gödel machines, and structured prompts | `review_8054` | Three PASS. |
| 8055 | Requested rerun of the warned omitted/frozen note | `review_8055` | PASS after the target made its six row-level premises and cohort-wide negative inference explicit. |

All jobs finalized successfully with matching `gpt-5.4`/`codex` provenance.
There were no FAIL or ERROR results. The ordinary post-finalization selector
for all nine target/gate pairs under `codex` returned `"targets": []`.

### Validation and cleanup

- All nine changed targets validate cleanly.
- Twelve changed ingests validate cleanly. The changed epiplexity ingest passes
  with its two pre-existing missing-link warnings for
  `../notes/definitions/distillation.md`; quote resolution itself passes for all
  6 retained passages.
- `commonplace-validate kb/notes` passes cleanly across 359 files.
- `commonplace-validate kb/sources` passes across 307 files with no failures;
  it reports pre-existing warnings in 20 source artifacts, including the two
  epiplexity warnings above.
- `git diff --check` passes. The operational-leftover scan across this record
  and every changed note and ingest finds no retired-workflow residue.
- Recovery commits `0e5df2c7eba7f6ae111119125607ad3870d92e7b` and
  `95561752b9c859de25f61baf8e222f2c40b9d637` remain readable commit objects.

## Identity and accumulation observation

The seven recovery ingests had no incumbent exact pairs. Six atomic requests
appended 51 distinct exact pairs. The Huxley request appended none: its first
two pairs matched but the atomic request failed because the third recovered
extract collapsed the snapshot bytes `SWE-Verified-\n60` into
`SWE-Verified-60`. That is a byte-identity failure, not a semantic dispute.

Similar passages remain side by side where they preserve different local
context, especially in the DGM and HyperAgents quote pools. No accepted pair
needed an identifier, reconciliation, or semantic deduplication. The mixed
quote/snapshot cases instead exposed route-association pressure: a bounded
positive mechanism was quote-judgeable while a protocol-wide absence claim
needed the snapshot. Placing marked links at those target uses resolved the
ambiguity without changing quote identity.

The rejected Beyond Not Novel Enough and PAT append attempts were also exact
text-boundary failures, not disputes about source meaning; both ingests were
restored unchanged and routed to their verified snapshots. The epiplexity
repair exposed target-scope pressure rather than quote-pool pressure: the
retained passages support the framework, but the note's worked examples are
local extrapolations and are now labeled that way.
