# Follow-up consistency scan — 2026-09-25

**Commission:** operator request to read the existing workshop and scan again
for additional contradictions. Findings only; implementing repairs is separate
work. Base commit: `2959ee61`, after ADR 088.

**Result:** four additional findings, two P1 and two P2. No new P0 observed.
The migration finding has two independently reproduced cases. Two statements
in the workshop's own bookkeeping also needed correction.

## Boundary and method

Read the workshop's existing ledger, witness file, and plans first. Compared
current doctrine, collection contracts, type specs and schemas, skills,
reference prose, and accepted decisions with their runtime consumers. Focused
the runtime probes on the recent type migration, type lookup, and review
selection. Inspected installation/build routing, validation, source capture
and grounding, authoring, relocation, retirement, and review interfaces. This
was a targeted follow-up, not a repeat of the previous wheel/sdist test or an
exhaustive review of every procedure and ADR. Linking semantics and lineage
remain outside this workshop's scope.

Ran bare `commonplace-*` commands from temporary projects using the current
editable installation. Temporary projects were removed afterward. No live KB
artifacts or review store were used as probe inputs. No pytest run was needed
for recording these Markdown findings.

The checkout was clean at entry. During the scan, concurrent edits appeared
on 28 files, mostly addressing the old ledger. The runtime files carrying I4,
H1 and H2 below were unchanged by that cleanup when checked. Existing-finding
status observations below distinguish those working-tree edits from committed
closure; line numbers should be re-derived before repair.

## I4 — P1: type migration leaves incompatible declarations

**Current promise.** [INSTALL.md](../../../INSTALL.md), line 330, says older
frontmatter `type:` and `requires_type:` values become the new form.
[ADR 088](../../reference/adr/088-type-values-are-paths-on-a-two-root-search-path.md),
lines 48–59 and 227–233, makes the KB-relative path the type identity and names
init as the installed-project migration consumer.

**Conflicting implementation.** In
[init_project.py](../../../src/commonplace/cli/init_project.py), lines 310–314
and 357–442, Markdown frontmatter is rewritten, but schema processing rewrites
only `$ref` values. It does not migrate a local schema's type identity
constraint. The frontmatter matcher also does not handle a single-quoted
scalar correctly.

**Probe A: local schema identity.** In a freshly initialized temporary project,
create `kb/notes/types/custom.md` declaring `type: type-spec`, `name: custom`,
a nonempty description, and `schema: ./custom.schema.yaml`. Give its schema
this constraint:

```yaml
type: object
properties:
  frontmatter:
    type: object
    properties:
      type:
        const: kb/notes/types/custom.md
```

Create an instance with `type: kb/notes/types/custom.md`, a nonempty description,
and a title. Run `commonplace-init` again. It exits 0 and rewrites the spec's
type and the instance's type. The instance now declares
`notes/types/custom.md`, while the schema still requires
`kb/notes/types/custom.md`.

`commonplace-validate kb/notes/custom.md` exits 1 with
`validation.schema.frontmatter-type`: `'kb/notes/types/custom.md' was expected`.
The post-migration artifact and its contract cannot agree.

**Probe B: ordinary YAML quoting.** Create a note with `type: 'note'`, a
nonempty description, and a title, then run init again. Init exits 0 but leaves
that value unchanged. Validation exits 1 and recommends
`type: types/note.md`. Single quotes are valid YAML, so this is a serialization
case of the advertised old value, not an invalid pre-migration type.

**Consequence and acceptance.** The advertised upgrade can leave a project
unable to validate. Repair must reconcile type identity constraints with the
migrated instances, handle supported YAML spellings, and check migration
idempotence. These probes establish neither whole-project migration coverage
nor support for every possible schema expression.

## H1 — P2: the promised project-wide collision diagnosis is absent

**Current promise.** ADR 088, lines 74–78, 175–180 and 227–233, says the health
check reports type collisions across a project.

**Conflicting procedure.** The
[health-check skill](../../instructions/cp-skill-health-check/SKILL.md), Step 2
and Step 6, runs `commonplace-init --check` and
`commonplace-validate landings` for an installed project. Neither enumerates
type collisions. `init_project.check_project`, lines 503–505, delegates only
to the library-pointer status check. No other step in the skill supplies the
promised type inventory check.

**Probe.** Initialize a temporary project, then add `kb/types/note.md` as a copy
of the library spec. Both commands above exit 0; every init-check entry is
`ok`. Validating a note with `type: types/note.md` exits 1 and correctly names
both colliding files.

