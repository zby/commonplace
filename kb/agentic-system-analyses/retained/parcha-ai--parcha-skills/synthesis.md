---
type: agentic-system-analyses/types/agentic-system-synthesis.md
description: "Recall skill instructs a host agent to pull and match-check bounded windows of prior coding sessions; its engine, ranking, redaction and Brain service are declared only, and every check is model-enforced"
run-id: AAS-2026-11-05-parcha-skills-d5ad184aa4af-01
reviewed-boundary: "c82883b15e5e8f02483bee513b3c8dcac48e3c9e"
---

# Recall (parcha-skills) synthesis

## Bounded synthesis

### Evidence basis and boundary

The target is the `recall/` skill package in the Git repository
`https://github.com/Parcha-ai/parcha-skills` at commit
`c82883b15e5e8f02483bee513b3c8dcac48e3c9e` (SRC-1), as frozen in the
[boundary](boundary.md). The package has eight tracked files: the skill
`recall/skills/recall/SKILL.md`, two reference files
(`recall/skills/recall/references/central-brain.md` and
`recall/skills/recall/references/query-cookbook.md`), a README, a license and
three manifests. It contains no executable code. The repository's
`tests/test_portability.py` enforces that it holds instructions and manifests
only. The boundary classifies the target as an `extension or tool mechanism`,
with boundary kind `complete artifact, partial loop` and evidence tier
`doc-grounded`.

Evidence comes in two layers, and this account keeps them apart throughout:

