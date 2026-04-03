# Obsidian Web Clipper As A Capture Layer

## Core idea

The most obviously useful Obsidian affordance for commonplace is not graph view, Canvas, or wikilinks. It is the **Obsidian Web Clipper** extension.

The strongest version of the idea is:

- use Web Clipper to capture source material into `kb/sources/`
- keep `/ingest` for connection discovery, classification, extraction, limitations, and next-action recommendations

That means Web Clipper would replace the **capture** half of our current ingestion pipeline, not the entire ingestion system.

## Why this is attractive

Our current source workflow has two distinct phases that are easy to conflate:

1. **Capture** — fetch the URL, clean it up, save it into `kb/sources/`
2. **Ingest** — connect the saved snapshot to the KB and write the `.ingest.md` analysis

The current `/ingest` skill already makes this split explicit by calling `/snapshot-web` first when the input is a URL, then running `/connect`, then writing the analysis artifact.

Web Clipper looks like a much stronger human-facing tool for the first phase:

- browser-native capture flow
- templateable output
- direct save into the vault
- easier everyday clipping than our current bespoke route

This could let us stop investing in a general-purpose browser capture interface of our own.

## Important boundary

Web Clipper does **not** replace the whole ingest workflow.

It does not know:

- which existing notes a source connects to
- what relationship types those connections should carry
- what is genuinely new relative to our existing graph
- what limitations we should assign to the source
- what the recommended next action should be

Those are exactly the responsibilities that still belong to `/ingest`.

So the right framing is:

- **replace `/snapshot-web` for suitable cases**
- **keep `/ingest`**

## Proposed workflow

For ordinary web articles and documentation:

1. Use Obsidian Web Clipper to save the page into `kb/sources/`
2. Run `/ingest {clipped-file}`
3. Let `/ingest` run `/connect`, classify the source, and produce `{file}.ingest.md`

This is cleaner than asking `/ingest` to also be the primary browser-capture UX.

## What this likely replaces

- manual or semi-manual web-page clipping into `kb/sources/`
- much of `/snapshot-web`'s generic web-page capture path

## What this probably does not replace

- GitHub issue / PR snapshotting with repo-specific handling
- X / Twitter capture paths
- PDF-specific extraction
- headless or agent-triggered URL capture where no human browser is present

Those may still need a script path, or at least a fallback path.

## Recommended direction

Treat Web Clipper as the **default human capture interface** for ordinary web sources, not as a full ingest replacement.

That implies a cleaner architecture:

- **capture layer:** Obsidian Web Clipper and maybe a few scripts for special source types
- **analysis layer:** `/ingest`
- **graph integration layer:** `/connect`

This is a better decomposition than one monolithic ingest command that tries to own browser UX, source normalization, graph discovery, and editorial judgment at once.

## Open questions

- What Web Clipper template shape would best match `kb/sources/` conventions?
- Should clipped notes include enough frontmatter that `/ingest` can assume a cleaner, more regular input format?
- Which source classes should still route through bespoke scripts rather than Web Clipper?
- Should `/ingest URL` remain supported, or should the preferred workflow become "clip first, then ingest the saved file" for browser-driven capture?
