# Brief: integrate Cordis into the select/call lemma

## Question the target must answer

When can an effectful, dynamically reconfigurable agent harness still be treated as a select/call program, and what does that equivalence preserve?

The target must distinguish the mechanical transformation around LLM call sites from stronger claims about symbolic orchestration, external effects, runtime reconfiguration, rollback, and scheduler quality.

## Audience and intended consequence

The audience is an agent or maintainer using the computational-model cluster to analyze harnesses or transfer a result proved for the select/call loop to another program.

After reading the target, that reader should be able to:

- decide whether a candidate program satisfies the lemma's actual preconditions;
- identify the complete explicit state needed for resumption;
- avoid hiding non-LLM environmental effects inside a supposedly symbolic `select`;
- distinguish an LLM making a control judgment from symbolic code executing that judgment;
- state what must be reified when the active harness program or plugin composition changes;
- know which properties the transformation preserves and which require additional effect or lifecycle semantics.

## Governing purpose supplied by the user

Integrate the Cordis paper and its concrete use as the basis of DeepSeek Harness into Commonplace's computational model, with particular attention to `kb/notes/any-symbolic-program-with-llm-calls-is-a-select-call-program.md`.

This direction is authoritative for the workshop commission. It does not pre-authorize a conclusion that Cordis confirms, refutes, or replaces the lemma; source reconstruction must determine the relationship.

## Target contribution

Substantively revise the existing note so its decomposition lemma remains as strong as its proof warrants and no stronger. The intended contribution is a precise normal-form claim plus explicit boundaries for:

- non-LLM effects and observations;
- dynamic program/configuration state;
- LLM-produced scheduling judgments;
- concurrency and mid-call change;
- the difference between call-trace equivalence and full operational equivalence.

The current run may conclude that one adjacent note is needed, but it must not create or draft that second artifact. Keep the incumbent title if the qualified lemma still supports it; changing the title is allowed only if the proof's weakest correct formulation requires it.

## Scope

In scope:

- the decomposition construction and what “same LLM calls” means;
- whether a full request includes provider, model, prompt, tool schemas, and parameters rather than prompt text alone;
- the relation between scheduler state `K`, active program/configuration `Γ`, and a fixed meta-interpreter;
- programs that issue tool, filesystem, network, timer, or other host operations between LLM calls;
- Cordis revertible effects, reactive coeffects, committed dependency views, and component lifecycle as semantics for changing the host machine;
- DeepSeek Harness as a current implementation witness: plugin-defined loop, model adapter, tools, prompt assembly, event-sourced session state, and live control events;
- downstream claims that rely on select/call universality.

Out of scope:

- a general review of DeepSeek Harness quality or benchmark performance;
- a claim that Cordis makes arbitrary agent actions reversible;
- a design for Commonplace's own runtime;
- the optimizer/evaluator required to decide whether a harness change is beneficial;
- promotion of a separate self-modifying-harness or effectful-dispatch note;
- edits to downstream notes during this run.

## Required terminology and distinctions

- `K`: explicit symbolic machine state sufficient to resume execution under the stated program.
- `Γ`: provisional notation for the active harness composition or program/configuration generation; reconstruction must decide whether it is analytically separate or simply part of an enlarged `K`.
- `select/call`: the existing LLM-call-oriented normal form.
- `select/dispatch`: provisional name for a possible effectful normal form over an operation alphabet; do not promote it as vocabulary unless the argument needs it.
- **LLM-call trace equivalence**: same LLM requests in the same order.
- **Operational equivalence**: preservation of relevant non-LLM effects and observations as well as calls; do not conflate it with trace equivalence.
- **Mechanical representability** versus **architectural quality**: a model-mediated scheduling decision may remain representable even when it degrades the clean scheduler/LLM separation.
- **Mediated system boundary**: only state and effects brought into the explicit machine/context can support exact reasoning or structured recovery.

