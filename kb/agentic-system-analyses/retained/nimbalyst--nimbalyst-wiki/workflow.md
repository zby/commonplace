---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Nimbalyst Wiki workflow account: local session capture from destination choice through page maintenance, rejection recovery and linked delivery."
run-id: AAS-2026-11-08-nimbalyst-wiki-d9ff54186a76-01
reviewed-boundary: "97c1ba1594d6e3d466a23d33c1bda084026b01b8"
---

# Nimbalyst Wiki workflow report

## Workflow account

### Selection and evidence limit

The representative workflow is **capturing a coding session into an existing local wiki**. It is selected because the capture skill supplies an ordered procedure connecting changed code, retained page meaning, session decisions, writes and final links. This is one prescribed workflow, not a sequence reconstructed from unrelated tool capabilities. Its canonical route is [RT-RTE-session-capture](runtime.md#rt-rte-session-capture); destination and writing controls are supplied by `connect` and `update` (SRC-1, `skills/capture/SKILL.md`, `skills/connect/SKILL.md`, `skills/update/SKILL.md`).

The account describes what shipped instructions ask the foreground agent to do. The frozen repository contains neither the local server implementation nor an execution trace. Tool responses, storage changes, conflict enforcement and model compliance are therefore unobserved, as established in [boundary](boundary.md). Design conclusion status is claimed; operation conclusion status is uninspected. The registered commit remains the evidence boundary. For this member, the three skill entry points above were read in full at that checkout; they supply doctrine/design, not newly inspected executable behavior. No additional source or source-register entry is introduced.

### 1. Request and destination handoff

The user can ask to record the session, optionally narrowing its focus. A reminder is another declared trigger, but it is not required for this selected invocation; host reminder coverage differs by client ([RT-RTE-host-entry](runtime.md#rt-rte-host-entry)). `capture` hands procedural control to `connect` for destination selection and `update` for every write. These are instruction loads by the same foreground agent, not delegation to independently executing model workers (SRC-1, `skills/capture/SKILL.md`).

> Record what this session decided in the project's wiki. Load the `update` skill and follow it for every write; the `connect` skill covers choosing the wiki and finding the project.
> --- `skills/capture/SKILL.md`

Before continuing, the agent must prefer desktop tools if present. Otherwise it resolves one wiki for the session. In the selected branch a local wiki exists, is not an obsolete migrated copy, and either has no competing bound team destination or the user chooses local. These are branch conditions, not observed facts about a particular checkout. A migrated local copy is not silently eligible for writes; inability to reach its team project requires asking whether to use that copy. With no destination, capture offers a wiki and stops if none is available. If the user declines starting one, there is no delivered page artifact (SRC-1, `skills/connect/SKILL.md`, `skills/capture/SKILL.md`).

The local server takes no team `repo` or `project`. Results name `wikiFolder`; if it is the wrong project, the agent must call `useLocalWiki` before proceeding. This is a destination check owned by the agent, not evidence of enforced isolation. The instruction to use only the chosen server constrains the procedure; the external implementation and other file writers remain outside inspection ([RT-OBJ-wiki-pages](runtime.md#rt-obj-wiki-pages); SRC-1, `skills/update/SKILL.md`).

### 2. Load writing guidance and identify affected pages

The agent obtains the guide and Home through `listPages` and `readCollabDoc`. If no guide exists, `update` directs it to the shipped guide reference and offers setup. The selected existing-guide branch needs no setup workflow. The guide is a retained instruction surface for later writing, not merely background facts ([RT-BAP-guide-writing](runtime.md#rt-bap-guide-writing)). Its precedence is natural-language policy, with no inspected enforcement.

Next the agent supplies changed files to `pagesForFiles`. With uncommitted work it can omit arguments to inspect the working tree; for committed work it passes files or `since` with the preceding commit. The external tool identifies candidate covering pages, while the foreground agent reads them and judges whether the code change affects their meaning. An unaffected page is skipped. An affected page is revised, or marked `outdated` with a line identifying what changed and where if the agent cannot explain the new meaning well. A `stale` result is not proof this session caused all divergence: capture explicitly warns that older commits may be involved (SRC-1, `skills/capture/SKILL.md`).

This handoff separates discovery from semantic judgment. The tool supplies coverage candidates; it does not certify that the prose is current. The agent's inability to explain a change has an explicit degraded output—an outdated page—rather than a requirement to invent missing history. Its actual ability to make that judgment is not established by the instruction.

### 3. Select and attribute content before writing

The agent selects decisions, reasons, alternatives, answered or open questions and context useful to a teammate. It drops routine progress and information already evident in code or Git history. If no candidate survives and no page required maintenance, the terminal answer is “nothing to record” ([RT-RTE-session-capture](runtime.md#rt-rte-session-capture); SRC-1, `skills/capture/SKILL.md`).

For remaining candidates it searches/reads existing pages and extends the page that owns the subject, creating a page only if none fits. Local `listMarks` is an additional duplicate check before recording a possibly existing decision. `searchPages` is prescribed before page creation. These are model-directed checks over tool output, not an inspected uniqueness constraint (SRC-1, `skills/capture/SKILL.md`, `skills/update/SKILL.md`).

> **Decisions already recorded.** `listMarks` lists the decided and open marks across the wiki, filtered by `query` words, `kind` or `by`. Check it before writing a decision that may already be on a page, and extend that page rather than recording it twice.
> --- `skills/update/SKILL.md`

Identity for the local terminal user comes from Git name/email. `list_session_inputs` can supply ready-made citation markdown, which must be copied unchanged and attached only when the person's words support the sentence. Missing session citations do not reject the whole capture: prose attribution is permitted, and a decision can be marked without a quote. The supplied baseline distinguishes citation availability from the external reader's claimed transcript isolation ([RT-CLM-session-isolation](runtime.md#rt-clm-session-isolation); SRC-1, `skills/update/SKILL.md`). Thus the tool output supports attribution, not an answer oracle certifying that a decision or its rationale is true.

### 4. Admit edits and handle rejection

Before writing, the agent identifies the local folder to the user. This notice is a chance to detect a wrong destination, not a required approval response. The agent proposes and submits ordinary additions directly. People supply the session's decisions, but the agent chooses their wording and placement; starting capture is not per-content human approval. Deleting or rewriting another person's text requires asking. `update` requests small edits, marked decision sentences rather than duplicate decision boxes, and local relative links carrying IDs from looked-up pages ([RT-RTE-session-capture](runtime.md#rt-rte-session-capture); SRC-1, `skills/update/SKILL.md`).

The foreground agent delegates persistence to local tools. For typed pages, `tracker_update` with `description` replaces the whole body and requires a preceding `tracker_get`; this is not the team branch's restricted replacement behavior. Ordinary files can also be edited by people or other tools. The local protocol requires reading before editing and describes stale-version refusal:

> Pages are ordinary files: a person may edit them in any editor or commit them. Read before every edit; a write with a stale `expectedVersion` is refused, so re-read and apply your change again.
> --- `skills/update/SKILL.md`

This supplies a concrete rejection and recovery path: a stale write must not be treated as delivered; the agent rereads and reapplies its intended change to current content. It is a changed-input retry, not blind repetition. The server is the claimed rejection owner; the agent owns recovery and content reconciliation. Without the implementation or a trace, no conclusion follows about actual atomicity, conflict detection or preservation under concurrent edits.

Destination/access errors have a different recovery rule:

> If a tool returns an error, do not retry the same call. Tell the user in plain words, then carry on with the task without writing:
> --- `skills/connect/SKILL.md`

The following error-specific instructions can require status resolution, a user choice or a replacement tool. They do not authorize repeated identical writes. No general transaction or autonomous workflow supervisor is shipped here. Local deletion is described as recoverable through `.trash/`, but that is not a demonstrated rollback for a sequence of page edits (SRC-1, `skills/update/SKILL.md`, `skills/connect/SKILL.md`).

### 5. Verification and delivery

Verification is conditional and distributed across the procedure, rather than a separate reviewer agent. Read-before-write, duplicate checks and changed-file coverage constrain proposals before submission. For maps or pages of links, the agent must check every wiki target against `listPages`; if a browser tool is available, it also opens the page and clicks two boxes. These checks are not required for every plain prose capture. After a large rework, or before claiming the wiki is tidy, `wikiDoctor` is required. Its findings return to the same agent for repair:

> **Checking the wiki.** After a large rework, and before saying the wiki is tidy, call `wikiDoctor`. It changes nothing; fix what it reports with the tools above: scan `issues` such as broken links, `orphans` to link from the page they belong under or from Home, `stale` pages to update or mark `outdated`, `duplicateTitles` to merge into one page, and `deadPaths` (a `current` page whose `paths` match no file) to correct or mark `outdated`.
> --- `skills/update/SKILL.md`

`wikiDoctor` is a declared diagnostic interface, not an inspected implementation or an independent semantic answer oracle. Its non-mutating contract leaves repair to the agent; no successful check, repair loop or correctness of captured decisions was observed. There is no basis to promote the prompt's requested checks into guaranteed acceptance gates.

The prescribed delivery is the final reply ending with links to updated or outdated pages, one per line. An outdated page is explicitly a possible delivered result; capture does not require every page to become current. The alternative “nothing to record” ends without a new page. Neither a final link nor a write tool's returned title/link establishes successful persistence, fidelity or later behavioral benefit without execution evidence (SRC-1, `skills/capture/SKILL.md`, `skills/update/SKILL.md`).

Later recall is a separate consumer, not a mandatory final capture stage. It can retrieve the retained decisions and surrounding reasoning before answering or changing code ([RT-RTE-wiki-recall](runtime.md#rt-rte-wiki-recall)). The capture workflow establishes the intended producer-to-reader path, not that a later session exercised it or improved its work. There is no prescribed separate sub-agent context or compacted return value here: selected pages and session inputs reach the foreground model, while persistence calls carry the edits; host context retention and compaction remain uninspected.

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

#### On [RT-RTE-session-capture](runtime.md#rt-rte-session-capture)

Workflow-specific verification: local coverage review and duplicate lookup precede edits; link checks apply to maps/pages of links; `wikiDoctor` applies after large rework or before a tidy claim. The foreground agent owns repairs, with no separate reviewer prescribed.

Workflow-specific recovery: stale-version rejection returns control to the foreground agent for reread and reapplication; destination errors follow the non-repetition and resolution procedure. These remain prescribed paths, not observed recoveries.

Workflow-specific delivery: a final linked list may include pages marked outdated rather than fully revised. The empty-result branch terminates with “nothing to record”. Later recall is a separate invocation, not a condition for completing capture.
