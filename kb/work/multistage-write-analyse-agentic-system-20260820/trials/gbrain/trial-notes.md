# Trial notes — cold run of `analyse-agentic-system` on GBrain

**Trial apparatus. Not part of the instruction's own logical result.**

Run: `RUN-GBRAIN-20260820`. Candidate: `../../candidate.md`.
Executed 2026-08-20 against `related-systems/gbrain` @ `9a0bae8`.

---

## A. Lens-applicability reasoning (recorded here as requested; the formal records are in `lens-dispositions.md`)

**Memory/context — applicable.** The trigger is "a path by which material accumulated or changed
through use can affect a later invocation or action." GBrain met it on several independent,
implemented paths, so no judgement call was needed on the headline case: conversation-derived facts
are pushed into `_meta.brain_hot_memory` on every MCP tool response; the dream cycle writes durable
pages and takes that later retrieval selects; the calibration profile — built from *graded past
claims* — is spliced into a later `think` prompt.

One genuine boundary case: **the 43 shipped skills**. As distributed they are static shipped
material, which the instruction explicitly excludes as a trigger. But SkillOpt mutates SKILL.md
bodies using measured scores from prior runs, and the mutated file is then loaded into a later
session's prompt. I judged the *SkillOpt-mutated* skill a read-back path and the *as-shipped* skill
retained-static, and asked the lens worker to keep the two apart. The instruction gives no rule for
an artifact that changes category depending on whether an optimizer has touched it; I had to invent
the split. See friction F9.

**Epistemic — applicable.** Two independent sufficient triggers. (1) Material routes handle truth-apt
content: the repository itself calls `takes` "the epistemological layer", storing WHO believes WHAT
with a confidence weight; `grade_takes` runs a judge model over unresolved claims; the contradiction
eval hunts conflicts. (2) The system makes a consequential knowledge-production claim in its own
README ("Search finds the pages. The brain reads them for you and writes the answer"), with gap
analysis named as the differentiator. Either alone would have triggered the lens.

The **direct-adaptation exception** did real work here. GBrain contains several evaluated adaptation
loops with no truth-apt object: lease-cap control, backoff/jitter, quiet-hours deferral, RSS
watchdog drain, search-mode knob resolution. I set those aside into the runtime account rather than
letting them inflate the epistemic route ledger. Because another trigger made the lens applicable,
I asked the worker to fold in only the set-aside routes that actually feed an epistemic one (query
cache reuse changes what evidence a `think` call sees).

---

## B. Friction points

Recorded in the order they were hit. "Friction" = ambiguous, impossible, or forced improvisation.

### F1. No ID allocation scheme (step 1.1)
"Allocate one run/result ID before any analysis" — the instruction never says what a run ID looks
like or where uniqueness is checked. I minted `RUN-GBRAIN-20260820`. Two runs against the same
system on the same day would collide, and step 10.1's "unique, resolving IDs" check cannot catch a
collision because there is no registry to check against.

### F2. "Evidence layer" is per-source, but a source checkout is not homogeneous (step 2.3)
The register asks one `evidence layer` per `SRC-*` record, from a five-value list. A repository
checkout carries `implementation` in `src/` and `doctrine/design` in `docs/` and `README.md`, and
`README.md` alone carries both `doctrine/design` and `reported operation`. I split the register by
file rather than by source-of-record and let two rows carry two layers. That is a reasonable
reading, but it means "one source register" and "per-source evidence layer" pull against each other
for any repo-shaped source, which is the common case.

### F3. `CLM-*` ownership is split in a way that breaks when the epistemic lens does not run (step 3 table)
The table says `CLM-*` is the "Orchestrator namespace" but that "Epistemic lens owns truth, scope,
and warrant fields." The orchestrator cannot pre-allocate claim IDs without already knowing the
claims, and if the epistemic lens exits `inapplicable` nobody owns the fields at all. I resolved it
by letting the lens worker number `CLM-01…` in its own return and registering those numbers on
receipt. That works only because the lens ran.

### F4. `BAP-*` depends on a definition a cold executor may not be able to open (step 3)
"Behavioral authority: one consumption path's consumer, channel, and force — **the cited definition
fixes these three parts**". No definition is cited in the instruction body; the only pointer is a
footer link (`kb/notes/definitions/behavioral-authority.md`) that the footer itself frames as
grounding, and which this trial forbade me to read. I applied consumer/channel/force from the
instruction's own sentence plus the run-level `horizon`. If the external definition draws those
three lines differently, every `BAP-*` record in this run is mis-specified and I would have no way
to know. This is the sharpest dependency-on-absent-context in the instruction.

### F5. The materiality test is defined for surfaces and reused for loops (steps 4.2 and 4.4)
Step 4.2 says "A loop is material under the same test step 4.4 applies to other surfaces." Step 4.4's
test ("alters the analysis question, a control path, evidence strength, or a lens result") is
workable for loops, but the instruction never says what delimits *one loop* from *two*. GBrain's
subagent loop has two implementations behind a feature flag; the dream cycle has 22 phases, several
of which contain their own inner iteration. I recorded six loops and stated the materiality of each,
but a different executor could defensibly record four or fifteen.

