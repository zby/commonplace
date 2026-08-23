# Working content model

This is the reconstruction for the workshop's governing question. It does not propose a closed artifact taxonomy, but it now has a settled organizing rule.

## The organizing rule: bind choices in theory; record selections and state in reference

The maintainer's boundary, adopted 2026-08-22 and sharpened 2026-08-23, is that **`kb/notes/` holds beliefs about the design space, with particular system choices bound; `kb/reference/` holds the choices Commonplace made and the current or historical state they produced**. Notes ask what is true, or believed true, about how systems of this kind can work. Reference records the values Commonplace assigned within that space and faithfully describes the resulting system.

The operational placement test comes from the notes collection's existing formulation constraint. A note's intended contribution must remain a substantive truth-apt claim when every particular system choice it names is bound universally, through equivalent generic or conditional grammar, or existentially as a witness. If binding leaves only “Commonplace selected X” or “Commonplace currently does Y,” the contribution is a Commonplace record and belongs in reference. This is not a counterfactual test: observations and choice records can both change when a choice is varied, so asking what would remain true cannot distinguish them.

**Why this split survives where derived/committed failed.** The workshop's first attempt split content into derived and committed, and it failed: Commonplace can produce an ampliative theory not entailed by its sources, so producing it is a commitment while what it asserts stays truth-apt. That objection does not reach belief/choice, because belief/choice asks what the content *is*, not how it was produced. The ampliative theory is a belief; that its production was a commitment is recorded on the production-relation axis. The earlier split failed by conflating two axes that this one keeps apart.

**What it predicts that a profile label does not.** Beliefs and choices have different revision rules. A belief is revised against evidence — rewritten in place, holistically, and the superseded version has no standing in its former role. A choice is superseded rather than corrected, and the earlier choice remains a fact about what this system once committed to. Current-state descriptions refresh when the implementation changes, while historical state stays as part of the record. That is why ADR chains are append-only, reference descriptions track the system, and notes get holistic rework. The theoretical/descriptive labels had to state these as separate conventions; content and contribution explain them.

## “What is stored?” has several attachment levels

A whole file is often the wrong unit. One artifact can carry a belief, a requirement, a residual selection, historical rationale, and executable instruction. The model asks five independent questions at the level each answer attaches to:

| Question | Primary unit | What it changes |
|---|---|---|
| Content kind — belief or residual choice | Material proposition or operative region | Truth and choice conditions; review and retention obligations |
| Production relation | Material proposition or operative region | Refresh, re-derivation, or supersession obligations |
| Behavioral authority | Consumption path | Advice, instruction, enforcement, routing, evaluation, or learning force |
| Intended contribution | Whole artifact, stated by its title, description, and opening | Whether the artifact offers choice-bound theory, records Commonplace's selection or state, or serves another collection role |
| Collection prototype | Collection, at creation time only | Which existing contract a new collection starts from |

Recoverability adds a sixth maintenance question without replacing these five: can another retained surface faithfully regenerate this content, and if so, at what cost and with what warrant?

The collection-prototype question was previously called communicative profile and was listed first, as though a live classifier. It has been recast as a creation-time input — see [the completed retirement task](./tasks/retire-profiles-for-collection-prototypes.md) — because nothing was inherited from a profile at use time. Every `COLLECTION.md` states its contract in full locally, so the former label carried no force once the collection existed.

**The unit mismatch is handled through intended contribution, case by case.** Content kind attaches to a proposition or region; a collection boundary is necessarily file-level. The title, description, and opening state the artifact's intended contribution, and that contribution determines placement. Supporting local observations, rationale, and explicitly scoped choice reports may remain without becoming independent contributions. There is no general mixed-artifact threshold yet. Prefer splitting when it yields atomic, independently useful notes; decide the residual hard cases individually.

## Candidate retained payload

### Beliefs

The KB retains truth-apt propositions it uses for reasoning. Their warrant can come from sources, observations, derivation, testing, or Commonplace's own ampliative conjecture and synthesis. Being authored here rather than copied from a source does not turn a belief into a choice.

Beliefs need their modality, evidence-earned scope, counterevidence, and revision conditions. A conjecture can be retained as a belief without being treated as accepted.

