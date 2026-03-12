# Connection Report: Lessons from Building AI Agents for Financial Services

**Source:** [Lessons from Building AI Agents for Financial Services](kb/sources/lessons-from-building-ai-agents-for-financial-services-2015174818497437834.md)
**Ingest report:** [Ingest: Lessons from Building AI Agents for Financial Services](kb/sources/lessons-from-building-ai-agents-for-financial-services-2015174818497437834.ingest.md)
**Date:** 2026-03-09
**Depth:** standard

## Phase 1: Understanding

This is a captured X thread by @nicbstme, a practitioner who built Fintool (an AI agent for professional investors) over two years. The source covers 11 architectural lessons. Key themes:

1. **Skills as product** -- markdown-based skills are the product surface, not the model. Non-engineers write skills. No deployment needed. Copy-on-write shadowing (private > shared > public).
2. **Model will eat scaffolding** -- designing for obsolescence; skills are temporary, to be deleted when models absorb the capability.
3. **Filesystem-first architecture** -- S3 as source of truth, PostgreSQL as derived index. User memories, watchlists, skills all live as files.
4. **Context is the product** -- normalizing heterogeneous financial data into clean markdown/CSV/JSON for agent consumption. Chunking strategy matters.
5. **Evaluation is non-optional** -- ~2,000 domain-specific test cases. PR blocked if eval score drops >5%. Adversarial grounding tests.
6. **Sandboxing** -- isolated execution environments for each user, pre-warmed.
7. **Long-running task orchestration** -- Temporal for durable workflow execution.
8. **User memories as injectable markdown** -- a simple markdown file users edit, injected into every conversation.

The central thesis: "The model is not your product. The experience around the model is your product."

## Discovery Trace

**Index scan:**
- Read kb/notes/index.md -- 142 entries scanned. Flagged candidates:
  - [files-not-database](kb/notes/files-not-database.md) -- filesystem-first architecture directly matches S3-first claim
  - [skills-derive-from-methodology-through-distillation](kb/notes/skills-derive-from-methodology-through-distillation.md) -- skills-as-product theme, but Fintool's skills derive from practitioner expertise not methodology
  - [methodology-enforcement-is-constraining](kb/notes/methodology-enforcement-is-constraining.md) -- skills as constraining gradient
  - [bitter-lesson-boundary](kb/notes/bitter-lesson-boundary.md) -- "model eats scaffolding" is the bitter lesson applied to agent infrastructure
  - [oracle-strength-spectrum](kb/notes/oracle-strength-spectrum.md) -- evaluation methodology, oracle hardening
  - [context-efficiency-is-the-central-design-concern](kb/notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) -- "context is the product" theme
  - [agent-statelessness-makes-routing-architectural](kb/notes/agent-statelessness-makes-routing-architectural-not-learned.md) -- skills as permanent infrastructure
  - [deploy-time-learning-the-missing-middle](kb/notes/deploy-time-learning-the-missing-middle.md) -- verifiability gradient, constraining mechanisms
  - [inspectable-substrate-not-supervision](kb/notes/inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md) -- inspectable repo artifacts
  - [llm-context-is-a-homoiconic-medium](kb/notes/llm-context-is-a-homoiconic-medium.md) -- skills/memories/data all "just files"
  - [three-space-agent-memory-maps-to-tulving-taxonomy](kb/notes/three-space-agent-memory-maps-to-tulving-taxonomy.md) -- user memories architecture
  - [automated-tests-for-text](kb/notes/automated-tests-for-text.md) -- testing/evaluation
  - [error-correction-works-above-chance-oracles](kb/notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) -- evaluation amplification
  - [related-systems/agent-skills-for-context-engineering](kb/notes/related-systems/agent-skills-for-context-engineering.md) -- skill architecture convergence
  - [related-systems/clawvault](kb/notes/related-systems/clawvault.md) -- memory architecture comparison
  - [related_works/granular-software](kb/notes/related_works/granular-software.md) -- sandbox as agent environment
  - [related_works/evans-ai-components-deterministic-system](kb/notes/related_works/evans-ai-components-deterministic-system.md) -- modeling vs classification, constraining

