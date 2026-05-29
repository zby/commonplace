---
source: file:///home/zby/txt/paper/submissions/asisas-2026/paper.md
description: Position paper proposing a four-field architectural vocabulary (storage substrate, representational form, lineage, behavioral authority) for classifying retained behavior-shaping artifacts in agentic systems, beyond storage-first labels.
captured: 2026-05-28
capture: local-file
type: kb/sources/types/snapshot.md
tags: [academic-paper]
---

# Where It Lives Is Not What It Is: An Architectural Vocabulary for Retained Adaptation in Agentic Systems

## Abstract

Agentic systems increasingly adapt by retaining behavior-shaping artifacts such as prompts, workflows, validators, routing rules, memories, adapters, and checkpoints. These artifacts are managed and often classified by storage substrate, such as memory systems, flat files, prompt registries, repositories, vector stores, databases, or model-artifact stores. This position paper argues that storage-first classification is architecturally insufficient. Retained behavior-shaping artifacts should instead be classified by the characteristics that determine how they affect behavior: how their operative parts are represented and consumed, where they came from, and what behavioral authority they have.

The vocabulary records four properties of retained behavior-shaping artifacts: storage substrate, representational form, lineage, and behavioral authority. Storage remains important, but only as one field among others. Representational form distinguishes prose such as prompts, symbolic artifacts such as code, and distributed-parametric artifacts such as embeddings, adapters, and weights: the same retained lesson may be cheap to capture as prompt text but cheaper to execute and easier to test as symbolic control. Each form has its own default inspection method: prose can be read directly, symbolic artifacts can be tested or checked, and distributed-parametric artifacts usually require behavioral probes. When objects bundle several behavior-shaping parts, the vocabulary applies to the relevant operative part or consumption path.

We frame this as an architectural view over retained behavior-shaping artifacts. The view supports architectural review of efficiency, security, and sovereignty, and helps architects choose the appropriate representational form for retained behavior.

Keywords: agentic systems; LLM agents; persistent adaptation; agent memory; software architecture; context engineering

## 1. Introduction

Agentic systems do not adapt only by changing model weights. Their behavior is also shaped by prompts, repositories, tools, validators, configuration, routing systems, traces, and learned controllers. These retained artifacts shape future behavior in distinct ways, yet they are often discussed under broad labels such as memory, tool use, or prompt management.

Consider a coding agent that repeatedly mishandles dependency resolution: it installs incompatible versions, ignores lockfile constraints, or misses conflicts that appear only during tests. The surrounding system may retain the lesson as a prose reflection, project workflow, conflict-checking script, lockfile validator, derived prompt summary, or learned scoring weights.

These artifacts may all be lumped under broad labels, but they create different affordances and obligations for execution, review, invalidation, and rollback. A reflection is readable, but affects behavior only if retrieval and prompt interpretation carry it forward. A validator blocks execution cheaply and repeatably, and must be tested like control logic. A stale derived artifact can govern behavior after its apparent source has been fixed. Learned scoring weights require behavioral probes rather than reading one record.

The architectural question is therefore not only where retained state lives, but which retained form gives the system acceptable tradeoffs in efficiency, security, and sovereignty. Retained behavior-shaping artifacts can be modeled as architectural elements, or as retained state that defines, configures, connects, or constrains such elements; their properties matter because they determine how retained behavior is reviewed, enforced, and governed (Perry and Wolf, 1992). This paper captures those properties in four fields:

| Field | Examples | Why the architect cares |
|---|---|---|
| Storage substrate | Reflection in vector store or flat file; validator in repository; prompt summary in registry. | Determines access, deletion, versioning, and rollback paths. |
| Representational form | Prose reminder; prose prompt content; symbolic executable validator; dense-vector retrieval index. | Determines default inspection methods (reading, tests, or probes), review evidence, and recurring execution cost. |
| Lineage | Prompt summary as derived view of canonical workflow. | Determines what must be invalidated when the source changes. |
| Behavioral authority | Reflection as advice; prompt as instruction; validator as enforcement. | Records who consumes the artifact, through which channel, and with what force. |

