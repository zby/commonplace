# Case packet

Neutral case identifier: case-d45ce3e679afe0

The possible directed relationship from Artifact A to Artifact B is under review.

## Artifact A

# Commitment, not derivation, creates new ground truth

An artifact produced from source material stands in one of two relations to it, and this KB's [lineage vocabulary] keeps them apart deliberately. **Derivation**, in the narrow registered sense, means the artifact's substantive claims are recoverable from the source plus its declared consumer goal — nothing added. Every other production adds something the source does not determine: a generalization beyond the evidence, a decision among live options, one reading selected from a space of admissible ones. Call the act that fixes such an addition in a retained artifact a **commitment**.

The claim: this boundary settles which artifact is ground truth afterwards. A derived artifact leaves its source as ground truth and remains a dependent copy — when the source revises, the copy is stale and re-derivation is authoritative. A committed artifact *becomes* ground truth for what it adds, at the moment of commitment, and its raw material demotes to provenance. The maintenance and disposal consequences follow from that inversion, because every recompute-style repair assumes the source still holds the answer — and on the commitment side it never does.

## The discriminator is what gets added, not what gets lost

The tempting reading is that derivation keeps the information and commitment loses some. That reading is wrong, and getting it wrong misfiles most real cases. A hash is extremely lossy and fully derived: the source determines the digest, and any conforming re-derivation reproduces it. Loss is orthogonal; what matters is whether the source *determines* the artifact's substantive content.

The clearest modern case is generated code. Since [agentic systems interpret underspecified instructions], a natural-language spec admits a space of valid programs and the model collapses that space to one — a projection, not a compilation. Every resolution the spec left open arrives in the output as content the source does not entail, and no fact about the spec records which resolutions were taken. Kept code is therefore not derived from its prompt; it is a committed interpretation of it — which matches how such artifacts are actually treated: the code, not the prompt, is what gets debugged, maintained, and trusted.

Determinism of the producer does not move this line. An LLM at temperature zero returns the same output every time, and the output's unentailed content is still unentailed — it is fixed by source *plus* model, prompt, decoding, and runtime, not by the source. Pinning the arbiter reproduces one arbitration; it does not make the source determine the answer. Freezing indeterminism and resolving underspecification are separate moves, and only content the source determines is derived.

## Whoever resolves the free choice is the committer

The commitment side is usually discussed as an LLM phenomenon, but the argument never uses the arbiter's substrate — and in this KB the committer is very often a person. Anything that resolves the free choice occupies the same position:

- **A human accepting a decision.** Nothing in a design proposal determines which option wins; the deciding *is* the addition. An accepted ADR is therefore not derived from the proposal it adopted — re-reading the proposal does not regenerate the decision. The [discovery lifecycle] names this phase exactly: acceptance is *gated commitment*, a consuming workflow's recorded judgment that evidence meets a criterion — a fact about the judgment, not a consequence of the evidence.
- **A human attesting.** `user-verified: true` is recoverable from nothing in the note it sits on; it records a person's judgment, added from outside the text. That is why a substantive edit must strip it and only an explicit act can re-grant it — the field is a commitment wearing a frontmatter field's clothes, and treating it as a checkable mark would be the category error described below.
- **A human keeping a good output.** [Storing an LLM output is constraining]: the generator produced candidates, and the keeping resolved which one becomes the artifact.

So the claim classifies productions, not producers. A generated index and a promoted synthesis note differ in kind though both are machine-produced; an ADR and a completeness [mark] differ in kind though both are authored by hand.

## Two boundaries, three zones

Derivation itself is graded, and the grading must not be confused with the commitment boundary. [Methodology and its theory form a two-layer execution system] splits derived content by verification method: **mechanical** fragments, where a machine re-derives and a validator compares — these are recomputable copies proper — and **judgment-checked** derived natural-language, where the claims are recoverable from the source but re-derivation and comparison take judgment, so the regime is managed staleness rather than a deterministic check.

Both zones sit on the derivation side of the ground-truth question: a judgment-checked summary that restates its source in new words has added no claims, and when the source revises, the summary is stale and the source wins. The commitment boundary is different in kind, not merely harder to check — on its far side the artifact outranks its raw material, and "stale against the source" stops being a meaningful state because the source was never the authority for what was added.