**Topic indexes:**
- Read [related-systems-index](kb/notes/related-systems/related-systems-index.md) -- confirmed filesystem-over-databases convergence pattern across independent systems; Fintool adds commercial-scale evidence
- Read [kb-design](kb/notes/kb-design.md) (via index candidates) -- no additional candidates beyond index scan

**Semantic search:** (via qmd)
- query "skills as markdown files, model eats scaffolding, filesystem-first agent architecture" --collection notes -n 15:
  - [agent-skills-for-context-engineering](kb/notes/related-systems/agent-skills-for-context-engineering.md) (93%) -- strong, skill architecture overlap
  - [instruction-specificity-should-match-loading-frequency](kb/notes/instruction-specificity-should-match-loading-frequency.md) (51%) -- progressive disclosure convergence
  - [files-not-database](kb/notes/files-not-database.md) (46%) -- already flagged
  - [instructions-are-skills-without-automatic-routing](kb/notes/instructions-are-skills-without-automatic-routing.md) (46%) -- skill format similarity but too tangential
  - [related-systems-index](kb/notes/related-systems/related-systems-index.md) (45%) -- already read
  - [skills-derive-from-methodology](kb/notes/skills-derive-from-methodology-through-distillation.md) (44%) -- already flagged
  - [granular-software](kb/notes/related_works/granular-software.md) (39%) -- sandbox framing

- query "evaluation testing domain-specific evals verification financial agents production monitoring" --collection notes -n 15:
  - [inspectable-substrate](kb/notes/inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md) (91%) -- strong, eval/verification theme
  - [quality-signals-for-kb-evaluation](kb/notes/quality-signals-for-kb-evaluation.md) (50%) -- evaluation methodology but KB-specific, weak connection
  - [evans-ai-components](kb/notes/related_works/evans-ai-components-deterministic-system.md) (38%) -- modeling vs classification
  - [methodology-enforcement-is-constraining](kb/notes/methodology-enforcement-is-constraining.md) (35%) -- already flagged
  - [unit-testing-llm-instructions](kb/notes/unit-testing-llm-instructions-requires-mocking-the-tool-boundary.md) (34%) -- testing theme, weak connection

- query "context normalization data pipeline chunking retrieval agent knowledge" --collection sources -n 10:
  - Self (93%) -- expected
  - [graphiti-temporal-knowledge-graph-ingest](kb/sources/graphiti-temporal-knowledge-graph-ingest.md) (55%) -- knowledge graph, different approach
  - [context-engineering-ai-agents-oss-ingest](kb/sources/context-engineering-ai-agents-oss-ingest.md) (38%) -- context engineering practices
  - [koylanai-personal-brain-os-ingest](kb/sources/koylanai-personal-brain-os.ingest.md) (51%) -- parallel practitioner, already flagged

- query "skills markdown files domain expertise operational procedures model scaffolding" --collection sources -n 10:
  - Self (93%) -- expected
  - [koylanai-personal-brain-os-ingest](kb/sources/koylanai-personal-brain-os.ingest.md) (51%) -- already flagged

**Keyword search:**
- grep "sandbox|sandboxing" kb/notes/ -- found [agent-skills-for-context-engineering](kb/notes/related-systems/agent-skills-for-context-engineering.md), [granular-software](kb/notes/related_works/granular-software.md) (already flagged)
- grep "scaffold|obsolescence|model.*eat" kb/notes/ -- found [agent-statelessness](kb/notes/agent-statelessness-makes-routing-architectural-not-learned.md) (already flagged), [operational-signals-that-a-component-is-a-relaxing-candidate](kb/notes/operational-signals-that-a-component-is-a-relaxing-candidate.md) (related to bitter lesson)
- grep "user memor|personali|preference" kb/notes/ -- found [clawvault](kb/notes/related-systems/clawvault.md) (already flagged), [three-space-memory](kb/notes/three-space-agent-memory-maps-to-tulving-taxonomy.md) (already flagged)

