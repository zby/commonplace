# Case packet

Neutral case identifier: case-30111db7b8e1ad

The possible directed relationship from Artifact A to Artifact B is under review.

## Artifact A

# Machinery persists by warrant, not position, in a reflective loop

[The bitter lesson] has two modes, and its folk application remembers only one. The apply-mode is a selection rule over existing methods: prefer the techniques "that have been shown to scale." The build-mode is in Sutton's own conclusion — "time is better invested in finding simple scalable solutions" — and it is what compliance means where no scaled method exists yet: building one. [The two-axis reading] locates the localized forms in exactly that situation.

The build-mode's own history shows what gets hand-crafted. Every victory in Sutton's list is hand-designed *machinery* whose *content* is produced by computation: Deep Blue's alpha-beta search, the hidden Markov models that beat hand-crafted speech pipelines, the convolutional architecture that beat hand-coded features. The lesson never opposed hand-crafting as such — it requires it, at the meta-method level — and damns it only for content. [Sutton's own closing says so directly]: "we should build in only the meta-methods that can find and capture this arbitrary complexity… We want AI agents that can discover like we can, not which contain what we have discovered." Hand-craft the machine that learns; never hand-write what it should have learned.

## Sutton's geometry has an outside; reflection erases it

That prescription has a clean geometry: the meta-method sits *outside* the learned system. The researcher designs the architecture; the architecture learns the content; the boundary never moves — and the frozen outside is also where gradient descent's stability comes from, since the machinery doing the selecting is never itself under selection.

A [reflective system] has no outside. Its machinery — types, gates, validators, skills, the loop's own instructions — is artifacts in the localized forms, sitting in the same repository, revisable by the same loop. This is not a design flaw to engineer away; it is already operative: the traced tag-readme episode is machinery produced *by* the loop (an operational strain became validator code), [oracle accumulation is machinery-production as a standing channel], and [the symbolic layer is a learning target with codification as its write path]. "Hand-craft the meta-method, learn the content" cannot be stated as an architecture here, because no component is structurally *not content*.

## What replaces the outside

Three substitutions, each already carried by a standing claim:

- **The hand-crafted/learned boundary becomes a per-artifact, time-indexed provenance fact.** "Hand-crafted" says who produced the current version, nothing more. Everything starts hand-crafted — that is what bootstrapping means — and the loop takes over production progressively, content first, machinery later. The boundary is a frontier that moves, not a partition that holds.
- **Exemption by position becomes persistence by warrant.** In the frozen geometry the meta-method escapes selection by sitting outside it. Here nothing escapes by position: a gate survives because its criterion keeps discriminating, a type because its carve keeps earning use — [the earned-reach standard] applied uniformly, machinery included. This is more lesson-compliant than the frozen geometry, not less: even the meta-method faces search and selection.
- **The permanently external becomes a function class, not a component class.** What stays outside the loop is not any artifact but the functions no loop can perform for itself: [the objective], commitments, and the adoption "no" — external by category, however much of its machinery the loop comes to rewrite.

## The cost is the fixed point

Gradient descent buys stability precisely from its frozen meta-method. A reflective loop judges proposed changes with machinery that is itself in scope — the trusting-trust condition, with fuzzier tools than Thompson had. Giving up exemption-by-position means giving up the free fixed point, and what stands in for it is governance: an adoption decision [allocated outside the text being judged], acceptances kept localized and reversible, and [accumulated oracles whose exhaustive wire does not depend on the judgment currently under revision]. The reflective build-mode is harder than Sutton's for exactly this reason — the fixed point is replaced by governance — and pretending the machinery is exempt would not restore stability; it would only hide where the trust is being spent.

## Scope

- The claim is about what *licenses* persistence, not about current production ratios: one traced instance of loop-produced machinery plus one standing channel do not make the loop the main producer of its own machinery today. Content-first-machinery-later is an observed bootstrap order, not a law.

## Open Questions

- Is there a minimal kernel that must stay fixed for the loop to remain stable — a trusted-computing-base analog for reflective improvement — or can governance plus reversibility fully replace the fixed point?
- What warrant would license moving a piece of machinery's *production* into the loop, as distinct from its revision — the migration-earned criterion applied to authorship rather than judgment?

---

Relevant Notes:

## Artifact B

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

## Under-review context phrase

the symbolic layer as learning target, with codification as the write path
