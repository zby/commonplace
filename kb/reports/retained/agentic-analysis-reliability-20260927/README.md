# Agentic-analysis reliability trial, 2026-09-27

This record supports scheduling of the agent-memory refresh and regression
checks of the analysis workflow. It tests repairs prompted by 19 pilot session
traces containing 719 tool outputs. Those traces showed recovered operational
failures; they did not establish an unresolved integrity failure in the three
then-current published pilot results.

The operator commissioned the repairs and authorized autonomous execution.
The implementation starts from commit `34dc62e3`; the changes and trial were
uncommitted when measured. Unrelated working-tree edits were excluded from the
repair scope. Historical analysis results were preserved byte for byte.

## Repairs and bounded acceptance

| Item | Change or disposition | Evidence and limit |
|---|---|---|
| R01: masked failures | Require separately inspected statuses or fail-fast chains, preserving stderr and wrapper metadata. | A negative subprocess test stops before a later success marker and leaves public outputs unchanged. The fresh run's failed source check returned nonzero and preceded its correction. |
| R02: source citations | Add `verify-sources` to the existing publication command, using the same frozen-source checks; separate adjacent attributed quote blocks. | Tests reject bad ranges, wrong pins, absent quotes and missing quote bodies. Fresh specialist passed 62 checks; the integrated result passed 104 after one range repair. Source occurrence remains distinct from semantic support. |
| R03: capacity and delivery | Reserve specialist capacity, preserve completed reports when notification fails, yield to a supervisor when needed, and prohibit competing writers or local substitution for specialist analysis. | Fresh coordinator and specialist completed. A specialist quotation correction returned a new checked hash. Launch and telemetry failures remained explicit. Five simulated recovery cases supplement observed behavior; they do not prove control over the runtime's thread limit. |
| R04: source-only status | Prohibit agent listings, including filtered listings, in fresh analysis workers; use completion events and the owned report path. Exposure requires abandonment and a new clean run. | The fresh trial used the permitted route. A fixture specifies the failed-run and clean-restart response to an unrelated completed report. No real analysis was deliberately contaminated. |
| R05: record grammar | Document canonical declarations, prose references and registered identifier kinds. Keep the parser strict. | Fresh report and result passed record validation on their first validation attempt. Grammar probes still reject duplicates, unresolved IDs, shorthand and unsupported record kinds. |
| R06: truncated reads | Cover aggregate wrapper limits as well as individual command limits; require bounded rereads of missing supporting spans. | A deliberate 9,045-token omission was recovered for a selected span. Fresh workers reread omitted material; selected synthesis examples require their full bundled results. This is not an exhaustive audit of every source byte. |
| R07: comparison prerequisites | Require linked ontology inputs before bundle capture; include source/record verification and publication code in the captured method. Keep invalid retained-result rejection. | A missing ontology target rejects preparation without output. The selected three-system trial checks matrix, table, statistics and 21 query records. Pond remains a named regeneration dependency of the full refresh. |
| R08: supporting assumptions | Correct the historical account of which check caught Mem0's ranges. Preserve frozen quote bytes and distinguish justified quote separators from accidental whitespace. | Full suite: 865 passed. After extending bundle method capture, 32 affected comparison/bundle tests passed. Changed Python passed Ruff. Markdown uses the applicable Commonplace validator. |

The early source command checks a running run's exact `result.md` or
`memory-report.md` without publishing or mutating it. A specialist need not
wait for the coordinator's assembled result. Publication still repeats its
checks and verifies integration identities. No legacy fallback, weaker source
check, or new classification format was introduced.

The generic skill-creator validator rejected Commonplace's existing extended
frontmatter keys. Both edited skill frontmatters remained unchanged, and their
Commonplace validation passed. This is a validator-contract mismatch, not a
reason to strip valid local metadata.

## Fresh analysis identity

The coordinator received only source identity, pin, permitted paths, method and
authority. Its independent memory specialist received the frozen input, not
prior analyses or audit findings. The producer instructions stayed fixed
through publication.

- System: Napkin, `https://github.com/Michaelliv/napkin` at
  `7582d6a46f5a11995956e60a59c41a5b242109f1`.
