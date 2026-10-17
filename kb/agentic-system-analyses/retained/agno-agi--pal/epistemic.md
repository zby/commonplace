---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Pal epistemic routes: source acquisition, wiki compilation, lint, operational learning and bounded evaluators."
run-id: AAS-2026-10-17-pal-e313a0902289-01
reviewed-boundary: 6516b8ede0c085e48f39f3bd04cb85b475a855dc
---

# Pal epistemic report

## Source-and-claim boundary

The question is how Pal admits personal and external information, turns it into reusable wiki content or operational guidance, checks it, and licenses later reliance. Scope and external exclusions are see [boundary](boundary.md#boundary-and-evidence); evidence identities and layers are see the [Source register](boundary.md#source-register). All source findings below use SRC-1 at the frozen commit. Source inspection and supplied runtime findings establish configuration, implementation and instruction contracts, not successful operation. No execution trace, populated user corpus, provider state or causal comparison was supplied.

Consequential claims are [EPI-CLM-compounding-learning](#epi-clm-compounding-learning), [EPI-CLM-source-tracking](#epi-clm-source-tracking), [EPI-CLM-wiki-quality](#epi-clm-wiki-quality), and the supplied [RT-CLM-control-scope](runtime.md#rt-clm-control-scope). Missing provider/runtime internals prevent conclusions about generation fidelity, exact learning admission and identity isolation. Missing compiled artifacts prevent classifying any actual summary's semantic relation to its sources. Missing traces prevent conclusions about checks performed, accepted claims, correction uptake or improvement. Missing interventions prevent attribution of benefit to wiki, memory, routing or any individual component.

### Coverage

“Direct” means source read by this analyst; “supplied” means the runtime's inspected finding is used without claiming an independent read of that implementation. The available but uninspected paths below are not access gaps and prevent a system-complete negative.

| Entry point or operation | Source path | Coverage and records / limit |
|---|---|---|
| Team, API, Slack and direct specialists | `pal/team.py`, `app/main.py` | Direct application wiring and team search; supplied [RT-RTE-team-dispatch](runtime.md#rt-rte-team-dispatch). Exact external delegation filtering uninspected. |
| Direct ingest and Researcher tools | `app/router.py`, `pal/tools/ingest.py`, `pal/agents/researcher.py` | Direct full source; [RT-RTE-raw-ingest](runtime.md#rt-rte-raw-ingest), [EPI-OBJ-raw](#epi-obj-raw). Direct route bypasses source-selection guidance. |
| Compiler, forced compile, scheduled compile | `pal/agents/compiler.py`, `pal/tools/build.py`, `pal/tools/wiki.py`, `app/router.py`, `app/main.py` | Direct; [EPI-RTE-compiler-transform](#epi-rte-compiler-transform), [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance). No mandatory evidence-consuming acceptance gate identified in these paths. |
| Linter, scheduled and direct lint | `pal/agents/linter.py`, `app/main.py`, `app/router.py` | Direct; [EPI-RTE-lint-check](#epi-rte-lint-check), [EPI-RTE-lint-retain](#epi-rte-lint-retain). Findings are advisory, not automatic withdrawal. |
| Navigator retrieval, captures, synthesis and outputs | `pal/instructions.py`, `pal/agents/navigator.py`, `pal/tools/build.py` | Direct; [RT-RTE-navigator-work](runtime.md#rt-rte-navigator-work), [EPI-OBJ-sql](#epi-obj-sql), [EPI-OBJ-answer](#epi-obj-answer). SQLTools, FileTools, Gmail, Calendar and MCP internals excluded dependencies. |
| Routing writes by several specialists | `pal/tools/knowledge.py`, `pal/tools/build.py` | Direct; [EPI-RTE-knowledge-write](#epi-rte-knowledge-write). Discoveries can change retrieval without checking source truth. |
| Context loader CLI dispatch and recreate | `context/load_context.py` | Direct full source including parser/main; [RT-RTE-context-refresh](runtime.md#rt-rte-context-refresh), [EPI-OBJ-routing](#epi-obj-routing). Recreate deletes non-file metadata too. |
| Learned knowledge, corrections and agentic memory | `pal/agents/navigator.py`, `pal/agents/researcher.py`, `pal/instructions.py`, `pal/team.py` | Direct configuration/instructions and supplied team configuration; [EPI-RTE-learning-adapt](#epi-rte-learning-adapt). External Agno admission, memory rewriting and delivery internals uninspected. |
| Startup, scheduled and direct pull; Syncer | `pal/tools/git.py`, `pal/agents/syncer.py`, `app/main.py`, `app/router.py` | Direct caller wiring; implementation supplied by [RT-RTE-git-sync](runtime.md#rt-rte-git-sync). No semantic endorsement follows from Git success. |
| Unified evaluator CLI and wiki cases | `evals/run.py`, `evals/cases/wiki.py` | Direct; [RT-RTE-evaluation-driver](runtime.md#rt-rte-evaluation-driver). Criteria/expected answers and expected tool calls assess different targets. |
| Smoke and extended evaluator result/cleanup consumers | `evals/smoke.py`, `evals/extended_smoke.py` | Direct runner ranges and dependency/cleanup code; [EPI-RTE-smoke-select](#epi-rte-smoke-select). Available case definitions not all read; no exhaustive test-quality verdict. |
| General validation and loader unit tests | `.github/workflows/validate.yml`, `scripts/validate.sh`, `evals/test_load_context.py` | Available, uninspected here. Prevents an exhaustive statement about all shipped static/unit checks; none of this missing inspection is evidence of production claim acceptance. |
| OAuth, setup, deployment helpers and user templates | `scripts/`, `docs/GOOGLE_AUTH.md`, `docs/SLACK_CONNECT.md`, `context/templates/`, `context/voice/` | Roles supplied by boundary, details uninspected here. No blanket conclusions about authorization or drafting fidelity. |

No Pal plugin registry or event-hook system beyond the supplied tool assemblies, startup lifespan and scheduled calls is established by this inspection. This is not a negative about dependency-provided operations. Distributed-parametric generation and embedding configuration is see [RT-CMP-openai-responses](runtime.md#rt-cmp-openai-responses) and [RT-CMP-openai-embedder](runtime.md#rt-cmp-openai-embedder): no Pal weight-update route inspected; exact backing versions and provider mutation remain uninspected. Database/vector configuration is supplied evidence, not a new source or a demonstration of learning.

## Epistemic-object inventory

Fields owned by each record are see its citation; these rows do not restate its storage or authority findings.

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-raw](#epi-obj-raw) | Imported document claims; sometimes only a pending/error stub | see record | SRC-1 `pal/tools/ingest.py` | Warrant of external source unknown |
| [EPI-OBJ-summaries](#epi-obj-summaries) | Source thesis, findings and selected data | see record | SRC-1 `pal/agents/compiler.py` | No candidate outputs supplied |
| [EPI-OBJ-concepts](#epi-obj-concepts) | Cross-source concept explanations and contradictions | see record | SRC-1 `pal/agents/compiler.py` | Citation prescription is not verified support |
| [EPI-OBJ-lint-report](#epi-obj-lint-report) | Claims of conflict, omission, staleness and overlap; suggested actions | see record | SRC-1 `pal/agents/linter.py` | No completed report supplied |
| [EPI-OBJ-routing](#epi-obj-routing) | File/location metadata and model-proposed discoveries | see record | SRC-1 `pal/tools/knowledge.py` | File metadata and inferred connections have different provenance |
| [EPI-OBJ-learnings](#epi-obj-learnings) | Strategy success, patterns and user corrections; directives may be non-truth-apt | see record | SRC-1 `pal/instructions.py` | Actual retained entries and dependency admission opaque |
| [EPI-OBJ-sql](#epi-obj-sql) | User facts, notes, decisions and query results | see record | SRC-1 `pal/instructions.py` | No database or actual query supplied |
| [EPI-OBJ-answer](#epi-obj-answer) | Answers, briefings, research and optional retained outputs | see record | SRC-1 `pal/instructions.py` | Meaning preservation through per-source and leader synthesis unobserved |
| [RT-OBJ-manifest](runtime.md#rt-obj-manifest) | Processing flag, not a truth or acceptance certificate | see record | SRC-1 `pal/tools/ingest.py` | Compiled flag can be set without inspecting output |
| [RT-OBJ-agent-instructions](runtime.md#rt-obj-agent-instructions) | Primarily policy/directives rather than candidate claims | see record | SRC-1 `pal/instructions.py` | Delivery is not compliance |

## Authority-route ledger

Each row is a separate consequential function, including where the same supplied route performs several functions. Record-owned generic fields are see the linked record. “Possible” results are architectural possibilities, not observed instances. No observed accepted ampliative claim is established.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority | Behavioral-authority path | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-raw-ingest](runtime.md#rt-rte-raw-ingest) | content transformation | implemented | [EPI-OBJ-raw](#epi-obj-raw) | truth-apt transformation: acquisition/import | see record | see record; no source-truth evaluator | see record | see record | see record | Source attribution retained, source warrant unknown; external extraction fidelity unknown | see record | see record | SRC-1 `pal/tools/ingest.py` | none | none | Text import preserves supplied body; URL failure may import no substantive claims |
| [RT-RTE-raw-ingest](runtime.md#rt-rte-raw-ingest) | retention | implemented | [EPI-OBJ-raw](#epi-obj-raw) | no content change | see record | see record | see record | see record | see record | None added by saving | see record | see record | SRC-1 `pal/tools/ingest.py` | none | retention is not acceptance | Filename collision can break historical lineage |
| [EPI-RTE-compiler-transform](#epi-rte-compiler-transform) | content transformation | implemented | [EPI-OBJ-summaries](#epi-obj-summaries), [EPI-OBJ-concepts](#epi-obj-concepts) | truth-apt transformation: indeterminate | see record | see record | see record | see record | see record | No verified source fidelity or novel accepted proposition established | see record | see record | SRC-1 `pal/agents/compiler.py` | [EPI-CLM-source-tracking](#epi-clm-source-tracking) | intended compression is not established preservation | Needs paired inputs/outputs to distinguish reshaping, derivation and conjecture |
| [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance) | retention | implemented | [EPI-OBJ-summaries](#epi-obj-summaries), [EPI-OBJ-concepts](#epi-obj-concepts) | no content change | see record | see record | see record | see record | see record | No added warrant from file/index/state writes | see record | see record | SRC-1 `pal/tools/wiki.py` | [EPI-CLM-source-tracking](#epi-clm-source-tracking) | retention is not lifecycle integration | No evidence-consuming acceptance decision in inspected write functions |
| [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance) | operational admission/selection/consumption | implemented | [RT-OBJ-manifest](runtime.md#rt-obj-manifest) | non-truth-apt policy/content update: processing eligibility | see record | see record | see record | see record | see record | Compile flag licenses no truth claim | see record | see record | SRC-1 `pal/tools/ingest.py` | none | completion is not acceptance | Force prompt and incremental guidance conflict; model resolves |
| [EPI-RTE-lint-check](#epi-rte-lint-check) | check/evidence production | implemented | [EPI-OBJ-concepts](#epi-obj-concepts), [EPI-OBJ-lint-report](#epi-obj-lint-report) | truth-apt transformation: indeterminate | see record | see record | see record | see record | see record | Model assessments bounded to inspected articles and requested criteria; not proof of truth | see record | see record | SRC-1 `pal/agents/linter.py` | [EPI-CLM-wiki-quality](#epi-clm-wiki-quality) | diagnostic suggestion is not enforced rejection | Contradiction detection and freshness checks have distinct licenses |
| [EPI-RTE-lint-retain](#epi-rte-lint-retain) | retention | implemented | [EPI-OBJ-lint-report](#epi-obj-lint-report) | no content change | see record | see record | see record | see record | see record | Saving a critique adds no acceptance warrant | see record | see record | SRC-1 `pal/agents/linter.py` | [EPI-CLM-wiki-quality](#epi-clm-wiki-quality) | none | No mandatory report-to-repair or invalidation consumer |
| [EPI-RTE-knowledge-write](#epi-rte-knowledge-write) | retention | implemented | [EPI-OBJ-routing](#epi-obj-routing) | no content change | see record | see record | see record | see record | see record | Stored model assertions not verified | see record | see record | SRC-1 `pal/tools/knowledge.py` | [EPI-CLM-compounding-learning](#epi-clm-compounding-learning) | routing authority precedes acceptance | Metadata writer accepts arbitrary strings |
| [RT-RTE-context-refresh](runtime.md#rt-rte-context-refresh) | content transformation | implemented | [EPI-OBJ-routing](#epi-obj-routing) | truth-apt transformation: non-ampliative reshaping | see record | see record | see record | see record | see record | Carries file identity and tags, not document-claim warrant | see record | see record | SRC-1 `context/load_context.py` | none | none | Sorted tags are routing hints, not checked relevance |
| [RT-RTE-context-refresh](runtime.md#rt-rte-context-refresh) | lineage/freshness/recovery | implemented | [EPI-OBJ-routing](#epi-obj-routing) | no content change | see record | see record | see record | see record | see record | Indexed time is not source endorsement | see record | see record | SRC-1 `context/load_context.py` | none | none | Recreate withdraws all vector entries, ordinary reload does not explicitly prune removed files |
| [RT-RTE-navigator-work](runtime.md#rt-rte-navigator-work) | operational admission/selection/consumption | implemented | [EPI-OBJ-routing](#epi-obj-routing), [EPI-OBJ-concepts](#epi-obj-concepts), [EPI-OBJ-raw](#epi-obj-raw), [EPI-OBJ-sql](#epi-obj-sql) | no content change | see record | see record | see record | see record | see record | Relevance and retrieval priority do not certify source truth | see record | see record | SRC-1 `pal/instructions.py` | [EPI-CLM-compounding-learning](#epi-clm-compounding-learning) | use before acceptance | Raw and live fallbacks defeat a wiki-only account |
| [RT-RTE-navigator-work](runtime.md#rt-rte-navigator-work), [RT-RTE-team-dispatch](runtime.md#rt-rte-team-dispatch) | content transformation | implemented | [EPI-OBJ-answer](#epi-obj-answer) | truth-apt transformation: indeterminate | see records | see records | see records | see records | see records | No demonstrated checked entailment or ampliative acceptance | see records | see records | SRC-1 `pal/instructions.py` | [EPI-CLM-compounding-learning](#epi-clm-compounding-learning) | none | Per-source summaries and leader rewrite may alter meaning; outputs absent |
| [EPI-RTE-learning-adapt](#epi-rte-learning-adapt) | behavior/policy adaptation | implemented | [EPI-OBJ-learnings](#epi-obj-learnings) | non-truth-apt policy/content update: retrieval and correction priority | see record | see record | see record | see record | see record | Explicit corrections outrank recency by instruction, not independent truth validation | see record | see record | SRC-1 `pal/instructions.py` | [EPI-CLM-compounding-learning](#epi-clm-compounding-learning) | adaptation is not measured improvement | Truth-apt pattern-generation internals not determinable |
| [RT-RTE-git-sync](runtime.md#rt-rte-git-sync) | lineage/freshness/recovery | implemented | [EPI-OBJ-raw](#epi-obj-raw), [EPI-OBJ-concepts](#epi-obj-concepts) | truth-apt transformation: acquisition/import | see record | see record; Git mechanics, not truth | see record | see record | see record | Remote source warrant unknown | see record | see record | SRC-1 `pal/tools/git.py` | [RT-CLM-control-scope](runtime.md#rt-clm-control-scope) | synchronization is not semantic review | Incoming files can supersede local content independently of lint |
| [RT-RTE-evaluation-driver](runtime.md#rt-rte-evaluation-driver) | check/evidence production | implemented | [EPI-OBJ-answer](#epi-obj-answer) | no content change | see record | see record; response criteria, expected-output comparison, expected tool calls are separate targets | see record | see record | see record | Only configured response/tool-call criteria, not full KB truth or external non-effects | see record | see record | SRC-1 `evals/run.py` | [RT-CLM-control-scope](runtime.md#rt-clm-control-scope) | tool presence is not output fidelity | Underlying judge/reliability algorithms external |
| [EPI-RTE-smoke-select](#epi-rte-smoke-select) | check/evidence production | implemented | [EPI-OBJ-answer](#epi-obj-answer) | no content change | see record | see record | see record | see record | see record | Lexical assertions over response text only | see record | see record | SRC-1 `evals/extended_smoke.py` | none | none | Passing a regex does not establish article correctness |
| [EPI-RTE-smoke-select](#epi-rte-smoke-select) | operational admission/selection/consumption | implemented | [EPI-OBJ-answer](#epi-obj-answer) | no content change | see record | see record | see record | see record | see record | Test continuation only, no product acceptance | see record | see record | SRC-1 `evals/extended_smoke.py` | none | none | Concrete consequential consumer refines runtime's console-only endpoint, without contradicting its no-deployment-gate finding |
| [RT-RTE-evaluation-driver](runtime.md#rt-rte-evaluation-driver) | operational admission/selection/consumption | implemented | [EPI-OBJ-raw](#epi-obj-raw), [EPI-OBJ-concepts](#epi-obj-concepts) | non-truth-apt policy/content update: unconditional fixture reset | see record | see record | see record | see record | see record | Cleanup is no finding of falsity | see record | see record | SRC-1 `evals/extended_smoke.py` | [RT-CLM-control-scope](runtime.md#rt-clm-control-scope) | deletion is not epistemic rejection | Removal can affect later KB use but no rollback supplied |

No disposition/acceptance or post-acceptance lifecycle-integration route was established in the inspected ingest, compile, lint, metadata-write and evaluation consumers. This is a bounded finding about these paths, not a system-complete negative. Source-linking and index organization are real requested operations; without a prior acceptance decision they remain organization/retention, not lifecycle integration in this report's sense.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-compounding-learning](#epi-clm-compounding-learning) | see record | SRC-1 `docs/SPEC.md`; doctrine/design | see record | [EPI-RTE-learning-adapt](#epi-rte-learning-adapt), [EPI-RTE-knowledge-write](#epi-rte-knowledge-write), [RT-RTE-navigator-work](runtime.md#rt-rte-navigator-work) | None supplied | No intervention or outcome comparison; retention alone cannot license improvement | Reusable stores and requested learning loop are configured | “Every interaction improves” exceeds evidence; not disproved by missing traces |
| [EPI-CLM-source-tracking](#epi-clm-source-tracking) | see record | SRC-1 `pal/agents/compiler.py`; doctrine/design | see record | [EPI-RTE-compiler-transform](#epi-rte-compiler-transform), [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance) | None supplied | No checked source/claim pairs or fidelity comparison | Source-linked article format and writing capability | No inspected citation-entailment validator; compile flag does not attest fidelity |
| [EPI-CLM-wiki-quality](#epi-clm-wiki-quality) | see record | SRC-1 `pal/agents/linter.py`; doctrine/design | see record | [EPI-RTE-lint-check](#epi-rte-lint-check), [EPI-RTE-lint-retain](#epi-rte-lint-retain) | None supplied | No sensitivity/specificity or repair-outcome evidence | Requested model checks and advisory report persistence | No mandatory withdrawal or repair; timestamp is not truth evaluation |
| [RT-CLM-control-scope](runtime.md#rt-clm-control-scope) | see record | SRC-1 `pal/instructions.py`; doctrine/design and supplied implementation | see record | [RT-RTE-navigator-work](runtime.md#rt-rte-navigator-work), [RT-RTE-evaluation-driver](runtime.md#rt-rte-evaluation-driver), [RT-RTE-git-sync](runtime.md#rt-rte-git-sync) | None supplied | Response-level evaluation does not prove isolation or side-effect absence | Distinct policies and tool grants, not one global invariant | Direct ingress, broad file grants and evaluator cleanup bound claims |

## Bounded conclusion

Pal has implemented paths for importing supplied text and extracted URLs, retaining raw sources, configuring model-produced summaries/concepts, and prioritizing those files for later answers. Imported text bodies are preserved by the deterministic text writer; source truth remains unknown. URL extraction and Researcher summarization have additional uninspected fidelity boundaries. Filename collisions can overwrite a body while retaining multiple manifest entries. See [RT-RTE-raw-ingest](runtime.md#rt-rte-raw-ingest) and [EPI-OBJ-raw](#epi-obj-raw).

The Compiler's requested summaries and cross-source concept updates do not by themselves establish non-ampliative reshaping, entailed derivation or ampliative conjecture in an actual output. No warranted premises and checked interpretation yielding a particular derived proposition were supplied. The ledger therefore keeps model transformations indeterminate rather than treating novelty or absent entailment proof as conjecture. A raw body can be consulted before compilation, and a wiki article can be used without lint or acceptance. See [EPI-RTE-compiler-transform](#epi-rte-compiler-transform) and [RT-RTE-navigator-work](runtime.md#rt-rte-navigator-work).

The Linter is configured to assess inter-article conflict, structural gaps and age/length heuristics, optionally using web search for suggestions. Its output can be retained and can add Discovery metadata, but no mandatory consumer invalidates an article or checks that Compiler repairs a finding. Compile flags and state timestamps are operational bookkeeping, not evidence-consuming acceptance decisions. No particular accepted ampliative claim, acceptance criterion for KB truth, or subsequent lifecycle integration is established in these inspected paths. See [EPI-RTE-lint-check](#epi-rte-lint-check), [EPI-RTE-lint-retain](#epi-rte-lint-retain) and [RT-OBJ-manifest](runtime.md#rt-obj-manifest).

Operational authority is broader than epistemic license: routing entries can shortcut retrieval; corrections can outrank other learnings; wiki-first instructions can favor retained content; a passing smoke result permits dependent cases. These consumers give stored material consequential force without making its truth established. Evaluation targets remain separate: model-judged response criteria, expected-answer accuracy, expected-tool presence, and deterministic lexical smoke assertions. None of those inspected consumers installs a better model or automatically repairs the wiki. See [EPI-RTE-knowledge-write](#epi-rte-knowledge-write), [EPI-RTE-learning-adapt](#epi-rte-learning-adapt), [EPI-RTE-smoke-select](#epi-rte-smoke-select), and [RT-RTE-evaluation-driver](runtime.md#rt-rte-evaluation-driver).

Direct policy adaptation is configured through retrieval strategies and corrections. Its architecture is not made indeterminable by absent runs; actual updates, successful reuse and improved capacity are unobserved. Natural-language explanations and critique prompts support potential localized content and inspectability, but no actual formulated theory, content-dependent criticism with blame and changed reliance, or criticism-driven next round was supplied. A functioning theory builder is not established; opaque model processing is not evidence of its absence. Learning, reflection, autonomy and self-improvement remain separate: model-selected work is afforded, system-oriented metadata is retained, but no observed two-way reflective loop, complete autonomous theory process, or evidence-responsive self-change causally exercised in later operation is demonstrated. The broad compounding claim remains unsupported at the benefit layer, not refuted at the capacity layer. See [EPI-CLM-compounding-learning](#epi-clm-compounding-learning), [EPI-RTE-learning-adapt](#epi-rte-learning-adapt), and [EPI-RTE-lint-check](#epi-rte-lint-check).

## Shared records

### Operative objects

#### EPI-OBJ-raw
Label: Raw source bodies

Source-native identity: `raw/{slug}.md`, natural-language source body plus YAML frontmatter stored in context files. Distinct from [RT-OBJ-manifest](runtime.md#rt-obj-manifest), which stores processing metadata, and the endpoint route [RT-RTE-raw-ingest](runtime.md#rt-rte-raw-ingest). Direct text imports preserve supplied body text; the source field is caller-supplied attribution, not authentication. URL extraction is external; failures produce persistent non-substantive stubs. Researcher may summarize multi-page sources, so not all raw content is verbatim external evidence. SRC-1 `pal/tools/ingest.py`, `pal/agents/researcher.py`.

> file_path.write_text(frontmatter + content + "\n")
> --- `pal/tools/ingest.py`

> - For multi-page sources, summarize and save key sections
> --- `pal/agents/researcher.py`

Concrete implementation deduction, not target execution: text title `A_B!` becomes `a-b.md`; body `The meeting is Tuesday.` is appended unchanged after frontmatter. Title `A B` yields the same filename. The second write replaces the first file while `_read_manifest` followed by append retains another entry. The body-preserving write does not validate the meeting claim or preserve a version-specific source body. Relevant code:

> text = text.lower().strip()
> text = re.sub(r"[^\w\s-]", "", text)
> text = re.sub(r"[\s_]+", "-", text)
> text = re.sub(r"-+", "-", text)
> return text[:80].strip("-")
> --- `pal/tools/ingest.py`

#### EPI-OBJ-summaries
Label: Wiki source summaries

Source-native identity: `wiki/summaries/{doc-name}.md`; natural-language summary with source metadata in context filesystem. Distinct from the concept articles below; nearest supplied container is [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance), an operation rather than a content object. Summaries select thesis/findings, data and links. No paired candidate/source artifact establishes semantic preservation. SRC-1 `pal/agents/compiler.py`.

> Summaries in wiki/summaries/ should be concise (200-500 words) and capture:
> - Main thesis/findings
> - Key data points or claims
> - How it connects to other concepts in the wiki
> --- `pal/agents/compiler.py`

#### EPI-OBJ-concepts
Label: Wiki concept articles

Source-native identity: `wiki/concepts/{concept}.md`; natural-language explanations plus symbolic source/related links, context filesystem. Distinct from source-specific summaries and from [RT-OBJ-manifest](runtime.md#rt-obj-manifest); closest supplied workflow is [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance). Cross-source enrichment can contain changed assertions, but no actual new proposition is supplied to establish non-entailment. SRC-1 `pal/agents/compiler.py`.

> - If wiki/concepts/{concept}.md exists, update it with new information and cite the source
> - If not, create a new concept article with clear structure
> --- `pal/agents/compiler.py`

#### EPI-OBJ-lint-report
Label: Wiki lint report

Source-native identity: `wiki/lint-report.md`, natural-language findings and suggested actions in context filesystem. Distinct from articles: it diagnoses them rather than replacing their content. Closest supplied route is [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance); no supplied operative-object counterpart. No completed artifact was supplied. SRC-1 `pal/agents/linter.py`.

> 4. Write a lint report to wiki/lint-report.md via `save_file`
> 5. Update wiki state (`update_wiki_state` with mark_linted=True)
> 6. Save any new `Discovery:` entries to knowledge for connections found
> --- `pal/agents/linter.py`

#### EPI-OBJ-routing
Label: Knowledge routing entries

Source-native identity: `pal_knowledge` entries named `File:`, `Schema:`, `Source:`, `Discovery:`, `Wiki:` and `Raw:`. Natural-language descriptions and symbolic paths live through the configured PostgreSQL/vector knowledge substrate. Dense embedding representation is separately see [RT-CMP-openai-embedder](runtime.md#rt-cmp-openai-embedder). Distinct from [RT-OBJ-manifest](runtime.md#rt-obj-manifest), which controls compile eligibility. Loader-origin file entries and agent-origin discoveries remain separate provenance classes: the former are fixed-format metadata, the latter model assertions about source locations/connections. No supplied object counterpart after comparison; [RT-RTE-context-refresh](runtime.md#rt-rte-context-refresh) is the nearest route.

SRC-1 `context/load_context.py` produces file path, rounded size, frontmatter tags and indexing time, not document bodies. Concrete deduction: frontmatter list `[zeta, alpha]` becomes `alpha, zeta` because tags are sorted before joining; no added proposition about the document's substantive truth follows.

> if isinstance(tags, list) and tags:
>     return sorted(str(t) for t in tags)
> --- `context/load_context.py`

> f"Intent tags: {', '.join(tags)}\n"
> --- `context/load_context.py`

#### EPI-OBJ-learnings
Label: Operational learnings

Source-native identity: `pal_learnings` with `Retrieval:`, `Pattern:` and `Correction:` entries. Natural-language retained operational guidance and possible truth-apt descriptions, persisted through Agno's knowledge configuration; actual records/serialization are uninspected. Distinct from static [RT-OBJ-agent-instructions](runtime.md#rt-obj-agent-instructions) and file-routing entries. Nearest supplied operation is [RT-RTE-navigator-work](runtime.md#rt-rte-navigator-work). Configuration enables AGENTIC learned knowledge; source does not expose a content validator or prove that a correction is true. SRC-1 `pal/agents/navigator.py`, `pal/instructions.py`.

> **Hygiene**: Search before saving — update, don't duplicate. Include dates. When learnings conflict, prefer recent; `Correction:` always wins. If a learning references something that no longer exists, verify before following.
> --- `pal/instructions.py`

#### EPI-OBJ-sql
Label: Structured user records

Source-native identity: user-created `pal_*` tables; symbolic rows/queries and natural-language content stored in PostgreSQL. Distinct from routing metadata that describes where these records live; closest supplied route is [RT-RTE-navigator-work](runtime.md#rt-rte-navigator-work). Query results can be truth-apt; actual schema, contents and queries are absent. No general derivation warrant follows from SQL availability; a particular aggregate would need its inputs and query interpretation checked. SRC-1 `pal/instructions.py`.

> The user's structured data: notes, people, projects, decisions. You own the schema. Tables are created on demand.
> --- `pal/instructions.py`

#### EPI-OBJ-answer
Label: Answers and optional outputs

Source-native identity: Navigator substantive answers, summaries and optional `wiki/outputs/` files, then leader synthesis. Natural-language model outputs; current replies flow through team responses and optional retained outputs through context filesystem. Distinct from source articles and operational guidance; nearest supplied routes are [RT-RTE-navigator-work](runtime.md#rt-rte-navigator-work) and [RT-RTE-team-dispatch](runtime.md#rt-rte-team-dispatch). No candidate output or provenance trace supplied. SRC-1 `pal/instructions.py`; leader synthesis passage is supplied in the dispatch account.

> 5. If you produce a substantive answer (research, analysis, briefing), offer to
>    file it to wiki/outputs/ so it compounds into the knowledge base
> --- `pal/instructions.py`

### Routes

#### EPI-RTE-compiler-transform
Label: Compiler content transformation
Part of: [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance)

The parent includes compilation, metadata updates and lint; this part is the raw-to-summary/concept generation step only. Caller/schedule triggers a maintenance request; Compiler model selects uncompiled material and proposes content under incremental, additive and source-tracked instructions. Bound FileTools affords persistence; no per-claim human decision or truth oracle is wired. Open request mode, not a bounded proof domain. Source/body interpretation and cross-source synthesis are not inspectable from prompts alone: candidate relation remains indeterminate among reshaping, entailed derivation and conjecture until actual inputs/outputs are available. Writes are admitted by tools rather than evidence-consuming acceptance. Recovery is later overwrite or separately available Git history, not mandatory automatic rollback. SRC-1 `pal/agents/compiler.py`, `pal/tools/build.py`; parent supplies tool/state-write evidence.

> b. Write a summary to wiki/summaries/{doc-name}.md
> c. Extract key concepts from the document
> --- `pal/agents/compiler.py`

- Immediate return: Proposed article text through tool writes and Compiler response.
- Later read-back: Persisted articles may be read by Navigator and future Compiler/Linter invocations.
- Delegated visibility: Team receives Compiler output; exact forwarding of underlying tool calls is uninspected Agno behavior.
- Selection predicate: Model follows manifest compiled-false guidance; force caller requests all sources instead.
- Invalidation or expiry: Later overwrite is possible; no automatic citation-failure invalidation in inspected tools.
- Activation or effect: Implemented generation configuration and write affordance; actual generated assertions unobserved.
- Evidence limits: No candidate source/output pair, fidelity evaluator result or accepted claim supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

#### EPI-RTE-lint-check
Label: Linter quality checks
Part of: [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance)

This part evaluates rather than writes concept articles. Request or weekly schedule activates Linter model guidance to compare claims across articles, inspect links/inventory, assess overlap, apply a conditional age threshold and a length heuristic, and suggest research. Target/domain distinctions matter: contradictory article claims concern consistency, missing links/orphans concern graph structure, 30-day age in fast-moving fields is a freshness proxy, and fewer than 200 words is an enrichment heuristic. None alone establishes world truth. The evaluator is the configured model reading tool results, not deterministic built-in lint logic. It proposes severity and suggestions; no inspected software vetoes content on its findings. There is no answer oracle. Open maintenance mode, potentially external search for suggestions. Whether any diagnosis is correct or any proposition newly conjectured is not determinable without content. SRC-1 `pal/agents/linter.py`, `pal/tools/build.py`.

> 1. **Contradictions**: Compare claims across concept articles. Flag conflicts with source citations.
> 2. **Stale articles**: Flag concepts not updated in 30+ days where the field moves fast.
> --- `pal/agents/linter.py`

> 5. **Thin articles**: Flag articles under 200 words that could use enrichment.
> --- `pal/agents/linter.py`

- Immediate return: Model-proposed findings/suggestions, then response/report via separate retention part.
- Later read-back: Findings can persist through report or Discovery writes; no mandatory future critique consumer identified.
- Delegated visibility: Leader can receive Linter response; underlying tool-result visibility is external/uninspected.
- Selection predicate: Requested index inventory followed by each concept article, with optional web research.
- Invalidation or expiry: Flags do not automatically withdraw articles or revoke retrieval priority.
- Activation or effect: Check prompts and requisite file/search tools are configured; compliance and diagnostic success unobserved.
- Evidence limits: No checked corpus, report, calibration, external-source validation or resulting repair supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

#### EPI-RTE-lint-retain
Label: Linter report retention
Part of: [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance)

This part persists proposed findings, distinct from their production in [EPI-RTE-lint-check](#epi-rte-lint-check). The Linter model requests save_file and timestamp updates; file/state tools admit them without verifying the diagnoses. Discovery writes use [EPI-RTE-knowledge-write](#epi-rte-knowledge-write), a separate cross-agent mechanism. Report content is advisory to a later reader, not an enforced Compiler input or article veto. The source explicitly asks the Compiler to fix issues but supplies no automatic transfer/repair loop. Caller initiation is not per-finding approval. Model/tool overwrite permits replacement; no automatic rollback on false diagnosis. SRC-1 `pal/agents/linter.py`, `pal/tools/build.py`, `pal/tools/wiki.py`.

> - Do not modify concept articles directly — report findings, let the Compiler fix them
> --- `pal/agents/linter.py`

- Immediate return: Tool save/state confirmation and Linter response.
- Later read-back: File retained for later reads; a required report-to-Compiler consumer is not wired in inspected instructions/callers.
- Delegated visibility: Team may summarize Linter response; exact report forwarding uninspected.
- Selection predicate: Model chooses report text and tool arguments under report-format guidance.
- Invalidation or expiry: Report can be overwritten on later lint; mark_linted changes a timestamp, not article validity.
- Activation or effect: Report persistence and state updates afforded; no completed report observed.
- Evidence limits: Retention does not establish accepted findings, repair or improvement.
- implementation conclusion status: wired
- operation conclusion status: uninspected

#### EPI-RTE-knowledge-write
Label: Routing metadata writes

Distinct cross-agent route: not contained in exactly one supplied route. Overlaps [RT-RTE-navigator-work](runtime.md#rt-rte-navigator-work) and [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance); also Researcher receives the same tool. Unlike deterministic [RT-RTE-context-refresh](runtime.md#rt-rte-context-refresh), model/caller strings become metadata without a fixed-format file derivation. Agent proposes title/content; Python calls knowledge.insert and returns confirmation. No semantic rejection, human veto, provenance check or truth oracle is present in this function. Open requests or maintenance can trigger writes. The proposed content remains caller/model-authored; tool storage adds no warrant. Metadata can target later retrieval directly, including cross-source connections inferred by the agent. Recovery via loader recreate discards the whole vector store rather than selectively rejecting false assertions; ordinary update semantics are dependency-owned. SRC-1 `pal/tools/knowledge.py`, `pal/tools/build.py`, `pal/instructions.py`, `context/load_context.py`.

> knowledge.insert(name=title, text_content=content)
> return f"Knowledge updated: {title}"
> --- `pal/tools/knowledge.py`

> 1. `search_knowledge` — relevant tables, files, sources. **If a `Discovery:`
>    entry exists for this topic, use it to target retrieval directly.**
> --- `pal/instructions.py`

- Immediate return: Knowledge updated confirmation.
- Later read-back: search_knowledge can deliver metadata to future agent calls, which are instructed to target retrieval from Discovery entries.
- Delegated visibility: Writer sees confirmation; whether full inserted content reaches leader is dependency-internal.
- Selection predicate: Model/caller supplies title/content; external hybrid search later selects matches.
- Invalidation or expiry: No per-entry expiry or validation in writer; loader recreate can delete all entries.
- Activation or effect: Metadata insertion wired and shortcut-retrieval instruction configured; actual changed retrieval unobserved.
- Evidence limits: Insert/search behavior, actual records and downstream compliance uninspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected

#### EPI-RTE-learning-adapt
Label: Operational learning adaptation

Distinct from generic [RT-RTE-navigator-work](runtime.md#rt-rte-navigator-work): this cross-agent learning configuration and instruction path also includes leader/Researcher. It is not solely a part of one supplied route. Natural-language guidance requests retained Retrieval/Pattern/Correction entries after interactions; Agno AGENTIC LearningMachine and agentic memory are configured. Source exposes proposal guidance and later precedence, not exact dependency-internal content checks or write/rejection policy. Model is requested to save strategies that worked and explicit user fixes; user authorship of a correction is distinct from per-entry approval. No answer oracle for learning truth is supplied. Open interaction mode; no fixed curriculum. Operational behavioral path: later agent receives/searches learnings, interprets them as retrieval/correction guidance, with requested Correction-over-recency priority across sessions. Retained learning descriptions can be truth-apt; the actual truth-apt generation relation is not determinable from configuration. Direct policy-priority adaptation is independently supported. SRC-1 `pal/instructions.py`, `pal/agents/navigator.py`, `pal/agents/researcher.py`; team configuration supplied by runtime.

> - Strategy worked → `save_learning("Retrieval: ...", "...")`
> - User corrected you → `save_learning("Correction: ...", "...")`
> - Behavioral pattern → `save_learning("Pattern: ...", "...")`
> --- `pal/instructions.py`

> learned_knowledge=LearnedKnowledgeConfig(mode=LearningMode.AGENTIC),
> --- `pal/agents/navigator.py`

Theory-related limits: no actual formulated strategy/pattern was supplied, so theory-builder conditions 1–4 are individually uninspected for retained instances: localized content, content-dependent consumption, criticism with blame/reliance change, and iteration. Prompt categories do not prove a theory. Addressability is afforded by named entries, but their internal scope/assumptions and revision granularity are uninspected. Persistence across interactions is configured, not observed. Learning: improved future capacity unobserved, no attributed improvement evidence. Reflection: metadata/learnings about Pal are afforded, but no observed two-way representation/behavior loop. Autonomy: model-selected updates are afforded, not evidence that computation performs every theory operation. Self-improvement over future sessions has a candidate behavior-shaping path; update determination, changed organization, and later causal exercise are not jointly demonstrated. Neither absence of weights training nor absence of an acceptance gate disproves this potential path. Missing improvement comparisons prevent successful self-improvement attribution.

- Immediate return: uninspected — actual learning-tool result and serialization belong to external Agno.
- Later read-back: Configured learning knowledge store, search_learnings instructions and leader/Researcher learning-context supply; actual selected entries not supplied.
- Delegated visibility: uninspected — dependency controls memory and learning exposure between team/member calls.
- Selection predicate: AGENTIC model choice plus requested search-before-save, correction precedence and recency.
- Invalidation or expiry: Guidance requests verify missing references and update rather than duplicate; no inspected Pal TTL or automatic correction retraction.
- Activation or effect: Learning machinery wired and behavioral-priority instructions supplied; actual retained update and causal reuse unobserved.
- Evidence limits: External implementation and absent user traces prevent exact admission, semantic relation, exercise and benefit conclusions.
- implementation conclusion status: wired
- operation conclusion status: uninspected

#### EPI-RTE-smoke-select
Label: Smoke result continuation
Part of: [RT-RTE-evaluation-driver](runtime.md#rt-rte-evaluation-driver)

This part adds a concrete result consumer to the supplied evaluation container; no supersession is needed. Smoke/extended drivers call the actual team, then deterministic substring and regex checks judge returned text. Check target is lexical content of that response for authored expected/forbidden phrases and patterns, not article truth, source coverage or actual external effects. Software decides PASS/FAIL/ERROR; the test author supplies the oracle predicates. No model judge in this check. In bounded suite mode a PASS admits dependent tests; failed prerequisite causes skip, and the returned session ID can pass into a later team call. This is operative continuation, not acceptance for production use. It can exercise mutable files/DB; cleanup is a separate operation in the parent. No automatic code update, runtime policy installation or rollback consumes a passing result in these runner functions. SRC-1 `evals/smoke.py`, `evals/extended_smoke.py`.

> for pattern in test.response_matches:
>     if not re.search(pattern, response):
>         failures.append(f"NO MATCH: '{pattern}'")
> --- `evals/extended_smoke.py`

> if test.depends_on and test.depends_on not in passed_tests:
>     print(f"  [{test.id}] {test.name}... SKIP (depends on {test.depends_on})")
>     skipped += 1
>     continue
> --- `evals/extended_smoke.py`

> if result.status == "PASS":
>     passed_tests.add(test.id)
> --- `evals/extended_smoke.py`

- Immediate return: Result object with response/failures/status and session ID, then printed report.
- Later read-back: Later dependent cases consume pass membership and session ID within suite; durable runtime result-policy read-back not identified.
- Delegated visibility: Driver receives team response text; internal specialist/tool completeness not inferred from it.
- Selection predicate: Authored cases/dependencies; substring/regex assertions over response and PASS prerequisite membership.
- Invalidation or expiry: Pass/session maps are local to suite; persistent side effects of actual team calls need not expire with those maps.
- Activation or effect: Implemented prerequisite skip/continue enforcement and session reuse; no suite run supplied.
- Evidence limits: Lexical oracle false positives/negatives unmeasured; no truth/citation or external-state guarantee.
- implementation conclusion status: wired
- operation conclusion status: uninspected

### Claims

#### EPI-CLM-compounding-learning
Label: Compounding learning promise

Claimed operation: heterogeneous acquisition and a structured wiki make every interaction improve the next. This is doctrine/design in SRC-1 `docs/SPEC.md`, not measured outcome. Distinct from governance [RT-CLM-control-scope](runtime.md#rt-clm-control-scope); no supplied claim counterpart for general learning benefit. The strongest contrary cases to an unconditional reading are direct stub ingestion, title collisions, metadata deletion on recreate, and advisory lint without required repair. These limit the claim but do not show any deployed interaction worsened performance.

> It navigates heterogeneous data sources — files, email, calendar, SQL, and web — using each source's native query interface. Raw data goes in, a structured wiki comes out, and every interaction compounds. A learning loop ties it together: every interaction improves the next one.
> --- `docs/SPEC.md`

#### EPI-CLM-source-tracking
Label: Compiler source tracking

Claimed operation: every wiki claim links to supporting raw source; contradiction-preserving additive enrichment. Doctrine/design, SRC-1 `pal/agents/compiler.py`. Distinct from governance [RT-CLM-control-scope](runtime.md#rt-clm-control-scope); parent maintenance route already quotes this prescription but declares no matching claim. Tool writes do not inspect whether a linked source actually supports the claim; no actual violating or satisfying article supplied.

> - **Additive**: New information enriches existing articles. Note contradictions, don't silently overwrite.
> - **Source-tracked**: Every claim links back to the raw source that supports it.
> --- `pal/agents/compiler.py`

#### EPI-CLM-wiki-quality
Label: Linter wiki quality

Claimed operation: Linter maintains wiki quality/integrity by checking and reporting. Doctrine/design, SRC-1 `pal/agents/linter.py`. Distinct from [RT-CLM-control-scope](runtime.md#rt-clm-control-scope); related supplied [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance) covers mechanisms rather than a claim record. The source itself limits the promise: suggestions, not direct edits. No stronger guaranteed truth claim is attributed.

> You are the Linter, responsible for wiki quality and integrity.
>
> ## Your Job
> Run health checks on the wiki and produce a lint report.
> --- `pal/agents/linter.py`

### Behavioral-authority paths

none declared in this member; route-local consumers/channels/force/horizon are recorded above, and static instruction authority is see [RT-BAP-agent-guidance](runtime.md#rt-bap-agent-guidance).
