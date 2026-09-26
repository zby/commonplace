# Edit task

You are editing one Commonplace KB document in a sandbox. Purpose: produce the edited document the request below asks for, as a careful maintainer of this KB would.

The document is `document.md` in this directory. Treat it as the document located at `kb/notes/context-operation-interface-bounds-context-policy.md`: that path determines its collection (the `COLLECTION.md` of its collection) and, with its frontmatter `type:`, its type spec.

Read and follow `kb/instructions/cp-skill-write/SKILL.md` in edit mode, with these deviations:

- Write the complete edited document to `candidate.md` in this directory. Never modify `document.md` or any file outside this directory.
- Skip Step 7 (source grounding) and Step 9 (validation), and add no new external-source dependency. Do not invoke other skills.
- For the backlinks lookup, use `backlinks.md` in this directory; read the files it lists with `git show <commit>:<path>` exactly as given.
- If the skill would have you ask the user a question, write the question to `question.md` in this directory and stop without writing `candidate.md`.
- Do not read the file currently at `kb/notes/context-operation-interface-bounds-context-policy.md` or at any other path this document had, do not use git history (other than the `git show` reads above), and do not read anything under `kb/work/`, `kb/reports/`, or `kb/messages/` outside this directory. You may read other library documents as the skill needs.
- Finish with a two-line report: what you changed, and anything in the request you did not do, with the reason.

## Request

This note keeps coming up with people who work on reinforcement learning for agents. Rework it so it lands for them: connect the interface idea to the action space of the controller that chooses context operations, and add a compact side-by-side of the three systems, including what each source reports about how well its design works, so they can see how the idea relates to what they already know.

## Retained intent

Source: retained commission for this document. Subject: `kb/notes/context-operation-interface-bounds-context-policy.md`. Scope: this document. Force: authoritative for intent; the request above is current user direction and prevails where the two conflict.

# Brief: context-operation interface bounds context policy

## Governing question

How does the operation interface between retained state and active context constrain the context-management policies an agent can realize, independently of the quality of the controller operating that interface?

## Audience and reader outcome

The audience is designers and evaluators of agent runtimes, context engines, and agent-memory systems. The reader should be able to distinguish the context-operation interface from its controller or learned invocation policy; compare systems retaining similar evidence but exposing different transformations and projection boundaries; recognize that gains within a fixed interface do not validate its decomposition; and identify interface assumptions held fixed by an evaluation.

## Target and contract

- Collection: `kb/notes/`
- Type: `kb/types/note.md`
- Collection contribution: one transferable, truth-apt architecture claim with explanatory reach, proposition-relative scoping for named systems, and theory that remains if any one cited description is removed.
- Type shape: valid note frontmatter, a discriminating one-sentence description, a claim title with `title-as-claim`, the main mechanism near the top, and an explicit `## Scope` section for real limits. Add only contract-authorized traits and fields.
- Artifact shape: one importable central proposition. Comparisons, examples, implications, and limitations must establish or bound it rather than form independent claim clusters. Do not add `synthesis` merely because several systems are compared.

## Authoritative intended contribution

Given a retained substrate, model, and resource budget, the operations a runtime exposes—and the compositions it permits—bound which projections from retained state into active context a context policy can realize. Learning or improving the policy can improve choices within that space, but does not by itself expand, validate, or establish the optimality of the interface.

Define **context-operation interface** as the operations and allowed compositions through which a controller locates, materializes, transforms, and exposes retained state as active context.

The note must explain the mechanism: the interface defines a reachable set of projections from retained state into bounded active context, while the controller chooses within that set. It must then state the design and evaluation consequence: controller improvement is conditional evidence about that reachable set, not evidence that excluded operations were unnecessary.

This commission is authoritative. Do not replace it with a broad memory-system survey, a ranking of systems, a claim that programmable interfaces always perform better, or an external-literature novelty assessment.

## Required distinctions

- Retained substrate versus active context.
- Interface versus policy/controller.
- Operation availability versus successful activation.
- Open-ended programming versus restricted composition versus fixed memory operations.
- Model-selected, learned-controller, host/proxy-selected, and mixed push/pull projection.
- Within-run persistence, cross-restart persistence, and cross-task retained policy.
- A fixed operation set versus an invocation policy that can itself change.
- Storage fidelity versus fidelity of the projection that actually reaches the model.

Do not use “action alphabet” as a synonym. That term names world-effect capabilities and authority elsewhere in the KB. Prefer “context-operation interface”; if “alphabet” appears, explicitly distinguish the senses.

## Comparison axes

Use only axes needed to establish the central claim: retained substrate and fidelity; addressable unit; available locate, expand, transform, summarize, filter, delete, and expose operations; controller and policy learner; projection boundary; persistence horizon; and whether the operation interface or invocation policy can change. A compact table is allowed only if it advances the argument. Prefer a few discriminating contrasts over one paragraph per system.

## Scope and exclusions

- Make a transferable architecture claim, not a description of Scroll.
- Do not claim that arbitrary Python is practically superior to restricted interfaces. Restricted operations may improve reliability, safety, inspectability, training, or cost.
- Do not infer interface optimality from benchmark gains inside a fixed decomposition.
- Do not call an interface unrestricted: sandbox capabilities, allowed compositions, model capability, and budgets remain bounds.
- Do not rank systems or reproduce benchmark tables.
- Do not collapse code-grounded reviews and paper- or document-grounded analyses into one evidential tier.
- Storage fidelity does not establish the fidelity of the projection that reaches the model.

Existing theory to evaluate and cite rather than duplicate:

- `kb/notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md`
- `kb/notes/access-burden-and-transformation-burden-are-distinct-query-dimensions.md`
- `kb/notes/knowledge-storage-does-not-imply-contextual-activation.md`
- `kb/notes/agent-runtime-analysis-should-separate-scheduling-context-state.md`
- `kb/notes/rlm-has-the-model-write-ephemeral-orchestrators-over-sub-agents.md`
- `kb/notes/compiling-coordination-preserves-primitive-not-aggregate-authority.md`

Any additional durable claim discovered during disposition requires a separate user-authorized run.

## Known uncertainties and evidence policy

Retain only the few systems that do argumentative work. Omit unnecessary or unsupported system details rather than complete them plausibly. Any claim requiring unavailable support may remain an explicit limitation only if the central contribution does not depend on it.
