# Trial evaluation — lens-routing cold trials of `candidate.md`

Evaluates four cold trials run 2026-08-20/21 against the exact candidate. Trial workers were fresh
`claude-opus-5` contexts given the candidate, their frozen source, and nothing else from `kb/`; prior
Commonplace coverage of every trial system was withheld so the runs stayed cold. Per-trial artifacts
live under `trials/<system>/`; each carries a `trial-notes.md` recording friction, which is the
evidence this evaluation rests on.

## Verdict

The candidate is executable end to end by a cold reader. Three trials (Fractal, Swamp, CC dynamic
workflows) produced the complete eleven-record logical result, held one source register and one
revision, kept IDs resolving across multi-file layouts, upgraded no evidence status, and reported the
publication blocker instead of improvising a target. The fourth (GBrain) completed its source freeze,
runtime account, both lens dispositions, and both lens outputs; its reconciliation and final records
were still being written when this evaluation was drafted, after a usage limit killed the run
mid-flight (see apparatus notes). Its central design bet — frontload the shared records and the runtime baseline,
then let isolated lenses annotate rather than re-derive — is validated by direct evidence, not just
by absence of complaint.

**Status after the trials.** The evaluation originally held the candidate back from promotion for one
structural reason — no trial exercised an early exit — and one list of ten recurring or
consequence-bearing defects. Both have since been worked through, and this document records the
history rather than the current blocker list:

- Twelve fixes were applied (the ten below plus two from the completed GBrain trial), then four more
  repairs after a fifth trial, one of which caught a regression introduced by fix 5 itself.
- The structural reason was escalated rather than repaired. A fifth trial run specifically to force
  an early exit failed to produce one, making it five for five; on that evidence the user chose to
  **make both lenses mandatory with depth proportionate to findings** (2026-08-21), which removes the
  untested branch by removing the branch. The workshop's design boundary was amended to match.
- Remaining before promotion: validate the new proportionate-depth rule (a re-run of the
  `sequentialthinking` trial against the revised candidate), the required acceptance review, and the
  deferred `allowed-tools`/`context`/`model` frontmatter, which is blocking at promotion.

## Coverage against R6.18 — the four combinations were not achieved

The skeleton required cold runs across four lens combinations: runtime only; runtime + memory;
runtime + epistemic; runtime + both. **All four trials returned `applicable` for both lenses.**

| Trial | Expected | Actual | Why the expectation failed |
|---|---|---|---|
| Fractal | runtime only | runtime + both | Disk-persisted session summary and `session_history` are re-delivered to later turns; the marketed deliverable is truth-apt and `AGENTS.md` states a provenance/warrant policy |
| Swamp | runtime + memory | runtime + both | Stored resources assert external state and the docs claim "accurate"/"validate they are correct"; both triggers fire independently |
| CC dynamic workflows | runtime + epistemic | runtime + both | Save-as-command, the per-run script archive, and the persistent consent record are each sufficient read-back |
| GBrain | runtime + both | runtime + both | As expected — the clean double positive |

Two scouting passes over the reviewed corpus had already failed to find a clean runtime-only or
epistemic-without-memory system, and the trials confirmed that read on the two contested picks.

### The fifth trial, run to force an early exit, also failed to produce one

A fifth trial was run against the post-fix candidate on a target chosen specifically for being
trigger-poor: the `sequentialthinking` MCP server, about 200 lines, no filesystem, no database, no
network, with accumulated thoughts held in plain instance fields. **It returned both lenses
`applicable` as well — five for five.**

The memory disposition turned on a definitional gap rather than a mis-pick. `index.ts:113-114`
returns `Object.keys(this.branches)` and `this.thoughtHistory.length` to the caller on every call:
not the accumulated *content*, but a count and a set of caller-authored branch labels, both derived
from state accumulated across prior calls. Under the trigger as written — material accumulated
through use that can affect a later invocation — that is read-back. The scout that nominated the
target read the same lines and concluded the opposite, because the content never returns. What
separates the two readings is that **"ordinary current-run state" is not defined against a unit**:
for a long-lived server process serving many tool calls, "the run" can be the process or the call,
and the disposition flips on which. The trial anchored it to the consuming agent's invocation, which
is the right reading, and that is now a repair.

The trial's own finding is the useful one: read-back exists but is *degenerate* — retention is
total, retrieval of content is nil, and branch labels are the only accumulated caller-authored text
that returns. The lens produced a real result on a near-trivial system rather than exiting.

### What five-for-five means

**For any system in scope, both lenses appear to be effectively always applicable.** The memory
trigger fires on a bare counter derived from accumulated state; the epistemic trigger fires on
shipped doctrine alone, since a tool description or README claiming the system verifies, checks, or
produces something is enough, and marketing copy of that shape is near-universal. Neither trigger has
fired an exit in five attempts across a deliberately spread sample: a research harness, an automation
control plane, a knowledge system, a closed vendor orchestration API, and a 200-line reasoning
scaffold.

