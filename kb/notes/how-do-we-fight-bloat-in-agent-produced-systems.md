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
- **Recursive exposure:** in agent-operated systems, retained prose and code become future model input, so verbose or obsolete material anchors later generations.

This query stays open as long as bloat control relies on periodic manual sweeps and ad-hoc restraint; it narrows or retires if a tested lifecycle regime keeps both code and natural-language bloat bounded under sustained autonomous production.

## Current answer

Commonplace currently counters bloat with five partial mechanisms across prose, structure, and the code–prose boundary:

- **Do not write what the executor or live source already supplies.** [An author should fix what the executor can't determine, not what it will](../theory/fix-what-the-executor-cant-determine-not-what-it-will.md) trims instruction and specification bloat by leaving choices open when verified doctrine, task intent, and execution evidence already determine them. At the code–prose boundary, [seven documentation cases left routing and synthesis](../theory/evidence/seven-documentation-cases-left-routing-and-synthesis.md) showed in a bounded sweep that direct access to live source and CLI help eliminated exact-fact prose copies (cutting six candidate pages by 53 percent and retiring two), leaving unknown-name routing and cross-component synthesis.
- **Target zero-structure expansion, not word count.** [Reverse compression is when LLM output expands without adding information](../theory/reverse-compression-is-when-llm-output-expands-without-adding.md) targets selection bloat in both prose (inflating a compact seed with generic priors) and code (output-matching boilerplate without a reusable generative rule). Local rewrites confirm that raw brevity is the wrong target: [two rewrites exposed a syntax-or-repetition tradeoff](../theory/evidence/two-rewrites-exposed-a-syntax-or-repetition-tradeoff.md) and [three simplification passes exposed different clarity–precision tradeoffs](../theory/evidence/three-simplification-passes-exposed-different-tradeoffs.md) found that naive shortening dropped technical relations while clearer rewrites sometimes added words.
- **Balance cheap adoption with an operative retirement path.** [Cheap adoption and weak retirement accumulate cost](../theory/cheap-adoption-and-weak-retirement-accumulate-cost.md) diagnoses structural bloat: even locally sound additions (tags, schemas, templates, conventions) accumulate routing and migration debt when adding is local and retiring needs distributed evidence and migration. [Current-task fit alone does not warrant costly structural entrenchment](../theory/current-task-fit-alone-does-not-warrant-costly-entrenchment.md) keeps reversible local adoption separate from shared commitments that require stronger warrant.
- **Retire fixed-difficulty scaffolding as models improve.** [Scaling absorbs scaffolding at fixed task difficulty, not at the deployment frontier](../theory/scaling-absorbs-scaffolding-at-fixed-difficulty-not-at-the-frontier.md) distinguishes retiring checklists, scripts, and guards that newer models no longer need on fixed tasks from retaining external structure only where frontier difficulty still justifies it.
- **Gate inflow by value as well as validity.** Connected to [How do we value notes?](./how-do-we-value-notes.md) and [choosing what to learn requires both validity and learning-value gates](../theory/choosing-what-to-learn-requires-both-validity-and-learning-value-gates.md): structural and grounding checks block invalid artifacts, but without a value gate, valid redundant artifacts still accumulate.

## Unsettled

- **No reachability oracle for natural language.** Code has unused-symbol checks, call graphs, and test coverage — and even those miss live but over-engineered code. Natural language has no comparable reachability check: a redundant section, obsolete convention, or overlapping note can stay syntactically valid and linked without changing any real decision or answer.
- **Cross-boundary bloat between code and prose.** Mixed systems accumulate co-bloat across the boundary: prose restating live code, code enforcing obsolete prose conventions, tests locking in incidental behavior, and prompt guards compensating for code bugs that were later fixed. We lack a reliable way to surface when a change on one side has made an artifact on the other side redundant.
- **Missing triggers for retirement.** [Cheap adoption and weak retirement accumulate cost](../theory/cheap-adoption-and-weak-retirement-accumulate-cost.md) notes that a cleanup procedure exists once a target is named, but we lack reliable signals and rules that route obsolete prose, conventions, or code into retirement review before migration cost compounds.
- **Separating useful redundancy from bloat.** Some repetition pays — checked routing catalogues, explicit relations that prevent reader misreading, or local warnings placed next to the code they constrain. We have no practical test that reliably separates load-bearing redundancy from bloat without case-by-case judgment.
- **Brevity pressure can distort wording without cutting content.** Pushing models to write shorter text does not automatically reduce content bloat: a model can keep all the content while squeezing the wording into denser, harder-to-parse syntax. One producer-side study reports that "we find that AI models use these difficult features more often than paraphrases generated by round-trip translation" ([Why is AI-generated language so hard to understand?](../sources/why-is-ai-generated-language-so-hard-to-understand.ingest.md), verbatim), and demonstrates a proof-of-concept "by fine-tuning a language model under a length penalty, which leads to a divergence from human-like linguistic behavior" ([Why is AI-generated language so hard to understand?](../sources/why-is-ai-generated-language-so-hard-to-understand.ingest.md), verbatim) — with human reading cost inferred from prior work rather than measured directly. An unconfirmed conjecture in `kb/log.md` is that thoroughness pressure paired with superficial length pressure produces both failures at once; we do not yet know how to apply selection pressure cleanly without triggering that encoding distortion.
- **Why agents are biased toward adding, and how to counteract it.** Empirically, agents default to additive changes — adding a helper, guard, section, or new note — rather than deleting or consolidating existing structure. We do not yet understand the mechanism behind this bias (for example, how much comes from training and reward incentives, local risk aversion around unknown dependents, or narrow context hiding existing structure). Understanding *why* it happens matters because different causes call for different countermeasures — and we do not yet know what workflow, review, or selection design makes subtraction and consolidation routine.

---

Relevant Notes:

- [How do we value notes?](./how-do-we-value-notes.md) — see-also: companion standing query on selecting which notes earn retention and maintenance cost
- [Cheap adoption and weak retirement accumulate cost](../theory/cheap-adoption-and-weak-retirement-accumulate-cost.md) — see-also: explains how locally sound structural additions accumulate routing and migration cost without an operative retirement path
- [Reverse compression is when LLM output expands without adding information](../theory/reverse-compression-is-when-llm-output-expands-without-adding.md) — see-also: analyzes zero-structure expansion in both LLM prose and generated code
- [Seven documentation cases left routing and synthesis](../theory/evidence/seven-documentation-cases-left-routing-and-synthesis.md) — see-also: bounded Commonplace sweep showing which documentation survived direct source access and which was retired
- [An author should fix what the executor can't determine, not what it will](../theory/fix-what-the-executor-cant-determine-not-what-it-will.md) — see-also: determinability boundary for avoiding unnecessary specification in instructions and prompts
- [Maintenance capacity must match harmful-artifact inflow](../theory/maintenance-capacity-must-match-harmful-artifact-inflow.md) — see-also: frames why inflow pressure turns bloat into a queue-stability problem
- [Why is AI-generated language so hard to understand?](../sources/why-is-ai-generated-language-so-hard-to-understand.ingest.md) — evidenced-by: producer-side corpus and proof-of-concept length-penalty evidence that brevity pressure can distort encoding without cutting content
