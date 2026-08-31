# Codex ingest-session tool-result volume audit — 2026-08-31

This frozen report measures one Codex ingest run and its two delegated workers.
It records what each shell command produced, what each outer tool result retained,
where truncation occurred, and what context usage the runtime reported. The
complete per-command and per-tool-result inventories are retained beside this
report in [commands.csv](./commands.csv) and
[tool-results.csv](./tool-results.csv).

## Operator result

The root ingest did not have a large-result problem. Its 74 tool results
returned 75,651 bytes of decoded content, no runtime truncation was observed,
and its final input occupied 23.9% of the available context window.

The isolated connection worker did have a large-result problem. Ninety-seven
shell commands produced 1,621,402 stdout bytes. Thirteen outer tool results
were truncated, including two results truncated once by `exec_command` and
again by the enclosing executor. Input reached 234,058 of 258,400 tokens
(90.6%), after which the worker compacted once.

The important distinction is therefore not “broad command allowed or
forbidden.” It is whether the agent can see the expected and actual result
volume at each layer before that volume consumes context. Broad discovery was
sometimes required by the connection workflow. Its cost was not visible while
the worker chose commands and result budgets.

## Observation boundary and provenance

The measured root session began with the request to ingest
`https://arxiv.org/abs/2608.26218`. The root observation has two scopes:

- `root_ingest_and_commit` ends immediately before the user asked to inspect
  the session for large tool results.
- `root_self_audit` starts with that inspection request and ends immediately
  before the user requested this retained report. Report-generation calls are
  excluded, avoiding an unbounded observer effect.

The two delegated-worker observations cover their complete session files.
All three sessions used Codex CLI `0.150.0`, model `gpt-5.6-sol`, reasoning
effort `max`, and a reported 258,400-token context window.

| Observation | Session ID | Retained input boundary | SHA-256 |
|---|---|---:|---|
| Root ingest-and-commit prefix | `01a05804-eb51-7831-b236-1414450a3ac9` | 541 JSONL records; 913,097 bytes | `7b0e4669d33c9dd647ebddcf21a0a0d41c2452d489f5d61edcc66962def5ccd8` |
| Root through self-audit | `01a05804-eb51-7831-b236-1414450a3ac9` | 759 JSONL records; 3,116,141 bytes | `726ececa78ad07ea07898295b3f7c886f7e9ec9dd36bf48ef9b831390382dab7` |
| Connection worker | `01a0580a-b41f-71b3-8108-5481164fb82f` | Complete file; 6,580,061 bytes | `c86d699122ca91a72f5f4e91b96fceb62b1835f57a77a70df1fb6e3369ae5523` |
| Draft worker | `01a0581f-f6a5-7902-a905-b119e0f17c5d` | Complete file; 945,047 bytes | `fdd62358da5a7b61a9301a6bfd539e0ccd78a0e4709e3e4c3b94c0895476920e` |

The source JSONL files are local Codex operational state and are not retained
in this repository. The CSV inventories retain the measurements and exact
call or command text needed to understand this report from a clean checkout.

## What was measured

The session records two distinct execution surfaces:

1. A `CommandExecution` event records each nested shell command and its
   captured `stdout` and `stderr`. `commands.csv` records the exact command,
   byte and line counts, exit state, duration, and JSONL record size.
2. A tool-call response records what the enclosing tool returned. For the
   executor used here, that response may contain output already truncated by
   `exec_command`, and the enclosing executor may truncate it again.
   `tool-results.csv` records both the serialized response field and the text
   decoded from its content blocks.

All byte counts are UTF-8 byte lengths taken from the retained fields. They are
not token estimates. A reported original token count appears only when the
runtime inserted an exact `Warning: truncated output` marker. The report keeps
all warning values in their printed order.

The decoded outer response is the closest session-visible measure of the text
returned toward the model. The transcript does not contain a per-item prompt
assembly receipt, so this report does not claim that every decoded byte entered
the next model request. Context usage comes separately from the runtime's
`token_count` events.

## Aggregate measurements