This corroborates the KB's existing thesis that agent memory is a crosscutting concern rather than a
separable niche. It also raises a design question the trials cannot settle, because the workshop's
design boundary fixes the two-optional-lens architecture: if `inapplicable` is unreachable in
practice, the applicability gate buys an explicit disposition record rather than any saved labour,
and the alternative — making the lenses mandatory with depth proportionate to what is found, so a
degenerate case yields a short lens output instead of an exit — is not currently permitted. See
"Open architecture question" below.

What remained untested at that point: the `inapplicable` branch, the `uncertain` branch, the
early-exit record shape, and the direct-adaptation exception as a *decisive* call. The exception was
checked in Swamp and Fractal and correctly found not to apply, but it never carried a disposition on
its own. The architecture decision below removes the first three from the design rather than testing
them.

## Sixth trial — validating proportionate depth (resolved)

After the architecture amendment, `sequentialthinking` was re-analysed cold against the revised
candidate, in a separate directory, with the earlier run's output explicitly withheld. The new
failure mode under test was the inverse of the old one: with no gate to exit through, the risk is
padding a thin subject to look substantial. It did not occur.

**The decisive evidence is that the two lenses got different depths on the same subject.** Memory was
judged **brief** — read-back is real but degenerate, and "a full pass would have produced eight rows
of 'none, see line number'". Epistemic was judged **full** — a warrant claim sitting next to zero
evaluators needs the route ledger and claim table, not a bounded confirmation of thinness. Depth was
set from what the evidence supported, per lens, which is exactly what the rule asks for and what a
padded or stubbed run could not have produced.

The brief pass also stayed complete: it named what was inventoried, what was found, and what the
thinness prevented, rather than collapsing into a stub. And the run produced a *sharper* headline
finding than the pre-amendment trial of the same target: the tool description ships four assertions
with no implemented route on the same channel as a numbered instruction block delegating those exact
four operations to the model — one-to-one, forty lines apart, with the hedge present in the
instruction and stripped from the feature claim. The verification claim then fails a stage earlier
than a missing evaluator: the schema individuates revisions and branches but has no hypothesis field,
so the object said to be verified cannot be named in the protocol at all.

Independently validated in the same run: the widened **correction branch** was named the
instruction's strongest mechanism. Both lens workers found the orchestrator's evidence packet
defective — one of them a misclassification that would have concealed the headline finding — and the
"misclassified by its own stated criterion" clause is what made the orchestrator accept a correction
rather than dismiss it as emphasis.

Three new friction points came out of it: the repurposed direct-adaptation exception collides with an
explicit class in the invoked procedure (a defect introduced by the amendment, being repaired); the
two `implemented` vocabularies remain "the one rule whose violation would be silent and fatal,
defended only by executor discipline", which argues for renaming our own status rather than warning
about the collision; and the evidence tier is judged from the step-4 baseline while ordered as
logical record 2, forcing a two-pass read.

## Open architecture question (resolved 2026-08-21 — option 2)

The targeted attempt to exercise an early exit has now been made and has failed, so the R6.18
requirement cannot be satisfied by picking a better target. Five trials, five both-applicable
dispositions. The remaining choices are design choices, not sampling choices:

1. **Keep the two-optional-lens architecture and record the limitation.** Promote with the
   `inapplicable`/`uncertain` branches explicitly marked untrialled, and require the first
   `inapplicable` disposition produced in real use to be reviewed before it is trusted. Cheapest;
   leaves untested exactly the path where a careless executor turns "we did not check" into "there is
   nothing there."
2. **Make both lenses mandatory, with depth proportionate to what is found.** The degenerate case
   becomes a short lens output rather than an exit — which is what the fifth trial produced anyway,
   and it produced a genuine finding (total retention, nil content retrieval) that an exit would have
   discarded. Removes the untested branch by removing the branch. Requires amending the workshop's
   fixed design boundary, which currently mandates explicit applicability dispositions for both
   lenses.
3. **Sharpen the triggers so degenerate cases exit.** Not recommended. It would require excluding
   things like a returned counter or label set, and that is the precise judgement call the trigger
   was written to take away from the executor; the KB's own thesis is that memory is crosscutting, so
   a trigger that fires broadly is arguably correct rather than broken.

Option 2 is the one the evidence points at, and option 1 is the one the current design boundary
allows. This is a user decision because the two-optional-lens shape is fixed by that boundary.

## What the trials validate

Each item below is backed by a trial executor naming a specific moment where the rule changed what
they wrote.

- **Mandatory runtime baseline before lens applicability.** Two trials independently reported that
  deciding applicability first would have been guesswork, and that after mapping the loops both
  dispositions were obvious. This ordering is load-bearing.
