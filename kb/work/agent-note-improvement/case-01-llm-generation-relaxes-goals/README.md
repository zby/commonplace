# Case 01: LLM generation relaxes goals

Target note: `kb/notes/llm-generation-relaxes-goals-where-human-writing-stalls.md`

## Frozen materials

- `baseline-e242c975.md` — version from `e242c975a2542b88d43b5d609ebbca27fd3bf3cd`.
- `current-2026-06-16.md` — current note copied on 2026-06-16.

Snapshot hashes:

```text
8496d3ca09551caeffbf04a33d98cf05a6c476ffd4cd64db61ed36393cfb0fc8  baseline-e242c975.md
83bbca223c98bad85f846c96b6667d3392bba764a3e6bb983de5eb2ea43c73e7  current-2026-06-16.md
```

## Accepted delta

The current note is mostly a subtractive revision of the baseline. It preserves the central claim: human composition stalls at unmet constraints while LLM generation emits a fluent relaxation that hides the dropped constraint.

The main accepted changes:

- Removed the section "Why the relaxation lands on the crux." Its typicality-biased crux-loss and friction/fluency inversion claims may be plausible, but they overreach the strongest established point.
- Replaced the longer "check moves to the reader, and gets harder" section with a shorter reader-cost statement. The accepted version keeps the displacement claim without the larger empirical prediction about under-witnessed throughput and difficulty becoming nondiagnostic.
- Removed "Relation to hallucination (hypothesis)." The analogy may be useful later, but in this note it bloated the argument and shifted attention away from the stronger witness/relaxation mechanism.
- Shortened the semi-decidability paragraph by dropping the extra burden-of-proof framing.
- Added a sentence acknowledging that human writers can also paper over gaps, while treating that as an exception rather than the default.

Working interpretation: the baseline was weak because it treated several plausible extrapolations as if they belonged in the same note. The accepted note keeps the load-bearing mechanism and demotes the speculative branches by deletion.

## Experiment log

### 2026-06-16: `critique-note`

Instruction under test: `kb/instructions/critique-note.md`.

Target: `baseline-e242c975.md`.

Generated report path: `kb/reports/critique/baseline-e242c975.critique.md`.

Workshop copy: [critique-note-report](./critique-note-report.md).

Result: partial hit.

What it found:

- It challenged the broad human-vs-LLM contrast and noted that human stalling is noisy rather than a reliable crux detector.
- It directly flagged the baseline's "typicality-biased relaxation lands on the crux" move as too strong. This matches the accepted deletion of "Why the relaxation lands on the crux."
- It objected that the "human pen stalls hardest / model is smoothest" formulation should be probabilistic unless supported by evidence. This also matches the accepted deletion.
- It noticed that the witness framing may over-formalize goals that are really trade-off negotiations.

What it missed or misdirected:

- It did not identify the main accepted edit as subtractive. The constructive findings mostly recommend adding qualifications and comparison units, which could make the note even larger.
- It did not flag the hallucination analogy as a low-yield speculative branch, even though the accepted version removed it.
- It attacked the central contrast more than it diagnosed which paragraphs were bloating a stronger core claim.
- It did not distinguish "weak but plausible extrapolation" from "false claim" clearly enough. The accepted revision removed plausible-but-underbuilt sections rather than refuting them.

Takeaway: `critique-note` is useful for finding overclaiming, especially when a speculative section states a strong generalization. It is not yet a good instruction for note improvement when the desired move is to preserve the central mechanism and prune plausible but underbuilt expansions. A follow-up instruction should explicitly ask for the strongest retained point, the lowest-yield sections, and the deletions that would make the note harder to attack.

### 2026-06-16: prune weak expansions

Instruction under test: [instruction-prune-weak-expansions](./instruction-prune-weak-expansions.md).

Target: `baseline-e242c975.md`.

Report: [prune-weak-expansions-report](./prune-weak-expansions-report.md).

Result: strong partial hit.

What it found:

- It correctly identified the strongest retained claim as hidden relaxation: the LLM emits a plausible witness for a weakened goal while leaving the dropped constraint unmarked.
- It named the central causal chain to preserve: constraint set, witness search, human stall, LLM relaxation, hidden dropped conjunct, reader-side audit.
- It correctly marked the hallucination analogy as a split candidate rather than core support.
- It recommended compressing the empirical prediction paragraph and code-oracle training speculation.

What it missed or misdirected:

