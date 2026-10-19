# Sift-KG — exact-publication follow-up audit

## Decision

**Specific hold — operational/authority disposition required.** The workflow
worker successfully wrote an empty file outside its assigned worktree and then
removed that file and its containing directory chain. Correcting the path and
passing content validation did not authorize those collateral actions. The
parent must decide whether this bounded incident permits integration and retain
that decision; a content rerun cannot erase it.

Within the semantic scope inspected below, no additional material publication
defect was established. The public synthesis already carries the known local
info-route attribution defect and the important source-level limits. That is
not integration clearance while the operational hold remains unresolved.

This completes the independent single-case follow-up. The earlier
`AAS-2026-10-15-sift-kg-dca68bc45a2c-01.md` remains unchanged as incomplete,
binding-only group evidence; its unfinished audit was not a production defect.

## Assignment, identity and boundaries

- Exact run: `AAS-2026-10-15-sift-kg-dca68bc45a2c-01`.
- Auditor: Pi, `openai/gpt-6.1-sol`, reasoning `medium`, independently confirmed
  from `PI_PROVIDER`, `PI_MODEL`, `PI_REASONING_LEVEL`.
- Actual auditor session: `01a146f6-5a46-73ea-b0c6-c2936c1a27cd`.
- W: `/home/zby/llm/commonplace/.commonplace/worktrees/sift-kg-dca68bc45a2c`.
- P: `W/kb/agentic-system-analyses/retained/sift-kg`.
- R: `W/kb/agentic-system-analyses/state/AAS-2026-10-15-sift-kg-dca68bc45a2c-01`.
- Source: `https://github.com/juanceresa/sift-kg`, frozen Git commit
  `d786991c024f5401f113fc0cb70aee96dd1bd3bf`, at
  `W/related-systems/juanceresa--sift-kg`.
- Method: `a568c6dc489ad546374536b642c3889ce23149a8`; plan SHA-256
  `5a5f56891d95a819c3f4fde00bb92eb301876598c022924ee52bed6262721bfd`.
- Intake SHA-256 freshly matches
  `29c5a94a2c926f9c8b895cf5a5f50b0157461fa2a8aff39779131d14ab6d530e`.

Fully read the current commission, audit-a-rerun, workshop framing, work
collection and text contracts. No delegation, analytic contact, target
execution/tests/services, fetch/install, state changes, integration, reset,
staging, commit or cleanup was performed. Only this report is an authored
output. Other pre-existing origin changes are outside this assignment.

## Fresh byte and identity binding

Recursive enumeration of P found exactly the intake's 13 files, with every
actual-byte SHA-256 equal to both the intake `published-sha256` and completed
own publish effect `new` map. No extra member was ignored. Map digest:
`da65f938e2cc3ddf5233ba48a80a408dbde0ef73dc71065b281e5246b819323b`.
Encoding: SHA-256 of UTF-8 JSON of the relative-path/hash map, sorted keys,
compact separators `(',', ':')`, without an added newline.

Freshly checked:

- preparation SHA-256
  `73c4fbf601110ba63ceeb05c412bab29dc115acf38f487cbcb4acff93c70f148`;
- run-definition SHA-256
  `3746e72ca02357270e64688864fad929cff029e1b89cc47a7b35aa241f099f73`;
- completed publish effect SHA-256
  `6401a0566cd6b2293ce07e280377d0a62afeb873ff9f37f76cdf890585f50069`;
- all 37 stored attempt metadata files equal intake hashes;
- all non-null publish input versions hash to their pins, and every publication
  byte hash resolves to an equal version blob;
- assembled manifest `871f5846c60ee404aea9f934374b66763ec4e8a94bcc8aae0d5ceb0e13e0a5de`
  equals the publish manifest pin and intake manifest, with exact hashes for all
  12 Markdown members;
- receipt `64f3a15724c46bdc296b2053b929076fefdec78e408e4878d3bc5ca6a4a9e67c`
  hashes correctly and binds the same 13-member map, run, source identity and
  method; effect destination equals P;
