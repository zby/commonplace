---
description: "When a summary cannot license a reliability-compliant stop, the authoritative fallback remains in the path; only fallback work the summary removes can offset its own cost"
type: kb/types/note.md
traits: [title-as-claim]
tags: [context-engineering, document-system]
---

# An insufficient summary precedes the source rather than replacing it

A summary saves read cost only by removing work from the authoritative fallback that would otherwise answer the same question at the same reliability. This note calls that fallback the **source path**. It may be the source artifact or an equivalent authoritative route, such as a checked interface. If a cheaper authoritative route can close the question, that route—not whichever artifact a reader happens to prefer—is the right baseline.

Full substitution requires two things. First, the summary's answer, together with the provenance and verification available to the consumer, must license the action at the reliability the task requires. Call this **sufficiency**. Second, the routed path must actually stop at the summary instead of reading the fallback anyway. If the summary is insufficient, every reliability-compliant route retains source-path work. The summary then precedes the source path rather than replacing it, though it may still narrow or shorten the remaining work.

This claim concerns reliability-compliant paths, not whether readers notice that an answer is inadequate. A reader can trust an insufficient summary, skip the source path, and act. That unsafe substitution appears cheap only because the route did not buy the required reliability; it does not show that the summary supplied an adequate answer cheaply.

## Count removed fallback work, not compression

Using a whole-artifact compression ratio as a proxy for read-cost savings assumes that one artifact substitutes for the other. Instead, fix a **cost currency**—such as tokens, reader time, or money—and compare the summary-routed path with the direct source path for the same question and reliability.

Define fallback work removed as the signed difference between source-path work on those routes. The value is positive when the summary leaves less fallback work, zero when it leaves the fallback unchanged, and negative when it creates correction or reorientation work. The resulting ledger is:

> read-cost value = fallback work removed − summary consumption cost

A sufficient summary whose route stops removes all fallback work for that question. An insufficient but useful summary may still reduce discovery, selection, interpretation, or verification work. A pure addition leaves the fallback unchanged, so its read-cost value is negative by exactly its own consumption cost. Insufficiency therefore rules out *full* substitution, but does not by itself determine whether the ledger is positive or negative.

A [pointer is deliberately designed to precede a source](./pointer-design-tradeoffs-in-progressive-disclosure.md). Its success may be narrowing rather than task closure. It earns partial-substitution credit only for the discovery, selection, interpretation, or verification work it actually removes.

Only attempts routed through the summary incur its cost. When readers cannot know its coverage or reliability in advance, they pay that cost before deciding whether to stop. A cheap advance signal could instead route a question directly to the source path, but [rule-based selection requires such a signal to exist before routing](./rule-based-context-selection-needs-a-pre-existing-signal.md). Routing changes who pays the cost; it does not change the accounting rule.

## Sufficiency is relative to the reliability the task demands

Sufficiency is not a property of a summary, or even of a summary–source pair. The same summary can close one question and leave another open because the corresponding actions require different reliability.

An **orientation** question may need only a component name or a plausible place to start. An approximation can license that next step when any error will be exposed within the accepted reliability bound. An **accuracy** question, such as one about an exact signature or schema field, requires evidence that licenses the change itself. An approximation may still route the reader, but it cannot close the question.

The sufficiency verdict therefore attaches to a four-part comparison: `(summary, source path, question, required reliability)`. Here `summary` means the consumed answer together with the provenance, corroboration, and verification available to this consumer—not bare text alone. Identical text can therefore be sufficient for one consumer and insufficient for another when their verification capabilities differ. Without a fixed question and reliability threshold, sufficiency has no per-use answer. Provenance, coverage, freshness, and corroboration matter only through whether they help the available answer clear that threshold; freshness alone neither guarantees nor precludes sufficiency.

## Sufficiency is independent of the matched grain floor

The matched grain test applies when the same known question maps to one discriminating, answer-bearing unit on each path: [the smaller addressed unit sets the matched selective-read floor](./addressability-grain-sets-a-matched-selective-read-floor.md). Grain asks how much material a reader must *select* to reach the candidate answer; sufficiency asks whether reading that answer *ends the task*. A summary must pass the two tests separately. Questions that require fan-out, discovery, or synthesis across several units need a broader path comparison because no single-unit floor captures all of their work.

