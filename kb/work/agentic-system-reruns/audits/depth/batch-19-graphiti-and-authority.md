# Batch 19 depth: Graphiti and authority

## Outcome and authority

Five candidates need report-level verification reopened to diagnose their faulty
records; GBrain's recorded journal-bypass defect needs synthesis verification.
Author rebuilding is a different depth: the four Graphiti candidates and Letta
Code require runtime and/or memory authors, not just synthesis wording. GBrain's
managed-write conditions survive in its records and are lost in synthesis.
These are historical depth recommendations, not permission to reset anything.
**All six holds and all six incumbent-transfer stops remain in force.** No
incumbent was inspected as a replacement project.

This report follows the [depth commission](../../batch-19-depth-commission.md)
and its explicit frozen-source variation of [audit-a-rerun](../../audit-a-rerun.md).
It diagnoses the assigned discrepancies, not the complete systems. No agents,
target code/tests/services, fetching, engine inspection/advance/reset/judge,
analytical-worker contact, integration, staging or commits were used. Only this
report is authored. Generic source-ingest/graph-discovery writes are excluded by
the commission; the supplied frozen implementations are the source boundary.

## Identity, byte binding and locator conventions

The immutable intake is `kb/work/agentic-system-reruns/audit-integration-intake-2026-10-15.json`.
Its freshly calculated SHA-256 is
`31fabfd2e3a3bdb7046a1e8f4a5ff7af6bea9d3ee43d8afd2529a8dd8fb3ed19`,
matching `batch-19.json`. The current `audit-integration-later-46.json` has no row
for these six IDs. Exact preparation, command prefix, run, source and publication
paths below resolve from those intake rows, not filename guesses.

`W` means `/home/zby/llm/commonplace/.commonplace/worktrees/<directory>`.
For each row, `R = W/kb/agentic-system-analyses/state/<run-id>`;
`A = W/kb/agentic-system-analyses/retained/<publication>`;
`V/<hash> = R/state/versions/<hash>`; attempts resolve as
`R/state/attempts/<attempt>.json`. `S` is `W/related-systems/<source directory>`.
The prepared command prefix is always that row's `W/.venv/bin`; no prepared
analysis command was executed. Every row's source HEAD matches the revision below.

| Run ID | W directory / publication | Method revision | Source identity, directory and revision |
|---|---|---|---|
| `AAS-2026-10-10-graphiti-5833fd846841-01` | `graphiti-5833fd846841` / `graphiti` | `6ff7c828e94dd66abdf5af00c89db6420bc6a1ad` | `https://github.com/getzep/graphiti`; `getzep--graphiti`; `964bb11d1e7020e3cc67fab244268b0736b6c219` |
| `AAS-2026-10-10-graphiti-85a21a06d35c-01` | `graphiti-85a21a06d35c` / `graphiti` | `6ff7c828e94dd66abdf5af00c89db6420bc6a1ad` | Same Graphiti identity and revision |
| `AAS-2026-10-11-graphiti-4896fccada9e-01` | `graphiti-4896fccada9e` / `graphiti` | `0275b8abb307039d0bc975b5699e5b86fe6ca1d5` | Same Graphiti identity and revision |
| `AAS-2026-10-11-graphiti-72c99440b180-01` | `graphiti-72c99440b180` / `graphiti` | `48453a8110bd36bc51fbcad3e9b2b394b694f603` | Same Graphiti identity and revision |
| `AAS-2026-10-11-letta-code-f54d2479889e-01` | `letta-code-f54d2479889e` / `letta-code` | `0275b8abb307039d0bc975b5699e5b86fe6ca1d5` | `https://github.com/letta-ai/letta-code`; `letta-ai--letta-code`; `271f119dcf37d58649a18e6c733386b3c710a456` |
| `AAS-2026-10-13-gbrain-ab46e8c48dba-01` | `gbrain-ctx-opus-ab46e8c48dba` / `gbrain` | `dc867d22e41763efe038292b9f1c5eee54e517d5` | `https://github.com/garrytan/gbrain`; `garrytan--gbrain`; `1be42ac99e275603b65ae6793679a411dfa36f94` |

