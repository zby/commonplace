# Writing conventions for kb/agentic-systems/

## Purpose and quality

This collection holds ordinary authored accounts of external agentic systems,
comparisons and the comparison procedures.
The quality goal for system accounts is fidelity and economy: explain the external
system's native operation before applying Commonplace concepts. Qualify uncertain
mappings. Open authored analyses with their evidence basis and capture boundary.
Memory and knowledge are lenses of whole systems; the agent-memory-systems corpus
is historical. New workflow analyses belong in `kb/agentic-system-analyses/`.

## Placement and ownership

The root holds README.md and COLLECTION.md. `reviews/` holds ordinary authored
accounts. `comparisons/` holds cross-system
analyses and generated tables. `instructions/` owns landscape synthesis and
taxonomy maintenance. `reports/` is frozen history from before the analysis
collection existed; it is excluded from validation and from comparison.
`types/` owns local types for artifacts that remain here. There are no nested
collection contracts. Research skill projections point to canonical instructions;
these skills are not promoted to every initialized KB.

Before editing instructions, shared contracts or local types, follow
[method maintenance](./method-maintenance.md). Use the instruction type's
executability and composition rules when authoring procedures. Supply each worker's required role/type inputs explicitly. Instruction
edits require checking direct callers, callees, conditional loads and result
consumers; update affected interfaces together. Method-maintenance guidance must
be loaded through an explicit instruction-authoring path, not by analyst packets.

## Workflow analyses

Workflow-produced analyses, their method and their publication belong to
`kb/agentic-system-analyses/`. Comparison tools read the current analyses
from that collection's `retained/` area. When a system is regenerated there,
its authored account here is retired with the relocation command.
Ordinary authored accounts remain author-maintained.

Before assessing theory pathways in ordinary authored accounts, read the Theory
account in the [shared record contract](../../../agentic-system-analyses/instructions/agentic-analysis-records.md).
It supplies the independent conditions and separately evidenced properties.

## Scope and titles

Durable analysis excludes current Commonplace differences, adoption advice and
watch items. Those belong in separately commissioned transfer scans under
`kb/reports/state/agentic-system-transfer/`. Transferable claims go to `kb/notes/`,
raw captures to source snapshots, descriptions of Commonplace to `kb/reference/`,
and in-flight work to `kb/work/`.

Descriptive account titles name the system or feature. Argumentative accounts
use a claim-shaped title and the `title-as-claim` trait. Procedures use imperative
titles and trigger descriptions. Comparison titles name their question and scope.

## Outbound links

- Sources: tracked ingests, never snapshots; `derived-from`, `evidenced-by`, `see-also`.
- External: source evidence already used, preferably version-pinned; `evidenced-by`, `see-also`.
- Notes: theoretical mappings; `rests-on`, `defined-in`, rare `is-evidence-for`, `see-also`.
- Agent-memory systems: related subsystem accounts; `contains`, `part-of`, `compares-with`, `see-also`.
- Agentic system analyses: accepted overview/member evidence; `see-also`.
- Reports: separately retained evidence; `evidenced-by`, `see-also`.
- Reference: direct Commonplace analogues; `see-also`.
- Instructions: directly mapped procedures; `procedure`, `see-also`.
- Local instructions: composition, conditions and operation targets; `composition`, `precondition`, `invokes`, `applies-when`, `operates-on`, `rests-on`, `see-also`. Do not use review, archive or workshop links as method execution inputs.

## Type eligibility

Use global types under `types/` or local types under
`agentic-systems/types/`. Frontmatter-free Markdown is text.
