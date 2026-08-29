# Provider treatment of operator-communication failures — 2026-08-29

This frozen report records why Commonplace kept local operator-communication
controls even though major model providers already treat clear user-facing
communication as a general requirement. It preserves the evidence available on
2026-08-29 for later evaluation of those controls. It does not establish a new
methodology rule; the operative rule and skill are linked below.

## Result

The problem was not simply omitted by the providers. Anthropic and OpenAI both
state that answers should be clear, direct, and calibrated to the reader. Both
also give developers controls for response length and style. Anthropic's current
Claude Fable 5 guide goes further: it explicitly describes agents carrying
working shorthand and unseen context into a final answer, and tells them to
reintroduce or discard vocabulary that the reader did not share.

That provider recognition does not make the Commonplace controls redundant.
Provider guidance supplies a broad default. It cannot know which terms have
canonical definitions in this project, which terms an agent coined during one
task, or when a technical finding should remain intact as evidence while a
separate explanation serves an operator. Provider documents also describe
intended or steerable behavior, not a guarantee that every model and harness
will produce it throughout a long run.

The local intervention therefore addresses two different needs:

- The always-loaded rule states the project's ordinary communication contract.
- The optional skill performs a separate operator explanation when a complex
  technical finding cannot satisfy both evidential and conversational needs in
  one presentation.

This is a plausible control, not yet a demonstrated solution. Its value must be
tested against representative findings and long agent runs.

## Inputs and method

The report compares four kinds of evidence:

1. Provider statements of intended model behavior.
2. Provider model-specific prompting and product guidance.
3. Several public user reports that describe the observed failure.
4. The two Commonplace changes made in commits `80a5f3a0` and `73f530b4`.

The external pages were read on 2026-08-29. They remain live sources and may
change; this report freezes the interpretation, not the pages. Public forum
posts show recurring failure shapes but do not estimate prevalence. The
initiating LinkedIn example was supplied in the working conversation without a
source URL and was not independently verified.

The synthesis was produced by Codex under the repository's `AGENTS.md`; the
runtime did not expose a more specific model identifier. No model-generated
claim is treated as primary evidence.

## The reported failure has several independent axes

"Use less jargon" or "be concise" compresses several failures into one global
style preference. The complaints and provider guidance distinguish at least
five axes:

| Axis | Failure | Why a brevity instruction is insufficient |
|---|---|---|
| Amount | The answer includes material the operator does not need. | A shorter answer can still contain the wrong material. |
| Density | Sentences, fragments, or arrow chains carry too many relations at once. | Removing words can make the remaining text harder to parse. |
| Order | Implementation detail appears before outcome, consequence, or decision. | The same content in fewer words can still start in the wrong place. |
| Audience | The answer continues an internal working thread the operator did not see. | Length does not restore missing context. |
| Vocabulary | The answer relies on task-local shorthand or inherited terms with no shared definition. | A coined term can be short, precise to its author, and opaque to everyone else. |

The last axis is the main Commonplace addition. Ordinary language, established
domain language, and project terms with canonical definitions are shared
vocabulary. They need not be removed merely because they are specialized. A
human operator can pay the learning cost once and then benefit from the compact
term. The risky category is vocabulary that exists only in the current agent's
work or has spread through artifacts without acquiring a canonical definition.

This distinction cuts across expertise. An expert can understand difficult
domain terms while still being unable to decode a label invented twenty tool
calls ago. Conversely, replacing every project term with generic language can
lose precision, create synonym drift, and repeatedly charge the operator for a
definition they already know.

## What users report

