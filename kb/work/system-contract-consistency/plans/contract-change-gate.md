# Workshop-wide outcome — Promote a contract-change implementation gate

**State:** promoted 2026-09-25 as
[change a contract that several consumers read](../../../instructions/change-a-contract-that-several-consumers-read.md),
loaded from the [ADR type](../../../reference/types/adr.md)'s operativity-path
rule. The two worked applications below added three fields to the original
nine.

## Outcome selected

Promote one small implementation/review instruction for changes to
cross-cutting operative contracts. It complements the ADR type's operativity
path. It does not turn ADRs into file inventories and does not claim to detect
semantic contradictions automatically.

The instruction requires a change packet to identify:

1. authoritative declaration;
2. declared scope;
3. current operative consumer classes;
4. generated or projected forms;
5. fresh-install consequence;
6. existing-install migration;
7. acceptance test;
8. drift guard;
9. retained witnesses that are explicitly historical.

“Consumer classes” means behavioral roles such as validator, generator,
runtime skill, routing template, installed projection, and published view. A
change may name concrete files while implementing the packet, but the durable
instruction should not freeze today's paths as a universal list.

## Work

1. Read the instructions collection contract and content-routing guidance.
2. Select the narrowest existing implementation/review instruction that can own
   this gate, or write a short new instruction if none has that purpose.
3. **Applications.** The 2026-08-27 disjoint-root ledger was abandoned with
   its design (it remains in git history). Apply the checklist
   retrospectively to the ADR 086 delivery change: its commit (`e6103225`)
   inventoried consumers, and the 2026-09-25 rescan shows which it missed.
   Then exercise the checklist against one independent migration packet. Revise fields that fail to expose a consumer or
   produce work the implementer cannot use.
4. Add a narrow discoverability route from the change workflow that needs it.
5. Validate the durable artifact and record the worked applications here.

## Completion

The gate is operative when a current change workflow loads it, both worked
applications identify their independent consumers and migration boundary, and
the instruction has a concrete maintenance path. Workshop prose alone does not
complete this outcome.

## Worked applications (2026-09-25)

Both applications are retrospective: the checklist was run against changes
already made, and the misses were found by the workshop's rescans.

| Field | ADR 086 (library delivery) | ADR 088 (type values as paths) |
|---|---|---|
| Consumer classes | Commit inventoried code, tests, frontmatter values, INSTALL, templates. Missed: prose rules in type specs, `cp-skill-write`, the reports contract; accepted ADRs 014, 022, 027, 038, 039 describing the copy as current | Code, schemas, init, docs sweep, tests covered. Missed at first: theory notes and collection-local specs teaching old values (found by its own contract tests) |
| Byte-pinned consumers | **Missed.** The rewrite broke 33 `analysis-result-sha256` pins; the matrix and publication checks would have failed | Covered: snapshot checksums re-pinned by a deterministic migration; result pins re-pinned by init |
| Spellings of the old value | Covered path and bare forms | **Missed** single-quoted YAML values (follow-up I4) |
| Derived copies | Schema `const` values rewritten in the repository | **Missed** in init's migration: a project's local schema `const` kept the old identity (I4) |
| Diagnostic promises | None | **Missed:** the ADR promised the health check reports collisions, and type review swallowed the collision error (H1, H2) |
| Existing installs and clones | Init migration of copies; checkout clones unaffected | Init migration plus `scripts/migrate-snapshot-types.py` for clones |
| Historical witnesses | ADR 021 and 037 marked superseded; later amended-by markers on five ADRs | Amended-by markers on ADRs 068, 086, 087 |

The misses in the byte-pin, spelling, derived-copy, and diagnostic rows are
why the instruction has fields 4, 5, and 9 and names schema constants in
field 3. Its maintenance rule adds a field whenever a later scan finds a
missed class.
