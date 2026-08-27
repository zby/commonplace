# Lens applicability dispositions — run `AAS-20260820-CCDW-01`

Step 5 of `analyse-agentic-system`. Both optional lenses carry an **explicit** disposition
record; neither disposition is implied by an absent section.

---

## Disposition 1 — Memory/context lens

| Field | Value |
|---|---|
| **Lens** | memory/context |
| **Disposition** | **`applicable`** |
| **Trigger evidence IDs** | `RTE-S2` + `BAP-2`; `RTE-S1` + `RTE-X4` + `BAP-9`; `RTE-S3` + `OBJ-8` + `BAP-5`; candidate: `RTE-C6`/`RTE-S5`/`CMP-9` |
| **Inspected boundary** | The subsystem boundary in packet §3, over `SRC-1` in full (2026-06-03 capture) plus the negative `SRC-2` capture |
| **Rationale** | The trigger is met several times over. (a) `RTE-S2`: a script *produced during a run* is saved into `CMP-7` and becomes a `/<name>` command in **future sessions** — material accumulated through use returning to a later invocation, and the clearest instance in the system. (b) `RTE-S1`/`RTE-X4`: **every** run archives its script under `~/.claude/projects/` and hands Claude the path; the docs explicitly describe reading it, diffing it against a previous run's script, editing it, and relaunching from the edited version — accumulated-from-use material re-entering a later run. (c) `RTE-S3`: consent recorded by a past approval decision changes whether a **later** launch prompts at all — a non-truth-apt policy read-back with permissive force (`BAP-5`). Each of (a)–(c) alone would suffice. |
| **Action** | Run the lens (step 6). Executed by a fresh worker context consuming only the prepared evidence packet and the frozen `SRC-1`. Output: `lens-memory-context.md`. |
| **Prevented conclusions** | None prevented by the disposition itself. The doc-only tier still prevents any `implemented`/`observed`/`causally supported` finding on any read-back path, and prevents every activation and causal-effect conclusion. |

**Note on a candidate that does *not* qualify as its own trigger.** `RTE-C6`/`RTE-S5`
(resume replaying cached agent results from `CMP-9`) is **ordinary current-run state**
under the run's definitions, and is explicitly session-bounded ("If you exit Claude Code
while a workflow is running, the next session starts the workflow fresh"). It is recorded
as retained state, not read-back. It is noted here so that the classification is on the
record rather than silently omitted.

**Note on material that is *not* a trigger.** Bundled workflow commands (`/deep-research`)
and the sub-agent tool allowlist (`OBJ-12`) are **static shipped or configured material**,
not accumulated-from-use material, and do not trigger the lens on their own.

---

## Disposition 2 — Epistemic lens

| Field | Value |
|---|---|
| **Lens** | epistemic |
| **Disposition** | **`applicable`** |
| **Trigger evidence IDs** | `RTE-E1`–`RTE-E6` over `OBJ-9`/`OBJ-10`/`OBJ-11`; `CLM-2`; `CLM-1` |
| **Inspected boundary** | Same as above |
| **Rationale** | Two independent triggers. (a) **Material truth-apt route**: the `/deep-research` chain (`CMP-11`) explicitly acquires external documents (`OBJ-10`), produces propositional **claims** (`OBJ-9`), *cross-checks* them against each other, *votes* on each one (`OBJ-11`), *filters out* those that fail, and emits a *cited* report. That is truth-apt content being produced, checked, and disposed — the trigger's core case. (b) **Consequential warrant claim**: `CLM-1` asserts that adversarial cross-review and multi-angle weighing yield "a more trustworthy result than a single pass". A warrant claim of that shape triggers the lens on its own, and the trigger holds even if the eventual finding is that the warrant is unsupported at this evidence boundary. |
| **Action** | Invoke `kb/instructions/analyse-external-system-epistemic-architecture.md` (step 7) with a bounded subquestion, this boundary, the frozen capture, the `SRC-*` register and evidence packet, the canonical records, and the trigger evidence above. Executed by a fresh worker context. Output: `lens-epistemic.md`. |
| **Prevented conclusions** | The doc-only tier prevents any `implemented` architectural status, any observed candidate state, and any causal conclusion about `CLM-1`. Non-inspection of the `/deep-research` script text prevents conclusions about the actual evaluator, voting rule, quorum, or filter threshold. |

**Direct-adaptation exception, applied and recorded.** `RTE-S3` (consent record) and
`RTE-C1`/`BAP-8` (the `ultracode` effort setting changing Claude's planning behavior) are
direct behavior/policy adaptations with no truth-apt object and no knowledge or warrant
claim. They do **not** by themselves trigger the epistemic lens, and they are kept in the
runtime account. Because the lens is applicable on other grounds, they are passed into the
invoked epistemic method as material non-truth-apt routes rather than being dropped.

---

## Neither disposition is `uncertain`

Both lenses have candidate triggers that resolve to `applicable` on the record. Per step 5,
a candidate trigger means `applicable`, not `uncertain`; no lens is exited here, so no
`uncertain`-driven evidence limitation arises from this step.
