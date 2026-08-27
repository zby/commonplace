# Epistemic lens — RUN-GBRAIN-20260820

> **Provenance note (trial apparatus, not part of the lens result).** The epistemic lens worker
> completed this analysis and returned it to the orchestrator, but both the worker and the
> orchestrator were terminated by a usage limit before the file was written to disk. This file was
> recovered verbatim from the worker's returned report. No content was added, and no finding was
> altered. Formatting may differ in trivial ways from the worker's original file layout.

**Scope note (wrapper):** the invoked instruction `kb/instructions/analyse-external-system-epistemic-architecture.md` was run inside the packet's boundary. Its links to further `kb/` files were treated as unavailable per wrapper rule — **limitation L-0: the invoked instruction may reference definitions or sub-procedures that could not be read; any conclusion depending on those is unbounded here.** No system-wide epistemic grade is given (wrapper override; the instruction also forbids it).

---

## 1. Source-and-claim boundary

| Field | Value |
|---|---|
| system | GBrain (github.com/garrytan/gbrain) |
| reviewed revision | `9a0bae8d62cdd1e0dd6655e24e082fe6c69c5dac`, VERSION `0.42.25.0`, commit date 2026-06-03 |
| declared scope | Packet §3 (unchanged, not widened). Whole-repo by function; **subsystem-only w.r.t. the advertised agent loop** — signal detection and the respond step live in the host agent platform, outside the checkout |
| analysis question | Within GBrain's own code and shipped doctrine at 9a0bae8, what routes handle truth-apt content — produced, transformed, checked, accepted, given authority, retained/integrated — and what warrant do the resulting artifacts carry? |
| assessed route families | takes lifecycle (propose → grade → resolve → calibrate); facts lifecycle (extract → decay → consolidate); `think` synthesis + citation + gaps; contradiction probe + resolution proposals; corpus-level quality assays (`eval takes-quality`, cross-modal, nightly probe); page/atom/concept synthesis; auto-link edges; guardrail seams; retention/mirroring routes |
| unassessed route families | hybrid retrieval internals (`hybrid.ts` 1,870 lines — ranking/rerank/expansion, `uninspected`); `operations.ts` body (4,751 lines) beyond named ops; minion scheduling/trust-boundary internals (runtime lens owns these); embedding-provider recipes; `evals/` harness internals; `admin/`; all 1,244 test files except as named; individual `skills/*/SKILL.md` bodies |
| new sources inspected | see §7 file list; all inside the frozen checkout, all `implementation` or `doctrine/design` layer, none reacquired |

### New source IDs (proposed — orchestrator owns registration)

| ID | Identity | Layer | Scope inspected |
|---|---|---|---|
| PROPOSED-SRC-19 | `src/core/cycle/propose-takes.ts` | implementation | full (474 lines) |
| PROPOSED-SRC-20 | `src/core/cycle/grade-takes.ts` | implementation | full (629 lines) |
| PROPOSED-SRC-21 | `src/core/cycle/calibration-profile.ts` | implementation | full (406) |
| PROPOSED-SRC-22 | `src/core/cycle/phases/consolidate.ts` | implementation | full (297) |
| PROPOSED-SRC-23 | `src/core/cycle.ts` | implementation | lines 57–175, 1860–1990 + greps; body elsewhere not line-read |
| PROPOSED-SRC-24 | `src/core/think/index.ts` | implementation | lines 185–220, 270–330, 380–600 |
| PROPOSED-SRC-25 | `src/core/think/cite-render.ts` | implementation | full (123) |
| PROPOSED-SRC-26 | `src/core/think/sanitize.ts` | implementation | full (106) |
| PROPOSED-SRC-27 | `src/core/eval-contradictions/judge.ts` | implementation | full (366) |
| PROPOSED-SRC-28 | `src/core/eval-contradictions/auto-supersession.ts` | implementation | full (202) |
| PROPOSED-SRC-29 | `docs/contradictions.md` | doctrine/design + reported operation | full (166) |
| PROPOSED-SRC-30 | `src/core/guardrails.ts` | implementation | full (137) |
| PROPOSED-SRC-31 | `src/core/takes-resolution.ts` | implementation | full (120) |
| PROPOSED-SRC-32 | `src/commands/takes.ts` | implementation | `cmdResolve` + subcommand dispatch (lines 344–580) |
| PROPOSED-SRC-33 | `src/commands/calibration.ts` | implementation | `getLatestProfile` (lines 40–80) |
| PROPOSED-SRC-34 | `src/core/cycle/nightly-quality-probe.ts` | implementation | full (220) |
| PROPOSED-SRC-35 | `src/core/skillopt/{validate-gate,bundled-skill-gate,score}.ts` | implementation | validate-gate + bundled gate full; score head |
| PROPOSED-SRC-36 | `docs/eval-takes-quality.md` | doctrine/design | full (159) |
| PROPOSED-SRC-37 | `src/core/cycle/synthesize.ts` | implementation | lines 1–70, 890–945 |
| PROPOSED-SRC-38 | `src/core/facts/decay.ts` | implementation | full (63) |
| PROPOSED-SRC-39 | `src/core/extract-takes-from-pages.ts` | implementation | lines 1–80 |
| PROPOSED-SRC-40 | `src/core/cycle/{extract-atoms,synthesize-concepts}.ts` | implementation | heads only (contract comments) |
| PROPOSED-SRC-41 | `src/core/operations.ts` | implementation | `think`, `get_calibration_profile`, `find_contradictions` op definitions only |
| PROPOSED-SRC-42 | `src/core/cross-modal-eval/runner.ts` | implementation | lines 1–50 |
| PROPOSED-SRC-43 | `docs/GBRAIN_VERIFY.md` | doctrine/design | headings only |

### Missing evidence → conclusion prevented (paired)

| Missing evidence | Exact conclusion it prevents |
|---|---|
| No execution of any GBrain command; no DB, no `takes` rows, no `take_grade_cache` rows, no `calibration_profiles` rows, no `synthesis_evidence` rows | **Every observed candidate state below is `no instance observed`.** Prevents: any claim that a take was actually graded, resolved, accepted, or integrated; any claim about real verdict distributions, Brier values, or citation accuracy |
| `gbrain-evals` repo (sibling, outside boundary) | Prevents assessing CLM-11 (P@5/R@5/+31.4pp), CLM-14 (propose_takes F1 0.952/0.922), and the cat15 tuning claim beyond `claimed` |
| No production brain snapshot | Prevents assessing CLM-10 (100,720 takes, 6.8/10 cross-modal) beyond `reported operation` |
| `src/core/search/hybrid.ts` and the rest of `search/*` not line-read | Prevents concluding what evidence set a `think` call actually sees; prevents assessing whether retrieval preserves or degrades source warrant into OBJ-06 |
| `src/core/operations.ts` body (4,751 lines) not line-read | Prevents an exhaustive claim that no other route writes to `takes`/`facts`/`calibration_profiles`; absence findings are scoped to `rg` over `src/` excluding tests |
| Individual `skills/*/SKILL.md` bodies not read | Prevents assessing whether shipped skill doctrine instructs agents to treat `think` output or takes as established fact (BAP-01 content unknown) |
| No causal/interventional evidence anywhere | Prevents any causal attribution for any check, gate, or prompt rule in this run |

---

## 2. Epistemic-object inventory (Required Return 1)

Packet OBJ-* extended by ID; new candidates as `PROPOSED-OBJ-*`.

