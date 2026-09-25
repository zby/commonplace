---
description: Use before implementing a decision that changes a form, identity, layout, or rule that more than one kind of consumer reads, such as frontmatter values, type naming, file layout, pinned artifacts, or command surfaces
type: types/instruction.md
---

# Change a contract that several consumers read

Goal: a decision reaches every consumer of the contract it changes, so no current artifact, command, or procedure is left teaching or enforcing the old form.

A decision usually reaches its primary implementation and misses other readers. ADR 086's type rewrite updated 847 frontmatter values but left the prose rules that taught the old form, left older ADRs describing the old layout as current, and silently broke 33 byte pins on retained analysis results. ADR 088's migration missed local schema constants, single-quoted values, and a collision check it promised. Each miss was a consumer class nobody listed. This procedure makes that list before implementation.

Use it for a change to something several kinds of consumer read: a frontmatter field or value form, a type or criterion identity, a path or directory layout, a file whose bytes something pins, a command's inputs or outputs, or a rule stated in a collection contract or type spec. Skip it for an edit with one reader.

## Steps

1. **Write a change packet** in the implementing workshop, or in the working notes for the change. Fill every field below. A field that does not apply gets one line saying why.
2. **Search for the old form, not the files you remember.** Use `rg` across the whole checkout, including ignored local state (`rg --no-ignore --hidden`) when the change rewrites artifact bytes. Record each search pattern with its hit count. The search results are the consumer inventory; a class with no search is not covered.
3. **Implement consumer class by consumer class**, and mark each field done in the packet.
4. **Probe from a temporary project**, not only from this checkout: run `commonplace-init --root <scratch dir>` on a fresh directory and on one holding the old form, then validate. Unit tests prove a copier or resolver; a probe proves the product a user receives.
5. **Name consumer classes, not files, in the ADR's operativity path.** Counts and file lists go in the implementing commit message (ADR 074).
6. **After the change lands, rescan for the old form once more** and record what the rescan found. A miss found here is a missing field: add it to this instruction.

## Packet fields

1. **Authoritative declaration.** Where the contract is stated: ADR, type spec, schema, code constant.
2. **Declared scope and its enforcement.** What the contract claims to cover ("every", "all", "supported on") and which mechanism enforces that scope. A scope word wider than its mechanism is a future contradiction.
3. **Consumer classes.** For each behavioral role, the search that found its members and whether each is updated:
   - resolvers and validators, including rules keyed by the old value;
   - schemas and every derived copy of the value, such as schema `const` constraints;
   - emitters: commands and code that write the form;
   - migration code in `commonplace-init`;
   - promoted skills and procedures that name or template the form;
   - collection contracts, type specs, and their templates and frontmatter tables;
   - control-plane templates (`AGENTS.md.template`) and the root `AGENTS.md`;
   - reference pages and accepted ADRs that state the old form in the present tense;
   - tests and fixtures;
   - published views: the site build, redirects, generated indexes.
4. **Byte-pinned consumers.** Every checksum or recorded hash over an artifact the change rewrites, such as `snapshot_sha256`, `analysis-result-sha256`, and review freshness baselines. Rewriting pinned bytes breaks the pin silently. For each pin, decide how it is re-pinned and how the re-pin is verified.
5. **Spellings of the old value.** Every form the old value takes in real files: quoted and unquoted YAML, JSON-style frontmatter, relative and repository-relative paths, list items, derived copies. Search for each spelling separately.
6. **Generated and projected forms.** Build outputs, the installed library, init-written stubs and routing files, generated indexes.
7. **Fresh install.** What `commonplace-init` creates under the new contract, and whether the result validates.
8. **Existing installs and clones.** What init rewrites, what it keeps and lists, whether a second run changes nothing, and how clones of this checkout, which never run init, catch up.
9. **Diagnostic promises.** Every claim that a command or check will report a condition. Name the command and give the probe showing that it does. A promised diagnosis with no check is a contradiction on arrival.
10. **Acceptance probe.** The temporary-project commands from step 4 and their expected results.
11. **Drift guard.** A test that compares the declared or discovered set with the consumed set, without hardcoding today's count.
12. **Historical witnesses.** Old forms that stay because they are history: ADRs marked amended, frozen evidence copies, retained results. Say how each is marked so later scans do not report it.

## Maintenance

When a rescan or a later scan finds a consumer this packet missed, add its class to field 3, or a new field, in the same commit that fixes the miss. The list grows from observed misses, not from speculation.
