---
description: "A build failure illustrates three tests of what a theory adds to a working patch: can a diagnosis guide search, can one premise be repaired, and does carrying the account to the next job save observations or effort?"
type: articles/types/article.md
status: draft
byline: Zbigniew Lukasiak
source_notes:
  - kb/theory/commonplace-builds-a-theory-builder-and-tests-whether-it-learns.md
  - kb/theory/definitions/theory-builder.md
  - kb/theory/definitions/addressable-theory.md
  - kb/theory/revision-guided-by-rationale-needs-faithfulness-not-just-legibility.md
  - kb/theory/retained-theories-may-improve-sample-efficiency.md
---

# What Does a Learning System Gain by Retaining a Theory Rather Than Just the Fix?

> **Draft.** The claims and structure of this article may change. Comments
> and counterexamples are welcome on
> [the repository's GitHub Discussions page](https://github.com/zby/commonplace/discussions).

A deployed agent system can improve with fixed model weights by keeping the
updates that win: it proposes changes to its own procedures, checks them,
and retains the ones that make later work better. The
[lead article](./continual-learning-with-fixed-model-weights-llm-selected-updates.md)
describes that loop. This article asks a narrower question for a
maintainer deciding what to build: is it worth paying to also retain an
explanation of *why* a winning patch works, and to keep testing it? We see
three separate bets, each with a comparison that could come out negative or
mixed. None has been tested.

## A hypothetical case

An agent maintains a client's build. Its test-selection rule skipped build
tests for documentation edits, and a README edit broke the build because the
packaging step reads the README. Two retained updates could follow. One is a
patch to the method: before skipping tests, inspect the build's configured
inputs and treat any listed file as code, instead of treating all
documentation as safe. The other keeps the patch plus an account of why it
works: "a file the build reads behaves as code; the configured input list
names every file the build reads." The account cites the README failure as
evidence and names a replay check.

Weeks later an edit to a snippet breaks the build. The build reaches the
snippet through an indirect include, and the input list does not name it. The
patch alone did not flag the edit, because the snippet was not listed.

A system that kept the account has a specific premise to suspect: that the
list is exhaustive. It can trace which files the failing build opens and compare them with the
list. Finding an unlisted read refutes the premise; a match leaves it
unchallenged on this run. A separate check tests the role of the edit:
revert only the snippet and rebuild under the same conditions. If the build
still fails in the same way, the omitted file alone does not explain the
failure. If the build reads the unlisted snippet and reverting the edit
restores the build, the system has a reason to follow includes as well as
listed inputs. That revised rule predicts which other edits need build tests.

The patch-only system is not doomed. It can also investigate, find the
include, and fix it. The question is what the account saves, and at what
cost.

## Bet one: a formulated diagnosis directs the next attempt

The conjecture is that a stated reason for a failure yields more from that
failure than a bare failure signal. To test it, give the proposer the same
raw evidence (diff, build log, failing output) with and without the
diagnosis "the input list may name only entry points". Match the proposal
budget, and count the cost of producing the diagnosis. A wrong diagnosis
counts too, since it can send search the wrong way.

A positive result shows that *supplying* a diagnosis helps. It does not show
that the system can *discover* that diagnosis on its own; that needs a
comparison in which the system formulates it.

## Bet two: criticism can name a separable premise

Does the system find a better repair when criticism identifies one premise
(“the list is exhaustive”) rather than the whole account (“the dependency
account failed”)? Hold edit options open in both arms:
naming one premise can still lead to rewriting everything. The comparison
is about the target of criticism, not the size of the edit. Then check that
retained claims still work on the prior case (the README edit is still
caught) and on fresh cases (other included files).

[Locating a candidate premise is not identifying a cause](../theory/definitions/addressable-theory.md).
The trace can blame the list while the real fault is elsewhere. And a
readable account is not thereby the one
[driving behaviour](../theory/revision-guided-by-rationale-needs-faithfulness-not-just-legibility.md):
the system may have succeeded through the patch alone. The test is
intervention. Keep the patch fixed and run the next investigation with the
exhaustiveness premise withheld, or replaced with a contrary premise. If the
investigation does not change as the premise predicts, the account was
available but not operative.

## Bet three: carrying the tested account across jobs saves work

The third conjecture concerns persistence. Compare a system that carries the
tested account into a different client's build with one that reconstructs
it from the same accessible case history: the README and include failure
records, with the same base model and the same patch. Measure two things
against a common performance threshold: the new target observations needed
(failing builds in the new client's repository) and total cost at comparable
quality, including retrieval, checking whether the account applies, and
maintaining it.

The two measures can diverge. A
[retained theory may reduce new observations after a shift that preserves its structure](../theory/retained-theories-may-improve-sample-efficiency.md),
but that is a separate claim from lower cost. A mixed result is plausible:
the retaining system skips rebuilding the account, so it diagnoses faster,
yet both systems need one failing build before they learn the new client's
include scheme. Retention then saves reconstruction cost but not
observations.

## Theory about a client, or research on one's own method

Revising "the list is exhaustive" changes a theory about the client's
build. Running the three comparisons above is research on the system's own
development method. These are different activities. Commonplace's
[definition of a theory builder](../theory/definitions/theory-builder.md)
covers the first: the system states content, acts on it, criticizes what it
says, and carries the result into the next round. Reflecting on its own
method is a separate property that a builder may or may not have.

The lead's loop can also select a self-edit without stating why it works.
Keeping "inspect build inputs" because it won a replay is selection of a
self-edit, not theory building. The bets here concern what the stated
account adds on top.

## Status

These three conjectures come from [Commonplace’s earlier theory-builder
research note](../theory/commonplace-builds-a-theory-builder-and-tests-whether-it-learns.md).
They concern the additional choice to retain and criticize theories, not
every system that selects changes to its own methods. The example is hypothetical and no comparison has been run.
Commonplace itself is maintained by people and agents together, so its
operation so far is not evidence for an autonomous system. The
[testing supplement](./testing-whether-a-theory-builder-learns.md) gives
fuller experimental designs.
