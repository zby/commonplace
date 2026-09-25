---
description: "Flywheel recommends claim nodes with counterevidence, evidence artifacts, and current summaries; a design example for separating live research state from its reasoning trail."
source: https://docs.flywheel.paradigma.inc/how-to-use-flywheel/encoding-the-scientific-method
captured: "2026-09-17"
capture: curl+trafilatura
capture_scope: partial-source
genre: official-statement
snapshot_sha256: f46a058b4cb0085f0d3e065a8edc89f56a7a0ec836671c3521c992d2989c134e
ingested: "2026-09-17"
type: types/ingest-report.md
domains: [knowledge-management, research-workflows, theory-refinement]
learning_claims: true
---

# Ingest: Flywheel — Encoding the Scientific Method

## Classification

Official product guidance prescribing a research-writing method. It is evidence of the publisher's recommended practice, without a reported study or account of observed outcomes.
Author: Paradigma, the organization publishing Flywheel documentation; no individual author or publication date is identified in the capture.

## Summary

Flywheel recommends treating research nodes as small arguments containing a claim, supporting evidence, counterevidence, and a next decision. Markdown holds the reasoning; attached artifacts preserve concrete evidence; executions record runs; summaries give the current interpretation; and tags expose operational state. Competing explanations branch from a shared question so each can accumulate its own evidence. The guidance allows other node uses and does not require a special claim field or universal template. Its contribution is a concrete allocation of research responsibilities across existing product primitives, not evidence that this arrangement improves research or enforces scientific standards.

## Quotes

No source quotes have been retained yet.

## Connections Found

The guidance provides a documentation-level example for [active work state being distinct from retrospective memory](../notes/active-work-state-is-not-retrospective-memory-or-chat-history.md): current summaries, operational tags, and next decisions serve different purposes from the longer reasoning trail. This supports the distinction's practical use, but does not establish the note's stronger requirements for closure and evidence gates.

Its instruction to keep concrete evidence inspectable compares with [retaining episode evidence for re-examination](../notes/retaining-episode-evidence-keeps-a-distilled-rule-open-to.md). A changed summary need not replace the premises available for reconsideration. The [discovery lifecycle](../notes/definitions/discovery-lifecycle.md) supplies a useful boundary: organizing support and counterevidence assists inquiry, while a `supported` tag alone supplies neither a named acceptance criterion nor a decision to integrate the claim.

## Learning Claims (our opinion)

The proposed learning mechanism is evidence-guided revision of an explicit research view: attach observations, distinguish rival explanations, and update the summary when evidence changes the interpretation. Nodes and branches make candidate explanations separately inspectable and editable. Against the [theory-builder](../notes/definitions/theory-builder.md) conditions, the claim nodes are localized content by design (condition 1). The workflow prescribes the other three: a next decision that acts on the claim (condition 2), counterevidence and rival branches aimed at what a claim says (condition 3), and a persistent project whose later nodes build on earlier ones (condition 4). A researcher who follows it would be a theory builder with the tool inside the boundary. The page shows none of conditions 2–4 in operation, so for any actual use they are unestablished. Merely adding artifacts or changing a status tag does not meet condition 3, and whether the practice improves later work is a separate learning claim.

The page leaves consequence derivation, diagnosis, revision judgment, and acceptance to the researcher. It describes neither a completed revision episode nor reuse of a revised explanation. Markdown permits varied claims without a dedicated hypothesis schema, but representational flexibility does not demonstrate reliable interpretation. The workflow also takes nodes, branches, artifacts, summaries, and tags as its organizing choices; it supplies no comparison showing that these choices outperform other research representations. The source adds an operational example to the current account, without requiring a change to its learning concepts.

## Extractable Value

1. **A concrete separation of live interpretation and retained reasoning.** Current summaries and next decisions sit beside inspectable evidence and a longer argument. This is a useful design example for the existing active-work-state note, bounded to documented practice rather than demonstrated effectiveness. [quick-win]
2. **Competing explanations as separately maintained arguments.** A common question branches into distinct explanations, each with its own evidence and disposition. This is a reusable research-writing pattern for keeping alternatives visible; the source does not establish when branching pays for its maintenance cost. [just-a-reference]

## Limitations (our opinion)

The capture is marked partial-source. It establishes only the retained guidance, not a complete account of Flywheel's documentation, implementation, or research workflow. The publisher has an interest in presenting its product primitives as suitable research infrastructure; no independent use evidence, comparison, or measured outcome is provided.

Attaching an artifact does not establish its validity, and a supported or rejected tag does not show which test justified that judgment. The page does not specify acceptance thresholds, protection against stale summaries, handling of disputed evidence, or how branching behaves at scale. Ordinary disciplined research writing with linked evidence could explain the proposed benefits without any distinctive graph mechanism. Its scientific-method framing should therefore be read as a recommendation for inspectable arguments, not a demonstrated account of reliable discovery.

## Recommended Next Action

Review [Active work state is not retrospective memory or chat history](../notes/active-work-state-is-not-retrospective-memory-or-chat-history.md) for adding Flywheel as a bounded documentation example of current summaries and next decisions kept distinct from a reasoning trail.
