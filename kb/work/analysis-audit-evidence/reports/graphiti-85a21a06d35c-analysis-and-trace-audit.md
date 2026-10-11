# Graphiti analysis and trace audit

## Identity and status

Retained on 2026-10-11 from the audit in the commissioning conversation. This
working report consolidates three independent workers' returned findings and
the coordinator's publication-byte check. It is not a new source audit or a
verbatim transcript. Findings and severity are auditor judgments; recommendations
are not adopted method decisions. The operator requested retention here after
receiving the audit.

```yaml
run-id: AAS-2026-10-10-graphiti-85a21a06d35c-01
method-commit: 6ff7c828e94dd66abdf5af00c89db6420bc6a1ad
source-revision: 964bb11d1e7020e3cc67fab244268b0736b6c219
worker-profile: pi-sol
audit-date: 2026-10-11
```

Local worktree: `/home/zby/llm/commonplace/.commonplace/worktrees/graphiti-85a21a06d35c`.
Local coordinator session:
`/home/zby/.pi/agent/sessions/--home-zby-llm-commonplace--/2026-10-10T22-09-14-881Z_01a127dc-f680-711e-8a12-57e725ff77d1.jsonl`.
Original worker messages are embedded in subagent tool-result
`message.details.results[0].messages` arrays. Separate original child-session
archives were not found. These local paths are evidence locators, not durable
run identities.

Path abbreviations:

- `A/`: the worktree's `kb/agentic-system-analyses/retained/graphiti/`.
- `S/`: the worktree's `related-systems/getzep--graphiti/`.
- `R/`: the worktree's `kb/agentic-system-analyses/state/AAS-2026-10-10-graphiti-85a21a06d35c-01/`.
- `P/`: the retained Graphiti set in sibling worktree `graphiti-5833fd846841`.
- `H`: repository file `kb/agent-memory-systems/reviews/graphiti.md`.
- `I`: repository file `kb/sources/graphiti-temporal-knowledge-graph.ingest.md`.

## Outcome and limits

The audit recommended deferring integration. One definite unit error and three
material missing conditions affect the operational account. The central
conclusion survives: Graphiti implements recurrent memory-to-model paths, but
source inspection does not establish source truth, lossless retention, durable
queued ingestion, or improved agent performance.

One worker audited source correctness, one audited traces, and one compared
local Graphiti analyses and checked consequential disagreements against source.
The coordinator independently checked publication hashes. Target inspection was
static and selective; no Graphiti tests, databases, services or models were run.
The source HEAD matched the recorded revision and its working tree was clean.
The audit did not modify analyses, method files, run state or integration state.

The recommendation for a corrected run remains a local recommendation. It does
not authorize a rerun, method change, integration or source-worktree disposal.
Retained analyses are frozen under their collection contract.

## Correctness findings

### G1 — High: Successful bulk ingestion ignores raw-content suppression

`A/memory.md:37,229,270`, `A/runtime.md:178–194` and `A/synthesis.md:20`
qualify ordinary retention and discuss early bulk writes surviving failure.
They miss the stronger successful-path condition: `add_episode_bulk` does not
apply `store_raw_episode_content=False`.

Ordinary `_process_episode_data` clears `ep.content` before persistence at
`S/graphiti_core/graphiti.py:1027–1042`. Bulk ingestion constructs episodes with
caller content and initially saves them at `1679–1703`; its final save at
`1763–1772` still uses those episodes without clearing content. Serialization at
`S/graphiti_core/utils/bulk_utils.py:160–174` preserves the field, and the Neo4j
bulk query at `S/graphiti_core/models/nodes/node_db_queries.py:102–110` writes it.

This changes privacy and retention expectations even when ingestion succeeds.
The proposed correction distinguishes ordinary suppression from bulk retention,
not merely successful writes from intermediate failed state. Confidence is high
for the inspected static chain; persistence was not database-tested.

### G2 — High: Bulk-created episodes omit an index consumed by provenance retrieval

The provenance discussion at `A/epistemic.md:369–399`, `A/memory.md:276` and
`A/synthesis.md:42` emphasizes fields omitted from returned edges. An earlier
producer/consumer mismatch can omit the associated edges entirely.

