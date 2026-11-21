# Commonplace

**Research on knowledge systems, running as one.**

The premise is simple. LLM-written text can be useful even when no person reads it directly, because it can improve how an LLM answers your questions. Commonplace is a **living doctrine for agent-operated knowledge systems, developed and tested by running one**.

The project stands on two reinforcing pillars:

- **A research direction — [deliberative learning](./theory/definitions/judgment-governed-self-improvement.md).** A system learns by changes that are each proposed, judged, and can be rejected. Commonplace's changes are edits to a readable, addressable store of prose, structured text, and code. Our empirical bet is that fixed-weight LLMs can perform that judgment on balance where no single scalar metric settles a change, allowing the loop to run without a person. No automated end-to-end test of that bet has been run yet.
- **A practical system — an agent-operated LLM wiki.** In the sense [Andrej Karpathy sketched](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f), a persistent, linked Markdown-and-Git layer where agents, directed by people, turn a project's work and sources into retained, connected notes, backed by installable types, skills, validators, and review workflows.

The two reinforce each other because memory is about learning: a note earns its keep when it changes what the system does next. A wiki that agents read and edit is the kind of addressable store a deliberative learner needs, and [real use supplies the problems and criticism](./theory/system-use-selects-theory-fit-without-a-fixed-oracle.md) its judgments draw on. Because Commonplace's own doctrine — how it writes, links, validates, and revises notes — lives inside the store it edits ([reflection](./theory/definitions/reflective-system.md)), [an improvement to the method is reused by later work](./theory/an-optimal-long-run-learning-strategy-invests-in-its-own-machinery.md). People still perform many of its operations; the work is moving them to computation.

This site holds the adopted doctrine together with research and evidence that can challenge it. Research does not become doctrine merely by being stored here.

## Research: deliberative learning

Standard machine learning updates opaque weights against a scalar loss or value function. At the opposite extreme, Schmidhuber's [Gödel machine](./theory/goedel-machines-are-a-proof-governed-case-of-self-modification.md) rewrites its own code only when it can formally prove higher expected utility, which leaves most real-world improvements out of reach. Commonplace is an attempt to build something like a Gödel machine made practical: replacing formal proof with fixed-weight LLMs realizing the judgment function, weighing changes on balance over a readable, addressable store and relying on reversibility and later evidence to catch mistakes.

- **Central thesis:** [Deliberative Learning: Judgment in Place of a Value Function](./articles/deliberative-learning-judgment-in-place-of-a-value-function.md) (draft) argues that deliberative learning is a distinct learning paradigm compatible with the Bitter Lesson, grounded in the [deliberative learning definition](./theory/definitions/judgment-governed-self-improvement.md) and [on-balance judgments](./theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md).
- **Test program:** [Testing Autonomous Deliberative Learning](./articles/testing-autonomous-deliberative-learning.md) (draft) separates human-assisted operation from autonomous model judgment, defines comparisons for admission, targeted correction, criterion revision, and whole-loop net gain, and proposes a first experiment.
- **Deployment-time adaptation:** Durable edits to prompts, rules, schemas, tests, and code change later sessions without updating model weights, provided later work loads or enforces them ([deploy-time learning](./theory/retained-artifacts-enable-persistent-deployment-time-adaptation.md), the [learning theory index](./tags/learning-theory-README.md), and the published ECSA 2026 paper and ASISAS 2026 slides in [Articles](./articles/README.md)).
- **Self-improving and reflective systems:** Deliberative learning is a [proposal–selection loop](./theory/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) over an addressable store. The [self-improving systems index](./tags/self-improving-systems-README.md), the [deliberative learning index](./tags/judgment-governed-self-improvement-README.md), and [Commonplace as a reflective system](./theory/evidence/commonplace-as-a-reflective-system.md) develop the machinery; [What an Automated Reviewer Should Measure](./articles/what-an-automated-reviewer-should-measure.md) (draft) proposes evaluating explanatory revisions by reach and economy.

## Practice: an agent-operated LLM wiki

Commonplace packages the methodology running this site as an open-source tool for building a project knowledge base with coding agents. You direct an agent toward outcomes in ordinary language; the agent discovers the conventions, skills, and commands it needs.

- **Discoverable, loadable, composable, trusted knowledge.** Agents work under bounded context ([agent memory requirements](./theory/agent-memory-needs-discoverable-composable-trusted-knowledge-under.md)). [Claims as titles](./theory/title-as-claim-enables-traversal-as-reasoning.md) and [explicit link semantics](./tags/links-README.md) make traversal a chain of reasoning rather than keyword search, while source provenance and review mark how strongly to rely on a note.
- **Progressive structure in place.** A plain Markdown file is valid `text`. Add frontmatter, a description, a type, or local collection contracts only when extra structure enables useful checks or workflows ([the wikiwiki principle](./theory/wikiwiki-principle-lowest-friction-capture-then-progressive-refinement.md)).
- **Explicit doctrine paired with deterministic code.** Skills and prose instructions guide model judgment; Python commands, schemas, and `commonplace-validate` enforce repeatable rules and bookkeeping ([scheduler–LLM separation](./theory/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md)).
- **Separated review and editing.** `commonplace-review` runs headless criteria against notes and never edits them; `commonplace-revise` is the only review/editing workflow that writes a note ([Review and editing system](./reference/README-REVIEW-SYSTEM.md)).

### Use it yourself

Commonplace is open source. Two ways to put it to work:

- **Point your agent at this site** (`https://zby.github.io/commonplace/`) or the [GitHub repository](https://github.com/zby/commonplace) when designing agentic systems, context engineering, or memory architecture, so it can draw on the accumulated methodology directly without installing anything.
- **Install `llm-commonplace` in a project** to get the types, conventions, skills, validators, and commands for your own agent-operated knowledge base: see the [GitHub README](https://github.com/zby/commonplace) and [INSTALL.md](https://github.com/zby/commonplace/blob/main/INSTALL.md) for setup, [Getting started](./reference/getting-started.md) for a first worked session, and [Reference](./reference/README.md) or [installation architecture](./reference/architecture.md) for how the system fits together.