- Run: `AAS-2026-09-27-napkin-01`.
- [Retained result](../agentic-system-analysis-archive/AAS-2026-09-27-napkin-01/result.md),
  SHA-256 `8484f622335c134237968326c9971d8fbb1e71f97128e411f96b8d46ccba41db`.
- Frozen specialist input:
  `5923140a12ae31e626a794d14f365d49f07a8c8e7748394c702fdbb3d7495734`.
- Final specialist report:
  `593207c1ea92222094a13a53fe6ec704326cdd7ebeebec964c97a1a8b2178d23`.
- Main instruction:
  `75f4ac90c1de0283d36f1a36c26c3478e0f74f1b31d1c0af92d4006fc093fdf8`;
  memory instruction:
  `4c5ae2555eda3623f12c02d062dd37d1634ddc3b17d0cac48e14e0f58f580743`.
- Coordinator, specialist and recovery/synthesis worker model recorded in
  their traces: `gpt-6-astra`.

The public review was replaced through guarded publication. The completed-run
handoff was independently rerun successfully by the repair coordinator.
Local report/input hashes document the handoff; public findings are
self-contained in the retained exact result and do not require those ignored
files on a clean checkout.

## Recovery exercise interpretation

The [independent exercise](./recovery-probe.md) covers failed launch, failed
notification, substantive versus mechanical correction, prior-analysis
exposure, and truncated evidence. Every fixture has a safe next step.

Three wording ambiguities receive bounded no-change dispositions. A root
without a supervisor can retain an execution blocker and report it to the
operator; automatic runtime resumption is not promised. Report maintenance
remains subject to the explicit prohibition on unresolved competing writers.
Explicit uncertainty can preserve supported limits or disagreement, while
known unsupported findings require specialist reanalysis under the existing
reconciliation and semantic-verification rules. The exercise itself correctly
distinguished these cases. No generic scheduler or new ownership protocol was
added to address an external runtime limitation.

## Operational trace audit

The completed coordinator trace has 56 tool outputs; its specialist trace has
17. All 73 outputs match recorded calls. Neither used an agent listing.
The coordinator's nonzero availability probe merely found that the report had
not yet been written; it was not an analysis failure.

Actual recoveries were retained rather than counted as first-pass success:

- An integration script raised `ValueError: substring not found` before
  writing. Corrected section selection integrated the final report.
- Structural validation passed, then `verify-sources` rejected
  `bench/overview-exposure.ts:15-85`: the pinned blob ends at line 82.
  The coordinator reread lines 15–82, corrected the citation and passed 104
  checks. This directly exercises the distinction the repair introduces.
- One specialist quotation contained a fence. The specialist replaced it
  with a sufficient fence-free excerpt, preserved classifications, reran its
  checks and returned the final hash before integration.
- Three coordinator deliveries and two specialist deliveries were truncated.
  The coordinator reread the main instruction in bounded ranges and the needed
  ontology section. The specialist reread selected overview and documentation
  passages before completing its report. The audit checks those calls and the
  final disclosure; it does not establish exhaustive source-file coverage.
- A later request for exact specialist truncation telemetry failed with
  `agent thread limit reached`. It sought operational detail after the checked
  report was complete, not a required substantive correction. Publication did
  not depend on the failed message arriving.

Local trace provenance, under `/home/zby/.codex/sessions/2026/09/27/`:

- Coordinator: `rollout-2026-09-27T09-51-05-01a0e1d8-a182-7e80-8b8a-e9abd313d7e4.jsonl`.
  Outputs 18/25/164 show truncation; 269 shows the integration error and 276
  recovery; 319 shows range rejection, 323–331 reread/repair; 337 shows failed
  telemetry follow-up; 362–375 cover guarded prepare, publish and handoff.
- Specialist: `rollout-2026-09-27T09-52-41-01a0e1da-15f6-7e40-9d5c-c0fadc05a2d5.jsonl`.
  Outputs 20/43 show truncation; calls 80/92/110 reread relevant source spans;
  130–153 cover initial checks and 168–175 the final quotation correction.

These local paths are audit provenance, not clean-checkout dependencies. The
exact diagnostics, dispositions and acceptance outputs needed by the refresh
owner are summarized here. Full raw sessions are not retained as KB content.

