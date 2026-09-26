# Check comparison and synthesis coverage

Historical initial pilot, before ADR 093 adopted per-value evidence. The results,
contracts and counts below belong to that frozen first trial.

## What must remain possible

The historical `kb/agent-memory-systems/systems.csv` contains 155 rows and 55
columns. The live reader uses 14 normalized axes with separate assessment,
evidence basis, and canonical-record references. These contracts differ;
column-name equality and unchanged counts are not acceptance criteria.

The following map comes from the historical CSV header and the current
`src/commonplace/lib/systems_matrix.py` contract, not historical system findings.

| Historical field family | Current evidence field | Acceptance query |
|---|---|---|
| `storage_substrate` | `storage_substrate` | Decode JSON value sets; count membership once per eligible system. |
| `representational_form`, `form_*` | `representational_form` | Natural language, symbolic, and parametric membership. |
| `lin_*` | `lineage` | Authored, imported, trace-extracted, and other-compiled membership. |
| `auth_*` | `behavioral_authority` | Separate knowledge, instruction, enforcement, routing, validation, ranking, and learning. |
| `wa_*` | `write_agency` | Manual and automatic membership. |
| `op_*` | `curation_operations` | Consolidate, dedup, evolve, synthesize, invalidate, decay, promote. |
| `trace_learning` | `trace_learning` | Count qualified write routes; do not translate this field into improved capacity. |
| `ts_*` | `trace_source` | Session logs, tool traces, event streams, trajectories. |
| `df_*` | `distilled_form` | Natural language, symbolic, parametric derivatives. |
| `ls_*` | `learning_scope` | Per-task, per-project, cross-task. |
| `lt_*` | `learning_timing` | Online, offline, staged. |
| `read_back_direction`, `rb_pull`, `rb_push` | `read_back_direction` | Pull and push membership and overlap. |
| `sig_*` | `read_back_signal` | Coarse, identifier, inferred lexical/embedding/judgment selection. |
| `rb_faithfulness_tested` | `faithfulness_tested` | Preserve uncertainty separately from supported yes/no. |
| `read_back_notes` | Axis rationale and canonical result routes | Read retained evidence for qualitative explanation; no standalone CSV notes column. |
| `public_repo`, `clone_path`, `one_line` | `source_identity`, source register, `one_line` | Source identity and retained bytes replace a local checkout dependency. |

The producer also records new identity fields: public-review and exact-result
hashes, run, revision, cutoff, boundary, tier, and memory comparison scope.
Those are prerequisites for comparing refreshed results without blending
different source versions or silently counting repeated runs twice.

## Checks to execute after publication

- Pass the identical explicit review list to `scripts/build_systems_matrix.py`,
  `scripts/render_systems_table.py`, and `scripts/analyze_matrix.py`. Write trial
  artifacts separately from the full-corpus comparisons.
- Verify matrix values, assessments, bases, and canonical IDs against every
  selected result; verify the table records the same input identities.
- Recompute selected memberships and overlaps from a frozen synthesis bundle.
  Eligible positive counts require code-grounded, known values at wired,
  observed, or causally supported basis. Report exclusions beside denominators.
- Run summary generation through
  [`synthesize-agent-memory-landscape`](../../instructions/synthesize-agent-memory-landscape/SKILL.md).
  Preserve the bundle identity and executable query/output ledger. Qualitative
  claims require reading full retained records, not only CSV fields.
- Test rejection of a missing or ineligible review and preservation of the
  previous output bytes on failure. Do not modify a published input for a test.

The numerical analyzer computes normalized entropy over complete value sets.
That is not the same statistic as entropy over each old boolean column. A
membership query can recover the old kind of binary count from an eligible
value set, but the old and new analyzer outputs must not be presented as a
longitudinal numerical series without reconciling these units and evidence
filters. This pilot checks output capabilities, not historical number equality.
Its mutual-information function returns zero for fewer than five paired rows.
A three-system pilot therefore checks that path executes, but cannot establish
the validity or usefulness of its redundancy diagnostics. Likewise, no
document-only case is selected initially: tier separation is part of the
contract, but needs a later document-grounded pilot.

## Executed checks

On 2026-09-26, both matrix builder and table renderer were called with a missing
main review and, separately, a legacy review path. All four calls exited 1.
The errors distinguished file absence from `not a main-review path`. Each test
started with an existing temporary output containing `previous-output`; its
bytes were unchanged after the rejected call. No published input was modified.

The unbounded `uv run python scripts/analyze_matrix.py` also exited 1 on
2026-09-26: `kb/agentic-systems/reviews/pond.md: missing or mismatched retained
result; regenerate the main review`. This is an observed corpus prerequisite,
not a defect in the current pilot targets. The explicit pilot population must
not be presented as a full-corpus rebuild, and the current public comparison
files are not thereby certified fresh.

