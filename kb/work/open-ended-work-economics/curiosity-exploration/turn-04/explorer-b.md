# Explorer B: preserve routes to questions, not only answers

## Finding and actual prior

**Exact reconstruction and future question formation require different protections.** Reconstructing acquired text preserves what was encountered, but neither guarantees that a later worker will encounter it again nor supplies context never acquired. Selective retention can preserve today's argument while removing the detail that would make tomorrow's question visible. The modest response is to retain some evidence outside today's explanatory selection, keep uncertainty about missing history explicit, and occasionally consult through a different route. This is a research conjecture, not an adopted retention policy.

The [turn-3 integration](../turn-03/integration.md) already distinguishes never-acquired, discarded, and retained-but-unconsulted information. It already rejects lossless prose summaries and requires a changed allocation reason for renewed clarification. I do not claim those distinctions as discoveries. The contribution here is to show how discovery of missing relevance depends on the route by which a later worker meets evidence, using three concrete documentary cases other than confidence.

I read the prior integrations and [current coordination](./coordination.md), not current Explorer A. The cases below are observations about retained Commonplace documents and hypothetical comparisons based on their stated distinctions. They are not independent verification of historical behavior. No external-source conclusion, experiment, or measured retention advantage is offered.

## 1. Tag retrieval: a detail can challenge the evidence selector

The [tag-change trace](../../../../theory/evidence/tag-readme-trace-observed-causal-connection.md) records that adopting `covered_by` exposed a member with block-style YAML tags that the documented `rg` recipe had missed. It also records a different, easily lost distinction: human recognition preceded the new warning machinery; an earlier completeness violation was not observed.

Consider a hypothetical retention choice that keeps only “verification found missing members and improved navigation.” That sentence preserves a useful outcome but loses two different opportunities for inquiry. The block-YAML detail invites the question: **does retrieval coverage depend on serialization syntax rather than membership?** The chronology invites: **did the new machinery detect the original problem, or was detection what people added afterward?** Neither question requires a service consumer. Each could change understanding of how a method succeeds.

How could a later worker discover the omitted syntax detail? A broader parser-based membership check, a direct read of an excluded note, or consultation of the retained trace could expose the difference. These routes do not all depend on the original search recipe. Repeating that recipe more diligently would not necessarily help. A retained source inaccessible through the usual retrieval path is not equivalent to discarded evidence, but can be functionally absent during inquiry.

What must remain recoverable depends on the question. Exact note content and the historical search pattern permit examination of syntax coverage. The before/after chronology permits examination of causal attribution. A current corrected navigation recipe cannot reconstruct the historical blind spot by itself. Commit references may recover committed versions, but cannot recover an unrecorded reader's recognition or workaround.

This case changes the retention emphasis from preserving the accepted account alone to preserving evidence capable of challenging how its examples were selected. The trace reports such a challenge; it does not establish how often an independent consultation route will find one.

## 2. Quote checking: exactness can survive while relational information disappears

[ADR 046](../../../../reference/adr/046-verbatim-quotes-are-validated-against-their-cited-source.md) distinguishes checking whether a URL exists from pairing a quotation with a nearby source link. Its recorded design issue is concrete: a set of URLs suffices for link health but loses positions needed for proximity pairing. The decision also distinguishes code-fenced examples from asserted citations and explains why blanking fences preserves offsets whereas deletion does not.

A hypothetical summary, “both checks resolve references against other files,” preserves their shared operation while concealing why they need different information. Common-case comparisons on one quotation with one link could make an impoverished representation look adequate. A later case with several quotations and links, or a fenced demonstration, makes the previously discarded relation relevant. The lost information need not be a rare fact; it may be order, adjacency, or the distinction between assertion and example.

Here a later worker can discover relevance without recovering the original incident. A new pairing ambiguity can originate the question: **which relations did our representation erase?** If the original Markdown remains available, positions can be reacquired from it. If only the URL set survives and multiple original arrangements yield that set, exact historical reconstruction is impossible from that set alone. Guessing a plausible arrangement does not recover the encounter.

This is a stipulated demonstration of non-uniqueness, not an observed data-loss experiment. Its importance for curiosity is that a representation adequate for existing checks can be inadequate for an unforeseen inquiry. Retaining exact Markdown would preserve the relevant arrangement in this example. It would not guarantee that later workers ask the pairing question, nor preserve tool behavior or author intent absent from that Markdown.

## 3. A parked question: naming is not retaining the choice

