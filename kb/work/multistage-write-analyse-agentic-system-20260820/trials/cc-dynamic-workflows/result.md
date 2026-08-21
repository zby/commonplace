# Analysis result — Claude Code dynamic workflows

**Run / result ID: `AAS-20260820-CCDW-01`**

Produced by the candidate instruction `analyse-agentic-system`. This file is the entry
point to the result; the eleven required logical records are distributed across the files
indexed below and are numbered here in the instruction's order.

## Logical-record index

| # | Required logical record | Where |
|---|---|---|
| 1 | Run / staging identity | this file §1; `evidence-packet.md` §1 |
| 2 | System boundary, revision, overall evidence tier | `evidence-packet.md` §2, §3, §4, §5 |
| 3 | Source register | `evidence-packet.md` §4 |
| 4 | Shared component / object / route / claim / authority records | `evidence-packet.md` §6, **extended by this file §8.1** |
| 5 | Runtime account | `evidence-packet.md` §7 |
| 6 | Both lens applicability records | `lens-dispositions.md` |
| 7 | Applicable lens outputs | `lens-memory-context.md`, `lens-epistemic.md` |
| 8 | Cross-lens reconciliation | this file §8 |
| 9 | Bounded synthesis | this file §9 |
| 10 | Limitations, each paired with the conclusion it prevents | this file §10 |
| 11 | Verification / blocker report | this file §11 |

Supporting artifact (not a logical record): `capture-live-session-tool-roster.md`, the
`SRC-2` capture. Trial apparatus (outside the result): `trial-notes.md`.

---

## §1. Run and staging identity

| Field | Value |
|---|---|
| Run / result ID | `AAS-20260820-CCDW-01` |
| System | Claude Code **dynamic workflows** — the Workflow orchestration facility inside the Claude Code harness |
| Staging identity | `kb/work/multistage-write-analyse-agentic-system-20260820/trials/cc-dynamic-workflows/` |
| Publication target | **none authorized** — result retained under the staging identity; publication blocker `PB-1` in §11 |
| Boundary | **subsystem-only** (`evidence-packet.md` §3) |
| Revision / capture | `SRC-1` captured **2026-06-03**; analysis cutoff **2026-06-03** |
| Overall evidence tier | **`doc-grounded`** |
| Run date | 2026-08-20 |

All IDs in this result resolve across all physical parts: `SRC-1`–`SRC-2`, `CMP-1`–`CMP-12`,
`OBJ-1`–`OBJ-16`, `RTE-*` (control `C1`–`C9`, context `X1`–`X6`, state `S1`–`S7`,
deep-research `E1`–`E9`), `BAP-1`–`BAP-10`, `CLM-1`–`CLM-10`, `ABS-1`–`ABS-6`, `MG-1`–`MG-9`,
`L-1`–`L-14`, `PB-1`.

---

## §8. Cross-lens reconciliation

### 8.1 Registration of proposed new records (step 7.4 / step 3 "one canonical ID")

Both lenses returned proposed records unminted, as required. The orchestrator registers
them here. **These are the only new canonical IDs in the run**; they extend the packet's
§6 tables and do not replace or rename anything.

