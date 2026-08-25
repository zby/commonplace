# Agent prompt — quote-grounding cohort 10b

Self-contained handoff. Point one agent at this file. It supersedes the retired
`## Claims`-ledger workflow still described in parts of the frozen cohort
record; use that record as the ownership manifest and historical inventory, not
as the current grounding procedure.

---

Complete source-grounding rollout cohort 10b in
`/home/zby/llm/commonplace`.

## Goal

Finish the nine target notes and eighteen ingests listed in
`kb/work/claim-grounding-rollout/cohort-10b.md` under the accepted direct-source
design:

- ingests retain only exact source/location pairs in `## Quotes`;
- an ordinary ingest link declares that those retained quotes are sufficient
  for that linked source use;
- an ingest link whose text contains the exact marker `(snapshot required)`
  declares that the full exact name-paired snapshot is required;
- `semantic/grounding-alignment` checks the note claim directly against the
  selected source material;
- ingest summaries, old paraphrased Claim fields, Scope, Confidence,
  Limitation, and target-specific transfer prose are never source support.

Repair the targets, complete the cohort work record, run fresh grounding
reviews, and commit the finished cohort.

## Starting state and recovery material

The direct-source implementation is established by these commits:

- `5e48d2d9` — `Check source claims against quotes or snapshots`
- `4db849e0` — `Clean up retired source grounding paths`

They must be ancestors of the working `HEAD`; `HEAD` may legitimately be newer
because other work is running in parallel.

Two stable stash commit IDs contain unfinished cohort work made under the old
Claims-ledger design:

- `0e5df2c7eba7f6ae111119125607ad3870d92e7b` — the completed source-blind
  inventory, the partial grounding record, and six modified ingests containing
  51 verified verbatim quote/location pairs;
- `95561752b9c859de25f61baf8e222f2c40b9d637` — the Huxley ingest containing
  three further verified verbatim quote/location pairs.

Treat both commits as read-only recovery evidence. Never run `git stash pop`,
`git stash apply`, `git stash drop`, or create a replacement stash. Do not use
the mutable `stash@{n}` names: another stash can renumber them. Read a retained
file only with its stable commit ID, for example:

```bash
git show 0e5df2c7eba7f6ae111119125607ad3870d92e7b:kb/work/claim-grounding-rollout/cohort-10b.md
```

Do not restore a stashed file wholesale. It predates the accepted data model
and would reintroduce `## Claims` and retired source-lens assumptions.

## Ownership and parallel-work boundary

You own only:

- `kb/work/claim-grounding-rollout/cohort-10b.md`;
- the nine target notes in its Targets table;
- the eighteen ingests named in that table.

The manifest remains authoritative for this path set. Do not edit the rollout
README, this prompt, cohort 10a, a source outside the manifest, shared
instructions, schemas, review gates, or runtime code.

Other agents may make unrelated changes. Start with `git status --short` and
inspect it again before every mutation phase and before committing. Preserve
and do not stage unrelated changes. If another agent has changed, staged, or is
actively changing one of your owned paths, stop and report the exact overlap;
append-only quote semantics do not make concurrent writes to one file safe.

The old manifest says cohort 10b must always run sequentially with 10a because
both appended to shared Claims sections. That statement is historical. The
operative rule is path ownership: do not overlap an active writer on either
bridge ingest, `goedel-machines-schmidhuber` or
`language-models-like-humans-show-content-effects-on-reasoning`. Their current
Quotes sections may already contain useful work from cohort 10a; preserve it.

## Required reading

Read these completely before mutation:

1. `AGENTS.md`
2. `kb/work/COLLECTION.md`
3. `kb/work/claim-grounding-rollout/cohort-10b.md`
4. `kb/reference/adr/073-untracked-source-snapshots-require-ingest-grounding.md`
5. `kb/sources/COLLECTION.md`
6. `kb/sources/types/ingest-report.md`
7. `kb/instructions/ground-source-dependent-claims.md`
8. `kb/instructions/cp-skill-ingest/SKILL.md`
9. `kb/instructions/review-gates/semantic/grounding-alignment.md`
10. `kb/reference/README-REVIEW-SYSTEM.md`
11. `kb/instructions/run-review-batches.md`
12. `kb/notes/COLLECTION.md` and every type contract declared by an owned
    target

