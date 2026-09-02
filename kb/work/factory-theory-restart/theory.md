# The reachability conjecture: train the house, not the LLM

## Claim

**The reachability conjecture.** At least one automated [software
house](../../notes/definitions/software-house.md) capable of open-ended coherent
software change is practically reachable with one or more LLMs available by
2026-09-02.

Reaching it requires no new LLM architecture, further LLM training, or more
capable model. The admitted LLMs remain fixed. The software house is trained
instead, through computationally produced and retained changes to two legible
[representational forms](../../notes/definitions/representational-form.md):
executable software and persistent natural-language notes.

A person may supply the initial software-and-notes seed. Practical reachability
means that, within a declared product scope, operating horizon, and resource
envelope, computational training can discover and maintain the decisive
project-specific structures and eventually remove the need for a human to fill
an internal production or theory-holding role. A description of an ideal
system, or a system that people must keep designing by hand, is not yet the
claimed result.

## Why the substrate could suffice

Open-ended coherent change confronts demands that were not fully pre-analysed
and questions of fit that available checks do not completely decide. Under
those conditions, a software house needs the Naurian program-theory function:
the capacity to relate software to the activity it supports, explain why the
software is organized as it is, and relate a new demand to that organization.
[Holding a program theory means sustaining coherent search under delayed
feedback](../../notes/program-theory-sustains-search-under-delayed-feedback.md),
not merely producing one locally acceptable edit.

Naur treated that function as human because its judgments could not be reduced
to a finite set of formulated criteria. An LLM does not escape formal
computation. The relevant change is that a machine can now apply informal
project-specific state without first translating that state into a complete
symbolic decision procedure. Thus a computational house could satisfy Naur's
functional test without refuting his claim that program theory cannot be fully
expressed as rules. It would refute only his unproved restriction of the
theory-holding function to people. [The distinction is between formal
execution and explicitly formulated
criteria](../../notes/naur-equates-machine-execution-with-formulated-criteria.md).

The conjecture assigns a different role to each component:

- Fixed current LLMs supply the general linguistic, programming, and reasoning
  capacity used to interpret project state and produce candidate changes.
- Natural-language notes supply persistent project-specific state: purposes,
  commitments, explanations, evidence, and prior search that need not reside in
  model weights.
- Executable software supplies exact behavior and continuity: products, tools,
  context assembly, scheduling, checks, rollback, and controlled retention.

No component is the theory-holder by itself. Notes without interpretation are
inert. A fixed LLM without sufficient project state may reconstruct or guess
rather than carry understanding across work. Software can execute a decision
without supplying the semantic judgment that selected it. The working
composite must exhibit the theory-holding capacity.

## Training in legible forms

Legibility describes the trained state, not how easily that state can be
designed. Useful software and notes may have to be found through search,
criticism, trials, production consequences, and retained correction. They can
be computationally acquired artifacts just as model weights can, while
remaining inspectable, executable or interpretable, and directly revisable.

This is compatible with the Bitter Lesson because [the lesson selects how
behavior-shaping structure is produced, not the representational form in which
it is retained](../../notes/the-bitter-lesson-selects-production-methods-not-representational.md).
Computationally learned software and notes therefore do not lose merely because
they remain localized and legible. But a hand-crafted seed is compatible only
if [learning outgrows the task-specific knowledge supplied by that
seed](../../notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md).
These points answer the categorical objection; they do not establish that
training over legible structures will scale. Demonstrating that practical path
remains the program's burden.

Current LLMs can produce both forms. Software can govern whether proposed or
direct changes become operative and can bring later consequences back into the
next update. The conjectured training path is therefore:

```text
production evidence + fixed LLMs + present software and notes
  -> computational update of software and/or notes
  -> retained successor software and notes
  -> later production
```

The update mechanism is not fixed. It may directly produce a successor or may
separate proposal, evaluation, and selection. Likewise, acquiring a successor
theory may edit prior theory-bearing state, discard it and build again from the
available evidence, or combine both. Revision names the change in what the
house comes to hold, not an incremental editing requirement.

This is training of the software house, not absence of training. A transition
counts as learning only when experience causes a retained change that affects
later behavior. Merely writing a note or changing code does not establish that
claim.

Hand-crafted tools, stores, interfaces, safety boundaries, and provisional
notes may initialize the loop. They are seed engineering, not evidence that
the house acquired the structures computationally. The training path must
outgrow repeated human authorship of the decisive project-specific theory and
machinery. A wholly hand-built endpoint could support the representational
sufficiency claim, but not the practical training-path claim.

