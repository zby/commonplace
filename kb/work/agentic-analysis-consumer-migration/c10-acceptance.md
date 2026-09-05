# C10 acceptance: main-review classification audit

Accepted on 2026-09-05 for the procedure migration and bounded checks below.
The preceding production pilot and publication fix are committed in
`f586fb1d`; this C10 migration and its follow-ups are recorded in Git history.

## Consumption and correction boundary

The [revised procedure](../../instructions/refresh-agent-memory-review-taxonomy.md)
reads complete retained main results through the existing strict reader, then
checks whether classifications preserve the recorded mechanisms. It returns a
diagnosis with input and method identities. It no longer patches legacy review
prose, moves observation dates forward or refreshes the trace-learning survey.

Repository search found no automated caller, skill projection or CLI entry for
this instruction. Mentions in the bulk-operations and self-improvement workshop
inventories are descriptive. The existing path remains the manual invocation
point. The conditional `analyse-agentic-system` interface already accepts the
source identity, revision, target boundary and issue to inspect, so no caller or
callee change was needed.

The audit distinguishes supported classifications, evidence limits,
classification defects and gaps in the shared method. An existing rule can
already cover an application error; regeneration then uses that rule unchanged.
When corrections are commissioned, the producer performs fresh source
inspection in a new run and publishes normally. The old result supplies the
diagnosis, not replacement evidence. These checks exercised diagnosis and
routing; they did not execute a production correction or source refresh.

## Selected input and method identities

The explicit population is one system: [Apache Maka's public main
review](../../agentic-systems/reviews/apache-maka.md) and its [exact retained
result](../../reports/retained/agentic-system-analysis/AAS-2026-09-05-apache-maka-01/result.md).
Run: `AAS-2026-09-05-apache-maka-01`. Source: `https://github.com/apache/maka`.
Recorded revision: `ece69ab3e7a1629a6073831005711d8aa7160ca4`.
Cutoff: 2026-09-05. Evidence tier: `code-grounded`.

The comparison scope covers built-in retained RuntimeEvents and checkpoints,
local `MEMORY.md`/`PENDING.md`, atomic MemoryItems, and their keys, provenance and
extraction bookkeeping. Goal/skill control material, offloaded tool artifacts,
arbitrary project files, external extensions and transient replay arrays are
excluded. The audit read the full result's source register, shared records,
lenses, reconciliation and limits, alongside its comparison profile.

SHA-256 identities at initial and final checks:

| Input | SHA-256 |
|---|---|
| Public main review | `cf2f80113c2c21074cdc07e149b9a9cb3a764f0ff5b6fb39728deee633eac76c` |
| Retained exact result | `fcd16d145d4ee6730eedab994478c8a320fd98f79123dd2df145c3cb6b8d3c18` |
| `kb/instructions/refresh-agent-memory-review-taxonomy.md` | `b384fd14ab74bb18fbac62bedd9f3bc28c8f01f57a8282017b963974c5080baf` |
| `kb/instructions/analyse-agentic-system/SKILL.md` | `7dcb69c3f9d29d940f6d3f627949819e89a6c493340e419e3418ec58d6d390ba` |
| `kb/types/agentic-system-analysis-result.md` | `df54e009e603fa9718c478360134160b39bff128e356b832b42ebb43209ce7b0` |
| `kb/types/agentic-system-analysis-result.schema.yaml` | `2c330378e5ff6a5e9f8810c30338b3455aaa1f7a6b3d5ce483626dc5162049d9` |
| `src/commonplace/lib/systems_matrix.py` | `3346be5e1b31ce49921a9fe9697fd810b15b8758794928e3326fa6b415d866e0` |
| `kb/notes/definitions/representational-form.md` | `2779941570fe6726a2832965ce711df45b22e515282443853803a623a7eee5a0` |
| `kb/notes/definitions/behavioral-authority.md` | `9c25df74af0e2df7dae032286300537b7e29b71ddf71b5932fdd3994d46809c9` |

## Bounded live diagnosis

