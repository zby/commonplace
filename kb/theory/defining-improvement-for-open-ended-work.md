---
description: "What a usable definition of improvement for open-ended work needs to handle, drawn from editor, release, dependency, KB, and refund cases, before proposing a working definition."
type: types/note.md
---

# Defining Improvement for Open-Ended Work

For any proposed change in open-ended work, a maintainer or automated selector faces one practical question: **what would count as better work here, and how could we tell?** Asking *what would make Emacs a better editor?* does not answer it, because Emacs itself is too broad. The focus comes from the stream of work its users expect to do, before anyone proposes a feature.

Suppose that expected work includes both multi-file replacements and routine single-file edits. Follow a recurring difficulty to the step and consequence that matter: users miss an unintended edit in a second file because they see only the current buffer before saving. That points to a needed capability—inspecting changes in *other affected files* before committing them—and yields two concrete requirements before anyone runs a trial: a proposed preview must show changes in buffers the user is not viewing, and an ordinary single-file save must require no extra confirmation.

Those checks reject poor designs early. A preview that interrupts every save taxes single-file editors for a feature they may never need; switching to an on-demand command removes the interruption but helps only users who remember to invoke it, leaving a trade-off that counting prevented mistakes alone will not settle. Once a design clears the initial checks, the trial tests the consequence that motivated the work: give users the same editing tasks with and without the preview and check which unintended edits reach disk, not just whether the preview renders.

An automated software house—a system that develops software for different clients—must answer that question afresh for each program it takes on, whether an editor, a parser, or a knowledge base. What transfers across domains is deriving requirements and tests from the expected task stream, not a fixed list of features or measures. Even then, the future task stream is a forecast unless the work is already scheduled: a test answers for the cases it represents, not how often they will occur or whose losses should count most.

The cases below—an open collection of hypothetical examples alongside one actual recorded judgment—show what a usable definition of improvement for open-ended work has to handle.

## Publish a release or hold it for a fix?

What counts as better depends on the decision being made and who bears its cost: publishing a release offers an option, whereas adopting it commits an application to using it. A release manager and an application maintainer can therefore agree that a Python version is ready to publish and that a given application should not upgrade yet.

Consider Python 3.11's removal of `inspect.getargspec`, which turned a 3.10 deprecation warning into a failure. Treating that as a release decision rather than a claim about Python's history, should the team publish now or hold the release while affected dependencies are repaired? Publishing lets some users benefit immediately; waiting may spare others a broken upgrade. Counting new features does not settle whether the wait is worthwhile. If affected users can test before switching and remain on a supported version, the case for publishing is stronger than if the break is hard to detect or waiting is not an option for them.

## Update one project's dependency?

Not every comparison stays open: when evidence ties a fix directly to the project's actual work and respects its commitments, a maintainer has clear grounds to act. Suppose an agent proposes a dependency update that fixes a parser error. The maintainer tests an input the project actually receives: the installed version rejects it, while the candidate parses it and produces the expected downstream calculation. Existing tests still pass, and the release drops no platform or interface the project promises to support.

That gives enough reason to merge the update rather than keep the lockfile unchanged: a live failure is fixed, existing behavior holds, and no commitment is broken. A green test suite alone would not have identified that gain. Conversely, if the broken input never reaches this project, the upstream fix is real but no longer this project's reason to update; if the release drops a promised platform, the trade-off reopens until that commitment can be preserved. The proposal and its approval do not by themselves establish a gain—those checks do.

## Add a KB note or leave the answer where it is?

Comparing against a simpler alternative can reveal the same work gain at lower maintenance cost, and clarifies what later evidence counts. Suppose a maintainer has twice had to reconstruct why two similar proposals received different decisions. Adding a note might save the next reader that work, yet if an existing decision record already gives the reason and readers simply miss it, linking to that record may do the same job without creating a second account to maintain. Either way, the useful later observation is not that someone opened the note, but that someone facing a fresh case found and applied the distinction they previously had to reconstruct. Whether that benefit justifies maintaining another note still depends in part on how often the question recurs.

