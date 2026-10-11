# Graphiti analysis and trace audit

## Identity and status

Retained on 2026-10-11 from the audit in the commissioning conversation. The
operator requested correctness review, session-trace inspection, comparison
with other Graphiti analyses, and retention here. This is a consolidated working
copy of returned audit findings, not a new analysis or a verbatim transcript.
Severity and improvement candidates are audit judgments, not adopted decisions.

```yaml
run-id: AAS-2026-10-10-graphiti-5833fd846841-01
method-commit: 6ff7c828e94dd66abdf5af00c89db6420bc6a1ad
source-revision: 964bb11d1e7020e3cc67fab244268b0736b6c219
worker-profile: pi-sol
audit-date: 2026-10-11
```

Original harness: Pi. Analytical workers used `openai/gpt-6.1-sol`, medium effort.
Local worktree: `/home/zby/llm/commonplace/.commonplace/worktrees/graphiti-5833fd846841`.
Local session trace:
`/home/zby/.pi/agent/sessions/--home-zby-llm-commonplace--/2026-10-10T22-06-52-156Z_01a127da-c8fb-70fc-aae4-d7e968a723ad.jsonl`.
Original worker traces are embedded in subagent tool-result
`details.results[].messages` arrays, not separate worker session files.

Path abbreviations below are relative to that worktree:

- `A/`: `kb/agentic-system-analyses/retained/graphiti/`.
- `S/`: `related-systems/getzep--graphiti/`.
- `R/`: `kb/agentic-system-analyses/state/AAS-2026-10-10-graphiti-5833fd846841-01/`.

Worktree and session paths are local evidence locators. They are not durable run
identities or permission to remove the evidence. Preserve them pending separate
extraction or disposition.

## Outcome and limits

The principal architectural account survived: caller admission, model-assisted
transformation, retained graph state, and later model consumption are wired.
The analysis correctly withholds certified truth, lossless retention, and
observed improvement. However, three high-impact retention/cleanup countercases
were omitted, and several narrower claims need correction or scope limits.

Three parallel reviewers covered runtime/memory correctness, epistemic/profile
correctness plus publication integrity, and comparison with other Graphiti
analyses. A fourth reviewed all original analytical worker traces and the
coordinator. The coordinator spot-checked principal source findings and resolved
one disagreement between auditors about a citation typo.

All target findings are static deductions. No Graphiti code, services, tests,
examples, benchmarks, or model calls were executed. Backend-wide behavior,
actual race occurrence, extraction accuracy, host instruction presentation and
compliance, and retrieval benefit remain unverified. The audit did not replay
the validator or exhaustively inspect every provider, backend, or quotation.

No frozen analysis, method, source, run state, or integration was changed. The
original recommendation was to correct detailed retention and cleanup claims
before integration or downstream reuse. This report does not authorize that
correction or a new run.

## Correctness findings

### G1 — High: Named-saga ingestion can erase a summary and its checkpoints

`S/graphiti_core/graphiti.py:516–533` loads an existing saga by name with identity
and episode pointers but without its summary or summary checkpoints. The
returned `SagaNode` defaults those fields to empty/null
(`S/graphiti_core/nodes.py:907–916`). Ingestion later saves the object
(`S/graphiti_core/graphiti.py:1087–1091`; bulk at `1821–1826`). Save passes the
missing fields' defaults, and the fallback Neo4j query replaces properties
(`S/graphiti_core/nodes.py:929–940`;
`S/graphiti_core/models/nodes/node_db_queries.py:368–373`).

The named-saga ingest → summarize cycle can therefore discard a previous summary
and restart incremental selection. `A/memory.md`'s saga recurrence account and
`A/synthesis.md:28` omit this qualification. Direct repeated summarization
without intervening named-saga ingestion remains supported. Behavior through
custom graph-operation implementations was not exhaustively audited.

### G2 — High: Bulk ingestion ignores disabled raw-content retention

Single processing clears content when storage is disabled
(`S/graphiti_core/graphiti.py:1031–1033`). Bulk bypasses that helper, constructs
new episodes with content, writes them early, and writes them again without
clearing content (`1672–1702,1765–1773`). Persistence serializes episode objects
(`S/graphiti_core/utils/bulk_utils.py:160–163`); the Neo4j query stores content
(`S/graphiti_core/models/nodes/node_db_queries.py:103–108`).

