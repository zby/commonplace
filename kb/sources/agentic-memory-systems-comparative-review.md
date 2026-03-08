# The fundamental split in agent memory is not storage format but who decides what to remember

Eleven systems for agent knowledge management reveal a design space defined by six architectural dimensions. The most consequential dimension is not the most obvious one (filesystem vs database) but the agency model: who controls what gets remembered, forgotten, and restructured. This choice cascades into every other architectural decision.

## The systems

Six database-oriented memory systems: **Mem0** (vector-first fact store with LLM-judged CRUD), **Graphiti** (bi-temporal knowledge graph on Neo4j), **Cognee** (pipeline-first graph+vector poly-store), **Letta/MemGPT** (agent-self-managed three-tier memory hierarchy), **A-MEM** (Zettelkasten-inspired note network with memory evolution), **AgeMem** (RL-trained unified LTM/STM management with six learnable memory operations).

Five filesystem-first knowledge systems: **Ars Contexta** (conversation-derived cognitive architecture with 249 research claims), **Thalo** (custom DSL with Tree-Sitter grammar and 27 validation rules), **ClawVault** (scored observations with session lifecycle and promotion pipelines), **Agent Skills** (instructional modules for context engineering), **commonplace** (this system -- methodology-as-content with typed notes and curated links).

## The six dimensions

### 1. Storage unit -- what is the atom of memory?

| System | Unit | Implications |
|--------|------|-------------|
| Mem0 | Isolated declarative fact ("user prefers dark mode") | Simplest to extract, no internal structure, found only by vector similarity |
| Graphiti | Entity node + relationship edge in a property graph | Rich queryable structure, requires graph database infrastructure |
| Cognee | Knowledge graph triplet (subject-predicate-object) via Pydantic schemas | Schema-controlled extraction, domain-customizable, but rigid |
| Letta | Text block with label and character limit (core), searchable record (archival) | Hybrid: structured blocks for hot state, unstructured archive for cold |
| A-MEM | Seven-field note (content, keywords, tags, context, embedding, links, timestamp) | Fixed universal schema avoids domain-specific modeling; richer than facts, flatter than graphs |
| AgeMem | Key-value pair in LTM store (task-state facts); text blocks in STM (active context) | Simple storage unit; value comes from learned policy for when to store/retrieve, not from unit structure |
| Ars Contexta | Wiki-style note with propositional links and relationship markers | Rich link semantics, requires elaborative encoding at write time |
| Thalo | Typed entry parsed by formal grammar into AST nodes | Compiler-grade validation, but requires custom tooling ecosystem |
| ClawVault | Scored observation (type + confidence + importance) that promotes to vault knowledge | Lightweight capture with explicit promotion pathway |
| Agent Skills | Instructional module with activation triggers | Not a memory system per se -- influences reasoning, doesn't store knowledge |
| commonplace | Typed markdown note with frontmatter, curated links, and semantic descriptions | Progressive formalization from text to note to structured-claim |

The spectrum runs from minimal (Mem0's isolated facts) through structured (A-MEM's notes, Letta's blocks) to maximally relational (Graphiti's graph, Cognee's triplets, Ars Contexta's propositional network). The key trade-off: richer units cost more to create but support more sophisticated retrieval and reasoning.

### 2. Agency model -- who decides what to remember?

This is the most consequential dimension. Four positions:

**Agent-self-managed (Letta).** The agent decides what to write to core memory, what to archive, what to search for. Memory management is part of reasoning. Advantage: the agent has the most context about what matters. Risk: quality depends entirely on model capability, and the agent burns reasoning tokens on memory housekeeping.

**Developer-managed external service (Mem0, Graphiti, Cognee).** A separate system extracts, stores, and retrieves memories. The agent calls an API; the memory system handles curation. Advantage: predictable behavior, separable from agent logic. Risk: the memory system guesses what matters without the agent's full reasoning context.

**Human+agent collaborative (Ars Contexta, Thalo, ClawVault, commonplace).** Knowledge artifacts are co-produced -- the agent writes, validation checks, human judgment gates promotion. Advantage: highest curation quality. Risk: doesn't scale without automation, and the human becomes a bottleneck.

**RL-trained self-managed (AgeMem).** Like Letta, the agent decides what to remember. Unlike Letta, the memory management policy is trained through RL rather than relying on the base model's instruction-following. Advantage: the policy improves from experience, and post-training agents use memory operations significantly more (Add operations increase from 0.92 to 1.64 per episode). Risk: the learned policy is opaque — stored in model weights, not inspectable or incrementally refinable — and [the learning depends on task-completion oracles](../notes/memory-management-policy-is-learnable-but-oracle-dependent.md) that may not exist in open-ended domains.

