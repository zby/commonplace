# Paper Vocabulary Deltas

Initial comparison between `persistent-adaptive-artifacts-focused-draft.md` and the current commonplace vocabulary. This is a workshop note, not a migration proposal.

## Status

Historical. The durable KB vocabulary has since landed with different internal terms:

- `persistent adaptive artifact` -> `retained artifact`
- artifact/future-use split -> `retained artifact`, `operative part`, and `behavioral authority`
- `future system use` / `control path` / `role` -> `behavioral authority`
- `source relation` -> `lineage`
- `artifact class` / prose-symbolic-opaque shorthand -> `representational form`
- backend/storage class -> `storage substrate`

Use this file as rationale history for why the vocabulary changed, not as the current proposal.

## Main Shift

The paper moves the center of gravity from **memory** and **context engineering** toward:

- **persistent adaptive artifact** — the retained object, state, package, policy, parameter set, configuration, or derived view that carries prior experience into future behavior;
- **future system use** — the authorized way that retained artifact can later become consequential;
- **artifact-use pairing** — the operational unit: not "a memory" or "a tool" alone, but a retained artifact plus a specified future use.

This is a real vocabulary redesign candidate. It captures a distinction the KB already circles around with "artifact role", "system-definition artifact", "activation", "authority", "compiled view", and "memory lifecycle", but makes the deployment binding primary.

## Mapping To Current KB Terms

| Paper term | Closest current KB term | Delta |
|---|---|---|
| Persistent adaptive artifact | Artifact / memory artifact / learned artifact / system-definition artifact | Broader and more explicit: includes maintenance, config, policies, derived views, learned weights, and use bindings, not only objects labeled memory |
| Future system use | Activation policy / consumer surface / artifact role / behavior-changing use | Stronger deployment framing: asks how the artifact later acts, not only what it is |
| Artifact-use pairing | Artifact role plus activation path | Likely strongest new term; prevents treating role as intrinsic to the object |
| Control path | Retrieval/loading/invocation/execution/enforcement/routing | Unifies consumer, activation, and consumption mode into one route from persistence to behavior |
| Authority and scope | Authority policy / collection scope / memory governance | More use-specific; separates assigned authority from effective behavioral authority |
| Eligibility/lifecycle | Frontmatter `status`, lifecycle policy, retirement | Important split: eligibility belongs to a specific use, while current `status` is mostly artifact-level |
| Source relation | Source-of-truth / derived view / compiled view alignment | Cleaner term for canonical-vs-derived relationships and drift risk |
| Derived view | Compiled view / generated index / prompt surface / skill bundle | Strong candidate to standardize; emphasizes source relation and future use |
| Prose / symbolic / opaque artifact | Artifact class / readable vs weights / codification gradient | Preserves current prose-to-code/weights distinction but uses inspectability and consumer semantics rather than only medium |
| Knowledge use / system-definition use | Knowledge role / system-definition role | Improves the current model by making role use-specific rather than intrinsic |
| Future-Use Readiness Test | Validation / review gate / promotion checklist | Candidate prescriptive artifact after vocabulary settles |

## Terms Worth Considering For Adoption

**Artifact-use pairing.** This should probably enter the KB vocabulary somewhere. It resolves a recurring ambiguity: the same file, memory row, skill, prompt summary, or validator can be low-authority evidence in one context and behavior-shaping policy in another. The current "artifact role" language says this, but "pairing" forces the deployment binding into view.

**Future system use.** Useful as a general term for how retained material becomes consequential. It may be too bulky for always-loaded context, but it is a good workshop/library term for memory design, review of related systems, and artifact lifecycle work.

**Control path.** Strong candidate for replacing scattered phrasing around retrieval, loading, activation, invocation, execution, enforcement, and routing when the question is the route from retained artifact to later behavior.

**Eligibility.** Useful because it separates "this artifact exists" from "this artifact may be used in this way now." This avoids overloading frontmatter `status`.

**Source relation.** Good umbrella for canonical source, derived view, compiled view, stale prompt surface, and regeneration rules. It may be clearer than using "compiled view" for every derived artifact.

**Persistent adaptive artifact.** Conceptually useful but probably too heavy for always-loaded context. A shorter local term like **adaptive artifact** might work if the persistence condition is defined in the note that introduces it.

## Terms That May Need Revision

**System-definition artifact.** The paper's "knowledge use / system-definition use" argues that system-definition is not an intrinsic artifact type. It is a future use with authority over instructions, routing, execution, validation, evaluation, memory operations, or policy. The KB should keep the concept but consider revising wording from "artifact is system-definition" to "artifact is used as system definition" where precision matters.

**Memory.** The paper confirms the existing pressure: "memory" is too coarse for retained adaptation across prompts, workflows, scripts, validators, routes, derived views, policies, and checkpoints. The KB can still use "agent memory" as a domain label, but design notes should shift from "is this memory?" toward "what artifact-use pairing does this retained adaptation create?"

**Status.** Current frontmatter `status` is artifact-level. The paper's eligibility states are use-level: active for retrieval, candidate for enforcement, archival for audit, etc. The workshop should avoid merging these without a design decision.

**Artifact role.** The paper suggests role should be represented as a property of use, not only artifact class. This may revise notes that treat knowledge role and system-definition role as static properties.

**Activation.** Current notes use activation for getting memory into context before it matters. The paper's control path is broader: retrieval, preloading, explicit invocation, execution, enforcement, routing, view assembly, and review. Activation may remain a subtype.

## Operator Vocabulary Impact

The paper mostly avoids the KB's operator set:

- **Distillation** appears implicitly in source-to-derived-view compression and prompt summaries, but not as a central term.
- **Constraining** appears through authority, enforcement, validators, and symbolic artifacts, but not as the governing operator.
- **Codification** appears as the prose-to-symbolic move, again without using the term.

This is not necessarily a problem. The paper is trying to publish a deployment taxonomy; the KB is trying to operate a methodology. The redesign question is whether always-loaded vocabulary should foreground the operator set, the artifact-use pairing model, or both.

Candidate synthesis:

- Keep `distillation`, `constraining`, and `codification` as **update operators**.
- Add `artifact-use pairing`, `control path`, and `eligibility` as **deployment/accounting terms**.
- Treat `future system use` as the bridge between the two: operators produce or revise artifacts and bindings; future system use determines how they affect behavior.

## Likely Always-Loaded Consequences

The current `AGENTS.md` vocabulary probably should not absorb the full paper taxonomy. But it may need one added distinction:

> **Artifact-use pairing** — a retained artifact plus the specific future use through which it can affect behavior. The same artifact can be advice, instruction, executable tool, validator, route input, derived view, or audit evidence depending on its control path, authority, scope, and eligibility.

That single term may reduce pressure on several overloaded words without expanding the hot context too much.

## Open Questions

- Should "persistent adaptive artifact" become the public paper term while the KB uses the shorter "adaptive artifact" internally?
- Should `system-definition artifact` be renamed to `system-definition use`, or is that too disruptive?
- Should frontmatter `status` remain artifact-level while use-specific eligibility lives in review records, manifests, or lifecycle notes?
- Should `source relation` replace `compiled view` in general prose, leaving `compiled view` for generated artifacts specifically assembled for loading?
- Does `control path` belong in the agent-memory requirements notes, the artifact-analysis notes, or a new definition note?
- Is the Future-Use Readiness Test a candidate instruction/checklist, review gate, or note section template?