- **Central ID minting before the lenses run.** CC dynamic workflows reported reconciliation as
  "mostly verification: one status conflict, one label promotion, zero merges of duplicate objects" —
  the clearest evidence that the frontloading in steps 3–4 earns its cost.
- **The conclusion-status vocabulary and never-upgrade list.** Swamp caught itself three times about
  to write that the system "checks" something the code only conforms, and once about to treat an
  audit trail as agent memory.
- **The memory definition's exclusion of static shipped material.** Swamp's most conspicuous artifact
  is a ~1.1 MB bundled skill corpus; without the exclusion the trial would have run the memory lens
  over it and produced a category error. The wording is load-bearing, not decorative.
- **"A candidate trigger means `applicable`, not `uncertain`."** Decisive in two trials; it stopped
  both from parking a hard question as `uncertain`.
- **"Successful knowledge production is never a prerequisite."** Swamp produces no knowledge inside
  its boundary at all; without this clause the executor would have been tempted to record
  `inapplicable` after discovering that — discarding the run's most interesting finding.
- **Pairing every negative with its prevented conclusion.** Reported as making the absences the most
  informative part of the result.
- **The publication blocker rule.** Exercised in all four trials and handled cleanly every time.
- **Fresh-worker lens isolation.** Where it ran, it produced *independently derived agreement*: in
  Fractal both lenses converged on one discarded host-side measurement from opposite directions
  (write-side provenance vs warrant), resting on an `rg`-verifiable absent call site rather than
  either worker's judgment; in CC dynamic workflows the strongest synthesis claim was reached from
  opposite directions. A single-context run would have produced each claim once and left it looking
  like an assumption.
- **The prohibition on a system-wide epistemic grade.** Easy to honour and clearly right where
  checking quality varies sharply between subsystems.

## Defects to fix before promotion

Ranked by recurrence across trials and by whether they changed a recorded result.

1. **Step 2/4 ordering is wrong for a code target** *(Fractal, Swamp)*. Step 2.4 requires the packet
   to contain "the canonical records registered so far", but the runtime baseline that discovers
   those records is step 4. Following the steps literally yields either an empty packet or a
   mid-step-2 discovery that step 4 must run first. Fix: fold record registration into step 4, or
   state that step 4 completes before the packet is finalized.
2. **Status-vocabulary collision with the invoked epistemic instruction** *(CC dynamic workflows;
   verified directly)*. The candidate's `implemented` is a conclusion status ("inspected code affords
   it"); the invoked instruction's `implemented` is an *architectural* status sitting beside
   `doctrine only`. The words overlap, the meanings do not. Step 7 forbids restating the invoked
   method but says nothing about vocabulary. The trial had to pre-resolve the mapping in its worker
   prompt. Fix: state in step 3 or 7 that the two vocabularies are distinct and `implemented` is not
   shared.
3. **Evidence tier has no branch for a split boundary** *(Fractal; Swamp hit the same shape and
   resolved it differently)*. Where every loop the system *owns* rests on inspected code but the loop
   producing the actual agentic behavior is a declared external dependency, the tier rule's two
   sentences give opposite answers. Two trials chose `code-grounded` by different reasoning, which
   makes the field non-comparable across runs. Fix: make the tier explicitly boundary-relative, or
   require a two-part tier.
4. **A terminated worker's artifact versus its self-report** *(CC dynamic workflows; validated by
   real events in three trials)*. Step 3 covers a worker being *unavailable* but not one that dies
   after complete or partial work. In CC dynamic workflows the epistemic worker was killed
   immediately after writing a complete output while its self-report and the harness both said
   "failed"; the executor verified the artifact against the expected record set rather than redoing
   the work. Without a rule, the default reaction to a failure notice is to redo work already done.
   Fix: state that the artifact is authoritative over the self-report and must be verified against
   the expected record set before being accepted or redone.
5. **Scope test ambiguity excludes agent operating layers** *(Swamp; verified directly)*. In "an
   agent runtime, harness, orchestration framework, agent operating layer, or a narrower system whose
   deployed behavior depends on model calls plus surrounding machinery," the trailing clause
   grammatically qualifies only "a narrower system" but reads as a test over the whole list. Swamp
   contains no model call at all — it is deterministic machinery driven by a model living elsewhere —
   so the literal reading excludes an enumerated kind. Fix: restructure so the dependency test does
   not appear to govern the enumeration.
6. **No namespace for an evidenced absence** *(CC dynamic workflows)*. The status vocabulary
   distinguishes `absent` (a negative with a named search boundary) from `uninspected`, but the
   canonical-record table has no namespace for one. The trial improvised `ABS-*` and registered six;
   one of them was the single most consequential finding in its epistemic lens. Fix: add an absence
   namespace, or state that absences are recorded as limitations only.
