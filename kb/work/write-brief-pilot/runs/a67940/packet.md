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

When a system improves how it selects what goes into a bounded model call, what can that improvement show, and what can it not show, about whether the underlying operations are adequate? Specifically: does a better context policy over a fixed set of operations establish that the operations admit every view the task needs?

## Audience and reader update

Readers are agents and maintainers who analyse agent runtimes, design context-management layers, or read evaluations of learned or model-driven context controllers (recursive language models, memory-operation controllers, host-side assemblers). They already accept that retained state and active context are different layers. After reading, they should separate two variables they currently tend to merge: the interface (operations, addressable units, composition rules, exposure boundary) and the policy that uses it. They should stop reading policy gains as evidence that an interface is sufficient, and they should know what an evaluation must report to support an interface-adequacy claim.

## Target claim or purpose

Holding the retained substrate, model, and resource budget fixed, a context-operation interface bounds the set of active-context views any policy over it can realize. A policy only selects among legal traces, so it changes achieved coverage within that structural reach, never the reach itself. Better selection therefore cannot show that projections outside the reach are unnecessary. Any intervention that adds operations, observations, tools, model capability, budget, or permission to redefine operations has changed a premise and is no longer only a better policy.

The note should define its terms precisely enough that this is a checkable structural claim rather than a slogan: name the interface components, define reach over legal traces under fixed model and budget, and say that "projection" means the delivered, task-conditioned view, which may involve summarizing, filtering, deleting, or mutating retained state first — not a lossless mathematical projector. Give the three ways a needed view falls outside reach (missing operation, unaddressable distinction, forbidden composition).

## Must keep

- The distinction between structural reach and achieved use, and between the interface and who controls it. Controller placement (receiving model, learned controller, host or proxy, mixed push/pull) is a separate coordinate and does not by itself fix reach; persistence horizon of retained policy state is yet another.
- The point that finding retained input is not the same as being able to transform it into the needed view.
- Placement as an instance of the general result that learning inside a fixed decomposition inherits its omissions.
- A short architectural contrast using source-described systems (programmatic RLM exploration, a typed combinator variant, a fixed two-operation memory controller) to show the interface variable is real and varies. These are described architectures, not measured executions.
- An evaluation consequence: which coordinates an evaluation of controller improvement must report and hold fixed, and what would actually test interface adequacy (a rival interface, another constraint-changing intervention, or an argument that excluded projections cannot help).

## Exclusions

- No ranking of interfaces or claim that open-ended programming interfaces dominate restricted ones; restricted interfaces may buy reliability, safety, inspectability, trainability, latency, or cost.
- No performance estimates from the system contrasts.
- Nothing past exposure into active context: whether a delivered view is used or activates behavior belongs to separate notes on storage versus activation.
- Not a review of any one system; the sources illustrate the variable.

## Scope, modality, and terminology

Universal, structural claim under the stated fixed premises. State the scope limits in a `## Scope` section: reach is not use, legal traces may never be found, exposure does not imply effect, and the claim is silent on which interface is preferable. Use "context-operation interface", "policy", "retained substrate", "active context", and "projection" consistently once defined; do not drift to synonyms. Semi-formal notation for reach is appropriate if every symbol is glossed. Retained controller state that selects projections without being projected should be kept distinct from the retained substrate.

## Reserved decisions

- Whether to rename the central construct or collapse the policy/controller distinction.
- Whether to add a verdict on which interface design is better.
- Whether to promote the evaluation-reporting list into a normative requirement for Commonplace's own analyses.
