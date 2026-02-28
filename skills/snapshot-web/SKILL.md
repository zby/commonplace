---
name: snapshot-web
description: Snapshot any URL into kb/sources/. Routes by URL type — GitHub issues/PRs via gh API, X/Twitter via xdk, PDFs via download+Read, web pages via WebFetch. One skill, URL in, markdown snapshot out. Triggers on "/snapshot-web", "/snapshot-web [url]".
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

## Step 1: Check for Duplicates

Use Grep to search for the URL in existing `.md` files in `kb/sources/`. If found, tell the user and stop:

> Already snapshotted: kb/sources/{filename}

## Step 2: Route by URL Type

Detect the URL type and branch:

- **GitHub issue/PR** (`github.com/.../issues/N` or `github.com/.../pull/N`) → **Step 2a**
- **X/Twitter** (`x.com/.../status/...` or `twitter.com/.../status/...`) → **Step 2b**
- **PDF** (URL ends in `.pdf`, or `arxiv.org/pdf/`) → **Step 2c**
- **Everything else** → **Step 2d**

### Step 2a: GitHub Issue/PR

Run the snapshot script:

```bash
uv run kb/scripts/github_snapshot.py "{url}"
```

Parse the "Snapshot saved:" line from the output to get the file path. Tell the user and stop — the script handles metadata, formatting, and saving.

### Step 2b: X/Twitter Post

Run the snapshot script:

```bash
uv run kb/scripts/x_snapshot.py "{url}"
```

Parse the "Snapshot saved:" line from the output to get the file path. Tell the user and stop — the script handles metadata, formatting, and saving.

### Step 2c: Fetch PDF

Download the PDF to a temporary file:

```bash
curl -sL -o /tmp/snapshot_download.pdf "{url}"
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

From the fetched content and URL, determine:

- **title**: The article/post title. Use the first H1 if present, otherwise derive from content.
- **author**: If identifiable from the content or URL (e.g. simonwillison.net → Simon Willison)
- **type**: One of: `blog-post`, `documentation`, `forum-thread`, `news-article`, `academic-paper`, `web-page` (default)
- **slug**: Lowercase, hyphenated, max 70 chars. Derived from title. Example: `simon-willison-karpathy-claws`

For academic papers: prefer the paper title over any page title, and extract authors from the author list.

## Step 5: Write the Snapshot

Save to `kb/sources/{slug}.md` with this format:

```markdown
---
source: {url}
captured: {YYYY-MM-DD}
capture: {capture_method}
type: {type}
---

# {title}

Author: {author}
Source: {url}
Date: {publication date if known}

{extracted content}
```

For PDFs: convert the read content to clean markdown. Preserve section structure, tables, and lists. Drop page numbers, headers/footers, and layout artifacts.

Also tell the user where it was saved and show a 1-2 line preview.

## Critical Constraints

**Never:**
- Fabricate or hallucinate content not on the page
- Add analysis or commentary — this is capture, not ingestion
- Modify the extracted content beyond cleaning HTML/PDF artifacts
- Save to any directory other than `kb/sources/`

**Always:**
- Preserve the author's structure (headings, quotes, lists)
- Include the source URL in frontmatter
- Use today's date for `captured`
- Check for duplicates before fetching
- Clean up temporary PDF files after reading
