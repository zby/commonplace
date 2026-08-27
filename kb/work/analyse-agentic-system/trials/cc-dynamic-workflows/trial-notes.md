# Trial notes — cold trial of `analyse-agentic-system`

**Trial apparatus. This file sits OUTSIDE the instruction's own logical result.**

- Trial: cold execution of `kb/work/analyse-agentic-system/candidate.md`
- Target: Claude Code dynamic workflows
- Run ID minted: `AAS-20260820-CCDW-01`
- Date: 2026-08-20
- Executor: sub-agent, `claude-opus-5[1m]`

---

## Physical layout chosen

The instruction deliberately leaves physical layout free (step 9). I chose **five result
files plus one capture artifact**, with the eleven logical records distributed as:

| Logical record | File |
|---|---|
| 1 run/staging identity | `evidence-packet.md` §1 (restated in `result.md` §1) |
| 2 boundary, revision, tier | `evidence-packet.md` §3, §4, §5 |
| 3 source register | `evidence-packet.md` §4 |
| 4 shared records | `evidence-packet.md` §6 |
| 5 runtime account | `evidence-packet.md` §7 |
| 6 both lens dispositions | `lens-dispositions.md` |
| 7 lens outputs | `lens-memory-context.md`, `lens-epistemic.md` |
| 8 reconciliation | `result.md` §8 |
| 9 bounded synthesis | `result.md` §9 |
| 10 limitations | `result.md` §10 |
| 11 verification/blocker report | `result.md` §11 |

`result.md` is the entry point and indexes the others. `capture-live-session-tool-roster.md`
is the `SRC-2` capture artifact.

**Note on the runtime account (logical record 5).** It is embedded as `evidence-packet.md`
§7, not written as a separate file. This was deliberate: the runtime baseline is both the
mandatory step-4 output *and* the material the lens workers had to consume, so keeping it
inside the packet meant the workers received it automatically rather than needing a second
pointer. The mandatory coverage is therefore satisfied without a `runtime-account.md`.

---

## Lens-applicability reasoning (short form)

**Memory/context — applicable.** Three independent read-back paths, any one sufficient:
the save-as-command path (`RTE-S2`, run-authored script becomes a command in future
sessions), the per-run script archive (`RTE-S1`/`RTE-X4`, explicitly diffed/edited/relaunched),
and the permission consent record (`RTE-S3`, past decision changes later launch behavior).
I deliberately classified resume-from-cache (`RTE-C6`) as *retained current-run state*, not
read-back, because the candidate's own definition excludes ordinary current-run state and
the docs bound resume to a single session.

**Epistemic — applicable.** `/deep-research` handles explicitly truth-apt content
(claims, cross-checking, voting, filtering, citation), and the docs make a warrant claim
(`CLM-1`, "more trustworthy result than a single pass"). Either trigger alone suffices.
Because the lens is applicable, step 7 fired and the external epistemic instruction was
invoked — this was the only step that required reading a third file.

---

## Friction points (ambiguities, impossibilities, improvisations)

### F1 — Live source unavailable; capture rule had no negative branch
Source input (2) was "the Workflow tool contract visible inside your own running session".
**No workflow tool exists in this sub-agent's tool roster.** Step 2.1's live branch says
"capture a dated inspectable boundary" but says nothing about what to do when the live
inspection returns an *absence*. I improvised: I captured the absence with a date and full
scope caveats (`capture-live-session-tool-roster.md`), registered it as `SRC-2` with
evidence layer `observed run` and an explicit "supports no positive finding" scope, and
proceeded doc-grounded on `SRC-1` alone. **Suggested instruction fix:** step 2 should say
whether a negative live capture is a source, a gap, or both.

### F2 — Capture/host version conflict, with no rule for it
`SRC-1` is pinned at 2026-06-03 documenting v2.1.154–v2.1.160-era behavior; the host CLI
observed during the `SRC-2` capture is v2.1.237. Step 2.2 says "record one analysis cutoff
for the whole run" but gives no rule for a second source whose capture date is far outside
the first's. I set the cutoff to `SRC-1`'s date and recorded the divergence as a preserved
conflict plus a limitation. **Suggested fix:** step 2.2 should distinguish the *evidence
cutoff* from the *run date* and say which one bounds conclusions.

### F3 — `BAP-*` "horizon" is defined but not exemplified
Step 3 introduces `horizon` as "a run-level extension recorded on each `BAP-*` path"
without saying what values it takes or what makes two horizons different. I read it as the
duration/scope over which the path keeps force (one run / one session / persistent /
org-wide) and used that consistently. This was a genuine guess. **Suggested fix:** one
example value tuple would remove the ambiguity cheaply.

