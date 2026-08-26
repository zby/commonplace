<!-- copied from the gitignored kb/reports tree; original frontmatter retained below as data -->

```yaml
description: "Full improvement pass over Naur binds program theory to humans through the premise that machines only follow rules"
type: kb/reports/types/full-pass-report.md
source: kb/notes/naur-binds-theory-to-humans-via-premise-that-machines-follow-rules.md
source_capture: source.txt
source_sha256: 1c3e45c0488cacc59a52a1e4bd8ed6383ad13211d13e08cc139d15d808d1ca87
pass_id: 20260826T140020Z-7c9e
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

# Pass: Naur binds program theory to humans through the premise that machines only follow rules

**Target:** `kb/notes/naur-binds-theory-to-humans-via-premise-that-machines-follow-rules.md`
**Reports used:** compression bundle, critique-note, composition-friction-gate, premise-decomposition-gate, catalog review bundles (`accessibility`, `complexity`, `frontmatter`, `prose`, `semantic`, `sentence`, `structural`), connect

## Warranted contribution

**Collection/type fit:** FITS — the artifact advances a transferable claim about the logical reach of a program-theory argument and the conditions under which an interpreter-plus-artifact system could answer it. It is neither a procedure nor a description of one deployed system, so it satisfies the theoretical `kb/notes/` collection contract and the `note` type.

**Reader and prior:** The intended reader is an agent or maintainer deciding how program-theory arguments should constrain agent-operated KB architecture, selected by the repository KB purpose and `kb/notes/COLLECTION.md` as authoritative contracts. The existing KB already uses Naur to motivate interpreter-plus-retention and design-rationale claims. Connect found no near-duplicate that isolates the logical gap between rule-inexpressibility and human exclusivity; the closest notes consume the stronger incumbent claim instead.

**Update:** Naur's claim that program theory cannot be expressed as criteria does not by itself entail that only humans can hold it; human exclusivity needs an additional premise excluding every eligible nonhuman theory-holder.

**Why a generic treatment would not supply it:** A generic summary of *Programming as Theory Building* joins inexpressibility, human possession, and failed artifact transfer as one position. This artifact separates those propositions, identifies the extra exclusion needed for the human-only inference, and preserves program-specific acquisition, premise availability, and cross-occasion reliability as conditions without claiming that a current LLM meets them. The source ingest and adjacent KB notes do not already own that separation.

**Warrant:** The retained source extracts separately state that the relevant similarity criteria cannot be formulated, that program theory is bound to humans, that computing is formal symbol manipulation, and that Naur contrasts humans with machine-like rule-following. Logic supplies the narrow result: inexpressibility alone cannot entail human-only possession unless some additional premise excludes every eligible nonhuman candidate. The source also uses person-bound language beyond the machine/rule contrast, so the packet does not warrant identifying one dichotomy as the sole bridge. The compiler case warrants a bounded failure of the supplied artifact package and motivates acquisition and reliability conditions; it does not establish that personal advice alone repaired the transfer or that every possible retained-rationale route was tested. Critique, semantic review, and the source analysis all leave current LLMs unresolved because learned, non-hand-authored criteria may still be finitely and formally implemented.

## Disposition

**keep (reframe)** — reframe: the title overreaches in specificity and scope by treating the machine-as-rule-follower contrast as the sole bridge and a current trained interpreter as outside it; the warranted claim is that rule-inexpressibility alone does not establish human exclusivity.

## Body edits

| Location | Source method(s) | Finding | Action | Rationale |
|---|---|---|---|---|
| Note-level title, description, and opening thesis | critique-note; semantic/internal-consistency; semantic/underspecified-assertions; prose/confidence-miscalibration | The incumbent title and thesis identify one exhaustive bridge and rely on actual non-formulation where Naur claims possible non-formulability. | Retitle to “Naur's rule-inexpressibility argument does not by itself bind program theory to humans”; rewrite the description and opening around the additional-premise claim. | This is the strongest distinct update the source and logic warrant; it removes the stronger claim that the reports defeat without discarding the note's contribution. |
| First mention of Ryle | accessibility/unidentified-references | “Ryle” is not identified for an external reader. | Identify him inline as the philosopher Gilbert Ryle. | Supplies the minimum source role needed to follow the attribution. |
| “The inexpressibility argument targets formulable rules” | sentence/clause-packing; semantic/internal-consistency | One sentence delays its main restriction behind a three-item list; later prose drifts from “can be formulated” to “anyone formulated.” | Split the capability list from the restriction and use possible formulability consistently. | Makes the source argument readable and protects the modal boundary on which the note turns. |
| “The step to human beings rests on an exhaustive dichotomy” | critique-note; semantic/grounding-alignment; prose/confidence-miscalibration; prose/orphan-references | “Uses everywhere,” “argues nowhere,” “throughout,” and the 1985 causal explanation exceed the retained source support; other person-bound premises may also contribute. | Recast the human/machine passages as one visible exclusion premise in the retained extracts; delete the unsupported historical motive and acknowledge that other person-bound statements are additional premises rather than products of rule-inexpressibility. | Grounds the update in retained text and prevents the reframe from replacing one overclaim with another. |
| “A trained interpreter falls outside the partition” | critique-note; semantic/internal-consistency; semantic/underspecified-assertions; prose/confidence-miscalibration; prose/orphan-references | Learning from examples does not show that a resulting system is outside formal rule determination; the passage conflates human-readable criteria, finite formal specification, and computability. | Replace the section with “A trained interpreter exposes the question but does not settle it.” State that learned criteria can still be formally represented, distinguish the three properties, and treat current LLMs as unresolved rather than as the witness that closes the inference. | Removes the strongest landed attack while preserving the selected update: Naur still needs an additional exclusion premise, but this note need not prove a present implementation escapes it. |
| Compiler-case opening under “What the essay still establishes as conditions” | semantic/grounding-alignment; sentence/clause-packing | The sentence packs setup, outcome, interpretation, and repair, while “only personal advice repaired” is not in the retained extracts. | Split the case into short source-bounded observations: the successor group had extensive artifacts, proposed structure-destroying patches, and the original group recognized and proposed structure-preserving alternatives. | Keeps the evidence that supports the conditions without attributing an unreported repair mechanism. |
| Three conditions | semantic/grounding-alignment; compression/detail-overhang; critique-note | The conditions are useful, but the retained-premises bullet overstates what Naur tested and expands into an adjacent note's full recovery framework. | Preserve all three conditions; make premise availability a conditional requirement on any composite, state that Naur tested one supplied package rather than every rationale design, and compress the adjacent-note gloss. | Retains the artifact's non-generic architectural payoff while aligning each claim with its actual warrant and reducing context cost. |
| Closing paragraph | compression/marginal-value-redundancy | The division-of-labour link restates the just-completed list before the empirical-open/logical-closed contrast. | Move that relationship to `Relevant Notes` and close directly on what remains empirical versus what the argument cannot settle alone. | Sharpens uptake of the selected update without adding another thesis. |

## Routed attention (composition-friction-gate and premise-decomposition-gate — not auto-resolved)

**Composition friction — filter verdict:** SURVIVES

The note's rule-inexpressibility, additional-human-binding-premise, and agnosticism about an interpreter's competence can coexist because the commitment concerns the argument's reach rather than actual theory possession.

**Composition friction — thinnest joints:**

1. **“They were acquired from examples … So an LLM does not sit at either pole of Naur's partition”** — UNSUPPORTED — acquisition from examples does not establish that the resulting judgments cannot be determined by a formulable procedure.
2. **“Nor does it help to note that an LLM is a computable procedure. Naur's argument is about expressibility … not about computability”** — UNSUPPORTED — naming the distinction does not show that a finite implementation lies outside the rules Naur excludes.
3. **“The very act of adhering to rules can be done more or less intelligently … What stops the regress is a grasp of similarity … [which] cannot be expressed in terms of criteria”** — THIN — the regress motivates judgment in applying rules but does not itself derive the stronger inexpressibility claim.
4. **“So a competent interpreter plus text is not thereby a theory-holder, and any composite that claims to be one owes three things”** — THIN — one compiler handoff does not by itself establish every requirement for every composite, especially the retained-premise requirement.
5. **“The 'but' carries an inference from not expressible to human. It is valid only if the candidates for holding a theory are exhausted by two kinds”** — HOLDS — rule-inexpressibility cannot yield human-only possession without a premise excluding every eligible nonhuman, non-rule candidate.

**Premise decomposition — premises:**

1. **A deployed LLM is outside “what can be determined by rules” in Naur's sense because its similarity criteria were learned rather than written by a person.** — DOUBTFUL — finite executable architecture and parameters may belong to Naur's formal-machine pole — GLOBAL — instance.
2. **Naur's exhaustive human-insight/formulable-rule partition is the premise through which his human-binding conclusion is reached, rather than one of several independent anthropocentric restrictions.** — DOUBTFUL — other person-bound passages may supply additional restrictions — GLOBAL — instance.
3. **Acquisition from examples rather than direct human specification is sufficient to distinguish a recognizer from a follower of formulable rules.** — DEFEATED — an induced decision tree is learned from examples yet is an explicit finite rule set — LOCAL — instance.
4. **Inexpressibility in terms of criteria or rules does not by itself entail that only humans can possess the capacity.** — HOLDS — a further premise must exclude eligible nonhuman candidates.
5. **Naur supplies no separate argument that the relevant similarity judgment is noncomputable or unrealizable by every formally implemented interpreter.** — HOLDS — the retained source supplies assertions about criteria and rules, not a computation-level exclusion.
6. **Contesting the argument's reach does not require first showing that a current LLM possesses a program's theory.** — HOLDS — an eligible unexcluded candidate suffices for the logical point.
7. **A particular program theory requires program-specific acquisition; general competence and artifact access do not establish it.** — HOLDS — easy acquisition is not absence of acquisition.
8. **A necessary decision premise that the interpreter cannot regenerate must be supplied by some component of the composite.** — HOLDS — advice, training, or an external record each adds a supplying component.
9. **Theory possession is dispositional across later demands, so one successful extension does not establish it.** — HOLDS — a lucky or memorized success lacks the cross-occasion capacity.
10. **Naur's reported transfer failures do not exclude every untested retained-rationale or trained-interpreter route.** — HOLDS — the reported package and group do not compare all such routes.

No premise was `GLOBAL`-defeated. Premises 1 and 2 are `GLOBAL` doubts routed to the packet reader; premise 3 is a `LOCAL` defeat. None is converted here into an automatic passage action.

## Gate findings

### Accessibility

| Gate | Result | Finding |
|---|---|---|
| jargon-persistence | PASS | Repeated terms are locally explained or ordinary in context. |
| notation-opacity | PASS | No imported notation or symbolic syntax needs decoding. |
| undefined-terms | PASS | Program theory and the three conditions receive sufficient local explanation. |
| unidentified-references | FAIL | Ryle lacks an identifying role at first mention. |

### Complexity

| Gate | Result | Finding |
|---|---|---|
| claim-to-section-ratio | PASS | The four sections perform distinct argumentative jobs. |
| connection-inflation | PASS | Existing footer links do not duplicate the same inline relationships. |
| could-be-a-paragraph | PASS | The missing premise, interpreter question, and retained conditions require separate development. |
| framework-decoration | PASS | The three-item condition list is substantive, not ornamental taxonomy. |

### Frontmatter

| Gate | Result | Finding |
|---|---|---|
| claim-strength | PASS | The incumbent title is substantive and contestable. |
| description-discrimination | PASS | The description distinguishes the note by its two-step argument and trained-interpreter challenge. |
| title-as-claim | PASS | The title states a truth-apt proposition. |
| title-body-alignment | PASS | The incumbent body directly develops the incumbent title. |
| title-composability | PASS | The title composes as a causal premise. |

### Prose

| Gate | Result | Finding |
|---|---|---|
| anthropomorphic-framing | PASS | Cognitive vocabulary is functional and the note distinguishes competence from argument reach. |
| bridge-paragraph-duplication | PASS | Section transitions advance rather than preview-and-repeat. |
| confidence-miscalibration | WARN | The 1985 historical explanation and categorical LLM claim exceed their support. |
| orphan-references | WARN | Those same historical and technical empirical claims lack an adequate source. |
| proportion-mismatch | PASS | The longer closing section preserves useful conditions rather than displacing the main claim. |
| pseudo-formalism | PASS | The note uses no decorative formal apparatus. |
| redundant-restatement | PASS | Section openings introduce distinct argumentative steps. |
| source-residue | PASS | Programming and compiler details remain inside the note's stated domain. |
| unbridged-cross-domain | PASS | The note does not use unrelated-domain evidence to assert LLM competence. |

### Semantic

| Gate | Result | Finding |
|---|---|---|
| completeness-boundary-cases | PASS | The three conditions are necessary checks, not a sufficient or exhaustive taxonomy. |
| conceptual-role-conflation | PASS | Ryle, Naur, this note's diagnosis, the interpreter, and retained text keep distinct roles. |
| epistemic-status-blur | PASS | Source report, deduction, and open empirical question are mostly separated. |
| explanatory-reach | PASS | The argument exposes a criticizable missing-premise mechanism. |
| grounding-alignment | FAIL | Universal source claims and details of the compiler repair/rationale route exceed retained extracts. |
| internal-consistency | WARN | “Can be formulated” drifts into “was formulated” at the LLM application. |
| load-bearing-qualifiers | PASS | Program, human-only scope, and condition-specific qualifiers do real work. |
| underspecified-assertions | WARN | “Formulated criterion” leaves human-readable rubric versus finite formal specification unresolved. |
| unearned-generality | PASS | General interpreter vocabulary is necessary to test an exhaustive partition. |
| unwarranted-scope | PASS | The incumbent explicitly limits itself to argument reach rather than actual theory possession. |

### Sentence

| Gate | Result | Finding |
|---|---|---|
| clause-packing | WARN | The capability-list sentence and compiler-case sentence each carry too many steps. |
| concept-attribution | PASS | Linked recovery and interpretation/retention concepts match their targets. |
| framing-mismatch | PASS | The prose usually frames source argument, mechanism, and scope at the right levels. |
| misleading-link-text | PASS | Existing link text accurately previews its targets. |
| parsing-ambiguity | PASS | Dense sentences do not create materially different parses. |
| stock-phrases | PASS | Contrastive scope sentences are substantive rather than filler. |

### Structural

| Gate | Result | Finding |
|---|---|---|
| bullet-capitalization | PASS | All bullets begin with capitals. |
| compound-bullet | PASS | Each longer bullet develops one organizing condition or edge. |
| general-before-specific | PASS | The note moves from general argument to candidate and bounded cases. |

## Connection candidates

- `contrasts` -> `kb/notes/definitions/representational-form.md` — separates distributed-parametric model state from the symbolic runtime executing it, so training history alone cannot decide rule-determination.
- `contrasts` -> `kb/notes/opacity-is-a-scale-threshold.md` — prevents practical opacity or lack of human-authored criteria from being mistaken for in-principle informulability.

## Proposed revision shape

1. Retitled opening: rule-inexpressibility alone does not establish human exclusivity.
2. Source reconstruction: Naur's regress and similarity claim, with possible formulability kept distinct from actual formulation.
3. Additional-premise diagnosis: machine/rule passages are one exclusion route, while other person-bound language remains separate.
4. Trained-interpreter boundary: current LLMs expose but do not settle the difference among semantic rubrics, finite specification, and computability.
5. Bounded transfer evidence and three preserved conditions: program-specific acquisition, availability of non-regenerable premises, and cross-occasion reliability.
6. Direct close: current systems remain empirical; Naur's rule argument alone cannot settle them.

## Open items

- Required post-pass reframe operation: after this pass completes, rename the live note with `commonplace-relocate-note` to `kb/notes/naur-rule-inexpressibility-does-not-imply-human-only-theory.md`; then update visible link text and one-line summaries in `kb/notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md`, `kb/notes/design-rationale-must-preserve-unregenerable-decision-premises.md`, and `kb/sources/programming-as-theory-building.ingest.md`; finally reconcile any argument in those citers that relied on the stronger claim that a current trained interpreter is already outside Naur's partition. The retained packet, its historical source, and its directory must remain unchanged.
- Composition-friction and premise-decomposition attention remains human-routed. The edited note should be reread against their “For the human” lines, especially the learned-criteria/formal-execution boundary and the possibility of more than one person-bound exclusion premise.
- Step-8 reread: both initial “For the human” lines point to the learned-criteria/formal-execution shift. The edited note now rejects that inference explicitly and treats current LLMs as unresolved, so those initial lines no longer describe an unacknowledged gap in the edited text. The closing reruns must assess the new argument rather than carry the initial wording forward as an outstanding defect.
- Connection candidates are additive suggestions, not packet-applied body edits. Evaluate them only after the reframe is stable; do not use them to reintroduce the rejected LLM witness.
- Closing routed attention remains unresolved: friction finds that the Ryle regress needs an unstated premise that every standard for correct rule application must itself be represented as another rule. Premise decomposition marks as `DOUBTFUL — GLOBAL — instance` the reading of Naur's “inextricably bound to human beings” as a defended species boundary rather than a description of the embodied programmer teams in his setting. The central missing-premise diagnosis survives both findings, but a later reader should decide whether the Naur-specific framing needs rescoping.
- Closing grounding follow-up: either retain source support for “Naur ties a program's life to a team that remains in control and can answer later demands” or narrow that attribution. The current tracked ingest's retained quotes do not support the full proposition, so the closing semantic grounding gate fails on the dispositional-reliability test.
- Closing editorial follow-up: decide whether the three transfer tests belong in a separate note or should be compressed to a bounded application here. If they remain, address the unused `Computability` level, the immediate repetition of the additional-premise hinge, and the general-framework-after-specific-LLM ordering. The one-cycle stopping rule leaves these findings unapplied.

**Post-step-9 note SHA-256 recorded before closing job creation:** `1a9143d546bfcbc4cb31eca43de8c03769ea3f7a2cb0cc978b25fe85c51f210f`

## Closing cycle

**Pass ID:** `20260826T140020Z-7c9e`
**Final note SHA-256:** `1a9143d546bfcbc4cb31eca43de8c03769ea3f7a2cb0cc978b25fe85c51f210f`

| Assay | Closing result | Residual routed to Open items |
|---|---|---|
| compression bundle | WARN — core claim passes; branch bloat, detail overhang, and marginal redundancy remain around the transfer-test branch and repeated hinge | yes |
| critique-note | No surviving attack on the central commitment; secondary cautions concern species-level exegetical scope and how much the compiler case establishes | yes |
| composition-friction-gate | SURVIVES — one unsupported regress joint, three thin joints, and the central missing-premise inference HOLDS | yes |
| premise-decomposition-gate | Five premises HOLDS; one premise is `DOUBTFUL — GLOBAL — instance`; no premise is `DEFEATED` and there is no GLOBAL defeat | yes |
| accessibility / complexity / frontmatter / prose / semantic / sentence / structural | 38 PASS, 2 WARN, 1 FAIL — complexity warns that `Computability` is unused; structural warns that the general tests follow the specific LLM case; semantic grounding fails on the unsupported team-control attribution | yes |
| connect | Two `contrasts` candidates remain: representational form and scale-dependent opacity; the rerun also confirms the required relocation-and-citer reconciliation dependency | yes |
| warranted contribution | strengthened — the final text directly states and defends the selected missing-premise update, removes the unsupported learned-system counterexample, and introduces no new angle | no |

Relative to the same intended reader and existing-KB baseline, the final text strengthens the selected update. It now separates Naur's rule-inexpressibility claim from every possible route to human exclusivity, treats current LLMs as unresolved, and survives the closing critic's strongest conceptualist objection. The transfer tests were already part of the incumbent contribution, so retaining them does not introduce a new angle; the closing findings concern their proportion, ordering, and source support rather than the logical update itself. Catalog and critique verification selectors both returned empty target lists under the `codex` model partition.

## Resolution

**Status:** not-required
**Resolved at:** —
**Authority:** —
**Outcome:** —
**Rationale:** —
**Resulting paths:** —
