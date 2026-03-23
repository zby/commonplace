=== SEMANTIC REVIEW: evolving-understanding-needs-re-distillation-not-composition.md ===

Claims identified: 12

## Claims extracted

1. "A note graph distributes knowledge across composable fragments" — intro, definitional
2. "When understanding is evolving and a consumer needs the whole picture [...] fragment reconciliation may not be feasible" — intro, central claim
3. "A pre-distilled narrative sidesteps this" — intro, causal claim
4. "When understanding changes, you re-distill — holistic rewrite — rather than let fragments diverge until reconciliation breaks" — intro, prescriptive
5. "At least three properties of evolving understanding push fragment-based reconciliation toward the effective context boundary" — enumeration (three properties)
6. "The whole picture must be loaded at once" — property 1
7. "Discrimination complexity grows with change rate" — property 2
8. "Coherence requires simultaneous loading" — property 3
9. "The pattern applies when: [three conditions]" — scope claim (three conditions)
10. "The lifecycle is workshop, not library" — definitional/classification
11. Theorist "implements this pattern as THEORY.MD" — attribution claim
12. "Theorist is illustrative rather than confirmatory" — scope limitation on evidence

## Step 2: Completeness and boundary cases

### Enumeration: "at least three properties" (claim 5)

The grounding definition is the note's own framing: properties of evolving understanding that push fragment reconciliation toward the effective context boundary. The "at least" qualifier is an important hedge — the note does not claim exhaustiveness.

**Boundary cases tested:**

(a) **Simplest possible instance — two fragments, one supersedes the other.** A consumer loads two notes; one is stale. Discrimination is trivial (one contradicts the other on a single point). This maps to property 2 but the cost is minimal. The note's argument implicitly requires a threshold fragment count for the problem to bite. The note does acknowledge this in Open Questions: "If fragments are few and stable, a consumer can reconcile within effective context." This boundary is handled.

(b) **Fragments that are independently current but collectively incoherent.** All notes are individually up to date, but their combination reveals tensions the author hasn't reconciled. This maps to property 3 (coherence requires simultaneous loading), but the source of the problem is different from what property 2 addresses (stale vs. current discrimination). The note covers this adequately through property 3.

(c) **Understanding that evolves in structure, not just content.** The note's examples (onboarding docs, incident summaries, design rationales) all assume the evolution is in beliefs/facts. But understanding can also evolve structurally — the categories themselves shift, not just what's in them. A narrative might handle this better than fragments, but the note doesn't distinguish content evolution from structural evolution. This is a mild gap.

(d) **A consumer who needs only a slice of the evolving picture, not the whole thing.** The note's scope claim (condition 2: "a consumer needs the whole picture to act, not just a slice") explicitly excludes this. But in practice, the boundary between needing a slice and needing the whole picture is blurry — a consumer might think they need a slice until they discover a tension that requires the whole picture. The note doesn't address this intermediate case.

(e) **Re-distillation that itself exceeds effective context.** If accumulated understanding is large enough, the re-distillation operation (holistic rewrite) itself may exceed the agent's effective context. The note frames re-distillation as "the author performs reconciliation once," but doesn't address what happens when the source material for re-distillation is too large for one pass. Open Question 3 ("complex situations may resist compression into a single document") touches this tangentially but doesn't frame it as a feasibility constraint on the re-distillation operation itself.

### Enumeration: "the pattern applies when" (claim 9, three conditions)

**Boundary case tested:**

(f) **Static knowledge that a consumer needs as a whole picture.** An onboarding document for a stable system satisfies conditions 2 and 3 (whole picture, consumed value) but not condition 1 (accumulating from ongoing work). In this case, composition from fragments might work fine because there's no currency discrimination needed. The three conditions correctly exclude this — the note's scoping holds.

## Step 3: Grounding alignment

### Link: distillation.md — "foundation"

The note claims: "In distillation terms: accumulated understanding is the source, the consumer needing the current picture is the target, and the narrative is the distillate."

The distillation note defines distillation as "compressing knowledge so that a consumer can act on it within bounded context." It includes in its table: "Accumulated understanding -> Narrative | Consumer who needs the current whole picture." This is a direct match — the distillation note explicitly lists the exact source-target-distillate triple the reviewed note claims. Attribution is accurate.

### Link: context-efficiency-is-the-central-design-concern-in-agent-systems.md — "foundation"

The note claims fragment reconciliation competes for "context budget." The context-efficiency note establishes that "context is the scarce resource" and "everything competes for the same space." The note uses "context budget" as shorthand for this, which aligns with the source's framing of an "attention budget." Attribution is accurate.

### Link: effective-context-is-task-relative-and-complexity-relative-not-a-fixed-model-constant.md — "grounds"

The note claims "reconciliation can exceed effective context — making the operation infeasible, not merely expensive." The effective-context note establishes that effective context varies with task type and complexity. The reviewed note's use of "effective context" as a task-relative boundary is consistent with the source. However, the reviewed note goes further: it claims reconciliation complexity *itself* reduces effective context ("reconciliation complexity reduces effective context"). The source note says complexity changes the effective cost of a prompt, not that one task (reconciliation) reduces the available context for another task. The note is conflating two things: (a) reconciliation is a complex task that requires high effective context, and (b) reconciliation reduces effective context available for the actual task. Reading charitably, the note means (a) — reconciliation consumes context that could be used for the task — which is consistent with the source's framing that everything competes for the same window.

