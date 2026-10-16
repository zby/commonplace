---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "MentisDB workflow account: source-prescribed auth-debugging handoff, filtered retrieval and continuation admission, with delivery and recovery limits."
run-id: AAS-2026-10-14-mentisdb-a8b5903ae3e2-01
reviewed-boundary: "4c9b95041da68c5a26dece9f8776ff54b05b910c"
---

# MentisDB workflow report

## Workflow account

### Selected workflow and evidence boundary

The representative workflow is the cookbook's transfer of an unfinished auth-test investigation from a previous agent to a next agent. It was selected because one contiguous example supplies the work state, retained handoff, selector and accepting write, rather than requiring unrelated capabilities to be joined. It reaches a delivered continuation marker, not a demonstrated repaired application. MentisDB supplies memory coordination; the enclosing host owns task execution and agent scheduling. See [WF-RTE-session-continuation](#wf-rte-session-continuation) and the broader [RT-RTE-memory-roundtrip](runtime.md#rt-rte-memory-roundtrip).

Evidence is SRC-1 at the boundary's frozen revision. Additional workflow inspection covered the pattern and Rust example in `docs/cookbook/cookbook-2-2-cross-session-continuity.html`, the daily loop in `docs/cookbook/cookbook-1-0-operator-playbook.html`, the full `MENTISDB_SKILL.md`, and reference checking and append construction in `src/lib.rs`. Cookbook and skill passages are doctrine/design, including executable example text; core checks are implementation. No example, test, host or provider was executed. Thus the sequence is source-supported, not an observed multi-session run.

### Request, handoff and continuation

