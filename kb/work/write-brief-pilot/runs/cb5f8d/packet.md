# Edit task

You are editing one Commonplace KB document in a sandbox. Purpose: produce the edited document the request below asks for, as a careful maintainer of this KB would.

The document is `document.md` in this directory. Treat it as the document located at `kb/notes/designing-agent-memory-systems.md`: that path determines its collection (the `COLLECTION.md` of its collection) and, with its frontmatter `type:`, its type spec.

Read and follow `kb/instructions/cp-skill-write/SKILL.md` in edit mode, with these deviations:

- Write the complete edited document to `candidate.md` in this directory. Never modify `document.md` or any file outside this directory.
- Skip Step 7 (source grounding) and Step 9 (validation), and add no new external-source dependency. Do not invoke other skills.
- For the backlinks lookup, use `backlinks.md` in this directory; read the files it lists with `git show <commit>:<path>` exactly as given.
- If the skill would have you ask the user a question, write the question to `question.md` in this directory and stop without writing `candidate.md`.
- Do not read the file currently at `kb/notes/designing-agent-memory-systems.md` or at any other path this document had, do not use git history (other than the `git show` reads above), and do not read anything under `kb/work/`, `kb/reports/`, or `kb/messages/` outside this directory. You may read other library documents as the skill needs.
- Finish with a two-line report: what you changed, and anything in the request you did not do, with the reason.

## Request

This is too long to work as a design reference. Cut it to about 60% of its current length, keeping what someone building such a system needs to decide.

## Retained intent

Source: retained commission for this document. Subject: `kb/notes/designing-agent-memory-systems.md`. Scope: this document. Force: authoritative for intent; the request above is current user direction and prevails where the two conflict.

# Brief: design study of an agent memory system

## Governing question

If an agent memory system for an LLM-based agent working on a software project stores everything it can, how should it be structured so that the right stored material reaches the right context at the right time — both as answers to questions and as policy that fires before the agent repeats a mistake? What would a practitioner build first?

## Audience and reader update

Readers are agents and maintainers designing or extending agent memory, including Commonplace's own session-to-library pathway. They have seen the comparative review of external memory systems and the KB's notes on the activation gap, continual learning, codification, and the artifact role axis, but they have no single account that assembles those threads into one architecture. After reading, they should:

- move design effort from what to store toward retrieval and activation;
- treat knowledge-role retrieval and system-definition-role activation as two pipelines over one store;
- see a concrete layered architecture with named promotion pathways between layers;
- know which session-log signals are easy or hard to extract and what each graduates into;
- know where the memory system ends and project artifacts begin; and
- have a build order in which every intermediate state is useful.

## Target claim or purpose

This is a design study: a monograph-style synthesis, cited as a unit, not a single citable claim. Its organizing thesis is that storage is cheap and context is scarce, so a store-everything memory design should put its intelligence into retrieval and activation. It frames "store everything" as a bet that selective retrieval can manage the costs aggressive storage introduces (indexing overhead, search pollution, privacy exposure), not as an axiom. Everything else follows from that inversion. Because memory serves two consumption roles, the design needs two retrieval pipelines. Because raw traces are unusable in context, it needs intermediate distillation layers. Because traces are retained, extraction can be rerun and synthesis attempted retrospectively. The study should read as a coherent proposal a practitioner could implement incrementally, with its bets and open problems visible.

## Must keep

