# Writing conventions for kb/work/ (workshop layer)

## Workshop layer, not a register

Catch-all space for in-flight work: drafts, investigations, scratch notes, pasted traces, migration plans — anything that exists to move active work forward. Not a clean register; workshops mix theoretical drafts, descriptive sketches, and prescriptive runbooks freely.

Quality goal is **move the work forward** and **extract durable conclusions when it closes**. Workshop value is consumed, not accumulated — a finished workshop should produce library artifacts (notes, ADRs, instructions, references) and then disappear.

Plain markdown without frontmatter is fine. Imported, copied, or transitional files with incomplete or incompatible frontmatter are also fine. Don't "fix" workshop files just to make them look like notes — add structure only when it helps the work continue or makes later extraction easier.

## Structure

Substantial work lives in a named subdirectory `kb/work/<workshop-name>/` with a short `README.md` (or `framing.md` / `plan.md`) saying what the work is and what would close it. A workflow that produces many uniform run directories may group them under `kb/work/<workflow-name>/`; multistage writing uses `kb/work/multistage/`. Each nested run remains a workshop with its own framing file and entry in `kb/work/README.md`. Small one-off files can live directly under `kb/work/` until they disappear or grow into a workshop.

The framing file should fix only what a later session can't determine — the goal, who posed it and in what role (the operator's direction, or an agent's proposal awaiting adoption), what closes the workshop, the evaluation boundary, and bookkeeping conventions. A later session cannot recover from the question whose intent it serves. Whether the intent is still held is not a field: it is read from the workshop's lifecycle position — listed in the Active Workshops list, or deleted — and from the date posed, which the framing records so a triage of that list can catch a stale question. Don't pre-commit method, first targets, or interpretation of prior results; the live work will determine those — rationale: [An author should fix what the executor can't determine, not what it will](../notes/fix-what-the-executor-cant-determine-not-what-it-will.md).

The Active Workshops list in [`kb/work/README.md`](./README.md) is the curated operational navigation surface — add a one-line entry when starting, remove it when the workshop closes. If the README already has unrelated uncommitted edits, do not partially stage it just to keep navigation immediately complete; commit the workshop artifacts atomically and update the README in a later navigation cleanup.

## Title conventions

No constraint. Title fits whatever the workshop produces — claim, topic, plan, question.

## Outbound links

Permissive. Workshops freely cite the library to scaffold new work — library citation is how a workshop grounds itself in established knowledge before adding to it. Inline for prose connectives; footer for labelled — `- [title](path) — label: context phrase`.

Scan `kb/notes/`, `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, `kb/instructions/`, `kb/sources/`, and peer workshops in `kb/work/` for link targets. Workshop links are working notes, not durable graph contracts — borrow from theoretical/descriptive/prescriptive labels as the work calls for, or use a local phrase. Authorisation is loose; the articulation test still applies.

**Labels (suggestions, not authoritative):**

| label | destinations | reader-need / when to use |
|---|---|---|
| `extends`, `grounds`, `mechanism`, `contradicts`, `contrasts` | notes | theoretical-shaped (see `kb/reference/link-vocabulary.md`) |
| `evidenced-by`, `abstracted-from` | notes, reference, agent-memory, agentic-systems, sources, external, work | the target bears on this working assertion / the workshop was abstracted from this |
| `is-evidence-for` | notes, reference, work | this working observation bears materially on the target assertion without implying target-side uptake |
| `rests-on` | notes | this working design or rule depends on this claim |
| `defined-in` | notes/definitions | reader may not know the term |
| `draws-on`, `tests`, `depends-on`, `produces`, `supersedes` | any | working-state labels — use whichever fits the workshop's progress |
| `see-also` | any | adjacent companion |

Library collections do not link **into** `kb/work/` — workshops are sinks, not sources of durable references. If a workshop produces something the library should cite, extract it first.

## Closing a workshop

When the workshop's question is answered, extract the durable conclusions into the right library collection (`kb/notes/`, `kb/reference/`, `kb/instructions/`, `kb/reference/adr/`), delete the workshop directory, and remove its entry from `kb/work/README.md`. See `kb/notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md` for the rationale.

**No redirect, deliberately.** Workshops are published — `kb/work/` is not in `properdocs.yml`'s `exclude_docs`, because a live workshop is worth showing to someone for consultation. But closure does not add a `redirect_maps` entry the way [retiring a library artifact](../instructions/retire-artifact.md) does. The layer is temporary by design: a workshop URL was never a durable address, and a closed workshop often has several successors or none, so there is frequently no honest target to point at. Dead workshop URLs are an accepted cost, not an oversight — 84 closed workshops have left one redirect between them. Do not "fix" this by back-filling redirects.

## Type eligibility

An artifact anywhere under `kb/work/` may reference any valid type spec under `kb/`. This lifecycle exception lets a workshop stage an artifact for any target collection and test the real target contract; it does not relocate ownership of that type. Frontmatter-free Markdown remains implicit `text`.

## What does NOT belong here

- Anything stable enough to be referenced from the library → promote to the right durable collection
- External source captures → `kb/sources/`
- Durable external agentic-system and harness analyses → `kb/agentic-systems/`
- Generated reports → `kb/reports/`