| New ID | Kind | Record | Proposed by | Status | Evidence anchor |
|---|---|---|---|---|---|
| `RTE-S7` | state route (candidate) | Possible write-back from a mid-run tool-permission prompt (`RTE-C9`) into the user's tool allowlist `OBJ-12`. Registered explicitly as **`uninspected`** so that `OBJ-12`'s retained-state classification stays visibly provisional. | memory | `uninspected` | `SRC-1#approve`, `#limits` |
| `RTE-X5/structure` | linked row on `RTE-X5` | Main-session Claude's conversion of user-named input into the structured `args` value — a model-performed semantic transformation on the invocation path of **every** saved workflow, with no preservation check. | memory | `claimed`; transformation class **indeterminate** | `SRC-1#args` |
| `RTE-E9` | deep-research route | Claim individuation / extraction from fetched sources (`OBJ-10` → `OBJ-9`). Presupposed by `CLM-2`'s quantification over "each claim" and by cross-checking, **never declared** in `SRC-1`. Architectural status **`no route found within boundary`**. Supersedes the epistemic lens's provisional local label `RTE-E3/extract`, which is retained in `lens-epistemic.md` as a synonym. | epistemic | `no route found within boundary` | `SRC-1#bundled`, `#run-a-bundled-workflow` |
| `OBJ-15` | operative object | The `/` autocomplete command index derived over `CMP-7` plus bundled commands — the discovery surface for the saved-command read-back path, distinct from the registry files; maintenance semantics undocumented. | memory | `claimed` (existence); `uninspected` (maintenance) | `SRC-1#save`, `#bundled` |
| `OBJ-16` | operative object | **Per-claim citation binding** — the provenance pair linking an `OBJ-9` claim to the `OBJ-10` source it came from, carried inside `OBJ-6`. Split from `OBJ-9` (proposition) and `OBJ-11` (disposition value) by form (provenance edge), producer (`RTE-E6/lineage`), and consumer (**the human reader, not the script**). | epistemic | `claimed` | `SRC-1#run-a-bundled-workflow` |
| `CLM-9` | claim | Unconditional retention claim: "Every run writes its script to a file under your session's directory in `~/.claude/projects/`." Load-bearing premise of the archived-script read-back path and of `BAP-9`. | memory | doctrine/design | `SRC-1#how-it-runs` |
| `CLM-10` | claim | Lineage claim: the delivered report "cites the sources each claim came from". Distinct from `CLM-2` (which asserts the vote-and-filter *operation*); this asserts a **provenance property of the delivered artifact**. | epistemic | doctrine/design | `SRC-1#run-a-bundled-workflow` |

**Evidenced absences promoted to records.** Both lenses produced *documented* absences —
findings stronger than "we did not look". The packet had no namespace for these; the
orchestrator mints `ABS-*` (flagged as an improvisation in `trial-notes.md`, F9). Each names
its recorded search boundary, as the `absent` status requires.

| ID | Evidenced absence | Recorded search boundary | Proposed by |
|---|---|---|---|
| `ABS-1` | No cross-session or cross-run store of workflow **results/findings**. Doctrine positively asserts a fresh start: "If you exit Claude Code while a workflow is running, the next session starts the workflow fresh." | `SRC-1#resume`, `#how-it-runs`, `#save` | both |
| `ABS-2` | No documented **acceptance** of `OBJ-6` — no evaluator, criterion, intended use, or scope attaches to the delivered report. | `SRC-1#run-a-bundled-workflow`, `#when-to-use`, `#how-it-runs`, `#save`, `#bundled` | epistemic |
| `ABS-3` | No documented **retention or export** of `OBJ-6`. | `SRC-1#how-it-runs`, `#save`, `#resume` | epistemic |
| `ABS-4` | No documented **check on `OBJ-4`** in the general (non-`/deep-research`) case. | `SRC-1#when-to-use`, `#how-it-runs`, `#limits`, `#watch-the-run` | epistemic |
| `ABS-5` | No documented **retention of rejected `OBJ-9` claims or of `OBJ-11` vote results**. | `SRC-1#bundled`, `#run-a-bundled-workflow` | epistemic |
| `ABS-6` | No documented **comparison of a workflow's output against a single-pass baseline** — the absence that blocks `CLM-1`. | whole file | epistemic |

`ABS-*` records are scoped to **documented routes in `SRC-1`**. None asserts that no such
mechanism exists in the implementation.

### 8.2 Duplicate merge and namespace hygiene

- **No duplicate objects or routes were created.** Both lenses annotated the packet's
  existing `CMP-*`/`OBJ-*`/`RTE-*`/`BAP-*`/`CLM-*` records by ID, as instructed.
- **Linked-row suffixes** (`RTE-E3/check`, `RTE-E4`, `RTE-E5`, `RTE-E6/synth`,
  `RTE-E6/lineage`) are the authorized split of one base route into several functional rows,
  not a parallel namespace. They resolve to their base IDs.
- **`RTE-E3/extract` → `RTE-E9`.** The epistemic lens correctly refused to mint an ID for a
  route it found *undeclared*, and used a provisional linked label. The orchestrator has now
  given it a canonical ID with status `no route found within boundary`. This is the one place
  where a lens's local label needed promotion rather than mere mapping.
- **`RB-1`/`RB-2`/`RB-3`** (memory lens) are **path labels**, not new records. They map to
  existing IDs and are not carried into this result as canonical IDs:
  - `RB-1` = `RTE-S2` → `CMP-7` → `RTE-C7`, authority `BAP-2`, material `OBJ-7`
  - `RB-2` = `RTE-S1` → `CMP-8` → later read via `RTE-X4`, authority `BAP-9` → `BAP-1`, material `OBJ-1`
  - `RB-3` = `RTE-S3` → `OBJ-8` → `CMP-5`, authority `BAP-5`
