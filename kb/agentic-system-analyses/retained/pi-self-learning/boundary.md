---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "pi-self-learning's complete extension package and memory loop at commit e0d76a93195b11b688ca71da8a8b5700c6541542."
run-id: AAS-2026-10-15-pi-self-learning-1a318610d4b1-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: e0d76a93195b11b688ca71da8a8b5700c6541542
analysis-cutoff: "2026-10-15"
evidence-tier: code-grounded
source:
  identity: https://github.com/mcollina/pi-self-learning
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/pi-self-learning-1a318610d4b1/related-systems/mcollina--pi-self-learning
  revision: e0d76a93195b11b688ca71da8a8b5700c6541542
  sha256: null
---

# pi-self-learning boundary

## Boundary and evidence

The target is the shipped pi-self-learning extension package, not the enclosing pi coding-agent runtime. Its intended use is retaining mistake-prevention reflections from coding sessions and making retained material available to later turns. It qualifies as a memory/knowledge/context-engineering system: the extension issues model calls, persists their parsed output, maintains derived memory files, and reloads retained text into host context (SRC-1, `extensions/self-learning.ts`; declared intent: `README.md`).

The boundary is **whole-system for this extension package**. It includes all shipped production, admission, persistence, maintenance and later-consumption paths, including the prompts embedded in TypeScript. It does not mean the whole pi host. Package metadata identifies the executable entry point:

> "main": "./extensions/self-learning.ts",
> --- `package.json`

The exported registration function connects the task-end producer to the host event and separately connects the future-turn consumer (SRC-1, `extensions/self-learning.ts`):

> export default function (pi: ExtensionAPI) {
>   pi.on("agent_end", async (event, ctx) => {
> --- `extensions/self-learning.ts`

> pi.on("before_agent_start", async (event, ctx) => {
> --- `extensions/self-learning.ts`

Inspection traced those hooks through branch-message selection, completed-turn gating, reflection and repair prompts, model/auth selection, JSON parsing, daily append, core-index updates, ranked core rendering, long-term rendering and optional Git commits. It also traced the consumer through file selection, bounded context bundling, runtime notes and system-prompt policy. Manual reflection, monthly summarization, global-memory redistillation, branch controls, model settings and status commands are included; they are shipped entry points, not excluded callers (SRC-1, `extensions/self-learning.ts`). The persistence-to-consumption connection is explicit:

> const dailyFile = appendDailyEntry(root, now, entry);
> const coreFiles = updateCoreFromReflection(root, parsed, Math.max(1, config.maxCoreItems || 20));
> --- `extensions/self-learning.ts`

> const bundle = buildMemoryContextBundle(root, config, ctx.cwd);
> if (bundle) pieces.push(bundle);
> --- `extensions/self-learning.ts`

### Tracked top-level coverage

All six top-level tracked entries were inspected completely. No material shipped path remains uninspected or deliberately excluded from the package boundary (SRC-1, paths below).

| Top-level tracked entry | Coverage | Material paths and role | Exclusion or evidence limit |
|---|---|---|---|
| `.gitignore` | Included; inspected | Ignores `.pi`, the default project configuration/memory area. | Actual user memory under that ignored area is not supplied; no conclusions about accumulated user memories. |
| `AGENTS.md` | Included; inspected as doctrine/design | Repository maintenance guidance, stated architecture and manual verification instructions. | Instructions are evidence of intent, not proof of execution or successful verification. |
| `README.md` | Included; inspected as doctrine/design | Installation, configuration, memory layout, loading policy and public commands. | Examples do not establish operational reliability. |
| `docs/` | Included; inspected | `docs/example-settings.json`: the sole tracked document in this directory; configuration example, including legacy automatic-reflection setting. | Configuration example, not a recorded deployment. |
| `extensions/` | Included; inspected as implementation and embedded doctrine/design | `extensions/self-learning.ts`: sole tracked extension; settings/path resolution, host session readers, reflection/repair/monthly/redistill prompts and model calls, parse/admission logic, Git persistence, core migration/ranking/rendering, context reload/policy, both event hooks and all nine command registrations. | Source supports implemented control flow, not observed model quality or actual host compliance. |
| `package.json` | Included; inspected | Package v0.5.0, extension/main registration, published-file selection and host peer dependency. | No scripts or evaluator entry point; does not establish host compatibility in practice. |

The tracked tree contains no evaluator, automated tests, recorded execution traces or experimental results. `AGENTS.md` explicitly reports the lack of an automated suite. Consequently this run can assess code and declared contracts but cannot establish reflection accuracy, measured prevention of mistakes, long-term memory utility, successful Git commits in a deployment, or causal improvement (SRC-1, `AGENTS.md`, `package.json`, `extensions/self-learning.ts`).

### External responsibilities and time boundary

External dependencies are pi's extension lifecycle, session manager, conversation conversion/serialization, model registry/auth and UI; the `@mariozechner/pi-ai` completion/model API and its providers; Node filesystem/process/path facilities; and the installed Git executable. These interfaces are visible at the extension's call sites, but their implementations and actual services are outside the frozen repository. The host owns the enclosing agent/tool loop and whether injected instructions are followed. Those responsibilities are not attributed to this package. No other repository is registered; this prevents conclusions about host internals, provider behavior, or end-to-end integration guarantees (SRC-1, `extensions/self-learning.ts`, `package.json`).

Evidence is frozen to Git commit `e0d76a93195b11b688ca71da8a8b5700c6541542` of `https://github.com/mcollina/pi-self-learning`, accessed read-only at the supplied checkout. The analysis applicability cutoff is 2026-10-15; later changes and moving linked documentation are excluded. The overall evidence tier is **code-grounded**, with package documentation and embedded model instructions supplying doctrine/design. No target execution was performed, and no observed-run or causal-experiment layer is claimed.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/mcollina/pi-self-learning` | e0d76a93195b11b688ca71da8a8b5700c6541542 | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/pi-self-learning-1a318610d4b1/related-systems/mcollina--pi-self-learning`. Implementation: complete `extensions/self-learning.ts` and `package.json`. Doctrine/design: complete `README.md`, `AGENTS.md`, `docs/example-settings.json`, embedded prompts/policy in `extensions/self-learning.ts`; repository context: `.gitignore`. All tracked files inspected. | Implementation: [extension](https://github.com/mcollina/pi-self-learning/blob/e0d76a93195b11b688ca71da8a8b5700c6541542/extensions/self-learning.ts), [package](https://github.com/mcollina/pi-self-learning/blob/e0d76a93195b11b688ca71da8a8b5700c6541542/package.json). Doctrine/design: [README](https://github.com/mcollina/pi-self-learning/blob/e0d76a93195b11b688ca71da8a8b5700c6541542/README.md), [agent guidance](https://github.com/mcollina/pi-self-learning/blob/e0d76a93195b11b688ca71da8a8b5700c6541542/AGENTS.md), [example settings](https://github.com/mcollina/pi-self-learning/blob/e0d76a93195b11b688ca71da8a8b5700c6541542/docs/example-settings.json), [ignore file](https://github.com/mcollina/pi-self-learning/blob/e0d76a93195b11b688ca71da8a8b5700c6541542/.gitignore). | No access gap in the tracked package. Host/dependency internals and actual generated memories are outside the source set; no supplied execution or experiment evidence. Implementation cannot establish successful deployment or learning effectiveness; doctrine/design cannot establish realized behavior. |
