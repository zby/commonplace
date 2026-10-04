---
description: "Job of an analyse-agentic-system run: trace and challenge the runtime baseline and write the set's runtime member"
type: types/instruction.md
---

# Trace and challenge the runtime baseline

Read every file under `read-first` in your invocation before any other step.

## Job parameters

Common parameters are defined in the supplied worker rules.

| Name | Meaning | Present |
|---|---|---|
| `boundary` | Absolute path of the frozen boundary and Source register. | Always |

## Task

Write the runtime member to `output` under the supplied runtime type,
within `boundary`. It gives the later specialists their starting account.
No job rewrites it afterwards.
Declare runtime-owned records with `RT-` under the shared record contract.

1. Begin with consequential claimed work and shipped entry paths. Trace one
   ordinary invocation end to end and record it with the fields the type's
   Runtime account requires.
2. Enumerate materially equivalent alternate paths before judging a
   guarantee: direct model calls, provider-native tools, host callbacks,
   shell access, extension code, subprocesses or remote workers, manual
   graph control, and durable variants where present. A guarantee covers
   only the paths its enforcement point covers.
3. Inspect the smallest warranted set of forcing cases in the source,
   ordinarily two to four for a full code-grounded analysis. Use supplied
   execution evidence when available; state what remains unobserved.
4. Record material routes under the shared record contract and load-bearing
   guarantees under the runtime type. Audit each route's read-back fields
   and applicability reasons before submitting.
5. Distinguish the capability surface, current grant set, and deployed
   isolation envelope. Inspect permissions, approval, delegation, dynamic
   extension, reliability, observability, providers, packaging, and
   performance only where they change claimed work, a control path, evidence
   strength, or a result of the memory or epistemic analyst.
6. Inventory the distributed-parametric components used by inspected routes
   (LLMs, embedding models, parametric routers, critics and adapters) as
   `RT-CMP-*` records with the shared component fields.
7. Inspect materially distinct mechanisms that admit changes to the product,
   retained knowledge or instructions, capabilities, or production
   machinery. Record each on its admitting `RT-RTE-*` record with the
   conditional fields the shared record contract requires. Leave memory
   revisions to the memory analyst; the reconciliation attaches them.

Acceptance requires a valid member whose citations resolve against its
own declarations and the Source register of `boundary`.

Run the acceptance check before submitting.
