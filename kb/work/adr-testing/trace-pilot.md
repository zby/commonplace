# Local ADR-consultation trace pilot

## Outcome

One same-target temporal candidate survived adjudication: an author added a
collection-creation instruction, then consulted ADR 068 while removing one of
its requirements after operator intervention. The tool result proves a partial
ADR-body read, not a full ADR read. The consultation was relevant to the
revision and exposed a deliberately open choice. It does **not** establish that
earlier consultation would have prevented an error: the earlier requirement
followed the decision then in force.

- Sessions screened: **30** (15 pi, 15 Claude Code).
- Excluded ingestion/connect sessions: **19**; eligible sessions: **11**.
- Cases inspected in depth: **5**; same-target temporal candidates: **1**.
- Confirmed read-after-edit sequences: **1**, with partial body reading.
- Relevant post-edit consultation accompanied by observable intervention/revision:
  **1**, without establishing that the consultation caused the revision.
- Confirmed cases where earlier ADR reading would have changed a warranted
  initial choice: **0**. Confirmed fault or avoidable reversal: **0**.

This is a bounded preliminary scan, not a consultation-frequency estimate or
complete design-coverage test. No routing mechanism is recommended from it.

## Commission and method

Scan date: 2026-10-30. Repository HEAD during this probe:
`b82ba30b4bf45b63601fe2434e6e9ba900b53e41`. The new ingest and this workshop
were uncommitted; repository comparisons are supplementary to the historical
passages returned in the traces. Session files are mutable local evidence;
locators and retained excerpts support inspection but are not immutable archives.

The operator commissioned empirical testing of ADR consultation timing. Only
this file is owned by this scan; workshop framing and measurements belong to
the parent. Inputs were the two authorized native-session roots, this
repository, and [ADR routing](../adr-routing/README.md) with its
[trigger analysis](../adr-routing/trigger-analysis.md). The
[work contract](../COLLECTION.md) and [ADR type](../../reference/types/adr.md)
were read. No agents were launched and no code or contracts were changed.

### Exact selection and evidence criteria

1. Inventory both roots recursively by file extension without inspecting
   session bodies. Select the 15 most recently modified **top-level** `.jsonl`
   files in each root at the first selection on 2026-10-30. Do not replace an
   excluded session with an older one. Thus screening, including exclusions,
   stays within 30. Modification time selects recency, not session start time.
2. Exclude sessions identifiable from their opening task as ingest controllers,
   ingest drafters or connect workers. Exclude the live invocation; its runtime
   ID, `01a18dc3-c7f4-71b7-89d8-da7eb30e8bff`, was not among the selected files.
   An analysis controller is not automatically an ingestion worker.
3. Screen parsed actual assistant tool calls for retrieval involving
   `kb/reference/adr` and for edits/writes, including shell mutations. Mentions,
   filename listings, descriptions and search hits nominate cases only; they
   do not prove consultation. Inspect at most five promising sessions in depth.
4. Match actual calls to returned results in the native transcript. In Claude
   logs, exclude `api-request-blob` copies of messages, summaries and other
   non-message records from event chronology. In pi, use assistant `toolCall`
   and matching `toolResult` messages. Positions below are one-based JSONL
   physical line numbers, not tool-output line numbers. Multiple calls may
   occupy one event. No result means no proven successful action.
5. A temporal candidate requires a successful consequential edit/choice and a
   later returned ADR-body passage bearing on **that same choice**, not merely
   an older unrelated edit somewhere in a long conversation. Partial passages
   count only as partial consultation. Truncated output, a saved-result preview,
   or a range ending before EOF never proves full reading.
6. Adjudicate separately: chronology; relevance and observable intervention;
   whether the pre-action ADR actually ruled out the initial choice; and whether
   current instructions/contracts already supplied the rule. ADR creation or
   revision is not evidence of late consultation with an existing prohibition.
   A later ADR/amendment cannot be applied retroactively.

The initial mechanical screen also surfaced duplicated request records and
broad searches. These were discarded during adjudication, not counted as reads.
No raw session dumps, unrelated private content or credentials are retained here.

### Inventory and selected-session ledger

Local roots, abbreviated below:

