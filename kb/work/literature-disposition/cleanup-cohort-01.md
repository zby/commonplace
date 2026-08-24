# Cleanup cohort 01 — reconstructed completion record

**Status: reconstructed 2026-08-24, not the original record.** Cohort 01 was
frozen by the claim-pull implementation workshop, executed, and then deleted on
closure **with its completion table still reading `pending` on all eight rows**.
The work was done; the record was not. This file rebuilds the table from
evidence, so the identity findings that rest on this cohort are auditable rather
than inferred.

Every disposition below is derived from the committed diff of `6177bd42`, the
two `Claims` entries it wrote, and the review store — not from recollection.
Where the original would have recorded a judgment made at the time, this records
a judgment made after the fact from its artifacts. That is weaker evidence and is
labelled as such.

## Freeze (recovered from `6177bd42^`)

Repository HEAD at freeze: `391c8321`.

| Target | Frozen blob |
|---|---|
| `kb/notes/agents-navigate-by-deciding-what-to-read-next.md` | `90a4c08c` |
| `kb/notes/linking-theory.md` | `e5914b43` |

One source: `kb/sources/pirolli-proximal-information-scent-distal-content.ingest.md`,
snapshot SHA-256 `dcbc5653…5e1da2`, matching the ingest's `snapshot_sha256`.

**One source, two targets, eight claim uses.** The unit is a target use, so
`linking-theory` gets its own rows even where it imported wording from the other
note.

## Grounded entries written

- **E1** — proximal cues such as links and citations give users concise
  information about content that is not immediately available; users assess
  proximal cues to choose actions leading toward distal information sources.
- **E2** — Pirolli treats cue validity and predictive strength separately from a
  general value-to-interaction-cost tendency; in the cited anchor-text analysis
  elaborated cues averaged 11.02 terms and correlated .16 with linked pages
  versus approximately zero with random pages.

## Completion record

Validation is `commonplace-validate` PASS on both targets. Source review is the
`source` lens pair, `verdict` / `pass`, recorded `2026-08-24T18:04:22`.

| ID | Disposition | Target change | Basis |
|---|---|---|---|
| AN-1 | narrowed | "That decision is the fundamental unit of navigation" → "This note uses that decision as a model of navigation; it does not claim that every navigation operation reduces to it." | E1's Limitation states the chapter "does not call follow/skip the fundamental unit of navigation" |
| AN-2 | narrowed | "always probabilistic: how likely… and what does it cost to find out?" → uncertainty framing with benefit and cost compared **in the LLM-agent setting**, no longer attributed | E2 keeps cue validity and the value-to-cost tendency separate; the join is local, not source-side |
| AN-3 | narrowed | tractability and avoided-load kept but relocated to the agent, with "diagnostic context" replacing bare context; E1 cited for the proximal/distal core plus an explicit transfer paragraph | E1's Limitation excludes "surrounding prose prevents target loading or thereby makes navigation tractable" |
| AN-4 | **contradicted / repaired** | "The more context a pointer carries, the cheaper the navigation decision" **deleted**; replaced by "More context is not automatically better" and uncertainty reduction per unit of context | E2: the analysis does not vary cue length and establishes no monotone |
| LT-1 | narrowed | now states the follow/skip model is "the KB's abstraction, not an attribution that follow/skip is the fundamental unit of navigation" | same as AN-1 |
| LT-2 | narrowed | "always probabilistic — the agent can't know what the target contains until loading it" **dropped** rather than grounded; replaced by the transfer statement | the universal pointer-level formulation is not in the source |
| LT-3 | narrowed | cites E1 for the proximal-cue/distal-source structure only, with "it does not inherit Pirolli's human mechanisms or cost model" | E1 as scoped |
| LT-4 | **contradicted / repaired** | monotone **deleted**; replaced by the Davison bound and "uncertainty reduction per unit of context consumed, not context quantity alone" | same as AN-4 |

**Distribution: six narrowed, two contradicted-and-repaired, zero grounded as
written.** No item was a false positive, none was blocked on an unavailable
source, and none needed an artifact-level disposition handoff.

## What this cohort does and does not license

It **does** support the shape findings recorded in ADR 073 and carried in
[the cleanup procedure](./cleanup-procedure.md): whole-section reading selected
the right entry without claim IDs, two entries served eight uses, and no
similar-entry accumulation or identity ambiguity appeared.

It **does not** support much beyond that, and the numbers are the reason: one
source, two targets, eight uses, one model partition. "No identity pressure
observed" in a two-entry section is close to a tautology. The paths that would
stress the design — several sources per target, an unavailable observation, a
disputed entry, a literature handoff — were all untouched here, which is why
[cohort 02](./cleanup-cohort-02.md) selects for them deliberately.

## Open items this cohort left

1. **Reviewed under the `codex` partition only.** Under the operator-default
   `claude-sonnet-5`, both source pairs return `missing-baseline`. The pass is
   real and partition-specific.
2. **92 other review pairs on the two targets went stale**, across
   `jargon-persistence`, `notation-opacity`, `undefined-terms` and others in
   several partitions. That is correct fallout from a substantive edit, not a
   defect, but it is outstanding and the deleted record never flagged it.
3. **The zero-grounded-as-written result was not fed back.** Eight uses, none
   surviving contact unchanged, is the strongest available evidence for cohort
   02's predicted distribution — and it was sitting in a table nobody filled in.
