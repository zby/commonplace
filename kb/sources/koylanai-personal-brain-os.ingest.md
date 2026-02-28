---
source: https://x.com/koylanai/status/2025286163641118915
snapshot: koylanai-personal-brain-os.md
ingested: 2026-02-22
type: practitioner-report
domains: [context-engineering, agent-architecture, knowledge-management, file-based-systems]
---

# Ingest: The File System Is the New Database: How I Built a Personal OS for AI Agents

Source: [koylanai-personal-brain-os.md](./koylanai-personal-brain-os.md)
Captured: 2026-02-22
From: https://x.com/koylanai/status/2025286163641118915

## Classification

Type: **practitioner-report** -- The author built a specific system (Personal Brain OS), used it daily, and describes what worked, what failed, and what he'd do differently. Includes concrete file counts, schema decisions, and measured outcomes (e.g., 40% token reduction from module splitting).

Domains: context-engineering, agent-architecture, knowledge-management, file-based-systems

Author: Muratcan Koylan (@koylanai), Context Engineer at Sully.ai (healthcare AI). His open-source Agent Skills work has 8,000+ GitHub stars and is cited in academic research alongside Anthropic. Previously built multi-agent systems handling 10,000+ weekly interactions at 99Ravens AI. Credible practitioner with production experience in the exact domain he's writing about.

## Summary

Koylanai describes "Personal Brain OS," a Git-repository-based personal operating system comprising 80+ files in Markdown, YAML, and JSONL that provide persistent context to AI coding assistants (Cursor, Claude Code). The core architectural insight is "progressive disclosure" -- a three-level loading system (routing file, module instructions, data files) that gives the model exactly what it needs per task and nothing more, avoiding attention budget waste. The system includes 11 isolated modules, an episodic memory system (experiences, decisions, failures as append-only JSONL), a skill system built on the Anthropic Agent Skills standard (auto-loading reference skills vs. manually invoked task skills), and automation chains for weekly reviews and content pipelines. The most important lessons: append-only formats are a safety mechanism (not just a convention), module boundaries are loading decisions that directly affect token efficiency, and voice/style is best encoded as structured data (numeric scales, banned word lists) rather than prose descriptions.

## Connections Found

Six connections to existing KB notes:

1. **[deploy-time-learning](../notes/deploy-time-learning-the-missing-middle.md)** (exemplifies): Koylanai's progressive disclosure maps onto the verifiability gradient. His three levels (routing -> module -> data) are graduated artifact loading. His format-function mapping (JSONL for append-only logs, YAML for config, Markdown for narrative) is choosing the right hardness grade per content type -- the same principle the crystallisation gradient describes for prompts vs. schemas vs. deterministic code.

2. **[stabilisation-is-learning](../notes/agentic-systems-learn-through-three-distinct-mechanisms.md)** (exemplifies): Personal Brain OS is a concrete instance of the core claim. The system learns through accumulating versioned artifacts (decision logs, failure patterns, voice profiles), not weight updates. The feedback loop (goals -> content -> metrics -> reviews -> goals) is exactly the continuous learning loop described theoretically.

3. **[voooooogel-multi-agent-future](../notes/research/voooooogel-multi-agent-future.md)** (implements): The filesystem-as-collaboration-medium prediction is realized here. Files in markdown/YAML/JSONL that both humans and LLMs read natively, with "prompt as data" via instruction files on disk.

4. **[inspectable-substrate-not-supervision-defeats-the-blackbox-problem](../notes/inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md)** (exemplifies): "No database, just Git-versioned files" is the inspectable substrate argument applied to personal knowledge management. Every change is diffable, every decision traceable.

5. **[storing-llm-outputs-is-stabilization](../notes/storing-llm-outputs-is-stabilization.md)** (exemplifies): Episodic memory logs (experiences, decisions, failures) are stabilization -- each logged judgment collapses a distribution of possible advice to a specific, versioned point. Critically, Koylanai lost 3 months of engagement data when an agent overwrote a JSON file instead of appending -- concrete evidence for why the append-only/stabilization pattern matters.

6. **[agent-skills-unification](../notes/agent-skills-unification.md)** (shares standard): The skill system uses the same Agent Skills specification (YAML frontmatter + Markdown instructions, auto-load vs. manual invocation) that llm-do's .agent format is aligning with.

## Extractable Value

1. **"Module boundaries are loading decisions" -- the 40% token reduction data point.** Koylanai split identity+brand into two modules and measured 40% token savings for voice-only tasks. Concrete evidence for the cost of wrong module boundaries. [just-a-reference]

2. **Append-only as agent safety mechanism (not just data pattern).** He lost 3 months of data because an agent overwrote a JSON file instead of appending. JSONL's append-only nature is framed as a safety constraint that prevents agents from destroying accumulated knowledge. The KB notes discuss stabilization theoretically; this provides the "what goes wrong when you don't" evidence. [quick-win]

3. **Voice encoding as structured data (numeric scales + banned word lists).** Rating attributes on 1-10 scales and maintaining tiered banned word lists is more actionable for an AI than prose descriptions. [just-a-reference]

4. **Progressive disclosure as three-level architecture with max-two-hop guarantee.** Level 1 routing file (always loaded), Level 2 module instructions (40-100 lines each), Level 3 data files (loaded on demand). Concrete, replicable architecture for graduated artifact loading. [experiment]

5. **Schema over-engineering failure mode: sparse data confuses agents.** Initial schemas with 15+ fields per JSONL entry caused agents to fixate on empty fields. Cutting to 8-10 essential fields improved behavior. [just-a-reference]

6. **Lost-in-middle as an architecture constraint.** 1,200-line voice guide caused drift by paragraph four. Restructuring to front-load distinctive patterns in first 100 lines fixed it. [quick-win]

7. **[claw-learning-is-broader-than-retrieval](../claw-design/claw-learning-is-broader-than-retrieval.md)** (exemplifies): Personal Brain OS stores the four knowledge types that the action-oriented KB argument identifies as missing from retrieval-oriented systems: preferences (values/goals YAML), procedures (AGENT.md decision tables), judgment precedents (decisions/failures JSONL), and voice/style (brand files, voice guides). This convergence from practice supports the theoretical claim.

## Recommended Next Action

Filed as reference. Strong practitioner report that exemplifies several theoretical positions already well-articulated in the KB. No new theory, contradictions, or tensions. The two quick-win items (append-only as safety mechanism, lost-in-middle as architecture constraint) could enrich existing notes as cited examples.
