# Calibration design

Two tracks. A is cheap and produces the cost-side constants; B is the assay that produces the constants a cap must answer to. Run A first because it is mostly plumbing and B's jobs then carry usage for free.

## Track A — cost: usage regression

**Outcome variable.** Tokens per review job: input, output, reasoning, total. The codex runner reports these (legacy rows carry `last_usage`/`totals` with `input_tokens`, `output_tokens`, `cached_input_tokens`, `reasoning_output_tokens`); the live-agent path currently discards the worker's response and records nothing.

**Plumbing.** The contract already exists: `commonplace-finalize-review-job --telemetry-json` stores an opaque `harness_telemetry_json`. What is missing is the runner side — the executing instruction (`kb/instructions/run-review-batches.md`) tells the parent to ignore the worker's conversational output. Add: when the harness exposes usage, pass it. For codex, `codex exec --json` emits usage events; capture them into the JSON passed at finalization. No schema change, no review identity change.

**Data.** Every grounding review from then on. The 68-note population is currently all-PASS and fresh, so no rerun is needed; usage accrues from the next stale sweep and from Track B's jobs. Regress once n ≥ 50 with spread on both axes:

```
input_tokens   ≈ a₀ + a₁·artifacts + a₂·bytes        (mechanical: reading cost)
reasoning_tokens ≈ r₀ + r₁·artifacts + r₂·bytes      (effort: the attention proxy)
```

`a₁/a₂` is the per-artifact overhead of opening one more file against per-byte reading — the cost-side α/β. `r₁/r₂` is the nearer thing to attention: whether an extra artifact or extra bytes draws more reasoning. Report both; expect them to differ.

**Limits.** Bytes are not tokens and the ratio moves with content; count and bytes correlate across notes (r ≈ 0.78 in the 12-note sample), so check the condition number before trusting the split. A cost regression says what a review spends, not whether it stays right — it cannot set a quality cap on its own.

## Track B — degradation: paired packaging assay

**Outcome variable.** Detection of a known finding: hit or miss, per job. Severity recorded separately, not part of the hit rate (fixtures proposal).

**Fixtures.** Real grounding findings whose pre-repair text is in git: the four cap-attributable findings (jobs 8223, 8226, 8230, 8231; repaired in `c3fc6e1e`) and the eleven recertification repairs at sixteen (in or before `a6efeb52`). Recover each note snapshot and its linked ingests at the pre-repair commit into a fixture directory under this workshop. Label each independently — the finding text is in the job result files, but the fixture label is a person's or a fresh agent's confirmation that the snapshot instantiates the failure, not the reviewer's own verdict. Add an equal number of negatives: notes that passed uncapped with every artifact read (8220, 8222, 8224, 8227 and the like). Target ~12 positives, ~12 negatives.

**Leakage.** The reviewer must not see the finding. Pre-repair snapshots are safe; the repair commits and the evidence note are not linked from the fixtures. Fixture notes get new paths so no freshness baseline or prior verdict attaches.

**Packaging variants.** For each fixture, hold the evidence task fixed — the same claim, the same supporting passages — and vary how it is packaged:

