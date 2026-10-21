---
description: "Report verification selects omission questions by the conclusions they could change, searches beyond cited paths while a consequential conclusion could still change, and stops when every question has a disposition; no file bound or inventory"
type: reference/types/adr.md
status: accepted
---

# 120 — Report verification selects omission questions by consequence

**Status:** accepted
**Date:** 2026-10-11 (method commit `0275b8abb`; recorded 2026-10-21 at the closure of the analysis-lenses workshop)

## Context

An agentic-system analysis covers repositories too large to read whole.
The verification type bounded coverage by materiality and the declared
boundary, and said completeness is relative to the required questions,
not exhaustive inspection. Nothing said how the report verifier, the
role that checks the runtime and lens reports against the frozen source,
should choose where to look for mechanisms the analysts missed, or when
looking further stops being warranted. The instruction's wording, "judge
coverage against the frozen repository tree", named a comparison basis
without a selection procedure. A verifier could read only the cited
files, which finds no omissions, or scan the tree, which has no end.

The audits that prompted the question (Graphiti twice, Napkin, Letta
Code and a blocked Letta run, all pi-sol at one method revision) showed
what an omission search has to catch: a bulk write path that bypassed a
suppression the reports stated universally, a missing provenance index
consumed by retrieval, a retained-file consumer confused with current-run
aggregation, a promotion value no code supported. These are conditions
that change a reported conclusion, found by following a producer to its
consumer or an alternate shipped path, not by covering more files. The
force that would recur if this were reverted: without a selection rule,
omission effort is spent where the worker happens to look, and a
stopping point cannot be explained or audited.

## Decision

**Select omission questions by consequence.** The verifier picks a small
set of questions by the conclusions they could change, drawn from the
required analysis questions, alternate shipped paths and producer and
consumer dependencies, not from listed files. Each question names the
omitted mechanism or condition, where it would live, and why it matters.
Cited anchors are starting points, not a fence.

**Search while a consequential conclusion could still change.** The
report verifier may read and trace the frozen source beyond cited paths.
A search continues while further inspection is reasonably likely to
change a consequential conclusion and the breadth of the claim it
protects justifies the effort. The frozen boundary and correction
ownership are unchanged: the verifier marks defects and the declaring
analyst corrects them.

**Stop by disposition.** Each question closes with supported wording, a
correction request, or an uncertainty compatible with the affected
conclusion. Optional omission expansion stops when every selected
question has a disposition and no identified material challenge lacks
one. Further artifacts alone do not require more inspection. A known
contradiction cannot be deferred because the search stopped. If
narrowing cannot preserve a faithful bounded account, the verifier
requests correction or returns a problem.

**Constrain claims, not reader expectations.** An inconclusive search
narrows the claim to the searched scope rather than appending a caveat
to a universal statement. Unsearched behaviour is never evidence of
absence; an absence claim needs its own searched boundary.

**Retain a brief account.** The Verification section names the
consequential questions investigated, the search basis, the
dispositions and why the search stopped. It is not a query ledger or a
list of unselected questions. Material uninspected alternatives state
which conclusions remain supported and which comparisons cannot be
made. Profile and synthesis verification keep their narrower source
access.

## Considered alternatives

**Clarify the materiality rule only.** Require a stopping rationale and
state that more artifacts do not oblige more inspection, with no
selection procedure. Lost on circularity: a worker who does not know
which questions to ask cannot explain why it stopped asking. Its one
useful addition, the explicit stopping rationale, is kept.

**A recorded-path bound with structural accounting.** The operator's
proposal of 2026-10-11: the runtime role accounts for every top-level
package, manifest and shipped entry path, recording inclusion or an
immateriality reason; lens omission searches are bounded to runtime
paths plus lens-owned anchors. Lost on three counts. The checked
baseline had no exhaustive duty to relocate, so this would add
accounting work on every run rather than remove any. File inclusion
does not select the chain that matters: the Graphiti bulk path was in
an anchored file and still needed a producer-to-consumer question. And
a mechanism outside both sets, an optional cache or instruction
channel, would escape lens review while the comparison looked more
complete than it was. The runtime and lens roles keep independent
discovery authority, with the runtime record as an order-only input.

**Retain the live policy and run a trial first.** Defensible; the
operator chose the prose-only revision without a trial. The trial
design is retained here as the return point: one static comparison of
live-rule against question-driven review on the frozen Graphiti bulk
suppression and provenance claims and one Letta Code committed-versus-
current visibility claim, reviewers not supplied with audit answers, an
effort ceiling set before launch. It would test execution and stopping
after questions are supplied, not whether reviewers select the right
questions.

**A numerical budget.** No count of questions, files or reads was
inferred from the cases; the cases discriminate by consequence, not by
volume.

## Consequences

The change reaches behaviour through the verify-reports job instruction,
the shared worker rules' source-read clause for report verification, and
the verification type's required account. Plan, layout, schemas,
analysis code and the runtime are unchanged; no new verifier, memory
split or dependency was added. Downstream, report analysts receive
correction requests, profile extraction must not emit unsupported
values, and synthesis must carry consequential limits faithfully.

Evidence. The policy was tested retrospectively against five retained
audits, as a judgment of which policy would have framed the right
question, not as proof a worker would detect the errors. Three repeat
runs after the change (Graphiti, Napkin, Letta Code on 2026-10-11)
exercised consequential omission questions and retained stopping
explanations; all three took longer than their comparators, with
concurrent runs, changed inspection scope, repairs and service failures
preventing attribution. Confidence is moderate that this is the smallest
sufficient change and low in any prediction of better detection or
lower effort; neither has been measured.

Limits. Poor question selection is the principal risk: workers may
choose easy questions, miss a controlling mechanism, or write rationales
without narrowing broad claims. Evidence against the decision would be
recurrent missed central conditions despite justified selection, weaker
comparison values, or added reporting work that changes no operator or
consumer decision. The rule covers report verification of single-
repository analyses; multi-repository scope is a separate unadopted
proposal, and the open questions the workshop did not examine (whether
memory is too broad for one role, where feedback and adaptation belong,
which lenses stay fixed across systems, whether the runtime map anchors
lens discovery) are not decided here.
