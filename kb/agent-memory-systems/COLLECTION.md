# Writing conventions for kb/agent-memory-systems/

## Register

This collection operates in the **descriptive [register](../notes/definitions/register.md)** (one of three content modes — theoretical, descriptive, prescriptive — determining quality goal, title conventions, and linking rules). It documents external agent memory, knowledge, and context-engineering systems — what each is built from and does, grounded in the code. Broad cross-system comparison lives in the root-level analyses.

The quality goal is **fidelity + economy**: faithful to what the code actually does, in minimum tokens. A review that misrepresents the reviewed system is worse than none — it pollutes the landscape.

## Structure

**`reviews/`** — individual system reviews, one file per system, typed as `../types/agent-memory-system-review.md`. The workflow and section rules live in `types/agent-memory-system-review.md`.

**`lightweight/`** — lightweight `type: kb/types/note.md` coverage for systems known from papers, READMEs, or articles when no reachable repository has been inspected. These entries keep lightweight systems visible without using the repo-required review type.

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
- **→ `kb/instructions/`** — scan when a review describes a workflow with a Commonplace counterpart. Labels: `see-also`.

`compares-with` (a difference in *systems* on a design axis) is distinct from theoretical `contrasts` (a difference in *claims*); use `compares-with` here.

## Types

- `agent-memory-system-review` -> `./types/agent-memory-system-review.md`
  Use for code-grounded reviews of external agent memory or context-engineering systems.
- `note` -> `kb/types/note.md`
  Use for lightweight coverage and cross-system descriptive analyses.
- `index` -> `kb/types/index.md`
  Use for navigation hubs and generated directory indexes.

## What does NOT belong here

- Transferable claims about KB methodology → `kb/notes/`
- Procedures and how-to guidance → `kb/instructions/`
- Descriptions of the Commonplace system itself → `kb/reference/`
- Raw snapshots of external sources → `kb/sources/`
- Work in progress → `kb/work/`
