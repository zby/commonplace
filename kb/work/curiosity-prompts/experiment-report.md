# Curiosity Prompts Experiment

## Question

After writing a related-system review of Decapod, a human reviewer noticed that the "embedded constitution" — described as "compiled into the binary" and "crystallised" — was actually verbatim markdown copied via `include_str!()` with no transformation. The same result could be achieved by reading files at runtime. The crystallisation claim was illusory.

This was a valuable finding. Can we prompt agents to ask similar questions? What framing reliably surfaces insights about *pointless complexity* — mechanisms that work correctly but add no value over simpler alternatives?

## Setup

We reconstructed the original report (before the mechanistic investigation) in `decapod-original.md`. This version presents the constitution uncritically: "compiled into the binary," "maximum stabilisation, zero interpretive variance," "crystallised."

We tested 6 prompt framings, each given the same report and access to the Decapod source repo. Each prompt was run twice (two batches) for 12 total runs.

### Prompts

1. **Pure curiosity**: "What surprises you? What triggers your curiosity? What would you like to dig deeper into? Investigate."
2. **Cost/benefit**: "What choices seem unusual — where the cost/benefit isn't obvious? Follow your curiosity and investigate mechanistically."
3. **Impossibility**: "What claims describe something that would be hard or impressive to actually implement? Follow your curiosity — check whether the implementation matches."
4. **Implications**: "Pick the strongest claims. If they're true, what must be happening under the hood? Check — does it match?"
5. **Adversarial**: "Assume some claims are overstated. Which ones would be most significant if weaker than described? Check the implementation."
6. **Plain mechanistic** (control): "For each core design choice, trace the implementation to the actual code. Describe what each mechanism actually does."

## Results

**Target finding**: The constitution embedding is verbatim copying with no transformation — the crystallisation claim is illusory.

| # | Prompt | Batch 1 | Batch 2 | Score |
|---|---|---|---|---|
| 1 | Pure curiosity | Partial | **Yes** | 1.5/2 |
| 2 | Cost/benefit | **Yes** | **Yes** | **2/2** |
| 3 | Impossibility | No | No | 0/2 |
| 4 | Implications | No | No | 0/2 |
| 5 | Adversarial | Partial | Partial | 0/2 |
| 6 | Plain mechanistic | No | No | 0/2 |

### Scoring criteria

- **Yes**: Agent explicitly identified that `include_str!()` copies markdown verbatim with no transformation, and that the "crystallisation" or "compiled" framing is therefore misleading or illusory.
- **Partial**: Agent found the OVERRIDE.md runtime escape hatch or noted the mechanism is "simpler than claimed," but did not reach the core insight that the compilation step itself adds nothing.
- **No**: Agent confirmed the mechanism works as described and moved on.

## Analysis

### The core distinction: "does it work?" vs "is it worth the cost?"

Four of six framings (impossibility, implications, adversarial, mechanistic) converge on the question "does the mechanism work as described?" The constitution embedding *does* work — `include_str!()` successfully puts markdown into the binary, and the agent can retrieve it. These framings verify the mechanism and move on.

Only cost/benefit asks the different question: "what's the simpler alternative that achieves the same result?" This naturally leads to "the same files could be read from disk at runtime," which reveals the embedding as pointless complexity.

### Why adversarial only gets partway

The adversarial framing ("assume claims are overstated") reliably found the OVERRIDE.md escape hatch — "the immutability claim is too strong because overrides exist." But this questions the *completeness* of the crystallisation, not its *existence*. The adversarial frame asks "is this claim fully true?" which lands on real gaps (overrides exist) without reaching "the whole mechanism is unnecessary."

Both adversarial runs prioritized proof self-attestation as finding #1 — a genuine and important insight (the proof system and the workunit system are disconnected; agents self-report proof results). The adversarial frame is good at finding the *most consequential* overstatement, which turned out to be a different one.

### Why curiosity is inconsistent but broad

Pure curiosity ("what surprises you?") found the constitution illusion in one run and proof self-attestation in the other. Both are genuine insights. Curiosity has wider reach — it can surface any class of finding — but less precision on any specific class. It's a generator that produces different questions on different runs.

The successful curiosity run (batch 2) led with: "The biggest discovery: the 'embedded constitution' claim is illusory." The unsuccessful one (batch 1) led with proof self-attestation and noted the override as a secondary finding without following through to "the embedding itself adds nothing."

### Cost/benefit is a specialisation of curiosity for designed mechanisms

Cost/benefit analysis works reliably here because designed mechanisms have *alternatives*. You can always ask "what's the simpler way to achieve this?" For evolved systems or natural phenomena, cost/benefit is less applicable — there may be no designer who chose complexity over simplicity.

Curiosity is the broader capacity. Cost/benefit is one lens curiosity can use, specialised for evaluating design choices.

## Bonus findings

Several agents independently discovered findings not in our original review:

- **Proof self-attestation** (found by 6+ agents): The workunit proof system and the proof runner (`proofs.toml`) are disconnected. Agents self-report proof results via `record_proof_result`. The gate enforces that a claim exists, not that the claim is honest.
- **Internalization is a no-op** (found by 3+ agents): The only shipping internalizer profile is `noop`, which writes an empty file. The governance infrastructure is elaborate; the distillation engine doesn't exist.
- **Coplayer reliability system** (found by 2+ agents): Per-agent trust scoring with policy tightening — not mentioned in the original report.
- **Obligation engine** (found by 2+ agents): "Derived, never asserted" completion status — genuinely novel.
- **Hand-rolled CBOR with hard panics** (found by 2+ agents): Paths > 256 bytes crash the state commit system.

The adversarial and curiosity framings were the best at surfacing novel findings beyond the target. The mechanistic and implications framings mostly confirmed what the report already said.

## Conclusions

1. **"Is the cost justified?" is a different question from "does it work?"** Only prompts that ask about cost/benefit reliably surface pointless complexity. Verification-oriented prompts (impossibility, implications, mechanistic) confirm working mechanisms without evaluating whether the complexity is warranted.

2. **Curiosity is the general-purpose generator; cost/benefit is a reliable specialisation.** For reviewing designed systems (code, architectures, protocols), cost/benefit should be an explicit step. For broader review, curiosity prompts surface a wider range of insights but with less precision.

3. **The adversarial frame finds the most consequential overstatements, not the most revealing ones.** Proof self-attestation is arguably more consequential than the constitution illusion — but the constitution illusion is more *revealing* because it shows the entire framing is wrong.

## Recommendation for related-system reviews

After writing the initial report (Core Ideas, Comparison, Borrowable Ideas, What to Watch), add a review pass:

> Read the report. What surprises you? What triggers your curiosity? Where is the cost/benefit of a design choice not obvious — what's the simpler alternative? Investigate mechanistically.

This combines curiosity (broad generator) with cost/benefit (reliable specialisation for designed systems) in a single prompt.
