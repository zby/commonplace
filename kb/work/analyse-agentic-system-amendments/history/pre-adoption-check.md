# Archive rewrite and bounded split checks

Checked on 2026-10-02 for the operator's commission to run the rewrite and
update bounded fixtures. These are workshop copies and scripted checks of
the proposed rules. They supply pre-adoption evidence; the live record
contract and checker have not been amended by this work.

## Archive rewrite

The [PageIndex copies](./rewrite-check/AAS-2026-09-29-pageindex-02/overview.md)
and [Instinctual Memory copies](./rewrite-check/AAS-2026-09-30-instinctual-memory-02/overview.md)
contain all four Markdown members from each archived set. Runtime IDs were
prefixed with `RT-` throughout authored prose and metadata before the identity
rewrite. Source quotations and fenced excerpts remain byte-identical to the
archive. No archive file changed; each still matches its HEAD blob.

Only identity descriptions and reconciliation identity dispositions changed
beyond ID normalization. The copies retain historical type paths and other
method-era fields. They are record-check fixtures, not new completed analysis
sets: their acceptance here is reference resolution, not validation against
the current member schemas. No ARTIFACT manifest was copied or generated.

- `AAS-2026-09-29-pageindex-02`: 53 declared IDs including the source register; 3 `Part of:` declarations; no unresolved references. The in-memory missing-target variant is rejected as `epistemic.md: unresolved record RT-OBJ-999`.
- `AAS-2026-09-30-instinctual-memory-02`: 34 declared IDs including the source register; 4 `Part of:` declarations; no unresolved references. The in-memory missing-target variant is rejected as `epistemic.md: unresolved record RT-OBJ-999`.

| Set | Record | Declared parent |
| --- | --- | --- |
| PageIndex | EPI-OBJ-1 | RT-OBJ-1 |
| PageIndex | EPI-OBJ-3 | RT-OBJ-3 |
| PageIndex | EPI-RTE-1 | RT-RTE-1 |
| Instinctual Memory | EPI-OBJ-1 | RT-OBJ-2 |
| Instinctual Memory | EPI-OBJ-2 | RT-OBJ-2 |
| Instinctual Memory | EPI-OBJ-4 | RT-OBJ-3 |
| Instinctual Memory | EPI-RTE-1 | RT-RTE-4 |

Seven declaration-level possible-duplicate descriptions become explicit parts.
The two actual duplicate supersessions remain unchanged apart from `RT-`
normalization: `MEM-RTE-2` by `RT-RTE-1`, and `MEM-RTE-4` by `RT-RTE-6`.
The checker resolves every referenced ID, but supersession identity remains a
semantic assessment, not a property that reference resolution proves.

Multi-route groupings keep their comparisons: PageIndex's `EPI-RTE-2`
participates in `RT-RTE-1` and `RT-RTE-3`; its `MEM-RTE-1` supplies metadata
in `RT-RTE-2` and protocol variants on `RT-RTE-5`. Instinctual Memory's
`MEM-RTE-1` and `MEM-RTE-3` retain their cross-route groupings, as do its
`EPI-RTE-2` and `EPI-RTE-3`. None receives a single-parent relation.
In particular, assigning PageIndex's `MEM-RTE-1` only to `RT-RTE-2` would lose
its explicitly retained protocol-variant scope.

The negative check replaces one parent with `RT-OBJ-999` only in memory;
negative copies are not retained. Both are rejected. Existing reference
resolution therefore covers an undeclared parent; a new target-resolution
check is unnecessary. Proposed field-syntax and self-reference checks still
need implementation under A4.

## Bounded workflow fixtures

`test_split_dispositions_preserve_members_and_publish` in
[the workflow tests](../../../tests/commonplace/lib/test_agentic_workflow.py)
is parameterized over three cases:

- `declared-split`: the epistemic member declares two parts of `RT-OBJ-1`;
  reconciliation supersedes the combined record by those IDs, without
  declaring anything itself or starting a memory correction round.
- `memory-return`: reconciliation returns a missing policy part; the memory
  correction declares it, and the next reconciliation supersedes the
  combined record by the two memory parts. The retained memory bytes match
  the accepted corrected report.
- `unresolved-part`: returns are exhausted without a supported declaration;
  the last reconciliation receives `may-return = no`, retains an
  `Unresolved conflict:` with the combined ID, evidence and prevented
  conclusion, and synthesis carries that conflict into Limitations. No
  extra memory round is launched.

Each case must reach Done, publish exactly once, preserve runtime and epistemic
member bytes, retain the expected reconciliation disposition, and publish a
byte-identical retained set. Scripted workers supply all findings and verifier
judgments. Passing these fixtures demonstrates workflow handling; it does not
establish that a model will choose the right identity relation or discover a
missing part. That remains the purpose of the later fresh analysis.

## Verification and next step

`uv run pytest -q` passed all 1,307 tests in 76.90 seconds. After refining the
scripted missing-part return text and adding the store part's explicit parent,
the final targeted run passed all three cases (88 other workflow tests
deselected). `uv run ruff check tests/commonplace/lib/test_agentic_workflow.py`
also passed.

The rewrite supports the proposed part/split rules. A1 refusal hints and range
detection remain pending. After the bounded checks pass, adoption must update
the live contract and job texts and implement the proposed field-syntax check.
The amended method must be committed before opening the fresh analysis,
which pins that commit. The operator has commissioned these pre-adoption
checks; this work does not select a target for the later analysis.

## Archive provenance

SHA-256 of the original Markdown members, independently checked against HEAD:

| Original member | SHA-256 |
| --- | --- |
| AAS-2026-09-29-pageindex-02/runtime.md | `7d7ecfdbb84a8fca2fb4edb117dd2fc0f7c4e92174f851965ab857a86ae2b25e` |
| AAS-2026-09-29-pageindex-02/memory.md | `6bd03521c589433b8b014a5f6a547d65411575c5d5c3e351cb120ddab5a9ab5b` |
| AAS-2026-09-29-pageindex-02/epistemic.md | `b932b30f779c690a6cdf47a3f79f25feac25db7f780b532dde609e0f66f95520` |
| AAS-2026-09-29-pageindex-02/overview.md | `a6ae1b22335291812daa2ce3676d90f2d9c40cf4c58bb9b44c70837a6f667fd6` |
| AAS-2026-09-30-instinctual-memory-02/runtime.md | `83f57ac2ea000c71dbbda2fbb4afbbcd057f71b42e6afc685d0841ccae1928d1` |
| AAS-2026-09-30-instinctual-memory-02/memory.md | `54019a9353f8b3045ae99fc9c693f61137a58860f3b470ab656eab69bdec9bc1` |
| AAS-2026-09-30-instinctual-memory-02/epistemic.md | `190f975a5efe88efa0ae935d2316d6007d5f638f8060ce7cb0afc0befdb09ec5` |
| AAS-2026-09-30-instinctual-memory-02/overview.md | `a3bfaeff1d032eb59a10375e6f46dc5a3d46932e00021561977c52306c20d47b` |
