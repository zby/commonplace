# Source passage (terminology check trigger)

External conversational passage that triggered this workshop. It uses "crystallization" / "progressive crystallization", which is not Commonplace vocabulary — there is no `crystallization` definition and there never was one; the concept space is covered by [distillation](../../notes/definitions/distillation.md), [constraining](../../notes/definitions/constraining.md), [codification](../../notes/definitions/codification.md), and the operational notes on [spec mining](../../notes/spec-mining-as-codification.md) and relaxing.

Mapping to current terms:

- "theory → crystallized, tested fast path" → distillation (the methodology stays prose, so explicitly *not* codification per the codification definition's exclusions)
- "progressive crystallization" (noticing repeated corner cases and promoting their handling) → spec mining, applied to the methodology document rather than code — already stated in `spec-mining-as-codification.md` ("the maturation trajectory is spec mining applied to methodology")
- "inputs that fall outside the crystallized region drop back to the expensive general layer" → the fallback side of the codification↔relaxing pair
- "the crystallized core" → the distilled core

The residue the mapping does not cover — the two-layer runtime structure itself, and the requirement that the theory ship alongside the methodology — is what the workshop explores.

The one deliberate surviving use of the word in the library is `kb/notes/system-definition-artifacts-are-crystallized-reasoning-under-context.md`, which coins "crystallized reasoning" as a distinct concept (write-time-fixed reasoning, with distillation as the operator that produces it). Whether that coinage should also migrate is out of scope here.

## The passage

> That's the right order — the idea is load-bearing enough that it deserves its own note before being compressed into an intro sentence. And it's worth noticing what you've just described: it's your crystallization pattern applied one level up. The theory is the stochastic, general-purpose layer; the methodology is the crystallized, tested fast path; corner cases are the inputs that fall outside the crystallized region and get handled by dropping back to the expensive general layer. The learning step — noticing repeated corner cases and promoting their handling into the methodology — is exactly progressive crystallization, except the artifact being crystallized is the methodology document itself rather than code.
>
> A compact way to state it for the cluster note, in three claims:
>
> 1. Theory and methodology have a generator–distillate relationship: the methodology is derived from the theory and is cheaper to execute, but strictly less general.
> 2. The theory ships *with* the methodology, not instead of it, because corner cases require re-derivation from first principles — and this only works if the agent actually understands the theory, which is the bet from the intro.
> 3. Recurring corner cases are the learning signal: when the same re-derivation happens repeatedly, its result gets promoted into the methodology. The methodology grows at its boundary, driven by use.
>
> Claim 3 also gives you something testable, which you tend to want: a corner case is "promoted" when its handling no longer requires consulting the theory — you could check that by measuring whether the agent resolves it from the methodology alone. That's a crisp criterion for when learning has occurred.
>
> One connection worth flagging in the note: this is why the theory can't be discarded after distillation even in principle — the corner-case distribution is open-ended, so the methodology never converges to covering it. The theory is the reach; the methodology is the crystallized core. That framing might eventually be the one-sentence version that fits back into the intro.