7. **Step 10.3's validation requirement resolves to the empty set** *(Fractal, Swamp)*. With no
   authorized target there is no contract, no frontmatter, and no applicable generic validator, so the
   semantic checklist is the entire verification. The instruction is self-consistent — it forbids
   manufacturing a validation path — but an executor should be told plainly that "no deterministic
   validation is applicable" is an acceptable outcome, because the natural move otherwise is exactly
   the forbidden one.
8. **`horizon` is required but never exemplified** *(Fractal, CC dynamic workflows)*. Both trials
   guessed, and both guessed the same thing (duration/scope over which the path keeps force). Fix:
   one example value tuple.
9. **Step 9's "in order" versus multi-file layout** *(CC dynamic workflows, Swamp)*. Every trial chose
   a package over one file, and every trial satisfied some records by pointer. "In order" can then
   only mean logical order. Fix: say whether pointer-satisfaction counts and that logical order
   governs.
10. **A lens correcting a registered record** *(Fractal; also GBrain)*. Step 7.4's "affected work is
    rerun" covers new records and targeted-read invalidation, but not the case where a lens finds the
    packet itself *wrong*. In Fractal both lenses caught a false lineage claim in the packet; in
    GBrain the memory lens corrected a registered artifact count. Strictly read, the rule demands a
    rerun — but in both cases the lenses had already worked from the corrected facts because they read
    the source rather than trusting the packet. Fix: add a correction branch distinct from
    invalidation.

## Defects to record as known limits

Real but lower-consequence, single-trial, or cheap to live with: run/result ID has no format or
allocation rule; "promotion path toward stronger form or force" is undefined inline; no rule for a
named, pinned, acquirable dependency that is not present (this is what forced Fractal's subsystem
boundary); no slot for an out-of-boundary model-calling *peer* actor, as distinct from a subsystem;
the runtime loop template has no "owner is out of boundary" field value; `CLM-*` ownership is thinner
than the table implies, since registering claims before the epistemic lens runs is already close to
an epistemic judgement; a *negative* live capture is neither clearly a source nor clearly a gap;
evidence cutoff is not distinguished from run date when a second source is captured much later;
step 4.4's materiality test is circular on a doc-only target; loop individuation/grain is unspecified;
lens-local labels for composite paths are neither permitted nor forbidden; and status conflicts are
adjudicated by the status *definitions* rather than by evidence weight — which worked, and should be
stated. One positive gap: independently convergent lens findings are stronger evidence than either
lens alone, and step 8 currently discards the convergence as a duplicate.

## Post-trial revision pass — disposition of the twelve defects

Applied to `candidate.md` on 2026-08-21: the ten defects listed above plus two added after the GBrain
trial finished (fixes 11 and 12 below). All twelve are **applied**; none declined. Nothing in "What the
trials validate" was touched — the mandatory-runtime-baseline ordering relative to lens applicability,
the never-upgrade list, the static-shipped-material exclusion, "a candidate trigger means `applicable`,
not `uncertain`", and "successful knowledge production is never a prerequisite" are byte-identical to
the trialled text.

1. **Step 2/4 ordering** — applied as the cheaper repair, per direction: step order unchanged, the
   dependency made explicit. Step 2.4 now opens "Freeze the sources here; finalize the evidence packet
   after step 4," names the sequence (2.1–2.3, step-3 rules, step-4 baseline, then assemble once), and
   step 4.2 gains "Register the `CMP-*`, `OBJ-*`, and `RTE-*` records this baseline discovers as you
   go: these are the canonical records the step-2.4 packet carries."
2. **Status-vocabulary collision** — applied as two distinct-namespace statements, no unification. A
   new step-3 bullet says the statuses are this instruction's namespace and that the invoked method's
   `implemented` is an architectural status contrasting with `doctrine only`, "different fields; record
   each in its own terms." Step 7.3's wrapper rules add: map returns by recording both terms, never by
   rewriting its architectural `implemented` into the conclusion status of the same name.
3. **Split-boundary tier** — applied as boundary-relative, not two-part, per direction: "The tier is
   relative to the declared boundary — judge it over the loops the boundary includes. A loop the
   boundary declares an external dependency neither raises nor lowers the tier, but record it as a
   limitation naming the conclusion it prevents... Report one tier; do not split it into parts."
4. **Terminated worker's artifact** — applied in the run-level Worker topology subsection: the written
   artifact is authoritative over the worker's self-report and any harness failure notice; verify it
   against the record set that lens owed, accept if complete, redo only what is missing; "A failure
   notice alone is not grounds for redoing work already written."
5. **Scope test** — applied as sentence restructure only; scope unchanged and not narrowed. The
   enumeration and the model-call test are now separate routes, with "The model-call test admits
   narrower systems — it does not restrict the named kinds" and an explicit clause keeping a named kind
   in scope when the model call it serves runs outside its boundary (the Swamp case). The frontmatter
   `description` gets the same restructure so the trigger text matches.
