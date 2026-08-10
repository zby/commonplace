# Data Summit Warsaw talk

Workshop for preparing a 35-minute practitioner talk for Data Summit Warsaw: a concrete case study of Commonplace as an LLM-operated knowledge base, built around one core claim and four engineering lessons, with the deeper KB theory used only where it explains a design decision.

Core claim of the talk:

> LLMs make it cheap to continuously develop a knowledge base, not merely search or summarize it. But because fluent generation can turn weak thinking into convincing artifacts, the useful system is a hybrid: LLMs do semantic work, deterministic machinery enforces what can be formalized, and context is carefully budgeted so the knowledge system does not displace the task it is supposed to help.

The talk should leave the audience thinking "I can apply these patterns to my own LLM knowledge system next week", while the theory stays in the KB for those who follow the rabbit hole. It is deliberately **not** a tour of Commonplace's vocabulary — the material-selection table in [outline.md](./outline.md) records what is included, compressed, or cut, so later sessions don't re-litigate those cuts.

## State

- [outline.md](./outline.md) — the working 35-minute outline, the four practitioner lessons, the material triage against the KB, the visual spine, and the deliberate exclusions. Imported from the planning session that scanned the KB.

## What would close this workshop

The talk is delivered (or the submission is withdrawn). On closing: extract anything durable — most likely the "write rich; read selectively" formulation and any slide-tested framings that turn out stronger than their KB counterparts — into `kb/notes/` or `kb/articles/`, then delete the workshop.

## Boundaries

- Slides and speaker notes are the deliverable; they may live here while in flight.
- Presentation-level syntheses (e.g. "write rich; read selectively") are allowed to be looser than library claims — they are not KB theorems until promoted through normal review.
- Timing target for authored material is ~31–32 minutes; concrete examples run long.