- **`MG-1`..`MG-9`** (epistemic lens) are missing-evidence records, kept as-is and folded into §10.

### 8.3 Ownership held

| Layer | Owner | Verified |
|---|---|---|
| Complete control and context routes | runtime baseline (`evidence-packet.md` §7) | Yes — both lenses annotated `RTE-X1`..`RTE-X6` and the `RTE-C*`/`RTE-S*` routes; neither redefined an endpoint or a progression. |
| Read-back and activation | memory lens | Yes — the epistemic lens made no read-back or activation claim; it treated `RTE-S5`/`RTE-C6` as retention and recovery, which is its own vocabulary, not a read-back finding. |
| Transformation, checking, warrant, acceptance, integration, and the two authorities | epistemic lens | Yes — the memory lens explicitly **declined** to infer warrant from curation, endorsement from registry membership, or semantic preservation from lineage, and explicitly declined `CLM-1`. |

**Boundary, revision, and sources are consistent across every record**: one boundary
(subsystem-only, `evidence-packet.md` §3), one capture (`SRC-1`, 2026-06-03), one cutoff, one
register. Both lenses cite `SRC-1` for every positive finding and cite `SRC-2` for none.

### 8.4 Conflicts, preserved as conflicts

**C-1 — `OBJ-6` persistence: `uninspected` vs `absent`.** The memory lens recorded "no
persistence of the report to a store is documented" as **`uninspected`**; the epistemic lens
recorded it as an **evidenced absence** with a named search (`ABS-3`). These are different
statuses over the same fact. **Resolved on the vocabulary, not by picking the
stronger-sounding one:** the run's definitions make `absent` mean "not found within the
*named, recorded* search boundary" and `uninspected` mean "the evidence was unavailable or
not inspected". The epistemic lens named its search; the memory lens did not. The canonical
status is therefore **`absent` (`ABS-3`)**, and the memory lens's weaker reading is recorded
as under-specified rather than wrong. Note that `absent` here is still *scoped to `SRC-1`*
and remains compatible with an undocumented implementation route.

**C-2 — `CLM-3` ("Claude's context holds only the final answer") is doctrine-internally
imprecise.** The epistemic lens flagged the exactness of "only" as unknown. The memory lens's
`RTE-X4` annotation supplies the reason: the archived script's **path** is also pushed into
`CMP-12` at run start. The conflict is inside the source, not between the lenses, and it is
preserved as such: `CLM-3`'s substantive point (agent results do not land in the context
window) stands; its literal universal quantifier does not.

**C-3 — `OBJ-12` allowlist classification is open.** The memory lens classified the allowlist
as static configuration *provisionally*, conditional on whether mid-run prompts write back.
The epistemic lens treated `OBJ-12` as a non-truth-apt authorization consumed by `RTE-S4`.
These are compatible, but the open question is real and is now registered as `RTE-S7`
(`uninspected`). **Not resolved.** If `RTE-S7` turns out to exist, `OBJ-12` becomes a fourth
accumulation-through-use read-back path with **permissive** force over tool authority —
which would be the most consequential single change to this analysis.

**C-4 — Version divergence, carried from the register.** `SRC-1` is pinned to 2026-06-03 /
v2.1.154–v2.1.160; the host observed under `SRC-2` runs v2.1.237. Preserved unresolved
(`MG-8`, `L-2`); the cutoff stays at `SRC-1`'s date.

### 8.5 Cross-lens agreements that neither lens could reach alone

These are reconciliation products, not lens outputs.

1. **The subsystem retains method and authority, never findings.** The memory lens found that
   every durable retention holds a *procedure* (`OBJ-1`/`OBJ-7`) or an *authorization*
   (`OBJ-8`). The epistemic lens independently found no acceptance transition, no retention or
   export of `OBJ-6` (`ABS-3`), and lifecycle integration `not reached` by doctrine. Together
   these give a single structural finding with two independent derivations — and the doc's own
   `CLM-7` ("what's repeatable: the orchestration itself") states the design intent that
   matches it.
