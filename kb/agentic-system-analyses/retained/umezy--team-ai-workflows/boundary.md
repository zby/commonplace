---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "team-ai-workflows' shipped skill distribution and knowledge-search system at commit 9aebd7a6c2803da450904eb5621ae5439508ff94."
run-id: AAS-2026-11-09-team-ai-workflows-c00fb85f7ed1-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "9aebd7a6c2803da450904eb5621ae5439508ff94"
analysis-cutoff: "2026-11-09"
evidence-tier: code-grounded
source:
  identity: https://github.com/umezy/team-ai-workflows
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/team-ai-workflows-d4887b78cf12/related-systems/umezy--team-ai-workflows
  revision: "9aebd7a6c2803da450904eb5621ae5439508ff94"
  sha256: null
---

# team-ai-workflows boundary

## Boundary and evidence

This analysis covers the shipped repository template for distributing team skills and a Markdown knowledge base to Claude Code users. Its intended use is machine-wide access to team skills and retrieval of team knowledge while working in other projects. The target is a **memory/knowledge/context-engineering system**, not an enclosing agent runtime: its model-dependent portion is the skill workflow served to Claude Code, while shell and Python programs perform link synchronization and lexical retrieval. The README describes that division (SRC-1, `README.md`):

> A template for distributing **Claude Code skills** and a **team knowledge base** through a single git repository.
> --- `README.md`

The boundary is **whole-system** for this shipped template. It includes onboarding instructions, installation of user-level skill links and a Git hook, configuration of the knowledge-root environment variable, update-time link maintenance, the retained Markdown corpus, search code, and the prompt that makes the host generate queries and consume retrieved files. The same-repository setup driver and search consumer are included rather than treated as external applications (SRC-1, `.claude/skills/team-setup/SKILL.md`, `.claude/skills/team-setup/scripts/post-merge`, `.claude/skills/team-setup/scripts/sync_user_skills.sh`, `skills/docs-grep/SKILL.md`, `skills/docs-grep/scripts/docs_search.py`).

The model-dependent query and answer steps are declared instructions, not behavior implemented by the Python search program (SRC-1, `skills/docs-grep/SKILL.md`):

> Derive 4–8 search keywords from the question. Include synonyms, abbreviations, and both English and native-language variants where relevant.
> --- `skills/docs-grep/SKILL.md`

> Read the top-ranked files and answer the question. Cite the relative paths of the files you used. If the hits look weak, adjust the keywords and repeat Step 2.
> --- `skills/docs-grep/SKILL.md`

The corpus is maintained as repository files rather than through a shipped knowledge-write API. The README instructs adopters to replace samples, and the included writing guidance addresses file authors; the inspected tracked tree contains no separate ingestion service, evaluator or automated knowledge-maintenance runner (SRC-1, `README.md`, `sources/tips/writing-knowledge.md`).

> Replace the samples in `sources/` with your team's knowledge (docs copies, API references, first-hand tips)
> --- `README.md`

### Coverage of the tracked top level

All tracked text files were inspected. The following table accounts for every top-level tracked file or directory at the frozen commit; no material shipped operational path remains uninspected.

| Top-level path | Treatment and material paths | Role and limits |
|---|---|---|
| `.claude/` | Included; `.claude/skills/team-setup/SKILL.md`, `.claude/skills/team-setup/scripts/post-merge`, `.claude/skills/team-setup/scripts/sync_user_skills.sh` inspected | Model-facing onboarding, user-level link production and cleanup, hook installation instructions, environment configuration and update-time synchronization. Host compliance with instructions is not observed. |
| `.gitattributes` | Included; inspected | Text line-ending policy for shell/Python files and binary GIF treatment; no claim of tested platform compatibility. |
| `.gitignore` | Included; inspected | Excludes Python cache and environment files from tracking; does not establish deployed secret handling. |
| `LICENSE` | Included; inspected | MIT licensing context, not operational evidence. |
| `README.md` | Included; inspected | Intended usage, prerequisites, repository customization and update entry points. Its external article and linked Claude Code documentation are not included. |
| `docs/` | Deliberately excluded; `docs/demo.gif` is present but not inspected | README-linked demonstration media, not an executable path. No claims about depicted operation, successful demonstrations or timing follow from it. |
| `skills/` | Included; `skills/docs-grep/SKILL.md` and `skills/docs-grep/scripts/docs_search.py` inspected | Model-facing keyword generation, iterative search and answer instructions; deterministic source-root resolution, Markdown traversal, ranking and previews. |
| `sources/` | Included; `sources/api-reference/sample-api.md`, `sources/documentation/getting-started.md`, `sources/tips/writing-knowledge.md` inspected | Persisted sample corpus, onboarding knowledge and authoring guidance. Samples do not establish the quality or content of any adopter's real knowledge base. |

