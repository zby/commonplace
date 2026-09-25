# Proposal: gradual exposure for the compounding note

Candidate: [proposed_gradual.md](./proposed_gradual.md). It is a manual proposal written after the AutoReason trial, not an output of that trial. It starts from `current_a.md` because the operator found the AutoReason winner still hard to read.

## Why `current_a.md` is hard to read

- **It opens with the conclusion in its most compressed form.** The first paragraph gives two hypotheses. The second says the measurement is "displaced twice". Neither has been grounded in a case yet.
- **Terms arrive before they are defined.** *Accepting metric*, *later improvement episode*, *displaced measure*, *uptake*, *allocator*, and *reinvestment* are used before the reader has a picture to attach them to.
- **Its examples are fleeting.** The coverage validator and the search recipe each get half a sentence. After that, the concrete material is the three studies, and each study brings its own vocabulary: hyperagents, Improvement@50, Phase 1/2, and the harness ladder.
- **Protocol parts are separated from the requirements they serve.** The measures table and the baselines come after the three studies. So the reader meets the studies before having the full test the studies are read against.

## What the proposal changes

1. **One running example.** A hypothetical search-recipe fix (episode 1) is followed by a link diagnosis five weeks later (episode 2). The note already named the search recipe, so the example uses its own case. Every requirement is shown on this example before it is stated in general form.
2. **Requirements in order.** The body builds the claim one step at a time: why the acceptance record cannot decide the question → later episode → different measure (with the table) → causal trace (direct, then indirect with a worked "freed hour") → baselines → noticing.
3. **Terms defined at first use.** *Accepting metric* and *displaced* are defined where they first appear, and each is tied to the example.
4. **Studies last, read against an explicit ladder.** The six rungs are accepted → retained → taken up → displaced gain → attributed → sustained. Each study heading now says where that study stops. The ladder repackages requirements the note already had; it does not add a claim. Harness Benefit's own ladder is presented as a finer view of the early rungs.

## Preservation

The title, description, frontmatter, study numbers, qualifications, scope bullets, open questions, and Relevant Notes are copied unchanged. Paragraphs from `current_a.md` are kept verbatim where possible. New text is limited to the example, the definitions at first use, the ladder, and the transitions between sections.

The note is about 25% longer. The added length is concrete illustration, not new claims.

## Risks for review

- **The example is invented.** It is labelled hypothetical. A real Commonplace episode could replace it if one has traces good enough to use, for example from `evidence/commonplace-as-a-reflective-system.md`.
- **The ladder adds structure.** Placing "taken up" before "displaced gain" is a presentation choice. The original treats the measure and the trace as jointly required, not as ordered steps.
- **"Rungs 3–5 together are local evidence" is a new sentence.** It restates the first Scope bullet in ladder terms. Check that it does not overstate that bullet.
- **Validation.** Not run in this workshop, because relative links resolve from `kb/notes/`. Run `commonplace-validate` after copying the file to the live path.