- **Implementation (the agent-side procedure).** The skill text is the
  procedure a host model (Claude Code, Codex or pi) is asked to follow. It
  shows what the model is asked to do. It does not show that a model complies:
  no code checks compliance ([RT-BAP-skill-instructions](runtime.md#rt-bap-skill-instructions)).
- **Doctrine/design (everything the procedure calls).** The Recall engine
  (`recall.py`), its SQLite index, ranking, evidence gate, redaction, retention
  watchdog and export producer are not in the repository
  ([RT-ABS-engine-code](runtime.md#rt-abs-engine-code)). Neither is the private
  central Brain service and its MCP tools
  ([RT-CMP-central-brain](runtime.md#rt-cmp-central-brain)). Every statement
  about them comes from the skill's own description of their contract.

SRC-1 holds no Recall run trace. The exporter tests in the excluded `recap`
skill skip unless a separately installed engine is supplied, as the
[report verification](report-verification.md) found. Operation, activation and
benefit are therefore unobserved for every route below. Missing execution
evidence does not establish that a behavior is absent.

The host harnesses that write transcripts and load skills, the external skill
creator, and the sibling skills `recap` and `precap` are outside the
functional boundary. `recap` and `precap` were read only as downstream
consumers of Recall output. Their checks are not attributed to Recall.

### What the system is and what it claims to do

Recall is a retrieval procedure over a coding agent's own session history. It
claims to find the prior session that answers a user's question and to read
only the best-supported part of it
([EPI-CLM-best-supported-read](epistemic.md#epi-clm-best-supported-read)).
The model then uses that part for one of four outcomes: answer with a receipt
(find/verify), resume work (continue), re-run the driving prompts with fresh
inputs (repeat), or distill a reusable skill (skill-ify). Secondary claimed
work covers three more uses. It exports one exact session as paged JSON for
another skill. It captures and forgets records in a remote Brain on user
request. It keeps the index healthy.

The package stores nothing itself. The retained material it reads is written
by others:

- The host harness writes the raw transcripts
  ([RT-OBJ-session-transcripts](runtime.md#rt-obj-session-transcripts)).
- The absent engine writes the index
  ([RT-OBJ-session-index](runtime.md#rt-obj-session-index)).
- The absent service holds the Brain records
  ([RT-OBJ-brain-record](runtime.md#rt-obj-brain-record),
  [MEM-OBJ-brain-synced-content](memory.md#mem-obj-brain-synced-content)).

The procedure causes two durable writes of its own: Brain capture and
skill-ify packages.

### Runtime map

An invocation runs as follows.

1. **Trigger.** A user request matches the skill description, and the host
   loads the skill. Skill selection is host behavior.
2. **Interface selection**
   ([RT-RTE-interface-selection](runtime.md#rt-rte-interface-selection)). The
   model looks for Recall MCP tools or central-mode signals (`RECALL_URL`,
   `RECALL_MODE` `remote`/`shadow`, or a client config file).
   - With a central signal, it follows the remote procedure. It uses MCP tools
     when present. Otherwise the `RECALL_SCRIPT` CLI acts as a remote client.
   - Without a central signal, it uses the local CLI.
   - With no interface, it reports the missing dependency and stops.

   In central mode the skill forbids local fallback (runtime guarantee G1).
   That is a policy enforced only by model compliance. Shell access and
   `recap`'s own engine resolution are alternate paths around it.
3. **Outcome choice.** The model classifies the request among the four
   outcomes and asks the user only when the outcome is ambiguous.
4. **Search, match check and bounded read.** These differ by route:
   - *Local route*
     ([RT-RTE-local-search-read](runtime.md#rt-rte-local-search-read)): the
     model runs `search` with filter flags, reads each top hit's `WHY` line,
     selects by match type, and reads a window with `show`.
   - *Cold start* ([RT-RTE-cold-scan](runtime.md#rt-rte-cold-scan)): with no
     index, the model scans raw JSONL transcripts with `rg` and starts a
     detached `index` build.
   - *Query-free* ([RT-RTE-related-sessions](runtime.md#rt-rte-related-sessions)):
     `related` ranks sessions sharing cwd, branch or touched files.
   - *Remote* ([RT-RTE-remote-brain-read](runtime.md#rt-rte-remote-brain-read)):
     `recall_search`, then `recall_show` followed to `complete`, then neighbors
     and full documents.
5. **Outcome-specific step.** Continue and repeat read the last 30 turns or
   the user prompts
   ([RT-RTE-outcome-playbooks](runtime.md#rt-rte-outcome-playbooks)).
   Skill-ify writes a package
   ([RT-RTE-skillify-admission](runtime.md#rt-rte-skillify-admission)).
6. **Terminal output.** An answer in the host session that carries a session
   path or `recall://` receipt
   ([RT-OBJ-recall-receipt](runtime.md#rt-obj-recall-receipt)).

The other routes are
[RT-RTE-brain-capture](runtime.md#rt-rte-brain-capture) (user-requested
`recall_capture`, and `recall_forget` by exact receipt),
[RT-RTE-session-export](runtime.md#rt-rte-session-export) (paged export and
relation graph, consumed in-repo by `recap`'s code),
[RT-RTE-index-maintenance](runtime.md#rt-rte-index-maintenance) (`index`,
`doctor`, and `index --rebuild` only on explicit user request) and
[RT-RTE-package-change-gate](runtime.md#rt-rte-package-change-gate).

Coordination is single-agent. The skill delegates to no agent
([WF-ABS-agent-delegation](workflow.md#wf-abs-agent-delegation)). The skill
narrows no tool grant
([RT-ABS-tool-restriction](runtime.md#rt-abs-tool-restriction)). The Codex
manifest's `"capabilities": ["Read"]` label is narrower than the shipped
procedure, which needs shell execution and file writes; whether Codex enforces
the label is a host fact. The only distributed-parametric component on these
routes is the host model
([RT-CMP-host-model](runtime.md#rt-cmp-host-model)). It is not pinned, and the
host can resolve it to any model. Whether the engine's ranking uses dense
representations is unstated.

### Discriminating mechanisms

**Pull retrieval with match evidence as the selector.** Every route that reads
retained session material is pull. The foreground model, or a consuming
skill's code for export, requests each delivery through a tool or shell call.
The package ships no hook or other push of that material
([MEM-ABS-push-hook](memory.md#mem-abs-push-hook)). This holds for
session-material routes only. Generated skills reach later sessions through
the host skill loader
([MEM-RTE-generated-skill-load](memory.md#mem-rte-generated-skill-load),
implementation status `afforded`), so their read-back direction depends on the
host and is uninspected. A system-wide pull-only claim is unsupported.

Selection has two stages:

1. The absent engine ranks candidates and suppresses those below an evidence
   gate ([EPI-RTE-engine-evidence-gate](epistemic.md#epi-rte-engine-evidence-gate),
   status `claimed`). The skill also declares that identifiers are matched
   exactly through an entity index and a token leg
   ([RT-CLM-exact-identifier-matching](runtime.md#rt-clm-exact-identifier-matching)).
2. The model reads each top hit's `WHY` line
   ([EPI-OBJ-search-results](epistemic.md#epi-obj-search-results)). It treats
   generic-word matches as weak, and it prefers an identifier, phrase or
   exact-entity match over rank 1
   ([EPI-RTE-why-assessment](epistemic.md#epi-rte-why-assessment)).

This check licenses at most "these terms occurred in this session". It does
not license "this session answers the question". The skill itself warns that
lexically adjacent sessions can appear for work that never happened. `related`
output carries no described `WHY` line, so this check does not apply to it.

**Bounded windows as the context budget.** The main context-engineering
mechanism keeps most of a session on disk. The model reads a ±3-turn window
(`show --around`), the last 30 turns (`--tail 30`), the user prompts only
(`--prompts`), or `rg -C3` lines on a cold scan. The skill justifies `show`
over `cat` by size: sessions can reach 80 MB. The budget is stated in turns,
lines and row limits, not tokens, and nothing measures context use. The remote
route is less bounded, because it follows a record's cursor to `complete` and
can fetch full documents. A path, receipt or `logical_document_id` left in
context is a followable reference: the model can reopen it at another offset.
Host subagent transcripts persist and are indexed as their own sessions
([EPI-CLM-subagent-lineage](epistemic.md#epi-clm-subagent-lineage)). A later
invocation can therefore reload what a parent never received. Other
working-context controls are the following, as described in the
[memory member](memory.md):

- the engine replaces whole sessions with hit rows;
- the detached index build discards its output;
- `recap` consumes export pages in its own process, outside model context;
- the skill tells the model to read `central-brain.md` under central signals.

The last control is weaker than it looks: the file is also linked
unconditionally (see Limitations).

**Declared filters on retained material, and a path that bypasses them.**
According to the skill's contract, the index covers Claude Code and Codex
transcripts only, not pi sessions. It never stores reasoning or thinking
blocks, and it redacts secret-shaped lines at ingest
([RT-CLM-ingest-redaction](runtime.md#rt-clm-ingest-redaction)). All of this
is declared, not inspected. The cold scan reads raw transcripts with `rg`, so
none of these filters applies on that path. Whatever the host wrote, including
any secret-shaped line, reaches the model's context. Whether host transcripts
contain thinking text is a host fact. The skill's only safeguard on this path
is a disclosure duty: the model must tell the user that the answer came from a
cold scan ([EPI-RTE-cold-scan-disclosure](epistemic.md#epi-rte-cold-scan-disclosure)).

**Trust by evidence form, not by origin.** The skill ranks evidence strength
by form:

- identifiers and exact phrases are strong;
- generic words are weak;
- remote snippets are pointers;
- only opened receipts may be cited
  ([EPI-RTE-receipt-support-check](epistemic.md#epi-rte-receipt-support-check)).

It does not mark retrieved content by origin, such as own session, other
harness, captured record or imported export. It does not separate a prior
assistant's claims from what tools showed
([EPI-ABS-self-report-distinction](epistemic.md#epi-abs-self-report-distinction)).
It places no limit on the instructional force of retrieved transcript text
([EPI-ABS-data-instruction-rule](epistemic.md#epi-abs-data-instruction-rule)).

**Writes without content approval.** Recall causes two model-authored durable
writes. In each, a user request starts the write, and the model selects or
authors the content. No step requires the user to approve that text before
admission ([EPI-ABS-acceptance-record](epistemic.md#epi-abs-acceptance-record)).

- *Brain capture* ([RT-RTE-brain-capture](runtime.md#rt-rte-brain-capture)).
  The model captures "decisions or findings", private by default. The skill
  excludes secrets, hidden reasoning, whole transcripts and unselected
  third-party content. The record returns a receipt. Captured records later
  come back through the same search as other content. SRC-1 marks them as
  selections nowhere.
- *Skill-ify.* The model separates a durable recipe (commands, endpoints,
  auth patterns) from one-off data (specific IDs, dates)
  ([EPI-RTE-recipe-separation](epistemic.md#epi-rte-recipe-separation)), then
  writes a standard `SKILL.md` package. It may also hand the recipe to an
  external skill creator, whose behavior is uninspected. No test, approval or
  link back to the source session is required
  ([EPI-ABS-generated-skill-test](epistemic.md#epi-abs-generated-skill-test),
  [MEM-ABS-skill-provenance](memory.md#mem-abs-skill-provenance)). Later
  sessions may load the package with instruction force
  ([RT-BAP-generated-skill](runtime.md#rt-bap-generated-skill)).

Withdrawal has three forms:

- `recall_forget` removes one Brain record by exact receipt
  ([EPI-RTE-receipt-forget](epistemic.md#epi-rte-receipt-forget)). It leaves
  untouched any answers, skills or captures derived from that record.
- Generated skills are removed only by manual file deletion.
- The host deletes transcripts under its own retention setting. `doctor`
  surfaces this as a warning.

The Brain also has sync, ChatGPT-export import, a collector and pull
connectors ([MEM-RTE-brain-ingest](memory.md#mem-rte-brain-ingest)). These are
named only, with unknown admission and provenance. No route revises or
annotates an existing retained item.

**Export as a fail-closed protocol whose checks sit at the consumer.** The
skill declares paged `recall.session-export.v1` output
([RT-OBJ-session-export](runtime.md#rt-obj-session-export)). Pages carry
`complete`, `next_cursor` and `source_snapshot_stable`, and the cursor is
content-free
([MEM-OBJ-export-cursor](memory.md#mem-obj-export-cursor)). With `--current`,
identity resolves only by exact native session ID and otherwise fails closed
([RT-CLM-export-fail-closed](runtime.md#rt-clm-export-fail-closed)). The
producer is absent.

The in-repo consumer `recap` enforces its side in code (runtime guarantee G6).
It rejects non-zero exits, invalid JSON, an unsupported schema version, a
changed boundary, a discontinuous sequence and an incomplete page without a
cursor. One gap remains in that consumer: if no page carries
`source_snapshot_stable`, `recap` still reports its source as complete. These
checks and this gap belong to `recap`, not to Recall.

### Representative workflow: local find/verify

The [workflow member](workflow.md) traces local find/verify, because it is the
first-listed outcome and the base of the other three. It is also the only
outcome whose acceptance, rejection and recovery steps are all stated.

The participants are the user, the host model and the engine (declared only).
The model chooses the outcome, writes the query and filters, judges match
evidence, and writes the answer. The engine supplies ranked rows and windows.

Verification has two possible rejection points before delivery:

1. the engine's evidence gate, whose criterion SRC-1 does not state;
2. the model's own `WHY` check
   ([EPI-RTE-why-assessment](epistemic.md#epi-rte-why-assessment)), which is
   neither recorded nor checked.

No code path, second agent or user checks the delivered answer against the
shown window
([WF-ABS-independent-answer-check](workflow.md#wf-abs-independent-answer-check)).
The receipt lets a reader check the answer afterwards. It names the session
file, not the turns used
([EPI-RTE-answer-receipt](epistemic.md#epi-rte-answer-receipt)). The remote
variant adds a stricter rule: cite only opened receipts whose text supports
the answer, and state gaps. That rule is also model-enforced, and local mode
has no counterpart. If the model accepts a lexically adjacent session, no
later step detects the error.

The model owns all recovery:

- With no interface, it reports and stops.
- With no index, it falls back to the cold scan and labels the answer.
- With empty output, it retries once with an identifier or a wider window, and
  then reports what was searched and that no supported match was found
  ([EPI-RTE-empty-result-report](epistemic.md#epi-rte-empty-result-report)).
- With stale-looking results, it runs incremental `index`.

The shipped text disagrees on what an empty result licenses. `SKILL.md` says
empty output "does not prove the work never happened". The cookbook's
scripting note calls empty stdout a "confident no-answer"
([EPI-CLM-confident-no-answer](epistemic.md#epi-clm-confident-no-answer)).
The two can be reconciled only as "the engine ran and nothing cleared its
gate". Several classes are unsearchable through the index: pi sessions,
thinking-only traces, redacted lines and host-deleted transcripts. Only the pi
case is tied to a no-proof rule.

Delivery is an answer that names the receipt. Nothing persists the query, the
rejected candidates or the answer.

### Assessment relative to scenarios

- **Recalling what happened in an earlier Claude Code or Codex session.** The
  procedure supports this as a bounded, receipt-backed lookup, with
  match-type discipline asked of the model. How reliable the answer is depends
  on two unverified links: the declared engine ranking and gate, and the
  model's compliance with an unrecorded `WHY` check. In local mode the answer
  is accepted by the model that wrote it.
- **Proving that something did not happen.** The records do not support it.
  The index excludes several classes of history, and the shipped files
  disagree on what an empty result licenses.
- **Keeping secrets or reasoning out of context.** This rests on declared
  engine redaction for indexed paths only. The cold-scan path bypasses it.
- **Using retrieved sessions to drive new work** (continue, repeat). In
  repeat, prior prompts become driving instructions after a user confirmation
  that the skill requests but does not enforce
  ([EPI-RTE-repeat-confirmation](epistemic.md#epi-rte-repeat-confirmation)).
  Continue's branch check runs `git -C <cwd> branch --show-current`. That
  command reports the branch currently checked out in `<cwd>`. It does not
  show whether the prior session's branch still exists
  ([EPI-RTE-resume-branch-check](epistemic.md#epi-rte-resume-branch-check)).
  This is a reading of the command text, not an observed run.
- **Building durable capability from past work** (skill-ify). The package is
  written without evaluation, approval or provenance. Its lineage and its
  presupposition that the kept steps "worked" are lost.
- **Central mode.** On the MCP path, the instruction intends answers to come
  only from the central Brain. What CLI `search` returns under a central
  signal without MCP tools is not stated, and neither is what `shadow` mode
  means. Single-store provenance therefore holds as the instruction's intent
  on the MCP path only.

### Learning, reflection, autonomy and self-improvement

The runtime report assesses neither theory-builder conditions 1–4 nor
learning, reflection or autonomy. This synthesis therefore states no
conclusion on those properties. The records do support three narrower
findings, each at its own status:

- **Strongest supported contribution.** Retained session experience is
  automatically turned into durable artifacts that reach later sessions. The
  index is built from transcripts by a declared automatic ingest (`claimed`).
  Brain captures are model-selected without content approval (write `wired`).
  Skill-ify writes trace-distilled instruction packages that later sessions
  can load (write `wired`; later loading `afforded` through the host loader)
  ([RT-RTE-index-maintenance](runtime.md#rt-rte-index-maintenance),
  [RT-RTE-brain-capture](runtime.md#rt-rte-brain-capture),
  [RT-RTE-skillify-admission](runtime.md#rt-rte-skillify-admission)). This is
  trace-fed retention, and skill-ify adds capability for later sessions.
  Neither establishes improved capacity, because no improvement or
  attribution evidence exists.
- **Self-improvement (skill-ify pathway).** Link 1 is unestablished: nothing
  evaluates whether the kept steps worked, so no evidence about an objective
  shapes the update. Links 3 and 4 depend on the external host loader and on
  runs that were not observed. Exercised self-improvement is therefore not
  attributable. The pathway supports at most a marked dispositional claim of
  improvement-directed self-change, and only if the generated skills count as
  part of the system's organization.
- **Revision of its own method.** No route in the package revises the skill's
  own instructions from use (runtime change-admission account). Package
  changes go through repository commits. The instruction-only test does not
  run in CI when a change touches only `recall/`
  ([RT-RTE-package-change-gate](runtime.md#rt-rte-package-change-gate)).

The unresolved question is whether any generated skill or captured record
improves later work. Answering it needs run evidence comparing later
sessions that receive the artifact with sessions that do not.

### Evidence that would change this assessment

- The engine source or a pinned build would let the declared claims become
  inspected implementation. These are ranking, the evidence gate, exact
  matching, redaction, thinking-block exclusion, incremental indexing, `show`
  window extraction, the export producer, and handling of deleted sources.
- The Brain service source or its documentation would settle admission,
  visibility, sync and import filtering, and `recall_forget` semantics.
- Recall run traces would show model compliance with the `WHY` check, the
  window discipline, the central no-fallback rule, cold-scan disclosure and
  capture exclusions. They would also show whether answers stay within the
  shown windows.
- Host documentation or traces would show how generated skills are delivered
  (injected, listed or loaded on command), whether transcripts contain
  thinking text, and whether hosts enforce the Codex capability label.
- A comparison of later sessions with and without a generated skill or
  captured record would be needed for any learning or self-improvement claim.
- Two package changes would remove stated mismatches. One would reconcile the
  cookbook's empty-result wording with `SKILL.md`. The other would replace the
  continue branch command with one that tests branch existence.

## Limitations

| limitation | affected SRC IDs and record citations | inspected boundary | conclusion prevented | evidence that would resolve it |
|---|---|---|---|---|
| Engine absent: ranking, evidence gate, exact matching, redaction, thinking-block exclusion, incremental ingest and `show` windowing are declared only | SRC-1; [RT-ABS-engine-code](runtime.md#rt-abs-engine-code), [RT-CLM-exact-identifier-matching](runtime.md#rt-clm-exact-identifier-matching), [RT-CLM-evidence-gate](runtime.md#rt-clm-evidence-gate), [RT-CLM-ingest-redaction](runtime.md#rt-clm-ingest-redaction), [EPI-RTE-engine-evidence-gate](epistemic.md#epi-rte-engine-evidence-gate) | All tracked files at the reviewed commit; no `recall.py` at any path | Any implementation-level claim about what a `WHY` line, an empty result or a redacted line certifies, or how faithful a window is | Engine source or a pinned build |
| Central Brain service absent | SRC-1; [RT-CMP-central-brain](runtime.md#rt-cmp-central-brain), [MEM-RTE-brain-ingest](memory.md#mem-rte-brain-ingest), [MEM-OBJ-brain-synced-content](memory.md#mem-obj-brain-synced-content) | `recall/skills/recall/references/central-brain.md` and the capability list in `recall/skills/recall/SKILL.md` | Service admission, visibility, consent, sync and import filtering, encoding of synced content, and service-side curation | Service source or a service contract |
| No observed run or causal experiment | SRC-1; [RT-RTE-local-search-read](runtime.md#rt-rte-local-search-read), [RT-RTE-remote-brain-read](runtime.md#rt-rte-remote-brain-read), [RT-RTE-skillify-admission](runtime.md#rt-rte-skillify-admission), [RT-RTE-brain-capture](runtime.md#rt-rte-brain-capture) | Whole repository; `recap` exporter tests skip without a private engine | Operation, activation, model compliance with every instruction-level rule, answer quality, and any learning or improvement claim | Recall execution traces; with/without comparisons for generated skills and captures |
| Model-enforced rules have shell access as an alternate path | SRC-1; [RT-RTE-interface-selection](runtime.md#rt-rte-interface-selection), [RT-RTE-index-maintenance](runtime.md#rt-rte-index-maintenance), [RT-ABS-tool-restriction](runtime.md#rt-abs-tool-restriction) | `recall/skills/recall/SKILL.md`, manifests, `recap/skills/recap/scripts/recap.py` engine resolution | Treating no-local-fallback, rebuild consent, window discipline or capture exclusions as enforced guarantees | Host tool restrictions or engine-side enforcement, with traces |
| Index lifetime after host retention deletes source transcripts is unstated | SRC-1; [RT-OBJ-session-index](runtime.md#rt-obj-session-index), [RT-OBJ-session-transcripts](runtime.md#rt-obj-session-transcripts) | `recall/skills/recall/SKILL.md` (`doctor` warning; `show` reads by path) | Whether Recall's index extends memory beyond host retention or only mirrors surviving transcripts | Engine deletion handling or a trace after transcript deletion |
| Reach of `recall_forget` is unstated | SRC-1; [EPI-RTE-receipt-forget](epistemic.md#epi-rte-receipt-forget), [RT-RTE-brain-capture](runtime.md#rt-rte-brain-capture), [MEM-RTE-brain-ingest](memory.md#mem-rte-brain-ingest) | `recall/skills/recall/references/central-brain.md` | Whether forgetting reaches synced copies, local transcripts or the index, and whether it deletes or only withdraws reliance while keeping history | Service deletion semantics |
| CLI `search` under a central signal, and the meaning of `shadow` mode, are unstated | SRC-1; [RT-RTE-interface-selection](runtime.md#rt-rte-interface-selection), [RT-RTE-remote-brain-read](runtime.md#rt-rte-remote-brain-read) | `recall/skills/recall/SKILL.md`, `recall/skills/recall/references/central-brain.md` | Which store answers on the CLI central-client path; single-store answer provenance outside the MCP path | Engine mode-routing code or documentation of `shadow` |
| Generated-skill read-back direction depends on the host | SRC-1; [MEM-RTE-generated-skill-load](memory.md#mem-rte-generated-skill-load), [RT-BAP-generated-skill](runtime.md#rt-bap-generated-skill), [MEM-ABS-push-hook](memory.md#mem-abs-push-hook) | All eight `recall/` files; host loader excluded | A system-wide pull-only read-back claim; any push-selector classification for generated skills | Host skill-loader documentation or traces |
| External skill creator's admission behavior is uninspected | SRC-1; [RT-RTE-skillify-admission](runtime.md#rt-rte-skillify-admission), [EPI-ABS-generated-skill-test](epistemic.md#epi-abs-generated-skill-test) | `recall/skills/recall/SKILL.md` skill-ify outcome and playbook | Whether the creator branch adds testing, approval or provenance | Creator source or documentation |
| Shipped files disagree on what an empty result licenses (the source's own inconsistency) | SRC-1; [EPI-CLM-confident-no-answer](epistemic.md#epi-clm-confident-no-answer), [EPI-RTE-empty-result-report](epistemic.md#epi-rte-empty-result-report) | `recall/skills/recall/SKILL.md`, `recall/skills/recall/references/query-cookbook.md` | A negative claim that prior work did not happen, from Recall output alone | A package revision reconciling the two texts; engine gate semantics |
| Conditional reference loading is overstated in the memory account (report-verification limit): `central-brain.md` must be read under central signals but is also linked without condition | SRC-1; [RT-CMP-recall-skill](runtime.md#rt-cmp-recall-skill) | `recall/skills/recall/SKILL.md` (References list and Upgrade section) | That local-mode invocations reliably keep `central-brain.md` out of context; only the mandatory conditional read is established | Host progressive-disclosure behavior and run traces |
| `related` output is grouped under `knowledge` authority in the memory profile, but its recorded effect is ranking and candidate proposal (profile-verification limit) | SRC-1; [RT-RTE-related-sessions](runtime.md#rt-rte-related-sessions), [RT-BAP-retrieved-sessions](runtime.md#rt-bap-retrieved-sessions) | Accepted records only; system value set unchanged | A per-route authority classification of `related` output; cross-system comparison of query-free retrieval authority from that unit | A profile unit scoped to `related` output |
| Capture input and provenance are unstated: whether captures draw on tool results or keep a pointer to their source session | SRC-1; [RT-RTE-brain-capture](runtime.md#rt-rte-brain-capture), [RT-OBJ-brain-record](runtime.md#rt-obj-brain-record) | `recall/skills/recall/references/central-brain.md` | Whether captured records carry tool-trace content or a pointer to their source session | Service record schema or capture traces |
| Theory-builder conditions, learning, reflection and autonomy are not assessed in the runtime report | SRC-1; [RT-RTE-skillify-admission](runtime.md#rt-rte-skillify-admission), [RT-CMP-recall-skill](runtime.md#rt-cmp-recall-skill) | Runtime change-admission account; epistemic bounded conclusion | Any theory-builder, learning, reflection or autonomy conclusion beyond the narrower findings stated in the synthesis | A runtime assessment of those properties, plus run evidence for learning |