The fields come from distinct architectural concerns. Storage substrate locates retained state; representational form captures how it acts. Lineage and behavioral authority distinguish source from derivative and advice from enforcement. The set is a compact record that keeps these concerns visible.

This paper makes three claims:

- Retained adaptation should be recorded at the level of behavior-shaping operative parts and consumption paths, not merely stored objects.
- Four architectural record fields--storage substrate, representational form, lineage, and behavioral authority--capture affordances and obligations that storage labels hide, and guide the assignment of review evidence, invalidation triggers, and rollback paths.
- The resulting record supports architectural design and review decisions about whether retained behavior should remain prose, become symbolic control, be exposed through retrieval, or be learned into numerical state.

For efficient, secure, and sovereign agentic systems, these fields expose recurring architectural risks. Efficiency risk, covering recurring cost, latency, context bloat, and sustainability, appears when retained lessons remain in recurring prompt or retrieval paths even though they could be compressed into cheaper symbolic checks, schemas, tests, or workflows. Security risk appears when untrusted or poisoned artifacts enter high-authority channels. Sovereignty risk appears when behavior depends on artifacts the system owner cannot inspect, regenerate, delete, or roll back, such as vendor checkpoints or hosted retrieval indexes (Couture and Toupin, 2019; Dale, 2025).

## 2. Retained Adaptation as an Architectural Concern

A retained behavior-shaping artifact is retained state that a later agentic loop can consume in a way that affects behavior. It enters the scope whenever it has been produced, selected, revised, or maintained in response to experience, supervision, evaluation, correction, or incident review. Below, **retained artifact** refers to this class unless otherwise specified. The inclusion boundary is behavioral consequence rather than implementation label.

Its **operative part** is the content, structure, parameterization, or behavior-affecting mechanism that a later model, runtime, router, validator, tool, or learning loop can consume or apply in a behavior-shaping way. Within this paper's vocabulary, operative parts may be prose, symbolic, or distributed-parametric. Some retained objects bundle several operative parts or are consumed through several authority paths, so the relevant unit of classification may be an operative part or consumption path, not the stored object as a whole.

A stored export or backup outside the system's consumption paths does not count merely because it is persisted. The same artifact counts once a later agentic loop can read, retrieve, execute, or learn from it in a behavior-shaping way. This broad scope is practical: in LLM-agent systems, adaptation often moves into the surrounding architecture rather than only into explicit memory stores.

Some artifacts, such as workflows or validators, may originate as ordinary architectural assets but enter the retained-adaptation scope once they are revised in response to such feedback.

## 3. Relation to Existing Classifications

Architecture work on ML-based systems already treats models, data, and AI-related design decisions as architectural concerns (Muccini and Vaidhyanathan, 2021; Franch et al., 2022). Agent-specific work classifies mechanisms — memories, tools, skills, rules, workflows, context-management procedures, learned adaptation — and surveys how they are stored, retrieved, compressed, and updated (Jia et al., 2025; Du, 2026; Jiang et al., 2025; Mei et al., 2025; Kang et al., 2025; Wang et al., 2025; Zhou et al., 2026; Zhang et al., 2026).

These classifications are valuable for grouping artifacts by mechanism kind, storage, retrieval, compression, or update procedure. This paper records what those categories leave implicit: what evidence is needed to review a retained artifact, what source changes invalidate it, what channel gives it force, what rollback path removes its effect, and how form shifts recurring execution cost. A mechanism label does not settle these — a "memory" can be low-authority prose advice, a derived high-priority prompt, a retrieval index, or learned scoring state, and the architectural obligations differ across those cases. Four record fields — substrate, form, lineage, authority — make those obligations explicit inside and across mechanism categories.

## 4. Storage Substrate: Where Retained State Lives

Storage substrate records where retained state persists: flat files, repositories, databases, vector stores, prompt registries, configuration services, audit logs, service objects, or model-artifact stores. It matters for access control, deletion, versioning, rollback, latency, and deployment.