The independence runs in both directions. A finely grained summary can still be insufficient: the reader selects a small unit and then needs the source path, although that unit may earn partial credit by narrowing the remaining work. A sufficient summary can still lose on grain: it closes the question, but the reader consumes a coarse section while the source exposes the same answer in a smaller selectable unit. Full substitution occurred, yet the summary path cost more.

The failures also require different repairs. Grain failure calls for better addressable keys or units. Sufficiency failure calls for stronger warrant or precision, a narrower declared use, or direct routing to the fallback.

## Scope

The per-use claim is **universal**. Fix a consumed summary, an authoritative source path, a question, and a required reliability; assume no other authoritative evidence route intervenes. If the summary cannot license the action, any reliability-compliant answer retains source-path work. One genuine case that meets those conditions yet produces a compliant answer without source-path work would refute the claim.

A consumer with no reachable authoritative fallback faces a different problem. An insufficient summary then creates unsupported-answer or abstention risk rather than an added-read path, so that use falls outside this ledger.

Whether a summary layer is worth maintaining is a separate **statistical** claim over the questions it actually receives. For a fixed cost currency, horizon, and traffic distribution, its gross use-phase value is expected fallback work removed minus expected summary consumption cost. A non-positive result refutes positive gross read-cost value for that distribution. Total layer value must also subtract allocated creation and maintenance costs and may include separately measured effects on error, abstention, latency, or downstream action. Under a declared total-value objective, the layer merits maintenance only when that total expectation is positive. Closure rate alone decides neither result because the costs and other effects vary across questions.

Nothing here claims that summaries are usually insufficient. A routing layer built for orientation questions may substitute cleanly for most of the traffic it receives.

## Consequences

**It completes the broader cache ledger.** [Opposed recompute factors do not decide documentation segmentation](./opposed-recompute-factors-do-not-decide-documentation-segmentation.md) prices net savings from equivalent reconstructions over a horizon. This note supplies the stopping condition inside “reconstructions avoided”: count only reliability-equivalent work that the summary actually displaces.

**It bounds model-facing materialization and frontloading.** [LLM recompute cost shifts the store-vs-recompute balance](./llm-recompute-cost-inverts-the-store-vs-recompute-default.md), but expensive derivation alone does not make persistence pay. A materialized or [frontloaded](./frontloading-spares-execution-context.md) answer earns credit only for derivation it prevents. If the full derivation still runs unchanged, the answer is pure addition regardless of its size.

**It is independent of recoverability.** [Attempted recovery identifies informational gaps, not provenance or authority](./documentation-generates-the-system-rather-than-describing-it.md). Recoverability asks whether declared sources can reproduce content; sufficiency asks whether the available content licenses stopping. Recoverable content can be sufficient and worth caching. Irrecoverable content can be insufficient for a question yet worth retaining because it is unique. When no authoritative fallback can supply the missing warrant, the use lies outside this added-read ledger. When another fallback can, apply the same removed-work comparison to that path.

**The operational question is a stopping question.** For each claim in a summary, ask what a reliability-compliant reader does next. If the reader must use the source path, full substitution failed. Credit only the discovery, selection, interpretation, or verification work that the summary actually removed.

## Open Questions

- What cheap coverage, provenance, or reliability signal can route a question directly to the source path when the summary is unlikely to license stopping?
- What is the cheapest way to estimate fallback work removed and summary cost over the actual distribution of questions a layer receives?

---

Relevant Notes:

- [Context efficiency is the central design concern in agent systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — grounds: the premise that makes an added read a real cost rather than a rounding error
- [Seven documentation cases left routing and synthesis](./evidence/seven-documentation-cases-left-routing-and-synthesis.md) — evidenced-by: a bounded Commonplace sweep where exactness prose left source inspection in the path while orientation and cross-component synthesis survived as separate uses
