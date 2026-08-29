# Operationalize shared doctrine and intent in agent delegation

## Commission

The operator asked on 2026-08-29 for Commonplace's operational machinery to be
revised around a sharper reconstruction of *Auftragstaktik*: shared doctrine
makes concise delegation intelligible, while task-specific intent makes it
adaptive. Apply that reconstruction to this plan as well as to the machinery
the plan governs.

The intended end state is that an agent can issue a compact task as a delta
from a known Commonplace operating methodology. The executor can distinguish
what it inherits, what it must preserve, what it is authorized to decide from
execution-time evidence, and what is an actual gap. Concision is a consequence
of that shared basis, not an acceptance criterion.

This plan is written the way it asks packets to be written. It fixes outcomes,
invariants, priorities, and return triggers. Its routes, orderings inside an
outcome, and wording are defaults. When evidence makes a prescribed route
unsuitable, adapt the route, record the deviation in this file, and continue.
Return for direction only on the triggers listed under "Authority".

## What this pass changes, and what it must not undo

Two earlier passes already reshaped this machinery. Commit `d8eb9d86` rebuilt
the delegated-authoring surfaces around three roles. Commit `1cff50ea` moved
instruction precision from method preselection to purpose, authority,
interfaces, acceptance, and consequential failure handling; its report
([instruction machinery refinement](../../reports/planning-delegation-theory/instruction-machinery-refinement.md))
records which surfaces were deliberately kept exact and which redesigns were
deferred. Those dispositions are the starting state, not open questions.
Reopen one only for a named fault. A preference for shorter text is not a
fault.

What is new here is one idea. Shared doctrine is interpretive machinery, not
only a store of omitted defaults. The earlier passes let a packet omit what
the executor can *recover*. This pass lets a packet omit what the executor can
*derive* from shared doctrine plus task intent, and it requires the executor
to tell both apart from a real gap. Every step below serves that change. A
step that does not make an executor better at classifying an omission, or an
author better at deciding what to omit, is out of scope.

## Starting artifacts

This plan is a delta from the current Commonplace operating system. An
implementer reads the live versions of these artifacts rather than treating
the summaries here as replacements:

- [Shared operating substrate for agent work](./shared-operating-substrate.md)
  is the draft skeleton for outcome 1. It distinguishes weight-resident
  repertoire, methodology, doctrine, institutional memory, task commission,
  and execution evidence. It is a composition of existing notes, not a
  separate gate; outcome 1 says how to use it.
- [Planning and delegation: source-grounded evaluation](../../reports/planning-delegation-theory/source-grounded-evaluation.md)
  separates source doctrine, shared mechanisms, and Commonplace consequences.
- [Intent-framed instruction machinery refinement](../../reports/planning-delegation-theory/instruction-machinery-refinement.md)
  records the first operational sweep and the exact controls it deliberately
  retained.
- [Intent-framed delegation is a control regime, not a short prompt](../../notes/intent-framed-delegation-is-a-control-regime-not-a-short-prompt.md)
  owns the existing delegation boundary.
- [An author should fix what the executor cannot determine, not what it will](../../notes/fix-what-the-executor-cant-determine-not-what-it-will.md)
  owns the current allocation rule.
- [Weight-resident methodologies provide context-efficient behavioral compression](../../notes/weight-resident-methodologies-compress-behavior-in-context.md)
  owns the distinction between a compact parametric cue and an explicit,
  inspectable methodology.
- `AGENTS.md` is the primary always-loaded delegation doctrine for this
  checkout, and `AGENTS.md.template` ships that baseline to new projects.
  Collection and type contracts specialize authoring, an invoked skill adds
  workflow-specific controls, and the worker commission supplies the
  task-specific delta. A lower layer may rely on an upper one only when the
  worker's actual consumption path supplies it with binding force.

The working model is:

```text
shared operating doctrine
        + task-specific intent
        + binding constraints and commitments
        + authorized execution-time evidence
        + executor judgment
        -> acceptable locally selected means
```

