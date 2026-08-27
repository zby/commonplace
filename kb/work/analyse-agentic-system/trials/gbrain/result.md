# GBrain — agentic system analysis

**Result identity: `RUN-GBRAIN-20260820`**

One logical result across six physical files. Canonical IDs are **defined once** — in
`evidence-packet.md` §6 for records registered before lens dispatch, and in §4 of this file for
everything registered after. Every other file cites and never redefines. That convention satisfies
the requirement that IDs resolve across all physical parts.

| Logical record | Where |
|---|---|
| 1. Run / staging identity | this file, §1 |
| 2. Boundary, revision, evidence tier | this file, §2 (full statement: `evidence-packet.md` §3–§4) |
| 3. Source register | `evidence-packet.md` §5, extended in §4 of this file |
| 4. Shared component / object / route / claim / authority records | `evidence-packet.md` §6, extended and reconciled in §4 of this file |
| 5. Runtime account | `runtime-account.md` |
| 6. Both lens applicability records | `lens-dispositions.md` |
| 7. Applicable lens outputs | `lens-memory-context.md`, `lens-epistemic.md` |
| 8. Cross-lens reconciliation | this file, §8 |
| 9. Bounded synthesis | this file, §9 |
| 10. Limitations, each paired with the conclusion it prevents | this file, §10 |
| 11. Verification / blocker report | this file, §11 |

