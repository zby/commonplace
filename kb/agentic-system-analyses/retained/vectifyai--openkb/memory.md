---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "OpenKB memory: compiled wiki revisions, source reload, sanitized chat history and portable instruction artifacts."
run-id: AAS-2026-11-09-openkb-bd9c4c38a842-01
source-identity: https://github.com/vectifyai/openkb
reviewed-boundary: "ff54396e575ee6feb0113b631a34caa082b441cc"
---

# OpenKB memory report

## Boundary and evidence

OpenKB retains document-derived knowledge as a filesystem wiki, conversation state as session JSON, and generated skills/decks as output files. This report covers the whole-system memory surfaces fixed by [boundary](boundary.md), not just the query agent. SRC-1 is the repository at ff54396e575ee6feb0113b631a34caa082b441cc. Direct source reads establish implementation and doctrine/design; supplied runtime records establish the baseline quoted below. No target execution, model calls, tests or examples were run. There is no observed-run or causal evidence of activation, benefit or successful maintenance.

The memory scope includes admission from local/URL documents, PDF indexing and cloud import; compiler updates and source metadata; CLI/REST saves; chat persistence; page editing/deletion; recompile/remove/lint; installed instructions, generated skills, evaluation sets, snapshots, decks and graph outputs. External model/PageIndex internals and enclosing agents are outside the frozen source. Their call sites and shipped instructions are inside it. Provider storage and weights remain opaque, not inferred to be embedding memory or a learned local store. See [RT-CMP-pageindex-client](runtime.md#rt-cmp-pageindex-client) and [RT-CMP-litellm-model](runtime.md#rt-cmp-litellm-model).

### Coverage inventory

“Direct” means source read in this job; “supplied” means the runtime/boundary account, not a fresh inspection. Uninspected supporting internals remain included; they do not become negative findings.

| Entry point or memory operation | Source path and inspection | Covering record or remaining limit |
| --- | --- | --- |
| CLI add; REST upload; watcher; URL conversion | Supplied `openkb/cli.py`, `openkb/converter.py`, `openkb/watch_service.py`; direct compiler | [RT-RTE-document-add](runtime.md#rt-rte-document-add); [MEM-OBJ-source-content](#mem-obj-source-content). Converter/URL and watcher internals not freshly audited; no claim of extraction fidelity or complete event coverage. |
| Local long PDF and direct cloud import | Direct `openkb/indexer.py` artifact writer and local indexing; supplied cloud-entry wiring | Source content record; [RT-CMP-pageindex-client](runtime.md#rt-cmp-pageindex-client). Cloud fetch normalization/remote persistence not completely inspected; no complete hosted-state or extraction guarantee. |
| Short summary, concepts, entities, related links and index | Direct `openkb/agent/compiler.py` templates, briefs, generation, writers, removal and index routines | Annotations on [RT-OBJ-wiki-pages](runtime.md#rt-obj-wiki-pages) and [RT-RTE-document-add](runtime.md#rt-rte-document-add); [MEM-OBJ-page-frontmatter](#mem-obj-page-frontmatter), [MEM-OBJ-index](#mem-obj-index). |
| Query tool registration; alternate whole-file/page/image reads | Direct `openkb/agent/query.py`, `openkb/agent/tools.py` | [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query). Model choice, no enforced token-volume budget. |
| CLI and REST exploration saves; chat-derived note writes | Direct `openkb/cli.py`, `openkb/api_helpers.py` save delegation, query/chat tools; supplied session route | [MEM-OBJ-explorations](#mem-obj-explorations); query annotation. CLI and helper save implementations differ. No inspected automatic index publication. |
| CLI resume; REST turns and browser restore | Direct `openkb/agent/chat_session.py`, `openkb/agent/chat.py` REST turn path, `openkb/api.py` load response; supplied CLI/browser wiring | [MEM-OBJ-session-history](#mem-obj-session-history), [MEM-OBJ-session-display](#mem-obj-session-display); session annotation. Frontend implementation supplied rather than independently reread. |
| Human body editing/deletion and REST page reads | Direct `openkb/page_ops.py`, `openkb/api_pages_router.py` | [MEM-RTE-page-edit](#mem-rte-page-edit). No model admission or generic caller-to-human identity guarantee. |
| Remove/recompile/lint and schema refresh | Direct compiler cleanup, schema refresh, linter; supplied CLI remove/recompile orchestration | [RT-RTE-wiki-maintain](runtime.md#rt-rte-wiki-maintain), [MEM-OBJ-diagnostics](#mem-obj-diagnostics). Structural withdrawal is not semantic unlearning. |
| Hash registry and retry/recompile selection | Direct `openkb/state.py`; supplied driver wiring | [MEM-OBJ-hashes](#mem-obj-hashes). Hashes govern admission/deduplication, not truth or page completeness. |
| Schema instructions and skill discovery/loading | Direct `openkb/schema.py`, `openkb/agent/query.py`; supplied discovery roots/runner | [RT-OBJ-agents-md](runtime.md#rt-obj-agents-md), [RT-BAP-skill-instructions](runtime.md#rt-bap-skill-instructions). Initialization of arbitrary user edits is unresolved. |
| Skill creator, nested query, validation and export | Direct `openkb/skill/creator.py`, full `openkb/prompts/skill_create.md`; supplied generator/validator wiring | [RT-RTE-skill-create](runtime.md#rt-rte-skill-create), [MEM-OBJ-skill-package](#mem-obj-skill-package). Generated output is not automatically installed. |
| Trigger/body evaluation and saved question sets | Direct `openkb/skill/evaluator.py` prompts, read selection, results and save/load, CLI eval dispatch | [MEM-RTE-skill-eval](#mem-rte-skill-eval), [MEM-OBJ-eval-sets](#mem-obj-eval-sets). Diagnostic model judgments, not task execution. |
| Skill iteration snapshots, restore and diffs | Direct `openkb/skill/workspace.py` snapshot/restore; supplied CLI invocation | [MEM-OBJ-iterations](#mem-obj-iterations). Diff internals not fully inspected; no semantic revision-history guarantee. |
| Deck producer/critic and retained HTML | Supplied `openkb/agent/skill_runner.py`, `openkb/deck/creator.py`, CLI deck snapshot hook | [RT-RTE-deck-produce](runtime.md#rt-rte-deck-produce). Styling/critic bodies not reread; no claim that hidden producer reasoning or method changes cross contexts. |
| Graph rendering | Direct `openkb/visualize.py`, `openkb/schema.py` | [MEM-OBJ-graph](#mem-obj-graph). Graph excludes explorations/reports/sources as nodes because enumeration uses three page directories. |
| External-agent navigation skill | Direct complete `skills/openkb/SKILL.md` | [MEM-RTE-host-read](#mem-rte-host-read), [RT-CLM-wiki-trust](runtime.md#rt-clm-wiki-trust). Host execution and compliance unobserved. |
| Operation log and lint reports | Direct `openkb/log.py`, `openkb/agent/linter.py`; supplied report retention | Diagnostics record. No automatic semantic-fix or log-to-method update established by these paths. |

## Core ideas

1. **Retained text, not local weight updates, carries accumulated knowledge.** Compilation writes summaries and rewrites selected concept/entity bodies. Later queries, compiles and generators can read them. The current body is not a sequence of appended source excerpts; update calls receive the old body and ask for a replacement. Sources remain separately reloadable. [RT-OBJ-wiki-pages](runtime.md#rt-obj-wiki-pages), [MEM-OBJ-source-content](#mem-obj-source-content).
2. **Access metadata and knowledge bodies have different consumers.** Briefs feed the planner, source counts inform entity salience, source lists govern deletion, and summary pointers/tree ranges guide detailed retrieval. A source association is neither sentence-level provenance nor a guarantee that removing its link removes its claims. [MEM-OBJ-page-frontmatter](#mem-obj-page-frontmatter), [MEM-OBJ-index](#mem-obj-index).
3. **Read-back is predominantly requested and model-selected.** Query models request paths and ranges after a question. Chat history is instead composed automatically by code for the selected session. Skill descriptions enter chat instructions automatically at construction; their bodies enter only on a model tool request. None of these deliveries establishes compliance. [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query), [RT-RTE-session-chat](runtime.md#rt-rte-session-chat), [RT-BAP-skill-instructions](runtime.md#rt-bap-skill-instructions).
4. **Context reduction has several distinct mechanisms.** Compiler calls use explicit independent contexts; planning sees compact briefs, updates additionally see selected old bodies. Long-document compilation receives a tree summary and overview rather than all pages. Chat replaces image payloads with reload notes but does not semantically summarize the rest in the inspected sanitizer. Nested queries and deck critics use fresh contexts and copy back only an answer or artifact-mediated effect. [RT-RTE-skill-create](runtime.md#rt-rte-skill-create), [RT-RTE-deck-produce](runtime.md#rt-rte-deck-produce), session-history record.
5. **Instruction export and installation are separate memory stages.** The skill creator requests conditional decision rules and reasons derived from sources, while forbidding producer-wiki links in portable output. A generated directory can persist without ever becoming live instructions; installed roots or an external host supply the later consumer. [MEM-OBJ-skill-package](#mem-obj-skill-package), [RT-BAP-skill-instructions](runtime.md#rt-bap-skill-instructions).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-source-content
Label: Retained source content

Identity: `wiki/sources/<doc>.md`, per-page `<doc>.json`, and referenced image files. These are distinct from the generated bodies in [RT-OBJ-wiki-pages](runtime.md#rt-obj-wiki-pages), not duplicate page declarations. Form: source prose is natural language; page numbers, paths and JSON structure are symbolic routing data; images are opaque visual payloads exposed as base64, not readable textual summaries and not local model weights. Substrate: filesystem source files and extracted image bytes. Lineage: converted input documents; long PDFs use cloud OCR when available or local extraction fallback. Direct cloud import is a separate upstream source route. Provider derivation of tree summaries and conversion fidelity remain unverified. SRC-1, `openkb/indexer.py`, `openkb/tree_renderer.py`, `openkb/agent/tools.py`; short conversion wiring from [RT-RTE-document-add](runtime.md#rt-rte-document-add).

> if not all_pages:
>     raise RuntimeError(f"No page content extracted for {pdf_path.name}")
> --- `openkb/indexer.py`

> (sources_dir / f"{doc_name}.json").write_text(
>     json_mod.dumps(pages, ensure_ascii=False, indent=2),
>     encoding="utf-8",
> )
> --- `openkb/indexer.py`

Consumers: query/page/image tools, creator and runner wiki reads, external hosts; recompile uses retained short source text but long recompile uses retained summary. Persistence crosses sessions until explicit mutation/removal. Source content is evidence at answering consumers, not code-authorized commands. Tool access is reachable even for an entire in-root JSON file. PageIndex's own `.openkb` blobs/database or hosted state are separate opaque storage, described in [RT-CMP-pageindex-client](runtime.md#rt-cmp-pageindex-client), not proved equivalent to these exported files.

#### MEM-OBJ-page-frontmatter
Label: Page routing and source associations

Identity: code-managed `type`, `sources`, `full_text`, `doc_type`, descriptions and entity metadata on generated wiki pages. Distinct from the bodies in [RT-OBJ-wiki-pages](runtime.md#rt-obj-wiki-pages). Form/substrate: symbolic YAML keys/lists/paths in Markdown; the description value is a natural-language brief, separately interpreted by planning/reading models. Both parts are inspectable and have different authority: source lists drive deterministic removal, while prose briefs guide model choice. SRC-1, `openkb/agent/compiler.py`, `openkb/tree_renderer.py`, `openkb/visualize.py`.

> fm_lines.append(f"doc_type: {doc_type}")
> fm_lines.append(_yaml_kv_line("full_text", f"sources/{doc_name}.{ext}"))
> --- `openkb/agent/compiler.py`

> n_sources = len(fm_dict["sources"]) if isinstance(fm_dict.get("sources"), list) else 0
> --- `openkb/agent/compiler.py`

Lineage: code constructs/merges fields around model-authored bodies. Briefs come from model descriptions, legacy `brief`, or the first 150 body characters when missing. Source counts are recurrence cues in the entity planner. Source lists identify contributing documents at page granularity, not quoted passages or claim dependencies. The graph reads `full_text` as a source association; body edits preserve old metadata verbatim. Thus metadata can outlive a change in body meaning. Consumers and consequences differ from content-as-evidence. Unknown initial user metadata provenance does not suppress these known transformations.

#### MEM-OBJ-index
Label: Wiki content catalog

Identity: `wiki/index.md`, distinct from generated bodies and local schema. Form: natural-language descriptions plus symbolic section boundaries and wikilink paths. Substrate: Markdown file. Lineage: compiler inserts document entries and updates concept/entity entries from successful outputs; seed has an Explorations section, but that does not establish save-time catalog admission. Consumers: query/linter/creator models and instructed external hosts. Model-directed selection reads the catalog's descriptions and links; Python section editing uses fixed syntax. SRC-1, `openkb/agent/compiler.py`, `openkb/schema.py`, `openkb/agent/query.py`.

> if _section_contains_link(lines, "## Concepts", concept_link):
>     if name in concept_briefs:
>         _replace_section_entry(lines, "## Concepts", concept_link, concept_entry)
> else:
>     _insert_section_entry(lines, "## Concepts", concept_entry)
> --- `openkb/agent/compiler.py`

Document entries are skipped when the document link already exists; concept/entity brief refresh is not identical to document brief refresh. No observed synchronization or comprehensive catalog guarantee follows. Closest supplied object is [RT-OBJ-wiki-pages](runtime.md#rt-obj-wiki-pages), whose identity explicitly excludes index routing metadata; this is distinct, not a duplicate.

#### MEM-OBJ-hashes
Label: Hash registry

Identity: `.openkb/hashes.json` registry mapping hashes to document metadata. Form: symbolic keys, paths and metadata; substrate: JSON file loaded into a Python mapping. Lineage: file hashing and post-compile driver registration; consumers: deduplication, identifier resolution, recompile and remove/retry selection. This is control memory, not synthesized knowledge. Distinct from wiki bodies and [RT-RTE-document-add](runtime.md#rt-rte-document-add), which is its producing route. SRC-1, `openkb/state.py`; filename/driver use supplied in runtime and boundary.

> def add(self, file_hash: str, metadata: dict) -> None:
>     """Register file_hash with metadata and persist to disk."""
>     self._data[file_hash] = metadata
>     self._persist()
> --- `openkb/state.py`

Fixed consumer rules govern skip/reload/retry, not content truth. An admitted hash does not prove every planned page was generated; malformed plans and collected page failures can return normally. [RT-RTE-document-add](runtime.md#rt-rte-document-add).

#### MEM-OBJ-explorations
Label: Saved answers and chat notes

Identity: `wiki/explorations/*.md`. Form: natural-language answers/notes with symbolic YAML question metadata when saved by query drivers. Substrate: filesystem Markdown. Lineage: current question plus model answer; chat may separately write or overwrite notes through constrained tools. This is derived conversational material rather than the source-backed compiler page-body container [RT-OBJ-wiki-pages](runtime.md#rt-obj-wiki-pages). Closest supplied routes are [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query) and [RT-RTE-session-chat](runtime.md#rt-rte-session-chat); object identity is distinct.

SRC-1, `openkb/cli.py` has two save implementations. The REST helper delegates to `save_exploration`, which locks, strips ghost links, escapes the question and allocates a unique slug. Actual CLI `query --save` duplicates simpler logic, potentially replacing a same-slug file and not escaping its question. Neither inspected branch updates the index. This contradicts interpreting schema's intended catalog as a complete save-time consumer route.

> explore_path.write_text(
>     f'---\nquery: "{question}"\n---\n\n{cleaned_answer}\n',
>     encoding="utf-8",
> )
> --- `openkb/cli.py`

The answer is preserved after link demotion, not after truth verification. Later query/chat/creator reads can request a known path; external hosts can search. No guaranteed automatic rediscovery of every exploration is established. Retaining a query result is a trace-fed write of behavior-relevant text available to later consumers, not proof of improved capacity or autonomous method learning.

#### MEM-OBJ-session-history
Label: Reusable SDK chat history

Identity: `history` in `.openkb/chats/<id>.json`. Form: symbolic SDK message/tool records enclosing natural-language text and tool arguments/results. Large image data URLs are replaced by natural-language reload hints. Substrate: in-memory list and persisted JSON. Distinct from the display object below, and from the containing [RT-RTE-session-chat](runtime.md#rt-rte-session-chat) route. SRC-1, `openkb/agent/chat_session.py`, `openkb/agent/chat.py`.

> self.history = sanitize_history(new_history)
> --- `openkb/agent/chat_session.py`

> text += " Call get_image again if you need to inspect it."
> --- `openkb/agent/chat_session.py`

Raw-to-derived chain: SDK `to_input_list()` history → recursive sanitizer, with `get_image` call IDs used to recover source paths → saved/reloaded history → code prepends all retained history to the next user turn. The next model receives text and symbolic tool records, not merely final assistant prose. The reducer removes image bytes preferentially; other turns/tool text remain under this inspected transformation. It is not a semantic compactor or a learned summary. Reloading image content requires a later model tool choice. A missing/unrecoverable image path weakens the hint but still removes the data URL. Actual model-context overflow and provider-side compression are uninspected. Explicit new-session/deletion controls terminate reuse; no time-based expiry is established here.

#### MEM-OBJ-session-display
Label: Session display text and read trace

Identity: `user_turns`, `assistant_texts`, `assistant_traces` and session title/counters in the same JSON. Form: prose strings and symbolic display steps/tool-call arguments; substrate: persisted JSON returned by REST load. Distinct operative part from [MEM-OBJ-session-history](#mem-obj-session-history): it has a different consumer and filter. SRC-1, `openkb/agent/chat.py`, `openkb/agent/chat_session.py`, `openkb/api.py`.

> if d.get("name") in _TRACE_READ_TOOLS:
>     trace.append(
>         {"kind": "tool", "name": d.get("name"), "arguments": d.get("arguments")}
>     )
> --- `openkb/agent/chat.py`

REST retains ordered narration/read-call display steps, not every write argument or tool result. CLI may have empty traces; frontend uses text fallback per the supplied boundary/runtime. Session-load response sends display arrays, not SDK history. This supports human/browser continuity, not an independent model learning route. Omitting write payloads from the display trace does not establish their omission from SDK history.

#### MEM-OBJ-skill-package
Label: Generated portable skill files

Identity: `output/skills/<name>/SKILL.md` and package references/scripts. Form: natural-language method body/reasons/reference prose; symbolic activation metadata, file paths and any authored scripts are distinct executable/configuration parts. Substrate: filesystem directory and exported/copied package. Actual generated content and script execution are not supplied. Closest route is [RT-RTE-skill-create](runtime.md#rt-rte-skill-create); closest live consumer is [RT-BAP-skill-instructions](runtime.md#rt-bap-skill-instructions). This object is the generated output, not that installed instruction referent.

SRC-1, `openkb/prompts/skill_create.md`, `openkb/skill/creator.py`: user intent plus selected wiki/source reads guide distillation into conditional decision rules and short reasons. The prompt asks for source reading, known gaps and at least one revision pass; it does not prove those actions or reasoning quality occurred.

> - **When you see X, prefer Y over Z** — <one-line reason>
> --- `openkb/prompts/skill_create.md`

> * **Forbidden**: `[[concepts/...]]`, `[[summaries/...]]`,
>   `[[sources/...]]` — these point at the producer's wiki, which is not
>   shipped. On the consumer's side they are dead links *and* wasted
>   context tokens. Use them at compile time to navigate the wiki, but
>   never write them into the shipped output.
> --- `openkb/prompts/skill_create.md`

Reasons are requested inline, and package-local references may travel with the result; producer navigation lineage deliberately does not. Later installed-body readers can receive reasons if the model wrote them. Neither retention of full source rationale nor consumption of every reference is guaranteed. Validation is diagnostic and marketplace retention can proceed with errors; installation remains separate. No trace-of-the-system's-own-operation-to-method update is established merely by generating rules from external documents.

#### MEM-OBJ-eval-sets
Label: Saved skill evaluation questions

Identity: `.openkb/eval-sets/<skill_name>.json`. Form: natural-language questions grouped by symbolic `should_trigger`/`should_not` labels; substrate: JSON. Lineage: generated from current description/body/reference previews, or supplied from a saved file. Consumers: explicitly requested later evaluator invocations using `--eval-set`. Distinct from generated skills and their creation route; paired with [MEM-RTE-skill-eval](#mem-rte-skill-eval). SRC-1, `openkb/skill/evaluator.py`, `openkb/cli.py`.

> "should_trigger": [p.question for p in prompts if p.expected == "trigger"],
> "should_not": [p.question for p in prompts if p.expected == "no-trigger"],
> --- `openkb/skill/evaluator.py`

This retained payload contains expected membership labels, not generated answers, grader criticisms or execution traces. Saving fresh sets is optional and overwrites the named JSON file. The later consumer uses labels as reference expectations for triggering, not truth or task-success oracles.

#### MEM-OBJ-iterations
Label: Skill iteration snapshots

Identity: `output/skills/<name>-workspace/iteration-N/` copies and structural `diff.md`. Form: same content encodings as copied skill packages; symbolic iteration names and structural comparison. Substrate: filesystem directories. Lineage: CLI pre-overwrite copy of current output; restore first snapshots current output, then replaces it with chosen prior directory. Consumer: explicit history/rollback commands and operator inspection, not automatic winner selection. Distinct from current [MEM-OBJ-skill-package](#mem-obj-skill-package); closest supplied route is [RT-RTE-skill-create](runtime.md#rt-rte-skill-create). SRC-1, `openkb/skill/workspace.py`.

> if dest.exists():
>     save_iteration(kb_dir, skill_name)
>     shutil.rmtree(dest)
> shutil.copytree(src, dest)
> --- `openkb/skill/workspace.py`

This preserves alternate whole-file checkpoints, including chat edits if captured later. It does not preserve the model's hidden reasons or cause evaluation scores to choose a successor. Independent deck snapshots are supplied by the CLI deck hook in runtime; their full restore semantics were not inspected here.

#### MEM-OBJ-diagnostics
Label: Operation log and lint reports

Identity: `wiki/log.md` operation entries and `wiki/reports/` lint output. Form: natural-language descriptions/reports plus symbolic timestamps/categories; substrate: Markdown. These are different parts grouped only for their diagnostic retention role: log is a raw operation description, lint report is derived model/structural assessment. Neither is the compiler's knowledge-body object. Closest route: [RT-RTE-wiki-maintain](runtime.md#rt-rte-wiki-maintain). SRC-1, `openkb/log.py`, `openkb/agent/linter.py`; report writing supplied by runtime.

> entry = f"## [{date_str}] {operation} | {description}\n\n"
> --- `openkb/log.py`

> tools=[list_files, read_file],
> --- `openkb/agent/linter.py`

The lint agent can request contradictions, gaps, staleness and redundancy checks but receives no repair tool. Reports and log remain readable to humans or explicit wiki tool reads. These retention capabilities do not identify an automatic semantic-fix or log-trained instruction consumer. Structural `lint --fix` is a separate code path, not execution of model report recommendations.

#### MEM-OBJ-graph
Label: Derived wiki graph

Identity: `build_graph` output and rendered HTML graph. Form: symbolic node/edge JSON plus natural-language descriptions; substrate: in-memory mapping then HTML output. Lineage: enumerate `PAGE_CONTENT_DIRS` (`summaries`, `concepts`, `entities`), parse frontmatter/wikilinks, keep resolvable edges and count degree. Consumer: visualization/browser, not a model memory write-back. Distinct from wiki bodies and metadata; it is a projection of them. SRC-1, `openkb/visualize.py`, `openkb/schema.py`.

> if not tgt or tgt == src or (src, tgt) in seen:
>     continue
> seen.add((src, tgt))
> edges.append({"source": src, "target": tgt})
> --- `openkb/visualize.py`

Thus graph absence does not establish absence of an exploration, source or report. The graph cannot demonstrate semantic consistency, and no inspected graph-to-compiler feedback loop is established.

### Routes

#### MEM-RTE-page-edit
Label: Edit or delete wiki page

Distinct from [RT-RTE-wiki-maintain](runtime.md#rt-rte-wiki-maintain), whose referent is document removal/recompile/lint: these REST page-level endpoints replace bodies or delete concept/entity pages without removing a source document. SRC-1, `openkb/api_pages_router.py`, `openkb/page_ops.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: saved/deleted/not-found response plus demoted links or backlink impact; invalid page references raise/reject.
- Later read-back: current saved bodies reach later query/compiler/creator reads; deleted pages disappear and inbound links are demoted.
- Delegated visibility: inapplicable — this path performs deterministic filesystem edits without spawning a model context.
- Selection predicate: caller-supplied section/stem; edits allow concepts/entities/summaries, deletes only concepts/entities.
- Invalidation or expiry: explicit replacement/deletion; recompilation can regenerate edited/deleted products, with no permanent veto marker established.
- Activation or effect: under the ingest lock, existing frontmatter is retained and body saved atomically after ghost-link demotion; delete removes catalog entry and repairs affected inbound links.
- Evidence limits: REST caller identity does not itself establish human approval; implementation is a shipped human-facing Workbench editing surface, not evidence of an actual operator edit. No semantic correctness or permanent forgetting guarantee.

Admission: the caller supplies the proposed replacement, rather than a model proposing it on this path. Software checks allowed references/existence and links; no content-quality oracle or independent semantic veto is implemented here. A human using the Workbench can supply/edit/veto content; arbitrary API callers can also supply it. Mode: explicit content maintenance. Guidance: existing page and link context; retained result: body and unchanged metadata. Rejection: invalid/missing target; recovery: no revision snapshot or rollback in this inspected function, though later recompilation can replace content.

> cleaned_body, ghosts = strip_ghost_wikilinks(content, list_existing_wiki_targets(wiki))
> atomic_write_text(page, fm_block + cleaned_body)
> --- `openkb/page_ops.py`

The preservation of old frontmatter can leave a description or sources list that no longer describes the edited body. Code does not infer updated provenance from the new text.

#### MEM-RTE-skill-eval
Label: Evaluate and reload skill questions

Distinct from [RT-RTE-skill-create](runtime.md#rt-rte-skill-create): this is a diagnostic CLI evaluation and saved-question reuse path, not generation/admission of skill files. Owner: CLI chooses generated or loaded set; separate model calls grade trigger and coverage; Python computes rates and optionally writes fresh questions. SRC-1, `openkb/skill/evaluator.py`, `openkb/cli.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: scores, misses, coverage reasons, ambiguity and errors printed to the operator.
- Later read-back: `--save` persists fresh questions; a later explicit `--eval-set` reloads questions/expected labels. Skill replacement is not selected automatically by this dispatcher.
- Delegated visibility: question generator sees description, body and reference previews; trigger grader sees description and one question; coverage grader sees content and a should-trigger question. These are separate calls, not the same accumulated context.
- Selection predicate: selected skill directory and explicit eval-set path or generated count; reference previews include sorted Markdown references with each text sliced to 4000 characters despite the bytes-oriented constant/comment.
- Invalidation or expiry: named set can be overwritten; no automatic skill-version binding or freshness invalidation established by saved payload.
- Activation or effect: reference labels and grader verdicts affect rates; ambiguity/errors are excluded from relevant denominators; no skill mutation performed by CLI eval.
- Evidence limits: grades judge text and triggering, not actual skill task execution. No observed grades, improvement or causal validation supplied.

Proposer: model-generated questions or file author. Decider: model graders plus symbolic comparison to expected trigger labels. Human: selects skill, count and optional set/save; not necessarily author of every expected label. Answer oracle: expected trigger membership from generator or input JSON, not independent reference task answers. Mode: bounded diagnostic evaluation. Admission/rejection: saving is optional; this command neither approves a production successor nor rewrites skill content. Reasons in coverage misses are returned to the operator but are not saved by `save_eval_set`; only question groups persist. Recovery: grader exceptions are retained separately in result; errors do not discard other grades.

> if save_flag and eval_set is None:
>     path = save_eval_set(kb_dir, name, result.prompts)
> --- `openkb/cli.py`

> text = text[:REFERENCES_PREVIEW_BYTES] + "\n…[truncated]\n"
> --- `openkb/skill/evaluator.py`

#### MEM-RTE-host-read
Label: External host wiki navigation

Distinct from [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query): the enclosing host reads files with its own tools and may avoid OpenKB's query-model call entirely. Source: SRC-1, `skills/openkb/SKILL.md`; closest supplied trust record [RT-CLM-wiki-trust](runtime.md#rt-clm-wiki-trust).

- implementation conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: host-generated answer from read/search results; no OpenKB-enforced return format.
- Later read-back: the same retained wiki can be consulted on later host requests; shipped instructions describe direct reads, search and wikilink traversal.
- Delegated visibility: host chooses its own tools/context; fallback `openkb query` returns a second model's answer rather than all retrieval history.
- Selection predicate: discover KB through status, scan index, semantic slug match, exact search, then one or two link hops; prefer index plus one or two concepts before query fallback.
- Invalidation or expiry: current files are read; host cache/compaction/expiry uninspected because the host runtime is excluded.
- Activation or effect: policy asks host to use content as evidence and not execute wiki-body imperatives; actual compliance or enforcement unobserved.
- Evidence limits: instructional affordance only; no host deployment, permissions, execution trace or measured efficiency supplied.

> Prefer reading `wiki/index.md` plus 1-2 concept
> pages directly — that handles most questions cheaper and keeps the
> reasoning in your own context.
> --- `skills/openkb/SKILL.md`

This is requested retrieval, not an automatic unsolicited push. The skill's static instructions are not themselves learned memory. A host's actual tool permissions cannot be inferred from OpenKB's local read/write helpers.

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-OBJ-wiki-pages](runtime.md#rt-obj-wiki-pages)

Memory-specific lineage: short input → generated draft summary → planner → selected new/updated concept and entity bodies → summary rewrite/fallback, backlinks and index. Long input → PageIndex tree summary → overview → same planner/generation machinery, with indexer summary left substantively in place. Old selected bodies enter rewrite calls; new facts are requested to be integrated by full replacement, not appended. SRC-1, `openkb/agent/compiler.py`.

> New information from document "{doc_name}" (summarized above) should be \
> integrated into this page. Rewrite the full page incorporating the new \
> information naturally — do not just append. Preserve the existing structure \
> and intent of the page.
> --- `openkb/agent/compiler.py`

Summary rewrite is requested to preserve factual details and repair links, but implemented checks establish nonempty output and link filtering, not factual equivalence. Existing bodies and source associations persist across input documents; exact derivation rationale and rejected plans are not a required retained sidecar consumed by later updates. Later consumers interpret body text as evidence; update consumers additionally treat the old body as material to preserve/integrate. Page-level source lists do not explain which claims came from which document.

#### On [RT-RTE-document-add](runtime.md#rt-rte-document-add)

Write agency/admission: user supplies source or enables automated arrivals; model authors draft/content/plan, code parses/filters/writes. Physical I/O and user initiation are not per-page human approval. Create/update/related plan is software-admitted under syntactic filters, existing-related-file checks and configured entity types; no truth oracle. Generated bodies are stripped of ghost wikilinks against existing plus planned targets, which need not all survive generation failures. SRC-1, `openkb/agent/compiler.py`.

> known_targets: set[str] = (
>     list_existing_wiki_targets(wiki_dir)
>     | {f"concepts/{s}" for s in planned_slugs}
>     | {f"entities/{s}" for s in entity_planned}
>     | {f"summaries/{doc_name}"}
> )
> --- `openkb/agent/compiler.py`

Working-context control: planner reads descriptions or 150-character body fallbacks plus entity types/source counts, not all old bodies; selected update calls load full old body, with frontmatter removed when parseable. Each page generation has its own selected source/schema/summary/target-list messages. Long compile reads tree summary, not full per-page source JSON. Prompt-cache markers retain reusable prefixes at the provider interface; stripping unsupported markers preserves content. They are an optimization request, not a semantic compaction or proof of provider cache persistence. No hard total-token budget is established by concurrency, page ranges or call-count caps. SRC-1, `openkb/agent/compiler.py`.

#### On [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query)

Read-back chain: question → model follows prompted index/summary/entity/source strategy → model-selected path/range/image tool → selected text/image returned into the same model context → answer. This is requested selection. The page helper filters by page numbers, but the plain file helper also reads in-root JSON wholesale; prompt's “Never fetch the whole document” is not enforced by tool suffix or a token cap. SRC-1, `openkb/agent/query.py`, `openkb/agent/tools.py`.

Write/read-back distinction: optional saves create [MEM-OBJ-explorations](#mem-obj-explorations); later explicit file reads are possible. The inspected CLI/helper implementations do not append them to the index. Therefore “save result becomes guaranteed catalog-selected later context” is not supported. See Integration issues.

#### On [RT-RTE-session-chat](runtime.md#rt-rte-session-chat)

Memory-specific storage and selection: requested session ID chooses the persisted object; code supplies all sanitized SDK history plus new input. This is automatic historical delivery within a requested session, not model semantic retrieval from the session database. Display trace is separately filtered. Image-removal trigger is record/load sanitation, selector is code checking `input_image` data URLs, retained remainder is text/tool history plus a reload hint, and reload is a future `get_image` call. [MEM-OBJ-session-history](#mem-obj-session-history), [MEM-OBJ-session-display](#mem-obj-session-display).

Chat's write tool can admit notes/output replacements after the model authors them, with no per-file human confirmation in that helper. Its reads remain wiki-rooted; the returned chat tool set does not acquire generic output-file read authority merely because it has output write authority. Generic skill runner and external host grants are separate. SRC-1, `openkb/agent/query.py`; supplied [RT-RTE-deck-produce](runtime.md#rt-rte-deck-produce).

#### On [RT-RTE-wiki-maintain](runtime.md#rt-rte-wiki-maintain)

Withdrawal scope: compiler cleanup removes the document from source lists, Related Documents entries and standalone See-also references, deleting a page if no sources remain unless keep-empty is selected. It does not semantically regenerate surviving multi-source bodies to subtract every unsupported claim. SRC-1, `openkb/agent/compiler.py`.

> if sources_empty and not keep_empty:
>     path.unlink()
>     deleted.append(path.stem)
> elif new_text != text:
>     atomic_write_text(path, new_text)
>     modified.append(path.stem)
> --- `openkb/agent/compiler.py`

Consequently a removed source's textual influence may remain in shared pages, saved explorations, chat histories and generated packages. These are separate retained products; the inspected source-removal routines do not constitute provenance-complete semantic erasure. Recompile can regenerate bodies from retained source/summary plus existing selected bodies, so it also does not establish clean-room reconstruction. Lint's model reports do not automatically gate future reads or trigger semantic repairs. Source/registry deletion and partial PageIndex retry semantics remain as supplied, not broadened into system-wide forgetting.

#### On [RT-OBJ-agents-md](runtime.md#rt-obj-agents-md)

Initialization/control limit: arbitrary local `wiki/AGENTS.md` authorship and edit approval cannot be reconstructed from a read function. Known subsequent control: explicit schema refresh backs up differing local text to `AGENTS.md.bak` then replaces it with bundled guidance; fallback applies when absent. This is code-driven replacement after operator command selection, not model trace learning. SRC-1, `openkb/cli.py`.

> backup = wiki_dir / "AGENTS.md.bak"
> backup.write_text(current, encoding="utf-8")
> --- `openkb/cli.py`

#### On [RT-RTE-skill-create](runtime.md#rt-rte-skill-create)

Context and rationale: creator receives user intent/schema/static method and selected reads; nested query gets only the sub-question and fresh query instructions/tools. Parent sees returned answer, not full child working history. This resembles a temporary stack frame: selected input enters, answer escapes, frame is not promoted to shared model context. Wiki files remain reachable through tools but are not dereferenceable pointers in the window. Nested answers are derived from document/wiki content; they are not automatically persisted as separate explorations by `run_query` here. [MEM-OBJ-skill-package](#mem-obj-skill-package); SRC-1, `openkb/skill/creator.py`.

#### On [RT-RTE-deck-produce](runtime.md#rt-rte-deck-produce)

Memory distinction: producer/critic operate in separate contexts, joined by output path/brief and file reads/writes, not shared hidden reasoning. A retained HTML edit can affect later reading without changing installed producer/critic method. Optional critique is not an automatic trace-fed method revision. Output validation precedes critique and the wrapper does not revalidate afterward, as the supplied record establishes. Snapshot affordances are separate from content correctness.

## Write side

### Acquisition and admission

Document ingestion admits external content after user/file-event/upload initiation. Software chooses conversion/indexing and commits after compilation; authorship of generated bodies belongs to the model and admission to software, not to a human reviewing each page. Hash admission suppresses later duplicate work but does not certify output quality. PageIndex tree generation remains an opaque upstream transformation; exported page text and tree summary have separately known downstream consumers. [RT-RTE-document-add](runtime.md#rt-rte-document-add), [MEM-OBJ-hashes](#mem-obj-hashes), [MEM-OBJ-source-content](#mem-obj-source-content).

Compilation performs summarization, multi-source integration, description extraction, full-body replacement, backlink addition and catalog update. These are content curation mechanisms with implementation evidence. Their labels do not prove synthesis accuracy. Mechanical link filtering and nonempty checks reject some outputs but not false content. No per-claim warrant or retained criticism ledger is required by the inspected writers. The long-document branch never silently inherits full-source coverage from the short branch. Wiki-page annotation and document-add annotation retain the evidence.

### Alternative writers and maintenance

- Explicit page edits offer content-level human control in the Workbench, while the API itself accepts caller-supplied content without proving its author is human. It preserves code-managed frontmatter, unlike compiler metadata refresh. [MEM-RTE-page-edit](#mem-rte-page-edit).
- Query save and chat notes retain model-derived conversation results; save initiation is not a semantic acceptance check. Their later reachability does not depend on new weight training. Catalog incompleteness limits automatic rediscovery. [MEM-OBJ-explorations](#mem-obj-explorations).
- Session recording automatically derives reusable history from an interaction trace by dropping image payloads. This changes future context composition, not the meaning of prose through summarization. Display retention is a separate derivation used by people/browser. [MEM-OBJ-session-history](#mem-obj-session-history), [MEM-OBJ-session-display](#mem-obj-session-display).
- Skill generation distills documents into instruction candidates; diagnostic validation does not universally reject retention/publication. Snapshot/restore is operator-driven and distinct from evaluation or model criticism. No automatic evaluator-score-to-skill-successor loop is established by the inspected dispatcher. [RT-RTE-skill-create](runtime.md#rt-rte-skill-create), [MEM-RTE-skill-eval](#mem-rte-skill-eval), [MEM-OBJ-iterations](#mem-obj-iterations).
- Recompile, source removal, structural lint repair and page deletion are separate curation/withdrawal paths. They do not invalidate every descendant note, session or exported skill. Source list cleanup is not factual retraction in surviving prose. [RT-RTE-wiki-maintain](runtime.md#rt-rte-wiki-maintain) annotation.

The supported trace-fed chains are narrower than a claim of learning: saved answer → exploration → possible later read; SDK history → image-sanitized history → next session turn. External source → wiki → exported method is document-derived knowledge/instruction production, not by itself experience learning from OpenKB's own behavior. Grader outputs can inform a human but are not automatically admitted method revisions. No improved capacity, recursive self-improvement or outcome benefit is established.

## Read-back

| Retained part | Later trigger and selector | Delivery, budget and authority |
| --- | --- | --- |
| Wiki bodies, source Markdown, long page text and images | Question; query model chooses paths, page numbers and image paths | Tool outputs to query/chat/creator; 50-turn query cap is not a text-volume bound; whole-file alternate read remains. Evidence authority through model interpretation, not guaranteed compliance. |
| Briefs and source counts | New ingestion/recompile; code enumerates pages and constructs compact lines | Planner prompt; first 150 body characters only when description/legacy brief missing. Chosen old bodies enter update calls. Code controls which context each call receives. |
| Summary tree/pointers | Detailed question or creator source-reading task; model targets ranges | Source tool returns matching page bodies and image paths; range prompt is policy. Long compilation itself uses summary/overview, not this retrieval route. |
| Session history | Resume or next turn for selected ID; code supplies full sanitized history | Initial SDK input before new turn; image hints replace bytes; no semantic tail-summary policy established in sanitizer. Session context is not cross-session semantic search. |
| Session display arrays | REST session load/browser restore or CLI display/export | Display response/text fallback, not the SDK model-input history. Filtering read traces does not filter model history identically. |
| Saved exploration | Explicit requested path/search or a later model choosing that file | Wiki tool text; no inspected guaranteed save-to-index link. Accessible retention is not proven automatic discovery. |
| Schema | Agent/compile construction; local file wins else fallback | Natural-language instructions, reloaded across calls; user edits and explicit refresh can change future guidance. |
| Installed skill description/body | Chat construction plus subsequent model `read_skill`, or selected runner invocation | Catalog descriptions are supplied automatically; body deferred to a same-context tool response in chat, full instructions in runner. Not an isolated skill frame. |
| Generated skill package | Export/copy/install then host or execution-root discovery | Afforded external installation, not automatic adoption of output/skills. Body may carry reasons; producer-wiki provenance deliberately omitted. |
| Saved eval labels/questions | Explicit `--eval-set` | Separate evaluator prompts, question/label reference comparison; reference previews truncated by character slicing. Not task-success observation. |
| Snapshots | Explicit rollback/history request | Files restored/copied for future generation/review; no automatic score-selected winner. |
| Reports/log/graph/deck | Explicit inspection/read/render/critic request | Human/browser content or separate critic context; no established automatic report/log-to-method update. |

Evidence and record identities for these rows are in the coverage inventory and declarations/annotations. These are wired or afforded routes, not observed activation. The task-frame analogy applies to nested query and separate deck critic calls, but not to every skill: chat skill bodies are copied into the same foreground context. Files outside a frame remain tool-reachable; they are not live references whose reachability the model window can track. Provider-managed caching/compaction remains outside this evidence boundary.

## Integration issues

1. **Correction to save/catalog wording:** [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query) and the runtime account associate save-enabled query with exploration/catalog retention. Direct `openkb/cli.py` `save_exploration` and actual CLI `query` save branch write an exploration without an index update. Schema says every page is cataloged, but executable branches do not establish that for explorations. [MEM-OBJ-explorations](#mem-obj-explorations), [MEM-OBJ-index](#mem-obj-index). Consequence: retain save and explicit later-read affordance; do not assert guaranteed catalog discovery. The helper docstring claims CLI/REST sharing, but CLI duplicates separate code. Its uniqueness/escaping/lock behavior must not be extended to actual CLI save.
2. **Qualification of withdrawal:** [RT-RTE-wiki-maintain](runtime.md#rt-rte-wiki-maintain) describes source-contribution cleanup. Direct `_remove_doc_from_pages` demonstrates source-list and link edits/deletion, not subtraction of all source-derived factual claims from surviving multi-source bodies. Consequence: deletion is not semantic forgetting; separately retained explorations/history/skills can retain influence. This is a scope qualification, not a denial of the supplied cleanup implementation.
3. **Additional operative paths, not duplicates:** [MEM-RTE-page-edit](#mem-rte-page-edit) is page-level Workbench/API replacement/deletion, unlike supplied document maintenance; [MEM-RTE-skill-eval](#mem-rte-skill-eval) is evaluation/reload rather than skill generation; [MEM-RTE-host-read](#mem-rte-host-read) is direct host file navigation rather than internal query. Object records separate explicitly excluded metadata/source parts, generated-versus-installed packages and distinct session consumers. No possible duplicate requiring supersession was found after comparison with the supplied declarations.
4. **Unresolved activation and initial control:** no actual KB, generated skill, resumed session or host trace is supplied. Initial authorship/approval of arbitrary schema/local skills is unresolved; subsequent loading/replacement controls are known. Provider model version/weights, PageIndex internal state semantics, extraction fidelity and host execution remain outside the pin. Consequence: do not infer observed instruction compliance, trace learning benefit, hosted persistence guarantees or completeness of long-source representations. [RT-CMP-pageindex-client](runtime.md#rt-cmp-pageindex-client), [RT-OBJ-agents-md](runtime.md#rt-obj-agents-md), [RT-BAP-skill-instructions](runtime.md#rt-bap-skill-instructions).
5. **Catalog/metadata freshness:** manual body replacement retains descriptions/source lists, and document catalog entries are not refreshed like concept/entity entries. Whether a particular real KB has stale routing metadata is unobserved, but automatic metadata-body equivalence is not warranted. [MEM-RTE-page-edit](#mem-rte-page-edit), [MEM-OBJ-index](#mem-obj-index), [MEM-OBJ-page-frontmatter](#mem-obj-page-frontmatter).

## Limitations and checks

HEAD was rechecked as ff54396e575ee6feb0113b631a34caa082b441cc and `git status --short` was empty before source inspection. All new evidence is SRC-1 at that pin, including page operations, source/summary rendering, session representation, evaluator persistence and snapshots. Supplied records were read in full, including bounded continuation reads. The supplied job, member types, collection, worker rules and records contract governed this report; no outside characterization or prior analysis was consulted. No source or artifact members were modified and no target code was executed.

Uninspected support paths and excluded dependency internals are named in the inventory rather than silently treated as absent. The report establishes implemented or instructed mechanisms and selective consumer routes, not runtime quality, successful extraction, semantic erasure, prompt-injection immunity, token-budget safety or improved future capacity. Deterministic validation used the supplied worktree's command and artifact/role arguments; its pass checks form and quotations, not semantic support or acceptance.

Validation: passed. The separate validator returned exit status 0 and “Member content check passes; invocation residue not checked. This is not job acceptance or claim support.” The initial check identified an unfinished validation line and an inadvertently omitted line in the graph quotation; both were repaired without narrowing findings.
