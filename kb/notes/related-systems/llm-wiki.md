---
description: Claude Code plugin and portable AGENTS protocol for topic-isolated compiled markdown wikis, packaging ingest/research/query workflows as prompt artifacts rather than executable software
type: related-system
traits: [has-comparison, has-implementation, has-external-sources]
tags: [related-systems]
status: current
last-checked: 2026-04-06
---

# LLM Wiki

LLM Wiki is a Claude Code plugin plus a portable `AGENTS.md` "idea file" for building topic-isolated markdown wikis. The repo defines a wiki layout (`~/wiki/topics/<name>/` or `.wiki/`), a command surface for ingest/compile/query/research/thesis/assess/lint/output, and reference docs for indexing, ingestion, compilation, and linting. The notable architectural fact is that the repo is almost entirely promptware: the wiki system is described in markdown instructions and plugin metadata rather than implemented as an executable runtime with scripts, tests, or deterministic enforcement. That makes it a useful reference for packaging a knowledge-system protocol, but a weaker reference for hard guarantees about knowledge quality or workflow execution. The hub-plus-topic model is clearly the repo's center of gravity, but the project-local `.wiki/` mode matters as a smaller-scale topology variant rather than a mere footnote.

**Repository:** https://github.com/nvk/llm-wiki

## Core Ideas

**The repo ships a protocol, not a runtime.** The implementation is `AGENTS.md`, Claude plugin command files, one skill, and reference docs. That is still real implementation in the sense that a harness can load and follow it, but the behavior depends on agent compliance rather than on checked-in code that performs the operations directly.

**Topic-isolated sub-wikis are the main structural bet.** The hub at `~/wiki/` is only a registry plus log; all actual content lives in per-topic sub-wikis with separate `raw/`, `wiki/`, `output/`, `config.md`, `_index.md`, and `log.md`. A project-local `.wiki/` variant exists for single-repo use, but the design's default strong form is explicitly anti-monolith: one subject, one wiki, with sibling-peek only at the index level. In our terms, these topic wikis look a lot like long-lived research workshops: bounded sandboxes with raw intake, compiled intermediates, generated outputs, and an activity log rather than a mature shared library.

**`_index.md` is treated as the primary navigation substrate.** Every directory gets an index, and the references codify a three-hop strategy: master index, category index, then matched articles. This is the strongest mechanistic idea in the repo because it turns progressive disclosure into a repeatable file contract rather than leaving navigation entirely implicit. The payoff is clearest once the wiki is large or noisy enough that direct read/search loops stop being cheap; in a tiny local `.wiki/`, the extra hop can become mostly ceremony.

**Compilation is an agent-authored transformation over immutable raw sources.** Ingested material goes into `raw/` and is supposed to remain unchanged. The `compile` protocol tells the agent to synthesize cross-linked wiki articles with frontmatter, summaries, confidence scores, `See Also` links, and source backlinks. The transformation is real at the artifact level, even though the compiler is a prompted agent rather than a deterministic program.

**Research, thesis, and repo assessment are packaged as workflow templates.** The repo's most ambitious commands are not CRUD but multi-step inquiry loops: topic research with 5-10 parallel agents, thesis-driven evidence gathering with explicit pro/con roles, and repo-vs-wiki-vs-market assessment. These are strong workflow designs, but they remain prompt-level orchestration plans rather than scheduler-owned machinery.

**Obsidian compatibility is handled by duplicated link syntax rather than by a deeper shared substrate.** Cross-links are written in dual form: `[[wikilink]]` for Obsidian plus standard markdown for agents and GitHub. This is a pragmatic interoperability choice. It keeps one set of wiki articles readable across tools, but it also doubles part of the maintenance burden.

## Comparison with Our System

