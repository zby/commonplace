---
description: "Lightweight coverage note for Sig, a private-beta macOS work-memory app that stores meeting and decision context as local files for AI tools"
type: kb/types/note.md
traits: [has-comparison, has-external-sources]
status: current
---

# Sig

Sig is tracked here as lightweight related-system coverage, not as an `agent-memory-system-review`. The public `adamjramirez/sig-releases` repository has a [README](https://github.com/adamjramirez/sig-releases/blob/b703fdc2b64ed9164a75ad000103f108fc515b83/README.md) and screenshots, but no inspectable application source, package manifest, [public binary release](https://github.com/adamjramirez/sig-releases/releases), architecture document, or file-format spec as of 2026-04-24. The repo-backed review type requires code access, so this note records the visible system shape without treating the product claims as verified implementation.

Sig is a private-beta macOS app for turning work history into AI-readable local memory. Its public claim is simple: after meetings, the user spends a few minutes recording decisions, commitments, and their own interpretation of what happened; Sig stores that material as plain files on the user's machine; AI tools that can read files then use the resulting knowledge base instead of starting from scratch each chat. The [screenshot](https://github.com/adamjramirez/sig-releases/blob/b703fdc2b64ed9164a75ad000103f108fc515b83/screenshots/03-chat.png) reinforces the file-backed workflow by showing the assistant reading `bailey-drake.md`, `this_week.md`, and `kb-rollout.md`, writing to three files, updating an individual file, and adding a decision to a team KB.

## Source-visible design

**Human-captured work memory.** Sig's capture loop is manual and post-meeting: the human tells the app what happened, what was decided, who owns what, and what they think about it. This is not trace-derived agent learning; the source signal is human-authored operational memory.

**Plain files as the sharing boundary.** The README says Sig stores everything as plain files on the user's machine and relies on existing AI tools' file-reading ability. That aligns strongly with [files beat a database for agent-operated knowledge bases](../../notes/files-not-database.md): file access is the integration surface, not a product-specific retrieval API.

**Personal-first, team-later topology.** The product starts with private local memory and later shares selected material to a central team knowledge base. The README does not expose the promotion policy, conflict model, access control, or synchronization mechanism, so the team layer should be treated as direction rather than reviewed architecture.

**App UI over terminal workflow.** Sig's visible differentiation is packaging: it targets non-terminal workplace users who want capture, chat, pinned topics, activity logs, and skill-like modes in a native app. Compared with most systems in `../reviews/`, the novel part is less the storage substrate and more the UI wrapper around disciplined capture.

## Comparison with Our System

Sig and commonplace make the same substrate bet: agent memory should stay inspectable and directly readable by AI tools. Commonplace uses typed markdown, validation, indexes, and link semantics to make those files governable; Sig's public surface currently emphasizes low-friction capture and AI access, not document contracts.

The most interesting divergence is audience. Commonplace is an agent-operated methodology KB maintained by technical users and scripts. Sig appears to be a personal/team workplace memory app where the user should not need a terminal, type schema, or validation command. If Sig works, it is evidence that files-first memory can be packaged for ordinary work contexts, but the public repo does not show whether the underlying files remain composable, portable, or reviewable once the app mediates them.

## Borrowable Ideas

**Two-minute post-meeting capture as a workflow primitive.** Ready to borrow conceptually. Commonplace has sources, notes, and workshops, but it does not yet have a small capture ritual for "what changed in the user's operational world today." Sig's framing suggests a lightweight work-log-to-KB bridge.

**Visible activity ledger for memory writes.** Worth borrowing when commonplace grows a user-facing capture UI. The screenshot's right rail separates the user's input from concrete write effects: wrote this week's file, updated Bailey's file, added to team KB. That kind of write receipt would make agent memory mutation easier to audit.

**Personal-to-team promotion boundary.** Needs implementation evidence first. The claimed local-private-first flow maps well to a workshop-to-library promotion pattern, but the hard part is deciding what becomes shared knowledge and how conflicts are governed.

## Review boundary

Do not create `kb/agent-memory-systems/reviews/sig-releases.md` unless public application source, a readable release artifact, or implementation documentation becomes available and is inspected. The current repository is a release/early-access page, not a codebase. The review risk is therefore high: storage model, file layout, retrieval, privacy, team synchronization, and AI-tool integration are all product claims rather than code-grounded findings.

## What to Watch

- Whether public signed builds or source code appear in `adamjramirez/sig-releases`
- Whether Sig documents its on-disk file layout and team-KB synchronization model
- Whether the app keeps files as the primary source of truth or uses files as an export/projection of an internal store
- Whether it adds governed promotion from private captures into shared team knowledge, including provenance and conflict handling
- Whether AI tools read Sig's files directly or through an app-mediated context layer

---

Relevant Notes:

- [files beat a database for agent-operated knowledge bases](../../notes/files-not-database.md) — aligns: Sig's public story makes plain files the integration boundary for AI tools
- [agent statelessness means the context engine should inject context automatically](../../notes/agent-statelessness-means-the-context-engine-should-inject-context.md) — motivates: Sig addresses the "new chat starts from nothing" problem by making work context loadable
- [Napkin](../reviews/napkin.md) — compares: both adapt a local file substrate into an agent-facing memory interface, but Napkin is code-inspected and vault-oriented while Sig is lightweight and workplace-capture oriented
- [engraph](../reviews/engraph.md) — compares: both treat local human-authored notes as agent-accessible memory; engraph exposes the indexing and MCP/HTTP layer, while Sig's implementation is not visible
