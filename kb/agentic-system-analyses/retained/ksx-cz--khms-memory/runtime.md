---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "KHMS memory runtime baseline: capture, headless proposal stages, review admission and hook/CLI return paths at the frozen Git revision."
run-id: AAS-2026-11-08-khms-memory-c5267e800c56-01
reviewed-boundary: f739eb976dab199fd4cd64e352192cc0b112c047
---

# KHMS memory runtime report

## Runtime account

KHMS supplies a memory loop around an external agent, not an enclosing agent scheduler. The operative division is between foreground capture/use, scheduled proposal production, and separately invoked review/application. Files and deterministic Python/shell consumers coordinate the loop; external model calls interpret source excerpts and instructions. The frozen boundary and unavailable deployment evidence remain as stated in [boundary](boundary.md). All source citations below resolve to SRC-1 at that boundary. Implementation wiring is inspected; real activation, review adherence and benefit are not observed.

### Ordinary invocation: one queued MARK to a later answer

1. A foreground agent serving an operator records an event as a MARK in the day's journal. This is prescribed behavior, not a capture hook proven to record every consequential event. `AGENTS.md` supplies the instruction, kinds and later review procedure. The operator, agent and journal location supply the initial identities; the ledger later supplies stable MARK IDs. See [RT-RTE-nightly-proposals](#rt-rte-nightly-proposals).
2. A scheduler or manual caller starts `tools/nightly_distill.sh`. The script resolves the data root, CLI and model settings, takes its code-use/night locks, assembles transcripts, journal and configured Git inputs, freezes a chunk list and window, and calls a fresh generator stage for each group. The model is offered Read/Write/Edit/Glob/Grep, not Bash or delegation. Generated MARK-shaped output passes through `tools/generated_marks.py` and is committed with its window before evaluation. Thus current code is generator → per-MARK evaluation → checked carry/publication, not simply the older sweep/consolidate narrative in `AGENTS.md`. SRC-1: `tools/nightly_distill.sh`, `tools/permark.py`.
3. The evaluator owns progression over queued journal and generated MARKs. Each packet combines the event, source context and selected existing/tonight candidates. A separate tool-less CLI invocation proposes a decision; symbolic parsing determines whether it is usable. Accepted decisions update a document on disk, not approved cards. Deadlines, cost accounting and usage-limit responses stop new work while leaving unfinished items open. Optional format checking can request one repair but is not a universal rejection gate. See [RT-RTE-mark-evaluation](#rt-rte-mark-evaluation).
4. The shell post-processing/carry path retains completed proposals and publishes inbox units. On later runs it distinguishes an already verified publication, a durable output ready to publish, and a batch still requiring a model call. A publication conflict retains the batch and output for manual resolution. Review is attached to a unit/hash, not just a date. SRC-1: `tools/nightly_distill.sh`, `tools/approve_inbox.py`.
5. A reviewer edits or withholds proposals, then calls `tools/approve_inbox.py`. The implementation checks health, writable deployment, prior receipts, parse/schema/lint constraints and duplicate temporary IDs; allocates K IDs; rewrites references; writes cards; updates supersession/contradiction metadata; records unit review; and invokes view generation. The tool does not authenticate that a human or strong model actually reviewed the input. See [RT-RTE-card-admission](#rt-rte-card-admission).
6. On a subsequent foreground invocation, explicit recall returns ranked approved-card summaries, links and separately labelled pending evidence, or a configured host hook supplies selected text as `additionalContext`. The host owns continuation and the eventual answer/action. KHMS delivery alone does not establish that the agent opened a card, complied with a policy, or changed its answer. See [RT-RTE-recall-return](#rt-rte-recall-return) and [RT-BAP-context-delivery](#rt-bap-context-delivery).

The principal is the operator served by the base; a session ID partitions hook state, MARK IDs track queue coverage, temporary candidate labels partition proposal documents, K IDs identify approved cards, and unit hashes/receipts identify admission work. None of these is an identity proof of the reviewer. Source-native natural-language instructions and card bodies are distinct from symbolic IDs, statuses, relations, JSON results, counters and locks. Model parameters are separate components, not another interpretation of Markdown: [RT-CMP-agent-model](#rt-cmp-agent-model), [RT-CMP-qwen](#rt-cmp-qwen), [RT-CMP-bge](#rt-cmp-bge).

### Alternate routes and forcing cases

**Case 1 — approval is a protocol, not a filesystem security boundary.** The approval CLI accepts file arguments and writes after content checks; no signed review token or human challenge appears in that path. The nightly and weekly stages retain Write/Edit tools, and their tool lists are not path-scoped in the command. This establishes a capability surface wider than the promised proposal-only destination, not an observed model bypass. A deployed CLI permission envelope could impose further restrictions, but its implementation/configuration is unavailable. Manual foreground shell/file access also belongs to the excluded enclosing runtime's grants, not a KHMS sandbox. Review remains meaningful as an instructed separation and a specific checked import path; it is not a proved universal exclusion of unreviewed writes. SRC-1: `AGENTS.md`, `tools/approve_inbox.py`, `tools/nightly_distill.sh`, `tools/weekly_synthesis.sh`.

**Case 2 — implemented hook branches are not all shipped example wiring.** The hook contains Agent/Task dispatch and Stop/reply-owed branches. The supplied settings wire SessionStart, UserPromptSubmit, Edit/Write/Bash and a report-tool example, but not Agent/Task or Stop. Therefore those branches are available for further host wiring, not established as active in the example installation. On matched events the hook also fails open on errors, returns early for disabled injection and notifications, and treats a report tool as a stamping path rather than a report-refusal gate. The floor is conditional host integration, not an unavoidable retrieval check. SRC-1: `claude-code/settings.hooks.json`, `tools/khms_hook.py`.

**Case 3 — a format failure does not necessarily suppress a candidate.** Supported CLI/configuration controls can disable the format checker. Its initialization and execution failures explicitly allow unchecked continuation. A failed repair keeps the first decision for downstream checks; it does not mean a valid card was produced. This is reachable from `permark.run`, not merely an unused helper. The later shell checks and the approval gate remain separate enforcement points. No claim that every model output passes every check follows from the presence of the checker. SRC-1: `tools/permark.py`.

**Case 4 — current-only recall and budgets have explicit exceptions.** The recall CLI accepts `--history`/`--all`; those modes intentionally show flagged dead cards. `_finish` also calls pending-evidence rendering before approved results, so output is not exclusively approved knowledge. The hook's dangerous-command precheck runs before the normal card budget, and correction pointers expand the injection character allowance. These paths qualify broad readings of “only current approved cards” and “900-character maximum”; they are not proof that the intended ranking or the bounded exception fails. SRC-1: `tools/khms_recall_hybrid.py`, `tools/khms_pending.py`, `tools/khms_hook.py`, `tools/khms_select.py`.

Additional shipped change routes are weekly synthesis, contradiction triage, daily validity proposals, archive and erratum operations. Their distinct mutation surfaces must not be hidden behind “cards are immutable.” They are bounded in [RT-RTE-maintenance-admission](#rt-rte-maintenance-admission). Code releases and private prompt extensions have separate admission owners: [RT-RTE-operational-change](#rt-rte-operational-change). No target execution, tests or provider calls were performed. No supplied observed-run or causal-experiment layer establishes successful recovery, improved decisions, or a live self-improvement cycle.

### Guarantee ledger

| Guarantee and owner | Enforcement and strength | Coverage and external contract | Separate conclusion statuses |
|---|---|---|---|
| Review before approved knowledge; operator/reviewer | Approval procedure plus schema/lint import checks; **protocol** for review authorization | Checked CLI import only; requires reviewer compliance and host filesystem/CLI grants. Night/weekly file tools and manual writers are not confined by this tool. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Restricted model tools; driver and external CLI | Explicit `--tools`, setting-source and MCP controls; **policy** | Generator/legacy consolidation and weekly have file tools; per-MARK has no tools; validity judge has its own read/Bash policy. Requires the external CLI to honor flags. Not OS isolation. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Serialized recoverable card writes; Python writers | Host-local card lock, atomic single-file replacement, dirty marker and receipts; **protocol** | Cooperating writers on the same runtime lock domain. Not an all-files transaction or a cross-host synchronization guarantee; recovery needs retained server versions and reconciliation. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Automatic recall floor; hook integration | Event matching, selection and emission; **best effort** | Requires installed/matched host hooks; fail-open, switches, budgets and early returns apply. Delivery is not obedience. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Bounded background work; shell/evaluator | Per-call timeouts and no-new-work deadlines, estimated cost reservation; **best effort** | Limits start decisions/calls, not a proved exact total-dollar cap or full-model-context bound. External subprocess/provider behavior remains a dependency. | implementation conclusion status: wired; operation conclusion status: uninspected |

The source passages supporting these scopes are retained in the linked records below. Host-local locking explicitly prevents a stronger distributed conclusion. Added inspection beyond boundary's initial slices includes SRC-1 implementation in `tools/khms_select.py`, `tools/khms_pending.py`, `tools/khms_lock.py`, `tools/khms_prompt.py`, `tools/embed_index.py`, `tools/card_validity.py`, and maintenance decision slices in `tools/apply_triage.py`; it also includes doctrine in `tools/khms_erratum.py` and the release procedure in `README.md`. These remain the same registered source, not new sources or run evidence.

## Shared records

### Components

#### RT-CMP-agent-model
Label: Configured headless agent model

The nightly generator, per-MARK evaluator, consolidation and weekly synthesis invoke a configured external agent CLI with stage model names. This is a distributed-parametric inference component reached through symbolic command arguments and natural-language input packets. Provider weights/storage and internals are outside the checkout. No weight-changing operation is shown in the inspected call paths; that does not establish provider-side immutability. Exact model versions are not pinned by these alias/configuration arguments, and an endpoint or alias may resolve to a different model. The nightly script logs CLI version and served model metadata when available. SRC-1: `tools/nightly_distill.sh`, `tools/permark.py`, `tools/weekly_synthesis.sh`.

> SWEEP_MODEL=$(khms_get KHMS_SWEEP_MODEL)
> MARK_MODEL=$(khms_get KHMS_MARK_MODEL)
> CONS_MODEL=$(khms_get KHMS_CONS_MODEL)
> --- `tools/nightly_distill.sh`

> def claude_cmd(agent, model, rules, effort=None):
>     return [agent, "-p", "--model", model, "--output-format", "json", "--tools", "",
>             "--system-prompt", rules, "--setting-sources", "", "--strict-mcp-config",
>             "--no-session-persistence", "--effort", effort or EFFORT]
> --- `tools/permark.py`

Validity judging also has a Claude CLI adapter with its own policy and a Copilot calibration adapter. These are alternative model consumers, not evidence of local training. Exact deployed providers/models are uninspected. SRC-1: `tools/card_validity.py`.

#### RT-CMP-qwen
Label: Qwen embedding model

Optional dense retrieval uses the source-native `qwen` configuration for `Qwen/Qwen3-Embedding-0.6B`. Distributed-parametric weights are loaded through SentenceTransformer; produced vectors are numerical representations stored separately from Markdown cards. The inspected loading path performs inference, not parameter updates. It supplies a model repository name but no immutable artifact revision; later resolution/cache changes may yield different weights. The running daemon's actual artifact is uninspected. SRC-1: `tools/embed_index.py`, `tools/embed_server.py`.

> "qwen": {"hf": "Qwen/Qwen3-Embedding-0.6B", "dim": 1024,
> --- `tools/embed_index.py`

> return SentenceTransformer(hf_id, device=device)
> --- `tools/embed_index.py`

#### RT-CMP-bge
Label: BGE embedding model

The alternative `bge` model is `BAAI/bge-m3`, with the same distributed-parametric inference/loading substrate and no revision argument in the loader cited in [RT-CMP-qwen](#rt-cmp-qwen). No parameter update appears in that path. Exact artifact fixity and deployment selection are uninspected; mutable model-name resolution is possible. It is an optional alternative, not evidence both models serve every query. SRC-1: `tools/embed_index.py`.

> "bge":  {"hf": "BAAI/bge-m3", "dim": 1024,
>              "query_prefix": "", "doc_prefix": ""},
> --- `tools/embed_index.py`

### Operative objects

none declared in this member

### Routes

#### RT-RTE-nightly-proposals
Label: Nightly proposal production

Trigger/owner: scheduler or manual caller starts the shell driver for the operator's base; shell code owns window/chunk progression and the external model proposes generated event lines. Endpoints are configured transcripts/journal/Git sources → generated ledger → per-MARK output → carry batches → inbox units. Source guidance is the rendered generator/MARK/consolidation prompts, schema and tags. Natural-language proposals are selected under symbolic queue and commit rules. This is open operational capture, not a curriculum with a known correct answer. Source-quote checks are local grounding checks, not an answer oracle for truth or usefulness. Human review can withhold later admission, but no per-proposal human decision is needed to produce an inbox unit. SRC-1: `tools/nightly_distill.sh`, `tools/permark.py`.

- Immediate return: Shell status/logs and completed inbox/carry outputs; no direct final user answer.
- Later read-back: Generated windows, completion records, carry outputs and open MARKs drive later runs; inbox units reach review.
- Delegated visibility: File-tool generator sessions receive prompt-listed chunk groups; per-MARK sessions receive prepared packets, not the foreground conversation.
- Selection predicate: Frozen source window/list, queue coverage, stage deadlines, usage limits and batch publication verification.
- Invalidation or expiry: Hash/window mismatch prevents reuse; unfinished work remains queued; conflicting publication requires manual reconciliation.
- Activation or effect: Writes proposals and progress state; approved-card effects require a separate admission invocation.
- Evidence limits: Source wiring only; complete capture and successful model compliance are unobserved.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> STAGE_ISOLATION=(--setting-sources "" --effort high --strict-mcp-config --tools $TOOLS)
> --- `tools/nightly_distill.sh`

> TOOLS="Read Write Edit Glob Grep"
> --- `tools/nightly_distill.sh`

> echo "$(date -Is) PUBLISH CONFLICT $BID (verify rc=$VRC): ${UNIT##*/} is not provably this batch's output — batch and its output stay in the carry queue, no model call; resolve by hand (see the verify line above)" >> "$LOG"
> --- `tools/nightly_distill.sh`

Working-context control: generator groups isolate source chunks in separate sessions, retaining generated lines/completion hashes rather than an ever-growing conversation. This resembles per-task frames with file results escaping, but file-tool sessions may read beyond their initial prompt lists under host permissions. The group limit bounds primary source input, not total model context. Retry/continued work is coordinated by disk artifacts, not shared agent context. No runtime model-parameter update follows from this persistence.

#### RT-RTE-mark-evaluation
Label: Per-MARK decision evaluation

Owner: `permark.run` builds a packet, calls the configured model, parses its decision and applies it to the proposal document. The model proposes new/superseding/contradicting candidates or coverage/verdict decisions; code can refuse unparsed answers. Configured format checks compare schema, quotes and lint, and can request a repair. These are mechanical predicates, not a reference answer oracle. The operating mode is sequential evaluation of operational MARKs; a format failure, transport failure or quota/deadline can change retry/progression. SRC-1: `tools/permark.py`.

- Immediate return: Atomic proposal-document updates and per-call usage/decision logs.
- Later read-back: Existing decisions are skipped on resume; earlier candidates are selected into subsequent packets; nightly carries completed output onward.
- Delegated visibility: Tool-less subprocess sees rules, schema/tags and selected packet, not the foreground agent's full state.
- Selection predicate: Undecided queued MARKs, packet budgets, retrieval of related cards/candidates and remaining stage budget.
- Invalidation or expiry: Failed/unparsed work is not applied; configurable format failure can retain the original answer for downstream checking rather than reject it.
- Activation or effect: Parsed decisions change proposal state, not approved knowledge; later consumers must separately admit it.
- Evidence limits: Real semantic accuracy, grounding success and benefit are unobserved; checker continuation is not validation success.
- implementation conclusion status: wired
- operation conclusion status: uninspected

The driver can retry failed model calls twice and can spend another call on a format repair. “One call per MARK” describes the normal path, not a strict maximum. A fresh no-persistence CLI call is a context frame: the packet is pushed, the model returns text/metadata, and the parent retains only parsed material plus logs. Code controls packet budget/retrieval; it does not compact a live foreground conversation. SRC-1: `tools/permark.py` and [RT-CMP-agent-model](#rt-cmp-agent-model).

> for attempt in (1, 2):
>             res = one_call(packet, f"attempt {attempt}/2")
>             if res["ok"] or res["limit"]:
>                 break
> --- `tools/permark.py`

> except Exception as exc:      # the check's own failure: logged, the answer goes on unchecked, no call spent
> --- `tools/permark.py`

> log_to(log, f"permark-{mk['id']} format check FAILED after the retry — the first answer is kept, the later "
>                 f"stage drops or flags it: " + " | ".join(probs2))
> --- `tools/permark.py`

#### RT-RTE-card-admission
Label: Reviewed card import

Owner/trigger: a reviewer invokes `approve_inbox.py` on reviewed file arguments. Human/strong-model review is prescribed, while the computational tool decides structural acceptance. The principal can reject or edit before invoking it; caller identity alone does not establish a human contribution. Guidance is the approval procedure, card schema and lint rules. Proposed changes are new cards plus associated graph/status metadata. The importer cuts withheld trailers, validates the accepted head, rejects duplicate temporary IDs and schema/lint failures, then allocates IDs and records the work. There is no expected-answer oracle; guards test structure and selected consistency properties. Mode is review/import of operational proposals. SRC-1: `AGENTS.md`, `tools/approve_inbox.py`.

- Immediate return: K-ID mapping, status output and subsequent view-build status.
- Later read-back: Cards and generated views serve retrieval; receipts and hash-bearing unit review markers prevent blind repeated admission and inform later review.
- Delegated visibility: inapplicable — the importer itself calls no model; reviewer context is supplied by its enclosing session.
- Selection predicate: Parsed cards above DEFERRED/DROPPED trailers, healthy/writable base, no conflicting partial receipt, valid schema/lint and unique temporary labels.
- Invalidation or expiry: Changed unit content invalidates prior review-hash equivalence; differing content at a reserved path forces reconciliation.
- Activation or effect: Atomic per-card writes, temporary-reference remap, supersession/contradiction metadata changes and generated-view rebuild.
- Evidence limits: Review authorization/compliance is not authenticated; multi-file crash recovery and external version retention are not observed.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> Run ONLY after human/smart review of the input files (P6). Validate with build_views.py afterwards.
> --- `tools/approve_inbox.py`

> if os.path.exists(path) and open(path, encoding="utf-8").read() != out:
>                 print(f"ERROR: {path} differs from the pending approval — reconcile receipt", file=sys.stderr)
>                 sys.exit(1)
>             L.atomic_text(path, out)
> --- `tools/approve_inbox.py`

Recovery is receipt-aware retry/reconciliation, not rollback of an all-files database transaction. The importer marks the base dirty before mutation; a failed build leaves it dirty. Locks serialize cooperating local writers, while external file versions are the prescribed per-file recovery substrate. Metadata updates explicitly revise old cards even though the doctrine calls approved cards immutable. SRC-1: `tools/approve_inbox.py`, `tools/khms_lock.py`, `AGENTS.md`.

> Lockfiles are host-local;
> only durable mutation/rebuild receipts live in the synchronized base.
> --- `tools/khms_lock.py`

#### RT-RTE-recall-return
Label: CLI and hook recall return

Owner/trigger: foreground agent invokes `recall.sh`, or the enclosing host invokes `khms_hook.py` on a matched event. CLI code returns results; hook code extracts an event-specific query, evaluates experiment switches and cooldown/rate conditions, loads/prepares cards, runs selection, saves session state and emits context. The next-step owner is the foreground model/host, not a KHMS action executor. Natural-language snippets/pointers enter context under symbolic scoring and budget rules. SRC-1: `claude-code/settings.hooks.json`, `tools/khms_hook.py`, `tools/khms_recall_hybrid.py`, `tools/khms_select.py`.

- Immediate return: Ranked CLI summaries/links and channel/freshness labels, or JSON additionalContext; no-hit CLI status can be 1.
- Later read-back: Retained cards reach later model invocations; session-state files retain injection timestamps, recent queries and budget use.
- Delegated visibility: Hook dispatch handling is implemented for Agent/Task but not wired by the supplied example; injected context's propagation to subagents depends on the external host.
- Selection predicate: Event-specific query extraction; lexical ranking and optional dense retrieval; live-card handling, thresholds, dedup TTL, rate cap/bypass, primary slots and text budget.
- Invalidation or expiry: Kill switch, experiment controls, query cooldown, TTL and state windows affect delivery; dense freshness check can refresh or label/fallback. History mode intentionally returns dead cards flagged.
- Activation or effect: Context delivery and audit/state writes are implemented; behavioral activation by the receiving model remains unobserved.
- Evidence limits: External hook installation, model compliance and quality of ranking/embeddings are not observed. CLI pending evidence is labelled unreviewed, not admitted knowledge.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> def emit(event, text):
>     print(json.dumps({"hookSpecificOutput": {"hookEventName": event, "additionalContext": text}}))
> --- `tools/khms_hook.py`

> if a in ("--history", "--all"):
>             history = True
>             continue
> --- `tools/khms_recall_hybrid.py`

> print('UNREVIEWED EVIDENCE (lexical; journal findings, not approved knowledge):')
> --- `tools/khms_pending.py`

> return text[:p.char_cap + warn_chars], used
> --- `tools/khms_select.py`

Working-context control here is selective introduction of retained material, not trimming already accumulated turns. The hook deliberately suppresses repeated/budget-exceeding material, while explicit recall and card-file opens provide reload paths under the agent's control. The frame analogy only partly fits: emitted text is by value in the host window; pointers name external files but are not automatically dereferenced or liveness-managed. A risky-command precheck can return before ordinary selection and is not blocked by the regular budget. Exceptions in the top-level hook are logged and exit successfully, making the control best effort rather than fail-closed. SRC-1: `tools/khms_hook.py`.

> except Exception as e:      # fail open, always
>         _append(LOG, f"{_stamp()} | ERROR | v2 {type(e).__name__}: {e}\n")
>         sys.exit(0)
> --- `tools/khms_hook.py`

#### RT-RTE-maintenance-admission
Label: Maintenance proposal and application

Distinct entry paths share a proposal/reviewer/application separation but not one universal guard. Weekly synthesis uses chunked model calls with read-coverage checks and stages a proposal; triage application consumes explicit per-row verdicts; daily validity judging generates proposals and waits for a reviewer-maintained APPLIED marker before a later batch. Archive and erratum commands are separate explicit mutation operations. SRC-1: `tools/weekly_synthesis.sh`, `tools/apply_triage.py`, `tools/khms_validity_daily.sh`, `tools/khms_archive.py`, `tools/khms_erratum.py`.

- Immediate return: Proposal files or application reports/diffs, depending on command and apply mode.
- Later read-back: Accepted status/link/body/archive changes alter later retrieval; proposal and review state coordinate subsequent maintenance.
- Delegated visibility: Weekly sessions see required file groups; validity uses copied evidence trees and a model adapter with read/Bash policy. Actual host isolation and private review contexts remain unobserved.
- Selection predicate: Weekly required-input/read-coverage gates; triage verdict and quote-coverage guards; validity sampled unchecked active cards and older-batch waiting condition; archive/erratum explicit target/operation arguments.
- Invalidation or expiry: Missing triage verdict rejects that row; evidence/graph conflicts can reject changes. Recovery uses file history and ledger/receipt reconciliation, not a demonstrated universal undo.
- Activation or effect: Application can change status/relations, move cards to archive, or correct text through an erratum while retaining retracted wording.
- Evidence limits: This is an inventory of distinct admission surfaces, not an exhaustive proof of every maintenance helper's correctness or real reviewer decisions.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Proposers are background models/code; reviewer verdicts or explicit CLI choices decide/veto application subject to guards. A reviewer may be human or computational; `--by owner|coordinator` records a declared role, not authentication. Guidance includes synthesis and maintenance instructions, evidence quotes and card classification rules. Proposed changes persist only through the selected application command. This route establishes admission machinery, not formulated criticism or a demonstrated theory-builder cycle. No answer oracle is established by a judge label: evidence commands/quote matching constrain its assessment, not a supplied correct answer. SRC-1: `tools/apply_triage.py`, `tools/khms_erratum.py`, `tools/card_validity.py`.

> if not d:
>             outcomes[n] = ("REJECT", "no verdict line in the REVIEW VERDICT section — "
>                                      "silence is not approval")
>             continue
> --- `tools/apply_triage.py`

> # Verification and apply are NOT this job: they belong to whoever reviews the base, and the morning ping
> # (khms_review_ping.sh) names every batch whose parts wait.
> --- `tools/khms_validity_daily.sh`

> """Erratum — correct ONE claim of ONE approved card in place — a claim that was false when it
> was written (default kind `wrong-record`), or a VALUE that was true when written and has since
> moved in the repo (kind `dated-pointer`) — keeping the retracted wording visible inside the
> card and in the tombstone ledger.
> --- `tools/khms_erratum.py`

The validity Claude adapter differs materially from tool-less per-MARK calls: it offers Bash/Read/Grep/Glob with command-pattern preapproval and dontAsk permissions. Its working directory is the copied evidence root, but its subprocess inherits the environment. A read-only tree and CLI restrictions do not establish an OS-level isolation envelope. The separate Copilot calibration leg and provider internals remain an opaque alternative beyond these inspected adapter slices. SRC-1: `tools/card_validity.py`.

> allowed = ["Read", "Grep", "Glob"] + [f"Bash({c} *)" for c in ALLOWED_COMMANDS] + \
>                   [f"Bash({c})" for c in ("ls",)]
> --- `tools/card_validity.py`

#### RT-RTE-operational-change
Label: Code and prompt configuration changes

Trigger/owner: deployment maintainer updates the code clone or private prompt/configuration files. The release procedure requires pausing jobs/users, stopping the embedding daemon, selecting an exact approved commit with green CI, and fast-forwarding under an exclusive code-use lock. Prompt rendering substitutes configured fields and private extension slots before model invocation. These are two separate admission paths: operator Git release selection and filesystem/configuration-controlled prompt replacement. The current deployment's private content and actual approval process are unavailable. SRC-1: `README.md`, `tools/khms_prompt.py`.

- Immediate return: Git refusal/success or rendered prompt/error; subsequent jobs consume the changed code/instructions.
- Later read-back: Clone code and extension files persist across jobs; base data is retained separately.
- Delegated visibility: Rendered stage prompts carry extension text into headless calls; not every stage sees every extension.
- Selection predicate: Release procedure selects an approved SHA; renderer selects named templates, slots and configured fields, with shipped defaults for missing extensions.
- Invalidation or expiry: Unknown/malformed placeholders fail rendering; locks can refuse updates. Rollback/recovery of deployed code beyond the stated Git procedure is uninspected.
- Activation or effect: Changes future driver/consumer behavior or model guidance when used; no automatic code self-rewriter is established by these paths.
- Evidence limits: Release gate is instructed, not cryptographically enforced by Git; extension authorship, review and actual deployment changes are unavailable.
- implementation conclusion status: wired
- operation conclusion status: uninspected

The maintainer proposes/decides/vetoes release and prompt changes; software enforces rendering and lock/fast-forward mechanics. Green tests are a prescribed release criterion, not an answer oracle for live outcomes. Mode is operator-managed deployment. Extensions can replace a whole shipped default block verbatim; this is dynamic instruction customization, not evidence of arbitrary plugin execution or autonomous capability acquisition. The guidance and persisted result are the replacement instruction text/configuration and the selected code revision. SRC-1: `README.md`, `tools/khms_prompt.py`.

> flock -n -x "$lock" git -C "$KHMS_CODE" merge --ff-only "$approved_sha"
> --- `README.md`

> if not os.path.isfile(f):
>             if used is not None:
>                 used.append(f"EXT:{slot} (shipped default)")
>             return default
>         with open(f, encoding="utf-8") as fh:
>             body = fh.read()
> --- `tools/khms_prompt.py`

### Claims

#### RT-CLM-review-boundary
Label: Proposal-only background contract

Claimed operation: the foreground agent must obtain operator approval before writing know/, and background work proposes rather than approves. This is doctrine, qualified by [RT-RTE-card-admission](#rt-rte-card-admission) and the broader file-tool capabilities in [RT-RTE-nightly-proposals](#rt-rte-nightly-proposals). SRC-1: `AGENTS.md`.

> **You may not write into `memory/know/` without your operator's approval.** Background
>    stages propose; approval is a separate, human-or-strong-model step.
> --- `AGENTS.md`

- doctrine conclusion status: claimed
- implementation conclusion status: wired
- operation conclusion status: uninspected

The wired portion is separate proposal/import machinery, not authenticated universal approval enforcement.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-context-delivery
Label: Retained cards into foreground context

Consumer: enclosing foreground agent model and, through its answer/actions, the operator. Channel: explicit recall tool output or hook JSON additionalContext. Force: informational snippets and instruction/policy text interpreted by the model, not code-level control of its answer. Horizon: later invocations and sessions that share the retained base. [RT-RTE-recall-return](#rt-rte-recall-return) supplies selection and delivery evidence; actual compliance or beneficial action is unobserved. The bootstrap procedure also tells the agent to keep generated MEMORY.md in context, a prescribed rather than independently enforced channel. SRC-1: `tools/khms_hook.py`, `AGENTS.md`.

> `MEMORY.md` is generated — never edit it by hand, and never edit anything in `memory/views/`.
> Its §1 is the body of the bootstrap-digest card, so the retrieval rules travel with the index
> that is always in your context.
> --- `AGENTS.md`

## Annotations

none
