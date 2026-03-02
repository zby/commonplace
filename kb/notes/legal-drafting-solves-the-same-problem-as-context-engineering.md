---
description: Law has centuries of methodology for writing natural language specifications interpreted by a judgment-exercising processor — the same problem as context engineering for LLMs. Legal techniques (defined terms, structural conventions, precedent) are stabilisation techniques native to the underspecified medium; law mostly lacks crystallisation because statutes remain natural language.
type: note
traits: [has-external-sources]
areas: [learning-theory]
status: seedling
---

# Legal drafting solves the same problem as context engineering

Context engineering for LLMs is writing natural language instructions that will be interpreted by a processor exercising judgment. Law is the same problem with centuries of accumulated methodology. The parallel is not metaphorical — both domains face [semantic underspecification](./agentic-systems-interpret-underspecified-instructions.md) as a structural property of natural language, and both have developed techniques to manage it.

## The structural parallel

A statute is a natural language specification. A judge is a processor that interprets it. The specification admits multiple valid readings. The processor resolves the ambiguity through judgment, not compilation. This is the exact structure of the [underspecified instructions framing](./agentic-systems-interpret-underspecified-instructions.md): a spec in a language with underspecified semantics, projected onto a concrete outcome by a processor that selects one interpretation from the space the spec admits.

Both domains face the same impossibility: you cannot write a natural language specification that eliminates all ambiguity. Legal drafters have known this for centuries. Context engineers are learning it now.

**Spec-to-program projection is judicial application.** A judge reading a statute and applying it to a specific case IS projecting an underspecified spec onto a concrete outcome. The "space of valid interpretations" is what lawyers call "the range of reasonable readings." Two judges can reach different conclusions from the same statute and the same facts — just as two LLM runs can produce different outputs from the same prompt.

## Techniques that transfer

Legal drafting has developed specific techniques to narrow the interpretation space — all of which have direct analogues in prompt and knowledge system design:

| Legal technique | What it does | Context engineering analogue |
|---|---|---|
| **Defined terms** | Pin a word to one meaning within the document | Glossaries, type definitions, naming conventions |
| **Structural conventions** | Required sections in a predictable order | Document type templates (spec, ADR, structured-claim) |
| **Enumeration** | Exhaustive lists instead of open-ended prose | Structured output schemas, enum fields in frontmatter |
| **Canons of interpretation** | Rules for resolving ambiguity ("specific governs general") | Skill precedence rules, CLAUDE.md routing tables |
| **Precedent** | Past rulings narrow future interpretation | Stabilised conventions, few-shot examples |
| **Codification** | Settled case law encoded in statute | Stabilisation — committing an interpretation to a more authoritative text (still natural language, still interpreted) |

## Law is rich in stabilisation but largely lacks crystallisation

**Stabilisation is precedent.** Each court ruling that interprets a statute narrows the space of valid interpretations for future cases. A line of consistent rulings is stabilisation: the same underspecified text, repeatedly interpreted, converging on one reading. The interpretation hasn't changed medium — it's still natural language (judicial opinions) — but the space has narrowed.

**Codification is stronger stabilisation, not crystallisation.** When case law stabilises enough, legislatures encode the settled interpretation in statute. But statute is still natural language, still interpreted by judges — the medium hasn't changed. Codification narrows the interpretation space further (statute is more authoritative than case law, harder to overturn) but doesn't eliminate it. This is the prompt engineering equivalent of promoting a convention to a structured template: more committed, more constrained, but still underspecified.

**The stabilise/soften cycle is overturning precedent.** New facts, social changes, or edge cases reveal that the settled interpretation is wrong. Courts overturn precedent (soften), then a new line of cases stabilises a different reading. The same cycle operates in prompt engineering — a stabilised convention encounters new requirements and gets relaxed back to open-ended guidance.

**Distillation is legal commentary.** Treatises and restatements extract operational principles from masses of case law — staying in the same medium (natural language) but changing rhetorical mode from judicial reasoning to systematic exposition. This parallels how [distillation](./distillation.md) extracts procedures from discursive reasoning without changing medium.

**Crystallisation is rare in law.** True crystallisation — where interpretation moves from judicial judgment to deterministic code — would be algorithmic sentencing, automated compliance checks, or smart contracts. These are marginal in legal practice. The rarity is itself informative: law shows that a domain can develop sophisticated stabilisation methodology while doing almost no crystallisation. This suggests that stabilisation techniques deserve more attention in prompt engineering than they currently receive — the field may be over-focused on the crystallisation end of the spectrum.

## Why this matters for knowledge system design

[Programming practices apply to prompting](./programming-practices-apply-to-prompting.md) because claws are a kind of software system. But legal drafting may be an equally strong source discipline, because law operates in natural language — the actual medium of prompts and knowledge bases. Programming analogies require a translation step (code is precise, prompts are underspecified). Legal analogies don't — law has always worked in the underspecified medium and has developed techniques native to it.

This doesn't replace the programming lens — typing, testing, and compilation remain powerful. But it adds a second source discipline that addresses the dimension programming abstracts away: how to write specifications that work despite irreducible ambiguity.

## Open questions

- Which specific legal drafting techniques haven't been applied to prompt engineering yet? Contract law's "reasonable person" standard might inform how we think about the LLM-as-interpreter.
- Does the common law / civil law distinction map to anything? Common law (precedent-heavy, bottom-up stabilisation) vs civil law (code-heavy, top-down specification) might correspond to different prompt engineering styles.
- Legal interpretation has explicit hierarchies (constitution > statute > regulation > case law). Is there an analogue for prompt systems — which instructions take precedence when they conflict?

---

Relevant Notes:
- [agentic systems interpret underspecified instructions](./agentic-systems-interpret-underspecified-instructions.md) — foundation: the underspecified instructions framing that legal drafting independently addresses; both face the same structural impossibility
- [programming practices apply to prompting](./programming-practices-apply-to-prompting.md) — parallel: the programming lens on the same problem; this note adds a second source discipline native to natural language rather than precise formal languages
- [design methodology — borrow widely, filter by first principles](./design-methodology-borrow-widely-filter-by-first-principles.md) — extends: law as another source discipline alongside computer science, with potentially equal transfer strength because it operates in the same medium
- [stabilisation](./stabilisation.md) — mapped: legal precedent is stabilisation — narrowing interpretation space through repeated consistent rulings
- [crystallisation](./crystallisation.md) — contrast: codification is NOT crystallisation — statute is still natural language interpreted by judges; true legal crystallisation would be algorithmic sentencing or automated compliance
- [distillation](./distillation.md) — mapped: legal commentary and restatements are distillation — extracting principles from case law without changing medium
- [three distinct mechanisms](./agentic-systems-learn-through-three-distinct-mechanisms.md) — validated: all three mechanisms map to legal analogues, but unevenly — law is rich in stabilisation, has distillation in commentary, and largely lacks crystallisation

Source:
- Prompted by a social media post observing that context engineering is close to law

Topics:
- [learning-theory](./learning-theory.md)