### F4 — "Materiality" test for step 4.4 is circular in a doc-only run
Step 4.4 says to inspect conditional surfaces only when they "materially alter the analysis
question, a control path, evidence strength, or a lens result" — but with doc-only evidence
you often cannot tell whether a surface is material until after you have read it. I read
the whole (short) source first and then justified inclusion retrospectively, stating
materiality per surface as required. On a large code-grounded target this rule would be
much more expensive to satisfy honestly.

### F5 — Step 4.2's field list assumes a single loop grain
"For each material loop, record: trigger/input, next-step owner, decision policy…" does not
say how to individuate loops. This system has at least five plausible grains (authoring,
approval, script execution, sub-agent execution, human observation) that are nested rather
than peer. I used five loops at mixed grains and said so. **Suggested fix:** a sentence on
loop individuation, or an explicit licence to use nested loops.

### F6 — Step 3's evidence-tier rule vs. the epistemic instruction's status vocabulary
The candidate's conclusion statuses (`claimed`/`implemented`/`observed`/…) and the invoked
epistemic instruction's *architectural statuses* (`doctrine only`/`implemented`/
`observed, implementation uninspected`/…) overlap in wording but not in meaning —
`implemented` means different things in the two vocabularies, and the epistemic
instruction additionally uses *observed candidate state*. Step 7 forbids restating the
invoked method but does not address vocabulary collision. I instructed the epistemic worker
explicitly on the mapping. **Suggested fix:** step 3 should note the two vocabularies are
distinct and that `implemented` is not shared.

### F7 — Publication rule exercised as designed
No authorized target exists for this run. Step 9's rule ("retain the logical result under
the run's staging identity and report a publication blocker") was followed literally, and
the blocker is recorded in `result.md` §11. This was **not** friction — the rule handled
the case cleanly. Noting it because it is the branch under trial.

### F8a — Step 9's "in order" vs. a multi-file layout
Step 9 requires the eleven logical records "in order" while explicitly leaving physical
layout free. Across four files "in order" can only mean logical order. I preserved the
order in `result.md`'s index and cross-references rather than in byte order. Flagging it
because a validator reading one file at a time would see the records out of order.

### F9 — No namespace for an evidenced absence
Both lenses produced *documented* absences — negatives with a named search boundary, which
the candidate's own status vocabulary calls `absent` and distinguishes sharply from
`uninspected`. But step 3's canonical-record table has namespaces only for sources,
components, objects, routes, claims, and authority paths. An evidenced absence is a
first-class finding here (`ABS-6`, "no comparison against a single-pass baseline anywhere in
the source", is the single most consequential finding in the epistemic lens) and it had
nowhere to live. **I improvised an `ABS-*` namespace** and registered six, each carrying its
recorded search boundary. **Suggested fix:** either add an absence namespace to the step-3
table, or say explicitly that absences are recorded as limitations only.

### F10 — Lens workers mint local labels; the rule anticipates IDs but not labels
Step 3 forbids a lens from renaming or re-inventorying a registered object and requires new
material records to return for a canonical ID. Both workers complied on *records* — but both
also minted **local labels** for things the packet had not named: the memory lens used
`RB-1`/`RB-2`/`RB-3` for read-back *paths* (composites of existing routes), and the epistemic
lens used linked-row suffixes (`RTE-E3/check`, `RTE-E6/lineage`). The suffixes I had
explicitly authorized in the worker prompt; the `RB-*` labels I had not. Neither is a
namespace violation in substance — the underlying IDs are preserved and I mapped both in
`result.md` §8.2 — but the instruction gives no guidance, so a stricter reading would call
`RB-*` a parallel namespace. **Suggested fix:** one sentence permitting lens-local labels for
composite paths, provided they resolve to canonical IDs and are mapped at reconciliation.

The related good case: the epistemic lens found a route that `CLM-2` *presupposes* but the
docs never declare. It correctly refused to mint an ID for an undeclared route and used a
provisional label, which I then promoted to `RTE-E9` with status `no route found within
boundary`. The return-for-registration rule handled that cleanly.

### F11 — "Preserve conflicts" needed a tie-break rule the step does not state
The lenses disagreed on one status: whether the absence of report persistence is
`uninspected` (memory) or `absent` (epistemic). Step 8.1 says to preserve conflicts and
"never resolve one by selecting the strongest-sounding status" — correct, but it leaves no
positive rule. What actually resolved it was step 3's *definitions*: `absent` requires a
named recorded search boundary, and only the epistemic lens had named one. **This worked and
is worth making explicit:** status conflicts should be adjudicated against the status
definitions, not against evidence weight. Recorded as friction only because I had to derive
the rule rather than read it.

### F12 — Worker termination mid-step is not covered
The epistemic worker's process was killed by a session usage limit immediately after it
wrote its output file; its final self-report claimed it was still about to produce the
output, and the harness reported the task as failed. Step 3's worker-topology rule covers a
worker being *unavailable* (fall back to sequential) but not a worker **dying after complete
or partial work**. I verified the artifact on disk against the invoked procedure's six
required blocks rather than trusting either the self-report or the failure status, found it
complete, and recorded a run-integrity note in `result.md` §11.4. **Suggested fix:** step 3
should say that a worker's artifact is authoritative over its self-report, and that a
terminated worker's output must be verified against the expected record set before it is
accepted or redone. Without that, the default reaction to a "failed" notification is to redo
work that is already done.

---

## What I could not do

1. **Could not inspect any implementation.** No repository exists for this system; the
   runtime, the sub-agent primitive, and the `/deep-research` script text are all closed.
   Every finding is doctrine-layer. This is the single largest limit on the run.
2. **Could not observe a run.** No execution trace, no artifact, no phase record, no report
   instance. Consequently: no observed candidate state anywhere in the epistemic lens, and
   no activation or causal finding anywhere in the memory lens.
3. **Could not use the live source substantively** (see F1).
4. **Could not follow the source's outbound links** (`/en/sub-agents`, `/en/skills`,
   `/en/agent-teams`, `/en/agents`, `/en/costs`). They were not in the frozen bundle and
   fetching them would have widened the boundary, which step 2.4 forbids. Named as an
   excluded route family.