**A-MEM** sits between positions: the agent triggers memory creation, but an automated pipeline handles linking and evolution without explicit agent decisions.

**Agent Skills** is the outlier: it shapes the agent's reasoning through loaded instructions rather than managing persistent memory at all.

### 3. Link structure -- how is knowledge connected?

| System | Link model | Navigability |
|--------|-----------|-------------|
| Mem0 | None -- facts are isolated, found by vector similarity only | Zero navigability; pure retrieval |
| Graphiti | Typed relationship edges in property graph (extracted by LLM) | High navigability via graph traversal; relationships are first-class |
| Cognee | Subject-predicate-object triplets via schema-driven extraction | Navigable within schema; constrained by predefined relationship types |
| Letta | None between blocks; implicit via shared context window | No persistent link structure |
| A-MEM | Untyped embedding-similarity links, LLM-filtered | Adjacency, not connection -- links exist but carry no articulated reason |
| AgeMem | None -- LTM entries are independent key-value pairs | Zero navigability; pure retrieval by key match |
| Ars Contexta | Propositional wiki-links with relationship semantics (causes, enables, contradicts) | Highest navigability; links are evaluable claims |
| Thalo | Grammar-typed links without relationship semantics | Structural but not semantic |
| ClawVault | Graph neighbors via observation co-occurrence | Weak emergent links |
| commonplace | Markdown links with semantic context phrases (extends, grounds, contradicts) | High navigability; relationship is articulated in prose |

The link structure dimension reveals the deepest theoretical split. Mem0 and Letta have no links at all -- memory is a search index. A-MEM has links but they are "adjacency, not connection" (embedding similarity filtered by LLM confidence, with no articulated reason). Graphiti and Cognee have typed relationships but they are extracted automatically. Only Ars Contexta and commonplace require articulated reasons for every link -- what the Ars Contexta research calls the difference between an "adjacency engine" and a "knowledge system."

### 4. Temporal model -- how is change over time handled?

| System | Temporal approach |
|--------|------------------|
| Mem0 | None -- facts are current-state only; updates overwrite |
| Graphiti | Bi-temporal: valid_at/invalid_at on every edge; point-in-time queries; contradictions resolved through temporal invalidation |
| Cognee | Optional temporal_cognify; no invalidation model |
| Letta | Implicit via conversation history in recall memory; no temporal reasoning over knowledge |
| A-MEM | Timestamps on notes; memory evolution updates context and tags but doesn't track what changed |
| AgeMem | None -- LTM entries are current-state; no versioning or invalidation |
| Ars Contexta | None explicit; git history provides implicit versioning |
| Thalo | None explicit; git history |
| ClawVault | Session timestamps; observation dates drive promotion-by-recurrence |
| commonplace | None explicit; git history; status field (seedling/current/outdated) marks lifecycle |

Graphiti is the clear outlier here -- its bi-temporal model is a genuine capability that cannot be replicated over flat files. When "user works at Company A" is superseded by "user works at Company B," Graphiti invalidates the old edge with a timestamp rather than deleting it, enabling queries like "where did the user work in January?" This is the strongest argument for database infrastructure in the entire survey.

### 5. Curation operations -- what happens to old knowledge?

| System | Operations | What's missing |
|--------|-----------|---------------|
| Mem0 | ADD, UPDATE, DELETE, NOOP (LLM-judged per fact) | No splitting, synthesis, or regrouping |
| Graphiti | Extract, deduplicate, invalidate (temporal) | No synthesis or reformulation |
| Cognee | Classify, chunk, extract, summarize, embed; memify promises pruning/reweighting but ships simpler | Gap between documented ambitions and implementation |
| Letta | Agent writes/edits/archives blocks | Unbounded -- whatever the agent decides, limited by model capability |
| A-MEM | Construct, link, evolve (update context and tags on existing notes) | Evolution is the unique operation -- notes change when new notes arrive |
| AgeMem | Add, Update, Delete (LTM); Retrieve, Summary, Filter (STM) -- all RL-trained | Operations are hand-crafted tools; the [policy for when to use them is learned](../notes/memory-management-policy-is-learnable-but-oracle-dependent.md). No synthesis or evolution of existing entries |
| Ars Contexta | Record, Reduce, Reflect, Reweave, Verify, Rethink (6 Rs pipeline) | Most complete curation lifecycle; each phase has a separate skill |
| ClawVault | Extract, score, promote, reflect | Promotion-by-recurrence is a concrete, testable curation heuristic |
| commonplace | Write, connect, validate, convert (type promotion) | Manual curation; no automated evolution or promotion |