| Dimension | LLM Wiki | Commonplace |
|---|---|---|
| Primary shape | Prompt-packaged knowledge-system protocol: plugin commands, skill docs, and portable `AGENTS.md` | Repo-native knowledge base with notes, instructions, skills, scripts, and review workflows |
| Main content boundary | Separate topic sub-wikis outside the repo root, each with `raw/`, compiled `wiki/`, and `output/` | One repo with library artifacts (`kb/notes/`, `kb/instructions/`) plus workshop areas for in-flight work |
| Navigation model | Mandatory `_index.md` at every directory and explicit three-hop index traversal | Titles, descriptions, curated indexes, semantic link phrases, and search working together |
| Knowledge transformation | Agent compiles raw sources into synthesized wiki articles | Human and agent author notes directly; distillation is explicit but not framed mainly as raw -> compiled wiki |
| Governance | Prompt-defined lint rules, confidence labels, and "structural guardian" reminders | Deterministic validation, semantic review bundles, explicit note types, and stronger maintenance conventions |
| Link model | Dual-links for Obsidian plus markdown; navigational, not semantically typed | Standard markdown links with explicit relationship semantics |
| Portability story | Strong: Claude plugin for native use plus one-file `AGENTS.md` for other harnesses | Strong within agent repos, but less aggressively packaged as a portable single-file protocol |
| Research surface | First-class workflows for research, thesis investigation, and repo assessment | Stronger on curation and theory; research workflows exist but are less central to the day-to-day interface |

LLM Wiki is stronger where the task is "bootstrap a topic-specific research corpus quickly and keep the workflow legible to the agent." Commonplace is stronger where knowledge needs to be semantically linked, compositional, and checked by hard or at least harder oracles. The sharpest difference is that LLM Wiki concentrates intelligence in the prompt pack, while commonplace pushes more of the contract into durable artifacts and scripts. The topic wiki is therefore closer to one of our workshop packets than to one of our mature note collections: it is scoped, operational, and allowed to accumulate temporary structure in service of a research loop.

## Borrowable Ideas

**Ship a portable single-file protocol alongside harness-specific packaging.** LLM Wiki's `AGENTS.md` gives the system a clean export format independent of Claude plugin support. This is ready to borrow now as a distribution pattern for any stable methodology we want to share outside this repo.

**Borrow the research skill design, not just the command names.** `research`, `thesis`, and `assess` are genuinely different workflows: topic mode uses angle-based swarms, question mode decomposes into sub-questions, thesis mode assigns explicit support/opposition/mechanistic/meta roles, and `--min-time` turns the whole thing into a multi-round loop. That is stronger than a single generic "do deep research" prompt. Ready to borrow now for workshop-scale investigations and survey packets.

**Treat repo assessment as a first-class downstream operation of a knowledge base.** The `assess` command is a concrete pattern: compare an implementation against accumulated research and the market, then file the result back into the KB. Ready to borrow now for comparative analysis tasks and workshop packets.

**Use topic-isolated sub-wikis when research corpora would otherwise contaminate each other.** The hub-plus-topics layout is a serious answer to cross-topic noise, and the closest analogue on our side is a workshop rather than a library area. We should not adopt it broadly inside commonplace's main library, but it is a credible pattern for temporary survey corpora or long-lived domain sandboxes. The awkward middle case is overlapping domains: the repo mostly chooses separation plus sibling-index peeks rather than richer cross-wiki synthesis. Needs a concrete use case first.

**Make the navigation contract explicit in reference docs, not just in habit.** LLM Wiki's indexing reference spells out the three-hop read strategy and when indexes must be updated. We already rely on similar ideas, but packaging the navigation discipline as a named protocol is itself borrowable. Ready to borrow now where a workflow depends heavily on derived navigational artifacts.

## Curiosity Pass

**The prompt-packaged-protocol claim produces portability, not strong enforcement.** The mechanism is real: a plugin loader or agent can ingest these markdown instructions and act on them. But the simpler alternative is a single README or ad hoc prompt collection. What LLM Wiki adds is structured packaging and role-separated command surfaces, not runtime guarantees. Even if the system works perfectly, its ceiling is bounded by agent obedience and prompt clarity rather than by executable invariants.

**Topic isolation is genuine constraining, not just naming.** The property is reduced cross-topic interference. The mechanism really does change the shape of the artifact space: separate directories, separate logs, separate indexes, sibling-peek only at `_index.md`. The simpler alternative is one big wiki with tags. LLM Wiki earns the added structure if the topics are broad enough, but it likely becomes overhead for smaller or highly overlapping corpora.