Do not follow `kb/work/claim-grounding-rollout/procedure.md` where it conflicts
with ADR 073 or the current grounding instruction. In particular, there is no
Claims selection, source lens, per-ingest semantic pair, or normalized ingest
claim to reuse.

## Phase 0 — verify the base and frozen targets

1. Confirm both implementation commits above are ancestors of `HEAD`.
2. Confirm the two stash commit objects are readable without changing stash
   state.
3. Confirm each target's current blob still equals the frozen blob in the
   manifest. A newer unrelated repository commit is fine; a target mismatch is
   an overlap or named blocker and must not be silently refrozen.
4. Confirm every exact name-paired snapshot exists. Existence alone is not
   authority: verify canonical `source` equality and exact-byte SHA-256 before
   reading a snapshot or appending quotes.

## Phase 1 — recover and translate the completed work

Recover the source-blind inventory from the stashed cohort record at
`0e5df2c7eba7f6ae111119125607ad3870d92e7b`. It was completed before source
reading, so preserve its rows and frozen target wording rather than attempting
to recreate a source-blind inventory after seeing the sources.

Copy that inventory into the current `cohort-10b.md`, then translate the rest
of the work record to the current vocabulary:

- `quotes sufficient`
- `quotes added`
- `snapshot required`
- named blocker or literature handoff

An old normalized Claim may help identify which inventory need the prior work
was addressing, but it is not evidence and must not be copied into an ingest or
treated as a semantic premise. Rewrite old “entry reused/added” records as
direct quote or snapshot routes. Remove operational Claims-ledger, claim-ID,
source-lens, and whole-section-selection language from the live cohort record.

Preserve the previously identified outside-manifest needs as literature
handoffs rather than expanding source ownership: PS-2–PS-6, MO-2, and GM-8.
They are terminal cohort handoffs, not successful grounding results. Do not
create or modify an ingest for them in this task.

## Phase 2 — recover the 54 retained quote pairs mechanically

Recover only the exact `Source extract (verbatim)` and adjacent
`Source location` values from the old Claims entries. Discard Claim, Scope,
Confidence, Limitation, and every other interpreted field.

From `0e5df2c7eba7f6ae111119125607ad3870d92e7b`, recover:

| Ingest slug | Expected quote/location pairs |
|---|---:|
| `autogenesis-a-self-evolving-agent-protocol` | 5 |
| `continual-harness-online-adaptation-foundation-agents` | 7 |
| `darwin-godel-machine-open-ended-evolution-self-improving-agents` | 12 |
| `hyperagents` | 13 |
| `self-harness-harnesses-that-improve-themselves` | 6 |
| `self-improving-ai-coding-agents-through-accumulated-rules` | 8 |

From `95561752b9c859de25f61baf8e222f2c40b9d637`, recover:

| Ingest slug | Expected quote/location pairs |
|---|---:|
| `huxley-godel-machine-human-level-coding-agent-development` | 3 |

For each of these seven ingests:

1. Read the current complete `## Quotes` section first.
2. Compare exact extract/location pairs. Skip only a pair already present
   exactly; do not perform semantic deduplication or replace incumbent text.
3. Verify the exact name-paired snapshot against the current ingest's canonical
   source and `snapshot_sha256`.
4. Flatten each retained pair into the current adjacent form:

   ```markdown
   - **Source extract (verbatim):** <exact source bytes>
     - **Source location:** <retained locator>
   ```

5. Invoke `cp-skill-ingest` once per ingest with one `quote_append_request`
   containing all still-missing pairs for that ingest. Do not edit Quotes
   directly, and do not repair around a rejected append.
