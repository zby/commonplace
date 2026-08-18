---
description: Use when source ingest receives a Papers with Code URL or the user requests an arXiv paper analysis grounded in its released implementation.
type: kb/types/instruction.md
---

# Ingest a paper with code

Use this conditional branch inside `cp-skill-ingest`. It replaces ordinary URL
snapshot resolution and adds code-grounding context to the normal connection,
drafting, validation, and reporting steps.

Keep the version-pinned paper snapshot as the primary source. Treat inspected
code as corroborating evidence pinned to a Git commit, not as proof that the
paper's experiments can be reproduced.

## Resolve and capture the paper

1. Extract the arXiv ID and any trailing version suffix such as `v2` from the
   Papers with Code or arXiv target.
2. For both target kinds, fetch
   `https://paperswithcode.co/api/v1/papers/{arxiv_id}?include_resources=true`.
   Use the response to discover paper metadata and associated repositories. Do
   not snapshot the Papers with Code page as the paper.
3. If that API is unavailable: for a Papers with Code target, extract the
   canonical arXiv URL and `codeRepository` values from the paper page's
   JSON-LD; for an arXiv target, take repository candidates from links in the
   paper or its abstract page. Treat either path as a resolver fallback, not
   paper evidence.
4. Resolve an unversioned target to the current arXiv version. Prefer the API's
   `version` when available. Otherwise inspect the arXiv PDF response's
   `content-disposition` header or the abstract page. Stop if no version can be
   established.
5. Set `paper_url` to
   `https://arxiv.org/abs/{arxiv_id}{version}` and invoke
   `cp-skill-snapshot-web` on it. Parse either `Snapshot saved:` or
   `Already snapshotted:` to obtain `source_snapshot`.

Use `https://arxiv.org/html/{arxiv_id}{version}` as a reading and navigation
surface when it contains the full paper. The PDF-derived snapshot remains the
durable capture. If HTML is absent or incomplete, read the snapshot; consult
the versioned TeX source only to resolve extraction problems in equations or
tables. Do not substitute a Papers with Code summary or generated read endpoint
for the paper.

## Resolve and pin the code

1. Start with repositories returned by the Papers with Code API or the
   fallback resolver (JSON-LD or paper links).
2. Prefer repositories marked official, but verify the association from
   primary evidence: the repository names the paper, arXiv ID, or released
   artifact, or the paper links back to the repository. Papers with Code is a
   discovery surface, not authority for the association.
3. If several verified repositories implement distinct claim-bearing parts,
   keep each necessary repository. Do not select by star count.
4. If the association is ambiguous, stop and ask which repository to trust. If
   no official or directly verified repository is available, report that a
   code-grounded ingest cannot be completed and offer the ordinary paper ingest.

For each selected GitHub repository, normalize the URL to
`https://github.com/{owner}/{repo}` and use
`related-systems/{owner}--{repo}/` as its checkout.

Before cloning, run `git check-ignore -q related-systems` from the main
project root; exit status 0 means the path is ignored. If it is not ignored,
stop and ask the user to approve an ignore rule rather than creating a large
untracked checkout. Create the directory when it is absent and ignored.

- If the checkout is absent, run `git clone "{repo_url}" "{checkout_dir}"`.
- If it exists, verify that `origin` resolves to the same owner/repository.
  From inside the checkout, run `git fetch --all --prune`, inspect
  `git status --short`, and stop if the working tree is dirty. Otherwise
  fast-forward with
  `git merge --ff-only @{upstream}`.
- Stop rather than repurposing a checkout, overwriting local changes, resolving
  conflicts, resetting, or forcing an update.

Record `reviewed_commit` with `git rev-parse HEAD` and construct:

- revision: `{repo_url}/commit/{reviewed_commit}`
- file citation: `{repo_url}/blob/{reviewed_commit}/{path}`
- directory citation: `{repo_url}/tree/{reviewed_commit}/{path}`

## Inspect the implementation

Read the top-level listing, README, manifests, central implementation files,
configuration, tests, training/evaluation scripts, and released result
artifacts that bear on the paper's main claims. Classify each relevant claim:

- **implemented** -- source code realizes the claimed mechanism;
- **artifact-supported** -- configs, tests, scripts, or result files expose how
  a claim was operationalized without independently verifying its run;
- **paper-only** -- the checkout contains no evidence beyond restating the
  paper or README claim.

Inspect details that clarify or contradict the paper. Do not install
dependencies, download weights or datasets, or run training or heavyweight
evaluation during ingestion. Run a cheap existing test only when the
environment is already ready and no download is required. Record exactly what,
if anything, was executed.

## Return to normal ingest

Continue at `cp-skill-ingest` Step 2 with:

- `source_snapshot` set to the version-pinned paper snapshot;
- `code_revisions` containing each pinned commit URL;
- the claim-to-code classifications and pinned file citations as drafting
  context;
- the paper version, checkout paths, reviewed commits, and execution status as
  final-report context.

During the normal draft step, include `code_revisions` in frontmatter and add a
`## Code Grounding` section after `## Summary`. Link pinned revisions and source
files. State the claim classifications and execution status. Carry findings
into `Connections Found`, `Extractable Value`, and `Limitations (our opinion)`
where they change the judgment.

Do not cite `related-systems/` paths or generated connect reports in the durable
ingest. Never describe source availability, static inspection, or passing unit
tests as reproduction of training, benchmark, throughput, or quality results.
