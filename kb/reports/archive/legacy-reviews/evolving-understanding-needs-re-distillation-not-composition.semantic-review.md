<!-- REVIEW-METADATA
note-path: kb/notes/evolving-understanding-needs-re-distillation-not-composition.md
last-full-review-note-sha: 2580833d6964bfae8dee6a6ae51ca36909b831c9
last-full-review-note-commit: 77b36d90b09b102404f4e2800ecad318640838d0
last-full-review-at: 2026-03-23T12:00:00+01:00
last-accepted-note-sha: 2580833d6964bfae8dee6a6ae51ca36909b831c9
last-accepted-note-commit: 77b36d90b09b102404f4e2800ecad318640838d0
last-accepted-at: 2026-03-23T12:00:00+01:00
last-acceptance-kind: full-review
review-type: semantic-review
-->

=== SEMANTIC REVIEW: evolving-understanding-needs-re-distillation-not-composition.md ===

Claims identified: 13

## Claims extracted

1. "A note graph distributes knowledge across composable fragments — each note makes one claim, links provide traversal." — intro, definitional
2. "When understanding is evolving and a consumer needs the whole picture [...] fragment reconciliation may not be feasible." — intro, central claim
3. "Loading many notes, identifying which are current, and assembling a coherent view competes for context budget on two dimensions: volume [...] and complexity" — intro, causal claim citing two cost dimensions
4. "As fragment count grows, reconciliation can exceed effective context — making the operation infeasible, not merely expensive." — intro, threshold claim
5. "A pre-distilled narrative sidesteps this. The author [...] performs reconciliation once and produces a single document sized for effective context." — intro, proposed solution
6. "When understanding changes, you re-distill — holistic rewrite — rather than let fragments diverge until reconciliation breaks." — intro, prescriptive
7. "At least three properties of evolving understanding push fragment-based reconciliation toward the effective context boundary" — enumeration (three properties)
8. "The whole picture must be loaded at once" — property 1
9. "Discrimination complexity grows with change rate" — property 2
10. "Coherence requires simultaneous loading" — property 3
11. "The pattern applies when: [three conditions — accumulating knowledge, needs whole picture, value consumed]" — scope claim
12. "The lifecycle is workshop, not library" — classification claim
13. "Theorist is illustrative rather than confirmatory: it demonstrates the pattern's mechanics but offers no controlled evidence that re-distillation outperforms composition." — scope limitation on evidence

## Step 2: Completeness and boundary cases

### Enumeration: "at least three properties" (claim 7)

The grounding definition is the note's own framing: properties of evolving understanding that push fragment-based reconciliation toward the effective context boundary. The "at least" qualifier hedges against exhaustiveness.

**Boundary cases tested:**

(a) **Simplest instance — two fragments, one superseding the other.** A consumer loads two notes; one contradicts the other on a single point. Discrimination is trivial. This maps to property 2 but at minimal cost. The note's own Open Questions section acknowledges this: "If fragments are few and stable, a consumer can reconcile within effective context." The boundary is handled.

(b) **Most extreme instance — hundreds of interdependent fragments evolving daily.** All three properties compound: volume is enormous (property 1), currency discrimination is near-impossible across the set (property 2), and coherence checking requires holding the entire graph (property 3). The note's argument handles this naturally — it is the prototypical case. No gap.

(c) **Between-items case: fragments that are all current but implicitly conflict.** No individual note is stale, yet the collection contains unreconciled tensions because insights were added independently. Property 2 (discrimination of current vs. stale) does not capture this — the fragments are all current. Property 3 (coherence requires simultaneous loading) does capture it, but only partially: it says the consumer must hold all notes and reconcile tensions, but it does not distinguish "tensions from staleness" from "tensions from independent authorship of non-stale notes." The note treats these as the same problem, which is roughly correct (both require simultaneous loading to detect), but the source of incoherence differs and could warrant different responses (re-distillation vs. explicit reconciliation of genuinely competing insights).

(d) **Adjacent concept: evolving understanding where the ontology itself shifts.** The note's examples (onboarding docs, incident response, design rationales) assume the categories are stable while content evolves. But understanding can evolve structurally — the categories themselves merge, split, or get renamed. Fragment-based approaches fail differently here: it is not just that notes become stale, but that the vocabulary for connecting them shifts. The three properties do not distinguish this case, though all three still apply.

(e) **Re-distillation exceeding effective context.** The note positions re-distillation as the solution, but if accumulated understanding is large enough, the holistic rewrite operation itself may exceed the rewriter's effective context. The note does not address this recursion. Open Question 3 ("complex situations may resist compression into a single document") touches the output side (the narrative may not fit), but not the input side (the source material for the rewrite may not fit in the rewriter's context either). This is a genuine gap in the argument.

