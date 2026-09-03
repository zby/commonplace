---
run-id: AAS-2026-09-03-academic-research-skills-02
lens: memory/context
packet-id: AAS-2026-09-03-academic-research-skills-02-MEM-P1
reviewed-boundary: 94436237913091d4739870159d241660527e8338
source-register: SRCREG-v1-94436237913091d4739870159d241660527e8338
canonical-register: CANON-v1-94436237913091d4739870159d241660527e8338
runtime-baseline-sha256: 29dadeea6a5b2e76fc9959f91a18dc9e70f1f9d70d43ff5aab0785ccb715d458
---

## Header verification

- Packet path: `/home/zby/llm/commonplace/kb/reports/state/agentic-system-analysis/AAS-2026-09-03-academic-research-skills-02/packets/memory-p1.md`
- Supplied packet SHA-256: `6d719519f501033d6c459958f28007c5b148e24e04c3c1cfae5cf5ce910941b9`
- Computed packet SHA-256: `6d719519f501033d6c459958f28007c5b148e24e04c3c1cfae5cf5ce910941b9`
- Digest verification: **PASS**.
- Seven-field header verification: **PASS**. All and only the expected fields were present, and their values matched the packet identity: `run-id`, `lens`, `packet-id`, `reviewed-boundary`, `source-register`, `canonical-register`, and `runtime-baseline-sha256`.
- Runtime-baseline digest verification: **PASS**. The computed digest was `29dadeea6a5b2e76fc9959f91a18dc9e70f1f9d70d43ff5aab0785ccb715d458`.

## Canonical annotations

### `OBJ-5` — Pipeline state, Material Passport, and append-only ledgers

- **Write agency:** Mixed. The prompt-layer orchestrator is instructed to freeze stage state, append reset/resume and compliance entries, preserve `audit_artifact[]`, and obtain the user-supplied Passport path, resume hash, branch choice, and any override. The deterministic `slr_lineage` reducer derives and preserves one Passport field by monotonic OR. The external host/model and human remain the agents that would perform the prompt-governed Passport transaction (`academic-pipeline/references/passport_as_reset_boundary.md:20-42,44-65`; `scripts/slr_lineage.py:31-59`).
- **Persistence and lineage:** Passport reset and compliance ledgers are user-project files with no TTL. Boundary/resume entries and stage re-runs preserve prior entries; version labels advance and prior entries are not deleted, reordered, or mutated. `slr_lineage: true` is preserved across resume even when reconstructed live stage state is empty. Within a run, immutable `dialogue_log_ref` pointers and append-only `collaboration_depth_history[]` retain stage interaction ranges and checkpoint observer reports for later checkpoint/Process Record consumption (`academic-pipeline/references/passport_as_reset_boundary.md:67-78`; `scripts/slr_lineage.py:46-59`; `academic-pipeline/agents/state_tracker_agent.md:26-32`; `docs/DATA_FLOWS.md:84-92`).
- **Invalidation and regeneration:** `verification_status: STALE|UNVERIFIED` requires a warning and re-verification before continuation. Audit entries are selected against the current `(stage, agent, deliverable_sha)` tuple and rechecked; current-byte drift or invalid/missing evidence falls back to a fresh audit path while historical entries remain. No automatic artifact regeneration follows merely from retained state (`academic-pipeline/references/passport_as_reset_boundary.md:59-65,112-125`).
- **Read-back direction:** Pull. A later orchestrator is instructed to load the user-named Passport, resolve one `kind: boundary` by hash, read referenced artifacts and verification state, and append a consuming resume record. Separately, the disclosure renderer reads the persisted `slr_lineage` value; the collaboration-depth observer/Process Record receives stored dialogue-range pointers and checkpoint-history entries (`academic-pipeline/references/passport_as_reset_boundary.md:44-65`; `scripts/slr_lineage.py:2-8`; `academic-pipeline/agents/state_tracker_agent.md:26-32`).
- **Selection signal and scope:** The user-pasted 12-hex `resume_from_passport` hash selects one unconsumed boundary; an optional explicit path selects the Passport. The selected entry's artifact references delimit restored material. If `pending_decision` exists, the user's exact option value selects its `next_stage` and `next_mode`; the boundary's `next` value is advisory in that case (`academic-pipeline/references/passport_as_reset_boundary.md:42,44-65`).
- **Delivery and consumption point:** Intended delivery is BAP-6/RTE-8: the Passport is the authoritative input for the resumed stage, including in-session continuation, and the selected artifacts are loaded by reference. `slr_lineage` has a narrower executable consumption point in the disclosure renderer (`academic-pipeline/references/passport_as_reset_boundary.md:39-41,59-65`; `scripts/slr_lineage.py:2-8`).
- **Context-presence status:** `claimed` for Passport material in a resumed orchestrator/model context. `wired` for the deterministic `slr_lineage` value supplied to its renderer. The frozen tree does not contain the external context builder or an executable general Passport context loader.
- **Activation status:** `uninspected`. There is no candidate-linked run showing that a host loaded the selected Passport material, that it changed a later model action, or that `slr_lineage` changed a delivered disclosure. Executable derivation and persistence do not establish behavioral activation.
- **Prevented conclusions:** ABS-1 and ABS-6 prevent treating the Passport protocol as an observed or fully wired restoration route. ABS-7 prevents treating SessionStart as Passport restoration. The sources also disclaim measured token savings (`academic-pipeline/references/passport_as_reset_boundary.md:120-125`).

