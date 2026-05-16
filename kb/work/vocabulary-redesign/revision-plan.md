# Vocabulary Revision Plan

Plan for revising the KB vocabulary in response to `persistent-adaptive-artifacts-focused-draft.md`. This plan deliberately separates workshop analysis from durable edits.

## Goal

Adopt the useful part of the paper vocabulary without turning `AGENTS.md` into a paper abstract.

The likely shape is:

- keep the current operator vocabulary (`distillation`, `constraining`, `codification`) as the KB's update-mechanism language;
- add a small deployment/accounting vocabulary around retained artifacts and their future uses;
- revise memory and system-definition prose so role is not treated as intrinsic to an artifact when the use binding is what matters.

## Non-Goals

- Do not rewrite every note in one pass.
- Do not replace the existing definition-note system with a new ontology.
- Do not add schema or validator changes until the vocabulary is stable.
- Do not import the full paper terminology into always-loaded context.

## Proposed First-Pass Decisions

| Term | Decision | Rationale |
|---|---|---|
| Context engineering | Keep always-loaded | Still names the domain and explains routing/loading/scoping work |
| Distillation | Keep always-loaded | Still the main compression/update operator for KB artifacts |
| Constraining | Keep always-loaded | Still names narrowing interpretation space across prose, schemas, validators, and code |
| Codification | Keep always-loaded | Still names the prose-to-symbolic transition |
| Register | Tentatively demote from always-loaded | Important for collection authors, but probably collection-loaded rather than globally loaded |
| Workshop | Keep, but pair with library | Operational boundary is important; the current gloss should make the library contrast explicit |
| Artifact-use pairing | Add, likely always-loaded | One compact term resolves memory/tool/skill/policy ambiguity by naming retained artifact plus future use |
| Future system use | Add to definition note / migration note, not necessarily `AGENTS.md` | Useful but slightly heavy for always-loaded vocabulary |
| Control path | Add to definition note / memory requirements | Strong concept for how retained material reaches behavior |
| Eligibility | Add to lifecycle discussion | Separates artifact existence/status from use-specific activation permission |
| Source relation | Add to compiled-view / lifecycle discussion | Clarifies canonical source, derived view, drift, regeneration |
| Persistent adaptive artifact | Use in paper-facing notes; maybe shorten internally to adaptive artifact | Conceptually broad, but too heavy for hot context unless shortened |

## Phase 1: Vocabulary Audit

Purpose: identify where the paper vocabulary changes existing claims rather than merely renaming them.

Tasks:

1. Search current notes for `system-definition`, `artifact role`, `activation`, `compiled view`, `status`, `memory`, `authority`, and `lifecycle`.
2. Mark each hit as one of:
   - already compatible with artifact-use pairing;
   - should be revised from intrinsic-artifact language to use-specific language;
   - unrelated ordinary usage.
3. Identify the smallest set of high-traffic notes that need revision first.

Expected output:

- `audit-results.md` in this workshop with path-level findings and recommended edit order.

## Phase 2: Definition Drafts

Purpose: draft vocabulary changes before editing durable docs.

Draft in workshop first:

1. A definition note for `artifact-use pairing`.
2. A short vocabulary migration note mapping:
   - artifact role -> artifact-use pairing;
   - system-definition artifact -> system-definition use, where precision matters;
   - activation -> control path, where broader than context loading;
   - status -> artifact-level state vs use-specific eligibility;
   - compiled view -> derived view / source relation, where source alignment is the issue.
3. A proposed `AGENTS.md` Vocabulary replacement block.

Expected output:

- `definition-drafts.md`
- `agents-vocabulary-proposal.md`

## Phase 3: Durable Minimal Edit

Purpose: land the smallest durable vocabulary change that improves future work.

Candidate first durable edits:

1. Add a definition note:
   - `kb/notes/definitions/artifact-use-pairing.md`
2. Revise `AGENTS.md` Vocabulary:
   - add `Artifact-use pairing`;
   - keep `Context engineering`, `Distillation`, `Constraining`, `Codification`, `Workshop`;
   - either demote `Register` or shorten it and note it is collection-authoring vocabulary.
3. Update `kb/notes/definitions/dir-index.md` via `commonplace-refresh-indexes`.

Hold point:

- Do not touch broad memory-design notes until this minimal edit reads cleanly in context.

Validation:

- `commonplace-validate AGENTS.md` if supported as text.
- `commonplace-validate kb/notes/definitions/artifact-use-pairing.md`
- `commonplace-validate kb/notes/definitions/dir-index.md`

## Phase 4: Targeted Propagation

Purpose: update notes where the old vocabulary would now actively mislead.

Likely targets:

- `kb/notes/memory-design-adds-operational-axes-to-artifact-analysis.md`
- `kb/notes/system-definition-artifacts-are-crystallized-reasoning-under-context.md`
- `kb/notes/agent-memory-requirements/activate-behavior-changing-memory.md`
- `kb/notes/agent-memory-requirements/keep-compiled-views-aligned.md`
- `kb/notes/agent-memory-requirements/retire-redact-supersede-relax.md`
- `kb/agent-memory-systems/trace-derived-learning-techniques-in-related-systems.md`

Edit rule:

- Prefer local clarifying paragraphs over global rewrites.
- Keep old terms where they still work, but add the use-specific distinction where it changes design decisions.

Validation:

- Validate each touched note.
- Run a semantic review bundle only on notes where the central claim changes.

## Phase 5: Optional Codification

Purpose: only after the vocabulary proves stable, decide whether any distinction can become a check.

Candidate checks:

- Review gate: warns when a note calls something "memory" but does not specify future use / control path.
- Review gate: warns when a high-authority derived view lacks source relation / refresh story.
- Authoring checklist: artifact-use record for validators, skills, generated prompt views, and learned policies.

Do not implement these until at least one durable note successfully uses the vocabulary.

## Proposed `AGENTS.md` Shape

Draft direction, not final text:

```markdown
- **Context engineering** — the architecture and machinery for getting the right knowledge into a bounded context at the right time. Includes routing, loading, scoping, maintenance, and observability.
- **Distillation** — goal-oriented compression whose purpose is the capacity change it produces in a bounded consumer; in this KB, directed context compression.
- **Constraining** — narrowing the interpretation space of an artifact or use, trading generality for reliability, speed, cost, and verifiability.
- **Codification** — constraining that crosses from natural language into a symbolic medium such as code, schema, tests, or validators.
- **Artifact-use pairing** — a retained artifact plus the specific future use through which it can affect behavior. The same artifact can be advice, instruction, executable tool, validator, route input, derived view, or audit evidence depending on its control path, authority, scope, and eligibility.
- **Workshop** — a named temporal workspace for work-in-flight artifacts; contrast with the library layer where value accumulates.
```

Open question: whether `Register` remains here, moves to collection docs only, or stays as a shorter collection-authoring term.

## Commit Strategy

Commit in small units:

1. Workshop plan and audit artifacts.
2. Definition draft promoted to `kb/notes/definitions/`.
3. `AGENTS.md` vocabulary change plus generated definition index.
4. Targeted note migrations in separate commits by theme.

Keep workshop files uncommitted or committed according to operator preference; durable KB edits should not depend on untracked workshop state.
