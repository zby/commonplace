<!-- copied from the gitignored kb/reports tree; original frontmatter retained below as data -->

```yaml
description: "Full improvement pass over Reaching unformalized improvements needs a pre-formal stage somewhere in the loop"
type: kb/reports/types/full-pass-report.md
source: kb/notes/unformalized-improvements-need-a-pre-formal-stage-in-the-loop.md
source_capture: source.txt
source_sha256: 6b321f0ff1093175666f587ec5c018d80feb05deab8b6c1a78dbd0c4b32e4aa6
pass_id: 20260826T154716Z-3fa27b
disposition: keep
merge_target: null
merge_target_capture: null
merge_target_title: null
merge_target_sha256: null
resolution: not-required
resolved_at: null
resolution_authority: null
resolution_summary: null
resolution_rationale: null
resulting_paths: []
```

# Full Pass: Reaching unformalized improvements needs a pre-formal stage somewhere in the loop

**Target:** `kb/notes/unformalized-improvements-need-a-pre-formal-stage-in-the-loop.md`
**Reports used:** compression bundle, critique-note, composition-friction-gate, premise-decomposition-gate, catalog review bundles (`accessibility`, `complexity`, `frontmatter`, `prose`, `semantic`, `sentence`, `structural`), connect

## Warranted contribution

**Collection/type fit:** FITS — the artifact makes a transferable claim about representational admission, translation, and warrant in improvement-loop design. The Gödel-machine and Commonplace material is scoped as evidence or application rather than as a description of one system, so a substantive design-space claim remains after the named systems are bounded.

**Reader and prior:** The intended reader is an agent or maintainer deciding how an agent-operated KB or reflective improvement loop should admit, translate, evaluate, and retain candidate theories. This audience comes from the repository purpose and the `kb/notes/` collection contract, which are authoritative fallback inputs because the artifact states no narrower intended reader. The existing KB already explains search/evaluation/retention, oracle-domain limits, semantic-work relocation, fixed update spaces, cross-form coverage, and the difference between exact implementation and objective fit. Connect found no existing note that owns the narrower combination of a formal gate's direct-admission limit, its warrant limit, and the effect of upstream translation on those two limits.

**Update:** Formal-only gates have a direct-admission limit distinct from their warrant limit: upstream translation can put a theory into the admitted language, but neither admission nor an internal proof establishes that the surrogate preserves an unsettled source theory or fits the world.

**Why a generic treatment would not supply it:** A generic “formal gates check formal candidates” account collapses three different questions: whether the gate can read the submitted representation, whether some upstream component can translate the same semantic candidate into that representation, and what the gate's oracle warrants after admission. The artifact's distinctive delta is that translation can restore loop-level reach while relocating unresolved semantic choices and leaving correspondence outside the downstream proof.

**Warrant:** The incumbent's Gödel-machine case supports the difference between an out-of-language conjecture and an in-language rewrite that lacks a proof. Its translation section supports the narrower claim that producing one determinate surrogate from an unsettled theory requires semantic choices and that proof inside the surrogate does not validate the source-to-surrogate mapping. The scheduler example and linked formal-system cases support the separation between internal validity and world-facing fit, although the DiscoverPhysics wording needs to be narrowed to its retained evidence. Critique partially lands against the incumbent's universal stage thesis, and premise decomposition GLOBAL-defeats the claims that concept stabilization must precede every formal representation and that translation must instantiate a rejection-capable pre-formal stage. Those counterexamples do not erase the admission/warrant distinction: they show that a formal family, partial formalization, or conjecture-and-counterexample loop can carry revision after formal representation. Compression finds a clear contribution but identifies the “relaxed Gödel machine” label as a competing thesis and repeated correspondence explanations as context cost. Catalog semantic gates defend several boundaries and the explanatory mechanism, so their positive findings remain alongside the stronger counterexamples rather than overruling them.

## Disposition

