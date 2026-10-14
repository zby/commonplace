---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "LLM Wiki's agent-maintained Markdown memory, structural access metadata, selective reload and delegated revision at the frozen commit."
run-id: AAS-2026-10-14-llm-wiki-b437987c5802-01
source-identity: https://github.com/cobusgreyling/llm-wiki
reviewed-boundary: a424e6875aa2d5736d9c0d03d7c28bdbe32892a5
---

# llm-wiki memory report

## Boundary and evidence

The memory boundary includes raw documents, compiled wiki pages, filed answers, the catalog, contradiction ledger, operation log, templates and maintainer instructions. It includes every CLI/MCP retrieval and inspection surface, scaffold writers, the watcher and the instruction-sync caller. Toolkit transformations are implementation evidence; semantic authoring and human admission are doctrine/design. Sampled demo pages supply reported operation, not authenticated execution. All evidence is SRC-1 at the revision above, as registered in `boundary.md`.

Direct reads covered `src/llm_wiki/cli.py`, `src/llm_wiki/mcp_server.py`, `src/llm_wiki/search.py`, `src/llm_wiki/expand.py`, `src/llm_wiki/links.py`, `src/llm_wiki/ingest.py`, `src/llm_wiki/lint.py`, `src/llm_wiki/stats.py`, `src/llm_wiki/watch.py`, `src/llm_wiki/new_page.py`, `src/llm_wiki/bootstrap.py`, `src/llm_wiki/paths.py`, `src/llm_wiki/scaffold/AGENTS.md`, all four scaffold templates and all four scaffold wiki seed pages. Added direct coverage includes `src/llm_wiki/scaffold/raw/README.md`, `scripts/sync_agents.py`, `scripts/ingest-checklist.sh`, `scripts/demo-walkthrough-fast.sh`, `Makefile`, the qmd setup passage in `README.md`, and demo synthesis, contradictions and log. A bounded search across `src/`, those operating documents and shipped scripts checked deletion, rejection, compaction, hooks, embeddings, history and budgets. The supplied runtime remains provisional; quotations in its cited records are used without duplicating them.

External host context, model weights, approvals, compaction and tool-result injection are excluded implementations. qmd's collection, numerical representations and refresh behavior are external and opaque; only the adapter and setup instructions are inspected. These exclusions prevent host-level isolation, prompt compliance, embedding provenance and retrieval-freshness conclusions. Remaining example corpora, target tests and external editor implementations were not inspected for content quality. No target code, tests, examples or services were executed.

