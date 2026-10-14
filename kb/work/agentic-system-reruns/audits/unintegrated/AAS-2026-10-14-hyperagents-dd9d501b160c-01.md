# Hyperagents exact-run audit

**Disposition: integrate with recorded limits.** No consequential defect established
within this bounded audit. No integration blocker; integration remains a separate decision.

## Identity and scope

- Run: `AAS-2026-10-14-hyperagents-dd9d501b160c-01`.
- Auditor: `audit-hyperagents`; runtime `openai/gpt-6.1-sol`, medium assignment.
- Worktree (`W`): `/home/zby/llm/commonplace/.commonplace/worktrees/hyperagents-dd9d501b160c`.
- Method and worktree HEAD recorded by preparation/inventory:
  `c0282c8ccb49edfef4bb095b8598c4b7aeb229b6`; preparation is `ready`, token `dd9d501b160c`.
- Frozen source (`S`): `W/related-systems/facebookresearch--Hyperagents`, identity
  `https://github.com/facebookresearch/Hyperagents`, revision
  `59a68f672dfb92c74aeb7e61535d776fb36e172d`. Independently checked HEAD and clean status.
- Publication (`P`): `W/kb/agentic-system-analyses/retained/hyperagents`.
- Run state (`R`): `W/kb/agentic-system-analyses/state/` plus the exact run ID.
- Historical lead: `kb/agent-memory-systems/reviews/hyperagents.md`, same source revision;
  no moved-account substitution. No existing audit or main incumbent in the inventory;
  current `git ls-tree main kb/agentic-system-analyses/retained/hyperagents` is empty.

Method: compare historical mechanisms with public overview/synthesis, investigate
admission, archive visibility, selector and ensemble qualifications against frozen
code, then sample operational evidence. Not a second analysis or target execution.

## Findings

1. **Executable inheritance is retained, without upgrading it to demonstrated gain.**
   Historical patch-lineage retention survives in `P/synthesis.md`, “From a generation
   request to executable change.” `S/utils/gl_utils.py:438–467` filters domain paths
   and applies saved diffs with `patch -p1`; this is code-state delivery, not prompt
   recall. Overview description and synthesis explicitly withhold exercised improvement,
   successful runs and causal benefit. No coverage regression established here.
2. **Prior evidence availability is not claimed as actual model consumption.**
   `S/meta_agent.py:7–19` accepts `eval_path` but constructs only the repository-edit
   instruction. Synthesis explicitly states discovery/tool-read dependence and distinguishes
   normal pruning, unpruned parent-only copying and full-archive optional consumers.
   This preserves the historical prompt-wiring caveat at the public surface.
3. **The new account corrects the historical universal score-gate shorthand.**
   `S/generate_loop.py:706–712` permits `meta_patch_files is not None` instead of
   successful score loading, while CLI lines 1087–1093 default that argument to `[]`.
   `S/utils/gl_utils.py:534` also has first-archive-node fallback. Synthesis names these
   exceptions and separates archive membership, eligibility and improvement. The old
   “except seed patches” wording is not a reason to restore a stronger gate claim.
4. **Optional consumers remain distinct and appropriately qualified.**
   `S/select_next_parent.py` ends in random choice among scored valid candidates;
   `P/runtime.md:34` records that behavior rather than importing default host weighting.
   `S/ensemble.py:23–48` selects using the requested split and loads a saved prediction.
   Synthesis explicitly excludes fresh inference and unseen-split generalization.
   Its limitations also retain DGM retry, Polyglot delivery, provenance, grouped-profile
   and domain-coverage limits. This audit did not independently re-prove those defects.

## Publication and operational evidence

- Independently hashed all 13 publication files: exact file set and every SHA-256 match
  `R/effects/publish.json` and inventory. Effect is completed for this run/source.
- Assembled `ARTIFACT.yaml`: `c6d0d1e2328565277d91843426d5234648b1f63bbd972656f5194b2c4eec0abb`;
  working declaration: `093c6e4a6c7cab7e4e1a9db63f6d2d45eec6a24bf51f7b287dd1db929b388322`.
  `R/state/attempts/000033-publish.json` pins the assembled hash, not the declaration.
- Attempts 000005 and 000030 record completed Sol/medium jobs; these are acceptance
  records, not by themselves proof of performed obligations.
- Read-only streamed `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/hyperagents.output`.
  Line 971 contains the completed worker for exact handout `000005-runtime/prompt.md`
  at W. Within that worker, paired executed read/results for `generate_loop.py`
  offsets 1, 301, 601 and 901 (300-line requests), including call
  `call_T09M5m6IS4PHBgZv2zvxkXTS|fc_034d87b5259d6b8a016acf6a84a31887d29a700d77e2a7e6c0`.
  Results are not errors. This establishes sampled source inspection, not exhaustive
  worker compliance. No missing trace or known stop was supplied for this run.

## Validation and remaining limits

From W, using `W/.venv/bin/commonplace-validate` without output-file options:
- Publication directory: `VALIDATION SUCCESS`; 1 directory artifact; 0 failures,
  0 warnings. `--full` confirms all 12 Markdown members plus directory roles/relations,
  `Overall: PASS (clean)`.
- Owned origin report (absolute path): `VALIDATION SUCCESS`; 1 text file;
  0 failures, 0 warnings.

No source acquisition, target execution, delegation, state mutation or publication edit.
The evidence supports a useful implemented-pathway account, not reliable target operation
or measured improvement. No unblock condition is required for this disposition; stronger
claims require the matched execution/comparison evidence already requested publicly.
