---
description: "Use when an artifact's TL;DR uses terms it never defines, ends on jargon, or its title carries a metaphor or bare term that reads wrongly before the body explains it"
type: kb/types/instruction.md
effort: judgment
---

# Opening and title

Make the TL;DR readable by someone who will read nothing else, and the title a
literal statement of the artifact's central contrast.

Effort: judgment. Title proposals need judgment; the TL;DR edits alone may run as simple.

TL;DR:

- Use only terms the TL;DR itself introduces. Where the body's technical term
  appears, replace it with the plain description the TL;DR gave earlier, so
  the opening ends where it began.
- State the alternative the artifact denies in one sentence, so the reader
  knows what is at stake before the argument.
- Cut words that add no content ("some software" is "software").
- Identify a named person at first mention, in the sentence, not inside a
  link.
- Define a term at its first use. Do not delete a term the body relies on
  later; a plain-language opening that drops it leaves a later section using
  it cold.
- When a term appears only in a link entry or only in the body, search the
  KB for inbound uses before choosing which side to fix. A term other notes
  cite this artifact as the source of stays, and is introduced in the body.

Title:

- Keep the half that names the claim. Replace a metaphor or a bare term with
  the full term and the literal contrast ("the LLM stays fixed, the software
  house learns", not "train the house").
- Check the slug the title would produce against the 70-character limit
  before proposing it.
- Propose the title; do not apply it. A title change also changes the file
  slug, which is a separate pure relocation commit.

Report: old and new TL;DR, proposed titles with one line each on what each
emphasizes, and the slug length.
