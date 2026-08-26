---
description: "Moving responsibility between model-interpreted rules and formal enforcement crosses natural-language and symbolic forms, so governing the transfer requires coverage of both and their mapping"
type: kb/types/note.md
traits: [title-as-claim]
tags: [foundations, constraining, self-improving-systems]
---

# Moving the interpretation–enforcement boundary requires cross-form coverage

In an agentic system — one whose operation runs through a model interpreting retained artifacts — a change moves the **interpretation–enforcement boundary** when responsibility for a behavior transfers between natural-language content and a symbolic artifact with assigned consequences. A self-representation covering only one form can represent one endpoint but cannot govern the transfer. Modification-grade reflective coverage of both forms and of the mapping between them is therefore necessary for governed boundary movement. This requirement concerns one class of system change; it does not imply that every reliability improvement crosses forms.

## The asymmetry creates pressure to reassign behavior

The engine is an error profile, [since scheduler-LLM separation exploits an error-correction asymmetry](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md): work that can be fully specified — counting, membership, state tracking, scoping — is exact on a symbolic substrate and error-prone inside a model, while judgment that cannot be fully specified has nowhere to live but natural-language content. Under reliability pressure, that difference makes some behaviors candidates for reassignment. A half-understood constraint can first be retained as natural-language instruction; once a check for it can be specified, [codification](./definitions/codification.md) transfers responsibility to a symbolic consumer. The pressure follows the [constraining gradient from convention to enforcement](./methodology-enforcement-is-constraining.md), but a rule can move only as far as its oracle permits, [because the boundary of automation is the boundary of verification](./the-boundary-of-automation-is-the-boundary-of-verification.md).

The asymmetry explains why boundary movements recur. It does not make movement necessary for improvement. A code-only bug fix, retry correction, atomicity repair, or tighter resource bound can materially improve reliability while leaving the allocation between interpretation and enforcement unchanged. Natural-language guidance can likewise improve within its form.

## Boundary movement and cross-form feedback are different changes

**Boundary movement.** A convention that decays into violations can become a validator; a membership claim can become an enforced mark. Responsibility for compliance then moves from an interpreter to a formal consumer. The unenforced natural-language version of a completeness claim is a trap, [since indexes lower recall when they suppress retrieval that would find more](./indexes-lower-recall-when-they-suppress-retrieval-that-would-find-more.md): it tells an exhaustive consumer to stop looking while members are missing. The [Commonplace reference case](./evidence/commonplace-as-a-reflective-system.md) records this natural-language-to-symbolic movement when a completeness rule acquired schema, validation, and rendering consumers. The reverse movement would retire formal enforcement and return responsibility to interpretation; the current evidence base contains no observed instance of that direction.

**Re-grounding enforcement.** When retained natural-language criteria warrant an existing symbolic rule, a change to those criteria may require the rule to be re-grounded. That repair crosses forms even when the allocation does not move: the revised criteria must constrain a revised symbolic rule. It changes the mapping between the forms rather than which form bears responsibility. The current reference case does not demonstrate this mechanism.

**Cross-form feedback.** Symbolic execution can instead produce evidence that causes a natural-language instruction to be corrected while the enforcement rule stays unchanged. The same [reference case](./evidence/commonplace-as-a-reflective-system.md) records this distinct path: validation exposed an incomplete natural-language search recipe, which was then revised. Information crossed forms, but responsibility for searching and validating did not move between them. This episode therefore supports cross-form feedback, not a symbolic-to-natural-language boundary movement or a re-grounded enforcement rule.

## Consequence for reflective coverage

[Since reflective coverage is graded across representational forms](./reflective-coverage-is-graded-across-representational-forms.md), the relevant question is which grades suffice for governing boundary changes, not agentic improvement generally. Natural-language-only coverage can revise an interpreted rule but cannot carry its transfer into formal enforcement. Symbolic-only coverage can revise a check but cannot represent the interpreted rule from which a transfer begins or the rationale against which enforcement is re-grounded. Governing boundary movement or re-grounding therefore requires modification-grade coverage of both involved artifacts and of their mapping. Same-form changes may be governed with narrower coverage.

## Scope

- The claim concerns changes that transfer responsibility between interpretation and formal enforcement. It does not rank those changes above same-form reliability improvements or claim that reliability gains concentrate at crossings.
- It concerns the natural-language/symbolic pair and does not extend to distributed-parametric artifacts. A localized model-binding request remains in the pair even when it names weights, because representational form follows the operative artifact rather than its referent.
- The direct evidence base separates two observations in [Commonplace as a reflective system](./evidence/commonplace-as-a-reflective-system.md): codification moved the boundary in one direction, while symbolic feedback corrected a natural-language procedure without moving it. [Knowledge-Centric Self-Improvement](../sources/knowledge-centric-self-improvement-2607.19592.ingest.md) is a boundary-stable comparison for behavior-changing guidance. Its fresh task-solving agents consume evolving natural-language guidance in a fixed typed bundle structure, while fixed benchmark evaluators score task outcomes. On this note's representational-form analysis, that combination makes the shared store mixed-form. The protocol does not transfer responsibility from interpreted guidance into new or revised symbolic enforcement, so it demonstrates improvement without that boundary movement. The evaluators establish attempt and artifact outcomes, not the validity of every retained claim, so the case does not show where a boundary would move under weaker oracles.

---

Relevant Notes:

- [Reflective coverage is graded across representational forms](./reflective-coverage-is-graded-across-representational-forms.md) — grounds: supplies the form and operation-profile vocabulary this claim selects sufficient grades from
- [Scheduler-LLM separation exploits an error-correction asymmetry](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) — mechanism: the error profile that sorts bookkeeping into code and judgment into natural language
- [A methodology governs its own extension only as far as it settles the meta-decisions it raises](./a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md) — extends: a boundary-moving proposal raises a representational-form decision the methodology must settle to govern adoption
- [Codification](./definitions/codification.md) — defined-in: the natural-language-to-symbolic crossing
- [Commonplace as a reflective system](./evidence/commonplace-as-a-reflective-system.md) — evidenced-by: the observed codification crossing and the distinct symbolic-feedback episode that corrected a natural-language recipe
- [Methodology with incomplete coverage and its live theory fallback form a two-layer execution system](./theory-and-methodology-form-a-two-layer-execution-system.md) — contrasts: an orthogonal axis of improvement movement — theory-to-methodology promotion can remain in natural-language form, and only its codification special case crosses the form boundary
- [Knowledge-Centric Self-Improvement ingest](../sources/knowledge-centric-self-improvement-2607.19592.ingest.md) — evidenced-by: a boundary-stable comparison in which evolving natural-language guidance remains interpreted while fixed symbolic evaluators score outcomes; this note classifies the resulting store as mixed-form
