# Theory proposals

Finished but unadopted theory: frameworks, distinctions, terms, and changes
to adopted definitions that the KB has not decided to import into its
vocabulary. A proposal is here because adoption is undecided, not because
its content is doubtful. Much of it may be careful, or standard elsewhere.
The undecided question is whether the KB wants to carry the distinctions:
every adopted term has to be maintained, used consistently, and loaded by
every reader.

Every file in this directory is live and undecided, so listing the
directory answers "what theory is waiting for a decision". It is the
counterpart, for theory, of the unadopted system designs in
[`kb/reference/proposals/`](../../reference/proposals/README.md). A
conjecture that needs no new vocabulary does not belong here; it is an
ordinary note that states its conjectural force.

## Contract

- **Finished.** A proposal reads on its own, without the conversation or
  workshop that produced it. Material still being worked out stays in
  `kb/work/`.
- **Labelled.** The frontmatter description begins with "Proposal:".
- **Opens with the import.** The opening states what adoption would add
  (which terms and distinctions) and what it would change (which
  definitions, notes, and articles).
- **Names its trigger and cost.** A proposal says what need would justify
  importing it, such as a note or an experiment that cannot state its claim
  without the distinction, and what adopting it would commit the KB to.
- **Nothing rests on it.** Other notes may point to a proposal. They do not
  cite it as a premise, and they do not use its terms as settled
  vocabulary.
- **Untagged.** Proposals stay out of the tag indexes. The directory
  listing is their index.

Proposals are `note`-typed and follow the rest of the
[collection contract](../COLLECTION.md), except that a proposal holding a
framework of several claims may use a topic title.

## Lifecycle

Workshop (`kb/work/`, active, closes) → proposal here (finished, undecided,
waits) → adoption or deletion.

Adoption moves the content out: terms become definition notes under
[`definitions/`](../definitions/) and, when they are everyday vocabulary,
entries in the `AGENTS.md` vocabulary; claims become ordinary notes; the
affected definitions and articles are edited. What was adopted is removed
from the proposal, and a proposal with nothing undecided left is deleted.
A proposal whose trigger has clearly failed to arrive is deleted too. Git
keeps both.
