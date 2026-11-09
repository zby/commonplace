---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "sqz epistemic routes: preservation checks, recovery, session claims and the limits of fixture warrant."
run-id: AAS-2026-11-09-sqz-154fb86209ba-01
reviewed-boundary: "495c078d8f4c94d060ecfbb4d919286670b87898"
---

# sqz epistemic report

## Source-and-claim boundary

The question is whether sqz's context transformations and retained state justify reliance on the content supplied to an agent. Scope, exclusions and source identity are see [boundary](boundary.md#boundary-and-evidence); source identity and evidence layers are see [Source register](boundary.md#source-register). SRC-1 at the frozen commit supplies implementation, doctrine/design and reported operation. No model execution, target execution or causal experiment is supplied. Source HEAD was checked against the pin; no target was executed.

sqz acquires caller/file/tool/session text and changes its presentation. A preservation evaluator concerns the relation between input and output, not the truth of the input's assertions. A session field named “learning,” a correction formatted as a decision, and a wrapper named “session_knowledge” do not themselves establish acceptance. These distinctions matter because the later consumer may see selected text without its omitted context.

Public warrant claims considered are [RT-CLM-recoverable-results](runtime.md#rt-clm-recoverable-results) and [EPI-CLM-fact-recall](#epi-clm-fact-recall). This is not a survey of every translated or historical claim. The overlay uses supplied runtime records where they already own a referent; new records below distinguish check results from their disposition and add the import/resume and fixture-evaluation paths.

| Entry point or operation | SRC-1 source path | Coverage and basis | Limit and conclusion prevented |
|---|---|---|---|
| CLI compress and hook delivery | `sqz/src/main.rs`, `sqz/src/cli_proxy.rs` | Dispatch directly inspected; detailed forcing branches supplied by [RT-RTE-cli-compress](runtime.md#rt-rte-cli-compress) | Formatter and final abbreviation are not covered by engine verification; no universal semantic guarantee |
| Native compression and verifier | `sqz_engine/src/engine.rs`, `sqz_engine/src/verifier.rs` | Direct main compress and verifier inspection; [EPI-RTE-preservation-check](#epi-rte-preservation-check), [EPI-RTE-fallback-select](#epi-rte-fallback-select) | Token scanner helpers beyond the main check are not re-audited; no exhaustive preservation or input-truth conclusion |
| MCP advertised/exposed tools | `sqz-mcp/src/lib.rs` | Dispatch, default compression and recall directly inspected; file/grep/list/expand detailed behavior supplied by [RT-RTE-file-read](runtime.md#rt-rte-file-read), [RT-RTE-cache-recovery](runtime.md#rt-rte-cache-recovery) | Unknown IDs default to compression, not a new evaluator; no executed filesystem search |
| MCP proxy / lazy help | `sqz-mcp/src/proxy.rs` | Supplied [RT-RTE-mcp-proxy](runtime.md#rt-rte-mcp-proxy) | Recovery/help delivery is not endorsement or sandboxing |
| Cache, freshness, pin, compact/reset | `sqz_engine/src/cache_manager.rs`, `sqz/src/main.rs` | Supplied [RT-RTE-cache-recovery](runtime.md#rt-rte-cache-recovery) and runtime account; expand regret logging searched directly | Detailed cleanup/reset/pin effects beyond supplied account unassessed here; prevents complete withdrawal/expiry verdict |
| Import/export and resume | `sqz_engine/src/engine.rs`, `sqz_engine/src/ctx_format.rs`, `sqz/src/main.rs`, `sqz_engine/src/session_continuity.rs` | Direct reads: [EPI-RTE-ctx-import](#epi-rte-ctx-import), [EPI-RTE-resume-guide](#epi-rte-resume-guide) | No supplied populated session; ordinary compression-to-session producer remains unresolved |
| HTTP request/history shaping | `sqz_engine/src/api_proxy.rs` | Direct summary and content-block inspection; [RT-RTE-request-transform](runtime.md#rt-rte-request-transform) | Returned body must be adopted externally; no task-quality test |
| Browser and IDE alternatives | `sqz-wasm/src/lib.rs`, `extension/content/common.js`, `vscode-extension/src/sqzBridge.ts`, `jetbrains-plugin/src/main/kotlin/com/sqz/SqzBridge.kt` | Supplied [RT-RTE-browser-compress](runtime.md#rt-rte-browser-compress) and runtime account | Native verification cannot be inherited; no bundle/site equivalence assessment |
| Installed guidance, hooks and preset reload | `sqz_engine/src/tool_hooks.rs`, `sqz_engine/src/codex_integration.rs`, `sqz_engine/src/engine.rs` | Supplied [RT-RTE-integration-install](runtime.md#rt-rte-integration-install), [RT-RTE-preset-reload](runtime.md#rt-rte-preset-reload) | Actual external host enforcement and agent compliance unobserved |
| Quality regression test and claimed results | `sqz/tests/quality_bench.rs`, `docs/quality-benchmark.md`, `README.md` | Direct measurement/gate code and documentation inspection; [EPI-RTE-fixture-check](#epi-rte-fixture-check), [EPI-RTE-regression-gate](#epi-rte-regression-gate) | Reported table is not independently observed execution; no component attribution |
| Analyze, tee, discover/replay, dashboards, statistics and other exposed helpers | `sqz/src/main.rs` | Dispatch inspected, detailed implementations uninspected in this member | No complete negative on all derived metrics, feedback/adaptation or exposed evaluators |
| Model routing / tool selection | `sqz_engine/src/model_router.rs`, `sqz_engine/src/tool_selector.rs` | Supplied runtime account | Symbolic arithmetic/sparse scores do not establish learned parameters; external model internals remain uninspected |

Available but uninspected helpers, custom pipeline configurations, site adapters and maintenance internals are not inaccessible or absent. They preclude a system-complete negative about knowledge production, revision or adaptation. The selected routes below are enough to distinguish implemented preservation/recovery from the stronger claim that compressed context warrants a successful task answer.

## Epistemic-object inventory

Object fields owned elsewhere say see their records. Local labels below are content families, not additional declarations.

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-context-text](#epi-obj-context-text) | Imported source assertions; compressed text may omit their conditions | Context supplied to agent | SRC-1, `sqz-mcp/src/lib.rs`; see record | Source assertions are not authenticated |
| [EPI-OBJ-verify-result](#epi-obj-verify-result) | Claims that sampled syntactic features survive | Preservation diagnostic | SRC-1, `sqz_engine/src/verifier.rs`; see record | Not a probability that the content is true |
| [EPI-OBJ-session-state](#epi-obj-session-state) | Summary, turns, learning key/value and correction pairs | Resumable session material | SRC-1, `sqz_engine/src/ctx_format.rs`; see record | Labels do not prove acquisition, criticism or acceptance history |
| [EPI-OBJ-fixture-outcome](#epi-obj-fixture-outcome) | Counts, missing fact strings, equality/recovery outcomes | Regression evidence | SRC-1, `sqz/tests/quality_bench.rs`; see record | Construction code, not an observed outcome |
| [RT-OBJ-preset](runtime.md#rt-obj-preset) | None required; operational configuration | see [RT-OBJ-preset](runtime.md#rt-obj-preset) | SRC-1, `sqz_engine/src/engine.rs` | Parse validity is not improvement evidence |
| [RT-CMP-wasm-engine](runtime.md#rt-cmp-wasm-engine) | Imported/editor text on this alternative | see [RT-CMP-wasm-engine](runtime.md#rt-cmp-wasm-engine) | SRC-1, `sqz-wasm/src/lib.rs` | Native checks do not cover it |
| [RT-BAP-host-guidance](runtime.md#rt-bap-host-guidance) | Protocol instructions plus product assertions | see [RT-BAP-host-guidance](runtime.md#rt-bap-host-guidance) | SRC-1, `sqz_engine/src/codex_integration.rs` | Natural-language requests do not enforce model behavior |

## Authority-route ledger

Each entry is an independent function. Shared-record fields are see the cited declaration; architectural status and the epistemic interpretation are local assessments. “Implemented” means supported wiring, never observed activation.

Route ID: [RT-RTE-file-read](runtime.md#rt-rte-file-read)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-context-text](#epi-obj-context-text)
Content/update relation: truth-apt transformation: acquisition/import
Transition or check target: Filesystem bytes to decoded, ranged, capped body.
Evaluator/condition and domain: File/range controls, then lossless cache presentation; domain is selected text.
Activation and timing: Host tool request; before tool response; operation unobserved.
Possible or observed result: Body, ref or delta; see record.
Implemented force: enforcing representation selection.
Epistemic authority and scope: Source warrant unknown; decode/cap can degrade context, not validate assertions.
Operational authority: Deliver chosen body.
Behavioral-authority path: MCP host, JSON tool result, enforcing representation choice, current response/recovery horizon.
Evidence source ID and local anchor: SRC-1, `sqz-mcp/src/lib.rs`; see [RT-RTE-file-read](runtime.md#rt-rte-file-read).
Claim IDs: none.
Mismatch marker: none.
Gap/limit: Whole-file fidelity is narrower than the label.

Route ID: [RT-RTE-engine-compress](runtime.md#rt-rte-engine-compress)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-context-text](#epi-obj-context-text)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: Candidate context representation.
Evaluator/condition and domain: Configured symbolic pipeline; content-dependent omissions.
Activation and timing: Native engine call before verification; operation unobserved.
Possible or observed result: Candidate then possible fallback; see record.
Implemented force: enforcing transform.
Epistemic authority and scope: No general entailment or semantic-preservation proof; individual copies/reformats are non-ampliative.
Operational authority: Change model-facing representation.
Behavioral-authority path: Caller, returned text, enforcing output choice, current call.
Evidence source ID and local anchor: SRC-1, `sqz_engine/src/engine.rs`; see [RT-RTE-engine-compress](runtime.md#rt-rte-engine-compress).
Claim IDs: none.
Mismatch marker: none.
Gap/limit: Remaining alternatives are non-ampliative reshaping, entailed metadata and meaning-changing content; need per-input/output semantics.

Route ID: [EPI-RTE-preservation-check](#epi-rte-preservation-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-verify-result](#epi-obj-verify-result)
Content/update relation: no content change
Transition or check target: Candidate versus original preservation.
Evaluator/condition and domain: Verifier substring/ratio checks; not real-world truth.
Activation and timing: After native candidate, before fallback decision; operation unobserved.
Possible or observed result: Pass/fail details, confidence, fallback flag.
Implemented force: diagnostic consumed by selection.
Epistemic authority and scope: Only named syntactic tests, with thresholds and sampling.
Operational authority: Supply fallback input, not final approval.
Behavioral-authority path: Engine, VerifyResult, advisory until consumer acts, current call.
Evidence source ID and local anchor: SRC-1, `sqz_engine/src/verifier.rs`; see [EPI-RTE-preservation-check](#epi-rte-preservation-check).
Claim IDs: none.
Mismatch marker: none.
Gap/limit: Passed check does not license all facts or successful model use.

Route ID: [EPI-RTE-fallback-select](#epi-rte-fallback-select)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-context-text](#epi-obj-context-text)
Content/update relation: no content change
Transition or check target: Choose candidate versus recomputation.
Evaluator/condition and domain: Code tests fallback flag and changed text.
Activation and timing: Immediately after check; operation unobserved.
Possible or observed result: Safe recomputation or ordinary candidate returned.
Implemented force: enforcing branch.
Epistemic authority and scope: Operational admission for context delivery, not evidence-consuming truth acceptance.
Operational authority: Return alternative representation; no mandatory all-checks-pass gate.
Behavioral-authority path: Native caller, returned CompressedContent, permissive output admission, current call.
Evidence source ID and local anchor: SRC-1, `sqz_engine/src/engine.rs`; see [EPI-RTE-fallback-select](#epi-rte-fallback-select).
Claim IDs: none.
Mismatch marker: none.
Gap/limit: Checks and disposition are separate; no task-answer oracle.

Route ID: [RT-RTE-cli-compress](runtime.md#rt-rte-cli-compress)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-context-text](#epi-obj-context-text)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: Formatter and abbreviation alternative.
Evaluator/condition and domain: Command classifier, net-win and postprocessing gates; see record.
Activation and timing: Auto stdin branch and final delivery; operation unobserved.
Possible or observed result: Formatted/abbreviated body or passthrough.
Implemented force: enforcing representation choice.
Epistemic authority and scope: No engine-wide semantic license on final text.
Operational authority: Deliver stdout and possibly retain original.
Behavioral-authority path: Shell host, stdout/stderr, enforcing text choice, current call plus cache.
Evidence source ID and local anchor: SRC-1, `sqz/src/cli_proxy.rs`; see [RT-RTE-cli-compress](runtime.md#rt-rte-cli-compress).
Claim IDs: none.
Mismatch marker: none.
Gap/limit: Formatter and abbreviation can escape native verifier scope.

Route ID: [RT-RTE-cache-recovery](runtime.md#rt-rte-cache-recovery)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-context-text](#epi-obj-context-text)
Content/update relation: no content change
Transition or check target: Original and compressed representations retained.
Evaluator/condition and domain: Wrapper never-store guard; SQLite admission; see record.
Activation and timing: Cache-enabled eligible input; operation unobserved.
Possible or observed result: Stored bytes or errors.
Implemented force: enforcing storage eligibility at wrapper only.
Epistemic authority and scope: Retained is not accepted as true.
Operational authority: Make content recoverable for later calls.
Behavioral-authority path: Cache/expand consumer, SQLite bytes, permissive future availability, across calls.
Evidence source ID and local anchor: SRC-1, `sqz_engine/src/cache_manager.rs`; see [RT-RTE-cache-recovery](runtime.md#rt-rte-cache-recovery).
Claim IDs: [RT-CLM-recoverable-results](runtime.md#rt-clm-recoverable-results).
Mismatch marker: scope-limited warrant.
Gap/limit: Recovery is bounded by captured originals and storage survival.

Route ID: [RT-RTE-cache-recovery](runtime.md#rt-rte-cache-recovery)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-context-text](#epi-obj-context-text)
Content/update relation: no content change
Transition or check target: Fresh reference/delta/recovery consumption.
Evaluator/condition and domain: Hash/slice/similarity, timestamps and pin policy; see record.
Activation and timing: Later call or explicit expansion; operation unobserved.
Possible or observed result: Ref/delta/original/compressed-only/error.
Implemented force: enforcing presentation selection.
Epistemic authority and scope: Identity/freshness is not endorsement or proof of host-window residence.
Operational authority: Substitute refs or restore captured text.
Behavioral-authority path: Host via cache response, enforcing delivery, later calls.
Evidence source ID and local anchor: SRC-1, `sqz_engine/src/cache_manager.rs`; see [RT-RTE-cache-recovery](runtime.md#rt-rte-cache-recovery).
Claim IDs: [RT-CLM-recoverable-results](runtime.md#rt-clm-recoverable-results).
Mismatch marker: scope-limited warrant.
Gap/limit: Pin bypasses freshness; expiry does not refute assertions or withdraw host copies.

Route ID: [RT-RTE-request-transform](runtime.md#rt-rte-request-transform)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-context-text](#epi-obj-context-text)
Content/update relation: truth-apt transformation: non-ampliative reshaping
Transition or check target: Old message first/last-line extraction.
Evaluator/condition and domain: Age/shape/size and token saving rules; summary function directly inspected.
Activation and timing: Eligible old request message; operation unobserved.
Possible or observed result: Middle omitted; line/byte counts added separately.
Implemented force: enforcing returned-body replacement.
Epistemic authority and scope: Retained spans preserve words, not necessarily sufficient conditions; count metadata is entailed only in byte-count domain.
Operational authority: Caller may submit transformed body.
Behavioral-authority path: HTTP caller, returned JSON, permissive adoption, one request.
Evidence source ID and local anchor: SRC-1, `sqz_engine/src/api_proxy.rs`; see [RT-RTE-request-transform](runtime.md#rt-rte-request-transform).
Claim IDs: none.
Mismatch marker: none.
Gap/limit: No engine verifier on summarize_text; no claim of accepted new explanation.

Route ID: [EPI-RTE-ctx-import](#epi-rte-ctx-import)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-session-state](#epi-obj-session-state)
Content/update relation: truth-apt transformation: acquisition/import
Transition or check target: External session assertions to stored session.
Evaluator/condition and domain: Serde shape parser then save_session.
Activation and timing: Import CLI/API call; operation unobserved.
Possible or observed result: Parse failure or stored session; version mismatch warns.
Implemented force: enforcing structural admission.
Epistemic authority and scope: Source warrant unknown; no truth check in inspected admission chain.
Operational authority: Permit later session load.
Behavioral-authority path: Session store, parsed SessionState, permissive availability, later invocations.
Evidence source ID and local anchor: SRC-1, `sqz_engine/src/ctx_format.rs`; see [EPI-RTE-ctx-import](#epi-rte-ctx-import).
Claim IDs: none.
Mismatch marker: none.
Gap/limit: No lifecycle integration after epistemic acceptance established.

Route ID: [EPI-RTE-resume-guide](#epi-rte-resume-guide)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-session-state](#epi-obj-session-state)
Content/update relation: truth-apt transformation: non-ampliative reshaping
Transition or check target: Session records to selected guide.
Evaluator/condition and domain: Requested/latest session, last five turns, category priority and guide budget.
Activation and timing: Resume invocation after load; operation unobserved.
Possible or observed result: Clipped/grouped <session_knowledge> text.
Implemented force: enforcing selection; advisory at agent.
Epistemic authority and scope: No new warrant conferred by correction arrow or knowledge wrapper.
Operational authority: Print potential next-window context.
Behavioral-authority path: Human/host then agent, stdout/directive, advisory, next context if adopted.
Evidence source ID and local anchor: SRC-1, `sqz_engine/src/session_continuity.rs`; see [EPI-RTE-resume-guide](#epi-rte-resume-guide).
Claim IDs: none.
Mismatch marker: none.
Gap/limit: Late categories can be omitted; loading does not show model use.

Route ID: [EPI-RTE-fixture-check](#epi-rte-fixture-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-fixture-outcome](#epi-obj-fixture-outcome)
Content/update relation: truth-apt transformation: entailed derivation
Transition or check target: Output preservation and recovery for authored fixtures.
Evaluator/condition and domain: Substring, trim-end equality, expanded-byte equality, byte-derived token arithmetic.
Activation and timing: Test measurement after test invokes CLI; operation unobserved.
Possible or observed result: Outcome fields and table.
Implemented force: diagnostic; consumed by gate.
Epistemic authority and scope: Determinate comparisons if executions return those bytes; not truth of fixture assertions.
Operational authority: Provide regression-gate inputs.
Behavioral-authority path: Test runner, Outcome values, advisory until asserts, test invocation.
Evidence source ID and local anchor: SRC-1, `sqz/tests/quality_bench.rs`; see [EPI-RTE-fixture-check](#epi-rte-fixture-check).
Claim IDs: [EPI-CLM-fact-recall](#epi-clm-fact-recall).
Mismatch marker: scope-limited warrant.
Gap/limit: No test execution supplied; no model-answer oracle.

Route ID: [EPI-RTE-regression-gate](#epi-rte-regression-gate)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-fixture-outcome](#epi-obj-fixture-outcome)
Content/update relation: no content change
Transition or check target: Regression acceptance of fixture behavior.
Evaluator/condition and domain: Test assertions: all facts, recovery, sensitive nonstore, >=40% aggregate reduction.
Activation and timing: After outcomes are measured; operation unobserved.
Possible or observed result: Test success or panic/failure.
Implemented force: enforcing test result only.
Epistemic authority and scope: Acceptance against finite regression criteria, intended use is source regression testing; no general semantic acceptance.
Operational authority: Allow test completion, not automatically deploy or revise code.
Behavioral-authority path: Test harness, assert outcome, enforcing pass/fail, this suite invocation.
Evidence source ID and local anchor: SRC-1, `sqz/tests/quality_bench.rs`; see [EPI-RTE-regression-gate](#epi-rte-regression-gate).
Claim IDs: [EPI-CLM-fact-recall](#epi-clm-fact-recall).
Mismatch marker: scope-limited warrant.
Gap/limit: No inspected automatic code-revision or deployment consumer.

Browser proposal acceptance, preset parse admission and installed guidance are additional operational, not epistemic-acceptance, paths: see [RT-RTE-browser-compress](runtime.md#rt-rte-browser-compress), [RT-RTE-preset-reload](runtime.md#rt-rte-preset-reload), [RT-RTE-integration-install](runtime.md#rt-rte-integration-install), [RT-BAP-host-guidance](runtime.md#rt-bap-host-guidance). Their architecture is implemented per supplied records. They update editor text/configuration or request tool preferences, with no established acceptance of a novel truth-apt claim. Browser choice is not obligatorily a separate human click; submission can apply a pending candidate. MCP proxy response selection/help delivery is see [RT-RTE-mcp-proxy](runtime.md#rt-rte-mcp-proxy); it exposes recovery rather than adding a truth evaluator.

Concrete deterministic trace (implementation deduction, not target execution): in SRC-1, `sqz_engine/src/api_proxy.rs`, let text be ASCII `begin\n`, 200 copies of `x`, then `\nprivate\nend`. It has four lines and 218 bytes. `summarize_text` returns `begin\n[... 4 lines, 218 chars ...]\nend`. The eligible string-content message exceeds 200 bytes and this result has a lower bytes/4 estimate, so `summarize_message` adopts it when reached. “private” and the 200-byte line do not reach the returned body through this route. First/last-line selection is non-ampliative extraction; the new count proposition is an entailed derivation from the byte string under Rust line/length semantics. The label “chars” actually uses byte length; Unicode character-count warrant does not follow. Neither preserved endpoints nor true size metadata establishes semantic equivalence of the whole message.

A countercase to treating the verifier as semantic acceptance follows directly from its checks: an ordinary prose candidate can retain sufficient length while altering a negation without presenting any sampled error/path/JSON/diff/numeric/preservation token. The inspected check criteria do not evaluate that negation. This is a limitation of the evaluator's domain, not a claim that the configured pipeline emits that candidate. Conversely, the preservation sentinel can force fallback even when six other checks pass; it would be wrong to describe all check failures as harmless averages.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-recoverable-results](runtime.md#rt-clm-recoverable-results) | see record | SRC-1, `sqz-mcp/src/lib.rs`; doctrine/design | Explicit recoverability promise | [RT-RTE-cache-recovery](runtime.md#rt-rte-cache-recovery), [RT-RTE-file-read](runtime.md#rt-rte-file-read) | None supplied | No intervention/comparison; source capture and storage survival required | Recovery route is wired for captured originals | Universal byte-exact interpretation fails to account for compressed-only entries, caps/decoding and uncached alternatives; see record |
| [EPI-CLM-fact-recall](#epi-clm-fact-recall) | see record | SRC-1, `README.md`, `docs/quality-benchmark.md`; reported operation and doctrine/design | Explicit fixture metric and limitations | [EPI-RTE-fixture-check](#epi-rte-fixture-check), [EPI-RTE-regression-gate](#epi-rte-regression-gate) | No inspectable execution supplied here | No live model contrast; substring facts can appear in an abbreviation legend without showing correct interpretation | Finite regression design checks authored fact strings and recovery; reported success remains attributed | Does not establish arbitrary critical-fact preservation or agent task success |

## Bounded conclusion

sqz's selected routes acquire and reshape assertions rather than establish their truth. The source warrant of caller/file/tool/session text is unknown. Even a faithfully captured original does not authenticate its claims. Decoding, caps, lossy transforms and omission can degrade the context needed to rely on them; refs and deltas move the burden to a recovery protocol and external host/model interpretation ([RT-RTE-file-read](runtime.md#rt-rte-file-read), [RT-RTE-cli-compress](runtime.md#rt-rte-cli-compress), [RT-RTE-cache-recovery](runtime.md#rt-rte-cache-recovery)).

Native preservation checks have real operational force through fallback, but their scope is syntactic preservation, not source truth or full semantic equivalence. Candidate checking and output admission are distinct ([EPI-RTE-preservation-check](#epi-rte-preservation-check), [EPI-RTE-fallback-select](#epi-rte-fallback-select)). Safe recomputation is not a mandatory successful revalidation barrier. Formatter/postprocessing, HTTP summary and browser/IDE alternatives prevent transferring this gate to the whole product.

The regression suite accepts finite fixture behavior under explicit criteria for a test-use scope. It does not accept an ampliative explanation, task answer or universal preservation proposition. Counts and byte comparisons are entailed within their formal input domain, conditional on the actual execution producing the compared bytes. Reported fixture success and savings are neither independently observed here nor causal evidence of improved agent performance ([EPI-RTE-fixture-check](#epi-rte-fixture-check), [EPI-RTE-regression-gate](#epi-rte-regression-gate), [EPI-CLM-fact-recall](#epi-clm-fact-recall)).

Session import/resume is a consequential route omitted from a simple compression-only picture. Structural parse admission permits externally authored learning/correction fields to survive into a later guide without an inspected truth gate in that chain. The guide may truncate or omit content by priority. It grants potential advisory model influence, not evidence-consuming epistemic acceptance or lifecycle integration ([EPI-RTE-ctx-import](#epi-rte-ctx-import), [EPI-RTE-resume-guide](#epi-rte-resume-guide)). No populated candidate instance or provenance trace is supplied.

Preset reload and generated host guidance can change future compression or request future tool choice. This is direct policy/configuration change, not evidence of learned weights, autonomous theory revision or increased capacity. No parameter-changing component is established on the selected routes; external consumer parameters and mutable model endpoints are uninspected (see [RT-CMP-compression-pipeline](runtime.md#rt-cmp-compression-pipeline) and runtime account). Learning, reflection, autonomy, self-improvement and theory-builder properties remain separate questions: these preservation, storage and guide labels do not prove them. Uninspected exposed metric/helper paths prevent a system-complete absence claim. No accepted ampliative claim or post-acceptance lifecycle integration is established by the selected evidence; that is a bounded finding, not an unqualified verdict on every shipped API.

## Shared records

### Components

none declared in this member

### Operative objects

#### EPI-OBJ-context-text
Label: Context text

Distinct content referent: input assertions and their selected/encoded delivery bodies, not the executable [RT-CMP-compression-pipeline](runtime.md#rt-cmp-compression-pipeline) or configuration [RT-OBJ-preset](runtime.md#rt-obj-preset). Native originals/cache bytes and current response strings are substrates; natural-language assertions are interpreted by the external agent, while ref/hash tokens have symbolic cache consumer rules. Parts differ by path as the ledger records. Source warrant is unknown; not every input is truth-apt. SRC-1, `sqz-mcp/src/lib.rs`; acquisition and preparation evidence is also see [RT-RTE-file-read](runtime.md#rt-rte-file-read).

> Some(text) => text.to_string(),
> None => serde_json::to_string(&request.input)
> --- `sqz-mcp/src/lib.rs`

#### EPI-OBJ-verify-result
Label: VerifyResult

Symbolic current-call struct containing Boolean pass, numeric ratio, check names/failures and fallback flag, produced in memory. It is a material result part of the engine route, not the pipeline component or preset. Closest supplied route is [RT-RTE-engine-compress](runtime.md#rt-rte-engine-compress); this object distinguishes diagnostic from selection. SRC-1, `sqz_engine/src/verifier.rs`.

> VerifyResult {
>             passed: failed.is_empty(),
>             confidence,
>             checks_passed: passed,
>             checks_failed: failed,
>             fallback_triggered,
>         }
> --- `sqz_engine/src/verifier.rs`

#### EPI-OBJ-session-state
Label: SessionState

Symbolic structured fields in a CTX JSON envelope and persistent session store contain natural-language conversation, summary, learning key/value and correction strings. Runtime mentions the session-resume container but declares no object counterpart. This is not the cache-original representation: sessions have their own import/load/guide consumers. SRC-1, `sqz_engine/src/ctx_format.rs`, `sqz/src/main.rs`.

> pub session: SessionState,
> --- `sqz_engine/src/ctx_format.rs`

> format!("{} → {}", correction.original, correction.correction),
> --- `sqz/src/main.rs`

#### EPI-OBJ-fixture-outcome
Label: Outcome

Symbolic test-process struct carries expected-fact membership counts, missing strings, recovery enum and token statistics. Its original/reference facts are authored fixture strings, not an independently answered agent task. Distinct from [RT-OBJ-preset](runtime.md#rt-obj-preset): evaluation output, not active product configuration. No supplied object counterpart. SRC-1, `sqz/tests/quality_bench.rs`.

> let missing: Vec<&'static str> = fx.facts.iter().copied().filter(|f| !out.contains(f)).collect();
> --- `sqz/tests/quality_bench.rs`

### Routes

#### EPI-RTE-preservation-check
Label: Preservation check

Part of: [RT-RTE-engine-compress](runtime.md#rt-rte-engine-compress)

Verifier owns the original/candidate comparison and constructs [EPI-OBJ-verify-result](#epi-obj-verify-result). The domain is retained input substrings and size/features, not the truth of source assertions. JSON permits at least half the top-level keys as substrings; numbers sample the first ten eligible values; path-line checks take twenty; preservation tokens require 85%. The original is a comparison reference, not an expected agent-task answer oracle. No human or model decides this check. Open text transformation, not an improvement curriculum.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: VerifyResult returned to engine.
- Later read-back: inapplicable — diagnostic is current-call state, with no inspected durable result reader.
- Delegated visibility: inapplicable — no model delegate.
- Selection predicate: Every non-risk-safe engine candidate reaches verify; check branches depend on input shape.
- Invalidation or expiry: inapplicable — recomputed for each candidate.
- Activation or effect: Supplies a fallback flag; the consumer, not the check alone, chooses output.
- Evidence limits: No target execution; substring thresholds do not evaluate semantic equivalence.

SRC-1, `sqz_engine/src/verifier.rs`, implementation.

> if retention_ratio >= 0.5 {
>                         passed.push("json_keys".to_string());
>                     }
> --- `sqz_engine/src/verifier.rs`

> if ratio >= 0.85 {
>                 passed.push("preservation".to_string());
>             }
> --- `sqz_engine/src/verifier.rs`


#### EPI-RTE-fallback-select
Label: Fallback selection

Part of: [RT-RTE-engine-compress](runtime.md#rt-rte-engine-compress)

Engine owns disposition after the check. This is a distinct material function within [RT-RTE-engine-compress](runtime.md#rt-rte-engine-compress), not a replacement of that valid container. Software proposes the pipeline candidate, tests the flag and can replace it with safe recomputation. The caller supplies input but has no per-candidate veto inside this function. Criterion: confidence below 0.6 and changed candidate; intended use: choose context output in this call. This grants operational permission to return text, not acceptance of its truth. Parse/pipeline errors remain errors; there is no versioned rollback or iterative content criticism. No task-answer oracle. Guidance is the configured preset; fallback changes this call, not a learned persistent policy.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Candidate or safe recomputation returned as CompressedContent.
- Later read-back: inapplicable — no persistence inside plain compress; cache callers are separate.
- Delegated visibility: inapplicable — no delegate.
- Selection predicate: fallback flag and result.data != input.
- Invalidation or expiry: inapplicable — disposition lasts for this invocation.
- Activation or effect: Replaces ordinary candidate when condition holds; otherwise permits return.
- Evidence limits: Supplied runtime and direct code show no mandatory successful verification barrier after recomputation.

SRC-1, `sqz_engine/src/engine.rs`, implementation.

> if fallback && result.data != input {
> --- `sqz_engine/src/engine.rs`

> let safe_result = self.compress_safe(input, &pipeline, &ctx, false)?;
>             return Ok(safe_result);
> --- `sqz_engine/src/engine.rs`


#### EPI-RTE-ctx-import
Label: CTX import

CLI/API caller supplies a CTX string; CtxFormat deserializes and the engine saves the resulting session. This retains [EPI-OBJ-session-state](#epi-obj-session-state), not cache entries. Closest supplied [RT-RTE-cache-recovery](runtime.md#rt-rte-cache-recovery) has different endpoints/state; runtime mentions but does not declare this session route. Admission owner is parser/save code. Caller authorship (human versus software) is unresolved; invoking import is not per-proposition human approval. Criterion is typed JSON acceptance, intended use is session storage. Invalid JSON can be rejected; a version mismatch only warns. No source-truth evaluator, task-answer oracle, autonomous candidate search or quality-based rollback is established in this chain. Export serializes a loaded session, not an epistemic certification.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Session ID or parse/store error.
- Later read-back: Stored session can be loaded by resume across invocations.
- Delegated visibility: inapplicable — import creates no model worker.
- Selection predicate: Caller-supplied CTX, successful serde decoding, successful save.
- Invalidation or expiry: uninspected — detailed session overwrite/deletion policy is not inspected here.
- Activation or effect: Admits typed caller assertions for possible later guide construction.
- Evidence limits: Import is inspected through the facade/parser; persistence behavior beyond the save boundary and actual sessions are not observed.

SRC-1, `sqz_engine/src/engine.rs`, implementation.

> let session = CtxFormat::deserialize(ctx)?;
>         self.session_store.save_session(&session)
> --- `sqz_engine/src/engine.rs`


#### EPI-RTE-resume-guide
Label: Resume guide

CLI selects an explicit/latest stored session, loads it, creates a Snapshot from summary, last five turns, learnings and corrections, then prints generate_guide output. Guide builder groups categories in fixed priority order and applies a body budget, potentially truncating a category and stopping before later ones. This is a distinct session consumption route, not cache hash expansion ([RT-RTE-cache-recovery](runtime.md#rt-rte-cache-recovery)). Code selects and can omit content; a human/host may adopt stdout as context. No model call, answer oracle or per-content truth disposition occurs here. The learning/correction labels supply asserted guidance rather than a demonstrated theory criticism and revision loop.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Capped session_knowledge guide on stdout or load error.
- Later read-back: uninspected — an external caller may use the printed guide in a later model invocation; no automatic host injection is shown by cmd_resume.
- Delegated visibility: inapplicable — no sqz model worker is created.
- Selection predicate: Requested/latest session; last five turns clipped at 200 bytes; fixed category priority and guide budget.
- Invalidation or expiry: inapplicable — stdout guide is current output; later session edits can change future guides.
- Activation or effect: Potentially gives retained session assertions advisory authority at a later external agent; actual use unobserved.
- Evidence limits: No populated session or consumer trace; imported provenance and model compliance are unresolved.

SRC-1, `sqz_engine/src/session_continuity.rs`, implementation.

> format!("<session_knowledge>\n{body}</session_knowledge>\n")
> --- `sqz_engine/src/session_continuity.rs`

> if body.len() + line.len() > body_budget {
> --- `sqz_engine/src/session_continuity.rs`


#### EPI-RTE-fixture-check
Label: Fixture checks

Test measure function feeds authored input through the real CLI, compares selected expected strings, optional trim-end verbatim output and expanded bytes, and builds [EPI-OBJ-fixture-outcome](#epi-obj-fixture-outcome). The evaluator is test code against fixture-provided references, not model judgment. The expected answer oracle exists only for this finite benchmark: authored fact strings and original bytes, not agent-task answers. Distinct from production [RT-RTE-engine-compress](runtime.md#rt-rte-engine-compress): it reaches CLI formatters/cache and tests their externally returned output. Operating mode is a bounded regression suite; humans maintain fixtures and code, not an inspected automatic proposal/revision loop.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Outcome values returned to quality_gates and printed in a table.
- Later read-back: inapplicable — no inspected product read-back of these test Outcome values.
- Delegated visibility: inapplicable — child process is CLI computation, not delegated model context.
- Selection predicate: Authored fixture set; fixed checks on emitted stdout and expand bytes.
- Invalidation or expiry: inapplicable — test-process outcomes end with the invocation; source fixtures persist unchanged.
- Activation or effect: Produces evidence consumed by assertions, conditional on execution.
- Evidence limits: Only source inspected; no new benchmark run or independent execution artifact. Substrings do not test relationships among facts or their interpretation.

SRC-1, `sqz/tests/quality_bench.rs`, implementation.

> if expanded.stdout == fx.input.as_bytes() {
>                 Recovery::Exact
>             } else {
>                 Recovery::Mismatch
>             }
> --- `sqz/tests/quality_bench.rs`


#### EPI-RTE-regression-gate
Label: Regression gates

quality_gates consumes fixture outcomes and determines test success/failure. This is disposition separate from [EPI-RTE-fixture-check](#epi-rte-fixture-check). Test authors propose references/thresholds; assertion code decides and can veto suite completion. Criterion and intended scope: preserve all enumerated fact strings, required trim-end equality, exact recovery or sensitive nonstorage, and at least 40% aggregate reduction on selected fixtures for source regression testing. A failed assertion stops the test; no inspected automatic repair, rollback, deployment or quality-based product update follows. Humans can edit source externally; this route does not establish that they did. No agent-task oracle or model-guided improvement mode.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Test completes or panics/fails.
- Later read-back: inapplicable — no production consumer of accepted test status inspected.
- Delegated visibility: inapplicable — no model delegate.
- Selection predicate: Test invocation after measure produces all rows.
- Invalidation or expiry: inapplicable — result concerns this test invocation and fixture revision.
- Activation or effect: Enforces test pass/fail, not deployment or runtime content acceptance.
- Evidence limits: No observed test result, CI consumer audit or causal attribution; test success would remain bounded to the fixtures.

SRC-1, `sqz/tests/quality_bench.rs`, implementation.

> assert!(r.missing.is_empty(), "[{}] lost critical facts: {:?}", r.name, r.missing);
> --- `sqz/tests/quality_bench.rs`

> assert!(reduction >= 40.0, "aggregate reduction on compressible fixtures fell to {reduction:.1}%");
> --- `sqz/tests/quality_bench.rs`

### Claims

#### EPI-CLM-fact-recall
Label: Benchmark critical-fact recall

Claim conclusion status: claimed

SRC-1, `README.md`, reports complete critical-fact recall in its benchmark. This differs from [RT-CLM-recoverable-results](runtime.md#rt-clm-recoverable-results): preserving enumerated visible strings is not recovering original bytes. SRC-1, `docs/quality-benchmark.md`, explicitly excludes live agent task success and treats fact recall as a proxy. Claimed measurements remain reported operation, not independently inspected execution. [EPI-RTE-fixture-check](#epi-rte-fixture-check) and [EPI-RTE-regression-gate](#epi-rte-regression-gate) establish the evaluation design and narrow intended use.

> **100%** of agent-critical facts kept in the [quality benchmark](docs/quality-benchmark.md) ·
> --- `README.md`

> Fact recall is the proxy used here because it is deterministic and cheap enough to run on every commit.
> --- `docs/quality-benchmark.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member
