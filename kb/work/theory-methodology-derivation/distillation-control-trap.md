# Distillation control trap

The trap: a use-shaped artifact feels more controlled because it is smaller, clearer, and executable, while the act that made it useful can hide the information needed to control it safely.

Old `distillation` bundled four different control regimes under one attractive label:

| Regime | What controls it | Failure when hidden under `distillation` |
|---|---|---|
| Selection | provenance, consumer fit, coverage/fallback evidence | a chosen slice is treated as if it carries the whole source's authority |
| Derivation | source retention, matching, recomputation, staleness checks | a stale fast path suppresses fallback to the generator source |
| Discovery | evidence, boundary statements, derived consequences, later tests | an untested conjecture is granted rule authority at capture time |
| Authored commitment | ownership, rationale, explicit commitment or constraint authority | author judgment is disguised as source-preserving transformation |

The word `distillation` made the control surface look unified: source material goes in, a better operational artifact comes out. But the artifact's maintenance semantics depend on which regime actually produced its authority. A compressed summary, a derived skill, a conjectured rule from traces, and an author-packaged judgment can all be "use-shaped"; they do not earn trust the same way.

## Why this matters for the migration

The migration is not only a rename from `distillation` to `derivation`. If we rename too early, we recreate the same trap with a stricter word: artifacts that are really selection, discovery, or authored commitment will borrow derivation's stronger control story.

So the safe migration rule is:

> Every former `distillation` case must say what controls the resulting artifact before it is renamed.

That question precedes the replacement term:

- If fidelity is checked by re-running the source logic and comparing, call it derivation.
- If the important act is choosing a region, source, or consequence for a consumer, call it selection and preserve the coverage bet.
- If the artifact adds a claim not entailed by the source, route it to discovery's conjecture/test lifecycle.
- If the artifact packages an author's judgment without derivation or tested generalization, name it as authored commitment, accumulation, or constraining.

## Diagnostic

For each candidate replacement, ask:

1. What source change would invalidate this artifact?
2. What test would show that the artifact is wrong?
3. What fallback does the artifact suppress when a consumer trusts it?
4. Does the artifact's authority arrive immediately, or only after later use/evidence?
5. Could another agent re-derive the substantive claims from the source and stated premises, or does the artifact add a new claim?

The answers identify the control regime. They also catch mixed artifacts: split separable stages when possible; otherwise classify the artifact by its dominant maintenance regime and treat that classification as a bet.

## Consequence

The control trap explains why the trace-to-rule cases were the first serious mistake. They looked like distillation because they transformed a trace into an operational rule. But their authority did not come from source-preserving transformation. It came, if at all, from discovery: conjecturing a reusable rule, deriving consequences, and earning authority through later tests.

It also explains why derived methodology remains legitimate. A skill derived from methodology can still be derivation if its substantive claims stay inside the source's claim closure. The mistake is not producing use-shaped artifacts. The mistake is letting use-shapedness stand in for a control regime.

---

Working links:

- [receiving-vocabulary-draft.md](./receiving-vocabulary-draft.md) - applies this as an acceptance test for Wave 0.
- [derivation-selection-vocabulary.md](./derivation-selection-vocabulary.md) - grounds the split into selection, derivation, discovery, and authored commitment.
- [distillation-usage-audit.md](./distillation-usage-audit.md) - evidence that the old term bundled multiple regimes.
- [distilled-artifacts-need-source-tracking](../../notes/distilled-artifacts-need-source-tracking.md) - grounds the lineage side of the trap.
- [a derived copy of recomputable truth must be checked or absent](../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) - grounds the stale trusted-copy side of the trap.