`store_raw_episode_content=False` therefore does not suppress raw retention for
successful bulk ingestion. `A/memory.md:35,51` and `A/synthesis.md:24` need an
explicit single-path scope. The existing warning that failed bulk work can leave
early raw writes is insufficient: this countercase also reaches completion.

### G3 — High: Bulk episodes lack the fact list needed by provenance and cleanup

New episodes default `entity_edges` to an empty list
(`S/graphiti_core/nodes.py:325–328`). Single processing populates it
(`S/graphiti_core/graphiti.py:1031`), but the completed bulk write does not
(`1751–1773`). Episode-provenance retrieval and episode removal use that list to
select facts (`2009–2016,2164–2175`).

New bulk episodes can have facts stored in the graph but yield no facts through
the episode-provenance API. Removal cannot enumerate those facts for explicit
edge cleanup. Node deletion may remove incident facts, but facts between
surviving shared entities can remain. The retained withdrawal account misses
this failure before its correctly identified first-provenance deletion test.

### G4 — Medium: Shared recipe mutation permits search-budget interference

Basic search selects a module-level recipe and mutates its limit
(`S/graphiti_core/graphiti.py:1945–1948`;
`S/graphiti_core/search/search_config_recipes.py:111–133`). Search can await an
embedding before reading the limit for scope searches
(`S/graphiti_core/search/search.py:145–153,166–225`).

Concurrent requests using that recipe can overwrite each other's budgets,
including across instances. This is an omitted shared-state race, not a measured
incident. The retained queue and request-target race discussions do not cover it.

### G5 — Medium: Temporal-filter controls have additional limitations

MCP's date-bound controls generate ordinary comparisons but expose no null
predicate (`S/mcp_server/src/utils/type_config.py:139–202`;
`S/mcp_server/src/graphiti_mcp_server.py:616–626`). They cannot express the usual
open-ended validity condition combining `invalid_at IS NULL` with dated intervals.

Core Cypher construction also reuses parameter names across outer OR groups:
names contain the inner index but not the outer index
(`S/graphiti_core/search/search_filters.py:167–226`). Different dates at the same
inner position can overwrite one another. These limitations supplement the
analysis's correct warning against universally current-only retrieval.

### G6 — Medium: Server-wired MCP instructions are omitted

`A/runtime.md` foregrounds externally installed Cursor rules, and
`A/memory.md:38` describes MCP instructions as requiring external installation.
But `S/mcp_server/src/graphiti_mcp_server.py:136–181` defines
`GRAPHITI_MCP_INSTRUCTIONS` and passes them directly into the server. This text
uses the implemented `search_memory_facts` name.

Separate this wired channel from externally installed Cursor rules. The latter's
`search_facts` mismatch is real, but not common to every instruction channel.
Host delivery and agent compliance still remain unverified.

### G7 — Low: Ordinary ingestion requests ten prior episodes, not three

`A/memory.md:247` conflates the retrieval helper's default of three with the
ordinary ingestion override. `S/graphiti_core/graphiti.py:1431–1442` passes
`RELEVANT_SCHEMA_LIMIT`; `S/graphiti_core/search/search_utils.py:64` sets it to ten.
The other October 10 analysis preserves this distinction.

### G8 — Low: The verification report alleges a nonexistent citation typo

`A/report-verification.md:36` says the epistemic ledger names
`dedupe_helpers.py`. The current ledger already names `dedup_helpers.py`, as do
the declaring record and quotation (`A/epistemic.md:56`).

The trace auditor initially reported a surviving typo. The coordinator checked
both retained files and the original epistemic worker's write at trace
P25/R1/M53: it already used the correct path. The error is the verifier's
observation, not an unresolved broken citation or publication drift. This is
also an audit false positive that required adjudication.

## Supported findings and publication checks

The audit confirmed that the analysis correctly separates queue acceptance from
persistence, semantic comparison from truth certification, literal summary
append from model replacement, and stored graph state from observed benefit.

The first-support episode deletion defect is accurately retained:
`S/graphiti_core/graphiti.py:2164–2192` can delete a multiply supported fact when
its first episode is removed, contrary to the MCP promise at
`S/mcp_server/src/graphiti_mcp_server.py:733–734`. Cleanup does not reconstruct
summaries or reverse prior invalidations.