Shared doctrine is not merely a store of omitted answers. It can supply known
defaults, but its more important role is to supply a common way to interpret
the task and derive means. Intent supplies the task-local criterion for judging
those means. Some omitted details are therefore inherited, some are deliberately
left for execution, and some are harmlessly irrelevant. An omission that fits
none of those classes is an underspecification defect.

## Priorities when requirements conflict

This plan contains requirements that pull against each other. Resolve a
conflict in this order. A lower item never overrides a higher one.

1. **Correctness controls.** Exact commands, parser grammars, source identity,
   isolation boundaries, write ownership, collision avoidance, digests, drift
   guards, transaction boundaries, and rollback rules. Never traded for
   anything below.
2. **Behavioral fidelity on the real consumption path.** A fresh worker, given
   only what it actually receives, acts correctly. This is the acceptance test
   for every change.
3. **Interpretive clarity.** The worker can classify each unstated choice as
   inherited, delegated, irrelevant, or a gap. This is the purpose of the work.
4. **Less duplicated doctrine.** Removing repeated text is the means, and only
   where items 2 and 3 survive the removal.
5. **Brevity.** A side effect. Never by itself a reason to change anything.

The error costs are asymmetric, and that asymmetry decides every close call. A
packet that is explicit where it could have inherited costs context. A packet
that inherits where the baseline is not actually delivered fails silently
inside a worker, often behind a plausible result. The burden of proof therefore
sits on compression: keep the explicit form until the consumption path has
been exercised, and when evidence is inconclusive, keep the explicit form.

Known tensions and their resolution:

- *No new universal checklist* versus the eight-item brief in outcome 3 and
  the six-item record in outcome 4. The eight items are an author's
  classification lens: a brief includes an item only when the baseline cannot
  determine it for this task. The six items are a workshop audit record, not a
  packet format. Neither becomes a required template, field list, or schema.
- *No new code or schema fields* versus *codify a rule that is repeatedly
  missed*. Codification is a response to evidence from outcome 5 only. Write
  it as a proposal in `kb/reference/proposals/` unless the change is trivially
  small and its deterministic consumer already exists.
- *Theory settles first* versus *the whole premise depends on a runtime
  fact*. Whether a worker receives `AGENTS.md` with binding force is an
  empirical question about each harness, and it is cheap to test. Test it
  first (step 0). Theory does not depend on the answer; outcomes 2–4 do.
- *Simplify the multistage skill* versus *its forward test passed*. The
  skill's states, digests, invalidation map, and promotion reference are
  correctness controls (item 1). Simplification targets its common-path
  delegation prose and any remaining preselection of worker means, not its
  control structure.
- *Produce a durable synthesis note* versus *three existing notes already own
  most of this ground*. Default to revising the existing notes and adding at
  most one new note that owns the omission classes. A second new note needs
  its own argument that no existing note can carry.
- *Use Auftragstaktik as an anchor* versus *import no military machinery*.
  The name appears in no operative instruction unless outcome 5 has shown the
  bare cue reliable for that model and context. Until then it is an example
  inside theory notes, always with a neutral gloss.

## Invariants

- Keep the source methodology, the transferable mechanism, and the
  Commonplace consequence separate. Do not attribute the resulting agent
  method to a military source.
- Do not rely on the parent conversation as shared doctrine. A worker may
  inherit system instructions, repository contracts, a skill, or an explicit
  packet only when its real consumption path establishes that inheritance.
- Do not treat trust, rank, force structure, synchronization doctrine,
  military risk doctrine, professional culture, or adversarial tempo as agent
  requirements merely because a source doctrine contains them.
- State a baseline or an omission class only where the executor could
  otherwise make a consequentially different interpretation.

## Authority

