# Writing conventions for kb/notes/

<!--
This is your project's notes collection. The shipped Commonplace library
has its own conventions at kb/commonplace/notes/COLLECTION.md — read
that for a worked example. Replace these placeholders with your own
decisions. Once installed, this contract belongs to your project;
Commonplace does not synchronize it with later changes to this template or
to the worked example.
-->

## Purpose and scope

<!--
State directly what artifacts in this collection contribute and what belongs
or does not belong here. A typical notes collection retains claims,
mechanisms, definitions, and synthesis used to reason about the project's
domain. Write the operative conventions in this file in full.
-->

## Quality goal

<!-- What makes a note worth keeping in this collection? Example:
"A note is worth keeping when it changes how a reader would build or
operate something." -->

## Title and body conventions

<!-- How should titles be formed? How long should notes be? -->

## Outbound links

<!--
Which collections does this one link into, with which labels?
See kb/commonplace/reference/link-vocabulary.md for the shipped vocabulary.
-->

## Type eligibility

A typed artifact in this collection may use a global type spec under `kb/types/` or a local type spec under this collection's `types/` directory. Its `type:` value is the path to that contract. Frontmatter-free Markdown is implicit `text`.
