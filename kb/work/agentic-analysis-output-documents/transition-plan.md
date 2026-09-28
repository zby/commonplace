# Transition plan: from one result to the member set

Step 3 of the [workshop](./README.md). Built on the
[consumer inventory](./consumer-inventory-20260928.md), the confirmed
[partition candidate](./partition-candidate.md) and the
[draft contracts](./contracts/README.md). It fixes what changes in the
producer, the validators, the consumers and the tests, the order of the
work, and the one decision that is the operator's.

## The finding that reframes historical results

Only three of the forty generated reviews load under today's contract:
the three 2026-09-27 pilots. The other thirty-seven fail validation on
the pre-ADR-093 profile shape, so the default matrix build already
raises and the committed comparison CSV cannot be regenerated. The
workshop's rule that restructuring preserves historical results is
already satisfied the only way it can be: the retained bytes stay, and
the consumers read the current shape only. Sixty retained single-file
results remain as they are, under the retired type, readable by a person
and unreadable by the loaders, exactly as thirty-seven of them are now.

Decision proposed: no compatibility code and no migration. The
corpus-refresh workshop regenerates reviews under the new producer, as
it was going to. The three current pilots are re-run under the new
producer in step 4 rather than converted, so every set in the corpus was
produced by the method. This is the operator's call because it accepts
that, between the producer change and the next refresh, no review loads.

## Producer changes

**Run state.** The `result` mapping becomes `overview`, pinning
`<run-id>/overview.md`. The run state pins nothing else; the overview's
manifest pins the members. Schema, `_output_identity`, the expected-path
check, the state dataclass, `_render_final_state` and the receipt
comparison follow. The reserved candidate names gain `overview.md`,
`runtime.md`, `memory.md`, `epistemic.md`.

**Coordinator outputs.** The skill's step 7 writes four members instead
of one result. The overview's manifest is written last, after the other
three are final, since it carries their hashes. `memory.md` is authored
by the coordinator as the local report with the Reconciliation mapping
applied by exact-token replacement, seeded re-declarations turned into
`On <ID>` annotations, and an `## Amendments` section appended. No new
command: finalization is authored, and its integrity is verified.

**Finalization integrity check**, in run-state verification. Read the
local `memory-report.md`, apply the mapping table from the overview's
Reconciliation and the re-declaration rewrite, and require the result to
equal `memory.md` up to its `## Amendments` section and its
`finalized-from` field; require `finalized-from` to equal the local
report's hash. This replaces the current memory-report projection lines
in the result body and makes the derivation checkable rather than
trusted.

**Set verification**, in run-state verification and publication. Verify
the manifest (existence, hash, type of each member); verify identity
fields across members against the overview; run source and quote anchor
resolution on every member and the review; build the declaration union
across members and fail on a duplicate or an unresolved reference in any
member or in the profile; require the memory member's `report-status`
to be `complete`; require at least one attributed quote across the set.

**Publication.** `_check_bundle` reads the disposition from the overview
and the profile from `memory.md`; prepare validates every member as its
retained path; publish retains the four members, backs up the incumbent
set under `incumbent-<member>.md`, and writes the review with
`analysis-overview` and `analysis-overview-sha256`.

**Site.** `properdocs.yml` publishes the four member names instead of
`result.md`.

## Validator changes

**Types and schemas.** The five draft contracts move to `kb/types/`
(the review type to `kb/agentic-systems/types/`) with schemas: the
overview's eleven-minus-three sections and the `members` manifest; the
runtime report's sections; the memory report's sections plus
`finalized-from`; the epistemic report's six sections; the review's
frontmatter. The result type is retired with a redirect.

**Records.** `record_reference_errors` gains a set mode: declarations
are level-four headings under the six kind headings in any member,
annotation headings are neither declarations nor errors, `SRC-*`
declarations come from the overview's register, and references are
checked against the union. The single-file mode stays for a member
validated alone, checking only shorthand and the member's own
duplicates, since a member cannot know the set's declarations.
`validate_comparison` takes the union instead of one section.

**Type rules.** The evidence-and-references rule runs on the runtime,
memory and epistemic types; the quote-minimum rule applies to the set,
not to each member, since the epistemic member cites and does not quote.
The comparison rule runs on the memory type only.

## Consumer changes

**Matrix loader.** `retained_overview_path` replaces
`retained_result_path`; `load_results` verifies the review pin, opens
the overview, verifies the manifest, takes identity from the overview,
the register text from the overview, the profile from `memory.md`, and
validates each member. The CSV's `result_file` and `result_sha256`
columns become `overview_file` and `overview_sha256`. The three scripts
follow the loader; the table's link points at the overview.

**Landscape bundle.** Copies every member; `METHOD_INPUTS` lists the
member types and schemas.

**Init repin.** The regex matches `analysis-overview-sha256`. Rewriting
a member's type line changes its hash, so the repin must cascade:
recompute the manifest entry in the overview, then the overview's hash,
then the review pin. Alternatively init stops rewriting type lines inside
retained analysis directories, treating them as frozen bytes. The second
is simpler and matches the retained-bytes rule; it is the recommended
choice and an open item for the operator.

**Skills and contracts.** The transfer-scan and landscape-synthesis
skills name the overview and say which member holds what: boundary,
register, reconciliation, synthesis and limits in the overview; runtime
account and runtime records in the runtime report; memory findings and
profile in the memory report; epistemic blocks in the epistemic report.
The collection contract and the comparisons README promise the overview
pin and the retained set. The analysis skill's steps 1, 7, 8 and 10 name
the members.

## Order of work

Each item is one commit with its tests; the suite stays green throughout
except between items 6 and 7, which land together.

1. Types and schemas for the four members and the review; result type
   retired with a redirect. Composition and type tests updated.
2. Records set mode and comparison union, with unit tests on a small
   fixture set.
3. Run-state schema and parsing: the `overview` pin.
4. Run-state verification: manifest, identity, anchors on every member,
   finalization integrity, set-wide records.
5. Publication: bundle check, prepare, publish, incumbents, review pin.
6. Matrix loader, scripts, bundle, init repin.
7. Skill steps, memory instruction, epistemic instruction, collection
   contract, comparisons README, site config.
8. Step 4 trial on one target with source pin and functional scope fixed.

The one-off fixture script is deleted with item 1, since the draft
contracts supersede it.

## Open items for the operator

- The historical-results decision above.
- Init repin: cascade, or freeze retained analysis directories.
- Whether the trial target should be a harness-class system, to see the
  runtime member dominate for the first time.
