---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Sig's declared local capture, synthesis and sharing system in the frozen sig-releases documentation at commit 314bbea9d1cef911cea0f201eec66a57c2e59020."
run-id: AAS-2026-10-14-sig-releases-50379145ac31-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: complete artifact, partial loop
reviewed-boundary: "314bbea9d1cef911cea0f201eec66a57c2e59020"
analysis-cutoff: "2026-10-14"
evidence-tier: doc-grounded
source:
  identity: https://github.com/sig-ai-app/sig-releases
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/sig-releases-50379145ac31/related-systems/sig-ai-app--sig-releases
  revision: "314bbea9d1cef911cea0f201eec66a57c2e59020"
  sha256: null
---

# Sig boundary

## Boundary and evidence

The target is Sig as described by its public release repository, not a runtime implemented by this repository. The intended use is to characterize its declared work-context capture, private synthesis, selective team sharing and later AI consumption. The target qualifies as a memory/knowledge/context-engineering system: its documentation connects retained work records to AI context and describes direct provider requests (SRC-1, `README.md`). These are product claims, not verified execution behavior.

> Sig is the context layer under your AI tools, not another subscription to choose between
> --- `README.md`

> **Your messages go to your provider directly.** When you send a message, Sig talks to your chosen AI provider (Claude, ChatGPT, etc.) from your computer. We don't proxy, log, or intercept those requests. Your provider keys live in your computer's secure keychain.
> --- `README.md`

The functional boundary includes the declared capture-to-synthesis-to-sharing sequence, local markdown retention, private versus organizational content separation, reusable skills, team knowledge synchronization and AI use of retained context. It also includes the declared privacy and telemetry constraints. SRC-1, `README.md`, `RELEASE_NOTES_v0.1.0-beta.md` and `ANALYTICS.md` supply these contracts; they do not establish how the app implements them.

> **Team knowledge with one click** — share what's worth sharing to a central knowledge base your whole team draws from. Your teammate's Sig has it as context immediately — git handles the sync in the background, invisibly
> --- `README.md`

> **Private by default, shared by choice** — everything lands on your machine as plain markdown. Nothing leaves until you review the exact text and approve it yourself
> --- `README.md`

The frozen boundary is Git commit `314bbea9d1cef911cea0f201eec66a57c2e59020`, with an applicability cutoff of 2026-10-14. The checkout HEAD matches the acquired revision. Inspection of the complete tracked tree and all tracked text files found documentation, issue forms, a license and screenshots, but no executable source, prompts, maintenance instructions, evaluators or shipped drivers. Consequently, the boundary kind is **complete artifact, partial loop**, and the evidence tier is **doc-grounded**. The release-document artifact is inspectable; the app's actual state-production, admission, persistence, retrieval and consumption loop is not. A complete disposition here means the evidence boundary is established, not that the app's behavior has been verified.

The install entry points described in SRC-1, `RELEASE_NOTES_v0.1.0-beta.md` are a macOS DMG and Linux AppImage. Neither is a tracked file at the frozen commit. Their implementations and consumers therefore cannot be traced within this source. No builds, release assets or external pages were acquired, and no target code was executed. The README's Windows availability statement is also only documentary evidence (SRC-1, `README.md`).

External dependencies described by the documents are the user's AI provider, local operating-system storage and secure keychain, git-backed team knowledge sharing, optional Slack and voice connections, and PostHog Cloud EU telemetry (SRC-1, `README.md`, `ANALYTICS.md`). Provider internals, remote team storage, Slack, voice services and PostHog are not frozen sources. Their behavior is not attributed to Sig. This prevents conclusions about end-to-end service guarantees or external enforcement of privacy claims.

### Tracked-tree coverage

This table accounts for every top-level tracked file or directory. It is an inventory of the release repository, not a claim of whole-system loop coverage.

| Top-level path | Treatment and inspected material | Role and conclusion limit |
|---|---|---|
| `.github/` | Included; read `ISSUE_TEMPLATE/bug_report.yml`, `ISSUE_TEMPLATE/config.yml`, `ISSUE_TEMPLATE/feedback.yml` | Public bug and feedback intake, privacy reminder and contact routing. These are support forms, not app entry points, memory maintenance instructions or evaluations. |
| `README.md` | Included; read completely | Product intent, capture/synthesis/share workflow, retention, AI context, team sync and privacy claims. Supports declared responsibilities only. |
| `ANALYTICS.md` | Included; read completely | Declared telemetry categories, exclusions, install identifier and absence of an in-app opt-out. No implementation of the claimed allowlist is available. |
| `RELEASE_NOTES_v0.1.0-beta.md` | Included; read completely | Declared beta features, install and uninstall paths, retention and privacy. Named downloadable builds and the app's `docs/analytics.md` are not present in this tracked source; this prevents inspecting launch behavior and the shipped telemetry contract. |
| `LICENSE` | Included; read completely | Proprietary materials and distribution terms. Does not supply executable behavior or an operational trace. |
| `screenshots/` | Deliberately excluded from visual inspection; inventory identifies `03-chat.png` and `icon.png` | Promotional UI image and branding. No visual UI-layout conclusions are made. Their availability is not an access gap, and screenshots would not establish runtime enforcement. |

The material access gap is the application implementation and its shipped operational content, not an unread tracked code path. It prevents verification of synthesis prompts, model-call sequencing, retention schema, context selection, approval enforcement, synchronization conflict handling, skill execution, maintenance and telemetry filtering. No observed execution trace or causal experiment is supplied. Later findings must remain attributed documentation claims unless the frozen source itself supplies stronger evidence.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/sig-ai-app/sig-releases` | 314bbea9d1cef911cea0f201eec66a57c2e59020 | doctrine/design; reported operation | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/sig-releases-50379145ac31/related-systems/sig-ai-app--sig-releases`. Complete tracked-tree inventory. Doctrine/design: complete `README.md`, `ANALYTICS.md`, `LICENSE`, and `.github/ISSUE_TEMPLATE/{bug_report.yml,config.yml,feedback.yml}`. Reported operation: complete `RELEASE_NOTES_v0.1.0-beta.md` and README feature claims. Screenshots inventoried, not visually inspected. | Doctrine/design: [README](https://github.com/sig-ai-app/sig-releases/blob/314bbea9d1cef911cea0f201eec66a57c2e59020/README.md), [analytics](https://github.com/sig-ai-app/sig-releases/blob/314bbea9d1cef911cea0f201eec66a57c2e59020/ANALYTICS.md), [license](https://github.com/sig-ai-app/sig-releases/blob/314bbea9d1cef911cea0f201eec66a57c2e59020/LICENSE), `.github/ISSUE_TEMPLATE/bug_report.yml`, `.github/ISSUE_TEMPLATE/config.yml`, `.github/ISSUE_TEMPLATE/feedback.yml`. Reported operation: [beta release notes](https://github.com/sig-ai-app/sig-releases/blob/314bbea9d1cef911cea0f201eec66a57c2e59020/RELEASE_NOTES_v0.1.0-beta.md), `README.md`. | No application source, executable build, shipped prompt or maintenance content, evaluator, execution trace or experiment in the frozen tracked tree. Declared beta functionality is not observed operation. Cannot establish actual memory-loop behavior, enforcement, reliability or causal effectiveness. External links and named release assets are outside this frozen evidence. |