| Entry point or memory operation | SRC-1 source path | Coverage and limit |
|---|---|---|
| Raw acquisition and agent ingest | `src/llm_wiki/scaffold/raw/README.md`, `src/llm_wiki/scaffold/AGENTS.md` | Direct; [MEM-OBJ-raw](#mem-obj-raw), [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) and annotation. Human source choice is not per-edit approval. |
| Source, entity/concept, synthesis, contradiction authoring | `src/llm_wiki/scaffold/templates/source.md`, `src/llm_wiki/scaffold/templates/entity.md`, `src/llm_wiki/scaffold/templates/concept.md`, `src/llm_wiki/scaffold/wiki/synthesis.md`, `src/llm_wiki/scaffold/wiki/contradictions.md` | Direct; separate operative objects below. Model execution and actual revision history unobserved. |
| Query and answer filing | `src/llm_wiki/scaffold/AGENTS.md`, `src/llm_wiki/scaffold/templates/answer.md` | Direct; [MEM-OBJ-answers](#mem-obj-answers), [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query) and annotation. No enforced acceptance handshake. |
| Built-in search and page/section expansion | `src/llm_wiki/search.py`, `src/llm_wiki/expand.py`, `src/llm_wiki/links.py` | Direct; query annotation. Metadata and text both enter lexical corpus; no relevance/trust gate. |
| qmd alternative | `src/llm_wiki/search.py`, `README.md` | Direct adapter/setup; [RT-RTE-qmd-search](runtime.md#rt-rte-qmd-search) and annotation. External index/update/embedding facts prevent a full lineage account. |
| Catalog, list, backlinks, graph, stats | `src/llm_wiki/scaffold/wiki/index.md`, `src/llm_wiki/links.py`, `src/llm_wiki/stats.py` | Direct; [MEM-OBJ-index](#mem-obj-index), [MEM-OBJ-page-metadata](#mem-obj-page-metadata), [MEM-RTE-metadata-read](#mem-rte-metadata-read). Graph returns pointers, not evidence text. |
| Recent log and broader corpus log reload | `src/llm_wiki/stats.py`, `src/llm_wiki/search.py` | Direct; [MEM-OBJ-log](#mem-obj-log), [MEM-RTE-log-read](#mem-rte-log-read), [MEM-CLM-log-parser](#mem-clm-log-parser). Parsed route omits hyphenated operations. |
| Status, watcher and checklist | `src/llm_wiki/ingest.py`, `src/llm_wiki/watch.py`, `scripts/ingest-checklist.sh` | Direct; [RT-RTE-pending-watch](runtime.md#rt-rte-pending-watch) annotation. Status is association metadata, not semantic completion. |
| Lint and delegated cleanup | `src/llm_wiki/lint.py`, `src/llm_wiki/scaffold/AGENTS.md` | Direct; [RT-RTE-wiki-lint](runtime.md#rt-rte-wiki-lint) annotation, [MEM-ABS-withdrawal-gate](#mem-abs-withdrawal-gate). Stale language does not suppress reload. |
| Project/page scaffolding, including force | `src/llm_wiki/bootstrap.py`, `src/llm_wiki/new_page.py` | Direct plus supplied [RT-RTE-project-init](runtime.md#rt-rte-project-init), [RT-RTE-page-create](runtime.md#rt-rte-page-create). Template writes bypass semantic integration. |
| Instruction evolution/sync and host startup | `scripts/sync_agents.py`, `src/llm_wiki/scaffold/AGENTS.md` | Direct sync/instructions plus supplied [RT-RTE-instruction-sync](runtime.md#rt-rte-instruction-sync), [RT-BAP-maintainer-instructions](runtime.md#rt-bap-maintainer-instructions). Host handoff/config conclusions use supplied runtime, not a new host inspection. |
| CLI/MCP dispatch and shipped demo consumers | `src/llm_wiki/cli.py`, `src/llm_wiki/mcp_server.py`, `scripts/demo-walkthrough-fast.sh`, `Makefile` | Direct dispatch/callers; no additional semantic writer or automatic model-driven callback found in these inspected surfaces. Driver execution unobserved. |

## Core ideas

LLM Wiki retains agent-authored interpretations as editable Markdown rather than deriving every answer directly from raw documents. Source summaries, topic pages, synthesis, conflicts and filed answers have different roles and lineage; they are not interchangeable copies of the raw material. The instruction assigns human source curation and agent bookkeeping, not human approval of every retained claim. [MEM-OBJ-raw](#mem-obj-raw), [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest).

Read-back is pull-based in the inspected consumer routes. An agent first reads a manually maintained catalog, asks for ranked snippets, then selects a page or heading. Section extraction controls a tool response, not the accumulated host window. Whole pages remain reachable; no token-budget allocator or session-compaction implementation is established. The optional qmd route changes the selector and freshness dependency, not wiki ownership. [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query), [RT-RTE-qmd-search](runtime.md#rt-rte-qmd-search).

Structure is checked more strongly than meaning. Source references and raw-file associations support navigation and coverage; they do not establish warrant or ingest completeness. Search admits every enumerated Markdown page, including operation logs and drafts. A contradiction entry can preserve conflicting evidence while both claims remain retrievable. [MEM-OBJ-page-metadata](#mem-obj-page-metadata), [MEM-OBJ-contradictions](#mem-obj-contradictions), [MEM-ABS-withdrawal-gate](#mem-abs-withdrawal-gate).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-raw
Label: Raw source documents

Source-native identity: project `raw/`. Storage substrate: filesystem originals, including text, PDFs, images and data. Representational form: document prose and images require interpretation; individual data-file encodings are unspecified. Lineage: human-curated acquisition; the repository does not implement acquisition conversion or authenticate originals. Consumers: instructed maintainer reads complete sources, while status/lint consume filenames. Content is evidence input, not an implemented permission or trusted-instruction channel. Authorship is external; human chooses what enters, and immutable treatment is protocol only. SRC-1: `src/llm_wiki/scaffold/raw/README.md`, `src/llm_wiki/scaffold/AGENTS.md`. Closest supplied record [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) is a transformation route, not this retained input.

> Keep originals intact — all synthesis happens in `wiki/`
> --- `src/llm_wiki/scaffold/raw/README.md`

#### MEM-OBJ-sources
Label: Source summary pages

Source-native identity: `wiki/sources/`, seeded by `templates/source.md`. Storage: Markdown files. Form: natural-language summary, takeaways, quotes and entity/concept references, with separately assessed symbolic `raw_file` association in [MEM-OBJ-page-metadata](#mem-obj-page-metadata). Lineage: interpreted extraction from a raw document by the external agent; template rendering alone creates only placeholders. Consumers: subsequent ingest and query agents, search/expand, and structural inspectors. Authority: defeasible source interpretation and pointers, not authenticated original content. The template can retain verbatim quotes but does not require complete evidential reasons for every takeaway. No supplied operative-object counterpart; produced on [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest). SRC-1: `src/llm_wiki/scaffold/templates/source.md`, `src/llm_wiki/scaffold/AGENTS.md`.

> ## Summary
>
> _3–5 sentence overview of the source._
> --- `src/llm_wiki/scaffold/templates/source.md`

#### MEM-OBJ-topics
Label: Entity and concept pages

Source-native identity: `wiki/entities/` and `wiki/concepts/`. Storage: Markdown files. Form: natural-language summaries, definitions, facts and relationships; links/frontmatter have symbolic navigation/inspection consumers. Lineage: incremental agent integration across sources, prescribed on every relevant ingest. Entity and concept pages share write admission and query consumers, so they are grouped here while their template-specific content remains distinct. Entity notes allow incremental observations; concepts explicitly allow an evolution account. Consumers: later maintainers and answering agents through index/search/expand. Authority is retained interpretation, not a software decision rule. Reasons can be retained in notes/evolution, but no consumer is required to read those sections. No supplied object counterpart; produced on [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest). SRC-1: `src/llm_wiki/scaffold/templates/entity.md`, `src/llm_wiki/scaffold/templates/concept.md`, `src/llm_wiki/scaffold/AGENTS.md`.

> ## Evolution
>
> _How understanding of this concept has changed over time._
> --- `src/llm_wiki/scaffold/templates/concept.md`

#### MEM-OBJ-synthesis
Label: Evolving synthesis

Source-native identity: `wiki/synthesis.md`. Storage: Markdown file. Form: natural-language evolving thesis and open questions; symbolic dates/counts are metadata, not a semantic verifier. Lineage: static seed initially, then agent revisions conditional on sources shifting the picture. Consumers: later maintainers and query agents; the demo driver explicitly expands synthesis. Authority: an interpretable cross-source account, not enforced truth. The demo retains a named revised insight and links, but does not authenticate the update process or demonstrate future behavior. Distinct from the production route [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest); no supplied object counterpart. SRC-1: `src/llm_wiki/scaffold/wiki/synthesis.md`, `examples/demo/wiki/synthesis.md`, `scripts/demo-walkthrough-fast.sh`.

> The evolving thesis of this knowledge base. Updated whenever new sources shift the picture.
> --- `src/llm_wiki/scaffold/wiki/synthesis.md`

#### MEM-OBJ-contradictions
Label: Contradiction ledger

Source-native identity: `wiki/contradictions.md`. Storage: Markdown table and resolution notes. Form: natural-language opposed claims, source/page links and status explanations; lint only checks lexical references. Lineage: agent conflict flagging during ingest and review during lint. Consumers: explicitly requested maintainer lint review, ordinary search/expand, and lexical ledger checks. Authority: candidate criticism and maintained explanations, not automatic claim invalidation. Resolved contradictions are prescribed to move into explanation-bearing notes rather than disappear. A later lint review can read those notes, but no per-resolution read or changed reliance is observed. The demo's open row is a reported example, not a proven content-directed revision cycle. No supplied object counterpart; overlaps the state outputs of [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) and [RT-RTE-wiki-lint](runtime.md#rt-rte-wiki-lint), not their identity. SRC-1: `src/llm_wiki/scaffold/wiki/contradictions.md`, `examples/demo/wiki/contradictions.md`, `src/llm_wiki/lint.py`.

> _Contradictions resolved by newer evidence are moved here with an explanation._
> --- `src/llm_wiki/scaffold/wiki/contradictions.md`

#### MEM-OBJ-answers
Label: Filed answer pages

Source-native identity: `wiki/answers/`, seeded from `templates/answer.md`. Storage: Markdown files. Form: natural-language question, synthesized response, consulted-source links and follow-ups. Lineage: a human question plus agent-selected wiki evidence and model interpretation; not a raw tool trace. Consumers: future queries and maintenance through the same corpus enumerator as other pages. Authority: retained prior analysis, not an answer oracle. The requested filing offer leaves acceptance details unresolved; filing is not automatically performed by search/expand. Template metadata lacks `updated`, although lint requires it: a new placeholder is not a ready or vetted answer. No supplied object counterpart; output of [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query) and possible scaffold output of [RT-RTE-page-create](runtime.md#rt-rte-page-create). SRC-1: `src/llm_wiki/scaffold/templates/answer.md`, `src/llm_wiki/scaffold/AGENTS.md`, `src/llm_wiki/lint.py`.

> ## Answer
>
> _Synthesized response with inline links to wiki pages._
> --- `src/llm_wiki/scaffold/templates/answer.md`

#### MEM-OBJ-index
Label: Wiki content catalog

Source-native identity: `wiki/index.md`. Storage: Markdown. Form: natural-language summaries and interpreted links for agents; lexical string membership for lint. Lineage: agent maintenance after ingest/new pages; neither page creation nor answer filing software repairs it automatically. Consumers: prescribed first query read, search and index-gap checking. Authority: discovery guidance, not access control. A missing catalog entry need not keep a page out of search/list. No supplied object counterpart; selection input to [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query). SRC-1: `src/llm_wiki/scaffold/wiki/index.md`, `src/llm_wiki/lint.py`, `src/llm_wiki/search.py`.

> Content catalog for this knowledge base. The LLM updates this file on every ingest.
> --- `src/llm_wiki/scaffold/wiki/index.md`

#### MEM-OBJ-log
Label: Wiki operation timeline

Source-native identity: `wiki/log.md`. Storage: Markdown. Form: natural-language operation details and optional body prose, plus machine-parsed heading fields. Lineage: initialization seed/rendering and prescribed agent appends after maintenance/answer filing. This is authored operational history, not a transcript of model turns or raw tool executions. Consumers: recent-log CLI/MCP returns heading summaries only; search/expand can return body prose. Authority: reported history to an agent/human, not an automatic experience-update rule. The demo body reports ingest outputs but supplies no authenticated trace. No supplied object counterpart; distinct from all writing routes. SRC-1: `src/llm_wiki/scaffold/wiki/log.md`, `src/llm_wiki/stats.py`, `examples/demo/wiki/log.md`.

> Append-only timeline of wiki operations. Each entry uses a consistent prefix for parsing:
> --- `src/llm_wiki/scaffold/wiki/log.md`

#### MEM-OBJ-page-metadata
Label: Page associations and access metadata

Source-native identity: page paths/stems, YAML `raw_file` and `sources`, and wikilinks embedded in Markdown. Storage: same files as the content objects; indexes, counts and graph results are reconstructed in process. Form: symbolic at filename association, YAML/reference checks and link resolution; natural-language meaning of linked pages is separate. Lineage: template seeds plus caller/agent-authored fields and links. Consumers: status, lint, list, backlinks, graph and stats; answering agents may then interpret their results. Authority: coverage and navigation rules, not source truth. Tags and dates are metadata, but the inspected retrieval does not select by tags, source confidence or freshness. `sources_consulted` in answer templates is not the `sources` field validated by lint. No supplied object counterpart; an operative access part across several page objects, not a part of exactly one supplied record. SRC-1: `src/llm_wiki/ingest.py`, `src/llm_wiki/links.py`, `src/llm_wiki/lint.py`, `src/llm_wiki/stats.py`, `src/llm_wiki/scaffold/templates/answer.md`.

> status="ingested" if source_page else "pending",
> --- `src/llm_wiki/ingest.py`

### Routes

#### MEM-RTE-metadata-read
Label: Wiki metadata exploration

Endpoints/progression: caller requests CLI/MCP list, backlinks, graph or stats → current Markdown/path enumeration → deterministic association/count selection → terminal display or JSON → external agent/human. Owner: caller chooses operation, page/type and root; code computes pointers/counts. Context/state/effects: reads files and reconstructs indexes; persists no derived graph/cache. Distinct from [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query), which selects evidence text, and [RT-RTE-wiki-lint](runtime.md#rt-rte-wiki-lint), which diagnoses violations. No supplied metadata-exploration counterpart. SRC-1: `src/llm_wiki/cli.py`, `src/llm_wiki/mcp_server.py`, `src/llm_wiki/links.py`, `src/llm_wiki/stats.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Page paths/stems, inbound paths, graph nodes/edges, or counts; no answer synthesis.
- Later read-back: Uses current accumulated page names/links and parsed log headings on each invocation; caller may next request content.
- Delegated visibility: CLI display or MCP JSON reaches its external caller; actual model injection is host-owned.
- Selection predicate: List type filters directory prefixes; backlinks resolve the requested page and unique link targets; graph includes enumerated nodes and resolvable links; stats counts prefix membership and parseable log headings.
- Invalidation or expiry: Recomputed each call; file edits/deletions change later output, without a persistent graph requiring invalidation.
- Activation or effect: Provides navigation and counts; subsequent page choice or behavior change unobserved.
- Evidence limits: Pointers/counts are neither evidence completeness nor semantic quality; graph omits unresolved/ambiguous edges and does not preserve linked passages.

> nodes = [{"id": p.rel_path, "stem": p.stem} for p in pages]
> --- `src/llm_wiki/links.py`

#### MEM-RTE-log-read
Label: Recent operation read

Endpoints/progression: CLI `log` or MCP `wiki_recent_log` request → `parse_log` reads retained timeline → regex heading extraction and tail slicing → external caller. Owner: caller sets root/limit; code selects recognized headings. State/effects: transient parsed summaries; no log write. No supplied route counterpart; related query reload can instead read the entire log, and [RT-RTE-project-init](runtime.md#rt-rte-project-init) creates its initial seed. SRC-1: `src/llm_wiki/stats.py`, `src/llm_wiki/cli.py`, `src/llm_wiki/mcp_server.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Date, operation and detail dictionaries, or formatted headings; no entry body text.
- Later read-back: Later calls read accumulated timeline entries but only those matching the parser.
- Delegated visibility: Caller receives parsed summaries, not complete retained reasons or operational traces.
- Selection predicate: Heading regex and last limit matches in file order; default limit 10. This is not timestamp sorting or a token budget.
- Invalidation or expiry: Re-read each call; source text remains reachable by full-page expansion even if omitted from this result.
- Activation or effect: Exposes reported history; automatic revision from it or changed agent behavior unobserved.
- Evidence limits: Hyphenated operation names are excluded and multiline bodies are omitted; append-only integrity is not enforced.

> {"date": date, "operation": op, "detail": detail} for date, op, detail in entries[-limit:]
> --- `src/llm_wiki/stats.py`

### Claims

#### MEM-CLM-log-parser
Label: Operation parser coverage mismatch

Finding: the prescribed operations `answer-filed` and `synthesis-update` do not match `\w+` immediately followed by the required space/pipe. Therefore recent-log delivery and stats' log-entry count omit otherwise correctly formatted headings using those operation names. Bodies beneath recognized headings are also absent from recent-log output. This corrects any interpretation of supplied recent-operation coverage as complete; it does not claim loss of the underlying Markdown or absence of filed answers. Closest supplied [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query) requests answer-filed headings but does not cover their parser; no duplicate claim counterpart. SRC-1: `src/llm_wiki/stats.py`, `src/llm_wiki/scaffold/AGENTS.md`.

> LOG_ENTRY_RE = re.compile(r"^## \[([^\]]+)\] (\w+) \| (.+)$", re.MULTILINE)
> --- `src/llm_wiki/stats.py`

> Operations: `ingest`, `query`, `lint`, `answer-filed`, `synthesis-update`, `init`
> --- `src/llm_wiki/scaffold/AGENTS.md`

### Evidenced absences

#### MEM-ABS-withdrawal-gate
Label: Toolkit semantic withdrawal gate

- implementation conclusion status: absent

Bounded finding: no semantic-rejection/withdrawal gate connects lint/contradiction status to built-in search or expansion in the inspected toolkit. Searched all CLI command and MCP tool registrations, and directly read `src/llm_wiki/search.py`, `src/llm_wiki/expand.py`, `src/llm_wiki/links.py`, `src/llm_wiki/lint.py`, `src/llm_wiki/new_page.py`, `src/llm_wiki/ingest.py` at the frozen revision; supplemental query was `delete|remove|withdraw|reject|compac|summari|cache|hook|embed|trust|history|log|limit` across `src/` and shipped operating surfaces. Corpus enumeration includes all `*.md`; search filters positive score, not ledger status; expansion resolves a file and extracts text. Lint reports but does not rewrite or quarantine. This is not an absence of manual deletion, agent criticism or host controls. It prevents treating a stale marker or resolved ledger row as a software-enforced end of reliance. Closest supplied [RT-RTE-wiki-lint](runtime.md#rt-rte-wiki-lint) is the reporting route, not this bounded absence. SRC-1: `src/llm_wiki/links.py`, `src/llm_wiki/search.py`, `src/llm_wiki/cli.py`, `src/llm_wiki/mcp_server.py`, `src/llm_wiki/lint.py`.

> for path in sorted(wiki_root.rglob("*.md")):
> --- `src/llm_wiki/links.py`

### Behavioral-authority paths

#### MEM-BAP-wiki-content
Label: Retained wiki interpretation

Consumer: later external maintainer or answering agent. Channel: project files read directly, CLI output or MCP search/expansion JSON. Force: natural-language evidential and discovery influence after interpretation, not toolkit-enforced instruction priority. Horizon: later maintenance/query invocations across project sessions if the same project is selected. Source summaries, topic pages, synthesis, conflict explanations and prior answers can affect selections and answers; delivery does not prove compliance, changed behavior or improved capacity. Raw/source content is not elevated to permission authority by this mechanism, and inspected tools implement no claim-level trust filter. Distinct from [RT-BAP-maintainer-instructions](runtime.md#rt-bap-maintainer-instructions), which carries schema/operation guidance rather than subject-matter knowledge. SRC-1: `src/llm_wiki/scaffold/AGENTS.md`, `src/llm_wiki/mcp_server.py`, `src/llm_wiki/search.py`.

> 4. **Synthesize** an answer with wikilinks and citations to source pages.
> --- `src/llm_wiki/scaffold/AGENTS.md`

## Annotations

#### On [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest)

Memory-specific lineage: human-admitted raw source → requested full read/discussion → agent-authored source summary and topic edits → conditional synthesis/conflict edits → updated catalog/log. Persistence is Markdown, not provider parameters. No software diff/approval stage is inserted between authorship and admission. Batch mode is a countercase to universal discussion-first admission. Human guidance and source choice remain separate from the agent's claim choices. Reasons may be retained as quotes, evolution text, conflict explanations and links; neither template fields nor later query selection require all reasons to survive. Source evidence: SRC-1 `src/llm_wiki/scaffold/AGENTS.md`, `src/llm_wiki/scaffold/templates/source.md`, `src/llm_wiki/scaffold/templates/concept.md`, `src/llm_wiki/scaffold/wiki/contradictions.md`; supplied route carries the ingest quotations. Derived content reaches later query/maintenance invocations by requested reload, not an automatic push.

#### On [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query)

Read-back trigger is the human question. Foreground agent chooses query/page/heading; code ranks current retained files and extracts selected content. Search defaults are CLI 10 results and MCP 8; these are result-count bounds, not enforced total-token budgets. Built-in snippet `width=160` is not a strict 160-character bound: start may precede the match while end is `idx + width`. CLI display caps long snippets at 120 plus ellipsis; JSON/MCP preserve the helper snippet. Full-page expansion has no size cap; section expansion includes its matched heading and descendants until a same-or-higher heading. It omits other sections, not old host turns. The whole file remains on disk and can be reloaded. This resembles selective external loading, not an isolated execution frame or compaction checkpoint. No sub-agent return boundary is wired by these tools. SRC-1: `src/llm_wiki/search.py`, `src/llm_wiki/expand.py`, `src/llm_wiki/cli.py`, `src/llm_wiki/mcp_server.py`; supplied route supplies extraction evidence.

> start = max(0, idx - width // 3)
> end = min(len(text), idx + width)
> --- `src/llm_wiki/search.py`

Both prose and frontmatter enter lexical scoring because the body filter removes heading lines, not YAML. Filed answers, log bodies and contradictions are searchable alongside source pages. Search returns access hints/snippets; agent-selected expansion is a second selection, not proof that all source support reaches the consumer. The answer-filing transformation creates derived memory from a question and selected knowledge, not automatic trace learning. Actual persistence, later use and benefit are unobserved. SRC-1: `src/llm_wiki/search.py`, `src/llm_wiki/scaffold/AGENTS.md`.

#### On [RT-RTE-qmd-search](runtime.md#rt-rte-qmd-search)

External numerical/index storage, embedding provenance, selection algorithm and freshness are uninspected. README affords manual collection creation and embedding; the target adapter does not implement those writes or a refresh trigger after wiki edits. Adapter output retains relative page pointer, score and at most 160 characters of snippet/content; it does not carry an opaque embedding or full support passages into the agent. `include_index=False` is implemented only for built-in BM25, not passed to qmd. This limits cross-backend selection equivalence without implying qmd cannot support a filter externally. SRC-1: `README.md`, `src/llm_wiki/search.py`; supplied route provides the backend branch quotation.

#### On [RT-RTE-wiki-lint](runtime.md#rt-rte-wiki-lint)

Curation is delegated: diagnostics → instructed immediate error fixes and proposed warnings → requested conflict review and log append. Inspection has no automatic persisted issue store. Contradiction checks recognize marker language and page-name presence, not claim-level status or argument correctness. Semantic correction can update readable content, but only actual edits/deletions alter built-in later reload; no downstream rejection is connected to the report. A resolved contradiction can retain reasons in resolution notes. Body explanations remain available to full expansion, not necessarily recent-log parsing. SRC-1: `src/llm_wiki/lint.py`, `src/llm_wiki/scaffold/AGENTS.md`, `src/llm_wiki/scaffold/wiki/contradictions.md`; supplied route covers report delivery/admission.

#### On [RT-RTE-pending-watch](runtime.md#rt-rte-pending-watch)

Association metadata determines pending/ingested, and only pending filenames are notified. Missing originals create orphan status; missing `raw_file` creates incomplete status. Same-name source changes are not hashed or date-compared. `seen_pending` is process-local suppression state, not a durable semantic result or trace-derived policy. The shipped CLI callback prints; it does not deliver a source to a model or perform admission. Library callback capability alone does not establish another actual consumer. SRC-1: `src/llm_wiki/ingest.py`, `src/llm_wiki/watch.py`, `src/llm_wiki/cli.py`; supplied route retains the selection quotation.

#### On [RT-RTE-instruction-sync](runtime.md#rt-rte-instruction-sync)

Retained mutable instructions have natural-language authority at the external maintainer, unlike topic knowledge's evidential role. Sync copies canonical bytes to the fixed scaffold/example targets, not arbitrary initialized user projects. Initial packaged instructions are static; modifications accumulated through convention changes can become later behavioral memory if reloaded. No automatic transformation from operational logs into instruction edits is wired. Co-evolution requests human participation but specifies no per-change acceptance protocol or preserved rationale. SRC-1: `scripts/sync_agents.py`, `src/llm_wiki/scaffold/AGENTS.md`; supplied sync record and [RT-BAP-maintainer-instructions](runtime.md#rt-bap-maintainer-instructions) supply passages. Improvement and actual activation remain unestablished independently.

## Write side

Acquisition is human source curation, not toolkit crawling. Semantic writes are agent-authored and physically performed through the external host; admission follows open ingest/query/lint requests and human guidance rather than a deterministic semantic gate. A workflow request is not individual content approval. Page scaffolding instead admits caller type/slug/title and a project-local template through syntax/existence checks; force bypasses overwrite rejection. Project initialization similarly copies bundled state with optional overwrite. These alternate writers can expose empty or incomplete pages to retrieval before the maintainer completes bookkeeping. [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query), [RT-RTE-wiki-lint](runtime.md#rt-rte-wiki-lint), [RT-RTE-page-create](runtime.md#rt-rte-page-create), [RT-RTE-project-init](runtime.md#rt-rte-project-init).

Maintenance keeps originals, derived summaries, cross-source accounts, conflict explanations and prior answers distinct. Source links retain attribution affordances, not guaranteed faithful compression. The initial template/seed lineage is known; the agent/model's internal derivation remains opaque. Logs record authored operation summaries, not raw episodes transformed by an automatic learning pipeline. No session transcript-to-summary/checkpoint path is implemented in the inspected toolkit; external host compaction remains uninspected. Instruction evolution is separate from topic curation and has no automatic log-fed update connection. [MEM-OBJ-sources](#mem-obj-sources), [MEM-OBJ-log](#mem-obj-log), [RT-RTE-instruction-sync](runtime.md#rt-rte-instruction-sync).

Rejection is local and mostly syntactic: bad type/slug, missing template, existing destination unless forced, invalid root and failed explicit resolution. Lint reports invalid structure after admission. Semantic withdrawal is manual/delegated; deleting or rewriting a page changes later built-in enumeration, but does not automatically purge copied claims from other pages or external qmd indexes. Optional Git initialization does not implement commits or rollback. Raw immutability and log append-only treatment depend on host/agent compliance. [MEM-ABS-withdrawal-gate](#mem-abs-withdrawal-gate), [RT-RTE-page-create](runtime.md#rt-rte-page-create), [RT-RTE-project-init](runtime.md#rt-rte-project-init), [RT-RTE-wiki-lint](runtime.md#rt-rte-wiki-lint).

## Read-back

Content read-back uses the query route and direct host reads afforded by the protocol. Trigger, selection and delivery are separate: the human asks; the agent chooses index/search/page/heading; code ranks/extracts; the host supplies returned data to the agent. Every tool response is requested. Watch notifications are polling outputs, not a wired unsolicited knowledge push into model context. The catalog is not exclusive: list, links and BM25 can reveal unindexed pages. [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query), [MEM-RTE-metadata-read](#mem-rte-metadata-read), [RT-RTE-pending-watch](runtime.md#rt-rte-pending-watch).

Structural consumers use names and associations. Status uses `raw_file`; lint uses references, marker language and substring catalog checks; backlinks/graph use resolvable wikilinks; stats counts directory membership and recognized log headings. These selectors produce pointers/diagnostics, not complete semantic source content. Recent-log output additionally omits body explanations and hyphenated operations. Full log expansion and built-in corpus search remain alternative read-back routes. [MEM-OBJ-page-metadata](#mem-obj-page-metadata), [MEM-RTE-log-read](#mem-rte-log-read), [MEM-CLM-log-parser](#mem-clm-log-parser).

Retention aims at project/session persistence, but no execution evidence establishes recurrent agent use. Content receives evidential authority through interpretation; revised maintainer instructions receive behavioral guidance authority only if loaded by the host. Neither delivery establishes learning, reliability or improvement. Sections and result counts bound selected output, not host window residency or total context. [MEM-BAP-wiki-content](#mem-bap-wiki-content), [RT-BAP-maintainer-instructions](runtime.md#rt-bap-maintainer-instructions).

## Integration issues

1. Parser coverage correction: [MEM-CLM-log-parser](#mem-clm-log-parser) limits any complete-history interpretation of [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query)'s answer-filed log and the supplied account of log consumers. Properly prescribed hyphenated entries do not reach recent-log/stats; source text still exists. SRC-1: `src/llm_wiki/stats.py`, `src/llm_wiki/scaffold/AGENTS.md`.
2. Distinct new identities: operative objects are retained inputs/outputs or access parts, not duplicate runtime routes. [MEM-RTE-metadata-read](#mem-rte-metadata-read) covers pointer/count exploration not declared by the supplied query/lint routes; [MEM-RTE-log-read](#mem-rte-log-read) covers parsed heading delivery. [MEM-BAP-wiki-content](#mem-bap-wiki-content) is subject-matter interpretation, distinct from maintainer-instruction guidance. No possible duplicate remains after supplied-record comparison.
3. Human control remains unresolved at individual semantic edits and optional filing: discussion and an offer are not enforced acceptance handshakes. This prevents a per-claim human-approval conclusion, not the known human source-curation role. [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query); SRC-1: `src/llm_wiki/scaffold/AGENTS.md`.
4. qmd freshness, embedding lineage and deployment remain external unknowns; include-index behavior is not equivalent across adapters. This prevents guaranteed reload of current edited/withdrawn knowledge through the alternative backend. [RT-RTE-qmd-search](runtime.md#rt-rte-qmd-search); SRC-1: `src/llm_wiki/search.py`, `README.md`.
5. Template readiness is not admission success: the answer seed lacks `updated`, source seeds lack a filled `raw_file`, and both can enter enumeration before repair. Different answer `sources_consulted` and lint `sources` fields prevent assuming universal source-reference checking. [MEM-OBJ-answers](#mem-obj-answers), [MEM-OBJ-page-metadata](#mem-obj-page-metadata), [RT-RTE-page-create](runtime.md#rt-rte-page-create); SRC-1: `src/llm_wiki/scaffold/templates/answer.md`, `src/llm_wiki/scaffold/templates/source.md`, `src/llm_wiki/lint.py`.
6. No observed semantic revision/reliance loop: the demo retains a revised thesis and an open disagreement, but not authenticated before/after operation, blame assignment, or later decisions. Reasons are afforded in evolution/resolution text; mandatory later reading is not established. Preserve the runtime's independent theory-condition and learning limits rather than treating a ledger as a complete theory builder. [MEM-OBJ-synthesis](#mem-obj-synthesis), [MEM-OBJ-contradictions](#mem-obj-contradictions), [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest); SRC-1: `examples/demo/wiki/synthesis.md`, `examples/demo/wiki/contradictions.md`, `examples/demo/wiki/log.md`.

## Limitations and checks

HEAD was directly rechecked as `a424e6875aa2d5736d9c0d03d7c28bdbe32892a5`; Git status showed no source-checkout changes. Source identity and run ID match the supplied boundary and invocation. All new evidence stays within SRC-1. Supplied member types, collection, worker rules and record contract were read completely; runtime was recovered in bounded ranges. The invocation's memory job and member type govern this output, not prior characterizations.

No deployment, compliance, semantic accuracy, measured maintenance benefit or causally demonstrated improvement is claimed. Host/provider internals and external qmd state remain uninspected. Source tests were not run. Coverage is the shipped mechanism surfaces and sampled illustrative state, not every example claim. Validation: passed with the invocation's deterministic output check; this establishes form and quotation occurrence, not analytical acceptance.