- **P**: `/home/zby/.pi/agent/sessions/--home-zby-llm-commonplace--`
- **C**: `/home/zby/.claude/projects/-home-zby-llm-commonplace`

Inventory at scan start: P had 485 files: 435 `.jsonl`, 32 `.json`, 16 `.log`,
one `.ts`, one `.mjs`; 419 JSONL files were top-level. C had 962 files:
355 `.jsonl`, 404 `.json`, 153 `.txt`, 50 `.md`; 75 JSONL files were top-level.
Nested session/event files were inventoried but not screened. This avoids
counting pi audit-event copies as additional conversations and deliberately
leaves nested worker contexts unexamined.

P filenames are the timestamp prefix plus `_` plus the listed UUID plus
`.jsonl`. C filenames are the listed UUID plus `.jsonl`. Order within each root
is selection order. E = excluded ingest/connect work; S = screened only;
D = inspected in depth.

| Root | Timestamp prefix (P only) | UUID | Disposition |
|---|---|---|---|
| P | 2026-10-30T16-20-16-155Z | 01a18d9c-a69a-737f-bc67-c42802ef2d39 | E: ingest |
| P | 2026-10-30T16-34-36-482Z | 01a18da9-c742-7210-810e-73ce82985a79 | S: analysis controller |
| P | 2026-10-30T09-54-27-363Z | 01a18c3b-6da2-7689-aada-f20c2958c707 | D: Windows delivery/review |
| P | 2026-10-30T11-22-24-048Z | 01a18c8b-f1af-7099-93b8-b82b72da28fa | E: ingest |
| P | 2026-10-30T08-47-48-565Z | 01a18bfe-6954-7689-aada-f20bfc7b9aea | E: ingest |
| P | 2026-10-30T09-25-00-616Z | 01a18c20-7847-7567-99ae-9bc0b88c2941 | E: connect |
| P | 2026-10-30T09-21-54-529Z | 01a18c1d-a161-7266-a002-111f7fd9a358 | E: ingest draft |
| P | 2026-10-30T09-16-13-065Z | 01a18c18-6b88-7275-a226-63ef32f6e2e6 | E: connect |
| P | 2026-10-30T08-57-27-224Z | 01a18c07-3db8-734b-905f-916fa942b121 | E: connect |
| P | 2026-10-30T08-55-01-490Z | 01a18c05-0472-7712-9ad3-9a64ce74a2fe | E: ingest draft |
| P | 2026-10-30T08-49-09-475Z | 01a18bff-a563-7304-8e4a-df29d25372d6 | E: connect |
| P | 2026-10-30T07-59-38-829Z | 01a18bd2-514d-7689-aada-f208dccb125e | E: ingest |
| P | 2026-10-30T08-09-15-542Z | 01a18bdb-1e16-7048-99aa-cb49a0064175 | E: connect |
| P | 2026-10-30T08-06-34-812Z | 01a18bd8-aa3b-71c8-b557-c4efa50449eb | E: ingest draft |
| P | 2026-10-30T08-01-15-885Z | 01a18bd3-cc6d-7074-8d90-bca9bd70b491 | E: connect |
| C | — | db1c50ad-2993-4ee2-8110-2b2fff509d09 | D: review redesign, later source-tag query |
| C | — | d5553e8f-9851-4802-81fa-07bec2e06dac | S: prose discussion |
| C | — | b5dfe264-701d-4798-a0ac-de22cd32b83f | S: delivery probe |
| C | — | e6a2e385-c9aa-4ceb-bc44-82718aad783a | D: delivery and worker decision |
| C | — | fe218974-6c8e-4d0c-8053-eee080382698 | D: routine-conversion theory |
| C | — | 8d538dcc-e36e-42b6-8e26-1cff1f94287d | S: writing guidance |
| C | — | 40fbe559-f02e-4930-85c9-16b69c74a9b4 | E: ingest |
| C | — | 5768043c-e489-4b24-a5d5-b5a77547058b | E: ingest |
| C | — | 4ff50af5-d20a-4d48-aa91-06a12e01f881 | E: ingest |
| C | — | 1daf7fcd-a8d7-41e8-8ed5-01331851824a | E: ingest |
| C | — | d6352c78-40c8-4e30-ac3b-6374f9f8649d | S: research/design history |
| C | — | d6e64408-ca4a-4fd6-a981-5a85b2c46c3b | S: lifecycle/task discussion |
| C | — | b8f1292b-a9d5-4d32-b92d-f22460763faa | E: ingest |
| C | — | 098063c2-08de-48bc-b6eb-28030e13cb42 | D: long mixed session, collection work |
| C | — | 3f84a91b-8dc7-4dab-83ed-63c834088a2c | E: ingest |

