# Intent-framed instruction machinery refinement

## Result

Commonplace now treats instruction precision as precision about purpose,
authority, interfaces, acceptance, and consequential failure handling. It no
longer treats precision as advance selection of every execution method or as
completion of one universal worker-packet checklist.

The operative rule is decision-specific: fix what the executor cannot safely
recover, codify choices whose inputs are stable, and leave a bounded choice to
an authorized executor when live or produced evidence can change it. Exact
commands, order, isolation, output grammar, and recovery remain fixed where a
machine interface, irreversible mutation, contamination risk, or coordination
dependency makes them part of correctness.

This is a Commonplace consequence derived from the retained planning theory.
It is not a claim made by military doctrine, and no instruction imports
*Auftragstaktik*, military hierarchy, adversarial purpose, or a military packet
format as an operative label.

## Baseline and theory delta

Commit `d8eb9d86` previously swept delegated-authoring surfaces and rebuilt the
multistage writer around three roles: isolated source reconstruction,
consolidated authorship, and digest-bound independent review. That sweep also
tightened warning-fix, full-pass, review-prompt, mailbox, revision, and memory-
review handoffs. It is the baseline for this pass rather than work to repeat.

The later source-grounding pass sharpened two boundaries:

1. Reciprocal adaptive opposition is the deep source-domain reason military
   planning is unusually hard to specify in advance. It transfers as a causal
   origin only to genuinely adversarial agent work.
2. Ordinary non-adversarial agent work can share only the downstream mechanism:
   a later observation or produced result can discriminate among permitted
   means. Control requirements follow the target's consequential failure
   surfaces, not a complete list copied from modern military doctrine.

The second boundary exposed two remaining machinery problems. The instruction
contract still presented a useful audit heuristic as a mandatory field list,
and the already-reduced multistage skill still prescribed worker organization
and repeated rare promotion machinery on its common path.

## Changes made

| Surface | Refinement | What remains fixed | What remains with execution |
|---|---|---|---|
| `kb/instructions/COLLECTION.md` and `kb/types/instruction.md` | Define precision around the decision boundary and select controls from actual failure consequences. | Goal, authority, stable interfaces, coupling, acceptance, and load-bearing protocol. | Harmless choices and means selected from authorized live evidence. |
| `kb/instructions/write-instruction.md` | Admit repeated practice, established methodology, or a fixed machine interface as evidence for codification; test cold execution. | Operative path, stable rules, consequential controls, deferral convergence. | Method where several permitted routes can satisfy the goal. |
| `cp-skill-write-multistage` | Reduce the common path to commission, source-first reconstruction, staged consolidated authorship, grounding, exact-byte review, one repair, and promotion. | One target, user-owned contribution changes, evidence partitions, sole outputs, exact grounding interface, accepted digest, live-target guard, rollback. | Reconstruction organization, disposition format, decomposition, examples, prose, and review analysis. |
| Multistage promotion | Move retitle, relocation recovery, validation rollback, lineage rollback, and cleanup into a conditional skill reference. | Every irreversible and recovery-sensitive step. | Nothing material; this branch is exact because mutation is costly to reverse. |
| Compression review | Replace role self-detection with one explicit parent dispatch and make captured note text the authoritative assessed bytes. | Criterion order, output grammar, no-mutation boundary, fresh independent judgment. | Criterion application and cross-finding synthesis. |
| Memory-system review | Change the trigger description from “optional sub-agent drafting” to “delegated drafting,” matching the actual workflow. | Existing anti-recursion, checkout, sole-write, and parent-QA controls. | Code reading, explanation, and review structure inside the artifact contract. |
| Theory notes | Add formal `Operationalized into:` edges from the delegation, determinability, and productive-deferral notes. | Lineage from theory to procedure. | No new claim of source-side authorship or agent effectiveness. |

The multistage entry file fell from 272 to 219 lines after the forward-test
clarifications. Its 94-line promotion reference is loaded only after acceptance.
Total package text did not shrink substantially; common-path context and
preselection of worker means did. That is the relevant simplification.