**keep (reframe)** — reframe — the title overreaches in logical scope and category: the artifact warrants distinct direct-admission and warrant limits, not the universal necessity of a pre-formal criticism stage. A formal conjecture-and-counterexample process can stabilize concepts after a formal representation already exists, so no body qualifier can rescue the title's “needs a pre-formal stage” assertion.

## Body edits

| Location | Source method(s) | Finding | Action | Rationale |
|---|---|---|---|---|
| Note-level title, description, and opening thesis | warranted-contribution comparison; critique-note; premise-decomposition GLOBAL findings | The universal title is defeated, while the artifact supports a narrower distinction between direct admission, upstream translation, and post-admission warrant. | Reframe first: retitle to “Formal-only gates have distinct admission and warrant limits,” replace the description, and rewrite the opening so it states the selected update and defines a formal-only gate by its admitted input language. | This surfaces the strongest warranted contribution instead of preserving a false architectural necessity through qualifications. |
| Opening scope and terminology | accessibility/undefined-terms; accessibility/unidentified-references | `representational form`, `codification`, `reflection`, `theory-mediated learning`, Commonplace, and Lean are not all locally glossed or category-identified. | Give necessary active vocabulary a short inline gloss; identify Commonplace as this KB/framework and Lean as a proof assistant if those examples remain. Remove optional terms whose linked mechanisms are no longer needed. | This makes the reframed update usable without forcing the reader through links and avoids adding explanatory branches merely to preserve terminology. |
| General translation section and Gödel-machine section | structural/general-before-specific; critique-note; compression/core-claim-obscured | The specific Gödel case precedes the general distinction, and the translation argument treats interpretive choice as necessarily adversarial criticism and rejection. | Put the general admission/translation/warrant distinction first. State that translation may restore loop-level reach; one determinate surrogate fixes semantic choices upstream, while a formal family or conjecture-and-counterexample process can preserve and revise alternatives after formal representation. Present the Gödel machine afterward as the fixed proof-gated limiting case. | The sequence then serves the selected update and answers the strongest critique without claiming that every translation is a criticism stage. |
| `## What the stage does, and what makes it cheap` | compression/branch-bloat; critique-note; accessibility/undefined-terms | Reflection and theory-mediated-learning benefits branch away from the admission/warrant distinction, and “prototype” standing is attributed too strongly to natural language. | Recast as a compact comparison of revisable candidate surfaces. Keep the useful governance point that authority, coupling, sunk work, and rollback cost determine disposability; state that natural language is one surface and that partial or lightweight formal representations can serve the same revision role. Remove the optional reflection and sample-efficiency branch. | This preserves the real boundary while removing the representation-specific necessity defeated by the counterexamples. |
| `## The relaxed Gödel machine` | compression/branch-bloat; critique-note | The coinage creates a second conceptual center and suggests an architectural family relation stronger than the evidence supports. | Remove the `relaxed Gödel machine` name. Retain Commonplace only as one compact worked example of natural-language criticism followed by codification, and separate that example from the general proof-versus-criticism comparison. | The application supports the update, but the name and its disclaimers do not earn their context cost. |
| Proof/correspondence discussion across translation, Commonplace, and scheduler sections | compression/marginal-value-redundancy; critique-note; semantic/grounding-alignment; prose/confidence-miscalibration | The internal-proof/correspondence distinction is stated three times, and the DiscoverPhysics clause overstates the retained ingest's support for separate scoring. | State the abstract limit once in the translation section. Let the later comparison add only the different warrant targets and let the scheduler example add only the model/world consequence. Narrow DiscoverPhysics to the supported claim that the benchmark requires both prose and implementation and reports an accuracy/explanation dissociation, or omit it. | This protects the selected update's warrant while removing circular repetition and unsupported empirical strength. |
| `## Failure in the world reopens concepts, not only parameters` | critique-note; compression/detail-overhang | Whether shared-resource load changes a concept or a parameter depends on the existing model; the current prose treats one representation-relative classification as unconditional. | Qualify the example relative to a fixed-capacity model. Distinguish revising an existing conditioned parameter, extending a precise symbolic model with a new dependency, and reopening an unsettled interpretation before rebuilding. Compress the two external cases. | The example then demonstrates correspondence and repair alternatives without reintroducing the defeated natural-language necessity. |
| `## Cheap formalization shortens the stage for settled concepts` | critique-note; compression/branch-bloat; semantic/load-bearing-qualifiers | Cheap formal iteration can itself participate in concept stabilization in bounded domains, so the current claim that cost can never remove the pre-formal stage is too strong. | Rename the section around which cost falls. Separate translation, artifact construction, proof generation, checking, and world evidence. State conditionally that cheaper formal iteration can move revision into formal representations, while one-shot translation and world correspondence remain separate obligations. | This preserves the useful cost decomposition without reviving the refuted title claim. |
| Dense comparison and example sentences | sentence/clause-packing | Five sentences combine several mechanisms, comparison arms, or examples. | Split the Gödel admission example, Commonplace lifecycle/example, proof-versus-criticism errors, external cases, and formalization-cost decomposition so each sentence carries one main point. | This lowers working-memory load while leaving the substantive packet decisions unchanged. |
| Relevant Notes footer | complexity/connection-inflation; connect | Three entries repeat inline roles, and the `context` label on the bitter-lesson portfolio edge is not authorized by the notes collection contract. | Remove footer entries whose evidentiary role is already inline; remove or relabel the unauthorized `context` edge. Add only the strongest distinct routes needed by the reframed claim, especially semantic-work relocation and fixed-update-space limits. | The footer should improve traversal for the selected update rather than repeat its proof or spray topical links. |

