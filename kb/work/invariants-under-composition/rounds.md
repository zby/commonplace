# Five-round investigation record

Commission: fresh-context brainstorming and separate critique, followed by parent revision and cleanup. Agent suggestions are proposals. This record retains decisions and failed candidates rather than transcripts.

## Round 1 — Conditional guarantees and actual assumptions

Fresh brainstorm: `round1_brainstorm`; independent fresh critic: `round1_critic`. Both read-only; parent integrated and cleaned.

- Added role: assign a component's needed assumption to an actual boundary, rather than infer composition from local tests. Primary reading: Abadi–Lamport §§1–2.2; parent checked the circularity warning in §4.3.1.
- Critique changed the draft: review coverage of published bytes and baseline concurrency are different requirements. Explicitly separated them; an old capture is not automatically an invalid finalization.
- Added a bounded edit check: generation-guard changes reopen transition-eligibility evidence, not every aspect of reviewer quality. Completeness of identified dependencies remains defeasible.
- Cut: the unworked shared-conversion example and generic “check everything” warning. Kept the progress counterexample only to prevent a safety argument from claiming termination.
- Cleanup outcome: one requirement-setting case, one publication case, one documented baseline-transition comparison. No new umbrella terminology or library change.

## Round 2 — The interval from checking to use

Fresh brainstorm: `round2_brainstorm`; fresh critic: `round2_critic`.

- Added role: test whether an assumption survives between its check and its consequential use. The publication race supplies a concrete pause/edit/resume probe.
- Critique tightened approval to recorded acceptance of exact immutable bytes, and required a state invariant. Renamed the repaired operation check-and-publish to make the atomicity boundary explicit.
- Bounded enumeration: C before P permits CEP, CPE and ECP; only CEP violates. Both orders of edit versus atomic check-and-publish preserve the invariant. This is model checking of a toy transition system, not runtime validation.
- Cut: duplicate formatter story as independent evidence, repeated caveats and a second taxonomy called rely/guarantee. Retained baseline concurrency as a different property.
- Cleanup outcome: one interval probe and one named obligation; no claim that every concurrent composition needs this exact mechanism.

## Round 3 — Small effects, margins and invariant sets

Fresh brainstorm: `round3_brainstorm`; fresh critic: `round3_critic`.

- Added role: a compact affine counterexample separates convergence from remaining inside a required interval. Decimal arithmetic confirms the one-step violation (0.1001 > 0.100).
- Critique changed the result: negative input is safe only for the illustrated next step; repeated negative input eventually crosses the other boundary. A current-state budget differs from an input bound preserving the entire interval; the latter is 0≤u≤0.010 for this model.
- Kept exact-byte versus semantic preservation as a separate KB choice, not a claim that numeric margins model text meaning.
- Parked small-gain machinery, chaos and catastrophe theory. None currently changes a KB check beyond the simpler interval example. Reentry needs a concrete state/interaction model and an obligation not already handled.
- Cleanup outcome: one numerical discriminator, no nonlinear-system taxonomy and no transfer of a continuous-control theorem to prompts.

### Retained quantitative counterexample

For dimensionless xₖ₊₁=0.9xₖ+u, x₀=0.099 and required interval [0, 0.100], u=0.011 gives x₁=0.1001 although trajectories converge to 0.110. The one-step upper input budget is 0.0109. A constant input preserves the whole interval for every initial state in it exactly when 0≤u≤0.010 (check both endpoints). At u=−0.011 the next state is 0.0781, but repeated negative input eventually crosses the lower boundary. Decimal arithmetic checked the stated values; the endpoint argument establishes the interval bound for this affine model. This is neither a KB dynamics model nor a claim about chaos.

## Round 4 — Reuse an argument, re-establish its affected premises

Fresh brainstorm: `round4_brainstorm`; fresh critic: `round4_critic`.

- Added role: a mutation probe challenges an alleged dependency boundary. A one-input Python example produces identical display text with deepcopy and alias variants; only the alias variant changes the caller's nested state.
- Critique separated old test results from an argument that remains applicable after its premises are re-established. Removed display-equivalence checking from the publication obligation because the publisher never consumes display text.
- Added a bounded completion condition: every identified affected premise has support, replaced support or an unresolved disposition; no discovered relevant mutation route is left unexamined. Unresolved premises prevent the preservation claim, while omissions can reopen the boundary later.
- Cut: separate generic impact-boundary section and duplicate dependency warnings. Merged its useful generation-guard example into argument reuse. Storage separation is not imported as semantic independence of prose.
- Cleanup outcome: one repair decision procedure with a concrete falsification probe; no new refinement relation or claim of complete dependency discovery.

## Round 5 — A held-out requirement that compares executions

Fresh brainstorm: `round5_brainstorm`; fresh critic: `round5_critic`.

- Added role: name the observations and runs that a requirement compares. Correct per-output facts and shape do not detect a confidential bit encoded in report order.
- Critique narrowed “input independence” to the chosen public observations and bit; explicitly distinguished unordered facts from ordered output. Equal or unequal samples and fixed-seed probes do not establish stochastic distributional equality.
- Executed finite pair: both secret-dependent outputs pass fact checks, but differ by order; fixed public ordering passes the pair. No deployment confidentiality claim follows.
- Added the compact change-to-probe table. It is a starting aid, not an exhaustive proof procedure.
- Cut/merged: moved the full affine calculation out of the main account; moved parked mathematical machinery into source assessments; removed repeated role paragraphs and generic warnings. Kept baseline concurrency because it distinguishes two actual checking obligations.
- Cleanup outcome: five rounds completed; main contribution is a set of discriminating probes and a bounded premise-disposition process. No new theory vocabulary, library promotion or runtime change.

## Next bounded test, not yet run

Use two public documents and a shared cache across two calls. Give the formatter public ordering, but let cache population depend on the first call's confidential bit. Enumerate the finite histories from a fresh cache and compare complete public output sequences while varying only that bit. Include a control whose cache depends only on public information. This tests whether the method notices dependence carried through retained state after the direct ordering leak is removed. Specify the cache and observation contract before testing. It does not call for a general security framework or a real-model evaluation yet.
