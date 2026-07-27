# Natural-language artifact terminology

## Goal

Replace **prose artifact** and the corresponding technical use of **prose** as a representational form with **natural-language artifact** and **natural-language form**. Use the shorter **prompt** where the artifact's relevant consumption path is unambiguously input to a language model.

This is a vocabulary migration, not a change to the underlying three-form model. The intended contrast remains:

> natural-language / symbolic / distributed-parametric

The new label names the actual classification boundary: whether the operative part receives its consequences through natural-language interpretation. The old label suggests continuous expository writing and fits poorly for fragments, facts, reflections, rules, structured records, and prompt components that are natural language without necessarily being prose.

## Replacement rule

Use **natural-language artifact**, **natural-language form**, **natural-language content**, or **natural-language instruction** when the representational category matters.

Use **prompt** only when all of these are true:

- the referent is supplied, or is explicitly assembled to be supplied, as model input;
- the sentence does not need to include human-interpreted natural-language artifacts;
- calling it a prompt does not hide a distinction among canonical source, retrieved record, instruction, and generated prompt view that matters to the claim.

A note that might later be retrieved into a model context is not thereby a prompt. A stored policy is not a prompt when the sentence is about its retained form rather than its model-input use. When either boundary matters, keep the broader natural-language term and name the consumption path separately.

## Evaluation boundary

In scope:

- the active-vocabulary summary in `AGENTS.md`;
- the definition of [representational form](../../notes/definitions/representational-form.md) and the technical vocabulary built on it;
- live notes, reference documentation, instructions, and external-system reviews that use **prose** to name the natural-language representational category;
- compounds and contrasts such as `prose/symbolic`, `prose form`, `prose record`, `prose instruction`, and `prose-to-code` where they invoke that category;
- selective shortening to **prompt** where the consumption path makes it exact.

Out of scope:

- ordinary editorial uses such as “clear prose,” “body prose,” “in prose,” or “improve the prose”;
- named review machinery such as the `prose` review bundle and its gates;
- verbatim quotations, captured sources, frozen snapshots, generated reports, and historical experiment outputs;
- the captured versions of **Where It Lives Is Not What It Is** (`kb/sources/where-it-lives-architectural-vocabulary-retained-adaptation.md` and `kb/sources/where-it-lives-retained-adaptation-2026-06-23.md`), which retain the paper's historical `prose / symbolic / distributed-parametric` terminology until a separate editorial decision revises the article;
- filenames and historical ADR wording unless leaving them unchanged would misstate the current system or break current navigation;
- replacing precise nouns such as note, policy, reflection, record, instruction, or playbook merely because they are natural-language artifacts.

Mixed artifacts remain mixed. For example, a skill can combine natural-language instructions, symbolic frontmatter, and executable scripts. The migration should not flatten those operative parts into “a prompt” merely because an LLM consumes one of them.

## Initial inventory

The seed scan on 2026-07-27 found 13 exact uses of `prose artifact(s)` across 12 live library files. They fall into four working groups:

| group | representative cases | likely treatment |
|---|---|---|
| Core category definition | `representational-form.md`, `axes-of-artifact-analysis.md`, `reach-assessment.md` | Replace with natural-language terminology and propagate the three-form contrast. |
| Model-input artifacts | Tendril system prompt; Dynamic Cheatsheet's updated memory inserted into the next prompt | Prefer **prompt** only where the sentence is specifically about model input; otherwise retain **natural-language artifact**. |
| Stored readable outputs | wiki pages, digests, drafts, policies, rubrics | Replace with **natural-language artifact** or the more precise existing noun. |
| Operational state contrast | review acknowledgement no longer rewriting review documents | Prefer the precise artifact noun when available; do not preserve the category label when it adds no information. |

The exact phrase is only the seed. The migration must also inspect category-bearing uses of **prose** without `artifact`, especially the canonical definition, `prose/symbolic/distributed-parametric` contrasts, and descriptions of instructions or records. It must not turn a broad `prose` search into an indiscriminate replacement pass.

Useful audit commands:

```bash
rg -n -i '\bprose artifacts?\b' AGENTS.md kb/notes kb/reference kb/instructions kb/types kb/agent-memory-systems kb/agentic-systems --glob '*.md'
rg -n -i '\bprose (form|content|records?|instructions?|memory|knowledge|commitments?)\b|\bprose/symbolic\b|\bprose-to-(code|prose)\b' AGENTS.md kb/notes kb/reference kb/instructions kb/types kb/agent-memory-systems kb/agentic-systems --glob '*.md'
rg -n -i '\bnatural-language (artifacts?|form|content|records?|instructions?)\b' AGENTS.md kb/notes kb/reference kb/instructions kb/types kb/agent-memory-systems kb/agentic-systems --glob '*.md'
```

## Plan

See the [migration plan](./plan.md).

The first independent verification found semantic and executable-surface leftovers. See the [verification-remediation plan](./remediation-plan.md) for the correction pass required before verification can be attempted again.

## Work products

- A migration ledger, split into manifest-backed batch tables if needed, that classifies each category-bearing use as **natural-language term**, **prompt shorthand**, **more precise noun**, or **preserve prose**.
- A lightweight [lessons-learned record](./lessons-learned.md) that can support reusable methodology if the migration earns it.
- A durable vocabulary decision, likely an ADR or an explicit revision rationale in the representational-form definition, that explains why the category name changed and records **prompt** as a narrower shorthand rather than a synonym.
- One coherent corpus edit covering the active vocabulary, definitions, theory notes, current reference documentation, instructions, and maintained external-system reviews.
- Validation and residual-search evidence showing that preserved uses of **prose** are deliberate.
- Promoted methodology for future terminology migrations where this workshop produces a supported transferable claim or an exercised reusable procedure.

## What closes the workshop

Close this workshop when:

1. **Natural-language** is the canonical name of the relevant representational form everywhere current Commonplace vocabulary is defined.
2. Live library uses of the old technical category have been migrated or recorded as deliberate exceptions.
3. Every new **prompt** substitution denotes an actual model-input artifact or view, not merely material that could someday enter context.
4. Ordinary editorial **prose** terminology and the named prose-review machinery remain intact.
5. The affected artifacts pass deterministic validation, and the final residual searches are recorded.
6. Lessons from the migration have been reviewed and any methodology they genuinely support has been extracted.
7. The durable rationale has been extracted, this directory has been deleted, and the active-workshop entry has been removed.

## Grounding

- [Representational form](../../notes/definitions/representational-form.md) — primary definition whose current `prose` category is being renamed.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) — main use of the three-form comparison and its mixed-artifact boundary.
- [Codification](../../notes/definitions/codification.md) — already defines the phase transition primarily as natural language crossing into symbolic form.
- [Vocabulary governance](../vocabulary-governance/README.md) — adjacent workshop for vocabulary scope and write-path governance; this workshop owns the concrete term migration.
- [Active vocabulary and write-path first mentions](../../reference/adr/022-active-vocabulary-and-write-path-first-mentions.md) — requires an accepted global term to propagate through `AGENTS.md` and authoring behavior.
