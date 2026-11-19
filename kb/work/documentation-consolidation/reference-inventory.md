# Inventory of the top-level reference documents

Made by an agent (claude-fable-5-2) on 2026-11-19 at the operator's request. It lists the 30 documents directly under `kb/reference/`, beside `README.md` and `COLLECTION.md`. The subdirectories `adr/`, `proposals/`, `definitions/` and `types/` stay as they are, by the operator's decision.

Basis: each document's description, opening paragraph and section headings, and a count of the files that name it. No document was read in full, so a role below is a first classification, not a review.

"Reached by" says where a reader meets the document: `AGENTS.md`, instructions or skills (a route), theory notes or ADRs (links), or search only.

## Operating manuals

They say how to run a command and what it does. A command's `--help` and its source carry the exact contract.

| Document | Size | Reader | Reached by |
|---|---|---|---|
| `README-REVIEW-SYSTEM.md` | 61k | operator deciding whether and how to run review and editing; agent for intent that help does not state | `AGENTS.md`, 3 instructions, 11 ADRs |
| `commands.md` | 43k | operator; agent looking up a command it was not routed to | `AGENTS.md`, 3 instructions, 2 skills |

## Architecture

They say which component owns what, which representation is authoritative, and what must hold across components. The reader is an agent or maintainer changing the code.

| Document | Size | Reader | Reached by |
|---|---|---|---|
| `architecture.md` | 8k | agent changing installation, init or library resolution | `AGENTS.md` (as a group pointer), 19 ADRs, 12 theory notes |
| `storage-architecture.md` | 7k | agent adding or moving stored state | `AGENTS.md`, 5 ADRs |
| `review-architecture.md` | 21k | agent changing review or editing code | `AGENTS.md`, 10 ADRs |
| `workflow-architecture.md` | 1k | agent changing a handoff between runs | no instruction, ADR or theory note names it |
| `instruction-generation.md` | 11k | agent changing the scaffold or init | 3 ADRs |
| `documentation-site.md` | 4k | agent or operator changing the published site | 4 ADRs |
| `control-plane-goals.md` | 7k | agent changing the always-loaded files or their scaffold | 1 instruction, 1 skill |
| `scenario-architecture.md` | 5k | reader asking why the command and skill split is as it is | 2 ADRs |

`scenario-architecture.md` and `instruction-generation.md` open with "How Commonplace instantiates" a theory. They are partly worked-case notes.

## Authoring rules

A writer of KB content applies them. They bind at write time, or the validator enforces them.

| Document | Size | Reader | Reached by |
|---|---|---|---|
| `link-vocabulary.md` | 20k | agent writing or connecting a note | `AGENTS.md`, 2 instructions, 1 skill, 10 ADRs |
| `validation-contract.md` | 22k | agent reading a validator finding; agent changing validation | 1 instruction, 1 skill, 5 code or test files |
| `collections-and-types.md` | 12k | agent adding a collection or type | 10 theory notes, 5 ADRs |
| `content-routing.md` | 10k | agent deciding where content goes | `AGENTS.md` |
| `navigation.md` | 9k | agent searching the KB | `AGENTS.md`, 1 instruction |
| `collection-prototypes.md` | 3k | agent or operator creating a collection | 4 theory notes |
| `vocabulary-collision-ledger.md` | 7k | agent choosing a term in new text | `AGENTS.md` |
| `vocabulary-unification-ledger.md` | 4k | agent revising a definition | `AGENTS.md` |
| `epistemic-stance.md` | 2k | agent assessing what a claim or definition means | `AGENTS.md`, 4 theory notes |

## The repository as a worked case

They make claims about Commonplace itself, often by applying a theory note to it. The reference index already groups most of them under this heading. They are found by search or from a theory note; no instruction routes to them.

| Document | Size | What it claims | Reached by |
|---|---|---|---|
| `commonplace-as-an-instrument.md` | 9k | the KB application tests the design's theories together | 2 theory notes |
| `commonplace-declared-frame.md` | 3k | the boundary under which self-improvement attributions to Commonplace hold | 3 theory notes |
| `tag-readme-trace-as-self-improving-loop.md` | 5k | one observed change maps onto search, evaluation and retention | 5 theory notes |
| `where-change-candidates-come-from-in-commonplace.md` | 6k | how problems are noticed and candidates drafted here | 4 theory notes |
| `design-rationale-management.md` | 10k | how rationale is spread over proposals, ADRs, contracts and enforcement | 4 theory notes, 1 ADR |
| `source-adoption-policy.md` | 7k | which borrowed ideas are adopted, by source | 4 theory notes |
| `agent-memory-coverage.md` | 7k | how the shipped surfaces realize agent-memory requirements | 1 theory note |
| `collections-never-own-frontmatter-semantics.md` | 5k | why the collection and type split is asymmetric | 1 ADR |

Two of these state a rule as well as a claim: `source-adoption-policy.md` (a policy) and `collections-never-own-frontmatter-semantics.md` (the rationale for a boundary, close to an ADR).

## Plans, briefs and records

Each has a different kind from the rest and may belong elsewhere.

| Document | Size | What it is | Possible home |
|---|---|---|---|
| `commonplace-agent-memory-gap-plan.md` | 10k | a nine-step plan for closing gaps | `proposals/`, as an undecided design |
| `agentic-system-analysis-design-brief.md` | 2k | operator direction for one subsystem, dated 2026-10-05 | beside the analysis method in `kb/agentic-system-analyses/` |
| `harness-sub-agent-model-selection-regression.md` | 4k | a dated incident and its operational consequence | `kb/reports/retained/`, or keep as a record |

## Observations

- The reference index (`README.md`) already groups the documents into architecture, type system, procedures and "the repository as a worked case". The grouping exists in the index only, not on disk.
- The operator's observation holds for the worked-case group: each is a claim about this system. The collection contract already names the test. A claim belongs in theory when a free variable remains after Commonplace's choices are scoped, and here when none does.
- Instructions and skills route to 6 of the 30: both manuals, `link-vocabulary`, `validation-contract`, `navigation` and `control-plane-goals`.
- The two manuals are 104k of the 381k at this level, and they overlap most with `--help` and the code.

## One possible layout

| Subdirectory | Holds | Count |
|---|---|---|
| `operation/` | the two manuals | 2 |
| `architecture/` | the architecture group | 8 |
| `authoring/` | the authoring rules | 9 |
| `worked-case/` | the worked-case group | 8 |

The three plans, briefs and records would move out of the collection or into `proposals/`.

Costs to weigh before choosing. Every move changes paths that `AGENTS.md`, ADRs and theory notes link; `commonplace-relocate-note` rewrites them, and each relocation is its own commit. Subdirectories group by kind, which helps a reader browsing and does not help a reader searching. They do not add a route from a task to a document, which is the workshop's main question.
