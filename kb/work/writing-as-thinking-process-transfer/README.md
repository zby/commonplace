# Writing-as-thinking → process transfer

## Goal

Harvest the still-unincorporated ideas from the four writing/thinking essays ingested 2026-08-10 and turn each into a Commonplace **process** change (review gate, FIX routing, connect/multistage step, writing convention) — or an explicit rejection with a recorded reason. The prior written-artifacts-in-learning-loops workshop (closed 2026-08-10) promoted two conjectures and closed, but its own ingests flagged ~20 extractable items and most were left as "scaffolding already covered." This workshop works that backlog.

## Why a workshop, and the one hard rule

The prior workshop was killed because it **accreted wrong ideas** faster than it tested them. So the governing discipline here is **discriminating-test-before-build**: no idea gets promoted to a durable artifact until a cheap one-note (or one-pair) test shows it has signal over what Commonplace already ships. An idea that fails its discriminator is *rejected in this README*, not built. Distilling the counterexamples that kill an idea is fine to do inline; do not reopen the closed workshop to mine them.

## What closes this workshop

Every candidate below reaches a terminal state: **promoted** (named library artifact) or **rejected** (one-line reason recorded here). When no candidate remains open, extract the survivors and delete this directory per `kb/work/COLLECTION.md`.

## Evaluation boundary

- These are **human** first-person essays. Transfer to an agent/KB process is a hypothesis, not an inheritance — `human analogies can motivate functions without determining component boundaries`. State each transfer as the behaviour/dependency a process must preserve, then test it.
- Changed human understanding, a retained artifact, and changed agent behaviour are different outcomes; do not call written output "learning" without the retention/activation/effect links.
- A candidate that only restates an existing gate or note is redundant, not novel — check the shipped gate catalogue (`kb/instructions/review-gates/`, `composition-friction-gate.md`, `critique-note.md`) before claiming novelty.

## Candidate backlog

Status ∈ {open, testing, promoted, rejected}. Method and first target are deliberately left to the live session.

