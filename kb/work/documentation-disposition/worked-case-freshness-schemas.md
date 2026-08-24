# Worked case: `freshness-schemas.md`

Executed and retired 2026-08-24. The third artifact taken through the full
disposition procedure.

## Result

**Retired. Exact JSON belongs to the live serializers and parsers; the useful
cross-command semantics belong to freshness architecture.** The 3,017-byte,
124-line page was neither generated nor checked against the executable
interface. A reader requiring exactness had to verify it against source anyway.

This case differs from `commands.md`. A command catalogue answers a discovery
question before the reader knows a command name. The schema page answered only
questions whose vocabulary already names `status`, `ack`, `retire`, or one of
their JSON fields. Those terms select the owning source symbols directly.

## Consumption events and dispositions

| Unit | Consumer question | Required reliability | Recovery result | Source grain | Document grain | Recurrence and saving | Maintenance form | Disposition | Retrieval path |
|---|---|---|---|---|---|---|---|---|---|
| Target identity and canonical key order | What identifies one registered target? | exact | recoverable | `keys.py` plus `_target_key_json()` | one example and one sentence | rare; prose saves one source hop | unchecked authored copy | omit | `commonplace-source`; `freshness/keys.py`, `freshness/transitions.py` |
| Status envelope, target rows, and changed-input rows | Which fields can status JSON contain? | exact | recoverable | `render_status_json()`, `_target_to_json()`, `_changed_input_to_json()` | three examples | one serializer already groups the answer | executable serializer | omit | `freshness/status.py` |
| Ack manifest and selected-input behavior | What must acknowledgement consume, and what races does it reject? | exact fields; semantic transition | mixed | CLI parser plus `parse_input_observation()` and `ack_target_inputs()` | two examples and three sentences | source fans out, but no repeated integration was found | fields in code; invariant in architecture | split | `cli/freshness_ack.py`, `freshness/transitions.py`, freshness architecture |
| Retire manifest and idempotence | How is one target retired? | exact | recoverable; recipe already operative elsewhere | CLI parser plus `retire_target()` | one example and one sentence | retirement instruction already carries the only production recipe | executable parser and instruction | omit | `cli/freshness_retire.py`; `instructions/retire-artifact.md` |
| Exit classes and codes | What does a status exit mean? | exact code; semantic meaning | mixed | `_exit_class()` and `status_exit_code()` | one table | small source unit; semantic meaning useful across commands | executable code plus architecture | split | `freshness/status.py`; freshness architecture |
| Freshness versus truth | Does stale mean the reviewed result is false? | conceptual | already recorded more strongly | freshness mechanism as a whole | implicit in status labels | high consequence, low volume | authored architecture | consolidate | opening and selection sections of freshness architecture |
| Ack revision/hash checks and evidence preservation | What makes acknowledgement safe, and what survives? | architectural invariant | partly unique | transition implementation | dispersed across two sections | useful to changers and workflow authors | authored architecture beside transition table | relocate | freshness architecture, committed before retirement |

## Recovery experiment

The source pass began with terms available to a consumer before reading the
candidate page:

| Starting terms | Selected live unit | Answer recovered |
|---|---|---|
| `commonplace-freshness-status --json`, `schema`, `targets` | `freshness/status.py`: `render_status_json()` and its two helper serializers | complete output field set and optional `diff` behavior |
| `commonplace-freshness-ack --input`, `selected_inputs` | `cli/freshness_ack.py`, then `parse_input_observation()` and `ack_target_inputs()` | top-level manifest, nested observation fields, CAS, live-hash checks, omission behavior |
| `commonplace-freshness-retire --input`, `schema` | `cli/freshness_retire.py`, then `retire_target()` | complete manifest and already-absent behavior |
| `fresh`, `stale`, `error`, exit | `freshness/status.py`: `_exit_class()` and `status_exit_code()` | status classification and exit mapping |

The ack path fans out across two files, so source does not win by a
one-unit retrieval-floor comparison. The cache still failed the value test:
repository search found no recurring consumer of the full ack contract, and an
exact answer from unchecked prose still required source verification. Creating
a formal generated schema would add a new shipped interface without a consumer
that needs it.

## Drift exposed by comparison

Two statements demonstrated why the page could not safely call itself
canonical:

- It specified `content_sha256` as 64 lowercase hexadecimal characters. The
  parser checks length and normalizes case; the later live-hash comparison, not
  that stated field constraint, rejects a non-matching value.
- It described omitted `selected_inputs` as taking all changed inputs from a
  paired status result. The transition actually re-resolves both registered
  inputs at execution time. Supplying selected inputs is what carries observed
  hashes forward as intent checks.

Neither discrepancy caused an observed failure, but both change what an exact
consumer should infer. Checking the prose against code would merely maintain a
second representation of an interface that has no demonstrated independent
consumer.

## Unique content moved first

Freshness architecture already said that the mechanism records accepted input
snapshots and does not adjudicate truth. It also recorded evidence preservation
and the transition owners. One cross-command invariant was incomplete there:
how acknowledgement combines revision CAS, optional observed hashes, live
re-resolution, and evidence preservation. That invariant was added and
committed separately as `10c0675a` before the schema page was removed.

Exact exit meanings were then kept compactly in the architecture selection
section. Exact fields and validation route to the live status serializer,
acknowledgement parser, retirement parser, and input-observation parser.

## Retirement

The reference page was deleted. Current reference routes now point semantic
questions to `freshness-architecture.md` and exact field questions to source.
Dated artifacts in the original freshness workshop retain their history but no
longer link to the deleted page. Its published URL redirects to freshness
architecture. A read-only store query found no baseline whose input path was
`kb/reference/freshness-schemas.md`, so no operational state needed retirement;
unrelated missing baselines were left untouched.

## Next

`review-architecture.md` is the next forcing case. Its module inventory and
exact schema descriptions should face the same recovery test, while
cross-module invariants and canonical-state boundaries may survive.
