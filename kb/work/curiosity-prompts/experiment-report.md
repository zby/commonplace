# Curiosity Prompts Experiment

## Question

After writing a related-system review of Decapod, a human reviewer questioned the "embedded constitution" — described as "compiled into the binary" and "crystallised." The reviewer's reasoning was not about implementation details but about *what the mechanism could achieve even if it works perfectly*: if the constitution is crystallised into code, what can it actually do? Only symbolic checks. But the constitution is freeform prose interpreted by an LLM — symbolic checks can't meaningfully verify freeform text. So the crystallisation, even if real, can't deliver the value the framing implies. Investigation then confirmed the mechanism was even weaker than that — just verbatim `include_str!()` copying with no transformation at all.

The reviewer's move was an oracle-strength question: what's the discriminative power of this verifier? The answer — "not much, because freeform prose resists symbolic verification" — followed from reasoning about the claim, not from reading the code.

This was a valuable finding. Can we prompt agents to ask similar questions? What framing reliably surfaces insights about mechanisms whose *claimed value exceeds their actual power*?

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

### The core distinction: "does it work?" vs "what can it achieve?"

The human reviewer's question was not "does the compilation work?" but "what could a compiled constitution actually *do*?" This is an oracle-strength question: even if the mechanism functions perfectly, what's the discriminative power of the resulting verifier? For freeform prose interpreted by an LLM, compiling it into the binary can't add verification capability — the prose is still interpreted at runtime, not checked at compile time. The crystallisation claim implies a stabilisation property the mechanism cannot deliver, regardless of implementation quality.

Four of six agent framings (impossibility, implications, adversarial, mechanistic) converge on the question "does the mechanism work as described?" The constitution embedding *does* work — `include_str!()` successfully puts markdown into the binary, and the agent can retrieve it. These framings verify the mechanism and move on.

Only cost/benefit asks a question that reaches a similar conclusion from a different direction: "what's the simpler alternative that achieves the same result?" This naturally leads to "the same files could be read from disk at runtime," which reveals the embedding as pointless complexity. The human's reasoning was stronger — it showed the mechanism can't deliver value *even if there's no simpler alternative* — but cost/benefit was the only agent-accessible framing that got there reliably.

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

1. **"Does it work?" is a different question from "what can it achieve?"** The human reviewer's insight came from asking what discriminative power the mechanism could have even if it works perfectly. No agent framing replicated this oracle-strength reasoning. The closest was cost/benefit, which arrived at a similar conclusion ("it's pointless") via a different path ("the simpler alternative works identically").

2. **Cost/benefit is the most reliable agent-accessible framing.** For reviewing designed systems (code, architectures, protocols), "what's the simpler alternative?" reliably surfaces pointless complexity. It doesn't reach the deeper "what *could* this achieve?" question, but it gets to a useful answer.

3. **Curiosity is the general-purpose generator; cost/benefit is a reliable specialisation.** Curiosity prompts surface a wider range of insights (proof self-attestation, coplayer system, eval framework) but with less precision on any specific class. Cost/benefit is narrower but reliable.

4. **The adversarial frame finds the most consequential overstatements, not the most revealing ones.** Proof self-attestation is arguably more consequential than the constitution illusion — but the constitution illusion is more *revealing* because it shows the entire framing is wrong.

5. **The oracle-strength question — "what could this verify?" — is the most powerful but hardest to prompt for.** The human reached it through domain knowledge (understanding that freeform prose resists symbolic verification). Whether agents can be prompted to ask this systematically remains an open question.

## Recommendation for related-system reviews

After writing the initial report (Core Ideas, Comparison, Borrowable Ideas, What to Watch), add a review pass:

> Read the report. What surprises you? What triggers your curiosity? Where is the cost/benefit of a design choice not obvious — what's the simpler alternative that achieves the same result? For each strong claim, ask: what could this mechanism actually achieve, even if it works perfectly? Investigate mechanistically.

This combines three layers:
- **Curiosity** (broad generator) — surfaces surprising or unusual choices
- **Cost/benefit** (reliable agent-accessible specialisation) — finds pointless complexity
- **Oracle-strength** ("what could this achieve?") — the hardest question, included because it's the most powerful even if agents reach it inconsistently
