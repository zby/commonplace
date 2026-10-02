---
type: agentic-systems/types/agentic-system-epistemic-report.md
description: "Epistemic routes of instinctual-memory: claim formation, checks, retrieval authority, and evaluation"
run-id: AAS-2026-10-02-instinctual-memory-01
reviewed-boundary: "6acb13dc35765bf5ccfc87e445dd09c480f1c28a"
---

# instinctual-memory epistemic report

## Source-and-claim boundary

The question is what `mem` acquires or produces as truth-apt content, what checks or disposes those candidates, what authority the results receive, and whether results affect later behavior. The boundary is the CLI/library and its registered hooks and service interfaces in `SRC-1` and `SRC-2`. The host agent, its prompt assembly beyond the hook protocol, user stores, deployments, external providers, and operation traces are excluded. Runtime findings below are supplied by the runtime member; direct source reads here checked the hook, consolidation, validation, tidy, evaluation, ingestion, and operation paths.

The runtime member establishes journal backfill, consolidation, explicit changes, search, MCP/HTTP, setup, and writeback. Direct inspection adds two relevant routes that its account did not trace: `mem hook prompt` returns selected facts as host `additionalContext`, and `mem tidy` can judge candidates and retract/suppress selected facts. The supplied whole-repository boundary is sufficient to assess these implemented routes, but no deployed hook configuration, rubric, actual store, provider response, or run trace is available. Thus activation in a host, proposition accuracy, human review, subsequent host use, and task benefit remain unobserved. No system-wide negative follows for operation or benefit.

| Entry point or operation | Source path | Coverage | Limit and conclusion prevented |
|---|---|---|---|
| Backfill/ingest; journal search | `src/ingest.rs`, `src/cli.rs`, `src/search/` | `OBJ-1`, `RTE-1`, `RTE-3` | Imported statements retain source references; source truth and use by a model are not assessed. |
| Consolidate | `src/consolidate.rs`, `src/validate.rs`, `src/repo.rs` | `OBJ-1`, `OBJ-2`, `RTE-2` | Candidate formation, checks, disposition, and publication are inspected; no semantic truth check or observed correctness is established. |
| Search through CLI, MCP, HTTP, shell | `src/ops.rs`, `src/mcp.rs`, `src/http_serve.rs`, `src/search/` | `RTE-3` | The caller receives ranked results. Host decision and activation are not established by these interfaces. |
| Prompt hook | `src/hook.rs` | `EPI-RTE-1` | Implemented hook protocol supplies context; installation and actual model consumption are unobserved. |
| Explicit remember/correct/forget and erase | `src/change.rs`, `src/erasure.rs`, `src/cli.rs` | `RTE-4` | Operator/client assertions determine content; validation checks domain structure and state transitions, not truth. |
| Tidy | `src/tidy.rs`, `src/cli.rs` | `EPI-RTE-2` | Duplicate and session-only judgments can affect future availability; no external truth labels or observed judgment quality are supplied. |
| Held-out retrieval evaluation | `src/evaluation.rs`, `src/cli.rs` | `EPI-RTE-3` | A caller-supplied rubric can score retrieval; no rubric or operation trace is supplied, and scoring does not establish claim truth or improve the store. |
| Writeback/setup | `src/cli.rs`, `src/setup.rs` | `OBJ-3`, `RTE-5` | Generated facts can enter host instruction files; later host reading and behavior are outside observed evidence. |

The only supplied system claim is `CLM-1`: an intended portable, durable agent-memory workflow with backfill, consolidation, search, and host integrations. No separate warrant or accuracy guarantee was found in the supplied claim record. The inspected paths implement mechanisms for forming, retaining, ranking, and publishing factual assertions, but do not establish that those assertions are true or improve future task performance (`SRC-1`, `README.md`; `SRC-2`, `src/consolidate.rs`, `src/validate.rs`).

## Epistemic-object inventory

