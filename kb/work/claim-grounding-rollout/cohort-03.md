# Cleanup cohort 03 — frozen 2026-08-24

Frozen at repository `15f4080f`. Follow [the procedure](./procedure.md)
and its **Executing a cohort** section, which carries the literal grounding and
re-ingest routes and explains why the claim inventory must precede source reading.

**Disjointness.** This cohort's notes and ingests are disjoint from every other
cohort's, on both axes — no two agents append to the same `Claims` section or
edit the same note. Cohorts 02–07 may therefore run fully in parallel.

Snapshot volume: 0.13 MB across 2 ingests.

## Targets

| Target | Blob | Ingests |
|---|---|---|
| `automating-kb-learning-is-an-open-problem` | `f559cd84` | `knowledge-centric-self-improvement-2607.19592` |
| `criteria-edits-invalidate-verdicts-process-edits-invalidate-artifacts` | `b5b8d2b2` | `build-systems-a-la-carte` |
| `first-principles-analysis-maps-design-space-before-selection` | `4d105602` | `build-systems-a-la-carte` |
| `moving-the-interpretation-enforcement-boundary-requires-coverage` | `398209d3` | `knowledge-centric-self-improvement-2607.19592` |
| `topology-isolation-and-verification-form-a-causal-chain-for-reliable` | `7917a770` | `knowledge-centric-self-improvement-2607.19592` |

## Your first task

Inventory each target's load-bearing claims **from the note itself, before
reading any source**, as a table of `ID | target | claim as frozen | source-side
need`. [Cohort 01](./cohort-01.md) is the shape. Then ground, disposition,
repair, and record — one row per claim use, not per note.

## Pre-source claim inventory

Recorded from the five frozen blobs above before either listed ingest or its
snapshot was opened. Footer descriptions that repeat a body claim travel with
that claim's row rather than counting as a second use.

