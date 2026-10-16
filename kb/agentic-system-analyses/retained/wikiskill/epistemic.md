---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "WikiSkill's truth-apt lessons, procedural candidates, evaluator domains and bounded admission authority."
run-id: AAS-2026-10-15-wikiskill-baafad05d35e-01
reviewed-boundary: da6984caca09d5f81b2336cf3067b59c0c18bb1e
---

# WikiSkill epistemic report

## Source-and-claim boundary

The question is whether experience becomes warranted reusable knowledge, or instructions selected for an evaluator outcome, and what later behavior each result can govern. Scope and exclusions: see [boundary](boundary.md#boundary-and-evidence). Evidence identities and layers: see [Source register](boundary.md#source-register). All added source inspection below belongs to SRC-1 at the frozen commit. No target execution occurred.

Public claims are [EPI-CLM-wiki-lessons](#epi-clm-wiki-lessons) and [RT-CLM-mcp-separation](runtime.md#rt-clm-mcp-separation). The former concerns the Wiki/skill distinction, score-based adoption and retained lessons. The latter concerns local operational privileges, not truth. No supplied fact needs supersession: the broad runtime routes remain valid containers, but their checking, retention and selection functions require separation here.

| Entry point or operation | Source path | Coverage and records |
|---|---|---|
| Product CLI, research CLI, study and results dispatch | `src/wikiskill/cli.py` | Direct complete read; ordinary and alternate dispatch agree with [RT-RTE-product-round](runtime.md#rt-rte-product-round), [RT-RTE-research-evolve](runtime.md#rt-rte-research-evolve), [RT-RTE-isolated-study](runtime.md#rt-rte-isolated-study); results adds [EPI-RTE-snapshot-check](#epi-rte-snapshot-check). |
| Product exposed operations | `src/wikiskill/product_cli.py`, `src/wikiskill/product.py` | Direct operation-name/dispatch search; direct learn/propose/feedback bodies. Other controller progression and scoring findings supplied by [RT-RTE-product-round](runtime.md#rt-rte-product-round). |
| MCP registered tools | `src/wikiskill/mcp_server.py` | Direct tool registration read and function search; no independent learning gate beyond product calls. See [RT-CLM-mcp-separation](runtime.md#rt-clm-mcp-separation). |
| Native dispatch, bind, collect, fail; install/restore | `src/wikiskill/native_agents.py`, `src/wikiskill/product_install.py` | Supplied [RT-RTE-native-handoff](runtime.md#rt-rte-native-handoff), [RT-RTE-skill-install](runtime.md#rt-rte-skill-install). Delivery/isolation requests do not validate lesson semantics. |
| Feedback begin/work/finish/skip | `src/wikiskill/feedback_loop.py` | Direct skip/work/finish read; initialization supplied by [RT-RTE-feedback-gate](runtime.md#rt-rte-feedback-gate). Skip closes without an adoption decision. |
| Research Wiki rendering, replacement, index regeneration and proposer staging | `src/wikiskill/wiki_maintainer.py`, `src/wikiskill/officeqa/wiki_agents.py` | Direct rendering-through-application, Maintainer call and Proposer staging reads; [EPI-RTE-wiki-index](#epi-rte-wiki-index) transforms [MEM-OBJ-research-wiki](memory.md#mem-obj-research-wiki), not product JSON patterns. Structural edits and full replacements are not truth checks. |
| Product Wiki views and authoring context | `src/wikiskill/product.py` | Direct `_wiki_view` and `_context` reads confirm separate rendering from replayed mappings; see [EPI-OBJ-wiki-patterns](#epi-obj-wiki-patterns) and supplied [MEM-OBJ-patterns](memory.md#mem-obj-patterns). |
| Additional callable research controllers | `src/wikiskill/officeqa/loop.py`, `src/wikiskill/spreadsheet/loop.py` | Not separately inspected here; the supplied refusal identifies promotion and candidate-file resume paths. Prevents complete research-controller enumeration and universal checkpoint, provenance or recovery comparisons; engine and isolated-study findings remain bounded to their named routes. |
| Paper-style patch, Wiki update, skill contracts and skill joining | `src/wikiskill/paper_alignment/contracts.py` | Direct complete read; [EPI-RTE-paper-contract](#epi-rte-paper-contract). This distinguishes structured study checks from minimal product admission. |
| Product Maintainer role | `src/wikiskill/resources/product/roles/maintainer.md` | Direct complete read; [EPI-OBJ-wiki-patterns](#epi-obj-wiki-patterns). Other role guidance supplied by [RT-BAP-role-guidance](runtime.md#rt-bap-role-guidance). |
| Example evaluator | `examples/text-cleanup/score.py` | Direct complete read; [EPI-RTE-label-score](#epi-rte-label-score). Concrete domain, not an evaluator for arbitrary knowledge. |
| Bundled lesson and README | `src/wikiskill/resources/research/repeatability-20260908/wiki-deliver-the-recalculated-workbook.md`, `README.md` | Direct complete lesson read and README layer/example section; [EPI-OBJ-workbook-lesson](#epi-obj-workbook-lesson), [EPI-CLM-wiki-lessons](#epi-clm-wiki-lessons). Artifact availability is not route provenance. |
| Research evolve, isolated study and tool boundary | `src/wikiskill/engine.py`, `src/wikiskill/spreadsheet/study.py`, `src/wikiskill/isolated/runtime.py`, `src/wikiskill/isolated/tools_server.py` | Supplied runtime findings, plus direct study operation search; [RT-RTE-research-evolve](runtime.md#rt-rte-research-evolve), [RT-RTE-isolated-study](runtime.md#rt-rte-isolated-study). Actual tool enforcement and reads remain unobserved. |
| Other domain scoring, dataset adapters, research result recomputation scripts and bundled traces | `src/wikiskill/officeqa/scoring.py`, `src/wikiskill/resources/research/`, `scripts/` | Relevant but unassessed beyond supplied runtime and results verifier. Prevents a domain-complete evaluator assessment, independent verification of reported improvement, causal attribution and a system-complete negative about acceptance routes. |

No hook mechanism is established by the inspected CLI/MCP dispatch; this is not an exhaustive absence finding about the repository. External host inference, arbitrary scorer validity, user evidence truth and provider internals remain outside accessible implementation evidence. Missing linked execution provenance prevents attributing the bundled lesson to a particular checked/accepted run. Missing controlled comparisons prevents attributing any improvement to Wiki maintenance, proposer criticism, isolation or another component separately.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-wiki-patterns](#epi-obj-wiki-patterns) | Scoped procedural explanations and lessons; actual submission semantics generally unknown | see record | SRC-1, `src/wikiskill/product.py` | Identifier-backed retention is not semantic acceptance. |
| [MEM-OBJ-research-wiki](memory.md#mem-obj-research-wiki) | Research Markdown lessons and their extracted headings/summaries | see record | SRC-1, `src/wikiskill/wiki_maintainer.py`, `src/wikiskill/officeqa/wiki_agents.py` | Index extraction reshapes these pages, not product journal patterns; no source-truth check. |
| [EPI-OBJ-workbook-lesson](#epi-obj-workbook-lesson) | A claim about formula caches and delivered versus inspected workbooks | see record | SRC-1, `src/wikiskill/resources/research/repeatability-20260908/wiki-deliver-the-recalculated-workbook.md` | Available candidate witness; correctness and production/check provenance unverified. |
| [RT-OBJ-product-journal](runtime.md#rt-obj-product-journal) | Event and integrity assertions, not reusable explanatory content by themselves | see record | SRC-1, `src/wikiskill/product.py` | Local consistency, not authenticated truth. |
| [RT-RTE-product-round](runtime.md#rt-rte-product-round) | Training outputs, human feedback and skill text are distinct inputs/products within this route | see record | SRC-1, `src/wikiskill/product.py` | No actual skill submission inspected; instruction text may contain assertions or non-truth-apt commands. |
| [RT-RTE-feedback-gate](runtime.md#rt-rte-feedback-gate) | Pair verdicts and requirement-fulfillment reports about named cases | see record | SRC-1, `src/wikiskill/feedback_loop.py` | Evidence strings are supplied reports, not independently checked observations. |
| [EPI-RTE-label-score](#epi-rte-label-score) | Exact equality of normalized-boundary output and a supplied reference label | see record | SRC-1, `examples/text-cleanup/score.py` | Says nothing about truth of the reference itself. |
| [RT-CMP-host-model](runtime.md#rt-cmp-host-model), [RT-CMP-research-model](runtime.md#rt-cmp-research-model) | Cannot individuate truth-apt parameter content from accessible evidence | see records | SRC-1, `src/wikiskill/product.py`, `src/wikiskill/isolated/runtime.py` | Distributed-parametric internals uninspected; text-memory learning remains independent. |

## Authority-route ledger

Each entry is an overlay, not a replacement of its declaring record. Split entries distinguish functions even where one controller implements them. Fields owned by a cited record say see; the architectural status and content relation below are this report's assessment.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-product-round](runtime.md#rt-rte-product-round) | content transformation | implemented | see record | truth-apt transformation: acquisition/import | see record | see record | see record | see record | see record | Source warrant unknown: supplied scores, outputs and feedback retain identifiers, not independent corroboration | see record | see record | SRC-1, `src/wikiskill/product.py` | none | none | Authorship and semantic validity external. |
| [RT-RTE-product-round](runtime.md#rt-rte-product-round) | content transformation | doctrine only | [EPI-OBJ-wiki-patterns](#epi-obj-wiki-patterns) | truth-apt transformation: indeterminate | see record | see record | see record | see record | see record | No semantic preservation, entailment or non-entailment established for an actual Maintainer/Proposer submission | see record | see [RT-BAP-role-guidance](runtime.md#rt-bap-role-guidance) | SRC-1, `src/wikiskill/resources/product/roles/maintainer.md` | [EPI-CLM-wiki-lessons](#epi-clm-wiki-lessons) | Semantic consolidation requested, not observed | Remaining possibilities include reshaping, derivation and conjecture; needs linked inputs and actual outputs. |
| [RT-RTE-product-round](runtime.md#rt-rte-product-round) | check/evidence production | implemented | [EPI-OBJ-wiki-patterns](#epi-obj-wiki-patterns) | no content change | see record | see record | see record | see record | see record | Nonempty content and allowed source IDs only; not entailment from cited records | see record | see record | SRC-1, `src/wikiskill/product.py` | [EPI-CLM-wiki-lessons](#epi-clm-wiki-lessons) | Citation membership is not semantic validation | No per-claim truth evaluator at this inspected admission point. |
| [RT-RTE-product-round](runtime.md#rt-rte-product-round) | retention | implemented | [EPI-OBJ-wiki-patterns](#epi-obj-wiki-patterns) | no content change | see record | see record | see record | see record | see record | Patterns remain candidates for later interpretation, not accepted ampliative claims merely by being stored | see record | see record | SRC-1, `src/wikiskill/product.py` | [EPI-CLM-wiki-lessons](#epi-clm-wiki-lessons) | none | Skill rejection does not retract Wiki lessons. |
| [EPI-RTE-paper-contract](#epi-rte-paper-contract) | check/evidence production | implemented | see record | no content change | see record | see record | see record | see record | see record | Structural validity and read-ID precondition, not comprehension or knowledge truth | see record | see record | SRC-1, `src/wikiskill/paper_alignment/contracts.py` | none | none | Different from product's weaker contract. |
| [EPI-RTE-paper-contract](#epi-rte-paper-contract) | content transformation | implemented | see record | truth-apt transformation: indeterminate | see record | see record | see record | see record | see record | Locator normalization preserves its intended locator role; arbitrary patch content has unresolved semantics | see record | see record | SRC-1, `src/wikiskill/paper_alignment/contracts.py` | none | none | Patching can revise or contradict a claim; no semantic invariant inferred. |
| [EPI-RTE-wiki-index](#epi-rte-wiki-index) | content transformation | implemented | [MEM-OBJ-research-wiki](memory.md#mem-obj-research-wiki) | truth-apt transformation: non-ampliative reshaping | see record | see record | see record | see record | see record | Extracted heading and summary, not warrant for either | see record | see record | SRC-1, `src/wikiskill/wiki_maintainer.py` | none | none | Concrete deduction in record; no target execution. |
| [EPI-RTE-label-score](#epi-rte-label-score) | check/evidence production | implemented | see record | truth-apt transformation: entailed derivation | see record | see record | see record | see record | see record | Equality result follows from supplied text/reference under Python string rules | see record | see record | SRC-1, `examples/text-cleanup/score.py` | none | none | Reference truth and procedure transfer not licensed. |
| [RT-RTE-product-round](runtime.md#rt-rte-product-round) | disposition/acceptance | implemented | see record | no content change | see record | see record | see record | see record | see record | Evidence-consuming acceptance of a skill for the configured validation metric; not acceptance of each explanatory claim | see record | see [RT-BAP-skill-consumption](runtime.md#rt-bap-skill-consumption) | SRC-1, `src/wikiskill/product.py` | [EPI-CLM-wiki-lessons](#epi-clm-wiki-lessons) | Metric superiority is narrower than warranted reusable explanation | Reused validation set; evaluator correctness external. |
| [RT-RTE-feedback-gate](runtime.md#rt-rte-feedback-gate) | disposition/acceptance | implemented | see record | no content change | see record | see record | see record | see record | see record | Acceptance conditional on reported case preferences, regressions and explicit requirements | see record | see record | SRC-1, `src/wikiskill/feedback_loop.py` | [EPI-CLM-wiki-lessons](#epi-clm-wiki-lessons) | Explicit requirements allow all ties | Evidence text is required, its truth not checked. |
| [RT-RTE-research-evolve](runtime.md#rt-rte-research-evolve), [RT-RTE-isolated-study](runtime.md#rt-rte-isolated-study) | disposition/acceptance | implemented | see records | no content change | see records | see records | see records | see records | see records | Binary validation superiority within each route's cases; not mechanism validation | see records | see records | SRC-1, `src/wikiskill/engine.py`, `src/wikiskill/spreadsheet/study.py` | [EPI-CLM-wiki-lessons](#epi-clm-wiki-lessons) | none | Domain scoring details unassessed; horizons differ, see records. |
| [RT-BAP-skill-consumption](runtime.md#rt-bap-skill-consumption) | operational admission/selection/consumption | implemented | see record | no content change | see record | see record | see record | see record | see record | Instructional reliance, not truth certification; validation can consume candidates before acceptance | see record | see record | SRC-1, `src/wikiskill/native_agents.py` | [EPI-CLM-wiki-lessons](#epi-clm-wiki-lessons) | none | Delivery does not establish activation. |
| [RT-RTE-skill-install](runtime.md#rt-rte-skill-install) | lineage/freshness/recovery | implemented | see record | no content change | see record | see record | see record | see record | see record | File identity/restoration scope only | see record | see record | SRC-1, `src/wikiskill/product_install.py` | [RT-CLM-mcp-separation](runtime.md#rt-clm-mcp-separation) | none | Installation/withdrawal of bytes does not retract lesson claims. |
| [EPI-RTE-snapshot-check](#epi-rte-snapshot-check) | check/evidence production | implemented | see record | truth-apt transformation: entailed derivation | see record | see record | see record | see record | see record | Recomputed snapshot consistency, not rerun task performance | see record | see record | SRC-1, `src/wikiskill/results.py` | none | none | No candidate gate consumes this verifier's return. |

A separate post-acceptance epistemic lifecycle-integration route is not established in the directly inspected product learn/propose and Wiki-edit code. They connect sources and store text before skill evaluation; changing the retained skill pointer is operational integration under the metric criterion, not demonstrated integration of accepted explanatory claims. This bounded finding does not exclude other routes in unassessed adapters or artifacts.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-wiki-lessons](#epi-clm-wiki-lessons) | see record | SRC-1, `README.md`, doctrine/design | see record | [RT-RTE-product-round](runtime.md#rt-rte-product-round), [RT-RTE-feedback-gate](runtime.md#rt-rte-feedback-gate), [RT-RTE-research-evolve](runtime.md#rt-rte-research-evolve), [RT-RTE-isolated-study](runtime.md#rt-rte-isolated-study) | No linked run inspected; [EPI-OBJ-workbook-lesson](#epi-obj-workbook-lesson) is a candidate witness only | No independent component contrast; admission does not validate proposed causes | Software separates retained experience, Wiki and skill; score-based successor selection exists on numeric paths | Universal strict improvement is qualified by explicit-requirement ties; retained lessons are not thereby semantically accepted knowledge. |
| [RT-CLM-mcp-separation](runtime.md#rt-clm-mcp-separation) | see record | SRC-1, `src/wikiskill/mcp_server.py`, doctrine/design | see record | see record | see record | see record | Tool-surface restriction, not host-wide enforcement | see record |

## Bounded conclusion

WikiSkill gives persistent text a real operational path without requiring each text claim to earn epistemic acceptance. The product's sourced-pattern check permits retention before skill evaluation. A failed candidate leaves the Wiki available to future proposers. Source identifiers preserve local lineage but do not show that a lesson follows from its sources. External reports enter with unknown warrant. Separately, research Markdown pages feed deterministic index extraction and proposer staging; this reshaping adds no warrant. That helper does not transform product JSON patterns. Product authoring contexts instead consume replayed pattern mappings, while `_wiki_view` renders separate derived pages. See [EPI-OBJ-wiki-patterns](#epi-obj-wiki-patterns), [MEM-OBJ-research-wiki](memory.md#mem-obj-research-wiki), [EPI-RTE-wiki-index](#epi-rte-wiki-index), [RT-RTE-product-round](runtime.md#rt-rte-product-round).

There are concrete, bounded checks. The example scorer decides exact label equality against a supplied reference. Paper contracts decide structure and edit applicability. The results command recomputes snapshot consistency. These licenses do not extend to reference truth, causal explanations, generalization or provider correctness. Each has its own consumer and force; the results verifier does not itself admit a candidate. See [EPI-RTE-label-score](#epi-rte-label-score), [EPI-RTE-paper-contract](#epi-rte-paper-contract), [EPI-RTE-snapshot-check](#epi-rte-snapshot-check).

Numeric routes accept a candidate skill for a configured validation criterion and intended task use, with software enforcing successor selection. The feedback route instead consumes host-reported pair verdicts and requirement evidence. Explicit requirements can license ties without regressions or worse cases. Neither route proves every sentence in the skill or Wiki. Rejection withholds successor selection, not prior Wiki retention; installation restoration protects checked bytes, not semantic retraction. See [RT-RTE-product-round](runtime.md#rt-rte-product-round), [RT-RTE-feedback-gate](runtime.md#rt-rte-feedback-gate), [RT-RTE-skill-install](runtime.md#rt-rte-skill-install).

A scoped causal explanation is visibly available in the bundled workbook lesson, but its linked production, testing and acceptance are not established. For actual model transformations the classification remains indeterminate, not automatically ampliative: linked inputs and outputs would be needed to distinguish reshaping, entailment and non-entailing conjecture. The installed API accepts text; role instructions request evidence-directed consolidation. Those are different facts. See [EPI-OBJ-workbook-lesson](#epi-obj-workbook-lesson), [EPI-OBJ-wiki-patterns](#epi-obj-wiki-patterns).

Retained and candidate skills can influence task executors through natural-language instructions, not new tool permissions. This is an implemented improvement-directed instruction adaptation path. Actual content-dependent behavior, improved future capacity, formulated criticism, autonomous theory building and exercised self-improvement remain independent unestablished conclusions, not a single negative verdict. The supplied runtime gives the separate condition-level limits. Parameters are external and no weight-changing route is established by these inspected mechanisms. See [RT-BAP-skill-consumption](runtime.md#rt-bap-skill-consumption), [RT-RTE-product-round](runtime.md#rt-rte-product-round), [RT-CMP-host-model](runtime.md#rt-cmp-host-model), [RT-CMP-research-model](runtime.md#rt-cmp-research-model).

## Shared records

### Operative objects

#### EPI-OBJ-wiki-patterns
Label: Wiki patterns
Part of: [RT-RTE-product-round](runtime.md#rt-rte-product-round)

This object is the natural-language lesson content and its symbolic source-ID links within the product learning route, not the whole route or the journal's integrity metadata. Local JSON events retain name/content/sources; later learning contexts receive replayed mappings, not rendered Wiki page bytes. `_wiki_view` separately generates pages and a link index. This is the same product content identified by the supplied [MEM-OBJ-patterns](memory.md#mem-obj-patterns), not the research Markdown tree in [MEM-OBJ-research-wiki](memory.md#mem-obj-research-wiki). The name identifies a pattern, not a separately evaluated proposition. Later model interpretation is natural-language consumption; allowed-ID membership is symbolic consumption. SRC-1, `src/wikiskill/product.py`, implementation.

> patterns[name]={'content':content,'sources':sources}
> --- `src/wikiskill/product.py`

> if not isinstance(sources,list) or not sources or any(x not in allowed for x in sources):raise ValueError('Cite permitted training request or human-feedback IDs')
> --- `src/wikiskill/product.py`

> for name,item in s['patterns'].items():
>         filename=hashlib.sha256(name.encode()).hexdigest()[:16]+'.md';p=folder/'patterns'/filename;p.parent.mkdir(exist_ok=True)
>         p.write_text('# '+name+'\n\n'+item['content']+'\n',encoding='utf-8')
> --- `src/wikiskill/product.py`

> return {'round':s['round'],'current_skill':s['current_skill'],'wiki':{name:{**v,'source_id':'pattern-'+digest([name,v])[:16]} for name,v in s['patterns'].items()},'human_feedback':s['feedback'],
> --- `src/wikiskill/product.py`

The guard's countercase matters: `allowed` also includes existing Wiki source IDs, so lineage need not reach a fresh training outcome in one hop. Semantic support is not evaluated by this loop.

> context=read(root/req['context_file']);allowed={x['source_id'] for x in context['training_records']}|{x['id'] for x in context['human_feedback']}|{x['source_id'] for x in context['wiki'].values()}
> --- `src/wikiskill/product.py`

The doctrine requests scoped knowledge and distinctions between observation and hypothesis; it does not implement those distinctions as semantic tests. This is not a second declaration of [RT-BAP-role-guidance](runtime.md#rt-bap-role-guidance): it identifies the resulting object and its admission limit.

> Preserve the meaning of original human notes and distinguish observations from hypotheses.
> --- `src/wikiskill/resources/product/roles/maintainer.md`

#### EPI-OBJ-workbook-lesson
Label: Deliver the recalculated workbook

Natural-language Markdown, stored as a bundled research resource in SRC-1, `src/wikiskill/resources/research/repeatability-20260908/wiki-deliver-the-recalculated-workbook.md`. Distinct from the generic patterns admitted by [RT-RTE-product-round](runtime.md#rt-rte-product-round): this is one available source-authored artifact, not an evidenced submission to that route. It asserts a scope condition and a mechanism involving formula-cache population and which file is delivered. Its imperative workaround is non-truth-apt policy content; its description and root-cause statements are truth-apt. Artifact presence alone does not establish production, acceptance or use.

> Formula recalculation is useful only if the recalculated file replaces the file handed to the evaluator or user.
> --- `src/wikiskill/resources/research/repeatability-20260908/wiki-deliver-the-recalculated-workbook.md`

> `openpyxl` writes formulas but does not populate cached results. A trace converted `output.xlsx` into `recalc/output.xlsx` and inspected that copy, while leaving the original uncached `output.xlsx` as the delivered artifact.
> --- `src/wikiskill/resources/research/repeatability-20260908/wiki-deliver-the-recalculated-workbook.md`

These are reported-operation assertions embedded in an available artifact, not independently observed failure or intervention evidence. The purported underlying trace and reference outcomes were not linked and inspected here. A useful explanatory candidate exists; neither its truth nor a particular conjecture-producing route follows from that existence.

### Routes

#### EPI-RTE-wiki-index
Label: Wiki index regeneration

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: apply_pattern_edits returns new and updated filenames after writing pages, index and log.
- Later read-back: Generated index remains on disk as a locator and heading/summary view for later Wiki consumers; actual later reads uninspected.
- Delegated visibility: inapplicable — deterministic local transformation, not a delegation.
- Selection predicate: Sorted patterns/*.md; first heading and first Summary line, with filename/empty-summary fallbacks.
- Invalidation or expiry: Regenerated after edits from pages currently on disk; updated pages replace full text, so old assertions need not survive.
- Activation or effect: Overwrites index.md and appends a narrative to logs.md; no epistemic acceptance decision is made.
- Evidence limits: Code deduction, not execution; summaries may omit qualifications and do not establish truth of the source pages.

Distinct from [RT-RTE-research-evolve](runtime.md#rt-rte-research-evolve): this helper is a transformation used by research Wiki maintenance, not the engine's validation gate. Its input/output storage is [MEM-OBJ-research-wiki](memory.md#mem-obj-research-wiki): Markdown pages under `wiki_dir/patterns` and a generated `wiki_dir/index.md`. It does not consume [EPI-OBJ-wiki-patterns](#epi-obj-wiki-patterns), the product's replayed JSON mapping. The default research Maintainer calls `apply_pattern_edits` on its research `wiki_dir`; the default Proposer then stages the index and pattern directory, reads the index into its prompt and exposes staged pages. These callers support an authoring-consumer path, not observed model use. SRC-1, `src/wikiskill/wiki_maintainer.py`, implementation. Owner is the Python edit helper; edit authors supply page text. Filename existence, uniqueness and safety checks permit/reject edits; neither human approval nor an answer oracle is required. This structural admission can replace content, but its index computation is separately non-ampliative.

> new_files, updated_files = apply_pattern_edits(
>                 wiki_dir, answer, iteration=iteration
>             )
> --- `src/wikiskill/officeqa/wiki_agents.py`

> patterns = wiki_dir / "patterns"
>         if patterns.is_dir():
>             shutil.copytree(patterns, staged_wiki / "patterns")
> --- `src/wikiskill/officeqa/wiki_agents.py`

> title, summary = _page_title_summary(path.read_text(encoding='utf-8'), filename=path.name)
> --- `src/wikiskill/wiki_maintainer.py`

> rows.append((path.name, title, summary))
> --- `src/wikiskill/wiki_maintainer.py`

> lines.append(f'| [{title}](patterns/{filename}) | {escaped} |')
> --- `src/wikiskill/wiki_maintainer.py`

Concrete static trace: given only `patterns/cache.md` containing `# Cache\nSummary: Reopen the delivered file.\n`, the extractor returns title `Cache` and summary `Reopen the delivered file.`; the sorted row renders `| [Cache](patterns/cache.md) | Reopen the delivered file. |`. No proposition is inferred from the procedural claim. The claim is copied into a locator view. This demonstrates reshaping, not successful knowledge synthesis.

> target.write_text(pattern.content, encoding='utf-8')
> --- `src/wikiskill/wiki_maintainer.py`

Full replacement is a countercase to any claim that maintenance only accumulates text. The helper can remove or revise a page's old claims by replacement; it does not decide whether the replacement is better warranted. The skill gate does not provide that decision either; see [RT-RTE-research-evolve](runtime.md#rt-rte-research-evolve).

#### EPI-RTE-paper-contract
Label: Paper Wiki and skill contracts

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Normalized Wiki change and resulting Wiki mapping, or normalized proposal and resulting skills mapping; invalid structures raise ContractError.
- Later read-back: Resulting Wiki feeds Proposer and resulting candidate skills feed validation in the supplied study route; actual use uninspected.
- Delegated visibility: Caller supplies existing maps, proposed content and trace-read IDs; no model invoked by contracts.
- Selection predicate: Exact edit field sets, canonical local names, unique mutation identities and local patch targets; skill metadata/headings, banned vocabulary and four distinct read IDs for a non-no_action proposal.
- Invalidation or expiry: Revalidate against current mappings; missing/nonunique patch target, duplicate mutation or incompatible structure rejects the operation. No claim-level truth expiry.
- Activation or effect: Produces revised mappings, repairs index locators and joins sorted skill text; study owns persistence and numeric selection.
- Evidence limits: Read-ID cardinality is not comprehension; lexical bans are not a semantic guarantee against answer leakage; arbitrary content patches can change meaning.

A distinct deterministic checking/editing mechanism within [RT-RTE-isolated-study](runtime.md#rt-rte-isolated-study), not a duplicate of the study gate. SRC-1, `src/wikiskill/paper_alignment/contracts.py`, implementation. Model role proposes; Python contract can veto structure; controller owns subsequent persistence and comparison. No human approval or truth oracle is required here. Trigger is structured submission; accepted structural edits can replace local passages, append content or insert content. Structural rejection leaves the caller without a returned revised mapping; no general filesystem transaction guarantee is inferred.

> if not isinstance(target,str) or not target or text.count(target)!=1:
>             raise ContractError('Patch target must occur exactly once')
> --- `src/wikiskill/paper_alignment/contracts.py`

> if len(set(read_trace_ids))<4:raise ContractError('Read at least four distinct execution traces before proposing a change')
> --- `src/wikiskill/paper_alignment/contracts.py`

> for banned in ('/Users/','ground_truth','golden.xlsx','answer_key','score_answer','r_best'):
>         if banned.lower() in skill.lower():raise ContractError('Skill contains evaluator/private-host vocabulary')
> --- `src/wikiskill/paper_alignment/contracts.py`

Filename repair is bounded: `canonical_pattern('patterns/Cache.MD')` yields `Cache.md` under inspected string rules; content is untouched by this function. Patch replacement has no such semantic-preservation invariant. Thus the combined patch route is indeterminate for truth-apt content, rather than automatically classified as reshaping. Represented objects are symbolic edit operations and natural-language Wiki/skill bodies on local mappings and later filesystem artifacts. Guidance/content conditions for theory building remain as in the supplied study record; structural checks do not establish content-directed criticism.

#### EPI-RTE-label-score
Label: Text cleanup reference comparison

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: JSON score, success boolean and feedback on stdout.
- Later read-back: When configured as product scorer, product persists score/feedback and supplies training records to later learning; no invocation observed.
- Delegated visibility: JSON stdin supplies full task including reference and output text; this is a scorer program, not a delegated model.
- Selection predicate: Strip leading/trailing whitespace from output text, then exact equality to the unmodified task reference.
- Invalidation or expiry: Recompute per request; no content-level expiry. Product comparison consistency is separately enforced by scorer configuration checks.
- Activation or effect: 1.0 or 0.0 can enter the product mean score and candidate gate; successful equality and unsuccessful equality select different feedback strings.
- Evidence limits: Exact match to a supplied label does not establish the label's truth or process correctness. No actual scored output inspected.

No counterpart with this target/domain is declared in the supplied runtime: [RT-RTE-product-round](runtime.md#rt-rte-product-round) describes an arbitrary external scorer interface, not this example evaluator. SRC-1, `examples/text-cleanup/score.py`, implementation. Target is the relation between delivered label text and a reference in the task JSON, not reusable procedural theory. The program derives the equality proposition under Python semantics. A hypothetical output `  blue sky\n` and reference `blue sky` produces equality and score 1.0; `Blue sky` does not. This is a static deduction from code, not target execution.

> actual = request['output']['text'].strip()
> expected = request['task']['reference']
> matched = actual == expected
> --- `examples/text-cleanup/score.py`

The wording of feedback is broader than its test: internal spaces and lowercase are not separately normalized or validated, but only checked indirectly if encoded by the reference. The evaluator checks an outcome, not the mechanism that produced it. Human configures the scorer and task reference; program judges; product software decides successor selection; the host supplies output. The authorizing operator can decline to configure/trust this scorer, but there is no per-output human approval requirement.

#### EPI-RTE-snapshot-check
Label: Bundled snapshot verification

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: verified:true plus captured_at, scope and cell summaries, or a raised error.
- Later read-back: inapplicable — read-only check returns summaries and does not update retained knowledge or instructions.
- Delegated visibility: inapplicable — local deterministic CLI check, not model delegation.
- Selection predicate: Snapshot digest matches stored expected digest; per-cell pairs match domain/arm, count and unique IDs; their means agree with stored summary within 1e-10; referenced skill bytes match stored hashes.
- Invalidation or expiry: Any tested inconsistency raises ValueError; cells with baseline None are skipped. Metadata rewritten consistently is not independently authenticated.
- Activation or effect: CLI results prints the return; no candidate-admission consumer inspected. Failed checks prevent a successful verification return.
- Evidence limits: Does not execute tasks, verify pair score truth, establish generation provenance or identify causal improvement. No bundled snapshot contents were independently evaluated here.

Distinct from [RT-RTE-research-evolve](runtime.md#rt-rte-research-evolve): it checks exported numerical/hash consistency, not rollout outcomes or successor choice. SRC-1, `src/wikiskill/results.py`, implementation; dispatch SRC-1, `src/wikiskill/cli.py`. Program owns recomputation; caller triggers it. Target domain is internal consistency of the supplied snapshot. No answer oracle beyond its own stored rows/hashes. Form is symbolic JSON plus referenced skill bytes on local disk.

> a=sum(x['s0'] for x in rows)/len(rows);b=sum(x['retained_val'] for x in rows)/len(rows)
> --- `src/wikiskill/results.py`

> if abs(a-c['baseline'])>1e-10 or abs(b-c['retained'])>1e-10:raise ValueError('Score mismatch')
> --- `src/wikiskill/results.py`

This produces a derived consistency result conditional on its inputs. It neither accepts an ampliative explanation nor supplies a causal experiment.

### Claims

#### EPI-CLM-wiki-lessons
Label: Wiki lessons and validated skills

SRC-1, `README.md`, doctrine/design. The public description separates raw experience, reusable Wiki patterns/explanations/counterexamples and executable skill instructions, and states score improvement as the retention rule. Distinct from [RT-CLM-mcp-separation](runtime.md#rt-clm-mcp-separation), which concerns privileged tools rather than knowledge-production claims.

> A **Wiki Maintainer** consolidates experience. A **Skill Proposer** turns relevant patterns into a candidate skill. The agent tries it on validation tasks; the system keeps it only if its score improves. If the candidate is rejected, the Wiki retains what was learned.
> --- `README.md`

> This improves the agent's working instructions without training new model weights.
> --- `README.md`

The supported mechanism is retained instruction selection, not a truth certificate for explanations. A countercase to universal strict improvement is the explicit-requirement feedback rule; unlike ordinary feedback, it requires zero worse cases rather than better>worse, allowing all ties once requirements are fulfilled.

> accepted=not no_action and fulfilled and not any(x['regressions'] for x in pairs) and (worse==0 if explicit else better>worse)
> --- `src/wikiskill/feedback_loop.py`

This source-supported qualification prevents conflating one numeric product rule with every shipped admission mode. README also scopes feedback integration as not evidence of benchmark improvement; [RT-RTE-feedback-gate](runtime.md#rt-rte-feedback-gate) preserves that distinction. No exercised improvement is inferred here.
