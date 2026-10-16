---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "LLM Wiki Coordination runtime baseline: agent-operated dialogue and canon protocols, deterministic audit entry point and enforcement limits at the frozen commit."
run-id: AAS-2026-10-14-llm-wiki-coordination-a12f3c7007f2-01
reviewed-boundary: "126749634d1c8c2fd6141f59711c882c2d629699"
---

# LLM Wiki Coordination runtime report

## Runtime account

### Work and principals

This is a documentation-first coordination package, not a scheduler or model-calling runtime. The consequential claimed work is preserving multi-agent discussion, directing subsequent contributions toward perceived deficits, admitting reviewed structural knowledge, and diagnosing wiki integrity. External agents interpret the procedures and modify a downstream filesystem wiki; a user recognizes closure and approves canon. The sole shipped executable is an audit reader/reporting CLI. Implementation findings below concern that CLI; dialogue and admission findings concern doctrine/design. Neither actual adoption nor successful compliance is established. SRC-1: `README.md`, `protocols/rolespace-coordination.md`, `protocols/multi-ai-consensus.md`, `tools/llm-wiki-audit.py`.

> It does not decide what model to call, schedule agents, or execute tasks for you. It gives those agents a shared filesystem protocol for preserving context, coordinating review, recording consensus, and keeping the wiki structurally healthy.
> --- `README.md`