The evaluator's conflicting Boolean guidance and string-sliced message context
are accurately qualified as static defects, not measured scoring failures:
`S/graphiti_core/prompts/eval.py:42–45,136–137` and
`S/tests/evals/eval_e2e_graph_building.py:173–174` plus its string construction and
iteration. Saga truncation/checkpoint countercases and the notebook's fact-only
model projection and asynchronous dialogue ingestion are also supported.

Independent hashing by the integrity reviewer established:

- All 11 retained Markdown members match their manifest hashes, publication
  pins, stored input bytes, and working member bytes.
- The retained manifest matches pinned hash
  `0a98343d230587a4482d8758fcb24ec505596fec11d0bdec69c66dff8c9afdef`.
- `R/effects/publish.json` and its receipt agree on all 12 published files.
- All 81 stored versions hash to their filenames.
- All 68 pinned coverage claims have accepted exact-version witnesses; all 27
  assembly file criteria match current bytes.
- Preparation, opening, receipt, and HEAD agree on the recorded method commit;
  source acquisition and source HEAD agree on the recorded source revision.
  Tracked method files and source status were clean.

The working `artifact/ARTIFACT.yaml` is a type stub, not the separately assembled
publication manifest. Its difference is expected. Earlier narrower acceptances
and the rejected predecessor profile are historical records, not substituted
for current coverage. These checks establish local publication consistency,
not external authenticity, integration, or semantic certification.

## Trace findings

Trace anchors use zero-based JSONL record numbers (`P`), result indices (`R`),
and embedded-message indices (`M`). For example P25/R1/M43 identifies a message
in the second worker result at record 25. Original coordination ran from
2026-10-10 22:09:08Z through the final report at 22:50:38Z. Audit workers are
excluded from the following counts.

### GT1 — Successful repair is absent from the final failure summary

The first profile candidate was structurally accepted, then semantically refused
for treating optional cross-encoder ranking as an established automatic delivery
route. P43/R0/M52 states the missing selector-to-consumer support.
`R/state/judgments/000022-apply-profile-verification-1.json` records the refusal
of predecessor `dbc038ef…`.

The code-scheduled retry changed the assessment to `not-determinable`, removed
unsupported findings, and supplied a correction explanation (P47/R0/M56,M58).
Checks `000024` and `000026` accepted the corrected profile and verification.
This was a successful safeguard, not an outstanding blocker.

Final inspection's empty `failed-attempts` and `refusals` arrays are not a
historical failure ledger. They report execution failures and refusals currently
in force. Completed producer attempts mean workers finished, not that their
first candidates survived semantic review. Interpretation of the final JSON as
an error-free history would be misleading.

### GT2 — Successful wrappers masked five nonzero inner commands

| Attempt and trace anchor | Failure and recovery |
|---|---|
| Runtime P21/R0/M29 | Nonexistent `llm_dispatch.py`; a dependent search was skipped. M30 supplied follow-up inspection. |
| Runtime P21/R0/M78 | Validator rejected an ambiguous quotation. M79 corrected the range; M83–84 passed. |
| Memory P25/R0/M50 | No-match search stopped an `&&` chain. M51–52 ran separate searches to recover skipped coverage. |
| Epistemic P25/R1/M24 | Nonexistent `invalidate_edges.py`; the actual disposition implementation was inspected subsequently. |
| Epistemic P25/R1/M43 | Nonexistent singular `summarize_saga.py`; the probe did not establish absence. Other summary evidence was inspected. |

Status-printing wrappers ended successfully despite printed inner exit codes 1
or 2. One epistemic pipeline also omitted `pipefail`. No unresolved analytical
failure was demonstrated from these recovered commands. Envelope/tool success
alone is insufficient to establish command success.

### GT3 — Three validation failures were repaired

Boundary P17/R0/M62 and M66 rejected quotation attribution. The worker inspected
the parser, added the frozen revision, and passed at M73–74. These two commands
propagated failure correctly. The third failure was the masked runtime validator
in GT2. All three eventually passed; the repairs do not establish content truth.

### GT4 — Actual delivery truncation was recovered

Boundary P17/R0/M39 delivered only lines 114–617 of an oversized search result.
M42–43 recovered lines 1–114 from its saved output. The many bounded-source-read
continuation notices are not themselves delivery failures. The audit found no
demonstrated omitted required-input content.

### GT5 — No demonstrated authority or coordination breach

