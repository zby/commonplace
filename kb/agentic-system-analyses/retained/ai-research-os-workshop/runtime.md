---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "AI Research OS Workshop runtime baseline: host-mediated research routing, wiki admission, helper enforcement and downstream consumption."
run-id: AAS-2026-10-12-ai-research-os-workshop-1a93869f8e7f-01
reviewed-boundary: dc6660555266239cd36483cf51b5ab39febacf02
---

# AI Research OS Workshop runtime report

## Runtime account

### What owns consequential work

This target ships a research plugin, not the enclosing inference/tool runtime. The marketplace points to `plugins/ai-research-os`; its manifest declares version 0.1.0. Four user-invocable skills route research, lint, distill and rendering. The host supplies the model, Agent dispatch, Read/Write/Bash tools and any WebFetch fallback. The source-native work is creating and consulting a topic-local catalog and synthesized wiki, then maintaining or exporting it. SRC-1: `.claude-plugin/marketplace.json`, `plugins/ai-research-os/.claude-plugin/plugin.json`, `plugins/ai-research-os/skills/research/SKILL.md`, `plugins/ai-research-os/skills/research-lint/SKILL.md`, `plugins/ai-research-os/skills/research-distill/SKILL.md`, `plugins/ai-research-os/skills/research-render/SKILL.md`.

The model reads shipped natural-language orchestration instructions, makes routing and content judgments, and asks the host to execute effects. Python helpers have fixed symbolic consumers and implement narrower transformations. Neither a prompt's imperative nor an executable helper proves that the enclosing model follows the whole workflow. The report distinguishes those surfaces through [RT-CMP-host-model](#rt-cmp-host-model), [RT-CMP-notebooklm-model](#rt-cmp-notebooklm-model), [RT-OBJ-skill-instructions](#rt-obj-skill-instructions) and [RT-OBJ-python-helpers](#rt-obj-python-helpers).

> You are a research orchestrator.
> --- `plugins/ai-research-os/skills/research/SKILL.md`

No supplied source has an observed-run or causal-experiment layer. Everything below is source inspection at the frozen commit: executable helpers establish implementation; prompts establish requested protocols and afforded model-mediated workflows. Successful dispatch, completed writes, factual quality, activation of retained content and latency savings remain unobserved. Examples are not used as execution verification.

### Ordinary invocation: append a web source, then ask about it

The ordinary trace selected here is an explicit “add this URL” request against an existing v4 research directory. The user is the initiating principal. The orchestrator locates the directory by explicit path, topic slug or semantic match against catalogs, chooses append rather than discovery, shows a plan, and normally proceeds without another approval. Ambiguity defaults to query; a source drop without a discovery choice requires a gate. Existing `index.yaml` supplies the dedup identity set and original creation timestamp. Missing YAML with an extant wiki blocks mutation but permits query fallback. These are prompt controls, not tool ACLs. SRC-1: `plugins/ai-research-os/skills/research/SKILL.md` Step 0.

The orchestrator extracts topic, themes, intent and seed identities. For a web URL it requests curl plus a Python HTML stripper, falling back to WebFetch for errors or very short stripped text. The fetched content enters `seeds.json` with URL identity and seed score 1.0; empty discovery results bypass discovery rounds. The builder receives JSON paths, target directory and raw-only instructions, writes raw content using shell operations, returns a small source/URI summary and writes augmented JSON. The asset helper may download remote images and rewrite the raw copy's references. A source writer reads one raw file, writes one source page and returns entity/concept suggestions. Qualifying slugs trigger entity/concept writers, followed by overview and synthesis writers, question aggregation, catalog generation, navigation generation, a log append, scratch cleanup and an operator result. The next-step owner is always the host-mediated orchestrator, except for the explicitly delegated bounded writer operation. Coordination is path-and-JSON based, with instructions to wait for workers and parallelize disjoint output paths. SRC-1: `plugins/ai-research-os/skills/research/SKILL.md` Steps 1 and 6–8; `plugins/ai-research-os/skills/research/agents/builder.md`; `plugins/ai-research-os/skills/research/agents/source_writer.md`.

