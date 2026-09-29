---
description: "Job of an analyse-agentic-system run: confirm the target is in scope, classify it, freeze its sources, and write boundary.md"
type: types/instruction.md
---

# Fix the boundary and freeze the sources

Write `boundary.md` in the run directory. It fixes what the run analyses and the evidence it may use; every later job works from it. The run's parameters and `opening.json` name the system and the caller's source input.

## Scope

Confirm the target is in scope: an agent runtime, orchestration framework, agent operating layer, memory/knowledge/context-engineering system, or a narrower mechanism whose operation depends on model calls it issues or serves. An MCP server, tool, or returning computation may qualify without owning the enclosing runtime. A target outside this boundary gets the disposition `out-of-scope`. If no coherent boundary or reachable source can be established, the disposition is `blocked`.

Classify an in-scope target with one `target-class` and one `boundary-kind` value from the [overview type](../../../types/agentic-system-analysis-overview.md)'s frontmatter table, and state functional inclusions, exclusions, and external dependencies. Do not assign responsibilities owned by an excluded host to the selected target.

## Freeze the sources

1. Before inspection, record a compact source allowlist: the exact repositories, captures, documents, and time boundary that may supply evidence. A supplied repository reference authorizes creating its missing ignored checkout and fetching the objects needed for the selected revision. It does not authorize changing an existing worktree, switching branches, merging, pulling, or resetting.
2. For GitHub, normalize the repository identity and use `related-systems/<owner>--<repo>/`. Require `git check-ignore -q related-systems` before creating it, verify an existing checkout's origin, and resolve the selected revision to a full commit.
3. Turn every non-Git source set into one immutable capture or bundle with a stable identity, version or capture label, absolute path, and SHA-256. Do not analyse a moving live page as though it were frozen.
4. Build one `SRC-*` register with the columns and evidence layers the overview type's Source register requires.

The source pin is an evidence boundary. If it changes or cannot be verified, write a problem report.

## Output

`boundary.md` has this frontmatter and these sections, and nothing else:

```markdown
---
result-disposition: complete        # or blocked, out-of-scope
target-class: "<value>"             # null when not classified
boundary-kind: whole-system         # null when not established
reviewed-boundary: "<full commit or capture identity>"   # null when not established
analysis-cutoff: "YYYY-MM-DD"       # null when not established
evidence-tier: code-grounded        # or doc-grounded; null when not established
source:                             # null when no source was frozen
  kind: git                         # or capture
  identity: https://github.com/owner/repository
  revision: "<full commit>"         # capture label for a capture
  path: /absolute/path/to/checkout  # absolute capture file for a capture
  sha256: null                      # the capture's digest for a capture
---

## Boundary and evidence

## Source register
```

The two sections are those the overview type requires; they go into the overview unchanged. A `blocked` or `out-of-scope` disposition adds a third section, `## Not reached`, saying what was not reached, why, and which conclusion that prevents.
