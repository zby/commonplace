---
description: Deploy-time learning fills the gap between training and in-context — durable symbolic artifacts co-evolve with code through deployment, forming a permanent hybrid rather than a waypoint toward full codification
type: note
traits: [has-comparison, title-as-claim]
tags: [learning-theory]
---

# Deploy-time learning is the missing middle

## Three timescales

Deployed AI systems adapt at three timescales, each with a different substrate:

| Timescale | When | Substrate | Properties |
|-----------|------|-----------|------------|
| **Training** | Before deployment | Weights | Durable but opaque; requires a training pipeline; cannot incorporate deployment-specific information |
| **In-context** | Within a session | Context window | Inspectable but ephemeral; evaporates when the session ends |
| **Deploy-time learning** | Across sessions, during deployment | Symbolic artifacts | Durable, inspectable, and verifiable; accumulates over time |

The table captures today's common configurations; substrate and timing are orthogonal in principle. The fourth cell — weight substrate with deployment timing — exists but remains rare because training infrastructure is heavy. [OpenClaw-RL](../sources/openclaw-rl-train-any-agent-simply-by-talking.ingest.md), which runs live RL from user interactions, is a current example.

Deploy-time learning is not a new training paradigm — model weights don't change. It is **system-level adaptation**: the deployed system's behavior improves because its *artifacts* improve. Like in-context learning, it happens during deployment; like training, it persists durably. Symbolic artifacts hit a pragmatic sweet spot: durable, inspectable, and compatible with ordinary software tooling. In Commonplace the artifacts are mostly repo-hosted, though the [substrate class is broader than the backend](./substrate-class-backend-and-artifact-form-are-separate-axes-that-get-conflated.md).

Two mechanisms drive it: [constraining](./definitions/constraining.md) (narrowing the interpretation space) and [distillation](./definitions/distillation.md) (re-compressing prior reasoning into task-ready artifacts). [Codification](./definitions/codification.md) — the far end of constraining — is where prompts undergo a phase transition into deterministic code. Both are reversible: commitments tighten along [the verifiability gradient](./verifiability-gradient.md) when patterns across runs make them safe, and loosen when new evidence shows them wrong. A system that can only tighten ratchets itself into brittleness.

The machinery involved — version control, diffs, tests, CI, code review — is unremarkable to programmers. But AI researchers, trained to think of adaptation through weights and gradients, look right past it. Symbolic artifacts sit in a disciplinary blind spot: "just engineering" to the ML community, yet they do genuine system-level learning.

## Co-evolving prose and code

Agile was already doing deploy-time learning, though with an asymmetry. Code and specs co-evolved — running code informed specs, revised specs drove new code — but only code executed. Moving a concern back to prose meant taking it out of production. LLMs close the asymmetry: prompts execute, so loosening a codified behavior back to prose keeps the system running.

You deploy with some behavior in prompts, observe what works, and progressively codify the understood parts — while the prompts evolve in response to what the code now handles. At any given moment, some behavior is deterministic code, some is still in prompts, and the boundary moves as understanding accumulates.

The end state also differs. Agile treats natural-language specs as temporary — stories waiting to become code, with fully codified software as the destination. Deploy-time learning recognises that some parts *should stay in prose* because they require judgment, interpretation, or context-sensitivity that deterministic code can't capture. A data-report system might move statistics into Python while leaving narrative interpretation with the LLM, with no plan to codify the narrative. The hybrid is the end state, not a waypoint.

This also reframes what agile calls "changing requirements." Much of that apparent change is really [late-surfacing disambiguation failure](./changing-requirements-conflate-genuine-change-with-disambiguation-failure.md): downstream specs silently commit to one interpretation of an underspecified upstream spec, and the error surfaces only at deployment. Short iterations limit how far wrong interpretations can propagate, not just how fast teams respond to genuine change — and the same logic applies when prompts silently commit to an interpretation that deployment later reveals.

## Failure modes

