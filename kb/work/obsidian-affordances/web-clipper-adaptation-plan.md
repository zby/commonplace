# Web Clipper Adaptation Plan

Concrete steps to adapt Obsidian Web Clipper into commonplace's source workflow without collapsing capture, graph integration, and analysis into one tool.

Each step should produce a working state. We do not need to finish the whole plan before the workflow becomes useful.

## Step 1: Define the target scope and source contract

Decide exactly which source classes Web Clipper is supposed to handle first.

Initial scope:

- ordinary web articles
- blog posts
- documentation pages that render cleanly in the browser

Explicitly out of scope for the first pass:

- GitHub issues and PRs
- X / Twitter posts
- PDFs
- headless or agent-triggered capture with no browser present

Also define the minimum snapshot contract for a clipped source file in `kb/sources/`.

The first-pass contract should be close to the current snapshot shape:

```yaml
---
source: {url}
description: {retrieval filter or temporary placeholder}
captured: {date}
capture: web-clipper
type: {blog-post|documentation|web-page|news-article}
---
```

Body should preserve:

- title
- author if available
- date if available
- cleaned article content

**Done when:** we have one explicit statement of what Web Clipper is for, what it is not for, and what a valid clipped source file must contain.

## Step 2: Design the first Web Clipper template

Create a Web Clipper template that writes directly into `kb/sources/`.

The template should optimize for:

- stable filenames/slugs
- enough frontmatter for `/ingest`
- preserving readable article structure
- minimal manual cleanup

Prefer a conservative template over a clever one. The first version should avoid ambitious transformations and focus on producing a clean snapshot.

First-pass template goals:

- path target: `kb/sources/{slug}.md`
- frontmatter values filled from page metadata where reliable
- article body extracted as markdown
- if a good discriminating `description` cannot be generated reliably, allow a temporary placeholder and let `/ingest` sharpen it

This is an important decision: Web Clipper does not need to solve the whole retrieval-filter problem on day one if that makes clipping brittle.

**Done when:** a single template can clip a representative article into `kb/sources/` with acceptable structure and no post-processing script.

## Step 3: Define the default human workflow

Make the preferred workflow explicit:

1. Clip page with Obsidian Web Clipper
2. Save into `kb/sources/`
3. Run `/ingest {clipped-file}`

The key architectural change is social as much as technical: browser-driven source capture stops being "ask `/ingest` to fetch a URL" and becomes "clip first, then ingest the saved artifact."

This gives us a cleaner separation:

- Web Clipper owns browser UX
- `/ingest` owns graph-aware analysis
- `/connect` owns connection discovery

**Done when:** we have a short written procedure that can replace "use `/ingest URL`" for ordinary browser capture.

## Step 4: Adapt `/ingest` to be smoother on clipped files

The current `/ingest` flow already accepts a file path, which means the main adaptation may be procedural rather than architectural.

Check what assumptions `/ingest` currently makes about snapshots:

- required frontmatter fields
- naming conventions
- whether `description` quality is assumed at snapshot time
- whether clipped files need any normalization before `/connect`

Only change `/ingest` if the clipped file format reveals real friction.

Likely improvements if needed:

- better tolerance for Web Clipper-produced frontmatter
- clearer output when ingesting a locally clipped file
- stronger "file-first" guidance in docs or skill description

Avoid rewriting `/ingest` around Web Clipper prematurely. The first question is whether the existing file-input path already works well enough.

**Done when:** a clipped file can be passed to `/ingest` cleanly and the workflow feels natural enough to repeat.

## Step 5: Keep selective fallback paths

Do not delete the bespoke capture paths just because Web Clipper handles ordinary articles better.

Retain script or skill fallbacks for:

- GitHub issue / PR capture
- X / Twitter capture
- PDF capture
- non-browser automation

If Web Clipper becomes the default human-facing capture layer, `/snapshot-web` can narrow rather than disappear.

The likely end state is:

- Web Clipper for ordinary human browser capture
- `/snapshot-web` for special source types and automation

**Done when:** we have an explicit split between "default browser capture" and "special-case fallback capture."

## Step 6: Evaluate whether the generic web-page path should be deprecated

After some real use, decide whether the generic web-page branch of `/snapshot-web` is still worth maintaining.

Questions to answer after usage:

- Is Web Clipper more reliable than the current generic web fetch path?
- Does it produce better markdown with less cleanup?
- Is the manual browser step acceptable for most actual source capture?
- How often do we still need headless generic capture?

Deprecation should be evidence-driven. If the generic path remains useful for automation or remote execution, keep it.

**Done when:** we have enough usage to justify either narrowing or preserving the generic web-page path.

## What to skip for now

- full replacement of `/ingest`
- automatic `/connect` triggering from the browser
- immediate migration of all historical capture workflows
- trying to make Web Clipper handle GitHub, X, and PDFs uniformly on day one
- large `.obsidian/` workspace configuration unrelated to source capture

## Recommended implementation order

1. write the source contract
2. build the first Web Clipper template
3. test clip -> `/ingest file`
4. document the preferred workflow
5. keep special-case fallbacks
6. only then consider deprecating parts of `/snapshot-web`

## Success criteria

- clipping an ordinary article into `kb/sources/` is easier than the current bespoke path
- `/ingest` still produces graph-aware analysis without architectural compromise
- the new workflow reduces maintenance burden rather than creating a second fragile ingestion stack
- special source types still have a reliable path
