# Change operations catalogue — working list

**Status: observational, first pass, 2026-08-25.** Each operation is admitted
by at least one observed instance. Premises and homes are one session's reading
of the ADR set and the instruction inventory, not audited claims. No
completeness is claimed; see the README before treating any cell as settled.

Columns: **Observed in** — ADRs or records that performed the operation.
**Must know before acting** — premises the actor needs and cannot cheaply
recover from the implementation or `git log`. **Current home** — where those
premises are written today. **Gap** — a premise with no home, or a home that is
the wrong kind (an ADR standing in for a contract, prose standing in for a
test).

## Operations

### 1. Add or alter a collection contract (`COLLECTION.md`)

- Observed in: ADR 017, 019, 042, 057, 061–063, 068–071.
- Must know: what a collection is and what its text contract must declare;
  type eligibility (global + owned-local); link authorization per destination;
  that the nearest `COLLECTION.md` is the complete local authority; which
  validator checks read the contract.
- Current home: `kb/reference/definitions/collection.md`,
  `collections-and-types.md`, `link-vocabulary.md`,
  `collection-prototypes.md`; validator behavior in `src/commonplace/lib/`.
- Gap: no instruction for the operation itself (write-instruction covers
  instructions, not contracts). Whether the collection-conformance gate (ADR
  041) must be re-baselined after a contract edit is stated only in the ADR.

### 2. Add or alter a type spec

- Observed in: ADR 012, 015, 016, 018, 026, 038, 047, 048.
- Must know: path-valued type identity; schema severity per constraint (fail
  by default; audit the corpus before adding a failing rule); that editing a
  type spec stales every type-conformance pair (ADR 038); imperative rules
  dispatch by canonical path; type specs validate through the normal pipeline.
- Current home: `kb/types/type-spec.md`, `collections-and-types.md`,
  `validation-contract.md`; ADR 024 for the audit-before-flip rule.
- Gap: the audit-before-flip rule and the re-baseline consequence live only
  in ADRs, which are not routed to at change time (see adr-routing).

### 3. Add or alter a deterministic validation check

- Observed in: ADR 024, 046, 047, 049, 050, 051.
- Must know: base/type-rule/schema sources of findings; severity model;
  run-scoped execution and shared parses; what a check may dereference.
- Current home: `validation-contract.md`; live code.
- Gap: none obvious at this pass; the contract doc is the right kind of home.

### 4. Add or alter a review gate or criterion

- Observed in: ADR 005, 038, 041, 066, 073.
- Must know: placement rule for quality checks (cost × false-positive
  tolerance × whether it gates creation — ADR 005); criterion/gate/critique
  vocabulary; that a criterion edit stales its pairs; the migration procedure
  for semantics-preserving gate changes.
- Current home: `README-REVIEW-SYSTEM.md`, `kb/instructions/review-gates/`,
  `migrate-semantics-preserving-gate-changes.md`.
- Gap: the ADR 005 placement rule has no home outside the ADR.

### 5. Add, alter, or promote a skill or instruction

- Observed in: ADR 013, 022, 037, 067; `write-instruction.md`.
- Must know: skills copy into runtime surfaces (no symlinks); what belongs in
  always-loaded context versus on-demand; the prompt is the sole worker
  contract for review workers; the instructions collection contract.
- Current home: `kb/instructions/COLLECTION.md`, `write-instruction.md`,
  `control-plane-goals.md`, `instruction-generation.md`, `architecture.md`.
- Gap: none obvious.

### 6. Add, alter, or withdraw a CLI command or entry point

- Observed in: ADR 014, 039, 064, 065.
- Must know: commands never invoke git; command catalogue parity is tested;
  only supported transitions are published; editable uv-tool installs need
  reinstall after entry-point changes.
- Current home: `commands.md`, `INSTALL.md`, `AGENTS.md` (development
  section); parity test in the test suite.
- Gap: none obvious; the parity test is the right kind of home.

### 7. Change the link vocabulary

- Observed in: ADR 009, 019, 020, 058, 059, 060.
- Must know: source-as-subject grammar; collection-owned authorization;
  directional asymmetry; the label-migration procedure and its conservation
  rule.
- Current home: `link-vocabulary.md`, `migrate-directional-link-label.md`.
- Gap: none obvious.

### 8. Add, retire, or rename a vocabulary term

- Observed in: ADR 011, 022, 053, 054, 055.
- Must know: first-mention glossing is write-path behavior; a common English
  word cannot carry a technical sense (hyphenated compounds do); term
  retirement is ADR-scale, not a single-artifact operation.
- Current home: `AGENTS.md` vocabulary and prose/identifier rule;
  `retire-artifact.md` (the exclusion); the definitions collections.
- Gap: no procedure for term retirement; each instance has improvised.

### 9. Record, revise, or supersede a decision

- Observed in: ADR 028, 056, 074; every ADR.
- Must know: the ADR retention rule; the git read path and unshallow
  precondition; the alternatives and operativity-path requirements; how
  rationale is distributed across surfaces.
- Current home: `kb/reference/types/adr.md`, `design-rationale-management.md`.
- Gap: nothing routes a change run to the ADRs that bind it
  ([adr-routing](../adr-routing/README.md)).

### 10. Adopt or retire a proposal

- Observed in: ADR 028, 056.
- Must know: extraction gate; archive is a link sink; provenance as title tag.
- Current home: `kb/reference/proposals/README.md`, `proposals/archive/README.md`.
- Gap: none obvious.

### 11. Open or close a workshop

- Observed in: `kb/work/COLLECTION.md`; continuous.
- Must know: framing fixes only what a later session cannot determine;
  closure extracts then deletes; no redirect.