### `OBJ-6` — Citation records, resolver outcomes, verification summaries, and cache rows

- **Write agency:** Automatic for resolver cache rows after a live computation; manual for `/ars-cache-invalidate`. Citation-verification rows are written by `VerificationCache.put`. The separate `RetractionStatusCache` is written only when a caller supplies a path, observation, resolver name, and timestamp (`scripts/verification_cache.py:102-180`; `scripts/retraction_status.py:407-463`).
- **Persistence and lineage:** The default citation cache is SQLite at `~/.cache/ars/verification.db` (or an override), keyed by `(citation_key, resolver_name, query_form)`. Its 90-day TTL controls reuse, not physical retention: expired rows remain until overwrite, per-citation invalidation, or database deletion. Retraction observations occupy a separate caller-selected SQLite namespace and remain stored without automatic expiry; after 30 days they are returned as `stale` (`scripts/verification_cache.py:102-218`; `scripts/retraction_status.py:407-463`; `docs/DATA_FLOWS.md:84-92`).
- **Invalidation and regeneration:** Citation rows become misses when absent, expired, malformed, non-object, decision-version-incompatible, or missing required typed fields. `ARS_CACHE_REVALIDATE=1` also bypasses a hit beyond the advisory age, after which a live computation overwrites the row. Manual invalidation deletes all resolver/query-form rows for a citation. Retraction observations are marked stale rather than deleted (`scripts/verification_cache.py:126-190`; `scripts/contamination_signals.py:227-295`; `scripts/retraction_status.py:441-463`).
- **Read-back direction:** Pull. Resolver/verifier code requests the exact cache key before making a live call. A valid hit substitutes its retained outcome for live computation and returns `served_from_cache`; a miss invokes the resolver and writes a replacement (`scripts/contamination_signals.py:227-295`; `scripts/verification_gate/__init__.py:74-94,117-178`).
- **Selection signal and scope:** Exact citation, resolver, and canonical query form select one row. The payload must match the current resolver decision version and, for gate use, have typed `matched` and `queried_by` values. Reuse is one resolver attempt, not general retrieval of neighboring citations or prior summaries.
- **Delivery and consumption point:** BAP-10/RTE-6 consumes a row inside the deterministic verifier before summary reduction and integrity/terminal policy. Retraction cache output is returned to its explicit caller with a `current|stale` label.
- **Context-presence status:** `wired` in deterministic resolver/verifier computation. Whether the resulting summary entered a model or orchestrator context is `uninspected`; the cache row itself is not shown to be prompt context.
- **Activation status:** `uninspected`. The code contains a wired cache-hit branch that changes whether a live resolver is called, but no supplied run observes a hit or its downstream behavioral effect.
- **Prevented conclusions:** No cache row was supplied, no live service was observed, and no candidate-linked integrity run exists. The cache cannot establish source truth, service correctness, or model use of the resulting summary.

