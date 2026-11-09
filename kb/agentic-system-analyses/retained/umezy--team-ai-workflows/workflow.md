---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Workflow account of team-ai-workflows: a user question passes through keyword search, full-file reading and a cited host answer, with retry and configuration-failure limits."
run-id: AAS-2026-11-09-team-ai-workflows-c00fb85f7ed1-01
reviewed-boundary: "9aebd7a6c2803da450904eb5621ae5439508ff94"
---

# team-ai-workflows workflow report

## Workflow account

### Selection and evidence boundary

The representative workflow is `/docs-grep`: a user question becomes keywords, a ranked file list, full-file reading and a cited answer. It is selected because it is the shipped knowledge-consumption procedure, not because a successful execution was supplied. Its consequential decisions and tool handoff are explicit in [RT-RTE-knowledge-search](runtime.md#rt-rte-knowledge-search). Setup and distribution are prerequisites rather than separate stages invented inside each lookup: [RT-RTE-machine-setup](runtime.md#rt-rte-machine-setup) requests installation and restart; [RT-RTE-skill-sync](runtime.md#rt-rte-skill-sync) exposes skill directories through links.

This account independently inspects SRC-1 at the frozen commit: `skills/docs-grep/SKILL.md` supplies doctrine/design, and `skills/docs-grep/scripts/docs_search.py` supplies implementation. The three sample files, `sources/api-reference/sample-api.md`, `sources/documentation/getting-started.md` and `sources/tips/writing-knowledge.md`, were also read as doctrine/design and corpus content. These paths are already in the boundary's coverage; no source or operational evidence is added. Neither the scripts nor the host were executed. The account establishes an instructed multi-step workflow with an implemented search step, not observed delivery or reliable answering.

### Request, delegation and result transformation

1. **User to host.** The skill receives the user's question or research topic as `$ARGUMENTS`. Claude Code is the external interpreter, not a locally implemented coordinator ([RT-CMP-claude-code](runtime.md#rt-cmp-claude-code)). The model is instructed to derive 4–8 keywords with synonyms, abbreviations and relevant language variants. That number is guidance, not a CLI constraint. The source-native instructions are [RT-OBJ-docs-grep](runtime.md#rt-obj-docs-grep); neither query quality nor compliance is demonstrated.
2. **Host to Python.** The host is told to run `python "$HOME/.claude/skills/docs-grep/scripts/docs_search.py"` with the derived keywords (SRC-1, `skills/docs-grep/SKILL.md`). This is tool delegation, not delegation to another model worker. The process receives keyword arguments and filesystem/environment access, not a separately specified copy of the whole question or conversation. It resolves a valid configured `sources/` root before falling back to its real script location. The chosen corpus can therefore differ from the checkout containing the script; root identity is not authenticated ([RT-RTE-knowledge-search](runtime.md#rt-rte-knowledge-search)).
3. **Python to host.** Code reads recursive Markdown files and selects lowercase substring matches. It orders files by distinct keywords matched, then keyword-line hit count, then path. It emits at most 15 relative paths with scores and at most two 100-character line previews each. The returned material is a navigation aid, not all matched document content. Unreadable files are skipped; the host cannot infer completeness from the ranked output. These implemented transformations are recorded in [RT-RTE-knowledge-search](runtime.md#rt-rte-knowledge-search).
4. **Host to files to user.** The next requested action is reading the top-ranked files, then answering with their relative paths. Full-file reading is a separate host action: Python does not pass complete documents through its result interface and does not write the answer. The prompt does not specify how many ranked files must be read. The host owns both that selection and the judgment that the hits suffice. Delivery, in this procedure, is the host's cited answer to the user, not the search process returning exit 0. No additional acceptance artifact or user-approval gate is prescribed by this skill (SRC-1, `skills/docs-grep/SKILL.md`; [RT-RTE-knowledge-search](runtime.md#rt-rte-knowledge-search)).

The distinction between preview and file consumption is load-bearing: the instructed answer depends on a subsequent read, not merely on displaying relevant-looking snippets. The inspected source requests that handoff; it does not establish that the host performed it or that cited content supports the eventual answer. Links make the instructions reachable, not binding on all host behavior ([RT-BAP-user-skills](runtime.md#rt-bap-user-skills)).

### Verification, retry and configuration failure

The verification decision is a model judgment about whether the hits look weak. Python's lexical scores are ordering rules, not an answer oracle or a semantic acceptance test. The model proposes keywords, judges the returned evidence and may replace the keywords. No independent reviewer, expected answer, fixed sufficiency threshold or retry budget is supplied in this route ([RT-RTE-knowledge-search](runtime.md#rt-rte-knowledge-search)). The complete requested loop is expressed in SRC-1, `skills/docs-grep/SKILL.md`:

> Read the top-ranked files and answer the question. Cite the relative paths of the files you used. If the hits look weak, adjust the keywords and repeat Step 2.
> --- `skills/docs-grep/SKILL.md`

There are distinct failure paths, not one generic rejection gate:

- **No matches:** Python prints a retry suggestion and returns 0. It does not generate new keywords or rerun itself. The host must act on the suggestion under the skill's retry policy. A zero status thus cannot mean a satisfactory answer was found (SRC-1, `skills/docs-grep/scripts/docs_search.py`):

> if not results:
>         print("no matches. try different keywords.")
>         return 0
> --- `skills/docs-grep/scripts/docs_search.py`

- **Missing corpus root after resolution:** Python returns 1 and suggests configuration or setup. This is a configuration repair request, not evidence that the user question lacks an answer. It supplies no automatic configuration write or retry (SRC-1, `skills/docs-grep/scripts/docs_search.py`):

> if not src.is_dir():
>         print(f"[error] sources/ not found: {src}")
>         print("Set TEAM_WORKFLOWS_DIR to the repo root, or run /team-setup.")
>         return 1
> --- `skills/docs-grep/scripts/docs_search.py`

- **Empty keyword input or unreadable files:** empty input gets usage and exit 1; individual read errors instead skip files and continue. Those paths are already bounded in [RT-RTE-knowledge-search](runtime.md#rt-rte-knowledge-search). The latter can produce a partial result set without a per-file error report.

The host/user must pursue any configuration repair through the setup route or environment changes; the search program only advises it. Rerunning setup is an instructed installation-repair affordance, not a guarantee that lookup recovers ([RT-RTE-machine-setup](runtime.md#rt-rte-machine-setup)). The skill does not specify what final response to give after repeated weak hits, how to resolve conflicting files or when to abandon a search. Those unspecified decisions prevent a claim of complete failure-handling coverage, but do not prevent tracing the supplied retry path.

### Delivery and limits

The prescribed terminal result is a question answer citing relative source paths. Search stdout is an intermediate return; a citation is requested attribution, not verification of correctness. Nothing in the inspected lookup code evaluates or rejects the final prose. The source supplies no execution trace establishing that an answer was produced, files were actually read or a retry improved relevance. It also supplies no persistence step for the query, failed attempt or answer: the route rebuilds results on each call, while later corpus changes belong to [RT-RTE-repository-admission](runtime.md#rt-rte-repository-admission), not to this search loop. Host session retention remains outside the inspected implementation.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

none declared in this member

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-knowledge-search](runtime.md#rt-rte-knowledge-search)

Workflow role: the representative request-to-answer chain. The critical handoff is from bounded ranked previews to separate host file reads; the preview list alone is not the requested answer evidence. Verification ownership remains with the foreground host/model. Its weak-hit judgment can initiate another search, while code supplies only lexical ordering and distinct error/no-match returns. Delivery is the subsequent cited answer, not a subprocess success status. Recovery from a missing corpus requires a host/user configuration action; search itself performs no repair. These are workflow-specific consequences of the route, not a distinct route identity. No observed completion, successful recovery or benefit is established.
