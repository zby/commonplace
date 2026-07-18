# Seeded-violation calibration — run 01

Executed 2026-07-18. Purpose: separate the two factors confounded in production catch rates — **incidence** (how often the corpus contains a violation) and **recall** (how often the reviewer sees one that is there) — per [gate-stats finding 6](./gate-stats.md), and adjudicate the three dead gates (absorbed vs blind).

## Design

Eight gates: the three dead ones (`frontmatter/title-as-claim` 0/66 production, `semantic/explanatory-reach` 7.5%, `semantic/load-bearing-qualifiers` 8.3%), three mid-rate judgment gates (`semantic/grounding-alignment`, `semantic/completeness-boundary-cases`, `prose/confidence-miscalibration`), two high-rate mechanical anchors (`accessibility/undefined-terms` 67%, `sentence/clause-packing` 59%). Per gate: 4 seeded items (donor note copies, exactly one crafted violation each) + 2 verbatim controls, blinded shuffled filenames, ground truth in manifests the reviewers were forbidden to open. Three seeder agents built the 48 items; eight separate reviewer agents judged them blind with production-shaped prompts (gate file as criterion, per-item Findings + Result, "PASS is a normal outcome"). Reviewer population: Claude-harness sub-agents — recall numbers are for this reviewer class, not for the codex/luna/sol partitions (whose 2–3× strictness variance gate-stats already established). Artifacts under `run-01/` (items, manifest, reviews).

## Results

Raw: **29/32 seeds caught, 2 control flags on 16 controls.** Four cases went to artifact-level adjudication; all four resolved:

| case | resolution |
|---|---|
| reach-B, reach-F "missed" | **Seed defects, not gate blindness.** The seeder hollowed two mechanism passages but the donor's central mechanism (the enforcement/teaching two-axis argument) survives verbatim at the item's core — the reviewer correctly found a load-bearing mechanism present. Valid reach seeds: 2, both caught. |
| qualifiers-B "missed" + control-C "flagged" | **Reviewer header misalignment, not misjudgment.** The review file's B/C/D sections describe items C/D/B respectively (verifiable from quoted titles). Content-aligned, all four qualifier seeds were caught and both controls passed. |
| terms-D control flag | **Defensible strict-letter finding on pre-existing text**: the verbatim donor glosses "constraining" inline but places the definition link two paragraphs after first mention; the gate's letter demands both at first mention. Real-corpus incidence, not hallucination — and a live demonstration of why this gate catches 67% in production. |
| grounding-E control | Correct INFO-only handling of a borderline (grounding on a self-described hedged synthesis); Result stayed PASS per contract. |

Adjudicated grid:

| gate | recall (valid seeds) | controls clean | production catch | reading |
|---|---|---|---|---|
| frontmatter/title-as-claim | 4/4 | 2/2 | 0.0% | **absorbed, not blind** |
| semantic/explanatory-reach | 2/2 | 2/2 | 7.5% | sees what's there; low incidence (weak n) |
| semantic/load-bearing-qualifiers | 4/4 | 2/2 | 8.3% | sees what's there; low incidence |
| semantic/grounding-alignment | 4/4 | 2/2 | 24.2% | followed links, quoted sources' own scope against each overreach |
| semantic/completeness-boundary-cases | 4/4 | 2/2 | 19.3% | generated boundary cases as instructed |
| prose/confidence-miscalibration | 4/4 | 2/2 | 34.2% | clean separation of own-construction vs sourced |
| accessibility/undefined-terms | 4/4 | 1/2* | 67.1% | *the one flag is defensible on real text |
| sentence/clause-packing | 4/4 | 2/2 | 59.2% | threshold applied accurately |

**Total: 30/30 valid seeds caught; zero clear false positives.**

## Findings

1. **Recall is not the bottleneck — production catch rate ≈ incidence.** For this reviewer class, gates see essentially everything seeded, judgment and mechanical alike. The incidence×recall confound from gate-stats resolves toward incidence: the lens gradient (mechanical 2–3× judgment) reflects what fresh writing actually contains, so the activation-gap interpretation stands on its own terms — writers really do violate the small mechanical distinctions far more often than the judgment-level ones.
2. **Dead-gate adjudication.** `title-as-claim` is *absorbed*: perfect recall, zero corpus incidence in 66 production runs — the convention is internalized. Options: retire, thin its schedule, or codify (its test is nearly mechanical). `explanatory-reach` and `load-bearing-qualifiers` see fine; their low production rates are low incidence — cheap low-yield insurance rather than broken instruments (reach's evidence is thin: n=2 valid seeds).
3. **Second-order exhaust, twice, from the calibration itself.** (a) Two of 32 seeds were defective — incomplete hollowing left the violation absent; seeding needs a self-check step (the seeder re-running the gate's own test against its seed before shipping — the self-application rule applied to the calibration pass). (b) The qualifiers reviewer wrote correct verdicts under wrong item headers — and the production worker contract has the same silent risk: finalization pairs verdicts to sentinel labels, not to content, so crossed headers would finalize cleanly with swapped outcomes. Cheap guard: require each verdict block to quote the note title, and have the finalizer check it.
4. **Blinding held well enough.** Reviewers knew nothing marked items as seeded; the 15/16 clean controls (plus correct INFO downgrades) show expectation pressure did not inflate false positives.

## Caveats

- Recall here is an **upper bound**: seeds carried single, deliberately clear violations; production violations co-occur, hide in long notes, and shade into judgment calls. A harder run would seed subtle variants and multiple-violation items.
- One reviewer class. Given luna/sol caught 34.3% vs 13.8% on identical text, per-partition calibration is the obvious next run if partition choice ever needs justification beyond cost.
- n is small throughout; treat per-gate numbers as adjudications, not measurements.

## Consequences for the workshop

- Systematisation claim A's activation reading is strengthened: catch rates now measure incidence for this reviewer class, so the 29.6% first-encounter rate is ~29.6% actual violation incidence in fresh writing.
- The "seeded-violation calibration" instrument moves from named to prototyped; rerun cost is ~11 agent tasks per 8 gates.
- New candidate second-order guards from finding 3: seeder self-check; verdict-block content binding in the worker output contract.
