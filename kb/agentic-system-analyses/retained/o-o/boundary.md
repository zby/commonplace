---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "o-o's self-updating document workflow and shipped library manager at commit b0d5063e37b4eafdbc23c1899a31f1836168b989."
run-id: AAS-2026-10-15-o-o-b6fd0055e5c1-01
result-disposition: complete
target-class: workflow
boundary-kind: whole-system
reviewed-boundary: b0d5063e37b4eafdbc23c1899a31f1836168b989
analysis-cutoff: "2026-10-15"
evidence-tier: code-grounded
source:
  identity: https://github.com/jahala/o-o
  kind: git
  path: /media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-17-o-o/related-systems/jahala--o-o
  revision: b0d5063e37b4eafdbc23c1899a31f1836168b989
  sha256: null
---

# o-o boundary

## Boundary and evidence

This run covers o-o as a **workflow** for creating, periodically researching, updating and reading persistent HTML/bash documents. Its intended use is maintaining living research articles and a browsable local library. It is in scope because its shipped shell driver launches an external model-powered agent with a document-specific research and editing task. It does not implement the agent's internal model/tool loop. The boundary is **whole-system** for the shipped o-o repository, not for Claude Code or the wider research web. SRC-1: `README.md`, `example/index.o-o.html`.

The classification rests on the executable dispatch in SRC-1, `example/index.o-o.html`:

>       local -a claude_args=(
>         -p "$prompt"
>         --allowed-tools "Bash,Read,Edit,WebSearch,WebFetch"
>         --max-budget-usd "$budget"
>       )
> --- `example/index.o-o.html`

>       claude "${claude_args[@]}"
> --- `example/index.o-o.html`

Included responsibilities are the polyglot entry points; template generation; interactive and quick document creation; freshness and budget extraction; agent dispatch and embedded update instructions; article, manifest, source-cache and changelog retention; subsequent prompt-directed reuse; browser rendering and navigation; library rebuilding and batch updates; contract/configuration editing; and shared-code synchronization. The index is a shipped producer and consumer of the same documents, not an excluded host. SRC-1: `example/index.o-o.html`, `example/anthropic-leadership.o-o.html`.

The document maintenance contract explicitly instructs later reuse rather than a fresh research start. This is declared agent behavior, not evidence that every update follows it. SRC-1: `example/anthropic-leadership.o-o.html`:

>       "3. Read the oo-source-cache JSON block to see what sources and facts were gathered previously. Build on prior research, do not start from scratch.",
> --- `example/anthropic-leadership.o-o.html:428-428`

The frozen evidence is repository commit **b0d5063e37b4eafdbc23c1899a31f1836168b989**, verified as the acquired checkout's HEAD. The analysis cutoff is **2026-10-15**, the supplied run date; it does not assert that the sample articles were refreshed on that date. The evidence tier is **code-grounded**: shell and browser code establish implementation, while embedded contracts and README establish declared intent. Sample caches and changelogs are attributed retained content, not independently observed executions or causal experiments.

### Shipped-path coverage

The tracked tree contains the following top-level entries. All material o-o state-producing, maintenance and consumption paths are included. No shipped evaluator or test suite appears in that tree. SRC-1: `README.md`, `example/index.o-o.html`.

