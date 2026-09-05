---
description: "Regeneration must preserve or recover the commitments later operation depends on; reuse, reconstruction cost, and failure consequences matter more than code size or explanatory-reach alone"
type: kb/types/note.md
traits: [title-as-claim]
tags: [learning-theory, artifact-analysis]
---

# Discarding software requires preserving the operational knowledge later work needs

Software can be regenerated without preserving every version of its code. But
later operation still needs access to the commitments that replacement must
respect: discovered edge cases, data compatibility, interface expectations,
and consequential design decisions. If those cannot be recovered from what
survives, discarding their only carrier creates an information gap.

Kirsch's [critique of ephemeral software](https://www.blackhc.net/essays/future_of_software/)
identifies these production pressures. They support a requirement to preserve
or reconstruct operational knowledge, not a requirement that the original
implementation remain its only carrier. Tests, specifications, records, and
retained explanations can carry different parts of it.

## What must survive a replacement

A billing fix may embody the reason a timezone boundary needs special handling.
A replacement can preserve the corrected behaviour through a retained test and
an account of the boundary, even when its implementation differs. Keeping only
an example may leave the reason unstated; keeping only the explanation may
lose the exact case that exposed the error.

A migration must respect existing data. A retained schema history or conversion
contract can preserve the necessary relationship between versions. Deleting a
migration script is not itself evidence that the relationship was lost, but a
new script must still be checked against it.

An interface carries commitments to other programs or users. Regeneration that
changes those commitments can impose costs outside the regenerated component.
An audit record has a different requirement: reproducing plausible behaviour
is not the same as preserving evidence of which decision actually occurred.

These examples distinguish behavioural continuity, reusable explanation, and
historical evidence. One retained artifact need not provide all three.

## Explanatory-reach is relevant but not sufficient

[Explanatory-reach](./first-principles-reasoning-selects-for-explanatory-reach-over.md)
concerns why a claim transfers beyond the cases that produced it. A retained
explanation may help a replacement handle cases its tests do not enumerate.
That can make preserving the explanation valuable.

Repeated use alone is not explanatory-reach. A particular identifier, contract,
or historical decision may need exact preservation without explaining a broad
class of cases. Conversely, a broadly useful explanation may be cheap to
reconstruct from surviving evidence. Neither code size nor explanatory-reach
alone decides whether retaining a particular implementation pays.

The comparison must include what later work depends on, where that information
survives, how reliably it can be reconstructed, and the costs of retention,
regeneration, validation, and failure. A small one-off script is not automatically
safe to discard; its result may underpin a later decision. A large implementation
is not automatically necessary to retain if replacement is adequately governed
by other durable state.

## Retain knowledge without retaining every computation

[Discarding an artifact is not the loss of all
learning](./ephemeral-computation-prevents-accumulation.md). A house can keep
records and theory, generate temporary code, test it, and retain the evidence
that should affect the next attempt. It can also install reusable code where
reconstruction is costly or inconsistent.

[Codification](./definitions/codification.md) changes how an operation executes.
Persistence changes whether its carrier remains available. Temporary code can
execute a specified rule, and durable notes can guide later judgment without
becoming code. These choices should be evaluated separately.

For a knowledge base, the same test applies. Discarding a draft need not lose
its contribution when evidence and a better formulation survive. Keeping the
draft is valuable when it preserves premises or rejected alternatives that
later work cannot adequately recover. Retaining text is not enough if no later
process can find or use it.

## A discriminating comparison

Compare retained and regenerated implementations on later changes, with access
to the same declared surviving records. Include cases that require a past
compatibility commitment and cases that require extending its rationale.
Measure outcome quality, reconstruction and maintenance costs, and loss of
required history.

If regeneration preserves the required behaviour and evidence at lower total
cost, retaining the old implementation was not justified on those grounds.
If it fails, identify what was missing or misapplied before concluding that
code persistence, rather than a different knowledge carrier, was necessary.

## Scope

The argument concerns continuity of operational knowledge, not a general
security guarantee. Claims about safe disposal still require checking external
effects, retention obligations, and the consequences of error. No artifact type
or project category is automatically safe or unsafe to regenerate.

---

Relevant Notes:

- [Discarding all experience-dependent state prevents cross-run accumulation](./ephemeral-computation-prevents-accumulation.md) — grounds: separates one artifact's lifetime from system-level retention
- [First-principles reasoning selects for explanatory-reach over adaptive fit](./first-principles-reasoning-selects-for-explanatory-reach-over.md) — grounds: distinguishes explanatory transfer from repeated use
- [Retained system-definition artifacts enable persistent deployment-time adaptation](./retained-artifacts-enable-persistent-deployment-time-adaptation.md) — extends: describes retained carriers that can change later production
- [Codification](./definitions/codification.md) — contrasts: assigned execution and durable storage are separate choices
- [The Flawed Ephemeral Software Hypothesis](https://www.blackhc.net/essays/future_of_software/) — evidenced-by: supplies the production pressures this note separates by continuity requirement
