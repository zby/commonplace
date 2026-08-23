---
description: "Substitution, not size, is what makes a summary cheap: where its answer cannot license the action the task requires, the source is read regardless and the summary's cost adds to the full path instead of replacing part of it"
type: kb/types/note.md
traits: [title-as-claim]
tags: [context-engineering, document-system]
---

# An insufficient summary precedes the source rather than replacing it

A summary is cheaper than its source only when it is read *instead of* the source. That substitution has a precondition: the answer the summary gives must be good enough for the consumer to act on at the reliability the task demands. Call that **sufficiency**. Where sufficiency fails, the consumer reads the summary, finds that it does not license the action, and reads the source anyway. The summary's cost is then added to the path rather than replacing part of it. An insufficient summary does not compete with the source; it precedes it.

## The usual accounting assumes substitution without checking it

The standard way to justify a summary compares its size against the source's — a compression ratio, a token count, a "this page is a tenth of the code it covers". That comparison is only meaningful if the reader consumes one artifact or the other. Substitution is smuggled in as an unstated premise, and it is the premise that actually decides the outcome.

When sufficiency fails, the comparison is not merely optimistic about the margin. Its sign is wrong. The reader pays the summary *and* the source, so the summary makes the total worse than having no summary at all, and it does so by exactly the amount the size comparison was offering as the saving.

The general ledger is one line: a summary's value is the source-read cost it removes, minus its own cost. Full sufficiency removes all of it. Insufficiency removes at most whatever narrowing the summary supplies — a file to open, a name to search for, a section to start in — and where it supplies no narrowing, it removes nothing and the value is strictly negative. The title claim is the universal half of this: sufficiency failing means the source read still happens. Whether the total gets worse then depends on whether the narrowing is worth more than the summary cost. The pure case, where an insufficient summary narrows nothing, is where the sign flips outright.

There is a further asymmetry in who pays. Insufficiency is usually discovered by reading. The consumer cannot tell in advance that this particular question is one the summary will not close, so the summary's cost is charged on every attempt while the saving arrives only on the attempts where it happens to suffice.

## Sufficiency is relative to the reliability the task demands

Sufficiency is not a property of the summary, nor even of the summary–source pair. The same summary over the same source can be substitutive for one question and additive for another, because different tasks require different reliability from the answer.

An **orientation** question — which component owns this concern, roughly what does this subsystem do, where should I start looking — can be closed by an approximation. Being approximately right is enough to take the next step, and if the approximation is wrong the next step reveals it cheaply. Here the summary genuinely substitutes for the source read, and its cost replaces a larger one.

An **accuracy** question — I am changing this code, I need the exact signature, I need the field names in this schema, I am debugging and the behaviour must be the actual behaviour — cannot be closed by an approximation. An approximate answer does not license the action, so the source read happens regardless of what the summary said. The summary can at best point at where to read. Whatever it says about the specifics is spent context.

So the verdict attaches to a tuple: (summary, source, question, required reliability). Asking "is this summary worth its cost" without fixing the last two terms has no answer. This is also why a summary can look adequate for a long time and then fail: it was receiving orientation questions, and the first accuracy question is where the additive case shows up.

The non-authoritative status of a summary is what ties reliability to substitution. A summary that is derived from a source, and can drift from it, cannot supply an answer more reliable than the reader's confidence that it is current. Where the required reliability exceeds that confidence, the source is consulted by construction.

In one instance from the repository this note is written inside, a per-module reference document's section covering a module was consulted for a symbol-level question — what a particular function returns — and did not close it, so the module was read anyway. That is one witness that the additive case occurs in ordinary well-written documentation, not a claim about how that repository's documents behave in general.

## Sufficiency and grain are two conditions, and neither implies the other