## Surfaces deliberately kept exact

- `cp-skill-ingest` and `draft-ingest-report` use clean context, exact snapshot
  identity, a sole output, a byte-preserved Quotes boundary, one replacement,
  and restore because contamination and partial mutation are concrete risks.
- `run-review-batches` dispatches an already-generated prompt. Job identity,
  model partition, sentinel grammar, provenance, transactionality, and
  single-use workers belong to the parser and freshness protocol.
- `analyse-agentic-system` centralizes evidence boundaries and canonical IDs to
  avoid cross-lens drift and parallel collisions while leaving lens depth and
  physical result layout open.
- The external-literature assessment uses bilateral isolation only when
  independence is explicitly at issue. Its extra roles are a conditional
  contamination control, not a default planning topology.
- The warning-fix sweep and tag follow-up already delegate only disjoint,
  authorized write sets with parent integration and a substantive-decision
  stop.
- Worker-side review criteria and drafting instructions are not additional
  delegation-authoring workflows. Their callers own the handoff.

## Deferred redesigns

- `cp-skill-revise-autoreason` is an experimental blind-comparison algorithm.
  Its roles, mappings, parseable returns, Borda aggregation, reruns, and stop
  rule should change only as a versioned protocol with isolation and failure-
  recovery tests.
- `run-full-improvement-pass-on-note` is primarily a persistent state machine,
  not a long worker prompt. Simplification must cover its report schema,
  captures, guards, re-entry, and rollback together. Its active coherence
  audit remains the owner.
- The memory-review worker brief repeats several lifecycle and anti-recursion
  controls. Removing them safely needs a checked reuse mechanism or a focused
  failure-path pass; this workshop changed only the false trigger description.
- The full-pass wrapper and compression dispatch still need one system-level
  decision about how a full-pass source capture remains identical to every
  report method's assessed capture under concurrent live-target drift. The
  compression packet itself now names one authoritative representation.

## Independent forward test

A fresh agent applied the revised multistage skill to an edit scenario with a
review block, candidate repair, newly added substantive grounding evidence, a
second acceptance, and live-target drift before promotion.

It correctly assigned commission, integration, mutation, and recovery to the
parent; source reconstruction to an incumbent-blind worker; candidate judgment
to the staged author; and acceptance to digest-bound independent reviewers. It
also reached the required terminal result: promotion is blocked when the live
target differs from `original.md` and no rebase authority exists.

The test found two ambiguities, both repaired in the skill:

- substantive new evidence after incumbent reveal now requires a fresh source-
  only reconstruction and a fresh author through both reveals;
- reconfirming identical candidate bytes does not spend another repair, but a
  further byte change does, and an exhausted-allowance rebase requires a new
  run.

This is a structural forward test, not evidence that the method improves LLM
writing outcomes.

## Consumed workshop evidence

The previously active multistage coherence audit is now closed. Its eight
findings are represented in the live skill: explicit authority for claim
replacement; guarded retitle and relocation; live-target drift detection;
brief provenance despite a non-fresh parent; stage-specific invalidation;
malformed or ambiguous run detection; independent review for every candidate;
and a closing account before workshop deletion. Its narrower observations
about near-duplicate rerouting, worker-bound decision returns, blocked-stage
exits, and grounding composition are covered by the same setup, authority,
invalidation, and sibling-interface rules. The independent forward test above
exercised the highest-risk combined path.

## Validation

- Every changed KB artifact passed `commonplace-validate` without warnings or
  failures.
- The promoted-skill scaffold test passed all 18 cases, including copying the
  new conditional reference.
- `git diff --check` passed.
- The generic Codex skill validator rejected Commonplace's pre-existing
  runtime frontmatter keys (`type`, `context`, `user-invocable`, and
  `argument-hint`). Those live Commonplace fields were preserved; the mismatch
  is a validator-compatibility boundary, not a defect introduced by this pass.
