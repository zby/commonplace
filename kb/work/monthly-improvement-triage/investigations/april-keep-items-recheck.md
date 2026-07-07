# Investigation: re-checking the two carried-forward April KEEP items

## Scope

Two low-priority `KEEP` items from `kb/work/log-triage-2026-04-27.md`, carried forward unchanged through `kb/work/monthly-improvement-triage/README.md`'s "Carried forward from log-triage-2026-04-27" section, confirmed again in this July triage pass. Task: check whether anything has changed enough since April to move either past `KEEP`.

---

## Item A: control-plane abstractions across repository/prompt/learning-architecture levels

### Claim under test

`kb/log.md` line 9:

> `[agents-md-should-be-organized-as-a-control-plane, context-engineering, why-ai-systems-dont-learn-and-what-to-do-about-it source]` share unnamed structure: control-plane abstractions recur at repository, prompt, and learning-architecture levels, but the transfer conditions between those levels are not yet named

April's verdict (from the now-deleted-per-README but still-present `kb/work/log-triage-2026-04-27.md`, line 14): "`KEEP` - control-plane abstractions across repository, prompt, and learning-architecture levels. Current KB has control-plane notes and transfer-condition notes, but not this cross-level transfer mechanism. Keep until it predicts concrete transfer failures."

### What I read

- `kb/notes/agents-md-should-be-organized-as-a-control-plane.md` (full) — the repository-level instance: AGENTS.md as a control plane, placed by loading frequency × failure cost, with layers (invariants/routing/escalation) and an explicit "Lifecycle of guidance" section (methodology note → AGENTS.md pointer → maintenance staging area → instructions/skills → codified scripts/hooks). This is itself a lifecycle claim, but scoped to one level (repo guidance maturation), not a cross-level transfer rule.
- `kb/notes/definitions/context-engineering.md` (full) — the prompt/architecture-level instance: routing/loading/scoping/maintenance as the operational core of a single bounded call, with an "Architectural scope beyond a single call" section. It cites the control-plane note as its routing example but does not state conditions under which a control-plane pattern moves between levels.
- `kb/sources/why-ai-systems-dont-learn-and-what-to-do-about-it.md` and `.ingest.md` (full) — the learning-architecture-level instance: System M as a meta-control plane routing between System A (observation) and System B (action). The ingest's own critique (lines 56, 60) already flags System M as under-specified — "naming a control plane is much easier than building the oracle that tells it what to do" — and notes the paper draws its system boundary too tightly (model-only), missing that prompts/tools/schemas/routing artifacts already form a learning substrate outside the model. This is exactly the repo/prompt-level material the log entry wants transfer conditions *to*, but the ingest stops at "the KB's substrate notes already cover this," not at a transfer rule.
- `kb/notes/soft-bound-traditions-as-sources-for-context-engineering-strategies.md` (full) — closest existing material on "transfer conditions" as a named concept, but for a different axis (twelve external soft-bound traditions transferring *into* agent context engineering, not control-plane abstractions transferring *between* repo/prompt/learning-architecture levels). Its own "Open questions" section asks, unresolved: "Can transfer conditions be formalized? Something like: 'a strategy transfers if it doesn't depend on feedback from the processor, targets task completion rather than durable learning, and addresses dilution/complexity rather than forgetting.'" This is the same unresolved-transfer-conditions shape as Item A, on a different axis — evidence the KB still lacks a general transfer-condition mechanism, not evidence this specific gap has closed.

### Search for anything new since April

- `git log --since=2026-04-01` on the three anchor artifacts (`agents-md-should-be-organized-as-a-control-plane.md`, `definitions/context-engineering.md`, `why-ai-systems-dont-learn-and-what-to-do-about-it.md`/`.ingest.md`) shows only prose-tightening and reorganization commits (definition-boundary alignment on 2026-05-17, a `covered_by` tag split on 2026-06-10) — diffed both; neither touches transfer conditions or adds cross-level claims.
- `grep -rn "transfer condition"` across `kb/` finds: the log line itself, the now-superseded April triage file, the soft-bound-traditions note (transfer *into* agent context, different axis), and one MOC note (`an-enforced-tag-readme-is-a-moc-with-a-machine-checked-contract.md`) that cites soft-bound-traditions as "a concrete case of transferring a Zettelkasten idea... with the transfer condition made explicit" — again the traditions axis, not the control-plane-levels axis.
- `kb/log.md` has no newer entry mentioning control planes, System M, or cross-level transfer since line 9 was written; `git log -p` on `kb/log.md` since 2026-04-27 shows no such addition.
- No note anywhere states a concrete prediction of the form "a control-plane abstraction transfers from level X to level Y when [condition]" or documents an observed transfer failure.

### Verdict: KEEP

Nothing material changed since April. The three anchor artifacts have been lightly edited for prose/boundary clarity but not extended with cross-level transfer claims. The one adjacent "transfer conditions" note in the KB (soft-bound-traditions) sharpens the general shape of the missing mechanism but explicitly leaves its own transfer-condition question open, on a different axis — if anything this reinforces that the KB still lacks a general account of when abstractions transfer across levels, rather than resolving the specific repo/prompt/learning-architecture case. April's watch condition ("watch for concrete transfer-failure predictions") has not fired: no note or log entry names a concrete prediction or an observed failure. Continue to watch.

---

## Item B: codification lifecycle (when/what/how to commit) as a unifying note