**Truth-aptness of a particular does not decide placement.** An observation about Commonplace itself — a traced episode, a cost measurement, an audit of what some mechanism achieved — is a belief, but it belongs in notes only when the artifact uses the particular as a substantive existential witness or supports another choice-bound inference about the design space. Existing `kb/notes/evidence/` artifacts do this: their titles and openings state what a bounded experiment, trace, or case establishes and delimit the inference. The larger theory may remain incomplete, but an observation whose theory-facing inference is still unresolved remains in `kb/work/`; a first occurrence or pure pattern record without explanation belongs in `kb/log.md`. A report whose intended contribution is only the local episode or current state remains reference even though every sentence is truth-apt.

`kb/reference/` currently holds `tag-readme-trace-observed-causal-connection.md`, `harness-sub-agent-model-selection-regression.md`, and `commonplace-as-a-reflective-system.md`. They are **candidates for individual reassessment**, not one class and not authorized moves. Relocation is warranted only where binding Commonplace's choices leaves a substantive claim about feasibility, mechanism, or consequence that is already the artifact's intended contribution. The harness regression is primarily an operational incident about an external tool and may remain reference or belong with its external-system evidence.

### Residual choices

A functioning system must sometimes select one of several options that its beliefs, requirements, and inherited constraints leave live. The residual selection is a choice even when the alternatives have unequal consequences and even when substantial reasoning narrows them.

A proposal can hold candidate selections, but proposal status does not make them operative. Adoption, installation, or another commitment path does that. The retained payload may need the selected option, applicable constraints, rejected live alternatives, and trade-offs that implementation cannot recover.

### Requirements and inherited constraints

These constrain the choice surface. The belief/choice rule does not dissolve the category, but it does decompose most instances: a requirement typically pairs a belief that supports it with a commitment that adopts it. "Notes must be self-sufficient" is a choice Commonplace made; "self-sufficient notes cost less to traverse" is the belief it rests on. Split that way, each half has a home and the pairing is carried by a `rests-on` edge.

What resists the decomposition is a requirement whose force comes from outside — a platform limit, a consumer's fixed interface, an inherited constraint nobody here selected. That is neither a belief Commonplace formed nor a choice it made, and it is the residue the workshop still has to place. Whether it is one kind or several remains open.

### Descriptions and caches

Faithful current-state descriptions may be derivable from implementation and therefore dispensable in principle. They can still earn retention by saving context, latency, inspection effort, or recomputation. Their risk is synchronization failure: a cache that looks canonical can conceal its own staleness.

**Current-state descriptions belong in `kb/reference/`.** Their intended contribution is faithful representation of the system Commonplace's selections produced. `architecture.md`, `lib-modules.md`, `commands.md`, `storage-architecture.md`, `freshness-schemas.md`, and the code-architecture halves of `review-architecture.md` and `freshness-architecture.md` are therefore correctly placed even though much of their content is derived from implementation.

The recovery test decides how to maintain this reference content, not where it belongs. Per artifact, Commonplace can generate the description, register it for staleness against the code it describes, author only the irrecoverable part, or minimize it when the synchronization cost exceeds its routing and context value. A generated or freshness-tracked description remains reference.

Historical descriptions also belong in reference when their intended contribution is what Commonplace once chose, exposed, or did. A historical episode can instead support a note when it is bound as a substantive witness for a claim about the design space; the inference, not mere truth-aptness of the episode, is what changes the placement.

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

This workshop resolves only the boundary between `kb/notes/` and `kb/reference/`. The special rules of instructions, sources, work, external-system collections, and articles continue to route artifacts whose operative role, fidelity obligation, lifecycle, subject system, or publication state decides their home. Apply the binding test only after the live choice is notes versus reference.

For that boundary, ask of the artifact's intended contribution: **after every particular system choice it names is bound, does a substantive claim about the design space remain?** Universal, generic, and conditional formulations bind the choice directly. An existential formulation qualifies only when the particular is evidence for feasibility, mechanism, or a bounded consequence; “Commonplace chose X” recast as “there exists a system that chose X” is not by itself a substantive theoretical contribution.

- **Notes:** the intended contribution remains a substantive truth-apt claim after its system choices are bound. Particular observations may supply existential evidence for that claim; truth-aptness alone does not place them here.
- **Reference:** the intended contribution records a choice Commonplace made or faithfully describes the current or historical state that choice produced. Binding removes rather than generalizes the contribution.
- **Other collections:** follow their local contracts. An imperative surface routes to instructions, fidelity to captured external material routes to sources, an unresolved disposition routes to work, and external-system or publication roles route to their dedicated collections before this two-way test runs.

