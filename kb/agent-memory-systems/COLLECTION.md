# Writing conventions for kb/agent-memory-systems/

## Text contract

This collection documents external agent memory, knowledge, and context-engineering systems — what each is built from and does, grounded in the code and normalized through a shared Commonplace ontology. Broad cross-system comparison lives in the root-level analyses.

The quality goal is **fidelity + economy**: faithful to what the code actually does, expressed in the minimum shared vocabulary needed to compare systems. A review that misrepresents the reviewed system or forces its mechanism into an ill-fitting Commonplace term is worse than none — it pollutes the landscape.

## Structure

**`reviews/`** — individual system reviews, one file per system, typed as `../types/agent-memory-system-review.md`. The workflow and section rules live in `types/agent-memory-system-review.md`.

**`lightweight/`** — doc-grounded coverage for systems known from papers, READMEs, or articles when no inspectable implementation supports a code-grounded review. These are ordinary `agent-memory-system-review` notes carrying `source-tier: doc-grounded`; they hold the **same ontology-normalized comparison elements** as code-grounded reviews (four-field record, write side, and read-back direction) at a lower evidence tier — claim-level. The tier is about authority, not scope. Flip `source-tier` to `code-grounded` when inspectable implementation source supports the material findings. The review spec's instructions are tier-neutral (evidence-stance, source-metadata, and citation rules cover both); see the `source-tier` field in `types/agent-memory-system-review.md`.

**Collection root** — navigation (`README.md` plus build-time directory listings), cross-system analyses (comparative reviews, focused comparisons), and any analysis grounded in multiple reviews. When an analysis makes a claim general enough to transfer beyond this landscape, consider promoting it to `kb/notes/`.

Reviews record each external mechanism absolutely, even when it resembles Commonplace. The shared ontology chooses the distinctions and names comparable solutions; it does not turn the review into a Commonplace delta. Closed controlled fields feed the matrix. Open-ended mechanisms and ontology boundary cases support qualitative synthesis but no prevalence claim until the full corpus has been assayed for that concept.

A code-grounded review change invalidates the generated matrix/table pair and any landscape synthesis presented as current until each downstream artifact is rebuilt from the new source set. The publishing workflow must either complete that chain under explicit authority or report the generated pair as stale and the prior synthesis as historical. A public synthesis pins the matrix, row-linked reviews, and ontology inputs at one reconstructable revision or retained snapshot and accepts only a zero-flag matrix build.

Selective Commonplace implications are living transfer scans under `kb/reports/state/agentic-system-transfer/`. They are conditioned on a current interest brief and current Commonplace artifacts, never feed the matrix or public corpus analysis, and do not belong in a durable review. Their owning workflow keeps unresolved candidate judgments until disposition, then may replace or delete them. Legacy `Comparison with Our System`, `Borrowable Ideas`, and `What to Watch` sections may remain until their reviews are regenerated from source; new and replacement reviews omit them.

## Title conventions

**Reviews:** the repository name (`napkin.md`, `crewai-memory.md`) unless there is an established house-style variant.

**Root-level analyses.** Two cases:

- **Surveys and overviews** — use a topical title naming the subject (e.g., `agentic-memory-systems-comparative-review.md`).
- **Argumentative analyses** — analyses asserting a specific claim — use a claim-shaped title and add the `title-as-claim` trait, following the same conventions as `kb/notes/` (see `kb/notes/COLLECTION.md`).

## Outbound linking conventions

Organised per destination: when to prospect for links, and the authorised labels (semantics in [link-vocabulary.md](../reference/link-vocabulary.md)).

- **→ `kb/agent-memory-systems/`** (within collection) — search when a review touches a component of a larger reviewed system, realizes a contract named in another review, or shares a design axis with another system (the core cross-system work). Labels: `part-of` / `contains`, `implements` / `implemented-by`, `compares-with`, `see-also`.
- **→ `kb/sources/`** — for lightweight coverage, link back to the snapshot it was abstracted from. Labels: `derived-from`, `evidenced-by`, `see-also`.
- **→ `external`** — cite the reviewed repository, code, documents, or papers already in hand. Code-grounded reviews follow the type's commit-pinning and citation-shape rules; do not prospect the open web. Labels: `evidenced-by`, `see-also`.
- **→ `kb/notes/`** — search when a system's design depends on a theoretical claim. Use `rests-on` for that design dependency and rare `is-evidence-for` when the reviewed system instead bears on the target claim; promote a novel claim to `kb/notes/` rather than author theory in a review. Labels: `rests-on`, `is-evidence-for` (rare), `defined-in`, `see-also`.
- **→ `kb/reference/`** — scan when a design element has a direct Commonplace analogue. Labels: `see-also`.
- **→ `kb/agentic-systems/`** — search when the reviewed memory, knowledge, or context-engineering subsystem is part of a broader agentic harness, or when a whole-system analysis supplies useful comparison context. Labels: `part-of` / `contains`, `compares-with`, `see-also`.
- **→ `kb/instructions/`** — scan when a review describes a workflow with a Commonplace counterpart. Labels: `see-also`.

`compares-with` (a difference in *systems* on a design axis) is distinct from theoretical `contrasts` (a difference in *claims*); use `compares-with` here.

## Type eligibility

A typed artifact in this collection may use a global type spec under `kb/types/` or a local type spec under this collection's `types/` directory. Its `type:` value is the path to that contract. Frontmatter-free Markdown is implicit `text`.

## What does NOT belong here

- Transferable claims about KB methodology → `kb/notes/`
- Procedures and how-to guidance → `kb/instructions/`
- Descriptions of the Commonplace system itself → `kb/reference/`
- Selective Commonplace differences, borrowable ideas, or current watch items → a transfer scan under `kb/reports/state/agentic-system-transfer/`
- Whole external agentic-system or harness analyses not centered on memory/knowledge/context engineering → `kb/agentic-systems/`
- Raw snapshots of external sources → `kb/sources/`
- Work in progress → `kb/work/`
