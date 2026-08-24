---
description: Draft delegated-worker instruction for grounding explicit external-source dependencies from a write candidate in tracked source ingests
type: kb/types/instruction.md
---

# Ground source-dependent claims

> Workshop draft. Intended target:
> `kb/instructions/ground-source-dependent-claims.md`. The V1 caller is
> `cp-skill-write`. Do not route live writes here until the section contract and
> caller handoff have passed the acceptance cases.

Use this instruction only as a fresh delegated worker after the caller has
identified one or a small set of explicit external-source dependencies in a
write candidate. Ground those claims in tracked ingests and return a compact
disposition. Do not write or edit the target artifact.

This is not a literature-discovery pass, a whole-note fact check, or a trigger
detector. Do not search for possible prior art, expand the supplied claim set, or
decide that an unlisted sentence probably needs a source.

## Inputs

Require a bounded handoff containing:

- `mode`: `new` or `edit`;
- `target_path`: the intended or existing library path;
- `intended_contribution`: one sentence giving the target's purpose;
- `claims`: a transient numbered list, where each item contains the exact
  candidate wording, the named source or ingest, `authority_role: primary`, why
  the claim matters to the target, and the exact candidate transfer argument or
  `none`; and
- for edit mode, the incumbent wording when it is needed to show what changed.

The numbers exist only in the handoff and result. Never persist them as claim
IDs. Stop with `BLOCKED` when the packet asks for broad discovery, omits the
candidate wording, or does not identify the source closely enough to resolve an
ingest. Do not compensate by loading the complete target or searching the
corpus.

V1 accepts only claims whose evidential authority is the ingest's primary
source. If an item depends on an implementation repository or another
`secondary_sources` resource, or the authority is ambiguous, return `BLOCKED`.
Never check such a claim against the primary snapshot merely because that is the
only observation carrying `snapshot_sha256`.

`transfer argument: none` asserts that the candidate stays within the source
claim's own domain and scope. If the candidate actually extrapolates across
domains, mechanisms, populations, or operating conditions, return `BLOCKED`
rather than inventing the missing transfer argument.

## Procedure

1. Read the source collection contract and the ingest type contract. Work only
   on the ingests needed by the supplied claims.

2. Resolve each named source to its one tracked ingest. Confirm that the packet
   names the primary source as the claim's authority. When a canonical primary
   source is supplied but no ingest exists, invoke the existing source-ingest
   workflow and resume with the produced ingest. Do not select an alternative
   source.

3. Read the ingest's complete `## Claims` section before reading the source.
   Treat the section as a demand-built grounding cache, not an index that
   predicts every future use.

4. If the section already contains an adequate source claim with the required
   fidelity, location, scope, and source-side limitations, reuse it. Do not
   reread the source merely because another note now uses the same grounded
   claim.

5. If the claim is absent, ambiguous, or inadequately grounded, resolve the
   exact source observation named by `snapshot_sha256`. Use the sole local
   checksum match. If no exact local observation exists, return `BLOCKED` with
   `legacy recovery required`, the ingest path, expected checksum, and canonical
   source URL. Do not recapture, invoke `cp-skill-ingest`, or run a backup
   procedure from this promoted worker. The cleanup runner may recover legacy
   evidence through its temporary rollout procedure and then dispatch a new
   fresh grounding worker.

6. Read only enough of the source observation to determine what it establishes,
   where the support occurs, and the population, conditions, exclusions,
   confidence, and source-side limitations that bound it. Never fill a missing
   passage from model recall.

7. Add or revise the smallest clear entry in `## Claims`. Check exact wording
   against the resolved observation before marking it verbatim. Label a
   lower-fidelity paraphrase explicitly. Avoid an obvious semantic duplicate
   after reading the whole section. If the candidate uses an exact quotation,
   retain that exact span in the entry so the target's later `verbatim` citation
   can resolve against the tracked ingest.

8. Validate every changed ingest with `commonplace-validate`. On validation
   failure, restore the worker's change to that ingest and return `BLOCKED` for
   its affected items. Preserve source identity, capture provenance, checksum,
   links, and unrelated analysis.

9. Compare the grounded source claim with the candidate wording and the exact
   supplied transfer argument. Assign exactly one status to each transient
   claim:

   - `SUPPORTED` — the candidate is warranted within the stated scope;
   - `NARROW` — a specific narrower candidate is warranted;
   - `CONTRADICTS` — the source defeats the candidate as written; or
   - `BLOCKED` — evidence, source identity, bearing, or transfer remains
     insufficient.

10. Return only the compact result below. Do not edit the target, add its link,
    run broader connection discovery, or retain source text that the ingest
    contract does not require.

## Result contract

Return one block per transient claim:

```text
Claim: <handoff number>
Status: SUPPORTED | NARROW | CONTRADICTS | BLOCKED
Ingest: <repo-relative path, or none>
Authority: primary | none
Grounded source claim: <concise statement, or none>
Scope and fidelity: <boundary the caller must preserve, or none>
Required candidate change: <exact narrowing, transfer revision, or block reason>
Ingest changed: yes | no
Validation: pass | not-run | fail
```

Do not return the whole ingest or source. Include a short source span only when
the caller must preserve exact wording in the target.

## Caller boundary

The caller may save the target only after every dependency it retains is
`SUPPORTED`. A `NARROW` result tells the caller what may be repairable; after
changing the candidate claim or its transfer argument, the caller must dispatch
a new fresh grounding worker with the exact revised wording. `CONTRADICTS` and
`BLOCKED` prohibit the original candidate claim. The target links to the whole
ingest and states which grounded claim it uses and why any cross-domain transfer
holds. When the target reproduces exact wording, it applies the existing
`verbatim` convention and cites the ingest so ordinary quote validation checks
the downstream copy against the tracked extract.

The ordinary write caller never follows `legacy recovery required` into a
backup path. It reports or removes the blocked dependency. Only the bounded
semantic-cleanup rollout may recover the exact observation and redispatch this
worker. This keeps legacy recovery out of the steady-state authoring machinery.

A valid ingest addition may remain if the target later fails for an unrelated
reason. Restore only an invalid or partially written ingest mutation; a
source-grounded claim is not made false by abandonment of one consumer.

## Draft decisions still required

- Exact prose or bullet shape for one grounded claim and the empty state.
- Permitted fidelity labels and minimum support for paraphrase.
- Exact clean-context dispatch syntax in `cp-skill-write`.

Remove this section before promotion.

## Verify

- The task was a bounded caller-selected claim set, not discovery.
- Every claim named the primary source as authority; secondary or ambiguous
  authority was blocked before snapshot resolution.
- The complete `Claims` section was read before source recovery.
- The source was read whenever a claim entry was added or materially revised.
- Every changed entry carries source statement, location, scope, and fidelity.
- Exact wording matches the observation used during grounding.
- Changed ingests validate and unrelated ingest content is unchanged.
- The result is compact and the target remains untouched.