### `OBJ-7` — Claim registry, provenance records, integrity findings, and verdicts

- **Write agency:** For the claim-standing subfamily, deterministic scripts derive query plans, candidate ledgers, stance identities, transmission ledgers, freshness reports, and views from explicit claim, consent, adapter, retrieval, relevance, and provider inputs. The researcher supplies consent and relevance/version judgments; an optional stance provider supplies classifications. These roles remain unobserved (`docs/design/2026-08-13-655-search-bounded-claim-standing-probe-design.md:379-438,440-480`; `scripts/build_claim_standing_candidate_ledger.py:928-1122`).
- **Persistence and lineage:** Claim-standing artifacts default to `session_only`. A persistent candidate ledger is allowed only by an exact `explicit_local_export` consent receipt bound to the absolute output path. Export creates a new file; a later probe after new consent receives a new probe id and does not overwrite the prior ledger (`docs/design/2026-08-13-655-search-bounded-claim-standing-probe-design.md:461-480,492-515`).
- **Invalidation and regeneration:** Claim text, consent receipt, query plan, adapter registry, candidate ledger, or stance configuration drift yields a closed stale reason. Stale results remain inspectable but cannot be presented as current; rerun requires new consent and a new probe id. The freshness checker is read-only and does not mutate or regenerate artifacts (`scripts/check_claim_standing_freshness.py:1-22,42-70,102-197`).
- **Read-back direction:** Pull. The freshness checker loads a current claim plus a prior plan and optional candidate/stance records. Validators replay retained ledgers against their named inputs; renderers read the retained candidate/stance family to construct the bounded advisory (`scripts/check_claim_standing_freshness.py:102-197`; `scripts/build_claim_standing_candidate_ledger.py:1125-1127`).
- **Selection signal and scope:** Exact digests bind the claim, consent, query plan, adapter versions, candidate ledger, evidence rows, and stance configuration. Candidate selection is deterministic within the recorded query/index/cap/filter boundary; it is not a field-wide memory search (`docs/design/2026-08-13-655-search-bounded-claim-standing-probe-design.md:379-438,492-515`).
- **Delivery and consumption point:** The retained family is consumed by deterministic validation/freshness/rendering and a human-facing advisory. It may also bind a subsequent stance action. It is explicitly search-bounded and cannot be presented as scientific consensus or verified truth.
- **Context-presence status:** `wired` for deterministic read-back into freshness and rendering code. Model/context presence for a later workflow step is `uninspected` except for the explicit provider request protocol; no host run was supplied.
- **Activation status:** `uninspected`. The frozen artifact affords and wires the deterministic readers, but there is no observed query, ledger, provider response, rendered advisory, or later decision changed by one.
- **Prevented conclusions:** The mechanism does not establish novelty, scientific consensus, field-level standing, source truth, or that a human consented. External services, stance provider, host, human, and candidate-linked runs are excluded.

### `OBJ-11` — Checkpoint branch choices, pending decisions, and override receipts

