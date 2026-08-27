# Claim skeleton: the context-operation interface bounds context policy

## Central contribution and shape

**Only durable proposition:** Holding the retained substrate, model, and
resource budget fixed, a context-operation interface bounds the active-context
projections a policy can realize. A better policy can improve selection within
that set, but cannot by itself expand the set or establish that the interface is
adequate or optimal.

- **Scope:** architecture-level and conditional on fixed premises; it does not
  rank interfaces or predict task performance.
- **Confidence:** high as a conditional structural inference, not as an
  empirical performance result.
- **Basis:** `claim-disposition.md` fixes the contribution; the reconstruction's
  `Reach(I, S, x; M, B)` account supplies the mechanism; the existing
  fixed-decomposition claim supplies the general premise. Authoritative user
  direction selects the proposition but is not empirical warrant.
- **Shape rule:** every definition, contrast, consequence, and limitation below
  must establish, apply, or bound this proposition. Do not promote controller
  placement, persistence, operation taxonomies, or evaluation advice into a
  second independently importable claim.

## Truth conditions and comparison vocabulary

Define only what the argument uses:

| Item | Meaning needed in the note | Scope, confidence, and basis |
|---|---|---|
| Retained substrate / active context | Retained substrate is state available outside a bounded model input; active context is what one bounded invocation actually receives. | Architecture-general; high confidence as an analytical distinction; basis: the reconstruction and the existing runtime-decomposition and storage/activation notes. |
| Context-operation interface | The operations and permitted compositions through which a controller locates, materializes, transforms, and exposes retained state as active context. Addressable units and the exposure boundary are part of what makes those operations effective. | Fixed local definition; basis: authoritative brief, elaborated by the reconstruction. |
| Projection / projection boundary | A projection is the task- and state-conditioned view delivered into active context after a legal interface trace. It need not be lossless, linear, idempotent, or non-mutating. The boundary is where that view becomes model input. | Local analytical definitions; high conditional confidence; basis: reconstruction synthesis across the corpus. |
| Controller or context policy | The mechanism choosing whether, when, and how to invoke legal interface operations. It may be the receiving model, a learned controller, a host/proxy, or a mixed push/pull arrangement. | Architecture-general classification; high confidence at this abstraction; basis: reconstruction's control-placement comparison. |
| Structural reach / achieved use / activation | `Reach(I, S, x; M, B)` is the set of views obtainable by legal traces. A policy induces an achieved subset or distribution. A delivered view's later behavioral use is a further activation boundary. | High confidence as explicitly introduced formalization; basis: reconstruction plus the fixed-decomposition and activation notes. |
| Operation class | Open-ended model-authored programming, restricted typed composition, and a fixed set of memory operations differ in permitted traces; these labels do not rank performance. | Descriptive comparison only; moderate confidence for source-described designs; basis: quoted practitioner RLM, lambda-RLM, and ACM inputs. |
| Persistence and mutability | Within-run, cross-restart, and cross-task persistence say how long state can affect selection. Changing a retained invocation policy is distinct from changing operation semantics or composition rules. | Boundary condition, not a system taxonomy; high confidence as an analytical distinction; basis: required brief distinction and reconstruction's RLM/Prime Agent/Fractal/AgeMem/Recuris inventory. |
| Fidelity | Storage fidelity concerns retained material; projection fidelity concerns the particular view delivered. Neither implies that exposed material is behaviorally activated. | Scope distinction; high confidence; basis: reconstruction and the existing storage/activation note. |

Use **context-operation interface**, not **action alphabet**. If the latter must
appear, use one sentence to reserve it for world-effect primitives and cite the
existing authority note; do not develop that separate theory here.

## Ordered paragraph plan

### Mechanism

**Paragraph 1 — identify the object and state the contribution.**

- **Work:** Make the reader separate retained state, active context, interface,
  and controller before encountering examples.
- **Assertions:** Retention and context assembly are distinct responsibilities;
  the interface supplies legal operations/compositions while the policy chooses
  among them; under fixed substrate, model, and budget, that interface bounds
  realizable projections.
- **Scope/confidence/basis:** Architecture-general; high conditional confidence;
  central proposition and definitions above, supported by the existing runtime
  decomposition and fixed-decomposition notes. Do not imply that the controller
  is always the model receiving the projection.

