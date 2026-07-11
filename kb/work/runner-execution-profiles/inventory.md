# Execution-policy inventory

Status: initial repository-grounded catalogue, 2026-07-11. This is not complete until the repeatable completeness sweep and runner capability verification are recorded.

## Catalogue fields

Each execution locus should eventually carry:

| Field | Meaning |
|---|---|
| `locus_id` | Stable repo-path plus role identifier |
| `source` | Canonical skill, instruction, code, or configuration path |
| `role` | Parent or delegated role being configured |
| `surface` | Skill invocation, harness worker, dynamic workflow, review job, or external runner |
| `declared_model` | Literal current declaration, if any |
| `declared_effort` | Literal current effort/thinking declaration, if any |
| `inheritance` | Inherited, overridden, selected at runtime, or unknown |
| `isolation` | Same context, fork, clean worker, fresh worker, different runner, or unspecified |
| `epistemic_effect` | None, report provenance, review partition, verdict evidence, or other |
| `fallback` | Current behavior when the requested execution is unavailable |
| `status` | Catalogued, capability-unverified, trialled, or migrated |

## Declarative whole-skill model policy

Nine canonical skills currently declare Claude-style `model:` frontmatter. The declaration applies to the skill invocation as a whole; it does not express different models for roles the skill later delegates.

| Source | Current model | Context | Notes |
|---|---|---|---|
| `cp-skill-connect/SKILL.md` | `opus` | fork | Discovery and connection judgment |
| `cp-skill-write/SKILL.md` | `opus` | fork | Note authoring |
| `cp-skill-ingest/SKILL.md` | `opus` | fork | Source analysis |
| `write-agent-memory-system-review/SKILL.md` | `opus` | fork | Parent plus delegated drafting and semantic QA |
| `cp-skill-revise-iterative/SKILL.md` | `opus` | fork | Parent invokes non-interactive Claude revision calls; nested runner model/effort is not declared |
| `cp-skill-revise-autoreason/SKILL.md` | `opus` | fork | Parent plus many Codex actor roles, all currently inherited/unspecified |
| `cp-skill-convert/SKILL.md` | `sonnet` | fork | Structured conversion |
| `cp-skill-snapshot-web/SKILL.md` | `sonnet` | fork | Snapshot routing and capture |
| `evaluate-scenarios/SKILL.md` | `sonnet` | fork | Mostly measurement and aggregation |

Questions the catalogue must resolve:

- Which runners honor these fields, ignore them, or translate them differently?
- Does `model: opus|sonnet` name a concrete model, a moving alias, or an intended capability tier?
- When a skill delegates, does its model policy apply only to the parent, inherit into workers, or need role-specific overrides?

## Delegated execution loci

| Source | Roles | Current execution policy | Gap |
|---|---|---|---|
| `run-full-improvement-pass-on-note.md` | compression reviewer, critique worker, friction worker, semantic reviewers, connect, synthesizer/editor, copyeditor, closing reruns, control judges | Mostly fresh workers on the inherited session model; review jobs record model/effort | No role-level model or effort configuration; high- and low-judgment work are treated alike |
| `run-review-batches.md` | assay worker per homogeneous job | Explicitly inherits orchestrator model; concrete model/effort reported at finalization; partition fixed before dispatch | Deliberately forbids override in the ordinary procedure, so cheaper routing requires a new resolution rule that preserves partition honesty |
| `run-compression-bundle-on-note.md` | compression report worker | Fresh worker, model/effort unspecified | Strong candidate for cheaper routing, but unmeasured |
| `critique-note.md` | adversarial critic | Fresh worker or different runner from author | Independence is specified; strength/cost posture and effort are not |
| `composition-friction-gate.md` | adversarial friction analyst | Fresh worker, different runner from author | Independence is specified; model/effort are not |
| `cp-skill-revise-autoreason/SKILL.md` | critic, revision author, synthesizer, auditor, three judges, reruns | Fresh Codex workers; whole skill uses `opus`; judges parallelized | Role count is explicit but every role effectively shares one unspecified worker policy |
| `write-agent-memory-system-review/SKILL.md` | drafting worker, semantic QA workers | Fresh minimal-context worker; harness mechanism only; whole skill uses `opus` | Drafting and semantic judgment cannot be configured independently |
| `fix-warnings/fix-review-warnings-sweep.md` | one fixer per note | Parallel sub-agents; model/effort unspecified | No mapping from finding complexity to worker strength or escalation |
| `FIX-SYSTEM.md` | one fixer per note | Delegation and parallelism only | Same policy gap as the sweep instruction |
| `revise-note.md` | tag-change follow-up worker | Spawned only after tag changes; narrow write scope | Likely mechanical role, but no cheap-model declaration or verification |

Incidental mentions that are not execution loci—examples, theory, or prose merely saying an artifact may be handed to a worker—remain searchable but should not receive configuration rows.

## Runner and review surfaces already represented

| Surface | Existing representation | What it does not yet solve |
|---|---|---|
| Skill frontmatter | `model: opus|sonnet`, `context: fork` | Cross-runner meaning, role-specific workers, effort, fallback |
| Claude dynamic workflow | Per-call `model` documented in the external-system review | Commonplace schema, Codex mapping, effort/provenance behavior |
| Harness sub-agent tools | Fresh/forked worker prose in instructions | Uniform portable arguments and capability detection |
| Review job | `model_partition`; finalization provenance `runner`, concrete model, effort | Choosing the worker before dispatch; portable cost/quality policy |
| Review model registry | Concrete aliases grouped into freshness partitions; effort normalization | It is epistemic identity/validation, not a general task-routing table |
| External CLI calls | `cp-skill-revise-iterative` invokes `claude -p` | Authorized cross-runner procedure, nested model/effort selection, portability |

## Initial fragmentation findings

1. Model policy is attached to whole skills even when the skill contains heterogeneous roles.
2. Most delegated roles specify isolation and ownership more carefully than model or effort.
3. “Fresh worker,” “different runner,” and “strong model” are independent requirements but currently tend to collapse into one inherited dispatch choice.
4. Review execution has the best provenance model but intentionally couples ordinary workers to the orchestrator's partition.
5. The current repository contains runner-specific names (`opus`, `sonnet`, Codex actors) but no shared vocabulary for portable execution intent.
6. There is no uniform unavailable-capability rule: procedures variously inherit, stop, request local fallback, or invoke an external CLI.
7. Cheap work is identifiable informally—measurement, mechanical edits, formatting, candidate generation—but no schema records why cheap execution is safe or when to escalate.

## Completeness sweep

The repeatable audit must cover canonical files and inspect every match, not just count them:

```bash
rg -n '^model:' kb/instructions --glob 'SKILL.md'
rg -n -i 'sub-agent|subagent|worker|runner|model partition|model-partition|reasoning effort|thinking effort|model:' \
  kb/instructions kb/reference src/commonplace --glob '*.md' --glob '*.py' --glob '*.yaml' --glob '*.json'
```

Generated skill projections are excluded. Historical ADRs and proposals are evidence for design history, not current execution loci, but any still-open requirement they contain should be linked from the appropriate catalogue row.