## Routed attention (composition-friction-gate and premise-decomposition-gate — not auto-resolved)

**Composition friction — filter verdict:** SURVIVES

**Composition friction — thinnest joints:**

1. **“An improvement whose concepts are not yet fixed enough to formalize is reachable only if some stage can criticize, revise, and reject it before it has a formal representation.”** — UNSUPPORTED — Being not yet formalizable establishes that something must change before faithful formalization, but it does not establish a distinct stage equipped with all three operations. The note does not exclude refinement through partial symbolic models, experiment-driven model revision, or candidate generation that yields a stabilized concept before submission.
2. **“The translator must decide what the prose commits to, resolve ambiguity, choose a boundary, and often revise the claim — pre-formal criticism, relocated upstream.”** — UNSUPPORTED — Interpretive choice establishes that translation is not transcription, but it does not establish adversarial criticism or a capacity to reject the candidate. A translator can silently choose one surrogate among several without performing the rejection-capable stage the central claim requires.
3. **“But ‘capacity depends on what another process is doing’ changes the concept, not its value.”** — UNSUPPORTED — The example does not fix a representation sharply enough to force that distinction. Another process could require a new causal variable or functional relation, but it could instead change the value of an already time-varying or load-conditioned effective-capacity parameter.
4. **“Formalization cost has parts — translating concepts into a model, building the artifact, generating a proof, checking it — and when the last three fall, formal models enter the prototype stage earlier and rival specifications become easy to compare.”** — THIN — Lower construction, proof-generation, and checking costs support earlier executable artifacts once translations exist. They do not make rival specifications easy to compare when correspondence to the source theory, comparison criteria, or world-facing evidence remain costly.
5. **“What natural language contributes is narrower: it exposes unsettled commitments before a faithful formalization exists.”** — THIN — Natural language can state commitments before formalization, but the preceding discussion does not show that it exposes rather than conceals them, or identify what exposure mechanism is unavailable to diagrams, partial formalisms, or other nonbinding representations.

**Composition friction — For the human:** Look first at the jump from unavoidable interpretive choices during translation to an architecturally necessary, rejection-capable criticism stage; that missing concretization supports both the necessity and relocation claims.

