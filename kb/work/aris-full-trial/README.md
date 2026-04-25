# Workshop: Full ARIS Trial

## Question

Can we run ARIS as a full paper-production workflow inside commonplace without exposing premature drafts, and what kind of paper should the trial attempt?

## Privacy Boundary

The public workshop records framing, candidate topics, decisions, and lessons learned. The ARIS project roots live under:

```text
kb/work/aris-full-trial/private/
```

That directory is gitignored. It may contain `research-wiki/`, `idea-stage/`, `refine-logs/`, `review-stage/`, `paper/`, `figures/`, `MANIFEST.md`, `.aris/`, traces, and paper drafts.

## Trial Project Roots

Two parallel ARIS project roots are available:

```text
kb/work/aris-full-trial/private/bounded-context-paper/
kb/work/aris-full-trial/private/agent-memory-review-paper/
```

Both can use ARIS's normal root-relative layout without polluting the main repo root.

## Candidate Directions

See [paper-candidates.md](./paper-candidates.md).

## Current Lean

The agent-memory review paper is probably the better first full-ARIS trial:

- It uses already accumulated review material.
- It is less sensitive than the bounded-context orchestration model.
- It naturally fits a survey / systematization-of-knowledge paper type.
- ARIS Research Wiki's papers/ideas/claims structure should help organize many practical systems.

The bounded-context paper remains valuable, but should stay private until the argument is more mature.

## Closure

This workshop closes when we either:

1. Complete a full ARIS paper trial and extract lessons about using ARIS inside commonplace.
2. Decide ARIS is too paper-specific for our workflows and retain only selected mechanisms.
3. Promote a publication plan into a separate paper workshop with a clear privacy/publication policy.
