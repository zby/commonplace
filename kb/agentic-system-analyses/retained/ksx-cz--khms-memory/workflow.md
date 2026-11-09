---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "KHMS memory workflow: one operational MARK through isolated proposal evaluation, review admission, recovery and later foreground recall."
run-id: AAS-2026-11-08-khms-memory-c5267e800c56-01
reviewed-boundary: f739eb976dab199fd4cd64e352192cc0b112c047
---

# KHMS memory workflow report

## Workflow account

### Selection and evidence boundary

The representative workflow is retaining a finding from foreground work and making it available to a later agent: journal MARK → nightly proposal → morning review/import → later recall. It was selected because it crosses the system's central authority boundary, from unreviewed evidence to approved knowledge, and connects production to consumption. This is a source-supported workflow, not a reconstruction of a real successful run. SRC-1 supplies implementation and doctrine/design at the revision in [boundary](boundary.md); no observed execution or causal benefit is established. The enclosing agent owns the original task and the eventual user answer. KHMS owns capture guidance, proposal machinery, import and recall, not the host's reasoning or action scheduler.

### 1. Capture supplies the background job, not a delegated conversation

The foreground agent is instructed to capture a decision, requirement, failure or solution as one line in the daily journal while working. That instruction supplies a cheap handoff artifact rather than assuming that the later background model inherits the session. SRC-1: `AGENTS.md`.

> One line per decision, stated requirement, failed attempt, solved problem. Kinds are open;
> those four cover most of it.
> --- `AGENTS.md`

A scheduler or manual caller later starts the nightly shell driver. The driver, not a model manager, owns progression: it prepares source windows/chunks, invokes generation, persists generated MARKs, and sends queued journal/generated IDs to per-MARK evaluation. The source's older sweep/consolidate description is not used to insert a second model approval of current per-MARK candidates. Current per-MARK output proceeds to post-processing and durable carry without another consolidation call. These handoffs and their evidence are established by [RT-RTE-nightly-proposals](runtime.md#rt-rte-nightly-proposals) and [RT-RTE-mark-evaluation](runtime.md#rt-rte-mark-evaluation). The generated branch supplies additional candidate events; it is not evidence that the foreground agent captured every relevant finding.

### 2. Code delegates one bounded decision and retains only its result