| object ID | candidate truth-apt content or none | claimed role | evidence source ID and local anchor | gap/limit |
|---|---|---|---|---|
| `OBJ-1` | Imported user, assistant, tool, note, and other source-event text; many entries can state propositions | Raw source material for search and later consolidation | `SRC-2`, `src/ingest.rs`, `src/journal.rs` | Source identity and text are retained; source reliability, truth, and context beyond recorded metadata are unknown. |
| `OBJ-2` | Entity fact statements with predicates, evidence excerpts, source references, and lifecycle status | Curated, retrievable assertions | `SRC-2`, `src/fact.rs`, `src/entity.rs`, `src/consolidate.rs` | Evidence excerpt matching is textual. Semantic entailment, source truth, and independent confirmation are not established. |
| `OBJ-3` | Generated instruction text containing selected fact statements | Project-specific instructions derived from curated facts | `SRC-2`, `src/cli.rs` | Its statements inherit the unresolved warrant of the facts; host delivery and reliance are unobserved. |
| `EPI-OBJ-1` | Tidy findings classify fact statements as duplicate or session-only | Candidate disposition input for optional forgetting | `SRC-2`, `src/tidy.rs` | Duplicate is a lexical similarity judgment; session-only is a model judgment against a code prompt. Their correctness is unobserved. |
| `EPI-OBJ-2` | Evaluation rubric cases specify expected fact IDs and required/forbidden strings | Retrieval-ranking reference outcomes | `SRC-2`, `src/evaluation.rs` | No run rubric is supplied. These criteria assess retrieval behavior, not truth of stored propositions. |

## Authority-route ledger