Keeping the two boundaries apart prevents two opposite misfilings: judgment-checked derivation mistaken for commitment (it is not — nothing was added, and the source remains authoritative), and a committed artifact mistaken for a checkable copy (there is no derivation to check it against).

## The maintenance and disposal split

|  | derivation | commitment |
|---|---|---|
| substantive content | recoverable from source plus declared consumer goal | includes resolutions the source does not determine |
| ground truth after production | the source | the artifact; source demotes to provenance |
| maintenance rule | checked-or-absent where mechanical; managed staleness where judgment-checked | supersession |
| repair on drift | recompute, or judged re-derivation | a new commitment naming the old |
| deletion cost | recomputation work — bounded and mechanical, or dear but claim-preserving | irrecoverable loss of the only record |
| worked instances | marks, generated indexes, duplicated build assets; derived summaries and reshaped natural-language | ADRs, notes promoted from workshops, verification attestations, kept generated code |

Three consequences do real work.

**Enforce-or-omit is a mechanical-zone rule.** [A derived copy of recomputable truth must be checked or absent] rides on the deletion column: absence costs a recomputation, a false copy costs silent unbounded wrongness, so hand-maintained-and-trusted is forbidden. Its precondition 1 — mechanical re-derivability — is the mechanical zone's admission test stated as an availability condition. Pushed past the commitment boundary the rule degenerates rather than weakens: with no derivation to check against, "checked or absent" reduces to "absent", which deletes the only copy of something no source recovers. The rule is not weaker there; it does not apply there.

**Supersession is a commitment rule, and demanding it of a derivation is over-ceremony.** You do not write a decision record to regenerate an index. Supersession exists because a superseded commitment is not wrong-relative-to-a-source — it was the ground truth for its moment, and only a later commitment can displace it. That is history, and history is not re-derivable.

**The boundary predicts disposal, and the KB's own two disposal decisions split along it.** Committed generated indexes were deleted outright and regenerated at build time from note frontmatter ([ADR 025]) — safe, because the derivation survives the file. Adopted proposals were archived rather than deleted ([ADR 056]) — because a proposal's option space, forces, and free choices are themselves committed records of a design conversation, and adoption does not make the proposal derivable from its ADR. Two originals, neither recoverable from the other, so the only live question is attention tier rather than existence. The two decisions were reached independently, on different artifact kinds, and neither invoked this distinction; that they land on opposite operations exactly where the boundary says they should is what makes it more than a relabelling of the cases that produced it.

## Regime membership attaches to the region, not the file

A tag-README carries curated editorial prose *and* validator-enforced `complete`/`covered_by` marks. The marks are mechanical derivations; the curation is a commitment. Both live in one file, and the file's disposal behaviour is per-region: dropping a mark costs a reader one scoped sweep, dropping the curation destroys editorial judgment nothing re-derives. This is why [ADR 026] could put a validator behind the marks without pretending to validate the prose around them. The [lineage vocabulary] handles the same fact at the artifact scale by labelling a mixed artifact by its dominant regime — an explicit, revisable call. When classifying, ask which regime a given *claim inside* an artifact belongs to; the file is often mixed.

## The boundary is crossable by committing once

A recurring arbitration can be retired by codifying it — which is what [progressive constraining] does: observe which resolution stabilizes across many runs, then commit that resolution to an artifact with precise semantics. The codified artifact is itself a commitment — it becomes the new source — but everything regenerated from it afterwards is derivation, with recompute available as the repair. Commit once, derive thereafter. The reverse move — relaxing a codified rule back into judgment — reopens the free choice and forfeits the repair, which is sometimes worth it and never a maintenance improvement.

That also bounds the promotion: until the arbitration is actually codified, treating its outputs as derived is aspiration, and the aspiration is the exact failure mode enforce-or-omit warns about — a trusted copy with no check behind it.

## Scope

