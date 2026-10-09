---
description: "Use for the boundary hand-out to classify one target and establish its frozen evidence"
type: types/instruction.md
---

# Fix the boundary from the engine inputs

Write the boundary that fixes this run's target, disposition and frozen evidence for every later job.

`blocked` and `out-of-scope` are valid dispositions, not failures. Use
`problem` only when you cannot write the boundary under these inputs: a
missing required input, a changed source pin, a needed identity change or
prior-analysis exposure. Use the opening's normalized `source-identity`
unchanged; do not derive it from caller text.

## Select the target

Confirm that the target is an agent runtime, orchestration framework, agent
operating layer, memory/knowledge/context-engineering system, or a narrower
mechanism whose operation depends on model calls it issues or serves. An MCP
server, tool or returning computation may qualify without owning the enclosing
runtime. A target outside this scope gets `out-of-scope`. If no coherent
boundary or reachable source can be established, use `blocked`.

Classify an in-scope target with a `target-class` and `boundary-kind` from the
boundary contract. State functional inclusions, exclusions and external
dependencies. Do not assign an excluded host's responsibilities to this target.

Inspect the repository tree and trace shipped entry points and their consumers
before classifying it. A caller in the same repository is not an excluded
application merely because it calls a library API; a shipped driver is not
external merely because it supplies state to an API. Decide membership from
shipped usage and responsibilities. For `whole-system`, include the boundary
contract's top-level coverage table. For a memory or knowledge system, trace
shipped prompts, maintenance instructions, persistence and reload callers,
later consumers and evaluators; include them or justify each exclusion and
its prevented conclusion. An intentional library-only target gets a narrower
boundary kind. Do not call an available, uninspected file an access gap.

## Establish frozen evidence

1. Record the repositories, commits, captures, documents and time boundary
   that may supply evidence. For Git, the registered unit is the repository
   at the commit; initially inspected paths are coverage, not an allowlist.
2. When `acquire` contains a Git object, code has already frozen that checkout.
   Inspect its `path` read-only. Do not clone, fetch, pull, check out, reset,
   clean or copy it elsewhere. Copy the whole object unchanged into boundary
   frontmatter `source` and its `revision` into `reviewed-boundary`, even for
   `blocked` or `out-of-scope`. Another source or revision requires `problem`.
3. When `acquire` is JSON `null`, freeze any non-Git source set as an immutable
   capture or bundle in the opening's `capture-directory`, with a stable
   identity, capture label, absolute path and exact-byte SHA-256. Set frontmatter
   `source.kind` to `capture` and `reviewed-boundary` to the capture label. Create that
   directory when needed; it survives hand-out cleanup. Do not modify existing
   captures or analyse a moving live page as frozen. On repair, preserve a
   previous boundary's established capture; if its pin cannot be verified,
   write `problem`, not a replacement source. `source.identity` must equal
   the opening identity. If no source was
   established, use frontmatter `source: null` and a non-complete disposition.
4. Build the `SRC-*` register under the boundary and source contracts. A frozen
   source must have a register row. Keep one row per source identity, labelling
   the layers' inspected scope, anchors and limits within it. Register paths
   describe initial coverage, not a restriction on later reading at the commit.

The boundary type gives its sections, including `## Not reached` for a
non-complete disposition.
