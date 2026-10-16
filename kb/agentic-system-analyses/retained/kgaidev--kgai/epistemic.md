---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "kgai epistemic routes: decision reasons, structural authority, bounded recall, integrity checks and capture evaluation."
run-id: AAS-2026-10-14-kgai-54bcae52e039-01
reviewed-boundary: "0ac7f1fae4528805c1d5f504c1bfd6cc34ac953b"
---

# kgai epistemic report

## Source-and-claim boundary

The question is how kgai acquires or produces engineering assertions and reasons, checks them, grants reliance, and changes later behavior. Scope and exclusions: see [boundary](boundary.md#boundary-and-evidence); source identity and evidence layers: see [Source register](boundary.md#source-register). The selected whole-system boundary includes shipped model-facing instructions, CLI, hooks, optional capture mod and editor reader. It does not include host/provider internals or remote service implementations.

The supplied runtime is provisional evidence, not an inspection limit. This member directly inspected SRC-1 CLI dispatch and decoding, event construction and authority assignment, recall output shaping, lexical ranking, structural conflict detection, historical replay, export/status/doctor, the skill, conflict command, optional-mod proposal parser, README claims and complete host-smoke harness. Other runtime mechanisms below are explicitly supplied findings. No target execution, supplied observed run or causal experiment establishes actual capture, decision truth, model compliance or benefit. Exact provider state and fork-context copying are uninspected; this prevents classifying individual model-produced assertions as imported, entailed or ampliative from their actual inputs.

The product claims are [RT-CLM-structural-capture](runtime.md#rt-clm-structural-capture), [EPI-CLM-full-story](#epi-clm-full-story), [EPI-CLM-semantic-conflicts](#epi-clm-semantic-conflicts) and [EPI-CLM-dead-ends](#epi-clm-dead-ends). They describe decision memory and later reliance, not a universal truth oracle. The skill expressly excludes unacted-on research findings and recommendations; this operational scope is not itself a product defect (SRC-1: `skills/knowledge-graph/SKILL.md`).

| Entry point or operation | Source path | Coverage and records | Limit and conclusion prevented |
|---|---|---|---|
| Foreground capture; explicit decision/review/ask | `src/main.go`, `src/internal/engine/engine.go`, `skills/knowledge-graph/SKILL.md` | Direct dispatch, decoder, builder and skill; see [RT-RTE-foreground-capture](runtime.md#rt-rte-foreground-capture), [EPI-OBJ-decision-reasons](#epi-obj-decision-reasons), [EPI-OBJ-decision-mutations](#epi-obj-decision-mutations) | Command-specific confirmation differences supplied by runtime; no observed authorship or evidence-consuming truth acceptance |
| SessionStart/Stop/turn; install | `hooks/hooks.json`, `hooks/auto-capture-stop.sh`, `src/internal/turn/turn.go`, `scripts/install.sh` | Supplied [RT-RTE-foreground-capture](runtime.md#rt-rte-foreground-capture), [RT-RTE-engine-install](runtime.md#rt-rte-engine-install) | Hook delivery and deployed binary unobserved |
| Optional capture fork and registered tools | `mods/kgai-mod/hooks/register.tsx` | Direct prompt/parser; complete registration and ingestion supplied by [RT-RTE-fork-capture](runtime.md#rt-rte-fork-capture) | No separate semantic validator exposed in inspected parser or supplied dry-run/ingest account; host isolation unobserved |
| Resolve/query/context/search/history | `src/internal/engine/reads.go`, `src/internal/engine/search.go` | Direct recall shaping/ranking; query and identity admission supplied by [RT-RTE-query-read](runtime.md#rt-rte-query-read), [RT-RTE-foreground-capture](runtime.md#rt-rte-foreground-capture); [EPI-RTE-recall-shaping](#epi-rte-recall-shaping) | Full alias traversal/native query semantics not directly reassessed; no complete-retrieval guarantee |
| Conflicts and user resolution | `src/internal/engine/reads.go`, `commands/kg-conflicts.md` | Direct [EPI-RTE-branch-check](#epi-rte-branch-check) | Structural branch result does not establish disagreement in proposition meaning |
| As-of | `src/internal/engine/reads.go` | Direct [EPI-RTE-historical-replay](#epi-rte-historical-replay) | Full native projection/bulk equivalence not inspected here; no actual historical reconstruction demonstrated |
| Sync/rebuild/rotate/remote | `src/internal/engine/engine.go`, `src/internal/remote/objectsync.go` | Supplied [RT-RTE-team-sync](runtime.md#rt-rte-team-sync) | Full transport and retirement branches not directly reassessed; no universal integrity or convergence conclusion |
| Config/trust/prompt | `src/main.go`, `src/internal/store/settings.go`, `hooks/inject-prompt.sh` | Supplied [RT-RTE-config-admission](runtime.md#rt-rte-config-admission) | Human identity and convention quality not verified |
| Export/status/info/doctor | `src/internal/engine/reads.go` | Direct [EPI-RTE-doctor-check](#epi-rte-doctor-check); export emits selected graph fields and optional digest; status reports counts without doctor checks | Export omits rationale and computes a digest, not a truth verdict; status success is not integrity acceptance |
| Editor and kgread | `src/internal/view/model.go`, `src/internal/replay/projection.go` | Supplied [RT-RTE-editor-read](runtime.md#rt-rte-editor-read) | Complete rendering/protocol not reassessed; consumer integrity gate differs from engine |
| Host smoke evaluation | `tests/host-smoke.sh` | Direct [EPI-RTE-capture-evaluation](#epi-rte-capture-evaluation) | No execution results; test criterion is count, not truth or explanation |
| Init/help/version and packaging | `src/main.go` | Direct dispatch; setup/capability context supplied by runtime | No independently identified truth-acceptance route; detailed setup not audited here |
| Other shipped tests, benchmark tooling, demo fixtures | `tests/`, `src/tools/`, `examples/` | Included but not fully inspected in this member | Prevents system-complete negative about all evaluators and verification of scale assertions; fixtures are not production evidence |

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-decision-reasons](#epi-obj-decision-reasons) | Assertions about what was chosen, why and rejected alternatives; particular proposition not determinable without a grounded instance | see record | SRC-1 `src/internal/engine/engine.go` | Rationale optional; caller authorship is not evidence provenance |
| [EPI-OBJ-decision-mutations](#epi-obj-decision-mutations) | Symbolic structural assertions and operational updates; declarative relationships may be truth-apt, preferences need not be | see record | SRC-1 `src/internal/engine/engine.go` | Graph validity does not establish correspondence with code or domain |
| [RT-OBJ-knowledge-graph](runtime.md#rt-obj-knowledge-graph) | Primarily capture/recall policy; truth-apt mechanism descriptions separately assessable | see record | SRC-1 `skills/knowledge-graph/SKILL.md` | Instruction supply is not compliance |
| [RT-OBJ-capture-prompt](runtime.md#rt-obj-capture-prompt) | Primarily policy for proposing NONE or decision JSON | see record | SRC-1 `mods/kgai-mod/hooks/register.tsx` | Model reasoning and copied context opaque |
| [RT-OBJ-trusted](runtime.md#rt-obj-trusted) | Approval state, not warrant for project conventions | see record | SRC-1 `src/internal/store/trust.go` | Caller authorization state does not authenticate a human |
| [RT-CMP-host-model](runtime.md#rt-cmp-host-model) | Distributed-parametric state cannot be individuated into warranted propositions from this source | see record | SRC-1 `mods/kgai-mod/hooks/register.tsx` | Version/fixity/provider internals: see record; no weight-update evidence inferred from memory writes |

## Authority-route ledger

All entries describe architecture, not observed operation. Shared fields owned by cited records say `see`; each entry separates its epistemic classification from software admission. Linked entries separate checking, disposition and retention even when one implementation performs them.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-foreground-capture](runtime.md#rt-rte-foreground-capture) | content transformation | implemented | [EPI-OBJ-decision-reasons](#epi-obj-decision-reasons) | truth-apt transformation: indeterminate | see route | see route; model selects structural choice, no expected-answer oracle | see route | see route | Proposal supply | Candidate only; imports of past decisions acquire content with unknown source warrant; actual task-generated claims lack inspected input/output lineage | Can proceed toward ingest | see [RT-BAP-capture-policy](runtime.md#rt-bap-capture-policy) | SRC-1 `skills/knowledge-graph/SKILL.md` | [RT-CLM-structural-capture](runtime.md#rt-clm-structural-capture) | none | Cannot infer ampliation just because entailment is unproved |
| [RT-RTE-fork-capture](runtime.md#rt-rte-fork-capture) | content transformation | implemented | [RT-OBJ-capture-prompt](runtime.md#rt-obj-capture-prompt) | truth-apt transformation: indeterminate | see route | see route | see route | see route | NONE or parsed proposal controls continuation toward ingest | No semantic truth license; fork context is opaque | Eligible proposal can reach dry-run/real ingest | see route | SRC-1 `mods/kgai-mod/hooks/register.tsx` | [RT-CLM-structural-capture](runtime.md#rt-clm-structural-capture) | none | NONE is capture selection, not falsification of a candidate |
| [RT-RTE-foreground-capture](runtime.md#rt-rte-foreground-capture), [RT-RTE-fork-capture](runtime.md#rt-rte-fork-capture) | check/evidence production | implemented | [EPI-OBJ-decision-mutations](#epi-obj-decision-mutations) | no content change | Payload shape, required title, mutation operation and reference consistency | see routes; deterministic parser/resolver, schema domain | see routes | Errors or successful resolution/dry-run | Enforcing veto within covered paths | Typed admissibility only; not truth, attachment completeness or reason quality | Malformed candidates blocked; no-element candidates warned, not rejected | see routes | SRC-1 `src/main.go` | [RT-CLM-structural-capture](runtime.md#rt-clm-structural-capture) | policy/engine gap | Unknown-field gate is CLI-specific; direct typed API and synced events differ |
| [RT-RTE-foreground-capture](runtime.md#rt-rte-foreground-capture), [RT-RTE-fork-capture](runtime.md#rt-rte-fork-capture) | disposition/acceptance | implemented | [EPI-OBJ-decision-mutations](#epi-obj-decision-mutations) | no content change | Admission as a recorded structural decision | see routes; model/software/human roles differ by command, mode and UI | see routes | see routes | Operational admission; no evidenced truth acceptance | No evidence-consuming decision against truth criterion for an intended knowledge use found in these admission paths | Accepted payload may govern touched target elements | see [RT-BAP-decision-recall](runtime.md#rt-bap-decision-recall) | SRC-1 `src/internal/engine/engine.go` | [RT-CLM-structural-capture](runtime.md#rt-clm-structural-capture) | admission is not epistemic acceptance | User confirmation can judge choice; its evidence and criterion are not established by button/command alone |
| [RT-RTE-foreground-capture](runtime.md#rt-rte-foreground-capture) | retention | implemented | [EPI-OBJ-decision-reasons](#epi-obj-decision-reasons), [EPI-OBJ-decision-mutations](#epi-obj-decision-mutations) | truth-apt transformation: non-ampliative reshaping | Event append and graph projection | see route | see route | see route | Durable log eligibility for later recall | Preserves submitted rationale; its source warrant remains unknown | Mutation-derived authority and supersession change recall heads | see [RT-BAP-decision-recall](runtime.md#rt-bap-decision-recall) | SRC-1 `src/internal/engine/engine.go` | [EPI-CLM-full-story](#epi-clm-full-story), [EPI-CLM-dead-ends](#epi-clm-dead-ends) | none | Retention and graph connection before epistemic acceptance are not lifecycle integration |
| [EPI-RTE-recall-shaping](#epi-rte-recall-shaping) | content transformation | implemented | [EPI-OBJ-decision-reasons](#epi-obj-decision-reasons) | truth-apt transformation: indeterminate | Rationale to abbreviated recall text | see record | see record | see record | Output shaping | Warrant may degrade through omitted scope/qualification; no checked semantic preservation | Shortened text delivered instead of full rationale | see record | SRC-1 `src/internal/engine/reads.go` | [EPI-CLM-full-story](#epi-clm-full-story) | recall completeness gap | Full history is a separate recovery path, not automatic restoration of omissions |
| [EPI-RTE-recall-shaping](#epi-rte-recall-shaping), [RT-RTE-query-read](runtime.md#rt-rte-query-read), [RT-RTE-editor-read](runtime.md#rt-rte-editor-read) | operational admission/selection/consumption | implemented | [EPI-OBJ-decision-reasons](#epi-obj-decision-reasons), [EPI-OBJ-decision-mutations](#epi-obj-decision-mutations) | no content change | Selection for caller's read | see records | see records | see records | Ranking/informational delivery, not semantic endorsement | Graph-head status licenses current recorded choice, not correct explanation; lexical score licenses match, not truth | Model instructed to respect or supersede; editor human informed | see [RT-BAP-decision-recall](runtime.md#rt-bap-decision-recall) | SRC-1 `src/internal/engine/reads.go` | [EPI-CLM-full-story](#epi-clm-full-story), [EPI-CLM-dead-ends](#epi-clm-dead-ends) | none | Delivery, activation and benefit remain separate |
| [EPI-RTE-branch-check](#epi-rte-branch-check) | check/evidence production | implemented | [EPI-OBJ-decision-mutations](#epi-obj-decision-mutations) | truth-apt transformation: entailed derivation | More than one authoritative unsuperseded head per element | see record; symbolic projection domain | see record | see record | Conflict listing prompts resolution | Derives branch count from encoded authority relation, not contradiction in meaning | Surfaces choices for caller; does not arbitrate | see record | SRC-1 `src/internal/engine/reads.go` | [EPI-CLM-semantic-conflicts](#epi-clm-semantic-conflicts) | semantic claim exceeds predicate | Warrant conditional on projection/input fidelity |
| [EPI-RTE-branch-check](#epi-rte-branch-check) | disposition/acceptance | doctrine only | [EPI-OBJ-decision-mutations](#epi-obj-decision-mutations) | no content change | User resolution of competing branches | see record; user criterion not prescribed beyond intended state and rationale | see record | New ingest should re-express winning state and supersede heads | Advisory command workflow; subsequent ingest has engine force | Choosing an intended structure is not a truth-validation result | Resolution can change current heads and links | see record | SRC-1 `commands/kg-conflicts.md` | [EPI-CLM-semantic-conflicts](#epi-clm-semantic-conflicts) | none | The instruction is implemented as shipped text, but the semantic resolution procedure is doctrine, not observed adjudication |
| [RT-RTE-team-sync](runtime.md#rt-rte-team-sync) | check/evidence production | implemented | [EPI-OBJ-decision-reasons](#epi-obj-decision-reasons), [EPI-OBJ-decision-mutations](#epi-obj-decision-mutations) | no content change | Event hashes, decision IDs and transport chain/prefix integrity | see route | see route | see route | Enforcing in covered admission paths | Integrity consistency only; no source authentication or rationale truth follows | Invalid events skipped/rejected as specified by path | see route | SRC-1 `src/internal/engine/engine.go` | none | consumer asymmetry | Editor lacks same verification; external services uninspected |
| [RT-RTE-team-sync](runtime.md#rt-rte-team-sync) | retention | implemented | [EPI-OBJ-decision-reasons](#epi-obj-decision-reasons), [EPI-OBJ-decision-mutations](#epi-obj-decision-mutations) | truth-apt transformation: acquisition/import | Remote decisions to local log/projection | see route | see route | see route | Accepted transport content becomes recallable | Carries supplied assertions; source warrant unknown, hashes alone do not establish it | May add heads/conflicts and change later views | see route | SRC-1 `src/internal/remote/objectsync.go` | [EPI-CLM-semantic-conflicts](#epi-clm-semantic-conflicts) | none | No per-rationale human approval in supplied route |
| [EPI-RTE-historical-replay](#epi-rte-historical-replay) | content transformation | implemented | [EPI-OBJ-decision-mutations](#epi-obj-decision-mutations) | truth-apt transformation: non-ampliative reshaping | Retained events at/before cutoff to historical graph | see record | see record | see record | Informational return | Historical recorded structure, conditional on filtered events and replay fidelity, not real-world historical truth | Caller can inspect prior structure | see record | SRC-1 `src/internal/engine/reads.go` | [EPI-CLM-full-story](#epi-clm-full-story) | none | This entry does not establish universal replay equivalence |
| [EPI-RTE-doctor-check](#epi-rte-doctor-check) | check/evidence production | implemented | [EPI-OBJ-decision-mutations](#epi-obj-decision-mutations) | no content change | Stored hash consistency and local shard chain | see record | see record | see record | Advisory diagnostics | Scoped integrity verdict, not truth of decisions | Caller receives problems; inspected doctor code does not withdraw decisions | see record | SRC-1 `src/internal/engine/reads.go` | none | none | Status and canonical export digest are weaker/different checks |
| [EPI-RTE-capture-evaluation](#epi-rte-capture-evaluation) | check/evidence production | implemented | [EPI-OBJ-decision-mutations](#epi-obj-decision-mutations) | no content change | Capture count for structural vs cosmetic fixture | see record | see record | see record | Test verdict and shell exit | Count fit for two task cases only; no semantic correctness, mechanism or transfer license | Can fail manual test command; does not revise product automatically | see record | SRC-1 `tests/host-smoke.sh` | [RT-CLM-structural-capture](runtime.md#rt-clm-structural-capture) | none | No runs supplied; no ablation or causal attribution |
| [RT-RTE-config-admission](runtime.md#rt-rte-config-admission), [RT-RTE-engine-install](runtime.md#rt-rte-engine-install) | operational admission/selection/consumption | implemented | [RT-OBJ-trusted](runtime.md#rt-obj-trusted) | non-truth-apt policy/content update: capture conventions, store choice or executable capability | see routes | see routes | see routes | see routes | Approval fingerprint or executable readiness controls use | Neither convention truth nor product improvement licensed | Changes model guidance/read destination or later tool implementation | see routes and [RT-BAP-installed-engine](runtime.md#rt-bap-installed-engine) | SRC-1 `src/internal/store/settings.go` | none | none | Not evidence-responsive parameter adaptation; deployed effects unobserved |

No route of epistemic acceptance followed by lifecycle integration was established in the directly inspected capture, conflict, recall and diagnostic paths. This is not a system-complete absence: other shipped evaluators remain uninspected. Operational graph integration is established independently of that limit.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-structural-capture](runtime.md#rt-clm-structural-capture) | see record | SRC-1 `skills/knowledge-graph/SKILL.md`; doctrine/design | see record | [RT-RTE-foreground-capture](runtime.md#rt-rte-foreground-capture), [RT-RTE-fork-capture](runtime.md#rt-rte-fork-capture), [EPI-RTE-capture-evaluation](#epi-rte-capture-evaluation) | None supplied | Count harness has no mechanism ablation and does not verify rationale | Capture/recall wiring and policy exist | Hook eligibility, confirmation alternatives and unobserved model compliance prevent automatic-completion guarantee |
| [EPI-CLM-full-story](#epi-clm-full-story) | see record | SRC-1 `README.md`; doctrine/design | see record | [RT-RTE-foreground-capture](runtime.md#rt-rte-foreground-capture), [EPI-RTE-recall-shaping](#epi-rte-recall-shaping), [EPI-RTE-historical-replay](#epi-rte-historical-replay) | None supplied | No capture completeness or replay equivalence demonstration | Retained decision history can expose submitted reasons | Default recall truncates/caps/selects; unrecorded reasons cannot be recovered; full story is not universally warranted |
| [EPI-CLM-semantic-conflicts](#epi-clm-semantic-conflicts) | see record | SRC-1 `README.md`; doctrine/design | see record | [EPI-RTE-branch-check](#epi-rte-branch-check), [RT-RTE-team-sync](runtime.md#rt-rte-team-sync) | None supplied | No semantic contradiction evaluator established in branch predicate | Competing authority heads are surfaced | Compatible concurrent changes can be flagged; conflicting assertions on different elements can escape this check |
| [EPI-CLM-dead-ends](#epi-clm-dead-ends) | see record | SRC-1 `README.md`; doctrine/design | see record | [RT-RTE-foreground-capture](runtime.md#rt-rte-foreground-capture), [EPI-RTE-recall-shaping](#epi-rte-recall-shaping) | None supplied | No evidence that recorded failure reasons are tested or later affect action | Dead-end decisions can remain searchable/history-visible without governing an existing element | Avoiding repeated failure and having proved an approach wrong exceed storage/delivery alone |

## Bounded conclusion

kgai retains caller-supplied choices and reasons and deterministic graph mutations. Its model instructions make those reasons relevant to later tasks, while authority-bearing mutations determine which choices govern an element in ordinary recall. This is operational reliance before established epistemic acceptance, not an implemented evidence-consuming truth certification ([RT-RTE-foreground-capture](runtime.md#rt-rte-foreground-capture), [EPI-OBJ-decision-mutations](#epi-obj-decision-mutations)). Imports acquire past claims with unknown source warrant; hashes and actor fields do not authenticate the historical evidence behind a rationale.

Model capture can summarize task experience, but accessible source does not establish actual content lineage. It therefore leaves imported, non-ampliative, entailed and ampliative alternatives unresolved for individual model outputs. Numerical provider state is independently opaque, not evidence that all knowledge production is absent ([RT-CMP-host-model](runtime.md#rt-cmp-host-model), [RT-RTE-fork-capture](runtime.md#rt-rte-fork-capture)).

The deterministic branch check derives a scoped proposition about encoded authority heads. It neither tests an engineering explanation nor detects all semantic disagreements. The concrete compatible-branch countercase in [EPI-RTE-branch-check](#epi-rte-branch-check) prevents equating branch detection with semantic falsification. Software ingestion checks schema and identities; sync/rebuild checks scoped integrity. Doctor reports problems without implementing withdrawal. These evaluators have different targets and consumers; none becomes a universal answer oracle.

Ordinary recall ranks and selects recorded material. It can omit historical reasons and truncate a decisive qualifier; full history is separately reachable. Thus source text preserved in the log can arrive with degraded warrant at the model consumer ([EPI-RTE-recall-shaping](#epi-rte-recall-shaping)). Historical replay returns recorded structure, not a newly accepted explanation of it. The skill's respect-or-supersede policy is an advisory behavioral-authority path across tasks, with actual dependence and benefit unobserved ([RT-BAP-decision-recall](runtime.md#rt-bap-decision-recall)).

The host-smoke harness supplies a reference count for two task types and an operative test verdict, not correctness evidence for a retained reason or the effectiveness of a component. No result is supplied. Config approval and installation can change instructions or executable capability without a truth-apt route; no direct evaluation-fed policy improvement was established in those routes. Learning, reflection, theory-builder conditions and self-improvement remain independent of capture automation; their supplied runtime assessments are not strengthened by these source-only evaluator findings.

## Shared records

### Operative objects

#### EPI-OBJ-decision-reasons
Label: Decision title and rationale

Part of: [RT-RTE-foreground-capture](runtime.md#rt-rte-foreground-capture)

This is the natural-language retained-content part of that route, not a replacement for its control flow. Closest other overlap: [RT-RTE-fork-capture](runtime.md#rt-rte-fork-capture) can propose the same payload class. Source-native identity: `Decision.Title` and `Decision.Rationale`; representational form: natural language; substrate: event JSON and derived graph fields. Author and refs accompany content but do not establish the evidence behind its propositions. Rationale is copied from input and can be empty. Particular truth-apt content, scope and non-entailment are not determinable without a provenance-grounded instance. SRC-1 implementation: `src/internal/engine/engine.go`.

> d := event.Decision{
> Title: di.Title,
> Rationale: di.Rationale,
> Author: orDefault(di.Author, e.S.Config.Actor),
> Refs: joinRefs(di.Refs),
> Summary: summarize(di.Mutations),
> }
> --- `src/internal/engine/engine.go`

#### EPI-OBJ-decision-mutations
Label: Decision mutations and authority

Part of: [RT-RTE-foreground-capture](runtime.md#rt-rte-foreground-capture)

This is the symbolic retained-content part of that route. Source-native identity: `Mutations`, `Shapes`, `Targets`, `Supersedes`, `ProvenanceOnly`; representational form: symbolic operations and relations; substrate: event JSON and graph projection. Distinct from natural-language reasons: fixed engine rules grant operational authority independent of rationale quality. Fork capture and sync can introduce instances of this class too; those routes are not duplicate object declarations. SRC-1 implementation: `src/internal/engine/engine.go`.

> // Supersede the current head decision(s) of every target element.
> supSet := map[string]bool{}
> for id := range targets {
> for _, h := range e.headDecisions(g, id) {
> supSet[h] = true
> }
> }
> d.Supersedes = sortedKeys(supSet)
> d.Shapes = sortedKeys(shapes)
> d.Targets = sortedKeys(targets)
> --- `src/internal/engine/engine.go`

An existing-element bare upsert takes provenance but not authority; setting a property, creating an element, linking from it or explicit extra targeting takes authority. This countercase prevents treating every recorded reason as the current governing reason. See [RT-RTE-foreground-capture](runtime.md#rt-rte-foreground-capture) for required conditional admission/theory fields and evidence; this object adds no theory-process claim.

### Routes

#### EPI-RTE-recall-shaping
Label: Rationale selection and abbreviation

Part of: [RT-RTE-foreground-capture](runtime.md#rt-rte-foreground-capture)

The CLI recall-transformation part, distinct from production/admission. SRC-1 implementation: `src/internal/engine/reads.go`, `src/internal/engine/search.go`. Engine owns projection reads, weighted lexical ranking, output limits and `oneLine`; graph state and caller query provide context. This route sends selected existing content to a model or human, not a newly accepted theory.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Search hits carry title, abbreviated rationale, element names and score; context carries current links and up to four head reasons per element.
- Later read-back: Subsequent calls read retained decision content; history can separately return full rationale, including superseded decisions.
- Delegated visibility: CLI caller/host receives shaped JSON; no complete history is automatically forwarded.
- Selection predicate: Lexical query/weighted fields and limits for search; context selects elements then only authoritative unsuperseded heads for reasons.
- Invalidation or expiry: Supersession removes a reason from context heads without deleting its history; query/rank/limit changes delivery.
- Activation or effect: Implemented JSON supply and ranking; actual effect on later coding uninspected.
- Evidence limits: No semantic-preservation check accompanies abbreviation; full alias/context/native behavior not exhaustively audited.

Code selects/decides delivery; caller proposes query and limit; no per-read human approval or answer oracle. Operating mode: open recall, not an improvement trial. Recovery from omitted reasons is another history/query call, not automatic restoration. SRC-1:

> if len(byEl[eid]) >= 4 {
> continue
> }
> --- `src/internal/engine/reads.go`

> Extra: oneLine(asStr(r["rationale"])), Elements: els},
> --- `src/internal/engine/reads.go`

> func oneLine(s string) string {
> s = strings.TrimSpace(strings.ReplaceAll(strings.ReplaceAll(s, "\n", " "), "\r", " "))
> if len(s) > 160 {
> return s[:157] + "..."
> }
> return s
> }
> --- `src/internal/engine/reads.go`

Concrete deduction, not target execution: input rationale `Invoice remains standalone. ` (28 ASCII bytes), followed by 132 ASCII spaces and `Only for the pilot.` has 179 bytes. Replacements leave it unchanged; `TrimSpace` does not remove internal spaces; slicing keeps the first 157 bytes plus `...`. The operative search/context output therefore loses the scope condition while the full rationale remains stored. Semantic preservation is not established: potentially non-ampliative shortening versus changed apparent scope remains indeterminate. Ranking independently measures lexical overlap, not accuracy:

> h := d.hit
> h.Score = total
> out = append(out, scored{h, total})
> }
> sort.SliceStable(out, func(i, j int) bool { return out[i].score > out[j].score })
> --- `src/internal/engine/search.go`

#### EPI-RTE-branch-check
Label: Competing head detection and resolution

Part of: [RT-RTE-foreground-capture](runtime.md#rt-rte-foreground-capture)

This is its structural conflict-check subroute, not a semantic replacement for foreground judgment. Engine executes a query over encoded SHAPES authority and SUPERSEDES relations, lists groups, and a shipped command asks a model to explain branches and a user to choose. The intended resolution goes through the ordinary ingest route. SRC-1 implementation: `src/internal/engine/reads.go`; doctrine/design: `commands/kg-conflicts.md`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Element identity, competing head IDs and titles, optionally filtered by element-name substring.
- Later read-back: Conflict lists on later invocations reflect retained authority relations; a new authority-bearing decision can remove competing heads from that view while preserving history.
- Delegated visibility: CLI caller gets branch list; command requests history and user-facing explanation.
- Selection predicate: More than one unsuperseded authoritative head on the same element, not contradiction between proposition meanings.
- Invalidation or expiry: A later decision superseding both heads resolves the symbolic branch; bare existing-element upsert does not.
- Activation or effect: Listing is advisory; actual resolution and changed reliance unobserved. Subsequent ingest can enforce head replacement.
- Evidence limits: No semantic comparison in the inspected predicate; no supplied user adjudication or evidential truth criterion.

> WITH e, collect(d.id) AS heads, collect(d.title) AS titles
> WHERE size(heads) > 1
> RETURN e.id AS eid, e.name AS name, e.kind AS kind, heads, titles ORDER BY e.id`)
> --- `src/internal/engine/reads.go`

Countercase deduction: two concurrently recorded heads for Invoice, one setting `display=standalone`, the other setting `owner=billing`, satisfy the query's multiple-head condition even though both propositions can hold. Conversely, contradictory reasons attached to different elements are outside its same-element predicate. This licenses branch detection, not an exhaustive semantic conflict check.

> 3. Explain each branch and recommend a resolution.
> 4. On the user's decision, record ONE new decision that changes that element again — it
> automatically supersedes both heads. Its mutations must RE-EXPRESS the intended state
> of what the branches disagreed on (re-assert the winning link/prop, retire the losing
> one) — do not invent a marker property just to touch the element:
> --- `commands/kg-conflicts.md`

Admission roles: model proposes explanation/resolution, user decides under this command, engine can veto malformed ingest. Oracle: inapplicable — no expected correct engineering answer supplied. Operating mode: open user-led conflict resolution. Trigger: competing heads; guidance: re-express intended state with rationale; rollback/recovery: another superseding decision, history retained. Theory-process possibilities and limits stay in [RT-RTE-foreground-capture](runtime.md#rt-rte-foreground-capture); branch cardinality is not formulated criticism and does not strengthen those conditions.

#### EPI-RTE-historical-replay
Label: As-of historical projection

Distinct identity after comparison: [RT-RTE-team-sync](runtime.md#rt-rte-team-sync) projects synchronized current state; this CLI operation returns an ephemeral cutoff view without admitting new retained decisions. Engine owns timestamp parsing, filtering and native graph replay. SRC-1 implementation: `src/internal/engine/reads.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Cutoff timestamp, element names and live links in the ephemeral replay graph.
- Later read-back: Reads accumulated log content on each invocation; output itself is not retained by this route.
- Delegated visibility: CLI caller receives structure, not full decision rationale/evidence.
- Selection predicate: Recorded timestamp parses and is at/before cutoff, event hash verifies; date-only cutoff is end of that day; large slices use BulkLoad, small slices ApplyEvent.
- Invalidation or expiry: inapplicable — no retained output to invalidate; temporary graph removed after invocation.
- Activation or effect: Historical structure becomes inspectable; no actual caller behavior established.
- Evidence limits: Event-hash filtering is inspected; full replay/native equivalence and decision-ID gate equivalence are not established here.

> rt, perr := time.Parse(time.RFC3339, ev.RecordedAt)
> if perr != nil || rt.After(cut.UTC()) {
> continue // unparseable timestamp ⇒ excluded, not silently always-included
> }
> if !ev.Verify() {
> continue
> }
> kept = append(kept, ev)
> --- `src/internal/engine/reads.go`

Code decides membership; caller proposes cutoff; invalid timestamp rejects request and invalid event/timestamp excludes event. Answer oracle: inapplicable — reconstruction uses records, not a reference correct historical domain. Mode: requested historical read. No product/theory admission or policy adaptation occurs. Result does not entail source truth or the explanation of a historical choice.

#### EPI-RTE-doctor-check
Label: Doctor integrity diagnostics

No counterpart after comparison: [RT-RTE-team-sync](runtime.md#rt-rte-team-sync) checks at replay/sync admission, whereas Doctor returns diagnostics without rejecting or repairing the checked decisions. Engine owns hash recomputation across ReadAll and parent-chain checking on MyShard, then returns counts/problems/OK. SRC-1 implementation: `src/internal/engine/reads.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Problems for bad content hashes or broken local shard chain; OK is whether that problems list is empty.
- Later read-back: Reads retained log and graph on later calls; diagnostic result is not retained by Doctor itself.
- Delegated visibility: Caller receives diagnostics; host-smoke consumes its decision count, not its OK field.
- Selection predicate: All parsed events for hashes, own shard for chain continuity after first event; graph counts and conflicts supplement report.
- Invalidation or expiry: inapplicable — no retained diagnostic candidate or authority withdrawal.
- Activation or effect: Advisory return; inspected implementation does not delete, supersede or quarantine decisions on finding a problem.
- Evidence limits: Does not check rationale truth or all shard chains; successful counts do not imply complete integrity.

> for _, ev := range all {
> if !ev.Verify() {
> rep.Problems = append(rep.Problems, "bad content hash: "+ev.Hash)
> }
> }
> --- `src/internal/engine/reads.go`

> for i, ev := range mine {
> if i > 0 && (len(ev.Parents) == 0 || ev.Parents[0] != prev) {
> rep.Problems = append(rep.Problems, fmt.Sprintf("broken hash-chain at lamport %d", ev.Lamport))
> }
> prev = ev.Hash
> }
> --- `src/internal/engine/reads.go`

> rep.OK = len(rep.Problems) == 0
> return rep, nil
> --- `src/internal/engine/reads.go`

Code judges the integrity domain, caller requests check; no human contribution to the verdict or expected engineering-answer oracle. Mode: diagnostic read; no automatic repair/update selected. Comparison scope matters: Status explicitly omits chain checking; Export's canonical digest hashes selected graph fields and does not include rationale. Neither is acceptance of the retained reasons.

#### EPI-RTE-capture-evaluation
Label: Host smoke store-count verdict

No counterpart after comparison: [RT-RTE-foreground-capture](runtime.md#rt-rte-foreground-capture) is the work route; this manual evaluator drives a host on two authored fixture task types, reads persisted decision count and produces a verdict. SRC-1 implementation/design: complete `tests/host-smoke.sh`. Harness owns task setup, host invocation, doctor/search reads and final shell status; host/model executes work when a user deliberately runs it. No such run is supplied.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Per-run verdict/count/wanted count plus diagnostic titles/hook counts and final success/failure exit.
- Later read-back: Harness reads that run's retained store; it does not load prior verdicts to adapt later production capture.
- Delegated visibility: Manual operator sees output and artifacts; no product model-feedback delivery is implemented here.
- Selection predicate: Struct expects one decision, trivial expects zero; verdict is equality of persisted doctor count and wanted count.
- Invalidation or expiry: Each harness execution removes its work directory and reseeds independent fixture projects; results are not promoted into decision truth authority.
- Activation or effect: Test exit depends on all counts matching; no automatic production policy update or rollback follows.
- Evidence limits: Count success does not prove requested refactor occurred, rationale is true, recorded structure matches code or hook caused capture; no independent ablation or run evidence.

> want=1; [ "$TASK_TYPE" = trivial ] && want=0
> verdict=FAIL
> [ "$decisions" = "$want" ] && verdict=ok
> --- `tests/host-smoke.sh`

> printf '\n%s/%s runs matched the expectation. Artifacts under %s\n' "$recorded_total" "$RUNS" "$WORK"
> [ "$recorded_total" = "$RUNS" ]
> --- `tests/host-smoke.sh`

Oracle: authored task-type reference count supplied by harness author, used for verdict and final exit, not a reference reason or correct explanation. Human selects host/task/repeats; code decides verdict; model supplies candidate capture. Operating mode: bounded fixture experiment with optional repeated runs. No tested successor/product admission; trigger is explicit manual invocation. A false positive retained decision can pass the structural count criterion, and failure attribution is no finer than the complete host/plugin/model treatment. Diagnostic search uses empty text, while inspected `scoreDocs` returns nil for no query tokens; thus displayed titles cannot be assumed to audit captured semantics. This qualifies diagnostic visibility, not the count verdict:

> qToks := tokenize(query)
> if len(qToks) == 0 {
> return nil
> }
> --- `src/internal/engine/search.go`

### Claims

#### EPI-CLM-full-story
Label: Full retained story

Distinct from [RT-CLM-structural-capture](runtime.md#rt-clm-structural-capture): this is a completeness/reliance claim about later historical answers, not the policy to capture. SRC-1 doctrine/design: `README.md`.

> Nothing is ever overwritten, so you can always ask *how did this get this way?* and get
> the full story.
> --- `README.md`

Implemented retention/history supports recovery of recorded reasons, not reasons never captured or omitted by default recall. Compare [EPI-RTE-recall-shaping](#epi-rte-recall-shaping).

#### EPI-CLM-semantic-conflicts
Label: Only semantic conflicts

No counterpart after comparison with [RT-CLM-structural-capture](runtime.md#rt-clm-structural-capture); this is a sync/branch meaning claim. SRC-1 doctrine/design: `README.md`.

> Only real *semantic* conflicts surface — as branches
> you resolve with one new decision, and the resolution is kept too.
> --- `README.md`

[EPI-RTE-branch-check](#epi-rte-branch-check) establishes a same-element authority predicate, not equivalence to semantic disagreement. The countercase preserves the useful branch mechanism while bounding this wording.

#### EPI-CLM-dead-ends
Label: Remembered failed approaches

Distinct from [RT-CLM-structural-capture](runtime.md#rt-clm-structural-capture): this claim gives retained rejected choices warrant and a future avoidance effect. SRC-1 doctrine/design: `README.md`.

> **It even remembers the dead ends.** Rejected approaches stay in the graph with the
> reason they failed — so no engineer, and no AI, re-walks a path the team already proved
> wrong.
> --- `README.md`

Storage and later access are afforded/wired in [RT-RTE-foreground-capture](runtime.md#rt-rte-foreground-capture). Proof of wrongness, complete retrieval, behavioral activation and avoided failure are not established by that wiring.
