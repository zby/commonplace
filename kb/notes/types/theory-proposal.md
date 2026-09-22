---
type: kb/types/type-spec.md
name: theory-proposal
description: Finished theory the KB has not decided to import into its vocabulary — the terms and distinctions adoption would add, the definitions it would change, its trigger, and its cost
schema: ./theory-proposal.schema.yaml
---

# Theory proposal

## Authoring Instructions

Use a theory proposal for finished theory the KB has not decided to import: a framework, a distinction, new terms, or a change to an adopted definition. A proposal exists because adoption is undecided, not because its content is doubtful; much of it may be careful, or standard elsewhere. The undecided question is whether the KB wants to carry the distinctions, since every adopted term has to be maintained, used consistently, and loaded by every reader. A conjecture that needs no new vocabulary is not a theory proposal; it is an ordinary note that states its conjectural force. An unadopted design for the Commonplace system is a [design proposal](../../reference/types/design-proposal.md). Where theory proposals may live, and how other notes may point to them, is stated in [`kb/notes/COLLECTION.md`](../COLLECTION.md) ([ADR 084](../../reference/adr/084-kind-rules-live-in-type-specs-and-operations-in-instructions.md)).

- **Finished.** The proposal reads on its own, without the conversation or workshop that produced it. Material still being worked out stays in `kb/work/`.
- **Labelled.** The description begins with "Proposal:".
- **Opens with the import.** The opening states what adoption would add (which terms and distinctions) and what it would change (which definitions, notes, and articles).
- **Names its trigger and cost.** State what need would justify importing it, such as a note or an experiment that cannot state its claim without the distinction, and what adopting it would commit the KB to.
- **Untagged.** Proposals stay out of the tag indexes; the directory listing is their index.
- **Title.** A proposal holding one claim takes a claim title; one holding a framework of several claims may take a topic title.

Everything else follows the `kb/notes/` collection contract and the base [note](../../types/note.md) type, including its traits.

## Frontmatter

| Field | Required | Use |
|---|---:|---|
| `description` | Yes | Begins with `Proposal:`. |
| `type` | Yes | `../types/theory-proposal.md`, file-relative from `kb/notes/proposals/`. |
| `tags` | No | Must be empty or absent. |
| `traits` | No | Review-routing traits, as for `note`. |

The schema enforces the `Proposal` lead and the empty tags; the other clauses are checked by type-conformance review.

## Lifecycle

| State | What must hold | Enters by |
|---|---|---|
| **Live** (`kb/notes/proposals/`) | Every clause above; nothing in it has been adopted. | Promotion from a workshop, or a new proposal written directly |
| **Partially adopted** (still live) | The adopted part has moved out: terms are definition notes under `kb/notes/definitions/` and, when they are everyday vocabulary, entries in the `AGENTS.md` vocabulary; claims are ordinary notes; the affected definitions, notes, and articles are edited. The adopted part is removed from the proposal. | No dedicated instruction yet; the adoption commit carries the change |
| **Deleted** | Nothing undecided is left, or its trigger has clearly failed to arrive. Git keeps the text. | [Retire an artifact](../../instructions/retire-artifact.md) |

**Retirement destination: delete.**