| ID | Name / description | Form | Source & lineage | Producer → consumer | Candidate truth-apt content | Claimed role | Evidence anchor | Gap/limit |
|---|---|---|---|---|---|---|---|---|
| OBJ-01 | Page (`compiled_truth` markdown + frontmatter + timeline) | natural-language | user/agent authored; imported; dream-written | user, agent, `synthesize` → retrieval, `think`, extractors | **yes** — asserted content about people/companies/events | brain's system of record | SRC-02; PROPOSED-SRC-37 | mixed provenance; no per-page warrant field |
| OBJ-03 | Typed graph edge (`works_at`, `attended`, …) | symbolic | regex/wikilink extraction on every page write, **no LLM** | `put_page` → graph query, graph signals | **yes** — asserts a relation holds | "self-wiring knowledge graph" | SRC-02 README:12,257 | extraction correctness uninspected; edges inherit page warrant unexamined |
| OBJ-04 | Fact row (hot memory) | NL + typed fields (`kind`, `confidence`, `valid_from/until`) | per-turn Haiku/Sonnet extraction from conversation | extractor → `recall`, `_meta.brain_hot_memory`, `consolidate` | **yes** — single-holder (brain owner) assertions | real-time personal knowledge | SRC-10/11/12; PROPOSED-SRC-38 | confidence is model-self-reported; no check route found within boundary |
| OBJ-05 | Take row (cold, attributed claim) | NL + `kind`/`holder`/`weight`/`since`/`active` | LLM extraction from pages; `consolidate` bridge; `takes add` | extractors → `think`, takes CLI/MCP, `grade_takes` | **yes** — attributed claim over a named holder and time | "epistemological layer: WHO believes WHAT" | SRC-13; PROPOSED-SRC-22/39 | `weight` is LLM-inferred from hedging language, not a calibrated probability |
| OBJ-06 | Synthesis answer (+Conflicts+Gaps) | natural-language | `think` LLM call over `<pages>`/`<takes>`/`<graph>`/`<calibration>`/`<trajectory>` | `think` → user / calling agent / optional saved page | **yes** — the system's headline knowledge product | "GBrain gives you the answer" | SRC-08; PROPOSED-SRC-24 | never checked against its inputs before delivery |
| OBJ-07 | Structured citation `(page_slug, row_num)` | symbolic | `think` structured output; regex fallback from body | `think` → `synthesis_evidence` | **yes** — asserts "this claim is supported at slug#row" | citation persistence | PROPOSED-SRC-25 full | **row existence and support relation never verified**; slug existence checked only on `--save` |
| OBJ-08 | Gap statement | natural-language | `think` LLM output field | `think` → user; `--rounds N` scaffold | **yes** — asserts the brain lacks X | "the gap analysis is the differentiator" | SRC-08:55–57; PROPOSED-SRC-24:495–500 | `rounds>1` is not gap-driven (`ROUNDS_GT_1_NOT_GAP_DRIVEN_IN_V028`); gaps are unverified against the corpus |
| OBJ-09 | Take verdict (`take_grade_cache` row: verdict, confidence, evidence_signature, applied) | symbolic + NL | judge model in `grade_takes` | judge → cache row | **yes** — asserts the take turned out correct/incorrect/partial/unresolvable | hindsight grading | PROPOSED-SRC-20:544–551 | evidence input is a placeholder (see M-01); no implemented consumer by default (M-05) |
| OBJ-10 | Calibration profile (patterns + bias tags + Brier + `published`) | NL + symbolic | aggregation of `takes.resolved_*` via `getScorecard`, then LLM narration + voice gate | `calibration_profile` phase → `think` `<calibration>` block, `get_calibration_profile` MCP op | **yes** — asserts a track-record pattern about a holder | debiasing feedback loop | PROPOSED-SRC-21:350–380; PROPOSED-SRC-33 | `published` written `false` and ignored on read (M-06); `grade_completion` always 1.0 (M-07) |
| OBJ-11 | Suspected-contradiction record (verdict ∈ 6-enum, severity, axis, confidence) | symbolic + NL | query-conditioned LLM judge over retrieval pairs, date pre-filtered | judge → `eval_contradictions_runs.report_json` | **yes** — asserts two statements conflict/supersede/regress | contradiction evidence | PROPOSED-SRC-27:173–225, 235–319 | judge sees ≤1500 chars/side; page-level `effective_date` only |
| OBJ-20 | Atom / concept page (lens packs) | natural-language | Haiku atom extraction; Sonnet T1/T2 concept narratives; deterministic T3/T4 stubs | `extract_atoms`, `synthesize_concepts` → retrieval | **yes** — synthesized assertions about a concept | knowledge condensation | PROPOSED-SRC-40 heads | pack-gated, default-off for most packs; no check route found within boundary |
| **PROPOSED-OBJ-21** | Take proposal row (`take_proposals`: claim_text, kind, holder, weight, domain, status) | NL + typed | `propose_takes` LLM extractor over page prose | phase → queue | **yes** — a proposed gradeable claim | "review queue; user accepts/rejects" | PROPOSED-SRC-19:392–415 | **no implemented reader or accept path** (M-02) |
| **PROPOSED-OBJ-22** | Take resolution tuple on the takes row (`resolved_quality`, `outcome`, `resolved_by`, `source`) | symbolic | human `takes resolve`, or auto-apply from OBJ-09 | CLI/engine → `getScorecard` → OBJ-10; markdown fence mirror | **yes** — asserts the take's outcome | recorded disposition | PROPOSED-SRC-31:22–58; PROPOSED-SRC-32 `cmdResolve` | the only implemented, reachable acceptance transition for a take at this revision |
| **PROPOSED-OBJ-23** | Resolution proposal (`resolution_kind` + paste-ready `resolution_command`) | symbolic | deterministic classifier over OBJ-11 + judge hint | classifier → report/doctor/MCP → human | non-truth-apt directive (an imperative), attached to a truth-apt finding | "descriptive, not directive… probe NEVER auto-applies" | PROPOSED-SRC-28:1–24, 58–102 | commands are rendered even when date order is unclear |
| **PROPOSED-OBJ-24** | Takes-quality receipt (`eval_takes_quality_runs`, 5-dim scores, verdict pass/fail/inconclusive, 4-sha key) | symbolic | 3-model frontier panel over a random sample of takes | eval → DB row + disk artifact → trend/regress/CI | **yes** — asserts corpus-level extraction quality at a rubric epoch | CI-able quality gate | PROPOSED-SRC-36 | sample-scoped; no per-take disposition; CI consumer is outside the boundary |
| **PROPOSED-OBJ-25** | Nightly quality-probe audit row (outcome, pass/fail counts, cost, fixture sha8) | symbolic | longmemeval → cross-modal batch judge | probe → `~/.gbrain/audit` JSONL → `doctor` | **yes** — asserts retrieval/answer quality against a committed fixture | nightly regression signal | PROPOSED-SRC-34:176–197 | **default disabled**; fixture-scoped |
| OBJ-12 / OBJ-13 | Subagent turn / tool-execution record | NL blocks / symbolic | subagent loop | loop → crash replay | yes (record-of-what-happened; lineage-preserving) | replay substrate | packet | not material to the analysis question beyond lineage |
| OBJ-02, OBJ-14–OBJ-19 | Chunk+embedding, SKILL.md, SOUL/HEARTBEAT/USER/ACCESS_POLICY, schema pack, job row, audit event, query cache | symbolic / NL-prompt | — | — | **no candidate truth-apt output** (indexing artifacts, instruction artifacts, control records) | — | packet | per-object no-candidate lines in §4 |

---

## 3. Authority-route ledger (Required Returns 2, 4, 5, 6)

One function per row. Architectural status is recorded independently of function; activation is recorded separately.

### 3a. Content transformation routes

