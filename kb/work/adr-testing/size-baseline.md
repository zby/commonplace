# ADR size baseline

Measured 2026-10-30 against checkout HEAD `b82ba30b4bf45b63601fe2434e6e9ba900b53e41`. The ingest created earlier in this session was untracked; it is outside this measurement. ADR inputs were unchanged according to Git status.

## Method

Read every numeric-prefixed `kb/reference/adr/*.md` file as UTF-8. Classify by frontmatter `status`. Extract exact level-two sections with headings Decision and Consequences, case-insensitively. Count whitespace-separated words and Unicode characters. Token estimates are characters divided by four, rounded; no tokenizer was used. Full-document counts include frontmatter and links. Section counts exclude the section heading. Consequences may include limits and operativity paths, but selecting these sections is not a semantic extraction of commitments.

The paired inventory records exact-file SHA-256 for each input; recomputation must check these hashes or identify a new observation.

## Results

| Set | Documents | Material | Characters | Words | Rough tokens |
|---|---:|---|---:|---:|---:|
| All ADRs | 122 | Full documents | 828,708 | 114,719 | 207,177 |
| All ADRs | 122 | Decision | 248,605 | 35,616 | 62,151 |
| All ADRs | 122 | Decision + Consequences | 451,873 | 63,202 | 112,968 |
| Accepted | 108 | Full documents | 752,815 | 104,456 | 188,204 |
| Accepted | 108 | Decision | 226,201 | 32,403 | 56,550 |
| Accepted | 108 | Decision + Consequences | 409,035 | 57,346 | 102,259 |
| Superseded | 14 | Full documents | 75,893 | 10,263 | 18,973 |
| Superseded | 14 | Decision | 22,404 | 3,213 | 5,601 |
| Superseded | 14 | Decision + Consequences | 42,838 | 5,856 | 10,710 |

Median accepted document: full 6004 characters, Decision 1745 characters, Decision + Consequences 3306 characters.

## Interpretation and limits

Accepted is a document status, not a guarantee that every commitment remains current. Superseded documents can retain surviving commitments. These are size proxies, not upper or lower bounds on the true current commitment set. Requirements also live outside ADRs. This measurement does not establish task-level selection quality, area boundaries, context occupancy, or whether prose can be safely shortened.

Full accepted documents are roughly 188k estimated tokens; Decision + Consequences roughly 102k. Task-specific subsets may be much smaller, but no feature-specific subset has yet been independently selected or checked. Ten median-sized full ADRs would be about 15k estimated tokens; that arithmetic is an illustration, not an observed task bundle.

## Input inventory

[Per-ADR counts and hashes](./size-inventory.tsv) permit later comparison without confusing content changes with improved selection.