The applicable [comparison contract](../../types/agentic-system-analysis-result.md#memory-comparison-fields)
requires a known set to cover the declared scope and use the weakest basis
supporting that union. Missing evidence remains explicit. The following are
analytical judgments from the retained records, not conclusions computed by the
structural reader.

| Classification | Disposition and support in the retained result |
|---|---|
| Storage substrate | **Supported.** Files and SQLite preserve the distinct stores in OBJ-1–OBJ-4. |
| Representational form | **Evidence limit.** The opaque provider checkpoint in OBJ-4 prevents a complete aggregate; the result keeps known natural-language and symbolic parts explicit without guessing its encoding. |
| Lineage | **Evidence limit.** Opaque, replacement and import provenance prevent a complete scoped set. Established extraction routes do not decide every object's lineage. |
| Behavioral authority | **Supported.** BAP-2–BAP-4 distinguish advisory payload from validation, routing and enforcement in scoped metadata and write controls. Authority is attached to consumers and operative parts. |
| Read-back direction | **Supported.** RTE-8/RTE-13 wire push routes; RTE-11 affords a pull API and ABS-1 records no production caller. The union correctly uses the weaker `afforded` basis. |
| Trace learning and its dependent axes | **Supported within the recorded limit.** RTE-12/RTE-13 wire automatic text checkpoints into later task continuation, supporting per-task online learning from the event stream. This does not establish cross-task consumption of atomic SQLite memory. Opaque distilled form remains not determinable. |
| Curation and faithfulness | **Evidence limit.** Recorded individual operations do not decide the full curation set. Faithfulness testing remains uninspected; the audit cannot turn that into either a tested dependence claim or an assertion that no such test exists. |

No classification defect was established within this retained boundary. That
finding does not establish current upstream behavior, operational success or
coverage beyond the selected system. No regeneration was required by the live
diagnosis, and no generated result or public review was changed.

## Procedure exercise and rejection checks

The Python preflight was extracted from the instruction and executed with the
explicit Maka path. Its output recorded both file hashes and the full population
identity. The project interpreter ran the snippet because the sandbox's `uv`
launcher could not acquire its required capabilities.

| Case | Observed result |
|---|---|
| Live explicit Maka selection | Accepted; final population and input hashes matched the initial check. |
| Isolated copy of the same retained evidence and reader method inputs | Accepted without a legacy corpus or local run-state directory. |
| Explicit Pond; default all-generated population | Both blocked on Pond's missing or mismatched retained-result metadata; no silent subset selection. |
| Explicit legacy review path | Rejected as not a main-review path. |
| Missing copied retained result | Blocked on the absent file. |
| Changed retained bytes with unchanged public digest | Blocked on retained-result SHA-256 mismatch. |
| Public-review drift after initial load | Final `recheck` rejected the changed input; current conclusions must be withheld. |

Two additional temporary copies retained the original canonical records but
introduced profile contradictions. Their public result hashes were updated so
that the semantic check, rather than a digest error, was exercised:

| Synthetic change | Structural reader | Audit diagnosis and correction route |
|---|---|---|
| Replace the known storage set with only `files` | Accepted | **Classification defect:** omits SQLite parts in OBJ-1, OBJ-2 and OBJ-4 while retaining file-backed OBJ-3. The existing complete-set rule covers this; send the omission to a new producer run. |
| Upgrade aggregate read-back basis from `afforded` to `wired`, claiming wired task-model pull | Accepted | **Classification defect:** contradicts RTE-11 and ABS-1. Wired push in RTE-8/RTE-13 cannot upgrade the pull route. The existing weakest-basis rule covers this; send the contradiction to a new producer run. |

These are synthetic diagnostic cases, not revised claims about Maka. Their
defect dispositions were assigned by reading support, not detected by code.
Both route to source inspection under the existing method; neither justifies
editing a production profile in place.

The temporary exercise report is `/tmp/commonplace-c10-yweicqwg/checks.json`.
The observations needed for acceptance are recorded here; that temporary file
is not a durable evidence dependency. Real review/result bytes and all recorded
method hashes matched at the final check.

## Acceptance and remaining scope

The changed instruction, this record and the queue passed
`commonplace-validate` with no failures or warnings; `git diff --check` passed.
No executable implementation changed, so this Markdown migration exercised the
reader directly rather than adding tests or repeating pytest. The preceding
committed pilot passed all 723 tests.

C10 is done for its active procedure and bounded acceptance. The wider corpus
has not been audited: all-generated selection still blocks on Pond. Quote
grounding is the next independent procedure, C11; mandatory legacy publication
remains for C12/C14 to resolve.

The subsequent [oh-my-pi session-report audit](./c10-oh-my-pi-audit.md) exercises
the diagnostic on a second published result and establishes two semantic
defects despite structural success. That follow-up preserves this initial
Maka trial's evidence boundary and records the required source regeneration
separately.

The later [producer-check exercise](./producer-check-acceptance.md) applies the
clarified method independently to both inputs. It finds task-horizon and
learning-branch accounting gaps in Maka that this initial bounded audit did
not establish. Affected learning claims now require regeneration or supported
uncertainty; the original structural-reader checks still pass.