6. **Absence namespace** — applied as `ABS-*`, per direction, rather than relegating absences to
   limitations. New table row (orchestrator-owned; lenses return absences with their recorded search
   boundary for central registration) plus a rule: an `ABS-*` carries the searched boundary and the
   conclusion the absence prevents or supports, and an `uninspected` gap is explicitly *not* an
   absence and gets no ID.
7. **Validation empty set** — applied in step 10.3: "When no authorized target contract applies, no
   deterministic validation applies either: record `no deterministic validation applicable` alongside
   the semantic checklist result and treat that as a complete verification," with the forbidden move
   restated (no schema/parser change, no adopting an unrelated contract).
8. **`horizon` unexemplified** — applied with an example tuple matching what both trials guessed:
   `{consumer: spawned lens workers; channel: injected system prompt; force: binding instruction;
   horizon: the single run that spawned them}`, plus a gloss of horizon as the span over which the path
   keeps its force.
9. **Step 9 "in order" vs multi-file** — applied as a new rule: order is logical, not physical; a
   package may distribute records and satisfy one by a resolvable pointer, provided the result names
   one canonical location per record and every ID resolves across parts.
10. **A lens correcting a registered record** — applied as a correction branch explicitly distinct from
    invalidation: the lens returns the correction with its evidence anchor rather than re-inventorying;
    the orchestrator amends the record, notes the superseded value, and reruns only work that relied on
    it; a lens that already derived findings from the corrected source facts does not repeat its work.

### Two further defects from the completed GBrain trial

11. **Parallel fresh workers collide on ID allocation** *(GBrain; verified in its artifacts)*. The
    instruction prefers parallel fresh lens workers and requires new records to return for a canonical
    ID, but supplied no allocation scheme — so `result.md` §4 registered `SRC-19` =
    `src/openclaw-context-engine.ts` while `lens-epistemic.md` §1 independently proposed
    `PROPOSED-SRC-19` = `src/core/cycle/propose-takes.ts`. Different files, one number, colliding the
    moment either is promoted; GBrain reports three collision classes. The collision is guaranteed
    under the preferred topology, not incidental. **Applied** as the orchestrator-rewrites option,
    which the trials show already works informally: a lens proposes each new record under a lens-local
    tag (`MEM-1`, `EPI-2`, unique only inside that lens) and cites it that way throughout its return;
    the orchestrator rewrites accepted proposals to canonical IDs on registration and records the
    mapping; workers never mint a canonical ID. A closing clause reconciles this with step 7's "no
    parallel ID namespace" rule — a proposal tag is discarded at registration and never reaches the
    emitted result.
12. **`BAP-*` leaned on a definition a cold executor cannot open** *(Fractal F-4, GBrain F4)*.
    **Applied**, and merged with fix 8 as directed since both touch one sentence. Step 3 now defines
    all four parts inline — consumer, channel, force, and horizon — with "These four definitions are
    complete as given; apply them without opening any other document," followed by the example tuple
    from fix 8. The earlier revision of this sentence still framed the linked note as the definition's
    home ("the three parts the cited definition fixes"); that framing is gone. The footer `rests-on`
    link stays as grounding metadata for reviewers, which is what the collection reserves it for.

### GBrain friction points folded beyond the twelve

`trials/gbrain/trial-notes.md` carries fifteen friction points in its finished form. F13 is fix 10
(now hit by three trials), F14 is fix 11, and F15 is fix 4's mid-flight variant — the run was killed
after both workers completed but before their output reached disk, which fix 4's artifact-over-
self-report rule disposes wherever the artifact survives. F1, F3, F5, F7, F8, F10, and F11 are covered
by the fixes above or by the known-limits list. F14 also supplied the identity-keyed merge rule now in
fix 11: a proposal whose identity is already registered merges instead of taking a second ID, the rule
GBrain invented mid-reconciliation. Of the remainder:

- **F2 (a source checkout is not homogeneous)** — folded into step 2.3: a source whose parts carry
  different layers records each layer against the inspected scope it covers instead of flattening the
  source to one layer.
- **F4 (`BAP-*` depends on a definition the executor may not open)** — promoted out of this list; it
  is fix 12 above. GBrain called it "the sharpest dependency-on-absent-context in the instruction."
- **F6 (the ten-field loop record versus the "fixed template" prohibition)** — folded into step 4.4:
  the prohibition governs the conditional surface inventory, not the mandatory loop record, "whose
  fields are fixed on purpose."
- **F9 (static-vs-accumulated is not decidable per artifact kind)** — **declined for this pass.** The
  per-kind exclusion is in "What the trials validate" with a specific trial moment (Swamp's ~1.1 MB
  bundled skill corpus), and the direction for this pass forbids changing it. GBrain's case (SkillOpt
  moving an installed skill into an accumulated-through-use category) is real and argues for a
  per-instance test, but replacing a validated rule is a claim-level change, not a defect repair.
  Recorded as an open question for acceptance.
