# Explicit approval contract change

Historical implementation record. The later
[publication-boundary change](./publication-boundary-change.md) removes routine
plan approval while retaining explicit selection and final-publication approval.
The probes below describe the earlier contract, not current operation.

Implement the phase-5 correction without treating a retry as an operator
choice. No paid model calls, ingest implementation or data migration are
part of this change.

## Consumer packet

| Contract field | Disposition |
|---|---|
| Authoritative declaration | ADR 127 and `headless/operator.py`: only an explicitly captured answer authorizes continuation past an operator stop. |
| Scope and enforcement | Revision plans and strike lists use `answer()`; the function reads a stored answer, never the editable draft. Full-pass `--direction` is unchanged. |
| Consumer classes | Runtime reader/writer, revision workflow, review CLI, fake-harness fixtures, revision instruction, review guide, architecture, command reference and ADR updated. No result-file schema or validator change. |
| Byte-pinned consumers | The edited revision instruction is a captured assessment input. Its new bytes invalidate plan approval and call reuse. Existing review result hashes naturally become stale; no baselines are rewritten. Historical run captures stay unchanged. |
| Old spellings | Searched `operator\.answer|operator\.waiting`, `edited or not|unedited.*answer`, `repeats the command|repeat the command|repeating the same command`, and `artifact/plan\.yaml|--plan FILE` in `src`, `tests`, `kb/reference` and `kb/instructions`. Post-change line counts: 5, 1, 2 and 12 respectively; remaining hits describe the new interface or unrelated full-pass retry. |
| Generated and projected forms | No scaffold, template or skill-name change. Installed projects read the revised instruction in the library. The existing editable uv tool pointed to this checkout but had stale launchers; reinstallation exposed `commonplace-review` and removed retired launchers. |
| Fresh install | Scratch `commonplace-init` plus a named empty plan exercised the real CLI without model calls. An unapproved repeat remained stopped. |
| Existing installs and clones | Init preserves existing run files. An old draft with no proposal record cannot be approved. No compatibility or migration: existing drafts are not authority; the next workflow materializes a keyed proposal. Source clones use the same code. |
| Diagnostic promises | Old keys fail with `proposal changed`; unregistered files fail with `no operator proposal`; out-of-run paths are refused; concurrent approval raises the run-lock error. Covered by CLI or runtime tests. |
| Acceptance probe | `/tmp/commonplace-approval-probe-bbass0r8`: init fresh, seed Git, propose an empty named plan, repeat, init again with a legacy draft present, reject approval of that draft, approve the registered plan, edit its draft without reapproval, repeat successfully using the captured answer. Note unchanged; validation and init pointer checks pass. Initial attempt before the seed commit failed because the runtime requires Git HEAD; no worker launched. |
| Drift guard | Parameterized consumer tests change assessment instruction/profile and strike criterion/profile; they require new approval even when the generated proposal text is identical. Existing plan-edit tests require explicit reapproval and retain replay assertions. |
| Historical witnesses | The plan's phase-5 build history retains the original repeat-as-answer mechanism, explicitly distinguished from the correction. Old run captures and retained evidence are not rewritten. |
| Identity by convention | A stop names an artifact-relative file. Its operator record is keyed by that path; the proposal identity covers stop name, producing inputs and original proposal text. The approval command requires that identity. |
| Shared exclusions | Not applicable: no new artifact-membership predicate. Both runtime paths use the same proposal-path validation. |
| Relocation side effects | Not applicable: no artifacts moved. |

The revision instruction is consumed both by operators following its workflow
section and by the assessment worker as a captured criterion. Its composition
landing routes to that section without restating the approval mechanism.
No changes are needed to other pass instructions or the root control plane.

## Verification

- Focused runtime and revision tests: 29 passed, including unapproved repeats,
  captured answers, stale keys, lock refusal, path escape, changed proposal
  inputs, named plans, reapproval, publication conflicts and replacement
  proposals from retried calls under the same request key.
- Broader run: 915 passed in 788.52 seconds across general, headless,
  review, agentic analysis, relocation and docs, including slow tests
  (`-m ''`). The first attempt timed out at 200 seconds; the completed
  run replaced it.
- Core rerun after the additional regression cases: 319 passed in 51.20
  seconds across general, headless, review, relocation and docs (`-m ''`).
  The final focused rerun passed all 29 tests after the last local edits.
- Ruff passed. Five changed library documents passed deterministic validation.
- No live-worker evidence is claimed. Phase-5 paid trials and the first
  collection sweep remain for the operator.
