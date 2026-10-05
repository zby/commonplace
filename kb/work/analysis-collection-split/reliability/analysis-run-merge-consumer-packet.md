# Analysis run merge consumer packet

This packet follows [change a contract that several consumers read](../../../instructions/change-a-contract-that-several-consumers-read.md) for the run ID and integration command adopted by ADR 106.

1. **Declaration and scope.** ADR 106 decides the new ID and merge path. `prepare_analysis` emits the token; `AnalyseAgenticSystem.run_location` and `open` enforce it. The new start rule applies to prepared Commonplace source worktrees, not all consuming-project workflows. The schema regex continues to accept frozen legacy IDs.
2. **Consumer inventory.** Searches: `rg -n 'run_location\(' src tests` found the hook, one analysis override and one test definition; all were updated. `rg -n 'retained_overview_path|retained_artifact_path' src tests` found only their definitions and fixture uses; production helpers were removed and fixtures now use the stable source path. `rg -n 'AAS-YYYY-MM-DD-system-slug-nn' kb/agentic-system-analyses/types` found eleven type-prose uses across eight files; all were updated. `rg -n 'Do not remove the worktree|transfer the retained|Stage and' kb/agentic-system-analyses/instructions` found the skill and publication instruction; both now give integration and retention rules. The command reference and method-maintenance instruction consume the new operation and evidence keys.
3. **Schemas, emitters and fixtures.** Existing run-ID patterns accept the token as a segment and retain legacy validity. Preparation and workflow start emit new IDs. Tests cover tokenized starts, an override path, a mismatched token, a clean merge and a stale conflict. No migration rewrites frozen sets.
4. **Byte pins.** No retained set, archive or run-state bytes were rewritten. Type examples and instructions are not the archived set's member bytes. Existing pins remain untouched.
5. **Spellings and projections.** The old placeholder was present as literal Markdown type prose and a source docstring; those current forms were updated. Historical workshops, reports and archived evidence stay frozen. Promoted skill symlinks target the canonical skill; no new skill name or stub is required. The existing `commonplace-workflow` entry point exposes the new subcommand.
6. **Fresh and existing installs.** A fresh consuming project receives skill pointers through `commonplace-init`; this analysis setup command itself only prepares committed Commonplace source checkouts. Existing projects need no KB byte migration. Installed editable commands read this checkout; isolated worktrees keep their pinned command environment.
7. **Diagnostics and acceptance.** A missing, non-ready or foreign preparation record refuses a new start. A mismatched token refuses opening. Integration refuses an unmerged method commit, unrelated tracked changes and pre-staged changes; a conflicting merge aborts and retains the publication branch. The corresponding tests exercise the token and merge paths. The product probe is a fresh scratch project initialized and checked with `commonplace-init`.
8. **Historical witnesses and identity.** Legacy `AAS-...-nn` sets and historical reports stay valid. The stable retained directory is derived from source identity, never parsed from the run ID. No new artifact predicate, relocation, or generated index is involved.

The final current-source rescan found no old ID placeholder or old worktree
removal instruction in `src/`, the analysis collection or `kb/reference/`
outside historical proposals and ADRs. A fresh scratch project initialized
with `commonplace-init`, and `commonplace-init --check` reported its pointers
current. The project does not receive the source-checkout-only analysis skill;
this probe checks the generic installed pointers, not run preparation.
