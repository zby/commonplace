---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "deja-vu workflow: extract recurring corrections, obtain user selection and distribute standing rules at the frozen Git boundary."
run-id: AAS-2026-10-14-deja-vu-22137d4d39a5-01
reviewed-boundary: "4c08fb26ad8a8b8e656a120f06ca4175a7078148"
---

# deja-vu workflow report

## Workflow account

### Selected workflow and evidence boundary

The representative workflow is a user's request to find standing preferences in prior corrections, followed by rule proposal, user selection, source-file editing and distribution to installed agents. It was selected because the shipped skill explicitly joins these stages and defines a consequential stop before writing. This is not a reconstruction from unrelated capabilities. The existing [RT-RTE-rules-sync](runtime.md#rt-rte-rules-sync) covers the route; [RT-OBJ-rules](runtime.md#rt-obj-rules) identifies its retained output and [RT-BAP-standing-rules](runtime.md#rt-bap-standing-rules) identifies the intended later consumer.

The evidence is SRC-1 at the boundary's frozen commit. Executable Go establishes extraction and file-distribution wiring; `skills/deja-search/SKILL.md` establishes the requested model/user procedure. No supplied trace establishes an actual proposal, approval, sync or later compliance. The enclosing host's inference, shell execution permissions and instruction loading remain external, as described in [boundary](boundary.md#boundary-and-evidence).

### Request and extraction handoff

The user asks their foreground agent to find or suggest standing rules. The skill directs that agent to invoke `deja rules candidates`, optionally narrowing to recent history. The agent delegates extraction to the binary, not semantic synthesis or user approval. The command ensures the index and walks indexed user, assistant, command and edit records. It accepts a corrective user turn only after an earlier user turn and an intervening agent-side record. Matching uses correction patterns near the start of the turn, rejects long turns and pseudo-user blocks, and excludes subagent, temporary/test and ignored sessions. These are extraction heuristics, not proof that a correction is a standing preference (SRC-1, `cmd/deja/rules_candidates.go`).

The handoff back to the agent is a numbered list or JSON array. It supplies correction text, preceding agent/command/edit context, harness, date and session provenance; JSON additionally carries full session ID and project. The agent does not receive an unabridged transcript in this operation. Correction text is whitespace-folded and clipped to 300 runes; prior context to 150. Terminal-safe text transformation occurs before delivery. The retained index supplying these candidates is [RT-OBJ-index-db](runtime.md#rt-obj-index-db), not a new workflow-owned store.

> Correction:  search.SafeLine(squeezeTrim(x, candidateQuote)),
> AgentBefore: search.SafeLine(squeezeTrim(st.lastAgent, candidateBefore)),
> --- `cmd/deja/rules_candidates.go`

Candidates are sorted chronologically, deduplicated, optionally limited to the newest, then numbered. Deduplication keys on the lowercased first 200 runes of the already clipped correction, independently of session identity. Thus the list is not a complete occurrence count: identical corrections in distinct sessions can collapse alongside fork copies. The model's requested recurrence assessment depends on this reduced evidence and cannot treat missing duplicates as evidence that the preference occurred only once (SRC-1, `cmd/deja/rules_candidates.go`).

> k := strings.ToLower(firstRunes(c.Correction, candidateDedupRunes))
> if seen[k] {
> 	continue
> }
> seen[k] = true
> --- `cmd/deja/rules_candidates.go`

An invalid option, index failure or record-reading failure returns an error rather than a rule proposal. Empty text-mode results describe the searched time window or indexed-session count and can mention excluded test runs. An empty candidate list is not an absence claim about all user preferences (SRC-1, `cmd/deja/rules_candidates.go`).

### Semantic proposal and human decision

The foreground agent is instructed to distinguish recurrent standing preferences from task-specific corrections. It must propose at most 15 imperative sentences, most recurrent first, giving candidate numbers and distinct-session counts. The declared threshold is evidence from at least two different sessions. This synthesis is natural-language model work in the host, not an internal deja model call or a code-enforced recurrence test (SRC-1, `skills/deja-search/SKILL.md`, `cmd/deja/rules_candidates.go`).

> 2. Find the standing rules in that list: preferences the user would want applied in every future session, stated in at least two different sessions. Ignore one-off corrections about a specific task. For each rule give one imperative sentence, the `#n` that state it, and how many distinct sessions. At most 15, most recurring first.
> --- `skills/deja-search/SKILL.md`

The proposed list is handed to the user. The user can select none or only some. The foreground agent must stop before writing and then show the exact lines to append. The user is the prescribed semantic decision owner; candidate citations and counts are review aids, not an independent expected-answer oracle. The Go command does not verify user selection, accurate candidate citations or model obedience. File access can bypass this procedural gate (SRC-1, `skills/deja-search/SKILL.md`, `cmd/deja/rules.go`; see [RT-RTE-rules-sync](runtime.md#rt-rte-rules-sync)).

The minimum passage establishing that stop and subsequent handoff is retained in the supplied runtime route. Its force is an instruction to the foreground agent, not a sandbox or approval token. No child agent is launched by this workflow; a separate context or return-from-worker protocol is not established here.

### Admission and delivery

After selection, the foreground agent is instructed to append only the chosen lines to the source file named by `deja rules`, then call `deja rules sync`. The source resides under XDG configuration as `deja/rules.md`. The source append is performed by the host agent's file/shell tools; deja's sync reads that file and distributes its current contents. Candidate extraction itself does not revise the rules source (SRC-1, `skills/deja-search/SKILL.md`, `cmd/deja/rules.go`).

Before distribution, Go rejects a source over 8 KiB or containing deja's own block delimiters, removes an initial byte-order mark, normalizes CRLF and trims trailing whitespace. These checks admit a structurally usable text block, not a true, helpful or user-approved rule set. Sync chooses known, ready rule-file targets from recorded installations, with a configuration-directory fallback when no installations are recorded. Consequently the skill's phrase “every installed agent” is implemented through known paths and readiness checks, not guaranteed universal host coverage (SRC-1, `cmd/deja/rules.go`).

Each target receives a marked copy of the normalized source. Complete prior rule blocks are replaced, while text outside the blocks is retained with separator handling. Dedicated rule files may also receive host-specific headers. This is a transition from historical evidence into intentionally standing instructions, rather than merely framed recall. The later intended consumer is each host's instruction loader/model, described by [RT-BAP-standing-rules](runtime.md#rt-bap-standing-rules) (SRC-1, `cmd/deja/rules.go`, `cmd/deja/marked_block.go`).

At the software boundary, delivery consists of per-target write/unchanged/remove outcomes and an aggregate command result. `deja rules` or `status` compares source and marked copies and can identify missing, stale or unbounded blocks. These comparisons do not establish that a host loaded the file or that a later model applied the rule. The inspected workflow has no post-distribution behavioral correctness test (SRC-1, `cmd/deja/rules.go`; [RT-RTE-rules-sync](runtime.md#rt-rte-rules-sync)).

### Rejection, recovery and reversal

A concrete rejection path is an unmatched whole-line start delimiter in an existing target file. Replacement refuses rather than guessing where user-owned text ends. A lone end marker is not symmetrically refused, so this check should not be generalized to all delimiter irregularities (SRC-1, `cmd/deja/marked_block.go`).

> if open {
> 	return fmt.Errorf("deja's %s block has no end marker — put it back, or delete the block entirely", what)
> }
> --- `cmd/deja/marked_block.go`

The error is annotated with the target path. Sync continues attempting other targets and returns the refused-file errors at the end. A failed sync can therefore have already changed some hosts; it is not an all-host transaction. The user or foreground agent must repair the named block boundaries and retry distribution. Status explicitly reports an unbounded block as needing manual repair (SRC-1, `cmd/deja/guidance.go`, `cmd/deja/rules.go`).

> if err != nil {
> 	refused = append(refused, err.Error())
> 	continue
> }
> --- `cmd/deja/rules.go`

To reverse selected rules, edit the source and sync again. Empty or absent source means no rule block to copy and causes existing bounded copies to be removed; a file containing only deja's block/header can be deleted. This is source-driven reversal, not an established automatic restoration of an earlier semantic rule set. Failed targets still require repair/retry. The source and copies persist for later sessions, but actual loading, improved behavior and the historical measurement claims in the skill were not observed in this run (SRC-1, `cmd/deja/rules.go`, `skills/deja-search/SKILL.md`).

### Added inspection coverage

Implementation inspection expanded to all of `cmd/deja/rules_candidates.go` and `cmd/deja/marked_block.go`; `cmd/deja/rules.go` constants, readiness checks and source/status/sync/removal functions; `cmd/deja/guidance.go`'s `markerErrorFor`; and the opening guards of `cmd/deja/install.go`'s `writeIfChanged`. Doctrine/design inspection covered the complete `skills/deja-search/SKILL.md`. All are SRC-1 at the reviewed commit. The narrow helper inspection does not establish full file-write durability, every host-specific mapping or rollback across concurrent writers. No target code, tests, examples, provider or host was executed.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

none declared in this member

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-rules-sync](runtime.md#rt-rte-rules-sync)

Workflow handoffs: user request → foreground agent → binary candidate extraction → foreground semantic proposal → user selection → foreground source append → binary distribution → later host instruction consumption. Extraction and distribution are implemented; proposal, stopping and selected-only writing are instructed host behavior.

Verification scope: candidate provenance and session counts support user review; source-size/delimiter checks and copy comparison assess file structure/state. Neither verifies rule truth or later compliance. Candidate clipping and text-prefix deduplication constrain recurrence evidence.

Recovery ownership: the binary reports source/target refusal and continues eligible target attempts; the user or foreground agent repairs content/boundaries and retries. Partial success remains possible. Editing or emptying the source followed by sync reverses bounded copies, not necessarily already exercised model behavior.

Delivery criterion: successful distribution is a file-level outcome for selected known/ready targets, distinct from host loading and behavioral use. Operation conclusion status remains uninspected.
