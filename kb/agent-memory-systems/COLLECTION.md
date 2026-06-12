# Writing conventions for kb/agent-memory-systems/

## Register

This collection operates in the **descriptive [register](../notes/definitions/register.md)** (one of three content modes — theoretical, descriptive, prescriptive — determining quality goal, title conventions, and linking rules). It documents external agent memory, knowledge, and context-engineering systems — what each is built from and does, grounded in the code. Broad cross-system comparison lives in the root-level analyses.

The quality goal is **fidelity + economy**: faithful to what the code actually does, in minimum tokens. A review that misrepresents the reviewed system is worse than none — it pollutes the landscape.

## Structure

**`reviews/`** — individual system reviews, one file per system, typed as `../types/agent-memory-system-review.md`. The workflow and section rules live in `types/agent-memory-system-review.md`.

**`lightweight/`** — doc-grounded coverage for systems known from papers, READMEs, or articles when no reachable repository has been inspected. These are ordinary `agent-memory-system-review` notes carrying `source-tier: doc-grounded`; they hold the **same comparison elements** as code-grounded reviews (four-field record, read-back direction, borrowable ideas) at a lower evidence tier — claim-level. The tier is about authority, not scope. Flip `source-tier` to `code-grounded` if inspectable source later appears. The review spec's instructions are tier-neutral (evidence-stance, source-metadata, and citation rules cover both); see the `source-tier` field in `types/agent-memory-system-review.md`.

**Collection root** — navigation (index, README), cross-system analyses (comparative reviews, focused comparisons), and any analysis grounded in multiple reviews. When an analysis makes a claim general enough to transfer beyond this landscape, consider promoting it to `kb/notes/`.

## Title conventions

**Reviews:** the repository name (`napkin.md`, `crewai-memory.md`) unless there is an established house-style variant.

**Root-level analyses.** Two cases:

- **Surveys and overviews** — use a topical title naming the subject (e.g., `agentic-memory-systems-comparative-review.md`).
- **Argumentative analyses** — analyses asserting a specific claim — use a claim-shaped title and add the `title-as-claim` trait, following the same conventions as `kb/notes/` (see `kb/notes/COLLECTION.md`).

## Outbound linking conventions

Organised per destination: when to prospect for links, and the authorised labels (semantics in [link-vocabulary.md](../reference/link-vocabulary.md)).

- **→ `kb/agent-memory-systems/`** (within collection) — search when a review touches a component of a larger reviewed system, realizes a contract named in another review, or shares a design axis with another system (the core cross-system work). Labels: `part-of` / `contains`, `implements` / `implemented-by`, `compares-with`, `see-also`.
- **→ `kb/sources/`** — for lightweight coverage, link back to the snapshot it was abstracted from; code-grounded reviews cite the repo directly. Labels: `derived-from`, `evidence`, `see-also`.
- **→ `kb/notes/`** — search when a system's design rests on a theoretical claim. Links usually run inverse (theory links in via `evidence` / `derived-from`), so promote a novel claim to `kb/notes/` rather than author theory in a review. Labels: `rationale`, `evidence` (rare), `defined-in`, `see-also`.
- **→ `kb/reference/`** — scan when a design element has a direct Commonplace analogue. Labels: `see-also`.
- **→ `kb/agentic-systems/`** — search when the reviewed memory, knowledge, or context-engineering subsystem is part of a broader agentic harness, or when a whole-system analysis supplies useful comparison context. Labels: `part-of` / `contains`, `compares-with`, `see-also`.
- **→ `kb/instructions/`** — scan when a review describes a workflow with a Commonplace counterpart. Labels: `see-also`.

`compares-with` (a difference in *systems* on a design axis) is distinct from theoretical `contrasts` (a difference in *claims*); use `compares-with` here.

## Types

- `agent-memory-system-review` -> `./types/agent-memory-system-review.md`
  Use for reviews of external agent memory or context-engineering systems. Set `source-tier: code-grounded` when source was inspected, `doc-grounded` (under `lightweight/`) when coverage is paper/README/article-only — same comparison elements, lower evidence tier.
- `note` -> `kb/types/note.md`
  Use for cross-system descriptive analyses and comparative reviews.
- `index` -> `kb/types/index.md`
  Use for navigation hubs and generated directory indexes.

## What does NOT belong here

- Transferable claims about KB methodology → `kb/notes/`
- Procedures and how-to guidance → `kb/instructions/`
- Descriptions of the Commonplace system itself → `kb/reference/`
- Whole external agentic-system or harness analyses not centered on memory/knowledge/context engineering → `kb/agentic-systems/`
- Raw snapshots of external sources → `kb/sources/`
- Work in progress → `kb/work/`
