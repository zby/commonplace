# Working content model

This is the reconstruction for the workshop's governing question. It does not propose a closed artifact taxonomy, but it now has a settled organizing rule.

## The organizing rule: belief and choice

The maintainer's boundary, adopted 2026-08-22, is that **`kb/notes/` holds beliefs and `kb/reference/` holds choices**. Notes are about the design space — what is true, or believed true, about how systems of this kind can work. Reference is about the selections Commonplace made within that space.

This is the content-kind axis promoted to the collection boundary. It replaces the earlier framing, in which collection membership was a communicative-profile question decoupled from what the content is.

**Why this split survives where derived/committed failed.** The workshop's first attempt split content into derived and committed, and it failed: Commonplace can produce an ampliative theory not entailed by its sources, so producing it is a commitment while what it asserts stays truth-apt. That objection does not reach belief/choice, because belief/choice asks what the content *is*, not how it was produced. The ampliative theory is a belief; that its production was a commitment is recorded on the production-relation axis. The earlier split failed by conflating two axes that this one keeps apart.

**What it predicts that a profile label does not.** Beliefs and choices have different revision rules. A belief is revised against evidence — rewritten in place, holistically, and the superseded version has no standing. A choice is superseded rather than corrected, and the earlier choice remains a fact about what this system once committed to. That is why ADR chains are append-only while notes get holistic rework. The theoretical/descriptive labels had to state this as a separate convention; belief/choice derives it.

## “What is stored?” has several attachment levels

A whole file is often the wrong unit. One artifact can carry a belief, a requirement, a residual selection, historical rationale, and executable instruction. The model asks four independent questions at the level each answer attaches to:

| Question | Primary unit | What it changes |
|---|---|---|
| Content kind — belief or residual choice | Material proposition or operative region | Truth and choice conditions; and, applied to an artifact's dominant contribution, which collection owns it |
| Production relation | Material proposition or operative region | Refresh, re-derivation, or supersession obligations |
| Behavioral authority | Consumption path | Advice, instruction, enforcement, routing, evaluation, or learning force |
| Collection prototype | Collection, at creation time only | Which existing contract a new collection starts from |

Recoverability adds a fifth maintenance question without replacing these four: can another retained surface faithfully regenerate this content, and if so, at what cost and with what warrant?

The fourth question was previously called communicative profile and was listed first, as though a live classifier. It is being retired in favour of collection prototypes — see [the retirement task](./tasks/retire-profiles-for-collection-prototypes.md) — because nothing is inherited from a profile at use time. Every `COLLECTION.md` restates its contract in full locally, so the label carries no force once the collection exists.

**The unit mismatch is real and unresolved by the rule.** Content kind attaches to a proposition or region; a collection boundary is necessarily file-level. The boundary can therefore track only an artifact's dominant contribution, and a genuinely mixed artifact has to be split rather than filed. The rule says where each proposition belongs, not how to avoid splitting.

## Candidate retained payload

### Beliefs

The KB retains truth-apt propositions it uses for reasoning. Their warrant can come from sources, observations, derivation, testing, or Commonplace's own ampliative conjecture and synthesis. Being authored here rather than copied from a source does not turn a belief into a choice.

Beliefs need their modality, evidence-earned scope, counterevidence, and revision conditions. A conjecture can be retained as a belief without being treated as accepted.

**Beliefs about a particular are still beliefs.** An observation about Commonplace itself — a traced episode, a cost measurement, an audit of what some mechanism actually achieved — is truth-apt and records no choice. The rule therefore sends it to `kb/notes/`, and existing practice already agrees: `kb/notes/evidence/` holds seven such artifacts, five of them observations of this repository — a six-path addressability audit, a note-history trace, review-bundle cost telemetry, three simplification passes of one article, and two rewrites of one note. The outgoing profile rule could not justify that directory, since by communicative profile an account of this repo is descriptive and belongs in reference. Belief/choice justifies it exactly.