- **Write agency:** Human-originated choices and consent/override declarations are serialized by prompt-layer orchestration or deterministic receipt builders. For Passport reset, the orchestrator records `pending_decision`; on resume it must obtain the user's option and append `chosen_branch` plus any override. For claim-standing, scripts bind the exact displayed consent surface and accepted receipt to downstream artifacts (`academic-pipeline/references/passport_as_reset_boundary.md:42,59-65`; `docs/design/2026-08-13-655-search-bounded-claim-standing-probe-design.md:461-480`).
- **Persistence and lineage:** Pending choices and resume decisions persist in the Passport's append-only reset ledger. Claim-standing consent may remain session-only or persist with its explicitly authorized export family. Prior probe/ledger identities remain rather than being overwritten.
- **Invalidation and regeneration:** A pending decision survives the reset and must be re-prompted; `stage=` alone cannot satisfy it. Claim-standing drift of the consented surface, filters, exact plan, or authorized path invalidates reuse and requires a new consent/probe identity.
- **Read-back direction:** Pull. The resumed orchestrator reads the pending decision and option table before downstream dispatch. Claim-standing builders and freshness checks read digest-bound consent/plan values before retrieval, export, stance, and currentness decisions.
- **Selection signal and scope:** The exact user option value selects one declared branch; the resume hash selects which pending decision is active. Consent receipts select only their digest-bound recipient/content/path/action scope.
- **Delivery and consumption point:** BAP-3/BAP-6 consume branch and override values at the next transition or resumed run. Claim-standing consumers use receipts as permissive authorization and identity binding, not evidence that research claims are true.
- **Context-presence status:** Passport choice delivery is `claimed` because it depends on external host/model prompt adherence. Deterministic receipt validation is `wired` within the scripts.
- **Activation status:** `uninspected`. No observed human choice, consent, override, resume, or downstream changed action is supplied.
- **Prevented conclusions:** The tree cannot authenticate the person behind a session, prove informed consent, or establish that the host re-prompted or followed the selected branch.

### `OBJ-12` — Post-terminal adjudication-activity records and store

- **Write agency:** Automatic and deterministic after the ordinary effect and terminal write. Producers may best-effort append pending bindings only after the user's ordinary action is durable; the tracker seals the exact five-family inventory, then an explicitly invoked helper may build and append a run. The human/caller selects the store path (`academic-pipeline/agents/state_tracker_agent.md:34-103`; `academic-pipeline/references/pipeline_state_machine.md:250-281`).
- **Persistence and lineage:** The explicit caller-selected canonical JSON store retains cross-run records with strictly increasing append sequence and store revision. Identical `run_id` plus input receipt is idempotent; conflicting identity is rejected. Deletion requires explicit run selection or whole-store confirmation plus store identity and raw-byte hash (`scripts/adjudication_activity.py:1216-1304,1311-1392,1452-1520`).
- **Invalidation and regeneration:** Source/run authority is the terminal state's `run_id` plus sealed inventory and hash-bound artifacts. The store validates canonical bytes, schemas, digests, identities, event counts, and ordering. It does not regenerate missing source activity or infer paths/roles from ambient state.
- **Read-back direction:** Pull only into the deterministic renderer/validator from an explicitly named store. The renderer selects the last requested retained-run window and computes advisory counts for the human (`scripts/adjudication_activity.py:1395-1449`).
- **Selection signal and scope:** Explicit store path and render window select retained runs; deletion additionally requires exact ids or sequence range and confirmations. There is no ambient discovery or default path (`scripts/adjudication_activity.py:1-8,1395-1449`).
- **Delivery and consumption point:** BAP-12 delivers a standalone advisory rendering to the human after terminal state. Source doctrine explicitly excludes the store, renderer output, and diagnostics from every Passport, handoff, Process Record, reviewer/model/observer input, compliance decision, gate, verdict, checkpoint, and transition (`academic-pipeline/agents/state_tracker_agent.md:105-109`; `academic-pipeline/references/pipeline_state_machine.md:269-280`).
- **Context-presence status:** `wired` for deterministic renderer-to-human output. `absent` for model, observer, compliance, pipeline, and checkpoint context within the inspected artifact.
- **Activation status:** Human use is `uninspected`; agent/pipeline activation is `inapplicable` under the explicit non-consumption contract. No observed store or human response was supplied.
- **Prevented conclusions:** Retention across runs is not agent memory activation. The store cannot explain or improve later pipeline behavior, and the evidence cannot show that a human viewed or used the advisory.