Fresh recursive relative-path/SHA-256 maps include every file, including the
assembled manifest. For **each** candidate, the exact file set and all hashes
match (1) its completed `R/effects/publish.json:new`, (2) intake
`effect-published-sha256`, and (3) intake `published-sha256`. Missing, extra and
changed files are all empty. All published hashes also have matching stored
version bytes. This is a new observation, not a backdated check. Each supplied
prior audit's bytes still match its intake hash. Those audits report historical
full-map checks; their manifest hashes agree below. The intake retains the full
maps used here; prose assertions in older audits are not a second independent
historical map.

For reproducible compact binding, map digest means SHA-256 of UTF-8
`json.dumps(map, sort_keys=True, separators=(',', ':'))`, with no newline.

| Token | Files / completed publish attempt | Assembled ARTIFACT.yaml SHA-256 | Fresh complete-map digest |
|---|---|---|---|
| `5833fd846841` | 12 / `000032-publish` | `0a98343d230587a4482d8758fcb24ec505596fec11d0bdec69c66dff8c9afdef` | `bc1bbd1f38d380e0f3737e8a4939498deb193d7a46817ce278e8a47a0493fcf3` |
| `85a21a06d35c` | 12 / `000028-publish` | `eca2bfafdcd3cc11be49a87dfe6fba9b486f461d50bd9e5d9563714ef2d3978c` | `3e8e45a27da59dbae80a76c086795b3e8cc9fae67f55fe3ae7351cb7cfadaa0a` |
| `4896fccada9e` | 12 / `000042-publish` | `6bc7138483846655623b7ba5cc697d0a314810f58891d45ef58b0bfa5b5919d8` | `07101005b76cdef40663b8599f26acb4351ad213a5eb153360d25a1d7af0e1a4` |
| `72c99440b180` | 12 / `000037-publish` | `b80635dde20520eff3d5f8f3951fae702f3218068db3e48ba4fab14008266195` | `4d3d73daadfeaa955b207d94c132dede924586bef3fdce5242abc2102559e283` |
| `f54d2479889e` | 12 / `000032-publish` | `0f7603d2c792ed657ac19734cc877d762368e3ccf6f152956c6252a3369a0674` | `909cc15ae1391b1c2915d7db5a2b1cbb555c13f391ec98f6208a753689239080` |
| `ab46e8c48dba` | 13 / `000064-publish` | `638c5e6b59bf3f807ac332cff11eb331139e7856bc4f2309270780a09961a204` | `971a28891a700401ec9cab8a25f589d56652459a0b4a4a9ac18480611af12035` |

Publication agreement is not semantic acceptance or integration clearance.
Working type-only manifest stubs are not the assembled publication manifests.

## What the pinned jobs could repair

Actual attempt names and pinned instruction versions were inspected. The common
missions are retained in each applicable version store:

- `runtime`, instruction `07451230…bbc5`: challenge consequential claims and
  enumerate materially equivalent alternate control/delegation paths.
- `memory`, `7804d086…0d75`: trace retained results, cleanup/withdrawal and later
  consumers; runtime is provisional, not an inspection limit.
- `reconciliation`, `fe4541ee…bfa2` (GBrain `679917ce…9e88`): connect identities
  and disagreements, **not** judge or rewrite findings.
- `report-verification`: `5c81a1e9…d0d8` for the October 10 pair;
  `41163de9…90b2` for the others. Both independently check consequential
  behavior, conditions, scope and coverage against frozen source. The latter
  explicitly includes alternate paths and producer/consumer omission questions.
  They can request owner-specific report corrections. Thus this is the earliest
  verification restart for source/record faults, not reconciliation or profile.
- `memory-profile` and `profile-verification`, `d548d5a9…7056` and
  `6d359c59…bfb0`: classify/check accepted records; they cannot add source evidence
  or reopen report verification. Partial inventories are not independent checks
  of the disputed source conditions.
- `synthesis` and `synthesis-verification`, `3000dccb…05c4` and
  `f737a0a1…869c`: produce/check a self-standing public account from records.
  The verifier must read it without supporting-member context. It adds no source
  evidence and cannot reopen reconciliation, but can block its own synthesis or
  return `problem`. A true condition buried only in verification is not public
  repair. Pinned verification types `7a95b4ed…09a2` and `6ea2cb1c…432e` distinguish
  publishable limits from materially misleading unsupported statements.