However, the same substrate can host different operative forms and risks. A repository may contain prose workflows, symbolic validators, generated prompt views, route tables, and pointers to checkpoints. A vector store may package readable prose records together with dense-vector indexes and scoring procedures. Storage is therefore an operational field, not a sufficient representational or behavioral classification.

## 5. Representational Form

Representational form asks how an artifact's operative parts are encoded and consumed. The same dependency lesson may be retained as a prose reminder, an executable validator, or prose records surfaced through a dense-vector retrieval index; those choices shape execution cost, review evidence, and the invalidation and rollback they admit.

Prose carries content in natural language interpreted by language models. Symbolic form carries it in localized units whose consequences are specified by the artifact or surrounding system. Distributed-parametric form carries it in model-derived or learned numerical state consumed by model, retrieval, scoring, ranking, or policy procedures.

These are coarse families rather than genre taxonomies. When a retained object bundles several operative parts or is consumed through several authority paths, the representational-form field should classify the relevant operative parts rather than the stored object as a whole.

### Prose Artifacts

Prose artifacts include reflections, user facts, project notes, prompts, workflow descriptions, policies, playbooks, and incident reports. Generative-agent memory and verbal-reflection systems retain natural-language observations, reflections, or feedback for later retrieval and use (Park et al., 2023; Shinn et al., 2023). Their strength is flexibility: they are cheap to create, easy to revise, and naturally consumable by language models.

Their limitations follow from the same flexibility. Prose artifacts are interpreted under underspecified natural-language semantics, so their effect can vary with context, prompt position, retrieval order, and model behavior. They lack strict artifact-internal mechanisms for fixing scope, binding, precedence, exceptions, locality, and code/data separation, creating prompt-injection risk. Indirect prompt-injection work identifies the same problem: LLM-integrated applications "blur the line between data and instructions" (Greshake et al., 2023).

### Symbolic Artifacts

The term symbolic is architectural, not a claim about classical symbolic AI. The distinction is not syntax but operative semantics: a YAML file, Markdown document, or JSON object is symbolic only where a consumer assigns defined consequences to particular fields, values, or structures.

Symbolic artifacts make a different tradeoff from prose: they cost more to specify and cover less by default, but a correct specification can be fast, repeatable, and easy to test, enforce, and roll back. When the specification is wrong, the failure is systematic: a validator may reject legitimate exceptions, or a route table may encode stale tool assumptions.

### Distributed-Parametric Artifacts

Distributed-parametric artifacts include model checkpoints, adapters, embedding spaces, dense-vector indexes, reward models, learned controllers, and other parameterized components encoded across numerical parameters or dense representations (Du, 2026; Yu et al., 2026). The category does not imply identical lifecycle treatment for these artifacts; it marks the shared fact that operative behavior is not localized in directly inspectable symbolic units. They are consumed by numerical procedures such as forward passes, similarity scoring, ranking, and policy selection.

These artifacts differ from symbolic artifacts even when both are executed by machinery: their behavioral effect is induced by training, optimization, or model-derived dense representation rather than assigned to localized symbolic units.

### Inspection

Form sets the default inspection method: prose calls for reading and prompt review, symbolic artifacts for tests or static checks, and distributed-parametric artifacts for behavioral probes. Direct inspection can weaken in assembled or large-scale settings: a small validator may be easy to test, while a large rule system or retrieval pipeline can make the unit of review the assembly and ranking around individual records rather than any single record (Chen et al., 2024; Srivastava and He, 2025). Lineage and behavioral authority modulate how much evidence is enough: a prose note retrieved as advice differs from the same text inserted into a high-priority prompt.

## 6. Lineage and Behavioral Authority

Lineage records an artifact's review-relevant source dependencies and whether it is source material, a derived view, an index, a compiled artifact, an assembled package, or a learned update. Lineage here is not a full provenance model; it records the dependency information needed to invalidate, regenerate, or retire retained behavior.

