---
description: "Proposal: restructure the behavioral-authority sub-divisions — pipeline paths, force families, an effective/warranted split — with a literature survey of existing authority and provenance decompositions before any carve is chosen"
type: ../types/design-proposal.md
tags: [artifact-analysis, learning-theory]
---

# Revise the behavioral-authority decomposition

The [behavioral authority](../../notes/definitions/behavioral-authority.md) definition's core claim — authority attaches to a consumption path, not to bytes — is sound and heavily load-bearing. Its sub-divisions are not equally developed: the consumer, channel, and force lists were enumerated rather than derived, and writing [a consumption channel delivers force without the history that earned it](../../notes/a-consumption-channel-delivers-force-without-the-history-that.md) strained them at three identifiable points. This proposal holds the option space for restructuring them, with a literature survey as the first gate: authority, integrity, and provenance have decades of prior decompositions, and [a carve that inherits a tested ontology is in a better position than one chosen freely](../../notes/only-derivation-and-inheritance-warrant-a-scope-claim-use-earns-it.md) — the same secondhand purchase that Maes and Smith supplied for [reflective system](../../notes/definitions/reflective-system.md).

## Current state (as of 2026-07-28)

- The definition records three components: consumer, channel, force, each as a flat example list. Two clarifications were adopted directly as uncontested: authority paths compose (one consumer's act is the next path's channel), and placement within a channel is part of effective force.
- Roughly 37 files cite the definition, including the `kb/agent-memory-systems/` reviews, which record behavioral-authority observations per reviewed system. Any change to the component structure has a migration surface there.
- The authority-failure note is live and builds the contrast between force a channel delivers and force the artifact earned entirely in prose, because the definition offers no handle for it.
- The definition's Exclusions section names *effective* authority; no term for *warranted* authority exists anywhere in the vocabulary.

## Problem

Three misfits, each observed in use rather than conjectured:

1. **No warrant dimension.** The record captures who consumes what, through which channel, with what force — and nothing about what stands behind the occupancy: a review verdict, a human commitment, an attestation, or nothing. The authority-failure note's entire subject is the gap between delivered and earned force, and it had to construct the distinction ad hoc.
2. **The force list mixes kinds.** Advice/instruction/enforcement form a bindingness gradient read by an interpreting consumer; validation/routing/ranking influence are executed mechanically; learning input lands in weights with delayed, non-addressable effect. The definition's own hedge on audit triggers ("no force by themselves") signals the heterogeneity. Claims built on the vocabulary inherit it: the authority-failure note's countermeasures hold for interpretive and mechanical force but break for parametric force, where "rollback" means retraining.
3. **Channel is one slot; real paths are staged.** Retrieval selects, assembly positions, the consumer acts — one consumption event spans several list entries, and the countermeasures in the authority-failure note land at different stages (entrance, placement, consumption, after-the-fact). The note had to invent entrance-side/consuming-side vocabulary the definition does not supply.

## Design space

1. **Warrant as a fourth record component.** Every behavioral-authority record names what backs the occupancy. Most expressive; largest migration surface (every existing review record becomes incomplete rather than merely coarse).
2. **Warrant as companion vocabulary.** The record stays a triple; *effective authority* and *warranted authority* are defined as a contrast pair, in the definition or a sibling. No migration; the authority-failure note gets its handle; per-record warrant stays unrecorded.
3. **Pipeline path structure.** A path becomes an ordered chain of stages with position as a named component; the current channel list is re-read as stage instances. Resolves misfit 3 and the retriever/retrieval double-listing; touches every record's shape.
4. **Force families.** Organize the force list into interpretive, mechanical, and parametric families — checking first whether the families are derivable from [representational form](../../notes/definitions/representational-form.md)'s axes (the read/test/probe consumption rule is suspiciously parallel), which would make the carve derived rather than free.
5. **Inherit an external decomposition.** If the survey finds a tested ontology that covers the record's job, adopt it with purchase and local extension explicitly separated, as the reflective-system definition did with Maes 1988.

Free choices, marked as such: the family names in option 4; the warrant vocabulary (warrant vs. earning vs. backing); whether options compose (2 + 4 is coherent; 1 + 3 is a full rebuild).

## Survey targets

The gate before choosing: run the misfits across prior art, recording per thread what it decomposes, whether the bridge to retained-artifact consumption holds, and what it would supply.

- **Clark–Wilson integrity model** — certified transformation procedures as the only write path to constrained data items, plus separation of duty; the closest prior form of the write-authority-plus-review conjunction.
- **Information-flow integrity (Biba; taint tracking)** — integrity levels and taint propagation; the prior form of treating adversarial and innocent low-integrity content as one flow problem.
- **Trust management (PolicyMaker/KeyNote, SPKI/SDSI)** — authority bound to credentials and delegation chains, checked at consumption; a worked warrant dimension.
- **Capability-based security, including its recent application to prompt injection (CaMeL)** — authority as an unforgeable token carried with the reference rather than read from content.
- **Software supply-chain attestation (in-toto, SLSA, sigstore)** — provenance levels and signed attestations in the delivery channel; "history re-coupled to the channel" as shipped engineering practice, with a levels vocabulary that may transfer.
- **W3C PROV** — the entity/activity/agent ontology; a tested general provenance decomposition, possibly too generic to bind force.
- **Speech-act theory (Austin, Searle)** — illocutionary force taxonomies; "force" is already their word, and the interpretive family may inherit its gradient rather than invent one.
- **LangSec** — the data/instruction separation whose absence in natural-language channels is the injection opening the authority-failure note cites via Greshake et al.

## Forces

- **Migration surface**: the agent-memory-systems reviews record the current fields; options 1 and 3 change record shape, option 2 changes none. Cited from [use tests a decomposition locally](../../notes/use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md): the current triple's local success does not license it, but replacing it also re-opens every record built on it.
- **Provenance discipline**: a freely chosen replacement carve is no better warranted than the freely chosen current one; the survey exists to make the revision derived or inherited rather than a second free choice ([rationale](../../notes/only-derivation-and-inheritance-warrant-a-scope-claim-use-earns-it.md)).
- **Context cost**: richer records spend context at every consumption; the authority-failure note's own open question asks whether provenance survives context pressure or entrance control always dominates.
- **Naming risk**: axis names carry hidden dichotomies; expect multiple naming rounds before any family or warrant term is fixed.

## Operativity and warrant

A revised definition is consumed by review authors and note writers through the definition-lookup channel with authoring-instruction force; existing review records are its migration surface, not its consumer. No option adds automated evaluation; the only oracle in play remains human review of the definition itself. For options 1 and 3, "no consumer yet reads the new components" is the honest operativity answer until a gate or review template consumes them — which the adoption decision should weigh against option 2's zero-surface alternative.

## Adoption criteria

- The survey is complete with a per-thread verdict — inherit, adapt, or reject — and a bridge argument for anything inherited, purchase separated from local extension.
- The chosen decomposition re-derives the current consumer/channel/force lists as instances rather than discarding them.
- The migration path for existing review records is stated and priced before any record-shape option is adopted.
- The authority-failure note can be re-grounded on the revised vocabulary without losing any of its three moves (unification, gate-bypass separation, countermeasures-as-one-operation).
