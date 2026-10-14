---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Sentry Skills PR iteration workflow: feedback and CI repair, local verification, push, monitoring and bounded delivery."
run-id: AAS-2026-10-14-skills-2719567f917c-01
reviewed-boundary: d18b7aa8ba878354e5c348310230e652f7690f9c
---

# Sentry Skills workflow report

## Workflow account

### Selection and evidence boundary

The representative workflow is `iterate-pr`, selected because its shipped instructions connect a user request, external feedback, model-directed repair, verification, remote publication and a fresh feedback loop. It also states explicit failure and stop paths. This is the route already declared as [RT-RTE-pr-iteration](runtime.md#rt-rte-pr-iteration), not a new orchestration mechanism. The [boundary](boundary.md) identifies Sentry Skills as a host-consumed extension with a partial operational loop: the package supplies instructions and Python helpers; an external host owns model calls, tool execution and permissions.

This account independently inspected the complete `skills/iterate-pr/SKILL.md` and all four `skills/iterate-pr/scripts/*.py` files at the frozen revision. SRC-1, `skills/iterate-pr/SKILL.md`, `skills/iterate-pr/scripts/fetch_pr_checks.py`, `skills/iterate-pr/scripts/fetch_pr_feedback.py`, `skills/iterate-pr/scripts/monitor_pr_checks.py`, `skills/iterate-pr/scripts/reply_to_thread.py`. These are doctrine/design and implementation evidence, not execution traces. The reply helper adds coverage beyond the runtime baseline; no target code or service was executed. Actual host selection, compliant repairs and successful delivery remain unobserved.

### Request and initial handoff

A request to fix PR CI or review feedback is interpreted by the host, which loads the skill instructions for the foreground model. [RT-OBJ-skill-md](runtime.md#rt-obj-skill-md) and [RT-BAP-skill-consumption](runtime.md#rt-bap-skill-consumption) distinguish model-consumed instructions from host-parsed metadata. Automatic activation is declared, not implemented by this package. The workflow requires authenticated `gh`, `uv`, and the target repository root as cwd. Its first command identifies the PR number, URL, head branch, draft status and review decision. The supplied commands use skill-root-relative script paths; resolving those while keeping target-repository cwd is an external host responsibility. SRC-1, `skills/iterate-pr/SKILL.md`.

No model-worker delegation is required. The foreground model requests deterministic helper work and retains ownership of repair decisions. PR identity and current service results pass to helpers; their JSON returns to the foreground agent. The optional background monitor is a separate polling program, not a code-repair agent. Host isolation, notification delivery and context removal are not established by the package.

### Feedback admission and diagnosis

The feedback fetcher obtains repository/PR identity, overall reviews, inline review threads and general conversation comments. Its output groups issues into high, medium, low, informational-bot and resolved buckets. Explicit priority markers precede content regexes; otherwise substantive non-informational comments default to medium. Actionable review bots are categorized by content rather than silently discarded. The foreground model is instructed to fix high/medium items, ask the user which low items to address, skip resolved/informational items, and distinguish real bot findings from false positives. Human low-priority choice is a scoped decision, not approval of every code change. SRC-1, `skills/iterate-pr/scripts/fetch_pr_feedback.py`, `skills/iterate-pr/SKILL.md`.

The agent does not receive an exhaustive review transcript. GraphQL requests the first 100 threads and first 10 comments per thread; processing uses only the first comment. Self-comments and bodies shorter than three stripped characters are omitted. A short summary and the selected comment's full body are both returned. `isOutdated` is retained as metadata, not a filter. Service errors can become empty lists. Thus a clean high/medium bucket is evidence about selected, successfully fetched content, not proof that every criticism was resolved. SRC-1, `skills/iterate-pr/scripts/fetch_pr_feedback.py`. These transformation limits qualify the runtime route rather than contradict its prescribed success condition.

The CI fetcher similarly returns check classifications and bounded log snippets. It searches ten recent branch workflow runs and matches failed runs by workflow name, without enforcing current-head SHA equality. The workflow consequently requires full failed-log inspection before editing, rather than treating the helper snippet as sufficient diagnosis. The model must state the cause, inspect related call sites, fix the root cause and add focused tests when needed. SRC-1, `skills/iterate-pr/scripts/fetch_pr_checks.py`, `skills/iterate-pr/SKILL.md`.

> 1. read full log: `gh run view <run-id> --log-failed`
> 2. trace from assertion/exception/lint rule to source
> 3. state the cause before editing: "fails because X, affected by Y"
> --- `skills/iterate-pr/SKILL.md`

### Verification, publication and return to monitoring

The foreground agent proposes and executes edits through the host. Tests/checkers provide bounded reference outcomes; reviewer comments supply criticism, not a complete correct-answer oracle. Before committing, the agent must rerun the specific test, affected checker or covering tests, depending on the fix. A local failure rejects progression to push under the instruction policy. Recovery belongs to the foreground agent, which fixes the local failure; no code wrapper enforces that gate. [RT-RTE-pr-iteration](runtime.md#rt-rte-pr-iteration) retains the policy and operation statuses. SRC-1, `skills/iterate-pr/SKILL.md`.

> - local failure: fix before pushing
> --- `skills/iterate-pr/SKILL.md`

After verification, the agent stages files, commits and pushes. The changed branch and GitHub results become state for the next cycle. There is no mandatory per-fix human approval or automatic rollback transaction in the inspected instructions. Host permissions and GitHub acceptance remain external. The loop checks CI, polls feedback while actionable checks are pending, immediately handles new high/medium feedback, and restarts after any verified push. The skill explicitly prescribes restarting an optional monitor after every push. SRC-1, `skills/iterate-pr/SKILL.md`.

The monitor receives a PR number or resolves the current branch PR, snapshots PR metadata initially, then repeatedly fetches checks. Pending non-human checks delay termination even when failures already exist. Once none remain, failure precedes a human-gate blocked result; otherwise it emits `ALL_CHECKS_PASSED`. Its summary includes at most 20 checks. Terminal failure, blocked and no-check classifications also exit zero, so the caller must interpret markers, not treat process success as workflow success. The marker means no received `pending` or `fail` bucket, not necessarily all checks explicitly passed. [RT-RTE-check-monitor](runtime.md#rt-rte-check-monitor) supplies the canonical mechanism and supporting source passage. SRC-1, `skills/iterate-pr/scripts/monitor_pr_checks.py`.

### Failure, escalation and delivered result

Three rejection/recovery paths are source-supported:

- **Local verification rejects the proposed publication.** The foreground agent fixes before pushing; successful recovery is not observed.
- **Repeated failure or ambiguous diagnosis escalates.** The same failure after two attempts, unclear feedback or an infrastructure issue requires asking the user. The package does not implement an attempt counter or the user's ensuing decision.
- **Checks cannot reach the intended actionable terminal state.** No PR, required rebase, no registered checks after the grace period, draft/no-checks or remaining human gates produce a stop/report rather than a readiness mutation or indefinite wait. The monitor's transient fetch-error path retries without a total retry limit; that implemented retry is not the same as escalation from a diagnosed infrastructure issue. SRC-1, `skills/iterate-pr/SKILL.md`, `skills/iterate-pr/scripts/monitor_pr_checks.py`.

> | Success | actionable CI passed; post-CI feedback clean; low-priority choice handled |
> | Ask user | same failure after 2 attempts; feedback unclear; infrastructure issue |
> | Stop | no PR; branch needs rebase; no checks; draft no-checks; only human gates remain |
> --- `skills/iterate-pr/SKILL.md`

If scripts fail, the agent may use direct `gh` commands. This bypasses helper normalization, so the model must interpret raw output; helper classifications are not mandatory enforcement points. The check fetcher can mask errors as an empty list, while the monitor distinguishes a failed fetch from a valid empty check list. A caller cannot infer complete observation merely from an empty result. SRC-1, `skills/iterate-pr/SKILL.md`, `skills/iterate-pr/scripts/fetch_pr_checks.py`, `skills/iterate-pr/scripts/monitor_pr_checks.py`; the fallback passage is retained in [RT-RTE-pr-iteration](runtime.md#rt-rte-pr-iteration).

Delivery consists of the pushed repair plus the foreground agent's terminal success, stop or ask-user report. For success, the skill requires waiting ten seconds after actionable checks pass and fetching feedback again; fresh high/medium items reopen repair. It also requires handling the user's low-priority choice. Therefore the monitor marker alone does not deliver the full workflow result. The instructions explicitly exclude waiting for human approval, draft readiness and merge readiness; successful iteration does not mean mergeable or approved. SRC-1, `skills/iterate-pr/SKILL.md`. The reply helper can publish explanations to review threads, but the router does not require every thread to receive a reply or to be marked resolved. That optional communication path is recorded separately below.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

#### WF-RTE-thread-replies
Label: Optional review thread replies
Part of: [RT-RTE-pr-iteration](runtime.md#rt-rte-pr-iteration)

This is the bundled communication subroute, not a replacement for PR repair or the monitor. Foreground agent supplies alternating thread IDs and reply bodies → Python normalizes escaped newlines and constructs aliased GraphQL mutations → external `gh`/GitHub processes replies → helper returns per-operation and grouped thread statuses. The reply text is natural-language content; JSON serialization, GraphQL construction and status classification are symbolic transformations. SRC-1, `skills/iterate-pr/scripts/reply_to_thread.py`, `skills/iterate-pr/SKILL.md`.

- Immediate return: JSON replied/failed counts, ordered operations and grouped thread statuses; any failed operation causes exit one.
- Later read-back: published comments can be fetched by later feedback invocations, but the fetcher omits PR-author comments and processes only the first inline thread comment, so successful publication does not establish later delivery to that agent.
- Delegated visibility: helper receives supplied thread IDs and bodies, not repair context or proof that a fix was verified.
- Selection predicate: caller chooses thread/body pairs; no automatic thread selection or mandatory reply step is specified.
- Invalidation or expiry: inapplicable — no reply expiry or installed-content lifecycle is specified.
- Activation or effect: implemented request for remote review-thread replies through one GraphQL mutation; actual service mutation is unobserved.
- Evidence limits: external authorization and service behavior are uncaptured; helper-reported success is not observed execution or proof of accurate reply content.
- implementation conclusion status: wired
- operation conclusion status: uninspected

The foreground model proposes the explanatory text; GitHub accepts or rejects the mutation under external authorization. This is optional communication within an open repair request, not a bounded experiment or answer-oracle comparison. No per-reply human admission gate is prescribed. Successful replies persist at GitHub if accepted. The helper supplies no rollback or automatic retry: nonzero CLI result, invalid JSON or timeout marks all pairs failed; a parsed response identifies per-alias failures without treating the batch as atomic. Recovery selection belongs to the caller. A retry's duplicate-post behavior is not established. SRC-1, `skills/iterate-pr/scripts/reply_to_thread.py`.

> if alias in error_paths or data.get(alias) is None:
>     operation_results.append((tid, False))
> else:
>     operation_results.append((tid, True))
> --- `skills/iterate-pr/scripts/reply_to_thread.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-pr-iteration](runtime.md#rt-rte-pr-iteration)

Workflow handoff: helper outputs inform foreground diagnosis; local checker outcomes condition the prescribed push; subsequent service results reopen the cycle. No required model-worker handoff exists in this selected workflow. User authority is scoped to low-priority selection and escalation, not a mandatory approval of each edit. Delivery requires the post-CI feedback check and handled low-priority choice, not just a pushed commit or monitor marker. Verification and stopping are instruction policies whose compliant execution remains unobserved.

#### On [RT-RTE-check-monitor](runtime.md#rt-rte-check-monitor)

Workflow return handling: the foreground agent must distinguish a zero-exit failure/blocked/no-check marker from a success marker and still perform the skill's post-CI feedback check. Optional MonitorTool use does not transfer code-repair ownership. Restart after each push is the source-prescribed handoff for a new repair cycle; actual host timeout, notifications and isolated context lifecycle remain uninspected.
