---
type: types/type-spec.md
name: agentic-system-synthesis
description: "The synthesizer's public account of one analysis run: retrieval description, bounded synthesis and limitations, retained as a set member"
schema: ./agentic-system-synthesis.schema.yaml
---

# Agentic system synthesis

The public account of one analysis run, written after the records have
passed independent verification. It is the set's `synthesis.md` member,
linked from the [overview](./agentic-system-analysis-overview.md). The
overview uses its retrieval description but does not copy its body. The
[record contract](../instructions/agentic-analysis-records.md) governs the
records it cites and what its findings may claim from evidence.

## Frontmatter

| Field | Required | Use |
|---|---:|---|
| `type` | Yes | `agentic-system-analyses/types/agentic-system-synthesis.md` |
| `description` | Yes | One sentence on the system's mechanism and limits, 50 to 250 characters; also the overview's retrieval description |
| `run-id` | Yes | The run's ID |
| `reviewed-boundary` | Yes | The run's immutable revision or capture identity |

## Bounded synthesis

`## Bounded synthesis` gives the evidence basis and boundary, architectural
characterization and claimed work, runtime map, only the discriminating
mechanisms this target needs, scenario-relative assessment, and concrete
evidence or system changes that would alter the assessment. Where the
runtime report supports it, the synthesis states separately whether the
system meets theory-builder conditions 1–4, whether criticism of a consumed
theory improved the system's capacity for future action, whether the system
is reflective or autonomous, and whether it is
[self-improving](../../notes/definitions/self-improving-system.md) at the
declared boundary, each at its own evidence status; these are independent
properties, not a grade or a ladder. It is organized around the system's
operational progression, not as concatenated analyst reports, and cites
member records rather than restating them. It gives no product ranking,
generic adoption advice, system-wide epistemic grade, Commonplace delta, or
transfer recommendation. For learning and self-improvement findings it leads
with the strongest supported contribution, including partial results, then
states the unresolved question, at the level of the comparison actually
performed. Supported positives coexist with unresolved included parts, naming
missing facts and prevented conclusions locally. A positive witness warrants
existence, not complete enumeration; an uninspected or inconclusive part is
not an absent one. Several unestablished independent properties are not a
bundled negative. Trace-fed durable updates alone do not establish improved
capacity. Faithfully bounded uncertainty remains publishable; unsupported
assertions or concealed coverage gaps do not.

The Bounded synthesis must read without the members' context. State its
evidence basis and boundary, and link the member records that support it so
a reader can inspect the underlying account. Every record ID resolves in the
members its layout role cites. Relative links resolve from `synthesis.md`
in the set directory.

## Limitations

`## Limitations` contains one row per limitation:

`limitation | affected source, record, or route IDs | inspected boundary | conclusion prevented | evidence that would resolve it`

Every `Unresolved conflict:` in the reconciliation appears here, and so does
a record fault found during synthesis verification, with its prevented
conclusion. Every limit declared by any of the three verification members
is carried here with its IDs and analytical consequence. `none` means the
whole set was checked and no limitation remains. A blocker also recorded in
a verification still has its analytical consequence stated here.

## Template

```markdown
---
type: agentic-system-analyses/types/agentic-system-synthesis.md
description: "{one sentence on the system's mechanism and limits}"
run-id: AAS-YYYY-MM-DD-system-slug-token-nn
reviewed-boundary: "{immutable revision or capture identity}"
---

# {System} synthesis

## Bounded synthesis

## Limitations
```
