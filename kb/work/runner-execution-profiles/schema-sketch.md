# Portable execution-profile schema sketch

This is a question-shaping sketch, not an adopted schema. It exists to test whether one representation can cover the inventory without confusing portable intent, runner resolution, observed provenance, and review identity.

## Required properties

The schema must:

- configure a whole procedure and override individual roles;
- express runner-neutral cost/quality intent without pretending model families are equivalent;
- allow explicit concrete runner/model/effort overrides;
- distinguish preferred settings from hard requirements;
- represent context isolation, independence from an author, concurrency, retries, and escalation;
- resolve deterministically for Codex and Claude;
- expose unsupported settings before work starts;
- record the actual runner/model/effort separately from the request;
- integrate with review `model_partition` without deriving freshness identity from a vague tier;
- support operator/project defaults without editing the shipped skill body;
- leave room for additional runners without making lowest-common-denominator capability the design center.

## Candidate shape

```yaml
execution_profile: fast-full-pass

defaults:
  runner: auto
  model_class: balanced
  effort: standard
  context: clean
  fallback: fail

roles:
  compression:
    model_class: economical
    effort: low
    escalation:
      when: uncertain-or-structural-change
      model_class: strongest

  critique:
    model_class: strongest
    effort: high
    independence:
      fresh_context: required
      different_from_author: preferred

  semantic:
    model_class: strongest
    effort: high
    review_identity:
      model_partition: explicit

  copyedit:
    model_class: economical
    effort: low
    constraints:
      semantic_changes: forbidden

runner_mappings:
  claude:
    economical: {model: configurable-claude-model, effort: runner-default}
    balanced: {model: configurable-claude-model, effort: runner-default}
    strongest: {model: configurable-claude-model, effort: runner-default}
  codex:
    economical: {model: configurable-codex-model, effort: low}
    balanced: {model: configurable-codex-model, effort: medium}
    strongest: {model: configurable-codex-model, effort: high}
```

The placeholder mappings are deliberate. Concrete defaults should be configuration, verified against current runner capabilities, not frozen into the portable schema or workshop framing.

## Candidate field groups

### Portable role intent

- `model_class`: a project-defined posture such as `economical`, `balanced`, or `strongest`; names and semantics remain open.
- `effort`: portable intent or runner-native literal—the workshop must decide whether these are separate fields.
- `quality_floor`: what failure/uncertainty must trigger escalation.
- `latency_priority` and `cost_priority`: possibly more honest than a single cheap/strong axis.

### Dispatch requirements

- `runner`: `auto`, `inherit`, a concrete runner, or an ordered preference list.
- `context`: `inherit`, `fork`, `clean`, or runner-native isolation.
- `independence`: fresh context, different model, different runner, or different author lineage.
- `concurrency`, `timeout`, `retries`, and `fallback`.
- `mutation_scope`: report-only, named output, isolated worktree, or shared workspace.

### Escalation

- triggering signals: uncertainty, parse failure, validator failure, material-change classification, disagreement, or sampled audit;
- target profile or concrete override;
- maximum escalation count;
- whether weak-model output is discarded, supplied as evidence, or hidden from the stronger judge to preserve independence.

### Resolution and provenance

- requested portable profile and role;
- resolved runner/model/effort/context;
- actual runner/model/effort reported by the worker;
- fallback or escalation taken and why;
- timestamps, latency, usage/cost when exposed;
- epistemic identity such as `model_partition`, recorded separately.

## Open design questions

1. Are model classes ordered capability tiers, cost postures, named project profiles, or some combination?
2. Is thinking effort portable enough to normalize, or should portable intent resolve into runner-native effort values?
3. Where does configuration live: project file, user file, skill frontmatter, procedure arguments, environment, or a precedence stack?
4. Can a procedure require a different runner from the artifact's author when author provenance is unknown?
5. Should review job creation receive resolved execution policy, or should the orchestrator resolve it immediately before dispatch?
6. How does a cheaper review worker choose an honest `model_partition` without exploding partitions by every effort value?
7. Which roles may cascade from cheap to strong, and which must start strong because a cheap false negative is unobservable?
8. When a stronger worker sees a cheaper worker's output, does anchoring create bias that invalidates the escalation?
9. Should whole-skill `model:` remain as a compatibility projection generated from the profile, or disappear in favor of runner-local mappings?
10. What is the portable response when a runner cannot honor model selection or effort: inherit with a warning, choose the closest mapping, or fail before dispatch?

## Evaluation cases the schema must express

- Full pass: economical compression/copyedit, strong critique/friction/semantic/synthesis, configurable closing sampling and controls.
- AutoReason: different profiles for author, synthesizer, auditor, and blind judges while preserving fresh contexts and judge independence.
- Agent-memory-system review: strong code-grounded drafting, potentially different semantic QA workers, minimal clean context, no CLI fallback.
- Warning-fix sweep: parallel economical fixes with escalation on semantic or cross-note changes.
- Scenario evaluation and note conversion: whole-skill economical execution without delegated roles.
- Review batch: an explicitly resolved worker whose concrete provenance validates against a separately declared freshness partition.