| route ID | route function | architectural status | object/candidate ID | content/update relation | transition or check target | evaluator/condition and domain | activation and timing | possible or observed result | implemented force | epistemic authority and scope | operational authority: behavior permitted, blocked, or changed | behavioral-authority path: consumer, channel, force, horizon | evidence source ID and local anchor | claim IDs or none | mismatch marker or none | gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `RTE-1` | content transformation | implemented | `OBJ-1` | `truth-apt transformation: acquisition/import` (source warrant unknown) | Supported source records to journal events | Format adapters parse and normalize records; no truth evaluator | On explicit ingest/backfill or host-triggered sync | Journal events or skipped/error records | Retained input available to search and consolidation | No truth license beyond the recorded source assertion | Makes imported text retrievable and eligible for later processing | Search/consolidation callers; journal; advisory; later invocations | `SRC-2`, `src/ingest.rs`, `src/cli.rs` | `CLM-1` | none | Parsing and normalization do not authenticate proposition truth. |
| `RTE-2` | content transformation | implemented | `OBJ-1` → `OBJ-2` | `truth-apt transformation: indeterminate` | Event text to proposed factual statement and evidence reference | Rules patterns or configured LLM; event text and evidence reference are the input domain | On `mem consolidate`, in bounded batches | Candidate facts, quarantine reasons, and updated entities | Candidates can enter published memory after subsequent disposition and validation | No truth warrant established; an exact textual evidence match does not establish semantic entailment or truth | Makes selected proposals eligible for future reads; blocked/repeated facts may be dropped | Consolidator to `OBJ-2`; durable Git state; permissive eligibility; across invocations | `SRC-2`, `src/consolidate.rs` | `CLM-1` | none | For LLM proposals, verbatim evidence text is required; source truth and the semantic relation between quote and assertion remain unverified. For rules, a narrow pattern is applied to user statements. |
| `RTE-2` | check/evidence production | implemented | `OBJ-2` candidate | `no content change` | Fact/entity schema, source references, known IDs, controls, checkpoint, and candidate-tree invariants | `DomainValidator`; structural/domain rules over candidate Git state | Before publication | Candidate accepted by validator or rejected with error | Publication gate for writes through the publisher | Structural validity only; no epistemic license for proposition truth | Permits publication of schema-valid state, blocks invalid state | Validator to publisher; protocol gate; publication attempt | `SRC-2`, `src/validate.rs`, `src/repo.rs` | `CLM-1` | none | The validator's stated remit is domain-rule validation; no truth criterion is present. |
| `RTE-2` | disposition/acceptance | implemented | `OBJ-2` candidates | `non-truth-apt policy/content update: event disposition and fact lifecycle status` | Whether extraction generated a fact, passed filters, and can be published | Extractor proposes; code filters, validates, and publishes; operator/host invokes and selects configuration, but the ordinary publication path has no human review gate. No expected-answer oracle. Mode is open-ended input consolidation in bounded batches; new journal events after the checkpoint trigger work. | During each consolidation batch | Accepted event sequences, quarantined sequences, and committed candidate tree | Controls admission to curated storage | “Accepted” here means pipeline disposition, not evidence-consuming epistemic acceptance of a claim | Admits or excludes candidate material from curated memory | Consolidator/publisher to stored memory; permissive or withholding; later searches | `SRC-2`, `src/consolidate.rs`, `src/repo.rs` | `CLM-1` | none | No intended-use truth criterion or independent reference outcome is applied. |
| `RTE-2` | retention | implemented | `OBJ-2` | `no content change` | Published entity facts, controls, index, and checkpoint | Git publisher validates candidate and compare-and-swaps against base revision | On successful publish | New revision or conflict | Durable read-back in later invocations | Retention carries no new warrant | Makes the retained version available to search/read/history; stale-base writes are blocked | Store consumers; Git tree; persistent across invocations | `SRC-2`, `src/consolidate.rs`, `src/repo.rs` | `CLM-1` | none | Persistence and atomic publication do not establish correctness. |
| `RTE-3` | operational admission/selection/consumption | implemented | `OBJ-1`, `OBJ-2` | `no content change` | Query, scope/project filters, candidate eligibility, and ranking | Lexical search and optional JEV/local reranker judge relevance/order, not proposition truth | On CLI/MCP/HTTP/shell search request | Ranked hits with statements, IDs, and source references | Advisory output to caller | No epistemic endorsement; ranking licenses relevance ordering only | Makes selected material available for caller use; caller decides what to believe or do | CLI/client caller; result payload; advisory; current request | `SRC-2`, `src/ops.rs`, `src/search/`, `src/mcp.rs`, `src/http_serve.rs` | `CLM-1` | none | Runtime traces do not establish any host model receives or acts on these results. |
| `EPI-RTE-1` | operational admission/selection/consumption | implemented | `OBJ-2` | `no content change` | Current prompt and returned fact statements | Hook search plus lexical-word overlap predicate; at least two meaningful terms, or one for a one-term prompt | On installed host prompt hook, for eligible prompts | Up to six selected fact statements serialized as host `additionalContext` | Advisory context injection through hook protocol | No new truth warrant; facts are explicitly framed as recorded memory to check against code if it may have changed | Can affect the receiving host model's current prompt if the host activates and consumes the hook result | Host model; `hookSpecificOutput.additionalContext`; advisory; current prompt/session | `SRC-2`, `src/hook.rs` | `CLM-1` | Runtime RTE-3 covers search outputs but omits this distinct hook consumer and context channel. | Hook implementation and selection are inspected; installation, delivery, and effect in a deployment are unobserved. |
| `RTE-4` | content transformation | implemented | `OBJ-2` | `truth-apt transformation: acquisition/import` (source warrant unknown) | Operator/client-supplied fact assertion in remember/correct request | Requester supplies the statement and target; code validates payload and current entity state, but no answer oracle or truth evaluator is established | On explicit remember/correct request | New assertion, or replacement assertion with prior fact superseded | Published to curated memory | Epistemic authority is the requester's assertion alone; source reliability and truth are unknown | Makes the assertion available for later reads and searches | Operator/client to Git-backed store; permissive; later invocations | `SRC-2`, `src/change.rs`, `src/cli.rs` | `CLM-1` | none | This open-ended request route has no independent reference outcome or human review gate in the inspected publication path. |
| `RTE-4` | disposition/acceptance | implemented | `OBJ-2` | `non-truth-apt policy/content update: retract and suppress a targeted assertion` | Target fact's current lifecycle state and request | Requester proposes forget; code checks target/entity state, then publishes; no truth criterion or answer oracle | On explicit forget request | Fact retracted and suppressed, or request rejected | Withholds targeted fact from reads and future consolidation | No truth finding is made; this is an operational withdrawal | Blocks future availability and re-extraction of the target | Operator/client to Git-backed store; withholding; later invocations | `SRC-2`, `src/change.rs`, `src/cli.rs`, `src/erasure.rs` | `CLM-1` | none | Validation of identifiers and lifecycle rules is not an epistemic acceptance. |
| `EPI-RTE-2` | check/evidence production | implemented | `OBJ-2` → `EPI-OBJ-1` | `truth-apt transformation: indeterminate` | Whether a stored fact is duplicate or lasting/useful for a future teammate | Word overlap/containment for duplicates; optional LLM judgment against the session-only prompt. Operator invokes this open-ended tidy review; the optional model compares wording to the specified criterion; no answer oracle or external labels. | On `mem tidy`; LLM branch only when configured | Tidy findings | Advisory report; no store change | The judgment concerns duplication or expected persistence/use, not proposition truth | Provides findings for operator review and possible withdrawal | Tidy caller; report output; advisory; current invocation | `SRC-2`, `src/tidy.rs` | `CLM-1` | none | The session-only category is a model judgment without external labels; duplicate detection uses lexical criteria. Correctness and deployment use are unobserved. |
| `EPI-RTE-2` | operational admission/selection/consumption | implemented | `EPI-OBJ-1` → `OBJ-2` | `non-truth-apt policy/content update: retract and suppress selected facts` | Tidy findings and fact lifecycle state | Operator chooses whether to apply; code retracts and suppresses selected facts. There is no answer oracle for truth and no automatic learning trigger. | Only on explicit `mem tidy --apply` | Selected facts disappear from all reads and are excluded from later consolidation | Withholding from future retrieval | No proposition truth authority is assigned | Blocks selected facts from reads and re-extraction | Store consumers; controls and fact status; enforcing exclusion; subsequent invocations | `SRC-2`, `src/tidy.rs` | `CLM-1` | none | The operator may keep listed facts; deployed use and downstream effect are not observed. |
| `EPI-RTE-3` | check/evidence production | implemented | `OBJ-1`, `OBJ-2`, `EPI-OBJ-2` | `no content change` | Whether expected IDs and required/forbidden strings appear in top search hits | Rubric cases and search output; rubric author supplies reference IDs and strings | On explicit evaluation with a rubric | Per-case pass/fail, recall and rank; optional lexical/reranked comparison | Report only; no automatic memory update | Scoped evidence about retrieval against that rubric, not truth, source warrant, or general knowledge quality | Can inform a human/operator's later choices; code does not apply result to facts or policy | Evaluation report to invoking operator; advisory; later decisions only if operator uses it | `SRC-2`, `src/evaluation.rs`, `src/cli.rs` | none | none | No rubric, run, or later decision is supplied. The criterion has a bounded retrieval use; it does not establish ampliative claim acceptance. |
| `RTE-5` | operational admission/selection/consumption | implemented | `OBJ-2`, `OBJ-3` | `truth-apt transformation: non-ampliative reshaping` | Eligible curated facts selected for project instruction writeback | Project/fact selection and managed-region merge; no truth evaluator | On explicit writeback or setup-related operator action | Managed instruction-file region or host configuration | Can shape later host context if read | Inherits source warrant of each fact; no additional endorsement | Makes selected content available to later host operation | Host runtime; project instruction file; advisory; later invocations | `SRC-2`, `src/cli.rs`, `src/setup.rs` | `CLM-1` | none | Host reading and behavioral effect are not observed. |

