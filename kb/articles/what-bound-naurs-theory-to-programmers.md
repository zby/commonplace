---
description: "On Naur's own reading of formulated criteria, his argument for binding program theory to humans runs through a premise true of the programs he describes; trained recognizers block that step without showing any composite holds a theory"
type: kb/articles/types/article.md
status: draft
byline: Zbigniew Lukasiak
source_notes:
  - kb/notes/naur-equates-machine-execution-with-formulated-criteria.md
  - kb/notes/design-rationale-must-preserve-unregenerable-decision-premises.md
  - kb/notes/holding-a-program-theory-means-sustaining-coherent-search-under-delayed-feedback.md
  - kb/notes/definitions/discovery-lifecycle.md
  - kb/reference/adr/080-full-passes-hand-claim-changes-back-as-a-pending-revise.md
  - kb/sources/programming-as-theory-building.ingest.md
  - kb/sources/popper-a-realist-view-of-logic-physics-and-history-1966.ingest.md
  - kb/sources/argyris-organizational-learning-and-mis-1977.ingest.md
---

# What bound Naur's theory to programmers

> **Draft.** This article is circulating for comments; its claims, structure, and central thesis may still change. Counterexamples, disputed readings of the sources, and boundary cases are welcome through the repository's issue tracker.

Computer scientist Peter Naur argued in 1985 that the main product of programming is not the program but a theory: the programmer's capacity to map the program onto the world, justify each part, and extend it coherently when a new demand arrives. He also argued that this theory cannot be reduced to the program plus written rules and is therefore bound to human beings. This article accepts the first claim and examines the argument for the second.

Read with *criteria* meaning a rubric a person could state, Naur's argument depends on one premise that was true of the programs he described: a machine judges only by criteria someone has formulated. Trained recognizers made that premise false even on Naur's own examples, faces and tunes. This blocks one step and nothing more. It does not show that any machine holds a program's theory or make the theory writable. Naur's bearer requirements still stand: the holder must understand the world the program addresses, justify the parts, and extend the program coherently. A case from this project's maintenance shows a machine-plus-text composite failing the third requirement.

## Naur's thesis, both halves

Naur's essay *Programming as Theory Building* ([source analysis](../sources/programming-as-theory-building.ingest.md)) defines programming as matching “some significant part and aspect of an activity in the real world to the formal symbol manipulation that can be done by a program running on a computer.” What the programmer builds is a theory in philosopher Gilbert Ryle's sense: not a body of propositions, but a capacity to act and to explain, justify, and answer questions.

Naur gives three signs that someone holds a program's theory. First, the holder can map between the world and the program text, including deciding which affairs matter — a decision that “can only be made by someone who understands the whole world.” Second, the holder can “explain why each part of the program is what it is.” Third, the holder can incorporate a new demand by recognizing its similarity to existing facilities, a similarity “between aspects of the world” that “cannot be reduced to any limited set of criteria or rules.”

The second half of Naur's thesis follows from the third capability. Ryle argues that intelligent behavior cannot consist in following rules because following a rule is itself done well or badly. Adding rules for following rules starts an endless regress. A grasp of similarity stops it, yet the relevant similarities “are not, and cannot be, expressed in terms of criteria, no more than” similarities among faces, tunes, or wines. Naur then makes what he calls “a main claim”: the theory of a program “could not conceivably be expressed, but is inextricably bound to human beings.” A program whose theory-holders have dispersed is dead even while it runs; the death becomes visible when modification demands cannot be answered intelligently.

The evidence Naur gives is strong. In his compiler case, a successor group received “full documentation, including annotated program texts and much additional written design discussion, and also personal advice.” It still proposed extensions the original group saw as “patches that effectively destroyed its power and simplicity,” while the original group could propose simple changes within the existing structure. The supplied package did not carry what the original group had. Naur concludes that a new programmer can acquire an existing theory only by working “in close contact with the programmers who already possess the theory.”

## What a theory is here