| variant | artifacts | bytes | construction |
|---|---|---|---|
| base | as offered | as offered | the recovered snapshot |
| merge | fewer | same | concatenate the linked ingests into one or two files, links rewritten |
| split | more | same | cut each ingest into per-section files, links rewritten to the section holding the passage |
| pad | same | more | append plausible, non-bearing material (other ingests' analysis sections) to each linked file |
| split+pad | more | more | both |

Merge and split move only α's input; pad moves only β's. Bytes stay whole-file so charging matches V1.

**Criterion.** A trial copy of `grounding-alignment` in the catalog (`semantic/grounding-alignment-calibration-trial`) with *no* count limit — the assay measures degradation, so nothing may stop the reviewer early. Same execution contract as the paired assay: one note per job, fresh isolated worker, `codex` / `gpt-5.4` / high. Every job also carries Track A usage.

**Repeats.** The paired assay's capped repeat disagreed 1 in 5. Three repeats per cell is the floor; five if the budget allows.

**Size.** 24 fixtures × 5 variants × 3 repeats = 360 jobs. Cut to 12 positives × 5 × 3 + 12 negatives × 2 variants (base, split+pad) × 3 = 252 if needed; negatives matter mostly for false alarms under padding. Run in batches; stop early if the first 60 jobs show no detection movement across variants, and say so.

**Analysis.** Logistic fit `P(hit) ~ artifacts + bytes` on positives, with fixture as a random effect. α/β is the ratio of the slopes: how much detection one more artifact costs relative to one more kilobyte. The budget is the price at which predicted detection drops below the acceptable floor — a choice, stated in the ADR, not derived. False-alarm rate on negatives under pad and split+pad checks that padding does not manufacture findings.

**Possible null.** If detection does not move across the corpus range (up to ~25 artifacts, ~350 KB), the assay has shown the cap protects cost, not quality, in this setting. That is a result: the budget becomes Track A's cost budget and the ADR records that degradation was looked for and not found in range.

## Mechanism

What the reviewer is told and how it stops, independent of the constants' values.

**The constraint that shapes it.** Today the rule is "check at most N" and the agent keeps a count — imperfectly: one reviewer opened seven under a cap of five, and stops at exactly the cap self-report as "sufficiency". A price rule stated as "keep `α·n + β·bytes` under B" asks the agent to maintain a running sum of large numbers while doing the review. That is a worse instrument than the count, and the evidence for it would be indistinguishable from reviewer noise. So: the arithmetic lives in code, the agent gets small integers, and adherence is measured after the fact from `opened_paths` rather than trusted.

1. **Sizing → slots.** The pre-resolved link table already carries whole-file bytes per distinct target. Code prices each artifact, `α + β·bytes`, then converts price to an integer slot weight: `w = ceil(price / u)` where `u` is the price of a typical artifact for the partition (α + β·median bytes). Most artifacts weigh 1; a large ingest or snapshot weighs 2–4. The budget is a slot count `S = floor(B / u)`. With the current interim numbers this degenerates to exactly ADR 079's rule — sixteen slots, every artifact weight 1 — so the mechanism is a strict generalization, not a replacement.
2. **Prompt surface.** The pair block shows the table with a `slots` column and the line "budget: S slots". The reviewer chooses which artifacts to open — the command prices, it does not choose. Tallying small integers is the same skill as counting to sixteen, which reviewers do adequately.
3. **Stop rule.** Stop when the next artifact's weight would exceed the remaining slots. Reaching the budget is not WARN or FAIL (ADR 079). Name every material route left unopened and scope the verdict.
4. **Disclosure and adherence.** `opened_paths` stays the provenance; finalization prices them exactly as bytes are priced now, and records spend against S. Overspend is a telemetry fact, not a verdict change. If adherence is poor, the next step is a code-side meter (the harness refusing reads past the budget), not a stricter instruction — but that needs the read path to be tool-mediated, which the live-agent path is today and a future runner may not be.
5. **Scope.** Per pair. Per-job packing is a separate question (`review-bundle-packing`).
6. **Where the constant lives.** Two options, neither free:
   - in criterion text: hashed, so a change stales the population once (ADR 079's route) — but α/β and the budget are per model partition, so criterion text would carry partition-specific numbers;
   - as a partition parameter the prompt renders: no stale on change, but a judgment-shifting input outside the hash, which the review-gate type says owes a deliberate re-review.
   Decide in the ADR; the review-gate type's "judgment outside the freshness hash" paragraph is the premise.
7. **The other criteria.** Under a price, a gate's reading pattern is what gets charged: `misleading-link-text` reads a title and an opening paragraph per link (small β, one α each), `concept-attribution` reads one treatment per identity claim, `critique-note` reads what it needs. Each states its pattern; the budget is shared. The three fives go away.

## Mechanism B — code gathers the context (2026-08-25)

Posed by the maintainer after Mechanism A: for the criteria that need other artifacts, let code assemble the evidence pack instead of the reviewer opening files. Then the budget is a packing constraint and nothing is trusted to a tally. Recorded as the preferred candidate; Mechanism A remains the fallback for criteria that keep open-ended reading.

**What it dissolves.** The stop rule and disclosure obligation go away as mechanisms; the pack is the consumption record. Linked material becomes a known input, so pinning it for freshness is bookkeeping (closes the scope limit in the paired-assay evidence note without touching the lineage workshop's deferred refresh-state design). Notes are packed whole. Ingests are the one target type packed differently: an ingest represents a snapshot, and its evidential surface is its `## Quotes` section (ADR 073 — analysis elsewhere in the ingest is not support), so that section is what enters the pack. Packing the whole ingest was considered and rejected: it would put the KB's own analysis of the source in front of the reviewer as if it were evidence, which is exactly the contamination the grounding gate exists to catch. Charging then matches the route exactly rather than whole-file approximating it. Cost-side α (opening one more file) goes to near zero; only degradation-side α survives, which is Track B's quantity.

**What it costs.** The reviewer no longer chooses load-bearing links or follows a second hop. Acceptable for `grounding-alignment` (direct cited support), `misleading-link-text` (title + opening paragraph per target), `concept-attribution` (the target note's treatment; pack the note). `critique-note` may stay pull. Prompt schema, finalization, and the store change; this is the review-model change the splitting proposal described, not a gate edit.

**Splitting under code-push.** The hard part of the splitting proposal — partition by claim, which needs a semantic inventory — has a mechanical answer once code owns the pack:

1. Unit: a citing paragraph of the target note plus the packed evidence of the targets its links resolve to. Joint support within a paragraph stays together by construction.
2. Cross-paragraph joint support: build the paragraph–target bipartite graph and take connected components. One component = one pass: whole note for context, the component's paragraphs marked as under review, its targets' packed evidence. Nothing is severed unless two paragraphs cite disjoint targets.
3. Pack each pass up to the pass size; a component larger than the pass size falls back to a sampled pass for that component, disclosed — and is counted, because it is the case the tail must be watched for.
4. Combination at finalization: PASS iff every pass passes; FAIL if any fails; WARN aggregates. The pair remains the verdict unit; passes are its recorded inputs, each with its packed paths pinned.

**Pack shapes.** Two rules compose. By target type: a note packs whole; an ingest packs its `## Quotes` section, or the snapshot when the route requires it (the ingest stands in for the source, and only its verbatim extracts are evidence). By criterion: `whole` (default) or `head` — title plus opening paragraph, format-generic. `head` exists for `misleading-link-text`, whose test needs exactly that and would otherwise pay grounding's pack for a sentence check; for an ingest target `head` is its title and description. Nothing finer than these; a further shape is a special case and is refused. `misleading-link-text` is not subsumed by `grounding-alignment`: grounding examines links that ground a material claim, link-text examines every link's label against its target, including navigational and definitional links that ground nothing; they overlap on mislabelled support links and fail independently elsewhere.

**Pack transport: files, not inline text.** Inlining packed content in the prompt needs a boundary syntax — which file, which part — and every such syntax is a collision problem: a nonce per job with a hard fail if any packed content contains it is the known answer (MIME boundaries), but it is a second protocol to maintain. The alternative avoids the syntax: code **materializes the pack as files** in the job directory (`review-job-N/pass-K/pack/`, gitignored like the rest of the job artifacts) — a copy of each whole note, an extracted `<slug>.quotes.md` per ingest, `<slug>.head.md` under the `head` shape, the snapshot path where required — and the prompt lists those files with their sizes. The reviewer reads files with the tools it already has, exactly as it does today; what changed is that code chose the files. This is "code chooses, agent reads":

- budget control is exact — the pack *is* the selection, and per-pass packs are just directories;
- charging is exact — pack file sizes, with the ingest's Quotes file charged rather than the ingest;
- freshness inputs are the pack files' hashes, known at packing time;
- adherence is measured, not trusted: `opened_paths` outside the pack is a recorded violation, and the instruction says to read only the pack;
- the passage under review in a split pass is named by paragraph line ranges in the prompt, the same technique as the existing pre-resolved link table — no markers inside the note.

The nonce-fenced inline pack stays as the fallback for a runner without file tools. It is not needed for the live-agent path or codex.

**Measurable before any code.** From the existing resolved-link table: the component-size distribution per note across the corpus, in artifacts and bytes. That says how often splitting would fire at a given pass size, and whether oversized components exist. Do this first; it is a script over `resolved_links` plus paragraph link positions.

**What it changes in this design.** Nothing in Tracks A and B. The pass size is Track B's output — the pack size at which detection stays at the acceptable floor — and the budget question becomes "how large a pass" rather than "how many links". Mechanism A's slot table survives only as the fallback for pull-mode criteria.

### The full-source exception

Some claims cannot be carried by bounded quotes; ADR 073 lets the ingest declare the snapshot required for that route. Some snapshots are large. Both are rare, and their intersection is rarer, so the packing rule does not bend for them — they are an exception with a counted fallback.

Measured 2026-08-25: 1 of 296 ingests declares a snapshot-required route (8 notes carry the marker). Snapshots: 355 files, p50 25 KB, p90 109 KB, max 753 KB, 15 above 200 KB. A snapshot enters the pack only when a route requires it; a large snapshot behind an ordinary route costs nothing, because the pack carries the ingest's Quotes.

Rule:

1. Default pack: a linked note whole; an ingest's `## Quotes` section. A target whose route declares the snapshot required is packed as the snapshot instead, which also repairs the pricing proposal's under-charging of that route.
2. If the required snapshot fits the pass size, its component runs as an ordinary pass.
3. If it does not, that component runs in **pull mode**: the reviewer receives the snapshot path and the claim it must support, opens it under Mechanism A's disclosure rule, and the pass is marked `pull: snapshot exceeds pass size`. This is the only place pull mode survives inside a push-mode criterion.
4. Count it. The marker in the pass record is how the exception's frequency is known; if it stops being rare, the pass size or the route contract is what to revisit, not the packing rule.
