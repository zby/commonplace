---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Gnosis runtime baseline: repository-local CLI, doctrine delivery, retrieval, admission and maintenance at the frozen commit."
run-id: AAS-2026-10-15-gnosis-5bfb42422ce3-01
reviewed-boundary: "429528bf98e424b40837d2dbe3631d0fb42da6fd"
---

# Gnosis runtime report

## Runtime account

Gnosis supplies a local knowledge CLI and instructions for an external coding agent, not the agent's execution loop. Its consequential work is preserving non-reconstructable repository context and making it available before later implementation decisions. The shipped sequence is help → agent-chosen search → optional full-entry read → external work → write during work → review and maintenance. The next-step owner outside each CLI invocation is the caller, not a Gnosis scheduler. SRC-1: `README.md`, `AGENTS.md`, `cmd/gn/main.go`, `internal/doctrine/plan.txt`.

> At the start of any task, run `gn help plan` and follow its instructions.
> After finishing a task, run `gn help review`.
> --- `README.md`

This account inspects implementation and doctrine/design in SRC-1 at the reviewed commit. No target command, test or example was executed, and no observed-run or experimental source was supplied. Wiring below does not establish agent compliance, deployment reliability, retrieval quality or benefit. Added inspection beyond the boundary's initial coverage includes full `internal/commands/author.go`, `internal/commands/resolve.go`, `internal/storage/filelock.go`, `internal/storage/filelock_unix.go` and `internal/storage/filelock_windows.go`; these supply implementation evidence, not execution evidence.

### Ordinary invocation and control ownership

