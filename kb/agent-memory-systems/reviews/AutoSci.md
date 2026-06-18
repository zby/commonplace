---
description: "AutoSci review scoped to its OmegaWiki/SciMem subsystem: file-backed research wiki, schema/runtime contracts, skills, tools, graph, and bounded context packs"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
status: current
last-checked: "2026-06-18"
---

# AutoSci

AutoSci, from `skyllwt/AutoSci`, is a Claude Code-centered research-agent project by DAIR Lab. This review covers only the memory/wiki subsystem on `main`: OmegaWiki/SciMem-style `raw/`, `wiki/`, `runtime/`, `.claude/skills/`, and `tools/` behavior. The broader full research lifecycle claims around experiment execution, manuscript drafting, rebuttal, and paper-branch SciMem/SciFlow/SciDAG/SciEvolve behavior are outside this review; that whole harness belongs under `kb/agentic-systems/` if reviewed separately.

**Repository:** https://github.com/skyllwt/AutoSci

**Reviewed commit:** [71469e89eb1381e557661da0b90c0585c48288d7](https://github.com/skyllwt/AutoSci/commit/71469e89eb1381e557661da0b90c0585c48288d7)

**Source directory:** `related-systems/skyllwt--AutoSci`

## Core Ideas

**The stable branch is a lean wiki/runtime, not the full paper system.** The README explicitly says `main` is the stable lean version and that the full SciMem/SciFlow/SciDAG/SciEvolve paper system lives on the `paper` branch, so this review treats the implemented `main` wiki as the inspected memory system rather than importing paper-branch claims ([README.md](https://github.com/skyllwt/AutoSci/blob/71469e89eb1381e557661da0b90c0585c48288d7/README.md)).

**The wiki is a structured research memory surface.** `wiki/` is the product surface with typed entity directories for papers, concepts, topics, people, ideas, methods, experiments, summaries, foundations, outputs, plus generated graph files; `raw/` holds user-owned papers/notes/web and generated discovery/tmp handoffs ([CLAUDE.md](https://github.com/skyllwt/AutoSci/blob/71469e89eb1381e557661da0b90c0585c48288d7/CLAUDE.md), [docs/runtime-directory-structure.en.md](https://github.com/skyllwt/AutoSci/blob/71469e89eb1381e557661da0b90c0585c48288d7/docs/runtime-directory-structure.en.md)). At the reviewed commit the checked-in `wiki/` is a scaffold, not a populated memory corpus ([wiki/index.md](https://github.com/skyllwt/AutoSci/blob/71469e89eb1381e557661da0b90c0585c48288d7/wiki/index.md)).

**Runtime YAML is the memory contract.** `runtime/schema/entities.yaml`, `edges.yaml`, `xref.yaml`, and `conventions.yaml` define entity fields, lifecycle states, edge endpoints, bidirectional link obligations, slug rules, ownership zones, and generated graph locations. `runtime/loader.py` derives the Python constants consumed by both `tools/research_wiki.py` and `tools/lint.py`, so adding entity or edge types is intended to be a YAML change rather than a code-generation workflow ([runtime/CLAUDE.md](https://github.com/skyllwt/AutoSci/blob/71469e89eb1381e557661da0b90c0585c48288d7/runtime/CLAUDE.md), [runtime/loader.py](https://github.com/skyllwt/AutoSci/blob/71469e89eb1381e557661da0b90c0585c48288d7/runtime/loader.py)).

**Skills are the agent-facing write/read workflows.** `/ingest` turns a paper into wiki pages plus graph edges, `/ask` retrieves and optionally crystallizes answers, `/check` wraps structural lint, `/discover` ranks candidate papers against anchors or wiki state, `/prefill` seeds terminal foundations, and `/init` bootstraps the wiki through prepared raw inputs and parallel ingest ([.claude/skills/ingest/SKILL.md](https://github.com/skyllwt/AutoSci/blob/71469e89eb1381e557661da0b90c0585c48288d7/.claude/skills/ingest/SKILL.md), [.claude/skills/ask/SKILL.md](https://github.com/skyllwt/AutoSci/blob/71469e89eb1381e557661da0b90c0585c48288d7/.claude/skills/ask/SKILL.md), [.claude/skills/discover/SKILL.md](https://github.com/skyllwt/AutoSci/blob/71469e89eb1381e557661da0b90c0585c48288d7/.claude/skills/discover/SKILL.md)). Much of the higher-level curation is prompt-governed Claude Code behavior rather than deterministic Python.

**Context efficiency is compiled and task-scoped, but not globally enforced.** `tools/research_wiki.py compile-context` emits `wiki/graph/context_brief.md` with per-purpose budgets for methods, gaps, failed ideas, papers, experiments, edges, and stale entities; `/ask` caps full-page retrieval at 15 pages; `/ingest` caps new concepts/methods per paper and checks for similar concepts before creation ([tools/research_wiki.py](https://github.com/skyllwt/AutoSci/blob/71469e89eb1381e557661da0b90c0585c48288d7/tools/research_wiki.py), [.claude/skills/ask/SKILL.md](https://github.com/skyllwt/AutoSci/blob/71469e89eb1381e557661da0b90c0585c48288d7/.claude/skills/ask/SKILL.md), [.claude/skills/ingest/references/dedup-policy.md](https://github.com/skyllwt/AutoSci/blob/71469e89eb1381e557661da0b90c0585c48288d7/.claude/skills/ingest/references/dedup-policy.md)). The actual context load still depends on Claude Code following skill instructions.

**Trust is split between deterministic gates and prompt discipline.** Edge endpoint validation, lifecycle transitions, graph/citation consistency checks, missing required fields, broken links, and some xref fixes are implemented in Python; writer permissions are explicitly declared as a spec, not a runtime gate ([tools/lint.py](https://github.com/skyllwt/AutoSci/blob/71469e89eb1381e557661da0b90c0585c48288d7/tools/lint.py), [tools/research_wiki.py](https://github.com/skyllwt/AutoSci/blob/71469e89eb1381e557661da0b90c0585c48288d7/tools/research_wiki.py), [runtime/policy/writers.yaml](https://github.com/skyllwt/AutoSci/blob/71469e89eb1381e557661da0b90c0585c48288d7/runtime/policy/writers.yaml)). That gives the wiki stronger structure than a prompt-only notebook, but weaker write authority than a fully enforced schema/database.

## Artifact analysis

- **Storage substrate:** `files` `repo` — Retained memory is Markdown and JSON/YAML files in a git repository: `raw/` inputs, `wiki/` entity pages, `wiki/graph/*.jsonl` and generated briefs, `.checkpoints/*.json`, runtime schemas, skill instructions, and Python tools. I found no database, vector store, model weights, or service-side memory substrate in the reviewed `main` subsystem.
- **Representational form:** `prose` `symbolic` — Wiki pages, summaries, skill instructions, and generated context packs are prose; frontmatter, YAML schemas, entity kinds, lifecycle enums, edge records, checkpoints, command arguments, graph JSONL, lint issue objects, and ranking formulas are symbolic. External LLMs are used by skills, but the repository does not retain parametric state such as embeddings, adapters, or model weights.
- **Lineage:** `authored` `imported` — Runtime contracts, tools, skills, templates, and user-edited wiki pages are authored; `/ingest`, `/prefill`, `/init`, `/daily-arxiv`, and `/ask --crystallize` import or derive wiki artifacts from papers, notes, web pages, Wikipedia, Semantic Scholar, DeepXiv, Paper Copilot data, and existing wiki pages. I did not find a durable mechanism that mines session logs, tool traces, or trajectories into memory artifacts, so this review does not mark `trace-extracted`.
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` `learning` — Wiki entities advise future research work as knowledge; skills and `CLAUDE.md` files instruct Claude Code; `research_wiki.py` rejects invalid new edges and illegal lifecycle transitions; entity kinds, slugs, xref rules, topics, and writer policies route writes; `lint.py` validates structure and can fix deterministic issues; discovery and context compilation rank candidates/entities; imported and crystallized wiki pages let accumulated research memory change later recommendations and answers.

**Raw inputs and prepared sources.** `raw/papers`, `raw/notes`, and `raw/web` are user-owned source material, while `raw/discovered` and `raw/tmp` are generated handoff areas for discovered or prepared sources. These are imported source artifacts, not the normalized behavior-shaping memory surface ([CLAUDE.md](https://github.com/skyllwt/AutoSci/blob/71469e89eb1381e557661da0b90c0585c48288d7/CLAUDE.md), [.claude/skills/init/SKILL.md](https://github.com/skyllwt/AutoSci/blob/71469e89eb1381e557661da0b90c0585c48288d7/.claude/skills/init/SKILL.md)).

**Wiki entity pages.** Paper, concept, topic, method, idea, experiment, summary, people, foundation, and output pages are the central knowledge artifacts. Their prose bodies carry scientific content; frontmatter fields such as status, importance, maturity, key papers, origin gaps, linked experiments, and source papers give the tools deterministic routing and validation handles ([runtime/schema/entities.yaml](https://github.com/skyllwt/AutoSci/blob/71469e89eb1381e557661da0b90c0585c48288d7/runtime/schema/entities.yaml)).

**Graph and citation rows.** `wiki/graph/edges.jsonl` and `citations.jsonl` are derived/append-maintained symbolic access structures. `add-edge` validates edge type, endpoint shape, required confidence/evidence, symmetric canonicalization, and duplicates before writing; citation rows are separated from semantic edges ([tools/research_wiki.py](https://github.com/skyllwt/AutoSci/blob/71469e89eb1381e557661da0b90c0585c48288d7/tools/research_wiki.py), [runtime/schema/edges.yaml](https://github.com/skyllwt/AutoSci/blob/71469e89eb1381e557661da0b90c0585c48288d7/runtime/schema/edges.yaml)).

**Runtime contracts and validators.** The YAML schema files and `runtime/loader.py` are system-definition artifacts. `tools/lint.py` consumes them to detect missing fields, broken wikilinks, orphan pages, invalid enum/range values, xref asymmetry, dangling graph edges, malformed graph/citation rows, and several content-quality hints ([runtime/loader.py](https://github.com/skyllwt/AutoSci/blob/71469e89eb1381e557661da0b90c0585c48288d7/runtime/loader.py), [tools/lint.py](https://github.com/skyllwt/AutoSci/blob/71469e89eb1381e557661da0b90c0585c48288d7/tools/lint.py)).

**Skill packages.** `.claude/skills/*/SKILL.md` files are prompt-level system-definition artifacts: they tell Claude Code what to read, what to write, which tools to call, what not to mutate, and when to ask the user. Their authority depends on the host model following instructions; only the called Python tools provide hard checks.

**Compiled context and discovery checkpoints.** `context_brief.md`, `open_questions.md`, projected edges, shortlist checkpoint JSON, and `.checkpoints/init-*.json` are derived views. They are not canonical memory, but they shape future action by determining which gaps, failures, methods, papers, and recommendations get surfaced to the agent.

**Promotion path.** The common path is raw source or question answer -> wiki entity/output -> graph/index/context brief -> skill read-back. A weaker but important path is prose instruction -> YAML contract -> Python validation; however writer permissions remain declarative rather than enforced unless a specific tool implements the check.

## Comparison with Our System

AutoSci and Commonplace share a file-first premise: durable knowledge should be inspectable Markdown/YAML in a repository, with generated graph/index/context artifacts kept subordinate to source files. Both systems also separate raw/source material, library artifacts, type contracts, instructions, and validators.

The main divergence is register and boundary. AutoSci's wiki is a domain working memory for scientific research: it stores papers, concepts, ideas, experiments, and generated outputs that feed concrete research workflows. Commonplace is a methodology KB about agent-operated KBs; it treats type specs, collection contracts, review gates, and note quality as the product, not as support infrastructure for a research lifecycle.

AutoSci has a stronger workflow package around research ingestion and recommendation. `/ingest`, `/discover`, `/daily-arxiv`, `/ask`, and `/init` give an agent direct operational moves over the wiki. Commonplace has stronger artifact governance: collection-local contracts, validation across note types, review-run machinery, replacement history, and a clearer distinction between durable library artifacts and work-in-progress.

The core tradeoff is flexibility versus enforceability. AutoSci can let Claude Code synthesize pages, append links, update graph rows, and bootstrap a wiki from raw sources quickly. But many curation decisions live in skill prose and LLM judgment, and `writers.yaml` says its permissions are not runtime gates. Commonplace is slower and narrower, but its retained artifacts are more tightly tied to type contracts and deterministic validation.

### Borrowable Ideas

**Purpose-specific context budgets.** Commonplace could compile task-start packs with explicit per-section budgets, as AutoSci does for ideation, experiment, writing, review, and general use. Ready for workshop/review contexts; should stay generated and subordinate to source artifacts.

**Schema-driven edge endpoint validation.** AutoSci's `edges.yaml` plus loader helpers give a compact pattern for making graph edge semantics checkable. Ready if Commonplace adds more machine-readable relationship projections beyond Markdown links.

**Terminal foundations.** AutoSci's foundation pages are a useful anti-duplication pattern: background concepts can receive inward links without becoming active bidirectional graph participants. Needs a concrete Commonplace use case before adding another artifact class.

**Discovery as proposal, not ingestion.** `/discover` ranks and dedupes candidates but refuses to ingest them automatically. That separation is a good default for any Commonplace source-acquisition helper.

**Do not borrow prompt-only writer permissions as enforcement.** The `writers.yaml` declaration is useful documentation, but Commonplace should implement hard checks when write authority matters.

## Write side

**Write agency:** `manual` `automatic` — Humans and Claude Code can author/edit wiki pages, raw inputs, and skill-controlled outputs; tools and skills automatically initialize scaffolds, import sources, create entity pages, append graph/citation rows, rebuild context/open-question/index artifacts, write discovery/init checkpoints, log actions, and apply deterministic lint fixes.

**Curation operations:** `consolidate` `dedup` `evolve` `synthesize` — `compile-context` and `rebuild-open-questions` consolidate stored wiki content into compact derived views; `dedup-edges`, `dedup-citations`, `find-similar-concept`, and discovery's wiki filtering remove or prevent duplicate access records/candidates; `lint --fix`, lifecycle transitions, reverse-link repairs, and metadata updates evolve existing artifacts; `/ask --crystallize` and prompt-governed research skills can synthesize new output/concept/idea/method artifacts from existing wiki evidence. The deterministic core is strongest for graph/index/schema maintenance; semantic synthesis remains LLM-mediated.

The automatic write path is not trace-derived learning in this review's sense. It imports scientific sources and compiles derived access structures, but I did not find a loop that consumes agent transcripts, session logs, tool traces, or repeated trajectories to create durable rules, wiki pages, validators, rankers, or weights.

## Read-back

**Read-back:** `both` — Pull read-back comes from `/ask`, `find`, `neighbors`, full-page reads, graph traversal, and discovery queries; push read-back occurs when skill workflows load `context_brief.md`, `open_questions.md`, selected wiki pages, or purpose-compiled context into the agent's task context before the next answer/action.

**Read-back signal:** `coarse` `identifier` `inferred / lexical` — Coarse push appears in skill-start loading of the generated context pack and open-question map. Identifier targeting uses entity kinds, slugs, frontmatter status/importance/maturity/linked fields, graph endpoints, and purpose labels. Lexical/content inference appears in `/ask` keyword matching, `find-similar-concept` token overlap, and `discover.py`'s BM25-style wiki relevance corpus for venue-mode ranking.

**Faithfulness tested:** `no` — The reviewed code validates files, edges, field values, lifecycle transitions, and ranking computations, but I found no with/without-memory ablation or post-action audit proving that read-back from the wiki changed Claude Code behavior correctly.

Selection and scope are partly bounded. `compile-context` has per-purpose character budgets and section allocations; `/ask` reads at most 15 pages; graph traversal has a depth parameter; discovery applies shortlist limits and wiki dedup filters ([tools/research_wiki.py](https://github.com/skyllwt/AutoSci/blob/71469e89eb1381e557661da0b90c0585c48288d7/tools/research_wiki.py), [.claude/skills/ask/SKILL.md](https://github.com/skyllwt/AutoSci/blob/71469e89eb1381e557661da0b90c0585c48288d7/.claude/skills/ask/SKILL.md), [tools/discover.py](https://github.com/skyllwt/AutoSci/blob/71469e89eb1381e557661da0b90c0585c48288d7/tools/discover.py)). Effective context dilution and recall quality are not knowable from static code alone.

Authority at consumption varies. A paper page or concept page is advisory knowledge; a skill instruction is prompt-level instruction; a lint or transition failure is a hard tool-level gate; a discovery score or context-pack ordering is ranking authority. The same retained wiki material can therefore be soft evidence in `/ask`, a candidate generator in `/discover`, or an operational dependency inside a research-writing skill.

Other consumers are first-class. Humans can inspect and edit the same Markdown/YAML/JSON files, browse the web/Obsidian graph views, and use git history for rollback. That adoption affordance is stronger than database-backed memory but weaker than Commonplace's fully specified review artifact lifecycle.

## Curiosity Pass

The most important implementation nuance is that `writers.yaml` is deliberately not enforced. It is still useful as a behavioral contract for skills, but a reader should not infer access control from its field/edge ownership lists.

AutoSci's "memory-centric" README framing is accurate for the subsystem, but it is not the same claim as "implemented autonomous scientific lifecycle." The `main` branch memory substrate is inspectable; whole-system research autonomy needs a separate agentic-system review.

The checked-in wiki is empty scaffolding. The architecture is visible in tools, schemas, and skills, but quality of a populated AutoSci memory cannot be evaluated from this repository snapshot.

The distinction between canonical pages and generated graph/context files is healthy. `wiki/graph/` is explicitly derived and should be modified through `research_wiki.py`, which keeps the storage story from drifting into opaque generated state.

Discovery is a read-back mechanism as much as a recommendation feature. Venue mode uses the existing wiki corpus to personalize what the user should read next, so stored memory changes acquisition, not only answer generation.

## What to Watch

- Whether `writers.yaml` becomes runtime enforcement; that would materially change the authority of skill-specific write permissions.
- Whether `main` imports more of the paper-branch SciMem/SciFlow/SciDAG/SciEvolve implementation; the current review should not be treated as coverage of those claims.
- Whether the wiki gains embeddings, vector search, or persistent learned rankers; that would add a parametric representational form and change read-back precision questions.
- Whether AutoSci adds session-log or tool-trace mining; that would make the system trace-derived and should add the trace-derived section to this review.
- Whether populated example wikis or evaluations appear; they would let reviewers assess retrieval quality, duplicate control, and faithfulness rather than only structure.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes AutoSci's retained wiki files from the skill/tool paths that actually load them into Claude Code context.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies to the split between raw inputs, wiki pages, graph JSONL, schemas, skill prompts, validators, and generated context packs.
- [Storage substrate](../../notes/definitions/storage-substrate.md) - frames AutoSci's repo/files substrate and lack of inspected database/vector/model-weight memory.
- [Representational form](../../notes/definitions/representational-form.md) - supports separating prose wiki content from symbolic schemas, graph rows, and command contracts.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies runtime schemas, skill instructions, validators, and tool commands as behavior-shaping artifacts.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies paper/concept/idea/method/wiki output pages as advisory retained research memory.
- [Symbolic context engineering is bounded by symbol availability](../../notes/symbolic-context-engineering-is-bounded-by-symbol-availability.md) - explains why AutoSci's slugs, entity kinds, status fields, and graph edges matter for targeted read-back.