**Subject matter is not placement.** A note may discuss machinery at length if its intended claim ranges over any system built that way. A reference artifact may contain supporting belief propositions without becoming a note. The test runs on what survives binding in the intended contribution, not on topic and not on whether every sentence is truth-apt.

## Publishability: a choice named in a theory must be a bound variable

The boundary earns its keep twice, and maintenance is only the first way. The second is that notes get published. `kb/articles/` distils them for "highly technical readers with no KB context" — a reader who has none of Commonplace's choices.

That sets a hard condition on how a note may mention a choice. A **free** occurrence — a claim whose truth conditions silently depend on a selection Commonplace made, while the sentence presents as general — does not survive publication. Stripped of the local context that made it true, it reads as either false or empty. A note asserting that a collection's contract file declares its quality goal is not stating a mechanism; it is reporting a Commonplace choice in a general voice.

A note may name a choice only under a quantifier:

- **Universally bound.** "For any system that localizes authoring contracts per subtree, X follows." The choice ranges over the design space and Commonplace's selection is one value. This is the shape that transfers.
- **Existentially bound, as witness.** "At least one system does X, so X is feasible and these consequences are observed." The particular is evidence for a claim about the space, not the subject of the claim.

**The binding test comes with two dispositions.** If a substantive proposition remains with the selection as a parameter, bind it and keep the theory. If the whole intended contribution is the selected value or the state it produced, there is nothing substantive to generalize; reference preserves the local record. Neither disposition is preferred independently of what remains after binding.

That is the same constraint as the collection's stated quality goal. A claim with a free choice-variable has no [explanatory-reach](../../notes/first-principles-reasoning-selects-for-explanatory-reach-over.md) beyond the system that made the choice; binding the variable lets the claim state what transfers. Publishability, reach, and the notes/reference boundary are one requirement seen three ways.

**The test cuts one way.** Reference cannot fail a theory-formulation gate, because reporting Commonplace's selections and state in a local voice is exactly its job. Binding is the eligibility test for the notes side of this two-collection boundary, not a writing requirement imposed on reference.

Two existing notes supply the halves. [A framework rule with a boundary-preserving rival is not inherited](../../notes/a-framework-rule-with-a-boundary-preserving-rival-is-not-inherited.md) detects the defect: if a rival design preserves the invariants while dropping the rule, the rule was a choice. [A universal knowledge framework demotes content taxonomies to defaults](../../notes/a-universal-knowledge-framework-demotes-content-taxonomies-to-defaults.md) performs one binding move: a closed taxonomy becomes a guarded default rather than a certified universal, which is quantification over the choice rather than assertion of it.

## Stipulated vocabulary is the hard binding case

Vocabulary that Commonplace stipulates can look theoretical because its meaning is stable. Stability is not reach. Replace the local term with a general description and ask whether a substantive, contestable distinction remains. If removing the selected label removes the intended contribution, the definition records Commonplace machinery and belongs in reference. The definition audit applies this binding test to vocabulary.

## Open forks

- Are definitions supporting apparatus for theories rather than beliefs themselves, and if so, what minimum theoretical dependence justifies their presence in `kb/notes/`?
- Externally imposed constraints survive the belief/choice decomposition of requirements. Are they a third content kind, a species of belief about the environment, or a boundary condition that belongs with the choices they constrain?
- Which maintenance disposition should each current-state reference artifact use: generation, staleness registration, authored irrecoverable content, or minimization?
- What minimum inference makes a particular observation a substantive existential witness rather than a local report restated with existential grammar?
- Which rationale is required for selective revision, and which belongs only in git history or workshop records?
- Should `knowledge artifact` and `system-definition artifact` survive as convenient authority-family shorthands now that behavioral authority is path-relative?
- Does the generator/cache distinction need a separate cost axis for recoverable-but-worth-retaining content?
- What admits an artifact to the KB at all: a universal theory of answerability, a chosen framework boundary, or collection-specific contracts?
- Is the binding requirement checkable more cheaply than Level B semantic judgment? A proxy such as a Commonplace-specific identifier outside a witness clause creates false positives, so any cheaper check needs its own calibration.