**Link following:**
- From [files-not-database](kb/notes/files-not-database.md) -- links to [what-works](kb/notes/what-works.md), [koylanai-personal-brain-os](kb/sources/koylanai-personal-brain-os.ingest.md) -- confirms convergence cluster
- From [bitter-lesson-boundary](kb/notes/bitter-lesson-boundary.md) -- links to [oracle-strength-spectrum](kb/notes/oracle-strength-spectrum.md), [deploy-time-learning](kb/notes/deploy-time-learning-the-missing-middle.md) -- confirms evaluation/verification cluster
- From [agent-skills-for-context-engineering](kb/notes/related-systems/agent-skills-for-context-engineering.md) -- already links to [instruction-specificity-should-match-loading-frequency](kb/notes/instruction-specificity-should-match-loading-frequency.md), [bitter-lesson-boundary](kb/notes/bitter-lesson-boundary.md), [oracle-strength-spectrum](kb/notes/oracle-strength-spectrum.md)
- From [related-systems-index](kb/notes/related-systems/related-systems-index.md) -- notes convergence on filesystem-first; Fintool is additional production-grade evidence

## Connections Found

### Strong connections (pass articulation test clearly)

1. **[files-not-database](kb/notes/files-not-database.md)** -- **exemplifies at production scale**: Fintool's S3-first architecture is the files-not-database claim validated at commercial scale. S3 as source of truth, PostgreSQL as derived index for fast queries, user data (memories, watchlists, skills) stored as YAML/markdown files. The note argues files beat databases for agent KBs; Fintool demonstrates this with 11-nines durability and real paying users. The "derived indexes for capabilities files alone can't provide" pattern is exactly what Fintool built with Lambda-synced PostgreSQL.

2. **[bitter-lesson-boundary](kb/notes/bitter-lesson-boundary.md)** -- **exemplifies the relaxing prediction**: The "model will eat your scaffolding" section is the bitter lesson applied to agent infrastructure. The author predicts basic skills will become one-liners in two years as models improve. He even describes the response: "write skills, delete them when unnecessary, build new ones for harder problems." This maps onto the codify-for-current-leverage-not-permanence heuristic. Fiscal period normalization (10,000+ company calendars) is a clean example of a calculator-regime component that models will NOT eat -- the spec IS the problem.

3. **[Agent Skills for Context Engineering](kb/notes/related-systems/agent-skills-for-context-engineering.md)** -- **provides production evidence for shared patterns**: Fintool's skill architecture independently converges with the Agent Skills framework: markdown files with YAML frontmatter, progressive disclosure (discover metadata first, load full content on use), SQL discovery with lazy loading. Agent Skills identifies "hosted agent infrastructure (sandboxing, warm pools)" as an area they cover deeply; Fintool provides the production implementation detail. Both systems validate the same context-as-finite-resource framing.

4. **[llm-context-is-a-homoiconic-medium](kb/notes/llm-context-is-a-homoiconic-medium.md)** -- **exemplifies without naming**: Skills, memories, and watchlists are all "just files" -- the same markdown serves as content and agent instructions. The copy-on-write skill shadowing system works because skills are text files, not compiled code. The author writes: "Skills tell the agent how to do things. Memories tell it what the user cares about. Both are just files." This is homoiconicity described as production architecture.

5. **[skills-derive-from-methodology-through-distillation](kb/notes/skills-derive-from-methodology-through-distillation.md)** -- **provides a counter-example**: Fintool's skills are written by analysts and customers, not distilled from a methodology KB. A portfolio manager with 500 DCF valuations encodes their methodology directly in markdown. This is distillation from human expertise, not from written methodology notes -- a different distillation pathway the KB note should account for. The caveat "Not all skills are distilled from methodology" already acknowledges this, but Fintool shows that practitioner-authored skills may be the dominant mode in product contexts.

6. **[deploy-time-learning-the-missing-middle](kb/notes/deploy-time-learning-the-missing-middle.md)** -- **exemplifies the full gradient**: Fintool demonstrates multiple grades of the verifiability gradient in production: restructured prompts (skills as markdown), structured output schemas (metadata-driven filtering), eval-driven development (~2,000 test cases, PR blocked on eval regression), and deterministic modules (fiscal period normalization, parsing pipeline with quality scoring). The "model will eat your scaffolding" thesis maps onto the constrain/relax cycle -- codify for current leverage, relax back when models absorb the capability.

