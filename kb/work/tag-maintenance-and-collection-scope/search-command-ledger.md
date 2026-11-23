# Search commands recommended in Commonplace instructions

**Finding, 2026-11-23:** `rg` is the default for finding candidate KB documents by text. It is not the only recommended search tool. More importantly for tagging, the same `rg` expression serves two different purposes today: *find plausible reading* and *enumerate every member*. Only the second must agree exactly with the validator and the published listing.

## Coverage and reading key

Baseline: `5be94e42e`. Searched the 150 tracked files in `kb/instructions/`, `kb/agentic-system-analyses/instructions/` and `kb/agentic-systems/instructions/`, including nested skill references and worker instructions. Checked inline examples, fenced commands and prose naming a search tool, not just occurrences of `rg`. Also checked root agent instructions and their scaffold counterparts. Selected companion contracts and reference recipes are identified separately below. Do not count skill symlinks, report copies, historical proposals or workshop drafts as additional prescriptions.

The unit is a recommended local lookup of content, files, or history, not every occurrence of a tool name. A pipeline is one lookup. Related occurrences share a row with line locators at the baseline; command signatures below are abbreviated where the original gives a pipeline or repeats the same paths. Tool allowlists are not recommendations. Reading a known path, validating or running a workflow, searching the open web and requests to reason about a passage are not search commands. Tool-neutral directions are not evidence for `rg`; a few that matter to scope are called out separately.

Unless qualified, locators below are relative to `kb/instructions/`; skill names refer to their `SKILL.md`.

## Candidate discovery and tag maintenance

| Instruction : line | Command or recommendation | What it searches for, and where |
|---|---|---|
| `maintain-curated-indexes.md:23–25` | `rg -N --no-heading '^tags:'` → `grep -o '\[.*\]'` → split and count | Tag sizes across five literal roots: theory, reference, instructions, agent-memory-systems and agentic-systems. Omits participating `reports`; does not apply the collector’s exclusions. |
| `maintain-curated-indexes.md:35–36` | `rg -l '^tags:.*\bTAG\b'` → `xargs -r rg … '^description:\s*'` | Purports to list full membership across the same five roots. A word boundary also matches before a hyphen: searching for `foo` can pick up `foo-bar`. Line matching is not YAML parsing. |
| `maintain-curated-indexes.md:51` | `rg -L "^tags:" kb/theory/*.md` | Intended to find untagged notes. In ripgrep `-L` follows symlinks; this prints **matching** lines. The shell glob also limits it to top-level Markdown, not all eligible theory notes. |
| `cp-skill-connect:63,82–86` | Same by-tag → description pipeline, but under `kb/<destination>/`; skip it for a `complete` head | Topic candidates in one authorized destination at a time. A complete head says nothing about tagged sources outside the participating set. Keep destination selection; revisit the skip condition separately. |
| `cp-skill-connect:67,73` | `rg -N --no-filename -m1 '^# (.*)' -r '$1' …`; `rg -l -F -x '# <title>' …` | First scan titles in the destination’s Markdown excluding briefs; then resolve an exact heading in that destination. Neither needs a tag filter. |
| `cp-skill-connect:80,87–90` | `rg '^description:' …`; `rg -n "term" …` | Descriptions and focused body queries, both in destination Markdown. The source collection contract selects destinations, not the tag. |
| `cp-skill-write:73` | `rg -i "key term" kb/theory/ --glob "*.md"` | Duplicate guard in the **target** collection; theory is an example, not a default search universe. |
| `evaluate-log-entry-for-note-creation.md:32` | `rg '^description:' kb/theory/ --glob '*.md'` | Potential existing theory for a log proposal. Prose also requests terms and tags. Do not silently add source analyses to this result. |
| `find-next-straightforward-task.md:40` | `rg -ni '^#{1,6}[[:space:]]+.*open questions' kb/theory --glob '*.md'` | Open-question headings in theory, not topical membership. |
| `example-onboard-second-brain.md:68,85,109` | `rg` over descriptions and bodies; no fixed expression | Recall test, repeated discovery, and a proposed search routine across the consuming KB. Decide what the operator wants to recall before narrowing. |
| `evaluate-scenarios:50,114`; `invert-solution-shaped-requests.md:101` | Scoped `rg` listing; `rg` as a cheap local check | The first estimates retrieval cost for a scenario; the second leaves the lookup to the task. Neither defines membership. |

## Searches that should not inherit a topic filter