Recommendations below name semantic restart depth, not a simulated engine reset
closure. No reset was tried. After authorized record correction, dependent
reconciliation, verification, profile and synthesis would need regeneration or
rechecking against changed pins. This report does not prescribe manual edits to
accepted outputs.

## Shared frozen Graphiti discrepancy checks

The following checks were made in 5833's S. The seven relevant orchestration,
node/query, search/filter and MCP source files were byte-compared across all four
assigned Graphiti checkouts and are identical. Repetition across candidates is
therefore not independent source confirmation.

- **Saga reset:** `graphiti_core/graphiti.py:516–533` hydrates named sagas without
  summary/watermarks; `nodes.py:907–940` defaults them to empty/null and saves
  them. Ordinary ingestion saves at `graphiti.py:1087–1091`; the prior audits
  additionally locate bulk save at 1821–1826. Fallback replacement at
  `models/nodes/node_db_queries.py:352–373` writes those defaults. The static
  countercase requires intervening named-saga ingestion. Repeated summarization
  without it, fully hydrated caller objects and custom operation implementations
  differ. No live loss or backend-wide guarantee is asserted.
- **Successful bulk retention and missing reverse index are separate faults:**
  ordinary helper `graphiti.py:1027–1042` assigns `entity_edges` and conditionally
  blanks raw text. Bulk constructs content-bearing episodes with one `now` at
  1664–1703 and saves them again at 1750–1773 without that helper. The operative
  episode-list assignment search finds 1031, not a bulk counterpart.
  `nodes.py:325–328` defaults the list empty; `utils/bulk_utils.py:160–163` and
  `models/nodes/node_db_queries.py:97–109` persist content and list. Lookup at
  `graphiti.py:2009–2021` and cleanup selection at 2164–2192 consume the list.
  Facts may exist but be missing from episode lookup and explicit edge cleanup;
  deletion of incident nodes can still remove some facts. Surviving shared
  entities are the consequential cleanup countercase.
- **Whole-episode tie loss differs from truncated suffix loss:** the shared bulk
  timestamp, fetch cap 20 and strict `created_at > since` at 635–666, followed by
  selected-maximum watermark at 782–786, admit the 21-short-sibling static case.
  One sibling can be excluded next time. No oversized text or clock accident is
  required. This is the inspected fallback selector, not every custom operation.
- **Units:** `graphiti.py:130–175` packs 100000 characters using `len(content)`;
  assembled UTF-8 bytes are a separate control. **Count:** 1431–1442 overrides
  the helper default with `RELEVANT_SCHEMA_LIMIT`, ten at
  `search/search_utils.py:64`, unless explicit previous UUIDs are supplied.
- **Instruction channels:** `mcp_server/src/graphiti_mcp_server.py:136–181`
  supplies correctly named `search_memory_facts` instructions directly to
  `MCPServer`. Cursor's externally installed `search_facts` rules are separate.
  Server wiring establishes neither host presentation nor compliance.
- **Other retained source faults:** `graphiti.py:1945–1948` mutates a shared search
  recipe; `search/search.py:145–170` can await before reading its limit. This
  permits budget interference, not an observed race. MCP date-range construction
  `mcp_server/src/utils/type_config.py:139–202` has comparisons but no null
  predicate; core `search/search_filters.py:167–226` reuses inner-index parameter
  keys across OR groups. These are two distinct temporal-filter limitations.

## 1. Graphiti 5833fd846841

Prior [readiness audit](../unintegrated/AAS-2026-10-10-graphiti-5833fd846841-01.md)
and its [full original audit](../../../analysis-audit-evidence/reports/graphiti-analysis-and-trace-audit.md)
were read completely. The byte-binding row above applies to this exact run.

**Earliest authors and retained faults:**

