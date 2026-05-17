# Vocabulary Revision Plan

Plan for propagating the landed KB vocabulary after the artifact-analysis redesign. This replaces the earlier proposal to adopt `artifact-use pairing` and related paper terms.

## Current State

The useful part of the paper vocabulary has been translated into the KB's internal vocabulary:

- `retained artifact`
- `operative part`
- `storage substrate`
- `representational form`
- `lineage`
- `behavioral authority`
- `knowledge artifact`
- `system-definition artifact`

The current goal is not to choose the vocabulary from scratch. It is to propagate the landed terms through high-traffic notes and write paths, while keeping paper-facing terms in paper/workshop artifacts where they are useful.

## Non-Goals

- Do not rewrite every note in one pass.
- Do not replace the definition-note system with a new ontology.
- Do not add schema or validator changes until the vocabulary has survived more use.
- Do not treat paper terms as internal hot-path terms unless a later decision reverses the current landing.

## Adopted Decisions

| Old or candidate term | Current term | Notes |
|---|---|---|
| Persistent adaptive artifact | Retained artifact | Internal term; paper-facing term can remain in paper drafts |
| Artifact-use pairing | Retained artifact + operative part + behavioral authority | Pairing was useful as a bridge but too bundled for durable use |
| Future system use | Behavioral authority / consumption path | Authority records consumer, channel, and force |
| Control path | Behavioral authority | Use "channel" or "consumption path" where route is specifically meant |
| Source relation | Lineage | Lineage covers source dependencies and derivation status needed for invalidation/regeneration |
| Backend / storage class | Storage substrate | Storage is one field, not the taxonomy |
| Artifact class | Representational form | Form classifies how operative parts are encoded and consumed |
| Opaque artifact | Distributed-parametric form, plus opacity as scale/property | Opaque is now an inspectability threshold, not a form name |
| Knowledge role | Knowledge artifact | Authority-path family, not intrinsic object type |
| System-definition role/use | System-definition artifact | Authority-path family, not form or substrate |
| Eligibility | Lifecycle/authority metadata | Useful, but not one of the four core artifact-analysis fields |

## Phase 1: Confirm Hot Paths

Purpose: make sure the current write and read paths teach the landed vocabulary consistently.

Tasks:

1. Check `AGENTS.md` Vocabulary for all adopted terms and links.
2. Check `kb/notes/definitions/dir-index.md` and curated indexes for discoverability.
3. Check `kb/notes/axes-of-artifact-analysis.md` as the main conceptual router.
4. Check `kb/notes/memory-design-adds-operational-axes-to-artifact-analysis.md` as the memory-design companion.
5. Check agent-memory review type specs and skill instructions for the new terms.

Expected output:

- A short audit note or checklist in this workshop if gaps remain.

## Phase 2: Replace Stale Shorthand

Purpose: update high-traffic notes where old terms would now mislead.

Search targets:

- `artifact-use pairing`
- `future system use`
- `control path`
- `source relation`
- `artifact role`
- `knowledge role`
- `system-definition role`
- `artifact class`
- `backend`
- `opaque artifact`

Edit rule:

- Preserve historical or paper-facing usage in workshop/paper files.
- In durable notes, prefer local clarifying edits over broad rewrites.
- Keep ordinary words like "backend", "role", or "class" when they are not standing in for the artifact-analysis fields.

Likely durable targets:

- `kb/notes/system-definition-artifacts-are-crystallized-reasoning-under-context.md`
- `kb/notes/agent-memory-requirements/activate-behavior-changing-memory.md`
- `kb/notes/agent-memory-requirements/keep-compiled-views-aligned.md`
- `kb/notes/agent-memory-requirements/retire-redact-supersede-relax.md`
- `kb/agent-memory-systems/trace-derived-learning-techniques-in-related-systems.md`
- agent-memory review files that still use role/backend/class shorthand as taxonomy

## Phase 3: Align Write Paths

Purpose: make new writing use the landed vocabulary without hardcoding every term in the generic write skill.

Tasks:

1. Keep `cp-skill-write` generic: it should load collection and type policies, not know the vocabulary list.
2. Put general vocabulary usage rules in collection conventions or the emerging vocabulary-governance design.
3. Keep type-specific requirements in type specs, especially `agent-memory-system-review`.
4. Avoid forcing artifact-analysis vocabulary into notes where it does not change the design decision.

Related workshop:

- [Vocabulary governance](../vocabulary-governance/README.md) handles global vs collection-local vs type-specific vocabulary policy.

## Phase 4: Review And Validation Candidates

Purpose: only after propagation, decide what can become a check.

Candidate checks:

- Review warning when a note uses "memory" as a design answer without naming storage substrate, representational form, lineage, or behavioral authority where those fields matter.
- Review warning when a derived high-authority artifact lacks lineage or refresh story.
- Review warning when a note treats `knowledge artifact` or `system-definition artifact` as intrinsic form/substrate rather than authority-path family.
- Advisory undefined-term check for active vocabulary terms without first-mention gloss/link.

Do not implement these until the vocabulary has stabilized in enough notes to avoid noisy gates.

## Proposed `AGENTS.md` Shape

Already landed in current form. Future edits should test whether this cluster is too large for always-loaded context:

- `Context engineering`
- `Distillation`
- `Constraining`
- `Codification`
- `Retained artifact`
- `Operative part`
- `Storage substrate`
- `Representational form`
- `Lineage`
- `Behavioral authority`
- `Knowledge artifact`
- `System-definition artifact`
- `Register`
- `Workshop`

Open questions:

- Does `register` remain always-loaded or move to collection-authoring context?
- Does `operative part` need more examples to be teachable in hot context?
- Should `knowledge artifact` and `system-definition artifact` remain always-loaded, or be loaded only when artifact analysis is in play?
- Should `eligibility` eventually become a definition note, or remain memory-lifecycle vocabulary?

## Commit Strategy

Commit in small units:

1. Workshop updates that mark the new vocabulary as landed.
2. Hot-path documentation fixes.
3. Targeted note migrations by theme.
4. Optional review-gate or validation changes only after the language proves stable.

When adding or revising artifacts, prefer atomic artifact commits over temporary README/index consistency.
