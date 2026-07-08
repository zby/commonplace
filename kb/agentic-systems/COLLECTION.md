---
type: kb/types/collection.md
description: "Authoring contract for kb/agentic-systems/ — descriptive register: analyses of external agentic systems and harnesses as whole systems"
---

# Writing conventions for kb/agentic-systems/

## Register

This collection operates in the **descriptive [register](../notes/definitions/register.md)**. It covers external **agentic systems and harnesses as whole systems** — execution loops, orchestration APIs, sub-agent surfaces, scheduling, permissioning, control — what each is built from and does.

The quality goal is **fidelity + economy**: faithful to what the system actually does, in minimum tokens. An analysis that misrepresents the analysed system is worse than none.

Memory and knowledge subsystems are carved out: they have their own collection, `kb/agent-memory-systems/`, with a full review methodology that runs largely automatically. This collection covers everything else about how agentic systems are built. If a memory-subsystem category here ever matures into its own methodology, it should follow the same path and split out.

## Structure

The collection root holds per-system and per-feature analyses plus navigation. No subdirectory structure yet — add one when a category accumulates enough artifacts to need its own conventions.

## Evidence basis

Open each analysis with a one-line **evidence basis**: what it is grounded in — docs, source code, papers, or first-hand operation of the system — and when that evidence was captured. There is no formal `source-tier` field yet; adopt one if the collection grows a comparison methodology.

## Title conventions

- **Descriptive coverage of one system or feature** — name the system (`claude-code-dynamic-workflows.md`).
- **Argumentative analyses** — analyses asserting a specific claim — use a claim-shaped title and the `title-as-claim` trait, following `kb/notes/COLLECTION.md` conventions.

## Outbound linking conventions

Organised per destination; label semantics in [link-vocabulary.md](../reference/link-vocabulary.md).

- **→ `kb/sources/`** — link the snapshots an analysis is grounded in. Labels: `derived-from`, `evidence`, `see-also`.
- **→ `kb/notes/`** — search when an analysis maps a system onto theory. Links usually run inverse (theory links in via `evidence`), so promote a novel transferable claim to `kb/notes/` rather than author theory here. Labels: `rationale`, `see-also`.
- **→ `kb/agent-memory-systems/`** — when the analysed whole system has a memory, knowledge, or context-engineering subsystem reviewed there. Use `contains` from the whole-system analysis to the subsystem review; use `part-of` only from a subsystem-focused analysis back to the whole system. Labels: `part-of` / `contains`, `compares-with`, `see-also`.
- **→ `kb/reference/`** — scan when a design element has a direct Commonplace analogue. Labels: `see-also`.
- **→ `kb/instructions/`** — link a Commonplace procedure when the external system analysis directly maps onto an operating rule or workflow. Labels: `procedure`, `see-also`.

## Types

- `note` -> `kb/types/note.md`
  Use for system and feature analyses, and for cross-system comparisons.
- `index` -> `kb/types/index.md`
  Build-time generated directory listings only (ADR 026); the committed `README.md` navigation hub carries no frontmatter.

## What does NOT belong here

- Memory, knowledge, and context-engineering subsystem reviews → `kb/agent-memory-systems/`
- Transferable claims about KB methodology or orchestration theory → `kb/notes/`
- Raw snapshots of external sources → `kb/sources/`
- Descriptions of the Commonplace system itself → `kb/reference/`
- Procedures and how-to guidance → `kb/instructions/`
- Work in progress → `kb/work/`