### Scope conditions: "the pattern applies when" (claim 11)

**Boundary cases tested:**

(f) **Static knowledge requiring the whole picture.** A comprehensive onboarding document for a stable system satisfies conditions 2-3 (whole picture, consumed value) but not condition 1 (knowledge accumulating from ongoing work). Composition from fragments should work here because there is no currency discrimination problem. The scope conditions correctly exclude this case.

(g) **Rapidly evolving knowledge where only a slice is needed.** A developer investigating a specific bug in a rapidly changing system satisfies condition 1 but not condition 2 — they need a targeted slice, not the whole picture. Fragment-based retrieval should work. The scope conditions correctly exclude this. However, the boundary is fuzzy: the developer might discover mid-investigation that the bug interacts with recently changed assumptions elsewhere, suddenly requiring the whole picture. The note does not address this discovery-during-consumption dynamic.

## Step 3: Grounding alignment

### Link: distillation.md — "foundation"

The note claims: "In distillation terms: accumulated understanding is the source, the consumer needing the current picture is the target, and the narrative is the distillate."

The distillation note defines distillation as "compressing knowledge so that a consumer can act on it within bounded context" and includes the table row "Accumulated understanding -> Narrative | Consumer who needs the current whole picture." This is a direct and exact match. Attribution is accurate.

### Link: context-efficiency-is-the-central-design-concern-in-agent-systems.md — "foundation"

The note says fragment reconciliation "competes for context budget on two dimensions: volume [...] and complexity." The context-efficiency note establishes context as "the scarce resource" with "everything competes for the same space" and decomposes the soft bound into "volume (how many tokens) and complexity (how hard they are to use)." The reviewed note's two-dimension framing matches the source exactly. Attribution is accurate.

### Link: effective-context-is-task-relative-and-complexity-relative-not-a-fixed-model-constant.md — "grounds"

The note claims reconciliation "can exceed effective context — making the operation infeasible, not merely expensive." The effective-context note establishes that usable context varies by task type and complexity. The reviewed note's inference — that reconciliation is a high-complexity task that can push past the effective context boundary — is consistent with the source. The link text in the Relevant Notes section says "reconciliation complexity reduces effective context," which is a slight misstatement: the source says complexity changes the effective cost of the prompt, not that one task reduces the available context for another. But the operational meaning (reconciliation may be too complex for the available effective context) is consistent.

### Link: a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md — "workshop lifecycle"

The note claims "the narrative lives and dies with the period of active evolution. When understanding stabilizes, insights should be extracted into durable notes, a second distillation into a different form for a different consumer." The workshop note defines workshop documents as having "consumed value" lifecycles where "completion and archival are success states" and lists extraction bridges (workshop -> library) as a key mechanism. The workshop note also explicitly lists the reviewed note as exemplifying the workshop layer. Bidirectional confirmation — attribution is accurate.

### Link: Augment bidirectional spec ingest — "extends"

The reviewed note's link text says the Augment source "extends: distributes the re-distillation burden between human review and agent-generated updates." The ingest describes a bidirectional spec where agents update the spec as they discover reality diverges from the plan. The connection to re-distillation is established by the ingest itself (listing the reviewed note as a moderate connection that "extends the re-distillation pattern by making it bidirectional"). However, the Augment source is specifically about evolving plans/specs for implementation tasks, not about evolving understanding of a domain. Plans and understanding both evolve, but they have different structures: a plan has completion criteria and a defined scope, while understanding is open-ended. The reviewed note's claim that the Augment approach "distributes the re-distillation burden" is reasonable but the domain mismatch (plans vs. beliefs) means the link is weaker than the "extends" label suggests.

## Step 4: Internal consistency

### Pairwise contradiction check

The intro says fragment-based composition "works for durable knowledge: the consumer picks what to load, coherence is local to each note." The "why composition is expensive" section says "each note can be internally coherent while the set is collectively inconsistent." These are consistent — the first describes the case where collective coherence is not needed, the second describes the case where it is.

The note says "the author — human or agent — performs reconciliation once" (suggesting agents can do this) and then Open Questions asks "Can agents perform holistic rewrite reliably, or does re-distillation require human judgment?" This is not a contradiction — the body includes agents as potential authors, and the open question flags uncertainty about whether they can fulfill that role. The hedging is appropriate.

### Definition drift check

"Re-distillation" is introduced as "holistic rewrite" in the intro and used consistently throughout. "Effective context" aligns with its linked definition. "Workshop" and "library" are used consistently with the workshop note's definitions. No drift detected.