`EpisodicNode.entity_edges` defaults to an empty list at
`S/graphiti_core/nodes.py:325–328`. Ordinary ingestion populates it at
`S/graphiti_core/graphiti.py:1030–1031`; the bulk route at `1586–1854` does not
populate it for newly constructed episodes. The bulk persistence query preserves
that list. `get_nodes_and_edges_by_episode` consumes it at `2009–2021`, rather
than querying the edges' own episode provenance. Core removal uses it to select
candidate edges at `2164–2176`.

Bulk-created facts can therefore be absent from episode-based edge retrieval
although the facts exist. Core removal also receives an empty edge candidate
list. This does not establish absence of all edge-side provenance or exclude
other deletion effects. The report marked query internals as uninspected; this
is a material missing condition, not a contradiction of exhaustive coverage.
Confidence is high from static producer, persistence and consumer inspection.

### G3 — Medium: Saga progress can skip whole bulk episodes

`A/memory.md:130–148`, `A/synthesis.md:34,66` and
`A/memory-profile.md:965–984` identify truncated episode suffixes but leave
equal-created-time cases mostly as unexercised uncertainty.

Bulk ingestion assigns one `now` to all newly constructed episodes at
`S/graphiti_core/graphiti.py:1664–1691`. Saga summarization selects at most 20
at `635–641`; the inspected fallback queries at `645–666` require subsequent
creation times to be strictly greater than the watermark. The watermark becomes
the maximum selected creation time at `782–786`.

A static counterexample is a successful bulk call creating 21 nonempty episodes
in one saga. The first summary selects at most 20 and advances to their shared
time; an unselected sibling fails the next strict comparison. Content-budget
limits can produce the same problem with fewer episodes. No oversized individual
episode, provider error or accidental clock collision is needed.

This is high-confidence static reasoning for the inspected query path, not an
observed loss incident. The correction should distinguish whole-episode loss
from truncated-suffix loss. Both correctness and comparison reviewers identified
this mechanism; their agreement is not evidence from two independent runs.

### G4 — Medium: Saga selection counts characters, not UTF-8 bytes

`A/memory.md:135` says 100,000 UTF-8 bytes; `A/synthesis.md:34` propagates the
unit error. The selector measures 100,000 characters, then separately applies a
128-KiB constructed-prompt limit.

`S/graphiti_core/graphiti.py:130–175` distinguishes the constants and uses
`len(content)` and character slicing. Lines `689–690` supply the character
limit; `725–750` apply the later prompt-byte limit. The misleading compatibility
constant and log wording do not change execution. The difference matters for
non-ASCII input.

`P/memory.md:312` and `P/synthesis.md:28` correctly distinguish the controls at
the same revision. `A/report-verification.md:30` did not catch the unit error.
This is a factual regression, not revision drift.

## Comparison with other Graphiti analyses

### Comparator boundaries

| Set | run-id | method-commit | source-revision |
|---|---|---|---|
| New | `AAS-2026-10-10-graphiti-85a21a06d35c-01` | `6ff7c828e94dd66abdf5af00c89db6420bc6a1ad` | `964bb11d1e7020e3cc67fab244268b0736b6c219` |
| Same-revision retained comparator | `AAS-2026-10-10-graphiti-5833fd846841-01` | `6ff7c828e94dd66abdf5af00c89db6420bc6a1ad` | `964bb11d1e7020e3cc67fab244268b0736b6c219` |
| October 6 state archive | `AAS-2026-10-06-graphiti-370e139ea7c2-01` | `ec24f7b4e919185101bd2e1ed0010c44b8427cd4` | `2a85bbbf27f3d0d07dd3a8bf6dc8700c5193c066` |
| October 5 state archive | `AAS-2026-10-05-graphiti-0b7292fa4af1-01` | `b95a2bb79b17f3dea5b29ba74cb4c6225749c904` | `4083f51812d381d7ca28b887cfa3c3db188f576d` |