The five depth selections favored actual body-retrieval commands near edits,
operator interventions, or plausible revision signals. They were not randomly
sampled. The research/design-history session was left at screening depth rather
than exceeding the five-case limit.

## Candidate 1: ADR 068 after adding a collection-creation requirement

**Locator:** C / `098063c2-08de-48bc-b6eb-28030e13cb42.jsonl`.
The relevant subtask was authoring `cp-skill-add-collection`, not the external
analysis that opened this long session.

| UTC on 2026-10-23 | Event lines | Actual evidence and interpretation |
|---|---|---|
| 12:32:31–32 | 4716–4717 | `Write` creates `kb/instructions/cp-skill-add-collection/SKILL.md`; result confirms file creation. Requirement: `Add a "Type eligibility" section: artifacts may use a global type ... or a local type under ...`. This is a shipped procedure requirement, not a speculative mention. |
| 12:37:29 onward | 4838, 4862, 4877 | Operator asks what the section means and what would happen without it. Author answers that validation does not read it and the writing skill ignores it. This intervention precedes the ADR lookup. |
| 12:46:26 | 4879 | Operator: `I think we should just delete it everywhere`. The direction to revise precedes consultation. |
| 12:46:51 | 4900–4901 | Actual `Bash` call: `sed -n 1,60p kb/reference/adr/068-collection-contracts-stop-enumerating-available-types.md`; returned result includes Context, Decision and alternatives. It ends at the Consequences heading: partial reading only. |
| 12:47:47 | 4948 | Shell replacement changes the skill to `Do not restate which types the collection may use; validation enforces that for every collection.` The same call appends the resolution to ADR 068. |
| 12:49:32–42 | 4966, 4975 | Commit result `6e80d139c Stop restating type eligibility in collection contracts`, followed by completion report, corroborates that the revision landed. |

The returned ADR passage, not just its filename, contains the deciding limit:

> Free choice left open: whether the derivation rule is stated per collection
> or stated once and referenced. Stated per collection for now, since
> `COLLECTION.md` is meant to be readable standalone; a shared statement is
> worth revisiting if the sentence proves identical across all of them.

### Independent adjudication

[ADR 068](../../reference/adr/068-collection-contracts-stop-enumerating-available-types.md)
is dated 2026-08-22, before the action. The historical wording above is present
in the actual returned result at event 4901; today's ADR also contains the
resolution this session added. The latter must not be treated as an earlier
constraint.

- **(a) Read-after-edit:** confirmed. Successful creation precedes actual
  partial-body consultation by about fourteen minutes.
- **(b) Relevant post-edit consultation with observable revision:** confirmed in
  the limited sense that the ADR bears directly on the revised requirement,
  and the later edit resolves its open choice. The operator had already ordered
  deletion; the read is not shown to have discovered the problem or caused
  the reversal.
- **Earlier reading would have mattered:** not established. The original ADR
  explicitly chose per-collection statements for standalone readability and
  left centralization open. The initial skill requirement followed that choice;
  earlier reading could have justified it rather than prevented it. Existing
  contracts also supplied that convention. There is no demonstrated violation.
- **(c) Unobserved reading:** no assertion that event 4900 was the first-ever
  consultation. This long session includes compaction, historical instructions
  and other contexts; prior delivery is not fully reconstructible here.
- **(d) Revision versus consultation:** event 4948 is ADR revision; it is not
  counted as a second consultation. Event 4901 independently proves that an
  existing decision was consulted before amendment.

This case tests the false-positive risk in treating any late ADR read plus
correction as proof of an avoidable miss.

## Four depth checks that did not qualify

### 2. Windows delivery: search hits are not an ADR read

**Locator:** P / timestamp `2026-10-30T09-54-27-363Z`, UUID
`01a18c3b-6da2-7689-aada-f20c2958c707`.

