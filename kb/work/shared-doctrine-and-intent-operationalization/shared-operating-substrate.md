# Shared operating substrate for agent work

## Purpose

Determine what Commonplace agents may safely share without restating it, what
must remain explicit and binding, and what belongs in institutional memory or
a current task commission. Settle this model before changing live delegation
machinery.

The operator's starting proposal is:

1. leave broad professional consensus in model weights;
2. record how Commonplace departs from that consensus; and
3. record facts learned after training or otherwise unavailable in the
   weights.

This is a strong starting point. It needs two additions. First, models contain
several legitimate approaches, so Commonplace often must record a **selection
among alternatives**, not only a departure from consensus. Second, retained
material has different roles: a fact, a methodology, a binding doctrine, a
task intent, and an exact protocol should not be collapsed into one category
merely because agents share them.

## Doctrine and methodology are different

A **methodology** is an organized way of approaching a class of work. It
supplies principles, heuristics, methods, and characteristic decision rules.
It can be compared with alternatives, borrowed, taught, selected for one task,
or retained as advice. It does not become authoritative merely by existing.

A **doctrine** is a standing common framework adopted by an organization or
system. It tells its members which purposes, concepts, methodologies, defaults,
and decision rules they should normally bring to bear together. It also
provides a basis for coordinated adaptation when no procedure determines the
answer. Doctrine has an authority and coordination role that a methodology by
itself lacks. In the KB's own vocabulary this is the difference between a
[knowledge artifact](../../notes/definitions/knowledge-artifact.md) and a
[system-definition artifact](../../notes/definitions/system-definition-artifact.md):
[behavioral authority](../../notes/definitions/behavioral-authority.md) comes from the
consumption path — consumer, channel, force — not from the content.

The distinction is therefore partly about content and partly about force:

| | Methodology | Doctrine |
|---|---|---|
| Primary question | How can this kind of work be done? | How do we normally understand and conduct work here? |
| Scope | A class of problems or activities | A community, organization, or system |
| Authority by itself | None; it is available for selection | Standing, within its declared scope |
| Contents | Principles, heuristics, methods, decision rules | Selected methodologies plus purposes, vocabulary, defaults, precedence, authority, and coordination norms |
| Variation | Competes with neighboring methodologies | Resolves or governs enough variation for members to act coherently |

Doctrine therefore includes a **meta-methodological** function: it can say
which methodology applies, how several methodologies compose, which takes
precedence, and when departure is authorized. But doctrine is not merely a
higher-order methodology. A method for choosing methods does not by itself
supply the community's purposes, shared meanings, binding commitments,
authority relations, or coordination defaults. Doctrine combines that
meta-methodological function with an adopted first-order operating framework
and the standing force that makes it common.

The same material can change role. Rolling-wave planning is an external
methodology. If Commonplace adopts its progressive-detail rule for a declared
class of work, integrates it with Commonplace's authority and evidence rules,
and places it in a binding instruction path, that bounded adaptation becomes
part of Commonplace doctrine. The source methodology remains the source
methodology; the adopted doctrine is a Commonplace commitment.

Likewise, *Auftragstaktik* can exist in model weights as a methodology or
historical tradition. A bounded cue may activate it. It does not become
Commonplace doctrine until Commonplace selects the transferable mechanism,
states its local interpretation and limits, and gives it an operative path.

Procedures and protocols are narrower again:

- A **procedure** prescribes how to perform a recurring operation.
- A **protocol** fixes an interface, ordering, grammar, or exchange whose
  exactness is part of correctness.
- **Codified enforcement** implements a rule in code, a schema, a validator,
  or another symbolic consumer.

Doctrine can select or generate procedures. Stable parts of doctrine can be
operationalized into protocols or enforcement. Those artifacts belong to the
shared control plane, but calling all of them doctrine would hide their
different force and verification regimes.

## The shared operating substrate

“Shared doctrine” is too narrow for everything agents need in common. Use
**shared operating substrate** for the combined basis from which a task packet
can be a compact delta:

```text
parametric background
        +
standing Commonplace doctrine and contracts
        +
retained institutional memory
        +
current task commission
        +
execution-time evidence
        -> situated agent action
```