Trial apparatus (outside the instruction's result): `trial-notes.md`.

---

## 1. Run and staging identity

- **Run / result ID:** `RUN-GBRAIN-20260820`
- **Subject:** GBrain — `github.com/garrytan/gbrain`
- **In-scope determination:** in scope. GBrain is an agent operating layer whose deployed behavior
  depends on model calls plus surrounding machinery: a durable job queue with an LLM tool loop
  (`gbrain agent run`), an autonomous nightly maintenance cycle, a synthesis engine, an MCP tool
  server, and a shipped skillpack that instructs a host agent platform.
- **Staging identity:** `kb/work/analyse-agentic-system/trials/gbrain/`
- **Publication:** none. See §11.

## 2. Boundary, revision, evidence tier

- **Revision:** `9a0bae8d62cdd1e0dd6655e24e082fe6c69c5dac`, `VERSION` `0.42.25.0`, committed 2026-06-03.
  Clean working tree. Inspected read-only. One revision governs every record in this run; both lens
  outputs cite it.
- **Boundary:** declared by function in `evidence-packet.md` §3 — inclusions, exclusions, and named
  external dependencies.
- **Boundary character — stated as required by step 1.4:** whole-system for the GBrain repository;
  **subsystem-only with respect to the advertised agent loop.** The "signal → search → respond →
  write → auto-link → sync" loop that `README.md:241` presents as *the* GBrain loop executes inside
  a host agent platform (OpenClaw, Hermes, Claude Code, Codex) that is not in this checkout. The one
  in-repo crossing is the opt-in OpenClaw context-engine plugin (RTE-23). **No whole-system
  conclusion about end-to-end agent behavior is drawn anywhere in this result.**
- **Overall evidence tier:** `code-grounded`. Every material loop in `runtime-account.md` rests on
  inspected TypeScript in this checkout, and both lenses grounded their findings in the same way.
  Doctrine is cited as `doctrine/design` and never upgraded. Nothing was executed, so **no `observed`
  and no `causally supported` conclusion appears anywhere in this run.**

## 3. Source register

`evidence-packet.md` §5 (SRC-01 … SRC-18), extended by §4 below.

## 4. Records registered after packet freeze, and canonical ID assignment

Step 2.4 permits targeted reads inside the frozen boundary provided they are added centrally.
Step 3 reserves ID assignment to the orchestrator: *"Any new material record returns to the
orchestrator for one canonical ID."* Both lenses proposed records in their own `PROPOSED-*`
namespaces, and those namespaces collided — with each other and with records the orchestrator had
already registered post-freeze. Canonical assignment below.

### 4.1 Orchestrator's own post-freeze reads

| ID | Record | Effect on lens findings |
|---|---|---|
| SRC-19 | `src/openclaw-context-engine.ts` (67 lines, full) | none; folded into the runtime account |
| SRC-20 | `src/core/calibration/voice-gate.ts` (238 lines; header + types) | see conflict C3 |
| SRC-21 | `DESIGN.md` (149 lines, full) | see conflict C3 |
| SRC-22 | `skills/manifest.json` (metadata + count) | see conflict C1 |
| SRC-23 | `src/core/brainstorm/{checkpoint,domain-bank}.ts` (headers) | RTE-21; no lens annotation |
| SRC-24 | `src/core/minions/{supervisor,system-prompt,tools/brain-allowlist}.ts` | none; runtime account |
| SRC-25 | `AGENTS.md` (full), `INSTALL_FOR_AGENTS.md` (1–60) | none; runtime account |
| SRC-26 | `src/core/remediation/{index,context,plan,run}.ts` | adds L7 / RTE-24 |
| SRC-27 | `src/commands/jobs.ts` (handler registration, plugin loader) | none; runtime account |

### 4.2 Epistemic lens sources — canonical assignment

The epistemic lens numbered its proposals `PROPOSED-SRC-19…43`, colliding with SRC-19…27 above.
Reassigned in listed order:

| Lens ID | Canonical | Identity |
|---|---|---|
| PROPOSED-SRC-19 | **SRC-28** | `src/core/cycle/propose-takes.ts` (full) |
| PROPOSED-SRC-20 | **SRC-29** | `src/core/cycle/grade-takes.ts` (full) |
| PROPOSED-SRC-21 | **SRC-30** | `src/core/cycle/calibration-profile.ts` (full) |
| PROPOSED-SRC-22 | **SRC-31** | `src/core/cycle/phases/consolidate.ts` (full) |
| PROPOSED-SRC-23 | **SRC-32** | `src/core/cycle.ts` (partial) |
| PROPOSED-SRC-24 | **SRC-33** | `src/core/think/index.ts` (partial) |
| PROPOSED-SRC-25 | **SRC-34** | `src/core/think/cite-render.ts` (full) |
| PROPOSED-SRC-26 | **SRC-35** | `src/core/think/sanitize.ts` (full) |
| PROPOSED-SRC-27 | **SRC-36** | `src/core/eval-contradictions/judge.ts` (full) |
| PROPOSED-SRC-28 | **SRC-37** | `src/core/eval-contradictions/auto-supersession.ts` (full) |
| PROPOSED-SRC-29 | **SRC-38** | `docs/contradictions.md` (full) |
| PROPOSED-SRC-30 | **SRC-39** | `src/core/guardrails.ts` (full) |
| PROPOSED-SRC-31 | **SRC-40** | `src/core/takes-resolution.ts` (full) |
| PROPOSED-SRC-32 | **SRC-41** | `src/commands/takes.ts` (partial) |
| PROPOSED-SRC-33 | **SRC-42** | `src/commands/calibration.ts` (partial) |
| PROPOSED-SRC-34 | **SRC-43** | `src/core/cycle/nightly-quality-probe.ts` (full) |
| PROPOSED-SRC-35 | **SRC-44** | `src/core/skillopt/{validate-gate,bundled-skill-gate,score}.ts` |
| PROPOSED-SRC-36 | **SRC-45** | `docs/eval-takes-quality.md` (full) |
| PROPOSED-SRC-37 | **SRC-46** | `src/core/cycle/synthesize.ts` (partial) |
| PROPOSED-SRC-38 | **SRC-47** | `src/core/facts/decay.ts` (full) — duplicate identity with SRC-11; **merged into SRC-11**, ID retired |
| PROPOSED-SRC-39 | **SRC-48** | `src/core/extract-takes-from-pages.ts` (partial) |
| PROPOSED-SRC-40 | **SRC-49** | `src/core/cycle/{extract-atoms,synthesize-concepts}.ts` (heads) |
| PROPOSED-SRC-41 | **SRC-50** | `src/core/operations.ts` — duplicate identity with SRC-18; **merged into SRC-18** with widened inspected scope, ID retired |
| PROPOSED-SRC-42 | **SRC-51** | `src/core/cross-modal-eval/runner.ts` (partial) |
| PROPOSED-SRC-43 | **SRC-52** | `docs/GBRAIN_VERIFY.md` (headings) |

Two retirements above are the correct handling of *"Merge duplicate objects and routes by canonical
ID"* — a lens may not re-register an object the orchestrator already holds.

### 4.3 Memory/context lens sources

The memory lens proposed no SRC IDs; it returned a 45-row file-read table (`lens-memory-context.md`
§7) plus a named list of grep-only sweeps. That table is registered as a block, **SRC-53 onward, one
per row in listed order**, with the lens file as the authoritative record of extent and what was
taken. Rows whose identity duplicates an already-registered source (`src/core/facts/meta-hook.ts` =
SRC-10, `decay.ts` = SRC-11, `extract.ts` = SRC-12, `cycle.ts` = SRC-07/SRC-32, `think/prompt.ts` =
SRC-08, `mcp/dispatch.ts` = SRC-09, `context-engine` = SRC-19, `CLAUDE.md` = SRC-03, `skills/` =
SRC-16/SRC-22, `VERSION` = SRC-01) **merge into the existing ID with widened inspected scope** rather
than taking a new one.

### 4.4 Corrections to already-registered records

The memory lens returned corrections to records the packet had already registered (`lens-memory-context.md`
§0). Applied centrally:

| Record | Registered value | Corrected value | Basis |
|---|---|---|---|
| SRC-16, CMP-16, packet §3 | "43 skills" | **53 directories, 51 `SKILL.md` files, 125 files total** under `skills/` | direct tree inspection, `implemented` |
| CMP-16 | "Skillpack (43 skills + RESOLVER)" | manifest declares **50** skills at `version: 0.32.3.0` while `VERSION` is `0.42.25.0` — **the manifest is stale relative to the tree** | `skills/manifest.json:1-5` + `VERSION`, `implemented` |
| OBJ-04, OBJ-05, OBJ-19 anchors | implied `src/schema.sql` | `facts` (migration v40), `takes` (v37), and `query_cache` (v55/v56) are defined **only** inside the `MIGRATIONS` array of `src/core/migrate.ts`; `schema.sql` does not contain them | `implemented` |

The third correction is load-bearing beyond bookkeeping: an inventory keyed on `schema.sql` alone
misses the three most memory-relevant tables in the system.

### 4.5 New components

| Canonical | Source | Component |
|---|---|---|
| CMP-21 | orchestrator + memory `PROPOSED-CMP-01` (**merged**) | GBrain Context Engine / OpenClaw plugin (`createGBrainContextEngine`, `ENGINE_ID`). Zero LLM calls; `ingest()` is an explicit no-op; `ownsCompaction: false` |
| CMP-22 | orchestrator | Voice gate (`gateVoice`) — Haiku judge over five generated user-facing calibration surfaces |
| CMP-23 | orchestrator | Brainstorm orchestrator + judges |
| CMP-24 | memory `PROPOSED-CMP-02` | Facts markdown-fence writer/parser (`fence-write.ts`, `facts-fence.ts`, `extract-from-fence.ts`) — distinct from CMP-10 in persistence, concurrency control, and rebuild survival |
| CMP-25 | memory `PROPOSED-CMP-03` | Trajectory subsystem (`trajectory.ts`, `trajectory-format.ts`, `findTrajectory`) |
| CMP-20 (extended) | memory `PROPOSED-CMP-04` | Shared audit-writer primitive + 16 consumers, `GBRAIN_AUDIT_DIR` override, current+previous ISO-week read window, best-effort posture. **Extension by ID, not a new record** — the lens rule for `CMP-*`. |

### 4.6 New operative objects

| Canonical | Source | Object |
|---|---|---|
| OBJ-21 | memory `PROPOSED-OBJ-01` | Facts fence row (markdown table row on an entity page) |
| OBJ-22 | memory `PROPOSED-OBJ-02` | Trajectory point / `TrajectoryStats` (regressions + `drift_score`) |
| OBJ-23 | memory `PROPOSED-OBJ-03` | `emotional_weight` salience score |
| OBJ-24 | memory `PROPOSED-OBJ-04` | `last_retrieved_at` retrieval-recency stamp |
| OBJ-25 | memory `PROPOSED-OBJ-05` | Recall cursor record |
| **OBJ-26** | memory `PROPOSED-OBJ-06` **+** epistemic `PROPOSED-OBJ-21` — **independent duplicate, merged** | Take proposal row (`take_proposals`) |
| OBJ-27 | memory `PROPOSED-OBJ-07` | SkillOpt version snapshot + `history.json` + `best.md` / `proposed.md` |
| OBJ-28 | memory `PROPOSED-OBJ-08` | Dream verdict (`dream_verdicts`, keyed `(file_path, content_hash)`) |
| OBJ-29 | memory `PROPOSED-OBJ-09` | Live-context block (`## Live Context (deterministic…)`) |
| OBJ-30 | memory `PROPOSED-OBJ-10` | Pattern page |
| OBJ-31 | memory `PROPOSED-OBJ-11` | Detected / suggested schema candidate |
| OBJ-32 | epistemic `PROPOSED-OBJ-22` | Take resolution tuple (`resolved_quality`, `outcome`, `resolved_by`, `source`) |
| OBJ-33 | epistemic `PROPOSED-OBJ-23` | Resolution proposal (`resolution_kind` + paste-ready command) — an imperative, **not** truth-apt |
| OBJ-34 | epistemic `PROPOSED-OBJ-24` | Takes-quality receipt (`eval_takes_quality_runs`, 5-dim, 4-sha key) |
| OBJ-35 | epistemic `PROPOSED-OBJ-25` | Nightly quality-probe audit row |

OBJ-26 is the one object both lenses discovered independently. They agree on its producer and its
substrate and diverge on nothing; the memory lens classified it `retained (gated)`, the epistemic
lens found the gate itself absent (conflict C5).

### 4.7 New routes

The orchestrator had registered RTE-21…RTE-24 post-freeze before the lenses returned; the epistemic
lens independently used `PROPOSED-RTE-21…30` for different routes. Canonical assignment resolves it.

| Canonical | Source | Route |
|---|---|---|
| RTE-21 | orchestrator | Brainstorm: question + close/far retrieval → cross-product idea generation → LLM judge → ranked ideas. **No lens annotation** — registered after dispatch; epistemic status `uninspected` |
| RTE-22 | orchestrator; epistemic annotates via OBJ-10 | Generated calibration string → `gateVoice` Haiku judge → pass, ≤2 regens, or hand-written template fallback; failures recorded to `calibration_profiles.voice_gate_passed/attempts` |
| **RTE-23** | orchestrator **+** memory `PROPOSED-RTE-A` — **independent duplicate, merged** | Workspace state files (`memory/heartbeat-state.json`, `upcoming-flights.json`, `calendar-cache.json`, `ops/tasks.md`) → `assemble()` → `systemPromptAddition`, every host turn |
| RTE-24 | orchestrator | Doctor remediation: target score → dependency-ordered plan → step → recheck → next |
| RTE-25 | memory `PROPOSED-RTE-B` | Query → semantic query-cache hit → a prior call's results, bypassing retrieval |
| RTE-26 | memory `PROPOSED-RTE-C` | Facts typed claims → `findTrajectory` → `<trajectory>` block in `think` |
| RTE-27 | memory `PROPOSED-RTE-D` | Tags + active takes → `recompute_emotional_weight` → salience ranking |
| RTE-28 | memory `PROPOSED-RTE-E` | Retrieval op → `last_retrieved_at` → LSD stale-page selection |
| RTE-29 | memory `PROPOSED-RTE-F` | Transcript hash → `dream_verdicts` → later `synthesize` gate |
| RTE-30 | memory `PROPOSED-RTE-G` | Unprefixed phantom page → redirect pass → canonical slug + migrated facts |
| RTE-31 | memory `PROPOSED-RTE-H` | Page write → fact fence → DB reconcile on `extract_facts` / `rebuild` |
| RTE-32 | epistemic `PROPOSED-RTE-21` | Bootstrap takes extraction: page → Haiku classifier → **canonical takes fence directly**, bypassing the proposal queue; double consent gate, both default false |
| RTE-33 | epistemic `PROPOSED-RTE-22` | Human `gbrain takes resolve` → take resolution tuple |
| RTE-34 | epistemic `PROPOSED-RTE-23` | Contradiction findings → top-5 by severity → dream `synthesize` prompt |
| RTE-35 | epistemic `PROPOSED-RTE-24` | Contradiction → deterministic classifier → rendered resolution command (never auto-applied) |
| RTE-36 | epistemic `PROPOSED-RTE-25` | Sampled takes → 3-provider frontier panel → 5-dim rubric verdict |
| RTE-37 | epistemic `PROPOSED-RTE-26` | Nightly probe: longmemeval → cross-modal batch judge → audit row → doctor |
| RTE-38 | epistemic `PROPOSED-RTE-27` | Guardrail seams at 5 hook points → external classifier → **verdict discarded** |
| RTE-39 | epistemic `PROPOSED-RTE-28` | `think --save` → `synthesis/<slug>-<date>` page → later retrieval and citation |
| RTE-40 | epistemic `PROPOSED-RTE-29` | Takes/resolutions → markdown fence mirror on the page |
| RTE-41 | epistemic `PROPOSED-RTE-30` | Atom/concept synthesis into retrievable pages |

RTE-38 overlaps an observation already in `runtime-account.md` §4.3 (the guardrail seam inside
`gateway.toolLoop`). The runtime account records where the seam sits; RTE-38 records what it does
with the verdict. Both stand; neither re-inventories the other.

### 4.8 New behavioral-authority paths

| Canonical | Source | Consumer | Channel | Force | Horizon |
|---|---|---|---|---|---|
| BAP-13 | memory `PROPOSED-BAP-A` | host platform LLM | `systemPromptAddition` from CMP-21, including the explicit "trust it over compaction summaries" line | advisory instruction + advisory context | every turn, while the OpenClaw slot is configured |
| BAP-14 | memory `PROPOSED-BAP-B` | SkillOpt acceptance | `runValidationGate`: `sel_score > best_score + 0.05`, median-of-3 judged rollouts | binding enforcement (candidate rejected in code) | one optimization step |
| BAP-15 | memory `PROPOSED-BAP-C` | SkillOpt bundled mutation | `assertBundledMutationHeldOut` — throws when held-out < `MIN_HELD_OUT_SIZE` | binding enforcement (hard refusal at every entry point) | per run |
| BAP-16 | memory `PROPOSED-BAP-D` | `grade_takes` auto-apply | `autoResolve` param + confidence ≥ 0.95 + tighten-only ratchet | binding enforcement, default-closed — **but see C6: the documented config key that would open it has no reader** | per verdict |
| BAP-17 | memory `PROPOSED-BAP-E` | facts extraction | `facts.extraction_enabled` kill switch + `isFactsBackstopEligible` + `dream_generated` anti-loop | binding enforcement (code refuses to extract) | every write surface |
| BAP-18 | memory `PROPOSED-BAP-F` | fence write path | FS page-lock (`~/.gbrain/page-locks/<sha256>.lock`, PID-liveness + 5-min TTL, 5s timeout) + atomic tmp/re-parse/rename | binding enforcement (multi-process serialization) | per page write |

The epistemic lens proposed no new `BAP-*` records; it referenced the packet's and kept epistemic and
operational authority separate from them, as required.

### 4.9 Claims

`CLM-01 … CLM-15` are registered in the orchestrator's namespace with truth, scope, and warrant
fields owned by the epistemic lens (`lens-epistemic.md` §5). No renumbering was needed — the lens was
the sole producer in that namespace.

---

## 8. Cross-lens reconciliation

### 8.1 Merges performed

Four independent duplicates were found and merged by identity, not by label:

1. **RTE-23** — the orchestrator registered the OpenClaw context-engine route from the runtime side
   (a context route, runtime-owned); the memory lens discovered the same route from the read-back
   side as `PROPOSED-RTE-A`. Merged. The memory lens's annotation (direction, selection signal,
   budget, delivery point, faithfulness guards) attaches to the runtime-owned record. **This is the
   ownership rule working as designed**, not a defect: runtime owns the endpoints, memory annotates
   read-back.
