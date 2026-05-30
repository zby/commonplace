---
description: "Static Agent Skills collection for context engineering: plugin-packaged instructional artifacts with progressive disclosure, activation triggers, examples, and no runtime memory learner"
type: ../types/agent-memory-system-review.md
status: current
last-checked: "2026-05-16"
---

# Agent Skills for Context Engineering

Agent Skills for Context Engineering is Muratcan Koylan's open repository of Claude Code/Open Plugins skills for context engineering, multi-agent architecture, memory-system design, tool design, evaluation, hosted agents, and related agent-building practices. It is best understood as a library of instructional artifacts: when a compatible agent loads a skill, that skill acts as a system-definition artifact with advisory/instructional force; when a human or agent reads the same files as background documentation, they are ordinary knowledge artifacts. The repository does not implement an automated memory substrate or trace-derived skill learner.

**Repository:** https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering

**Reviewed revision:** [7a95d94c364e25c869a86896a45791dfda6db8bf](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/commit/7a95d94c364e25c869a86896a45791dfda6db8bf)

## Core Ideas

**Skills are the retained behavior-shaping unit.** The repository's durable artifacts are `SKILL.md` files with YAML frontmatter names and descriptions, plus optional references and scripts. The root skill describes a collection-level skill map and activation scope, while the marketplace manifest packages fourteen skill directories into one Claude Code plugin. The storage substrate is a git repository; the representational form is mostly prose with small symbolic manifests and example scripts; the behavioral authority depends on consumption path: instruction when loaded by an agent, reference when browsed as documentation. See the root [`SKILL.md`](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/7a95d94c364e25c869a86896a45791dfda6db8bf/SKILL.md) and [Claude plugin manifest](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/7a95d94c364e25c869a86896a45791dfda6db8bf/.claude-plugin/marketplace.json).

**Progressive disclosure is both content and distribution architecture.** The README and root skill say agents should load names and descriptions first, full skill bodies on activation, and references only when needed. The context-fundamentals skill repeats this as a three-level design rule: skill selection, document loading, and tool-result retention. The same pattern appears in the digital-brain example, which demonstrates SKILL metadata, module instructions, and data files as separate loading layers. This is the repository's clearest memory-adjacent contribution: it treats durable instructions as externally stored context that becomes behavior-changing only when activated. See the [README](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/7a95d94c364e25c869a86896a45791dfda6db8bf/README.md), [context-fundamentals skill](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/7a95d94c364e25c869a86896a45791dfda6db8bf/skills/context-fundamentals/SKILL.md), and [digital-brain skill](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/7a95d94c364e25c869a86896a45791dfda6db8bf/examples/digital-brain-skill/SKILL.md).

**Activation triggers are explicit routing metadata, not learned retrieval.** Each skill frontmatter description names when it should be used, and the README includes a trigger table mapping phrases such as "compress context", "build knowledge graph", or "evaluate agent performance" to specific skills. That makes activation inspectable and portable across skill-aware hosts, but it is static metadata. There is no local router, embedding index, ranker, or feedback loop in this repo that tunes trigger precision from outcomes. See the README's [skill trigger table](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/7a95d94c364e25c869a86896a45791dfda6db8bf/README.md) and example skill frontmatter in [`memory-systems/SKILL.md`](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/7a95d94c364e25c869a86896a45791dfda6db8bf/skills/memory-systems/SKILL.md).

**The context-management claims are practical teaching claims.** The skills repeatedly frame context as a limited attention budget, recommend just-in-time file loading, warn about lost-in-middle and context poisoning, and advise compaction before the window is exhausted. The filesystem-context skill is especially close to commonplace's domain: it recommends scratch files, plan persistence, sub-agent workspaces, dynamic skill loading, and selective `ls`/`glob`/`grep`/read access. These are prescriptive patterns rather than an implemented runtime. See [`context-degradation/SKILL.md`](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/7a95d94c364e25c869a86896a45791dfda6db8bf/skills/context-degradation/SKILL.md), [`context-optimization/SKILL.md`](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/7a95d94c364e25c869a86896a45791dfda6db8bf/skills/context-optimization/SKILL.md), and [`filesystem-context/SKILL.md`](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/7a95d94c364e25c869a86896a45791dfda6db8bf/skills/filesystem-context/SKILL.md).