| Fault | Earliest evidenced account and consequential propagation |
|---|---|
| G1 named-saga reset omitted | Initial `000005-runtime` (`report=abfea44e…44b7`), `RT-RTE-summary-maintenance`, already describes old-summary recurrence without the intervening ingestion case. `000007-memory` (`ecca537f…4729`), `MEM-OBJ-saga-summary`, `MEM-OBJ-saga-watermarks`, `MEM-RTE-saga-summary`, supplies the detailed but incomplete retention account; `A/synthesis.md:28` repeats it. Not reconciliation loss. |
| G2 successful bulk raw retention omitted | Initial runtime bulk route documents early-write failure, not successful suppression parity. First broad retention interpretation is `000007-memory`, core idea/object and ordinary-ingestion annotation (`A/memory.md:35,51,248`). `A/synthesis.md:24` says raw content can be disabled without single-path scope. Rebuilding memory is necessary; rebuilding only the failure caveat is insufficient. |
| G3 bulk lookup/cleanup index omitted | Initial memory `MEM-OBJ-episode-metadata`, read-back and `MEM-RTE-episode-withdrawal` omit the producer/consumer break. Runtime's bulk route is already incomplete upstream; synthesis's first-support deletion caveat concerns a later predicate and is not repair. |
| G4 shared search-budget race | Initial runtime `RT-RTE-memory-retrieval` omits shared recipe mutation. No concurrency-budget qualification is added by memory or synthesis. |
| G5a MCP null-filter expressivity; G5b core OR parameter collision | Initial runtime retrieval/filter account omits both; memory temporal-revision qualifications do not identify either. Preserve separately from G4 and from general non-current-only retrieval. |
| G6 second MCP instruction channel | Initial runtime `RT-BAP-memory-rules` inventories Cursor rules only. Initial memory core idea 4 (`A/memory.md:38`) says MCP instructions require external installation. `reconciliation.md` and synthesis preserve that conflation rather than losing an existing positive server-wiring record. |
| G7 ordinary context count | Initial memory ordinary-ingestion annotation at 248 substitutes helper-default three for caller ten. Not a synthesis-created number. |
| G8 false typo criticism | Origin is `000017-report-verification` (`b06c2003…1504`), `A/report-verification.md:36`, not epistemic authorship. `000008-epistemic` is the published version `04dbbea9…8b45`; its ledger at 56 and declaration already say `dedup_helpers.py`. No source citation repair is needed. |

**Failed barrier / verification depth:** `000017-report-verification` declares no
blockers while accepting the affected admission, objects, summaries, withdrawal
and host-doctrine accounts. It had source-check/correction authority for G1–G7.
`000029-synthesis-verification` (`e09abe0d…1861`) accepts the repeated public
claims but is not an independent source check. Restart recommendation:
`report-verification` for G1–G7; regenerate that same verifier's own account for
G8, without sending a false typo repair to epistemic. G8 alone does not justify
rebuilding otherwise correct analyst records.

**Author depth:** `runtime` for instruction, retrieval/control omissions and the
incomplete saga/bulk route account; `memory` for the retention, index, saga and
count records. Preserve the good equal-timestamp and character/byte distinctions,
optional-cache account and repaired profile refusal. The partial profile is a
downstream consumer of incomplete records, not an established independent
classification error. Keep boundary/acquisition, identity and frozen source.
Confidence is high for source conditions and installed origins; an omission's
precise cognitive cause is not knowable from stored output. Original trace
recoveries remain attributed to the full audit, not newly replayed.

## 2. Graphiti 85a21a06d35c

Prior [readiness audit](../unintegrated/AAS-2026-10-10-graphiti-85a21a06d35c-01.md)
and [full original audit](../../../analysis-audit-evidence/reports/graphiti-85a21a06d35c-analysis-and-trace-audit.md)
were read completely. Exact 12-file binding is in the table.

- **G1 successful bulk raw retention:** `000005-runtime` (`f7681adc…2894`),
  `RT-RTE-bulk-admission`, already omits successful-path suppression parity;
  ordinary raw suppression is correctly scoped there. `000007-memory`
  (`8b1028f9…7ab9`), write-side/object account, does not add the successful bulk
  condition. `A/synthesis.md:20` narrows ordinary admission but describes bulk
  only as a different intermediate state. This is an initial route/retention
  omission, not a new synthesis-only universal raw-suppression claim.
- **G2 missing bulk fact index:** initial memory provenance and withdrawal
  discussion, plus `000008-epistemic` provenance-delivery record, emphasizes
  projected-away fields, not absent upstream edge selection. Synthesis at 42
  propagates that narrower explanation. No reconciliation record preserves the
  missing producer assignment and then loses it.
