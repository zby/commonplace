# Vocabulary Inventory

Working inventory for the redesign. The first durable artifact-analysis vocabulary has now landed; this file tracks which terms are hot-path, which remain adjacent, and which earlier candidates have been replaced.

## Always-loaded Terms

| Term | Current role | Pressure to test |
|---|---|---|
| Context engineering | Names the domain: routing, loading, scoping, maintenance under bounded context | Broad but probably foundational; check whether it absorbs too much that should be named separately |
| Distillation | Goal-oriented compression for a bounded consumer | Strong operator term; test whether "compression" language causes selection-only misunderstandings |
| Constraining | Narrowing interpretation space for reliability/speed/cost | Strong operator term; test whether it overlaps too much with validation, convention, and governance |
| Codification | Natural language to symbolic medium; far end of constraining | Probably stable; test whether "far end" hides cases where code is not the right endpoint |
| Retained artifact | Retained state a later agentic loop can consume in a behavior-shaping way | Newly landed; check whether it is too broad for always-loaded context or earns its slot by preventing memory/storage confusion |
| Operative part | Behavior-affecting content, structure, parameterization, or mechanism inside a retained artifact or consumption path | Newly landed; important for mixed artifacts, but may be hard to teach without examples |
| Storage substrate | Where retained state persists | Newly landed; replaces backend/storage-class shorthand |
| Representational form | How the operative part is encoded and consumed: prose, symbolic, distributed-parametric, or mixed | Newly landed; replaces artifact class / opaque-prose-symbolic shorthand |
| Lineage | Source dependencies and derivation status needed for invalidation, regeneration, retirement, or review | Newly landed; replaces source relation in the hot path |
| Behavioral authority | Consumer, channel, and force of behavior shaping | Newly landed; replaces loose role/control-path/future-use language |
| Knowledge artifact | Retained artifact consumed as evidence, reference, context, explanation, or advice | Newly landed as authority-path family; guard against treating it as intrinsic object type |
| System-definition artifact | Retained artifact consumed with instruction, enforcement, routing, validation, configuration, evaluation, or learning force | Newly landed as authority-path family; guard against treating it as form or substrate |
| Register | Theoretical/descriptive/prescriptive content mode | Useful for collection conventions; test whether it deserves always-loaded status |
| Workshop | Temporal work-in-flight workspace | Stable operational term; test whether it needs a paired "library" definition in always-loaded context |

## Replaced Candidate Terms

| Earlier candidate | Current disposition | Replacement |
|---|---|---|
| Persistent adaptive artifact | Keep paper-facing only | `retained artifact` |
| Adaptive artifact | Avoid unless paper-local | `retained artifact` |
| Artifact-use pairing | Transitional bridge, no durable hot-path term | `retained artifact` + `operative part` + `behavioral authority` |
| Future system use | Avoid as primary term | `behavioral authority` / consumption path |
| Control path | Use only when route matters more than force | `behavioral authority` includes consumer, channel, and force |
| Source relation | Use only as ordinary prose | `lineage` |
| Artifact class | Retire for this taxonomy | `representational form` |
| Backend / storage class | Retire for this taxonomy | `storage substrate` |
| Role / artifact role | Retire when precision matters | `behavioral authority` |
| Opaque artifact | Use for practical inspectability, not taxonomy class | `distributed-parametric` as form, plus opacity as scale/property |
| Eligibility | Keep as lifecycle/policy metadata | Not a core artifact-analysis field |

## Adjacent Terms To Audit

| Term | Where it appears | Redesign question |
|---|---|---|
| Artifact | Notes, memory design, type system, reviews | Ordinary usage remains broad; use `retained artifact` when behavioral consequence is the boundary |
| System-definition | Memory and learning notes | Use `system-definition artifact` for the authority-path family; avoid implying intrinsic object type |
| Memory | Agent-memory notes and reviews | Does the KB need one governing definition, or does "memory" remain a family resemblance term? |
| Knowledge | KB goals, notes, source/review language | Use `knowledge artifact` when the specific question is advice/reference/evidence authority |
| Instruction | `kb/instructions/`, skills, AGENTS.md | Does it mean a collection, an artifact class, or any behavior-shaping text? |
| Skill | Skills workflow, instructions, plugin packaging | Is the distinction from instruction crisp enough after the skills-vs-instructions work? |
| Type | Frontmatter and type contracts | Does "type" mean schema, writing contract, collection-local option, or artifact role? |
| Trait | Frontmatter property | Does the term still earn its slot, or should traits be described as checkable properties? |
| Status | Frontmatter lifecycle/commitment state | Is status maturity, freshness, processing state, or review confidence? |
| Source | `kb/sources/`, citations, evidence | Does source mean captured external material, any evidence, or provenance root? |
| Report | `kb/reports/`, review bundles, generated outputs | Does report mean generated artifact, reviewer output, or analysis summary? |
| Index | Generated directories, curated indexes, tag hubs | Are generated vs curated indexes sufficiently distinguished? |
| Link label | Link vocabulary | Should labels be reader-need terms, register-crossing terms, or authoring instructions? |

## Known Friction Signals

- Always-loaded vocabulary must be short, but the methodology now includes a substantial artifact-analysis cluster.
- Link labels have both local collection rules and a global catalogue; authors need one source of truth at write time.
- `distillation`, `constraining`, and `codification` are useful together, but the hierarchy between them is easy to blur.
- `register`, `type`, `trait`, and `status` are all classification axes; agents may treat them as one taxonomy unless the distinction is explicit.
- "Memory" in related-system reviews can mean storage substrate, representational form, lineage, behavioral authority, activation policy, or whole adaptation loop.
- Earlier paper vocabulary still appears in workshop material; durable docs should use the landed terms unless discussing the paper.
- Workshop/library language is operationally important but may need a paired definition rather than only a workshop entry.

## Candidate Decision Shapes

- **Keep always-loaded:** term remains in `AGENTS.md` with a one-line gloss and definition-note link.
- **Demote:** remove from `AGENTS.md`, keep or improve an on-demand definition note.
- **Split:** keep the current term but introduce a sharper subterm or paired contrast.
- **Merge:** retire a local term and route writers to an existing term.
- **Rename:** choose a clearer word, then add migration notes and update high-traffic references.
- **Codify:** add a review gate, validator warning, or authoring checklist when misuse is detectable.

## First Pass Tasks

1. Extract all terms from `AGENTS.md`, `kb/notes/definitions/`, `kb/reference/link-vocabulary.md`, and collection `COLLECTION.md` files.
2. Mark each term by load tier: always-loaded, collection-loaded, type-loaded, note-local, or review-local.
3. For each always-loaded term, write the bad decision that happens when the term is missing or misunderstood.
4. Identify terms that are synonyms, near-synonyms, or overloaded across collections.
5. Draft propagation edits for places that still use replaced shorthand: backend, class, role, source relation, future system use, and artifact-use pairing.