### Link: a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md — "workshop lifecycle"

The note claims: "The lifecycle is workshop, not library — the narrative lives and dies with the period of active evolution." The workshop note defines workshop documents as having "consumed value" lifecycles where "completion and archival are success states." It also explicitly lists "evolving understanding needs re-distillation not composition" as exemplifying the workshop layer. Bidirectional confirmation — attribution is accurate.

### Link: Augment bidirectional spec ingest — "extends"

The note's link text says the Augment source "extends: distributes the re-distillation burden between human review and agent-generated updates." The ingest describes a bidirectional spec where "agents update it as they discover reality diverges from the plan, and the human reviews at any point." The connection to re-distillation is the ingest's own: it lists the reviewed note as a moderate connection, saying it "extends the re-distillation pattern by making it bidirectional." The reviewed note's claim that the Augment approach "distributes the re-distillation burden" is a reasonable inference — the bidirectional spec does split the update work between agent and human. But the Augment source is specifically about specs (plans for work), not about accumulated understanding of a domain. The re-distillation note is about evolving beliefs; the Augment note is about evolving plans. These are related but not identical — applying "re-distillation" to both stretches the term slightly.

## Step 4: Internal consistency

### Pairwise contradiction check

The intro says "the consumer picks what to load, coherence is local to each note" for durable knowledge, then the "why composition is expensive" section says "each note can be internally coherent while the set is collectively inconsistent." These are consistent — the first describes the normal library case (local coherence suffices), the second describes the evolving-understanding case (collective coherence is also needed).

### Definition drift check

"Re-distillation" is introduced as "holistic rewrite" in the intro and used consistently throughout. "Effective context" is used consistently with its linked definition. No drift detected.

### Summary faithfulness

The description reads: "When understanding evolves, reconciling fragments into a coherent picture can exceed effective context; a pre-distilled narrative keeps the whole picture within feasible bounds." This faithfully represents the body's argument. It elides the three properties and the workshop lifecycle, which is appropriate for a one-line description. It does not overstate — "can exceed" preserves the note's conditionality.

---

WARN:
- [Completeness] The note frames re-distillation as the solution to reconciliation exceeding effective context, but does not address the case where re-distillation itself exceeds effective context. If accumulated understanding grows large enough, holistic rewrite faces the same feasibility constraint it solves for the consumer. Open Question 3 ("complex situations may resist compression") touches this but frames it as a compression problem rather than a feasibility-of-the-rewrite-operation problem.
- [Grounding] The link to the Augment bidirectional spec ingest is labeled "extends: distributes the re-distillation burden between human review and agent-generated updates." The Augment source is about evolving plans/specs, not evolving understanding/beliefs. Applying the re-distillation framing to spec maintenance is the note's own inference, not something the source claims. The domain mismatch is mild (plans and understanding both evolve) but a reader could mistake this link as grounding the re-distillation pattern in a broader context than the source supports.

INFO:
- [Completeness] The note does not distinguish between content evolution (beliefs/facts change) and structural evolution (the categories themselves shift). Both are plausible instances of "evolving understanding," but the properties enumerated in "why composition is expensive" are primarily about content currency. Structural evolution might produce different failure modes — e.g., fragments that use incompatible ontologies rather than merely stale facts.
- [Completeness] The boundary between "needs the whole picture" and "needs a slice" (scope condition 2) is presented as sharp, but in practice a consumer may discover they need the whole picture only after starting with a slice. The note doesn't address this discovery-during-consumption case, which could strengthen the argument for pre-distilled narratives (you can't know in advance whether you'll need the whole picture).

PASS:
- [Completeness] The "at least three properties" enumeration uses an open-ended qualifier that avoids overclaiming. All three properties are distinct (volume, discrimination, coherence) and map to different dimensions of context cost. The simplest boundary case (two fragments, trivial discrimination) is handled by the note's own Open Questions section acknowledging the threshold.
- [Completeness] The scope conditions ("the pattern applies when") correctly exclude static knowledge and slice-consumers, which are cases where fragment composition would work fine. The conditions are necessary (removing any one would admit cases where composition suffices).
- [Grounding] The distillation.md link is accurate — the distillation note explicitly contains a table row matching the exact source-target-distillate triple the reviewed note claims. No vocabulary or scope mismatch.
- [Grounding] The context-efficiency link is accurate — "context budget" maps to the source's "attention budget" and the competition-for-space framing is faithful.
- [Grounding] The workshop lifecycle claim is bidirectionally confirmed — the workshop note lists this note as an exemplar of the workshop pattern, and the reviewed note's description of "lives and dies with the period of active evolution" matches the workshop note's "consumed value" lifecycle.
- [Internal consistency] No contradictions found between sections. The intro/body/open-questions maintain a consistent argument with appropriate hedging. The description faithfully compresses the body without overstating.
- [Internal consistency] Key terms (re-distillation, effective context, workshop) are used consistently throughout without drift.

Overall: 2 warnings, 2 info
===