- Current home: `kb/work/COLLECTION.md`.
- Gap: none obvious.

### 12. Retire or relocate a library artifact

- Observed in: `retire-artifact.md`; ADR 039 (relocation), 056; the 2026-08-25
  retirement of the ADR 021 appendices.
- Must know: destination by type; extraction gate; inbound handling; redirect;
  baseline retirement; the decision-audit exception (ADR 074).
- Current home: `retire-artifact.md`; `commonplace-relocate-*` help.
- Gap: none obvious.

### 13. Change the scaffold, install layout, or projection

- Observed in: ADR 006, 013, 014, 021, 027, 037, 064.
- Must know: library/user split and path invariance; packaged-then-source
  resolution; no symlinks; one command version per OS user.
- Current home: `architecture.md`, `scenario-architecture.md`,
  `instruction-generation.md`, `INSTALL.md`; scaffold manifest in code.
- Gap: none obvious.

### 14. Change the freshness or review store schema

- Observed in: ADR 010, 031–036, 043, 052, 065.
- Must know: target/input/baseline model; acceptance is current state; schema
  migration is exceptional; identity is path-keyed; declared model partition is
  never re-derived from telemetry.
- Current home: `freshness-architecture.md`, `review-architecture.md`,
  `storage-architecture.md`.
- Gap: none obvious.

### 15. Change the documentation site

- Observed in: ADR 057, 061–063; every retirement's redirect.
- Must know: README-vs-index rule; redirect map constraints (no chains);
  which paths are excluded; article lifecycle states and their visibility.
- Current home: `documentation-site.md`, `retire-artifact.md` step 8,
  `kb/articles/COLLECTION.md`.
- Gap: none obvious.

### 16. Change always-loaded context (`AGENTS.md`, template)

- Observed in: ADR 002, 013, 022, 069, 074.
- Must know: what belongs in always-loaded context and what the template
  ships; the vocabulary section's role.
- Current home: `control-plane-goals.md`, `INSTALL.md`.
- Gap: none obvious.

### 17. Change the source-ingest model

- Observed in: ADR 045, 072, 073.
- Must know: ingest owns source authority; snapshots are local; quotes are
  verbatim-only; the two grounding routes.
- Current home: `kb/sources/COLLECTION.md`, the ingest-report type,
  `cp-skill-ingest`, `cp-skill-ground`.
- Gap: none obvious.

### 18. Adopt a borrowed idea into the framework

- Observed in: `source-adoption-policy.md`; ADR 015 (JSON Schema), 064 (uv).
- Must know: fast pass for programming patterns; demotion test for
  framework rules with boundary-preserving rivals.
- Current home: `source-adoption-policy.md`.
- Gap: none obvious.

### Candidates without a clear instance yet

Listed so a later session can look for evidence, not because they are admitted:
change the review execution medium (live-agent versus workflow); change the
tag system or a tag-README's marks; change a runtime skill projection on
Windows; change the freshness *model partition* registry. Each has ADR
touchpoints but no clean "this operation was performed" record found at this
pass.

## First-pass reference audit (unverified)

Which operation reads each `kb/reference/` artifact. "None found" means this
pass could not name one — a question for the next session, not a disposition.

| Artifact | Read by operation(s) |
|---|---|
| `architecture.md` | 5, 13 |
| `scenario-architecture.md` | 13 |
| `storage-architecture.md` | 9, 14 |
| `freshness-architecture.md` | 4, 14 |
| `review-architecture.md` | 4, 14 |
| `README-REVIEW-SYSTEM.md` | 4; also an operating guide (not a change premise) |
| `validation-contract.md` | 2, 3 |
| `collections-and-types.md` | 1, 2 |
| `collections-never-own-frontmatter-semantics.md` | 1, 2 |
| `collection-prototypes.md` | 1 |
| `link-vocabulary.md` | 1, 7 |
| `commands.md` | 6; also an operating reference |
| `documentation-site.md` | 12, 15 |
| `instruction-generation.md` | 5, 13 |
| `control-plane-goals.md` | 5, 16 |
| `navigation.md` | operating guide; no change operation found |
| `design-rationale-management.md` | 9, 10 |
| `source-adoption-policy.md` | 18 |
| `full-improvement-pass-closure.md` | 4 (routing of residual findings); weak |
| `where-change-candidates-come-from-in-commonplace.md` | none found — describes how changes are *noticed*, which precedes every operation; may be a reference-level description of the reflective loop rather than a premise |
| `commonplace-declared-frame.md` | none found — read when *assessing* Commonplace's self-improvement claims (article writing), not when changing it |
| `commonplace-as-an-instrument.md` | none found — same class as the declared frame |
| `tag-readme-trace-as-self-improving-loop.md` | none found — an application of theory to one episode; candidate for `kb/notes/evidence/` under ADR 070's witness test |
| `harness-sub-agent-model-selection-regression.md` | none found — dated operational incident; ADR 070 already left it in reference as the record of a provenance defect |
| `agent-memory-coverage.md` | none found — outward-facing account of what shipped surfaces realize; possibly article material |
| `commonplace-agent-memory-gap-plan.md` | none found — a plan, i.e. work in flight; candidate for `kb/work/` or a proposal |
| `definitions/collection.md` | 1 |
| `definitions/answerability.md` | 1 (admission boundary) |

Two readings of the "none found" rows are open, and the audit cannot choose
between them: either these artifacts serve operations this list does not yet
name (assess, publish, notice), or they are not change premises and ADR 074
sends them elsewhere. Resolving that is the next task, and it should start by
looking for the operation, not by moving the file.
