---
description: "Explicit artifacts give a learner direct targets for inspecting and revising commitments; durability, writability, and effective addressability still depend on the boundary and available operations"
type: kb/types/note.md
traits: [title-as-claim, has-comparison, synthesis]
tags: [learning-theory, self-improving-systems, agent-memory]
---

# Explicit retention provides direct targets for selective revision

A retained theory, rule, or procedure can make a commitment an object the
learner retrieves, criticizes, and revises. This is the practical advantage of
explicit retention: it supplies a direct target for a named change. It does not
establish that explicit artifacts are the only way to learn, transfer a
judgment, or govern behaviour.

Three properties must be assessed separately. **Durability** means state
survives across the horizon of the learning claim. **Writability** means the
system can change it through its permitted operations. **Addressability**
means those operations can target the relevant commitment, rather than only
replace or probe the component as a whole. [Reflection buys
addressability](./reflection-buys-addressability.md), but neither a readable
file nor a numerical parameter guarantees a clean boundary around a semantic
commitment.

## Compare operations, not opaque and readable substrates alone

| Retention form | Durability and writability | Handle on a commitment |
|---|---|---|
| Context-conditioned state | Depends on runtime persistence; discarded state does not survive the episode | The retained transcript may be editable even when the state it induces is not directly inspectable |
| Pinned model parameters | Durable over the run, not writable under the pin | Prompting or probing changes the conditions of use, not the parameters |
| Parameters with an allowed update path | Updates can persist | A targeted edit needs evidence that it changes the intended judgment without unacceptable collateral effects |
| Human expertise inside the boundary | Can persist and change through practice | Articulation and behavioural tests expose some commitments; the person's whole competence is not a versioned artifact |
| Natural-language and symbolic artifacts | Durable when retained and writable when permissions allow | Text spans, rules, functions, and fields provide direct edit targets; their consequences still need checking |

These are operation profiles, not permanent rankings of
[representational forms](./definitions/representational-form.md). A read-only
note is not writable. A vague theory paragraph may not isolate one assumption.
A retained context can affect later work even without a separately written
theory. A numerical representation with a tested commitment-level editing
interface should be assessed by that interface, not excluded by its form.

The distinction between a transcript and the competence it induces is useful.
Editing a sentence is direct control over the text, not guaranteed selective
control over the resulting judgment. The same limitation applies to a retained
theory: its apparent locality must be checked against the behaviour of the
system that consumes it. [Reflective coverage](./reflective-coverage-is-graded-across-representational-forms.md)
therefore reports the operations available on each part.

## What follows under the fixed-model premise

When model parameters are pinned and the declared writable surfaces are
natural-language and symbolic artifacts, retained changes must use those
surfaces. This follows from the declared update rules, not from a theorem that
other substrates cannot learn. A cached state or external record also needs
its own declared persistence and consumption path.

[Commonplace's declared frame](../reference/commonplace-declared-frame.md)
places provider weights outside the revision boundary. Changing a model binding
there edits a configuration request; it does not edit the provider's weights.
That describes one system's available operations, not a general limit on
learning systems.

## Explicitness supports one route to transfer

A human can externalize a criterion as a rule, rationale, example, or test that
computation later consumes. A named criterion makes it easier to compare what
was transferred and to revise the record when its use fails. This is useful for
[methodological closure](./methodological-and-computational-closure-track-different-changes.md),
which asks what a retained method settles.

Computational transfer need not follow that route. A model may already supply
the required judgment, infer it from examples, or acquire it through an allowed
parameter-learning process. Such a transfer may be harder to inspect
commitment by commitment. It can still be governed through outcome checks,
limited authority, regression tests, and rollback. Lack of a directly editable
criterion is not lack of all governance, and automatic execution is not proof
that a criterion has become explicit.

## What would establish the advantage

At a selected decision, identify the commitment to change and compare the
available editing routes. Measure whether the intended later behaviour changes,
what collateral behaviour changes, whether the update can be reversed, and the
cost of diagnosis and validation. Explicit retention earns its place when its
direct targets make that process more useful at acceptable cost.

An equally selective numerical or reconstructed representation would defeat
an exclusivity claim. A readable edit that repeatedly changes unrelated
judgments would defeat the assumed locality of that artifact. Neither result
would deny that retained state can support learning.

## Scope

Addressability concerns the commitment and the operations the claim actually
needs. It is not complete transparency of the learner. Retained episodes,
examples, theories, and programs can supply different information and different
edit targets; [retaining an episode](./retaining-the-episode-keeps-a-distilled-rule-re-derivable.md)
can preserve details that a distilled rule omits. None guarantees that later
interpretation recovers those details correctly.

---

Relevant Notes:

- [Reflection buys addressability](./reflection-buys-addressability.md) — grounds: supplies the direct-target advantage and its comparative scope
- [Reflective coverage is graded across representational forms](./reflective-coverage-is-graded-across-representational-forms.md) — grounds: evaluates available operations rather than inferring control from component membership
- [Methodological and computational closure track different changes](./methodological-and-computational-closure-track-different-changes.md) — contrasts: explicit decision content and human-free execution are separate properties
- [Retained system-definition artifacts enable persistent deployment-time adaptation](./retained-artifacts-enable-persistent-deployment-time-adaptation.md) — extends: connects retained artifacts to later behaviour
- [Retained artifact](./definitions/retained-artifact.md) — defined-in: the durable state whose later consumption matters
