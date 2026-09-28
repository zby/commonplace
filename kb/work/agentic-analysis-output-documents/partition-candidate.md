# Partition candidate: overview, runtime, memory and epistemic members

Step 2 of the [workshop](./README.md). This document settles how shared
records are owned across several files before it draws the files, then
proposes the member set, the completion rule, and the fixture test that
decides whether the candidate holds. Nothing here changes a shipped contract.

## Where the words are

Whitespace-separated words per section of the three fresh retained results
(runs `dynamic-cheatsheet-04`, `mem0-04`, `napkin-05`, 2026-09-27):

| Section | Dynamic Cheatsheet | Mem0 | Napkin |
|---|---:|---:|---:|
| Frontmatter, almost all `memory-comparison` | 1,173 | 1,292 | 1,125 |
| Run identity, boundary, source register | 414 | 404 | 433 |
| Shared records, of which routes | 4,834 / 3,232 | 7,213 / 4,287 | 7,330 / 4,091 |
| Runtime account | 523 | 869 | 538 |
| Lens scoping | 121 | 138 | 172 |
| Memory/context lens | 905 | 955 | 940 |
| Epistemic lens | 2,370 | 2,289 | 2,914 |
| Reconciliation | 299 | 316 | 391 |
| Bounded synthesis, limitations, verification | 1,089 | 1,027 | 908 |
| Total | 12,593 | 14,862 | 14,770 |
| Local specialist report, not retained | 5,451 | 8,622 | 7,703 |

Three observations drive the design. The canonical records are half the
result and routes are most of that. The memory/context lens section is the
coordinator's re-narration of the specialist's report with canonical IDs, so
the same findings exist twice, once locally and once retained. The epistemic
lens is a self-contained block of two to three thousand words that only
annotates IDs.

## Ownership model

The README's own candidate is that each report owns its evidence and
findings and other reports reference rather than copy. Two models satisfy
that sentence; this candidate chooses the second.

**Central register.** One member declares every canonical record and holds
every evidence passage; the lens members hold only interpretation. Clean
ownership, but the register member stays at five to seven thousand words,
and the specialist's report must be taken apart to move its quotes onto
records it did not declare. That is the "equally large common-record
document" the README warns against.

**Distributed register, chosen.** The run has one ID namespace. A record is
declared exactly once across the set, in the member that established it:

- the runtime member declares the records the coordinator's runtime pass
  registered, which are the seeds the memory input carries;
- the memory member declares the records registered from specialist
  proposals, under their canonical IDs;
- the epistemic member declares nothing; a rare epistemic proposal is
  registered by the coordinator in the runtime member.

An evidence passage occurs once across the set, in the member whose finding
it supports. A member that needs a passage another member already holds
cites the record instead. The specialist's quotes on seeded records stay in
the memory member under its annotation of that record, because the finding
they support is the memory finding; the coordinator removes only exact
duplicates at finalization and records each removal.

An amendment attaches to the declared record in its declaring member, with
the superseded value, replacement, evidence anchor and affected findings, as
the result type already requires. Anchored conflicts stay as amendment
entries carrying both values. The overview's Reconciliation lists the
proposal mapping and every disposition, as today.

A cross-member reference is the bare ID. The overview's manifest makes the
set resolvable, and set validation checks that declarations are unique
across members and that every reference resolves to one declaration in the
set. Nothing in the reference syntax changes.

## Member set

All members live in the run directory and are retained together under
`kb/reports/retained/agentic-system-analysis/<run-id>/`.

**`overview.md`**, new type. Frontmatter: today's identity fields (`run-id`,
`system`, `run-date`, `result-disposition`, `target-class`,
`boundary-kind`, `reviewed-boundary`, `analysis-cutoff`, `evidence-tier`)
plus a `members` manifest: for each member its path, SHA-256 and type. No
`memory-comparison`. Sections: Run identity, Boundary and evidence, Source
register, Lens scoping, Reconciliation, Bounded synthesis, Limitations,
Verification and blockers. About two thousand words on the fixtures.

**`runtime.md`**, new type. The Runtime account with its preflight records
and probe capsules, then the declared records under the six subheadings,
with their evidence. Its size follows the target: large for an agent
harness, small for a memory system whose routes the specialist established.