- **Judged re-derivation is not recompute, and re-examination is neither.** Re-deriving judgment-checked natural-language reproduces claims in possibly different words; it stays inside derivation. [Retaining the episode keeps a distilled rule re-derivable] describes a third thing: going back to the evidence behind an *abstracted* — committed — rule and judging whether the generalization survives. That is real recourse, and it is a fresh arbitration over retained provenance which may disagree with what it re-examines; a recompute cannot.
- **The managed-staleness machinery is taken as given.** [Lineage recorded at the source] surfaces downstream artifacts when a source changes, with judgment doing the verification for the non-mechanical zone. This note adds no machinery there; it says why nothing on the commitment side can be repaired by that machinery or any validator.
- **Neither relation is better.** The claim is that the maintenance operations are not interchangeable, not that derivation should be preferred where a judgment is what the work needs.
- **A derivation still needs its ground truth to exist at check time.** Where the source is destroyed or was never recorded, recompute is unavailable in practice even though nothing was added — [history has one chance to become checkable].

## Open Questions

- Is there a third relation for artifacts determined by the source *plus* evidence the run itself generates? Such an artifact adds nothing by judgment, yet is reproducible only by re-running the world — which is neither recompute nor supersession.
- Does anything checkable distinguish the relations, or must membership always be declared? A validator can confirm a claimed derivation reproduces its copy, but nothing detects a commitment misfiled as a derivation except its first silent mismatch.
- What retires a commitment when no successor commitment is coming — the case where a note simply stops being true and no one has decided what replaces it?

---

Relevant Notes:

## Artifact B

# Agentic systems interpret underspecified instructions

*A theoretical framing for LLM-based agentic systems — enough conceptual machinery to clarify why certain design choices make sense.*

## Two Distinct Phenomena

LLM-based systems differ from traditional programs in two ways that are often conflated but are conceptually distinct:

**1. Semantic underspecification.** Natural language specifications don't have precise denotations. "Write a summary" admits a *space* of valid interpretations — different lengths, emphases, structures. This is a property of the specification language itself, not the engine.

**2. Execution indeterminism.** The same prompt can produce different outputs across runs due to sampling (temperature > 0). This is a property of the execution engine — conceptually simpler than semantic underspecification, and largely eliminable via temperature=0, though implementation details (floating-point non-determinism, batching, infrastructure changes) make true determinism hard to guarantee in practice. Deployed systems run with indeterminism anyway, and often benefit from it.

The two are not entirely orthogonal — indeterminism is the mechanism by which different interpretations get surfaced across runs — but they are fundamentally different in kind. The first is semantics; the second is engineering.

### Indeterminism obscures the real difference

Counterintuitively, indeterminism *hides* the deeper issue rather than revealing it. Because outputs vary across runs, people attribute the variation to randomness — "it's stochastic" — and reach for familiar tools: temperature tuning, retries, sampling strategies. The stochastic framing is comfortable precisely because it avoids confronting the real difference from traditional programming.

If LLMs were deterministic, you'd get one stable output for a given prompt — but you'd have to ask: *why this interpretation and not any of the other equally valid ones?* That question forces you to see that the specification language doesn't have the same semantics as a formal programming language. The indeterminism lets you avoid that question by explaining everything as noise.

## Spec-to-Program Projection

A natural-language spec admits multiple valid programs. The LLM picks one:

```
Spec → choose interpretation → execute on input → output
```

The spec-to-program mapping is one-to-many — a semantic property, not a probabilistic one. Even a deterministic LLM would face it: it would always pick the same interpretation, but the user couldn't predict which one from the spec alone.

This makes LLMs different from compilers — but the contrast has to be stated carefully, because production compilers don't have complete formal semantics and verified equivalence proofs either. Most compiler stacks define equivalence operationally and imperfectly: language standard, compiler, target architecture, flags, and implementation-defined edges all matter. The real distinction is one of aim: a programming-language implementation aims at a unique operational semantics for the relevant program once those parameters are fixed, so any divergence counts as a bug, a portability limit, or explicitly unspecified behavior.

An LLM has no such aim. It too has operational behavior once fixed to a model, prompt, context, decoding settings, and runtime — but that behavior is not a model-independent semantics of the natural-language prompt that another conforming interpreter is expected to preserve. The prompt still admits a space of valid interpretations, and the LLM performs a *projection*: it collapses that space to one concrete program.

Nor could the aim be adopted. For programming languages, formal semantics is a plausible ideal even when practice falls short. For ordinary natural-language instructions it is not attainable even in principle: a general language rich enough to talk about truth, meaning, and computation runs into Tarski/Gödel/halting-style impossibility results, so a complete executable semantics would have to drop that openness and become a constrained formal language.

