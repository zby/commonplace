---
description: "Retention test for source-checkout design rationale: keep current decision premises not faithfully recoverable from implementation, git, and general knowledge; treat recoverable, role-free explanation as a cache"
type: kb/types/note.md
traits: [title-as-claim, has-external-sources]
tags: [document-system, context-engineering]
---

# Design rationale must preserve decision premises its interpreter cannot regenerate

An LLM-read knowledge base need not restate every theory that could explain a system. For a source-checkout consumer, design rationale must preserve the current decision premises that the interpreter cannot faithfully recover from the implementation, git history, and general knowledge. An explanation the consumer can recover at the required fidelity should be treated as a cache only when the retained passage has no independent authority, cross-check, provenance, activation, or exact-record role.

In his essay *Programming as Theory Building*, Peter Naur locates design theory in the programmer. The programmer can map program parts to world affairs, justify those parts, and judge whether a requested change is similar on the world side. A knowledge base whose retained knowledge participates in its own redesign splits these functions between an interpreter and retained text, since [theory-mediated self-improvement needs both interpretation and retention from one substrate](./theory-mediated-self-improvement-needs-interpretation-and-retention.md). Naur's situated programmer already holds the theory; the essay does not establish how much a fresh interpreter can reconstruct from artifacts. The retention problem here is therefore an extension of Naur's account: which decision premises must the retained text supply when the interpreter lacks that situated history?

## Recovery depends on the consumer, fidelity, and sources

A recovery test must state what the consumer needs to do, how faithfully it must reconstruct the rationale, and which sources it may use. Faithful regeneration reproduces the same decision-relevant claim, including any warrant, epistemic status, or boundary needed to modify the design at the required reliability. A plausible post-hoc rationale that merely fits the visible behavior is a substitute, not a recovery.

For the source-checkout consumer scoped here, three sources are available before it reads any separate rationale:

- **The implementation** — code, contracts, validators, type specs, and the artifacts themselves expose current behavior and enforced state. They establish intended behavior only where a contract records it; otherwise they cannot show whether a mismatch is a regression.
- **git** — the history records what changed, when, and in what order, plus whatever intent or rejected alternatives its commits actually retained. [ADR 074](../reference/adr/074-git-is-the-change-history-layer.md) makes it the checkout's change-history layer, not an oracle for which side of a transition is correct.
- **The interpreter's general knowledge** — ordinary software reasoning and similarity judgments can reconstruct explanations that follow from the other inputs. General availability does not make an explanation current or project-specific.

## What still needs retention

Naur's theory-holder capabilities show where missing decision premises matter, but retention turns on recoverability premise by premise.

A relevance decision explains why a world affair belongs inside the design boundary. The implementation may show that the affair is tracked, but not why it should be tracked or why the boundary stops there. If a contract or commit records that reason at the required fidelity, the declared source set already determines it. Otherwise the rationale must retain it.

A modification judgment depends on applicability scope. Code exhibits behavior in the cases it handles, but it does not determine the intended limit unless a contract or another declared source records that limit. Without this premise, a fresh interpreter cannot distinguish a natural extension from a patch merely by generating a plausible explanation for the current behavior.

Several designs can serve the same intent. Given the intent and implementation, an interpreter may explain why each part exists. But it cannot recover which alternatives were actually considered or why one lost unless a declared source records those facts. Git can carry that record; an unrecorded branch leaves the interpreter to invent a substitute history.

Warrant creates the same problem. Identical implementation and history could result from an evidence-backed choice or an admitted guess when neither input records that status. If the difference would change later testing or revision, the epistemic status is a decision premise worth retaining.

The retained set is therefore not a fixed taxonomy. It consists of current decision premises whose exact claim, warrant, or boundary the consumer needs but whose declared sources do not determine them. Intents, project-specific forces, rejected alternatives, and applicability limits are common instances, not categories necessarily absent from implementation or git.

## Recoverability does not erase independent roles

Whether the sources determine a passage's content is separate from what the retained passage must do. [Attempted recovery identifies informational gaps, not provenance or authority](./documentation-generates-the-system-rather-than-describing-it.md): a governing specification, independent cross-check, provenance record, activation cue, or exact historical record may duplicate recoverable semantic content and still merit retention. Its job is to bind, provide an independent check, trigger use, or identify what was actually adopted. A governing specification exemplifies the authority-bearing exception to reconstructable guidance in [system-definition artifacts are crystallized reasoning under context scarcity](./system-definition-artifacts-are-crystallized-reasoning-under-context.md).

## Treat only role-free recoverable explanation as a cache

Once the fidelity test passes and independent roles are excluded, judge recoverable explanation as a cache. Compare the reconstruction work it avoids across expected uses with its creation, validation, retrieval, maintenance, and failure costs. This is the comparison developed in [opposed recompute factors do not decide documentation segmentation](./opposed-recompute-factors-do-not-decide-documentation-segmentation.md). A retained summary can reduce source access, transformation, verification, and model-side reasoning. It cannot preserve information absent from its declared sources.

Mechanically derived copies have a stricter maintenance rule: [a derived copy of recomputable truth must be checked or absent](./a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md). Natural-language explanations whose fidelity requires judgment instead need an explicit lineage and review path. Neither case licenses a hand-maintained copy to acquire unexamined authority merely because it is convenient to read.

## Scope

- **Source-checkout consumer.** The three reconstruction sources assume access to the implementation and full git history. A vendored or published reader may lack either, so the artifact set for that reader must preserve more decision premises.
- **Interpreter-relative reconstruction.** A stronger interpreter may recover more explanations at the declared fidelity, reducing the material that is retained only for information availability.
- **Trace-free facts.** Greater reasoning strength cannot recover a particular historical fact that no declared source determines. The invariant attaches to the missing trace, not to whole categories such as rejected alternatives or scope limits.
- **Current and decision-relevant.** Nonrecoverability alone does not preserve a refuted or obsolete design belief. The consumer must still need the premise for explanation, modification, audit, or another declared role.
- **Independent roles.** Governing specifications, cross-checks, provenance, activation cues, and exact records are outside the cache test even when their semantic content is recoverable elsewhere.

---

Relevant Notes:

- [A specific intent may out-yield local rationales, but contingent facts stay separate](./specific-intent-may-out-yield-local-rationales-facts-stay-separate.md) — extends: conjectures that an unrecoverable governing intent reconstructs more local rationale per token than equal-budget rationale snippets, and states the test that would refute it
- [An author should fix what the executor can't determine, not what it will](./fix-what-the-executor-cant-determine-not-what-it-will.md) — extends: applies the same availability boundary at instruction grain, where the executor replaces the design-rationale consumer
- [Programming as Theory Building](../sources/programming-as-theory-building.ingest.md) — abstracted-from: supplies the theory-holder's mapping, justification, and modification capabilities; the fresh-interpreter recovery test is this note's extension