- **F12 (no stopping rule for a very large subject)** — **declined**; recorded as a known limit. The
  depth choice interacts with the tier rule that fix 3 just changed, and inventing a sampling rule here
  would be an unplanned commitment.

The evaluation's own known-limits paragraph is untouched by this pass, including its positive gap
(step 8 discarding independently convergent lens findings as duplicates). Those remain limits to
record, not fixes to apply.

## Fifth trial — `sequentialthinking`, run against the revised candidate

Run 2026-08-21 against the post-revision `candidate.md`, deliberately targeting a trigger-poor subject
(an MCP server of roughly 200 lines) to exercise an early exit. **It did not exercise one: both lenses
came out `applicable` again — five for five.** Artifacts in `trials/sequentialthinking/`; friction
detail in its `trial-notes.md` §A.

Two revisions from the previous pass are confirmed working by this run, and are not to be disturbed:
the **fix 11 lens-local tag scheme** prevented a real collision (the memory lens's `MEM-1` and the
epistemic lens's `EPI-1` named different things and would have collided had either minted a canonical
ID), and the **fix 2 `implemented`/`implemented` warning** was consulted and worked (§A7).

### Repairs applied (R1–R4)

All four are defect-level; none touches the applicability architecture, which is a separate open
question for the user and is deliberately left alone here.

- **R1 — regression in fix 5, repaired.** The clause added last pass ("A system of a named kind stays
  in scope when the model call it serves runs outside its own boundary") was grammatically bound to
  the enumeration route, but this subject was admitted through the *narrower system* route, so the
  clause that should have resolved it did not reach it (§A1). The trial also found route (ii) reads as
  covering only systems that *issue* model calls, while this server only serves them. Step 1.2 now
  reads "depends on model calls it issues **or serves**" and the clarifying clause opens "Under either
  route," naming both the model-driven-machinery case and the serves-a-call-it-never-issues case.
- **R2 — third boundary kind added.** Step 1.4's whole-system/subsystem-only binary forced an
  improvisation in four of five trials (Fractal and GBrain: whole-system for the repo, subsystem-only
  for the advertised loop; Swamp: whole-system for swamp, partial for the composite loop; this trial:
  "whole-artifact, not whole-loop"). The recurring shape is now a named kind — **complete artifact,
  partial loop** — with its own conclusion-limiting rule: conclusions may be whole-artifact but may not
  describe the behavior the crossing loop produces, and the external participants are listed as named
  exclusions each with the conclusion it prevents. Step 1.4 is now a three-item list rather than a
  single sentence.
- **R3 — "ordinary current-run state" anchored to a unit.** The exclusion was decisive here and the
  disposition flipped on the reading (§A5): for a long-lived stdio server, "current run" can mean the
  process lifetime or one tool call. The definition now fixes it as **the consuming agent's invocation
  boundary, not the host process's lifetime**, and states that state surviving from one consumer
  invocation to the next is read-back even when a long-lived process holds it and even when only a
  derived value returns rather than the content — the trial's verified case, `index.ts:113-114`
  returning `Object.keys(this.branches)` and `this.thoughtHistory.length` to every later call. The
  consequence is stated in the text as deliberate: read-back becomes easy to trigger, and a degenerate
  read-back belongs in a brief lens output rather than an early exit. The validated static-shipped-
  material exclusion in the same definition is untouched.
- **R4 — correction branch widened, and unclassifiable returns given a destination.** The
  wrong/incomplete binary fitted neither of the trial's two real corrections (§A9: a record
  misclassified by its own stated criterion, and one true as far as it went but misleading past that
  point). The branch now triggers on a record that is false, misclassified by the criterion the record
  itself states, or accurate but misleading at the scope it is stated. More consequentially, five of
  the epistemic lens's six proposals fit none of the six record kinds and none of the correction branch
  (§A8) — findings *about* records, such as an output asserting something false or a lineage break.
  These now register as **amendments** to the record they attach to, carrying an evidence anchor and
  any superseded value and cited through that record's ID, with an explicit rule against discarding
  such a return or inflating it into a new record. The amendment mechanism and its superseded-value
  discipline are adopted from what this trial improvised. Step 9's record 4 was updated for
  consistency, since it had not been refreshed when `ABS-*` was added either: it now reads "shared
  component, object, route, claim, absence, and authority records, each carrying its amendments."

### Noted, not applied

- **§A10 (dotted sub-anchors versus "no parallel ID namespace").** The worker split heterogeneous
  registered objects as `OBJ-3.thought`, `RTE-4 (a)/(b)/(c)` to satisfy the epistemic method's own
  split rule without minting a parallel namespace. The trial calls this the right answer, and it
  extends rather than parallels the canonical namespace — but authorizing a sub-anchor grammar is a
  design addition beyond a defect repair. Recorded for acceptance.
