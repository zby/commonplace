---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "team-ai-workflows epistemic routes: lexical relevance, source reliance and host answer generation."
run-id: AAS-2026-11-09-team-ai-workflows-c00fb85f7ed1-01
reviewed-boundary: "9aebd7a6c2803da450904eb5621ae5439508ff94"
---

# team-ai-workflows epistemic report

## Source-and-claim boundary

The question is how distributed team text becomes material for an answer, and what checks license reliance on it. Scope and exclusions are see [boundary](boundary.md#boundary-and-evidence); evidence identities are see the [Source register](boundary.md#source-register). SRC-1 supplies implementation for Python/shell and doctrine/design for model instructions. No supplied execution or causal evidence establishes answer quality, compliance or improvement. External host/model internals and deployed corpus provenance remain unavailable; the excluded GIF supplies no demonstration evidence.

The public retrieval claim is [EPI-CLM-repository-rag](#epi-clm-repository-rag). Distribution is [RT-CLM-machine-distribution](runtime.md#rt-clm-machine-distribution), not an assertion that corpus propositions are verified. No stronger source-truth guarantee was found in the directly inspected README, skills or sample writing guidance. The external article's title is not treated as evidence of learning or self-improvement.

| Entry point or operation | SRC-1 source path | Coverage and evidence basis |
|---|---|---|
| `/team-setup`, settings, hook installation and verification | `.claude/skills/team-setup/SKILL.md` | Direct read; [RT-RTE-machine-setup](runtime.md#rt-rte-machine-setup); checks concern installation state, not knowledge truth |
| Direct synchronization; post-merge hook; cleanup | `.claude/skills/team-setup/scripts/sync_user_skills.sh`, `.claude/skills/team-setup/scripts/post-merge` | Direct reads; [RT-RTE-skill-sync](runtime.md#rt-rte-skill-sync); directory existence and reachability control exposure, not endorsement |
| Corpus authoring and Git distribution | `README.md`, `sources/tips/writing-knowledge.md` | Direct reads; [RT-RTE-repository-admission](runtime.md#rt-rte-repository-admission); actual author/reviewer and approval policy unspecified |
| `/docs-grep` query, full-file reading, answer, retry | `skills/docs-grep/SKILL.md` | Direct read; [RT-RTE-knowledge-search](runtime.md#rt-rte-knowledge-search), [EPI-RTE-answer-synthesis](#epi-rte-answer-synthesis), [EPI-RTE-weak-retry](#epi-rte-weak-retry); doctrine only for model behavior |
| Direct Python CLI, alternate environment root, fallback, failures, ranking and previews | `skills/docs-grep/scripts/docs_search.py` | Direct read; [EPI-RTE-keyword-ranking](#epi-rte-keyword-ranking), [EPI-RTE-preview-output](#epi-rte-preview-output); implementation, no execution |
| Retained sample propositions and guidance | `sources/api-reference/sample-api.md`, `sources/documentation/getting-started.md`, `sources/tips/writing-knowledge.md` | Direct reads; [EPI-OBJ-sources](#epi-obj-sources); sample availability does not establish real API facts |
| Host model and discovery | `README.md`, `skills/docs-grep/SKILL.md` | Supplied [RT-CMP-claude-code](runtime.md#rt-cmp-claude-code); internals excluded; parameter updates, actual context management and exact model unresolved |

This checks all shipped operational entry points identified by the supplied boundary against direct reads. It is not a system-complete negative about an adopter's external host, review process or deployment.

## Epistemic-object inventory

| object ID | candidate truth-apt content or none | claimed role | evidence source ID and local anchor | gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-sources](#epi-obj-sources) | Sample API behavior and setup assertions; writing guidance has policy and explanatory parts | see record | SRC-1 `sources/api-reference/sample-api.md` | Sample status blocks real API reliance |
| [EPI-OBJ-search-output](#epi-obj-search-output) | File excerpts and lexical counts, not truth judgments | see record | SRC-1 `skills/docs-grep/scripts/docs_search.py` | Truncated evidence, no source authentication |
| [EPI-OBJ-answer](#epi-obj-answer) | Potential answer propositions; no actual answer supplied | see record | SRC-1 `skills/docs-grep/SKILL.md` | Actual content and relation to sources not determinable |
| [RT-OBJ-docs-grep](runtime.md#rt-obj-docs-grep) | Procedure; keywords are selection strings rather than necessarily assertions | see record | SRC-1 `skills/docs-grep/SKILL.md` | Policy delivery is not compliance |
| [RT-OBJ-skill-links](runtime.md#rt-obj-skill-links) | None: symbolic references | see record | SRC-1 `.claude/skills/team-setup/scripts/sync_user_skills.sh` | Reachability gives no semantic license |
| [RT-CMP-claude-code](runtime.md#rt-cmp-claude-code) | Opaque model processing; no individuated parametric proposition | see record | SRC-1 `README.md` | Version, updates and hidden knowledge not determinable |

## Authority-route ledger

Route ID: [RT-RTE-repository-admission](runtime.md#rt-rte-repository-admission)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-sources](#epi-obj-sources).
Content/update relation: truth-apt transformation: acquisition/import. Source warrant is unknown; the workflow accepts docs copies and first-hand tips without a required provenance record.
Transition or check target: repository text retained for future search; not semantic acceptance.
Evaluator/condition and domain: see cited route; no evidence-consuming criterion for truth is specified.
Activation and timing; possible or observed result; implemented force: see cited route; repository reads implement later availability, not an observed import episode.
Epistemic authority and scope: consulted team material, not certified facts.
Operational authority: stored Markdown may become later answer context.
Behavioral-authority path: Python search then host full-file read; filesystem/text channel; ranking then advisory influence; later invocations until edited/deleted.
Evidence source ID and local anchor: SRC-1 `README.md`, `skills/docs-grep/scripts/docs_search.py`; see cited route for admission and recovery.
Claim IDs: [EPI-CLM-repository-rag](#epi-clm-repository-rag).
Mismatch marker: none. Gap/limit: retention precedes any demonstrated acceptance; no lifecycle-integration route after acceptance established in these paths.

Route ID: [RT-RTE-skill-sync](runtime.md#rt-rte-skill-sync)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [RT-OBJ-skill-links](runtime.md#rt-obj-skill-links), [RT-OBJ-docs-grep](runtime.md#rt-obj-docs-grep).
Content/update relation: no content change.
Transition or check target: skill exposure based on directory existence and destination reachability, not instruction quality.
Evaluator/condition and domain; activation and timing; possible or observed result; implemented force: see cited route.
Epistemic authority and scope: none from link creation or cleanup.
Operational authority; behavioral-authority path: see [RT-BAP-user-skills](runtime.md#rt-bap-user-skills).
Evidence source ID and local anchor: SRC-1 `.claude/skills/team-setup/scripts/sync_user_skills.sh`, `.claude/skills/team-setup/scripts/post-merge`.
Claim IDs: [RT-CLM-machine-distribution](runtime.md#rt-clm-machine-distribution).
Mismatch marker: none. Gap/limit: a kept link need not be team-owned; deletion of broken links is withdrawal of reachability, not retraction of a claim. Hook exit success cannot establish semantic or installation success.

Route ID: [RT-RTE-knowledge-search](runtime.md#rt-rte-knowledge-search)
Route function: operational admission/selection/consumption
Architectural status: doctrine only
Object/candidate ID: [RT-OBJ-docs-grep](runtime.md#rt-obj-docs-grep).
Content/update relation: non-truth-apt policy/content update: question converted into keyword selection strings.
Transition or check target: model proposes 4–8 keywords, synonyms and language variants for search.
Evaluator/condition and domain; activation and timing; possible or observed result: see cited route, limited here to its query-generation part.
Implemented force: advisory instruction, no Python count enforcement.
Epistemic authority and scope: keyword generation licenses a search, not an answer.
Operational authority: selects which corpus text is likely to reach the host.
Behavioral-authority path: host interprets skill, submits CLI arguments, Python uses them during this lookup.
Evidence source ID and local anchor: SRC-1 `skills/docs-grep/SKILL.md`.
Claim IDs: [EPI-CLM-repository-rag](#epi-clm-repository-rag). Mismatch marker: none.
Gap/limit: direct CLI bypasses this instruction; no observed query supplied.

Route ID: [EPI-RTE-keyword-ranking](#epi-rte-keyword-ranking)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-sources](#epi-obj-sources), [EPI-OBJ-search-output](#epi-obj-search-output).
Content/update relation: no content change.
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force: see record.
Epistemic authority and scope: lexical match statistics only; no license for truth, relevance completeness or answer correctness.
Operational authority: provides ordered file candidates to output selection.
Behavioral-authority path: Python result list → sorting/output slice; symbolic ranking; one invocation.
Evidence source ID and local anchor: SRC-1 `skills/docs-grep/scripts/docs_search.py`.
Claim IDs: [EPI-CLM-repository-rag](#epi-clm-repository-rag). Mismatch marker: relevance is a lexical proxy.
Gap/limit: finding words is not checking propositions against evidence.

Route ID: [EPI-RTE-preview-output](#epi-rte-preview-output)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-search-output](#epi-obj-search-output).
Content/update relation: truth-apt transformation: non-ampliative reshaping. Excerpts and paths preserve limited attribution; truncation and permissive decoding can degrade evidential context.
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force: see record.
Epistemic authority and scope: excerpt availability, not source endorsement or complete evidence.
Operational authority: selects material initially shown to the host.
Behavioral-authority path: stdout tool result; code-enforced slicing for previews, advisory text for host interpretation; current lookup.
Evidence source ID and local anchor: SRC-1 `skills/docs-grep/scripts/docs_search.py`.
Claim IDs: [EPI-CLM-repository-rag](#epi-clm-repository-rag). Mismatch marker: none.
Gap/limit: the separate full-file instruction is a countercase to interpreting preview limits as a hard answer-evidence limit.

Route ID: [EPI-RTE-weak-retry](#epi-rte-weak-retry)
Route function: check/evidence production
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-search-output](#epi-obj-search-output).
Content/update relation: no content change.
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force: see record.
Epistemic authority and scope: subjective hit sufficiency, not source truth or independently scored answer correctness.
Operational authority: model may revise keywords and continue searching.
Behavioral-authority path: host judgment under skill text; advisory force; current question.
Evidence source ID and local anchor: SRC-1 `skills/docs-grep/SKILL.md`.
Claim IDs: [EPI-CLM-repository-rag](#epi-clm-repository-rag). Mismatch marker: none.
Gap/limit: no recorded acceptance decision, threshold or independent oracle; continuation does not establish epistemic warrant.

Route ID: [EPI-RTE-answer-synthesis](#epi-rte-answer-synthesis)
Route function: content transformation
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-answer](#epi-obj-answer).
Content/update relation: truth-apt transformation: indeterminate. Acquisition from read files, paraphrase, entailed answers and conjectural additions are possible; no actual input/output pair distinguishes them. Non-entailment is not established.
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force: see record.
Epistemic authority and scope: requested source-based answer with relative paths; source warrant unknown, no general truth license.
Operational authority: answer delivered to user, with no prescribed per-answer approval gate.
Behavioral-authority path: corpus text → host interpretation → answer text; advisory force to user; current question, later retention unspecified.
Evidence source ID and local anchor: SRC-1 `skills/docs-grep/SKILL.md`.
Claim IDs: [EPI-CLM-repository-rag](#epi-clm-repository-rag). Mismatch marker: none.
Gap/limit: citation requests do not implement citation verification, acceptance or integration.

## System-claim versus route comparison

| claim ID | claimed operation or warrant | claim source ID/anchor and evidence layer | doctrine/design support | implemented route IDs | observed-run support | causal support and design limits | supported conclusion | mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-repository-rag](#epi-clm-repository-rag) | see record | SRC-1 `README.md`, doctrine/design | see record | [EPI-RTE-keyword-ranking](#epi-rte-keyword-ranking), [EPI-RTE-preview-output](#epi-rte-preview-output) | none supplied | none; lexical proxy and opaque host | retrieval code plus requested grounded synthesis | synthesis and answer correctness unobserved |
| [RT-CLM-machine-distribution](runtime.md#rt-clm-machine-distribution) | see record | SRC-1 `README.md`, doctrine/design | see record | [RT-RTE-skill-sync](runtime.md#rt-rte-skill-sync) | none supplied | none; collisions, partial failure, external discovery | operational reachability affordance | not epistemic endorsement or demonstrated improvement |

## Bounded conclusion

The repository retains externally authored/sample natural-language assertions and procedure text. Imported warrant is unknown: no source-verification or evidence-consuming acceptance criterion is prescribed in the inspected authoring, synchronization and search paths. This is not proof that real teams do no review. Sample API claims are explicitly demonstration material, not evidence about an actual SDK ([EPI-OBJ-sources](#epi-obj-sources)).

Python computes lexical statistics and reshapes selected text into paths/previews. Those checks have a deterministic ranking consumer but no truth-checking license. A weak-hit judgment and source-based answer are requested from the host; neither is observed. The source supports selection, acquisition and reshaping, not an accepted ampliative claim or a demonstrated entailed answer. No particular answer's truth-apt content can be individuated without an answer trace ([EPI-RTE-answer-synthesis](#epi-rte-answer-synthesis)).

Installation checks and cleanup change operational exposure, not semantic reliance. No after-acceptance lifecycle integration is established by retaining files or invoking them. Host parameter changes and hidden reasoning are uninspected; fixed or changing weights cannot be inferred. The retry instruction can adapt search behavior within a question, but supplies no retained criticism loop or evidence of improved future capacity. Distribution of changed skill text affords later behavioral change, independently of any learning, reflection, autonomy or self-improvement claim; no exercised benefit or causal attribution follows from these sources.

## Shared records

### Operative objects

#### EPI-OBJ-sources
Label: sources Markdown corpus

Source-native identity: `sources/` Markdown files. Natural-language assertions and advice stored in Git-tracked filesystem text. Distinct from [RT-OBJ-docs-grep](runtime.md#rt-obj-docs-grep), which instructs the consumer; no supplied corpus-object counterpart. SRC-1 `sources/api-reference/sample-api.md` supplies a candidate instance, not its actual SDK provenance. Setup assertions and writing advice are separately identifiable text parts in `sources/documentation/getting-started.md` and `sources/tips/writing-knowledge.md`; no distinct checks or approval mechanisms are prescribed for them.

> Sample knowledge for the search demo. Replace with your SDK's real API reference.
> --- `sources/api-reference/sample-api.md`

> Destroys the widget. Destroying an unknown id is a no-op, not an error.
> --- `sources/api-reference/sample-api.md`

#### EPI-OBJ-search-output
Label: ranked search output
Part of: [RT-RTE-knowledge-search](runtime.md#rt-rte-knowledge-search)

The object is a material product of the supplied route, not a duplicate of its whole progression. Representational form: symbolic counts/relative paths plus natural-language line excerpts. Substrate: transient Python list/stdout, no output store. SRC-1 `skills/docs-grep/scripts/docs_search.py`, implementation. Counts concern textual matches, not warranted premises; excerpts may omit qualifiers. Closest supplied object [RT-OBJ-docs-grep](runtime.md#rt-obj-docs-grep) is static guidance rather than produced search data.

> print(f"[{kinds}/{len(keywords)} keywords, {hits} hits] {rel}")
> --- `skills/docs-grep/scripts/docs_search.py`

#### EPI-OBJ-answer
Label: requested answer
Part of: [RT-RTE-knowledge-search](runtime.md#rt-rte-knowledge-search)

Natural-language answer with relative-path citations requested in the host session, not a persisted answer instance. Substrate: external host conversation, unspecified retention. This is the output part of the supplied route rather than the static [RT-OBJ-docs-grep](runtime.md#rt-obj-docs-grep). SRC-1 `skills/docs-grep/SKILL.md`, doctrine/design; supporting passage is retained below in the answer route. No supplied answer artifact establishes produced content.

### Routes

#### EPI-RTE-keyword-ranking
Label: lexical match evaluation
Part of: [RT-RTE-knowledge-search](runtime.md#rt-rte-knowledge-search)

Endpoints: CLI keywords/current readable corpus → match statistics and sorted results. Owner: Python code. Context/state: lowercased strings, per-file distinct set and line-entry count. Check target: lexical overlap between query strings and file lines; domain: readable recursive lowercase-matched Markdown, not proposition truth. This separates evaluation from the output transformation part of the supplied route.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: ordered in-memory result tuples for preview emission.
- Later read-back: inapplicable — scoring retains no changed material for later invocation.
- Delegated visibility: inapplicable — no separate model worker.
- Selection predicate: nonblank keyword arguments and readable `*.md`; any substring hit admits a file; descending distinct matches then line-entry hits then path.
- Invalidation or expiry: all scores rebuilt each invocation.
- Activation or effect: determines ranking; does not evaluate semantic truth or completeness.
- Evidence limits: source deduction, not executed search or observed answer effect.

SRC-1 `skills/docs-grep/scripts/docs_search.py`, implementation:

> matched = [k for k in lowered if k in low]
> --- `skills/docs-grep/scripts/docs_search.py`

> hit_kinds.update(matched)
>                 total_hits += len(matched)
> --- `skills/docs-grep/scripts/docs_search.py`

> results.sort(key=lambda r: (-r[0], -r[1], str(r[2])))
> --- `skills/docs-grep/scripts/docs_search.py`

Concrete deduction, not target execution: query arguments `widget widget` lower to two identical entries. In the sample line `Creates a widget and returns its id.`, both entries match; that line contributes two hits but one distinct kind. `widget` repeated twice on one line would still contribute only two hits, not four. Other lines accumulate independently. Thus a high count can reflect duplicated arguments rather than independent corroboration. The checked target is text overlap; this countercase prevents treating the score as evidential confidence.

> Creates a widget and returns its id.
> --- `sources/api-reference/sample-api.md`

#### EPI-RTE-preview-output
Label: excerpt and result emission
Part of: [RT-RTE-knowledge-search](runtime.md#rt-rte-knowledge-search)

Endpoints: ranked tuples → stdout relative paths and previews → host. Owner: Python. This is the transformation/selection part of the supplied combined route. SRC-1 `skills/docs-grep/scripts/docs_search.py`, implementation. Output rule: 15 files, two earliest matching lines per file, 100 stripped characters per line. No evaluator of source truth. Current-run result selection is not knowledge acceptance.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: ranked paths, counts, bounded excerpts; zero hits prints a suggestion and returns success.
- Later read-back: inapplicable — no output artifact persisted by script.
- Delegated visibility: inapplicable — stdout returns to invoking host or shell, no model delegation.
- Selection predicate: sorted result prefix; first matching lines, not best supporting passages.
- Invalidation or expiry: transient output; future invocations reread files.
- Activation or effect: code bounds preview delivery; separate full-file host access remains possible.
- Evidence limits: context truncation and ignored decoding errors can lose qualifiers; output does not authenticate corpus identity.

> text = path.read_text(encoding="utf-8", errors="ignore")
> --- `skills/docs-grep/scripts/docs_search.py`

> if len(previews) < PREVIEW_PER_FILE:
>                     previews.append(f"    L{lineno}: {line.strip()[:PREVIEW_WIDTH]}")
> --- `skills/docs-grep/scripts/docs_search.py`

> for kinds, hits, path, previews in results[:TOP_N]:
> --- `skills/docs-grep/scripts/docs_search.py`

For the sample sentence quoted in the ranking record, a match emits that sentence after an `L<line>:` prefix, without changing its proposition. A longer matching line loses its suffix; later qualifiers elsewhere are not emitted merely because the file matched. Direct CLI still performs this transformation without the skill's full-file-read instruction. These source deductions need no runtime fixture.

#### EPI-RTE-weak-retry
Label: weak-hit judgment and retry
Part of: [RT-RTE-knowledge-search](runtime.md#rt-rte-knowledge-search)

Endpoints: hits → host judgment → revised keywords and another search if weak. Owner/proposer/decider: model under skill guidance; no explicit human approval/veto or expected-answer oracle. Domain: apparent hit usefulness for the user's open question. Operating mode: open lookup, no fixed experiment or improvement objective. This is the evaluative part of the supplied route, distinct from answer generation. SRC-1 `skills/docs-grep/SKILL.md`, doctrine/design; passage retained in the next record.

- implementation conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: possible revised keywords and repeat search, not a structured verdict.
- Later read-back: inapplicable — no persistent judgment or revised search policy is prescribed.
- Delegated visibility: inapplicable — no separate evaluator agent specified.
- Selection predicate: host considers hits weak; no threshold or independent reference answer defined.
- Invalidation or expiry: judgment concerns current question; no stored acceptance to revoke.
- Activation or effect: advisory request to continue lookup, no enforced retry.
- Evidence limits: actual critique, changed reliance and improved answers not observed; corpus consultation is not an answer oracle.

#### EPI-RTE-answer-synthesis
Label: source-based host answer
Part of: [RT-RTE-knowledge-search](runtime.md#rt-rte-knowledge-search)

Endpoints: selected files and question → requested cited answer. Owner/proposer: host model; user receives answer without a prescribed acceptance decision. Context: full files are requested beyond previews. No output validator, expected answer or approval criterion is defined in this prompt. Operating mode: open question. This is the answer-producing part of the supplied route, not the whole lookup procedure. SRC-1 `skills/docs-grep/SKILL.md`, doctrine/design.

- implementation conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: requested answer citing relative file paths.
- Later read-back: uninspected — host retention is external and no repository answer-write route is prescribed.
- Delegated visibility: inapplicable — no separate synthesis worker specified.
- Selection predicate: read top-ranked files; exact file count and evidence sufficiency left to host.
- Invalidation or expiry: uninspected — no answer retraction or expiry protocol supplied.
- Activation or effect: source reliance and citations requested, not enforced or observed.
- Evidence limits: no actual answer licenses classification as paraphrase, derivation or conjecture; no evidence-consuming acceptance established.

> Read the top-ranked files and answer the question. Cite the relative paths of the files you used. If the hits look weak, adjust the keywords and repeat Step 2.
> --- `skills/docs-grep/SKILL.md`

### Claims

#### EPI-CLM-repository-rag
Label: repository-shaped retrieval and answer

Distinct from [RT-CLM-machine-distribution](runtime.md#rt-clm-machine-distribution): this claim concerns retrieval and synthesis, not installation reach. SRC-1 `README.md`, doctrine/design, describes searchable knowledge without vector DB/server and an answer synthesized from top hits. It does not itself claim fact verification or accepted novel knowledge.

> - Knowledge (`sources/`) is searchable from any project via the bundled `/docs-grep` skill — a "repository-shaped RAG" with no vector DB and no server
> --- `README.md`

> | `/docs-grep` | Multi-keyword search over `sources/`, ranked by relevance, with an answer synthesized from the top hits |
> --- `README.md`