**Premise decomposition — premises:**

1. **For an improvement that begins with unsettled concepts, mere reachability requires a pre-formal component able to criticize, revise, and reject it; direct generation and later formal selection cannot suffice.** — DEFEATED — Consider a scheduler-model grammar that permits capacity to depend on any observed load signal: a generator enumerates formal models, and an exact trace oracle retains the model in which another process's load predicts failures. The initially unsettled “shared resource” improvement is reached without any component criticizing, revising, or rejecting it before formal candidates exist; rejection occurs only after generation. — GLOBAL — instance
2. **An externally interpreted theory's concept boundaries must stabilize before any formal representation can carry those concepts in a form that supports criticism and revision.** — DEFEATED — In Angluin's L* learner, the latent state partition of a black-box system is unsettled while the learner repeatedly proposes formal automata and uses counterexamples to split and revise the represented state classes. A person can read each automaton as a nonbinding behavioral theory of the system, yet concept stabilization happens through a sequence of already-formal conjectures. — GLOBAL — instance
3. **To count as reaching an unformalized improvement, the loop must preserve the identity of the prose-born candidate through translation; independently discovering an extensionally equivalent formal theory does not count.** — DOUBTFUL — A causal-structure search over scheduler traces can introduce an unnamed latent common cause and thereby recover the predictive content of “failures come from an unrepresented shared resource” without ever consuming that prose candidate. Whether this is the same improvement or a replacement depends on a candidate-identity rule the note leaves open explicitly. — GLOBAL — instance
4. **Every route that translates one unsettled natural-language theory into formal candidate space must resolve its ambiguity through a pre-formal stage that can reject the source, rather than preserve the ambiguity for formal evaluation.** — DEFEATED — A translator can mechanically emit a formal disjunction of `fixed_capacity`, `time_varying_capacity`, and `capacity_dependent_on_other_load`, rejecting none; a trace checker can then eliminate alternatives after the disjunction already has assigned symbolic consequences. The interpretive choice is deferred into formal candidate selection, so translation need not instantiate the required pre-formal rejection-capable stage. — GLOBAL — instance
5. **A gate whose input language is exclusively programs and proofs cannot directly admit a natural-language theory that has no encoding in that language.** — HOLDS — Treating the text as an uninterpreted byte string admits the string but not its theoretical content; giving the gate a human or language-model interpreter changes the gate, while giving it translated axioms supplies a formal surrogate rather than the unrepresented theory.
6. **Turning a genuinely ambiguous natural-language theory into one single, determinate formal surrogate necessarily adds semantic choices that the source does not entail.** — HOLDS — A controlled language with fixed semantics would avoid the ambiguity but falls outside the premise, and a disjunction or family of translations postpones the choice rather than producing one determinate surrogate; no case was found in which one fixed surrogate preserved mutually incompatible source readings without selecting among them.
7. **A proof or check of consequences inside a formal surrogate does not by itself establish that the surrogate faithfully captures the externally interpreted source theory or the world it describes.** — HOLDS — Exhaustive checking over a finite observation interface can establish behavioral equivalence on that interface, but the interface, measurements, and adequacy criterion already encode correspondence commitments; the internal proof remains conditional on those mappings rather than proving them from the external theory alone.
8. **Even when artifact construction, proof generation, and checking become cheap, an unsettled theory's concepts cannot be settled by a formal conjecture-and-counterexample cycle, so cheap formalization can shorten but never eliminate the pre-formal interval.** — DEFEATED — An exact active-automata-learning setup cheaply constructs a formal state-machine conjecture, receives a counterexample from the target system, and refines the state partition until the behavioral concepts stabilize; all criticism and revision occur after the first formal representation. Cheap formal iteration is the concept-settling stage in this bounded case, not merely a downstream consumer of already settled concepts. — GLOBAL — instance