The implementation does not independently close all these handoffs. Step 6.7 augments the original discovery/seeds files with source-page pointers and assets; the builder says the orchestrator instead picks up its `*-with-uris.json` files. Unless the orchestrator also carries the raw URIs into that augmentation, the YAML builder merely projects missing fields to null. Likewise overview/synthesis writers are instructed to read `index.yaml` before Step 6.7 creates or refreshes it: init can have no catalog yet and append can supply old metadata. Those are source-level workflow seams, not observed failures. [RT-RTE-append-ingest](#rt-rte-append-ingest) and [RT-RTE-index-build](#rt-rte-index-build) retain the admission and executable transformation separately. SRC-1: `plugins/ai-research-os/skills/research/SKILL.md` Steps 6.5 and 6.7; `plugins/ai-research-os/skills/research/agents/builder.md` Steps 3–4; `plugins/ai-research-os/skills/research/agents/wiki_summary_writer.md`; `plugins/ai-research-os/skills/research/scripts/build_index_yaml.py`.

A later question begins a fresh host invocation. The query driver loads the canonical catalog, selects summaries using the request, tags, scores and origin-specific filters, then optionally follows source-page, highlight, full-text or wiki pointers. It returns a cited answer, optionally persists answer-derived content and a question pointer, regenerates navigation and logs the interaction. This is requested later read-back of retained artifacts, not a demonstrated activation trace. [RT-RTE-query-answer](#rt-rte-query-answer) records the material save-back conflict rather than treating “read-only” as a blanket guarantee. SRC-1: `plugins/ai-research-os/skills/research/SKILL.md` Query path.

### Material alternate paths

- **Init:** creates a topic directory, then uses the append or explicit deep pipeline. It is not a distinct independent runtime. Its missing prior catalog makes the summary-writer ordering seam material. [RT-RTE-append-ingest](#rt-rte-append-ingest).
- **Deep:** preset-bounded discovery queries Obsidian, both Readwise library/feed and every available non-empty NotebookLM notebook. Researcher subagents select relevant hits and cap at 15 unique findings per query. Deterministic dedup chooses the longest summary per `original_path`; the gap analyzer uses compact metadata to propose next-round queries. Optional user discussion redirects propagation before entity/concept writers. [RT-RTE-deep-discovery](#rt-rte-deep-discovery).
- **GitHub seed:** parses requested paths, refreshes a sibling clone cache, delegates module specs before architecture, and registers one seed per repository commit. Downstream readers follow architecture links rather than individual catalog rows. This path exposes a conflict between the builder's copy command and its declared pointer; it also bypasses assumptions that every source has retained raw text. [RT-RTE-github-ingest](#rt-rte-github-ingest).
- **Maintenance:** user-triggered lint runs mechanical checks and bounded model checks; model checks append contradictions/open questions while stale-claim repair remains a user decision. The model judge is not an answer oracle. [RT-RTE-lint-maintenance](#rt-rte-lint-maintenance).
- **Consumption/export:** distill matches a user content corpus against the catalog and source layers, exporting a research appendix outside the research directory. Render delegates selected wiki pages to format-specific writers and retains outputs inside the wiki. Chart rendering crosses from model-written content into executed Python. [RT-RTE-distill-export](#rt-rte-distill-export), [RT-RTE-render-output](#rt-rte-render-output).

### Guarantees and forcing cases

Four source-supported forcing cases bound the account. They are inspections, not executions.

**1. Query save-back challenges “read-only.”** Query opening rules forbid writes to entity/concept/comparison pages, but Q.5 instructs enrichment of those pages or a repo topic document. The authoritative conventions' side-effect table lists only question-page addition for saved query, plus count updates. Thus the higher-priority contract restricts the literal Q.5 recipe; a host/model must reconcile it rather than mechanically executing the whole recipe. A truthful guarantee is a policy for bounded writes, not an invariant that query never writes. The fallback with missing YAML is explicitly stricter: no saves, index regeneration or log append. [RT-CLM-query-safety](#rt-clm-query-safety). SRC-1: `plugins/ai-research-os/skills/research/SKILL.md` Q.2 and Q.5; `plugins/ai-research-os/skills/research/CONVENTIONS.md`.

**2. Asset rewriting and builder overwrites challenge immutable raw.** Conventions explicitly permit ingest-time image-reference rewriting, so “never edited” cannot mean byte preservation from initial fetch. Separately the builder says to overwrite partial existing files without prompting, while conventions require explicit consent for re-ingesting existing sources. The orchestrator dedup gate is the intended protection; direct builder calls and helper execution do not enforce it. Scope raw immutability to the intended post-ingest policy, with initialization transformation and conflicting overwrite guidance stated. [RT-CLM-raw-policy](#rt-clm-raw-policy). SRC-1: `plugins/ai-research-os/skills/research/CONVENTIONS.md`; `plugins/ai-research-os/skills/research/agents/builder.md`; `plugins/ai-research-os/skills/research/scripts/download_assets.py`.

**3. Direct catalog calls challenge append-preservation and dedup guarantees.** `--existing-index` controls carry-forward; omit it and only current seeds/results survive. The script forces every seed score to 1.0 and removes rest entries matching seed paths. It does not deduplicate duplicate seeds or duplicate ranked results among themselves. The earlier dedup helper drops findings with no identity and deduplicates valid ones; prose also asks for cross-origin URL dedup, which that helper does not implement. Preservation and complete uniqueness therefore depend on upstream admission and correct invocation, not just calling the final builder. [RT-CLM-index-contract](#rt-clm-index-contract). SRC-1: `plugins/ai-research-os/skills/research/scripts/build_index_yaml.py`; `plugins/ai-research-os/skills/research/scripts/dedup_findings.py`; `plugins/ai-research-os/skills/research/SKILL.md` Important notes.

**4. GitHub copy and cache refresh challenge reproducible local delivery.** The builder creates `wiki/repos/<repo-slug>` but its copy recipe targets `raw/<repo-slug>`; it advertises a `wiki/repos/.../ARCHITECTURE.md` pointer and conventions prohibit a GitHub raw entry. This is a conflicting recipe, not evidence that the pointer resolves. Cache identity is owner/repo, not branch/commit; subsequent refreshes fetch, checkout and hard-reset the shared clone. Commit metadata pins citations but does not lock a writer's read view against another refresh. Also render's idempotency gate compares prompt and source-path list, not changed source bodies: an updated wiki with the same prompt/paths can request a noop, preserving an older embedded chart snapshot. [RT-RTE-github-ingest](#rt-rte-github-ingest), [RT-RTE-render-output](#rt-rte-render-output). SRC-1: `plugins/ai-research-os/skills/research/agents/builder.md`; `plugins/ai-research-os/skills/research/scripts/github_clone.py`; `plugins/ai-research-os/skills/research-render/SKILL.md`; `plugins/ai-research-os/skills/research-render/agents/chart_writer.md`.

The declared guarantee owners are the skill author and the interpreting orchestrator; enforcement points are prompt gates except for the narrow helper rules. Covered paths and alternates are explicit in the claim records below. Required external contracts include host compliance with instructions, successful tool execution, usable authenticated source CLIs and normal filesystem behavior. No deployed isolation envelope or current tool grant set is supplied. The capability surface requests shell, file reads/writes, Agent dispatch, source CLI calls and generated-script execution. The plugin manifests inspected here declare discovery metadata rather than per-operation grants. Direct helper CLI calls, user file edits, delegated shell access and chart execution materially exceed a prompt's nominal file-write scope if the host permits them. This does not establish that any particular deployment grants those capabilities. SRC-1: `plugins/ai-research-os/.claude-plugin/plugin.json`; `plugins/ai-research-os/skills/research/SKILL.md`; `plugins/ai-research-os/skills/research-render/SKILL.md`.

### Change admission and coverage limits

User requests authorize routes, not individual claims. Model writers propose and physically write wiki knowledge under static instructions; the discussion checkpoint can redirect selected propagation, and `<!-- KEEP -->` blocks request preservation of deliberate human overrides. Lint appends criticism without rewriting challenged source/entity/concept pages. Render admits generated Python as an executable artifact when the orchestrator runs it; its specified purpose is chart output, not runtime self-modification. Extending the researcher prompt with new search steps is a stated development affordance, not an automatically admitted capability update. No inspected route revises the plugin's own skill source or model weights. This bounded account makes no system-wide absence claim about host extensions or provider updates. SRC-1: `plugins/ai-research-os/skills/research/SKILL.md` Extensibility and Step 6.3.5; `plugins/ai-research-os/skills/research/agents/wiki_page_writer.md`; `plugins/ai-research-os/skills/research-render/agents/chart_writer.md`.

Additional coverage under SRC-1: this member reads the complete research driver, conventions, researcher, gap analyzer, builder, source writer, entity/concept writer, overview/synthesis writer and GitHub-spec writer; complete dedup, YAML/Markdown builders, asset downloader and GitHub clone helper; complete lint driver/judge and broken-link checker; complete distill/render drivers and chart writer; complete manifests. Executable helper passages supply implementation evidence; prompt passages supply doctrine/design. Remaining extraction/target-parser details, the other mechanical lint implementations, comparison writer dispatch/body, other format writer bodies and source-CLI references are not fully inspected here. They prevent complete claims about extraction fidelity, comparison production, all checker predicates, all render shapes and external-service behavior, but not the bounded driver trace. No unavailable tracked file is claimed. The broken-link helper delegates page enumeration and resolution to `_lintlib.py`, which is not inspected here; its exact resolution semantics therefore remain uninspected. SRC-1: `plugins/ai-research-os/skills/research-lint/scripts/lint_broken_links.py`.

## Shared records

### Components

#### RT-CMP-host-model
Label: Host research model

The model behind the host orchestrator and dispatched researcher/writer/judge roles is a distributed-parametric component. Its weights/provider state are outside this repository's storage substrate; prompts and output files are not those parameters. Exact model version is not pinned by the inspected skill/agent dispatch instructions. Parameter changes during operation are uninspected because the provider/host implementation is outside SRC-1. Whether a mutable endpoint resolves to another model is likewise uninspected; no stable endpoint identity is supplied. Static role text does not establish weight fixity. SRC-1: `plugins/ai-research-os/skills/research/SKILL.md` Steps 4 and 6; `plugins/ai-research-os/skills/research-lint/SKILL.md` Step 4.

> For each round, spawn **one Research Subagent per query** in parallel using the Agent tool.
> --- `plugins/ai-research-os/skills/research/SKILL.md`

#### RT-CMP-notebooklm-model
Label: NotebookLM query and description model

Discovery can call an external model-mediated NotebookLM query/description service through `nlm`. Numerical parameters and any provider retained state have an opaque external storage substrate. Its exact model version is not pinned; parameter changes and mutable endpoint resolution are uninspected because the service implementation is outside the source boundary. Its returned answer identifies source candidates, not a reference answer for testing the plugin. SRC-1: `plugins/ai-research-os/skills/research/agents/researcher.md` Step 3.

> The response is an AI-synthesized answer that cites specific sources from the notebook. Parse the response to identify which sources were referenced.
> --- `plugins/ai-research-os/skills/research/agents/researcher.md`

### Operative objects

#### RT-OBJ-skill-instructions
Label: Shipped skill and agent instructions

Source-native `SKILL.md`, `CONVENTIONS.md` and `agents/*.md` files are natural-language instructions stored as plugin Markdown. Paths and JSON examples have symbolic parts, but the host model interprets the procedural/citation/write-scope content. Conventions declare precedence over skill text. These static shipped instructions are not accumulated read-back through use. They supply routing, thresholds, read budgets, preservation requests and response formats; [RT-BAP-skill-guidance](#rt-bap-skill-guidance) identifies their behavioral-authority channel. SRC-1: `plugins/ai-research-os/skills/research/CONVENTIONS.md`; `plugins/ai-research-os/skills/research/SKILL.md`.

> If you're operating on a research dir, this file is authoritative — when a SKILL.md and CONVENTIONS.md disagree, CONVENTIONS.md wins.
> --- `plugins/ai-research-os/skills/research/CONVENTIONS.md`

#### RT-OBJ-python-helpers
Label: Python helper programs

The dedup, index builders, clone and asset helpers are symbolic Python source stored in the plugin tree. Their consumers are Python processes invoked by shell/uv, not a model interpreting prose. They implement fixed transformations but do not own the full model loop or admission policy. This object denotes shipped tooling, not generated chart scripts and not memory content. SRC-1: `plugins/ai-research-os/skills/research/scripts/dedup_findings.py`; `plugins/ai-research-os/skills/research/scripts/build_index_yaml.py`; `plugins/ai-research-os/skills/research/scripts/build_index_md.py`; `plugins/ai-research-os/skills/research/scripts/github_clone.py`; `plugins/ai-research-os/skills/research/scripts/download_assets.py`.

> Path(args.output).write_text(yaml.safe_dump(doc, sort_keys=False, allow_unicode=True, width=1000))
> --- `plugins/ai-research-os/skills/research/scripts/build_index_yaml.py`

### Routes

#### RT-RTE-append-ingest
Label: Append or initialize research knowledge

Endpoints: explicit user seed request → host orchestrator → builder/source/entity/concept/summary agents and helpers → raw/wiki/catalog/log → user result. The host model chooses mode and output directory, seeds identities and content, delegates bounded outputs and joins them before catalog generation. Init creates the layout and has no prior index. Append reads prior YAML and skips known `original_path` values. Source pages are built from raw; higher-level writers read scoped wiki content. Mention threshold is at least two distinct sources; writers distinguish substantive source count from passing links. SRC-1: `plugins/ai-research-os/skills/research/SKILL.md` Steps 0, 1 and 6–8; `plugins/ai-research-os/skills/research/agents/source_writer.md`; `plugins/ai-research-os/skills/research/agents/wiki_page_writer.md`.

- Immediate return: Builder and writers return small JSON summaries; orchestrator presents source/wiki counts, skips, location and suggested next operations.
- Later read-back: Retained catalog, raw/source pages and synthesized wiki are requested by later query, lint, distill, render and ingest invocations.
- Delegated visibility: Builder sees input JSON and uses shell content transfer; source writer sees one raw source and metadata; entity/concept writers receive assigned source pages; summary writers discover wiki state with a five-full-read budget.
- Selection predicate: User seeds score 1.0; known identities are skipped by the orchestrator; entity/concept propagation uses mention counts and optional redirects.
- Invalidation or expiry: No TTL is specified; later ingest rewrites mutable pages, requests preservation of KEEP blocks and updates timestamps. Source writer can overwrite a prior page.
- Activation or effect: Requested file creation/update and later model consumption; asset helper's rewriting is implemented. Activation of retained content in actual behavior is unobserved.
- Evidence limits: Prompt orchestration is not a retained execution trace; raw-URI handoff and pre-catalog summary reads have the seams described above.
- design conclusion status: claimed
- implementation conclusion status: afforded
- operation conclusion status: uninspected

Admission: user supplies sources/problem and can request dry-run or confirmation; model writers choose claims and write knowledge without routine per-claim human approval. Proposer and decider are the model roles; the user can redirect or override but append normally skips the discussion checkpoint. Guidance requests source links, source-native framing and explicit synthesis markers. What persists is source copies and formulated wiki content, not model parameters. Rejection occurs through dedup/skips or worker noops; user can stop the workflow. Recovery is per-source skip/fallback and partial-run overwrite guidance, not a transactional rollback. Existing KEEP blocks request preservation, not a software veto. Operating mode is an open research request with seed-only processing, not a scored experiment. Answer oracle: none supplied; source texts support claims but do not define an expected complete answer.

> For **append**, show the plan and proceed unless the user asked for confirmation first.
> --- `plugins/ai-research-os/skills/research/SKILL.md`

> - **Preserve user edits.** If `existing_page_path` has a `<!-- KEEP -->` marker around any line/block, preserve those lines verbatim in your rewrite. (This is the user's escape hatch for hand-editing.)
> --- `plugins/ai-research-os/skills/research/agents/wiki_page_writer.md`

Theory account: synthesis instructions request a thesis, assumptions, counter-evidence and revision conditions; these are formulated external-topic theories if produced, not revisions of the plugin method. Guidance is applied to source/wiki material; the model proposes and retains an argument, preserving prior human blocks. SRC-1: `plugins/ai-research-os/skills/research/agents/wiki_summary_writer.md`.

> <What the wiki contains that pushes against the thesis. Be honest — if there's strong contradiction, the thesis should weaken or split. Wikilink contradictions.md.>
> --- `plugins/ai-research-os/skills/research/agents/wiki_summary_writer.md`

Theory-builder conditions 1–4:
- Condition 1 conclusion status: afforded
  The requested whole thesis plus dependencies is localized language content; no produced theory is observed here.
- Condition 2 conclusion status: afforded
  Query/compose and export routes are instructed to use retained synthesis; actual content-dependent decisions are unobserved.
- Condition 3 conclusion status: afforded
  The summary writer requests counter-evidence and weakening/splitting; it does not supply an observed criticism with blame and resulting revision.
- Condition 4 conclusion status: afforded
  Existing synthesis and contradiction/open-question files can enter the next ingest; the ordering and bounded reads limit what actually reaches a writer.

Addressability: headings expose assumptions and supporting/counter moves for inspection and whole-page or block revision; arbitrary fine-grained independent revision is not implemented as an API. Persistence: wiki pages are intended to survive sessions and topics' successive ingests. Learning: improved future action capacity is not established by this source-only account; persistence and requested synthesis revision alone do not prove it. Reflection: represented subject matter is external research, not demonstrated bidirectional self-representation of the plugin's operations. Reflective theory builder: uninspected beyond these external-topic routes; own method criticism is not established here. Autonomous theory builder: computation is assigned writing/selection, but optional discussion and deliberate overrides leave internal human participation mode-dependent; no complete exercised autonomous cycle is supplied.

#### RT-RTE-index-build
Label: Canonical index and navigation generation

Endpoints: supplied seed/results JSON plus optional prior YAML → `load_sources` normalization/carry-forward/sort → YAML write → Markdown builder with live wiki tree → navigation file. Owner is the Python process for transformation; orchestrator owns input selection and invocation. Metadata strings are preserved/projected fields, not fact-checked claims. Missing raw/source pointers become null rather than verified files. SRC-1: `plugins/ai-research-os/skills/research/scripts/build_index_yaml.py`; `plugins/ai-research-os/skills/research/scripts/build_index_md.py`.

- Immediate return: Each helper writes its requested file and prints a small completion/count message.
- Later read-back: YAML source metadata/pointers enter later query and export; Markdown navigation enters browsing and query fallback.
- Delegated visibility: Helpers read input files directly, normalize all source rows and scan wiki paths; output depends on supplied files rather than orchestrator prose context.
- Selection predicate: Seeds force 1.0, supersede carried rows with matching nonempty original_path and exclude matching rest rows; rest sorts by descending score. Navigation groups seeds/origins and lists files.
- Invalidation or expiry: New invocation replaces output, sets last_updated to local now for YAML, and optionally preserves created. Markdown regenerates from YAML and the current wiki tree.
- Activation or effect: File writes are wired; downstream behavioral activation is unobserved.
- Evidence limits: No target execution; uniqueness among seeds/ranked rows, file-pointer validity and prior preservation without --existing-index are not guaranteed.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission: caller supplies proposed rows and flags; software normalizes and writes without per-content human approval or oracle. Seed score is a fixed rule; longest-summary dedup occurs upstream, not a truth ranking. Rejection is limited to schema projection/existing-row supersession rather than source validity checks. Recovery: driver snapshots prior YAML briefly, then deletes snapshot after the builder; helper itself writes output directly and has no multi-file transaction. Operating mode is deterministic catalog construction under an open request. Persistent result is YAML/Markdown; guidance is the fixed code schema, not a revised instruction set.

> # Seeds always score 1.0 per the skill's rules; enforce it in case the input lied.
> for row in seed_rows:
>     row["relevance_score"] = 1.0
> --- `plugins/ai-research-os/skills/research/scripts/build_index_yaml.py`

> if existing_index_path is None or not existing_index_path.exists():
>     return []
> --- `plugins/ai-research-os/skills/research/scripts/build_index_yaml.py`

#### RT-RTE-deep-discovery
Label: Preset discovery and gap-directed rounds

Endpoints: explicit user discovery choice → preset and CLI/auth detection → query workers → dedup helper → optional gap analyzer → next queries → final scored discovery results → append construction. Host orchestrator owns dispatch and count limits. Researchers use Obsidian search/reads, Readwise library/feed/highlight/annotation searches and NotebookLM notes plus model query citations. Missing or unauthenticated sources degrade with warnings; zero usable sources stops the route. SRC-1: `plugins/ai-research-os/skills/research/SKILL.md` Steps 0.5, 2–5; `plugins/ai-research-os/skills/research/agents/researcher.md`; `plugins/ai-research-os/skills/research/agents/gap_analyzer.md`; `plugins/ai-research-os/skills/research/scripts/dedup_findings.py`.

- Immediate return: Research workers save findings JSON; gap analyzer saves next queries and coverage notes; helper returns counts; final ingestion returns the ordinary research result.
- Later read-back: Selected findings' summaries/tags and copied source content reach later catalog/wiki consumers; intermediate round and query JSON is scheduled for deletion after success.
- Delegated visibility: Research workers receive topic/themes, query, notebook IDs and CLI availability; gap analyzer receives compact findings metadata, never full source files.
- Selection predicate: Presets fast/light/deep mean 1/2/3 rounds with 3, 3+2 or 3+3+3 queries; available nonempty notebooks are all searched, but researcher relevance and top-K cap restrict admitted findings.
- Invalidation or expiry: Auth failure skips NotebookLM for the remaining run; intermediate JSON is cleaned after successful construction. Retained source/wiki content has no TTL.
- Activation or effect: Prompted next-query changes based on round metadata; helper dedup/scoring is wired. Source acquisition and next-round exercise are unobserved.
- Evidence limits: “Every candidate kept” applies after upstream relevance filtering/capping, not all search hits or all notebook content; model query omissions and service semantics are outside inspected implementation.
- design conclusion status: claimed
- implementation conclusion status: afforded
- operation conclusion status: uninspected

Admission/comparison roles: user chooses discovery/depth; orchestrator proposes initial angles; researchers select and label hits; dedup software keeps longest summaries; gap analyzer diagnoses thin themes and proposes the successor query set. User discussion can drop propagation, merge slugs or change emphasis before higher wiki admission, and is skippable. No expected-answer oracle is supplied; NotebookLM's AI answer is a selector input, not a gold answer. Operating mode is preset-bounded search, not a causal experiment. Improvement trigger is thin/missing theme coverage, not measured model capacity. Rollback/recovery is skipping unavailable origins or rerunning partial output, with no atomic multi-agent transaction. The static gap guidance persists in the plugin; findings and query notes are temporary unless propagated to the wiki. This is coverage-guided query refinement, not by itself theory criticism: thin themes do not identify a false theory or placement of blame.

> 2. **Apply the top-K cap: keep at most 15 unique findings.** Rank by (a) `relevance: "high"` before `"medium"`, then (b) richness of metadata + summary length as tiebreakers. Drop anything beyond rank 15.
> --- `plugins/ai-research-os/skills/research/agents/researcher.md`

> if not key:
>     continue
> --- `plugins/ai-research-os/skills/research/scripts/dedup_findings.py`

#### RT-RTE-github-ingest
Label: GitHub clone to curated repository specifications

Endpoints: user repo/path references → target-parser JSON → sibling cached clone/HEAD SHA → parallel module writers then architecture writer → staged docs → one catalog seed. Source identity includes owner/repo@commit; module paths are ancillary metadata. The host orchestrator owns ordering; clone helper owns fetch/reset/reclone. Agent specs are natural-language curated content, not copies of all code. SRC-1: `plugins/ai-research-os/skills/research/SKILL.md` Step 1a; `plugins/ai-research-os/skills/research/scripts/github_clone.py`; `plugins/ai-research-os/skills/research/agents/github_spec_writer.md`; `plugins/ai-research-os/skills/research/agents/builder.md`.

- Immediate return: Clone helper returns owner/repo/branch/path/SHA/action JSON; writers save staged specs; orchestrator makes one seed and reports ingestion.
- Later read-back: Intended wiki repo ARCHITECTURE hub leads query/distill readers to module specs; index stores commit and referenced file union, not each module as a source.
- Delegated visibility: Module workers receive referenced files/ranges; architecture worker sees repo entry points/docs and staged module summaries. Per-writer read/output budgets narrow coverage.
- Selection predicate: GitHub is seed-only; parser groups references by directory; empty target modules select global architecture mode; one seed per repo receives 1.0.
- Invalidation or expiry: Cache refresh fetches/reset branch HEAD and returns new SHA; explicit cache override is possible. Curated files are overwritten on ingestion; no content-hash refresh policy for consumers is specified.
- Activation or effect: Git subprocess and cache writes are wired. Spec generation and resolved curated-document delivery remain afforded, with the inconsistent builder copy destination stated here.
- Evidence limits: Target parser implementation is uninspected; shared cache concurrency is not locked in the inspected clone helper; builder creates wiki destination but copies to raw while declaring wiki pointers.
- implementation conclusion status: afforded
- operation conclusion status: uninspected

Admission: user supplies repo/paths; model spec writer chooses explanatory content under topical scope and commit-permalink guidance; software does not approve the resulting claims. No answer oracle or per-spec human review is specified. Operating mode is bounded source reading under an open request. The user may stop or correct the result; absent files are recorded and skipped. Cache update failure deletes/reclones cache, not a knowledge rollback. What persists should be curated wiki specs plus commit metadata; cache is reusable but mutable. The conventions win over builder recipes, so the raw-target copy cannot be treated as the intended contract.

> - **GitHub**: stored ONLY under `wiki/repos/<repo>/` (curated `ARCHITECTURE.md` + per-module `<module>.md`).
> --- `plugins/ai-research-os/skills/research/CONVENTIONS.md`

> cp -a "<staged_repo_dir>"/. "<research_dir>/raw/<repo-slug>/"
> --- `plugins/ai-research-os/skills/research/agents/builder.md`

> run(["git", "reset", "--hard", f"origin/{branch}"], cwd=clone_path)
> --- `plugins/ai-research-os/skills/research/scripts/github_clone.py`

#### RT-RTE-query-answer
Label: Progressive query and conditional answer admission

Endpoints: user/skill question → directory/catalog locator → summary/wiki/pointer selection → answer → conditional knowledge/question save-back and log. Owner is host model interpreting query instructions; missing YAML selects read-only Markdown/wiki fallback. Source-native shape can be query, load, filter, drill-down or compose. Immediate consumer receives selected/synthesized content rather than all retained evidence. SRC-1: `plugins/ai-research-os/skills/research/SKILL.md` Query path; `plugins/ai-research-os/skills/research/CONVENTIONS.md` operation map.

- Immediate return: User gets cited answer and optional saved paths; another skill gets YAML-shaped sources/pages/layers/saved-path metadata without conversational framing.
- Later read-back: Intended saved question pointers and knowledge documents reach later wiki/query consumers; query log records even unsaved conversational answers under the skill recipe.
- Delegated visibility: inapplicable — the query recipe does not dispatch its answer to a dedicated subagent; another skill caller receives selected result, not all raw files.
- Selection predicate: Match summaries/tags/frontmatter, origin/score/date/repo filters and caller depth; ascend summary → source page → curated highlights → full content only as necessary. Save on explicit bookmark or at least two cited sources.
- Invalidation or expiry: Saved topic knowledge is to update in place; missing canonical YAML disables all writes in fallback. No TTL or automatic correctness invalidation is specified.
- Activation or effect: Answer synthesis and conditional save-back are requested; downstream content-dependent activation remains unobserved.
- Evidence limits: Q.5 knowledge-doc enrichment exceeds both opening query permissions and the authoritative conventions' question-page-only addition map; compliant landing behavior is not established.
- design conclusion status: claimed
- implementation conclusion status: afforded
- operation conclusion status: uninspected

Admission: model proposes/decides synthesized answer content; explicit user bookmark or two-source answer triggers save without per-content approval. User can request keeping content or deliberately override. No expected-answer oracle is supplied. Operating mode is open question answering with depth controls, not a curriculum. Guidance requires claim links, a synthesis line, knowledge/pointer split and dedup enrichment. Rejection is no-save for ordinary single-source conversation; fallback rejects all saves. Recovery is restoring YAML before mutation, with no transactional rollback across knowledge doc/pointer/index/log. Persisted knowledge is not established solely by a cited-source count: that count licenses the route rather than proving its truth.

> - The answer cites ≥ 2 sources (i.e., the question required synthesis across the wiki)
> --- `plugins/ai-research-os/skills/research/SKILL.md`

> | **Concept / entity drill-down** — about a concept or entity the wiki tracks | Enrich existing `wiki/concepts/<slug>.md` / `wiki/entities/<slug>.md` in place | If the concept doesn't yet have a page but the answer has enough material to start one, create it. If it's only a single-source mention, flag in `wiki/open-questions.md` for next ingest instead. |
> --- `plugins/ai-research-os/skills/research/SKILL.md`

#### RT-RTE-lint-maintenance
Label: User-triggered mechanical and model wiki review

Endpoints: user lint request → locator/check selection → four mechanical subprocess outputs and three bounded judge roles → additive contradiction/question files, navigation and log → report/action items. Orchestrator owns request/check coordination; mechanical helpers own fixed checks; judges decide semantic findings. Stale claims and ordinary broken links are flags, not automatic claim rewrites. SRC-1: `plugins/ai-research-os/skills/research-lint/SKILL.md`; `plugins/ai-research-os/skills/research-lint/agents/lint_judge.md`; `plugins/ai-research-os/skills/research-lint/scripts/lint_broken_links.py`.

- Immediate return: Mechanical JSON and judge summaries feed a capped report with full-finding scratch paths and actions needing user judgment.
- Later read-back: Contradictions and questions can enter query and next summary-writer context; log records counts. No automatic follow-on discovery is specified.
- Delegated visibility: Judge reads wiki only, capped at eight full pages; contradictions use entity/concept tensions with at least two sources; stale claims use at least three sources and over twelve-month backing-date spread.
- Selection predicate: User may skip LLM checks; driver says cheap four always run. Candidate sections/source counts/date spread narrow semantic review; duplicate judgments decide whether to append.
- Invalidation or expiry: Rolling findings append and do not remove old entries; scratch JSON can be removed after review. Stale-entry cleanup is a future feature in judge guidance.
- Activation or effect: Broken-link traversal/finding output is wired through imported helpers; contradiction/question writes are requested. Actual correction of claims and later reliance changes are unobserved.
- Evidence limits: Driver asks broader source-page tensions reads while judge narrows to entity/concept pages; no comprehensive semantic audit or reliable idempotency is established. Exact imported link-resolution rules are uninspected.
- implementation conclusion status: afforded
- operation conclusion status: uninspected

Admission/diagnosis: model judge proposes and appends contradictions/questions without individual human approval; user decides how to resolve stale claims, orphans or broken links. Expected answer oracle: none; source opposition/date metadata and file existence are judgment inputs, not a correctness benchmark. Operating mode is user-triggered audit with scope options. Improvement trigger is inconsistency/thin coverage. Rejection is duplicate skip, conservative stale flagging or empty findings. Recovery is rerun/explicit user repair, not restoring a previous transaction. Guidance requests citation separation from synthesis. Criticism persists in rolling files, not automatically a revised plugin method or corrected source claim.

> - **Append, never rewrite.** `contradictions.md` and `open-questions.md` grow; older sections stay even when no longer relevant. Lint cleanup of stale entries is a future feature, not yours to do.
> --- `plugins/ai-research-os/skills/research-lint/agents/lint_judge.md`

Theory account: judges describe opposing claims and current leaning; stale-claim flags compare unqualified older claims with newer contradictory/superseding claims. They retain criticism and candidate research questions. These can feed the thesis writer, but a report is not by itself theory revision or changed reliance. SRC-1: `plugins/ai-research-os/skills/research-lint/agents/lint_judge.md`; `plugins/ai-research-os/skills/research/agents/wiki_summary_writer.md`.

Theory-builder conditions 1–4:
- Condition 1 conclusion status: afforded
  Claim A/B and subject fields request localized challenged assertions.
- Condition 2 conclusion status: afforded
  Summary writer is directed to read contradictions and incorporate counter-evidence; actual dependence is unobserved.
- Condition 3 conclusion status: afforded
  Stale flags name challenged claim and newer counterclaim; resulting revision/blame beyond claim disagreement is not established by the flag-only route.
- Condition 4 conclusion status: afforded
  Rolling files are eligible inputs to subsequent ingest/query, but retained unused reports do not establish exercised iteration.

Addressability: individual conflict/claim sections can be inspected; the judge does not expose a semantic revision API. Persistence: intended across sessions in rolling Markdown. Learning: no improved future capacity or outcome comparison is supplied. Reflection and reflective theory builder: this route represents wiki research claims, not demonstrated criticism of its own method against its own operational records. Autonomous theory builder: automatic additive diagnosis coexists with human resolution of stale claims; full autonomous internal revision is not established.

#### RT-RTE-distill-export
Label: Content-relative source appendix export

Endpoints: user content files plus located research directory → model source matching and layered reads → compact `research.md` beside content → user report. Model owns explicit/traceable match decisions and claim/quote distillation. Directory requests expand all Markdown content into the matching corpus. SRC-1: `plugins/ai-research-os/skills/research-distill/SKILL.md`.

- Immediate return: Export file plus matched counts, match types, path, rough token estimate and borderline candidates.
- Later read-back: Appendix is intended as writer-agent context with exact metadata/pointers and quote fragments; whether a later writer receives/uses it is unobserved.
- Delegated visibility: inapplicable — the distill driver specifies direct content/source reading and export, not a dedicated dispatched subagent.
- Selection predicate: Explicit title/author/URL/path/citation/repo-file references or distinctive traceable ideas; user seeds are not auto-included. Read source page, highlights, full text and catalog summary as availability permits.
- Invalidation or expiry: New exports describe generated time; no automatic invalidation when corpus or sources change is specified. Missing layers degrade to metadata/summary with explanations.
- Activation or effect: Requested compact appendix write outside research directory; delivery/benefit to a later writer is unobserved.
- Evidence limits: Model matching does not prove actual source use or quote exactness; driver read-only instruction conflicts with conventions' distill log exception, whose precedence allows the log.
- implementation conclusion status: afforded
- operation conclusion status: uninspected

Admission: user supplies corpus; model decides source inclusion and distilled claims without per-source approval; conservative exclusions are surfaced so the user can add borderline cases. No expected-reference appendix/answer oracle is supplied. Operating mode is open export constrained by a corpus, not measured evaluation. Guidance preserves metadata and quotes while condensing prose to relevant claims/nuances; export is persistent content, not a capability update. Recovery is layered fallback or rerun; no rollback gate is specified. SRC-1: `plugins/ai-research-os/skills/research-distill/SKILL.md`; `plugins/ai-research-os/skills/research/CONVENTIONS.md`.

> - **Seed URIs (score 1.0) are not auto-included.** Even though they were user-provided in the research phase, they should only appear in `research.md` if the content actually uses them. The question is "was it used?", not "was it important to the research?"
> --- `plugins/ai-research-os/skills/research-distill/SKILL.md`

#### RT-RTE-render-output
Label: Wiki rendering and generated chart execution

Endpoints: user format/framing plus selected wiki pages → prompt/path idempotency gate → format writer → retained artifact → navigation/log/result. One writer per format can run in parallel. Chart subagent writes Python; orchestrator executes it with uv to generate PNG. The chart skeleton embeds hard-coded data from read-time wiki state. Owner is host orchestrator for admission/execution, model writer for generated program/prose and external Python/matplotlib for chart effects. SRC-1: `plugins/ai-research-os/skills/research-render/SKILL.md`; `plugins/ai-research-os/skills/research-render/agents/chart_writer.md`.

- Immediate return: Writer JSON and user artifact paths/viewing instructions; chart execution failure is surfaced with script retained.
- Later read-back: Render files appear in regenerated navigation; chart's Python preserves the extracted numerical snapshot for later execution. Later actual reuse is unobserved.
- Delegated visibility: Each writer receives selected wiki pages, user prompt and output path; orchestrator normally does not read page bodies. Chart writer may extract index tallies despite general wiki-page framing.
- Selection predicate: User verb or multiselect chooses formats; source pages/frame determine data; identical prompt and source list request noop. Different metadata requires overwrite/suffix/skip choice.
- Invalidation or expiry: No source-content hash is compared; identical paths/prompt after changed wiki content can still noop. Script data remains frozen at render time until regeneration actually occurs.
- Activation or effect: Requested artifact writes and chart Python execution; actual execution and host confinement are unobserved.
- Evidence limits: Other format writer bodies are uninspected here; declared same-input reproducibility is not a measured model guarantee. Generated code executes under host permissions, not an inspected plugin sandbox.
- implementation conclusion status: afforded
- operation conclusion status: uninspected

Admission: user selects format/prompt and can veto overwrite; model chooses chart data/kind and writes executable Python; driver requests execution without a separate program-content approval. No chart expected-answer oracle is supplied. Operating mode is open rendering, not a bounded experiment. Guidance shapes matplotlib/headless output and hard-coded data; `.py` plus PNG persist. Brief can return needs_guidance without writing and ask for adjusted scope; chart failures retain code for user fix/rerun. This admits an executable output capability for one render, not a demonstrated revision to the plugin's production machinery. SRC-1: `plugins/ai-research-os/skills/research-render/SKILL.md`; `plugins/ai-research-os/skills/research-render/agents/chart_writer.md`.

> For `chart` only: after the writer subagent saves the `.py` script, the orchestrator runs it via `uv run --script` to produce the `.png` (the script carries a PEP 723 header declaring matplotlib, so it self-bootstraps).
> --- `plugins/ai-research-os/skills/research-render/SKILL.md`

> 5. Hard-code the data inside `build_data()`. The wiki snapshot you read is now embedded in the script — that's the *point*: the PNG is reproducible from this script alone, even if the wiki changes later. If the user wants a re-render against fresh data, they re-run `/research-render`.
> --- `plugins/ai-research-os/skills/research-render/agents/chart_writer.md`

### Claims

#### RT-CLM-query-safety
Label: Query write-scope safety policy

Claimed operation: answer fast from existing memory without discovery/raw rewrites, with limited conditional save-back. Owner: skill author/orchestrator. Enforcement point: interpreted routing and query instructions. Guarantee strength: policy. Coverage: normal query and stricter missing-YAML fallback; alternate ingest/lint/render paths have separate scopes, and direct shell/helper/manual edits are not intercepted. External contract: host follows precedence and limits tool effects. SRC-1: `plugins/ai-research-os/skills/research/SKILL.md`; `plugins/ai-research-os/skills/research/CONVENTIONS.md`.

- design conclusion status: claimed
- implementation conclusion status: afforded
- operation conclusion status: uninspected

> | `/research` (query, save Q&A) | — | — | add `wiki/questions/...` | update counts | regenerate | append | — |
> --- `plugins/ai-research-os/skills/research/CONVENTIONS.md`

This is not blanket read-only: the authoritative map permits question addition, and Q.5 requests wider knowledge landing in conflict with it. Actual model resolution is unobserved. [RT-RTE-query-answer](#rt-rte-query-answer) gives the corresponding admission route.

#### RT-CLM-raw-policy
Label: Post-ingest raw immutability policy

Claimed operation: raw and assets are retained without automatic post-ingest edits/deletions, with explicit consent for re-ingesting an existing source. Owner: conventions author/interpreting orchestrator. Enforcement point: dedup/preconditions and instructions, not filesystem protection. Guarantee strength: policy. Coverage: prescribed ingest and subsequent consumption; asset localization is an explicit initial transformation, direct builder/helper calls and user edits are alternate paths. External contract: host respects raw-scope rules and consent despite builder overwrite guidance. SRC-1: `plugins/ai-research-os/skills/research/CONVENTIONS.md`; `plugins/ai-research-os/skills/research/agents/builder.md`; `plugins/ai-research-os/skills/research/scripts/download_assets.py`.

- design conclusion status: claimed
- implementation conclusion status: afforded
- operation conclusion status: uninspected

> - `raw/` is **immutable**. Files land here on ingest and are never edited. Re-ingesting an existing source overwrites only with explicit user consent.
> --- `plugins/ai-research-os/skills/research/CONVENTIONS.md`

> - **Idempotent.** If `research_dir` already has some of the files (e.g. partial previous run), overwrite without prompting. `cp` and `>` already do this.
> --- `plugins/ai-research-os/skills/research/agents/builder.md`

The asset helper implements initial reference rewriting, so byte immutability from first copy is not even the full declared ingest behavior. Dedup intent cannot protect direct helper calls. [RT-RTE-append-ingest](#rt-rte-append-ingest).

#### RT-CLM-index-contract
Label: Narrow executable catalog guarantees

Claimed operation: canonical YAML construction forces seed scores, preserves supplied prior rows not superseded, and emits a fixed projection; navigation regeneration is deterministic for YAML plus wiki-tree inputs. Owner/enforcement: helper code executes these transformations. Guarantee strength: invariant within the relevant function inputs, not a whole-workflow guarantee. Covered paths: direct/helper driver invocation with required inputs and normal Python/filesystem behavior. Alternates: omitting prior index loses carry-forward; bypassing upstream dedup can preserve duplicate ranked or seed rows; hand-editing outputs bypasses construction. SRC-1: `plugins/ai-research-os/skills/research/scripts/build_index_yaml.py`; `plugins/ai-research-os/skills/research/scripts/build_index_md.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected

> # De-dupe by original_path: a seed always wins over a ranked/carried row.
> seen = {row.get("original_path") for row in seed_rows if row.get("original_path")}
> rest = [r for r in rest if r.get("original_path") not in seen]
>
> return seed_rows + rest
> --- `plugins/ai-research-os/skills/research/scripts/build_index_yaml.py`

> - Output is deterministic: identical inputs (yaml + wiki tree) produce
>     byte-identical output.
> --- `plugins/ai-research-os/skills/research/scripts/build_index_md.py`

The comment describes seed precedence, not complete dedup of every rest entry. Markdown determinism includes tree contents; the conventions' shorter identical-YAML claim omits that input. The YAML builder changes last_updated each invocation and cannot promise byte-identical YAML. [RT-RTE-index-build](#rt-rte-index-build).

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-skill-guidance
Label: Static plugin guidance to host behavior

Consumer: host orchestrator and delegated model roles. Channel: installed skill text and agent-file content included in dispatch prompts. Force: natural-language routing/selection/write policy, dependent on host/model compliance rather than mandatory tool interception. Horizon: current invocation and any later invocation that loads the shipped plugin; static material is not accumulated memory. Different role instructions scope reads and outputs but do not reveal deployed tool grants. SRC-1: `plugins/ai-research-os/skills/research/SKILL.md` Step 4 and Agent reference; `plugins/ai-research-os/skills/research/agents/source_writer.md`.

> Each subagent follows the instructions in `agents/researcher.md` (read that file and pass its content as the subagent prompt, along with the specific query and context).
> --- `plugins/ai-research-os/skills/research/SKILL.md`

#### RT-BAP-helper-execution
Label: Symbolic helper and generated-program effects

Consumer: Python/Git/shell processes invoked by the host. Channel: CLI arguments/files and source programs. Force: executable transformations and filesystem/subprocess/network effects under host permissions. Horizon: one helper/render execution; generated chart script can persist for reruns. This path distinguishes program execution from model interpretation of wiki text; host access controls and exact deployment confinement are uninspected. SRC-1: `plugins/ai-research-os/skills/research/scripts/github_clone.py`; `plugins/ai-research-os/skills/research/scripts/build_index_yaml.py`; `plugins/ai-research-os/skills/research-render/SKILL.md`.

> return subprocess.run(cmd, cwd=cwd, check=True, capture_output=True, text=True)
> --- `plugins/ai-research-os/skills/research/scripts/github_clone.py`

## Annotations

none
