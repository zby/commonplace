---
description: "Letta Context Constitution review: authored prose policy for token-space learning, context hierarchy, MemFS affordances, and agent self-management"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
status: current
last-checked: "2026-06-01"
---

# Context Constitution

Context Constitution, from Letta, is a documentation repository for an agent-facing policy about token-space continual learning. The inspected repository contains the public README, the constitution itself, an affordances document, a CC0 license, and a whitespace-check workflow. It is not an implementation of Letta Code or MemFS; it is authored prose that describes how Letta agents should manage context, identity, memory, skills, messages, compaction, and memory-maintenance subagents.

**Repository:** https://github.com/letta-ai/context-constitution

**Reviewed commit:** [0f0a23b66c262f41ce7e060a4da628dc983fb24f](https://github.com/letta-ai/context-constitution/commit/0f0a23b66c262f41ce7e060a4da628dc983fb24f)

**Last checked:** 2026-06-01

## Core Ideas

**The repository is a policy artifact, not a memory runtime.** The source tree is small: `README.md`, `constitution/CONSTITUTION.md`, `constitution/AFFORDANCES.md`, `LICENSE`, and a GitHub Actions whitespace check. The README says Letta uses the constitution internally as a foundation for prompting and for training memory-native models, but this repository does not include the harness code, training code, memory database, retrieval service, or prompt assembly path that would verify that deployment claim ([README.md](https://github.com/letta-ai/context-constitution/blob/0f0a23b66c262f41ce7e060a4da628dc983fb24f/README.md), [check-whitespace.yml](https://github.com/letta-ai/context-constitution/blob/0f0a23b66c262f41ce7e060a4da628dc983fb24f/.github/workflows/check-whitespace.yml)).

**Learning is framed as self-management of context, not weight updates.** The constitution argues that Letta agents learn by actively curating token-space representations of identity, memory, and knowledge. The behavior-changing substrate is the context window plus retrievable external context, especially the system prompt, messages, tools, and skills ([CONSTITUTION.md](https://github.com/letta-ai/context-constitution/blob/0f0a23b66c262f41ce7e060a4da628dc983fb24f/constitution/CONSTITUTION.md)).

**The system prompt is the highest-authority retained surface in the story.** The constitution treats the system prompt as the compact, always-present program of the agent's identity and memory. It instructs agents to update prompts incrementally when learnings become durable, while avoiding rote event memorization in favor of generalized future guidance ([CONSTITUTION.md](https://github.com/letta-ai/context-constitution/blob/0f0a23b66c262f41ce7e060a4da628dc983fb24f/constitution/CONSTITUTION.md)).

**Progressive disclosure is the main context-efficiency mechanism.** The document tells agents to keep compact summaries, indexes, file descriptions, skill metadata, and references in context, then load full memory files, skills, retrieved records, or message history only when the current task demands them. It explicitly treats context efficiency as both token-volume control and complexity control: stale skills, redundant instructions, raw history, and unnecessary full documents should leave the active window ([CONSTITUTION.md](https://github.com/letta-ai/context-constitution/blob/0f0a23b66c262f41ce7e060a4da628dc983fb24f/constitution/CONSTITUTION.md)).

**The affordances document describes a filesystem projection of memory.** `AFFORDANCES.md` says newer Letta agents have memory blocks projected into a local memory filesystem, with `/system` representing in-context memories and other directories representing external memories. Changes are described as git-tracked and propagated to the true underlying memory blocks only after a successful push. The review should treat this as a described host affordance, not code implemented in this repository ([AFFORDANCES.md](https://github.com/letta-ai/context-constitution/blob/0f0a23b66c262f41ce7e060a4da628dc983fb24f/constitution/AFFORDANCES.md)).

**Message history and subagents are part of the memory-maintenance model.** The affordances document says conversations have persisted, searchable message histories; old in-context messages are compacted into summaries; multiple concurrent conversations can share memory; and specialized recall, reflection, and defragmentation subagents can manage memory without occupying the primary task context ([AFFORDANCES.md](https://github.com/letta-ai/context-constitution/blob/0f0a23b66c262f41ce7e060a4da628dc983fb24f/constitution/AFFORDANCES.md)).

**The public governance surface is intentionally lightweight.** The repo invites feedback through GitHub issues and releases the text under CC0. The only executable check in the inspected source enforces trailing whitespace in Markdown files; there are no schemas, policy tests, examples of prompt assembly, or validation rules for whether an agent follows the constitution ([README.md](https://github.com/letta-ai/context-constitution/blob/0f0a23b66c262f41ce7e060a4da628dc983fb24f/README.md), [LICENSE](https://github.com/letta-ai/context-constitution/blob/0f0a23b66c262f41ce7e060a4da628dc983fb24f/LICENSE)).

## Artifact analysis

- **Storage substrate:** `files` — GitHub-hosted Markdown in `constitution/CONSTITUTION.md`
- **Representational form:** `prose` — Prose
- **Lineage:** `authored` `trace-extracted` — the public policy and workflow are authored, while the described host memory surfaces include agent-authored edits and conversation-derived compaction summaries
- **Behavioral authority:** `knowledge` `instruction` `routing` `validation` `learning` — the public docs are reference material; prompt inclusion, context hierarchy, MemFS routing, whitespace CI, and claimed training use give the described consumption paths stronger authority

**Constitution prose.** The storage substrate is GitHub-hosted Markdown in `constitution/CONSTITUTION.md`. Its representational form is prose. Its lineage is authored public policy, not generated output, trace-extracted memory, or compiled configuration. As a public document it is a knowledge artifact: readers can use it as reference and rationale for Letta's context-management philosophy. When Letta inserts the same or derived text into an agent prompt or training corpus, it becomes a system-definition artifact with instruction or learning authority, but that consumption path is asserted in the README rather than implemented in this repository.

**Affordances prose.** The storage substrate is GitHub-hosted Markdown in `constitution/AFFORDANCES.md`. The representational form is mostly prose with some path and layout conventions, such as `/system`, `/skills`, skill metadata, external memory metadata, message history, and named subagents. Its lineage is authored descriptive guidance about a host harness. Its behavioral authority is split: inside this repo it is a knowledge artifact describing available affordances; in a running Letta system, the described MemFS layout, metadata injection, compaction, and subagent affordances would be system-definition artifacts implemented by the harness.

**Described memory filesystem and message store.** These are not stored in the reviewed repo, but they are the central retained surfaces described by the docs. The claimed storage substrate is an underlying Letta memory-block store projected to local files, plus persisted and indexed message history. The representational form is mixed: prose files and summaries, symbolic filesystem paths and metadata, git commits, and searchable message indexes. The described lineage is partly authored by the agent through file edits and partly derived from prior conversations through compaction and summaries. The described behavioral authority depends on location: `/system` memories have always-loaded prompt authority, external memory has pull-accessible advisory authority until loaded, and compaction summaries can shape future conversation state.

**Whitespace workflow.** The `.github/workflows/check-whitespace.yml` file is a symbolic CI artifact. Its storage substrate is GitHub Actions configuration in the repo, its lineage is authored project maintenance code, and its behavioral authority is validation authority over Markdown formatting. It does not validate semantic fidelity, prompt effects, memory quality, or context-management compliance.

**Promotion path.** The conceptual promotion path is clear even though not implemented here: experience can become a message-history record, then a summary or external memory reference, then a more durable system-prompt learning. That path crosses authority boundaries from knowledge artifact to system-definition artifact. The repo does not provide a validator, review gate, or provenance schema for that promotion.

## Comparison with Our System

| Dimension | Context Constitution | Commonplace |
|---|---|---|
| Primary purpose | Agent-facing policy for token-space learning and context self-management | Agent-operated methodology KB with typed artifacts, validation, review, and source-grounded notes |
| Storage substrate | Public Markdown repository; described host memory lives outside the repo | Git-tracked Markdown collections, schemas, generated indexes, source snapshots, and review outputs |
| Representational form | Prose policy plus a small symbolic CI workflow | Typed prose, frontmatter, links, schemas, commands, indexes, and validation code |
| Lineage | Authored public documents; no trace-derived pipeline in the repo | Source-pinned artifacts, replacement history, generated indexes, validation and review reports |
| Activation model | Prompt/policy text when included by a host harness; external memory is described as actively retrieved | Pull through `rg`, indexes, links, and skills; push-like authority through instructions, type specs, and validation gates |
| Governance | CC0 text, GitHub feedback, whitespace check | Collection contracts, type specs, deterministic validation, review bundles, status fields, and curated links |

Context Constitution and Commonplace share a strong view that context is architecture. Both care about progressive disclosure, explicit indexes, metadata that lets an agent decide what to load, and a split between always-present context and external retrievable context. The difference is authority discipline. Context Constitution is written directly to agents and treats prompt editing as the central learning mechanism. Commonplace separates retained artifacts into notes, references, instructions, type specs, reports, and generated indexes so that stronger authority travels through more inspectable forms.

The Letta framing is more agent-autonomy-forward: the agent owns its context, modifies its prompt, curates identity, and uses reflection or defragmentation subagents to improve itself over time. Commonplace is more library-and-governance-forward: an agent can write and revise artifacts, but type contracts, validation, citations, review states, and git history constrain what receives durable authority.

The biggest comparison risk is over-reading the source. The documents describe a rich harness with MemFS, message search, compaction, multi-conversation memory, and subagents. This repository does not implement those pieces, so the review can credit the design vocabulary and policy shape but not the runtime behavior.

**Read-back:** `both` — The described Letta harness coarsely push-loads retained `/system` memory in the prompt, while external memory files and message history require agent pull; the constitution itself is shipped policy text, a baseline context surface rather than read-back, and no implemented relevance-gated push activation is present in this repo

**Read-back signal:** `coarse` — the only push read-back evidenced in the review is always-loaded retained `/system` memory; external memory files and message history remain pull surfaces

**Faithfulness tested:** `no` — the reviewed repository has no implementation, ablation, or policy-following test showing that pushed memory changes behavior

### Borrowable Ideas

**State the context hierarchy in agent-facing prose.** Commonplace already has collection contracts and navigation guidance, but the constitution is a useful example of telling the agent what kinds of context exist, which ones are always active, which ones are external, and why that matters. Ready now for high-level instruction cleanup.

**Treat prompt edits as authority promotions.** The constitution's strongest practical idea is that not every memory belongs in the system prompt. Commonplace can use the same framing for workshop outputs: a finding can remain a note, become an index entry, become an instruction, or eventually become validation code. Ready as vocabulary; automation needs stronger review gates.

**Use filesystem projection for agent-owned context.** The described MemFS pattern is close to Commonplace's git-native preference, but applied to an individual agent's own prompt and external memory. Worth borrowing only where a real runtime needs agents to batch-edit their own retained state; not needed for ordinary KB authoring.

**Separate memory-maintenance subagents by job.** Recall, reflection, and defragmentation are sensible roles. Commonplace already uses specialized skills and review workflows; it could name memory-maintenance roles more explicitly when trace review, promotion, or index repair become recurring operations.

**Do not borrow identity rhetoric as architecture.** The constitution uses strong selfhood and continuity language. Commonplace should borrow the operational parts - context hierarchy, promotion boundaries, progressive disclosure, and reviewable self-modification - without making methodology quality depend on a metaphysical claim about agent identity.

## Write-side placement

**Write agency:** `automatic` `manual` — the review describes system-driven generation, extraction, consolidation, or update of retained artifacts rather than only manual authoring.

**Curation operations:** `consolidate` `synthesize` `invalidate` `promote` — the existing review evidence identifies automatic store-changing operations matching these curation classes.

## Curiosity Pass

**The public artifact is more constitutional than mechanical.** It is valuable as a design statement, but the repo cannot answer concrete implementation questions: how MemFS pushes are authorized, how compaction is scored, how message search ranks results, how subagents are invoked, or how prompt edits are reviewed.

**Always-loaded policy is reliable but expensive.** Putting identity and durable learnings into the system prompt makes read-back dependable, but it spends scarce context on every inference. The constitution recognizes this tension and tells agents to use indexes, references, compaction, and external memory, but the repo does not show selection budgets or tests.

**Agent ownership creates a governance gap.** If agents can edit their own system prompts, then review, rollback, conflict handling, and authority boundaries matter. The affordances document gives a git-push story for propagation, but not a policy for what edits should be accepted or rejected.

**The trace-learning claim is conceptual here.** The docs discuss learning from experience and persisted message histories, but this checkout does not implement durable artifact derivation from traces. That is why the review omits the `trace-derived` tag.

**The CC0 license is a practical adoption affordance.** Because the policy text is released under CC0, other projects can copy, adapt, or fork the constitution without licensing friction ([LICENSE](https://github.com/letta-ai/context-constitution/blob/0f0a23b66c262f41ce7e060a4da628dc983fb24f/LICENSE)).

## What to Watch

- Whether Letta publishes the MemFS protocol, push semantics, and memory-block synchronization rules. That would determine whether the filesystem projection is a governed source of truth or a convenient editing view.
- Whether future commits add examples of actual prompt assembly. That would clarify which parts of the constitution are always-loaded system-definition artifacts and which are only human-facing documentation.
- Whether compaction and message-history search become specified with budgets, ranking, provenance, and failure modes. That would make the progressive-disclosure mechanism reviewable instead of aspirational.
- Whether reflection and defragmentation subagents gain public prompts or tools. That would show whether memory maintenance is a real staged workflow or just a described affordance.
- Whether the constitution gains tests, schemas, review checklists, or policy gates. That would move it from authored guidance toward an enforceable context-management contract.

## Bottom Line

Context Constitution is best read as an authored policy layer for Letta's memory-first agent vision. Its durable artifact is not a vector store, database, or trace compiler; it is prose that can acquire system-definition authority when inserted into prompts, model training, or a Letta harness. Commonplace should borrow its explicit context hierarchy and promotion framing, while keeping stronger lineage, validation, and review before prose guidance becomes durable operating policy.

Relevant Notes:

- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - exemplifies: Context Constitution needs separate labels for public prose policy, described MemFS state, always-loaded prompt memory, external memory, summaries, and CI validation.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - distinguishes: the public constitution and affordances document are reference material until a host system consumes them with stronger authority.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes: the same prose becomes instruction or learning input when included in prompts or training.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - contrasts: external memory files and message history only affect behavior when the agent or harness brings them back into context.
- [Context engineering](../../notes/definitions/context-engineering.md) - relates: the constitution is explicitly about choosing, compressing, indexing, and loading the right retained context under a bounded context window.