**Consequence and acceptance.** The documented diagnostic path misses the
condition ADR 088 tells an operator it will find. Either implement and wire
that diagnosis into the procedure or amend the current guarantee. Pointer
health and landing health alone do not establish type health.

## H2 — P1: a type collision silently removes the conformance pair

**Current promise.** ADR 088 says a collision is an error wherever a type value
is resolved. The [review-system reference](../../reference/README-REVIEW-SYSTEM.md),
line 39, describes the `type` lens as deriving a pair for each typed note.

**Conflicting implementation.**
[type_conformance.py](../../../src/commonplace/review/type_conformance.py),
lines 80–101, intentionally skips malformed declarations, but its blanket
`except ValueError: return None` also swallows the resolver's collision error.
The selector consequently treats the typed note as having no applicable type
pair. This is distinct from H1: the review path actually calls the collision
check and discards its error.

**Probe.** In a fresh temporary project, create `kb/notes/example.md` with
`type: types/note.md`, a description and a title. Run:

```bash
commonplace-review-target-selector type --note kb/notes/example.md --json
```

Before adding the duplicate `kb/types/note.md`, it exits 0 with one
`type/note` target whose criterion is `commonplace:types/note.md`. After adding
the duplicate it still exits 0, with `targets: []` and no diagnostic. Direct
validation of the same note reports the collision.

**Consequence and acceptance.** An operator requesting type review can mistake
a type-binding failure for an empty review workload. Distinguish the collision
from the deliberately skipped malformed-declaration case and expose the
failure at the review boundary. A deterministic validation precheck catches
it, but the standalone selector remains a supported command.

## Q1 — P2: retirement requires a test run doctrine forbids

**Witnesses.** [AGENTS.md](../../../AGENTS.md), line 91, says not to run pytest
for changes confined to Markdown KB data that are not test inputs; use the
relevant validator checks instead. [Retire an artifact](../../instructions/retire-artifact.md),
lines 124–130, unconditionally ends its verification list with `uv run pytest`.

**Overlap.** Retire a normal Markdown note that is not a fixture or test input,
has never had a review baseline, and needs no redirect update. The root rule
forbids the test run and the procedure requires it for the same operation.
Root doctrine supplies the immediate precedence, but the procedure still
directs an incompatible action.

**Acceptance.** Qualify the retirement test requirement by the changed
surface, preserving the deterministic artifact checks. This finding was
established by reading the two instructions, not by retiring an artifact.

## Corrections and extensions to existing findings

- **M1 closure evidence was wrong.** `note-base.schema.yaml:40` has
  `additionalProperties: true` inside `frontmatter`. The `false` at line 56
  governs the outer validation object. A temporary note carrying
  `areas: [retired-field]` validates with zero warnings or failures. This
  corrects the asserted enforcement evidence; it does not establish that the
  retired Areas procedure has returned or authorize a new validator feature.
- **The implementation plan contradicted G1's closure.** Its proposed guard
  against a path-valued global `type:` is the opposite of ADR 088. The plan
  now calls for the adopted KB-relative path form and rejection of retired
  spellings. The old X1 complaint that project-shared types were omitted is
  also superseded: ADR 088 deliberately removed that eligibility.
- **Extend X1 with residual type tables.** `source-review.md:24` still tells
  authors to put `source-review` in the type field;
  `agent-memory-analysis-report.md:29` says `agent-memory-analysis-report`;
  `type-spec.md:56` still says the instance type is the spec's “own repo path.”
  Their current schemas/resolver require the ADR 088 form. These are narrower
  authoring remnants of G1, not a reason to undo its adopted decision.

## Existing findings and concurrent cleanup

R1, U1, V2/V3 and N1 still had their reported operative witnesses during this
scan. T1 and E1 retain their named owners. D1, A1, L1, K1, O1 and several
A2/X1/X2 items were receiving concurrent working-tree repairs; do not count
their original descriptions as new findings or treat this scan as verification
of that cleanup's completion. In particular, amendment markers appeared on
ADRs 014, 022, 027, 038 and 039; ADR 068 already carries its ADR 088 amendment.

The suspected installed-library article-schema problem was discarded:
`hatch_build.py` ships instructions, notes, reference and global types, not the
articles collection. Likewise, snapshot immutability is explicitly amended by
ADRs 087 and 088 for the recorded type-line migrations; that exception is not
a new contradiction.