5. **Could not run deterministic validation against a result contract** — none exists for
   this result type (step 10.3 anticipates this and routes to the semantic checklist,
   which I ran instead).
6. **Did not read any prior Commonplace coverage of this system**, per the cold-trial
   constraint. I have no idea whether these findings agree or disagree with existing
   `kb/agentic-systems/` material.

---

## Instruction-quality observations from executing it

- The **frontloaded runtime baseline (step 4) is the strongest part**: it produced most of
  the shared record set, and both lenses then had something concrete to annotate rather
  than re-derive. The anti-conflation rules in 4.3 caught real distinctions here (the
  script is a scheduler but deliberately *not* an actor; `CMP-9` retains far more than
  ever reaches any context window).
- The **ownership table in step 3 did real work**: because routes were minted centrally
  before the lenses ran, reconciliation was mostly verification rather than merging. Only
  one genuine duplicate-risk area appeared (the several lives of the run script), and I
  pre-split it in the packet.
- **Step 5's "a candidate trigger means `applicable`, not `uncertain`"** is a good rule and
  was decisive here: it stopped me from parking the resume-cache question as `uncertain`
  and forced an explicit classification instead.
- **Running both lenses as fresh workers paid off in a specific, checkable way.** Neither
  worker could see the other's output, so the four agreements in `result.md` §8.5 are
  genuinely independent derivations rather than one lens echoing the other. The strongest —
  "this subsystem retains method and authority, never findings" — was reached from opposite
  directions: the memory lens by inventorying what persists, the epistemic lens by finding no
  acceptance transition and no report retention. A single-context run would probably have
  produced that claim once and left it looking like an assumption.
- **Step 7's "invoke, do not restate" is the right call but raises the coordination cost.**
  Passing the subquestion, boundary, revision, register, records, and trigger evidence into
  the invocation took a long prompt, and I had to pre-resolve a vocabulary collision (F6) and
  pre-authorize a labelling convention (F10) that the instruction does not mention. The
  invoked procedure is high quality; the seam between the two documents is where the work is.
- **Reconciliation was cheap because record ownership was settled first.** Because routes and
  objects were minted centrally before either lens ran, step 8 was mostly verification: one
  status conflict (F11), one label promotion (`RTE-E9`), zero merges of duplicate objects.
  This is the clearest evidence in the trial that the frontloading in steps 3–4 earns its cost.
- The **weakest instruction seams**, in order: step 3's status vocabulary versus the invoked
  instruction's (F6); the missing absence namespace (F9); the undefined `horizon` values
  (F3); and no rule for a terminated worker (F12).