Premises 1, 2, 3, 4, and 8 carry GLOBAL routed attention. Their defeats inform the note-level keep (reframe) Disposition; they do not authorize any passage edit by themselves.

**Premise decomposition — For the human:** Look first at premise 2: formal conjecture-and-counterexample learning provides a scoped case in which externally read concepts stabilize through already-formal theories, so the claimed temporal boundary needs a narrower domain than “unsettled concepts.”

## Gate findings

### Accessibility

| Gate | Result | Finding |
|---|---|---|
| jargon-persistence | PASS | Specialized terms occur sparingly rather than persisting as opaque active vocabulary. |
| notation-opacity | PASS | The note does not depend on imported notation or symbols. |
| undefined-terms | FAIL | `representational form` and `codification` are linked without the required first-use gloss; reflection and theory-mediated learning also assume linked-note familiarity. |
| unidentified-references | WARN | Commonplace and Lean appear without category-first identification. |

### Complexity

| Gate | Result | Finding |
|---|---|---|
| claim-to-section-ratio | PASS | The incumbent sections carry distinct support units, although the reframe will retire some of them. |
| connection-inflation | WARN | Three footer entries duplicate relationships already stated inline. |
| could-be-a-paragraph | PASS | The warrant/admission, translation, correspondence, and cost distinctions do not collapse safely to one paragraph. |
| framework-decoration | PASS | The limit and revision distinctions are inferential rather than decorative. |

### Frontmatter

| Gate | Result | Finding |
|---|---|---|
| claim-strength | PASS | The incumbent title is contestable, even though stronger counterexamples defeat it. |
| description-discrimination | PASS | The incumbent description adds retrieval detail beyond the title. |
| title-as-claim | PASS | The incumbent H1 is truth-apt. |
| title-body-alignment | PASS | The body consistently argues the incumbent title; critique and premise decomposition challenge that shared claim rather than an alignment defect. |
| title-composability | PASS | The incumbent title composes grammatically as a linked premise. |

### Prose

| Gate | Result | Finding |
|---|---|---|
| anthropomorphic-framing | PASS | Gates, critics, and theories are described in functional rather than mentalistic terms. |
| bridge-paragraph-duplication | PASS | Section endings do not duplicate the next opening. |
| confidence-miscalibration | WARN | The DiscoverPhysics accuracy/explanation claim is stronger than the retained abstract-page ingest warrants. |
| orphan-references | PASS | External references are named and linked, despite the separate confidence problem. |
| proportion-mismatch | PASS | No section dominates under this lens; compression independently finds the coinage to be branch bloat. |
| pseudo-formalism | PASS | No decorative notation or quasi-formal scaffold appears. |
| redundant-restatement | PASS | Section openings add new work, while compression separately flags repeated correspondence material across sections. |
| source-residue | PASS | Named systems are presented as cases rather than leaked into the general claim. |
| unbridged-cross-domain | PASS | The Eigenius and DiscoverPhysics transfers state the intended shared distinction. |

### Semantic

| Gate | Result | Finding |
|---|---|---|
| completeness-boundary-cases | PASS | The catalog lens found the incumbent framework to cover its stated cases; premise decomposition supplies stronger formal-revision counterexamples. |
| conceptual-role-conflation | PASS | Systems, translators, gates, and applications are assigned recoverable roles. |
| epistemic-status-blur | PASS | Derived claims, cases, and open questions remain distinguishable. |
| explanatory-reach | PASS | The note states a mechanism rather than only a pattern. |
| grounding-alignment | WARN | DiscoverPhysics does not directly support the claimed independent scoring detail. |
| internal-consistency | PASS | The incumbent distinctions remain internally stable. |
| load-bearing-qualifiers | WARN | The description says `proof gate` while the body argues from formal-only admission more broadly. |
| underspecified-assertions | PASS | Nearby prose resolves the catalog lens's materially relevant readings. |
| unearned-generality | PASS | The catalog lens accepts the abstraction; the adversarial methods separately defeat the universal stage requirement. |
| unwarranted-scope | PASS | The catalog lens accepts the stated scope; the stronger premise counterexamples still require the title reframe. |

