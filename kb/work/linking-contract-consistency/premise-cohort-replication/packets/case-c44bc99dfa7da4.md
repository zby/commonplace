# Case packet

Neutral case identifier: case-c44bc99dfa7da4

The possible directed relationship from Artifact A to Artifact B is under review.

## Artifact A

# Scheduler-LLM separation exploits an error-correction asymmetry

The [bounded-context orchestration model] separates symbolic scheduling from bounded LLM calls. Context scarcity is [one motivation] for that separation. This note develops the other: an error-correction asymmetry grounded in the [three phenomena] that cause LLM output to deviate from intent.

## The three phenomena affect bookkeeping and semantic work differently

LLM output deviates from intent through [underspecification, indeterminism, and interpretation error (bias)]. Each affects bookkeeping and semantic operations differently.

**Bookkeeping** — counting, state tracking, list manipulation — can in principle be fully specified: given disk configuration X in Towers of Hanoi, there is exactly one correct next move. This eliminates underspecification as a theoretical source of error. What remains are indeterminism (variance) and interpretation error (bias).

In practice, when bookkeeping is done inside the LLM, even well-specified tasks show residual errors — from indeterminism and bias, not underspecification. [ConvexBench] shows LLMs tracking compositional depth see F1 collapse from 1.0 to 0.2 at depth 100 despite using only 5,331 tokens. [MAKER] faces similar residual errors on well-specified Towers of Hanoi steps (~99.8% per-step accuracy before correction). Both papers have tasks with unique correct answers — the errors are properties of the interpreter, not the spec. The whole point of separation is to move bookkeeping out of the LLM and onto a substrate where these problems don't arise.

**Semantic operations** — summarisation, reasoning, code generation — face all three simultaneously. Underspecification is inherent: the "correct" output is not unique. Indeterminism explores a space whose boundaries are set by underspecification. And bias adds systematic misses on top.

## Symbolic systems eliminate all three for bookkeeping

Symbolic systems — pen and paper, digital computers — restore signals to discrete states at each step. A transistor just needs to be close enough to snap back to 0 or 1. This eliminates all three phenomena simultaneously, relative to the implemented transition function: the input fully specifies the output (no underspecification), operations are deterministic (no indeterminism), and discrete-state restoration leaves no room for the interpreter to miss systematically (no bias). The relativization matters: the substrate executes a wrong transition function exactly as faithfully as a right one, and [an artifact can be exact with respect to a requirement that is itself a proxy] — what the substrate eliminates is interpreter deviation, not specification error.

This is so fundamental we forget it's there. The reliability of digital systems isn't a property of the components — it's a property of the discrete-state restoration at every step.

## Humans exhibit the same pattern

We cannot multiply large numbers in our heads or track deep recursion without external aids. We reach for pen and paper — not because we can't reason, but because our mental operations lack reliable intermediate state. LLMs, like humans, are powerful per-step reasoners that fail at extended bookkeeping. Both need an external substrate for reliable multi-step state tracking.

## MAKER: error correction when bias is low

[MAKER] achieves zero errors over 1,048,575 Towers of Hanoi steps by addressing each phenomenon:

- **Eliminating effective underspecification**: maximal decomposition ensures each LLM call sees only the current disk configuration — minimal, bounded context.
- **Correcting indeterminism**: first-to-ahead-by-k voting across multiple samples at low temperature (0.1).
- **Keeping bias low**: bounded context prevents the context-length-dependent bias that ConvexBench demonstrates. Per-step accuracy is ~99.8% — residual errors are mostly variance, not bias, so same-prompt voting works.

The critical insight: when bias is low, same-prompt sampling decorrelates errors because they're variance. When bias is high (the distribution itself is wrong), all voters draw from the same wrong distribution and agree on the wrong answer. Correcting bias requires prompt perturbation — different phrasings per voter — which is far more expensive. (The [synthesis-is-not-error-correction] distinction also matters — MAKER uses voting, not synthesis.)

## Semantic operations resist cheap error correction