### F6. Step 4.2's ten-field record is itself close to the "fixed template" step 4.4 forbids
Step 4.4 says "Do not turn this inventory into a universal taxonomy, fixed template, maturity ladder,
ranking, or adoption advice." Step 4.2 hands down a fixed ten-field record for every material loop.
I read the prohibition as scoped to the *conditional* surfaces of 4.4, not to the mandatory loop
record — but the two paragraphs sit adjacent and the tension is visible on a first read.

### F7. Logical-record order in step 9 inverts the production order
Required order puts "shared component/object/route/claim/authority records" (record 4) before the
"runtime account" (record 5). But step 3 assigns the runtime owner the generic identity of `CMP-*`,
`OBJ-*`, and `RTE-*`. In practice I had to build the runtime account and the shared registers
together and then present them in the mandated order. Not a defect — but a cold executor following
the steps strictly in sequence will find that step 3 asks for a register it cannot populate until
step 4 is done, and step 2.4 ("the canonical records registered so far") already anticipates this
without resolving it.

### F8. Step 10.3's validation instruction is unexecutable without an authorized target
"Run the deterministic validation required by the chosen existing target contract. Until a dedicated
result contract exists, use applicable generic validation plus the semantic checklist above." With
no authorized target (this run, by construction), there is no contract to name a validator. I ran
the semantic checklist and the step-10.1 structural checks by hand and recorded the result. I did
**not** run `commonplace-validate`: the trial forbids modifying anything outside the trial directory,
and I could not confirm from inside the trial's read constraints which generic validation would even
apply to a workshop-staged result. Recorded as a limitation rather than silently skipped.

### F9. Static-vs-accumulated is not decidable per artifact type (step 5, memory trigger)
Covered in §A. The instruction's exclusion ("Static shipped material (documentation, tool
specifications, installed skills) … are retained state, not read-back") is stated per *kind of
artifact*, but SkillOpt makes "installed skill" a category that can move. The rule needs a
per-instance test, not a per-kind list.

### F10. Physical layout is deliberately unspecified, and that cost real time (step 9 preamble)
"this instruction deliberately does not fix the physical layout, which remains under trial." I chose
five files (`evidence-packet.md`, `runtime-account.md`, `lens-dispositions.md`, `lens-memory.md`,
`lens-epistemic.md`) plus a `result.md` carrying records 1–4 and 8–11 and indexing the rest. The
eleven logical records survive the split, but I had to invent a cross-file ID-resolution convention
(all IDs live in `evidence-packet.md` §6; every other file cites, none redefines) to satisfy step
9's "IDs resolvable across all physical parts". That convention is not in the instruction and a
different executor would invent a different one.

### F11. "One frozen revision" vs a genuinely two-layer subject
The boundary GBrain presents is whole-system for the repository but subsystem-only for the
*advertised* agent loop: README's "signal → search → respond → write" loop runs in the host agent
platform (OpenClaw/Hermes/Claude Code), which is not in the checkout. Step 1.4 permits a
subsystem-only boundary "named as such", which I did — but step 1.3's function-based inclusion test
("components or actors whose scheduling … produce or constrain the behavior under review") arguably
*requires* including the host platform, which is unreachable. The instruction has no vocabulary for
"the system under review defines a loop whose other half ships separately." I named it as a boundary
limitation and bounded the conclusions.

### F12. No guidance on how much of a very large subject to line-read
744 source files, 1,244 test files. Step 2.4's "prepare the evidence packet once" and step 4's
"for each material loop" give no stopping rule. I line-read the loop-defining files and inventoried
the rest, marking `uninspected` where I did. That is defensible but the depth choice was entirely
mine, and the resulting `code-grounded` tier rests on a sample I selected.

### F13. A lens correcting an already-registered record is a case the instruction does not cover
Step 3's ownership table says lenses "extend by ID" and that "No lens may rename or independently
re-inventory a registered object or route." It says nothing about what happens when a lens inspects a
registered record and finds it **factually wrong**. The memory lens opened its report with a §0
headed "one packet correction" and returned three: the packet's "43 skills" (53 directories, 51
`SKILL.md` files); a stale `skills/manifest.json` (50 skills at version 0.32.3.0 against `VERSION`
0.42.25.0); and the fact that `facts`, `takes`, and `query_cache` are defined in `migrate.ts`'s
`MIGRATIONS` array, not in `schema.sql` as the packet's anchoring implied.

None of those is a rename or a re-inventory, and all three are better-grounded than what the packet
said — the packet's figure came from `README.md`, the correction came from the tree. But the
instruction gives no verb for it. "Extend by ID" does not obviously license *replacing* a field. I
applied them centrally as corrections to the registered records (`result.md` §4.4) and preserved the
documentary disagreement as conflict C1, on the reading that step 8.1's conflict-preservation rule
governs *evidence conflicts between anchored sources*, while a lens finding that the orchestrator
mis-transcribed a source is a different thing — a correction, not a conflict. That reading is mine;
the instruction does not supply it.

