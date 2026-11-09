---
type: agentic-system-analyses/types/agentic-system-verification.md
description: "Report verification of the instruction-only recall skill (recall/) of Parcha-ai/parcha-skills at c82883b15e5e8f02483bee513b3c8dcac48e3c9e"
run-id: AAS-2026-11-05-parcha-skills-d5ad184aa4af-01
reviewed-boundary: "c82883b15e5e8f02483bee513b3c8dcac48e3c9e"
---

# Recall (parcha-skills) report verification

## Verification

**Scope and basis.** This verification judges the corrected runtime, memory,
epistemic and workflow members and the new reconciliation afresh against the
boundary and SRC-1. The frozen checkout's `HEAD` was confirmed as
`c82883b15e5e8f02483bee513b3c8dcac48e3c9e`. The structural report check is
`none`, so no structural blocker is owed. No refusal was handed to this job;
the previous verification and the runtime, memory and epistemic answers were
read as arguments, not as established repairs. The workflow answers file is
empty, and no workflow blocker was raised before. Read in full at the frozen
commit: `recall/skills/recall/SKILL.md`,
`recall/skills/recall/references/central-brain.md`,
`recall/skills/recall/references/query-cookbook.md`, `recall/README.md`,
`recall/package.json`, `recall/.claude-plugin/plugin.json`,
`recall/.codex-plugin/plugin.json` and `.github/workflows/desloppify-ci.yml`.
Also read: the Recall test in `tests/test_portability.py`, the `test` script in
root `package.json`, `recap/skills/recap/scripts/recap.py` lines 90–180 and
255–325 plus a search of its consumer checks, the Recall lines of
`recap/skills/recap/SKILL.md` and `precap/skills/precap/SKILL.md`, and the
first exporter tests in `recap/tests/test_recap.py`.

**Boundary.** The target class `extension or tool mechanism`, the boundary
kind `complete artifact, partial loop` and the tier `doc-grounded` fit the
evidence. The package holds eight instruction and manifest files. The engine
and the Brain service are absent at every path. Nothing found contradicts the
frozen target or boundary kind.

**Previous blockers, rechecked against source.**

