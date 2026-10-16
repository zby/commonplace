---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Sig runtime baseline: declared capture, AI-provider, sharing, skills and telemetry paths in its public release documentation."
run-id: AAS-2026-10-14-sig-releases-50379145ac31-01
reviewed-boundary: "314bbea9d1cef911cea0f201eec66a57c2e59020"
---

# Sig runtime report

## Runtime account

This is a documentation-grounded account, not an implementation trace. The frozen artifact describes a desktop application but does not contain its executable implementation, prompts or supplied run traces. The boundary is the complete release-document artifact and a partial application loop, as established in [boundary](boundary.md#boundary-and-evidence). All runtime activation, reliability and benefit remain unobserved. Source references below use SRC-1 at the frozen revision. Inspection covered the complete README, release notes, analytics document and three issue forms already registered by the boundary; no new source or execution evidence was acquired.

### Ordinary invocation and effect boundary

The documented entry is a desktop app. The beta release notes name macOS DMG installation followed by opening Sig from Applications, and a Linux AppImage launched after making it executable (SRC-1, `RELEASE_NOTES_v0.1.0-beta.md`). The README also advertises Windows but does not supply a corresponding launch sequence (SRC-1, `README.md`). Builds are outside the frozen source. These are described shipped entry paths, not inspected executable entry points.

In the ordinary workflow, the user opens Sig and describes a meeting. Sig structures a private note with facts separated from personal observations; local markdown in the first-run-selected directory is the declared durable result. Sig then prepares an organizational version. The user decides its contents, reviews the exact text and clicks send. The team knowledge base receives the approved material and git performs background synchronization. A teammate's Sig is said to receive it as context. This is the declared sequence in [RT-RTE-capture-share](#rt-rte-capture-share), not a verified call graph. The user owns capture and approval decisions; Sig owns synthesis and preparation; git is the named synchronization mechanism. The documents do not specify synthesis prompts, computational decision policy, intermediate state, provider-call ordering, concurrency, conflict resolution, cancellation or failure recovery.

The provider path is separately described: when the user sends a message, Sig contacts the selected provider directly using credentials stored in the OS keychain. The terminal conversational reply is implied by the app's chat description and analytics references to replies, but its transport, streaming, retries and persistence are not specified. [RT-RTE-provider-message](#rt-rte-provider-message) and [RT-CMP-ai-provider](#rt-cmp-ai-provider) retain this distinction. No source establishes whether synthesis and chat share an invocation loop, or exactly which retained records a particular request receives.

The advertised long-term result is more useful AI context, not demonstrated improvement. SRC-1, `README.md` supplies this assertion:

> **Week 12:** You've built something nobody else has — months of real work history that makes every AI you use dramatically sharper.
> --- `README.md`

There is no supplied comparison or execution trace supporting the benefit. Detailed retained-object revision and retrieval analysis belongs to the memory member; this runtime baseline does not infer those mechanisms from the workflow labels.

### Forcing paths and guarantees

Three documentary forcing cases materially bound the privacy account:

1. **Provider egress despite sharing approval.** The exact-text review policy concerns team sharing. Sending a message independently sends data to an AI provider. Therefore approval before team publication cannot be treated as a gate on every network request. The separate clauses in [RT-CLM-private-sharing](#rt-clm-private-sharing) and [RT-CLM-provider-direct](#rt-clm-provider-direct) support this narrower reading.
2. **Telemetry and explicit feedback.** Analytics is described as automatic anonymous counts, with no current in-app off toggle. User-submitted feedback text is an explicit exception to content exclusion. [RT-RTE-analytics-egress](#rt-rte-analytics-egress) makes this a separate outbound path rather than asserting that all content remains local.
3. **Reusable skills and optional integrations.** Team-shared skills can reach another installation; Slack, team knowledge and voice are separately enabled connections. A skill's label does not establish its permissions or its ability to bypass approval. Neither shell execution, provider-native tools, host callbacks, remote workers, dynamic executable extensions nor alternate direct APIs can be enumerated from the supplied documentation. Their existence and absence both remain unestablished; the docs cannot support universal mediation.

For the team-sharing guarantee, Sig is the declared policy owner, the proposed enforcement point is the exact-text review/send boundary, and the strength is **policy**, not an inspected invariant. Coverage is the prepared organizational share, not provider messages, analytics or public issue submissions. End-to-end privacy additionally depends on the provider, OS storage/keychain and team repository contracts, none of which are frozen here. The claims below carry separate documentation, implementation and operation statuses.

For telemetry, the claimed enforcement point is an in-app allowlist plus sanitization before sending; its owner is Sig and its strength is **policy** in this evidence. The named destination is PostHog Cloud EU. Source text asserts regional confinement, but provider-side processing and retention are not inspected. Anonymous event grouping by install ID is also distinct from an absence of all linkage: the document explicitly groups events from one install (SRC-1, `ANALYTICS.md`).

Capability surface, grant set and isolation must not be conflated. The surface advertised is AI conversation, capture/synthesis, reusable workflows, local markdown, team sync, Slack and voice. The stated grant defaults are optional connections off and provider credentials supplied through setup; the actual enabled connections for any deployment are unknown. Local storage and keychain use describe placement, not a sandbox or deployed isolation envelope. No inspected code establishes filesystem scope, subprocess privileges or network confinement (SRC-1, `README.md`, `RELEASE_NOTES_v0.1.0-beta.md`).

### Change admission and operating modes

Knowledge admission is user capture followed by Sig synthesis, then a separate per-content human approval for team publication. Human initiation of capture is not proof of human approval of every local write. [RT-RTE-capture-share](#rt-rte-capture-share) distinguishes these decisions. Shared skills admit reusable workflows to teammates' installations, but their creation, review, replacement and execution rules are unresolved in [RT-RTE-skill-sync](#rt-rte-skill-sync).

The public issue forms collect problem reports and feature requests; they are not a software-production or automatic self-update mechanism. [RT-RTE-product-feedback](#rt-rte-product-feedback) ends at intake, not an admitted product change. Analytics policy changes require modifying the app allowlist and the document, but the implementer, review gate, release process and rollback mechanism are not supplied (SRC-1, `ANALYTICS.md`). These paths provide no basis for a claim of autonomous improvement or a theory-building loop.

The described operating mode is open user requests and reusable task workflows, not an inspected curriculum or bounded experiment. No expected-answer oracle, candidate-comparison implementation or correctness checker is disclosed. Observability is limited to the declared telemetry categories and public reporting forms; counts of success and elapsed time do not establish correctness or causal benefit. Performance measurements, retries, model fallback, scheduling and admission recovery remain uninspected.

## Shared records

### Components

#### RT-CMP-ai-provider
Label: Chosen AI provider

The documentation names Claude, ChatGPT and Gemini, with Copilot only forthcoming. Identity is provider family, not a pinned model (SRC-1, `README.md`, `RELEASE_NOTES_v0.1.0-beta.md`). The model's operative representational form is distributed-parametric; provider-side storage, exact models, parameter changes during operation and endpoint mutability are uninspected. No version pin is disclosed, so reproducibility or fixed weights cannot be concluded. This is an external dependency, not a Sig implementation inspected here.

> **Works with the AI you already have** — Claude, ChatGPT, Gemini today; GitHub Copilot coming soon. Sig is the context layer under your AI tools, not another subscription to choose between
> --- `README.md`

### Operative objects

#### RT-OBJ-skills
Label: Reusable skills

Source-native skills are reusable workflows such as 1:1 preparation, weekly updates and call debriefs. SRC-1, `README.md` declares git-backed team sharing. Exact representation, file layout, storage location, executable versus interpreted parts, invocation context and versioning are uninspected; the word skill alone does not establish any of them. This object denotes the reusable workflow material, not the private captures or shared meeting record.

> **Skills sync the same way** — reusable workflows (1:1 prep, weekly updates, call debriefs) shared with your team in one click. Non-technical users never see the git layer
> --- `README.md`

### Routes

#### RT-RTE-capture-share
Label: Capture synthesis and team publication

SRC-1, `README.md` describes user narrative → private structured note → organizational draft → user review/send → central team knowledge → teammate context. Local retention is plain markdown in a user-selected directory; natural-language narrative is interpreted by Sig and the user, while the synchronization protocol is unspecified beyond git. The user supplies the problem and can veto the proposed share. Sig proposes the synthesized and organizational text. Which transformations use a model, and how facts are separated from observations, remain opaque.

> Every capture goes through three stages:
>
> 1. **Capture** — after a meeting, talk through what happened. Raw, unfiltered, shorthand and all.
> 2. **Synthesis** — Sig structures your private notes: facts separated from your personal observations, stored only on your machine.
> 3. **Share** — Sig prepares a clean, org-level version. You review the exact text before anything leaves your machine. You decide what to include. Then you click send.
> --- `README.md`

> **Team knowledge with one click** — share what's worth sharing to a central knowledge base your whole team draws from. Your teammate's Sig has it as context immediately — git handles the sync in the background, invisibly
> --- `README.md`

- Immediate return: A structured private note, then a proposed organizational version for human review; UI timing is unspecified.
- Later read-back: Team knowledge is claimed to reach a teammate's Sig as context; private history is advertised as later AI context, with selector and request payload unknown.
- Delegated visibility: Approved organizational content reaches the team; the personal layer is declared local only. No agent delegation boundary is documented.
- Selection predicate: The user decides what to include in the share; automatic context selection is uninspected — no selector is supplied.
- Invalidation or expiry: uninspected — deletion of local files is allowed, but remote retraction, stale-context invalidation and synchronization tombstones are not described.
- Activation or effect: Claimed local note retention and team publication; actual downstream behavioral change is not observed.
- Evidence limits: Documentation only; no prompts, executable gate, sync trace, conflict behavior or demonstrated benefit.
- documentation conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected

Admission: Capture triggers a local knowledge write; Sig supplies structured text, but per-write local approval is not specified. The organizational draft has a stated human content-review/veto step before send. Guidance is the facts/personal-layer separation and org-level sharing policy quoted above. The private note and approved team text persist; the draft's lifetime is unknown. Rollback/recovery is uninspected beyond the user's ability to delete local files. No answer oracle is disclosed; a human review is not a reference-answer test. Operating mode is open user capture, not a documented improvement curriculum.

#### RT-RTE-provider-message
Label: Direct provider message

The user sends a message; Sig contacts the chosen provider from the user's computer using a key held in the OS keychain. The documented owner of transport is Sig; the provider owns external inference. Source: SRC-1, `README.md`; the load-bearing passage is retained in [RT-CLM-provider-direct](#rt-clm-provider-direct).

- Immediate return: A conversational response is implied; the response protocol and completion contract are uninspected.
- Later read-back: uninspected — documentation does not specify transcript reload or which retained material enters this particular message.
- Delegated visibility: The chosen provider receives messages; exact payload, retained-context subset and provider retention are uninspected.
- Selection predicate: User selects a provider and sends a message; model and context selection policies are not disclosed.
- Invalidation or expiry: uninspected — credentials revocation, provider retention and conversation expiry are not specified.
- Activation or effect: Claimed direct outbound request, without Sig proxying; no observed request or response supplied.
- Evidence limits: Provider internals, transport implementation, retry/fallback paths and actual credential access are unavailable.
- documentation conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected

#### RT-RTE-skill-sync
Label: Team skill synchronization

The declared endpoints are reusable workflows on one installation and teammates' installations, with git handling background sharing. The user initiates one-click sharing; Sig and git perform the otherwise opaque progression. Evidence: SRC-1, `README.md`, quoted in [RT-OBJ-skills](#rt-obj-skills).

- Immediate return: uninspected — one-click sharing is advertised but no acknowledgment or completion semantics are supplied.
- Later read-back: Reusable team workflows are intended for later use; loading, selection and exact consumed representation remain uninspected.
- Delegated visibility: Shared skills reach the team; executable permissions and visibility outside the team are uninspected.
- Selection predicate: User chooses to share; recipient activation and invocation rules are not specified.
- Invalidation or expiry: uninspected — replacement, revocation, pinning and conflict resolution are not described.
- Activation or effect: Claimed skill synchronization; receiving a skill does not establish execution or behavioral compliance.
- Evidence limits: No skill body, loader, executor, permission model, review gate or execution trace is supplied.
- documentation conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected

Admission: The trigger is user sharing of a reusable workflow, and the proposed change is workflow availability to the team. Author/proposer, per-content review, recipient veto, rollback and recovery are uninspected. The advertised task examples guide intended use, not an inspected instruction body. What persists is shared workflow material; its encoding and execution authority remain unresolved. Operating mode is reusable user-task workflows; no answer oracle, comparison process or improvement trigger is disclosed. This route cannot establish capability expansion through arbitrary code.

#### RT-RTE-analytics-egress
Label: Analytics and explicit feedback egress

Sig is the declared event producer; PostHog Cloud EU is the destination. Automatic usage/crash events and explicit comment submission are distinct inputs within this channel. The app's allowlist is the claimed gate, not inspected code (SRC-1, `ANALYTICS.md`).

> Anything not on the allowlist enforced inside the app is dropped before it leaves your computer.
> --- `ANALYTICS.md`

> If you click a feedback button or submit a comment from the feedback surfaces, that comment text is sent. Each of those buttons states this directly before you click. Nothing else you type ever leaves your machine via analytics.
> --- `ANALYTICS.md`

> There is no in-app toggle to turn analytics off today. We may add one in the future.
> --- `ANALYTICS.md`

- Immediate return: uninspected — event acknowledgment and feedback confirmation are not specified.
- Later read-back: Events are said to support crash investigation and prioritization; no automatic app read-back or resulting product revision is established.
- Delegated visibility: Analytics backend receives allowed events, and submitted comments explicitly include their text.
- Selection predicate: Claimed in-app allowlist; feature categories, aggregate totals, connection state and sanitized errors are listed. Feedback text requires explicit submission.
- Invalidation or expiry: Resetting install ID breaks subsequent linkage to prior events according to the document; event deletion and retention periods are uninspected.
- Activation or effect: Claimed outbound diagnostics and event grouping by random install ID, not demonstrated product improvement.
- Evidence limits: No emitter, sanitizer, allowlist implementation, backend trace or regional-processing audit is supplied.
- documentation conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected

The comment-submission decision is human; automated emission is not per-event human approval. This route is intake, not evidence of admitted production changes. For future event/property additions, the stated guidance is updating both the in-app allowlist and documentation; proposal owner, veto, release gate and rollback remain uninspected.

#### RT-RTE-product-feedback
Label: Public product feedback intake

The repository supplies GitHub bug and feedback forms. The human reporter provides context, observed friction and optional suggestions; GitHub hosts the submission. This is an inspectable form definition, not an inspected app-production loop (SRC-1, `.github/ISSUE_TEMPLATE/feedback.yml`, `.github/ISSUE_TEMPLATE/bug_report.yml`, `.github/ISSUE_TEMPLATE/config.yml`).

> label: What were you trying to do?
> description: The situation matters more than the suggestion. Tell us what you were trying to get done.
> --- `.github/ISSUE_TEMPLATE/feedback.yml`

> label: I've reviewed my report and removed any private meeting content, names, or notes I don't want public.
> --- `.github/ISSUE_TEMPLATE/bug_report.yml`

- Immediate return: A public issue is the intended endpoint; actual GitHub execution and submission acknowledgment are unobserved.
- Later read-back: uninspected — no mechanism connects a submitted issue to an admitted build or later application invocation.
- Delegated visibility: Public issue readers can see submitted content; the bug form requests a privacy check rather than implementing content sanitization.
- Selection predicate: Reporter chooses bug or feedback intake; feedback context/friction and bug version/problem fields are required by the form definitions.
- Invalidation or expiry: uninspected — issue retention, withdrawal and downstream processing are outside these forms.
- Activation or effect: Forms afford structured product feedback; no accepted change or repair is established.
- Evidence limits: Form YAML is inspectable, but GitHub hosting behavior, maintainer decisions and build/release machinery are not supplied.
- implementation conclusion status: afforded
- operation conclusion status: uninspected

Admission boundary: The user proposes a problem or idea, not an executable product revision. Human maintainer admission/veto, implementation guidance, rollback and recovery are uninspected. The retained result would be an issue, not automatically changed product behavior. Operating mode is open feedback. A reporter's expected-versus-actual account is evidence input, not an implemented answer oracle. No inference of self-improvement follows from intake alone.

### Claims

#### RT-CLM-private-sharing
Label: Local personal layer and approved sharing

SRC-1, `README.md` declares a local-only personal layer and explicit approval before team sharing:

> **Your thinking, not just the facts** — Sig saves two things: the factual record, and your personal layer — your read on what it means, your honest take. The personal layer stays on your machine and is never shared
> --- `README.md`

> Nothing reaches your team without your explicit approval. That's the whole mechanism.
> --- `README.md`

Owner: Sig. Enforcement point: proposed exact-text review/send gate. Guarantee strength: policy. Covered path: organizational publication in [RT-RTE-capture-share](#rt-rte-capture-share). Alternate outbound paths include provider messages, analytics comments and public issue submissions; their differing purposes prevent reading this as a universal no-egress assertion. External contracts: OS storage/access control and team repository confidentiality. Whether model requests include personal content is unresolved; local retention alone does not prove it stays out of inference payloads.

- documentation conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected

#### RT-CLM-provider-direct
Label: Direct provider traffic and keychain credentials

SRC-1, `README.md` supplies the transport and credential claim:

> **Your messages go to your provider directly.** When you send a message, Sig talks to your chosen AI provider (Claude, ChatGPT, etc.) from your computer. We don't proxy, log, or intercept those requests. Your provider keys live in your computer's secure keychain.
> --- `README.md`

Owner: Sig for client transport and key access; provider and OS for external execution and storage contracts. Enforcement point: claimed direct client request path and secure keychain; neither inspected. Guarantee strength: policy. Coverage: user messages, not a proven enumeration of synthesis, integration, telemetry or tool requests. This limits claims of universal provider routing, credential isolation or provider-side privacy.

- documentation conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected

#### RT-CLM-telemetry-filter
Label: Telemetry allowlist and sanitation

SRC-1, `ANALYTICS.md` claims filtering before egress, sanitization of raw errors and an EU endpoint. The filtering passage and feedback exception are retained in [RT-RTE-analytics-egress](#rt-rte-analytics-egress).

> - Raw error messages. They're sanitized: emails, URLs, and home-directory paths are stripped, and they're truncated.
> - Stack traces with real paths. Your home directory becomes `<home>`; your Sig folder becomes `<profile>`.
> --- `ANALYTICS.md`

Owner: Sig for pre-send filtering; PostHog for external service behavior. Enforcement point: app allowlist and error sanitization before transmission. Guarantee strength: policy. Coverage: analytics, not provider requests or team sharing. Explicit feedback submission sends comment text; therefore blanket exclusion of all user-entered text is not warranted. No implementation or observed payload establishes sanitizer completeness, regional confinement or anonymity against all reidentification.

- documentation conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

none
