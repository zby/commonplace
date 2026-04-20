# Type migration inventory
Generated: 2026-04-20
## Types
| Current type | Files | Target type-spec doc | Schema | Existing support | Migration action |
|---|---:|---|---|---|---|
| `adr` | 19 | `kb/reference/types/adr.md` | `kb/reference/types/adr.schema.yaml` | template, instructions, schema | rewrite frontmatter to `kb/reference/types/adr.md` |
| `agent-memory-system-review` | 98 | `kb/agent-memory-systems/types/agent-memory-system-review.md` | `kb/agent-memory-systems/types/agent-memory-system-review.schema.yaml` | template, instructions, schema | rewrite frontmatter to `kb/agent-memory-systems/types/agent-memory-system-review.md` |
| `connect-report` | 9 | `kb/reports/types/connect-report.md` | `kb/reports/types/connect-report.schema.yaml` | template, instructions, schema | rewrite frontmatter to `kb/reports/types/connect-report.md` |
| `definition` | 7 | `kb/types/definition.md` | `kb/types/definition.schema.yaml` | template, instructions, schema | rewrite frontmatter to `kb/types/definition.md` |
| `index` | 70 | `kb/types/index.md` | `kb/types/index.schema.yaml` | template, instructions, schema | rewrite frontmatter to `kb/types/index.md` |
| `ingest-report` | 81 | `kb/sources/types/ingest-report.md` | `kb/sources/types/ingest-report.schema.yaml` | template, instructions, schema | rewrite frontmatter to `kb/sources/types/ingest-report.md` |
| `instruction` | 64 | `kb/types/instruction.md` | `kb/types/instruction.schema.yaml` | template, instructions, schema | rewrite frontmatter to `kb/types/instruction.md` |
| `note` | 235 | `kb/types/note.md` | `kb/types/note.schema.yaml` | template, schema | rewrite frontmatter to `kb/types/note.md` |
| `snapshot` | 77 | `kb/sources/types/snapshot.md` | `kb/sources/types/snapshot.schema.yaml` | instructions, schema | rewrite frontmatter to `kb/sources/types/snapshot.md` |
| `source-review` | 1 | `kb/sources/types/source-review.md` | `kb/sources/types/source-review.schema.yaml` | template, instructions, schema | rewrite frontmatter to `kb/sources/types/source-review.md` |
| `spec` | 1 | `retired` | `retired` | retired schema-only support | retire; migrate the one artifact to the new type-spec doc model |
| `structured-claim` | 8 | `kb/notes/types/structured-claim.md` | `kb/notes/types/structured-claim.schema.yaml` | template, instructions, schema | rewrite frontmatter to `kb/notes/types/structured-claim.md` |
| `text` | 1 | `kb/sources/types/snapshot.md` | `kb/sources/types/snapshot.schema.yaml` | implicit text; explicit source artifact migrates to snapshot | explicit text is invalid; migrate current metadata-bearing source to snapshot |
| `task-active` | 0 | `kb/tasks/types/task-active.md` | `null` | sidecar-only/new | create type-spec from task sidecars; no current artifacts |
| `task-backlog` | 0 | `kb/tasks/types/task-backlog.md` | `null` | sidecar-only/new | create type-spec from task sidecars; no current artifacts |
| `task-recurring` | 0 | `kb/tasks/types/task-recurring.md` | `null` | sidecar-only/new | create type-spec from task sidecars; no current artifacts |
| `type-spec` | 0 | `kb/types/type-spec.md` | `kb/types/type-spec.schema.yaml` | sidecar-only/new | introduce root type-spec |
| `review` | 0 | `retired` | `retired` | retired schema-only support | delete schema-only retired type |

### Files by current type

#### `adr`
- `kb/reference/adr/002-inline-global-types-in-writing-guide.md`
- `kb/reference/adr/003-connect-skill-discovery-strategy.md`
- `kb/reference/adr/004-replace-areas-with-tags.md`
- `kb/reference/adr/005-quality-check-placement.md`
- `kb/reference/adr/006-two-tree-installation-layout.md`
- `kb/reference/adr/007-reports-directory-for-generated-snapshots.md`
- `kb/reference/adr/008-stdlib-only-core-scripts.md`
- `kb/reference/adr/009-link-relationship-semantics.md`
- `kb/reference/adr/010-review-state-should-move-to-sqlite-once-reviews-leave-git-and-accumulate-operational-metadata.md`
- `kb/reference/adr/011-notes-must-be-accessible-to-external-readers.md`
- `kb/reference/adr/012-types-for-structure-traits-for-review.md`
- `kb/reference/adr/013-skills-first-delivery-with-core-local-type-split.md`
- `kb/reference/adr/014-scripts-as-python-package-one-tree-model.md`
- `kb/reference/adr/015-standardize-authored-type-definitions-on-json-schema.md`
- `kb/reference/adr/016-custom-types-use-template-instruction-pairs.md`
- `kb/reference/adr/017-collection-md-is-the-register-convention-boundary.md`
- `kb/reference/types/adr.template.md`
- `kb/work/link-label-audit/adr-018-draft.md`
- `kb/work/write-type-resolver/adr-018-draft.md`

#### `agent-memory-system-review`
- `kb/agent-memory-systems/reviews/Awesome-Agent-Memory.md`
- `kb/agent-memory-systems/reviews/CORAL.md`
- `kb/agent-memory-systems/reviews/KBLaM.md`
- `kb/agent-memory-systems/reviews/Memori.md`
- `kb/agent-memory-systems/reviews/MiroShark.md`
- `kb/agent-memory-systems/reviews/OpenSage.md`
- `kb/agent-memory-systems/reviews/REM.md`
- `kb/agent-memory-systems/reviews/REM.replaced.2026-04-12.md`
- `kb/agent-memory-systems/reviews/Self-Training-LLM.md`
- `kb/agent-memory-systems/reviews/Zikkaron.md`
- `kb/agent-memory-systems/reviews/ace.md`
- `kb/agent-memory-systems/reviews/ace.replaced.2026-04-12.md`
- `kb/agent-memory-systems/reviews/agent-r.md`
- `kb/agent-memory-systems/reviews/agent-r.replaced.2026-04-12.md`
- `kb/agent-memory-systems/reviews/agent-skills-for-context-engineering.md`
- `kb/agent-memory-systems/reviews/archie.md`
- `kb/agent-memory-systems/reviews/arscontexta.md`
- `kb/agent-memory-systems/reviews/atomic.md`
- `kb/agent-memory-systems/reviews/auto-harness.md`
- `kb/agent-memory-systems/reviews/autocontext.md`
- `kb/agent-memory-systems/reviews/autocontext.replaced.2026-04-12.md`
- `kb/agent-memory-systems/reviews/binder.md`
- `kb/agent-memory-systems/reviews/browzy-ai.md`
- `kb/agent-memory-systems/reviews/browzy-ai.replaced.2026-04-12.md`
- `kb/agent-memory-systems/reviews/byterover-cli.md`
- `kb/agent-memory-systems/reviews/cass_memory_system.md`
- `kb/agent-memory-systems/reviews/cass_memory_system.replaced.2026-04-12.md`
- `kb/agent-memory-systems/reviews/claude-context-guard.md`
- `kb/agent-memory-systems/reviews/clawvault.md`
- `kb/agent-memory-systems/reviews/clawvault.replaced.2026-04-12.md`
- `kb/agent-memory-systems/reviews/cludebot.md`
- `kb/agent-memory-systems/reviews/cludebot.replaced.2026-04-12.md`
- `kb/agent-memory-systems/reviews/cocoindex.md`
- `kb/agent-memory-systems/reviews/cognee.md`
- `kb/agent-memory-systems/reviews/context-constitution.md`
- `kb/agent-memory-systems/reviews/cq.md`
- `kb/agent-memory-systems/reviews/crewai-memory.md`
- `kb/agent-memory-systems/reviews/crewai-memory.replaced.2026-04-13.md`
- `kb/agent-memory-systems/reviews/decapod.md`
- `kb/agent-memory-systems/reviews/docmason.md`
- `kb/agent-memory-systems/reviews/docmason.replaced.2026-04-12.md`
- `kb/agent-memory-systems/reviews/dynamic-cheatsheet.md`
- `kb/agent-memory-systems/reviews/dynamic-cheatsheet.replaced.2026-04-12.md`
- `kb/agent-memory-systems/reviews/engraph.md`
- `kb/agent-memory-systems/reviews/equipa.md`
- `kb/agent-memory-systems/reviews/equipa.replaced.2026-04-12.md`
- `kb/agent-memory-systems/reviews/exocomp.md`
- `kb/agent-memory-systems/reviews/expel.md`
- `kb/agent-memory-systems/reviews/expel.replaced.2026-04-12.md`
- `kb/agent-memory-systems/reviews/g-memory.md`
- `kb/agent-memory-systems/reviews/g-memory.replaced.2026-04-12.md`
- `kb/agent-memory-systems/reviews/gbrain.md`
- `kb/agent-memory-systems/reviews/gbrain.replaced.2026-04-12.md`
- `kb/agent-memory-systems/reviews/getsentry-skills.md`
- `kb/agent-memory-systems/reviews/hindsight.md`
- `kb/agent-memory-systems/reviews/hindsight.replaced.2026-04-12.md`
- `kb/agent-memory-systems/reviews/hyalo.md`
- `kb/agent-memory-systems/reviews/hyperagents.md`
- `kb/agent-memory-systems/reviews/kenhuangus--llm-wiki.md`
- `kb/agent-memory-systems/reviews/lacp.md`
- `kb/agent-memory-systems/reviews/llm-wiki.md`
- `kb/agent-memory-systems/reviews/mempalace.md`
- `kb/agent-memory-systems/reviews/mempalace.replaced.2026-04-12.md`
- `kb/agent-memory-systems/reviews/mentisdb.md`
- `kb/agent-memory-systems/reviews/meta-harness.md`
- `kb/agent-memory-systems/reviews/nao.md`
- `kb/agent-memory-systems/reviews/napkin.md`
- `kb/agent-memory-systems/reviews/napkin.replaced.2026-04-12.md`
- `kb/agent-memory-systems/reviews/nuggets.md`
- `kb/agent-memory-systems/reviews/o-o.md`
- `kb/agent-memory-systems/reviews/openviking.md`
- `kb/agent-memory-systems/reviews/openviking.replaced.2026-04-12.md`
- `kb/agent-memory-systems/reviews/operational-ontology-framework.md`
- `kb/agent-memory-systems/reviews/pal.md`
- `kb/agent-memory-systems/reviews/pi-self-learning.md`
- `kb/agent-memory-systems/reviews/pi-self-learning.replaced.2026-04-12.md`
- `kb/agent-memory-systems/reviews/playground.md`
- `kb/agent-memory-systems/reviews/reasoning-bank.md`
- `kb/agent-memory-systems/reviews/reasoning-bank.replaced.2026-04-12.md`
- `kb/agent-memory-systems/reviews/reflexion.md`
- `kb/agent-memory-systems/reviews/reflexion.replaced.2026-04-12.md`
- `kb/agent-memory-systems/reviews/sage.md`
- `kb/agent-memory-systems/reviews/semiont.md`
- `kb/agent-memory-systems/reviews/sift-kg.md`
- `kb/agent-memory-systems/reviews/siftly.md`
- `kb/agent-memory-systems/reviews/skillnote.md`
- `kb/agent-memory-systems/reviews/spacebot.md`
- `kb/agent-memory-systems/reviews/supermemory.md`
- `kb/agent-memory-systems/reviews/synapptic.md`
- `kb/agent-memory-systems/reviews/synapptic.replaced.2026-04-12.md`
- `kb/agent-memory-systems/reviews/thalo.md`
- `kb/agent-memory-systems/reviews/tracecraft.md`
- `kb/agent-memory-systems/reviews/virtual-context.md`
- `kb/agent-memory-systems/reviews/voyager.md`
- `kb/agent-memory-systems/reviews/voyager.replaced.2026-04-12.md`
- `kb/agent-memory-systems/reviews/xMemory.md`
- `kb/agent-memory-systems/reviews/xMemory.replaced.2026-04-12.md`
- `kb/agent-memory-systems/types/agent-memory-system-review.template.md`

#### `connect-report`
- `kb/reports/connect/notes/a-knowledge-base-holds-theories-descriptions-and-prescriptions-with-asymmetric-linking.connect.md`
- `kb/reports/connect/notes/databricks-memory-scaling-ai-agents.connect.md`
- `kb/reports/connect/notes/scaling-managed-agents-decoupling-brain-from-hands.connect.md`
- `kb/reports/connect/reference/available-types.connect.md`
- `kb/reports/connect/sources/autoreason-self-refinement-that-knows-when-to-stop.connect.md`
- `kb/reports/connect/sources/everything-you-need-to-know-about-llm-memory.connect.md`
- `kb/reports/connect/sources/externalization-in-llm-agents-unified-review.connect.md`
- `kb/reports/connect/sources/into-the-unknown-self-learning-large-language-models.connect.md`
- `kb/reports/types/connect-report.template.md`

#### `definition`
- `kb/notes/definitions/codification.md`
- `kb/notes/definitions/constraining.md`
- `kb/notes/definitions/context-engineering.md`
- `kb/notes/definitions/distillation.md`
- `kb/notes/definitions/register.md`
- `kb/reference/definitions/collection.md`
- `kb/types/definition.template.md`