### Sentence

| Gate | Result | Finding |
|---|---|---|
| clause-packing | WARN | Five sentences combine multiple mechanisms, comparison arms, or examples. |
| concept-attribution | PASS | Checked linked concepts match their local use. |
| framing-mismatch | PASS | The catalog lens found the incumbent framing internally aligned. |
| misleading-link-text | PASS | Five inspected targets matched their anchors; eleven listed targets remained outside the inspection cap. |
| parsing-ambiguity | PASS | No materially competing parse was found. |
| stock-phrases | PASS | Emphatic transitions carry argumentative work. |

### Structural

| Gate | Result | Finding |
|---|---|---|
| bullet-capitalization | PASS | Open-question and footer bullets begin correctly. |
| compound-bullet | PASS | Footer bullets remain single-purpose. |
| general-before-specific | WARN | The Gödel-machine example precedes the general translation rule it exemplifies. |

## Connection candidates

- `mechanism` → `kb/notes/semantic-work-can-be-relocated-but-not-eliminated.md` — supplies the general placement mechanism behind upstream semantic choices.
- `grounds` → `kb/notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md` — explains why optimization inside an admitted representation cannot repair a still-excluded distinction or mapping.
- `extends` → `kb/notes/moving-the-interpretation-enforcement-boundary-requires-coverage.md` — develops the source-to-surrogate correspondence issue into cross-form coverage requirements.
- `grounds` → `kb/notes/exact-implementation-does-not-validate-a-requirement.md` — separates local formal correctness from the upstream proxy-to-world link.
- `grounds` → `kb/notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md` — supplies the substrate conditions under which unformalized theories can be retained and interpreted.
- `extends` → `kb/notes/theory-and-methodology-form-a-two-layer-execution-system.md` — develops the downstream architecture where revisable theory remains beside a narrower checked path.
- `operationalized-from` → `kb/instructions/invert-solution-shaped-requests.md` — gives an ordered procedural instance of criticism before commitment.

## Proposed revision shape

1. Open with the reframe: formal-only gates have distinct direct-admission and warrant limits; translation can restore loop-level reach without proving fidelity.
2. Explain the general translation cases before the Gödel-machine example: one surrogate fixes choices upstream, while a formal family can preserve revision after formal representation.
3. Treat natural language as one low-authority candidate surface rather than a necessary stage; keep governance and coupling as the real determinants of disposability.
4. Use the Gödel machine as the fixed proof-gated limiting case and Commonplace as one compact criticism-to-codification example, without the relaxed-machine coinage.
5. State the internal-proof/correspondence limit once, then use a representation-relative scheduler example to distinguish parameter revision, symbolic model extension, and reopening an unsettled interpretation.
6. Close with a conditional cost decomposition, compact open questions, and a reduced footer containing only distinct traversal routes.

## Open items

