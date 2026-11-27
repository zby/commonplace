# Consulting Commonplace for another agentic system

Use this page when you are working on an external or private agentic system and want transferable design advice, diagnostic lenses, or real-system comparisons from Commonplace — without installing Commonplace or adopting its file layout.

## What transfers and what does not

Read each section of the site according to its authority:

- **Transferable theory and problem maps:** [Theory](./theory/README.md), [Theory questions](./theory/questions/README.md), and [Articles](./articles/README.md). Claims state mechanisms and design-space tradeoffs. Always check `## Scope` or `## Caveats`, and distinguish corroborated claims from explicitly stated conjectures.
- **Empirical comparisons of external systems:** [Comparisons](./agentic-systems/comparisons/README.md) and [Research topics](./agentic-systems/topics/README.md) inspect real agent runtimes, memory layers, verification loops, and workflows. Use these to see concrete implementations and failure modes behind the theory.
- **One worked implementation (do not copy blindly):** [Reference](./reference/README.md) and [Instructions](./instructions/README.md) document Commonplace's own choices (file-backed Markdown KB, CLI validators, review workflows). Borrow a mechanism only when its assumptions match your system.
- **Do not cite as settled doctrine:** `work/` holds in-flight exploratory drafts; `theory/proposals/` holds unadopted theory; `agent-memory-systems/` is a frozen legacy survey superseded by [Agentic Systems](./agentic-systems/README.md).

Commonplace focuses on agent memory, context engineering, prompt-vs-code boundaries, LLM evaluation and review, orchestration, and continual learning outside model weights. It does not cover model pretraining/RLHF, UI design, or general infrastructure scaling.

## Start from your problem

Match the symptom or design decision in your system to the right entry points (in plain engineering terms, before learning Commonplace's vocabulary):

| Problem in your system | Start here | Concrete comparisons / anchor notes |
|---|---|---|
| Agents ignore rules in prompts, `AGENTS.md`, or memory | [Context engineering](./tags/context-engineering-README.md) | [Knowledge storage does not imply contextual activation](./theory/knowledge-storage-does-not-imply-contextual-activation.md), [Always-loaded context mechanisms](./theory/always-loaded-context-mechanisms-in-agent-harnesses.md) |
| Deciding whether behavior belongs in code, prompts, or skills | [Constraining](./tags/constraining-README.md), [Artifact analysis](./tags/artifact-analysis-README.md) | [Scheduler–LLM separation](./theory/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md), [Codification and relaxing](./theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) |
| Designing or fixing cross-session agent memory | [Agent memory](./tags/agent-memory-README.md) | [Agent memory requirements](./theory/agent-memory-requirements/README.md), [Memory comparisons](./agentic-systems/comparisons/README.md#agent-memory), [Memory topic](./agentic-systems/topics/memory.md) |
| Growing prose, prompt, rule, or memory bloat | [Curation](./tags/curation-README.md), [KB maintenance](./tags/kb-maintenance-README.md) | [How do we fight bloat?](./theory/questions/how-do-we-fight-bloat-in-agent-produced-systems.md), [How do we value notes?](./theory/questions/how-do-we-value-notes.md) |
| Noisy, drifting, or Goodharted LLM judges and evals | [Evaluation](./tags/evaluation-README.md), [LLM reliability](./tags/llm-reliability-README.md) | [Oracle strength spectrum](./theory/oracle-strength-spectrum.md), [Three-way output deviation diagnosis](./theory/llm-output-deviation-requires-three-way-diagnosis.md), [Knowledge & verification topic](./agentic-systems/topics/epistemic.md) |
| Multi-agent isolation, handoffs, or lost global priorities | [Architecture](./tags/architecture-README.md) | [Context isolation vs. global prioritization](./theory/context-isolation-for-focus-conflicts-with-global-prioritization.md), [Privilege quarantine](./theory/orchestration-needs-privilege-quarantine-not-permission-scope.md), [Runtime topic](./agentic-systems/topics/runtime.md), [Workflow topic](./agentic-systems/topics/workflow.md) |
| Making a deployed system improve across runs without fine-tuning | [Continual learning](./tags/continual-learning-README.md), [Self-improving systems](./tags/self-improving-systems-README.md) | [Selection-based learning overview](./index.md#research-selection-based-learning) |
| Structuring, validating, or testing natural-language specs and docs | [Document system](./tags/document-system-README.md) | [Type system](./tags/type-system-README.md) |

For the complete topic map, see [Tags](./tags/README.md).

## Diagnostic lenses to run on your system

Rather than summarizing general principles, apply one of these concrete frameworks to your architecture:

1. **Artifact analysis ([Axes of artifact analysis](./theory/axes-of-artifact-analysis.md)):** List every piece of retained state in your system (prompts, memory entries, indexes, schemas, validators, learned policies) and classify each by *storage substrate*, *representational form*, *lineage*, and *behavioral authority* (consumer, channel, force). This exposes drift, missing review paths, and unowned authority.
2. **Memory coverage audit ([Agent memory requirements](./theory/agent-memory-requirements/README.md)):** Check your memory layer against the 11 operational requirements (capture, import, raw-evidence preservation, trace extraction, multi-consumer surfaces, activation, promotion, compiled-view alignment, retirement/relaxation, explicit authority, effect-based evaluation).
3. **Runtime decomposition ([Separate scheduling, context, and state](./theory/agent-runtime-analysis-should-separate-scheduling-context-state.md)):** Separate what schedules turns, what assembles context, and what holds durable state to spot hidden schedulers and ungoverned control surfaces.
4. **Failure and oracle triage ([Three-way deviation diagnosis](./theory/llm-output-deviation-requires-three-way-diagnosis.md) & [Oracle strength spectrum](./theory/oracle-strength-spectrum.md)):** Separate *underspecification* (missing spec), *interpreter failure* (model missed the spec), and *indeterminism* (sampling variance), then match automation autonomy to actual oracle strength.
5. **Codify-vs-relax check ([Relaxing candidate signals](./theory/operational-signals-that-a-component-is-a-relaxing-candidate.md)):** Test rigid rules and scripts for paraphrase brittleness, unit-vs-integration gaps, and process-over-outcome constraints to decide what to harden into code and what to relax back into LLM judgment.
6. **Real-system cross-check ([Comparisons](./agentic-systems/comparisons/README.md)):** Compare your candidate design against inspected systems in [Memory](./agentic-systems/topics/memory.md), [Runtime](./agentic-systems/topics/runtime.md), [Epistemic](./agentic-systems/topics/epistemic.md), and [Workflow](./agentic-systems/topics/workflow.md).

## Reading efficiently

- **Use the rendered HTML pages by default.** Page chrome is small, links and redirects resolve automatically, and collection/tag navigation links are included.
- **Start with curated [tag heads](./tags/README.md).** Each head explains what qualifies and picks the load-bearing entries; open full member lists or directory listings only when you need exhaustive coverage.
- **Markdown companions are optional.** Every published page links to `View as Markdown` if you want raw YAML frontmatter. Note that links inside raw `.md` files are relative to that `.md` file's URL under `/commonplace/`, and links climbing above `kb/` (such as `src/` or `INSTALL.md`) live on GitHub rather than on this site.
- **Need broad search across descriptions?** If you have a shell, `git clone --depth 1 https://github.com/zby/commonplace.git` followed by `rg "^description:" kb/theory/` is faster than multi-hop HTTP browsing.

## Giving advice back to your project

Cite the specific Commonplace pages you relied on, preserve their stated scope limits and caveats, and explicitly separate what Commonplace's evidence supports from what you are extrapolating to your system's constraints.
