---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "llm-wiki epistemic routes: imported and caller-authored claims, structural checks, trust labels, retirement and consequential host delivery."
run-id: AAS-2026-11-08-llm-wiki-97b740596442-01
reviewed-boundary: f70e680d852a78d48504425d87252531e68c5624
---

# llm-wiki epistemic report

## Source-and-claim boundary

This report asks what licenses reliance on llm-wiki's retained knowledge and how results reach later behavior. Scope and frozen evidence are those of [boundary](boundary.md#boundary-and-evidence); source identity and layers are in its [Source register](boundary.md#source-register). All source citations below use SRC-1. Direct inspection supplies implementation deductions and doctrine/design, never observed operation. External hosts, models, real bundles and remote services remain outside the frozen implementation. No run trace or causal experiment was supplied.

The assessed families are caller-authored concepts, raw-source registration, metadata and link reshaping, diagnostics, write admission, retirement, synchronization and instruction delivery. Public claims include [RT-CLM-form-equivalence](runtime.md#rt-clm-form-equivalence), [EPI-CLM-format-check](#epi-clm-format-check), [EPI-CLM-knowledge-recording](#epi-clm-knowledge-recording) and [EPI-CLM-attester-demo](#epi-clm-attester-demo). A name such as “Attested Computation” is not itself evidence of an attestation event.

| Operation | Source path | Coverage and records | Limit |
|---|---|---|---|
| list/search/get | `packages/core/lib/bundle.mjs`, `packages/core/lib/search.mjs`; CLI and MCP get handlers | Direct full core reads and selected handler reads; [RT-RTE-bundle-read](runtime.md#rt-rte-bundle-read), [EPI-OBJ-concept](#epi-obj-concept) | No real retrieval workload; adapter response need not expose source/trust metadata. |
| create/update | `packages/core/lib/write.mjs` | Direct full read; supplied adapter admission findings in [RT-RTE-concept-create](runtime.md#rt-rte-concept-create), [RT-RTE-concept-update](runtime.md#rt-rte-concept-update) | Host proposal/approval events unavailable; no semantic warrant inferred. |
| ingest | `packages/core/lib/ingest.mjs` | Direct full read; [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), [EPI-OBJ-reference](#epi-obj-reference), [EPI-OBJ-derived-reference](#epi-obj-derived-reference) | Copy precedes lookup; a separate excerpt concept is conditional, not a uniform ingest output. |
| validate/lint | `packages/core/lib/validate.mjs`, `packages/core/lib/lint.mjs`, `packages/core/lib/yaml.mjs`, `packages/core/lib/doc.mjs` | Direct full reads; CLI/MCP diagnostic handlers read; [EPI-RTE-format-check](#epi-rte-format-check), [EPI-RTE-health-check](#epi-rte-health-check) | DSH/pi registration searches locate analogous handlers, not independently certified adapter/vendor equivalence. |
| deprecate/index | `packages/core/lib/write.mjs`, `packages/core/lib/indexlog.mjs` | Direct full reads; CLI/MCP retirement handlers; [EPI-RTE-directory-deprecate](#epi-rte-directory-deprecate), [EPI-RTE-index-refresh](#epi-rte-index-refresh) | Not an enforced retrieval ban or evidence-consuming acceptance. |
| hooks/rules/tools | `packages/pi/extensions/index.ts`, `packages/dsh/wiki.mjs`, `packages/mcp/lib/tools.mjs`, `packages/codex/hooks/inject-context.mjs` | Supplied [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery), [RT-BAP-rule-delivery](runtime.md#rt-bap-rule-delivery); direct MCP get/diagnostic handlers and registration searches | Supplied host-channel traces used, not re-established as observed compliance. |
| sync/delete | `packages/core/lib/git.mjs`, `packages/core/lib/feishu.mjs` | Supplied [RT-RTE-remote-sync](runtime.md#rt-rte-remote-sync) | Exhaustive branches and remote execution uninspected; cannot conclude universal safety or semantic reconciliation. |
| legacy migration | `scripts/migrate.mjs` | Direct full read; [EPI-RTE-legacy-migration](#epi-rte-legacy-migration) | Renaming and metadata loss do not validate imported propositions. |
| cloud migration | `scripts/migrate-to-feishu.mjs` | Direct full read; [EPI-RTE-cloud-migration](#epi-rte-cloud-migration) | Markdown-only copy omits non-Markdown computation assets. |
| evaluation | `scripts/smoke-test.mjs` | Direct full read; [EPI-OBJ-smoke-checks](#epi-obj-smoke-checks) | Synthetic assertions, not observed passes or causal evidence. Other tests remain uninspected here. |
| example computation/attester and human views | `examples/demo-bundle/computations/revenue.md`, `examples/demo-bundle/references/attesters/sql-equality.md`, `obsidian/dataview-examples.md` | Direct full reads; [EPI-OBJ-attester](#epi-obj-attester), [EPI-CLM-attester-demo](#epi-clm-attester-demo) | SQL receipt, live executor/attester and external Dataview behavior unavailable. Other examples/templates and Chinese README not independently assessed. |

These remaining available-but-uninspected paths prevent a system-complete negative about every possible evaluator or knowledge-producing practice. Missing host traces prevent attribution of synthesis, acceptance, critique, model adherence or benefit. Missing original-source warrant prevents treating imported propositions as warranted. Missing upstream specification prevents independently establishing OKF conformance beyond the local implementation's predicate. No supplied runtime fact requires supersession: its broad read/write containers remain useful, while this report adds diagnostics and maintenance routes.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-concept](#epi-obj-concept) | Domain propositions, definitions, pitfalls and computation descriptions | see record | SRC-1 `packages/core/lib/write.mjs` | Authorship and retention do not establish truth; individual production relation depends on proposed body. |
| [EPI-OBJ-reference](#epi-obj-reference) | Imported source payload, truth aptitude depends on content | see record | SRC-1 `packages/core/lib/ingest.mjs` | Raw copy preserves bytes when new; existing destination is not refreshed. |
| [EPI-OBJ-derived-reference](#epi-obj-derived-reference) | Registration assertion and shortened first-line excerpt | see record | SRC-1 `packages/core/lib/ingest.mjs` | Generated only when stem-based readConcept returns null; excerpt can lose qualifications. |
| [EPI-OBJ-trust-fields](#epi-obj-trust-fields) | Assertions of generation, verification, source lineage and lifecycle state | see record | SRC-1 `packages/core/lib/write.mjs` | Labels can outlive content revision; no authenticated approval witness. |
| [EPI-OBJ-health-results](#epi-obj-health-results) | Claims about parsed structure, graph connectivity and timestamps | see record | SRC-1 `packages/core/lib/lint.mjs` | Not claims that domain content is correct. |
| [EPI-OBJ-index-log](#epi-obj-index-log) | Concept membership/descriptions and action history | see record | SRC-1 `packages/core/lib/indexlog.mjs` | Derived navigation, not evidence acceptance. |
| [RT-OBJ-agents](runtime.md#rt-obj-agents) | Policy; gate type list has no domain-truth judgment | see record | SRC-1 `packages/core/lib/rules.mjs` | Gate allows behavior, not knowledge warrant. |
| [RT-OBJ-append-system-prompt](runtime.md#rt-obj-append-system-prompt) | Instructions, possibly including domain claims | see record | SRC-1 `packages/core/lib/bundle.mjs` | Meaning and compliance host-dependent. |
| [EPI-OBJ-attester](#epi-obj-attester) | Proposed equality relation between executed and sanctioned SQL | see record | SRC-1 `examples/demo-bundle/references/attesters/sql-equality.md` | Placeholder prose; receipt/verdict not supplied. |
| [EPI-OBJ-smoke-checks](#epi-obj-smoke-checks) | Expected properties of synthetic bundle operations | see record | SRC-1 `scripts/smoke-test.mjs` | Test text supplies expectations, not outcomes. |

## Authority-route ledger

Fields owned by cited shared records are referenced with “see”; this ledger supplies architectural status and edge-specific epistemic interpretation. Repeated citations identify different functions of the same route, not new record identities.

| route ID | route function | architectural status | object/candidate ID | content/update relation | transition or check target | evaluator/condition and domain | activation and timing | possible or observed result | implemented force | epistemic authority and scope | operational authority: behavior permitted, blocked, or changed | behavioral-authority path: consumer, channel, force, horizon | evidence source ID and local anchor | claim IDs or none | mismatch marker or none | gap/limit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) | content transformation | implemented | [EPI-OBJ-reference](#epi-obj-reference) | truth-apt transformation: acquisition/import | External file → raw reference copy | Copy if destination absent; no truth evaluator | Explicit request; before concept lookup | Possible retained copy; existing destination unchanged | Filesystem retention | Source warrant unknown; new raw bytes preserved | Makes imported payload available | Later caller, resource read or Markdown graph read, permissive, later invocations | SRC-1 `packages/core/lib/ingest.mjs` | [EPI-CLM-knowledge-recording](#epi-clm-knowledge-recording) | Copy ≠ semantic synthesis | Copied Markdown can itself satisfy subsequent concept lookup |
| [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) | content transformation | implemented | [EPI-OBJ-derived-reference](#epi-obj-derived-reference) | truth-apt transformation: indeterminate | External source first eligible line → excerpt in Reference concept | readConcept must return null; first-line selection and 200-character cap, not truth evaluation | After raw-copy stage, only on missing concept | Possible separate Reference with resource/path/time and excerpt | Conditional core create and retention | Excerpt may degrade source scope; registration metadata does not warrant domain truth | Makes excerpt and resource pointer available | Later graph/get consumer, concept Markdown, permissive, later calls | SRC-1 `packages/core/lib/ingest.mjs` | [EPI-CLM-knowledge-recording](#epi-clm-knowledge-recording) | No generated Reference on existing-concept branch | Existing destination and current external excerpt can differ; source/proposition comparison is needed to distinguish scope-preserving reshaping from a changed, possibly non-entailed claim |
| [RT-RTE-concept-create](runtime.md#rt-rte-concept-create) | disposition/acceptance | implemented | [EPI-OBJ-concept](#epi-obj-concept) | no content change | Proposed write admission | See record: type gate, caller flag, ID/type/existence; not truth criterion | Before adapter/core write | Possible refusal or admission | Enforcing on covered create path | No recorded evidence-consuming acceptance of domain truth | See record | See record | SRC-1 `packages/core/lib/write.mjs` | [EPI-CLM-knowledge-recording](#epi-clm-knowledge-recording) | Confirmation is caller assertion | Update/core/ingest alternatives remain |
| [RT-RTE-concept-create](runtime.md#rt-rte-concept-create); [RT-RTE-concept-update](runtime.md#rt-rte-concept-update) | retention | implemented | [EPI-OBJ-concept](#epi-obj-concept); [EPI-OBJ-trust-fields](#epi-obj-trust-fields) | truth-apt transformation: indeterminate | Caller body/metadata → Markdown | Caller supplies semantics; serializer persists | After admission; see records | Possible durable candidate and labels | Filesystem write | Retention only; no general entailment or non-entailment proof for arbitrary body | New text eligible for later reads | Graph/get consumer, files, permissive, later calls | SRC-1 `packages/core/lib/write.mjs` | [EPI-CLM-knowledge-recording](#epi-clm-knowledge-recording) | Verified label need not cover current body | Generated labels do not prove a model produced the body |
| [RT-RTE-bundle-read](runtime.md#rt-rte-bundle-read) | operational admission/selection/consumption | implemented | [EPI-OBJ-concept](#epi-obj-concept) | truth-apt transformation: non-ampliative reshaping | Stored concepts → selected response | Lexical score/ID/title/prefix; see record | Caller read request | Possible summaries/body/backlinks | Ranking and delivery | Relevant matches, not endorsed facts; backlinks mean textual relationship | Supplies answer context, not a warranted answer | See record; MCP formatted text may truncate | SRC-1 `packages/core/lib/search.mjs` | [RT-CLM-form-equivalence](runtime.md#rt-clm-form-equivalence) | Retrieval ≠ acceptance | MCP/CLI get omit structured sources/verified metadata |
| [EPI-RTE-format-check](#epi-rte-format-check) | check/evidence production | implemented | [EPI-OBJ-health-results](#epi-obj-health-results) | truth-apt transformation: entailed derivation | Parsed bundle structure | Local parser and explicit checks, not complete YAML or domain truth | Explicit diagnostic request | Possible ok/errors/warnings | Diagnostic output | Only inspected predicate over parsed inputs | No mandatory admission block | Caller, returned result, advisory; CLI nonzero on errors, current invocation | SRC-1 `packages/core/lib/validate.mjs` | [EPI-CLM-format-check](#epi-clm-format-check) | Compliance label exceeds demonstrated external conformance | No upstream comparison or executed result |
| [EPI-RTE-health-check](#epi-rte-health-check) | check/evidence production | implemented | [EPI-OBJ-health-results](#epi-obj-health-results) | truth-apt transformation: entailed derivation | Links, timestamps, title/description/index structure | Graph membership/date comparisons | Explicit request; current time or opts.now | Possible issue list/counts | Advisory diagnostics | Facts about graph/time, not semantic contradiction or source truth | May guide human/model repair; no automatic rewrite | Caller, text/results, advisory, current and discretionary later use | SRC-1 `packages/core/lib/lint.mjs` | [EPI-CLM-knowledge-recording](#epi-clm-knowledge-recording) | Stale ≠ false | MCP output cap may omit issues |
| [EPI-RTE-directory-deprecate](#epi-rte-directory-deprecate) | disposition/acceptance | implemented | [EPI-OBJ-concept](#epi-obj-concept); [EPI-OBJ-trust-fields](#epi-obj-trust-fields) | non-truth-apt policy/content update: mark deprecated | Selected subtree → lifecycle label | Caller chooses subtree; no truth evaluation | Explicit request | Possible status change/counts | Retained label, not exclusion invariant | Withdrawal recommendation, not falsification | Changes status shown in results; search/get still possible | Later host, metadata/display, advisory, until changed | SRC-1 `packages/core/lib/write.mjs` | [EPI-CLM-knowledge-recording](#epi-clm-knowledge-recording) | Retirement does not forbid use | No content-specific veto in core; body retained |
| [EPI-RTE-index-refresh](#epi-rte-index-refresh) | content transformation | implemented | [EPI-OBJ-index-log](#epi-obj-index-log) | truth-apt transformation: non-ampliative reshaping | Graph → index Markdown | Deterministic grouping/sorting/descriptions | After writes or explicit refresh | Possible regenerated navigation | Filesystem overwrite | No new warrant for described claims | Changes later navigation, not accepted-claim integration | Caller/host, index files, advisory, later reads | SRC-1 `packages/core/lib/indexlog.mjs` | none | Not lifecycle integration | Metadata descriptions may already be wrong |
| [EPI-RTE-legacy-migration](#epi-rte-legacy-migration) | content transformation | implemented | [EPI-OBJ-concept](#epi-obj-concept); [EPI-OBJ-trust-fields](#epi-obj-trust-fields) | truth-apt transformation: acquisition/import | Legacy files → bundle concepts | Path/regex-derived types; target-exists skip | --real; default dry run | Possible imported body/new metadata | Direct filesystem admission | Imported source warrant unknown; selected metadata discarded | Eligible for later bundle reads without adapter confirmation | Caller/host, files, permissive, subsequent sessions | SRC-1 `scripts/migrate.mjs` | none | Type name not attestation | Legacy approval/source fields not carried generally |
| [EPI-RTE-cloud-migration](#epi-rte-cloud-migration) | lineage/freshness/recovery | implemented | [EPI-OBJ-reference](#epi-obj-reference); [EPI-OBJ-concept](#epi-obj-concept) | truth-apt transformation: acquisition/import | Local Markdown → cache/remote | Extension filter, apply flag, service results | Explicit --apply | Possible copy, push/status or failure | Writes and remote publication | No semantic endorsement; non-Markdown evidence/computations omitted | Changes later accessible bundle content | See record | SRC-1 `scripts/migrate-to-feishu.mjs` | none | Partial asset transfer | No successful service result supplied |
| [RT-RTE-remote-sync](runtime.md#rt-rte-remote-sync) | lineage/freshness/recovery | implemented | [EPI-OBJ-concept](#epi-obj-concept); [EPI-OBJ-index-log](#epi-obj-index-log) | truth-apt transformation: acquisition/import | Local/remote state reconciliation and explicit delete | See record | Explicit or timer; see record | Possible import/conflict/delete | See record | History/ledger comparisons do not resolve semantic disagreement | See record | See record | SRC-1 `packages/core/lib/feishu.mjs` | none | Freshness ≠ endorsement | Supplied bounded account, exhaustive branches uninspected |
| [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery) | operational admission/selection/consumption | implemented | [RT-OBJ-append-system-prompt](runtime.md#rt-obj-append-system-prompt); [RT-OBJ-agents](runtime.md#rt-obj-agents) | no content change | Retained guidance → host instructions | See record | See record | Possible delivered or omitted/truncated text | Advisory text; symbolic create gate separate | Delivery confers no factual warrant | Requested query-first, recording and rule-following behavior | See [RT-BAP-rule-delivery](runtime.md#rt-bap-rule-delivery) | SRC-1 `packages/pi/extensions/index.ts` | [RT-CLM-form-equivalence](runtime.md#rt-clm-form-equivalence) | Delivery ≠ compliance | Host precedence/model behavior uninspected |
| [EPI-RTE-attester-check](#epi-rte-attester-check) | check/evidence production | doctrine only | [EPI-OBJ-attester](#epi-obj-attester) | no content change | Receipt executed_sql vs bound sanctioned SQL | Declared deterministic equality attester; SQL string equality domain | No implemented invocation established in inspected core/handlers | Declared verdict, no observed receipt/result | No implemented consumer established | Even realized equality would not establish business definition or data truth | No automatic execution/acceptance licensed by metadata alone | Declared external consumer; channel/verdict consequence not established | SRC-1 `examples/demo-bundle/references/attesters/sql-equality.md` | [EPI-CLM-attester-demo](#epi-clm-attester-demo) | Placeholder not running evaluator | Not a system-complete absence of host evaluators |

No accepted ampliative-claim lifecycle integration is established by these routes. This is not a claim that hosts cannot generate or accept knowledge. For arbitrary caller bodies, semantic preservation, entailment and non-entailment are not determinable without the source/proposal/decision trace. The source-copy edge is acquisition; diagnostic deductions are limited to implementation predicates. Neither is evidence of an internally produced accepted ampliative theory.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-form-equivalence](runtime.md#rt-clm-form-equivalence) | see record | SRC-1 `README.md`, doctrine/design | see record | [RT-RTE-bundle-read](runtime.md#rt-rte-bundle-read), [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery) | None supplied | No intervention/comparison | Shared core plus differing adapter channels | Full equivalence unsupported. |
| [EPI-CLM-format-check](#epi-clm-format-check) | see record | SRC-1 `packages/skill/bin/wiki.mjs`, doctrine/design and implementation label | Local schema specifies structural checks | [EPI-RTE-format-check](#epi-rte-format-check) | None supplied | No external specification comparison | Implements a bounded local structural predicate | “Compliant” not a domain-truth verdict or full YAML validator. |
| [EPI-CLM-knowledge-recording](#epi-clm-knowledge-recording) | see record | SRC-1 `packages/skill/SKILL.md`, doctrine/design | Requests investigation, user confirmation, unverified-use marking and maintenance | [RT-RTE-concept-create](runtime.md#rt-rte-concept-create), [RT-RTE-concept-update](runtime.md#rt-rte-concept-update), [EPI-RTE-health-check](#epi-rte-health-check), [EPI-RTE-directory-deprecate](#epi-rte-directory-deprecate) | None supplied | Host cooperation required; no factual accuracy or capacity experiment | Wired storage/retrieval plus declarative epistemic discipline | No evidence-consuming acceptance record; get does not expose all trust/source fields. |
| [EPI-CLM-attester-demo](#epi-clm-attester-demo) | see record | SRC-1 `examples/demo-bundle/references/attesters/sql-equality.md`, doctrine/design | Equality-check description | No execution route established in inspected core/handlers | Synthetic candidate only | Equality cannot validate sanctioned premises or component benefit | Declared external attestation pattern | No receipt, verdict or consequential decision. |

## Bounded conclusion

llm-wiki provides persistence and later lexical retrieval of caller-supplied knowledge, not an inspected internal semantic knowledge-production loop. Raw ingestion copies an external file only when the destination is absent, then conditionally adds a small Reference if stem-based readConcept finds nothing; source warrant is unknown. A copied Markdown file can itself satisfy that lookup without frontmatter, skipping separate Reference generation. A new raw copy preserves bytes; the optional derived excerpt and adapter presentations can lose context. Core objects retain source/trust metadata, but MCP and CLI get primarily expose title/type/status, description, body and backlinks. A source footnote in the body can survive without its structured source mapping reaching that consumer ([EPI-OBJ-reference](#epi-obj-reference), [EPI-OBJ-derived-reference](#epi-obj-derived-reference), [EPI-OBJ-concept](#epi-obj-concept), [RT-RTE-bundle-read](runtime.md#rt-rte-bundle-read)).

Its implemented evaluators assess named structural targets. Validation's local predicate, lint's graph/date deductions and identifier ambiguity rejection have bounded warrant; none judges domain propositions. CLI validation can fail the current command, but is not wired as mandatory approval before writes. Lint is advisory and MCP truncation can omit its tail. Confirmation checks grant operational admission on covered creates. A flag and retained human label are not a recorded evidence-consuming acceptance decision with criterion, intended use and scope ([EPI-RTE-format-check](#epi-rte-format-check), [EPI-RTE-health-check](#epi-rte-health-check), [RT-RTE-concept-create](runtime.md#rt-rte-concept-create)).

Retirement is a recommendation expressed in retained status. It does not erase bodies or exclude deprecated concepts from unfiltered search/get. Generated metadata refreshes on updates, while earlier verified entries can remain. Navigation refresh and synchronization alter accessibility and organization without establishing post-acceptance integration. The alternative migrations bypass interactive create admission; cloud migration copies only Markdown, so computation/evidence links can outlive omitted assets ([EPI-RTE-directory-deprecate](#epi-rte-directory-deprecate), [EPI-OBJ-trust-fields](#epi-obj-trust-fields), [EPI-RTE-index-refresh](#epi-rte-index-refresh), [EPI-RTE-legacy-migration](#epi-rte-legacy-migration), [EPI-RTE-cloud-migration](#epi-rte-cloud-migration), [RT-RTE-remote-sync](runtime.md#rt-rte-remote-sync)).

Retained rules have a live target-side channel into later host context, plus executable type-gate consequences. Their interpretation is external. No direct model-parameter update is established; external model versions, endpoint mutation and weights remain uninspected, not fixed by this target. Retention and changed prompts can support later behavior without demonstrating learning, reflection, autonomous theory-building or exercised self-improvement. These are independent unresolved properties, not a bundled negative. The SQL attester placeholder and synthetic smoke expectations cannot fill the missing receipt, acceptance, operation or causal evidence ([RT-BAP-rule-delivery](runtime.md#rt-bap-rule-delivery), [EPI-OBJ-attester](#epi-obj-attester), [EPI-OBJ-smoke-checks](#epi-obj-smoke-checks)).

## Shared records

### Components

none declared in this member

### Operative objects

#### EPI-OBJ-concept
Label: Concept Markdown

Source-native identity: nonreserved concept files, natural-language domain text plus symbolic frontmatter/link fields; substrate: bundle Markdown and reconstructed JavaScript graph. Distinct from supplied rule objects; overlaps [RT-RTE-bundle-read](runtime.md#rt-rte-bundle-read) as its input, not a duplicate route. SRC-1 `packages/core/lib/bundle.mjs`, `packages/core/lib/write.mjs`. Caller supplies the body; type names do not prove its origin or correctness.

> return { id, path: relPath, meta, body, title, type, desc, hasFM }
> --- `packages/core/lib/bundle.mjs`

The core retains metadata, but the inspected CLI/MCP get presentations do not serialize sources/verified/generated/stale_after/executor/attester/computation fields. This limits lineage and attestation information reaching the model through that response; direct file reading is a separate possible host operation. MCP additionally caps the assembled response. SRC-1 `packages/mcp/lib/tools.mjs`, `packages/skill/bin/wiki.mjs`:

> got.body.trim(),
>         ]
>         return { text: lines.join('\n').slice(0, limits.maxGetChars) }
> --- `packages/mcp/lib/tools.mjs`

#### EPI-OBJ-reference
Label: Registered raw source

Source-native identity: copied references/refDir asset, not the separately generated Reference concept. Representational form: original payload, possibly binary/opaque; substrate: filesystem. This corrects the former combined raw/excerpt finding while preserving its ID and supported copying finding. Same raw referent as supplied [MEM-OBJ-reference-source](memory.md#mem-obj-reference-source), not a different object because of prefix; [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) supplies the copy passage. SRC-1 `packages/core/lib/ingest.mjs`, `packages/core/lib/bundle.mjs`.

Copy precedes stem-based lookup. A readable copied `memo.md` makes readConcept return an object even without frontmatter, so no separate Reference is generated. A non-Markdown payload needs a separate resource read; a nonreserved Markdown payload can itself enter the graph. Existing destination bytes are not recopied. These paths preserve neither an independent source-warrant judgment nor a uniform raw/derived artifact pair.

> const existing = await readConcept(root, conceptId)
> let sourceConceptId = existing ? conceptId : null
> if (!existing) {
> --- `packages/core/lib/ingest.mjs`

> return { id, path: relPath, meta, body, title, type, desc, hasFM }
> --- `packages/core/lib/bundle.mjs`

#### EPI-OBJ-derived-reference
Label: Generated Reference concept

Source-native identity: the conditional stem-named Reference page with registration statement, resource pointer and first-line excerpt. Form: natural-language body plus symbolic resource/type/generated fields; substrate: concept Markdown. It is distinct from the raw asset in [EPI-OBJ-reference](#epi-obj-reference) and supplied [MEM-OBJ-reference-source](memory.md#mem-obj-reference-source): it is generated only after a null lookup, takes its excerpt from the external source rather than necessarily the retained destination, and reaches graph/get consumers instead of requiring a raw-resource read. It is a material subtype of the ordinary concept container, not another ingestion route.
Part of: [EPI-OBJ-concept](#epi-obj-concept)

SRC-1 `packages/core/lib/ingest.mjs`: raw copy → lookup → optional core create. No truth check or evidence-consuming acceptance intervenes. Existing concepts, including copied Markdown without frontmatter, bypass generation. For a new `memo.txt` containing “Revenue is gross.\nException: refunds excluded.” with no existing stem concept, copying preserves both lines but the derived page includes only the first eligible line, capped at 200 characters. This is an implementation deduction, not execution. The excerpt cannot replace the source's full scope; if the raw destination already exists, the current external excerpt need not match it.

> const firstLine = srcText.split('\n').find((l) => l.trim() && !l.startsWith('---')) || ''
> --- `packages/core/lib/ingest.mjs`

> resource: `/${rel}`,
> body: `> Ingested from \`${p.source}\` at ${nowIso()}\n\n${firstLine.slice(0, 200)}`,
> --- `packages/core/lib/ingest.mjs`

#### EPI-OBJ-trust-fields
Label: Trust and lifecycle fields

Source-native identity: generated/verified/sources/status/stale_after metadata on concept files. Symbolic keys and natural-language actor/source values, filesystem substrate. Distinct material part of [EPI-OBJ-concept](#epi-obj-concept); supplied [RT-RTE-concept-create](runtime.md#rt-rte-concept-create) and [RT-RTE-concept-update](runtime.md#rt-rte-concept-update) establish consumers, not a counterpart object.
Part of: [EPI-OBJ-concept](#epi-obj-concept)

SRC-1 `packages/core/lib/write.mjs`: confirmation adds a human-prefixed claim without authentication; update copies old metadata and only modifies verified inside the confirmed branch. Thus changing body without confirmation can leave historical verified metadata. The supplied update record supports the old-meta copy and body overwrite.

> if (p.opts?.confirmed) {
>     const user = p.opts.user || 'human:unknown'
>     meta.verified = [{ by: user.startsWith('human:') ? user : `human:${user}`, at: nowIso() }]
>   }
> --- `packages/core/lib/write.mjs`

#### EPI-OBJ-health-results
Label: Validation and lint results

Source-native identity: ok/errors/warnings and issues/summary objects, symbolic diagnostic structures rendered as text; substrate: current invocation memory/stdout/tool results. Different referent from domain concepts and supplied runtime records. SRC-1 `packages/core/lib/validate.mjs`, `packages/core/lib/lint.mjs`; passages in the corresponding routes.

#### EPI-OBJ-index-log
Label: index.md and log.md

Source-native identity: reserved index/log files; natural-language descriptions/action text plus symbolic links/date headers; filesystem substrate. Distinct from supplied AGENTS/APPEND objects and a generated output of supplied write/sync routes, not a duplicate route. SRC-1 `packages/core/lib/indexlog.mjs`. Index refresh reads the graph; logs record action labels, not evidence-consuming truth judgments.

> const line = `* **${action}**: ${entry}`
> --- `packages/core/lib/indexlog.mjs`

#### EPI-OBJ-attester
Label: SQL equality attester demo

Source-native identity: `references/attesters/sql-equality.md` linked by the demo revenue computation. Natural-language instructions on filesystem, not executable attester code. Compared with [RT-RTE-bundle-read](runtime.md#rt-rte-bundle-read): this is a retained candidate/check specification that retrieval can expose, not another retrieval route. SRC-1 `examples/demo-bundle/references/attesters/sql-equality.md`, `examples/demo-bundle/computations/revenue.md`.

> attester: { resource: references/attesters/sql-equality.md }
> --- `examples/demo-bundle/computations/revenue.md`

#### EPI-OBJ-smoke-checks
Label: Smoke test assertions

Source-native identity: script check predicates over synthetic bundles, symbolic JavaScript on filesystem; counters/errors in current-run memory if executed. No counterpart among supplied runtime objects. SRC-1 `scripts/smoke-test.mjs`. Expected outcomes are authored by test code, not an ordinary domain-answer oracle. Failure drives script exit 1 and temporary files are removed after the checks; no automatic product revision or knowledge acceptance follows.

> check('英文检索命中口径', s2.some((r) => r.id === 'computations/revenue'))
> --- `scripts/smoke-test.mjs`

### Routes

#### EPI-RTE-format-check
Label: Bundle format validation

Endpoints: resolved bundle → scan/read/parse → errors/warnings/ok → CLI or tool caller. Owner: deterministic core, invoked explicitly by caller; no proposal selection or content approval. Target/domain: frontmatter presence and nonempty parsed type plus limited reserved-file structure. The parser tolerates lines it cannot map and implements a YAML subset; this is not proof of full YAML validity. Separate from supplied [RT-RTE-concept-create](runtime.md#rt-rte-concept-create): a diagnostic request, not a write admission mechanism. SRC-1 `packages/core/lib/validate.mjs`, `packages/core/lib/yaml.mjs`, `packages/skill/bin/wiki.mjs`, `packages/mcp/lib/tools.mjs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: ok/errors/warnings; CLI exits 1 on errors, otherwise prints a compliance label; MCP returns text.
- Later read-back: inapplicable — diagnostics do not accumulate changed retained material in this route.
- Delegated visibility: inapplicable — no target-side model worker is created by this route.
- Selection predicate: all scanned nonhidden/nonreserved Markdown concepts plus traversed reserved-file checks.
- Invalidation or expiry: recomputed on each explicit call; no durable approval state.
- Activation or effect: current caller receives diagnostics; no mandatory prewrite invocation or automatic semantic repair.
- Evidence limits: no executed result; no independent OKF specification comparison; validation does not check truth, attestation receipts or source accuracy.

> return { ok: errors.length === 0, errors, warnings }
> --- `packages/core/lib/validate.mjs`

> if (!kv) { i++; continue }
> --- `packages/core/lib/yaml.mjs`

> if (!v.ok) { for (const e of v.errors) console.error('ERROR ' + e); process.exit(1) }
> --- `packages/skill/bin/wiki.mjs`

#### EPI-RTE-health-check
Label: Bundle health lint

Endpoints: bundle graph/time → structural comparisons → issue array/counts → CLI/MCP/host. Owner: core program; caller elects maintenance. Target/domain: links absent from node set, no incoming/outgoing edges, parsed stale timestamps, deprecated flag, absent description, repeated titles and missing subdirectory indexes. Not semantic contradiction detection. No expected domain-answer oracle; author/program predicates serve only structural diagnosis. Distinct from [RT-RTE-bundle-read](runtime.md#rt-rte-bundle-read): produces diagnostic propositions, not search ranking. SRC-1 `packages/core/lib/lint.mjs`, `packages/mcp/lib/tools.mjs`, `packages/skill/bin/wiki.mjs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: sorted issues and counts; MCP renders text truncated at maxGetChars, CLI prints issues/summary.
- Later read-back: inapplicable — this route writes no durable issue ledger or changed concepts.
- Delegated visibility: inapplicable — no target-side model worker is created by this route.
- Selection predicate: current graph and concept directories; opts.now or current Date determines stale comparison.
- Invalidation or expiry: recomputed when invoked; time passage may change stale results.
- Activation or effect: advisory facts exposed to caller; no automatic rejection or revision of content.
- Evidence limits: graph/parser fidelity and timestamps bound conclusions; no model-driven contradiction evaluator inside this module; external repair is unobserved.

> 「矛盾检测」为 LLM 辅助（消费方外部做），本模块输出结构事实。
> --- `packages/core/lib/lint.mjs`

> if (!Number.isNaN(t) && t <= now.getTime()) {
> --- `packages/core/lib/lint.mjs`

> return { text: lines.join('\n').slice(0, limits.maxGetChars) }
> --- `packages/mcp/lib/tools.mjs:408-412`

#### EPI-RTE-directory-deprecate
Label: Directory deprecation

Endpoints: caller-selected subtree → graph nodes → status writes → log/index → count. Owner: caller chooses policy withdrawal; core executes. Distinct from [RT-RTE-concept-update](runtime.md#rt-rte-concept-update): batch status-only path with no content-specific confirmation option. Admission: CLI/MCP online guard may block remote conflicts, otherwise core selects subtree without directory human-confirmation gate. Proposer/decider is caller; no independent truth evaluator or answer oracle; human veto is only through caller choice. Mode: open maintenance request. Rollback: later status update/file restoration; not transactional across subtree writes. Guidance: deprecated means not recommended, retained for history. SRC-1 `packages/core/lib/write.mjs`, `packages/skill/bin/wiki.mjs`, `packages/mcp/lib/tools.mjs`, `schema.md`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: deprecated/total counts and adapter flush status.
- Later read-back: status and generated metadata remain for later graph/list/get/lint consumption; body remains unchanged.
- Delegated visibility: inapplicable — no target-side model worker is created by this route.
- Selection predicate: all graph IDs with selected directory prefix, or all IDs for empty dir; skip missing frontmatter and already deprecated.
- Invalidation or expiry: no automatic expiry/undo; subsequent update can replace status.
- Activation or effect: writes status and new generation timestamp; does not force search/get exclusion.
- Evidence limits: retirement recommendation is not evidence that any proposition was falsified; later host obedience unobserved.

> meta.status = 'deprecated'
>     const producer = 'llm-wiki'
>     meta.generated = { by: `agent:${producer}/0.1.0`, at: nowIso() }
>     await writeFile(file, serializeDoc({ meta, body }))
> --- `packages/core/lib/write.mjs`

#### EPI-RTE-index-refresh
Label: Index regeneration

Endpoints: graph → deterministic directory grouping/title sorting/description projection → index files. Standalone refresh does not append an action log; mutation callers separately log their actions before index maintenance. Owner: core after mutation or caller-triggered refresh. Distinct from supplied [RT-RTE-concept-create](runtime.md#rt-rte-concept-create) and [RT-RTE-remote-sync](runtime.md#rt-rte-remote-sync): derived-navigation operation called by both, not another concept admission. No semantic evaluator or acceptance transition. SRC-1 `packages/core/lib/indexlog.mjs`. Concrete deduction: a graph containing only `tables/orders` yields root directory entry `* [tables](tables/index.md) — 1 个概念`; descriptions are copied into direct-concept entries, not independently checked.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: refreshIndex returns written file list; writeDirIndex returns after write.
- Later read-back: regenerated reserved index files can guide a later host read; standalone refresh creates no durable action-log entry.
- Delegated visibility: inapplicable — no target-side model worker is created by this route.
- Selection predicate: graph membership and directory path; refresh includes concept-containing directories and existing indexes.
- Invalidation or expiry: later writes/refresh replace derived indexes; logs append action text.
- Activation or effect: rewrites navigation, not accepted-claim lifecycle integration.
- Evidence limits: body meaning and description truth not validated; downstream navigation use unobserved.

> lines.push(`* [${k}](${k}/index.md) — ${groups.get(k)} 个概念`)
> --- `packages/core/lib/indexlog.mjs`

> const bodyText = renderIndexBody(graph, dir)
> --- `packages/core/lib/indexlog.mjs`

> await updateIndex(root, { dirs: [...dirs] })
> return { files: ['index.md', ...[...dirs].sort().map((d) => `${d}/index.md`)] }
> --- `packages/core/lib/indexlog.mjs`

#### EPI-RTE-legacy-migration
Label: Legacy bundle migration

Endpoints: legacy trees → flat legacy-frontmatter parser → mapped type/title/description/tags, annotated body/linkification → target files. Owner: script rules; caller selects roots and --real. Distinct from [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest): bulk legacy mapping, no core create call or directory gate. Mode: open migration, default dry-run; caller authorizes bulk copying, not demonstrated per-content approval. No truth or expected-answer oracle. Existing destinations skipped as conflicts; real writes directly to disk. Recovery: source unchanged, no automatic undo of already written targets. Metadata such as prior verified/sources/enabled is not generally carried by the selected outMeta constructors. SRC-1 `scripts/migrate.mjs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: planned/created file list, conflicts and errors to console.
- Later read-back: new Markdown concepts become inputs to subsequent graph/get; generated marks process:migrate.
- Delegated visibility: inapplicable — no target-side model worker is created by this route.
- Selection predicate: nonhidden .md except README in legacy KB; selected tables/examples/pitfalls directories; SQL regex selects Attested Computation type.
- Invalidation or expiry: existing targets skipped; no freshness or trust invalidation beyond newly mapped metadata.
- Activation or effect: imports candidate knowledge and guessed types without attestation or adapter approval.
- Evidence limits: retained body can preserve claims but transformed metadata loses lineage/approval detail; no successful migration supplied.

> const hasSql = /```sql|select\s/i.test(body)
>       const outMeta = {
>         type: hasSql ? 'Attested Computation' : 'Reference',
> --- `scripts/migrate.mjs`

> if (!o.dryRun) {
>       await mkdir(dirname(dest), { recursive: true })
>       await writeFile(dest, content)
>     }
> --- `scripts/migrate.mjs`

#### EPI-RTE-cloud-migration
Label: Cloud bundle migration

Endpoints: local tree → .md selection → Feishu initialization/registration → cache copy → optional index refresh → sync adopt local → status. Owner: caller plus script and backend. Distinct entry from [RT-RTE-remote-sync](runtime.md#rt-rte-remote-sync): it first determines which assets enter the new bundle; backend sync is supplied by that record. Caller --apply admits copying, target/CLI errors can terminate; no human per-proposition approval or answer oracle. Recovery: source untouched; partial cloud/cache mutations can precede failure, no transaction established. SRC-1 `scripts/migrate-to-feishu.mjs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: plan on dry-run, otherwise initialization/copy/push/status messages or early failure.
- Later read-back: copied/remote Markdown is accessible to later consumers; non-.md assets are not copied by this selector.
- Delegated visibility: inapplicable — no target-side model worker is created by this route.
- Selection predicate: nonhidden, non-node_modules paths ending .md; explicit --apply; optional --skip-index.
- Invalidation or expiry: backend status/push results determine continuation; not semantic endorsement or source-freshness certification.
- Activation or effect: retained metadata pointers may refer to omitted .sql files, as in the shipped revenue example.
- Evidence limits: remote service execution unavailable; state-count review is not receipt validation or successful computation.

> else if (e.name.endsWith('.md')) out.push(child)
> --- `scripts/migrate-to-feishu.mjs`

> const sync = await core.feishuSync(spec, { adopt: 'local' })
> --- `scripts/migrate-to-feishu.mjs`

#### EPI-RTE-attester-check
Label: Declared SQL equality check

Endpoints declared: receipt plus parameter-bound sanctioned computation → deterministic comparison → verdict. Owner: external consumer unspecified. Different referent from [RT-RTE-bundle-read](runtime.md#rt-rte-bundle-read): proposed checking procedure, not retrieval. Mode and proposer/decider/veto roles are unspecified. Intended comparison reference is sanctioned SQL, not independent business truth. SRC-1 `examples/demo-bundle/references/attesters/sql-equality.md`; no internal invocation established in inspected core exports, write/validate/lint modules or CLI/MCP handlers. See [EPI-CLM-attester-demo](#epi-clm-attester-demo).

- implementation conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: uninspected — only a declared verdict; no execution trace or implemented invocation supplied.
- Later read-back: uninspected — no receipt/verdict persistence and later consumer established; the specification itself is static shipped material.
- Delegated visibility: inapplicable — no target-side model worker is created by this route.
- Selection predicate: uninspected — no operative attester selection established beyond metadata pointer.
- Invalidation or expiry: uninspected — no verdict expiry or invalidation route supplied.
- Activation or effect: uninspected — declaration alone establishes no consequential result consumer.
- Evidence limits: doctrine only in inspected paths; host-side implementation not frozen; equality would warrant only executed-versus-sanctioned comparison.

> 确定性（无 LLM）校验器：输入 receipt，比对 `executed_sql` 与 sanctioned `computation` 绑定参数后的 SQL 是否一致，返回 verdict。
> --- `examples/demo-bundle/references/attesters/sql-equality.md`

### Claims

#### EPI-CLM-format-check
Label: OKF compliance label

Claimed operation: validate reports local OKF v0.2 compliance. SRC-1 `packages/skill/bin/wiki.mjs`, `schema.md`, doctrine/design and emitted-label implementation. Closest supplied [RT-CLM-form-equivalence](runtime.md#rt-clm-form-equivalence) concerns form parity, not validation criteria; distinct claim. The implementation predicate in [EPI-RTE-format-check](#epi-rte-format-check) has structural scope, not domain truth. Full specification equivalence is unestablished.

> console.log('OKF v0.2 compliant ✓')
> --- `packages/skill/bin/wiki.mjs`

#### EPI-CLM-knowledge-recording
Label: Investigate record and confirm

Claimed operation: host guidance requests investigation before recording new facts, human confirmation for configured types, and consumption of unverified material with an unconfirmed mark. SRC-1 `packages/skill/SKILL.md`, doctrine/design. Different from supplied [RT-CLM-form-equivalence](runtime.md#rt-clm-form-equivalence): this is an epistemic discipline requested of external hosts, not adapter equivalence. Wired persistence/admission supports the means, not observed investigation, fresh approval or truth.

> 探查事实（表结构等）：可直接 `wiki create`（自动写 `generated: {by: agent…}`，无 verified = unverified 态，可消费但标未确认）。
> --- `packages/skill/SKILL.md`

> 规则声明需 human 确认的类型 → 先向用户展示、确认后加 `--confirmed`
> --- `packages/skill/SKILL.md`

#### EPI-CLM-attester-demo
Label: Demo equality attester

Claimed operation: deterministic executed SQL versus sanctioned SQL comparison yields verdict. SRC-1 `examples/demo-bundle/references/attesters/sql-equality.md`, doctrine/design, as quoted in [EPI-RTE-attester-check](#epi-rte-attester-check). Distinct from supplied equivalence claim and ordinary read route. The file explicitly labels itself demo placeholder; the example's verified field is candidate metadata, not a supplied approval/receipt trace.

> # sql-equality attester 说明（demo 占位）
> --- `examples/demo-bundle/references/attesters/sql-equality.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member; supplied [RT-BAP-rule-delivery](runtime.md#rt-bap-rule-delivery) covers retained rules, while each new route states its own bounded consumer/channel/force/horizon.