- **§A3, §A4, §A11.** Tier reading stronger than the analysis's reach (the trial reports the
  instruction already handles it), packet assembly reading as a loop-back (minor, and the fix-1 wording
  is what made it legible), and an under-split runtime container the trial marks self-inflicted.

The early-exit gap is now five trials wide and is escalated as an open question rather than patched
here.

## Architecture decision — both lenses mandatory, depth proportionate (user, 2026-08-21)

The user resolved the open applicability question with **option 2: make both lenses mandatory, with
depth proportionate to what is found.** This amends the workshop's fixed design boundary and is
recorded as such in `README.md`; it is an authorized amendment, not drift.

### Applied to `candidate.md`

- **Step 5 is now "Scope the two lenses,"** not a gate. It emits a per-lens scoping record —
  `{lens, trigger evidence IDs, inspected boundary, routes and objects the evidence points the lens
  at, warranted depth, rationale}` — keeping the part worth keeping, which is where trigger evidence
  gets named before a worker sees it. `applicable`/`inapplicable` are gone from the record.
- **`uncertain` is neither a scoping value nor an exit.** Unresolvable evidence becomes an explicit
  limitation inside the lens output, paired with its prevented conclusion. The text states the reason
  the branch was removed rather than relaxed: an exit meaning "we could not tell" reads later as
  "there is nothing there."
- **Proportionate depth is given a floor** so it cannot be hand-waved: however degenerate the case, a
  lens output states what was inventoried, what was found, and what the thinness prevents, and
  brevity never licenses dropping the prevented-conclusion pairing. The fifth trial's memory finding
  is embedded as the worked example of a complete brief result. Step 6 adds that a brief pass covers
  the full pass's ground proportionately rather than skipping items silently.
- **The direct-adaptation exception survives with a new job.** It no longer decides whether the
  epistemic lens runs; it scopes what the lens treats as its objects, and the route stays in the
  runtime account, named for the orchestrator in the scoping record.
- **Step 7's invocation is unconditional,** and the scoping record is passed so the invoked procedure
  knows whether it is building a full route ledger or bounding a thin finding. The text states that
  depth is the *only* thing the scoping record governs; the wrapper rules are unweakened and hold
  identically at either depth.
- **Downstream contract updated:** logical record 6 is now "both lens scoping records" and record 7
  "both lens outputs" with no early-exit alternative; step 8.4 mentions a lens's thinness rather than
  early exits; step 10.1 verifies both scoping records, both outputs against the brief-output floor,
  and prevented conclusions for every thin, negative, or unresolved finding; step 10.4 reports the
  depth each lens ran at; the `Verify` block now opens "Both lenses ran." The publishable-limitations
  list trades "unresolved applicability" for "trigger evidence too thin to resolve." The worker-topology
  rule now forbids letting a thin scoping record stand in for an unrun lens, preserving the
  capacity-blocker force that previously forbade relabelling a lens `inapplicable`.
- **One guard added:** the conclusion status `inapplicable` survives — it is a finding about the
  reviewed system — but now says so explicitly, so it cannot be read as resurrecting the removed lens
  branch.

### Trial evidence transfer

The five trials' evidence largely transfers: every trial ran both lenses, so the lens-execution,
reconciliation, and result paths are heavily trialled, and what the decision removes is a branch no
trial ever took. Fixes 1–12 and R1–R4 are unaffected — none of them depended on the gate.

**Genuinely new and untrialled: the proportionate-depth rule.** The re-run of the sequentialthinking
trial should specifically exercise:

1. **The brief-output floor** — does a degenerate memory finding still come back with inventory,
   finding, and prevented conclusions, or does "brief" collapse into a stub?
2. **Whether depth is set honestly** — with no gate to exit through, does a thin case get a genuinely
   proportionate pass, or does the worker pad it to look like a full one?
3. **Step 7's bounded invocation** — the invoked epistemic procedure now runs on every system,
   including one whose epistemic content is thin. Does passing the scoping record actually bound its
   effort, and do the wrapper rules survive the bounded mode intact?
4. **The repurposed direct-adaptation exception** — it now scopes objects rather than gating; the
   re-run should show whether an executor still routes such a route to the runtime account.
5. **Cost** — every run now invokes the external procedure. The re-run is the first measurement of
   what the unconditional invocation costs on a thin subject.

## Validation re-run — `sequentialthinking` against the mandatory-lens candidate

Run 2026-08-21; artifacts in `trials/sequentialthinking-rerun/`.

**The proportionate-depth rule works, and the evidence is differentiated rather than merely absent of
complaint.** The worker judged the memory lens **brief** and the epistemic lens **full** *on the same
subject* — the discrimination the rule exists to produce. Its reasoning for brief: a full pass "would
have produced eight rows of 'none, see line number'." For full: a warrant claim sitting next to zero
evaluators needs the route ledger, not a bounded confirmation. Neither output was stubbed nor padded,
and the run produced a sharper headline finding than the pre-change run on the same subject. The five
flagged re-run questions are answered affirmatively, except cost, which the run does not isolate.

