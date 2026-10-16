# AI Memex CLI renewed-publication audit

## Disposition: hold

The renewed publication changes the synthesis verifier's judgment, not the public synthesis. A narrow source-attribution defect remains: the synthesis criticizes a README implication of already **resolved** contradictions, while the README promises already **flagged** contradictions. Reclassifying this as immaterial in a supporting verification does not correct or qualify the public attribution. The implementation account remains useful; this hold does not call for exhaustive reanalysis.

**Unblock:** produce an authorized, accepted publication whose public synthesis accurately states the flagging claim or explicitly withdraws the resolution attribution. Rebind and validate the resulting bytes and independently check this issue. The parent owns the supported recovery route; this audit neither edits accepted outputs nor authorizes integration.

## Identity and inspection boundary

- Auditor: independent Pi session `01a14620-b946-77ad-aa7a-0fdf07f603bf`; environment reports `openai`, `gpt-6.1-sol`, reasoning `medium`. No delegation or analysis-worker feedback.
- Run: `AAS-2026-10-15-ai-memex-cli-4324549b4bc0-01`.
- `W`: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-17-ai-memex-cli`.
- `S`: `W/kb/agentic-system-analyses/state/AAS-2026-10-15-ai-memex-cli-4324549b4bc0-01`.
- `P`: `W/kb/agentic-system-analyses/retained/ai-memex-cli`.
- `A`: `W/kb/agentic-system-analyses/state/.reset-history/AAS-2026-10-15-ai-memex-cli-4324549b4bc0-01/d9e3230fb9944819ab27255b386c17f8`. Old publication: `A/effects/0/before`; old run: `A/before`.
- Upstream identity: `https://github.com/zelixag/ai-memex-cli`. Frozen checkout `W/related-systems/zelixag--ai-memex-cli` has HEAD `4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f` and empty short status.
- Prepared method: `989a702d695f78f4c329a29144878377a6e04f7b`, retained in opening metadata version `92c22fec369db29701fa6cdebcb97b4903009ca7f5b4387090951828f20219c2` and overview. Current and archived `run.json` are byte-identical, SHA-256 `af9ed53a588b7afd4688a169dc96ea13147540d71ebff2dc2fc9cefc0f8d81c7`; plan hash is `5a5f56891d95a819c3f4fde00bb92eb301876598c022924ee52bed6262721bfd`. Acquisition effects are byte-identical and pin the same upstream identity/revision. This is a downstream reentry, not new source or method evidence.

Method: hash every recursive old/new publication file; inspect both changed files' complete deltas; read the historical review, overview, synthesis and verification records completely; inspect source for the consequential attribution and two historical mechanism leads. The prior audit was a discrepancy lead, not an accepted verdict.

## Exact byte binding and old/new comparison

Recomputed all 13 current file hashes. The complete map equals `S/effects/publish.json:new`, with no extra or missing files. That completed effect names this run, upstream identity and destination; `expected: absent`, `old: null` refer to publication after reset, not proof there was no earlier publication. Effect SHA-256: `d10252be198dcdad05b2bd6799bb9cc5e3271a7e66d2d5b427cf9d180c9df290`.

The manifest pins all twelve Markdown members to these bytes. All working Markdown members also match P; the working `artifact/ARTIFACT.yaml` is only the type stub, whereas attempt `000036-assemble` produces the full published manifest. This is not an unexplained publication mismatch.

| Member | Current SHA-256 | Compared with old publication |
|---|---|---|
| ARTIFACT.yaml | `3ceb466d1c3705970d3fc2a7c63fe882f0f6b37ee73c1bedc4aab2bdc039bb49` | Changed only synthesis-verification hash |
| boundary.md | `184947c5495b0d539fbb5570dbf10c3276503b0829864b5a6287c66769c53fa2` | Identical |
| epistemic.md | `dc119cd5f83605732a77fd808c9575263294aa5b29d06848edfed89bb8990311` | Identical |
| memory-profile.md | `376f1cc6b4a2d272c1aebe8c4c3f61c9fa62866a1c3262aad5b332ce542d2010` | Identical |
| memory.md | `9347de0bc15ae78d2cfccbfd147dfdd562e2d8b6eeb9a39e61273b1bcd567b66` | Identical |
| overview.md | `62e693f6d9ad7e3197ea3f7f9dc577ae586bc79ba75e1af37f9a471b6f147b3f` | Identical |
| profile-verification.md | `102a688bfae78d6aa6478d6cd3780604a45a814ee14051c152095bdd0220faf1` | Identical |
| reconciliation.md | `4b1e3b297cd7593cc54d21cd4fb3bc1eaa45ebea072e95d8c5e6d6ee4340e1e7` | Identical |
| report-verification.md | `51a2155b16ca9930243086942e28af3d833dc1f285d33c4ad03325f83304ee43` | Identical |
| runtime.md | `b21b7537df07117c99a468f7183662f3a69d338c294e68c88e631d7a5558daf1` | Identical |
| synthesis-verification.md | `4bdea64cc59424bab5df1113e6675ef29c8aa7db0a8526eee2bdeab550dc3aca` | Changed |
| synthesis.md | `94ec4923a404ac31553353aa94eeb2b5c49cd4a994d7aa99bc0d6847cc6104ae` | Identical |
| workflow.md | `8b7e372d07498ae41f179b7c0cd734941b1bbb4ac596523cb52d40366176bf35` | Identical |

