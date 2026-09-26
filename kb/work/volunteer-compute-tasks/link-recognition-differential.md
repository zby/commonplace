# Link recognition differential

Find Markdown links that Commonplace components recognize differently, then
propose one positioned link recognizer that could replace their private
patterns. The first stage returns small disagreement cases checked against an
independent renderer. The second stage uses those cases as the acceptance test
for the proposed function. Follow the [shared handoff](./README.md).

## Inputs and baseline

Several components each carry their own link pattern:

| Component | Pattern | Use |
|---|---|---|
| Validator, promotion, review prompts | `_LINK_RE` via `find_markdown_links` in [note_parser.py](../../../src/commonplace/lib/note_parser.py) | Link health; link sets |
| Relocation | `TOKEN_PATTERN` in [relocation.py](../../../src/commonplace/lib/relocation.py) | Rewriting links when an artifact moves |
| Package build | `LINK` in `hatch_build.py` at the repository root | Redirecting links that leave the shipped trees; failing on dead links |
| Quote verification | `LINK_RE` in [quote_verification.py](../../../src/commonplace/lib/quote_verification.py) | Pairing verbatim quotes with cited sources |
| Link audit extraction | `_LINK_RE` in [link_audit.py](../../../src/commonplace/lib/extraction/link_audit.py) | Auditing links line by line |

They differ in how they treat fenced and inline code, titles, angle-bracket
targets, and brackets inside link text. The published site uses neither: it
renders pages with Python-Markdown through ProperDocs, configured by
`properdocs.yml` at the repository root.

The [validation contract](../../reference/validation-contract.md#open)
already names the missing shared, positioned link representation. The
[graph-loader workshop](../kb-graph-loader/README.md) owns where such a
representation lives. This task supplies evidence and a candidate recognizer; it
does not design the loader.

```bash
python -m pytest tests/commonplace/lib/test_note_parser.py tests/commonplace/cli/test_relocate_note.py tests/commonplace/test_quote_verification.py tests/commonplace/test_library_build.py
```

## Stage 1: disagreement search

Use Python-Markdown, with the extension set that `properdocs.yml` configures, as
the independent reference for which text renders as a link and to which target.
Collect the `href` of every rendered anchor. Do not use any Commonplace pattern
to compute the expected result.

Generate Markdown documents and run each component on them through its normal
entry path where practical: validation of a temporary KB, a relocation that
should rewrite the link, a library build, and quote verification over a
citing note. Compare each component's recognized links, targets, and anchors
with the renderer. Candidate families include inline and reference-style links,
titles in each quote style, angle-bracket targets, spaces and percent-encoding,
parentheses and brackets in targets or text, escaped characters, images, links
inside fenced blocks, indented code, inline code, HTML, and blockquotes, and
fences that other text makes unbalanced.

Before searching, write down the link syntax the committed contracts and
existing tests support. A disagreement within that syntax is a candidate
defect. A disagreement outside it goes on the ambiguous-requirements list; do
not report the renderer's broader syntax as a requirement by default.

Rank findings by consequence:

- A link the site renders but link health does not check, so a dead link can
  ship unreported.
- A link the validator checks but relocation does not rewrite, so a move breaks
  it.
- A link that leaves the shipped trees but the package build does not redirect
  or check, so the installed library carries a dead link.
- A code example that a component treats as a live link, or rewrites.

For each finding, supply the Markdown fixture, the renderer's anchors, each
component's result, and the command that shows the practical consequence.

## Stage 2: unified recognizer

After Stage 1 has returned at least one finding packet, propose one function
that recognizes links in a Markdown body. Each result should carry at least its
character span, target, anchor, title, and whether it lies in code. Spans must
let relocation and the package build rewrite one link and leave all other bytes
unchanged. The quote checker needs positions to pair quotes with citations by
proximity. Choose the implementation, whether a Markdown parser library or a
hand-written scanner, and justify it with the Stage 1 results. Any new runtime
dependency is a finding for the maintainer to decide, not a default.

Acceptance for the function:

- It agrees with the renderer on every generated case within the supported
  syntax, including a reserved set frozen before implementation.
- It reproduces the correct result for every Stage 1 finding.
- Rewriting each link through its spans and re-parsing gives the rewritten
  targets and leaves the rest of the document byte-identical.

Submit the function and its tests as one patch. Submit the adoption of one
caller, preferably `find_markdown_links`, as a separate patch that passes
`python -m pytest`. That patch lists every change in validation output on the
pinned `kb/notes`, `kb/reference`, and `kb/instructions` collections. Do not
migrate relocation, the package build, or quote verification. For each
remaining caller, state in a few lines what adoption would change. The
maintainer owns the supported syntax and all further integration.

## Stopping

If the supported syntax is too unclear to classify most disagreements, stop
after Stage 1 and return the ambiguous-requirements list. If no single function
can meet every caller's needs, report which needs conflict and which cases show
it, rather than weakening a caller.