### 1. Parametric background

Model weights supply general knowledge, language and software competence,
familiar professional methods, and representations of established traditions.
This material usually need not be restated when a supported model can
reconstruct it at sufficient fidelity and variation is harmless.

This layer is better described as a repertoire or common prior than as
Commonplace doctrine
([weight-resident methodologies compress behavior in context](../../notes/weight-resident-methodologies-compress-behavior-in-context.md)). It is opaque, model-dependent, and effectively
read-only from Commonplace's perspective. It may also contain mutually
incompatible methods. Knowing several methods does not select one
([a capable agent needs methodology selection](../../notes/capable-agents-need-methodology-selection.md)),
and knowing a relevant principle does not guarantee that it activates when
needed
([knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md)).

Commonplace can rely on this layer for background competence. It needs an
explicit selector when different weight-resident approaches would produce
consequentially different behavior.

### 2. Standing Commonplace doctrine and contracts

This layer answers “how do we normally operate in Commonplace?” It includes:

- project purposes, values, and quality priorities;
- selected methodologies and standing decision rules;
- shared vocabulary and distinctions;
- defaults and conventions used for coordination;
- authority, ownership, escalation, and integration norms;
- departures from broad professional defaults;
- selections among several legitimate professional defaults;
- methodology cues and routing rules that activate the right approach; and
- exact procedures, protocols, schemas, validators, and code where variation
  would be unsafe.

The last item is part of the standing control plane but not all one
representational form. Natural-language doctrine guides judgment. Procedures
specialize it for recurring operations. Symbolic contracts settle choices
that should no longer be left to interpretation.

This layer contains more than departures from consensus. For example, two
commit-message styles, testing strategies, or planning methods may all be
conventional. The weights cannot reveal which one this project selected. The
selection needs retention when independent local choices would conflict or
when later work must not silently reverse it.

It also contains commitments a model probably already endorses. A model may
know that validation and preserving user work are good practices. Commonplace
still states them where they must bind, because likely agreement is not the
same as project authority — the heuristic versus authority-bearing split in
[system-definition artifacts are crystallized reasoning under context scarcity](../../notes/system-definition-artifacts-are-crystallized-reasoning-under-context.md).

### 3. Retained institutional memory

This layer records what Commonplace has learned or committed that cannot be
recovered from weights, current artifacts, and available history at the
required fidelity. It includes:

- observations, measurements, source-grounded claims, and evaluation results;
- failed approaches and counterexamples worth not rediscovering;
- accepted decisions and rejected alternatives;
- project-specific forces, external commitments, and applicability limits;
- provenance, epistemic status, and scope where they affect later use; and
- retained episodes when a distilled rule may need re-examination.

These are not all doctrine. An observation can change what Commonplace
believes without yet establishing how it should normally operate. An accepted
decision is also not merely a learned fact: it records a commitment that
selected one option even when the evidence permitted several
([commitment, not derivation, creates new ground truth](../../notes/commitment-not-derivation-creates-new-ground-truth.md);
[retaining the episode keeps a distilled rule re-derivable](../../notes/retaining-the-episode-keeps-a-distilled-rule-re-derivable.md)). Recurring,
stable interpretations may later earn promotion into methodology, doctrine,
a contract, or code.

### 4. Current task commission

The commission is the task-specific delta over the standing control plane. It
normally carries what the standing doctrine cannot determine for this task
([fix what the executor cannot determine, not what it will](../../notes/fix-what-the-executor-cant-determine-not-what-it-will.md);
[intent-framed delegation is a control regime, not a short prompt](../../notes/intent-framed-delegation-is-a-control-regime-not-a-short-prompt.md)):

- the purpose or desired effect;
- the concrete result and acceptance boundary;
- current privileged facts and external commitments;
- task-specific constraints, permissions, and owned mutations;
- deviations or exceptions from standing doctrine;
- consequential choices deliberately left to the executor; and
- return, escalation, or recovery conditions.