The two phenomena layer on top of each other: the projection picks an interpretation (semantic underspecification), then execution of that interpretation may vary across runs (indeterminism). But the more interesting variation comes from the first source — qualitatively different strategies, not noisy executions of the same one.

### Example: "Refactor for Readability"

Ask an LLM coding assistant to refactor a function for readability. Valid interpretations include:

- Extract helper functions
- Rename variables for clarity
- Restructure control flow (loops → comprehensions)
- Add comments explaining intent

These aren't noisy variations of *one* strategy — they're different *interpretations* of "readability." The spec doesn't pick out a unique transformation; the space of valid approaches is genuinely plural.

This reframes prompt engineering: it's about narrowing the space of valid interpretations, not debugging a fixed program.

## Narrowing the Interpretation Space

The usual tools are system prompts, few-shot examples, tool definitions, output schemas, conversation history, and temperature. In practice it's hard to determine which phenomenon a given mechanism addresses — a more detailed system prompt might narrow the interpretation space, or it might just make one interpretation more likely without eliminating the others. The line between "disambiguating the spec" and "biasing the engine" is rarely clean.

Temperature is often cited as purely an indeterminism control, but it's subtler than that. Lowering temperature concentrates the sampling distribution — which can change *which interpretation* you see, not just how noisily you see it. At temperature=0 the LLM still picks one interpretation from the space the spec admits; you just get the same one every time. This is why lowering temperature alone doesn't solve the "wrong interpretation" problem — it eliminates variation without ensuring the remaining interpretation is the one you wanted.

None of these tools eliminates ambiguity entirely. Natural language specs remain underspecified even under maximum constraint. So real systems don't just manage underspecification *within* LLM components — they also manage the transitions between LLM and code.

## Boundaries

Agentic systems interleave LLM components and code. When execution crosses from LLM to code (or back), both phenomena change regime: LLM components carry semantic underspecification and indeterminism, while code is treated as precise and deterministic inside the chosen runtime contract. Each crossing is therefore a natural **checkpoint** — the deterministic side doesn't care how it was reached, only what arguments arrived — which anchors debugging, testing, and refactoring against the mess upstream. See [LLM↔code boundaries are natural checkpoints].

Boundaries aren't fixed. As systems evolve, logic moves across them.

## Constraining and Relaxing

Components exist on a spectrum from underspecified semantics (natural language, LLM-interpreted) to precise semantics (formal language, deterministic code). Logic can move in both directions.

**Constraining**: Replace an LLM component with a deterministic one. This does two things simultaneously: it **resolves semantic underspecification** by choosing one interpretation from the space the spec admits and committing to it in a language with precise semantics, and it **removes execution indeterminism** by eliminating sampling noise. Both matter in practice, but the semantic commitment is the deeper operation.

**Relaxing**: Replace a deterministic component with an LLM-interpreted one. Describe new functionality in natural language; the LLM figures out how to do it.

```
Underspecified (flexible, handles ambiguity)  ——constrain——>  Precise (reliable, testable, cheap)
Underspecified (flexible, handles ambiguity)  <——relax———  Precise (reliable, testable, cheap)
```

### Why constrain?

Constraining a pattern to code has four benefits — three quantitative, one qualitative:

**Cost.** LLM API calls are priced per token. A simple operation like sanitising a filename might cost fractions of a cent, but at scale those fractions compound. The same operation in code costs effectively nothing.

**Latency.** Every LLM call involves network round-trip plus inference time. Even fast models add hundreds of milliseconds. Code executes in microseconds.

**Reliability.** Deterministic code returns the same output for the same input, every time. No hallucination, no refusal, no silent behavior changes when the underlying model is updated.

**Enforcement.** Some properties — scope rules, type rules, contract checks, invariants — only exist if a deterministic interpreter checks them. Natural-language instructions can describe them but can't enforce them; LLM adherence is always probabilistic. Reliability is about output consistency on typical inputs; enforcement is the binary fact that a constraint holds for *all* inputs. For properties that require enforcement, the constraining move is not optional — the alternative is to go without the guarantee. Scope is one such property ([LLM context is composed without scoping]); bookkeeping is another ([scheduler-LLM separation exploits an error-correction asymmetry]).

