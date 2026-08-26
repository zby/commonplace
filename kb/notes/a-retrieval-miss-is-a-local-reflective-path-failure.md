---
description: "A missed relevant artifact leaves its represented aspect inert for the affected task and discovery route, while other loading paths and reflective aspects can remain causally connected"
type: kb/types/note.md
traits: [title-as-claim]
tags: [foundations, computational-model, self-improving-systems]
---

# A retrieval miss is a local reflective-path failure

In a [reflective system](./definitions/reflective-system.md) whose causal connection runs through discovery over retained artifacts, a **retrieval miss** is a failure to surface a relevant part of the self-representation for a particular task. It breaks the causal path through that discovery route for the represented constraint or aspect the task needed. The failure is local before it is global: another mandatory or discovery path may still surface the same artifact, and other represented aspects may remain causally connected, so one miss does not by itself make the whole system non-reflective.

Discovery can therefore sit *inside* the reflective architecture rather than alongside it. A process searches the artifacts, finds those bearing on its task, and lets what it found shape its behavior. The search recipes, frontmatter fields that make an artifact findable, indexes that shortcut the search, and mandatory loading rules are distinct wires along which the self-representation can act. Editing an artifact reaches later behavior through any wire that surfaces it.

A represented constraint that no available path surfaces for a task is inert for that task: it is written, it may be true, and it changes nothing about the operation that needed it. The miss is therefore more than inconvenience. It breaks that represented aspect's causal path into that operation. The local unit matters: the same artifact may remain operative for another task, and the same task may receive it through a redundant wire.

## The failure is worst where the wire is trusted

The sharpest case is a membership claim that is asserted rather than enforced, [since stale indexes reduce discovery when they suppress fallback search](./indexes-lower-recall-when-they-suppress-retrieval-that-would-find-more.md). A head that says *this lists every note with the tag* tells an exhaustive consumer to stop looking. If members are missing, the claim cuts the wire precisely where a process was relying on it — and that process cannot tell, because the whole point of trusting the claim was to skip the check that would have caught it. Another process that runs the full search can still find the member, so the failure belongs to the trusted shortcut's path rather than to the system as a whole.

The [Commonplace reference case](./evidence/commonplace-as-a-reflective-system.md) shows this failure being converted from an asserted completeness claim into an enforced one.

## Best-effort discovery differs from declared-input consumption

Retrieval-mediated connection is weaker than deterministic declared-input consumption in one specific way: relevance-based discovery is best-effort. A compiler, validator, or loader can enumerate the inputs its specification declares and process each under defined rules; whether an input changes the result still depends on those rules. A search cannot enumerate a complete relevance-defined input set before interpreting the task. It consumes what its query happens to surface, and relevance is an inference.

Either path can fail. A build graph can omit a dependency, a cache can be stale, a declared scope can be wrong, or a consumer can be buggy. The contrast is therefore not perfection against fallibility. It is enumerated processing over declared inputs against relevance-based discovery. The former can make consumption exhaustive relative to a declared scope; the latter cannot assume its query exhausts what the task might need.

A system can strengthen the wire — enforcing a membership claim rather than asserting it, adding a field that makes an artifact findable, correcting a search recipe observed to miss a member. It cannot assume relevance-based discovery holds by construction. Discovery can silently omit a needed artifact even when storage and query execution behave exactly as specified, because the specification does not enumerate relevance in advance; declared-input consumption instead fails when declaration, delivery, or processing is wrong.

[Memento-Skills](../sources/memento-skills-let-agents-design-agents.ingest.md) supplies a bounded external measurement of this wire. In its real-trajectory router evaluation, the behavior-trained Memento-Qwen router raised route-hit rate from 0.53 for the Qwen3 embedding baseline to 0.58 and judge success from 0.79 to 0.80. Route hit means that the top-ranked skill was appropriate for the task; judge success means that the full trajectory solved it. This router comparison changes the routing method and reports both outcomes together; it does not isolate the downstream effect of the selected skill. For this note, the one-point judge-success difference is therefore evidence about the retrieval-to-success association, not proof that the selected skill causally shaped the later action. Uptake still needs a separate perturbation or with/without test.

The same [reference case](./evidence/commonplace-as-a-reflective-system.md) records the stronger check exposing and repairing a blind spot in the natural-language retrieval recipe.

## Scope

- The claim is relative to a represented aspect, task, and causal path in a retrieval-mediated system. A miss narrows the aspects and operations reached by that path. It defeats the system-level reflection attribution only if no qualifying causal path remains inside the declared frame.
- A mandatory loading path can preserve the causal connection despite a search miss. Where a self-representation is consumed through enumerated declared inputs, retrieval is not the wire and this failure mode does not arise, though declaration and consumption can fail in their own ways.
- Successful retrieval is not sufficient for causal connection. A found artifact can still be misread, ignored, or overridden — [behavioral authority](./definitions/behavioral-authority.md) names the consumer, channel, and force that have to hold downstream of discovery.

---

Relevant Notes:

- [Reflective system](./definitions/reflective-system.md) — grounds: supplies the path-relative causal-connection criterion this note applies to retrieval
- [Stale indexes reduce discovery when they suppress fallback search](./indexes-lower-recall-when-they-suppress-retrieval-that-would-find-more.md) — mechanism: why a trusted-but-incomplete membership claim is the sharpest form of the failure
- [Behavioral authority](./definitions/behavioral-authority.md) — extends: the consumer, channel, and force that must hold after an artifact is found
- [Commonplace as a reflective system](./evidence/commonplace-as-a-reflective-system.md) — evidenced-by: the observed trace where a symbolic check corrected the natural-language search recipe that had been missing a member
- [Memento-Skills](../sources/memento-skills-let-agents-design-agents.ingest.md) — evidenced-by: in the reported router comparison, behavior-trained routing improves both route hits and downstream success while causal uptake after retrieval remains untested
