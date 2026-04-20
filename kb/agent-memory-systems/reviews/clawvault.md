---
description: TypeScript vault memory (now v3.5, deprecated in favor of OpenClaw native memory) with write-time fact extraction, a typed observation ledger, scored promotion, hybrid search, and OpenClaw memory-slot plugin
type: kb/agent-memory-systems/types/agent-memory-system-review.md
traits: [has-comparison, has-implementation]
status: current
tags: [related-systems, trace-derived]
last-checked: "2026-04-12"
---

# ClawVault

ClawVault is a TypeScript CLI and OpenClaw plugin that treats a local markdown vault as a structured memory backend for AI agents. It bundles session lifecycle commands (`wake`, `checkpoint`, `sleep`, `recover`), a typed observation ledger compressed from session transcripts, a write-time fact store with conflict resolution, a hybrid BM25+embedding+rerank search engine, context profiles that assemble prompts from five vault sources, and a set of background maintenance workers (Curator, Janitor, Distiller, Surveyor). It is authored by Versatly and, as of the April 2026 head commit, the README and docs explicitly deprecate it for new deployments in favor of OpenClaw's first-party memory stack — the repo remains maintained for legacy installs and as a plugin-based memory slot.

**Repository:** https://github.com/Versatly/clawvault (v3.5.2, Node 18+, 466+ tests, built as an OpenClaw `memory` slot plugin)

## Core Ideas

**Two-layer capture: typed memory writes and a scored observation ledger.** The `capture` subsystem (`src/capture/extractor.ts`) pulls typed memories directly out of assistant turns via `<memory_note>` tags and heuristic sentence classification, writing into category folders (`decisions/`, `preferences/`, `facts/`, `lessons/`, `people/`). In parallel, the `observer` pipeline (`src/observer/observer.ts`) watches session JSONL files, tracks per-session byte offsets in `.clawvault/observe-cursors.json`, compresses new content through a provider-agnostic LLM into scored observation lines (`[type|c=0.9|i=0.85] content`), and routes them through `Router.route()` into dated ledgers. Compression vs. capture are separate code paths with separate triggers.

**Eleven-type observation taxonomy with regex noise filters.** `OBSERVATION_TYPES` in `src/lib/observation-format.ts` has expanded beyond the original decision/preference/lesson set to eleven values: `decision`, `preference`, `fact`, `commitment`, `task`, `todo`, `commitment-unresolved`, `milestone`, `lesson`, `relationship`, `project`. Compression is also defensive rather than just generative: `src/observer/compressor.ts` hardcodes a `NOISE_PREFIX_RE`, `STRUCTURED_NOISE_MARKER_RE`, `ACK_ONLY_RE`, `ROUTINE_MAINTENANCE_RE`, and a `BASE64_DATA_URI_RE` scrubber so tool-result wrappers, base64 blobs, and "ok, got it" turns never enter the ledger.

**Scored promotion with a superseding fact store.** Importance thresholds (`IMPORTANCE_THRESHOLDS = { structural: 0.8, potential: 0.4 }`) drive observation promotion: `i >= 0.8` promotes immediately, `i >= 0.4` promotes if seen on two different dates, below that is context-only. Orthogonally, `src/lib/fact-store.ts` maintains a write-time `(entity, relation, value, validFrom, validUntil)` log in `.clawvault/facts.jsonl` with conflict resolution: when a new fact matches an existing one on entity+relation, the old fact's `validUntil` is set and the new fact replaces it in the indexed hot set. Facts therefore get bitemporal supersession, while observations get date-based recurrence promotion — two different lifecycle models living in the same vault.

**Context profiles as named retrieval strategies with a cheap classifier.** `src/lib/context-profile.ts` defines four resolved profiles (`default`, `planning`, `incident`, `handoff`) and an `auto` value. The `auto` path runs three hardcoded regexes (`INCIDENT_PROMPT_RE`, `PLANNING_PROMPT_RE`, `HANDOFF_PROMPT_RE`) against the task string and picks a profile in a fixed priority order — no LLM involved. Each profile tunes which of the five vault sources (daily notes, observations, fact store, graph neighbors, project files) enters the prompt and in what order, fit to a token budget.

