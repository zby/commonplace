---
description: Choosing to keep a specific LLM output resolves semantic underspecification to one interpretation and freezes it against execution indeterminism — the same stabilizing move the parent note describes for code, applied to artifacts
type: note
traits: []
areas: [learning-theory]
status: speculative
---

# Storing LLM outputs is stabilization

A natural language prompt admits a space of valid interpretations — "write a summary" doesn't pick out a unique text. On top of that, execution indeterminism means the same interpretation may render differently across runs. When you choose to keep a specific output, you're doing two things at once: **resolving semantic underspecification** (committing to one interpretation from the space the prompt admits) and **freezing against indeterminism** (locking in this particular run's rendering). The semantic commitment is the deeper operation — it's the same stabilizing move described in [agentic systems interpret underspecified instructions](./agentic-systems-interpret-underspecified-instructions.md) for code, but applied to the artifact rather than the implementation.

The parent note already says "version both spec and artifact" because "regeneration is a new projection from the same spec — potentially a different resolution of the same ambiguity, not a deterministic rebuild." The insight here is *why* that matters: storing an artifact is itself a stabilization decision. You're not just saving a file — you're committing to one interpretation from a space of valid possibilities, and freezing it against the variation that further runs would introduce.

This applies broadly:
- **Generated code** — the prompt could produce many valid implementations; you lock down the one that works
- **Generated documents** — a note-writing prompt produces varying quality; you keep the good one
- **Configuration** — an LLM suggests settings; you freeze the ones that behave well
- **Accumulated logs** — append-only formats (JSONL) enforce stabilization structurally: the agent can add but cannot overwrite. [Koylanai lost 3 months of engagement data](../sources/koylanai-personal-brain-os.ingest.md) when an agent rewrote a JSON file instead of appending — concrete evidence that without append-only constraints, agents will accidentally destroy stabilized artifacts

In each case, the stored artifact is more stable than the process that created it. The prompt retains both its semantic underspecification (it still admits multiple valid interpretations) and its execution indeterminism (it still produces different outputs across runs); the artifact has neither. This is how [stabilisation is learning](./agentic-systems-learn-through-three-distinct-mechanisms.md) — each stored artifact is a step in the system's adaptation, narrowing behavior through versioned artifacts rather than weight updates.

## Testing implications

This creates two distinct testing targets:

1. **Testing the interpretation space** (prompt testing) — does this prompt reliably produce good outputs? Run N times, check statistical properties. You're testing both whether the space of valid interpretations is acceptable (semantic underspecification) and whether the variation across runs is tolerable (indeterminism). You're testing the generator.
2. **Testing the sample** (artifact testing) — is this specific output good? Check structural properties, quality criteria, corpus consistency. You're testing the product.

You need both because even a well-tuned prompt admits multiple valid interpretations and produces variable output across runs — you can't skip artifact testing. And artifact testing alone doesn't tell you whether the prompt will work next time.

The parent note covers distribution testing ("statistical hypothesis testing, not assertion equality") but doesn't address sample testing. Artifact testing is closer to static analysis or linting — checking properties of a thing that already exists, not verifying behavior of a process.

## Generator/verifier: an alternative to constraining prompts

There are two strategies for getting reliable output from a generator whose outputs vary — both because the prompt admits multiple interpretations and because each run renders differently:

1. **Constrain the generator** — tighter prompts, more examples, lower temperature. Narrowing the interpretation space (more precise spec) and reducing execution variation (lower temperature) both reduce output diversity, but cap the upside. You get consistently mediocre results. Evans' framing of [separating modeling from classification](./related_works/evans-ai-components-deterministic-system.md) is a specific instance: freeze the taxonomy (constrain the interpretation space), then classify within it.
2. **Filter the samples** — wide interpretation space + quality gate. Keeps the upside, rejects the failures. A prompt that sometimes produces great output and sometimes garbage can outperform a "safe" prompt that always produces mediocre output — if you have a good filter.

This is the generator/verifier pattern: verification is often cheaper than generation. For code, you can run tests. For text, you need the automated checks described in the testing pyramid (deterministic → LLM rubric → corpus).

Strategy 2 is only viable when verification is cheap relative to generation — which is to say, when [oracle strength](./oracle-strength-spectrum.md) is sufficient. The viability of generator/verifier varies along the oracle spectrum: it works well in the hard-to-soft oracle range but breaks down in the delayed-oracle and no-oracle zones where the quality gate can't discriminate. This also reframes the relationship between prompt testing and artifact testing: they're not just separate concerns, they're *complementary strategies*. Prompt testing tells you the distribution is worth sampling from. Artifact testing is the filter that makes a high-variance distribution usable.

The implication for stabilization: a good filter lets you *not* stabilize the prompt. You keep the underspecified, indeterministic generator because the verifier handles quality. Constraining the prompt is pushing reliability into the generator instead — a different tradeoff, not a strictly better one.

## Verbatim risk: the hardest verification failure

The generator/verifier pattern has a specific failure mode where the verifier *can't* discriminate: the agent produces output that looks like synthesis — headings, bullet points, "key points" — but contains no insight beyond what the source already stated. The output is reformatted repetition, not processing. This is the worst case because the quality gate passes confidently: the output is well-structured, grammatical, and topically relevant. It just doesn't add anything.

The test: does the output contain claims, connections, or implications not already in the source? If not, the "processing" is illusory. This applies directly to extraction and ingestion workflows — an agent asked to extract insights from a source may produce a note that paraphrases the source with better formatting, which then gets stabilized (stored, linked, indexed) as if it were new knowledge. The KB grows in volume without growing in knowledge.

This is hard to catch because it requires comparing the output against the source, which is a judgment call with low [oracle strength](./oracle-strength-spectrum.md). Structural checks can't detect it — the output has all the right properties (frontmatter, links, claim title). Only semantic comparison reveals the gap.

---

Relevant Notes:
- [deploy-time-learning](./deploy-time-learning-the-missing-middle.md) — extends the stabilization gradient with a new application: output artifacts, not just code
- [stabilisation-is-learning](./agentic-systems-learn-through-three-distinct-mechanisms.md) — foundation: each stored artifact is a step in the continuous learning loop this note describes
- [evans-ai-components-deterministic-system](./related_works/evans-ai-components-deterministic-system.md) — exemplifies the constraint strategy: Evans' "freeze taxonomy then classify" resolves semantic underspecification for the modeling/classification boundary by committing to one interpretation space
- [adaptation-agentic-ai-analysis](./research/adaptation-agentic-ai-analysis.md) — provides data-driven triggers (error patterns, repeated tool failures) for when to make the stabilization decision this note describes
- [oracle-strength-spectrum](./oracle-strength-spectrum.md) — determines where generator/verifier is viable: the pattern requires sufficient oracle strength for the quality gate to discriminate

Topics:
- [learning-theory](./learning-theory.md)