- opening metadata pin
  `31aadc2a932c1383ea4d38aa0c83ac4a71f2362c2ef202295b82739c1e7f31da`
  matches actual bytes; opening/intake and acquisition/source identities agree;
- prepared method HEAD and source HEAD equal the revisions above; the source
  checkout has empty `git status --porcelain --untracked-files=all`;
- actual plan bytes equal the run's plan hash.

Opening/receipt `source-revision: null` is the original unpinned request, not a
claim that acquisition lacked a revision. The acquired source object and public
boundary bind the concrete commit. Manifest worker metadata reports `pi-sol`,
Pi, `openai/gpt-6.1-sol`, medium for all roles. This binding does not certify
worker authority compliance. No source-matched canonical incumbent is listed
for this row; this audit does not grant transfer authority or check a later
canonical inventory.

## Historical comparison and source challenges

Fully read `kb/agent-memory-systems/reviews/sift-kg.md`. It identifies the same
owner/repository and **the same full source commit**, despite its earlier
2026-06-05 review date. Consequently revision drift does not explain the
following differences. Its Commonplace comparison and borrowing suggestions
are historical interpretations, not required rerun outputs or instructions to
analysts.

Fully read public boundary, overview and synthesis; runtime, memory, workflow,
reconciliation, memory profile and all three public verifications. Read the
relevant epistemic definitions/normalization account at lines 90–219, not its
entire ledger. The rerun preserves the historical central loop: imported
documents, generated/reused schema, retained extraction/graph files, resolution
and review, prose sidecars, selective graph retrieval and host-owned use.

Meaningful differences were challenged as follows:

1. **Human review versus status admission.** The old account emphasizes human
   review but also mentions automatic thresholds. The rerun makes the latter
   consequential: confirmed status is not authenticated universal human
   approval. Directly read frozen `src/sift_kg/resolve/reviewer.py:39-163`:
   default 0.85 auto-confirmation precedes interactive review, and quit leaves
   prior confirmations intact. This supports the public qualification, not a
   coverage regression.
2. **Cached/incremental does not mean content-fresh or surgery-preserving.**
   Directly read `src/sift_kg/extract/extractor.py:1-54`; `_check_stale` compares
   model, domain name and chunk size, not source contents. Directly read
   `src/sift_kg/pipeline.py:1-180`: build reloads retained extractions and calls
   fresh construction, saves graph before flags, and loads the discovered
   domain for later build. This supports the rerun's distinction between
   retention, freshness and approval. I did not independently retrace every
   extraction caller or all CLI build alternatives; those remain supported by
   the accepted records rather than a fresh exhaustive audit here.
3. **Parametric inference is not retained parametric memory.** The historical
   artifact profile includes model inference and clustering. The current
   profile explicitly scopes its inventory to retained content and excludes
   weights/transient embeddings, while runtime separately inventories those
   components. This is a declared unit-of-analysis difference, not silent
   deletion of model involvement. No dependency internals were inspected.
4. **Pull-only versus internal push.** Fully read the frozen bundled skill.
   Session-start orientation, optional direct small-graph loading and requested
   query/topology remain host protocols. The new profile distinguishes internal
   automatic supply to model/code consumers from requested CLI delivery; the
   pipeline's discovered-domain reload is a concrete internal reuse witness.
   Public synthesis does not promote it into automatic host-session injection.
5. **Trace-learning absence versus uncertainty.** The old account says no
   trace-derived retained artifacts were found. The rerun declines a universal
   negative over all possible imported content/decision origins. Neither
   account supplies an exercised trace-fed update chain. The changed
   uncertainty is explicit in profile and synthesis; it does not establish new
   target capability or conceal missing observations.
6. **Semantic normalization counterexample.** Directly checked
   `src/sift_kg/graph/postprocessor.py`'s mapping and lines 294–348. When the
   origin relation is not already valid, the code can assign TRAVELED_TO while
   keeping endpoints. The public conditional counterexample is supported; it
   is not evidence of an observed corpus incident. No target was run.