Behavioral authority has three components: the consumer (a model, router, tool runtime, validator, human reviewer, or learning loop), the channel (retrieval, prompt assembly, execution, configuration, ranking, validation, or training), and the force (advice, instruction, enforcement, selection or ranking influence, or learning input). Audit records affect behavior only when a consumer acts on them; they are not themselves a force. Advice may be ignored; instruction enters an instruction channel; enforcement constrains execution; selection or ranking influence biases which artifact is consulted next; learning input feeds an automatic training pipeline that produces an updated model, adapter, retriever, or controller.

Retained objects often combine operative parts or authority paths. A prompt template may assemble prose instruction with symbolic schema constraints; a semantic-retrieval package may assemble prose records with distributed-parametric embeddings or scoring behavior; and a skill package may assemble prose guidance, code, tests, and activation metadata (Wang et al., 2024; Zheng et al., 2025). A Markdown prompt with required sections may be read by an LLM as prompt structure and instruction while validation code checks the same headings as required structure. In such cases, the architectural record should name the relevant operative parts and consumption paths because they create different affordances and obligations: deterministic execution, selective reuse, separate review, invalidation, or rollback.

The record exposes both repair targets and security failure modes for each retained artifact. If a dependency workflow changes while a stale prompt summary preserves the old procedure, repair requires invalidating the derived view and updating affected consumers. Security failures arise when untrusted prose enters high-authority prompts, stale derived views survive source changes, or opaque retrieval hides poisoned records.

## 7. Using the Vocabulary: Dependency Example

In practice, the vocabulary becomes a retained-adaptation record. To use it, identify retained artifacts; split bundled objects into operative parts or consumption paths; record substrate, form, lineage, and authority; then assign review evidence, invalidation triggers, and rollback or deletion paths. In the dependency-resolution example below, the first columns record the four fields (substrate and lineage merged); the last three columns are review consequences the architect assigns: what to do to gather review evidence, when to invalidate, and how to roll back or delete. Each row below shows the same dependency lesson retained in a different form; calling all of them "memory" would hide the distinct architectural profiles the four record fields expose:

| Artifact | Substrate / lineage | Form | Authority path / force | Review evidence | Invalidates when | Rollback / delete |
|---|---|---|---|---|---|---|
| Failure reflection | Vector store or file record; derived from run trace. | Prose; dense-vector path if indexed. | LLM via retrieval or prompt context; advice. | Read; probe retrieval. | Correction, deletion, or retirement. | Delete record; refresh index. |
| Project workflow | Repository or workflow store; canonical source. | Prose source; symbolic commands if present. | LLM or skill runtime; instruction or skill guidance. | Human review; freshness checks. | Policy or workflow change. | Version revert or replacement. |
| Conflict-check script | Repository artifact; source executable. | Symbolic executable. | Tool runtime or validator; enforcement. | Unit and integration tests. | Policy or tooling change. | Commit revert or feature flag. |
| Markdown prompt with required sections | Prompt registry; derived from workflow. | Prose instruction; symbolic section contract. | LLM prompt channel; instruction. Validator; enforcement. | Prompt review; validation and assembly tests. | Source workflow change. | Remove or regenerate registry entry. |
| Semantic-retrieval package | Vector store; assembled retrieval package. | Prose records; dense-vector embeddings and scoring path. | Retriever/ranker; selection or ranking influence. | Read records; probe retrieval and ranking. | Poisoning, drift, or retired sources. | Rebuild index or roll back deployment; verify hosted copies are removed. |

Each row admits a different action: delete and re-index records, version workflows, feature-flag validators, invalidate derived prompts, and rebuild or roll back retrieval packages.

The record reframes the design question. Instead of asking whether a dependency lesson is "in memory," the architect can ask whether its current form and authority are justified. Rare or uncertain lessons may stay as low-authority prose advice. Frequent, stable, or safety-critical lessons may be promoted to symbolic validation or workflow control. Lessons that require broad generalization may justify retrieval or learned numerical state when the loss of direct inspectability is acceptable.

## 8. Limitations and Future Work

