# Batch 23 OpenRSI exact-publication audit

**Disposition: hold.** The publication still omits the shipped default sandbox's candidate access to nominally private answers. Generic deployment and scoring caveats do not disclose this concrete evaluation boundary. No actual leakage is established.

## Identity and byte binding

- run-id: `AAS-2026-10-19-openrsi-4f870183cadd-01`
- method-commit: `3e2491c83a4613d410511af8c3cfde30f4b67689`
- source-revision: `71ae803a035d5e3b78c19fa49ed9f67d0550cbaa`
- Source identity: `https://github.com/FrontisAI/OpenRSI`.
- Auditor: independent Pi session `01a15556-9230-7492-9fad-ce74f4f8cce8`; environment reports `openai/gpt-6.1-sol`, reasoning `medium`. No delegation.

Paths below use E = `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs`:

| Locator | Exact path or suffix |
| --- | --- |
| W, prepared checkout | `E/commonplace-worktrees/batch-23-openrsi` |
| Preparation | `E/commonplace-worktrees/batch-23-openrsi.preparation.json` |
| Prepared command prefix | `W/.venv/bin` |
| R, run | `W/kb/agentic-system-analyses/state/AAS-2026-10-19-openrsi-4f870183cadd-01` |
| S, frozen source | `W/related-systems/FrontisAI--OpenRSI` |
| P, publication | `W/kb/agentic-system-analyses/retained/frontisai--openrsi` |
| Publish effect | `R/effects/publish.json` |
| External log | `E/batch-23/openrsi.output` |

Fresh SHA-256 checks match every `cases.openrsi` pin in [the intake](../batch-23-audit-intake.json): 897 source files, 13 publication files and 157 run files. Source membership also equals the tracked source tree; recursive publication enumeration has exactly the 13 pinned members. Publication bytes equal the completed publish effect's `new` map; effect identifies this run/source/destination, expected incumbent `absent`, old map null. Preparation is `ready` and agrees on W, method and command prefix. W HEAD equals the method; S HEAD equals the source revision. Source Git status is empty; W has only its untracked publication in the inspected status output, not a clean origin/integration approval.

| Identity | Fresh SHA-256, matching intake |
| --- | --- |
| Preparation | `76be9b48c63a08e6df1629b9dfb52eb3d9fb9de06bc7ce02a9a34d62f760232c` |
| Publish effect | `a9639d17fc052072210d7b894f3fcb92e5af21e8a99a4d9cb8198001097a9dcf` |
| External log | `be67d500c668f311b98775011514b34125300356049f246b9521f81d9af585b2` |
| Published manifest | `e3b9f71467cd8afa66fe1e1e1f3495a6994e6b38b1a6ecba930141ddc5cc9416` |
| Publication map digest | `1ec7e92a83d8665409437995b05319b8daf10baf0a9f7549e661ec4351236291` |

Map digest recipe: SHA-256 of `json.dumps(map, sort_keys=True).encode()`. The intake retains every individual member hash. All 33 stored attempts are completed; completion is not semantic or worker-compliance certification.

## Consequential finding

Historical audits supplied a question, not its answer. Independently inspected frozen SRC-1 evidence establishes:

- `S/OpenMLE-Gym/openmle-sandbox/README.md:80–109` places submitted candidate execution and private-answer scoring on the same worker. `DATA_DIR` names public data; it is not an access restriction. The source explicitly states:
  > The private directory is an evaluation convention in this source snapshot, not a security boundary: the default worker mount exposes the shared filesystem read-only except for selected writable paths.
- `S/OpenMLE-Gym/openmle-sandbox/node_workers/sandbox_builder/start_sandboxes.sh:150–154,177–181` mounts the shared root read-only in both GPU and CPU workers, with selected writable overlays. Read-only prevents modification, not reading the private answer file.

P/`runtime.md:24,39–43,151–181` describes the private scoring command, mount flags and configurable score policies, but never explains candidate answer visibility. A scoped search across every published Markdown member for private/secrecy/leakage/read-only/convention terms found no equivalent disclosure. P/`synthesis.md`'s “Propose, execute, repair and deliver a program” section and final scoring/execution limitation retain analyzer fallback, printed-score trust, test-score substitution and deployment uncertainty, not this default shared-mount condition. P/`overview.md` links members and expressly limits deterministic checks; it supplies no missing qualification.