**The R4 correction branch was named the instruction's strongest mechanism** (F10). Both lens workers
found the orchestrator's prepared packet defective in ways it had not seen, and the branch routed both
without improvisation. The case that matters: the orchestrator had registered the tool description as
"54 lines of instruction addressed to the model in the second person" — misclassified by the very
criterion its own record stated, and left standing it would have licensed the conclusion that the
description cannot mislead, because directives have no truth value. It is roughly half third-person
assertion, and the assertive half carries the run's headline finding. The "misclassified by its own
stated criterion" clause is what made the orchestrator accept the correction instead of dismissing it
as emphasis. That clause earned its place; it is not to be trimmed.

### Applied

- **Direct-adaptation seam decided (F1).** This collision was introduced by the mandatory-lens change:
  step 5's exception withheld non-truth-apt adaptation routes from the epistemic lens, while the
  invoked procedure has an explicit `non-truth-apt policy/content update` class and instructs the
  analyst to classify every content-changing edge it meets. Resolved in favour of **handing the route
  over tagged classify-only** — the option the worker improvised — because withholding leaves a silent
  hole in the invoked procedure's ledger rather than keeping the analysis clean. Classify-only is
  defined in the text: recorded in its content/update classification, *not* analysed for warrant,
  transformation, or acceptance. A lens concluding the route is truth-apt after all must return that as
  a correction under step 3's correction branch, never as silent scope expansion — which composes the
  seam with the mechanism the same trial identified as strongest. Step 7.2's pass-list now carries the
  classify-only routes explicitly.
- **The `implemented` collision removed structurally, not warned about (F7).** The re-run called it
  "the one rule whose violation would be silent and fatal, defended only by executor discipline," and
  the one place an unassisted run would fail quietly. A warning is the weakest instrument against a
  silent failure, so this instruction's conclusion status **`implemented` is renamed `afforded`**
  ("inspected code affords it, without proving deployment"). The invoked instruction's vocabulary is
  promoted and accepted; ours is the one free to move, and moving it now is free where moving it after
  promotion would not be. The step-3 bullet now states the avoidance is deliberate rather than asking
  the executor to hold two same-named fields apart, and step 7.3 says the two sets share no value, so a
  return needing both simply carries both. Step 5's memory paragraph updated to `claimed`/`afforded`/
  `observed`. The five trials' artifacts use the old term; they are evidence about the instruction, not
  artifacts that must match its wording.
- **Forward dependency in the result order (F2, third clause).** Not a reorder: record 2's tier is
  judged over the runtime baseline that record 5 carries, and the reader needs the tier up front where
  it bounds everything after it. Step 9 now states that the required order is the reading order, not
  the writing order, and that record 2 is written after step 4.

### Recorded, not applied

The re-run's remaining friction is logged for acceptance rather than patched: F3 (whether "consume only
the prepared packet" forbids reading the invoked method document — the worker read "only" as
constraining evidence sources and authorized the one file), F4 (nothing bounds absence-register
inflation except the implicit rule that an absence must bound a conclusion; making it explicit would
help), F5 (how to fill a crossing loop's fields without over-reaching on a `complete artifact, partial
loop` boundary), F6 ("generic identity, form, substrate" undefined), F9 (run-ID format, now four
trials deep), F12 (the fuzzy line between 7.1's "do not restate the method" and 7.4's interface
enumeration), and F14 (whether the frozen packet is immutable for the run or amendable as corrections
arrive — the apparatus race that raised it caused no harm, but a rule either way removes the check).

### Escalated upstream, out of scope here

The re-run found a defect in the *invoked* instruction (F11): Branch 2's closing "Then stop" would
literally have discarded this artifact's only real truth-apt edges, and the worker had to override the
text to reach the right answer. That instruction is promoted and accepted, so the repair is separate
work; it is recorded with its evidence in the workshop README's pending handoffs.

## Apparatus notes

- A usage limit interrupted three trials mid-run and killed both GBrain lens workers after they had
  completed. Fractal resumed from disk with no work redone; Swamp lost both lens workers and used the
  instruction's sequential fallback, so that run did not achieve fresh-context lens isolation
  (recorded as its limitation 9); GBrain's lens outputs were recovered from transcript and written to
  disk, so its lens files are recovered rather than worker-written. This is harness apparatus, but it
  produced the live evidence behind fix 4.
- The Fractal executor's Write tool refused to create the result file under the name `analysis.md`
  ("Subagents should return findings as text, not write report files") and succeeded with `result.md`
  via shell. Not an instruction defect, but a live hazard for any promoted skill whose deliverable is
  a sub-agent-written artifact.
- No trial mutated a checkout, wrote outside its trial directory, or opened prior KB coverage of its
  system. The cold constraint held.
