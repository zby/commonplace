---
name: cp-skill-snapshot-web
description: Snapshot a URL into the local kb/sources/.snapshots/ cache, routing GitHub, X/Twitter, PDF, and ordinary web sources to the appropriate capture path.
type: kb/types/instruction.md
user-invocable: true
allowed-tools: Read, Write, Grep, Glob, WebFetch, Bash
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

Set `pdf_url`:

- For an arXiv abstract URL, replace `/abs/` with `/pdf/` and discard any query string or fragment. Preserve an explicit terminal version such as `v1`. If the abstract URL has no terminal version, leave the PDF URL unversioned so arXiv serves the latest paper version. For example, `https://arxiv.org/abs/2606.03979` becomes `https://arxiv.org/pdf/2606.03979`. Do not fetch the abstract page with WebFetch.
- For an existing PDF URL, use `source_url` unchanged.

Download the PDF to a temporary file:

```bash
curl -fsSL -o /tmp/snapshot_download.pdf "{pdf_url}"
```

Then use the Read tool to read the PDF:
- For short papers (< 20 pages): `Read(file_path="/tmp/snapshot_download.pdf")`
- For longer papers: read in chunks using the `pages` parameter (max 20 pages per request), e.g. `pages: "1-20"`, then `pages: "21-40"`, etc.

Set `capture_method` to `pdf-read` and go to **Step 4**.

### Step 2d: Fetch Web Page

Use WebFetch with this prompt:

> Extract the main article/post content from this page as clean markdown.
> Return ONLY the content — no navigation, sidebars, ads, cookie banners, or boilerplate.
> Preserve: headings, block quotes, code blocks, links, lists, emphasis.
> For blog posts: include the author name, publication date, and tags if visible.
> If the page has no extractable content (login wall, JS-only, error page), say "NO_CONTENT:" followed by a brief reason.

Set `capture_method` to `web-fetch` and go to **Step 4**.

## Step 3: Handle Failures

If any fetch method fails (WebFetch NO_CONTENT, curl error, script error):
- Tell the user what happened
- Suggest they paste the content manually: "You can paste the text and I'll save it as a snapshot"
- Stop

## Step 4: Determine Metadata

**(Only for PDF and web page paths — GitHub and X scripts handle their own metadata.)**

This workflow supplies `kb/sources/types/snapshot.md` as the type. Open that path and verify from its own frontmatter that it is a type spec before determining metadata. Stop if it is missing or invalid.

From the fetched content and `source_url`, determine:

- **title**: The article/post title. Use the first H1 if present, otherwise derive from content.
- **author**: If identifiable from the content or URL (e.g. simonwillison.net → Simon Willison)
- **genre**: the source's genre per the snapshot type spec's vocabulary. This is a surface judgment of what kind of document the source is as evidence — ingestion may correct it later. Prefer a value from the type spec's list; a value outside it validates with a warning, so extend only for a genuinely new evidential kind, not a container.
- **description**: One sentence describing what makes this source worth retrieving. Not a summary — a retrieval filter (e.g. "Anthropic CEO's capability-timeline predictions — verifiable domains get confident timelines, unverifiable ones get hedged"). Focus on what distinguishes this source from others on the same topic.
- **slug**: Lowercase, hyphenated, max 70 chars. Derived from title. Example: `simon-willison-karpathy-claws`

For academic papers: prefer the paper title over any page title, and extract authors from the author list.

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

For PDFs: convert the read content to clean markdown. Preserve section structure, tables, and lists. Drop page numbers, headers/footers, and layout artifacts.

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
- Clean up temporary PDF files after reading
