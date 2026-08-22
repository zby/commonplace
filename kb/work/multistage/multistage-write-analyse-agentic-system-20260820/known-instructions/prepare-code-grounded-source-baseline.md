---
description: Workshop baseline for safely preparing and pinning a local GitHub source checkout once for all lenses in an external agentic-system analysis.
type: kb/types/instruction.md
---

# Prepare a Code-Grounded System Source

Use this procedure when an external agentic-system analysis is grounded in a GitHub repository. Prepare one local checkout and one immutable source dossier for every analysis lens. Do not let lens workers fetch, refresh, or select their own revisions.

This is a workshop extraction of the functioning source-preparation branch in `write-agent-memory-system-review`. It does not analyse the source, archive an incumbent review, write an artifact, run semantic QA, or cover document-only evidence.

## Inputs

- GitHub repository reference: `owner/repo` or `https://github.com/owner/repo`.
- Commonplace repository root.
- Optional established checkout path, only when an existing analysis already names one.

## Required output dossier

Return:

`repo_url | owner | repo_name | checkout_dir | origin_url | reviewed_commit | commit_url | checkout dirty state | refresh time and warning | top-level inventory | primary entry documents/manifests | file citation form | directory citation form | source ID | evidence layer | gaps/blockers`

The evidence layer is `implementation` for inspected executable source. Documentation within the checkout remains doctrine/design evidence unless implementation or run artifacts establish more.

## Steps

1. **Normalize identity.** Derive:

   - `repo_url`: `https://github.com/{owner}/{repo}` without `.git` or a trailing slash;
   - `repo_name`: the final path segment; and
   - default `checkout_dir`: `related-systems/{owner}--{repo_name}/`.

2. **Resolve an existing checkout without repurposing it.** If the default checkout exists, inspect its `origin` remote and use it only when it resolves to the requested repository. An established legacy basename-only checkout may be reused only when its `origin` resolves to the same repository. If a candidate path belongs to another repository, leave it untouched and use the owner-qualified path.

3. **Record the Commonplace worktree state.** Run `git status --short` at the Commonplace root before cloning or refreshing. This is collision evidence; it does not authorize changing unrelated files.

4. **Clone or refresh safely.** For a missing checkout, clone the canonical URL into the resolved owner-qualified path. For an existing matching checkout, run checkout-local commands from inside that directory:

   ```bash
   git fetch --all --prune
   git status --short
   git merge --ff-only @{upstream}
   ```

   Stop if the checkout has relevant local changes, no usable upstream, divergent local commits, or a non-fast-forward update. Do not force, reset, delete, stash, clean, or overwrite the checkout.

5. **Capture immutable identity.** From inside the checkout, record:

   ```bash
   git remote get-url origin
   git rev-parse HEAD
   git status --short
   ```

   The recorded commit, not a branch name or fetch time, is the shared revision for every lens.

6. **Capture the entry inventory.** Record the top-level listing, README or equivalent entry documents, package/manifests, and any repository-level `AGENTS.md`, `CLAUDE.md`, architecture, or design documents that govern source reading. This is a routing inventory, not evidence that every documented mechanism is implemented.

7. **Construct pinned citation forms.** Use:

   - commit: `{repo_url}/commit/{reviewed_commit}`;
   - file: `{repo_url}/blob/{reviewed_commit}/{source-relative-path}`; and
   - directory: `{repo_url}/tree/{reviewed_commit}/{source-relative-path}`.

8. **Record freshness.** Write or update the checkout-local refresh marker only after a successful clone or fetch-and-fast-forward. If drafting begins more than one hour later, attach a freshness warning. If more than 24 hours later, refresh again or explicitly retain the older pinned revision as the intended boundary.

9. **Freeze the dossier for workers.** Give every analysis worker the same checkout path, reviewed commit, dirty-state result, source ID, and citation forms. Workers may inspect but must not mutate or refresh the checkout.

## Failure branches

- If the repository is unreachable and no suitable checkout exists, stop with `source unavailable`; do not silently fall back to unpinned web claims.
- If only documents are available, return `code-grounded preparation not applicable` and route to a separately defined doc-grounded source procedure.
- If the checkout is dirty, identify the paths and state which conclusions could be contaminated. Do not discard or hide the changes.
- If origin identity is ambiguous, stop before fetch or merge.
- If the revision changes after any lens starts, invalidate every lens result and restart them from the new dossier.

## Verify

- The checkout identity matches the requested repository.
- The update, if any, was fast-forward only.
- Dirty state and refresh time are explicit.
- One immutable commit anchors every lens.
- Citation URLs are derived from that commit.
- No source worker can silently refresh, mutate, or substitute a different boundary.
