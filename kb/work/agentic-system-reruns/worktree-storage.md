# Worktree storage and verified archival

## Decision and current result

On 2026-10-14 the operator approved external storage for new worktrees, cleanup of completed integrated worktrees after evidence verification, and a cold-storage approach for failed/held evidence. This is storage authority, not permission to advance analyses, integrate publications, rewrite frozen methods or dispose of unresolved failed-run evidence.

**Archived and removed 37 completed integrated worktrees.** Each had one own completed publication, clean Git status, matching publication bytes at a commit on main, and retained audit records. No matching active process was found; its run lock was held during archival and removal. Agemem was deferred because this inventory did not establish an audit record. All running, unintegrated, failed, held and other uncertain worktrees remain in place.

The primary disk's available space increased from about **44 GiB to 51 GiB** during the operation. The worktree directory decreased from about **43 GiB to 35 GiB**. These are concurrent-system measurements, not an exact attribution of freed blocks. Archive payloads total **4,415,092,361 bytes**; the external archive directory uses about 4.2 GiB including manifests and metadata. The separate root `related-systems/` directory was not changed.

No publication or completion count changed. Historical audit inventory paths now describe their inspection-time locations; an absent archived worktree does not mean its analysis failed or its publication disappeared. Future inventories must consult origin retained publications, verified integration history and the archive index as well as live preparation records.

## External locations

The external disk is `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372`.

| Purpose | Path below that disk |
|---|---|
| New worktrees for batches 15–16 | `outputs/commonplace-worktrees/batch-<number>-<output-key>` |
| Completed-worktree archives | `outputs/commonplace-worktree-archives/2026-10-14-integrated/` |
| Authoritative archive index | `outputs/commonplace-worktree-archives/2026-10-14-integrated/index.json` |
| New process logs | `outputs/batch-15/` and `outputs/batch-16/` |

An initial attempt to create `commonplace-worktree-archives` directly below the mount root failed with `PermissionError: [Errno 13] Permission denied`. No worktree had been changed. The mount root is root-owned; its existing `outputs/` directory is writable by the operator. The operation therefore used subdirectories below `outputs/`. Mount state and permissions were not changed.

[Batches 15–16](./failed-batch-reruns.md) now supply an operator preparation instruction to the analysis skill: use the existing `commonplace-analysis prepare --worktree <absolute-external-path>` route, then continue in the returned worktree with its returned command prefix. They do not launch a replacement harness inside a prepared tree. Each destination is batch-qualified; existing worktrees or sibling preparation records are skipped rather than reused. The scripts refuse an unavailable mount and require writable output/worktree parents. This placement is a binding instruction to the fresh coordinator, not a claim that a real analysis has exercised it yet. No new analysis was launched during storage work.

The four already-running pipelines (11–14) and their prepared environments were not moved or edited. Their paths remain on the primary disk. External worktrees still share origin Git metadata, and some environment symlinks depend on local Python installations. External placement reduces source/working-file growth; it is not a portable self-contained installation or zero primary-disk usage.

## Archive verification and cleanup boundary

The archive index records every exact run ID, original worktree/preparation paths, method revision, source identity/revision/path, saved worktree HEAD, audit paths, verified main commit, archive/manifest/preparation locators and SHA-256 hashes, per-run status and completion time.

For each of the 37 worktrees:

1. Rechecked the single own run, completed publish effect, exact publication file set/hash map, clean Git status, worktree HEAD ancestry and full publication bytes at a main commit. Audit record existence and prior retained inspection supplied extracted evidence; this operation did not perform a new semantic audit.
2. Checked live same-user commands and readable working directories for the worktree/token; acquired its existing run lock nonblocking. This is cooperative scheduling protection, not a system-wide proof that no arbitrary process can read a file.
3. Archived the whole worktree, including cloned-source Git data, ignored run state, rejected/partial versions, local environment, instructions and retained files. Saved the sibling preparation record separately.
4. Fully extracted the archive into a temporary external directory and compared every regular file's SHA-256/size, directory/file modes and symlink target. Checked the restored primary Git source HEAD where applicable. Archive member paths and symlink-parent relationships were checked before extraction. No huge operator batch logs outside these worktrees were moved or copied.
5. Rechecked the original file manifest, preparation bytes, Git status, process references and mount before removal. Finalized archive hashes/status before issuing `git worktree remove`, without force. Removed its local preparation record only after successful worktree removal; updated the archive index durably.