The strongest consolidated complaint is
[Claude Code issue #77136](https://github.com/anthropics/claude-code/issues/77136).
It describes verbose, jargon-heavy, and invented phrasing; forced metaphors;
answers that become cryptic when asked to be concise; and style instructions
that drift during a session. The issue summarizes a larger Reddit discussion,
but its vote and comment counts are evidence of one cluster of users rather
than a population measure.

Separate threads report the same distinctions from different angles:

- An [Opus 5 discussion](https://www.reddit.com/r/ClaudeAI/comments/1vn8ml6/opus_5_is_actually_almost_rageinducing_to_use/)
  says project-level style rules stop holding after meaningful work and that
  buzzword-heavy explanations can make otherwise useful results difficult to
  review.
- A [cryptic-phrasing discussion](https://www.reddit.com/r/ClaudeAI/comments/1vv14nh/is_anyone_else_finding_claude_really_hard_to/)
  describes dense shorthand and missing transitions; several participants say
  they use another model to translate the output.
- A [Claude Code discussion](https://www.reddit.com/r/ClaudeCode/comments/1vw637w/please_kill_me_now/)
  contains the more specific observation that an agent can invent shorthand in
  its working context, repeat it until it becomes locally familiar, and then
  fail to notice that the shorthand was never user-facing. The same discussion
  notes that an aggressive brevity style can worsen this by condensing prose
  into invented labels.

These reports support the existence and shape of the problem. They do not show
that every user, model, or harness encounters it, and their explanations of the
underlying model mechanism remain hypotheses.

## How Anthropic describes the problem

Anthropic addresses the issue at three layers.

At the intended-behavior layer,
[Claude's Constitution](https://www.anthropic.com/constitution) says response
length should follow the request and should avoid padding, excessive caveats,
and unnecessary repetition. The same document says Claude's actual behavior
may depart from these ideals. This frames appropriate length as a contextual
judgment and acknowledges an implementation gap.

At the model-guidance layer, the
[Claude Opus 5 prompting guide](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5)
says the model's user-facing answers are longer than those of prior Opus models.
It separates reasoning effort from visible response length, recommends an
explicit concision instruction, tells agents to lead with the outcome, and
warns that old verification instructions can compound the model's own
verification and add narration. This account mainly treats amount, order, and
harness interaction.

The
[Claude Fable 5 prompting guide](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5)
matches the observed failure most closely. It says that extended agentic work
can lead to dense shorthand, deep implementation detail, references to work the
user never saw, and overly technical phrasing. It explicitly separates
readability from concision and says shortening should select details rather
than compress sentences into fragments, arrows, abbreviations, or jargon. Its
central vocabulary instruction is: "The vocabulary you built up while working
is yours, not theirs." It recommends treating the final response as a fresh
orientation for the reader, reintroducing any necessary terms, and using a
dedicated `send_to_user` tool when the harness must separate exact user-facing
messages from working narration.

At the product layer, Claude Code
[release 2.1.237](https://platform.claude.com/docs/en/release-notes/claude-code#21237)
added a built-in Concise output style that leads with results and skips preamble
and narration. Its public description addresses amount and order, not the
status of project and task-local terms. The release still shows that Anthropic
treats the harness as a control surface rather than expecting training alone to
settle the problem.

The evidence therefore rejects the simple "Anthropic forgot" explanation.
Anthropic recognizes the general problem and, for Fable 5, the case where
working vocabulary was never shared with the user. Its published remedy still
includes operator prompts, model-specific migration work, and harness
scaffolding. It is not a claim that the base model will always do this unaided.

## How OpenAI describes the problem

OpenAI also treats clarity as both a model target and an application-level
control.

The current
[OpenAI Model Spec](https://github.com/openai/model_spec/blob/main/model_spec.md)
says answers should be lucid, succinct, organized, clear, and direct. It says a
professional default does not mean business jargon. OpenAI's explanation of
[how the Model Spec is used](https://openai.com/index/our-approach-to-the-model-spec/)
is important to interpreting those rules: the specification is partly
aspirational, production models do not yet fully reflect it, training cannot
cover every context, and models can generalize differently from the intended
behavior. The same explanation argues that explicit policies remain useful
because high-level goals underdetermine behavior and runtime context is
limited.

The current
[GPT-5.6 model guidance](https://developers.openai.com/api/docs/guides/latest-model)
offers a `text.verbosity` control but warns that broad brevity instructions can
make an answer too short. It recommends specifying what a short answer must
preserve: the conclusion, necessary evidence, material caveats, and next
action. It also tells developers to keep style guidance when it encodes a
product requirement or corrects a measured failure, and to validate prompt
changes on representative work.

Some earlier model-specific guidance is more explicit about reader vocabulary.
The
[GPT-5.2 guidance](https://developers.openai.com/api/docs/guides/latest-model?model=gpt-5.2)
says to avoid jargon unless the conversation clearly establishes an expert
reader. That is an expertise rule. In the OpenAI pages examined for this
report, no rule distinguishes a canonically defined project term from a term
invented inside one task. The current guidance does supply the pieces—audience,
clarity, explicit output shape, preserved evidence, and local evaluation—but
not this project's vocabulary boundary.

## Why a local control remains necessary

### Only the project knows which vocabulary is shared

A provider can discourage obscure language globally or adapt to apparent user
expertise. It cannot determine from the word alone whether `freshness baseline`
is a registered Commonplace term, whether a code identifier names an important
project mechanism, or whether a plausible compound was invented during the
current review. That information lives in the project's vocabulary and
artifacts.

The Commonplace rule therefore classifies terms by whether their definitions
are shared, not by whether they sound technical. It permits domain language and
canonically defined project terms. It requires an agent to define, expand, or
omit task-local terms and inherited terms that have no canonical definition.
This is more precise than "avoid jargon," and it preserves the value of a small,
stable technical vocabulary.

This also reflects a human-agent asymmetry already described by
[minimum viable vocabulary](../../notes/minimum-viable-vocabulary-is-the-naming-set-that-most-reduces.md)
and
[agent statelessness](../../notes/agent-statelessness-makes-routing-architectural-not-learned.md).
Humans retain useful project terms across sessions. Agents normally need those
definitions loaded again. A durable vocabulary can lower the human's repeated
reading cost while still requiring deliberate routing for each new agent
context.

### The evidence and the explanation have different jobs

A technical finding must preserve exact identifiers, code paths, conditions,
and evidence. Editing it until it reads like ordinary conversation can destroy
the basis for review or implementation. An operator message instead needs to
make the practical outcome, reachability, consequence, and decision clear.

The local design keeps both. The operator explanation points to the technical
finding rather than copying its proof into the opening. This is not merely a
verbosity setting: it is a separation between an evidential artifact and a
reader-facing view of that artifact.

### Provider behavior is a dependency, not the project contract

Model defaults change. The Anthropic guides themselves distinguish Opus 5 from
Fable 5, recommend revisiting prompts during migration, and warn that
instructions tuned for an older model can compound a newer model's defaults.
OpenAI likewise recommends retesting model migrations and keeping local style
guidance when it fixes a measured product requirement.

Commonplace needs one communication contract across providers and versions.
If a future model satisfies it by default, the instruction should become
redundant rather than harmful. If a model-specific prompt conflicts with it,
the conflict should be found by evaluation and the obsolete scaffolding
removed. Waiting for a provider fix would neither encode the project's
vocabulary boundary nor protect it during the next migration.

## The local controls

Commit
[`80a5f3a0`](https://github.com/zby/commonplace/commit/80a5f3a08d90d0a16bfe64b56affcf1c713a40bf)
added two paths:

- The always-loaded
  [operator-communication paragraph](../../../AGENTS.md) tells agents to
  lead with the practical outcome or decision, preserve important conditions
  and uncertainty, introduce implementation details after their meaning, and
  point to technical evidence rather than reproducing it.
- The
  [`operator-brief` skill](../../instructions/operator-brief/SKILL.md) handles a
  consequential explanation that still depends on several concepts or a long
  causal chain. It preserves the full finding as the technical basis and writes
  a separate practical explanation.

Commit
[`73f530b4`](https://github.com/zby/commonplace/commit/73f530b4865aed444654e8d00bfd046317cad54a)
sharpened the vocabulary rule. Project terminology is permitted only when it
has a canonical definition. A term that merely circulated through artifacts
does not become shared project vocabulary by repetition.

The skill is intentionally not the default for ordinary chat. The short rule
covers routine communication; the separate operation pays for a heavier pass
only when the finding's complexity warrants it.

## Worked check against the initiating example

The initiating code-review finding began with the title:

> `drifted` ignores `clearCacheFor`, re-enabling the editor on the chapter whose
> reload just failed

It then led through line references, escalation sites, branch conditions, code
identifiers, and comments. Those details matter to a developer validating the
finding, but they do not tell an operator what happens without first loading
the implementation.

Applying the local rule produces this operator explanation:

> If a global search-and-replace finishes while you switch chapters, and the
> chapter then fails to reload, the editor can show an old copy and still let
> you type. Your next edit can save that old copy over the completed replacement.
>
> The affected chapter should remain locked until fresh content is available.
> The current lock decision ignores the list of chapters whose cached content
> must be discarded, so it can unlock the editor too early.
>
> Technical basis: finding I1 in the full review.

The rewrite keeps ordinary product vocabulary such as *chapter*, *editor*, and
*global search-and-replace*. It explains the one implementation concept needed
for the cause, and leaves `drifted`, `clearCacheFor`, and the line-by-line proof
in the technical finding. It also preserves the narrow triggering conditions.

The check exposes a second reason to retain the technical finding. The supplied
informal gloss can be read as saying the search-and-replace later undoes the
operator's edit. The technical excerpt appears to describe the opposite causal
direction: editing the stale chapter can overwrite the already committed
search-and-replace result. Simplification must not silently choose between
those readings. The evidence remains authoritative when the brief is disputed.

## Plausible causes, with evidence limits

Provider documentation establishes intended behavior and observed model
differences, but it does not expose a complete causal account of this failure.
Several mechanisms remain plausible:

- Long agent traces make temporary working labels locally frequent, so the
  model may treat them as shared even when the user never saw them. Anthropic's
  Fable guidance and user reports support the symptom; they do not by
  themselves establish the internal mechanism.
- Instructions can compete or drift as context grows. User reports describe
  this, and provider migration guides warn that accumulated scaffolding can
  compound new defaults.
- Training and automated evaluation may reward superficial signals of quality.
  The ICLR 2026 paper
  [*Flattery, Fluff, and Fog*](https://proceedings.iclr.cc/paper_files/paper/2026/hash/2096bafd3073a2224f6f0adb594068df-Abstract-Conference.html)
  finds preference-model miscalibration across length, structure, jargon,
  sycophancy, and vagueness. It is evidence for a general selection pressure,
  not evidence about Anthropic's or OpenAI's private training recipe.
- Communication style varies by model and setting. Anthropic's study of
  [values across models and languages](https://www.anthropic.com/research/claude-values-models-languages)
  identifies a depth-versus-brevity axis and says the causes of model shifts are
  not yet understood. This supports testing each deployment rather than
  assuming one universal baseline.

The report therefore does not attribute the problem to hidden reasoning
leakage, reward-model bias, deliberate token inflation, or any other single
cause. Those explanations require evidence not available here.

## Evaluation implications

The local fix should be evaluated as three conditions: provider default,
provider default plus the `AGENTS.md` paragraph, and a separate
`operator-brief` pass. Each should be tested after both short and long technical
runs and across the models Commonplace actually uses.

The primary question is whether an operator can state, after one reading, what
happens, when it happens, why it matters, and what decision or action follows.
Checks should also count undefined task-local terms, verify that causal
direction and material qualifiers survive, and record rereading time. Token
count alone is not a success measure.

The outcomes distinguish likely failure modes:

- If the small `AGENTS.md` rule fixes both short and long cases, the gap was
  mainly local underspecification.
- If it works initially but decays during long runs, context competition or
  instruction drift remains.
- If a separate brief succeeds where the in-context final answer fails, the
  main problem is likely the collision between working context and reader
  context.
- If readability improves while causal or qualifying detail is lost, the
  two-artifact design is necessary but the brief instruction needs stronger
  fidelity checks.
- If results differ substantially by model or harness, the provider layer
  remains a material variable and local guidance should be calibrated rather
  than assumed universal.

Until those tests exist, the evidence supports retaining the current controls
without expanding them. Provider work makes the controls more plausible—it
independently converges on outcome-first writing, selective detail, and
re-grounding after agentic work—but does not yet demonstrate that the controls
will hold in Commonplace's operating context.
