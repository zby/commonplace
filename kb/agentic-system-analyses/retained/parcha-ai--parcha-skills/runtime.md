---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Runtime baseline of the instruction-only recall skill (recall/) of Parcha-ai/parcha-skills at c82883b1: agent-side retrieval, reading, export, capture and skill-ify, with the absent engine and Brain as declared contract"
run-id: AAS-2026-11-05-parcha-skills-d5ad184aa4af-01
reviewed-boundary: "c82883b15e5e8f02483bee513b3c8dcac48e3c9e"
---

# Recall (parcha-skills) runtime report

## Runtime account

### What runs and what this account can establish

The target ships no executable code. Its runtime is a host coding agent
(Claude Code, Codex or pi) whose model reads
[RT-CMP-recall-skill](#rt-cmp-recall-skill) and then issues shell commands or
MCP tool calls against an engine and service outside the repository (SRC-1,
`recall/skills/recall/SKILL.md`, `recall/README.md`). The package states this
directly:

> The Recall engine is distributed separately. This skill contains no executable
> implementation.
> --- `recall/skills/recall/SKILL.md`

Two evidence layers therefore apply throughout. The skill text is
`implementation` evidence for the agent-side procedure: it is the procedure the
host model is asked to follow. Every statement about what the engine
([RT-CMP-recall-engine](#rt-cmp-recall-engine)) or the central Brain
([RT-CMP-central-brain](#rt-cmp-central-brain)) does is `doctrine/design`
only. An implemented instruction establishes the request to the model, not
compliance: the skill has no code path that checks whether the model obeyed.
No observed run or causal experiment exists for Recall in SRC-1, so
operation, activation and benefit remain unobserved for every route below.
Missing execution evidence does not establish absent behavior.

The consequential claimed work is: find a prior coding-agent session that
answers the user's question, read only the supported part of it, and use it to
answer with a receipt, resume work, re-run the driving prompts with fresh
inputs, or distill a reusable skill. Secondary claimed work: export one exact
session as paged JSON for another skill, deliberately capture or forget records
in a remote Brain, and keep the index healthy.

### Shipped entry paths

- **Skill trigger.** The host loads `recall/skills/recall/SKILL.md` when its
  description matches the request. The description lists trigger phrases and
  two exclusions (code search; facts already in `MEMORY.md`). Selection is the
  host's skill-matching behavior, external to the target.
- **Plugin and marketplace discovery.** `recall/.claude-plugin/plugin.json`
  and `recall/.codex-plugin/plugin.json` point at `./skills/`; repository
  registrations in `.claude-plugin/marketplace.json`,
  `.agents/plugins/marketplace.json` and root `package.json` expose `./recall`
  (SRC-1). The Codex manifest also supplies two default prompts.
- **Install through skills.sh** (`recall/README.md`). Installing the skill
  does not install or start the engine.
- **Invocation by another skill.** `precap` asks its agent to run `$recall` or
  `/recall` when installed (SRC-1, `precap/skills/precap/SKILL.md`). `recap`
  bypasses the skill and calls the engine directly (see below).

### Ordinary invocation, end to end: local find/verify

This is [RT-RTE-local-search-read](#rt-rte-local-search-read).

1. **Trigger and principal.** A user in a host session asks, for example,
   "what did we do last time about X". The principal is that user; the
   identity under which commands run is the host agent's OS user and shell.
2. **Interface selection** ([RT-RTE-interface-selection](#rt-rte-interface-selection)).
   The model checks whether Recall MCP tools exist, or whether `RECALL_URL`,
   `RECALL_MODE` or `~/.config/recall-brain/client.json` signals central
   mode. If so it switches to the central procedure, which uses MCP tools
   when present and otherwise the same CLI as a remote client (`doctor`
   reports the configured mode; `show '<recall://receipt>'` opens remote
   receipts). Otherwise it uses the local CLI through `RECALL_SCRIPT`. If
   neither interface exists it reports the missing dependency and stops.
3. **Outcome choice.** The model classifies the request as find/verify,
   continue, repeat or skill-ify, asking the user only when ambiguous. The
   decision policy is natural-language instruction interpreted by the model.
4. **Search.** The model runs `python3 "$RECALL_SCRIPT" search "<user
   phrasing + identifiers>"` with flags for time, cwd, harness and branch.
   The skill instructs flags over query text and UTC conversion of local days.
5. **Evidence check.** The model reads the `WHY` line of the top results and
   prefers a hit whose `WHY` contains an identifier, phrase or exact-entity
   match over rank 1. Empty output means nothing cleared the engine's evidence
   gate; retry once, then report what was searched.
6. **Bounded read.** `show <path> --around <timestamp>` prints a ±3-turn
   window. The reason given is size:

   > Use `show` rather than
   > `cat`: sessions can reach 80 MB, and `show` parses and prints only the requested
   > content.
   > --- `recall/skills/recall/SKILL.md`

7. **Terminal output.** The model answers in the session with the session
   path as the receipt.

Context, state and effect boundary: the search result and the `show` window
enter the host model's context as tool output for the current invocation only.
The skill itself persists nothing. The engine reads transcripts and maintains
an index ([RT-OBJ-session-index](#rt-obj-session-index)) under its own
declared contract. Coordination is single-agent; there is no delegation in the
skill. Recovery is limited to "retry once with a distinctive identifier or a
wider window" and running `index` when results look stale.

### Material alternate and forcing routes

- [RT-RTE-cold-scan](#rt-rte-cold-scan): when no index exists, the model
  reads raw JSONL transcripts with `rg` and starts a detached `index` process.
- [RT-RTE-related-sessions](#rt-rte-related-sessions): query-free retrieval by
  shared cwd, branch or touched files.
- [RT-RTE-remote-brain-read](#rt-rte-remote-brain-read): MCP
  `recall_search` → `recall_show` (receipt only) →
  `recall_session_context` / `recall_exec` → cite `opened_receipts`; without
  MCP tools, the CLI acts as the central client.
- [RT-RTE-outcome-playbooks](#rt-rte-outcome-playbooks): continue, repeat and
  skill-ify variants of the read step.
- [RT-RTE-skillify-admission](#rt-rte-skillify-admission): writes a new skill
  package that later sessions can load.
- [RT-RTE-brain-capture](#rt-rte-brain-capture): user-requested
  `recall_capture` and exact-receipt `recall_forget`.
- [RT-RTE-session-export](#rt-rte-session-export): paged machine export and
  relation graph, consumed in-repo by `recap`.
- [RT-RTE-index-maintenance](#rt-rte-index-maintenance): `index`, `doctor`,
  and the consent rule for `index --rebuild`.
- [RT-RTE-package-change-gate](#rt-rte-package-change-gate): how changes to
  the skill package itself are checked in the repository.

### Load-bearing guarantees and where they hold

Each guarantee below is enforced, if at all, by the host model reading the
instruction, unless stated otherwise. The host grants the model shell access
for the CLI route; that same shell access is a materially equivalent
alternate path around every model-enforced rule.

**G1. No local fallback when central mode is configured.**

> Do not run the local CLI
> as a parallel or fallback retrieval path.
> --- `recall/skills/recall/SKILL.md`

- Owner: skill author; enforcement point: host model compliance.
- Guarantee strength: policy.
- Covered paths: retrieval launched through this skill.
- Alternate paths: direct shell use of `RECALL_SCRIPT`; the cold-scan `rg`
  path reads `~/.claude/projects` directly; `recap` resolves the engine from
  `--recall-script`, `RECALL_SCRIPT` or three fixed home paths without reading
  any central-mode signal (SRC-1, `recap/skills/recap/scripts/recap.py`,
  `recall_candidates`). `recap` does refuse `recall://` targets for relation
  graphs, so a remote receipt does not silently resolve locally there.
- Required external contract: the engine's own mode routing, reported by
  `doctor`, which is uninspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected

**G2. Redaction and no stored thinking.** The skill states the engine never
stores reasoning blocks and redacts secret-shaped lines at ingest
([RT-CLM-ingest-redaction](#rt-clm-ingest-redaction)).

- Owner: engine; enforcement point: engine ingest (absent from SRC-1).
- Guarantee strength: no claimed guarantee from the skill itself; the
  engine's guarantee is declared only.
- Covered paths: indexed `search`, `show`, `session-export`, as the skill
  describes them.
- Forcing case: [RT-RTE-cold-scan](#rt-rte-cold-scan) reads raw transcripts
  with `rg -n -i -C3`. That path does not pass through the engine, so whatever
  the host wrote to the transcript, including any secret-shaped line, reaches
  the model's context unredacted. Whether host transcripts contain thinking
  text is a host fact outside the boundary. The `show`-over-`cat` instruction
  is justified by size, not privacy, and shell `cat` remains available.
- implementation conclusion status: claimed
- operation conclusion status: uninspected

**G3. Local mode touches no network.**

> Otherwise everything below is fully local and nothing
> touches a network.
> --- `recall/skills/recall/SKILL.md`

- Owner: engine and its deployment configuration; enforcement point: engine
  mode routing (absent).
- Guarantee strength: deployment guarantee.
- Covered paths: CLI commands when no central signal is present.
- Alternate paths: none inspected; the `rg` and `show` steps are local file
  reads by construction of the command text.
- implementation conclusion status: claimed
- operation conclusion status: uninspected

**G4. Capture only on user request, private by default; forget only by exact
receipt.** See [RT-RTE-brain-capture](#rt-rte-brain-capture).

- Owner: skill author for the request rule; the service for permissions
  ("Source and visibility permissions come from the configured service").
- Enforcement point: host model compliance; service-side enforcement
  uninspected.
- Guarantee strength: policy.
- Alternate paths: any MCP-capable model can call `recall_capture` outside
  this skill; whether the service requires user consent is unknown.
- implementation conclusion status: wired
- operation conclusion status: uninspected

**G5. Empty result is not proof of absence.** SKILL.md says empty output
"does not prove the work never happened". The cookbook's scripting note says
the opposite at face value:

> Empty stdout = confident no-answer. Non-zero exit = the engine itself failed.
> --- `recall/skills/recall/references/query-cookbook.md`

The two can be reconciled as "the engine ran and found nothing above the gate"
versus "the work did not happen", but the text does not say so. The pi gotcha
adds a scoped case: a cold result does not prove no pi session exists, because
pi sessions are not indexed. The guarantee is advisory (policy) and its
wording is inconsistent across the two shipped files.

- implementation conclusion status: wired
- operation conclusion status: uninspected

**G6. Export completeness and fail-closed identity** for
[RT-RTE-session-export](#rt-rte-session-export). The skill describes pages
with `complete` and `next_cursor`, `source_snapshot_stable`, and `--current`
failing closed without exact `CODEX_THREAD_ID` or `CLAUDE_SESSION_ID`. The
producer is absent (claimed). The in-repo consumer `recap` does enforce its
side in code: it rejects non-zero exits, invalid JSON, an unsupported
`schema_version`, a changed boundary between pages, discontinuous sequence,
an incomplete page without cursor, and a page-count overrun (SRC-1,
`recap/skills/recap/scripts/recap.py`). That is consumer-side protocol
enforcement attributable to `recap`, not to Recall.

- producer implementation conclusion status: claimed
- consumer implementation conclusion status: wired

**G7. No `index --rebuild` without explicit user request.** Policy, enforced
by model compliance; shell access is the alternate path. See
[RT-RTE-index-maintenance](#rt-rte-index-maintenance).

**Capability surface, grant set and isolation.** The procedure needs shell
execution (`python3`, `rg`, `ls`, `git -C`, `setsid nohup`), read access to
`~/.claude/projects` and `~/.codex/sessions`, file writes for skill-ify, and
MCP tool calls in central mode. The Codex manifest declares
`"capabilities": ["Read"]` in its `interface` block (SRC-1,
`recall/.codex-plugin/plugin.json`); the shipped procedure exceeds a read-only
reading of that label, and whether Codex enforces it is a host fact outside
the boundary. The skill has no `allowed-tools` restriction
([RT-ABS-tool-restriction](#rt-abs-tool-restriction)). The current grant set
and isolation envelope are therefore whatever the host session grants; the
target supplies none. The detached `setsid nohup ... index` process escapes
the agent's process lifetime.

### Distributed-parametric component

The only distributed-parametric component on these routes is the host model
([RT-CMP-host-model](#rt-cmp-host-model)). The engine's ranking may use dense
representations, but the skill describes an entity index, a token leg and a
phrase-before-terms match, all symbolic as declared; embedding use is not
stated and remains uninspected.

### Change-admission mechanisms

- Retained knowledge: automatic indexing by the engine, declared to cover
  Claude Code and Codex transcripts but not pi sessions or thinking blocks
  ([RT-RTE-index-maintenance](#rt-rte-index-maintenance)). The skill
  implements only the trigger; the ingest is declared contract, and the skill
  has no per-content admission. Deliberate Brain capture on user request
  ([RT-RTE-brain-capture](#rt-rte-brain-capture)).
- Capabilities: skill-ify writes a new skill package
  ([RT-RTE-skillify-admission](#rt-rte-skillify-admission)).
- Product and production machinery: changes to `recall/` go through
  repository commits; CI does not run the instruction-only test on
  `recall/**` changes ([RT-RTE-package-change-gate](#rt-rte-package-change-gate)).
- No route in the package revises the skill's own instructions from use.

### Unobserved and out of reach

Engine ranking, the evidence gate, identifier matching, redaction, index
freshness, central mode routing, service permissions, capture and deletion
semantics, and host skill selection are all unobserved; the first eight are
absent from SRC-1, the last is a host responsibility. No Recall execution
trace exists in SRC-1. The memory analyst owns retained-content revision
questions; this account names the write routes only.

## Shared records

### Components

#### RT-CMP-recall-skill

Label: Recall skill instructions

- Source-native identity: `recall` skill, `recall/skills/recall/SKILL.md`,
  with `references/central-brain.md` and `references/query-cookbook.md`.
- Representational form: natural language with embedded command templates;
  consumed by the host model's interpretation.
- Storage substrate: Markdown files in the installed skill directory.
- Evidence: SRC-1, `recall/skills/recall/SKILL.md` (`implementation` for the
  agent-side procedure).

#### RT-CMP-recall-engine

Label: Recall engine

- Source-native identity: `recall.py`, reached through the operator-set
  `RECALL_SCRIPT` environment variable.
- Representational form: executable code, symbolic as declared; uninspected.
- Storage substrate: a privately installed file outside the repository; its
  index is [RT-OBJ-session-index](#rt-obj-session-index).
- Evidence: SRC-1, `recall/skills/recall/SKILL.md` (`doctrine/design` only).
  [RT-ABS-engine-code](#rt-abs-engine-code) records its absence from SRC-1.

#### RT-CMP-central-brain

Label: Central Recall Brain

- Source-native identity: "central Recall Brain", reached through MCP tools
  `recall_search`, `recall_show`, `recall_session_context`, `recall_exec`,
  `recall_capture`, `recall_forget`, or `RECALL_URL`/`RECALL_MODE`.
- Representational form: remote service; uninspected.
- Storage substrate: private service storage; uninspected.
- Evidence: SRC-1, `recall/skills/recall/references/central-brain.md`
  (`doctrine/design`).

#### RT-CMP-host-model

Label: Host agent model

- Source-native identity: the model behind Claude Code, Codex or pi.
- Representational form: distributed-parametric.
- Storage substrate: provider- or host-managed weights; inaccessible.
- Parameters changing during operation: uninspected — provider internals are
  outside SRC-1; the skill neither claims nor relies on weight updates.
- Exact version pinned: no — the skill and manifests name no model.
- Mutable endpoint: yes as far as the target is concerned — the host chooses
  the model, so the same skill can run on any model the host resolves.
- Evidence: SRC-1, `recall/skills/recall/SKILL.md` frontmatter (no model
  field), `recall/.claude-plugin/plugin.json`, `recall/.codex-plugin/plugin.json`.

### Operative objects

#### RT-OBJ-session-transcripts

Label: Raw host session transcripts

- Source-native identity: JSONL files under `~/.claude/projects` and
  `~/.codex/sessions`; subagent transcripts under
  `<session-uuid>/subagents/…`.
- Representational form: symbolic JSON records containing natural-language
  turns and tool input/output.
- Storage substrate: host filesystem, written by the host harness, subject to
  host retention (`cleanupPeriodDays`).
- Evidence: SRC-1, `recall/skills/recall/SKILL.md` (cold-scan commands and
  gotchas).

#### RT-OBJ-session-index

Label: Recall SQLite index

- Source-native identity: "a local SQLite engine" index with an entity index.
- Representational form: symbolic as declared; internal structure uninspected.
- Storage substrate: local SQLite database (location not stated); WAL
  temporary space on rebuild.
- Evidence: SRC-1, `recall/skills/recall/SKILL.md`,
  `recall/skills/recall/references/query-cookbook.md` (`doctrine/design`).

#### RT-OBJ-recall-receipt

Label: Recall receipt

- Source-native identity: session file path (local) or `recall://` receipt
  and `opened_receipts` (remote, opened by `recall_show` or by the CLI's
  `show '<recall://receipt>'`); `logical_document_id` for documents.
- Representational form: symbolic identifier.
- Storage substrate: returned in tool output; persisted only if the answer or
  a later artifact repeats it.
- Evidence: SRC-1, `recall/skills/recall/SKILL.md`,
  `recall/skills/recall/references/central-brain.md`.

#### RT-OBJ-session-export

Label: Session export pages

- Source-native identity: `recall.session-export.v1` JSON pages and
  `recall.session-relations.v1` graph; cursors stored "owner-private under
  `~/.recall`".
- Representational form: symbolic JSON with redacted natural-language text
  and digests.
- Storage substrate: stdout of the engine; cursors on local disk.
- Evidence: SRC-1, `recall/skills/recall/SKILL.md` (`doctrine/design`);
  consumer checks in `recap/skills/recap/scripts/recap.py` (`implementation`,
  consumer side).

#### RT-OBJ-brain-record

Label: Captured Brain record

- Source-native identity: a record created by `recall_capture`, identified by
  its canonical receipt.
- Representational form: natural-language decision or finding, as selected by
  the model; service encoding uninspected.
- Storage substrate: central Brain service storage; uninspected.
- Evidence: SRC-1, `recall/skills/recall/references/central-brain.md`.

#### RT-OBJ-generated-skill

Label: Skill-ified package

- Source-native identity: a standard `SKILL.md` package or Agent Skills
  directory produced by the skill-ify outcome.
- Representational form: natural-language instructions with commands.
- Storage substrate: host skill directory on disk; location chosen by the
  harness skill creator or the model.
- Evidence: SRC-1, `recall/skills/recall/SKILL.md`.

### Routes

#### RT-RTE-interface-selection

Label: Interface selection

- Endpoints: skill load → central procedure (MCP tools, or the CLI as a
  remote client), local CLI procedure, or stop.
- Progression: check for Recall MCP tools, `RECALL_URL`, `RECALL_MODE`
  `remote`/`shadow`, or `~/.config/recall-brain/client.json`; under a central
  signal use MCP tools when present, else the `RECALL_SCRIPT` CLI with
  `doctor` to check the configured mode; with no central signal require
  `RECALL_SCRIPT` for local use; else report and stop without fetching old
  commits or archived packages.
- Owner: host model under [RT-CMP-recall-skill](#rt-cmp-recall-skill).
- Context/state/action effects: decides which tools the model uses; no state.
- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: inapplicable — selection returns no material; it selects the next procedure.
- Later read-back: inapplicable — nothing is retained by selection.
- Delegated visibility: inapplicable — no delegation.
- Selection predicate: presence of MCP tools or the three central-mode signals; otherwise presence of `RECALL_SCRIPT`.
- Invalidation or expiry: inapplicable — evaluated per invocation.
- Activation or effect: routes the invocation to [RT-RTE-remote-brain-read](#rt-rte-remote-brain-read) or [RT-RTE-local-search-read](#rt-rte-local-search-read), or ends it with a dependency report.
- Evidence limits: model compliance with G1 is unobserved; the engine's own mode routing is absent from SRC-1. Under a central signal without MCP tools, what the CLI's `search` does is not stated, and `shadow` mode is named without a defined meaning, so neither which store answers nor whether `shadow` answers come from a single store can be established.

> If neither interface is available, report the missing dependency and stop.
> --- `recall/skills/recall/SKILL.md`

The CLI also serves as a central client, not only as the local path:

> For the separately installed CLI, the operator sets `RECALL_SCRIPT` to its
> absolute path. Run `python3 "$RECALL_SCRIPT" doctor` to check the configured
> mode. Open a remote receipt with:
> --- `recall/skills/recall/references/central-brain.md`

> `RECALL_MODE` is `remote` or `shadow`
> --- `recall/skills/recall/SKILL.md`

#### RT-RTE-local-search-read

Label: Local search and read

- Endpoints: user question → answer with session path receipt.
- Progression: outcome choice → `search` with flags → `WHY` check → `show
  --around` → answer.
- Owner: host model; engine executes `search` and `show`.
- Context/state/action effects: search rows and the shown window enter the
  current context; no write by the skill.
- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: ranked sessions with date, cwd, slot, branch, snippet and `WHY`; then a ±3-turn window from `show`.
- Later read-back: prior sessions' transcripts, accumulated through use and indexed by the engine, reach this invocation; that is the retained material this route reads back.
- Delegated visibility: inapplicable — single-agent route.
- Selection predicate: engine ranking over the user's phrasing, identifiers and filter flags, then the model's choice of the hit whose `WHY` shows an identifier, phrase or exact-entity match.
- Invalidation or expiry: host transcript retention deletes sources; index staleness is handled by running `index`; no invalidation in the skill itself.
- Activation or effect: the window is meant to ground the answer; activation is unobserved.
- Evidence limits: ranking, the evidence gate and exact-identifier matching are declared only; no run trace.

> Prefer a result whose `WHY` includes an identifier, phrase,
> or exact-entity match rather than selecting rank 1 automatically.
> --- `recall/skills/recall/SKILL.md`

Conditional fields (candidate comparison): the engine proposes ranked
candidates; the host model selects; the user can redirect. No answer oracle:
the `WHY` line is engine-produced match evidence, and the model's judgment of
it is not an expected answer. Operating mode: open requests.

#### RT-RTE-cold-scan

Label: Cold transcript scan

- Endpoints: missing index → answer from raw transcripts, plus a background
  index build.
- Progression: `rg -l -i` over transcript roots → `ls -t` → `rg -n -i -C3`
  on the best hit; concurrently `setsid nohup python3 "$RECALL_SCRIPT" index`.
- Owner: host model; `rg` and the detached engine process execute.
- Context/state/action effects: raw transcript lines enter context; a
  detached process starts building [RT-OBJ-session-index](#rt-obj-session-index).
- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: matching file list and ±3-line windows from raw JSONL.
- Later read-back: prior host transcripts reach this invocation unmediated by the engine.
- Delegated visibility: the detached index process reads whatever transcripts the engine's declared ingest scope covers (Claude Code and Codex); its output is discarded to `/dev/null`.
- Selection predicate: model-chosen terms and regular expressions; recency by `ls -t`.
- Invalidation or expiry: ends when `doctor` shows a healthy db and the model switches to indexed search.
- Activation or effect: grounds an answer the skill requires labelling as a cold scan; bypasses engine redaction (G2).
- Evidence limits: whether host transcripts contain thinking or secrets is a host fact; no run trace.

> Tell the user when an answer came from a cold scan of the
> raw transcripts.
> --- `recall/skills/recall/SKILL.md`

#### RT-RTE-related-sessions

Label: Related sessions lookup

- Endpoints: session start with implicit reference to prior work → ranked
  related sessions.
- Progression: `related --cwd "$(pwd)" --branch "$(git branch --show-current)"`.
- Owner: host model; engine ranks.
- Context/state/action effects: related-session list enters context.
- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: sessions sharing project, branch or touched files.
- Later read-back: prior sessions' metadata reaches the current invocation.
- Delegated visibility: inapplicable — single-agent route.
- Selection predicate: overlap of cwd, branch and touched files, and recency, as declared.
- Invalidation or expiry: inapplicable — no retained output.
- Activation or effect: supplies candidates without a query; activation unobserved.
- Evidence limits: ranking is declared only.

#### RT-RTE-remote-brain-read

Label: Remote Brain read

- Endpoints: question → answer citing `opened_receipts`.
- Progression: `recall_search` → `recall_show` with only `target`, following
  the continuation cursor until `complete` → `recall_session_context` for
  neighbors → `recall_exec` with `logical_document_id` for full documents.
  Without MCP tools, the CLI is the central client: `doctor` reports the
  configured mode and `show '<recall://receipt>'` opens a remote receipt;
  local paths and `--tail`, `--around` and `--prompts` do not open remote
  receipts. The skill does not say what CLI `search` returns in central or
  `shadow` mode.
- Owner: host model; the service executes, through MCP tools or the engine CLI.
- Context/state/action effects: opened records enter context; no write.
- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: search snippets, then opened record text with receipts.
- Later read-back: records synced or captured earlier, possibly from other devices or imports, reach this invocation.
- Delegated visibility: inapplicable — single-agent route; service visibility rules are external.
- Selection predicate: service search over identifiers, source filters and UTC bounds, then model selection; snippets are "pointers to evidence".
- Invalidation or expiry: `recall_forget` removes an exact record; other expiry uninspected.
- Activation or effect: the skill restricts citation to opened receipts whose text supports the answer and requires stating gaps.
- Evidence limits: service behavior, permissions and sync are absent from SRC-1; the CLI's central-mode search behavior and the meaning of `shadow` are unstated, so single-store answer provenance is established only as the instruction's intent for the MCP path.

> Cite only `opened_receipts` whose returned text supports the answer.
> --- `recall/skills/recall/references/central-brain.md`

#### RT-RTE-outcome-playbooks

Label: Outcome playbooks

- Endpoints: search hit → continue, repeat or skill-ify input.
- Progression: continue: `show --tail 30` → `git -C <cwd> branch
  --show-current` → summary and "resume there or here?"; repeat: `show
  --prompts` → present prompts verbatim → confirm fresh inputs before
  re-running.
- Owner: host model.
- Context/state/action effects: prior session tail or prompts enter context;
  repeat may re-run prior prompts after confirmation.
- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: final turns, or the session's user prompts.
- Later read-back: prior session prompts and final state reach the current invocation and can drive new actions.
- Delegated visibility: inapplicable — single-agent route.
- Selection predicate: outcome classification by the model; then the chosen session from [RT-RTE-local-search-read](#rt-rte-local-search-read).
- Invalidation or expiry: the skill asks continue to "check the session's branch/slot still exists", but its command, `git -C <cwd> branch --show-current`, reports only the branch currently checked out in `<cwd>` (a reading of the command text, not an observed run); it does not establish that the prior session's branch still exists. Nothing else.
- Activation or effect: user confirmation is requested before resuming or re-running.
- Evidence limits: confirmation is an instruction to the model, not enforced.

#### RT-RTE-skillify-admission

Label: Skill-ify admission

- Endpoints: working window from a prior session → new skill package
  ([RT-OBJ-generated-skill](#rt-obj-generated-skill)).
- Progression: search → `show` working window → separate durable recipe from
  one-off data → invoke harness skill creator, or write a standard `SKILL.md`
  package directly.
- Owner: host model; the external skill creator when installed.
- Context/state/action effects: writes files that hosts may load as skills.
- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: the new skill package path, as produced by the model or creator.
- Later read-back: later sessions may load the generated skill; that consumer is the host's skill loader.
- Delegated visibility: the external skill creator receives the recipe and a proposed name.
- Selection predicate: the model's judgment of which steps "worked" and which data are one-off.
- Invalidation or expiry: none in the skill; removal is manual.
- Activation or effect: capability change for later sessions; activation unobserved.
- Evidence limits: the external creator's admission behavior is outside SRC-1.

Admission fields: trigger is a user request matching skill-ify. Proposed change
is a new skill. The skill states no approval step before writing; it says to
ask "only if the outcome is genuinely ambiguous". Rejection ability rests with
the user in conversation, the host's file-write permissions, or the external
creator. Rollback is deleting the files; no recovery procedure is given. The
guidance shaping the proposal is the instruction to keep "commands, endpoints,
auth patterns" and drop "specific IDs, dates". What persists is the generated
package only; no link back to the source session is required.

#### RT-RTE-brain-capture

Label: Brain capture and forget

- Endpoints: user request → `recall_capture` record with canonical receipt;
  or exact receipt → `recall_forget`.
- Progression: user requests capture → model selects decisions or findings →
  `recall_capture`, private by default → return receipt.
- Owner: host model selects content; the service admits.
- Context/state/action effects: writes to or deletes from the remote store.
- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: canonical receipt.
- Later read-back: captured records become searchable through [RT-RTE-remote-brain-read](#rt-rte-remote-brain-read) in later sessions, possibly on other devices.
- Delegated visibility: shared visibility only when the user explicitly selects it; service permissions govern.
- Selection predicate: model selection of "selected decisions or findings", excluding secrets, hidden reasoning, whole transcripts and unselected third-party content.
- Invalidation or expiry: `recall_forget` on the exact receipt only.
- Activation or effect: retained-knowledge change; activation unobserved.
- Evidence limits: service-side consent, permission and deletion semantics are absent.

> Capture durable information only when the user requests it.
> --- `recall/skills/recall/references/central-brain.md`

Admission fields: trigger is a user request; the model proposes the captured
content; the user starts the action, but the skill does not require the user to
approve the selected text before capture. The service decides acceptance;
rejection behavior is uninspected. Rollback is `recall_forget` by exact
receipt.

#### RT-RTE-session-export

Label: Session export

- Endpoints: exact session (current, path or receipt) → ordered JSON pages, or
  a native relation graph.
- Progression: `session-export --current|--target|--cursor --limit 1000`
  repeated until `complete`; `session-relations --chain --include-children`.
- Owner: engine produces; the consuming skill's code or agent drives.
- Context/state/action effects: cursors stored under `~/.recall`; pages go to
  the consumer.
- producer implementation conclusion status: claimed
- consumer implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: pages with evidence IDs, redacted text, digests, entities, receipts, `complete` and `next_cursor`.
- Later read-back: inapplicable — the export reads one session for the current consumer; durable use belongs to the consumer.
- Delegated visibility: `recap` receives only the exported page content, not raw transcripts, when it uses this route.
- Selection predicate: exact native identity (`CODEX_THREAD_ID`, `CLAUDE_SESSION_ID`) or exact path; otherwise fail closed with candidate receipts.
- Invalidation or expiry: `source_snapshot_stable` signals a live source advancing; cursor lifetime not stated.
- Activation or effect: consumer-side checks in `recap` reject malformed or inconsistent pages.
- Evidence limits: producer absent; consumer checks belong to `recap`, outside the functional boundary.

> if page.get("schema_version") != "recall.session-export.v1":
> --- `recap/skills/recap/scripts/recap.py`

#### RT-RTE-index-maintenance

Label: Index maintenance

- Endpoints: stale results or setup → refreshed index; `doctor` → health and
  retention warnings.
- Progression: `index` (incremental), `doctor`; `index --rebuild` only on
  explicit user request; surface a `cleanupPeriodDays` warning immediately.
- Owner: host model triggers; engine ingests.
- Context/state/action effects: the model issues `index`, `doctor` or the
  detached cold-start `index`; the engine, as declared, writes
  [RT-OBJ-session-index](#rt-obj-session-index) from Claude Code and Codex
  transcripts, excluding pi sessions and reasoning/thinking blocks and
  redacting secret-shaped lines. That ingest scope is declared contract only.
- trigger implementation conclusion status: wired
- ingest implementation conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: `doctor` prints coverage, index age, mode and retention watchdog.
- Later read-back: as declared, an ingested Claude Code or Codex session, including this one once its transcript is ingested, becomes searchable by later invocations; pi sessions do not.
- Delegated visibility: inapplicable — no delegation.
- Selection predicate: the engine's declared ingest scope (Claude Code and Codex transcripts; pi not indexed; thinking blocks never stored); per-content admission is not described.
- Invalidation or expiry: host retention deletion of transcripts; how the index treats deleted sources is uninspected.
- Activation or effect: trace-fed retained material for later retrieval, as declared; activation unobserved.
- Evidence limits: only the model-issued commands are in SRC-1; ingest, its scope, redaction and incremental logic are absent ([RT-ABS-engine-code](#rt-abs-engine-code)), so the write itself is `doctrine/design` evidence.

The two status fields separate what the skill text implements from what it
declares. The trigger is the command text the model is asked to run. The
ingest that writes retained material belongs to the absent engine. The
declared scope is narrower than all host history:

> the current index covers Claude Code and Codex transcripts
> --- `recall/skills/recall/SKILL.md`

> Running Recall from pi is supported, but pi's own session format is not yet
> indexed.
> --- `recall/skills/recall/SKILL.md`

> Never run `index --rebuild` without the user's explicit request;
> --- `recall/skills/recall/SKILL.md`

Admission fields: trigger is the agent or a background process; the proposed
change is ingesting transcripts within the declared scope. No content-level
admission or rejection is described; the engine's redaction and its exclusion
of thinking blocks are the only declared filters. Recovery is `index` or a
user-approved `--rebuild`.

#### RT-RTE-package-change-gate

Label: Package change gate

- Endpoints: commit touching `recall/` → package published through
  skills.sh or plugin marketplaces.
- Progression: `tests/test_portability.py` asserts `recall/` holds only
  `.md`, `.json`, `.yaml` and `LICENSE`, that `package.json` is private with
  no `bin`, and that the pi caveat text is present. CI runs it through root
  `npm test` in `.github/workflows/desloppify-ci.yml`, whose path filters do
  not include `recall/**`. `.github/workflows/secret-scan.yml` runs gitleaks
  on every push and pull request to `main`.
- Owner: repository maintainers and CI.
- Context/state/action effects: production-machinery change admission.
- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: CI pass or fail.
- Later read-back: inapplicable — a build check, not retained material.
- Delegated visibility: inapplicable — no delegation.
- Selection predicate: path filters on the workflow; a change confined to `recall/` does not trigger the portability job.
- Invalidation or expiry: inapplicable — per change.
- Activation or effect: the instruction-only test runs in CI only when a listed path also changes; it can run locally at any time.
- Evidence limits: branch protection and publication steps are outside SRC-1.

```text
paths:
  - "desloppify/**"
  - "package.json"
  - "README.md"
  ...
  - "tests/test_portability.py"
```

### Claims

#### RT-CLM-exact-identifier-matching

Label: Exact identifier matching

Claimed operation: identifiers are matched exactly through the entity index
and a token leg, including inside tool output; error strings are tried as a
phrase before term matching. Source: SRC-1,
`recall/skills/recall/references/query-cookbook.md`,
`recall/skills/recall/SKILL.md` (`doctrine/design`).

> Identifiers are matched exactly via the entity index and a dedicated token
> leg
> --- `recall/skills/recall/references/query-cookbook.md`

#### RT-CLM-evidence-gate

Label: Search evidence gate

Claimed operation: search output is limited to results that clear an evidence
gate, each with a `WHY` explanation. Source: SRC-1,
`recall/skills/recall/SKILL.md` (`doctrine/design`).

> Empty output means nothing cleared the evidence gate;
> --- `recall/skills/recall/SKILL.md`

#### RT-CLM-ingest-redaction

Label: Ingest redaction

Claimed operation: the engine indexes user text, assistant text and tool
input/output, never stores reasoning/thinking blocks, and redacts
secret-shaped lines at ingest. Source: SRC-1, `recall/skills/recall/SKILL.md`
(`doctrine/design`).

> reasoning/thinking blocks are never stored, and secret-shaped lines are
> redacted at ingest.
> --- `recall/skills/recall/SKILL.md`

#### RT-CLM-local-only

Label: Local mode offline

Claimed operation: without central configuration, Recall is fully local and
touches no network. Source: SRC-1, `recall/skills/recall/SKILL.md`; quoted
under G3 above.

#### RT-CLM-export-fail-closed

Label: Export fails closed

Claimed operation: `session-export --current` resolves only through exact
native session IDs and otherwise fails closed with content-free candidate
receipts; `session-relations` fails on missing or ambiguous native links.
Source: SRC-1, `recall/skills/recall/SKILL.md` (`doctrine/design`).

> Otherwise it fails closed with content-free ranked
> candidate receipts;
> --- `recall/skills/recall/SKILL.md`

### Evidenced absences

#### RT-ABS-engine-code

Label: Engine code absent

- Status: absent
- Searched: all tracked files at `c82883b15e5e8f02483bee513b3c8dcac48e3c9e`
  via `git ls-files | grep -i -E "recall|\.github/workflows"`, and
  `grep -rn -i -E "allowed-tools|recall\.py|sqlite"` over `recall/`.
- Evidence: the only tracked `recall` paths are the eight package files; the
  only `recall.py` mention is the instruction to set `RECALL_SCRIPT`.
  `tests/test_portability.py` enforces instruction-only content.
- Conclusion supported: no engine, index, ranking, redaction or export
  producer is inspectable in SRC-1. Conclusion prevented: any
  implementation-level claim about them.

#### RT-ABS-tool-restriction

Label: No tool restriction

- Status: absent
- Searched: `recall/` at `c82883b15e5e8f02483bee513b3c8dcac48e3c9e`, query
  `allowed-tools`; frontmatter of `recall/skills/recall/SKILL.md` read in
  full (only `name` and `description`).
- Evidence: no match; the Codex manifest's `"capabilities": ["Read"]` is the
  only capability declaration.
- Conclusion supported: the package itself narrows no tool grant; isolation
  is entirely the host's. Conclusion prevented: whether any host enforces the
  Codex capability label (host behavior is outside SRC-1).

### Behavioral-authority paths

#### RT-BAP-skill-instructions

Label: Skill instructions to model

- Consumer: host model ([RT-CMP-host-model](#rt-cmp-host-model)).
- Channel: host skill loading places [RT-CMP-recall-skill](#rt-cmp-recall-skill) and referenced files in context.
- Force: natural-language instruction; advisory, unenforced by code.
- Horizon: each invocation where the host selects the skill.

#### RT-BAP-retrieved-sessions

Label: Retrieved session content

- Consumer: host model in the current invocation.
- Channel: tool output from `search`, `show`, `rg`, `recall_show` and related tools.
- Force: evidence the model is told to ground answers in; in repeat and continue, prior prompts and state can drive new actions after user confirmation.
- Horizon: the current invocation; the material comes from earlier sessions.

#### RT-BAP-generated-skill

Label: Generated skill package

- Consumer: the host skill loader and the model in later sessions.
- Channel: [RT-OBJ-generated-skill](#rt-obj-generated-skill) on disk, discovered as a skill.
- Force: natural-language instruction, as for any skill.
- Horizon: later sessions until removed.

#### RT-BAP-brain-records

Label: Captured Brain records

- Consumer: host models in later sessions using [RT-RTE-remote-brain-read](#rt-rte-remote-brain-read).
- Channel: service search and `recall_show`.
- Force: evidence delivered on request.
- Horizon: later sessions and devices until `recall_forget`.

## Annotations

none