Task intent is not standing doctrine. Doctrine gives agents a shared way to
interpret and act. Intent tells them what this action is meant to accomplish.
Repeating doctrine in every commission wastes context. Omitting task intent
because doctrine is shared removes the criterion needed for adaptation.

### 5. Execution-time evidence

Tool results, current repository state, intermediate artifacts, failures, and
newly exposed constraints become available during execution. When these facts
can change a permitted means, the commission should preserve the choice rather
than frontload a guessed answer.

An observed value does not become doctrine or institutional memory merely
because an agent saw it. Retain it only when a later operation needs it, its
interpretation is stable enough, and the appropriate lifecycle accepts it.

## Two deltas and two information flows

The model has two nested compression boundaries. The first is the
composition diagram in
[borrowing can operate through retained artifacts or weight activation](../../notes/borrowing-can-operate-through-retained-artifacts-or-weight-activation.md),
which this draft sharpens by naming selections and binding restatements as
part of the retained delta:

```text
model repertoire
    + Commonplace selection, commitments, and departures
    = standing Commonplace doctrine

standing Commonplace doctrine
    + current intent, constraints, facts, permissions, and exceptions
    = current task commission
```

Institutional memory and execution evidence enter from the side. Memory
supplies retained facts and prior commitments. Execution supplies current
facts that may alter the chosen means. A later lesson may move from execution
evidence into institutional memory; a stable recurring lesson may later move
into doctrine or enforcement. None of those promotions is automatic.

Calling both deltas “departures” loses selections among mainstream
alternatives. Calling both information flows “doctrine” turns evidence into a
standing prescription before its consequence has settled.

## What must be explicit even when the model knows it

Information availability is only one retention reason. Recoverable material
still needs an explicit artifact when the artifact has an independent role —
the list extends the one in
[design rationale must preserve decision premises its interpreter cannot regenerate](../../notes/design-rationale-must-preserve-unregenerable-decision-premises.md)
with selection, coordination, exactness, and versioning:

- **authority** — it must bind rather than merely advise;
- **selection** — it chooses one methodology or convention among several;
- **activation** — it must become relevant at a particular trigger;
- **coordination** — several actors must use the same value or interpretation;
- **exactness** — variation would break an interface or acceptance condition;
- **versioning and selective revision** — the project must inspect, diff, or
  change the commitment itself;
- **provenance and audit** — later work must know what was adopted and on what
  basis; or
- **stable address** — links, vocabulary, reviews, or other machinery need a
  durable target.

The provisional rule for leaving material in weights is:

> Leave material parametric only when a supported executor can regenerate it
> at sufficient fidelity, it is likely to activate when needed, variation is
> harmless, and no independent artifact role requires it to be explicit.

The complementary retention rule is:

> Retain material when the executor cannot safely regenerate it, or when an
> explicit artifact must bind, select, activate, coordinate, preserve
> exactness, support revision, carry provenance, or provide a stable address.

## Consequence for delegation packets

A packet should not reproduce the whole operating substrate. It should rely
only on standing surfaces the worker actually receives, then supply the
current commission as a delta.

For an omitted detail, the worker must be able to distinguish these cases:

| Omitted detail | Legitimate source of completion |
|---|---|
| inherited default or method | verified standing doctrine or contract |
| deliberately open means | task intent, constraints, and authorized evidence |
| irrelevant variation | any result inside the acceptance boundary |
| unresolved requirement | none; return or escalate |

The packet need not label every omission. It needs enough information to
prevent a consequential ambiguity among these cases.

This turns “self-contained” into a consumption-path property. Ask:

1. Which system instructions, repository contracts, skill text, and task
   packet does the worker actually receive?
2. Which part supplies standing doctrine, and with what force?
3. What current intent and constraints cannot that standing layer supply?
4. Which choices are intentionally completed from execution evidence?
5. Which supposedly shared rule still needs repetition because activation or
   exact reconstruction is unreliable?

For `cp-skill-write-multistage`, generic delegation rules may be omitted only
after the worker's inherited control plane is verified. Each stage commission
still needs its distinct intent, evidence boundary, owned output, acceptance,
and return conditions. Isolation, digests, drift checks, and rollback are
exact workflow contracts, not prose recoverable from general doctrine.

