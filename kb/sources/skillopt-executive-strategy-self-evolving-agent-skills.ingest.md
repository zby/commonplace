---
description: "SkillOpt paper showing validation-gated text-space optimization of compact agent skills as readable deploy-time learning around frozen models"
source: https://arxiv.org/html/2605.23904v2
captured: "2026-05-28"
capture: web-fetch
genre: scientific-paper
snapshot_sha256: bbb6e835d348b695d3c7e2d09c480af82b953b9891ea7e3f28b57839c8ff077b
ingested: "2026-05-28"
type: kb/sources/types/ingest-report.md
domains: [skill-optimization, deploy-time-learning, trace-learning, readable-artifacts]
---

# Ingest Report: SkillOpt: Executive Strategy for Self-Evolving Agent Skills

## Classification

ArXiv preprint with a proposed optimization method, benchmark evaluation, baselines, ablations, and limitations.
Author signal: multi-author research paper with benchmark tables and ablation/transfer studies, but not yet independently reproduced in this KB.

## Summary

SkillOpt treats an agent skill document as trainable external state. A separate optimizer model inspects scored rollouts and proposes bounded add/delete/replace edits to a single skill, while a held-out validation split accepts only strict improvements. The loop keeps rejected edits as negative evidence, uses a textual learning-rate budget plus slow/meta updates to preserve useful strategy, and deploys only a compact `best_skill.md` artifact at inference. Across six benchmarks, seven target models, and direct-chat/Codex/Claude Code harnesses, the paper reports consistent gains over no-skill, human-written, one-shot, Trace2Skill, TextGrad, GEPA, and EvoSkill baselines, with transfer across models, harnesses, and some benchmark pairs. The key boundary is evaluator quality: SkillOpt is strongest where scored trajectories and held-out validation are available.

## Quotes

- **Source extract (verbatim):** A skill is a natural-language policy inserted into the agent context before execution. In direct-chat benchmarks it is prepended to system or developer instructions; in tool-use harnesses it becomes persistent procedural memory. The target model and execution harness are frozen.
  - **Source location:** Section 3.1 "Problem Setup"
- **Source extract (verbatim):** Every candidate skill is evaluated on the selection split with the same frozen target model and harness. A candidate is accepted only if it strictly improves the current selection score; otherwise it is rejected.
  - **Source location:** Section 3.5 "Validation Gate and Rejected-Edit Buffer"
- **Source extract (verbatim):** SkillOpt is described as best or tied-best on every evaluated cell, with positive gains over no-skill baselines throughout.
  - **Source location:** Section 4.1 "Main Results"
- **Source extract (verbatim):** The learned skills are reported as compact. Table 6 lists final skill lengths ranging from 379 tokens for LiveMathematicianBench to 1,995 tokens for SpreadsheetBench, with one to four accepted edits in the GPT-5.5 target/optimizer runs.
  - **Source location:** Section 4.4 "Learned Skills: Compactness, Cost, and Examples"
- **Source extract (verbatim):** The paper concludes that agent skill documents can be optimized as external natural-language state for frozen agents. It presents SkillOpt as a reproducible, validation-gated text-space training loop that improves a compact skill artifact while keeping the target model and harness fixed.
  - **Source location:** Section 5 "Conclusion"

## Connections Found

