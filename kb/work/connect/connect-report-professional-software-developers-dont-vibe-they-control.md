# Connection Report: Professional Software Developers Don't Vibe, They Control

**Source:** [Professional Software Developers Don't Vibe, They Control: AI Agent Use for Coding in 2025](kb/sources/professional-software-developers-dont-vibe-they-control.md)
**Date:** 2026-03-09
**Depth:** standard

## Discovery Trace

**Index scan:**
- Read kb/notes/index.md (145 entries) — scanned all entries against source concepts (agent control, prompting strategies, task suitability, human expertise, vibe coding vs disciplined use, plan-before-execute, version control for agents).
- Flagged candidates: [programming-practices-apply-to-prompting](kb/notes/programming-practices-apply-to-prompting.md), [agentic-systems-interpret-underspecified-instructions](kb/notes/agentic-systems-interpret-underspecified-instructions.md), [constraining](kb/notes/constraining.md), [inspectable-substrate-not-supervision-defeats-the-blackbox-problem](kb/notes/inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md), [methodology-enforcement-is-constraining](kb/notes/methodology-enforcement-is-constraining.md), [context-efficiency-is-the-central-design-concern-in-agent-systems](kb/notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md), [writing-styles-are-strategies-for-managing-underspecification](kb/notes/writing-styles-are-strategies-for-managing-underspecification.md), [oracle-strength-spectrum](kb/notes/oracle-strength-spectrum.md), [deploy-time-learning-the-missing-middle](kb/notes/deploy-time-learning-the-missing-middle.md), [bounded-context-orchestration-model](kb/notes/bounded-context-orchestration-model.md), [human-llm-differences-are-load-bearing-for-knowledge-system-design](kb/notes/human-llm-differences-are-load-bearing-for-knowledge-system-design.md), [legal-drafting-solves-the-same-problem-as-context-engineering](kb/notes/legal-drafting-solves-the-same-problem-as-context-engineering.md), [deploy-time-learning-is-agile-for-human-ai-systems](kb/notes/deploy-time-learning-is-agile-for-human-ai-systems.md), [agents-md-should-be-organized-as-a-control-plane](kb/notes/agents-md-should-be-organized-as-a-control-plane.md), [structure-activates-higher-quality-training-distributions](kb/notes/structure-activates-higher-quality-training-distributions.md), [frontloading-spares-execution-context](kb/notes/frontloading-spares-execution-context.md), [Professional Software Developers and AI Agent Use](kb/notes/related_works/professional-developers-ai-agents.md)

**Topic indexes:**
- Read [learning-theory](kb/notes/learning-theory.md) — confirmed constraining, deploy-time learning, and oracle-strength connections
- No additional candidates beyond index scan

**Semantic search:** (via qmd)
- query "experienced developers control AI agents through planning supervision prompting strategies software quality" (notes) — top hits:
  - [professional-developers-ai-agents](kb/notes/related_works/professional-developers-ai-agents.md) (93%) — existing related_works note about same paper
  - [agents-md-should-be-organized-as-a-control-plane](kb/notes/agents-md-should-be-organized-as-a-control-plane.md) (51%) — control plane concept maps to paper's control theme
  - [agent-skills-for-context-engineering](kb/notes/related-systems/agent-skills-for-context-engineering.md) (45%) — context engineering framework
  - [methodology-enforcement-is-constraining](kb/notes/methodology-enforcement-is-constraining.md) (43%) — enforcement gradient matches paper's control strategies
  - [writing-styles-are-strategies-for-managing-underspecification](kb/notes/writing-styles-are-strategies-for-managing-underspecification.md) (40%) — writing style taxonomy maps to prompting strategies
  - [programming-practices-apply-to-prompting](kb/notes/programming-practices-apply-to-prompting.md) (37%) — SE practices transfer to prompting

- query "vibe coding vs disciplined agent use task suitability complexity business logic human expertise" (notes) — top hits:
  - [professional-developers-ai-agents](kb/notes/related_works/professional-developers-ai-agents.md) (56%) — same paper
  - [agents-md-should-be-organized-as-a-control-plane](kb/notes/agents-md-should-be-organized-as-a-control-plane.md) (38%) — control theme
  - [context-efficiency-is-the-central-design-concern-in-agent-systems](kb/notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) (36%) — context as bottleneck
  - [agentic-systems-interpret-underspecified-instructions](kb/notes/agentic-systems-interpret-underspecified-instructions.md) (34%) — underspecification framework

- query (sources) — top hits:
  - [context-engineering-ai-agents-oss](kb/sources/context-engineering-ai-agents-oss.md) (56%) — companion empirical study of context engineering practices

**Keyword search:**
- rg "vibe cod" — found only [professional-developers-ai-agents](kb/notes/related_works/professional-developers-ai-agents.md) (already flagged)
- rg "2512.14012" — found target source + related_works note (confirms existing connection)
- rg "human expertise|human judgment|human oversight" — found 6 notes, none with strong enough connection to add beyond index candidates
- rg "task suitability|task complexity" — no new candidates
- rg "plan file|user rules|context file" — found [deploy-time-learning-the-missing-middle](kb/notes/deploy-time-learning-the-missing-middle.md), [agents-md-should-be-organized-as-a-control-plane](kb/notes/agents-md-should-be-organized-as-a-control-plane.md) (already flagged)

## Connections Found

### Strong connections

- [Professional Software Developers and AI Agent Use](kb/notes/related_works/professional-developers-ai-agents.md) — **extends**: this related_works note is an existing summary/analysis of the same paper (arXiv:2512.14012), mapping its findings to llm-do architecture; the full source text in kb/sources provides the complete empirical evidence the summary distills from

- [programming-practices-apply-to-prompting](kb/notes/programming-practices-apply-to-prompting.md) — **grounds**: the paper's central finding -- that experienced developers apply SE practices (testing, version control, clear specs, progressive compilation) to control agents -- is large-scale empirical evidence for this note's theoretical argument that programming practices transfer to prompting. The paper's S88 quote ("I prompted by applying the lessons of software engineering to narrative") could be the epigraph for this note.

- [agentic-systems-interpret-underspecified-instructions](kb/notes/agentic-systems-interpret-underspecified-instructions.md) — **grounds**: the paper finds "vague prompts will not work" and developers need "clear context and explicit instructions" (12/13 observations, 43/99 survey). This is direct empirical confirmation that semantic underspecification is the practical problem developers face -- they respond by narrowing the interpretation space through the mechanisms this note describes.

- [constraining](kb/notes/constraining.md) — **exemplifies**: the paper documents developers performing constraining at every level of the spectrum -- user rules (conventions), plan files (structured artifacts), context files (stored outputs), version control (commitment), and testing (verification). The progression from plan files through code review to extraction of deterministic patterns matches the constraining spectrum from partial narrowing to full commitment.

- [methodology-enforcement-is-constraining](kb/notes/methodology-enforcement-is-constraining.md) — **exemplifies**: the paper's Table 2 shows an enforcement gradient in practice -- user rules (instruction layer), plan files with step-by-step execution (skill-like structured prompts), systematic testing and version control (hook/script-like verification). The paper's observation that 5/13 developers felt "more willing to test their code systematically while using agents" is developers spontaneously moving methodology down the enforcement gradient.

- [deploy-time-learning-the-missing-middle](kb/notes/deploy-time-learning-the-missing-middle.md) — **exemplifies**: plan files, context files, user rules, and accumulated prompting strategies observed in the paper are all deploy-time learning artifacts -- durable, inspectable adaptations that persist across sessions and improve system behavior. The paper's Table 2 shows participants P1 and P11 maintaining both plan files and context files, which is maintaining repo artifacts for deploy-time adaptation.

### Moderate connections

- [context-efficiency-is-the-central-design-concern-in-agent-systems](kb/notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) — **exemplifies**: the paper finds developers keep agents to an average of 2.1 steps per prompt (Table 2) and prefer short, focused tasks over long autonomous runs. This is direct behavioral evidence that practitioners treat context as the binding constraint -- they manage it by limiting what goes in per call.

- [oracle-strength-spectrum](kb/notes/oracle-strength-spectrum.md) — **exemplifies**: the paper's task suitability findings map directly onto oracle strength. Agents excel at tasks with cheap verification (straightforward, repetitive, scaffolding = hard oracle) and fail at tasks with expensive verification (complex logic, business rules, domain knowledge = soft/delayed oracle). The unsuitable categories (business logic, complex tasks, security-critical code) are exactly the low-oracle-strength regime. **Warning:** target is seedling.

- [bounded-context-orchestration-model](kb/notes/bounded-context-orchestration-model.md) — **exemplifies**: the paper's observation that developers decompose work into small chunks (avg 2.1 steps per prompt, manual task decomposition) and maintain symbolic state externally (plan files, version control, context files) is the select/call/absorb loop in practice -- developers are acting as the symbolic scheduler driving bounded LLM calls. **Warning:** target is seedling.

- [inspectable-substrate-not-supervision-defeats-the-blackbox-problem](kb/notes/inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md) — **contradicts (partially)**: the paper's finding that experienced developers control agents primarily through active supervision and human review (69% reviewed every change) is a counterpoint to this note's claim that inspectable substrate, not supervision, defeats the blackbox problem. However, the tension is nuanced: the developers do rely on inspectable substrate (code diffs, test output, version control) as the medium of their supervision. The paper may show that in current practice, supervision over inspectable substrate is the actual pattern, not substrate alone.

- [writing-styles-are-strategies-for-managing-underspecification](kb/notes/writing-styles-are-strategies-for-managing-underspecification.md) — **exemplifies**: the paper's prompting strategies (clear context, explicit instructions, step-by-step thinking, examples, user rules, file references) are instances of the five writing styles applied informally by practitioners. Prescriptive style dominates (explicit instructions), supplemented by conditional (context-dependent prompts) and descriptive (file references). **Warning:** target is seedling.

- [legal-drafting-solves-the-same-problem-as-context-engineering](kb/notes/legal-drafting-solves-the-same-problem-as-context-engineering.md) — **exemplifies**: the paper's S88 ("I described what good would look like, I described concrete used experiences, I explained the economics, and I gave a spec of what I needed implemented") reads like a legal brief: defined terms, exhaustive specification, enumeration of desired outcomes, and canons of interpretation. Practitioners are independently reinventing legal drafting techniques for agent prompting. **Warning:** target is seedling.

- [deploy-time-learning-is-agile-for-human-ai-systems](kb/notes/deploy-time-learning-is-agile-for-human-ai-systems.md) — **exemplifies**: the paper documents the agile cycle in developer-agent interaction: start underspecified (prompt), observe agent output, learn which parts need hardening (review code, test), codify (accept or revise), repeat. Developers iterate with agents on small chunks -- exactly the deploy-time learning sprint. **Warning:** target is seedling.

**Bidirectional candidates** (reverse link also worth adding):
- [programming-practices-apply-to-prompting](kb/notes/programming-practices-apply-to-prompting.md) <-> source — **grounds (both directions)**: the paper validates the note's theoretical argument; the note provides the conceptual framework that explains WHY the paper's observed strategies work. Both directions are useful for traversal.
- [agentic-systems-interpret-underspecified-instructions](kb/notes/agentic-systems-interpret-underspecified-instructions.md) <-> source — **grounds (both directions)**: the paper provides N=112 empirical evidence for the theoretical framework; the framework explains why "clear context and explicit instructions" are necessary.

### Sources

- [Context Engineering for AI Agents in Open-Source Software](kb/sources/context-engineering-ai-agents-oss.md) — **complements**: this study examines the same phenomenon (how developers structure instructions for agents) from the artifact side (466 AGENTS.md files) while the Huang et al. paper examines it from the behavioral side (13 observations + 99 surveys). Together they triangulate: what developers say they do (Huang), what their artifacts look like (Mohsenimofidi), and why the strategies work (KB theory notes).

## Rejected Candidates

- [structure-activates-higher-quality-training-distributions](kb/notes/structure-activates-higher-quality-training-distributions.md) — the paper mentions structured prompts getting better results, but the connection to training distribution activation is too speculative. The paper's findings are about practitioner behavior, not about which training distributions structured prompts activate.

- [agents-md-should-be-organized-as-a-control-plane](kb/notes/agents-md-should-be-organized-as-a-control-plane.md) — surface vocabulary overlap ("control") but different scopes. The paper is about developer strategies for controlling agents during coding tasks; this note is about how to organize the AGENTS.md file specifically. Too indirect.

- [frontloading-spares-execution-context](kb/notes/frontloading-spares-execution-context.md) — the paper mentions plan files, which are a form of frontloading, but the connection is too indirect. The paper doesn't discuss the partial-evaluation mechanism that makes frontloading effective.

- [human-llm-differences-are-load-bearing-for-knowledge-system-design](kb/notes/human-llm-differences-are-load-bearing-for-knowledge-system-design.md) — the paper's human-expertise findings are about expertise as a strategy for agent control, not about human-LLM cognitive differences as a design concern. Different claims.

- [Agent Skills for Context Engineering](kb/notes/related-systems/agent-skills-for-context-engineering.md) — surface topic overlap (context engineering + agents), but no specific mechanism or claim that connects.

## Index Membership

- [learning-theory](kb/notes/learning-theory.md) — the paper provides large-scale empirical evidence for multiple learning theory concepts (constraining, deploy-time learning, the oracle-strength spectrum). Worth adding as an empirical grounding source.
- Already referenced from: [professional-developers-ai-agents](kb/notes/related_works/professional-developers-ai-agents.md) (existing related_works note)

## Synthesis Opportunities

**Developer control strategies as empirical constraining taxonomy.** The paper's Table 2 documents a rich set of control strategies (plan files, context files, user rules, iterative prompting, testing, version control, code review) that have not been systematically mapped against the KB's constraining spectrum. A synthesis note could argue: "Experienced developers independently rediscover the constraining gradient -- their strategies map onto the spectrum from partial narrowing (user rules) through commitment (plan files) to codification (extracting stable patterns into code)." Contributing notes: [constraining](kb/notes/constraining.md), [methodology-enforcement-is-constraining](kb/notes/methodology-enforcement-is-constraining.md), [programming-practices-apply-to-prompting](kb/notes/programming-practices-apply-to-prompting.md), and this source.

**Oracle strength predicts task suitability.** The paper's fine-grained task suitability data (Table 4, 89 task codes) could be mapped against oracle strength. A synthesis note could argue: "Task suitability is a function of verification cost -- tasks where developers can cheaply verify agent output (boilerplate, tests, documentation) show high suitability; tasks where verification is expensive or requires domain expertise (business logic, architecture, security) show low suitability. This is the oracle-strength spectrum observed in the wild." Contributing notes: [oracle-strength-spectrum](kb/notes/oracle-strength-spectrum.md), this source.

## Flags

- **Existing related_works note may need revision:** [professional-developers-ai-agents](kb/notes/related_works/professional-developers-ai-agents.md) was written as a related_works summary mapping to llm-do architecture. Now that the full paper text is in kb/sources/, the related_works note may be redundant or need updating to serve as an ingest/analysis rather than a standalone summary.
- **No ingest file exists:** The source at kb/sources/ has no corresponding .ingest.md file. Running /ingest would produce a proper classification with connection annotations.