1. **Orient before work.** The operator playbook prescribes opening the chain, reading context, searching prior decisions and then editing, testing and reviewing. The host decides which task to perform and when to call MentisDB. Startup and search-before-write guidance remain host-interpreted protocols, not prerequisites enforced by the append API. See [RT-CLM-startup-protocol](runtime.md#rt-clm-startup-protocol). SRC-1, `docs/cookbook/cookbook-1-0-operator-playbook.html`, `MENTISDB_SKILL.md`.
2. **Previous agent transfers incomplete work.** The concrete example opens a binary-backed chain, registers `agent-prev` and `agent-next`, and appends a `Handoff` with role `Handoff`, concepts `auth-flake` and `test-debugging`, tags and importance. Its content separates completed reproduction from unresolved diagnosis and gives the next action. This is instruction and state passed through memory, not a MentisDB-created child-agent invocation. SRC-1, `docs/cookbook/cookbook-2-2-cross-session-continuity.html`.

> "Done: reproduced the flaky auth test. Pending: isolate whether cache state or clock skew causes it. First next step: rerun with fixed clock.",
> --- `docs/cookbook/cookbook-2-2-cross-session-continuity.html`

3. **Next agent retrieves selected work.** The example queries with an auth-investigation question, filters by `Handoff` role and `auth-flake` concept, and limits results to one. It asserts one hit. This is a bounded selection, not an unfiltered restoration of the prior conversation. Importantly, the example already has `handoff_index` in its local variables: it does not extract the continuation target from the selected hit. Its single function uses the same open chain for both agent identities and never closes and reopens between sessions. It illustrates the intended cross-session protocol but does not itself establish process restart, an independently starting next agent, or correct choice among competing handoffs. The general reload path is separately established by [RT-RTE-memory-roundtrip](runtime.md#rt-rte-memory-roundtrip). SRC-1, `docs/cookbook/cookbook-2-2-cross-session-continuity.html`.
4. **Accept by writing, not merely reading.** `agent-next` appends a `Checkpoint` referring to `handoff_index`, with content saying it will start with a fixed-clock rerun before changing cache code. The example asserts that the continuation's refs match. That write makes the declared acceptance available in retained state. It neither runs the fixed-clock test nor verifies the diagnosis. SRC-1, `docs/cookbook/cookbook-2-2-cross-session-continuity.html`.

> assert_eq!(continuation.refs, vec![handoff_index]);
> --- `docs/cookbook/cookbook-2-2-cross-session-continuity.html`

The source uses two handoff conventions: this cookbook example uses a dedicated `Handoff` type/role, whereas the core skill asks for `Summary` with role `Checkpoint`. The example's role filter therefore does not establish retrieval of the skill's differently typed handoffs. A host following one convention must select accordingly; the report does not treat them as automatically interchangeable. SRC-1, `docs/cookbook/cookbook-2-2-cross-session-continuity.html`, `MENTISDB_SKILL.md`.

> 4. **Handoffs = `Summary` with `role: Checkpoint`** — include what's done, pending, and next steps.
> --- `MENTISDB_SKILL.md`

### Verification, rejection and recovery

The concrete workflow has two example assertions: one selected hit and a retained backlink. They check structural results, not whether the investigation succeeded. Runtime storage construction and integrity checks cover a different question: whether a record meets structural/hash rules, not whether its natural-language claims are true. See [RT-OBJ-thought](runtime.md#rt-obj-thought) and [RT-RTE-memory-roundtrip](runtime.md#rt-rte-memory-roundtrip). No reference answer selects a correct auth diagnosis. Host-side tests and review are requested by the daily loop, but their execution and task acceptance are outside this example. SRC-1, `docs/cookbook/cookbook-1-0-operator-playbook.html`, `docs/cookbook/cookbook-2-2-cross-session-continuity.html`, `src/lib.rs`.

A supported rejection path is an invalid continuation ref. The core append method calls `validate_refs` before constructing and persisting the thought. A ref outside the current chain's range returns `InvalidInput`; it cannot be accepted as the intended continuation. The calling example uses `?` to propagate append errors and contains no retry handler. Recovery therefore remains with the caller: resolve an existing handoff target and decide whether to resubmit. This is a plausible available repair, not an implemented automatic recovery loop. SRC-1, `src/lib.rs`, `docs/cookbook/cookbook-2-2-cross-session-continuity.html`.

> validate_refs(&self.thoughts, &input.refs)?;
> --- `src/lib.rs`

> if reference as usize >= thoughts.len() {
>     return Err(io::Error::new(
>         io::ErrorKind::InvalidInput,
>         format!("Thought reference {reference} does not exist"),
>     ));
> }
> --- `src/lib.rs`

This pre-admission rejection differs from a downstream append error: canonical storage may already have changed before derived work fails. A caller must not infer non-admission from every error and blindly replay the write. The supplied runtime record retains the storage-order evidence and limits; no transaction-wide rollback is established. See [RT-RTE-memory-roundtrip](runtime.md#rt-rte-memory-roundtrip).

### What counts as delivery

Within MentisDB, the example's endpoint is a successfully appended continuation with a reference to the previous handoff and a successful function return. The selected handoff and retained acceptance are delivered memory artifacts. A generated statement that a rerun is starting is not evidence of execution, and a `TaskComplete` label would not independently prove task correctness. The core skill asks agents to save completion and flush memories before exit; it does not supply an enclosing scheduler or acceptance controller. Actual resumed debugging, the final fix and operator acceptance remain unobserved. SRC-1, `docs/cookbook/cookbook-2-2-cross-session-continuity.html`, `MENTISDB_SKILL.md`.

Before context loss, the host is told to distill a checkpoint. What survives is selected text plus chain-addressable records, not a restored live model frame. In the next invocation the host requests a bounded subset by value. MentisDB does not itself demonstrate clearing the host window, dispatching a fresh agent, or transmitting all of the prior agent's working context. See [RT-BAP-retained-context](runtime.md#rt-bap-retained-context). SRC-1, `MENTISDB_SKILL.md`, `docs/cookbook/cookbook-2-2-cross-session-continuity.html`.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

#### WF-RTE-session-continuation
Label: Session handoff and accepting continuation

Part of: [RT-RTE-memory-roundtrip](runtime.md#rt-rte-memory-roundtrip)

This is the concrete two-agent handoff subroute of the broader memory admission/read-back route, not a replacement identity for that route. Endpoints/progression: previous agent's unfinished investigation → stored handoff → filtered ranked retrieval → next agent's referenced checkpoint. The caller owns the investigation, identities and acceptance content; core code owns ref validation and persistence. Context effects are selected handoff text and a resumable next action; state effects are two appended records. Evidence: SRC-1, `docs/cookbook/cookbook-2-2-cross-session-continuity.html`, `src/lib.rs`; minimum passages are retained in the workflow account.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: append returns the new thought or an I/O error; query returns ranked candidates; the example returns `Ok(())` after asserting the accepting ref.
- Later read-back: stored handoff and continuation can be retrieved later; the example illustrates the sequence within one function and does not exercise reopening.
- Delegated visibility: the two named agent identities use the same chain; a separate host must arrange access and dispatch. No autonomous sub-agent launch is demonstrated.
- Selection predicate: text about resuming the auth investigation, role `Handoff`, concept `auth-flake`, limit one; the continuation uses the previously held handoff index rather than resolving it from the query hit.
- Invalidation or expiry: no expiry or invalidation is applied in this example; the broader memory route supports relation-driven invalidation and later audit reads.
- Activation or effect: handoff and accepting checkpoint writes are wired; the asserted intention to rerun does not establish resumed debugging or changed model behavior.
- Evidence limits: source example and implementation only; no true session boundary, competing-handoff selection, fixed-clock test, host execution, successful fix or causal benefit was observed.

Admission: caller-provided content proposes the handoff and next action; software admits structurally valid refs and storage writes. The next agent's acceptance is another caller-provided statement, not an independent task-quality judgment. Human authorship or per-content approval is unresolved. Invalid refs can veto admission; callers can withhold or revise proposals. Operating mode is an open caller-directed handoff, with session end/context loss as prescribed triggers. Guidance says to preserve done, pending, risks and next steps; those statements and links persist. Recovery is caller-owned error handling or later correction, not automatic rollback. Answer oracle: inapplicable — the example checks hit count and backlink structure, not an expected auth-test outcome. SRC-1, `docs/cookbook/cookbook-2-2-cross-session-continuity.html`, `MENTISDB_SKILL.md`, `src/lib.rs`.

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-memory-roundtrip](runtime.md#rt-rte-memory-roundtrip)

Workflow-specific delivery boundary: a receiving agent's accepting write distinguishes recorded transfer from read-only orientation. Structural acceptance does not certify task execution. The representative handoff subroute is [WF-RTE-session-continuation](#wf-rte-session-continuation); the receiving host remains responsible for independently finding the target, carrying out the next step and checking its result.

#### On [RT-BAP-core-skill](runtime.md#rt-bap-core-skill)

Workflow-specific coordination boundary: pre-warming shared memory, coordinator-supplied identities, wave-by-wave synthesis and pre-exit flushing are instructions to the enclosing host. They do not establish a MentisDB-owned launch, join, retry or final-task acceptance mechanism. The cookbook's direct Rust example registers identities itself, so it is not a demonstration of host compliance with the skill's user-authorization rule.