**Paragraph 2 — construct the reachable-set mechanism.**

- **Work:** Give the reader the reason the bound exists, not merely the slogan.
- **Assertions:** Let `I` include operation semantics, addressable units,
  composition rules, and exposure boundary; with `S`, task/run signal `x`,
  model(s) `M`, and budget `B` fixed, `Reach(I, S, x; M, B)` contains the views
  obtainable by legal traces. A required view that needs an unavailable
  operation, an unaddressable distinction, or a forbidden composition lies
  outside that set.
- **Scope/confidence/basis:** Explicit local formalization; high confidence as a
  deduction from the definitions; reconstruction's reachable-set inference and
  the general fixed-decomposition premise. State that traces may transform or
  update retained state before exposure, so “projection” is not a narrow
  mathematical projector.

**Paragraph 3 — derive the policy boundary.**

- **Work:** Show exactly what policy learning can and cannot establish.
- **Assertions:** A policy selects legal traces and therefore induces achieved
  coverage or a distribution within structural reach. Better selection can
  improve coverage, reliability, or cost without changing structural reach.
  It cannot show that excluded projections are unnecessary, so within-interface
  gains do not validate completeness or optimality. If an intervention adds
  observations, computation, tools, model capability, budget, or permission to
  change operation definitions, a premise changed; it is not merely a better
  policy over the same interface.
- **Scope/confidence/basis:** High conditional confidence; direct inference from
  Paragraph 2 and the fixed-decomposition note. “Improvement” remains agnostic
  about learning method and outcome magnitude.

### Two discriminating architectural contrasts

**Paragraph 4 — vary permitted composition while avoiding a survey.**

- **Work:** Make the interface variable concrete with one compact three-way
  contrast.
- **Assertions:** The quoted practitioner RLM account permits model-authored
  programmatic search and transformation before explicit return/exposure;
  lambda-RLM replaces arbitrary programs with a small typed combinator
  language; ACM fixes two memory operations and learns invocation/abstention.
  These designs admit different legal traces even though all construct bounded
  model context.
- **Scope/confidence/basis:** Claims only about the described architectures;
  moderate confidence for practitioner/paper descriptions with retained Quotes,
  not code execution or causal performance. Basis: RLM walkthrough,
  lambda-RLM, and ACM reconstruction records. Omit benchmark quantities and do
  not infer that the broadest interface performs best.

**Paragraph 5 — separate who selects from what can be selected.**

- **Work:** Prevent controller placement, persistence, or learning from being
  mistaken for interface richness.
- **Assertions:** Reuse RLM and ACM as model-selected and learned-controller
  cases; add only Virtual Context as a host/proxy-selected initial projection
  and Letta as a mixed push/pull boundary. These placements can coexist with
  different operation vocabularies, so placement does not determine structural
  reach. Within-run, cross-restart, and cross-task retained state describe the
  conditioning horizon; changing an invocation policy is not by itself a change
  to the operation interface.
- **Scope/confidence/basis:** The independence claim is a high-confidence
  inference from the reconstruction. Named facts are moderate confidence for
  source-described RLM/ACM designs and high only for pinned static wiring in the
  Virtual Context/Letta reviews; they do not establish runtime correctness.
  Keep persistence as a boundary sentence, not a multi-system catalogue.

### Evaluation consequence

**Paragraph 6 — turn the mechanism into an evaluation test.**

- **Work:** Let an evaluator identify which assumption a reported gain actually
  tests.
- **Assertions:** A controller evaluation must identify the retained substrate,
  addressable unit, operations and composition rules, controller placement,
  projection boundary, mutable policy/artifacts, persistence horizon, model,
  and budget that remained fixed or changed. Gains with one fixed operation set
  are evidence that a policy was useful in that regime, not that excluded
  operations are unnecessary. Interface adequacy needs a rival or
  constraint-changing intervention, or an argument that excluded projections
  cannot improve the objective.
- **Scope/confidence/basis:** High confidence as the direct diagnostic
  consequence of Paragraphs 2–3; basis: reconstruction's evaluation section,
  the fixed-decomposition note, and ACM only as a conditional example. Do not
  restate ACM numbers already owned by the existing note.

