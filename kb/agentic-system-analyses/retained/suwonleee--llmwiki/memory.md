---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "llmwiki memory: transcript-to-wiki compilation, bounded context supply, version-bound feedback, topic maintenance and human quiz state."
run-id: AAS-2026-11-08-llmwiki-7f7e35008c0f-01
source-identity: https://github.com/suwonleee/llmwiki
reviewed-boundary: "e6be788bdfd969c3695f839a5d6b5752bb233cfc"
---

# llmwiki memory report

## Boundary and evidence

This report covers llmwiki's retained project knowledge and the machinery that selects, transforms, withholds and later consumes it. It uses SRC-1 at the frozen revision in [boundary](boundary.md). Included are the foreground save/deep procedures, passive capture, optional unattended generation, arbitrary-file ingest, explicit query/file-back, topic consolidation/distillation, automatic context and edit rules, version-bound feedback, freshness acknowledgements, cleanup and human quiz scheduling. External host windows, provider weights and live transcript stores are not available evidence. No target execution was performed. Implementation findings establish wiring, not actual deployment, compliance or benefit.

The supplied runtime establishes ordinary capture, save, context, edit-rule, autoupdate and deep routes. Direct source reads below extend those findings rather than treating runtime as an inspection limit. All added paths remain under SRC-1; no new source identity is introduced.

