---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Cortexes runtime baseline: Claude Code lifecycle capture, bounded Raw review, human-admitted vault changes and hybrid retrieval."
run-id: AAS-2026-11-08-cortexes-af94078f2405-01
reviewed-boundary: "2b8e79f0099203e0453147b708346349952bb963"
---

# Cortexes runtime report

## Runtime account

Cortexes is a Claude Code plugin plus a Python CLI, not an enclosing agent executor. The host owns foreground model calls, tools, permissions, transcripts and lifecycle delivery. Cortexes supplies lifecycle shell programs, a host UI module, model-followed procedures and indexing/review commands. The ordinary loop is: initialize a vault; work in the host; capture a session into Raw; review selected Raw passages; obtain human decisions; write and index Notes/Projects; retrieve those pages in a later host session. Initialization and direct saves also admit material without distillation. SRC-1, `commands/genesis.md`, `hooks/hooks.json`, `skills/cortex-evolve/SKILL.md`, `skills/cortex-distill/SKILL.md`, `skills/cortex-query/SKILL.md`.

This report adds implementation inspection of the filter's exception/forwarding branches, deck callbacks, takeoff helper, CLI dispatcher, store, fusion, reranker and map/span/plan consumers, and doctrine/design inspection of command and maintenance procedures, all under SRC-1 at the frozen revision. No target program, test, provider or example was executed. Wiring and requested behavior below are not observed operation, reliable model adherence or demonstrated benefit. Provider/host internals, actual grants, real vault contents and deployed isolation remain uninspected.

### Ordinary invocation and return