A-MEM's memory evolution is distinctive: when a new note arrives, existing notes in its neighborhood have their context descriptions and tags updated. The ablation study shows this improves multi-hop reasoning more than link generation alone. No other system modifies existing knowledge in response to new knowledge arriving (Mem0's UPDATE replaces facts; A-MEM's evolution enriches neighboring notes).

### 6. Extraction schema -- how much structure is imposed on incoming data?

| System | Schema approach |
|--------|---------------|
| Mem0 | Free-form fact extraction via LLM; no schema |
| Graphiti | Generic entity/relationship extraction; LLM decides types |
| Cognee | Custom Pydantic schemas define exactly what entities and relationships to extract |
| Letta | No extraction -- agent writes blocks directly |
| A-MEM | Fixed universal schema (7 fields); avoids domain-specific modeling |
| AgeMem | No explicit schema -- agent decides what key-value pairs to store via learned policy |
| Ars Contexta | Conversation-derived; schemas generated from user description |
| Thalo | Formal grammar with typed entities and metadata fields |
| ClawVault | Fixed observation types (decision, lesson, preference, commitment, fact, relationship) |
| commonplace | Progressive: text (no schema) to note (frontmatter) to structured-claim (sections) |

The spectrum runs from no schema (Mem0, Letta) through fixed universal schema (A-MEM, ClawVault) to domain-customizable (Cognee, Thalo, Ars Contexta). Commonplace is unusual in making schema progression explicit -- the same content can start as raw text and progressively acquire structure as understanding develops.

## Convergences

**The filesystem-first consensus breaks.** The related-systems-index noted convergence on "filesystem over databases" across the four previously documented systems. The five new systems break this pattern decisively. Mem0, Graphiti, Cognee, and Letta all require database infrastructure (vector stores, graph databases, PostgreSQL). Only A-MEM uses in-memory storage with no persistent database requirement. The convergence on filesystem-first was a sampling artifact -- we were looking at systems in our own lineage.

**Everyone automates extraction, nobody automates synthesis.** Every system that processes incoming data (Mem0, Graphiti, Cognee, A-MEM, ClawVault, Ars Contexta) can automatically extract structured knowledge from unstructured input. None of them can automatically synthesize across existing knowledge to produce novel insights, reformulate existing notes for clarity, or recognize when two separate threads should merge. Cognee's memify phase promises this but ships simpler. This boundary -- extraction yes, synthesis no -- appears to be a hard capability limit of current LLM-based automation.

**Context efficiency trade-off at ingestion.** Mem0, Graphiti, Cognee, and Ars Contexta all invest substantial LLM compute at ingestion time (multiple calls per item) to produce structured knowledge that is cheap to retrieve. This is the same bet: pay upfront in tokens and latency to save at query time. The filesystem-first systems (Thalo, commonplace) make the opposite bet -- minimal ingestion cost, richer retrieval-time reasoning.

**Progressive disclosure appears everywhere.** Whether the system is database-backed or filesystem-backed, every system that handles non-trivial knowledge volumes implements some form of "load summaries first, details on demand." Mem0 returns relevant facts. Letta keeps core memory small and archives the rest. Agent Skills loads skill names at startup, full content on activation. Commonplace loads descriptions from frontmatter before full notes. This is the strongest convergence in the survey.

## Divergences

**The agency question is the deepest split.** Storage format (files vs database) is obvious but secondary -- it follows from what you're trying to do. The agency question (who decides what to remember) is prior because it determines the entire system architecture:

- If the agent manages its own memory (Letta), you need memory operations as tools and the agent must reason about what to store.
- If a service manages memory (Mem0, Graphiti, Cognee), you need extraction pipelines and reconciliation logic, and you accept that the service will sometimes get it wrong because it lacks the agent's reasoning context.
- If humans co-manage memory (commonplace, Thalo, Ars Contexta), you get the highest quality but the lowest throughput.
- If the agent learns its own policy through RL (AgeMem), you get adaptive memory management that improves from experience, but the policy is opaque and the training requires a clear oracle.