- **G3 whole equal-time episodes:** initial memory `MEM-RTE-saga-summary`
  characterizes oversized suffix loss but leaves tied batches unexercised;
  profile saga units and synthesis at 34/66 carry that weakness. Frozen source
  provides a concrete static countercase, not merely a need for target testing.
- **G4 unit error:** already in initial runtime `RT-RTE-maintenance-admission`,
  `A/runtime.md:280` (UTF-8 payload budget), then explicitly `100000 UTF-8 bytes`
  in initial memory at 135. `000014-reconciliation`'s summary-controls account
  does not correct it; synthesis at 34 repeats byte selection. The origin is
  not profile or synthesis.

**Barrier:** `000017-report-verification` (`e6eff41e…6037`) accepts bulk writes,
summary controls and provenance, with no blockers/limits; its count/byte reading
fails the measuring-operation check. `000025-synthesis-verification`
(`2cbb4eef…a6bc`) repeats count/byte acceptance. Minimum verification restart is
`report-verification`, not a source-free synthesis verifier. Author depth is
`runtime` for the incorrect unit and incomplete bulk route; `memory` for G1–G4,
with dependent epistemic provenance checked after correction. Keep correctly
scoped ordinary suppression and ten-versus-three distinction.

The original audit's optional-cache omission, Cursor mismatch omission and
weakened first-support deletion consequence remain separate comparison-breadth
limits, not claims of absent features or newly cleared defects. Its late
publication prerequisite, ordering and shell-status incidents remain historical
operational findings. They are not fixed by resetting a semantic job and are not
newly traced here. No current operational clearance is inferred. Boundary and
acquisition can be retained. Confidence is high for G1–G4 and output depth;
complete alternative-provider/backend behavior remains outside inspection.

## 3. Graphiti 4896fccada9e

Prior [readiness audit](../unintegrated/AAS-2026-10-11-graphiti-4896fccada9e-01.md)
and [full repeat audit](../../../analysis-audit-evidence/reports/graphiti-4896fccada9e-repeat-analysis-and-trace-audit.md)
were read completely. Exact binding is in the table.

- **C2 bulk provenance:** first memory output `000007-memory`,
  `V/f46637165bb87e199ab13ab8a0aabc6f0d5ea51c4e28d957236dbb22ae72710f`,
  already describes `entity_edges` assignment/navigation without the missing
  bulk assignment. Installed correction `000021-memory` (`a0fd77fb…939b`),
  `MEM-OBJ-graph-metadata`, `MEM-RTE-explicit-read`,
  `MEM-RTE-memory-withdrawal`, keeps that omission. Raw suppression was repaired
  in that retry; the neighboring index defect was not. Not a reconciliation loss.
- **C3 named-saga reset:** initial memory's saga object/route is already missing
  the intervening named-ingestion save. Installed `MEM-OBJ-saga-node` and
  `MEM-RTE-saga-summary`, plus epistemic saga records, retain that gap.
  Runtime expressly leaves detailed saga internals to memory; this is the first
  detailed author stage, not a profile mistake. Synthesis at 32 repeats it.
- **C4 ties:** initial memory at 172 already says deferred later episodes remain
  eligible; installed memory at 188 retains it while 190/365 leave ties
  unresolved. The source's strict comparison refutes the unqualified eligibility
  sentence. Reconciliation's preservation discussion and synthesis's general
  no-losslessness caveat do not repair that route-specific statement.
- **C5 instructions:** initial `000005-runtime` (`53d3eaf1…3c73`) and installed
  `000019-runtime` (`b7bcab58…86a6`), `RT-BAP-memory-rules`, omit the server
  channel. Synthesis at 44 extends Cursor's mismatch to “the instructions”.
  This has both initial coverage loss and downstream overgeneralization.

**Barrier:** first `000017-report-verification` successfully forced raw-retention
and evaluator corrections, but not C2–C5. Final `000031-report-verification`
(`9f72da90…8496`) accepts those records after the corrections. Its omission
questions and stopping decision do not dispose of these distinct conditions.
`000039-synthesis-verification` accepts repetition, not new corroboration.
Minimum verification restart: `report-verification`. Author restart: `memory`
for C2–C4; `runtime` for C5. A whole dependent rebuild must therefore start no
later than `runtime`, but this must not conceal the separate memory origins.