The two October 10 sets have the same source and method boundary. Their
`overview.md:6–15` and preparation records retain the identities. The older
archives' `run-state.md:4–11` and `run-metadata.json` retain theirs. No equivalent
retained publications were found for those two older archives. The October 5
final verification still names blockers; October 6 records a resolved previous
blocker. They are archive evidence, not interchangeable accepted publications.

`H` pins `34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6` without run/method identity.
Copies in the inspected sibling worktrees were byte-identical, not independent
reviews. `I:51` identifies its original snapshot as a manual architectural
summary, not a verbatim repository capture. Neither has the same evidential
status as the frozen implementation.

### Gains

- **Context count:** `A/memory.md:212–223` correctly separates ten prior episodes
  for ordinary ingestion from three for general retrieval. `P/memory.md:248`
  blurs them. Source: `S/graphiti_core/graphiti.py:1436` and
  `S/graphiti_core/search/search_utils.py:64`.
- **Attribute updates:** `A/memory.md:99–116` distinguishes node overlay from
  edge replacement/clearing more precisely than `P/memory.md:22`. Source:
  `S/graphiti_core/utils/maintenance/node_operations.py:1068–1074` and
  `edge_operations.py:1061–1072`.
- **Shipped automatic delivery:** `H:103` overstates the absence of automatic
  memory injection. `A/runtime.md:246–268` traces the shipped notebook's search,
  system-message facts, invocation and later ingestion. Source:
  `S/examples/langgraph-agent/agent.ipynb:328–375`. The comparator checked that
  this notebook did not change between the historical and new source pins.
  This is improved inspection, not a new feature; the other October 10 set also
  captures it. It does not establish deployment or answer improvement.
- **Operational qualification:** Compared with `H`, the new account is stronger
  on queue acknowledgement, worker-start races, partial bulk writes, temporal
  filtering and evaluator defects (`A/runtime.md:24–29`,
  `A/memory.md:240–248`, `A/synthesis.md:56`). Much of this gain is shared with
  the other October 10 set.

### Lost or weakened findings

- **Response cache omitted:** `P/memory.md:133–139,173–199` and
  `P/synthesis.md:36` cover optional SQLite/JSON inference-response retention.
  Source: `S/graphiti_core/llm_client/client.py:75–92,253–281` and
  `cache.py:27–61`. A cache hit substitutes retained output for new inference.
  It is disabled by default; provider overrides may bypass it. The new set
  lacks a corresponding account.
- **Equal-time backlog loss weakened:** `P/memory.md:157,312` and
  `P/synthesis.md:28` preserve the concrete mechanism described in G3.
- **MCP name mismatch omitted:** `P/runtime.md:440` records that shipped rules
  use `search_facts` (`S/mcp_server/docs/cursor_rules.md:6`) while the tool is
  `search_memory_facts` (`S/mcp_server/src/graphiti_mcp_server.py:616`). This is
  an integration obstacle, not proof every host fails; an adapter could resolve it.
- **Shared-support deletion consequence obscured:** `A/memory.md:275–280`
  retains the first-provenance rule but does not foreground that deleting the
  first supporting episode can delete an edge supported elsewhere.
  `P/memory.md:216,311` states the consequence. Source checks `edge.episodes[0]`
  at `S/graphiti_core/graphiti.py:2174`, despite the preservation promise at
  `S/mcp_server/src/graphiti_mcp_server.py:734`.
- **Replay question omitted:** `I:31,41,53` distinguishes reprocessing retained
  episodes from reproducing equivalent graph state. This useful research
  question is not a demonstrated rebuild guarantee or irrebuildability claim.

The October 6 archive's 200-episode limit and wall-clock watermark differ from
the current 20-episode limit and selected-episode watermark because source
changed. The older source contains those operations at `graphiti.py:491,563`.
The absence of historical Commonplace borrowing advice is also not a defect:
the new analysis has a different scope.

## Trace findings

Trace anchors use 1-based coordinator JSONL lines (`L`) and 0-based worker
message indices (`m`) in the embedded array named above. Original-run coverage
ends at L71; subsequent audit messages are not analysis contamination.