The operator has fixed the central mechanism, the machinery scope, and the
priorities above. The implementing agent may choose exact wording, note
decomposition, audit order, route adaptations, and local simplifications from
the evidence it finds, and records each route deviation here. Return for
direction if the evidence would require abandoning the central mechanism,
choosing between incompatible control-plane architectures, expanding
authority, or weakening a load-bearing safety protocol. Step 0 finding that
the primary delegation runtime does not deliver the baseline is an
architecture choice: return with the finding and the candidate delivery paths
rather than picking one.

## Sequence

Steps have real dependencies; the work inside each is left to its owner.

One step was taken out of order on 2026-08-29 because its leverage is
highest: the `AGENTS.md` and `AGENTS.md.template` Delegation section now
declares the file as the Commonplace doctrine, states the handoff-as-delta rule
with its consumption-path condition, and gives the four omission cases. That
is the `AGENTS.md` part of outcome 2, landed before outcomes 1 and 2 proper.
It does not change the dependencies: step 0 still decides whether workers
receive that file, and outcome 2 still owns how the collection and instruction
contracts specialize it. The term is *Commonplace doctrine*, defined in
`kb/reference/definitions/commonplace-doctrine.md` and entered in the
`AGENTS.md` vocabulary.

- **Step 0 — probe baseline delivery.** Discriminating evidence for
  outcomes 2–4.
- **Outcome 1 — durable theory.** Must settle before it binds contracts.
- **Outcome 2 — shared delegation doctrine.** Contracts must settle before
  common rules are removed from task packets.
- **Outcome 3 — multistage pilot**, comparing the current and revised skill
  on the same scenarios.
- **Checkpoint.** Report step 0 results, the theory and contract changes,
  and the pilot result. Wait for the operator before outcome 4: it is a batch
  change across many surfaces, and the operator gates batch changes.
- **Outcome 4 — audit every commissioning surface.** Adopts the pilot's
  compression only where the same consumption path holds.
- **Outcome 5 — cue and packet evaluation.** Bounded; may close with a
  recorded deferral.

### Step 0. Probe baseline delivery

Operator-supplied fact (2026-08-29): the Codex harness delivers `AGENTS.md`
as the first message to every worker it spawns. For harness-spawned
sub-agents, delivery is therefore established as standing instruction; record
it as such and do not spend a probe on it.

For every other path through which this checkout actually delegates — at
least the hermetic review-prompt path, whose jobs run through the CLI rather
than a sub-agent spawn, and any other harness in use — determine whether a
fresh worker receives the `AGENTS.md` delegation doctrine with binding force,
and how: system-instruction load, explicit packet, or not at all. Read the
harness documentation, then confirm with a probe worker asked to quote the
delegation paragraph and say where it came from. Record the result per
runtime in this file.

Where delivery is absent or unverifiable, the Commonplace doctrine for that
runtime is whatever the packet explicitly carries. Compression there is off
the table until the delivery path is repaired, and the repair is a separate,
reviewable change.

#### Step 0 findings (2026-08-29)

- **Codex harness-spawned workers — verified ambient delivery.** A fresh worker
  launched with parent-turn inheritance disabled received the root `AGENTS.md`
  as an ambient repository instruction. It quoted the Delegation paragraph
  without opening a file and distinguished that instruction from its compact
  task packet. The injected repository instruction remains context supplied by
  the harness; no parent task narrative is part of the inherited baseline.
- **Hermetic review workers — the Codex result applies; this is not a second
  runtime.** Live review documentation and source show that Commonplace's CLI
  creates prompts and finalizes outputs but never launches a model. The parent
  dispatches each generated prompt through the current harness's fresh-worker
  surface. A Codex review worker therefore receives the same ambient
  `AGENTS.md`; the generated prompt stays the complete task-specific review
  commission. This corrects step 0's earlier premise that review jobs run
  through the CLI instead of a sub-agent spawn.