| Instruction : line | Command or named tool | Search boundary and purpose |
|---|---|---|
| `retire-artifact.md:39,49,116` | `rg -n '<artifact-slug>' …` piped to `rg -i` for ownership language; `rg -c …`; `rg -l …` | All searchable `kb/` Markdown: find delegated responsibilities, count references, verify remaining paths. Narrowing to the retired artifact’s collection could hide dependents. |
| `extract-adopted-part-of-a-proposal.md:32`; `re-ingest.md:107` | `rg -n '<proposal-slug>' …`; `rg -n "<ingest-filename>" …` | Both search Markdown across `kb/` for inbound uses. Restrictions on *editing* particular hits do not narrow discovery. |
| `change-a-contract-that-several-consumers-read.md:17`; `upgrade-the-theory-library-layout.md:50` | `rg --no-ignore --hidden` for byte changes; `rg -n --hidden 'commonplace:notes/\|<library>/notes/' .` | Whole checkout for affected consumers or obsolete paths; the first deliberately includes ignored state. |
| `extract-adopted-part-of-a-proposal.md:20,24` | `git log -S'<identifier>'`; `git log --grep='ADR 0NN'` | Search changes in tracked content or commit messages for the implementing decision. Not a working-tree text search. |
| `refresh-a-proposal-current-state.md:19`; `example-onboard-second-brain.md:123` | `ls kb/reference/adr/`; `git log --since=<anchor date> -- <paths>`; `git log --since` | List ADR candidates and inspect their dates; search history of named implementation paths, or recent KB edits for the example daily brief. |
| `cp-skill-snapshot-web:62–64,158,211` | Harness **Grep** | Exact `source:` URL in existing ignored Markdown snapshots; evidence in one extracted PDF text; article DOI metadata in one temporary HTML file. The interface prescribed is Grep, irrespective of its backend. Not searches of tracked source *topics*. |
| `fix-warnings/fix-descriptions.md:65` | `commonplace-validate notes 2>/dev/null` piped to `grep "description:"` | Filters diagnostic output, not notes. This and the maintenance count pipeline are literal shell `grep` uses. |
| `retire-artifact.md:103–105` | `commonplace-review status --json` piped to `python3 -c …` | Filter orphan result paths by the retired artifact’s exact directory prefix; operational state, not library membership. |
| `evaluate-scenarios:25`; `cp-skill-add-collection:44` | `ls tests/scenarios/*.md`; `ls "$(commonplace-source)"/_data/templates/user-*-COLLECTION.md` | Filename discovery in the test fixtures and the installed template directory respectively. |
| `upgrade-the-theory-library-layout.md:78–79` | `commonplace-status --collection kb/notes`; `commonplace-promotion-candidates kb/notes` | Collection-scoped operational inventory after migration, not text matching. |
| `kb/agentic-systems/instructions/refresh-agent-memory-review-taxonomy.md:40–65,149` | `uv run python` calling `load_results(…)` | Enumerate the selected analysis population with the existing loader; repeat against the same inputs. Do not substitute a topical candidate search. |

Executable discovery is another non-content case: `cp-skill-health-check:135–154` uses `command -v`, `which -a` and PowerShell `Get-Command`; `cp-skill-snapshot-web:117–119,173–174` uses `command -v` for capture prerequisites. These do not need collection decisions.

## Standing instructions and companion recipes

- `AGENTS.md:213` says “Use `rg` first,” not “only.” `AGENTS.md.template:119,136,139,142` recommends lexical search and gives three concrete `rg` queries: `^description:`, `^type: types/note.md`, and `^tags:.*my-tag`, all over Markdown in `kb/notes/ kb/reference/ kb/instructions/`. The last is explicitly candidate discovery in a scaffold example, not proof of exact membership.
- The [tag type’s exact-membership recipe](../../types/tag-readme.md#checking-exact-membership) uses `uv run python` with `collect_tag_space`, the same collector as the validator and site. The [generated-index type](../../types/generated-index.md) already distinguishes this from description search. No new query mechanism is needed to correct the maintenance instruction’s membership claim.
- Other scoped examples: `kb/types/ingest-report.md:70` uses `rg -l "^learning_claims: true" kb/sources/` for source candidates; `kb/reference/README.md:70` uses `rg` on ADR descriptions; `kb/reference/link-vocabulary.md:134` uses `rg "<artifact-name>" kb/theory/` for reverse provenance. These answer three different questions despite using the same tool.
- Not every search direction names a command. For example, `cp-skill-library:18` searches instruction descriptions; `cp-skill-ingest:119` searches tracked ingests for source identity; `cp-skill-write:77` asks for one backlinks lookup. Keep these separate from command counts. In particular, an ingest URL lookup is not a reason to search sources by topical tag.

## Use in the tag audit

Start with the three maintenance queries and connect’s complete-head shortcut. Check each against a participating member, a same-tag tracked source, a hyphenated neighboring tag, and an ignored or ineligible file. For an orphan query include an eligible *untagged* file. Record the expected paths **for that question** before comparing results. A source should be found by an explicit source-topic lookup without being counted as a member under the current contract. Broad dependency searches are controls: a tagging change should not narrow them.