| # | Idea (essay source) | Residual increment over what ships / what to discriminate | Status |
|---|---|---|---|
| 1 | **Premise-decomposition review** (how-to-think #2) | `composition-friction-gate` already decomposes into inferential *joints (edges)* and attacks each. Increment: decompose into *premises (nodes)* and test each for external support / counterexample. Discriminator: on one note, does the premise-node check surface a real weakness the joint check misses? | **promoted** → `kb/instructions/premise-decomposition-gate.md` (discriminator + generalization test passed 2026-08-10, see Test log). Registration into the review pipeline deferred. |
| 2 | **Counterexample-scope routing** (how-to-think #1) | Classify a defeated point *local* (defeats a premise → revise, keep the commitment) vs *global* (propagates to the commitment → retire). **Reconsidered 2026-08-10:** this is a review-layer property, not a `discovery-lifecycle` phase. Local/global is Lakatos argument-internal (premise-vs-conclusion within an explanation), while `discovery-lifecycle` tracks a conjecture's evidential *status* through phases and deliberately abstracts its internal premises away; its test phase checks *consequences* (forward), not *premises* (backward). The earlier "add a test-result branch to `discovery-lifecycle`" framing (and the ingest's recommended action) was over-scoped. | **mostly delivered** — `premise-decomposition-gate` emits LOCAL/GLOBAL per premise; the full pass consumes GLOBAL→Disposition. Remaining: optional fix-routing-by-scope in `FIX-SYSTEM`. A `discovery-lifecycle` one-line cross-ref (its revise-vs-reject step *may cite* a scope verdict) is likely not worth it. |
| 3 | **Value-of-information reading** (learning-by-writing #3) | Route the next read by *expected claim-change*, not retrieval relevance, in `connect` / `write-multistage`. Operationalizes the open question in the claim-routed conjecture. | open |
| 5 | **Stance-reversal operator** (learning-by-writing #4) | Routine "write the strongest note that contradicts this one" as an anchoring check in connect/review. Cheap; de-risks the claim-routed conjecture's own anchoring failure mode. | open |
| 6 | **False-precision anti-gate / "accurately-vague" register** (wordless #2) | A check for stating-as-settled what the evidence leaves open — the counter-pressure to constraining. `AGENTS.md` forbids invented precision but no gate enforces it. | open |

(#4, a killed-conjecture ledger, is deprioritized per maintainer: distilling counterexamples is useful but the closed workshop is not to be reopened.)

## Open discriminating tests carried in from the two promoted conjectures

- [descriptive-link-labels may supply claim self-sufficiency](../../notes/descriptive-link-labels-may-supply-claim-self-sufficiency.md) — a **label-ablation test (2026-08-10)** was run: 6/6 cold-reader PASS, gate never fired even de-labeled; it reassigned the mechanism from the label convention to the body-premise convention and left the **thin pre-connect-draft** case open. That thin-draft test is the cheapest remaining experiment.
- [claim-routed reading may beat reading-first for synthesis notes](../../notes/claim-routed-reading-may-beat-reading-first-for-synthesis-notes.md) — its head-to-head test (build one synthesis note both ways, compare warranted update vs context cost) is **deferred** by maintainer to control scope.

## Sources

- [How to think in writing](../../sources/how-to-think-in-writing.ingest.md) — Karlsson/Lakatos: conjecture, premises, local/global counterexamples (#1, #2)
- [Learning by writing](../../sources/learning-by-writing.ingest.md) — Karnofsky: hypothesis as inquiry-control state (#3, #5)
- [Putting ideas into words](../../sources/putting-ideas-into-words.ingest.md) — Graham: exact-word commitment + neutral-stranger reread
- [When is it better to think without words](../../sources/when-is-it-better-to-think-without-words.ingest.md) — Karlsson: expansion/compression phasing, false precision (#6)

## Test log

### 2026-08-10 — #1 premise-decomposition discriminator (premise-node vs joint-edge)

**Setup.** Two title-as-claim notes resting on empirical premises — `llm-generation-confidence-tracks-typicality-not-soundness.md` (A) and `weakly-discriminated-qualities-tend-to-be-underselected.md` (B). Each read by two fresh, cold (no linked notes), no-tools adversarial sub-agents: a **JOINT** reader running the shipped `composition-friction-gate` (test each inference/edge; default UNSUPPORTED) and a **PREMISE** reader (assume inferences valid; decompose the claim into premise-nodes; hunt a counterexample per premise; route failures LOCAL/GLOBAL). Question: does PREMISE surface a real weakness JOINT misses?

**Result — yes, on both notes, and the two are complementary.**
- **A:** PREMISE-only found (i) an RLVR/post-training counterexample to the premise "training optimizes text likelihood" — a premise stated as background, which an edge-check has no joint to attack — and (ii) a token-logprob vs verbalized-confidence conflation. JOINT-only found the automation-boundary corollary as an inference overreach.
- **B:** heavy convergence (both caught "no-lift underselection" over-stated as "directional drift," and the Bug-That-Shipped activation-vs-selection confound). PREMISE still added: whether decorrelated maintainability signals *exist* to assemble (JOINT endorsed that reasoning as holding), and whether the weak quality has a stance-independent ordering at all ("underselection" as possible category error).
- **#2 evidence:** PREMISE's LOCAL/GLOBAL routing converted findings into "scope the claim" vs "the headline must weaken" — actionable in a way JOINT's thin-joint ranking is not.

**Verdict.** Premise-node decomposition reaches a distinct, actionable defect class (false/doubtful *background* premises; scope-repairs) the joint-edge check cannot structurally reach; the two are complementary, not redundant. Build #1 as a **sibling** to `composition-friction-gate` with #2's LOCAL/GLOBAL routing built in — do **not** replace the joint check.

**Caveats.** Two notes, both theoretical/empirical-premise register (where node/edge divergence is most expected); single reader per cell, no replication. Medium confidence: justifies building, not a universal-lift claim. Untested on definitional and procedural notes.

### 2026-08-10 — #1 build + generalization test

**Built** `kb/instructions/premise-decomposition-gate.md` (experimental, run-by-hand sibling to `composition-friction-gate.md`; register-aware Step 1/2 for claim / definition / procedure; LOCAL/GLOBAL routing per premise; writes a report, mutates nothing; not wired into the review system).

**Generalization test.** Ran the gate (fresh cold readers) against a **definition** (`directed-reading.md`) and a **procedure** (`critique-note.md`) to check the defect class holds beyond title-as-claim/empirical notes.
- **Definition:** produced boundary-commitment premises and mis-sorting counterexamples — three LOCAL condition-repairs (mid-pass scoping vs "bounded before the pass"; short sources vs the behavioural check; FAQ/API-reference sources vs the "native structure" contrast) and a GLOBAL "this may mark a *phase* of task-lensed synthesis, not a *kind*" defeater reached by a sharper route than the note's own "may be redundant" hedge.
- **Procedure:** produced assumption-premises and misfire counterexamples — LOCAL repairs (register inference, link-scoped engagement judgement, output-destination guard) and three GLOBAL defeaters, incl. **P4**: `critique-note` mandates "the strongest case" with an ERROR path covering only *inability*, not *correctness*, so it has no sanctioned way to report "the note is sound," driving fabricated opposition on correct notes.

**Verdict.** Gate generalizes to definition and procedure registers, producing register-appropriate, actionable LOCAL/GLOBAL findings. Confidence: medium → good (three registers). #1 **promoted**.

**Byproduct (spun off, not acted on):** the P4 finding is a real gap in `critique-note.md` — no sanctioned "no strong critique exists / note is sound" outcome. Candidate fix for a separate session; do not scope-creep here.

**Next.** (1) ~~Decide whether to wire the gate into the review pipeline~~ **Resolved (maintainer):** the gate does NOT belong in the wired review pipeline — that pipeline is for verdict-producing, easy-to-auto-fix findings. Hard, human-routed, no-verdict methods (`composition-friction-gate`, `critique-note`, compression bundle) are set aside from it and orchestrated by `kb/instructions/run-full-improvement-pass-on-note.md`. Integrate `premise-decomposition-gate` there as the node-check companion to `composition-friction-gate` (edges), carried unresolved in "Routed attention", with a GLOBAL-defeated load-bearing premise feeding the note-level Disposition. Integration pending. (2) #2 is mostly delivered at the review layer — the gate emits LOCAL/GLOBAL and the full pass consumes GLOBAL→Disposition. Reconsidered: local/global is a review-layer property, **not** a `discovery-lifecycle` phase, so do not graft a test-result branch there; the only remaining option is optional fix-routing-by-scope in FIX-SYSTEM. (3) Optionally write the theory note behind premise-vs-joint decomposition and link the gate to it via `rests-on`.

## Bookkeeping

- Move each candidate to `testing` when its discriminator runs; record the verdict and the promoted/rejected outcome in this table's row before closing it.
- Run cold-reader / adversarial tests in fresh sub-agents (no sympathy for the framing), mirroring the label-ablation setup.
- Validate any promoted artifact with `commonplace-validate` before it leaves the workshop.
