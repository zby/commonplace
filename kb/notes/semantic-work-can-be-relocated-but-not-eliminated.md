---
description: "A meaning-dependent judgment is never removed, only placed — moved upstream where its inputs exist (amortized) or off a bottlenecked context (offloaded); 'free at use-time' always means paid earlier"
type: kb/types/note.md
traits: [title-as-claim]
tags: [computational-model, context-engineering]
---

# Semantic work can be relocated but not eliminated

Some of a system's work is mechanical — matching codified features, following a rule — and a better algorithm can do less of it. Some is _semantic_: a judgment about what content means or which case is relevant, one that cannot be settled by matching features already present. The two behave differently under optimization. Mechanical work can be reduced toward zero; a meaning-dependent judgment cannot be removed from the point where its output is needed. It can only be **placed** — paid at a different time, or by a different processor. Wherever such a judgment looks free or deterministic at the point of use — mechanical, deriving no fresh meaning — it was paid earlier: for this case, or for the regularity it falls under.

What lets a judgment move is the availability of its inputs. It can be pre-paid upstream only where the inputs it depends on already exist; otherwise it falls due at use-time. [Codification](./definitions/codification.md) is the limiting case: resolve a meaning-dependent decision once and freeze the result into a symbolic rule, so every later check is mechanical. A rule-ready signal — a path, a tool event, a typed field — is precisely this: semantic work already done and compiled into a feature a rule can match, which is why [rule-based selection needs that signal to pre-exist](./rule-based-context-selection-needs-a-pre-existing-signal.md) rather than conjuring it.

Placement is free along two axes, and they answer to different scarce resources. Moving a judgment **upstream in time** lets its result be reused — pay once, serve many — which is amortization: a cache, a built index, [a frontloaded instruction result](./frontloading-spares-execution-context.md). Its scarce resource is per-use compute, driven toward zero. Moving a judgment **off a loaded context** onto another processor is offloading; here the scarce resource is not total compute but the consuming agent's context and attention. Offloading can raise total work — a whole separate model call — and still pay, because it protects the bottleneck. The cases sort onto the axes: frontloading does both (pre-computed _and_ out of the execution context); a side model that decides what to push is pure offloading, paid every time but off the main agent; an agent that pulls for itself is the opposite, paying the judgment inside the very context that is scarce, cheap only because it is already reasoning there.

It is tempting to call this a conservation of semantic work, and the phrase is a fair informal handle — but the physics reading misleads, because the total is not constant: amortization lowers it per use, offloading can raise it in aggregate. The real invariant is informational: a system cannot emit reliable information about a case without something upstream having accessed that case, or the regularity it falls under. This is why the ceiling holds even when the specific input is novel — a trained model or a market price answers correctly only where the new case falls under a regularity already paid for; outside it the output is not free but absent or unreliable. A meaning-dependent judgment therefore cannot be driven to zero at the point where its output is needed, except by having paid, upstream, for the case or its regularity. Relocation buys secondary goods — lower per-use cost, a relieved bottleneck — never the judgment's disappearance.

The useful residue is a question to put to any design that presents a meaning-dependent step as free or deterministic: where was the judgment paid, and what did it need to access? A good answer names an upstream point; a bad one exposes hidden use-time cost or a lossy shortcut — and abandoning correctness is not elimination, only a different price.

## Relevant Notes

- [frontloading spares execution context](./frontloading-spares-execution-context.md) — evidenced-by: the time-axis case — pre-compute where inputs are known — that instantiates this rule

- [rule-based context selection needs a pre-existing signal](./rule-based-context-selection-needs-a-pre-existing-signal.md) — evidenced-by: the context-selection case; its pre-existing signal is semantic work already paid upstream

- [codification](./definitions/codification.md) — mechanism: the operation that freezes a resolved judgment into a rule a later check can match mechanically

- [context efficiency is the central design concern in agent systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — grounds: the scarce-context premise that makes offloading worth net-more work

- [LLM recompute cost inverts the store-vs-recompute default](./llm-recompute-cost-inverts-the-store-vs-recompute-default.md) — extends: develops the amortize/time axis for an LLM consumer, where recompute is dear

- [Increasing computational autonomy relocates human effort to the frontier instead of reducing it](./increasing-computational-autonomy-relocates-human-effort.md) — contrasts: the same relocation-not-elimination shape with a different conserved quantity — human effort rather than a meaning-dependent judgment
