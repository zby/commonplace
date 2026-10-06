---
description: Directory artifacts add schema-owned membership and shared set checks while preserving ordinary validation of every member.
type: reference/types/adr.md
status: accepted
---

# 095 — Directory artifacts add shared set validation

**Status:** accepted
**Date:** 2026-09-28

**Amended by:** [ADR 102](./102-separate-the-analysis-collection-and-publish-stable-system-paths.md). The accepted overview is now the public entry point; completed run state pins it and the manifest, and the manifest still pins every member.
[ADR 111](./111-directory-types-declare-their-layout.md). A type's declared layout, not its schema, owns membership, requiredness and member relations; the schema keeps the manifest's metadata.

## Context

Individually valid documents can form an invalid set. A required member may
be missing, members may describe different runs, or a reference in one may
lack a declaration in another. Workflow-specific checking makes those
conditions invisible to ordinary validation and gives consumers separate
implementations to maintain.

The first instance is an agentic-system analysis. Its complete output has
an overview, runtime report, memory report and epistemic report. Its exact
version matters to publication and comparison, but other directory types
may need consistency checks without stored hashes.

## Decision

Recognize a directory artifact by `ARTIFACT.yaml` at its root. The manifest
selects a path-valued type whose shared JSON Schema owns required and
optional members, expected types, hash requirements, and permission for
undeclared members. Call that last distinction **open membership** versus
**closed membership**. Requiredness and membership policy are independent.
A manifest holds instance metadata; it cannot relax the type's rules.
Existing type resolution and collection eligibility apply.

Membership consists of visible Markdown files directly beside the manifest,
including files with no metadata entry. Hidden files, non-Markdown files
and descendants are outside membership. Manifest and member symlinks are
rejected. Duplicate YAML keys and metadata paths that do not name a direct
member fail. The loader supplies actual parsed members to the schema;
manifest data cannot replace their content. Every supplied SHA-256 is
checked against the same bytes used for parsing, even when hashes are
optional for the type.

Directory validation adds set checks to ordinary member checks. A malformed
manifest cannot suppress a member failure. Traversal continues through
subdirectories. Explicit file validation checks that file alone. Directory
and collection reports group members under their artifact and count the
artifact once, while member diagnostics retain the member path.

Workflow consumers call the shared artifact checker without starting
traversal. One validation context caches bytes, parses and results; an
active dependency cycle fails explicitly. This separates the set's contract
from source-bound and publication-state checks that need external inputs.

The analysis workflow uses the collection-local
[analysis set type](../../agentic-system-analyses/types/agentic-system-analysis-set.md).
Its working output has a dedicated `output/` directory, separate from run
state and specialist inputs. The manifest pins every actual member;
run state pins the manifest, and a published review pins its retained copy.
Complete outcomes have four reports; blocked and out-of-scope outcomes have
only the overview and cannot publish or supply comparison rows. The shared
set rule resolves record references and comparison references against the
set's declarations. Source anchors and specialist provenance remain
workflow checks.

Retained output remains frozen. The analysis method's committed-input check
includes the set contract. Hashes establish content identity; reproducing
historical validation also needs the recorded method revision.

## Considered alternatives

**Keep specialized checks or anchor a set on one Markdown member.** The first
leaves ordinary validation without a set guarantee. The second makes
recognition depend on a designated member and gives that member different
integrity treatment. A separate manifest provides one recognition rule and
allows every report to be hashed alike.

**Put rules in each manifest.** This permits instances of one type to diverge.
A shared schema keeps the contract at the type level. `ARTIFACT.yaml` was
chosen over `MANIFEST.yaml` to identify one typed artifact explicitly.

**Adopt an external directory format or constraint language.** Data Package,
DirSchema, directory-schema-validator, CUE and RO-Crate were considered.
Their adapters would still need Commonplace's Markdown representation,
type resolution and imperative checks. Ordinary JSON Schema already
expresses the required membership rules without another toolchain.

**Give the schema only manifest data.** That requires code to compare member
content and can hide undeclared files. The schema instead receives the
actual discovered set alongside the manifest.

**Require hashes for every directory type.** Editable sets need not carry
exact-version bookkeeping. Types choose when hashes are required; supplied
hashes always bind. A single computed set digest is deferred until experience
shows that per-member metadata upkeep outweighs its precise mismatch reports.

## Consequences

Authors declare membership through type schemas. The validator consumes
that declaration for directory and collection checks; member types retain
their ordinary force. Analysis producers load the format through their
skill and type contracts. Completion, publication and comparison readers
invoke the same checker, while CLI and JSON reporting expose its findings.
A valid file no longer implies a valid containing set, and a set manifest
never exempts files from their own checks.

The tested boundary is local Markdown membership with collection-local
fixtures and the analysis workflow. Nested membership, automatic sidecar
migration, change-triggered validation and freshness registration are
outside this decision. Direct-child discovery does not make descendants
members of their parent's artifact. Deterministic success establishes the
expressed constraints, not analytical truth or semantic support.