2. **CMP-21** — same route's component, same story.
3. **OBJ-26** — the take proposal row, found independently by both lenses.
4. **SRC-11 / SRC-18** — the epistemic lens re-proposed `facts/decay.ts` and `operations.ts`, both
   already registered. Merged with widened inspected scope; the duplicate IDs retired.

### 8.2 Ownership respected

Checked per step 8.2. Runtime owns complete control and context routes (RTE-01…RTE-05, RTE-16,
RTE-21…RTE-24); the memory lens annotated read-back and activation on RTE-04, RTE-05, RTE-07, RTE-08,
RTE-23, RTE-25, RTE-26; the epistemic lens annotated transformation, checking, warrant, acceptance,
integration, and its two authorities on RTE-05, RTE-06, RTE-09…RTE-15 and its own additions.

The epistemic lens explicitly returned RTE-01, RTE-02, RTE-03, RTE-04, RTE-17, RTE-19, RTE-20 and
the SkillOpt loop to the runtime account as direct behavior/policy adaptation with no truth-apt
object (`lens-epistemic.md` §3e). That is the direct-adaptation exception applied correctly at the
lens level, and it is accepted. **No lens renamed or re-inventoried a registered object or route.**

Both lenses annotated **RTE-12** (verdicts → calibration profile → `think`). Memory covered read-back
direction and delivery point; epistemic covered transformation class, acceptance, and integration.
Complementary, not conflicting.