2. **Force and horizon run in the same direction as retention.** `BAP-1`/`BAP-2`/`BAP-9`/
   `BAP-10` (procedure) are enforcing and durable; `BAP-4` (findings) is advisory with a
   session/turn horizon. The memory lens established the horizons; the epistemic lens
   established the force asymmetry. Neither alone shows that the two axes align.
3. **The one curation act is ungated in both vocabularies.** `RTE-S2` is the memory lens's
   sole curation act, and the epistemic lens finds its stated criterion is "if the run does
   what you wanted" — a human bundle-satisfaction judgement whose target is the *procedure*.
   Per step 8.3, the curation label does not determine any epistemic transformation, and
   neither lens inferred warrant from it. **Bundle satisfaction licenses nothing about any
   component of the orchestration.**
4. **Checking and action are asymmetric, and the memory account explains why the gap
   persists.** Checking exists only inside `CMP-11` and applies only to report content
   (`RTE-E3/check`, `RTE-E4`); agent output that *drives action* has no documented check
   (`ABS-4`), and agents act unconditionally in forced `acceptEdits` (`RTE-S4`, `CLM-8`).
   The memory lens adds that `OBJ-4` is *retained, replayed on resume without revalidation,
   and reused as another agent's premise* (`RTE-X1`) — so unchecked output propagates
   forward through the retention layer as well as outward through the action layer.

**Two rules were checked and held.** Memory curation labels did **not** determine epistemic
transformation anywhere in this reconciliation. Behavioral influence was **not** allowed to
imply epistemic or operational authority — most visibly at `BAP-4`, where the report reaching
a context window is recorded as advisory delivery and explicitly **not** as activation, not as
acceptance, and not as warrant.

---

## §9. Bounded synthesis

Organized around the deployed system's progression. Scope: the dynamic-workflows subsystem
of Claude Code, at the 2026-06-03 documentation boundary, on `doc-grounded` evidence. **This
is a subsystem-only boundary; nothing here supports a conclusion about Claude Code as a
whole. No system-wide epistemic grade is given, and none is available at this evidence
boundary.** Every statement below is a doctrine-layer statement about a route unless marked
otherwise.

### Scheduling — the plan moves into code, and that is the whole design

The defining move is that the orchestration plan is written down as an executable artifact.
In the turn-by-turn alternatives the doc compares against, a model decides what runs next at
each step; here a **JavaScript script decides**, and the runtime executes it in an isolated
background process (`RTE-C3`, `RTE-C4`, `BAP-1`). Three consequences follow directly, and all
three are visible in the runtime account rather than inferred:

- **Scheduling becomes inspectable and repeatable.** The script can be read before it runs
  (`RTE-C2`), read after (`RTE-X4`), diffed against a previous run's, edited, relaunched, and
  installed as a command (`RTE-S2`). None of that is available for a plan that exists only as
  model intent across turns.
- **Scale is decoupled from context.** Fan-out is bounded by the runtime (≤16 concurrent,
  ≤1000 per run, `BAP-10`) rather than by what a context window can hold.
- **The model's judgement moves upstream.** It is spent once, on authoring (`RTE-C1`,
  Loop A), instead of continuously on dispatch. Under `/effort ultracode` (`BAP-8`) even the
  decision *whether* to use a workflow becomes a standing model decision for the session.

The trade the doc does not name: a script fixes the plan **before** any result is seen. The
only documented adaptations after launch are human interrupts (`RTE-C5`) and whatever
branching the script's author anticipated.

### Context assembly — code selects, and nothing tests what the selection did

The script composes each sub-agent's prompt from its own variables (`RTE-X1`). Selection is
**code-determined, not model-determined at dispatch**, which is the sharpest difference from
a conversational orchestrator. Results return into script variables, not into any context
window (`RTE-X2`), and only the final answer reaches the originating session (`RTE-X3`,
`CLM-3` — with the literal "only" qualified by C-2). Invocation input passes through a
model-performed structuring step on the way in (`RTE-X5/structure`) that has no preservation
check.

The packet's anti-conflation rule bites here and is the load-bearing observation: **the
runtime retains far more than any model ever sees.** Every agent result is tracked (`RTE-S5`);
most of it is never selected into a prompt and never reaches the session. What the human sees
by default is one synthesized report; the underlying per-agent prompts, tool calls, and
results are reachable only by opt-in drill-down (`RTE-X6`) that produces no verdict and gates
nothing. No route anywhere in the subsystem tests that delivered material actually changed a
receiver's behavior — there is no behavioral-faithfulness test on any context route.

