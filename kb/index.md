# Commonplace

**Research on knowledge systems, running as one.**

LLM-written text can be useful even when no person reads it directly, because it can improve how an LLM answers your questions. Commonplace is a **living doctrine for agent-operated knowledge systems, developed and tested by running one**.

Commonplace combines two things:

- **A research direction — [continual learning with fixed model weights](./articles/continual-learning-with-fixed-model-weights-llm-selected-updates.md) (draft).** A deployed system can learn while its model weights stay fixed by changing what it retains between tasks—procedures, rules, notes, and scripts—through updates that are proposed, evaluated on whether they make later work better, and can be rejected. Our empirical bet is that fixed-weight LLMs can help search for candidate updates and perform that selection for open-ended knowledge work where no single score settles a change, allowing the loop to run without per-update human judgment. No automated end-to-end test of that bet has been run yet.
- **A practical system — an agent-operated LLM wiki.** In the sense [Andrej Karpathy sketched](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f), a persistent, linked Markdown-and-Git layer where agents, directed by people, turn a project's work and sources into retained, connected notes, backed by installable types, skills, validators, and review workflows.

They reinforce each other because memory is about learning: a note earns its keep when it changes what the system does next. A wiki that agents read and edit is the kind of addressable store a selection-based learner needs, and [real use supplies the problems and criticism](./theory/system-use-selects-theory-fit-without-a-fixed-oracle.md) its judgments draw on. Commonplace also keeps its own operating rules—how it writes, links, validates, and revises notes—inside the store it edits ([reflection](./theory/definitions/reflective-system.md)). When a method improves, [later work reuses it](./theory/an-optimal-long-run-learning-strategy-invests-in-its-own-machinery.md). People still perform many of its operations; the work is moving them to computation.

## Research: selection-based learning

Standard machine learning updates opaque weights against a scalar loss or reward. At the opposite extreme, Schmidhuber's [Gödel machine](./theory/goedel-machines-are-a-proof-governed-case-of-self-modification.md) rewrites its own code only when it can formally prove higher expected utility, which leaves most real-world improvements out of reach. Commonplace explores the middle ground: replacing formal proof with fixed-weight LLMs making local comparisons over a readable, addressable store, relying on reversibility and later evidence to catch mistakes.

- **Core theory:** [selection-based learning](./theory/definitions/selection-based-learning.md) defines the loop; [local comparison suffices](./theory/selection-based-learning-needs-only-a-local-comparison.md) explains why costly search removes the need for a global score; [defining improvement for open-ended work](./theory/defining-improvement-for-open-ended-work.md) sets out what a usable improvement standard has to handle; and [on-balance judgment with an LLM](./theory/on-balance-judgment-with-an-llm.md) shows how a model compares remedies (with [necessary preference](./theory/necessary-preference-can-guide-improvement-without-a-global-measure.md) as one formalization).
- **The judgment bet:** [Can an LLM Judge Which Changes Are Worth Making?](./articles/can-an-llm-judge-which-changes-are-worth-making.md) (draft) traces one real decision across evidence-packet and tool-using setups, sketches a three-arm diagnostic test, and separates working definition, judge competence, and framework prompting.
- **Test program:** [Testing Autonomous Selection-Based Learning](./articles/testing-autonomous-selection-based-learning.md) (draft) separates human-assisted operation from autonomous model judgment, defines comparisons for admission, targeted correction, criterion revision, and whole-loop net gain, and proposes a first experiment.
- **Continual learning:** Software and KB maintenance can carry lessons from use into later work: durable edits to prompts, rules, schemas, tests, and code change later sessions without touching model weights, provided later work loads or enforces them ([deployed systems can learn with fixed model weights](./theory/deployed-systems-can-learn-from-feedback-with-fixed-model-weights.md), the [continual learning index](./tags/continual-learning-README.md), the [learning theory index](./tags/learning-theory-README.md), and the published ECSA 2026 paper and ASISAS 2026 slides in [Articles](./articles/README.md)).
- **Self-improving and reflective systems:** Commonplace uses **reflective self-improvement by selection**—a [proposal–selection loop](./theory/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) over the instructions and checks that govern its own later work (currently with human maintainers inside the boundary for both search and selection; automating the loop is the bet). The [self-improving systems index](./tags/self-improving-systems-README.md), the [improvement loop index](./tags/improvement-loop-README.md), the [robust comparison index](./tags/robust-comparison-README.md), and [Commonplace as a reflective system](./theory/evidence/commonplace-as-a-reflective-system.md) develop the machinery; [What an Automated Reviewer Should Measure](./articles/what-an-automated-reviewer-should-measure.md) (draft) proposes evaluating explanatory revisions by reach and economy.