### T1 — Medium: Publication prerequisite loaded after publication

The method requires publication instructions before publication
(`instructions/analyse-agentic-system/SKILL.md:205`). L57–58 submitted the final
verifier result and advanced at 22:48:42–22:48:51 UTC. The run records show
completed `000027-assemble` and `000028-publish`. L59–62 attempted two wrong
instruction paths; L65–66 first loaded the correct file at 22:49:06 UTC.
L67–68 then issued a redundant advance instead of immediately inspecting.

Engine-controlled publication did not demonstrate corrupt bytes, but the
coordinator missed a required prerequisite. The proposed remedy is to load
publication instructions before the first advance, which can automatically
reach publication.

### T2 — Medium: Shell success concealed a validation failure that was repaired

Runtime L27 m77 had `isError: false` while validation output reported a missing
notebook quotation and printed `exit=1`. A final `printf` masked the command's
failure status. The worker noticed it: m78 repaired attribution, m81 and m83
searched/read the raw notebook, and m85 passed validation with `exit=0`.

Runtime m30 and m42 also chained searches with semicolons, exposing only the
last status. No unresolved validation error was found. The existing worker
rules at `jobs-engine/follow-worker-rules.md:29–34` already require status
preservation. Tool-level success alone was insufficient monitoring evidence.

### T3 — Low: Recovered errors disappear from the completed summary

- Boundary L23 m62 and m66: attribution validation failures. The worker added
  frozen-revision attribution; m74 passed. At m68 a search of nonexistent
  `src/commonplace/lib/validate*` exited 2 while another operand produced hits.
- Epistemic L32 m71: exact replacement failed; m72 retried and m75 validated.
- Coordinator L11–14: `start` ran from the originating checkout and was refused;
  the retry used the prepared worktree.
- Coordinator L59–66: wrong publication-instruction paths, then successful read.

No claim withdrawal was evident in the quotation repairs. These are recovered
failures and execution friction, not outstanding acceptance failures.

### T4 — Low: Relative paths replaced supplied absolute paths

Examples include runtime L27 m9, m70, m72 and m74. Worker rules at
`jobs-engine/follow-worker-rules.md:17–19` require supplied absolute paths.
Correct launch directories prevented demonstrated misrouting; the practice
still introduced an unnecessary dependency on working-directory assumptions.

### T5 — Coordinator ordering and report fidelity deviations

The coordinator opened and advanced the run before inspecting the worker
profile, although capability checking was required before start. Every actual
analysis launch explicitly selected the correct model and effort, so this was
an ordering violation, not a demonstrated identity mismatch.

The final response reformatted inspect JSON rather than returning it unchanged.
The trace auditor found it semantically identical. Together with T1's redundant
advance, these are bounded protocol deviations, not evidence of failed publication.

### Successful checks

All ten analysis workers used `openai/gpt-6.1-sol`, medium effort, and inspected
their runtime identity. The coordinator used `gpt-6-luna`; explicit worker
selection prevented inherited mismatch. Launches used minimal fresh-session
handoffs. Both parallel specialists finished before the next advance.

No original worker call was found reading forbidden prior analyses, launching
another worker, installing dependencies or executing Graphiti. Notebook decoding
was static processing. No actual unrecovered delivery truncation was found;
selective source reads were not mistaken for incomplete mandatory reads.
Later roles used supplied records; the report verifier documented direct
source checks for named ambiguities.

All 20 retained judgments accepted their inputs. Historical stale structural
judgments were disclosed, with later checks present. There were no model-worker
retries. Inspected method/code/lockfile paths had no tracked drift from the
recorded method commit. Completion showed no open attempts or refusals.

## Publication check

The coordinator independently calculated SHA-256 for every file beneath the
publication destination and compared the complete path/hash mapping with
`R/effects/publish.json`'s `new` mapping:

```json
{
  "files": 12,
  "exact_journal_tree_match": true,
  "missing": [],
  "extra": [],
  "changed": []
}
```

The journal records an absent previous destination and no archive. This check
establishes matching published bytes at audit time, not analytical truth or an
integration authorization. No integration was performed.