### State and action — a pure coordinator delegating unconditional action

The script has **no direct filesystem or shell access** (`CLM-6`); sub-agents read, write, and
run commands (`RTE-S4`). This is a genuine architectural line, and it is easy to over-read:
it is an **isolation property of the orchestrator, not a check on action**. The agents doing
the acting run in forced `acceptEdits` regardless of the session's own permission mode, with
file edits auto-approved and the user's allowlist inherited (`CLM-8`, `BAP-6`). Non-allowlisted
shell, web, and MCP calls can still prompt mid-run (`RTE-C9`) — the only thing besides an
explicit pause that can stop a run, since there is otherwise no mid-run user input.

### Memory return — three read-back paths, all carrying procedure or permission

Applicable lens; the trigger was met three times over.

- **Saved workflow command** (`RTE-S2` → `CMP-7` → `RTE-C7`, `BAP-2`) — a script produced by
  one run becomes a `/<name>` command in future sessions, discoverable through `OBJ-15`, and
  when saved to `.claude/workflows/` it is shared with everyone who clones the repo. Force is
  enforcing on invocation; horizon is persistent. This is the strongest read-back path in the
  subsystem, and **no quality check, test, or review gates the save**.
- **Archived run script** (`CLM-9`, `RTE-S1` → `CMP-8`, `BAP-9`) — every run archives its
  script; the path is pushed to the session at run start and the content is pulled on demand.
  A *previous* run's file can be re-read, diffed, edited, and relaunched, at which point
  advisory material becomes control flow. No index, listing, search, retention bound, or
  staleness check over the archive is documented.
- **Persistent consent** (`RTE-S3` → `OBJ-8` → `CMP-5`, `BAP-5`) — an approval decision
  persists and suppresses later prompts; in Auto mode persistence is an automatic by-product
  of any Yes. Force is permissive: it removes a check without authorizing anything new. This
  is the **only** read-back path for which the documentation asserts the behavior change
  itself; the other two have `uninspected` activation.

Deliberately **excluded** as retained state rather than read-back: resume-from-cache
(`RTE-C6`/`CMP-9`) is same-run, same-session, and doctrine positively closes the cross-session
case; script variables, the final report into the session, the bundled `/deep-research` script,
and the session-scoped `ultracode` setting likewise.

**Nothing in this subsystem retains a finding.** No cross-run result store is documented, and
doctrine asserts a fresh start in a new session (`ABS-1`). Raw traces exist (`OBJ-4`, `OBJ-5`)
but no distillation step turns them into a retained artifact; `RTE-S2` copies the procedure,
never the results.

### Truth-apt and warrant routes — one real pipeline, no acceptance anywhere

Applicable lens; invoked through the epistemic procedure.

The subsystem's one documented knowledge pipeline is the bundled `/deep-research` workflow:
search fan-out → fetch → cross-check → vote → filter → cited synthesis (`RTE-E1`–`RTE-E6`).
Read at the doctrine layer, it is a **filtered acquisition-and-synthesis pipeline with
preserved citation lineage** — a real architectural commitment, and more epistemic structure
than an orchestration layer needs to have.

What it does **not** amount to, at this boundary:

- **Acquisition warrant is unknown.** External sources (`OBJ-10`) are imported with no
  documented authority, recency, independence, or quality criterion — and the value of
  cross-checking depends on exactly the independence property that is undocumented.
- **A step is missing from the doctrine itself.** `CLM-2` quantifies over "each claim", but no
  route producing claims from sources is declared (`RTE-E9`). That gap blocks classifying the
  claim object's transformation as faithful reshaping or as model conjecture, and blocks
  tracing source warrant into it.
- **The test domain is agreement, not truth.** Cross-checking and voting assess whether
  retrieved sources agree, by model evaluators whose rule, quorum, threshold, and tie-handling
  are all undocumented.
- **Disposition is admission by non-rejection.** Survival is named only by outcome. No rule,
  no intended use, no reliance scope, no persisted acceptance artifact — and rejected claims
  and vote results are not retained (`ABS-5`). **No acceptance transition in the invoked
  procedure's sense exists anywhere in this subsystem.**
