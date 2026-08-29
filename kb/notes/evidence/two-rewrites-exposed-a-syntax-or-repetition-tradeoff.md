---
description: "Evidence from two ASD-STE100-inspired passes over one note: unguarded sentence splitting lost semantic relations, while guarded splitting preserved them by adding 4.9% more words"
type: kb/types/note.md
traits: [title-as-claim]
tags: [document-system, evaluation]
---

# Two rewrites exposed a syntax-or-repetition tradeoff

Two retrospective rewrites of one mature theoretical note reduced the parsing load inside selected sentences, but they did not produce a free simplification. The first pass lost semantic relations that the original syntax carried. The second pass preserved the known relations by restating them, but the note became 4.9% longer. In this case, simpler sentence structure traded syntactic compression for lexical repetition.

## Experiment

The target was `kb/notes/frontloading-spares-execution-context.md`. Two fresh sub-agents rewrote its body with an experimental ASD-STE100-inspired instruction. The first used general meaning-preservation guidance. After independent review exposed its failures, the note was reverted and the instruction gained explicit checks for definitional force, modifier attachment, shared qualifiers, appositive identity, logical connections, and list parallelism. A second agent then rewrote the clean baseline.

| Pass | Preservation constraint | Result | Final word count |
|---|---|---|---:|
| Baseline | Existing prose | Reference artifact | 1,028 |
| First rewrite | Preserve meaning and scope generally | Five attachment or structure failures; reverted | 1,066 after one correction (+3.7%) |
| Second rewrite | Explicitly preserve relations carried by syntax | No recurrence of the known failure classes; retained | 1,078 (+4.9%) |

The first pass moved a temporal qualifier away from the definition it limited, detached an appositive definition, broke list parallelism, narrowed the reach of a shared sufficiency qualifier, and briefly broadened the codification boundary. Some individual sentences became easier to scan, but the rewrite was rejected because those local gains did not justify the semantic errors.

The second pass retained risky complex constructions or restated their relations explicitly. For example, it repeated the refresh sufficiency condition for lineage, timestamp information, and a regeneration instruction rather than relying on one distributed qualifier. This prevented the known attachment failure, but it used more words than both the original and the first rewrite.

The retained artifacts and both run logs are in commit `43a404f0` and `kb/reports/retained/asd-ste100-inspired-rewrite.md`.

## Inference

Sentence syntax was carrying more than presentation. Subordination attached conditions to definitions. Apposition identified one phrase with another. A shared modifier distributed one requirement across a list. Flattening those constructions without replacement reduced local parsing load by deleting semantic relations, not only complexity.

The stricter pass restored the relations in separate sentences or repeated them at each point of use. That made each sentence more locally explicit, but it expanded the note. The experiment therefore exposes a tradeoff for retrospective simplification of mature theoretical prose:

- Keep the compressed syntax, and the reader must parse its attachments.
- Replace the syntax with explicit sentences, and the artifact can require more repetition and context.
- Split without preserving either form, and the artifact silently changes meaning.

This result supports simple writing as a prospective authoring target more strongly than it supports wholesale rewriting of existing notes. Fresh prose can start with direct structure before qualifications accumulate. Mature prose can already have load-bearing syntax, so a later simplification pass must treat grammatical relations as semantic content.

## Limits

- The experiment rewrote one note twice. It does not establish a general effect size.
- Review was qualitative and sequential, not blind.
- Easier scanning was a reviewer judgment. No downstream extraction, comprehension, or application task measured agent performance.
- The size comparison uses words, not model tokens or realized execution context.
- The experiment used an ASD-STE100-inspired instruction, not full ASD-STE100 compliance.
- The second pass avoided the known failure classes. That does not prove that it introduced no other semantic drift.

---

Operationalized into:

- [Rewrite a note with ASD-STE100-inspired language](../../instructions/asd-ste100-inspired-rewrite.md) — the first pass's failures became explicit relation-preservation and verification checks

Relevant Notes:

- [Frontloading spares execution context](../frontloading-spares-execution-context.md) — evidenced-by: the retained second-pass artifact whose rewrite the experiment compares with its tracked baseline
- [Claim notes should use Toulmin-derived sections for structured argument](../claim-notes-should-use-toulmin-derived-sections-for-structured.md) — evidenced-by: independently records that added structure can make mature arguments stiff enough to undo
- [Short composable notes maximize combinatorial discovery](../short-composable-notes-maximize-combinatorial-discovery.md) — grounds: added words reduce the number of notes that can be co-loaded under bounded context