The framework is a classification discipline, not a new memory mechanism or full lifecycle theory. The proposed fields are not exhaustive. Lineage and behavioral authority in particular were compressed for space.

A fuller lineage account should specify how canonical sources generate, refresh, and retire derived prompts, retrieval indexes, skill bundles, route entries, and audit surfaces, integrating with provenance and dependency-tracking work. A fuller behavioral-authority account should grade force levels, describe authority composition across multi-path artifacts, resolve contested authority among competing consumers, and trace how authority propagates across advice, instruction, enforcement, routing, audit, model behavior, and learning input.

The paper does not present empirical validation. A next step is to apply the record in design reviews and incident analyses of real agentic systems, testing whether different reviewers classify operative parts consistently, whether the record produces actionable design decisions, and whether obligations derived from it expose risks that storage labels alone would miss.

## 9. Conclusion

Persistent adaptation cannot be classified by storage substrate alone. Storage locates retained state; form, lineage, and authority determine how it acts and what review it admits. The resulting record supports architectural review of efficiency, security, and sovereignty, and gives design and cross-system comparison a precise vocabulary for those requirements.

The practical design question for each retained lesson is: should it remain quick-to-capture prose, become symbolic control, be surfaced through retrieval, or be learned into numerical state? Functionally related artifacts can differ sharply in cost, coverage, behavioral variance, and the review and rollback they admit. Naming those differences lets architects keep uncertain lessons as prose, move recurring or safety-critical lessons toward schemas, validators, tests, or workflow rules, and reserve retrieval or learned state for cases where coverage or generalization matters more than direct examination.

## References

Chen, Z., Xiang, Z., Xiao, C., Song, D., and Li, B. (2024). AgentPoison: Red-teaming LLM Agents via Poisoning Memory or Knowledge Bases. In Advances in Neural Information Processing Systems. URL https://openreview.net/forum?id=Y841BRW9rY.

Couture, S. and Toupin, S. (2019). What does the notion of "sovereignty" mean when referring to the digital? New Media & Society, 21(10), 2305--2322. DOI 10.1177/1461444819865984.

Dale, R. (2025). Sovereign AI in 2025. Natural Language Processing, 31(5), 1312--1321. DOI 10.1017/nlp.2025.10007.

Du, P. (2026). Memory for autonomous LLM agents: Mechanisms, evaluation, and emerging frontiers. URL https://arxiv.org/abs/2603.07670.

Franch, X., Martínez-Fernández, S., Ayala, C. P., and Gómez, C. (2022). Architectural decisions in AI-based systems: An ontological view. In Proceedings of the 15th International Conference on the Quality of Information and Communications Technology, pages 18--27. DOI 10.1007/978-3-031-14179-9_2.

Greshake, K., Abdelnabi, S., Mishra, S., Endres, C., Holz, T., and Fritz, M. (2023). Not what you've signed up for: Compromising real-world LLM-integrated applications with indirect prompt injection. In Proceedings of the 16th ACM Workshop on Artificial Intelligence and Security, pages 79--90. DOI 10.1145/3605764.3623985.

Jia, Z., Li, J., Kang, Y., Wang, Y., Wu, T., Wang, Q., Wang, X., Zhang, S., Shen, J., Li, Q., Qi, S., Liang, Y., He, D., Zheng, Z., and Zhu, S.-C. (2025). The AI hippocampus: How far are we from human memory? Transactions on Machine Learning Research. URL https://openreview.net/forum?id=Sk7pwmLuAY.

Jiang, P., Lin, J., Shi, Z., Wang, Z., He, L., Wu, Y., Zhong, M., Song, P., Zhang, Q., Wang, H., Xu, X., Xu, H., Han, P., Zhang, D., Sun, J., Yang, C., Qian, K., Wang, T., Hu, C., Li, M., Li, Q., Peng, H., Wang, S., Shang, J., Zhang, C., You, J., Liu, L., Lu, P., Zhang, Y., Ji, H., Choi, Y., Song, D., Sun, J., and Han, J. (2025). Adaptation of agentic AI: A survey of post-training, memory, and skills. URL https://arxiv.org/abs/2512.16301.

