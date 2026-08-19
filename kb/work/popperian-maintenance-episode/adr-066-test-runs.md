# ADR 066 test runs: first passes under the modality machinery

Six full passes, chosen from [statistical-mode-candidates.md](./statistical-mode-candidates.md) so that together they exercise every path ADR 066 added: both reframe directions, both new mode targets, both landing guards, the premise gate's counterexample-shape annotations, and one control where the machinery must not fire. Run sequentially (the pass's concurrency precondition; also each run's readout may adjust expectations for the next). Independent runner preferred, per the 2a6408 precedent. Route each report's readout back into this file.

## Protocol per run

Ordinary `run-full-improvement-pass-on-note.md` invocation — the point is that the standard pass now does this work; no special harness. Record per run: (a) did the premise report carry shape annotations, and were they accurate; (b) did step 7 name a target mode where warranted, routed by those shapes; (c) did the landing meet its guard (stated refuter / adequacy record present before step 9); (d) did the closing premise rerun attack any new adequacy record; (e) were reframe follow-ups (rename, citer reconciliation) recorded as Open items.

## The runs

**Run 1 — statistical reframe down, easiest case. COMPLETED 2026-08-19 (pass `20260819T125030Z-s5qz`) — prediction wrong, machinery coherent.**
`kb/notes/task-fitted-structure-costs-cross-task-reuse.md` → renamed `current-task-fit-alone-does-not-warrant-costly-entrenchment.md`
The predicted statistical landing did not happen, and rightly so. The premise gate's shape annotations fired (`instance` on both non-HOLDS premises — a cheap-additive index defeating the exhaustive-warrants premise GLOBAL, a scope-determination edge case LOCAL); with no prevalence- or priced-exception-shaped defeats, no mode conversion was routed, and the pass instead found the warranted claim in the note's warrant structure: a *universal insufficiency* claim ("current-task fit alone does not warrant costly structural entrenchment"), retitled by ordinary keep-reframe. The survey had misread the body hedge ("often invisible, rarely revisited") as the core claim; the pass located the core elsewhere, and the hedge survives as a description of the bet's visibility, not as the thesis. Readouts: (a) shapes present and accurate; (b) no target mode named — consistent with the routing, since the shapes gave no mode signal; (c)/(d) mode guards unexercised this run; (e) follow-ups recorded and executed (relocated with redirect, four citers reconciled — including the coordination-value definition, whose gloss had become false the moment the reframe made coordination the rule's third warrant). Bonus behavior worth keeping: the closing premise rerun surfaced a *new* GLOBAL defeat (a temporary deadline with present stakes is a fourth warrant the packet's exhaustive formulation omitted), and the pass correctly routed it without another edit round — the reframed insufficiency title survives it because "alone does not warrant" is not an exhaustiveness claim.
Series consequence: run 1 turned into an unplanned second no-false-fire datum — the machinery declined a mode conversion on a note we expected to convert. Statistical-guard coverage now rests entirely on runs 3 and 5; if run 3 also lands off-mode, promote `structure-activates-higher-quality-training-distributions.md` (numeric prevalence core, survived null already in the body) into the series immediately.

**Run 2 — ideal-type conversion.**
`kb/notes/agent-runtimes-decompose-into-scheduler-context-engine-and-execution.md`
The hedge "in many real systems the boundaries blur; the claim is that the functions are analytically distinct" is an undeclared first-order model. Expected: keep (title may stand) with a body edit converting the hedge into a declared idealization plus adequacy record — declared use (what the decomposition is for: predicting which limitation a change fixes), omitted mechanism (implementation blurring), bound, dominance — and the closing premise rerun attacking that record in the same pass. Failure tells: conversion without the record (immunization guard missed), or the record present but the closing premises never engaging it.

**Run 3 — upward reframe from vacuity, the hard test.**
`kb/notes/the-framework-is-often-larger-than-the-durable-contribution.md`
"Often" in the title, "tends to" in the body, no refuter anywhere — the purest Class B case. Expected: reframe that lands on a *guarded* claim — a statistical form stating what measured framework-to-contribution ratio would refute it, or a stronger conditional the material warrants. This run tests whether the machinery repairs the ratchet's end state rather than reproducing it. Failure tell: the pass keeps or produces another unguarded tendency.

**Run 4 — upward reframe to universal.**
`kb/notes/memory-backed-personalization-can-look-like-model-improvement.md`
A bare possibility title with a sharp universal core buried in paragraph two ("it cannot make one of several prompt-compatible commissions authoritative without user-specific evidence"). Expected: keep-reframe *up*, promoting the refutable core to the title. This is the direct test of bidirectionality — before ADR 066 no repair path could strengthen a claim.

**Run 5 — mixed modality in one note.**
`kb/notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md`
The anchor case: a statistical binding claim (title says "not hard token limits"; its own description already retreats to "not just") over an ideal-type mechanism model (the three-dimension decomposition plus workspace hypothesis, self-described as "not fully separable" and "a working hypothesis"). Expected: the pass assigns different modes to different claims — statistical retitle with a stated refuter for the binding claim, declared idealization with an adequacy record for the mechanism section — without flattening one into the other. The hardest coordination test; a defensible lesser outcome (fixing one mode and routing the other to Open items) is a finding, not a failure.

**Run 6 — control: a sound universal the machinery must leave alone.**
`kb/notes/an-outcome-check-licenses-replay-a-rule-needs-the-process-verified.md`
Deductively argued ("a rule asserts 'do X because Y'; an outcome check never inspected Y"), correctly universal, not in the candidate survey. Expected: no modality finding — shape annotations may appear on any dented premise, but no mode reframe fires. Failure tell: the pass invents a statistical or ideal-type reading for a claim whose warrant is deductive. A machinery that fires everywhere is as broken as one that never fires.

## Second wave (queue, not scheduled)

After readouts from the six: `structure-activates-higher-quality-training-distributions.md` and `knowledge-storage-does-not-imply-contextual-activation.md` (statistical with numeric prevalence refuters), `entropy-management-must-scale-with-generation-throughput.md` (deontic universal), `weakly-discriminated-qualities-tend-to-be-underselected.md` (well-behaved Class B with named conditions), `codified-scheduling-patterns-can-turn-tools-into-hidden-schedulers.md` (upward to universal), `files-not-database.md` (statistical vs ideal-type boundary decision), `bounded-context-orchestration-model.md` (the clean-model cluster — last, because reframing the hub note has the widest citer blast radius).

## Series success criteria

The machinery validates when, across runs 1–5, every landed reframe names its target mode and meets its guard, at least one adequacy record is attacked by a closing premise rerun, at least one upward reframe fires, and run 6 produces no modality finding. Any guard that binds only because the runner happened to be careful — rather than because the instruction text forced it — is an instruction defect to fix before the second wave.