**OpenClaw memory-slot plugin with in-process hooks.** `src/openclaw-plugin.ts` registers ClawVault as a `memory` slot plugin against an `OpenClawPluginApi`. It attaches to `before_prompt_build` (priority 30), `message_sending` (priority 20), `gateway_start`, `session_start`, `session_end`, `before_reset`, `before_compaction`, and `agent_end`, and registers two tools — `memory_search` and `memory_get`. The 3.5.0 release explicitly moved these hooks from CLI shell-outs to direct library calls on `ClawVault.find()` and `buildSessionRecap()` to eliminate SQLite lock contention. The plugin surface, not the CLI, is now the canonical integration path.

**Background maintenance workers as a first-class subsystem.** `src/lib/maintenance/` defines four workers run by `clawvault maintain`: Curator (organizes captures), Janitor (cleans), Distiller (`distiller-worker.ts` — extracts facts/decisions/lessons from inbox items over 80 words, writing `distilled-<hash>.md` files), and Surveyor (`surveyor-worker.ts` — globs the vault, counts link coverage, and writes a dated `surveyor-report.md` with recommendations). Each worker is a function taking a `WorkerExecutionContext`, a `MaintenanceState`, and an `WorkerLlmClient`, with explicit dry-run support and per-run action logs. This is structurally close to the "boiling cauldron" mutations — but scheduled, not event-driven, and partially LLM-dependent.

**Deprecation in favor of OpenClaw native memory is the current framing.** The head README carries a prominent deprecation warning; `docs/openclaw-plugin-usage.md` is now a migration guide pointing at OpenClaw's builtin memory and QMD memory engines. The repo still ships plugin wiring and publishes to npm, but the project's stated position is that the good ideas were absorbed upstream and new deployments should use OpenClaw's first-party memory stack. This substantially changes how to read ClawVault as a reference: less as a product to evaluate, more as a frozen experiment whose mechanisms are public and readable.

## Comparison with Our System

**Two layers of structure vs. one.** ClawVault separates workshop-layer artifacts (session handoffs, checkpoints, observation ledgers, inbox captures) from library-layer artifacts (`decisions/`, `lessons/`, `preferences/`, fact store). We have the library layer (`kb/notes/`, `kb/reference/`) and a workshop layer (`kb/work/`), but the library-to-workshop boundary is still mostly about lifecycle and not about type. ClawVault additionally enforces a typed taxonomy on the workshop side (eleven observation types) that we have no equivalent for — our workshop is prose-shaped.

**Retrieval preassembly vs. agent-driven navigation.** ClawVault's `context --profile` command pre-assembles a token-budgeted bundle from five sources before the agent speaks. Our position — [instruction specificity should match loading frequency](../../notes/instruction-specificity-should-match-loading-frequency.md) and [always-loaded context has two surfaces](../../notes/always-loaded-context-mechanisms-in-agent-harnesses.md) — keeps the always-loaded surface small and trusts the agent to search. ClawVault bets that a cheap classifier plus hardcoded profile shapes can pick relevance better than a model navigating on its own; we bet that a small routing prompt plus good descriptions scales better as the KB grows.

**Separate lifecycles for facts vs. observations.** The fact store's bitemporal supersession (`validFrom`, `validUntil`) is a real lifecycle model for structured facts, distinct from the observation ledger's recurrence-based promotion. Our notes have neither: we track status (`seedling`, `current`, `outdated`) manually per note, without per-claim validity intervals or automatic conflict resolution. For durable-note-level assertions this may be fine; for fast-moving observational facts it is a gap.

**Automated maintenance workers vs. reviewed sweeps.** ClawVault runs Distiller and Surveyor on a schedule, generating artifacts without human authorship in the loop. We run semantic review bundles and batch sweeps, but every write into the library goes through a human or through an agent we review. The tradeoff is visibility: their workers produce artifacts continuously; our reviews produce artifacts deliberately. ClawVault accepts more noise in exchange for not losing signal.

**Deprecation narrative vs. methodology accumulation.** ClawVault is now a maintained legacy repo whose best ideas have been absorbed into OpenClaw's memory stack. Our position is opposite: we accumulate methodology in the repo itself as theory, and the theory is the product. That means a ClawVault-style deprecation does not apply to us — but it also means we cannot benefit from the "merged into a host runtime" consolidation path that made ClawVault's v3 architecture cheap to abandon.

## Borrowable Ideas

