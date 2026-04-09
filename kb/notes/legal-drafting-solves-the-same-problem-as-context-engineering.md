---
description: Legal drafting parallels context engineering because both write ambiguous natural-language specifications for judgment-based interpreters, but law develops constraining more than codification
type: note
traits: [has-external-sources]
tags: [learning-theory]
status: seedling
---

# Legal drafting solves the same problem as context engineering

Context engineering for LLMs is writing natural language instructions interpreted by a processor exercising judgment. Law has been doing this for centuries. The parallel is structural rather than merely metaphorical — both domains face [semantic underspecification](./agentic-systems-interpret-underspecified-instructions.md) as a property of natural language, and both have developed techniques to manage it.

The parallel has limits. Judges have decades of domain training, access to external context (legislative history, prior rulings), and operate under institutional constraints (stare decisis, appellate review). LLMs have none of these. At the abstract level, the shared structure is: a spec in a language with irreducible ambiguity, interpreted by a processor that must choose among multiple reasonable readings. The interpreters differ enough that techniques do not transfer intact at the operational level, but the abstract spec-writing problem is the same.

## The structural parallel

A statute is a natural language specification that a judge must interpret, resolving its ambiguity through judgment rather than compilation. This matches the abstract structure the [underspecified instructions framing](./agentic-systems-interpret-underspecified-instructions.md) describes: a spec that admits multiple valid interpretations, resolved by a processor exercising judgment. What makes the parallel structural is the shared formal situation, not shared subject matter: natural-language specifications remain partly ambiguous, admit multiple reasonable readings, and require an interpreter to choose one in application.

No natural language specification eliminates all ambiguity. Legal drafters have known this for centuries; context engineers are learning it now.

**Judicial application resolves the spec into a case outcome.** A judge reading a statute and applying it to a specific case is turning an underspecified spec into one concrete result. What lawyers call "the range of reasonable readings" corresponds to what the underspecified instructions framing calls valid interpretations. Two judges can reach different conclusions from the same statute and the same facts — just as two LLM runs can produce different outputs from the same prompt.

In common law systems, judicial application is also constraining: each ruling generates precedent that narrows future interpretation, fusing what the KB vocabulary separates (resolution and constraining). Civil law systems work differently — judges apply comprehensive codes without their rulings binding future courts. The case-resolution step is the same, but the constraining feedback loop is absent. This split is itself informative: it shows that resolution and constraining are genuinely separable, not inevitably fused. Common law fuses them; civil law keeps them apart.

## Techniques that transfer

Legal drafting has developed specific techniques to narrow the interpretation space. Most have analogues in prompt and knowledge system design, though the mappings vary in tightness. Here, "tightness" means how much of the mechanism carries over without depending on interpreter-specific institutions: tight mappings preserve most of the mechanism, moderate ones preserve the pattern but rely on different scaffolding, and loose ones are functional analogies with materially different enforcement or accumulation.

| Legal technique | What it does | Context engineering analogue | Mapping tightness |
|---|---|---|---|
| **Defined terms** | Pin a word to one meaning within the document | Glossaries, type definitions, naming conventions | Tight — same mechanism |
| **Structural conventions** | Required sections in a predictable order | Document type templates (spec, ADR, structured-claim) | Tight — same mechanism |
| **Enumeration** | Exhaustive lists instead of open-ended prose | Structured output schemas, enum fields in frontmatter | Tight — same mechanism |
| **Canons of interpretation** | Rules for resolving ambiguity ("specific governs general") | Skill precedence rules, CLAUDE.md routing tables | Moderate — both are meta-rules, but legal canons are institutionally enforced |
| **Precedent** | Past rulings narrow future interpretation | Conventions, few-shot examples | Loose — precedent is binding and accumulative; conventions are advisory |
| **Statute codification** | Settled case law encoded in authoritative text | Promoting a convention to a template or routing rule | Moderate — both commit an interpretation, but statutes carry legal authority |

Two major legal techniques are absent from this table: **boilerplate** (pre-drafted reusable language that eliminates negotiation variance — analogous to skill libraries or reusable prompt components) and **provisos/exceptions** (explicit carve-outs from general rules — analogous to conditional overrides in routing tables). Both deserve exploration.

## Law is rich in constraining but largely lacks codification

**Constraining is precedent (in common law).** Each court ruling that interprets a statute narrows the space of valid interpretations for future cases. A line of consistent rulings is constraining: the same underspecified text, repeatedly interpreted, converging on one reading. Civil law systems constrain differently — through comprehensive codes drafted to minimize interpretation rather than through accumulated rulings.

**Statute codification is stronger constraining, not KB-codification.** When case law constrains enough, legislatures encode the settled interpretation in statute. But statute is still natural language, still interpreted by judges — the medium hasn't changed. In the KB's vocabulary, [codification](./definitions/codification.md) requires crossing a medium boundary (natural language to executable code, changing the consumer from a judgment-exercising interpreter to a deterministic runtime). Statute-writing doesn't cross that boundary. It narrows the interpretation space further (statute is more authoritative than case law) but doesn't eliminate it.