The same class is currently split across both collections. `kb/reference/` holds `tag-readme-trace-observed-causal-connection.md`, `harness-sub-agent-model-selection-regression.md`, and `commonplace-as-a-reflective-system.md` — particular, truth-apt, recording no selection. Under the rule these are misfiled. They are a **candidate** list for relocation, not an authorization; the harness regression in particular may be better read as a source observation about an external tool than as a Commonplace belief.

### Residual choices

A functioning system must sometimes select one of several options that its beliefs, requirements, and inherited constraints leave live. The residual selection is a choice even when the alternatives have unequal consequences and even when substantial reasoning narrows them.

A proposal can hold candidate selections, but proposal status does not make them operative. Adoption, installation, or another commitment path does that. The retained payload may need the selected option, applicable constraints, rejected live alternatives, and trade-offs that implementation cannot recover.

### Requirements and inherited constraints

These constrain the choice surface. The belief/choice rule does not dissolve the category, but it does decompose most instances: a requirement typically pairs a belief that supports it with a commitment that adopts it. "Notes must be self-sufficient" is a choice Commonplace made; "self-sufficient notes cost less to traverse" is the belief it rests on. Split that way, each half has a home and the pairing is carried by a `rests-on` edge.

What resists the decomposition is a requirement whose force comes from outside — a platform limit, a consumer's fixed interface, an inherited constraint nobody here selected. That is neither a belief Commonplace formed nor a choice it made, and it is the residue the workshop still has to place. Whether it is one kind or several remains open.

### Descriptions and caches

Faithful current-state descriptions may be derivable from implementation and therefore dispensable in principle. They can still earn retention by saving context, latency, inspection effort, or recomputation. Their risk is synchronization failure: a cache that looks canonical can conceal its own staleness.

**This class has no home under the rule, and that is the finding rather than a defect.** A description of what the shipped system currently does is neither a belief about the design space nor a choice made within it. It is derived state — the consequence of choices already recorded elsewhere. `kb/reference/` currently holds a substantial block of it: `architecture.md`, `lib-modules.md`, `commands.md`, `storage-architecture.md`, `freshness-schemas.md`, and the code-architecture halves of `review-architecture.md` and `freshness-architecture.md`.

Two independent criteria converge on this same set. The recovery test marks it as cache, because the running system can regenerate it. The belief/choice rule marks it as homeless, because it asserts neither kind of content. Convergence from two directions is reasonable evidence the set is real, and it points at a disposition the workshop can now recommend: generate this content, register it for staleness against the code it describes, or minimize it — rather than authoring and maintaining it as prose. Deciding which of the three, per artifact, is downstream work.

Historical descriptions are not current-state caches. They answer to what existed or what was decided at a stated time and may preserve facts the present system no longer exposes. Where they record a decision they are choices; where they record an observation they are beliefs about a particular.

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

The primary test is one question asked of the artifact's dominant contribution: **would this still be true if Commonplace had chosen differently?** A belief survives the counterfactual; a choice does not, because the choice is what the counterfactual varies.

- **Notes:** the content is truth-apt and its truth does not depend on what Commonplace selected. This covers general claims about the design space and particular observations about this system alike.
- **Reference:** the content is true because Commonplace adopted, implemented, or currently exposes it. Choices, their live alternatives, and the rationale that makes them defensible.
- **Instructions:** the content directs an operator's next action, including defaults, ordering, and stopping conditions. An instruction is a choice with an imperative surface; it sits here rather than in reference because its consumer executes it.
- **Sources:** the artifact's principal obligation is fidelity to captured external material rather than a claim Commonplace now owns.
- **Work:** the governing question or disposition is unresolved, so the artifact's value will be consumed by completing the investigation.

**Subject matter is not content kind.** A note may discuss machinery at length and remain a belief, if what it asserts about that machinery would hold for any system built the same way. A reference artifact may contain belief propositions without becoming a note. The test runs on what makes the content hold, never on what it is about — which is the error that placed a definition of chosen collection machinery in the theoretical collection.

## Publishability: a choice named in a theory must be a bound variable

