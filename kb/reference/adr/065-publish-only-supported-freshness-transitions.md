---
description: "Generic freshness acceptance is withdrawn until a concrete non-review target supplies identity, input semantics, and an end-to-end registration path"
type: ../types/adr.md
tags: []
status: accepted
---

# 065-Publish only supported freshness transitions

**Status:** accepted  
**Date:** 2026-08-19  
**Amends:** [ADR 052](./052-general-freshness-store-review-first-migration.md)

## Context

[ADR 052](./052-general-freshness-store-review-first-migration.md) generalized
the freshness store around target identities and input snapshots. Its v1 scope
admitted only `review-pair` targets, whose baselines can be created or replaced
only by finalizing completed review evidence.

The package nevertheless published `commonplace-freshness-accept` for
non-review targets. The transition rejected `review-pair`, then checked an
empty set of accepted non-review target kinds. Every legal invocation therefore
failed before the snapshot and baseline code could run. The entry point,
schema, implementation, and rejection-only tests proved presence, not a usable
capability.

## Decision

Withdraw `commonplace-freshness-accept`, its JSON contract, and its unreachable
transition. Review finalization remains the only path that creates or replaces
a baseline in v1. `commonplace-freshness-status`,
`commonplace-freshness-ack`, and `commonplace-freshness-retire` remain because
they operate on registered review targets.

Generic initial acceptance or refresh may return only with the first adopted
non-review target. That adoption must define the target key, input roles and
version kinds, producer, initial and refresh semantics, JSON or other operator
contract, and end-to-end tests. A disabled placeholder is not part of the
interim interface.

This amendment is operative through `[project.scripts]`, the
`commonplace.cli` and `commonplace.freshness.transitions` modules, the command
and freshness reference pages, and the test that requires exact parity between
published command names and command-reference headings.

## Considered alternatives

**Keep the rejecting placeholder.** This preserved a prospective interface but
made command discovery and documentation overstate the system. A command with
no admissible input is not a useful compatibility surface.

**Permit arbitrary non-review target kinds.** The core could accept any
canonical target key, but without a registered producer and input contract it
could not establish that the identity or dependency set was complete.

**Implement collection freshness now.** The worked proposal has not been
adopted, and no current consumer requires its `collection-text` encoding.
Implementing it only to justify the command would violate the project's YAGNI
rule.

**Let acknowledgement create an initial baseline.** Acknowledgement is a
disposition of changes to an existing accepted baseline. Giving it a second
registration meaning would erase the distinction between accepting a target's
complete dependency set and acknowledging a displayed change.

## Consequences

- The published Commonplace command set shrinks by one, with package metadata
  and the command catalogue changing together.
- Review freshness retains global status, live-hash acknowledgement,
  retirement, capture finalization, evidence retention, and revision CAS.
- Future non-review freshness work must introduce its usable registration path
  deliberately rather than activating dormant scaffolding.
- Existing editable uv-tool installations must be reinstalled after this
  entry-point change so their generated launcher set matches package metadata.

---

Relevant Notes:

- [Freshness architecture](../freshness-architecture.md) — implemented-by: the retained transition and command surfaces
- [Collection-as-artifact freshness](../proposals/collection-as-artifact-freshness.md) — future-work: a possible first non-review target
