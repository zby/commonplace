# Desloppify: reading for the code-quality scope question

Source: `https://github.com/peteromallet/desloppify` at commit
`3a7735d531a96b6a226bfbdc9fd662b14195f857` (2026-05-13), cloned to the
untracked `related-systems/peteromallet--desloppify`. Read on 2026-11-16:
the README, `docs/SKILL.md`, `docs/scoring.md`, `docs/CLAUDE.md`,
`dev/DEVELOPMENT_PHILOSOPHY.md`, `dev/QUEUE_LIFECYCLE.md`,
`dev/review/README.md`, the shared review prompt and rubrics in
`desloppify/languages/_framework/review_data/dimensions.json`, and selected
modules named below. Most of the 1,460 Python files were not read. Nothing was
run. Paths below are relative to the clone.

## What it is

A Python command-line tool that an AI coding agent runs against a codebase. It
finds quality problems, keeps them in local state under `.desloppify/`, and
hands the agent one item at a time until a score reaches a target. Its authors
say the primary user is the agent, not a person.

One cycle has six phases, and the queue enforces their order:

`scan → review → workflow → triage → execute → scan`

- **Scan.** Deterministic detectors per language: unused code, duplication,
  complexity, coupling, test coverage gaps, security. Each reports checks made
  and failures found.
- **Review.** Subagents score twelve subjective dimensions from 0 to 100 and
  return findings as JSON. The tool imports the JSON and rejects it if it does
  not match the schema.
- **Triage.** Six stages (observe, reflect, organize, enrich, sense-check,
  commit) turn the findings into clusters and an ordered queue. Each stage
  takes a written report from the agent.
- **Execute.** `desloppify next` shows one queued item with its file and the
  command that resolves it. The agent fixes it, resolves it, and asks again.
- **Rescan.** Checks the result and starts the next cycle.

## Mechanisms worth naming

**A rubric with exclusions.** Each subjective dimension has a description, a
`look_for` list and a `skip` list. For naming, `skip` includes "a name used
50+ times is a convention, not an outlier". The exclusions say when a
construction that looks like the defect is not one.

**Observe, then judge.** The review prompt has two phases. The reviewer first
collects observations for every dimension, including positive ones, and is
told not to score. Then it writes a characterization, then a rationale, and
sets the number last. A finding must name a file and a concrete change.
Positive observations may not be reported as findings.

**Signals guide, they do not count as evidence.** Detector output aggregated
per file becomes a "concern": a summary, the signals and a question for the
reviewer (`desloppify/engine/_concerns/`). The prompt says these are
navigation aids, not confirmed issues and not inputs to the score. A dismissed
concern is stored by fingerprint and not raised again.

**Persistent characteristics.** The reviewer maintains a list of what the
codebase is like on each dimension, including deliberate tradeoffs and
positive patterns, with a `settled` flag. Later reviews receive the list and
may amend it.

**Blind review.** The reviewing subagents get a packet with no score history
and no target, and no conversation context.

**Declined work stays visible.** Marking an item `wontfix` removes it from the
default score but not from the strict score. The gap is the accepted debt, and
the agent is told to maximise the strict score.

**Detector silence does not close an item.** A queued item is completed only
by an explicit resolve, skip or reopen. A scan that stops reporting it can
corroborate a resolution but not make one.

**Tiers by kind of work.** T1 automatic fix, T2 quick manual fix, T3 judgment
call, T4 major refactor.

**Symmetric challenge, for the project's own pull requests.** Under
`dev/review/`, each proposed accept gets a challenger whose default is no, and
each proposed reject gets an advocate whose default is yes. A third stage
reads both files and decides. This is how the maintainers process
contributions; it is not part of the shipped tool.

## The score, and what the code shows about it

The overall score is 25% mechanical and 75% subjective. The authors call the
score the point of the tool and its honesty the thing they care about most.
They list four defences. The code shows less than the documents claim for two
of them:

- **Attestation on resolve.** `desloppify/app/commands/helpers/attestation.py`
  accepts an attestation when it contains the substrings "i have actually" and
  "not gaming". It checks wording, not work.
- **Reset of scores that land near the target.** `docs/SKILL.md` says
  target-matching scores trigger an automatic reset. In
  `desloppify/engine/_scoring/state_integration_subjective.py` the policy
  function returns the assessments unchanged with status `disabled`. Its
  docstring says blind packets made false positives more likely than gaming.

So the working defences are the blind packet and the strict score. Three
quarters of the number is a model's holistic judgment. The repository gives no
measurement of how stable that judgment is across repeated reviews, or of how
well a rising score tracks a codebase that engineers find better. The README
states the correlation as a hope ("should correlate").