### `RTE-1` / `BAP-1` — SessionStart delivery and update-state reuse

- **Write agency:** The update checker automatically writes `UP_TO_DATE|UPDATE_AVAILABLE`, installed version, and remote version after a successful fetch. SessionStart reads the state only on `startup|clear`; `compact|resume` receives a static short announcement and assumes transcript/summary context carried by the external host (`scripts/ars_update_check.sh:92-157,159-215`; `scripts/announce-ars-loaded.sh:30-77`).
- **Persistence and lineage:** One local `update-check` file under the configured/default ARS cache directory is atomically replaced after successful checks. Fresh matching state is reused for 24 hours; failed fetches leave it untouched; local-version change or malformed state forces refetch (`scripts/ars_update_check.sh:92-157,159-215`).
- **Invalidation and regeneration:** Age at least 24 hours, changed installed version, malformed cached state/version, deletion, or disabling via `ARS_UPDATE_CHECK=0` prevents reuse or triggers refetch as specified. The file has replacement, not append-only, lineage.
- **Read-back direction:** Pull by a later SessionStart update check, followed by push of an update notice in hook `additionalContext` only when the retained/current result is `UPDATE_AVAILABLE`.
- **Selection signal and scope:** Session source chooses whether the update checker runs; cache mtime, installed-version equality, valid state, and bounded version grammar select reuse. The selected payload is only two version strings and a state, not user/project memory.
- **Delivery and consumption point:** Hook JSON emits `hookSpecificOutput.additionalContext` to the external Claude Code host. Static plugin material is retained shipped content, not accumulated-from-use memory. Only the update-state reuse is a memory read-back subroute (`hooks/hooks.json:1-12`; `scripts/announce-ars-loaded.sh:49-105,108-142`).
- **Context-presence status:** `wired` at the hook-output boundary. Receipt in a host/model context is `uninspected` because CMP-9 is excluded.
- **Activation status:** `uninspected`. No supplied SessionStart run shows a cached result being selected, delivered by the host, or changing model/user behavior.
- **Prevented conclusions:** The short `resume|compact` announcement's assumption that prior transcript/summary context exists is not evidence that ARS itself persisted or selected that context. ABS-7 still establishes no Passport read at SessionStart.

### `RTE-4` / `BAP-3` / `BAP-4` — Retained evidence and choices at checks and transitions

- **Write agency:** Mixed human and automatic. A user writes read attestations through `/ars-mark-read` or rescinds them through `/ars-unmark-read`; deterministic code writes and validates the peer ledger. The finalizer reads the current ledger and anchor on every Stage 4-to-5 pass. Other checkpoint/override choices remain prompt-layer human inputs.
- **Persistence and lineage:** The read log is a Passport-adjacent YAML peer file. Marks append; rescission adds `rescinded_at` to the latest active matching row rather than deleting it. The source corpus is not mutated to cache the derived state (`commands/ars-mark-read.md:7-16`; `commands/ars-unmark-read.md:7-13`; `scripts/ars_mark_read.py:92-103,243-323,384-418`).
- **Invalidation and regeneration:** The transient resolution is never persisted. Every finalizer pass recomputes it from the current exact anchor and strict current ledger; changed anchor, mark, scope, rescission, or invalid ledger changes the route. `ledger_invalid` stops the transition; only `covered` is eligible for `ok` (`scripts/human_read_attestation_resolver.py:1-10,311-413`; `academic-pipeline/agents/pipeline_orchestrator_agent.md:1014-1044`).
- **Read-back direction:** Pull from peer ledger to deterministic resolver/finalizer. A covered mark may promote `LOW-WARN` to `ok`; rescission or uncovered scope may demote it on the next pass.
- **Selection signal and scope:** Citation key selects relevant events; most recent timestamp/index event wins. Exact anchor kind/value plus declared `full_text|sections|abstract_only|toc_only|unknown` scope decides coverage. No semantic inference of reading or comprehension is permitted.
- **Delivery and consumption point:** The finalizer consumes the derived state immediately before the formatter gate and mutates the draft marker; counts enter the Stage 4.5 report. The attestation is routing input, not proof (`academic-pipeline/agents/pipeline_orchestrator_agent.md:1008-1046`).
- **Context-presence status:** Deterministic resolution is `wired`; external host invocation and draft-to-model delivery are `claimed`/`uninspected`.
- **Activation status:** `uninspected`. Code and prompt contracts define promotion/demotion, but no candidate-linked finalizer pass demonstrates that retained attestation changed a draft, gate, or later action.
- **Prevented conclusions:** `USER_ATTESTED_READ` cannot prove a human read or understood a source. The external host and real workspace are unavailable.

