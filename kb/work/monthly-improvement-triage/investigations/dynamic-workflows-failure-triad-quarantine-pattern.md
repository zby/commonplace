# Investigation: dynamic-workflows failure-mode triad and quarantine pattern

## The gap under test

`kb/work/connect-maintenance-observations/README.md`: "Dynamic-workflows source lacked an ingest; the failure-mode triad and quarantine pattern had no note home. `a-harness-for-every-task-dynamic-workflows.ingest.md` now exists and preserves those gaps as extractable values. Decide whether to write notes for single-context failure modes and orchestration quarantine." Carried forward verbatim into `kb/work/monthly-improvement-triage/README.md`.

## What I read

- `kb/sources/a-harness-for-every-task-dynamic-workflows.ingest.md` (full) — the ingest report, including its own "Limitations (our opinion)" section.
- `kb/sources/a-harness-for-every-task-dynamic-workflows.md` (full) — the underlying X-thread snapshot: Thariq Shihipar and Sid Bidasaria's practitioner account of Claude Code's dynamic workflows.
- `kb/sources/claude-code-dynamic-workflows-docs.md` and its ingest — checked for corroboration of the failure-mode triad; neither mentions laziness, self-preferential bias, goal drift, or compaction at all.
- `kb/notes/COLLECTION.md` — reach test, theory-independence constraint, title/composability rules.
- Existing notes checked directly: `topology-isolation-and-verification-form-a-causal-chain-for-reliable.md`, `agent-runtimes-decompose-into-scheduler-context-engine-and-execution.md`, `the-four-field-record-exposes-an-efficiency-security-and-sovereignty.md`, `error-correction-works-above-chance-oracles-with-decorrelated-checks.md`, `agent-orchestration-needs-coordination-guarantees-not-just.md`, `compiling-coordination-preserves-primitive-not-aggregate-authority.md`, `kb/agentic-systems/claude-code-dynamic-workflows.md`, `kb/agentic-systems/gbrain.md`, `kb/notes/failure-modes-README.md`, `kb/notes/llm-interpretation-errors-README.md`.
- A fork (general-purpose sub-agent) independently searched `kb/notes/` and `kb/agentic-systems/` by term (`laziness`, `self-preferential`, `goal drift`, `compaction`, `context rot`, `quarantine`, `privilege`, `untrusted`) and by the specific candidate host notes named above; its findings corroborate the manual reads below.

## What the source actually says

**The failure-mode triad.** From the source directly: "the longer Claude works on a complex task in a single context window, the more it becomes susceptible to a few specific failure modes: Agentic laziness ... [stopping] before finishing a particularly complex, multi-part task and declar[ing] the job done after partial progress ... Self-preferential bias ... Claude's tendency to prefer its own results or findings, especially when asked to verify or judge them ... Goal drift ... the gradual loss of fidelity to the original objective across many turns, especially after compaction. Each summarization step is lossy, and details like edge-case requirements or 'don't do X' constraints can get lost." The claimed remedy: "orchestrating separate Claudes with their own context windows and focused, isolated goals" combats all three. No measurement, no baseline, no ablation is offered for any of the three, or for the claim that isolation fixes them — this is asserted, not shown, and the ingest's own Limitations section says so plainly ("Naming is not explaining ... treat the triad as a sharable diagnosis, not a validated causal model").

**The quarantine pattern.** From the "Triaging at scale" section: "A useful pattern for triage workflows is quarantine. This involves barring the agents that read untrusted public content from taking high-privilege actions, which are instead done by the agents in charge of acting on the information." One sentence, one use case (support-queue/incident triage), no further elaboration, no measurement of how much it reduces successful injection.

## Existing KB coverage

Direct term search for `laziness`, `self-preferential`, `goal drift`, `compaction`-as-constraint-loss, `quarantine`, and `privilege separation` across `kb/notes/` and `kb/agentic-systems/` returns nothing — the ingest's own claim that "no KB note names these three crisply" and that "no security-of-orchestration ('quarantine') home note exists" both check out. Nothing in `failure-modes-README.md` (scoped to KB-knowledge-activation failures, a different subject) or `llm-interpretation-errors-README.md` (scoped to prompt/sampling/interpreter deviation, also different) covers either gap.

The closest neighbors, read in full:

- `topology-isolation-and-verification-form-a-causal-chain-for-reliable.md` — status `speculative`, argues decomposition→isolation→verification is a dependency chain, using a *different* source (Tu 2026) as its causal argument. It does not name or cite this dynamic-workflows source anywhere, and does not name the triad.
- `agent-orchestration-needs-coordination-guarantees-not-just.md` — names a *different*, non-overlapping four-item taxonomy (contamination, inconsistency, amplification, accountability vacuum) for missing coordination *primitives*, explicitly framed as "these are not four names for one bug ... each requires a different primitive."
- `error-correction-works-above-chance-oracles-with-decorrelated-checks.md` — discusses LLM-as-judge decorrelation generically (a judge's failure modes should differ from the generator's) but never names "self-preferential bias" or ties it to context length.
- `the-four-field-record-exposes-an-efficiency-security-and-sovereignty.md` — states the general security-risk question ("does anything untrusted ... reach a high-authority channel?") but has no quarantine/privilege-separation content.
- `compiling-coordination-preserves-primitive-not-aggregate-authority.md` — argues per-call permission scoping doesn't bound *aggregate* effect volume in compiled orchestration. Adjacent vocabulary (authority, delegation), different question (capacity/authority coupling, not read-vs-act trust separation).
- `kb/agentic-systems/claude-code-dynamic-workflows.md` — the existing shipped-system analysis note for this exact source. Covers the API surface, withheld decisions, and promotion path in depth; does not mention the triad or quarantine at all.
- `kb/agentic-systems/gbrain.md` — not previously connected to this source, but describes an independent, source-inspected system that implements essentially the same read/act privilege split (see verdict below).

