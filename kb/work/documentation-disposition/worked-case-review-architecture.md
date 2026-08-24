# Worked case: `review-architecture.md`

Executed 2026-08-24. The fourth artifact taken through the full disposition
procedure.

## Result

**Minimized around four cross-component boundaries.** The document remains an
architecture surface, but no longer serves as a module catalogue, storage
schema, command list, or exact protocol reference. It now carries execution
ownership, canonical-state versus artifact roles, all-or-nothing finalization,
and the freshness hash boundary.

The edit reduced the page from 13,761 bytes and 126 lines to 5,877 bytes and
113 lines. Line count falls less than byte count because the retained rules are
wrapped for readable diffs; authored content fell by 57 percent.

## Consumption events and dispositions

| Unit | Consumer question | Required reliability | Recovery result | Source grain | Document grain | Recurrence and saving | Maintenance form | Disposition | Retrieval path |
|---|---|---|---|---|---|---|---|---|---|
| Package and module inventory | Which file owns a named operation? | orientation | recoverable, inventory incomplete | one task-vocabulary search over module docstrings and symbols | 20 bullets | recurring, but source selects a finer and more complete unit | live source | omit | `commonplace-source`; `rg` under `commonplace/review` |
| Execution flow and dispatch ownership | Which component selects, dispatches, writes, and finalizes? | architectural | distributed across CLI, library, harness procedure, and ADRs | selector, creation, prompt, worker instruction, finalizer | one flow plus several sections | high synthesis saving for changers and operators | authored boundary linked to ADR 067 | keep and compress | execution section |
| Physical data-model table | What tables and columns exist? | exact | duplicate and incomplete as schema | `commonplace.store`, `review_db.py`, storage tests | six-row summary | source/schema must still be read | live schema plus storage architecture | consolidate | `storage-architecture.md`; source |
| Canonical state versus artifacts | Which representation may advance or witness review state? | architectural | distributed; no single symbol closes it | DB transitions, artifact writer, finalizer, operator guide | one subsection | high consequence and aggregate source fan-out | authored boundary linked to ADR 035 | keep and compress | canonical-state section |
| Exact result kinds, statuses, and footer grammar | What values are accepted? | exact | recoverable and already documented operationally | schema and protocol parser | four detailed bullets | source/help and operator guide close exact questions | executable parser/schema | omit | review-system guide; protocol source |
| Selector freshness mechanics | Why is one pair fresh or stale? | operational exactness | duplicate | selector source, review guide, freshness architecture | one paragraph | no separate saving | live source plus operator guide | omit | review-system guide; freshness architecture |
| Prompt-scaffolding hash boundary | What changes can affect judgment without automatically staling baselines? | architectural | cross-module invariant | freshness capture plus prompt renderer and conformance sources | three paragraphs | high consequence; source requires synthesis | authored boundary plus comments in both change loops | keep and compress | freshness-boundary section; source comments |
| Factored dependency growth path | How might a third dependency be added? | design direction, not shipped behavior | stronger proposal exists | proposal plus current two-input implementation | one current-facing paragraph | architecture copy risks presenting proposal as shipped | proposal | consolidate | `factored-dependency-pairs-for-review-freshness.md` |
| Command surface | Which review commands exist? | complete discovery | duplicate | checked command catalogue | two lists | no saving | checked catalogue | omit | `commands.md` |
| Final invariant list | What must remain true across creation, worker execution, finalization, and freshness? | architectural or exact by row | mixed | ADRs, tests, source, earlier document sections | nine bullets | synthesis valuable only for cross-component rows | integrate boundary rows; source for exact rows | split | four retained sections |

## Source-routing experiment

Representative questions began with task vocabulary rather than module names:

| Starting terms | Live-source result | Former architecture result |
|---|---|---|
| stale or requested review pairs | `review_target_selector.py` and selector records | one module bullet |
| manifest, result filename, job output path | `artifacts.py` symbols and docstrings | four bullets across two sections |
| whole-job failure, finalization | `finalization.py`, protocol comments, and focused tests | protocol/finalization bullets plus invariant list |
| criterion resolution, type, collection | `resolve_criteria.py`, `type_conformance.py`, `collection_conformance.py` | five module bullets |

The source tree contains 24 Python files and 23 module docstrings. Excluding the
two `__init__.py` files, the authored module map named 20 of 22 modules: it
omitted `clock.py` and `critique.py` without signalling that it was partial.
Generating the map was not justified because task-vocabulary source search
already selected the owning files and their symbols.

## Exactness failure exposed by comparison

The former freshness section said that a conformance prompt's evaluated text
and baseline snapshot were identical. Job preparation actually hashes and
stores the full criterion file, then strips criterion frontmatter before
placing its text in the prompt. The intended architecture rule still holds—a
criterion-file edit changes the accepted input—but the byte-identity statement
did not.

This was the same failure mode as the retired schema page: implementation prose
claimed exactness that only the implementation could supply. The rewrite keeps
the stable rule and sends byte-level questions to `freshness.py` and
`protocol/prompt.py`.

## Why the document survives

The retained questions do not map to one source symbol. For example, deciding
whether a new worker-side behavior belongs in the generated prompt, the harness,
or deterministic finalization requires the selector-to-finalizer flow, ADR 067's
worker isolation, and the state boundary together. Likewise, understanding why
a result-file failure is fatal while a manifest refresh failure is not requires
the evidence-versus-inspection distinction plus the finalization transaction.

The 5.9 KB architecture page closes those questions without reconstructing the
relation from several modules and ADRs. It is a judgment-dependent synthesis,
not an exact implementation cache. Its maintenance section names the four
change triggers and explicitly excludes module additions, signatures, columns,
arguments, and protocol fields from its review obligation.

## Next

The three remaining scoped artifacts can now be swept without another genre
probe. `storage-architecture.md` is first because this case exposed its role as
the stronger home for physical-store facts; `architecture.md` and
`freshness-architecture.md` follow.