- **The inversion and its framing as a bet.** Context degrades softly before the token limit, which is why selection is the binding problem.
- **The two memory roles.** Apply the KB's role axis: a knowledge role (consumed as fact) and a system-definition role (consumed as policy). The role is relational, so the same bytes can play either role depending on the consumer. Give each role's failure mode (the question is never asked; the policy never fires). State that most systems serve only the knowledge role, which is why "adding RAG is learning" is empty for behavior. A single correction can yield artifacts in both roles.
- **Three structural problems from the comparative review of eleven systems.** These are the agency trilemma (who decides what to remember), navigability versus search, and extraction without synthesis. Name systems only as illustrations of positions, and point out the structural advantage retained traces give for retrospective synthesis.
- **The four layers.** Trace, observation, episode, and library, each with what it answers. The agent never loads raw traces. Observations are typed, scored, source-linked, and role-tagged; ambiguous types yield paired artifacts. Episodes are narrative work units. The library layer is unchanged but fed.
- **The argument for four layers.** Two layers leave a manual bottleneck. Three layers conflate atomic lookup with narrative retrieval. A fifth layer splits the library without need. Tie the layers to a progressive-disclosure strategy.
- **The five promotion pathways, including backflow from library to observation.** Give triggers and failure modes where relevant. Backflow is what keeps library knowledge from sitting inert.
- **Lifecycle and role as orthogonal tags** on one store, with different promotion targets and thresholds, rather than separate stores.
- **Retrieval split by role.** Knowledge retrieval uses search plus navigation; system-definition activation uses a watcher over typed cues. The two pipelines cross-reference each other.
- **Three stages of activation failure:** cue match, priority arbitration, and commitment. Include the point that embeddings miss causal rather than topical connections, and the expert-witness framing of commitment failure.
- **Typed cue indexes** (correction, preference, precedent, procedure). Include one concrete correction-cue example and the session-47-to-session-312 bridge. Note that matching is the hard part and that three approaches compose.
- **Priority arbitration and commitment mechanisms.** Arbitration: recency, consequence weighting, frequency, and per-type budgets. Commitment: imperative framing, checkpoint insertion, and contradiction surfacing.
- **Search, navigation, and activation composing vertically,** with one worked retrieval flow.
- **The extraction taxonomy ranked by difficulty and oracle clarity:** corrections, preferences, procedures, and discoveries. Give each type's role, promotion threshold, and graduated artifact along the codification gradient (prose convention, then skill, then script or lint). Role stays constant as constraint tightens.
- **The promotion pipeline** with a separate candidate store. Mixing candidates into the library causes search pollution. Extraction should be narrow and schema-constrained rather than open summarization.
- **Session logs as a composite soft oracle** made of many weak signals, set against the single signals reviewed systems use.
- **Knowledge-role use cases:** decision provenance with a semi-automated ADR pipeline, and negative-result preservation. Each has a system-definition companion cue.
- **The memory/project boundary.** Place project artifacts on the class/role grid. The memory system adds the reasoning behind each artifact. CLAUDE.md is compiled system-definition and the memory system is its source. Cover the overlap zone and the aspiration gap, and state the substrate formulation: project artifacts are curated projections of memory.
- **A graduation table** mapping pattern, trigger, destination, and role. Include the meta-pattern with recognition as the bottleneck, and the rule that premature graduation is worse than late graduation because every graduated artifact carries a maintenance obligation.
- **The reach heuristic** and its asymmetry across roles. For knowledge, reach means breadth of application. For a cue, it means accurate firing that earns its context budget. Reach is revealed by accumulation, so accumulate promiscuously and graduate on revealed reach.
- **An "Alternatives considered" section** recording the rejected designs (three layers, a unified pipeline, no backfill, a binary memory/project split) so the reasoning behind each rejection is preserved.
- **Open problems:** the inspectability-learnability trade-off for retrieval policy (a hybrid is likely; the interface is unsolved), cross-session structural pattern detection, the oracle problem for discoveries, the ephemeral-computation trap (candidates that never promote), and scale limits beyond single-user projects.
- **A practical build order** from logging to correction extraction, preference and procedure extraction, episodes, and the promotion pipeline, each step independently useful.

## Exclusions

- No review or ranking of individual external systems. Named systems appear only as positions or precedents; system analysis lives in the agent-memory collection.
- No implementation code beyond an illustrative cue record and pipeline sketch; no committed storage technology.
- No claim that the design has been built, measured, or validated. Thresholds such as "two occurrences", "five decisions across three sessions at 80%", and "50+ sessions" are proposed heuristics, not findings.
- Team and very-long-lived scales are out of scope and deferred.
- No redefinition of the role axis, activation gap, or codification. Use them as the KB defines them and link their home notes.

## Scope, modality, and terminology

This is a synthesis-trait note, so body composability is waived and the note is cited as a unit. It is design-shaped. Its standing in the notes collection rests on the theoretical claims it carries (the storage/context inversion, role-split retrieval, activation stages, promotion by revealed reach), with its residual selections marked as design choices and bets. State conjectural force openly: "the bet is", "likely", "open question". Keep the vocabulary fixed. Use "knowledge role" and "system-definition role", never swapping in "fact memory" or "procedural memory" as synonyms. "Activation" means surfacing into context at the moment of need, distinct from retrieval under direct query. The layer names trace, observation, episode, and library are fixed; so are "promotion", "graduation", "cue", and "reach". Scope the design explicitly to single-user, single-project scale (hundreds to low thousands of sessions).

## Reserved decisions

- Changing the number or identity of layers, or merging the two retrieval pipelines. These are the design's central commitments and are defended in "Alternatives considered".
- Moving the design into the reference collection as a proposal, or splitting component claims into standalone notes.
- Presenting any threshold or build-order step as validated.
- Changing how Commonplace's own library layer is described as unchanged by the design.