This coverage derives from the frozen tracked tree and SRC-1's paths listed in the table. Source inspection traces `/team-setup` to its synchronization script and installed hook, and `/docs-grep` to its search program and subsequent model-side consumption of corpus files. No tests or evaluator are shipped in that tree. No target programs, examples or model calls were executed.

### External dependencies and evidence limits

Claude Code supplies skill discovery, model execution, interactive user questions, tool execution and session behavior. Git supplies distribution and hook invocation; the user's shell and filesystem supply links, with Windows-specific utilities used by the synchronization script. Python supplies search execution. These dependencies are identified by shipped instructions and code but their implementations are outside the frozen source. Consequently, this run cannot establish host discovery semantics, actual session restart behavior, operating-system compatibility, successful installation or end-to-end answer quality (SRC-1, `README.md`, `.claude/skills/team-setup/SKILL.md`, `.claude/skills/team-setup/scripts/sync_user_skills.sh`, `skills/docs-grep/scripts/docs_search.py`). Local user configuration, installed links and actual team deployments are not supplied; their state and operational outcomes cannot be inferred.

The README's external design write-up and the host documentation are deliberately outside the source set. Their arguments, history and host guarantees cannot support this run. The uninspected GIF is a deliberate exclusion, not unavailable evidence. No material source-text access gap was encountered.

The frozen evidence is repository `https://github.com/umezy/team-ai-workflows` at full commit `9aebd7a6c2803da450904eb5621ae5439508ff94`, with applicability cutoff **2026-11-09**. The overall tier is **code-grounded** for shell/Python behavior and **doctrine/design** for model-facing instructions and declared intent. This is source-level analysis, not observed operation or a causal experiment. Later revisions, the current live repository and external articles are not evidence for this run.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/umezy/team-ai-workflows` | 9aebd7a6c2803da450904eb5621ae5439508ff94 | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/team-ai-workflows-d4887b78cf12/related-systems/umezy--team-ai-workflows`. Implementation: `.claude/skills/team-setup/scripts/post-merge`, `.claude/skills/team-setup/scripts/sync_user_skills.sh`, `skills/docs-grep/scripts/docs_search.py`. Doctrine/design: `README.md`, `.claude/skills/team-setup/SKILL.md`, `skills/docs-grep/SKILL.md`, all three `sources/` Markdown files. Supporting repository metadata: `.gitattributes`, `.gitignore`, `LICENSE`. Full tracked tree inspected for coverage. | Implementation: [synchronization](https://github.com/umezy/team-ai-workflows/blob/9aebd7a6c2803da450904eb5621ae5439508ff94/.claude/skills/team-setup/scripts/sync_user_skills.sh), [hook](https://github.com/umezy/team-ai-workflows/blob/9aebd7a6c2803da450904eb5621ae5439508ff94/.claude/skills/team-setup/scripts/post-merge), [search](https://github.com/umezy/team-ai-workflows/blob/9aebd7a6c2803da450904eb5621ae5439508ff94/skills/docs-grep/scripts/docs_search.py). Doctrine/design: [README](https://github.com/umezy/team-ai-workflows/blob/9aebd7a6c2803da450904eb5621ae5439508ff94/README.md), [setup instructions](https://github.com/umezy/team-ai-workflows/blob/9aebd7a6c2803da450904eb5621ae5439508ff94/.claude/skills/team-setup/SKILL.md), [search instructions](https://github.com/umezy/team-ai-workflows/blob/9aebd7a6c2803da450904eb5621ae5439508ff94/skills/docs-grep/SKILL.md), [knowledge-writing guidance](https://github.com/umezy/team-ai-workflows/blob/9aebd7a6c2803da450904eb5621ae5439508ff94/sources/tips/writing-knowledge.md). | No material text access gap. `docs/demo.gif` deliberately uninspected; no demonstration claims. Host implementation, external articles and deployed user state excluded; host guarantees, real deployment success and answer quality remain unestablished. No observed-run or causal-experiment evidence inspected. |
