---
description: "Pinned ARC execution code separates pre-spend admission, post-spend prediction grading, and suffix truncation for the behavioral-authority decomposition case."
source: https://github.com/pbshgthm/arc-skill/blob/dba53c3799eab600a512dd73ed037d7ab6958c66/skills/arc-skill/scripts/arc_skill/live.py
captured: "2026-08-31"
capture: trafilatura
capture_scope: full-source
genre: code-repository
snapshot_sha256: b9fa5bed86925f39fb7741ac7b053b591f5efbd72ad31c43762c8d786fea4323
ingested: "2026-08-31"
occasion: "Provide durable source grounding for the bounded ARC worked case in the behavioral-authority decomposition proposal."
type: kb/sources/types/ingest-report.md
domains: [behavioral-authority, action-execution, runtime-controls]
---

# Ingest: ARC live-action execution at dba53c3

## Classification

The [pinned `live.py` file](https://github.com/pbshgthm/arc-skill/blob/dba53c3799eab600a512dd73ed037d7ab6958c66/skills/arc-skill/scripts/arc_skill/live.py) is implementation evidence from a code repository: its functions define how one revision admits and executes paid actions, batches, solve plans, and resets.
Author: `pbshgthm`, identified by the repository and snapshot author metadata; the file is direct first-party implementation evidence, not an independent assessment.

## Summary

The file places several mechanical checks at different stages of paid ARC action execution. It rejects a stale event guard, malformed or reset-containing batch, unavailable public action, or solve plan whose event, observation, or rules identity has changed before the affected action is spent; it then grades predictions against each executed result and stops a batch or plan on divergence, level change, game over, or victory. The useful distinction is temporal and operational: prediction presence and plan freshness can block entrance, while a wrong prediction is discovered after the current action and can discard only the unexecuted suffix rather than undoing the spend.

## Quotes

- **Source extract (verbatim):** def parse_step(raw: str) -> tuple[str, str]: action, separator, predict = raw.partition("::") if not separator or not action.strip() or not predict.strip(): raise ArcSkillError( 'each step needs its own prediction: --step "ACTION1 :: <claims>"' ) return action.strip().upper(), predict.strip()
  - **Source location:** `live.py`, `parse_step`, pinned revision `dba53c3`
- **Source extract (verbatim):** current = { "event": int(latest["id"]), "observation_hash": observation_hash(frame_at(latest)), "rules_hash": rules_hash(paths), } source = plan.get("source") if not isinstance(source, dict): raise ArcSkillError("plan has no source provenance; rerun `arc rules solve`") stale = [name for name, expected in current.items() if source.get(name) != expected] if stale: raise ArcSkillError( f"plan is stale ({', '.join(stale)} changed); rerun `arc rules solve`" )
  - **Source location:** `live.py`, `execute_solve_plan`, provenance and freshness guard, pinned revision `dba53c3`
- **Source extract (verbatim):** remaining = len(parsed) - index - 1 discarded = f"; {remaining} remaining steps were discarded" if remaining else ""
  - **Source location:** `live.py`, `execute_steps`, remaining-suffix calculation, pinned revision `dba53c3`
- **Source extract (verbatim):** if not ok: outcome = "SURPRISE" detail = f"step {index + 1} missed: {failed[0][2:]}{discarded}" break
  - **Source location:** `live.py`, `execute_steps`, prediction-miss branch, pinned revision `dba53c3`
- **Source extract (verbatim):** parsed: list[tuple[str, str, list[dict[str, Any]]]] = [] for raw in raw_steps: token, predict = parse_step(raw) parsed.append((token, predict, parse_claims(predict))) _validate_batch_tokens([token for token, _, _ in parsed]) events = _head_events(paths, at_event) start_event = int(events[-1]["id"]) records: list[dict[str, Any]] = [] outcome = "PREDICTED" detail = f"all {len(parsed)} steps landed as predicted" last_warning: str | None = None for index, (token, predict, claims) in enumerate(parsed): pending, before, warning = _paid_step(paths, token, {"predict": predict}) last_warning = warning or last_warning graded = grade_claims(claims, before, pending) ok = all(item["ok"] for item in graded) pending["predict"] = predict pending["predict_ok"] = ok pending["grade"] = graded event = _record(paths, pending) failed = [line for line in grade_lines(graded) if line.startswith("✗")]
  - **Source location:** `live.py`, `execute_steps`, batch parsing through the first paid-action grade, pinned revision `dba53c3`

## Connections Found

This file is a bounded implementation anchor for [behavioral authority](../notes/definitions/behavioral-authority.md): one execution surface gives applicability, path position, and consequence separate work to do. Per-step prediction syntax applies before batch execution, solve-plan freshness applies at plan entrance, and prediction grading acts after each paid step with surprise and suffix-truncation consequences rather than rollback. The case therefore reinforces the [six-path applicability audit](../notes/evidence/six-commonplace-paths-establish-broad-addressability-not-completeness.md) and supplies the [behavioral-authority decomposition proposal](../reference/proposals/revise-behavioral-authority-decomposition.md) with a worked external case, without selecting an ontology or establishing that the proposed dimensions are complete.

## Extractable Value

1. **Applicability can be stated as a target operation plus activation condition.** The event guard applies when a caller names an expected head event, batch prediction syntax applies to every submitted step, and source-identity checks apply only when committing a solve plan. This gives the decomposition proposal a compact case where a shared runtime and execution channel do not identify the operative path by themselves. [quick-win]
2. **A paid-action path has consequentially different stages.** Parsing and whole-batch token checks occur before the first spend; public-action admission occurs per step; prediction grading and queue control occur after the current action returns. This directly supports representing path position instead of treating execution as one undifferentiated channel. [quick-win]
3. **Mechanical force varies by consequence even within one file.** A failed entrance check prevents execution, a prediction miss classifies the executed step as surprise, and batch or plan control discards the remaining suffix without rolling back the completed action. This is a bounded test case for separating force from delivery mechanism. [quick-win]
4. **Fresh provenance is not epistemic warrant.** Matching a solve plan's event, observation hash, and rules hash establishes that its declared inputs are current; the subsequent step can still diverge and expose the rules as wrong. This concretely preserves the proposal's boundary between path admission, provenance, and substantive correctness. [just-a-reference]

## Limitations (our opinion)

The capture contains the complete pinned file, but not the imported broker, prediction, rules, or persistence implementations, their tests, CLI wiring, or runtime traces. Static reading can establish the control flow expressed here, not that every branch is reachable, that paid actions are journaled exactly as described, or that deployed ARC runs use this revision. It is also one point-in-time implementation owned by the project author, so later commits may change the behavior. Most importantly, one convenient implementation can illustrate distinctions but cannot establish the completeness or best names of the ontology left open by the [decomposition proposal](../reference/proposals/revise-behavioral-authority-decomposition.md).

## Recommended Next Action

Add a compact ARC worked-case table to `kb/reference/proposals/revise-behavioral-authority-decomposition.md` that records each check's target operation, activation condition, path position, and operational consequence, including the post-spend boundary of prediction mismatch.
