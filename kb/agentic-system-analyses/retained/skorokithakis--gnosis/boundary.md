---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Gnosis's repository-local agent knowledge CLI and shipped doctrine at commit 429528bf98e424b40837d2dbe3631d0fb42da6fd."
run-id: AAS-2026-10-15-gnosis-5bfb42422ce3-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "429528bf98e424b40837d2dbe3631d0fb42da6fd"
analysis-cutoff: "2026-10-15"
evidence-tier: code-grounded
source:
  identity: https://github.com/skorokithakis/gnosis
  kind: git
  path: /media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-15-gnosis/related-systems/skorokithakis--gnosis
  revision: "429528bf98e424b40837d2dbe3631d0fb42da6fd"
  sha256: null
---

# Gnosis boundary

## Boundary and evidence

Gnosis is in scope as a memory/knowledge/context-engineering system. Its intended use is to retain repository-specific decisions, rejected alternatives, constraints and intent for coding agents across sessions. The target is the complete shipped `gn` CLI plus its embedded planning and review doctrine, repository setup instructions, and retained example knowledge. It is not an enclosing agent runtime. SRC-1: `README.md`, `docs/PRODUCT_STRATEGY.md`, `cmd/gn/main.go`, `internal/doctrine/doctrine.go`.

> gnosis is agent memory infrastructure. It gives AI coding agents a way to accumulate knowledge across sessions so that each session builds on the last instead of starting from zero. Agents are the primary writers and readers; humans read entries when they need to but are not expected to maintain the knowledge base.
> --- `docs/PRODUCT_STRATEGY.md`

The boundary is whole-system with respect to that shipped knowledge system, not the external agent's complete task loop. The CLI dispatches help, write, search, latest, show, topics, edit, removal and reindexing. Write validates and persists entries; storage reloads JSONL; search refreshes a disposable SQLite index and returns snippets; show and browsing commands expose retained content; edit and removal maintain it. Embedded doctrine supplies the semantic admission and supersession policy that executable validation alone does not supply. These are all included, rather than treating command functions as a standalone library. SRC-1: `cmd/gn/main.go`, `internal/commands/write.go`, `internal/storage/storage.go`, `internal/index/index.go`, `internal/commands/search.go`, `internal/commands/show.go`, `internal/commands/latest.go`, `internal/commands/topics.go`, `internal/commands/edit.go`, `internal/commands/rm.go`, `internal/commands/reindex.go`, `internal/doctrine/plan.txt`, `internal/doctrine/review.txt`.

> 2. During work:
>    If a decision is made or an alternative is explicitly rejected,
>    record it immediately with "gn write" rather than waiting for
>    the end of the session. Context may be lost before you get to the
>    review step.
> --- `internal/doctrine/plan.txt`

> Stale knowledge is worse than no knowledge. If during your review you
> notice an existing entry that's been superseded by work in this
> session, either remove it ("gn rm") or write a new entry that
> references it ("gn write ... --related <old-id>") explaining what
> changed. Don't leave contradictions in the system.
> --- `internal/doctrine/review.txt`

The shipped consumption path is explicit: setup instructions tell an external agent to read help; planning doctrine tells it to search before implementation, read results and surface conflicts. The repository's own `AGENTS.md` repeats the search/write/review workflow. Those callers and prompts belong to the target. The external agent's model, session context, shell authorization and decision to comply do not. No execution trace is supplied to establish compliance or an improvement in later task outcomes. SRC-1: `README.md`, `AGENTS.md`, `internal/doctrine/plan.txt`.

>    Read what comes back. If any recorded decision conflicts with your
>    plan, surface it to the user before proceeding. The recorded
>    decision may still hold, may be stale, or may need explicit
>    supersession — but don't silently contradict it. See "gn help
>    review" for how to supersede an entry.
> --- `internal/doctrine/plan.txt`

External dependencies are the agent and its shell, local filesystem and operating-system locking, Git configuration for default author attribution, an editor for interactive edits, and Go dependencies including the SQLite implementation. Version-control sharing is instructed, not implemented as a synchronization service by `gn`. Dependency implementations and remote provider behavior are outside the frozen repository; this prevents conclusions about their internals or end-to-end deployment reliability. SRC-1: `README.md`, `go.mod`, `internal/storage/storage.go`, `internal/commands/author.go`, `internal/commands/edit.go`, `internal/doctrine/review.txt`.

The frozen evidence is SRC-1 at full commit `429528bf98e424b40837d2dbe3631d0fb42da6fd`, verified against the acquired checkout's HEAD with no tracked worktree changes reported. The applicability cutoff is 2026-10-15, the supplied run date; it is not a claim about repository changes after this commit. Overall evidence is code-grounded. Documentation supplies declared intent, retained entries supply attributed decisions, and test source supplies inspectable assertions—not observed test results. No target code, tests or examples were executed.

### Top-level tracked coverage

Every top-level tracked item from the frozen Git tree is classified below. Included directories identify the material loop paths. “Not yet inspected” denotes available source, not an access gap; it does not silently exclude shipped runtime responsibilities.