| Route | Function | Arch. status | Object | Content/update relation | Activation | Epistemic authority & scope | Operational authority | Behavioral-authority path | Evidence anchor | Claims | Mismatch | Limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| RTE-06 | content transformation | `implemented` | OBJ-04 | truth-apt transformation: **ampliative conjecture** (LLM asserts a fact the turn did not state as such) + partial acquisition | per conversation turn, config-gated | none licensed by the route itself; row carries a model self-reported `confidence` only | writes `facts`; becomes injectable context | BAP-12 (advisory `_meta`, 30s cache) | SRC-10, SRC-12 | CLM-02 | none | extraction fidelity uninspected |
| RTE-09 | content transformation | `implemented` | OBJ-04 → OBJ-05 | **non-ampliative reshaping** (selection + relabel), *not* synthesis | dream cycle, every run; gates: ≥3 facts/bucket, oldest ≥24h, cosine ≥0.85, cluster ≥2 | none; claim text is the highest-confidence fact **verbatim** | INSERTs `takes(kind='fact', holder='self')`; marks facts consolidated; writes `valid_until` chain | none direct | PROPOSED-SRC-22:128–140, 176–201 | CLM-07 | **M-04** | doc and `cycle.ts:1861` both say "Sonnet-synthesize"; code has no LLM call |
| RTE-10 (produce half) | content transformation | `implemented` | OBJ-01 → PROPOSED-OBJ-21 | **ampliative conjecture** (a "gradeable claim" is asserted from prose) | every cycle; idempotency on `(source_id, page_slug, content_hash, prompt_version)`; $5 budget cap | candidate generation only | writes `take_proposals`; **does not touch canonical takes** | none | PROPOSED-SRC-19:300–415 | CLM-08, CLM-14 | **M-03** (prompt emits `prediction`/`judgment`; parser allowlist is `fact/take/bet/hunch` → silently coerced to `take` at :270–272) | prompt-version string claims tuning validated outside boundary |
| PROPOSED-RTE-21 | content transformation | `implemented`, **inactive by default** | OBJ-01 → OBJ-05 | **ampliative conjecture** (Haiku classifier extracts gradeable claims straight into the takes fence) | two consent gates: `takes.bootstrap_enabled` (false) AND `takes.autopilot_allowed` (false); allowlisted page types only; ≤15 claims/page | candidate generation only | writes canonical takes **without any proposal queue** when enabled | none | PROPOSED-SRC-39:1–40 | CLM-02 | none | this is a *second*, gate-only path into `takes` that bypasses RTE-10's queue entirely |
| RTE-05 | content transformation | `implemented` | → OBJ-06, OBJ-07, OBJ-08 | **ampliative conjecture** (synthesis across retrieved pages/takes) | every `think` call | candidate generation only; no check consumes the output before delivery | returns the answer; optional `--save` persists a page | BAP-08 (advisory prompt rules), BAP-09 (advisory + partial code enforcement) | SRC-08 full; PROPOSED-SRC-24 | CLM-01, CLM-03 | none at prompt level; **M-08** at verification level | prompt *mandates* citation; nothing *verifies* it |
| PROPOSED-RTE-30 | content transformation | `implemented`, pack-gated | → OBJ-20 | **ampliative conjecture** | only when the active schema pack declares the phase (`gbrain-creator`, `gbrain-everything`) | candidate generation only | writes atom/concept pages into retrieval | none | PROPOSED-SRC-40 | — | none | heads only; bodies uninspected |
| RTE-14 | content transformation | `implemented` | → OBJ-03 | **entailed derivation** within a declared syntactic domain (wikilink/typed-link syntax → edge), **no LLM** | every page write | edge warrant = page warrant; derivation is syntactic, not semantic | writes `links`; feeds graph signals into ranking | none | SRC-02 README:12,257 | CLM-11 | none | correctness of the regex domain uninspected |
| RTE-15 | lineage/freshness/recovery | `implemented` | OBJ-01 | **acquisition/import**; source warrant **preserved** (git repo is system of record; DB is derived) | on `sync` | no new warrant | soft-deletes, re-chunks, re-embeds | none | packet | — | none | — |

### 3b. Check / evidence-production routes (Required Return 5, checking)

| Route | Check target (named first) | Evaluator & domain | Arch. status | Activation/timing | Possible result | Implemented force | Epistemic authority & scope | Operational authority | Behavioral-authority path | Evidence anchor | Limit |
|---|---|---|---|---|---|---|---|---|---|---|---|
| RTE-11 | **OBJ-05, one take, over "did the world play out as claimed"** | single judge model (Sonnet default), NL domain | `implemented`, **but its evidence input is `absent`** | dream cycle; `since_date` ≥6 months old; ≤50 takes/run; $3 cap; idempotent on `(take_id, prompt_version, judge_model_id, evidence_signature)` | verdict ∈ correct/incorrect/partial/unresolvable + self-reported confidence; parse failure → `unresolvable @ 0.0` | **none by default** — row written with `applied=false`; no implemented reader (M-05) | Licenses **nothing about the world.** The judge's only "evidence" is the take's own claim text plus its date | none by default | none | PROPOSED-SRC-20:296–305 (`defaultEvidenceRetriever` returns `[evidence retrieval not yet wired — v0.36.1.0 ship-state]`), :391, :439; PROPOSED-SRC-23:1930 (`runPhaseGradeTakes(calibrationCtx, {})` — no retriever injected) | **M-01.** `src/core/search/evidence.ts` is unrelated (it classifies *retrieval-hit strength*, not take evidence — read in full) |
| RTE-11b | same target, ensemble path | 3 judges, unanimity + min-confidence ≥0.85 | `implemented`, **inactive in the inspected configuration** | `useEnsemble` defaults false and `ensembleJudges` is never supplied by any production caller | ensemble verdict | none | — | none | none | PROPOSED-SRC-20:400–402, 487; PROPOSED-SRC-23:1930 | reachable only through test injection |
| RTE-13 | **pair (chunk/take, chunk/take) over "do these conflict on a claim relevant to this query"** | query-conditioned LLM judge (Haiku default), NL domain | `implemented` | `gbrain eval suspected-contradictions`, operator-initiated; date pre-filter >30d; ≤1500 chars/side; persistent cache keyed on `(chunk_a_hash, chunk_b_hash, model, prompt_version, truncation_policy)` | 6-value verdict + severity + axis + confidence; `contradiction` below 0.7 confidence **downgraded in code** to `no_contradiction`; refusal/parse-fail counted in `judge_errors` denominator | **advisory only** — probe never mutates brain state | Licenses: "a judge, seeing ≤1500 chars of each side plus page-level `effective_date`, called this pair conflicting w.r.t. this query." Does **not** license that the pair conflicts, nor which side is true | writes only to `eval_contradictions_runs` / `_cache` | `find_contradictions` MCP op (read scope, **not** in subagent allowlist → user-initiated only); doctor findings; PROPOSED-RTE-23 into the synthesize prompt | PROPOSED-SRC-27:173–225, 235–319, 337–366; PROPOSED-SRC-29:137–143 | Wilson CI + `small_sample_note` at n<30 are honest sampling caveats; no ground-truth labels — the judge is the oracle for its own metric |
| PROPOSED-RTE-25 | **a random sample of OBJ-05 rows, over a 5-dim rubric (accuracy, attribution, weight calibration, kind classification, signal density)** | 3-provider frontier panel, NL rubric domain | `implemented` | `gbrain eval takes-quality run`, operator/CI initiated | `pass` (every dim mean ≥7 AND every dim min ≥5) / `fail` / `inconclusive` (<2/3 models contributed complete scores) | receipt persisted; exit code 0/1/2 | Licenses a **corpus-and-rubric-epoch-scoped** quality statement, fingerprinted by `corpus_sha8`/`prompt_sha8`/`models_sha8`/`rubric_sha8`. Does **not** license any individual take | CI gate (consumer outside boundary); `trend`/`regress` | none inside the boundary | PROPOSED-SRC-36 (verdict rule at :87–89) | no per-take disposition; `regress` surfaces sha diffs as warnings and does not refuse |
| PROPOSED-RTE-26 | **retrieval+answer quality against a committed fixture** | longmemeval → cross-modal 3-model batch judge | `implemented`, **default disabled** | opt-in `autopilot.nightly_quality_probe.enabled`; 24h rate limit; needs an embedding provider | pass/fail/inconclusive/error/budget_exceeded/rate_limited/no_embedding_key | audit JSONL row → `doctor` | Licenses a fixture-scoped quality statement at a fixture sha8 | none automatic | doctor surfaces a paste-ready enable hint | PROPOSED-SRC-34:97–219 | fixture-scoped; no interventional design |
| PROPOSED-RTE-27 | **content crossing 5 named boundaries** (markdown/code pre-persist, chat, expansion, tool input) | external provider classifier | `implemented`, **zero providers registered by default** | inline await at hook points | provider-internal verdict, **explicitly ignored** (`runGuardrails` returns `void`) | **no implemented force by design** — documented hard invariant: observe-only, fail-open, no verdict persistence | none | none | none | PROPOSED-SRC-30:15–33, 114–137 | a recorded-result-with-no-consumer case: GBrain does not even record it |
| — | **support relation between OBJ-06 claims and their cited OBJ-05/OBJ-01 sources** | — | **`no route found within boundary`** | — | — | — | — | — | — | PROPOSED-SRC-25 full (regex fallback promotes any `[slug]`-shaped bracket to a citation); PROPOSED-SRC-24:185–220 | **M-08.** Slug existence is checked only in `persistCitations`, i.e. only on `--save`; `row_num` existence is never checked; entailment is never checked |
| — | **truth of OBJ-04 facts** | — | **`no route found within boundary`** | — | — | — | — | — | — | greps over `src/core/facts/*` | decay (`effectiveConfidence`) is a **freshness** function, not a check — do not read a decayed confidence as a truth verdict |