Old manifest: `f0867829713c573d36447da211c361fb1d406c868d88bb02c52fb88f717bc684`. Old synthesis verification: `48f8d0415b38c2ee9d204df38b91d022154916d738f7c551ecaf811d81bee22e`. The other eleven hashes above also bind their old counterparts. No files were added or removed.

## Findings

### 1. Unresolved attribution; the explicit limit was downgraded, not repaired

`P/synthesis.md:40`, under “Make retained material available to later work,” says the architecture does not establish “the README's stronger implication that contradictions are already resolved.” Frozen `README.md:14` instead says “Contradictions have already been flagged.” Its nearby workflow description explicitly describes semantic lint “without flattening contradictions” (`README.md:48`). The supporting record `EPI-CLM-memory-compounds` correctly retains the flagging quotation.

Flagging a conflict and adjudicating it are different operations. Criticizing the latter as an advertised implication overstates what the cited source promises. The adjacent claim about synthesis reflecting everything read is actually in the README; it does not support the separate resolution attribution. The broader conclusion that semantic correctness and comprehensive integration are unestablished remains defensible.

The old verification's Limits explicitly identified this attribution defect. The new verification expands its reasoning and moves the issue into “Later consumption and independent property findings,” acknowledges that the quotation says flagged, then declares that it needs no publication limit because the larger conclusion survives. Its Limits now repeats the instruction-variant limitation. This is a consequential change of judgment, not a mere wording regression. The acknowledgment remains only in a supporting member; the public synthesis and overview are unchanged. Neither public surface distinguishes the overstated attribution from ordinary uncertainty about semantic success. This is why the hold persists independently of the earlier audit's decision.

### 2. Useful coverage preserved; no source-account improvement established by reentry

The historical review `kb/agent-memory-systems/reviews/ai-memex-cli.md` was read completely. It reviews the same frozen commit despite its earlier check date. Its mechanisms remain covered: Markdown raw/wiki separation, external semantic agents, fetch/session capture, lexical/optional-qmd retrieval, includes/projections, lint/watch feedback, native host installation and persistent context blocks. Runtime records `RT-RTE-install-update`, `RT-RTE-context-delivery` and `RT-RTE-session-distill` retain details compressed out of the public synthesis. No new loss of those mechanisms occurred in reentry.

The publication already improves on historical overstatements: raw immutability is policy rather than guaranteed storage behavior; mechanical session rendering is not semantic distillation or guaranteed redaction; context delivery is not demonstrated activation; structural cleanliness is not factual acceptance. Direct source reading confirms two important qualifications: `src/commands/inject.ts` accepts but does not consume task/token options, and `src/core/ingest-lint-loop.ts` catches ingestion failure before lint, accepts zero structural issues, retains earlier edits and refreshes best effort. Thus the old description of budgeted context and self-healing cannot be preferred merely because it is historical.

The installed-versus-local lint variation is already public in the synthesis body and limitation table, supported by report verification. It is not newly repaired by repeating it in synthesis verification. Historical Commonplace comparisons, borrowing proposals and watch-list predictions are outside the new source-grounded account's purpose; their omission is not a coverage regression.

## Operational evidence and limits

Actual state distinguishes renewed completion from correction. Archived attempts `000030`–`000033` performed synthesis verification, application, assembly and publication. Current attempts `000034`–`000037` repeat those downstream stages. The original synthesis attempt `000028` and structural check `000029` remain byte-identical to the archive; its answer output is the empty-file hash. New attempt `000034-synthesis-verification` reports `openai/gpt-6.1-sol`, `medium`, the new verifier hash and empty answers. Judgments `000035-apply-synthesis-verification-0` and `-1` are accepted with empty findings; the latter verifies the unchanged synthesis hash. `000036-assemble-0` is accepted and `000037-publish` is completed. These establish successful downstream acceptance, not a corrected synthesis or independent integration acceptance. Current stored judgments contain no refused outcome requiring a hidden correction explanation.

The supplied original coordinator trace is `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/batch-17/ai-memex-cli.output`. It was not replayed in this bounded reentry inspection. New coordinator handle `99878c5a-4809-4a42-a6f8-6aaf4224223c` is not accessible as a tool/session trace here. Therefore new worker tool use, complete input reading, truncation recovery and compliance are not independently certified. Stored attempts and the verifier's declared no-source-read boundary are the inspected evidence, not invented trace coverage.

No target code, tests, services, actual vault or host behavior was exercised. Source inspection stopped after the bounded attribution finding and historical checks; this is not exhaustive security, compatibility or semantic reanalysis. No publication, source, workflow state, index, ledger or Git state was edited. Only this report was authored.

## Validation

Using cwd W and W/.venv/bin prepended to PATH:

- `commonplace-validate kb/agentic-system-analyses/retained/ai-memex-cli`: `VALIDATION SUCCESS`; files analysed 1, text files 0; diagnostics 0 failures, 0 warnings.
- `commonplace-validate /home/zby/llm/commonplace/kb/work/agentic-system-reruns/audits/post-migration/AAS-2026-10-15-ai-memex-cli-4324549b4bc0-01-reentry.md`: `VALIDATION SUCCESS`; files analysed 1, text files 1; diagnostics 0 failures, 0 warnings.

Deterministic validation does not resolve the attribution finding.
