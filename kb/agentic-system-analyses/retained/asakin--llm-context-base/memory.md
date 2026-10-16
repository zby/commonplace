---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Memory mechanisms of llm-context-base: file-retained knowledge, conversation-derived operating guidance and selective session/query reload."
run-id: AAS-2026-10-14-llm-context-base-f63a7c0fb5f2-01
source-identity: "https://github.com/asakin/llm-context-base"
reviewed-boundary: "6d01cba8e2c22f9ca2519c70073a05cd54378a8c"
---

# llm-context-base memory report

## Boundary and evidence

This report covers the template's prescribed acquisition, extraction, filing, context adaptation, evaluation, withdrawal and later file consumption. The frozen source is SRC-1 in [boundary](boundary.md#source-register), at commit 6d01cba8e2c22f9ca2519c70073a05cd54378a8c. HEAD and the clean source checkout were rechecked. The external assistant, filesystem tool executor, Obsidian/clipper implementations, synchronization providers and host compactor remain outside the inspected implementation. Their configured or documented interfaces remain included. The overall evidence is doctrine/design; the metadata converter alone supplies executable implementation evidence. No target execution or supplied user trace establishes activation or benefit.

The following inventory distinguishes direct inspection in this job from supplied findings. All paths are SRC-1. No source-register expansion is needed. The tracked tree was inventoried, and a bounded search traced archive, source, sync, publish, template and inbox references through the content roots, Obsidian settings, bootstraps and relevant integration documentation. There is no internal CLI dispatch, service or registered retrieval-tool implementation among these tracked files; the operative entry points are prompts, declarative integrations and the standalone converter. This is a bounded inventory, not a claim about installed external hosts.

