---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "llm-wiki: source fidelity, synthesis, semantic-check proxies and authority granted to retained pages"
run-id: AAS-2026-10-16-llm-wiki-6786c5985cdc-01
reviewed-boundary: b1088890ee0743810a92577aecad946c6b3eb2d2
---

# llm-wiki epistemic report

## Source-and-claim boundary

The question is how session-derived propositions become reusable wiki content, what checks license reliance, and whether rejection or staleness constrains later consumers. Scope, exclusions and evidence identity: see [boundary](boundary.md#boundary-and-evidence) and its [Source register](boundary.md#source-register). SRC-1 supplies implementation and doctrine/design, not observed runs or causal experiments. The external foreground agent and model services are excluded implementations, not omitted shipped procedures.

Public/design claims assessed here are [RT-CLM-history-compilation](runtime.md#rt-clm-history-compilation), [RT-CLM-append-preservation](runtime.md#rt-clm-append-preservation), [EPI-CLM-source-fidelity](#epi-clm-source-fidelity), [EPI-CLM-semantic-checks](#epi-clm-semantic-checks), [EPI-CLM-lifecycle-states](#epi-clm-lifecycle-states) and [EPI-CLM-candidate-trust](#epi-clm-candidate-trust).

| Entry point or operation | SRC-1 source path | Coverage and records / prevented conclusion |
|---|---|---|
| CLI conversion, adapters, raw guard | `llmwiki/cli.py`, `llmwiki/convert.py` | Supplied [RT-RTE-session-conversion](runtime.md#rt-rte-session-conversion); adapter-specific bodies not independently traced here: no complete semantic-preservation conclusion. |
| CLI backend synthesis, pending completion, override | `llmwiki/synth/pipeline.py`, `llmwiki/synth/agent_delegate.py` | Supplied [RT-RTE-backend-synthesis](runtime.md#rt-rte-backend-synthesis), [RT-RTE-agent-completion](runtime.md#rt-rte-agent-completion); direct reads of `llmwiki/synth/base.py` and `llmwiki/synth/prompts/source_page.md` add deterministic example and fidelity doctrine. |
| Host ingest/query | `CLAUDE.md` | Direct workflow read plus supplied [RT-RTE-host-ingest](runtime.md#rt-rte-host-ingest); host compliance unavailable. |
| CLI lint and rule registration | `llmwiki/cli.py`, `llmwiki/lint/__init__.py`, `llmwiki/lint/rules/__init__.py` | Direct dispatch/runner reads; [EPI-RTE-semantic-proxies](#epi-rte-semantic-proxies), [EPI-RTE-lint-return](#epi-rte-lint-return). Individual remaining structural rules not fully audited; no system-complete absence of other checks. |
| Freshness and lifecycle/confidence helpers | `llmwiki/lint/rules/content_freshness.py`, `llmwiki/confidence.py`, `llmwiki/lifecycle.py` | Direct full reads and caller-name search under `llmwiki/`; [EPI-RTE-freshness-check](#epi-rte-freshness-check), [EPI-RTE-lifecycle-helper](#epi-rte-lifecycle-helper). |
| MCP registered operations | `llmwiki/mcp/server.py` | Searched handlers; directly read query/snippet, lint, confidence, lifecycle, dashboard and entity-search handlers. [RT-RTE-mcp-access](runtime.md#rt-rte-mcp-access), [EPI-RTE-metadata-selection](#epi-rte-metadata-selection). Search, category browse, exports and source listing not independently traced end-to-end; no universal selection/correctness verdict. |
| Candidate promote/merge/discard | `llmwiki/candidates.py`, `.claude/commands/wiki-candidates.md` | Supplied [RT-RTE-candidate-admission](runtime.md#rt-rte-candidate-admission), direct procedure read; no observed reviewer evidence. |
| Update, reflection, verification | `.claude/commands/wiki-update.md`, `.claude/commands/wiki-reflect.md`, `.kiro/steering/verification-rules.md` | Direct full reads; [EPI-RTE-page-update](#epi-rte-page-update), [EPI-RTE-wiki-reflection](#epi-rte-wiki-reflection). |
| Plugin hooks/registration | `.claude-plugin/plugin.json` | Direct full read; SessionStart registration names absent `hooks/session-start.sh` per supplied boundary. No hook execution attributable to target. |
| Reader build, optional Claude, exports | `llmwiki/build.py`, `llmwiki/pipeline.py` | Supplied [RT-RTE-reader-build](runtime.md#rt-rte-reader-build); direct correction reads of `synthesize_overview`, its build call and `render_index` establish the separate [EPI-OBJ-reader-overview](#epi-obj-reader-overview) output. No independent publication semantic audit. |
| Editor, repair, self-learn, CI/test and deployment variants | `integrations/`, `scripts/`, `.github/`, `tests/`, `.claude/skills/` | Boundary inventories these; not exhaustively inspected here. Prevents exhaustive assertions about every evaluator, correction route, or system-wide self-improvement. |

Added source reads are at SRC-1's frozen pin. No target execution, provider calls or tests were performed. Missing corpus/provenance traces prevent determining actual proposition fidelity, exercised acceptance and downstream answer dependence. Missing comparison evidence prevents causal benefit claims. Available but unread paths above are inspection limits, not access gaps.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-raw-sessions](#epi-obj-raw-sessions) | Session utterances, code and reported outcomes, each with local scope | Acquired source material | see record | Transcript evidence that a claim was said is not evidence that the claim is true. |
| [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages) | Summaries, facts, comparisons, contradictions and saved answers | Reusable knowledge | see record | Actual generated propositions and fidelity not supplied. |
| [EPI-OBJ-reader-overview](#epi-obj-reader-overview) | Optional prose about projects and activity inferred from grouped metadata | Reader landing-page overview, not curated wiki content | see record | No supplied output or proposition verification; separate reader consumer lineage. |
| [RT-OBJ-source-page](runtime.md#rt-obj-source-page) | None as task instruction; requests falsifiable claims | Synthesis guidance | see record | Not an evaluator or truth certificate. |
| [RT-OBJ-pending-prompts](runtime.md#rt-obj-pending-prompts) | Rendered source excerpt; UUID itself is not a substantive claim | Deferred work and association | see record | Matching identity does not check generated content. |
| [EPI-OBJ-quality-metadata](#epi-obj-quality-metadata) | Numeric confidence and lifecycle/status assertions | Quality labels and selectors | see record | Labels and scores do not establish proposition truth or actual review. |
| [EPI-OBJ-lint-issues](#epi-obj-lint-issues) | Assertions about page structure/date or skipped checks | Review cues / command result input | see record | Domain is the implemented predicate, not general semantic correctness. |

Opaque parametric components: see [RT-CMP-ollama](runtime.md#rt-cmp-ollama) and [RT-CMP-claude](runtime.md#rt-cmp-claude). No inspected request changes their parameters; exact weights and service-side mutability remain outside accessible evidence. Foreground-host parameters are likewise uninspected. This does not rule out retention-based changes to later context.

## Authority-route ledger

Fields owned by cited records are referenced rather than restated. These rows split checking, disposition and retention even where one supplied route contains several functions. All operation remains unobserved.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority | Behavioral-authority path | Evidence source ID and local anchor | Claim IDs | Mismatch marker | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-session-conversion](runtime.md#rt-rte-session-conversion) | content transformation | implemented | [EPI-OBJ-raw-sessions](#epi-obj-raw-sessions) | truth-apt transformation: acquisition/import | Native records to raw material | see route | see route | Acquired redacted/truncated transcript | File production | Source warrant unknown; omissions can degrade lineage/context | see route | see route | see route | [EPI-CLM-source-fidelity](#epi-clm-source-fidelity) | source-of-truth is scoped | No universal transcript preservation. |
| [RT-RTE-backend-synthesis](runtime.md#rt-rte-backend-synthesis) | content transformation | implemented | [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages) | truth-apt transformation: indeterminate | Model-produced source body | see route | see route | Candidate prose, dummy output or placeholder | Generation, not acceptance | Model semantics require actual input/output evidence | see route | see [RT-BAP-source-guidance](runtime.md#rt-bap-source-guidance) | see route | [RT-CLM-history-compilation](runtime.md#rt-clm-history-compilation) | none | No demonstrated entailment or non-entailment for unavailable model outputs. |
| [RT-RTE-backend-synthesis](runtime.md#rt-rte-backend-synthesis) | retention | implemented | [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages) | no content change | Returned body to file/index/state | see route | see route | Written page and synthesized counter | Permissive write | Retention supplies no acceptance warrant | Later consumers can read body | see route | see route | [EPI-CLM-source-fidelity](#epi-clm-source-fidelity) | retention before acceptance | No criterion-consuming acceptance shown. |
| [RT-RTE-agent-completion](runtime.md#rt-rte-agent-completion) | disposition/acceptance | implemented | [RT-OBJ-pending-prompts](runtime.md#rt-obj-pending-prompts) | no content change | UUID association and sentinel | see route | see route | Refusal or body replacement | Enforcing identity guard | Association only, not semantic acceptance | see route | see route | see route | [RT-CLM-append-preservation](runtime.md#rt-clm-append-preservation) | body preservation mismatch | No substantive truth check. |
| [RT-RTE-host-ingest](runtime.md#rt-rte-host-ingest) | other — ordinary ingest organization | doctrine only | [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages) | truth-apt transformation: indeterminate | Cross-linking and overview revision | see route | see route | Requested connected pages | Advisory host instructions | Connections do not prove prior acceptance; this is organization, not established post-acceptance integration | see route | see [RT-BAP-wiki-context](runtime.md#rt-bap-wiki-context) | see route | [RT-CLM-history-compilation](runtime.md#rt-clm-history-compilation) | acceptance unestablished | Host execution unavailable. |
| [RT-RTE-candidate-admission](runtime.md#rt-rte-candidate-admission) | disposition/acceptance | implemented | [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages) | no content change | Candidate promotion/merge/discard | see route | see route | Reviewed status or archive | Enforcing caller-selected file operation | Doctrine criterion: legitimate/nonduplicate, not exercised evidence-consuming acceptance | see route | see route | see route | [EPI-CLM-candidate-trust](#epi-clm-candidate-trust) | trust not retrieval isolation | Caller identity and review not verified. |
| [RT-RTE-mcp-access](runtime.md#rt-rte-mcp-access) | operational admission/selection/consumption | implemented | [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages) | truth-apt transformation: non-ampliative reshaping | Ranked page/snippet delivery | see route | see route | Lexical context | Ranking and delivery | Relevance score is not warrant | Host can consume returned text | see [RT-BAP-wiki-context](runtime.md#rt-bap-wiki-context) | SRC-1 `llmwiki/mcp/server.py` | [EPI-CLM-candidate-trust](#epi-clm-candidate-trust) | no lifecycle/status exclusion in query | Candidate/archive pages can match; semantic completeness not established. |
| [EPI-RTE-semantic-proxies](#epi-rte-semantic-proxies) | check/evidence production | implemented | [EPI-OBJ-lint-issues](#epi-obj-lint-issues) | no content change | see record | see record | see record | see record | Advisory issue production | Structural predicate only | see record | see record | see record | [EPI-CLM-semantic-checks](#epi-clm-semantic-checks) | advertised domain exceeds proxy | No semantic entailment check. |
| [EPI-RTE-freshness-check](#epi-rte-freshness-check) | check/evidence production | implemented | [EPI-OBJ-lint-issues](#epi-obj-lint-issues) | no content change | see record | see record | see record | see record | Advisory warning | Date-age predicate only | see record | see record | see record | [EPI-CLM-lifecycle-states](#epi-clm-lifecycle-states) | warning not withdrawal | No stale-read veto. |
| [EPI-RTE-lint-return](#epi-rte-lint-return) | disposition/acceptance | implemented | [EPI-OBJ-lint-issues](#epi-obj-lint-issues) | no content change | CLI exit | see record | see record | see record | Conditional exit failure | No page acceptance | see record | see record | see record | [EPI-CLM-semantic-checks](#epi-clm-semantic-checks) | success not semantic pass | Skips are info, not errors. |
| [EPI-RTE-lifecycle-helper](#epi-rte-lifecycle-helper) | check/evidence production | implemented | [EPI-OBJ-quality-metadata](#epi-obj-quality-metadata) | no content change | see record | see record | see record | see record | Return value / exception | Enum legality and heuristic score only | see record | see record | see record | [EPI-CLM-lifecycle-states](#epi-clm-lifecycle-states) | helper not automatic persistence | Operational consumer not found in caller search. |
| [EPI-RTE-metadata-selection](#epi-rte-metadata-selection) | operational admission/selection/consumption | implemented | [EPI-OBJ-quality-metadata](#epi-obj-quality-metadata) | no content change | see record | see record | see record | see record | Filtering/ranking/display | Metadata assertions remain unverified | see record | see record | see record | [EPI-CLM-lifecycle-states](#epi-clm-lifecycle-states) | labels not approval evidence | No score recomputation. |
| [EPI-RTE-page-update](#epi-rte-page-update) | content transformation | doctrine only | [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages) | truth-apt transformation: indeterminate | see record | see record | see record | see record | Host-interpreted instruction | Source reread requested; truth not guaranteed | see record | see record | see record | [EPI-CLM-source-fidelity](#epi-clm-source-fidelity) | none | No actual revision supplied. |
| [EPI-RTE-wiki-reflection](#epi-rte-wiki-reflection) | check/evidence production | doctrine only | [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages) | truth-apt transformation: indeterminate | see record | see record | see record | see record | Advisory proposals | Interpretations must be flagged | see record | see record | see record | none | none | No demonstrated criticism/revision iteration. |
| [RT-RTE-reader-build](runtime.md#rt-rte-reader-build) | content transformation | implemented | [EPI-OBJ-reader-overview](#epi-obj-reader-overview) | truth-apt transformation: indeterminate | Optional metadata-to-prose landing overview | see route | see route | Nonempty process stdout accepted | Permissive publication | Process success is not proposition verification | see route | see route | see route | [RT-CLM-history-compilation](runtime.md#rt-clm-history-compilation) | distinct synthesis route | Deterministic publication is separate from optional opaque prose semantics. |

Ordinary organization is requested without a preceding acceptance decision in the ingest sequence. SRC-1 `CLAUDE.md`:

> 8. **Cross-link** everything with `[[wikilinks]]` under `## Connections` on every page.
> --- `CLAUDE.md`

Deterministic witness, not target execution: [RT-RTE-backend-synthesis](runtime.md#rt-rte-backend-synthesis)'s dummy branch is narrower than the model branch. For raw body `Alpha\n\nBeta [[X]] [[X]]` and metadata project `ai-newsletter`, slug `s`, date `2026-01-01`, the inspected code selects `Alpha` as its first paragraph, deduplicates raw mentions to `X`, and emits `[[AiNewsletter]] — parent project` plus metadata claims. The first-paragraph and mention operations are non-ampliative reshaping; the project link is a naming-rule derivation, not verification that its target exists. A long first paragraph is cut at 500 characters and can lose a qualifier. Thus even deterministic text production is not uniformly a warranted summary. SRC-1 `llmwiki/synth/base.py`:

> first_para = raw_body.strip().split("\n\n")[0][:500] if raw_body else ""
> --- `llmwiki/synth/base.py`

> mentions = sorted(set(re.findall(r"\[\[([^\]]+)\]\]", raw_body)))
> --- `llmwiki/synth/base.py`

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-history-compilation](runtime.md#rt-clm-history-compilation) | see record | see record | Ingest and synthesis instructions | [RT-RTE-session-conversion](runtime.md#rt-rte-session-conversion), [RT-RTE-backend-synthesis](runtime.md#rt-rte-backend-synthesis) | None supplied | No intervention/comparison | File acquisition and candidate writing are supported architecture | Interlinked semantic correctness remains unobserved. |
| [EPI-CLM-source-fidelity](#epi-clm-source-fidelity) | see record | see record | Explicit traceability and contradiction rules | [RT-RTE-backend-synthesis](runtime.md#rt-rte-backend-synthesis), [EPI-RTE-page-update](#epi-rte-page-update) | None supplied | Truncation, dummy output and unconditional writes bound guarantee | Fidelity is requested, not enforced by truth checking | Transcript source-of-truth cannot license all reported facts. |
| [EPI-CLM-semantic-checks](#epi-clm-semantic-checks) | see record | see record | Rule descriptions promise semantic checks | [EPI-RTE-semantic-proxies](#epi-rte-semantic-proxies), [EPI-RTE-lint-return](#epi-rte-lint-return) | None supplied | No semantic callback invoked in these implementations | Structural proxies or explicit skip | Semantic names exceed implemented targets. |
| [EPI-CLM-lifecycle-states](#epi-clm-lifecycle-states) | see record | see record | Human confirmation and automatic staleness declared | [EPI-RTE-lifecycle-helper](#epi-rte-lifecycle-helper), [EPI-RTE-metadata-selection](#epi-rte-metadata-selection), [EPI-RTE-freshness-check](#epi-rte-freshness-check) | None supplied | Pure helper and display are not state persistence or human review | Legal transitions and metadata selection supported | Automatic lifecycle enforcement not established in searched callers. |
| [EPI-CLM-candidate-trust](#epi-clm-candidate-trust) | see record | see record | Human legitimacy/nonduplicate decision prescribed | [RT-RTE-candidate-admission](runtime.md#rt-rte-candidate-admission), [RT-RTE-mcp-access](runtime.md#rt-rte-mcp-access) | None supplied | No reviewer authentication or general query exclusion | Explicit disposition and archive mechanism exists | Archive/candidate content can still reach query; trusted-layer exclusion is not consumer isolation. |
| [RT-CLM-append-preservation](runtime.md#rt-clm-append-preservation) | see record | see record | Completion docstring | [RT-RTE-agent-completion](runtime.md#rt-rte-agent-completion) | None supplied | Replacement constructs body from supplied string | Frontmatter preservation, not automatic appended-body preservation | Supplied runtime mismatch retained; no observed data loss claimed. |

## Bounded conclusion

The supported acquisition path imports session material, then exposes it through retained raw and wiki files. Its source warrant is unknown: a transcript can warrant that an utterance occurred, not the utterance's factual content. Conversion filtering and synthesis prefix limits can remove premises or qualifiers. Generated claims require input/output evidence to classify them as reshaping, derivation or non-entailed conjecture; fluency and the word synthesis do not decide this. The deterministic dummy branch demonstrably reshapes excerpts and constructs metadata statements without testing the session's substantive propositions. See [RT-RTE-session-conversion](runtime.md#rt-rte-session-conversion), [RT-RTE-backend-synthesis](runtime.md#rt-rte-backend-synthesis).

Checking has heterogeneous domains. UUID completion checks association. Semantic-named lint rules inspect presence of structural markers, or skip; freshness checks age, and confidence is a heuristic over source labels/counts, dates and links. These results do not license proposition truth. CLI lint can make errors consequential to command success when explicitly requested, but does not remove pages; metadata endpoints filter/display assertions rather than confirm them. See [EPI-RTE-semantic-proxies](#epi-rte-semantic-proxies), [EPI-RTE-lint-return](#epi-rte-lint-return), [EPI-RTE-lifecycle-helper](#epi-rte-lifecycle-helper).

There is an explicit candidate disposition mechanism and human-review doctrine with intended use as trusted entity/concept content, criterion legitimate and nonduplicate, and discard/archive recovery. Actual evidence-consuming acceptance is not supplied. Other writes bypass that optional path. Ordinary ingest organization through cross-links and overview revision is requested; this is not lifecycle integration, because neither a preceding evidence-consuming acceptance decision nor a doctrine requiring that relation is established. Query scans do not exclude candidate/archive or stale labels; withdrawal by relocation is therefore not complete revocation of context availability. The authority path is page text → lexical snippets or host reads → foreground answer context, advisory/ranking rather than enforcing epistemic policy, across later questions while files remain. See [RT-RTE-candidate-admission](runtime.md#rt-rte-candidate-admission), [RT-RTE-mcp-access](runtime.md#rt-rte-mcp-access), [RT-BAP-wiki-context](runtime.md#rt-bap-wiki-context).

The optional build-time prose has a separate endpoint: grouped metadata → Claude stdout → reader `index.html`, not source/entity/concept or saved-answer Markdown. Its publication admission checks process success/nonempty output, not proposition truth. It therefore establishes no entry into the ordinary wiki-query lineage. See [EPI-OBJ-reader-overview](#epi-obj-reader-overview) and [RT-RTE-reader-build](runtime.md#rt-rte-reader-build).

Reflection and source-directed correction are shipped procedures, not evidence that a model performed criticism or that criticism changed later decisions. Instructions can directly guide behavior, and retained wiki context can shape later answers without parametric training. Neither delivery nor retention establishes improved capacity, autonomous theory building, or exercised self-improvement. Missing operation and causal evidence limit those properties independently; unread maintenance/evaluation variants additionally prevent a system-complete negative. No single epistemic score or unqualified system verdict follows.

## Shared records

### Components

none declared in this member

### Operative objects

#### EPI-OBJ-raw-sessions
Label: Raw session Markdown

SRC-1 `CLAUDE.md`; see [RT-RTE-session-conversion](runtime.md#rt-rte-session-conversion) for the producer's evidence passage. Natural-language transcripts and code/tool excerpts live in filesystem Markdown; symbolic metadata carries session identity. Distinct from [RT-OBJ-source-page](runtime.md#rt-obj-source-page), which is a static instruction rather than imported history. No supplied raw-data object counterpart. Warrant of imported claims remains unknown; source identity is recorded but redaction/truncation preclude assuming full preservation.

> Never modify files here. Treat as source-of-truth for facts.
> --- `CLAUDE.md`

#### EPI-OBJ-wiki-pages
Label: Wiki page bodies

SRC-1 `CLAUDE.md`. Natural-language summary/claim/contradiction bodies stored in Markdown, interpreted by host readers and models. Includes source/entity/concept and saved-answer bodies, not their symbolic quality metadata. Producer/consumer routes: [RT-RTE-host-ingest](runtime.md#rt-rte-host-ingest), [RT-RTE-backend-synthesis](runtime.md#rt-rte-backend-synthesis), [RT-RTE-candidate-admission](runtime.md#rt-rte-candidate-admission). Those are routes rather than a supplied page-body object; no object counterpart after comparison. Pages may contain theories, but supplied templates are not instantiated theory-production evidence.

> 9. **Flag contradictions** — if a new source contradicts existing wiki content, add a `## Contradictions` section to the affected page and leave BOTH claims visible. Do not silently overwrite.
> --- `CLAUDE.md`

#### EPI-OBJ-reader-overview
Label: Reader landing overview
Part of: [RT-RTE-reader-build](runtime.md#rt-rte-reader-build)

SRC-1 `llmwiki/build.py`. This object is the optional prose output within the cited route (an object part of a route, not a second route declaration). Natural-language Markdown returned in process memory is rendered as HTML in the filesystem reader `out_dir/index.html`. The requested content names projects, infers their subject from metadata, and describes activity. Its consumer is `render_index` followed by site readers; no inspected edge writes this prose into curated wiki Markdown. Distinct from [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages), whose host/MCP wiki consumers and storage differ. The supplied runtime route already contains this output, but supplies no separate operative-object counterpart. Exact output propositions and entailment remain uninspected; no observed run is supplied.

> render_index(groups, sources, out_dir, synthesis=synthesis)
> --- `llmwiki/build.py`

> {md_to_html(synthesis)}
> --- `llmwiki/build.py`

> out_path = out_dir / "index.html"
>     out_path.write_text(page, encoding="utf-8")
> --- `llmwiki/build.py`

#### EPI-OBJ-quality-metadata
Label: Confidence and lifecycle metadata

SRC-1 `llmwiki/confidence.py`, `llmwiki/lifecycle.py`, `llmwiki/mcp/server.py`. Symbolic numbers/enums/status text in Markdown frontmatter, with transient helper values in process memory. Distinct from natural-language page bodies and pending UUIDs in [RT-OBJ-pending-prompts](runtime.md#rt-obj-pending-prompts); no supplied metadata object counterpart. Candidate `status` and MCP `lifecycle` are different keys, not proven synchronized.

> if min_c <= conf <= max_c:
> --- `llmwiki/mcp/server.py`

#### EPI-OBJ-lint-issues
Label: Lint issue reports

SRC-1 `llmwiki/lint/__init__.py`, `llmwiki/cli.py`. Transient symbolic issue dictionaries and natural-language messages, rendered as JSON/chat/terminal output. Distinct from persisted wiki bodies and from supplied runtime route records; no supplied issue-object counterpart.

> issues.extend(rule.run(pages, llm_callback=llm_callback))
> --- `llmwiki/lint/__init__.py`

### Routes

#### EPI-RTE-semantic-proxies
Label: Semantic lint proxies

SRC-1 `llmwiki/lint/rules/claim_verification.py`, `llmwiki/lint/rules/summary_accuracy.py`, `llmwiki/lint/rules/contradiction_detection.py`, `llmwiki/lint/__init__.py`. Registry runner owns progression from page dictionaries to issues. ClaimVerification targets entity/concept pages with Key Facts/Claims markers lacking source metadata or Sessions/Sources headings. SummaryAccuracy targets an explicitly present but blank summary field. ContradictionDetection targets nonempty explicit Contradictions sections. All three skip without a callback; with any non-None callback, they run structural proxies without calling it. These predicates neither compare factual assertions against cited source contents nor judge cross-page inconsistency. A page with false claims and a Sources heading is a source-supported countercase to treating a clean proxy result as verification. Distinct from [RT-RTE-mcp-access](runtime.md#rt-rte-mcp-access): this is the package registry, not MCP's independent lint implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Issue dictionaries, or an info issue saying callback required.
- Later read-back: inapplicable — runner does not persist reports or change pages.
- Delegated visibility: Rule sees loaded page metadata/body; callback is tested for presence, not invoked.
- Selection predicate: Rule selected by registry/name and include_llm flag; internal page-type/marker conditions differ as above.
- Invalidation or expiry: Fresh checks per invocation; no stored validity certificate.
- Activation or effect: Issues flow to CLI summary/output; no page mutation or acceptance. Consumer/channel/force/horizon: lint caller, returned dictionaries, advisory, current invocation.
- Evidence limits: No run supplied; remaining rule bodies are not exhaustively assessed.

> # Structural proxy: check that entity/concept pages with claims
>         # (## Key Facts or ## Key Claims sections) also cite sources.
> --- `llmwiki/lint/rules/claim_verification.py`

> if llm_callback is None:
>             return [{
>                 "rule": self.name,
>                 "severity": "info",
>                 "page": "",
>                 "message": "skipped: requires LLM callback",
>             }]
> --- `llmwiki/lint/rules/summary_accuracy.py`

> # Structural proxy: check summary field is non-empty when present.
> --- `llmwiki/lint/rules/summary_accuracy.py`

> # is a simple structural detector for explicit `## Contradictions`
>         # sections (pages flagging their own contradictions).
> --- `llmwiki/lint/rules/contradiction_detection.py`

#### EPI-RTE-lint-return
Label: Lint command return

SRC-1 `llmwiki/cli.py`. CLI owns disposition of issue severity counts into exit status, distinct from issue production and from [RT-RTE-reader-build](runtime.md#rt-rte-reader-build)'s full-pipeline strict controls. Caller selects fail-on-errors; code decides exit; no per-content human veto, reference answer oracle or bounded improvement experiment. Trigger is lint invocation, not a proposed page change. CLI supplies include_llm but no callback, so semantic-rule skips can coexist with success. This route licenses command continuation, not acceptance of knowledge.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Printed/JSON issue report and integer exit status.
- Later read-back: inapplicable — no retained content change here.
- Delegated visibility: CLI receives summary counts and issues from package runner.
- Selection predicate: --fail-on-errors and error count greater than zero produce exit 1; absent wiki directory produces 2; other completed cases return 0.
- Invalidation or expiry: Current invocation only; no stored endorsement.
- Activation or effect: Shell caller receives conditional failure, enforcing command status only; no rejection/removal of page contents.
- Evidence limits: No shell/CI execution observed; warning/info skips are not semantic passes.

> if args.fail_on_errors and summary.get("error", 0) > 0:
>         return 1
>     return 0
> --- `llmwiki/cli.py`

#### EPI-RTE-freshness-check
Label: Page freshness warning

SRC-1 `llmwiki/lint/rules/content_freshness.py`. Rule owns page-by-page date-age evaluation; distinct from [RT-RTE-candidate-admission](runtime.md#rt-rte-candidate-admission)'s stale candidate listing. Target is time since last_verified or last_updated, not content truth; missing/invalid dates are skipped. More than 90 days produces warning, not persisted stale lifecycle.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Warning issue per overdue parseable date.
- Later read-back: inapplicable — no state write.
- Delegated visibility: Loaded page metadata only.
- Selection predicate: Runner includes rule; parseable preferred date older than threshold.
- Invalidation or expiry: Recomputed relative to current time.
- Activation or effect: Lint caller sees advisory issue in current invocation; ordinary query remains independently available.
- Evidence limits: Date freshness supplies no endorsement, correctness or exercised re-review evidence.

> date_str = meta.get("last_verified") or meta.get("last_updated")
> --- `llmwiki/lint/rules/content_freshness.py`

> if age_days > self.STALE_DAYS:
> --- `llmwiki/lint/rules/content_freshness.py`

#### EPI-RTE-lifecycle-helper
Label: Confidence and lifecycle helpers

SRC-1 `llmwiki/confidence.py`, `llmwiki/lifecycle.py`. Pure helper functions transform metadata/counts into heuristic score or legal state/exception. No supplied runtime counterpart; metadata display is separately [EPI-RTE-metadata-selection](#epi-rte-metadata-selection). Confidence is weighted source count, quality label, date recency and inbound links; decay multiplies by a content-type half-life factor. It does not read evidence bodies. Concrete deduction from defaults: 0.4×0.3 + 0.5×0.3 + 0.3×0.2 + 0.3×0.2 = 0.39. This is an arithmetic result under stipulated inputs, not 39% calibrated truth probability. Lifecycle transition checks enum adjacency; reviewed→verified returns verified without checking score, evidence or human identity. Auto-stale helpers return a suggestion, not a file write. Search for compute_confidence/check_auto_stale/check_confidence_stale under `llmwiki/` found their definitions, not a caller installing those values. This bounds the automatic-persistence claim without denying helper implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Float, state, None or InvalidTransition.
- Later read-back: inapplicable — pure helpers persist nothing.
- Delegated visibility: Explicit numeric/string inputs, not source propositions.
- Selection predicate: Caller invocation and helper-specific metadata/enum thresholds.
- Invalidation or expiry: Caller must recompute; no scheduler in these helpers.
- Activation or effect: Returned values available to a caller; consequential file-writing consumer not established in the searched package. No automatic epistemic/operational license follows.
- Evidence limits: Exact heuristic implemented; calibration, persisted automation and observed human verification unestablished.

> score = f1 * 0.3 + f2 * 0.3 + f3 * 0.2 + f4 * 0.2
>     return round(score, 2)
> --- `llmwiki/confidence.py`

> if not can_transition(current, target):
>         raise InvalidTransition(
>             f"Cannot transition from {current.value!r} to {target.value!r}"
>             + (f": {reason}" if reason else "")
>         )
>     return target
> --- `llmwiki/lifecycle.py`

#### EPI-RTE-metadata-selection
Label: MCP quality metadata views
Part of: [RT-RTE-mcp-access](runtime.md#rt-rte-mcp-access)

SRC-1 `llmwiki/mcp/server.py`. Material suboperations omitted from supplied runtime's detailed account: confidence range, lifecycle match, health dashboard and entity-name/type filters. Server reloads page metadata, filters/sorts/counts, then returns text. These are selection/display operations, not evaluation or admission of underlying propositions. Confidence filtering and sorting use numeric labels; lifecycle matches literal text; dashboard buckets count labels; entity search selects type/name and reports stored confidence. No callback verifies source claims, no human approves these outputs, and no expected-answer oracle or experiment is supplied.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Text list/counts, capped to 50 listed results where implemented, or missing-state error.
- Later read-back: Reloads existing frontmatter each invocation; does not accumulate results.
- Delegated visibility: Caller sees selected metadata summaries, not validation evidence.
- Selection predicate: Caller confidence bounds/state/name/entity type and stored metadata; no recomputation of confidence score.
- Invalidation or expiry: Files reloaded each call; labels remain until edited elsewhere.
- Activation or effect: Consumer is MCP host, channel tool text, force filtering/ranking/advisory, horizon current request and any opaque later host use. No verified-only query policy follows.
- Evidence limits: Source-grounded capacity only; actual host reliance unobserved.

> if page["meta"].get("lifecycle", "").lower() == state
> --- `llmwiki/mcp/server.py`

#### EPI-RTE-page-update
Label: Source-directed page update

SRC-1 `.claude/commands/wiki-update.md`. Distinct from [RT-RTE-host-ingest](runtime.md#rt-rte-host-ingest)'s ingest/query workflows: this is a single-page corrective operation. User points to page/reason; foreground agent reads source and page, diagnoses delta, then edits. User can decline invocation; no separate per-edit approval is required, except cross-page backlink changes. No answer oracle. Open correction workflow, triggered by changed source, stale fact, broken link or new contradiction. Guidance preserves both conflicting claims and limits rewrites; recovery is manual editing/re-ingest, not transaction rollback. Proposed content and timestamp/log persist if followed. Source-read evaluation precedes edit but neither its actual result nor evidence-consuming acceptance is supplied.

- implementation conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Requested edit summary and follow-up list.
- Later read-back: Revised page available to later host/MCP consumers.
- Delegated visibility: Foreground host instructed to read target, index and listed sources.
- Selection predicate: User target and agent diagnosis of delta.
- Invalidation or expiry: Edit updates last_updated; contradictory old claim stays visible.
- Activation or effect: Instruction channel to host, advisory/model-mediated force; later page context can affect future questions, not observed here.
- Evidence limits: Doctrine only; no actual revised page/provenance trace.

> 3. **Read the source(s)** listed in the frontmatter's `sources:` field.
> --- `.claude/commands/wiki-update.md`

> - **Never overwrite contradictions.** If new information conflicts with old, add a `## Contradictions` section, don't delete the old claim.
> --- `.claude/commands/wiki-update.md`

#### EPI-RTE-wiki-reflection
Label: Wiki reflection procedure

SRC-1 `.claude/commands/wiki-reflect.md`. Distinct from [RT-RTE-host-ingest](runtime.md#rt-rte-host-ingest) and corrective update: produces a review/proposal before mutation. Foreground host inspects index/overview and source/entity/concept pages, or a sample above 50 pages, interprets coverage/gaps/contradictions, and asks user before saving or follow-up action. User can veto persistence/change; no expected-answer oracle; open review, not scored experiment. Requested reflection/log retention is not automatic acceptance or integration. It requests specific cited diagnoses while flagging interpretations. No instantiated theory critique with blame placement, resulting changed reliance, and iteration is supplied, so those theory-builder properties remain unestablished independently of the procedure's availability.

- implementation conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Requested 3–5 paragraph reflection and user options.
- Later read-back: Optional saved synthesis and log; later consumption unobserved.
- Delegated visibility: Host reads selected wiki bodies; large-corpus sampling can omit evidence.
- Selection predicate: User focus hint and model interpretation, with representative sampling allowed.
- Invalidation or expiry: No automatic expiry; proposed changes require user approval by doctrine.
- Activation or effect: Consumer user/foreground host, channel chat and optional saved synthesis, force advisory, horizon current review plus potential later reads.
- Evidence limits: Named self-reflection is not demonstrated two-way reflective operation, learning benefit, autonomous revision or self-improvement.

> 1. **Don't edit pages during reflection.** Reflection is read-only. Any changes are proposed to the user, who approves before you touch the wiki.
> --- `.claude/commands/wiki-reflect.md`

### Claims

#### EPI-CLM-source-fidelity
Label: Source traceability rules

SRC-1 `llmwiki/synth/prompts/source_page.md`, `CLAUDE.md`. Doctrine declares raw as factual source-of-truth and requires source traceability plus preservation of contradictions. More specific than [RT-CLM-history-compilation](runtime.md#rt-clm-history-compilation): concerns warrant and lineage rather than compilation existence.

> 2. Every claim must be traceable to something said in the session
> --- `llmwiki/synth/prompts/source_page.md`

#### EPI-CLM-semantic-checks
Label: Semantic lint descriptions

SRC-1 `llmwiki/lint/rules/claim_verification.py`, `llmwiki/lint/rules/summary_accuracy.py`, `llmwiki/lint/rules/contradiction_detection.py`. Three rule-class descriptions imply semantic verification/accuracy/contradiction detection; separate implemented predicates are recorded above. No supplied claim counterpart after comparison with [RT-CLM-history-compilation](runtime.md#rt-clm-history-compilation).

> """Verify claims are supported by cited sources (LLM-powered)."""
> --- `llmwiki/lint/rules/claim_verification.py`

> """Check that summary: field matches content (LLM-powered)."""
> --- `llmwiki/lint/rules/summary_accuracy.py`

> """Detect semantic contradictions across pages (LLM-powered)."""
> --- `llmwiki/lint/rules/contradiction_detection.py`

#### EPI-CLM-lifecycle-states
Label: Lifecycle quality states

SRC-1 `llmwiki/lifecycle.py`. Claims human confirmation and confidence threshold for verified, plus automatic transitions. Distinct from supplied runtime claims; these concern evaluation state rather than compilation or hand-edit preservation.

> verified  — High confidence (≥ 0.8), human-confirmed.
> --- `llmwiki/lifecycle.py`

> Auto transitions:
>     Created by LLM        → draft
>     Basic lint passes      → reviewed
>     Confidence drops < 0.5 → stale
>     No update for 90 days  → stale  (auto-stale)
> --- `llmwiki/lifecycle.py`

#### EPI-CLM-candidate-trust
Label: Candidate trusted-layer exclusion

SRC-1 `.claude/commands/wiki-candidates.md`. Trust is declared conditional on human approval. Distinct from [RT-RTE-candidate-admission](runtime.md#rt-rte-candidate-admission)'s implementation account; this claim tests the doctrine against consumers, not just transition code.

> They
> are **not** part of the trusted wiki layer until a human approves them.
> --- `.claude/commands/wiki-candidates.md`

> - **promote** — candidate is legitimate and not a duplicate.
> --- `.claude/commands/wiki-candidates.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member