### 8.3 Shared-route consistency checks

One revision (`9a0bae8`) across every record — verified in both lens outputs. Sources consistent
after §4 merges. Endpoints consistent. `BAP-*` references consistent.

Two anti-conflation rules were applied at reconciliation and both bit:

- **Memory curation labels cannot determine epistemic transformation.** Both lenses independently
  refused the `consolidate` label. Memory: "selection + re-typing + re-attribution, not semantic
  distillation… the label does not establish semantic preservation." Epistemic: "non-ampliative
  reshaping, *not* synthesis." Convergent, from different starting points, and both anchored on
  `consolidate.ts:9-12` where the code concedes it.
- **Behavioral influence cannot imply epistemic or operational authority.** `_meta.brain_hot_memory`
  (BAP-12) is the most-injected content in the system and carries the weakest authority in it —
  advisory, ignorable, with no channel by which GBrain learns whether it was read. Its injection
  frequency licenses nothing.

A third rule, **operational continuation is not warrant**, applies to the dream cycle: it runs
nightly and writes durable pages, takes, atoms, and concepts. That it keeps running warrants nothing
about what it wrote.

### 8.4 Anchored evidence conflicts — preserved as conflicts

Per step 8.1 these are **not** resolved by selecting the strongest-sounding status.

**C1 — Skill count: four incompatible figures.**
`README.md:84,110,261` and `INSTALL_FOR_AGENTS.md:194` say **43**; `CLAUDE.md:241` says **29**;
`skills/manifest.json` lists **50** at `version: 0.32.3.0`; the tree holds **51** `SKILL.md` files in
**53** directories. The three documentary figures are `claimed` and mutually inconsistent; the tree
count is `implemented` by direct inspection. The registered record is corrected to the inspected
value (§4.4) and the documentary disagreement is preserved. Consequence: neither the README nor the
manifest can be relied on to say what a given install loads, and the memory lens flagged the
skillpack installer path as unread — so the gap is load-bearing, not cosmetic.

**C2 — `consolidate`: doctrine says synthesis, code says copy.**
`docs/takes-vs-facts.md:55-66` claims the bridge "adds proper attribution, deduplication, and
temporal reasoning"; `cycle.ts:1861` says it "Sonnet-synthesize[s] one take per cluster". The code
copies the highest-confidence fact's text **verbatim**, hardcodes `holder='self'` and `kind='fact'`,
and computes `weight` as a mean of confidences. The code's own comment concedes "v0.31 ships without
LLM synthesis to keep the cycle deterministic". Preserved: three anchors, two of which describe
behavior the third does not implement. (CLM-07 / M-04.)

