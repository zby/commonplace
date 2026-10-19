# Evidence for the sixteen unresolved targets

Use this evidence to resolve inherited holds and select previous publications
for the workshop's [publication comparison](../compare-publications.md). It is
not a packet for fresh source-first analysts and does not commission a new
source audit or worker-trace inspection.

## What is retained

- `captured/audits/` contains the five batch-23 content-hold reports, the three
  batch-22 incident reports, Ontology's positive content audit, and relevant
  predecessor audits. The JAZ-evals report is retained only because it was an
  explicit historical lead; it concerns a different system, not a seventeenth
  target. Older Sift-KG incident reports remain separate from its new incident.
- `captured/` also contains the Ontology scope stop, timeout tally, process
  outcomes and selected earlier recovery/ownership context.
- `publications/<target>/<run-id>/` contains **17 exact previous/held
  publications, 221 members**. These are captured evidence, not accepted new
  analyses. No baseline for a future comparison is selected automatically.
- [bindings.json](./bindings.json) retains selected original intake subobjects:
  the five batch-23 held cases, relevant batches 21–22 worktrees and decisions,
  and all sixteen targets' historical run/preparation/effect/state maps. These
  are projections, not copies with the complete original intake's hash.
- [manifest.json](./manifest.json) records original paths, pinned Git revision,
  original file hashes, exact report copies and publication-member hashes.

The transfer copied **27 reports/context records** byte for byte from revision
`defc4efaeeae631cff2a6f3f2370603df504b3ff`. All 17 available publication trees
matched their recorded complete membership and SHA-256 maps before copying.
This checked publication bytes only, not the truth of their claims, source
availability, worker traces, active writers or safety of recovery.

## Read the records without mistaking them for live instructions

Exact captures retain their historical wording, relative links, paths and
then-current requirements. Their relative links are interpreted from their
**original repository locations**, not from `captured/`. For a cited record,
first use the manifest to find a local capture. Otherwise retrieve its original
path at the pinned Git revision, for example:

```bash
git show defc4efaeeae631cff2a6f3f2370603df504b3ff:kb/work/agentic-system-reruns/batch-23-audit-intake.json
```

An audit's hash of the full original intake refers to that Git object, not to
`bindings.json`. Captured instructions to conduct a fresh source audit or
re-audit are historical commissions, not the successor workshop's current
procedure. The current additional check is publication comparison only.
Existing content holds still need disposition through supported verification
or explicit operator decisions; comparisons cannot clear them. Incident holds
also remain unresolved.

The validation-ignore markers distinguish exact captures from live authored
artifacts. They do not attest to semantic correctness or waive the recorded
byte-binding checks. The index, manifest and new procedure remain live files.

## What remains external or in Git

Raw worker traces, frozen source checkouts, full run states and preparation
files were not copied or modified. Their original locations and historical
hashes remain in the reports/bindings, principally beneath:

- `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/`
- `/home/zby/llm/commonplace/.commonplace/worktrees/`

Neither publication captures nor audit prose replace raw evidence needed to
investigate an incident. Preserve these external files pending a separate
retention/disposal decision. Recheck availability and identity before use; no
new trace/source integrity or idleness certification was performed here.

Targets stopped before publication have no manufactured publication baseline.
Legacy authored reviews remain in their existing collections; they were not
copied as substitutes. Select them for comparison only through an explicit
coordinator decision under the current procedure. Batch launchers, full-corpus
snapshots and completed-target audit history remain in Git rather than being
copied into this workshop.
