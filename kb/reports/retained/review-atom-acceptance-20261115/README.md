---
description: "Dated acceptance evidence for review atom reconstruction, interrupted fixture recovery and zero-launch replay, with distinct environment and test-coverage limits"
type: types/note.md
---

# Review atom machinery acceptance — 2026-11-15

**The parent accepted a qualified machinery result:** one ordinary assessment
supplied a hash-bound fixture; its isolated trial recovered from budget-blocked
starts, completed, and then replayed without another model launch. The trial
published no live current result. Effective environments were **different**.
This is not judgment calibration. The parent accepted this evidence to close
the bounded review-unification workshop; [ADR 132](../../../reference/adr/132-review-atoms-retain-observations-behind-current-results.md)
retains the adopted decisions. Other review families, edits, stops and new
compositions were not admitted by this closure.

This dated record serves future review/fixture changes and acceptance regression
comparisons. The sibling [selected evidence](./evidence.json) retains IDs, hashes,
counts and check outcomes without requiring ignored run files. It is a summary,
not a runnable fixture or a full trace archive. Current behavior belongs to the
[review architecture](../../../reference/review-architecture.md) and
[review-result contract](../../../types/review-result.md), not this record.

## Baseline and prior context

The admitted subset was catalog gates, type conformance, collection conformance
and critique. An earlier captured-contract defect was repaired offline; a
repeated live check then accepted all four kinds on their first launch. That
established bounded machinery acceptance, not judgment quality.

The parent's commit record `889cce5df3038c96c9e2f5a6e357924ba3a4eed4` reports
**1,516 tests passed, one skipped**, including slow tests. Its later status-fix
commit `490f0194bebd10dc62f63e71a614aa65700e4489` reports **380 tests passed**
across general, review-workflow, relocation and documentation suites, including
slow tests. These are parent-reported prior runs, not independent reruns for
this report or exhaustive verification of every acceptance case. Closure also
added fake-harness regressions for mutation of live inputs between capture and
dispatch, and failure between retained-result creation and current publication.
The latter resumes with unchanged retained bytes and no new worker launch.
The parent independently reviewed those tests and ran the general,
review-workflow, relocation and documentation suites with slow tests included:
**382 passed** in 216.29 seconds. All 11 closure Markdown artifacts validated
without failures or warnings.

The fixture case used code and KB commit `490f0194bebd10dc62f63e71a614aa65700e4489`.
The preceding library-policy fix excluded ignored ambient files from ordinary
library inventories. Historical observations/fixtures lacking
`git-visible-or-installed-v1` were refused, not silently reinterpreted or
rewritten. A new source observation supplied the current-policy fixture.

## Case, interruption and replay

The target was `a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md`
in `kb/theory/`; the gate was `sentence/stock-phrases`. Ordinary run
`20261115T200346Z` supplied fixture
`3870487350f9a4b6d7cbc816-6851bc80e3f6`. Outer trial `20261115T200508Z` owned
its reconstructed tree and nested execution. Short observation IDs are
run-local; the JSON preserves the run associations.

There were **two actual top-level review-model launches and three guard-blocked
process starts**, not five model calls. All three blocked starts exited 78
before Claude execution, with empty stdout and no review output. The final
budget was two allowed launches out of two authorized.

The parent reported its own execution mistake: pretrial verification used the
development interpreter against a CLI-created fixture; after the package
mismatch, the shell continued before the second budget slot was released.
The blocked starts are independently evidenced; the precise shell sequence is
the parent's explanation, not a reconstructed shell transcript. Verification
with the CLI interpreter found the recorded package map equal. The parent
released the second authorized slot and **resumed the same trial**. The initial
failure and all three blocked attempts remained recorded.

The recovered trial accepted one new answer. A subsequent resume added
**zero launches**: all 33 launch files, the completed result and the budget
history were unchanged. Recovery and replay receipts agreed. The ordinary
result was PASS with no findings; the trial was PASS with two INFO findings.
Neither verdict agreement nor identical findings were acceptance requirements.

| Launch | Reported model | Reported USD |
|---|---|---:|
| Ordinary assessment | `claude-opus-5-5` | 0.2997354 |
| Recovered trial | `claude-opus-5-5` | 0.352242 |
| **Total** | | **0.6519774** |

These are terminal reported list-price usage costs, not an invoice or net
subscription charge. Blocked starts had no model-usage report; replay is not
counted again.

## Independently checked evidence

The completed audit passed **52 core checks and four additional checks** using
byte hashes, tar inspection without extraction, read-only Git comparison and
complete raw JSONL parsing. It verified selected inputs, completed/raw outputs,
6,887 library files, 112 executor files, five dirty overlays and reconstructed
content. The committed-tree archive matched the recorded Git commit exactly;
archive paths and 35 reconstructed symlinks passed safety checks. The fixture
remained sealed. No source answer or shared report-state payload was copied
into executable trial inputs.

The trial did not publish live results. All four live views matched the
post-source snapshot; only the ordinary assessment had replaced its selected
view. All 160 files in the two checked historical v2 runs and five unrelated
dirty files retained their baseline hashes. These are audit-time comparisons,
not a claim that the library remains unchanged after adding this report.
Two representative completed results independently passed deterministic
validation with zero failures or warnings.

## Scope

The source advertised **71 tools** and MCP connections; the trial advertised
**25 tools** and no MCP servers. Trial stderr said four workspace permission
allow entries were ignored because the isolated tree was untrusted. Both
successful traces had six Reads and one Write, no failed tool results, no
permission denials and no spawned subagents. Both SessionStart hooks succeeded.
Those successes do not erase the configuration difference or establish
containment. Requested allowlists are not tool-inventory isolation.

Dependency artifacts, user-level harness settings, automatically loaded context
and provider internals were not fully pinned. Recovered tool failures still
require trace inspection rather than reliance on ordinary terminal success.
One recovered trial plus replay does not establish independent repeated-trial
behavior, installed-library live acceptance, judgment stability, calibration,
throughput or OS-level isolation. This record does not independently reverify
all offline race, interruption, publication-crash or consumer-preservation cases.