## Practice: an agent-operated LLM wiki

Commonplace packages the methodology running this site as an open-source tool for building a project knowledge base with coding agents. You direct an agent toward outcomes in ordinary language; the agent discovers the conventions, skills, and commands it needs.

- **Discoverable, loadable, composable, trusted knowledge.** Agents work under bounded context ([agent memory requirements](./theory/agent-memory-needs-discoverable-composable-trusted-knowledge-under.md)). [Claims as titles](./theory/title-as-claim-enables-traversal-as-reasoning.md) and [explicit link semantics](./tags/links-README.md) make traversal a chain of reasoning rather than keyword search, while source provenance and review mark how strongly to rely on a note.
- **Typed documents with two-part types.** Each document type pairs a syntactic part checked deterministically by software (YAML schema, required fields, links, and structural rules via `commonplace-validate`) with a semantic part checked by agents (prose authoring contracts, traits, and LLM review gates via `commonplace-review`; see [verifiable document types](./theory/document-types-should-be-verifiable.md)).
- **Progressive structure in place.** A plain Markdown file is valid `text`. Add frontmatter, a description, a type, or local collection contracts only when extra structure enables useful checks or workflows ([the wikiwiki principle](./theory/wikiwiki-principle-lowest-friction-capture-then-progressive-refinement.md)).
- **Explicit doctrine paired with deterministic code.** Skills and prose instructions guide model judgment; Python commands enforce repeatable operations and bookkeeping ([scheduler–LLM separation](./theory/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md)).
- **Separated review and editing.** `commonplace-review` runs headless criteria against notes and never edits them; `commonplace-revise` is the only review/editing workflow that writes a note ([Review and editing system](./reference/README-REVIEW-SYSTEM.md)).

### Browse the KB

- **[Topics (tags index)](./tags/README.md)** — the main access path for browsing the KB by topic; each tag head introduces the area, recommends where to start, and lists every tagged artifact grouped by collection.
- **[Theory questions](./theory/questions/README.md)** — recurring research questions treated as problem-first starting points beside individual claims.
- **[Articles](./articles/README.md)** — standalone technical articles, drafts, and talks.
- **[Reference](./reference/README.md)** — shipped architecture, contracts, CLI commands, and ADRs.

Pages under [`work/`](./work/README.md) record investigations. If you find a proposal there, check the [reference documentation](./reference/README.md) before describing it as an adopted Commonplace decision.

### Use it yourself

Commonplace is open source. Two ways to put it to work:

- **Point your agent at this site** (`https://zby.github.io/commonplace/`) or the [GitHub repository](https://github.com/zby/commonplace) when designing agentic systems, context engineering, or memory architecture, so it can draw on the accumulated methodology directly without installing anything.
- **Install `llm-commonplace` in a project** to get the types, conventions, skills, validators, and commands for your own agent-operated knowledge base: see the [GitHub README](https://github.com/zby/commonplace) and [INSTALL.md](https://github.com/zby/commonplace/blob/main/INSTALL.md) for setup, [Getting started](./reference/getting-started.md) for a first worked session, and [Reference](./reference/README.md) or [installation architecture](./reference/architecture.md) for how the system fits together.
