---
description: "When one agent in an orchestration reads untrusted content, the defense is a role-level privilege quarantine — barring that agent from high-privilege actions entirely — not finer per-call tool scoping"
type: kb/types/note.md
traits: [title-as-claim, has-external-sources]
tags: [computational-model, tool-loop]
status: seedling
---

# Agent orchestration needs a privilege quarantine, not just a permission scope

When an orchestrated agent's context includes untrusted, attacker-reachable content — a public web page, an incoming support ticket, an unvetted uploaded file — no amount of finer-grained per-call tool permission closes the risk that the agent takes a high-privilege action on the strength of an instruction smuggled inside that content. The reason is architectural, not a matter of tuning the permission list: a single call already carries enough authority to do damage once its action is steered by injected content, so scoping *which tools a call may use* cannot fix a problem located in *which content is allowed to steer a call that has privileged tools at all*. The defense that actually closes this is a **privilege quarantine**: split the work into a reader (or classifier) role that consumes the untrusted content and is never granted a high-privilege action, and a separate actor role that performs privileged operations only on structured, already-vetted output the reader produced — never on the raw untrusted content directly.

## Why per-call scoping doesn't reach this

[Compiling a coordination strategy preserves primitive authority but expands aggregate authority](./compiling-coordination-preserves-primitive-not-aggregate-authority.md) shows that a delegated channel's permission model is almost always enforced per call, and a per-call gate does nothing to bound what the calls add up to. Quarantine is the same gap read one level down: a per-call permission check authorizes an *action*, not the *provenance of the content that chose it*. An agent can be fully within its allowed tool scope and still be a confused deputy — executing an attacker's instruction using its own legitimate authority, because nothing in the per-call check asks where the instruction that shaped this call came from. Quarantine closes that gap upstream of any single call, by denying the untrusted-content role the privileged capability altogether, rather than trying to filter or detect bad instructions after they have already reached a call that could act on them.

## Two independent instances

- The dynamic-workflows [triage pattern](../sources/a-harness-for-every-task-dynamic-workflows.md) bars agents that read untrusted public content (a support queue, an incident channel) from taking high-privilege actions; those actions are delegated to separate agents that act on the triage agent's output rather than the raw content.
- [GBrain](../agentic-systems/gbrain.md)'s operations layer independently reaches the same split: every operation declares a scope (`read`/`write`/`admin`), and remote (agent-facing) callers — including the host agent GBrain otherwise instructs carefully at the prose level — are classified untrusted at the API boundary regardless of what the skill prose tells them to do, losing auto-linking on writes and access to protected job types. The system's own framing is exact: prose-level trust and code-level trust are managed separately.

Neither system cites the other. The convergence is on the role-level split itself — deny the content-exposed role the privileged capability, independent of what the untrusted content says — not on any shared implementation.

## Relation to the general security-risk question

[The four-field record exposes an efficiency, security, and sovereignty risk triad](./the-four-field-record-exposes-an-efficiency-security-and-sovereignty.md) frames security risk as a standing question: does anything untrusted, or anything stale, reach a high-authority channel? Quarantine is the architectural answer available whenever you can identify *in advance* which role in an orchestration will be exposed to untrusted content: preemptively deny that role the high-authority channel, rather than detecting or sanitizing an injected instruction after it has already reached a call that could act on it. This is the orchestration-specific case of the general security-engineering principle of privilege separation (compartmentalizing a system so that the component exposed to untrusted input cannot itself exercise the system's most damaging capabilities) — the pattern predates LLM agents and applies wherever a component processes attacker-reachable input.

## Scope limit

Quarantine moves the trust boundary from the tool call to the agent role, but it does not eliminate risk from the pipeline — it relocates where the risk concentrates. The actor role still trusts the reader's structured output completely; if the reader can be manipulated into emitting a malicious-but-well-formed extraction (correct schema, poisoned field values), the actor will act on it exactly as designed. A schema on the reader's output constrains its shape, not its truthfulness. Quarantine is a defense against the reader taking privileged action directly, not a defense against a compromised reader deceiving a trusting actor — that residual risk needs its own oracle (e.g. the actor or a third agent checking the reader's extraction against the source before acting), not a repetition of the same split.

## Open Questions

- How much independent verification should the actor apply to the reader's output before it is treated as "already vetted"? Zero verification collapses quarantine to a relabeling of trust rather than a reduction of it; full re-verification duplicates the reader's work. No source examined here specifies where this line should sit.
- Both witnessed instances are first-party accounts (a practitioner report and one source-inspected system) with no adversarial red-team measurement of how much the split actually reduces successful injection. Treat the pattern's existence as established by convergent design, its effectiveness as untested.

---

Relevant Notes:

- [A harness for every task — dynamic workflows](../sources/a-harness-for-every-task-dynamic-workflows.md) — derived-from: the triage use case's quarantine description is the pattern's first witnessed instance
- [GBrain](../agentic-systems/gbrain.md) — evidence: independently reaches the same read/act privilege split, with the host agent itself classified untrusted at the API boundary
- [Compiling a coordination strategy preserves primitive authority but expands aggregate authority](./compiling-coordination-preserves-primitive-not-aggregate-authority.md) — grounds: per-call permission scoping cannot bound aggregate risk, which is why the boundary has to move to the agent-role level instead
- [The four-field record exposes an efficiency, security, and sovereignty risk triad](./the-four-field-record-exposes-an-efficiency-security-and-sovereignty.md) — extends: quarantine is one architectural answer to that record's standing security-risk question, available when the untrusted-exposed role is known in advance
- [Agent orchestration needs coordination guarantees, not just coordination channels](./agent-orchestration-needs-coordination-guarantees-not-just.md) — see-also: a sibling case of the same form — naming the guarantee a channel needs, not just the channel itself
- [Claude Code dynamic workflows](../agentic-systems/claude-code-dynamic-workflows.md) — see-also: the shipped-system analysis of the same harness this pattern's first instance comes from