## Coverage and cost

| Worker | Coordinator trace line |
|---|---:|
| Boundary | 23 |
| Runtime | 27 |
| Memory | 31 |
| Epistemic | 32 |
| Reconciliation | 36 |
| Report verification | 40 |
| Memory profile | 44 |
| Profile verification | 48 |
| Synthesis | 52 |
| Synthesis verification | 56 |

Coverage: ten workers, 678 embedded messages and 394 worker tool results.
Original temporary handout workspaces were no longer present; embedded
transcripts were available, but separate original child-session archives were
not found. These records do not prove absence of unlogged activity.

Harness-reported original-worker usage: 264 model turns, 878,532 input tokens,
95,736 output tokens, 12,241,536 cache-read tokens and reported cost 3.9385776
in trace cost units. Approximately 38½ minutes elapsed from preparation to the
publication-producing advance. These figures exclude coordinator, diagnostic,
preparation usage and this audit; they are not an independently verified invoice.
Epistemic and report verification were the highest-cost workers. Required
independent reads should not be counted as avoidable work merely because repeated.

## Improvement candidates, not decisions

| Candidate | Expected benefit | Added cost / counterevidence to seek |
|---|---|---|
| Check retention, indexes and watermarks across producer/consumer paths | Catch G1–G3 conditions before acceptance | More source reads; compare whether existing verification already catches equivalent cases and whether misses are local variability |
| Check units against measuring operations | Catch G4 despite misleading names/logs | Small targeted read cost; repeated correct unit checks would argue against a broad new rule |
| Compare independent same-revision runs after source-only analysis | Detect coverage variance without contaminating characterization | Another run is expensive; narrower adjudication may suffice; do not treat agreement as source proof |
| Load coordinator prerequisites before start/advance | Avoid T1/T5 ordering errors | More startup reading; determine whether clearer placement suffices rather than adding a new gate |
| Preserve shell exit status and surface recovered failures | Make T2/T3 visible to monitoring | Telemetry and reporting cost; existing rules already require correct behavior |
| Give concrete citation syntax examples | Reduce attribution-repair friction | Prompt size; test whether it reduces retries without weakening checks |

The original recommendation prioritized sharper verification over adding more
reviewers or weakening isolation. These are hypotheses awaiting comparison, not
an implementation backlog. The audit did not determine whether source-specific
complexity, model variability or a method weakness best explains G1–G4.

## Initial comparison with the Napkin audit

The [Napkin audit](./napkin-analysis-and-trace-audit.md) supplies a second system
at the same method commit and analysis worker profile. This comparison uses its
retained findings, not a new inspection of its traces.

- **Shell-status masking:** Graphiti T2 and Napkin T2 both show a final successful
  `printf` masking an earlier failure. Napkin's failure was an inventory read;
  Graphiti's was validation. Both were noticed and recovered. This is two-run
  support for a concrete execution weakness, not two incorrect accepted results.
  An existing rule already prohibits it. Disposition: accumulating evidence;
  compliance failure and inadequate status tooling remain alternatives. The
  number of correctly handled status opportunities was not enumerated.
- **Attribution repair:** Graphiti T3 and Napkin T3 show validation detecting
  missing or ambiguous quotation attribution and workers repairing it. This
  supports a working safeguard with repair cost, not a failed acceptance gate.
- **Producer/consumer conditions:** Graphiti G2 and Napkin N2 both concern
  retained-state consumers, but their mechanisms differ: missing producer index
  versus aggregation of in-memory rather than reloaded data. Shared vocabulary
  is insufficient to establish one recurring method defect. Disposition:
  needs adjudication against the actual verification obligations.
- **Semantic correction opportunity:** Napkin T1 documents a caught and repaired
  substantive error; Graphiti had no model-worker retry. This is counterevidence
  to a claim that semantic review never works, not proof that either run received
  exhaustive coverage.

No general method change is adopted by adding this report. Publication-byte
checking also differs between audits: Graphiti was independently checked;
Napkin's report explicitly leaves that unverified. Preserve that asymmetry.
