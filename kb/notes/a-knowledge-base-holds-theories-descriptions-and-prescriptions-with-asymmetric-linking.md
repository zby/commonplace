---
description: "Three exhaustive registers — theory, description, prescription — with distinct quality goals; formulation constraint and maintenance asymmetry make the split real, distillation connects them; registers classify content orthogonally to operational roles, and in agent systems the prescription/implementation boundary collapses"
type: kb/types/note.md
traits: [title-as-claim]
tags: [document-system, foundations]
status: current
---

# A knowledge base holds theories, descriptions, and prescriptions with asymmetric linking

Every knowledge base writes in three registers, each with its own quality criteria:

| Register | What it does | Quality goal | Context-efficiency strategy | Example query |
|---|---|---|---|---|
| **Theory** | Makes transferable claims about what is true | [Reach](./first-principles-reasoning-selects-for-explanatory-reach-over-adaptive-fit.md) | One claim covers many situations — compress *across* contexts | "Why is X a good idea?" |
| **Description** | Accounts for what exists in a particular system | Fidelity + economy | One account covers the system in minimum tokens — compress *within* a single context | "How does X work here?" |
| **Prescription** | Directs what to do or not do | Executability + precision | One instruction says exactly what to do — compress to what's *actionable* | "How do I do X?" |

The three registers are exhaustive because they correspond to the three fundamental orientations toward knowledge: understanding why (theory), representing what exists (description), and directing action (prescription). Every question a KB consumer asks reduces to one of three forms: "Why is X a good idea?", "How does X work here?", or "How do I do X?" The classical philosophical tradition arrived at the same tripartition independently — epistemology, ontology, and praxeology (see below). If you try to state a fourth register, it collapses into one of the three: evaluations and reports are descriptions (they account for what was found); sources are pre-register raw material awaiting processing; proscriptions ("don't do X") are prescriptions with negative polarity.

The split recurs because the registers serve different queries and age differently. A personal research KB has theories (learned principles), descriptions (systems the person works with), and prescriptions (personal rules). An engineering-team KB has the same three — principles, codebase docs, runbooks.

All three registers face context budget pressure but respond differently. Any reader with bounded attention — a person scanning under time pressure, a team triaging documentation — benefits when descriptions are economical and prescriptions are precise. But the constraint is soft for humans: they skim, they tolerate redundancy, they fill gaps from memory. For LLM-operated KBs the constraint is hard: [context is the single scarce resource](./context-efficiency-is-the-central-design-concern-in-agent-systems.md), and every token competes for the same window. A bloated description or vague prescription directly degrades the agent's next action. This KB is designed for that harder case, where economy for descriptions and precision for prescriptions are what reach is for theories: the discipline that makes bounded context work.

## What makes the registers real

Two properties distinguish the registers from mere labels.

**Formulation constraint.** Descriptions are observations, so theories legitimately cite them as evidence. But a theory must be statable in general terms — its claim should stand without referencing any particular system. A theory can link to descriptions as evidence ("we observed X in system Y, which led us to theorize Z"), but its claim — title and opening argument — must hold independently. If you can't state it without saying "in commonplace, ..." it's still a description, not yet a theory.

**Maintenance asymmetry.** When a description changes (the system is redesigned), the theory's evidence base shifts — re-evaluate, but the theory may still hold from other evidence. A theory with one supporting observation is fragile; one with several is robust. When a theory changes, all downstream artifacts — descriptions citing it as rationale, prescriptions derived from it — may need revision. The theory is upstream; impact flows down.

| From → To | Typical relationship | Maintenance direction |
|---|---|---|
| Theory → Theory | since / because / contradicts / extends | Mutual — both may need revision |
| Theory → Description | evidence / derived-from / exemplifies | Theory may survive description changing |
| Description → Theory | rationale — "shaped this way because [theory]" | Description needs revision if theory changes |
| Description → Description | cross-reference between subsystems | Local impact |
| Prescription → Theory | justification — "this rule exists because [theory]" | Prescription needs revision if theory changes |
| Prescription → Description | reference — "this procedure acts on [system X]" | Prescription needs revision if system changes |
| Prescription → Prescription | composition — "after [step A], follow [step B]" | Local impact |

Without the formulation constraint, theories and descriptions blur — a "theory" that can only be stated in terms of one specific system is really a description with ambitions.

## The registers connect through distillation

[Distillation](./definitions/distillation.md) (directed context compression) and implementation connect the registers. The primary path runs through prescription:

```
theory  →  prescription  →  implementation  →  description
(claim)    (procedure)      (working system)    (account of what exists)
```