### `RTE-6` / `BAP-10` — Cache-through verification

- **Read-back direction:** Pull by exact cache key before a resolver call; a valid hit replaces the live call for that resolver attempt.
- **Selection signal and scope:** `(citation_key, resolver_name, query_form)` plus TTL, decision version, and typed payload checks select one row. `ARS_CACHE_REVALIDATE=1` may bypass an otherwise valid aged row.
- **Delivery and consumption point:** The retained resolver outcome enters deterministic citation-summary reduction and then the integrity/terminal-policy route, not directly a model prompt.
- **Context-presence status:** `wired` in CMP-8; downstream host/model presence is `uninspected`.
- **Activation status:** `uninspected`; no run supplies a cache hit and changed resolver behavior.
- **Prevented conclusions:** A cache hit is permissive substitution, not fresh service observation or evidence that the eventual integrity decision was correct.

### `RTE-8` / `BAP-6` — Passport boundary to resumed stage

- **Read-back direction:** Pull from an explicitly located Passport into a later orchestration session; append a resume entry after selection.
- **Selection signal and scope:** Exact hash, user-supplied/discovered Passport path, unconsumed-boundary check, referenced paths/IDs, verification state, and pending branch choice.
- **Delivery and consumption point:** Intended binding context for one resumed stage/run. Prior working-memory content is declared non-authoritative after reset.
- **Context-presence status:** `claimed`; the protocol and natural-language orchestrator obligations exist, but an executable general reset/resume transaction and context loader were not found.
- **Activation status:** `uninspected`; there is no behavioral run.
- **Prevented conclusions:** ABS-1 and ABS-6 prevent `wired`, `observed`, or `causally supported` resume conclusions. ABS-7 rules out SessionStart as the missing state loader.

### `BAP-12` — Adjudication rendering to the human

- **Read-back direction:** Pull from the caller-selected cross-run store into a deterministic last-`N` rendering.
- **Selection signal and scope:** Explicit store path and window; selected retained eligible runs only.
- **Delivery and consumption point:** Standalone advisory text for the human after terminal completion.
- **Context-presence status:** `wired` for human rendering and `absent` for pipeline/model inputs.
- **Activation status:** `uninspected` for any human consequence; `inapplicable` to pipeline/model behavior under the non-consumption contract.
- **Prevented conclusions:** No inference from retained activity to future agent adaptation, quality improvement, or human action is warranted.

## Proposals, corrections, and absences

### `MEM-1` — New operative-object proposal: SessionStart update-check state

Propose a distinct operative object for the local `update-check` state file. It has a stable identity and lifecycle not represented by OBJ-6's citation/resolver rows: automatic successful-fetch write, atomic replacement, 24-hour reuse horizon, local-version/format/age invalidation, and conditional delivery of two version values through RTE-1. Evidence: `scripts/ars_update_check.sh:92-157,159-215`, `scripts/announce-ars-loaded.sh:61-77`, and `docs/DATA_FLOWS.md:84-92`.

### `MEM-2` — New operative-object proposal: Passport peer human-read ledger