**Evaluation guidance is instruction-first, with demonstration code as support.** The evaluation and advanced-evaluation skills recommend outcome-focused evaluation, multidimensional rubrics, LLM-as-judge pipelines, bias mitigation, human review, complexity-stratified test sets, and continuous monitoring. Some skills include scripts, but the code is mostly illustrative or scaffold-like: for example, the compression evaluator says LLM judge calls are stubbed and token estimation uses simplified heuristics. The repository teaches evaluation and offers examples; it does not run a repository-level benchmark or gate skill changes with automated evals. See [`evaluation/SKILL.md`](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/7a95d94c364e25c869a86896a45791dfda6db8bf/skills/evaluation/SKILL.md), [`advanced-evaluation/SKILL.md`](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/7a95d94c364e25c869a86896a45791dfda6db8bf/skills/advanced-evaluation/SKILL.md), and [`compression_evaluator.py`](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/7a95d94c364e25c869a86896a45791dfda6db8bf/skills/context-compression/scripts/compression_evaluator.py).

**Examples show applied designs rather than shared runtime machinery.** The digital-brain example is the most concrete memory-like artifact: it uses module isolation, JSONL logs, YAML configs, markdown narrative files, append-only history, and helper scripts for reviews and content ideas. But it is an example skill package, not a service that the main repository operates. The same is true of the TypeScript LLM-as-judge example: it has its own `package.json`, tests, and build scripts under `examples/`, separate from any top-level runtime. See the [digital-brain file tree](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/7a95d94c364e25c869a86896a45791dfda6db8bf/examples/digital-brain-skill), [digital-brain skills mapping](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/7a95d94c364e25c869a86896a45791dfda6db8bf/examples/digital-brain-skill/SKILLS-MAPPING.md), and [`examples/llm-as-judge-skills/package.json`](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/7a95d94c364e25c869a86896a45791dfda6db8bf/examples/llm-as-judge-skills/package.json).

## Comparison with Our System

| Dimension | Agent Skills for Context Engineering | Commonplace |
|---|---|---|
| Primary artifact | Agent Skills: prose instructions with frontmatter and optional references/scripts | Typed KB notes, instructions, reviews, indexes, and validation rules |
| Storage substrate | Git repository distributed as Claude/Open Plugins skill package | Git repository as both methodology KB and shipped framework source |
| Behavioral authority | Skills instruct agents when activated; docs/examples advise when read | Instructions/skills guide agents; notes provide conceptual evidence; validators enforce contracts |
| Activation | Static descriptions and trigger phrases, host-mediated loading | `rg`, indexes, descriptions, authored links, and skill trigger descriptions |
| Memory mechanism | Teaches memory and filesystem patterns; does not provide a live memory runtime | Maintains a file-backed KB with type contracts, generated indexes, review workflows, and validation |
| Learning loop | Manual authoring and examples; no trace-derived skill evolution in the inspected code | Manual and agent-assisted distillation into notes, instructions, skills, scripts, and reviews |
| Evaluation | Evaluation skills and demo code, mostly prescriptive | Validation commands, review system, and semantic review workflows around KB artifacts |

The strongest alignment is the shared belief that agent memory is context engineering, not just storage. Both systems value progressive disclosure, inspectable files, skill-like procedural artifacts, and evaluation by downstream behavior. The difference is where the machinery lives. This repo packages context-engineering methodology as a set of static, loadable instructions. Commonplace turns methodology into a typed knowledge base with collection contracts, directory indexes, validation, review gates, and explicit source/link semantics.

The biggest divergence is authority and lifecycle. Agent Skills for Context Engineering has clear instructions but weak lifecycle machinery: there is no canonical promotion path from observation to durable note to skill to validator, no repository-level review state, and no automated regeneration/invalidation path for derived views. Commonplace is heavier because it treats artifact lifecycle as part of the system, not just authoring hygiene.

This review should therefore not classify the repository as an automated memory learner. It is a useful library about context engineering and memory systems, plus a distribution vehicle for those instructions. Its retained artifacts can change future agent behavior when loaded, but the repo does not itself observe agent traces, extract lessons, rewrite skills, or rank memories from usage.

