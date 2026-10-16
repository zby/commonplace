# Supermemory reentry publication audit

## Disposition

**hold** — normal synthesis verification did not correct the consequential capture qualification identified in the prior exact-publication audit. The public synthesis and all analyst work are byte-identical to the old publication. Only synthesis verification and its manifest pin changed. The renewed verifier explicitly carries a previously public MCP coverage limit, but finds no material defect and supplies no correction. Workflow completion is not evidence of semantic correction.

Unblock through an authorized correction route: narrow the public capture claim to structured tool-call/result parts and disclose the serializer's ungated generic non-system string-content branch, or establish an enforced input boundary excluding that case and publish the corresponding scope. Reconcile affected supporting/verification wording and revalidate the resulting exact publication. This report does not amend the analysis or authorize recovery or integration.

## Identity, auditor and evidence roots

- run-id: AAS-2026-10-15-supermemory-ae21530d128d-01
- method-commit: a568c6dc489ad546374536b642c3889ce23149a8
- source-revision: 5323f427d076c7a158a9154867d293b53acc3841
- Source identity: `https://github.com/supermemoryai/supermemory`, sole source SRC-1.
- Auditor: fresh independent Pi worker; exposed environment reports provider `openai`, model `gpt-6.1-sol`, reasoning `medium`; session `01a1464a-366f-738c-86dd-bd706526a758`. No delegation or analysis-worker feedback.
- W: `/home/zby/llm/commonplace/.commonplace/worktrees/supermemory-ae21530d128d`.
- S: `W/kb/agentic-system-analyses/state/AAS-2026-10-15-supermemory-ae21530d128d-01`.
- P: `W/kb/agentic-system-analyses/retained/supermemory`.
- Source: `W/related-systems/supermemoryai--supermemory`.
- A: `W/kb/agentic-system-analyses/state/.reset-history/AAS-2026-10-15-supermemory-ae21530d128d-01/c4641c185d92496a859fab8477b9f59b`.
- Old publication: `A/effects/0/before`; old run: `A/before`.

Followed [audit procedure](../../audit-a-rerun.md). Read `kb/work/COLLECTION.md`, `kb/types/text.md`, workshop framing, both historical leads and the [prior exact-publication audit](./AAS-2026-10-15-supermemory-ae21530d128d-01.md) completely. Historical material selected questions; frozen current source decided the bounded discrepancy below.

## Old/new byte binding and preservation

Recomputed recursive SHA-256 maps for both publication trees: **13 files each, identical name sets, no extras or missing members**. Eleven files are identical; the following two differ:

| File | Old SHA-256 | New SHA-256 |
| --- | --- | --- |
| ARTIFACT.yaml | `81cc49dc18bf4cfa5370c3b3f137eb9c7e1e3c2737cdb8998331f6d1d8105637` | `95f0ddb7d121e122e3486e944ff1dd42e227d59f109fee436dbf0e946ae4b0dd` |
| synthesis-verification.md | `fe2c2d7a61ae8c9dd6cc0b08c6ef0dbdea5e2799693ed315fe3825f707b04fae` | `b3c2381497ef51c7d2870e50c7bd384c919e9428912359641c1d473213cebcfd` |

All remaining hashes apply to **both** old and new:

```text
boundary.md             20eb29eca250e721b520d0cd36ddf7ec0f57478b6d9f71cf50344ce4c7e1660e
epistemic.md            183d92e94300d3349864eed223e892272f09cde5b5ec5bafc4d2f254ad9e0c76
memory-profile.md       7defc03d8523d173ccadb52676f49eb97e737bc3fd1c6563d6d526c63c64dc66
memory.md               6652f96342325249cda8c7dd9433de1ceb01695b758569a1f1d65372eebe9376
overview.md             a8c0e9c1e3396d7fa62af76a5bf07c368821ae3d9d0e7d9acf1c876aaaa27935
profile-verification.md 05ba8b87f94d5e0d934c4e0205e01abf968edbca43f1d1006478c70dfde360df
reconciliation.md       2b26e381f4522e2a311316bfa59509f039e2fd31c70393b494c3dfc06a841f35
report-verification.md  7fb6a7d1ee7460eb9c897c57ffa1ccf00cdd826c8cceac64ee45db22b4583c7d
runtime.md              0c497672094cb1d42b2e72d328073efacfb18fd946b9ad2755bb7291d68e2be6
synthesis.md            44cb739cef2298c6610434b39cecbe414416cc73ed017ab82f4efcada1d30371
workflow.md             858bd961fa03baffdf229846c333199e9c8bcc57268c2f7eafa234fd60cff679
```

