# Lens applicability records — RUN-GBRAIN-20260820

Logical record 6 of the result. Both optional lenses carry an **explicit** disposition record.
No disposition here is implied by an absent section elsewhere.

## Disposition 1 — memory/context lens

```yaml
lens: memory/context
disposition: applicable
inspected_boundary: >
  GBrain repository at 9a0bae8, functional boundary declared in the evidence packet §3.
  Excludes the host agent platform's own conversation memory.
trigger_evidence:
  - SRC-10 src/core/facts/meta-hook.ts:39-108 — facts accumulated from conversation turns are
    injected into the `_meta.brain_hot_memory` field of every successful MCP tool response
    (excluding recall/extract_facts/forget_fact), top-K by decayed confidence, 30s session cache.
  - SRC-11 src/core/facts/decay.ts:26-58 — per-kind halflife table and effectiveConfidence();
    retained material changes value with elapsed time, i.e. it is maintained, not merely stored.
  - SRC-13 docs/takes-vs-facts.md:55-66 — one-way `hot facts → [dream consolidate] → cold takes`
    bridge, with consolidated_at / consolidated_into marking.
  - SRC-07 src/core/cycle.ts:101-175 — dream-cycle phases that write durable material back into
    the brain (synthesize, patterns, consolidate, extract_atoms, synthesize_concepts, enrich_thin).
  - SRC-08 src/core/think/prompt.ts:88-96,172-193 — the calibration profile, itself derived from
    graded past claims, is delivered back into a later `think` invocation's context.
  - SRC-04 src/core/minions/handlers/subagent.ts:283-320 — subagent_messages / subagent_tool_executions
    are reloaded to reconstruct a later invocation of the same job after a crash.
  - SRC-14 src/core/skillopt/apply-edits.ts — instruction artifacts (SKILL.md bodies) are mutated
    by an optimizer using measured scores from prior runs.
rationale: >
  Multiple distinct implemented paths carry material accumulated or changed through use back into a
  later invocation or action. The trigger is met several times over, on both push and pull
  directions, so no judgement call was needed.
action: run the embedded memory/context lens in a fresh worker context consuming only the evidence packet.
prevented_conclusions: none — the lens ran.
```

## Disposition 2 — epistemic lens

```yaml
lens: epistemic
disposition: applicable
inspected_boundary: >
  GBrain repository at 9a0bae8, functional boundary declared in the evidence packet §3.
trigger_evidence:
  - SRC-13 docs/takes-vs-facts.md:1-23 — the repository names `takes` "the epistemological layer",
    storing WHO believes WHAT with a confidence weight and time, typed take/fact/bet/hunch.
    These rows are truth-apt objects by construction.
  - SRC-08 src/core/think/prompt.ts:48-70 — hard rules requiring a citation on every substantive
    claim, explicit marking of weight<0.5 and kind=hunch, a Conflicts section when two takes
    contradict, and a Gaps section naming what the brain does not know. These are checking and
    scope-limiting instructions applied to truth-apt content.
  - SRC-07 src/core/cycle.ts:63-72 — `grade_takes` retrieves evidence and asks a judge model to
    verdict unresolved takes (auto-resolve OFF by default); `calibration_profile` aggregates the
    resolved subset into pattern statements, bias tags, and a Brier score.
  - README.md:9-12,167 — a consequential knowledge-production claim: "Search finds the pages. The
    brain reads them for you and writes the answer", with gap analysis named as the differentiator.
  - README.md:265 — `eval suspected-contradictions` runs a query-conditioned LLM judge over
    retrieval pairs to surface conflicts between takes and facts; wired into the daily dream cycle.
rationale: >
  Material routes handle truth-apt content (attributed weighted claims, judged verdicts, cited
  syntheses, contradiction findings) and the system makes an explicit consequential
  knowledge-production claim. Successful knowledge production is not a prerequisite for running
  the lens, and the finding is not prejudged.
direct_adaptation_exception_applied_to: >
  Routes set aside as direct behavior/policy adaptation with no truth-apt object and no
  knowledge or warrant claim, and therefore left in the runtime account: rate-lease cap adaptation
  (`lease-cap-controller.ts`), backoff/jitter scheduling, quiet-hours deferral, RSS watchdog drain,
  search-mode knob resolution, and query-cache reuse. Where a set-aside route feeds an epistemic
  route (e.g. cache reuse changing what evidence a `think` call sees), the epistemic lens was asked
  to include it in its invoked method rather than re-adjudicate applicability.
action: >
  Invoke kb/instructions/analyse-external-system-epistemic-architecture.md in a fresh worker
  context, bounded by this run's boundary, revision, and source register; wrapper rules enforced
  (no reacquisition, no boundary widening, no parallel ID namespace, no independent publication,
  no system-wide epistemic grade).
prevented_conclusions: none — the lens ran.
```

## Worker topology used

Fresh sub-worker contexts were available and were used for both lenses (step 3, "Worker topology").
Each consumed only the prepared evidence packet plus targeted reads inside the frozen read-only
checkout. Neither worker was permitted to reacquire sources, change the revision, or decide
publication. The sequential fallback was not needed.
