# Owner-qualified publication namespace

The operator authorized this migration on 2026-10-15 before batch 18.
GitHub publications now use lowercase `owner--project` directories. Repository
punctuation is preserved, matching source-checkout names. Four document-source
publications keep their existing names.

## Result and evidence

Moved **66 GitHub publication sets** and updated incoming Markdown links.
All **910 files across 70 sets** match their original Git blob IDs exactly,
including manifests, member frontmatter, run IDs, findings and internal links.
The [migration ledger](./publication-namespace-migration.json) records the
baseline commit, old/new paths, source identities, run IDs and SHA-256 hashes.
No manifest was repinned. Source checkouts, frozen worktrees, runtime stores,
attempts, logs, receipts, publication-effect evidence and archives were not edited.
Existing audit reports received link-target updates only; their dispositions
were not changed.

For example, cobusgreyling's wiki is now under
`retained/cobusgreyling--llm-wiki/`. It is not replaced by any of batch 18's four
same-project-name targets. Document-source naming remains outside this migration.

`publication_slug` controls publication, opening destination checks, retained
validation and current-analysis enumeration. `source_slug` still controls the
run-ID component. This separation preserves old run IDs and their preparation
tokens; new runs also keep the existing run-ID grammar. Owner qualification is
not a source-equivalence rule or permission to rename an existing source identity.

## Migration execution

The first relocation stopped because the relocation helper normalized sibling
links from `member.md` to `./member.md`. The guard caught changed accepted bytes.
Only that verified transformation was reversed, not unrelated changes. The
helper now preserves a link's spelling when it still resolves correctly after
the move. Regression tests cover bare, dotted and anchored sibling links.

Repeated per-directory repository scans exceeded two shell time limits. No
workers or analyses were launched. The remaining moves used a single-pass helper
built from the same relocation-library functions. Final verification compared
all publications with the original commit, including the earlier moves, rather
than relying on the resumed helper's narrower plan.

The retained helper is
`uv run python scripts/migrate_analysis_publications.py` (dry run).
`--apply --record <new-record-path>` performs the preflighted moves and records
hashes. It checks manifests and all destinations before writing, rejects duplicate
sources, and rejects required retained-member edits rather than silently
repinning accepted evidence. Use it only with exclusive mutation ownership.

## Frozen legacy integrations

This migration does not make old prepared commands owner-aware. Do not patch
frozen worktrees or change their pinned method to obtain the new naming.
Their audit holds remain in force.

Before any separately authorized legacy integration, compare source identities
with the origin's canonical publications:

- **Canonical incumbent present:** stop. A legacy integration at the old path
  does not establish replacement or archive correctness at the new path.
  Preserve the worktree and audit evidence for a separately planned transfer.
- **No incumbent:** after audit and explicit integration authorization, the
  original pinned integration may be followed by a separately authorized
  namespace migration in the origin. Review the dry run, retain a new ledger,
  and validate before exposing the result to current readers.
- Duplicate identities, destination collisions or member-byte changes are
  stop conditions, not grounds to overwrite a canonical publication.

The shipped [publication instruction](../../agentic-system-analyses/instructions/publish-analysis.md)
records this boundary. No legacy publication was integrated in this task.

## Verification

Regression coverage includes different owners of `llm-wiki`, GitHub URL
normalization and punctuation, unchanged document-source naming and run slugs,
opening destinations, publication guards, migration refusal cases and exact-byte
relocation.

- `uv run pytest -m '' -q`: **1,622 passed**, including slow tests.
- `uv run ruff check .`, `git diff --check`, and Bash syntax: passed.
- Migration dry run: **0 moves; 70 unchanged publications**.
- `commonplace-validate kb/agentic-system-analyses/retained`: **VALIDATION SUCCESS**;
  70 files analysed, 0 failures, 0 warnings. It reports notices for quotations
  whose recorded source-checkout paths are unavailable. This is not fresh
  verification of those quotations; the migration does not repair source paths.
- Edited collection, method and workshop Markdown: deterministic checks passed.

Batch 18 remains prepared and unlaunched; the migration is not authorization to
launch it or certify outstanding audits.