| Scope | Nested shell commands | Raw stdout | Outer tool results | Decoded result text | Results at least 10 KB | Runtime-truncated results | Context result |
|---|---:|---:|---:|---:|---:|---:|---|
| Root ingest and commit | 33 | 71,366 B | 74 | 75,651 B | 4 | 0 | Ended at 61,667 tokens (23.9%) |
| Connection worker | 97 | 1,621,402 B | 71 | 1,219,000 B | 42 | 13 | Peaked at 234,058 tokens (90.6%); compacted once; first later nonzero sample was 28,825 |
| Draft worker | 18 | 164,332 B | 15 | 165,128 B | 7 | 0 | Ended and peaked at 67,677 tokens (26.2%) |
| Root self-audit | 23 | 821,425 B | 27 | 126,981 B | 4 | 1 actual truncation | Ended at 118,064 tokens (45.7%) |

The connection transcript represents its one compaction twice: once as the
top-level replacement record and once as a completed UI event. The table counts
the operation, not the two records. Immediately before compaction, input was
234,058 tokens, of which 228,096 were reported cached. The first later nonzero
sample was 28,825 input tokens.

Transcript file size is not context size. The JSONL retains full command-event
stdout, outer tool results, messages, reasoning records, and UI events. Some
information therefore appears on more than one operational surface even when
only the bounded outer result is available to the next model call.

## Largest root ingest results

The root results were sizeable but bounded. None carried a runtime truncation
warning.

| Operation | Raw command stdout | Decoded outer result |
|---|---:|---:|
| Read the first 260 lines of `cp-skill-ingest` | 14,499 B | 14,546 B |
| Read `cp-skill-connect` | 12,234 B | 12,281 B |
| Read `cp-skill-snapshot-web` | 10,549 B | 10,596 B |
| Read PDF metadata and the first 180 extracted lines | 9,914 B | 9,961 B |
| Read the delegated drafting instruction | 9,517 B | 9,564 B |
| Read the snapshot type contract | 4,881 B | 4,928 B |
| Read the remainder of `cp-skill-ingest` | 2,862 B | 2,909 B |

The ingest skill was also present in the user-supplied context. Reading its
file again therefore duplicated roughly 17 KB of instruction text in this
particular harness execution, even though the read was required by the active
skill-loading rule.

## Truncation mechanics observed

Yes, tool calls in this session truncated results.

The nested `exec_command` calls accepted their own `max_output_tokens` values.
The enclosing executor had a separate 10,000-token default result budget when
no explicit executor pragma was present. Eleven connection results crossed the
outer limit only. Two crossed both limits.

For the largest double-truncated connection result:

1. The shell command produced 167,492 stdout bytes.
2. `exec_command`, configured for 30,000 output tokens, reported an original
   count of 41,873 tokens and truncated its result.
3. The enclosing executor then reported that the serialized intermediate had
   30,028 tokens and truncated it to its default 10,000-token budget.
4. The decoded outer result retained 40,156 bytes, including truncation
   notices and wrapper text.

The second double-truncated result followed the same shape: 133,002 raw stdout
bytes, warning counts of 33,251 and 30,027 tokens, and 40,156 decoded outer
bytes.

Across all thirteen truncated connection results, nested commands produced
951,516 stdout bytes and the decoded outer results retained 522,015 bytes.
Those are exact measurements of the two retained surfaces. Their 429,501-byte
difference is not an exact omitted-source count because decoded results also
contain executor headers and truncation notices.

The self-audit demonstrated inner truncation without a second outer
truncation. An unbounded `rg` matched a single enormous JSONL compaction record:
the command event retained 779,042 stdout bytes, `exec_command` reported
194,761 original tokens against its 8,000-token budget, and the outer response
retained 32,157 decoded bytes under its 10,000-token budget. Two other
self-audit results contained copied warning text while inspecting the logs;
they were not themselves truncated and are not counted as runtime truncations
in the aggregate table.

## Runtime-truncated result records

Full commands are in `tool-results.csv`; operations below are shortened only
for display.

