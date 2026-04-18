---
name: cp-skill-compile-collections
description: Compile all COLLECTION.md files into a single optimized topology document showing registers, quality goals, and cross-register linking rules. The project owner runs this whenever a COLLECTION.md changes; commonplace-init ships a pre-compiled default so the connect skill works on first run.
type: instruction
user-invocable: true
allowed-tools: Read, Write, Glob, Grep
context: fork
model: haiku
---

## EXECUTE NOW

Compile a topology document from all per-collection COLLECTION.md files in the KB.

## Procedure

1. **Discover collections.** Find all `COLLECTION.md` files:

```bash
# Find via glob
kb/*/COLLECTION.md
```

2. **Read each COLLECTION.md as prose.** Do not expect YAML frontmatter or structured fields. Infer only what the prose clearly states:
   - register profile or layer role (for example theoretical, descriptive, prescriptive, catch-all workshop)
   - quality goal
   - title convention, if stated
   - outbound linking conventions, if stated

   Sparse collection files are valid. If a field is not stated, write `not specified` or omit it rather than inventing a rule. If a collection says linking is permissive, preserve that as the linking guidance.

3. **Produce an optimized topology document.** The output must be compact — optimized for an agent loading it into bounded context before connecting notes. Do NOT reproduce the full COLLECTION.md prose. Distill to:

   - **Collection registry** — one table: collection path, register, quality goal, title convention
   - **Cross-register linking matrix** — for each (source register, target register) pair, the appropriate relationship types. Merge the per-collection outbound tables into a single matrix. Deduplicate where multiple collections describe the same register pair.
   Do not include register constraints in the topology output. They belong in collection conventions and writing/review workflows; the connect skill loads topology only to choose relationship labels.

   Target: under 1500 tokens total. If a section adds no information beyond what the matrix already says, cut it.

4. **Save the output** to `kb/reports/collection-topology.md` with this frontmatter:

```yaml
---
description: "Compiled collection topology — registers and linking rules. Rebuild with cp-skill-compile-collections."
type: note
status: current
---
```

5. **Report.** Print the path and the number of collections compiled.

## Critical Constraints

**Always:**
- Read every COLLECTION.md before producing output
- Compress aggressively — the connect skill loads this document to make one decision (what relationship type to suggest)
- Include the rebuild command in the output so the reader knows this is generated

**Never:**
- Reproduce full COLLECTION.md sections — distill, don't copy
- Invent linking rules not present in the source COLLECTION.md files
- Skip collections that have a COLLECTION.md
