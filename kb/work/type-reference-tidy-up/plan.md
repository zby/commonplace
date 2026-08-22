# Plan

Ordering is load-bearing: the consumers must be repointed before the menus are removed, or writing breaks between steps.

## 0. Confirm the inventory

Re-run the checks the README's table records, so later steps act on current state rather than this snapshot.

```bash
# every type spec on disk, with its declared name
for f in $(find kb -path "*/types/*.md" | sort); do
  awk 'NR==1&&$0=="---"{f=1;next} f&&/^---/{exit} f&&/^name:/{print $2"  <- '"$f"'"}' "$f"
done

# frontmatter types actually used in a collection (example: kb/reference)
for f in $(find kb/reference -name "*.md"); do
  awk 'NR==1&&$0=="---"{f=1;next} f&&/^---/{exit} f&&/^type:/{print $2}' "$f"
done | sort | uniq -c | sort -rn

# who reads the menu
rg -n "## Types" kb/instructions/ src/commonplace/
```

The peer-type question is settled at the validator boundary. Ordinary durable collections may use global types plus their own local types. The whole `kb/work/` subtree is exempt: it may point to any valid type spec because it is a lifecycle staging layer for work aimed at any collection and for experiments on the contracts themselves. The agent-complexity workshop used the real `kb/notes/types/structured-claim.md` contract to test whether theorem sketches fit it; two sketches were later demoted to `note` because the trial exposed a mismatch, while two retained the type. This ADR draft similarly uses the reference ADR contract while it is being prepared.

Do not copy a borrowed type into `kb/work/types/`. Type identity is path-valued, so the copy would be a new contract and would no longer test or stage against the actual type. No special declaration or agent routing is required: the artifact's `type:` pointer already identifies the contract, and the validator's path-based exception supplies the lifecycle allowance.

## 1. Consolidate type exposition — completed 2026-08-22

Make [`kb/reference/collections-and-types.md`](../../reference/collections-and-types.md) the single general current-state exposition. It now shows how collection and type contracts compose, how an artifact follows a path-valued `type:` pointer, how schema validation and semantic conformance consume the spec, common global and collection-local examples, and where the live type directories sit.

The useful mechanics from the former `kb/reference/type-loading.md` were absorbed into that page. The drifting `kb/reference/available-types.md` catalogue and the now-redundant loading page were retired. `kb/types/README.md` remains a concise, curated landing for global contracts and explicitly makes no completeness claim; the filesystem is the inventory. Inbound links and the legacy ProperDocs redirect now land on the consolidated page.

The canonical page remains faithful to current behavior while this workshop is open: it states that writing skills still read collection `## Types` menus and that validation does not yet enforce collection-local ownership. Steps 3–5 must update that paragraph atomically with the behavior change.

## 2. Audit clauses that are not enumeration — completed 2026-08-22

The [row-by-row audit](menu-clause-audit.md) accounts for all 27 entries in the 8 collection menus. No clause needs to move into a type spec: every type-wide restriction mentioned in a row is already stated by its type contract.

Two collection-local policies need to survive as ordinary collection prose when step 5 removes the menus: definitions of KB vocabulary belong under `kb/notes/definitions/`, and raw source captures may remain frontmatter-free while awaiting classification. Review gates need no migration: they belong to the instructions collection, and `review-gate` is an instruction type whose path supplies its complete type identity. This requires neither a subtype mechanism nor a change to the instruction contract.

## 3. Repoint the consumers

Three skills read the menu:

- `kb/instructions/cp-skill-write/SKILL.md:26` — the hard gate
- `kb/instructions/cp-skill-write-multistage/SKILL.md`
- `kb/instructions/cp-skill-snapshot-web/SKILL.md` — templates `type: {snapshot type path from the Types menu, ...}`

Remove the menu as an agent-side authorization gate. Resolve the type in four cases:

- for an existing typed artifact, open the spec named by its `type:` pointer;
- for a new write with an explicit type path supplied by the user or calling workflow, open that path;
- for a new write identified by shorthand, search Markdown files under global and collection `types/` directories, inspect their own frontmatter, and require one exact `name:` match;
- for a general new write with no supplied type, use `kb/types/note.md`.