## Comparison with the Commonplace improvement procedures

Both systems have the same parts: deterministic checks, model review against
stated criteria, typed findings, a plan chosen from the findings, edits, and
stale results after the edits.

| | Desloppify | Commonplace (ADRs 132 to 135) |
|---|---|---|
| Unit of work | whole codebase, state across sessions | one note per run |
| Goal | a number to raise | no number; a plan of edit operations |
| Who orders the work | a six-stage triage that clusters findings across files | an assessor that picks operations in depth order for one note |
| Human decision | none required inside the loop | two stops: per-item answers, and approval of the exact final text |
| Check after an edit | tests, then a rescan | none in the run; the next sweep refreshes stale results |
| Declined work | `wontfix`, counted in the strict score | a strike with the operator's required reason (ADR 130) |
| Evidence the method works | none in the repository | single runs; controlled testing is a separate workshop |

The largest difference follows from the material. Code has an executable
check that an edit kept behaviour, so desloppify lets the agent run
unattended and verifies afterwards. A text has no such check, so Commonplace
puts the operator before publication. This is the main reason the text runner
would not carry over to code unchanged.

## Candidate transfers to the text procedures

Each is a candidate for the workshop that owns the matter. None is adopted.

1. **Exclusion lists per criterion.** The `skip` lists do the job of the
   "contrastive preservation examples" entry of 2026-11-16 in
   [decision-lifecycle-evidence](https://github.com/zby/commonplace/blob/142bff37aeaf7728a0c5cf9f3cd1c225598ba565/kb/work/decision-lifecycle-evidence/README.md#use-existing-decisions-to-calibrate-existing-operations):
   they tell the reviewer when a suspicious construction carries meaning. The
   form is cheap: a short list beside the criterion, grown from rejected
   findings. Deferred; not commissioned.
2. **Dismissal by fingerprint.** A finding the operator struck should not
   return on the next sweep in the same form. Desloppify fingerprints the
   concern type, file and signal keys. Whether Commonplace review results
   already suppress a struck finding after the note changes was not checked.
   Deferred; not commissioned.
3. **Settled characteristics of the target.** A per-note or per-collection
   list of deliberate choices that reviewers receive, so they stop
   re-reporting them. This overlaps with the cleared candidates retained under
   ADR 132. It also costs context on every review and can go stale. Treat as a
   question, not a proposal. Deferred; not commissioned.
4. **Clustering findings across targets by root cause.** Commonplace plans one
   note at a time. A defect repeated across many notes usually has one cause
   in a type spec, an instruction or a skill. Desloppify's triage looks for
   that before any fix. The existing instruction
   [review design pressure behind recurring errors](../../instructions/review-design-pressure-behind-recurring-errors.md)
   addresses the same thing by hand. Owner: open.
5. **Symmetric challenge.** Review a proposed accept and a proposed reject
   with opposite defaults. It bears on the proposed-fix check and on the
   stability question in
   [stochastic-operation-testing](../stochastic-operation-testing/README.md).
   It doubles launches. Owner: stochastic-operation-testing, as a variant to
   compare if a comparison is commissioned.
6. **Declined work stays counted.** Commonplace already keeps a strike with
   its reason. What it lacks is any view of accumulated strikes per criterion.
   A count per criterion would show which criteria the operator overrides
   most, which is calibration evidence. The
   [authority-grades proposal](../../reference/proposals/authority-grades-and-learning-from-operator-decisions.md)
   may already cover this; check before adding anything. Owner: that proposal.

## What not to take

- **A single score as the goal.** The tool's own history shows the problem:
  one defence is a phrase match and another was switched off. An agent told to
  raise a number that a model assigns has a direct route to raising it without
  improving the text. Commonplace's stops put the judgment with the operator
  instead. Nothing read here is a reason to change that.
- **"Don't substitute your own analysis."** The skill tells the agent to
  follow the queue and not reason about the scan itself. That fits an
  unattended loop over thousands of findings. It conflicts with the
  Commonplace rule that an author fixes only what the executor cannot
  determine.
- **Per-agent overlay documents.** Fourteen near-copies of the skill, one per
  coding agent, are maintained under both `docs/` and `desloppify/data/global/`.

## For the scope question

Desloppify is evidence that general code quality is a large, separately
maintained product: 29 languages, plugin detectors, autofixers and a queue
with its own lifecycle. A project that wants it can install it. Its language
plugins list no Markdown or prompt language, and no detector read here treats
an instruction file as a caller or a contract. If that holds, a function whose
only caller is a skill would look unused to it. This is an inference from the
plugin list, not an observed result. That gap is where position C in the
[framing](./README.md) sits. Whether it produces false findings on this
repository is what the proposed probe would show.