No system has found a way to combine high agency (the rememberer has full context) with high throughput (memory management doesn't consume reasoning budget) and high quality (what's remembered is actually useful). AgeMem comes closest: post-training, the agent has full context, the policy is fast (baked into weights), and quality improves measurably. But the quality is verified only against task-completion benchmarks in closed domains, the training is expensive, and the learned policy is opaque. The trilemma relaxes when you have a clear oracle; without one, it holds.

**Navigability vs retrieval.** The link structure dimension reveals two fundamentally different theories of knowledge access. Mem0, Graphiti, and Cognee treat knowledge as something you search for -- vector similarity, graph queries, BM25. Ars Contexta and commonplace treat knowledge as something you navigate -- follow links, traverse relationships, reason along connections. A-MEM occupies the middle ground with links that exist but carry no articulated reason. The A-MEM benchmark results show that search-optimized systems score well on QA tasks. But QA accuracy does not measure whether the knowledge structure supports agent reasoning, and no benchmark tests for that. The two approaches may optimize for different things.

**Letta's convergence toward files is a signal.** Letta started as a database-first system (PostgreSQL for everything) and is now evolving toward git-backed memory where blocks become version-controlled files. This is independent convergence on the files-as-source-of-truth thesis from a system with no exposure to the filesystem-first community. It suggests that even database-first systems eventually discover the advantages of version control, diffability, and tooling interoperability that files provide.

**The curation frontier.** The most revealing divergence is in what happens to knowledge over time. Mem0 overwrites. Graphiti invalidates temporally. A-MEM evolves neighbors. AgeMem learns curation policy through RL. ClawVault promotes by recurrence. Commonplace relies on human judgment. Each is a different theory of knowledge lifecycle, and none is complete. AgeMem is the only system where curation improves from experience, but the improvement is opaque and oracle-dependent. The hardest unsolved problem -- automated synthesis and reformulation -- is attempted by none of them in production.

## Implications for claw design

**What we got right:**

- *Curated links with articulated reasons.* Only two systems in the survey (Ars Contexta and commonplace) require semantic link justification. A-MEM's benchmark success with untyped links does not refute this -- it shows that adjacency is sufficient for QA retrieval, not that it's sufficient for agent reasoning. Our bet is that navigability matters for the harder tasks.
- *Progressive formalization.* The text-to-note-to-structured-claim pathway is unique in the survey. Every other system commits to a schema at write time. Our approach lets understanding develop before structure is imposed.
- *Filesystem as source of truth.* Letta's convergence toward git-backed memory is independent validation. But we should be honest that this choice forecloses temporal queries and graph traversal that Graphiti demonstrates are genuinely useful.

**What we're missing:**

- *Automated memory evolution.* A-MEM's most valuable contribution is that existing notes update when new notes arrive. We have nothing like this. When a new note is connected, the existing notes it connects to don't change. This means our knowledge graph accretes but doesn't self-organize. A `/evolve` operation that updates neighboring notes' descriptions and context phrases when new connections form would be the highest-value automation we could add.
- *Temporal reasoning.* Graphiti's bi-temporal model handles a real problem we ignore: knowledge changes over time, and the history of change is itself knowledge. Our status field (seedling/current/outdated) is a crude approximation. Git history provides raw data but no queryable temporal model.
- *Session lifecycle.* ClawVault's wake/sleep/checkpoint/handoff cycle solves context death concretely. We have no session infrastructure. The workshop layer we've theorized needs to ship.
- *Promotion heuristics.* ClawVault's "seen twice on different dates" rule for promoting observations to durable knowledge is a testable automation. Our log.md has no promotion pathway beyond human review.

**The strategic question:**

The survey reveals that the agent memory space is splitting into two camps with different assumptions. The database-first camp (Mem0, Graphiti, Cognee) optimizes for retrieval at scale, accepts infrastructure complexity, and automates curation through pipelines. The filesystem-first camp (Thalo, Ars Contexta, commonplace) optimizes for inspectability and human understanding, accepts scaling limits, and relies on curated structure.

Our position -- filesystem-first with curated links and progressive formalization -- is well-founded but faces a real challenge: as knowledge volume grows, manual curation will not scale. The answer is not to abandon curation for automation (which sacrifices navigability for retrieval) but to automate the curation itself. A-MEM's memory evolution, ClawVault's promotion-by-recurrence, and Ars Contexta's 6 Rs pipeline each point toward pieces of what automated curation could look like. The open problem is assembling these pieces into a system that maintains link quality and navigability while operating at scale without human bottlenecks.
