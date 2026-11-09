---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "RepoCodex runtime baseline: agent-directed repository-memory loop, deterministic checks, alternate admission paths and external repair at the frozen revision."
run-id: AAS-2026-11-08-repocodex-bf22ac3623d8-01
reviewed-boundary: "96978e292fcb3b100f53ac024b353e1b8b2c8af4"
---

# RepoCodex runtime report

## Runtime account

RepoCodex supplies instructions and deterministic repository commands, not the enclosing coding-agent runtime. A host agent receives a coding task, retrieves retained explanations for intended edit paths, edits code, validates, repairs or authors memory as needed, and commits code with memory and indexes. The host owns next-step selection and code execution; RepoCodex computes retrieval, admission and diagnostic results. Its skill requests compliance, but its executable checks do not enforce that context was read or that prose explains code correctly. The ordinary path is [RT-RTE-coding-loop](#rt-rte-coding-loop), supported by [RT-RTE-context-read](#rt-rte-context-read), [RT-RTE-memory-write](#rt-rte-memory-write) and [RT-RTE-validate-change](#rt-rte-validate-change). All evidence below is SRC-1 implementation or explicitly labelled doctrine/design, not an observed invocation.

### Ordinary invocation and boundaries

A consuming-repository operator first invokes installation, which copies rules, skills, hook and Action configuration ([RT-RTE-install-wiring](#rt-rte-install-wiring)). CLI commands use the process working directory as repository identity. Concepts have shard-relative identities and pinned code paths. The CLI returns JSON envelopes; MCP exposes functions using the same command implementations ([RT-CMP-command-engine](#rt-cmp-command-engine)). The foreground agent then follows the coding skill: request context for every intended edit path; inspect bounded plausible callers; edit; run `validate --diff`; use the verdict and `skipped_memory`, not just the result name, to decide whether to write, reanchor or reconcile. Its terminal product is a proposed/committed code change with `.context/` and reverse indexes. An actual agent's compliance, approval settings and successful commit remain unobserved.

Repository memory is persisted as Markdown in discovered `.context` shards, with catalogs, logs and generated reverse indexes. The later context invocation reloads retained material; this is not merely an expanding chat transcript. Natural-language bodies and symbolic frontmatter have different consumers ([RT-OBJ-concept-body](#rt-obj-concept-body), [RT-OBJ-concept-frontmatter](#rt-obj-concept-frontmatter)). Selection is by requested paths and reverse-index identities, with ranking and status filtering; related material is returned as titles, not automatically as bodies. The skill leaves the decision to open related bodies to the host agent. There is no inspected runtime-owned summary/compaction or isolated subagent frame in this path. Retrieval limits what is newly delivered; it does not evict earlier host context. Memory revision interpretation belongs to the memory specialist.

### Controls and forcing cases

Four forcing cases bound the load-bearing guarantees:

1. **Write admission is not a universal persistence barrier.** `write_memory` calls the anchor gate only when anchors exist; unanchored narrative is accepted, subject to the other write checks. Conversely, the gate function itself rejects no-anchor documents. CLI and MCP can reach the accepting branch with anchorless input. The first-touch ratchet requires pinning, so acceptance alone does not discharge uncovered-code obligations. A second ordering hazard is that superseded material is deprecated before the new candidate passes invariant-claim, prefix and anchor checks; a rejected replacement can therefore already have changed predecessor state ([RT-RTE-memory-write](#rt-rte-memory-write)).
2. **Reanchor is a separate admission path.** CLI `reconcile --apply-patch` accepts JSON and calls the patch writer directly; `validate --apply-patches` applies emitted patches. The patch writer changes path and optional terms without calling `evaluate_write`. MCP reconcile instead calls `write_memory`. Thus these routes cannot share an all-writes-gated guarantee. The direct JSON caller can supply a replacement rather than only replaying a trusted emitted patch ([RT-RTE-anchor-patch](#rt-rte-anchor-patch)).
3. **Blocking is posture-, acknowledgment- and caller-dependent.** Installation defaults to shadow posture, where only `skipped_memory` blocks. Other postures use the remaining deterministic reasons. A memory-exempt flag or label with accepted acknowledgment evidence clears reasons before posture evaluation. Plain CLI validation returns exit zero despite `blocking`; hook/check modes translate blocking into nonzero. MCP returns a verdict, leaving enforcement to its caller ([RT-RTE-validate-change](#rt-rte-validate-change)).
4. **Repair process success is not repaired-state success.** The repair driver validates, selects the first available external CLI, passes a static prompt and reports process status. It neither checks for a RECONCILE verdict before invoking nor revalidates afterward. Computed lost/candidate data is returned to the caller, not interpolated into the child prompt. The child can inspect the repository, but its actual discovery and compliance are external and unobserved ([RT-RTE-agent-repair](#rt-rte-agent-repair)).

These are source-traced forcing inputs/branches, not executed experiments. They challenge universal claims, not the existence of the ordinary path.

### Guarantee ownership and strength

| Guarantee or request | Owner and enforcement point | Strength and covered paths | Alternatives and required external contract | Conclusion statuses |
| --- | --- | --- | --- | --- |
| Read memory before editing, maintain why, repair before ending turn | Host agent interpreting installed coding skill | protocol; requested coding-skill loop | Direct editing, arbitrary shell writes and agents not loading skills are outside that protocol's executable enforcement. Host must load and follow it. | doctrine conclusion status: claimed; implementation conclusion status: wired; operation conclusion status: uninspected |
| Anchored write passes local term/region and claim checks | `write_memory` calling `evaluate_write` before writing candidate | invariant within that branch; CLI write and ordinary reconcile, MCP write/reconcile | Unanchored write, patch writer, bootstrap's direct storage call, relocation, deprecation and arbitrary host filesystem edits need separate treatment. Requires readable repository, Git/ripgrep behavior and caller use of the route. Not a guarantee of prose truth. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Deny commit/check on configured blocking result | CLI hook/check exit policy, portable hook, installed required Action | policy implemented by exit status; staged hook and configured CI diff checks | Shadow posture, acknowledgment override, direct JSON callers, plain CLI validation and absent/bypassed hooks differ. Requires installation, invocation, correct base and external branch-protection policy if merge denial is desired. | implementation conclusion status: wired; deployment conclusion status: uninspected |
| Agent narrative review cannot itself fail required verdict | Advisory envelope and separate advisory job | invariant of inspected advisory function and job separation | Deterministic contradictions may independently block; prose findings do not. Action invokes advisory without agent judgments; external review agent must provide judgment separately. | implementation conclusion status: wired; operation conclusion status: uninspected |

See [RT-CLM-executable-memory](#rt-clm-executable-memory) for the declared product description and [RT-RTE-review-audit](#rt-rte-review-audit) for the actual review/advisory distinction. No supplied trace establishes activation, benefit, reliability or latency. `context` estimates body tokens by characters divided by four, and validation records metrics; these are measurement mechanisms, not performance results (SRC-1, `src/repocodex/commands/context.py`, `src/repocodex/commands/validate.py`).

### Capability, grants and model boundary

The command surface can read repository files, invoke Git/ripgrep, write repository memory/configuration and start an external repair harness. That capability surface is not an observed grant set or an isolation guarantee. Inspected commands execute with the caller's operating-system permissions; the repair subprocess inherits execution context rather than receiving a RepoCodex-defined capability sandbox. The implementation sets cwd and captures stdout/stderr but defines no approval callback, tool allowlist or subprocess timeout there. Provider-native tools, model selection, shell approvals, remote workers, host callbacks and host context policy are external-harness matters, not demonstrated RepoCodex controls (SRC-1, `src/repocodex/commands/repair.py`).

The model-dependent component is [RT-CMP-coding-agent](#rt-cmp-coding-agent). No exact model or provider version is pinned by the inspected call path. Skills and retained explanations can change model inputs without changing parameters. Parameter mutation and mutable provider routing are uninspected, not evidence of fixed weights or absent learning. The deterministic engine has no inspected internal model call in context/write/validate/audit; the repair path starts a model-capable harness instead. All operation and benefits remain unobserved.

### Inspection coverage added

Within SRC-1's frozen tree, this member additionally read the complete `src/repocodex/engine/liveness.py`, `src/repocodex/engine/ratchet.py`, `src/repocodex/config.py`, `src/repocodex/data/plugin/hooks/claude-pre-commit`, `src/repocodex/data/plugin/hooks/cursor-pre-commit` and `src/repocodex/data/plugin/plugin.json`, and reread the command, retrieval, store, gate, packaged skill, hook and Action paths cited below. These supply implementation evidence, or doctrine/design for skill bodies. HEAD and clean status were checked without executing the target. No source ID, functional inclusion or source revision was changed. Supporting matching/relocation helpers were not exhaustively audited; region/relocation correctness beyond the inspected consumers is not established. Host/provider internals and real deployment remain outside the frozen evidence.

## Shared records

### Components

#### RT-CMP-command-engine
Label: RepoCodex command engine

Source-native Python command functions, Typer CLI and optional MCP wrappers; symbolic executable rules stored in package source. CLI repository root is `Path.cwd()`. MCP similarly uses its process cwd and returns dictionaries rather than CLI exit statuses. Storage functions perform local filesystem writes; subprocess interfaces include Git, ripgrep and external repair. SRC-1 implementation: `src/repocodex/cli.py`, `src/repocodex/mcp_server.py`, `src/repocodex/commands/write.py`, `src/repocodex/engine/gate.py`, `src/repocodex/store/bundle.py`.

> return write_memory(_root(), ".", identity=identity, stdin_text=markdown)
> --- `src/repocodex/mcp_server.py`

#### RT-CMP-coding-agent
Label: External coding and repair agent

Source-native Cursor, Claude or Codex harness, with model interpretation of the coding/review skills and repair prompt. The model is distributed-parametric; its storage substrate and provider implementation are outside the registered source. Parameters changing during operation: uninspected. Exact version pinned: no model pin in the inspected skill or repair argv. Mutable endpoint resolving to another model: uninspected; no endpoint selected in this source path. The harness executable selection itself depends on current PATH. Ordinary coding uses the already-running host, while repair invokes a fresh external process; model-context sharing between them is unestablished. SRC-1 implementation: `src/repocodex/commands/repair.py`; doctrine/design: `src/repocodex/data/skills/repocodex-coding/SKILL.md`.

> HARNESS_ORDER = ("cursor", "claude", "codex")
> --- `src/repocodex/commands/repair.py`

### Operative objects

#### RT-OBJ-coding-skill
Label: Coding skill

Shipped natural-language procedure stored as packaged Markdown, copied into client skill directories. Its consumer is the host agent, not a deterministic interpreter of each instruction. It tells the agent which commands to run, which concept types to consider and when not to end the turn. SRC-1 doctrine/design: `src/repocodex/data/skills/repocodex-coding/SKILL.md`; installation implementation: `src/repocodex/commands/install.py`.

> Do not finish the turn while `blocking` is true.
> --- `src/repocodex/data/skills/repocodex-coding/SKILL.md`

#### RT-OBJ-concept-body
Label: Concept body

Natural-language explanation in a typed concept Markdown file under a `.context` shard. `load_concepts` parses the file; retrieval returns selected bodies; coding and review agents interpret their meaning. The body is separately operative from its frontmatter, whose fixed-rule consumers determine selection and attestation. SRC-1 implementation: `src/repocodex/store/bundle.py`, `src/repocodex/retrieval.py`; doctrine/design: `src/repocodex/data/skills/repocodex-review/SKILL.md`.

> item["body"] = doc.body
> --- `src/repocodex/retrieval.py`

#### RT-OBJ-concept-frontmatter
Label: Concept frontmatter

Symbolic parsed metadata serialized with the concept body: type, status, verification anchors, claims, sources, supersession and related fields. Individual source/rationale strings can carry prose, but the inspected engine path consumes typed keys, statuses, literals and paths through fixed rules. Shard-relative identity derives from file path. Reverse indexes are generated lookup material used for path-to-identity selection, not an embedding store. SRC-1 implementation: `src/repocodex/store/bundle.py`, `src/repocodex/commands/write.py`, `src/repocodex/retrieval.py`.

> identity = identity_from_path(str(context_root), str(path))
> --- `src/repocodex/store/bundle.py`

### Routes

#### RT-RTE-coding-loop
Label: Coding skill loop

Host coding task → installed skill → context → bounded caller inspection → code edit → validate → memory repair/write → commit. Principal and next-step owner: external foreground agent acting for its user. Decision policy is natural-language [RT-OBJ-coding-skill](#rt-obj-coding-skill); command outcomes are symbolic inputs to that judgment. The host proposes code and explanation changes; checks can reject command-mediated admission, while human veto/approval settings are external and uninspected. Open coding requests, not a bounded experimental curriculum. Answer oracle: no expected correct answer supplied by the skill; diff/code comparison is evidence, not a reference answer. SRC-1 doctrine/design: `src/repocodex/data/skills/repocodex-coding/SKILL.md`.

- Immediate return: Each CLI call returns JSON to the host; the enclosing host eventually returns a code change/message, whose actual form is external.
- Later read-back: Written concepts and indexes feed later context calls; see [RT-RTE-context-read](#rt-rte-context-read).
- Delegated visibility: No RepoCodex-created subagent frame in this ordinary loop; host context includes command results it receives.
- Selection predicate: Intended edit paths for context; changed symbols and proximity/test preference for bounded caller inspection.
- Invalidation or expiry: Validation can demand maintenance; the skill does not itself erase host context.
- Activation or effect: Requests that the agent preserve institutional why and repair blocking results before finishing; actual compliance unobserved.
- Evidence limits: Procedure is shipped, but no agent execution or code-quality outcome supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> Read plausible callers until the read cap (default 12 files). Stop at the cap; do not explode on common names.
> --- `src/repocodex/data/skills/repocodex-coding/SKILL.md`

#### RT-RTE-context-read
Label: Path-selected context read

CLI `context` or MCP `get_context` → `context_for` → `retrieve` → shard loading and merged reverse index → ranked selected bodies plus linked/catalog titles → envelope. Owner: deterministic retrieval code; foreground agent supplies paths and decides whether to open related bodies. Default excludes draft and deprecated selected concepts; CLI `--drafts` admits drafts. MCP `read_concept` is a distinct direct-identity read that returns any matching loaded document without the retrieval status filter. SRC-1 implementation: `src/repocodex/commands/context.py`, `src/repocodex/retrieval.py`, `src/repocodex/mcp_server.py`.

- Immediate return: Selected concept metadata/bodies, related titles, catalog, engine version and body-character token estimate.
- Later read-back: Reads previously persisted concepts across invocations; this route does not write their semantic content.
- Delegated visibility: CLI/MCP results reach the requesting host; related bodies require another read.
- Selection predicate: Exact reverse-index entries for supplied paths, then status filters; score rewards sources, stable status and verified metadata and subtracts Git churn.
- Invalidation or expiry: Deprecated selected concepts omitted, drafts omitted by default; retrieval itself does not test date expiry or evict host turns.
- Activation or effect: Delivers explanations for agent interpretation; behavior change is unobserved.
- Evidence limits: Index completeness and agent compliance are not guaranteed by delivery; direct MCP identity read has different filtering.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if doc.status == ConceptStatus.draft and not include_drafts:
>     continue
> if doc.status == ConceptStatus.deprecated:
>     continue
> --- `src/repocodex/retrieval.py`

#### RT-RTE-memory-write
Label: Attested concept write

CLI write/ordinary reconcile and MCP write/reconcile → parse incoming Markdown/identity → stable-body supersession check → possible predecessor deprecation → required claims and new-identity prefix checks → anchor gate when anchors exist → serialize concept, update catalog/log, regenerate indexes. Owner: command and gate code; proposal author may be agent or human, unresolved per invocation. No per-content human approval check. Gate rejects mechanically unsuitable anchors/claims, not incorrect prose. Operating mode: open authoring/maintenance. Answer oracle: local pinned source/term matching, not a semantic expected answer. Guidance: coding skill prefers stable tokens, distinct whys and rationale for why-changes. Admission persists body/frontmatter, predecessor status, catalog/log and indexes. Rollback is not transactional: predecessor deprecation precedes later rejection checks, and storage uses sequential writes. Caller must correct/retry or restore through repository operations. SRC-1 implementation: `src/repocodex/commands/write.py`, `src/repocodex/engine/gate.py`, `src/repocodex/store/bundle.py`; doctrine/design: coding skill.

- Immediate return: Accepted/rejected envelope with tighten reasons, counts, suggestions and on acceptance identity/path.
- Later read-back: Accepted concepts feed context and validation; deprecated predecessors are omitted by default retrieval even if a later replacement check fails.
- Delegated visibility: CLI/MCP caller receives result; no model called internally.
- Selection predicate: Caller identity/source; existing identity found across shards; existing shard preserved, otherwise owning shard selected from pinned paths.
- Invalidation or expiry: Supersession deprecates predecessor; draft lacking stale_after is promoted stable. Existing wrong-prefix identities get suggestions rather than new-write rejection.
- Activation or effect: Changes retained input to future agent decisions and symbolic attestation; semantic activation unobserved.
- Evidence limits: Anchorless writes bypass evaluate_write; direct patch and filesystem writers are not covered by this gate. No atomic rollback established.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> deprecate_concept(repo, doc.frontmatter.supersedes, reason=f"superseded by {ident}")
> --- `src/repocodex/commands/write.py`

> if doc.anchors:
>     gate = evaluate_write(doc, config)
> else:
>     gate = GateResult(accepted=True)
> --- `src/repocodex/commands/write.py`

> in_terms = claim_in_terms(claim.literal, owner_anchor.all_of)
> in_source = literal_as_token(claim.literal, region_text)
> if not in_terms or not in_source:
>     tighten.append("claim_not_anchored")
>     reasons.append(f'claim "{claim.literal}" is not anchored')
> --- `src/repocodex/engine/gate.py`

#### RT-RTE-validate-change
Label: Validate and enforce change

CLI/MCP/hook/Action → changed paths and stable concepts → anchor/claim classification, intent impact, contradictions, index-sync and skipped-memory checks → worst result plus blocking reasons → optional acknowledgment override → posture policy → envelope/metrics → CLI exit policy. Owner: deterministic code; caller selects base, staged/all scope and enforcement mode. `--hook` selects staged and nonzero-on-blocking; default CLI without `--diff` checks all stable concepts. Selected path lists can be staged while pinned source evaluation uses the working-tree reader in liveness, so this is not established as a complete index-snapshot attestation. SRC-1 implementation: `src/repocodex/commands/validate.py`, `src/repocodex/engine/liveness.py`, `src/repocodex/engine/ratchet.py`, `src/repocodex/cli.py`.

Decision roles: code classifies and can deny configured checks; caller can alter posture or request exemption. `_ack_evidence` accepts a CI environment evidence string when CI markers are set, or a tracked file containing an acknowledgment token. The Action separately seeks an APPROVED review by a non-author with a matching token, but the validator does not authenticate a review-agent identity itself. `review_ack` is accepted as an argument but does not drive the acknowledgment decision. The exemption emits audit/repair-task data in the response, not a persisted repair-task write here. Open change checking; source literals and regions are mechanical reference evidence, not an answer oracle for explanation truth. SRC-1: `src/repocodex/commands/validate.py`, `src/repocodex/data/action/repocodex.yml`.

- Immediate return: Verdict, classifications, patches/candidates, skipped memory, reasons, impacts, advisory warnings, metrics; exit 1 only in hook/check mode when blocking.
- Later read-back: Metrics accumulate for diagnostic false-drift calculation; persisted concepts/indexes are reloaded inputs, not revised by the default validation call.
- Delegated visibility: Hook prints results and refuses on nonzero; MCP returns data to host; CI visibility depends on configured workflow.
- Selection predicate: Stable concepts intersecting changed pinned paths, or all stable concepts; changed files omit installed skill artifacts. Ratchet skips memory/install wiring, listed basenames, exclusions and nonsubstantive changes; an updated pinning concept can discharge it.
- Invalidation or expiry: Results are a current inspection, not cached approval; posture/exemption change blocking without changing classification evidence.
- Activation or effect: Hook/check denial on configured blocking; plain CLI and MCP require caller response. No merge-protection deployment established.
- Evidence limits: Working-tree reads limit staged-snapshot guarantees; WEAK does not block solely for weakness. Source configuration is not observed enforcement.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if config.posture == "shadow":
>     blocking = "skipped_memory" in blocking_reasons
> else:
>     blocking = bool(blocking_reasons)
> --- `src/repocodex/commands/validate.py`

> code = 1 if (check or hook) and payload.get("blocking") else 0
> --- `src/repocodex/cli.py`

> text = target.read_text(encoding="utf-8")
> if "memory-exempt" not in text and "repocodex-ack" not in text.lower():
>     return None
> return {"via": "committed_record", "path": rel}
> --- `src/repocodex/commands/validate.py`

#### RT-RTE-anchor-patch
Label: Direct anchor patch

CLI `reconcile --apply-patch` parses caller JSON; CLI `validate --apply-patches` loops emitted patches. Both reach `apply_anchor_patch`, which finds a concept, updates the selected anchor for replace_path, serializes directly and regenerates indexes. Owner: patch function, not write gate. Trigger: reanchor proposal or direct caller patch. Proposed change: anchor path and optionally terms; admission: existing concept and usable index/keys, with no evaluate_write call. Caller can withhold patch; invalid keys/identity/index can error. Recovery/rollback: no transactional reversal implemented here. Guidance in coding skill says to apply emitted patch and stage it. Operating mode: maintenance; no semantic answer oracle. SRC-1 implementation: `src/repocodex/cli.py`, `src/repocodex/commands/reconcile.py`; doctrine/design: coding skill.

- Immediate return: Applied path/envelope or exception; CLI validate also lists applied patches.
- Later read-back: Rewritten anchor and indexes feed later validation/retrieval.
- Delegated visibility: Caller receives application result; no delegated model in patch writer.
- Selection predicate: Supplied concept identity and integer anchor_index; replace_path controls mutation.
- Invalidation or expiry: Existing path/terms overwritten; no expiry or gate-based invalidation on admission.
- Activation or effect: Changes future symbolic attestation and selection; records reconcile metric with false_drift true for replace_path.
- Evidence limits: Direct JSON entry can reach the writer without proof of a unique relocation; later validation is a separate caller action.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if patch.get("op") == "replace_path":
>     doc.anchors[idx].path = patch["to"]
>     if patch.get("terms"):
>         doc.anchors[idx].all_of = list(patch["terms"])
> path.write_text(serialize_concept(doc), encoding="utf-8")
> regenerate_all(repo)
> --- `src/repocodex/commands/reconcile.py`

#### RT-RTE-agent-repair
Label: External agent repair

CLI repair → validation → available harness selection by PATH → subprocess with static repair prompt and repository cwd → process-result envelope. Principal: caller; next-step owner becomes external harness, whose choices are opaque. Trigger: explicit repair call, not an internal automatic DRIFT scheduler. Proposed changes: drifted-anchor repair through requested write/reconcile; admission/rejection comes from those commands only if the harness uses them. No RepoCodex per-content human review or sandbox is inserted. Prompt guidance requests stable terms and gate acceptance; only whatever the child actually writes persists. Recovery: absent/unknown harness, spawn errors and nonzero exits are returned; no retry loop, timeout, rollback or post-child validation here. Operating mode: open repair request. No expected-answer oracle; validation is diagnostic evidence. SRC-1 implementation: `src/repocodex/commands/repair.py`.

- Immediate return: Pre-child verdict, lost/candidates, prompt, chosen agent and invocation status; captured child output is not included in the result payload.
- Later read-back: Any child-written concepts may reach later commands; their actual production is unobserved.
- Delegated visibility: Child receives static prompt, repository cwd and inherited process environment; lost/candidates remain parent return data rather than prompt interpolation. Model-context sharing uninspected.
- Selection predicate: First available cursor, claude or codex binary; no verdict guard before invocation.
- Invalidation or expiry: One subprocess result, not a validated repair certificate.
- Activation or effect: Invokes external agent-capable process; zero exit sets invoked/ok without verifying repaired memory.
- Evidence limits: Actual tools, approvals, provider, parameter changes, execution and retained results external/unobserved.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> completed = subprocess.run(
>     argv,
>     cwd=str(repo),
>     capture_output=True,
>     text=True,
>     check=False,
> )
> --- `src/repocodex/commands/repair.py`

> invoked = completed.returncode == 0
> --- `src/repocodex/commands/repair.py`

#### RT-RTE-bootstrap-drafts
Label: Bootstrap draft decisions

Explicit bootstrap → tracked comments/docs and last 100 commit subjects → deterministic candidates → require evidencing commit → evaluate_write → direct write_concept → regenerate indexes. Owner/proposer/admitter: code, not an internal model; caller initiates but no per-item human approval. Candidate body copies mined note; guidance is regex selection of why-like content and local anchor checks, not an observed synthesized explanation. Rejections are returned. Operating mode: bounded mining pass; no answer oracle for narrative correctness. Recovery: rejected candidates remain unadmitted; already-written candidates are not transactionally rolled back. SRC-1 implementation: `src/repocodex/commands/bootstrap.py`.

- Immediate return: Kept identities, rejected candidates/reasons, draft status.
- Later read-back: Draft Markdown with commit source and stale_after can be requested through draft-enabled context or direct reads; default context omits drafts.
- Delegated visibility: No model invoked in this producer; later host may inspect drafts.
- Selection predicate: Supported source suffixes/comment regex or why-like commit subjects, first changed history path, deduplicated stable ID; source commit and gate required.
- Invalidation or expiry: Draft stale_after set approximately 30 days ahead; audit GC applies expiry rather than retrieval automatically deleting it.
- Activation or effect: Creates retained draft input and indexes; does not demonstrate future use or benefit.
- Evidence limits: Passes gate directly, not all write_memory wrapper checks; draft production does not authenticate why prose.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> gate = evaluate_write(doc, config)
> if not gate.accepted:
>     rejected.append({"identity": identity, "tighten": gate.tighten})
>     continue
> write_concept(repo, doc)
> kept.append(identity)
> --- `src/repocodex/commands/bootstrap.py`

#### RT-RTE-review-audit
Label: Review and audit maintenance

Review skill asks external review agent to compare new prose against the originating diff and report advisory findings. CLI advisory separately computes ranked code hits and emits judgment categories, but CLI supplies no judgments; absent categories remain not_evaluated. The installed advisory Action invokes that CLI, not an agent. Audit samples stable concepts for out-of-band review, produces screening bodies/regions, imports optional findings JSON as proposals, and runs GC. Owners: review agent for semantic judgment; deterministic code for screening/proposal wrapping/retirement. SRC-1 doctrine/design: `src/repocodex/data/skills/repocodex-review/SKILL.md`; implementation: `src/repocodex/commands/advisory.py`, `src/repocodex/commands/audit.py`, `src/repocodex/cli.py`, `src/repocodex/data/action/repocodex.yml`.

Admission distinctions: imported findings do not automatically edit concepts. GC does deprecate without per-item approval when orphaned with no matching anchor, or draft expired. Trigger is audit invocation; proposed change is retirement; code admits it, and subsequent correction/restoration is caller-owned. Reviewer can recommend rejection, but is instructed not to block required checks. Guidance asks prose/diff comparison, weakening checks and distinct-whys review. Operating modes: open PR review and bounded seeded sampling. Answer oracle: none supplied for semantic truth; current pinned region/diff is comparison evidence. No formulated-theory revision is established merely by these review requests.

- Immediate return: Advisory categories/code hits or audit sample/screening, contradictions/proposals and retired identities.
- Later read-back: GC-deprecated status persists and affects future context; imported proposals have no automatic persisted semantic revision here.
- Delegated visibility: Screening payload is returned for out-of-band reviewer; no audit-internal model call.
- Selection predicate: Seeded stable-concept sample; GC separately considers loaded concepts, inbound links, anchor hits and draft date.
- Invalidation or expiry: GC retires orphan/no-hit concepts and expired drafts; advisory judgments do not change required verdict.
- Activation or effect: Produces review inputs and deterministic retirement; actual semantic review, accepted correction and benefit unobserved.
- Evidence limits: Action advisory output cannot stand as evidence an agent checked new prose; optional imported judgments are not authenticated reference answers.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if name in judgments:
>     return _category(EVALUATED, judgments[name])
> return _category(NOT_EVALUATED)
> --- `src/repocodex/commands/advisory.py`

> if orphan or expired_draft:
>     deprecate_concept(repo, doc.identity, reason="gc")
>     retired.append(doc.identity)
> --- `src/repocodex/commands/audit.py`

#### RT-RTE-relocate-identity
Label: Relocate concept identity

Explicit identity or --mismatched → load/find concept → suggest type prefix → reject occupied/missing/inapplicable target → remove source/catalog link → write identical content at new identity → update catalog/log/index. Owner/admitter: code; caller proposes individual or bulk relocation. Trigger is prefix debt cleanup, not automatic model discovery. Guidance comes from authored-type folder mapping. No per-content human approval or semantic answer oracle. Rollback/recovery is caller-owned; unlink-before-write is not transactional. SRC-1 implementation: `src/repocodex/commands/relocate.py`.

- Immediate return: Moved from/to/path records and skipped reasons.
- Later read-back: New path-derived identities and regenerated indexes feed later consumers; no semantic body rewrite.
- Delegated visibility: Caller receives results; no model invocation.
- Selection predicate: Requested identity or all loaded mismatched identities, allowed-prefix mapping, vacant target.
- Invalidation or expiry: Old concept file removed; catalog link removed; existing body retained at new identity.
- Activation or effect: Changes retained addressing and lookup; not an evaluation of explanation truth.
- Evidence limits: No gate call and no atomic rollback; broader inbound-reference correctness not established here.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> text = src.read_text(encoding="utf-8")
> src.unlink()
> _remove_catalog_link(root, doc.identity)
> dest.write_text(text, encoding="utf-8")
> --- `src/repocodex/commands/relocate.py`

#### RT-RTE-install-wiring
Label: Install behavioral wiring

Operator CLI install → copy hook/Action, skills/rules/plugin and optional MCP configuration → create version-pinned shadow config if absent → report files installed/failed/skipped. Owner/proposer: caller choosing installation/options; code chooses shipped artifact contents. No independent content approval gate. Existing hook/Action/skill copies may be overwritten; CLAUDE.md pointer and MCP server mapping are merged by their specific branches. Trigger is explicit installation; changed instruction/control files persist into later host/CI operations. Rollback is external repository/filesystem recovery, not implemented as an installer transaction. Operating mode: setup/upgrade, no answer oracle beyond file-existence checks. SRC-1 implementation: `src/repocodex/commands/install.py`, `src/repocodex/data/hooks/pre-commit`, `src/repocodex/data/action/repocodex.yml`, `src/repocodex/data/plugin/plugin.json`.

- Immediate return: Installed/failed/skipped paths, ok and MCP-config-written flags.
- Later read-back: Clients can load copied skills/rules; Git can invoke hook; Actions can load workflow; these external activations are unobserved.
- Delegated visibility: Plugin manifest exposes skills/MCP; packaged adapters exec the portable pre-commit floor, but manifest alone does not activate adapters.
- Selection predicate: Presence of .git, skills option, MCP option and optional-extra availability; fixed packaged source paths.
- Invalidation or expiry: Files persist until changed/reinstalled; pin mismatch can be rejected by config loading, not proof host loads skill.
- Activation or effect: Installs behavior-shaping instructions and check machinery; actual deployment/enforcement uninspected.
- Evidence limits: Existence checks establish copied files, not correct client loading or branch protection; no evaluated model/version pin.
- implementation conclusion status: wired
- deployment conclusion status: uninspected

> config.write_text(
>     f'engine_version = "{ENGINE_VERSION}"\nposture = "shadow"\nscope_lines = 40\n',
>     encoding="utf-8",
> )
> --- `src/repocodex/commands/install.py`

### Claims

#### RT-CLM-executable-memory
Label: Executable repository memory claim

The shipped plugin description claims executable memory consisting of context, impact, attested writes and deterministic validation. The inspected implementation wires those operations but not semantic proof of explanation truth. Coding/review compliance and anti-regression benefit remain unobserved. SRC-1 doctrine/design: `src/repocodex/data/plugin/plugin.json`; implementation support and limits are in the routes above.

> "description": "Executable repository memory: context, impact, attested writes, and deterministic validation.",
> --- `src/repocodex/data/plugin/plugin.json`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-skill-consumption
Label: Skill to host behavior

Consumer: external coding/review agent. Channel: installed natural-language skills and client rule pointers. Force: protocol instruction interpreted by a model, not an executable guarantee that every step occurred. Horizon: later tasks/sessions in a consuming repository until instructions change. Installation supplies delivery opportunity; host loading and compliance remain unobserved. SRC-1 doctrine/design: `src/repocodex/data/skills/repocodex-coding/SKILL.md`, `src/repocodex/data/skills/repocodex-review/SKILL.md`; implementation: `src/repocodex/commands/install.py`. See [RT-RTE-install-wiring](#rt-rte-install-wiring), [RT-RTE-coding-loop](#rt-rte-coding-loop).

#### RT-BAP-memory-consumption
Label: Memory to coding judgment

Consumer: foreground coding agent. Channel: path-selected concept body JSON or direct concept read. Force: explanatory guidance interpreted by agent; symbolic frontmatter separately controls retrieval/attestation. Horizon: later invocations across repository changes. Delivered body does not establish changed action. SRC-1: `src/repocodex/retrieval.py`, `src/repocodex/mcp_server.py`, coding skill; see [RT-RTE-context-read](#rt-rte-context-read).

#### RT-BAP-check-enforcement
Label: Verdict to check denial

Consumer: CLI hook/check wrapper, portable pre-commit hook and configured Action. Channel: symbolic blocking flag → exit status → external commit/check control. Force: denial when invoked and policy marks blocking; shadow/exemption/caller options qualify it. Horizon: each checked diff; installed machinery persists between invocations. No universal shell-access restriction or deployed branch-protection guarantee follows. SRC-1: `src/repocodex/cli.py`, `src/repocodex/data/hooks/pre-commit`, `src/repocodex/data/action/repocodex.yml`; see [RT-RTE-validate-change](#rt-rte-validate-change).

## Annotations

none
