# Workshop: Philosophy Borrowing

## Question

Which philosophy concepts are worth borrowing into commonplace methodology because they improve how agents write, review, maintain, or type KB artifacts?

## Why this workshop exists

The KB already borrows from philosophy in a few targeted ways: Popper for falsifiability and criticism, Deutsch for explanatory reach, Toulmin for argument structure, and Carnap's explication as a prior-work analogue for constraining. Those borrowings work because they map onto concrete KB operations rather than functioning as decorative vocabulary.

This workshop keeps that adoption bar. It considers only the three most promising new candidates from the current discussion, plus an expansion of the existing Carnap connection:

- Peirce's abduction for note promotion from observations to explanatory hypotheses
- Quine's web of belief for high-reach revision and downstream staleness
- Speech-act theory for document types as actions in the KB
- Carnap's explication for turning vague operational vocabulary into constrained KB terms

## Current grounding

- [Programming patterns get a fast pass but other borrowed ideas must earn first-principles support](../../notes/programming-patterns-get-a-fast-pass-but-other-borrowed-ideas-must-earn-first-principles-support.md) — adoption filter for borrowing outside programming
- [Mechanistic constraints make Popperian KB recommendations actionable](../../notes/mechanistic-constraints-make-popperian-kb-recommendations-actionable.md) — existing Popperian borrowing
- [First-principles reasoning selects for explanatory reach over adaptive fit](../../notes/first-principles-reasoning-selects-for-explanatory-reach-over-adaptive-fit.md) — existing Deutsch borrowing
- [Claim notes should use Toulmin-derived sections for structured argument](../../notes/claim-notes-should-use-toulmin-derived-sections-for-structured-argument.md) — existing Toulmin borrowing
- [Constraining](../../notes/definitions/constraining.md) — current home of the Carnap explication reference
- [Document types should be verifiable](../../notes/document-types-should-be-verifiable.md) — type semantics the speech-act candidate may sharpen
- [Brainstorming: how reach informs KB design](../../notes/brainstorming-how-reach-informs-kb-design.md) — maintenance risk from high-reach revisions, relevant to Quine

## Candidate artifacts

- [Peirce: abduction](./peirce-abduction.md) — note promotion as inference to the best explanation
- [Quine: web of belief](./quine-web-of-belief.md) — revision impact scales with centrality and reach
- [Speech acts](./speech-acts.md) — document types as KB actions rather than subjects
- [Carnap: explication](./carnap-explication.md) — concept-sharpening as a specific constraining operation

## Evaluation criteria

For each candidate, ask:

1. What concrete KB operation would change?
2. Which existing failure mode does the concept explain or prevent?
3. Can the borrowing be expressed as a checklist, review gate, type rule, or maintenance workflow?
4. What would make the borrowing decorative rather than operational?

## Working synthesis

The strongest common thread is not "philosophy helps KBs." It is that several philosophical ideas name operations this KB already performs informally:

- Abduction names how observations become candidate explanations.
- Web-of-belief names why central high-reach notes require special revision handling.
- Speech acts name why types should encode what a document does for the system.
- Explication names how vague vocabulary becomes precise enough to constrain future interpretation.

The likely output is not a single philosophy note. The better path is probably four small operational notes, each connected to an existing workflow: note promotion, staleness/revision, type-system semantics, and definition writing.

## Open questions

- Should abduction become a review prompt for turning logs into notes, or just a note explaining promotion quality?
- Does Quine add anything beyond the existing reach-maintenance note, or does it mainly supply a better theoretical frame?
- Can speech-act theory improve type definitions without creating a parallel taxonomy that competes with the current base-type + trait model?
- Should Carnap's explication stay as a line in `constraining`, or become its own definition-writing methodology note?
