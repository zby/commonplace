# Proposal: make promoted skill commands channel-portable

## Problem

`AGENTS.md` declares native Windows source-checkout support and provides `.venv\Scripts\...` fallbacks, but multiple promoted skills contain unqualified Bash-only examples such as pipelines to `wc`, command substitution, or POSIX virtual-environment paths. Promoted skills are copied into user-visible execution surfaces, so a selected procedure can fail on a supported channel before its substantive behavior runs.

This is not merely documentation style. In the cluster's terms, the consumer exists and the instruction has force, but the channel is unavailable in part of the declared frame; the intended behavior is therefore non-operative there.

## Proposed change

1. Establish one promoted-skill command convention: use cross-platform console entry points where possible; otherwise provide paired POSIX and PowerShell snippets.
2. Audit all promoted `SKILL.md` files and their bundled references against that convention.
3. Add a deterministic health check for known channel-specific idioms when an equivalent portable entry point exists. The check should report, not guess at semantic equivalence.
4. Add Windows and POSIX smoke coverage for commands that the scaffold advertises.

## Acceptance criteria

- Every executable snippet in a promoted skill either works unchanged in both declared channels or labels and pairs its channel-specific form.
- `cp-skill-health-check` identifies unlabelled known-incompatible snippets without claiming to prove general shell portability.
- Scaffold/init tests exercise the copied skill set on both path conventions.

## Scope boundary

This proposal covers promoted skills and their bundled references, not every historical command example in the knowledge base. It does not require translating shell languages mechanically; ambiguous cases remain human-reviewed.

---

Links:

- [Phase-1 authority audit](./audit/authority-and-authoring.md) — motivates: consumer/channel mismatch
- [Workshop framing](./README.md) — owns: disposition and later sequencing