- **Integration is not reached.** A surviving claim's terminus is a report delivered advisorily
  into a context window (`BAP-4`, horizon session/turn), with no documented persistence
  (`ABS-3`) and no acceptance (`ABS-2`).

The genuinely valuable epistemic feature is **`OBJ-16`, the per-claim citation binding**
(`CLM-10`): it is the subsystem's only warrant-transfer mechanism, and it is **reader-side**.
It lets a human re-derive or contest a claim. It issues no system warrant, and it is itself
unverified.

Outside `/deep-research`, no check is documented at all (`ABS-4`). Agent output is retained,
replayed on resume without revalidation, reused as another agent's premise, and acted on —
all before and without any check. **The asymmetry is the finding: action is unconditional and
continuous, while checking exists in exactly one shipped workflow and applies only to report
content, never to the agent output that drives action.**

The doc's own warrant claim (`CLM-1` — adversarial review or multi-angle weighing gives "a
more trustworthy result than a single pass") is, within this boundary, **untested**: there is
no baseline, no trustworthiness metric, no comparison, and no experiment anywhere in the
source (`ABS-6`, `MG-3`). It is further mismatched at the doctrine layer — it attaches to
capabilities of the pattern (`RTE-E7`, `RTE-E8`) with no named shipped instance, while the one
shipped instance implements a *different* pattern. It is licensed only as a stated design
rationale.

### Governing controls — one pre-execution decision, then a bounded free run

Authority in this subsystem is decided **once, before execution, by a human reading a phase
summary** (`RTE-C2`), with the full script text available only on request. That decision is
removable three ways: by permission mode, by a persistent consent record (`RTE-S3`), or
entirely under Auto plus ultracode. In `claude -p` and the Agent SDK there is no prompt at
all. After launch the controls are: the runtime's agent caps (`BAP-10`), mid-run permission
prompts for non-allowlisted tools (`RTE-C9`), human stop/pause/restart from telemetry
(`RTE-C5`), and the org-level kill switch (`BAP-7`) — which is the only hard prohibition.

Observability is the counterweight and is unusually good for a background system: per-phase
counts, tokens, and elapsed time, and per-agent prompt, recent tool calls, and result. But it
**gates nothing automatically**. It informs a human who may intervene, and it feeds the one
curation decision (`RTE-S2`) that has a persistent, potentially repo-shared consequence.

### Capability versus deployment, and the evidence floor

Two capability/deployment gaps are load-bearing and are preserved rather than smoothed over:
`RTE-E7`/`RTE-E8` are stated as things a workflow *can* be written to do, with no shipped
instance named; and per-stage model routing is likewise a script capability with no documented
instance. Separately, **every finding in this synthesis is doctrine-layer**. Nothing was
inspected in implementation, nothing was observed in a run, nothing was tested. That floor is
not a footnote to the synthesis — it is the reason no claim above rises past "the vendor
declares".

---

## §10. Limitations, each paired with the conclusion it prevents