6. Validate the ingest immediately and record the route and result in the
   cohort file.

The recovery input total is 54 pairs. Record the exact incumbent, appended,
and rejected counts. If the recovered total is not 54, or the appended total
differs from 54 because concurrent/current work already supplied exact pairs,
explain the difference pair-by-pair. Do not force the count by duplicating
quotes.

## Phase 3 — finish every source-side need

Work from the recovered inventory, grouped by ingest. For every need, judge the
target's source-side proposition directly against current verbatim quotes. Read
no ingest analytical section as support.

First inspect `goedel-machines-schmidhuber`, which already has incumbent Quotes
from the completed architecture migration. Then finish the ten source-demand
rows that were pending in the recovered record:

- `agentic-code-reasoning`
- `towards-automating-eval-engineering-2079976006644072796`
- `why-software-factories-fail-slopcodebench-2081797628552270027`
- `agent-optimizers-compound-terminal-bench`
- `harness-updating-is-not-harness-benefit`
- `poetiq-perspective-on-recursive-self-improvement`
- `from-entropy-to-epiplexity-rethinking-information-computational`
- `language-models-like-humans-show-content-effects-on-reasoning`
- `beyond-not-novel-enough-llm-assisted-scholarly-critique`
- `towards-automating-scientific-review-google-paper-assistant`

For each need, use `ground-source-dependent-claims.md` exactly:

1. Return `quotes sufficient` if the incumbent exact passages contain enough
   context for a later reviewer to judge the proposition soundly.
2. Otherwise verify and read the exact name-paired snapshot.
3. If one or a few bounded passages are enough, retain the minimum sound set by
   one mechanical `quote_append_request` for that ingest and return
   `quotes added`.
4. If support is broad, distributed, or would require an oversized quotation,
   append no substitute paraphrase and return `snapshot required`.
5. If the snapshot is absent, mismatched, unreadable, does not establish the
   claim, or delegates the needed assertion to a secondary source, fail closed
   with the exact blocker. Do not browse for a replacement or infer support
   from model familiarity.

Process one ingest at a time and persist its result in the cohort record before
moving on. A route is selected per source-dependent use, not globally per
ingest. Similar and overlapping exact quotes may coexist; do not introduce IDs,
reconciliation, or semantic deduplication.

## Phase 4 — repair all nine target notes

Repair these current files, subject to their collection and declared type
contracts:

- `kb/notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md`
- `kb/notes/an-omitted-loop-function-and-a-frozen-one-need-different-repairs.md`
- `kb/notes/brainstorming-maintainability-oracles-for-agentic-development.md`
- `kb/notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md`
- `kb/notes/computationally-directed-self-improvement-is-a-reallocation.md`
- `kb/notes/epiplexity-by-example-what-entropy-and-complexity-miss.md`
- `kb/notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md`
- `kb/notes/structured-prompt-gains-do-not-establish-distribution-selection.md`
- `kb/notes/verifiable-subroles-before-reviewer-identity.md`

For every frozen inventory row:

1. Re-read the current target wording; preserve post-freeze improvements and
   unrelated edits.
2. Compare the target claim directly with its selected quotes or verified
   snapshot. Do not compare it with an old stashed paraphrase.
3. Retain, narrow, qualify, rewrite, or remove the claim according to what the
   source establishes. Thematic overlap is not support.
4. Keep target-specific synthesis and cross-domain transfer reasoning in the
   target and identify it as local analysis where needed; do not ask the source
   to state the target's conclusion.
5. Use an ordinary ingest link only when the linked use is fully judgeable from
   `## Quotes`. If not, put the exact text `(snapshot required)` inside that
   ingest link's visible label. Never rely on silent snapshot fallback.
6. Keep route association inspectable. If one ingest supports several claims
   through different routes, place links close enough to each use to make the
   marker's scope unambiguous, or add enough bounded quotes for a uniform quote
   route.