**C3 — Voice gate: a check whose axis is tone, framed as quality control.**
`DESIGN.md:12-28` states every user-facing calibration string "passes through this filter", implying
content control. `voice-gate.ts:1-28` shows the judge's axis is conversational-vs-academic
**register**, and the fallback path emits a hand-written template that passed *no* content check at
all. The epistemic lens independently scoped it: the gate's "target is register/tone, not truth."
Preserved as a doctrine/implementation tension. Reconciliation rule applied: **curation is not
warrant** — passing the voice gate licenses nothing about the pattern statement's truth.

**C4 — `grade_takes` evidence retrieval: reference doc states behavior the code lacks.**
`cycle.ts:63-66` and `docs/architecture/KEY_FILES.md:421` state the phase "retrieves evidence".
`grade-takes.ts:296-305` shows `defaultEvidenceRetriever` returning the literal string
`[evidence retrieval not yet wired — v0.36.1.0 ship-state]`, and the sole production caller
(`cycle.ts:1930`) injects no replacement. Preserved. Material because `CLAUDE.md` designates
`KEY_FILES.md` as the current-state reference an agent should trust. (CLM-04 / M-01.)

**C5 — `gbrain takes propose --accept`: documented as the only path; the command does not exist.**
`propose-takes.ts:20-23` states operator accept is "the only path from queue to canonical fence".
`src/commands/takes.ts:566-574` dispatches only `search/add/update/supersede/resolve/scorecard/
calibration/revisit/extract`. Repo-wide `rg take_proposals` outside schema/migrate/tests hits only
the producer. The `status` column is written never and read never. Preserved. Note the direction:
this is a **completeness** failure, not a safety failure — the half that refuses to auto-promote
shipped; the half that would let a human promote did not. (CLM-08 / M-02.)

**C6 — Cross-lens divergence on auto-resolve, resolved by scope rather than by preference.**
The memory lens recorded auto-apply as "manual opt-in: `cycle.grade_takes.auto_resolve.enabled` =
true AND confidence ≥ 0.95" — reading the documented gate. The epistemic lens ran `rg auto_resolve
src/` and found the config key **has no reader anywhere in `src/`** and is absent from
`src/core/config.ts`'s key list, while the production caller passes `{}`. **Both are correct about
different things**: the in-code gate (`autoResolve` parameter, 0.95 threshold, unanimity rule) exists
and is default-closed; the documented switch that would open it does not exist. Recorded as
reconciliation, not as an unresolved conflict, because the epistemic finding is a specific negative
search with a named boundary rather than a competing reading of the same anchor. Net effect: the
deployed safety property is **stronger** than documented — no take is auto-resolved via the cycle at
this revision. (CLM-09 / M-09.)

### 8.5 Independent convergences worth carrying forward

Two findings were reached separately by two workers that could not see each other's work. That
independence is itself the evidential point.

1. **The calibration loop is CLI-only.** Memory (§4.4): "deployed wiring **split** — `implemented` on
   the CLI path; **`absent` on the agent-facing MCP path**; the `think` op handler never passes
   `withCalibration`, and `think`'s declared `params` do not include a calibration flag." Epistemic
   (M-10): "the MCP `think` op exposes no calibration parameter, so the loop is unreachable for agent
   callers." Same anchor set, reached from opposite directions — read-back wiring vs. lifecycle
   integration.
2. **The grade-takes evidence input is a placeholder.** Memory (§1.2, §4.4): "`implemented`,
   **evidence stage is a declared stub**"; both prompt versions self-label `-stub`. Epistemic
   (M-01, CLM-04): the route is `implemented` but its evidence input is `absent`; "a verdict from
   RTE-11 is a model's opinion about a sentence, not a hindsight test against outcomes."

Taken together these two findings compose into the single most consequential structural fact in the
run, and it is stated in §9.

### 8.6 Records with no lens annotation

RTE-21 (brainstorm, CMP-23) was registered after lens dispatch. Its epistemic status — whether
judge-scored idea generation constitutes a truth-apt route — is `uninspected`. This prevents any
claim that the epistemic route inventory is complete.

---

## 9. Bounded synthesis

Organized around the deployed system's progression, not as concatenated lens reports. Capability
and deployment are kept apart throughout. **No system-wide epistemic grade is assigned**, and none
would be meaningful: the routes below differ so sharply in maturity that a single mark would erase
the finding.

### Scheduling — symbolic throughout, and deliberately so

Nothing in GBrain lets a model decide what runs next. The Minions queue claims work with
`ORDER BY priority ASC, created_at ASC … FOR UPDATE SKIP LOCKED` (RTE-01). The dream cycle runs a
fixed 22-phase list whose ordering encodes stated data dependencies — fix files, then index; extract
before patterns so graph state is fresh (RTE-03). Even the one loop that pursues a numeric goal, the
doctor remediation loop (RTE-24), derives its dependency-ordered plan from a scored checklist with
**no model call in the planning decision**; model calls happen inside individual steps.

The one place a model *does* choose the next step is inside a single subagent job (RTE-02), bounded
by `maxTurns` default 20, a name-based tool allow-list, and a slug namespace confined to
`wiki/agents/<subagentId>/`. This is a system that uses models as workers, not as planners —
`implemented`, and worth stating because the surrounding marketing ("full autonomous agent", "66 cron
jobs running autonomously") reads the other way.

The scheduler's engineering is unusually careful and the care is legible in the code: session-mode
pooled claims so a transaction pooler cannot orphan a lock; stall-before-timeout ordering with a
documented one-tick TOCTOU window; `INFRASTRUCTURE_ABORT_REASONS` so a pooler blip does not burn a
retry attempt; budget reserve ordered *before* lease acquisition so a budget throw cannot consume a
fleet-wide pacer slot. That care is `implemented`. Whether it holds in production is `uninspected`.

### Context assembly — layered, cache-sensitive, and the cache has a history

Retrieval (RTE-04) fuses vector, BM25, RRF, reranking, and four post-fusion stages including
per-query graph signals, with three named mode bundles trading cost against recall. The
schema pack threads through every read and write path so the brain re-interprets itself when the pack
changes.

The most instructive detail is the query cache (RTE-25). A hit returns a **prior call's results
verbatim**, with no keyword search, vector search, expansion, fusion, or dedup. Its key was widened
twice — once to fold in the mode bundle, once to fold in the embedding column and provider — because
each omission had produced cross-serving. The memory lens draws the right inference: the fact that
equivalence had to be *engineered* is evidence it was not initially true. Cost claims about the cache
remain `claimed`.

### External state and action — the brain repo is the system of record, and the fence is real

Markdown in a git repo is authoritative; the database is a derived index. This is not a slogan here:
the facts subsystem writes to the page's `## Facts` markdown fence **first**, under a filesystem
page-lock with PID-liveness and atomic tmp/re-parse/rename (BAP-18), and the DB row is reconciled
from the fence. A fact that exists only in the DB does not survive a rebuild — and the memory lens
found exactly that failure mode preserved for legacy pre-v51 `forget` state.

