# Writing conventions for kb/work/ (workshop layer)

<!--
This is your project's workshop collection. Once installed, this contract
belongs to your project; Commonplace does not synchronize it with later
changes to this template. Adapt the generic rules below when the project
needs a narrower workshop policy.
-->

## Purpose and scope

This collection holds in-flight work: drafts, investigations, scratch notes,
pasted traces, and migration plans. It is a workshop layer, not a register.
Workshops may mix theoretical drafts, descriptive sketches, and procedures.

## Quality goal

Move the work forward, and extract durable conclusions when it closes. A
finished workshop produces library artifacts (notes, reference, instructions)
and is then deleted.

Plain Markdown without frontmatter is fine. So are imported or transitional
files with incomplete frontmatter. Do not add structure to workshop files
unless it helps the work continue or makes later extraction easier.

## Structure

Substantial work lives in a named subdirectory `kb/work/<workshop-name>/` with
a short `README.md` that says what the work is, who asked for it, and what
would close it. Small one-off files can live directly under `kb/work/` until
they are deleted or grow into a workshop.

List each active workshop with a one-line entry in
[`kb/work/README.md`](./README.md). Add the entry when the workshop starts and
remove it when the workshop closes.

## Titles and descriptions

No constraint. A title fits whatever the workshop produces: a claim, topic,
plan, or question.

## Outbound links

Workshops may cite any collection to ground their work. Inline links carry
load-bearing relationships. Footer links use a label plus a context phrase:
`- [title](path) — label: context phrase`. Labels here are suggestions, not
an authorised set; the reader must still gain something concrete by following
the link.

Other collections do not link into `kb/work/`. If a workshop produces
something they should cite, extract it into that collection first.

## Closing a workshop

When the workshop's question is answered, move its durable conclusions into
the right collection, delete the workshop directory, and remove its entry from
`kb/work/README.md`.

## Type eligibility

An artifact under `kb/work/` may use any valid type spec in the project, named
by its path, or a global Commonplace type, named by its bare name. This lets a
workshop stage an artifact for its target collection and test that
collection's contract. Frontmatter-free Markdown is implicit `text`.