Both gaps are genuine: nothing already states either claim, and nothing is close enough to make either a natural graft onto an unrelated argument.

## Reach test, applied per item

### Item A: the single-context failure-mode triad

Applying the reach test ("change one premise — can you predict the change in the conclusion?"): the three named modes do not share one mechanism, and this matters because the KB's own coordination-guarantees note explicitly warns against packaging unrelated failure modes as one bug. Checking each against "grows with single-context length":

- **Goal drift** is specifically about information *loss* — lossy compaction dropping "don't do X" constraints. This is a straightforward, well-motivated consequence of long single-context runs and connects cleanly to context-rot/soft-degradation material already in the KB (`agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md`), though that note is about volume/interference, not compaction-specific constraint loss.
- **Agentic laziness** (declaring partial work done) is plausibly correlated with task complexity and turn count, but the source gives no mechanism for *why* a long context specifically induces premature stopping rather than, say, a hard task alone doing so regardless of context length.
- **Self-preferential bias** is conceptually a *same-context-anchoring* effect (the judge is biased toward reasoning/output already visible in its own context), not obviously a function of context *length* — a short single-turn self-judgment call would plausibly show the same bias. Bundling it into "grows with length" alongside goal drift (which is genuinely a length effect) conflates two different claims under one banner.

This is the same failure pattern this triage has already caught and dismissed six times this month for other items: a source-level framing that reads as one coherent finding but, on inspection, packages phenomena with different actual mechanisms. The theory-independence constraint also cuts against a standalone note here: this is the *only* source in or out of the KB investigation that states this triad as a unit (the companion official-docs source and ingest for the same feature never mention it), so there is no second source to corroborate the triad-as-such — only the sourced label survives if the framing is removed, not an independently-supported mechanism.

**Verdict: DISMISS** (as a candidate for a standalone note asserting the triad as a unified mechanism). The individual named concepts (self-preferential bias in same-context judging, compaction dropping negative constraints) may have standalone citable value as small, separately-scoped additions to notes that already discuss adjacent territory (LLM-as-judge decorrelation for the former, context-rot/soft-degradation for the latter) — but that is future, separately-scoped work, not something this investigation authorizes or performs, since folding two-thirds of an already-shaky triad into unrelated notes' existing arguments without their own justification would be scope creep beyond what this investigation earned. No action taken on Item A beyond this write-up.

### Item B: the orchestration-quarantine pattern

Applying the same test: is this a general, transferable claim, or a one-off product-feature description? The general form — deny a role that processes untrusted/attacker-reachable content any high-privilege action, and route privileged actions through a separate role that only consumes already-vetted, structured output — is the classic security-engineering principle of privilege separation applied specifically to LLM multi-agent orchestration (where the confused-deputy risk is prompt injection via untrusted content). It passes "would the insight apply in a different domain?" cleanly — it predates LLM systems and is a named pattern in classical systems security (e.g. privilege-separated daemons).

Critically, this does **not** rest on the dynamic-workflows source alone. `kb/agentic-systems/gbrain.md` (already in the KB, source-inspected, unconnected to this ingest before this investigation) independently documents the same split: GBrain's operations layer classifies every remote/agent-facing caller as untrusted at the API boundary — including the host agent GBrain otherwise instructs carefully in prose — with write/admin operations withheld regardless of what the agent's own skill prose claims. This satisfies the theory-independence constraint: the claim survives removal of either source, because the other still witnesses it.

It also connects productively to two already-accepted notes rather than sitting in isolation: `compiling-coordination-preserves-primitive-not-aggregate-authority.md`'s finding that per-call permission scoping cannot bound aggregate reachable effect (explaining architecturally *why* the boundary has to move to the agent-role level, not just to a tighter tool allowlist), and `the-four-field-record-exposes-an-efficiency-security-and-sovereignty.md`'s standing security-risk question (quarantine is one concrete architectural answer, available specifically when the untrusted-exposed role is known in advance).

**Verdict: WRITE-NOTE.**

## Note written

`kb/notes/orchestration-needs-privilege-quarantine-not-permission-scope.md` — "Agent orchestration needs a privilege quarantine, not just a permission scope." `status: seedling`, `traits: [title-as-claim, has-external-sources]`, `tags: [computational-model, tool-loop]` (matching the existing cluster's tag usage, no new tag introduced).

Claim scope: when an orchestrated agent's context includes untrusted content, the defense is denying that agent's role a high-privilege action entirely (a role-level trust boundary), not finer per-call tool permission scoping — because a per-call check authorizes an action, not the provenance of the content that steered it. Grounded in two independent instances (the dynamic-workflows triage pattern; GBrain's remote-untrusted operations layer), connected to the aggregate-authority and four-field-security-risk notes, and explicitly scoped: quarantine relocates risk (to the actor's blind trust in the reader's structured output) rather than eliminating it, and its effectiveness is untested in both witnessed sources.

`commonplace-validate` result: clean PASS (title 77 chars, filename slug 61 chars, all links resolve, schema satisfied). No edits were needed after validation.

## Compression gate review

Run per `kb/work/agent-note-improvement/run-compression-bundle-on-note.md` by a fresh sub-agent given only the note's full text and the concatenated four-gate packet (core-claim-obscured, branch-bloat, detail-overhang, marginal-value-redundancy), blind to this investigation's reasoning. Full report: `kb/work/monthly-improvement-triage/investigations/dynamic-workflows-failure-triad-quarantine-pattern-compression-review.md`.