- **Theory → prescription** is the direct distillation step. WRITING.md conventions distill theory notes about title-as-claim, reach, and linking semantics into rules an agent can follow. The theory explains *why*; the prescription says *what to do*.
- **Prescription → implementation** is where the system gets built. Following prescriptions produces a working system, but implementations always deviate through edge cases, pragmatic compromises, and technical constraints.
- **Implementation → description** is where we account for what was actually built. A note like [why-notes-have-types](./why-notes-have-types.md) describes how *this* system's type system works — faithful to the implementation, not to the theory it descended from.

Descriptions are therefore not direct distillations of theory — they are accounts of systems built by following prescriptions derived from theory. This matters because descriptions can *contradict* their originating theory: the implementation may discover that the theory was wrong in some case, and the description faithfully records that reality.

This chain reinforces the maintenance asymmetry: changes flow down from theory through prescriptions and implementations into descriptions. When theory changes, its downstream chain may need revision — but the same theory might be implemented differently in a different system, so the theory's formulation should stay general.

## Registers and operational roles are orthogonal

Registers classify what an artifact *says* — its linguistic content. But artifacts also have operational roles — what they *do* in the KB:

| Operational role | What the artifact does | Example |
|---|---|---|
| Evidence | Supports or challenges a claim | A related-system review cited by a theory note |
| Executable instruction | Directs agent behavior at runtime | WRITING.md, a skill template |
| Generated report | Records the output of an operation | A review bundle, a connect report |
| Index / routing surface | Helps agents find other artifacts | tags-index.md, notes/dir-index.md |
| Workshop state | Tracks in-flight work | A task, a decision thread |

These roles cross-cut registers. A review report is generated by an operation but its content is descriptive — it accounts for what was checked and what was found. An index is an operational routing surface but its content is descriptive — it describes what exists in a collection. Workshop artifacts may contain prescriptive steps or descriptive state, but their operational role (lifecycle, expiration) is orthogonal to their register.

The interesting dual case is **instructions**. In a traditional system, the distillation chain has four distinct steps: theory → prescription → implementation → description. But in an agent-operated KB, markdown instructions are executed directly by the agent interpreter. WRITING.md is prescriptive by content ("use claim titles, check reach") and part of the working system by role — changing it changes agent behavior immediately. The prescription/implementation boundary collapses because natural-language instructions are part of the runtime:

```
theory  →  instruction/prescription
                    |
                    v
           working system behavior
```

This is not a fourth register. It is an orthogonal axis: what the artifact says (register) vs. what it does in the system (operational role). Instructions remain prescriptive text — they direct action, they optimize for executability and precision, they need revision when theory changes. But they are also executable, which means the maintenance asymmetry has immediate operational consequences: changing a theory note may require revising an instruction, and revising the instruction changes the running system.

## Evidence from this KB

Commonplace's existing collections instantiate this pattern:

- `kb/notes/` → theoretical register (transferable claims, [title-as-claim](./title-as-claim-enables-traversal-as-reasoning.md), optimized for reach)
- `kb/reference/` → descriptive register (how the shipped system works, topical titles, optimized for fidelity)
- `kb/instructions/` → prescriptive register (procedures and conventions, imperative titles, optimized for executability)
- `kb/notes/related-systems/` → a second descriptive collection (external landscape), candidate for promotion to `kb/related-systems/`

The separation was not designed from the three-register theory — it emerged from practical pressure. `kb/reference/` was created because system documentation didn't fit the theory-optimized conventions of `kb/notes/`. The theory names what practice already discovered.

The maintenance asymmetry is already visible in the link graph. A link audit found substantial inbound linking from theory notes into `kb/notes/related-systems/` — theories citing related systems as evidence and illustrations. The theories are stated in general terms; the related-system descriptions serve as supporting observations.

The [title-as-claim](./title-as-claim-enables-traversal-as-reasoning.md) convention already carves out multi-claim specs and definitional notes from claim-title requirements — exactly the documents written in the descriptive register. That carve-out recognizes that descriptions play a different role in traversal than theories.

Some notes currently in `kb/notes/` are better understood as descriptions. [Why notes have types](./why-notes-have-types.md) describes how this system's type system works — a description of our implementation, not a transferable theory. If the framework helps you see that a note belongs in a different collection, it's doing useful work. **TODO:** Once collection moves are complete, replace these examples with the new locations or remove them.

## The three registers correspond to classical sub-disciplines

The registers map onto classical philosophical sub-disciplines, each reshaped by LLM-operated KB constraints:

- **Theory → epistemology** — what can be known, what justifies a claim, what transfers across contexts. Reshaped: knowledge not loaded into context is functionally absent; reach measures how many future contexts one compressed claim serves.
- **Description → ontology** — what exists, what categories carve up a system. Reshaped: what exists is what can be named and retrieved; identity is maintained by the referencing graph, not by internal continuity.
- **Prescription → praxeology** — what counts as effective action, what patterns of work succeed. Reshaped: the agent reads the rule every time without internalization; instructions must survive first-reading execution. (Kotarbiński's general theory of efficient action is the stronger precedent here than Mises's economic framing.)

