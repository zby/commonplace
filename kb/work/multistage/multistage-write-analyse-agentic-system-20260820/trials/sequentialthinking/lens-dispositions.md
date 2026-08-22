# Lens applicability dispositions — RUN `AGS-20260821-sequentialthinking`

Logical record 6. Both dispositions are explicit records, decided after the mandatory
step-4 runtime baseline and before any lens ran. Neither is implied by the presence or
absence of a section elsewhere.

---

## Disposition 1 — Memory / context lens

| Field | Value |
|---|---|
| **Lens** | memory/context |
| **Disposition** | **`applicable`** |
| **Trigger evidence IDs** | `OBJ-4`, `OBJ-5`, `RTE-6`, `RTE-7`, `RTE-9`, `SRC-1:94`, `SRC-1:96-101`, `SRC-1:113-114` |
| **Inspected boundary** | search boundary **B0** — the four subtree files at `2ecb382`, each read in full, plus targeted `rg` over `thoughtHistory`, `branches`, and all persistence/IO symbols |
| **Rationale** | The trigger asks for a path by which material *accumulated or changed through use* can affect a later invocation or action. Such a path exists and is inspected in implementation. `OBJ-4` and `OBJ-5` grow monotonically with use (`RTE-6`, `RTE-7`). At `SRC-1:113-114` the response builder reads both — `Object.keys(branches)` and `thoughtHistory.length` — and `RTE-9` returns those values to the host as part of `OBJ-6`. Call *n+1* therefore receives two values computed from material accumulated during calls *1..n*. Each MCP `tools/call` is a distinct invocation, and the `CMP-5` singleton spans all of them for the process lifetime, so this is cross-invocation return, not ordinary current-run state. The definitional exclusions do not apply: `OBJ-1`/`OBJ-2` are static shipped material and are excluded as triggers, but `OBJ-4`/`OBJ-5` are not shipped and are not per-call. |
| | The path is thin — derived scalars and keys, never content (`ABS-3`) — but thinness is a **finding of the lens, not a reason to skip it**. Step 5 states a candidate trigger means `applicable`, not `uncertain`. |
| **Action** | Run the embedded memory/context lens (step 6) in a fresh worker consuming only `evidence-packet.md`, `runtime-account.md`, and the frozen read-only boundary. |
| **Prevented conclusions** | Not applicable — the lens runs. Findings will be capped at `implemented` by `ABS-8` (no run artifact anywhere in the boundary), so no `observed` activation or causal effect can be established. |

---

## Disposition 2 — Epistemic lens

| Field | Value |
|---|---|
| **Lens** | epistemic |
| **Disposition** | **`applicable`** |
| **Trigger evidence IDs** | `CLM-1`, `CLM-2`, `CLM-3`, `CLM-4`, `CLM-5`, `CLM-8`, `CLM-10`; `OBJ-3.thought`, `OBJ-4`, `OBJ-5`; `RTE-4`, `RTE-6`; `SRC-1a:154-157`, `SRC-1a:187`, `SRC-2:12` |
| **Inspected boundary** | search boundary **B0**, as above |
| **Rationale** | Both halves of the trigger fire independently, so either alone would suffice. |
| | **(a) A material route handles truth-apt content.** The `thought` field is unconstrained natural language whose documented contents include "Hypothesis generation", "Hypothesis verification", "Realizations about needing more analysis", and "Questions about previous decisions" (`SRC-1a:160-167`). Content of that kind is capable of truth or falsity over a named scope. `RTE-4` disposes it (accept/reject the envelope), `RTE-6` retains it, and `RTE-8` renders it to a human reader — retention for later reliance and disposition of a candidate are both material-route criteria. |
| | **(b) The system makes consequential knowledge-production and warrant claims.** `CLM-2` claims hypothesis *verification*; `CLM-3` claims a *correct answer*; `CLM-4` is in the README's own system voice and claims the server's feature set includes "Generate and verify solution hypotheses". Verification and correctness are warrant claims, and assessing them requires the epistemic method. |
| | The **direct-adaptation exception** does not apply: it exempts evaluated direct behavior or policy adaptation that has *no* truth-apt object and *no* knowledge or warrant claim. Here there is both a truth-apt object and explicit warrant claims. |
| | Step 5 is explicit that the trigger fires "even when the eventual finding is failure or absence", and that "successful knowledge production is never a prerequisite for running the lens". `ABS-5`, `ABS-6`, and `ABS-9` make an absence-shaped finding likely; that strengthens the case for running the lens, since the claims can only be adjudicated by running it. |
| **Action** | Invoke [Analyse an external system's epistemic architecture](../../../../../instructions/analyse-external-system-epistemic-architecture.md) (step 7) in a fresh worker, inside this run's frozen boundary, under the step-7.3 wrapper rules. |
| **Prevented conclusions** | Not applicable — the lens runs. `ABS-8` caps every observed-candidate-state field at `no instance observed`; no lifecycle phase can be evidenced, and no causal support is available for any claim. |

---

## Worker topology decision

Fresh worker contexts are available and are used, per the step-3 preference. Each worker
receives only `evidence-packet.md`, `runtime-account.md`, this file, and read-only access to
the frozen boundary at `2ecb382`. Neither worker may reacquire, refresh, or widen sources,
mint a canonical ID, decide publication, or establish its own boundary. Lens-local proposal
tags (`MEM-n`, `EPI-n`) are used for any new record and are rewritten or merged by the
orchestrator at registration.