This changes how a reader interprets execution-grounded fitness and nominally private evaluation. It is not merely an uninspected optional implementation. The default boundary is directly documented and supported by the launcher within the unchanged frozen source. The synthesis type requires preserving conditions that change what evidence establishes. A caveat appearing only in this audit cannot repair the public account.

**Unblock:** under separately authorized recovery, publish source-grounded runtime/evaluation qualifications and dependent public synthesis explicitly stating candidate access through the default shared mount. Preserve possible access versus observed leakage, and this route versus other deployments. Independently reverify and audit the new exact bytes. No target execution or expanded acquisition is necessary to state this static limit.

## Historical coverage and public qualifications

Read both intake-listed historical audits completely, and the [archived review](../../../agentic-systems/reviews-archive/openrsi.md) linked by `systems.md`. All concern the same source revision. Their default-answer-access concern is freshly confirmed above; old holds remain evidence rather than being cleared by fresh publication. No predecessor or old trace was treated as source truth.

The new public synthesis retains the important architectural coverage: separately invoked Gym/Evo/ERL, retained journal/cards/board/summary consumers, training-input paths, conditional scoring, restart limitations and absent observed benefit/lineage. It visibly carries partial inventory and storage-classification limits. The archived review's stronger theory-builder/reflection readings and detailed benchmark numbers are not acceptance requirements; their omission alone establishes no defect. This audit does not adjudicate every historical SFT conversion claim or independently reconstruct the full memory profile. The decisive evaluation omission is sufficient to hold without a second analysis.

## Bounded operational evidence

Inspected settled `message_end` worker results, not repeated streaming snapshots. Log line 1293 is the successful runtime worker result, outer call `call_SDT1gypiMKUdmLdBPHqO9rCS|fc_0433ba31b4390db0016ad627745f1487d28716a23f4367b77f`, exit 0. Within that same worker's zero-based messages 77/80, call/result `call_N2PgZJ13rdPZt7CxE7DlT9K5|fc_0bdcc216ad4de922016ad6281954b887d298f25c19ccf20a6f` successfully reads launcher lines 122–191, including both mounts. Source inspection actually occurred; recognizing its consequence is not proved by reading it.

The same worker's messages 98/99 pair a successful report write, followed by successful edits at 102/103 and 104/105. These are executed handout writes, not proposed actions or evidence of target execution. `R/state/attempts/000005-runtime.json` and the current member bind the accepted runtime. Log line 2968 records the successful report-verification worker; its messages 116/117 pair the actual verification write. `R/state/attempts/000022-report-verification.json` pins the current runtime and produces current verification hash `0de9b2a60c1936b02fb4037085dd473206c12b7e8c526995263afdcb9a3cfef2`. P/`report-verification.md` accepts the conditional-oracle account and declares no blockers without disposing of private-answer visibility. Thus publication and independent verification did not catch this omission.

Read applicable workshop/collection, text, runtime, synthesis and verification contracts and frozen worker rules. This sample establishes actual source reads and output writes, not exhaustive instruction reading, authority compliance, writer idleness or a complete no-target-execution history. No additional operational hold is established within this sample; no historical incident is cleared.

## Validation and coverage limits

Bounded audit stopped at the confirmed consequential omission. No acquisition, target execution, run/effect command, state/source/analysis edit, integration, cleanup, termination, commit, push or feedback to analysts occurred. Only this report was authored. Unpublished timeout cases and other independently owned reports were excluded. No causal improvement, actual leakage, deployed enforcement or exhaustive worker compliance is certified.

From W with its prepared `W/.venv/bin` first on PATH, read-only `commonplace-validate` checks returned:

```text
Target: kb/agentic-system-analyses/retained/frontisai--openrsi
VALIDATION SUCCESS
Files analysed: 1
Text files: 0
Diagnostics: 0 failures across 0 subjects; 0 warnings across 0 subjects

Target: /home/zby/llm/commonplace/kb/work/agentic-system-reruns/audits/batch-23-openrsi.md
VALIDATION SUCCESS
Files analysed: 1
Text files: 1
Diagnostics: 0 failures across 0 subjects; 0 warnings across 0 subjects
```

These deterministic passes do not clear the semantic hold.