### 3c. Disposition / acceptance routes (Required Return 5, acceptance)

| Route | Function | Arch. status | Evaluator | Criterion | Intended use & scope | Result | Force | Epistemic authority | Operational authority | Behavioral-authority path | Evidence anchor | Mismatch |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| RTE-10 (accept half) | disposition/acceptance | **`doctrine only`** | declared: human operator via `gbrain takes propose --accept N` | none implemented | — | — | **none** | — | — | BAP-10 as declared | **`gbrain takes propose` does not exist.** `src/commands/takes.ts` dispatch (:566–574) has only `search/add/update/supersede/resolve/scorecard/calibration/revisit/extract`. Repo-wide `rg take_proposals` outside schema/migrate/tests hits only `propose-takes.ts` itself and `KEY_FILES.md`. The `status` column is written never and read never | **M-02** vs CLM-08 |
| **PROPOSED-RTE-22** | disposition/acceptance | `implemented` | **human operator** | operator's own judgement; `--quality correct/incorrect/partial/unresolvable` (+ optional `--evidence`, `--value/--unit`, `--by`) | resolves one take; enters the Brier/accuracy denominators | `resolved_quality` + `outcome` tuple, consistency-checked (`deriveResolutionTuple` throws on `--quality`/`--outcome` disagreement; schema CHECK is defense-in-depth) | **binding** — writes the canonical takes row and mirrors into the markdown fence | Licenses "the operator recorded this outcome," scoped to that take. Not an oracle claim | changes scorecard inputs → OBJ-10 | operator-invoked CLI only | PROPOSED-SRC-32 `cmdResolve`; PROPOSED-SRC-31:22–58 | none |
| RTE-11 (auto-apply half) | disposition/acceptance | `implemented`, **unreachable via the production path** | judge model | `confidence ≥ 0.95` single, or 3/3 unanimous with min ≥0.85; `unresolvable` **never** auto-applies | would resolve the take | `engine.resolveTake` | **none in production** — `autoResolve = opts.autoResolve ?? false`, and the only production caller (`cycle.ts:1930`) passes `{}`. The documented config key `cycle.grade_takes.auto_resolve.enabled` **is read nowhere in `src/`** and is not in `src/core/config.ts`'s key list | — | — | — | PROPOSED-SRC-20:395–396, 527–533; PROPOSED-SRC-23:1930; `rg auto_resolve src/` | **M-09**: doctrine says the operator "flips the flag once trust is earned"; the flag has no reader |
| RTE-18 | disposition/acceptance | `implemented` | LLM/rule/qrels judge, median-of-3 | `sel_score > best_score + 0.05` (strict; ties and sub-ε gains rejected) | accepts a candidate SKILL.md version | accept/reject + per-task medians | **binding** on the version store | *not* a truth claim — see §3e | mutates SKILL.md (user-owned) or writes `proposed.md` (bundled) | BAP-01 (skillpack → host agent prompt) | PROPOSED-SRC-35 validate-gate:118–128 | — |
| RTE-18b | operational admission | `implemented` | code | bundled skill + no `--allow-mutate-bundled` → never mutate; in-place bundled mutation **hard-refuses** without a held-out set ≥ `MIN_HELD_OUT_SIZE` | protects shipped skills | proposed.md, or throw | **binding enforcement** | none | blocks a write | BAP-10 | PROPOSED-SRC-35 bundled-skill-gate:62–100 | — |

### 3d. Retention / lifecycle-integration routes (Required Return 5, retention/integration — kept separate)

| Route | Function | Arch. status | Object | Content relation | Force | Notes |
|---|---|---|---|---|---|---|
| RTE-10 (write half) | **retention** (not integration) | `implemented` | PROPOSED-OBJ-21 | no content change after generation | rows persist | Retained **without acceptance**; the queue is write-only at this revision |
| RTE-11 (cache write) | **retention** | `implemented` | OBJ-09 | no content change | rows persist with `applied=false` | Retained without acceptance and, by default, without any consumer |
| RTE-12 | **retention + context** | `implemented` | OBJ-09-derived → OBJ-10 | non-ampliative reshaping (aggregation) then **ampliative conjecture** (LLM narrates patterns; second LLM emits bias tags) | writes `calibration_profiles` | Two linked edges. The aggregation reads `takes.resolved_*` (i.e. PROPOSED-OBJ-22), **not** `take_grade_cache` — so with auto-resolve unreachable, the profile is built from **human-recorded** resolutions only |
| PROPOSED-RTE-29 | **retention / lineage** | `implemented` | OBJ-05, PROPOSED-OBJ-22 | no content change | mirrors DB rows into the page's `<!-- gbrain:takes:begin -->` fence | Makes the git repo self-describing; keeps the markdown system-of-record and DB in sync |
| PROPOSED-RTE-28 | **retention → later reliance** | `implemented` | OBJ-06 → OBJ-01 | acquisition of the system's own output into its corpus | `think --save` writes `synthesis/<slug>-<date>` with `type: synthesis`, then `persistCitations` | **Circularity route.** An unchecked ampliative synthesis becomes a retrievable page that later `think` calls can surface and cite. `synthesisOk === false` blocks empty/malformed persistence (#1698) — a *non-emptiness* guard, not a truth check |
| PROPOSED-RTE-23 | **lifecycle-relevant read-back** (pre-acceptance use, **not** integration) | `implemented` | OBJ-11 → dream `synthesize` prompt | no content change | top-5 findings by severity injected as an informational block with reconcile guidance; silent `''` on any failure | Advisory. Findings were never accepted; this is pre-acceptance operational use |
| PROPOSED-RTE-24 | **disposition proposal** (not disposition) | `implemented` | OBJ-11 → PROPOSED-OBJ-23 | non-truth-apt policy/content update: renders an imperative | deterministic classifier + judge hint; **never auto-applies** (invariant pinned by an R1+R8 grep guard) | Only `consolidate` writes `valid_until`; the probe writes nothing to the brain |
| RTE-12 → BAP-08 | **operational consumption** | `implemented`, **CLI-only** | OBJ-10 → `think` | no content change | `--with-calibration` CLI flag; `getLatestProfile` **ignores the `published` column** while the writer always sets `published=false` | **M-06.** The MCP `think` op exposes no calibration parameter, so the loop is unreachable for agent callers — **M-10** |
| RTE-07 / RTE-08 | **operational consumption** | `implemented` | OBJ-04 | no content change | `_meta.brain_hot_memory` push (30s cache) and `recall` pull | BAP-12: advisory; client may ignore unknown `_meta` |
| RTE-16 / BAP-06 / BAP-07 | **operational admission** | `implemented` | all | no content change | `scope` + `localOnly` + `OperationContext.remote` fail-closed; `sourceScopeOpts` SQL predicate; `takesHoldersAllowList` | Binding enforcement. Purely operational — **no epistemic license whatsoever**; a claim that survives source isolation is not thereby warranted |