### Claim under test

From the carried-forward README section: "partially distributed across `progressive-constraining-commits-only-after-patterns-stabilize.md` (when) and `codify-versus-llm-decision-heuristics.md` (what), but nothing unifies them as a staged lifecycle. Low-priority `KEEP`; April's assessment ('reads like a phase grouping more than a mechanism') still holds."

### What I read

- `kb/notes/progressive-constraining-commits-only-after-patterns-stabilize.md` (full) — the "when" note: one-shot vs. progressive constraining; codify only after a pattern proves stable across many runs; version both spec and artifact.
- `kb/notes/codify-versus-llm-decision-heuristics.md` (full) — the "what" note: four lenses (spec completeness, oracle strength, interpretation space, pattern stability) for the code-vs-LLM boundary, a quick-reference checklist, an explicit "reverse a codification (relax)" section listing relaxing signals, a "hybrid case" section, and a "three common mistakes" section whose third mistake is explicitly about lifecycle: "Static allocation. Treating the code/LLM split as a one-time design decision rather than a continuous cycle of codification and relaxing as understanding evolves" — linking directly to the cycle note below.
- `kb/notes/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md` (full) — a third, pre-existing note (last touched 2026-04-13, well before the April 27 triage) that already states the codify↔relax cycle explicitly: codification is a bet, working heuristics for making the bet ("codify for current leverage, not permanence," "prefer specs that describe what over how"), and relaxing signals for when the bet fails, with the trajectory framed as repeating at different levels of the stack (edge detection codified → relaxed → potentially re-codified as an accelerator).
- `kb/notes/spec-mining-as-codification.md` and `kb/notes/definitions/codification.md` (full) — the "how" piece: spec mining is the operational mechanism (observe a working system, identify regularities, extract deterministic checks), already cross-linked from both the progressive-constraining note and codify-versus-llm-decision-heuristics's lens 4.

### Recent commits check

`git log --since=2026-04-01 -- kb/notes/progressive-constraining-commits-only-after-patterns-stabilize.md kb/notes/codify-versus-llm-decision-heuristics.md` returns nothing — no commits since April touch either note. `codify-versus-llm-decision-heuristics.md` was created 2026-04-04 (before the April 27 triage), and `codification-and-relaxing-navigate-the-bitter-lesson-boundary.md` and `spec-mining-as-codification.md` both predate it by weeks. Nothing new has been added to the KB on this topic since April; the April triage already had all four notes available when it made its "phase grouping" call.

### Reach test (`kb/notes/COLLECTION.md`)

Would a unifying "codification lifecycle" note predict anything the existing notes don't?

- **Change one premise, predict the conclusion change?** A staged lifecycle would read: (1) observe underspecified behavior, (2) detect pattern stability [progressive-constraining], (3) decide code vs. LLM via the four lenses [codify-versus-llm-decision-heuristics], (4) extract via spec mining [spec-mining-as-codification], (5) commit as a bet, watch for relaxing signals, and re-relax if the bet fails [codification-and-relaxing]. Every stage already has a home, and the notes already cross-link into this sequence (codify-versus-llm-decision-heuristics's "reverse a codification" section already points at relaxing signals; its mistake #3 already names the continuous-cycle framing and links to the cycle note). A "lifecycle" note would restate this sequence in one place without adding a claim that changes if a premise changes — it's a re-index, not a new mechanism.
- **Would it apply in a different domain?** The individual pieces already generalize (pattern-stability criterion, oracle-strength gradient, bet/relax cycle, spec mining as extraction method). Grouping them under "lifecycle" doesn't add cross-domain reach beyond what each piece already has on its own.
- **Could someone say exactly how it's wrong, not just incomplete?** No — a lifecycle note assembled purely by sequencing four already-existing, already-cross-linked notes has no independent claim to be wrong about. This is the same relabeling failure mode this triage round already caught in six other candidates (see the README's dismissed-items list): a synthesis that looks insightful under the log's compressed framing but is superficial once the actual sources are read in full.

### Verdict: DISMISS

April's "reads like a phase grouping more than a mechanism" assessment was correct, and closer reading this pass shows the gap is smaller than the carried-forward framing suggested: the KB does not have just two notes covering "when" and "what" with a missing unifying layer — it has (at least) four notes already covering when, what, how, and the bidirectional cycle (codify → relax → re-codify), already cross-linked to each other (codify-versus-llm-decision-heuristics's own text names the "continuous cycle" and links straight to the cycle note). A unifying note would relabel this existing, already-navigable structure as "phases" without adding a claim that predicts anything the individual notes don't. Per `kb/notes/COLLECTION.md`'s body-composability guidance, the KB already prefers small composable notes connected by links over a duplicative synthesis note, which is what already exists here. No reopening condition beyond the general one: revisit only if a genuinely new stage (not covered by observe→stabilize→decide→extract→bet→relax) surfaces that the existing four notes cannot accommodate by extension.

---

## Summary

| Item | Verdict | Note written |
|---|---|---|
| A: control-plane cross-level transfer conditions | **KEEP** | — |
| B: codification lifecycle unifying note | **DISMISS** | — |

No note written for either item. Item A remains a genuine open gap with an unmet watch condition. Item B's gap does not survive a full re-read of the four already-existing, already-linked notes that cover it — the "unifying note" would be pure relabeling with no new predictive content.
