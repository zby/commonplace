---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "OKF memory: editable Markdown knowledge, provenance and lifecycle metadata, selective retrieval, and Pro retained work-state feedback."
run-id: AAS-2026-11-08-okf-8bc42addf404-01
source-identity: https://github.com/serradura/okf
reviewed-boundary: "cfb7ffac7fef37d56e97b5b7dd8fe97ffc648c7c"
---

# OKF memory report

## Boundary and evidence

The memory boundary includes all four gems, baseline skills, plugin feedback and Pro's shipped operating profile. It follows the whole-system boundary, not just the MCP store. Retained knowledge, authored navigation, work records, mechanical snapshots, telemetry and installed instruction text have different consumers. The external agent host, its conversation storage and model parameters are outside the inspected implementation. Optional SQLite backend internals are unavailable in SRC-1; their persistence, representation and selection cannot be inferred from the fallback seam.

All direct reads below are SRC-1 implementation or doctrine/design at the frozen commit. Supplied runtime findings are identified separately. No observed run or causal experiment was supplied. Source-dependent quotations support implementation or requested behavior, not successful agent compliance.

| Entry point / operation | Source path in SRC-1 | Coverage and limit |
|---|---|---|
| CLI dispatch and read views | `gems/okf/lib/okf/cli.rb`, `gems/okf/lib/okf/bundle/search.rb` | Direct registry/field vocabulary and search-facade reads; supplied [RT-CMP-cli](runtime.md#rt-cmp-cli), [RT-RTE-skill-work](runtime.md#rt-rte-skill-work) cover dispatch and CLI search. Engine internals not independently audited here; no measured ranking effectiveness conclusion. |
| Acquire, distill, migrate, maintain | `skills/okf/playbooks/produce.md`, `skills/okf/playbooks/migrate.md`, `skills/okf/playbooks/maintain.md`, `skills/okf/playbooks/consume.md` | Direct doctrine reads; [MEM-OBJ-concept-body](#mem-obj-concept-body), [MEM-OBJ-concept-metadata](#mem-obj-concept-metadata), annotations on [RT-RTE-skill-work](runtime.md#rt-rte-skill-work). Admission is agent judgment and subsequent structural checks, not obligatory human review of each ordinary concept. |
| Load, parse, publish, reload | `gems/okf/lib/okf/bundle/reader.rb`, `gems/okf/lib/okf/concept.rb` | Direct Reader and relevant Concept fields; supplied [RT-RTE-publish-bundle](runtime.md#rt-rte-publish-bundle) covers Writer's distinct validation gate. Hidden files and unusable entries do not become searchable concepts. |
| MCP registered retrieval and alternate attachment | `gems/okf-mcp/lib/okf/mcp/server.rb`, `gems/okf-mcp/lib/okf/mcp/resources.rb` | Direct handlers for list_bundles, dirs, index, search, read_concept, catalog, log, validate, lint, graph, references, prompts and resource reads; [RT-RTE-mcp-retrieve](runtime.md#rt-rte-mcp-retrieve) and annotation. Residency/byte-cut implementation supplied by runtime, not independently re-audited. No host-use or whole-window budget conclusion. |
| Browser and TUI consumers | `gems/okf/lib/okf/server/app.rb`, `gems/okf/lib/okf/server/hub.rb`, `gems/okf-tui/lib/okf/tui/workspace.rb` | Supplied runtime account and [RT-RTE-registry-manage](runtime.md#rt-rte-registry-manage), not direct UI-body reads here. Human browsing and registry edits are distinct from model-context delivery; UI rendering fidelity not assessed. |
| Post-edit curation feedback | `plugin/hooks/scripts/curate.rb` | Supplied [RT-RTE-curation-feedback](runtime.md#rt-rte-curation-feedback); advisory output does not itself change retained memory. |
| Pro new-content reconciliation | `gems/okf-pro/lib/okf/pro/reconcile.rb` | Direct implementation; [MEM-RTE-reconcile-search](#mem-rte-reconcile-search). Narrow vocabulary match, not semantic contradiction detection. |
| Pro board, journal, closure and extraction | `gems/okf-pro/lib/okf/pro/template/gem/.claude/skills/okf-pro/SKILL.md`, `gems/okf-pro/lib/okf/pro/template/gem/.claude/skills/okf-pro/guides/closing.md` | Direct doctrine; supplied [RT-RTE-pro-writes](runtime.md#rt-rte-pro-writes) covers deterministic writes. [MEM-OBJ-board](#mem-obj-board), [MEM-OBJ-journal](#mem-obj-journal); extraction remains agent-authored, not performed by close. |
| Pro snapshot, state, Stop and SessionStart | `gems/okf-pro/lib/okf/pro/snapshot.rb`, `gems/okf-pro/lib/okf/pro/state.rb`, `gems/okf-pro/lib/okf/pro/closing.rb` | Direct implementation; [MEM-RTE-snapshot-context](#mem-rte-snapshot-context). Supplied [RT-RTE-pro-gates](runtime.md#rt-rte-pro-gates) supplies host wiring. |
| Pro trust and attribution | `gems/okf-pro/lib/okf/pro/template/gem/.claude/skills/okf-pro/guides/frontmatter.md`, `gems/okf-pro/lib/okf/pro/template/gem/.claude/skills/okf-pro/guides/attribution.md` | Direct doctrine and Concept classifier; [MEM-OBJ-concept-metadata](#mem-obj-concept-metadata). Supplied gates constrain matched edit paths only, not universal provenance authentication. |
| Pro friction recorder and read-back | `gems/okf-pro/lib/okf/pro/friction.rb`, `gems/okf-pro/lib/okf/pro/closing.rb` | Direct implementation; [MEM-RTE-friction-feedback](#mem-rte-friction-feedback). Raw intent records plus transient count, not autonomous method revision. |
| Executable/reference alternatives | `skills/okf/templates/attested-computation.md`, `gems/okf/lib/okf/bundle/references.rb`, `gems/okf/lib/okf/concept.rb` | Direct template, inventory and accessor reads; [MEM-OBJ-references](#mem-obj-references). Inventory is not execution or payload inspection. External executor/attester contracts and arbitrary payload semantics remain uninspected. |
| Instruction installation / restructuring | `gems/okf-pro/lib/okf/pro/template/seed/CLAUDE.md`; runtime-cited scaffold/refine paths | Direct seeded routing instruction; supplied [RT-RTE-governance-install](runtime.md#rt-rte-governance-install), [RT-RTE-refine-proposal](runtime.md#rt-rte-refine-proposal), [RT-OBJ-skill](runtime.md#rt-obj-skill). Fixed shipped guidance is not acquired memory; adopter edits can persist but no automatic trace-to-instruction updater is established. |

Included repository knowledge bundles and tests are source-native authored examples and checks, not authenticated episodes. Their individual leaf claims and complete fixture coverage were not audited. This prevents a claim of semantic corpus correctness or exhaustive evaluator coverage, not tracing the shipped memory loop.

## Core ideas

1. **The durable unit is editable text, not a hidden model store.** Bodies carry claims; frontmatter carries provenance, lifecycle and retrieval keys. Reader constructs a process-local parsed view. Search scores and graph maps derive from that view; they do not replace the disk corpus. See [MEM-OBJ-concept-body](#mem-obj-concept-body), [MEM-OBJ-concept-metadata](#mem-obj-concept-metadata).
2. **Read less through maps and queries, not through conversation eviction.** Consume requests orientation, a branch map, recent changes and only relevant bodies. MCP adds projections and cuts; full concept and resource reads remain uncapped by those row controls. The system supplies selected content but does not own the host's window. See annotations on [RT-RTE-skill-work](runtime.md#rt-rte-skill-work) and [RT-RTE-mcp-retrieve](runtime.md#rt-rte-mcp-retrieve).
3. **Semantic maintenance is an agent duty with structural evidence.** A deprecated loser remains readable; unresolved disagreement becomes board work. Pro's reconciliation search prompts judgment without deciding truth. Structural conformance, human-review labels and semantic correctness are not equivalent. See [MEM-RTE-reconcile-search](#mem-rte-reconcile-search).
4. **Work-state feedback crosses sessions by explicit retained artifacts.** A person/agent appends a mechanically computed snapshot to the log; SessionStart selects it alongside fresh cheap state. Friction records are automatically appended and later summarized, but neither chain automatically writes a revised skill. See [MEM-RTE-snapshot-context](#mem-rte-snapshot-context), [MEM-RTE-friction-feedback](#mem-rte-friction-feedback).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-concept-body
Label: Concept body

Natural-language Markdown on disk is interpreted by later agents or humans. Inline computation fences are a distinct symbolic consumption path described in [MEM-OBJ-references](#mem-obj-references). A parsed body is also searched as text. This object is retained knowledge, distinct from the shipped procedural [RT-OBJ-skill](runtime.md#rt-obj-skill) and from the CLI component that parses it. No supplied operative-object counterpart after comparison.

Lineage can be distilled code/docs, human-only knowledge, project findings or verbatim adopted documents; a label such as Learning does not establish improvement. Acquisition and edits are authored by the agent/user; ordinary maintenance does not require per-content human approval. Persistence is file-based across sessions until edited/deleted; consumption uses task-directed reads. Reasons may be retained in prose and sources, but are not required to be complete. SRC-1, `skills/okf/playbooks/produce.md`, `skills/okf/playbooks/migrate.md`, `gems/okf/lib/okf/bundle/reader.rb`:

> Bodies are sacred: migrate never rewrites, reorders, or summarizes a body — the
> one permitted edit besides prepending frontmatter is repointing a relative link
> that a file move broke.
> --- `skills/okf/playbooks/migrate.md`

#### MEM-OBJ-concept-metadata
Label: Concept provenance and lifecycle fields

Symbolic YAML fields on disk include generated actor/time, verified events, source mappings/ids, status, tags and stale_after. Natural-language title/description/source titles remain interpreted text and search features; their content is not authenticated by parsing. This metadata is separate from [MEM-OBJ-concept-body](#mem-obj-concept-body) because filtering, classification and invalidation differ. Closest supplied [RT-RTE-skill-work](runtime.md#rt-rte-skill-work) is a route, not this object; no supplied object counterpart.

Lineage: author-supplied provenance and review events, plus compatibility accessors for old timestamp/Citations. Trust tier is derived in memory, not a durable subjective score. A human-prefixed verifier makes the parsed concept human-reviewed; that is classification of recorded events, not proof of an actual human read. SRC-1, `gems/okf/lib/okf/concept.rb`:

> return :human_reviewed if events.any? { |event| event["by"].to_s.strip.start_with?(HUMAN_ACTOR) }
> --- `gems/okf/lib/okf/concept.rb`

> def stale_on?(today)
>       date = stale_after_date
>       !date.nil? && today >= date
>     end
> --- `gems/okf/lib/okf/concept.rb`

Actual consumers include search/catalog filters, displays and Pro pairing/attestation checks. Status is stable by default; deprecation can be requested as a filter but does not erase evidence. Staleness is reported, not automatic removal. SRC-1, `gems/okf-pro/lib/okf/pro/template/gem/.claude/skills/okf-pro/guides/frontmatter.md`:

> `stale_after:` | Whoever files the concept | At creation, per the table below | The day this becomes stale — `today >= stale_after`, inclusive. Reports; never gates.
> --- `gems/okf-pro/lib/okf/pro/template/gem/.claude/skills/okf-pro/guides/frontmatter.md`

#### MEM-OBJ-index
Label: Authored directory index

Natural-language index.md bodies on disk guide traversal; the root also carries symbolic format-version metadata. Reader retains index text as reserved material rather than ordinary concepts. Directory listings/rollups can be computed, so a synthesized map is not evidence of authored index prose. Distinct from [RT-OBJ-skill](runtime.md#rt-obj-skill); no supplied object counterpart. SRC-1, `gems/okf/lib/okf/bundle/reader.rb`, `gems/okf-mcp/lib/okf/mcp/server.rb`, `skills/okf/playbooks/maintain.md`:

> **Update every enumeration that names what you changed — including `index.md`
>    bodies**, not just the concept files:
> --- `skills/okf/playbooks/maintain.md`

Agent maintenance supplies/edits index content; structural tools expose enumeration drift. Later agents consume branch maps through CLI/MCP or host-attached root resource. This is access guidance, not an answer oracle or enforced traversal policy.

#### MEM-OBJ-log
Label: Durable update log

Reserved log.md is raw Markdown text on disk, separate from concept parsing. Authored dated entries retain changes and significance, not an automatic transcript of tool calls. The Pro Snapshot line is a separately consumed part, [MEM-OBJ-snapshot](#mem-obj-snapshot). No supplied operative-object counterpart; [RT-RTE-pro-writes](runtime.md#rt-rte-pro-writes) changes this object but is not it. SRC-1, `skills/okf/playbooks/maintain.md`:

> Append a dated `log.md` entry — what changed and why it
>    matters, never the rounds it took
> --- `skills/okf/playbooks/maintain.md`

Later agents are asked to read recent history before use or maintenance; MCP returns selected date groups, potentially byte-truncated. Retained explanations can therefore fail to reach a consumer when omitted by selection. There is no demonstrated automatic generalization from these logs into new concepts.

#### MEM-OBJ-board
Label: Pro forward work state

board.md is Markdown stored on disk. Task prose is natural language; section/bullet/date/link grammar, cap and Resolve markers have symbolic consumers. Operational parts affect counters, promotion refusal, conflict and deadline reports. The prose affects later agent/human prioritization by interpretation. These paths share storage, not authority. No supplied object counterpart; [RT-RTE-pro-writes](runtime.md#rt-rte-pro-writes) is the closest writer route.

Inputs can be agent/human captures and explicit software transforms. Broad origin of initial adopter content is caller-dependent, while capture/promote/demote transformations are known. SRC-1, `gems/okf-pro/lib/okf/pro/template/gem/.claude/skills/okf-pro/SKILL.md`:

> An unresolved contradiction is work. It competes for attention like
> work, and only resolving it takes the line away.
> --- `gems/okf-pro/lib/okf/pro/template/gem/.claude/skills/okf-pro/SKILL.md`

Board removals do not imply deletion of supporting concepts. Cap applies to in-flight work, not to model context tokens. Malformed line grammar can make a line invisible to counts; [RT-RTE-pro-gates](runtime.md#rt-rte-pro-gates) and [MEM-RTE-snapshot-context](#mem-rte-snapshot-context) retain the checks and limits.

#### MEM-OBJ-journal
Label: Pro daily backward record

Journal entries are dated concept files with natural-language records of work, not automatically captured raw conversations. Agent/user authors content; journal-open creates the mechanical scaffold and index pairing. Past-day edits have separate approval/refusal policy in [RT-RTE-pro-gates](runtime.md#rt-rte-pro-gates). No supplied object counterpart; closest [RT-RTE-pro-writes](runtime.md#rt-rte-pro-writes) is not a content object.

SRC-1, `gems/okf-pro/lib/okf/pro/template/gem/.claude/skills/okf-pro/SKILL.md`:

> reconstruct the entry from `log.md` and git history, and say in the
> entry that it was reconstructed
> --- `gems/okf-pro/lib/okf/pro/template/gem/.claude/skills/okf-pro/SKILL.md`

This is an alternative authored checkpoint from two retained inputs, not automated compaction. Later search can retrieve entry bodies; project links also feed dormancy questions through the supplied Pro context route. Durable lessons are requested to be extracted into learnings/glossary on closure, rather than assuming the whole daily narrative becomes an effective lesson.

#### MEM-OBJ-snapshot
Label: Pro mechanical Snapshot line

A symbolic, regex-readable counter line within log.md, stored on disk only when the caller appends it. It derives from board/work/corpus state, not hidden reasoning. The returned computed line is transient until written. Distinct part of [MEM-OBJ-log](#mem-obj-log), with separate verification and SessionStart consumer; no supplied object counterpart. SRC-1, `gems/okf-pro/lib/okf/pro/snapshot.rb`, `gems/okf-pro/lib/okf/pro/state.rb`:

> def line(root, today: Date.today, board: nil, concepts: nil)
>         render(counters(root, today: today, board: board, concepts: concepts))
>       end
> --- `gems/okf-pro/lib/okf/pro/snapshot.rb`

> { "day" => day, "line" => line.strip, "counters" => Snapshot.parse(line) }
> --- `gems/okf-pro/lib/okf/pro/state.rb`

Later consumers receive the latest dated line, not the full history or the reasons behind each count. Journal judgment is separate. A checked counter is no guarantee that task prose or underlying claims are true.

#### MEM-OBJ-friction
Label: Pro friction intent log

JSON-lines symbolic events in repository-root .tmp/okf-pro-friction.log, outside the knowledge bundle; an unavailable marker records incomplete collection. Fields include date, via, what and optional detail. These are raw operational intent records, not a learned rule or necessarily completed actions. No supplied object counterpart; related gate route [RT-RTE-pro-gates](runtime.md#rt-rte-pro-gates) does not declare this telemetry.

SRC-1, `gems/okf-pro/lib/okf/pro/friction.rb`:

> entry = { "at" => today.to_s, "via" => via, "what" => what }
>         entry["detail"] = detail if detail
>         File.open(path, "a") { |file| file.puts JSON.generate(entry) }
> --- `gems/okf-pro/lib/okf/pro/friction.rb`

Append is automatic at instrumented hook paths; no per-event human admission. Later report/banner uses parsed events and unreadable/unavailable indicators. Explicit clear deletes log and marker; no automatic pruning established in the inspected recorder.

#### MEM-OBJ-references
Label: Reference payloads and attested computation contracts

Filesystem payloads under references/ can be code, run instructions, mirrors or Markdown concepts. Path inventory is symbolic access metadata, not the payload bytes or a readable summary of their full semantics. Computation may alternatively be inline in a concept or in a file elsewhere in the bundle. Symbolic code has an executor consumer distinct from natural-language run instructions interpreted by an agent. Payload encoding/provenance is per file; no universal numerical or textual form is inferred. No supplied object counterpart; related [RT-RTE-mcp-retrieve](runtime.md#rt-rte-mcp-retrieve) only inventories it.

SRC-1, `skills/okf/templates/attested-computation.md`:

> an agent MAY bind values for the declared
>      `parameters` and MUST NOT author or edit the computation itself.
> --- `skills/okf/templates/attested-computation.md`

The template requests human-sanctioned code, named parameters, executor resource/receipt fields and deterministic attester resource. This establishes a documented external consumer contract, not an implemented execution service or proof of attestation. The inventory connects path-valued fields to files and reports dangling pointers; it does not execute, validate meaning, or serve arbitrary non-Markdown payload contents through read_concept. SRC-1, `gems/okf/lib/okf/bundle/references.rb`:

> Scope is the folder, by design. §6.3 is "a naming convention, not a
>     # requirement", and a computation stored beside its concept is legal —
>     # and deliberately not this inventory's to list.
> --- `gems/okf/lib/okf/bundle/references.rb`

### Routes

#### MEM-RTE-reconcile-search
Label: Pro admission-time vocabulary feedback

Part of: [RT-RTE-pro-gates](runtime.md#rt-rte-pro-gates)

This specializes the parent gate route's reconciliation checker, not a duplicate of all its guard/Stop operations. A Write event and Target select a bundle; code takes up to four non-stopword basename terms, searches each, drops self/structural hits and retains five hits per term. It supplies ids, types, titles, snippets and deprecated annotations. The external agent must then read/decide whether to correct, deprecate or file a conflict. Code detects vocabulary overlap, not contradictory propositions. No semantic answer oracle; open project work. Agent proposes/decides semantic changes; ordinary unverified edits require no human approval, while attestation has its separate ask path.

- Immediate return: Reconciliation finding requesting inspection of matched concepts, or no findings.
- Later read-back: Existing concepts reach the editing agent as snippets and ids; requested subsequent body reads and corrected/deprecated concepts can shape later sessions.
- Delegated visibility: uninspected — host context propagation is not specified.
- Selection predicate: Write only; excludes journal and structural basenames; first four filename terms and first five search hits per term, excluding self.
- Invalidation or expiry: Recomputed on eligible event; status changes affect later annotation, not automatic removal.
- Activation or effect: Vocabulary feedback is wired; semantic correction is requested, not observed.
- Evidence limits: Filename vocabulary can miss a contradiction; Edit events do not take this checker branch. No automatic semantic admission decision or truthful-result guarantee.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1, `gems/okf-pro/lib/okf/pro/reconcile.rb`:

> return [] unless event.tool_name == "Write"
>         return [] if target.rel.start_with?("journal/")
> --- `gems/okf-pro/lib/okf/pro/reconcile.rb`

> status == "deprecated" ? "  [deprecated — this collision was already settled]" : ""
> --- `gems/okf-pro/lib/okf/pro/reconcile.rb`

Admission/rejection/recovery: emitted feedback can require follow-up under the parent's host protocol; it does not roll back prose or itself select the winner. Skill policy says correct loser title/description, set deprecated, retain superseded reasoning in details, or file a linked Resolve line. The retained rationale is available in full-body reads but is not included as such in this snippet projection. Correction guidance is the installed Pro skill; result is edited knowledge/work state, not model parameters.

#### MEM-RTE-snapshot-context
Label: Snapshot retention and next-session supply

Part of: [RT-RTE-pro-gates](runtime.md#rt-rte-pro-gates)

Distinct subchain of the supplied gate route: caller requests Snapshot derivation; agent/user appends it to log; dirty-session Stop recomputes/compares; SessionStart reads latest dated snapshot plus cheap live board/log/project state. Host owns hook execution and model-window inclusion. This is operational summary read-back, not conversation compression. The agent/person controls writing each line; software can veto disagreement at Stop, but snapshot command never writes automatically. No expected semantic answer; deterministic counters are a state-consistency reference. Open daily operation, not a training curriculum.

- Immediate return: Computed line, Stop findings, or SessionStart banner depending on entry point.
- Later read-back: Latest retained dated Snapshot line is included whole in a later SessionStart banner and in state output; fresh board counts are computed separately.
- Delegated visibility: uninspected — host decides recipients; no worker isolation or propagation protocol is supplied.
- Selection predicate: Bundle ancestor of cwd; dirty Markdown precondition at Stop; latest snapshot by date, cheap live board/log and directory state at SessionStart. Corpus-heavy counts remain from the labeled snapshot unless full state requested.
- Invalidation or expiry: Banner is explicitly current only at session start; refresh with pro state after writes. Old Snapshot is labeled not live, not silently recomputed into a fresh historical line.
- Activation or effect: Software computes/verifies counters and emits context. Agent comparison of deltas is requested, not observed.
- Evidence limits: Correct counts depend on parseable grammar and visible corpus. This does not verify historical semantic accuracy or demonstrate improved prioritization.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1, `gems/okf-pro/lib/okf/pro/closing.rb`:

> msgs.concat(Snapshot.verify(root, snap, today: today, board: board, concepts: concepts))
> --- `gems/okf-pro/lib/okf/pro/closing.rb`

> "Last snapshot (#{snap["day"]}, not live): #{snap["line"]}"
> --- `gems/okf-pro/lib/okf/pro/closing.rb`

Rejection requires correcting state or appending the correct line and retrying; no automatic rollback of prior content. Guidance asks the agent to read deltas and journal judgment separately. The snapshot preserves counters, not causal explanations. This is a trace/state-derived retained result with a later consumer, but its physical write is caller-mediated, not an automatic trace-fed concept updater.

#### MEM-RTE-friction-feedback
Label: Automatic intent recording to later banner

Instrumented pre-shell and post-edit paths call Friction.record; JSON-lines accumulate; report parses them; SessionStart computes a covered-event count and emits a request to tell the maintainer. This is distinct telemetry-to-context routing, not a duplicate of [RT-RTE-pro-gates](runtime.md#rt-rte-pro-gates): the recorder never blocks. Recorded shell intent is not proof that a denied action occurred. Code owns append/parse/count; user/agent chooses whether to request a new verb, clear or send a report. No automated successor policy selection or semantic answer oracle.

- Immediate return: Boolean recorder success/failure; report data or banner prose on subsequent reads.
- Later read-back: SessionStart counts retained events covered by a Pro verb and requests operator feedback; CLI friction exposes the fuller record. No automatic revised method artifact follows.
- Delegated visibility: uninspected — later host/maintainer sharing is caller-controlled.
- Selection predicate: Instrumented hand-edit/recognized shell paths; banner counts only verb-covered events, excluding shell redirects whose alternative is Edit/Write. Unreadable/unavailable states are reported separately.
- Invalidation or expiry: Append-only lifetime record until explicit clear removes log and unavailable marker; no per-session reset.
- Activation or effect: Recording and transient summary supply are wired, not observed to induce a new verb or improved agent behavior.
- Evidence limits: Intent/outcome differ; heuristic recognition and parse/write failures limit coverage. Raw telemetry plus count is not a durable learned policy.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1, `gems/okf-pro/lib/okf/pro/closing.rb`:

> covered = report.events.count { |e| Friction.verb_covered?(e["via"], e["what"]) }
> --- `gems/okf-pro/lib/okf/pro/closing.rb`

SRC-1, `gems/okf-pro/lib/okf/pro/friction.rb`:

> [ log_path(root), marker_path(root) ].count do |path|
>           next false unless File.exist?(path)
>
>           File.unlink(path)
> --- `gems/okf-pro/lib/okf/pro/friction.rb`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-retained-knowledge
Label: Selected knowledge to later task judgment

Consumer: later external agent or human. Channel: selected Markdown body/index/log, CLI/MCP projections, resource attachment or human browser/TUI reads. Force: interpreted evidence and guidance, not automatic truth or compliance. Horizon: later task invocations across sessions, until content/selection changes. Distinct from [RT-BAP-skill-guidance](runtime.md#rt-bap-skill-guidance): that path is shipped procedural text; this one is acquired/revised corpus content. SRC-1, `skills/okf/playbooks/consume.md`:

> Then follow links only into the concepts the
>    task needs.
> --- `skills/okf/playbooks/consume.md`

#### MEM-BAP-state-context
Label: Retained work state to opening priorities

Consumer: external agent/human at SessionStart. Channel: computed board/state text, retained last snapshot and selected friction count. Force: interpreted prioritization cues; board grammar separately constrains software writers/counters. Horizon: current session after prior-session retention, refreshed explicitly after writes. Distinct from [RT-BAP-hook-protocol](runtime.md#rt-bap-hook-protocol), which concerns admission machinery rather than data supplied for work judgment. SRC-1, `gems/okf-pro/lib/okf/pro/closing.rb`:

> "Read the delta, not the status: a number that moved the wrong way is today's first signal."
> --- `gems/okf-pro/lib/okf/pro/closing.rb`

## Annotations

#### On [RT-RTE-skill-work](runtime.md#rt-rte-skill-work)

Memory inputs include [MEM-OBJ-concept-body](#mem-obj-concept-body), [MEM-OBJ-concept-metadata](#mem-obj-concept-metadata), [MEM-OBJ-index](#mem-obj-index) and [MEM-OBJ-log](#mem-obj-log). Produce requests distillation from code, docs/wiki or manual knowledge; migrate instead preserves body bytes and adds metadata. These are different transformations, not uniform summarization. Maintain updates bodies/provenance, links/enumerations/log and requests validation/lint/loose/tag judgment. Retirement retains explanatory context rather than silently deleting it. SRC-1, `skills/okf/playbooks/maintain.md`:

> mark retired assets with a `**Deprecation**` note rather than
>    silently deleting the context that explains them.
> --- `skills/okf/playbooks/maintain.md`

Write agency is external agent/user; ordinary content admission is not necessarily human-controlled. Tools report structure; general-purpose edits bypass Writer's pre-publication validation. Physical file writing is not evidence of semantic approval. Index-first retrieval is task-directed pull: agent selects branch, CLI returns map/ids, agent follows relevant bodies. It has no fixed token budget in the inspected consume procedure. Search matches current symbolic criteria, not a learned preference model. Source titles/resource strings are searchable in addition to bodies (SRC-1, `gems/okf/lib/okf/bundle/search.rb`); a source match is not inspection of the source itself.

#### On [RT-RTE-mcp-retrieve](runtime.md#rt-rte-mcp-retrieve)

Read-back can be model-requested tool retrieval or host-requested resource attachment. A host attachment does not establish an OKF autonomous selector. Search applies terms/filters then row limits and projection; read_concept returns original full Markdown via exact id mapping, not reserialization. Catalog projects metadata; index supplies authored/synthesized branch maps; graph excludes bodies; references returns path inventory. These channels do not all deliver retained reasons. SRC-1, `gems/okf-mcp/lib/okf/mcp/server.rb`:

> text = begin
>               context.folder(bundle).concept_source(id)
> --- `gems/okf-mcp/lib/okf/mcp/server.rb`

Index defaults depth 1 with bodies/listing configurable. Log defaults date-group selection with a per-file content budget; the runtime's checked truncation/fallback findings bound freshness and completeness. Full-body/resource reads are not bounded by search row projection. Cached corpus eviction is Ruby residency management, not removal of already delivered conversation tokens. Reload is a fresh read/query; paths/URIs are not model-window references with automatic dereferencing. Optional backend payload/provenance remain uninspected, not absent.

#### On [RT-RTE-pro-writes](runtime.md#rt-rte-pro-writes)

Known transformations preserve declared deltas of board/log/project/journal text; they do not infer a lesson from narrative. Initial caller-supplied prose/control may be human or agent. Mechanical close changes closure marker, board and log; it does not discharge the semantic extraction request. SRC-1, `gems/okf-pro/lib/okf/pro/template/gem/.claude/skills/okf-pro/guides/closing.md`:

> First, extract the durable part to `learnings/` or `glossary/`
> --- `gems/okf-pro/lib/okf/pro/template/gem/.claude/skills/okf-pro/guides/closing.md`

The guide keeps the project directory in place because later shared-layer citations point into it. Closure is metadata and work-list removal, not archive relocation or knowledge deletion. Journal-open supplies scaffold/index; caller writes judgment. Conservation and per-file atomicity protect mechanical changes, not semantic truth, lesson quality or group transactionality.

#### On [RT-RTE-refine-proposal](runtime.md#rt-rte-refine-proposal)

Requested retained outputs include changed layout, pointers and declines. They can shape later navigation, but supplied evidence does not establish that later diagnosis reads a retained decline or that it improves retrieval. Instruction restructuring changes installed guidance rather than embedding weights; shipped static text is not itself use-acquired memory. Parameter mutability remains outside SRC-1 as already bounded by [RT-CMP-agent](runtime.md#rt-cmp-agent). No extra theory-builder, reflection or self-improvement conclusion is inferred from text persistence.

## Write side

Acquisition has two source-native branches: produce distills into new concepts, while migrate adopts existing bodies verbatim. The input can be code/documentation, external claims or agent/human findings; origins are heterogeneous and are supposed to be recorded, not guessed. Ordinary maintain is agent-authored semantic updating plus structural checks. Writer publication is a separate software gate over a caller's proposed bundle; it cannot be generalized to direct edits. See [RT-RTE-publish-bundle](runtime.md#rt-rte-publish-bundle) and the skill-work annotation.

Pro adds targeted admission: owner decision for verification, vocabulary feedback on eligible Write, board cap and shape checks, past-journal protection, Stop/commit/CI checks. These mechanisms neither authenticate all provenance nor mechanically settle disagreements. [MEM-RTE-reconcile-search](#mem-rte-reconcile-search) preserves both the retained loser and unresolved-work branch. Status deprecated and age expiry are not automatic deletion. Search filters and projections can change visibility independently of physical retention.

Trace/state transformations differ. [MEM-RTE-snapshot-context](#mem-rte-snapshot-context) is raw board/corpus state → computed counter line → caller append → Stop comparison → later banner. [MEM-RTE-friction-feedback](#mem-rte-friction-feedback) is instrumented event intent → automatic raw JSON-line append → later count/report. The latter automatically writes durable traces, not durable behavior-shaping generalizations. A journal can be reconstructed from log/Git history with an explicit disclosure; closure requests extraction of durable findings. Neither is an automatic conversation compactor, and a file named Learning is not proof of learned capacity.

Retention of reasons is selective: concept prose, sources, deprecation details, log significance and journal judgment can retain them. Counter snapshots and friction summaries omit most reasons. Full-body reads can recover recorded prose; snippets, graphs, listings and counters do not guarantee that it arrives. Explicit clear withdraws friction telemetry; registry removal withdraws discovery without deleting bundle files; overwrite publication replaces a tree. No universal semantic expiry, automatic source-refresh or universal rollback is established by those operations.

## Read-back

The ordinary later consumer is the agent doing a new task. It chooses maps, branch, terms and bodies; the software selects matches and returns requested views. MCP is a concrete shipped retrieval consumer interface, not just an unused storage API. Resource attachment affords host-supplied context without a model fetch decision. Browser/TUI provide human consumption and registry selection, not proof of model memory activation. Relevant records are [RT-RTE-skill-work](runtime.md#rt-rte-skill-work), [RT-RTE-mcp-retrieve](runtime.md#rt-rte-mcp-retrieve), [RT-RTE-registry-manage](runtime.md#rt-rte-registry-manage).

The automatic push is Pro SessionStart: cwd selects bundle; software reads cheap live state and the latest retained snapshot, adds dormancy and selected friction cues, and emits banner text under the installed host protocol. The snapshot is labeled historical. There is no overall banner token ceiling established here; cheap inputs constrain computation rather than constitute a strict payload bound. Refresh routes are pro state, full state when corpus-derived counters are needed, board listing and ordinary content reads. See [MEM-RTE-snapshot-context](#mem-rte-snapshot-context), [MEM-RTE-friction-feedback](#mem-rte-friction-feedback).

Working-context controls are selective supply: branch maps, short search snippets, requested metadata projections, graph without bodies, bounded logs, filtered hook feedback and computed state in place of multiple full files. They keep irrelevant bytes out before entry. None of these inspected paths removes old host turns or isolates a child reasoning frame. The stack-frame analogy therefore has no evidenced OKF-owned push/pop: a later resource read returns new bytes, not a live heap reference. External host compaction/delegation remains uninspected. No closed-window or activation claim follows.

Attested computation is a different offered consumer contract: agent binds declared parameters, external executor runs sanctioned code, deterministic attester checks receipt. The inspected implementation models and inventories the contract; it does not establish actual executor/attester invocation or certify arbitrary mirrored payloads. Inventory metadata is not delivery of executable bytes. See [MEM-OBJ-references](#mem-obj-references).

## Integration issues

- No supplied fact is corrected. The runtime's freshness, bypass, per-file atomicity and host-boundary qualifications remain load-bearing.
- New objects have no supplied object counterpart after comparison. [MEM-RTE-reconcile-search](#mem-rte-reconcile-search) and [MEM-RTE-snapshot-context](#mem-rte-snapshot-context) explicitly specialize parts of [RT-RTE-pro-gates](runtime.md#rt-rte-pro-gates), rather than replacing it. [MEM-RTE-friction-feedback](#mem-rte-friction-feedback) is additional telemetry routing; the opening banner overlaps the parent's context endpoint, not its complete identity. No duplicate proposed for supersession.
- Backend internals remain unresolved: [RT-RTE-mcp-retrieve](runtime.md#rt-rte-mcp-retrieve) exposes an optional backend seam but SRC-1 does not include that package. Prevents conclusions about its persistent index, embeddings, admission and invalidation; fallback findings must not be generalized to it.
- Actual human approval, host attachment/window retention, semantic write-back, extracted lessons and later behavior remain unobserved for [RT-RTE-skill-work](runtime.md#rt-rte-skill-work), [MEM-RTE-reconcile-search](#mem-rte-reconcile-search), [MEM-BAP-retained-knowledge](#mem-bap-retained-knowledge) and [MEM-BAP-state-context](#mem-bap-state-context). Source wiring/request is supportable; activation and benefit are not.
- Non-Markdown reference payloads and consumer-side executor/attester behavior remain per-payload uninspected under [MEM-OBJ-references](#mem-obj-references). Symbolic contract fields and inventory do not establish payload meaning or successful execution.
- Migration, source attribution, counters and status make heterogeneous lineage visible, but cannot establish its truth. An unknown initial caller does not erase known subsequent mechanical transformations in [RT-RTE-pro-writes](runtime.md#rt-rte-pro-writes) or [MEM-RTE-snapshot-context](#mem-rte-snapshot-context).

## Limitations and checks

The registered checkout HEAD was rechecked as cfb7ffac7fef37d56e97b5b7dd8fe97ffc648c7c and git status was clean. Direct source reads used that checkout; no target, tests, examples or services were executed. The supplied invocation, member types, worker rules and complete records contract were read; truncated delivery was recovered in smaller reads before findings were settled. The method boundary is this invocation and its supplied contracts; no prior target analysis or comparison was used.

Countercases checked against strong interpretations include direct edits bypassing Writer, Edit bypassing the reconciliation Write branch, deprecated hits remaining visible, stale dates reporting rather than deleting, caller-appended rather than automatically written snapshots, shell intent versus completed action, and reference inventory versus payload execution. These bound rather than negate the supported routes. Source code and doctrine do not establish semantic correctness, future capacity improvement, model compliance or successful self-improvement.

Validation: the required role-specific commonplace-validate command passed with exit status 0: “Member content check passes; invocation residue not checked. This is not job acceptance or claim support.” No check-driven claim narrowing or withdrawal was needed. Validation checks form, references and quotation occurrence, not semantic support or acceptance.