### 3e. Routes set aside as direct behavior/policy adaptation (Required Return, explicit flag)

These have **no truth-apt object and no knowledge/warrant claim**. They belong to the runtime account, not to this lens. Named so the orchestrator can route them:

| Route | Why set aside |
|---|---|
| **RTE-18 / RTE-18b (SkillOpt)** | Target is `SKILL.md` — a prescriptive instruction artifact. Its gate measures *task performance* (`sel_score`), not truth. A real acceptance transition with a named criterion exists, but what it accepts is a **policy**, not a claim. Flagged, not disposed here. |
| **RTE-17 (skillpack install → host prompt)** | Static shipped instruction material; per the packet's vocabulary this is retained state, not memory read-back. |
| **RTE-19 (schema-pack activation)** | Configuration changing parse/extract/route/cache-key behavior. No truth-apt object. |
| **RTE-01, RTE-02, RTE-03 (job queue, subagent loop, cycle orchestration)** | Control routes. `no content change` from an epistemic standpoint. |
| **RTE-20 (audit JSONL → doctor)** | Observability. Records events, asserts nothing about the world. |
| **RTE-04 (hybrid retrieval)** | Non-ampliative reshaping (ranking/selection) — it changes *which* truth-apt content reaches a consumer without changing content. Material to OBJ-06's warrant, but its internals are `uninspected` (see §1 missing evidence). |
| **PROPOSED-RTE-27 (guardrails)** | Observe-only by hard invariant; no verdict is consumed, persisted, or branched on. |
| **`gbrain doctor` / `docs/GBRAIN_VERIFY.md`** | Installation and schema verification. Despite the name "verify," the target is **configuration and coverage**, not content truth — `inapplicable` to this lens. |

---

## 4. Per-object lifecycle disposition (Required Return 4: architectural status separate from observed candidate state)

**Global note:** nothing was executed in this run. Therefore **every observed candidate state below is `no instance observed`**, and no implementation or doctrine anywhere in §3 upgrades that.

### Ampliative truth-apt candidates

**OBJ-05 (take row)** — routes RTE-09, RTE-10, PROPOSED-RTE-21, RTE-11, PROPOSED-RTE-22, RTE-12, PROPOSED-RTE-29

| Phase | Routes | Architectural status | Observed candidate state | Evidence |
|---|---|---|---|---|
| observation/anomaly | RTE-06, RTE-15, RTE-10 | `implemented` (page prose / conversation turns are the input) | no instance observed | PROPOSED-SRC-19:322–341 |
| conjecture | RTE-10, PROPOSED-RTE-21, RTE-09 | `implemented` (RTE-10 to a queue; PROPOSED-RTE-21 straight to canonical, double-gated off; RTE-09 is reshaping, not conjecture) | no instance observed | PROPOSED-SRC-19, -39, -22 |
| derived consequence | — | **`no route found within boundary`** — nothing derives a testable consequence from a take; grading asks the judge to re-read the claim itself | no instance observed | PROPOSED-SRC-20:52–77 |
| test/evidence | RTE-11 | route `implemented`; **its evidence-retrieval input `absent`** (placeholder string; production caller injects nothing) | no instance observed | PROPOSED-SRC-20:296–305, :391, :439; PROPOSED-SRC-23:1930 |
| acceptance | RTE-10-accept: **`doctrine only`** (no `takes propose` command exists) · RTE-11-auto-apply: `implemented` but **unreachable** (config key has no reader) · PROPOSED-RTE-22: **`implemented`** (human `takes resolve`, criterion = operator judgement, intended use = enter the scorecard, scope = that take) | as stated per sub-route | no instance observed | PROPOSED-SRC-32; PROPOSED-SRC-31 |
| lifecycle integration | RTE-12 (accepted resolutions → scorecard → OBJ-10 → `think` framing), PROPOSED-RTE-29 (fence mirror) | `implemented` for the human-accepted path only; CLI-only at the `think` end | no instance observed | PROPOSED-SRC-21; PROPOSED-SRC-33 |
| **missing phase/evidence** | Consequence derivation is absent as a route. Test is present as a route but empty of evidence. **Retention (RTE-10 write, RTE-11 cache write) happens without acceptance — this is not lifecycle integration.** | | | |

**PROPOSED-OBJ-21 (take proposal)** — routes RTE-10

| Phase | Routes | Arch. status | Observed state | Evidence |
|---|---|---|---|---|
| observation/anomaly, conjecture | RTE-10 | `implemented` | no instance observed | PROPOSED-SRC-19:377–415 |
| derived consequence, test/evidence | — | `no route found within boundary` | no instance observed | — |
| acceptance | declared human gate | **`doctrine only`** | no instance observed | M-02 |
| lifecycle integration | — | **`not reached`** as an architectural matter: with no acceptance route, integration cannot occur | no instance observed | — |
| missing | An implemented reader, an accept command, and any writer of `take_proposals.status` | | | |

**OBJ-06 / OBJ-07 / OBJ-08 (synthesis answer, citations, gaps)** — routes RTE-05, PROPOSED-RTE-28

| Phase | Routes | Arch. status | Observed state | Evidence |
|---|---|---|---|---|
| observation/anomaly | RTE-04 → RTE-05 gather | `implemented` (retrieval internals uninspected) | no instance observed | PROPOSED-SRC-24:260–290 |
| conjecture | RTE-05 | `implemented` | no instance observed | SRC-08 |
| derived consequence | — | `no route found within boundary` | no instance observed | — |
| test/evidence | — | **`no route found within boundary`** for the support relation; only a **non-emptiness** guard (`synthesisOk`) and, on `--save` only, a **slug-existence** check | no instance observed | PROPOSED-SRC-24:185–220, 533–540; PROPOSED-SRC-25:112–123 |
| acceptance | — | **`no route found within boundary`** — the answer is delivered to the user/agent with no evidence-consuming disposition | no instance observed | — |
| lifecycle integration | PROPOSED-RTE-28 | **`not reached`** — `--save` is **retention and later reuse without acceptance**, explicitly not integration under the method's rule | no instance observed | PROPOSED-SRC-24:527–572 |
| missing | Any implemented verifier that a cited `(slug, row_num)` exists in the prompt's evidence and supports the sentence it is attached to | | | |

**OBJ-09 (take verdict)** — routes RTE-11, RTE-12

| Phase | Routes | Arch. status | Observed state | Evidence |
|---|---|---|---|---|
| conjecture | RTE-11 | `implemented` | no instance observed | PROPOSED-SRC-20:310–340 |
| test/evidence | RTE-11 retriever | **`absent`** | no instance observed | M-01 |
| acceptance | auto-apply | `implemented` but unreachable via production path | no instance observed | M-09 |
| lifecycle integration | — | **`not reached`**: the cache row is retained; no implemented consumer reads it by default (only `doctor`'s `applied=true` count and `undo-wave`'s rollback) | no instance observed | `rg take_grade_cache src/` |