7. Treat a purely adjacent source link that makes no support claim as such;
   neither invent support nor add a marker merely because the link exists.

Record one terminal disposition per inventory row in the cohort completion
table. Use clear result names such as `grounded`, `narrowed`,
`contradicted/repaired`, `retained local delta`, `removed`, or `literature
handoff`, plus the selected source route and target change. A blocker must name
the exact missing evidence or failed identity check.

If target repair exposes a new need from an owned ingest, return to Phase 3 and
complete its direct-source route before resuming. Do not expand to an unowned
source.

## Phase 5 — run the operational semantic gate

Run a fresh `semantic/grounding-alignment` review for all nine targets through
the standard review job pipeline. This is one ordinary gate pair per note, not
a source lens and not one pair per linked ingest.

Follow `kb/instructions/run-review-batches.md` and
`kb/reference/README-REVIEW-SYSTEM.md` exactly:

- choose and record a real model partition that the current harness can run;
  do not omit the partition or invent a disposable one;
- select in requested mode so every owned target receives a new check;
- create jobs, run the captured prompts, and finalize the sentinel-bracketed
  results with matching runner/model provenance;
- do not acknowledge or migrate an old grounding baseline in place of a new
  semantic judgment;
- resolve every valid WARN or FAIL by repairing the target or its owned quote
  route, then rerun the affected note;
- a missing or mismatched snapshot for a `(snapshot required)` link is FAIL and
  remains a named blocker, never WARN;
- after finalization, rerun the ordinary selector under the same partition and
  confirm the intended grounding pairs are no longer stale.

Record the partition, job results, outcomes, fixes, reruns, and final empty
selector in the cohort completion record.

## Validation and cleanup

This task changes Markdown KB artifacts, not runtime code. Do not run pytest.

1. Run `commonplace-validate` on every changed ingest and target note.
2. Run the relevant source and note collection validations if they will not
   sweep in failures from unrelated concurrent work; otherwise report the
   individually validated owned paths and the unrelated obstruction.
3. Run `git diff --check`.
4. Scan the live cohort record and all mutated artifacts for operational
   leftovers from the retired approach: `## Claims`, `Claim (paraphrase)`,
   source lens/resolver language, raw-ingest criteria, source-specific review
   pairs, and paraphrased ingest content treated as evidence. Historical text
   in ADR 073 and warnings in this handoff are intentional; do not edit them.
5. Review the complete diff and `git status --short`. Confirm that both stash
   commit objects still exist and that no unrelated path is staged.

## Definition of done

The cohort is complete only when:

- the recovered source-blind inventory is present in the live cohort record;
- all 54 stashed verbatim quote/location pairs are accounted for and every
  accepted append passed the ingest skill and deterministic validation;
- every owned source-dependent use has `quotes sufficient`, `quotes added`,
  `snapshot required`, or a specific terminal blocker/handoff;
- all nine targets express only source claims supported by their declared
  route, with snapshot markers only where required;
- every inventory row has a terminal disposition;
- fresh `semantic/grounding-alignment` reviews have completed for all nine
  targets under the recorded model partition, with no unresolved in-scope WARN
  or FAIL;
- all owned changed artifacts validate and `git diff --check` passes;
- the live cohort record describes the Quotes/snapshot design and contains no
  operative Claims-ledger or source-lens workflow;
- unrelated work and both recovery stashes remain untouched.

## Commit and handoff

Review `git diff` first. Stage only the exact owned files changed by this task,
using explicit paths, and combine staging and commit atomically. Never use
`git add -A`, and do not stage this prompt merely because another agent left it
modified.

Use this commit message:

```text
Complete quote-grounding cohort 10b
```

Report the commit hash, quote recovery counts, per-route and per-disposition
counts, snapshot-required links, literature handoffs or blockers, validation
results, semantic-review model partition and outcomes, final selector result,
and confirmation that both stash commits remain intact.
