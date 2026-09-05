# Workshop: operator-led article clarification

Goal: turn one observed way of improving a draft article into a reusable
procedure, once enough examples exist to say what the procedure is.

Posed by the operator on 2026-09-05, after one session on
`kb/articles/automated-software-houses-with-fixed-llms.md` produced nineteen
small commits by this method. The operator asked for the approach to be
recorded for reuse "after we have more examples and process them into a
coherent procedure". This is a record-and-accumulate workshop, not an
execution plan.

## The approach as observed

The loop has two phases and the operator drives the first.

**Phase 1: operator-flagged passages.** The operator reads the article and
quotes one passage at a time with a short verdict: "hard to read", "I don't
understand this", "the transition is not clear", or a substantive objection
("the conjecture should not be about reachability"). The agent does not fix
the passage first. It names the *kind* of difficulty, proposes a rewrite, and
waits. The operator often corrects the frame before the rewrite lands (for
example, "Naur makes two claims" replaced the agent's "two objections"), and
that correction is usually the most valuable step. Each accepted rewrite is
its own commit, so any one can be reverted alone.

**Phase 2: agent sweep by pattern.** After several flagged passages, the
operator asks the agent to take the accepted edits as examples and find
similar opportunities in the rest of the article. The agent lists candidates
in article order, ranked, each with the pattern it matches and a proposed
rewrite, and applies them on approval, still one commit each.

The division of labour matters: the operator supplies the judgment that a
passage fails a reader and the conceptual frame; the agent supplies the
diagnosis of *why* it fails, which is what makes the sweep possible.

## Working taxonomy of difficulties

Each kind is named by what the reader is missing. Examples are commits on
`kb/articles/automated-software-houses-with-fixed-llms.md` unless stated.

| Kind | What the reader is missing | Typical fix | Examples |
|---|---|---|---|
| Vestigial framing | The word belongs to an earlier version of the argument; the content moved but the term stayed | Rename the concept and rethread every consumer; relocate files last | `298295d2` reachability to operability; `98e8ea3f`, `5c9bc227` supplements |
| Defensive definition | A definition written to fend off adversarial readings has gone vacuous or invites a degenerate reading | State the working standard plainly and accept an informal term | `4d5bf80d` open-ended, with "reasonable" left informal and a comparative baseline |
| Lost claim after restructure | Concurrent or mechanical edits removed the sentence that carried the main claim | Restore the claim first in the passage | `9f864870` TL;DR |
| Unlabelled example or parallel | A concrete case is mapped onto an abstract mechanism without saying it is an example, or which part maps to which | Announce the example; map each part | `383244f8` tenant commitments; `41920fc4` human-written axioms as the seed parallel |
| Unintroduced term | A word appears once, carrying a technical meaning the article never set up | Introduce it through the sentence that uses it, or through the example that explains it | `383244f8` "search for a design"; `82a6c51e` equivalent reconstruction; `bad358db` trial-specific |
| Unsignposted roles | Adjacent paragraphs do different jobs and nothing says which | One lead-in naming the roles; a topic sentence per paragraph | `c65e2933`, `b06e616b` Naur's thesis and its evidence; `485156d0` components |
| Verdict without its why | A sentence states a conclusion ("leaves untouched", "depends on the rest of the evaluation") that compresses a reason the reader cannot reconstruct | Spell the reason out, one idea per sentence | `5fbf07d7` what a house refutes in Naur; `d12e15e9` pinning; `b108973f` the two limits of an intervention |
| Compressed description | A phrase stands in for an ordinary-language description ("expose an assumption after intervening changes", "unlisted parameter variations") | Say it in the words the reader would use | `f462b3d8` |
| Missing baseline | A standard is named ("useful success") after the article has defined the real standard elsewhere | Name the baseline wherever the standard is invoked; use one term for it | `3f3fa5f7` human-agent house |

Two of these are not readability kinds. Vestigial framing and lost claim are
conceptual drift after a restructure, and the operator caught both by
reading the article as a whole rather than sentence by sentence. Keep them in
the table because the same session finds both, and a procedure that only
looks at sentences will miss them.

## Why this workshop is an instance of the conjecture's own learning

The operator's reading, 2026-09-05: this workshop is exactly the learning
mechanism the [training
article](../../articles/the-software-house-as-the-unit-of-training.md)
proposes. Fixed model weights cannot supply this kind of fine-tuning of
texts, because what counts as a good fix is specific to this KB's texts: its
conventions, its terms, its readers, and one author's judgment of when a
passage fails. The knowledge has to be gathered as a corpus of examples and
rules that apply to these texts, retained in notes, and applied by a fixed
model at the next edit. That is learning in retained natural-language state
around a pinned model, and this workshop is the corpus at its first
observation.

Two consequences for the theory, both open:

- **Theories may need to carry exemplars, not only rules.** The training
  article defines an explicit project theory as design commitments, causal
  assumptions, and invariants. The taxonomy above carries its meaning mostly
  through the commit examples in its last column; the rule text alone
  ("verdict without its why") would not let a fresh session recognize a case.
  If that holds up, the theory's carrier needs a slot for worked examples.
  The KB already uses *prototype* for something else (a theory's [revision
  cost standing](../../notes/prototype-standing-is-revision-cost-binding-plus-lost-investment.md)),
  so call these *exemplars* until a term is settled. Disposition
  (operator, 2026-09-05): do not change the training article. Exemplars sit
  closer to its raw-record treatment than to its theory treatment, so folding
  them into the definition would blur the contrast the component experiment
  isolates. If the effect holds over the next two article runs, propose a
  fifth treatment, theory with exemplars, and let the experiment decide
  whether they belong in the theory.
