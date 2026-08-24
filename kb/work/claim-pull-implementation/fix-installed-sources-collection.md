# Bug-fix procedure: install `kb/sources/` as a collection

> Implemented in commit `bffedcae` (`Install sources as a user collection`).
> Retain this handoff until its test, package, fresh-install, and rerun evidence
> has been accepted by the claim-pull prerequisite gate.

## Outcome

`commonplace-init` must install `kb/sources/` as the same kind of user-owned
collection as `kb/notes/`, `kb/reference/`, and `kb/instructions/`: it has a
local authoring contract and a curated landing from its first initialization.

This fix is a prerequisite for claim pulling, but it is not part of the
claim-pull implementation. A separate agent can complete and ship it without
changing ingest behavior, grounding instructions, quote verification, or the
proposed `Claims` section.

## Defect

The source checkout has treated `kb/sources/` as a collection since
`kb/sources/COLLECTION.md` was added. Before `bffedcae`, installed projects did
not reproduce that topology:

- `src/commonplace/scaffold_manifest.py` created `kb/sources/` and installed its
  local types and `.gitignore`;
- it did not install `kb/sources/COLLECTION.md` or `kb/sources/README.md`;
- collection discovery therefore treated installed `kb/sources/` as a support
  directory rather than a collection; and
- `commonplace-validate landings` did not expose the omission, because it only
  requires a landing after `COLLECTION.md` makes the directory a collection.

The intended boundary is:

> Tracked source analyses are authored collection content. Local captures under
> `kb/sources/.snapshots/` are ignored, hidden, immutable evidence
> materializations; they are not collection artifacts or durable link targets.

The dot-prefixed directory already keeps snapshots out of Commonplace's normal
visible Markdown walks. The `.gitignore` controls version retention. This bug
fix does not need a new visibility rule.

## Scope

Change only the installed scaffold and the documentation and tests that state
what it installs.

Do not change:

- `cp-skill-ingest`, `cp-skill-write`, or any other instruction;
- ingest or snapshot type semantics;
- the quote verifier or other collection traversal code;
- existing project files during `commonplace-init` reruns; or
- the claim-pull proposal, `Claims` syntax, or grounding guarantees.

The only Python behavior change should be the two new entries in the declarative
scaffold manifest.

## Procedure

### 1. Add the source collection templates

Create these scaffold-only files beside the existing user collection
templates:

- `src/commonplace/_data/templates/user-sources-COLLECTION.md`
- `src/commonplace/_data/templates/user-sources-README.md`

The collection contract must be generic to an installed project. It should
state:

- purpose: tracked analyses and durable records of external sources;
- quality goal: faithful source identity and capture provenance, separated from
  project-relative analysis;
- artifact boundary: tracked ingest reports are collection content, while
  `.snapshots/` contains ignored, immutable local inputs;
- naming, title, description, and mutation conventions;
- no durable links into `.snapshots/`;
- a small outbound-link grammar usable by ordinary project collections; and
- type eligibility through `kb/sources/types/` and shared `kb/types/` contracts.

Do not copy the claim-pull workshop's draft contract wholesale. In particular,
do not mention `Claims`, re-grounding, primary-only claim policy, or future
worker behavior. Those decisions have not shipped and belong to the later
claim-pull implementation.

The landing should identify tracked source analyses, link to
`./COLLECTION.md`, explain that local captures live under `.snapshots/`, and
state the empty collection state. It must not link to
`kb/commonplace/sources/`: the installed Commonplace library does not ship that
collection.

### 2. Add both templates to the manifest

In `src/commonplace/scaffold_manifest.py`, add file mappings for:

- `templates/user-sources-COLLECTION.md` → `kb/sources/COLLECTION.md`
- `templates/user-sources-README.md` → `kb/sources/README.md`

Keep `.gitignore` and the existing source type tree mappings unchanged. Do not
special-case sources in `init_project.py`; its existing copy-and-preserve
behavior is sufficient.

The templates already live inside the Python package tree. Do not change Hatch
force-includes unless a built-wheel check proves that they are absent from the
wheel.

### 3. Make the regression tests direct

Amend `tests/commonplace/cli/test_init_project.py` to prove all of the
following:

- a fresh project contains both source collection heads;
- `kb/sources/` satisfies `is_collection_dir` or equivalent collection
  discovery;
- `validate_collection_landings` passes with sources included;
- a second initialization creates neither file again; and
- user edits to both files survive a rerun and are reported as preserved
  differences.

Do not rely only on the existing landing test: without a `COLLECTION.md`, that
test silently omits sources from its candidate set.

### 4. Correct the shipped-system documentation

Update both descriptions of the scaffold:

- `INSTALL.md`
- `kb/reference/instruction-generation.md`

List sources with notes, reference, and instructions as a user collection that
receives both a `COLLECTION.md` contract and a `README.md` landing. Keep the
separate statement that `kb/sources/.gitignore` excludes local snapshots from
version control.

No instruction document needs amendment for this fix.

### 5. Verify source and packaged installations

During development, run the focused init tests as needed. Before handoff, run
the repository-required checks:

```bash
uv run pytest
uv run ruff check .
uv build
```

Because this changes packaged scaffold content, reinstall the editable tool as
required by `AGENTS.md`:

```bash
uv tool install --reinstall --python ">=3.11" --editable .
```

Then initialize a fresh temporary project and verify:

```bash
commonplace-init --root /tmp/<fresh-project> --name source-collection-smoke
```

From that project root, run `commonplace-validate landings`. Inspect that both
source heads exist, then edit each, rerun `commonplace-init`, and confirm neither
edit was overwritten. Repeat the fresh-project smoke test from the built wheel
if the normal release workflow does not already exercise wheel package data.

## Completion evidence

The implementing agent should return:

- the exact files changed;
- the focused and full test results;
- the built-wheel or release-workflow evidence that both templates are
  packaged; and
- the fresh-install and rerun-preservation results.

Once that evidence exists, the claim-pull workshop may assume a generic
installed source collection. It must still implement claim-specific behavior in
the ingest type and grounding path rather than assuming existing user-owned
collection contracts were upgraded.