LLM constraints (no persistent memory, no direct perception, no habit formation) strip away human fallbacks, making the structural core of knowledge management visible. But the resulting claims vary in reach — many transfer to any reader with bounded attention, some are genuinely LLM-specific. Scope should be mapped per claim, not blanket-decided.

## Practical consequences

1. **Per-register writing conventions** are justified — each register has a different quality goal, so a single set of conventions undersells two of the three. Theory conventions enforce reach; description conventions enforce economy; prescription conventions enforce precision. Whether those conventions are keyed to directories, types, or traits is an implementation choice — see #2.

2. **The register mechanism is a design choice.** Several options exist:
   - **Directories** — each collection maps to a register (`kb/notes/` = theoretical, `kb/reference/` = descriptive, `kb/instructions/` = prescriptive). Simple, visible, enforceable by path. Types can be shared across registers — a `note` in a descriptive collection is descriptive; the same type in a theoretical collection is theoretical.
   - **Types** — each document type implies a register (`structured-claim` = theoretical, `spec` = descriptive, `instruction` = prescriptive). Documents of different registers can coexist in one directory. Requires the type system to encode register, adding a responsibility beyond structural contracts.
   - **Traits or metadata** — an explicit `register: theoretical | descriptive | prescriptive` field in frontmatter. Most flexible — any document anywhere can declare its register. But requires discipline and doesn't provide the physical separation that makes conventions enforceable by path.
   - **Convention only** — no formal mechanism; the author picks the right conventions based on what the document does. Lightest-weight, but invisible to tooling and hard to validate.

   Commonplace currently uses directories. The choice should match how the KB is operated — directories work well when collections are already separated; types work well when registers are mixed within directories.

3. **Convention docs are [deploy-time learning](./deploy-time-learning-is-the-missing-middle.md) artifacts** — instructions to agents, early on the [verifiability gradient](./verifiability-gradient.md). They should be iterated from use, not designed to completion upfront.

## Open questions

- How many notes currently in `kb/notes/` are actually descriptive or prescriptive and belong elsewhere? A systematic audit would test the framework and clean up the collection.
- Is the distillation chain (theory → prescription → implementation → description) the only path, or do some descriptions arise independently — system descriptions written before any theory, or operator procedures that don't derive from a principle?
- How robust must a theory's evidence base be? A theory with one supporting observation is fragile. Is there a practical threshold (two systems? three?) or is this a judgment call?
- Does the instruction duality (prescription by content, implementation by role) create maintenance patterns not captured by the current asymmetry table? When an instruction changes, the effect is immediate — unlike changing a description, which merely updates an account.

---

Relevant Notes:

- [Title as claim enables traversal as reasoning](./title-as-claim-enables-traversal-as-reasoning.md) — extends: that note already carves out multi-claim and definitional docs from claim-title conventions; those are documents in the descriptive register getting a different convention because they play a different role in traversal
- [Reach informs KB design](./brainstorming-how-reach-informs-kb-design.md) — qualifies: reach is the quality axis for the theoretical register specifically, not a universal goal; descriptions optimize for economy and prescriptions for precision
- [Deploy-time learning is the missing middle](./deploy-time-learning-is-the-missing-middle.md) — enables: per-register conventions are deploy-time artifacts, to be iterated from use rather than designed upfront
- [The verifiability gradient](./verifiability-gradient.md) — the ladder those deploy-time artifacts sit on
- [First-principles reasoning selects for explanatory reach](./first-principles-reasoning-selects-for-explanatory-reach-over-adaptive-fit.md) — foundation: the reach concept that serves as the quality criterion for the theoretical register
- [Why directories despite their costs](./why-directories-despite-their-costs.md) — extends: the three-register split provides a principled reason for directory-level separation beyond topic grouping
- [Distillation](./definitions/distillation.md) — foundation: the theory → prescription path is a distillation step; the full chain (theory → prescription → implementation → description) shows how registers connect through work
- [Skills derive from methodology through distillation](./skills-derive-from-methodology-through-distillation.md) — exemplifies: methodology → skill is an instance of the theory → prescription distillation path
- [Agent memory needs discoverable, composable, trusted knowledge under bounded context](./agent-memory-needs-discoverable-composable-trusted-knowledge-under-bounded-context.md) — grounds: the three properties apply differently per register; reach is the quality criterion for the theoretical register, economy and precision serve the other two
- [A functioning KB needs a workshop layer](./a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — extends: the library/workshop distinction adds a temporal dimension orthogonal to registers — library documents (all three registers) accumulate value, while workshop documents consume it through lifecycle progression
- [Instructions are typed callables](./instructions-are-typed-callables.md) — extends: the instruction duality (prescriptive content, executable role) is a specific case of treating documents as typed callables; the callable framing captures the operational role axis