#### `index`
- `kb/agent-memory-systems/README.md`
- `kb/agent-memory-systems/dir-index.md`
- `kb/agent-memory-systems/reviews/dir-index.md`
- `kb/agent-memory-systems/source-only/dir-index.md`
- `kb/instructions/dir-index.md`
- `kb/notes/architecture-index.md`
- `kb/notes/computational-model-index.md`
- `kb/notes/definitions/dir-index.md`
- `kb/notes/dir-index.md`
- `kb/notes/document-system-index.md`
- `kb/notes/evaluation-index.md`
- `kb/notes/evidence/dir-index.md`
- `kb/notes/foundations-index.md`
- `kb/notes/kb-maintenance-index.md`
- `kb/notes/learning-theory-index.md`
- `kb/notes/links-index.md`
- `kb/notes/llm-interpretation-errors-index.md`
- `kb/notes/observability-index.md`
- `kb/notes/research/dir-index.md`
- `kb/notes/tags-index.md`
- `kb/notes/tool-loop-index.md`
- `kb/notes/type-system-index.md`
- `kb/reference/adr/dir-index.md`
- `kb/reference/definitions/dir-index.md`
- `kb/reference/dir-index.md`
- `kb/sources/dir-index.md`
- `kb/tasks/backlog/dir-index.md`
- `kb/tasks/completed/dir-index.md`
- `kb/tasks/dir-index.md`
- `kb/tasks/recurring/dir-index.md`
- `kb/types/index.template.md`
- `kb/work/agent-complexity-theory/dir-index.md`
- `kb/work/agent-memory-design/dir-index.md`
- `kb/work/curiosity-prompts/dir-index.md`
- `kb/work/dir-index.md`
- `kb/work/gate-refactor/dir-index.md`
- `kb/work/harness-taxonomy-convergence/dir-index.md`
- `kb/work/information-measures/dir-index.md`
- `kb/work/ingestion-and-deep-search/dir-index.md`
- `kb/work/link-label-audit/dir-index.md`
- `kb/work/obsidian-affordances/dir-index.md`
- `kb/work/paper-bounded-context-orchestration/dir-index.md`
- `kb/work/philosophy-borrowing/dir-index.md`
- `kb/work/positioning/dir-index.md`
- `kb/work/prompt-bottleneck/dir-index.md`
- `kb/work/review-revise-gated/dir-index.md`
- `kb/work/review-revise-gated/gates/accessibility/dir-index.md`
- `kb/work/review-revise-gated/gates/complexity/dir-index.md`
- `kb/work/review-revise-gated/gates/dir-index.md`
- `kb/work/review-revise-gated/gates/frontmatter/dir-index.md`
- `kb/work/review-revise-gated/gates/prose/dir-index.md`
- `kb/work/review-revise-gated/gates/semantic/dir-index.md`
- `kb/work/review-revise-gated/gates/sentence/dir-index.md`
- `kb/work/review-revise-gated/gates/structural/dir-index.md`
- `kb/work/review-revise-gated/run-08/dir-index.md`
- `kb/work/review-run-lifecycle/dir-index.md`
- `kb/work/review-system-rewrite/dir-index.md`
- `kb/work/skill-creator-distillation/dir-index.md`
- `kb/work/skill-creator-distillation/sources/claude-code-skill-creator/agents/dir-index.md`
- `kb/work/skill-creator-distillation/sources/claude-code-skill-creator/dir-index.md`
- `kb/work/skill-creator-distillation/sources/claude-code-skill-creator/references/dir-index.md`
- `kb/work/skill-creator-distillation/sources/codex-skill-creator/dir-index.md`
- `kb/work/skill-creator-distillation/sources/codex-skill-creator/references/dir-index.md`
- `kb/work/skill-creator-distillation/sources/dir-index.md`
- `kb/work/skills-vs-instructions/dir-index.md`
- `kb/work/system-documentation/dir-index.md`
- `kb/work/token-wiki-review/dir-index.md`
- `kb/work/tool-loop-control/dir-index.md`
- `kb/work/type-system-rationalization/dir-index.md`
- `kb/work/write-type-resolver/dir-index.md`

#### `ingest-report`
- `kb/sources/a-mem-agentic-memory-for-llm-agents.ingest.md`
- `kb/sources/adam-mastroianni-infinite-midwit.ingest.md`
- `kb/sources/agent-behavioral-contracts-formal-specification-runtime-enforcement.ingest.md`
- `kb/sources/agentic-code-reasoning.ingest.md`
- `kb/sources/agentic-memory-learning-unified-long-term-and-short-term-memory-management.ingest.md`
- `kb/sources/agentic-note-taking-23-notes-without-reasons-2026894188516696435.ingest.md`
- `kb/sources/arrmlet-tracecraft.ingest.md`
- `kb/sources/autoreason-self-refinement-that-knows-when-to-stop.ingest.md`
- `kb/sources/coding-agents-are-effective-long-context-processors.ingest.md`
- `kb/sources/cognee-knowledge-engine.ingest.md`
- `kb/sources/components-of-a-coding-agent-raschka.ingest.md`
- `kb/sources/context-engineering-ai-agents-oss.ingest.md`
- `kb/sources/continual-learning-in-token-space.ingest.md`
- `kb/sources/convexbench-can-llms-recognize-convex-functions.ingest.md`
- `kb/sources/creative-thinking-by-claude-shannon.ingest.md`
- `kb/sources/dario-amodei-we-are-near-the-end-of-the-exponential.ingest.md`
- `kb/sources/databricks-memory-scaling-ai-agents.ingest.md`
- `kb/sources/eric-evans-ai-components-deterministic-system.ingest.md`
- `kb/sources/esolang-bench-evaluating-genuine-reasoning-via-esoteric-programming-languages.ingest.md`
- `kb/sources/even-if-you-set-aside-whether-citations-are-the-right-proxy-for-scient-2035982137539559616.ingest.md`
- `kb/sources/everything-you-need-to-know-about-llm-memory.ingest.md`
- `kb/sources/externalization-in-llm-agents-unified-review.ingest.md`
- `kb/sources/from-entropy-to-epiplexity-rethinking-information-computationally-bounded.ingest.md`
- `kb/sources/graphiti-temporal-knowledge-graph.ingest.md`
- `kb/sources/gsm-dc-llm-reasoning-distracted-irrelevant-context.ingest.md`
- `kb/sources/harness-engineering-is-cybernetics-2030416758138634583.ingest.md`
- `kb/sources/harness-engineering-leveraging-codex-agent-first-world.ingest.md`
- `kb/sources/improving-ai-skills-with-autoresearch-evals-skills-2035257434365976671.ingest.md`
- `kb/sources/induction-bias-sequence-models-ebrahimi-2026.ingest.md`
- `kb/sources/intelligent-ai-delegation-tomasev-franklin-osindero.ingest.md`
- `kb/sources/into-the-unknown-self-learning-large-language-models.ingest.md`
- `kb/sources/karpathy-llm-wiki.ingest.md`
- `kb/sources/koylanai-personal-brain-os.ingest.md`
- `kb/sources/language-models-like-humans-show-content-effects-on-reasoning-tasks.ingest.md`
- `kb/sources/large-language-model-agents-are-not-always-faithful-self-evolvers.ingest.md`
- `kb/sources/lessons-from-building-ai-agents-for-financial-services-2015174818497437834.ingest.md`
- `kb/sources/letta-memgpt-stateful-agents.ingest.md`
- `kb/sources/llm-knowledge-bases-something-i-m-finding-very-useful-recently-using-2039805659525644595.ingest.md`
- `kb/sources/llm-webagents-long-context-reasoning-benchmark.ingest.md`
- `kb/sources/mem0-memory-layer.ingest.md`
- `kb/sources/memory-intelligence-agent.ingest.md`
- `kb/sources/mesa-optimizers-and-language-recursion.ingest.md`
- `kb/sources/meta-harness-end-to-end-optimization-of-model-harnesses.ingest.md`
- `kb/sources/meyerson-maker-million-step-llm-zero-errors.ingest.md`
- `kb/sources/multi-agent-memory-computer-architecture-perspective.ingest.md`
- `kb/sources/natural-language-agent-harnesses.ingest.md`
- `kb/sources/novel-memory-forgetting-techniques-autonomous-ai-agents.ingest.md`
- `kb/sources/openclaw-rl-train-any-agent-simply-by-talking.ingest.md`
- `kb/sources/pathway-beyond-transformers-sudoku-bench.ingest.md`
- `kb/sources/paulsen-maximum-effective-context-window-mecw.ingest.md`
- `kb/sources/professional-software-developers-dont-vibe-they-control.ingest.md`
- `kb/sources/prompt-stability-code-llms-emotion-personality-variations.ingest.md`
- `kb/sources/psychology-solves-ai-memory-identity-construction-2025307030651871631.ingest.md`
- `kb/sources/purdue-owl-toulmin-argument.ingest.md`
- `kb/sources/recursive-language-models-what-finally-gave-me-the-aha-moment-2035040781074145412.ingest.md`
- `kb/sources/scaling-managed-agents-decoupling-brain-from-hands.ingest.md`
- `kb/sources/simon-willison-karpathy-claws.ingest.md`
- `kb/sources/skill-synthesis-materializing-knowledge-as-skills-2032179291031806408.ingest.md`
- `kb/sources/slate-moving-beyond-react-and-rlm.ingest.md`
- `kb/sources/spacedriveapp-spacebot-ai-agent.ingest.md`
- `kb/sources/superarc-ait-benchmark-llm-compression-abstraction.ingest.md`
- `kb/sources/the-anatomy-of-an-agent-harness-2031408954517971368.ingest.md`
- `kb/sources/the-bug-that-shipped-2035319413474206122.ingest.md`
- `kb/sources/the-flawed-ephemeral-software-hypothesis.ingest.md`
- `kb/sources/the-geometry-of-forgetting.ingest.md`
- `kb/sources/the-mismanaged-geniuses-hypothesis-2042588627260018751.ingest.md`
- `kb/sources/the-price-of-meaning-why-every-semantic-memory-system-forgets.ingest.md`
- `kb/sources/the-second-brain-trap-2041486539067154753.ingest.md`
- `kb/sources/the-spec-is-the-new-code-a-guide-to-spec-driven-development-2033303156340240481.ingest.md`
- `kb/sources/the-thing-we-refer-to-as-memory-in-llms-is-just-a-bunch-of-superfici-2036857868914483592.ingest.md`
- `kb/sources/this-tweet-had-me-thinking-what-s-the-minimum-viable-ontology-or-li-2029332670115614799.ingest.md`
- `kb/sources/towards-a-science-of-ai-agent-reliability.ingest.md`
- `kb/sources/towards-a-science-of-scaling-agent-systems.ingest.md`
- `kb/sources/trajectory-informed-memory-generation-self-improving-agents.ingest.md`
- `kb/sources/types/ingest-report.template.md`
- `kb/sources/voooooogel-multi-agent-future.ingest.md`
- `kb/sources/what-spec-driven-development-gets-wrong-2025993446633492725.ingest.md`
- `kb/sources/when-code-is-free-research-is-all-that-matters-2031072399731675269.ingest.md`
- `kb/sources/why-ai-systems-dont-learn-and-what-to-do-about-it.ingest.md`
- `kb/sources/wikipedia-bitter-lesson.ingest.md`
- `kb/sources/xinmingtu-structured-test-time-scaling-hierarchical-mas-theory.ingest.md`

#### `instruction`
- `kb/instructions/complexity-review.md`
- `kb/instructions/cp-skill-compile-collections/SKILL.md`
- `kb/instructions/cp-skill-connect/SKILL.md`
- `kb/instructions/cp-skill-convert/SKILL.md`
- `kb/instructions/cp-skill-ingest/SKILL.md`
- `kb/instructions/cp-skill-revise-autoreason/SKILL.md`
- `kb/instructions/cp-skill-revise-iterative/SKILL.md`
- `kb/instructions/cp-skill-snapshot-web/SKILL.md`
- `kb/instructions/cp-skill-validate/SKILL.md`
- `kb/instructions/cp-skill-write/SKILL.md`
- `kb/instructions/evaluate-log-entry-for-note-creation.md`
- `kb/instructions/evaluate-scenarios/SKILL.md`
- `kb/instructions/example-onboard-second-brain.md`
- `kb/instructions/fix-warnings/fix-descriptions.md`
- `kb/instructions/fix-warnings/fix-review-warnings-sweep.md`
- `kb/instructions/fix-warnings/fix-review-warnings.md`
- `kb/instructions/fix-warnings/fix-strategy-taxonomy.md`
- `kb/instructions/maintain-curated-indexes.md`
- `kb/instructions/migrate-semantics-preserving-gate-changes.md`
- `kb/instructions/prose-review.md`
- `kb/instructions/re-ingest.md`
- `kb/instructions/review-gates/accessibility/jargon-persistence.md`
- `kb/instructions/review-gates/accessibility/notation-opacity.md`
- `kb/instructions/review-gates/accessibility/undefined-terms.md`
- `kb/instructions/review-gates/accessibility/unidentified-references.md`
- `kb/instructions/review-gates/complexity/claim-to-section-ratio.md`
- `kb/instructions/review-gates/complexity/connection-inflation.md`
- `kb/instructions/review-gates/complexity/could-be-a-paragraph.md`
- `kb/instructions/review-gates/complexity/framework-decoration.md`
- `kb/instructions/review-gates/frontmatter/claim-strength.md`
- `kb/instructions/review-gates/frontmatter/description-discrimination.md`
- `kb/instructions/review-gates/frontmatter/title-as-claim.md`
- `kb/instructions/review-gates/frontmatter/title-body-alignment.md`
- `kb/instructions/review-gates/frontmatter/title-composability.md`
- `kb/instructions/review-gates/prose/anthropomorphic-framing.md`
- `kb/instructions/review-gates/prose/bridge-paragraph-duplication.md`
- `kb/instructions/review-gates/prose/confidence-miscalibration.md`
- `kb/instructions/review-gates/prose/orphan-references.md`
- `kb/instructions/review-gates/prose/proportion-mismatch.md`
- `kb/instructions/review-gates/prose/pseudo-formalism.md`
- `kb/instructions/review-gates/prose/redundant-restatement.md`
- `kb/instructions/review-gates/prose/source-residue.md`
- `kb/instructions/review-gates/prose/unbridged-cross-domain.md`
- `kb/instructions/review-gates/semantic/completeness-boundary-cases.md`
- `kb/instructions/review-gates/semantic/explanatory-reach.md`
- `kb/instructions/review-gates/semantic/explication-quality.md`
- `kb/instructions/review-gates/semantic/grounding-alignment.md`
- `kb/instructions/review-gates/semantic/internal-consistency.md`
- `kb/instructions/review-gates/sentence/clause-packing.md`
- `kb/instructions/review-gates/sentence/concept-attribution.md`
- `kb/instructions/review-gates/sentence/framing-mismatch.md`
- `kb/instructions/review-gates/sentence/misleading-link-text.md`
- `kb/instructions/review-gates/sentence/parsing-ambiguity.md`
- `kb/instructions/review-gates/sentence/stock-phrases.md`
- `kb/instructions/review-gates/structural/bullet-capitalization.md`
- `kb/instructions/review-gates/structural/compound-bullet.md`
- `kb/instructions/review-gates/structural/general-before-specific.md`
- `kb/instructions/review-sweep.md`
- `kb/instructions/review-triage.md`
- `kb/instructions/revise-note.md`
- `kb/instructions/run-review-bundle-on-note.md`
- `kb/instructions/write-agent-memory-system-review.md`
- `kb/instructions/write-instruction.md`
- `kb/types/instruction.template.md`