The two applied transformations into claim-bearing content remain indeterminate. The fact statements may restate source assertions, but the implementation checks quoted-text occurrence or pattern matches, not semantic preservation. The evidence needed to decide entailment is an inspection of each input/proposal pair and the transformation's semantics; no such execution pairs are supplied. Accordingly, no ampliative fact-production claim is inferred merely because exact entailment is unproven.

## System-claim versus route comparison

| claim ID | claimed operation or warrant | claim source ID/anchor and evidence layer | doctrine/design support | implemented route IDs | observed-run support | causal support and design limits | supported conclusion | mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| `CLM-1` | Portable durable memory workflow that backfills, consolidates, searches, and integrates with agent hosts | `SRC-1`, `README.md`, doctrine/design | Product description and command/integration documentation; inspected code implements import, candidate formation, durable retention, retrieval, host hook output, and writeback | `RTE-1`, `RTE-2`, `RTE-3`, `EPI-RTE-1`, `RTE-4`, `RTE-5` | None supplied | None; no intervention or comparison evidence | Mechanisms for retaining and exposing source-linked assertions are implemented. The claim does not establish truth, reliable delivery, activation, or improved future performance. | Runtime account omitted the prompt hook's additional-context consumer; corrected here. Deployment and outcome remain unknown. |

No claim of a universal truth checker, independent oracle, or reliable knowledge production was found in the supplied claim record. The explicit evaluation route tests retrieval against operator-authored expected IDs and strings, but that reference criterion is not a truth check and its output has no automatic consumer that changes memory.

## Bounded conclusion

`mem` imports records into a durable journal and can form source-linked factual assertions for a curated Git-backed store. The transformation from event text to fact statement is indeterminate between semantic restatement and meaning-changing paraphrase on the supplied evidence. The system's evidence gate verifies a cited excerpt occurs in its source event, and its domain validator checks memory structure and state invariants. Neither establishes the source proposition's truth or an independent warrant. Pipeline acceptance means a candidate passed extraction/disposition and publication gates; it is not evidence-consuming acceptance against a named truth criterion and intended use.