**1. Noise-prefix filters in transcript compression.** `NOISE_PREFIX_RE`, `ACK_ONLY_RE`, `STRUCTURED_NOISE_MARKER_RE`, and `BASE64_DATA_URI_RE` in `compressor.ts` are a concrete defensive layer we currently lack. If we add any form of trace-derived capture, these regex classes are a zero-cost filter we can copy almost verbatim. Ready to borrow the day we start consuming session logs.

**2. Bitemporal facts for fast-moving operational claims.** The `(entity, relation, value, validFrom, validUntil)` schema with supersede-on-conflict is a compact, inspectable lifecycle. This would not replace our prose notes, but it fits a narrow class of claims we currently handle inconsistently — tool versions, config values, owner assignments, status of external systems. Needs a concrete use case before adopting; premature now.

**3. Named retrieval profiles with a keyword-based selector.** The `auto` profile's three-regex classifier is the smallest interesting mechanism in the codebase. If we ever build task-kind-aware retrieval, starting with hardcoded regexes over task strings (rather than an LLM classifier) keeps the system inspectable and cheap. The profiles themselves are less borrowable — the right profiles depend on what work the system does.

**4. A distiller-style worker as a contained experiment.** The Distiller's pattern — read inbox items above a word threshold, route into `distilled-<hash>.md` files in typed categories, keep a per-run action log — is a self-contained automation we could mirror for log entries we never promote. The bounded scope (inbox only, fixed categories, idempotent hash-based output) makes it safer than a general-purpose auto-promoter. Needs a real accumulation of unpromoted log entries first.

**5. Explicit noise filtering for acknowledgment turns.** Separate from transcripts, `ACK_ONLY_RE` captures a broader lesson: some turns carry no durable signal at all and should be filtered before any extraction considers them. If we ever review our own log entries for patterns, an ack-class filter that drops "ok / got it / sounds good" entries is a first-pass win.

## What We Should Not Borrow (Yet)

**Preassembled context bundles.** ClawVault's `context` command pre-loads the prompt from five sources before the agent speaks. We have chosen the opposite strategy, and until we have evidence that agent-driven navigation misroutes a meaningful fraction of queries, frontloading would just burn tokens on guessed relevance.

**Scheduled LLM maintenance workers.** The Distiller and Surveyor make LLM calls on a timer and write artifacts without a review gate. We do not have the volume to justify this yet, and automation-before-understanding is a related oracle/evaluation gap [automating-kb-learning-is-an-open-problem](../../notes/automating-kb-learning-is-an-open-problem.md) warns about.

**The eleven-type observation taxonomy as a library-level type.** The types are useful as workshop tags; they are not fundamental categories of knowledge. Imported wholesale, they would conflict with our existing type system and muddy the `note` vs. `structured-claim` vs. `adr` distinctions.

**`c=`/`i=` float scoring.** The scored observation format (`[type|c=0.9|i=0.85]`) implies LLM-extractable precision we do not believe exists. The buckets (structural/potential/contextual) are the honest abstraction; the floats are cosmetic. If we adopt anything here, it should be the buckets.

## Curiosity Pass

**The workshop layer claim weakened once the OpenClaw deprecation landed.** The February reading of this system — "a working workshop where we have only theory" — is narrower now. ClawVault's workshop patterns are still concrete, but they also just shifted into OpenClaw's core. The signal is no longer "an independent system arrived at these primitives" so much as "these primitives graduated into a host runtime." That is still useful, but it is a different kind of evidence.

**The fact store does real work; the observation ledger mostly relocates data.** The fact store's supersession logic genuinely transforms inputs — incoming facts trigger lifecycle changes on existing records. The observation ledger, by contrast, mostly reorganizes and filters: compress session turns into typed lines, route into dated files, promote by recurrence. The transformation is small; the value is in the filtering. Useful to be clear which half of the system earns its complexity.

**The `auto` context profile is weaker than it looks.** Three regexes over a task string will misclassify any task that does not self-declare its kind. The profile system still provides value for explicitly-invoked profiles (`--profile incident`), but the "automatic" intent inference is a cheap heuristic, not a real classifier. Honest in the code, slightly oversold in the docs.

**Maintenance workers produce artifacts the system does not read back.** The Surveyor writes a report; nothing in the codebase consumes that report as input to later decisions. The Distiller's output goes into category folders that do feed retrieval, so that loop closes. The Surveyor loop currently does not. That is not a bug, but it is a good example of an automated write path that looks like learning and is actually logging.

## Trace-derived learning placement

