---
description: Methodology for testing prompt framings — uses controlled variation against a human-verified finding to identify which cognitive moves agents can reliably execute, then deploys the winning framing as instruction
type: note
traits: []
areas: [kb-design]
status: seedling
---

# Prompt ablation converts human insight into deployable agent framing

When a human reviewer catches something an agent missed, the finding is oracle-strength but not reusable. The prompt experiment pattern converts it into a deployable instruction by testing which prompt framings let agents reach a similar conclusion reliably. "Ablation" because only the framing varies — input, tools, and model are held constant.

## The pattern

1. **Start from a miss.** An agent produces output. A human identifies something the agent didn't catch. This finding becomes the scoring target — ground truth for the experiment.

2. **Design prompt framings.** Create 4-6 variants that might surface the target through different cognitive moves. Include a control (the current framing, or a neutral baseline). The framings should elicit genuinely different approaches — rephrasings of the same question won't reveal which cognitive moves work.

3. **Fix everything else.** Same input, same tools, same model. Only the prompt framing varies.

4. **Run each framing multiple times.** At least 2 runs per framing. A single run can't distinguish reliable framings from lucky ones.

5. **Score against the target.** Yes/Partial/No. Partial matters — it reveals framings that identify symptoms without reaching root cause.

6. **Track bonus findings.** Agents may surface findings outside the target. These reveal each framing's *reach* (what else it catches) and *selectivity* (whether it scatters or focuses).

7. **Analyze mechanisms, not just scores.** Understanding *why* each framing works or fails identifies which cognitive moves agents can reliably execute. This is what transfers beyond the specific test case — once you know that cost/benefit analysis reliably surfaces pointless complexity while adversarial framing reliably finds the most consequential overstatement, you can choose framings for new situations without running a new experiment.

8. **Deploy as instruction.** The winning framing (or combination) becomes a step in the relevant template or skill.

## Why it works

The experiment uses the human's finding as a hard oracle — a clear, verifiable target — to evaluate a soft question: which prompt framing elicits the right reasoning? Without the known target, there's no scoring criterion. Without mechanism analysis, there's a score but no transferable understanding. This is the [oracle-strength spectrum](./oracle-strength-spectrum.md) applied to experimental design: a hard oracle making a soft question answerable.

The conversion from human insight to agent framing is inherently lossy. The human's reasoning may be oracle-strength ("what discriminative power could this verifier have?") while the agent's successful path is a weaker approximation ("what's the simpler alternative?"). The [curiosity-prompts experiment](../work/curiosity-prompts/experiment-report.md) showed this: cost/benefit reliably reached the target finding (2/2) but through a less powerful reasoning path than the human used. The deployed framing trades depth for reliability — good enough, not equivalent.

## Design constraints

**The target must be specific and verifiable.** "The report is too generous" is not a target. "The constitution embedding is verbatim copying — the crystallisation claim is illusory" is. Vague targets make Yes/Partial/No scoring impossible.

**The framings must elicit different cognitive moves.** The curiosity experiment tested six genuinely different approaches: broad curiosity, cost/benefit analysis, impossibility checking, implication tracing, adversarial assumption, and mechanistic tracing. Four of six converged on "does it work?" — only cost/benefit asked "is it worth the cost?" If the framings had been variations on "look more carefully," that structural insight would have been invisible.

**The control should be current practice.** This answers "does the new framing add value over what we already do?" If the control scores well, the experiment may be unnecessary. If it scores zero, the gap is confirmed.

## Deployments

The curiosity-prompts experiment produced two deployed artifacts:

- The [Curiosity Pass](./types/related-system.md) in the related-system template — a systematic per-claim review step combining broad curiosity, cost/benefit, and the oracle-strength question
- The [Curiosity Gate](../instructions/ingest/SKILL.md) in the ingestion skill — a lighter two-question version (what surprises you? what's the simpler account?) adapted for source analysis

Both include the oracle-strength question ("what could this achieve even if it works perfectly?") despite inconsistent agent performance, because it's the most powerful framing when it does fire.

## Open questions

- How many runs per framing are sufficient? 2 is minimum for detecting consistency; it may be insufficient for close calls.
- Can synthetic targets (deliberately planted flaws) substitute for human-discovered findings? They risk testing for the wrong thing — a planted flaw is obvious by construction, while valuable targets are things that slipped past a capable agent.
- Does the pattern extend beyond review framings to skill testing? The structure seems applicable wherever you have a known-correct output and want to find the instruction that produces it. The connection to [unit testing LLM instructions](./unit-testing-llm-instructions-requires-mocking-the-tool-boundary.md) is suggestive — both test instructions against known expectations, using different mechanisms.

---

Relevant Notes:

- [oracle-strength-spectrum](./oracle-strength-spectrum.md) — grounds: the experiment pattern uses a hard oracle (known finding) to evaluate a soft question (which framing works?)
- [unit-testing-llm-instructions-requires-mocking-the-tool-boundary](./unit-testing-llm-instructions-requires-mocking-the-tool-boundary.md) — complements: tests skill execution via tool mocking; this note tests prompt framings via ablation against known targets
- [curiosity-prompts experiment](../work/curiosity-prompts/experiment-report.md) — worked example: 6 framings tested against a known Decapod finding

Topics:

- [kb-design](./kb-design.md)
