# The holding conjecture: notes, interpreter, harness

The why-now document diagnoses a gap: models can consume informal artifacts,
but current machinery does not yet hold their theory reliably. This document
states the program's conjecture about what the holding machinery is. Unlike
the two derivations, this is not derived; it is the program's constructive
bet, stated so it can fail.

**The conjecture.** Reliable, economical theory holding across a long horizon
requires three parts working together:

- **Natural-language notes** cache selected results of theory building in
  informal, addressable, revisable artifacts.
- **An LLM interpreter** reconstructs the theory from those results and brings
  it to bear on the change at hand — content usable without content
  codification.
- **A harness**: code that builds each prompt — which notes enter which
  context, when, in what order and framing — so the right theory activates
  on the demand it bears on, and that gates what gets retained back.

The composite holds the theory; the notes alone do not. They spare it from
repeating and reselecting the whole theory-building computation on every
demand, preserve continuity among decisions, and give later learning an
explicit surface to revise.

Mapped to the holding requirements from the holding-gap conjecture: uncued
relevance is harness routing; winning in context is prompt construction;
staying live is retention and curation of the notes; revision is notes
edited from production experience, with the interpreter proposing edits and
the harness gating them.

## Codification returns, aimed at logistics

The harness is code. A purely codified approach formalizes content so
machinery can act on it; this conjecture leaves the theory-building results
informal and codifies their delivery. Naur's limit blocks formalizing the
theory; nothing blocks formalizing when and how the retained results are read.

## The Naur objection, faced

Notes are writing, and Naur's later group had writing: documentation did
not transmit the theory. The conjecture's answer is that the transmission
failed at reading, not at writing — a cold human reader gets the record
without the activation. The triple aims the writing at a different reader
and a different moment: curated for machine reading, routed into the
context at change time, against the demand it bears on. Whether that
difference suffices is exactly what theory-holding experiments must test.
If model-plus-harness readers fail the way the later group failed, the
conjecture is wrong.

## Each part conjectured necessary

Without notes, the theory must live in weights or be reconstructed from the
primary record on each demand. Without the interpreter, notes are
documentation. Without the harness, storage and exposure do not ensure
activation — context stuffing, the current wave's gap. Ablating each part is
therefore a designed experiment, not a thought experiment.

**The competing reconstruction conjecture.** Dedicated theory notes are
unnecessary: an LLM and harness can reconstruct the theory on demand from the
current software, production machinery, task, and raw production record. The
system holds the theory as a reproducible capability rather than a retained
representation; notes merely cache a computation that can be repeated. The
conjecture succeeds if reconstruction preserves coherent change across novel
demands at acceptable cost, and fails if retained theory notes provide a
lasting advantage in capability, reliability, continuity, or total operating
cost that additional reconstruction effort cannot recover.

## Status

The conjecture defines a theoretical system. No running automated software
house of this kind exists: today's software houses fill the theory-holding
role with people — the wave diagnosis. How such a system could come to exist
at all is its own question, taken up by the bootstrap-conjecture document.
