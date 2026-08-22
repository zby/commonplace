# Working content model

This is the initial reconstruction for the workshop's governing question. It does not yet propose a closed artifact taxonomy.

## “What is stored?” has several attachment levels

A whole file is often the wrong unit. One artifact can carry a belief, a requirement, a residual selection, historical rationale, and executable instruction. The current model therefore asks four independent questions at the level each answer attaches to:

| Question | Primary unit | What it changes |
|---|---|---|
| Communicative profile | Artifact under a collection contract | Intended contribution and review priority |
| Content kind | Material proposition or operative region | Truth and choice conditions |
| Production relation | Material proposition or operative region | Refresh, re-derivation, or supersession obligations |
| Behavioral authority | Consumption path | Advice, instruction, enforcement, routing, evaluation, or learning force |

Recoverability adds a fifth maintenance question without replacing these four: can another retained surface faithfully regenerate this content, and if so, at what cost and with what warrant?

## Candidate retained payload

### Beliefs

The KB retains truth-apt propositions it uses for reasoning. Their warrant can come from sources, observations, derivation, testing, or Commonplace's own ampliative conjecture and synthesis. Being authored here rather than copied from a source does not turn a belief into a choice.

Beliefs need their modality, evidence-earned scope, counterevidence, and revision conditions. A conjecture can be retained as a belief without being treated as accepted.

### Residual choices

A functioning system must sometimes select one of several options that its beliefs, requirements, and inherited constraints leave live. The residual selection is a choice even when the alternatives have unequal consequences and even when substantial reasoning narrows them.

A proposal can hold candidate selections, but proposal status does not make them operative. Adoption, installation, or another commitment path does that. The retained payload may need the selected option, applicable constraints, rejected live alternatives, and trade-offs that implementation cannot recover.

### Requirements and inherited constraints

These constrain the choice surface but are not yet cleanly placed in the belief/choice pair. Some report facts about the environment or consumer; some express stakeholder commitments; some acquire binding force only through an operative contract. The workshop must decide whether this is one content kind, several kinds, or a cross-cutting source of constraint.

### Descriptions and caches

Faithful current-state descriptions may be derivable from implementation and therefore dispensable in principle. They can still earn retention by saving context, latency, inspection effort, or recomputation. Their risk is synchronization failure: a cache that looks canonical can conceal its own staleness.

Historical descriptions are not current-state caches. They answer to what existed or what was decided at a stated time and may preserve facts the present system no longer exposes.

### Operative system definition

Contracts, instructions, schemas, validators, configuration, routing rules, and code may directly shape behavior. Natural-language artifacts can be part of the running system when a consumer loads them with binding force; they are not merely documentation that generated something else.

Their content can still contain beliefs and choices. Behavioral force does not decide content kind, and a binding channel does not make a belief true.

### Evidence, sources, lineage, and rationale

The KB may need more than the conclusions it currently accepts. Selective revision can require the evidence, assumptions, scope boundaries, production dependencies, rejected alternatives, and reasons that made a conclusion or choice defensible. Some of this is recoverable from version history; some is irrecoverable unless explicitly retained.

The workshop must distinguish rationale needed for future criticism from process narration kept only because work happened.

### Routing and coordination surfaces

Indexes, descriptions, shared vocabulary, type contracts, and collection contracts may be retained because agents need cheap routing and a common coordination point. Their value can lie in shared adoption rather than in a theoretical claim. Their semantic home should follow that role, while their behavioral authority depends on the actual consumers that load or enforce them.

### Sources and work in flight

Source records preserve externally answerable material for later belief formation and review. Workshops retain unresolved state long enough to complete a purpose, then yield durable artifacts or disappear. Neither belongs in theory merely because later theory depends on it.

## Recovery test for documentation

For each material region, attempt recovery in both directions:

1. Can the running system faithfully regenerate the documentation content?
2. Can the documentation faithfully regenerate the running-system resolution?
3. Does a consumer execute the documentation directly instead of regenerating another artifact?
4. If the content is recoverable, does retaining it still save enough bounded context, latency, recognition effort, or audit cost to justify synchronization risk?
5. If it is not recoverable, is it needed for truth assessment, future revision, re-coordination, or only historical narration?

Generator, cache, directly operative artifact, and archival rationale are therefore roles of regions and paths, not mutually exclusive document classes.

## Tests for collection placement

- **Theory:** would the central distinction or mechanism still be meaningful when Commonplace's current implementation and conventions are replaced by a different system?
- **Reference:** is the content true because Commonplace adopted, implemented, or currently exposes this architecture or rule?
- **Instructions:** does the content primarily direct an operator's next action, including defaults, ordering, or stopping conditions?
- **Sources:** does the artifact's principal obligation remain fidelity to captured external material rather than a claim Commonplace now owns?
- **Work:** is the governing question or disposition still unresolved, such that the artifact's value will be consumed by completing the investigation?

These are contribution tests, not intrinsic information kinds. A reference artifact may report beliefs about the shipped system; a theory note may discuss mechanisms instantiated by machinery.

## Open forks

- Are definitions supporting apparatus for theories rather than beliefs themselves, and if so, what minimum theoretical dependence justifies their presence in `kb/notes/`?
- Are requirements and inherited constraints truth-apt descriptions, adopted commitments, behavioral-authority relations, or a family needing its own content distinction?
- Which rationale is required for selective revision, and which belongs only in git history or workshop records?
- Should `knowledge artifact` and `system-definition artifact` survive as convenient authority-family shorthands now that behavioral authority is path-relative?
- Does the generator/cache distinction need a separate cost axis for recoverable-but-worth-retaining content?
- What admits an artifact to the KB at all: a universal theory of answerability, a chosen framework boundary, or collection-specific contracts?