Action outward is gated three ways, all pre-handler and all symbolic: `localOnly` filters the tool
list, `hasScope` checks the OAuth scope, and `OperationContext.remote` is fail-closed by type —
anything not strictly `false` is untrusted. Source isolation runs as a SQL predicate through
`sourceScopeOpts`, with a second orthogonal `takesHoldersAllowList` filter whose default hides
non-`world` takes. These are **operational** authority and nothing more. Surviving source isolation
is not evidence of truth.

### Memory return — four distinct shapes, and the push channel carries the least authority

The memory lens separated read-back from retention across roughly sixty retained parts. Four shapes
matter:

- **Push, unconditioned** — `_meta.brain_hot_memory` (RTE-07) attaches up to ten facts, sorted by
  decayed confidence, to *every* successful MCP tool response. Not query-conditioned, not
  task-conditioned; targeted only by `(source_id, session_id)`. Deployed wiring on both transports:
  `implemented`. Activation: `uninspected` — `_meta` is by design ignorable, and there is no channel
  by which GBrain learns whether it was read.
- **Push, per-turn, host-side** — the OpenClaw context engine (RTE-23) injects deterministic
  temporal/spatial context into the host system prompt every turn, ending with an explicit
  instruction to trust it over compaction summaries. It carries an unusual honesty guard: rather than
  emit a confidently-wrong local time on an unmapped timezone, it emits a "Local time NOT computed"
  warning. That is a guard on the *injected content*, not a test that the model used it.
- **Pull** — `recall` (RTE-08) with five mutually exclusive selection branches; `think`'s gather
  (RTE-05) pulling pages, takes, and an optional anchor subgraph.
- **Decay, read-time only** — per-kind half-lives (event 7d, commitment/preference 90d,
  belief/fact 365d) applied at read and never written back. **A high effective confidence means
  "recent, and the extractor was confident." It never means "checked."**

One retained artifact modifies the system's own instructions: SkillOpt rewrites `SKILL.md` bodies in
place after a validation gate (RTE-18, BAP-14). It is default-OFF, refuses to touch bundled skills
without an explicit flag, and **hard-refuses** in-place bundled mutation without a held-out set
(BAP-15). Capability: `implemented`. Deployment in a default install: it does not happen.

### Truth-apt and warrant routes — where the shape and the substance diverge

GBrain conjectures in seven places: `think` answers with citations and gaps, fact extraction, two
separate take-extraction routes, take verdicts, calibration narratives, contradiction findings, and
atom/concept synthesis. All ampliative. Fluency and plausibility establish candidate generation and
nothing else.

It tests in three places, and none of the three tests whether a claim is true:

- Contradiction probing (RTE-13) checks **pairwise consistency relative to a query**, on ≤1500 chars
  per side, with an LLM as its own oracle and no labeled ground truth. Advisory by design; the
  probe's refusal to mutate brain state is pinned by a grep guard.
- Takes-quality and nightly probes (RTE-36, RTE-37) check **aggregate quality against rubrics and
  fixtures**, with genuine fingerprinting discipline — four content hashes in the receipt key,
  Wilson confidence intervals, an explicit `inconclusive` verdict when fewer than two of three models
  contribute. Corpus- and fixture-scoped. **Bundle success licenses nothing about any individual
  take or answer.**
- Take grading (RTE-11) is architecturally the per-claim test, and it is the one the system's warrant
  story depends on. **At this revision it consumes no evidence.**

It accepts in exactly one place over truth-apt content: a human running `gbrain takes resolve`
(RTE-33), with a consistency check that refuses contradictory input. Everything else declared as
acceptance is either doctrine with no implementation (`gbrain takes propose --accept`, C5) or
implemented but unreachable (auto-apply, C6). `think` answers, facts, gaps, atoms, concept pages, and
contradiction findings have **no acceptance route at all** — and mostly by design, which the doctrine
says out loud.

**The composite finding.** Put C4 and the calibration wiring together and the shape of the
system's headline epistemic loop becomes clear. The intended loop is: extract gradeable claims →
grade them against what actually happened → aggregate into a calibration profile with a Brier score →
feed that back so the next answer names the user's prior *and* counter-prior. Every stage is built.
But the grading stage consumes a placeholder instead of evidence; the acceptance stage that would
feed it is a command that does not exist; the profile is therefore built from human-recorded
resolutions only; and the feedback stage is reachable from the CLI but not from the MCP surface every
agent uses. **The loop's architecture is complete and its evidence path is not.** Both lens workers
reached the two halves of this independently (§8.5), which is the strongest thing this run can say
about it.

Two further asymmetries follow from it. First, `think` mandates citation of every substantive claim
in its prompt, but **no route verifies the support relation** — slug existence is checked only on
`--save`, `row_num` existence never, entailment never. The existence of a regex fallback for models
that omit the structured `citations` field is evidence the authors expected non-compliance; it is not
evidence of behavior. Second, `think --save` (RTE-39) writes an unchecked synthesis into the corpus
as an ordinary page, and **GBrain records no source-warrant field anywhere** — an imported page, a
hand-written page, and a saved synthesis are the same row modulo `type`. A later `think` call can
retrieve and cite that synthesis with its status as unchecked model output stripped. That is a
lineage-degradation route and it is `implemented`.

