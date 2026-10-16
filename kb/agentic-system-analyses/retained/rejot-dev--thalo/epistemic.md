---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Thalo epistemic routes: structural checking, synthesis candidates, admission, retention and later reliance."
run-id: AAS-2026-10-14-thalo-86fcc3efe983-01
reviewed-boundary: "cdb9aae983e6bc0b75eff1606bc99b088c3aebff"
---

# Thalo epistemic report

## Source-and-claim boundary

The question is whether Thalo merely organizes supplied knowledge or also produces, checks, accepts and integrates truth-apt claims. Scope and exclusions are see [boundary](boundary.md#boundary-and-evidence); evidence identities and layers are see [Source register](boundary.md#source-register). SRC-1 supplies implementation and doctrine/design, not observed operation or causal experiments. The included shipped Pi/action path matters even though the CLI alone stops at context preparation. External providers, host internals and actual human PR decisions remain excluded; those exclusions prevent judgments about provider reasoning, deployed enforcement and exercised human acceptance.

Truth-apt objects can occur in entry bodies and synthesis prose. Their initial truth and authorship are unknown. Titles such as `lore` do not supply warrant. Queries, checkpoints and schemas have operational authority without asserting the truth of those bodies. The source claims structural feedback and synthesized understanding: see [RT-CLM-agent-feedback](runtime.md#rt-clm-agent-feedback), [EPI-CLM-synthesized-understanding](#epi-clm-synthesized-understanding), and the narrow-edit request [EPI-CLM-preserve-content](#epi-clm-preserve-content).

### Coverage

Direct reads below are additional source inspection at SRC-1's frozen revision. Supplied findings are identified separately; neither establishes activation. CLI registration was read directly, including `rules`, which runtime did not name explicitly. It only lists rule metadata and is not a further evaluator.

| Entry point or operation | Source path | Coverage and records; limit |
| --- | --- | --- |
| CLI dispatch and rule listing | `apps/thalo-cli/src/mod.ts`; `apps/thalo-cli/src/commands/rules.ts` | Direct complete reads; nine registered commands accounted for here and below. Rule listing is descriptive output, not claim admission. |
| Check, watch, LSP diagnostics | `packages/thalo/src/checker/rules/rules.ts`; `packages/thalo/src/checker/rules/invalid-field-type.ts`; `packages/thalo/src/checker/rules/unresolved-link.ts`; `packages/thalo/src/checker/rules/actualize-missing-updated.ts` | Direct rule registry and selected visitors; supplied dispatch/exit/LSP findings: [RT-RTE-check-feedback](runtime.md#rt-rte-check-feedback). Individual uninspected visitors and type matcher internals prevent exhaustive diagnostic-correctness conclusions. |
| Query | `packages/thalo/src/commands/query.ts` | Direct complete read; [EPI-RTE-query-selection](#epi-rte-query-selection). Query service internals uninspected here; no claim of exhaustive predicate correctness. |
| Actualize, CLI force, browser fallback, tracker recovery | `packages/thalo/src/commands/actualize.ts`; `packages/thalo/src/services/change-tracker/git-tracker.ts`; `packages/thalo/src/services/change-tracker/timestamp-tracker.ts`; `apps/docs/app/components/playground/thalo-runner.ts` | Supplied [RT-RTE-actualize-selection](runtime.md#rt-rte-actualize-selection); alternate routes prevent treating up-to-date as semantic correctness or complete invalidation. |
| Pi generation, output guard, writeback | `packages/scripts/src/synthesize-with-pi.mjs` | Direct complete read; [RT-RTE-pi-synthesis](runtime.md#rt-rte-pi-synthesis), [EPI-RTE-output-guard](#epi-rte-output-guard), [EPI-RTE-file-reconstruction](#epi-rte-file-reconstruction), [EPI-RTE-prose-retention](#epi-rte-prose-retention). No tools or hooks registered by this script; opaque imported Agent behavior is not inspected. |
| Action subprocess, failure and publication | `packages/thalo-action/src/action.ts` | Direct complete read; [RT-RTE-action-publication](runtime.md#rt-rte-action-publication). Arbitrary replacement command implementation is outside the frozen target. |
| Init, format and direct edits | `apps/thalo-cli/src/commands/init.ts`; `apps/thalo-cli/src/commands/format.ts`; `skills/thalo/SKILL.md` | Supplied [RT-RTE-local-authoring](runtime.md#rt-rte-local-authoring); direct complete skill read. Formatter semantic fidelity and external author decisions unassessed, preventing a system-complete negative about every possible production/check route. |
| Merge driver, conflict check, deletion/rejection | `apps/thalo-cli/src/commands/merge-driver.ts`; `packages/thalo/src/merge/driver.ts`; `packages/thalo/src/merge/conflict-detector.ts`; `packages/thalo/src/merge/entry-merger.ts`; `packages/thalo/src/merge/merge-result-builder.ts` | Direct complete reads; [EPI-RTE-merge-check](#epi-rte-merge-check), [EPI-RTE-merge-disposition](#epi-rte-merge-disposition). Entry matching and serializer internals uninspected; no universal lossless-merge guarantee. |
| Merge setup and editor formatter | `apps/thalo-cli/src/commands/setup-merge-driver.ts`; `packages/thalo-vscode/src/mod.ts` | Supplied boundary/runtime coverage for editor; scoped text search only here. Setup internals uninspected: installation enforcement cannot be judged. Neither is treated as an evidenced absence of semantic checking. |
| Shipped guidance and candidate fixtures | `README.md`; `skills/thalo/SKILL.md`; `thalo-test/syntheses.thalo`; `thalo-test/AGENTS.md` | Direct complete first three reads; supplied KB instruction findings. No provenance-linked generation/evaluation trace supplied; fixtures cannot prove routes operated. |

A bounded source search for tool/hook registration, acceptance, rejection, verification, truth, evidence and contradiction covered the Pi script, checker rules, merge code, skill, KB instructions, CLI dispatcher and editor integrations. The returned checks concern syntax, references, schema values and merge disagreements. This search and the direct route traces support the narrower conclusions below, not an exhaustive system-wide assertion that no semantic evaluator could ever be supplied. No model output trace is available to distinguish actual reshaping, entailed derivation or non-entailed conjecture. No acceptance record is available to establish evidence-consuming acceptance against a criterion for an intended epistemic use. No later outcome/comparison is available to establish learning or causal benefit.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
| --- | --- | --- | --- | --- |
| [EPI-OBJ-source-entries](#epi-obj-source-entries) | Entry assertions and attributions, where present | see record | SRC-1, `packages/scripts/src/synthesize-with-pi.mjs` | Imported content; initial source warrant unknown. |
| [EPI-OBJ-synthesis-prose](#epi-obj-synthesis-prose) | Possible summaries, factual assertions and explanations | see record | SRC-1, `packages/scripts/src/synthesize-with-pi.mjs` | Particular output propositions not determinable without a trace. |
| [RT-OBJ-command-input](runtime.md#rt-obj-command-input) | None in routing fields; body payload split above | see record | SRC-1, `packages/thalo-action/src/action.ts` | Structured provenance is not all forwarded separately to model. |
| [RT-OBJ-system-prompt](runtime.md#rt-obj-system-prompt) | None: behavioral guidance | see record | SRC-1, `packages/scripts/src/synthesize-with-pi.mjs` | Requests are not proof of compliant output. |
| [RT-BAP-synthesis-guidance](runtime.md#rt-bap-synthesis-guidance) | None required: retained query/prompt guidance | see record | SRC-1, `packages/scripts/src/synthesize-with-pi.mjs` | Natural-language force is advisory, not enforced. |
| [RT-OBJ-checkpoint](runtime.md#rt-obj-checkpoint) | None: selector state | see record | SRC-1, `packages/thalo/src/commands/actualize.ts` | Checkpoint records a cutoff, not verified incorporation. |
| [RT-RTE-check-feedback](runtime.md#rt-rte-check-feedback) | Diagnostic propositions about parsed structure | see record | SRC-1, `packages/thalo/src/checker/rules/unresolved-link.ts` | Domain is reference/schema/syntax conformance, not subject-matter truth. |
| [EPI-RTE-merge-check](#epi-rte-merge-check) | Diagnostic propositions about version disagreement | see record | SRC-1, `packages/thalo/src/merge/conflict-detector.ts` | No truth arbitration between competing entry assertions. |
| [RT-CMP-gpt5-mini](runtime.md#rt-cmp-gpt5-mini) | Distributed-parametric content is opaque | see record | SRC-1, `packages/scripts/src/synthesize-with-pi.mjs` | Weights, processing and exact immutable model identity unavailable; no parameter-update inference. |

## Authority-route ledger

Each row is a consequential function, not a claim that it operated. The record owns implementation details; `see` avoids duplicating its generic route fields. Every implemented row has unobserved activation and outcome. No lifecycle-integration row is warranted merely by a write or a PR.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [RT-RTE-local-authoring](runtime.md#rt-rte-local-authoring) | content transformation | implemented | [EPI-OBJ-source-entries](#epi-obj-source-entries) | truth-apt transformation: acquisition/import | Saved external assertions enter workspace | Filesystem/loader; no source-truth check established | On author save/reload; see record | Available entries | Local admission | Source warrant unknown; acquisition is not production | Makes saved content queryable | Workspace consumers / text load / permissive / later invocations | SRC-1, `apps/thalo-cli/src/commands/init.ts` | none | none | Actual author and authored derivation uninspected. |
| [RT-RTE-check-feedback](runtime.md#rt-rte-check-feedback) | check/evidence production | implemented | [EPI-OBJ-source-entries](#epi-obj-source-entries) | no content change | Parsed schema/reference/syntax conformance | Configured checker predicates; structural domain | Explicit check, watch or editor event | Diagnostics | Advisory diagnostic output | Bounded structural evidence only | Supplies potential revision reasons | Agent/editor / stdout or LSP / advisory / until next check | SRC-1, `packages/thalo/src/checker/rules/rules.ts` | [RT-CLM-agent-feedback](runtime.md#rt-clm-agent-feedback) | none | Does not validate body truth; visitors not exhaustively verified. |
| [RT-RTE-check-feedback](runtime.md#rt-rte-check-feedback) | disposition/acceptance | implemented | [EPI-OBJ-source-entries](#epi-obj-source-entries) | no content change | Whether CLI check may exit successfully | Error count and optional warning budget | After explicit checking | Nonzero exit on failed criterion | Enforcing process exit, not file gate | No evidence-consuming subject-matter acceptance | Blocks successful check completion, not independent writers | CLI caller / exit code / enforcing / that process | SRC-1, `apps/thalo-cli/src/commands/check.ts` | [RT-CLM-agent-feedback](runtime.md#rt-clm-agent-feedback) | gate-bypass | Action/Pi do not require this check. |
| [EPI-RTE-query-selection](#epi-rte-query-selection) | operational admission/selection/consumption | implemented | [EPI-OBJ-source-entries](#epi-obj-source-entries) | no content change | Query membership and result delivery | Parsed query, optional entity validation, limit and cutoff | Caller request; see record | Selected entries, errors or null | Symbolic selection | Matching metadata is not endorsement | Selects material visible to caller | Caller / structured result or raw text / enforcing membership / request | SRC-1, `packages/thalo/src/commands/query.ts` | none | none | Lower predicate implementation uninspected. |
| [RT-RTE-actualize-selection](runtime.md#rt-rte-actualize-selection) | lineage/freshness/recovery | implemented | [RT-OBJ-checkpoint](runtime.md#rt-obj-checkpoint) | no content change | Changed matching entries since marker | Tracker/query rules, not truth evaluator | Before each pending decision | Changed list or up-to-date flag; replay/failure alternatives | Cutoff and source-cleanliness gate | No license that prose is current or correct | Enables/skips command and alters future context | Actualize/action / checkpoint and selected list / enforcing selection / later loads | SRC-1, `packages/thalo/src/commands/actualize.ts` | none | freshness-not-warrant | Deleted/no-longer-matching entries and timestamp in-place edits not emitted; force/fallback differ. |
| [RT-RTE-pi-synthesis](runtime.md#rt-rte-pi-synthesis) | content transformation | implemented | [EPI-OBJ-synthesis-prose](#epi-obj-synthesis-prose) | truth-apt transformation: indeterminate | New Markdown from selected entries and current file | Model generation under stored/static guidance; semantic domain opaque | One prompt per script invocation | Candidate text | Candidate generation only | No demonstrated entailment, non-entailment or acceptance | Supplies proposed replacement prose | Host / streamed text deltas / permissive candidate supply / invocation | SRC-1, `packages/scripts/src/synthesize-with-pi.mjs` | [EPI-CLM-synthesized-understanding](#epi-clm-synthesized-understanding) | candidate-not-acceptance | Actual proposition and relation require output plus inputs; fluency would not settle warrant. |
| [EPI-RTE-output-guard](#epi-rte-output-guard) | check/evidence production | implemented | [EPI-OBJ-synthesis-prose](#epi-obj-synthesis-prose) | no content change | Nonempty generated text and available reconstruction inputs | Program string/fence/identifier/checkpoint predicates | After generation, before write | Throw or continue | Enforcing pre-write guards | Evidence only of nonemptiness and packaging prerequisites | Blocks that update on predicate failure | Host / exceptions / enforcing / invocation | SRC-1, `packages/scripts/src/synthesize-with-pi.mjs` | none | none | Neither H1 nor factual accuracy nor source coverage checked. |
| [EPI-RTE-output-guard](#epi-rte-output-guard) | disposition/acceptance | implemented | [EPI-OBJ-synthesis-prose](#epi-obj-synthesis-prose) | no content change | Candidate eligibility for disk installation | Host accepts passing text; human has no pre-write decision | After guards | Prose passed to reconstruction/write | Permissive operational admission | Not epistemic acceptance against an evidence criterion | Permits overwrite | Host writer / returned string / permissive / immediate write | SRC-1, `packages/scripts/src/synthesize-with-pi.mjs` | none | admission-not-warrant | Later PR veto does not retroactively supply acceptance at this point. |
| [EPI-RTE-file-reconstruction](#epi-rte-file-reconstruction) | content transformation | implemented | [EPI-OBJ-synthesis-prose](#epi-obj-synthesis-prose) | truth-apt transformation: non-ampliative reshaping | Packaging supplied Markdown, retained prefix/block, omitted suffix | Fixed first-fence slicing, no truth evaluator | Before write | Reconstructed file | Enforcing text replacement | No added warrant; omitted suffix can lose assertions/lineage | Replaces whole suffix, not just target prose | Writer / string return / enforcing / installed file | SRC-1, `packages/scripts/src/synthesize-with-pi.mjs` | [EPI-CLM-preserve-content](#epi-clm-preserve-content) | unrelated-suffix-loss | Does not search target block by ID; model can reproduce suffix but preservation is not guaranteed. |
| [EPI-RTE-prose-retention](#epi-rte-prose-retention) | retention | implemented | [EPI-OBJ-synthesis-prose](#epi-obj-synthesis-prose) | no content change | Passing reconstructed text to retained file | Host write, no additional evaluator | After guards/reconstruction | Prose and checkpoint retained | Enforcing disk write | Retention supplies no semantic warrant | Prior prose can influence a later generation | Pi host / entire current file in user prompt / advisory to model / later invocations | SRC-1, `packages/scripts/src/synthesize-with-pi.mjs` | none | none | Not lifecycle integration after acceptance; read-back activation unobserved. |
| [RT-RTE-action-publication](runtime.md#rt-rte-action-publication) | disposition/acceptance | implemented | [EPI-OBJ-synthesis-prose](#epi-obj-synthesis-prose) | no content change | Publication eligibility of working-tree changes | Successful subprocess return and Git operations | After all commands; see record | Commit, forced branch push and PR | Enforcing publication after return | Exit success is not content correctness | Publishes all staged changes before human review | Action / git add and push / permissive admission / branch lifetime | SRC-1, `packages/thalo-action/src/action.ts` | none | publication-not-acceptance | No automatic rollback of earlier writes on failure; base-branch human acceptance external. |
| [EPI-RTE-merge-check](#epi-rte-merge-check) | check/evidence production | implemented | [EPI-OBJ-source-entries](#epi-obj-source-entries) | no content change | Syntax and conflicting version changes | Parser plus default/custom conflict predicates; text/AST domain | Git/manual merge request | Conflict list or no conflicts | Result guides merge disposition | Detects specified disagreement, not which assertion is true | Changes automatic merge eligibility | Merge builder / conflict list / enforcing selection / merge invocation | SRC-1, `packages/thalo/src/merge/conflict-detector.ts` | none | none | No global semantic-consistency criterion established. |
| [EPI-RTE-merge-disposition](#epi-rte-merge-disposition) | disposition/acceptance | implemented | [EPI-OBJ-source-entries](#epi-obj-source-entries) | truth-apt transformation: non-ampliative reshaping | Existing alternatives, deletions and unresolved conflicts | Software chooses changes or emits conflict markers; Git/user later resolves | After conflict detection | Reconstructed file written even on conflict; exit 0/1 | Disk admission plus Git-facing failure signal | Conflict-free does not establish subject-matter truth | Deletes selected entries or blocks clean merge completion | Driver / ours file and exit / enforcing local write and status / later reload | SRC-1, `packages/thalo/src/merge/entry-merger.ts` | none | none | Full serializer fidelity unassessed; manual resolution is not observed acceptance. |

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [RT-CLM-agent-feedback](runtime.md#rt-clm-agent-feedback) | see record | SRC-1, `README.md`; doctrine/design | Structural/reference feedback as stated | [RT-RTE-check-feedback](runtime.md#rt-rte-check-feedback) | None supplied | No agent correction/comparison; action bypasses checker | Structural feedback capacity exists | Higher quality means no demonstrated semantic truth gain. |
| [EPI-CLM-synthesized-understanding](#epi-clm-synthesized-understanding) | see record | SRC-1, `README.md`; doctrine/design | Query plus model synthesis; minimal CLI preparation | [RT-RTE-actualize-selection](runtime.md#rt-rte-actualize-selection), [RT-RTE-pi-synthesis](runtime.md#rt-rte-pi-synthesis) | None supplied | No accepted-claim decision or outcome comparison | Candidate synthesis is wired in shipped driver | Understanding and epistemic warrant are unestablished, not disproven. |
| [EPI-CLM-preserve-content](#epi-clm-preserve-content) | see record | SRC-1, `packages/scripts/src/synthesize-with-pi.mjs`; doctrine/design prompt | Requests narrow in-place updates | [EPI-RTE-file-reconstruction](#epi-rte-file-reconstruction) | None supplied | First-block slicing supplies deterministic countercase | Prefix and first fence retained; original suffix not independently preserved | Prompt is stronger than host preservation guarantee. |

## Bounded conclusion

Thalo acquires externally authored entry content and gives it symbolic structure, selection and structural feedback. Source truth is unknown. Reference resolution licenses only that a definition exists in the loaded workspace; schema conformance licenses only satisfaction of configured structural predicates. Diagnostic results can enforce a CLI exit and advise a collaborating agent, but they are not a universal write-admission gate. See [RT-RTE-check-feedback](runtime.md#rt-rte-check-feedback), SRC-1, `packages/thalo/src/checker/rules/unresolved-link.ts`.

The shipped Pi route can produce truth-apt candidate prose, install it and deliver that retained prose to a later model invocation. Actual output relations remain indeterminate: no supplied input/output instance establishes entailed derivation or non-entailed conjecture. No warranted premises, truth evaluation, or evidence-consuming epistemic acceptance is established for that prose. The operative admission criteria are nonempty output and reconstruction prerequisites; intended operational use is replacement Markdown, not a checked subject-matter claim. Publication adds subprocess-success admission and a PR-review opportunity, not pre-write epistemic acceptance. See [EPI-RTE-output-guard](#epi-rte-output-guard), [EPI-RTE-prose-retention](#epi-rte-prose-retention), [RT-RTE-action-publication](runtime.md#rt-rte-action-publication), SRC-1, `packages/scripts/src/synthesize-with-pi.mjs`, `packages/thalo-action/src/action.ts`.

The host may lose unrelated original suffix content while retaining a checkpoint that shapes future selection. That checkpoint has enforcing selector force across loads, not warrant that the model incorporated the selected entries. Git/timestamp differences and omitted deletions bound refresh claims independently of synthesis quality. See [EPI-RTE-file-reconstruction](#epi-rte-file-reconstruction), [RT-BAP-checkpoint-selection](runtime.md#rt-bap-checkpoint-selection), SRC-1, `packages/scripts/src/synthesize-with-pi.mjs`, `packages/thalo/src/commands/actualize.ts`.

Merge checks and conflict disposition are an additional material route, not evidence of semantic acceptance. Syntax/disagreement results change local output and Git continuation; one-sided entry deletion can withdraw content from later loads, while conflict output remains written locally. This is software version reconciliation, not demonstrated criticism of the entry's explanatory account. See [EPI-RTE-merge-check](#epi-rte-merge-check), [EPI-RTE-merge-disposition](#epi-rte-merge-disposition), SRC-1, `packages/thalo/src/merge/driver.ts`, `apps/thalo-cli/src/commands/merge-driver.ts`.

No inspected Pi/action route establishes lifecycle integration after epistemic acceptance or direct evaluator-driven revision of its own method. Retained prompts can guide future model behavior and checkpoints deterministically adapt later context membership; those are separate authority paths, not proof of improved capacity. Learning, reflection, criticism-driven theory building and self-improvement remain independently unestablished here, not bundled into a system-wide negative. Provider processing is opaque and model parameter changes are uninspected; successful generation, retention and later use are themselves unobserved. Unassessed formatter, query predicate and extension details prevent a system-complete negative. See [RT-BAP-synthesis-guidance](runtime.md#rt-bap-synthesis-guidance), [RT-CMP-gpt5-mini](runtime.md#rt-cmp-gpt5-mini), SRC-1, `packages/scripts/src/synthesize-with-pi.mjs`.

## Shared records

### Operative objects

#### EPI-OBJ-source-entries
Label: Selected source-entry payload

Part of: [RT-OBJ-command-input](runtime.md#rt-obj-command-input)

Source-native identity: `entries` payload of command JSON. Representational form: natural-language raw entry bodies with symbolic title/type/link/tag wrappers. Storage substrate: source files, serialized transiently on stdin and reformatted into model prompt text. This part is distinct from routing/checkpoint fields in the supplied container. Some assertions are truth-apt; initial truth and authorship are unknown. The script does not separately forward `entry.file` or `entry.timestamp`, though raw text can retain such information. This supports weakened explicit provenance delivery, not total removal of provenance. SRC-1, `packages/thalo-action/src/action.ts`, `packages/scripts/src/synthesize-with-pi.mjs`.

> `Entry: ${entry.title ?? "(untitled)"}`,
> `Type: ${entry.entity ?? "unknown"}`,
> entry.linkId ? `Link: ^${entry.linkId}` : null,
> entry.tags?.length ? `Tags: ${entry.tags.join(", ")}` : null,
> entry.rawText?.trim() ? `Raw:\n${entry.rawText.trim()}` : null,
> --- `packages/scripts/src/synthesize-with-pi.mjs`

#### EPI-OBJ-synthesis-prose
Label: Generated and retained synthesis prose

Part of: [RT-RTE-pi-synthesis](runtime.md#rt-rte-pi-synthesis)

The parent is a route; this is its material candidate-output part, not another route declaration. Source-native identity: `output`, then `trimmedOutput`/`markdown` in the Pi command. Representational form: natural-language Markdown. Storage substrate: transient text-delta string followed by target file suffix. It differs from [RT-OBJ-system-prompt](runtime.md#rt-obj-system-prompt), which is guidance, and [RT-OBJ-checkpoint](runtime.md#rt-obj-checkpoint), which is selector state. The entire retained file can later enter another model request. Actual candidate propositions and their truth relations are not determinable without a linked output trace. SRC-1, `packages/scripts/src/synthesize-with-pi.mjs`.

> let output = "";
> agent.subscribe((event) => {
>   if (event.type === "message_update" && event.assistantMessageEvent.type === "text_delta") {
>     output += event.assistantMessageEvent.delta;
>   }
> });
> --- `packages/scripts/src/synthesize-with-pi.mjs`

### Routes

#### EPI-RTE-query-selection
Label: Query result selection

Distinct identity: standalone `runQueries`/`runQuery`, compared with [RT-RTE-actualize-selection](runtime.md#rt-rte-actualize-selection). Both select entries, but query returns caller-requested results and validation errors rather than synthesis work/checkpoint outputs. SRC-1, `packages/thalo/src/commands/query.ts`, implementation.

Endpoints/progression: caller query/options plus workspace → parsed queries and optional validation → query/tracker filtering → optional limit → file-associated structured entries. Owner: program; caller chooses request, limit and tracker. This is an open retrieval request, not an experiment or answer oracle. No semantic proposal/admission occurs; caller can change query or discard result.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Structured entries/count/query description, null on invalid query, or entity/checkpoint error.
- Later read-back: inapplicable — this producer writes no retained result; it reads caller workspace.
- Delegated visibility: Calling code receives structured results and optional source raw text.
- Selection predicate: Parsed query matches, optional since marker, positive limit and located file; entity validation defaults on.
- Invalidation or expiry: inapplicable — no persisted query result is maintained by this route.
- Activation or effect: Determines caller-visible entries; no endorsement or observed downstream use.
- Evidence limits: Lower query service and type semantics not exhaustively inspected; source code is not execution evidence.

> const limitedResults = limit && limit > 0 ? results.slice(0, limit) : results;
> --- `packages/thalo/src/commands/query.ts`

#### EPI-RTE-output-guard
Label: Pi output guard and operational admission

Part of: [RT-RTE-pi-synthesis](runtime.md#rt-rte-pi-synthesis)

Endpoints/progression: generated text → trim/nonempty check → reconstruction prerequisite checks → eligible string for host write. Owner/decider: host program; proposer: model. Target/domain: output nonemptiness, first Thalo fence existence/termination, target link and checkpoint presence. No answer oracle or evidence criterion for body truth. Open synthesis trigger; no per-content human veto before write. Failure throws before that update; later editing/revert and PR veto remain possible, not automatic rollback. Guidance is the parent's static and retained prompt; accepted local prose/checkpoint persist. This part separates guard/admission from generation and retention without superseding the valid container. SRC-1, `packages/scripts/src/synthesize-with-pi.mjs`, implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Continuation with reconstruction inputs, or exception.
- Later read-back: inapplicable — guard results are not retained; passing prose is retained by the separate write part.
- Delegated visibility: Host sees text and exceptions; command exit reaches action, not a subject-matter verdict.
- Selection predicate: Trimmed output must be nonempty; reconstruction requires fences, link and checkpoint.
- Invalidation or expiry: Recomputed per invocation; no persistent acceptance decision.
- Activation or effect: Failing checks block local update; passing checks permit write, not epistemic acceptance.
- Evidence limits: No output trace or semantic-check criterion; provider error behavior outside inspected source.

> const trimmedOutput = output.trim();
> if (!trimmedOutput) {
>   throw new Error("Pi agent returned empty output.");
> }
> --- `packages/scripts/src/synthesize-with-pi.mjs`

> if (!checkpoint) {
>   throw new Error("Missing current checkpoint for synthesis.");
> }
> --- `packages/scripts/src/synthesize-with-pi.mjs`

#### EPI-RTE-file-reconstruction
Label: First-fence file reconstruction

Part of: [RT-RTE-pi-synthesis](runtime.md#rt-rte-pi-synthesis)

Endpoints/progression: original file plus passing Markdown/link/checkpoint → first-fence slices → appended actualization entry → replacement string. Owner: host program. Non-ampliative text packaging/replacement does not independently warrant generated content; it can drop unrelated assertions and later blocks. Trigger is passing generation; admission guards are the separate part above. No truth evaluator, human choice or answer oracle in the transformation. Static narrow-edit guidance shapes the model proposal but is not enforced by slicing. SRC-1, `packages/scripts/src/synthesize-with-pi.mjs`, implementation; counterpart claim [EPI-CLM-preserve-content](#epi-clm-preserve-content).

Concrete source deduction, not execution: take an input with prefix `P`, first Thalo fenced block `B`, followed by unrelated suffix `U` and a second block `C`; supply generated Markdown `M`, link `x` and checkpoint `git:h`. `fenceStart` chooses the first block regardless of `x`. `before` retains `P`; `block` retains `B` without its closing fence; `blockWithActualize` adds a timestamped marker. `closingFence` retains only the first closing line. The returned string contains `P`, first block plus marker and `M`; neither `U` nor `C` is independently copied. If M repeats them they survive by model reproduction only. This countercase limits preservation and lineage, not observed loss frequency.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Reconstructed Markdown string or prerequisite error.
- Later read-back: inapplicable — this function itself returns a string; the separate retention part writes it for later use.
- Delegated visibility: Host writer receives replacement string.
- Selection predicate: First literal Thalo fence and its next closing fence; target ID does not choose a block.
- Invalidation or expiry: Original suffix is replaced in returned string; later writes can replace it again.
- Activation or effect: Determines installed text layout and possible omission; body truth not evaluated.
- Evidence limits: Concrete transformation is inferred from source; model reproduction and actual file layouts unobserved.

> const fenceStart = source.indexOf("```thalo");
> --- `packages/scripts/src/synthesize-with-pi.mjs`

> return `${before}${blockWithActualize}${closingFence}\n\n${markdown}\n`;
> --- `packages/scripts/src/synthesize-with-pi.mjs`

#### EPI-RTE-prose-retention
Label: Synthesis prose retention and read-back

Part of: [RT-RTE-pi-synthesis](runtime.md#rt-rte-pi-synthesis)

Endpoints/progression: reconstructed file → filesystem write → later script file read → whole trimmed current file in a subsequent model prompt. Owner: host program. This part separates retention/read-back from generation and guard admission; it is not lifecycle integration after epistemic acceptance. Open pending-synthesis trigger; model proposes, host writes, human has later edit/PR veto. No independent quality oracle. Recovery is later edit/Git, not automatic rollback. Static and definition guidance remain; generated prose and checkpoint persist. SRC-1, `packages/scripts/src/synthesize-with-pi.mjs`, implementation. Checkpoint consumer is separately see [RT-BAP-checkpoint-selection](runtime.md#rt-bap-checkpoint-selection).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Disk write completion and log, or I/O exception.
- Later read-back: Entire target file content, including previous generated prose, enters later script userPrompt.
- Delegated visibility: Model receives current file text, selected entry payload and prompt; provider retention is uninspected.
- Selection predicate: Parent input file resolved against process cwd, read in full; no prose-specific retrieval predicate.
- Invalidation or expiry: Subsequent reconstruction replaces suffix; external edits can change file; no automatic factual expiry.
- Activation or effect: Retains candidate prose for possible influence on later generation; no observed behavioral activation.
- Evidence limits: Retention and prompt supply do not prove model reliance, acceptance, learning or quality.

> "Current File Content:",
> original.trim() || "(file is empty)",
> --- `packages/scripts/src/synthesize-with-pi.mjs`

Write passage is see [RT-RTE-pi-synthesis](runtime.md#rt-rte-pi-synthesis).

#### EPI-RTE-merge-check
Label: Merge syntax and conflict checking

Part of: [RT-RTE-local-authoring](runtime.md#rt-rte-local-authoring)

Endpoints/progression: base/ours/theirs → parsed ASTs → syntax conflicts or matched entries → default/custom conflict rules → conflicts consumed by builder. Owner: software; caller supplies versions and optional custom rules. Target/domain: parsed syntax and defined concurrent-change contrasts (duplicate IDs, metadata, content, schemas, titles), not assertion truth. Reference is base plus alternative versions, not an expected semantic answer oracle. Git/manual open reconciliation, not improvement experiment. Software decides conflict status; human can later resolve or replace versions. This part is distinct from diagnostics in [RT-RTE-check-feedback](runtime.md#rt-rte-check-feedback): three-way version state, not workspace schema conformance. SRC-1, `packages/thalo/src/merge/driver.ts`, `packages/thalo/src/merge/conflict-detector.ts`, implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Conflict list; syntax/exception path produces unsuccessful result with original ours content.
- Later read-back: inapplicable — check results themselves are not retained by this producer; disposition writes file output.
- Delegated visibility: Builder/driver receives conflicts; CLI can display them and Git receives exit status.
- Selection predicate: Matched triplets, default rules followed by caller custom rules, first detected conflict per match.
- Invalidation or expiry: Recomputed from supplied versions on each merge.
- Activation or effect: Conflict result selects marked output versus automatic entry merge and changes success status.
- Evidence limits: Matching internals and exhaustive correctness unassessed; version disagreement does not decide factual truth.

> const rules: ConflictRule[] = [...DEFAULT_CONFLICT_RULES, ...(options.conflictRules || [])];
> --- `packages/thalo/src/merge/conflict-detector.ts`

> if (oursValue !== baseValue && theirsValue !== baseValue && oursValue !== theirsValue) {
> --- `packages/thalo/src/merge/conflict-detector.ts`

#### EPI-RTE-merge-disposition
Label: Merge output admission and withdrawal

Part of: [RT-RTE-local-authoring](runtime.md#rt-rte-local-authoring)

Endpoints/progression: matches/conflicts → conflict markers or selected merged entries → timestamp-ordered output → write ours → success exit. Owner: software; human/Git owns later conflict resolution. This is a distinct disposition part of local authoring, linked to [EPI-RTE-merge-check](#epi-rte-merge-check). Trigger is explicit driver request; proposed content comes from existing versions and deterministic reconstruction, not model generation. Program decides local output and Git-facing status. No epistemic acceptance criterion or answer oracle. Admission happens even when conflicts remain. Later user resolution/revert is available, not automatic rollback. Guidance is the fixed merge predicates/options; retained result is merged text or conflict-marked text, not a retained truth decision. SRC-1, `packages/thalo/src/merge/merge-result-builder.ts`, `packages/thalo/src/merge/entry-merger.ts`, `apps/thalo-cli/src/commands/merge-driver.ts`, implementation.

Concrete deduction: a matched base entry present in theirs but absent in ours reaches `mergeEntry`'s deletion branch and returns null. Builder emits nothing for null. If no conflict was recorded for that match, its assertion is withdrawn from the resulting file without a truth judgment. Other conflict-bearing entries instead get marked output. This is a bounded route case, not a claim all deletion/edit combinations merge cleanly.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: File output and exit 0/1, or fatal I/O exit 2.
- Later read-back: Saved merged entries, schemas, prompts or markers enter subsequent workspace loads, as in parent local-authoring route.
- Delegated visibility: Git receives status; human can receive conflicts; downstream loaders receive saved text.
- Selection predicate: Conflicted matches get markers; other matches invoke mergeEntry; null deletes; survivors sort by timestamp.
- Invalidation or expiry: Subsequent edit/merge/revert changes saved result; deletion withdraws entry from this output.
- Activation or effect: Writes ours regardless of success; nonzero conflict status blocks treating merge as clean, not local file installation.
- Evidence limits: Serialization fidelity and human resolution uninspected; no observed successful merge or accepted truth revision.

> if (base && !ours && theirs) {
>   return null;
> }
> --- `packages/thalo/src/merge/entry-merger.ts`

> success: conflicts.length === 0,
> content: lines.join("\n"),
> --- `packages/thalo/src/merge/merge-result-builder.ts`

> process.exit(result.success ? 0 : 1);
> --- `apps/thalo-cli/src/commands/merge-driver.ts`

Write passage is see [RT-RTE-local-authoring](runtime.md#rt-rte-local-authoring).

### Claims

#### EPI-CLM-synthesized-understanding
Label: Query and model synthesized understanding

Claimed operation: structured entries plus queries and LLMs yield synthesized understanding; README also deliberately limits actualization itself to printing selected entries and prompt. Distinct from [RT-CLM-agent-feedback](runtime.md#rt-clm-agent-feedback), whose benefit concerns entry structure. SRC-1, `README.md`, doctrine/design. Shipped implementation is see [RT-RTE-pi-synthesis](runtime.md#rt-rte-pi-synthesis); the README slogan does not establish accepted new knowledge.

> **Scattered thoughts → Structured entries → Queries + LLMs → Synthesized understanding.**
> --- `README.md`

#### EPI-CLM-preserve-content
Label: Preserve unrelated synthesis content

Claimed operation: model should update current synthesis in place without replacing unrelated content. This is the request carried by [RT-OBJ-system-prompt](runtime.md#rt-obj-system-prompt), not a duplicate object or guarantee; the claim is distinct from structural feedback. SRC-1, `packages/scripts/src/synthesize-with-pi.mjs`, doctrine/design prompt. Load-bearing request passage is see [RT-OBJ-system-prompt](runtime.md#rt-obj-system-prompt). Countercase is [EPI-RTE-file-reconstruction](#epi-rte-file-reconstruction): first-fence suffix replacement has weaker protection than requested.