| ID | Limitation | Conclusion it prevents |
|---|---|---|
| `L-1` | **Doc-only evidence.** Tier `doc-grounded`; `SRC-1` is vendor documentation (doctrine/design). No implementation inspected, no observed run, no causal experiment. | Prevents any status above `claimed` anywhere in the run; prevents concluding that any documented route actually operates, that any write path writes, or that any read-back path returns material. |
| `L-2` | **Version divergence, unresolved** (`MG-8`, C-4). `SRC-1` pinned 2026-06-03 / v2.1.154–160; host observed at v2.1.237; no changelog in the bundle. | Prevents any statement about present-day behavior of this subsystem, including whether the archive gained retention limits or whether consent semantics changed. |
| `L-3` | **No repository or implementation exists to inspect** for this system; it is a closed vendor feature. | Prevents ever reaching `code-grounded` for this target by the route this instruction defines, absent an observed run or a leaked artifact. |
| `L-4` | **No script text was inspected** (`MG-1`) — `/deep-research`'s source is boundary-excluded and `SRC-1` contains no example script. | Prevents naming the vote's quorum, threshold, tie or abstention rules; prevents attributing the filter's criterion; prevents any conclusion about how `RTE-X1` selects material into a prompt (policy, ordering, size discipline, truncation). |
| `L-5` | **No observed run** (`MG-2`); `SRC-2` is roster-only and negative. | Prevents **every** observed candidate state in the epistemic lens; prevents every activation and causal finding in the memory lens; prevents upgrading `CLM-2` past doctrine. |
| `L-6` | **No baseline, metric, or interventional comparison anywhere in `SRC-1`** (`MG-3`, `ABS-6`). | Prevents any support for the comparative core of `CLM-1`; prevents attributing trustworthiness to adversarial review, to cross-checking, or to agent count. |
| `L-7` | **The sub-agent primitive's internals are outside the bundle** (`MG-4`; `/en/sub-agents` not fetched, and fetching it would have widened the frozen boundary). | Prevents any conclusion about what a sub-agent loads besides its spawn prompt, whether agent-internal checking exists, or what warrant `OBJ-4` carries; specifically prevents claiming `RTE-X1` is the *only* context route into a worker. |
| `L-8` | **No claim-individuation step is documented** (`MG-5`, `RTE-E9`). | Prevents classifying `OBJ-9`'s transformation as non-ampliative reshaping or ampliative conjecture; prevents saying source warrant is preserved into it. |
| `L-9` | **`OBJ-3` persistence past process exit is uninspected** (`MG-7`). | Prevents concluding that intermediate results are strictly ephemeral, and prevents any confident statement about a run's data-at-rest footprint. |
| `L-10` | **`CMP-8` archive lifecycle undocumented** — no retention bound, deletion, rotation, or index. | Prevents concluding the archive is a usable memory surface over time rather than an unbounded write-only log; prevents estimating whether the re-read path degrades with volume. |
| `L-11` | **Consent-record invalidation undocumented** — nothing states whether a *changed* script under an existing workflow name re-prompts. | Prevents concluding that `OBJ-8`'s scope still matches what the human approved; therefore prevents any safety conclusion about the persistent-consent path. |
| `L-12` | **Allowlist write-back unresolved** (`RTE-S7`, C-3). | Prevents settling whether `OBJ-12` is static configuration or a fourth accumulation-through-use read-back path with permissive force over tool authority. |
| `L-13` | **Agent-restart (`r`) state semantics undocumented.** | Prevents any conclusion about within-run retry memory; leaves a possible intra-run retained-state route unregistered. |
| `L-14` | **Only one bundled workflow is documented, and no non-bundled script was inspected** (`MG-9`). | Prevents generalizing any checking or epistemic finding from `/deep-research` to workflows as a class — including to any workflow a user saves. |

**Conflicting evidence, published as a limitation:** C-1 (`uninspected` vs `absent` on
`OBJ-6` persistence, resolved on the vocabulary), C-2 (`CLM-3`'s "only" contradicted by
`RTE-X4` inside the source itself), C-3 (open, registered as `RTE-S7`), C-4 (version
divergence, unresolved).

**Unresolved applicability:** none. Both lens dispositions resolved to `applicable` and both
lenses ran.

---

## §11. Verification and blocker report

### 11.1 Result identity and location

| Field | Value |
|---|---|
| Result identity | `AAS-20260820-CCDW-01` |
| Location | `kb/work/multistage-write-analyse-agentic-system-20260820/trials/cc-dynamic-workflows/` (staging identity; entry point `result.md`) |
| Boundary | Claude Code dynamic workflows — **subsystem-only** |
| Revision / capture | `SRC-1`, captured 2026-06-03; cutoff 2026-06-03 |
| Evidence tier | `doc-grounded` |
| Memory/context lens | **`applicable`**, ran |
| Epistemic lens | **`applicable`**, ran (external procedure invoked) |

### 11.2 Step 10.1 verification

