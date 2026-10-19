# Batch-21 Supermemory independent publication audit

## Disposition

**hold — the public capture guarantee still needs a bounded qualification.** At the fresh source revision, the serializer gates structured tool-call/result parts on `includeToolCalls`, but copies generic non-system string content without that check. The new runtime still describes “default exclusion of tool payloads”; the synthesis says optional tool payload capture adds traces “only when enabled.” Neither discloses the generic branch nor establishes an enforced input restriction excluding it. This affects a reader deciding what automatic capture may submit.

This is not an observed disclosure or proof that valid typed SDK tool input reaches that branch. Integration can be unblocked by publishing the source-visible distinction, or by establishing and publishing the applicable enforced input boundary. Align the supporting runtime and public synthesis, reconcile dependent verification/profile wording as needed, and revalidate the resulting exact publication through an authorized recovery route. An audit-only qualification cannot repair the public analysis. Parent owns recovery and integration; none was performed here.

## Identity and method

- Run: `AAS-2026-10-18-supermemory-75d21b14316b-01`.
- Source identity: `https://github.com/supermemoryai/supermemory`, sole source SRC-1.
- Source revision: `f81fad00e4bfc42610159cf6bd7bdb5fc4ca7cbe`; applicability cutoff 2026-10-18.
- Method/prepared worktree HEAD: `b12b855f4224ee847eaec5f269188b02ac532ccc`.
- Auditor: independent Pi session `01a14ff1-812d-765d-ad6e-c833cb4b3393`; exposed provider `openai`, model `gpt-6.1-sol`, reasoning `medium`. No delegation.
- W: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-21-fresh-supermemory`.
- R: `W/kb/agentic-system-analyses/state/AAS-2026-10-18-supermemory-75d21b14316b-01`.
- P: `W/kb/agentic-system-analyses/retained/supermemoryai--supermemory`.
- S: `W/related-systems/supermemoryai--supermemory`.
- T: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/batch-21/supermemory.output`.

Followed the [audit procedure](../audit-a-rerun.md), workshop framing, work collection contract and implicit text type contract. This report is the sole authorized output. Chose a discrepancy-led audit: read current public overview, boundary, synthesis and report/synthesis verifications completely; inspect capture records and targeted source; compare historical audit leads; sample settled worker actions rather than reconstruct the entire system. Stop at a consequential unresolved qualification rather than expand into dependency-input reachability analysis.

### Preparation and frozen evidence

`W.preparation.json` records status `ready`, token `75d21b14316b`, origin `/home/zby/llm/commonplace`, exact W, method commit above and command prefix `W/.venv/bin`. It records dirty-origin exclusion, not inclusion of uncommitted origin changes. Independently verified W HEAD, startup-file SHA-256 against preparation, command availability, and the current plan against `R/run.json`'s `plan_sha256` (`5a5f56891d95a819c3f4fde00bb92eb301876598c022924ee52bed6262721bfd`). Run parameters name the correct source and `pi-sol` profile. Preparation also appears as the successful result at T:311.

`R/effects/acquire.json` records completed acquisition at S and the source revision above; current S HEAD agrees and read-only Git status is clean. The boundary's source register pins the same source. No external dependency, live service or additional source was acquired or executed.

## Exact publication binding

Frozen from completed `R/effects/publish.json`, whose SHA-256 is `00c1acc1966cb5fcef240bfa3157f8443870f87c05dd679e3e32e8873b5a0bd6`. It names the correct run, source identity and P, with expected destination absent. Recursively enumerated and hashed P before inspection: exactly these **13 files**, matching `new` without extras or omissions.