For each undecided MARK, `permark.run` prepares an input packet and invokes the external agent CLI without tools or session persistence. Its rules/schema/tag guidance are separate from the packet. The packet supplies the MARK, nearby journal lines, related existing cards, selected earlier candidates from tonight, and a source excerpt when available. The model decides whether to propose a new card, attach to an earlier candidate, propose correction, or give a not-carded/already-carded verdict. These are proposal decisions, not authority to install knowledge. The configured headless model is [RT-CMP-agent-model](runtime.md#rt-cmp-agent-model); the delegation and parsing belong to [RT-RTE-mark-evaluation](runtime.md#rt-rte-mark-evaluation).

The actual recipient sees a selected representation, not the entire base. `build_packet` can show some cards whole and others as summaries. When its character target is exceeded it drops lower-ranked cards/candidates first, then trims the beginning of the source excerpt, then removes journal context farthest from the MARK. It preserves the MARK's own context line and returns the remaining shown IDs to downstream checks. Consequently, lack of a matching sentence in this packet does not establish lack of that information in the base. SRC-1 implementation: `tools/permark.py`.

Each invocation resembles an isolated task frame: prepared inputs enter; returned text and metadata leave; parsed candidates and verdicts persist in the parent document. It is not a shared conversation among autonomous subagents, nor a compactor of the foreground agent's window. Persisted candidates influence the packets for later MARKs, but the model does not retain its own session context. See the workflow-specific packet annotation below.

### 3. Verification can repair or withhold output, but is not a truth oracle

The evaluator retries a failed call up to twice; failed or unparsed responses do not update the proposal document. An optional format checker can spend another call on repair. A failed format repair retains the first answer for later checking, rather than necessarily rejecting it. Quota/deadline/cost stops leave unfinished work open. These distinctions are documented in [RT-RTE-mark-evaluation](runtime.md#rt-rte-mark-evaluation), including the implementation excerpts.

The nightly driver then performs post-processing and publication. Its checks are not one fail-closed gate: quote-check exit status is tolerated, relation checking is skipped when nearest-card preparation fails, and `postprocess_batch` returns success. Header normalization/quarantine is a separate step. Thus reaching an inbox is not equivalent to passing every check, much less to establishing truth. The source performs deterministic consistency/format tests and requests model judgment; neither constitutes a supplied expected-answer oracle for semantic correctness. SRC-1: `tools/nightly_distill.sh`; see the post-processing annotation below.

### 4. Durable carry defines recovery before delivery to review

The shell commits post-processed evaluator output to carry, including ready batch outputs, before publication. Its source comments distinguish a kill before commit, which leaves MARKs eligible for re-evaluation, from a kill after commit, which leaves output in carry. Budget or usage stops commit completed decisions while leaving the rest open. This is implemented recovery design, not a successfully observed restart. SRC-1: `tools/nightly_distill.sh`.

> # A deadline, the dollar cap (MARK_BUDGET_USD, #243) or the usage limit ends the evaluator early: what it decided
> # is committed, the rest stays OPEN. The cap writes one line `MARK stage stopped at the $ cap: …` (exit 0).
> --- `tools/nightly_distill.sh`

On later runs the driver verifies whether a batch was already published, publishes surviving durable output without another model call, or resumes work that still needs one. A conflicting publication is retained for manual resolution, not silently overwritten. The recovery owner is therefore shell code for recognizable durable states and the operator for unresolved conflicts. [RT-RTE-nightly-proposals](runtime.md#rt-rte-nightly-proposals) retains the conflict-path evidence. An immutable inbox unit is delivery to the reviewer, not admission to the approved base.

### 5. Review and import separate semantic judgment from mechanical acceptance

The morning reviewer is told to inspect flagged content, fix or withhold candidates, and invoke `approve_inbox.py`. Withheld DEFERRED/DROPPED trailers are excluded by the importer. Accepted candidates receive allocated K IDs and remapped references; existing relation/status metadata and generated views are updated. Parse/schema/lint constraints and duplicate-label checks can refuse import. A partial import is not a completed review, and receipt-aware recovery is not rollback of an atomic all-files transaction. These mechanisms and the importer excerpts are in [RT-RTE-card-admission](runtime.md#rt-rte-card-admission).

The admission policy requires separate human-or-strong-model review, but the CLI does not authenticate that review. The background generator's file tools are also not path-confined by KHMS command arguments. The source therefore establishes a protocol and a checked import path, not an unavoidable security boundary excluding every unreviewed write. See [RT-CLM-review-boundary](runtime.md#rt-clm-review-boundary) and the runtime's forcing case. No real reviewer decision is evidenced here.

For foreground delivery of review work, the instructions additionally require reporting to the operator after import:

> Finish
> with a two-sentence report to your operator in their language.
> --- `AGENTS.md`

That is a prescribed communication endpoint, not a report automatically generated or verified by the importer.

### 6. Later recall completes availability, not demonstrated use

A later foreground task can invoke explicit recall or receive context from an installed matching host hook. Ranking, live-card rules, budgets and deduplication determine which retained content reaches that invocation. CLI output can also include separately labelled unreviewed evidence; it is not exclusively approved knowledge. The next-step owner is the receiving agent/host, which must decide whether to open a pointer, follow evidence links and use the content in an answer or action. [RT-RTE-recall-return](runtime.md#rt-rte-recall-return) and [RT-BAP-context-delivery](runtime.md#rt-bap-context-delivery) establish the implemented return channels and limits.

The source explicitly distinguishes injection from reading and judgment:

> **An injected card is a pointer, not an answer.** If it is relevant, open the file and follow
> its links (`derived_from`, `supports`, `contradicts`, and any `[[K-…]]` in the body).
> --- `AGENTS.md`

Hook errors fail open and installation remains an external dependency. There is no supplied trace linking a captured finding to approved content, its later selection, an agent's changed behavior and a delivered successful answer. The bounded result is an inspectable end-to-end availability workflow with resumable proposal state and separate review admission, not proven capture completeness, review compliance, reliability or benefit.

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

#### On [RT-RTE-mark-evaluation](runtime.md#rt-rte-mark-evaluation)

Workflow-specific handoff selection: the source packet is not guaranteed to fit its target if the retained mandatory material alone exceeds it. Code attempts successive removal but stops before removing the MARK's own journal line. The shown-ID return reflects removed cards. This limits what subsequent relation/quote judgments can establish about unseen retained content. Additional implementation coverage within SRC-1: `tools/permark.py`, `build_packet`.

> for d, t in sorted(ctx, key=lambda x: -x[0]):       # 3. journal context, farthest from the mark first
>         if len(text) <= budget or d == 0:
>             break
>         ctx_keep.remove((d, t))
>         text = render()
> --- `tools/permark.py`

> return (text, [key for key, _t in cards if ("card", key) not in drop],
>             [key for key, _t in tonight if ("tonight", key) not in drop])
> --- `tools/permark.py`

#### On [RT-RTE-nightly-proposals](runtime.md#rt-rte-nightly-proposals)

Workflow-specific verification limits: the post-processing shell does not treat every failed subprocess as a blocked publication. Additional implementation coverage within SRC-1: `tools/nightly_distill.sh`, `postprocess_batch` and `publish_batch`. These are code facts, not observations of malformed output reaching review.

> python3 "$CODE/verify_quotes.py" "$f" --source digest="$dg" --source journal="$jv" \
>     --source gitlog="$gl" > "$qr" 2>&1 || true
> --- `tools/nightly_distill.sh`

> python3 "$CODE/verify_relations.py" "$f" > "$rr" 2>&1 || true   # report, not a gate
> --- `tools/nightly_distill.sh`

> echo "$(date -Is) === verify_relations === SKIPPED for $tag — nearest(post) FAILED, and a RELATION gate without NEAREST lines would drop candidates for the tool's own reason" >> "$LOG"
> --- `tools/nightly_distill.sh`

Malformed-header recovery is narrower than rejecting an entire batch: if normalization fails the driver invokes quarantine, preserving the candidate under a dropped trailer for review rather than guessing a header. The publisher remains a separate check after that attempted quarantine.

> if ! python3 "$CODE/card_header.py" fix "$1" >> "$LOG" 2>&1; then
>     python3 "$CODE/card_header.py" quarantine "$1" >> "$LOG" 2>&1 || true
> --- `tools/nightly_distill.sh`
