# Frontier scan — 2026-11-08

## Commission and outcome

The operator invoked [Scan the unresolved frontier and select straightforward next steps](./scan-and-select-frontier-work.md). The scan returned four recommendations in the conversation. The operator subsequently authorized saving the results here and requested a reassessment of the first recommendation: is it also a theory note carrying too much local-system detail?

This record preserves the initial assessment. That follow-up question is not silently incorporated into its original rationale. No discovered task was executed during the scan.

## Scan basis

- Time: 2026-11-08, 08:29:48–08:31:28 UTC.
- Objective: identify useful bounded work in this KB, not maximize recommendations.
- Coverage: recursive unresolved-heading discovery in `kb/theory/` and `kb/reference/`; substantive assessment of 12 candidate work packages across 13 source documents. Related questions were grouped.
- Comparison: prefer visible benefit, a known next action, narrow file scope and a meaningful check. No absolute scores.
- Limits: selective current-state scan, not a complete inventory. Ledgers, heading-free gaps and most theory questions were not assessed. Targeted reads elsewhere checked current procedures and workshop ownership; they did not supply new candidates.
- No files changed, workers launched, external sources acquired, or review/freshness state altered during the scan. This record was written afterwards under the operator's separate authorization.

## Initial shortlist

### 1. Reconcile the directory-placement note with adopted placement rules

Source: “Execution shaping determines directory placement” (historical source: `44ea70b86de2534f195d3b8d925f27e5109f2d1e:kb/theory/execution-shaping-determines-directory-placement.md`), opening example and Open Questions.

Evidence: the note describes `kb/instructions/WRITING.md` as sitting “at the top of the KB directory.” Later rules permit collection-owned instructions: [content routing](../../reference/content-routing.md), [ADR 084](../../reference/adr/084-kind-rules-live-in-type-specs-and-operations-in-instructions.md), and [ADR 099](../../reference/adr/099-agentic-analysis-method-and-reports-belong-to-the-collection.md).

- Benefit: remove a contradictory example and distinguish the transferable reading-mode argument from placement choices already made.
- Next action/file scope: revise the theory note only; check which open questions later rules answer and retain genuinely unanswered ones. No relocation or ADR rewrite.
- Ease: the inconsistency is visible and later placement rules provide a concrete comparison.
- Verification: check current-placement statements against collection contracts and decisions, inspect inbound references, and run relevant validation.
- Permission: separate note-edit commission.
- Stop: preserving its contribution requires a new placement policy or retirement decision.

### 2. Update instruction-testing examples to match the current connect protocol

Source: [unit testing LLM instructions requires mocking the tool boundary](../../theory/unit-testing-llm-instructions-requires-mocking-the-tool-boundary.md), Architecture and behavioral assertions.

Evidence: the note proposes “Attempted semantic search before falling back to grep” as correct behavior. The current [connect skill](../../instructions/cp-skill-connect/SKILL.md) instead requires repository-local discovery and says, “Do not call external semantic-search tools or MCP search services.”

- Benefit: avoid tests that enforce obsolete behavior while preserving the tool-boundary argument.
- Next action/file scope: revise the theory note's connect-specific tool inventory and assertions. Use current obligations such as contract reads, local discovery and report-only writes. Do not build a runtime.
- Ease: direct mismatch with an executable procedure, not an unresolved testing architecture choice.
- Verification: map each connect assertion to the skill; distinguish deterministic trace checks from semantic judgments; validate the note.
- Permission: separate note-edit commission.
- Stop: examples are intentionally historical, or correction requires changing the skill.

### 3. Test the unresolved thin-draft case for claim reconstruction

Source: “Descriptive link labels may supply claim self-sufficiency” (historical source: `89dd98770eec00359da3a3aee6a8866ea51c0658:kb/theory/descriptive-link-labels-may-supply-claim-self-sufficiency.md`), Open questions.

Evidence: the retained ablation found mature bodies sufficient without labels; a genuinely thin pre-connect draft remains untested. The [writing-as-thinking workshop](../writing-as-thinking-process-transfer/README.md) carries the test as open.

- Benefit: distinguish whether labels repair missing premises or body enrichment does the work; inform whether another review check adds signal.
- Next action/file scope: coordinate with that workshop, identify one authentic thin draft with provenance, compare the unchanged body with and without informative labels, and add a separate body-enriched condition if needed. Retain protocol, exact inputs and cold-reader results in an authorized workshop record.
- Ease: missing case and variable already identified; a one-draft discriminator need not estimate corpus-wide rates.
- Verification: genuine pre-connect provenance; fixed bodies in label comparisons; no target reads; retain reconstructions and missing-premise findings, not just PASS labels.
- Permission: workshop experiment authority, output location and fresh-worker/model-call authorization; no gate adoption.
- Stop: no authentic draft, unrecoverable reconstruction criterion, or inseparable body and label changes.

### 4. Try the lightweight vocabulary collision screen before a registry

Sources: [write-time vocabulary collision controls](../../reference/proposals/write-time-vocabulary-collision-controls.md), option 3 and Risks; [vocabulary collision theory](../../theory/vocabulary-collisions-prevented-at-write-time-not-read-time.md).

Evidence: the proposal calls the screen “self-serve and nearly free”; registry adoption should wait for actual slot-escape or retirement violations. No explicit coinage-collision step was found in the inspected write-skill text.

- Benefit: test naming-time exact-string audits without persistent machinery.
- Next action/file scope: coordinate with [vocabulary governance](../vocabulary-governance/README.md). On the next real proposed technical term, screen exact-string occurrences and classify matches. Retain a small workshop report; no registry, command or mandatory gate.
- Ease: existing search and manual semantic inspection; no need to settle collection-local vocabulary policy first.
- Verification: retain proposed sense, scope, queries, classifications and whether the naming decision changed.
- Permission: workshop record and a real naming case; later skill changes require a separate commission.
- Stop: no real term, unresolved vocabulary-scope policy, or expansion into registry implementation.