The repeat audit's C6 optional cache and C7 node-versus-edge update detail remain
breadth limits. Its C8 shared-recipe race and the two temporal-filter limitations
are separate earlier runtime omissions, supported by the shared source checks
above; do not collapse them into saga depth or call them repaired. Keep successful
bulk suppression/evaluator repairs and correct count/units. Profile units are
partial and depend on these records; no independent extractable-value fault was
established. Preserve boundary/acquisition. High confidence for source and initial
memory wording; no new all-worker action/compliance claim is made.

## 4. Graphiti 72c99440b180

Prior [readiness audit](../unintegrated/AAS-2026-10-11-graphiti-72c99440b180-01.md)
and [full amendment audit](../../../analysis-audit-evidence/reports/graphiti-72c99440b180-amendment-effects-audit.md)
were read completely. Exact binding is in the table.

- **Named-saga reset:** initial `000005-runtime` (`5164b109…b683`), maintenance
  route, already gives old-summary recurrence without the named-ingestion case.
  Initial `000007-memory` (`07b9b7dc…c83a`, identical to publication) supplies
  detailed `MEM-OBJ-saga-summary`, `MEM-OBJ-saga-watermarks` and
  `MEM-RTE-saga-summary` without reset. Synthesis at 24 repeats the gap.
- **Bulk reverse index:** initial memory `MEM-OBJ-graph-metadata` at 64–66 quotes
  only the ordinary assignment. Its lookup/removal account lacks the bulk
  producer break. General lineage and first-support qualifications are not the
  missing route condition. Initial runtime bulk coverage is incomplete but
  explicitly withholds retention-setting parity; memory is the detailed fault.
- **Server instruction channel:** initial runtime `RT-BAP-memory-procedures`
  inventories Cursor rules only; corrected `000019-runtime` (`2dc259bd…9f3d`)
  preserves it. Reconciliation and synthesis's tool-name statement do not restore
  the wired server channel.
- **Ordinary count:** initial memory's ordinary-ingestion annotation at 249–252
  says three, quoting the helper instead of its caller. This predates profile,
  reconciliation and synthesis; runtime's general selection does not supply that
  false number.
- **False verifier typo:** already present in first `000017-report-verification`
  (`de4fb0c6…2c36`), version line 23; retained by `000026-report-verification`
  (`2f880df3…a1a0`), `A/report-verification.md:24`. The published and initial
  `000008-epistemic` output (`3cd5ab20…4b68d`) already uses `dedup_helpers.py`
  at ledger 155 and declaration/quotation 534/550. This is verifier-authored
  criticism, not an epistemic citation defect.

**Barrier:** `000017-report-verification` routes an evaluator repair, not these
conditions; `000026-report-verification` accepts the installed account.
`000034-synthesis-verification` carries public tie/withdrawal/evaluator limits
but does not detect the omitted source channels. Minimum verification restart:
`report-verification`. Author rebuilding: `runtime` for instruction coverage and
maintenance baseline; `memory` for saga/index/count; the verifier owns its false
criticism. Not an instruction to rewrite correct epistemic locators.

Preserve the repaired evaluator, successful bulk raw-retention qualification,
character/byte distinction and **already public tied-timestamp qualification**.
Do not reclassify ties as an unresolved false claim in this candidate. The two
stale specialist evaluator attributions arise after runtime correction; final
reconciliation identifies them and verification/synthesis explicitly carry them.
They are an acknowledged dependent-history limit, not an unnoticed source fault.
Cache breadth is explicitly bounded. Earlier shared-recipe and filter findings
remain attributed/unresolved; the common static mechanisms above still apply,
but their complete candidate-specific propagation was not re-audited. No profile
error independent of faulty records was established. Boundary/acquisition can
remain. Confidence is high for the named faults and their initial/installed
output stages, including the first verifier's false criticism.

## 5. Letta Code f54d2479889e