- **Claude Code workers — documented delivery, probe unverified.** This
  checkout's `CLAUDE.md` is a symlink to `AGENTS.md`, and the installed Claude
  Code CLI documents project-file auto-discovery as the default (its bare mode
  explicitly disables that discovery). A fresh no-tools probe ended at its
  cost cap before returning a quote, so direct binding-force evidence was not
  obtained. Treat Claude Code packets as self-contained and do not compress
  them against the Commonplace doctrine until a successful fresh-worker probe
  establishes delivery.
- **No package-owned model runtime.** The review package exposes deterministic
  selection, prompt creation, and finalization seams only. Repository tests
  reject operative instructions that launch `claude` or `codex` subprocesses.
  No additional delegation runtime needs a separate baseline in this pass.

Route deviation: step 0 named the hermetic review-prompt path as a non-spawn
runtime. The live architecture disproves that classification, so the probe was
applied to its actual harness-spawned consumption path instead.

## Required outcomes

### 1. Establish the durable theory

Revise the planning-and-delegation synthesis so it no longer reduces safe
omission to recoverability from doctrine. Revise the existing delegation,
determinability, and weight-resident-methodology notes where the new
distinctions would otherwise leave them contradictory or misleading, and add
at most one new note that owns these distinctions:

- shared doctrine can both recover defaults and guide generation of previously
  undecided means;
- intent supplies the task-specific purpose and success criterion when the
  prescribed task or anticipated route no longer fits;
- binding constraints and coordination commitments limit acceptable
  adaptation;
- execution-time evidence selects among or helps construct permitted means;
- an executor must recognize when neither inheritance nor authorized judgment
  closes a gap; and
- concise tasking is an effect of shared interpretive machinery, not evidence
  that the control relation is adequate.

Use the substrate draft as the skeleton, under these rules:

- **Map onto existing vocabulary; do not add a layer ontology.** The
  doctrine/methodology split is the KB's system-definition versus knowledge
  artifact distinction (`kb/notes/definitions/behavioral-authority.md` and its
  two families): force comes from the consumption path, not from the content.
  The five-layer stack is the composition diagram already in
  `borrowing-can-operate-through-retained-artifacts-or-weight-activation.md`
  plus execution-time evidence from the delegation notes. "Evidence is not a
  standing prescription until adopted" is
  `commitment-not-derivation-creates-new-ground-truth.md`. "Explicit even when
  the model knows it" is the independent-role list in
  `design-rationale-must-preserve-unregenerable-decision-premises.md` and the
  heuristic/authority-bearing split in
  `system-definition-artifacts-are-crystallized-reasoning-under-context.md`.
  Frontloaded restatement is fine in the workshop draft, which now carries
  provenance links at each passage; the durable note cites these rather than
  restating them under new names.
- **The term is resolved** (2026-08-29): *Commonplace doctrine* is the
  technical compound, defined in
  `kb/reference/definitions/commonplace-doctrine.md` as the standing
  instruction a worker inherits with binding force when its runtime loads it
  — a natural-language system-definition artifact, not a new class. Bare
  *doctrine* stays ordinary English and abbreviates the compound only where
  source-side military doctrine (MCDP 1, ADRP 6-0) could not be meant.
  `AGENTS.md` carries the vocabulary entry and its Delegation section uses
  the term.
- **Fold, do not spawn.** The draft's "selections and binding restatements,
  not only departures" point already existed in
  `specific-intent-may-out-yield-local-rationales-facts-stay-separate.md`
  (arbitrary conventions) and
  `fix-what-the-executor-cant-determine-not-what-it-will.md`
  (coordination-bearing selection); the borrowing note's composition diagram
  now cross-links them (2026-08-29). The draft's independent-role list merges
  those unrecoverable cases with the recoverable-but-role-bearing exceptions
  in the design-rationale note; keep the two apart. What remains new — the
  four omission classes, and concise tasking as an effect of shared
  interpretive machinery rather than evidence of an adequate control
  relation — folds into the delegation notes, or earns one new note if no
  existing note can carry the omission-class argument.
- **Use the classification table as a test, not as the deliverable.** The
  outcome's acceptance below is reader-testable; classifying representative
  artifacts consistently is a check on the way, not the finish.