The word *theory* carries two senses that must stay separate. Philosopher Karl Popper treats a theory as an objective product that stands outside its producer and has consequences no one holder fully grasps ([source analysis](../sources/popper-a-realist-view-of-logic-physics-and-history-1966.ingest.md)). Later readers can operate on that object: derive consequences, test them, and find where it breaks. Naur places Ryle's theory-as-capacity inside this Popperian frame, then insists that possessing a program's theory is a capacity rather than a text.

In this article, *retained theory* names the stored object. *Holding the theory* names the capacity of whoever uses it. Text alone does not hold a theory, though an interpreter-plus-text composite may.

## Two readings of "formulated", and what the separation blocks

Read closely, Naur's inexpressibility argument targets criteria that can be formulated. The similarity judgment is “entirely outside the reach of what can be determined by rules, since even the criteria on which to judge it cannot be formulated.” Everything below turns on what *formulated* means.

On the first reading, a formulated criterion is a rubric a person could state and apply. On the second, anything that fully determines the judgment counts, including a trained network's architecture, weights, and output threshold.

This article takes the first reading for two reasons in Naur's text. Ryle's regress concerns rules a person could follow, so it applies to articulable rules. Naur also writes of similarities “expressed in terms of criteria” and chooses examples — faces, tunes, wine — whose relevant conditions people struggle to state. The second reading instead makes the claim about any finite determining mechanism, a claim the essay does not argue. On that reading, a trained recognizer remains inside Naur's rule pole and nothing has come apart.

On the first reading, the [basis note for this article](../notes/naur-equates-machine-execution-with-formulated-criteria.md) traces how the essay gets from inexpressibility to “bound to human beings.” Programming matches the world to formal symbol manipulation by a computer. The view Naur rejects pairs “act[ing] like machines, by following rules” with the idea “that the human mind works like a computer.” A program, rule-determination, and formulable criteria occupy one pole; human judgment occupies the other.

The inference is: the criteria for the similarity judgment cannot be formulated; a machine judges only by formulated criteria; therefore no machine makes the judgment; therefore the judgment and its theory are human. The second step is the bridge. Naur does not argue it because he did not need to for the compiler and production-monitoring programs he describes. In those cases, making a machine judge meant writing the criteria.

A face recognizer is formal symbol manipulation by a program, yet it performs a similarity judgment for which no person can state the rubric. On the first reading, this leaves Naur's inexpressibility claim intact but breaks the bridge: formal execution no longer requires a formulated rubric. Learning alone is not the discriminator. A learned decision tree remains an explicit rule set; an opaque recognizer does not yield a human-usable rubric.

A language model judging whether a new demand resembles what a design already provides is formally on the recognizer's side of that line: a machine can produce the judgment without executing a stated rubric. Whether it makes *Naur's* judgment is a separate question. That judgment must be world-directed, reason-responsive, and able to adapt when the purpose changes. A face recognizer does none of those things, so the formal similarity does not settle theory possession.

The result is narrow. Blocking the bridge does not show that any current system holds a program's theory. Naur's compiler case still shows that one rich package of text and advice failed to transfer possession. As the [recovery analysis](../notes/documentation-generates-the-system-rather-than-describing-it.md) explains, such a failure identifies a gap in the tested inputs; it does not prove that no artifact package could transfer more. The open proposition is only that text plus a sufficiently capable interpreter may carry more of the capacity than text alone.

A reader may take Naur's other passages as an independent human binding: theory is the programmer's mental possession, and relevance “can only be made by someone who understands the whole world.” This is a fair rival reading. The article does not treat the words *programmer* or *mental* as proof by species label. In Ryle's sense, possession is defined by what the holder can do, while “someone who understands” specifies a capacity. These passages describe the human bearers Naur discusses. The machine-and-criteria bridge supplies the further premise that makes any machine bearer inconceivable. A reader who treats mental possession itself as necessarily human will therefore reject the article's reading.

On the article's reading, blocking the bridge changes “must the bearer be human?” into “can a composite meet the bearer requirements?” Naur's transfer cases provide three tests. The composite must acquire *this* program's mapping, justification, and modification judgments. Some component must supply the [decision premises the interpreter cannot regenerate](../notes/design-rationale-must-preserve-unregenerable-decision-premises.md): which world affairs matter and why, where the intended scope stops, and which alternatives were rejected. The capacity must also be reliable across occasions, since one coherent extension may be luck.

