---
description: "Proposal: let document and directory types select Python validation checks without a new constraint language, while leaving code trust, registration and the hook interface open."
type: reference/types/design-proposal.md
tags: [type-system, kb-maintenance]
---

# Type-selected Python validation checks

This proposal asks how a document or directory type can select Python checks
for properties that its schema cannot express. The operator's settled design
constraint is to avoid inventing a cross-check language. Selection may be data;
check logic and reusable operations remain ordinary Python.

The trust boundary, registration mechanism and checker interface are not yet
adopted. This proposal does not authorize executing code supplied by a KB.

## Current state (as of 2026-10-06)

- `src/commonplace/lib/validation.py` already has `type_rule` and
  `directory_type_rule` registries. Framework Python registers functions under
  canonical type paths; the type document does not select the implementation.
- The analysis-set rule uses those hooks to check member identities, record
  references, its reconciliation index and comparison data. These checks
  demonstrate a collection-local need. Since 2026-10-09 they live in the
  analysis package (`commonplace.lib.agentic_analysis.rules`), but
  `validation.py` still imports that module by name to register them.
- `ValidationRun` supplies shared byte reads, parsed documents, directory
  artifacts and candidate content overrides. Existing checks can consume that
  context instead of independently reopening files.
- The [type-spec contract](../../types/type-spec.md) separates schema validation
  from semantic type-conformance review. The [validation contract](../validation-contract.md)
  also permits imperative rules for properties needing related artifacts.
  The extension question is who selects and supplies those rules, not whether
  Python checks should exist.

## Problem

A local type can state a cross-artifact requirement in prose, yet adding its
mechanical enforcement currently requires framework registration keyed to that
type. This couples the framework's rule table to particular local contracts.

A declarative cross-check language would replace Python with another system
whose expressions, scope rules and composition require design and maintenance.
The operator excludes that route. A narrow executable-check interface could
provide extensibility while preserving ordinary Python development and testing.

## Responsibilities

The type contract states what must hold and the limits of what a successful
check establishes. Python implements mechanically checkable properties. A type
selection identifies the implementation to run; it does not encode predicates,
selectors or a miniature program. Workflow callers decide when to validate and
which findings prevent acceptance.

A registry of checker names is a possible selection interface, not a required
syntax. Reusable field comparisons and reference resolution can remain Python
helpers rather than universal YAML operations.

## Options

### A. Types select framework-supplied checks

The validator resolves a type's selection through a registry shipped with
Commonplace and invokes the selected Python implementation with the artifact
and validation context. Type authors can reuse installed checks without adding
a new type-path registration; new implementations still require a framework
release or development change.

The oracle is the parsed artifact and related evidence the implementation
checks. For example, field equality establishes identity agreement, not the
truth of the reports. A source quotation match establishes occurrence, not
semantic support. The type must state the relevant warrant and limit.

This is the narrowest candidate and reuses the existing trusted execution
boundary. It does not make independently authored project checks available.

### B. Types select checks from explicitly authorized extensions

Allow an operator-approved Python package or project extension to register
additional implementations. Validation consumes only the registrations enabled
for that environment; a type's reference does not itself authorize loading
new code.

The checker has the same evidential limits as in option A. Authorization says
whose code may run, not that its judgments are correct. Python executes with
the validator process's permissions unless a separate isolation mechanism is
provided; a registry is not a sandbox.

This supports local experimentation without framework edits. It requires
choices about installation, naming collisions, interface compatibility and
reproducing the implementation environment. It may follow option A rather
than being a prerequisite for it.

### C. Types directly name repository Python code

The validator could import a module or file named by a type. That creates a
short development path, but validation of repository content becomes an
execution trigger for code supplied by that repository.

The consumer is the validator's loader, and the declaration would have force
to execute code unless an independent authorization boundary intervenes.
Check results retain the same evidential limits, while code trust becomes a
separate requirement. This option remains outside the recommended starting
scope. If selected, its authorization and isolation policy must be decided
explicitly; ordinary artifact validation cannot silently acquire that power.

## Interface constraints

A useful extension must preserve the existing validation guarantees:

- An unavailable required checker is an explicit validation failure, never a
  silent omission or successful conformance result.
- Checker execution errors are distinguishable from findings that an artifact
  violates its contract. Neither can be reported as a successful check.
- Checks are read-only by contract and observe the same candidate bytes as the
  rest of the validation run. Access through the shared context supports that
  consistency; it does not technically prevent arbitrary Python side effects.
- Findings enter the existing result surface with an identifiable rule and
  subject. A new result protocol is needed only if an actual consumer cannot
  express its required findings through the current one.
- A historical result depends on the checker implementation as well as the type
  and inputs. Reproducible method environments must identify the executable
  code and dependencies; editing a checker is not equivalent to unchanged
  validation merely because the type text is unchanged.

Base framework checks remain mandatory. Type-selected checks do not grant
permission to disable them or to broaden a worker's evidence or write authority.
Semantic judgments remain review tasks rather than deterministic hook claims.

## Candidate selection and free choices

Option A is the proposed starting point; option B is a possible extension when
a separately developed checker has a real consumer. This preference is not an
adoption decision. Direct repository execution requires a distinct trust
choice and is not implied by interest in Python hooks.

Selection syntax, registration and packaging, callable shape, execution order
and failure reporting details remain implementation choices constrained by the
existing validation API and demonstrated consumers. No general plugin manager,
constraint language or dependency-invalidation engine is required by this
proposal. [Generalized validation invalidation](./generalized-validation-invalidation-and-imperative-extension.md)
addresses which artifacts need another check, not how this hook executes.

## Adoption criteria

Adopt a type-selection mechanism when it can replace a real hardcoded
registration while preserving conformance outcomes, diagnostic usefulness and
candidate-byte consistency. Exercise both document and directory consumers
before claiming the interface serves both. Missing implementations and checker
exceptions must have tested non-success outcomes.

The operator must choose the code-supply and authorization boundary before
external extension loading ships. Require a concrete independently supplied
checker before building that distribution path. Do not require existing check
logic to be re-expressed in a generic primitive vocabulary merely to make it
selectable.

Draft validation in a role ([ADR 113](../adr/113-artifact-runs-execute-declared-plans-with-pinned-judgments.md))
is a consumer that uses the existing Python registrations; its adoption did not
depend on this proposal.