| Top-level tracked entry | Included or excluded | Material paths, role and inspection | Limit or conclusion prevented |
|---|---|---|---|
| `.github/` | Excluded after inspection | `.github/FUNDING.yml` contains sponsorship configuration only. | No conclusion about sponsorship-service operation; no document-loop responsibility excluded. |
| `.gitignore` | Excluded after inspection | Local ignore rules, including `docs/`, environment files and logs. | Ignored or untracked files are not evidence; no conclusion about their contents. |
| `LICENSE` | Excluded after inspection | MIT licensing text. | No legal assessment; no runtime responsibility excluded. |
| `README.md` | Included | Complete README inspected: usage, structure, update contracts, index CLI, synchronization, dependencies and roadmap. | Intent and usage claims are not execution evidence. Roadmap items are not treated as shipped automation. |
| `example/` | Included | `example/index.o-o.html`: shell template, embedded maintenance prompt, state initialization, create/update-all drivers, freshness checks, dispatch, config editing, sync, index state consumption and browser JS inspected. All nine files' marked shell, JS and CSS blocks compared; each respective block is identical across the shipped files. | Static inspection supports the shipped control paths, not successful updates, rendering compatibility or adherence by the external agent. CSS block equality was checked; individual styling rules were not reviewed. |
| `example/` article instances | Included, detailed coverage of the preceding directory | `example/anthropic-leadership.o-o.html`: complete contract, source cache and changelog inspected as the representative populated document. `example/agi-declared.o-o.html` and `example/trump-incarceration.o-o.html`: complete sentinel contracts inspected. `example/ai-model-landscape.o-o.html`, `example/competitor-costco.o-o.html`, `example/openclaw.o-o.html`, `example/vendor-comparison-vector-dbs.o-o.html` and `example/yc-w26-batch.o-o.html`: entry preambles, manifest values, contract identity and instruction equality, and cache/changelog shapes inspected. Their maintenance instructions match the representative ordinary contract; sentinel instructions differ and were read separately. | Article bodies, embedded images and every topic-specific research setting were not exhaustively inspected. Their factual accuracy and research quality are not established. These are included data instances, not omitted drivers; their common execution and consumption code was inspected through the identical shared blocks. |

### External dependencies and evidence limits

Claude Code and its model providers are external execution dependencies. The registered repository supplies the command invocation and allowed-tool list, not Claude Code's implementation, permission enforcement, model selection defaults, billing behavior or internal session persistence. Those responsibilities must not be attributed to o-o. Bash and shell utilities supply local execution; browser APIs supply reading and UI behavior. The shell uses Perl for multiline parsing and edits despite the README's emphasis on minimal dependencies. Optional image instructions refer to curl, base64 and platform image utilities. SRC-1: `README.md`, `example/index.o-o.html`.

Research websites, linked references and the hosted live demo were not acquired as separate evidence. Their availability, current contents and support for sample article claims are therefore not established. No target code, examples or tests were executed, and no providers were called. No missing repository access prevented inspection of a material shipped path. The absence of observed update traces prevents conclusions about actual cost, factual quality, successful incremental reuse, safety enforcement or repeatability; it does not prevent establishing the source-level workflow boundary. SRC-1: `example/index.o-o.html`, `example/anthropic-leadership.o-o.html`.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/jahala/o-o` | b0d5063e37b4eafdbc23c1899a31f1836168b989 | implementation; doctrine/design; reported operation | Access root: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-17-o-o/related-systems/jahala--o-o`. Implementation: tracked tree, identical shared blocks across `example/*.o-o.html`, index shell and browser JS, article preambles and state-block structure. Doctrine/design: complete `README.md`, generated contract in `example/index.o-o.html`, ordinary contract in `example/anthropic-leadership.o-o.html`, and sentinel contracts in `example/agi-declared.o-o.html` and `example/trump-incarceration.o-o.html`. Reported operation: representative populated cache and changelog in `example/anthropic-leadership.o-o.html`; sample manifests and changelog shapes across the other articles. Ancillary files inspected as listed above. | Implementation: [index driver and consumer](https://github.com/jahala/o-o/blob/b0d5063e37b4eafdbc23c1899a31f1836168b989/example/index.o-o.html). Doctrine/design: [README](https://github.com/jahala/o-o/blob/b0d5063e37b4eafdbc23c1899a31f1836168b989/README.md), [ordinary contract and retained state](https://github.com/jahala/o-o/blob/b0d5063e37b4eafdbc23c1899a31f1836168b989/example/anthropic-leadership.o-o.html), [AGI sentinel](https://github.com/jahala/o-o/blob/b0d5063e37b4eafdbc23c1899a31f1836168b989/example/agi-declared.o-o.html), [legal sentinel](https://github.com/jahala/o-o/blob/b0d5063e37b4eafdbc23c1899a31f1836168b989/example/trump-incarceration.o-o.html). Reported operation: representative retained state at the ordinary-contract anchor. | No material checkout access gap. External agent/runtime, providers, research pages and live demo are outside the frozen source. No observed-run or causal-experiment evidence was established. Sample retained content does not demonstrate execution provenance, factual accuracy, enforcement or costs. Uninspected article prose and styling remain available source, not access gaps. |