- [Readable artifact loop is the tractable unit for continual learning](../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) -- **evidence**. SkillOpt is a concrete natural-language-only readable-artifact loop: frozen model, mutable skill, bounded text edits, validation gate, and compact deployed artifact.
- [Retained system-definition artifacts enable persistent deployment-time adaptation](../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md) -- **evidence**. The system learns by updating durable skill text across runs, not by changing weights at inference.
- [Continual learning requires governing behaviour-changing writes, not just storing content](../notes/continual-learning-requires-governing-behaviour-changing-writes.md) -- **evidence**. The retained artifact changes future behavior through instruction authority, so the learned object is behavioral policy rather than passive knowledge.
- [Diagnostic richness constrains outer-loop learning quality](../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) -- **evidence**. Rollout traces, success/failure contrast, rejected edits, and slow/meta updates supply more diagnostic state than a scalar score alone.
- [The verifiability gradient](../notes/verifiability-gradient.md) -- **evidence**. SkillOpt's success depends on resettable, scored tasks and held-out validation; the paper's limitations mark subjective/open-ended domains as weaker targets.
- [Use trace extraction](../notes/agent-memory-requirements/use-trace-extraction-as-meta-learning.md) -- **evidence**. The paper converts trajectories into a retained behavior-shaping text artifact, with held-out selection and edit rejection as signal-quality controls.
- [Trajectory-Informed Memory Generation for Enhanced Agentic Reasoning](trajectory-informed-memory-generation-self-improving-agents.ingest.md) -- **compares-with**. Both learn from execution trajectories; TIMG produces retrievable tips, while SkillOpt edits one portable skill document.
- [Agent Workflow Memory](agent-workflow-memory.ingest.md) -- **compares-with**. Both induce procedural text from traces; SkillOpt adds bounded patches, rejected-edit memory, and explicit held-out selection.
- [Skill Synthesis: Materializing Knowledge as Skills](skill-synthesis-materializing-knowledge-as-skills-2032179291031.ingest.md) -- **compares-with**. Skill Synthesis derives skills from source/domain corpora; SkillOpt optimizes skills from scored rollouts.
- [Meta-Harness: End-to-End Optimization of Model Harnesses](meta-harness-end-to-end-optimization-of-model-harnesses.ingest.md) -- **compares-with**. Both optimize readable artifacts around a fixed model from evaluation feedback; Meta-Harness changes code harnesses, while SkillOpt changes natural-language skills.
- [Improving AI Skills with AutoResearch Evals Skills](improving-ai-skills-with-autoresearch-evals-skills-203525743436.ingest.md) -- **compares-with**. That practitioner account emphasizes manual comprehension and judge calibration; SkillOpt automates more of the loop in hard-oracle domains but still depends on scored trajectories and held-out selection.

## Extractable Value

- **Skill documents can be trained as readable external policy** [quick-win]. SkillOpt is strong evidence for treating skill text as a behavior-shaping artifact that can be improved without weight updates.
- **Validation gates are the practical boundary for automated skill evolution** [quick-win]. The strict held-out gate is what lets text edits become a learning loop instead of uncontrolled prompt rewriting.
- **Textual learning-rate budgets and bounded edits reduce skill drift** [experiment]. The add/delete/replace budget gives an operational pattern for future skill revision tools: constrain the edit surface before evaluating effects.
- **Rejected edits are retained learning artifacts** [experiment]. Keeping a rejected-edit buffer turns failed proposed changes into negative evidence for later optimizer calls.
- **Slow/meta updates split runtime context from optimizer memory** [deep-dive]. The deployed skill stays compact, while the optimizer can use richer history and strategy outside the runtime path.
- **Skill transfer suggests learned procedure can outlive one harness** [just-a-reference]. Cross-model and Codex/Claude Code transfer support the claim that optimized skills can encode portable task procedure rather than only harness quirks.
- **Single-skill optimization does not solve skill-library governance** [just-a-reference]. SkillOpt improves one domain skill; it does not address discovery, routing, retirement, provenance, or conflicts across many skills.

## Limitations (our opinion)

- This is a scientific preprint; independent reproduction and implementation details should be checked before treating the numbers as settled.
- The arXiv HTML snapshot is sufficient for conceptual ingestion but may lose exact formulas and table formatting; use the PDF for precise numeric or mathematical claims.
- The method is strongest in domains with scored trajectories and held-out validation. Open-ended, subjective, or sparse-feedback skill domains still need stronger human or model evaluation.
- The optimized skill can encode benchmark-specific heuristics. Held-out validation and transfer tests reduce this risk but do not eliminate it.
- The paper optimizes a compact skill artifact, not a full skill library lifecycle with provenance, routing, retirement, and conflict management.

## Recommended Next Action

Write a note tentatively titled **Skill documents can be trained as readable external policy**. It should connect SkillOpt to the readable-artifact loop, retained-artifact deployment-time adaptation, diagnostic richness, and verifiability gradient notes. The central claim should be that scored rollouts plus held-out validation can make natural-language skills into trainable external policy artifacts, with the boundary condition that the evaluator must be good enough to make text edits learnable rather than merely plausible.