**OBJ-10 (calibration profile)** — routes RTE-12, BAP-08

| Phase | Routes | Arch. status | Observed state | Evidence |
|---|---|---|---|---|
| observation | `getScorecard` over resolved takes; cold-brain skip at <5 resolved | `implemented` | no instance observed | PROPOSED-SRC-21:247–259 |
| conjecture | pattern-statement LLM + bias-tag LLM | `implemented` | no instance observed | PROPOSED-SRC-21:126–160 |
| test/evidence | **voice gate** (2 regeneration attempts, then hand-written template fallback) | `implemented` — but the gate's target is **register/tone**, not truth; a template fallback produces a statement that passed *no* content check | no instance observed | PROPOSED-SRC-21:287–306 |
| acceptance | `published` column | **`doctrine only` in effect** — always written `false`, never read | no instance observed | **M-06**: PROPOSED-SRC-21:357 vs PROPOSED-SRC-33:50–68 |
| lifecycle integration | `<calibration>` block → `think` framing | `implemented`, **CLI-only** | no instance observed | **M-10**: PROPOSED-SRC-41 (`think` op params lack calibration) |

**OBJ-11 (suspected contradiction)** — routes RTE-13, PROPOSED-RTE-23, PROPOSED-RTE-24

| Phase | Routes | Arch. status | Observed state | Evidence |
|---|---|---|---|---|
| observation | retrieval pair sampling + date pre-filter | `implemented` | no instance observed | PROPOSED-SRC-29:24–70 |
| conjecture + test/evidence | RTE-13 judge (linked rows — the judge both conjectures the conflict and is the only evaluator of it) | `implemented` | no instance observed | PROPOSED-SRC-27 |
| acceptance | — | **`no route found within boundary`** — by design; `NEVER auto-applies` is a stated invariant | no instance observed | PROPOSED-SRC-28:1–24 |
| lifecycle integration | PROPOSED-RTE-23 (synthesize prompt), `find_contradictions` MCP | **`not reached`** — pre-acceptance advisory use | no instance observed | PROPOSED-SRC-37:890–932 |

**OBJ-04 (fact row)**, **OBJ-01 (page)**, **OBJ-20 (atom/concept page)** — ampliative or mixed; **conjecture `implemented`; derived-consequence, test, and acceptance all `no route found within boundary`; retention `implemented`; lifecycle integration `not reached`.** For OBJ-04 the only post-write transformation is decay (freshness, not endorsement) and RTE-09 promotion (reshaping, not acceptance).

### Non-ampliative truth-apt content

- **OBJ-03 (typed edge)** — routes RTE-14. Transformation: **entailed derivation** within a declared syntactic domain. Discovery lifecycle: not applicable. Warrant: carries the source page's warrant through a syntactic (not semantic) interpretation; the edge asserts the relation only as strongly as the page did. Limit: the regex domain's fidelity is uninspected.
- **OBJ-01 imported pages** — route RTE-15. Transformation: **acquisition/import**, source warrant **preserved** (git is the system of record; DB is derived). Limit: warrant of the *original* source is unknown and unrecorded — GBrain has no source-warrant field.
- **OBJ-12, OBJ-13** — acquisition of execution records; lineage preserved for replay; no ampliation.

### Indeterminate

