---
description: "Draft decision that every type value is a KB-relative path to its spec file, found on a search path of the library root and the artifact's KB root; restores path-valued types without relative paths and drops project-shared types"
type: reference/types/adr.md
tags: []
---

# 088-Type values are paths on a two-root search path

**Status:** workshop draft; not accepted
**Date:** 2026-09-25
**Amends:** [ADR 086](../../reference/adr/086-projects-read-the-library-from-the-installed-package.md) (bare global type names; project-shared types stay allowed), [ADR 087](../../reference/adr/087-source-and-report-types-are-global-library-types.md) (the one permitted snapshot rewrite), and [ADR 068](../../reference/adr/068-collection-contracts-stop-enumerating-available-types.md) (type eligibility)
**Restores:** the path-valued `type:` of [ADR 018](../../reference/adr/018-types-are-path-references-to-instruction-docs.md), for every type
**Promotion condition:** accept only with the implementation that makes the
resolver, the collision check, the emitters, init's migration, and the specs,
contracts, and skills that teach the form operative. Allocate the ADR number
at promotion; 088 is provisional.

## Context

ADR 018 made every `type:` value a path to the type's spec, so a reader, agent,
or tool could check a declaration by opening the file it names. ADR 086 moved
the library out of the repository. A committed file can no longer hold a path
to a global type, because the library's location differs per machine, so ADR
086 named global types by bare name (`type: note`) and resolved them as
`types/<name>.md` under the library root.

Two problems remain. A bare name is not a pointer: checking `type: note` needs
an unwritten rule (library root, plus `types/`, plus the name, plus `.md`). The
operator found the path form convenient for checking declarations and wants it
back (operator, 2026-09-25). And local types are still file-relative, so one
type has several spellings that depend on the artifact's depth: an ADR is
`../types/adr.md` from `reference/adr/` and `kb/reference/types/adr.md` from
elsewhere, and a design proposal changes spelling when it moves into
`proposals/archive/`. A file-relative value breaks when its artifact moves
within its collection, and library files cannot use the `kb/` form at all,
because the installed library has no `kb/` root.

Programmers already know a rule that fixes both: a search path, as for
executables, modules, and include files. The value is a relative path, and a
short, fixed list of roots says where to look.

ADR 086 also kept project-shared types: a project's own `kb/types/`, eligible
in every collection. Init never creates that directory, and nothing in the
framework uses it. Its only realistic contents are the old copies of library
types that ADR 086's migration keeps when they differ from the library.

## Decision

**Every type value is a KB-relative path to its spec file.** The value names
the spec's path under a KB root, with its `.md` extension and no leading `./`,
`../`, or `kb/`:

- a global type: `type: types/note.md`;
- a collection-local type: `type: reference/types/adr.md`,
  `type: notes/types/structured-claim.md`.

The same form applies wherever a type is named: `type:` in frontmatter, gates'
`requires_type:`, and type specs' own `type:` (the root spec is
`type: types/type-spec.md`).

**Two roots form the search path.** A value resolves under:

1. the library root, for global types only: a value resolves there only when
   it names `types/<name>.md`; and
2. the root of the KB that holds the artifact: the project's `kb/` for a
   project artifact, and the library root for a library file.

The library's collection-local types are not on a project's search path.
Projects are scaffolded with collections that share the library's names
(`notes/`, `reference/`, `instructions/`), so a project's own
`reference/types/adr.md` would otherwise collide with the library's. In the
source checkout, and for every library file, both roots are the same
directory, so the value names exactly one file. Values starting with `./`,
`../`, or `kb/`, and bare names, no longer resolve; validation rejects them
and names the form to use.

**A value that finds two different files is an error.** If a value resolves
under both roots to two different files, validation fails and names both. No
root takes precedence, so a project file can never silently override a library
type, and search order does not matter. The check runs wherever a value is
resolved; the health check reports the same collisions for a whole project.

**Project-shared types are dropped.** A project's `kb/types/` no longer has
special standing. Types a whole project needs are global library types; types
a collection needs live in that collection's `types/`. A leftover copy of a
library type in a project's `kb/types/` collides with the library file of the
same path, and the error tells the operator to delete it or move its change
into the project's own collections, as ADR 086's migration already asks.

**Eligibility is otherwise unchanged.** A global type (`types/<name>.md` under
the library root) is eligible in every collection. A collection-local type is
eligible only in its own collection, and the whole `kb/work/` subtree may use
any valid type, as ADR 068 decided. The workshop exception needs no special
form any more: a workshop writes `reference/types/adr.md` like everyone else.

**The written value is the type's identity.** Framework validation rules,
type-conformance gating, and `requires_type:` matching key on the value as
written, such as `types/full-pass-report.md` or `articles/types/article.md`.
Review identities of spec files are unchanged: `commonplace:types/<name>.md`
in an installed project and the repository path in the source checkout.

**One more recorded snapshot rewrite.** ADR 087 permits exactly one change to
a capture's bytes. This decision extends that exception to one further line
change, from `type: snapshot` to `type: types/snapshot.md`, made by the same
byte-deterministic, idempotent migration, re-pinning the same two checksums
(`snapshot_sha256`, `original_snapshot_sha256`). ADR 087 has not shipped in a
release, so init goes straight from the retired snapshot path to the new
value, and an installed project rewrites each capture once. Only the source
checkout and its clones rewrite twice.

## Considered alternatives

The design went through several drafts on 2026-09-25; the rejected ones are
recorded here.

