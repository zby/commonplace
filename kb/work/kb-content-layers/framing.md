# KB Content Layers Workshop

## Origin

Started from a narrower question: do we need per-collection WRITING procedures in commonplace (`kb/notes/`, `kb/reference/`, `kb/instructions/`), or can the current single `WRITING.md` plus per-type instructions cover it?

That question surfaced a deeper one that isn't specific to commonplace: **every KB holds at least three distinguishable kinds of content**, and the WRITING-per-collection question only has a clean answer once the general structure is named.

## Methodological angle

See [angle.md](./angle.md). The workshop commits to approaching the three registers as three LLM-specific sub-disciplines rather than borrowing classical philosophy wholesale:

- Theory layer → **epistemology for LLMs**
- Description layer → **ontology for LLMs**
- Prescription layer → **praxeology for LLMs** (Kotarbiński's sense, not Mises's)

This is a constraint on how the workshop proceeds: classical concepts are re-derived for agents whose knowledge is context-loaded, whose worlds are read-about not perceived, and whose rules are executed at read-time without internalization. Concepts that don't translate are named as gaps, not forced.

## The claim this workshop is testing

> Every KB holds content of three distinct kinds:
>
> - **Theories** — transferable claims about what is true (mechanisms, principles, general arguments). Quality goal: reach.
> - **Descriptions** — accounts of what exists in a particular system (architecture, current state, type inventories). Quality goal: fidelity to the described system.
> - **Prescriptions** — directives about what to do or not do (procedures, conventions, proscriptions). Quality goal: executability / followability.
>
> The three kinds are governed by different quality criteria, consumed via different queries, and — most consequentially — have an **asymmetric linking topology** between them.

This is not a commonplace-specific split. A personal research KB, an engineering-team KB, and an operations KB all have theories, descriptions of what the team / codebase / infrastructure is, and rules they hold themselves to.

If the claim is right, commonplace's `kb/notes/ + kb/reference/ + kb/instructions/` is already an instance of the pattern, and the per-collection WRITING question is the question of how the layers should differ in authoring and linking.

## The linking asymmetry (the load-bearing insight)

The sharpest lever here. Between the three registers, the six possible directed links are not symmetric:

| From → To | Allowed? | Notes |
|---|---|---|
| Theory → Theory | Yes | The claim-traversal graph. |
| Theory → Description | **No** (load-bearing) | A theory that depends on a particular system's description stops being transferable. This is the constraint. |
| Theory → Prescription | **No** (load-bearing) | Same reason. |
| Description → Theory | Yes | A description can cite theories as rationale ("this is why the system is shaped this way"). |
| Description → Description | Yes | Subsystem docs reference each other. |
| Description → Prescription | Sometimes | "To operate this, follow X procedure" — acceptable when the description is operator-facing. |
| Prescription → Theory | Yes | Procedures cite the rationale they instantiate. |
| Prescription → Description | Yes | Procedures refer to the things they act on. |
| Prescription → Prescription | Yes | Procedures compose. |

The core constraint: **theories do not link down**. If a theory cites a description or a prescription to make its argument, it has absorbed that dependency and is no longer transferable — the system changes and the theory breaks silently.

Evidence this is already half-built in commonplace:

- `cp-skill-connect` excludes workshops and reports from the link graph. Workshops are ephemeral; reports are run outputs. Neither should be cited as foundation by transferable notes. This is the same asymmetry applied to a temporal axis.
- `title-as-claim-enables-traversal-as-reasoning.md` already carves out multi-claim specs and definitional notes from the claim-title convention. Those exceptions are exactly description-layer and prescription-layer documents.
- `kb/reference/README.md:21` states that reference docs should be "self-contained within the shipped surface" with no links back to the methodology library — this is the asymmetry constraint enforced on descriptions.

Open: is "load-bearing" the right distinction, or is the rule cleaner? Maybe theory → description is *never* allowed, period, even as a see-also. The stricter version is easier to validate.

## The central question: separate spaces or mixed?