**The constrain/relax cycle is overturning precedent.** New facts, social changes, or edge cases reveal that the settled interpretation is wrong. Courts overturn precedent (relax), then a new line of cases constrains a different reading. The same cycle operates in prompt engineering — a constrained convention encounters new requirements and gets relaxed back to open-ended guidance.

**Distillation has a legal analogue, but only loosely in commentary.** Treatises and restatements extract operational principles from masses of case law — staying in the same medium but changing rhetorical mode from judicial reasoning to systematic exposition. That parallels one aspect of [distillation](./definitions/distillation.md), but legal commentary is usually a general reference work rather than a task-targeted compression for a specific consumer under a strict context budget. A legal brief is the tighter analogue: it compresses authorities for a specific decision-maker and case under explicit page and attention limits.

**True codification is rare in law.** Algorithmic sentencing, automated compliance checks, smart contracts — these cross the medium boundary. They are marginal in legal practice. The rarity is itself informative: law shows that a domain can develop sophisticated constraining methodology while doing almost no codification, suggesting that constraining techniques deserve more attention in prompt engineering than they currently receive.

## Why this matters for knowledge system design

[Programming practices apply to prompting](./underspecification-and-indeterminism-complicate-programming-for-prompts-in-distinct-ways.md) because LLM-based systems are a kind of software system. Legal drafting is a second source discipline that addresses the dimension programming abstracts away: how to write specifications that work despite irreducible ambiguity. Programming analogies require translating from a precise medium to an underspecified one; legal analogies require translating from one kind of interpreter (institutionally constrained judges with external memory) to another (stateless LLMs with bounded context). Neither transfer is free, but they address different gaps.

This doesn't replace the programming lens — typing, testing, and compilation remain powerful. But it adds a complementary perspective native to the underspecified medium.

## ABC as a case study

Agent Behavioral Contracts ([ABC](../sources/agent-behavioral-contracts-formal-specification-runtime-enforcement.ingest.md)) provides independent support for this note's thesis. The paper extends Design-by-Contract (a programming practice) to autonomous agents, but its entire vocabulary — contracts, enforcement, compliance, violation, recovery — is legal vocabulary. The convergence could reflect shared problem structure (as this note argues) or simply shared metaphorical vocabulary; the paper doesn't cite law as a source discipline, so the connection is circumstantial.

ABC's hard/soft constraint hierarchy answers the open question below about interpretation hierarchies: hard constraints (zero-tolerance invariants, deterministic rejection) take absolute precedence over soft constraints (which permit transient violations if recovered within k steps). This mirrors the legal hierarchy where constitutional provisions override statutes, which override regulations.

## Open questions

- Which specific legal drafting techniques haven't been applied to prompt engineering yet? Contract law's "reasonable person" standard might inform how we think about the LLM-as-interpreter.
- Does the common law / civil law distinction map to prompt engineering styles? Common law (bottom-up constraining through precedent) vs civil law (top-down constraining through comprehensive codes) — the body text now notes the split but the prompt engineering mapping remains open.
- ~~Legal interpretation has explicit hierarchies (constitution > statute > regulation > case law). Is there an analogue for prompt systems — which instructions take precedence when they conflict?~~ Partially answered by ABC's hard/soft constraint hierarchy — see above.

---

Relevant Notes:

- [agentic systems interpret underspecified instructions](./agentic-systems-interpret-underspecified-instructions.md) — foundation: the underspecified instructions framing that legal drafting independently addresses
- [programming practices apply to prompting](./underspecification-and-indeterminism-complicate-programming-for-prompts-in-distinct-ways.md) — parallel: the programming lens on the same problem; this note adds a second source discipline native to natural language
- [design methodology — borrow widely, filter by first principles](./programming-patterns-get-a-fast-pass-but-other-borrowed-ideas-must-earn-first-principles-support.md) — extends: law as another source discipline alongside computer science
- [constraining](./definitions/constraining.md) — mapped: legal precedent is constraining — narrowing interpretation space through repeated consistent rulings
- [codification](./definitions/codification.md) — contrast: statute-writing is NOT KB-codification — still natural language interpreted by judges; true legal codification would be algorithmic sentencing or automated compliance
- [distillation](./definitions/distillation.md) — mapped, loosely: legal commentary extracts principles from case law without changing medium; legal briefs are the tighter analogue for task-targeted compression
- [writing styles are strategies for managing underspecification](./writing-styles-are-strategies-for-managing-underspecification.md) — complementary: legal techniques address what goes inside instructions; writing styles address how instructions are framed

- [ABC: Agent Behavioral Contracts](../sources/agent-behavioral-contracts-formal-specification-runtime-enforcement.ingest.md) — validates: ABC reinvents legal enforcement patterns via programming's Design-by-Contract; its hard/soft constraint hierarchy partially answers the interpretation hierarchy question

Source:
- Prompted by a social media post observing that context engineering is close to law