The tradeoff: code requires you to commit to one precise interpretation, while LLMs let you specify *intent* in natural language and defer the choice of interpretation to runtime. That's why constraining should be progressive — wait until patterns emerge before committing to a specific semantics.

LLM code generation is itself a constraining move, but only a one-shot form — freezing a single projection of the spec into code. Progressively extracting only the patterns that stabilize across many runs is a different mode with different tradeoffs; see [progressive constraining commits only after patterns stabilize]. For the wider gradient of constraining techniques — from prompt restructuring through evals to deterministic modules — see [codification]. Either way, **version both spec and artifact** — regeneration is a new projection, not a deterministic rebuild.

### Relaxing as extension

The common path for relaxing is **extension**: you need new capability, describe it in natural language, and it becomes callable. The rarer path is **replacement**: rigid code is drowning in edge cases, so you swap it for an LLM call that handles linguistic variation.

Real systems need both directions. A component might start as an LLM call (quick to add), constrain to code as patterns emerge (reliable and fast), then grow new capabilities via relaxing. The system breathes.

## Testing and Debugging

The two phenomena create different challenges for testing and debugging.

**Testing**: Execution indeterminism means you can't rely on assertion equality for LLM outputs — you need to run the same input multiple times and check that outputs fall within acceptable bounds. In practice this looks more like sampling and checking invariants than formal hypothesis testing, but the principle holds: you're characterising a distribution, not verifying a point. Semantic underspecification adds a second obligation: verify that the *space* of valid interpretations is acceptable, not just that individual outputs look right. Every piece you constrain escapes both obligations and becomes traditionally testable — because you've committed to one interpretation in a precise language.

**Debugging**: the two phenomena suggest different fixes — retry for indeterminism failures, rewrite the spec for underspecification failures. Mistaking one for the other wastes effort. See [LLM debugging starts with retry-versus-rewrite triage].

## Design Implications

Treating agentic systems as interpreters of underspecified instructions suggests:

1. **Be explicit about semantic boundaries** — know where you're crossing between precise and underspecified semantics
2. **Enable bidirectional refactoring** — design interfaces so components can move across the boundary without rewriting call sites
3. **Narrow interpretations where reliability matters** — use schemas, constraints, and deterministic code on critical paths
4. **Preserve ambiguity where it helps** — don't over-constrain creative or genuinely open-ended tasks
5. **Version both spec and artifact** — regeneration is a new projection, not a deterministic rebuild
6. **Design for unpredictable interpretation** — the LLM may resolve ambiguity differently than you expect
7. **Constrain progressively, relax tactically** — start with underspecified for flexibility, commit to precise semantics as patterns emerge

---

Relevant Notes:

- [learning-theory] — parent index: learning mechanisms, oracle theory, memory architecture
- [llm-code-boundaries-are-natural-checkpoints] — splits from this note: the boundary-as-checkpoint argument expanded with debugging, testing, and refactoring applications
- [progressive-constraining-commits-only-after-patterns-stabilize] — splits from this note: the one-shot vs progressive distinction for LLM code generation as a constraining mode
- [llm-debugging-starts-with-retry-versus-rewrite-triage] — splits from this note: the debugging heuristic derived from the two-phenomena model
- [constraining] — defines the narrowing mechanism this note frames theoretically
- [codification] — the constraining gradient from prompt tweaks to deterministic modules
- [context efficiency is the central design concern in agent systems] — intensified by: underspecification means extra context distorts interpretation, not just wastes space — making context scarcity qualitatively worse than traditional resource constraints
- [interpretation errors are failures of the interpreter not the spec] — bounded by: the two-phenomena model assumes a perfect interpreter; real LLMs add a third failure mode with different remedies

Sources:

- Ma et al. (2026). [Prompt Stability in Code LLMs] — strongest empirical evidence for the two-phenomena separation: emotion/personality prompt variations change code output while holding task spec constant, isolating underspecification (which interpretation?) from indeterminism (which run?)

## Under-review context phrase

the projection-versus-compilation distinction behind the generated-code case, including why temperature-zero determinism does not entail the additions