The gap matters more than it looks. The orchestrator prepares the packet once, before any lens
inspects anything, so the packet is exactly where under-inspected assertions accumulate — and it is
the one artifact every lens is told to treat as given.

### F14. The instruction guarantees ID collisions between parallel lenses and gives no scheme
Step 3 puts every namespace under orchestrator ownership and says "Any new material record returns to
the orchestrator for one canonical ID." Step 3's worker topology then says to prefer *fresh worker
contexts*, which by construction cannot see each other's allocations. Both of mine returned
`PROPOSED-*` records, as instructed — and they collided three ways: with each other (memory's
`PROPOSED-OBJ-06` and epistemic's `PROPOSED-OBJ-21` are the same take-proposal row), with my own
post-freeze registrations (epistemic's `PROPOSED-SRC-19…43` against my `SRC-19…27`; my `RTE-21…23`
against epistemic's `PROPOSED-RTE-21…30`), and by re-proposing sources I already held
(`facts/decay.ts`, `operations.ts`).

Every collision was resolvable — that is what §4.2–4.7 of the result does — but resolving them was a
substantial, mechanical, error-prone pass with no guidance behind it. Three cheap fixes the
instruction could carry and does not: hand each worker a disjoint reserved block; require workers to
return proposals keyed by *identity* (file path, table name) rather than by invented ID; or state
that a proposal duplicating a registered identity must merge rather than take a new ID. I ended up
inventing the third rule mid-reconciliation.

Related and worth separating: because both lenses ran in parallel against a frozen packet, neither
could see that the other had found half of the same structural fact. That the two halves of the
calibration finding (§8.5 of the result) arrived independently is *evidentially valuable* — but it
was luck that I noticed they composed, not a step the instruction asks for. Step 8 tells me to merge
duplicates and preserve conflicts; it never tells me to look for independent convergence, which was
the single most informative thing in this run's reconciliation.

### F15. "Prefer fresh worker contexts" has an availability failure mode the instruction treats as binary
Step 3's topology rule is three-valued: fresh workers, else sequential in-context, else stop with a
capacity blocker. It assumes availability is known before dispatch. In this run both workers were
*available*, dispatched, and completed — and then the whole run, workers and orchestrator alike, was
killed by a usage limit before any lens output reached disk. That is neither "fresh workers
available" nor "unavailable"; it is a mid-flight capacity failure, and the instruction has no
disposition for it. Had the returned reports not been recoverable from the transcript, the correct
action under step 3 would have been to stop with a capacity blocker and discard a completed analysis.
See §C.7.

---

## C. Things I could not do

1. **No observed-run or causal evidence.** By trial constraint I never executed GBrain. Every
   activation, efficacy, and causal question is `uninspected`. This is the single largest limit on
   the run and it is recorded against each conclusion it prevents in `result.md` §10.
2. **No `commonplace-validate` run.** See F8.
3. **Could not verify the `behavioral-authority` definition.** See F4.
4. **Could not verify the sibling `gbrain-evals` repository.** README's benchmark figures (P@5 49.1%,
   R@5 97.9%, +31.4 P@5 over the graph-disabled variant) and the production corpus counts
   (146,646 pages, 100,720 takes, \$361.49 extraction run) live outside the boundary. All stay
   `claimed`. Prevents: any conclusion about retrieval quality or extraction quality.
5. **Did not line-read `src/core/operations.ts` (4,751 lines), `src/core/search/hybrid.ts` (1,870),
   `src/core/minions/queue.ts` beyond the claim/timeout paths, or any individual SKILL.md body.**
   Prevents: exhaustive claims about the operation contract, the exact ranking formula, and the
   instruction content of the skillpack.
6. **Did not open any prior Commonplace coverage of GBrain** (trial constraint). So this run cannot
   report whether its findings agree with, extend, or contradict earlier analysis — which is
   exactly what the cold trial is meant to leave open.

7. **Run interrupted by a usage limit; lens outputs recovered rather than worker-written.** Both lens
   workers completed their analyses and returned their reports, but the workers and this orchestrator
   were terminated by a usage limit before either report was written to disk. `lens-memory-context.md`
   and `lens-epistemic.md` were recovered verbatim from the returned reports and written by the
   orchestrator on resume; each carries a provenance note at its head. No content was added and no
   finding was altered, but the files are not worker-authored artifacts and should not be treated as
   such. This is recorded as limitation L16 in `result.md` §10, and the instruction-level gap it
   exposes is F15.

   Two knock-on effects on this trial's evidence about the *instruction*: the run's wall-clock and
   token cost is not a clean measurement of the candidate's cost, and the reconciliation pass
   (`result.md` §8) was executed on resume from the lens files rather than from live workers — so the
   option of sending a clarifying follow-up to a lens worker, which step 7.4's "affected work is
   rerun" clause implicitly assumes is available, was not exercised and could not be.