**Read-back:** push — host trigger metadata loads relevant skill instructions into the agent's context.

## Borrowable Ideas

**Collection-level skill packaging.** The marketplace manifest bundles related skills as one plugin while keeping individual skill directories separate. Commonplace could use the same packaging idea for installable topical bundles, especially where one conceptual area spans several skills. Ready to borrow when distribution becomes a product concern.

**Trigger tables as human-auditable routing specs.** The README's skill-trigger matrix is simple, but it makes activation expectations visible. Commonplace skills could maintain compact should-load phrase sets beside descriptions, not as a learned router but as reviewable intent. Ready to borrow now for skills whose activation boundaries are fuzzy.

**Examples that map design decisions back to skills.** The digital-brain example's `SKILLS-MAPPING.md` is a useful lineage surface: it says which source skill justified each architectural choice. Commonplace could apply this pattern when examples or templates embody methodology from several notes. Ready to borrow for richer examples.

**Evaluation advice packaged as agent-operable instruction.** The evaluation skills are not a runtime gate, but they are good examples of turning evaluation methodology into a loadable instruction surface. Commonplace already has validation and review workflows; the borrowable part is making evaluation design itself available as a skill when agents build new evals. Ready to borrow selectively.

**Keep skill bodies compact and move depth behind references.** The repository's authoring rules in `CLAUDE.md` require skill bodies to stay under 500 lines and move detail into references. That is a concrete version of progressive disclosure. Commonplace already follows this in places; the explicit line-budget heuristic is worth considering for skill authoring guidance.

## Curiosity Pass

**The repository's claims are stronger than its machinery.** Many skills talk about production-grade systems, continuous evaluation, memory consolidation, and self-modification safeguards. The repository mostly supplies prose guidance and demonstration scripts, not the production substrate those skills describe. That is fine for an instructional library, but reviews should not confuse described architecture with implemented architecture.

**Static skills are still real retained behavior.** The absence of automated learning does not make the repo irrelevant to agent memory. A loaded skill is retained state that can alter future action through instruction. The correct classification is static system-definition artifacts, not "not memory at all."

**Skill activation is only as good as the host.** The repo declares descriptions and trigger phrases, but actual discovery is delegated to Claude Code, Cursor/Open Plugins, or whatever compatible host loads the plugin. There is no local fallback if the host fails to activate the right skill or activates too many adjacent skills.

**The examples may be more operationally valuable than the core skills.** The digital-brain example makes progressive disclosure, file-backed memory, append-only logs, and module isolation concrete. For commonplace, that example is a better comparison point for applied file-backed context design than the general memory-systems skill, which is mostly a framework survey and decision guide.

## What to Watch

- Whether the repository adds a real skill-improvement loop: captured task traces, labeled failures, skill diffs, holdout tests, and promotion rules.
- Whether activation moves beyond static descriptions into evaluated should-trigger/should-not-trigger sets.
- Whether example scripts graduate from demonstrations into tested reusable tools with versioned interfaces.
- Whether the Open Plugins/Claude marketplace packaging remains the main distribution surface or the skills become portable across more agent hosts.
- Whether the memory-systems skill gains code-grounded examples that clarify what the repository itself endorses versus what it merely surveys.

---

Relevant Notes:

- [Context efficiency is the central design concern in agent systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) - foundation: the repository's skills repeatedly treat attention budget and signal density as the core design constraint
- [Instruction specificity should match loading frequency](../../notes/instruction-specificity-should-match-loading-frequency.md) - exemplifies: skill descriptions stay cheap and always visible while full procedures load only on activation
- [Skills derive from methodology through distillation](../../notes/skills-derive-from-methodology-through-distillation.md) - exemplifies: the repository packages context-engineering methodology as loadable skills
- [System-definition artifacts are crystallized reasoning under context](../../notes/system-definition-artifacts-are-crystallized-reasoning-under-context.md) - clarifies: these skills have behavior-shaping authority when an agent consumes them as instructions
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) and [system-definition artifact](../../notes/definitions/system-definition-artifact.md) - vocabulary: the same file can advise as reference or instruct as a loaded skill depending on the consumption channel