Prior [publication audit](../unintegrated/AAS-2026-10-11-letta-code-f54d2479889e-01.md)
and [full repeat audit](../../../analysis-audit-evidence/reports/letta-code-f54d2479889e-repeat-analysis-and-trace-audit.md)
were read completely. Exact 12-file binding is in the table.

**Earliest omission versus public overgeneralization:** `000005-runtime`
(`6c7aa89e…5fbe`, identical to installed runtime) has a correctly named
`RT-RTE-subagent-launch` / “Task subagent launch and return” at 200–219. Its
forcing-case summary at 36 is still Task/subagent-manager scoped, but it does not
inventory Workflow as the materially different delegation route. `000014-reconciliation`
(`5edd1009…7bfe`) connects memory workers to this Task container; it does not lose
an existing Workflow qualification. `000027-synthesis` (`c21cf1ad…edad`) at 22
then drops the Task restriction: “Delegation launches a local unrestricted
headless child”. That is a separate public scope error built on incomplete
runtime coverage, not proof that the Task record itself is false.

**Frozen discrepancy:** `S/src/tools/impl/workflow.ts:204–219` passes current
runtime permission mode (or global mode) to its SDK spawner;
`src/tools/workflow/sdk-spawner.ts:334–383` passes it into worker query options.
`workflow.ts:227–266` also captures permission inputs and rejects direct MCP
calls whose decision is not allow. This establishes different wiring, not
successful SDK enforcement or an exhaustively safe Workflow route. Task's
unrestricted launch remains a valid positive case.

**Barrier/depth:** `000017-report-verification` (`9ee4f541…eba4`) accepts Task
launch and selects alternate-caller questions without retaining the Workflow
permission contrast. It has authority to request runtime coverage/narrowing.
`000029-synthesis-verification` (`484a614c…e840`) additionally accepts the generic
public delegation sentence against a Task-only record. For the **public sentence
alone**, a `synthesis-verification` restart and `synthesis` author correction can
confine it to Task without reanalysis. For a faithful account of the consequential
alternate delegation control, the minimum verification depth is
`report-verification`, with `runtime` author rebuilding. Recommend this deeper
route for the held candidate; do not mistake the cheaper Task-only qualification
for a repaired alternate-route inventory.

The memory profile's mod-workflow and memory-worker values are not Workflow
permission findings; the repaired skill-gate classification remains separate.
No independent profile-origin fault was established. The old audit's hook
ERROR/BLOCK and Workflow security coverage losses remain breadth caveats, not
certified absent mechanisms. Keep source/acquisition/boundary, local Task result
and existing successful profile repair. High confidence in the wiring and two
separate origins; deployed SDK enforcement is outside this static evidence.

## 6. GBrain ab46e8c48dba

The assigned [prior audit](../unintegrated/AAS-2026-10-13-gbrain-ab46e8c48dba-01.md)
was read completely. Exact 13-file binding is in the table.

**Earliest faulty stage is synthesis, not runtime or reconciliation.** Initial
`000005-runtime`, `V/32b63bdd52912f5a74efd3f97261cdaf6f189efe6aee2894e10d86cd06736c90`,
already restricts maintenance writes to unmanaged brains and identifies managed
file imports. Corrected/installed `000024-runtime`
(`a5ee7dd2…cbab`) keeps both at `A/runtime.md:1259–1354`:
`RT-RTE-unmanaged-maintenance-write` says managed guard refusal;
`RT-RTE-file-sync-import` says managed changes go through the coordinator.
Final `000046-reconciliation` (`cab5ed6c…0493`) at 404–410 distinguishes content
screening from grants, not a finding that all maintenance bypasses the journal.
The selected profile scope likewise describes journaled verbs rather than
claiming uniform bypass. No upstream missing managed condition was established.

`000059-synthesis`, `V/b445132706711540d5474432f9330f3b59fc78418c926d3d0194f40a97076cce`,
`A/synthesis.md:101–113`, says three alternate paths bypass the journal and
includes maintenance and checkout sync without their managed conditions.
Credential-level direct SQL is a separate remaining bypass. These must not be
merged into one global failure of managed coordination.

**Frozen source check:** `S/src/core/persistence/maintenance.ts:55–69` refuses
legacy canonical writers on managed brains; `src/core/import-file.ts:345`
requires unmanaged mode for direct non-preparation import;
`src/core/persistence/import-mutations.ts:181–202` creates
`managed_file_import` intents and submits managed imports. This corroborates the
retained conditions, without executing GBrain or certifying its whole write path.