For an ordinary future coding task, the setup file directs the agent to request `gn help plan`. The dispatcher prints embedded planning doctrine plus the shared commands reference without constructing a store. No argument prints generic help; unknown commands/topics fail with stderr and exit 1. The natural-language guidance asks the agent to choose plan keywords and run an OR query before implementing, inspect conflicts and surface them to the user. The CLI does not block code edits until this happens. [RT-RTE-doctrine-delivery](#rt-rte-doctrine-delivery) and [RT-BAP-agent-guidance](#rt-bap-agent-guidance) identify that instruction channel. SRC-1: `cmd/gn/main.go`, `internal/doctrine/doctrine.go`, `internal/doctrine/plan.txt`.

For `gn search 'billing OR reconciliation'`, the process creates a Store once, resolving its root by walking upward for `.git`, `.jj` or `.gnosis`, falling back to the current directory if none exists. The retained file is `<root>/.gnosis/entries.jsonl`; cache and lock are under `$XDG_CACHE_HOME/gnosis/<first-16-hex-sha256(root)>`, falling back to `~/.cache`. Thus repository scope is a discovery convention, not an authorization boundary. `Search` accepts a positive limit (default 20), joins non-flag arguments, sanitizes query terms, opens SQLite, refreshes by JSONL modification time and performs FTS5 matching ordered by rank. The result is an ID/date/primary-topic/short-snippet listing, not all retained evidence. A caller can then use `gn show <id>` for complete entry text or `gn show <topic>` for all matching entries. [RT-RTE-knowledge-read](#rt-rte-knowledge-read) retains the selection and omission details. SRC-1: `internal/storage/storage.go`, `internal/paths/paths.go`, `internal/commands/search.go`, `internal/index/index.go`, `internal/commands/show.go`.

> WHERE entries_fts MATCH ?
> ORDER BY rank
> LIMIT ?
> --- `internal/index/index.go`

The external agent decides whether results alter its plan. Gnosis provides no answer oracle for that judgment. During work, doctrine asks it to record decisions promptly; `gn write` validates syntax, topics and related IDs, resolves an attribution string, obtains an exclusive lock, generates a unique ID against the locked snapshot and appends JSONL. It rereads entries and prints the new ID. This is admission of caller-supplied text, not software verification that the text is true, originated with a human, or belongs in the KB. [RT-RTE-entry-admission](#rt-rte-entry-admission) separates those roles. SRC-1: `internal/commands/write.go`, `internal/storage/storage.go`, `internal/commands/author.go`.

> If a decision is made or an alternative is explicitly rejected,
> record it immediately with "gn write" rather than waiting for
> the end of the session. Context may be lost before you get to the
> review step.
> --- `internal/doctrine/plan.txt`

After external work, review doctrine asks the agent to select unreconstructable knowledge and tidy superseded entries. `gn edit` and `gn rm` perform explicit maintenance; new text with `--related` is another ordinary write, not a machine-interpreted supersession event. Persistence survives sessions in JSONL; sharing depends on callers committing and distributing `.gnosis`, not on a CLI synchronization service. [RT-RTE-entry-maintenance](#rt-rte-entry-maintenance). SRC-1: `internal/doctrine/review.txt`, `internal/commands/edit.go`, `internal/commands/rm.go`, `internal/commands/write.go`.

### Forcing routes and qualified guarantees

Three source-inspected forcing cases challenge stronger readings of the ordinary loop:

1. **Direct mutation without review.** A shell caller can invoke write, non-interactive edit or removal directly. Positional edit text wins over piped input; neither needs an editor or per-entry human approval. Interactive edit instead invokes `$EDITOR` (default `vi`) with a temporary buffer. Both save paths use Store.Update, but only interactive editing revalidates changed topics and related IDs against the locked snapshot. Author metadata can be supplied with `--author`, falls back to Git configuration and finally a literal unknown identity; it is not authentication. This falsifies any claim that semantic filtering or human authorship is an executable admission invariant. SRC-1: `cmd/gn/main.go`, `internal/commands/write.go`, `internal/commands/edit.go`, `internal/commands/author.go`.

2. **Concurrent edits versus concurrent appends.** Production write uses AppendNew's exclusive lock across ID generation and append; edit/removal use Update across read-modify-rewrite. This preserves concurrently appended records when maintenance reacquires the latest snapshot. An editor buffer, however, was read before that lock: another edit to the same entry can be overwritten, with no version comparison. Write's related-prefix validation also precedes its append lock, so removal can invalidate a related target before the new entry is appended. The library's plain Append takes only a shared lock and assumes a preassigned unique ID; Rewrite accepts a caller-supplied whole snapshot. Neither is selected by the production command dispatch, and neither inherits the full AppendNew/Update guarantee. Direct JSONL edits or Git merges do not cooperate with these locks. SRC-1: `internal/storage/storage.go`, `internal/commands/write.go`, `internal/commands/edit.go`, `internal/commands/rm.go`.

3. **Cache freshness is not semantic freshness.** Search compares a stored mtime string with the current JSONL mtime. Rebuild takes a shared lock around entry read plus mtime capture, then transactionally replaces index rows and metadata. This pairs the snapshot with its timestamp against exclusive production writers; it does not make all subsequent search/render operations one snapshot. Show/latest/topics read JSONL without this index path. If the JSONL file disappears, EnsureFresh returns success without clearing old index rows, so a pre-existing cache can still yield old snippets; if contents change while mtime stays equal, automatic refresh will not detect that change. Explicit `gn reindex` forces rebuild, but a database that fails to open/schema initialization is returned as an error before rebuild, not universally repaired. SRC-1: `internal/index/index.go`, `internal/commands/search.go`, `internal/commands/reindex.go`, `internal/commands/show.go`, `internal/commands/latest.go`, `internal/commands/topics.go`.

> if storedMtime == currentMtime {
> return nil
> }
> --- `internal/index/index.go`

The load-bearing guarantees are therefore scoped as follows. Each operation status is uninspected because these are source traces, not executions.

| Guarantee | Owner and enforcement point | Strength and coverage | External contract and excluded alternate paths | Statuses |
|---|---|---|---|---|
| Collision-free new IDs against the locked store | Store.AppendNew; exclusive lock encloses reread, generation and append | protocol; production `gn write` using a common lock | OS lock semantics, same root/cache/lock identity, cooperative writers; plain Append and direct edits excluded | implementation conclusion status: wired; operation conclusion status: uninspected |
| Preservation of unrelated concurrent additions during maintenance | Store.Update rereads under exclusive lock, writes temporary file then renames | protocol; command edit/rm | Shared lock convention and filesystem rename semantics; stale same-entry edit contents and external writers excluded; no fsync-based crash-durability claim | implementation conclusion status: wired; operation conclusion status: uninspected |
| Rebuilt index rows and metadata commit together | Index.Rebuild SQL transaction | protocol; successful rebuild after open/schema initialization | SQLite transaction contract; not a guarantee of uninterrupted newest-data search or semantic truth | implementation conclusion status: wired; operation conclusion status: uninspected |
| Record only useful non-reconstructable context; surface conflicting decisions | External agent interpreting embedded plan/review | policy; instructed caller workflow only | Caller reads and complies; direct CLI/manual file mutation and arbitrary external task paths are not gated | instruction conclusion status: wired; compliance conclusion status: uninspected |

SRC-1: `internal/storage/storage.go`, `internal/storage/filelock.go`, `internal/storage/filelock_unix.go`, `internal/storage/filelock_windows.go`, `internal/index/index.go`, `internal/doctrine/plan.txt`, `internal/doctrine/review.txt`. The locking helpers use Unix flock or Windows LockFileEx on the cache lock, not access control on the knowledge file.

> // fileLock wraps the open file descriptor the store uses as an advisory lock.
> --- `internal/storage/filelock.go`

### Capability and deployment limits

The inspected shipped entry point dispatches local commands, not model calls or delegated agents. No distributed-parametric component is used inside the inspected Gnosis route: FTS5 ranking is symbolic query/index processing, not an embedding endpoint. The external agent's exact model version, weight mutability, provider routing and context compaction are uninspected and outside this boundary; the report declares no internal model component for that host. SRC-1: `cmd/gn/main.go`, `internal/index/index.go`.

The capability surface includes local reads, appends, rewrites, deletion, SQLite cache writes, Git-config subprocesses and arbitrary editor-program execution selected by the environment. The current host grant set and deployed isolation envelope were not supplied. No CLI-local role/approval policy should be inferred from an author string or repository-root discovery. External shell authorization is responsible for whether the agent can invoke these operations at all. Editor execution is not a Gnosis model tool loop or extension-registration system. SRC-1: `internal/commands/author.go`, `internal/commands/edit.go`, `internal/storage/storage.go`, `cmd/gn/main.go`.

Working-context control within the target is selective delivery: query/limit/snippet, explicit full-entry reload, recent-entry listing and topic browsing. The caller chooses what tool output to receive; Gnosis neither isolates agent frames nor trims or summarizes an existing model window. The index returns 12-token snippets from the best matching column (possibly topics), latest caps body snippets at 200 runes, and show returns the full body. Full JSONL remains reachable after either abbreviated listing. These limits select output, not a proof that the model saw or acted on the whole entry. SRC-1: `internal/index/index.go`, `internal/commands/latest.go`, `internal/commands/show.go`.

Recovery consists of surfaced errors, retry by the external caller, explicit cache rebuild, and further edit/removal or caller-managed Git restoration of retained content. CLI errors ordinarily print diagnostics and exit 1; a post-write reread can fail after the append already succeeded, so a failed invocation is not necessarily a rolled-back write. No supplied run establishes error rates, lock contention or performance. SRC-1: `cmd/gn/main.go`, `internal/commands/write.go`, `internal/commands/reindex.go`, `internal/storage/storage.go`.

## Shared records

### Components

none declared in this member

### Operative objects

#### RT-OBJ-doctrine
Label: Embedded doctrine

Identity: `internal/doctrine` Help, Plan, Review and Commands strings, embedded into the Go binary from text files. Representational form: natural-language workflow and semantic selection guidance, with command examples; Go embed and dispatch are symbolic delivery machinery. Storage substrate: versioned text files, compiled binary, stdout at invocation. Plan and Review tell agents when and what to read/write; the actual knowledge entries and derived index are distinct retained objects left to the memory account. SRC-1: `internal/doctrine/doctrine.go`, `internal/doctrine/plan.txt`, `internal/doctrine/review.txt`, `cmd/gn/main.go`.

> //go:embed plan.txt
> var Plan string
> --- `internal/doctrine/doctrine.go`

### Routes

#### RT-RTE-doctrine-delivery
Label: Doctrine delivery

Endpoints/progression: caller shell → CLI help dispatch → embedded text and shared command list → caller stdout. Owner: Go dispatcher for delivery, external agent for interpretation and the next action. Context is requested help topic, not a captured session. No knowledge store is created by this path. SRC-1: `cmd/gn/main.go`, `internal/doctrine/doctrine.go`; operative text is [RT-OBJ-doctrine](#rt-obj-doctrine).

- Immediate return: Help body followed by commands reference; unknown topic returns a diagnostic and exit 1.
- Later read-back: inapplicable — static embedded doctrine is not content accumulated through this invocation.
- Delegated visibility: inapplicable — no Gnosis worker or delegation is launched; host handling of stdout is external.
- Selection predicate: No arguments/default help, `help plan`, or `help review` determines the body.
- Invalidation or expiry: Binary embeds its build's text; changes require rebuilding/replacing the binary, not editing retained entries.
- Activation or effect: Printing is implemented; caller compliance is unobserved.
- Evidence limits: Source delivery establishes the request for behavior, not reliable obedience.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> fmt.Print(body)
> fmt.Println()
> fmt.Print(doctrine.Commands)
> --- `cmd/gn/main.go`

#### RT-RTE-knowledge-read
Label: Requested knowledge read

Endpoints/progression: caller → search/latest/topics/show → JSONL and, for search, derived FTS5 index → formatted stdout. Caller supplies the query/target and chooses whether to request fuller content or alter its task. Code determines lexical matching, rank, limits and output transformation; it does not choose a new task step. State effects are cache/lock creation and index refresh, not retained knowledge revision. SRC-1: `internal/commands/search.go`, `internal/index/index.go`, `internal/commands/show.go`, `internal/commands/latest.go`, `internal/commands/topics.go`.

- Immediate return: Search emits up to 20 default ranked snippet rows; latest emits up to 20 newest-by-CreatedAt rows with ID tie-break and 200-rune snippets; topics emits counts; show emits full entry details or topic-matching entries in creation order. Empty searches/lists can return no text successfully.
- Later read-back: Retained JSONL entry text and metadata reach later explicit search/show/latest invocations; search indexes only ID, text and joined topics, not author/related/time fields. FTS can choose a topic snippet; full body requires show.
- Delegated visibility: inapplicable — no internal delegation; stdout sharing into another agent is controlled by the external host.
- Selection predicate: Sanitized FTS5 expression ordered by BM25 rank and positive limit; latest by creation time; topics by aggregate count; show target length at most six runes selects unique ID prefix, otherwise normalized topic equality.
- Invalidation or expiry: No automatic semantic expiry; index freshness compares mtime, explicit reindex forces rebuild. JSONL removal or unchanged mtime can evade automatic cache replacement as described above.
- Activation or effect: Symbolic code returns selected text; decision influence occurs only if the external caller interprets and uses it, which is unobserved.
- Evidence limits: No recall/precision or downstream-plan evidence; independent JSONL/index reads do not establish a single transactional search/render snapshot.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> snippet(entries_fts, -1, ?, ?, '…', 12),
> --- `internal/index/index.go`

#### RT-RTE-entry-admission
Label: Entry admission

Endpoints/progression: caller-supplied topics/text/related/author → Write parsing and validation → Store.AppendNew → JSONL → printed ID and later retrieval. Trigger: a caller command, doctrinally an unreconstructable decision or observation during work. Guidance: [RT-OBJ-doctrine](#rt-obj-doctrine) filters reproducible/code-anchored information out and requests context sufficient for later readers. The caller proposes and makes the semantic admission decision; human versus computational authorship of any particular entry is unresolved. Software can reject malformed command arguments, empty text, short/empty topics, unresolved or ambiguous related IDs and I/O failure, not bad reasoning. No answer oracle is consulted. Operating mode is open caller-directed work, not a curriculum or bounded experiment. SRC-1: `internal/commands/write.go`, `internal/commands/topics.go`, `internal/commands/resolve.go`, `internal/storage/storage.go`, `internal/doctrine/review.txt`.

- Immediate return: Newly assigned six-letter ID rendered with unique-prefix highlighting; diagnostics on failure, unknown-author warning does not block admission.
- Later read-back: JSONL text, topics, related full IDs, author and timestamps persist for later CLI consumers; only text/topics feed lexical search matching.
- Delegated visibility: inapplicable — caller performs admission; no internal reviewer agent exists on this route.
- Selection predicate: Explicit submitted content; structural validation, not software assessment of relevance, truth or empirical origin.
- Invalidation or expiry: Explicit edits/removals or a new related entry; no TTL or automatic contradiction resolver.
- Activation or effect: Appends a retained entry under exclusive lock; subsequent behavioral use remains unobserved.
- Evidence limits: Related resolution is outside the append lock; author is attribution not authentication; no supplied trace establishes any per-content human approval or improvement.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Rejection/rollback: caller can withhold the command, software can reject the listed malformed inputs, and subsequent edit/removal or external Git restoration can undo content. Append is not a semantic transaction spanning later ID rendering; no automatic rollback follows a post-append read failure. The proposed change retained here is knowledge text, not code, capabilities or model parameters. Product changes remain ordinary external source edits/builds; this CLI does not admit them. SRC-1: `internal/commands/write.go`, `internal/storage/storage.go`, `internal/doctrine/review.txt`.

> if authorArg = strings.TrimSpace(authorArg); authorArg != "" {
> return authorArg, true
> }
> --- `internal/commands/author.go`

> return "Unknown <unknown@gnosis>", false
> --- `internal/commands/author.go`

#### RT-RTE-entry-maintenance
Label: Entry maintenance

Endpoints/progression: caller review/explicit intent → edit or rm → locked Store.Update → replacement JSONL; alternatively caller invokes reindex → index rebuild without revising retained entry meaning. Trigger and proposed change come from the caller; doctrine recommends correcting stale knowledge by removal or a new related entry. Caller proposes, decides and may withhold; structural validation and storage errors can reject. Interactive editor use does not establish a human operator in every invocation; non-interactive edit/removal require no approval prompt. No answer oracle is used. Operating mode is explicit open-ended maintenance, not an automatic trace-fed improvement job. SRC-1: `internal/doctrine/review.txt`, `internal/commands/edit.go`, `internal/commands/rm.go`, `internal/commands/reindex.go`, `internal/storage/storage.go`.

- Immediate return: Edit returns success (or `no changes`), rm prints removed IDs and warnings for surviving dangling references, reindex prints count and cache location; errors return to dispatcher.
- Later read-back: Edited/surviving entries are loaded on subsequent direct reads and later index rebuilds; removed entries no longer exist in JSONL. A related replacement preserves both records unless separately removed.
- Delegated visibility: Interactive editing sends one buffer with topics/related/body to an environment-selected editor subprocess inheriting stdio. Non-interactive edit supplies body only; no separate agent result is returned.
- Selection predicate: Unique ID prefixes select edit/removal targets; interactive changes include metadata, positional/piped edits replace only body. Reindex selects the full JSONL corpus.
- Invalidation or expiry: Explicit caller action; rm warns about references but does not rewrite those references automatically. Cache replacement follows mtime or forced rebuild.
- Activation or effect: Retained content is rewritten under lock using temp-file rename; edited UpdatedAt changes, while semantic supersession remains a prose convention.
- Evidence limits: Latest locked snapshot preserves other records but does not veto stale-buffer overwrite of the same record. No observed review decisions, later reliance or maintenance efficacy supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Rollback/recovery: failures before successful rename leave the original file rather than a partially rewritten final file; failed temporary writes/renames remove the temporary path. No built-in version history restores an overwritten entry. Caller-managed version control or another edit/removal is needed. Reindex cannot fix malformed JSONL and is not a universal corrupt-database repair if opening fails. SRC-1: `internal/storage/storage.go`, `internal/commands/reindex.go`, `internal/index/index.go`.

> // Warn about dangling Related references in surviving entries. We do
> // not modify those entries automatically because silent data mutation
> // would be surprising and hard to audit.
> --- `internal/commands/rm.go`

### Claims

#### RT-CLM-agent-compliance
Label: Agent compliance claim

Claimed operation: README says agents follow the instruction every time; this is an author claim, not an execution observation or enforced CLI contract. Direct admission routes and unguarded external task execution prevent treating the wording as an implementation invariant. The actual guidance delivery is [RT-RTE-doctrine-delivery](#rt-rte-doctrine-delivery). SRC-1: `README.md`, `cmd/gn/main.go`.

> Nobody keeps a decision log going, but an agent follows the instruction every single time, and it has the context fresh in its window at the moment the decision is made, which is the only moment anyone ever has the energy to write it down.
> --- `README.md`

- claim conclusion status: claimed
- compliance conclusion status: uninspected

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-agent-guidance
Label: Agent guidance channel

Consumer: external coding agent (or human reader). Channel: startup instructions in README/repository AGENTS direct explicit CLI help/search calls; embedded doctrine and returned retained entry text arrive as natural-language stdout. Force: advisory interpretation, with a request to surface conflicts to the user; not a Gnosis-enforced veto on code changes. Horizon: doctrine across uses of the installed binary; retained entry guidance potentially across problems/sessions through explicit read-back. No supplied trace closes delivery → changed decision or benefit. Structural validity at the update consumer does not establish semantic authority at the downstream agent. SRC-1: `README.md`, `AGENTS.md`, `internal/doctrine/plan.txt`, `internal/doctrine/review.txt`, `internal/commands/show.go`.

> Read what comes back. If any recorded decision conflicts with your
> plan, surface it to the user before proceeding.
> --- `internal/doctrine/plan.txt`

## Annotations

none