**Keep bare names (ADR 086 as is).** Shortest, and already implemented. Lost
on checkability: the value does not name its file. It also leaves local types
file-relative.

**Keep bare names and add a lookup command** that prints a type's spec path.
Lost for the reason ADR 086 dropped lookup commands for the library: a command
call per check, a shell, and a permission rule, where a file path needs none.

**A reserved `kb/types/<name>.md` value for global types.** Rejected in ADR
086: in an installed project it looks like a project path but names no file
there.

**A namespaced name without a path** (`commonplace:note`). Short, and the
prefix keeps no-shadowing by syntax. Lost: it is still not a path, so the
reader still needs the `types/<name>.md` rule, and it would give `commonplace:`
two meanings, a path under the library root in schema references and review
identities, and a name here.

**Library-rooted paths for global types only** (`commonplace:types/note.md`,
the first draft of this decision). The prefix states the root, no-shadowing
holds by syntax, the form matches the `commonplace:` schema references and
library review identities, and in an installed project a type's identity would
equal its spec's review identity. Lost: the value is still not a path a
programmer can open without substituting the root, it lengthens every global
value, a colon in the value breaks the frontmatter if an author adds a space
after it, and it leaves local types file-relative. The first draft deferred
local types to a separate decision; this one takes them in.

**A second prefix for local types** (`collection:types/adr.md`, resolved at the
artifact's collection root). Gives local types one spelling and makes
eligibility structural. Lost to the search path: two prefixes are two rules to
teach, and the written value would not identify a local type, because two
collections could each have `collection:types/adr.md`.

**Bare names on a per-collection search path** (the artifact's collection
`types/`, the project's `kb/types/`, the library's `types/`). Shortest values
and structural eligibility. Lost: names can repeat across collections, so the
written value is not an identity, and the path depends on where the artifact
sits.

**The whole library root on the search path.** Simpler to state. Lost: a
project's collection-local types would share a namespace with the library's
collection-local types, because both use the same collection names, so an
ordinary project type such as its own `reference/types/adr.md` would collide.

**Precedence instead of a collision error.** The first root that has the file
wins, as with `PATH`. Lost: a leftover project copy of a library type would
silently override the library, which is the shadowing ADR 086 ruled out.

**Collision check in the health check only.** Proposed as sufficient, since
collisions are rare. Lost as the only check: the health check runs when someone
invokes it, while validation resolves every value anyway, so it can reject a
collision at no extra cost on every run. The health check keeps a
project-wide report.

**Keep project-shared types.** Nothing would break, but the library's
`types/` and a project's `kb/types/` would share one namespace for good, and
the collision check would guard real use rather than migration leftovers.
Dropped under YAGNI: no project is known to use them.

**Values without `.md`.** Reads like a module path. Lost: the value would no
longer be the file's path, which is the property being restored, and adding
the extension back is one more rule every reader and tool must be told
(operator, 2026-09-25).

Left open: schema references. Local schemas refer to global schemas as
`commonplace:types/<name>.schema.yaml`. They are JSON Schema `$ref`s, which
normally resolve relative to the referring file, so this decision leaves them
as they are.

## Consequences

**Easier.** Every type value is a path to its spec under one of two stated
roots. In the source checkout, and for library files, it is exactly the path
to open under `kb/` or the library root. A type has one spelling everywhere,
an artifact can move within its collection without breaking its type, and a
search such as `rg "^type: reference/types/adr.md"` finds every instance.
Library files and project files use the same form. The workshop exception and
the project-shared eligibility rule disappear from the resolver.

**Harder or riskier.**

- Every type value in the corpus is rewritten again, days after ADR 086's
  rewrite. Every rewritten artifact registers a content change, so review
  baselines on those files need acknowledgement or refresh.
- Snapshot checksums are re-pinned a second time in the source checkout and
  its clones. Until a clone runs the migration, validation warns, and
  grounding, ingest, and re-ingest stop on the affected pairs, as under ADR
  087.
- In an installed project a global value such as `types/note.md` names no file
  in the project; the reader must look under the library root, given in
  `.commonplace/library.md`. The rule is stated, but it is a lookup.
- In the source checkout a spec has two strings: its type identity
  (`types/note.md`) and its review identity (`kb/types/note.md`). Code that
  compares a type value with a criterion path would break only there, so the
  implementation tests type-conformance gating in both layouts.
- A project that relied on project-shared types loses them. None is known.
- Local, ignored report state carries old type values. Files init does not see
  fail validation until rewritten.

**Operativity path.** The type resolver consumes the decision when it resolves
values on the two roots, rejects other forms, and fails on collisions; the
validator keys its rules and eligibility checks on the written value. The
snapshot commands and the full-pass and agentic-analysis code write the new
values. `commonplace-init` rewrites type values in installed projects and runs
the snapshot migration; the source checkout runs the same rewrite through a
one-off script. The health check reports collisions across a project. Agents
consume the form through the type specs' frontmatter tables and templates,
`cp-skill-write`, the collection contracts' type-eligibility sections, and the
type-search recipes in `AGENTS.md` and its template, with the force of the
type contract, the collection contract, and the invoked skill. Global schemas
change their `type` constants to the new values.

**Where the decision stops applying.** It covers how type values are written
and resolved. It does not change schema references, review identities, or
which collections may use which types. It removes project-shared types;
adding them back needs an eligibility rule and a namespace that cannot collide
with the library's `types/`. The extension of ADR 087's snapshot exception
covers only the one frontmatter line named above.
