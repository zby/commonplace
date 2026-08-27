# Trial notes — cold trial of `analyse-agentic-system` on Swamp

Trial apparatus. Not part of the instruction's logical result. Records friction
points, lens-applicability reasoning, and what could not be done.

Run: `AGS-2026-08-20-SWAMP-01`. Candidate:
`kb/work/analyse-agentic-system/candidate.md`.
Target: `github.com/swamp-club/swamp` at `cf38c4ec1068613bb7d3432eb74a1ad854156dd7`.

## Lens-applicability reasoning

**Memory/context — easy call, but only after one deliberate decision.** The
trigger is "material accumulated or changed through use can affect a later
invocation or action", and swamp has many such paths (versioned data read by
later runs, the audit JSONL, the skill-dir registry, the evaluated-definition
cache). The decision that took work was the *opposite* direction: swamp's most
conspicuous artifact — a ~1.1 MB bundled skill corpus written into agent skill
directories — is emphatically **not** a memory trigger, because the instruction's
definition classes static shipped material as retained state. The definition did
its job here: without it I would probably have run the memory lens over the skill
corpus and produced a category error. Worth noting that the instruction's
definition and the system's most salient feature point in opposite directions, so
this is a case where the wording is load-bearing rather than decorative.

**Epistemic — easy call.** Two independent triggers: material routes handle
truth-apt content (a stored `resource` asserts external state; two append-only
trails assert that an action occurred; reports derive propositions), and the
system makes consequential warrant claims ("accurate", "validate they are
correct", "proving which automation read which secret, when"). Either alone would
suffice. The "successful knowledge production is never a prerequisite" clause
mattered: swamp turns out to produce no knowledge inside its boundary — there is
no generative step in it at all — and without that clause I might have been
tempted to record `inapplicable` after discovering that, which would have thrown
away the run's most interesting finding.

**Direct-adaptation exception — checked, does not apply.** The closest candidate
is the permission grant and instruction installation, which change the external
model's behavior with no truth-apt object. But these are not *evaluated*
adaptations — nothing measures an outcome and adjusts — so the exception's trigger
conditions are false. They stayed in the runtime account and in the authority
ledger as non-truth-apt policy updates.

## Friction points

1. **Scope test is ambiguous for this system class (step 1.2).** The scope clause
   reads "a narrower system whose deployed behavior depends on model calls plus
   surrounding machinery". Swamp's deployed behavior contains *no* model call:
   it is pure deterministic machinery whose entire purpose is to be driven by a
   model that lives elsewhere. Read literally, that test excludes swamp. Read
   through the earlier phrase "agent operating layer", it clearly includes it. I
   followed the "agent operating layer" reading. This is a real gap: the
   scope test enumerates system kinds and then gives a dependency test that does
   not cover one of the enumerated kinds. A system that *serves* an agent rather
   than *being* one passes the enumeration and fails the test.

2. **The boundary rules do not say where to put an external model-calling actor.**
   Step 1.3 defines the boundary by function — "the components or actors whose …
   decisions produce or constrain the behavior under review" — and the harness's
   decisions plainly produce the behavior under review. But the harness is
   uninspectable here, so including it would make every conclusion `uninspected`.
   I named it an excluded external dependency and added an explicit "boundary
   consequence" paragraph saying the result is whole-system for swamp and partial
   for the composite loop. Step 1.4's subsystem-only rule is the nearest available
   instrument but does not quite fit: this is not a subsystem of swamp, it is a
   *peer* actor. A rule for "the model-calling actor is out of boundary" would
   have removed the improvisation.

3. **The runtime baseline's loop template assumes the loop is inside the system.**
   Step 4.2 asks for trigger/input, next-step owner, decision policy and its form,
   context selection, and so on, per material loop. For L1 (the agent/CLI loop)
   the next-step owner and the decision policy are both outside the boundary, so
   half the template resolves to `uninspected`. The template still earned its
   place — filling it is what made the split-loop structure explicit — but the
   fields want an explicit "owner is out of boundary" value rather than repeated
   `uninspected` prose.

4. **Fresh lens workers were terminated by an external usage limit.** Both lens
   workers (and two of three runtime fact-gatherers) died before reporting. Per
   step 3's worker-topology rule I fell back to executing both lenses sequentially
   in the orchestrator context against the same registers. The instruction handles
   this cleanly and the fallback is explicitly permitted, so this is a note about
   the run, not a defect in the instruction — but it does mean the run did not
   achieve fresh-context lens isolation, and I recorded that as limitation 9. One
   terminated worker's findings (state/action/data) were never received; I
   replaced them with direct orchestrator reads, which are thinner. One
   surviving worker's findings had already been folded into `canonical-records.md`
   before termination; I re-verified eight of its code anchors directly in the
   checkout afterwards rather than trusting anchors I could no longer see the
   source of.

5. **Ordering versus parallelism (steps 4→5→6/7).** The instruction is written as
   a strict sequence, and the evidence packet is described as containing "the
   canonical records registered so far", which suggests lenses may start before
   the runtime account is complete. I tried to parallelize by launching lens
   workers once the registers were populated but before the runtime account was
   written, and I think that was the right reading — but the phrase is doing a lot
   of quiet work and a reader could just as reasonably serialize everything. Worth
   deciding explicitly.

6. **Result-record 4 versus the physical-layout freedom (step 9).** Step 9 says
   the physical layout is deliberately unfixed but requires eleven logical records
   "in order". I split the result across three files (packet, canonical records,
   result) and satisfied records 3 and 4 by pointer. That is defensible and IDs
   resolve, but "in order" and "one file or a package" sit in mild tension: a
   reader following record order has to jump between files twice. The instruction
   might want to say whether pointer-satisfaction counts.

7. **No validation path exists, and the instruction anticipates this (step 10.3).**
   It says to use "applicable generic validation plus the semantic checklist"
   until a dedicated contract exists. In practice there was no applicable generic
   validation at all — the output carries no collection type and sits in the
   workshop layer — so the checklist was the entire verification. That is what
   step 10.3 intends, but "applicable generic validation" resolving to the empty
   set on the first real run is worth knowing.

8. **Minor: `CLM-*` ownership.** The record table says the orchestrator owns the
   `CLM-*` namespace and the epistemic lens owns truth, scope, and warrant fields.
   Registering claims *before* running the epistemic lens (which is what the
   evidence-packet flow requires) means the orchestrator must already decide what
   counts as a consequential claim — which is close to an epistemic judgement. It
   worked, but the ownership line is thinner than the table suggests.

## What worked well, briefly

- The conclusion-status vocabulary and the "never upgrade" list did real work:
  three times I caught myself about to write that swamp "checks" something when
  the code only conforms it, and once about to treat the audit trail as agent
  memory.
- The mandatory runtime baseline before lens applicability was the right order.
  Deciding applicability first would have been guesswork; after mapping the loops
  both dispositions were obvious.
- Forcing "prevented conclusion" onto every negative made the absences into the
  most informative part of the result (no automatic read-back to the agent; no
  correspondence check on stored resources; no conjecture inside the boundary).
- The prohibition on a system-wide epistemic grade was easy to honour and clearly
  right for this system, where checking quality varies sharply between
  `doctor audit` (strong) and `model validate` (over-worded).

## Could not do

- **Could not observe anything.** No run, no execution, no `.swamp/` artifacts
  anywhere in the checkout. Every lifecycle phase is `no instance observed`, and
  the run reaches at most `implemented`. Running the binary was outside the
  trial's read-only constraint and would have required a Deno toolchain and live
  external credentials.
- **Could not inspect the model-calling half** of the deployed system, so nothing
  about activation or causality is available.
- **Could not resolve two doc-versus-code conflicts** (skill version stamping;
  the "manual" approval label) without either running the system or reading
  beyond the frozen revision.
- **Could not use fresh-context lens workers** (friction 4).
- **Could not publish.** No authorized target contract existed for this run, so
  per step 9 the result is retained under the staging identity and the publication
  blocker is recorded as result record 11.
- **Did not read** any `kb/` file other than the candidate instruction and, once
  step 7 became applicable, `kb/instructions/analyse-external-system-epistemic-architecture.md`.
  No `kb/agentic-systems/`, `kb/agent-memory-systems/`, `kb/notes/`, or
  `kb/sources/` file was opened at any point, by me or by any worker (each worker
  prompt carried the prohibition explicitly). The checkout was never mutated and
  nothing was written outside this trial directory.