| Scope and call line | Operation | Raw stdout | Decoded outer result | Outer / nested budget | Printed original token counts |
|---|---|---:|---:|---|---|
| Root audit 710 | Search raw JSONL for compaction and truncation text | 779,042 B | 32,157 B | 10,000 / 8,000 | 194,761 |
| Connect 71 | Read six collection and navigation heads together | 50,880 B | 40,155 B | 10,000 / 50,000 | 12,720 |
| Connect 95 | List every note title | 53,931 B | 40,155 B | 10,000 / 30,000 | 13,483 |
| Connect 143 | List note descriptions, first partition | 54,356 B | 40,155 B | 10,000 / 30,000 | 13,589 |
| Connect 149 | List note descriptions, second partition | 55,297 B | 40,155 B | 10,000 / 30,000 | 13,825 |
| Connect 173 | List source descriptions, first partition | 43,999 B | 40,155 B | 10,000 / 30,000 | 11,000 |
| Connect 179 | List source descriptions, second partition | 44,815 B | 40,155 B | 10,000 / 30,000 | 11,204 |
| Connect 230 | Search notes for context-pressure mechanisms | 61,700 B | 40,155 B | 10,000 / 30,000 | 15,425 |
| Connect 242 | Search notes for repeated-failure and stall mechanisms | 78,044 B | 40,155 B | 10,000 / 20,000 | 19,511 |
| Connect 248 | Search agent-memory reviews for context-management mechanisms | 167,492 B | 40,156 B | 10,000 / 30,000 | 30,028; 41,873 |
| Connect 260 | Search sources for model–harness and context comparisons | 133,002 B | 40,156 B | 10,000 / 30,000 | 30,027; 33,251 |
| Connect 326 | Read four agent-memory and agentic-system candidates in parallel | 124,720 B | 40,156 B | 10,000 / 10,000 each | 31,188 |
| Connect 335 | Read five source-ingest candidates in parallel | 40,222 B | 40,153 B | 10,000 / 6,000 each | 10,064 |
| Connect 419 | Read retained note candidates in parallel | 43,058 B | 40,154 B | 10,000 / 5,000 each | 10,913 |

The nearly constant 40,153–40,156-byte outer results are the observable effect
of the enclosing 10,000-token budget. Larger nested budgets did not make more
content visible once the outer budget bound.

## Exact impact and remaining observability gap

The report can establish exactly:

- every retained shell command and its captured stdout and stderr bytes;
- every outer call's requested outer and nested result budgets when present;
- every serialized outer result and decoded content-text byte count;
- every truncation warning and its runtime-reported original token count;
- sampled whole-request input, cached-input, and context-window token counts;
- the connection worker's compaction boundary; and
- the exact observed transcript prefixes through their SHA-256 values.

The current session format cannot establish exactly:

- how many tokens each individual tool result contributed to a later prompt;
- which decoded content blocks were included in each assembled model request;
- how many raw source bytes survived each layer when wrapper notices and
  serialization are mixed into the delivered result;
- semantic loss from head/tail truncation; or
- a reliable result-size estimate before an arbitrary shell command runs.

Whole-request `token_count` events include instructions, messages, reasoning,
call arguments, and tool results. The root's reported input grew from 61,667
tokens at the end of ingest to 118,064 at the end of the self-audit, but the
56,397-token difference cannot be attributed only to tool results.

Exact per-call context impact requires a runtime receipt that reports, for
each result, producer bytes and tokens, nested and outer budgets, delivered
bytes and tokens, truncation at each layer, and context occupancy after
assembly. A pre-call estimate may legitimately be `unknown` or `potentially
unbounded`; making that uncertainty visible would still improve agent choice
without prohibiting broad operations.

## Complete inventories

- [commands.csv](./commands.csv) contains all 171 nested shell command
  executions across the four measured scopes. Its byte columns describe the
  full operational event retained in the session.
- [tool-results.csv](./tool-results.csv) contains all 187 outer calls and
  results. It includes the exact call input, a compact operation label, outer
  and nested budgets, associated nested-command output totals, serialized and
  decoded result sizes, and all printed truncation counts.

The CSV row order follows session record order. `call_line`, `result_line`, and
command `line` identify the source JSONL record within the pinned observation.

## Production note

The measurements were extracted deterministically from the three local JSONL
sessions with Python standard-library JSON and CSV handling. The technical
interpretation and operator account were produced by Codex under the
repository's `AGENTS.md` and the `operator-brief` instruction. No external
source was used as evidence for the measurements.
