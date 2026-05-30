# Writing conventions for kb/work/ (workshop layer)

## Workshop layer, not a register

Catch-all space for in-flight work: drafts, investigations, scratch notes, pasted traces, migration plans — anything that exists to move active work forward. Not a clean register; workshops mix theoretical drafts, descriptive sketches, and prescriptive runbooks freely.

Quality goal is **move the work forward** and **extract durable conclusions when it closes**. Workshop value is consumed, not accumulated — a finished workshop should produce library artifacts (notes, ADRs, instructions, references) and then disappear.

Plain markdown without frontmatter is fine. Imported, copied, or transitional files with incomplete or incompatible frontmatter are also fine. Don't "fix" workshop files just to make them look like notes — add structure only when it helps the work continue or makes later extraction easier.

## Structure

Substantial work lives in a named subdirectory `kb/work/<workshop-name>/` with a short `README.md` (or `framing.md` / `plan.md`) saying what the work is and what would close it. Small one-off files can live directly under `kb/work/` until they disappear or grow into a workshop.

The Active Workshops list in [`kb/work/README.md`](./README.md) is the curated operational navigation surface — add a one-line entry when starting, remove it when the workshop closes. If the README already has unrelated uncommitted edits, do not partially stage it just to keep navigation immediately complete; commit the workshop artifacts atomically and update the README in a later navigation cleanup.

## Title conventions

No constraint. Title fits whatever the workshop produces — claim, topic, plan, question.

## Outbound links

Permissive. Workshops freely cite the library to scaffold new work — library citation is how a workshop grounds itself in established knowledge before adding to it. Inline for prose connectives; footer for labelled — `- [title](path) — label: context phrase`.

Scan `kb/notes/`, `kb/reference/`, `kb/agent-memory-systems/`, `kb/instructions/`, `kb/sources/`, and peer workshops in `kb/work/` for link targets. Workshop links are working notes, not durable graph contracts — borrow from theoretical/descriptive/prescriptive labels as the work calls for, or use a local phrase. Authorisation is loose; the articulation test still applies.

**Labels (suggestions, not authoritative):**

| label | destinations | reader-need / when to use |
|---|---|---|
| `extends`, `grounds`, `mechanism`, `contradicts`, `contrasts` | notes | theoretical-shaped (see `kb/reference/link-vocabulary.md`) |
| `evidence`, `derived-from` | reference, agent-memory, sources | this artifact corroborates / the workshop was abstracted from this |
| `rationale` | notes | this design or rule rests on this claim |
| `defined-in` | notes/definitions | reader may not know the term |
| `draws-on`, `tests`, `depends-on`, `produces`, `supersedes` | any | working-state labels — use whichever fits the workshop's progress |
| `see-also` | any | adjacent companion |

Library collections do not link **into** `kb/work/` — workshops are sinks, not sources of durable references. If a workshop produces something the library should cite, extract it first.

## Closing a workshop

When the workshop's question is answered, extract the durable conclusions into the right library collection (`kb/notes/`, `kb/reference/`, `kb/instructions/`, `kb/reference/adr/`), delete the workshop directory, and remove its entry from `kb/work/README.md`. See `kb/notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md` for the rationale.

## Types

| type | file | use for |
|---|---|---|
| `note` | `kb/types/note.md` | workshop output that needs normal note metadata before promotion |
| `instruction` | `kb/types/instruction.md` | temporary procedures, experimental gates, runbooks |
| `structured-claim` | `kb/notes/types/structured-claim.md` | workshop draft already shaped as evidence/reasoning argument |
| `dir-index` | `kb/types/dir-index.md` | generated workshop directory listings |
| `curated-index` | `kb/types/curated-index.md` | curated workshop navigation hubs |
| `text` (implicit) | no frontmatter | drafts, traces, scratch, anything pre-structural |

## What does NOT belong here

- Anything stable enough to be referenced from the library → promote to the right durable collection
- External source captures → `kb/sources/`
- Generated reports → `kb/reports/`
