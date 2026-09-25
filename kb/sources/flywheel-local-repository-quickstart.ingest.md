---
description: "Flywheel documents pending graph inspection, stale-state guards, explicit discard, and separate local commit and publication boundaries."
source: https://docs.flywheel.paradigma.inc/quickstart
captured: "2026-09-17"
capture: curl+trafilatura
capture_scope: partial-source
genre: official-statement
snapshot_sha256: 0cbf939eb38fa046c232098540d9cd24dd8b045ea4fdb5fb66471d80b106cb74
ingested: "2026-09-17"
type: types/ingest-report.md
domains: [knowledge-graphs, state-management, recovery]
---

# Ingest: Flywheel local repository quickstart

## Classification

Official product documentation by Paradigma describing the intended behavior of Flywheel's local repository commands. Its author is positioned to specify the interface, but the page supplies neither implementation evidence nor an account of observed operational outcomes.

## Summary

Flywheel's [quickstart](https://docs.flywheel.paradigma.inc/quickstart) separates pending graph edits, local durable commits, and hosted publication. Edits operate on the pending graph and validate graph rules before replacing staging. Explicit staged readers expose pending state with its staging digest and committed base, while default readers expose committed state. The complete staged diff shows net changes; review does not reserve a subsequent commit, so changed staging or head requires renewed inspection. Invalid saved batches remain inspectable through status and can be discarded only with explicit confirmation and the matching digest. Local editing and commit work offline; a separate authenticated push publishes. The useful contribution is a documented division of state inspection, mutation guards, destructive recovery, and publication authority.

## Quotes

No source quotes have been retained yet.

## Connections Found

The source is a concrete design example for [Enforcement without structured recovery is incomplete](../notes/enforcement-without-structured-recovery-is-incomplete.md): rejection preserves earlier pending work, failure reports identify the offending operation, and an explicit discard operation handles an already-invalid saved batch. This supports distinguishing enforcement from a subsequent recovery choice. It does not establish automatic repair or the ability to reconstruct the intended graph.

It also illustrates [Error messages that teach are a constraining technique](../notes/error-messages-that-teach-are-a-constraining-technique.md). Superseded commands fail without mutation and print their exact replacements. That is a specified remediation interface, with no measurement here of whether agents successfully follow it.

## Extractable Value

1. **Separate rejection from recovery and preservation.** The documented workflow preserves prior pending work when an edit fails, allows status inspection without applying invalid operations, and reserves whole-batch discard for an explicit digest-matched choice. This adds a concrete recovery boundary to the existing enforcement discussion: abandoning pending work can restore an editable workspace without repairing the intended graph. [quick-win]
2. **Make the inspected state identifiable.** Pending reads identify both the staging digest and nullable committed base; staged pagination binds its cursor to those values and the query. Changed state invalidates continuation. The reusable design question is how a review consumer detects that the state it inspected has changed; the page does not establish that inspection locks or reserves that state. [just-a-reference]
3. **Keep persistence and publication separate.** Local commit records pending graph work without sending it to the service; authenticated push is a distinct operation. This is a context-bound interface example for deciding where a KB workflow crosses from local retention to shared availability. [just-a-reference]
4. **Provide migration instructions in failure output.** Exact replacement commands turn obsolete-command rejection into a documented next step, illustrating the existing teaching-error claim without supplying new outcome evidence. [just-a-reference]

## Limitations (our opinion)

The capture is explicitly partial: several passages introduce command examples that are absent. It supports analysis of the retained interface descriptions, but cannot establish a complete runnable setup or the omitted command syntax. No Flywheel code was inspected or executed, and no concurrent-edit, crash-recovery, or publication behavior was tested. These are vendor statements about intended behavior, with no independent confirmation or performance comparison.

The strongest mechanisms concern transactional state management. They do not show that graph contents are correct, useful, or scientifically justified. In particular, a digest identifies pending state; it does not establish its semantic quality. Review is also not a reservation of the later commit.

Discard permanently removes all pending work in the selected repository, makes no automatic backup, and preserves committed history. Calling it recovery must retain that cost and scope. As the [recovery note](../notes/enforcement-without-structured-recovery-is-incomplete.md) distinguishes, detecting a violation does not by itself supply the correct replacement: this source documents an abandonment route, not an oracle for repair. It offers no evidence comparing this design with alternative recovery interfaces or showing improved agent outcomes.

## Recommended Next Action

Review [Enforcement without structured recovery is incomplete](../notes/enforcement-without-structured-recovery-is-incomplete.md) for a bounded example distinguishing preservation after rejection, explicit abandonment of invalid pending work, and repair of the intended result, using Flywheel's documented discard behavior.
