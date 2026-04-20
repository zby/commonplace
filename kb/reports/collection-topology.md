---
description: "Compiled collection topology — registers and linking rules. Rebuild with cp-skill-compile-collections."
type: kb/types/note.md
status: current
---

# Collection topology

## Collections

| Collection | Register / layer | Quality goal | Titles |
|---|---|---|---|
| `kb/notes/` | theoretical | reach | claim by default |
| `kb/reference/` | descriptive | fidelity + economy | topical; ADRs numbered |
| `kb/instructions/` | prescriptive | executability + precision | imperative or action-oriented |
| `kb/agent-memory-systems/` | descriptive, with root-level analysis exceptions | fidelity + economy | repo-name for reviews; topical or claim-shaped for analyses |
| `kb/work/` | catch-all workshop layer | move active work forward; extract durable conclusions | not specified |

## Linking Matrix

What relationships to use when linking FROM a source register or layer TO a target register or layer.

| From -> To | Theoretical | Descriptive | Prescriptive | Workshop |
|---|---|---|---|---|
| **Theoretical** | since / because / contradicts / extends / qualifies | evidence / derived-from / exemplifies | evidence (rare) | not specified |
| **Descriptive** | rationale / grounds / evidence | cross-reference / see-also / supersedes | procedure | not specified |
| **Prescriptive** | justification | reference | composition | not specified |
| **Workshop** | permissive: whatever label clarifies work state | permissive: whatever label clarifies work state | permissive: whatever label clarifies work state | permissive: whatever label clarifies work state |

For workshop links, examples include `draws-on`, `tests`, `depends-on`, `produces`, `supersedes`, or a local phrase. Workshop links are working notes, not durable graph contracts.