| ID | Target | Claim as frozen | Source-side need |
|---|---|---|---|
| AK-1 | `automating-kb-learning-is-an-open-problem` | “Knowledge-Centric Self-Improvement runs a fully automated version of several cauldron mutations — extraction into evidence-grounded claims, cross-claim criticism, synthesis and retirement through distillation.” | Does the source describe an automated protocol that extracts evidence-grounded claims, criticizes claims across attempts or tasks, synthesizes retained knowledge, and retires material through distillation? |
| AK-2 | `automating-kb-learning-is-an-open-problem` | “A task-level forum converts attempts into local claims, a cross-task forum tests which claims recur beyond their originating task, and distillation retains typed, scoped guidance … that later agents consume.” | Does the source specify this three-stage task-forum → cross-task-forum → distillation protocol and the stated roles of each stage? |
| AK-3 | `automating-kb-learning-is-an-open-problem` | Distillation retains “transferable insights, confirmed constraints, rejected hypotheses, pitfalls, checks, next steps.” | Does the distilled artifact use these categories, and are they all retained output types rather than target-side interpretation? |
| AK-4 | `automating-kb-learning-is-an-open-problem` | “Its frozen distilled artifact improves performance on unseen tasks across LLM families.” | Does evaluation freeze the distilled artifact, test unseen tasks, cover more than one LLM family, and report improvement? |
| AK-5 | `automating-kb-learning-is-an-open-problem` | “Claims are grounded in benchmark pass/fail evidence.” | Does the protocol ground its candidate claims in task executions with mechanically observed benchmark success or failure? |
| AK-6 | `automating-kb-learning-is-an-open-problem` | “Claim survival is adjudicated by LLM forum debate.” | Does an LLM-mediated forum decide which claims survive, rather than merely generating or restating them? |
| AK-7 | `automating-kb-learning-is-an-open-problem` | “The artifact's end value is measured mechanically as held-out solve rate.” | Is the final retained knowledge evaluated by a mechanically scored solve-rate measure on held-out tasks? |
| AK-8 | `automating-kb-learning-is-an-open-problem` | The source “does not touch … curation for open-ended question-answering, where no solve-rate oracle exists”; it shows “the loop's mechanism is buildable where the oracle is given.” | Is the demonstrated system bounded to tasks with externally supplied evaluators rather than open-ended question-answering, and within that bound does it instantiate the claimed automated loop? |
| CV-1 | `criteria-edits-invalidate-verdicts-process-edits-invalidate-artifacts` | “An accepted verdict is a cached judgment keyed on its inputs. In build-systems terms it is a verifying trace.” | Does the source define a verifying trace as retained evidence used to decide whether a prior result remains valid from its inputs? |
| CV-2 | `criteria-edits-invalidate-verdicts-process-edits-invalidate-artifacts` | A verifying trace “store[s] hashes of the inputs, [then] compare[s] later to decide freshness.” | Does the source's verifying-trace model specifically store hashes of dependencies and later compare them to decide whether rebuilding is necessary? |
| CV-3 | `criteria-edits-invalidate-verdicts-process-edits-invalidate-artifacts` | “A key too coarse … makes every process wording tweak spuriously stale … [while] a key too fine … leaves verdicts falsely fresh when the real contract changes.” | Does the build-system account support both failure directions: recording irrelevant dependencies causes unnecessary rebuilds, while omitting real dependencies misses required rebuilds? |
| CV-4 | `criteria-edits-invalidate-verdicts-process-edits-invalidate-artifacts` | “The key must contain exactly the criteria: nothing more, nothing less”; verifying traces and rebuilder design are “the formal home of verdict invalidation.” | Does the source warrant the exact-dependency principle and distinguish trace freshness from the policy that decides how to rebuild, so the criteria/process mapping can be stated as a target-side transfer? |
| FP-1 | `first-principles-analysis-maps-design-space-before-selection` | “The scheduler-and-rebuilder grid in Build Systems à la Carte demonstrates the method: separating two choices …” | Does the source independently factor build-system design into scheduler and rebuilder choices and cross them as a design grid? |
| FP-2 | `first-principles-analysis-maps-design-space-before-selection` | Separating those choices “exposes both occupied implementations and empty but buildable regions.” | Does the source place known systems in some grid cells and identify previously unoccupied combinations that it constructs or argues are buildable? |
| MB-1 | `moving-the-interpretation-enforcement-boundary-requires-coverage` | Knowledge-Centric Self-Improvement's “retained improvements stay in natural-language.” | Are the protocol's retained, later-consumed improvements textual knowledge rather than changes to code, schemas, or model weights? |
| MB-2 | `moving-the-interpretation-enforcement-boundary-requires-coverage` | “Fixed external benchmark verification supplies an adequate symbolic check.” | Does a fixed external benchmark or deterministic evaluator verify attempts and final performance while remaining separate from the retained textual knowledge? |
| MB-3 | `moving-the-interpretation-enforcement-boundary-requires-coverage` | The system is “a boundary-stable comparison” demonstrating “that improvement need not cross forms.” | Across the demonstrated improvement loop, does behavioral responsibility remain with the same natural-language artifact form while external verification supplies evidence rather than taking over that responsibility? |
| MB-4 | `moving-the-interpretation-enforcement-boundary-requires-coverage` | The system “is not evidence for where boundary movement would occur.” | Does the source omit any demonstrated transfer of behavioral responsibility between model-interpreted text and formal enforcement, making it only a negative-scope comparison for boundary movement? |
| TV-1 | `topology-isolation-and-verification-form-a-causal-chain-for-reliable` | Knowledge-Centric Self-Improvement has “all three mechanisms instantiated in the knowledge-curation dimension, with measured gains.” | Does the source instantiate a multi-level topology, isolation between acting agents, and verification, and measure an improvement attributable to the resulting protocol? |
| TV-2 | `topology-isolation-and-verification-form-a-causal-chain-for-reliable` | “Stateless disposable agents give isolation by construction.” | Does the protocol describe agents as stateless or disposable between bounded calls such that one agent's conversational state is not inherited by the next? |
| TV-3 | `topology-isolation-and-verification-form-a-causal-chain-for-reliable` | “The task-forum → cross-task-forum → distillation ladder is the topology.” | Does the source implement these stages in that dependency order, with outputs of lower stages feeding higher-stage consolidation? |
| TV-4 | `topology-isolation-and-verification-form-a-causal-chain-for-reliable` | “Peer challenge plus benchmark oracles supply verification.” | Are claims challenged or adjudicated by peer/forum agents and also checked against benchmark outcomes or deterministic evaluators? |
| TV-5 | `topology-isolation-and-verification-form-a-causal-chain-for-reliable` | The source's “motivating critique of persistent-agent improvement” is that “lessons dilute and conflict as one agent absorbs them.” | Does the source explicitly identify dilution and conflict of accumulated lessons in a persistent/self-updating agent as a motivating failure? |
| TV-6 | `topology-isolation-and-verification-form-a-causal-chain-for-reliable` | “The protocol shares mutable state across its isolated agents (the knowledge base).” | Is there one evolving knowledge artifact or store that multiple otherwise isolated agent calls read and update during the protocol? |
| TV-7 | `topology-isolation-and-verification-form-a-causal-chain-for-reliable` | “Every write passes through challenge and distillation before later agents consume it — shared state gated by verification.” | Must every item that becomes consumable retained knowledge survive both challenge and distillation, or can later agents consume intermediate or unverified writes? |

