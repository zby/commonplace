# Functional matrix

This is a working comparison, not a settled taxonomy. Its purpose is to stop the surface phrase “learning by writing” from hiding different causal processes.

## Dimensions

- **Change locus** — what is claimed to become different: human understanding, an artifact, transient model state, or later system behaviour.
- **Operation** — what the writing-related step does: articulate, constrain, inspect, criticize, route inquiry, stabilize, retain, select, or activate.
- **Representation** — the form before and after the operation. Natural-language and symbolic artifacts remain distinct even when one loop mutates both.
- **Retained state** — what survives the immediate episode.
- **Activation path** — how retained state can affect later work.
- **Evidence of learning** — what shows more than production or storage occurred.

“Not established” is a substantive result. It identifies a missing causal link rather than an empty cell to fill by analogy.

## Human-side cases

| Case | Change locus | Main operation | Representation and retained state | Activation path | Evidence and boundary |
|---|---|---|---|---|---|
| [Graham](../../sources/putting-ideas-into-words.ingest.md) | Human understanding; draft content | Commit an idea to exact words, then reread from a context-poor stranger's stance | Tacit or incomplete idea → revisable prose; repaired claims survive in the draft | Immediate rereading drives another revision cycle | First-person practitioner report. It separates commitment from inspection, but does not establish a medium-specific cause or an agent-learning mechanism. |
| [Karlsson: writing](../../sources/how-to-think-in-writing.ingest.md) | Human understanding; explicit argument | Fix a positive conjecture, expose premises, and search for local or global counterexamples | Diffuse impression → claim-plus-premise structure | Research, rereading, or feedback attacks separately exposed parts | Practitioner account with anecdotes. It supplies a falsification surface, not comparative evidence that the procedure is generally superior. |
| [Karnofsky](../../sources/learning-by-writing.ingest.md) | Human view and investigation state | Write a premature hypothesis, identify its weakest point, route reading toward what could change it, and revise | Current bottom-line claim plus its reasoning | The current claim selects the next subquestion, source, or critic | First-person account with one extended example. It shows inquiry routing but leaves anchoring risk and transferability untested. |
| [Karlsson: wordless thought](../../sources/when-is-it-better-to-think-without-words.ingest.md) | Human understanding and working-memory load | Alternate broad, partly wordless exploration with textual testing, stabilization, and relay | Unsettled intuition → checked intermediate result | A stabilized result becomes a premise or stepping stone for a longer chain | Historical testimony, introspection, and cited research. The neuroscience and human-to-LLM analogy remain speculative. |
| [Borretti](../../sources/borretti-human-routers-of-machine-words.ingest.md) | Human writer's understanding; reader's verification burden | Concretize a vague idea, or delegate that commitment and leave contradictions hidden | Vague idea → apparently coherent prose | A reader must re-derive unsupported “because” and “therefore” links | Conceptual polemic. It sharply states the failure mode but does not test partial or adversarial delegation. |
| [Grunewald](../../sources/why-almost-never-use-ai-to-write-anything-substantive.ingest.md) | Human expert judgment; reader trust | Compose to discover the contribution, or adversarially re-derive an AI draft rather than passively assent | Expert notes or model draft → reviewed prose with an implied authorial warrant | Expert review and later reader interpretation | One worked domain-expert audit plus first-person argument. It reveals dense local defects and anchoring risk but does not compare stronger workflows. |

## Engineered-system cases

