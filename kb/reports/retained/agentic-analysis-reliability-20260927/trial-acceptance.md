# Bounded synthesis trial acceptance

The synthesis trial was commissioned on 2026-09-27 to forward-test the revised landscape procedure against exactly Dynamic Cheatsheet, Mem0, and the newly completed Napkin run `AAS-2026-09-27-napkin-01`. It owns only the three `trial-*.md` workshop artifacts and the specifically commissioned cache outputs. It authorizes no public synthesis, additional reviews, source-checkout inspection, or commits.

## Context and boundary

The worker was reused after a new synthesis worker could not launch because of a reported thread limit. Before this commission its context contained only instruction-recovery fixtures, not external-system analyses or old findings. This prior context is disclosed rather than described as a fresh context. Semantic verification is local; no independent reviewing agent is commissioned. The worker did not inspect model metadata; the parent trace audit records `gpt-6-astra`.

The selected reviews are exactly `kb/agentic-systems/reviews/dynamic-cheatsheet.md`, `kb/agentic-systems/reviews/mem0.md`, and `kb/agentic-systems/reviews/napkin.md`. All other systems, legacy reviews, old matrices, prior syntheses, workshops and audits are excluded as evidence. Prior recovery-probe output is not evidence for this synthesis. The Napkin incumbent must remain unread until the target run publishes.

The method is `kb/instructions/synthesize-agent-memory-landscape/SKILL.md`. The workshop and reports collection contracts, main-result contract and comparison/bundle scripts were inspected before capture. The commissioned query source is `/tmp/reliability-trial-queries.py`; it supplies query logic only. Snapshot-specific code and exact outputs will be retained in the query ledger.

## Frozen evidence identity

The target Napkin run reached `complete` before its review was inspected. Metadata extraction confirmed `AAS-2026-09-27-napkin-01`. The bundle prepare command then succeeded with exactly the three commissioned `--review` arguments and the three explicit ontology inputs. The selected results' local ontology links were inspected before capture; Napkin linked the three selected definitions, and the other two results supplied no local ontology links.

Recorded outside the bundle **before interpretation**:

- Bundle: `kb/reports/cache/agentic-analysis-reliability/2026-09-27/trial-bundle`.
- Manifest SHA-256: `44f4ef62bda8116eeac568daae97207931a6cd4ad93f459151091a00903a76cd`.
- Matrix SHA-256: `fb2f5e4554e24e9514afe71ea6c75b7f6e7b12e0f0082de02d92a0d4f097ed06`.
- Selection: three distinct sources, all code-grounded; cutoffs `2026-09-26` and `2026-09-27`.
- Repository revision recorded by capture: `34dc62e3b936c97b9d7424a4b2e232dfd0b0272b`. This identifies the checkout, not a claim that every captured input was committed there.

The temporary cache bundle is the exact reconstructable evidence location for this workshop trial. Parent owns durable retention before any later public use.

## Operational failures and recoveries

- A metadata-only preliminary extractor assumed YAML-style `analysis-result:` syntax and failed with exit code 1 on Dynamic Cheatsheet's JSON-style YAML frontmatter. It wrote nothing. Recovery parsed the delimited frontmatter with YAML and extracted the selected result paths and local ontology link targets. This failure did not omit a selected system or supply any substantive finding.

## Acceptance

The bounded synthesis and query ledger are written. All three selected systems remain in the population; no missing input was repaired from an excluded source or dropped. Parent owns final reliability acceptance and evidence retention.

## Executed commands and identity checks

Bundle capture (exit 0):

```bash
uv run python scripts/bundle_agentic_landscape.py prepare --output kb/reports/cache/agentic-analysis-reliability/2026-09-27/trial-bundle --review kb/agentic-systems/reviews/dynamic-cheatsheet.md --review kb/agentic-systems/reviews/mem0.md --review kb/agentic-systems/reviews/napkin.md --ontology kb/notes/definitions/theory-builder.md --ontology kb/notes/definitions/reflective-system.md --ontology kb/notes/definitions/self-improving-system.md
```

Comparison outputs (each executed separately, exit 0):

```bash
uv run python scripts/build_systems_matrix.py --review kb/agentic-systems/reviews/dynamic-cheatsheet.md --review kb/agentic-systems/reviews/mem0.md --review kb/agentic-systems/reviews/napkin.md --output kb/reports/cache/agentic-analysis-reliability/2026-09-27/trial-matrix.csv
uv run python scripts/render_systems_table.py --review kb/agentic-systems/reviews/dynamic-cheatsheet.md --review kb/agentic-systems/reviews/mem0.md --review kb/agentic-systems/reviews/napkin.md --output kb/reports/cache/agentic-analysis-reliability/2026-09-27/trial-table.md
uv run python scripts/analyze_matrix.py --review kb/agentic-systems/reviews/dynamic-cheatsheet.md --review kb/agentic-systems/reviews/mem0.md --review kb/agentic-systems/reviews/napkin.md > kb/reports/cache/agentic-analysis-reliability/2026-09-27/trial-statistics.txt
```