Agent identity is a local author/consensus handle, not an authenticated provider identity. Agents may have persistent persona files, but neither startup loading nor persona reconstruction is implemented here. Anchor Form doctrine explicitly allows model changes subject to continued manifestation and user recognition; it is not a pinned model or isolation contract. [RT-CMP-agent-substrate](#rt-cmp-agent-substrate) records this model boundary. SRC-1: `protocols/multi-ai-consensus.md`, `concepts/persona-manifest-ontology.md`.

### Ordinary agent-operated invocation

An adopter copies/adapts protocols, chooses a dialogue root and supplies agents capable of filesystem work. An initiating agent creates `thread.md`, `meta.yaml`, and an initial numbered contribution; it updates indices/logs. `thread.md` carries stable context and append-only open questions, metadata carries participants, status, targets and preferred directions, and entries carry prose plus YAML. A subsequent external invocation reads the prior entry, evaluates its N/C/R contribution, calculates a cumulative vector, selects the greatest target deficit and contributes with `last_eval` pointing backward. Natural-language interpretation supplies the semantic scores; symbolic sums/thresholds organize them. There is no shipped dispatcher to select the next participant, lock entry allocation, supply model context or execute the write. The next-step owner is the participating external agent, under host/user scheduling. [RT-RTE-thread-participation](#rt-rte-thread-participation). SRC-1: `README.md`, `protocols/dialogue-thread-format.md`, `protocols/rolespace-coordination.md`.

The prescribed closure adds the previous contribution's evaluation to the sum and records `current_at_close` plus a canon proposal. A user may refuse recognition, including for insufficient target values. Continuing after closure requires a reopen entry that evaluates the closure; it returns the thread to open. Crystallization/signing tooling is not shipped, so production of canon and state transitions remains an external agent/user duty. Canonical structural documents then undergo revision-specific consensus and explicit user approval, with a soft-canonical alternative and disputes routed to dialogue. These are two different decisions: accepting a thread's closure is not itself full active-agent consensus on a canon page. [RT-RTE-canon-admission](#rt-rte-canon-admission). SRC-1: `protocols/dialogue-thread-format.md`, `protocols/rolespace-coordination.md`, `protocols/multi-ai-consensus.md`, `README.md`.

> The final decision on **Crystallization** is made by the User through their **Recognition**.
> --- `protocols/rolespace-coordination.md`

### Ordinary executable invocation

The shipped installation path runs `python3 tools/llm-wiki-audit.py` from the adopter repository root. `argparse` supplies root (default current directory), cutoff, strict-legacy, JSON output and maximum-layer values. `GenericWikiAudit` resolves root and creates in-memory findings, heading/link indexes and a text cache. `run()` invokes L0 hygiene, L1 graph, L2 dialogue/consensus/crypto and conditionally L3. Markdown discovery is `root/wiki/**/*.md`; dialogue checks specifically traverse `root/wiki/agents/dialogue`. This is not an arbitrary adopter-root discovery mechanism. SRC-1: `README.md`, `tools/llm-wiki-audit.py`.

Checks parse YAML, strip code for most link/crypto text scans, resolve file references, compare entry vectors and collect severity, invariant, locus, reason and proposed action. Reports are printed as text or JSON; the CLI returns zero exactly when the collected HARD count is zero, assuming it reaches the terminal exit. No wiki repair, canon write, report-file persistence or log update occurs in this executable. The audit protocol separately assigns semantic review, report retention, log summary and contested-Hard escalation to an external agent/user. [RT-RTE-audit-invocation](#rt-rte-audit-invocation). SRC-1: `tools/llm-wiki-audit.py`, `protocols/integrity-audit.md`.

>     audit.run()
>     audit.print_report(as_json=args.json)
>     sys.exit(0 if audit._summary()[HARD] == 0 else 1)
> --- `tools/llm-wiki-audit.py`

Recovery is recommendation-driven, not transactional. Syntax errors in ordinary frontmatter become HARD findings; malformed metadata YAML is converted to an empty mapping on several dialogue paths. Filesystem failures or parsed YAML shapes inconsistent with subsequent `.get()` calls can instead interrupt the process: there is no enclosing exception/retry handler. Cache/index state lasts only for this audit object. The findings are not a snapshot or a concurrency barrier, and no downstream runner is supplied to obey the exit status. SRC-1: `tools/llm-wiki-audit.py`.

### Four source-level forcing cases

These cases were inspected, not executed. They challenge the package's strong construction/enforcement language without assuming that external agents violate it in practice.

1. **Self-evaluation through alternate references.** The format says self-evaluation is structurally impossible. The checker detects `ref == entry.name` only when there is a previous entry, and detects matching previous author only when `ref == previous.name`. A different reference is WARN, not HARD, and older referenced authors are not resolved. A reference to an older same-author entry therefore does not receive the D5 check used for the immediate predecessor. Merely placing evaluation in the next file also cannot prevent the same author writing both files. This is a protocol plus partial retrospective checker, not a filesystem invariant. SRC-1: `protocols/dialogue-thread-format.md`, `tools/llm-wiki-audit.py`. [RT-CLM-peer-evaluation](#rt-clm-peer-evaluation).
2. **Archival/reopen bypass.** Setting `migration_mode: archival` makes metadata validation and the entire entry-chain check return early. The prose requires normal schema for new entries after reopening, but code never switches back based on status or entry type. This bypass affects dialogue-specific validation, not general markdown hygiene, links or all L3 checks. [RT-RTE-archival-audit](#rt-rte-archival-audit). SRC-1: `protocols/dialogue-thread-format.md`, `tools/llm-wiki-audit.py`.
3. **Closure and canon without admission enforcement.** The checker compares closure sums with tolerance 0.01, but does not compare them with target, enforce no ordinary append after closure, validate only-one-reopen, prove user recognition or authenticate authors. Consensus checks focus on `lifecycle == "accepted"` and string statuses beginning `pending`; they do not enforce full/soft canonical quorum, active-agent age, revision matching, stale transitions or user approval. The prose's canonical and canonical-pending paths therefore have no matching admission gate here. [RT-RTE-canon-admission](#rt-rte-canon-admission). SRC-1: `tools/llm-wiki-audit.py`, `protocols/multi-ai-consensus.md`, `protocols/dialogue-thread-format.md`.
4. **Reduced-layer/root paths.** `--layer 0`, `1` or `2` does not restrict execution to that layer: `run()` always invokes L0–L2 and uses the value only for L3. Conversely, an adopter using `docs/dialogue/` or the starting-thread example `protocols/dialogue/` does not enter the code's fixed dialogue traversal. Direct method callers can also run a subset and receive no CLI exit gate. L3 allows explicit `signature: null` and never verifies cryptographic signatures. SRC-1: `tools/llm-wiki-audit.py`, `protocols/dialogue-thread-format.md`. [RT-RTE-audit-invocation](#rt-rte-audit-invocation).

### Guarantee coverage and effect boundary

| Load-bearing guarantee | Owner and enforcement point | Strength | Covered versus alternate paths; external contract | Separate conclusion statuses |
|---|---|---|---|---|
| Entries do not overwrite others; prior context remains | Participating agents; instructions to allocate new entry files and append OQ | protocol | Prescribed entry writes only. Host shell/editor/direct filesystem writes remain outside any shipped write interceptor; host must enforce permissions/concurrency if required. | doctrine conclusion status: claimed; implementation conclusion status: absent; operation conclusion status: uninspected |
| No self-evaluation; sums reflect evaluations | Agents and retrospective entry checker | protocol | Non-archival recognized entry types receive reference/vector checks; alternate references, archival chains and arbitrary file writes escape parts of coverage. Correct semantic evaluation still requires external agent judgment. | doctrine conclusion status: claimed; implementation conclusion status: wired; operation conclusion status: uninspected |
| Closure/canonical transition requires legitimate approval | User, individual agents and document authors; protocol decision rules | protocol | Closure, full and soft canon are prescribed paths. Checker does not intercept promotion or enforce approval; external host/agents must record and honor decisions. | doctrine conclusion status: claimed; implementation conclusion status: absent; operation conclusion status: uninspected |
| Non-Hard findings do not block work | CLI owner; final HARD-count exit | invariant | Normal completed CLI invocation has this exit rule. Exceptions, direct API use and host decisions are separate. An adopter must honor the exit code to turn it into workflow blocking. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Models do not hold signing keys | Tool/repository operators and agents; ontology plus heuristic crypto text scan | policy | Scan flags some prose, omits code and recognized negations; it neither controls custody nor authenticates signatures. Signing is deferred. | doctrine conclusion status: claimed; implementation conclusion status: wired; operation conclusion status: uninspected |

SRC-1: `protocols/dialogue-thread-format.md`, `protocols/multi-ai-consensus.md`, `protocols/integrity-audit.md`, `concepts/persona-manifest-ontology.md`, `tools/llm-wiki-audit.py`, `README.md`. The minimum passages supporting the disputed guarantees and executable coverage are retained in the records below.

The target's capability surface is protocol-directed external filesystem editing plus deterministic local audit reads. Current downstream grants and deployed isolation are uninspected: no adopting host configuration is supplied. The source contains no provider-native tools, remote workers, direct model-call alternate path or extension loader. This limits conclusions to the shipped package, not external hosts' capacities. [RT-ABS-runtime-orchestration](#rt-abs-runtime-orchestration). Working-context economy is claimed through per-entry files and on-demand cumulative calculation, but no loader, truncation policy, context frame or automatic reload mechanism is shipped; actual model-visible selection remains host/agent-owned. SRC-1: `README.md`, `protocols/dialogue-thread-format.md`, `tools/llm-wiki-audit.py`.

Product changes have a separate maintainer procedure: discuss new features in an issue/design document, preserve generic scope and update the changelog when semantics change. No automated merge/admission machinery is supplied. [RT-RTE-package-revision](#rt-rte-package-revision). The frozen changelog reports criticism-driven formula and closure fixes; this is reported development, not an execution trace or causal experiment. SRC-1: `AGENTS.md`, `CHANGELOG.md`.

All sources used are SRC-1 at the reviewed commit. Runtime inspection covered the README, all four protocols, persona ontology, maintainer instructions, changelog and all 714 lines of the audit implementation. No new source or execution evidence was added. File-tree inspection and bounded implementation searches checked the absence and alternate-path findings; no target code, tests or fixtures were executed. Operational activation, concurrency behavior, semantic review quality and benefit remain unobserved.

## Shared records

### Components

#### RT-CMP-generic-wiki-audit
Label: GenericWikiAudit

Source-native identity: Python class `GenericWikiAudit` and its script entry point in SRC-1: `tools/llm-wiki-audit.py`. Representational form: symbolic Python control rules. Storage substrate: shipped source file; per-instance findings/cache/indexes in process memory. It reads local files with Python/PyYAML, computes checks and prints recommendations; no model inference or mutation executor is present in the inspected code.

>     def markdown_files(self):
>         wiki_dir = self.root_dir / "wiki"
>         if not wiki_dir.exists():
>             return []
>         return sorted(wiki_dir.rglob("*.md"))
> --- `tools/llm-wiki-audit.py`

#### RT-CMP-agent-substrate
Label: External agent substrate

Source-native identity: the underlying model/generative environment described as Substrate in SRC-1: `concepts/persona-manifest-ontology.md`, and AI models performing consensus in `protocols/multi-ai-consensus.md`. Representational form: distributed-parametric for the external language model, distinct from textual manifests and local agent identifiers. Storage substrate: external provider/host parameters; inaccessible here. Parameters changing during operation: uninspected, because neither weights nor provider calls/configuration are shipped. Exact version pinned: no model version is specified by this package. Mutable endpoint resolution: uninspected, because no endpoint is shipped; doctrine explicitly permits a model changing or being updated. This component supplies the prescribed interpretation/authoring roles, not a wired invocation inside the audit.

> - **Bounded Substrate-Portability:** The form is distinct from any single runtime session. A model may change or be updated while the Anchor Form remains recognizable, but portability is not automatic: the new substrate must still be able to manifest the form and receive Recognition.
> --- `concepts/persona-manifest-ontology.md`

### Operative objects

#### RT-OBJ-coordination-protocols
Label: Shipped coordination protocols

Source-native identity: the four files under `protocols/`, especially RoleSpace attention rules and consensus admission rules. Representational form: natural-language instructions consumed by agents/users; formulas and field examples become symbolic only where an actual fixed-rule consumer implements them. Storage substrate: static Markdown files copied/adapted into an adopting wiki. These are operational guidance, not evidence that a host loaded them. Their later copies, thread material, consensus blocks and revisions are left to specialist memory characterization. SRC-1: `README.md`, `protocols/rolespace-coordination.md`, `protocols/multi-ai-consensus.md`, `protocols/integrity-audit.md`, `protocols/dialogue-thread-format.md`.

> 1. Copy or adapt the files in `protocols/` into your wiki's workflow/protocol folder.
> --- `README.md`

### Routes

#### RT-RTE-thread-participation
Label: Thread participation and deficit-directed contribution

Endpoints/progression: initiating agent creates a thread and first entry; subsequent participant reads the preceding contribution, records peer scores, calculates current/target deficit, selects a direction and appends a numbered contribution; closer records sum/proposal; reopen supplies explicit recovery. Owner: external participating agents, with external scheduling. Context/state/effects: stable context/OQ, participants/target/zhat/status and prior entry prose/YAML guide a filesystem entry write. No dispatched delegation or automatic status transition exists in the package. SRC-1: `protocols/dialogue-thread-format.md`, `protocols/rolespace-coordination.md`.

- doctrine conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Prescribed new contribution or closure/reopen file, not a runtime return value.
- Later read-back: Next participant reads preceding entry and retained chain to evaluate and calculate current; actual host delivery is uninspected.
- Delegated visibility: Shared downstream wiki entries are intended for participants/user; no isolation or selective delegation mechanism is supplied.
- Selection predicate: Previous sequential entry for peer evaluation; greatest target deficit for direction; zhat supplies preferred orientation rather than implemented participant scheduling.
- Invalidation or expiry: Prescribed no standard appends after closure; reopen evaluates closure and restores open status. Old entries remain append-only.
- Activation or effect: Instructions prescribe an attention choice and new entry; behavior change in an actual agent invocation is uninspected.
- Evidence limits: Doctrine only for agent execution; checker partially diagnoses entry structure retrospectively and does not execute this loop.

Proposal/decision/veto: participant supplies semantic scores and chooses content/direction; closer proposes canon; user accepts/refuses recognition. Numerical sums do not establish a ground-truth answer oracle. Operating mode: open-ended collaborative questions with user/agent-set bounded target axes, not an implemented experimental curriculum. Trigger for further work is a deficit or reopened concern. Guidance is the N/C/R definition, previous contribution and thread context; the new contribution and evaluation persist. Rejection/recovery is user refusal or agent reopen, not automatic rollback of content.

>     - Identify the axis with the largest gap. This is the **Situational Momentum** — the direction in which the thread "wants" to develop.
> --- `protocols/rolespace-coordination.md`

Theory account: RoleSpace expresses a localized account of participation quality and deficit-directed attention. It guides derivation of contributions and asks agents to stress-test claims, but contains no supplied execution of that criticism/revision loop. Arbitrary thread subject matter is not assumed to be theory. Theory-builder conditions 1–4: condition 1 conclusion status: afforded — definitions and deficit/threshold rules form an inspectable unit; condition 2 conclusion status: claimed — agents are instructed to depend on those definitions; condition 3 conclusion status: claimed — Robustness asks for counterexamples/assumptions, but an exercised blame-and-revision sequence is not supplied; condition 4 conclusion status: claimed — later peer evaluations and reopen prescribe continued rounds, not observed criticism retention shaping behavior. Addressability: axes and thresholds are individually inspectable in Markdown/YAML, with human-interpreted semantics. Persistence: instructions and contributions are intended to span sessions, but actual later consumption is uninspected. Learning conclusion status: uninspected — no improved future-capacity evidence. Reflection conclusion status: claimed — protocol represents participation through evaluations and directs attention in response, but both causal directions are not observed. Reflective theory builder conclusion status: uninspected — no record of agents criticizing the coordination method against their own operation. Autonomous theory builder conclusion status: uninspected — external computation and human duties are not traced, and recognition is explicitly human. These findings do not infer self-improvement from retained evaluations.

#### RT-RTE-canon-admission
Label: Closure recognition and revision-specific canon admission

Endpoints/progression: closure proposal to user recognition, then structural-page endorsements and user-approved full or soft canon. Authors own lifecycle/content; individual agents own endorsements; user owns final approval/conflict decision. Effects are external page creation/editing and state/consensus metadata writes. Significant edits increment revision and stale other agents; disputes go to dialogue and can return soft canon to working. SRC-1: `protocols/dialogue-thread-format.md`, `protocols/rolespace-coordination.md`, `protocols/multi-ai-consensus.md`.

- doctrine conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Prescribed recognized/refused closure and approved/unapproved document lifecycle; no shipped canon-producing function.
- Later read-back: Agents working on a page must read its consensus block, compare revisions and re-review; actual context loading is external.
- Delegated visibility: Canon page and local agent endorsements are shared wiki records, not authenticated or selectively delivered by a dispatcher.
- Selection predicate: Consensus-required structural documents; active agents determine full consensus or two-thirds soft quorum, with explicit user approval.
- Invalidation or expiry: Significant edits (>30% or structural reorganization) stale nonauthor endorsements; mismatched revision is stale; inactivity affects active/dormant duties; disputed soft canon returns to working.
- Activation or effect: Prescribed admission changes page maturity/endorsement, potentially shaping later work; neither admission nor subsequent behavioral dependence is observed.
- Evidence limits: Doctrine sets human approval; audit implements only narrower accepted/pending checks, not canonical admission or stale enforcement.

Proposer: any agent can propose crystallization; document authors propose/edit structural content. Computational contribution: external agent interpretation, authorship, peer review and metadata I/O. Decider/veto: user explicitly approves canonical transitions and has final dispute decision; disputed endorsements prohibit soft canon, while incomplete active consensus prevents full canon under the rules. Answer oracle: inapplicable — user approval and peer agreement supply judgments, not expected-answer ground truth. Operating mode: open collaborative structural knowledge work. Improvement trigger: mature thread, changed structural page or specific dispute. Proposal guidance: retained discussion, current_at_close/target and consensus rules. What persists: page content, revision-specific endorsements and referenced disputes. Recovery: refusal/review, stale/reset statuses, downgrade to working, and dialogue reopen; no content rollback engine is shipped.

> All active agents are in `accepted` or `contributed` status, with no `stale` entries, and the User has explicitly approved the status.
> --- `protocols/multi-ai-consensus.md`

> If the document's current revision differs from the one recorded in the agent's entry, the status is considered `stale`.
> --- `protocols/multi-ai-consensus.md`

The route can admit theories or protocol instructions as content, but no concrete downstream candidate theory or criticism history is supplied. Theory-builder conditions 1–4: each condition conclusion status: uninspected for candidate content, because no adopting wiki is in the boundary. Agreement alone establishes neither content-directed criticism nor improved capacity.

#### RT-RTE-audit-invocation
Label: Deterministic audit diagnosis and CLI return

Endpoints/progression: caller/root/flags → GenericWikiAudit construction → L0–L2 checks → optional L3 → findings report/summary → HARD-dependent exit. Owner: CLI code for checks; external caller for running and honoring results. State/effects: in-memory text cache, heading/link indexes and findings; local file reads and stdout/exit only. Direct class/method invocation is an alternate surface without the CLI terminal gate. SRC-1: `tools/llm-wiki-audit.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Text or JSON findings/summary on stdout; normal CLI exit 0 without HARD findings, 1 otherwise.
- Later read-back: inapplicable — executable does not persist findings; protocol separately asks external agents to retain reports and log summaries.
- Delegated visibility: stdout/process status reaches the invoking host; no model, remote worker or user notification is wired.
- Selection predicate: Markdown under root/wiki; dialogue under wiki/agents/dialogue; L3 only if max_layer >= 3; fixed rules select loci and severity.
- Invalidation or expiry: Findings/cache/indexes are per audit instance; no durable invalidation policy or atomic wiki snapshot.
- Activation or effect: Local diagnostics and process status; externally applied repairs or blocking decisions remain uninspected.
- Evidence limits: Source-level behavior only; no execution traces. Parser/type/I/O failures can terminate before summary; no proof of complete semantic integrity.

Diagnosis roles: code proposes findings/actions against fixed checks; it makes no content repair/admission decision. External agent/user chooses repairs and may contest Hard findings; user is final verdict owner under the protocol. Answer oracle: fixed schema, computed vector sum and file-existence expectations are reference predicates, not a semantic-answer oracle. Operating mode: bounded deterministic audit of supplied root with externally initiated follow-up semantic review. Trigger: caller launches audit; protocol prescribes escalation when Hard is contested. Audit is read-only, so repair rejection/rollback lies outside this executable. No cryptographic verification or immutable-source baseline is implemented.

>     def run(self):
>         self.run_l0_hygiene()
>         self.run_l1_graph()
>         self.run_l2_protocol()
>         if self.max_layer >= 3:
>             self.run_l3_cross_protocol()
> --- `tools/llm-wiki-audit.py`

> 3. The User provides the final Recognition verdict.
> --- `protocols/integrity-audit.md`

#### RT-RTE-archival-audit
Label: Archival metadata bypass of dialogue validation

Part of: [RT-RTE-audit-invocation](#rt-rte-audit-invocation)

Endpoints/progression: thread metadata with migration_mode archival → early return from metadata/entry checks. Owner: deterministic checker; external writer controls the flag. Context/state/effect: no entry-chain accumulation or schema diagnosis on this path; report adds an INFO historical-wrapper finding. Other audit passes are not bypassed. SRC-1: `tools/llm-wiki-audit.py`, `protocols/dialogue-thread-format.md`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Entry checker emits one INFO legacy finding and returns without inspecting the entry chain.
- Later read-back: inapplicable — bypass emits no retained artifact or writer; external archival metadata is merely read.
- Delegated visibility: INFO flows into the same caller-visible findings report as other checks.
- Selection predicate: meta.get("migration_mode") == "archival", without reopened-status or new-entry qualification.
- Invalidation or expiry: No automatic expiry in code; removing/changing archival flag restores checks in a subsequent audit.
- Activation or effect: Entry schema/evaluation/sum checks omitted even if new entries follow reopening; general Markdown checks still run.
- Evidence limits: Inspectable branch, not an observed exploit; doctrine explicitly requires new reopened entries to use normal schema.

> This marks `entries/001-<author>.md` as historical text, not a fully schema-valid RoleSpace entry. New entries after a reopen must use the normal schema.
> --- `protocols/dialogue-thread-format.md`

>         if meta.get("migration_mode") == "archival":
>             self.report(INFO, "Legacy", "L2", "D3", thread_dir, "migration_mode",
>                         "Archival migration keeps pre-format entry metadata as historical text",
>                         "No action required unless the thread is reopened")
>             return
> --- `tools/llm-wiki-audit.py`

#### RT-RTE-package-revision
Label: Maintainer protocol revision

Endpoints/progression: agent maintaining this package → prior discussion in issue/design doc for new features → edits → changelog update → external repository admission. Owner: maintainers/external agent, not the audit. Context/state/effects: protocol/tool source and rationale in changelog can change later adopter guidance and checks. The repository does not ship a merge, signing, test or deployment admission driver. SRC-1: `AGENTS.md`, `CHANGELOG.md`, `README.md`.

- doctrine conclusion status: claimed
- operation conclusion status: claimed
- Immediate return: Edited package/source and changelog are the prescribed output; actual maintainer execution is supplied only as reported release history.
- Later read-back: Changed protocols/tool source can be copied by later adopters; changelog records rationale, but no actual later consumer invocation is supplied.
- Delegated visibility: Repository changes are intended for maintainers/community; external version-control/release mechanics are uninspected.
- Selection predicate: Maintainer feature/semantics proposal; AGENTS requires prior issue/design discussion and generic scope.
- Invalidation or expiry: No automated update/rollback or adopter migration is shipped; versioned release history does not itself invalidate local adopter copies.
- Activation or effect: Frozen source includes corrected formulas and checker logic described in changelog; subsequent adopter behavior/benefit is uninspected.
- Evidence limits: Release assertions support reported development only; historical file layout is not current shipped content, and AGENTS still refers to absent templates/docs.

Proposal/decision/veto: agent proposes and edits; prior discussion constrains features, but identity of merge decider, mandatory per-content human approval and veto mechanism are unspecified. Answer oracle: inapplicable — textual/math consistency review has no supplied expected-answer dataset. Operating mode: open maintainer development, with reported robustness/consistency passes. Trigger/proposed change: defects in formulas, closure accounting or portability claims. Guidance: maintainer generality rules and source-native protocol semantics. What persists: corrected source and changelog rationale. Rejection/recovery: discussion affords rejection; no shipped rollback executor or policy is specified.

> 6. The protocols described here have been tested in private usage. Do not invent new protocol features in this repo without first discussing in an issue or design doc.
> --- `AGENTS.md`

> - RoleSpace Situational Momentum formula was inverted (`softmax(-D)`); the largest deficit incorrectly received the smallest weight. Corrected to `softmax(D)`.
> --- `CHANGELOG.md`

Theory account: this reported repair criticizes an addressable rule in the coordination method, identifies its inverted effect and retains a replacement rule plus rationale. Theory-builder conditions 1–4: condition 1 conclusion status: afforded — the rule is localized and inspectable; condition 2 conclusion status: claimed — intended next-direction decisions use it, without a supplied run; condition 3 conclusion status: claimed — changelog names the formula, counterproductive result and correction; condition 4 conclusion status: uninspected — retention is visible, but a next criticism round depending on that result is not supplied. Addressability: formula/deficit definition are separately inspectable and editable. Persistence: package source and changelog survive the development episode and are available across adopter sessions, but actual later rationale consumption is uninspected. Learning conclusion status: uninspected — repaired text/code alone does not establish improved future-action capacity. Reflection conclusion status: claimed — method critique responds to its direction-selection rule and changes guidance; no own-operation trace proves both causal directions. Reflective theory builder conclusion status: uninspected — no own-run record closes conditions 2–4. Autonomous theory builder conclusion status: uninspected — internal proposal, critique and admission principals are not traced. Self-improvement attribution is not established: update rationale and changed source are supplied, but live behavioral dependence in subsequent operation and an independently evaluated improvement objective are not.

### Claims

#### RT-CLM-peer-evaluation
Label: Structural exclusion of self-evaluation

Claimed operation: moving peer evaluation into the next entry makes self-evaluation structurally impossible. SRC-1: `protocols/dialogue-thread-format.md`. Guarantee owner is the participating agent and retrospective checker; strength is protocol, not immutable enforcement. This record concerns the construction claim, not endorsement truth.

- doctrine conclusion status: claimed
- implementation conclusion status: wired
- operation conclusion status: uninspected

> 3. **Peer-eval, not self-eval.** Evaluation of a contribution lives in the **next** entry, not its own. It is structurally impossible to evaluate oneself.
> --- `protocols/dialogue-thread-format.md`

The checker has real D5 diagnostics, but one file per contribution does not prevent repeated authors, arbitrary references, rewrites or archival bypass. Its alternate-reference diagnostic is only WARN; previous-author equality requires exact reference matching. SRC-1: `tools/llm-wiki-audit.py`.

>                     elif previous and ref != previous.name:
>                         self.report(WARN, "Protocol", "L2", "D4", entry, "last_eval.ref",
>                                     f"last_eval.ref points to {ref}, expected {previous.name}",
>                                     "Point last_eval.ref at the immediately previous entry")
> --- `tools/llm-wiki-audit.py`

>                 if ref == previous.name and previous_frontmatter.get("author") == author:
>                     self.report(HARD, "Cascade", "L2", "D5", entry, "last_eval.ref",
>                                 "Author evaluates their own previous contribution",
>                                 "Have a different participant evaluate the previous contribution")
> --- `tools/llm-wiki-audit.py`

#### RT-CLM-canon-enforcement
Label: Canon admission contract exceeds audit checks

Claimed operation: full/soft canonical structural knowledge requires specified consensus and user approval; significant modifications invalidate endorsements. Doctrine owner: agents/authors/user, strength protocol. The implementation contains a narrower accepted/pending check, not the canonical contract. Its scope is path-based structural-page classification, skipping dialogue/honest/notes and selected logs; it is neither exactly the document-type scope described in the protocol nor an endorsement-authentication mechanism. SRC-1: `protocols/multi-ai-consensus.md`, `tools/llm-wiki-audit.py`.

- doctrine conclusion status: claimed
- implementation conclusion status: absent
- operation conclusion status: uninspected

> If a document is significantly modified (>30% change or structural reorganization), all statuses (except for the author of the changes) automatically transition to `stale`. A `stale` status blocks a document from full `canonical` status until it is reviewed and updated.
> --- `protocols/multi-ai-consensus.md`

>             if "consensus" in frontmatter and lifecycle == "accepted":
>                 consensus = frontmatter["consensus"]
>                 if isinstance(consensus, dict):
>                     for agent_name, status in consensus.items():
>                         if isinstance(status, str) and status.startswith("pending"):
> --- `tools/llm-wiki-audit.py`

This absent implementation conclusion is limited to enforcement of canonical/stale/user-approval obligations, not to all consensus diagnostics. Required external contract: downstream agents or host perform and honor those transitions.

### Evidenced absences

#### RT-ABS-runtime-orchestration
Label: Shipped agent orchestration and write interception absent

- implementation conclusion status: absent

Searched boundary: complete tracked tree of SRC-1 at `126749634d1c8c2fd6141f59711c882c2d629699`, complete sole executable `tools/llm-wiki-audit.py`, README entry paths and all four protocols. Query: tracked-file enumeration plus `write_text|open\(|subprocess|requests|provider|model|canonical|awaiting-crystallization|migration_mode|target|last_eval` in the executable, followed by full control-flow inspection. No model caller, agent scheduler, write interceptor, remote executor, extension loader, cryptographic verifier or downstream wiki driver is shipped. Documentation explicitly assigns execution to the adopting agents/host and defers signatures. This prevents attributing enforcement, model selection, context loading, transaction isolation or automated canon generation to the package; it says nothing about external hosts implementing them. SRC-1: `README.md`, `tools/llm-wiki-audit.py`, `protocols/integrity-audit.md`.

> - Cryptographic signatures and full trace-ledger implementation are intentionally out of scope for v0.2.0.
> --- `README.md`

### Behavioral-authority paths

#### RT-BAP-protocol-guidance
Label: Copied protocol guidance to adopting agents

Consumer: external wiki agents/users. Channel: copied/adapted Markdown instructions, thread rules and consensus procedures. Force: intended normative guidance through natural-language interpretation, not executed permissions or authenticated mandate. Horizon: later adopting sessions while the copied procedures remain in use; actual delivery/compliance is uninspected. Adoption is optional and instructions may be locally adapted. SRC-1: `README.md`, `protocols/rolespace-coordination.md`, `protocols/multi-ai-consensus.md`. The minimal adoption passage is retained in [RT-OBJ-coordination-protocols](#rt-obj-coordination-protocols).

#### RT-BAP-audit-exit
Label: Audit diagnostics and process status to caller

Consumer: invoking human/agent/host process. Channel: printed findings and CLI exit code. Force: a process-result gate only if caller honors it; proposed repairs are advisory text and no mutation is applied. Horizon: current audit invocation; protocol-retained reporting may reach later work through externally implemented writes. SRC-1: `tools/llm-wiki-audit.py`, `protocols/integrity-audit.md`. Terminal-exit evidence is retained in Runtime account and dispatch evidence in [RT-RTE-audit-invocation](#rt-rte-audit-invocation).

## Annotations

none