Observed writes were confined to assigned outputs, answers, identities, and
permitted scratch. The scratch profile generator and retry copy were authorized.
No original worker source execution, nested delegation, prior-analysis reads,
source edits, engine-state edits, or Git staging/commits were observed.

Workers used fresh contexts and the specified model/effort. Memory and epistemic
had disjoint outputs and both finished before advance. The coordinator launched
only scheduled handouts, read publication instructions, and did not repair
worker prose. Missing operation evidence remained explicitly unresolved.

### Coverage and recovery cost

| Analytical attempt | Trace result | Embedded messages |
|---|---|---:|
| `000003-boundary` | P17/R0 | 76 |
| `000005-runtime` | P21/R0 | 86 |
| `000007-memory` | P25/R0 | 69 |
| `000008-epistemic` | P25/R1 | 62 |
| `000014-reconciliation` | P29/R0 | 49 |
| `000017-report-verification` | P35/R0 | 95 |
| `000019-memory-profile` | P39/R0 | 56 |
| `000021-profile-verification` | P43/R0 | 57 |
| `000023-memory-profile` | P47/R0 | 65 |
| `000025-profile-verification` | P51/R0 | 67 |
| `000027-synthesis` | P55/R0 | 62 |
| `000029-synthesis-verification` | P59/R0 | 58 |

Totals: 12 analytical attempts, 802 embedded messages, 467 tool calls (378 reads,
50 Bash, 32 writes, 7 edits). An additional diagnostic launch had three messages;
it is not an analytical prompt handoff. The engine recorded 32 attempts: 12 model
and 20 code jobs. All analytical envelopes reported exit code zero, empty stderr,
and normal termination. Seven inner shell commands were nonzero across four
workers; five were masked. Eighteen validation invocations yielded 15 passes and
three failures. Historical judgments comprise 22 acceptances and one refusal.

No token/cost accounting was established by this audit. Successful review and
avoidable retries should not be combined into a single waste measure.

## Comparison with other Graphiti analyses

Local peer worktrees are under `/home/zby/llm/commonplace/.commonplace/worktrees/`.
Their paths locate evidence; the run identities and pinned revisions distinguish
outputs. The older stopped runs are not completed retained analyses.

| Run | Source revision | Method revision | Status and provenance |
|---|---|---|---|
| `AAS-2026-10-10-graphiti-5833fd846841-01` | `964bb11d1e7020e3cc67fab244268b0736b6c219` | `6ff7c828e94dd66abdf5af00c89db6420bc6a1ad` | Current completed local publication; Pi, pi-sol, medium. |
| `AAS-2026-10-10-graphiti-85a21a06d35c-01` | Same as current | Same as current | Completed local publication; same profile/settings and plan hash. |
| `AAS-2026-10-06-graphiti-370e139ea7c2-01` | `2a85bbbf27f3d0d07dd3a8bf6dc8700c5193c066` | `ec24f7b4e919185101bd2e1ed0010c44b8427cd4` | Stopped, unpublished; model parameter gpt-6.1-sol; harness/effort not established. |
| `AAS-2026-10-05-graphiti-0b7292fa4af1-01` | `4083f51812d381d7ca28b887cfa3c3db188f576d` | `b95a2bb79b17f3dea5b29ba74cb4c6225749c904` | Stopped, unpublished; harness/model/effort not established. |

Evidence: October 10 `boundary.md`, `overview.md`, `ARTIFACT.yaml`, preparation
records, and publication receipts; older `opening.json`, `run-metadata.json`,
`workflow-state/run.json`, and `run-state.md`. All 12 files of the other October
10 publication also matched its receipt. Integration was not audited.

The October 10 pair broadly agrees. Current coverage is stronger on optional
SQLite inference cache, withdrawal countercases, and checkpoint edges. The peer
is stronger on node overlay versus edge replacement/clearing, descriptive
attribute consumption, notebook MemorySaver state, and evaluator scoring details.
Neither is uniformly better; omitted topics should not be read as absent features.

The peer correctly distinguishes the ten-episode ingestion override (G7), but
misstates initial saga packing as 100,000 UTF-8 bytes. Source `graphiti.py:130–181`
uses a 100,000-character budget, then separate byte diagnostics and assembled
prompt checking. The current analysis gets that unit distinction right.