| Entry point or operation | Source paths and inspection | Covering records or limits |
|---|---|---|
| Session/profile initialization; phase loading; framework exception | Direct: `_config/config.md`, `_meta/instructions/general.md`; supplied runtime: `AGENTS.md`, `.claude/CLAUDE.md` | [RT-RTE-session-start](runtime.md#rt-rte-session-start); [MEM-OBJ-config](#mem-obj-config), [MEM-OBJ-context](#mem-obj-context). Actual host discovery uninspected. |
| Conversation-derived preferences, conventions, templates and directories | Direct: `_meta/instructions/general.md`, `_config/config.md`, `_config/context.md` | [MEM-RTE-pattern-capture](#mem-rte-pattern-capture); [RT-BAP-instruction-load](runtime.md#rt-bap-instruction-load). No real training episode supplied. |
| Capture, extraction, filing and source preservation | Direct: `_meta/instructions/agent-write.md`, `_meta/instructions/general.md`, `_inbox/README.md`, `_sources/README.md` | [RT-RTE-capture-file](runtime.md#rt-rte-capture-file); [MEM-OBJ-inbox](#mem-obj-inbox), [MEM-OBJ-sources](#mem-obj-sources), [MEM-OBJ-knowledge](#mem-obj-knowledge). Original retention optional. |
| Human/editor/clipper admission | Direct: `assets/clipper-template.json`, `.obsidian/daily-notes.json`, `_inbox/README.md`; supplied boundary: `.obsidian/app.json`, `.obsidian/templates.json` | Capture annotation; inbox object. External execution uninspected; clip metadata differs from standard. |
| Query, saved synthesis, proactive precedent | Direct: `_meta/instructions/knowledge-query.md`, `_config/standard.md`, `_meta/templates/decision.md` | [RT-RTE-knowledge-query](runtime.md#rt-rte-knowledge-query); [MEM-OBJ-decision](#mem-obj-decision), [MEM-OBJ-metadata](#mem-obj-metadata). No populated corpus or retrieval result. |
| Project lifecycle, navigation/index updates, logs and README regeneration | Direct: `1-Projects/README.md`, `_meta/instructions/general.md`, `2-Knowledge/log.md`, `WIKI-LOG.md` | Knowledge/metadata objects; [MEM-OBJ-logs](#mem-obj-logs). Supplied boundary covers parked README and other templates; no active project supplied. |
| Completion, lint, archive/supersede, link and filename cleanup | Direct: `_meta/instructions/definition-of-done.md`, `_meta/instructions/knowledge-lint.md`, `_config/standard.md` | [MEM-RTE-lint-maintenance](#mem-rte-lint-maintenance). Checks are instructions, not a deployed validator. |
| Instruction optimization | Direct: `_meta/instructions/optimization-review.md` | [RT-RTE-context-review](runtime.md#rt-rte-context-review). Later loading is prescribed, not observed. |
| Compaction reload and read-path log recipes | Direct: `docs/claude-code-setup.md`; supplied boundary: `.claude/settings.json` | [MEM-RTE-compact-reload](#mem-rte-compact-reload), logs object. Scripts shown in docs, not shipped installed hooks. Host summary contents opaque. |
| Bulk metadata migration | Direct: `migrate-to-yaml-frontmatter.py` | [RT-RTE-metadata-migrate](runtime.md#rt-rte-metadata-migrate). Direct rewrite bypasses capture review; no execution. |
| Journal/private retention and optional sync | Direct: `.gitignore`, `.obsidian/daily-notes.json`; supplied boundary and source search: `docs/journal-sync.md`, `3-Journal/README.md`, `4-Private/README.md` | Knowledge object. Local plain text versus encrypted Git or external-sync recipes are distinct substrates; implementations and deployments uninspected. |
| Blog publishing, exports and linked-code consumption | Direct: `_meta/instructions/blog-posts/instructions.md`, `_output/README.md`, `docs/linked-code-repos.md` | Knowledge object; [MEM-BAP-linked-context](#mem-bap-linked-context). Published platforms and code roots not acquired; actual export/publication not established. |

Excluded host-native transcript/memory stores are not treated as target-retained knowledge. The documented transcript-history setting and compaction interface do not disclose a raw-to-summary algorithm or complete payload. Sources, journal entries, private files and user outcomes are absent from the shipped example corpus as actual user data; this prevents quality and effectiveness conclusions, not an architectural account of their intended routes.

## Core ideas

1. **The files, not a hidden index, carry continuity.** Conversation discoveries are directed into profile/context, operating instructions, templates and content. Future sessions read the current files; relevant queries read selected content. Static shipped prompts are operating guidance, while use-derived edits to them constitute retained memory. The supplied [RT-BAP-instruction-load](runtime.md#rt-bap-instruction-load) supports the consequential text-to-policy route; [MEM-RTE-pattern-capture](#mem-rte-pattern-capture) separates its write agency and retained products.
2. **Selection is model-mediated and budgeted in files/lines, not tokens.** Startup phase excludes some static files; task routing defers unused instruction bodies; query routing scans summaries/tags then reads 1–3 files, truncating very large files to their first major section. The host still must put read text into the window by value. A path or index entry is not a live reference to unloaded content. See query and session annotations.
3. **Admission differs by retained part.** Ordinary captures start as draft/inbox with a filing question. New rules and preferences are to be written immediately; instruction restructuring specifically needs approval; independent clipper/user writes and the converter have different controls. Draft status is not a universal quarantine. [RT-CLM-review-policy](runtime.md#rt-clm-review-policy) already qualifies the intended review opportunity.
4. **Extraction may lose provenance.** A working article can replace a full clip; retaining the original is off by default. Metadata attribution identifies an agent or URL, not source truth. Decision records can retain rationale, rejected alternatives and outcomes, but generic learned preferences need not retain their reasons. [MEM-OBJ-sources](#mem-obj-sources) and [MEM-OBJ-decision](#mem-obj-decision) distinguish those cases.
5. **Withdrawal changes selection rather than guaranteeing disappearance.** Archived files remain for reference and are usually deprioritized, not universally blocked. Supersession reasons are retained by convention. Completion moves project folders out of active indexes. Staleness produces warnings, not automatic eviction. [MEM-RTE-lint-maintenance](#mem-rte-lint-maintenance) traces these controls and their limits.

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-config
Label: Configuration profile and training log

Source-native identity: `_config/config.md`, specifically About You, System Settings, Training Log and Your Conventions. Storage: local Markdown, normally Git-versionable; form: natural-language facts, observations and directives with textual date/phase values interpreted by the assistant. This is not model-parameter training. Its shipped placeholders are initialization state, not learned user information. User answers initialize the profile; assistant observations and user corrections subsequently populate preferences, structure adaptations and conventions. The log records selected observations, not a verbatim transcript. Later startup reads it to calculate phase, choose questions/tips and apply learned conventions. Authority at that consumer is requested personalization and operating policy, contingent on interpretation/adherence. No counterpart after comparison with [RT-OBJ-instruction-modules](runtime.md#rt-obj-instruction-modules): config is a separate retained destination, consumed through [RT-RTE-session-start](runtime.md#rt-rte-session-start). SRC-1, `_config/config.md`, `_meta/instructions/general.md`.

> - At the end of each session, update the Training Log with anything new you learned
> --- `_config/config.md`

> - Stop logging to Training Log (it should be stable by now)
> --- `_config/config.md`

The second instruction applies in cooldown; immediate capture elsewhere remains prescribed. Calendar-based reduction of questions is not evidence that preferences are correct or stable. Initial admission is user-supplied answers; later observations are model-authored, without universal per-entry approval. No demonstrated improvement is supplied.

#### MEM-OBJ-context
Label: Personal context

Source-native identity: `_config/context.md`; storage: local Markdown, normally Git-versionable; form: natural-language personal details, key people, communication preferences, tools/environment. Lineage: user manual entries or assistant-derived facts from conversation. The file declares population during training, while general instructions also require immediate preference/detail capture. Future session reads provide personalization; the title's “machine-readable” label does not establish a fixed-schema symbolic consumer. No counterpart after comparison with [RT-OBJ-instruction-modules](runtime.md#rt-obj-instruction-modules): this is contextual content, not the modules. SRC-1, `_config/context.md`, `_meta/instructions/general.md`.

> **This file is populated by your AI during training.** As it learns about you, it logs personal details here so future sessions can reference them without asking again. You can also add things manually at any time.
> --- `_config/context.md`

The template contains illustrative comments, not actual learned personal facts. Reasons for preferences and their original turns are not required fields. Startup delivery is prescribed; accurate interpretation, correction and future behavior are unobserved.

#### MEM-OBJ-inbox
Label: Inbox captures

Source-native identity: `_inbox/` captures. Storage: dated filesystem notes, normally Git-versionable. Form: natural-language raw user material, clipped text, or an assistant's derived first take; not uniformly raw traces or uniformly curated knowledge. Lineage varies by entry point: user capture, assistant capture from conversation, or external clipper content plus user intent. Selector metadata is treated separately in [MEM-OBJ-metadata](#mem-obj-metadata). Distinct from [RT-OBJ-instruction-modules](runtime.md#rt-obj-instruction-modules); it is an input/output store on [RT-RTE-capture-file](runtime.md#rt-rte-capture-file), not operating guidance. SRC-1, `_inbox/README.md`, `_meta/instructions/general.md`, `assets/clipper-template.json`.

> Override signal: "just park this" = park raw, no commentary.
> --- `_meta/instructions/general.md`

> Inbox items are meant to be **temporary**. After 7 days, your AI will surface them for triage at the start of a session - but it will never delete them without asking you. The 7-day mark is a nudge, not a deadline.
> --- `_inbox/README.md`

Age-based startup triage later consumes filenames/dates and may initiate filing; clip triage reads intent/content. Draft denotes review need, not enforced unreadability. The seven-day rule conflicts with the source archive README's automatic-discard wording; see Integration issues.

#### MEM-OBJ-sources
Label: Preserved source originals

Source-native identity: `_sources/`; storage: local original-format files, including Markdown or PDFs, intended to travel in Git; form: source-dependent, readable text or an opaque original requiring an external parser. Lineage: original inbox source moved after working knowledge is extracted, conditional on configuration and model judgment of importance. This is not the article's regenerated body. Distinct from [RT-OBJ-instruction-modules](runtime.md#rt-obj-instruction-modules); it supplies optional lineage retention on [RT-RTE-capture-file](runtime.md#rt-rte-capture-file). SRC-1, `_sources/README.md`, `_meta/instructions/agent-write.md`.

> Sources here are **immutable** - they're reference copies, not working documents
> --- `_sources/README.md`

> **If set to `no` (default):** Discard inbox items normally after filing. No source preservation.
> --- `_meta/instructions/agent-write.md`

Immutability is a policy, not filesystem enforcement. A documented reprocessing role affords later consumption, but no installed re-ingestion caller or automatic source-to-working-copy link/revalidation mechanism is specified in these paths. Importance is selected by the assistant after enabling the setting, not individually approved merely by changing the toggle. Discarding originals prevents guaranteed reconstruction of extraction decisions.

#### MEM-OBJ-knowledge
Label: Working knowledge and project content

Source-native identity: working files in `2-Knowledge/`, `1-Projects/`, `3-Journal/`, and `4-Private/`, plus user-established content areas. Storage: filesystem Markdown and linked artifacts; ordinary tracked content can persist in Git, journal/private bodies are ignored by default. Form: natural-language articles, plans, meeting/journal notes and project overviews; embedded code/artifacts are source-dependent and do not acquire executable authority just by inclusion. Lineage: captures, source extraction, human edits and optionally saved query syntheses. Decision records have a separate rationale/outcome consumer in [MEM-OBJ-decision](#mem-obj-decision). Distinct from [RT-OBJ-instruction-modules](runtime.md#rt-obj-instruction-modules); these are content inputs to [RT-RTE-knowledge-query](runtime.md#rt-rte-knowledge-query), not instructions by default. SRC-1, `_meta/instructions/general.md`, `1-Projects/README.md`, `_meta/instructions/agent-write.md`, `.gitignore`.

> Each project gets a folder. Everything related to it lives there — design docs, decisions, architecture, plans, notes. The actual work product goes wherever it belongs when shipped, but the thinking stays here.
> --- `1-Projects/README.md`

> 3. **Never file the full raw HTML content** as-is — extract what matters, discard the rest.
> --- `_meta/instructions/general.md`

Later query synthesis treats content as evidence, not inherently as operating policy. Freshness/citations constrain the requested answer without verifying factual trust. Private writes require human judgment under agent-write; gitignore alone does not prevent AI reads or public disclosure. Optional journal sync recipes change persistence to plain Git, encrypted Git with unlocked local text, or externally synchronized files: actual encryption, key custody and sync behavior remain external/uninspected (SRC-1, `docs/journal-sync.md`; supplied boundary plus bounded source search).

Blog content is another user-established working-content type: review may be self or peer, then publication updates `status: published` and retains URLs. This is a specialized write/check path, not a new memory engine; external platforms and a later analytics consumer are uninspected (SRC-1, `_meta/instructions/blog-posts/instructions.md`). Throwaway `_output/` exports instead have explicitly non-query intent and default Git exclusion, so generating an export alone does not establish memory read-back (SRC-1, `_output/README.md`).

#### MEM-OBJ-decision
Label: Decision rationale and outcomes

Source-native identity: decision records shaped by `_meta/templates/decision.md` in `2-Knowledge/Decisions/`. Storage: Markdown, normally Git-versionable. Form: natural-language context, options, rationale, rejected alternatives, outcome status/observations and discovered constraints. Lineage: initial user/assistant decision documentation plus later outcome reporting; no automatic environment measurement or mandatory outcome-writing schedule is provided by this template. Distinct from [RT-OBJ-instruction-modules](runtime.md#rt-obj-instruction-modules); this is the specific outcome-bearing input to [RT-RTE-knowledge-query](runtime.md#rt-rte-knowledge-query). SRC-1, `_meta/templates/decision.md`, `_meta/instructions/knowledge-query.md`.

> <!-- Fill this in AFTER the decision has played out — weeks or months later. -->
> <!-- This is what makes decisions compound: future decisions learn from past outcomes. -->
> --- `_meta/templates/decision.md`

> 4. **Include failure constraints** — Past decisions that failed or had mixed outcomes are especially valuable. Their "Constraints Discovered" sections should actively inform the new decision.
> --- `_meta/instructions/knowledge-query.md`

This route preserves reasons where filled in and explicitly asks a later assistant to read outcome/constraint content for a new decision. A pending or empty outcome does not establish experience. Recorded outcomes are reports, not an independent answer oracle; model-selected relevance and user decisions remain distinct. The “learning” label establishes intent to reuse experience, not improved future capacity or demonstrated attribution.

#### MEM-OBJ-metadata
Label: Metadata and navigation summaries

Source-native identity: document frontmatter and directory/project README indexes. Storage: text beside or linking to content; form: natural-language summary/status/failure explanation and localized YAML/path/date syntax. YAML can have symbolic consumers such as Obsidian Properties, but the query assistant semantically interprets summary/tags and does not use an inspected fixed parser. Lineage: author/assistant creates or revises metadata with content; general instructions refresh project index rows and meaningful personal README changes. No counterpart after comparison with [RT-OBJ-instruction-modules](runtime.md#rt-obj-instruction-modules): metadata is content access state, not an instruction module. SRC-1, `_config/standard.md`, `_meta/instructions/general.md`.

> **Summary** — One sentence, present tense, describing what the file contains OR its current state. This is the most important field — a future query will use it to decide relevance without reading the whole file.
> --- `_config/standard.md`

> **Failure_reason** — Required when `status: archived` or `status: superseded`. One sentence explaining why the file was retired or replaced. Prevents "ghost" archived pages with no explanation.
> --- `_config/standard.md`

Summaries are selection proxies, not necessarily complete content. Status/date affect reliance through warnings/deprioritization. Failure reasons may retain withdrawal rationale, but the query protocol does not explicitly guarantee reading that field in every historical query. Migration can replace metadata mechanically without inspecting truth, source quality or completion. The canonical YAML standard and older bold-field search wording coexist; this is a prompt ambiguity, not a demonstrated retrieval failure.

#### MEM-OBJ-logs
Label: Operation and structural logs

Source-native identity: `2-Knowledge/log.md`, `WIKI-LOG.md`, `.last-optimization-review`, and optional `/tmp/claude-wiki-reads-${SESSION_ID}.log` recipe. Storage: Markdown operation/structure logs and plain date/read-path files; `/tmp` read logs are host-local and lack a guaranteed cross-session retention contract. Form: natural-language descriptions plus dates/path strings, not raw conversation or model-state checkpoints. Lineage: assistant's selected operation summaries, review timestamp, or a proposed host hook copying read paths. Distinct from [RT-OBJ-instruction-modules](runtime.md#rt-obj-instruction-modules); these record operations rather than policy, and the training observation log is separately [MEM-OBJ-config](#mem-obj-config). SRC-1, `2-Knowledge/log.md`, `WIKI-LOG.md`, `_meta/instructions/optimization-review.md`, `docs/claude-code-setup.md`.

> Append-only. One line per operation. Never edit existing lines.
> --- `2-Knowledge/log.md`

> Each entry captures what changed and why.
> --- `WIKI-LOG.md`

Current-status queries can route to WIKI-LOG; lint/optimization use the review date for cadence. No instruction in the inspected read-log recipe automatically derives policy from its path list. The knowledge log affords provenance inspection, but a general log-to-improvement consumer is not established. These logs must not all be conflated with the conversation-fed behavioral update route.

### Routes

#### MEM-RTE-pattern-capture
Label: Conversation pattern capture

Endpoints: newly established rule/preference or observed usage pattern → foreground assistant selects a destination → immediate retained edit → later startup/task reads. This write-side route is distinct from the bootstrap/consumer side in [RT-BAP-instruction-load](runtime.md#rt-bap-instruction-load) and from new-content filing in [RT-RTE-capture-file](runtime.md#rt-rte-capture-file); it spans config, personal context and modules, rather than being part of one supplied route. Owner: foreground assistant interprets conversation; human supplies statements, may correct or decline proposed conventions/templates/directories, and is asked when capture worth is ambiguous. Physical writes remain host tools. Open conversational adaptation is the mode, not a bounded experimental curriculum. No expected-answer oracle is specified. SRC-1, `_meta/instructions/general.md`, `_config/config.md`.

> **The signal to act:** any time a conversation produces a rule, a preference, a "we decided to always...", or a "from now on..." — that's a pattern. Write it before moving on.
> --- `_meta/instructions/general.md`

> If it's ambiguous whether something is worth capturing, ask: *"We worked out [X] — should I add that to the instructions?"* Then capture it in the same exchange, not at the end of the session.
> --- `_meta/instructions/general.md`

- Immediate return: Current conversational response plus proposed or acknowledged retained edit; no separate software return contract.
- Later read-back: Future sessions read config/context/general, and task-triggered reads load changed modules/templates; routing tables and indexes can change what future queries select.
- Delegated visibility: inapplicable — no delegated agent is prescribed in this route.
- Selection predicate: Assistant judges a conversational rule, preference, purpose/structure shift or recurring usage pattern; thresholds depend on training phase and user pushback.
- Invalidation or expiry: Later corrections replace current guidance; cooldown stops Training Log growth but does not delete it. No automatic expiry of context facts or rules is specified.
- Activation or effect: Prescribed filesystem edits and requested future personalization/convention changes; exercised behavior is uninspected.
- Evidence limits: No conversation trace, admission episode or dependent later operation is supplied; reasons/raw turns need not be retained.
- design conclusion status: claimed
- operation conclusion status: uninspected

Admission is not identical across outputs: clear newly established rules/preferences trigger immediate writes; ambiguous capture prompts a question; directory creation follows approval; template changes are suggested when usage differs. User rejection of directories reduces suggestions immediately. Recovery is subsequent file editing or available Git history for committed material, not automatic rollback. Guidance says preserve discoveries before they can be lost, adapt to actual use and respect user pace; products are textual instructions, preferences, templates and structure, not changed weights.

Trace chain: live user/assistant exchange and usage observations → selected derived rule/fact/log entry → durable file → later assistant read. This supports a prescribed trace-fed behavior-shaping write, separate from raw transcript retention. Rationale is not mandatory for each preference/rule; the Training Log may retain a short reason, but the consumer is not guaranteed the original exchange. Addressability is file/section/text-level; scope and reasoning completeness vary. Persistence horizon is intended across sessions.

Theory-builder conditions 1–4: condition 1 conclusion status: afforded — an entire written convention or rule is localized and revisable; condition 2 conclusion status: claimed — future sessions are asked to apply learned conventions; condition 3 conclusion status: uninspected — user pushback is accommodated, but no supplied episode codifies a challenged explanatory claim, blame and resulting revision; condition 4 conclusion status: claimed — retained results and later corrections are prescribed, not an observed criticism-fed cycle. Learning: improved capacity uninspected. Reflection: usage observations may revise the template's own behavior representation, which later startup is asked to consume; exercised two-way causation uninspected. Reflective theory builder and autonomous theory builder: uninspected; explicit user approval contributes to some internal updates. Self-improvement boundary is personal-instance behavior-determining text across later sessions, objective adaptation to user needs. Only an improvement-directed dispositional path is claimed: evidence-shaped determination, installed changes and later causal dependence are not demonstrated by a run, and successful improvement is uninspected.

#### MEM-RTE-lint-maintenance
Label: Lint and content maintenance

Endpoints: user/cadence request → assistant loads lint/completion guidance and inspects files → report/nudges → selected content/metadata/lifecycle changes → retained files and logs → later query/startup selection. Distinct from [RT-RTE-context-review](runtime.md#rt-rte-context-review), which restructures instruction loading with explicit approval, and [RT-RTE-capture-file](runtime.md#rt-rte-capture-file), which admits new captures. Owner: assistant diagnoses/proposes under textual criteria; user can reject deletion/overwrite and choose triage disposition. Completion wording sometimes asks before changing status and sometimes directs marking complete when checks pass; no universal per-change approval is established. Mode: open/event-triggered maintenance, monthly recommended; oracle: none independent of assistant assessment. SRC-1, `_meta/instructions/knowledge-lint.md`, `_meta/instructions/definition-of-done.md`, `_config/standard.md`, `_inbox/README.md`.

> **Exemptions:** Files with `status: archived` or `status: superseded` are exempt — terminal-status pages are intentionally frozen and should not be flagged as stale. Only flag `active` files.
> --- `_meta/instructions/knowledge-lint.md`

> 1. Status updated to Active/Complete
> 2. Filed in the correct directory
> 3. Wiki log updated if it's a significant addition
> --- `_meta/instructions/definition-of-done.md`

- Immediate return: Seven-check lint report or completion/filing suggestion, with operation/structural log entries requested.
- Later read-back: Changed summaries, tags, links, filenames, dates, statuses and project indexes affect future lookup; archived content remains available to historical queries. Review date can prompt context optimization.
- Delegated visibility: inapplicable — no separate validator/reviewer agent is prescribed.
- Selection predicate: Inbox age >7 days, metadata `type:` presence in first 20 lines in selected roots, active age >90 days, inbound links, instruction size/review date, filename and link checks; completion uses type-specific checklists.
- Invalidation or expiry: Archive/supersede removes active-staleness checks and usually reduces query priority, not all access. Inbox age prompts triage without automatic deletion. Project completion moves folders to `_SHIPPED/` and removes active rows.
- Activation or effect: Prescribed reports and accepted edits; later selection effects are requested, not observed.
- Evidence limits: Natural-language checklists cannot establish full YAML compliance or factual accuracy; link conventions conflict and rename/backlink atomicity is not guaranteed.
- design conclusion status: claimed
- operation conclusion status: uninspected

Proposals are shaped by findability, freshness, accurate/useful completion and context size. Rejection can leave drafts/inbox unchanged; withdrawal should retain `failure_reason` for archived/superseded content, not erase it. Deleting originals and rewriting existing files have user-control restrictions, with capture/source-specific exceptions discussed above. Recovery is manual editing/Git where available. No independent evaluator, automatic rollback or expected-output comparator is shipped in these instructions. Cleanup output persists as metadata/content/index edits and summaries, not merely a report if acted on. Reports/logs alone do not establish corrected knowledge. SRC-1, `_meta/instructions/agent-write.md`, `_meta/instructions/general.md`, `_meta/instructions/knowledge-lint.md`.

#### MEM-RTE-compact-reload
Label: Compaction sentinel reload

Endpoints: host manual compaction → proposed PostCompact hook writes `/tmp/wiki-post-compact` → next UserPromptSubmit hook removes sentinel and injects re-init text → assistant rereads startup files. Distinct from [RT-RTE-session-start](runtime.md#rt-rte-session-start): this is the optional invalidation/reload trigger around an opaque host compactor, not the startup progression itself. Owner: user triggers manual compact; host decides compression; recipe commands manage sentinel; assistant owns rereading. Context effects: conversation removed/transformed by external host; retained wiki files remain reachable on disk. SRC-1, `docs/claude-code-setup.md`.

> When you run `/compact`, Claude Code compresses the conversation context. Without intervention, the next response won't know it needs to re-run the session start protocol.
> --- `docs/claude-code-setup.md`

> The sentinel pattern is the correct workaround.
> --- `docs/claude-code-setup.md`

- Immediate return: Proposed PostCompact notification, then an additional-context instruction on the next user prompt; not restoration of discarded text.
- Later read-back: Re-init asks the assistant to reload current config/general/context and phase-selected startup material, including use-derived edits where present.
- Delegated visibility: inapplicable — no isolated worker/frame is part of this recipe.
- Selection predicate: PostCompact matcher `manual`; next user prompt tests sentinel presence; startup phase determines reread files. No token budget or host summary selector is disclosed.
- Invalidation or expiry: Consumed sentinel is removed; original file state stays reachable. `/tmp` lifetime and hook installation are deployment-dependent.
- Activation or effect: Documented reload affordance contingent on installation and compliance; no installed hook or exercised reload supplied.
- Evidence limits: Raw transcript-to-summary transformation, summary persistence/checkpoints, retained tail and actual host hook semantics are outside the frozen implementation; unsaved discoveries are not reconstructed by this recipe.
- design conclusion status: afforded
- deployment conclusion status: uninspected

This is working-context removal/reload, not evidence of a target-owned automatic trace-to-derived memory writer. If a host-produced summary reaches a later invocation, it could constitute retained within-session memory, but its payload, reasons and consumer behavior remain opaque here. The sentinel is symbolic reload-control state, not a readable display of the summary. Startup rereads are instruction/fact supply, not a reference-counted memory heap or a separate-context stack frame. Text must be read back into context by value.

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-linked-context
Label: Linked code context

Consumer: an external assistant working in a linked code repository. Channel: documented multi-root workspace plus code-root `CLAUDE.md`/`.cursorrules` pointing to wiki architectural decisions and context. Force: offered background/evidence and requested source-of-truth consultation, dependent on external discovery/reads; not repository-enforced authority. Horizon: fresh sessions and tasks in linked projects. This is distinct from [RT-BAP-instruction-load](runtime.md#rt-bap-instruction-load), whose consumer operates the wiki through its own bootstrap. SRC-1, `docs/linked-code-repos.md`.

> The code repo also gets a context file that explains how it fits into the larger system — something that would otherwise get lost every time you open a fresh session.
> --- `docs/linked-code-repos.md`

The route is a documented external-consumer affordance, not merely a storage API with a hypothetical caller. No scaffold implementation, actual workspace, installed code-root pointer or dependent run is supplied. The source's “full wiki context” claim exceeds guaranteed window contents: root inclusion and a pointer do not prove all content is loaded.

## Annotations

#### On [RT-OBJ-instruction-modules](runtime.md#rt-obj-instruction-modules)

Retained-use lineage matters: shipped modules are static guidance initially; immediate conversation-derived rule edits and approved optimization products can make their current bodies retained behavioral memory. The later consumer reads actual file text, not a stored learning score. Policy authority depends on delivery and interpretation. Reasons for an added rule are not universally required. Templates have a related but distinct consumer: future writing loads their current shape; user usage can prompt template revisions. SRC-1, `_meta/instructions/general.md`, `_meta/instructions/optimization-review.md`; the runtime record and [RT-BAP-instruction-load](runtime.md#rt-bap-instruction-load) supply the minimum policy passages.

#### On [RT-RTE-session-start](runtime.md#rt-rte-session-start)

Memory consumers: future foreground assistant reads current profile, learned conventions, Training Log and personal context. Phase/date/manual override inputs choose what to load and how actively to ask; training history guides nonrepeated tips and questions. Budget: no enforced tokens, but phase removes README/philosophy bodies and general routing avoids loading every module. Disk files remain reachable; skipped content is not automatically available by pointer. Framework mode blocks personal retention rather than merely changing a retrieval budget. Actual personalized behavior remains unobserved. SRC-1, `_config/config.md`, `_meta/instructions/general.md`; see [MEM-OBJ-config](#mem-obj-config) and [MEM-OBJ-context](#mem-obj-context).

> **Load instructions just-in-time** — don't read all instruction modules at startup. Load them only when triggered (see the routing table in `_meta/instructions/general.md`). This keeps context windows small as the wiki grows.
> --- `_config/config.md`

#### On [RT-RTE-capture-file](runtime.md#rt-rte-capture-file)

Raw-to-derived lineage: source/user input → inbox draft or clip → intent-directed extraction/working content → optional preserved original → future query. Regular idea capture may add a model first take; “just park this” preserves raw input. “Read later” clips stay in inbox, knowledge clips become extracted articles, project clips are filed/linked, draft sources can become preserved originals or extracted quotes. Origin/intent and agent attribution are cues, not authenticity checks. Retained reasons are optional outside dedicated decision shapes. SRC-1, `_meta/instructions/general.md`, `_meta/instructions/agent-write.md`.

Independent admission: the external clipper is configured to create dated `_inbox` notes, with a user-filled intent line and legacy bold metadata. User initiation/editing is distinct from model extraction and later filing approval; actual clipper execution is uninspected (SRC-1, `assets/clipper-template.json`). Obsidian new-file/daily-note paths afford human-authored inbox/journal writes outside agent admission. Daily notes select a journal template and `YYYY-MM-DD` name with `autorun: false`; these are configuration, not observed notes (SRC-1, `.obsidian/daily-notes.json`; supplied boundary covers `.obsidian/app.json`).

#### On [RT-RTE-knowledge-query](runtime.md#rt-rte-knowledge-query)

Ordinary read-back is user-requested retrieval; decision-context read-back proactively selects domain/topic-matching past outcomes without a separate request to retrieve precedents. Both selectors are the foreground assistant, consuming summaries/tags/indexes then bodies. The decision path specifically selects filled Outcome/Constraints content, not just filenames. Delivery is cited synthesis into the current conversation; retention of that synthesis needs a later save/write, and logs alone are not the synthesis. Query budget is 1–3 files, with a first-section reduction beyond 500 lines; no token budget, complete-corpus guarantee or embedding ranking is shipped. Status/date shape priority and warnings. SRC-1, `_meta/instructions/knowledge-query.md`, `_config/standard.md`; minimum passages are in the runtime record and [MEM-OBJ-decision](#mem-obj-decision).

#### On [RT-RTE-context-review](runtime.md#rt-rte-context-review)

The retained products are revised operating text, `.last-optimization-review` date and a WIKI-LOG description. The timestamp influences future review cadence; changed module text influences future loaded policy. Optional read-path logs can inform an operator, but no automatic pipeline from that log into accepted instruction edits is wired. Reasons may be summarized in the review log; neither a complete rejected-proposal archive nor guaranteed future rationale reading is required. Source metrics are file line counts and perceived repeated reads/slowness, not measured model token counts or causal benefit. SRC-1, `_meta/instructions/optimization-review.md`, `docs/claude-code-setup.md`; the runtime record supplies approval and theory-account evidence.

#### On [RT-RTE-metadata-migrate](runtime.md#rt-rte-metadata-migrate)

The later memory consumer receives rebuilt frontmatter/title/body, not original bytes. Code takes the first H1, gathers contiguous matching legacy bullet fields, emits fixed-order YAML plus extra fields, and rebuilds from that title onward; preceding material is omitted. Leading `---` causes a skip irrespective of semantic validity. The clipper's non-bullet, no-H1 metadata shape does not match this converter's admission pattern, so migration is not a guaranteed repair for clips. No backup/semantic validation precedes overwrite; errors do not reverse earlier conversions. This is deterministic representational curation, not experiential model learning. SRC-1, `migrate-to-yaml-frontmatter.py`, `assets/clipper-template.json`; the runtime record supplies the write quote.

## Write side

[RT-RTE-capture-file](runtime.md#rt-rte-capture-file) and its annotation cover user/clip acquisition, draft authorship and extracted working copies. User-supplied material and model-derived takes have different lineage even when co-stored. Source preservation is selectively enabled, judged by the model and calibrated with the user; “immutable original” is requested maintenance discipline, not an enforced property. Ordinary filing offers human disposition, but explicit destination writes and immediate pattern capture prevent a universal approval claim.

[MEM-RTE-pattern-capture](#mem-rte-pattern-capture) is the conversation-fed behavioral write. It retains selected observations as preferences, conventions, instructions, templates and structure. It does not retain every raw turn or every reason. Outcome-fed decision consumption is separate: [MEM-OBJ-decision](#mem-obj-decision) supplies fields for later observation/rationale updates, but does not itself instrument real outcomes. Raw transcripts retained by an external host are outside the target, and [MEM-RTE-compact-reload](#mem-rte-compact-reload) cannot establish their summary transformation or alternative checkpoint forms.

Evaluation/admission is procedural. [MEM-RTE-lint-maintenance](#mem-rte-lint-maintenance) distinguishes completion criteria, metadata/lifecycle cleanup and withdrawal from factual validation; [RT-RTE-context-review](runtime.md#rt-rte-context-review) separately gates instruction restructuring on approval. Rejected structural suggestions change future suggestion thresholds; rejected optimization proposals need not become edits. Archive/supersede retains explanation and reference access, while project shipping updates indexes/folders. No universal removal propagator or automatic source-retraction cascade is established in these inspected instructions.

Finally, [RT-RTE-metadata-migrate](runtime.md#rt-rte-metadata-migrate) writes mechanically under caller-selected scope. It is neither authored by the model at runtime nor admitted by the content review procedure. File mutation, content authorship and human content approval must not be collapsed.

## Read-back

Startup is repeated file supply under [RT-RTE-session-start](runtime.md#rt-rte-session-start), not autonomous surveillance. A new user session triggers prescribed reads, where profile/context/current rules reach the foreground assistant with policy/personalization authority. Task loading selects additional instruction bodies and templates. Phase control preferentially keeps irrelevant static bodies out; it does not create an isolated worker context or preserve the old model window.

Question answering under [RT-RTE-knowledge-query](runtime.md#rt-rte-knowledge-query) is selective content retrieval for synthesis. Directory indexes, summary/tags, type and freshness reduce reads; archived historical material can still be selected. A decision trigger affords proactive precedent delivery, with domain/topic and completed outcome as actual targeting inputs. Failure constraints are requested to shape the next decision. None of these instructions proves that a later answer used all relevant context, that an outcome was verified, or that capacity improved.

The optional compaction recipe reinjects an instruction to reload durable files rather than restoring conversation reasons. The linked-code documentation supplies a separate external consumer role via [MEM-BAP-linked-context](#mem-bap-linked-context). Preserved originals afford later manual/model reprocessing, but storage and documented purpose do not establish installed re-ingestion wiring. Logs have narrower consumers: WIKI-LOG can answer current-status queries and a review date triggers cadence; the read-path and knowledge-operation logs do not establish an automatic learned-policy producer.

## Integration issues

- **Contradictory discard timing:** SRC-1, `_sources/README.md`, says an original inbox capture “gets discarded after 7 days,” whereas `_inbox/README.md` explicitly says seven days is a nudge and deletion requires asking. Agent-write ties default discard to filing. Preserve the conflict as documentation, not an automatic TTL deletion route. Concerns [MEM-OBJ-inbox](#mem-obj-inbox), [MEM-OBJ-sources](#mem-obj-sources), [RT-RTE-capture-file](runtime.md#rt-rte-capture-file). The runtime's narrower filing-discard account is supported; no correction to that finding is required.

> When you ingest a source (an article, a PDF, a clipped web page), the knowledge gets extracted into your wiki and the original in `_inbox/` gets discarded after 7 days. That's the default - most originals aren't worth keeping.
> --- `_sources/README.md`

- **Metadata and link instruction conflicts:** YAML summaries/status coexist with query's older bold-field search wording; standard says CommonMark Markdown links while lint check 7 requests Obsidian wikilinks and orphan check 4 searches Markdown links. Thus cleanup can produce links its own orphan test does not recognize. This prevents claiming consistently enforced discoverability, not the afforded selection routes. Concerns [MEM-OBJ-metadata](#mem-obj-metadata), [MEM-RTE-lint-maintenance](#mem-rte-lint-maintenance), [RT-RTE-knowledge-query](runtime.md#rt-rte-knowledge-query). SRC-1, `_config/standard.md`, `_meta/instructions/knowledge-query.md`, `_meta/instructions/knowledge-lint.md`.

> **How:** Check if each scanned file appears in any other file as a markdown link `[text](path)`.
> --- `_meta/instructions/knowledge-lint.md`

> - Wrap in `[[` and `]]`
> --- `_meta/instructions/knowledge-lint.md`

- **Specialized lifecycle vocabulary:** Blog publishing prescribes `status: published`, absent from the canonical lifecycle list. This is a specialized instruction discrepancy; it does not establish published files become unreadable or automatically invalid. Concerns [MEM-OBJ-knowledge](#mem-obj-knowledge), [MEM-OBJ-metadata](#mem-obj-metadata). SRC-1, `_meta/instructions/blog-posts/instructions.md`, `_config/standard.md`.

> 3. **Publish** — Post to the primary platform. Update `status: published` and the `updated` date in frontmatter.
> --- `_meta/instructions/blog-posts/instructions.md`

- **Opaque/external alternatives:** Host compact summary/raw-tail/checkpoint contents and actual hook deployment remain unknown; journal encryption/sync and linked-code context deployment are recipes only. These prevent payload lineage and activation conclusions for [MEM-RTE-compact-reload](#mem-rte-compact-reload), [MEM-OBJ-knowledge](#mem-obj-knowledge), [MEM-BAP-linked-context](#mem-bap-linked-context), not known file-retention/control findings. Sources: SRC-1, `docs/claude-code-setup.md`, `docs/journal-sync.md`, `docs/linked-code-repos.md`.
- **Duplicate review:** No new declaration replaces a supplied referent. Module, session, capture, query, optimization and converter memory fields annotate their runtime declarations. The pattern-capture write route overlaps the runtime instruction-load behavioral-authority path but has distinct write-side endpoints and multiple retained destinations; compact-reload adds a trigger outside startup; lint adds content-maintenance operations outside instruction optimization. Object records cover retained parts that runtime did not declare. No supported supplied-fact correction is needed; the added source contradictions and local unknowns above should remain visible in reconciliation.

## Limitations and checks

The source identity, full commit and clean checkout were rechecked before analysis. The member identity matches the supplied boundary/run. Required inputs and their trailing blank ranges were read completely. Direct inspected paths and reliance on supplied findings are differentiated in the coverage table; no prohibited prior characterization was consulted. No target tests, hooks, converter, model call or synchronization service was run.

Doctrine establishes requested behavior and some documented consumer affordances, not reliable compliance, deployed wiring or causally improved action. Lack of filled user data prevents retrieval/fact-quality assessment and actual pattern/outcome lineage. External compaction, transcript history, host memory and synchronization opacity prevent complete hidden-state inventory; they do not erase the known file-based learning-intent routes.

Validation: the required `commonplace-run validate-output` check passed: “Member content check passes; invocation residue not checked. This is not job acceptance or claim support.” This establishes deterministic member form and quotation checks only.