**Failed barrier:** `000061-synthesis-verification`
(`5cb0a174…3027`) explicitly identifies the missing managed conditions at
`A/synthesis-verification.md:140–151` yet declares Blockers `none`. Its
reader-only qualification does not change the self-standing synthesis. The
failure is disposition/public-carriage, not failure to discover source evidence.
`000062-apply-synthesis-verification` and completed publication do not independently
settle materiality. Minimum verification restart is `synthesis-verification`;
author rebuilding is `synthesis`. Existing records, profile, reconciliation,
report verification, boundary and acquisition can remain for this fault.

**Separate consequential public faults already recorded by that verifier must
also survive the recommendation.** These are record-to-public comparisons, not
a fresh system-wide source audit. They share the `000059-synthesis` origin and
`000061-synthesis-verification` disposition failure; none calls for widening the
frozen source boundary:

| Public wording | Record condition lost / bounded depth finding |
|---|---|
| “Withdrawal reaches only exact-fingerprint copies” (`synthesis.md:402–403`) | `memory.md:1106–1122`, `MEM-ABS-withdrawal-invalidators`, establishes no registered additional invalidators and no inspected paraphrase reach, not exhaustive absence of every route. The synthesis's own bounded mechanism/limitations do not make the absolute scenario claim true. |
| “Strongest content check in the system” (406–408) | Verifier limits comparison to assessed routes; placed/untraced phases remain. Rebuild this synthesis comparison, not a complete evaluator inventory. |
| “remember and other explicit lanes” automatically supersede (137–145) | `MEM-RTE-facts-backstop` and preceding synthesis mechanism distinguish explicit extraction lanes that deduplicate without supersession. `EPI-RTE-fact-supersede` scopes the positive to remember, enabled managed supersession and legacy single-fact writes. The conflicting generalization must not subsume those cases. |
| All delivered memory has a “data, not instructions” envelope (194–196) | `memory.md:1154–1208` separates enveloped injected-memory paths from `MEM-BAP-memory-md` standing rules and compiled instruction files. Advisory force survives; universal envelope scope does not. |
| Frontmatter/overview “default-on … dream synthesis” | `memory.md:1284–1295` and synthesis body at 233 require a configured corpus directory. This is synthesis-description loss propagated into the assembled overview, not evidence of a boundary/acquisition problem. |
| Profile-coverage limitation omits SkillOpt history/rejected edits | `profile-verification.md:181` names these uninventoried objects; synthesis's carried coverage row does not. This is limit-carriage loss, not a newly proved false profile value. |

Confidence is high for the journal issue's source, synthesis origin and failed
barrier. The additional rows are high-confidence scope/carriage comparisons to
retained records; their complete implementation semantics were not reanalysed.
The no-trace limit from the assigned audit remains: worker reads, effort and
execution obligations are not certified by metadata. No operational violation
was invented from that absence.

## Preservation, limits and completion

All six identities are incumbent alternatives with explicit transfer stops.
No finding here establishes replacement advantage or waives any stop. Retain
opening/acquire/boundary, method/source pins, attempts, judgments, version stores,
publication effects and debug/session evidence. Historical repaired failures and
protocol deviations remain historical; a new semantic run cannot retroactively
satisfy a late prerequisite or decide acceptance of an operational violation.
No new operational hold or collateral mutation was established in this bounded
inspection.

No required evidence was inaccessible. Remaining gaps are limited: no exhaustive
trace replay, no deployed operation/backend/provider certification and no complete
profile reclassification. Earliest **output** stage is evidenced; cognitive origin
and actual source-inspection action are not inferred from citations or verifier
prose. Historical trace findings are attributed to the completely read prior
audits; no fresh actual-action claim requires a trace pairing here.

Report-only `commonplace-validate` returned `VALIDATION SUCCESS`: one text file,
zero failures and zero warnings. Deterministic success checks its form, not these
semantic depth findings. Broader graph discovery through
`cp-skill-connect`, if ever wanted, requires a separate commission and is not a
next execution step under this report-only authority.