### Governing controls — the honest ones are the interesting ones

The controls that bind are symbolic and pre-handler: scope gating, `localOnly`, fail-closed trust,
SQL-predicate source isolation, tool allow-lists, slug namespaces, rate leases, budget trackers,
quiet hours, RSS watchdogs, page locks, and two SkillOpt refusals that throw rather than degrade.

The controls that advise are natural-language and unverified: the skillpack, SOUL/HEARTBEAT files,
subagent system prompts, and `THINK_SYSTEM_PROMPT_BASE`'s four hard rules. **No route in the
inspected boundary detects deviation from any of them.**

Three refusals deserve naming because they are load-bearing and easy to miss. Guardrails (RTE-38) are
observe-only and fail-open **by documented hard invariant** — `runGuardrails` returns `void`, the
verdict is not even persisted, and zero providers are registered by default. The contradiction probe
never auto-applies. `propose_takes` never writes canonical takes. In each case the doctrine is
unusually precise about the *absence* of force, and the code matches. A system that documents what
its checks cannot do is doing something most do not.

Against that: `_meta.brain_hot_memory` is the most-injected content in the system and the least
authoritative, and one instruction artifact changes force depending on channel — `_brain-filing-rules.json`
is advisory as skillpack markdown and **binding** where `synthesize` reads it as the subagent
`allowed_slug_prefixes` source, enforced in code by BAP-05. Same artifact, two force levels. And
BAP-05's own binding force is conditional on a second gate holding: the allow-list is trusted
*because* `PROTECTED_JOB_NAMES` stops MCP from submitting `subagent` jobs at all.

### What this run cannot say

Nothing was executed. Every activation, efficacy, and causal question is `uninspected`, and every
benchmark and production figure — P@5 49.1%, R@5 97.9%, +31.4 P@5, 146,646 pages, 100,720 takes,
$361.49, propose_takes F1 0.952/0.922 — is `claimed`, with its runs outside the boundary. The host
agent platform that executes the advertised loop is outside the checkout, so every push route ends at
GBrain's output boundary and the consumption side is unobservable here.

---

## 10. Limitations, each paired with the conclusion it prevents

| # | Limitation | Scope | Exact conclusion it prevents |
|---|---|---|---|
| L1 | Nothing was executed; read-only frozen checkout, no run, no database. | whole run | Prevents **any** `observed` or `causally supported` status anywhere in this result. Every activation and causal finding in both lenses is `uninspected` for this reason alone. |
| L2 | The host agent platform (OpenClaw, Hermes, Claude Code, Codex) is outside the checkout. | boundary character | Prevents "the injected `_meta`, skillpack, SOUL/HEARTBEAT, or live-context block reaches the model's attended context", and prevents any end-to-end conclusion about the advertised signal→search→respond→write loop. Bites hardest on the push routes RTE-07, RTE-17, RTE-23. |
| L3 | `gbrain-evals` (sibling repo) and `evals/functional-area-resolver/` runs are outside the boundary. | CLM-10, CLM-11, CLM-14, CLM-15 live application | Prevents upgrading any benchmark or production figure above `claimed`; prevents attributing the +31.4 P@5 contrast to the graph component, since the ablation's design, sampling, and confounds are not visible. |
| L4 | `src/core/search/hybrid.ts` (1,870 lines) not line-read — only the graph-signals, query-cache, and mode seams. | RTE-04 | Prevents "the ranking pipeline's full stage ordering and its interaction with salience, recency decay, autocut, and two-pass is as described", and prevents concluding what evidence set a `think` call actually sees — which in turn bounds every warrant statement about OBJ-06. |
| L5 | `src/core/operations.ts` (4,751 lines) read only at named ops. | RTE-16, read-back inventory | Prevents "the inventory of agent-facing read-back surfaces is complete" and prevents expanding any absence finding into "no route exists". `get_recent_salience`, `find_anomalies`, `get_recent_transcripts`, `whoknows` are named in doctrine with handlers `uninspected`. |
| L6 | Every absence finding is scoped to `rg` over `src/` excluding tests, plus the named file lists. | all `absent` statuses | Prevents reading any `absent` as "the behavior does not exist anywhere", including in an informal or unobserved path. |
| L7 | Individual `skills/*/SKILL.md` bodies not read. | BAP-01 content | Prevents assessing whether shipped skill doctrine instructs agents to treat `think` output or takes as established fact — i.e. prevents knowing whether the skillpack repairs or worsens the missing-warrant gap in §9. |
| L8 | Skillpack install/projection path (RTE-17 producer side) not read; C1 leaves four incompatible skill counts. | RTE-17, CMP-16 | Prevents "the 51 shipped `SKILL.md` files are what a given install actually loads." |
| L9 | Config defaults were read from code and header comments, not from a running configuration. | every default-ON/OFF claim | Prevents any claim about what a *particular deployment* has switched on, for `think.trajectory_enabled`, `search.track_retrieval`, `cycle.skillopt.enabled`, `cycle.enrich_thin.enabled`, `facts.extraction_enabled`, `search.mode`, `takes.bootstrap_*`, and the nightly probe. |
| L10 | `defaultEvidenceRetriever` is a placeholder, but `opts.evidenceRetriever` is an injectable seam and callers were not exhaustively traced. | C4, CLM-04 | Prevents "GBrain's calibration reflects a graded forecasting track record" **and** prevents the reverse conclusion that no real retriever exists in any path. |
| L11 | RTE-21 (brainstorm) was registered after lens dispatch and carries no lens annotation. | epistemic route inventory | Prevents "the epistemic route inventory is complete." |
| L12 | `page_versions` has a schema definition but no reader was found in the inspected surface. | OBJ inventory | Prevents both "page version history is read back" and "page version history is dead state." The consumer is `uninspected`, not `absent`. |
| L13 | Two of four `templates/*.md.template` files unread (`USER.md`, `ACCESS_POLICY.md`). | OBJ-15, BAP-02 | Prevents completing the OBJ-15 split — whether either carries binding rather than advisory force is `uninspected`. |
| L14 | The epistemic lens could not follow links out of the invoked instruction (wrapper rule L-0). | epistemic method fidelity | Prevents certainty that the invoked method's own definitions were applied as its authors intend, where those definitions live in files the wrapper made unavailable. |
| L15 | `behavioral-authority`'s cited definition was not readable in this run; `BAP-*` records apply consumer/channel/force from the instruction's own sentence plus the run-level `horizon`. | every `BAP-*` record | Prevents certainty that the `BAP-*` decomposition matches the registered definition. If that definition draws the three lines differently, every `BAP-*` record here is mis-specified. |
| L16 | Both lens workers and the orchestrator were terminated mid-run by a usage limit; the lens outputs were recovered from returned reports rather than written to disk by the workers themselves. | provenance of records 7 | Prevents treating the lens files as worker-authored artifacts. Content is verbatim as returned; no finding was altered. Prevents nothing about the findings themselves, but the provenance is recorded rather than hidden. |

