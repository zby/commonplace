# Sixth episode: a premise defeated by equivocation on the note's own term

**Note:** `kb/notes/unformalized-improvements-need-a-pre-formal-stage-in-the-loop.md`.
**Pass:** `20260826T154716Z-3fa27b`, started 17:47 CEST on the old procedure, its step-7 reframe decided before the bite rule landed at 18:53 (`0818173f`) and 18:59 (`4cda3808`). Disposition `keep (reframe)`; four premises `DEFEATED — GLOBAL`.
**Record:** [`sixth-episode-record/`](./sixth-episode-record/README.md) holds the packet, the pass-start note, and the initial and closing critique/friction/premise reports.
**Outcome:** the reframe was rejected, the thesis restored with a sharpened antecedent, and one clause added to the bite rule.

## What the pass did

The note claimed that an improvement "whose concepts are not yet fixed enough to formalize is reachable only if some stage can criticize, revise, and reject it before it has a formal representation," and named Commonplace's arrangement a relaxed Gödel machine. The pass retitled it to *Formal-only gates have distinct admission and warrant limits*, dropped the name, demoted the pre-formal stage to "one placement of revision," and recorded the contribution as *preserved*. The reframe was licensed by four GLOBAL defeats from the premise gate.

## The defeats

All four have one shape:

| Premise attacked | Counterexample | Where the concept already lives |
|---|---|---|
| reachability needs a pre-formal component | a generator enumerates formal scheduler models from a grammar that permits capacity to depend on any observed load signal; a trace oracle keeps the one where another process's load predicts failures | in the grammar |
| concept boundaries must stabilize before any formal representation | Angluin's L\* learner proposes automata and splits states on counterexamples until the partition stabilizes | in the automaton class |
| translation must instantiate a rejection-capable pre-formal stage | a translator emits the disjunction `fixed_capacity | time_varying | depends_on_other_load` and a checker prunes it | in the disjunction |
| cheap formalization can never eliminate the pre-formal interval | active automata learning settles the state concepts through already-formal conjectures | in the automaton class |

In every case the concept has an expression in the loop's admitted formal language; what is unsettled is which formal candidate is right. The note's antecedent was a concept with *no* expression in any admitted language. The counterexamples meet the antecedent only under the broader reading "not yet selected among formal candidates," and the note's own second Open Question had named that boundary. The pre-formal work in each case was done by whoever designed the grammar, chose the automaton class, or wrote the disjunction — outside the loop as the counterexample draws it, which is [learning inside a fixed decomposition](../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) restated, not a refutation.

The pass came close to seeing this twice. The closing critique noted that the note "still blurs a larger-loop candidate with a candidate directly evaluable by the gate." The friction gate's UNSUPPORTED joint on "translation involves interpretive choice, therefore a rejection-capable stage" was a real thin spot — the inference was under-argued. Neither reading undid the defeats, because the gate had already recorded them as facts about the note.

## Why the bite rule would not have caught it

The rule adopted at 18:53 blocks reframes on `DOUBTFUL` premises and on critiques that merely "partially land," which is exactly what the Naur note's third pass did. Here the premises were `DEFEATED`, so the rule would have classified the objection as *bites* and licensed the reframe. The gap is upstream of the classification: a `DEFEATED` verdict is trusted as a fact, but whether the counterexample satisfies the antecedent depends on what the note *means* by its key term, and that meaning was the note's theory, not a definition the gate could read. This is the fifth episode's mechanism moved one gate earlier — the premise checker is group B too.

## The repair

Two edits, both on the record in the same commit as this file:

1. **The note.** The thesis is kept and the antecedent sharpened: a concept with no expression in the loop's admitted formal language, as distinct from one the language contains but the loop has not yet selected; the stage may sit inside the loop or at design time in the choice of language, in which case reach is fixed there. The reframe's genuine gains are carried over — the two translation forms (one surrogate versus a preserved family, with the family's composition named as the relocated pre-formal decision), parameter-versus-concept change as model-relative, DiscoverPhysics narrowed to its retained ingest, glosses for the linked terms.
2. **The instruction.** One clause in the bite paragraph: a `DEFEATED` premise bites only if its counterexample meets the premise's antecedent under the note's own definitions; a counterexample that meets it only under a broader reading of a key term is *answerable* — repaired by sharpening the antecedent at the point of attack — and does not license a reframe. Record which passage fixes the term's meaning; if none does, the missing definition is the answerable finding.

The second edit is a guard on the gate's input rather than on the repair, and it is the first time in this series that a defeat itself, not a doubtful or partial finding, was ruled out as reframe warrant. Whether it over-blocks — every defeated universal can be recast as "you read my term too broadly" — is the thing the next passes will show. The guard asks for the passage that fixes the meaning, so a note that never defined its term cannot use it.

## What this adds

Episodes one to four are about which narrowings of a defeated claim are honest; the fifth is about who can repair at all. This one shows the gate producing a false defeat, and the pattern is the same as the repair failure: the gate reads the text and its own counterexample, and the term's meaning sat in neither. Sharpening the antecedent — writing the definition the note had only in its author's head — is the repair Naur would predict and the one the bite rule now routes to.