The info attribution issue is public, localized and non-blocking on this
inspection: synthesis names info's separate counts/status/existence consumer,
then explicitly withholds the broader attribution. No semantic correction
request or deep reconstruction is justified by the comparisons above. Source
accuracy, actual costs, host uptake, model compliance and downstream benefit
remain unestablished and already qualified publicly.

## Completed-trace finding and fault origin

Completed trace lead:
`/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/batch-14/sift-kg.output`.
Fresh size: 281,713,513 bytes; SHA-256:
`b35548d311a9c2e112454dfae893b57c9162c8d7b8eb7d7d0b0763312e0b98fb`.
Session header: `01a13e30-c428-7073-85c3-2307800cae37`.
The other intake lead, `outputs/sift-kg.output`, is still zero bytes and supplies
no corroborating trace.

Streamed all JSON events to inventory terminal coordinator tool calls and
terminal subagent-result message arrays, not every streamed token/prose event.
All 470 nested tool calls across the 13 analytical worker executions have
same-worker call/result matches in those arrays. Inspected the shell commands
and write/edit destinations, then the workflow incident's complete invocation
read, matched results and final response. This bounded operational pass found:

- In nested workflow result envelope at byte offset **134220312**, worker
  `000009-workflow` issued write call
  `call_8nyeeFF26U2C4HZi21r7cwOq|fc_01f20a1050fa6e6e016ad071b563c487d28dc2eae36180b87b`.
  It wrote empty content to
  `/home/zby/llm/commonplace/.commonplace/worktrees/sift-kg-dca68bc45a2c-01/state/handouts/000009-workflow/outputs/report.md`.
  Matched result reports successful write, `isError: false`, timestamp
  `1792045494811`. This is a sibling of W, not its assigned workspace.
- Call
  `call_jckFYr6f6ER0XFQh9XGdnLgi|fc_01f20a1050fa6e6e016ad071bc75b087d2a9a1734af62f130b`
  then ran `rm` on that file and chained `rmdir` on all five containing
  directories through the wrong worktree root. Its matched shell result has
  no output, `isError: false`, timestamp `1792045503946`. These are executed
  mutations, not unexecuted proposals. Successful rmdir bounds the residual
  tree; it does not establish the overwritten file's pre-write state.
- Correct-path write
  `call_NFmBbyMMMgRHHzKM1dh6eYkZ|fc_01f20a1050fa6e6e016ad071c37e8887d2b9d9d4605364bdac`
  subsequently produced the legitimate report, timestamp `1792045568862`.
  Its content equals the published workflow member, SHA-256
  `531a78047d8ceb8e9773bc6d6bf70a105adea2b9584f286d32a570a639dc6213`.
  The final worker response lists its legitimate outputs, without disclosing
  the collateral write/removal. Content validation passed with the explicit
  warning that it was not job acceptance or claim support.

The complete historical invocation was recovered from its matched trace read;
its live handout no longer exists. It supplied the correct absolute output and
workspace paths. Its pinned worker rules
`a2a29b5670a256ce21a9f55485734c82bbfa606be0668b177eb149cc58e88272`
expressly require supplied absolute paths, prohibit reconstruction, and allow
writes only to named outputs/problem/identity and scratch. Its workflow mission
`93bbd051e9b232efdb1dd3f4301b68224962d8ee93e8d72f5d33fb0f7d89aceb`
adds no collateral-write authority. Both version blobs were read completely and
rehash correctly. No scope ambiguity authorizes the wrong path or cleanup.

### Earliest output, missed barrier and restart classification

- **Origin:** `000009-workflow`, operational/authority, not deep or local
  analytical reconstruction. The first evidenced fault is the successful
  off-scope empty write, followed by off-scope cleanup. No faulty source record
  or erroneous installed semantic claim has been established.
- **First installed output associated with the incident:** workflow report
  hash above, accepted from `000009-workflow`; the publish-pinned attempt blob
  is `959a6a662efdf9da453681322efde6e8d0ff1dae45f48e68698c12b61a458710`.
  `000036-assemble` and `000037-publish` bind that report/attempt. It is not
  correct to pretend the wrong empty file itself became the installed report.