Initial relative priority: 1–2 have the clearest correction and least uncertainty. Item 3 needs readers and a suitable draft. Item 4 should wait for a real naming occasion. Larger mock runtimes, vocabulary registry/lint/semantic enforcement and a label-quality gate were not selected.

## Other assessed packages

Not selected means neither resolved nor permanently infeasible.

| Package/source | Finding or blocker |
|---|---|
| [Backlink surfacing](../../reference/proposals/backlink-surfacing.md) | A recipe might be small, but the linking-contract workshop owns inbound delivery. A command still needs recurring need; rendering adds another consumer. Avoid parallel implementation. |
| [Keyword tags without heads](../../reference/proposals/keyword-tags-without-heads.md) | Explicitly set aside until recurring head-cost friction or a host request. Source-search amendment uses existing heads. No trigger established. |
| [Tag maintenance and derived browsing](../../reference/proposals/tag-maintenance-and-derived-browsing.md) | Original trial set aside because observed misses were vocabulary misses. Narrowed split-candidate use still needs a tag and operator task. |
| [Calibrating semantic gates](../../reference/proposals/calibrating-semantic-gates-against-labelled-fixtures.md) | Independent labels, non-leaking prompts and recorded judging configuration are substantive prerequisites. Inline-example recognition cannot substitute for detection evidence. |
| [Gate learning from accepted edits](../../reference/proposals/gate-learning-from-accepted-edits.md) | Mining does not settle attribution, promotion, rollback or loading policy. Calibration proposal is not an implemented lifecycle. |
| [Temporary amendments](../../reference/proposals/temporary-amendments-to-published-analyses.md) | Needs producer verification, guarded publication, display attachment and replacement/archive behavior; not a local Markdown fix. |
| [Stale self-description](../../theory/stale-self-description-conceals-its-own-staleness.md) | Useful decomposition, but no named mutable claim and change operation established. General solution exceeds a straightforward task. |
| [Cheap adoption and weak retirement](../../theory/cheap-adoption-and-weak-retirement-accumulate-cost.md) | Retirement execution is distinguished from its unresolved signal/decision path. Useful measures need concrete structural histories, not an invented universal trigger. |

## Evidence and versions

Tracked input revision: `89dd98770eec00359da3a3aee6a8866ea51c0658`. All 13 candidate source documents linked above were clean at that revision. Commit plus path identifies retrievable inputs; the quoted passages above retain the main selection and deferral evidence.

Additional material checks at that revision:

- `kb/reference/content-routing.md` and `navigation.md`.
- ADRs 084 and 099.
- `kb/instructions/cp-skill-write/SKILL.md` (targeted text inspection) and `cp-skill-connect/SKILL.md`.
- `kb/work/linking-contract-consistency/README.md`.
- `kb/work/vocabulary-governance/README.md` and `prose-has-no-scope.md`.
- `kb/work/writing-as-thinking-process-transfer/README.md`.
- `tests/connect/README.md`.

Scoped ADR, implementation and test searches were supersession checks, not proof of absence. Some batched output was truncated; recommendations used passages subsequently visible in full-file or targeted reads.

Uncommitted inputs are not attributed to HEAD. SHA-256 of inspected bytes:

| Input | State during scan | SHA-256 |
|---|---|---|
| `scan-and-select-frontier-work.md` in this directory | Untracked | `ce926843dfd1a7fb0382b8e51e2025ef96fc74264593e4f4f8fb307fa3c10310` |
| `README.md` in this directory | Untracked | `383940137ea2b03f5beb5eb0d0cb9d696d80e4933c5e537af88a92d2dd1e8e53` |
| `AGENTS.md` | Modified | `a8a884a485441fd55c01421ecce5fd378e069da1b2d3d97a615a5dfd5861ddd6` |

The instruction's operative boundary was: “Inspect local files read-only. Do not execute tasks, delegate, acquire external sources or alter review/freshness state.” Hashes detect changes; they do not substitute for retaining uncommitted files.

The workshop README describes an earlier single-task trial. Its recommendation was not reused or treated as a comparative assessment. No prior record was overwritten.

## Follow-up — operator's first-item reassessment

The operator asked whether item 1 is also a theory note carrying excessive local-system detail. Against the current [theory collection contract](../../theory/COLLECTION.md), yes: the problem is not merely stale paths.

The contract asks whether, after named system choices are scoped, a substantive design-space claim remains. Local examples may illustrate a theory, but records of selected layout belong in reference and in-flight migration questions belong in a workshop.

In this note:

- The opening prescribes literal Commonplace directories instead of first stating a transferable mechanism.
- The WRITING.md trigger and the claim that procedures are currently scattered describe a local layout and proposed migration.
- Evaluation mixes theoretical tests with checking a particular relocation and its CLAUDE.md routing.
- Retroactive application and whether to collapse the local skill/instruction boundary are adoption questions, not necessary parts of the general argument.

A plausible theoretical residue remains: grouping execution-oriented procedures by reading mode may make procedure maintenance easier and reduce routing ambiguity, provided that grouping does not obscure ownership or produce an excessively heterogeneous directory. That is a conjecture to formulate and test, not a conclusion established by the existing local example.

Revised recommendation: do not merely update local paths or add more current placement rules to the theory note. First separate the general grouping mechanism and its limits from Commonplace's placement policy and migration history. Compare the residue with existing notes before deciding whether to rewrite, merge or retire this artifact. No library change or disposition has yet been authorized or executed.
