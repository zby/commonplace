# Draft: conjectural learning

Drafted 2026-11-21 by an agent (claude-fable-5-2) after the operator ruled for
the name. It is a workshop draft. Its destination would be
`kb/theory/definitions/conjectural-learning.md`. Passages marked **[source
needed]** rest on memory.

---

## Conjectural learning

**Conjectural learning** is the method by which a
[theory builder](../../theory/definitions/theory-builder.md) acquires its
theories. The builder proposes a
[tentative theory](../../theory/definitions/tentative-theory.md) in language,
acts on what it says, criticizes what it says, and keeps the result for the
next round. The KB needs the term to name the method as a learning paradigm,
beside methods such as gradient training, and apart from the system that runs
it.

The term names a method. It has no success condition. A builder that runs the
method and whose retained changes do not improve its later work is still doing
conjectural learning, as a reinforcement learning run that learns nothing is
still reinforcement learning. Whether a particular change was learned is a
separate claim, defined below.

### What the term covers

- **The system and the method are named separately.** "Theory builder" names
  the system and its four conditions. "Conjectural learning" names what the
  system does over time. Use the first for membership questions and the second
  when comparing ways of learning.
- **"Conjectural" is Popper's word for the status of the theories.** They
  "remain essentially tentative, or conjectural, or hypothetical"
  ([Conjectures and Refutations, Chapter 1](../../sources/popper-conjectures-and-refutations.ingest.md#quotes)).
  It does not mean speculative or unsupported.
- **The status does work.** A theory held as tentative can be dropped when
  criticism counts against it. Adopting it is a step that can be undone. So
  the builder can act on a theory before anyone has shown that adopting it was
  an improvement.
- **The performer is not fixed.** People, models and programs can each perform
  parts of the method. Commonplace's bootstrap is conjectural learning with
  people performing some of the conjecture and criticism.

### When a change was learned

A retained change was **learned** when the builder that has it is better, on
balance, at its future work than the builder without it. "On balance" has the
meaning given in
[on-balance judgments can guide improvement without a global measure](../../theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md):
for every reasonable measure of that capacity, the builder with the change
scores higher. No measure is selected.

Three verdicts are possible for one change:

- **Learned.** Every reasonable measure favours the builder with the change.
- **Not learned.** Every reasonable measure favours the builder without it.
- **Open.** Reasonable measures disagree, or the evidence has not arrived.

Three points govern use of the verdicts.

- **"Open" is the usual verdict for a recent change.** The capacity in
  question is for work not yet done, so the evidence comes from later
  episodes.
  [Compounding is tested the same way](../../theory/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md).
- **Keeping a change is not the same as having learned it.** A builder may
  keep a change whose verdict is open, because the change can be undone. That
  is a decision. It is reported as a decision until the verdict is in.
- **The claim is about one change in a declared area of work.** "This builder
  learns" is a summary of such claims, and is no stronger than they are.

### What the term does not cover

- **Learning in general.** Learning in
  [Simon's sense](../../theory/learning-is-not-only-about-generality.md) is
  any lasting change in capacity. Gradient training produces it without any
  stated theory. Conjectural learning is one method among several.
- **Any retained text.** Notes that the system stores and never acts on, or
  acts on and never criticizes, are outside the method. The theory-builder
  conditions draw this line.
- **A claim of success.** Calling a system's method conjectural learning does
  not say the system has learned anything.

### Misuse

- Citing the name as evidence that a system improves.
- Reporting a kept change as learned while its verdict is open.
- Using the term for the system. The system is a theory builder.

### Relation to symbolic AI

Stated by the operator on 2026-11-21 and not yet sourced.

What conjectural learning retains is the kind of thing symbolic AI held:
explicit statements that can be read and criticized. The definition of
"learned" above does not mention the method, so it would serve for a symbolic
system too. The difference is in whether the definition can be applied.

- **Choosing among measures.** Deciding which measures are reasonable for a
  purpose takes judgment. A symbolic learning system needed its evaluation
  written down in advance, which is one measure chosen beforehand. **[source
  needed]**
- **Scoring a single case.** The harder obstacle may be lower down. To judge
  one new Python release, a symbolic system could run tests, but it would need
  an enormous array of them. People do not work that way even on single cases.
  They judge on balance there too: whether an error message is better is
  decided by reading it, not by a test suite. For a symbolic system the volume
  of explicit checks would probably be prohibitive. The operator leaves open
  whether it could be organized.

So the new method is a new way of applying an old success condition. It
depends on the conjecture that an LLM can make on-balance judgments, both
about measures and about single cases. That conjecture is not established; the
[Python change judgment probe](../../reports/retained/python-change-judgment-probe-2026-11-20/README.md)
was designed to test it.

---

## Notes for the operator

- **One file or two.** "Learned" is drafted as a section of this definition.
  It could instead be a section of the on-balance note, with this definition
  linking to it. The section is the part most likely to be cited alone.
- **Judgment inside a single case.** The operator's second point means the
  on-balance judgment is recursive: comparing two sets of cases is an
  on-balance decision, and so is scoring each case. The
  [definition workshop](../bounding-omitted-effects/README.md#the-process-is-recursive)
  now records this.
- **What is reversed.** The September definition required changed capacity
  for membership. This draft does not. It restores the name, not that
  condition.
- **Consumers not yet listed.** The theory-builder definition, the research
  companion, the lead article's "distinct learning paradigm" section, the
  `AGENTS.md` vocabulary table, and the eight redirects that mention the
  retired term.