### Scope

**Paragraph 7 — locate the claim between retention and behavioral use.**

- **Work:** Stop readers from treating reachability as storage fidelity,
  discoverability, or successful activation.
- **Assertions:** Exact retention can coexist with a lossy or missed active
  projection; an admitted trace may never be discovered or produced reliably;
  and a delivered view may still fail to influence behavior. The central claim
  ends at exposure into active context.
- **Scope/confidence/basis:** High confidence as layer separation; basis:
  reconstruction, the storage/activation note, and proposition-relative system
  witnesses. Cite the existing note rather than reproducing its full evaluation
  ladder.

**Paragraph 8 — state the non-ranking and evidence limits.**

- **Work:** Preserve what the proposition does not license.
- **Assertions:** A restricted interface may trade admitted transformations for
  reliability, safety, inspectability, trainability, latency, or cost; an
  open-ended programming interface remains bounded by primitives, sandbox,
  permitted composition, model competence, and budget. The system contrasts
  show that architectural coordinates vary, not the causal performance effect
  of varying one coordinate.
- **Scope/confidence/basis:** Scope-qualified possibility and limitation, not an
  optimization claim; basis: authoritative exclusions plus the reconstruction's
  lambda-RLM tension and evidence-tier warning. End without a summary paragraph:
  Paragraph 6 already states the actionable consequence.

## Inferential spine

1. Retained state is not yet active context; some operation trace must expose a
   bounded view.
2. The interface defines which traces are legal under fixed substrate, model,
   task/run signal, and budget.
3. Legal traces determine a structural reachable set of views.
4. A policy only selects among those traces, producing achieved coverage within
   the reachable set.
5. Therefore improving selection can improve achieved results but cannot, by
   itself, add a view whose construction requires a missing operation,
   distinction, or composition.
6. Therefore gains under a fixed interface test the policy/interface pair in
   that regime; they do not test the necessity of excluded operations or prove
   interface adequacy.
7. The two contrast families show why operation/composition, controller
   placement, persistence, and mutability must be reported separately when
   applying that conclusion.

## Unresolved-marker disposition

| Marker or uncertainty | Classification | Authorized treatment |
|---|---|---|
| Named Scroll Event Log, namespace, eviction-index, or explicit-print details lack retained Quotes. | **Omittable; non-blocking.** | Omit Scroll entirely. The RLM walkthrough supplies the needed programmable-interface witness. |
| Named details from The Log Is the Agent, Coding Agents Are Effective Long-Context Processors, and Slate lack retained Quotes. | **Omittable; non-blocking.** | Omit all three; none is needed by the inferential spine. |
| Cross-system contrasts are not controlled interventions on interface design. | **Publishable limitation; non-blocking.** | State only that the coordinates vary across described systems; do not estimate a causal performance effect. |
| Whether a broader interface is preferable under reliability, safety, trainability, latency, or cost constraints. | **Publishable limitation/open question; non-blocking.** | Preserve as the non-ranking scope boundary; do not answer it in this note. |
| Central contribution, definition, target, or evidence indispensable to the mechanism. | **No blocking marker remains.** | Proceed to drafting without acquiring another source. |

## Tempting branches to omit

- A system-by-system survey, leaderboard, benchmark table, or broad memory-system
  taxonomy.
- Scroll-specific details or claims of exact-history superiority; the separate
  Scroll review remains later work.
- ACM and lambda-RLM outcome quantities; they do not establish the structural
  claim and already belong with their source-dependent analyses.
- Prime Agent, Fractal, AgeMem, Recuris, OpenViking, Playground, and optional
  boundary systems as extra examples once the two planned contrasts suffice.
- The advisory matrix's population statistics, its 148-versus-152 mismatch, or
  a proposal to add interface/projection axes.
- A general theory of action alphabets, authority, persistence, activation, or
  storage fidelity; cite their existing owners and retain only local boundaries.
- Claims that open programming is unrestricted or universally superior, that a
  restricted interface is necessarily deficient, or that controller gains prove
  the operation decomposition optimal.
- A closing recap or praise paragraph that adds no inference or usable test.