## The reverse derivation: a general theory builder becomes a software house

The argument also runs from theory building back to software production.
Consider a persistent automated system that builds, tests, and revises
natural-language theories for external users across domains not fixed in
advance. A one-shot generator or a prover confined to one predeclared formal
language is not the subject of this derivation.

At present, an LLM is the only generally available computational interpreter
for semantic operations over theories of that breadth. But an LLM alone is not
the complete builder. A long-lived theory corpus must be stored, organized,
selected into bounded contexts, connected to evidence, revised, and carried
across calls. Exact state transitions, scheduling, tool execution, checks, and
rollback also need software outside model interpretation. [Code complements
the weight–prompt pair with independently executed symbolic
operations](../../notes/code-complements-weight-prompt-with-symbolic-operations.md),
and [symbolic scheduling avoids using an LLM for unreliable
bookkeeping](../../notes/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md).

The next link is a conjecture. Open-ended theory domains bring not only new
theory content but new manipulation requirements: ways to organize a theory,
select evidence, construct contexts, test consequences, and coordinate tools.
The conjecture is that no fixed harness can anticipate that entire demand
space. If it holds, a general builder must acquire and revise the software that
supports its theory work as those demands arise.

If another required producer repeatedly supplies those decisive,
demand-specific software changes, that producer fills an internal role in the
complete theory-building system; excluding it would make the claimed automation
boundary too narrow. This does not pull suppliers of fixed general dependencies
inside the boundary. An automated builder must bring the demand-specific role
inside. It then persistently develops and evolves software in response to its
users and operating consequences and is, by the
[definition](../../notes/definitions/software-house.md), a software house.

The two directions converge. Starting from open-ended automated software
production without a human supplying the required project theory leads to a
theory builder for the house's own domain. Starting from open-ended automated
theory building leads to a software house that produces and changes its own
supporting machinery. The program's target is the coupled system that meets
both descriptions. This convergence explains why self-application is a
necessary destination rather than an optional extension of the reachability
claim.

## Obligations of a constructive witness

One construction must eventually demonstrate the whole progression:

1. **Holding and application.** Given adequate project-specific state, the
   composite uses a program theory across novel changes rather than merely
   storing or paraphrasing it.
2. **Initial acquisition.** From permitted records, interaction, and
   participation in the work, it builds an adequate theory instead of receiving
   the decisive theory from a human.
3. **Successor acquisition.** When experience exposes an inadequacy, it comes
   to hold an adequate successor theory, whether by editing, reconstruction, or
   a mixed process.
4. **Self-application.** It builds and uses theories of its own production
   machinery when changing that machinery under the same open-ended
   conditions.
5. **Automated continuation.** It sustains these capacities across the declared
   scope and horizon without a required human internal role. External users may
   still provide requirements, feedback, domain knowledge, and acceptance
   judgments.

Computational training of the legible state is a condition across acquisition,
successor acquisition, and self-application, not an additional stage. Meeting
an early obligation is progress toward the witness, not a weaker definition of
the target.

## Boundaries and epistemic status

The conjecture is existential. It does not say that every current LLM, every
arrangement of software and notes, or every product scope will work. The
admitted model versions must be pinned before testing so that a later model
cannot silently rescue the claim. Software and notes delimit the house's
trainable internal state; they do not exclude products, user demands, tool
outputs, or operating consequences from its work and evidence.

The software-house definition itself requires none of holding, acquisition,
training, learning, self-application, or automation. Those are properties of
the target constructed by this program. Open-ended also does not mean
literally unlimited: the declared demand stream must admit relevant novelty
rather than enumerate every case in advance.

The need for a program-theory function is a theoretical argument, not a proved
theorem. Current-LLM sufficiency and the practical training path are
conjectures. So is the reverse derivation's claim that open-ended theory
manipulation eventually exceeds every fixed harness. A fixed harness that
sustained a general theory builder across genuinely new domains would break
that reverse chain without refuting the forward program-theory argument.
The claim that LLMs are presently the only generally available interpreters
for theories of this breadth is a time-indexed engineering premise, not a
logical necessity.

The program is constructive: a working system can establish reachability over
its declared scope, horizon, and resource envelope. Failure of one architecture
establishes only that the attempted path failed; it cannot refute the
existential claim unless the search has first been bounded.
