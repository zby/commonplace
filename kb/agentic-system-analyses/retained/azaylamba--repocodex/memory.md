---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "RepoCodex memory: repository concept persistence, path-selected explanations, direct reads, draft mining and deterministic retirement, with consumer-specific trust limits."
run-id: AAS-2026-11-08-repocodex-bf22ac3623d8-01
source-identity: https://github.com/azaylamba/repocodex
reviewed-boundary: "96978e292fcb3b100f53ac024b353e1b8b2c8af4"
---

# RepoCodex memory report

## Boundary and evidence

RepoCodex retains explanations and checkable metadata in repository Markdown. This report includes the shipped skills, CLI, MCP tools, persistence helpers, retrieval, bootstrap, checking, patching, relocation, repair, audit/GC and enforcement callers. It follows the whole-system boundary in `boundary.md`. External hosts, provider state, actual consuming repositories and the external OKF specification remain excluded. Their exclusion prevents claims about host compaction, model compliance, deployment, historical memory quality or independent OKF conformance.

All source evidence is SRC-1 at the reviewed commit. Direct source reads covered the complete files in the table below, including newly inspected schema, metrics and impact helpers. Implementation and doctrine/design are distinguished; no target execution, test execution, supplied deployment trace or causal experiment supports the account. The supplied runtime orders the investigation but is not treated as an inspection limit. In particular, the reverse-index implementation corrects a potentially misleading reading of its retrieval description.