- *Index-maintenance status (runtime).* Corrected.
  [RT-RTE-index-maintenance](runtime.md#rt-rte-index-maintenance) now
  separates `trigger implementation conclusion status: wired` from
  `ingest implementation conclusion status: claimed`. Its effects, read-back,
  activation and evidence-limits fields agree with the split. The skill text
  contains only the `index`, `doctor` and detached `setsid nohup ... index`
  commands. The epistemic `doctrine only` rows on the same route are
  consistent with it.
- *"All host transcripts" (runtime).* Corrected. The effects field, the
  change-admission list and the cold-scan delegated-visibility field now
  state the declared scope. The frontmatter says "the current index covers
  Claude Code and Codex transcripts", and the pi and thinking-block gotchas
  are quoted where needed.
- *Pull-only read-back (memory).* Corrected. Core ideas, the Read-back
  opening and the conclusion-supported field of
  [MEM-ABS-push-hook](memory.md#mem-abs-push-hook) now cover only routes that
  read retained session material.
  [MEM-RTE-generated-skill-load](memory.md#mem-rte-generated-skill-load) now
  states that its direction is host-dependent and uninspected, and
  integration issue 9 says a system-wide pull-only value is unsupported. I
  rechecked the bounded absence: neither plugin manifest declares hooks, and
  the package ships no hooks file.
- *Search-result containment (epistemic).* Corrected.
  [EPI-OBJ-search-results](epistemic.md#epi-obj-search-results) now covers
  `search` rows only. The `related` row in the inventory has no object
  record, and the ledger row on
  [RT-RTE-related-sessions](runtime.md#rt-rte-related-sessions) names that
  route's own list. The source supports the split: `SKILL.md` describes
  `WHY` only for `search` output. It says `related` output is "ranked by
  overlap and recency", with no match explanation.
- *Pull-only convergence (reconciliation).* Corrected. The convergence
  bullet now has two scopes. The generated-skill scope matches
  [RT-RTE-skillify-admission](runtime.md#rt-rte-skillify-admission) and
  [RT-BAP-generated-skill](runtime.md#rt-bap-generated-skill), which name the
  host loader, not a model request.

**Previous limits.** Both are resolved in the records.
[RT-RTE-outcome-playbooks](runtime.md#rt-rte-outcome-playbooks) now reads
`git -C <cwd> branch --show-current` as reporting the current checkout of
`<cwd>`, as [EPI-RTE-resume-branch-check](epistemic.md#epi-rte-resume-branch-check)
does. The source command supports that reading. The CLI's role as a central
client is now recorded in
[RT-RTE-interface-selection](runtime.md#rt-rte-interface-selection),
[RT-RTE-remote-brain-read](runtime.md#rt-rte-remote-brain-read) and
[RT-OBJ-recall-receipt](runtime.md#rt-obj-recall-receipt), and in the
epistemic interface-selection row and memory issue 10. `central-brain.md`
supports the CLI as a remote client through `doctor` and
`show '<recall://receipt>'`. Two things stay unknown: what CLI `search`
returns under a central signal, and what `shadow` means. Each record states
these unknowns beside the claim, so they are faithfully scoped uncertainty,
not a limit.

**Other consequential claims checked against source.**

- Runtime G1 alternate paths hold. `recall_candidates` in `recap.py` takes
  `--recall-script`, `RECALL_SCRIPT` and three fixed home paths, and reads no
  central-mode signal. `session_target` refuses `recall://` only where
  `allow_remote_receipt` is false, which is the relation-graph path.
- G6 and the export row hold. `recall_session_pages` rejects non-zero exits,
  invalid JSON, an unsupported `schema_version`, a changed boundary receipt,
  discontinuous sequences, an incomplete page without a cursor, and more
  than 1,000,000 pages. The epistemic `source_complete` gap holds: when no
  page carries `source_snapshot_stable`, `source_stable` is `None` and passes
  `is not False`. The re-sanitize digest check (`text_sha256`) is described
  correctly. Each of these findings is attributed to `recap`.
- The package change gate holds. Root `npm test` runs
  `python3 -m unittest discover -s tests -v`, `desloppify-ci.yml` runs
  `npm test`, and its path filters omit `recall/**`.
- The Codex `"capabilities": ["Read"]` label, the two default prompts and
  the absence of `allowed-tools` all hold.
- The empty-result conflict (G5,
  [EPI-CLM-confident-no-answer](epistemic.md#epi-clm-confident-no-answer)) is
  the source's own. The workflow scoping holds: the cookbook sentence sits
  under its `--paths` Scripting example.
- The remote citation rule, the capture exclusions, private-by-default
  capture and exact-receipt forget all match `central-brain.md`.
- Status convention: `wired` for the agent-side procedure stays accepted
  where the model issues engine or service tools and the evidence-limits
  field marks the engine parts as declared. That covers local search,
  related, remote read and capture. The split statuses on export and index
  maintenance, `afforded` on generated-skill read-back, `claimed` on
  [MEM-RTE-brain-ingest](memory.md#mem-rte-brain-ingest) and
  [EPI-RTE-engine-evidence-gate](epistemic.md#epi-rte-engine-evidence-gate),
  and the epistemic architectural statuses all fit their evidence.

**Evidenced absences.** Each has a searched boundary and a prevented
conclusion. Rechecked against the files:
[RT-ABS-engine-code](runtime.md#rt-abs-engine-code),
[RT-ABS-tool-restriction](runtime.md#rt-abs-tool-restriction),
[MEM-ABS-push-hook](memory.md#mem-abs-push-hook),
[MEM-ABS-skill-provenance](memory.md#mem-abs-skill-provenance),
[EPI-ABS-acceptance-record](epistemic.md#epi-abs-acceptance-record),
[EPI-ABS-generated-skill-test](epistemic.md#epi-abs-generated-skill-test),
[EPI-ABS-self-report-distinction](epistemic.md#epi-abs-self-report-distinction),
[EPI-ABS-data-instruction-rule](epistemic.md#epi-abs-data-instruction-rule),
[WF-ABS-independent-answer-check](workflow.md#wf-abs-independent-answer-check)
and [WF-ABS-agent-delegation](workflow.md#wf-abs-agent-delegation). The
self-report query did not cover "tool output" or "tool input/output". Both
phrases occur only in matching and ingest descriptions, so the conclusion
stands.

**`Part of:` relations.** All are sound:
[MEM-OBJ-export-cursor](memory.md#mem-obj-export-cursor) and
[MEM-OBJ-brain-synced-content](memory.md#mem-obj-brain-synced-content), the
latter a cross-kind relation the member explains;
[EPI-OBJ-search-results](epistemic.md#epi-obj-search-results), now narrowed;
[EPI-OBJ-resume-summary](epistemic.md#epi-obj-resume-summary); and every
`EPI-RTE-*` and `WF-RTE-*` route part. The parent records still cover their
parts, including [RT-RTE-brain-capture](runtime.md#rt-rte-brain-capture),
which covers forget.

**Supersessions.** All four are accepted.
[MEM-OBJ-search-hit](memory.md#mem-obj-search-hit) superseded by
[EPI-OBJ-search-results](epistemic.md#epi-obj-search-results) is a duplicate
by granularity only: the two have the same producer, check, consumer,
substrate and `--paths` limit. The memory record's lineage remark stays a
memory finding. The two workflow route supersessions and the claim
supersession share container, steps, owner and quoted passage. The ruled-out
identities and the "no unresolved conflict" finding are correct. I found no
disagreement between reports that the source leaves open.

**Integration issues.** Reconciliation disposed of all ten memory issues.
Issues 6 and 7 (index lifetime after source deletion, reach of
`recall_forget`) and the CLI-central unknown in issue 10 are faithfully
scoped unknowns stated beside their claims.

**Omission questions investigated.**

- *Other shipped paths that reach Recall state.* A repository-wide search for
  `recall` outside the package found the registrations, the `.github` policy
  lines, root `README.md`, the portability test and script, `precap`
  (`SKILL.md` and `references/investigation.md`, which repeat the search
  instruction), `recap`, and `parable`, where the word is ordinary
  ("high-recall"). None adds a producer or consumer of Recall state.
- *Execution evidence in recap's tests.* `recap/tests/test_recap.py` skips
  the exporter tests unless `RECALL_TEST_SCRIPT` names the separately
  installed private engine. The repository therefore holds no Recall run or
  test double, and "no observed run" stands.
- *Working-context control claims.* Checked against the `SKILL.md`
  instructions on reading references. This found one overstatement, recorded
  as a limit.

The search stopped there. The engine and Brain are absent, so more reading of
the package cannot settle the remaining engine-side unknowns. The excluded
skills' internals bear on no Recall responsibility.

## Blockers

none

## Limits

- In memory's Read-back section, the working-context bullet on conditional
  reference loading says the skill tells the model to read
  `recall/skills/recall/references/central-brain.md` "only when MCP tools or
  central signals exist". It also says this keeps static skill material out
  of the window. The source makes the read mandatory ("immediately read")
  under MCP tools or central signals. It does not forbid reading the file
  otherwise. The Upgrade section points to the same file for "Setup, mode
  routing, and all Brain commands", and the References list links it without
  conditions (SRC-1, `recall/skills/recall/SKILL.md`). The mechanism is
  mandatory conditional loading plus unconditional links. Readers should not
  conclude that local-mode invocations reliably keep `central-brain.md` out
  of context. Whether it enters depends on the host's progressive disclosure
  and on the model. This dimension has no controlled value, and the other
  working-context mechanisms are unaffected. Concerns
  [RT-CMP-recall-skill](runtime.md#rt-cmp-recall-skill).