Bookkeeping admits cheap correction because underspecification is eliminable, hard oracles are available (exact equality checks), and bias stays low with bounded context.

Semantic operations face all three phenomena simultaneously. The [error correction framework] allows softer checks — metamorphic tests, judge models, cross-document consistency — but these oracles are weaker (smaller TPR - FPR gap), more expensive (each check costs an LLM call), and harder to decorrelate (LLMs share systematic biases from training). Semantic error correction requires bespoke techniques — there are no general methods analogous to discrete-state restoration.

Semantic error correction is possible in some cases, but expensive and domain-specific. Mixing bookkeeping with semantic work forces bookkeeping onto the same substrate, wasting resources on reliability that a symbolic machine provides for free.

There is an intermediate regime: systems like OpenProse use DSLs and explicit frame interfaces to recover scoping benefits *before* the scheduler moves into code. The parser and scheduler remain LLM-mediated, so the asymmetry argument still applies in principle — but how much practical reliability the intermediate regime actually delivers is an open empirical question. [Specification-level separation recovers scoping before it recovers error correction] develops this.

## The conjecture, stated

The effectiveness of separating symbolic scheduling from bounded LLM calls reflects an asymmetry across all three phenomena:

1. **Underspecification**: eliminable for bookkeeping (the task has one correct answer), inherent for semantic work
2. **Indeterminism**: cheaply correctable via voting when bias is low (bookkeeping with bounded context); expensive when interacting with underspecification and bias (semantic work)
3. **Bias**: eliminable for bookkeeping by moving to a symbolic substrate (relative to the implemented transition function); persistent for semantic work, requiring expensive decorrelated correction

Separation addresses all three: symbolic substrates eliminate underspecification, indeterminism, and bias for bookkeeping; bounded LLM calls keep semantic work in the regime where per-step bias is low enough for cheap error correction. Mixing forces bookkeeping into accumulated context where bias grows, underspecification is reintroduced by context noise, and error correction becomes expensive. The boundary is a cost gradient, not a hard line.