**The index-first strategy is real distillation with an obvious failure mode.** `_index.md` transforms a directory into a cheap decision surface by extracting summaries, tags, and categories. That is genuine representation change, not relocation. But the simpler alternative is `rg` plus filenames, and the ceiling is maintenance quality: once the index is stale, the whole navigation model becomes misleading. The repo names index maintenance repeatedly, which suggests this risk is central even in the protocol's own self-conception.

**"Compiler" is partly the right metaphor and partly flattering rhetoric.** Raw sources becoming synthesized wiki articles is a true transformation. But a compiler usually implies a stable executable procedure with deterministic syntax/semantic checks. Here the "compiler" is a prompted agent following prose rules. The simpler alternative is retrieval-time answer synthesis directly from raw sources. LLM Wiki's compile step earns itself by producing reusable intermediate artifacts, but it does not yet have compiler-like guarantees.

**Confidence scores and the structural guardian mostly relocate judgment into frontmatter and reminders.** The property claimed is trust and self-maintenance. Mechanistically, the repo gives criteria for `high|medium|low` confidence and a checklist for automatic cleanup, but there is no checked-in code that enforces those criteria or even verifies that they were applied consistently. The simpler alternative is to omit the labels and be explicit in prose. As shipped, these mechanisms provide posture more than reliable epistemic control.

**The multi-agent research counts are workflow designs, not software capabilities.** Five, eight, or ten agents can exist if the host harness supports subagents and the invoking model follows the command file faithfully. That is not nothing, but it means the repo's most impressive claims are contingent on external runtime features. The practical question is whether those workflows produce consistently better wikis than a smaller, tighter loop would. The current repo does not contain evidence either way.

## What to Watch

- Whether the repo grows executable helpers, tests, or deterministic validators that harden the current prompt contracts into software guarantees
- Whether `_index.md` maintenance remains tractable as real topic wikis accumulate hundreds of sources and articles
- Whether confidence scoring and structural-guardian claims stay mostly rhetorical or become backed by stronger checks
- Whether the portable `AGENTS.md` version remains genuinely cross-harness, or drifts toward Claude-specific assumptions despite the portability pitch
- Whether thesis and research modes produce durable compiled knowledge or mostly generate fast-moving wiki sprawl

---

Relevant Notes:

- [Skills are instructions plus routing and execution policy](../skills-are-instructions-plus-routing-and-execution-policy.md) — exemplifies: LLM Wiki ships both a portable instruction artifact (`AGENTS.md`) and a harness-specific command/skill package
- [Instruction specificity should match loading frequency](../instruction-specificity-should-match-loading-frequency.md) — extends: the Claude plugin packaging especially uses the same layered pattern of slim always-loaded metadata plus on-demand detailed procedures
- [Agents navigate by deciding what to read next](../agents-navigate-by-deciding-what-to-read-next.md) — exemplifies: the `_index.md` first-hop contract is a direct implementation of pointer-first navigation
- [Stale indexes are worse than no indexes](../stale-indexes-are-worse-than-no-indexes.md) — warns: LLM Wiki's index-first navigation inherits exactly this failure mode if `_index.md` stops being exhaustive
- [Files beat a database for agent-operated knowledge bases](../files-not-database.md) — aligns: LLM Wiki keeps the knowledge interface in readable files and treats structure as a convention layered on top
- [A functioning knowledge base needs a workshop layer, not just a library](../a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — extends: LLM Wiki's topic sub-wikis behave more like bounded research workshops with their own raw intake, outputs, and logs than like mature shared library collections
- [Napkin](./napkin.md) — compares: both are Obsidian-aware markdown systems, but Napkin ships executable CLI mechanics where LLM Wiki mostly ships protocol and prompt packaging
- [browzy.ai](./browzy-ai.md) — compares: both compile raw sources into a wiki, but browzy includes a real runtime and derived SQLite retrieval layer
- [OpenViking](./openviking.md) — contrasts: both formalize progressive disclosure, but OpenViking bakes it into a storage service while LLM Wiki expresses it as file conventions and agent instructions