- **Route the draft's open questions** rather than settling them by
  vocabulary: Q3 (actual inheritance) is step 0; Q4 (doctrine boundary) is
  settled by the mapping above; Q5 (standing authority) and Q6 (change
  propagation) go to outcome 2; Q1, Q2, and Q7 (supported interpreter,
  activation evidence, model drift) are evaluation conditions for outcome 5.

Ground source-side claims about doctrine, shared understanding, training, and
commander's intent from the retained MCDP 1, ADRP 6-0, and Stahel materials
through `cp-skill-ground`. Keep the stronger agent-side formulation visibly
marked as Commonplace synthesis. Scope claims; do not write "never", "only",
or "every" where the evidence supports "where" or "when".

Acceptance: a reader can explain why reconstructing a hidden complete plan is
not the same as intent-preserving adaptation, and can identify the separate
functions of doctrine, intent, constraints, and local evidence.

#### Outcome 1 result (2026-08-29)

The substrate draft was consumed into the existing theory owners rather than
promoted as a layer ontology. The omission classes and the distinction between
recovering an inherited answer and generating a new intent-preserving means now
live in the delegation and determinability notes; the weight-resident note
separates parametric repertoire from authority-bearing Commonplace doctrine.
The source-grounded synthesis report carries the same distinction while keeping
the military source claims separate from the Commonplace construction. No new
note was needed.

Grounding through `cp-skill-ground` added one minimum MCDP extract for
preparation, competence, and shared understanding and two ADRP extracts for
shared understanding, clear intent, adaptation, and training. The retained
Stahel extracts already supported the historical boundary, so that route
returned `quotes sufficient`. The workshop draft remains only as working state
until final closure.

### 2. Change the shared delegation doctrine

`AGENTS.md` and `AGENTS.md.template` already state the delegation baseline
(commits `59304ba6`, `530c01e9`): the file is the Commonplace doctrine a
worker inherits when its runtime loads it, a handoff is a delta from it, and a
worker classifies an unstated choice as inherited, delegated, irrelevant, or a
gap. What remains is to make the shared authoring contracts say how
instructions specialize that doctrine — what a consequential handoff can
inherit and what must remain task-specific — without restating it. Inspect at
least these live surfaces and their composition siblings:

- this checkout's `AGENTS.md` Delegation section and vocabulary entry, as the
  text the contracts specialize (re-edit only if a contract needs it);
- `kb/instructions/COLLECTION.md`;
- `kb/types/instruction.md`;
- `kb/instructions/write-instruction.md`;
- `kb/work/COLLECTION.md` and `kb/messages/README.md`, whose workshop and
  mailbox handoffs specialize the Commonplace doctrine;
- `kb/reference/control-plane-goals.md`; and
- scaffold or conformance tests that consume the changed text.

The resulting contracts should establish these effects without requiring these
phrases or a new mandatory schema. The first, third, fourth, and fifth are now
stated in the `AGENTS.md` Delegation section; the contracts specialize them for
their artifacts rather than repeat them:

- An instruction is context-complete relative to its declared consumption
  path. It may rely on verified always-loaded doctrine, but not on
  accidental conversational history or an unverified link chase.
- The task carries its particular purpose or desired effect. Naming an output
  alone is insufficient when different valid-looking outputs could serve
  different purposes.
- A handoff states deviations from inherited doctrine and consequential open
  choices. It need not restate generic rules already supplied with binding
  force by the Commonplace doctrine.
- The executor can tell whether an unstated choice is governed by an inherited
  default, deliberately delegated to its judgment, irrelevant to acceptance,
  or unresolved.
- Shared doctrine does not silently grant authority. Task authority,
  task-specific constraints, external commitments, owned mutations, and
  acceptance remain explicit where the doctrine cannot determine them.

Two failure modes the contract must name:

- **Change propagation.** Once packets omit a rule because the doctrine
  supplies it, editing the doctrine silently re-commissions every worker that
  relied on the omission. The contract says how that reliance is recorded or
  found — the mechanism is the source-side lineage rule in
  `artifacts-produced-from-sources-need-lineage-recorded-at-the-source.md` —
  or states that the risk is accepted for a named class of rules. Do not add
  machinery for it here; record the decision.
- **Standing authority.** Say which ownership, integration, and recovery
  defaults are stable enough to inherit and which must remain task-specific.
  A default that changes with the task is not doctrine.

Acceptance: a fresh agent receiving the doctrine its runtime actually delivers
and the task delta can act without the parent conversation, preserve the purpose, and
identify both its discretion and its stop condition. Test this with a probe
worker on the runtime step 0 confirmed, not by reading the text.

#### Outcome 2 result (2026-08-29)

The root `AGENTS.md` and scaffold template already carried the stable standing
defaults and needed no edit. The instruction collection and type now define
context completeness relative to a verified consumption path and treat a
worker packet as a task-specific delta from the Commonplace doctrine on that
path. The writing instruction applies the inherited, delegated, irrelevant, or
gap classification when drafting and testing a packet. Workshop commissions
specialize the same rule. Mailbox requests remain conservative because they may
cross sessions and harnesses: without a named verified recipient path, they
must carry every relied-on rule.

Standing doctrine keeps delegation inside existing authority, leaves
scheduling, integration, and recovery with the parent, and grants no nested
delegation authority by silence. Purpose, task authority and commitments,
owned mutations, acceptance, and return conditions remain task-specific; any
transfer of a standing responsibility is also explicit. Commonplace accepts a
searchable broad dependency cohort for universal root, collection, and type
rules rather than adding per-packet fields. A change to one of those rules
reopens the commissioning cohort before packets may omit the changed rule;
narrower methodology dependencies continue to use source-side lineage.

A fresh Codex worker received `AGENTS.md` through the step 0 delivery path. It
correctly inherited the parent recovery default while keeping sole file
ownership task-specific, classified the open analytical method as deliberately
delegated, and limited its evidence to the stated purpose, acceptance, inputs,
and produced observations. It rejected a bare output-only mailbox request as
incomplete and said an unverified recipient path must frontload the rule or
return control. The full probe commission was sufficient without repeating
the inherited default. Scaffold and instruction-safety tests passed (20 tests).

### 3. Use the multistage writer as the first operative pilot

Simplify `cp-skill-write-multistage` by treating the shared Commonplace
authoring and delegation contracts as doctrine and each worker commission as a
task-specific delta. Preserve the epistemic and mutation invariants that made
the current workflow pass its forward test:

- source-only reconstruction remains isolated from the incumbent;
- consolidated authorship remains responsible for claim selection and prose;
- an independent reviewer judges exact candidate bytes;
- evidence changes invalidate dependent stages;
- the parent alone owns live-target mutation, integration, recovery, and
  user-owned decisions; and
- accepted digests, drift checks, the one-repair boundary, validation, and
  rollback remain exact.

Within those invariants, let each role choose its investigative,
representational, and prose means. Prefer a brief that identifies, where the
baseline cannot determine them, the inherited contracts, the commissioned
contribution, task-specific intent, evidence boundary, exceptions, owned
output, acceptance condition, and return triggers. Remove repeated generic
delegation prose only when the worker demonstrably receives the rule from the
Commonplace doctrine (step 0).

Judge simplification by behavioral fidelity and by operational and
interpretive complexity on the actual consumption path: states, branches,
handoffs, exceptions, duplicated authority, implicit inheritance, and
unresolved choices. Add complexity only for a named failure mode, interface,
or coordination dependency, and normally match it by removing or consolidating
complexity elsewhere on that path. Treat words or tokens only as proxies for
context exposure. A shorter skill that hides an inherited rule is a
regression.

