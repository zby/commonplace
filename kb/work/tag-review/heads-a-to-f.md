# Tag head review A (11 heads)

Method note: `git log -1` gives 2026-09-25 for almost every member (the ADR 089/090 tag sweep touched them all), so "most recent" is not a usable signal; I sampled across collections and prioritised members the head does not link. "L" = linked from head. Sizes are bytes of the head file.

## agent-memory

1. Opening: frames a stance, not a scope — "Agent memory notes treat memory as part of agent architecture, not just storage." Searchable words a reader would use (retention, persistence across sessions, recall, trace extraction, memory-system comparison) are thin in the opening; "requirements, activation, lifecycle" appear only in the description.
2. Defining note: `designing-agent-memory-systems.md` (synthesis) acts as the anchor and is first in "Core Frame" as "starting point", but is not named in the opening paragraph.
3. Boundary: nearest confusable is **context-engineering** (28 of 40 members shared). Related Tags gives a relation ("memory becomes useful only through selection and activation") but no boundary line saying what is memory and what is context engineering.
4. Fit: `rule-based-context-selection-needs-a-pre-existing-signal.md` → context-engineering; `kb/agentic-systems/reviews/beads-rust.md` (an active-work substrate — the head itself says active work state "is not retrospective memory") → tool-loop/context-engineering; the three `kb/agent-memory-systems/` members (`agentic-memory-systems-comparative-review.md`, `systems-table.md`, `review-framework-design.md`) fit but are unlinked, and they are exactly what someone searching "memory system comparison" wants.
5. Staleness: "Related systems" (`../agent-memory-systems/README.md`) sits under "Related Tags" but is not a tag head. No retired terms found.
6. Size/shape: 5.9 KB, 20/40 linked. Natural child: the 17 `agent-memory-requirements/*` notes (all dual-tagged context-engineering). `complete` would need ~20 more links → past 8 KB unless the requirements subdirectory became a child tag. Leave selective.
7. Verdict: **rewrite opening** — say what the tag gathers in retrieval words and add a boundary line against context-engineering; picks are good.

## architecture

