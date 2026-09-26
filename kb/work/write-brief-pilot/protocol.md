# Write-brief pilot: protocol

**Status: DRAFT** — awaiting operator review. Changes are free until the commit that sets this line to `frozen`; after it, changes go to `deviations.md`.

The fixed parts below are fixed for comparability, not because the executor could not choose them: results must compare across arms, and a choice made after seeing outputs would let the data pick the hypothesis.

## Conjectures and refutation conditions

A *commission item* is one requirement a brief places on the target: a governing claim, an intended reader update, an exclusion, a passage to preserve because another artifact relies on it, a claim-mode or scope limit. An item is *recoverable* if a reader holding only the incumbent artifact and its backlinks would keep it without being told; otherwise it is *non-recoverable*. Recoverability is classified before any run (Phase 0).

**H1 — The value of a brief is concentrated in non-recoverable items.**
Prediction: across all pressure runs, the no-brief arm violates at least 3 more non-recoverable items than the original-brief arm, and the gap on recoverable items is smaller than the gap on non-recoverable items.
Refuted if the no-brief arm violates fewer than 2 more non-recoverable items than the original-brief arm, or the recoverable-item gap is at least as large. Refutation favors Options 1 or 2 of the proposal: the artifact, or the artifact plus its body, already carries what matters.

**H2 — A brief adds less where the title states the governing claim.**
Prediction: the per-target violation gap (no-brief minus original-brief, non-recoverable items, normalized by item count) is smaller on average for the four claim-titled notes than for the three non-claim documents.
Refuted if the average gap is equal or larger for the claim-titled notes. Weak test: see Limits.

**H3 — A brief written before drafting holds information that cannot be rebuilt from the finished artifact.**
Prediction: the rebuilt-brief arm violates at least 2 more non-recoverable items than the original-brief arm, summed over all pressure runs.
Refuted if the rebuilt-brief arm is within 1 violation of the original-brief arm. Refutation removes the proposal's argument for storing briefs independently: a brief could be generated on demand.

**H4 — A brief does not silently over-constrain.**
Prediction: in every override run with a brief, the writer either follows the request and states which commission item it amends, or asks the user, as `cp-skill-write` Step 4 requires.
Refuted if any brief-arm override run silently preserves the conflicting item against the request, or silently drops it without naming the amendment.

**Compliance guard.** A run that does not carry out its edit request scores as a failed run in every conjecture, not as preservation. Without this guard a brief arm could win by refusing to edit.

The thresholds are set for n = 7 targets with 2 replicates and are coarse by design. A result between the prediction and the refutation line is recorded as undecided, not rounded either way.

## Targets

| # | Target | Class | Source brief (commit) |
|---|---|---|---|
| 1 | `kb/notes/any-symbolic-program-with-llm-calls-is-a-select-call-program.md` | claim-titled note | `multistage-write-select-call-cordis-20260814` (`303e20b0`) |
| 2 | `kb/notes/context-operation-interface-bounds-context-policy.md` | claim-titled note | `multistage-write-context-operation-interface-20260827` (`d7615fea`) |
| 3 | `kb/notes/current-task-fit-alone-does-not-warrant-costly-entrenchment.md` | claim-titled note | `multistage-write-costly-entrenchment-options-20260828` (`16be19f9`) |
| 4 | `kb/notes/prototype-standing-is-revision-cost-binding-plus-lost-investment.md` | claim-titled note | `multistage-write-prototype-standing-revision-cost-20260827` (`db995fab`) |
| 5 | `kb/instructions/analyse-agentic-system/SKILL.md` | instruction | `multistage-write-analyse-agentic-system-20260820` (`303e20b0`) |
| 6 | `kb/instructions/analyse-external-system-epistemic-architecture.md` | instruction | `multistage-write-analyse-epistemic-architecture-20260820` (`303e20b0`) |
| 7 | `kb/work/epistemic-architectures/arc-skill-reading.md` | workshop reading | `multistage-write-arc-skill-reading-20260820` (`303e20b0`) |

Class is by whether the title states the governing claim, not by the `title-as-claim` trait (target 3 lacks the trait but has a claim title). Each brief path is `kb/work/multistage/<run>/brief.md` at the listed commit.

Every target has been edited since its brief was written, at least by the type-path sweep of 2026-09-25. The incumbent for each run is the target at the commit that freezes this protocol.

## Arms

- **A — no brief.** The writer receives the edit request and the incumbent, as in ordinary `cp-skill-write` use today.
- **B — original brief.** As A, plus the stripped original brief from `briefs/`.
- **C — rebuilt brief.** As A, plus a brief written by a fresh agent from the incumbent and its backlinks only, in the same format and length budget as B, and stripped by the same rule.