7. **[context-efficiency-is-the-central-design-concern-in-agent-systems](kb/notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md)** -- **validates from production**: "Context is the product" echoes the note's central claim. Fintool's entire data normalization pipeline (heterogeneous financial data into clean markdown/CSV/JSON) exists because context quality determines agent quality. Their SQL skill discovery (lazy loading, metadata-driven filtering) is progressive disclosure driven by context budget constraints. Their chunking strategy ("bad chunks = bad answers") is context engineering applied to retrieval.

8. **[oracle-strength-spectrum](kb/notes/oracle-strength-spectrum.md)** -- **exemplifies oracle hardening in practice**: Fintool's evaluation infrastructure is oracle hardening at scale: ~2,000 test cases manufacturing hard oracles (ticker disambiguation, fiscal period normalization, numeric precision), adversarial grounding tests (planting false data to verify hallucination resistance) amplifying oracle strength, and production monitoring detecting drift. Tables below 90% confidence get flagged for review -- quality scoring as soft oracle. PR blocked if eval drops >5% -- a hard oracle gate on deployment.

### Moderate connections (genuine but narrower)

9. **[inspectable-substrate-not-supervision-defeats-the-blackbox-problem](kb/notes/inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md)** -- **exemplifies inspectable substrate choice**: Fintool chose S3/files (inspectable, diffable, versionable) over databases (less inspectable) as the substrate for skills, memories, and user data. "YAML files are human-readable. You can debug with `cat`." This is the inspectable substrate argument applied to production agent architecture -- the same property that the note claims defeats the blackbox problem.

10. **[three-space-agent-memory-maps-to-tulving-taxonomy](kb/notes/three-space-agent-memory-maps-to-tulving-taxonomy.md)** -- **partially exemplifies the knowledge/self separation**: Fintool separates knowledge (financial data, normalized filings), self/preferences (UserMemories.md -- "I focus on small-cap value stocks"), and operational/procedural (skills -- "how to do a DCF"). The separation is implicit in their architecture (S3 mount points: public/shared/private) rather than theorized. Not a full three-space implementation, but the structural separation exists.

11. **[Koylanai Personal Brain OS](kb/sources/koylanai-personal-brain-os.ingest.md)** -- **parallel practitioner in a different domain**: Both independently arrive at filesystem-as-knowledge-base, markdown-as-universal-format, progressive disclosure, and skills-as-product. Koylanai builds for personal productivity; Fintool for commercial finance. Convergence across domains strengthens the signal that these patterns are durable. Fintool adds the production layer (S3 + Lambda sync + PostgreSQL) that Koylanai's Git-only approach doesn't need at personal scale.

12. **[related-systems-index](kb/notes/related-systems/related-systems-index.md)** -- **provides additional convergence evidence**: The index already documents convergence across independent systems on filesystem-first, progressive disclosure, and start-simple. Fintool adds commercial production-scale evidence for all three patterns, from a domain (financial services) with zero error tolerance -- strengthening the convergence signal.

13. **[Granular Software](kb/notes/related_works/granular-software.md)** -- **shares the sandbox-as-agent-environment framing**: Both Fintool and Granular Software treat the sandbox not just as a security boundary but as the agent's programmable world. Fintool's "each user gets their own isolated environment -- the agent can do whatever it wants in there" parallels Granular's "the sandbox becomes the agent's environment."

**Bidirectional candidates** (reverse link also worth adding):
- [files-not-database](kb/notes/files-not-database.md) <-> source -- **exemplifies**: the note already cites Koylanai; Fintool is stronger production evidence
- [bitter-lesson-boundary](kb/notes/bitter-lesson-boundary.md) <-> source -- **exemplifies**: fiscal period normalization as arithmetic, scaffolding-eating as relaxing
- [oracle-strength-spectrum](kb/notes/oracle-strength-spectrum.md) <-> source -- **exemplifies**: adversarial grounding is oracle manufacturing; PR-blocking is oracle-gated deployment
- [related-systems-index](kb/notes/related-systems/related-systems-index.md) <-> source -- convergence evidence from commercial production

## Rejected Candidates

