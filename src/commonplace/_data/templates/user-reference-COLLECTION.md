# Writing conventions for kb/reference/

<!--
This is your project's reference collection. The shipped Commonplace
library has its own conventions at kb/commonplace/reference/COLLECTION.md
for a worked example. Replace these placeholders with your own decisions.
Once installed, this contract belongs to your project; Commonplace does not
synchronize it with later changes to this template or to the worked example.
-->

## Purpose and scope

<!--
State directly what artifacts in this collection describe and what belongs
or does not belong here. A typical reference collection documents the current
system, architecture, interfaces, and decision history. Write the operative
conventions in this file in full.
-->

## Quality goal

<!-- What makes a reference doc worth keeping here? Example:
"A reference doc is worth keeping when an agent or new contributor
needs it to understand or operate the system correctly." -->

## Title and body conventions

<!-- Titles are typically noun phrases naming the subject. How long
should reference docs run? -->

## Outbound links

<!--
Reference typically links to notes (grounds, rationale) and cites
sources. See kb/commonplace/reference/link-vocabulary.md.
-->

## Type eligibility

A typed artifact in this collection may use a global type spec under `kb/types/` or a local type spec under this collection's `types/` directory. Its `type:` value is the path to that contract. Frontmatter-free Markdown is implicit `text`.