```text
ARTIFACT.yaml             bab92062c630c6f1907e01e3e1d79f582be4b1889ab2dc9a24970480bbb22af3
boundary.md               e63b8830010ed71a22973d157b1edff066f60ec835f8a09bebdcfcc97ba057fb
epistemic.md              4a79fede6e7b4084fd66d4820b876c917d5bd8fc7be2e8c32d13bb196709ab47
memory-profile.md         869171dd99c903f0ef2e96c6adc16a2f1a598c472ae60da23d41da31940670a0
memory.md                 8d1370ae880b09ad2999ba80a39de49971ce99f192a5a42e68a84b4374494d3e
overview.md               ecd15fe1e92eefd255374e168a082db9ef00463e30800a6f5a547fd452ed9d20
profile-verification.md   dc547608308f0d4020f463293833f7ce96ec5de40d3b50177566e38dee1fd2f9
reconciliation.md         274cce6d3f7d3e709c3aadd7ed955cf6b13fa2d809b37963136e91514fdf448e
report-verification.md    e01ee49165830867b2d25a427d6b0b7865850a612c902648f9f122739f15bf66
runtime.md                9d036e5bb0f25840e57019c5f1fd707cad040ce7eb53c735f8f78b739f52e928
synthesis-verification.md 8c6f82badeb4f8eb84485e535d2664941ebf9ceb8268ee008740d0971d159ac1
synthesis.md              3a1b427eb5d6afacb07fb397647b5e5356e239d99da4a1127d1d85629e17ae93
workflow.md               eda616175555843a7e95c5afe268cbf88c5cc16ae02b20646c82ef6880fd9215
```

Map digest using `sha256(json.dumps(map, sort_keys=True).encode())`: `e53f36c7a16e31bed03dfacba6b593f173dfe65861632df8793ec387b8918a3d`. Final post-audit verification is recorded below. These are own-worktree bytes, not an origin copy or integration approval.

## Consequential finding: capture scope

The new revision was checked directly; the historical finding was not assumed to persist.

At `S/packages/tools/src/vercel/middleware.ts:65–84`, `convertToConversationMessages` skips system messages, then copies nonempty string content and continues:

```typescript
if (typeof msg.content === "string") {
    if (msg.content) {
        messages.push({
            role: msg.role as "user" | "assistant" | "tool",
            content: msg.content,
        })
    }
    continue
}
```

That branch does not consult `includeToolCalls`. Later structured `tool-call` and `tool-result` branches at lines 116–136 do. The source-visible guarantee is therefore narrower than unconditional exclusion of tool payloads unless enabled.

The publication mixes narrower and broader language:

- `P/runtime.md:153`, RT-RTE-conversation-save, correctly says “tool-call/result parts opt in.”
- The same record at line 158 says admission includes “the default exclusion of tool payloads,” without the generic-content qualification.
- `P/synthesis.md`, “From conversation to retained material,” says saving excludes “by default, tool calls/results.” Its “What the progression establishes” paragraph broadens this to “Optional tool payload capture adds tool traces only when enabled.”
- Report verification speaks of normally omitted tool parts and finds no blocker; synthesis verification endorses optional tool payloads and records no additional limit. Neither supplies the missing boundary condition. The overview is navigation and deterministic-check disclosure, not a substantive repair.

`S/packages/tools/src/vercel/util.ts:27–30` aliases call options to external `LanguageModelV2CallOptions`; nearby compatibility code also supports later provider shapes. This audit does **not** establish ordinary typed tool-role string input reachability, dependency behavior or an exploitable path. Conversely, an alias is not an inspected runtime rejection of that input. Deciding the external input contract would require further work. The cheap sufficient resolution is an explicit source-visible qualification, not an assertion that all such content is reachable.

## Historical comparison boundaries

Read these historical reports completely as leads:

- [Batch-19 audit](./batches-19-20/AAS-2026-10-15-supermemory-ae21530d128d-01.md).
- [Original exact-publication audit](./next-publications/AAS-2026-10-15-supermemory-ae21530d128d-01.md).
- [Verifier-only reentry audit](./next-publications/AAS-2026-10-15-supermemory-ae21530d128d-01-reentry.md).

Those concern run `AAS-2026-10-15-supermemory-ae21530d128d-01`, source revision `5323f427d076c7a158a9154867d293b53acc3841` and method `a568c6dc489ad546374536b642c3889ce23149a8`. They describe earlier broad June and wrapper-only September reviews; those reviews and historical source checkouts were not independently reread here. No revision equivalence, old byte preservation or inherited operational finding is asserted for this fresh run.

The fresh synthesis still preserves the major meaning identified in those leads: public integration versus private engine; document/chunk/fact/profile distinction; unawaited and flush-dependent saving; namespace profile/search; context supply versus actual model reliance; unresolved cache/withdrawal propagation; and no observed operation or causal benefit. Guided MCP editing remains optional, with direct writes separately available. Review is now described as a documented post-formation opportunity, not universal pre-use acceptance. Exact file and voice consumers are distinguished from Vercel retrieval. Broader adapter, upload, connector/SMFS and application coverage remains explicitly incomplete. Thus historical inventory reduction is visible as a limit, not proof that those mechanisms disappeared.