#### `note`
- `kb/agent-memory-systems/agentic-memory-systems-comparative-review.md`
- `kb/agent-memory-systems/source-only/agemem.md`
- `kb/agent-memory-systems/source-only/trajectory-informed-memory-generation.md`
- `kb/agent-memory-systems/thalo-type-comparison.md`
- `kb/agent-memory-systems/trace-derived-learning-techniques-in-related-systems.md`
- `kb/notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md`
- `kb/notes/a-knowledge-base-holds-theories-descriptions-and-prescriptions-with-asymmetric-linking.md`
- `kb/notes/a-knowledge-base-should-support-fluid-resolution-switching.md`
- `kb/notes/access-burden-and-transformation-burden-are-independent-query-dimensions.md`
- `kb/notes/ad-hoc-prompts-extend-the-system-without-schema-changes.md`
- `kb/notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md`
- `kb/notes/agent-is-a-tool-loop.md`
- `kb/notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md`
- `kb/notes/agent-orchestration-needs-coordination-guarantees-not-just-coordination-channels.md`
- `kb/notes/agent-orchestration-occupies-a-multi-dimensional-design-space.md`
- `kb/notes/agent-runtimes-decompose-into-scheduler-context-engine-and-execution-substrate.md`
- `kb/notes/agent-statelessness-makes-routing-architectural-not-learned.md`
- `kb/notes/agentic-systems-interpret-underspecified-instructions.md`
- `kb/notes/agents-md-should-be-organized-as-a-control-plane.md`
- `kb/notes/agents-navigate-by-deciding-what-to-read-next.md`
- `kb/notes/alexander-patterns-and-knowledge-system-design.md`
- `kb/notes/always-loaded-context-mechanisms-in-agent-harnesses.md`
- `kb/notes/an-agentic-kb-maximizes-contextual-competence-through-discoverable-composable-trusted-knowledge.md`
- `kb/notes/any-symbolic-program-with-bounded-calls-is-a-select-call-program.md`
- `kb/notes/apparent-success-is-an-unreliable-health-signal-in-framework-owned-tool-loops.md`
- `kb/notes/areas-exist-because-useful-operations-require-reading-notes-together.md`
- `kb/notes/automated-synthesis-is-missing-good-oracles.md`
- `kb/notes/automated-tests-for-text.md`
- `kb/notes/automating-kb-learning-is-an-open-problem.md`
- `kb/notes/axes-of-substrate-analysis.md`
- `kb/notes/backlinks.md`
- `kb/notes/bounded-context-orchestration-model.md`
- `kb/notes/brainstorming-how-reach-informs-kb-design.md`
- `kb/notes/brainstorming-how-to-enrich-web-search.md`
- `kb/notes/brainstorming-how-to-test-whether-pairwise-comparison-can-harden-soft-oracles.md`
- `kb/notes/capability-placement-should-follow-autonomy-readiness.md`
- `kb/notes/changing-requirements-conflate-genuine-change-with-disambiguation-failure.md`
- `kb/notes/charting-the-knowledge-access-problem-beyond-rag.md`
- `kb/notes/claw-learning-is-broader-than-retrieval.md`
- `kb/notes/claw-learning-loops-must-improve-action-capacity-not-just-retrieval.md`
- `kb/notes/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md`
- `kb/notes/codified-scheduling-patterns-can-turn-tools-into-hidden-schedulers.md`
- `kb/notes/codify-versus-llm-decision-heuristics.md`
- `kb/notes/constraining-and-distillation-both-trade-generality-for-reliability-speed-and-cost.md`
- `kb/notes/constraining-during-deployment-is-continuous-learning.md`
- `kb/notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md`
- `kb/notes/continual-learning-open-problem-is-behaviour-not-knowledge.md`
- `kb/notes/conversation-vs-prompt-refinement-in-agent-to-agent-coordination.md`
- `kb/notes/decomposition-heuristics-for-bounded-context-scheduling.md`
- `kb/notes/deploy-time-learning-is-the-missing-middle.md`
- `kb/notes/deterministic-validation-should-be-a-script.md`
- `kb/notes/directory-scoped-types-are-cheaper-than-global-types.md`
- `kb/notes/discovery-is-seeing-the-particular-as-an-instance-of-the-general.md`
- `kb/notes/distillation-is-transformation-not-selection.md`
- `kb/notes/distillation-status-determines-directory-placement.md`
- `kb/notes/distilled-artifacts-need-source-tracking-at-the-source.md`
- `kb/notes/document-types-should-be-verifiable.md`
- `kb/notes/effective-context-is-task-relative-and-complexity-relative-not-a-fixed-model-constant.md`
- `kb/notes/elicitation-requires-maintained-question-generation-systems.md`
- `kb/notes/enforcement-without-structured-recovery-is-incomplete.md`
- `kb/notes/entropy-management-must-scale-with-generation-throughput.md`
- `kb/notes/ephemeral-computation-prevents-accumulation.md`
- `kb/notes/ephemerality-is-safe-where-embedded-operational-knowledge-has-low-reach.md`
- `kb/notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md`
- `kb/notes/error-messages-that-teach-are-a-constraining-technique.md`
- `kb/notes/evaluation-automation-is-phase-gated-by-comprehension.md`
- `kb/notes/evidence/single-artifact-review-bundles-still-cut-claude-costs-substantially-after-cache-aware-weighting.md`
- `kb/notes/evolving-understanding-needs-re-distillation-not-composition.md`
- `kb/notes/execution-indeterminism-is-a-property-of-the-sampling-process.md`
- `kb/notes/files-not-database.md`
- `kb/notes/first-principles-reasoning-selects-for-explanatory-reach-over-adaptive-fit.md`
- `kb/notes/fixed-artifacts-split-into-exact-specs-and-proxy-theories.md`
- `kb/notes/flat-memory-predicts-specific-cross-contamination-failures-that-are-empirically-testable.md`
- `kb/notes/frontloading-spares-execution-context.md`
- `kb/notes/generate-instructions-at-build-time.md`
- `kb/notes/human-llm-differences-are-load-bearing-for-knowledge-system-design.md`
- `kb/notes/human-writing-structures-transfer-to-llms-because-failure-modes-overlap.md`
- `kb/notes/in-context-learning-presupposes-context-engineering.md`
- `kb/notes/indirection-is-costly-in-llm-instructions.md`
- `kb/notes/information-value-is-observer-relative.md`
- `kb/notes/inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md`
- `kb/notes/instruction-specificity-should-match-loading-frequency.md`
- `kb/notes/instructions-are-typed-callables.md`
- `kb/notes/interpretation-errors-are-failures-of-the-interpreter.md`
- `kb/notes/kb-goals-in-always-loaded-context-guide-inclusion-decisions.md`
- `kb/notes/knowledge-storage-does-not-imply-contextual-activation.md`
- `kb/notes/learning-is-not-only-about-generality.md`
- `kb/notes/legal-drafting-solves-the-same-problem-as-context-engineering.md`
- `kb/notes/link-following-and-search-impose-different-metadata-requirements.md`
- `kb/notes/link-graph-plus-timestamps-enables-make-like-staleness-detection.md`
- `kb/notes/link-strength-is-encoded-in-position-and-prose.md`
- `kb/notes/linking-theory.md`
- `kb/notes/llm-code-boundaries-are-natural-checkpoints.md`
- `kb/notes/llm-context-is-a-homoiconic-medium.md`
- `kb/notes/llm-context-is-composed-without-scoping.md`
- `kb/notes/llm-debugging-starts-with-retry-versus-rewrite-triage.md`
- `kb/notes/llm-learning-phases-fall-between-human-learning-modes.md`
- `kb/notes/llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md`
- `kb/notes/maintenance-operations-catalogue-should-stage-distillation-into-instructions.md`
- `kb/notes/mcp-bundles-stateless-tools-with-stateful-runtime.md`
- `kb/notes/mechanistic-constraints-make-popperian-kb-recommendations-actionable.md`
- `kb/notes/memory-management-policy-is-learnable-but-oracle-dependent.md`
- `kb/notes/methodology-enforcement-is-constraining.md`
- `kb/notes/minimum-viable-vocabulary-is-the-naming-set-that-most-reduces-extraction-cost-for-a-bounded-observer.md`
- `kb/notes/notes-need-quality-scores-to-scale-curation.md`
- `kb/notes/operational-signals-that-a-component-is-a-relaxing-candidate.md`
- `kb/notes/oracle-strength-spectrum.md`
- `kb/notes/periodic-kb-hygiene-should-be-externally-triggered-not-embedded-in-routing.md`
- `kb/notes/pointer-design-tradeoffs-in-progressive-disclosure.md`
- `kb/notes/process-structure-and-output-structure-are-independent-levers.md`
- `kb/notes/programming-patterns-get-a-fast-pass-but-other-borrowed-ideas-must-earn-first-principles-support.md`
- `kb/notes/progressive-constraining-commits-only-after-patterns-stabilize.md`
- `kb/notes/prompt-ablation-converts-human-insight-to-deployable-framing.md`
- `kb/notes/psychology-to-agent-transfer-needs-per-principle-failure-mode-testing.md`
- `kb/notes/quality-signals-for-kb-evaluation.md`
- `kb/notes/readable-substrate-loop-is-the-tractable-unit-for-continual-learning.md`
- `kb/notes/reliability-dimensions-map-to-oracle-hardening-stages.md`
- `kb/notes/research/adaptation-agentic-ai-analysis.md`
- `kb/notes/reverse-compression-is-when-llm-output-expands-without-adding-information.md`
- `kb/notes/rlm-has-the-model-write-ephemeral-orchestrators-over-sub-agents.md`
- `kb/notes/scenario-decomposition-drives-architecture.md`
- `kb/notes/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md`
- `kb/notes/selector-loaded-review-gates-could-let-review-revise-learn-from-accepted-edits.md`
- `kb/notes/semantic-review-catches-content-errors-that-structural-validation-cannot.md`
- `kb/notes/semantic-sub-goals-that-exceed-one-context-window-become-scheduling-problems.md`
- `kb/notes/session-history-should-not-be-the-default-next-context.md`
- `kb/notes/short-composable-notes-maximize-combinatorial-discovery.md`
- `kb/notes/silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md`
- `kb/notes/skills-are-instructions-plus-routing-and-execution-policy.md`
- `kb/notes/soft-bound-traditions-as-sources-for-context-engineering-strategies.md`
- `kb/notes/solve-low-degree-of-freedom-subproblems-first-to-avoid-blocking-better-designs.md`
- `kb/notes/spec-mining-as-codification.md`
- `kb/notes/specification-level-separation-recovers-scoping-before-it-recovers-error-correction.md`
- `kb/notes/specification-strategy-should-follow-where-understanding-lives.md`
- `kb/notes/stale-indexes-are-worse-than-no-indexes.md`
- `kb/notes/stateful-tools-recover-control-by-becoming-hidden-schedulers.md`
- `kb/notes/storing-llm-outputs-is-constraining.md`
- `kb/notes/structure-activates-higher-quality-training-distributions.md`
- `kb/notes/structured-output-is-easier-for-humans-to-review.md`
- `kb/notes/subtasks-that-need-different-tools-force-loop-exposure-in-agent-frameworks.md`
- `kb/notes/synthesis-is-not-error-correction.md`
- `kb/notes/system-definition-artifacts-are-crystallized-reasoning-under-context-scarcity.md`
- `kb/notes/systematic-prompt-variation-serves-verification-and-diagnosis-not-explanatory-reach-testing.md`
- `kb/notes/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md`
- `kb/notes/the-boundary-of-automation-is-the-boundary-of-verification.md`
- `kb/notes/the-chat-history-model-trades-context-efficiency-for-implementation-simplicity.md`
- `kb/notes/three-space-agent-memory-echoes-tulvings-taxonomy-but-the-analogy-may-be-decorative.md`
- `kb/notes/title-as-claim-enables-traversal-as-reasoning.md`
- `kb/notes/title-as-claim-exposes-commitments-enabling-popperian-maintenance.md`
- `kb/notes/title-as-claim-makes-overlap-between-notes-visible.md`
- `kb/notes/topology-isolation-and-verification-form-a-causal-chain-for-reliable-agent-scaling.md`
- `kb/notes/traditional-debugging-intuitions-break-when-tool-loops-can-recover-semantically.md`
- `kb/notes/traversal-improvements-should-be-deferred-via-logging-to-avoid-mid-task-context-switching.md`
- `kb/notes/treat-continual-learning-as-substrate-coevolution.md`
- `kb/notes/two-context-boundaries-govern-collection-operations.md`
- `kb/notes/type-system-enforces-metadata-that-navigation-depends-on.md`
- `kb/notes/types-give-agents-structural-hints-before-opening-documents.md`
- `kb/notes/underspecification-and-indeterminism-complicate-programming-for-prompts-in-distinct-ways.md`
- `kb/notes/unified-calling-conventions-enable-bidirectional-refactoring.md`
- `kb/notes/unit-testing-llm-instructions-requires-mocking-the-tool-boundary.md`
- `kb/notes/verifiability-gradient.md`
- `kb/notes/vibe-noting.md`
- `kb/notes/why-directories-despite-their-costs.md`
- `kb/notes/why-notes-have-types.md`
- `kb/notes/wikiwiki-principle-lowest-friction-capture-then-progressive-refinement.md`
- `kb/notes/writing-styles-are-strategies-for-managing-underspecification.md`
- `kb/reference/architecture.md`
- `kb/reference/available-types.md`
- `kb/reference/collections-and-types.md`
- `kb/reference/commands.md`
- `kb/reference/control-plane-goals.md`
- `kb/reference/instruction-generation.md`
- `kb/reference/lib-modules.md`
- `kb/reference/review-architecture.md`
- `kb/reference/scenario-architecture.md`
- `kb/reference/storage-architecture.md`
- `kb/reference/type-loading.md`
- `kb/reports/collection-topology.md`
- `kb/reports/link-vocabulary.md`
- `kb/reports/revise-autoreason/deploy-time-learning-is-the-missing-middle.md.20260413-195941/current_a.md`
- `kb/reports/revise-autoreason/deploy-time-learning-is-the-missing-middle.md.20260413-195941/original.md`
- `kb/reports/revise-autoreason/deploy-time-learning-is-the-missing-middle.md.20260413-195941/pass_01/author_b/version_b.md`
- `kb/reports/revise-autoreason/deploy-time-learning-is-the-missing-middle.md.20260413-195941/pass_01/candidates/version_a.md`
- `kb/reports/revise-autoreason/deploy-time-learning-is-the-missing-middle.md.20260413-195941/pass_01/judges/judge_1_candidate_1.md`
- `kb/reports/revise-autoreason/deploy-time-learning-is-the-missing-middle.md.20260413-195941/pass_01/judges/judge_1_candidate_2.md`
- `kb/reports/revise-autoreason/deploy-time-learning-is-the-missing-middle.md.20260413-195941/pass_01/judges/judge_1_candidate_3.md`
- `kb/reports/revise-autoreason/deploy-time-learning-is-the-missing-middle.md.20260413-195941/pass_01/judges/judge_2_candidate_1.md`
- `kb/reports/revise-autoreason/deploy-time-learning-is-the-missing-middle.md.20260413-195941/pass_01/judges/judge_2_candidate_2.md`
- `kb/reports/revise-autoreason/deploy-time-learning-is-the-missing-middle.md.20260413-195941/pass_01/judges/judge_2_candidate_3.md`
- `kb/reports/revise-autoreason/deploy-time-learning-is-the-missing-middle.md.20260413-195941/pass_01/judges/judge_3_candidate_1.md`
- `kb/reports/revise-autoreason/deploy-time-learning-is-the-missing-middle.md.20260413-195941/pass_01/judges/judge_3_candidate_2.md`
- `kb/reports/revise-autoreason/deploy-time-learning-is-the-missing-middle.md.20260413-195941/pass_01/judges/judge_3_candidate_3.md`
- `kb/reports/revise-autoreason/deploy-time-learning-is-the-missing-middle.md.20260413-195941/pass_01/synthesizer/version_ab.md`
- `kb/reports/revise-autoreason/distillation-is-transformation-not-selection.md.20260413-224827/current_a.md`
- `kb/reports/revise-autoreason/distillation-is-transformation-not-selection.md.20260413-224827/original.md`
- `kb/reports/revise-autoreason/distillation-is-transformation-not-selection.md.20260413-224827/pass_01/author_b/version_b.md`
- `kb/reports/revise-autoreason/distillation-is-transformation-not-selection.md.20260413-224827/pass_01/candidates/version_a.md`
- `kb/reports/revise-autoreason/distillation-is-transformation-not-selection.md.20260413-224827/pass_01/judges/judge_1_candidate_1.md`
- `kb/reports/revise-autoreason/distillation-is-transformation-not-selection.md.20260413-224827/pass_01/judges/judge_1_candidate_2.md`
- `kb/reports/revise-autoreason/distillation-is-transformation-not-selection.md.20260413-224827/pass_01/judges/judge_1_candidate_3.md`
- `kb/reports/revise-autoreason/distillation-is-transformation-not-selection.md.20260413-224827/pass_01/judges/judge_2_candidate_1.md`
- `kb/reports/revise-autoreason/distillation-is-transformation-not-selection.md.20260413-224827/pass_01/judges/judge_2_candidate_2.md`
- `kb/reports/revise-autoreason/distillation-is-transformation-not-selection.md.20260413-224827/pass_01/judges/judge_2_candidate_3.md`
- `kb/reports/revise-autoreason/distillation-is-transformation-not-selection.md.20260413-224827/pass_01/judges/judge_3_candidate_1.md`
- `kb/reports/revise-autoreason/distillation-is-transformation-not-selection.md.20260413-224827/pass_01/judges/judge_3_candidate_2.md`
- `kb/reports/revise-autoreason/distillation-is-transformation-not-selection.md.20260413-224827/pass_01/judges/judge_3_candidate_3.md`
- `kb/reports/revise-autoreason/distillation-is-transformation-not-selection.md.20260413-224827/pass_01/synthesizer/version_ab.md`
- `kb/reports/revise-autoreason/distillation-is-transformation-not-selection.md.20260413-224827/pass_02/author_b/version_b.md`
- `kb/reports/revise-autoreason/distillation-is-transformation-not-selection.md.20260413-224827/pass_02/candidates/version_a.md`
- `kb/reports/revise-autoreason/distillation-is-transformation-not-selection.md.20260413-224827/pass_02/judges/judge_1_candidate_1.md`
- `kb/reports/revise-autoreason/distillation-is-transformation-not-selection.md.20260413-224827/pass_02/judges/judge_1_candidate_2.md`
- `kb/reports/revise-autoreason/distillation-is-transformation-not-selection.md.20260413-224827/pass_02/judges/judge_1_candidate_3.md`
- `kb/reports/revise-autoreason/distillation-is-transformation-not-selection.md.20260413-224827/pass_02/judges/judge_2_candidate_1.md`
- `kb/reports/revise-autoreason/distillation-is-transformation-not-selection.md.20260413-224827/pass_02/judges/judge_2_candidate_2.md`
- `kb/reports/revise-autoreason/distillation-is-transformation-not-selection.md.20260413-224827/pass_02/judges/judge_2_candidate_3.md`
- `kb/reports/revise-autoreason/distillation-is-transformation-not-selection.md.20260413-224827/pass_02/judges/judge_3_candidate_1.md`
- `kb/reports/revise-autoreason/distillation-is-transformation-not-selection.md.20260413-224827/pass_02/judges/judge_3_candidate_2.md`
- `kb/reports/revise-autoreason/distillation-is-transformation-not-selection.md.20260413-224827/pass_02/judges/judge_3_candidate_3.md`
- `kb/reports/revise-autoreason/distillation-is-transformation-not-selection.md.20260413-224827/pass_02/synthesizer/version_ab.md`
- `kb/sources/a-mem-agentic-memory-for-llm-agents.ingest.report-automation-quality.md`
- `kb/sources/a-mem-agentic-memory-for-llm-agents.ingest.report-learning-operations.md`
- `kb/types/note.template.md`
- `kb/work/curiosity-prompts/decapod-claims-audit.md`
- `kb/work/curiosity-prompts/decapod-original.md`
- `kb/work/harness-taxonomy-convergence/runtime-structure-determines-the-control-surfaces-available-to-governance.md`
- `kb/work/information-measures/epiplexity-eli5.md`
- `kb/work/positioning/related-systems-as-showcase.md`
- `kb/work/review-revise-gated/baseline.md`
- `kb/work/review-revise-gated/run-08/revised-1.md`
- `kb/work/review-revise-gated/run-08/revised-2.md`
- `kb/work/review-revise-gated/run-08/revised.md`
- `kb/work/review-revise-gated/target.md`
- `kb/work/tool-loop-control/a-framework-owned-tool-loop-can-simulate-explicit-orchestration-by-externalizing-control-state.md`
- `kb/work/tool-loop-control/anatomy-of-an-llm-application.md`
- `kb/work/tool-loop-control/llm-frameworks-should-keep-the-tool-loop-optional.md`

