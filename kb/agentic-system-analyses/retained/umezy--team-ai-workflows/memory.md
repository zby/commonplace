---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "team-ai-workflows memory: repository-authored Markdown, mutable skill exposure and request-driven lexical read-back."
run-id: AAS-2026-11-09-team-ai-workflows-c00fb85f7ed1-01
source-identity: https://github.com/umezy/team-ai-workflows
reviewed-boundary: "9aebd7a6c2803da450904eb5621ae5439508ff94"
---

# team-ai-workflows memory report

## Boundary and evidence

The memory boundary includes the retained `sources/` corpus, repository skill instructions, user-level skill links, root-selection configuration, the setup/update scripts, and the search-to-answer procedure. It follows the whole-system boundary in [boundary](boundary.md#boundary-and-evidence). Claude Code's internal context lifecycle, model parameters and deployed user state are outside the frozen evidence. Demonstration media and external articles remain excluded. This prevents conclusions about actual host discovery, session compaction, compliance, installation success or answer improvement.

Direct inspection covered SRC-1 at commit `9aebd7a6c2803da450904eb5621ae5439508ff94`: `README.md`, both skill files, the synchronizer, hook, search program and all three corpus files. These provide implementation and doctrine/design, not observed operation. The supplied runtime was compared against these files rather than used as an inspection limit. The tracked tree and clean checkout identity were checked directly. No target program was executed.

| Entry point or operation | Directly inspected SRC-1 paths | Record coverage and limits |
|---|---|---|
| Knowledge acquisition and editing | `README.md`; `sources/api-reference/sample-api.md`; `sources/documentation/getting-started.md`; `sources/tips/writing-knowledge.md` | [MEM-OBJ-sources](#mem-obj-sources), annotation on [RT-RTE-repository-admission](runtime.md#rt-rte-repository-admission); actual team review and deployment unknown |
| Initial setup, settings and hook installation | `.claude/skills/team-setup/SKILL.md` | [MEM-OBJ-team-workflows-dir](#mem-obj-team-workflows-dir); [RT-RTE-machine-setup](runtime.md#rt-rte-machine-setup); model-executed instructions, not enforced writes |
| Manual synchronization and merge hook | `.claude/skills/team-setup/scripts/sync_user_skills.sh`; `.claude/skills/team-setup/scripts/post-merge` | [RT-RTE-skill-sync](runtime.md#rt-rte-skill-sync), [RT-OBJ-skill-links](runtime.md#rt-obj-skill-links); cleanup is link maintenance, not corpus curation |
| Skill-mediated query, full-file reading and retry | `skills/docs-grep/SKILL.md` | [RT-OBJ-docs-grep](runtime.md#rt-obj-docs-grep), [RT-RTE-knowledge-search](runtime.md#rt-rte-knowledge-search), [MEM-BAP-corpus-answer](#mem-bap-corpus-answer); host compliance unobserved |
| Direct CLI, alternate configured root and fallback root | `skills/docs-grep/scripts/docs_search.py` | [MEM-OBJ-search-results](#mem-obj-search-results), [MEM-OBJ-team-workflows-dir](#mem-obj-team-workflows-dir), annotation on [RT-RTE-knowledge-search](runtime.md#rt-rte-knowledge-search); direct callers bypass answer instructions |
| Trace-fed updates, evaluation, rejection and withdrawal | All preceding implementation files and authoring instructions | [MEM-ABS-trace-update](#mem-abs-trace-update); manual replacement is afforded, semantic maintenance and exercised rejection unestablished |
| Host context management | Host dependency declared in `README.md`; procedure in `skills/docs-grep/SKILL.md` | [RT-CMP-claude-code](runtime.md#rt-cmp-claude-code); no supplied host internals, so no conclusion about host eviction, isolation, summaries or reload guarantees |

## Core ideas

The durable knowledge is ordinary repository Markdown. Search derives temporary access summaries, not a second durable memory store. Repository edits can reach later questions, but the search path does not itself learn from questions, answers or failures. [MEM-OBJ-sources](#mem-obj-sources), [MEM-OBJ-search-results](#mem-obj-search-results) and [MEM-ABS-trace-update](#mem-abs-trace-update) separate these roles.

Two selectors operate in sequence: the model is asked to derive keywords, then Python ranks whole files by lowercase substring matching. Previews expose only early matching lines. A subsequent model-side full-file read is requested, so previews are neither complete documents nor a proven account of the eventual answer context. The configured root can replace the checkout corpus without identity verification. These are selection and trust limits, not evidence that a different corpus was actually used; see the annotation on [RT-RTE-knowledge-search](runtime.md#rt-rte-knowledge-search).

Skill links and the environment value are access metadata, not knowledge payloads. Links expose mutable checkout instructions rather than copying or pinning them. Their later consumer is the host loader, whereas the corpus consumer is the answer-producing model. Knowledge advice and executable instructions therefore have different authority paths even though Git distributes both. See [RT-BAP-user-skills](runtime.md#rt-bap-user-skills) and [MEM-BAP-corpus-answer](#mem-bap-corpus-answer).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-sources
Label: sources Markdown corpus

Source-native identity: `sources/`, containing the sample API reference, getting-started instructions and writing tips. Storage substrate: Git-tracked files in the local checkout; the search can instead read another configured root's `sources/`. Representational form: natural-language knowledge, including code-like API names interpreted as reference content, not executed by search. Lineage: shipped illustrative content, explicitly intended to be replaced by team documentation copies, API references and first-hand tips. The real provenance and admission history of adopter content are uninspected. Evidence: SRC-1, `README.md`, `sources/api-reference/sample-api.md`, `sources/documentation/getting-started.md`, `sources/tips/writing-knowledge.md`, doctrine/design.

Distinct identity: this is the knowledge payload admitted through [RT-RTE-repository-admission](runtime.md#rt-rte-repository-admission) and read by [RT-RTE-knowledge-search](runtime.md#rt-rte-knowledge-search), not either route, the skill instruction object, or the link metadata. No supplied object declares this payload.

> Replace the samples in `sources/` with your team's knowledge (docs copies, API references, first-hand tips)
> --- `README.md`

> Sample knowledge for the search demo. Replace with your SDK's real API reference.
> --- `sources/api-reference/sample-api.md`

The corpus can preserve practical reasons, not merely commands: the API sample explains that calling before readiness silently returns null; the writing tips connect file focus to whole-file ranking. These are authored examples, not automatically derived experience or validated claims about a deployed SDK.

> - One topic per file — the search ranks whole files, so focused files rank cleanly
> --- `sources/tips/writing-knowledge.md`

Consumers: Python reads text to rank and preview it; the host is instructed to read selected files for answers. The former uses fixed lexical rules; the latter grants informational relevance, not a repository-enforced instruction precedence or truth guarantee. See [MEM-BAP-corpus-answer](#mem-bap-corpus-answer).

#### MEM-OBJ-team-workflows-dir
Label: TEAM_WORKFLOWS_DIR root configuration

Source-native identity: `env.TEAM_WORKFLOWS_DIR` requested in `~/.claude/settings.json`, then `TEAM_WORKFLOWS_DIR` read by Python. Representational form: symbolic filesystem-location string. Storage substrate: host settings file when setup is followed, then process environment; actual installed value uninspected. Lineage: setup instructs the host to resolve the repository root and write its absolute path while preserving other settings. Evidence: SRC-1, `.claude/skills/team-setup/SKILL.md`, doctrine/design, and `skills/docs-grep/scripts/docs_search.py`, implementation.

Distinct identity: a configuration payload produced by [RT-RTE-machine-setup](runtime.md#rt-rte-machine-setup), not the setup route or [RT-OBJ-skill-links](runtime.md#rt-obj-skill-links). It selects the knowledge location, not a specific relevant document or corpus version.

> Add to the `env` block of `~/.claude/settings.json` (always preserve every existing key when writing the file back):
> --- `.claude/skills/team-setup/SKILL.md`

> env = os.environ.get("TEAM_WORKFLOWS_DIR")
> --- `skills/docs-grep/scripts/docs_search.py`

Python accepts a configured root if its `sources` child is a directory; otherwise it resolves the script's real location. This string has code-consumed routing authority, but provides no trust attestation, content approval or version pinning. Requested setup writes are model-mediated; later manual edits and actual human approval are not evidenced.

#### MEM-OBJ-search-results
Label: Temporary ranked search results

Source-native identity: `results` and per-file `previews` in the search program. Storage substrate: process-local Python objects and stdout; no result-file write is implemented. Representational form: symbolic counts, paths and line locations mixed with natural-language source excerpts. Distinct operative parts: scores/paths guide access; excerpts expose source content. Lineage: readable current corpus files plus caller-supplied keywords; not conversation traces or model-generated summaries. Evidence: SRC-1, `skills/docs-grep/scripts/docs_search.py`, implementation.

Distinct identity: this is the temporary output object of [RT-RTE-knowledge-search](runtime.md#rt-rte-knowledge-search), not a second declaration of the route or the retained [MEM-OBJ-sources](#mem-obj-sources). No supplied object declares it. It is current-run state rather than independently persisted read-back memory.

> TOP_N = 15
> PREVIEW_PER_FILE = 2
> PREVIEW_WIDTH = 100
> --- `skills/docs-grep/scripts/docs_search.py`

> if len(previews) < PREVIEW_PER_FILE:
>                     previews.append(f"    L{lineno}: {line.strip()[:PREVIEW_WIDTH]}")
> --- `skills/docs-grep/scripts/docs_search.py`

The selected excerpts are the first matching lines in source order, not necessarily the highest-value evidence or the strongest match. Counts can reflect matches outside the emitted excerpts. UTF-8 decoding ignores errors, so read text need not preserve all source bytes. The human/model consumer receives at most 15 result entries, two 100-character previews each, scores and relative paths. These are output-size limits, not a token budget for the eventual model context.

### Routes

none declared in this member

### Claims

none declared in this member

### Evidenced absences

#### MEM-ABS-trace-update
Label: No shipped automatic trace-fed knowledge update

- implementation conclusion status: absent

Searched boundary: SRC-1 at the reviewed commit, complete tracked path inventory and direct inspection of `skills/docs-grep/scripts/docs_search.py`, `.claude/skills/team-setup/scripts/sync_user_skills.sh`, `.claude/skills/team-setup/scripts/post-merge`, both skills, `README.md` and all `sources/` text. Inspection question: is any query, answer, execution outcome, feedback or evaluation automatically transformed into retained knowledge/instructions and later read? The complete search entry point only reads corpus files and prints current results; synchronization creates/removes access links; the hook invokes synchronization; authoring instructions describe replacing files. No such trace-to-derived-to-later-consumer update is shipped. This bounded absence does not cover external host logs, opaque provider state or an adopter's additions. It does not negate manual experience-derived content.

Closest supplied records: [RT-RTE-knowledge-search](runtime.md#rt-rte-knowledge-search) and [RT-RTE-repository-admission](runtime.md#rt-rte-repository-admission). This is a distinct bounded absence, not a replacement for either positive route.

> text = path.read_text(encoding="utf-8", errors="ignore")
> --- `skills/docs-grep/scripts/docs_search.py`

> for pv in previews:
>             print(pv)
>     return 0
> --- `skills/docs-grep/scripts/docs_search.py`

The conclusion rests on the inspected complete programs and workflow, not on those read/print excerpts alone. No shipped evaluator, compactor, summary checkpoint writer or automatic semantic withdrawal path appears in that inspected boundary. Consequently, automatic trace learning and durable trace-derived memory are not established by this template.

### Behavioral-authority paths

#### MEM-BAP-corpus-answer
Label: Corpus content to answer synthesis

Consumer: external Claude Code model answering the user's question. Channel: keyword-ranked previews from Python, followed by the requested full-file reads. Force: informational material for synthesis and a citation instruction; no supplied mechanism makes corpus content verified truth or establishes priority against host instructions. Horizon: later questions/sessions can read changed repository knowledge, contingent on deployed access; actual exposure and behavioral activation are unobserved. Evidence: SRC-1, `skills/docs-grep/SKILL.md`, doctrine/design, and `skills/docs-grep/scripts/docs_search.py`, implementation.

Distinct identity: unlike [RT-BAP-user-skills](runtime.md#rt-bap-user-skills), whose payload is procedural skill text, this path carries retrieved knowledge. The common host does not make the payloads or authority identical. It is the knowledge-consumption portion of [RT-RTE-knowledge-search](runtime.md#rt-rte-knowledge-search), not a duplicate route.

> Read the top-ranked files and answer the question. Cite the relative paths of the files you used. If the hits look weak, adjust the keywords and repeat Step 2.
> --- `skills/docs-grep/SKILL.md`

The instruction establishes an intended later consumer and an afforded read-back path. It does not prove full-file reading, correct use, citation accuracy or improved capacity. Reasons preserved in corpus prose can be delivered by full-file reading; the preview selector does not guarantee their inclusion.

## Annotations

#### On [RT-OBJ-skill-links](runtime.md#rt-obj-skill-links)

Memory-specific distinction: links retain access metadata, not copies of knowledge or instruction bodies. Their referents remain mutable. Content edits inside an already-linked directory require no new link admission; directory deletion can leave an unreachable link until synchronization. Shell cleanup tests reachability, not semantic staleness, truth, content ownership or approval. SRC-1, `.claude/skills/team-setup/scripts/sync_user_skills.sh`, implementation; supporting passages are in the supplied record and [RT-RTE-skill-sync](runtime.md#rt-rte-skill-sync).

#### On [RT-OBJ-docs-grep](runtime.md#rt-obj-docs-grep)

Lineage: shipped authored procedure rather than learned interaction memory. Later consumer: the host interprets it after skill discovery. It selects working context by instructing query expansion, bounded search previews and further file reads. It has no explicit context-token budget, history trimming, isolated subagent frame or model summary checkpoint in its procedure. These scoped properties follow direct inspection of SRC-1, `skills/docs-grep/SKILL.md`; the supplied record preserves the load-bearing instructions. Host-side context operations remain outside the evidence.

#### On [RT-RTE-repository-admission](runtime.md#rt-rte-repository-admission)

Admission control: the README delegates content replacement to the team/adopter, so human authoring/editing is the documented path. Actual commit authorship, merge approval, veto and review rules are unresolved. Starting setup or pulling does not establish human approval of each content item. No model/program evaluator admits corpus edits in the shipped implementation. Physical file/Git writes are separate from approval. SRC-1, `README.md`; its replacement passage is retained in [MEM-OBJ-sources](#mem-obj-sources).

Curation guidance favors focused files, conclusions and symptom-cause-fix statements. It supplies reasons for retrievability, but does not implement rewriting, claim evaluation, extraction from traces or deduplication. A first-hand tip can have experiential lineage without an automatic trace-fed update. Later readers may receive retained reasons through full-file reads, not through a separately indexed rationale field. SRC-1, `sources/tips/writing-knowledge.md`:

> - Write pitfalls as "symptom -> cause -> fix", because people search by the symptom's wording
> --- `sources/tips/writing-knowledge.md`

#### On [RT-RTE-machine-setup](runtime.md#rt-rte-machine-setup)

Retained outputs relevant to later consumers are links, hook and configuration, not a knowledge summary. The configuration chooses a root; the hook schedules link maintenance after merges. Confirmation instructions concern hook/personal-skill collisions, not per-document knowledge admission. SRC-1, `.claude/skills/team-setup/SKILL.md`; supplied setup passages preserve the confirmation and settings instructions. No separate model worker or retained worker return is specified.

#### On [RT-RTE-skill-sync](runtime.md#rt-rte-skill-sync)

Maintenance affects reachability, not knowledge meaning. Cleanup removes broken links and keeps valid existing entries; it does not inspect instruction content. Merge-triggered synchronization can expose newly added skill directories, while edits to existing linked content already change what later consumers can access. The hook neither selects nor summarizes knowledge. SRC-1, `.claude/skills/team-setup/scripts/sync_user_skills.sh`, `.claude/skills/team-setup/scripts/post-merge`; load-bearing code is retained in the supplied route. Actual host reload timing and cached instruction invalidation are uninspected.

#### On [RT-RTE-knowledge-search](runtime.md#rt-rte-knowledge-search)

Read-back direction: request-driven. A user question prompts model keyword generation; a CLI call selects corpus content; stdout delivers previews; the host is asked to open full files. This is not independent unsolicited memory injection. Direct CLI callers supply their own keywords and have no enforced answer-generation stage. Storage capability and the documented host consumer must not be conflated with observed reading.

Selection uses lowercase substring matches in all Markdown lines, including quoted content or metadata if present. Distinct keyword count wins before aggregate matched keyword-line entries and path order. A repeated occurrence on the same line does not multiply that keyword's contribution, while duplicate arguments can inflate counts. File timestamps, authorship, first-hand provenance and trust labels are not ranking inputs. SRC-1, `skills/docs-grep/scripts/docs_search.py`:

> matched = [k for k in lowered if k in low]
>             if matched:
>                 hit_kinds.update(matched)
>                 total_hits += len(matched)
> --- `skills/docs-grep/scripts/docs_search.py`

The root branch qualifies corpus identity: any configured root with a `sources` directory wins, rather than only this repository's clone. Invalid configuration falls back to the script's resolved location. No-match returns a suggestion without writing knowledge or retrying; an unreadable file is skipped, not semantically rejected. The supplied route retains the branch and ordering passages; [MEM-OBJ-search-results](#mem-obj-search-results) retains the preview transformation. Current results are rebuilt rather than cached. Full-file selection count and token budget are unspecified.

## Write side

Acquisition is documented repository replacement with documentation copies, API references and first-hand tips, not an ingestion pipeline. The initial samples and authoring tips are source-authored. Their actual use as team experience is not observed. The admission annotation on [RT-RTE-repository-admission](runtime.md#rt-rte-repository-admission) separates human content choice, unresolved merge governance and physical distribution.

Subsequent content changes can reach later consumers through mutable links or search reads without a separate semantic approval gate in these programs. This includes instructions and scripts as well as knowledge; the distinct authority paths are [RT-BAP-user-skills](runtime.md#rt-bap-user-skills) and [MEM-BAP-corpus-answer](#mem-bap-corpus-answer). The environment selector is another admission surface for which corpus gets searched, but its acceptance test is directory existence, not content trust.

Maintenance/rejection is mechanical at installation: existing entries block replacement; explicit setup conflicts request human decisions; broken-link cleanup removes unreachable access references. It does not retract claims already delivered to a host context. Corpus withdrawal is afforded by deleting or editing files; a later fresh search sees the changed tree, but no shipped operation retracts earlier tool output or host answers. No TTL, knowledge deprecation state, semantic evaluator, learned summary store or automatic trace-derived checkpoint is implemented in the inspected programs. See [MEM-ABS-trace-update](#mem-abs-trace-update). Manual authoring can preserve reasons and causal explanations; search's excerpts may omit them.

## Read-back

The retained corpus supplies later invocations through [RT-RTE-knowledge-search](runtime.md#rt-rte-knowledge-search). Trigger: explicit question/CLI keywords. Producer/selector: model query expansion followed by Python ranking. Retained input: current configured or fallback corpus. Persistence: files persist, query/results do not persist through this program. Delivery: stdout previews and requested host full-file reads. Later consumer: answer-producing host model. Budget: 15 paths and two 100-character previews per path, not a full-context cap. Status: wired search selection, claimed model workflow, operation uninspected, as recorded in that route.

Skill instruction exposure follows links into the live checkout and depends on external discovery. The hook is an automatic update trigger for access metadata, not an unsolicited knowledge-push selector. `TEAM_WORKFLOWS_DIR` persists location selection if setup completes, not relevance selection. These paths retain neither episode summaries nor extracted conversation facts.

Working-context control is limited to search-output filtering and requested demand-loading. Ranking leaves nonselected corpus files outside the emitted result set; previews leave most document content outside it; the skill requests reading top files and re-querying weak hits. The rest of the corpus remains filesystem-reachable, with no special reload token or pointer resolution beyond paths and ordinary file access. There is no shipped isolated worker frame whose whole context is popped, no summarized conversation tail, and no explicit eviction operation. External host behavior could add these, but is not inspected. This mechanism resembles selective external-file loading, not stack-frame isolation; path metadata does not make model-window text a live reference to the repository.

## Integration issues

No corrections to supplied runtime facts and no possible duplicate declarations were found. New objects separate corpus payload, configuration metadata and ephemeral search output from the supplied routes and skill-link object. The new authority path separates knowledge delivery from procedural skill delivery. Existing referents receive annotations rather than redeclarations.

Unresolved integration limits remain:

- Actual corpus write approval, author identity and rollback practice are not supplied. This prevents a claim of enforced human review for [RT-RTE-repository-admission](runtime.md#rt-rte-repository-admission), despite documented human customization. SRC-1, `README.md`.
- Host full-file path resolution, reading compliance, instruction precedence and context retention are external. This prevents a complete model-visible context or activation claim for [MEM-BAP-corpus-answer](#mem-bap-corpus-answer) and [RT-RTE-knowledge-search](runtime.md#rt-rte-knowledge-search). SRC-1, `skills/docs-grep/SKILL.md`.
- Actual environment and installed link state are absent from the evidence, so the deployed corpus identity and skill version cannot be inferred from the frozen template. This concerns [MEM-OBJ-team-workflows-dir](#mem-obj-team-workflows-dir) and [RT-OBJ-skill-links](runtime.md#rt-obj-skill-links). SRC-1, `skills/docs-grep/scripts/docs_search.py`, `.claude/skills/team-setup/scripts/sync_user_skills.sh`.

These are bounded unknowns, not conflicting records or requests to extend the evidence boundary.

## Limitations and checks

Source identity was rechecked with Git: HEAD equals the full reviewed boundary and the checkout had no reported changes. The tracked inventory accounts for both shipped command entry points and the merge hook; no registered tool service or library API adds another memory route in that tree. All consequential source reads remained within SRC-1. The governing job, member types, worker rules and record contract were read completely; no authoring skill, prior analysis, external article, target execution or agent delegation was used.

The result establishes source-level persistence, access, selectors and requested consumption. It does not establish actual deployment, host context management, behavioral activation, learning benefit or successful improvement. Deterministic validation: passed the required `commonplace-validate` role-memory check. This establishes structural and quotation checks, not semantic correctness or job acceptance.