- It kept the "Why the relaxation lands on the crux" section, though with compression. The accepted revision removed it completely.
- It treated the crux-typicality section as "the note's best explanation for why relaxation is not just concealment," while the accepted revision concluded the note did not need that explanation.
- It produced more split candidates than the accepted revision preserved, including verifier-oracle and friction/fluency branches.

Takeaway: adding an explicit "strongest retained claim + weak expansions" frame substantially improves the critique. The remaining failure is a preservation bias: when an expansion is interesting and mechanistic, the instruction still tends to compress or split rather than recommend deletion.

### 2026-06-16: split and rehome critique

Instruction under test: [instruction-split-rehome-critique](./instruction-split-rehome-critique.md).

Target: `baseline-e242c975.md`.

Report: [split-rehome-critique-report](./split-rehome-critique-report.md).

Result: best hit so far.

What it found:

- It preserved the same main note the accepted revision preserves: witness search, silent relaxation, and reader-side audit burden.
- It identified typicality-biased constraint shedding as a distinct mechanism claim that should not remain in the original note without its own support.
- It identified friction/fluency inversion as a separate diagnostic claim requiring evidence.
- It identified the hallucination analogy as a candidate new note with a distinct correspondence/coherence taxonomy claim.
- It demoted predictions, reconstructed stalls, code-oracle training effects, and codification extension to open-question or later-work material.

What it missed or misdirected:

- It recommended several possible new notes, while the real accepted edit simply deleted most branches from this note. The hallucination branch is the one that still looks most worth rehoming.
- It did not strongly distinguish "new note now" from "workshop lead until evidence exists." The instruction's next version should make evidence thresholding more explicit.

Takeaway: the split/rehome frame best matches the desired operation. It avoids treating every weakness as an objection to the core claim and instead asks which branch deserves deletion, open-question status, or its own note.

### 2026-06-16: semantic review bundle

Instruction path: `kb/instructions/run-review-bundle-on-note.md`.

Command path:

```bash
commonplace-create-review-run --runner codex --model gpt-5-5-high --json --with-prompt kb/work/agent-note-improvement/case-01-llm-generation-relaxes-goals/baseline-e242c975.md semantic
commonplace-ingest-bundle-output --review-run-id 2303 --input-file kb/reports/bundle-reviews/review-run-2303/bundle-output.md
```

Review run: `2303`.

Workshop copy: [semantic-review-run-2303](./semantic-review-run-2303.md).

Result: useful signal, with one artifact caveat.

Gate results:

| Gate | Result | Relevant signal |
|---|---|---|
| `semantic/completeness-boundary-cases` | PASS | No taxonomy-like coverage failure. |
| `semantic/explanatory-reach` | WARN | Flags the crux-typicality section as overextended and under-supported; notes the hallucination analogy is plausible but separate from the core explanation. |
| `semantic/grounding-alignment` | WARN | Mostly a workshop-copy caveat: relative links from the frozen snapshot did not resolve, so grounding could not be checked. Still notes that the speculative branches depend on unavailable support. |
| `semantic/internal-consistency` | PASS | No contradiction; only emphasis overreach. |
| `semantic/load-bearing-qualifiers` | PASS | Title/scope qualifiers are load-bearing; the problem is unsupported strengthening, not artificial narrowing. |

Takeaway: the existing semantic bundle can mark the main weakness through `semantic/explanatory-reach`. It does not by itself produce the strong editorial action "delete or split weak branches," but its finding is compatible with that action. The grounding warning is not a reliable conceptual signal in this run because the baseline was copied into `kb/work/`, breaking relative links in the review prompt.

## Interim comparison

| Method | Finds overreach | Finds subtractive edit | Finds rehome candidates | Main weakness |
|---|---:|---:|---:|---|
| `critique-note` | yes | weakly | no | Attacks the core contrast and recommends additions. |
| prune weak expansions | yes | partly | yes | Still wants to keep/compress some branches the accepted edit deleted. |
| split and rehome critique | yes | yes | yes | Needs a sharper threshold between new-note candidates and workshop leads. |
| semantic bundle | yes, via explanatory reach | indirectly | weakly | Review-gate output is diagnostic, not an edit plan. |

Current instruction hypothesis: the best next reusable instruction should combine `semantic/explanatory-reach`'s hard-to-vary test with the split/rehome action frame, then require an evidence threshold before preserving a weak branch as a new note.
