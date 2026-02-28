# Meta

Observations and design work toward a knowledge base for design history.

## Goal

Build a knowledge base that applies [deploy-time learning](./deploy-time-learning-the-missing-middle.md), [stabilisation](./stabilisation.md), and the generator/verifier pattern to managing design notes, decisions, and architecture.

## Constraint: Claude Code as runtime

The knowledge base runs on Claude Code — using skills, hooks, and CLAUDE.md as the execution substrate. The implementation is markdown files, ripgrep queries, shell scripts, and skill definitions.

## Approach

arscontexta is our first large experiment. These observations evaluate what works and inform what comes next:

- **What to keep** — machinery that earns its complexity (e.g., `/connect` for finding relationships)
- **What to simplify** — overhead that doesn't pay for itself (e.g., queue management, pipeline chaining)
- **What to build** — automated quality checks as they become justified by real failures, not taxonomy

The verifiability gradient applies to the knowledge base itself:
1. Start soft — LLM writes and connects notes (stochastic)
2. Add filters — automated checks reject bad samples (deterministic code where possible, LLM rubrics where needed)
3. Stabilize search — recurring queries become indexes, tags, structured `rg` patterns
4. Stabilize the filters — LLM rubrics that prove reliable get replaced with deterministic checks

## Status

We're early. Record what you notice. Separate observations from prescriptions — note that something adds complexity before concluding what should replace it.
