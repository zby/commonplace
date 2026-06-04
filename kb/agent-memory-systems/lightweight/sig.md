---
description: "Lightweight doc-grounded coverage of Sig, a release-doc-backed desktop app that reports local markdown work memory, reviewed sharing, git-backed team sync, and AI-tool context reuse"
type: ../types/agent-memory-system-review.md
source-tier: doc-grounded
traits: [has-comparison, has-external-sources]
status: current
last-checked: "2026-06-02"
---

# Sig

Sig is a desktop work-memory app published through the public `sig-ai-app/sig-releases` repository. Coverage here is **doc-grounded**: the repository exposes README/release/analytics documents, screenshots, and binary releases, but no inspectable application source or file-format implementation was inspected. Mechanisms below are therefore reported product behavior, not code-grounded findings.

**Source:** current [README](https://github.com/sig-ai-app/sig-releases/blob/main/README.md), [latest release page](https://github.com/sig-ai-app/sig-releases/releases/tag/v0.1.0-beta.41), [release notes](https://github.com/sig-ai-app/sig-releases/blob/main/RELEASE_NOTES_v0.1.0-beta.md), [analytics document](https://github.com/sig-ai-app/sig-releases/blob/main/ANALYTICS.md), and the older pinned [README](https://github.com/sig-ai-app/sig-releases/blob/b703fdc2b64ed9164a75ad000103f108fc515b83/README.md) plus referenced screenshot path that the previous note cited.

**Reviewed version:** repository docs on `main` re-read 2026-06-02; latest visible release `v0.1.0-beta.41` dated 2026-05-21; `ANALYTICS.md` says last updated 2026-05-02. The older `adamjramirez/sig-releases` URLs now redirect to `sig-ai-app/sig-releases`.

## Core Ideas

- **Capture, synthesize, share is the reported workflow.** The current README describes a three-stage loop: capture raw meeting/work context, synthesize private notes with facts separated from personal observations, then prepare a reviewed org-level version before anything leaves the machine.
- **Local markdown is the reported memory substrate.** Sig says captures and notes are stored as plain markdown in a folder the user chooses during setup. This is a stronger and more concrete claim than the older pinned README's plain-file phrasing, but still not verified from code.
- **Team knowledge and skills are reported to sync through git.** The README says shared team knowledge and reusable workflows sync while non-technical users do not see the git layer. The repository does not expose the sync, conflict, access-control, or file-layout implementation.
- **Privacy is framed as local-first plus explicit sharing.** The README and release notes report direct provider calls from the user's computer, provider keys in the local secure keychain, optional connections off by default, and no Sig server holding memory content. The analytics document reports anonymous usage counts to PostHog Cloud EU with an allowlist, but this allowlist was not code-verified.
- **Context efficiency comes from human curation and staged disclosure, not documented retrieval budgets.** Sig's reported efficiency move is to keep work history as local markdown and separate raw capture, private synthesis, and reviewed sharing so AI tools can reuse selected history instead of starting from scratch. The docs do not describe token budgets, ranking, search, compaction, or a deterministic context assembly policy.

## Artifact analysis

Claim-level (no application source inspected):

- **Storage substrate:** `files` - Sig reports that captures and notes persist as plain markdown files in a user-chosen folder; team sharing and skills reportedly sync through git. Analytics event counts are a separate service path and are not the memory substrate.
- **Representational form:** `prose` - the central retained work memory is reported as markdown prose: facts, personal observations, team-facing summaries, and reusable workflow descriptions. Any hidden app metadata or sync state is not documented enough to classify.
- **Lineage** - human-authored and app-synthesized. Raw captures come from the user's post-meeting or work narration; Sig reportedly structures them into private notes and prepares a reviewed org-level version before sharing. The synthesis prompt, validator, reviewer UI, and regeneration rules are not exposed.
- **Behavioral authority** - mostly **knowledge artifact** authority when AI tools or Sig's own chat use notes as context. Shared skills/workflows would become **system-definition artifacts** if they instruct future work, but the docs do not show how they are selected, invoked, or enforced.

## Comparison with Our System

Sig and Commonplace make the same substrate bet: durable memory should stay inspectable as files rather than disappear into an opaque hosted chat history. Commonplace turns that bet into typed markdown, validation, indexes, authored links, source snapshots, and review states. Sig's public docs emphasize the adoption layer instead: an app UI, local setup, privacy framing, direct provider use, reviewed sharing, and hidden git for team sync.

The sharpest divergence is governance. Commonplace is explicit about document contracts and validation; Sig is explicit about user review before sharing but does not publish its file grammar, synthesis policy, conflict model, or context-loading rule. That makes Sig useful convergence evidence for local files as workplace memory, but weak evidence for a reviewed memory architecture.

### Borrowable Ideas

- **Capture -> synthesis -> share as a promotion workflow.** Commonplace already has sources, work, notes, and reviews; Sig's framing makes the user-facing promotion boundary cleaner: raw private capture, structured private interpretation, then a reviewed shared artifact. Conceptually ready; implementation should wait for a concrete capture UI or workshop use case.
- **Personal layer separated from factual/team layer.** Sig's reported split between private observations and org-level text is a practical way to preserve subjective signal without accidentally granting it team authority. This is worth borrowing for workplace or team KBs, not necessarily for the methodology library.
- **Hidden git for non-technical team sync.** If Commonplace ever targets non-terminal maintainers, Sig's reported approach is the right packaging direction: keep files/git as the substrate, but make routine contribution and pull operations visible as ordinary app actions.
- **Analytics allowlist as a documentation pattern.** The analytics document is not memory architecture, but it is a useful product trust pattern: enumerate exactly what leaves the machine and what never does. Borrow only if Commonplace grows telemetry or hosted surfaces.

## Read-back placement

**Read-back:** `both` - the docs report pull-style reuse when external AI tools read the local markdown folder, and push-style reuse when Sig itself sends user messages to an AI provider with Sig-managed context. The sources do not document an engineered activation path - no matcher, retrieval budget, before-action hook, or faithfulness test - so `push-activation` is not warranted.

## Curiosity Pass

- The older pinned README described a macOS private beta with signed builds coming soon; current docs now report macOS 13+, Linux, and a public beta release. The product moved faster than the previous note's boundary.
- The most interesting reported mechanism is not "plain markdown" alone; it is the distinction between private personal observations and reviewed org-facing summaries.
- Git-backed team sync is attractive precisely because it hides git from users, but that also hides the evidence needed to judge provenance, conflict resolution, and rollback.
- The analytics allowlist is unusually concrete for a lightweight product review, but without source it remains a policy claim rather than an enforceable finding.

## What to Watch

- Whether Sig publishes application source, an SDK, file-format documentation, or implementation docs; that would determine whether this promotes to `agent-memory-system-review`.
- Whether release notes catch up to the latest beta tags and document what changed between `v0.1.0-beta.1` and `v0.1.0-beta.41`; otherwise the public mechanism trail stays thin.
- Whether the docs explain how AI context is assembled from markdown: direct file reads, Sig-mediated prompt assembly, retrieval/search, truncation, or manual selection.
- Whether git-backed team sync exposes provenance, conflicts, review state, and access boundaries in a way that remains inspectable outside the app.
- Whether the analytics allowlist becomes auditable from source or remains only a public policy document.

## Relevant Notes

- [files beat a database for agent-operated knowledge bases](../../notes/files-not-database.md) - aligns: Sig reports local markdown files as the memory source of truth and git as team sync substrate.
- [agent statelessness means the context engine should inject context automatically](../../notes/agent-statelessness-means-the-context-engine-should-inject-context.md) - motivates: Sig addresses the "new chat starts from nothing" problem by making work context reusable.
- [Napkin](../reviews/napkin.md) - compares: both adapt a local file substrate into an agent-facing memory interface; Napkin is code-inspected and vault-oriented, while Sig remains doc-grounded and workplace-capture oriented.
- [engraph](../reviews/engraph.md) - compares: both treat local human-authored notes as agent-accessible memory; engraph exposes indexing and MCP/HTTP mechanisms, while Sig's implementation is not visible.
- [Fintool](./fintool.md) - compares: both are lightweight product coverage betting on files-first agent memory; Fintool is commercial finance/report evidence, Sig is desktop workplace-memory release-doc evidence.