A configured interactive host session triggers [RT-RTE-session-start](#rt-rte-session-start). The shell receives host JSON, determines repo and vault, emits topic names and menu instructions, and writes session-keyed deck data. A person may select retrieval, recent records, pending distillation or a baton. The deck can convert the menu into UI instead of model context; it submits whole action prompts as user input. Foreground next steps are selected by the host model interpreting the skill, not by a Cortexes executable agent scheduler.

On session exit, [RT-RTE-session-capture](#rt-rte-session-capture) receives transcript path and cwd, applies eligibility guards, detaches a writer, filters the transcript and publishes a dated Raw Markdown file. Optional classifier work runs in a separate CLI invocation, not a delegated foreground task. Automatic capture is not per-record human approval. Optional commits/pushes persist and distribute the result; failures can leave local-only data. A later explicit distillation follows [RT-RTE-distill-review](#rt-rte-distill-review), whose machine ledger limits returned Raw material and whose skill requires human verdict and draft approval. A new note is upserted, indexed and committed; a pending merge writes no new page. Eligible outcomes dispatch broadcast inline, but [RT-RTE-broadcast-edit](#rt-rte-broadcast-edit) still requires target selection and conversational approval of changes. The loop returns through [RT-RTE-vault-search](#rt-rte-vault-search): JSON hits first, a chosen page's body later. Batons offer a distinct, ephemeral continuation route, [RT-RTE-takeoff-handoff](#rt-rte-takeoff-handoff).

### Control coverage and forcing cases

1. **Preserve a record versus redact it.** Filter failures generally preserve the nearest available text; classifier errors keep a block. The same preference means an exception in whole-body redaction emits the unredacted body with an audit counter. This is a reachable implementation fallback, not a demonstrated runtime leak. Classification also receives a text prefix before final whole-body redaction. Consequently neither preservation nor regex redaction warrants a universal no-secret-egress guarantee. Owner: capture filter; strength: best effort; implementation conclusion status: wired; operation conclusion status: uninspected. Capture-path evidence is retained in [RT-RTE-session-capture](#rt-rte-session-capture).

2. **Bounded review versus unrestricted file access.** Map/span code enforces emitted-page and ledger budgets, identity checks and a coverage condition for sealing `no-insight`. It does not prove the model read or understood emitted text, approved a draft with a human, or refrained from using Read/Bash directly. CLI `--new-session` resets accounting on request; no host-session attestation was found in that function. The skill's “never full Read” and human-confirmation conditions are policies. Owner: plan/page code for API checks, foreground agent/human for admission; strengths: invariant on the named API checks, policy on the surrounding procedure; implementation conclusion status: wired; operation conclusion status: uninspected. See [RT-RTE-distill-review](#rt-rte-distill-review).

3. **Filtered retrieval versus alternative reads.** CLI repo scoping deliberately keeps Notes cross-repo. `where` reaches vector, BM25 and graph consumers, while reranking only reorders existing candidates. A repo filter is not tenant isolation; direct grep and page Read are separate host-controlled routes. Disabled/failed vectors still allow BM25, and returned `score: 0.0` can mean missing cosine rather than irrelevance. Distill/broadcast prose that says every hit has a measured cosine is too strong for these supported modes. The query skill already explains that ambiguity. Owner: store/fusion and host for file tools; strength: protocol, not deployment guarantee; implementation conclusion status: wired; operation conclusion status: uninspected. See [RT-RTE-vault-search](#rt-rte-vault-search).

4. **Baton preflight versus actual write.** The helper refuses prepare unless the target is Git-ignored and clear unless ownership matches, except explicit `--force` or missing legacy workdir. It returns a path; the model then writes via a different host tool. `path` returns a pathname without prepare's check. Thus the preflight is not a filesystem reference monitor or a universal non-commit guarantee. Resume is prescribed full-text loading without deletion. See [RT-RTE-takeoff-handoff](#rt-rte-takeoff-handoff).

Cortexes' capability surface includes shell, host Read/Write/Edit, Git and network-backed provider calls. The query command declares only scoped read-oriented shell approvals, whereas genesis declares general Bash and file-writing tools. These declarations do not establish the actual session grant set. The hook's detached subprocess and provider clients are material alternate execution paths; no Cortexes-owned sandbox is established by their existence. Plugin installation, host callbacks and external permissions are required contracts, not internally enforced isolation. SRC-1, `commands/query.md`, `commands/genesis.md`, `hooks/deck.tsx`, `hooks/scripts/session-end-record.sh`, `cortex-vec/src/cortex_vec/store.py`.

The selected forcing cases cover critical return/copy/fallback paths rather than every filter or host configuration. Specific TOML/command filters, all host approval semantics, deployed concurrent writers and real retrieval quality remain unobserved; no universal reliability or performance conclusion follows. The Python CLI lazily avoids the store import for queue/navigation commands, but its source timing comments are not measurements made in this run (SRC-1, `cortex-vec/src/cortex_vec/cli.py`). Memory revisions and detailed retained-object inventories belong to the memory member.

## Shared records

### Components

#### RT-CMP-claude-code
Label: Foreground host model

SRC-1, `hooks/hooks.json`, `skills/cortex-distill/SKILL.md`, `commands/query.md`. The source-native host is Claude Code; the model is a distributed-parametric external component. Its parameters reside in opaque provider infrastructure, not this repository. Exact foreground version, parameter changes during operation and endpoint routing are uninspected. The plugin supplies natural-language procedures and symbolic hook/command metadata to the host. It neither pins host weights nor implements their training. Current-run state and tool execution are host-owned.

> Invoke the `cortexes:cortex-query` skill and follow it for the actual search.
> --- `commands/query.md`

#### RT-CMP-sonnet
Label: Residue classifier

SRC-1, `hooks/scripts/filter-transcript.py`. Distributed-parametric Claude endpoint, invoked by subprocess with alias `sonnet`. No parameter update is wired in the inspected invocation. Exact weights are not pinned; an alias may resolve to a changed model. Provider parameter storage and internal mutation remain opaque. Local prompt and `log`/`content` parser are natural-language input and symbolic control respectively, not model weights.

> ["claude", "-p", "--model", "sonnet",
>              "--no-session-persistence", CLASSIFIER_PROMPT],
> --- `hooks/scripts/filter-transcript.py`

#### RT-CMP-embedding-model
Label: OpenAI embedding model

SRC-1, `cortex-vec/src/cortex_vec/store.py`. `text-embedding-3-small` is the distributed-parametric service behind Chroma's embedding function. Provider stores the parameters; local Chroma persists resulting numerical embeddings. The code requests embeddings, not updates to model parameters. The identifier is named but not an immutable weights revision; mutable service resolution is possible, and provider internals remain uninspected.

> EMBEDDING_MODEL = "text-embedding-3-small"
> --- `cortex-vec/src/cortex_vec/store.py`

#### RT-CMP-summary-model
Label: Bilingual summary model

SRC-1, `cortex-vec/src/cortex_vec/config.py`, `cortex-vec/src/cortex_vec/store.py`. Distributed-parametric OpenAI chat model identified as `gpt-5.4-mini`, with opaque provider-side weights. No update of those parameters is wired. The name is not an immutable snapshot and may resolve differently over time. Title/tags and the first 3000 body characters become a natural-language request; returned text, or title/tags on failure, becomes summary-index content. This does not establish faithful summarization.

> SUMMARY_MODEL = "gpt-5.4-mini"
> --- `cortex-vec/src/cortex_vec/config.py`

#### RT-CMP-rerank-model
Label: Optional reranking model

SRC-1, `cortex-vec/src/cortex_vec/config.py`, `cortex-vec/src/cortex_vec/rerank.py`. Separately configured distributed-parametric OpenAI model, default `gpt-5.4-mini`. Provider storage and training are opaque; no in-operation parameter-update path is wired here. Exact weights are not pinned and configuration can select another endpoint/model. This is a separate call role from summary production even when names coincide. Query, titles and summaries are natural-language inputs; parsed numerical scores only reorder candidates.

> "rerank_model": "gpt-5.4-mini",
> --- `cortex-vec/src/cortex_vec/config.py`

### Operative objects

none declared in this member

### Routes

#### RT-RTE-session-start
Label: Session initialization and deck delivery

SRC-1, `hooks/hooks.json`, `hooks/scripts/session-start-inject.sh`, `hooks/deck.tsx`. Trigger/principal: host SessionStart JSON. Shell resolves environment override before config, requires vault/cwd/repo, reads top-level topic names, pending baton summaries and unpushed-count metadata. It emits `additionalContext` plus a session-keyed JSON file written via rename. The deck watches that file and can cut the menu only from hook-context messages; failure forwards the original row. Code owns rendering and prompt submission; person owns action selection; the foreground host owns subsequent execution. Metadata and instructions are mixed symbolic/natural-language content, stored temporarily on local disk and host atoms. Context-window measurement can offer a handoff at 70% without performing it. External contract: compatible Claude Code module events, filesystem access and session identity. Strength: best effort for UI substitution, policy for prompt-followed menu/opt-out behavior.

- Immediate return: Host receives topic names, vault/repo metadata and routing instructions; compatible deck UI receives action prompts.
- Later read-back: Pending batons are represented by previews; their full bodies are loaded only through the chosen resume flow.
- Delegated visibility: inapplicable — this route creates no delegated agent; the UI submits an action as user input.
- Selection predicate: Valid configured vault and repo; top-level Notes/Projects topic names and repo-scoped batons.
- Invalidation or expiry: SessionEnd removes the session deck file; start opportunistically removes old deck files; stamp prevents duplicate reception.
- Activation or effect: Wired context/menu delivery and UI prompt submission; opt-out adherence remains requested behavior.
- Evidence limits: Host callback execution and actual user/model actions are unobserved. Environment override here can differ from the config-only write/search side.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> await $.prompt.submit({ text: prompt, asUser: true })
> --- `hooks/deck.tsx`

> if (found === null) return next(e)
> --- `hooks/deck.tsx`

#### RT-RTE-session-capture
Label: SessionEnd transcript capture

SRC-1, `hooks/scripts/session-end-record.sh`, `hooks/scripts/filter-transcript.py`. Trigger: host end event. Recursion/skip guards, recognized headless entrypoint unless forced, minimum transcript size and config-only vault resolution precede a detached writer. Shell owns I/O, filter code owns deterministic reductions, [RT-CMP-sonnet](#rt-cmp-sonnet) chooses preservation strategy for selected residue. Raw is Markdown derived from host transcript JSONL; state includes audit counters, matched tool metadata and filter results. Task output is forwarded verbatim by the filter; known MCP/Bash handlers can return before generic classification. Other sufficiently large user/tool residue receives at most five classifier calls, each with an 8 KiB prefix and 20-second subprocess timeout; disabled/error/unrecognized verdict returns `content`. Successful `log` decisions deduplicate or sample. Final body passes scrub, normalization and redaction attempts.

Change admission is automatic software admission into Raw, not human content approval. The external transcript and classifier prompt shape the result; no expected-answer oracle checks preservation. Operating mode: lifecycle capture of open-ended work. Terminal filter failure writes a recognizable stub with transcript pointer and redacted diagnostic logging; whole-body redaction failure instead preserves body and records an audit error. The writer prefers rename but falls back to copying the temp file, so atomic publication is not unconditional. Metadata-only maintenance recognition may append a processed marker; reclaim may remove superseded captures. Configured Git actions are path-scoped for capture and reclaimed files; push failure is logged and can be surfaced at next start. Recovery includes original transcript, logs and Git where retained; successful recovery is unobserved.

- Immediate return: Hook exits after detaching; no synchronous proof that a complete Raw, commit or push exists.
- Later read-back: Published Raw becomes queue input for distillation/broadcast and archive search; transcript pointer supports potential recovery.
- Delegated visibility: Nested CLI classifier receives only selected block prefix and fixed classification instruction; only its one-word verdict crosses back, not a foreground subagent context.
- Selection predicate: Eligibility guards above; Task passthrough and known command/MCP filters precede size-based classification.
- Invalidation or expiry: Raw persists until maintenance/user removal; filter temporary files are trapped for cleanup; classifier has no session persistence requested.
- Activation or effect: Creates Raw and optional processed marker, staged deletion, local commit and remote push; no later behavioral dependence demonstrated.
- Evidence limits: No capture trace. Regex redaction is not comprehensive secret detection; final redaction exceptions preserve unredacted text, and classifier input precedes that final pass.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if name == "Task":
>         return raw_output
> --- `hooks/scripts/filter-transcript.py`

> except Exception:
>         # Emitting an unredacted body is a real cost, not a free fallback; it
>         # is still the lesser one, because the alternative destroys the record
>         # AND leaves the secret in the transcript. body_errors>0 with
>         # redactions=0 is the signal to scan this Raw by hand.
>         body_errors += 1
>         redactions = 0
> --- `hooks/scripts/filter-transcript.py`

> mv -f "$tmp_raw" "$target_file" 2>/dev/null \
>     || cat "$tmp_raw" > "$target_file" 2>/dev/null \
>     || true
> --- `hooks/scripts/session-end-record.sh`

#### RT-RTE-vault-search
Label: Hybrid search and chosen-page retrieval

SRC-1, `commands/query.md`, `skills/cortex-query/SKILL.md`, `cortex-vec/src/cortex_vec/cli.py`, `cortex-vec/src/cortex_vec/store.py`, `cortex-vec/src/cortex_vec/fusion.py`, `cortex-vec/src/cortex_vec/bm25.py`, `cortex-vec/src/cortex_vec/rerank.py`. User query or prescribed prior-context signal triggers host skill routing. Query command explicitly invokes the skill and preserves supplied query text. Host detects repo and launches CLI; CLI owns parsing, store health check and `where` construction. Symbolic ranking combines vector/BM25 streams via weighted reciprocal rank fusion, optional graph neighbors and diversification; optional model rerank reorders a candidate window. Foreground model interprets returned JSON then asks which page to read. No answer oracle establishes factual correctness or relevance; model judgments and retrieval scores are selectors, not truth checks. Operating mode: open queries.

Repo filtering means `(repo match OR note)` combined with requested type/category. Vector receives `where`, BM25 evaluates the same boolean shape against repo membership lists, graph rejects metadata-less candidates when filtered and applies BM25's matcher. Backfill asks for cosine for missing selected IDs; exceptions are swallowed and scores default to zero. Reranker indexes into existing results, returns original order on failure and cannot add a new document. These are implemented selector controls, not host file-read restrictions. Command's scoped Bash approval metadata and fallback workspace discussion remain host contracts. Missing BM25 index causes setup error unless BM25 is disabled; missing API key can degrade to BM25, with diagnostic stderr. Exact grep over Notes/Projects is a separate fallback; Raw requires explicit archive request by policy. Full-body reading is not part of the JSON search itself.

- Immediate return: Up to requested count of JSON-line hits with metadata/summary and vector cosine field; degradation and empty-result messages go to stderr. Later chosen-page Read returns full body.
- Later read-back: Persisted indexed vault content is selected by query and delivered to later host sessions; fresh filesystem grep/Read can supply content outside indexed results.
- Delegated visibility: Embedding service receives query text; reranker receives query and candidate title/summary, not the full host conversation.
- Selection predicate: Configured stream flags and weights; repo/type/category predicate; fused rank, optional rerank and result count; human chooses a full page under skill policy.
- Invalidation or expiry: Index changes through rebuild/upsert/delete; direct file edits alone do not ensure index freshness. Current result lists have no retained invocation-level expiry mechanism inspected here.
- Activation or effect: Wired retrieval and prescribed later reading; no evidence that returned content changes an actual answer.
- Evidence limits: Real relevance/latency and host permissions unobserved. `score` is not hybrid confidence; zero may mean unavailable or failed cosine backfill. Distill/broadcast's stronger every-hit scoring prose does not cover those fallback cases.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> clauses.append({"$or": [{"repo": repo}, {"type": "note"}]})
> --- `cortex-vec/src/cortex_vec/store.py`

> if missing and use_vector and os.environ.get("OPENAI_API_KEY"):
>         try:
>             vec_score.update(store.cosine_for(query, missing))
>         except (Exception, SystemExit):
>             pass  # same degradation contract as the streams: score falls to 0.0
> --- `cortex-vec/src/cortex_vec/fusion.py`

> entry["score"] = round(vec_score.get(doc_id, 0.0), 4)
> --- `cortex-vec/src/cortex_vec/fusion.py`

#### RT-RTE-distill-review
Label: Bounded Raw review and new-note admission

SRC-1, `skills/cortex-distill/SKILL.md`, `cortex-vec/src/cortex_vec/cli.py`, `cortex-vec/src/cortex_vec/raw_map.py`, `cortex-vec/src/cortex_vec/raw_span.py`, `cortex-vec/src/cortex_vec/distill_plan.py`. A user request or chosen queue action starts an interactive open-ended maintenance run. Code lists eligible Raw; the host proposes a batch; human approves plan and verdict. Plan state and coverage intervals are symbolic JSON on local disk; original Raw remains external to the window. Map previews/lexical anchors choose what to expand; span returns exact source substrings, with continuation cursors. Map/span account final emitted JSON size before returning. A ledger tracks coverage and budget, not cognition. Positive candidates can stop early; `no-insight` seal requires map and semantic/ambiguous coverage. Evidence ranges must already be reviewed.

Foreground model applies the explicit symbol/mechanism/rationale heuristic, shows excerpts and a candidate to a human, then uses search cosine thresholds as placement recommendations. Human can override verdict and choose new/pending/skip; a new draft additionally requires confirmation. There is no expected-answer oracle; excerpts and existing pages inform judgment without establishing correctness. Only new outcome writes Notes/Projects and upserts; all outcomes can write a marker/log. Skill says seal after confirmed outputs; code seal accepts expected outcome and coverage, not proof of user approval, written notes or log. Completion checks source identity and matching terminal outcome; it does not execute those writes or admission. Product revision is a model/human procedure, with Git history as recovery affordance. No automatic change of the plugin's own method or machinery is established here.

The page API is an enforcement boundary, not a ban on Read/Bash. Explicit `resume --new-session` resets used chars; it does not inspect a host session identity. A fresh session plus takeoff is prescribed on exhausted budget. All prior prompt text remains host-managed; no in-window eviction is performed by these page APIs. Their useful stack-like feature is selected inputs only, but no isolated foreground frame is popped: already-returned pages accumulate. External text remains reloadable by cursor/anchor while plan/source checks hold.

- Immediate return: Page envelopes, ledger/status/errors and prescribed user questions; terminal outcome is note or pending/skip/no-insight marker plus log/commit.
- Later read-back: New indexed notes feed query; markers govern future queue eligibility; plan state resumes partial review and baton may carry plan ID.
- Delegated visibility: inapplicable — review is foreground and inline; no fresh reviewing agent is launched by the inspected route.
- Selection predicate: Queue marker state; map cards/find anchors; model expands spans and proposes verdict; human decides; coverage gates negative sealing only.
- Invalidation or expiry: Source/file hash or schema/parser mismatch rejects page loading; seal blocks page reads; completion removes plan files; clear can abandon ledger.
- Activation or effect: Page-budget/coverage checks wired; note admission, confirmation and commits prescribed. Delivery does not prove understanding or knowledge quality.
- Evidence limits: Direct file access and manual marker edits do not pass ledger controls. No actual human review, retained-note benefit or complete review transcript supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> **Always present the candidate to the user and wait
> for confirmation**, even when the verdict feels obvious. The user's
> answer is binding regardless of the agent's tilt.
> --- `skills/cortex-distill/SKILL.md`

> if expected_outcome == "no-insight" \
>             and not status_payload(state)["no_insight_candidate_allowed"]:
>         raise PageError("NO_INSIGHT_COVERAGE_INCOMPLETE",
>                         detail=status_payload(state))
> --- `cortex-vec/src/cortex_vec/distill_plan.py`

> if new_session:
>         state["session_used_chars"] = 0
>         state["session_seq"] += 1
>         _save(state)
> --- `cortex-vec/src/cortex_vec/distill_plan.py`

#### RT-RTE-broadcast-edit
Label: Conversational existing-page revision

SRC-1, `skills/cortex-broadcast/SKILL.md`. Trigger is standalone command or automatic inline dispatch after new/pending-merge distill outcomes. Host reads bounded Raw passages and full target pages, proposes exact changes and interprets user responses. Operating mode: open conversational revision. Search thresholds suggest candidates; no-candidate new outcomes can finalize without editing, while pending-merge retains its original target even below threshold. Search failure uses the index and model judgment. Human confirms target selection and individual changes; it can reject/revise proposals or abort. Code does not mechanically enforce this conversation. Answer oracle: none established; Raw/page content and human judgment are evidence, not a reference-answer test.

Proposed changes include prose, links, summaries and explicit contradiction flags. The guidance is a method text; actual revised pages and criticism records were not supplied, so this report does not infer formulated theory revision from the generic edit mechanism. If a page contains a theory, theory-builder conditions 1–4 remain individually uninspected here: no actual whole theory unit, decision dependence, content-directed criticism with blame/revision, or retained criticism shaping another round was supplied. Addressability is afforded by exact-section before/after proposals, not demonstrated for particular theories. Persistence is prescribed page/Git state across sessions. Learning is uninspected: no improved future capacity or attribution evidence. Reflection, reflective/autonomous theory building and exercised self-improvement are unestablished by this human-mediated external-page editing path; no assumption about hidden model reasoning resolves those properties.

- Immediate return: Candidate menu and edit proposals; accepted targeted Edits, upsert and per-page commit; terminal marker/log commit.
- Later read-back: Revised pages and embeddings reach later query; flags remain at the challenged claim; terminal marker removes Raw from future eligible queue.
- Delegated visibility: Inline broadcast shares distill's already-read passages; standalone review opens its own bounded plan. Neither is prescribed as an isolated subagent.
- Selection predicate: Eligible new/pending-merge Raw, own-target exclusion for new, score threshold or model fallback, pending-target override and human toggles.
- Invalidation or expiry: `quit` leaves Raw unresolved; mid-page abort discards that page's uncommitted proposals but preserves earlier committed pages; temporary plan cleared at end/abort.
- Activation or effect: Prescribed content-specific human-approved edits and later indexing. Flags expose conflict without independently adjudicating truth.
- Evidence limits: No execution or amended page supplied; no automatic consistency, truth, improvement or rollback of all prior pages guaranteed.
- implementation conclusion status: claimed
- operation conclusion status: uninspected

> `yes` / `y` → apply to working copy
> --- `skills/cortex-broadcast/SKILL.md`

> Already-committed prior pages from this session stand.
> --- `skills/cortex-broadcast/SKILL.md`

#### RT-RTE-direct-save
Label: Initialization and user-initiated save

SRC-1, `commands/genesis.md`, `skills/cortex-evolve/SKILL.md`, `cortex-vec/src/cortex_vec/store.py`. Genesis admits config, directory structure, Git setup and a regenerated human index through host tools, asking for path/author and whether to reconfigure. It offers CLI installation and can continue without it. These are user/method-guided capability/environment changes, not automatically selected improvements. Evolve accepts a user's save request, model-selects Notes/Projects placement, writes page/index/log, commits and requests upsert. It does not perform distill dedup. Model authorship and physical file I/O are distinct from the user's initiation; the skill does not require a separate final draft confirmation as distill does. Human can clarify ambiguous type; no per-content computational truth oracle is specified. Mode: open initialization/save requests.

Store upsert parses a path, removes stale vector entries, generates body/summary entries for repo memberships, then updates BM25. Rebuild scans Notes/Projects excluding `_archive`; BM25-only is an explicit no-embedding alternative. These transformations have no separate human approval inside the CLI and no atomic transaction across file, Git, Chroma and BM25 is established. Summary failure substitutes title/tags. Git and rebuild/upsert afford recovery, but failures can leave partially updated derived state; successful recovery is unobserved.

- Immediate return: Prescribed setup/save confirmation; CLI indexing counts or errors.
- Later read-back: Config controls subsequent operations; written pages/index and derived retrieval entries feed later queries and maintenance.
- Delegated visibility: Summary provider receives title/tags and a bounded body prefix; embedding function receives indexed documents. No foreground conversation is explicitly forwarded by store.
- Selection predicate: User path/save request, model placement heuristics; rebuild scans canonical content directories, upsert takes caller path.
- Invalidation or expiry: Upsert removes stale path variants; rebuild replaces vector collection and regenerates BM25; direct file changes require explicit refresh.
- Activation or effect: Prescribed vault/setup writes; executable derived-index admission through provider generation and local I/O.
- Evidence limits: Store path argument is not evidence of human approval or comprehensive filesystem confinement. No deployment/install run or end-to-end cross-store transaction observed.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> If they decline, continue anyway — recording and the skills degrade
> gracefully — but note that semantic indexing and `cortex-vec` search stay
> unavailable until it is installed.
> --- `commands/genesis.md`

> except Exception:
>         return f"{title}. Tags: {tags}"
> --- `cortex-vec/src/cortex_vec/store.py`

#### RT-RTE-takeoff-handoff
Label: Ephemeral topic baton handoff

SRC-1, `skills/cortex-takeoff/SKILL.md`, `hooks/scripts/takeoff.sh`, `hooks/scripts/session-start-inject.sh`. User request or accepted UI reminder starts create/resume/done. Model curates a natural-language continuation note; helper derives repo/topic pathname and checks ignored status before the host Write. Existing topic is overwritten; no separate draft acceptance is prescribed. Topic announcement and refusal on helper failure are policies. A later selected resume loads full body as continuation context, keeping the baton. User completion requests clear; helper compares physical workdir, can refuse or accept explicit force, then moves to trash. Missing workdir warns rather than refuses. This is state-admission guided by the takeoff method, not model-parameter learning. No answer oracle; open handoff mode.

- Immediate return: Helper paths/workdir or errors; prescribed confirmation; resume returns full curated body to host context.
- Later read-back: Topic baton reaches later host session, independently of Raw capture and normal note retrieval.
- Delegated visibility: Later foreground session receives only curated baton rather than the original entire window; no simultaneous worker is launched.
- Selection predicate: Repo slug and explicit/resumed topic; multiple unspecified topics require human choice; new topic proposed by model.
- Invalidation or expiry: Overwrite replaces active baton; clear soft-deletes; opportunistic trash pruning after 30 days; loading alone never clears.
- Activation or effect: Helper enforces preflight and clear checks on its paths; skill asks later host to adopt body as continuation guidance. Actual dependence unobserved.
- Evidence limits: Ignored-path preflight is separate from Write and bypassable through direct tools or helper path; prohibition on indexing/committing is policy beyond prepare. No original-context eviction is performed by this helper.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> Read` the baton in full (path from the list output) and adopt it as
>    continuation context.
> --- `skills/cortex-takeoff/SKILL.md`

### Claims

#### RT-CLM-vault-purpose
Label: Persistent external-memory purpose

SRC-1, `skills/using-cortex/SKILL.md`. Claimed operation is supplying a user's previously distilled knowledge and session records, not performing autonomous domain work in an enclosing runtime. The routes above establish mechanisms and requested maintenance; they do not establish actual benefit or complete preservation.

> The cortex vault is the user's own knowledge base: distilled Notes,
> Projects, and Raw session records.
> --- `skills/using-cortex/SKILL.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-plugin-guidance
Label: Plugin procedure to foreground decisions

SRC-1, `commands/query.md`, `skills/cortex-distill/SKILL.md`, `skills/cortex-broadcast/SKILL.md`, `hooks/scripts/session-start-inject.sh`. Consumer: foreground Claude Code model. Channel: explicitly loaded skills/commands and SessionStart additional context (minus menu when deck substitution succeeds). Force: interpreted natural-language policy, with some host command metadata for tool grants; not a code-enforced human-approval monitor. Horizon: current session, reloaded shipped procedures on later sessions. Human decision points are prescribed per verdict/draft/edit, not established merely by workflow initiation. Runtime clients can invoke CLI/file tools independently of these prompts; host permissions bound those alternatives.

> **Always ask the user**, regardless of where score falls.
> --- `skills/cortex-distill/SKILL.md`

#### RT-BAP-baton-context
Label: Baton to continuation behavior

SRC-1, `skills/cortex-takeoff/SKILL.md`, `hooks/scripts/session-start-inject.sh`. Consumer: later foreground host model. Channel: chosen full-file Read followed by adoption as continuation context; initial menu carries only summary/metadata. Force: interpreted work guidance, not automatic execution or verified correctness. Horizon: sessions for one repo/topic until replacement/clear. [RT-RTE-takeoff-handoff](#rt-rte-takeoff-handoff) establishes the prescribed route; no actual later operation was supplied.

> **Do NOT delete it** — loading is not completion; this session may itself
>    need to hand off again.
> --- `skills/cortex-takeoff/SKILL.md`

## Annotations

none
