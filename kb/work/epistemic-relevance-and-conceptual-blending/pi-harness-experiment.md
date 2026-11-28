# Pi-harness experiment: does project priority make an agent blend a second-guessed reading into its answer?

Status: design only, 2026-11-28, requested by the operator. Nothing here has been built or run. Running it needs separate authorization, as the [workshop README](./README.md) requires. This design narrows Experiment 1 of the [revised proposals](./experimental-proposals.md) to one runnable study and adds the requested-answer-form explanation from the [findings](./findings.md#4-competing-explanations-and-discriminators).

## The mistake this experiment tests

When an operator asks an agent a specific question, the agent often sees wider project goals in its context. Looking at the request through those goals, the agent may **second-guess** what the operator is really after — spotting a broader concern the operator might also care about.

Noticing a broader concern is not the mistake. There are two clean ways to handle it:

1. **Ask for clarification:** "Do you mean only the narrower problem, or also this broader goal?"
2. **Keep the two readings separate:** answer the literal request cleanly, then add an explicit branch — *"You could also mean X; in that case, consider B, which is a separate concern."*

The mistake is **silently blending the direct reading and the second-guessed reading into one account**. Instead of flagging the extra concern separately, the agent folds the solution to the second-guessed reading into the definition, steps, or scope of what the operator actually asked about.

This failure is subtle and easy to miss:

- Nothing looks fabricated or wildly off-topic.
- Both ideas are individually sensible and genuinely useful to the project.
- The resulting document reads smoothly, yet it is **imprecise**: it treats work that serves a different goal as if it were a way of solving the problem the operator asked about. A later reader who relies on the artifact inherits that blurred boundary.

### Concrete example

Suppose a team has a concept of **handoff readiness**: making a handoff usable by the designated crew for its assigned job.

- **Direct request:** "Write a guide on how to improve handoff readiness without prescribing every action. Explain what counts as progress."
- **Second-guessed reading:** The agent knows the project wants more value out of its handoffs, so it reads the practical concern behind the request as *"How can we get more use out of these handoffs overall?"* Adapting handoffs so additional crews can reuse them answers that broader question — even though it does nothing to fix a missing decision rule that blocks the designated crew today.
- **Clean response:** Explains what makes the handoff usable by the designated crew, and adds separately: *"If you also mean reuse by other crews, that is a different goal and calls for a different change."*
- **Blended response (the mistake):** Counts "serving additional crews" as a dimension or route to improving handoff readiness. Both goals survive in the text, but the document now gives an imprecise account of what fixes the assigned handoff.

### Motivating episode

A closely related error appeared in [O001](./o001-operationalization-exchange.md). The operator asked how a methodology could become more operational without becoming more constraining. Given the project's wider ambition, *"How else could we make this methodology more useful?"* was a plausible broader reading. Extending the method to cover more tasks answers that broader question, but it need not help an executor apply the method to the task already at hand.

In the first revised artifact (G02), the artifact treated an answer to the broader question as an answer to the narrower one: it counted "enlarging coverage" among operationalization moves, even while cautioning elsewhere that generalization and integration differ. Only the later repair (G04) separated them, treating generalization as a distinct question about which tasks to address. That record establishes the written inclusion; it does not show that the agent arrived there by second-guessing the operator.

### Experimental question

Does naming a secondary practice as a **project priority** lead an agent to fold that practice into its written account of the requested concept — presenting it as a way of achieving what the operator literally asked about, instead of omitting it, asking for clarification, or marking it as a separate concern?

Scope boundaries:

- **Not a test of helpfulness or anticipation.** Raising the broader concern explicitly in its own branch is scored as preserving the distinction, not as an error. Asking for clarification instead of writing the document is tracked as its own trial outcome (see [Outcomes](#outcomes)).
- **First authoring only.** The study tests whether project priority changes the written relation on first authoring. It does not reproduce O001's multi-turn correction sequence.
- **Observable relation, not hidden motive.** Second-guessing under project priorities is the motivating hypothesis, not something the artifact alone proves. The study measures the written relation and reader classifications; it does not assume the operator forgot anything or infer hidden motives or training causes.

## Why a harness and not a bare prompt

O001 occurred in agent work with three structural features: project priorities arrived through standing context, evidence sat in workspace files the agent had to read, and the output was a retained document written for later use.

This design keeps all three features in a minimal `pi` harness:

- The project priority sits in the system prompt.
- The conceptual evidence sits in workspace files the agent inspects with tools.
- The product is a Markdown document evaluated both directly and through a later reader.

Runs happen outside the Commonplace checkout with no Commonplace `AGENTS.md`, skills, or vocabulary loaded. Otherwise this KB's own warnings about conceptual blending would act as an uncontrolled intervention.

## Materials: concept worlds

Each test world is a small fictional team workspace of six to eight Markdown files. To keep the design general, call the requested concept **A** (like handoff readiness above) and the two tempting secondary practices **B** and **C** (like adapting handoffs for additional crews, or adapting them for additional jobs).

### Main-world contents

Every main world specifies:

- **Primary concept A:** introduced by a source document and case records. The process description must establish what counts as progress on A, not merely list examples.
- **Two secondary practices, B and C:** for each, the world author writes down a plausible second-guessed reading behind the operator's literal request and why the operator might care about its answer. Each practice must answer that broader reading without, by itself, making progress on A. Sharing an object or occurring in the same workflow is not enough.
- **Bidirectional dissociating cases:** case records showing `A without B`, `B without A`, `A without C`, and `C without A`. The records do not flag the dissociation; the agent must notice it while reading. Because `A without B` only excludes B as a *requirement* (not as an optional route), the process description must also fix A's scope so B does not count as progress on A.
- **Invented names for A, B, and C:** prevents the model from falling back on pre-existing dictionary definitions.

For each world, write down the literal operator request, the plausible broader reading, and the evidence fixing A's scope. Hold all three constant across priority assignments.

### Constituent control variant

Each world also has a control variant where one secondary practice genuinely *is* a constituent of A: the source document says so, and no dissociating case exists. Without this control, an agent that blindly separates every concept would score perfectly.

### Validation before freezing worlds

Before any authoring trials run, check every world in two ways:

1. **Two-stage human plausibility check (without priority).**
   - *Unprompted stage:* Give a human reviewer only what the authoring agent would see without the priority paragraph (the task request and workspace files — no truth table, no held-out cases, and without naming B or C). Ask: *"What else, if anything, might this operator reasonably be asking for? What wording or project fact suggests it?"* Record the answer before revealing anything else.
   - *Prompted stage:* Next, show the process description, truth table, and held-out cases (still without the priority paragraph). Ask what B and C would achieve under the broader reading and whether either would advance A if the task stayed fixed. Keep unprompted readings and once-suggested readings recorded separately: both are useful observations, but they are different evidence. Reject a world if the connection to B or C only becomes intelligible after the reviewer is told which practice the project favors.
2. **Model solvability check.** Separately verify that a model can recover the stipulated boundaries from the workspace files when asked directly.

Repair or drop worlds that fail either check, then freeze the materials.

## Manipulations

### 1. Project priority (main factor)

The project brief includes one priority paragraph that names one secondary practice (B or C) as **this quarter's funded priority** and the other as a **routine maintained capability**.

- Swap which practice is funded while keeping the wording identical.
- Independently vary clause order so each practice appears first once and second once for each funding assignment. Balance order within each world, framing, and model.
- Include a **baseline** with the priority paragraph omitted.

Comparing the two practices *within the same document*, then averaging across both funding assignments and both clause orders, holds the author, task, and evidence constant without confounding funding with a practice's name or first-mention position.

### 2. Task framing

Each world runs under three versions of the operator request:

- **Neutral:** the world's frozen literal request, for example: *"Write `docs/<A>.md` for the handoff team. How could we improve A without prescribing every action? Explain what would count as progress."* Never mention B, C, or the broader reading.
- **Unified:** the neutral request plus *"Give one unified account that shows how A fits the team's work."* Tests whether asking for one unified account amplifies silent blending.
- **Audience specified:** the neutral request plus *"Write for an external reviewer deciding whether a case counts as A."* Narrows the document's intended use without telling the author how A and B relate.

A prompt explicitly stating that priorities do not change the definition would test a remedy rather than a framing condition; it is excluded here.

## Procedure

Each trial consists of three separate, non-interactive `pi` calls:

1. **Authoring.** The agent runs in a fresh copy of the workspace with file tools and writes `docs/<A>.md`. The project brief arrives via the system prompt. Save the full session trace. If the agent asks a clarifying question and stops without writing `docs/<A>.md`, log that outcome directly and skip Stages 2 and 3.
2. **Reader probe.** Freeze a copy of the authored `docs/<A>.md` before running either probe. A fresh run with no tools and no brief receives only that frozen copy and eight held-out cases. It classifies each case as `A` or `not A` with a one-line reason. The reader model is fixed across all conditions.
3. **Author probe.** A fork of the authoring session receives the same eight cases. Because `--fork` preserves conversation history rather than workspace files, the separate frozen copy from Stage 2 is what protects the scored document from any file changes during the probe.

Sketch of the authoring call:

```bash
cd "$RUN/workspace" && pi -p --mode json \
  --no-context-files --no-skills --no-extensions --no-mcp --no-prompt-templates \
  --append-system-prompt "$RUN/brief.md" \
  --model "$MODEL" --thinking "$LEVEL" --session-dir "$RUN/sessions" \
  "$(cat "$RUN/task.txt")" > "$RUN/authoring.jsonl"
```

- `--no-context-files` stops `pi` from loading any `AGENTS.md` or `CLAUDE.md`, including global and ancestor files.
- `--append-system-prompt` delivers the brief so every trial sees it; `pi`'s default coding-agent system prompt stays in place as a recorded constant.
- The reader probe uses `--no-tools` and attaches the two files with `@`.
- The author probe uses `--fork`.

**Preflight before the pilot:** run a canary check confirming that the brief is present in context and that no other context file is loaded. Record the `pi` version, model identifiers, thinking levels, and dates.

## Outcomes

### Primary: what relation did the document assert?

A blinded scorer sees `docs/<A>.md` without its brief, task variant, or funding assignment. (If the document itself quotes or mentions the priority, record that disclosure rather than claiming complete blinding.)

For each secondary practice (B and C), the scorer quotes the wording that locates the practice relative to A (including its heading if needed) and assigns one of five labels:

| Label | Meaning | Example (handoff world) |
|---|---|---|
| **Omission** | Practice is not mentioned. | No mention of other crews. |
| **Separate concern / alternative reading** | Mentions the practice, but explicitly separates it from A as a different goal or possible reading. | *"If you also mean reuse by other crews, consider B."* |
| **Substitution** | Answers the broader question instead of A without making a clear claim about A. | Discusses wider reuse throughout without saying what makes the assigned handoff ready. |
| **Explicit inclusion (false inclusion in main worlds)** | Presents the practice as a step, route to progress, or dimension of A. | *"One way to improve handoff readiness is adapting it for other crews."* (Counts as inclusion even if never called a "step.") |
| **Unclear** | Wording is genuinely ambiguous about the relation. | Blended phrasing that does not clearly assert or deny inclusion. |

Scoring rules:

- Compare labels against the frozen world specification.
- **Mixed answers (disclaimer plus inclusion):** if a document explicitly says a practice is a separate goal or concern, yet elsewhere counts it as a criterion, step, or route to progress on A, quote *both* passages and score **explicit inclusion**. A disclaimer does not cancel an operative inclusion claim.
- **Clarification-only responses:** if an agent replies with a clarifying question and stops without writing `docs/<A>.md`, record that run as a **distinct trial outcome** (alongside any other non-file stops). Do not fold it into *omission* or *separate concern*, and do not pass it to the reader probe; report clarification-only rates separately per cell.
- In main worlds, score explicit inclusion as **false inclusion**. Keep all authored documents in the prose-relation denominator (including omissions), and report unclear labels, mention rates, and clarification-only stops separately.
- **Primary estimate:** prioritized minus non-prioritized false-inclusion rate under neutral framing. Compute paired within-document differences and average within each world before comparing across worlds.
- In constituent controls, report **correct inclusion**, **explicit false separation**, and **silence** separately.

### Secondary: which decisions did a reader get wrong?

Freeze eight held-out cases covering the combinations of A, B, and C.

- For each practice X, report both error directions: rejecting `A without X`, and accepting `X without A`.
- Score classifications against the frozen truth table, not the prose label.
- Cross-tabulate reader decisions against asserted prose relations. A wrong "optional route" claim can coexist with 8/8 correct classifications — that is a detected relation error with no observed classification cost on these cases.

### Diagnostic context (not causal proof)

- **Author probe:** report alongside the reader probe, not as a diagnosis of internal state. The author retains the full workspace and brief while the reader has only `docs/<A>.md`. A correct author and mistaken reader establish disagreement under different information, not that the author "knew the distinction all along."
- **File access:** report which case files the author opened as a measure of access, not proof of what the author noticed.

## Predictions

| Result in the main worlds | Interpretation |
|---|---|
| More false inclusions for the funded practice under neutral framing | Supports a priority effect on silent blending into the written relation |
| Paired difference is larger under unified than neutral framing | Requesting one unified account may amplify the priority effect; compare differences directly |
| Unified framing increases false inclusions equally for both practices | Evidence for a framing effect without a differential funding effect |
| Specifying the external audience reduces the paired difference | Consistent with task interpretation contributing; not a unique diagnosis |
| False inclusions also occur without a priority brief | Priority is not necessary for the error; the baseline alone does not identify its cause |
| Wrong assertions, correct reader decisions | Silent blending occurs, but these held-out cases show no classification cost |
| No wrong assertions despite calibrated scoring | This setting did not elicit the target error |

Two bounds on interpretation: a small paired difference with a narrow interval around zero weakens the priority hypothesis *for this setting*, not for long, open-ended work with real concepts; and a positive result does not establish a training cause.

## Size, pilot, and stop rules

### 1. Calibrate before authoring

Hand-write three otherwise identical explanations of one main world:

- **Clean branch:** keeps B separate as an answer to the broader question (*"If you also mean..."*).
- **Clean inclusion:** blends B into A as a way to improve A.
- **Mixed answer (modeled on G02):** explicitly states that wider reuse (B) is a separate goal, yet later counts "number of crews served" (B) as a readiness criterion for A.

Run the blinded rubric and the reader probe on all three:

- The rubric must distinguish the clean branch from both the clean inclusion and the mixed answer from quoted evidence. On the mixed answer, the scorer must quote *both* passages (the disclaimer and the criterion) and score the criterion as **explicit inclusion** — the disclaimer does not cancel it. If the rubric fails on any of the three documents, repair it and recalibrate before freezing it.
- Correct reader classifications on these documents are still compatible with successful calibration (since an optional-route blend need not break binary classification).
- Also check two edge documents — one making B explicitly *necessary* for A, one making B *sufficient* for A — to confirm the reader probe returns the expected classifications under a literal reading of the held-out cases. Record the reader's actual answers even if it compensates for faulty prose.

### 2. Pilot

- **Design:** 3 worlds, 1 model, 1 completion per cell.
- **Cells:** each of the 3 framings × 2 funding assignments × 2 clause orders, plus the no-paragraph baseline and constituent controls under neutral framing.
- **Goal:** verify the pipeline and inspect the distributions of relation labels and reader errors separately.
- **Unit of analysis:** the **world** — neither eight case classifications nor repeated completions give eight independent worlds.

### 3. Proposed full run

- **Design:** 12 fresh worlds, the same conditions, and 2–3 current checkpoints at one fixed thinking level each. Add a second thinking level on one model for a within-checkpoint compute comparison. Model choice remains an operator decision.
- **Freeze rule:** after the pilot, freeze the full-run world count, repetitions, control schedule, and interval method before collecting full-run data. Report estimates by model with uncertainty across worlds.

### 4. Stop and escalation rules

- **Floor rule:** if no main-world pilot document falsely asserts inclusion after rubric calibration, increase difficulty once by adding case records and spreading the dissociating cases across more files, then repeat the solvability check. If the relation-error floor remains, report it and stop. Zero reader errors alone do not trigger this rule.
- **Control rule:** if constituent controls systematically elicit false separation, inspect the stipulated constituent and its evidence before proceeding. Record repairs and recheck controls separately from the full run.
- **Retention rule:** retain calibration, pilot, and full-run results separately, including null results and failed checks.

## Known limits

- **Fictional concepts:** clean labels remove prior knowledge, but they also remove the familiar vocabulary that may have contributed to O001. A later variant can use real but obscure concepts with independently adjudicated relations.
- **Confounded payoff vs. compliance:** the priority paragraph changes stated project payoff; it cannot separate practical payoff from a tendency to please the brief's author.
- **Single reader model:** the reader probe measures the document's effect on one reader model; another reader may be more or less charitable.
- **Probe reactivity:** eliciting classifications is itself an intervention, so the author probe always runs on a fork after the document is frozen and is reported separately.
- **Authoring bias in test worlds:** using an LLM to draft worlds could bake the tested bias into the materials. The frozen truth table, solvability check, control variants, and human review of every world before the freeze are the guards.

## Deferred

- **Common-mechanism family (Q001):** testing whether an agent merges two separate mechanisms into one requires a held-out case where the separate mechanisms and the proposed single mechanism predict different outcomes. Binary `A` / `not A` classification does not test that claim; defer until such a case is available.
- **Follow-on experiments:** correction versus fresh restart (Experiment 2), remedy comparison (Experiment 3), checkpoint lineage (Experiment 4), and handoff propagation (Experiment 5) remain in the [revised proposals](./experimental-proposals.md). Experiment 2 becomes worth running only if this study produces enough natural false inclusions to correct.

## Retained outputs

The harness, generated worlds, and raw traces live in the external experiment directory. This workshop receives a summary containing: the frozen design, exact prompts, model and `pi` versions, scoring rubric, calibration results, counts per cell, quoted evidence for relation labels, reader and author decisions, exclusions, and interpretation against the predictions table above.
