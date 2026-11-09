---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Memory mechanisms of the instruction-only recall skill of Parcha-ai/parcha-skills: pull retrieval and bounded reads of host transcripts, Brain capture and skill-ify; engine and Brain declared only"
run-id: AAS-2026-11-05-parcha-skills-d5ad184aa4af-01
source-identity: "https://github.com/Parcha-ai/parcha-skills"
reviewed-boundary: "c82883b15e5e8f02483bee513b3c8dcac48e3c9e"
---

# Recall (parcha-skills) memory report

## Boundary and evidence

**Subject.** The `recall/` skill package of SRC-1 at
`c82883b15e5e8f02483bee513b3c8dcac48e3c9e`, as frozen by the boundary
(`complete artifact, partial loop`, `doc-grounded`). The package is
instructions only. Its memory role is that of a retrieval procedure: a host
model reads it and then pulls material from retained session history into its
own context. The package itself stores nothing.

**Memory scope chosen from the runtime routes.** Included:

- retained material the procedure reads: raw host transcripts
  ([RT-OBJ-session-transcripts](runtime.md#rt-obj-session-transcripts)), the
  engine index ([RT-OBJ-session-index](runtime.md#rt-obj-session-index)),
  central Brain content ([RT-OBJ-brain-record](runtime.md#rt-obj-brain-record),
  [MEM-OBJ-brain-synced-content](#mem-obj-brain-synced-content));
- retained material the procedure writes or causes: Brain captures, generated
  skills ([RT-OBJ-generated-skill](runtime.md#rt-obj-generated-skill)), export
  cursors ([MEM-OBJ-export-cursor](#mem-obj-export-cursor)), and the index
  build it starts;
- withdrawal: `recall_forget`, host retention deletion as surfaced by `doctor`,
  the `index --rebuild` consent rule;
- working-context control the procedure exercises: bounded windows, search-hit
  summaries, conditional reference loading, receipts as references.

Excluded: the host `MEMORY.md` facility, which the skill description routes
away from (it is a host surface, not shipped here); the host's own compaction
and context management; the internals of `recap` and `precap` beyond their
Recall call sites (boundary exclusion; prevents attributing their evidence
handling to Recall).

> Not for searching code (use grep on the repo) or for facts already in MEMORY.md.
> --- `recall/skills/recall/SKILL.md`

**Evidence layers.** Direct reads in this member: all eight tracked files under
`recall/` (listed with `git ls-tree` at the reviewed commit), the Recall call
sites in `recap/skills/recap/scripts/recap.py` (lines 92–240) and
`precap/skills/precap/SKILL.md` (lines 60–84). The skill text is
`implementation` evidence for the agent-side procedure only; it establishes the
request to the model, not compliance. Every statement about engine ingest,
ranking, redaction, index lifetime and Brain storage is `doctrine/design`.
No observed run or causal experiment exists, so delivery, activation and
benefit are unobserved for every route. Supplied runtime findings are cited as
`RT-` records and are not re-derived.

**Access gaps.** The engine (`recall.py`), its SQLite index and the Brain
service are absent from SRC-1
([RT-ABS-engine-code](runtime.md#rt-abs-engine-code)). This prevents any
implementation-level conclusion about how derived memory is produced, what it
contains, how it is ranked, and whether it outlives its sources.

**Coverage.**

| Memory operation or entry | Source path | Covering records | Evidence / conclusion prevented |
|---|---|---|---|
| Host transcript production | host (excluded) | [RT-OBJ-session-transcripts](runtime.md#rt-obj-session-transcripts) | Host-owned; content (thinking, secrets) and format uninspected |
| Index ingest (`index`, detached cold-start build) | `recall/skills/recall/SKILL.md` | [RT-RTE-index-maintenance](runtime.md#rt-rte-index-maintenance), [RT-RTE-cold-scan](runtime.md#rt-rte-cold-scan), [RT-CLM-ingest-redaction](runtime.md#rt-clm-ingest-redaction) | Declared only; ingest filter, incremental logic, deleted-source handling prevented |
| Indexed search with `WHY` | `recall/skills/recall/SKILL.md`, `recall/skills/recall/references/query-cookbook.md` | [RT-RTE-local-search-read](runtime.md#rt-rte-local-search-read), [MEM-OBJ-search-hit](#mem-obj-search-hit), [RT-CLM-evidence-gate](runtime.md#rt-clm-evidence-gate), [MEM-CLM-empty-no-answer](#mem-clm-empty-no-answer) | Agent procedure direct; ranking and gate declared |
| Bounded `show` reads (`--around`, `--tail`, `--prompts`) | `recall/skills/recall/SKILL.md` | [RT-RTE-local-search-read](runtime.md#rt-rte-local-search-read), [RT-RTE-outcome-playbooks](runtime.md#rt-rte-outcome-playbooks) | Window sizes declared; parsing uninspected |
| Cold raw scan | `recall/skills/recall/SKILL.md` | [RT-RTE-cold-scan](runtime.md#rt-rte-cold-scan) | Direct procedure; transcript content host-owned |
| Query-free related lookup | `recall/skills/recall/SKILL.md` | [RT-RTE-related-sessions](runtime.md#rt-rte-related-sessions) | Ranking declared only |
| Remote Brain read | `recall/skills/recall/references/central-brain.md` | [RT-RTE-remote-brain-read](runtime.md#rt-rte-remote-brain-read) | Service absent; visibility and sync prevented |
| Brain capture and forget | `recall/skills/recall/references/central-brain.md` | [RT-RTE-brain-capture](runtime.md#rt-rte-brain-capture) | Service admission and deletion semantics prevented |
| Brain sync, import, collectors, connectors | `recall/skills/recall/SKILL.md` | [MEM-RTE-brain-ingest](#mem-rte-brain-ingest), [MEM-OBJ-brain-synced-content](#mem-obj-brain-synced-content) | Named only; triggers, consent and content prevented |
| Skill-ify write | `recall/skills/recall/SKILL.md` | [RT-RTE-skillify-admission](runtime.md#rt-rte-skillify-admission) | Direct procedure; external creator uninspected |
| Generated-skill read-back | host loader (excluded) | [MEM-RTE-generated-skill-load](#mem-rte-generated-skill-load), [MEM-ABS-skill-provenance](#mem-abs-skill-provenance) | Host selection uninspected |
| Session export and relations | `recall/skills/recall/SKILL.md`, `recap/skills/recap/scripts/recap.py` | [RT-RTE-session-export](runtime.md#rt-rte-session-export), [MEM-OBJ-export-cursor](#mem-obj-export-cursor), [MEM-CLM-cursor-content-free](#mem-clm-cursor-content-free) | Producer absent; consumer checks are `recap`'s |
| Precap search consumer | `precap/skills/precap/SKILL.md` | [RT-BAP-retrieved-sessions](runtime.md#rt-bap-retrieved-sessions) (annotated) | Precap's later use excluded |
| Retention watchdog and `--rebuild` consent | `recall/skills/recall/SKILL.md` | [RT-RTE-index-maintenance](runtime.md#rt-rte-index-maintenance) (annotated) | Index fate after source deletion prevented |
| Automatic push or hook injection | `recall/` (all eight files) | [MEM-ABS-push-hook](#mem-abs-push-hook) | Bounded absence within the package; host hooks out of scope |

## Core ideas

**Retrieval by pull, with the evidence line as the selector the model reads.**
Every route that reads retained session material (transcripts, index, Brain
records, export pages) is requested by the foreground model or a consuming
skill's code through a tool or shell call. No shipped mechanism pushes that
material into context ([MEM-ABS-push-hook](#mem-abs-push-hook)). The one
exception in direction is the read-back of generated skills
([MEM-RTE-generated-skill-load](#mem-rte-generated-skill-load)). There the
host's skill loader decides delivery, so its direction is host-dependent and
uninspected, not established as model-requested. Selection has two stages: the
absent engine ranks and gates candidates, then the model is told to choose by
the `WHY` line rather than by rank
([MEM-OBJ-search-hit](#mem-obj-search-hit)). The design premise is that the
engine's match explanation, not its rank, is the trust signal the model should
act on.

**Bounded windows as the context budget.** The skill's main context-engineering
mechanism keeps most of a session out of the window: read only a ±3-turn
window, the last 30 turns, or the user prompts, never the whole file.

> Query the index and read only the best-supported session instead
> of searching entire transcripts.
> --- `recall/skills/recall/SKILL.md`

The budget is expressed in turns and command flags (`--limit N`, `-C3`), not
tokens. Nothing measures the context the reads consume. The remote route is
less bounded: it follows a record's continuation cursor until `complete`, and
`recall_exec` fetches full documents.

**Raw traces are the retained memory; derived memory is the absent index.**
The material that later sessions consume is the host's own transcript record
of earlier work. Recall adds an index and summaries over it but, as declared,
no derived knowledge layer: no extracted facts, summaries persisted for reuse,
or ranking feedback. Two exceptions produce durable derived material, both
model-authored and user-triggered: Brain capture of "selected decisions or
findings", and skill-ify. Neither retains the reasons for what it keeps, and
only capture returns a receipt.

**Source trust is assigned by evidence form, not by source.** Identifiers and
exact phrases count as strong evidence; generic word matches are weak; search
snippets are only pointers; only opened receipts may be cited. Retrieved
content is never marked as more or less trustworthy by origin (own session,
other harness, imported ChatGPT export). The skill warns that lexical
adjacency can return sessions about work that never happened.

> A query about work that never happened can still return lexically-adjacent
> sessions.
> --- `recall/skills/recall/SKILL.md`

**Receipts as references in a by-value window.** A session path, a
`recall://` receipt or a `logical_document_id` in context is a followable
reference to retained material outside the window. The model can re-open it at
a different offset. This is where the classical stack-frame lens breaks:
host subagent transcripts are not discarded when the frame pops. They persist
as their own indexed sessions, and their path names the parent, so a later
invocation can reload what the caller never received.

> Subagent and workflow transcripts are indexed as their own sessions
> --- `recall/skills/recall/SKILL.md`

**Editing and adoption surfaces.** Retained material can be changed only by
adding Brain records, forgetting exact receipts, rebuilding the index with
consent, or writing a new skill. Transcripts are host-owned and never edited
by Recall. No route revises or annotates an existing retained item.

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-search-hit

Label: Search hit row

- Source-native identity: one row of `search` output: "ranked sessions with
  date, cwd, slot, branch, a matched snippet, and `WHY` it matched"; with
  `--paths`, a bare file path.
- Representational form: symbolic fields (path, date, cwd, slot, branch) plus
  a natural-language snippet and a `WHY` explanation of matched terms;
  consumed by model interpretation.
- Storage substrate: engine stdout in the current tool result; not persisted.
- Lineage: derived at query time by the absent engine from
  [RT-OBJ-session-index](runtime.md#rt-obj-session-index); its relation to the
  underlying transcript is a readable display summary of an opaque ranking.
- Consumers and authority: the host model, which the skill tells to decide
  relevance from `WHY` and to treat generic-word matches as weak. It is a
  selection input, not citable evidence in the remote route.
- Identity comparison: closest supplied records are
  [RT-RTE-local-search-read](runtime.md#rt-rte-local-search-read) (whose
  immediate return lists these fields) and
  [RT-CLM-evidence-gate](runtime.md#rt-clm-evidence-gate); no supplied object
  declares the hit itself. Distinct identity.
- Evidence: SRC-1, `recall/skills/recall/SKILL.md`,
  `recall/skills/recall/references/query-cookbook.md` (procedure:
  `implementation`; row content: `doctrine/design`).

> Treat search snippets as pointers to evidence.
> --- `recall/skills/recall/references/central-brain.md`

#### MEM-OBJ-export-cursor

Label: Export cursor

Part of: [RT-OBJ-session-export](runtime.md#rt-obj-session-export)

- Source-native identity: `next_cursor`, an "opaque" continuation token for
  `session-export --cursor`.
- Representational form: symbolic opaque token; access metadata, not content.
- Storage substrate: "owner-private under `~/.recall`" on local disk, as
  declared.
- Lineage: produced by the absent engine per export page.
- Consumers and authority: the next `session-export` call, in practice
  `recap`'s page loop, which requires a non-empty cursor on every incomplete
  page. It has addressing authority only.
- Separate declaration reason: it persists across calls on disk while the
  pages go to stdout, and it carries a separate content-free claim
  ([MEM-CLM-cursor-content-free](#mem-clm-cursor-content-free)).
- Evidence: SRC-1, `recall/skills/recall/SKILL.md` (`doctrine/design`);
  `recap/skills/recap/scripts/recap.py` (consumer `implementation`).

#### MEM-OBJ-brain-synced-content

Label: Synced and imported Brain content

Part of: [RT-CMP-central-brain](runtime.md#rt-cmp-central-brain)

The parent is a component (the service) and this object is part of its
storage. The relation is containment of retained content within the service,
not a kind match.

- Source-native identity: Brain content arriving by sync from local Recall,
  "consented ChatGPT-export import", "a Cowork collector" and "pull
  connectors", as opposed to deliberate `recall_capture` records.
- Representational form: uninspected — the service and its schemas are absent.
- Storage substrate: private Brain service storage; uninspected.
- Lineage: from local session history (sync) and external systems (imports,
  connectors); provenance and redaction for these paths are not stated.
- Consumers and authority: later `recall_search` / `recall_show` reads in any
  configured session, as evidence the model may cite once opened.
- Identity comparison: [RT-OBJ-brain-record](runtime.md#rt-obj-brain-record)
  is scoped by the runtime to records "created by `recall_capture`"; this
  object has different lineage and admission. Distinct identity.
- Evidence: SRC-1, `recall/skills/recall/SKILL.md` (`doctrine/design`).

> Recall can sync into a private central Brain service that provides deliberate
> memory writes, cross-device search, consented ChatGPT-export import, a Cowork
> collector, pull connectors, and MCP capture.
> --- `recall/skills/recall/SKILL.md`

### Routes

#### MEM-RTE-brain-ingest

Label: Brain sync and import

- Endpoints: local session history and external sources (ChatGPT export,
  Cowork, pull connectors) → [MEM-OBJ-brain-synced-content](#mem-obj-brain-synced-content).
- Progression: named only; the skill gives no command, trigger or schedule.
  "The service is off unless explicitly configured."
- Owner: the central Brain service and its private setup; no agent step in
  the shipped skill.
- Context/state/action effects: writes remote retained content; no
  model-visible effect at write time.
- Identity comparison: closest supplied route is
  [RT-RTE-brain-capture](runtime.md#rt-rte-brain-capture), which covers
  user-requested capture only. This route has no model authorship and a
  different consent basis ("consented" import, configuration for sync).
  Distinct identity.
- implementation conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: uninspected — no shipped command returns from these paths.
- Later read-back: ingested content becomes searchable through [RT-RTE-remote-brain-read](runtime.md#rt-rte-remote-brain-read), including on other devices, as declared.
- Delegated visibility: uninspected — service visibility and permission rules are absent from SRC-1.
- Selection predicate: uninspected — what is synced or imported, and with what filtering, is not stated.
- Invalidation or expiry: uninspected — whether `recall_forget` or local deletion reaches synced content is not stated.
- Activation or effect: uninspected — no run evidence.
- Evidence limits: only the capability list is in SRC-1; admission control, redaction and provenance on these paths are unestablished.

#### MEM-RTE-generated-skill-load

Label: Generated skill read-back

- Endpoints: [RT-OBJ-generated-skill](runtime.md#rt-obj-generated-skill) on
  disk → host skill loader → host model in a later session.
- Progression: skill-ify writes a standard `SKILL.md` package → a later
  session's host matches its description → the body enters context as
  instructions.
- Owner: the host skill loader (excluded host); the package defines only the
  write.
- Context/state/action effects: places model-distilled instructions derived
  from a prior session's trace into a later model's context with instruction
  force.
- Identity comparison: [RT-RTE-skillify-admission](runtime.md#rt-rte-skillify-admission)
  names this consumer in its later read-back field but declares the write;
  [RT-BAP-generated-skill](runtime.md#rt-bap-generated-skill) gives the
  authority path. This route is the read-back leg those records point to,
  with a different trigger (host matching) and owner. Distinct identity;
  possible overlap with the BAP noted under Integration issues.
- implementation conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: inapplicable — the route delivers instructions to a later session, not a return to the writer.
- Later read-back: the generated package's text reaches later sessions whenever the host selects it.
- Delegated visibility: inapplicable — no delegation in this route.
- Selection predicate: host skill matching on the generated description; host behavior outside SRC-1.
- Read-back direction: host-dependent and uninspected. Whether the host injects the package on a description match, lists it for the model to invoke, or loads it only on an explicit user command is host behavior outside SRC-1. The route is not established as model-requested pull.
- Invalidation or expiry: none stated; removal is manual file deletion.
- Activation or effect: capability change for later sessions; activation unobserved.
- Evidence limits: the host loader and the external skill creator are outside SRC-1; the route is afforded by the documented Agent Skills format, not wired by the package.

### Claims

#### MEM-CLM-empty-no-answer

Label: Empty output is a no-answer

Claimed operation: in scripted use, empty `search --paths` stdout is a
"confident no-answer" and a non-zero exit is engine failure. Source: SRC-1,
`recall/skills/recall/references/query-cookbook.md` (`doctrine/design`).

> Empty stdout = confident no-answer. Non-zero exit = the engine itself failed.
> --- `recall/skills/recall/references/query-cookbook.md`

The same package's `SKILL.md` says empty output "does not prove the work never
happened", and the pi gotcha says a cold result does not prove no pi session
exists. The claim is reconcilable only as "the engine found nothing above its
gate". A scripted consumer reading the cookbook literally would treat absence
in the index as absence of work. That conflicts with the index's declared
exclusions (thinking blocks, pi sessions, redacted lines, host-deleted
transcripts).

#### MEM-CLM-cursor-content-free

Label: Cursors hold no content

Claimed operation: export cursors are owner-private on disk and contain no
transcript text or path. Source: SRC-1, `recall/skills/recall/SKILL.md`
(`doctrine/design`).

> and never encode transcript text or a path.
> --- `recall/skills/recall/SKILL.md`

### Evidenced absences

#### MEM-ABS-push-hook

Label: No push injection

- Status: absent
- Searched: all eight tracked files under `recall/` at
  `c82883b15e5e8f02483bee513b3c8dcac48e3c9e` (listed by `git ls-tree -r
  --name-only`), query `hook|SessionStart|UserPromptSubmit|PreCompact|compact|inject|automatic`
  (case-insensitive); both plugin manifests read in full.
- Evidence: the only match is "rather than selecting rank 1 automatically";
  neither manifest declares hooks; no hooks file is tracked.
- Conclusion supported: the package ships no mechanism that inserts retained
  session material into a model context without a model-issued request; every
  route reading session material is pull. `related` is suggested "at session
  start" but is still a model-run command.
- Conclusion prevented: whether a host or the separately installed engine
  configures hooks, and whether the host's own memory or compaction surfaces
  inject Recall output. This absence does not cover generated skills: the
  package ships no hook for them either, but their delivery is decided by the
  host skill loader, so their read-back direction is host-dependent
  ([MEM-RTE-generated-skill-load](#mem-rte-generated-skill-load)).

#### MEM-ABS-skill-provenance

Label: No skill provenance link

- Status: absent
- Searched: `recall/skills/recall/SKILL.md` at
  `c82883b15e5e8f02483bee513b3c8dcac48e3c9e`, the skill-ify outcome and
  playbook read in full, plus a search for
  `receipt|source session|provenance|link back|cite`.
- Evidence: receipt matches occur only in find/verify, remote read and export
  text; the skill-ify text asks to drop "specific IDs, dates" and states no
  requirement to record the source session or why steps were kept.
- Conclusion supported: the shipped procedure does not ask the generated skill
  to retain its source session or its selection reasons.
- Conclusion prevented: whether an external skill creator adds provenance, and
  whether a model adds it unprompted.

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-OBJ-session-transcripts](runtime.md#rt-obj-session-transcripts)

- Raw versus derived: raw traces. They are the primary retained memory; every
  local read-back route ultimately reads them, through the engine or `rg`.
- Write agency: the host harness writes them as a by-product of every session;
  Recall has no admission control over them.
- Lineage: user text, assistant text, tool input/output, and possibly thinking
  text (host fact). Subagent transcripts sit under the parent's directory and
  are indexed as separate sessions; child and continuation sessions are
  separate export boundaries by default.
- Persistence: governed by host retention (`cleanupPeriodDays`), not by Recall.
- Limits: content and format are uninspected host facts.

#### On [RT-OBJ-session-index](runtime.md#rt-obj-session-index)

- Raw versus derived: derived from transcripts by automatic, trace-fed ingest
  (declared). Declared filters: no reasoning/thinking blocks, redaction of
  secret-shaped lines, Claude Code and Codex only.
- Curation: the declared transformation is indexing (entity index, token leg,
  phrase matching). No meaning-changing curation, summarization or
  rationale is declared.
- Trace learning: automatic and trace-fed, but its output is retrievable
  evidence, not behavior-shaping instructions. It reaches behavior only
  through the model's reading of a hit and window.
- Lineage gap: whether entries survive deletion of their source transcript is
  unstated; `show` reads by path, which suggests the source file is still
  needed for windows. Unresolved (see Integration issues).

> If the only trace of something was a thinking block, it is
> not findable.
> --- `recall/skills/recall/SKILL.md`

#### On [RT-OBJ-recall-receipt](runtime.md#rt-obj-recall-receipt)

- Form: symbolic reference to retained material outside the window.
- Consumer authority: addressing only; the remote route makes it a citation
  constraint ("cite only `opened_receipts`") and the forget route makes it the
  sole deletion key.
- Read-back role: a receipt in an answer lets a later turn re-open the same
  record. A receipt identifies a record, not a session's tail or prompts.

> do not treat one opened receipt as the full session's final state.
> --- `recall/skills/recall/SKILL.md`

#### On [RT-OBJ-brain-record](runtime.md#rt-obj-brain-record)

- Write agency: model-authored selection, user-triggered; the service admits.
- Curation: the model selects "decisions or findings"; the skill excludes
  secrets, hidden reasoning, whole transcripts and unselected third-party
  content. Whether captured text keeps a pointer to its source session is not
  stated.
- Reasons: not required to be retained with the decision.
- Persistence and withdrawal: until `recall_forget` on the exact receipt.

> Do not capture secrets, hidden reasoning, whole transcripts, or
> unselected third-party content.
> --- `recall/skills/recall/references/central-brain.md`

#### On [RT-OBJ-generated-skill](runtime.md#rt-obj-generated-skill)

- Raw versus derived: derived, behavior-shaping natural-language instructions
  distilled by the model from a prior session's working window.
- Curation: the model separates durable recipe from one-off data; this is a
  meaning-changing generalization performed by the model, as requested.
- Trace learning: trace-fed, but user-triggered rather than automatic.
- Reasons and lineage: not retained
  ([MEM-ABS-skill-provenance](#mem-abs-skill-provenance)).

> separate the durable
> recipe (commands, endpoints, auth patterns) from one-off data (specific IDs,
> dates)
> --- `recall/skills/recall/SKILL.md`

#### On [RT-RTE-local-search-read](runtime.md#rt-rte-local-search-read)

- Read-back trigger: a user request matched by host skill selection; then
  model-issued `search` and `show`.
- Selector inputs: user phrasing, identifiers, and filter flags (`--since`,
  `--until`, `--cwd`, `--harness`, `--branch`); then the model's reading of
  [MEM-OBJ-search-hit](#mem-obj-search-hit).
- Selected retained parts: a ±3-turn window around a timestamp.
- Budget: `--limit N` rows, the window size; no token budget.
- Delivery: tool output into the current context.
- Later consumer and status: the same model's answer; activation unobserved.

#### On [RT-RTE-cold-scan](runtime.md#rt-rte-cold-scan)

- Selected retained parts: raw transcript lines with three lines of context;
  candidate files ordered by modification time.
- Budget: `-C3` per match; the number of matches and files is unbounded.
- Raw versus derived: reads raw traces, so the index's declared exclusions do
  not apply. The "not findable" thinking-block gotcha is scoped to indexed
  search; whether a cold scan can find thinking text depends on the host.

#### On [RT-RTE-outcome-playbooks](runtime.md#rt-rte-outcome-playbooks)

- Selected retained parts: continue reads the final 30 turns; repeat reads the
  user prompts only, presented verbatim.
- Behavioral authority: in repeat, retrieved prior prompts become the driving
  instructions for new work after the user confirms fresh inputs. This is the
  strongest authority any read-back route gives retained raw material.

#### On [RT-RTE-remote-brain-read](runtime.md#rt-rte-remote-brain-read)

- Selected retained parts: on the MCP path, one record per receipt, followed
  to `complete`; neighbors through `recall_session_context`; full documents
  through `recall_exec`. On the CLI central-client path, `show
  '<recall://receipt>'` opens a receipt; what CLI `search` selects there is
  not stated.
- Budget: bounded by "the installed tool's schema and limits", which are not
  shipped. Following a cursor to `complete` reads a whole record, whatever its
  size.
- Source trust: snippets are pointers; only opened receipts are citable; gaps
  must be stated. No trust distinction by record origin (capture, sync,
  import).
- Failure handling: a failing remote configuration stays remote.

> Keep an existing remote configuration remote if it fails;
> do not silently fall back to a local index.
> --- `recall/skills/recall/references/central-brain.md`

#### On [RT-RTE-brain-capture](runtime.md#rt-rte-brain-capture)

- Admission control: a human decision starts the capture; the model authors
  the selected content; the service admits. The human does not approve the
  selected text under the skill's procedure.
- Withdrawal: exact-receipt forget; identity must not be inferred from search
  text. Whether forget reaches synced copies is unstated.

#### On [RT-RTE-skillify-admission](runtime.md#rt-rte-skillify-admission)

- Admission control: user request triggers; model authors; no human approval
  of the generated text is required by the skill; the external creator's
  admission is uninspected.
- Raw-to-derived chain: transcript → `show` working window in context → model
  distillation → package on disk → later host loader
  ([MEM-RTE-generated-skill-load](#mem-rte-generated-skill-load)).
- Reasons: the selection reasons and source session are not retained.

#### On [RT-RTE-session-export](runtime.md#rt-rte-session-export)

- Working-context control: when `recap` uses this route, export pages go to
  `recap`'s Python process, not the model's context. Recall's text is
  redacted before `recap` sees it, as declared. The cursor
  ([MEM-OBJ-export-cursor](#mem-obj-export-cursor)) persists between calls.
- Later consumer: `recap`'s code, which writes private output files
  (`private_write`, `private_write_text`, mode 0600); their later use is
  excluded.

#### On [RT-RTE-index-maintenance](runtime.md#rt-rte-index-maintenance)

- Write agency: software admission (engine ingest scope and redaction); the
  model or a detached process triggers it. No per-content human or model
  admission.
- Self-feeding: the current session, once its transcript is ingested, becomes
  retrievable by later invocations, including whatever Recall output the
  current session read back.
- Withdrawal: host retention deletion is treated as a loss to surface
  immediately; `--rebuild` requires explicit user request.

> Surface that to the user immediately because history is being deleted.
> --- `recall/skills/recall/SKILL.md`

#### On [RT-BAP-retrieved-sessions](runtime.md#rt-bap-retrieved-sessions)

- Additional consumer: `precap`'s agent, instructed to run one query, read the
  top five results and stop if the top hit is not about the same path.

> one query built
> from the repo path and the task's key nouns, top five results, and stop there if the top hit
> is not about the same path.
> --- `precap/skills/precap/SKILL.md`

## Write side

**Acquisition.** The retained memory is acquired outside Recall: the host
harness writes transcripts of every session, including subagents
([RT-OBJ-session-transcripts](runtime.md#rt-obj-session-transcripts)).
Admission control is absent at the target; whatever the host records is
eligible.

**Automatic transformation.** The engine ingests transcripts into the index
([RT-RTE-index-maintenance](runtime.md#rt-rte-index-maintenance)), triggered
by a model-run `index`, the detached cold-start build
([RT-RTE-cold-scan](runtime.md#rt-rte-cold-scan)), or engine scheduling the
skill does not describe. Admission is software-only and declared: Claude Code
and Codex transcripts, no thinking blocks, secret-shaped lines redacted
([RT-CLM-ingest-redaction](runtime.md#rt-clm-ingest-redaction)). The chain is
raw transcript → index entry → search hit and `show` window → current model.
No intermediate derived form is persisted for reuse beyond the index itself.
The index keeps no reasons because it holds no judgments; a hit's `WHY` is
recomputed per query.

**Authoring.** Two model-authored writes exist, both started by the user:

- Brain capture ([RT-RTE-brain-capture](runtime.md#rt-rte-brain-capture)): the
  model selects decisions or findings; private by default; the receipt returns.
- Skill-ify ([RT-RTE-skillify-admission](runtime.md#rt-rte-skillify-admission)):
  the model distills a recipe from a prior window into an instruction package.
  This is the only route whose derived output carries instruction force for
  later sessions
  ([MEM-RTE-generated-skill-load](#mem-rte-generated-skill-load)). It keeps
  neither the source session nor its reasons
  ([MEM-ABS-skill-provenance](#mem-abs-skill-provenance)).

**Service-side admission.** Sync, ChatGPT-export import, a Cowork collector and
pull connectors write into the Brain
([MEM-RTE-brain-ingest](#mem-rte-brain-ingest)). These are claimed only, with
unknown initialization control, filtering and provenance.

**Access metadata.** Export cursors persist under `~/.recall`
([MEM-OBJ-export-cursor](#mem-obj-export-cursor)), declared content-free
([MEM-CLM-cursor-content-free](#mem-clm-cursor-content-free)).

**Maintenance, rejection and withdrawal.**

- Rejection at write: model-enforced capture exclusions; engine redaction
  (declared). No route rejects a transcript or a generated skill on content.
- Withdrawal: `recall_forget` by exact receipt; manual deletion of generated
  skills; host retention deletion of transcripts, which `doctor` surfaces as
  a warning. The index's response to deleted sources is unstated.
- Rebuild: `index --rebuild` only on explicit user request, justified by cost
  (WAL space, CPU), not by content.
- Revision: none. No route edits, supersedes or annotates retained items.

## Read-back

Every route that reads retained session material is pull: the foreground
model, or for export a consuming skill's code, issues the request
([MEM-ABS-push-hook](#mem-abs-push-hook)). That material arrives as tool
output in the current context, or in the consumer's process for export.
Nothing is persisted from the read. Generated-skill read-back
([MEM-RTE-generated-skill-load](#mem-rte-generated-skill-load)) is the
exception: the host skill loader decides delivery, so its direction is
host-dependent and uninspected.

| Route | Trigger | Selector and inputs | Selected part and budget | Later consumer |
|---|---|---|---|---|
| [RT-RTE-local-search-read](runtime.md#rt-rte-local-search-read) | User request, host skill match | Engine ranking and gate over phrasing, identifiers, flags; model reads `WHY` | ±3 turns; `--limit N` rows | Current model's answer, path as receipt |
| [RT-RTE-cold-scan](runtime.md#rt-rte-cold-scan) | No index | Model-chosen `rg` terms; `ls -t` recency | `-C3` lines; unbounded matches | Current model; answer labelled cold scan |
| [RT-RTE-related-sessions](runtime.md#rt-rte-related-sessions) | Implicit reference to prior work | Engine overlap of cwd, branch, files; recency | Ranked list | Current model |
| [RT-RTE-outcome-playbooks](runtime.md#rt-rte-outcome-playbooks) | Continue or repeat outcome | Model's outcome choice and hit choice | Last 30 turns, or user prompts verbatim | Current model; prompts may drive re-execution after confirmation |
| [RT-RTE-remote-brain-read](runtime.md#rt-rte-remote-brain-read) | Central mode configured | Service search; model selection | One record to `complete`; neighbors; full documents | Current model; only opened receipts citable |
| [RT-RTE-session-export](runtime.md#rt-rte-session-export) | Consumer skill needs full coverage | Exact native identity or path | Every event, paged by 1000 | `recap` code, outside the model context |
| [MEM-RTE-generated-skill-load](#mem-rte-generated-skill-load) | Later host skill match; direction host-dependent | Host description matching | Whole generated package | Later model, instruction force |

**Working-context control.** The mechanisms that decide what enters the window,
other than accumulation, are:

- *Bounded windows* (`show --around`, `--tail`, `--prompts`, `rg -C3`): the
  foreground model, by its own tool call, keeps the rest of an up-to-80 MB
  session on disk. The window holds the excerpt by value. The path and
  timestamp remain as a reference, and reloading another window is the
  reload route.
- *Hit summaries* ([MEM-OBJ-search-hit](#mem-obj-search-hit)): the engine
  replaces whole sessions with a row and an explanation; the model decides
  which to open.
- *Conditional reference loading*: the skill tells the model to read
  `references/central-brain.md` only when MCP tools or central signals exist.
  This keeps static skill material out of the window; it is not retained
  memory.
- *Discarded side output*: the detached index build sends output to
  `/dev/null`, keeping it out of context entirely.
- *Process isolation for export*: `recap` consumes export pages in a
  subprocess rather than in model context, which resembles a frame whose
  only return is `recap`'s rendered output.

The stack-frame lens fits the export case and breaks for host subagents.
Their frames' full transcripts persist and can be paged back in later by path.
The receipt and path in context are followable references; the window still
holds no reference that tracks liveness of what it loaded.

## Integration issues

1. **Absorbed correction to
   [RT-RTE-index-maintenance](runtime.md#rt-rte-index-maintenance).** An
   earlier version of its context/state field said the engine writes the
   index "from all host transcripts". The supplied runtime now states the
   declared scope: Claude Code and Codex transcripts, no pi sessions or
   thinking blocks, secret-shaped lines redacted
   ([RT-CLM-ingest-redaction](runtime.md#rt-clm-ingest-redaction)). No
   correction remains. Consequence kept: the index is a filtered derivation,
   not a mirror of host history.
2. **Possible overlap: [MEM-RTE-generated-skill-load](#mem-rte-generated-skill-load)
   with [RT-BAP-generated-skill](runtime.md#rt-bap-generated-skill)** and the
   later read-back field of
   [RT-RTE-skillify-admission](runtime.md#rt-rte-skillify-admission). The
   memory route declares the read-back leg as a route with status fields; the
   BAP declares the authority path. Reconciliation may treat them as one
   referent seen as route and authority path.
3. **Distinct identity: [MEM-OBJ-brain-synced-content](#mem-obj-brain-synced-content)
   and [MEM-RTE-brain-ingest](#mem-rte-brain-ingest)** versus
   [RT-OBJ-brain-record](runtime.md#rt-obj-brain-record) and
   [RT-RTE-brain-capture](runtime.md#rt-rte-brain-capture). The runtime
   records cover deliberate capture only; the Brain has other declared
   admission paths with different lineage and consent basis.
4. **Part relation: [MEM-OBJ-export-cursor](#mem-obj-export-cursor)** is a
   part of [RT-OBJ-session-export](runtime.md#rt-obj-session-export), declared
   separately because it persists on disk with its own claim.
5. **Conflicting shipped wording: [MEM-CLM-empty-no-answer](#mem-clm-empty-no-answer)**
   versus the `SKILL.md` statement that empty output does not prove absence
   (runtime guarantee G5). Consequence for memory: a scripted consumer of the
   cookbook would treat index exclusions as absence of work. Unresolved;
   retain both.
6. **Unresolved: index lifetime after host retention deletion.** Evidence:
   `doctor` warns that "history is being deleted" when `cleanupPeriodDays`
   retention is re-enabled, and `show` reads by session path. Missing fact:
   whether index entries or snippets survive source deletion. Prevents: saying
   whether Recall's index extends memory beyond host retention or merely
   mirrors surviving transcripts. Concerns
   [RT-OBJ-session-index](runtime.md#rt-obj-session-index) and
   [RT-OBJ-session-transcripts](runtime.md#rt-obj-session-transcripts).
7. **Unresolved: reach of `recall_forget`.** Whether forgetting a captured
   record affects synced copies, local transcripts or the local index is not
   stated. Concerns [RT-RTE-brain-capture](runtime.md#rt-rte-brain-capture)
   and [MEM-RTE-brain-ingest](#mem-rte-brain-ingest).
8. **Qualification of the thinking-block gotcha.** "Not findable" holds for
   indexed search as declared; the cold scan reads raw transcripts and is not
   subject to the index filter. Concerns
   [RT-RTE-cold-scan](runtime.md#rt-rte-cold-scan) and
   [RT-CLM-ingest-redaction](runtime.md#rt-clm-ingest-redaction).
9. **Scoped read-back direction.** The pull finding covers the routes that
   read session material, not every read-back route.
   [MEM-RTE-generated-skill-load](#mem-rte-generated-skill-load) delivers
   trace-derived instructions through the host skill loader, whose trigger and
   selection are outside SRC-1. Its direction is host-dependent and
   uninspected. Consequence: a system-wide "pull-only" read-back value is not
   supported; it holds for session-material routes only. Concerns
   [MEM-ABS-push-hook](#mem-abs-push-hook) and
   [RT-BAP-generated-skill](runtime.md#rt-bap-generated-skill).
10. **CLI as central client.** The supplied runtime now records that the CLI
    also serves as a central client
    ([RT-RTE-interface-selection](runtime.md#rt-rte-interface-selection),
    [RT-RTE-remote-brain-read](runtime.md#rt-rte-remote-brain-read)). The
    selected parts and budget in this member's annotation on the remote read
    describe the MCP path. What CLI `search` returns under a central or
    `shadow` signal is not stated, so this member does not establish which
    store answers on that path.

## Limitations and checks

**Prevented conclusions.** With the engine and Brain absent, this report cannot
establish what the index contains, how hits are ranked, whether redaction or
the evidence gate works, whether derived entries outlive their sources, how
Brain imports are filtered, or what `recall_forget` removes. No route has
observed delivery, activation or benefit. Model compliance with every
instruction-level rule (window discipline, capture exclusions, citation of
opened receipts, rebuild consent) is unobserved, and shell access is an
alternate path around each. Host skill loading, host memory (`MEMORY.md`) and
host compaction are outside the boundary.

**Source and method identity rechecks.** The frozen checkout's `HEAD` was
confirmed as `c82883b15e5e8f02483bee513b3c8dcac48e3c9e`; the `recall/` file
list was taken with `git ls-tree` at that commit. No prior analyses were read.

**Correction round.** This version answers one refusal blocker: the pull
finding is scoped to session-material routes, and generated-skill read-back
is stated as host-dependent. The frozen checkout's `HEAD` was rechecked for
this round.

**Validation.** `commonplace-validate` was run on this report with
`--artifact` and `--role memory` from the supplied command path. The member
content check passed. A pass establishes form and quotation occurrence only,
not claim support.