The current profile also leaves individual attributes broadly unresolved despite
known descriptive-content consumption in its own memory account. The peer
preserves this positive path separately from arbitrary payload uncertainty;
`S/graphiti_core/utils/maintenance/node_operations.py:1046–1067` supplies prior
attributes to extraction, with another summary-context use near line 1197.
The October 6 run stopped over a related omitted attribute-consumption path.
This is a coverage concern, not proof that the current publication lacks valid
engine coverage.

The October 5 run retained an unsupported positive claim that extraction is
ampliative after its reconciliation amendment; its own `verification-2.md`
identified the contradiction. Its example scope was narrower. October 5 → 6
source differences were contributor-signature data, but method and scope also
changed. October 6 → 10 includes substantial runtime and saga implementation
changes. Older 200-versus-20 episode windows and checkpoint differences are
source evolution, not worker-quality evidence.

The legacy June 4 review used source
`34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6`, with no producing method/harness
record established here. Its pull-only account overlooked the shipped LangGraph
notebook model-context path already present at that revision. This is a scope
or inspection omission, not proof of later feature introduction.

Comparable provenance in the October 10 pair is not a controlled quality
experiment. Older comparisons additionally confound source, method, and scope.

## Comparison with the existing Napkin audit

The [Napkin report](./napkin-analysis-and-trace-audit.md) concerns a distinct
system and run at the same method commit and profile. The following comparisons
are accumulating evidence, not adopted general method recommendations.

| Candidate mechanism | Graphiti evidence | Napkin evidence | Current disposition |
|---|---|---|---|
| Shell wrappers conceal failure | GT2: five masked nonzero commands, recovered | T2: masked missing-file command, recovered | Same failure mechanism observed in two runs. Existing status-preservation rule, compliance variation, and source complexity remain competing explanations. |
| Semantic review repairs a structurally valid candidate | GT1: unsupported automatic-delivery finding corrected | T1: incompatible evaluator route corrected | Successful safeguard in both runs; preserve its value and account separately for recovery cost. |
| Final success conceals recovery history | GT1 plus recovered commands | T1–T3 record recovered failures | Historical recovery deserves visibility; inspection semantics were directly checked only for Graphiti. |
| Positive consumer paths lose scope/strength distinctions | G6 and attribute comparison | N2 retained-file/current-run confusion; N3 documented delivery omitted | Related concerns, not one proven common defect. Operations and evidence-strength errors differ. Needs adjudication before pooling. |
| Numeric/scope qualifications survive verification | G2, G7 and peer saga units | N4–N6 search scope, creation condition, score denominator | Broad error category only; no common causal mechanism or error rate established. |

Multiple auditors on this run are not independent runs. The peer Graphiti
comparison was substantive but did not include a full peer trace audit. No
uninspected opportunity is counted as a success or failure.

## Improvement candidates, not adopted changes

The intended result is more reliable detail and more visible recovery without
weakening source isolation or removing successful independent review. These are
candidates for the workshop's comparison process, not an implementation backlog.

| Candidate | Evidence and expected benefit | Added cost and evidence against adoption |
|---|---|---|
| Separate retention/provenance/cleanup checks for each write path | G2–G3: avoid generalizing single-path behavior to bulk | More source inspection. Count against blanket adoption if targeted checks rarely alter consequential conclusions or duplicate existing review. |
| Follow existing-state hydration through its next save | G1: reveal unintended overwrite before a maintenance route | Additional cross-function reads. Bound to reused mutable objects; do not require exhaustive backend tracing without benefit. |
| Selectively verify overrides, units, and alternate instruction channels | G6–G7, peer saga error: improve narrow factual precision | Review cost and possible redundant reads. Compare missed errors against successful checks, not just finding counts. |
| Report historical rejection and recovery separately from unresolved failures | GT1: prevent error-free-history interpretation | More report detail. A bounded summary is preferable if complete traces would obscure the current decision. |
| Preserve command/pipeline status through logging | GT2 and Napkin T2: make existing failures visible | Existing rule already requires it. Determine whether enforcement or tooling helps before adding another instruction. |
| Use peer outputs as a post-run coverage checklist | Complementary attributes/cache/checkpoint/evaluator coverage | Extra audit effort and contamination risk if supplied to fresh analysis workers. Keep this strictly post-run and compare against cheaper targeted review. |

No general method change is adopted here. A separately authorized local
correction decision can address G1–G8 without asserting that every omission is
caused by the method. Frozen-run evidence and the session must remain intact.
