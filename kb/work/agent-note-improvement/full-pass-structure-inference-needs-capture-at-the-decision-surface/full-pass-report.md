# Full Improvement Pass: Bottom-up structure inference needs capture at the decision surface, not the state

**Target:** `kb/notes/structure-inference-needs-capture-at-the-decision-surface.md`
**Reports used:** compression bundle, critique-note, composition-friction-gate, connect (semantic bundle skipped — exploratory pass, not a promotion decision)

## Strongest retained claim

Bottom-up inference of *rationale-bearing* structure (the entities and relations that name why a decision went one way) from traces is feasible only when capture is decision-shaped rather than state-shaped, because the "why" is cheap to record at decision time and decays toward unrecoverable once only the resulting state remains. The italicized scope qualifier is new — see Body edits — and narrows the claim to defend it against critique-note's strongest attack, rather than leaving it stated as "structure" in general.

## Body edits

| Location | Source method(s) | Finding | Action | Rationale |
|---|---|---|---|---|
| "Capture position..." §, final sentence of paragraph 1 ("not an optimization... learnable at all") | critique-note, composition-friction-gate (joint 2) | Two independent methods converged on the same sentence: critique-note calls it a categorical overclaim the note's own Open Questions undercut; friction-gate flags it as UNSUPPORTED for the same reason (tension with the continuum admission). Independent corroboration, not a hedge. | reword to scope the categorical claim to "past whatever threshold," matching the note's own continuum admission | Keeps the qualitative-shift intuition without asserting a hard binary the note elsewhere disclaims |
| "Capture position..." §, paragraph 2 (wikiwiki-principle paragraph) | compression/branch-bloat, compression/marginal-value-redundancy | Narrates this note's relation to another note's claim; duplicates the Relevant Notes annotation for the wikiwiki link | replace with a new paragraph (below), keeping one clause ("deferring structure is safe... why does not wait") | Compression's suggested revision explicitly asked to preserve that one clause while cutting the rest |
| (new paragraph, same location) | critique-note (primary attack + constructive finding) | Strongest attack: decision/process mining recovers structural regularities from state-shaped event logs with no decision receipts — a working counterexample to "only if," at the population level. Critique's own fix: state explicitly which scope the claim targets. | add a paragraph distinguishing rationale-bearing structure (this note's target) from predictive regularities over an already-imposed state schema (what decision mining recovers), and note the distinction sharpens rather than resolves the note's own continuum open question | This is not a hedge against a possible objection — it is critique-note's constructive finding, independently reinforced by friction-gate's joint 2 on the adjacent sentence. Left un-engaged, the note's "only if" claim is contradicted by a real, cited research program. |
| "Boundary" §, paragraph 2 (create-memory-directly / trace-derived-extraction paragraph) | compression/branch-bloat, compression/marginal-value-redundancy | Duplicates the Relevant Notes annotations for `create-memory-directly.md` and `use-trace-derived-extraction.md` almost verbatim; doesn't bound this note's own claim the way paragraph 1 does | cut | Deletion test passes per the compression report — nothing in the note's support route depends on it |
| "The 'why' is cheap..." §, sentence 3 | compression/detail-overhang (INFO) | Re-lists the intro's decision-shaped/state-shaped item inventory in near-synonymous form | compress to a callback ("which of the inputs, constraints, or exceptions named above") | Lower priority than the WARNs above, but a safe, mechanical trim consistent with the INFO finding |

Not adopted: friction-gate's joints 1, 3, 4, 5 (the "nearly free" claim, the unsupported locality-of-intent mechanism, the "same gap" identity claim, and the "independent preconditions" claim) are real findings but not independently corroborated by another method, so per this instruction's rule they are **not** converted into edits here — see Routed attention below. Also not adopted: critique's secondary objections (the capture-schema-is-itself-upfront-imposition point, and the correlated-multi-stream recovery point) — both are real but read as hedges against edge cases the note's existing boundary language already gestures at; adding them would reopen the additive-apparatus failure mode compression is biased against.

## Routed attention (composition-friction-gate — not auto-resolved)

**Filter verdict:** SURVIVES — the apparent binary-vs-continuum tension resolves because the note's own Open Questions already supply the reconciling move (a threshold on a continuum is still a necessary condition).

**Thinnest joints (not converted into edits by this pass):**
1. "Recording those 'decision receipts'... is nearly free" — UNSUPPORTED — conflates the information being *available* at decision time with capturing it being *costless*; authoring/maintaining consistent capture across every decision path (including exceptions) is not argued to be free, only that the raw material is in hand.
2. *(Corroborated by critique-note — resolved above, not left routed.)*
3. "The reason is a locality property of intent..." — THIN — the note's single load-bearing mechanism, asserted once with no worked example or corroboration.
4. "This is the same gap [raw accumulation]... names as the ingress problem" — THIN — claims identity between this note's mechanism and the other note's, where the text only demonstrates analogy.
5. "...two independent preconditions on trace-derived memory... satisfying one says nothing about the other" — THIN — independence is asserted by architectural parallelism; a decision-shaped record (e.g., an approval-and-signoff receipt) plausibly correlates with easier verification, which the note doesn't rule out.

## Connection candidates (from connect report)

- `agent-memory-requirements/preserve-evidence-without-loading-history.md` — **extends** (add). That note requires capture to keep enough for later extraction and separate capture from activation; this note supplies the positional precondition it leaves open.
- `agent-memory-systems/lightweight/trajectory-informed-memory-generation.md` — **evidence** (add). A trace-extraction system whose tip categories are tied to outcome/exception shape — corroborating evidence for the claim, from a different collection.
- `distilled-artifacts-need-source-tracking.md` — **contrasts** (add, outbound only). Same locality-of-provenance principle applied to a different provenance kind (source-dependency vs. decision rationale). Connect flagged the reverse edge as the source-note author's judgment call; out of scope for this pass, which only edits the target note.

## Proposed revision shape

Same overall structure and length, net roughly neutral: the "Capture position" section's second paragraph is replaced (not just cut) with a scope-narrowing paragraph that does real argumentative work against critique-note's strongest attack; the "Boundary" section loses its second paragraph outright; the "why is cheap" section's redundant item-list sentence is trimmed to a callback. No section is removed, split, or rehomed — connect's own "not a split candidate" flag agrees. Footer gains three links.

## Open items

- Friction-gate's joints 1, 3, 4, and 5 remain genuinely open — they were deliberately not resolved by this pass (see "Routed attention"). A future editor should judge whether any deserves a real fix; this instruction does not decide that for them.
- Whether the rationale-vs-regularity distinction added to the "Capture position" section actually survives a second adversarial pass (i.e., whether a sufficiently rich state-shaped log could still be argued to name new rationale entities, not just fit a rule over given fields) is left as the sharpened form of the note's own second Open Question, not resolved here.