**Trace-derived learning placement.** ClawVault still qualifies as trace-derived, and the mechanisms we noted in the survey remain — but the API has broadened. *Trace source:* assistant turns (`captureTurn` in `src/capture/`), OpenClaw session JSONL files watched with per-session byte cursors, and OpenClaw plugin hook events (`before_compaction`, `agent_end`, `session_start`, `session_end`, `before_reset`). Triggers are per-turn for capture, size-threshold for observer compression, event-driven for plugin hooks, and scheduled (cron/weekly) for reflection and maintenance workers. *Extraction:* the typed-memory extractor (`src/capture/extractor.ts`) plus the eleven-type observation compressor (`src/observer/compressor.ts`), plus the write-time fact extractor (`src/lib/fact-extractor.ts`, rule-based or LLM) that produces `(entity, relation, value)` tuples with conflict resolution. The oracle is a mix of regex rules and LLM judgment, not benchmark-grounded. *Promotion target:* inspectable markdown plus a JSONL fact log — purely symbolic artifacts, no weights. Still stored as service-adjacent files under a vault path, not a hosted service. *Scope:* per-vault, cross-session; no cross-agent pooling. *Timing:* online capture/compression during deployment, staged weekly reflection cycles, offline background maintenance workers. On the [survey's axes](../trace-derived-learning-techniques-in-related-systems.md): axis 1 (ingestion pattern) — live session mining with event-driven and scheduled triggers; axis 2 (artifact vs weights) — symbolic artifacts only, no weight promotion. ClawVault continues to occupy the "live session mining into symbolic artifacts" quadrant. The new observation — write-time bitemporal facts as a separate lifecycle from recurrence-scored observations — is a useful refinement within the symbolic-artifact substrate: it *splits* the artifact-structure axis into "lifecycle-managed tuples" and "scored prose lines" at the same installation. That split is not yet captured as a subtype in the survey but would be worth one if another system shows the same pattern.

## What to Watch

- Whether OpenClaw's native memory stack absorbs ClawVault's remaining distinct mechanisms (fact store, recurrence-scored observations) or keeps them as legacy. That answers whether the mechanisms were the insight or the packaging was.
- Whether the maintenance workers (especially Surveyor) grow a consumer. Right now the Surveyor writes reports nothing reads back; if that loop closes, it becomes a real example of an automated review cadence.
- Whether the two-lifecycle split (bitemporal facts + recurrence-scored observations) proves stable or collapses back into a single model as OpenClaw absorbs both.
- Whether the `auto` context profile picks up a smarter classifier or stays as three regexes. The current setup is a useful reference point for "cheap-and-inspectable"; a shift to LLM classification would change the tradeoff.

---

Relevant Notes:

- [a-functioning-kb-needs-a-workshop-layer-not-just-a-library](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — ClawVault's typed observation ledger and session-handoff artifacts remain a concrete implementation of workshop-layer primitives, though now partially absorbed into OpenClaw's memory stack
- [claw-learning-loops-must-improve-action-capacity-not-just-retrieval](../../notes/claw-learning-loops-must-improve-action-capacity-not-just-retrieval.md) — the eleven observation types (decision, preference, commitment, todo, milestone, etc.) are a concrete taxonomy for action-oriented knowledge this note identifies as missing from retrieval-only systems
- [automating-kb-learning-is-an-open-problem](../../notes/automating-kb-learning-is-an-open-problem.md) — the Curator/Janitor/Distiller/Surveyor workers are a working (if partly LLM-dependent) implementation of the extract/synthesise/regroup mutations, with the Surveyor notably not yet read back
- [deploy-time-learning-is-the-missing-middle](../../notes/deploy-time-learning-is-the-missing-middle.md) — ClawVault automates promotion (recurrence thresholds, fact supersession) without a theory of when automation is premature; the v3 deprecation suggests at least some of that automation did not justify the complexity
- [always-loaded-context-mechanisms-in-agent-harnesses](../../notes/always-loaded-context-mechanisms-in-agent-harnesses.md) — ClawVault's profile-based preassembly contrasts with our two always-loaded surfaces; the regex-based `auto` selector is a cheap alternative to either extreme
- [instruction-specificity-should-match-loading-frequency](../../notes/instruction-specificity-should-match-loading-frequency.md) — frontloaded context bundles face the same tradeoff this note describes: specificity costs tokens that are paid whether the task needs them or not
