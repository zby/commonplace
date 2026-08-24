---
name: cp-skill-snapshot-web
description: Snapshot a URL into the local kb/sources/.snapshots/ cache, routing GitHub, X/Twitter, PDF, and ordinary web sources to the appropriate capture path.
type: kb/types/instruction.md
user-invocable: true
allowed-tools: Read, Write, Grep, Glob, Bash
context: fork
model: sonnet
argument-hint: "[url] — URL to snapshot (web page, PDF, GitHub issue/PR, or X/Twitter post)"
---

## EXECUTE NOW

**Target: $ARGUMENTS**

If no URL provided, ask the user for one.

If URL provided, start Step 1 immediately.

**START NOW.**

---

## Step 1: Verify Local Storage and Check for Duplicates

Keep the provided URL as `source_url`. Verify that
`kb/sources/.snapshots/` is ignored by the project. The shipped scaffold does
this through `kb/sources/.gitignore`. If the directory is not ignored, stop
before writing and report the missing rule.

Use Grep to search for an exact frontmatter `source: {source_url}` in existing
Markdown files in `kb/sources/.snapshots/`. If found, compute the SHA-256 of
the exact file bytes, tell the user, and stop:

> Already snapshotted: kb/sources/.snapshots/{filename}
> SHA-256: {64-character lowercase checksum}

## Step 2: Route by URL Type

Detect the `source_url` type and branch:

- **GitHub issue/PR** (`github.com/.../issues/N` or `github.com/.../pull/N`) → **Step 2a**
- **X/Twitter** (`x.com/.../status/...` or `twitter.com/.../status/...`) → **Step 2b**
- **arXiv abstract page** (`arxiv.org/abs/...`) → **Step 2c**
- **PDF** (URL ends in `.pdf`, or `arxiv.org/pdf/`) → **Step 2c**
- **Everything else** → **Step 2d**

### Step 2a: GitHub Issue/PR

Run:

```bash
commonplace-github-snapshot "{source_url}"
```

Parse either the `Snapshot saved:` or `Already snapshotted:` line from the
output to get the file path. Tell the user and stop — the script handles
metadata, formatting, and saving.

### Step 2b: X/Twitter Post

Run:

```bash
commonplace-x-snapshot "{source_url}"
```

Parse either the `Snapshot saved:` or `Already snapshotted:` line from the
output to get the file path. Tell the user and stop — the script handles
metadata, formatting, and saving.

### Step 2c: Resolve and Fetch PDF

Verify that the PDF capture prerequisites are available:

```bash
command -v curl
command -v pdfinfo
command -v pdftotext
```

If any command is missing, go to **Step 3**. Do not probe for an alternative
converter.

Set `pdf_url`:

- For an arXiv abstract URL, replace `/abs/` with `/pdf/` and discard any query string or fragment. Preserve an explicit terminal version such as `v1`. If the abstract URL has no terminal version, leave the PDF URL unversioned so arXiv serves the latest paper version. For example, `https://arxiv.org/abs/2606.03979` becomes `https://arxiv.org/pdf/2606.03979`. Do not route the abstract page through ordinary HTML capture.
- For an existing PDF URL, use `source_url` unchanged.

Run this as one Bash invocation. Retain the printed directory path as
`{snapshot_tmp}`:

```bash
set -e
snapshot_tmp=$(mktemp -d)
printf 'Snapshot temp: %s\n' "$snapshot_tmp"
curl -fsSL -o "$snapshot_tmp/source.pdf" "{pdf_url}"
pdfinfo -isodates "$snapshot_tmp/source.pdf" > "$snapshot_tmp/pdfinfo.txt"
pdftotext -enc UTF-8 -eol unix -nopgbrk \
  "$snapshot_tmp/source.pdf" "$snapshot_tmp/extracted.txt"
```

Use Read to inspect `pdfinfo.txt`, then read `extracted.txt` in chunks until
EOF. Treat `pdfinfo` fields as metadata leads, not as authority: confirm the
title and authors against the document text when available. If
`extracted.txt` is empty or contains no substantive text, go to **Step 3**.

Set `capture_method` to `pdftotext` and go to **Step 4**.

### Step 2d: Fetch Web Page

Verify that the HTML capture prerequisites are available:

```bash
command -v trafilatura
```

If the command is missing, go to **Step 3**. Do not probe for another HTML
converter.