Search and reranking decide which stored statements are returned and in what order. The prompt hook can pass selected facts as advisory `additionalContext` to a host under its hook protocol, while writeback can place selected statements in a project instruction file. Those routes provide operational influence paths, but deployment activation, actual model reliance, and downstream behavior are unobserved. Explicit changes rely on requester-supplied assertions. Tidy can withdraw facts based on duplicate or session-only judgments; its criteria concern memory utility and persistence, not truth. The held-out evaluator scores retrieval against a supplied rubric and makes no automatic change. No supplied execution evidence shows any route operated, produced a true claim, improved future capacity, or caused better task outcomes.

## Shared records


### Operative objects

#### EPI-OBJ-1 — Tidy findings

Source-native identity and form: a transient report of fact IDs judged duplicate or session-only, with an optional applied outcome. Storage substrate: CLI/report output; when applied, related retraction and suppression state is committed in `OBJ-2`. It is produced from `OBJ-2` facts by the tidy heuristics or optional LLM classifier. Closest supplied record: `OBJ-2` contains the facts it assesses, but not this distinct evaluator result. `SRC-2`, `src/tidy.rs`.

> For each fact decide whether it is LASTING: still true and useful to a new teammate weeks from now, in a different task.
> --- `src/tidy.rs:55-55` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

> Without `--apply` nothing changes. With it, every listed fact is
> //! forgotten in one commit: retracted in its entity file and suppressed in
> //! `state/controls.json` with the reason, so it disappears from every read
> //! and consolidation never re-adds it.
> --- `src/tidy.rs:12-15` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

#### EPI-OBJ-2 — Retrieval evaluation rubric

Source-native identity and form: caller-supplied JSON cases containing a query, expected fact IDs, optional required/forbidden strings, and optional project. Storage substrate: external rubric file read for one evaluation. It supplies comparison outcomes for search results and is not a stored claim set. No supplied counterpart; `OBJ-1` and `OBJ-2` provide evaluated inputs, not this criterion. `SRC-2`, `src/evaluation.rs`.

> A case passes when every
> //! expected id is in the top `limit` hits, every `must_include` string
> //! appears in them, and no `must_not_include` string does.
> --- `src/evaluation.rs:5-7` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

### Routes

#### EPI-RTE-1 — Prompt-hook fact injection

Endpoints: `OBJ-2` facts to the host hook's `additionalContext` output. Principal: installed host invokes the hook; `mem` selects facts and formats context. Context is the current prompt, project, and resolved memory store. Selection requires a prompt with at least three words, then matching meaningful terms; the output is capped at six facts. Immediate return is a JSON hook response; later read-back is inapplicable to the response itself, while underlying facts remain in `OBJ-2`. Invalidation/expiry: response is per invocation and is not retained by `mem`; host lifetime is outside the boundary. Activation and effect on model behavior are unobserved. `SRC-2`, `src/hook.rs`.

> // Injected context has to earn its place: a fact must share at least
>     // two of the prompt's meaningful words (one when the prompt has only
>     // one), so a single incidental word match never pulls a fact in.
> --- `src/hook.rs:132-134` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

> let out = json!({"hookSpecificOutput": {"hookEventName": name, "additionalContext": text}});
>         writeln!(output, "{out}")
> --- `src/hook.rs:77-78` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

#### EPI-RTE-2 — Tidy classification and withdrawal

Endpoints: active `OBJ-2` facts to `EPI-OBJ-1`, with optional retraction/suppression changes back to `OBJ-2`. Principal: operator invokes tidy; lexical rules and optional LLM judge propose findings, and `--apply` controls publication. Context includes active fact statements and existing suppression/deletion controls. Immediate return is a report; later read-back is affected when changes are applied. Selection predicate is lexical near-duplicate/containment or LLM session-only classification. No expiry is stated. Activation of applied withdrawal is implemented in the store; use by a future consumer is unobserved. `SRC-2`, `src/tidy.rs`.

#### EPI-RTE-3 — Held-out retrieval evaluation

Endpoints: `EPI-OBJ-2` rubric and `OBJ-1`/`OBJ-2` search results to a per-case report. Principal: operator supplies rubric and invokes evaluation; code computes ranking metrics. It is a bounded test mode with an explicit expected-ID and string-match reference outcome. Immediate return is pass/fail and ranking report; no memory write or later read-back effect is implemented. No expiry applies to the external rubric; the report is invocation output. It can inform later operator choice, but no automatic consumer or behavioral effect is established. `SRC-2`, `src/evaluation.rs`, `src/cli.rs`.


### Claims

### Evidenced absences

### Behavioral-authority paths

none declared in this member