| Entry point or operation | Source paths and evidence basis | Coverage / prevented conclusion |
| --- | --- | --- |
| Passive capture; warm save; snapshot issuance and marking | Supplied runtime: `src/daemon/watch.ts`, `src/engine/update.ts`, `src/engine/update-pages.ts`, `src/engine/extract.ts`, `skill/wiki-save.md` | [RT-RTE-passive-capture](runtime.md#rt-rte-passive-capture), [RT-RTE-warm-save](runtime.md#rt-rte-warm-save); raw/snapshot lineage retained below. Parser adapters not exhaustively re-audited. |
| CLI dispatch and alternate acquisition | Direct `src/cli.ts` command map/search, `src/engine/ingest.ts`; runtime autoupdate | Arbitrary-file ingest reuses autoupdate, with optional force-reset; [RT-RTE-auto-update](runtime.md#rt-rte-auto-update). Exact per-format extraction remains a limit. |
| Cold/turn push, explicit search, hooks and adapters | Direct selected `src/engine/context.ts`, `src/engine/turncontext.ts`, `src/engine/page-rank.ts`; hook/CLI call-site searches; supplied adapter findings | [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery), annotations; prompt-dependent selection, budgets and authority distinguished. Commit/absence channels are supplied-runtime findings, not independently fully audited. Their retained parts and negative-claim evaluators are not independently inventoried; not all per-turn content can be attributed to accepted wiki pages. |
| Recall-selection projection | Correction-round direct full `src/engine/page-rank.ts`, full `src/engine/knowledge-policy.ts`, and turn selection/excerpt range of `src/engine/turncontext.ts` | [MEM-OBJ-recall-triggers](#mem-obj-recall-triggers) separates lexical trigger authority from imperative delivery in [MEM-OBJ-wiki-rules](#mem-obj-wiki-rules). No measured effect inferred. |
| Before-edit rules | Direct `src/engine/knowledge-policy.ts`, ranker; supplied hook/rule implementation | [RT-RTE-edit-rules](runtime.md#rt-rte-edit-rules), [MEM-OBJ-wiki-rules](#mem-obj-wiki-rules). Manual reads and unknown Bash targets remain outside that gate. |
| Index, raw provenance and source currency | Direct `src/engine/schema.sql`, selected `src/engine/db.ts`, full `src/engine/source-freshness.ts` | [MEM-OBJ-wiki-index](#mem-obj-wiki-index), [MEM-RTE-freshness-recheck](#mem-rte-freshness-recheck). Whole DB rebuild equivalence is not established. |
| Query answer and file-back | Direct full `skill/wiki-ask.md`, CLI search dispatch, page ranker | [MEM-RTE-query-fileback](#mem-rte-query-fileback); human approval policy differs from routine save. Host compliance unobserved. |
| Topic merge and distillation | Direct `src/engine/consolidate.ts` acquisition/helpers and publication half; full `src/engine/distill.ts`, `skill/ref/distill.md` | [MEM-RTE-topic-merge](#mem-rte-topic-merge); supplied deep route. Claim preservation is not guaranteed by citation-set preservation. |
| Review, gaps and overview | Direct `src/engine/session-review.ts`, initial semantic-review selection/prompt code in `src/engine/review.ts`; supplied deep orchestration | [MEM-OBJ-review-reports](#mem-obj-review-reports). Legacy review publication, overview and gap state internals not fully inspected; complete automatic application or gap-resolution correctness prevented. |
| Emissions, explicit feedback and downstream reranking | Direct `src/engine/observe.ts` emission writer, full `src/engine/injected-feedback.ts`, `src/engine/reported-wrong.ts`, `src/engine/work-feedback.ts`, selected `src/engine/affinity.ts`; daemon/CLI call searches | [MEM-OBJ-emission-ledger](#mem-obj-emission-ledger), [MEM-RTE-feedback-fold](#mem-rte-feedback-fold), [MEM-OBJ-work-feedback](#mem-obj-work-feedback). Automatic legacy read-scan refresh is disabled by default; no actual usage inferred from emission. |
| Tier cleanup and withdrawal | Direct `src/engine/tiering.ts`, plan/apply portions of `src/engine/wiki-clean.ts`, capture export/prune code | [MEM-RTE-tier-cleanup](#mem-rte-tier-cleanup), [MEM-OBJ-capture-state](#mem-obj-capture-state). Tiering changes access, not page truth or physical body deletion. |
| Quiz | Direct `skill/wiki-quiz.md`, `src/engine/quiz.ts` selection/record code and declaration search; DB exclusion search and ranker exclusions | [MEM-OBJ-quiz-ledger](#mem-obj-quiz-ledger). Human-facing recollection loop, not model training; question quality/recall benefit unobserved. |
| Other public diagnostics and maintenance | CLI inventory includes digest, topics, related, excerpt, reconcile, context-audit, doctor, longitudinal-report, DB maintenance, migration and export | Supplied runtime covers bookkeeping at route level. No exhaustive independent audit of every command, database migration, OS wiring, export format or fixture. Prevents universal retention, security and efficacy claims, not the positive paths traced here. |

## Core ideas

1. **The wiki is derived experience made readable, not a transcript replay.** The host model compiles useful human-expressed facts, decisions and insights into Markdown; capture state controls what remains to be processed. Transcript identity and byte receipts are not authored knowledge. See [RT-RTE-warm-save](runtime.md#rt-rte-warm-save), [MEM-OBJ-wiki-pages](#mem-obj-wiki-pages) and [MEM-OBJ-capture-state](#mem-obj-capture-state).
2. **Knowledge and access policy are separate.** Retirement, cold tier, expiry, changed sources and wrong reports influence different consumers differently. Cold pages remain discoverable by metadata; their bodies are not automatically excerpted. Changed-source prose can be supplied with a warning while its rule is withheld. This is not one system-wide truth/admission bit ([RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery), [RT-RTE-edit-rules](runtime.md#rt-rte-edit-rules), [MEM-OBJ-wiki-rules](#mem-obj-wiki-rules)).
3. **Read-back is both requested and automatically supplied.** Wiki-ask requests search, then explicitly reads pages and raw evidence. Hooks push selected L0, excerpts and rule reminders without an explicit wiki lookup. A path is a reload opportunity, not proof of a later Read. Citation evidence and rationale stored on a page need not survive the bounded excerpt transformation ([MEM-RTE-query-fileback](#mem-rte-query-fileback), context annotation).
4. **Feedback can change selection without changing knowledge prose.** Version-bound judgments become compact reranking evidence or factual recheck markers. Silver work-feedback cases instead remain diagnostic assertions. Neither is an independent truth label or proof of improved capacity ([MEM-RTE-feedback-fold](#mem-rte-feedback-fold), [MEM-OBJ-work-feedback](#mem-obj-work-feedback)).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-wiki-pages
Label: Project wiki knowledge pages

Source-native identity: `docs/wiki/` category pages, living topic pages and configured L0/overview. Natural-language claims and rationale live in Markdown files under the project; YAML paths, source declarations, status/tier and rule targeting have symbolic roles separated below. Lineage: raw transcripts/code/dropped documents → model selection/synthesis → page bodies, citations and optional retained evidence excerpts; L0/topic synthesis is not raw history. Consumers include subsequent host invocations, query answers, review/consolidation and human quiz authorship. Authority at each model consumer is reference knowledge except explicit rule reminders; human-direction policy is not a general parser-level approval proof. Compared with supplied [RT-OBJ-save-skill](runtime.md#rt-obj-save-skill), these are changed-through-use products, not shipped writer instructions; no counterpart object was supplied. SRC-1, `skill/wiki-ask.md`, `src/engine/consolidate.ts`, `src/engine/context.ts`; supplied [RT-RTE-warm-save](runtime.md#rt-rte-warm-save).

> //   • the TOPIC ENCYCLOPEDIA (5_topic) — per-concept, create-or-update, MERGED in place —
> //     the living page for a recurring concept, module, or pattern (built here).
> --- `src/engine/consolidate.ts`

Rationale may persist in ordinary decision prose and cited evidence, but its presence in every page is not established. The query procedure requests raw verification; turn excerpts deliberately strip footnote definitions and evidence lines. Thus storage of reasons is not proof that an automatically supplied claim carries its reasons.

#### MEM-OBJ-wiki-rules
Label: Wiki rule and recall extension

Source-native identity: `x-llmwiki` rule, recall phrases and `applies_to` targeting on a wiki page. Storage: page YAML/Markdown; rule content and recall phrases are natural language. Glob matching, shape/length checks and freshness flags are symbolic consumers. This is a materially different part from ordinary page prose: rule text can be withheld while factual prose is excerpted, and targeting/recall influences retrieval. Distinct from [RT-OBJ-save-skill](runtime.md#rt-obj-save-skill); delivered by [RT-RTE-edit-rules](runtime.md#rt-rte-edit-rules) and [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery), not a duplicate of those routes. SRC-1, `src/engine/page-rank.ts`, `src/engine/knowledge-policy.ts`; supplied edit-rule record supplies parsing/provenance limits.

> return !state.retired && !state.cold && !state.stale && !state.sourceChanged && !state.reportedWrong;
> --- `src/engine/knowledge-policy.ts`

> if (rule.length > RULE_MAX_CHARS) rule = ""; // Never inject an instruction with its exception truncated.
> --- `src/engine/page-rank.ts`

This record remains the extension container. Its retrieval-selection part is declared separately as [MEM-OBJ-recall-triggers](#mem-obj-recall-triggers); trigger matching is not imperative delivery, and `applies_to` path targeting belongs to the edit-rule consumer rather than the recall selector.

Lineage is page authorship/maintenance, not an independent verification service. Actual downstream force is a model-facing imperative reminder plus the scoped one-time denial; neither YAML nor human-verification-looking metadata demonstrates obedience or human authorization.

#### MEM-OBJ-recall-triggers
Label: Wiki recall and rule retrieval triggers

Part of: [MEM-OBJ-wiki-rules](#mem-obj-wiki-rules)

Source-native identity: the `x-llmwiki.recall` strings and rule text projected into `WikiPage.trigger` by `triggersOf` and `parseWikiPages`. Storage substrate: page YAML on disk, then a derived cached string in the ranker's parsed-page data. Unlike the container's imperative rule delivery and symbolic `applies_to` glob matching, this part is consumed as lexical selection metadata. The author writes natural-language anticipated requests; the ranker consumes their normalized character strings symbolically through substring matches, rarity weights and coverage rules, not by interpreting them as instructions. No numerical embedding or weight update is involved. SRC-1, `src/engine/page-rank.ts`.

> const recall = [v.recall].flat().filter((r): r is string => typeof r === "string" && r.trim() !== "").map((r) => r.trim());
> --- `src/engine/page-rank.ts`

> const trig = [rule, ...recall].join(" ").toLowerCase();
> --- `src/engine/page-rank.ts`

Lineage: page authoring or maintenance supplies the phrases; code trims recall strings, collapses rule whitespace, excludes overlong rule text, joins both sources and adds a despaced copy. Recall strings can remain when rule text is absent or excluded. Per-content human approval is not established by this parser: it checks value shape, not authorship or human verification. Foreground routine admission remains that of [RT-RTE-warm-save](runtime.md#rt-rte-warm-save); this projection introduces no separate semantic approval. Editing the metadata changes the cached parse under the file fingerprint, rather than requiring FTS reindexing. Initial phrase provenance on arbitrary existing pages is unresolved.

Consumers and authority: `rankPages` reads trigger text for both explicit `searchWiki` and automatic turn selection. A trigger hit adds a relevance bonus of 3 times term rarity and can promote coverage for sufficiently long terms. This is authority over which retained page is selected, not authority for the trigger phrase itself to command a host model. It is distinct from [RT-OBJ-save-skill](runtime.md#rt-obj-save-skill), which instructs the writer, and is a contained part of the existing extension object, not a duplicate of [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery).

> const inTrigger = page.trigger.includes(t);
> --- `src/engine/page-rank.ts`

> const named = inTrigger ? TRIGGER_BONUS : inIdentity ? IDENTITY_BONUS : inTags ? TAG_BONUS : 0;
> --- `src/engine/page-rank.ts`

Selection and delivery differ: turn selection still requires current-prompt relevance/coverage, excludes retired pages, deduplicates the session and limits the selected pages. It ranks trigger text before the excerpt-stage `canInjectRule` check. Cold or stale/source-changed rule-bearing pages can therefore remain discoverable as pointers while their imperative rule text is withheld; explicit search also consumes trigger text without that imperative-delivery gate. `applies_to` is not an input to this trigger construction. Selected pointers and eligible bounded excerpts reach the host through the existing context route; recall strings are not themselves explicitly delivered as a separate instruction block. Rule text has two consumption paths: lexical trigger here and imperative reminder in the container's rule-delivery path. SRC-1, `src/engine/turncontext.ts`, `src/engine/knowledge-policy.ts`; [RT-RTE-edit-rules](runtime.md#rt-rte-edit-rules).

> if (!excerptEnabled()) return [head, ...pages.map(pointer)].join("\n");
> --- `src/engine/turncontext.ts`

> if (e.rule && !canInjectRule(e.page)) return;
> --- `src/engine/turncontext.ts`

- implementation conclusion status: wired
- operation conclusion status: uninspected

No observed trace demonstrates that a recall edit changed retrieval or later coding behavior, and selection metadata is not evidence of truth, compliance or benefit.

#### MEM-OBJ-capture-state
Label: Capture queue and retained source pointers

Source-native identity: central `capture.db` queue, route hints, source kind, watermark/issued offsets and source exports; interactive extraction snapshots are temporary derived input under the supplied save route. Queue and receipts are symbolic access/processing metadata; raw utterances/exports are natural-language evidence with structured harness envelopes. These are not page knowledge, model parameters or evidence of successful filing. Storage includes machine state and host-owned source files; OpenCode plaintext exports are engine-owned body copies. Initial host transcript provenance is outside capture, while known parsing/screening/snapshot transformations are retained by [RT-RTE-warm-save](runtime.md#rt-rte-warm-save). No supplied object counterpart; this supplies storage/lineage for [RT-RTE-passive-capture](runtime.md#rt-rte-passive-capture). SRC-1, `src/engine/capture.ts`, `src/engine/db.ts`.

> // Tombstone, not deletion (2026-07-22 decision, device 2): the transcript is gone, so this row
> // is the ONLY remaining evidence that the session existed at all. It leaves `pending` — nothing
> // will ever condense it — but stays auditable, and stays silent.
> --- `src/engine/capture.ts`

Consumers: pending writers, citation registration and capture diagnostics. Missing aged pending sources become lost; vanished ephemeral destinations become skipped. OpenCode export expiry removes owned body/meta pairs and pending rows, but distilled/skipped ledger rows remain. This limits later raw verification even when a wiki citation and registration pointer survive. Lost source bodies are not reconstructed by a metadata pointer.

#### MEM-OBJ-wiki-index
Label: Per-project wiki index and provenance registry

Source-native identity: engine-held `index.db`, document rows/chunks, trigram FTS and reference graph. Symbolic text indexes and graph rows derive from Markdown and metadata; chunk text remains natural-language content when displayed to models. Transcript registration inserts filename, original path and session metadata without transcript body. Consumers include non-wiki FTS lookup, reference/lint/synthesis tooling and source-change warning checks; default wiki ranking reads current checkout pages rather than querying only this index. Distinct from the shipped policy object [RT-OBJ-save-skill](runtime.md#rt-obj-save-skill), and an input/storage layer for [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery), not that route itself. SRC-1, `src/engine/schema.sql`, `src/engine/db.ts`, `src/engine/page-rank.ts`, `src/engine/source-freshness.ts`.

> // Reflect the real source extension (rollout.jsonl → jsonl, a dropped notes.md → md)
> // instead of hardcoding jsonl, now that non-Claude sources can be registered.
> --- `src/engine/db.ts`

> JSON.stringify({ transcript_path: transcriptPath, session_id: sessionId }),
> --- `src/engine/db.ts`

The schema's broad claim that everything is derived needs qualification: `registerTranscript` supplies external pointers, `reindex` preserves transcript rows, and freshness acknowledgements create verification receipts inside the DB. Complete reconstruction of these from wiki bodies alone is not established. Content hashes and graph invalidation are access/freshness mechanisms, not factual validation.

#### MEM-OBJ-emission-ledger
Label: Versioned emission metadata

Source-native identity: `observe/emissions.jsonl` and rotation, engine-held per-project state. Form: symbolic JSON rows with session, channel, root, emitted page paths, page SHA-256 snapshots and byte counts. It is not a copy of the emitted excerpt or a full page snapshot despite the `snapshots` label: those entries are path/digest pairs. Producer is context/edit-rule recording; later consumers are exact-session injected-page feedback and explicit observation/affinity analysis. Distinct from [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery), whose delivery it records; no supplied object counterpart. SRC-1, `src/engine/observe.ts`.

> if (bytes !== null) snapshots.push({ page, sha256: createHash("sha256").update(bytes).digest("hex") });
> --- `src/engine/observe.ts`

The writer bounds snapshot pages to 64, rotates at its byte cap and catches failures. Emission establishes supplied output, not reception, usage or recoverable historical text. An old digest can identify a version that is no longer readable from the current page.

#### MEM-OBJ-usage-affinity
Label: Explicit usage affinity and recheck aggregate

Source-native identity: immutable session receipts in `injected-feedback/`, resolution receipts in `rechecks/`, compact `observe/usage-affinity.json`, with optional legacy `observe/affinity.json`. Symbolic JSON aggregates/counts/hashes steer deterministic selectors; natural-language evidence/verification strings in receipts retain the submitter's reasons. These are not model-weight updates or knowledge-page edits. Lineage and differing admission paths are in [MEM-RTE-feedback-fold](#mem-rte-feedback-fold). Consumers: `loadAffinity`, turn/cold ordering, `reportedWrongPages`, recheck queue and rule eligibility. Distinct from the emission ledger and from supplied [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery). SRC-1, `src/engine/injected-feedback.ts`, `src/engine/reported-wrong.ts`, `src/engine/affinity.ts`.

> // Explicitly reported wrong versions do not retain positive ranking evidence while pending.
> --- `src/engine/injected-feedback.ts`

Reasons remain in receipts/recheck items; hot-path selection consumes counts, hashes and markers rather than adjudicating that prose. The metadata has authority over selection/withholding, not authority to rewrite the underlying claim or certify it false.

#### MEM-OBJ-work-feedback
Label: Silver work-feedback regression receipts

Source-native identity: machine-local `work-feedback/<session-hash>.json`. Mixed natural-language task assertions and symbolic query/page/evidence paths, hashes and required/forbidden exact strings. Input author supplies one or two concrete cases, code snapshots current page and raw evidence; immutable per-session receipts have file/count/size limits. Consumer `checkFeedback` replays retrieval and exact excerpts against the original assertions; changed raw evidence invalidates the case. Not a ranking reward and not an automatic page author. Distinct from [MEM-OBJ-usage-affinity](#mem-obj-usage-affinity) and supplied save route, which can request recording it. SRC-1, `src/engine/work-feedback.ts`, `skill/ref/work-feedback.md`.

> const context = buildTurnContext(root, c.query, "", { affinity: null });
> --- `src/engine/work-feedback.ts`

This evaluation path has a supplied expected result: case-author required/forbidden strings, not an independent correct task solution. It exercises retrieval without live affinity. It retains task evidence assertions rather than demonstrating improved capacity or causally effective learning.

#### MEM-OBJ-review-reports
Label: Semantic review drafts and snapshots

Source-native identity: generated semantic-review reports under the review queue, including provider-based legacy review and foreground session-review import. Natural-language criticisms/recommendations with symbolic bounded page/hash/scope metadata; storage is project Markdown, with preparation returned as JSON. Session review selects up to 40 non-retired recent pages, 450-character excerpts; import binds report to current page hashes and selected scope, screens content and checks links. Consumer is a later explicit maintenance session, not an automatic repair executor. Distinct from [RT-RTE-deep-maintenance](runtime.md#rt-rte-deep-maintenance), which orchestrates using these inputs. SRC-1, `src/engine/session-review.ts`, `src/engine/review.ts`.

> throw new Error("review snapshot scope changed; prepare current review-input again");
> --- `src/engine/session-review.ts`

Legacy semantic review uses brief/excerpt selection and a separate generative call; its prompt treats current-state/overview as latest authority. Reports are advisory drafts. Their existence is not evidence that a criticism was applied or retained in a successor page; bounded excerpts prevent a full-wiki contradiction guarantee.

#### MEM-OBJ-quiz-ledger
Label: Human quiz ledger and notebook

Source-native identity: per-person `docs/wiki/6_quiz/quiz-ledger.<id>.md` plus dated quiz records. Symbolic embedded quiz markers encode box, due date, counters, last result/question; natural-language notebook records human answer, verdict and grounded answer. Engine scheduling reads/writes ledger; foreground model reads selected wiki pages to author/grade questions; human receives questions and answer explanations. Records are excluded from ordinary model knowledge retrieval, while due-count metadata can reach cold-start. Distinct from [RT-OBJ-save-skill](runtime.md#rt-obj-save-skill) and wiki knowledge prose. SRC-1, `src/engine/quiz.ts`, `skill/wiki-quiz.md`, `src/engine/page-rank.ts`.

> const box = opts.result === "correct" ? Math.min((prior ? prior.box : 0) + 1, INTERVALS.length - 1) : 0;
> --- `src/engine/quiz.ts`

Retention horizon is repeated human quiz sessions. Correct/wrong/skip is caller-supplied grading; the page is the instructed answer key. Due wrong/skip precedes other review and new candidates; a maximum seven items is selected. Missing pages are pruned on recording; superseded/draft pages leave rotation. No measured human-memory benefit or autonomous semantic grading guarantee follows.

### Routes

#### MEM-RTE-query-fileback
Label: Explicit wiki query and approved file-back

Trigger/owner: user question under wiki-ask → foreground model invokes index/search → reads candidate pages and cited raw files → answers → asks whether to save → files a useful approved answer and runs bookkeeping/checks. Natural-language synthesis is model work; human approval is a requested per-answer gate, unlike routine warm save. Compared with [RT-RTE-warm-save](runtime.md#rt-rte-warm-save), distinct entry point, knowledge selection and approval rule. SRC-1, `skill/wiki-ask.md`.

- implementation conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: grounded answer with citations, then file-back/check summary if approved.
- Later read-back: accepted page becomes ordinary wiki input for later search, context and maintenance.
- Delegated visibility: procedure requires inline search/synthesis, no subagents; host execution is unobserved.
- Selection predicate: explicit question/keywords, candidate page reads and raw citation tracing; only reusable supported answers should be proposed.
- Invalidation or expiry: no-match should yield no basis; contradictions shown; category-specific draft status and later ordinary wiki currency apply.
- Activation or effect: approved file-back can add a page/log/index entry; actual human approval and model compliance are unobserved.
- Evidence limits: natural-language protocol, not an intercept on every host file write; no task-success evidence.

Admission: model proposes useful answer/page; user can veto saving. Judgment-type content remains draft/human-confirm, factual synthesis may be stable. Guidance is conventions, wiki/raw evidence and ask procedure; no expected-answer oracle for synthesis. Operating mode is an explicit open question, not an experiment. Unsupported answers should be declined, prior pages generally not overwritten; rollback of host edits is not enforced by this skill.

> **Propose file-back (human confirm)**: if the answer has reuse value, ask the user "save this to the wiki?" and on approval:
> --- `skill/wiki-ask.md`

#### MEM-RTE-topic-merge
Label: Optional generative topic consolidation

Trigger/owner: CLI consolidate → transcripts with bytes beyond independent consolidation offsets → source parser/extract and bounded existing-topic context → optional WRITE → added-claim VERIFY/grounding → topic replacement/new page → index/references/lint/log and offset. Engine owns execution, optional model proposes destination/content and verifier signal. Different from [RT-RTE-auto-update](runtime.md#rt-rte-auto-update): living-topic replacement and independent offsets, not new log-page publication. SRC-1, `src/engine/consolidate.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: per-transcript topic/merge/verdict/dry-run/grounding data, including overlap audit information.
- Later read-back: topic page is consumed by later consolidation and wiki retrieval; independent offset suppresses repeated processing.
- Delegated visibility: WRITE sees screened extract plus up to 24 existing topic bodies capped at 1,200 characters each; VERIFY sees screened extract and added claims, not the whole history.
- Selection predicate: raw bytes since independent offset, selected source adapter; model picks durable topic and an eligible merge target; only added claim lines face VERIFY and grounding.
- Invalidation or expiry: committed no-topic/no-new-claim/rejection advances consolidation offset; raw source may still permit deliberate reprocessing. Existing topic knowledge follows normal retirement/currency controls.
- Activation or effect: commit writes topic before lint; a failed new-page lint removes that new page, but the inspected failed-merge branch does not restore oldContent.
- Evidence limits: no execution or claim-fidelity proof; default deterministic path grounding is advisory. Separate calls do not establish different model identities. Old claims can disappear without being part of added-claim verification.

Admission: model drafts and selects merge; exact verifier token, enabled grounding strictness and post-write lint govern acceptance. Human per-content approval is not in this engine path. Guidance is transcript-grounded topic synthesis, added-claim checking and existing-page context; existing text is not an answer oracle. Mode is open-ended pending-source processing, dry-run by default. Rejects omit/advance offset; recovery differs for new versus merged pages. This counterexample prevents a universal no-loss or all-rejects-roll-back claim.

> const added = addedClaims(oldContent, page);
> --- `src/engine/consolidate.ts`

> if (!merging) removeRepoFile(root, destRel); // roll back through the boundary
> --- `src/engine/consolidate.ts`

#### MEM-RTE-feedback-fold
Label: Version-bound feedback to future selection

Trigger/owner: explicit session close-out supplies injected-feedback judgments → engine validates exact emitted page/version/channel → immutable receipt → aggregate rebuild → later cold/turn selectors and rule-currency checks. Separate explicit legacy refresh can fold emission/read traces, but automatic daemon transcript scanning is disabled. No counterpart route was supplied; this changes selection inputs to [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery) and [RT-RTE-edit-rules](runtime.md#rt-rte-edit-rules), not their identities. SRC-1, `src/engine/injected-feedback.ts`, `src/engine/affinity.ts`, `src/engine/reported-wrong.ts`, `skill/ref/work-feedback.md`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: receipt path/duplicate result or rejection; later explicit recheck can return a resolution receipt.
- Later read-back: aggregate counts can reorder eligible pages; wrong markers remove positive affinity and withhold rules until current evidence is acknowledged. Receipts retain evidence prose for explicit recheck readers.
- Delegated visibility: no worker launched by recording/folding; foreground protocol forbids another model/session scan for these bounded warm cases.
- Selection predicate: exact session emission membership and page hash/channel; used/irrelevant feedback contributes only for matching current page versions, excluding edit_rules ranking. Thirty-day evidence window and minimum multi-session/day thresholds limit influence.
- Invalidation or expiry: immutable receipts; page hash/mtime changes invalidate ranking evidence, stale aggregates ignored, changed raw verification evidence reopens warning. Pending wrong-version markers are hash-bound.
- Activation or effect: deterministic aggregate publication can alter future near-tie ranking and eligibility; no observed model behavioral activation or improved task capacity.
- Evidence limits: self-assessment and read-open counts are not independent truth/benefit oracles. Hashes attest revision identity, not semantic correctness. Legacy read scanning is explicit capability, not a running default daemon learner.

Admission: caller supplies judgments/reasons, normally foreground model under skill; code rejects non-emitted versions, malformed/duplicate judgments and replacement of immutable session history. Starting save is not human per-judgment approval. `wrong` needs explicit verification plus one to eight raw evidence paths to close recheck; code binds page/evidence revisions but does not adjudicate truth. Proposed change is selector metadata, not page prose or weights. Operating mode is bounded task self-assessment; guidance requests witnessed usage, sourced contradiction, and unknown when uncertain. No expected-answer oracle. No-content-change replays are idempotent; history is not silently overwritten.

> throw new Error("page version was not emitted in this session");
> --- `src/engine/injected-feedback.ts`

> // Automatic transcript consumption is disabled. Explicit injected-feedback writes its own
> // aggregate during /wiki-save; legacy read scans remain available only to explicit callers.
> if (!sourcesFor) return out;
> --- `src/engine/affinity.ts`

This raw-to-derived-to-later-selector chain qualifies as trace-fed adaptation of retrieval metadata, not demonstrated learning. Original inputs mix task-local human/model activity, tool outcomes and model-authored judgments; legacy scan input is recorded host read activity. Reasons are not reinterpreted on the hot path. `adjustedScore` caps the score shift below one point; current-prompt eligibility remains necessary before affinity ordering. Cold-start list adjustment is relevant only when those lists are emitted; slim OKF cold-start substitutes a listing pointer.

#### MEM-RTE-freshness-recheck
Label: Explicit source freshness acknowledgement

Trigger/owner: caller requests precise page/dependency snapshot → warm verifier inspects current evidence → supplies snapshot plus verifiedBy/evidence → code rechecks revisions and graph → stores verification receipt and clears stale_since. Distinct from supplied deep orchestration and context consumption; an admission path for changed access metadata, not automatic page repair. SRC-1, `src/engine/source-freshness.ts`, `skill/ref/work-feedback.md`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: current snapshot or acknowledgement receipt/cleared flag; stale or mismatching input is rejected.
- Later read-back: sourceChangedPages reads stale_since to influence future rule/prose handling; receipt remains in freshness_verifications.
- Delegated visibility: inapplicable — this API does not schedule a verifier or delegate its context.
- Selection predicate: explicit wiki page; current reference graph, matching page/dependency disk/index hashes, exact snapshot and non-empty verifier/evidence strings.
- Invalidation or expiry: dependency/page/graph mismatch refuses acknowledgement; later indexed dependency changes can mark stale again.
- Activation or effect: clears a read-time warning/withholding signal without rewriting claims; it records caller attestation, not verified truth.
- Evidence limits: generic caller identity does not prove human decision or that verification was actually performed. Transcript virtual pointers are excluded from dependency verification.

Admission: human or model verifier contribution is caller-dependent; software controls revision matching, not semantic judgment. No answer oracle; mode is explicit page recheck. Veto is mismatch/error or caller declining incomplete verification. Guidance requests current raw verification and relevant checks before acknowledgement. Recovery is prepare a fresh snapshot; provenance receipt remains, while text revision is separate.

> db.run("INSERT INTO freshness_verifications (receipt) VALUES (?)", [JSON.stringify(receipt)]);
> --- `src/engine/source-freshness.ts`

#### MEM-RTE-tier-cleanup
Label: Reversible lifecycle tier cleanup

Trigger/owner: explicit wiki-clean plan/commit → deterministic classification → automatic tier writes and ambiguous review queue → human answers accepted IDs → apply checks current hashes and consumes review file. Different from broad [RT-RTE-deep-maintenance](runtime.md#rt-rte-deep-maintenance): concrete reversible access-tier mutation, not semantic rewriting. SRC-1, `src/engine/wiki-clean.ts`, `src/engine/tiering.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: automatic/ambiguous/protected plan, projected bytes and optional review path; apply returns accepted IDs.
- Later read-back: cold-tier pages remain searchable by identity/tags/keywords but body excerpts are hidden; no page-body deletion is shown by tiering.
- Delegated visibility: inapplicable — no model worker is launched by this deterministic plan/apply path.
- Selection predicate: page age/status/category, configured L0/overview/log, queue, direction/decision, conflict, dirty tree and incoming protected/hot links; ambiguous cases remain warm candidates for human decision.
- Invalidation or expiry: review application requires matching current page hashes; automatic tier can later be changed. Source text remains on disk for explicit Read.
- Activation or effect: writes tier frontmatter and reindexes; rejected IDs stay unchanged; accepted review is removed after application.
- Evidence limits: no measured savings, semantic truth or global context eviction follows. Reviewed human-answer format does not authenticate who edited the file.

Admission: code classifies automatic changes, human policy selects ambiguous IDs, engine validates format/hash and applies. Direction/decision/draft/conflict pages are protected; age alone does not cool all knowledge. Eligible old milestone/insight/lesson or superseded pages can cool after 180 days. Operating mode is explicit maintenance; no answer oracle. Guidance is fixed lifecycle policy; changes are reversible-tier-only, not model-derived criticism of page truth.

> "Accept only IDs whose proposed tier is appropriate. Rejected IDs stay unchanged.",
> --- `src/engine/wiki-clean.ts`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-warm-save](runtime.md#rt-rte-warm-save)

Memory lineage: served extraction snapshots are screened/parsed derivatives, not verbatim full transcripts; supplied runtime establishes grouped user/assistant conclusions, omitted sidechain/compact rows and separate draft summary. Later authors are instructed to ground in extracts, not the harness summary. The changed durable products are wiki knowledge and L0; raw transcripts and processing metadata have separate rollback/retention. Sequential page issuance is not semantic reading or admission. Host model authors and admits routine content; human review is reserved for direction/conflict policy. These distinctions are supported by the supplied quotations and progression, not a new execution claim.

#### On [RT-RTE-auto-update](runtime.md#rt-rte-auto-update)

Alternative acquisition: direct inspection of SRC-1, `src/engine/ingest.ts` establishes that ingest enqueues an arbitrary source using inferred/forced adapter kind, optionally resets the canonical queue watermark to zero, then invokes updateOne with dry-run/commit. It is not restricted to prior daemon-discovered coding sessions. Caller selection of input/destination does not establish human approval of every generated claim. Provenance may therefore be dropped text, not only session experience. Accepted page authority and rejection semantics remain those of the supplied route.

> const result = await updateOne(ws, path, !!opts.commit);
> --- `src/engine/ingest.ts`

#### On [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery)

Direct SRC-1 reads of `src/engine/context.ts`, `src/engine/turncontext.ts` and `src/engine/page-rank.ts` establish these memory-specific selection details. Cold current-state/overview is high-priority reference data, not necessarily a hard-truncated body. Full mode can show six recent and four spine pointers; slim OKF mode replaces both with the generated listing pointer. Human-review titles have an explicit budget exception. Thus cold-start is not uniformly bounded by the turn budget.

Turn push selects current checkout pages through deterministic lexical rarity/frequency/identity/trigger scoring, not a dense embedding retrieval model. The selector gates on current-prompt coverage/relevance before accumulated-term/affinity ordering, deduplicates previously suggested pages, then takes at most three. The shared character allowance is 1,600 including save-nudge reserve; first/rest excerpt caps are 700/400 with conditional allocation. Actual body delivery can be smaller or absent. Pointer-only is an alternative checkpoint/display form, not proof of a subsequent page Read.

> pages = pages.slice(0, MAX_PAGES);
> --- `src/engine/turncontext.ts`

> if (FOOTNOTE_DEF.test(raw) || EVIDENCE.test(raw) || /^[ \t]*<!--.*-->[ \t]*$/.test(raw)) continue;
> --- `src/engine/turncontext.ts`

The selected body transformation removes provenance definitions/evidence lines, cleans formatting and chooses bounded sections/atomic blocks. It does not deliver complete retained rationale or source excerpts. Current-page plain Read or wiki-ask raw tracing can reload omitted detail; that reload is requested work, not guaranteed from injection.

Working-context state is disposable OS-temp JSON per session/repository. It retains `seen` paths plus a term→weight map, not past turns or their reasons. Code decays prior terms by 0.5, drops below 0.25, stores at most 24 and carries at most four not already current. Loss of the file repeats suggestions/loses carry, not page knowledge. This is retained within-session selector memory, distinct from the durable cross-session wiki.

> return join(tmpdir(), `llmwiki-turnctx-${h}.json`);
> --- `src/engine/turncontext.ts`

Host turn accumulation, host compaction and provider caches remain external. llmwiki selectively supplies material; it does not implement whole-host-window garbage collection. Save's scratchpad-return delegation is a host-dependent frame-like protocol: selected input can stay in a worker, only a path returns, and a later Read loads content by value. A returned path is not a live reference whose reachability controls eviction. No automatic llmwiki host-summary replacement path is established by these inspected selectors.

#### On [RT-RTE-deep-maintenance](runtime.md#rt-rte-deep-maintenance)

Direct SRC-1, `src/engine/distill.ts`, `skill/ref/distill.md`: the pre-distill page snapshot is an explicit recovery artifact, distinct from raw cited transcripts and the later reconstructed topic. The deterministic gate checks source-set inclusion and conflict-line survival, not complete preservation of claims, reasons or claim-to-citation attachment. The foreground model must compare against snapshot; snapshot retention lasts until the page is committed under the procedure. Alternative topic merging is separately traced in [MEM-RTE-topic-merge](#mem-rte-topic-merge).

> ok: droppedSources.length === 0 && droppedConflicts.length === 0,
> --- `src/engine/distill.ts`

## Write side

Acquisition and admission differ. Passive daemon enqueue is a source-availability decision; exact manual save can admit a short session that passive capture skips. Ingest admits an explicitly selected arbitrary file to the same optional generation path. None means a human approved the resulting page. Foreground save chooses useful claims and admits routine content under policy; direction review records a human answer and only then moves the draft, as specified by SRC-1, `skill/ref/review-item.md` and [RT-RTE-warm-save](runtime.md#rt-rte-warm-save).

> On confirmation the recorded `1_direction/` page stamps `verified: { by: human:<owner login>, at: <ISO now> }` — the human's answer is the verification; a model's own confirmation never is.
> --- `skill/ref/review-item.md`

Wiki-ask imposes a separate proposed-answer saving approval. Autoupdate and consolidation instead use model proposals plus software/model checks; their commit flag is publication authority, not semantic human approval. These write routes preserve source citations/provenance but not necessarily the model's deliberation. Supplied autoupdate attaches evidence excerpts for ordinary pages; consolidation preserves old sources/verified metadata as history even when content changes. Therefore a human verification stamp alone is not proof of a newly verified successor.

Maintenance revises readable knowledge, not weights. Distillation has snapshot/citation/conflict controls; topic merge has added-claim verification and asymmetric rollback. Session review imports bounded criticisms but does not itself apply them. Source freshness acknowledgement changes access metadata, injected feedback changes selection/eligibility, work-feedback records diagnostics, and quiz-record changes a human schedule. These mechanisms have different authors, admission gates, persistence and later consumers and cannot be collapsed into one autonomous self-improvement loop.

Withdrawal is also plural: retirement suppresses automatic turn candidates while explicit lookup can retain marked historical records; cold tier hides bodies from automatic excerpts without deleting source pages; source-changed/wrong markers withhold rules and warn ordinary prose. Autoupdate rejects can advance skipped offsets without retaining candidate pages; consolidation rejects can advance separate offsets. Capture prune preserves lost tombstones but can expire engine-owned raw export bodies. A raw-source citation can outlive evidence availability; no universal replay/reconstruction guarantee follows.

## Read-back

The main unsolicited path is host event → deterministic selector → bounded text/context envelope → later host invocation. That is read-back of accumulated wiki knowledge. Host event triggers and delivery channels are established by [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery) and [RT-RTE-edit-rules](runtime.md#rt-rte-edit-rules); [RT-BAP-wiki-context](runtime.md#rt-bap-wiki-context) supplies consumer/force/horizon without a duplicate declaration here. Rule text is behavior-guiding, ordinary page text is reference data, and one-time edit denial is a symbolic interruption rather than compliance proof.

Requested paths are wiki-ask search/read/raw verification, explicit page/source reads, consolidation/review input, feedback replay, and quiz authoring. An index record or storage API alone is not a read-back route: the traced caller/consumer matters. Emission metadata records selected output identities but cannot reconstruct exact historical text. Feedback hot paths consume compact aggregates rather than the full feedback reasons; semantic maintenance must deliberately read the retained evidence. Quiz consumes retained results as scheduling metadata and human-facing study content, not as model knowledge training data.

No observed trace establishes that delivered text changed a later coding action or improved task capacity. Lexical/numeric access metadata and natural-language knowledge can both shape future context without distributed-parametric updates. That architectural possibility is narrower than demonstrated learning, reliable self-correction or successful self-improvement.

## Integration issues

- **Recall partition repaired:** [MEM-OBJ-recall-triggers](#mem-obj-recall-triggers) declares the lexical-selection part of [MEM-OBJ-wiki-rules](#mem-obj-wiki-rules), preserving that extension container. SRC-1 `src/engine/page-rank.ts` constructs triggers from rule plus recall independently of excerpt delivery; `src/engine/turncontext.ts` ranks before imperative withholding. Object-level comparison must distinguish retrieval-trigger authority from rule authority, including when the same rule string feeds both. This is containment, not a proposed duplicate or supersession.
- **Alternate per-turn channels remain a coverage limit:** [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery) includes commit and absence channels. This correction does not independently inventory their retained parts or evaluator domains in `src/engine/commit-context.ts` and `src/engine/absent-subject.ts`. Complete read-back-source and negative-claim-evaluator coverage is prevented. In particular, do not infer that a lexical absence result proves a subject never occurred in the project's full history, or that all turn content derives from accepted wiki pages.

- **Capture cleanup precision:** supplied [RT-RTE-passive-capture](runtime.md#rt-rte-passive-capture) mentions pruning lost/dead rows without internal detail. [MEM-OBJ-capture-state](#mem-obj-capture-state) refines this: ordinary aged missing pending sources are tombstoned lost; expiring OpenCode body exports have a distinct removal path. Reconciliation should not paraphrase all cleanup as deletion or all raw evidence as permanent.
- **Topic no-loss/recovery boundary:** [MEM-RTE-topic-merge](#mem-rte-topic-merge) adds an alternate write path to [RT-RTE-deep-maintenance](runtime.md#rt-rte-deep-maintenance). Added-claim checks do not verify disappearance of old claims, and failed merged-page lint does not restore oldContent in the inspected branch. Do not generalize distill's snapshot/no-loss protocol to all topic replacement.
- **Derived-index label:** [MEM-OBJ-wiki-index](#mem-obj-wiki-index) qualifies SRC-1 `src/engine/schema.sql`'s all-derived claim using transcript registrations and freshness_verifications. Reconstruction of every receipt/provenance pointer from Markdown alone is unresolved; prevents a blanket delete-and-fully-recover assertion.
- **Default legacy adaptation is not active:** [MEM-RTE-feedback-fold](#mem-rte-feedback-fold) distinguishes explicit legacy read scans from actual daemon invocation with no sourcesFor. Documentation/comments describing daily passive refresh are broader than the early-return implementation. No supplied runtime record needs withdrawal, but any later account of automatic trace learning must retain this distinction.
- **Review application and remaining maintenance:** [MEM-OBJ-review-reports](#mem-obj-review-reports) is an input/product within supplied deep orchestration, not a duplicate route. Full legacy report publication, gaps/overview transformations, DB maintenance, export and migration details remain partially inspected as the coverage table states. Complete semantic repair/retention conclusions are prevented; supported review preparation/import and selector findings remain.
- **Wrong-version scope:** [MEM-OBJ-usage-affinity](#mem-obj-usage-affinity) markers are version-bound; changed pages can differ from the originally reported wrong version while a recheck item remains open. Reconciliation should not equate an open queue item with permanent blocking of every future page version. Explicit resolution still requires current page/raw evidence hashes.

No new declaration is intended to duplicate a supplied record: objects add previously undeclared retained parts; routes add different entry/admission/transformation identities; supplied routes receive annotations. External host/provider behavior and actual model compliance remain unresolved evidence limits, not absences.

## Limitations and checks

Checkout HEAD was rechecked as e6be788bdfd969c3695f839a5d6b5752bb233cfc and Git status was clean before source inspection. All source reads/searches were read-only under SRC-1. Required prompt, job, type, worker and records inputs were read in bounded batches; no prior characterization or target execution was used. Additional direct scope is recorded in the coverage table. This report retains uninspected internals rather than inventing complete enumeration or inferring absence from omitted mechanisms.

Validation: the required role-specific content validator passed for this corrected report. Form/quote occurrence validation does not establish semantic truth, host deployment, causal activation or benefit. The correction round rechecked the frozen checkout identity and clean status, then directly inspected the recall/trigger projection, eligibility predicate and turn selection/excerpt code. Unrelated findings and their carried limits are retained from the supplied previous report.