Arms B and C present the brief as a retained-intent block in the form `cp-skill-write` Step 4 accepts: source, subject, scope, and force (authoritative for intent). B and C carry identical labels, so the writer cannot tell an original brief from a rebuilt one.

Deferred, not part of this pilot: an arm with the brief's content moved into the artifact body (Option 2), and a replay of the fifth Popperian maintenance episode with the operator's sentence as a brief.

## Phase 0 — materials (before freeze)

1. **Strip the original briefs.** Remove items that bind only the original run: review findings to address, evidence and source lists, workshop mechanics, commit instructions, relocation steps already done. Keep the governing question, audience and reader update, target claim, must-keep and must-exclude items, scope, terminology, and reserved decisions. Write the result to `briefs/<n>.md`, recording each removed item and why in a trailing list. The operator reviews all seven before freeze.
2. **Extract commission items.** A fresh agent lists the commission items of each stripped brief in `rubric/<n>.md`, one line each, numbered.
3. **Classify recoverability.** A second fresh agent, given the incumbent and a list of its backlinks but not the brief, receives each item and answers: does the artifact state or clearly imply this, so a careful editor would keep it without being told? Mark recoverable or non-recoverable. The operator may spot-check but does not reclassify after freeze.
4. **Write the edit requests.** For each target, one **pressure** request that invites drift on at least two non-recoverable items without naming them (such as "cut this to 60% of its length", "generalize the claim", "fold in neighbor X", "rewrite for a newcomer"), and for targets 3, 4, and 5 one **override** request that legitimately conflicts with one named commission item. Requests are written from the rubric, before any run, and are identical across arms.
5. **Build the rebuilt briefs (arm C).** Done now, not during runs, so every run of a cell uses the same brief.

## Phase 1 — runs (after freeze)

- **Cells.** 7 targets × 3 arms × 2 replicates of the pressure request = 42 runs. Override runs: 3 targets × arms B and C × 1 = 6 runs. Total 48.
- **Worker.** A fresh sub-agent per run, on the session's Opus model (record the concrete model id), following `cp-skill-write` in edit mode with these deviations: it writes its candidate to `runs/<target>-<arm>-<replicate>/candidate.md`, never to the target path; it skips Step 7 source grounding and Step 9 validation, and adds no new source dependency; it does not invoke `cp-skill-connect` or ask the user a question it could not ask in a real run. If it would ask the user (Step 4 conflict), it writes the question to `question.md` and stops; that is a valid outcome and scores as *flagged*.
- **Order.** Randomize run order across cells; record the order.
- **Isolation.** Workers get no access to this workshop beyond their own run directory and input packet.

## Phase 2 — blind scoring

- For each run, strip arm identifiers and assign an opaque id. The mapping stays in `scores/key.md`, unread by scorers.
- A fresh scorer per target receives: the incumbent, the edit request, the numbered commission items (without the recoverable/non-recoverable label), and the candidate or `question.md`.
- It scores:
  - **compliance** with the edit request: done, partial, or not done;
  - each **commission item**: kept, violated, flagged (the writer named a conflict or asked), or amended-with-notice (override runs only: changed as requested, and the change is stated).
- Two scorers per target on different model families if available; otherwise two independent Opus scorers. Record disagreements. Resolve them by a third scorer, not by the operator.

## Analysis

Tally per arm, per class, and per item-recoverability, then read each conjecture against its frozen refutation line. Report every run in a table, including partial-compliance and failed runs. Record anything the conjectures did not predict under **Unpredicted** before interpreting it; that section is where the surprise the operator asked about will show up, if any.

## Limits (to state in the evidence note)

- Seven targets, two replicates: the pilot can refute the stronger predictions, but it cannot estimate effect sizes.
- The original briefs are careful, operator-written commissions made inside multistage runs. Ordinary briefs would likely be thinner.
- H2 is weak: only three non-claim targets, two of which are instructions, which already open with their intent under the directive-text rule. Instructions therefore partly test Option 2, not the claim-title effect alone.
- Writers, rebuilders, and scorers are all Claude models. Shared biases may inflate agreement.
- The pressure requests are written by someone who has seen the briefs. They are designed to test the items, which is the point of a severe test, but they do not measure how often ordinary edits threaten a commission.

---

- [Per-artifact write briefs](../../reference/proposals/per-artifact-write-briefs.md) — tests: Options 1–3 and the pre-draft independence force
- [cp-skill-write](../../instructions/cp-skill-write/SKILL.md) — depends-on: the writing procedure and its Step 4 retained-intent input used in every arm
- [Warranted reader update is the objective of substantive writing](../../notes/warranted-reader-update-is-the-objective-of-substantive-writing.md) — draws-on: the reader update as a commission item distinct from the title claim
