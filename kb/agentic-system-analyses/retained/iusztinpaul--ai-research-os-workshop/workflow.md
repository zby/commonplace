---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "AI Research OS Workshop workflow: explicit web-source append through delegated wiki construction, catalog delivery and bounded failure handling."
run-id: AAS-2026-10-12-ai-research-os-workshop-1a93869f8e7f-01
reviewed-boundary: dc6660555266239cd36483cf51b5ab39febacf02
---

# AI Research OS Workshop workflow report

## Workflow account

### Selected workflow and evidence

The representative workflow is an explicit request to add generic web URLs to an existing v4 research directory without discovery. It exercises the system's central source-to-wiki-to-catalog chain without combining unrelated entry skills. One successful source is enough to write a source page; several newly processed sources can enable entity/concept propagation. This is the same route as [RT-RTE-append-ingest](runtime.md#rt-rte-append-ingest), with workflow-specific handoff findings below, not a new route identity.

The evidence establishes an instructed multi-step workflow and narrower executable catalog behavior, not successful execution. The host supplies inference, Agent dispatch and tools; the plugin orchestrator requests effects and owns progression. No supplied trace establishes completed delegation, trustworthy synthesis or useful later answers. SRC-1: `plugins/ai-research-os/skills/research/SKILL.md`; `plugins/ai-research-os/skills/research/scripts/build_index_yaml.py`; [RT-CMP-host-model](runtime.md#rt-cmp-host-model).

Additional inspection at SRC-1's frozen commit covers research-driver routing, web seeds and Steps 6–8; complete builder, source-writer and entity/concept-writer prompts; the summary-writer input/read-budget section; and YAML-builder normalization, source loading and document construction. Prompt passages supply doctrine/design; Python passages supply implementation. Other origins, discovery rounds and downstream maintenance/export are not independently traced here.

### 1. Admit the request before dispatch

The user supplies the topic, URLs and explicit append intent. The orchestrator locates the directory, shows the planned inputs and writes, and proceeds unless confirmation was requested. A dry-run stops at the plan. Ambiguous source drops instead ask whether to ingest or discover. The plan's confirmation language also mentions estimates above five minutes; its append-specific proceed rule leaves actual reconciliation to the interpreting host/model. These are instruction gates rather than intercepted tool permissions. SRC-1: `plugins/ai-research-os/skills/research/SKILL.md`.

The preconditions inspect layout and canonical YAML. An older layout requires migration before ingest. If YAML is missing while the wiki and Markdown index exist, mutation is blocked until YAML is restored; read-only query fallback remains available. Existing `original_path` identities reject already-ingested sources with a skip message. This is a source-identity gate, not a factual-validity assessment. The user authorizes the route, not each later generated claim. [RT-RTE-append-ingest](runtime.md#rt-rte-append-ingest) and [RT-CLM-index-contract](runtime.md#rt-clm-index-contract) retain the prior-source and invocation constraints. SRC-1: `plugins/ai-research-os/skills/research/SKILL.md`.

### 2. Acquire text and hand off raw persistence

For generic web URLs, the orchestrator requests curl plus HTML stripping, switching to WebFetch after an error or suspiciously short output. It records URL identity, origin and fetched text in seed metadata with score 1.0. This fixed score means user-selected relevance, not verified content quality. Append skips the discovery stages. SRC-1: `plugins/ai-research-os/skills/research/SKILL.md`.

The builder receives its role instructions, seed/results JSON paths, target directory, topic, input summary, rounds, skill path and `raw_only` mode. It checks JSON parsing, transfers source content through shell operations, writes raw files and URI-augmented temporary JSON, and returns successful entries and skipped reasons. The orchestrator receives compact metadata rather than raw bodies at this stage. It then requests asset localization and collects asset manifests. [RT-RTE-append-ingest](runtime.md#rt-rte-append-ingest); SRC-1: `plugins/ai-research-os/skills/research/agents/builder.md`, `plugins/ai-research-os/skills/research/SKILL.md`.

### 3. Delegate semantic construction through selected source pages

Each successful raw entry triggers one source writer. Its handoff supplies raw path, source metadata, research topic/intent, existing entity/concept slugs, assets and one output path. It reads the raw source, writes a source page and returns referenced slugs, candidate new slugs and claim/quote counts. Writers can run in parallel because each is assigned a different page. The orchestrator collects their JSON before deciding propagation. Source interpretation is therefore delegated; the orchestrator's next-step judgment uses reports and metadata, not a fresh raw-text audit. SRC-1: `plugins/ai-research-os/skills/research/SKILL.md`, `plugins/ai-research-os/skills/research/agents/source_writer.md`.

> A single markdown file at `output_path` with YAML frontmatter and a structured body. **No other side effects** — do not modify the raw file, do not touch index.yaml, do not write to other wiki pages.
> --- `plugins/ai-research-os/skills/research/agents/source_writer.md`

The orchestrator aggregates slug mentions across the returned source-writer outputs. Only slugs reaching two distinct sources trigger entity/concept writers. An append ordinarily skips the discussion checkpoint; when explicitly requested, user redirects change propagation after source pages have already been written. The checkpoint does not roll those pages back. Each higher-level writer receives only assigned source-page paths, canonical naming, topic/intent, prior page path and output path. It reads prior content for preservation, then merges supported claims and exposes tensions/questions. SRC-1: `plugins/ai-research-os/skills/research/SKILL.md`, `plugins/ai-research-os/skills/research/agents/wiki_page_writer.md`.

> You aggregate from per-source wiki pages. **You never read raw files** — every claim you record must already exist on a source page; if it isn't there, it isn't in the wiki yet.
> --- `plugins/ai-research-os/skills/research/agents/wiki_page_writer.md`

This boundary makes source-page omissions consequential: higher-level synthesis cannot recover an omitted raw claim by its prescribed input path. Existing slug lists support name reuse, but Step 6.4 does not explicitly gather all historical source pages for each slug; its stated aggregation uses current source-writer outputs. Retaining an existing entity page is therefore not evidence of an exhaustive re-review of its historical backing. SRC-1: `plugins/ai-research-os/skills/research/SKILL.md`, `plugins/ai-research-os/skills/research/agents/wiki_page_writer.md`.

### 4. Acceptance is distributed, not a final independent quality gate

Builder JSON parsing checks input form. Successful raw entries select source-writer dispatch; mention counts select higher-level dispatch. Entity/concept writers compute substantive source counts and confidence, preserve KEEP blocks and can return a noop for unchanged bodies. A low substantive count does not force rejection:

> - `low` — `source_count == 1` (this shouldn't happen in normal flow — entity/concept pages are gated on ≥2 mentions; if it does, the orchestrator made an error and you should still write the page but flag low confidence)
> --- `plugins/ai-research-os/skills/research/agents/wiki_page_writer.md`

Citation and source-faithfulness requirements guide the writers; they are not an inspected independent claim verifier. No expected-answer oracle is supplied. The selected mode is an open user request, not an experiment. The driver collects writer reports and aggregates tensions as a lint flag, but Steps 6–8 end with a suggestion to run lint, not a mandatory lint acceptance before delivery. [RT-RTE-lint-maintenance](runtime.md#rt-rte-lint-maintenance) describes that separate route. SRC-1: `plugins/ai-research-os/skills/research/SKILL.md`.

Two summary writers next produce overview and synthesis in parallel. They receive directory/topic/intent and prior page/output paths, discover the wiki themselves and may fully read only five selected pages, alongside metadata and rolling criticism/question files. This bounded context constrains what the final thesis can assess. Their first prescribed read is canonical YAML, yet catalog refresh happens later: append supplies old catalog metadata, and init can supply no catalog. This seam is already retained in [RT-RTE-append-ingest](runtime.md#rt-rte-append-ingest). The thesis/theory properties assessed there are not strengthened by this source-only workflow trace. SRC-1: `plugins/ai-research-os/skills/research/agents/wiki_summary_writer.md`, `plugins/ai-research-os/skills/research/SKILL.md`.

### 5. Join persistent artifacts and deliver

After wiki writing, the orchestrator appends surfaced questions, augments source metadata with source-page pointers/assets, snapshots prior YAML, runs the YAML builder with prior-index carry-forward, then regenerates Markdown navigation. The helper owns normalization and file generation; it does not approve synthesized claims or check that advertised raw pointers resolve. The temporary prior-index copy prevents read/write aliasing, not a multi-file rollback protocol. [RT-RTE-index-build](runtime.md#rt-rte-index-build); SRC-1: `plugins/ai-research-os/skills/research/SKILL.md`, `plugins/ai-research-os/skills/research/scripts/build_index_yaml.py`.

The driver then appends an ingest log, cleans intermediate JSON after successful construction and reports mode, counts, skipped items, directory path and usage suggestions. Delivery means the instructed persistent raw/wiki/catalog/navigation artifacts plus an operator-facing result, not a release accepted by a separate reviewer. Subsequent query is a separate invocation that selects retained content; it is not demonstrated here. [RT-RTE-query-answer](runtime.md#rt-rte-query-answer); SRC-1: `plugins/ai-research-os/skills/research/SKILL.md`.

### Failure and recovery boundaries

The inspected web failure path is per-source degradation: orchestrator fetch fallback, builder retry when fetched text is missing, then a skipped report if every fetch fails. Other successful sources can continue. Image failures are non-fatal and leave the original URL. The orchestrator owns continuing dispatch and reporting skips; the builder owns local acquisition attempts. This does not establish successful fallback in a deployed host. SRC-1: `plugins/ai-research-os/skills/research/SKILL.md`, `plugins/ai-research-os/skills/research/agents/builder.md`.

> If `fetched_markdown` is empty/missing (e.g. the seed was added without pre-fetching), fetch it now with `curl` and strip the HTML to `<research_dir>/raw/web-<slug>.md` (canonical recipe in `SKILL.md` Step 1, point 3), falling back to WebFetch if `curl` fails or returns < ~500 chars. Set `uri_highlights: null`, `uri_full: "raw/web-<slug>.md"`. If every fetch fails, record the source as skipped.
> --- `plugins/ai-research-os/skills/research/agents/builder.md`

Neither reporting a source as skipped nor completing a helper automatically closes the catalog handoff. The annotations below identify the mismatches. Interrupted writes can leave partial raw/wiki state; builder rerun overwrite guidance conflicts with the explicit re-ingest consent policy in [RT-CLM-raw-policy](runtime.md#rt-clm-raw-policy). The selected recipe supports local retries, noops and reporting, not an inspected transaction restoring all artifacts or a retry protocol for failed semantic workers. SRC-1: `plugins/ai-research-os/skills/research/agents/builder.md`, `plugins/ai-research-os/skills/research/SKILL.md`.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

none declared in this member

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-append-ingest](runtime.md#rt-rte-append-ingest)

Workflow-specific handoff limit: Step 6's expected `raw_files` entries contain `raw_path`, while the builder's actual return template contains `uri_full` and `uri_highlights` rather than `raw_path`. Step 6.3 requires an absolute raw path. An orchestrator can derive it from directory plus relative URI, but the literal output schema does not supply the declared input directly. No observed execution establishes that repair. SRC-1: `plugins/ai-research-os/skills/research/SKILL.md`, `plugins/ai-research-os/skills/research/agents/builder.md`.

> `raw_files` is a list of `{source_idx, raw_path, original_path, slug, origin}` entries — one per successful source. You'll feed this to Step 6.2 (asset processing) and Step 6.3 (source-page writing). `skipped_details` (truncated to 10) lists sources that fetched no content.
> --- `plugins/ai-research-os/skills/research/SKILL.md`

> "uri_full": "raw/<slug>.md",
> "uri_highlights": "raw/<slug>-key-highlights.md or null"
> --- `plugins/ai-research-os/skills/research/agents/builder.md`

#### On [RT-RTE-index-build](runtime.md#rt-rte-index-build)

Workflow-specific failure propagation: the driver augments original seed/result arrays, whereas the builder returns URI-enriched files and separate skipped details. The supplied runtime already retains this URI seam. Additionally, the inspected augmentation maps over all original seeds, and `load_sources` normalizes every seed without testing fetch success or file existence. A skipped seed can consequently remain a score-1.0 catalog row unless the orchestrator removes it upstream; no explicit skipped-row filtering is prescribed in the selected augmentation recipe. This is an afforded failure case, not an observed defective catalog. SRC-1: `plugins/ai-research-os/skills/research/SKILL.md`, `plugins/ai-research-os/skills/research/scripts/build_index_yaml.py`.

> seed_rows = [normalize_source(s) for s in seeds]
> --- `plugins/ai-research-os/skills/research/scripts/build_index_yaml.py`

The account therefore distinguishes acquisition acceptance (a successful file reported for writer dispatch), catalog admission (supplied rows projected to YAML) and operator delivery (counts, paths and skips). These checks have different predicates; none supplies end-to-end factual or pointer-validity verification.