The fresh report verifier also identifies a conditional Claude view example and an omitted documented feedback-conditioned review recipe; the synthesis carries both consequences. It carries the profile verifier's combined-unit comparison limit as well. These are useful public qualifications, but do not qualify serializer filtering. No additional consequential regression was established in this bounded comparison; this is not an exhaustive older-account reconciliation.

## Selected operational evidence

Parsed settled `tool_execution_end` records in T, not repeated streaming snapshots. For selected workers, matched assistant tool-call IDs to same-worker `toolResult.toolCallId`. Locators are 1-indexed JSONL lines, then `result.details.results[0].messages`; call prefixes below are unique within the worker.

- **T:1162, runtime 000005**, model `gpt-6.1-sol`, exit 0: `call_8RMtbsZpGKMSM06jaJaZq8tf` successfully reads middleware lines 1–400, actually returning the generic-string and gated structured branches. `call_HlPivkGcMsMlxqYyNnqX8xpp` successfully writes the runtime report. `call_WCDUGaI2MuwwxSYd8xkHO9kD` returns the member-content check pass; after a quotation-context edit, `call_y5b59Gbq5IYIJThqaNBAFimH` returns the same pass. The result explicitly says invocation residue is not checked and this is not claim support.
- **T:2792, report verifier 000022**, model `gpt-6.1-sol`, exit 0: `call_bnjoOgU3C5CrFaxhbNqmbZ4I` successfully reads complete middleware, including the generic branch. `call_csoWJnK4wtS1cPFQyscqeeHd` successfully writes the no-blocker verification. `call_jXFn4G8bHLWnDzQj9zFq4qDc` returns the same limited content-check pass.

The affected source was actually available to author and verifier; citations alone were not used to infer access. These checks establish selected actions and a missed semantic qualification, not their cognitive cause. All 33 stored attempt records report state `completed`; this is sequence evidence, not certification of every performed obligation or judgment. No new consequential operational violation was established in this sample. Complete instruction delivery, source isolation, no-feedback conduct, all writes and every worker's compliance were not audited and are not certified by publication success.

## Coverage and stopping limits

Direct source inspection was limited to serializer branches and the call-option alias/compatibility context. The other public mechanisms were checked for qualification and historical carriage, not independently re-proven. Detailed runtime/memory inspection was selective; epistemic, workflow, reconciliation and profile claims were not exhaustively reconstructed. The private engine, external provider contracts, actual operations, all adapters, historical revisions and dependency reachability remain unverified.

This stops with a bounded hold rather than acquiring dependencies or reanalysing the system. No delegation, target execution, acquisition, analysis/source/state edit, run advance/reset, integration, commit or cleanup occurred. Unrelated origin dirt was not changed or adjudicated. Broader graph discovery is outside this audit; if separately commissioned, `cp-skill-connect` is the corresponding next procedure, not a prerequisite for this disposition.

## Validation and final preservation check

From W, using the verified prepared environment:

```text
.venv/bin/commonplace-validate --full kb/agentic-system-analyses/retained/supermemoryai--supermemory
```

Exit 0. `Overall: PASS (clean)`; WARN, FAIL and INFO all `(none)`; twelve Markdown members and directory roles/relations pass. Files analysed 1, failing notes 0. No unavailable-source notice. Deterministic success does not resolve the semantic hold.

Also ran from W:

```text
.venv/bin/commonplace-validate --full /home/zby/llm/commonplace/kb/work/agentic-system-reruns/audits/batch-21-supermemory-75d21b14316b.md
```

Exit 0; type `text`; base text check passes with no structural requirements. `Overall: PASS (clean)`; WARN, FAIL and INFO all `(none)`. This checks report admissibility, not the audit judgment.

After inspection and validation, recursively rehashed all 13 P files. Their complete name/hash map still equals the frozen publication effect above, with identical map digest `e53f36c7a16e31bed03dfacba6b593f173dfe65861632df8793ec387b8918a3d`; the effect's own SHA-256 is unchanged. No publication member changed during this audit.