## A local test case: repair without theory

The claim that an interpreter-plus-text composite may hold a theory was tested, without anyone planning the test, on the note behind this article. It is evidence about one note on one day. The [basis note](../notes/naur-equates-machine-execution-with-formulated-criteria.md) went through two cycles of the project's automated improvement pass, a process that checks and repairs notes against their collection's writing rules. In each cycle, the pass found a real overreach and then [retreated to the nearest defensible claim](../notes/narrowing-bought-to-survive-review-is-paid-for-in-content.md).

The second cycle shows the pattern. The note placed a trained interpreter “outside” Naur's partition, although a language model is formal symbol manipulation on a computer and belongs inside it. The pass replaced that claim with “the inexpressibility argument does not by itself bind program theory to humans.” The first cycle made the same kind of retreat. Both repairs were true, but neither preserved what the note was for: identifying the premise through which the human binding runs. In the second cycle, that purpose was already in the note's title and opening. One sentence from the maintainer restored the missing direction each time.

The pass then assessed each repair against a brief reconstructed after it had defeated the earlier claim and reported that the contribution had been strengthened. In Naur's terms, the pass played the successor group. It had the note, its stated purpose, the review reports, the writing rules, and the checks. Critique did not require the note's theory: counterexamples and grounding defects were visible in those inputs. Repair did. The pass could not modify the claim coherently within the structure the note was for, so the episode fails Naur's third test. The purpose was available but did not guide the repair, which makes this a failure of use rather than simple retrieval.

The project's response was to [stop a full pass when repair would change a claim](../reference/adr/080-full-passes-hand-claim-changes-back-as-a-pending-revise.md) and hand the objection back to whoever holds the theory. The machinery arrived at Naur's own operational conclusion: transfer still needed contact with the theory-holder.

The failure became visible only afterward. Stating the tests in advance would have turned it into a measurement rather than a discovery. This one case supports one operational rule: before claiming that a composite holds a theory, define program-specific acquisition, required decision premises, and a reliability threshold.

## Coherent modification is a search-and-recovery test

Naur's third bearer test should not be read as a demand that the holder deduce a
correct change on its first attempt. Human theory-holders use partial and
fallible theories. They inspect the program, construct alternatives, encounter
conflicts, reverse course, and revise their understanding.

The theory matters because it keeps that search program-specific. It shapes
which candidates are considered, what must be preserved, how failures are
interpreted, when to backtrack, and what recovery should restore or revise. A
failed first candidate can belong to coherent modification when the process
recognizes the failure and recovers. A locally successful candidate can fail the
test when it damages the program's wider organization and the process cannot
detect the damage.

The computational test must therefore cover a sequence of demands and at least
one refuting exposure. It should ask whether withholding or replacing the
project theory changes proposal or recovery, whether consequences not authored
only by the candidate can trigger backtracking, and whether the resulting
revision affects a later modification. The full process-level formulation is
that [holding a program theory means sustaining coherent search under delayed
feedback](../notes/holding-a-program-theory-means-sustaining-coherent-search-under-delayed-feedback.md).

This reframing makes the local failure above more precise. The improvement pass
did not merely choose a bad sentence. It lacked a reliable process for using the
note's project-specific purpose to steer repair, recognize that a defensible
narrowing had destroyed the intended contribution, and recover before claiming
success.

## Where to go next

Separating execution from formulated criteria reopens questions Naur's argument had closed without answering: whether a computational composite can pass his bearer tests, what combination of retained theory, model judgment, symbolic code, and evidence could sustain the result, and how a human-inclusive theory-building tool could progressively move required judgments into its automatic operation. Those questions form a research program; this article establishes the opening, not its success.

For the underlying evidence, the [basis note](../notes/naur-equates-machine-execution-with-formulated-criteria.md) carries the full reading of Naur, the [source analysis](../sources/programming-as-theory-building.ingest.md) retains the passages, and the [design-rationale note](../notes/design-rationale-must-preserve-unregenerable-decision-premises.md) develops the second bearer test. The [decision record](../reference/adr/080-full-passes-hand-claim-changes-back-as-a-pending-revise.md) records the project's response to the repair episode.