Events 30–31 create and confirm a Windows handoff. A later operator request at
43 starts review of two different commits. Event 54 searches ADRs 118/119 for
lock terms; result 55 returns no ADR passage and reports a missing wildcard
path. Event 56's executable probe and result 57 do expose a recovery defect
(`After run_lock: accepted corrupt/missing record`). That is real review
intervention, but **not proven ADR consultation**, nor evidence that the earlier
handoff author violated an ADR. Do not substitute the reproduced software
finding for the missing ADR-reading evidence.

### 3. Source-tag explanation: relevant contracts were already read

**Locator:** C / `db1c50ad-2993-4ee2-8110-2b2fff509d09.jsonl`.

Events 519–520 return the tag contract's exclusion of `sources` from membership.
Event 528 explains the design. Events 548–550 return selected ADR 089 passages,
including alternatives; this is partial consultation, not a full read. The
actual source edit at 572–573 subsequently adds `prose-readability` to
`domains`. Earlier workshop edits concerned review redesign, not this source
classification. Accordingly this is consultation **before** the relevant edit,
with the membership rule already available from a contract.

[ADR 089](../../reference/adr/089-tags-are-one-namespace-per-kb-with-heads-in-kb-tags.md)
now has a 2026-10-30 source-search amendment. Its newer allowance must not be
read backward into the earlier returned passages or treated as evidence of
fault in that answer. The historical transcript, not today's amended text,
anchors this check.

### 4. Worker route: amendment records a new operator choice

**Locator:** C / `e6a2e385-c9aa-4ceb-bc44-82718aad783a.jsonl`.

Events 777–778 return the ingest instruction's existing prohibition on launching
agent CLIs from the shell, plus selected ADR 118/119 material. Event 794 supplies
the operator's preference for harness sub-agents rather than headless-session
emulation. Events 822–823 return ADR 086's header and selected emulation text;
837–838 write and validate a new worker amendment; 849–850 confirm its commit
`c76e1fb37`.

This is **ADR revision**, not discovery that the agent had already violated the
new amendment. The earlier code edits at 691–692 addressed argument substitution,
not worker routing. [ADR 086](../../reference/adr/086-projects-read-the-library-from-the-installed-package.md)
previously anticipated emulation; the session's instruction already prohibited
shell emulation for ingest. The new amendment cannot govern earlier choices.

### 5. Exposure argument: correction without a demonstrated late read

**Locator:** C / `fe218974-6c8e-4d0c-8053-eee080382698.jsonl`.

Events 929/933 request narrow matching lines in ADR 026 while preparing an
exposure argument; filenames are checked at 950/952. The note addition lands
before commit confirmation at 965 (`de94e0e2d`). At 1222 the author accepts a
criticism that stale completeness suppresses search and zero exposure was an
overclaim; replacements at 1240 and commit result 1252 (`34cb6d431`) correct it.
The inspected correction sequence does not show a new ADR-body read after the
addition. It cannot establish late consultation.

Independent reading of [ADR 026](../../reference/adr/026-tag-readme-type-with-completeness-and-coverage-marks.md)
shows both the accelerator language and the consumer's skipped-search behavior.
That makes broader reading a plausible preventive hypothesis, but the trace
supports **insufficient inference from already available material**, not a
confirmed read-after-edit episode. Worker contexts were not inspected; absence
of a later parent read is not proof that nobody read the ADR.

## Limits and stopping point

The formats support actual call/result chronology, but not exhaustive knowledge
of what a model previously received or retained. Compaction summaries, nested
workers, saved-result previews and request-record duplicates make mention-based
counts particularly misleading. Full reading was not proved for the retained
temporal candidate. Decisions made by other agents cannot be attributed to the
current session merely because their commits are reviewed there.

The five-case depth budget is exhausted. No inaccessible-format blocker
prevented this preliminary result; the blocker to a stronger causal claim is
**missing evidence that a pre-existing decision required a different initial
choice**. A larger or targeted follow-up would need additional authorized
sessions and historical instruction delivery, not stronger wording about these
five cases. The scan does not estimate missed-consultation prevalence or test
the ADR-routing workshop's complete design space.