## Completion record

Both ingests and all five repaired targets pass `commonplace-validate`. Source
review ran in requested mode under the `codex` partition. Job 8003 passed the
two Build Systems pairs. Job 8002 passed the automation note and warned on two
compressed target-side inferences; after those were labelled as local analysis,
job 8004 passed both rerun KSI pairs. The final selector returned `targets: []`.

| ID | Disposition | Target change | Validation |
|---|---|---|---|
| AK-1 | narrowed | Replaced the claimed extraction/criticism/synthesis/**retirement** bundle with extraction, criticism, synthesis, and selection; stated that the source does not establish retirement of previously retained knowledge. | PASS — target + source/codex job 8002 |
| AK-2 | grounded | Recast the passage in the grounded task-forum → cross-task-forum → LLM-distillation wording. | PASS — target + source/codex job 8002 |
| AK-3 | grounded | Retained the six bundle fields exactly and attached them to the scoped distillation claim. | PASS — target + source/codex job 8002 |
| AK-4 | narrowed | Bounded transfer to selected 20-task Polyglot and ARC-AGI-1 splits, GPT/Haiku pairs, a task-conditioned adapter, and the Polyglot same-exercise limitation. | PASS — target + source/codex job 8002 |
| AK-5 | narrowed | Limited mechanical grounding to benchmark attempt outcomes and aggregate solve rates; natural-language generalizations remain LLM-judged. | PASS — target + source/codex job 8002 |
| AK-6 | narrowed | Replaced forum-only adjudication with evidence-citing forum discussion followed by LLM distillation. | PASS — target + source/codex job 8002 |
| AK-7 | narrowed | Kept held-out solve rate but bounded it to the two transfer benchmarks and adapter-mediated consumption. | PASS — target + source/codex job 8002 |
| AK-8 | retained local delta | Made the source boundary explicit, then retained the open-ended-question-answering comparison as this note's inference rather than a source result. | PASS — target + source/codex job 8002 |
| CV-1 | narrowed | Replaced “a verdict is a verifying trace” as attribution with a bounded build-system analogy. | PASS — target + source/codex job 8003 |
| CV-2 | narrowed | Replaced generic input-hash wording with the source's exact Shake mechanism: prior dependency graph plus file-content hashes and rebuild on recorded dependency change. | PASS — target + source/codex job 8003 |
| CV-3 | retained local delta | Kept the coarse/fine review-key failure modes but labelled them as the Commonplace application, not a source claim. | PASS — target + source/codex job 8003 |
| CV-4 | narrowed | Corrected “exactly the criteria” to the evaluated artifact plus all criteria-bearing inputs, excluding production process; marked the criteria/process boundary and regeneration conclusion as local transfer. | PASS — target + source/codex job 8003 |
| FP-1 | grounded | Named task ordering and rebuild decision as the source's orthogonal scheduler/rebuilder choices. | PASS — target + source/codex job 8003 |
| FP-2 | narrowed | Replaced unqualified “buildable” with four formally workable combinations in the executable model and identified Cloud Shake as a later-implementation blueprint. | PASS — target + source/codex job 8003 |
| MB-1 | narrowed | Limited the natural-language claim to evolving behavior-changing guidance in fixed typed bundles; explicitly classified the complete shared store as mixed-form on the note's own analysis. | PASS — target + source/codex job 8004 after job 8002 WARN |
| MB-2 | narrowed | Limited symbolic verification to task and artifact outcomes rather than every retained claim. | PASS — target + source/codex job 8004 after job 8002 WARN |
| MB-3 | retained local delta | Kept boundary stability as the note's representational-form analysis of the grounded fixed-agent/fixed-evaluator design. | PASS — target + source/codex job 8004 after job 8002 WARN |
| MB-4 | retained local delta | Reframed the case as evidence for improvement without observed boundary movement, not evidence for where movement would occur under weaker oracles. | PASS — target + source/codex job 8004 after job 8002 WARN |
| TV-1 | narrowed | Changed causal-sounding support to coexistence of the three mechanisms with measured gains; explicitly made the no-component-isolation judgment target-side. | PASS — target + source/codex job 8004 after job 8002 WARN |
| TV-2 | narrowed | Scoped stateless-agent isolation to fresh private conversational state, not shared-data isolation. | PASS — target + source/codex job 8004 after job 8002 WARN |
| TV-3 | grounded | Retained the task-forum → cross-task-forum → distillation ladder as the protocol topology. | PASS — target + source/codex job 8004 after job 8002 WARN |
| TV-4 | narrowed | Separated peer challenge of natural-language claims from benchmark evaluation of task and artifact outcomes. | PASS — target + source/codex job 8004 after job 8002 WARN |
| TV-5 | narrowed | Kept dilution by conflicting updates as the paper's motivation, while stating that the experiment does not isolate that failure mechanism. | PASS — target + source/codex job 8004 after job 8002 WARN |
| TV-6 | grounded | Retained the shared mutable knowledge base while distinguishing it from private agent context. | PASS — target + source/codex job 8004 after job 8002 WARN |
| TV-7 | **contradicted / repaired** | Deleted the every-write verification gate. Forum agents read earlier posts and task agents receive attempt tables alongside distilled bundles; only reusable guidance is described as distillation-gated. | PASS — target + source/codex job 8004 after job 8002 WARN |

## Source mutation and identity record

- No source was unavailable, no snapshot required re-ingest, and no literature
  handoff was needed. Both name-paired snapshots matched their tracked SHA-256
  values and canonical source URLs.
- Three bounded Claims entries were appended to `build-systems-a-la-carte`:
  Shake's verifying-trace mechanism, the orthogonal scheduler/rebuilder grid,
  and self-tracking task-description changes.
- Six bounded Claims entries were appended to
  `knowledge-centric-self-improvement-2607.19592`: fresh-agent/shared-store
  architecture, the three-stage curation protocol, intermediate shared-state
  reads, symbolic benchmark evaluation, held-out transfer, and the
  persistent-agent motivation.
- Those nine entries served 25 target uses. Whole-section selection remained
  unambiguous. No duplicate entry, merge question, disputed identity, or need
  for claim IDs appeared. The two initial review warnings concerned how target
  inferences were labelled, not which Claims entry applied.

Disposition distribution: **5 grounded, 15 narrowed, 4 retained local deltas,
1 contradicted-and-repaired, 0 false positives, 0 unavailable, 0 literature
handoffs**.
