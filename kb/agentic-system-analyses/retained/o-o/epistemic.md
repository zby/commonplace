---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "o-o epistemic routes: web research, source validity guidance, direct admission and later reliance at the frozen commit."
run-id: AAS-2026-10-15-o-o-b6fd0055e5c1-01
reviewed-boundary: b0d5063e37b4eafdbc23c1899a31f1836168b989
---

# o-o epistemic report

## Source-and-claim boundary

The question is how o-o's living articles acquire claims, check them and authorize later reliance. Scope and exclusions: see [boundary](boundary.md#boundary-and-evidence); source identity and evidence layers: see [Source register](boundary.md#source-register). This is the shipped document workflow, including its library manager, not Claude Code's internal agent loop or the research web. All source anchors below use SRC-1 at the reviewed commit. No execution or causal experiment is supplied. Populated caches establish available candidate instances, not the provenance, evaluation or acceptance of those instances.

The consequential public claim is [RT-CLM-living-document](runtime.md#rt-clm-living-document). Additional design claims concern incremental research and conditional source preservation: [EPI-CLM-research-reuse](#epi-clm-research-reuse). There is no need to interpret either as a claim of infallible knowledge production.

| Entry point or operation | Source path | Coverage and record | Inspection basis and limit |
|---|---|---|---|
| Default article, force, agent/model dispatch | `example/index.o-o.html` | [RT-RTE-document-update](runtime.md#rt-rte-document-update) | Direct read of argument parsing, freshness, complete dispatch and final action switch; supplied runtime supplies external-loop limits. |
| New article, interactive creation, update-all | `example/index.o-o.html` | [RT-RTE-batch-create](runtime.md#rt-rte-batch-create) | Supplied runtime; direct final switch confirms interactive branch and child invocation. Template generation and batch internals not independently reread; no independent claim of successful operation. |
| Research, article rewriting, cache and changelog maintenance | `example/anthropic-leadership.o-o.html` | [EPI-RTE-web-research](#epi-rte-web-research), [EPI-RTE-source-check](#epi-rte-source-check), [EPI-RTE-document-retention](#epi-rte-document-retention) | Direct complete ordinary contract, cache and changelog read. Article factual accuracy not assessed. |
| AGI and incarceration sentinel checks | `example/agi-declared.o-o.html`, `example/trump-incarceration.o-o.html` | [EPI-RTE-sentinel-check](#epi-rte-sentinel-check), [EPI-RTE-sentinel-selection](#epi-rte-sentinel-selection) | Direct complete contracts; no external event evidence or reference-answer oracle. |
| Image verification, size rejection, cleanup | `example/index.o-o.html` | [EPI-RTE-image-check](#epi-rte-image-check), [EPI-RTE-image-selection](#epi-rte-image-selection) | Direct dispatch prompt read. These are instructions to the agent, not checks executed by the driver. |
| Set/add/remove guidance | `example/index.o-o.html` | [RT-RTE-contract-edit](runtime.md#rt-rte-contract-edit) | Direct complete editor functions and dispatch. Includes whole-line removal outside the named array. |
| Sync shared code | `example/index.o-o.html`, `README.md` | [RT-RTE-code-sync](runtime.md#rt-rte-code-sync) | Supplied implementation account and direct README; operator propagation, not a research evaluator. |
| Index projection | `example/index.o-o.html` | [EPI-RTE-index-excerpt](#epi-rte-index-excerpt) | Direct complete rebuild function; concrete deduction below. |
| Browser and --show | `example/index.o-o.html` | [RT-RTE-library-read](runtime.md#rt-rte-library-read), [RT-RTE-contract-edit](runtime.md#rt-rte-contract-edit) | Supplied browser findings; direct --show implementation. Projection/display, not endorsement. |
| Help and unknown options | `example/index.o-o.html` | [RT-RTE-document-update](runtime.md#rt-rte-document-update) | Direct dispatch: help displays usage; unknown options reject before research. No independent epistemic evaluator. |
| External tools, hooks and provider state | `example/index.o-o.html` | [RT-CMP-claude](runtime.md#rt-cmp-claude), [RT-BAP-update-prompt](runtime.md#rt-bap-update-prompt) | Direct requested tools: Bash, Read, Edit, WebSearch, WebFetch. No o-o tool registration or hook branch in the inspected dispatch; external registrations and implementation remain uninspected, preventing a whole-enclosing-runtime negative. |

Missing web-page contents prevent checking factual support, source independence and source warrant. Missing agent traces prevent identifying actual fetched evidence, candidate transformations, rejections, accepted propositions and later activation. Missing provider internals prevent judgments about parameter updates or internal evaluation; model mutability fields: see [RT-CMP-claude](runtime.md#rt-cmp-claude). No material omitted operation is established within the shipped boundary; independence of browser/template/batch details relies on the supplied runtime, not a new exhaustive audit.

## Epistemic-object inventory

Each row names a material part, not a uniform knowledge store. Identity, form and substrate are owned by its linked record.

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-article](#epi-obj-article) | Assertions about the configured topic | see record | SRC-1 `example/anthropic-leadership.o-o.html` | Source truth and exact production edge unestablished. |
| [EPI-OBJ-source-cache](#epi-obj-source-cache) | Sources and factual summaries | see record | SRC-1 `example/anthropic-leadership.o-o.html` | Flat facts do not supply per-fact support or acceptance. |
| [EPI-OBJ-manifest](#epi-obj-manifest) | Date/version assertions about document maintenance | see record | SRC-1 `example/index.o-o.html` | Update date is not a factual-validity judgment. |
| [EPI-OBJ-changelog](#epi-obj-changelog) | Attributed claims about prior edits | see record | SRC-1 `example/anthropic-leadership.o-o.html` | No execution-linked audit provenance. |
| [EPI-OBJ-contract](#epi-obj-contract) | Mostly non-truth-apt policy; sentinel includes dated event assumptions | see record | SRC-1 `example/agi-declared.o-o.html` | Supplied initial non-event premise is not independently verified. |
| [EPI-OBJ-image](#epi-obj-image) | Captions and source attributions; image bytes alone need an interpretation | see record | SRC-1 `example/index.o-o.html` | File-type and size checks cannot establish caption truth or relevance. |
| [RT-OBJ-shared-shell](runtime.md#rt-obj-shared-shell) | None as executable policy | see record | SRC-1 `example/index.o-o.html` | Changes execution authority, not research warrant. |

## Authority-route ledger

The ledger separates functions even when the same delegate performs them. Fields owned by a declaration say see; architectural status and content/update relation are this overlay's assessments. A doctrine-only entry means the requested agent action, not the implemented delivery of its prompt.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [EPI-RTE-web-research](#epi-rte-web-research) | content transformation | doctrine only | [EPI-OBJ-article](#epi-obj-article), [EPI-OBJ-source-cache](#epi-obj-source-cache) | truth-apt transformation: acquisition/import | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1 `example/anthropic-leadership.o-o.html` | [RT-CLM-living-document](runtime.md#rt-clm-living-document) | none | Source warrant unknown; imported content is acquired, not newly established. |
| [EPI-RTE-web-research](#epi-rte-web-research) | content transformation | doctrine only | [EPI-OBJ-article](#epi-obj-article) | truth-apt transformation: indeterminate | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1 `example/anthropic-leadership.o-o.html` | [RT-CLM-living-document](runtime.md#rt-clm-living-document) | none | Article synthesis may reshape, derive or conjecture; no linked input/output proves which. |
| [EPI-RTE-source-check](#epi-rte-source-check) | check/evidence production | doctrine only | [EPI-OBJ-source-cache](#epi-obj-source-cache) | no content change | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1 `example/anthropic-leadership.o-o.html` | [EPI-CLM-research-reuse](#epi-clm-research-reuse) | none | No explicit validity test or checked source outcome. |
| [EPI-RTE-source-selection](#epi-rte-source-selection) | disposition/acceptance | doctrine only | [EPI-OBJ-source-cache](#epi-obj-source-cache) | no content change | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1 `example/anthropic-leadership.o-o.html` | [EPI-CLM-research-reuse](#epi-clm-research-reuse) | none | Conditional preservation, not evidenced claim acceptance. |
| [EPI-RTE-document-retention](#epi-rte-document-retention) | retention | implemented | [EPI-OBJ-article](#epi-obj-article), [EPI-OBJ-source-cache](#epi-obj-source-cache), [EPI-OBJ-manifest](#epi-obj-manifest), [EPI-OBJ-changelog](#epi-obj-changelog) | no content change | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1 `example/index.o-o.html` | [RT-CLM-living-document](runtime.md#rt-clm-living-document) | none | Driver enables direct persistence; external edits and successful adherence not observed. |
| [EPI-RTE-cache-reuse](#epi-rte-cache-reuse) | operational admission/selection/consumption | doctrine only | [EPI-OBJ-source-cache](#epi-obj-source-cache), [EPI-OBJ-manifest](#epi-obj-manifest) | no content change | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1 `example/anthropic-leadership.o-o.html` | [EPI-CLM-research-reuse](#epi-clm-research-reuse) | none | Prompt requests reliance; activation is unobserved. |
| [EPI-RTE-sentinel-check](#epi-rte-sentinel-check) | check/evidence production | doctrine only | [EPI-OBJ-contract](#epi-obj-contract), [EPI-OBJ-article](#epi-obj-article) | no content change | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1 `example/agi-declared.o-o.html`, `example/trump-incarceration.o-o.html` | none | none | Event occurrence and credibility are separate from AGI actually existing or legal predictions being true. |
| [EPI-RTE-sentinel-selection](#epi-rte-sentinel-selection) | behavior/policy adaptation | doctrine only | [EPI-OBJ-contract](#epi-obj-contract) | non-truth-apt policy/content update: choose concise status or comprehensive event coverage | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1 `example/agi-declared.o-o.html`, `example/trump-incarceration.o-o.html` | none | none | Local article-writing policy selection, not revision of the maintenance method. |
| [EPI-RTE-image-check](#epi-rte-image-check) | check/evidence production | doctrine only | [EPI-OBJ-image](#epi-obj-image) | no content change | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1 `example/index.o-o.html` | none | none | Check domain is file type and byte size, not visual truth. |
| [EPI-RTE-image-selection](#epi-rte-image-selection) | disposition/acceptance | doctrine only | [EPI-OBJ-image](#epi-obj-image) | no content change | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1 `example/index.o-o.html` | none | none | Skip/reduce/cleanup instructions do not establish observed rejection or epistemic acceptance. |
| [EPI-RTE-index-excerpt](#epi-rte-index-excerpt) | content transformation | implemented | [EPI-OBJ-article](#epi-obj-article) | truth-apt transformation: indeterminate | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1 `example/index.o-o.html` | none | none | Literal truncation and removed citations need not preserve meaning or support. |
| [RT-RTE-document-update](runtime.md#rt-rte-document-update) | operational admission/selection/consumption | implemented | [EPI-OBJ-manifest](#epi-obj-manifest) | no content change | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1 `example/index.o-o.html` | [RT-CLM-living-document](runtime.md#rt-clm-living-document) | none | Freshness gates expenditure, not truth. |
| [RT-RTE-library-read](runtime.md#rt-rte-library-read) | operational admission/selection/consumption | implemented | [EPI-OBJ-article](#epi-obj-article), [EPI-OBJ-manifest](#epi-obj-manifest) | no content change | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1 `example/index.o-o.html` | none | none | Rendering and date-ranked cards supply visibility, not warrant. |
| [RT-RTE-contract-edit](runtime.md#rt-rte-contract-edit) | behavior/policy adaptation | implemented | [EPI-OBJ-contract](#epi-obj-contract) | non-truth-apt policy/content update: operator changes guidance or scalar controls | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1 `example/index.o-o.html` | none | none | Operator admission; no evaluation-responsive method revision established. |
| [RT-RTE-code-sync](runtime.md#rt-rte-code-sync) | operational admission/selection/consumption | implemented | [RT-OBJ-shared-shell](runtime.md#rt-obj-shared-shell) | non-truth-apt policy/content update: replace shared executable or presentation blocks | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1 `example/index.o-o.html` | none | none | Marker checks authorize copying, not behavioral correctness. |

No evidence-consuming claim acceptance followed by lifecycle integration is established in the inspected driver and contracts. This does not imply that the external agent cannot evaluate or reject claims. Conditional source preservation and sentinel checks are counterexamples to a broader claim that the workflow requests no evaluation at all. Citation links, cache retention and in-place admission are not substitutes for that missing acceptance evidence.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-living-document](runtime.md#rt-clm-living-document) | see record | SRC-1 `README.md`; doctrine/design | see record | [RT-RTE-document-update](runtime.md#rt-rte-document-update), [RT-RTE-library-read](runtime.md#rt-rte-library-read) | None supplied | No comparison; external agent compliance required | Runnable dispatch and retained browser-readable artifact are supported capacities | Factual freshness, successful research and quality unobserved; invocation is required. |
| [EPI-CLM-research-reuse](#epi-clm-research-reuse) | see record | SRC-1 `example/anthropic-leadership.o-o.html`; doctrine/design | see record | [EPI-RTE-document-retention](#epi-rte-document-retention), [RT-RTE-document-update](runtime.md#rt-rte-document-update) deliver the request and persistence path | Candidate cache and attributed changelog only; no observed route | No intervention or component comparison | Prior facts are available; later reuse and conditional validity selection are explicitly requested | No demonstrated incremental-reuse benefit, source validation or evidence-consuming acceptance. |

## Bounded conclusion

The driver delegates web acquisition and article editing, retains the result directly, and exposes it to readers, index projection and subsequent updates. Acquired sources carry unknown warrant here: links and domain preferences preserve some attribution but the research pages and actual tool outputs are not supplied. The representative cache even uses broad domain strings and flat facts rather than the requested structured source entries. See [EPI-OBJ-source-cache](#epi-obj-source-cache). This qualifies provenance, not the existence of a reuse instruction.

The requested source-validity and event checks have consequential consumers: preservation of old sources and selection of concise versus comprehensive reporting. Their evaluators are the external agent using web evidence. No reference-answer oracle, fixed factual acceptance criterion or recorded evidence-consuming claim acceptance is established. Image checks target format and size and can select reduction or rejection; they do not license factual reliance on captions. The shell's successful-return message and freshness gate are operational signals, not acceptance of claims. See the separate check and disposition records above.

No produced ampliative claim is established as accepted within a named criterion, intended use and scope. No warranted entailed research derivation is established either: accessible artifacts lack route-linked premises and checked interpretations. Article synthesis remains indeterminate between reshaping, derivation and conjecture, rather than being classified as ampliative solely because entailment is unknown. Index extraction is deterministically reconstructible, but its arbitrary truncation and citation removal do not guarantee semantic preservation. See [EPI-RTE-index-excerpt](#epi-rte-index-excerpt).

Retention can guide later research without acceptance: the cache is requested background, and the date narrows attention to changes. That is a potential behavioral-authority path across invocations, not demonstrated learning or improved capacity. Sentinel branch selection directly changes writing policy; operator contract editing and shared-code synchronization change guidance/machinery without an evidenced automatic criticism loop. Model parameter changes and internal criticism remain uninspected. These limits do not collapse autonomy, reflection, learning and self-improvement into one verdict: agent-owned research decisions, retained factual material and explicit operator maintenance are independently supported; successful learning, formulated iterative criticism and exercised evidence-responsive self-improvement are not established by these sources. See [RT-CMP-claude](runtime.md#rt-cmp-claude), [RT-RTE-contract-edit](runtime.md#rt-rte-contract-edit) and [RT-RTE-code-sync](runtime.md#rt-rte-code-sync).

## Shared records

### Operative objects

#### EPI-OBJ-article
Label: Article content

Source-native identity: `<article id='article'>` content, natural-language assertions encoded as HTML in a local `.o-o.html` file. Browser markup is symbolic; factual prose is interpreted by readers and the external model. Distinct from [RT-OBJ-shared-shell](runtime.md#rt-obj-shared-shell), which expressly excludes article content. Claimed role: reader-facing topic report and previous context for later research. SRC-1 `example/anthropic-leadership.o-o.html`; the contract passage in [EPI-RTE-web-research](#epi-rte-web-research) supports the producer and consumer request. No factual accuracy is inferred.

#### EPI-OBJ-source-cache
Label: oo-source-cache

Source-native identity: JSON block `oo-source-cache`; local text substrate. JSON structure is symbolic, while `facts` and informal source descriptions are natural-language material consumed by the research agent. Distinct from the shared-shell object; no supplied object counterpart after comparison with [RT-OBJ-shared-shell](runtime.md#rt-obj-shared-shell). Claimed role: previous sources/facts for reuse. SRC-1 `example/anthropic-leadership.o-o.html`.

The sample has no per-fact citation map, acceptance decision or route provenance. It differs from the contract's requested URL/title/tier/access-date entries. Those fields' absence in this sample does not establish all caches lack them.

>     "anthropic.com/company",
>     "en.wikipedia.org/wiki/Anthropic",
>     "anthropic.com/news (multiple)",
> --- `example/anthropic-leadership.o-o.html:498-500`

>     "Anthropic closed $30B Series G at $380B valuation (Feb 2026)",
> --- `example/anthropic-leadership.o-o.html:511-511`

#### EPI-OBJ-manifest
Label: oo-manifest

Source-native identity: `oo-manifest` JSON block, local symbolic metadata with title, version, `as_of` and update interval. Claimed role: date/version reporting and update selection. Distinct from [RT-OBJ-shared-shell](runtime.md#rt-obj-shared-shell); it is the data consumed by [RT-RTE-document-update](runtime.md#rt-rte-document-update) and [RT-RTE-library-read](runtime.md#rt-rte-library-read), not their executable rules. SRC-1 `example/index.o-o.html`; evidence passages in those supplied records and [EPI-RTE-document-retention](#epi-rte-document-retention). Maintenance-date claims are not factual validation of article contents.

#### EPI-OBJ-changelog
Label: oo-changelog

Source-native identity: local `oo-changelog` JSON array; symbolic fields hold natural-language edit summaries. Claimed role: attributed edit history. Distinct from [RT-OBJ-shared-shell](runtime.md#rt-obj-shared-shell). SRC-1 `example/anthropic-leadership.o-o.html`. Available entries do not authenticate the described execution or criticism.

>     "summary": "Initial document creation with full coverage of leadership team, board of directors, and research leadership.",
> --- `example/anthropic-leadership.o-o.html:552-552`

#### EPI-OBJ-contract
Label: oo-contract

Source-native identity: local `oo-contract` JSON, symbolic fields carrying natural-language role, research policy, identity, procedure and image rules. Claimed role: task instructions. Separate from the template-bearing [RT-OBJ-shared-shell](runtime.md#rt-obj-shared-shell): this denotes the instantiated document contract, not the generator. The external agent interprets it; scalar budget is also consumed by shell extraction. Sentinel text contains a creation-time event premise and a prospective checking policy. SRC-1 `example/anthropic-leadership.o-o.html`, `example/agi-declared.o-o.html`, `example/trump-incarceration.o-o.html`. Evidence: [EPI-RTE-source-check](#epi-rte-source-check), [EPI-RTE-sentinel-check](#epi-rte-sentinel-check), [RT-BAP-update-prompt](runtime.md#rt-bap-update-prompt). Delivery is not enforcement.

#### EPI-OBJ-image
Label: Embedded research image

Source-native identity: requested downloaded image, resized temporary file, embedded base64 image and HTML caption/source link. Storage spans temporary local files and the persistent article; image payload is symbolic file-format data, captions are natural language. Claimed role: reader enrichment and illustrated attribution. Distinct from [RT-OBJ-shared-shell](runtime.md#rt-obj-shared-shell); article material, not shared machinery. SRC-1 `example/index.o-o.html`; supporting passages: [EPI-RTE-image-check](#epi-rte-image-check) and [EPI-RTE-image-selection](#epi-rte-image-selection). No image-content validation or execution provenance established.

### Routes

#### EPI-RTE-web-research
Label: Web research and article writing
Part of: [RT-RTE-document-update](runtime.md#rt-rte-document-update)

Subroute: instantiated contract → external model selects web evidence → article and fact candidates. Owner is external agent, guided by topic, intents, source policy, format and budget. Separate edges are acquisition/import with unknown source warrant and synthesis with indeterminate semantic relation. Without input/output traces, synthesis cannot be distinguished as reshaping, entailed derivation or ampliative conjecture. Claimed intended use is a current topic report, not a formal proof.

- implementation conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: requested updated article and facts; actual model/tool output uninspected.
- Later read-back: local article/cache requested as background on later updates, and article is browser-readable.
- Delegated visibility: path-first prompt requests entire-file reading and exposes web/file tools through external Claude.
- Selection predicate: document identity, intents, source preferences/denials and date-focus instructions; actual web selection uninspected.
- Invalidation or expiry: subsequent research may replace old assertions; no deterministic fact expiry or withdrawal procedure is specified.
- Activation or effect: prompt delivery is wired by parent; research and successful edits are not observed.
- Evidence limits: SRC-1 doctrine/design, not inspected external search/model implementation or observed production provenance.

The agent proposes/selects claims and writes via tools. Starting the workflow is not human per-claim approval. There is no supplied reference-answer oracle. Operating mode is open-ended research; sentinel-specific mode is split below. No checked argument from warranted premises can be reconstructed from this instruction alone.

>       "4. Using the identity and research fields below, search the web for current information. On subsequent runs, focus on what changed SINCE the as_of date. If there is little new information to report, use remaining budget to enrich the article: add images, improve entity links, or add missing context rather than making only a minimal changelog entry.",
> --- `example/anthropic-leadership.o-o.html:429-429`

>       "5. Write the article content as HTML inside the <article id='article'> element. Use <h2 id='section-id'> for each section listed in required_sections. Use <h3> for subsections. Precede every <p> with a <!-- pid:section-id:8hexchars --> comment for stable paragraph IDs.",
> --- `example/anthropic-leadership.o-o.html:430-430`

#### EPI-RTE-source-check
Label: Source validity assessment
Part of: [RT-RTE-document-update](runtime.md#rt-rte-document-update)

Subroute target: whether previous sources remain valid for the document's research. Evaluator: external model using unspecified judgment and any fetched evidence. Preferences and denials guide source choice, not an implemented HTTP/domain filter. Condition domain is document research; there is no formal validity definition or expected-answer oracle. Possible result: source still valid or not; disposition is separate below. SRC-1 `example/anthropic-leadership.o-o.html`, doctrine/design.

- implementation conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: requested source-validity judgment; no recorded per-source assessment supplied.
- Later read-back: inapplicable — this checking step itself specifies no retained check result; retained sources belong to the selection/retention routes.
- Delegated visibility: prior cache and source policy reach the agent only if it reads them as requested.
- Selection predicate: previous sources and document source guidance.
- Invalidation or expiry: validity can be reconsidered on updates; no automatic expiry criterion.
- Activation or effect: judgment is intended to inform source preservation; actual assessment unobserved.
- Evidence limits: no test method, checked source evidence or result-level provenance.

>       "10. Update oo-source-cache: record all sources you used (url, title, tier, accessed date). Preserve previous sources that are still valid.",
> --- `example/anthropic-leadership.o-o.html:435-435`

>       "prefer_domains": ["anthropic.com", "reuters.com", "bloomberg.com", "nytimes.com", "washingtonpost.com", "techcrunch.com", "theverge.com", "wired.com"],
>       "deny_domains": ["reddit.com", "quora.com", "medium.com"],
>       "require_https": true
> --- `example/anthropic-leadership.o-o.html:457-459`

#### EPI-RTE-source-selection
Label: Conditional source preservation
Part of: [RT-RTE-document-update](runtime.md#rt-rte-document-update)

Subroute from source-validity judgment to requested cache membership; same underlying instruction as [EPI-RTE-source-check](#epi-rte-source-check), different function. Agent proposes, decides and can omit sources; no per-source human approval, independent veto or answer oracle. Criterion is loosely stated continuing validity, intended use is subsequent topic research, scope is prior sources. This is not a recorded evidence-consuming acceptance of a proposition. Explicit invalid-source deletion, dependent-claim withdrawal and automatic rollback are not specified. SRC-1 `example/anthropic-leadership.o-o.html`; exact supporting passage in the check record.

- implementation conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: requested preservation of still-valid sources and recording of newly used ones.
- Later read-back: cache membership is requested input to later research.
- Delegated visibility: agent sees cache and its own assessment, subject to actual reading.
- Selection predicate: still valid for old sources; used during research for new sources.
- Invalidation or expiry: future agent edits may change membership; no hard TTL or revocation cascade.
- Activation or effect: retained membership can influence later selection; activation unobserved.
- Evidence limits: no recorded source dispositions or operational rejection trace; preservation does not warrant associated flat facts.

#### EPI-RTE-document-retention
Label: In-place document retention
Part of: [RT-RTE-document-update](runtime.md#rt-rte-document-update)

Subroute: external file edits → original persistent document → later Bash/browser/agent consumers. Owner of content selection and physical writes is the external agent; the local driver calls it without a candidate/commit or acceptance transaction. This route is implemented as direct file-target dispatch, not as a verified editor implementation. Requests cover article, cache, manifest and changelog. No per-edit user veto or post-edit acceptance test is implemented in this driver; failures do not restore previous content. Intended output is a living research article. Retention itself supplies no epistemic license. SRC-1 `example/index.o-o.html` implementation, `example/anthropic-leadership.o-o.html` doctrine/design. Parent passage establishes direct-edit guidance and lack of a post-edit check.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: external CLI return followed on success by a completion message; edits, if made, remain in original file.
- Later read-back: browser/index consume local content; next update is requested to read manifest/cache and whole file.
- Delegated visibility: absolute target path, contract-reading instruction and file/web tool request.
- Selection predicate: parent dispatch admission; external model decides individual edits under contract guidance.
- Invalidation or expiry: later edits can overwrite content; no automatic claim invalidation, rollback or retained previous version by this driver.
- Activation or effect: wiring admits in-place writes; persisted candidates are available but their producing routes and compliance are unobserved.
- Evidence limits: implementation of external editing and actual resulting changes uninspected; cache/changelog are not execution traces.

>       "9. Update oo-manifest: increment version, set as_of to today (YYYY-MM-DD).",
> --- `example/anthropic-leadership.o-o.html:434-434`

>       "11. Update oo-changelog: append an entry with version, timestamp, and summary of what changed.",
> --- `example/anthropic-leadership.o-o.html:436-436`

#### EPI-RTE-cache-reuse
Label: Previous research reuse
Part of: [RT-RTE-document-update](runtime.md#rt-rte-document-update)

Subroute: cache/manifest → requested agent reads → narrowed subsequent research. Consumer is the external research agent; channel is in-file instruction and read content; force is advisory task guidance; horizon crosses document-update invocations. Flat cached facts have requested background authority, not demonstrated acceptance. Date is a research-focus control, not a freshness guarantee for every fact. SRC-1 `example/anthropic-leadership.o-o.html`; supporting whole-file/cache read passage in parent plus the web-research passage above.

- implementation conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: requested reuse of sources/facts and focus on changes since as_of.
- Later read-back: previous retained cache and manifest reach a later invocation if the requested reads occur.
- Delegated visibility: entire-file read requested; actual model context and omission uninspected.
- Selection predicate: prior research and date; actual within-cache selection is model-owned and uninspected.
- Invalidation or expiry: source validity is reconsidered under source-selection guidance; no fact-level invalidation mechanism specified.
- Activation or effect: reuse can shape what is searched and rewritten; delivered-cache dependence is not observed.
- Evidence limits: available facts do not prove reuse, reduced cost, improved quality or changed behavior.

#### EPI-RTE-sentinel-check
Label: Sentinel event assessment
Part of: [RT-RTE-document-update](runtime.md#rt-rte-document-update)

Subroute targets differ: formal/credible AGI declaration by a major company/lab, and actual incarceration of Donald Trump. Both are open web checks delegated to the model, not fixed answer oracles or deterministic shell branches. Possible yes/no outcome is intended to guide writing; it does not prove AGI capability or future legal events. Owner and evaluator are external agent. SRC-1 doctrine/design `example/agi-declared.o-o.html`, `example/trump-incarceration.o-o.html`; parent record quotes AGI premise. The domains differ but warrant and force are identical; no system-wide event detector is inferred.

- implementation conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: requested event determination from web research.
- Later read-back: inapplicable — no separate structured event-check result is specified; resulting article persistence is separate.
- Delegated visibility: event policy and topic arrive through requested contract reading.
- Selection predicate: sentinel subject and research intents.
- Invalidation or expiry: check is requested again on subsequent updates; initial non-event premise alone cannot establish later status.
- Activation or effect: result is intended to select reporting mode; no observed evaluation or activation.
- Evidence limits: evidence sufficiency, credibility threshold and external event truth remain unverified.

>       "5. SENTINEL CHECK: Search for whether any major AI company or lab has formally declared they have achieved AGI. If NO — keep the article concise. State upfront that no credible declaration has been made. List only the leading candidates, their latest capabilities, and what gaps remain. Do NOT write lengthy background on AI history. If YES — this is now a major event. Provide comprehensive coverage: who declared it, what definition they used, what evidence they presented, how the scientific community responded, and who disputes the claim.",
> --- `example/agi-declared.o-o.html:383-383`

>       "5. SENTINEL CHECK: Search for whether Trump has actually been incarcerated. If NO — keep the article concise and factual. State upfront that incarceration has not occurred. List only active cases, upcoming court dates, and realistic legal paths. Do NOT write lengthy background sections. If YES — this is now a major event. Provide comprehensive coverage: when, where, circumstances, reactions, legal basis, what happens next.",
> --- `example/trump-incarceration.o-o.html:351-351`

#### EPI-RTE-sentinel-selection
Label: Sentinel reporting selection
Part of: [RT-RTE-document-update](runtime.md#rt-rte-document-update)

Subroute from event judgment to concise status or comprehensive coverage. Computational selector is the instructed external agent; human supplies initial topic/instructions, not a per-event decision. It can revise article output; no o-o separate veto, rollback or expected-answer oracle. This is operational branch authority over scope and length, not epistemic acceptance of the event as true. Consumer: same writing agent; channel: conditional contract instruction; force: advisory, not shell enforcement; horizon: current update, with changed article retained. SRC-1 anchors and passages: [EPI-RTE-sentinel-check](#epi-rte-sentinel-check). No method revision is requested.

- implementation conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: requested concise non-event report or comprehensive event report.
- Later read-back: selected article persists for later readers/updates; no distinct durable mode field specified.
- Delegated visibility: check result resides in external agent processing, uninspected.
- Selection predicate: model's no/yes event judgment under sentinel instruction.
- Invalidation or expiry: next update can change report when event status changes.
- Activation or effect: writing scope is intended to change; actual branch execution unobserved.
- Evidence limits: possible policy adaptation does not establish factual event acceptance or exercised self-improvement.

#### EPI-RTE-image-check
Label: Image format and size check
Part of: [RT-RTE-document-update](runtime.md#rt-rte-document-update)

Subroute target: downloaded/resized image file type and size relative to `max_file_kb`. Evaluator: agent-interpreted `file` result and size measurement, with measurement command unspecified. Domain is format/bytes, not source truth, license, caption accuracy or causal relevance. Agent executes requested external tools if it follows the prompt; o-o does not call these checks itself. SRC-1 `example/index.o-o.html`, doctrine/design.

- implementation conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: requested file-type/size observations.
- Later read-back: inapplicable — check outputs have no specified persisted audit field.
- Delegated visibility: tool results would reach external agent; actual tool transcript unavailable.
- Selection predicate: contract allows images and agent selects a download.
- Invalidation or expiry: new or resized bytes require rechecking; no automatic ongoing image validation.
- Activation or effect: output is intended to guide resizing/skipping and embedding.
- Evidence limits: no executed check, actual measurement, result or enforcement established.

> - Verify it is an image: file /tmp/oo_img_N.ext
> --- `example/index.o-o.html:1054-1054`

> - Check size: if over max_file_kb, reduce further or skip
> --- `example/index.o-o.html:1058-1058`

#### EPI-RTE-image-selection
Label: Image reduction and rejection
Part of: [RT-RTE-document-update](runtime.md#rt-rte-document-update)

Subroute: format/size results → agent reduces, skips or embeds selected bytes; later temporary-file cleanup. Agent proposes, decides and can reject; user supplies contract bounds, no per-image approval. Intended use is browser illustration, criterion is bounded format/size suitability. This licenses operational embedding at most, not acceptance of factual captions. No expected-answer oracle or automatic rollback. Prompt controls behavior by advisory instructions for one update; embedded result survives later opens. SRC-1 `example/index.o-o.html`; check passage above and cleanup below.

- implementation conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: requested embedded image, reduced candidate or skipped candidate, and temporary-file removal.
- Later read-back: embedded data/caption/source link persist in article; temporary files are requested removed.
- Delegated visibility: check outputs and image rules reach agent if executed/read.
- Selection predicate: image allowance, relevance guidance and size bound; external agent decides.
- Invalidation or expiry: subsequent article edit may replace/remove image; no dependent-caption withdrawal protocol specified.
- Activation or effect: requested reduction/rejection changes what is embedded; actual result unobserved.
- Evidence limits: cleanup is not research-source retraction or epistemic rollback; compliance unobserved.

> - Clean up: rm /tmp/oo_img_N*
> --- `example/index.o-o.html:1061-1061`

#### EPI-RTE-index-excerpt
Label: Index excerpt projection
Part of: [RT-RTE-library-read](runtime.md#rt-rte-library-read)

Subroute: discovered article → first matching paragraph line → stripped/truncated excerpt → persisted date-ranked card → browser reader. Owner is deterministic shell/awk code. Check target/evaluator: inapplicable as a truth check; syntactic extraction and top-eight date selection only. No epistemic license; operational authority supplies prominent navigation/excerpt text. Channel is index HTML, force is ranking/display, horizon later browser opens until rebuild. This is a part of the supplied projection route, not a duplicate whole-route declaration. SRC-1 `example/index.o-o.html`, implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: first matching paragraph line stripped of tags and citation markers, truncated to 120 characters, with ellipsis when nonempty.
- Later read-back: rewritten index cards persist for later browser opens; full article stays available by link.
- Delegated visibility: inapplicable — projection has no model delegate.
- Selection predicate: first line matching literal <p> inside article range; top eight cards sorted by extracted date.
- Invalidation or expiry: next index rebuild replaces projection; no factual revalidation.
- Activation or effect: code determines excerpt delivery/ranking; browser operation unobserved.
- Evidence limits: lossy text need not preserve proposition scope or support; nested link accuracy remains limited as in parent.

>     excerpt=$(awk '/<article/,/<\/article/{if(/<p>/){gsub(/<[^>]*>/,"");gsub(/&amp;/,"\\&");gsub(/&mdash;/,"—");gsub(/\[s[0-9]+\]/,"");gsub(/^[[:space:]]+|[[:space:]]+$/,"");print substr($0,1,120);exit}}' "$file")
> --- `example/index.o-o.html:621-625`

Implementation deduction, without target execution: input line `<p>A is true [s1].</p>` in an article range loses its tags and `[s1]`, yielding `A is true .`; because it is nonempty, the next code line appends `...`. The visible card thus does not carry the citation marker. Longer lines are cut at 120 characters even if a qualification follows. This proves lossy extraction, not that any particular shipped excerpt is false. Semantic preservation is indeterminate; some inputs are harmless reshaping, others lose essential scope.

### Claims

#### EPI-CLM-research-reuse
Label: Incremental prior research reuse

Claimed operation: subsequent research should build on prior sources and facts, focus on changes since last update and preserve still-valid sources. SRC-1 `example/anthropic-leadership.o-o.html`, doctrine/design. Closest supplied claim [RT-CLM-living-document](runtime.md#rt-clm-living-document) describes self-updating documents generally; this record isolates the narrower cross-update reliance and validity claim, not a duplicate public self-update slogan. Implemented delivery: parent dispatch; requested execution: [EPI-RTE-cache-reuse](#epi-rte-cache-reuse), [EPI-RTE-source-check](#epi-rte-source-check), [EPI-RTE-source-selection](#epi-rte-source-selection). Passage for conditional preservation is in source-check; incremental reuse is quoted below.

>       "3. Read the oo-source-cache JSON block to see what sources and facts were gathered previously. Build on prior research, do not start from scratch.",
> --- `example/anthropic-leadership.o-o.html:428-428`