#### `snapshot`
- `kb/sources/a-mem-agentic-memory-for-llm-agents.md`
- `kb/sources/adam-mastroianni-infinite-midwit.md`
- `kb/sources/agent-behavioral-contracts-formal-specification-runtime-enforcement.md`
- `kb/sources/agentic-code-reasoning.md`
- `kb/sources/agentic-memory-learning-unified-long-term-and-short-term-memory-management.md`
- `kb/sources/agentic-note-taking-23-notes-without-reasons-2026894188516696435.md`
- `kb/sources/arrmlet-tracecraft.md`
- `kb/sources/autoreason-self-refinement-that-knows-when-to-stop.md`
- `kb/sources/coding-agents-are-effective-long-context-processors.md`
- `kb/sources/cognee-knowledge-engine.md`
- `kb/sources/components-of-a-coding-agent-raschka.md`
- `kb/sources/context-engineering-ai-agents-oss.md`
- `kb/sources/continual-learning-in-token-space.md`
- `kb/sources/convexbench-can-llms-recognize-convex-functions.md`
- `kb/sources/creative-thinking-by-claude-shannon.md`
- `kb/sources/dario-amodei-we-are-near-the-end-of-the-exponential.md`
- `kb/sources/databricks-memory-scaling-ai-agents.md`
- `kb/sources/eric-evans-ai-components-deterministic-system.md`
- `kb/sources/esolang-bench-evaluating-genuine-reasoning-via-esoteric-programming-languages.md`
- `kb/sources/even-if-you-set-aside-whether-citations-are-the-right-proxy-for-scient-2035982137539559616.md`
- `kb/sources/everything-you-need-to-know-about-llm-memory.md`
- `kb/sources/externalization-in-llm-agents-unified-review.md`
- `kb/sources/from-entropy-to-epiplexity-rethinking-information-computationally-bounded.md`
- `kb/sources/graphiti-temporal-knowledge-graph.md`
- `kb/sources/gsm-dc-llm-reasoning-distracted-irrelevant-context.md`
- `kb/sources/harness-engineering-is-cybernetics-2030416758138634583.md`
- `kb/sources/harness-engineering-leveraging-codex-agent-first-world.md`
- `kb/sources/improving-ai-skills-with-autoresearch-evals-skills-2035257434365976671.md`
- `kb/sources/induction-bias-sequence-models-ebrahimi-2026.md`
- `kb/sources/intelligent-ai-delegation-tomasev-franklin-osindero.md`
- `kb/sources/into-the-unknown-self-learning-large-language-models.md`
- `kb/sources/karpathy-llm-wiki.md`
- `kb/sources/koylanai-personal-brain-os.md`
- `kb/sources/language-models-like-humans-show-content-effects-on-reasoning-tasks.md`
- `kb/sources/large-language-model-agents-are-not-always-faithful-self-evolvers.md`
- `kb/sources/lessons-from-building-ai-agents-for-financial-services-2015174818497437834.md`
- `kb/sources/llm-knowledge-bases-something-i-m-finding-very-useful-recently-using-2039805659525644595.md`
- `kb/sources/llm-webagents-long-context-reasoning-benchmark.md`
- `kb/sources/mem0-memory-layer.md`
- `kb/sources/memory-intelligence-agent.md`
- `kb/sources/mesa-optimizers-and-language-recursion.md`
- `kb/sources/meta-harness-end-to-end-optimization-of-model-harnesses.md`
- `kb/sources/meyerson-maker-million-step-llm-zero-errors.md`
- `kb/sources/multi-agent-memory-computer-architecture-perspective.md`
- `kb/sources/natural-language-agent-harnesses.md`
- `kb/sources/novel-memory-forgetting-techniques-autonomous-ai-agents.md`
- `kb/sources/openclaw-rl-train-any-agent-simply-by-talking.md`
- `kb/sources/pathway-beyond-transformers-sudoku-bench.md`
- `kb/sources/paulsen-maximum-effective-context-window-mecw.md`
- `kb/sources/professional-software-developers-dont-vibe-they-control.md`
- `kb/sources/prompt-stability-code-llms-emotion-personality-variations.md`
- `kb/sources/purdue-owl-toulmin-argument.md`
- `kb/sources/recursive-language-models-what-finally-gave-me-the-aha-moment-2035040781074145412.md`
- `kb/sources/scaling-managed-agents-decoupling-brain-from-hands.md`
- `kb/sources/simon-willison-karpathy-claws.md`
- `kb/sources/skill-synthesis-materializing-knowledge-as-skills-2032179291031806408.md`
- `kb/sources/slate-moving-beyond-react-and-rlm.md`
- `kb/sources/spacedriveapp-spacebot-ai-agent.md`
- `kb/sources/superarc-ait-benchmark-llm-compression-abstraction.md`
- `kb/sources/the-anatomy-of-an-agent-harness-2031408954517971368.md`
- `kb/sources/the-bug-that-shipped-2035319413474206122.md`
- `kb/sources/the-flawed-ephemeral-software-hypothesis.md`
- `kb/sources/the-geometry-of-forgetting.md`
- `kb/sources/the-mismanaged-geniuses-hypothesis-2042588627260018751.md`
- `kb/sources/the-price-of-meaning-why-every-semantic-memory-system-forgets.md`
- `kb/sources/the-second-brain-trap-2041486539067154753.md`
- `kb/sources/the-spec-is-the-new-code-a-guide-to-spec-driven-development-2033303156340240481.md`
- `kb/sources/the-thing-we-refer-to-as-memory-in-llms-is-just-a-bunch-of-superfici-2036857868914483592.md`
- `kb/sources/this-tweet-had-me-thinking-what-s-the-minimum-viable-ontology-or-li-2029332670115614799.md`
- `kb/sources/towards-a-science-of-ai-agent-reliability.md`
- `kb/sources/towards-a-science-of-scaling-agent-systems.md`
- `kb/sources/trajectory-informed-memory-generation-self-improving-agents.md`
- `kb/sources/what-spec-driven-development-gets-wrong-2025993446633492725.md`
- `kb/sources/when-code-is-free-research-is-all-that-matters-2031072399731675269.md`
- `kb/sources/why-ai-systems-dont-learn-and-what-to-do-about-it.md`
- `kb/sources/wikipedia-bitter-lesson.md`
- `kb/sources/xinmingtu-structured-test-time-scaling-hierarchical-mas-theory.md`

#### `source-review`
- `kb/sources/types/source-review.template.md`

#### `spec`
- `kb/types/note.md`

#### `structured-claim`
- `kb/notes/agent-statelessness-means-the-context-engine-should-inject-context-automatically.md`
- `kb/notes/claim-notes-should-use-toulmin-derived-sections-for-structured-argument.md`
- `kb/notes/index-curation-adds-orientation-that-generation-cannot-produce.md`
- `kb/notes/skills-derive-from-methodology-through-distillation.md`
- `kb/notes/types/structured-claim.template.md`
- `kb/work/agent-complexity-theory/adaptive-dependencies-force-width-reopening-or-sequential-rounds.md`
- `kb/work/agent-complexity-theory/exact-retrieval-over-semantically-opaque-items-requires-linear-inspection.md`
- `kb/work/agent-complexity-theory/no-universal-distillation-preserves-all-task-relevant-structure.md`

#### `text`
- `kb/sources/psychology-solves-ai-memory-identity-construction-2025307030651871631.md`

### Type sidecars
- `kb/agent-memory-systems/types/agent-memory-system-review.instructions.md`
- `kb/agent-memory-systems/types/agent-memory-system-review.schema.yaml`
- `kb/agent-memory-systems/types/agent-memory-system-review.template.md`
- `kb/notes/types/review.schema.yaml`
- `kb/notes/types/spec.schema.yaml`
- `kb/notes/types/structured-claim.instructions.md`
- `kb/notes/types/structured-claim.schema.yaml`
- `kb/notes/types/structured-claim.template.md`
- `kb/reference/types/adr.instructions.md`
- `kb/reference/types/adr.schema.yaml`
- `kb/reference/types/adr.template.md`
- `kb/reports/types/connect-report.instructions.md`
- `kb/reports/types/connect-report.schema.yaml`
- `kb/reports/types/connect-report.template.md`
- `kb/sources/types/ingest-report.instructions.md`
- `kb/sources/types/ingest-report.schema.yaml`
- `kb/sources/types/ingest-report.template.md`
- `kb/sources/types/snapshot.instructions.md`
- `kb/sources/types/snapshot.schema.yaml`
- `kb/sources/types/source-review.instructions.md`
- `kb/sources/types/source-review.schema.yaml`
- `kb/sources/types/source-review.template.md`
- `kb/tasks/types/task-active.instructions.md`
- `kb/tasks/types/task-active.template.md`
- `kb/tasks/types/task-backlog.instructions.md`
- `kb/tasks/types/task-backlog.template.md`
- `kb/tasks/types/task-recurring.instructions.md`
- `kb/tasks/types/task-recurring.template.md`
- `kb/types/definition.instructions.md`
- `kb/types/definition.schema.yaml`
- `kb/types/definition.template.md`
- `kb/types/index.instructions.md`
- `kb/types/index.schema.yaml`
- `kb/types/index.template.md`
- `kb/types/instruction.instructions.md`
- `kb/types/instruction.schema.yaml`
- `kb/types/instruction.template.md`
- `kb/types/note-base.schema.yaml`
- `kb/types/note.schema.yaml`
- `kb/types/note.template.md`

## Consumers
Pre-migration search command:

```bash
rg -n "\.template\.md|\.instructions\.md|type: (note|index|definition|instruction|adr|structured-claim|agent-memory-system-review|connect-report|snapshot|ingest-report|source-review|spec|review|text)\b|requires-type: (note|index|definition|instruction|adr|structured-claim|agent-memory-system-review|connect-report|snapshot|ingest-report|source-review|spec|review|text)\b|get\(\"type\"\).*==|get\(\"type\"\).*!=|note_type|resolved_type|definition_path|check_type_uniqueness|discover_all_types" src test kb scripts AGENTS.md README.md
```

Pre-migration matches (operational and historical; workshop code out of scope per plan):