| Check | Result |
|---|---|
| Source anchors and statuses | **Pass.** Two sources registered with kind, identity, capture, evidence layer, inspected scope, anchors, and access gaps. Every positive finding cites `SRC-1` with a section anchor; `SRC-2` supports no positive finding and is cited as such. |
| Unique, resolving IDs | **Pass.** ID inventory in §1. Checked for collisions after minting `RTE-S7`, `RTE-X5/structure`, `RTE-E9`, `OBJ-15`, `OBJ-16`, `CLM-9`, `CLM-10`, `ABS-1`–`ABS-6`: none. Lens-local labels (`RB-*`, `RTE-E3/extract`) are mapped in §8.2 and are not canonical. |
| One boundary and revision across all records | **Pass.** Both lens outputs restate the same boundary and cutoff verbatim from the packet; neither widened either. |
| Mandatory runtime coverage | **Pass.** `evidence-packet.md` §7 covers five material loops with the full step-4.2 field list, the three anti-conflation checks, and materiality statements for each conditional surface inspected. |
| Both lens dispositions present as explicit records | **Pass.** `lens-dispositions.md`; neither is implied by an absent section, and the non-triggering candidates are recorded explicitly rather than omitted. |
| All applicable lens outputs present | **Pass.** Both lenses ran and both outputs are on disk; the epistemic output contains all six required blocks of the invoked procedure plus its step-7.4 returns (see the integrity note in 11.4). |
| Prevented conclusions stated for every non-run | **Pass, vacuously for lens non-runs** (no lens was skipped). Prevented conclusions are nonetheless stated for every negative and uncertain finding: `L-1`–`L-14`, `MG-1`–`MG-9`, and the recorded search boundary on every `ABS-*`. |
| Shared-route ownership respected | **Pass.** §8.3. |
| No forbidden evidence upgrades | **Pass.** §11.3. |

### 11.3 Step 10.2 distinction checks

| Distinction | Held? |
|---|---|
| Retention is not read-back | **Yes.** Resume-from-cache, script variables, the report into the session, the bundled script, and the session effort setting are all explicitly classified as retained state with reasons. |
| Context presence is not activation | **Yes.** The four-way table records presence, wiring, activation, and causal effect as four separate findings; two of three activation cells are `uninspected` and all four causal cells are `uninspected`. |
| Implementation is not deployment | **Yes.** `RTE-E7`/`RTE-E8` and per-stage model routing are recorded as capabilities with no named shipped instance. Nothing reached `implemented` at all — this run's floor is `claimed`/`doctrine only`. |
| Observation is not causality | **Yes, vacuously and explicitly.** There is no observation to over-read; `SRC-2` is negative and roster-only, and every observed candidate state is `no instance observed`. |
| Curation is not warrant | **Yes.** `RTE-S2` is the sole curation act; both lenses declined to infer validation, correctness, or endorsement from a saved script's presence in the registry. |
| Use is not acceptance | **Yes.** The report's delivery into a context window is advisory (`BAP-4`); the surviving-claim filter is recorded as admission by non-rejection, not acceptance; lifecycle integration is `not reached`. |
| Behavioral authority is not epistemic or operational authority | **Yes.** Three authority families kept separate throughout, with consumer/channel/force/horizon populated per `BAP-*` and never collapsed into a family label. |

### 11.4 Run-integrity note

The epistemic lens worker's process **terminated on a session usage limit after writing its
output file**. The orchestrator verified the file rather than assuming it: it contains all
six required output blocks of the invoked procedure in order, the per-object lifecycle
dispositions, the claim comparison for `CLM-1`–`CLM-8`, the bounded conclusion, and the
explicit step-7.4 returns section. **No content is missing and no lens work was redone.** The
worker's own last status line was written before its final tool call completed and is
misleading; the artifact on disk is authoritative.

### 11.5 Step 10.3 deterministic validation

**No deterministic validation was run, by rule and not by omission.** Step 9 forbids
improvising a collection contract or reusing the agent-memory review schema, and no
result contract exists for this artifact type. Step 10.3 anticipates exactly this and routes
to "applicable generic validation plus the semantic checklist"; the semantic checklist is
11.2–11.3 above. No schema or parser was changed to manufacture a validation path.

### 11.6 Blockers

**Publication blocker `PB-1` — no authorized target contract.**
There is no authorized publication target for this run, and no existing collection contract
in reach can represent an eleven-record, multi-lens, ID-reconciled system analysis. Per the
step-9 rule, the complete logical result is **retained under the run's staging identity**
(`kb/work/multistage-write-analyse-agentic-system-20260820/trials/cc-dynamic-workflows/`) and
the blocker is reported here. No collection contract was improvised and the agent-memory
review schema was not reused.

**No other blockers.** Specifically: no missing logical records (all eleven present and
indexed); no ID collisions (11.2); no unsupported material claims — every claim in §9 is
either doctrine-attributed or an explicitly scoped negative; no failed applicable validation
(11.5).

**Publishable limitations** (each already scoped in §10): doc-only evidence (`L-1`),
inaccessible components (`L-3`, `L-4`, `L-7`), no observed run (`L-5`), no causal experiment
(`L-6`), conflicting evidence (C-1 through C-4). Unresolved applicability: **none**.
