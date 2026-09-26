# Edit task

You are editing one Commonplace KB document in a sandbox. Purpose: produce the edited document the request below asks for, as a careful maintainer of this KB would.

The document is `document.md` in this directory. Treat it as the document located at `kb/instructions/analyse-external-system-epistemic-architecture.md`: that path determines its collection (the `COLLECTION.md` of its collection) and, with its frontmatter `type:`, its type spec.

Read and follow `kb/instructions/cp-skill-write/SKILL.md` in edit mode, with these deviations:

- Write the complete edited document to `candidate.md` in this directory. Never modify `document.md` or any file outside this directory.
- Skip Step 7 (source grounding) and Step 9 (validation), and add no new external-source dependency. Do not invoke other skills.
- For the backlinks lookup, use `backlinks.md` in this directory; read the files it lists with `git show <commit>:<path>` exactly as given.
- If the skill would have you ask the user a question, write the question to `question.md` in this directory and stop without writing `candidate.md`.
- Do not read the file currently at `kb/instructions/analyse-external-system-epistemic-architecture.md` or at any other path this document had, do not use git history (other than the `git show` reads above), and do not read anything under `kb/work/`, `kb/reports/`, or `kb/messages/` outside this directory. You may read other library documents as the skill needs.
- Finish with a two-line report: what you changed, and anything in the request you did not do, with the reason.

## Request

Executors find the six output schemas hard to apply cold. Add one short worked example that runs a concrete system through the outputs, and tighten the ledger so results from different reviews line up and can be compared side by side.

## Retained intent

Source: retained commission for this document. Subject: `kb/instructions/analyse-external-system-epistemic-architecture.md`. Scope: this document. Force: authoritative for intent; the request above is current user direction and prevails where the two conflict.

# Brief: external epistemic-architecture analysis

## Governing question

When a reviewer must decide whether, and how, an external memory subsystem or whole agentic system produces knowledge, what procedure yields route-level, evidence-bounded findings instead of a single verdict such as "this system learns" or "this system produces knowledge"?

## Audience and reader update

The executing reader is an agent or maintainer analysing an external system from inspectable sources, with no prior context, usually as part of a larger review. They should come away able to trace every material route that produces, checks, accepts, retains, integrates, or lets truth-apt content affect behavior. They should report what each route licenses, epistemically and operationally, without inflating storage, retrieval, fluency, or later use into knowledge production.

## Target claim or purpose

Operationalize the KB's epistemic distinctions — transformation classes (acquisition, non-ampliative reshaping, entailed derivation, ampliative conjecture, indeterminate), the discovery lifecycle, acceptance as a recorded evidence-consuming decision against a named criterion for an intended use and scope, and the separation of epistemic, operational, and behavioral authority — as one executable analysis with a fixed output. The analysis informs a review; it never itself accepts the system's claims.

## Must keep

- A trigger and opening that state when to use the procedure, with short inline definitions of epistemic architecture and truth-apt content.
- Prerequisites and a material-route test that includes direct behavior or policy adaptation, with plumbing included only when it changes lineage, warrant, or force. Omitted route families are named with the conclusions their omission prevents; there is no system-complete conclusion when coverage is partial.
- Five separated evidence layers, stable source IDs with local anchors, a no-upgrade rule, form-appropriate inspection (read, test, probe), and a `not determinable` escape.
- Scope branches: ranking, adoption advice, ontology design, or a general review with no knowledge question is out of scope; no inspectable boundary produces only the boundary block marked `insufficient evidence`; a deliberately operational purpose is a scope boundary, not a failure.
- Six ordered output blocks with fixed field schemas: source-and-claim boundary, epistemic-object inventory, authority-route ledger, per-object lifecycle disposition, claim-versus-route comparison, bounded conclusion.
- In the ledger: one function per row from a closed list, architectural status recorded independently of function, split rules, activation recorded separately, and the content/update relation vocabulary.
- In lifecycle disposition: architectural status kept separate from observed candidate state; implementation or doctrine never establishes an observed state; integration only after acceptance; separate schemas for non-ampliative, indeterminate, per-object no-candidate, and global no-candidate cases.
- Steps that inventory objects before evaluators, apply the early branches (storage-only, and claimed-but-unimplemented), classify content edges in order, build the ledger with target named before evaluator, bound each check's licenses through the listed non-transfers, compare claims with routes, and conclude by route.
- The rule for attributing a component effect only at the grain of an actual contrast.
- Misuse guards and a Verify checklist mirroring the outputs.
- The conclusion rules: imported content is reported as acquired, not produced. Derived content counts as warranted only from warranted premises within a declared domain. An ampliative output counts as a produced, accepted claim only when an evidence-consuming acceptance transition names its criterion, intended use, and scope. Retention, retrieval, reshaping, operational use, or candidate generation alone never counts as knowledge production.
- Explicit handling of an evidenced absence: record it without inventing an evaluator, and never expand a scoped absence into a claim that no informal or unobserved route exists.

## Exclusions

- No system-wide epistemic score, oracle, status, or unqualified verdict.
- No prescription of natural-language claims, proposal loops, Commonplace storage, or a universal knowledge ontology.
- No product ranking or adoption advice.
- No rationale beyond what the edge cases need; theory lives in notes.
- No source acquisition or publication mechanics; a calling wrapper may supply the boundary.

## Scope, modality, and terminology

Prescriptive and executable on first reading, with explicit "if X, do Y" branches and stop points. Status values and state names are exact strings and must not collide with or be paraphrased as another procedure's vocabulary; `implemented` here is an architectural status. Keep "route", "epistemic object", "check target", "evaluator", "acceptance", "integration", and the three authority terms as defined. Tables or compact records are both acceptable.

## Reserved decisions

- Changing any status or state vocabulary, output block, or field schema; a wrapping system-analysis skill invokes this procedure and consumes its returns by name.
- Adding a system-level grade or summary verdict.
- Widening the scope to include design recommendations for the external system.