| Case | Change locus | Main operation | Representation and retained state | Activation path | Evidence and boundary |
|---|---|---|---|---|---|
| [Adversarial human-agent loop](../../notes/adversarial-loop-can-reconstruct-the-writing-is-thinking-filter.md) | Human judgment and candidate artifact; possibly later consumers | Generate, criticize, re-derive constraints, and accept or revise | Human intent plus model prose → inspected artifact | Later use depends on ordinary artifact routing and loading | Proposed architecture, not an empirical result. Human presence is insufficient when review becomes passive assent. |
| [J-space experiments](../../sources/verbalizable-representations-global-workspace-llms.ingest.md) | Transient model computation | Externalize intermediate steps so later tokens can reuse them instead of carrying all state internally | Distributed-parametric state → token scratchpad within the current context | Generated tokens are fed back as context during the same episode | Causal swaps and ablations support internal-workspace relief in studied tasks. This is not durable artifact learning and does not validate a human wordless-thought analogy. |
| [Meta-Harness](../../sources/meta-harness-end-to-end-optimization-of-model-harnesses.ingest.md) | Harness artifact and later task performance | Inspect raw execution traces, propose harness-code changes, and select them with benchmark scores | Traces plus source code → retained harness implementation | The revised harness runs on later examples, distributions, and models | Benchmark gains, controlled trace-richness ablation on one domain, and some transfer evidence. It depends on hard oracles, costly traces, and a highly capable proposer. |
| [Symbolic Learning](../../sources/symbolic-learning-enables-self-evolving-agents.ingest.md) | Prompts, tools, pipeline topology, and later task performance | Attribute textual feedback across nodes, mutate mixed-form artifacts, retry illegal edits, and roll back regressions | Trajectory → revised natural-language and symbolic harness | The revised harness governs subsequent runs | Proof-of-concept benchmark results. The same prompted evaluator helps propose and accept changes, so correlated error and weak validation remain possible. |
| [Memento-Skills](../../sources/memento-skills-let-agents-design-agents.ingest.md) | Skill library, router, and later task performance | Route a failure, attribute it to one skill, rewrite or create the skill, and gate it with a generated test | Trajectory → retained `SKILL.md`, prompts, code, and utility state | A learned router selects the skill for a later task and execution consumes it | Read-write ablations and held-out results show gains, especially under domain recurrence. They do not by themselves establish causal uptake of each selected skill. |
| [Faithful self-evolvers study](../../sources/llm-agents-are-not-always-faithful-self-evolvers.ingest.md) | Later agent behaviour, often unchanged despite stored memory | Condense experience, retrieve it, and inject it into a later task | Raw trajectory or summary → stored and selected memory | Retrieved memory appears in context | Perturbation across frameworks, models, and environments finds strong dependence on raw trajectories but weak dependence on many condensed memories. This is the counterexample showing that retention and retrieval do not establish learning. |

## Boundary checks for every candidate mechanism

Before treating two rows as instances of one mechanism, ask:

1. Is the shared property an operation, a representation, an outcome, or only a metaphor?
2. What changed: a human, an artifact, transient computation, or later system behaviour?
3. What selected the change, and what evidence justified retaining it?
4. What later event activated the retained state?
5. What observation would show that the activated state caused a behavioural difference?
6. Which component boundary came from evidence, and which was inherited from the human analogy?

These checks come from [the human-analogy boundary](../../notes/human-analogies-suggest-functions-not-component-boundaries.md), [the storage/activation distinction](../../notes/knowledge-storage-does-not-imply-contextual-activation.md), and [the behavioural criterion for continual learning](../../notes/continual-learning-open-problem-is-behaviour-not-knowledge.md).

## First-pass synthesis

The corpus currently supports a decomposition, not yet a universal “learning by writing” mechanism:

1. **Exploration** searches candidate structure. It may be linguistic, symbolic, environmental, or partly wordless.
2. **Articulation and commitment** turn some candidate structure into an inspectable representation and give up ambiguity.
3. **Testing and criticism** compare that representation with logic, evidence, feedback, or an oracle.
4. **Revision and selection** decide what changes and which candidate survives.
5. **Stabilization and retention** preserve a result outside the immediate computation.
6. **Activation** makes that retained result operative in later work.
7. **Behavioural effect** is the additional requirement for calling the retained change system learning rather than artifact maintenance.

The human essays are strongest on articulation, criticism, inquiry routing, and changed understanding. The engineered-system cases are strongest on explicit retention, selection, activation, and measured downstream effects. No source yet shows that these are one mechanism rather than functions that can be assembled into different loops.

This makes **written artifacts in learning loops** a better workshop label than **learning by writing** for now. It names the object being compared without presupposing that inscription itself learns, that every useful operation is verbal, or that human and engineered systems change in the same place.

## Decisions still unsupported

- Whether the stable concept should cover only natural-language artifacts or the natural-language-plus-symbolic readable pair.
- Whether “relay result” is a useful general term or only a human-side metaphor for retained intermediate state.
- Whether inquiry routing belongs inside this concept or remains a connection to directed reading and the discovery lifecycle.
- Whether the graph needs a new tag. A tag is warranted only if the final inclusion rule routes a coherent set of durable notes better than existing tags do.