---

## 11. Verification and blocker report

### 11.1 Structural verification (step 10.1)

| Check | Result |
|---|---|
| Source anchors and statuses present | **pass.** Every substantive claim in both lens outputs and the runtime account carries a file anchor and a conclusion status from the fixed vocabulary. |
| Unique, resolving IDs | **pass, after central repair.** Three collisions existed at return time (SRC-19…27, RTE-21…23, OBJ-21…25 across the two lens namespaces and the orchestrator's post-freeze registrations). All resolved in §4; two duplicate SRC IDs retired by merge. |
| One boundary and one revision across all records | **pass.** `9a0bae8` and the packet §3 boundary are cited by the runtime account and both lenses; neither lens widened the boundary or changed the revision. |
| Mandatory runtime coverage | **pass.** Seven material loops recorded with materiality stated, plus eight conditional surfaces each with its materiality named. |
| Both lens dispositions present as explicit records | **pass.** `lens-dispositions.md`; neither is implied by an absent section. |
| All applicable lens outputs present | **pass.** Both lenses were `applicable` and both ran; outputs at `lens-memory-context.md` and `lens-epistemic.md`. |
| Prevented conclusions stated for every non-run | **n/a for lens non-runs** (both ran). Stated for every negative and uncertain finding: §10 and the per-finding tables in both lenses. |
| Shared-route ownership respected | **pass.** §8.2. |
| No forbidden evidence upgrades | **pass.** §11.2. |

### 11.2 Semantic checklist (step 10.2), checked explicitly

| Distinction | Where it was enforced |
|---|---|
| Retention is not read-back | The memory lens carries an explicit `RB` column separating **read-back** from **retained** and **static** across ~60 parts. `subagent_messages` is retained (single-job replay), not cross-task memory. |
| Context presence is not activation | Four separate findings per read-back path (memory §4), with activation `uninspected` in every case. |
| Implementation is not deployment | Recorded on RTE-18 (SkillOpt, default OFF), RTE-32 (bootstrap takes, double-gated off), RTE-37 (nightly probe, default disabled), RTE-41 (pack-gated), and the gateway subagent loop (flag default OFF). |
| Observation is not causality | No `observed` status exists in this run, so no upgrade to causality was available; benchmark contrasts stay `claimed` with the ablation design named as unavailable (L3). |
| Curation is not warrant | Applied to `consolidate` by both lenses (§8.3), to the voice gate (C3), and to fact decay — a freshness function, never a truth verdict. |
| Use is not acceptance | Applied to the proposal queue, the verdict cache, `--save`d syntheses, the contradiction block in the synthesize prompt, and `_meta` injection — all retention or pre-acceptance operational use, none of it lifecycle integration. |
| Behavioral authority is not epistemic or operational authority | Three authority families kept in separate columns throughout `lens-epistemic.md` §3 and restated in §9: surviving source isolation is not evidence of truth; injection frequency licenses nothing. |

### 11.3 Deterministic validation

**Not run.** Step 10.3 directs running "the deterministic validation required by the chosen existing
target contract", falling back to "applicable generic validation" until a dedicated result contract
exists. With no authorized target (§11.4) there is no contract to name a validator, and the trial's
read constraints prevented determining which generic validation would apply to a workshop-staged
result. The step-10.1 structural checks and the step-10.2 semantic checklist were executed by hand
and are reported above. No schema or parser was changed to manufacture a validation path.

### 11.4 Blockers

**Publication blocker — no authorized target contract.** There is no authorized target for this run
whose existing contract can represent this result. Per step 9's publication rule the complete logical
result is **retained under the run's staging identity**
(`kb/work/analyse-agentic-system/trials/gbrain/`) and the blocker is
recorded here rather than worked around. No collection contract was improvised and the agent-memory
review schema was not reused.

**Consequent blocker — validation path unavailable.** §11.3, same root cause.

No other blocker applies. Specifically: no logical record is missing (all eleven present, §0 index);
ID collisions occurred but were resolved centrally before this report rather than left standing; no
material claim in this result is unsupported by an anchor; and no applicable validation failed —
one was unavailable, which is recorded as a blocker rather than reported as a pass.

### 11.5 Report

- **Result identity:** `RUN-GBRAIN-20260820`
- **Location:** `kb/work/analyse-agentic-system/trials/gbrain/` (six files)
- **Boundary:** GBrain repository, declared by function; **subsystem-only w.r.t. the advertised agent
  loop**, whose other half runs in an out-of-boundary host platform
- **Revision:** `9a0bae8d62cdd1e0dd6655e24e082fe6c69c5dac` (`VERSION` 0.42.25.0), clean tree
- **Evidence tier:** `code-grounded`; no `observed`, no `causally supported` anywhere
- **Memory/context lens:** `applicable`, ran
- **Epistemic lens:** `applicable`, ran
- **Limitations:** sixteen, each paired with its prevented conclusion (§10)
- **Blockers:** publication blocker (no authorized target contract) and the consequent validation
  blocker (§11.4)
