---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Sparks epistemic routes: source acquisition, semantic revision doctrine, deterministic collection inferences and the limits of mechanical checks."
run-id: AAS-2026-10-15-sparks-563865f8b26f-01
reviewed-boundary: "49abddc848ea55f78518bfbbbe04c3d37a5f2705"
---

# Sparks epistemic report

## Source-and-claim boundary

This assessment asks what warrants reliance on content entering, changing or leaving Sparks. The [boundary and Source register](boundary.md#source-register) supply SRC-1 and the frozen whole-product scope. External harness scheduling, model inference and the personal vault remain outside the supplied evidence. No target program, test, service or model was executed. Implementation deductions below are not observed runs.

The supplied runtime orders the investigation but does not settle the epistemic interpretation. Direct inspection adds all seven collection extractors, their shared generated header, diagnostic implementations and their CLI consumers, task matching, affected-collection advice, status, archive/clear and finalization. It also checks CLI dispatch, the MCP registry and system-Git invocation against the supplied routes. No additional source identity is introduced.

| Entry point or operation | SRC-1 source path | Coverage and conclusion limit |
|---|---|---|
| CLI dispatch; MCP operations | `cmd/sparks/main.go`; `internal/mcp/serve.go` | Direct dispatch/registry read; handler findings supplied by [RT-RTE-mcp-tools](runtime.md#rt-rte-mcp-tools). The registry exposes status, scan, describe, lint, affected, index, prepare/finalize, done, tasks add, brief and query; no separate semantic approval tool. |
| init; describe; installed instructions | `internal/contract/contract.md`; `internal/core/agent.go` | Direct full contract read; installation supplied by [RT-RTE-contract-install](runtime.md#rt-rte-contract-install). Loading/compliance not observed. |
| prepare; finalize; abort; raw archive/clear | `cmd/sparks/ingest.go`; `internal/core/ingest_finalize.go`; `internal/inbox/archive.go` | Direct reads, prepare-core details supplied by [RT-RTE-ingest-cycle](runtime.md#rt-rte-ingest-cycle). Completion does not certify page coverage or truth. |
| scan; status | `internal/core/scan.go`; `internal/core/status.go` | Scan findings supplied by [RT-RTE-maintenance-write](runtime.md#rt-rte-maintenance-write); status read directly. Counts/metadata, not semantic assessments. |
| lint; fmt | `internal/lint/lint.go`; `internal/frontmatter/frontmatter.go`; `cmd/sparks/lint.go`; `cmd/sparks/fmt.go` | Direct reads; [EPI-RTE-health-check](#epi-rte-health-check). Structural and proxy targets only. |
| collections regen: all registered extractors | `internal/collections/collections.go`; `internal/collections/header.go`; `internal/collections/quotes.go`; `internal/collections/bookmarks.go`; `internal/collections/books.go`; `internal/collections/reading_list.go`; `internal/collections/media.go`; `internal/collections/ideas.go`; `internal/collections/projects.go` | Direct full reads. Seven transformation records below separate their material outputs. Persistence supplied by [RT-RTE-maintenance-write](runtime.md#rt-rte-maintenance-write). |
| index | `internal/core/index.go` | Direct main transformation/description-preservation read; [RT-RTE-maintenance-write](runtime.md#rt-rte-maintenance-write). Old descriptions are retained, not reassessed. |
| tasks add; done | `internal/core/tasks.go` | Direct add/matching/completion read; [RT-RTE-maintenance-write](runtime.md#rt-rte-maintenance-write). Target identification is checked, real-world completion is not. |
| affected | `internal/core/affected.go` | Direct read; [EPI-RTE-affected-select](#epi-rte-affected-select). Advice is not complete dependency proof. |
| query; brief; view | `internal/manifest/queries.go`; `internal/core/brief.go`; `internal/view/server.go` | Brief read directly; query/view supplied by [RT-RTE-vault-consume](runtime.md#rt-rte-vault-consume). Delivery is not successful synthesis. |
| Git hooks and development checks | `internal/git/git.go`; `Makefile`; `.github/workflows/ci.yml` | Git wrapper read directly; build/CI supplied by [RT-RTE-product-build](runtime.md#rt-rte-product-build). User-configured hooks can reject a commit; their content and deployed policies are uninspected. No semantic guarantee is inferred from hook capability. |

Public/design claims assessed are [RT-CLM-work-split](runtime.md#rt-clm-work-split), [RT-CLM-mechanical-integrity](runtime.md#rt-clm-mechanical-integrity), [EPI-CLM-revision-sources](#epi-clm-revision-sources) and [EPI-CLM-stable-maturity](#epi-clm-stable-maturity). The latter two make particular epistemic consequences explicit rather than replace the supplied containers.

Missing personal-vault content prevents identifying actual accepted claims or checking their truth. Missing agent-session traces prevents establishing semantic production, criticism, acceptance, integration or actual downstream reliance. Missing comparisons prevents attributing quality, learning or other improvement to these mechanisms. Opaque provider state prevents assessing parameter updates, exact model fixity or endpoint substitution beyond [RT-CMP-agent](runtime.md#rt-cmp-agent). These are separate limits, not one negative verdict. Available helper/test/view/query details not directly reread here remain supplied-runtime coverage, not access failures or an exhaustive independent semantic audit.

## Epistemic-object inventory

The named object records own their identity, encoding, substrate and evidence; this table adds no competing object fields. Truth-apt scope concerns possible content, not evidence that any actual proposition is true.

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-inbox-raw](#epi-obj-inbox-raw) | Captured propositions and attributed source text | see record | SRC-1, `internal/contract/contract.md` | Actual source warrant unknown; capture is not verification. |
| [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages) | Summaries, cross-source claims, Revision text, maturity/source declarations | see record | SRC-1, `internal/contract/contract.md` | No actual page or acceptance trace supplied. |
| [EPI-OBJ-quotes](#epi-obj-quotes) | Quoted text and attribution | see record | SRC-1, `internal/collections/quotes.go` | Rendered output omits raw path held by parser. |
| [EPI-OBJ-bookmarks](#epi-obj-bookmarks) | URL/description associations | see record | SRC-1, `internal/collections/bookmarks.go` | Same-line extraction need not preserve prose meaning. |
| [EPI-OBJ-books](#epi-obj-books) | Alleged referenced book/source titles and contexts | see record | SRC-1, `internal/collections/books.go` | Attribution punctuation is not evidence of a book title. |
| [EPI-OBJ-reading-list](#epi-obj-reading-list) | Mostly directives; reported queue membership is truth-apt | see record | SRC-1, `internal/collections/reading_list.go` | Historical capture is not current endorsement. |
| [EPI-OBJ-media](#epi-obj-media) | Title/raw-file/first-URL association | see record | SRC-1, `internal/collections/media.go` | First URL need not identify titled work. |
| [EPI-OBJ-ideas](#epi-obj-ideas) | File title/status classification | see record | SRC-1, `internal/collections/ideas.go` | Last matching title/status wins; body omitted. |
| [EPI-OBJ-projects](#epi-obj-projects) | Project ship-status headings | see record | SRC-1, `internal/collections/projects.go` | Maturity does not entail shipping status. |
| [EPI-OBJ-tasks](#epi-obj-tasks) | Directives plus recorded open/done state | see record | SRC-1, `internal/core/tasks.go` | Checked marker does not establish completed work. |
| [RT-OBJ-contract](runtime.md#rt-obj-contract) | Primarily prescriptions; also design claims | see record | SRC-1, `internal/contract/contract.md` | Delivery is not interpretation/compliance. |
| [RT-OBJ-ingests](runtime.md#rt-obj-ingests) | Recorded lifecycle status, not semantic completion | see record | SRC-1, `internal/core/ingest_finalize.go` | Administrative state has no page-level acceptance receipt. |
| [RT-CMP-agent](runtime.md#rt-cmp-agent) | Not determinable in distributed-parametric state | see record | SRC-1, `internal/contract/contract.go` | Provider internals and actual outputs uninspected. |

## Authority-route ledger

Fields owned by the linked declaring records are incorporated as `see`; these rows separate consequential functions, including when the same runtime container implements several. All implementation rows denote inspected wiring, not exercised behavior. There is no observed route in the supplied evidence.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-ingest-cycle](runtime.md#rt-rte-ingest-cycle) | content transformation | implemented | [EPI-OBJ-inbox-raw](#epi-obj-inbox-raw) | truth-apt transformation: acquisition/import | Capture enters prepare result | see route; parser, not source-truth judge | see route | see route | delivery | Imported source warrant unknown | Offers entries for agent work | see route | SRC-1, `internal/core/ingest.go` | [RT-CLM-work-split](runtime.md#rt-clm-work-split) | none | Entry content is not endorsed. |
| [EPI-RTE-semantic-revision](#epi-rte-semantic-revision) | content transformation | doctrine only | [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages) | truth-apt transformation: indeterminate | Captures/existing pages to derived prose | see record | see record | see record | protocol | Candidate summaries/syntheses, not licensed accepted claims | Requests direct edits and later cited synthesis | see record | SRC-1, `internal/contract/contract.md` | [EPI-CLM-revision-sources](#epi-clm-revision-sources) | no enforcement inferred | Actual propositions needed to distinguish reshaping, derivation and conjecture. |
| [EPI-RTE-semantic-revision](#epi-rte-semantic-revision) | check/evidence production | doctrine only | [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages) | no content change | Contradictions and source adequacy | see record | see record | see record | protocol | Neither contradiction resolution nor named acceptance standard established | Requests Revision text and cautious maturity | see record | SRC-1, `internal/contract/contract.md` | [EPI-CLM-revision-sources](#epi-clm-revision-sources) | evidence-consuming acceptance unestablished | Both-source recording preserves disagreement, not adjudication. |
| [RT-RTE-ingest-cycle](runtime.md#rt-rte-ingest-cycle) | retention | implemented | [EPI-OBJ-inbox-raw](#epi-obj-inbox-raw); [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages) | no content change | Archive/clear/complete | see route | see route | see route | file and lifecycle mutation | Retained candidates, not acceptance | Clears inbox and enables later ingest | see route | SRC-1, `internal/core/ingest_finalize.go` | [RT-CLM-mechanical-integrity](runtime.md#rt-clm-mechanical-integrity) | administrative completion only | Agent page writes precede and are not validated by finalize. |
| [EPI-RTE-quotes-extract](#epi-rte-quotes-extract) | content transformation | implemented | [EPI-OBJ-quotes](#epi-obj-quotes) | truth-apt transformation: non-ampliative reshaping | Blockquote text and attribution | see record | see record | see record | renders candidate text | No independent warrant; raw-path lineage degraded | Offers quotations as generated page | see record | SRC-1, `internal/collections/quotes.go` | none | none | Attribution is copied, not authenticated. |
| [EPI-RTE-bookmarks-extract](#epi-rte-bookmarks-extract) | content transformation | implemented | [EPI-OBJ-bookmarks](#epi-obj-bookmarks) | truth-apt transformation: indeterminate | URL plus residual same-line text | see record | see record | see record | renders association | No semantic equivalence licensed | Offers extracted links/descriptions | see record | SRC-1, `internal/collections/bookmarks.go` | none | none | URL trimming and context removal can change reference/meaning. |
| [EPI-RTE-books-extract](#epi-rte-books-extract) | content transformation | implemented | [EPI-OBJ-books](#epi-obj-books) | truth-apt transformation: ampliative conjecture | Attribution to probable source/book | see record | see record | see record | renders conjectural label | Book identity not entailed by punctuation | Offers guessed title as book grouping | see record | SRC-1, `internal/collections/books.go` | none | deterministic does not mean entailed | Explicit book hints are a separate literal-import branch; see record. |
| [EPI-RTE-reading-extract](#epi-rte-reading-extract) | content transformation | implemented | [EPI-OBJ-reading-list](#epi-obj-reading-list) | non-truth-apt policy/content update: extracted reading directives | Archived to-read hints to deduplicated queue | see record | see record | see record | renders queue | No current-interest warrant | Supplies retained reading suggestions | see record | SRC-1, `internal/collections/reading_list.go` | none | none | Count entails only distinct matched strings. |
| [EPI-RTE-media-extract](#epi-rte-media-extract) | content transformation | implemented | [EPI-OBJ-media](#epi-obj-media) | truth-apt transformation: indeterminate | File title to first URL | see record | see record | see record | renders association | No verified work/link identity | Supplies navigation | see record | SRC-1, `internal/collections/media.go` | none | none | Need actual note to assess association. |
| [EPI-RTE-ideas-extract](#epi-rte-ideas-extract) | content transformation | implemented | [EPI-OBJ-ideas](#epi-obj-ideas) | truth-apt transformation: non-ampliative reshaping | Selected title/status lines to groups | see record | see record | see record | renders selected fields | Carries supplied status, not a checked project fact | Supplies portfolio-like grouping | see record | SRC-1, `internal/collections/ideas.go` | none | none | Semantics limited to field extraction, not whole-note summary. |
| [EPI-RTE-projects-extract](#epi-rte-projects-extract) | content transformation | implemented | [EPI-OBJ-projects](#epi-obj-projects) | truth-apt transformation: ampliative conjecture | Maturity to ship status | see record | see record | see record | renders status claim | Reviewed/stable does not warrant shipped | Supplies Shipped/Building/Exploring/Archived headings | see record | SRC-1, `internal/collections/projects.go` | [EPI-CLM-stable-maturity](#epi-clm-stable-maturity) | maturity/status mismatch | Requires extra equivalence premise absent from page contract. |
| [RT-RTE-maintenance-write](runtime.md#rt-rte-maintenance-write) | retention | implemented | Seven collection objects above | no content change | Extractor result to persisted file | see route | see route | see route | enforcing overwrite on non-dry-run | No acceptance criterion consumed | Replaces generated pages without semantic approval | see route | SRC-1, `internal/collections/collections.go` | [EPI-CLM-stable-maturity](#epi-clm-stable-maturity) | auto-stable is not review | Generated header says stable with empty sources. |
| [EPI-RTE-health-check](#epi-rte-health-check) | check/evidence production | implemented | [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages) | no content change | Schema, graph, paths, timestamps, punctuation count | see record | see record | see record | diagnostic; text-mode exit signal | Licenses only named mechanical predicates | Can inform repair; no built-in finalize veto | see record | SRC-1, `internal/lint/lint.go` | [RT-CLM-mechanical-integrity](runtime.md#rt-clm-mechanical-integrity) | health is not truth | No substantive support, contradiction or semantic completeness evaluator. |
| [EPI-RTE-affected-select](#epi-rte-affected-select) | operational admission/selection/consumption | implemented | Collection objects above | no content change | Changed paths to regen advice | see record | see record | see record | advisory selection | Heuristic dependency indication only | Can prioritize manual regeneration | see record | SRC-1, `internal/core/affected.go` | none | incomplete dependency witness | Books consumes quote files but empty-glob branch checks inbox archives. |
| [RT-RTE-maintenance-write](runtime.md#rt-rte-maintenance-write) | check/evidence production | implemented | [EPI-OBJ-tasks](#epi-obj-tasks) | no content change | Requested task identity among open lines | see route | see route | see route | exact/fuzzy candidate selector | Match confidence only; no completed-work evidence | Selects line or rejects missing/ambiguous match | see route | SRC-1, `internal/core/tasks.go` | none | none | Score gap is not outcome verification. |
| [RT-RTE-maintenance-write](runtime.md#rt-rte-maintenance-write) | disposition/acceptance | implemented | [EPI-OBJ-tasks](#epi-obj-tasks) | non-truth-apt policy/content update: close selected task | Selected open marker to checked marker | see route | see route | see route | enforcing write | Acceptance of target selection only, not claim of real-world success | Removes task from later open-task previews | see route | SRC-1, `internal/core/tasks.go` | none | operational disposition only | No second approval or task execution check. |
| [RT-RTE-maintenance-write](runtime.md#rt-rte-maintenance-write) | content transformation | implemented | [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages) | truth-apt transformation: non-ampliative reshaping | Existing descriptions and manifest to index | see route | see route | see route | rebuild/preserve | Source count describes listed paths, not evidential strength | Retains descriptions for later navigation | see route | SRC-1, `internal/core/index.go` | none | none | Path/title matching does not revalidate old descriptions. |
| [RT-RTE-vault-consume](runtime.md#rt-rte-vault-consume) | operational admission/selection/consumption | implemented | Wiki, task and generated-page objects above | no content change | Query/brief/view selection | see route | see route | see route | delivery/advisory | Selection not endorsement | Offers metadata, retained log/task text or bodies to consumer | see route | SRC-1, `internal/core/brief.go` | [RT-CLM-work-split](runtime.md#rt-clm-work-split) | none | Actual answer dependence unobserved; brief outputs only selected projections. |
| [RT-RTE-ingest-cycle](runtime.md#rt-rte-ingest-cycle) | lineage/freshness/recovery | implemented | [RT-OBJ-ingests](runtime.md#rt-obj-ingests) | no content change | Abort/failure recovery | see route | see route | see route | lifecycle transition/manual recovery | No withdrawal of false claims established | Abort unblocks next prepare; no content rollback | see route | SRC-1, `cmd/sparks/ingest.go` | none | abort is not retraction | Scan deletion removes metadata visibility, not truth-based repudiation. |
| [RT-RTE-product-build](runtime.md#rt-rte-product-build) | check/evidence production | implemented | Product sources and [RT-OBJ-contract](runtime.md#rt-obj-contract) | no content change | Authored tests/vet/build/copy parity | see route | see route | see route | CI/process results | Program-specific assertions only | Possible build failure; merge/deployment veto unresolved | see route | SRC-1, `.github/workflows/ci.yml` | none | none | No observed passing tests, causal experiment or wiki-answer oracle. |

No lifecycle-integration row is inferred from storage, indexing or links: the inspected routes do not establish an evidence-consuming acceptance decision for a substantive claim followed by integration. This is bounded to the listed binary paths and shipped protocol; inaccessible agent cognition and hypothetical user Git hooks are not assigned absent evaluators.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-work-split](runtime.md#rt-clm-work-split) | see record | SRC-1, `internal/contract/contract.md`, doctrine/design | see record | [RT-RTE-ingest-cycle](runtime.md#rt-rte-ingest-cycle), [RT-RTE-vault-consume](runtime.md#rt-rte-vault-consume), [EPI-RTE-projects-extract](#epi-rte-projects-extract), [EPI-RTE-books-extract](#epi-rte-books-extract) | none supplied | No agent-quality comparison | External agent owns open semantic writing; binary supplies deterministic processing | Literal claim that CLI does not understand content must not imply semantic neutrality: deterministic status/title heuristics add interpretive claims. No runtime record supersession required. |
| [RT-CLM-mechanical-integrity](runtime.md#rt-clm-mechanical-integrity) | see record | SRC-1, `internal/contract/contract.md`, doctrine/design | see record | [RT-RTE-maintenance-write](runtime.md#rt-rte-maintenance-write), [EPI-RTE-health-check](#epi-rte-health-check), [EPI-RTE-affected-select](#epi-rte-affected-select) | none supplied | No reliability measurement | Selected mechanical mechanisms and diagnostics are wired | Not comprehensive admission; advisory dependency selection can omit a Books input change. |
| [EPI-CLM-revision-sources](#epi-clm-revision-sources) | see record | SRC-1, `internal/contract/contract.md`, doctrine/design | see record | [RT-RTE-contract-install](runtime.md#rt-rte-contract-install) delivers policy; [EPI-RTE-semantic-revision](#epi-rte-semantic-revision) is doctrine only | none supplied | No actual before/after contradiction trace | An explicit request to retain contradictions and both sources | Not implemented semantic comparison, acceptance or observed criticism. |
| [EPI-CLM-stable-maturity](#epi-clm-stable-maturity) | see record | SRC-1, `internal/contract/contract.md`, doctrine/design | see record | [RT-RTE-maintenance-write](runtime.md#rt-rte-maintenance-write), [EPI-RTE-projects-extract](#epi-rte-projects-extract) | none supplied | No review record | Stable is a declared convention, checked only as an enum | Generated pages receive stable automatically; Projects reinterprets it as Shipped. Neither establishes source review or delivery. |

## Bounded conclusion

Sparks acquires human capture and attributed text, retains archives and agent-written files, and supplies metadata, selected text and rendered bodies for later use. Acquisition preserves some text and source pointers but does not import demonstrated source warrant. Quote rendering drops raw-path lineage; generated frontmatter supplies no source paths. Index rebuilding preserves descriptions without a new support check. These are implemented persistence/consumption affordances, not observed reliance or accepted knowledge: see [RT-RTE-ingest-cycle](runtime.md#rt-rte-ingest-cycle), [RT-RTE-vault-consume](runtime.md#rt-rte-vault-consume) and the collection records.

The code is not epistemically inert merely because it is deterministic. Counts and field selections can be derived within their parser domain, conditional on readable selected inputs and manifest state. They do not establish source truth or exhaustive coverage. More consequentially, [EPI-RTE-books-extract](#epi-rte-books-extract) guesses source identity from punctuation, and [EPI-RTE-projects-extract](#epi-rte-projects-extract) converts maturity into shipping status. The counterexamples retained in those records establish non-entailment without target execution. Their output can be persisted and read without an intervening acceptance check. That operational route gives the generated claims exposure, not warrant.

The semantic protocol explicitly asks agents to compare captures with existing pages, preserve conflicting sources, choose cautious maturity and cite pages in answers. It neither specifies a reproducible acceptance criterion for a substantive claim and intended use nor provides an inspected model evaluator. Actual truth-apt outputs are unavailable, so the production relation of external-agent summaries/syntheses is indeterminate, not automatically ampliative. Evidence-consuming acceptance and post-acceptance integration remain unestablished, independently of the positive retention and revision-policy findings: [EPI-RTE-semantic-revision](#epi-rte-semantic-revision).

Mechanical checks have narrow licenses: schema membership, graph/path availability, source-mtime comparisons and punctuation-count proxies. Their consumer paths are caller-visible issues/exit signals and selected brief revisit suggestions, not enforced semantic admission. Finalization may archive and clear content without consuming a clean health report. Task matching and completion have stronger operational force: a selected marker is changed and later brief previews omit it, but no evaluator checks whether the underlying work succeeded. Abort and scan deletion are administrative recovery/visibility changes, not truth-based retraction. User-configured Git hooks remain an opaque possible commit gate, not an attributed semantic evaluator.

Persistence can support later improvement but does not itself establish learning, reflection, autonomy or self-improvement. No source-supplied execution or causal comparison establishes increased future capacity or evidence-responsive change to Sparks' own behavior-determining organization. The shipped contradiction protocol is a criticism affordance; it is not a demonstrated iterative theory-building episode. Distributed-parametric learning and internal criticism remain uninspected, rather than absent. These conclusions are independent and bounded by the source and coverage above.

## Shared records

### Operative objects

#### EPI-OBJ-inbox-raw
Label: Inbox and raw capture

Source-native identity: `inbox.md` entries and `raw/` files, including `raw/inbox/YYYY-MM-DD.md`. Representational form: natural-language capture; separators/dates are symbolic parsing structure. Storage substrate: Markdown files. Evidence: SRC-1, `internal/contract/contract.md`, `internal/inbox/archive.go`. No counterpart object in runtime; distinct from lifecycle rows [RT-OBJ-ingests](runtime.md#rt-obj-ingests). Archive copies captured content by date; its truth is not checked.

> **Raw** is the source of truth. **Wiki** is a derived view. **Manifest** tracks state for incremental operations. All three are plain files on disk (the manifest is a single SQLite file), versioned by git.
> --- `internal/contract/contract.md`

#### EPI-OBJ-wiki-pages
Label: Derived wiki pages

Source-native identity: wiki entity/concept/summary/synthesis bodies and their source/maturity frontmatter, including Revision text and descriptions later reused by index. Representational form: natural-language propositions plus symbolic metadata consumed by fixed filters. Storage substrate: Markdown files; frontmatter projections in SQLite. Evidence: SRC-1, `internal/contract/contract.md`, `internal/core/index.go`. Distinct from runtime's static [RT-OBJ-contract](runtime.md#rt-obj-contract), which requests these writes rather than containing their accumulated results. No actual page is supplied. The quote in [EPI-CLM-revision-sources](#epi-clm-revision-sources) supplies the semantic write policy; the runtime's [RT-RTE-vault-consume](runtime.md#rt-rte-vault-consume) supplies later consumers.

#### EPI-OBJ-quotes
Label: Quotes collection

Source-native identity: generated `wiki/collections/Quotes.md`. Representational form: quoted natural language and copied attribution; counts are symbolic output. Storage substrate: Markdown. Evidence: SRC-1, `internal/collections/quotes.go`. Unlike [RT-OBJ-contract](runtime.md#rt-obj-contract), this is a derived content artifact, not static instructions. See [EPI-RTE-quotes-extract](#epi-rte-quotes-extract) for the load-bearing passage and loss of SourcePath.

#### EPI-OBJ-bookmarks
Label: Bookmarks collection

Source-native identity: generated `wiki/collections/Bookmarks.md`. Representational form: natural-language descriptions, symbolic URLs and grouped counts. Storage substrate: Markdown. Evidence: SRC-1, `internal/collections/bookmarks.go`. No counterpart runtime object; its write is inside [RT-RTE-maintenance-write](runtime.md#rt-rte-maintenance-write). See [EPI-RTE-bookmarks-extract](#epi-rte-bookmarks-extract).

#### EPI-OBJ-books
Label: Books collection

Source-native identity: generated `wiki/collections/Books.md`. Representational form: natural-language title/context associations, symbolic grouping/counts. Storage substrate: Markdown. Evidence: SRC-1, `internal/collections/books.go`. No counterpart runtime object; compare maintenance container [RT-RTE-maintenance-write](runtime.md#rt-rte-maintenance-write). See [EPI-RTE-books-extract](#epi-rte-books-extract).

#### EPI-OBJ-reading-list
Label: Reading List collection

Source-native identity: generated `wiki/collections/Reading List.md`. Representational form: natural-language reading directives and source labels; symbolic queue count. Storage substrate: Markdown. Evidence: SRC-1, `internal/collections/reading_list.go`. No counterpart runtime object; compare [RT-RTE-maintenance-write](runtime.md#rt-rte-maintenance-write). See [EPI-RTE-reading-extract](#epi-rte-reading-extract).

#### EPI-OBJ-media
Label: Media collection

Source-native identity: generated `wiki/collections/Media.md`. Representational form: natural-language titles plus symbolic links/counts. Storage substrate: Markdown. Evidence: SRC-1, `internal/collections/media.go`. No counterpart runtime object; compare [RT-RTE-maintenance-write](runtime.md#rt-rte-maintenance-write). See [EPI-RTE-media-extract](#epi-rte-media-extract).

#### EPI-OBJ-ideas
Label: Ideas collection

Source-native identity: generated `wiki/collections/Ideas.md`. Representational form: natural-language selected titles/status and symbolic grouping/path labels. Storage substrate: Markdown. Evidence: SRC-1, `internal/collections/ideas.go`. No counterpart runtime object; compare [RT-RTE-maintenance-write](runtime.md#rt-rte-maintenance-write). See [EPI-RTE-ideas-extract](#epi-rte-ideas-extract).

#### EPI-OBJ-projects
Label: Projects collection

Source-native identity: generated `wiki/collections/Projects.md`. Representational form: natural-language ship-status headings derived from symbolic frontmatter. Storage substrate: Markdown. Evidence: SRC-1, `internal/collections/projects.go`. No counterpart runtime object; compare [RT-RTE-maintenance-write](runtime.md#rt-rte-maintenance-write). See [EPI-RTE-projects-extract](#epi-rte-projects-extract).

#### EPI-OBJ-tasks
Label: Live Tasks collection

Source-native identity: `wiki/collections/Tasks.md`. Representational form: natural-language directives with symbolic open/done markers. Storage substrate: Markdown. Evidence: SRC-1, `internal/core/tasks.go`. Not a regenerated collection and not an ingest row. Runtime has no counterpart object; its mutation/consumption routes are [RT-RTE-maintenance-write](runtime.md#rt-rte-maintenance-write) and [RT-RTE-vault-consume](runtime.md#rt-rte-vault-consume).

> lines[idx] = strings.Replace(lines[idx], "- [ ]", "- [x]", 1)
> --- `internal/core/tasks.go`

The selector checks line identity, not work completion. A unique case-insensitive substring wins; otherwise one fuzzy match or a lead exceeding the next score by five wins. Missing/close matches reject the completion request. The caller proposes and code decides the write; no per-match human review or answer oracle is required. This is open task maintenance with manual edit/Git recovery, not an improvement experiment.

### Routes

#### EPI-RTE-semantic-revision
Label: Agent semantic revision

Part of: [RT-RTE-ingest-cycle](runtime.md#rt-rte-ingest-cycle)

This is the protocol-directed semantic part, not a second declaration of the complete ingest cycle. Endpoints/progression: prepare output and pages → external agent comparison/writing → wiki/index/log/task edits. Owner: agent under human request and shipped guidance. Context: source text, aliases and existing content the agent chooses to read. Effects requested: summaries/syntheses, contradiction records and cautious maturity, followed by finalization. Evidence: SRC-1, `internal/contract/contract.md`; passages in [EPI-CLM-revision-sources](#epi-clm-revision-sources) and [EPI-CLM-stable-maturity](#epi-clm-stable-maturity).

- implementation conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Requested agent-written pages and eventual answer; no supplied instance.
- Later read-back: Requested persisted wiki/index/log material can reach later page reads, queries and briefs; actual dependence unobserved.
- Delegated visibility: uninspected — enclosing harness, not Sparks, determines model/tool visibility.
- Selection predicate: Agent is asked to inspect relevant pages/aliases and contradictions; no programmatic semantic selector.
- Invalidation or expiry: Revision sections preserve conflict; no truth-based withdrawal procedure or mandatory expiry is specified here.
- Activation or effect: Requested direct filesystem writing and later cited synthesis; compliance not observed.
- Evidence limits: Doctrine is implemented as delivered prose, not an implemented semantic evaluator; actual outputs cannot be classified without content/trace evidence.

Admission: human initiates; external agent proposes and directly writes under prose guidance; ordinary filesystem permissions and external human edits can intervene. Sparks finalize cannot veto a contradiction. No expected-answer oracle, named substantive acceptance criterion, accepted scope or evidence-consuming acceptance record is provided. Open maintenance, not a curriculum. Recovery follows external edits/Git and administrative ingest recovery. Persistence records candidate/revision text, not necessarily accepted theory. Theory-builder conditions 1–4: each is uninspected for actual theories, because no whole theory instance, content-dependent decision, criticism/revision trace or retained-next-round use is supplied. Addressability is afforded by ordinary editable prose, not demonstrated for a theory; learning and reflective/autonomous theory-building are not inferred from these requested steps.

#### EPI-RTE-quotes-extract
Label: Quotes extraction

Part of: [RT-RTE-maintenance-write](runtime.md#rt-rte-maintenance-write)

Endpoints/progression: configured quote-file glob → blockquote parser → rendered Quotes body. Owner: deterministic extractor invoked by caller. Natural-language text and attribution are retained while parser structure is removed. Evidence: SRC-1, `internal/collections/quotes.go`. Distinct material part: this extracts quotations rather than other collection fields.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Markdown body with quote count, text and attribution or literal missing-attribution marker.
- Later read-back: Regenerate can persist the body for later page readers; actual use unobserved.
- Delegated visibility: inapplicable — extractor has no delegation; enclosing caller receives its result.
- Selection predicate: Configured glob, sorted readable files, blockquotes beginning with greater-than plus space, following attribution/blank/EOF boundaries.
- Invalidation or expiry: Regeneration overwrites output; source edits require another regeneration.
- Activation or effect: Body is offered to the dispatcher for optional persistence; no source-truth check.
- Evidence limits: Missing/unreadable files can be skipped; scanner errors are not surfaced here; completeness is not established.

Admission/recovery: caller selects regeneration; parser generates; dispatcher may reject extractor/write failures or skip persistence on dry-run. No human content approval or answer oracle; open maintenance. Manual edit/source repair and regeneration provide recovery; output edits are overwritten. Count is entailed only for parsed records. Source warrant remains unknown, and lineage is degraded: QuoteRecord has SourcePath, but the renderer emits Text and Attribution without that path.

> if r.Attribution != "" {
> fmt.Fprintf(&out, "— %s\n\n", r.Attribution)
> } else {
> out.WriteString("— (no attribution)\n\n")
> }
> --- `internal/collections/quotes.go`

#### EPI-RTE-bookmarks-extract
Label: Bookmarks extraction

Part of: [RT-RTE-maintenance-write](runtime.md#rt-rte-maintenance-write)

Endpoints/progression: configured raw link files → URL regex matches → per-file grouped URL/description body. Owner: extractor; context/state is selected file text. Effects: candidate link associations. Evidence: SRC-1, `internal/collections/bookmarks.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Markdown links and residual same-line descriptions, counts and filename headings.
- Later read-back: Dispatcher can persist Bookmarks for later readers; actual consumption unobserved.
- Delegated visibility: inapplicable — no internal delegate.
- Selection predicate: Sorted glob files; every URL match on each scanned line.
- Invalidation or expiry: Next regeneration replaces body; no content expiry.
- Activation or effect: Renders cleaned URLs and text associations without semantic check.
- Evidence limits: Unreadable files skipped; punctuation stripping and URL removal need not preserve meaning/reference.

Admission/recovery: explicit caller request, deterministic extraction and dispatcher write; errors/dry-run can prevent persistence, not reject misleading associations. No answer oracle or required human review; open maintenance with manual source repair/regeneration. For a line with multiple URLs, each output retains the other URL as part of its description; this is not evidence of a semantically accurate summary. Warrant unknown; source filename grouping preserves partial lineage, not an evidential citation check.

> clean := strings.TrimRight(u, trailingPunct)
> desc := strings.TrimSpace(strings.Replace(line, u, "", 1))
> desc = strings.TrimLeft(desc, "-*> ")
> --- `internal/collections/bookmarks.go`

#### EPI-RTE-books-extract
Label: Books extraction

Part of: [RT-RTE-maintenance-write](runtime.md#rt-rte-maintenance-write)

Endpoints/progression: default quote stream and archived book hints → probable-title heuristic/literal hint extraction → grouped Books body. Owner: extractor. Context includes quote text, attribution and archive paths. Evidence: SRC-1, `internal/collections/books.go`. Distinct from quote rendering: this assigns a source/book identity and truncates long quote context.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Sorted title headings, quote snippets or archive-path contexts and distinct-title count.
- Later read-back: Dispatcher can persist Books, supplying later page readers; actual reliance unobserved.
- Delegated visibility: inapplicable — no internal delegate.
- Selection predicate: Quotes uses default Quotes glob, not its configured override; attribution segment after first matching separator in ordered slash/comma/em-dash alternatives; archive lines matching book prefix provide literal titles.
- Invalidation or expiry: Replacement on regeneration; no canonical identity or expiry check.
- Activation or effect: Renders inferred titles as referenced books/sources without independent validation.
- Evidence limits: Quote parse failures and archive read failures can be ignored; heuristic name classification is not book verification.

Concrete implementation deduction, not execution: attribution `Ada, London` matches comma-space and yields `London`. A raw author/location attribution is compatible with that input and need name no book. The renderer nevertheless puts London under a book heading/count. Thus the inferred book/source proposition is not entailed by the input, even though the string transformation is deterministic. In contrast, an explicit `book: Dune` line is literal supplied book content, not a new heuristic title conjecture. Snippet truncation at 80 bytes and omitted quote raw paths limit context/lineage. Count is over distinct title strings, not verified distinct books.

Admission/recovery: explicit regeneration; code proposes and writes without human title approval, expected-answer oracle or source-identity check. Open maintenance. Dispatcher errors/dry-run can stop a write; manual source changes/regeneration recover. No evidence-consuming acceptance decision intervenes.

> for _, sep := range []string{" / ", ", ", " — "} {
> if i := strings.Index(attr, sep); i > 0 {
> return strings.TrimSpace(attr[i+len(sep):])
> }
> }
> --- `internal/collections/books.go`

> fmt.Fprintf(&out, "%d distinct book(s) referenced.\n\n", len(sortedTitles))
> --- `internal/collections/books.go`

#### EPI-RTE-reading-extract
Label: Reading queue extraction

Part of: [RT-RTE-maintenance-write](runtime.md#rt-rte-maintenance-write)

Endpoints/progression: archive to-read lines → exact-text deduplication → Reading List queue. Owner: extractor; directives and archive paths become rendered queue entries. Evidence: SRC-1, `internal/collections/reading_list.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Queue Markdown, count and first retained archive path per exact text.
- Later read-back: Persisted queue can guide later reading requests; actual behavioral activation unobserved.
- Delegated visibility: inapplicable — no internal delegate.
- Selection predicate: Sorted raw/inbox archives, case-insensitive prefix, exact case-sensitive captured-text deduplication.
- Invalidation or expiry: Regeneration recomputes from archives; no read/done removal criterion.
- Activation or effect: Converts historical directives into a displayed queue, without current-intent check.
- Evidence limits: Unreadable archives skipped; queue is not evidence of current endorsement or unread status.

Admission/recovery: caller requests, code selects/writes via dispatcher, no per-entry human approval or oracle; open maintenance. Errors/dry-run affect persistence; source edit/regeneration recover. The queue directives are not truth-apt assertions; the count derives only from selected unique strings. A rendered path preserves partial lineage.

> if text == "" || seen[text] {
> continue
> }
> seen[text] = true
> entries = append(entries, entry{text: text, source: rel(v.Root, path)})
> --- `internal/collections/reading_list.go`

#### EPI-RTE-media-extract
Label: Media extraction

Part of: [RT-RTE-maintenance-write](runtime.md#rt-rte-maintenance-write)

Endpoints/progression: configured media files → filename/H1 and first URL → linked Media body. Owner: extractor; effects are navigation associations, not verified work identities. Evidence: SRC-1, `internal/collections/media.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Raw-file wikilinks with titles and optional cleaned first-URL links.
- Later read-back: Dispatcher can persist Media for later readers.
- Delegated visibility: inapplicable — no internal delegate.
- Selection predicate: Sorted configured glob; title starts as filename, matching H1 can replace while title equals filename; first regex URL wins.
- Invalidation or expiry: Replaced by regeneration; no link-health expiry.
- Activation or effect: Publishes file/title/URL associations without checking whether URL identifies the titled work.
- Evidence limits: Unreadable files skipped; actual inputs needed to establish semantic preservation.

Admission/recovery: caller request, deterministic rendering, dispatcher errors/dry-run; no human per-link approval or oracle. Open maintenance with manual source repair/regeneration. Raw-file links preserve navigation, not source warrant; first URL could be a review or unrelated link, so association remains indeterminate without actual content.

> if firstURL == "" {
> if m := urlRE.FindString(line); m != "" {
> firstURL = strings.TrimRight(m, trailingPunct)
> }
> }
> --- `internal/collections/media.go`

#### EPI-RTE-ideas-extract
Label: Ideas extraction

Part of: [RT-RTE-maintenance-write](runtime.md#rt-rte-maintenance-write)

Endpoints/progression: configured idea files → selected title/status → grouped Ideas body with source paths. Owner: extractor. Evidence: SRC-1, `internal/collections/ideas.go`. This selects fields; it does not synthesize the idea's body.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Title/path entries grouped by normalized status, including custom statuses.
- Later read-back: Persisted Ideas can feed later page reads.
- Delegated visibility: inapplicable — no internal delegate.
- Selection predicate: Sorted glob; last H1 and last status line encountered override prior values; filename and uncategorized fallbacks.
- Invalidation or expiry: Replacement on regeneration; status is not independently refreshed.
- Activation or effect: Exposes supplied title/status fields and count, without a status-truth check.
- Evidence limits: Comment says first H1, but loop repeatedly assigns; body and interpretation context are omitted.

Admission/recovery: explicit regeneration; code selects and dispatcher persists, no oracle or per-item human review. Open maintenance; errors/dry-run affect writes, source editing/regeneration recover. Source path is preserved, source warrant unknown. Non-ampliative classification is limited to reporting the selected field values, not to claiming a comprehensive or faithful note summary.

> if strings.HasPrefix(line, "# ") {
> title = strings.TrimSpace(strings.TrimPrefix(line, "# "))
> }
> if strings.HasPrefix(strings.ToLower(line), "status:") {
> status = strings.TrimSpace(line[len("status:"):])
> }
> --- `internal/collections/ideas.go`

#### EPI-RTE-projects-extract
Label: Projects extraction

Part of: [RT-RTE-maintenance-write](runtime.md#rt-rte-maintenance-write)

Endpoints/progression: manifest entity pages with project tag → group by maturity → Projects ship-status headings and links. Owner: extractor; symbolic metadata is interpreted into natural-language status. Evidence: SRC-1, `internal/collections/projects.go`, contrasted with `internal/contract/contract.md`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Tracked-project count and headings Building, Shipped, Exploring, Archived.
- Later read-back: Dispatcher can persist Projects; future readers see status headings with links, not an acceptance receipt.
- Delegated visibility: inapplicable — no internal delegate.
- Selection predicate: Type entity, case-insensitive project tag; fixed maturity order and label map.
- Invalidation or expiry: Regeneration replaces output; changes in manifest depend on scan freshness.
- Activation or effect: Publishes ship-status claims from maturity alone.
- Evidence limits: No ship-date, deployment result, human status approval or independent status evaluator is consulted.

Concrete implementation deduction: an entity with tag project and maturity stable is placed under Shipped. Under the shipped page contract, stable means well-sourced, reviewed and unlikely to change. A reviewed, well-sourced description of an unshipped project satisfies that definition. Shipping therefore does not follow from the input. This is a deterministic ampliative status conjecture, not entailed derivation. The same map also interprets historical as Archived; none of these labels receives an outcome check here.

Admission/recovery: caller requests; code assigns labels and dispatcher writes without a second human gate or expected-answer oracle. Open maintenance; failures/dry-run can prevent writing, manual metadata/source repair and regeneration recover. The deliberate design mapping does not establish empirical equivalence. See [EPI-CLM-stable-maturity](#epi-clm-stable-maturity).

> maturityLabel := map[string]string{
> "working":    "Building",
> "stable":     "Shipped",
> "seed":       "Exploring",
> "historical": "Archived",
> }
> --- `internal/collections/projects.go`

#### EPI-RTE-health-check
Label: Mechanical health checks

Part of: [RT-RTE-maintenance-write](runtime.md#rt-rte-maintenance-write)

Endpoints/progression: explicit lint/fmt request → manifest/filesystem parsing and predicates → issues/exit result; brief separately consumes selected lint issue kinds as revisit paths. Owner: program for predicates, caller/agent for semantic repair. Targets and domains: frontmatter required fields/enums/dates; path existence; manifest graph references and alias collisions; updated date versus listed-source mtime; punctuation-count thinness proxy. Evidence: SRC-1, `internal/lint/lint.go`, `internal/frontmatter/frontmatter.go`, `cmd/sparks/fmt.go`, `cmd/sparks/lint.go`, `internal/core/brief.go`. Unlike the parent mutation container, this record owns only diagnostic production and its advisory consumers, not collection writes.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Issue list/counts; fmt and lint text mode fail on issues; lint JSON returns serialization result without issue-count failure.
- Later read-back: inapplicable — diagnostics do not retain reports; brief recomputes selected signals from retained files/manifest.
- Delegated visibility: inapplicable — no internal delegate; CLI/MCP caller receives findings.
- Selection predicate: Lint's eight named checks; fmt walks chosen/default Markdown glob; brief keeps stale/thin issues and computes seed-orphans separately.
- Invalidation or expiry: Results describe current read/manifest state; scan freshness is a precondition, no automatic freshness endorsement.
- Activation or effect: Caller can act on issues; brief offers revisit paths. No automatic repair, substantive acceptance or finalize veto is implemented by these checks.
- Evidence limits: Source existence and metadata validity do not establish source truth, adequate support, successful contradiction resolution or completeness; skipped read/DB errors can hide findings.

Admission comparison: caller proposes a diagnostic request; fixed predicates decide findings; external user/agent decides repairs. No expected semantic answer oracle or mandatory human content acceptance. Open maintenance. Check failure does not roll back files. The frozen lint CLI has no fix flag; fmt reports rather than rewrites. This qualifies the prose safe-fix claim, without denying implemented diagnostics.

Concrete deduction: outside headings/fences, body `False. False. False.` reaches punctuation count three and avoids thin-page warning, regardless of truth. Conversely a correct two-sentence definition can be flagged. Thus thinness is a length proxy, not a semantic-quality evaluator. A listed path can exist while supporting no page assertion; dead-source check establishes availability only. Generated collection headers set sources empty, while Validate reports empty sources: generation alone is not even a clean diagnostic result.

> if len(fm.Sources) == 0 {
> issues = append(issues, "missing required field: sources (must list raw/ paths)")
> }
> --- `internal/frontmatter/frontmatter.go`

> switch r {
> case '.', '!', '?':
> count++
> }
> --- `internal/lint/lint.go`

> case "stale-pages":
> r.Stale = append(r.Stale, iss.Path)
> case "thin-pages":
> r.Thin = append(r.Thin, iss.Path)
> --- `internal/core/brief.go`

#### EPI-RTE-affected-select
Label: Affected collection advice

Endpoints/progression: caller → changed manifest paths since last completed ingest → fixed mapping → affected collection names/reasons. Owner: code for mapping, caller for regeneration. Context/state: manifest change state and configured/default globs. This is distinct from [RT-RTE-maintenance-write](runtime.md#rt-rte-maintenance-write): it advises which maintenance writes to request, rather than doing those writes. It shares transport with [RT-RTE-mcp-tools](runtime.md#rt-rte-mcp-tools), not identity. Evidence: SRC-1, `internal/core/affected.go`, checked against `internal/collections/books.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Affected names and path reasons, or empty set/error.
- Later read-back: inapplicable — this function does not retain advice; future calls reread changed-path state.
- Delegated visibility: inapplicable — no internal delegate; result goes to requesting CLI/MCP client.
- Selection predicate: Path-prefix matches against glob prefix; Projects checks wiki/entities changes; other empty-glob derived collections check raw/inbox changes.
- Invalidation or expiry: Recomputed per call relative to last completed ingest; stale manifest limits input completeness.
- Activation or effect: Advisory collection selection; no regeneration is invoked here.
- Evidence limits: Prefix advice is not semantic dependency validation; downstream caller obedience and regenerated freshness are unobserved.

Counterexample to completeness: Books reads default raw/quotes as well as inbox archives, but its empty-glob affected branch triggers only on inbox changes. A quote-only path change can affect Books content without selecting Books here. This implementation deduction bounds incremental-regeneration claims. Caller proposes the query, program decides suggestions; there is no expected-output oracle, required human confirmation or improvement trigger. Open maintenance; no persisted change or rollback.

> if anyMatches(changed, func(p string) bool { return strings.HasPrefix(p, "raw/inbox/") }) {
> reason[name] = []string{"raw/inbox/* changed"}
> }
> --- `internal/core/affected.go`

### Claims

#### EPI-CLM-revision-sources
Label: Preserve conflicting sources

Part of: [RT-CLM-mechanical-integrity](runtime.md#rt-clm-mechanical-integrity)

Claimed operation: agents reconcile new and existing content by noting contradictions and both sources, without silent overwrite. This makes the particular semantic obligation explicit within the supplied invariants claim. Source: SRC-1, `internal/contract/contract.md`, doctrine/design. Installed prose can request this, but [EPI-RTE-semantic-revision](#epi-rte-semantic-revision) remains doctrine only as a semantic procedure.

> 4. If an existing wiki page contradicts a new entry, append a `## Revision` section noting the contradiction and both sources. Never silently overwrite.
> --- `internal/contract/contract.md`

#### EPI-CLM-stable-maturity
Label: Stable maturity meaning

Claimed operation/warrant: stable pages are well-sourced, reviewed and unlikely to change; new pages should normally be seed. Source: SRC-1, `internal/contract/contract.md`, doctrine/design. Distinct from [RT-CLM-mechanical-integrity](runtime.md#rt-clm-mechanical-integrity): this is a meaning/reliance convention for metadata, not a generic integrity guarantee. The binary validates enum membership, not review. Header generation assigns stable without a review decision; Projects applies a different operational interpretation.

> - **stable** — well-sourced, reviewed, unlikely to change
> --- `internal/contract/contract.md`

> 5. Set `maturity: seed` on new pages unless clearly well-sourced.
> --- `internal/contract/contract.md`

> title: %s
> type: collection
> maturity: stable
> sources: []
> created: %s
> updated: %s
> --- `internal/collections/header.go`