The first positive smoke check selected only the completed Napkin review. The
matrix builder, table renderer, and numerical analyzer all exited 0; the first
two emitted one code-grounded row to the ignored pilot cache. The analyzer
reported weaker `afforded` assessments separately from wired values. This
establishes one-result compatibility, not the final three-result trial or
equivalence to historical classifications.

Selecting the Napkin review twice was also rejected (exit 1, no output file):
`multiple selected reviews of source https://github.com/Michaelliv/napkin;
choose one boundary explicitly`. Repeated selection cannot inflate the system
count through that path.

All three pilot analyses have now published and passed checked handoffs.

The first synthesis bundle preparation failed because Napkin's retained result
links three ontology definitions not included by the default capture. Repeating
the command with the supported `--ontology` arguments for `theory-builder.md`,
`reflective-system.md`, and `self-improving-system.md` succeeded. This is a
required input-discovery step for future bundles, not grounds to strip valid
links from an immutable analysis. No script change was needed.

The explicit three-result bundle was frozen before interpretation:

- Local trial bundle: `kb/reports/cache/agentic-memory-refresh/2026-09-26-pilot/bundle`.
- Manifest SHA-256: `844f158f87906823765feb7371be95afc54929f3bdb6c28cb71aecb7c3d3bb82`.
- Matrix SHA-256: `d0901f96a8f43605f43e63a97a3f7a1eea21426c74244e96786ca3f17e2a7f95`.
- Population: Dynamic Cheatsheet, Mem0, Napkin; three code-grounded results,
  all with analysis cutoff 2026-09-26. Selection is explicit, not all-generated.
- Repository revision recorded by the bundle: `26fbe60caa5431b958a7f01569b404ffa1978bc9`.
  This revision alone does not contain the newly created result bytes; the
  temporary bundle is the exact evidence for this workshop trial.

The complete three-result matrix builder, table renderer, and numerical
analyzer all exited 0. The generated matrix equals the bundled matrix byte for
byte. All 42 axis profiles were checked against their result frontmatter:
values, assessment, evidence basis, and canonical-record references matched.
The table records the same three run/source identities and all six input hashes.

The [executable query ledger](./query-ledger.md) contains all fourteen dimension
membership counts plus six focused queries, including exclusions and eligible
run IDs. Re-executing its code produced identical output. The
[bounded synthesis trial](./synthesis-trial.md) used full bundled results and
canonical records. Its author checked its own claims; no independent semantic
review was commissioned. Current-source bundle verification passed immediately
before the workshop trial was written.

Trial output directory: `kb/reports/cache/agentic-memory-refresh/2026-09-26-pilot/`.
It contains `memory-systems.csv`, `memory-systems-table.md`, `statistics.txt`,
`query-output.jsonl`, and the frozen `bundle/`. These ignored outputs support
the workshop trial; the historical and full-corpus public comparisons were not
replaced. The published per-system results are retained under their normal
skill-owned paths.

## Acceptance decision and next batch

The end-to-end producer and consumer mechanics pass for these three cases.
Statistical parity is conditional. Query Q3 (wired automatic writing and push)
has zero eligible rows because every write-agency union has afforded basis;
this is not evidence that no automatic writing exists. Mem0 and Dynamic
Cheatsheet explicitly retain wired automatic routes alongside afforded manual
input. Mem0's wired internal push is also hidden from the strong-value count
when combined with afforded application pull. Lineage has the same aggregate
coverage loss in all three rows.

The initial proposal (subsequently adopted as
[ADR 093](../../reference/adr/093-memory-comparisons-keep-evidence-per-value.md))
recorded the alternatives: keep complete-profile statistics with this limit, retain
finer evidence, or define narrower comparison questions. Resolve or explicitly
accept that limitation before bulk refresh. A changed contract requires new
pilot runs and another acceptance check; do not patch these retained results.

After that decision, the next batch should test a document-grounded target,
replacement of an existing generated review (Pond is already an observed
unbounded-reader prerequisite), and enough additional code-grounded cases to
reach the analyzer's five-pair redundancy threshold. Merely reaching five rows
does not guarantee five eligible pairs. Broader source availability, every
legacy boundary, and full-corpus completeness remain untested.

The three-system summary supports named mechanism contrasts. Representation
counts require particular care: Mem0 includes model-derived dense encodings as
parametric; Dynamic Cheatsheet classifies its imported numeric access vectors
as symbolic with generation uninspected. These scoped labels must not be read
as prevalence of vector use or model-weight training.

## Producer observations

Napkin completed the independent memory pass, main-result integration, source
verification, publication, and checked handoff. During integration, executable
fallback paths contradicted an overstrong guarantee quoted from a source
comment. The final result explicitly qualified the guarantee and retained the
specialist disagreement in reconciliation. A matching quotation alone did not
establish its attached claim.

Recoverable structural friction included adjacent canonical IDs separated by
em dashes being interpreted as shorthand in Napkin, and ID-leading prose being
interpreted as duplicate declarations in Mem0. Formatting was corrected while
the runs remained running. These observations do not establish a need to change
the schema or validator; no consumer or method code was changed for the pilot.