```text
README.md:73:- Agent-memory-system reviews are handled by writing with the `agent-memory-system-review` type — workflow in `kb/agent-memory-systems/types/agent-memory-system-review.instructions.md`
AGENTS.md:82:rg "^type: structured-claim" kb/notes/ kb/reference/ kb/instructions/ --glob "*.md"
src/commonplace/cli/github_snapshot.py:144:        f"type: snapshot\n"
scripts/session-tools.py:44:                if obj.get("type") == "queue-operation" and obj.get("operation") == "enqueue":
scripts/session-tools.py:73:                    if not isinstance(block, dict) or block.get("type") != "tool_use":
test/connect/fixtures/constraining-stripped.md:3:type: note
kb/reference/type-loading.md:3:type: note
kb/reference/type-loading.md:14:Commonplace stores a type's structural contract as files on disk — typically a `{type}.template.md`, a `{type}.instructions.md`, and a `{type}.schema.yaml` — rather than compiling the contract into code. Loading a type means finding and reading those files. Nothing else knows what an `adr` or a `source-review` is.
kb/reference/type-loading.md:30:The consequence is that bare type names are scoped by where the note lives: `type: adr` under `kb/reference/` resolves to `kb/reference/types/adr.*`, and the same name under another collection would resolve to that collection's definition. Adding a new type is an authoring step — drop the template, instructions, and schema into the owning collection's `types/` — with no code change. Per [ADR-012](./adr/012-types-for-structure-traits-for-review.md), the validator reads these schemas rather than carrying a hard-coded type-profile map.
kb/reference/type-loading.md:38:Other shipped specialised types stay in either global `kb/types/` or their owning collection's `types/` directory and load only when an agent is explicitly writing one. A skill or routing table line points at the specific template file (e.g., `kb/types/instruction.template.md` or `kb/reference/types/adr.template.md`) rather than relying on the agent to remember every type definition.
kb/reference/type-loading.md:56:- Does the `type:` frontmatter field stay useful as a search filter once directory scoping becomes load-bearing? `rg '^type: note'` still works today, but adding more directory-local type names in consuming projects could fragment the filter.
kb/notes/evolving-understanding-needs-re-distillation-not-composition.md:3:type: note
kb/reference/instruction-generation.md:3:type: note
kb/notes/kb-goals-in-always-loaded-context-guide-inclusion-decisions.md:3:type: note
kb/notes/llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md:3:type: note
kb/reference/architecture.md:3:type: note
kb/notes/storing-llm-outputs-is-constraining.md:3:type: note
kb/notes/reliability-dimensions-map-to-oracle-hardening-stages.md:3:type: note
kb/notes/codified-scheduling-patterns-can-turn-tools-into-hidden-schedulers.md:3:type: note
test/connect/fixtures/codification-intact.md:3:type: note
kb/reference/review-architecture.md:3:type: note
kb/notes/agent-orchestration-needs-coordination-guarantees-not-just-coordination-channels.md:3:type: note
kb/notes/areas-exist-because-useful-operations-require-reading-notes-together.md:3:type: note
kb/reference/available-types.md:3:type: note
kb/reference/available-types.md:21:| `note` | `note.md`, `note.template.md`, `note.schema.yaml`, `note-base.schema.yaml` | Base structured type. Requires a non-empty `description`; carries shared `status`, `traits`, `tags`. Every specialised type inherits its frontmatter shape from here. |
kb/reference/available-types.md:22:| `instruction` | `instruction.template.md`, `instruction.instructions.md`, `instruction.schema.yaml` | Prescriptive procedure, promoted skill body, or review gate. Requires `description`; review gates additionally require gate metadata plus `Failure mode` and `Test` sections. |
kb/reference/available-types.md:23:| `definition` | `definition.template.md`, `definition.instructions.md`, `definition.schema.yaml` | Vocabulary note with `Scope`, `Exclusions`, and `Misuse Cases` sections. |
kb/reference/available-types.md:24:| `index` | `index.template.md`, `index.instructions.md`, `index.schema.yaml` | Navigation hub: directory listings or curated tag indexes with generated tails. |
kb/notes/first-principles-reasoning-selects-for-explanatory-reach-over-adaptive-fit.md:3:type: note
kb/reference/collections-and-types.md:3:type: note
kb/notes/scenario-decomposition-drives-architecture.md:3:type: note
test/connect/fixtures/frontloading-stripped.md:3:type: note
kb/notes/frontloading-spares-execution-context.md:3:type: note
kb/notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md:3:type: note
kb/work/philosophy-borrowing/dir-index.md:3:type: index
kb/notes/maintenance-operations-catalogue-should-stage-distillation-into-instructions.md:3:type: note
kb/notes/ad-hoc-prompts-extend-the-system-without-schema-changes.md:3:type: note
kb/reference/commands.md:3:type: note
src/commonplace/cli/validate_notes.py:16:from commonplace.lib.type_resolver import check_type_uniqueness
src/commonplace/cli/validate_notes.py:99:    lines = [f"=== VALIDATION: {path.name} ===", "", f"Type: {results.note_type}", ""]
src/commonplace/cli/validate_notes.py:159:        if results.note_type == "text":
src/commonplace/cli/validate_notes.py:161:        if scope is not None and path in inbound and not inbound[path] and results.note_type != "text":
src/commonplace/cli/validate_notes.py:173:        type_warnings = check_type_uniqueness(repo_root)
kb/notes/definitions/register.md:3:type: definition
kb/notes/definitions/distillation.md:3:type: definition
kb/notes/definitions/context-engineering.md:3:type: definition
kb/notes/definitions/constraining.md:3:type: definition
kb/notes/definitions/dir-index.md:3:type: index
kb/reference/lib-modules.md:3:type: note
kb/reference/lib-modules.md:155:- `resolved_type: str` — type name
kb/reference/lib-modules.md:156:- `definition_path: Path | None` — path to the `.schema.yaml` file (or `None` for `"text"`)
kb/reference/lib-modules.md:181:**`ParsedNote`** — dataclass bundling a note's `path`, `content`, `note_type`, `profile` (`TypeProfile`), and `document` (`ParsedDocument`).
kb/notes/definitions/codification.md:3:type: definition
kb/notes/system-definition-artifacts-are-crystallized-reasoning-under-context-scarcity.md:3:type: note
kb/notes/tags-index.md:3:type: index
kb/notes/programming-patterns-get-a-fast-pass-but-other-borrowed-ideas-must-earn-first-principles-support.md:3:type: note
kb/reference/dir-index.md:3:type: index
kb/notes/human-llm-differences-are-load-bearing-for-knowledge-system-design.md:3:type: note
kb/notes/instructions-are-typed-callables.md:3:type: note
kb/reference/storage-architecture.md:3:type: note
kb/notes/spec-mining-as-codification.md:3:type: note
kb/notes/prompt-ablation-converts-human-insight-to-deployable-framing.md:3:type: note
kb/notes/prompt-ablation-converts-human-insight-to-deployable-framing.md:49:- The [Curiosity Pass](./types/related-system.template.md) in the related-system template — a systematic per-claim review step combining broad curiosity, cost/benefit, and the oracle-strength question
kb/notes/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md:3:type: note
kb/notes/systematic-prompt-variation-serves-verification-and-diagnosis-not-explanatory-reach-testing.md:3:type: note
kb/notes/document-system-index.md:3:type: index
kb/notes/access-burden-and-transformation-burden-are-independent-query-dimensions.md:3:type: note
test/commonplace/cli/test_init_project.py:50:    assert (tmp_path / "kb" / "reference" / "types" / "adr.template.md").is_file()
test/commonplace/cli/test_init_project.py:51:    assert (tmp_path / "kb" / "reference" / "types" / "adr.instructions.md").is_file()
test/commonplace/cli/test_init_project.py:54:    assert (tmp_path / "kb" / "types" / "instruction.template.md").is_file()
test/commonplace/cli/test_init_project.py:55:    assert (tmp_path / "kb" / "types" / "instruction.instructions.md").is_file()
test/commonplace/cli/test_init_project.py:58:    assert (tmp_path / "kb" / "reports" / "types" / "connect-report.template.md").is_file()
test/commonplace/cli/test_init_project.py:59:    assert (tmp_path / "kb" / "reports" / "types" / "connect-report.instructions.md").is_file()
test/commonplace/cli/test_init_project.py:61:    assert (tmp_path / "kb" / "sources" / "types" / "ingest-report.template.md").is_file()
test/commonplace/cli/test_init_project.py:62:    assert (tmp_path / "kb" / "sources" / "types" / "ingest-report.instructions.md").is_file()
test/commonplace/cli/test_init_project.py:64:    assert (tmp_path / "kb" / "sources" / "types" / "snapshot.instructions.md").is_file()
test/commonplace/cli/test_init_project.py:66:    assert not (tmp_path / "kb" / "sources" / "types" / "snapshot.template.md").exists()
kb/notes/unified-calling-conventions-enable-bidirectional-refactoring.md:3:type: note
test/commonplace/cli/test_promotion_candidates.py:40:type: note
kb/reference/adr/013-skills-first-delivery-with-core-local-type-split.md:3:type: adr
kb/notes/types/structured-claim.template.md:3:type: structured-claim
kb/reference/adr/007-reports-directory-for-generated-snapshots.md:3:type: adr
test/commonplace/cli/test_sync_generated_index.py:26:type: index
test/commonplace/cli/test_sync_generated_index.py:43:type: note
test/commonplace/cli/test_sync_generated_index.py:73:type: index
test/commonplace/cli/test_sync_generated_index.py:84:type: index
test/commonplace/cli/test_sync_generated_index.py:98:type: index
test/commonplace/cli/test_sync_generated_index.py:108:        notes_root / "types" / "index.template.md",
test/commonplace/cli/test_sync_generated_index.py:111:type: index
test/commonplace/cli/test_sync_generated_index.py:134:type: index
test/commonplace/cli/test_sync_generated_index.py:150:type: index
test/commonplace/cli/test_sync_generated_index.py:162:type: index
kb/notes/interpretation-errors-are-failures-of-the-interpreter.md:3:type: note
src/commonplace/cli/x_snapshot.py:128:        if ref.get("type") == "replied_to" and ref.get("id"):
src/commonplace/cli/x_snapshot.py:248:        "type: snapshot",
kb/work/skill-creator-distillation/sources/claude-code-skill-creator/references/dir-index.md:3:type: index
kb/notes/architecture-index.md:3:type: index
kb/reference/adr/008-stdlib-only-core-scripts.md:3:type: adr
kb/notes/title-as-claim-enables-traversal-as-reasoning.md:3:type: note
kb/notes/title-as-claim-enables-traversal-as-reasoning.md:61:This maps onto the existing type system: notes with claim titles may be promoted to `type: structured-claim` when the argument matures; `spec`, `index`, and other structural types carry topical titles. The title convention (claim vs topical) is independent of the type — any `note` can use a claim title.
kb/notes/title-as-claim-enables-traversal-as-reasoning.md:65:Not every idea decomposes into a single declarative sentence — some are relational, procedural, emergent, or compositional. When reformulation feels forced, the question is whether the insight isn't ready or the format can't accommodate it. The type system makes this explicit: if you can't write a claim title, the note stays `type: note` with a topical title, and that's fine.
kb/notes/types-give-agents-structural-hints-before-opening-documents.md:3:type: note
kb/notes/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md:3:type: note
kb/notes/llm-context-is-composed-without-scoping.md:3:type: note
kb/reference/adr/005-quality-check-placement.md:3:type: adr
kb/notes/structure-activates-higher-quality-training-distributions.md:3:type: note
kb/notes/an-agentic-kb-maximizes-contextual-competence-through-discoverable-composable-trusted-knowledge.md:3:type: note
kb/notes/wikiwiki-principle-lowest-friction-capture-then-progressive-refinement.md:3:type: note
kb/notes/evaluation-index.md:3:type: index
kb/notes/claw-learning-loops-must-improve-action-capacity-not-just-retrieval.md:3:type: note
kb/work/skill-creator-distillation/sources/claude-code-skill-creator/agents/dir-index.md:3:type: index
kb/notes/learning-is-not-only-about-generality.md:3:type: note
kb/reference/adr/016-custom-types-use-template-instruction-pairs.md:3:type: adr
kb/reference/adr/016-custom-types-use-template-instruction-pairs.md:40:- `{type}.template.md` defines the literal draft scaffold the agent should follow.
kb/reference/adr/016-custom-types-use-template-instruction-pairs.md:41:- `{type}.instructions.md` explains how to fill that scaffold in well.
kb/reference/adr/016-custom-types-use-template-instruction-pairs.md:50:- if the target is a specialized or practitioner-defined type, load `{type}.template.md`
kb/reference/adr/016-custom-types-use-template-instruction-pairs.md:51:- if present, also load `{type}.instructions.md`
kb/reference/adr/016-custom-types-use-template-instruction-pairs.md:66:- Existing references, tests, and workflows had to migrate from `{type}.md` to `{type}.template.md` plus `{type}.instructions.md`.
kb/notes/learning-theory-index.md:3:type: index
kb/notes/apparent-success-is-an-unreliable-health-signal-in-framework-owned-tool-loops.md:3:type: note
kb/notes/synthesis-is-not-error-correction.md:3:type: note
kb/reports/reviews/kb__notes__directory-scoped-types-are-cheaper-than-global-types/semantic__grounding-alignment.claude-opus-4-6.md:25:**document-classification.md** — The note says "The document classification spec defines seven global base types: text, note, structured-claim, spec, review, index, adr." The source lists exactly these 7 in its base types table and has `type: spec`. Accurate attribution. However, the source's current framing is softer than "seven global base types" — it says "The `type` field is a free-form string. The table below lists the common values." The note reads this as a more rigid taxonomy than the source currently presents.
kb/notes/selector-loaded-review-gates-could-let-review-revise-learn-from-accepted-edits.md:3:type: note
kb/reference/adr/002-inline-global-types-in-writing-guide.md:3:type: adr
kb/reference/adr/002-inline-global-types-in-writing-guide.md:17:- Type templates in `kb/types/note.template.md` and `kb/notes/types/structured-claim.template.md`
kb/notes/link-strength-is-encoded-in-position-and-prose.md:3:type: note
kb/notes/stateful-tools-recover-control-by-becoming-hidden-schedulers.md:3:type: note
kb/notes/constraining-during-deployment-is-continuous-learning.md:3:type: note
kb/notes/deterministic-validation-should-be-a-script.md:3:type: note
kb/notes/mcp-bundles-stateless-tools-with-stateful-runtime.md:3:type: note
kb/reference/adr/014-scripts-as-python-package-one-tree-model.md:3:type: adr
kb/notes/alexander-patterns-and-knowledge-system-design.md:3:type: note
kb/notes/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md:3:type: note
kb/reference/adr/006-two-tree-installation-layout.md:3:type: adr
kb/notes/dir-index.md:3:type: index
kb/notes/continual-learning-open-problem-is-behaviour-not-knowledge.md:3:type: note
kb/notes/evaluation-automation-is-phase-gated-by-comprehension.md:3:type: note
kb/notes/entropy-management-must-scale-with-generation-throughput.md:3:type: note
kb/reference/adr/012-types-for-structure-traits-for-review.md:3:type: adr
kb/reference/adr/012-types-for-structure-traits-for-review.md:15:The type system had accumulated inconsistencies: `related-system` template said `type: note` despite being a distinct artifact kind, the validator hard-coded type profiles while docs said "add a template, get a type," and there was no principled boundary between what should be a type vs a trait vs a directory convention. Semantic checks (description quality, title composability) lived in `/validate` alongside structural checks, blurring the validation/review boundary.
kb/reference/adr/012-types-for-structure-traits-for-review.md:35:**Type definitions are two files.** Each type has `{type}.template.md` (prose template for agents) plus `{type}.instructions.md` (how to fill it in), and a machine-readable schema in its `types/` directory. ADR-015 later standardized that schema as JSON Schema in YAML syntax. The schema replaces the validator's hard-coded `TYPE_HEADINGS` map.
kb/notes/skills-derive-from-methodology-through-distillation.md:3:type: structured-claim
kb/notes/two-context-boundaries-govern-collection-operations.md:3:type: note
kb/notes/bounded-context-orchestration-model.md:3:type: note
kb/notes/link-following-and-search-impose-different-metadata-requirements.md:3:type: note
kb/reference/adr/003-connect-skill-discovery-strategy.md:3:type: adr
kb/notes/indirection-is-costly-in-llm-instructions.md:3:type: note
kb/notes/skills-are-instructions-plus-routing-and-execution-policy.md:3:type: note
kb/work/skill-creator-distillation/sources/claude-code-skill-creator/dir-index.md:3:type: index
kb/reference/adr/011-notes-must-be-accessible-to-external-readers.md:3:type: adr
kb/notes/information-value-is-observer-relative.md:3:type: note
kb/notes/elicitation-requires-maintained-question-generation-systems.md:3:type: note
kb/notes/charting-the-knowledge-access-problem-beyond-rag.md:3:type: note
kb/reference/adr/dir-index.md:3:type: index
kb/notes/topology-isolation-and-verification-form-a-causal-chain-for-reliable-agent-scaling.md:3:type: note
kb/notes/kb-maintenance-index.md:3:type: index
kb/notes/agent-is-a-tool-loop.md:3:type: note
kb/notes/session-history-should-not-be-the-default-next-context.md:3:type: note
kb/reference/adr/009-link-relationship-semantics.md:3:type: adr
kb/notes/linking-theory.md:3:type: note
kb/notes/knowledge-storage-does-not-imply-contextual-activation.md:3:type: note
kb/notes/deploy-time-learning-is-the-missing-middle.md:3:type: note
kb/notes/subtasks-that-need-different-tools-force-loop-exposure-in-agent-frameworks.md:3:type: note
kb/notes/instruction-specificity-should-match-loading-frequency.md:3:type: note
kb/notes/claw-learning-is-broader-than-retrieval.md:3:type: note
kb/reference/adr/017-collection-md-is-the-register-convention-boundary.md:3:type: adr
kb/reference/adr/017-collection-md-is-the-register-convention-boundary.md:57:- The same structural type can be reused across registers. `type: note` means "uses the note contract," not "is theoretical."
kb/notes/three-space-agent-memory-echoes-tulvings-taxonomy-but-the-analogy-may-be-decorative.md:3:type: note
kb/notes/specification-strategy-should-follow-where-understanding-lives.md:3:type: note
kb/notes/ephemerality-is-safe-where-embedded-operational-knowledge-has-low-reach.md:3:type: note
src/commonplace/docs/mkdocs_hooks.py:46:        fm.get("type") == "index"
src/commonplace/docs/mkdocs_hooks.py:80:    note_type = meta.get("type")
src/commonplace/docs/mkdocs_hooks.py:82:    if not status and not note_type and not tags:
src/commonplace/docs/mkdocs_hooks.py:86:    if note_type:
src/commonplace/docs/mkdocs_hooks.py:87:        parts.append(f"**Type:** {note_type}")
kb/reference/adr/004-replace-areas-with-tags.md:3:type: adr
kb/notes/progressive-constraining-commits-only-after-patterns-stabilize.md:3:type: note
kb/notes/why-directories-despite-their-costs.md:3:type: note
kb/notes/stale-indexes-are-worse-than-no-indexes.md:3:type: note
kb/notes/execution-indeterminism-is-a-property-of-the-sampling-process.md:3:type: note
kb/notes/agents-navigate-by-deciding-what-to-read-next.md:3:type: note
kb/reference/adr/010-review-state-should-move-to-sqlite-once-reviews-leave-git-and-accumulate-operational-metadata.md:3:type: adr
kb/notes/links-index.md:3:type: index
kb/notes/verifiability-gradient.md:3:type: note
kb/work/skill-creator-distillation/sources/claude-code-skill-creator/scripts/run_eval.py:129:                    if event.get("type") == "stream_event":
kb/work/skill-creator-distillation/sources/claude-code-skill-creator/scripts/run_eval.py:135:                            if cb.get("type") == "tool_use":
kb/work/skill-creator-distillation/sources/claude-code-skill-creator/scripts/run_eval.py:145:                            if delta.get("type") == "input_json_delta":
kb/work/skill-creator-distillation/sources/claude-code-skill-creator/scripts/run_eval.py:157:                    elif event.get("type") == "assistant":
kb/work/skill-creator-distillation/sources/claude-code-skill-creator/scripts/run_eval.py:160:                            if content_item.get("type") != "tool_use":
kb/work/skill-creator-distillation/sources/claude-code-skill-creator/scripts/run_eval.py:170:                    elif event.get("type") == "result":
kb/notes/enforcement-without-structured-recovery-is-incomplete.md:3:type: note
kb/notes/document-types-should-be-verifiable.md:3:type: note
kb/notes/document-types-should-be-verifiable.md:21:Here, the "compiler" is a mix of agents and scripts. An agent reading `type: spec` can decide to implement from it. A script can grep for `type: structured-claim` to find citable arguments with full Evidence/Reasoning sections. But they can only do this if the type asserts something checkable. `type: design` gives them nothing to act on — every note in a design KB is "about design." An unverifiable type is like an unenforced type annotation: technically present, practically invisible. The [text testing pyramid](./automated-tests-for-text.md) sketches what enforcement could look like in practice: deterministic checks for structural contracts, LLM rubrics for judgment-dependent traits.
kb/notes/document-types-should-be-verifiable.md:31:This means we need types that are useful despite underspecification — types that assert structural properties you can check, even if the checking requires judgment rather than proof. Type assignment is itself a case of [storing an LLM output as constraining](../notes/storing-llm-outputs-is-constraining.md) — choosing to label a document `type: spec` collapses a space of possible classifications to a single point.
kb/notes/document-types-should-be-verifiable.md:46:type: note
kb/notes/document-types-should-be-verifiable.md:73:1. New content enters as `type: note` — soft, no structural claims
kb/notes/automating-kb-learning-is-an-open-problem.md:3:type: note
kb/notes/inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md:3:type: note
kb/notes/pointer-design-tradeoffs-in-progressive-disclosure.md:3:type: note
kb/notes/always-loaded-context-mechanisms-in-agent-harnesses.md:3:type: note
kb/reference/adr/015-standardize-authored-type-definitions-on-json-schema.md:3:type: adr
kb/reports/reviews/kb__reference__type-system/complexity__claim-to-section-ratio.claude-opus-4-6.md:14:**Pass.** This is a spec (`type: spec`) that serves as a reference document rather than an argument, so the claim-to-section ratio test applies differently here than to a note. The document has two sections (Base types, Migration from old flat types) and makes no novel claims — it is intentionally a lookup table for type definitions and migration mappings. As a spec, section count matching content categories is appropriate. The note itself defers the design rationale to `document-types-should-be-verifiable`, so the lack of argumentative sections is by design.
kb/notes/agent-statelessness-means-the-context-engine-should-inject-context-automatically.md:3:type: structured-claim
kb/notes/agent-statelessness-means-the-context-engine-should-inject-context-automatically.md:32:For the context engine to identify definitions, they need a machine-readable type. Definition notes now use `type: definition`, which can:
kb/notes/backlinks.md:3:type: note
kb/notes/llm-context-is-a-homoiconic-medium.md:3:type: note
kb/reference/scenario-architecture.md:3:type: note
kb/notes/notes-need-quality-scores-to-scale-curation.md:3:type: note
kb/notes/semantic-review-catches-content-errors-that-structural-validation-cannot.md:3:type: note
kb/notes/agent-runtimes-decompose-into-scheduler-context-engine-and-execution-substrate.md:3:type: note
kb/notes/tool-loop-index.md:3:type: index
kb/notes/agent-statelessness-makes-routing-architectural-not-learned.md:3:type: note
kb/notes/reverse-compression-is-when-llm-output-expands-without-adding-information.md:3:type: note
kb/reports/reviews/kb__reference__type-system/complexity__could-be-a-paragraph.claude-opus-4-6.md:14:**Pass.** The note is a reference spec, not an argument, and its tables are lookup tables rather than arguments in paragraph form. The base-types table (seven rows with structural tests and verifiability levels) and the migration table cannot be reduced to a paragraph without defeating the spec's purpose — an agent querying for what `type: adr` requires needs to find "has Context/Decision/Consequences" without parsing a paragraph. The spec is appropriately terse and its structure is functional rather than rhetorical.
kb/notes/a-knowledge-base-should-support-fluid-resolution-switching.md:3:type: note
kb/notes/memory-management-policy-is-learnable-but-oracle-dependent.md:3:type: note
kb/notes/llm-debugging-starts-with-retry-versus-rewrite-triage.md:3:type: note
kb/notes/rlm-has-the-model-write-ephemeral-orchestrators-over-sub-agents.md:3:type: note
kb/notes/distillation-status-determines-directory-placement.md:3:type: note
kb/notes/decomposition-heuristics-for-bounded-context-scheduling.md:3:type: note
kb/notes/llm-code-boundaries-are-natural-checkpoints.md:3:type: note
kb/reference/definitions/collection.md:3:type: definition
test/commonplace/cli/test_refresh_indexes.py:25:type: index
test/commonplace/cli/test_refresh_indexes.py:40:type: note
test/commonplace/cli/test_refresh_indexes.py:52:type: index
test/commonplace/cli/test_refresh_indexes.py:74:type: index
test/commonplace/cli/test_refresh_indexes.py:85:type: index
kb/notes/specification-level-separation-recovers-scoping-before-it-recovers-error-correction.md:3:type: note
kb/notes/axes-of-substrate-analysis.md:3:type: note
kb/notes/any-symbolic-program-with-bounded-calls-is-a-select-call-program.md:3:type: note
kb/notes/human-writing-structures-transfer-to-llms-because-failure-modes-overlap.md:3:type: note
kb/reference/definitions/dir-index.md:3:type: index
kb/notes/writing-styles-are-strategies-for-managing-underspecification.md:3:type: note
kb/notes/operational-signals-that-a-component-is-a-relaxing-candidate.md:3:type: note
kb/notes/research/adaptation-agentic-ai-analysis.md:3:type: note
kb/notes/research/dir-index.md:3:type: index
kb/work/skill-creator-distillation/sources/codex-skill-creator/references/dir-index.md:3:type: index
kb/notes/silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md:3:type: note
kb/notes/error-messages-that-teach-are-a-constraining-technique.md:3:type: note
kb/reference/types/adr.template.md:3:type: adr
kb/notes/convert-still-requires-semantic-description.md:3:The `/convert` skill was redesigned to be purely structural — add frontmatter with fixed values (`type: note`, `status: seedling`, `traits: []`, `areas: []`) and align the filename to the title.
kb/notes/oracle-strength-spectrum.md:3:type: note
kb/reference/control-plane-goals.md:3:type: note
kb/notes/index-curation-adds-orientation-that-generation-cannot-produce.md:3:type: structured-claim
kb/notes/a-knowledge-base-holds-theories-descriptions-and-prescriptions-with-asymmetric-linking.md:3:type: note
kb/work/skill-creator-distillation/sources/codex-skill-creator/dir-index.md:3:type: index
kb/notes/solve-low-degree-of-freedom-subproblems-first-to-avoid-blocking-better-designs.md:3:type: note
kb/notes/underspecification-and-indeterminism-complicate-programming-for-prompts-in-distinct-ways.md:3:type: note
kb/notes/methodology-enforcement-is-constraining.md:3:type: note
test/commonplace/cli/test_validate_notes.py:168:    assert results.note_type == "text"
test/commonplace/cli/test_validate_notes.py:186:type: snapshot
test/commonplace/cli/test_validate_notes.py:198:    assert results.note_type == "snapshot"
test/commonplace/cli/test_validate_notes.py:216:type: snapshot
test/commonplace/cli/test_validate_notes.py:227:    assert results.note_type == "snapshot"
test/commonplace/cli/test_validate_notes.py:238:type: note
test/commonplace/cli/test_validate_notes.py:247:    assert results.note_type == "note"
test/commonplace/cli/test_validate_notes.py:259:type: note
test/commonplace/cli/test_validate_notes.py:294:type: note
test/commonplace/cli/test_validate_notes.py:330:type: structured-claim
test/commonplace/cli/test_validate_notes.py:354:type: spec
test/commonplace/cli/test_validate_notes.py:512:type: adr
test/commonplace/cli/test_validate_notes.py:631:type: instruction
test/commonplace/cli/test_validate_notes.py:663:type: note
test/commonplace/cli/test_validate_notes.py:684:type: note
test/commonplace/cli/test_validate_notes.py:704:type: note
test/commonplace/cli/test_validate_notes.py:719:type: note
test/commonplace/cli/test_validate_notes.py:740:type: note
test/commonplace/cli/test_validate_notes.py:749:        notes_root / "types" / "adr.template.md",
test/commonplace/cli/test_validate_notes.py:752:type: adr
test/commonplace/cli/test_validate_notes.py:759:        notes_root / "types" / "adr.instructions.md",
test/commonplace/cli/test_validate_notes.py:763:        notes_root / "collection" / "types" / "nested.template.md",
test/commonplace/cli/test_validate_notes.py:776:    assert notes_root / "types" / "adr.template.md" not in discovered
test/commonplace/cli/test_validate_notes.py:777:    assert notes_root / "types" / "adr.instructions.md" not in discovered
test/commonplace/cli/test_validate_notes.py:778:    assert notes_root / "collection" / "types" / "nested.template.md" not in discovered
test/commonplace/cli/test_validate_notes.py:787:type: note
test/commonplace/cli/test_validate_notes.py:799:type: note
test/commonplace/cli/test_validate_notes.py:823:type: note
test/commonplace/cli/test_validate_notes.py:835:type: note
test/commonplace/cli/test_validate_notes.py:859:type: note
test/commonplace/cli/test_validate_notes.py:871:type: note
test/commonplace/cli/test_validate_notes.py:880:        tmp_path / "kb" / "agent-memory-systems" / "types" / "review.template.md",
test/commonplace/cli/test_validate_notes.py:883:type: note
test/commonplace/cli/test_validate_notes.py:893:type: note
kb/work/skill-creator-distillation/sources/dir-index.md:3:type: index
kb/notes/link-graph-plus-timestamps-enables-make-like-staleness-detection.md:3:type: note
kb/work/skill-creator-distillation/dir-index.md:3:type: index
kb/agent-memory-systems/reviews/o-o.md:3:type: agent-memory-system-review
kb/notes/codify-versus-llm-decision-heuristics.md:3:type: note
kb/notes/constraining-and-distillation-both-trade-generality-for-reliability-speed-and-cost.md:3:type: note
kb/agent-memory-systems/reviews/REM.md:3:type: agent-memory-system-review
kb/notes/distillation-is-transformation-not-selection.md:3:type: note
kb/agent-memory-systems/reviews/clawvault.replaced.2026-04-12.md:3:type: agent-memory-system-review
kb/notes/the-chat-history-model-trades-context-efficiency-for-implementation-simplicity.md:3:type: note
kb/agent-memory-systems/reviews/synapptic.md:3:type: agent-memory-system-review
kb/agent-memory-systems/reviews/docmason.replaced.2026-04-12.md:3:type: agent-memory-system-review
kb/notes/flat-memory-predicts-specific-cross-contamination-failures-that-are-empirically-testable.md:3:type: note
kb/notes/llm-interpretation-errors-index.md:3:type: index
kb/agent-memory-systems/reviews/cocoindex.md:3:type: agent-memory-system-review
kb/agent-memory-systems/reviews/auto-harness.md:3:type: agent-memory-system-review
kb/agent-memory-systems/reviews/CORAL.md:3:type: agent-memory-system-review
kb/notes/quality-signals-for-kb-evaluation.md:3:type: note
kb/notes/vibe-noting.md:3:type: note
kb/agent-memory-systems/reviews/crewai-memory.replaced.2026-04-13.md:3:type: agent-memory-system-review
kb/notes/agents-md-should-be-organized-as-a-control-plane.md:3:type: note
kb/agent-memory-systems/reviews/kenhuangus--llm-wiki.md:3:type: agent-memory-system-review
kb/notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md:3:type: note
kb/agent-memory-systems/reviews/pal.md:3:type: agent-memory-system-review
kb/agent-memory-systems/reviews/dynamic-cheatsheet.md:3:type: agent-memory-system-review
kb/work/token-wiki-review/dir-index.md:3:type: index
kb/notes/legal-drafting-solves-the-same-problem-as-context-engineering.md:3:type: note
kb/agent-memory-systems/reviews/hyperagents.md:3:type: agent-memory-system-review
kb/notes/discovery-is-seeing-the-particular-as-an-instance-of-the-general.md:3:type: note
kb/agent-memory-systems/reviews/g-memory.replaced.2026-04-12.md:3:type: agent-memory-system-review
kb/notes/conversation-vs-prompt-refinement-in-agent-to-agent-coordination.md:3:type: note
kb/notes/distilled-artifacts-need-source-tracking-at-the-source.md:3:type: note
kb/agent-memory-systems/reviews/operational-ontology-framework.md:3:type: agent-memory-system-review
kb/agent-memory-systems/reviews/llm-wiki.md:3:type: agent-memory-system-review
kb/notes/automated-tests-for-text.md:3:type: note
kb/agent-memory-systems/reviews/ace.md:3:type: agent-memory-system-review
kb/notes/short-composable-notes-maximize-combinatorial-discovery.md:3:type: note
kb/agent-memory-systems/reviews/arscontexta.md:3:type: agent-memory-system-review
kb/agent-memory-systems/reviews/OpenSage.md:3:type: agent-memory-system-review
kb/agent-memory-systems/reviews/atomic.md:3:type: agent-memory-system-review
kb/notes/minimum-viable-vocabulary-is-the-naming-set-that-most-reduces-extraction-cost-for-a-bounded-observer.md:3:type: note
kb/notes/evidence/single-artifact-review-bundles-still-cut-claude-costs-substantially-after-cache-aware-weighting.md:3:type: note
kb/agent-memory-systems/reviews/nao.md:3:type: agent-memory-system-review
kb/agent-memory-systems/reviews/expel.md:3:type: agent-memory-system-review
kb/notes/evidence/dir-index.md:3:type: index
kb/notes/readable-substrate-loop-is-the-tractable-unit-for-continual-learning.md:3:type: note
kb/agent-memory-systems/reviews/KBLaM.md:3:type: agent-memory-system-review
kb/agent-memory-systems/reviews/cludebot.replaced.2026-04-12.md:3:type: agent-memory-system-review
kb/work/gate-refactor/dir-index.md:3:type: index
kb/notes/psychology-to-agent-transfer-needs-per-principle-failure-mode-testing.md:3:type: note
kb/agent-memory-systems/reviews/hindsight.replaced.2026-04-12.md:3:type: agent-memory-system-review
kb/notes/fixed-artifacts-split-into-exact-specs-and-proxy-theories.md:3:type: note
kb/agent-memory-systems/reviews/cludebot.md:3:type: agent-memory-system-review
kb/notes/type-system-index.md:3:type: index
kb/agent-memory-systems/reviews/decapod.md:3:type: agent-memory-system-review
kb/notes/directory-scoped-types-are-cheaper-than-global-types.md:3:type: note
kb/notes/mechanistic-constraints-make-popperian-kb-recommendations-actionable.md:3:type: note
kb/agent-memory-systems/reviews/cognee.md:3:type: agent-memory-system-review
kb/notes/periodic-kb-hygiene-should-be-externally-triggered-not-embedded-in-routing.md:3:type: note
kb/agent-memory-systems/reviews/pi-self-learning.md:3:type: agent-memory-system-review
kb/notes/observability-index.md:3:type: index
kb/agent-memory-systems/reviews/cass_memory_system.replaced.2026-04-12.md:3:type: agent-memory-system-review
kb/notes/in-context-learning-presupposes-context-engineering.md:3:type: note
kb/agent-memory-systems/reviews/crewai-memory.md:3:type: agent-memory-system-review
kb/agent-memory-systems/reviews/docmason.md:3:type: agent-memory-system-review
kb/work/obsidian-affordances/dir-index.md:3:type: index
kb/notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md:3:type: note
kb/agent-memory-systems/reviews/virtual-context.md:3:type: agent-memory-system-review
kb/agent-memory-systems/reviews/meta-harness.md:3:type: agent-memory-system-review
kb/notes/title-as-claim-exposes-commitments-enabling-popperian-maintenance.md:3:type: note
kb/agent-memory-systems/reviews/browzy-ai.replaced.2026-04-12.md:3:type: agent-memory-system-review
test/commonplace/review/test_review_target_selector.py:36:    note_type: str = "note",
test/commonplace/review/test_review_target_selector.py:42:type: {note_type}
test/commonplace/review/test_review_target_selector.py:324:        make_note(types_dir / "definition.template.md", "Definition template", "\nBody.\n", status="current")
test/commonplace/review/test_review_target_selector.py:415:    def test_type_gated_gates_apply_only_to_matching_note_type(self, tmp_path: Path) -> None:
test/commonplace/review/test_review_target_selector.py:420:        make_note(notes_dir / "definition.md", "Definition", "\nBody.\n", note_type="definition")
test/commonplace/review/test_review_target_selector.py:777:        note = make_note(notes_dir / "definition.md", "Definition", "\nBody.\n", note_type="definition")
test/commonplace/review/test_review_target_selector.py:807:        note = make_note(notes_dir / "definition.md", "Definition", "\nBody.\n", note_type="definition")
kb/agent-memory-systems/reviews/autocontext.md:3:type: agent-memory-system-review
kb/notes/foundations-index.md:3:type: index
kb/agent-memory-systems/reviews/ace.replaced.2026-04-12.md:3:type: agent-memory-system-review
kb/agent-memory-systems/reviews/Awesome-Agent-Memory.md:3:type: agent-memory-system-review
kb/notes/automated-synthesis-is-missing-good-oracles.md:3:type: note
kb/agent-memory-systems/reviews/napkin.md:3:type: agent-memory-system-review
kb/agent-memory-systems/reviews/synapptic.replaced.2026-04-12.md:3:type: agent-memory-system-review
test/commonplace/review/test_review_runs_direct_write.py:26:def make_note(path: Path, title: str, body: str, *, traits: str = "[]", note_type: str = "note") -> Path:
test/commonplace/review/test_review_runs_direct_write.py:31:type: {note_type}
test/commonplace/review/test_review_runs_direct_write.py:134:    make_note(repo / "kb" / "notes" / "sample.md", "Sample", "\nBody.\n", note_type="definition")
kb/agent-memory-systems/reviews/reflexion.md:3:type: agent-memory-system-review
kb/work/tool-loop-control/a-framework-owned-tool-loop-can-simulate-explicit-orchestration-by-externalizing-control-state.md:3:type: note
kb/agent-memory-systems/reviews/binder.md:3:type: agent-memory-system-review
kb/agent-memory-systems/reviews/Zikkaron.md:3:type: agent-memory-system-review
kb/agent-memory-systems/reviews/cass_memory_system.md:3:type: agent-memory-system-review
kb/notes/claim-notes-should-use-toulmin-derived-sections-for-structured-argument.md:3:type: structured-claim
kb/notes/claim-notes-should-use-toulmin-derived-sections-for-structured-argument.md:46:A note with a claim title starts as `type: note`. When the argument matures — evidence accumulates, reasoning gets explicit — it gets promoted to `type: structured-claim`. The remaining notes keep `type: note` with their claim-ish titles, honest about their level of development. Of the current 30 `has-claim` notes, perhaps 5-10 are developed enough for `type: structured-claim` today.
kb/notes/claim-notes-should-use-toulmin-derived-sections-for-structured-argument.md:56:## Section template for `type: structured-claim`
kb/notes/claim-notes-should-use-toulmin-derived-sections-for-structured-argument.md:60:type: structured-claim
kb/notes/claim-notes-should-use-toulmin-derived-sections-for-structured-argument.md:95:- `type: structured-claim` → file must contain `## Evidence` and `## Reasoning` headings
kb/notes/claim-notes-should-use-toulmin-derived-sections-for-structured-argument.md:111:- **`type: structured-claim`** — notes with developed arguments that can fill Evidence/Reasoning/Caveats sections (estimated 5-10 today)
kb/notes/claim-notes-should-use-toulmin-derived-sections-for-structured-argument.md:112:- **`type: note`** — notes with claim-like titles but free-form bodies. The title-as-claim convention still applies; they just don't commit to the Toulmin scaffold.
kb/work/tool-loop-control/dir-index.md:3:type: index
kb/agent-memory-systems/reviews/xMemory.md:3:type: agent-memory-system-review
kb/agent-memory-systems/reviews/mempalace.replaced.2026-04-12.md:3:type: agent-memory-system-review
test/commonplace/review/test_ack_trivial_note_changes.py:35:type: note
test/commonplace/review/test_ack_trivial_note_changes.py:159:type: note
test/commonplace/review/test_ack_trivial_note_changes.py:170:type: note
test/commonplace/review/test_ack_trivial_note_changes.py:190:type: note
test/commonplace/review/test_ack_trivial_note_changes.py:201:type: note
test/commonplace/review/test_ack_trivial_note_changes.py:221:type: note
test/commonplace/review/test_ack_trivial_note_changes.py:232:type: note
test/commonplace/review/test_ack_trivial_note_changes.py:252:type: note
test/commonplace/review/test_ack_trivial_note_changes.py:263:type: note
test/commonplace/review/test_ack_trivial_note_changes.py:283:type: note
test/commonplace/review/test_ack_trivial_note_changes.py:294:type: note
test/commonplace/review/test_ack_trivial_note_changes.py:314:type: note
test/commonplace/review/test_ack_trivial_note_changes.py:325:type: note
test/commonplace/review/test_ack_trivial_note_changes.py:348:type: note
test/commonplace/review/test_ack_trivial_note_changes.py:406:type: note
test/commonplace/review/test_ack_trivial_note_changes.py:452:type: note
test/commonplace/review/test_ack_trivial_note_changes.py:493:type: note
test/commonplace/review/test_ack_trivial_note_changes.py:586:type: note
kb/notes/changing-requirements-conflate-genuine-change-with-disambiguation-failure.md:3:type: note
kb/agent-memory-systems/reviews/tracecraft.md:3:type: agent-memory-system-review
kb/agent-memory-systems/reviews/browzy-ai.md:3:type: agent-memory-system-review
kb/work/tool-loop-control/anatomy-of-an-llm-application.md:3:type: note
kb/agent-memory-systems/reviews/context-constitution.md:3:type: agent-memory-system-review
kb/notes/title-as-claim-makes-overlap-between-notes-visible.md:3:type: note
kb/agent-memory-systems/reviews/archie.md:3:type: agent-memory-system-review
kb/work/tool-loop-control/llm-frameworks-should-keep-the-tool-loop-optional.md:3:type: note
kb/agent-memory-systems/reviews/g-memory.md:3:type: agent-memory-system-review
test/commonplace/review/test_run_gate_sweep.py:30:type: note
kb/agent-memory-systems/reviews/pi-self-learning.replaced.2026-04-12.md:3:type: agent-memory-system-review
kb/notes/brainstorming-how-reach-informs-kb-design.md:3:type: note
kb/notes/unit-testing-llm-instructions-requires-mocking-the-tool-boundary.md:3:type: note
kb/notes/brainstorming-how-to-test-whether-pairwise-comparison-can-harden-soft-oracles.md:3:type: note
kb/notes/llm-learning-phases-fall-between-human-learning-modes.md:3:type: note
kb/agent-memory-systems/reviews/clawvault.md:3:type: agent-memory-system-review
kb/agent-memory-systems/reviews/REM.replaced.2026-04-12.md:3:type: agent-memory-system-review
kb/work/prompt-bottleneck/dir-index.md:3:type: index
kb/agent-memory-systems/reviews/gbrain.replaced.2026-04-12.md:3:type: agent-memory-system-review
kb/notes/soft-bound-traditions-as-sources-for-context-engineering-strategies.md:3:type: note
kb/agent-memory-systems/reviews/Self-Training-LLM.md:3:type: agent-memory-system-review
kb/agent-memory-systems/reviews/spacebot.md:3:type: agent-memory-system-review
kb/agent-memory-systems/reviews/sage.md:3:type: agent-memory-system-review
kb/notes/treat-continual-learning-as-substrate-coevolution.md:3:type: note
kb/agent-memory-systems/reviews/hindsight.md:3:type: agent-memory-system-review
kb/agent-memory-systems/reviews/expel.replaced.2026-04-12.md:3:type: agent-memory-system-review
kb/notes/effective-context-is-task-relative-and-complexity-relative-not-a-fixed-model-constant.md:3:type: note
kb/agent-memory-systems/reviews/autocontext.replaced.2026-04-12.md:3:type: agent-memory-system-review
kb/agent-memory-systems/reviews/napkin.replaced.2026-04-12.md:3:type: agent-memory-system-review
kb/notes/computational-model-index.md:3:type: index
kb/agent-memory-systems/reviews/agent-skills-for-context-engineering.md:3:type: agent-memory-system-review
kb/agent-memory-systems/reviews/nuggets.md:3:type: agent-memory-system-review
kb/agent-memory-systems/reviews/dynamic-cheatsheet.replaced.2026-04-12.md:3:type: agent-memory-system-review
kb/notes/process-structure-and-output-structure-are-independent-levers.md:3:type: note
kb/agent-memory-systems/reviews/xMemory.replaced.2026-04-12.md:3:type: agent-memory-system-review
kb/agent-memory-systems/reviews/mempalace.md:3:type: agent-memory-system-review
kb/notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md:3:type: note
kb/agent-memory-systems/reviews/voyager.md:3:type: agent-memory-system-review
kb/agent-memory-systems/reviews/getsentry-skills.md:3:type: agent-memory-system-review
kb/notes/generate-instructions-at-build-time.md:3:type: note
test/commonplace/lib/test_index_directory.py:20:type: note
test/commonplace/lib/test_index_directory.py:28:    write(collection / "types" / "note.template.md", "# Template\n")
test/commonplace/lib/test_index_directory.py:35:    assert "note.template.md" not in content
test/commonplace/lib/test_index_directory.py:45:type: note
test/commonplace/lib/test_index_directory.py:55:type: adr
test/commonplace/lib/test_index_directory.py:64:    write(collection / "types" / "adr.template.md", "# Template\n")
kb/agent-memory-systems/reviews/thalo.md:3:type: agent-memory-system-review
kb/agent-memory-systems/reviews/voyager.replaced.2026-04-12.md:3:type: agent-memory-system-review
kb/agent-memory-systems/reviews/exocomp.md:3:type: agent-memory-system-review
kb/notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md:3:type: note
kb/agent-memory-systems/reviews/supermemory.md:3:type: agent-memory-system-review
kb/notes/semantic-sub-goals-that-exceed-one-context-window-become-scheduling-problems.md:3:type: note
kb/agent-memory-systems/reviews/reasoning-bank.replaced.2026-04-12.md:3:type: agent-memory-system-review
kb/agent-memory-systems/reviews/sift-kg.md:3:type: agent-memory-system-review
kb/agent-memory-systems/reviews/skillnote.md:3:type: agent-memory-system-review
kb/notes/files-not-database.md:3:type: note
kb/agent-memory-systems/reviews/reasoning-bank.md:3:type: agent-memory-system-review
kb/agent-memory-systems/reviews/byterover-cli.md:3:type: agent-memory-system-review
kb/agent-memory-systems/reviews/openviking.md:3:type: agent-memory-system-review
kb/notes/traditional-debugging-intuitions-break-when-tool-loops-can-recover-semantically.md:3:type: note
kb/agent-memory-systems/reviews/MiroShark.md:3:type: agent-memory-system-review
kb/agent-memory-systems/reviews/semiont.md:3:type: agent-memory-system-review
kb/agent-memory-systems/reviews/claude-context-guard.md:3:type: agent-memory-system-review
kb/notes/agent-orchestration-occupies-a-multi-dimensional-design-space.md:3:type: note
kb/agent-memory-systems/reviews/equipa.replaced.2026-04-12.md:3:type: agent-memory-system-review
kb/notes/the-boundary-of-automation-is-the-boundary-of-verification.md:3:type: note
kb/agent-memory-systems/reviews/cq.md:3:type: agent-memory-system-review
kb/notes/agentic-systems-interpret-underspecified-instructions.md:3:type: note
kb/notes/type-system-enforces-metadata-that-navigation-depends-on.md:3:type: note
kb/agent-memory-systems/reviews/dir-index.md:3:type: index
kb/notes/ephemeral-computation-prevents-accumulation.md:3:type: note
kb/agent-memory-systems/reviews/equipa.md:3:type: agent-memory-system-review
kb/notes/structured-output-is-easier-for-humans-to-review.md:3:type: note
kb/agent-memory-systems/reviews/mentisdb.md:3:type: agent-memory-system-review
kb/notes/traversal-improvements-should-be-deferred-via-logging-to-avoid-mid-task-context-switching.md:3:type: note
kb/agent-memory-systems/reviews/reflexion.replaced.2026-04-12.md:3:type: agent-memory-system-review
kb/notes/why-notes-have-types.md:3:type: note
kb/agent-memory-systems/reviews/siftly.md:3:type: agent-memory-system-review
test/commonplace/lib/test_type_resolver.py:50:type: note
test/commonplace/lib/test_type_resolver.py:59:    assert profile.resolved_type == "note"
test/commonplace/lib/test_type_resolver.py:60:    assert profile.definition_path == tmp_path / "kb" / "types" / "note.schema.yaml"
test/commonplace/lib/test_type_resolver.py:123:type: structured-claim
test/commonplace/lib/test_type_resolver.py:132:    assert profile.resolved_type == "structured-claim"
test/commonplace/lib/test_type_resolver.py:133:    assert profile.definition_path == tmp_path / "kb" / "notes" / "types" / "structured-claim.schema.yaml"
test/commonplace/lib/test_type_resolver.py:174:    assert profile.resolved_type == "note"
test/commonplace/lib/test_type_resolver.py:175:    assert profile.definition_path == tmp_path / "kb" / "types" / "note.schema.yaml"
test/commonplace/lib/test_type_resolver.py:243:type: index
test/commonplace/lib/test_type_resolver.py:268:    assert profile.resolved_type == "index"
test/commonplace/lib/test_type_resolver.py:269:    assert profile.definition_path == tmp_path / "kb" / "types" / "index.schema.yaml"
test/commonplace/lib/test_type_resolver.py:349:    assert profile.resolved_type == "memo"
test/commonplace/lib/test_type_resolver.py:350:    assert profile.definition_path == tmp_path / "kb" / "work" / "types" / "memo.schema.yaml"
test/commonplace/lib/test_type_resolver.py:358:    assert profile.resolved_type == "text"
test/commonplace/lib/test_type_resolver.py:359:    assert profile.definition_path is None
test/commonplace/lib/test_type_resolver.py:406:type: definition
test/commonplace/lib/test_type_resolver.py:419:    assert profile.resolved_type == "definition"
test/commonplace/lib/test_type_resolver.py:420:    assert profile.definition_path == tmp_path / "kb" / "notes" / "types" / "definition.schema.yaml"
test/commonplace/lib/test_type_resolver.py:468:type: connect-report
test/commonplace/lib/test_type_resolver.py:478:    assert profile.resolved_type == "connect-report"
test/commonplace/lib/test_type_resolver.py:479:    assert profile.definition_path == tmp_path / "kb" / "reports" / "types" / "connect-report.schema.yaml"
test/commonplace/lib/test_type_resolver.py:526:type: instruction
test/commonplace/lib/test_type_resolver.py:539:    assert profile.resolved_type == "instruction"
test/commonplace/lib/test_type_resolver.py:540:    assert profile.definition_path == tmp_path / "kb" / "types" / "instruction.schema.yaml"
test/commonplace/lib/test_type_resolver.py:591:type: ingest-report
test/commonplace/lib/test_type_resolver.py:605:    assert profile.resolved_type == "ingest-report"
test/commonplace/lib/test_type_resolver.py:606:    assert profile.definition_path == tmp_path / "kb" / "sources" / "types" / "ingest-report.schema.yaml"
test/commonplace/lib/test_type_resolver.py:678:type: adr
test/commonplace/lib/test_type_resolver.py:688:    assert profile.resolved_type == "adr"
test/commonplace/lib/test_type_resolver.py:689:    assert profile.definition_path == tmp_path / "kb" / "notes" / "types" / "adr.schema.yaml"
kb/agent-memory-systems/reviews/agent-r.replaced.2026-04-12.md:3:type: agent-memory-system-review
kb/notes/capability-placement-should-follow-autonomy-readiness.md:3:type: note
kb/agent-memory-systems/reviews/hyalo.md:3:type: agent-memory-system-review
kb/notes/brainstorming-how-to-enrich-web-search.md:3:type: note
test/commonplace/lib/test_frontmatter.py:19:        r = frontmatter.parse("---\ntype: note\n---\nbody")
test/commonplace/lib/test_frontmatter.py:99:        content = '---\ndescription: "Some description here"\ntype: note\ntags: [kb-design, architecture]\nstatus: seedling\n---\n# Title\n'
test/commonplace/lib/test_frontmatter.py:110:        r = frontmatter.parse("---\ntype: note\ntype: adr\n---\n")
test/commonplace/lib/test_frontmatter.py:117:        r = frontmatter.parse("---\nnot a valid line\ntype: note\n---\n")
test/commonplace/lib/test_frontmatter.py:176:        content = "---\ntype: note\n---\n# Title\nBody."
test/commonplace/lib/test_note_parser.py:18:type: note
test/commonplace/lib/test_note_parser.py:40:type: review
kb/agent-memory-systems/README.md:3:type: index
test/scenarios/write-a-note.md:100:**Directory-local types:** When the target type is adr, index, or related-system, step 4 requires an additional hop to `kb/notes/types/{type}.template.md` plus its companion `kb/notes/types/{type}.instructions.md`. This adds extra reads for the less common specialized-type path.
test/commonplace/lib/test_project_paths.py:38:    template = write(collection / "types" / "note.template.md")
test/commonplace/lib/test_project_paths.py:39:    nested_template = write(collection / "definitions" / "types" / "definition.template.md")
test/scenarios/ingest-a-source.md:36:- **Source:** `kb/sources/types/source-review.template.md`
kb/agent-memory-systems/COLLECTION.md:11:**`reviews/`** — individual system reviews, one file per system, typed as `agent-memory-system-review`. The workflow and section rules live in `types/agent-memory-system-review.instructions.md`.
kb/agent-memory-systems/COLLECTION.md:13:**`source-only/`** — lightweight `type: note` coverage for systems known from papers, READMEs, or articles when no reachable repository has been inspected. These entries keep source-only systems visible without using the repo-required review type.
kb/agent-memory-systems/reviews/lacp.md:3:type: agent-memory-system-review
kb/agent-memory-systems/agentic-memory-systems-comparative-review.md:3:type: note
kb/agent-memory-systems/dir-index.md:3:type: index
kb/agent-memory-systems/reviews/agent-r.md:3:type: agent-memory-system-review
kb/work/write-type-resolver/plan.md:13:- `*.template.md` and `*.instructions.md` sidecars are absorbed and removed; `*.schema.yaml` files remain.
kb/work/write-type-resolver/plan.md:19:- No enum-to-path redirect table. After the migration, explicit `type:` values are paths. Enum values such as `type: adr`, `type: note`, or `type: snapshot` are validation errors.
kb/work/write-type-resolver/plan.md:61:- Type-gated review metadata such as `requires-type:` must migrate to path values too. Example: `requires-type: definition` becomes `requires-type: kb/types/definition.md`.
kb/work/write-type-resolver/plan.md:62:- Explicit `type: text` is invalid after migration. `text` remains the implicit no-frontmatter case only. Existing explicit text-typed files must either lose frontmatter if they are truly raw text, or migrate to a real type path if they carry metadata.
kb/work/write-type-resolver/plan.md:64:- The current explicit `type: text` source file (`kb/sources/psychology-solves-ai-memory-identity-construction-2025307030651871631.md`) carries metadata and should migrate to `type: kb/sources/types/snapshot.md`.
kb/work/write-type-resolver/plan.md:69:- The shipped scaffold and init tests migrate in the same bundle. Newly initialized projects must ship type-spec docs, not absorbed `*.template.md` / `*.instructions.md` sidecars.
kb/work/write-type-resolver/plan.md:73:- `spec` has exactly one KB artifact using `type: spec` today — `kb/types/note.md` — and that file is being replaced wholesale. After the migration there are no `spec`-typed artifacts in the corpus. Delete `kb/notes/types/spec.schema.yaml` in the same bundle and do not create a `spec` type-spec doc. The only remaining `type: spec` reference is a test fixture in `test/commonplace/cli/test_validate_notes.py`, which must migrate to a path-valued type or a deliberately-invalid fixture depending on what the test asserts.
kb/work/write-type-resolver/plan.md:74:- `review` is retired on the same basis. `kb/notes/types/review.schema.yaml` exists schema-only with zero KB artifacts declaring `type: review`. Delete the schema in the same bundle and do not create a `review` type-spec doc. The only remaining `type: review` reference is a test fixture in `test/commonplace/lib/test_note_parser.py`, which must migrate to a path-valued type or a deliberately-invalid fixture depending on what the test asserts.
kb/work/write-type-resolver/plan.md:81:- Use the filesystem to list every existing type sidecar in `kb/**/types/`: `*.template.md`, `*.instructions.md`, and `*.schema.yaml`.
kb/work/write-type-resolver/plan.md:84:  - **Types**: every explicit frontmatter type value and the number of files using it; the target type-spec doc path for each value; the target schema path or `null`; whether the type has existing template/instructions sidecars, schema-only support, no sidecar, or is implicit text; the migration action for explicit `type: text` files; generated or non-write-target classifications, especially source artifact types.
kb/work/write-type-resolver/plan.md:85:  - **Consumers**: every `src/` writer that emits `type:` literals; every `src/` reader that compares `type:` (e.g. `fm.get("type") == "index"`); every non-write skill or instruction that points at absorbed sidecars; every `requires-type:` reference; every test fixture that constructs typed markdown. This section is the preflight for Step 6.5 and Step 7 test-fixture migration — results from running the Step 8 cleanup regexes against the pre-migration tree are what go here.
kb/work/write-type-resolver/plan.md:86:- The inventory from 2026-04-20 had 13 explicit frontmatter type values. `spec` is retired in this migration (see the `spec` retirement policy above). `type-spec` is introduced by this migration as the self-referential meta type declared by every type-spec doc. Logical types backed by a type-spec doc after the migration: `adr`, `agent-memory-system-review`, `connect-report`, `definition`, `index`, `ingest-report`, `instruction`, `note`, `snapshot`, `source-review`, `structured-claim`, `type-spec`. Stored `type:` values are the paths to those docs (for example `type: kb/types/note.md`). `text` is the implicit no-frontmatter case only: files with no frontmatter are `text`; explicit `type: text` is invalid, and there is no `text` type-spec doc — only the `kb/types/text.md` documentation page. Sidecar-only contracts migrated without current artifact users (`task-active`, `task-backlog`, `task-recurring`) are valid type-spec docs but not part of the accepted-for-authoring list.
kb/work/write-type-resolver/plan.md:102:- For every existing `{type}.template.md` / `{type}.instructions.md` pair, create `{type}.md` in the same type directory:
kb/work/write-type-resolver/plan.md:108:- Delete absorbed `*.template.md` and `*.instructions.md` sidecars in the same migration. Leave sibling `*.schema.yaml` files in place.
kb/work/write-type-resolver/plan.md:110:- Existing `kb/types/note.md` is replaced wholesale. The current prose is redesigned, not copy-pasted, for its new role as an authoring spec. The rewritten file contains type-spec frontmatter (`type: kb/types/type-spec.md`, `name: note`, `schema: kb/types/note.schema.yaml`), authoring prose for how to write a note, a concise reference for the shared frontmatter fields (description, status ladder, trait vocabulary) so inbound links from `kb/reference/available-types.md` still find that material, and the template content absorbed from `kb/types/note.template.md`. Canonical field shape lives in `kb/types/note.schema.yaml`; design-principle discussion about why notes look this way moves to (or stays in) a dedicated theory note, not the type-spec doc. Update `kb/reference/available-types.md` link anchors if section names shift.
kb/work/write-type-resolver/plan.md:129:- Treat explicit `type: text` as invalid input to resolve during migration. The one current explicit text-typed source carries metadata and should migrate to `type: kb/sources/types/snapshot.md`.
kb/work/write-type-resolver/plan.md:131:  - `type: note` -> `type: kb/types/note.md`
kb/work/write-type-resolver/plan.md:132:  - `type: instruction` -> `type: kb/types/instruction.md`
kb/work/write-type-resolver/plan.md:133:  - `type: adr` -> `type: kb/reference/types/adr.md`
kb/work/write-type-resolver/plan.md:134:  - `type: structured-claim` -> `type: kb/notes/types/structured-claim.md`
kb/work/write-type-resolver/p
... truncated ...
```