Kang, M., Chen, W.-N., Han, D., Inan, H. A., Wutschitz, L., Chen, Y., Sim, R., and Rajmohan, S. (2025). ACON: Optimizing context compression for long-horizon LLM agents. URL https://arxiv.org/abs/2510.00615.

Mei, L., Yao, J., Ge, Y., Wang, Y., Bi, B., Cai, Y., Liu, J., Li, M., Li, Z.-Z., Zhang, D., Zhou, C., Mao, J., Xia, T., Guo, J., and Liu, S. (2025). A survey of context engineering for large language models. URL https://arxiv.org/abs/2507.13334.

Muccini, H. and Vaidhyanathan, K. (2021). Software architecture for ML-based systems: What exists and what lies ahead. In Proceedings of the 1st IEEE/ACM Workshop on AI Engineering--Software Engineering for AI, pages 121--128. DOI 10.1109/WAIN52551.2021.00026.

Park, J. S., O'Brien, J. C., Cai, C. J., Morris, M. R., Liang, P., and Bernstein, M. S. (2023). Generative agents: Interactive simulacra of human behavior. In Proceedings of the 36th Annual ACM Symposium on User Interface Software and Technology. DOI 10.1145/3586183.3606763.

Perry, D. E. and Wolf, A. L. (1992). Foundations for the study of software architecture. ACM SIGSOFT Software Engineering Notes, 17(4), 40--52. DOI 10.1145/141874.141884.

Shinn, N., Cassano, F., Gopinath, A., Narasimhan, K., and Yao, S. (2023). Reflexion: Language agents with verbal reinforcement learning. In Advances in Neural Information Processing Systems 36. URL https://proceedings.neurips.cc/paper_files/paper/2023/hash/1b44b878bb782e6954cd888628510e90-Abstract-Conference.html.

Srivastava, S. S. and He, H. (2025). MemoryGraft: Persistent compromise of LLM agents via poisoned experience retrieval. URL https://arxiv.org/abs/2512.16962.

Wang, G., Xie, Y., Jiang, Y., Mandlekar, A., Xiao, C., Zhu, Y., Fan, L., and Anandkumar, A. (2024). Voyager: An open-ended embodied agent with large language models. Transactions on Machine Learning Research. URL https://openreview.net/forum?id=ehfRiF0R3a.

Wang, Z. Z., Mao, J., Fried, D., and Neubig, G. (2025). Agent workflow memory. In Proceedings of the 42nd International Conference on Machine Learning, PMLR 267:63897-63911. URL https://proceedings.mlr.press/v267/wang25bx.html.

Yu, Y., Yao, L., Xie, Y., Tan, Q., Feng, J., Li, Y., and Wu, L. (2026). Agentic memory: Learning unified long-term and short-term memory management for large language model agents. URL https://arxiv.org/abs/2601.01885.

Zhang, X., Wang, G., Cui, Y., Qiu, W., Li, Z., Zhu, B., and He, P. (2026). Experience compression spectrum: Unifying memory, skills, and rules in LLM agents. URL https://arxiv.org/abs/2604.15877.

Zheng, B., Fatemi, M. Y., Jin, X., Wang, Z. Z., Gandhi, A., Song, Y., Gu, Y., Srinivasa, J., Liu, G., Neubig, G., and Su, Y. (2025). SkillWeaver: Web agents can self-improve by discovering and honing skills. URL https://arxiv.org/abs/2504.07079.

Zhou, C., Chai, H., Chen, W., Guo, Z., Shan, R., Song, Y., Xu, T., Yang, Y., Yu, A., Zhang, W., Zheng, C., Zhu, J., Zheng, Z., Zhang, Z., Lou, X., Zhang, C., Fu, Z., Wang, J., Liu, W., Lin, J., and Zhang, W. (2026). Externalization in LLM agents: A unified review of memory, skills, protocols and harness engineering. URL https://arxiv.org/abs/2604.08224.