Propose the `<passport-stem>_human_read_log.yaml` as a distinct operative object. It is user-attested, Passport-adjacent, strictly validated, mark-append/rescind-preserving state. Its derived coverage is recomputed from the current ledger and exact anchor at every finalizer pass; it can promote, demote, or block a transition without mutating `literature_corpus[]`. Evidence: `commands/ars-mark-read.md:7-16`, `commands/ars-unmark-read.md:7-13`, `scripts/ars_mark_read.py:92-103,243-323,384-418`, `scripts/human_read_attestation_resolver.py:1-10,311-413`, and `academic-pipeline/agents/pipeline_orchestrator_agent.md:1008-1046`.

### `MEM-3` — New operative-object proposal: `inquiry-branch-ledger/1.0`

Propose the opt-in inquiry branch ledger and its Passport `inquiry_ledger_ref` as a distinct operative object. It materializes only on the second recorded branch when `ARS_INQUIRY_LEDGER=1`; its append-only event chain plus Passport content digest supports deterministic replay and cross-session carry. Author actions own adoption and branch changes; AI facets begin `parked`; reopening mechanically adds first-degree artifact-stale events; stale artifacts are not silently regenerated. The Passport pointer is authoritative, exact historical profile bytes are required, and broken bindings fail rather than falling back. Evidence: `academic-pipeline/SKILL.md:338-362`, `academic-pipeline/agents/pipeline_orchestrator_agent.md:225-268`, `docs/design/2026-08-17-743-inquiry-branch-ledger-design.md:30-120,180-319`, and `scripts/inquiry_branch_ledger.py:1-43,1129-1190,1217-1275,2041-2201`.

Memory-owned disposition for the proposal: write agency is mixed author/AI/system with closed event permissions; persistence is append-only user-project JSON plus Passport digest; invalidation is first-degree stale-event accumulation with explicit reconfirm/supersede; read-back is pull through exact pointer/profile replay; selection is the Passport binding plus prescribed checkpoint/signal moment; delivery is an advisory summary immediately before a checkpoint response prompt; context presence is `claimed` at the host/model boundary and deterministic replay/rendering is `wired`; activation is `uninspected`. The design itself records behavioral evidence as `NOT_RUN` (`docs/design/2026-08-17-743-inquiry-branch-ledger-design.md:321-340`).

### `MEM-4` — New operative-object proposal: Claim-standing probe artifact family

Propose a distinct operative-object family for the consent-bound query plan, retrieval input, candidate ledger, stance record, transmission ledgers, and freshness result. The family has its own export authority, exact digest lineage, replay, selection caps, stale reasons, and new-probe rather than overwrite behavior. Grouping it only under broad OBJ-7/OBJ-11 labels hides the state identity that returns to freshness, validation, stance, transmission, and rendering consumers. Evidence: `docs/design/2026-08-13-655-search-bounded-claim-standing-probe-design.md:379-480,492-515`, `scripts/build_claim_standing_candidate_ledger.py:928-1145`, `scripts/check_claim_standing_transmissions.py:288-369`, and `scripts/check_claim_standing_freshness.py:1-22,42-70,102-197`.

### `MEM-5` — New route proposal: Human-read ledger to provenance finalizer

Propose a route with endpoints: user mark/rescind command → Passport peer read ledger → deterministic latest-event and anchor-coverage resolution → Stage 4-to-5 Cite-Time Provenance Finalizer → marker promotion/demotion or invalid-ledger stop → formatter gate. Deterministic selection and reduction are `wired`; host invocation is `claimed`; operation/activation are `uninspected`. This is more specific than RTE-4 because its retained object, recomputation rule, and delivery effect are stable and independently testable.

### `MEM-6` — New route proposal: Inquiry-ledger replay to checkpoint interaction