Acceptance: run two scenarios against both the current skill and the revised
skill — the existing drift/evidence/repair forward scenario, and one in which
the prescribed intermediate route becomes unsuitable while the commissioned
contribution remains achievable. The revised skill must match the current one
on every invariant and must not do worse on adaptation: the worker adapts its
means, preserves the contribution and evidence boundaries, and returns control
rather than inventing authority. Inspect the traces, not only the final
artifacts. If the revised skill loses on either scenario, keep the current
skill and record why; that result still counts as a completed pilot.

### 4. Audit every surface that commissions another agent

After the checkpoint, inventory instructions, skills, generated prompts,
templates, and code that produce plans or commands for another agent. Freeze
the cohort against a named commit and recorded repository searches; surfaces
added after that baseline are follow-up work unless they invalidate the shared
doctrine. Include:

- source ingestion and grounding handoffs;
- external-literature and agentic-system analysis;
- note revision, warning fixes, compression, and full-pass work;
- review-job dispatch and generated hermetic review prompts;
- memory-system review drafting;
- the experimental AutoReason workflow; and
- examples or gates that prescribe a fresh independent worker.

For each real commissioning surface, record:

1. what baseline the worker actually receives and with what force;
2. the task-specific intent and acceptance condition;
3. choices inherited from doctrine;
4. choices deliberately delegated to execution evidence;
5. exact controls retained because failure would be consequential; and
6. apparent omissions that neither doctrine nor authorized judgment can close.

Classify rather than automatically rewrite. The default disposition is
*retain exact*; the refinement report's kept-exact and deferred lists start in
that disposition. Source ingestion already carries task-specific intent as a
declared, optional `occasion` that governs only the report's selection
sections (landed 2026-08-29 in `cp-skill-ingest`, `draft-ingest-report.md`,
and the ingest-report type); record its disposition, do not redesign it. Remove duplicated doctrine only where step 0 showed the
shared path reliable for that surface's runtime. Add intent where a plausible
output could satisfy the literal task while defeating its purpose. Keep
self-contained hermetic packets where the worker does not receive a dependable
common baseline. Leave versioned experimental protocols unchanged unless the
audit finds a concrete fault that their own evaluation and recovery rules can
test.

Acceptance: every inventoried surface has a retained disposition — revise,
retain exact, defer behind evidence, or not a commissioning surface — and
every revision names the consumption path that makes its omission safe.

### 5. Evaluate the cue and packet policy, and expand only on evidence

This outcome decides two things: whether *Auftragstaktik* may be used as a
bounded mnemonic on any operative surface, and whether the packet policy
landed in outcomes 3–4 generalizes to tasks outside the pilot. It does not
reopen those outcomes.

Before the first run, fix and record in this file a finite evaluation
boundary: held-out task set, runtime and model partitions, repetition count,
and decision rule. Record as conditions of the result, not as settled facts:
which interpreter the recovery baseline assumes (weakest supported model,
each partition, or the current selection); what evidence licenses relying on
a named methodology without a gloss; and what provider-model change triggers
re-evaluation. Use tasks that require execution-time adaptation, not tasks
whose method is already mechanically determined. Compare at least:

1. the revised doctrine-plus-task-delta packet as landed;
2. the same packet with an explicit neutral intent-preserving delegation
   gloss; and
3. the same gloss with *Auftragstaktik* as a recognition anchor.

Retain the pre-pilot explicit packet as a control where the pilot's own
comparison did not already cover the task. A bare-name arm may be added as a
diagnostic; it never becomes the operative default merely because it is
shorter. Assess preservation of intent, respect for constraints and authority,
correct use of local evidence, recognition of insufficiency, unnecessary
military imports, and integration quality. Inspect execution traces as well as
final artifacts when route violations can be hidden by a plausible result.

Default on inconclusive evidence: neutral gloss, no name on operative
surfaces, packet policy as landed. If the available runtimes cannot support
the comparison, close this outcome with a recorded deferral that names the
missing capability and the decision it would change. A deferral is a scoped
decision, not a failure.

