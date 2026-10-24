---
type: types/type-spec.md
name: conjecture
description: A stated, refutable conjecture retained without support — its problem, the reach it claims, its refuters, the missing piece that would make it consequential, and a trigger for finding that piece
schema: ./conjecture.schema.yaml
---

# Conjecture

A conjecture is a tentative solution to a stated problem, retained because
it is refutable, not because it is supported. Use this type for any claim
worth keeping that has not earned a theory note: a candidate connection
between distant notes, a rival to an existing theory, a unification that
would explain several notes if true, a hypothesis a later episode might
witness. A conjecture that already has independent witnesses and survived
criticism is a theory note, not a conjecture. Finished theory awaiting
vocabulary adoption is a [theory proposal](../../theory/types/theory-proposal.md).
A first observation with no claim yet is a log entry.

The store this type lives in is primary state and holds theory conjectures
and design conjectures alike. The theory collection and the current design
are projections from it at a stated threshold, sorted by each conjecture's
declared bindings; the levels are computed from the record fields below and
are never stored
([migration plan](./README.md#threshold-vocabulary-decided-at-stage-0)).

## Content contract

- **Title as claim.** The title is a proposition that can be true or false
  and carries the `title-as-claim` trait.
- **Labelled.** The description begins with "Conjecture:" so scoped title
  and description scans show the status.
- **Opens with the claim and its force.** The first paragraph states the
  claim and says that it is a conjecture; it may say how it arose.
- **Names its problem.** `problem` is one sentence stating the problem the
  conjecture tries to solve, repeated verbatim on every rival conjecture to
  the same problem. `## Problem` says why the problem is open. Restating a
  problem edits `problem` on every rival in one commit; Git keeps the old
  sentence.
- **States its reach.** `## Reach` states what the conjecture would unify,
  constrain or newly distinguish if true, the scope it claims, and, for a
  causal claim, the rung it is made at (association, intervention,
  counterfactual). Reach is claimed, not earned
  ([derivation and inheritance give starting warrant](../../theory/derivation-and-inheritance-give-starting-warrant-earns-scope.md)).
- **Names its refuters.** `refuters` lists at least one observation,
  artifact or test outcome that would count against the claim. A refuter is
  something a later reader could meet; "no evidence appears" is not one.
- **Names the missing piece.** `missing` states the kind of evidence, note
  or bridge term that would make the conjecture consequential: the second
  witness, the instance, the discriminating test.
- **Carries a trigger.** `trigger` lists one or more search patterns or
  claim schemas that a new artifact matching the missing piece would match.
  Writers and connect run open triggers against new artifacts.
- **Declares its bindings.** `choices` lists the Commonplace choices the
  conjecture takes as given, each named by ADR or by the artifact that fixed
  it. A choice backed by theory points to that theory in `because`; a choice
  without one is a bare choice, a free variable of the argument. An empty
  list means the conjecture claims to hold for any system: it is a theory
  conjecture. A non-empty list means it is a design conjecture, and its
  theory content is whatever survives when the bound choices are quantified
  out. The store does not sort by this; the projection does.
- **Keeps its record.** `witnesses` and `criticism` are dated lists. A
  witness is an artifact, episode or test outcome that bears on the claim,
  with its source so independence can be judged: witnesses that share a
  dataset, method, author, citation lineage, or for agents a model family
  and prompt, count as one. A criticism entry records who criticized, with
  what verdict, and where. The record is appended, never rewritten.
- **Never a premise.** No other artifact cites a conjecture as a premise or
  uses its terms as settled vocabulary. Pointing to it is allowed.
- **Untagged.** Conjectures stay out of tag heads; the directory listing and
  triggers are their index.
- **Rivals are visible.** When another conjecture answers the same problem,
  `rivals` lists it, and `## Rivals` says on what the two disagree and what
  would decide between them.

## Frontmatter

| Field | Required | Use |
|---|---:|---|
| `description` | Yes | Begins with `Conjecture:`. |
| `type` | Yes | `conjectures/types/conjecture.md` once the collection exists. |
| `traits` | Yes | Includes `title-as-claim`. |
| `problem` | Yes | One sentence, verbatim across rivals. |
| `refuters` | Yes | At least one; each a short statement of what would count against the claim. |
| `missing` | Yes | The evidence, note or bridge term that would make the conjecture consequential. |
| `trigger` | Yes | At least one `rg` pattern or claim schema a matching artifact would satisfy. |
| `witnesses` | No | Dated list: `{date, source, note}`. |
| `criticism` | No | Dated list: `{date, by, verdict, note}`; verdict is `survived` or `refuter-met`. |
| `rivals` | No | Paths of other conjectures with the same `problem`. |
| `choices` | Yes | List, possibly empty, of `{choice, because}`; `because` is a theory path or absent for a bare choice. |
| `tags` | No | Must be empty or absent. |

The schema enforces the label, the trait, the required fields, the empty
tags, and the `## Problem` and `## Reach` headings. The clauses about
refuters being meetable, triggers matching the missing piece, rivals
sharing the problem verbatim, and `choices` naming every Commonplace choice
the argument leans on are checked by type-conformance review. Warrant gates
do not run on this type.

## Lifecycle

| State | Location | What must hold | Enters by |
|---|---|---|---|
| **Stated** | `kb/conjectures/` | Every clause above. | Writing, seeding from the log or connect reports, or a discovery sampler. |
| **Refuted** | `kb/conjectures/refuted/` | A `criticism` entry with verdict `refuter-met` names the refuter. Retained because rivals guide discriminating experiments. | Relocation in its own commit. |
| **Moot** | `kb/conjectures/moot/` | A choice in `choices` was revised or superseded, so the bindings no longer match the live system. Not a refutation: the theory content, if any, may be restated with empty `choices`. | Relocation in its own commit. |
| **Promoted** | `kb/theory/` when `choices` is empty | The computed level is `corroborated`. The file moves with its record and is then edited to meet the theory contract; the projection selects, it does not rewrite. A design conjecture is not moved: an ADR that adopts it cites it and it stays in the store. Its theory content promotes separately, as its own unbound conjecture, once the bound choices are quantified out and the generalization is argued. | Relocation in its own commit. |
| **Merged** | deleted | Two records answered the same problem with one claim. The survivor's text names the absorbed claim; the absorbed `witnesses` and `criticism` entries are appended to the survivor with their original dates. Nothing is rewritten. | Edit of the survivor and deletion of the absorbed file in one commit. |
| **Expired** | deleted | No witness and no criticism after a stated number of trigger sweeps. Git keeps the text. | [Retire an artifact](../../instructions/retire-artifact.md). |

**Retirement destination: delete.** Refutation and mootness are not retirement.

## Template

```markdown
---
description: "Conjecture: {one sentence a reader can route on}"
type: conjectures/types/conjecture.md
traits: [title-as-claim]
problem: "{One sentence; verbatim on every rival}"
refuters:
  - "{An observation or artifact that would count against the claim}"
missing: "{What would make this consequential}"
trigger:
  - "{rg pattern or claim schema}"
witnesses: []
criticism: []
rivals: []
choices: []
# or, for a design conjecture:
# choices:
#   - choice: "ADR 025 — complete listings are never committed"
#     because: "kb/theory/stale-indexes-are-worse-than-no-indexes.md"
#   - choice: "one heartbeat, not one cron entry per task"
---

# {Claim as title}

{The claim, stated as a conjecture, and how it arose.}

## Problem

{Why the problem is open and what an answer would change.}

## Reach

{What the conjecture would unify, constrain or distinguish; claimed scope;
rung for a causal claim.}

## Rivals

{Optional: what rivals disagree on and what would decide between them.}
```

---

Relevant Notes:

- [Tentative theory](../../theory/definitions/tentative-theory.md) — rests-on: every retained conjecture has this status; the type adds the record, not the status
- [Candidacy evidence licenses escalation, not acceptance](../../theory/candidacy-evidence-licenses-escalation-not-acceptance.md) — rests-on: triggers and witnesses route a conjecture to criticism; they never accept it
- [Theory proposal](../../theory/types/theory-proposal.md) — contrasts: finished theory awaiting vocabulary adoption, with the same no-premise rule
- [Content routing](../../reference/content-routing.md) — see-also: where a first observation goes before it is a conjecture