For a compact independent binding, SHA-256 of each complete map encoded as Python `json.dumps(map, sort_keys=True, separators=(',', ':')).encode()` is old `cc697aa249b34a5c8876b9458e13eb24fa34bc3adfbc330cb052492904d65963`, new `81e3781f2181b991b7a5909c94b3fe70511e03aec761fd02fb558910ce7e758f`.

The old map exactly matches the completed archived publication effect `A/effects/1/before`; the new map exactly matches completed `S/effects/publish.json`. Both assembled manifests pin all twelve Markdown members correctly. All current working Markdown members match P. The working `S/artifact/ARTIFACT.yaml` is only the type declaration, not the assembled manifest; no equivalence is claimed for that file.

Read-only Git checks (`git --no-optional-locks`) confirm W HEAD equals method-commit and Source HEAD equals source-revision. Source status is clean; W status contains only the untracked retained publication directory. Opening metadata version `b3b520fc99677ee2db9f8378063b5a0c0fe5e2f2f5264baa69ffe0e4af61df04` binds run ID and inputs commit; acquired source version `490eb1da50931f11105ea45a649245b65e489e5a46b3b43abcdb939fd88d5a2e` binds identity/path/revision. `S/run.json`, acquisition effect, all **29 attempts and 22 judgments before sequence 30**, and the eleven unchanged working Markdown members are byte-identical to A/before. These checks establish preserved upstream records, not complete worker compliance.

## What ordinary verification changed

Inspected the complete publication diff, overview, synthesis, boundary, report/profile verification, renewed synthesis verification and relevant attempts/judgments.

`A/reset.json` records completed reset of synthesis-verification and downstream apply/assemble/publish, archiving attempts 000030–000033. Old synthesis attempt 000028 and check 000029 remain unchanged. New attempt `S/state/attempts/000034-synthesis-verification.json` takes the same synthesis hash as old 000030, has null refusal, and outputs the new verification plus empty answers. No synthesis-author correction attempt follows it.

Old apply judgments `A/before/state/judgments/000031-apply-synthesis-verification-{0,1}.json` and new `S/state/judgments/000035-apply-synthesis-verification-{0,1}.json` both accept their verifier and the **same synthesis**, with empty findings and no overrides. New assembly 000036 pins the new verifier and unchanged overview; completed publication 000037 pins the new assembled manifest. These are acceptance records, not a corrected capture account.

Substantive delta: the new verifier changes `Limits: none` to an explicit carried MCP inventory limitation. It names optional editable saving, persistent active-space storage and transactional upload expiry/token/single-use controls, and withholds exhaustive admission/recovery comparisons and service-durability inference. This improves the verifier's own disclosure. Those facts and consequences were already in the old synthesis's Limitations table and report verification; they are **not newly recovered public coverage**. The remaining verifier prose reorganizes its support judgment, explicitly noting five-second abort versus deadline race and separate model dependencies. It still says no source files were read, no corrected text is supplied and no material synthesis defect was found. No important public coverage was lost in the renewal: the public account is exactly unchanged. No consequential public correction was made either.

## Bounded findings and historical coverage

### 1. Capture qualification remains unresolved — consequential hold

Current `P/synthesis.md`, “From a conversation to retained material,” still says the serializer “excludes tool payloads unless enabled.” `P/runtime.md:47` says “excludes tool payloads by default”; report verification repeats the broad opt-in statement. Neither public summary scopes this to structured parts or states the generic-content exception. The overview is navigation/identity, not a repair.

Independent source check: `Source/packages/tools/src/vercel/middleware.ts:65-84` skips system messages, then copies any nonempty string content with its non-system role, cast as `user | assistant | tool`, and continues. That branch does not consult `includeToolCalls`. Only the later structured `tool-call` and `tool-result` branches at lines 116–136 test that option. The narrower RT-RTE-conversation-save predicate (“tool calls/results are opt-in”) does not qualify the broader public sentence. The renewed verifier's capture approval does not identify this discrepancy.