Use the results as signposts:

- If the Commonplace doctrine is not reliably present in a runtime, keep the packet
  explicit there or repair the delivery path before compressing it.
- If the name imports irrelevant military machinery or varies materially by
  model, retain the neutral mechanism and use the name only as an example.
- If the name plus boundary improves coherent adaptation without contamination,
  it may be used as a bounded mnemonic; record the supported model and context
  boundary.
- If a supposedly inherited rule is repeatedly missed, make it explicit at
  the task surface, strengthen its routing, or propose codifying it. Do not
  explain the failure away as insufficient trust.
- If an implementation detail recurs with stable inputs, promote it into the
  shared doctrine or deterministic machinery. If evidence keeps changing the
  right answer, leave it with the authorized executor.

## Drift checks

Stop and re-read "Priorities when requirements conflict" if any of these is
true:

- You are writing a packet template, a required field list, or a schema.
- A skill got shorter and you cannot name, for each removed rule, the artifact
  that now supplies it and the path by which the worker loads it.
- You are editing a surface the refinement report kept exact or deferred, and
  you have not named the fault.
- The theory note restates the three existing notes instead of adding the
  omission classes.
- You are defining layers or classes that the artifact-analysis vocabulary
  (behavioral authority, system-definition and knowledge artifacts,
  representational form) already names.
- An evaluation is being designed whose every possible result leads to the
  same decision.
- You are accepting a compression because a worker produced a plausible
  result, without inspecting whether it followed the route.
- You are returning for direction on a route choice this plan leaves to you,
  or deciding an authority question this plan reserves.
- Changes from more than one outcome are uncommitted at once.

## Integration and recovery

Land step 0's findings, theory, shared contracts, the multistage pilot, and
later audit cohorts as separately reviewable commits. Keep `AGENTS.md` and
`AGENTS.md.template` consistent when the framework invariant changes. For each
promoted skill, edit the canonical source and verify its installed projection
or scaffold path only as required by the manifest.

Before removing repeated text, identify the artifact that now supplies its
force and exercise that consumption path in a fresh context. If the revised
path fails, restore the last accepted wording for that cohort and retain the
failure as evaluation evidence. Do not continue a broad compression sweep
after its shared-doctrine premise has failed.

For each cohort, record which operational or interpretive complexity was
added, removed, or consolidated and which consequential interpretations remain
open. Record common-path words or tokens only as secondary context-exposure
evidence.

Use `commonplace-validate` for changed KB artifacts, the relevant scaffold and
instruction tests for control-plane changes, and `git diff --check`. Run the
full Python suite only when code, fixtures, package behavior, or broad shared
templates make it proportionate.

## Non-goals

- importing mission-command doctrine as Commonplace's organizational model;
- treating every omission as recoverable from a pre-existing answer;
- making *Auftragstaktik* a required keyword in any plan or worker packet;
- optimizing prompt length independently of behavioral fidelity;
- designing one universal plan or delegation schema;
- re-deciding dispositions the refinement report already recorded, absent a
  named fault; or
- revising unrelated planning, review, or orchestration machinery merely
  because it contains detailed steps.

## Closure

This workshop closes when:

1. baseline delivery is recorded per runtime, with the delivery path named or
   its absence recorded;
2. the durable theory distinguishes inherited doctrine, intent-guided
   generation, and accidental gaps, and the substrate draft has been consumed
   into it;
3. the live instruction doctrine makes task packets relative to a verified
   Commonplace doctrine;
4. the multistage pilot has a recorded result — revised skill adopted, or
   current skill kept with the reason — without loss of its epistemic or
   recovery invariants;
5. every identified commissioning surface has a disposition;
6. the cue and packet evaluation has produced a scoped operational decision,
   which may be a recorded deferral;
7. changed artifacts and their real consumption paths validate; and
8. durable notes, instructions, reference updates, decisions, and evaluation
   reports have been extracted, after which this workshop and its active-list
   entry are removed.
