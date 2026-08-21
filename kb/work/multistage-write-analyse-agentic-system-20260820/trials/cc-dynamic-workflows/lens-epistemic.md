# Epistemic-architecture lens — run `AAS-20260820-CCDW-01`

Invoked procedure: `kb/instructions/analyse-external-system-epistemic-architecture.md`,
called conditionally at step 7 of `analyse-agentic-system`. This lens does **not** own the
boundary, the sources, the revision, the evidence tier, or any publication decision.
It annotates the orchestrator's canonical records (`CMP-*`, `OBJ-*`, `RTE-*`, `BAP-*`,
`CLM-*`) by existing ID and returns proposed new records unminted.

Wrapper constraints enforced: no source reacquisition; no boundary widening; no revision
change; evidence tier fixed at `doc-grounded`; `SRC-1` treated as **doctrine/design**;
no route recorded as `implemented`; no parallel ID namespace; no system-wide epistemic
grade; no publication decision.

---

## 1. Source-and-claim boundary

| Field | Value |
|---|---|
| System | Claude Code **dynamic workflows** — the Workflow orchestration facility inside the Claude Code harness. **Subsystem-only boundary**; no whole-system conclusion about Claude Code is drawn or licensed here. |
| Reviewed revision / version | `SRC-1` captured **2026-06-03**, documenting v2.1.154–v2.1.160-era behavior. Analysis cutoff 2026-06-03. Unchanged by this lens. |
| Declared scope | As packet §3. Included: `CMP-1`..`CMP-12`. Excluded (named): Claude Code's ordinary turn-by-turn loop, skills, agent teams (except the doc's own comparison table cited as doctrine); the sub-agent primitive's internals (`/en/sub-agents` not in bundle); the `/deep-research` script's source text; model inference and provider routing; billing internals; the general permission engine beyond the quoted workflow rows. |
| Analysis question (bounded epistemic subquestion) | Within the dynamic-workflows subsystem at the frozen 2026-06-03 documentation boundary, which material routes handle truth-apt content — acquiring, transforming, checking, disposing, retaining, or integrating it — and what does the documented evidence actually license about the system's stated warrant claim that adversarial multi-agent review and cross-checked synthesis yield "a more trustworthy result than a single pass" (`CLM-1`)? |
| Assessed route families | Deep-research knowledge pipeline (`RTE-E1`..`RTE-E6`); pattern-capability quality routes (`RTE-E7`, `RTE-E8`); context selection and delivery of truth-apt material (`RTE-X1`, `RTE-X2`, `RTE-X3`, `RTE-X6`); retention and recovery of truth-apt material (`RTE-S5`, `RTE-C6`); artifact retention and installation (`RTE-S1`, `RTE-S2`); operational admission of the orchestration (`RTE-C2`); external action by agents (`RTE-S4`); direct behavior/policy adaptation with no truth-apt object (`RTE-C1`, `RTE-C5`, `RTE-S3`) — included under the run's direct-adaptation exception because they are material to authority even though they do not themselves trigger this lens. |
| Unassessed route families | Sub-agent-internal reasoning, retrieval, and self-checking (`RTE-X1` terminates at the prompt; the agent's own loop is outside the bundle). Search-engine ranking and retrieval behind `RTE-E1`. Model inference and provider routing. Usage accounting (`RTE-S6`) and the disable surface (`RTE-C8`) — inspected by the orchestrator as control, carrying no truth-apt content; not re-analysed here. Command-registry name resolution (`RTE-C7`) beyond its authority effect. **No system-complete epistemic conclusion is drawn**, and none is available at this boundary. |
| Source register | `SRC-1` → `kb/sources/claude-code-dynamic-workflows-docs.md` (from `https://code.claude.com/docs/en/workflows`), captured 2026-06-03, genre `tool-announcement` — evidence layer **doctrine/design** (vendor documentation; its permission and limit tables are *doctrine about implemented behavior*, not inspected implementation). `SRC-2` → live-session tool-roster capture, 2026-08-20, host `2.1.237` — evidence layer **observed run**, scope roster-only / **negative**; supports **no positive finding** about the target. |
| Overall evidence tier | `doc-grounded`, fixed by the orchestrator (packet §5). No implementation inspected, no observed run of the target, no causal experiment. **No route in this lens reaches `implemented` or above.** |
| System knowledge-production / warrant claims | `CLM-1` (warrant claim, `SRC-1#when-to-use`); `CLM-2` (knowledge-production/operation claim, `SRC-1#bundled`); `CLM-3` (`#when-to-use`), `CLM-4` (`#how-it-runs`), `CLM-5` (`#limits`, `#cost`), `CLM-6` (`#limits`), `CLM-7` (`#when-to-use`), `CLM-8` (`#approve`) — the last six are operation, mechanism, control, isolation, design, and authority claims that bound what `CLM-1`/`CLM-2` can mean. |

### Missing evidence → conclusion prevented

| Missing evidence | Conclusion it prevents |
|---|---|
| `MG-1` — the `/deep-research` script text (excluded by boundary; never inspected) | Prevents recording `RTE-E1`..`RTE-E6` as `implemented`; prevents naming the vote's quorum, threshold, tie-handling, or abstention rule; prevents attributing the filter's criterion; prevents any component-level attribution among fan-out, cross-check, vote, filter, and synthesis. |
| `MG-2` — no observed run of any workflow (`SRC-2` is roster-only and negative) | Prevents **every** observed candidate state in output 4; prevents any acceptance, rejection, revision, or integration finding for `OBJ-9`, `OBJ-6`, `OBJ-4`, `OBJ-11`; prevents upgrading `CLM-2` from doctrine to reported or observed operation. |
| `MG-3` — no baseline contrast, metric, or interventional comparison anywhere in `SRC-1` | Prevents any support for the comparative core of `CLM-1` ("**more** trustworthy **than a single pass**"); prevents attributing trustworthiness to adversarial review, to cross-checking, or to agent count. |
| `MG-4` — `/en/sub-agents` not in the bundle | Prevents any conclusion about what a sub-agent reads, whether agent-internal checking exists, or what warrant `OBJ-4` carries when it enters `OBJ-3`. |
| `MG-5` — no documented claim-individuation step between fetched sources and voted claims | Prevents classifying `OBJ-9`'s transformation as non-ampliative reshaping vs. ampliative conjecture; prevents saying source warrant is preserved into `OBJ-9`. (See `RTE-E3/extract` and PROPOSED NEW RECORD 1.) |
| `MG-6` — no documented persistence, export, or downstream consumer of `OBJ-6` | Prevents any retention or lifecycle-integration conclusion about workflow reports. The negative is scoped to **documented routes**; it does not assert that no informal user-side retention exists. |
| `MG-7` — `OBJ-3` persistence past process exit is uninspected (packet Loop C) | Prevents any lineage conclusion about intermediate truth-apt results after the run's process ends. |
| `MG-8` — version gap: `SRC-1` pinned 2026-06-03 / v2.1.154–160; host under `SRC-2` runs 2.1.237; no changelog in bundle | Prevents any conclusion about present-day behavior of this subsystem. Preserved as a conflict, not resolved. |
| `MG-9` — no inspected instance of a non-bundled workflow script | Prevents generalizing any checking finding from `/deep-research` (`CMP-11`) to workflows as a class. |

---

## 2. Epistemic-object inventory

Orchestrator-owned generic identity (packet §6.2) is reused verbatim by ID; this lens adds
the truth-apt, lineage, role, and gap columns.

| Object ID | System name and description | Representational form | Source/input and lineage | Producer / consumer | Candidate truth-apt content or none | Claimed role | Evidence (source ID + anchor) | Gap / limit |
|---|---|---|---|---|---|---|---|---|
| `OBJ-1` | Workflow script text | symbolic (JavaScript) | authored by `CMP-3` from the user prompt (+ optionally an existing orchestrator pointed at) | producer `CMP-3` / consumers `CMP-1`, human reader, `RTE-C2` gate | **none** — an orchestration procedure, not a proposition. Its *phase list* summary is a description of itself, not a claim about the world. | "the plan moves into code"; "what's repeatable is the orchestration itself" (`CLM-7`) | `SRC-1#how-it-runs`, `#when-to-use` | What the authoring model read is undocumented (`MG-1`-adjacent); the shipped `/deep-research` text is boundary-excluded. |
| `OBJ-2` | `args` global | structured data | supplied by the user via `CMP-12` at invocation | producer `CMP-12` / consumer `OBJ-1` | **none** in the general case (parameters); may transport user-asserted content, unclassified here | invocation-time input instead of script editing | `SRC-1#args` | No example of truth-apt payload in `args` documented. |
| `OBJ-3` | Script variables / intermediate results | in-language values; **may hold natural-language agent output** | written by `RTE-X2` from `OBJ-4`; read by `RTE-X1`, `RTE-E3`..`RTE-E6` | producer/consumer `OBJ-1` in `CMP-1` | **heterogeneous container** — its truth-apt content is instances of `OBJ-4`, `OBJ-9`, `OBJ-11`; the container itself is not a proposition | keeps intermediate results out of `CMP-12`'s context (`CLM-3`) | `SRC-1#when-to-use`, `#how-it-runs` | `MG-7`: persistence past process exit uninspected. Container split is honoured by the packet's own `OBJ-4`/`OBJ-9`/`OBJ-11` rows. |
| `OBJ-4` | Agent result (with its prompt and recent tool calls) | natural-language + tool-call trace | produced by a sub-agent (`CMP-4`) from its prompt and its own tool use; agent-internal lineage **not in bundle** (`MG-4`) | producer `CMP-4` / consumers `OBJ-3` (via `RTE-X2`), `CMP-9` (via `RTE-S5`), human (via `RTE-X6`) | **yes** — natural-language findings about a codebase, the web, or a task; truth-apt over the task's domain | the unit the runtime tracks; the unit the human drills into | `SRC-1#watch-the-run`, `#how-it-runs` | No documented check applies to `OBJ-4` in the general case; checking is documented only inside `CMP-11`. |
| `OBJ-5` | Phase record (agent count, token total, elapsed time) | numeric/structured telemetry | measured by `CMP-1` instrumentation | producer `CMP-1` / consumer human via `CMP-6` | **yes, non-ampliative** — measurements truth-apt over the run itself | progress and cost visibility | `SRC-1#watch-the-run`, `#cost` | Instrumentation is uninspected; no accuracy claim, no reconciliation against billing (`#cost` excluded). |
| `OBJ-6` | Final report / answer | natural language; **cited** in the `/deep-research` case | synthesized by `RTE-E6` from surviving `OBJ-9` over `OBJ-10`; in the general case, from `OBJ-3` by undocumented means | producer `OBJ-1` / consumer `CMP-12` and the human | **yes** — the subsystem's sole delivered truth-apt product | "one report at the end instead of a turn-by-turn transcript"; "Claude's context holds only the final answer" | `SRC-1#run-a-bundled-workflow`, `#when-to-use` | `MG-6`: no documented retention, export, or downstream consumer. Lands in a context window with advisory force (`BAP-4`) and no documented persistence. |
| `OBJ-7` | Saved workflow command file | symbolic (JavaScript) + command name | a specific `OBJ-1` promoted by human keypress `s` | producer human via `RTE-S2` / consumer future sessions' resolver (`BAP-2`) | **none** — a procedure, not a proposition | turns a one-off run into a repeatable command | `SRC-1#save` | The promotion criterion is stated only as "if the run does what you wanted" — no recorded evaluation artifact. |
| `OBJ-8` | Permission consent record | configuration entry | written by human answer at `RTE-C2` | producer human / consumer `CMP-5` | **none** — an authorization, not a proposition | suppresses the launch prompt | `SRC-1#approve` | Scope differs by mode (per workflow+project vs. user-wide under Auto); no expiry documented. |
| `OBJ-9` | Deep-research **claim** | natural-language proposition **with source citation** | derived from `OBJ-10` by an **undocumented** individuation step (`MG-5`); then held in `OBJ-3`, then in `OBJ-6` | producer: undocumented (see `RTE-E3/extract`) / consumers `RTE-E3/check`, `RTE-E4`, `RTE-E5`, `RTE-E6` | **yes — the central truth-apt candidate of this subsystem** | the unit that is cross-checked, voted on, filtered, and cited | `SRC-1#bundled`, `#run-a-bundled-workflow` | `MG-5` blocks its transformation classification; `MG-1` blocks its check semantics; `MG-2` blocks every observed state. |
| `OBJ-10` | Fetched web source | external document | acquired from the open web by `RTE-E1`→`RTE-E2` | producer external / consumers `RTE-E3`, `RTE-E6` (citation target) | **yes, acquired** — external truth-apt content entering the system | the evidence base claims are checked against | `SRC-1#run-a-bundled-workflow`, `#bundled` | No documented source-quality, authority, recency, or independence assessment. Source warrant on import: **unknown**. |
| `OBJ-11` | Cross-check / vote result on a claim | disposition value | produced by `RTE-E3/check` + `RTE-E4` over `OBJ-9` and `OBJ-10` | producer sub-agents/script / consumer `RTE-E5` | **yes, second-order** — a proposition about `OBJ-9`'s standing across fetched sources | decides which claims survive into the report | `SRC-1#bundled` | Value space, threshold, and tie rules undocumented (`MG-1`). Not documented as retained or surfaced to the reader. |
| `OBJ-12` | Tool allowlist | configuration | user settings; inherited by `CMP-4` | producer user / consumer sub-agent tool executor | **none** — an authorization | bounds what agents may call | `SRC-1#approve` | Inheritance is stated, not inspected. |
| `OBJ-13` | Session effort setting (`ultracode`) | configuration | set by user via `/effort` | producer user / consumer `CMP-3` planning | **none** — a policy setting | makes Claude plan a workflow for every substantive task | `SRC-1#ultracode` | Session-scoped; resets on new session. |
| `OBJ-14` | Session model selection | configuration | set by user via `/model`; overridable per stage by `OBJ-1` | producer user/script / consumer `CMP-4` | **none** — a policy setting | controls which model backs each agent | `SRC-1#cost` | Per-stage routing is stated as a script capability, no shipped instance documented. |

**Omitted object families and the conclusions their omission prevents:** sub-agent-internal
scratch state and retrieved context (not in bundle — prevents any warrant conclusion about
how `OBJ-4` was produced); search-engine result ranking state (prevents any conclusion about
`OBJ-10` selection bias); provider-side inference state (prevents any conclusion about model
behavior). None of these can be reached without widening the boundary, which this lens must
not do.

---

## 3. Authority-route ledger

One functional kind per record. Linked rows share a base `RTE-*` ID with a functional
suffix; no new base IDs are minted. **Architectural status is recorded independently of
function, and — per the fixed `doc-grounded` tier — no record reaches `implemented`.**

### 3.1 Deep-research knowledge pipeline (`CMP-11`)

**`RTE-E1` — search fan-out**
- route function: `content transformation`
- architectural status: `doctrine only` — declared at `SRC-1#bundled`; no implementation inspected (`MG-1`), no run observed (`MG-2`)
- object/candidate id: `OBJ-10` (candidate source references entering)
- content/update relation: `truth-apt transformation: acquisition/import` — external search results enter the system; **source warrant: unknown** (no ranking, authority, or independence criterion documented). The angle decomposition that precedes the searches is a `non-truth-apt policy/content update: query set derived from the question`, undocumented in mechanism.
- transition or check target: none — this route acquires, it does not check
- evaluator/condition and domain: none documented; the external search engine's ranking is outside the boundary
- activation and timing: on `/deep-research <question>` invocation, first phase of the run
- possible or observed result: a set of source references; **no instance observed**
- implemented force: none demonstrable at this tier; within doctrine it seeds every later route
- epistemic authority and scope: **none** — acquisition licenses nothing about truth
- operational authority: permits the fetch phase to proceed
- behavioral-authority path: consumer `OBJ-1` in `CMP-1` | channel script control flow | force enforcing (`BAP-1`) | horizon one run
- evidence: `SRC-1#bundled`, `#run-a-bundled-workflow`
- claim IDs: `CLM-2`
- mismatch marker: none
- gap/limit: `MG-1`, `MG-2`. Prevents any conclusion about coverage, recall, or angle independence.

**`RTE-E2` — source fetch**
- route function: `content transformation`
- architectural status: `doctrine only`
- object/candidate id: `OBJ-10`
- content/update relation: `truth-apt transformation: acquisition/import` — document content enters; **source warrant preserved as received, i.e. unknown**; no filtering, dating, or provenance check documented
- transition or check target: none
- evaluator/condition and domain: none documented
- activation and timing: after `RTE-E1` within the run
- possible or observed result: fetched documents; **no instance observed**
- implemented force: none demonstrable at this tier
- epistemic authority and scope: **none** — imported content is acquired, not produced, and carries whatever warrant its origin had, which is unrecorded
- operational authority: supplies the material the cross-check operates on
- behavioral-authority path: consumer `OBJ-1` | channel script variables `OBJ-3` | force enforcing (`BAP-1`) | horizon one run
- evidence: `SRC-1#bundled`, `#run-a-bundled-workflow`
- claim IDs: `CLM-2`
- mismatch marker: none
- gap/limit: `MG-1`, `MG-2`. Prevents concluding that fetched sources are independent of one another — the property the later cross-check's value depends on.

**`RTE-E3/extract` — claim individuation from fetched sources (linked row; implied, not declared)**
- route function: `content transformation`
- architectural status: **`no route found within boundary`** — neither inspected implementation, observed operation, **nor doctrine** establishes this step. `SRC-1` speaks of "each claim" and of cross-checking sources "against each other" without ever documenting how a claim is individuated from a source.
- object/candidate id: `OBJ-9` (produced), from `OBJ-10`
- content/update relation: **`indeterminate`** — classifications still possible: (a) `non-ampliative reshaping` if a claim is a quotation or faithful extraction of a source's assertion; (b) `ampliative conjecture` if a model composes a proposition that no single source asserts. Evidence needed to decide: the script text or an observed run artifact showing claim provenance (`MG-1`, `MG-5`, `MG-2`).
- transition or check target: none — this is the step that *creates* the check target
- evaluator/condition and domain: none
- activation and timing: necessarily between `RTE-E2` and `RTE-E4`; undocumented
- possible or observed result: `OBJ-9` instances; **no instance observed**
- implemented force: not determinable
- epistemic authority and scope: **none established** — and because this step is unclassified, **no warrant can be traced from `OBJ-10` into `OBJ-9`**
- operational authority: none recorded
- behavioral-authority path: none recorded (no consequential consumer distinct from `RTE-E4`)
- evidence: `SRC-1#bundled` (presupposition only)
- claim IDs: `CLM-2` (presupposed by it)
- mismatch marker: **yes** — `CLM-2` asserts an operation over "each claim" while the source documents no route that produces claims. This is a doctrine-internal gap, not a doctrine-versus-implementation gap.
- gap/limit: `MG-5`. See PROPOSED NEW RECORD 1.

**`RTE-E3/check` — cross-check of a claim against the fetched sources (linked row)**
- route function: `check/evidence production`
- architectural status: `doctrine only`
- object/candidate id: `OBJ-9` checked; `OBJ-11` produced
- content/update relation: `no content change` to `OBJ-9`; produces a new second-order object `OBJ-11`
- transition or check target: **named before evaluator** — the target is an individual `OBJ-9` claim, and the domain is **agreement among the sources this run fetched**, not truth
- evaluator/condition and domain: model-backed sub-agents comparing `OBJ-10` documents "against each other" (`SRC-1#run-a-bundled-workflow`); a hybrid model procedure with no documented rubric; domain limited to retrieved-source agreement
- activation and timing: mid-run, after fetch, before vote
- possible or observed result: a per-claim corroboration signal; **no instance observed**
- implemented force: none demonstrable at this tier
- epistemic authority and scope: **at most** "corroborated across the sources retrieved by this run at this time" — explicitly **not** veracity, not source independence, not absence of common-origin error, not completeness of the evidence base
- operational authority: its result is consumed by `RTE-E5` to admit or drop the claim
- behavioral-authority path: consumer `RTE-E5` within `OBJ-1` | channel script variable `OBJ-11` | force enforcing on report membership | horizon one run
- evidence: `SRC-1#bundled`, `#run-a-bundled-workflow`
- claim IDs: `CLM-2`, and it is the closest shipped analogue to the mechanism `CLM-1` invokes
- mismatch marker: **yes, scope mismatch** — `CLM-1` speaks of *trustworthiness*; this route's evaluator domain reaches only inter-source agreement.
- gap/limit: `MG-1`, `MG-2`, `MG-4`. Prevents naming the rubric, the comparison unit, or the handling of a claim supported by exactly one source.

**`RTE-E4` — vote on each claim**
- route function: `check/evidence production` (aggregation of the cross-check into a per-claim result)
- architectural status: `doctrine only`
- object/candidate id: `OBJ-9` (target), `OBJ-11` (result)
- content/update relation: `no content change`
- transition or check target: the individual claim `OBJ-9`; domain: aggregate agent judgement over the cross-check evidence
- evaluator/condition and domain: a multi-agent **vote** — plural model evaluators; quorum, threshold, weighting, abstention, and tie rules **all undocumented**
- activation and timing: after cross-check, before filtering
- possible or observed result: survive / not survive; **no instance observed**
- implemented force: none demonstrable at this tier
- epistemic authority and scope: **majority-of-model-evaluators agreement over retrieved sources** — an aggregation of judgements, not a measurement; it licenses no claim about accuracy, and voting agreement among instances of the same model is not evidence of independence
- operational authority: determines `RTE-E5`'s input
- behavioral-authority path: consumer `RTE-E5` | channel `OBJ-11` | force enforcing on report membership | horizon one run
- evidence: `SRC-1#bundled`
- claim IDs: `CLM-2`
- mismatch marker: none within doctrine; **unknown** against implementation
- gap/limit: `MG-1`. Prevents stating the decision rule, and therefore prevents predicting the filter's behavior on any given claim.

**`RTE-E5` — filter (survival disposition)**
- route function: `disposition/acceptance` — kept strictly separate from the checking rows above
- architectural status: `doctrine only`
- object/candidate id: `OBJ-9`
- content/update relation: `no content change` to the surviving claim; the run's claim set is reduced
- transition or check target: transition of each `OBJ-9` from candidate to included-in-report or dropped
- evaluator/condition and domain: consumes `OBJ-11`; the criterion is stated only as "didn't survive cross-checking", i.e. **the criterion is named by outcome, not by rule**
- activation and timing: before synthesis, at report-assembly time
- possible or observed result: `included` / `dropped`; **no instance observed**
- implemented force: none demonstrable at this tier; within doctrine, enforcing on report membership
- epistemic authority and scope: **this is the only place in the subsystem where anything resembling an acceptance transition occurs, and it is a weak one.** Survival is *admission by non-rejection*, not an affirmative recorded decision; the doc names **no intended use**, **no reliance scope**, and **no persisted acceptance artifact**. It does not license reliance on a surviving claim beyond "not contradicted by the sources this run happened to fetch".
- operational authority: permits a claim to appear in `OBJ-6`; blocks the rest from appearing
- behavioral-authority path: consumer human + `CMP-12` reader | channel `OBJ-6` via `RTE-X3` | force **advisory** (`BAP-4`) | horizon session / turn
- evidence: `SRC-1#bundled`, `#run-a-bundled-workflow`
- claim IDs: `CLM-2`
- mismatch marker: **yes** — the doc presents the filter as a report-quality property, but records no criterion, no acceptance artifact, and no scope; dropped claims are not documented as retained, so the rejection is also unrecoverable.
- gap/limit: `MG-1`, `MG-2`. Prevents any statement of the acceptance criterion, and therefore prevents calling a surviving claim "accepted knowledge".

**`RTE-E6/synth` — cited synthesis (linked row)**
- route function: `content transformation`
- architectural status: `doctrine only`
- object/candidate id: `OBJ-6` produced from surviving `OBJ-9`
- content/update relation: **`indeterminate`** — classifications still possible: `non-ampliative reshaping` (ordering, grouping, and formatting surviving claims) or `ampliative conjecture` (synthesis prose asserting propositions no surviving claim asserts). "Synthesizes a cited report" does not decide between them. Evidence needed: the script text or an observed report artifact with claim-level attribution coverage (`MG-1`, `MG-2`).
- transition or check target: none
- evaluator/condition and domain: none — **no check is documented on the synthesized text itself**; the checks upstream apply to claims, not to the synthesis that assembles them
- activation and timing: final phase of the run
- possible or observed result: one cited report; **no instance observed**
- implemented force: none demonstrable at this tier
- epistemic authority and scope: **none produced by this route.** Any warrant `OBJ-6` carries is inherited from `RTE-E5` survivors, and the inheritance is unverified because synthesis-introduced content is unchecked.
- operational authority: produces the run's sole deliverable
- behavioral-authority path: consumer `CMP-12` + human | channel `RTE-X3` | force advisory (`BAP-4`) | horizon session / turn
- evidence: `SRC-1#bundled`, `#run-a-bundled-workflow`
- claim IDs: `CLM-2`
- mismatch marker: **yes** — the report is presented as carrying the filter's quality property, while the step that composes it is itself unchecked.
- gap/limit: `MG-1`, `MG-2`. Prevents concluding that the report contains only surviving claims.

**`RTE-E6/lineage` — per-claim citation binding (linked row)**
- route function: `lineage/freshness/recovery`
- architectural status: `doctrine only`
- object/candidate id: citation pairs binding `OBJ-9` to `OBJ-10` (see PROPOSED NEW RECORD 2)
- content/update relation: `no content change` — provenance attached alongside content
- transition or check target: none
- evaluator/condition and domain: none — attribution is asserted, not verified; no citation-accuracy check documented
- activation and timing: at synthesis
- possible or observed result: a report that "cites the sources each claim came from"; **no instance observed**
- implemented force: none demonstrable at this tier
- epistemic authority and scope: **this is the subsystem's most consequential epistemic feature and it is reader-side, not system-side.** Preserved lineage lets a human re-derive or contest a claim; it issues no system warrant, and it is not itself checked.
- operational authority: none — citations do not gate anything downstream
- behavioral-authority path: consumer human reader | channel `OBJ-6` text | force **advisory** | horizon session / turn (no documented persistence)
- evidence: `SRC-1#run-a-bundled-workflow` ("It cites the sources each claim came from")
- claim IDs: `CLM-2`; see PROPOSED NEW RECORD 3
- mismatch marker: none
- gap/limit: `MG-2`, `MG-6`. Prevents concluding that citation coverage is complete or that attributions are correct.

**`RTE-E7` — adversarial peer review (generic pattern)**
- route function: `check/evidence production`
- architectural status: **`doctrine only`, and weaker than the deep-research rows** — `SRC-1#when-to-use` states this as something a workflow "**can**" be written to do. It is a capability of the pattern; **no shipped workflow is documented as doing it.** The packet's anti-conflation check "capability is not deployment" applies directly.
- object/candidate id: unnamed findings (a generic `OBJ-4`-class object); no shipped instance
- content/update relation: `no content change` documented; would produce review results
- transition or check target: another agent's findings, "before they're reported"
- evaluator/condition and domain: independent model agents in an adversarial posture; independence is asserted by role assignment, and no mechanism for it is documented
- activation and timing: only if a script author writes it; **not active in any documented shipped workflow**
- possible or observed result: none documented; **no instance observed**
- implemented force: **none** — a capability statement has no consumer
- epistemic authority and scope: **none.** A capability that no named artifact exercises licenses nothing.
- operational authority: none
- behavioral-authority path: none recorded
- evidence: `SRC-1#when-to-use`
- claim IDs: **`CLM-1`** — this is one of the two routes `CLM-1`'s warrant rests on
- mismatch marker: **yes, and it is the central mismatch of this lens** — the subsystem's strongest warrant claim is attached to a route with no named shipped instance.
- gap/limit: `MG-1`, `MG-2`, `MG-9`. Prevents any conclusion that adversarial review happens in this subsystem at all.

**`RTE-E8` — multi-angle drafting and weighing (generic pattern)**
- route function: `check/evidence production`
- architectural status: `doctrine only` — same capability status as `RTE-E7`
- object/candidate id: candidate plans (unnamed; no shipped instance)
- content/update relation: `no content change` documented; the weighing would produce comparative results
- transition or check target: several independently drafted plans, weighed "against each other"
- evaluator/condition and domain: model agents; no rubric, no criterion, no weighting rule documented
- activation and timing: only if a script author writes it
- possible or observed result: none documented; **no instance observed**
- implemented force: **none**
- epistemic authority and scope: **none**
- operational authority: none
- behavioral-authority path: none recorded
- evidence: `SRC-1#when-to-use`
- claim IDs: **`CLM-1`**
- mismatch marker: **yes** — same as `RTE-E7`
- gap/limit: `MG-1`, `MG-2`, `MG-9`.

### 3.2 Context, retention, and recovery routes for truth-apt material

**`RTE-X1` — script → sub-agent prompt**
- route function: `operational admission/selection/consumption`
- architectural status: `doctrine only`
- object/candidate id: content selected from `OBJ-3`/`OBJ-2` into a prompt consumed by `CMP-4`
- content/update relation: **`indeterminate`** — classifications still possible: `non-ampliative reshaping` (templated concatenation of prior results) or `ampliative conjecture` (a composed framing asserting more than its inputs). The selection signal is script-authored code, not model judgement at dispatch — which makes reshaping the more likely class but does not establish it without the script text (`MG-1`).
- transition or check target: none — **no check is documented between an agent's result and its reuse in another agent's prompt**
- evaluator/condition and domain: none in the general case; only `CMP-11` documents downstream checking
- activation and timing: at each dispatch, per `RTE-C4`
- possible or observed result: a composed prompt; **no instance observed** (though `RTE-X6` makes prompts inspectable in principle)
- implemented force: none demonstrable at this tier
- epistemic authority and scope: **none** — selection into context is not endorsement; unchecked `OBJ-4` content can seed a later agent's premises
- operational authority: determines what each worker works from
- behavioral-authority path: consumer sub-agent `CMP-4` | channel spawn prompt | force **directive** (`BAP-3`) | horizon that agent's lifetime
- evidence: `SRC-1#when-to-use`, `#watch-the-run`
- claim IDs: `CLM-3`, `CLM-7`
- mismatch marker: none
- gap/limit: `MG-1`, `MG-4`. Prevents any conclusion about warrant propagation between workflow stages.

**`RTE-X2` — sub-agent result → script variables**
- route function: `retention` (pre-acceptance; explicitly **not** lifecycle integration)
- architectural status: `doctrine only`
- object/candidate id: `OBJ-4` into `OBJ-3`
- content/update relation: `no content change`
- transition or check target: none
- evaluator/condition and domain: none documented — results are retained unchecked
- activation and timing: on each agent completion
- possible or observed result: values in `OBJ-3`; **no instance observed**
- implemented force: none demonstrable at this tier
- epistemic authority and scope: **none** — retention is not acceptance
- operational authority: makes results available to later stages
- behavioral-authority path: consumer `OBJ-1` | channel script variables | force enforcing on control flow (`BAP-1`) | horizon one run
- evidence: `SRC-1#when-to-use`, `#how-it-runs`
- claim IDs: `CLM-3`
- mismatch marker: none
- gap/limit: `MG-7`.

**`RTE-S5` — agent-result tracking**
- route function: `retention`
- architectural status: `doctrine only`
- object/candidate id: `OBJ-4` in `CMP-9`
- content/update relation: `no content change`
- transition or check target: none
- evaluator/condition and domain: none
- activation and timing: continuously as the run progresses
- possible or observed result: a per-agent result store; **no instance observed**
- implemented force: none demonstrable at this tier
- epistemic authority and scope: **none** — this is the packet's "retaining material is not selecting it into context" line, and it holds: most `OBJ-4` content documentedly never reaches `CMP-12`
- operational authority: enables `RTE-C6` resume and `RTE-X6` inspection
- behavioral-authority path: consumer `CMP-1` scheduler and `CMP-6` UI | channel runtime store | force enforcing on resume behavior | horizon session-scoped
- evidence: `SRC-1#how-it-runs`
- claim IDs: **`CLM-4`**
- mismatch marker: none
- gap/limit: `MG-1`, `MG-2`. Store contents and eviction are uninspected.

**`RTE-C6` — resume (cached-result replay)**
- route function: `lineage/freshness/recovery`
- architectural status: `doctrine only`
- object/candidate id: cached `OBJ-4`
- content/update relation: `no content change` — a completed agent's earlier result is reused rather than recomputed
- transition or check target: none — **no freshness or revalidation check is documented on a replayed result**
- evaluator/condition and domain: none
- activation and timing: on resume, within the same session only; exiting Claude Code starts the workflow fresh
- possible or observed result: cached results returned, remainder run live; **no instance observed**
- implemented force: none demonstrable at this tier
- epistemic authority and scope: **none, and this is a freshness limit worth naming** — a replayed result is reused without re-evidence, so a resumed run mixes results produced at different times against a possibly changed world. Applicability is not endorsement.
- operational authority: permits a partially completed run to finish without redoing work
- behavioral-authority path: consumer `CMP-1` | channel `CMP-9` | force enforcing on what reruns | horizon same session only
- evidence: `SRC-1#resume`, `#how-it-runs`
- claim IDs: `CLM-4`
- mismatch marker: none
- gap/limit: `MG-2`, `MG-8`.

**`RTE-X3` — final answer → main session**
- route function: `operational admission/selection/consumption`
- architectural status: `doctrine only`
- object/candidate id: `OBJ-6`
- content/update relation: `no content change`
- transition or check target: none — **no check is documented on the report at delivery**
- evaluator/condition and domain: none in the system; the human reader is an evaluator only informally, with no recorded result
- activation and timing: at run completion
- possible or observed result: report in `CMP-12`'s context; **no instance observed**
- implemented force: none demonstrable at this tier
- epistemic authority and scope: **none issued** — arrival in a context window is not acceptance and not endorsement
- operational authority: the report becomes available to influence the conversation
- behavioral-authority path: consumer main-session Claude + user | channel context delivery | force **advisory** (`BAP-4`) | horizon session / turn
- evidence: `SRC-1#when-to-use`, `#run-a-bundled-workflow`
- claim IDs: `CLM-3`
- mismatch marker: none
- gap/limit: `MG-6`. Prevents any retention or integration conclusion about the report.

**`RTE-X6` — run internals → human**
- route function: `other — evidence surfacing without a recorded evaluation`
- architectural status: `doctrine only`
- object/candidate id: `OBJ-4`, `OBJ-5`
- content/update relation: `no content change`
- transition or check target: none — this route **makes evidence available**; it does not evaluate
- evaluator/condition and domain: the human, informally; no criterion, no recorded verdict, no artifact
- activation and timing: any time during or after a run, via `/workflows` drill-down
- possible or observed result: the human reads a prompt, recent tool calls, and a result; **no instance observed**
- implemented force: **none by itself** — a surfaced result with no recorded consumer has no implemented force; force appears only when the human acts through `RTE-C5`
- epistemic authority and scope: none issued by the system
- operational authority: none directly
- behavioral-authority path: consumer human | channel `CMP-6` TUI / Desktop pane | force advisory | horizon the human's attention span during the run
- evidence: `SRC-1#watch-the-run`
- claim IDs: none
- mismatch marker: none
- gap/limit: The run does **not** wait for the human (`SRC-1#limits`, "No mid-run user input"), so this surface is asynchronous by construction and cannot gate anything.

### 3.3 Artifact retention, installation, and admission (non-truth-apt objects with epistemic consequence)

**`RTE-S1` — run-script archive write**
- route function: `retention`
- architectural status: `doctrine only`
- object/candidate id: `OBJ-1`
- content/update relation: `non-truth-apt policy/content update: the run's orchestration procedure is written to disk under the session directory`
- transition or check target: none
- evaluator/condition and domain: none
- activation and timing: **every run**, at start
- possible or observed result: a readable, diffable script file; **no instance observed**
- implemented force: none until relaunched
- epistemic authority and scope: none — but note the asymmetry it creates: **the orchestration is archived every run while the report is not documented as persisted at all** (`MG-6`)
- operational authority: enables reading, diffing, editing, and relaunching
- behavioral-authority path: consumer Claude/user on request | channel path delivered by `RTE-X4` | force **material for relaunch** — advisory until relaunched, then `BAP-1` (`BAP-9`) | horizon persists on disk under the session directory
- evidence: `SRC-1#how-it-runs`
- claim IDs: `CLM-7`
- mismatch marker: none
- gap/limit: `MG-2`.

**`RTE-S2` — save run script as command**
- route function: `retention`, linked to `operational admission/selection/consumption` for future `/<name>` invocation. **This is deliberately not recorded as lifecycle integration**: no truth-apt claim was accepted beforehand, so the procedure's post-acceptance condition is not met.
- architectural status: `doctrine only`
- object/candidate id: `OBJ-7` (from a specific `OBJ-1`)
- content/update relation: `non-truth-apt policy/content update: a one-off orchestration becomes an installed, repo-shareable command`
- transition or check target: the orchestration procedure, not any proposition
- evaluator/condition and domain: **the human**, on the stated criterion "if the run does what you wanted" (`SRC-1#ask-in-prompt`) — a satisfaction judgement with no recorded artifact, no rubric, and no scope statement
- activation and timing: human presses `s` in `/workflows`, after a run; save dialog chooses project or personal location
- possible or observed result: `/name` available in future sessions; project entry beats personal on collision; **no instance observed**
- implemented force: none demonstrable at this tier
- epistemic authority and scope: **none over any truth-apt content.** This is the subsystem's only human evaluation that durably changes future behavior, and its target is the *procedure*, not any claim the procedure produced. Success of the bundle does not license any conclusion about an individual component of it.
- operational authority: permits future sessions to run that orchestration by name
- behavioral-authority path: consumer future sessions' command resolver + Claude/user | channel `CMP-7` registry lookup | force **enforcing on invocation** (`BAP-2`) | horizon persistent across sessions; project-scoped (repo-shared) or user-scoped
- evidence: `SRC-1#save`, `#ask-in-prompt`
- claim IDs: `CLM-7`
- mismatch marker: **yes, worth flagging** — `CLM-7` says what is repeatable is "the orchestration itself"; the ledger confirms that and shows the corollary the doc does not state: **nothing the orchestration concluded is made repeatable, retained, or accepted.**
- gap/limit: `MG-2`, `MG-6`.

**`RTE-C2` — launch approval**
- route function: `operational admission/selection/consumption`
- architectural status: `doctrine only` (its permission table is doctrine about implemented behavior)
- object/candidate id: `OBJ-1`
- content/update relation: `no content change`
- transition or check target: admission of a script to execution; **not** a check on any proposition
- evaluator/condition and domain: **the human**, on an unstated criterion, deciding from a **summary** (the planned phases) with full script text available only on opt-in (View raw script, `Ctrl+G`); on Desktop, name + phase list + token caution. Table-driven configuration selects between human decision and automatic start.
- activation and timing: pre-execution, per run; Default/accept-edits → every run unless "don't ask again"; Auto → first launch only, and skipped entirely when ultracode is on; Bypass permissions / `claude -p` / Agent SDK → never
- possible or observed result: run / cancel / adjust prompt via `Tab`; **no instance observed**
- implemented force: within doctrine, enforcing on whether the run starts
- epistemic authority and scope: **none** — approving an orchestration says nothing about the truth of what it will produce
- operational authority: permits or blocks the entire run, including all agent file edits downstream
- behavioral-authority path: consumer `CMP-5` gate | channel `OBJ-8` consent record | force **permissive** — suppresses the prompt (`BAP-5`) | horizon persistent per workflow+project (default/acceptEdits) or per user (Auto)
- evidence: `SRC-1#approve`
- claim IDs: `CLM-8`
- mismatch marker: none
- gap/limit: This is the run's **only** pre-execution human control point, it decides on a summary by default, and it is removable by mode or by one persistent consent record.

**`RTE-S4` — agent-mediated external action**
- route function: `operational admission/selection/consumption` (action execution admitted by inherited authorization)
- architectural status: `doctrine only`
- object/candidate id: none truth-apt; the filesystem/shell is the target
- content/update relation: `no content change` to any truth-apt object; the external world changes
- transition or check target: none — **no check on `OBJ-4` or any claim precedes an action**
- evaluator/condition and domain: the allowlist `OBJ-12` (configuration, not evaluation) plus forced `acceptEdits`
- activation and timing: mid-run, whenever an agent acts; non-allowlisted shell/web/MCP calls can still prompt
- possible or observed result: files written, commands run; **no instance observed**
- implemented force: within doctrine, enforcing
- epistemic authority and scope: **none** — and this is the sharpest asymmetry in the subsystem: **action is unconditional and mid-run, while checking exists only inside one bundled research workflow and applies only to report content.**
- operational authority: permits file edits regardless of session mode; the script itself has no filesystem or shell access (`CLM-6`)
- behavioral-authority path: consumer sub-agent tool executor | channel inherited `OBJ-12` + forced `acceptEdits` | force **permissive/enforcing** (`BAP-6`) | horizon the run
- evidence: `SRC-1#limits`, `#approve`
- claim IDs: `CLM-6`, `CLM-8`
- mismatch marker: none
- gap/limit: `MG-4`. Prevents any conclusion about agent-internal restraint before acting.

### 3.4 Direct behavior/policy adaptation with no truth-apt object (run's direct-adaptation exception)

These do not by themselves trigger this lens; they are recorded because they are material to
authority and would otherwise leave the authority picture incomplete.

**`RTE-S3` — consent record write**
- route function: `behavior/policy adaptation`
- architectural status: `doctrine only`
- object/candidate id: `OBJ-8`
- content/update relation: `non-truth-apt policy/content update: a human's one-time approval becomes a standing suppression of the launch prompt`
- transition or check target: the gate's future activation
- evaluator/condition and domain: the human, at one launch, on an unstated criterion
- activation and timing: on "Yes, and don't ask again for `<name>` in `<path>`"; under Auto, **any** Yes records consent in user settings
- possible or observed result: later launches start without prompting; **no instance observed**
- implemented force: within doctrine, enforcing on gate behavior
- epistemic authority and scope: **none** — one approval is not a warrant for future runs, and the doc records no re-evaluation trigger even if the saved script is later edited
- operational authority: removes the only pre-execution human control point for that workflow
- behavioral-authority path: consumer `CMP-5` | channel project/user settings | force **permissive** (`BAP-5`) | horizon persistent, per workflow+project or per user
- evidence: `SRC-1#approve`
- claim IDs: `CLM-8`
- mismatch marker: none
- gap/limit: `MG-2`. Prevents knowing whether an edited script re-triggers the prompt.

**`RTE-C1` — trigger → script authoring**
- route function: `behavior/policy adaptation`
- architectural status: `doctrine only`
- object/candidate id: `OBJ-13`
- content/update relation: `non-truth-apt policy/content update: a session setting changes Claude's default planning behavior`
- transition or check target: the planning path for every substantive task
- evaluator/condition and domain: model judgement, keyword- or setting-gated; under `/effort ultracode` the model decides per task, and one request can become several workflows in a row
- activation and timing: per prompt (keyword / natural language) or per session (`/effort ultracode`); resets on new session; disableable in `/config`
- possible or observed result: a workflow is planned instead of turn-by-turn work; **no instance observed**
- implemented force: within doctrine, directive
- epistemic authority and scope: **none**
- operational authority: changes which execution path a task takes, and under Auto+ultracode it also suppresses the launch prompt entirely — two authority reductions composing
- behavioral-authority path: consumer main-session Claude's planning (`CMP-3`) | channel `OBJ-13` session setting | force **directive default** (`BAP-8`) | horizon current session; resets on new session
- evidence: `SRC-1#ultracode`, `#ask-in-prompt`, `#approve`
- claim IDs: none
- mismatch marker: none
- gap/limit: `MG-2`. What the authoring model reads is uninspected.

**`RTE-C5` — interactive mid-run control**
- route function: `behavior/policy adaptation`
- architectural status: `doctrine only`
- object/candidate id: none truth-apt; the target is the run or an agent
- content/update relation: `non-truth-apt policy/content update: a human judgement from telemetry stops, restarts, or pauses execution`
- transition or check target: the run's continuation
- evaluator/condition and domain: the human, from `RTE-X6` telemetry; **no criterion, no recorded result, no artifact**
- activation and timing: any time during a run; asynchronous — the run does not wait
- possible or observed result: pause/resume, stop agent, stop run, restart agent, save script; **no instance observed**
- implemented force: within doctrine, enforcing on execution
- epistemic authority and scope: **none** — stopping or letting a run continue is not a verdict on its content. Operational continuation must not be read as epistemic warrant.
- operational authority: halts or resumes work; stopping preserves completed work
- behavioral-authority path: consumer `CMP-1` | channel `CMP-6` keypress | force enforcing | horizon the current run
- evidence: `SRC-1#watch-the-run`, `#limits`
- claim IDs: none
- mismatch marker: none
- gap/limit: Staged human sign-off is impossible within one workflow; it requires splitting into separate workflows (`SRC-1#limits`).

### 3.5 Evidenced absences within the boundary

- **No route found within boundary: acceptance of `OBJ-6`.** No documented evaluator, criterion, intended use, or scope attaches to the delivered report. Searched: `#run-a-bundled-workflow`, `#when-to-use`, `#how-it-runs`, `#save`, `#bundled`. This absence is scoped to documented routes; it does not assert that no informal user-side acceptance occurs.
- **No route found within boundary: retention or export of `OBJ-6`.** Only `OBJ-1`/`OBJ-7` are documented as persisted. Searched: `#how-it-runs`, `#save`, `#resume`.
- **No route found within boundary: checking of `OBJ-4` in the general (non-`/deep-research`) case.** Searched: `#when-to-use`, `#how-it-runs`, `#limits`, `#watch-the-run`.
- **No route found within boundary: retention of rejected `OBJ-9` claims or of `OBJ-11` vote results.** Filtered claims are described only as removed from the report. Searched: `#bundled`, `#run-a-bundled-workflow`.
- **No route found within boundary: any comparison of a workflow's output against a single-pass baseline.** Searched: whole file. This is the absence that blocks `CLM-1`.

---

## 4. Per-object lifecycle disposition

Architectural status and observed candidate state are recorded separately throughout.
Because the tier is `doc-grounded` with no observed run of the target (`MG-2`), **every
observed candidate state below is `no instance observed`** — doctrine alone cannot establish
one, and `SRC-2` is roster-only and negative.

### `OBJ-9` — deep-research claim (primary candidate)

- **candidate object ID:** `OBJ-9`
- **relevant route IDs:** `RTE-E1`, `RTE-E2`, `RTE-E3/extract`, `RTE-E3/check`, `RTE-E4`, `RTE-E5`, `RTE-E6/synth`, `RTE-E6/lineage`, `RTE-X3`
- **transformation:** **`indeterminate`, not established as ampliative.** The discovery-lifecycle schema is therefore applied provisionally and flagged: `MG-5` prevents deciding between faithful extraction (`non-ampliative reshaping`) and model-composed proposition (`ampliative conjecture`). Classifications still possible: both. Evidence needed to decide: the `/deep-research` script text or an observed run artifact showing per-claim provenance.
- **observation/anomaly:** routes `RTE-E1`, `RTE-E2` | architectural status `doctrine only` | observed candidate state **`no instance observed`** | evidence `SRC-1#bundled` (doctrine/design). The "observation" here is web retrieval, i.e. acquisition of others' assertions, not observation of a phenomenon by this system.
- **conjecture:** route `RTE-E3/extract` | architectural status **`no route found within boundary`** — the step is presupposed by `CLM-2` but never declared | observed candidate state **`no instance observed`** | evidence `SRC-1#bundled` (presupposition only).
- **derived consequence:** **no route found within boundary.** `SRC-1` documents no step in which a claim's testable consequences are derived before checking; cross-checking compares the claim to retrieved text directly. Architectural status `no route found within boundary` | observed candidate state `no instance observed`.
- **test/evidence:** routes `RTE-E3/check`, `RTE-E4` | architectural status `doctrine only` | observed candidate state **`no instance observed`** | evidence `SRC-1#bundled`, `#run-a-bundled-workflow` (doctrine/design). **Test domain is agreement among retrieved sources, not truth**; the evaluator is a multi-agent vote whose rule is undocumented (`MG-1`).
- **acceptance:** route `RTE-E5` | evaluator: the vote result `OBJ-11`, consumed by the filter | criterion: **stated only by outcome** ("didn't survive cross-checking"); no rule, threshold, or rubric documented | intended use: **none stated** | architectural status `doctrine only` | observed candidate state **`no instance observed`** | accepted scope: **none stated by the system**; the most the route could license is "not contradicted by the sources this run retrieved, as of the run" | evidence `SRC-1#bundled`. **Finding: this is admission by non-rejection, not a recorded evidence-consuming acceptance decision naming criterion, intended use, and scope. No acceptance transition in the procedure's sense is documented anywhere in this subsystem.**
- **lifecycle integration:** routes `RTE-E6/synth`, `RTE-X3` | post-acceptance change/consumer: the claim appears in `OBJ-6`, which lands in `CMP-12`'s context with advisory force (`BAP-4`) and no documented persistence | architectural status `doctrine only` | observed candidate state **`no instance observed`**; **and independently `not reached` as a matter of doctrine** — appearing in a report and being read is *use*, not integration: nothing is connected to evidence for later reliance, nothing changes the system's organization, and no store is updated | evidence `SRC-1#run-a-bundled-workflow`, `#how-it-runs`, and the evidenced absence in §3.5.
- **missing phase/evidence:** `MG-1`, `MG-2`, `MG-5`. Missing phases: consequence derivation (no route), acceptance-with-named-scope (route present but criterion and scope absent), integration (no route). The prevented conclusions: that `/deep-research` produces accepted knowledge; that surviving claims carry any system-issued warrant; that any claim was in fact checked in any run.

### `OBJ-6` — final report / answer

- **candidate object ID:** `OBJ-6`
- **relevant route IDs:** `RTE-E6/synth`, `RTE-E6/lineage`, `RTE-X3`
- **transformation:** **`indeterminate`** — `non-ampliative reshaping` of surviving `OBJ-9` claims, or `ampliative conjecture` where synthesis prose asserts more than the claims do. Classifications still possible: both.
- **preserved lineage:** per-claim citations to `OBJ-10` (`RTE-E6/lineage`) — asserted, unverified, with no documented coverage guarantee.
- **implemented checks, retention, or use:** **no check** at or after synthesis (§3.5); **no documented retention** (`MG-6`); use is advisory delivery into `CMP-12` (`RTE-X3`, `BAP-4`, horizon session/turn).
- **current warrant limit:** whatever warrant survives from `RTE-E5`, degraded by an unchecked composition step. The system issues no warrant of its own for the report.
- **evidence needed to decide preservation, entailment, or ampliation:** an observed report artifact with per-claim attribution, plus the script text (`MG-1`, `MG-2`).
- **observed candidate state across all phases:** `no instance observed`.

### `OBJ-4` — agent result

- **candidate object ID:** `OBJ-4`
- **relevant route IDs:** `RTE-X1` (as later input), `RTE-X2`, `RTE-S5`, `RTE-C6`, `RTE-X6`
- **transformation:** **`indeterminate`, ampliation not established** — an agent's natural-language findings may report what it read (acquisition/reshaping) or assert conclusions beyond it (ampliative conjecture); the producing loop is outside the bundle (`MG-4`).
- **discovery lifecycle:** **not applicable as established** — ampliation is not established, so the lifecycle schema is not forced onto it. Recorded instead as an indeterminate object.
- **preserved lineage:** the agent's prompt and recent tool calls are retained alongside the result and are inspectable via `RTE-X6` — a genuine lineage strength at the doctrine layer.
- **implemented checks, retention, or use:** **no check documented in the general case**; retained by `RTE-X2` and `RTE-S5`; replayed unrevalidated by `RTE-C6`; reused as another agent's premise via `RTE-X1`; surfaced to the human by `RTE-X6` with no recorded verdict.
- **current warrant limit:** none established. Retention, replay, and reuse as premises all occur **before and without** any check.
- **evidence needed:** the sub-agent primitive's documentation and an observed run (`MG-4`, `MG-2`).
- **observed candidate state:** `no instance observed`.

### `OBJ-11` — cross-check / vote result

- **candidate object ID:** `OBJ-11`
- **relevant route IDs:** `RTE-E3/check`, `RTE-E4`, `RTE-E5`
- **transformation:** **`indeterminate`** — an aggregated evaluative judgement about `OBJ-9`. Classifications still possible: `entailed derivation` if the vote is a deterministic function of recorded per-source comparisons; `ampliative conjecture` if the models judge holistically. Undecidable without the script text (`MG-1`).
- **preserved lineage:** none documented — the result is not documented as retained or surfaced to the reader.
- **implemented checks, retention, or use:** unchecked; consumed once by `RTE-E5`; not documented as retained.
- **current warrant limit:** licenses only inter-source agreement as judged by model evaluators of unknown independence, at the moment of the run.
- **evidence needed:** the vote rule and an observed run (`MG-1`, `MG-2`).
- **observed candidate state:** `no instance observed`.

### `OBJ-10` — fetched web source

- **candidate object ID:** `OBJ-10`
- **relevant route IDs:** `RTE-E1`, `RTE-E2`, `RTE-E3/check`, `RTE-E6/lineage`
- **transformation:** `truth-apt transformation: acquisition/import`
- **discovery lifecycle:** **not applicable** — imported content is acquired, not produced by this system.
- **applicable acquisition, lineage, derivation, or update route and warrant:** acquired by `RTE-E1`→`RTE-E2` with **source warrant unknown** — no authority, recency, independence, or quality criterion is documented. Lineage is preserved forward into `OBJ-6` by `RTE-E6/lineage`.
- **missing evidence/limit:** `MG-1`, `MG-2`. Prevents any conclusion that fetched sources are mutually independent — the property `RTE-E3/check`'s value depends on.

### `OBJ-5` — phase record (telemetry)

- **candidate object ID:** `OBJ-5`
- **relevant route IDs:** `RTE-X6`, `RTE-S6`
- **transformation:** `truth-apt transformation: acquisition/import` (instrumented measurement of the run)
- **discovery lifecycle:** **not applicable** — non-ampliative measurement.
- **applicable acquisition, lineage, derivation, or update route and warrant:** produced by `CMP-1` instrumentation, surfaced to the human; warrant rests on uninspected instrumentation, and no reconciliation against billing is available (that surface is boundary-excluded).
- **missing evidence/limit:** `MG-1`. Prevents any accuracy claim about token totals or timings.

### Per-object no-candidate lines

- No lifecycle record for `OBJ-1`: no candidate truth-apt output for this object; relevant direct-adaptation or update routes: `RTE-S1`, `RTE-S2`, `RTE-C2`, `RTE-C3`.
- No lifecycle record for `OBJ-2`: no candidate truth-apt output for this object; relevant direct-adaptation or update routes: `RTE-X5`, `RTE-C7`.
- No lifecycle record for `OBJ-3`: heterogeneous container with no candidate truth-apt output of its own; its truth-apt content is dispositioned under `OBJ-4`, `OBJ-9`, and `OBJ-11`; relevant routes: `RTE-X1`, `RTE-X2`.
- No lifecycle record for `OBJ-7`: no candidate truth-apt output for this object; relevant direct-adaptation or update routes: `RTE-S2`, `RTE-C7`.
- No lifecycle record for `OBJ-8`: no candidate truth-apt output for this object; relevant direct-adaptation or update routes: `RTE-S3`, `RTE-C2`.
- No lifecycle record for `OBJ-12`: no candidate truth-apt output for this object; relevant direct-adaptation or update routes: `RTE-S4`.
- No lifecycle record for `OBJ-13`: no candidate truth-apt output for this object; relevant direct-adaptation or update routes: `RTE-C1`, `RTE-C8`.
- No lifecycle record for `OBJ-14`: no candidate truth-apt output for this object; relevant direct-adaptation or update routes: `RTE-C4` (per-stage model routing).

The global no-candidate statement does **not** apply: the inventory contains candidate
truth-apt output (`OBJ-4`, `OBJ-6`, `OBJ-9`, `OBJ-10`, `OBJ-11`, `OBJ-5`).

---

## 5. System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor + evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch / unknown |
|---|---|---|---|---|---|---|---|---|
| `CLM-1` | Independent agents adversarially reviewing each other's findings, or drafting a plan from several angles and weighing them, gives "a more trustworthy result than a single pass". **Warrant claim.** | `SRC-1#when-to-use`; **doctrine/design** | Yes, but only as a **capability of the pattern** (`RTE-E7`, `RTE-E8`), phrased with "can"; no shipped workflow is named as doing either | **none** — nothing reaches `implemented` at this tier (`MG-1`) | **none** — no run observed; `SRC-2` is roster-only and negative (`MG-2`) | **none.** `SRC-1` contains no baseline, no metric of trustworthiness, no comparison, and no experiment (`MG-3`). No contrast exists, so no causal identification is even attemptable; component attribution among review, multi-angle drafting, and agent count is impossible. | **Only that Anthropic states this as a design rationale for the workflow pattern.** The comparative core — "more trustworthy than a single pass" — has no doctrine-internal argument, no implementation, no run, and no measurement behind it. Within this boundary it is not merely unsupported but **untested and unfalsifiable**. | **Mismatch, two layers.** (1) The warrant claim attaches to `RTE-E7`/`RTE-E8`, which have no named shipped instance; the one shipped instance (`CMP-11`) implements a *different* pattern (cross-check → vote → filter), so even doctrine does not connect `CLM-1`'s mechanism to shipped behavior. (2) "Trustworthy" is never operationalized; the nearest shipped evaluator domain (`RTE-E3/check`) reaches only inter-source agreement. |
| `CLM-2` | `/deep-research` "votes on each claim, and returns a cited report with claims that didn't survive cross-checking filtered out". **Knowledge-production / operation claim.** | `SRC-1#bundled`; **doctrine/design** | Yes — `RTE-E1`..`RTE-E6` are declared as the shipped behavior of a named bundled workflow, which is stronger doctrine than `CLM-1`'s capability phrasing | **none** (`MG-1`; the script text is boundary-excluded) | **none** (`MG-2`) | **none.** No comparison of filtered vs. unfiltered output; no accuracy measurement; nothing licenses attributing report quality to the filter rather than to retrieval, model, or question. | **That the vendor declares a shipped check-and-disposition pipeline with a named evaluator form (a multi-agent vote) and a named disposition (survival filtering), plus preserved per-claim citation lineage.** That is a real architectural commitment and is the strongest epistemic structure in the subsystem. It licenses **nothing** about: the vote rule (quorum, threshold, ties — all undocumented); whether filtering tracks truth rather than retrieved-source consensus; whether surviving claims are accepted for any named use or scope; whether the synthesis step introduces unchecked content; or whether any run behaved this way. | **Doctrine-internal gap:** the claim quantifies over "each claim" while no route producing claims from sources is documented (`RTE-E3/extract`, `MG-5`). **Scope unknown:** whether "cross-checking" is claim-vs-source or source-vs-source is not resolved by the text. |
| `CLM-3` | "A workflow script holds the loop, the branching, and the intermediate results itself, so Claude's context holds only the final answer." | `SRC-1#when-to-use`; doctrine/design | Yes; consistent with `RTE-X2`/`RTE-X3` and the packet's anti-conflation check | none | none | none | That the declared context economy is `OBJ-4` → `OBJ-3` (not `CMP-12`), with only `OBJ-6` delivered. **Epistemic corollary the doc does not state: the human's default view of the run's evidence is one synthesized report, and the underlying results are reachable only by opt-in drill-down (`RTE-X6`) that gates nothing.** | Unknown whether "only the final answer" is exact (the archive path also arrives via `RTE-X4`). |
| `CLM-4` | "The runtime tracks each agent's result as the run progresses, which is what makes a run resumable within the same session." | `SRC-1#how-it-runs`; doctrine/design | Yes — `RTE-S5` retention, `RTE-C6` recovery | none | none | none | That retention exists for recovery purposes and is session-bounded. **Retention is not acceptance**, and replayed results are reused without revalidation (`RTE-C6`). | Unknown whether cached results are revalidated on resume; nothing suggests they are. |
| `CLM-5` | The 1,000-agent cap "prevents runaway loops"; caps "bound the cost of a runaway script". | `SRC-1#limits`, `#cost`; doctrine/design | Yes — `BAP-10` enforcing ceiling | none | none | none | That a ceiling is declared. It bounds **count and spend**, not correctness; a bounded run can still be wrong. | Unknown how the cap interacts with `RTE-C6` resume accounting. |
| `CLM-6` | "No direct filesystem or shell access from the workflow itself" — agents act, the script coordinates. | `SRC-1#limits`; doctrine/design | Yes — `RTE-S4`, the architectural line that the orchestrator is a pure coordinator | none | none | none | That the *orchestrator* is declared non-acting. **This is an isolation property of the script, not a check on action**: agents act unconditionally in `acceptEdits`, and no documented check on `OBJ-4` precedes their actions. | None internal; the safety reading it invites (that action is constrained) is not what the claim says. |
| `CLM-7` | What is repeatable in a workflow is "the orchestration itself"; the plan moves into code. | `SRC-1#when-to-use`; doctrine/design | Yes — `RTE-S1`, `RTE-S2`, `BAP-2` | none | none | none | That the **procedure** is the retained, shareable, repeatable unit. **The corollary this lens adds: nothing the procedure concluded is retained, accepted, or made repeatable.** The subsystem codifies method, not findings. | None internal; a real asymmetry against `MG-6`. |
| `CLM-8` | "Your permission mode controls only the launch prompt" — spawned sub-agents always run in `acceptEdits` and inherit the allowlist regardless of session mode. | `SRC-1#approve`; doctrine/design | Yes — `BAP-6`, `RTE-S4`, `RTE-C2` | none | none | none | That authority is decided **once, pre-execution, on a phase summary**, and that the session's own mode does not constrain agents thereafter. | None internal. Bounds every authority conclusion in §6. |

No further consequential public or design claim was found in `SRC-1` beyond `CLM-1`..`CLM-8`
and the two proposed additions in the returns section.

---

## 6. Bounded conclusion

Scoped to the dynamic-workflows subsystem at the 2026-06-03 documentation boundary, on
`doc-grounded` evidence (`SRC-1` = doctrine/design; `SRC-2` = negative, roster-only). **No
whole-system conclusion about Claude Code, and no system-wide epistemic grade, is given or
available.** Every finding below is a finding about a route, at the doctrine layer.

**What it retains, retrieves, reshapes, or uses.** The subsystem retains two things
durably: the orchestration script, archived every run (`RTE-S1`) and optionally installed as
a repo-shareable command (`RTE-S2`, `BAP-2`); and per-agent results, retained
session-scoped for recovery (`RTE-S5`, `RTE-C6`). It retains **no findings** — `OBJ-6` has
no documented persistence, export, or downstream consumer (`MG-6`, §3.5). Retained agent
results are reused as later agents' premises (`RTE-X1`) and replayed on resume without
revalidation (`RTE-C6`), in both cases **before and without any check**. Retention here is
not acceptance and not integration.

**What it acquires, and whether source warrant is preserved.** `RTE-E1`→`RTE-E2` import
external web content (`OBJ-10`) with **source warrant unknown**: no authority, recency,
independence, or quality criterion is documented. Provenance is preserved forward as
per-claim citations in the report (`RTE-E6/lineage`) — the single most consequential
epistemic feature in the subsystem, and it is **reader-side**: it lets a human re-derive or
contest a claim; it issues no system warrant and is itself unverified.

**What it derives.** Nothing is documented as an entailed derivation from warranted
premises within a declared formal domain. `OBJ-11` (the vote result) is the only plausible
candidate and is `indeterminate` without the vote rule (`MG-1`).

**What it conjectures, tests, accepts, and integrates.** Claims (`OBJ-9`) appear in the
pipeline without a documented step that produces them from sources — `RTE-E3/extract` is
presupposed by `CLM-2` and never declared (`MG-5`), which blocks classifying `OBJ-9` as
reshaped or conjectured and blocks tracing warrant from `OBJ-10` into it. Claims are then
tested (`RTE-E3/check`, `RTE-E4`) in a domain that is **agreement among the sources this run
retrieved, not truth**, by model evaluators whose independence is asserted by role rather
than mechanism. Disposition (`RTE-E5`) is **admission by non-rejection**: survival is named
by outcome, with no rule, no intended use, no reliance scope, and no persisted acceptance
artifact. **No acceptance transition in this procedure's sense — a recorded, evidence-
consuming decision against a named criterion for a named use and scope — is documented
anywhere in this subsystem.** Consequently **lifecycle integration is `not reached` as a
matter of doctrine and `no instance observed` as a matter of evidence**: a surviving claim's
terminus is a report delivered advisorily into a context window (`RTE-X3`, `BAP-4`, horizon
session/turn). Consequence derivation has no route at all. `/deep-research` is best
described as a **filtered acquisition-and-synthesis pipeline with preserved citation
lineage** — not a knowledge-production loop.

**Acceptance criteria, intended use, scope, and authority — the three kept separate.**
*Epistemic authority:* the only route issuing anything like a license is `RTE-E5`, and its
honest ceiling is "not contradicted by the sources this run retrieved, as judged by a model
vote of undocumented rule, at run time". Nothing else in the subsystem issues epistemic
authority; retention (`RTE-S5`), delivery (`RTE-X3`), surfacing (`RTE-X6`), and continuation
(`RTE-C5`) issue none.
*Operational authority:* decided **once, pre-execution, by a human reading a phase summary**
(`RTE-C2`), with full script text opt-in only; removable by permission mode, by a persistent
consent record (`RTE-S3`), or entirely under Auto+ultracode. Thereafter agents act in forced
`acceptEdits` with the inherited allowlist (`RTE-S4`, `CLM-8`), bounded only by the ≤16/≤1000
caps. **The asymmetry is the finding: action is unconditional and mid-run, while checking
exists only inside one bundled research workflow and applies only to report content, never to
the agent output that drives action.**
*Behavioral authority (consumer | channel | force | horizon):* enforcing and durable for the
*procedure* — `BAP-1` (script is control flow, one run), `BAP-2` (saved command, persistent,
repo-shared), `BAP-9` (archived script, relaunchable), `BAP-10` (caps, every run), `BAP-7`
(org-wide prohibition). Advisory and ephemeral for the *findings* — `BAP-4` (report into the
session, horizon session/turn). Permissive and durable for *authority reduction* — `BAP-5`
(consent record, persistent per workflow+project or per user), `BAP-6` (forced `acceptEdits`,
run), `BAP-8` (ultracode directive default, session). **Force and horizon both run in favour
of method over findings.**

**Direct behavior/policy adaptation without a truth-apt route.** Three routes change
behavior on human or model judgement with no truth-apt object and no recorded result:
`RTE-S3` (one approval becomes standing prompt suppression), `RTE-C1` (a session setting makes
workflow planning the default), and `RTE-C5` (mid-run stop/restart from telemetry). The
human evaluation with the largest durable footprint is `RTE-S2` — saving a script on the
stated criterion "if the run does what you wanted" — and its target is the **procedure**, not
any claim. Bundle satisfaction licenses nothing about any component of the orchestration.

**Claims that remain unsupported for want of implementation, run, or causal evidence.**
`CLM-1` is unsupported in its comparative core and, within this boundary, untested: no
baseline, no trustworthiness metric, no contrast, and no named shipped workflow implementing
`RTE-E7`/`RTE-E8` (`MG-1`, `MG-2`, `MG-3`, `MG-9`). It is licensed only as a stated design
rationale. `CLM-2` is supported as doctrine about a shipped pipeline and licenses the
existence of a declared check-and-disposition architecture with citation lineage; it licenses
nothing about the vote rule, about whether filtering tracks truth rather than retrieved
consensus, about acceptance scope, or about any run's behavior. `CLM-3`..`CLM-8` are
doctrine-consistent and bound the above; none is implementation- or run-supported. All
findings are pinned to v2.1.154–160-era documentation; `MG-8` prevents any statement about
current behavior.

---

## Returns to the orchestrator (step 7.4)

**Material objects by canonical ID.** Truth-apt candidates: `OBJ-9` (primary), `OBJ-6`,
`OBJ-4`, `OBJ-11`, `OBJ-10` (acquired), `OBJ-5` (measurement). Non-truth-apt but material to
authority: `OBJ-1`, `OBJ-7`, `OBJ-8`, `OBJ-12`, `OBJ-13`, `OBJ-14`, `OBJ-2`; `OBJ-3` is a
heterogeneous container dispositioned through its contents.

**Material routes by canonical ID, with transformation class and route function.**

| Route | Route function | Content/update relation |
|---|---|---|
| `RTE-E1` | content transformation | acquisition/import (warrant unknown) |
| `RTE-E2` | content transformation | acquisition/import (warrant unknown) |
| `RTE-E3/extract` | content transformation | **indeterminate** (reshaping vs. ampliative conjecture) |
| `RTE-E3/check` | check/evidence production | no content change |
| `RTE-E4` | check/evidence production | no content change |
| `RTE-E5` | disposition/acceptance | no content change |
| `RTE-E6/synth` | content transformation | **indeterminate** |
| `RTE-E6/lineage` | lineage/freshness/recovery | no content change |
| `RTE-E7` | check/evidence production | no content change (capability only) |
| `RTE-E8` | check/evidence production | no content change (capability only) |
| `RTE-X1` | operational admission/selection/consumption | **indeterminate** |
| `RTE-X2` | retention | no content change |
| `RTE-S5` | retention | no content change |
| `RTE-C6` | lineage/freshness/recovery | no content change |
| `RTE-X3` | operational admission/selection/consumption | no content change |
| `RTE-X6` | other — evidence surfacing, no recorded evaluation | no content change |
| `RTE-S1` | retention | non-truth-apt policy/content update |
| `RTE-S2` | retention + linked operational admission | non-truth-apt policy/content update |
| `RTE-C2` | operational admission/selection/consumption | no content change |
| `RTE-S4` | operational admission/selection/consumption | no content change |
| `RTE-S3` | behavior/policy adaptation | non-truth-apt policy/content update |
| `RTE-C1` | behavior/policy adaptation | non-truth-apt policy/content update |
| `RTE-C5` | behavior/policy adaptation | non-truth-apt policy/content update |

**Architectural status vs. observed candidate state.** All routes above are `doctrine only`
except `RTE-E3/extract` (`no route found within boundary`) and the four evidenced absences in
§3.5. **No route is `implemented` or above** (tier fixed). **Every observed candidate state
is `no instance observed`** (`MG-2`).

**Checking / acceptance / retention-integration, kept separate.** Checking: `RTE-E3/check`,
`RTE-E4` only, inside `CMP-11` only, in the domain of retrieved-source agreement. Acceptance:
`RTE-E5` only, and it is admission by non-rejection with no criterion, use, scope, or
artifact — **no acceptance transition in the procedure's sense exists in this subsystem**.
Retention: `RTE-X2`, `RTE-S5`, `RTE-S1`, `RTE-S2` — all pre-acceptance, none integration.
Lifecycle integration: **`not reached` by doctrine, `no instance observed` by evidence.**

**Three authorities, kept separate.** Epistemic: `RTE-E5` only, ceiling stated in §6.
Operational: `RTE-C2`, `RTE-S3`, `RTE-S4`, `BAP-10`, `BAP-7`. Behavioral (consumer | channel
| force | horizon): `BAP-1`..`BAP-10` as annotated per route in §3; force and horizon both
favour method over findings.

**Missing evidence paired with prevented conclusions:** `MG-1`..`MG-9` in output 1, cited
per route in output 3 and per phase in output 4.

**PROPOSED NEW RECORDS** (unminted; for the orchestrator to register or reject):

1. `PROPOSED NEW RECORD: route — claim individuation/extraction from fetched sources (OBJ-10 → OBJ-9). Presupposed by CLM-2's quantification over "each claim" and by cross-checking, but never declared as a step in SRC-1; its absence blocks classifying OBJ-9's transformation and blocks tracing source warrant into it. Provisionally annotated in this lens as the linked row RTE-E3/extract. — evidence anchor: SRC-1#bundled, SRC-1#run-a-bundled-workflow.`
2. `PROPOSED NEW RECORD: object — per-claim citation binding (the provenance pair linking an OBJ-9 claim to the OBJ-10 source it came from), carried in OBJ-6. Distinct from OBJ-9 (proposition) and OBJ-11 (disposition value) by form (provenance edge), producer (RTE-E6), and consumer (the human reader, not the script). It is the subsystem's only reader-side warrant-transfer mechanism. — evidence anchor: SRC-1#run-a-bundled-workflow ("It cites the sources each claim came from").`
3. `PROPOSED NEW RECORD: claim — lineage claim: the delivered report "cites the sources each claim came from". Distinct from CLM-2, which asserts the vote-and-filter operation; this asserts a provenance property of the delivered artifact and is the only claim in SRC-1 that bears on reader-side re-derivation. — evidence anchor: SRC-1#run-a-bundled-workflow.`