Use `Cordis`, `DeepSeek Harness`, `context`, `effect`, and `coeffect` according to the source and project vocabulary. Do not treat “everything is a plugin” as eliminating the fixed Cordis meta-machine.

## Collection and type constraints

- Target collection: `kb/notes/`; theoretical profile and explanatory-reach quality goal.
- Target type: `kb/types/note.md`.
- Keep the title as a contestable general claim.
- State the weakest assumptions actually used.
- Preserve body composability; DeepSeek Harness is a worked witness, not the note's subject.
- A substantive revision must not acquire `user-verified: true`.
- Use authorized note outbound labels only.

## Source and evidence inputs

Primary local source:

- `kb/sources/a-programming-paradigm-for-spatiotemporal-composability.md`

Local analysis and theory context:

- `kb/sources/a-programming-paradigm-for-spatiotemporal-composability.ingest.md`
- `kb/notes/bounded-context-orchestration-model.md`
- `kb/notes/llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md`
- `kb/notes/the-practical-scheduler-is-the-host-language.md`
- `kb/notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md`

Primary implementation sources, pinned to DeepSeek Harness revision `47f943859bef60e4160492346772ded9b24f765a` as observed 2026-08-14 and to be read directly rather than through search snippets:

- `https://github.com/deepseek-ai/deepseek-harness/tree/47f943859bef60e4160492346772ded9b24f765a`
- `https://github.com/deepseek-ai/deepseek-harness/blob/47f943859bef60e4160492346772ded9b24f765a/docs/architecture.md`
- `https://github.com/deepseek-ai/deepseek-harness/blob/47f943859bef60e4160492346772ded9b24f765a/docs/subsystems/core.md`
- `https://github.com/deepseek-ai/deepseek-harness/blob/47f943859bef60e4160492346772ded9b24f765a/docs/agent-lifecycle.md`
- `https://github.com/deepseek-ai/deepseek-harness/blob/47f943859bef60e4160492346772ded9b24f765a/docs/tool-execution-pipeline.md`
- `https://github.com/deepseek-ai/deepseek-harness/blob/47f943859bef60e4160492346772ded9b24f765a/docs/capability-seams.md`

Structural contracts:

- `kb/notes/COLLECTION.md`
- `kb/types/note.md`

The fresh reconstruction context must not read `original.md`, any draft, or prior assistant conclusions.

## Retained intent inputs

- Source: current user direction, 2026-08-14. Subject: integrate Cordis/DeepSeek Harness into the computational model, especially the select/call note. Scope: selects the workshop and target, not the factual conclusion. Role: authoritative commission.
- Source: the incumbent note. Subject: existing mechanical lemma and its downstream role. Scope: incumbent commitments to preserve, alter explicitly, or reject during audit. Role: authoritative current library state, withheld from source-first reconstruction.
- Source: prior assistant analysis in the current conversation. Subject: possible `Γ`-indexed select/call interpretation, effectful-dispatch extension, and correction to the LLM-mediated scheduling boundary. Scope: candidate hypotheses only. Role: advisory; it may focus questions but cannot warrant claims.

## Known uncertainties and evidence boundary

- DeepSeek Harness is in developer preview. Implementation evidence is fixed to revision `47f943859bef60e4160492346772ded9b24f765a`; any claim about a later version requires a new pin or durable capture. This is non-blocking for reconstructing the general Cordis relationship.
- The Cordis paper proves properties under explicit independence, dependency, termination, and mediation assumptions. The target may use only the properties relevant to the decomposition lemma and must carry their scope.
- It is not yet established whether the cleanest repair enlarges `K`, introduces configuration `Γ`, or limits the lemma to a projection over LLM calls. Reconstruction must compare these formulations.
- It is not yet established whether an effectful operation alphabet needs a companion note. The target can name this as an open boundary without solving it.
- A replayable session log does not by itself establish replayable external-world state or a pinned harness generation. Check the implementation sources before making either claim.

## Decisions reserved for the user

None before source reconstruction. Promotion remains separate because the user asked to create and retain a workshop rather than to edit the library note immediately.