**`memory.md`**, the existing report type finalized. The specialist's
report with canonical IDs applied by exact-token mapping, amendments
appended under the affected records, and the `memory-comparison` profile in
its frontmatter as the authoritative comparison input. It keeps the
specialist's `worker-model`, `method-sha256` and
`canonical-register-sha256`, and gains `finalized-from`, the SHA-256 of the
local `memory-report.md` it was derived from. The local report remains
provenance in the run directory; the finalized member is the retained
artifact. The result's memory/context lens section disappears: its content
is this member plus the synthesis.

**`epistemic.md`**, new type. The six blocks exactly as the result type's
Epistemic lens contract now states them, with identity frontmatter. Written
by the coordinator or an epistemic worker straight into the member.

The compact review is unchanged in shape and pins the overview instead of
the result.

Projected sizes on the Napkin fixture: overview about 1,900 words, runtime
about 3,500, memory about 7,000 after duplicate-quote removal, epistemic
about 2,900. The largest member halves against today's 14,770-word result.
The set totals about 15,300 words against today's 14,770 retained plus 7,703
local, because the local report's content stops being retained twice. On an
agent-harness fixture the runtime member would dominate instead; the
Dynamic Cheatsheet fixture, with twenty-nine of thirty-one quotes on
runtime-registered records, is the case to check.

## Completion rule and rejection

Completion is a chain of pins. The run state binds the overview's path and
SHA-256, as it binds the result today. The overview's manifest binds every
other member. The compact review pins the overview's path and SHA-256.
Downstream readers open the review, follow the pin to the overview, and
verify the manifest before reading any member.

A reader rejects the set, and reports which check failed, when:

- a manifest member is missing, or its bytes do not hash to the manifest;
- a member's `run-id`, `reviewed-boundary` or source identity differs from
  the overview's;
- the overview's disposition is not `complete`, or the memory member's
  `report-status` is not `complete`;
- a canonical ID is declared in two members or referenced without a
  declaration anywhere in the set;
- a member's own validation fails.

A `blocked` or `out-of-scope` run produces the overview alone with an empty
manifest and no review, which keeps today's regime.

## Consumers that change

From the live code and skills: publication (review frontmatter check,
retained copy, incumbent inspection), the matrix loader (reads the result's
frontmatter profile and Source register, validates the result), the
handoff renderer, the run-state verifier of the memory report, the
init-time pin rewriter, the transfer-scan skill and the landscape-synthesis
skill. Twenty-eight code and skill references name the single result path.
Step 3 plans the transition; this document only notes that every consumer
must move from "read the result" to "verify the manifest, then read the
member it needs", and that the matrix loader's profile source becomes the
memory member.

## Against the acceptance criteria

- **Largest document**: halves on the memory-system fixtures; to be
  measured on a harness fixture.
- **Duplicated evidence**: the local report's second copy of the memory
  findings and quotes is gone; runtime and epistemic members never
  duplicated. The remaining duplication risk is a passage quoted by both the
  runtime pass and the specialist, removed at finalization.
- **Duplicated requirements**: each member has one type contract; the
  overview and runtime contracts are cut from the cleaned result type, not
  written anew.
- **Instructions each worker loads**: the specialist loads the report type
  and four result-type sections today; after the split it loads the report
  type and the runtime type's record grammar. The epistemic worker loads
  the epistemic type only.
- **Added coordination cost**: finalization of the memory member is one new
  mechanical step with a disclosed derivation; the manifest is one new
  frontmatter block; set validation is one new check.

## Open choices

- Whether `runtime.md` should further split declared records from the
  runtime account. Not until a reading boundary shows; a harness fixture
  may show one.
- The review's pin field name: keep `analysis-result` pointing at the
  overview, or rename to `analysis-overview`. No consumer outside this
  repository reads it, so renaming costs only the migration step 3 already
  plans.
- Whether the finalized memory member keeps the specialist's section order
  or is reordered to match the runtime member's record grammar. Keeping the
  order preserves the derivation as a pure ID rewrite plus appended
  amendments.

## Next: fixture test

Split `napkin-05` and `dynamic-cheatsheet-04` by script along these rules,
using each result's Reconciliation mapping to assign records to the runtime
or memory member and the local specialist report as the memory member's
source. Then check: every reference resolves within the set, no ID is
declared twice, the set of quote passages equals the union of the result's
and report's passages with exact duplicates removed, and each member
validates against a draft contract. Record the member sizes, the number of
passages removed as duplicates, and every place where a finding in the
result's memory/context lens section has no home in the memory member or
the synthesis. That last count is the test of whether the re-narration
carried anything the specialist's report did not.
