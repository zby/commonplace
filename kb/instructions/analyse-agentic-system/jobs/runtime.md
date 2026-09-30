---
description: "Job of an analyse-agentic-system run: trace and challenge the runtime baseline and write the set's runtime member"
type: types/instruction.md
---

# Run and challenge the runtime baseline

Write the set's runtime member, `output/runtime.md`, under the [runtime report type](../../../types/agentic-system-runtime-report.md): the runtime account, probe evidence, and the records the runtime analyst declares, with IDs of the form `OBJ-1` or `RTE-1`: no `MEM-` or `EPI-` prefix, which belong to the memory and epistemic analysts. The memory and epistemic analysts start from it, and no job rewrites it afterwards. Work within the boundary and source register of `boundary.md`.

1. Begin with consequential claimed work and shipped entry paths. Trace one ordinary invocation end to end and record it with the fields the type's Runtime account requires.
2. Enumerate materially equivalent alternate paths before judging a guarantee: direct model calls, provider-native tools, host callbacks, shell access, extension code, subprocesses or remote workers, manual graph control, and durable variants where present. A guarantee covers only the paths its enforcement point covers.
3. Trace the smallest warranted set of forcing cases, ordinarily two to four for a full code-grounded analysis. Prefer static inspection. Before any dynamic check, write its execution-preflight record and verify tools, packages, services, credentials, configuration, and authority.
4. Record an executed check as a `SRC-*` probe evidence capsule.
5. Record each material route and load-bearing guarantee with the fields the type's Runtime account and Routes records require, then audit every `RTE-*` record for the read-back fields the Routes records list. A route that neither retains material nor reads retained material back records those fields as `inapplicable`, with the reason.
6. Distinguish the capability surface, current grant set, and deployed isolation envelope. Inspect permissions, approval, delegation, dynamic extension, reliability, observability, providers, packaging, and performance only where they change claimed work, a control path, evidence strength, or a result of the memory or epistemic analyst.
7. Inventory the distributed-parametric components used by the inspected runtime routes (LLMs, embedding models, parametric routers, critics, and adapters) as `CMP-*` records. Each states, with its own evidence status, whether the component's parameters can change while the system runs, whether it is pinned to an exact version, and whether its name can resolve to a different model later.
8. Inspect materially distinct mechanisms that admit changes to the product, retained knowledge or instructions, capabilities, or production machinery. Record each on its admitting `RTE-*` record with the admission, decision-role, answer-oracle, operating-mode, and guidance fields the type requires. Leave memory revisions to the memory analyst; the reconciliation attaches them.

Your output is refused while it is not a valid member or cites a record that neither it nor the Source register of `boundary.md` declares. The memory and epistemic analysts declare their own records; corrections to your records are amendments in the overview's Reconciliation, not edits of this member.