Propose a route with endpoints: explicit author/AI event → deterministic append and Passport-pointer transaction → later exact-pointer/profile replay → compact summary at Stage 1, 2.5, 4.5, or a named reopen signal → author display choice or branch action. The route is advisory and cannot alter an integrity verdict or satisfy a mandatory checkpoint. Deterministic append/replay/render/transaction code is `wired`; host delivery and activation are `uninspected` (`academic-pipeline/agents/pipeline_orchestrator_agent.md:225-268`; `scripts/inquiry_branch_ledger.py:1129-1190,1217-1275,2041-2201`).

### `MEM-7` — New route proposal: Update-check state to SessionStart context

Propose a subroute of RTE-1 with endpoints: prior successful update fetch → local `update-check` replacement → later `startup|clear` cache selection → optional update line → SessionStart `additionalContext` → external host/model. The cache read/write and hook-output boundary are `wired`; external context presence and activation remain `uninspected`.

### `MEM-8` — New route proposal: Claim-standing retained artifacts to currentness and advisory

Propose a route with endpoints: consent-bound claim/query/retrieval inputs → candidate/stance/transmission artifacts → later deterministic replay and freshness comparison → bounded human advisory or stale refusal. Exact artifact read-back is `wired`; live retrieval/provider operation, host delivery, human use, and behavioral activation are `uninspected`. The route cannot support field-global or truth conclusions.

### `MEM-9` — Evidenced absence: Adjudication-store delivery to agent or pipeline context

Status: `absent` within the frozen artifact. The state-machine and tracker contracts explicitly prohibit pending bindings, sealed inventory, selected-store information, store contents, renderer output, and diagnostics from entering a Passport, handoff, Process Record, reviewer/model/observer input, compliance decision, gate, verdict, checkpoint, or transition. The deterministic helper has no default path or ambient scan. This prevents classifying OBJ-12 retention/read-back as agent memory activation. Evidence: `academic-pipeline/references/pipeline_state_machine.md:250-281`, `academic-pipeline/agents/state_tracker_agent.md:84-109`, and `scripts/adjudication_activity.py:1-8`.

### Corrections

No canonical correction is proposed. The baseline's `claimed`/`wired` distinctions, ABS-1/ABS-2/ABS-6/ABS-7, and legacy disposition remain supported. The `MEM-*` items are proposed separations of materially distinct operative objects and routes, not replacements for defective canonical values.

## Legacy review routing check

- Detection: **not detected**.
- Basis: Academic Research Skills primarily offers research, writing, integrity review, revision, and finalization. Its persistent state, ledgers, and caches support that workflow; they are not its primary offered memory, knowledge, or context-engineering product.
- Invocation disposition: **not invoked**. The legacy agent-memory review workflow is not applicable.

## Summary and limitations

The inventory covered the Material Passport and its reset/compliance/audit/lineage fields; citation-verification and retraction caches; SessionStart update-check state; checkpoint and consent receipts; human-read attestations; the inquiry branch ledger; claim-standing plans/ledgers/stance/transmission/freshness artifacts; and the post-terminal adjudication-activity store.

The frozen tree contains genuine later-use read-back mechanisms. The most concrete are exact cache-hit substitution, monotonic `slr_lineage` preservation, current-ledger human-read recomputation, exact-pointer inquiry-ledger replay, claim-standing artifact replay/freshness comparison, update-state reuse, and deterministic rendering of retained adjudication activity. These mechanisms differ materially in write agency, persistence, invalidation, selection, and consumption. Static shipped prompts and the ordinary SessionStart announcement were not counted as memory merely because they are retained.

No mechanism reaches `observed` or `causally supported` activation. The evidence contains no candidate-linked run. The external Claude Code host/model/context builder, human researcher, project execution, bibliographic services, and optional model providers are excluded. Consequently the return can establish code-level wiring, prompt-level affordances/claims, context output at in-tree boundaries, and evidenced absences; it cannot establish that retained material entered a real model context, changed an agent or human action, restored a session, improved research quality, or produced correct scholarly conclusions.