**Arguments for separate directories (commonplace's current shape):**

- The linking constraint is enforceable by path — a validator can grep for forbidden cross-layer links.
- Loading hierarchies can respect the layer: load theory only when reasoning, description only when answering operator questions, prescription only when executing a procedure.
- Progressive disclosure works at directory level.
- Quality goals are homogeneous within a directory — WRITING conventions can be per-directory without contradiction.
- Different collections can have different index structures appropriate to their query pattern.

**Arguments for a mixed / flat space with traits:**

- Straddling documents (a note that makes a theoretical claim AND describes how commonplace instantiates it) have no home in the separate model. They get split or duplicated.
- Directory boundaries are brittle when content evolves — a theory that gets more specific is hard to "move down."
- Related documents across layers can sit next to each other — the practitioner's mental model may group by topic, not by kind.
- Trait-based marking (`layer: theory | description | prescription`) is more flexible and survives reorganization.

**Middle-ground:**

- Separate directories as the operational default, with an explicit mechanism for "extraction" — promoting a theory out of a description when it stabilizes, or specializing a theory into a prescription when it's codified.
- The directory is the staging area; the trait (if it exists) is the actual classification.

## The practical question this workshop is trying to answer

Once the general structure is named, the original question has an answer:

- **Per-collection WRITING procedures** make sense if collections correspond to layers and each layer has a distinct quality goal and linking discipline.
- **Per-type instructions** handle the structural contract of specific document types within a layer.
- **Shared base WRITING.md** holds mechanics that are truly universal (frontmatter format, link syntax, filenames).

The three-register hypothesis gives a principled reason to split WRITING.md that isn't just "the file got too long." Per-collection conventions exist because the collections are different kinds of content, not just different piles of the same kind.

## Open questions

1. **Is "prescription" one category or two?** The user's original word was "proscription" (forbidding). Are proscriptions a distinct layer (normative constraints) from prescriptions (procedures)? Or both sub-kinds of a single "directives" layer? Working hypothesis: one layer, both covered.

2. **Where do workshops fit?** Workshops hold drafts of all three kinds in progress. They're orthogonal — a fourth axis (temporal / in-flight), not a fourth layer.

3. **Where do reports and sources fit?** Reports are descriptions of a particular run (short-lived). Sources are raw material for theory (raw, not yet theory). Both seem to be sub-kinds of description with different lifetimes.

4. **Are indexes a layer or a cross-cut?** Indexes navigate all three registers. They're probably a cross-cutting navigation mechanism, not a fourth kind.

5. **Does the type system already encode this?** `note` / `structured-claim` → theory; `spec` / architecture doc → description; `instruction` → prescription; `index` → navigation. If so, the three registers might be deducible from the type, and a separate `layer` field is redundant.

6. **How does this interact with reach?** Reach is the quality criterion for *theories*. Descriptions are evaluated on fidelity, not reach. Prescriptions are evaluated on executability. The existing reach note generalizes — it should say reach is the quality axis for one of three registers, not the universal goal.

7. **Strict or lax linking rule?** Is theory → description forbidden absolutely, or only as load-bearing? The stricter rule is mechanically enforceable; the laxer rule respects see-also links that don't create dependency.

8. **Does commonplace's current structure need to change?** If yes, what moves? If no, what gets documented as the rationale for the current shape?

## Decisions made

1. **Linking rule: lax, not strict.** Theory → description is allowed as **exemplifies / evidence** but not as **grounds / foundation**. The theory must stand if the example is deleted. This was decided after observing 179 inbound links from theory notes into related-systems — nearly all are exemplifies links, and forbidding them would be artificial. The strict rule (never link down) is too strong.

2. **Workshop output is bounded.** One or two theory notes + an experiment plan. Not a finished architecture or a full rewrite.

3. **Reference conventions are deploy-time learning artifacts.** Per-collection WRITING conventions are instructions to agents — early on the verifiability gradient. We iterate them from use, not design them perfectly upfront. The whole `kb/reference/` design should be treated as experimental, consistent with the [deploy-time learning thesis](../notes/deploy-time-learning-is-the-missing-middle.md): constrain only when patterns emerge from runs, and relax when new requirements reveal wrong commitments.

4. **Related-systems is a candidate for its own collection** (`kb/related-systems/`). It's a different kind of description (landscape/external) than `kb/reference/` (system/internal). The move is a separate task, not part of this workshop.

5. **Terminology: "registers" not "layers" or "kinds."** The three content categories are registers — varieties of content adapted to different purposes, each with its own conventions and quality criteria. Borrowed from linguistics, where registers are varieties of language adapted to context. Avoids the hierarchy implied by "layers" and the blandness of "kinds."

6. **Linking rule revised: formulation constraint + maintenance asymmetry, not a linking prohibition.** The original rule ("theories must not depend on descriptions") was too strong — theories start with observations, and descriptions ARE observations. The real constraints are: (a) a theory must be statable in general terms even when derived from a specific system (formulation), and (b) theory changes flow downstream while description changes don't break upstream theories (maintenance direction). Theories can and should cite descriptions as evidence.

7. **The distillation chain runs theory → prescription → implementation → description**, not theory → description directly. Descriptions are accounts of implemented systems, not direct distillations of theory. This matters because descriptions can contradict the theory they descended from — the implementation discovered the theory was wrong.

8. **Directories are the register mechanism for now.** Other options exist (types, traits, convention-only) but directories are simplest and already match how we operate. The theory note lists all four options without committing to one universally.

## Next steps

1. ~~**Draft theory note 1**~~ — DONE. See `kb/notes/a-knowledge-base-holds-theories-descriptions-and-prescriptions-with-asymmetric-linking.md`. The three-register claim, formulation constraint, maintenance asymmetry, distillation chain, context-efficiency strategies (reach/economy/precision), and the "registers" terminology are all in the note.
2. **Decide if note 2 is needed** — the LLM-specific angle (epistemology/ontology/praxeology) is currently a section in note 1. Might deserve its own note if it grows.
3. **Design the per-collection declaration format** — each collection gets a `COLLECTION.md` (or equivalent) that declares:
   - What register it operates in (theoretical / descriptive / prescriptive)
   - Quality goals and context-efficiency strategy
   - Title and description conventions
   - Outbound linking conventions (what relationship types are appropriate when linking FROM this collection TO each register)
   - Within-collection writing conventions (the authoring guidance for agents writing in this collection)
   
   This is the source of truth. Practitioners add collections by creating a directory with a `COLLECTION.md` — no central file to edit.

4. **Build a compile step** — a deterministic command (`commonplace-compile-collections` or a skill) that reads all `COLLECTION.md` files and produces a single compiled topology document. This is what `cp-skill-connect` reads — one artifact with the full cross-register linking rules, instead of loading N collection guides. The compiled document is a deploy-time artifact: deterministic, diffable, on the verifiability gradient.

5. **Experiment with the format** — draft `COLLECTION.md` for `kb/notes/`, `kb/reference/`, and `kb/instructions/`. Test by running write and connect against notes in each collection and seeing whether the conventions produce better output. Iterate from observation.
6. **Adapt the writing skill** — one parameterized `cp-skill-write` that takes a target collection, reads that collection's `COLLECTION.md` for conventions, and reads the shared base `WRITING.md` for universal mechanics. The skill body is generic: the conventions, template, quality goals, and "what belongs here" guidance all come from `COLLECTION.md`. Per-collection skills (e.g. `cp-skill-write-reference`) can be thin wrappers that set the collection parameter.
7. **Adapt the connect skill** — reads the compiled topology document (produced by the compile step) for cross-register linking rules. When connecting a note, knows the source register from the source collection's `COLLECTION.md` and picks appropriate relationship types based on the target's register.

   Draft COLLECTION.md for notes is at [draft-collection-notes.md](./draft-collection-notes.md).

Full experiment plan is at [plan.md](./plan.md).
5. **Only then**: the related-systems move and the WRITING.md restructure follow as corollaries.

## Relation to other workshops

- `system-documentation/` — the commonplace-specific instance. That workshop produced `kb/reference/` as a description layer. This workshop generalizes the pattern.
- `philosophy-borrowing/` — already evaluating speech-act theory as a candidate borrowing. The three-register frame is a speech-act-style decomposition (assertive / representative / directive). Worth cross-pollinating.
- `type-system-rationalization/` — if the type system already encodes layers, this workshop's conclusions feed into type-system decisions.
- `obsidian-affordances/` — decisions about representation drift may depend on which layer the affordance touches.

## What this workshop is NOT

- Not a rewrite of `kb/reference/`. That's already done.
- Not a redesign of the type system. If types already encode layers, this just names the encoding.
- Not a commonplace-only document. If the claim is right, the output note is a general KB-design principle.
