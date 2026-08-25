# Consumed-cost calibration pilot

Selected 2026-08-25 after consumed-cost capture shipped in `708d65b4`. This is
a bounded pilot before any production gate edit or broad re-review.

## Question

Does the new per-pair report produce enough complete, uncensored observations to
justify a larger calibration run? In particular:

- do reviewers reliably report distinct opened paths and a stop reason;
- do any reviews stop for sufficiency before the current five-link cap binds;
- does the pilot vary artifact count and whole-file bytes independently enough
  to support a later estimate of their relative cost?

If most rows stop for `budget`, the current gate censors the natural stopping
point. Do not expand the same protocol in that case; design an uncapped
measurement-only assay first.

## Fixed selection

The population is the 68 tracked source-citing notes present at `708d65b4`,
recovered from their direct `../sources/*.ingest.md` links. Offered cost was
recomputed from the live files at `883ea974` using the same resolver and
whole-file charging code that creates review telemetry.

Artifact-count terciles are `<=9`, `10–13`, and `>=14`. Byte-volume terciles are
`<=84,786`, `84,787–133,999`, and `>=134,000`. Eight of the nine bivariate cells
are populated. Selection takes the bivariate medoid of each populated cell,
then adds four points greedily maximizing minimum normalized distance in the
artifact-count × byte-volume plane. Paths break ties deterministically.

| # | Cell | Note | Link occurrences | Distinct artifacts | Whole-file bytes |
| ---: | :---: | --- | ---: | ---: | ---: |
| 1 | low / low | `llm-generation-relaxes-goals-where-human-writing-stalls` | 9 | 7 | 61,449 |
| 2 | low / middle | `context-contamination-operates-below-an-agents-compliance-reasoning` | 10 | 9 | 89,749 |
| 3 | low / high | `diagnostic-richness-constrains-outer-loop-learning-quality` | 8 | 6 | 195,965 |
| 4 | middle / low | `checked-outcome-licenses-episode-retention-not-abstraction` | 14 | 10 | 81,152 |
| 5 | middle / middle | `files-defer-centralized-schema-commitment-until-invariants-stabilize` | 11 | 11 | 107,915 |
| 6 | middle / high | `topology-isolation-and-verification-form-a-causal-chain-for-reliable` | 28 | 11 | 135,466 |
| 7 | high / middle | `compounding-is-tested-in-later-improvement-not-by-the-accepting-metric` | 24 | 14 | 132,615 |
| 8 | high / high | `treat-continual-learning-as-representational-form-coevolution` | 20 | 16 | 168,153 |
| 9 | high / high | `automating-kb-learning-is-an-open-problem` | 33 | 22 | 322,097 |
| 10 | high / high | `theory-mediated-learning-may-improve-sample-efficiency-under-shifts` | 36 | 21 | 203,329 |
| 11 | low / low | `criteria-edits-invalidate-verdicts-process-edits-invalidate-artifacts` | 4 | 3 | 21,599 |
| 12 | high / high | `axes-of-artifact-analysis` | 29 | 23 | 260,372 |

## Execution contract

- requested `semantic/grounding-alignment` reviews under the `codex` partition;
- one note and one isolated fresh reviewer context per job;
- concrete worker model `gpt-5.4`, effort `high`;
- finalize through the ordinary review pipeline so availability and consumption
  sit together in `review_jobs.telemetry_json`;
- stop after these 12 jobs and inspect completeness and censoring before any
  expansion;
- do not edit the production gate in this pilot.

## Results

Jobs 8202–8213 ran as specified. All 12 reports finalized with complete
consumption telemetry. No row has a missing field, malformed field, or unpriced
opened path. The stale selector returns no target among the 12 under `codex`.

| Job | Note | Offered artifacts | Offered bytes | Opened artifacts | Charged bytes | Stop | Outcome |
| ---: | --- | ---: | ---: | ---: | ---: | --- | --- |
| 8202 | `automating-kb-learning-is-an-open-problem` | 22 | 322,097 | 5 | 68,940 | sufficiency | PASS |
| 8203 | `axes-of-artifact-analysis` | 23 | 260,372 | 5 | 55,445 | sufficiency | PASS |
| 8204 | `checked-outcome-licenses-episode-retention-not-abstraction` | 10 | 81,152 | 5 | 49,944 | sufficiency | PASS |
| 8205 | `compounding-is-tested-in-later-improvement-not-by-the-accepting-metric` | 14 | 132,615 | 5 | 56,781 | sufficiency | PASS |
| 8206 | `context-contamination-operates-below-an-agents-compliance-reasoning` | 9 | 89,749 | 5 | 52,985 | sufficiency | WARN |
| 8207 | `criteria-edits-invalidate-verdicts-process-edits-invalidate-artifacts` | 3 | 21,599 | 3 | 21,599 | sufficiency | PASS |
| 8208 | `diagnostic-richness-constrains-outer-loop-learning-quality` | 6 | 195,965 | 5 | 92,859 | sufficiency | PASS |
| 8209 | `files-defer-centralized-schema-commitment-until-invariants-stabilize` | 11 | 107,915 | 5 | 43,868 | sufficiency | WARN |
| 8210 | `llm-generation-relaxes-goals-where-human-writing-stalls` | 7 | 61,449 | 4 | 39,497 | sufficiency | PASS |
| 8211 | `theory-mediated-learning-may-improve-sample-efficiency-under-shifts` | 21 | 203,329 | 5 | 66,334 | budget | WARN |
| 8212 | `topology-isolation-and-verification-form-a-causal-chain-for-reliable` | 11 | 135,466 | 7 | 90,308 | sufficiency | WARN |
| 8213 | `treat-continual-learning-as-representational-form-coevolution` | 16 | 168,153 | 5 | 49,709 | sufficiency | WARN |