A workflow that requires another type supplies its exact path, so it creates no separate lookup case. In particular, the snapshot workflow supplies `kb/sources/types/snapshot.md` and opens it before using its `genre` vocabulary. Implicit `text` remains an explicit request for unstructured capture rather than a fallback.

Open the chosen path and verify that it resolves to a type-spec doc. Do not add a `kb/work/` branch to the skills: the same lookup works there, and the validator owns the difference in eligibility. Validation already rejects missing type files, bare enum values, absolute paths, URLs, paths escaping `kb/`, and non-type-spec targets ([`collections-and-types.md`](../../reference/collections-and-types.md)). The new eligibility check rejects a peer-local type outside `kb/work/`.

Keep the skills' fail-fast posture: if a requested shorthand has no unique match or the chosen path does not resolve, stop and report that condition. Report every matching path when a name is ambiguous; do not add collection-specific precedence or guess a type path. After writing, run `commonplace-validate`; it is authoritative for collection eligibility.

## 4. Enforce collection-local eligibility

Current behavior is purely referential. `validate_type_path()` accepts a repo-relative or file-relative Markdown path that resolves under `kb/`; `resolve_type_definition()` then verifies that the target is a type spec and loads its schema. Neither function checks whether a collection-local type belongs to the artifact's collection.

Add a generic deterministic validation check after the type path has resolved:

- a type under `kb/types/` is global and valid in every collection;
- a type under the artifact's own collection-root `types/` directory is valid there;
- an artifact anywhere under `kb/work/` may use any valid type spec;
- a peer collection's local type fails everywhere else.

Keep path resolution and type-spec loading unchanged. The new check classifies the already-resolved artifact and type paths. Cover global, owned-local, forbidden peer-local, `kb/work/` peer-local, file-relative paths, and installed `kb/commonplace/<collection>/types/` paths in tests. The rule applies to artifacts inside a collection; leave namespaces without a `COLLECTION.md` unchanged unless their collection status is decided separately.

## 5. Replace the menus with a rule

`kb/types/COLLECTION.md` already shows the target shape. It does not enumerate:

> Every Markdown artifact in this collection other than `COLLECTION.md`, `README.md`, and `text.md` is a type spec and carries `type: kb/types/type-spec.md`.

Derivation-free, binding, cannot drift. Give each ordinary collection a sentence of the same kind: validation permits type specs from `kb/types/` plus this collection's `./types/`, resolved by path, with any collection-specific restriction stated as a restriction rather than a list.

Give `kb/work/COLLECTION.md` the lifecycle-overlay rule instead: any valid type spec may be referenced from anywhere under `kb/work/`. This exception does not make peer types work-local and does not change the artifact's current workshop lifecycle.

Preserve the two collection-local clauses identified by the [menu audit](menu-clause-audit.md) in the same change: put the definition placement rule in `kb/notes/COLLECTION.md` and the raw-capture allowance in `kb/sources/COLLECTION.md`. No other menu-row prose survives.

## 6. Fix the scaffold

`src/commonplace/_data/templates/user-{notes,reference,instructions}-COLLECTION.md` ship `## Types` as an empty section with commented examples. Apply the eligibility rule sentence there too. This also removes the phantom `kb/types/skill.md` from `user-instructions-COLLECTION.md`.

Check whether `commonplace-init` or `scaffold_manifest.py` asserts anything about the section before removing it.

## 7. Validate and close

`commonplace-validate` over the touched collections; `uv run pytest` because this change adds validator behavior, changes packaged scaffold data, and must update the snapshot type-pointer parity test that currently asserts a menu row. Changing every `COLLECTION.md` also changes its collection-conformance criterion snapshot, so inspect and deliberately dispose the resulting freshness changes rather than leaving them implicit. Then extract anything durable and delete this workshop.

## Open items

- Update `tests/commonplace/docs/test_type_contract_integrity.py`, which currently asserts the snapshot row in `kb/sources/COLLECTION.md`.
- The collection-conformance pair hashes and reviews the whole `COLLECTION.md`; removing the section stales the affected collection pairs even though no parser special-cases the heading.