The repair coordinator also recovered a test-fixture construction error and a
Ruff requirement before the passing suite. Its later multi-target
`commonplace-validate` invocation failed because the command accepts one target;
separate checked invocations passed. An arbitrary report-directory validation
also failed because it is not a collection root; all six retained Markdown
artifacts then passed explicit file checks. Its first query replay omitted the ledger's
required hash argument and failed; replay with both documented arguments matched
all 21 records. During retention, an initial extractor split a verification
block at backticks inside a Python string and failed with a syntax error. A
line-anchored closing-fence extraction recovered the full block, whose hash was
updated and whose replay passed. Some audit reads were oversized and were
replaced with bounded extracts. Two optional worker launches hit the thread
limit: the first was retried after specialist completion; the second reused
an instruction-only probe worker for synthesis, disclosing that context.
These are limitations of this execution, not erased failures.

A whitespace check on the frozen new result reports thirteen exact `> ` blank
quote separators. Inspection found no other trailing whitespace. Those bytes
are retained, and ordinary accidental whitespace remains rejected. All eleven
tracked 2026-09-26 retained results were rechecked byte-identical to HEAD.

## Comparison and closure

All eight repair items are accepted at the bounded scope above. The fresh
analysis, comparison writers, query replay and synthesis completed without an
unresolved failure affecting evidence or completion. The workshop is closed;
its durable changes are the source checker, parser fix, authoring and recovery
instructions, and this evidence record.

The [synthesis](./trial-synthesis.md), [executable query ledger](./trial-query-ledger.md)
and [execution record](./trial-acceptance.md) use exactly Dynamic Cheatsheet,
Mem0 and the new Napkin result. All three are code-grounded; their cutoffs are
2026-09-26 and 2026-09-27. No other row was silently dropped from that explicitly
selected population. Local semantic checking was performed by the synthesis
worker; there was no independent-agent semantic review.

- Exact evidence and captured method: `trial-bundle/` beside this record.
- Manifest SHA-256:
  `44f4ef62bda8116eeac568daae97207931a6cd4ad93f459151091a00903a76cd`.
- Matrix SHA-256:
  `fb2f5e4554e24e9514afe71ea6c75b7f6e7b12e0f0082de02d92a0d4f097ed06`.
- Exact matrix, table and statistics captures: `outputs/`.
- Query output: one population record, fourteen axis records and six named
  queries, all 21 reproduced exactly. A second implementation also checked
  all 42 result-axis records and the comparison outputs' identities.

The repair coordinator independently reran the ledger and then reran its full
cross-check using the retained paths. The relocated exact bundle verified with
its previously recorded hash and `--source-root .`. Its contents are sufficient
without the ignored cache or local run state. Retain this record and its bundle together for Git-backed reconstruction.
The bundle captures the actual input bytes measured before this repair commit;
commit `34dc62e3` alone is insufficient.

The recovery/synthesis worker trace,
`rollout-2026-09-27T10-03-14-01a0e1e3-c0a2-7c42-9483-e4c28ff9beb0.jsonl`
in the same session directory, contains 51 tool outputs with no unmatched calls
or returns. Its initial instruction batch was truncated (output 21) and reread
in bounded calls. Its synthesis metadata extractor assumed colon-style YAML,
failed on JSON-style YAML frontmatter (output 142), then used a YAML parser.
It wrote nothing on the failed attempt. No later operational failure was found.
Calls 228–306 cover the full 1,201-line Dynamic Cheatsheet, 1,003-line Mem0 and
1,176-line Napkin results in contiguous bounded ranges, without truncation.
Together, the three completed trial traces contain 124 matched tool outputs.
This count excludes the separately reported repair-coordinator execution.

The refresh inventory now names the new Napkin run. Three of 162 legacy
artifacts have current replacements; 159 remain pending. Pond still requires
source regeneration because its generated candidate lacks matching retained
evidence, and continues to block all-generated comparison. Broader document-only
and heterogeneous-source trials belong to the refresh owner. Old full-corpus
statistics and syntheses remain historical. Runtime thread limits remain
external, and these tests establish bounded recovery, not guaranteed unattended
completion under every capacity condition.