The asymmetry justifies a symbolic runtime; it does not make the symbolic layer static infrastructure. The right schedulers, schemas, and invariants are not known once and for all — operation keeps revealing better decompositions and new enforceable constraints, as when [an index's strained completeness promise became validator code] that then caught what the prose search recipe had missed. So the symbolic layer is itself a learning target, and the write path into it is [codification, with relaxation as the reverse move]: the boundary this note prices is renegotiated as evidence accumulates, not fixed at design time.

## Status and scope

The exact boundary remains conjectural, but the core asymmetry claim now has enough convergent support to keep as a seedling rather than a pure speculation. The evidence (ConvexBench, MAKER, RLM, the human parallel, and Tu's structured test-time scaling analysis) is consistent, but a precise characterization of the boundary remains open.

The [RLM architecture] provides a striking limit case: the LLM writes whole programs, yet the call stack for recursion still runs in the REPL. Even an LLM powerful enough to write correct recursive programs delegates execution bookkeeping to the symbolic layer.

---

Relevant Notes:

## Artifact B

# Exact implementation does not validate a requirement against its objective

An artifact can be perfectly correct relative to its immediate requirement yet still be wrong for the system-level problem. Exactness belongs to the artifact–requirement link; proxyhood belongs to the requirement–objective link above it. Confusing the two makes local verification look like upstream validation.

The unit of analysis is a single named artifact–requirement–objective path within a declared boundary. Real requirement structures branch: the same artifact may exactly implement one adopted requirement while serving as a conjectured proxy under another objective. Artifact-level phrases such as “exact-spec artifact” are safe shorthand only when the relevant path is named or every path in scope has the same status.

Arithmetic, sorting, schema validation, fiscal-period normalization, and legal move generation in chess illustrate locally exact requirements once the intended variant, input encoding, and output contract are fixed. Vision features such as SIFT, Haar cascades, and Canny edge detection likewise had precise mathematical specifications and useful invariants. They implemented those specifications exactly. What remained conjectural was the link from edge maps and keypoints to seeing: a theory about what seeing requires, not a definition of seeing.

## A commitment creates a local floor, not a chain endpoint

At the highest link in scope, an analysis encounters either an adopted commitment or a conjectured decomposition. That is a boundary chosen for the analysis, not the top of an objective hierarchy.

An adopted commitment [creates ground truth for the levels below it]. A schema is the contract because the project adopted it; chess move generation is exact because the rules constitute the game. Below the commitment sits conformance, checkable against the adopted requirement. Above it sits a different question: whether adopting that requirement serves a further objective. Adoption settles who or what defines local correctness; it does not establish that the choice is useful, stable, legitimate, or cheap to reverse.

A conjectured decomposition instead posits that satisfying one requirement contributes to a capability nobody defined. “Detect edges” was a theory about what seeing requires. The machinery could be checked against the edge-detection specification, but the link from that requirement to seeing needed separate evidence.

These questions require different checks. A hard oracle can make conformance cheap without showing that its target is the right target. Evidence for the requirement–objective link must instead come from an explicitly constitutive scope, outcome data, predictive tests, ablations, or composition. [Oracle strength] is therefore one confidence factor in hardening a conjectured link, alongside coverage, failure cost, reversibility, volatility, and external dependencies.

## A failed proxy link preserves local correctness, not necessarily artifact value

The vision story invalidates less than it first appears to. Edge detection remains exact relative to its own requirement and useful wherever edges are genuinely wanted, such as document deskewing or industrial inspection. What failed was the broad conjecture that the requirement would compose into seeing—the [unearned reach that scale selects against].

That diagnosis preserves a fact, not an asset. The artifact still conforms locally, but retaining it depends on whether anyone wants the narrower requirement and whether reuse is cheaper than replacement or removal. The logical repair is to retract the failed requirement–objective claim and rescope any surviving use; disposal remains appropriate when the narrower capability has no value.

## Composition tests what local conformance cannot

Local checks test the artifact–requirement link. End-to-end composition tests whether the chosen requirements jointly serve the capability above them. Where no earlier oracle directly exposes a conjectured link, composition may be its first strong test, so locally correct components that systematically fail together are evidence against the decomposition.

Composition failure is not unique to proxy theories. Incompatible interfaces, inconsistent composed specifications, omitted resource limits, and execution defects can produce the same symptom. Conversely, a proxy can compose successfully over the observed range. Diagnose those alternatives before attributing failure upward. The key point is narrower: passing every local check cannot validate a link that none of those checks addresses.

## Diagnose one path at a time

Three questions inform confidence; none determines the classification alone:

1. **Is the immediate requirement constitutive of the declared objective?** If satisfying the requirement is what the bounded analysis means by success, there is no additional proxy link inside that boundary. If the requirement only stands in for a larger capability, the link remains conjectural.
2. **What does the available oracle establish?** A deterministic checker establishes conformance to its target. Human judgment, outcome measures, and proxy scores may bear on the upstream link, but their verdicts remain limited to their stated domains.
3. **Where do failures surface?** Local errors implicate the artifact or immediate specification. Repeated objective failure despite local passes implicates a higher link only after competing integration causes have been ruled out.

The practical posture is provisional [codification]: crossing from natural-language guidance into a symbolic artifact with formal semantics. Harden local conformance when the gain in reliability, speed, or cost exceeds the expected costs of change and failure; adoption supplies authority, not prudence. Harden a conjectured link only to the degree its evidence warrants, keeping the artifact inspectable, tested, and easy to relax.

[Spec mining] strengthens the evidence by extracting candidate requirements from working behavior rather than inventing decompositions upfront. [Operational relaxing signals] help detect when a hardened link has stopped fitting. When a link fails, record which reach claim was retracted, preserve whatever local correctness remains, and reassess the narrower artifact on its actual value.

---

Relevant Notes:

## Under-review context phrase

the substrate executes its implemented function exactly; whether that function is the right one is the requirement-chain question this note delegates
