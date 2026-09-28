# Generate citations before inserting them

The operator clarified the intended quotation workflow on 2026-09-27: provide
source text and a frozen source, generate a citation for every occurrence, and
let the author choose one. The generator does not validate documents. There is
no separate agent quotation-checking step; publication uses regular validation.

`commonplace-quote` now implements this for agentic-analysis Git blobs and
checksum-pinned captures. Authors supply a run state, a Git path when relevant,
and selected text through a UTF-8 file or stdin. One match outputs only its
Markdown citation. Two to ten matches output JSON candidates with selection
metadata; more than ten returns an error asking for a longer quote, without
partial output. Every citation copies source text and has derived locations.
When occurrences share
a line, the generated excerpt includes context needed for the existing unique
occurrence rule. Missing text produces an error rather than a fabricated quote.

The generator is separate from publication. `agentic_publication.py` retains
destination checks, artifact identity checks, atomic publication and rollback.
Its separate `verify-sources` operation was removed. Publication already invokes
the regular validator on the prospective complete run and on the written state.

The [validator investigation](./validator-disagreements.md) describes the
pre-repair behavior. Structural attribution checking now uses the shared
parser. Link and ordinary source-anchor scans omit recognized quotation bodies
while retaining their attributions; quotation matching receives original text.
Malformed attributions, ordinary author links, and author-added source anchors
remain subject to their checks.

## Acceptance

- The subsequent simplification passes all 950 tests, including single-citation
  output, the ten/eleven occurrence boundary, no partial CLI output on error,
  and one result-validation pass inside each prepare operation. Ruff and scoped
  document validation pass.
- The initial implementation passed all 942 tests. Added cases cover every occurrence, same-line and
  overlapping matches, multiline whitespace, preserved comment markers,
  changed worktrees, capture integrity and generation without invoking a quote
  validator.
- The publication integration case inserts generated quotes containing a
  relative image, a foreign repository link and a fictional source path.
  Regular bundle validation and publication pass. An author-added invalid
  range still fails regular validation.
- `uv run ruff check src tests` passes. A broader `ruff check .` also visits
  retained historical source bundles and reports existing import-order issues
  there; frozen witnesses were preserved.
- Reinstalled the editable package. The bare `commonplace-quote` command works
  in a fresh initialized project at `/tmp/commonplace-quote-probe-ilze22m3`,
  using the pilot's frozen Dynamic Cheatsheet commit. Repeated initialization
  preserves an existing citation, `--check` passes, and the probe's run state
  validates without warnings.

This is implementation acceptance, not another three-pilot authoring trial.
The generator deliberately uses the existing citation syntax. A source passage
containing an attribution-delimiter line, or a source identity containing a
backtick, is rejected as unrepresentable rather than emitted as a malformed
citation. Semantic support remains the author's responsibility.

## Contract-change packet

| Field | Disposition |
|---|---|
| Authoritative declaration | The operator's commission, amended ADR 094, analysis instruction and result/report types. |
| Scope and enforcement | Construction from the analysis run's frozen Git blob or capture; source reading and derived locations in `quote_generation.py` and `quote_matching.py`. No general KB prose-citation constructor is claimed. |
| Consumer classes | Updated CLI emitter/entry point, coordinator and specialist instructions, global types, command catalogue, ADR, parser/validator consumers and tests. Existing init templates and control-plane templates do not name the removed operation. |
| Byte-pinned consumers | Prior reports, their method hashes and retained source bundles remain historical witnesses. No report bytes are rewritten or re-pinned. |
| Old spellings | Searched `verify-sources`, `verify_sources`, `_SOURCE_REF_RE`, including command instructions and code. Final current-consumer scan has zero hits for each. |
| Generated/projected forms | Editable command installation refreshed. Skill symlinks load the changed canonical instruction. No citation format/schema migration or generated-index change. |
| Fresh install | Temporary `commonplace-init` project consumes the installed command and library; Git-source quotation probe succeeds. |
| Existing installs/clones | Init preserves existing source/citation content; repeated init and pointer check pass. This source checkout uses the editable reinstall, not init. |
| Diagnostic promises | Tests establish absent-text, blank selection, changed capture and unrepresentable-form errors; source integrity is checked during resolution, without document verification. |
| Acceptance probe | Fresh project, bare generator invocation against a frozen source, unchanged old citation after re-init, clean run-state validation; unit and full publication tests above. |
| Drift guard | Existing command-catalogue test discovers entry points and tests each command's help; updated publication tests require standard validation to reject unsupported evidence. |
| Historical witnesses | Prior rerun/RCA records and retained trial bundles retain the removed command as dated execution evidence. They are not current instructions. |
| Identity by convention | Existing run-state paths, source identities and citation grammar stay in force. The new command emits that same grammar. |
| Shared exclusions | `blank_quote_bodies` supplies quotation-body exclusion to both Markdown link discovery and ordinary source-anchor scanning. Source matching retains original bodies. |
| Relocation effects | No artifacts moved; no relocation pins or size gates affected. |

Current-consumer searches covered `src`, `tests`, instructions, reference,
types, and root doctrine. The whole-checkout scan excludes related source
checkouts and the explicitly historical report/workshop areas. The change does
not rewrite analysis bytes, so an ignored-state migration is not required.

## Command count and simplification audit

The baseline is `34dc62e3^`, immediately before the first commit retaining this
workshop. Comparing package entry points gives **25 before, 26 now**. The only
added executable is `commonplace-quote`.

The subsidiary pilot-reliability repair added `verify-sources` in `2d5a9d9a`.
This change removes it. Thus two CLI operations were introduced across the
refresh/repair work, one remains, and the net executable increase is one.
`inspect-destination`, `prepare`, `publish`, and the handoff command already
existed before this workshop; their introducing commits date to September 4–5.
Comparison scripts were modified, not added.

The operator resolved the simplification candidates on 2026-09-27:

1. **Keep prepare.** It remains a useful dry run; its command and the current
   workflow are retained.
2. **Remove duplicate checks inside `_check_bundle`.** Removed the direct result
   validation wrapper and explicit comparison check. Regular validation of the
   prospective complete run owns those checks. Identity/shape reads needed to
   construct the prospective run remain. Publication also keeps its distinct
   field-presence requirement for `memory-comparison`; ordinary validation
   permits historical results without that field.
3. **Limit selection metadata to ambiguous quotations.** A unique match outputs
   only its citation. Multiple matches retain location and selection metadata.
   The chosen ambiguity limit is ten; a larger set requires a longer quote.

The post-write state check remains: it verifies actual written artifacts rather
than just prospective bytes. Destination collision handling and rollback stay
in the publication module; those operations are outside regular validation.