- **Missed barrier:** the worker's path/authority check before writing and
  escalation/disclosure after the mistake; then the coordinator's completion
  handling accepted workflow at terminal call envelope byte offset 136242873
  (`call_FSu4PprG8rXB5IntPYlwPhIN|fc_079a98f2448538b2016ad072d3680c87d2853c0ea4a2feaeae`).
  Publication success did not settle the returned worker trace's authority.
- **Verifier attribution:** `000021-report-check` and
  `000022-report-verification` allowed the legitimate workflow content onward.
  The latter pins the same report and mission
  `41163de951b29115cfad318fa1f3baf7b36a94ee730dbb93b2d91397145490b2`,
  read completely and rehashed. Its mission verifies records/source, not
  worker execution traces. Do not falsely diagnose it as having inspected and
  excused the collateral operations. The missed operational barrier belongs
  to worker/coordinator handling and this pre-integration audit, not a claimed
  semantic-verifier obligation to discover unavailable history.
- **Author correction/restart:** none selected. The actual origin job is
  `workflow`; rerunning that author job cannot authorize its earlier actions.
  No deep restart at boundary/runtime and no profile/synthesis rewrite is
  supported by this finding.
- **Verification restart:** none of `report-verification`,
  `profile-verification` or `synthesis-verification` clears this operational
  hold. Required next action is parent-owned authority/collateral-effect
  disposition of the exact incident. If the parent separately commissions a
  new workflow output, `workflow` is the actual author job and
  `report-verification` its semantic verification restart; that would be a
  separate decision, not a remedy selected or executed here.
- **Other categories:** no independent deep, local-content or incumbent-transfer
  hold established. Evidence limit: no pre-write filesystem image proves that
  the empty write did not replace a pre-existing file. The trace bounds the
  observed operations but does not authorize an assumption of zero collateral
  impact. Resolve or explicitly accept that uncertainty before integration.

## Validation and concrete coverage limits

Executed exactly from W, using its prepared executable:

```sh
cd /home/zby/llm/commonplace/.commonplace/worktrees/sift-kg-dca68bc45a2c
/home/zby/llm/commonplace/.commonplace/worktrees/sift-kg-dca68bc45a2c/.venv/bin/commonplace-validate /home/zby/llm/commonplace/.commonplace/worktrees/sift-kg-dca68bc45a2c/kb/agentic-system-analyses/retained/sift-kg
```

Exit 0: `VALIDATION SUCCESS`; one directory artifact, zero failures and zero
warnings. This is deterministic content/set validation, not authority or
semantic certification.

Executed report validation from the same cwd:

```sh
/home/zby/llm/commonplace/.commonplace/worktrees/sift-kg-dca68bc45a2c/.venv/bin/commonplace-validate /home/zby/llm/commonplace/kb/work/agentic-system-reruns/audits/current-publications/AAS-2026-10-15-sift-kg-dca68bc45a2c-01-followup.md
```

Exit 0: `VALIDATION SUCCESS`; one text file, zero failures and zero warnings.
Neither command emitted an additional notice.

This is not an exhaustive source reanalysis. Fresh source reads are exactly the
skill, extractor opening/cache predicate, pipeline opening/build, merge-review
body and normalization mapping/body described above, plus scoped searches.
Other mechanisms rely on the fully read accepted records and their retained
witnesses. Dependency internals, test bodies, examples, all CLI alternatives
and the full epistemic ledger were not independently retraced. No new source
or target operational evidence was acquired. The completed production trace is
analysis-worker history, not a sift-kg target execution trace. The operational
scan does not certify every required read, every truncation recovery, all shell
script semantics or undisclosed external effects. It is sufficient to establish
the specific paired write/removal incident. Missing handout files were not
reconstructed on disk. Parent owns acceptance and recovery; no analytical
feedback has been sent to the producing run.