### Summary faithfulness

The description reads: "When understanding evolves, reconciling fragments into a coherent picture can exceed effective context; a pre-distilled narrative keeps the whole picture within feasible bounds." This faithfully represents the body. It preserves the conditionality ("can exceed") and captures both the problem (reconciliation exceeding effective context) and the solution (pre-distilled narrative). It omits the three properties, the scope conditions, and the workshop lifecycle, all of which are appropriate omissions for a retrieval-oriented one-liner.

---

WARN:
- [Completeness] The note frames re-distillation as the solution to reconciliation exceeding effective context, but does not address the case where the re-distillation operation itself exceeds effective context. If accumulated understanding is large enough, holistic rewrite faces the same feasibility constraint it solves for the consumer. Open Question 3 ("complex situations may resist compression into a single document") addresses the output side (the narrative may not fit in one document) but not the input side (the source material may not fit in the rewriter's context window). This is a structural gap: the argument assumes re-distillation is always feasible while arguing composition is not.
- [Grounding] The link to the Augment bidirectional spec ingest is labeled "extends: distributes the re-distillation burden between human review and agent-generated updates." The Augment source concerns evolving implementation plans/specs, not evolving domain understanding. Plans have completion criteria and bounded scope; understanding is open-ended. Applying the "re-distillation" framing to spec maintenance is the reviewed note's own inference. The domain gap is mild but a reader following the link expecting evidence about re-distillation of understanding will find evidence about co-maintenance of specs instead.

INFO:
- [Completeness] The note does not distinguish content evolution (beliefs and facts change) from structural evolution (the categories and ontology shift). Both are instances of "evolving understanding," but they produce different failure modes in fragment composition: stale facts vs. incompatible vocabularies across fragments. The three enumerated properties address the stale-facts case more directly than the shifting-ontology case.
- [Completeness] The boundary between "needs the whole picture" (scope condition 2) and "needs a slice" is presented as a precondition the consumer knows in advance. In practice, a consumer may discover mid-task that a slice is insufficient because of tensions with recently changed understanding elsewhere. This discovery-during-consumption dynamic could strengthen the note's argument for pre-distilled narratives (you cannot always know in advance whether you will need the whole picture), but the note does not discuss it.
- [Grounding] The Relevant Notes link text for effective-context says "reconciliation complexity reduces effective context" — this is a slight vocabulary mismatch with the source, which says complexity changes the effective cost of a prompt rather than reducing the available context. The operational implication is the same (reconciliation may exceed what the context can handle), but the phrasing could mislead a reader into thinking reconciliation literally shrinks the window.

PASS:
- [Completeness] The "at least three properties" enumeration uses an open-ended qualifier that avoids overclaiming exhaustiveness. All three properties are distinct and map to different failure modes: volume saturation (property 1), discrimination difficulty (property 2), and collective incoherence (property 3). The simplest boundary case (two fragments, trivial discrimination) is handled by the Open Questions section acknowledging the threshold.
- [Completeness] The scope conditions ("the pattern applies when") correctly exclude cases where composition would work: static knowledge (fails condition 1), slice-only consumption (fails condition 2), and library-style accumulated value (fails condition 3). Each condition is necessary — removing any one admits cases where fragment composition suffices.
- [Grounding] The distillation.md link is accurate — the source explicitly contains a table row matching the exact source-target-distillate triple the reviewed note claims. No vocabulary or scope mismatch.
- [Grounding] The context-efficiency link is accurate — "context budget on two dimensions: volume and complexity" directly matches the source's decomposition of the soft bound into volume and complexity. No overextension.
- [Grounding] The workshop lifecycle claim is bidirectionally confirmed — the workshop note defines consumed-value lifecycles and lists this note as an exemplar; the reviewed note's characterization of the narrative as "lives and dies with the period of active evolution" matches faithfully.
- [Grounding] The theorist evidence is appropriately scoped — the note explicitly states "illustrative rather than confirmatory" and identifies the strongest signal as "indirect" (easier onboarding reports). No overclaiming of evidential weight.
- [Internal consistency] No contradictions found between sections. The intro, body, and open questions maintain a coherent argument. The body includes agents as potential re-distillers while the open questions flag uncertainty about agent reliability — appropriate hedging rather than contradiction.
- [Internal consistency] Key terms (re-distillation, effective context, workshop, library) are used consistently throughout without drift.
- [Internal consistency] The description faithfully compresses the body without overstating. The conditional phrasing ("can exceed") preserves the note's hedging.

Overall: 2 warnings, 3 info
===
