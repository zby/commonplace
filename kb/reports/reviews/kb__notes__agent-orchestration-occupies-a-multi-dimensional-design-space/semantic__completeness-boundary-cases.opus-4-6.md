The note presents a five-dimension design space: scheduler placement, persistence horizon, coordination form, coordination guarantee, and boundary-return artifact. Each dimension is tested below.

---

**Framework: Five-dimension design space**

Grounding definition: "The better picture is a design space with separable dimensions, so new systems can occupy new combinations without rewriting the taxonomy."

- Simplest instance: a raw chat loop with no explicit orchestration. Scheduler: in the LLM. Persistence: per-step. Coordination form: direct prompt. Guarantee: none. Return artifact: raw NL. All five dimensions have a value. ✓
- Most extreme: a large versioned multi-agent platform. Scheduler: symbolic/external. Persistence: cross-session. Coordination: shared-state. Guarantee: isolation + consistency + adjudication. Return: structured code. All five dimensions map. ✓
- Between: RLM (model-authored ephemeral external scheduler). The note explicitly handles this as a boundary case for scheduler placement. ✓
- Between: Slate. The note explicitly handles this as occupying a new combination on persistence and boundary-return artifact. ✓

**Boundary test: dimension independence**

The note claims separability: "new systems can occupy new combinations." But some dimensions likely interact:
- Coordination guarantee depends on coordination form — you can only provide isolation if there's something to isolate; you can only provide consistency if there's shared state. A system with no shared state doesn't need a consistency guarantee.
- Persistence horizon constrains boundary-return artifact — an ephemeral system can't produce cross-session reusable artifacts.

INFO — the note's "Why this matters" section poses "Which dimensions interact, and which vary independently?" as an open question, which appropriately acknowledges that full independence is not claimed. The framing as "separable" rather than "independent" is precise.

**Adjacent concept: evaluation/feedback**

How the system evaluates outputs and adjusts. The note's scope limits section explicitly acknowledges this: "Evaluation infrastructure, policy layers, and social workflows may deserve their own treatment." ✓

**Adjacent concept: authority/trust model**

Who can invoke what, and what verification occurs at boundaries. This partially overlaps with coordination guarantee but also touches governance. Not named as a dimension. INFO — this is a minor gap; it may be subsumed under coordination guarantee or may warrant its own dimension, but the note's explicit "open map, not closed classification" framing handles this appropriately.

No WARN. Two INFOs: dimension interactions acknowledged as open question, and authority/trust model as potential unnamed dimension.
