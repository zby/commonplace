# Fixture split of two retained results along the partition candidate

Executed on 2026-09-28 with `scripts/split_agentic_result_fixture.py`
(one-off, deleted when this workshop closes) against the retained results
and local specialist reports of `AAS-2026-09-27-napkin-05` and
`AAS-2026-09-27-dynamic-cheatsheet-04`. Members were written outside the
repository. The rules applied are those of the
[partition candidate](./partition-candidate.md): a record is declared in the
member that established it, using the result's Reconciliation mapping to
identify specialist-registered records; the memory member is the local
specialist report with proposal IDs mapped to canonical IDs; a passage the
memory member holds is cited, not repeated, by the runtime member; the
coordinator's own version of a specialist-registered record is appended as
an amendment body, not a second declaration.

## Set checks

| Check | Napkin | Dynamic Cheatsheet |
|---|---:|---:|
| Canonical records, runtime-declared / memory-declared | 26 / 11 | 20 / 5 |
| IDs declared twice across the set | 0 | 0 |
| References unresolved within the set | 0 | 0 |
| Proposal IDs left unmapped in the memory member | 0 | 0 |
| Distinct quote passages, result and report union | 43 | 31 |
| Distinct quote passages in the set | 43 | 31 |
| Passages repeated within the set | 0 | 0 |
| Passages moved out of the runtime member as memory-held copies | 21 | 14 |

The union of evidence is preserved and no passage occurs twice. Every
cross-member reference resolves with the bare ID.

## Sizes

Whitespace-separated words.

| Document | Napkin | Dynamic Cheatsheet |
|---|---:|---:|
| Old result, retained | 14,770 | 12,593 |
| Old specialist report, local | 7,703 | 5,451 |
| Overview member | 1,950 | 1,934 |
| Runtime member | 4,665 | 4,391 |
| Memory member | 9,968 | 6,397 |
| of which coordinator amendment bodies | 2,196 | 908 |
| Epistemic member | 2,922 | 2,378 |
| Set total | 19,505 | 15,100 |
| Dropped memory/context lens section | 937 | 902 |

The largest member is the memory member at 67 and 51 percent of the old
result. The set is 87 and 84 percent of the old result plus local report.
Both figures depend on the coordinator amendment bodies, which are the
coordinator's rewrite of records the specialist declared; the assessment
below decides how much of them survives.

## Findings that change the design

**Seeded records are re-declared by the specialist.** Both reports declare
the seeded canonical records with the same heading form as their own
proposals: eleven in Napkin and ten in Dynamic Cheatsheet. Under one
namespace with one declaration per record, the memory member must mark
these as annotations. The fixture rewrote them as `### On OBJ-1 — label`.
The report type needs that annotation grammar, and set validation needs to
distinguish the two heading forms.

**The coordinator carries specialist passages onto records it declares.**
All 35 and all 20 specialist passages were copied into the old result, so
the runtime member started with every one of them on seeded records. The
ownership rule moved them back: the passage stays with the memory finding
it supports and the runtime record cites it. Finalization needs this
deduplication step, and the runtime record's evidence field must be able
to cite a passage held by another member.

**The grammar varies between results.** One result declares records at
heading level three, the other at level four; one records the proposal
mapping as a table, the other as prose. The type contracts for the members
should fix one declaration grammar and one mapping grammar so set
validation does not need to accept both.

## Coverage of the dropped memory/context lens section

An independent reader compared every paragraph of the dropped section with
the memory member and the overview's synthesis. In both fixtures every
paragraph is present word for word in the memory member: fourteen of
fourteen in Napkin, eleven of eleven in Dynamic Cheatsheet, drawn from the
specialist's Core ideas, Write side, Read-back and Comparison rationale
sections with canonical IDs already applied. No claim lacks a home and the
section never disagrees with the specialist.

So the section was not a re-narration but a verbatim copy, about 900 words
per result, retained twice today. Dropping it is lossless for these
fixtures. A run whose coordinator paraphrases or adjusts the specialist's
text would need the same check; an exact-match comparison of the old
section against the memory member is cheap and flags any changed paragraph.

## The coordinator's amendment bodies

An independent reader compared the coordinator's version of each
specialist-registered record with the specialist's declaration, sentence by
sentence.

| Class | Napkin (11 records) | Dynamic Cheatsheet (5 records) |
|---|---:|---:|
| Verbatim copy, or only "proposal" relabelled "registered" | 7 | 3 |
| Copy plus added fields only | 2 | 1 |
| Copy plus added fields and added findings | 2 | 1 |
| Words that survive if only additions are kept | about 240 of 2,196 | about 260 of 908 |

None of the amendments contradicts its declaration. The additions are of
two kinds. Bookkeeping fields: a cross-record link (to ABS-2, RTE-6, RTE-7
or CLM-1), a source re-identification (SRC-2 to the new SRC-3 for the
reported-operation layer, which the specialist had asked for), and a
consolidated evidence line. And the coordinator's own classifications on
three memory routes: the theory-builder conditions, decision roles,
operating mode, answer oracle and addressability that the runtime pass
records on every admitting route and the specialist does not.

The reader flagged that the added links point to IDs the memory member
does not declare. Across the set they all resolve, as the set check above
shows; that is what the manifest-resolved namespace is for. The memory
member's own source table is the frozen input's register, so SRC-3, which
the coordinator registered after the specialist asked for it, is declared
only in the overview.

## Consequences for the candidate

With re-narration dropped and only additions kept, the projected sizes are:

| Document | Napkin | Dynamic Cheatsheet |
|---|---:|---:|
| Memory member | about 8,000 | about 5,750 |
| Largest member as a share of the old result | 54% | 46% |
| Set total | about 17,550 | about 14,450 |
| Set as a share of old result plus local report | 78% | 80% |

Three rules follow, to be written into the member contracts:

1. **Finalization appends deltas, not versions.** The coordinator's
   version of a specialist-registered record contributes only what differs
   from the declaration: a changed token with its superseded value, an
   added field, an added link. A relabelling from proposal to registered is
   carried by the Reconciliation mapping and is not an amendment.
2. **Amendment and annotation are different mechanisms.** An amendment
   corrects a declared fact and attaches to the declaring member. An
   annotation is another lens's classification of a record and lives in
   the annotating member, keyed `On <ID>`. The memory member already
   annotates seeded runtime records this way; symmetrically, the runtime
   pass's theory-builder overlay on a memory route is an annotation in the
   runtime member, not an amendment in the memory member.
3. **One source register.** The overview's Source register is the set's
   only declaration of `SRC-*` IDs. The memory member keeps the frozen
   input's register as provenance, not as declarations.

The candidate holds on both fixtures: no duplicated declaration, no
duplicated passage, every reference resolving, the dropped section
lossless, and the amendment bodies reducible to about a tenth to a third of
their size. The largest member is half the old result rather than the
"halves" the candidate projected for Napkin, because the memory member
absorbs the specialist's full report; the cost shows up as a set about a
fifth smaller than today's retained plus local text, not as a much smaller
largest file. A harness-class fixture, where the runtime member would
dominate, has not been tested.