- **Concurrency interruption resolved for the resumed closing cycle:** after step 9 first completed, the note was byte-stable at SHA-256 `a0f1c7f0cb9803c42ad8fd6043dca970d8213d747e230024a5f68fc44be749c3`, and review jobs 8407–8414 plus the first closing compression run read those bytes. At 2026-08-26 18:53:34 +02:00 another actor restored the live target to the pass-start SHA-256 `6b321f0ff1093175666f587ec5c018d80feb05deab8b6c1a78dbd0c4b32e4aa6`; that partial closing evidence remains invalid. The user then directed the pass to continue. The packet guard reported every input matching, and the preserved post-copyedit text in `closing/interrupted-final.txt` was reapplied byte-for-byte, restoring SHA-256 `a0f1c7f0cb9803c42ad8fd6043dca970d8213d747e230024a5f68fc44be749c3` without reopening the copyedit. Fresh direct reviewers and new requested-mode jobs 8415–8422 then completed against that one version.
- **Required reframe follow-up after this pass:** rename the live note with `commonplace-relocate-note` to a slug matching the new claim, such as `kb/notes/formal-only-gates-have-distinct-admission-and-warrant-limits.md`. Then update the visible link text and table summary in `kb/notes/the-bitter-lesson-defense-portfolio-has-one-load-bearing-member.md`, the only current library citer, and reconcile whether that row still relies on the defeated assertion that unsettled concepts necessarily need a pre-formal stage. Leave this retained packet's `source`, frontmatter description, H1, displayed Target, and historical directory untouched.
- Closing critique and composition friction converge on one unresolved identity boundary: the note shows that translation can produce an admitted surrogate, but it does not give a criterion for when that surrogate preserves the same semantic candidate rather than replacing it. This does not defeat the gate-relative admission/warrant distinction; it limits the stronger claim that translation restores semantic reach.
- Closing compression still finds repeated correspondence/world-fit material and optional Commonplace, prototype-economics, and external-case detail. A future pass could consolidate those branches around one canonical statement and one operational example; this closing cycle does not authorize another edit round.
- Accessibility's unidentified-reference gate fails because the first mention of Commonplace does not identify it as this KB/framework. Sentence clause-packing warns on the 41-word DiscoverPhysics sentence. Both are bounded clarity repairs for a later pass.
- The premise report's Angluin L* example is routed attention, not grounded library evidence for an automatic edit. The revision can state the self-contained formal-family and conjecture/counterexample countercases; retaining the named external example would require source grounding.
- The misleading-link-text gate inspected five targets and left eleven named targets outside its cap; no defect was established in the unchecked set.
- Connection candidates remain discovery suggestions. Add only routes that materially improve traversal for the selected admission/warrant distinction.
- Closing connect still flags a possible future split between the core admission/warrant theory and its broader cheap-formalization objection role. The current artifact remains coherent, so no split is proposed in this pass.
- The unrelated concurrent edit to `kb/notes/naur-equates-machine-execution-with-formulated-criteria.md` is outside this pass and must remain untouched.

## Resolution

**Status:** not-required
**Resolved at:** —
**Authority:** —
**Outcome:** —
**Rationale:** —
**Resulting paths:** —

## Closing cycle

**Pass ID:** 20260826T154716Z-3fa27b
**Final note SHA-256:** `a0f1c7f0cb9803c42ad8fd6043dca970d8213d747e230024a5f68fc44be749c3`

| Assay | Closing result | Residual routed to Open items |
|---|---|---|
| compression bundle | WARN — the core claim is clear, but correspondence/world-fit repeats and the prototype, Commonplace, and external-case branches retain avoidable context cost; two consolidation opportunities surfaced | yes |
| critique-note | REPORT; attack partially lands — admission is clearly gate-relative, but the note still blurs a larger-loop candidate with a candidate directly evaluable by the gate | yes |
| composition-friction-gate | SURVIVES; two UNSUPPORTED and three THIN joints, led by whether surrogate admission restores the same semantic candidate | yes |
| premise-decomposition-gate | Seven premises HOLDS; no DOUBTFUL or DEFEATED premise and no GLOBAL defeat | no |
| accessibility / complexity / frontmatter / prose / semantic / sentence / structural | accessibility 3 PASS, 1 FAIL; complexity 4 PASS; frontmatter 5 PASS; prose 9 PASS; semantic 10 PASS; sentence 5 PASS, 1 WARN; structural 3 PASS | yes |
| connect | Five outbound, two bidirectional, and two reverse-edge candidates; stale citer wording and a possible future split surfaced | yes |
| warranted contribution | preserved — the final text states and supports the selected gate-relative admission/warrant distinction without restoring the rejected universal pre-formal-stage thesis; candidate identity remains an explicit limit on the translation-reach clause | yes |