| Top-level item | Classification and inspected scope | Role and limitation |
|---|---|---|
| `.github/` | Included: inspected `.github/workflows/test.yml`; release workflow deliberately excluded from functional analysis | The test workflow invokes `go test ./...`. Release delivery is not the knowledge loop; no claim about release reliability or successful CI runs. |
| `.gitignore` | Excluded, deliberate; contents not inspected | Repository hygiene; no claim about ignore-rule correctness. Actual cache location is grounded in `internal/paths/paths.go`. |
| `.gnosis/` | Included: `.gnosis/entries.jsonl` inspected | Shipped retained knowledge and attributed design decisions; not a session trace or proof that later agents used entries. |
| `.goreleaser.yaml` | Excluded, deliberate; contents not inspected | Distribution configuration; prevents conclusions about platform artifact correctness. |
| `.release-please-manifest.json` | Excluded, deliberate; contents not inspected | Release bookkeeping; prevents conclusions about released version correspondence. |
| `.tickets/` | Excluded, deliberate; file inventory only | Development task records, not dispatched runtime or embedded doctrine; no inference about task history or completion from ticket contents. |
| `AGENTS.md` | Included, inspected | Repository-local agent caller instructions: search before implementation, record during work, review after completion. These are evidence, not instructions for this analysis worker. |
| `CHANGELOG.md` | Excluded, deliberate; contents not inspected | Historical release narrative; no historical evolution or version-by-version claims. |
| `LICENSE` | Excluded, deliberate; contents not inspected | Legal artifact; no licensing assessment. |
| `Makefile` | Excluded, deliberate; contents not inspected | Build/test/install convenience wrapper; no wrapper behavior claim. The shipped CLI entry and CI test command are independently inspected. |
| `README.md` | Included, inspected | Intended use, adoption instructions, CLI surfaces and declared limits. No user compliance demonstrated. |
| `cmd/` | Included: `cmd/gn/main.go` inspected in full | Sole shipped CLI entry: doctrine/help dispatch and all stateful subcommands. |
| `docs/` | Included: `docs/PRODUCT_STRATEGY.md` inspected | Design intent and knowledge-selection policy; not independent efficacy evidence. |
| `go.mod` | Included, inspected | Module and dependency declarations; external implementations not inspected. |
| `go.sum` | Included as dependency-pin context; contents not yet inspected | Available lock data; no dependency-integrity audit or transitive implementation assessment. |
| `internal/` | Included: full `storage/storage.go`, `index/index.go`, `paths/paths.go`; full command bodies in `write.go`, `search.go`, `show.go`, `latest.go`, `topics.go`, `edit.go`, `rm.go`, `reindex.go`; all `doctrine/` files inspected. `author.go`, `resolve.go`, locking shims and remaining support/test files inventoried and searched; selected index and reindex tests inspected | Persistence, admission, retrieval, reload, maintenance and prompt-driven later consumption are covered. `termcolor/` and `textwrap/` provide presentation support. Not every helper or test assertion was read; no exhaustive concurrency, portability, rendering or test-adequacy claim. Available helper/test bodies remain evidence for later source inspection. |
| `release-please-config.json` | Excluded, deliberate; contents not inspected | Release automation configuration; no release-process correctness claim. |

The evaluator evidence initially inspected is unit-test source for freshness/rebuild and persistence-to-search, plus the CI test invocation. It establishes what the tests assert, not their passage, agent recall quality, or downstream decision quality. SRC-1: `internal/index/index_test.go`, `internal/commands/reindex_test.go`, `.github/workflows/test.yml`. No required material source path was unavailable; the access limit is absence of supplied run/experiment evidence and external host/dependency internals, not failure to inspect an available file.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/skorokithakis/gnosis` | 429528bf98e424b40837d2dbe3631d0fb42da6fd | implementation; doctrine/design; reported operation | Access root: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-15-gnosis/related-systems/skorokithakis--gnosis`. Implementation: `cmd/gn/main.go`; `internal/commands/` write, search, show, latest, topics, edit, rm and reindex; `internal/storage/storage.go`; `internal/index/index.go`; `internal/paths/paths.go`; selected test ranges in `internal/index/index_test.go` and `internal/commands/reindex_test.go`; `.github/workflows/test.yml`. Doctrine/design: `README.md`, `AGENTS.md`, `docs/PRODUCT_STRATEGY.md`, all `internal/doctrine/` files, dependency declarations in `go.mod`. Reported operation/design history: `.gnosis/entries.jsonl` and README self-use claims. Whole tracked tree inventoried and helper/test declarations searched; coverage distinctions above apply. | Implementation: [CLI](https://github.com/skorokithakis/gnosis/blob/429528bf98e424b40837d2dbe3631d0fb42da6fd/cmd/gn/main.go), [storage](https://github.com/skorokithakis/gnosis/blob/429528bf98e424b40837d2dbe3631d0fb42da6fd/internal/storage/storage.go), [index](https://github.com/skorokithakis/gnosis/blob/429528bf98e424b40837d2dbe3631d0fb42da6fd/internal/index/index.go). Doctrine/design: [planning](https://github.com/skorokithakis/gnosis/blob/429528bf98e424b40837d2dbe3631d0fb42da6fd/internal/doctrine/plan.txt), [review](https://github.com/skorokithakis/gnosis/blob/429528bf98e424b40837d2dbe3631d0fb42da6fd/internal/doctrine/review.txt), [setup](https://github.com/skorokithakis/gnosis/blob/429528bf98e424b40837d2dbe3631d0fb42da6fd/README.md). Reported operation: [retained entries](https://github.com/skorokithakis/gnosis/blob/429528bf98e424b40837d2dbe3631d0fb42da6fd/.gnosis/entries.jsonl). | No repository access gap identified. No supplied execution trace, observed test run or causal experiment: prevents asserting actual agent compliance, empirical retrieval quality, demonstrated reliability or causal task improvement. External agent/runtime and dependency internals are not captured; their responsibilities cannot be attributed to Gnosis. |