- **[agent-statelessness-makes-routing-architectural](kb/notes/agent-statelessness-makes-routing-architectural-not-learned.md)** -- While Fintool's skill architecture is permanent infrastructure, the source doesn't discuss agent statelessness or routing as a design concern. The connection would be "skills are permanent" which is too generic.
- **[methodology-enforcement-is-constraining](kb/notes/methodology-enforcement-is-constraining.md)** -- The constraining gradient (instruction -> skill -> hook -> script) is about methodology enforcement in a KB context. Fintool's skills are product features for domain experts, not methodology enforcement. The structural similarity is real but the purposes diverge enough to make the connection misleading.
- **[automated-tests-for-text](kb/notes/automated-tests-for-text.md)** -- Fintool's evaluation tests financial agent output quality, not text artifact structure. Different testing targets, different test pyramid.
- **[error-correction-works-above-chance-oracles](kb/notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md)** -- Fintool's adversarial grounding tests are conceptually related to oracle amplification but the connection is too abstract to be useful -- the note is about error correction theory, Fintool describes a specific testing practice.
- **[ClawVault](kb/notes/related-systems/clawvault.md)** -- Both have memory/preferences systems, but ClawVault's session lifecycle and observation pipelines are fundamentally different from Fintool's simple injectable markdown file. Surface similarity only.
- **[Evans AI Components](kb/notes/related_works/evans-ai-components-deterministic-system.md)** -- Evans' modeling/classification distinction maps vaguely to Fintool's "model eats scaffolding" but the connection doesn't pass the articulation test -- Evans is about separating deterministic classification from exploratory modeling, not about temporal obsolescence of scaffolding.
- **[constraining-during-deployment-is-continuous-learning](kb/notes/constraining-during-deployment-is-continuous-learning.md)** -- Tangential; Fintool doesn't frame its work as continuous learning.

## Index Membership

- **[kb-design](kb/notes/kb-design.md)** -- Fintool's files-first architecture, skill system, and progressive disclosure are production evidence for KB design patterns documented in this area
- **[related-systems-index](kb/notes/related-systems/related-systems-index.md)** -- Fintool is a comparable system that should be tracked. However, it's a source snapshot (not a repo we can clone), so it would get the lightweight coverage tier (snapshot + ingest, which already exists). The ingest report is the coverage.
- **[learning-theory](kb/notes/learning-theory.md)** -- The "model eats scaffolding" thesis and evaluation infrastructure connect to bitter lesson boundary and oracle hardening, but the source is evidence for those notes rather than a learning-theory contribution itself

## Synthesis Opportunities

1. **"Production-scale convergence on filesystem-first" synthesis.** Three independent sources -- this Fintool report, [Koylanai Personal Brain OS](kb/sources/koylanai-personal-brain-os.ingest.md), and the systems in [related-systems-index](kb/notes/related-systems/related-systems-index.md) -- all converge on filesystem-as-source-of-truth with derived indexes. A synthesis note could argue that this convergence across personal/commercial/research contexts, combined with the failure of database-first approaches at the same tasks, constitutes strong evidence for a durable architectural pattern rather than a phase. Contributing notes: [files-not-database](kb/notes/files-not-database.md), [related-systems-index](kb/notes/related-systems/related-systems-index.md), this source, Koylanai.

2. **"Oracle hardening in practice" synthesis.** Fintool's evaluation infrastructure (adversarial grounding, domain-specific test suites, PR-blocking on regression) is a concrete production implementation of the manufacture/amplify/monitor pipeline from [oracle-strength-spectrum](kb/notes/oracle-strength-spectrum.md). Combined with the Agent Skills evaluation methodology (chain-of-thought scoring, position-bias mitigation), there may be enough practitioner evidence to write a note about how oracle hardening actually works in deployed agent systems versus the theoretical framework.

## Flags

- The ingest report already identified these connections. This connect run confirms and refines them, adding the homoiconicity and context-efficiency connections that the ingest missed, and rejecting several candidates the ingest didn't evaluate.
- The ingest report's recommended next action (write a note about skill shadowing enabling per-user customization) remains unfulfilled and is still a worthwhile note to write.