This matters to deciding what conversation content automatic capture may submit. It is **not** an observed disclosure or an established valid typed SDK input route. `Source/packages/tools/src/vercel/util.ts:27-30` aliases call options to the external `LanguageModelV2CallOptions`; no enforced runtime exclusion was established in this bounded inspection. The historical narrow review is not proof of reachability either. Further SDK-input provenance work would exceed this audit's useful scope; the public claim can instead be narrowed to the source-visible guarantee. The specific unblock is stated above. A qualification only here cannot repair P.

### 2. Historical boundaries and preserved coverage

Read both leads completely:

- `kb/agent-memory-systems/reviews/supermemory.md`: broad June review at `c5bf8ff1f75fc5de22d03ca4be2e03630daa9f77`; includes browser capture, graph UI, connectors and many adapters.
- `kb/agentic-systems/reviews-archive/supermemory.md`: September Vercel-wrapper-only review, run `AAS-2026-09-25-supermemory-02`, revision `0e12f0b3a65af1cf7b03f48561f20ddf4369bc3f`; retains the generic tool-role string case, best-effort capture, cache and namespace qualifications.

Neither source revision was substituted for the October pin. The current synthesis preserves the major public-client/private-engine distinction, document/chunk/graph/profile separation, profile/query/full retrieval, prompt delivery versus model use, and no demonstrated causal benefit. It also retains optional inference review rather than asserting no review; unreviewed inferences remain search-eligible at lower rank. Exact document-backed file access and MCP host delivery prevent reducing all consumption to semantic retrieval.

The narrow review's capture/durability and withdrawal cautions largely survive publicly: unawaited saving, normal-flush dependence, caught errors, bounded local cache, new-user refetch and unresolved cross-store/cache/prompt erasure. Its generic-content capture qualification does not survive, and is the bounded source-confirmed discrepancy above. Historical conversation-specific retrieval addressing is not falsely promised by the current public synthesis; it describes namespace retrieval.

The broad review's browser/UI/connector inventory is not reproduced exhaustively. This is a coverage reduction relative to that historical review, **not a new loss caused by reentry**, and not proof those mechanisms disappeared. Current synthesis explicitly lists remaining web/graph/debug/upload/connector and adapter paths as unresolved, with every profile axis partial. No system-wide absence or exhaustive comparison is justified. Its public table already carries the positive MCP mechanisms missing from analyst inventory and the review claimed/afforded label disagreement without upgrading either to observed operation. These are useful, visible qualifications, but do not fix capture wording.

## Operational and audit limits

The supplied commission characterizes reentry as no-feedback external reset followed by ordinary orchestration. Archived reset/effect records and current attempts corroborate that recorded stage sequence. I did not inspect a new coordinator/worker trace for handle `33a2a0ba-8ce5-41d6-b1a0-e53e72edde3a`; no accessible trace was supplied as paired worker-action evidence. Consequently this audit does not certify instruction delivery, fresh-worker independence, no-feedback conduct or every worker obligation from acceptance records or the manifest's model/effort declarations. The original external trace was not sampled: exact-byte preservation and the frozen serializer settle the consequential question without it. The prior audit's trace claims are not newly certified here.

This is a discrepancy-led audit, not a second source analysis. Source inspection was bounded to the capture serializer and its type alias; other retained judgments were assessed for consistency, public visibility and preservation, not independently re-proven. Valid-input reachability, private service internals, all adapters, historical revision equivalence and complete worker compliance remain unresolved. No source acquisition, target code/tests/services, state-writing run command, advance/reset/judge, analysis/source/state/ledger/index edit, integration, staging, commit or delegation was performed. This report is the only authored file; findings were not fed to analysis workers.

## Validation

From W, using W/.venv/bin:

```text
.venv/bin/commonplace-validate --full kb/agentic-system-analyses/retained/supermemory
```

Exit 0. `Overall: PASS (clean)`; WARN, FAIL and INFO all `(none)`. Twelve Markdown members and directory artifact roles/relations passed. Batch: files analysed 1, text files 0, failing notes 0; no source-unavailable notice. Deterministic validation does not settle the semantic hold.

Also from W: `.venv/bin/commonplace-validate --full /home/zby/llm/commonplace/kb/work/agentic-system-reruns/audits/next-publications/AAS-2026-10-15-supermemory-ae21530d128d-01-reentry.md`. Exit 0; type `text`; base text check passes with no structural requirements. `Overall: PASS (clean)`; WARN, FAIL and INFO all `(none)`. Text validation does not certify the audit judgment.
