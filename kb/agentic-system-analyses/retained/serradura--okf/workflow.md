---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "OKF workflow account: task-context consumption, discovery-triggered maintenance and checked knowledge delivery."
run-id: AAS-2026-11-08-okf-8bc42addf404-01
reviewed-boundary: "cfb7ffac7fef37d56e97b5b7dd8fe97ffc648c7c"
---

# OKF workflow report

## Workflow account

### Selection and evidence

The representative workflow is **use project knowledge for a task, then record a durable discovery and close out the maintenance pass**. It is selected because the consume playbook explicitly hands discoveries to maintain; these are connected steps, not a workflow assembled from unrelated APIs. The enclosing route is [RT-RTE-skill-work](runtime.md#rt-rte-skill-work). The user supplies the task, an external agent owns semantic decisions and the final answer, and the CLI supplies mechanical observations. This is procedural delegation to commands and playbooks, not evidenced delegation to another model worker.

All source evidence is SRC-1 at the frozen revision. The playbooks establish requested agent behavior, not successful execution. Additional inspection for this member covered `skills/okf/SKILL.md`, `skills/okf/playbooks/consume.md`, `skills/okf/playbooks/maintain.md`, `skills/okf/playbooks/curate.md`, the Closeout section of `skills/okf/reference/authoring.md`, `gems/okf/lib/okf/cli/validate.rb` and the call/exit-policy portion of `gems/okf/lib/okf/cli/lint.rb`. Markdown supplies doctrine/design evidence; the two Ruby command paths supply implementation evidence. No target code was executed, and no supplied session trace establishes completion, semantic accuracy or benefit.

### Request to selected context

The skill routes a task in a repository already carrying a bundle to consume. An explicit target may be a directory or registry reference; genuinely ambiguous intent calls for asking the user rather than silently selecting work (SRC-1, `skills/okf/SKILL.md`). The consume procedure first requests directory shape, then a relevant branch index and recent log history. Only then does the agent follow links into concepts the task needs. A pointed question transfers to search; a large bundle can use a minimal graph to plan traversal (SRC-1, `skills/okf/playbooks/consume.md`; [RT-RTE-skill-work](runtime.md#rt-rte-skill-work)).

The handoff to the CLI supplies a bundle identity and a narrow query or branch. Its return is structural data, not a proposed task answer. The external agent chooses and reads concept bodies, interprets them and carries out the user's task. This keeps irrelevant bodies out of the initial model input by requested selection; it does not establish a separately isolated task frame, compaction or removal of material already delivered. Host context sharing remains uninspected. The retained skill instructions have requested rather than enforced force at the agent consumer ([RT-BAP-skill-guidance](runtime.md#rt-bap-skill-guidance)).

### Discovery to revised knowledge

The workflow's consequential handoff is an agent judgment that something learned during work is durable enough to record. The consume instruction explicitly identifies missing facts, missing links and concepts that no longer match reality as triggers (SRC-1, `skills/okf/playbooks/consume.md`; passage retained in [RT-RTE-skill-work](runtime.md#rt-rte-skill-work)). It transfers responsibility to maintain without transferring to a new executor. The selected bundle, project change or discovery, and relevant concepts become the maintenance context.

Maintain asks the same agent to reorient through directory/index/log views and statistics, then find affected concepts through search and graph edges. The request to find every affected concept is not an executable completeness guarantee. The agent updates bodies, generation attribution and cross-links; creates concepts for new assets; and leaves deprecation context for retired assets. It must also update enumerations and append a durable dated log entry. These obligations are in SRC-1, `skills/okf/playbooks/maintain.md`:

> 3. Update bodies and `generated.at` (and `generated.by` — who is making this
>    change, in §7's spelling); fix or add cross-links; create new concepts for
>    new assets; mark retired assets with a `**Deprecation**` note rather than
>    silently deleting the context that explains them.
> --- `skills/okf/playbooks/maintain.md`

The proposer and semantic decider here are the external agent. The general maintain procedure does not impose per-content human approval. Ordinary host file edits persist the candidate before subsequent checks; they are not equivalent to the library's validated temporary-tree publication ([RT-RTE-publish-bundle](runtime.md#rt-rte-publish-bundle)). Installed Pro guards are a separate operating profile, not a prerequisite silently assumed for this workflow ([RT-RTE-pro-gates](runtime.md#rt-rte-pro-gates)).

### Verification, rejection and recovery

[WF-RTE-maintenance-closeout](#wf-rte-maintenance-closeout) traces the final checking subroute. The agent reruns the index and compares listings against actual changes, then runs validate and lint and reviews loose concepts and tags. The checks have different decision authority: validate can return nonconformance, lint reports structural debt, and the agent decides whether a loose leaf or singleton tag is intentional. Neither structural tool supplies a reference answer for the user's task or determines whether prose is true.

A concrete supported failure path is **the edited bundle fails conformance**. The validate command returns exit 1; it does not undo the file edits. The finishing procedure requires zero conformance errors before calling the task done. Thus recovery belongs to the agent: correct the candidate and rerun checks, not rely on a transaction or autonomous retry. Another supported distinction is a lint finding with a successful default exit: the agent must read the report rather than treat zero as proof of no debt. These are implementation branches plus authored recovery obligations, not observed failures or successful repairs.

When the base plugin is installed, an eligible post-edit event can additionally supply filtered validate/lint findings as host context. This is an advisory return after mutation, not a veto; repair still depends on the agent ([RT-RTE-curation-feedback](runtime.md#rt-rte-curation-feedback)). The selected workflow does not require that plugin, so its feedback cannot substitute for the explicit closeout procedure.

### Delivery boundary

For the original task, the external agent delivers the answer or work product through its host. OKF does not own that terminal-answer admission. For the knowledge side, delivery means revised on-disk concepts plus matching index/log material, with the requested closeout completed. Subsequent bundle readers can load those files ([RT-RTE-skill-work](runtime.md#rt-rte-skill-work)); no automatic downstream notification or proof of later use follows. The closeout is a policy for a compliant agent, not software proof that every task answer is correct or every affected concept was found. Actual completion and later behavioral activation remain unobserved.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

#### WF-RTE-maintenance-closeout
Label: Maintenance closeout checks

Part of: [RT-RTE-skill-work](runtime.md#rt-rte-skill-work)

This is the finishing subroute of the supplied consume/maintain route, not a second identity for that whole route. Endpoints are the agent's edited bundle and its decision to call the maintenance task done. The agent delegates structural checks to CLI commands, interprets their returns, performs semantic loose-file/tag review and corrects remaining problems. Natural-language guidance lives in shipped Markdown; symbolic command code consumes current files and emits reports and exit statuses. Files, not model parameters, carry the admitted changes.

- Immediate return: Index views, validation and lint reports, loose/tag views and command exit statuses to the invoking agent.
- Later read-back: Revised concepts, enumeration text and dated log entries remain available to later bundle loads; no execution evidence establishes actual later consumption.
- Delegated visibility: uninspected — no sub-agent handoff or host context-sharing protocol is specified by this finishing gate.
- Selection predicate: Touched concepts and every affected enumeration; validate checks conformance, lint supplies configured structural findings, and the agent judges loose-file intent and tag meaning.
- Invalidation or expiry: Corrections require new checks over current files; no automatic semantic expiry or scheduled retry is specified by the gate.
- Activation or effect: CLI result/exit paths are wired; the agent's enforcement of the finishing requirements is requested, not observed. Direct edits already persist before checks.
- Evidence limits: The gate cannot establish prose truth, affected-concept completeness, host compliance or actual delivery from source text alone.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission and recovery: the agent proposes and writes content, code determines conformance, and the agent decides whether remaining advisory findings are deliberate or need repair. The gate requests zero conformance errors and cleared cheap lint findings. Its guarantee strength is policy for task completion; validate's exit computation is narrower deterministic machinery. A nonconformant result can reject a claim of completed closeout but cannot prevent or roll back the preceding direct edit. No expected-answer oracle, fixed curriculum or automatic improvement loop is supplied; this is open project work. Guidance is the finishing checklist, and persisted outputs are the edited bundle files and log, not the transient checker reports.

SRC-1, `skills/okf/reference/authoring.md`:

> - **`validate`** — zero §11 errors.
> - **`lint`** — cheap findings cleared; `expired` reports out of the box, and
>   `--stale-after` adds the reader-side age cutoff when you want one.
> --- `skills/okf/reference/authoring.md`

SRC-1, `gems/okf/lib/okf/cli/validate.rb` implements the conformance return:

> result = OKF::Bundle::Folder.load(dir).validate
>         options[:json] ? print_validation_json(dir, result) : print_validation(dir, result)
>         result.valid? ? 0 : 1
> --- `gems/okf/lib/okf/cli/validate.rb`

SRC-1, `gems/okf/lib/okf/cli/lint.rb` distinguishes configured failure from the default advisory return:

> def lint_exit(fail_on, report)
>         case fail_on
>         when :warn then report.warnings.any? ? 1 : 0
>         when :info then report.findings.any? ? 1 : 0
>         else 0
>         end
>       end
> --- `gems/okf/lib/okf/cli/lint.rb`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-skill-work](runtime.md#rt-rte-skill-work)

Workflow selection: consume's explicit discovery-to-maintain transition supplies the representative request-to-write-back chain. Semantic ownership stays with the external agent throughout; command delegation returns evidence rather than another agent's judgment. [WF-RTE-maintenance-closeout](#wf-rte-maintenance-closeout) supplies its finishing subroute. Delivery separates the host's task answer from the bundle's persisted knowledge. A completed command invocation establishes neither completed maintenance nor a correct terminal answer.
