---
participating: [notes, reference, instructions]
---

# Tag heads for kb/tags/

These defaults are ready to use. Customize them only when the project needs
different conventions. Once installed, this contract belongs to your project;
Commonplace does not synchronize it with later template changes.

## What this collection holds

One head per tag: `kb/tags/<tag>-README.md`, type `types/tag-readme.md`. The
filename names the tag. A head introduces what the tag gathers, in the words
a reader would search for, and picks a few entries with a phrase saying why
each matters. It is the page a tag link leads to on the published site.

Every tag in use has a head. Validation reports a tag on an artifact in a
participating collection whose head does not exist; write the head or drop
the tag. A tag not worth a head is not worth assigning.

## Participating collections

The `participating:` list in this file's frontmatter names the collections
whose `tags:` lines count as membership. Every completeness or coverage mark
on a head, and every generated tag listing on the site, ranges over exactly
those collections. Tags on artifacts elsewhere are not read. Add a collection
here to bring its tags into the tag space; nothing is inferred from the
directory tree.

## Marks

A head may declare `complete: true`: every member is linked from the head or
carries a tag whose head is linked from it, so the head reaches every member
in one hop. Validation checks the claim; drop the mark when it cannot be made
true. See the `tag-readme` type spec in the Commonplace library.

## Outbound links

Link members with a relative path (`../notes/<file>.md`) and a context phrase.
Link other heads under a `## Related Tags` heading. Do not link into
`kb/work/`.

## Type eligibility

Heads use the global `types/tag-readme.md`. `README.md` is this collection's
landing and carries no type.