- **PROPOSED-OBJ-22 (resolution tuple)** — when produced by the human path it is an operator assertion (acquisition of a human judgement, warrant = the operator's). When produced by auto-apply it would be ampliative. Classifications still possible: acquisition vs ampliative conjecture. Preserved lineage: `resolved_by` + `source` fields distinguish them. Evidence needed to decide: an observed row.

### Per-object no-candidate lines

- `No lifecycle record for OBJ-02: no candidate truth-apt output for this object; relevant direct-adaptation or update routes: RTE-04.`
- `No lifecycle record for OBJ-14: no candidate truth-apt output for this object; relevant direct-adaptation or update routes: RTE-18, RTE-17.`
- `No lifecycle record for OBJ-15: no candidate truth-apt output for this object; relevant direct-adaptation or update routes: RTE-17.`
- `No lifecycle record for OBJ-16: no candidate truth-apt output for this object; relevant direct-adaptation or update routes: RTE-19.`
- `No lifecycle record for OBJ-17: no candidate truth-apt output for this object; relevant direct-adaptation or update routes: RTE-01.`
- `No lifecycle record for OBJ-18: no candidate truth-apt output for this object; relevant direct-adaptation or update routes: RTE-20.`
- `No lifecycle record for OBJ-19: no candidate truth-apt output for this object; relevant direct-adaptation or update routes: RTE-04.`
- `No lifecycle record for PROPOSED-OBJ-23: no candidate truth-apt output for this object (it is an imperative); relevant direct-adaptation or update routes: PROPOSED-RTE-24.`

---

## 5. Claims register and route comparison (Required Return 3)

Truth / scope / warrant fields per claim, plus the instruction's cross-layer comparison.

| ID | Claim (truth-apt content asserted) | Scope | Source anchor & layer | Doctrine support | Implemented routes | Observed-run | Causal | Conclusion status | Warrant this run can grant | Mismatch |
|---|---|---|---|---|---|---|---|---|---|---|
| **CLM-01** | "Search gives you raw pages. GBrain gives you the answer" — synthesized, well-cited prose plus explicit gap analysis | the `think` product generally | `README.md:3,11,167` — doctrine/design + marketing | strong | RTE-05 (+RTE-04) `implemented` | none | none | **`implemented`** as a *generation* capability; **`claimed`** as a warrant capability | Warrants "GBrain generates a synthesis with citation markers and a Gaps section." Does **not** warrant that the answer is well-cited, since no route checks the citation-support relation (M-08) | scope mismatch: "the answer" reads as a knowledge claim; the implementation is unchecked candidate generation |
| **CLM-02** | `takes` stores attributed, typed, weighted, time-scoped claims; conflating takes and facts is a "category error"; facts→takes is one-way | the two storage layers | `docs/takes-vs-facts.md` (whole) — doctrine/design | strong | schema + RTE-09 one-way bridge `implemented`; PROPOSED-RTE-21 is a *second* entry to `takes` that skips the queue | none | none | **`implemented`** for the schema and one-way direction | Warrants the *structural* separation | none on directionality |
| **CLM-03** | `think` mandates citing every substantive claim, explicit marking of `weight<0.5`/`hunch`, a Conflicts section, a Gaps section, and never instructing the user | one `think` call | `src/core/think/prompt.ts:48–58` — implementation of a *prompt* | strong | RTE-05, BAP-08 | none | none | **`implemented` as instruction text; `claimed` as behavior** | Warrants "the model was told." **Context presence is not activation** — nothing in the boundary tests compliance | none in the text; the gap is between instruction and enforcement |
| **CLM-04** | `grade_takes` "retrieves evidence and asks a judge model to verdict unresolved takes" | the grading phase | trigger evidence; `cycle.ts:63–66`; `KEY_FILES.md:421` — doctrine/design | declared | judge call `implemented`; **evidence retrieval `absent`** | none | none | **partially `absent`** | Warrants only "a judge model was asked about the claim text." **M-01** | **Yes, material.** `defaultEvidenceRetriever` returns a literal placeholder; the sole production caller injects no retriever. `KEY_FILES.md` states the false version as current behavior |
| **CLM-05** | `calibration_profile` aggregates resolved verdicts into pattern statements, bias tags and a Brier score, fed back into the `think` prompt | one holder, one source | trigger evidence; `calibration-profile.ts:1–26`; `prompt.ts:88–96` — implementation + doctrine | strong | RTE-12 `implemented`; feedback **CLI-only** | none | none | **`implemented`** with two activation caveats | Warrants the aggregation and the injection path on the CLI. Brier excludes `partial` and `unresolvable` from its denominator by design (`takes-resolution.ts:78–89`) — a real, documented scope limit | **M-06** (`published` inert), **M-07** (`grade_completion` always 1.0), **M-10** (no MCP path) |
| **CLM-06** | `eval-contradictions` samples retrieval pairs and runs a query-conditioned LLM judge to surface conflicts | sampled query set | trigger evidence; `docs/contradictions.md`; `judge.ts` — doctrine + implementation | strong | RTE-13 `implemented` | none (Wilson-CI numbers in the doc are illustrative) | none | **`implemented`** | Warrants "a judge, on truncated inputs, classified these pairs." The Wilson CI and `small_sample_note` are honest sampling discipline. Judge is its own oracle — no labeled ground truth | none |
| **CLM-07** | The `consolidate` bridge adds "proper attribution, deduplication, and temporal reasoning"; `cycle.ts` says it "Sonnet-synthesize[s] one take per cluster" | the promotion phase | `docs/takes-vs-facts.md:55–66`; `cycle.ts:1861` — doctrine/design | declared | `implemented` but **materially different**: claim text is the highest-confidence fact **verbatim**; `holder` hardcoded `'self'`, `kind` hardcoded `'fact'`; dedup is an exact `(page_id, claim, since_date)` match; temporal reasoning = a `valid_until` chronological chain | none | none | **`implemented` with a doctrine mismatch** | Warrants "clustered facts were relabelled and promoted." Does **not** warrant attribution reasoning or synthesis | **M-04.** The code's own comment (`consolidate.ts:9–12`) concedes "v0.31 ships without LLM synthesis"; the phase-orchestrator comment and the user-facing doc were not updated |
| **CLM-08** | `propose_takes` writes only to a review queue; "Operator opt-in via `gbrain takes propose --accept N` is the only path from queue to canonical fence"; "auto-accept is intentionally NOT a thing — user always reviews" | the proposal queue | `propose-takes.ts:20–23`; `cycle.ts:63` — doctrine/design | strong | write half `implemented`; **accept half `absent`** | none | none | **first conjunct `implemented`; second conjunct `absent`** | Warrants "nothing auto-promotes." Does **not** warrant that a review path exists | **M-02, material.** Not a safety failure — a *completeness* failure. The safe half shipped; the acceptance half did not. Proposals accumulate with no disposition |
| **CLM-09** | Auto-resolve is OFF by default; verdicts land `applied=false` in a "review-queue posture" pending operator trust | grading disposition | `grade-takes.ts:11–21` — doctrine/design | strong | default-off `implemented`; **the documented enabling config key has no reader**; **no review-queue surface exists** | none | none | **`implemented` (off) + `absent` (the enable path and the queue surface)** | Warrants "no take is auto-resolved via the cycle at this revision" — a strictly *stronger* safety property than documented | **M-09, M-05** |
| **CLM-10** | First full extraction run: 100,720 takes from 28,256 pages, 6,239 holders, $361.49, 0.3% errors; cross-modal 6.8/10 with per-dimension scores | one 2026-05-10 production run | `docs/takes-vs-facts.md:67–86` — **reported operation** | reported | the extraction machinery is `implemented` | **not inspectable here** | none | **`claimed`** | Warrants nothing beyond "the maintainer reports this." The self-reported weak dimension (attribution 6.5, "holder/subject confusion was #1 issue") is a candid quality signal, not a verified one | none |
| **CLM-11** | P@5 49.1%, R@5 97.9%, +31.4 P@5 over the graph-disabled variant and over BM25+vector RAG, on a 240-page Opus-generated corpus | that corpus | `README.md:12` — **reported operation**; runs live in `gbrain-evals`, outside the boundary | reported | RTE-14 + RTE-04 `implemented` | not inspectable | **not assessable** — the "+31.4 vs graph-disabled variant" is described as an ablation contrast, but its design, sampling, and confounds are outside the boundary | **`claimed`** | No component effect may be attributed from this run. A contrast is necessary but not sufficient for causal identification, and the design is not visible | none detectable here |
| **CLM-12** | The contradiction probe "NEVER auto-applies"; only `consolidate` writes `valid_until` | probe mutations | `auto-supersession.ts:1–24`; `docs/contradictions.md:137–143,160–166` | strong | `implemented` — classifier renders strings; a grep guard pins the invariant | none | none | **`implemented`** | Warrants the read-only posture of the probe | none |
| **CLM-13** | Guardrails are observe-only, fail-open, non-persisting; zero registered by default | the 5 hook points | `guardrails.ts:15–33` | strong | `implemented` | none | none | **`implemented`** | Warrants "no guardrail verdict can block or alter GBrain behavior through this interface" | none — the doc is unusually precise about its own non-force |
| **CLM-14** | The propose_takes extractor prompt is tuned; F1 0.952 train / 0.922 holdout, gap 0.03, validated via `gbrain-evals` cat15 | the extractor prompt vs a synthetic hand-labeled corpus | `propose-takes.ts:25–34, 58–84` — doctrine inside implementation | declared | prompt `implemented`; the eval is outside the boundary | not inspectable | none | **`claimed`** | Warrants nothing about live extraction. The file's own later comment (`:218–222`) still calls the production prompt "a placeholder" — the file contradicts itself | internal doctrine inconsistency |
| **CLM-15** | `gbrain eval takes-quality` gates on `pass` = every dim mean ≥7 and every dim min ≥5; `inconclusive` when <2/3 models contribute | one sampled corpus at one rubric epoch | `docs/eval-takes-quality.md:87–89` | strong | PROPOSED-RTE-25 `implemented` | none | none | **`implemented`** | Warrants a corpus-and-rubric-scoped quality statement, fingerprinted by 4 shas. **Does not transfer to any individual take**, and bundle success does not license a component effect | none |

---

## 6. Bounded conclusion (Required Returns 6, 7 folded in)

Findings that change the answer to the analysis question. Route-level verbs only; no system-wide grade.

**What it retains, retrieves, reshapes, and uses.** GBrain retains truth-apt content in five distinct stores with different producers and authorities: pages (git as system of record, DB derived), typed edges, hot `facts`, cold `takes`, and derived artifacts (verdicts, profiles, contradiction reports, synthesis pages). Retrieval (RTE-04) reshapes non-ampliatively; its internals are `uninspected`, which bounds every warrant statement about OBJ-06. Fact decay is a **freshness** function, not endorsement — a high effective confidence means "recent and the extractor was confident," never "checked."

**What it acquires, and what happens to source warrant.** RTE-15 preserves source warrant in the sense that git remains authoritative over the DB. But GBrain records **no source-warrant field anywhere**: an imported page, a hand-written page, and a `think --save` synthesis page are the same `pages` row modulo `type`. Consequently, when a synthesis page written by PROPOSED-RTE-28 is retrieved by a later `think` call, its status as unchecked model output is not carried with it. This is a lineage-degradation route, and it is `implemented`.

**What it derives from warranted premises.** Only RTE-14 (typed edges) and RTE-09 (facts→takes reshaping). RTE-14 is an entailed derivation within a *syntactic* domain and carries page warrant no further than the page had it. RTE-09 is non-ampliative selection: it does not add attribution reasoning, contrary to CLM-07.

**What it conjectures.** RTE-05 (`think` answers, citations, gaps), RTE-06 (facts), RTE-10 and PROPOSED-RTE-21 (takes), RTE-11 (verdicts), RTE-12 (calibration narratives), RTE-13 (contradiction findings), PROPOSED-RTE-30 (atoms/concepts). All are ampliative. Novelty, fluency, and plausibility establish candidate generation only.

**What it tests.** Three genuine check routes exist, and they check three different things, none of which is "is this claim true":

- RTE-13 checks **pairwise consistency relative to a query**, on truncated inputs, with an LLM as its own oracle and no labeled ground truth. Advisory force only.
- PROPOSED-RTE-25 and PROPOSED-RTE-26 check **aggregate quality against rubrics and fixtures**, with real fingerprinting discipline. Corpus- and fixture-scoped. **Bundle success here licenses nothing about any individual take or answer.**
- RTE-11 is architecturally a per-claim test, and it is the one that matters most for the system's warrant story — and **at this revision it consumes no evidence.** The retriever is a placeholder that hands the judge the take's own claim text; the sole production caller injects no replacement. A verdict from RTE-11 is a model's opinion about a sentence, not a hindsight test against outcomes.

**What it accepts.** Exactly one acceptance transition over truth-apt content is implemented and reachable: **PROPOSED-RTE-22, the human `gbrain takes resolve`** — evaluator: the operator; criterion: the operator's judgement expressed as `--quality`, with a consistency check that refuses contradictory input; intended use: enter the Brier/accuracy denominators; scope: that one take; operational authority: writes the canonical row and mirrors it to markdown. Every other declared acceptance is either `doctrine only` (RTE-10's `gbrain takes propose`, which does not exist) or implemented-but-unreachable (RTE-11's auto-apply, whose documented config key has no reader). **`think` answers, facts, gaps, atoms, concept pages, and contradiction findings have no acceptance route at all.**

**What it integrates after acceptance.** Only the human-accepted resolutions, via RTE-12 into the calibration profile and thence — **on the CLI only** — into `think`'s question framing. Everything else the system does with candidates is retention or pre-acceptance operational use: the proposal queue, the verdict cache, the contradiction block in the synthesize prompt, `--save`d syntheses, `_meta.brain_hot_memory` injection. **None of that is lifecycle integration**, and the useful thing to say about GBrain's design here is that its own doctrine mostly agrees: `propose_takes` deliberately refuses to write canonical takes, the probe deliberately refuses to mutate, guardrails deliberately refuse to enforce.

**Three authorities, kept separate.**

- *Behavioral* (BAP-01…BAP-12, per packet): the skillpack, SOUL/HEARTBEAT files, system prompts, `THINK_SYSTEM_PROMPT_BASE`, and `_meta.brain_hot_memory` are **advisory** — the model may deviate, and no route in the boundary detects deviation. Tool allowlists, MCP scope/`localOnly`, source isolation, and worker rate/quiet-hour leases are **binding enforcement**. BAP-09 is the interesting hybrid: `<take>`-as-DATA framing is advisory, while `INJECTION_PATTERNS` is partial code enforcement whose own docstring declines to claim bulletproofing.
- *Epistemic*: licensed content is narrow. RTE-13 licenses "a judge flagged this pair"; PROPOSED-RTE-25 licenses "this sampled corpus scored thus at this rubric epoch"; PROPOSED-RTE-22 licenses "the operator recorded this outcome." **No route in the boundary licenses reliance on a `think` answer, a fact, a gap statement, or a take.**
- *Operational*: MCP scope gating, `remote` fail-closed trust, `sourceScopeOpts` SQL predicates, the takes-holder allowlist, budget caps, the bundled-skill held-out refusal, and the two `takes.bootstrap_*` consent gates all permit or block behavior. **None of them confers epistemic warrant.** Surviving source isolation is not evidence of truth, and operational continuation of the dream cycle is not warrant for what it wrote.

**Direct behavior/policy adaptation without a truth-apt route** (set aside for the runtime lens, named in §3e): SkillOpt's optimize→gate→accept loop, skillpack install, schema-pack activation, job/subagent/cycle control, audit-to-doctor, and the guardrail seams. SkillOpt is worth the orchestrator's attention because it is the **only** place in the repository where a real evidence-consuming acceptance gate with a named margin criterion (`> best + 0.05`, median-of-3, held-out required for bundled in-place mutation) is wired end to end — but what it accepts is a prescriptive artifact, not a claim.

**Claims that remain unsupported here for want of evidence.** CLM-10, CLM-11, CLM-14, CLM-15's live application, and every behavioral claim about prompt compliance (CLM-03) remain `claimed` — implementation, run, or causal evidence is missing and is located outside the frozen boundary. No causal attribution of any kind is licensed by this run: nothing was executed, and no interventional comparison was inspected.

**Nine mismatch markers** (M-01 evidence retrieval absent; M-02 accept path absent; M-03 kind-enum coercion; M-04 consolidate not synthesized; M-05 verdicts unconsumed; M-06 `published` inert; M-07 `grade_completion` always 1.0; M-08 citations unverified; M-09 auto-resolve key unread; M-10 calibration MCP-unreachable) are recorded above with anchors. Three of them (M-01, M-02, M-04) are places where a **reference doc states as current behavior something the code does not do** — which matters here because `CLAUDE.md` designates `KEY_FILES.md` as the current-state reference an agent should trust.

**Scoping guard.** Every absence above is scoped to `rg` over `src/` excluding tests, plus the files listed in §7. `src/core/operations.ts` (4,751 lines) and `src/core/search/hybrid.ts` (1,870 lines) were not line-read, so none of these absences should be expanded into a claim that no informal or unobserved route exists.

---

## 7. Files read inside the frozen checkout (all reads reportable for central registration)

Full-file reads: `docs/takes-vs-facts.md`; `docs/contradictions.md`; `docs/eval-takes-quality.md`; `CLAUDE.md`; `src/core/think/prompt.ts`; `src/core/think/cite-render.ts`; `src/core/think/sanitize.ts`; `src/core/search/evidence.ts`; `src/core/cycle/propose-takes.ts`; `src/core/cycle/grade-takes.ts`; `src/core/cycle/calibration-profile.ts`; `src/core/cycle/phases/consolidate.ts`; `src/core/cycle/nightly-quality-probe.ts`; `src/core/guardrails.ts`; `src/core/takes-resolution.ts`; `src/core/facts/decay.ts`; `src/core/eval-contradictions/judge.ts`; `src/core/eval-contradictions/auto-supersession.ts`; `src/core/skillopt/validate-gate.ts`; `src/core/skillopt/bundled-skill-gate.ts`.

Partial reads: `src/core/cycle.ts` (57–175, 1860–1990); `src/core/think/index.ts` (185–220, 270–330, 380–600); `src/core/cycle/synthesize.ts` (1–70, 890–945); `src/core/cycle/synthesize-concepts.ts` (1–45); `src/core/cycle/extract-atoms.ts` (1–40); `src/core/extract-takes-from-pages.ts` (1–80); `src/core/skillopt/score.ts` (1–60); `src/core/cross-modal-eval/runner.ts` (1–50); `src/commands/calibration.ts` (40–80); `src/commands/takes.ts` (`cmdResolve` + dispatch 344–580); `src/core/operations.ts` (`think`, `get_calibration_profile`, `find_contradictions` definitions); `README.md` (1–60 + grep); `docs/GBRAIN_VERIFY.md` (headings only).

Grep-only (matched lines seen, files not read): `src/cli.ts`; `src/schema.sql`; `src/core/migrate.ts`; `src/core/pglite-schema.ts`; `src/core/schema-embedded.ts`; `src/core/config.ts`; `src/commands/doctor.ts`; `src/commands/serve-http.ts`; `src/core/calibration/gstack-coupling.ts`; `docs/architecture/KEY_FILES.md`; `docs/architecture/lens-packs.md`; `docs/architecture/calibration-quality-gate-spec.md`; `skills/conventions/calibration.md`; `CHANGELOG.md`; `test/propose-takes.test.ts` (filenames only, not content).

No file was modified; no git state was changed; no GBrain command was executed.
