---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "WikiSkill memory: journal-backed lessons, retained skills, research trace selection and paper-role alternatives."
run-id: AAS-2026-10-15-wikiskill-baafad05d35e-01
source-identity: https://github.com/Stahl-G/WikiSkill
reviewed-boundary: da6984caca09d5f81b2336cf3067b59c0c18bb1e
---

# WikiSkill memory report

## Boundary and evidence

The subject is WikiSkill's shipped experience-to-Wiki-to-skill system at SRC-1, commit `da6984caca09d5f81b2336cf3067b59c0c18bb1e`. Scope follows [the boundary](boundary.md): product CLI/MCP, native handoffs, feedback-first API, legacy research evolution, paper-role library adapters, isolated Spreadsheet study, inheritance and skill installation. Implementation and source-authored instructions establish wiring and requested behavior, not an observed learning run. No target code, test, example, provider or experiment was executed.

The supplied [runtime account](runtime.md#runtime-account) supplies route identities and model components. Direct reads below extend and test that account. The Source register remains [boundary's register](boundary.md#source-register); every source reference here is SRC-1. External model state, host context management and host discovery are outside the frozen implementation. User corpora are task inputs, not evidence of experience-derived memory. Bundled research results, contributor instructions and tests were not used as operation evidence. Uninspected domain-specific scoring and runtime internals prevent complete evaluator-validity or sandbox conclusions, not the traced memory-account conclusions.

| Entry point or operation | Directly inspected source paths (SRC-1) | Coverage and limits |
|---|---|---|
| Product dispatch and wrappers | `src/wikiskill/cli.py`, searched `src/wikiskill/product_cli.py`, `src/wikiskill/mcp_server.py` | Direct CLI/MCP APIs reach the same product writes; MCP text staging is temporary, not a separate knowledge store. [RT-RTE-product-round](runtime.md#rt-rte-product-round), annotations below. No lifecycle hook was assumed from the presence of tools. |
| Hook entry-point check | Bounded case-insensitive `hook` text search under `src/` and `skills/` in Python, Markdown, JSON, TOML and YAML; direct header read of `src/wikiskill/isolated/runtime.py` | The sole hit is `hooks` in isolated runtime's DISABLE tuple. No additional hook-triggered memory route was established by this search. This does not characterize external host hooks or mechanisms without that spelling. |
| Initialization, replay, inheritance and learning | `src/wikiskill/product.py` | Direct `_load`, `start`, `_context`, `next_work`, `record`, `learn`, `propose`, `feedback`, `export`; [MEM-OBJ-patterns](#mem-obj-patterns), [MEM-OBJ-feedback](#mem-obj-feedback), [MEM-OBJ-skill](#mem-obj-skill), [MEM-OBJ-experience](#mem-obj-experience). |
| Native selection and collection | `src/wikiskill/native_agents.py`, `src/wikiskill/resources/product/roles/maintainer.md`, `src/wikiskill/resources/product/roles/proposer.md` | Direct staging, aggregation omissions, retry reuse and role guidance; [RT-RTE-native-handoff](runtime.md#rt-rte-native-handoff). Host's actual fresh context remains uninspected. |
| Feedback admission | `src/wikiskill/feedback_loop.py` | Direct `begin`, `finish`, `skip`, `work`; [RT-RTE-feedback-gate](runtime.md#rt-rte-feedback-gate). Source of submitted verdicts and human declarations is not authenticated. |
| Research initialization, checkpointing, acceptance | `src/wikiskill/engine.py`, `src/wikiskill/wiki.py` | Direct initialization, batch, evolve, state and impact serialization/read; [MEM-OBJ-research-wiki](#mem-obj-research-wiki), [MEM-OBJ-skill-impact](#mem-obj-skill-impact). Custom adapter initialization remains caller-controlled. |
| Default research maintenance/proposal | `src/wikiskill/officeqa/wiki_agents.py`, `src/wikiskill/wiki_maintainer.py`, `src/wikiskill/skill_proposer.py`, `src/wikiskill/resources/officeqa/wiki/prompts/maintainer.md`, `src/wikiskill/resources/officeqa/wiki/prompts/proposer.md` | Direct sample, compaction, staged read-back, edit and proposal checks; [MEM-OBJ-research-evidence](#mem-obj-research-evidence). Other domain prompt bodies were inventoried, not inspected: their exact requested procedures remain uninspected. |
| Domain execution delivery | Searched `src/wikiskill/officeqa/rollout.py`, `src/wikiskill/spreadsheet/rollout.py`, `src/wikiskill/livemath/rollout.py`, `src/wikiskill/sealqa/rollout.py`, `src/wikiskill/alfworld/rollout.py` | `build_prompt`/`skill_text` hits corroborate injection on those paths, not full adapter inspection. [RT-BAP-skill-consumption](runtime.md#rt-bap-skill-consumption) remains the supplied delivery finding; OfficeQA retrieval-specific implementation and domain evaluator validity were not independently traced here. |
| Alternative paper library | `src/wikiskill/paper_alignment/agents.py`, `src/wikiskill/paper_alignment/contracts.py`, `src/wikiskill/paper_alignment/evidence.py`, `src/wikiskill/resources/paper_alignment/prompts/proposer.paper.md` | Direct callable factories, payloads, local patches and purpose mapping; [MEM-RTE-paper-adapters](#mem-rte-paper-adapters). Injected invocation transport is unspecified by the library; no default CLI wiring inferred. |
| Isolated study | `src/wikiskill/spreadsheet/study.py`, `src/wikiskill/isolated/tools_server.py`, paper contracts/evidence above | Direct prepare, feedback paging, learning, finish/read tool and final freeze. [RT-RTE-isolated-study](runtime.md#rt-rte-isolated-study), [MEM-OBJ-paper-skills](#mem-obj-paper-skills). Runtime sandbox implementation is supplied-runtime evidence, not independently verified operation. |
| Export, installation, restoration | `src/wikiskill/product.py`, `src/wikiskill/product_install.py`, native asset installation in `src/wikiskill/native_agents.py` | Direct retained-file selection, backup and withdrawal; [RT-RTE-skill-install](runtime.md#rt-rte-skill-install). Host reload and later use remain external. |
| Result display, preflight, bundled evaluations | CLI/MCP registrations above; supplied runtime/boundary coverage | Display/verification consumers, not established learning writers here. `src/wikiskill/product_views.py`, result bundles and evaluation scripts not inspected in this job; no conclusion that their summaries preserve complete provenance or prove benefit. |

## Core ideas

1. **Knowledge admission and skill adoption are different decisions.** Product `learn` admits named lessons before proposal evaluation. Rejection changes neither those lessons nor their original feedback. Research likewise updates Wiki before gating a candidate. Later authors receive rejected-attempt history, while task executors receive a selected skill, not the Wiki. See [MEM-OBJ-patterns](#mem-obj-patterns), [MEM-OBJ-research-wiki](#mem-obj-research-wiki), [RT-RTE-product-round](runtime.md#rt-rte-product-round).
2. **Persistent evidence is not identical to displayed context.** Native learning omits candidate bodies from aggregate gate history. Default research Proposer sees a shortened impact rendering plus readable staged files; Maintainer sees the full Wiki snapshot. Raw traces are sampled, tailed or middle-trimmed before inclusion. The budgets and escape hatches differ by route; none establishes lossless context. See [MEM-OBJ-skill-impact](#mem-obj-skill-impact), [MEM-OBJ-research-evidence](#mem-obj-research-evidence).
3. **Source links constrain admissibility, not truth.** Product source membership and research schema/path checks regulate accepted submissions. They do not establish that a lesson follows from its sources. Human-origin metadata does not authenticate a human. Roles request reusable explanations and counterexamples, but actual content-directed reasoning and future benefit remain uninspected. See [MEM-OBJ-patterns](#mem-obj-patterns), [MEM-OBJ-feedback](#mem-obj-feedback).
4. **Context separation is an explicit delivery frame.** Native handoffs request a fresh child with task/skill or learning context and return a result pointer. Isolated research gives learning roles staged reads and structured submission. The former is host protocol; the latter has additional runtime controls described by the supplied runtime. Neither file pointers nor an isolated frame imply that excluded material is inaccessible to every host tool. See [RT-RTE-native-handoff](runtime.md#rt-rte-native-handoff), [RT-RTE-isolated-study](runtime.md#rt-rte-isolated-study).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-patterns
Label: Product Wiki patterns
Part of: [RT-OBJ-product-journal](runtime.md#rt-obj-product-journal)

The part is the name-keyed `patterns` content in committed `wiki` events and replayed state, not the whole event chain. Natural-language lessons are wrapped in symbolic name/source-ID mappings. Local event JSON and immutable submissions preserve past versions; `_wiki_view` regenerates Markdown pages using hashed names and an index. Editing those pages is not the inspected admission mechanism: learning contexts use replayed state, not those page bytes. Identity differs from the container's sequencing/integrity metadata (SRC-1, `src/wikiskill/product.py`).

> s['patterns'].update(value['patterns']);s['requests'][value['request_id']].update(status='complete',submission=value['submission']);s['phase']='proposer'
> --- `src/wikiskill/product.py`

`learn` permits current-round completed train request IDs, original feedback IDs and existing pattern source IDs. This qualifies the error message's narrower training/feedback wording and the supplied route's shorter description. Existing-pattern citations allow lesson-to-lesson lineage. It validates nonblank name/content and nonempty permitted sources, not semantic entailment. No per-pattern human approval is required; model Maintainer is the intended author, but a generic caller can submit the file. Reusing a name replaces its current value; an empty list does not delete existing patterns. Old event versions remain recoverable by journal inspection; current context selects the latest mapping.

> context=read(root/req['context_file']);allowed={x['source_id'] for x in context['training_records']}|{x['id'] for x in context['human_feedback']}|{x['source_id'] for x in context['wiki'].values()}
> --- `src/wikiskill/product.py`

Later Maintainer/Proposer contexts receive all current patterns, with generated source IDs. They are evidence and reusable procedural suggestions for those authors, not executable controller rules. Task executors receive the resulting skill instead. Direct derivation from a supplied trace is possible, but optional trace submission means pattern provenance can also be outputs/scores/feedback without execution trajectories. No inference of universal trace origin or improvement follows.

#### MEM-OBJ-feedback
Label: Product original feedback
Part of: [RT-OBJ-product-journal](runtime.md#rt-obj-product-journal)

The distinct part is original feedback records and their text, IDs, source/origin/intent fields and file references. Natural-language feedback is copied to local Markdown; symbolic metadata in the journal governs selection. `feedback` accepts any nonblank caller text. Feedback-first `begin` additionally accepts declarations of explicit human requirement and requires origin `human` plus source identity. Neither entry authenticates the person; admission is caller-supplied content under software checks. Patterns derived from it have separate identity and revision behavior (SRC-1, `src/wikiskill/product.py`, `src/wikiskill/feedback_loop.py`).

> if not set(sources)<=allowed:raise ValueError('Explicit requirement source is not recorded human intent')
> --- `src/wikiskill/feedback_loop.py`

All original notes enter later learning context and may be copied by workspace inheritance. Explicit requirements receive requested design-constraint force at the model author; source IDs also enter symbolic requirement-check selection at `finish`. Fulfillment and evidence strings remain caller judgments. Requirements do not become verified truths merely by admission. Ordinary product `feedback` labels origin `user_feedback`; it does not itself create the explicit-intent record shape. Raw notes survive lesson replacement, candidate rejection and cross-workspace copying.

#### MEM-OBJ-skill
Label: Candidate and retained SKILL text

Local UTF-8 files hold natural-language instructions; journal/configuration pointers and hashes are symbolic access/adoption metadata, not the instruction content. Initial bytes come from a caller file or prior workspace. Product proposals copy whole nonempty files plus a separate note. Research accepted text goes to `skills/iteration-*.md`; rejected text remains in proposal artifacts, not the incumbent path. These files are distinct from [RT-OBJ-product-journal](runtime.md#rt-obj-product-journal), although that journal records product adoption; [RT-BAP-skill-consumption](runtime.md#rt-bap-skill-consumption) describes their behavioral channel (SRC-1, `src/wikiskill/product.py`, `src/wikiskill/engine.py`).

> if not Path(skill).read_text(encoding='utf-8').strip():raise ValueError('Skill must not be empty')
> --- `src/wikiskill/product.py`

Product's guidance requests applicability, exclusions and supporting counterexamples; the actual text validator does not require those features. Computational authorship is intended, not authenticated. Software gates adoption using supplied scores or pair verdicts; callers select initial content and may withhold a submission. No universal per-content human approval applies. The selected full body or file pointer reaches later task invocation, including unretained candidate validation. Scope is rounds, explicitly inherited workspaces, or afforded later host sessions after installation. Source reasons can remain in note/Wiki/history, but delivery of SKILL alone does not ensure those reasons accompany it. Actual dependent task decisions and learning benefit remain uninspected.

#### MEM-OBJ-experience
Label: Product retained task evidence

Distinct from the journal's integrity metadata, task output files and optional `trace.txt` copies are local retained evidence payloads. Output format can be opaque binary; it is not necessarily natural-language memory. Optional traces are caller-provided text, with unverified completeness/origin. JSON result rows contain symbolic scores, request identity, hashes and pointers alongside natural-language feedback. These raw records are not already derived lessons; their behavioral influence is through later authors' interpretation (SRC-1, `src/wikiskill/product.py`).

> if trace:
>     trace_record,t=_store_file(root,trace,'trace.txt');files.append(t)
> --- `src/wikiskill/product.py`

Only completed current-round train results enter `_context`, with the full training task. Native staging converts pointers to absolute paths. Validation outputs remain retained but do not enter that training-record selection. Acquisition is generic caller submission or external scorer output; finite-number/type checks admit results, not truthful grading. Infrastructure failure preserves output separately for retry; successful retry can reuse that output without fresh execution. The later Maintainer can transform selected evidence into [MEM-OBJ-patterns](#mem-obj-patterns); Proposer receives the training evidence too. Raw archival retention alone is not a demonstrated trace-fed update.

#### MEM-OBJ-research-wiki
Label: Research Wiki pages

Distinct from product's journal-backed patterns, research Wiki is a local Markdown tree copied from a domain template by `engine.initialize`; optional caller prompt overrides are separately hash-bound. Natural-language pattern content and narratives are read as guidance/evidence. Index locators are access structure, not learned conclusions. `wiki_snapshot` reads Markdown recursively except paths containing `prompts`; fixed prompt bodies are control inputs rather than learned state (SRC-1, `src/wikiskill/engine.py`, `src/wikiskill/wiki.py`).

> if "prompts" in path.parts:
>     continue  # harness-owned prompt files are not loop memory
> --- `src/wikiskill/wiki.py`

Default Maintainer proposes structured creates and full-page updates. Code validates the complete edit list before beginning writes, then renders new evidence/guidance sections, overwrites updated text, regenerates index and appends narrative. The implementation provides pre-write contract validation, not an OS transaction covering I/O failure. New-page evidence references may be empty; path/schema checks do not ensure source support. No per-content human approval is required. Research copies `wiki-before` and uses a completion marker for resume; it does not automatically revert learned pages on skill rejection (SRC-1, `src/wikiskill/wiki_maintainer.py`, `src/wikiskill/engine.py`).

> if not evidence_lines:
>     evidence_lines = ['- (no case references recorded)']
> --- `src/wikiskill/wiki_maintainer.py`

Later default Maintainer gets full snapshot; default Proposer gets index inline, pattern filenames and staged pages on demand, not the narrative log in its staged-copy loop. Paper adapters use different patches and preserve log content. Knowledge has authoring authority, not direct task-tool permission. This object is an input/output of [RT-RTE-research-evolve](runtime.md#rt-rte-research-evolve), not a duplicate route.

#### MEM-OBJ-skill-impact
Label: Research skill-impact history

Local `wiki/skill-impact.md` holds fenced, strictly parsed JSON records projected from gate events. Symbolic fields preserve identities, gate verdicts, scores and adoption; natural-language purpose and diff preserve an intervention account. Full `proposal.json` separately retains rationale and candidate body. This is not the same as the Wiki pattern pages or the product gate history; its closest supplied counterpart is the history described by [RT-RTE-research-evolve](runtime.md#rt-rte-research-evolve) (SRC-1, `src/wikiskill/wiki.py`, `src/wikiskill/engine.py`).

> # Model-facing impact contains accepted and rejected proposals alike.
> --- `src/wikiskill/engine.py`

Engine-generated records include both rejected and accepted changes; model failure to pass the gate does not erase the experiment. Default Maintainer's snapshot includes the full file. Default Proposer parses it, injects only verdict/accepted flag/purpose/motivating pattern names, and stages the full file for further reading. Thus its inline display omits the stored diff, numeric detail and some provenance; availability does not prove those details were read (SRC-1, `src/wikiskill/officeqa/wiki_agents.py`).

> if entry.motivated_by_patterns:
>     lines.append(f"  patterns: {', '.join(entry.motivated_by_patterns)}")
> --- `src/wikiskill/officeqa/wiki_agents.py`

The paper Proposer instruction says the log contains full rejected proposals. That is a source claim, not an invariant of every adapter: default engine history stores a diff rather than the candidate's full text in that file; isolated study starts with an empty impact file and writes final `skill-impact.json` only after proposing/gating. The full legacy proposal remains separately retained. Its causal effect on avoiding repetition is uninspected.

#### MEM-OBJ-research-evidence
Label: Research selected trajectory views

Raw Codex output/events and outcome rows persist in local attempt workspaces. Derived views are text/JSON files or prompt sections; control fields and scores are symbolic, stdout/commands and narrated task content are interpreted text. `_public_outcome` removes nonallowlisted fields but visible stdout/event content is not a proved gold-answer scrubber. This is a material evidence input distinct from the Wiki outputs in [RT-RTE-research-evolve](runtime.md#rt-rte-research-evolve) (SRC-1, `src/wikiskill/officeqa/wiki_agents.py`).

> kept = commands[-max_commands:]
> --- `src/wikiskill/officeqa/wiki_agents.py`

Default Maintainer selects up to five failures and three successes, seed=iteration; shortages are not backfilled. It includes 40 stdout lines, last 12 recognized tool events, truncated command/result representations and full current Wiki, refusing a prompt over 900,000 characters. Full selected traces are staged for optional reads. Default Proposer stages up to 12 sorted eligible case traces, requiring existing stdout; this is not relevance ranking. Its prompt includes outcome summary, incumbent, index, impact summary and file locators. These are per-role context selectors, not automatic foreground-chat compaction (SRC-1, `src/wikiskill/officeqa/wiki_agents.py`).

Paper `visible_trace` prefers tool receipts, falls back to visible session call/output items, adds final prediction, and middle-trims beyond 15,000 characters while retaining a 4,000-character tail. Study learning can additionally receive training workbook reference cells, unlike the legacy public-outcome filter. Large cell feedback is paged: a four-cell preview is explicitly incomplete, while all cells persist in 200-cell pages. These derived views feed model Wiki/skill authors; only the latter's admitted output becomes retained procedural memory. No actual author's use or preservation of causal reasons was observed (SRC-1, `src/wikiskill/paper_alignment/evidence.py`, `src/wikiskill/spreadsheet/study.py`).

> tail=4000;text=text[:limit-tail-len(marker)]+marker+text[-tail:]
> --- `src/wikiskill/paper_alignment/evidence.py`

#### MEM-OBJ-paper-skills
Label: Paper skill and purpose mapping

A local JSON mapping holds named `skill_md` and `purpose_md` text, with symbolic keys. The skills' natural-language procedures are distinct from explanatory provenance in PURPOSE. Unlike [MEM-OBJ-skill](#mem-obj-skill)'s single deployment text, this mapping retains multi-file content. It underlies [MEM-RTE-paper-adapters](#mem-rte-paper-adapters) and [RT-RTE-isolated-study](runtime.md#rt-rte-isolated-study), so it is not part of exactly one supplied route (SRC-1, `src/wikiskill/paper_alignment/contracts.py`, `src/wikiskill/paper_alignment/agents.py`, `src/wikiskill/spreadsheet/study.py`).

> result[name]={'skill_md':value['skill_md'],'purpose_md':value['purpose_md']}
> --- `src/wikiskill/paper_alignment/contracts.py`

Create requires matching frontmatter, apply/not-apply/instructions sections and Origin/Patterns Addressed/Evolution History in purpose. Patch changes a unique specific substring, not a whole-file target; PURPOSE stays unchanged on that patch route. Software also checks at least four distinct trace reads before change. These are structural constraints, not evidence of criticism or generality. Task injection joins only SKILL bodies, not purposes:

> return '\n\n'.join(skills[name]['skill_md'].strip() for name in sorted(skills))
> --- `src/wikiskill/paper_alignment/contracts.py`

Library adapters save `paper-candidate.json` and reconstruct an accepted mapping for later learning-role payloads, checking its joined text against incumbent. Isolated study saves candidate mapping and accepted-only `FINAL-SKILLS.json`, plus joined `FINAL-SKILL.md`. Its proposer starts with empty skills; generic patch capability therefore does not imply that patch is reachable in this one-round study. Reasons are retained for authoring/audit but are omitted from task injection. No deployment of the study's final mapping was inspected.

### Routes

#### MEM-RTE-paper-adapters
Label: Paper role adapter round

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Factory callbacks return normalized Wiki edits or ProposalResult and save structured candidate mapping.
- Later read-back: Maintainer changes persist in Wiki for Proposer; accepted mapping is reconstructed from the last accepted iteration and supplied as skills.json to subsequent learning roles.
- Delegated visibility: Payload contains Wiki without prompt subtree, named skills with purposes, selected train traces for Maintainer and all train traces for Proposer; optional caller training feedback augments views.
- Selection predicate: Train-only unique rows; Maintainer failure/success sample; proposal contract plus at least four reported and actual successful trace reads for a change. Engine owns numeric successor admission.
- Invalidation or expiry: Changed accepted text/map mismatch fails; invalid patch/schema fails before controller applies it; engine's prompt/config/batch checks govern resume. Invocation transport's recovery remains external to this library.
- Activation or effect: Validated Wiki text is written; candidate map is saved and joined skill text returned to engine for validation. Actual content-dependent model decisions remain uninspected.
- Evidence limits: Exposed injected-transport library path, not established default CLI activation or observed operation; no proof that retained purpose or criticism influenced behavior.

This alternate adapter implementation is not identical to [RT-RTE-research-evolve](runtime.md#rt-rte-research-evolve): it plugs into that controller, but constructs different context, edits and candidate mapping. It also differs from [RT-RTE-isolated-study](runtime.md#rt-rte-isolated-study)'s separate one-round caller. SRC-1, `src/wikiskill/paper_alignment/agents.py`:

> """Use an injected isolated invocation transport and optional TRAIN feedback.
> --- `src/wikiskill/paper_alignment/agents.py`

Computational roles propose Wiki and skill edits; generic caller supplies transport/configuration/optional evaluator feedback, not obligatory per-content human approval. `wiki_update` validates creates and local patches, retains every existing pattern in the updated index, and appends narrative. No delete command is in this contract; section replacement can still remove content. Admission rejects malformed mutations; candidate gate veto/retention belongs to engine, not model author. Rejected candidates do not roll back Wiki. The bounded train/validation operating mode and external domain oracle are those of the engine; no independent answer oracle is created by requiring file reads (SRC-1, `src/wikiskill/paper_alignment/contracts.py`, `src/wikiskill/engine.py`).

Theory-builder conditions 1–4: (1) implementation conclusion status: afforded — whole skills with explicit scope sections can state localized theories, but no actual proposal was inspected; (2) operation conclusion status: uninspected — injection/read receipts do not establish decisions dependent on claims; (3) implementation conclusion status: afforded — trace-directed diagnosis and local patches support criticism, not verified claim/result/blame articulation; (4) implementation conclusion status: wired — admitted Wiki and accepted mapping reach later callbacks, while iteration of formulated criticism remains uninspected. Addressability includes named patterns, named skills and unique-section patches. Persistence reaches engine rounds; later cross-experiment reuse is not established by this adapter. Learning benefit and attribution are uninspected. Execution traces can update procedural self-representations and skill instructions can reach later tasks; realized reflection, reflective theory building and autonomous theory building remain uninspected independently.

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-wiki-authors
Label: Wiki to learning authors

The consumers are later Maintainer/Proposer invocations. Channel is full Wiki snapshot for default Maintainer; index/impact summary plus staged pages for default Proposer; full pattern mappings in product context; staged Wiki reads in paper roles. Force is evidence and authoring guidance interpreted by a model, with original explicit requirements requested as binding design constraints in the feedback route. Horizon is subsequent role invocations/rounds and copied product workspaces. This is distinct from [RT-BAP-skill-consumption](runtime.md#rt-bap-skill-consumption), whose consumer is a task executor, and [RT-BAP-role-guidance](runtime.md#rt-bap-role-guidance), whose referent is static packaged instructions rather than learned material (SRC-1, `src/wikiskill/officeqa/wiki_agents.py`, `src/wikiskill/product.py`, `src/wikiskill/paper_alignment/agents.py`).

> parts.append("## Current wiki (read-only snapshot)\n")
> --- `src/wikiskill/officeqa/wiki_agents.py`

Source membership and valid syntax gate writes; source evidence content has no fixed truth-enforcement rule. Delivery is wired; activation and benefit at these model consumers remain uninspected.

## Annotations

#### On [RT-OBJ-product-journal](runtime.md#rt-obj-product-journal)

Storage hashes/sequences are symbolic consistency metadata consumed by Python replay, not natural-language instruction authority. The journal container also holds separately declared natural-language parts [MEM-OBJ-patterns](#mem-obj-patterns) and [MEM-OBJ-feedback](#mem-obj-feedback); those parts' sources and consumers differ from integrity metadata. Historical result/proposal events retain raw evidence and current-pointer changes, not only the latest display. SRC-1, `src/wikiskill/product.py`; the supplied record's quote supplies the replay warrant.

#### On [RT-RTE-product-round](runtime.md#rt-rte-product-round)

Read-back is code-selected push after caller `next`: completed current-round train records, all current patterns, all original feedback and gate history enter a saved learning context. Proposer's new context follows committed learning; task requests select candidate during validation and incumbent otherwise. Count limits work issuance, not context tokens. There is no token selector in the inspected `_context` construction; no universal context-cap claim follows. Source trust is ID membership, additionally including existing patterns as shown by [MEM-OBJ-patterns](#mem-obj-patterns). The raw-output/optional-trace → interpreted lesson → skill → later task chain is wired, but trace presence and actual use remain conditional (SRC-1, `src/wikiskill/product.py`).

Inheritance copies patterns and original feedback plus retained skill by default; an explicit initial skill overrides that default. It records source workspace fingerprints/event identity, not a full original workspace archive. Feedback-first `begin(previous=..., skill=None)` is a counterexample to unqualified inherited-skill use: after product initialization it explicitly clears `current_skill` while retaining inherited knowledge (SRC-1, `src/wikiskill/product.py`, `src/wikiskill/feedback_loop.py`).

> state=p._event(root,state,'phase',{'phase':'maintainer', **({'current_skill':None} if skill is None else {})})
> --- `src/wikiskill/feedback_loop.py`

#### On [RT-RTE-native-handoff](runtime.md#rt-rte-native-handoff)

Dispatch code pushes task plus selected skill only to executor, and paths to a staged learning context to authors. It requests a fresh host frame and no inherited coordinator conversation. Result pointer/status crosses back; raw output/optional trace is copied through collection. Entire child-context disposal is host behavior, not inspected memory eviction. Files stay reachable subject to normal host permissions; no host compaction or global-memory disablement is established by product handoff. A scoring retry may deliberately reuse saved output and earlier delegation instead of making a new model invocation (SRC-1, `src/wikiskill/native_agents.py`; supplied route supports the host-report limit).

Native `_learning_context` replaces gate history with aggregate fields. Numeric history omits candidate text, note and candidate pointers; feedback history keeps verdict/reason/pairs but not full original gate event. Thus prior rationale and rejected candidate bodies can persist in artifacts without being delivered by this context. This narrows any reading that all history is automatically supplied.

> context['gate_history'] = [{k: row[k] for k in ('round','verdict','incumbent_score','candidate_score','improvement')}
>                            for row in state['history']]
> --- `src/wikiskill/native_agents.py`

#### On [RT-RTE-feedback-gate](runtime.md#rt-rte-feedback-gate)

Original notes and optional comparison artifact remain local evidence; paired verdicts and requirement checks are symbolic inputs plus interpreted evidence prose. Rejection retains Wiki and incumbent and can produce REVISION_REQUIRED; subsequent learning context explicitly requests revising regressions without dropping requirements. `skip` can terminate without comparison/adoption; it is not a successful evaluation or withdrawal of retained knowledge. Per-content human control is established only when a person actually supplies the content, not by origin strings. The software selection predicates do not verify evidence entailment (SRC-1, `src/wikiskill/feedback_loop.py`, `src/wikiskill/product.py`; supplied route quotes the predicate).

#### On [RT-RTE-research-evolve](runtime.md#rt-rte-research-evolve)

Default context selection and edits are detailed in [MEM-OBJ-research-evidence](#mem-obj-research-evidence) and [MEM-OBJ-research-wiki](#mem-obj-research-wiki). They separate raw retained attempts from curated pages and inline summaries. Resume has multiple retained forms: valid outcome rows are reused against batch identity; a Maintainer completion marker suppresses repeat maintenance; `proposal.json` suppresses repeat proposal; gate events reconstruct incumbent. `wiki-before` is retained for review/recovery, not an automatic candidate-rejection rollback. Rebuilding temporary `.maintainer`/`.proposer` work directories removes those staging directories, not the already committed Wiki or accepted skill (SRC-1, `src/wikiskill/engine.py`, `src/wikiskill/officeqa/wiki_agents.py`).

> if not marker.exists():
>     # Retain before/after Wiki snapshots for review and recovery.
>     backup = directory/'wiki-before'
> --- `src/wikiskill/engine.py`

#### On [RT-RTE-isolated-study](runtime.md#rt-rte-isolated-study)

Preparation freezes empty Wiki/skills and first bounded train/validation selections. Each task is a fresh invocation with workbook/task/skill rather than Wiki. Learning-role selection pushes sampled failures/successes to Maintainer and all training summaries to Proposer, with staged reference feedback and trimmed visible traces. Automatic selection is triggered by `_learn`, then model `read_file` selects exact staged files on demand; the read returns whole text, not an embedding search. Successful trace reads are checked, not comprehension. Maintainer's admitted Wiki is the retained bridge to Proposer (SRC-1, `src/wikiskill/spreadsheet/study.py`, `src/wikiskill/isolated/tools_server.py`).

> content = path.read_text(encoding='utf-8')
> --- `src/wikiskill/isolated/tools_server.py`

Final gate writes accepted-only skill mapping/text while preserving candidate and Wiki evidence. The empty initial `wiki/skill-impact.md` is not updated with this study's gate before Proposer: final `skill-impact.json` is a distinct post-gate artifact and no second learning consumer is scheduled. This bounds any implication that rejection history already shapes a next study iteration. Native raw event/session archives and sealed reuse are supplied runtime findings; actual isolation/compaction remains unobserved.

#### On [RT-RTE-skill-install](runtime.md#rt-rte-skill-install)

Export selects current retained text and writes provenance; installation changes only SKILL.md with local backup/receipt. Restore either reintroduces the checked previous bytes or removes a new install, refusing to overwrite subsequent edits. This withdraws a deployment copy, not the originating Wiki/history. Supporting files and paper PURPOSE mappings are not deployed by this installer. Generic callers choose destination and replacement flag; software receipt/hash checks are separate from human approval. Future host discovery is afforded, not verified read-back (SRC-1, `src/wikiskill/product_install.py`; supplied route supports complete-phase admission).

> if old is None:
>     target.unlink()
> else:
>     _replace(target, old)
> --- `src/wikiskill/product_install.py`

## Write side

Acquisition and transformation have separate authority. Product accepts caller task artifacts, optional traces and original feedback; configured scorer results are externally produced judgments. The intended Maintainer transforms these into [MEM-OBJ-patterns](#mem-obj-patterns), whose source-ID check admits contributions without proving truth. Proposer transforms committed knowledge into [MEM-OBJ-skill](#mem-obj-skill). Software adopts only after the route-specific numeric or pairwise predicate; it does not require per-candidate human approval. Initial skill supply, generic caller submission, model authorship and physical file copying must not be collapsed into one admission category (SRC-1, `src/wikiskill/product.py`, `src/wikiskill/feedback_loop.py`).

Default research transforms selected tool trajectories/outcomes into Wiki pages and then proposals; paper adapters alternatively use local patches and named skill/purpose mappings. Structural admission differs: product checks nonblank bodies and source membership; legacy pages check filenames/existence/duplicates; default skill checks include 200 lines, 150 changed lines and known motivating patterns; paper contracts check local unique patch targets and required sections/read counts. None of these proves the resulting lesson is warranted. Admission and rejection/recovery particulars belong to [RT-RTE-research-evolve](runtime.md#rt-rte-research-evolve), [MEM-RTE-paper-adapters](#mem-rte-paper-adapters) and their object records (SRC-1, `src/wikiskill/officeqa/wiki_agents.py`, `src/wikiskill/wiki_maintainer.py`, `src/wikiskill/paper_alignment/contracts.py`).

Reasons can survive separately as original notes, evidence IDs, page evidence/guidance, narrative, proposal note/rationale/purpose/diff and gate history. They are not guaranteed to survive every transformation into the deployed skill. Later authoring routes can read some of them; task injection typically carries only the procedural text. Partial context rendering must not be mistaken for loss of every original artifact, or archival retention for automatic later consumption.

Rejection keeps the incumbent but generally preserves learned Wiki and proposal evidence. Retry/resume prevents some repeated work through sealed results and checkpoints. No inspected learning API exposes a general delete-pattern operation: product merges keys, legacy edit lists create/replace pages, paper contracts create/patch while retaining index coverage. This is a scoped description of those interfaces, not a repository-wide absence claim; text replacements can retract assertions. Installation restore is an explicit downstream withdrawal route, not knowledge erasure (SRC-1, `src/wikiskill/product.py`, `src/wikiskill/wiki_maintainer.py`, `src/wikiskill/paper_alignment/contracts.py`, `src/wikiskill/product_install.py`).

## Read-back

There is no single retrieval direction. The caller asks for work, controller code selects a phase-specific bundle and pushes it to a later model invocation; that model can then pull exact source files. Product selection is by phase/round, not semantic search. All current Wiki patterns/feedback enter authoring context. Native output-only return limits coordinator context growth by protocol, while underlying files remain. Default research uses a full Wiki snapshot for maintenance, index/impact/outcome summaries for proposal, and on-demand staged trace/page reads. Paper tools similarly expose staged text, with explicit read receipts. These mechanisms determine what enters a fresh role frame; they do not demonstrate trimming an already accumulated foreground conversation (SRC-1, `src/wikiskill/product.py`, `src/wikiskill/native_agents.py`, `src/wikiskill/officeqa/wiki_agents.py`, `src/wikiskill/isolated/tools_server.py`).

Budgets are heterogeneous: product has no inspected token cap; legacy maintenance caps selected cases, tails and prompt characters; legacy proposal caps staged eligible traces and skill/diff size; paper views middle-trim traces and study feedback uses pages. The model or host decides whether to follow available file pointers, and host window truncation is uninspected. Raw archives, derived summaries, Wiki and adopted skills persist independently. Only the actual delivery route determines which one a consumer sees. [MEM-BAP-wiki-authors](#mem-bap-wiki-authors) and [RT-BAP-skill-consumption](runtime.md#rt-bap-skill-consumption) separate knowledge-authoring influence from task-execution instruction force.

Inheritance and installation extend potential horizons without establishing deployed use. Product can copy current knowledge into a new workspace; installation/export copies retained SKILL for an external host. A generic library storage/read function such as `wiki_snapshot` is not itself an additional consumer route; concrete calls in role factories establish that route. Similarly an injected paper transport affords a caller role but does not establish a shipped default CLI execution of it (SRC-1, `src/wikiskill/product.py`, `src/wikiskill/product_install.py`, `src/wikiskill/wiki.py`, `src/wikiskill/paper_alignment/agents.py`).

## Integration issues

- **Qualification of source admission:** [RT-RTE-product-round](runtime.md#rt-rte-product-round)'s short training/feedback account omits existing pattern source IDs. [MEM-OBJ-patterns](#mem-obj-patterns) shows the actual allowed union. It permits derived-to-derived lineage; no semantic-entailment guarantee should be inferred from the narrower error string (SRC-1, `src/wikiskill/product.py`).
- **History delivery is route-specific:** [RT-RTE-native-handoff](runtime.md#rt-rte-native-handoff) already identifies aggregate history; its omissions matter for [MEM-OBJ-skill](#mem-obj-skill)'s retained rationale. Default research history also has an inline summary versus full staged artifact distinction ([MEM-OBJ-skill-impact](#mem-obj-skill-impact)). Prior failed interventions remain archived without necessarily being present in the author's immediate context (SRC-1, `src/wikiskill/native_agents.py`, `src/wikiskill/officeqa/wiki_agents.py`).
- **Additional alternative, not duplicate:** [MEM-RTE-paper-adapters](#mem-rte-paper-adapters) supplies a callback path not characterized separately by [RT-RTE-research-evolve](runtime.md#rt-rte-research-evolve). It is also not identical to [RT-RTE-isolated-study](runtime.md#rt-rte-isolated-study). Engine ownership overlaps, payload/contract/controller callers differ. [MEM-OBJ-paper-skills](#mem-obj-paper-skills) is a mapping distinct from joined [MEM-OBJ-skill](#mem-obj-skill) text; both remain needed (SRC-1, `src/wikiskill/paper_alignment/agents.py`, `src/wikiskill/spreadsheet/study.py`).
- **Inheritance exception:** Ordinary product inheritance can carry an incumbent, but feedback-first initialization with absent explicit skill clears its active pointer. This qualifies a universal reading of [RT-RTE-feedback-gate](runtime.md#rt-rte-feedback-gate)/[RT-RTE-product-round](runtime.md#rt-rte-product-round)'s inheritance horizons; patterns and feedback still carry forward (SRC-1, `src/wikiskill/feedback_loop.py`).
- **Claim/implementation mismatch in paper history:** The source prompt's “full content of rejected proposals” wording exceeds default impact-file contents and cannot describe an already evaluated predecessor in a fresh one-round study. [MEM-OBJ-skill-impact](#mem-obj-skill-impact) and the isolated annotation localize the limit. No supplied runtime record must be replaced to retain it (SRC-1, `src/wikiskill/resources/paper_alignment/prompts/proposer.paper.md`, `src/wikiskill/engine.py`, `src/wikiskill/spreadsheet/study.py`).
- **Open operation questions:** Whether model authors read full staged evidence, preserve reasons, obey constraints, or improve subsequent decisions remains uninspected for [MEM-BAP-wiki-authors](#mem-bap-wiki-authors), [MEM-RTE-paper-adapters](#mem-rte-paper-adapters) and supplied task-consumption paths. No execution evidence resolves these. Available but unread domain prompt/evaluator/retrieval details in the coverage table prevent universal prompt-equivalence, source-scrubbing or scoring-validity conclusions, not the specific positives above.
- **Record identity comparison:** No duplicate declaration is intended. Product patterns/feedback are declared parts of the supplied journal; other new objects separate its external payloads or describe research-only material with different consumers/checks. The new behavioral path concerns learned Wiki, not static [RT-BAP-role-guidance](runtime.md#rt-bap-role-guidance). Container and part findings can coexist without supersession.

## Limitations and checks

The source identity and full checkout HEAD were rechecked against the supplied boundary before analysis. Inspection stayed within SRC-1 and authorized supplied members; no prior target analyses or mutable run metadata were read. Consequential positives were challenged against alternate direct APIs, feedback initialization, paper adapters, history projections and final-study retention. These checks restrict strong labels rather than erase implemented memory paths.

No observed activation, human authorship authentication, provider-weight change, future-task benefit or causal attribution was established. [RT-CMP-host-model](runtime.md#rt-cmp-host-model) and [RT-CMP-research-model](runtime.md#rt-cmp-research-model) supply the external distributed-parametric component limits; this job does not convert procedural memory into weight learning. Context window eviction/compaction inside external hosts remains uninspected. The coverage table identifies further source-reading limits without asserting absence.

Deterministic validation: the invocation-specific `commonplace-run validate-output` check passed. Its complete result was: “Member content check passes; invocation residue not checked. This is not job acceptance or claim support.” The check establishes structure, identities and quotation occurrence, not semantic correctness or acceptance.