| Entry point or memory operation | Directly inspected source paths (SRC-1) | Record coverage and limits |
| --- | --- | --- |
| CLI dispatch and optional service registration | `src/repocodex/cli.py`, `src/repocodex/mcp_server.py` | [RT-CMP-command-engine](runtime.md#rt-cmp-command-engine), [MEM-RTE-concept-read](#mem-rte-concept-read); all registered MCP tools checked, not only get_context |
| Concept loading, sharding, serialization and writes | `src/repocodex/store/bundle.py`, `src/repocodex/schema.py`, `src/repocodex/commands/write.py`, `src/repocodex/engine/gate.py` | [RT-OBJ-concept-body](runtime.md#rt-obj-concept-body), [RT-OBJ-concept-frontmatter](runtime.md#rt-obj-concept-frontmatter), [RT-RTE-memory-write](runtime.md#rt-rte-memory-write); filesystem/Git substrate, not an opaque vector store |
| Path read-back and index generation/checking | `src/repocodex/retrieval.py`, `src/repocodex/commands/context.py`, `src/repocodex/store/reverse_index.py` | [RT-RTE-context-read](runtime.md#rt-rte-context-read), [MEM-OBJ-reverse-index](#mem-obj-reverse-index), [MEM-CLM-context-selection](#mem-clm-context-selection); no host-window eviction inference |
| Catalog and write history | `src/repocodex/store/bundle.py`, `src/repocodex/retrieval.py`, `docs/memory.md` | [MEM-OBJ-context-catalog](#mem-obj-context-catalog), [MEM-OBJ-context-log](#mem-obj-context-log) |
| History/comment mining | `src/repocodex/commands/bootstrap.py` | [RT-RTE-bootstrap-drafts](runtime.md#rt-rte-bootstrap-drafts); automatic copied draft prose, not observed model synthesis |
| Checking and intent-side graph | `src/repocodex/commands/validate.py`, `src/repocodex/engine/impact.py` | [RT-RTE-validate-change](runtime.md#rt-rte-validate-change); detailed matching, ratchet and contradiction correctness relies on supplied runtime findings, not an exhaustive helper audit here |
| Anchor repair and identity maintenance | `src/repocodex/commands/reconcile.py`, `src/repocodex/commands/relocate.py`, `src/repocodex/commands/repair.py` | [RT-RTE-anchor-patch](runtime.md#rt-rte-anchor-patch), [RT-RTE-relocate-identity](runtime.md#rt-rte-relocate-identity), [RT-RTE-agent-repair](runtime.md#rt-rte-agent-repair); child model/tools and outputs unobserved |
| Screening, optional judgments and withdrawal | `src/repocodex/commands/audit.py`, `src/repocodex/commands/advisory.py` | [RT-RTE-review-audit](runtime.md#rt-rte-review-audit); imported findings remain proposals, GC changes status |
| Diagnostic trace retention and later consumption | `src/repocodex/metrics.py`, `src/repocodex/commands/context.py`, `src/repocodex/commands/validate.py`, `src/repocodex/commands/reconcile.py` | [MEM-OBJ-metrics](#mem-obj-metrics), [MEM-RTE-metric-readback](#mem-rte-metric-readback); diagnostic reuse is not automatic explanation revision |
| Installed policy, authoring and review | `src/repocodex/commands/install.py`, `src/repocodex/data/skills/repocodex-coding/SKILL.md`, `src/repocodex/data/skills/repocodex-review/SKILL.md`, `src/repocodex/data/hooks/pre-commit`, `src/repocodex/data/action/repocodex.yml`, `src/repocodex/data/plugin/hooks/claude-pre-commit`, `src/repocodex/data/plugin/hooks/cursor-pre-commit`, `plugin/plugin.json` | [RT-RTE-install-wiring](runtime.md#rt-rte-install-wiring), [RT-BAP-check-enforcement](runtime.md#rt-bap-check-enforcement); deployment and client loading uninspected |
| Product account and labels | `docs/memory.md`, `docs/architecture.md` | Doctrine/design checked against the implementation above; no independent benefit evidence |

Root hook/rule/plugin distribution counterparts and test suites were not independently re-audited here; supplied boundary/runtime findings establish their declared role. Installed packaged callers, rather than hypothetical external API users, establish the covered loop. Provider-side session retention, parameter changes and exact model version remain uninspected as recorded in [RT-CMP-coding-agent](runtime.md#rt-cmp-coding-agent). There is no included opaque alternative memory service left implicit: the inspected persistence is readable files; host/provider state is outside the boundary, not evidence of absent retention there.

## Core ideas

1. **The same page has two authorities.** Its body explains why to an agent; its parsed anchors, claims and lifecycle status control fixed-rule checking and retrieval. A live pin is not a semantic truth certificate. The existing object split is retained in [RT-OBJ-concept-body](runtime.md#rt-obj-concept-body) and [RT-OBJ-concept-frontmatter](runtime.md#rt-obj-concept-frontmatter).
2. **Read-back is path requested, not unsolicited injection.** A foreground agent requests intended edit paths; code selects pinned concepts and sends full bodies, plus linked/catalog titles. Related-body expansion is an agent decision. Ranking changes order but does not impose a token budget. A direct identity tool is an alternate route, including to draft/deprecated material ([MEM-CLM-context-selection](#mem-clm-context-selection), [MEM-RTE-concept-read](#mem-rte-concept-read)).
3. **Curation has several admission mechanisms.** Agent-authored writes, deterministic bootstrap drafts, direct reanchor patches, relocation and GC do not pass the same checks. Human task initiation is not per-content approval. Stable-body replacement requests supersession/rationale, but prior deprecation can survive rejection of its replacement ([RT-RTE-memory-write](runtime.md#rt-rte-memory-write)).
4. **Retained reasons are not always delivered reasons.** The stored frontmatter can retain supersession rationale and source pointers. Ordinary context returns the body and selected metadata, not the complete rationale/anchor record; direct MCP read does return complete frontmatter. Diagnostic traces have a different consumer and do not become explanatory memory merely because they persist ([MEM-OBJ-metrics](#mem-obj-metrics)).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-reverse-index
Label: Generated reverse index

Symbolic path-to-concept-identity map rendered as Markdown under `.repocodex/reverse-index.md`, or `.repocodex/reverse-index/<escaped-package>.md` for shards. This is access metadata, not explanation content or learned parameters. It derives from concept anchor paths and is regenerated after writes/patches/relocation/bootstrap. Persisted copies are consumed by index-sync checks; retrieval's `merged_index` instead rebuilds the expected mappings from current concepts. Thus a missing/stale committed map does not itself prove missing path retrieval, although it can cause a configured check denial. Material paths: SRC-1 implementation, `src/repocodex/store/reverse_index.py`, `src/repocodex/retrieval.py`, `src/repocodex/commands/validate.py`.

Distinct from [RT-OBJ-concept-frontmatter](runtime.md#rt-obj-concept-frontmatter): that object supplies pins; this generated artifact stores derived lookup metadata outside the concept. The supplied record mentions indexes but does not declare them as its own referent.

> def merged_index(repo: Path) -> dict[str, list[str]]:
>     """Return the union of expected reverse-index mappings across all shards."""
>     merged: dict[str, list[str]] = defaultdict(list)
>     for context_root in discover_context_roots(repo):
>         for path, identities in expected_index(context_root, repo).items():
> --- `src/repocodex/store/reverse_index.py`

> committed = load_reverse_index(context_root, repo, staged=staged)
> expected = expected_index(context_root, repo)
> if committed != expected:
> --- `src/repocodex/store/reverse_index.py`

#### MEM-OBJ-context-catalog
Label: Context catalog

Directory `index.md` files in `.context` shards retain Markdown title/description links; the root catalog also carries the bundle version. These mix human-readable descriptions with symbolic link targets parsed for sibling discovery. They are derived display/navigation summaries, not opaque semantic payloads. `write_concept` updates catalogs; relocation removes the old link and adds the new one. `update_catalog` returns early if the leaf string already occurs, so updating a concept need not refresh its catalog description. Retrieval can substitute the currently loaded title/type, but it does not thereby refresh the stored catalog. SRC-1 implementation: `src/repocodex/store/bundle.py`, `src/repocodex/retrieval.py`, `src/repocodex/commands/relocate.py`.

Distinct from [RT-OBJ-concept-body](runtime.md#rt-obj-concept-body): catalogs point to bodies; they are not typed concept bodies. The loader reserves their filename.

> if leaf in current:
>     return
> --- `src/repocodex/store/bundle.py`

> siblings.append({"identity": identity, "title": title, "type": None})
> --- `src/repocodex/retrieval.py`

#### MEM-OBJ-context-log
Label: Context write log

Natural-language event lines in each shard's `log.md`, grouped by UTC day. `write_concept`, deprecation and relocation append identities/actions, not full before/after bodies or the full reasoning behind a revision. This is an automatically derived operation history, not the original task transcript. It is separately reserved from concept loading. A documented reader can open it, but no inspected retrieval/validation consumer uses its contents to select concepts or update explanations. SRC-1 implementation: `src/repocodex/store/bundle.py`, `src/repocodex/commands/relocate.py`; doctrine/design: `docs/memory.md`.

No counterpart after comparison with the supplied concept objects: this log is neither [RT-OBJ-concept-body](runtime.md#rt-obj-concept-body) nor its symbolic metadata.

> RESERVED = {"index.md", "log.md"}
> --- `src/repocodex/store/bundle.py`

> append_log(root, f"wrote {doc.identity} ({type_str(doc.frontmatter.type)})")
> --- `src/repocodex/store/bundle.py`

#### MEM-OBJ-metrics
Label: Metrics event sink

Symbolic timestamped JSONL events at `.repocodex/metrics.jsonl` by default, with `REPOCODEX_METRICS_SINK` allowing another absolute or repository-relative path. Context writes requested paths and estimated body tokens; validation writes drift and outcome/latency fields; replace-path patching writes a reconcile event marked `false_drift`. These are selected event records, not raw model traces, complete command transcripts or derived prose. Installation adds the default sink to `.gitignore`. Later validation loads events to compute a diagnostic ratio, not to change gate policy or concept bodies. SRC-1 implementation: `src/repocodex/metrics.py`, `src/repocodex/commands/context.py`, `src/repocodex/commands/validate.py`, `src/repocodex/commands/reconcile.py`, `src/repocodex/commands/install.py`.

Distinct from the inputs and outputs of [RT-RTE-validate-change](runtime.md#rt-rte-validate-change): this is the retained diagnostic store that route only mentions. No supplied operative-object counterpart.

> line = {"event": event, "at": utc_now(), **payload}
> with metrics_path(root).open("a", encoding="utf-8") as handle:
>     handle.write(json.dumps(line) + "\n")
> --- `src/repocodex/metrics.py`

### Routes

#### MEM-RTE-concept-read
Label: Direct concept identity read

MCP `read_concept(identity)` → load all concepts → return first identity match with JSON frontmatter/body. Owner/selector is deterministic wrapper code; the requesting host chooses identity. No writing or admission occurs, so human content approval is inapplicable. Distinct from the path-ranked progression of [RT-RTE-context-read](runtime.md#rt-rte-context-read), which mentions this alternative but does not trace it separately. Both consume the existing concept objects; no duplicate object is declared. SRC-1 implementation: `src/repocodex/mcp_server.py`, `src/repocodex/store/bundle.py`.

- Immediate return: Engine version, requested identity, complete model-dumped frontmatter and body, or not_found; obtains the version through context_for with an empty path list, which also records a context metric.
- Later read-back: Persisted concept content reaches a later requesting host invocation, including rationale and anchors omitted by path context.
- Delegated visibility: Tool response is available to its host; any onward delegation is uninspected — external host policy is excluded.
- Selection predicate: Exact identity equality, first match in shard discovery/file iteration order; no draft/deprecated filter or body truncation here.
- Invalidation or expiry: Identity missing from disk returns not_found; deprecation and stale_after do not deny this read.
- Activation or effect: Makes retained text and metadata available for model interpretation; changed decisions are not established.
- Evidence limits: Caller/tool invocation and host compliance unobserved; repeated identities across shards can resolve differently from path retrieval's by_id dictionary.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> for doc in load_concepts(_root()):
>     if doc.identity == identity:
>         return {
> --- `src/repocodex/mcp_server.py`

> "frontmatter": json.loads(
>     # round-trip via model dump
>     json.dumps(doc.frontmatter.model_dump(mode="json"), default=str)
> ),
> "body": doc.body,
> --- `src/repocodex/mcp_server.py`

#### MEM-RTE-metric-readback
Label: Diagnostic metric read-back
Part of: [RT-RTE-validate-change](runtime.md#rt-rte-validate-change)

Context/validation/patch operations append [MEM-OBJ-metrics](#mem-obj-metrics) → a later validation invokes false_drift_rate → reads persisted events → computes bounded false/drift ratio → returns it in the verdict and appends it to the validation event. Code owns acquisition, admission and derivation; no human approves individual events. This is an open diagnostic calculation, not candidate knowledge admission or a semantic answer oracle. Distinct from [RT-RTE-validate-change](runtime.md#rt-rte-validate-change): it expands the cross-invocation diagnostic subroute without replacing the validation referent. SRC-1 implementation: `src/repocodex/metrics.py`, `src/repocodex/commands/validate.py`, `src/repocodex/commands/reconcile.py`.

- Immediate return: Numeric rate to validate, then verdict JSON to caller.
- Later read-back: Earlier drift and reconcile events are read from the file; context events and previous validation-rate fields are retained but not counted by this calculation.
- Delegated visibility: No internal model call; the host sees the verdict field.
- Selection predicate: event equals drift increments denominator; event equals reconcile with truthy false_drift increments numerator; zero drift returns zero, otherwise clamp ratio at one.
- Invalidation or expiry: Blank/malformed JSONL lines skipped; no time-window expiry in this reader. Changing/removing the sink changes the available history.
- Activation or effect: Changes the diagnostic value returned; no inspected path uses this value to revise concepts or blocking policy.
- Evidence limits: A replace_path application labels itself false drift; ratio does not independently verify diagnosis or pair each reconcile to a particular drift. No observed improvement established.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if event.get("event") == "drift":
>     drifts += 1
> elif event.get("event") == "reconcile" and event.get("false_drift"):
>     false += 1
> --- `src/repocodex/metrics.py`

> derived_false_drift = false_drift_rate(root)
> --- `src/repocodex/commands/validate.py`

### Claims

#### MEM-CLM-context-selection
Label: Scoped context is selection, not compaction

The scoped-context design claim is supported as requested path selection, full-body delivery and title-only expansion hints, not a hard token budget or host compaction guarantee. All matching eligible concepts are sorted and returned; `chars / 4` measures the delivered bodies rather than limiting them. Ranking rewards the presence of sources and verified stamps, not their correctness or authenticated authority. Related titles/catalog siblings do not run the selected-body status filter. This qualifies [RT-RTE-context-read](runtime.md#rt-rte-context-read), without denying that its selected bodies exclude drafts/deprecated concepts by default. SRC-1 implementation: `src/repocodex/retrieval.py`, `src/repocodex/commands/context.py`; doctrine/design: `docs/architecture.md`.

> - Keep retrieval token-cheap (reverse index + staged reads; never dump `.context/`).
> --- `docs/architecture.md`

> if doc.frontmatter.sources:
>     score += 100.0
> if doc.status == ConceptStatus.stable:
>     score += 20.0
> if doc.frontmatter.verified:
>     score += 10.0
> --- `src/repocodex/retrieval.py`

> chars = sum(len(item.get("body") or "") for item in payload.get("concepts") or [])
> tokens_per_turn = chars / 4.0
> --- `src/repocodex/commands/context.py`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-OBJ-concept-body](runtime.md#rt-obj-concept-body)

Storage is `.context/<identity>.md` within discovered shards, intended for versioning with source code. Natural-language explanations may contain markdown links that also serve a symbolic consumer: `linked_identities` extracts body links for related discovery, impact and GC inbound-link calculation. That consumer does not interpret the explanation's meaning. Existing authored bodies, copied comment/history drafts and future agent-authored bodies share storage, not an established common provenance. Arbitrary imported concepts' initial authorship remains local uncertainty; generated/verified metadata is caller-supplied information, not authentication.

SRC-1 implementation: `src/repocodex/engine/impact.py`, `src/repocodex/commands/audit.py`, `src/repocodex/schema.py`; doctrine/design: coding skill.

> for match in LINK_RE.finditer(doc.body):
>     identity = resolve_link(doc.identity, match.group(1))
> --- `src/repocodex/engine/impact.py`

#### On [RT-OBJ-concept-frontmatter](runtime.md#rt-obj-concept-frontmatter)

Lineage and reason fields persist through parse/serialize: source resources, generated/verified actor stamps, supersedes and rationale. Schema permits additional fields and open type strings. A stamp's presence affects retrieval rank; it does not establish human admission or verified semantic truth. The ordinary context response includes identity/title/type/status/tags/sources/body but omits rationale, supersedes, verification anchors and verified stamps. Their stored presence is therefore not evidence that ordinary context conveyed them. [MEM-RTE-concept-read](#mem-rte-concept-read) provides the alternative complete frontmatter channel. SRC-1 implementation: `src/repocodex/schema.py`, `src/repocodex/retrieval.py`; doctrine/design: `docs/memory.md`.

> supersedes: str | None = None
> rationale: str | None = None
> --- `src/repocodex/schema.py`

> - A passing pin check does **not** write `verified`.
> --- `docs/memory.md`

#### On [RT-RTE-context-read](runtime.md#rt-rte-context-read)

Read-back is pull/request driven: intended edit paths supplied by the foreground agent trigger automatic code selection, not an independent background push. Exact path lookup targets the retained pins. There is no top-k/token cutoff in the inspected selector, and no summarization/truncation of selected bodies. The response excludes other bodies, but does not remove prior host turns. Link/catalog title delivery is followed by optional agent-selected expansion. Source anchors: SRC-1 `src/repocodex/retrieval.py`, `src/repocodex/commands/context.py`, coding skill. See [MEM-CLM-context-selection](#mem-clm-context-selection) for budget and trust evidence and [MEM-OBJ-reverse-index](#mem-obj-reverse-index) for reconstructed-versus-persisted index consumption.

> selected.sort(key=lambda doc: rank_score(doc, root), reverse=True)
> --- `src/repocodex/retrieval.py`

> Read returned concept bodies. Related pages are titles only — open a body only if the edit might touch that scenario.
> --- `src/repocodex/data/skills/repocodex-coding/SKILL.md`

#### On [RT-RTE-memory-write](runtime.md#rt-rte-memory-write)

Write agency is caller-authored Markdown followed by software admission and physical file serialization; no per-content human approval gate is inserted. Stable-body edits without supersession are rejected, and supersession requires rationale. The reason is retained as frontmatter, not automatically delivered by ordinary context. Direct filesystem editing and bootstrap/patch/relocation alternatives qualify any claim that this mechanism governs all persistence. Rejection can still leave the predecessor deprecated because of ordering, reducing later default retrieval before the replacement exists. This corroborates, rather than corrects, runtime's warning. SRC-1 implementation: `src/repocodex/commands/write.py`, `src/repocodex/store/bundle.py`.

> if incoming.frontmatter.supersedes and incoming.frontmatter.rationale:
>     return None
> --- `src/repocodex/commands/write.py`

The deprecation and anchorless branches have retained passages in the supplied route. No need to repeat them here. Gate matching establishes local source-term correspondence, not prose correctness; review remains a separate requested semantic check.

#### On [RT-RTE-bootstrap-drafts](runtime.md#rt-rte-bootstrap-drafts)

This is an automatic trace-fed transformation for history-derived candidates: repository commit subject/first changed path → regex-selected note/terms and commit source pointer → gated draft body → later draft-enabled context or direct read → host interpretation. Comment/document-derived candidates have authored repository text as origin; the attached last-touch commit pointer is not proof that the note is that commit's rationale. Both paths retain the copied note, not a reconstruction of all original criticism, outcome or alternatives. The producer does not invoke a model or require per-candidate human approval. Gate rejection prevents that candidate write; no-source candidates are rejected. Draft expiry is only acted on through GC. SRC-1 implementation: `src/repocodex/commands/bootstrap.py`; later routes: [RT-RTE-context-read](runtime.md#rt-rte-context-read), [MEM-RTE-concept-read](#mem-rte-concept-read).

> if not any(token in lower for token in ("why:", "because", "decision:", "do not ")):
>     continue
> --- `src/repocodex/commands/bootstrap.py`

> body=f"Bootstrapped from `{rel}`.\n\n{note}\n",
> --- `src/repocodex/commands/bootstrap.py`

Automatic retention creates potential later behavior-shaping input. Neither exercised learning nor improved future capacity follows from that chain alone. Host-authored revisions following validation are afforded/requested through the skill; actual trace-responsive model revision remains unobserved.

#### On [RT-RTE-review-audit](runtime.md#rt-rte-review-audit)

Audit emits sampled stable bodies and matched source regions to an out-of-band reviewer. Imported findings produce returned proposal dictionaries, not automatic persisted explanation changes. GC is the separate automatic admission mechanism for withdrawal: code computes inbound body links and live anchor hits, or expired draft date, then deprecates content without per-item human approval. Files and catalog entries remain; default selected-body retrieval omits the retired concept, while related-title and direct-identity paths can still expose it. No hard deletion or universal access withdrawal follows. SRC-1 implementation: `src/repocodex/commands/audit.py`, `src/repocodex/store/bundle.py`, `src/repocodex/retrieval.py`, `src/repocodex/mcp_server.py`.

> orphan = doc.identity not in inbound and not live_anchor
> expired_draft = doc.status == ConceptStatus.draft and _expired(doc.frontmatter.stale_after)
> if orphan or expired_draft:
>     deprecate_concept(repo, doc.identity, reason="gc")
> --- `src/repocodex/commands/audit.py`

#### On [RT-RTE-agent-repair](runtime.md#rt-rte-agent-repair)

Working-context isolation is only process-level evidence here. A new external harness receives a static prompt and repository cwd; no parent conversation, lost list or candidate payload is passed in argv. It can recover repository state through its own tools, but what it actually reads, retains or returns to a model is uninspected. Captured child stdout/stderr is not returned in RepoCodex's result. This resembles a separate task frame only at the process interface, not a demonstrated model-window isolation or compaction mechanism. SRC-1 implementation: `src/repocodex/commands/repair.py`; the supplied route retains subprocess passages.

## Write side

The mechanisms use different admission controls, not merely different file I/O APIs:

| Mechanism | Author/proposer and admission | Retained change, rejection and later consumer |
| --- | --- | --- |
| Ordinary write/reconcile/MCP write | Caller authors text; code parses, checks supersession/rationale, required claims and new identity prefix, then gates anchored input. Human identity/approval not resolved per call. | Body/frontmatter, catalog/log and derived indexes; anchorless input bypasses evaluate_write. Rejected superseding candidate can already have deprecated predecessor. Future context and checking reload files. [RT-RTE-memory-write](runtime.md#rt-rte-memory-write) |
| Bootstrap | Deterministic mining of repository text/history; commit evidence and gate admit candidates automatically. | Drafts with copied notes, sources and stale_after; default context excludes them. No per-item approval, model synthesis or reliable rationale validation. [RT-RTE-bootstrap-drafts](runtime.md#rt-rte-bootstrap-drafts) |
| Reanchor patch | Caller proposes/applies JSON; existing concept/index/keys control application, not write gate. | Path/optional terms overwritten, indexes regenerated and metric appended. No transactional reversal. Later validation and retrieval consume changed pins. [RT-RTE-anchor-patch](runtime.md#rt-rte-anchor-patch) |
| Relocate | Caller chooses identity or bulk mismatches; code checks prefix suitability and occupied targets. | Same bytes at a new identity, catalog/log/index updated; old path unlinked first. Inbound body-link repair is not performed by this implementation. [RT-RTE-relocate-identity](runtime.md#rt-rte-relocate-identity) |
| Review/advisory | External model may judge prose/diff; library caller can supply judgments. CLI/Action do not supply such judgments. | Return-only advisory findings/proposals, not an admission gate for semantic content. [RT-RTE-review-audit](runtime.md#rt-rte-review-audit) |
| Audit GC | Code decides orphan/no-live-anchor or expired draft; no human per-item approval. | Deprecated status retained on disk; selective read exclusion, not deletion. Same route, separate mechanism. [RT-RTE-review-audit](runtime.md#rt-rte-review-audit) |
| Repair subprocess | Caller starts operation; external agent proposes actual edits if it acts. RepoCodex admission applies only if commands are used. | Written result and model behavior unobserved; no post-child validation certificate. [RT-RTE-agent-repair](runtime.md#rt-rte-agent-repair) |
| Install | Operator starts setup; package selects fixed instruction/check/config contents. No per-concept approval implied. | Skills/rules/hooks/Action/config persist for later client/check operations; not accumulated task learning. [RT-RTE-install-wiring](runtime.md#rt-rte-install-wiring) |
| Metrics/log/catalog/index maintenance | Code admits derived metadata/events automatically. | Navigation, diagnostics and operation history, not synthesized semantic explanations. New operative-object records above trace consumers. |

Starting a coding task or invoking bootstrap is not approval of each retained statement. Conversely, lack of a per-record human gate does not mean a person could not author, edit or veto repository changes outside these commands. The inspected architecture explicitly treats per-record human approval as a non-goal (SRC-1 `docs/architecture.md`), while actual external repository review policy remains uninspected.

Raw model transcripts and alternative checkpoint summaries are not produced by the inspected storage routes. Bootstrap transforms commit subjects, not a full action/outcome transcript; metrics retain selected operational fields; the log retains operation labels. The trace-to-derived-to-later-consumer chain is known for bootstrap and diagnostics, but neither proves improved explanatory quality. Stable supersession preserves a rationale field; ordinary context does not automatically deliver that field. Original imported content provenance remains unresolved without suppressing these known later transformations.

## Read-back

**Primary consumer: coding agent.** Requested edit paths select pins from current concept-derived mappings; status filtering removes draft bodies by default and deprecated bodies always on this path; metadata/churn ranking orders all eligible results. CLI/MCP delivers body text through JSON. Sources and stamps influence order, not authenticated authority. Related/catalog titles are a discovery hint, with body expansion chosen by the agent. No budget-limited selection, automatic summarization, host tail preservation or eviction is implemented by these inspected paths ([MEM-CLM-context-selection](#mem-clm-context-selection)). This is keeping unrelated material out of a new response, not removing already accumulated context. The stack-frame analogy does not fit ordinary retrieval: no task frame is popped and no summary replaces it.

**Alternate consumer channel: direct identity tool.** MCP `read_concept` returns body and complete frontmatter, including deprecated or expired content still on disk. Its identity is a requested address, not a topical relevance selector. This route can recover reason/anchor details omitted by context; a filesystem reader is also afforded by the documented bundle layout, but unspecified library users are not counted as wired routes ([MEM-RTE-concept-read](#mem-rte-concept-read)).

**Other implemented consumers.** Validation loads stable concepts and consumes anchors/claims/status with fixed rules; `intent_impact` uses retained body links to emit identities rather than explanatory bodies. Audit selects stable samples by seed/size and emits body/source-region screening payloads for out-of-band review. GC consumes inbound links/status/dates/anchor results. These are distinct from model interpretation and cannot certify narrative truth. The installed hook and required Action consume symbolic verdicts and enforce configured check policy, not whether the agent read the bodies. Their posture/exemption limits remain those of [RT-RTE-validate-change](runtime.md#rt-rte-validate-change).

Metrics are request-adjacent automatic recording but not unsolicited memory delivery. A later validate explicitly reads the sink for a diagnostic ratio; no inspected branch uses that ratio to choose a semantic update. Catalogs supply title navigation; generated index files supply sync-check inputs; logs have a documented human-readable surface but no established automatic behavioral consumer. Storage capabilities alone do not add consumer routes.

## Integration issues

1. **Index-consumption correction/clarification.** [RT-RTE-context-read](runtime.md#rt-rte-context-read) describes reverse-index selection and an index-completeness limit. [MEM-OBJ-reverse-index](#mem-obj-reverse-index) shows that merged_index rebuilds expected mappings from current concepts; it does not load persisted reverse-index files. Generated files are the checked copies, not the context lookup source. Reconciliation should avoid implying a stale committed map necessarily hides a concept from context. The distinction affects both retrieval reliability and enforcement explanations.
2. **Withdrawal is route-specific.** [RT-RTE-context-read](runtime.md#rt-rte-context-read) correctly filters selected bodies, but related titles/catalogs and [MEM-RTE-concept-read](#mem-rte-concept-read) can still expose deprecated material. [RT-RTE-review-audit](runtime.md#rt-rte-review-audit) retires by status, not deletion. No conflict in the scoped runtime finding; a universal withdrawal claim would be unsupported.
3. **Potential overlap, not a duplicate declaration.** [MEM-RTE-concept-read](#mem-rte-concept-read) expands the explicitly mentioned direct identity alternative within [RT-RTE-context-read](runtime.md#rt-rte-context-read); retain it as the separately traced operation or reconcile the overlap explicitly. [MEM-RTE-metric-readback](#mem-rte-metric-readback) expands diagnostic reuse mentioned by [RT-RTE-validate-change](runtime.md#rt-rte-validate-change). New operative objects describe stores not separately declared there; existing concept objects received annotations instead of new IDs.
4. **Unresolved identity uniqueness across shards.** SRC-1 `src/repocodex/store/bundle.py` derives identities relative to each shard; `src/repocodex/retrieval.py` builds by_id with a dictionary, while direct reading and writing search first matches. No uniqueness admission check is present in the inspected paths. If distinct shards contain the same identity, path retrieval can select the later-loaded document while direct read/write choose the earlier one. This prevents a universal shard-qualified identity or unambiguous-consumer claim; no evidence establishes that such a collision occurred. Concerns [RT-OBJ-concept-frontmatter](runtime.md#rt-obj-concept-frontmatter), [RT-RTE-memory-write](runtime.md#rt-rte-memory-write), [MEM-RTE-concept-read](#mem-rte-concept-read).
5. **Unobserved host activation and initial provenance.** The skill requests reading, revision and stopping behavior, but no trace establishes compliance or semantic improvement. Per-import initial authorship and host/provider retained state remain unknown. These limits concern [RT-CMP-coding-agent](runtime.md#rt-cmp-coding-agent), [RT-BAP-memory-consumption](runtime.md#rt-bap-memory-consumption) and the concept annotations; they do not negate known deterministic transformations.

## Limitations and checks

The analysis establishes source-wired persistence and later consumption opportunities, not that a host used memory, changed its decisions, repaired it successfully or learned a beneficial policy. No conclusion about model parameter learning, exercised self-improvement or long-term explanation quality is supported. Direct reads covered dispatch, registered tools, packaged hook/Action callers and alternate admission routes, but did not independently audit every matching/test helper or root distribution copy. Supplied runtime findings remain explicitly identified where used.

Source identity was rechecked with Git: HEAD equals 96978e292fcb3b100f53ac024b353e1b8b2c8af4, with clean status at inspection. The frozen SRC-1 identity and run identity were preserved. Method identity for this invocation is the supplied job, worker rules, member type, collection and complete record contract; no additional method revision is inferred. Countercases checked before settling claims included regenerated versus loaded indexes, direct deprecated reads, related-title filtering, anchorless writes, pre-rejection deprecation, patch bypasses, rationale omission and the absence of a retrieval cutoff in the complete selector.

Validation: the required role-specific commonplace-validate check passed on this candidate. This establishes deterministic form and quotation occurrence, not semantic verification or acceptance.