The archived tree includes its old root `.git` pointer, but Git registration metadata lives in the origin repository. Removing a worktree deletes that registration. **An extracted archive is therefore not automatically a registered, runnable worktree.** Restoration must recreate Git registration and index at the original path; the old `.git` pointer must not overwrite a different newly generated registration. The origin repository and its method/HEAD commits remain required. Analysis branches were kept; there was no branch deletion or Git pruning.

## Restore pilot

After archival/removal, **Agno** (`AAS-2026-10-13-agno-60e6e09dd4a6-01`) was restored at its exact original path from the archive:

- Recreated detached Git registration at the archived HEAD without an initial checkout.
- Restored the archived tree without replacing the newly generated root `.git` file; rebuilt the Git index from that HEAD and restored the sibling preparation record.
- Verified manifest file hashes, modes and symlink targets, and clean Git status.
- Executed the restored local Python binding check: the Commonplace engine resolved to that worktree's `src/commonplace/artifactrun/engine.py`.
- From the restored worktree, its recorded local `commonplace-validate` validated the publication set: **VALIDATION SUCCESS**, Files analysed 1, Text files 0, 0 failures and 0 warnings.
- Removed the temporary restored registration/worktree and preparation again. Its archive remains intact. No run was advanced or source acquired.

The index records this pilot. It establishes same-origin, original-path restoration for this worktree, not recovery on a different machine or exhaustive executable restoration of every archived run.

## Deferred work

- **Agemem:** `AAS-2026-10-12-2601-01885v1-32274e5bddc1-01`, worktree `agemem-32274e5bddc1`, remains live because the prior inventory had no audit record. Establish audit retention/disposition before cleanup; integration alone is insufficient.
- **Failed and held runs:** remain outside routine cleanup. At the finished-run checkpoint, review their partial evidence and any uncertain public state, record the per-run retention/recovery decision, and archive with the same verified procedure before considering local removal. Do not infer that this approval releases a semantic hold or authorizes deleting rejected evidence.
- **Unintegrated publications:** retain live worktrees until authorized integration/replacement decisions and audits are complete.
- **New external worktrees:** future enumeration must scan their sibling preparation records under the external parent, not just `.commonplace/worktrees/`. Recorded preparation tokens, not directory-name inference, bind run identities.
- **Shallow/shared clones:** not implemented. Prospective acquisition changes require checking source-history consumers and preserving independent frozen working trees; do not rewrite current clones.

The next storage review is after the active runs finish, or earlier if primary-disk capacity becomes critical. The live archive index takes precedence over an interrupted session's memory; reconcile its `archiving` or `removal pending` states before any repeated operation. Never overwrite an existing archive or assume a partial archive authorizes removal.

## Verification

Archival/restoration checks and outcomes above were executed, not inferred from archive existence. No method, dependency or production code was changed.

- Bash syntax passed for scripts 15–16.
- Mock-only shell checks passed: all 22 source/placement prompts, exact Sol/medium arguments, preexisting worktree and preparation skips, repeat log skips, continuation after a mocked process exit 7, initial and mid-pipeline mount failure, and invocation outside the repository. No real Pi or preparation command was launched.
- `uv run pytest tests/commonplace/general tests/commonplace/agentic_analysis`: **469 passed, 96 deselected** by the default marker filter, in 51.72 seconds. No relevant slow-test behavior changed; this is selected coverage, not the complete suite.
- `commonplace-validate` passed for this record, failed-batch rerun record, workshop README and updated audit inventory: each analysed one text file, with zero failures or warnings.
- Final reconciliation confirmed all 37 archives/manifests/preparation backups present, metadata digests matched, original worktree/preparation copies absent, and deferred Agemem still present. `git diff --check` passed. No staging, commit or push was performed.
