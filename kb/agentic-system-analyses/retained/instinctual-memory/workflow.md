---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Instinctual Memory workflow: host-agent cleanup request, preview, user keep choices, recomputed suppression and delivery."
run-id: AAS-2026-10-12-instinctual-memory-af48437aa60c-01
reviewed-boundary: "6acb13dc35765bf5ccfc87e445dd09c480f1c28a"
---

# Instinctual Memory workflow report

## Workflow account

### Selected workflow and evidence boundary

The representative workflow is `/mem tidy`: a host agent previews proposed cleanup, presents it to the user, receives keep choices and invokes cleanup application. It was selected because the shipped skill explicitly connects request, computation, human review and durable delivery. This is a coordinated host-agent procedure around a memory tool, not an internal multi-agent runtime. The host owns command sequencing and communication; the Rust implementation owns candidate selection and publication. The skill supplies the intended handoffs, while source code supplies their executable limits. No supplied execution trace establishes that an agent followed the procedure or that cleanup improved memory.

The baseline identities are [RT-OBJ-mem-skill](runtime.md#rt-obj-mem-skill), [RT-RTE-tidy-maintenance](runtime.md#rt-rte-tidy-maintenance) and [RT-CMP-llm-config](runtime.md#rt-cmp-llm-config). This member adds workflow detail to those records rather than declaring the same referents again. Evidence is SRC-1 at the boundary's frozen revision. Added inspection covers the complete skill, the production cleanup function and its publication helper in `src/tidy.rs`, and the cleanup output handler in `src/cli.rs`. These are doctrine/design and implementation evidence, not observed operation.

### Request and first delegation

The skill recognizes `/mem tidy` or noisy memory as the cleanup trigger. Before the requested action, it tells the host to check command availability and `mem status`; if the command is missing, tell the user and stop. A missing store leads to initialization and sync. The separate sync procedure is conditional on requested sync, an empty journal or stale memory before answering; it is not a mandatory cleanup-specific extraction pass. The user delegates the cleanup task to the host; the host delegates fact inspection to `mem --output-format text tidy` (SRC-1, `skills/mem/SKILL.md`). The skill's review instruction and exact command handoff are retained in [RT-OBJ-mem-skill](runtime.md#rt-obj-mem-skill).

The CLI opens `memory.git` and calls the cleanup function with `apply` and keep IDs. A preview uses `apply = false`. Cleanup reads the current Git head and controls, parses eligible entity files, and selects active facts that are neither suppressed nor deleted. Unparseable entity files are skipped by the inspected enumeration, so the report is not an assertion that every stored file was successfully assessed (SRC-1, `src/tidy.rs`, `src/cli.rs`).

### Computational proposal and preview delivery

Duplicate detection processes longer statements first and compares content-word overlap/containment within the implemented entity-family relation, including preference comparisons. This is a heuristic proposal, not semantic verification that the retained statement is more complete. The optional model receives batches of at most 60 remaining fact IDs and statements, not their original source evidence. The prompt asks it to distinguish lasting facts from session-only material and leave uncertain IDs out. Software only accepts returned IDs belonging to the batch. No independent true-answer oracle verifies the model's classifications (SRC-1, `src/tidy.rs`; [RT-RTE-tidy-maintenance](runtime.md#rt-rte-tidy-maintenance)).

The CLI returns a JSON report by default or text containing checked count, session-only findings, duplicate findings and retained duplicate IDs. With no model configuration it explicitly says only duplicates were checked. A preview with findings says nothing changed and offers the apply command. This report is the tool-to-host handoff; showing it to the user remains a host responsibility (SRC-1, `src/cli.rs`).

> None => println!(
>     "\nNothing changed. Run `mem tidy --apply` to forget these {} fact(s) (add `--keep id,id` for any to leave).",
>     report.findings.len()
> ),
> --- `src/cli.rs`

### User review is not a bound approval artifact

The host must show the findings and ask what to keep before invoking `mem tidy --apply --keep <ids to keep>`. The user can veto removal of named IDs through this exclusion list. But the executable receives only an apply flag and keep IDs, not a reviewed preview, approval token or fixed candidate revision. Direct CLI invocation does not require the exchange (SRC-1, `skills/mem/SKILL.md`, `src/tidy.rs`; [RT-RTE-tidy-maintenance](runtime.md#rt-rte-tidy-maintenance)).

Application starts cleanup again from a newly read head and can issue new model judgments. Therefore the removal set can differ from what the user saw even if the store has not changed. Keep IDs exclude matching findings from that new set; they do not restrict removal to the previously displayed IDs. This is the consequential approval gap: following the skill establishes a review interaction, but not immutable per-content approval for the eventual commit (SRC-1, `src/tidy.rs`).

> findings.retain(|f| !keep.contains(&f.fact_id));
> --- `src/tidy.rs`

### Acceptance, rejection and recovery ownership

With apply enabled and nonempty findings, cleanup retracts selected facts, adds soft-forget controls and reasons, refreshes entity bodies and index, then publishes one candidate through DomainValidator and Git compare-and-swap. Validation and CAS can reject structural defects or a changed base; they do not decide whether a session-only judgment is true. The baseline publication evidence is in [RT-RTE-immediate-change](runtime.md#rt-rte-immediate-change), while cleanup's distinct admission and recovery limits are in [RT-RTE-tidy-maintenance](runtime.md#rt-rte-tidy-maintenance) (SRC-1, `src/tidy.rs`, `src/repo.rs`).

A concrete no-change path occurs when the user keeps all proposed IDs, or selection produces no findings. The function returns a report without publication and the text handler prints “Nothing to tidy.” Without a model key, duplicate-only assessment is a disclosed degraded path, not successful session-only verification. A model/parse error propagates before publication, including on apply; cleanup does not publish the already collected duplicate subset after such an error (SRC-1, `src/tidy.rs`, `src/cli.rs`).

> if apply && !report.findings.is_empty() {
>     report.applied_at = Some(forget_all(repo, &head, entities, controls, &report.findings)?);
> }
> --- `src/tidy.rs`

No automatic retry-and-merge or durable-intent recovery is established for this cleanup route. After a returned failure, another invocation is a caller/host decision and recomputes from current state; it is not replay of an approved candidate. Git history retains previous facts, but cleanup does not automatically roll back a successful commit. Host response to failure and successful recovery remain unobserved (SRC-1, `src/tidy.rs`; [RT-RTE-tidy-maintenance](runtime.md#rt-rte-tidy-maintenance)).

### Delivery and later consumption

Executable completion is a report containing the applied revision after successful publication, or a no-change report. Text application output names the forgotten count and revision. The durable delivery is retracted entity facts plus suppression controls and the updated index in one published memory snapshot. User-facing completion additionally requires the host to convey the outcome; no trace establishes that communication (SRC-1, `src/tidy.rs`, `src/cli.rs`).

Later fact retrieval and consolidation reload those controls, as described in [RT-RTE-memory-retrieval](runtime.md#rt-rte-memory-retrieval) and [RT-RTE-journal-consolidation](runtime.md#rt-rte-journal-consolidation). Soft forget does not erase raw journal excerpts or history. Thus successful cleanup narrows curated-fact eligibility, not every possible channel by which the host can encounter the content. It also does not update already delivered context or previously written instruction files. The workflow establishes implemented selection, suppression and return paths; correct removal, host compliance and downstream benefit remain uninspected.

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

#### On [RT-RTE-tidy-maintenance](runtime.md#rt-rte-tidy-maintenance)

Workflow handoffs: user cleanup request → host preview command → report shown to user → keep choices → host apply command → recomputed candidate → publisher result → host completion message. The first, review and final communication steps are shipped host policy; computation and CLI return are implementation wiring. No execution trace establishes the complete chain.

Verification boundary: keep choices veto named findings, while DomainValidator/CAS gate the new candidate. Neither binds application to a previously reviewed preview or verifies semantic classification. The host owns failure communication and any subsequent retry; a retry obtains a new proposal set rather than recovering a saved cleanup approval.
