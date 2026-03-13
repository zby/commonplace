# Improvement log

Append one line per observation. Don't fix anything — just record it.

Format: `- path/to/note.md: what needs improving`

- SYNTHESIS: [methodology-enforcement-is-constraining, unified-calling-conventions (harness layer section), bounded-context-orchestration-model, agent-statelessness-means-harness-should-inject-context-automatically] all describe harness design decisions from different theoretical angles but the KB has no note that maps the practitioner "harness component" taxonomy to the theoretical framework — convergence across three independent sources (Vtrivedy10, Lopopolo, cybernetics)
- SYNTHESIS: [error-correction-works-above-chance-oracles-with-decorrelated-checks (vary the prompt), operational-signals-that-a-component-is-a-relaxing-candidate (paraphrase brittleness), prompt-stability-code-llms source (emotion templates)] converge on unnamed claim: systematic prompt variation serves simultaneously as a verification technique (decorrelating checks) and a diagnostic technique (measuring brittleness)
- kb/notes/index.md: qmd semantic search returned commonplace-installation-architecture at 88% relevance for a prompt stability query — suggests qmd may be overweighting YAML frontmatter structure over semantic content in ranking
- kb/notes/rlm-achieves-the-clean-scheduler-model-but-opts-out-of-accumulation.md: design space section lists three points but Slate's thread-weaving and voooooogel's forking add at least two more — the enumeration is incomplete
- ABSTRACTION: [bounded-context-orchestration-model (r = call(P)), llm-context-is-composed-without-scoping (sub-agent return value), conversation-vs-prompt-refinement (coordination primitives), Slate source (episodes), Spacebot (branch scrubbed conclusions)] share unnamed structure: execution-boundary compression — bounded execution that returns compressed results rather than full context, with the completion boundary providing the natural unit of distillation
- kb/sources/slate-moving-beyond-react-and-rlm.md: source has zero inbound links from any note — fully orphaned in the link graph despite high connection density to the computational-model cluster
- kb/notes/distillation.md: the source->distillate table lists "Methodology -> Skill" and "Research -> Design principle" but doesn't include the common case of "Domain artifacts (logs, patches, docs) -> Detection/analysis skill" — which is what Cramer's skill synthesis and spec mining both describe