## Representative classifications

These cases test whether the decomposition is useful:

| Commonplace material | Proposed layer and reason |
|---|---|
| Generic Markdown and Git competence | Parametric background; variation is usually harmless until a project rule narrows it |
| “Never `git add -A`” | Standing doctrine; a binding local safety commitment even though the model understands Git |
| Imperative commit subjects | Standing convention; a selection among legitimate alternatives |
| A review result showing one prompt failed | Institutional memory; evidence, not yet a standing rule |
| An accepted ADR | Institutional commitment; the evidence cannot regenerate the selection |
| A review sentinel grammar | Exact protocol; parser compatibility makes variation unsafe |
| The purpose of this workshop | Current commission; doctrine cannot infer why this work is being done now |
| A tool result showing live-target drift | Execution-time evidence; it selects the recovery branch and may not need durable retention |

The classification may move when a material role changes. A repeated review
failure may produce a methodology note; an adopted response may become
doctrine; a stable exact rule may be codified. The later form does not make the
earlier evidence doctrinal in retrospect.

## Questions to settle before machinery revision

1. **Supported interpreter.** Is the recovery baseline the weakest supported
   model, each model partition separately, or the currently selected model?
2. **Activation evidence.** What evidence is enough to rely on a named
   methodology or familiar convention without an explicit gloss?
3. **Actual inheritance.** Which Commonplace and harness surfaces reliably
   survive into each kind of fresh worker context?
4. **Doctrine boundary.** Should “Commonplace doctrine” remain limited to
   standing natural-language interpretation and decision rules, while
   “control plane” also contains procedures and symbolic enforcement? This
   file provisionally says yes.
5. **Standing authority.** Which ownership, integration, and recovery defaults
   are stable enough to inherit, and which must remain task-specific?
6. **Change propagation.** How does a changed standing rule surface every
   skill or packet that relied on omitting it? The mechanism candidate is the
   source-side lineage rule in
   [source changes should surface downstream review targets](../../notes/artifacts-produced-from-sources-need-lineage-recorded-at-the-source.md).
7. **Model drift.** What triggers re-evaluation when a provider model's
   parametric reconstruction changes?

## Acceptance boundary

This model is ready to drive theory and machinery revision when it classifies
representative Commonplace artifacts without conflicting authority, and when
each real worker runtime can name what part of the substrate it actually
receives. It need not become a universal ontology of agent context.

The model fails if:

- methodology and doctrine remain interchangeable, so availability is
  mistaken for authority;
- project selections among mainstream alternatives disappear because they
  are neither departures nor new facts;
- institutional evidence becomes a standing prescription without an adoption
  decision;
- a packet assumes conversational context or doctrine its worker does not
  receive; or
- an omitted requirement is mistaken for local discretion merely because no
  text mentions it.

## Existing theory this model composes

- [Borrowing can operate through retained artifacts or weight activation](../../notes/borrowing-can-operate-through-retained-artifacts-or-weight-activation.md)
  supplies the weight-resident baseline plus explicit project delta.
- [A capable agent needs methodology selection, not just relevant knowledge](../../notes/capable-agents-need-methodology-selection.md)
  explains why broad model competence does not choose one governing method.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md)
  prevents treating availability in weights or context as operative use.
- [Design rationale must preserve decision premises its interpreter cannot regenerate](../../notes/design-rationale-must-preserve-unregenerable-decision-premises.md)
  supplies the recovery test and the independent-role exceptions.
- [A specific intent may out-yield local rationales, but contingent facts stay separate](../../notes/specific-intent-may-out-yield-local-rationales-facts-stay-separate.md)
  separates purpose as an inference seed from facts it cannot entail.
- [Only explicit retention is currently durable, writable, and addressable at once](../../notes/only-explicit-retention-is-durable-writable-and-addressable.md)
  explains why parametric competence cannot serve as Commonplace's versioned
  and selectively revisable commitment surface.
- [Commitment, not derivation, creates new ground truth](../../notes/commitment-not-derivation-creates-new-ground-truth.md)
  distinguishes learned evidence from a project decision that selects among
  options the evidence leaves open.
