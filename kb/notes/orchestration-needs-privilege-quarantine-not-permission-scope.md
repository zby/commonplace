---
description: "When one agent in an orchestration reads untrusted content, the defense is a role-level privilege quarantine — barring that agent from high-privilege actions entirely — not finer per-call tool scoping"
type: kb/types/note.md
traits: [title-as-claim, has-external-sources]
tags: [computational-model, tool-loop]
---

# Agent orchestration needs a privilege quarantine, not just a permission scope

When an orchestrated agent's context includes untrusted, attacker-reachable content — a public web page, an incoming support ticket, an unvetted uploaded file — no amount of finer-grained per-call tool permission closes the risk that the agent takes a high-privilege action on the strength of an instruction smuggled inside that content. Scoping *which tools a call may use* simply doesn't reach this risk. The defense that closes this **direct** path — the untrusted-content role itself taking the privileged action — is a **privilege quarantine**: split the work into a reader (or classifier) role that consumes the untrusted content and is never granted a high-privilege action, and a separate actor role that performs privileged operations only on structured, already-vetted output the reader produced, never on the raw untrusted content directly. (Quarantine does not close every path; see Scope limit below for the indirect one it leaves open.)

## Why per-call scoping doesn't reach this

A per-call permission check authorizes an *action*, not the *provenance of the content that chose it*. An agent can be fully within its allowed tool scope and still be a confused deputy, executing an attacker's instruction using its own legitimate authority — nothing in a tool-identity-based per-call check asks where the instruction that shaped this call came from. The natural objection is that per-call checks could be made provenance-aware instead: a taint-tracking or capability system that gates a call not on which tool it uses but on whether its arguments trace back to untrusted content, the way an interpreter tracks tainted variables. That works when the steering value is a discrete argument a runtime can label and follow. It does not extend cleanly to an LLM role that both reads the untrusted content and decides the call: the content can steer the call's *judgment* diffusely, without ever appearing as a taggable argument, leaving no variable-level lineage to check. That is why the boundary has to move to the role level instead of trying to make the per-call check itself provenance-aware — [compiling a coordination strategy preserves primitive authority but expands aggregate authority](./compiling-coordination-preserves-primitive-not-aggregate-authority.md) shows the same enforcement gap from a different angle: aggregate call volume rather than single-call provenance.

## Two independent instances

- The dynamic-workflows [triage pattern](../sources/a-harness-for-every-task-dynamic-workflows.md) bars agents that read untrusted public content (a support queue, an incident channel) from taking high-privilege actions; those actions are delegated to separate agents that act on the triage agent's output rather than the raw content.
- [GBrain](../agentic-systems/gbrain.md)'s operations layer independently reaches the same split: every operation declares a scope (`read`/`write`/`admin`), and remote (agent-facing) callers — including the host agent GBrain otherwise instructs carefully at the prose level — are classified untrusted at the API boundary regardless of what the skill prose tells them to do, and lose certain write/admin capabilities as a result. The system's own framing is exact: prose-level trust and code-level trust are managed separately.

Neither system cites the other. The convergence is on the role-level split itself — deny the content-exposed role the privileged capability, independent of what the untrusted content says — not on any shared implementation.

## Relation to the general security-risk question

[The four-field record exposes an efficiency, security, and sovereignty risk triad](./the-four-field-record-exposes-an-efficiency-security-and-sovereignty.md) frames security risk as a standing question: does anything untrusted, or anything stale, reach a high-authority channel? Quarantine is the architectural answer available whenever you can identify *in advance* which role in an orchestration will be exposed to untrusted content. This is the orchestration-specific case of the general security-engineering principle of privilege separation (compartmentalizing a system so that the component exposed to untrusted input cannot itself exercise the system's most damaging capabilities) — the pattern predates LLM agents and applies wherever a component processes attacker-reachable input.

## Scope limit

Quarantine moves the trust boundary from the tool call to the agent role, but it does not eliminate risk from the pipeline — it relocates where the risk concentrates. The actor role still trusts the reader's structured output completely; if the reader can be manipulated into emitting a malicious-but-well-formed extraction (correct schema, poisoned field values), the actor will act on it exactly as designed. A schema on the reader's output constrains its shape, not its truthfulness. Quarantine is a defense against the reader taking privileged action directly, not a defense against a compromised reader deceiving a trusting actor — that residual risk needs its own oracle (e.g. the actor or a third agent checking the reader's extraction against the source before acting), not a repetition of the same split.

## Open Questions

- How much independent verification should the actor apply to the reader's output before it is treated as "already vetted"? Zero verification collapses quarantine to a relabeling of trust rather than a reduction of it; full re-verification duplicates the reader's work. No source examined here specifies where this line should sit.
- Both witnessed instances are first-party accounts (a practitioner report and one source-inspected system) with no adversarial red-team measurement of how much the split actually reduces successful injection. Treat the pattern's existence as established by convergent design, its effectiveness as untested.

---

Relevant Notes:

- [A harness for every task — dynamic workflows](../sources/a-harness-for-every-task-dynamic-workflows.md) — abstracted-from: the triage use case's quarantine description is the pattern's first witnessed instance
- [GBrain](../agentic-systems/gbrain.md) — evidence: independently reaches the same read/act privilege split, with the host agent itself classified untrusted at the API boundary
- [Compiling a coordination strategy preserves primitive authority but expands aggregate authority](./compiling-coordination-preserves-primitive-not-aggregate-authority.md) — see-also: a related but distinct enforcement gap — per-call scoping fails to bound aggregate call volume there, and fails to track diffuse single-call provenance here
- [The four-field record exposes an efficiency, security, and sovereignty risk triad](./the-four-field-record-exposes-an-efficiency-security-and-sovereignty.md) — extends: quarantine is one architectural answer to that record's standing security-risk question, available when the untrusted-exposed role is known in advance
- [Agent orchestration needs coordination guarantees, not just coordination channels](./agent-orchestration-needs-coordination-guarantees-not-just.md) — see-also: a sibling case of the same form — naming the guarantee a channel needs, not just the channel itself
- [Claude Code dynamic workflows](../agentic-systems/claude-code-dynamic-workflows.md) — see-also: the shipped-system analysis of the same harness this pattern's first instance comes from