Run this as one Bash invocation to download and extract the page. Retain the
printed directory path as `{snapshot_tmp}`:

```bash
set -e
snapshot_tmp=$(mktemp -d)
printf 'Snapshot temp: %s\n' "$snapshot_tmp"
trafilatura -u "{source_url}" \
  --markdown --with-metadata --links --no-comments --recall \
  > "$snapshot_tmp/extracted.md"
```

Use Read to inspect `extracted.md`. Its leading YAML block, when present, is
Trafilatura metadata: retain it as input to Step 4 but do not copy that block
into the snapshot body. If the file is empty or contains no substantive main
content, go to **Step 3**.

Set `capture_method` to `trafilatura` and go to **Step 4**.

## Step 3: Handle Failures

If any fetch or extraction method fails (missing prerequisite, curl error,
empty Trafilatura result, or PDF with no embedded text):

- Tell the user exactly what happened.
- For a missing prerequisite, name the canonical installation:
  - `trafilatura`: `uv tool install "trafilatura>=2.2"`
  - `pdfinfo` or `pdftotext`: install Poppler (`poppler-utils` on
    Debian/Ubuntu, `poppler` through Homebrew, or
    `oschwartz10612.Poppler` through WinGet)
  - `curl`: install curl
- For an image-only PDF, say that this workflow has no OCR fallback.
- Suggest they paste the content manually: "You can paste the text and I'll save it as a snapshot"
- Remove `{snapshot_tmp}` if one was created.
- Stop.

## Step 4: Determine Metadata

**(Only for PDF and web page paths — GitHub and X scripts handle their own metadata.)**

This workflow supplies `kb/sources/types/snapshot.md` as the type. Open that path and verify from its own frontmatter that it is a type spec before determining metadata. Stop if it is missing or invalid.

From the extracted content, extractor metadata, and `source_url`, determine:

- **title**: The article/post title. Use the first H1 if present, otherwise derive from content.
- **author**: If identifiable from the content or URL (e.g. simonwillison.net → Simon Willison)
- **genre**: the source's genre per the snapshot type spec's vocabulary. This is a surface judgment of what kind of document the source is as evidence — ingestion may correct it later. Prefer a value from the type spec's list; a value outside it validates with a warning, so extend only for a genuinely new evidential kind, not a container.
- **description**: One sentence describing what makes this source worth retrieving. Not a summary — a retrieval filter (e.g. "Anthropic CEO's capability-timeline predictions — verifiable domains get confident timelines, unverifiable ones get hedged"). Focus on what distinguishes this source from others on the same topic.
- **slug**: Lowercase, hyphenated, max 70 chars. Derived from title. Example: `simon-willison-karpathy-claws`

For academic papers: prefer the title and complete author list printed in the
paper over `pdfinfo` or Trafilatura metadata.

## Step 5: Write the Snapshot

Save to `kb/sources/.snapshots/{slug}.md` with this format:

```markdown
---
source: {source_url}
description: {description}
captured: "{YYYY-MM-DD}"
capture: {capture_method}
genre: {genre}
type: kb/sources/types/snapshot.md
---

# {title}

Author: {author}
Source: {source_url}
Date: {publication date if known}

{extracted content}
```

For PDFs: convert the extracted text to clean Markdown. Preserve section
structure, tables, and lists. Drop page numbers, repeated headers/footers, and
layout artifacts. For web pages: use Trafilatura's Markdown as the body after
removing its metadata block and any residual boilerplate; do not summarize it.

Compute SHA-256 after the file is complete. Hash the exact `.md` bytes,
including frontmatter, line endings, and the presence or absence of a final
newline. Do not include a PDF, JSON, image, or other capture companion. Tell
the user where the snapshot was saved, its lowercase checksum, and a one- or
two-line preview.

## Critical Constraints

**Never:**
- Fabricate or hallucinate content not on the page
- Add analysis or commentary — this is capture, not ingestion
- Modify the extracted content beyond cleaning HTML/PDF artifacts
- Save to any directory other than `kb/sources/.snapshots/`
- Install software — if a required tool is missing, bail with an error telling the user what to install

**Always:**
- Preserve the author's structure (headings, quotes, lists)
- Include the source URL in frontmatter
- Use today's date for `captured`
- Check for duplicates before fetching
- Keep the snapshot and every capture companion local and ignored
- Remove the unique temporary download/extraction directory after the snapshot
  is written and hashed