A separate condition governs the same decision: [a summary layer helps a selective reader only when its own smallest addressable unit is finer than the source's](./addressability-grain-not-compression-ratio-decides-whether-a.md). Grain is about how small a piece the reader can *select*; sufficiency is about whether reading that piece *ends the task*. A summary must pass both, separately.

The independence runs in both directions. A finely grained summary — one whose units are small, named, and precisely selectable — is still additive if its answers cannot be acted on; the reader selects a small unit, reads it, and then goes to the source. And a sufficient summary can still lose on grain: if it closes the question but the reader had to consume a whole coarse section to get there, while the source would have yielded the same answer from a smaller selectable unit, the substitution happened and still cost more than not summarizing.

The two conditions also fail for different reasons and are repaired differently. Grain failure is structural — it is fixed by giving the summary's content search keys a reader would actually query. Sufficiency failure is about authority and precision — it is fixed by carrying content the source cannot supply as cheaply, or by not carrying that content at all.

## Consequences

**It is a second condition on the materialization default.** Since [LLM recompute cost inverts the store-vs-recompute default](./llm-recompute-cost-inverts-the-store-vs-recompute-default.md), materializing a derived value for a model to read is normally worth it. That default already carries a volume condition. Sufficiency is a second one, and it is prior: materializing pays only when the materialized form is consulted *instead of* the recompute. If the model reads the materialized value and then runs the recompute anyway — because the value is not trusted enough for what it is about to do — the materialization has negative value regardless of how small it is.

**It is what licenses frontloading's volume caveat.** [Frontloading spares execution context](./frontloading-spares-execution-context.md) saves, on raw volume, only when the inserted result is smaller than the material it *replaces*. "Replaces" is doing the work in that sentence, and this claim is why: without replacement there is no saving to compare sizes about. An inserted result the call reads and then goes and derives properly anyway is pure addition, however compact.

**It is a different question from recoverability.** Asking whether a document's content can be regenerated from the system it describes — the test that finds [documentation generates the system rather than describing it](./documentation-generates-the-system-rather-than-describing-it.md) — asks whether the content *exists* elsewhere. Sufficiency asks whether reading it *ends the reader's task*. The two cross freely. Fully recoverable content can be sufficient, and is then worth keeping as a cache that genuinely substitutes. Content nothing else records can be insufficient, and is then worth keeping for the irrecoverability reason while contributing nothing to read cost. Conflating them produces both mistakes: cutting a cache that was doing real substitution, and defending a unique document on cost grounds it does not meet.

**The operational question is a stopping question.** For each thing a summary says, ask what the reader will do next after reading it. If the honest answer is "open the source to check", that content is additive for that use, and its size is not a defence.

## Scope

The claim is universal per tuple: fix a summary, a source, a question, and a required reliability, and either the summary closes the question or the source read still happens. Whether a summary *layer* is worth maintaining is a different, aggregate judgment over the distribution of questions it actually receives, and that judgment is statistical — a layer that closes most of its traffic can carry a minority of additive cases and still pay. Nothing here says a layer must be sufficient for every question; it says the accounting must count the additive cases as costs rather than as smaller savings.

Partial substitution is real and is not the same as sufficiency. A summary that narrows the source read without ending it has removed some cost, and the ledger credits that. The sharp case in the title is the one where nothing is removed.

The argument assumes the reader is willing to go to the source. A consumer that *cannot* reach the source — a model with no tool access, a reader with only the summary in context — faces a different problem: an insufficient summary there does not add cost, it produces an unsupported answer. That is a correctness failure rather than an accounting one, and it is worse.

Nothing here claims summaries are usually insufficient. Orientation traffic is common, and a routing layer whose whole job is to answer orientation questions substitutes cleanly and is among the strongest uses of the pattern.

## Open Questions

- Sufficiency is discovered by reading, which means the cost is paid before the verdict is known. Is there a cheap advance signal — a declared reliability level on the summary, a marker on content known to be approximate — that lets a reader skip to the source without paying the summary first?
- The aggregate judgment needs the distribution of questions a layer receives, which is rarely observed. What is the cheapest proxy for it?

---

Relevant Notes:

- [Addressability grain, not compression ratio, decides whether a summary layer helps](./addressability-grain-not-compression-ratio-decides-whether-a.md) — contrasts: grain asks how small a unit the reader can select, sufficiency asks whether reading it ends the task; a summary must pass both and neither implies the other
- [LLM recompute cost inverts the store-vs-recompute default](./llm-recompute-cost-inverts-the-store-vs-recompute-default.md) — extends: adds a second condition on that note's materialization default, alongside the volume condition its scope already records
- [For its load-bearing part, documentation generates the system rather than describing it](./documentation-generates-the-system-rather-than-describing-it.md) — contrasts: its recovery test asks whether content exists elsewhere, this asks whether reading it suffices; recoverable content can be sufficient and unique content can be insufficient
- [Context efficiency is the central design concern in agent systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — grounds: the premise that makes an added read a real cost rather than a rounding error