The boundary earns its keep twice, and maintenance is only the first way. The second is that notes get published. `kb/articles/` distils them for "highly technical readers with no KB context" — a reader who has none of Commonplace's choices.

That sets a hard condition on how a note may mention a choice. A **free** occurrence — a claim whose truth conditions silently depend on a selection Commonplace made, while the sentence presents as general — does not survive publication. Stripped of the local context that made it true, it reads as either false or empty. A note asserting that a collection's contract file declares its quality goal is not stating a mechanism; it is reporting a Commonplace choice in a general voice.

A note may name a choice only under a quantifier:

- **Universally bound.** "For any system that localizes authoring contracts per subtree, X follows." The choice ranges over the design space and Commonplace's selection is one value. This is the shape that transfers.
- **Existentially bound, as witness.** "At least one system does X, so X is feasible and these consequences are observed." The particular is evidence for a claim about the space, not the subject of the claim.

**This is stronger than the counterfactual test because it comes with a repair.** Failing the counterfactual does not by itself mean "move it to reference." It means the claim has a free choice-variable, and there are two dispositions: bind the variable and the note stays, or move the proposition to reference because it was only ever a report of what was selected. Binding is usually the better outcome, since it *adds* reach rather than relocating content.

That is the same constraint as the collection's stated quality goal. A claim with a free choice-variable has no [explanatory-reach](../../notes/first-principles-reasoning-selects-for-explanatory-reach-over.md) beyond the system that made the choice; binding the variable is what creates reach. Publishability, reach, and the belief/choice boundary are one requirement seen three ways.

**The test cuts one way.** Reference cannot fail it, because reference is not published as theory — reporting Commonplace's selections in a local voice is exactly its job. So publishability is a gate specific to `kb/notes/`, not a general placement criterion.

Two existing notes supply the halves. [A framework rule with a boundary-preserving rival is not inherited](../../notes/a-framework-rule-with-a-boundary-preserving-rival-is-not-inherited.md) detects the defect: if a rival design preserves the invariants while dropping the rule, the rule was a choice. [A universal knowledge framework demotes content taxonomies to defaults](../../notes/a-universal-knowledge-framework-demotes-content-taxonomies-to-defaults.md) performs one binding move: a closed taxonomy becomes a guarded default rather than a certified universal, which is quantification over the choice rather than assertion of it.

## Residual sharpness of the counterfactual test

**The counterfactual test has a known soft spot.** Vocabulary that Commonplace stipulates can look belief-shaped because its meaning is stable. Stability is not independence: a stipulated term is true by choice, and would simply not exist had the choice gone the other way. The definition audit's theory-versus-machinery test is this same question applied to definitions.

## Open forks

- Are definitions supporting apparatus for theories rather than beliefs themselves, and if so, what minimum theoretical dependence justifies their presence in `kb/notes/`?
- Externally imposed constraints survive the belief/choice decomposition of requirements. Are they a third content kind, a species of belief about the environment, or a boundary condition that belongs with the choices they constrain?
- Current-state descriptions have no home under the rule. Is generation, staleness registration, or minimization the right disposition, and does the answer vary by artifact or hold for the class?
- Does the collection boundary need an exception for particular observations, or does `kb/notes/evidence/` already show the rule works unchanged?
- Which rationale is required for selective revision, and which belongs only in git history or workshop records?
- Should `knowledge artifact` and `system-definition artifact` survive as convenient authority-family shorthands now that behavioral authority is path-relative?
- Does the generator/cache distinction need a separate cost axis for recoverable-but-worth-retaining content?
- What admits an artifact to the KB at all: a universal theory of answerability, a chosen framework boundary, or collection-specific contracts?
- Is the binding requirement checkable? A free choice-variable is a semantic property, so detection is a Level B judgment — but a cheaper proxy may exist, such as a note naming a Commonplace-specific identifier outside a witness clause.
- Do existing notes pass? A sweep for free choice-variables across `kb/notes/` would test whether the boundary describes current practice or prescribes a migration.

