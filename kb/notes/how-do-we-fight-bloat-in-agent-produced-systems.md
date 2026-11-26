---
type: types/note.md
description: "Standing query on controlling code, prose, and structural bloat in mixed natural-language and code systems produced by agents, where software anti-bloat advice falls short."
---

# How do we fight bloat in agent-produced systems?

## Stakes

Agents make generating both code and natural-language artifacts — notes, documentation, specifications, instructions, tests, and schemas — cheap. Software engineering already has many partial defenses against code bloat (dead-code elimination, refactoring, linters, dependency budgets, YAGNI), yet none has settled bloat even for pure software. Systems like Commonplace combine **natural language and code**, which adds prose, conventions, links, and routing surfaces that lack static reachability checks.

Bloat in these mixed systems compounds through three channels:

- **Context and routing cost:** duplicated or verbose prose, overlapping conventions, and extra routes compete for bounded agent attention and raise lookup cost.
- **Maintenance and drift load:** every retained artifact, copy, or structure must be reconciled when neighboring code or claims change; [maintenance capacity must match harmful-artifact inflow](../theory/maintenance-capacity-must-match-harmful-artifact-inflow.md).
- **Recursive exposure:** retained prose and code can become input to later agents. [Anecdotal reports about generated code comments](../theory/maintenance-capacity-must-match-harmful-artifact-inflow.md#evidence) suggest that later agents may repeat a misleading explanation; they do not establish how often this happens.

This query stays open as long as bloat control relies on periodic manual sweeps and ad-hoc restraint; it narrows or retires if a tested lifecycle regime keeps both code and natural-language bloat bounded under sustained autonomous production.

## Current answer

Our current answer is to follow five principles:

- **Do not write what the executor or live source already supplies.** [An author should fix what the executor can't determine, not what it will](../theory/fix-what-the-executor-cant-determine-not-what-it-will.md) trims instruction and specification bloat by leaving choices open when verified doctrine, task intent, and execution evidence already determine them. Once agents could reliably recover exact facts from source and CLI help, a [documentation sweep](../theory/evidence/seven-documentation-cases-left-routing-and-synthesis.md) retired two pages and reduced five. Combined size fell 53% across the six pages with byte counts; the other retired page had no recorded starting size. The remaining pages helped readers find unfamiliar commands or understand how components fit together.
- **Target zero-structure expansion, not word count.** [Reverse compression is when LLM output expands without adding information](../theory/reverse-compression-is-when-llm-output-expands-without-adding.md) targets selection bloat in both prose (inflating a compact seed with generic priors) and code (output-matching boilerplate without a reusable generative rule). In [two rewrites of one note](../theory/evidence/two-rewrites-exposed-a-syntax-or-repetition-tradeoff.md), splitting sentences lost relations between claims and their qualifiers; restating those relations preserved them but used more words. In a [separate comparison of three revisions](../theory/evidence/three-simplification-passes-exposed-different-tradeoffs.md), the shortest version weakened several technical relations.
- **Balance cheap adoption with an operative retirement path.** [Cheap adoption and weak retirement accumulate cost](../theory/cheap-adoption-and-weak-retirement-accumulate-cost.md) diagnoses structural bloat: even locally sound additions (tags, schemas, templates, conventions) accumulate routing and migration debt when adding is local and retiring needs distributed evidence and migration. [Current-task fit alone does not warrant costly structural entrenchment](../theory/current-task-fit-alone-does-not-warrant-costly-entrenchment.md) keeps reversible local adoption separate from shared commitments that require stronger warrant.
- **Retire fixed-difficulty scaffolding as models improve.** [Scaling absorbs scaffolding at fixed task difficulty, not at the deployment frontier](../theory/scaling-absorbs-scaffolding-at-fixed-difficulty-not-at-the-frontier.md) distinguishes retiring checklists, scripts, and guards that newer models no longer need on fixed tasks from retaining external structure only where frontier difficulty still justifies it.
- **Gate inflow by value as well as validity.** Connected to [How do we value notes?](./how-do-we-value-notes.md) and [choosing what to learn requires both validity and learning-value gates](../theory/choosing-what-to-learn-requires-both-validity-and-learning-value-gates.md): structural and grounding checks block invalid artifacts, but without a value gate, valid redundant artifacts still accumulate.

## Unsettled

- **Would removing this passage change any decision or answer?** Code has unused-symbol checks, call graphs, and test coverage — and even those miss live but over-engineered code. Natural language has no comparable reachability check: a redundant section, obsolete convention, or overlapping note can stay syntactically valid and linked without changing any real decision or answer.
- **Cross-boundary bloat between code and prose.** Mixed systems accumulate co-bloat across the boundary: prose restating live code, code enforcing obsolete prose conventions, tests locking in incidental behavior, and prompt guards compensating for code bugs that were later fixed. We lack a reliable way to surface when a change on one side has made an artifact on the other side redundant.
- **Missing triggers for retirement.** [Cheap adoption and weak retirement accumulate cost](../theory/cheap-adoption-and-weak-retirement-accumulate-cost.md) notes that a cleanup procedure exists once a target is named, but we lack reliable signals and rules that route obsolete prose, conventions, or code into retirement review before migration cost compounds.
- **Separating useful redundancy from bloat.** Some repetition pays — checked routing catalogues, explicit relations that prevent reader misreading, or local warnings placed next to the code they constrain. We have no practical test that reliably separates load-bearing redundancy from bloat without case-by-case judgment.
- **When we ask for a shorter note, does the revision remove redundant content or just use fewer words to say the same thing?** In a [controlled training experiment](../sources/why-is-ai-generated-language-so-hard-to-understand.ingest.md), a length penalty led one small model to prefer the shorter of two correct constructions. The study did not test revision prompts or measure reader comprehension. One conjecture in `kb/log.md` is that asking for both thoroughness and brevity could preserve redundant content while making sentences harder to parse.
- **When do agents add rather than consolidate?** When an agent adds another guard instead of revising an existing one, what made addition the easier choice? An agent that cannot see the existing guard needs a way to find it. An agent that finds the guard but cannot tell what depends on it needs a way to check the consequences of changing it.

---

Relevant Notes:

- [How do we value notes?](./how-do-we-value-notes.md) — see-also: companion standing query on selecting which notes earn retention and maintenance cost
- [Cheap adoption and weak retirement accumulate cost](../theory/cheap-adoption-and-weak-retirement-accumulate-cost.md) — see-also: explains how locally sound structural additions accumulate routing and migration cost without an operative retirement path
- [Reverse compression is when LLM output expands without adding information](../theory/reverse-compression-is-when-llm-output-expands-without-adding.md) — see-also: analyzes zero-structure expansion in both LLM prose and generated code
- [Seven documentation cases left routing and synthesis](../theory/evidence/seven-documentation-cases-left-routing-and-synthesis.md) — see-also: bounded Commonplace sweep showing which documentation survived direct source access and which was retired
- [An author should fix what the executor can't determine, not what it will](../theory/fix-what-the-executor-cant-determine-not-what-it-will.md) — see-also: determinability boundary for avoiding unnecessary specification in instructions and prompts
- [Maintenance capacity must match harmful-artifact inflow](../theory/maintenance-capacity-must-match-harmful-artifact-inflow.md) — see-also: frames why inflow pressure turns bloat into a queue-stability problem
- [Model upgrades obsolete notes by function rather than uniformly](../theory/model-upgrades-obsolete-notes-by-function-rather-than-uniformly.md) — see-also: extends retirement on model upgrades from fixed-difficulty scaffolding to absorbed general prose and pure activation cues
- [Why is AI-generated language so hard to understand?](../sources/why-is-ai-generated-language-so-hard-to-understand.ingest.md) — evidenced-by: controlled experiment showing that a training-time length penalty can favor shorter constructions