The matrix is byte-identical to bundled `matrix.csv`. The table records exactly the same three review/result/source/revision tuples. Statistics stdout retains exactly six matching review/result hashes, and its fourteen positive-membership records agree with the query ledger. This checks more than successful command exits.

Current-input verification (exit 0 before synthesis writing; repeat before final return):

```bash
uv run python scripts/bundle_agentic_landscape.py verify kb/reports/cache/agentic-analysis-reliability/2026-09-27/trial-bundle --sha256 44f4ef62bda8116eeac568daae97207931a6cd4ad93f459151091a00903a76cd --source-root .
```

## Evidence reading and semantic checks

Only bundled selected results supplied findings. Full reads covered Dynamic Cheatsheet lines 1–1201, Mem0 lines 1–1003 and Napkin lines 1–1176, in sequential bounded ranges. Each delivered call was checked for truncation; none of these result reads was truncated. The declared full-read boundary includes frontmatter, sources, records, both lenses, reconciliation, limitations and verification. No source checkout or incumbent Napkin analysis was used.

The local semantic check selected these examples:

| Example | Canonical records checked in full bundled result | Acceptance limit |
|---|---|---|
| Dynamic Cheatsheet curator replacement and later delivery | RTE-2, RTE-6, CLM-4 | Inspected templates are a condition of the intended criticism route; recorded delivery and wrong retention do not establish behavioral dependence, error causation or error prevalence. |
| Mem0 internal context supply versus external retrieval | RTE-1, RTE-2, RTE-3, RTE-5, BAP-1, BAP-2 | Internal extractor push is wired; external answering consumer is afforded; additive extraction does not become automatic correction. |
| Napkin automatic writes versus skill extraction/session supply | OBJ-8, RTE-7, RTE-8, RTE-10, RTE-11 | File/cache/import code does not upgrade external skill extraction or host loading; query-driven retrieval is pull. |
| Mixed forms and evidence coverage | All three memory-comparison profiles, corresponding objects, memory lenses and limits | Positive membership includes partial coverage; weaker members cannot be filtered out to make a complete strong profile. |
| Recall-dependence uncertainty | Dynamic Cheatsheet CLM-5; Mem0 RTE-1, RTE-3, RTE-4 and limitations; Napkin CLM-1 | All three assessments remain not-determinable. Zero evidenced no values is not proof of no tests or no recall dependence. |

Every synthesis example links the original retained result and names canonical records; the synthesis identity table pins run, source revision, cutoff and exact result hash. The ledger additionally pins each review hash. Captured ontology supplies the distinction between trace-fed write machinery and stronger theory-builder/learning/reflection/self-improvement claims; the trial does not make a comparative membership or success claim.

The query ledger contains snapshot-specific executable code and exactly 21 JSON output records. A separate executable recomputation reads bundled result frontmatter, checks all 42 axis records against CSV, reconstructs all 21 query records, and checks comparison output identities. It also reruns the original query and requires byte-identical output. Both executions passed with empty stderr. This is independent computational recomputation by the same worker, not independent-agent semantic review.

No operational failure occurred after metadata parsing was repaired. The mandatory Napkin completion wait resolved before capture. No agent listing, further delegation, live failure injection, public output edit or commit occurred.

## Final checks

Final current-source verification returned exit 0 with the same manifest/matrix hashes, three selected reviews, three code-grounded rows and unchanged cutoffs. It checked every captured input against the live checkout and the selected population against the bundled matrix; no source drift was reported.

Explicit `commonplace-validate --full` checks returned exit 0 and `PASS (clean)` for `trial-synthesis.md`, `trial-query-ledger.md`, `trial-acceptance.md` and the generated cache `trial-table.md`, with no warnings or failures. The three workshop documents are frontmatter-free text with no structural requirements; the table additionally passed its note schema and link checks. Structural validation cannot certify the semantic judgments above.

Trial deliverables are ready for parent review. This completes the commissioned bounded forward test, not the parent's broader reliability acceptance or a public landscape publication.

## Retention after parent acceptance

The repair coordinator retained the exact bundle at `trial-bundle/` and the
three comparison outputs at `outputs/` beside this record. Historical commands
above retain their executed cache paths; the query ledger has executable paths
for the retained copies. Bundle bytes and hashes are unchanged. Retain these files together; the earlier repository revision is not a
reconstruction boundary.