1. Opening: "How Commonplace is structured and installed. Repo layout, the two-tree split between user content and framework, control-plane design, and the file-based storage decision." Scope says "Commonplace's own architecture", but half the members are general agent-runtime architecture (`agent-runtime-analysis-should-separate-scheduling-context-state.md`, `always-loaded-context-mechanisms-in-agent-harnesses.md`, `runtime-structure-determines-governance-control-surfaces.md`, `skill-discovery-re-fires-in-every-sub-agent-context.md`).
2. Defining note: none among members. The head's anchors (`reference/README.md`, `reference/architecture.md`, `storage-architecture.md`, `scenario-architecture.md`, ADR 006) all carry `tags: []` — the head is mostly a map of non-members.
3. Boundary: nearest confusable is **computational-model** (4 of the 6 unlinked notes are dual-tagged with it); not named. No Related Tags section at all.
4. Fit: `agent-runtime-analysis-should-separate-scheduling-context-state.md`, `always-loaded-context-mechanisms-in-agent-harnesses.md` → computational-model/context-engineering; `many-to-many-edge-state-is-where-files-yield-to-a-database.md` fits (storage), unlinked; `reference/proposals/checked-inline-blocks-for-shared-instruction-text.md` → context-engineering (already dual).
5. Staleness: **"the two-tree split" is superseded** — ADR 006 is `status: superseded` by ADR 014 (one-tree model), yet the head links it as "how Commonplace installs into projects". `scenario-architecture` is glossed as "the two-tree split, the escalation path to `commonplace/kb/`" — that file no longer mentions two-tree and now says explanatory material "is not an external escalation target". The "Notes" heading lists mostly reference docs.
6. Size/shape: 3.5 KB, 12 members, 6 linked; `complete` trivially achievable (add 6 links). The real question is the sense: Commonplace-system docs are already routed by `kb/reference/README.md`; the theory members overlap computational-model.
7. Verdict: **rewrite opening** (fix stale two-tree framing and decide whether the tag means Commonplace's layout or agent-runtime structure); if the latter, consider **merge** into computational-model.

## artifact-analysis

1. Opening: strong — "where behavior-shaping state persists, how it is encoded, where it came from, and with what force it acts", plus the four field names (substrate, form, lineage, authority).
2. Defining note: `axes-of-artifact-analysis.md` is first under "The scheme" but not named in the opening sentence; the nine definitions are linked. Adequate.
3. Boundary: nearest confusable is **agent-memory** (`memory-design-adds-operational-axes-to-artifact-analysis.md` shared) and **document-system** (`artifact-classification-…`, `answerability.md`, `artifacts-must-preserve-named-choice-scope.md` dual-tagged). Only the learning-theory parent is named; no boundary line.
4. Fit: `local-materialization-should-outperform-distant-declarations.md` (context presentation conjecture) → context-engineering; `orchestration-strategies-and-run-state-have-opposite-persistence.md` and `rlm-tendril-and-llm-do-place-symbolic-work-at-different-persistence.md` → tool-loop/computational-model (fit via persistence, but loosely); `ephemeral-computation-prevents-accumulation.md` fits.
5. Staleness: none found; "agent-memory-systems reviews apply this vocabulary" is a claim about non-members (reviews don't carry the tag) — fine as orientation.
6. Size/shape: **8,094 bytes — at the 8 KB warn line**; complete (30/30 linked). "Applications" is a 17-entry grab-bag; the next member forces a split or trimming. Natural child: persistence/ephemerality cluster (ephemeral computation, ephemerality-is-safe, opposite persistence, RLM/Tendril/llm-do).
7. Verdict: **keep** — the best head of the eleven; plan a split of "Applications" before it crosses the warn.

## computational-model

1. Opening: good for the PL half ("scoping, homoiconicity, partial evaluation, typing") and "scheduling architecture", but silent on the largest block of members: ~28 self-improving-systems/foundations notes (reflective systems, Gödel machines, software factories, search control).
2. Defining note: yes — `bounded-context-orchestration-model.md` named in bold at the top, with the select/call lemma. Good.
3. Boundary: only learning-theory named ("Unlike learning-theory…"). Nearest confusables are **self-improving-systems** (28 shared), **tool-loop** (19 shared, a child), and **context-engineering** (10 shared); none given a boundary line.
4. Fit (misfiled): `definitions/context-engineering.md` (tagged only computational-model!) → context-engineering; `definitions/self-improving-system.md`, `definitions/reflective-system.md`, `goedel-machines-are-a-proof-governed-case-of-self-modification.md`, `universal-software-factory-needs-a-declared-universality-axis.md` → self-improving-systems; also `vocabulary-collisions-prevented-at-write-time-not-read-time.md` → document-system.
5. Staleness: Related Tags "[tags](./README.md) — practical architecture applying these computational properties; frontloading and indirection cost are PL concepts applied to KB instructions" is a garbled remnant (the hub was substituted for a retired tag link in f54a2e90). "Agent Notes: 2026-03-10 … Multi-Agent Aggregation note … paper-outline workshop" is historical scratch.
6. Size/shape: **8,191 bytes — at the warn line**, 92 members, ~27 linked; `complete` not achievable. Natural split: tool-loop (exists), orchestration/scheduling (bounded-context model, select/call, decomposition heuristics, coordination guarantees, feasibility-is-heaviest-fork), instruction semantics (underspecification, scoping, one medium, indirection, frontloading). First remedy: drop the tag from the ~20 self-improvement/factory notes whose computational-model tag adds nothing.
7. Verdict: **split** — the tag has drifted into a second home for self-improving-systems and is at the size gate.

## constraining

1. Opening: good — "narrowing the space of valid interpretations an artifact admits — from partial narrowing (conventions) to full commitment (deterministic code)" matches the registered definition; "relaxing as its deliberate reverse" adds a search word.
2. Defining note: `definitions/constraining.md` is the first entry ("definition and spectrum"); not named in the opening paragraph but effectively at the top.
3. Boundary: no boundary line. Confusable: **computational-model** (underspecification/calling-convention notes dual-tagged) and **self-improving-systems** (9 shared: `a-methodology-governs-its-own-extension-…`, `moving-the-interpretation-enforcement-boundary-requires-coverage.md`, `llm-executed-methodologies-are-metacircular-interpreters.md`).
4. Fit: `prototype-standing-is-revision-cost-binding-plus-lost-investment.md` → learning-theory/self-improving-systems; `bitter-lesson-selects-against-unearned-reach-not-against-structure.md` → discovery (about reach); `opacity-is-a-scale-threshold.md` → artifact-analysis (representational form).
5. Staleness: Related Tags calls deploy-time-learning "the framework constraining serves; the verifiability gradient locates constrained artifacts" — deploy-time-learning's own head now says it is "the phenomenon", not a framework, and `verifiability-gradient.md` (a member) is not linked here.
6. Size/shape: 3.7 KB, 35 members, 17 linked. `complete` achievable by ~18 more links (~7 KB) — feasible under the warn. Unlinked load-bearing: `verifiability-gradient.md`, `enforcement-without-structured-recovery-is-incomplete.md`, `constraining-and-extraction-both-trade-generality-for-reliability.md`, `legal-drafting-solves-the-same-problem-as-context-engineering.md`.
7. Verdict: **keep** — solid opening; fix the stale Related Tags line and link the verifiability gradient.

## context-engineering

1. Opening: "the machinery for getting the right knowledge into a bounded context at the right time … routing, loading, scoping, scheduling, and maintenance" — matches AGENTS.md vocabulary; acceptable words.
2. Defining note: **missing** — `kb/notes/definitions/context-engineering.md` exists but is tagged only `computational-model`, so it is not a member and the head does not link it. The first "Core Claim" is the memory synthesis instead. `context-efficiency-is-the-central-design-concern-in-agent-systems.md` is also not tagged context-engineering.
3. Boundary: none. Nearest confusable is **agent-memory** (28 of 69 members shared) — and the agent-memory head is **not linked at all** from "Adjacent Indexes".
4. Fit: `warranted-reader-update-is-the-objective-of-substantive-writing.md` → discovery/document-system; `cheap-generation-breaks-text-volume-as-an-effort-signal.md` → llm-reliability; `brainstorming-how-to-test-whether-pairwise-comparison-can-harden.md` → evaluation; `naur-equates-machine-execution-with-formulated-criteria.md` → foundations/self-improving-systems; `history-has-one-chance-to-become-checkable.md` → artifact-analysis (lineage).
5. Staleness: "Learning theory — covers how context machinery contributes to deploy-time learning" predates deploy-time-learning being its own phenomenon tag. Description style "Index for context-engineering notes" is the old index framing.
6. Size/shape: 2.9 KB, 69 members, 8 member links — the thinnest head relative to size. Natural children from titles: agent-memory (already a tag; link it as child), methodology activation (`weight-resident-methodologies-…`, `borrowing-can-operate-through-…`, `capable-agents-need-methodology-selection.md`), documentation/summary retention (`design-rationale-must-preserve-…`, `an-insufficient-summary-precedes-the-source…`, `specific-intent-may-out-yield-…`, `evolving-understanding-needs-holistic-rewrite…`), write-context assembly (5 `reference/proposals/*`). `complete` not near.
7. Verdict: **rewrite opening** — tag the definition and name it at the top, link agent-memory as child/neighbour with a boundary line, then curate by the clusters above.

## deploy-time-learning

1. Opening: clear — "a software system meets its users and their needs only after it is deployed, the meeting is surprising, and … forces changes after the first release." Vocabulary risk: a reader searching "deploy-time learning" as *continuous learning outside weights* finds a phenomenon framing; "continuous learning", "adaptation" appear only in picks.
2. Defining note: none named; `changing-requirements-conflate-genuine-change-with-disambiguation.md` is called "the core case". Acceptable.
3. Boundary: **self-improving-systems** named explicitly ("the machinery for doing so lives under that tag, not here"). Good.
4. Fit: the head contradicts its own boundary — `constraining-during-deployment-is-continuous-learning.md`, `retained-artifacts-enable-persistent-deployment-time-adaptation.md`, `ad-hoc-prompts-extend-the-system-without-schema-changes.md` are adaptation machinery (→ self-improving-systems / constraining), listed under "Where the change lands".
5. Staleness: none found.
6. Size/shape: 4.3 KB, 12/12 linked, complete holds. Leave.
7. Verdict: **keep** — small, complete, boundary stated; either soften "machinery lives under that tag, not here" or move the three machinery notes.

## discovery

1. Opening: "positing a new general concept and simultaneously recognizing existing particulars as instances of it." Reader words (conjecture, hypothesis, generalization, insight, theory formation) are mostly absent from the opening; "conjecture" appears only in picks.
2. Defining note: `definitions/discovery-lifecycle.md` exists and is linked, but second in the list; the opening links explanatory-reach instead.
3. Boundary: names constraining and "source-derived reshaping". Nearer confusables are **evaluation** (warrant/verdict notes) and **self-improving-systems**; not named.
4. Fit: `warranted-reader-update-is-the-objective-of-substantive-writing.md` → document-system (writing objective); `revision-guided-by-rationale-needs-faithfulness-not-just-legibility.md` → evaluation/self-improving-systems; `theory-warrant-tracked-at-the-finest-granularity-evidence-licenses.md` and `derivation-and-inheritance-give-starting-warrant-earns-scope.md` → evaluation (warrant, not discovery); `candidacy-evidence-licenses-escalation-not-acceptance.md` fits the lifecycle's test phase.
5. Staleness: **the opening definition diverges from the registered term** — AGENTS.md defines the discovery lifecycle as "the ideal-type staged path by which an ampliative conjecture earns acceptance"; the head's "positing … and simultaneously recognizing" is the co-arising-insight sense the definition now calls "the degenerate case". "Discovery produces theories — the highest-explanatory-reach items accumulation can store" does not connect to *theory builder* / *tentative theory*. Section heading "Reach — what discovery produces" uses bare "reach" where the vocabulary says the compound is the technical term.
6. Size/shape: 5.9 KB, 18/18 linked, complete. The "Reach" section is really warrant/evaluation content; no split needed at this size.
7. Verdict: **rewrite opening** — lead with the registered discovery-lifecycle sense and its definition, keep the co-arising case as the degenerate one.

## document-system

1. Opening: "How documents are classified, structured, and quality-checked" — serviceable; description "Index of notes about document types, writing conventions, validation…" is old index framing. Members now also cover documentation retention/segmentation and claim-repair failures, which the opening does not mention.
2. Defining note: none; `definitions/knowledge-artifact.md` is linked in the opening but is an artifact-analysis member.
3. Boundary: type-system named as "sub-area" (no boundary line). Confusables: **artifact-analysis** (4 shared), **kb-maintenance**, **failure-modes** (3 shared).
4. Fit: `domain-pricing-routes-an-exception-to-idealization-assessment.md` is filed under "Testing" — it is claim-repair workflow → failure-modes/kb-maintenance; `generality-bought-…` and `narrowing-bought-…` → failure-modes (already dual); `vocabulary-collisions-prevented-at-write-time-not-read-time.md` (tagged computational-model only) belongs here; `definitions/coordination-value.md`, `current-task-fit-alone-does-not-warrant-costly-entrenchment.md` → foundations/kb-maintenance (structure-adoption economics).
5. Staleness: "Decisions" links **ADR 002 (superseded — WRITING.md was replaced by COLLECTION.md files)** as a live decision; `deterministic-validation-should-be-a-script` glossed as "half of /validate's checks … could run as a Python script instead" (now `commonplace-validate`); Related Tags "[tags](./README.md) — the document system is infrastructure for the KB; architecture decisions about storage substrate…" is a garbled remnant of a retired tag link.
6. Size/shape: 5.7 KB, 31 members, 12 linked. Natural children: claim-quality/repair (generality, narrowing, domain pricing, `repair-dispositions-for-defeated-claims`, simplification evidence), documentation retention/segmentation (design-rationale, specific-intent, opposed recompute, addressability grain, insufficient summary), structure adoption (directories, taxonomies, coordination value, entrenchment, cheap-adoption). `complete` would need ~19 links → ~9 KB; needs a child first.
7. Verdict: **rewrite opening** (fix three stale items and widen the stated sense); consider **split** of the claim-repair cluster.

## evaluation

1. Opening: "What works, what doesn't, what needs testing. Empirical observations about KB operations, prompt design, and techniques from other systems." No searchable words for what members are about: oracle, judge, benchmark, experiment, warrant, assay, verdict, evidence record.
2. Defining note: none named. Candidates among members: `warranted-autonomy-is-bounded-by-oracle-domain.md`, `evaluation-automation-is-phase-gated-by-comprehension.md`, `an-experiment-identifies-only-the-contrast-it-actually-runs.md`.
3. Boundary: none; no Related Tags. Confusables: **llm-reliability** (9 shared, oracle hardening), **self-improving-systems** (13 shared), **failure-modes**.
4. Fit: head link `agent-memory-systems/reviews/cludebot.md` is **not a member** (tagged `trace-learning`); `mixed-epistemic-status-must-be-preserved-below-the-document-level.md` → document-system; `a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md` → document-system/kb-maintenance; `knowledge-storage-does-not-imply-contextual-activation.md` → failure-modes (primary).
5. Staleness: "techniques from other systems" describes no current member; the "empirical observations" framing fits only the `kb/notes/evidence/*` records, while most members are evaluation theory (oracles, warrant vs fit, experiment design). The review system's own terms (assay, gate, verdict) are absent though `reference/full-improvement-pass-closure.md` is a member.
6. Size/shape: 1.6 KB, 35 members, 4 member links. Natural children: evidence records (`kb/notes/evidence/*`, ~7), oracles and judges (`warranted-autonomy…`, `weakly-discriminated-qualities…`, `reasoning-production-is-not-reasoning-evaluation.md`, `verifiable-subroles…`, pairwise-comparison brainstorm, maintainability-oracles brainstorm), theory warrant and fit (`a-claims-warrant-does-not-determine-its-fit…`, `system-use-*` x2, `disconnected-witnesses…`, `retained-theory-intervention…`). `complete` not near.
7. Verdict: **rewrite opening** — the head describes a different tag than its members; rewrite in full with oracle/warrant/experiment vocabulary and boundary lines.

## failure-modes

1. Opening: "recurring ways an agent-operated KB can fail despite having relevant artifacts on disk … not discovered, loaded, interpreted, or acted on." Narrower than membership: three of nine members are claim-repair escapes under review (`generality-bought-…`, `narrowing-bought-…`, `domain-pricing-…`), one is `generation-confidence-does-not-by-itself-certify-soundness.md`, one is authority leakage (`a-consumption-channel-delivers-force-without-the-history-that.md`).
2. Defining note: none; `knowledge-storage-does-not-imply-contextual-activation.md` is the anchor ("core distinction"), first in list.
3. Boundary: **llm-reliability** named with a difference ("deviation taxonomy and correction machinery"). Good.
4. Fit: `generation-confidence-does-not-by-itself-certify-soundness.md` → llm-reliability; `elicitation-requires-maintained-question-generation-systems.md` fits weakly (inquiry process decay); the claim-repair trio fits only if the opening is widened.
5. Staleness: description "Index for failure-modes notes about characteristic ways knowledge can exist without changing agent behavior" — old index framing, and too narrow. Separator is ` - ` rather than ` — ` (cosmetic).
6. Size/shape: 2.0 KB, 9 members, 5 linked. `complete` achievable by adding 4 links.
7. Verdict: **rewrite opening** — widen to "claims and knowledge that fail to do their job despite passing or existing", or move the claim-repair trio; then declare complete.

## Cross-cutting

- **Vocabulary misses mirror the operator's failures.** Heads open with stance or thesis sentences ("treat memory as part of agent architecture, not just storage"; "What works, what doesn't") instead of the nouns a searcher types. evaluation (oracle, judge, benchmark, warrant), agent-memory (retention, recall, comparison), discovery (conjecture, hypothesis, generalization) all miss their obvious search words.
- **Defining notes are mis-tagged, not just unnamed.** `definitions/context-engineering.md` is tagged only computational-model, so the context-engineering head cannot reach its own definition; `context-efficiency-is-the-central-design-concern…` likewise. Only computational-model names its defining note in the opening; constraining and discovery link theirs but not first-sentence.
- **Boundary lines are the rarest element.** Only deploy-time-learning and failure-modes state one. The heaviest overlaps have none: agent-memory/context-engineering (28 shared; context-engineering does not even link agent-memory), computational-model/self-improving-systems (28 shared), evaluation/llm-reliability/self-improving-systems.
- **computational-model and context-engineering absorb dual-tags.** Self-improvement and factory notes carry `foundations, computational-model, self-improving-systems` as a boilerplate triple; all 17 `agent-memory-requirements/*` carry context-engineering. This inflates the big tags and pushes their heads toward the size gate while adding little routing value.
- **Post-sweep remnants.** Two heads (computational-model, document-system) have "[tags](./README.md) — …" Related-Tags lines whose phrases describe a retired tag; architecture and document-system link superseded ADRs (006, 002) as current; constraining describes deploy-time-learning in its old "framework" sense; several descriptions keep the "Index for … notes" framing even where members span reference and agentic-systems.
- **Heads whose stated sense is narrower than membership:** failure-modes (activation only vs claim-repair escapes), evaluation (empirical observations vs evaluation theory), architecture (Commonplace layout vs agent-runtime structure), document-system (types and conventions vs documentation retention). The head was written for an earlier tag and members accreted.
- **Size gate:** artifact-analysis (8,094 B, complete) and computational-model (8,191 B) sit at the 8 KB warn; the complete-and-small heads (deploy-time-learning, discovery) are the healthiest. Easy `complete` wins: architecture (+6 links), failure-modes (+4), constraining (+~18, stays under 8 KB).
- **Recency signal unusable:** the 2026-09-25 tag sweep touched every member, so `git log -1` dates do not identify recent additions.
