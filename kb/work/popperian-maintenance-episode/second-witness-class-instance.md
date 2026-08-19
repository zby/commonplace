# Second witness: the class-instance-analogy defeats as priced exceptions

Recorded 2026-08-19 from a parallel session's analysis, relayed by the operator; pass report verified on disk at `kb/reports/full-pass/agent-definitions-and-sessions-break-the-class-instance-analogy/20260818T221445Z-91860b/`.

## What the gate did

The premise-decomposition gate GLOBAL-defeated three premises of `kb/notes/agent-definitions-and-sessions-break-the-class-instance-analogy.md` (since retitled by its owning session to `instantiation-alone-cannot-model-agent-learning-across-sessions.md`, committed 2026-08-19 in `2f12319a` with a redirect from the old slug):

1. "Class-based OO fixes a class before its instances exist and provides no instance-caused path for changing class behavior inherited by later instances" — defeated by Python mutating `type(self)` from an instance method.
2. "A class-based system fixes the boundary between shared class behavior and instance-local content at authoring time" — defeated by reflective class mutation and Ruby singleton methods.
3. "Instance state can only parameterize a repertoire fixed by the class" — defeated by per-instance bound methods.

The pass recast the affected section as "a limit of the common immutable/closed-world reading" — a qualification repair, since the gate's verdict vocabulary offers only DEFEATED or HOLDS.

## The pricing analysis

Every counterexample the gate cited is one the source domain itself marks as exceptional: routed through a separate reflection API or metaobject protocol, named pejoratively (monkey-patching), charged for by runtimes (JIT deoptimization), or ritualized into governance (changesets, Erlang `code_change`). A rival paradigm — prototype-based OO — exists precisely because class-based OO would not give up the guarantee. On that reading the defeated premises were ideal-type claims about the paradigm, and the counterexamples were priced exceptions, not refuters. The missing verdict is "holds as idealization, exceptions priced."

This is the operational form the honesty test lacked in the first witness: **an exception fails to refute an idealization when the domain's own practice prices it** — a marked separate interface, a pejorative name, a tooling cost, a governance ritual, or a rival paradigm founded on rejecting the ideal. The pricing must be independently attested in the domain, not authored after the counterexample lands; an unpriced counterexample — ordinary, unmarked practice in the domain — still refutes. Lakatos's anomaly-versus-refutation correction, not an exemption from criticism.

## Contrast with the first witness

The two witnesses bracket the test. In the three-way-diagnosis case, the defeating cross-effects (a schema also steering the interpreter off format violations) are arguably ordinary unmarked practice in prompt engineering — the honesty test might have refused the idealization, and the reframe would stand. In the class-instance case the pricing is richly attested in the domain and the routing stage plausibly passes (the third episode later split the test: pricing routes, adequacy — still unassessed here — decides). A vocabulary with the third verdict would have treated the two cases differently; the current vocabulary treated them the same. That asymmetry — not either case alone — is the evidence that the missing verdict does discriminating work.

## Conversion executed — outside a pass (2026-08-19)

The owning session has since restored the strong claim as a declared idealization by direct revision (at the operator's standing revise-directly instruction): the write-back section states the fixed class as class-based OO's first-order model, carries the pricing inline (marked reflection interface, the warning name monkey-patching, runtime deoptimization charges, versioned changesets and migration callbacks), and links `grounds` to the criterion note. The pricing lives in the note body deliberately — the criterion's gate question is "does the note carry the pricing?", so a bare link would not satisfy it. It also found a convergence result: read through the idealization, the paradigm contains a *fenced* version of the second relation (metaobject protocols, Smalltalk changesets, Erlang `code_change`), so what an LLM agent lacks is the enforcement, not the concept.

Status against the proposal's adoption criterion: **unmet**. The honesty test has not run inside a pass — this was content-level work. It sets up the first real run: a future full pass on `instantiation-alone-cannot-model-agent-learning-across-sessions.md` will find the pricing there to be attacked, and its premise verdicts on the idealization paragraph are the test operating against resistance.

## Ratchet observation

Author-side guidance sweeps drafts for absolutes; gate-side defeat forces qualification, reframe, or delete. All available repairs weaken. Two witnessed cases so far; in the first the narrowed claim happened to end sharper, which was the material, not the procedure. Parked as a mechanism claim inside the promoted note's scope, pending more cases.