The median offer was 11 artifacts / 134,041 whole-file bytes. The median
consumption report was 5 artifacts / 54,215 charged whole-file bytes. Eleven
reviewers reported stopping for sufficiency; one reported budget. Nine of the
12 reports opened exactly five artifacts. Restricting the comparison to the 11
notes that offered more than five artifacts leaves nine at exactly five, one at
four, and one at seven. The seven-artifact report exceeded the gate's stated
five-link maximum.

## Interpretation

The transport works: reviewers can supply path-level consumption data, and the
finalizer can price and persist it without affecting the verdict. This pilot
does **not** identify the relative attention price `α / β`.

The current protocol supplies two putative cost inputs — artifact count and
bytes — but no independent observation of attention cost. A sufficiency stop is
set by the evidence needs of a particular note, so sufficiency points across
different notes do not lie on one shared attention frontier. A budget stop under
the current gate is set mechanically by the five-link rule, so it cannot reveal
the trade-off between another artifact and more bytes. The observed opened
artifact count and charged bytes are themselves correlated (`r = 0.777` in this
small selected sample), and nine exact-five reports show that the policy
compresses the count variation. Calling eight of those exact-five stops
`sufficiency` does not establish that the salient cap had no effect.

The 7 PASS / 5 WARN outcomes are useful review results but not attention-price
observations. The WARN results temporarily replaced five of the frozen
population's current `codex` PASS baselines, leaving the accepted `codex` or
`claude-sonnet-5` population at 63 PASS / 5 WARN before the repair below.

## Grounding findings to repair

- Job 8206: `context-contamination-operates-below-an-agents-compliance-reasoning`
  calls the contamination-isolation implication an inherited constraint, while
  the linked note supplies only the more general demotion heuristic.
- Job 8209: `files-defer-centralized-schema-commitment-until-invariants-stabilize`
  says the Fintool case is specific to its AWS setting and access patterns, but
  the ingest's retained Quotes do not establish that qualification.
- Job 8211: `theory-mediated-learning-may-improve-sample-efficiency-under-shifts`
  gives DiscoverPhysics an exact count of 22 simulated worlds that its retained
  Quotes do not support.
- Job 8212: `topology-isolation-and-verification-form-a-causal-chain-for-reliable`
  asks the KCSI Quotes to support a stronger shared-state qualification than
  they contain, and classifies scheduler separation as `topology + isolation`
  without making that target-side synthesis explicit.
- Job 8213: `treat-continual-learning-as-representational-form-coevolution`
  transfers the Bitter Lesson's historical pattern to a claim about current
  mainstream work subsuming prompts, tools, and evals without marking the step
  as synthesis or citing direct support.

## Repair completion

All five findings were repaired in the targets. No ingest or snapshot changed:
the retained Quotes in the Fintool, DiscoverPhysics, KCSI, and Bitter Lesson
ingests were sufficient once unsupported detail was removed and target-side
synthesis was named explicitly.

Fresh isolated `codex` reviews passed in jobs 8214, 8216–8218, and 8219. Job
8215 first returned an adjacent WARN because the file/schema note transferred a
progressive-constraining pattern from LLM runs to schema timing without naming
that cross-setting inference. The target now states the transfer directly, and
job 8219 passed it. The stale selector returns no target among the five, and the
accepted frozen population is back to 68/68 PASS.

## Decision

Do not expand the same capped protocol. It would add rows without resolving the
identifiability problem.

An uncapped arm is still useful for measuring natural evidence demand and for
testing whether sampled and fuller verdicts diverge. It does not by itself
identify `α / β`: that requires either an independent resource outcome (for
example model usage or elapsed active review time) or a controlled paired assay
that holds the claim and evidence constant while varying how the evidence is
divided among artifacts and how many bytes must be scanned.

The five WARN findings were repaired in a separate pass and only those pairs
were rerun. Keep the complete telemetry from this pilot as evidence about
reporting, cap adherence, and the observed demand distribution.
