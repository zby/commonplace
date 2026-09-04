---
description: "Arguments for The Automated Software House Conjecture paper"
type: kb/articles/types/article.md
status: draft
byline: Zbigniew Lukasiak
---
# Appendix B: Arguments

These entries preserve only the reasoning required by the paper's linked claims.

### Holding a program theory means sustaining coherent search under delayed feedback

The body uses this claim to explain why choosing among locally valid implementations requires more than passing the checks available at the moment of change. Peter Naur's program theory is the capacity to map software to the activity it supports, justify its organization, and incorporate a new demand by recognizing which existing facilities and commitments matter ([Naur, §§4–5](https://ingenieria-de-software-i.github.io/assets/bibliografia/programming-as-theory-building.pdf)). In the body's multi-tenant example, the evidence that distinguishes locally valid choices consists of consequences exposed by later demands. That evidence is unavailable when the first choice is made, so a useful theory may be partial and fallible. It counts by shaping which candidates are proposed, what must be preserved, how failure is interpreted, when the process backtracks, and what it revises. A single correct change is insufficient evidence. Withholding or replacing the relevant theory must change proposal, evaluation, diagnosis, recovery, or later revision in a predicted way; otherwise the retained theory is inert rather than held by the house.

Adapted from kb/notes/program-theory-sustains-search-under-delayed-feedback.md at `50121b7178058782f7b264127bbd23d94f7eeff5`; the live note may have changed.

### Naur's compiler case tested one historically bounded document-and-reading system

The body uses this claim to keep Naur's transfer failure from ruling out every future way of representing and consuming project knowledge. In the reported case, a motivated successor group received full program text, annotated sources, extensive written design discussion, and personal advice, yet proposed patches that the original group judged to damage the compiler's structure ([Naur, §2](https://ingenieria-de-software-i.github.io/assets/bibliografia/programming-as-theory-building.pdf)). That result shows that this supplied package and its use did not transfer enough program-specific understanding to that group. The materials and consumption process relied on people to organize, find, select, and activate relevant rationale. The case did not compare linked decision rationale, scoped architecture records, machine-maintained indexes, semantic retrieval, dependency-aware context assembly, or automatic activation at the decision point. Those mechanisms create an empirical alternative; they do not establish success by definition. A newer interpreter-plus-artifact system must still show causal, longitudinal effects on coherent modification.

Adapted from kb/notes/naurs-compiler-case-tests-one-historically-bounded-documentation-and-consumption-system.md at `50121b7178058782f7b264127bbd23d94f7eeff5`; the live note may have changed.

### Formal execution is not the same as explicitly formulated criteria

The body uses this distinction to reject the inference that a capacity not reducible to a finite explicit rule set must be human-only. Naur argues that recognizing the similarity between a new demand and existing program facilities cannot be reduced to a limited set of criteria, and he places machine execution on the rule-determined side of that divide ([Naur, §§3–5](https://ingenieria-de-software-i.github.io/assets/bibliografia/programming-as-theory-building.pdf)). That bridge fit programs whose relevant judgments were implemented by rules a programmer had formulated. A trained recognizer is still formally executed computation, but its numerical parameters need not yield an explicit human-writeable rubric for the similarity judgment it performs. If those parameters count as formulated criteria, trained recognition refutes Naur's inexpressibility premise; if they do not, formal execution no longer entails formulated criteria. Either way, the human-only conclusion does not follow. This does not prove that an LLM-plus-artifact composite holds a program theory; it makes that an empirical question.

Adapted from kb/notes/naur-equates-machine-execution-with-formulated-criteria.md at `50121b7178058782f7b264127bbd23d94f7eeff5`; the live note may have changed.

### Behaviour-changing writes require selection, validation, authorization, and coordination

The body uses this claim to expose what the schematic learning loop hides. Persistence alone copies content into future state; it does not decide which candidate should shape behaviour, whether the candidate preserves prior capabilities, through which consumption path it gains force, or how it remains consistent with other mutable parts. Selection chooses among proposed changes. Validation supplies reject-capable evidence about the candidate. Authorization determines whether and how the accepted change becomes operative. Coordination manages coupled changes across natural-language artifacts, symbolic software, and any other writable form. A write counts as learning by the house only when the house's own evidence-responsive loop selects and retains it because experience bears on improvement, and the retained result changes later handling of a job not yet given. The same durable edit chosen by a person is maintenance by that person, not autonomous learning by the house.

Adapted from kb/notes/continual-learning-requires-governing-behaviour-changing-writes.md at `50121b7178058782f7b264127bbd23d94f7eeff5`; the live note may have changed.