The [first trial's turn-2 Explorer A](../../bootstrap-exploration/turn-02/explorer-a.md) lists compression-based curiosity among parked ideas without an individual comparative reason. Its surrounding text does retain a broader account: useful question formation need not identify a consumer, and renewal is separate from discovery. The missing reason must not be filled with today's preferred explanation.

The later operator-selected direction makes the old omission consequential. A worker can now ask whether compression was parked for cost, evidence, scope, or preference. The record establishes that it was formulated; it does not establish which reason controlled its selection. This is a case of discovering that a detail matters while remaining unable to answer the resulting historical question.

The evidence inspected does not establish whether that rationale was never recorded or was recorded elsewhere and subsequently lost. If an accessible contemporaneous record exists, reacquisition may answer it. Without one, a later participant's reconstruction is new testimony, not recovery of the original decision record. A new comparison can evaluate compression's present promise but cannot retroactively establish the old reason.

This limits any promise to preserve unforeseen questions. Sometimes we retain enough to originate an important question but not enough to resolve it. Sometimes we lose even the clue: a summary omitting the parked branch entirely would leave no internal sign that the question had once been considered.

## Hidden deterioration and its limits

Holding old and new accounts to the same retained cases is necessary for some fair comparisons, but the cases can share a blind spot. All-inline YAML examples conceal syntax-dependent retrieval loss; one-link citation examples conceal lost adjacency; accepted outcomes conceal missing selection reasons. Both accounts may pass because neither is asked about what the selection excluded. Apparent improvement on common cases can coexist with narrower ability to recognize a new question.

The strongest rival is **retain concise conclusions and version locators, then reacquire detail when a concrete question demands it**. This avoids costly speculative capture and reduces consultation burden. It can succeed when originals remain accessible and an independent encounter supplies the question. My proposed addition is justified only where waiting for a question systematically removes its own trigger, or where the relevant original is transient. That risk is plausible here, not measured.

Discriminating evidence would include later inquiries whose origination can be traced to a retained incidental detail, contrasted with inquiries equally reachable through fresh acquisition. Also needed are the costs of saving, finding, and interpreting those details, including unproductive consultations. No such comparison ran here. Cases where concise records and reacquisition suffice count against expanding retention, not as failures to appreciate curiosity.

There is an irreducible limit: when two histories leave the same accessible record but differ on a discarded feature, that record cannot identify which history occurred. An independent encounter may establish that the feature matters generally without recovering its old value. If no trace, witness, external copy, or subsequent consequence distinguishes them, later workers cannot even discover the particular loss from the surviving record alone.

## Modest candidate requirements

To preserve opportunities for learning without requiring everything to be kept:

- **Acquire beyond the conclusion when the encounter is transient.** Preserve the actual counterexample, ambiguous passage, or consequential choice reason while available. Do not acquire an entire environment by default. State what the capture excludes when that limits later challenge.
- **Retain a small amount not selected solely by the favored explanation.** In these cases that means syntax and chronology, an ambiguous citation arrangement, and the strongest parked alternative with its reason or explicit absence. These details preserve different possible questions, not a universal checklist of fields.
- **Treat reacquisition as a contingent route.** Name the original and version when available; distinguish an accessible retained original from a mutable URL or unverified recovery hope. Reopening, reading, and comparing have costs even when storage is cheap.
- **Consult outside common-case success when renewing an explanation.** Revisit a prior exception or inspect through a route that does not share the original selector's limitation. This is bounded examination, not whole-history testing. Record which unexamined cases still limit the progress claim.

These proposals compete with acquisition time, context capacity, privacy or retention constraints, navigation burden, and false leads. Exact retention can be cheaper than predicting every future relevance, yet costly to search and interpret. No universal amount follows from these cases. Learning value is the ability to originate and challenge explanations; task benefit such as faster retrieval remains a separate, unmeasured return.

## Disposition

Keep the independent-consultation requirement as a candidate supplement to concise records and reacquisition. Park keep-everything retention for cost and scope, general storage design for ownership, numerical compression for lack of a defensible prose measure, and historical motive reconstruction for missing evidence. Ordinary explanation-seeking remains the strongest steering rival; these requirements do not establish a special compression advantage.

This report is complete as documentary reasoning and partial on comparative effectiveness. Costs are unknown. No source mutation or broader graph work occurred. Optional `cp-skill-connect` work would require separate authorization; it is not needed to finish this turn. Only this result file is owned.