- **Premature codification.** Committing to one interpretation before enough runs reveal which is right locks in brittle assumptions. The remedy is to constrain only once patterns emerge across runs, and to relax back toward prose when new requirements expose the wrong commitment.
- **Goodharting on evals.** Optimising for the eval metric until it stops tracking real quality. Prompt tests can enshrine the wrong behavior; if eval cases aren't representative of real traffic, gains on the eval set may regress in production.
- **Model drift.** Vendor model updates can break codified prompts and schemas. Regression evals are the defense — they catch drift even when the artifact hasn't changed.
- **Bad assumptions codified confidently.** An agent that writes a bad test codifies a bad assumption that now passes CI. The quality gate is typically human review — codification is a human-AI collaboration, not a purely autonomous process.

## Related work

How systems learn through accumulated artifacts is well-studied outside ML:

- **Organizational learning** (Argyris & Schön, 1978) — double-loop learning: organizations adapt by revising governing assumptions, not just actions. Deploy-time learning is double-loop learning for agent systems — constraining revises the rules, not just the outputs.
- **Knowledge creation** (Nonaka & Takeuchi, 1995) — the SECI spiral: tacit → explicit → combination → internalization. Constraining and distillation map to the externalization and combination phases.

Kirsch's [Flawed Ephemeral Software Hypothesis](../sources/the-flawed-ephemeral-software-hypothesis.ingest.md) makes the same case in software-engineering language: AI lowers the cost of mutating durable artifact stacks, not replacing them. It also names the pressures that keep artifacts durable even when generation becomes cheap — state, integration surfaces, interface stability, auditability, deployment-discovered edge cases.

Within ML/LLMOps, corresponding practices are well-established. Prompt versioning and "prompts as code" are standard advice. Eval-driven development has its own frameworks (OpenAI Evals, promptfoo) and process models ([EDDOps](https://arxiv.org/abs/2411.13768)). Automated prompt optimisation (DSPy, ProTeGi) pursues the same goal — improving system behavior without weight updates — through search over prompt components. Agent skill libraries like [Voyager](https://arxiv.org/abs/2305.16291) and evaluator-guided program evolution like [FunSearch](https://www.nature.com/articles/s41586-023-06924-6) accumulate executable code as a form of cross-episode memory.

**TODO:** The organizational learning and knowledge creation citations are from the agent's training data, not systematic. Revisit with deep search — both traditions likely have results about when formalization helps vs hinders learning.

## Contribution

Deploy-time learning offers two contributions: a **taxonomy** (three timescales of system adaptation) and a **co-evolution model** that treats the prose/code hybrid as a permanent end state rather than a transitional phase. Together they frame deployment-discovered knowledge as a first-class adaptation mechanism alongside weights and context.

Relevant Notes:

- [Continuous learning requires durability, not weight updates](./continuous-learning-requires-durability-not-weight-updates.md) — foundation: deploy-time learning is one durable non-weight form of continuous learning
- [The verifiability gradient](./verifiability-gradient.md) — extends: the ladder that deploy-time artifacts move along in both directions
- [Learning substrates, backends, and artifact forms](./substrate-class-backend-and-artifact-form-are-separate-axes-that-get-conflated.md) — sharpens: the repo is commonplace's backend choice within the broader symbolic artifact substrate
- [Context Engineering for AI Agents in OSS](../sources/context-engineering-ai-agents-oss.ingest.md) — validates: the paper's conclusion that AI context files are "maintained software artifacts" that are "versioned, reviewed, quality-assured, and tested" is the deploy-time learning thesis stated as an empirical finding across 466 projects
- [ABC: Agent Behavioral Contracts](../sources/agent-behavioral-contracts-formal-specification-runtime-enforcement.ingest.md) — extends: behavioral contracts (YAML DSL specs with runtime enforcement) are verifiable repo artifacts that improve reliability without weight updates
- [Harness Engineering (Lopopolo, 2026)](../sources/harness-engineering-leveraging-codex-agent-first-world.ingest.md) — exemplifies: "good harnesses compound" is the deploy-time learning thesis in practitioner language; each constraint makes future work more reliable across a 1M LOC agent-generated codebase
- [in-context learning presupposes context engineering](./in-context-learning-presupposes-context-engineering.md) — extends: in-context learning depends on deploy-time learning to build the context engineering machinery that selects the right knowledge; responds to Amodei's claim that continual learning is unnecessary
