---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Labyrinth Exploration's Codex campaign from open conjectures through independent review, integration and project handoff."
run-id: AAS-2026-11-23-labyrinth-exploration-4000731242d4-01
reviewed-boundary: "019a93da59313e697dc6f28bcfe1588a376c7565"
---

# Labyrinth Exploration workflow report

## Workflow account

**Selected workflow: a Codex research campaign in an existing project.** This is the skill's prescribed route when more promising questions are open than one iteration can handle. It is representative because one campaign connects delegated discovery, independent checking and document delivery. The coordinator runs the campaign through the host's tools; the project engine handles files and views, not delegation or scientific judgment. This is a trace of the shipped procedure, not a reconstruction of a completed campaign ([RT-RTE-research-iteration](runtime.md#rt-rte-research-iteration); SRC-1 `references/loop.md`, `references/campaigns.md`, `references/codex.md`, `templates/lab.py`).

1. **Request → assignments.** The user asks to advance the research programme with the installed skill. The coordinator reads project status and the dashboard, checks any outstanding agents and jobs, and chooses the questions. It turns the guide, labeled proofs and list of what's missing into briefs. Each attacker receives a precise question, several suggested approaches, failed approaches with lessons, reusable files, a unique output directory and a share of the session's compute budget. A literature agent returns leads that the coordinator forwards while attacks are underway; a lead needs a source check before use. The coordinator records thread ID, role, output directory and state in the journal. Staggering is a scheduling instruction, not a concurrency control implemented by the skill ([RT-BAP-brief-worker](runtime.md#rt-bap-brief-worker); SRC-1 `SKILL.md`, `references/codex.md`, `references/campaigns.md`, `templates/briefs/attack.md`).
2. **Assignments → pending evidence.** The attacker produces proofs or scripts and data in its own directory. Its final message gives item-level statements, status and proof or script locations, plus dead ends and next steps. The coordinator saves the message verbatim, initially marks its provenance as not yet refereed, and logs the result as under review. A key claim can go to review before the whole attack finishes. The event write makes work visible without admitting it as established. On a missing completion notice, the coordinator looks for the final message in the transcript before requesting a redo. On a limit reset it resumes existing agents if possible; after a restart it consults reports and events and checks actual thread and job state before replacing work. A queued job or a notification is not proof of completed computation ([RT-RTE-event-append](runtime.md#rt-rte-event-append); SRC-1 `references/campaigns.md`, `references/codex.md`, `templates/briefs/attack.md`).

   > If a completion notification never arrives, look for the final message in the session's
   > transcript before asking the agent to redo the work.
   > --- `references/campaigns.md`

3. **Evidence → verdict → admission decision.** The coordinator starts a fresh referee with the claim, definitions, raw evidence and specific concerns such as quantifier order or missing hypotheses. The reviewer may read the author's material as specified but must not reuse its verification code. Where the host offers context control, Codex guidance calls for a minimal brief rather than inherited attacker reasoning. The referee returns an itemized verdict, reasons, evidence locations and exact corrections. For computations, an independent per-member recomputation supplies a reference outcome; if full recomputation is too expensive, the brief allows a stated random sample, not a claim of exhaustive agreement. The coordinator adds its own small exact spot check. An ESTABLISHED WITH CORRECTIONS verdict is not permission to use the original text. GAP or FALSE withholds the item as stated. For a refutation, the loop prescribes recording the counterexample and lesson and testing a modified statement. If delegation is unavailable or prohibited and no independent check exists, the coordinator may continue authorized exploration but leaves the result pending. The referee can supply grounds for withholding; the coordinator owns the admission decision and canonical edits. No general answer key is supplied, and neither host context isolation nor referee independence was observed ([RT-RTE-review-integration](runtime.md#rt-rte-review-integration); SRC-1 `SKILL.md`, `references/codex.md`, `references/loop.md`, `templates/briefs/referee.md`).

   > Code you may read for definitions but must **not** reuse for verification:
   > `<the agent's code and earlier engines>`. Your verification code is your own, written from
   > the definitions in the write-ups.
   > --- `templates/briefs/referee.md`

4. **Verdict → writer draft → canonical text.** For a result that can be integrated, the writer receives the attack write-up and report, referee report with required corrections, local style guide and target section. It returns a LaTeX block, uniquely anchored replacements and a build result from a copy ([WF-RTE-writer-draft](#wf-rte-writer-draft)). The coordinator compares the draft to the verdict and checks references, then applies script-checked unique replacements and builds after each insertion. If one edit changes another's anchor, the second is re-anchored after the first. A clean draft build does not prove that the prose preserves the verdict. The campaign document reports that a draft changed “and” to “or” without support and the change was reverted; it does not include the draft, transcript or build result. For long runs the prescribed split is to commit data and events as under review first, then commit notes after review if committing is in scope. The intermediate checkpoint is not scientific admission or an automatic rollback ([RT-RTE-review-integration](runtime.md#rt-rte-review-integration); SRC-1 `references/campaigns.md`, `templates/briefs/writer.md`, `SKILL.md`).

   > **Read every draft against the referee's verdicts.** Writers drift. One weakened a
   > conjecture from "and" to "or" with no support, and the change was reverted. Check that
   > every label and cross-reference exists and points where the text says.
   > --- `references/campaigns.md`

5. **Canonical update → user handoff.** The coordinator updates graph tier, status and review, table history, events and frontier data. It rebuilds derived documents from anchors and reviews any supervised editor's changes to those documents. The prescribed close uses `check && build` and hands over the updated documents and dashboard path with changes in resolved fractions, theorems, refutations, new questions and outstanding checks or jobs. If the file check fails, the coordinator must address diagnostics before using that chained build; a direct build does not enforce this ordering. The check is about consistency, not the referee verdict, so a successful build cannot substitute for scientific review. The default deliverable is local; a private deployment requires user authorization and an access-policy check. The journal, plan and project memory preserve what to resume. Delivery in this procedure is a user-facing handoff with accessible artifacts and explicit pending work, not just a worker's final message. The source does not show that these delivery steps ran or that a user received or rendered the result ([RT-RTE-build-views](runtime.md#rt-rte-build-views); SRC-1 `SKILL.md`, `references/campaigns.md`, `references/codex.md`, `templates/lab.py`).

**Inspected coverage and limits.** At the pinned revision, this trace adds detailed coverage of the attack, referee and writer brief inputs and returns, the Codex journal and restart handoffs, and the campaign integration and session-close instructions (SRC-1 `templates/briefs/attack.md`, `templates/briefs/referee.md`, `templates/briefs/writer.md`, `references/codex.md`, `references/campaigns.md`, `references/loop.md`, `SKILL.md`). These are doctrine/design. The revert anecdote is reported operation. The engine behavior cited above comes from the baseline's implementation trace, not execution evidence. Directory ownership, independent checking and authorized publication are coordinator policies; the source supplies no observed host permission enforcement, review compliance or campaign effectiveness.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

#### WF-RTE-writer-draft
Label: Draft and test on a copy
Part of: [RT-RTE-review-integration](runtime.md#rt-rte-review-integration)

This is the draft-producing part of the supplied integration route, with its own temporary document, checks and return before canonical admission. Coordinator → writer after the verdict → coordinator review. The writer proposes text and replacements against the target section and referee corrections. Its build checks presentation and references on a copy, not mathematical truth. The coordinator can reject or revise the proposal before applying it; the writer cannot change canonical files by policy. In this open research campaign the referee verdict constrains what can be stated; there is no new scientific answer oracle at the drafting step. SRC-1 `templates/briefs/writer.md`, `references/campaigns.md`.
- doctrine conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: LaTeX block, exact OLD → NEW edits, insertion anchor and final report with test result.
- Later read-back: inapplicable — the draft is sent for current integration; subsequent use of admitted canonical text belongs to the parent route.
- Delegated visibility: Style guide, target section and labels, attack write-up and report, and referee report with identified corrections.
- Selection predicate: Coordinator sends the writer only after the verdict, with refereed results to draft.
- Invalidation or expiry: Delete the test copy at the end; re-anchor replacements if earlier accepted edits changed their target.
- Activation or effect: Produces a candidate edit set and copy-build result; only coordinator integration can make it canonical.
- Evidence limits: Shipped brief and campaign instructions, not observed draft output, test execution or write isolation.

> **Test** on a copy of the notes (`research/agents/integration/test-<topic>/`; delete it at the
> end): insert the block, apply the edits, build twice, and require zero errors, zero
> undefined references and zero overfull boxes.
> --- `templates/briefs/writer.md`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-research-iteration](runtime.md#rt-rte-research-iteration)

Campaign coordination: the journal's thread, role, directory and state entries support recovery; the coordinator checks actual agent and job state before replacement rather than treating a prior journal entry as live state. SRC-1 `references/codex.md`.

#### On [RT-RTE-review-integration](runtime.md#rt-rte-review-integration)

Campaign integration: the writer's copy build is a distinct check, linked at [WF-RTE-writer-draft](#wf-rte-writer-draft). A successful copy build still leaves verdict fidelity to the coordinator's comparison against the referee report. SRC-1 `references/campaigns.md`, `templates/briefs/writer.md`.