- **The rules have instance-level warrant only.** Each row was abstracted
  from edits the operator accepted, and [an accepted edit verifies the change,
  not the rule](../../notes/an-accepted-edit-verifies-the-change-not-the-rule.md).
  The closing condition below (two more article runs) is the re-verification
  that would give a row rule-level standing; a row that fires wrongly on a
  later article is the refutation.

## What is not yet known

- Whether the taxonomy is stable across articles, or specific to one author
  and one draft series. One article is one example.
- Whether phase 2 can run without phase 1. The sweep worked because the
  accepted rewrites fixed the operator's taste; a sweep from the taxonomy
  alone may produce edits the operator would not accept.
- How this relates to the existing prose instructions:
  [edit-with-churchill-and-zinsser](../../instructions/edit-with-churchill-and-zinsser.md)
  aims at shorter and more direct prose; several fixes here made passages
  longer. [critique-note](../../instructions/critique-note.md) attacks the
  claim, not its legibility. Neither covers unsignposted roles or verdicts
  without their why, which were the most common kinds here.
- Whether operator verdicts should be recorded verbatim in commit messages.
  Today's messages record the diagnosis, not the operator's words.
  If the rows are exemplar-carried, the operator's verdict is part of the
  exemplar and the commit is the cheapest place to keep it.

## What would close this workshop

Examples from at least two more articles, each run through both phases, with
the taxonomy revised against them. Then either a procedure under
`kb/instructions/` (a report-only pass that lists candidates by kind, leaving
application to the operator), or a finding that the method does not
generalize and a note saying why. The taxonomy rows that survive become the
procedure's checklist; rows that appear once are dropped.

## Bookkeeping

- Add each new article run as a section below with its commit range and any
  new or retired taxonomy rows.
- Commit references above are on `main` of this repository.

## Runs

### 2026-09-05: the automated software house conjecture

`kb/articles/automated-software-houses-with-fixed-llms.md`, commits
`298295d2` through `3f3fa5f7` (nineteen, one unrelated landscape commit
interleaved). Phase 1 covered the claim, the TL;DR, the open-ended
definition, the mechanism paragraph, and the Naur section. Phase 2 produced
eight candidates, all applied. Side effects: the software-house definition
note lost its declared-scope clause (`08215a3d`), and one supplement was
renamed.