## Add a pointer to `AGENTS.md`?

Unlike the hypothetical cases above, this is an actual recorded judgment: Commonplace [considered and rejected such a pointer](../reference/adr/076-source-claim-grounding-is-a-promoted-skill.md) after an agent took a request to retain supporting quotations to the wrong skill. The case shows how the stated aim narrows which remedies even count. A pointer would have made the intended procedure easier to find, but the other skill would still have advertised the same operation. Because the aim was to remove a competing route rather than merely make a missing procedure findable, the maintainers chose one advertised entry instead. The decision record explains why they expected their change to help; it does not count subsequent misroutes or establish that they stopped.

## Change who can authorize a refund?

When a permanent change carries unclear downside, a time-bounded trial is itself a distinct alternative—and checking whether it works as designed is separate from checking whether it works better. Suppose a company requires head-office approval for every refund, and a branch manager proposes letting branch staff decide routine cases. Starting from counter work separates two situations. For a low-cost item returned with a receipt, head office repeats a check the branch already made while the customer waits. For a disputed large charge on a delivered service, the branch may lack the records needed to settle it. That detail reshapes the proposal: delegate authority for receipted returns below an agreed amount rather than for all refunds.

Suppose the company delegates that authority for one month, after which it returns to head office unless a manager reviews the results and renews it. Even if the manager says, “Let’s try it for a month before we decide,” we count [the trial itself as a change](./reversibility-can-favor-a-change-by-limiting-future-loss.md): during that month, branch staff can issue refunds they could not issue before. Delegation with expiry and review is a third alternative alongside keeping head-office approval and delegating indefinitely.

During the trial, two checks show whether the arrangement *works as designed*: can staff complete an eligible refund during the customer's visit without waiting for head office, and do disputed charges still reach someone with the records and authority to resolve them? Judging whether it *works better* requires comparing customer waiting time, staff effort, and mistaken payments against similar cases under the old rule. If customers wait less while mistaken payments rise, a larger sample can clarify how often each occurs, yet it cannot decide how much loss the company is willing to accept to spare customers a second visit.

## What a usable definition of improvement needs

Taken together, these cases set the requirements for any working definition of improvement we might propose and test:

- **Grounded in consequences for the expected work.** It must separate working as designed or mere uptake (a rendering preview, a green unchanged test suite, an opened note) from whether the work went better (fewer unintended disk writes, a real input parsed, a distinction applied on a fresh case).
- **Indexed to the named alternative, decision, and commitments.** It must tie the comparison to the actual choice—offering a release versus adopting it, linking a record versus adding a note, running a time-bounded trial versus permanent delegation—and respect prior commitments such as a promised platform rather than dropping them for an easy win.
- **Clear wins without forced closure.** It must give clear grounds to act when a change fixes a live failure without breaking commitments, while letting genuinely contested trade-offs (interruption against safety, waiting time against mistaken payments) stay visibly open so a maintainer can still act without claiming the change was established as better.
- **Fixed for a test, yet responsive to new evidence.** Because a working definition is not the only meaning of *better*, it must be stated before a test and kept fixed for that test. New evidence can still overturn a verdict—users may turn out to rely on an interface thought unused—without changing the standard after seeing who lost.
- **Three distinct judgments.** It must keep separate:
  - **A reasoned forecast** at selection time: whether available evidence gives reason to *expect* better work than under the alternative, without requiring exact probabilities or a single formula.
  - **A calculation of expected value**: a narrower quantitative forecast combining estimated frequencies (saved visits, mistaken payments) with valuations of those outcomes.
  - **An observed outcome** afterward: whether the resulting work *was* better—where a loss during one trial does not by itself refute a reasonable earlier forecast.

## Evaluating a selector over a stream of work

Those requirements govern a single change. A usable definition also has to support testing a selector itself—human or LLM—without demanding that it find the best conceivable change or be right about every proposal. Compare the system that uses the selector's choices against a specified alternative over the same stream of work, counting what happened during trials—including review cost and losses incurred before reversal. The question is whether the resulting work was better over that period, not how many individual changes were kept.
