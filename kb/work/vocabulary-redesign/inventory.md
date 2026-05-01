# Vocabulary Inventory

Working inventory for the redesign. This is not a proposal yet; it names the current terms, likely pressure points, and candidate decisions to test.

## Always-loaded Terms

| Term | Current role | Pressure to test |
|---|---|---|
| Context engineering | Names the domain: routing, loading, scoping, maintenance under bounded context | Broad but probably foundational; check whether it absorbs too much that should be named separately |
| Distillation | Goal-oriented compression for a bounded consumer | Strong operator term; test whether "compression" language causes selection-only misunderstandings |
| Constraining | Narrowing interpretation space for reliability/speed/cost | Strong operator term; test whether it overlaps too much with validation, convention, and governance |
| Codification | Natural language to symbolic medium; far end of constraining | Probably stable; test whether "far end" hides cases where code is not the right endpoint |
| Register | Theoretical/descriptive/prescriptive content mode | Useful for collection conventions; test whether it deserves always-loaded status |
| Workshop | Temporal work-in-flight workspace | Stable operational term; test whether it needs a paired "library" definition in always-loaded context |

## Adjacent Terms To Audit

| Term | Where it appears | Redesign question |
|---|---|---|
| Artifact | Notes, memory design, type system, reviews | Does it need a definition, or is ordinary usage enough? |
| System-definition | Memory and learning notes | Is this clear enough for always-loaded use, or should it stay in notes? |
| Memory | Agent-memory notes and reviews | Does the KB need one governing definition, or does "memory" remain a family resemblance term? |
| Knowledge | KB goals, notes, source/review language | Is this overloaded between factual content, operational context, and durable artifacts? |
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

- Always-loaded vocabulary must be short, but the methodology now uses more terms than the original control-plane section can comfortably teach.
- Link labels have both local collection rules and a global catalogue; authors need one source of truth at write time.
- `distillation`, `constraining`, and `codification` are useful together, but the hierarchy between them is easy to blur.
- `register`, `type`, `trait`, and `status` are all classification axes; agents may treat them as one taxonomy unless the distinction is explicit.
- "Memory" in related-system reviews can mean storage backend, learned artifact, activation policy, or whole adaptation loop.
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
5. Draft a keep / revise / demote proposal before editing durable docs.
