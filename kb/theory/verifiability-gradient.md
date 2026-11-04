---
description: Compare verification by the requirement checked, reset conditions, retry cost and strength of feedback; prompts and code have no automatic ordering on these dimensions
type: types/note.md
traits: [has-comparison]
tags: [learning-theory, constraining, evaluation]
---

# The verifiability gradient

> Software 1.0 easily automates what you can specify. Software 2.0 easily automates what you can verify.
> — Andrej Karpathy, [Verifiability](https://karpathy.bearblog.dev/verifiability/)

Karpathy identifies three properties that make a task verifiable: **resettable** (you can retry), **efficient** (retries are cheap), and **rewardable** (you can evaluate results automatically). The more verifiable a task is, the more you can hill-climb on it — through RL at training time, or through iteration at runtime.

For [deployment-time adaptation through retained artifacts](./retained-artifacts-enable-persistent-deployment-time-adaptation.md), assess those properties for a particular task and checking procedure. A prompt, schema, test suite or code module does not have a fixed grade of verifiability. The same artifact can admit an exact check for one requirement and a difficult judgment for another.

## Examples of checking different requirements

These are illustrative checking arrangements, not measured cost comparisons. Each uses saved inputs and keeps retries separate from production side effects.

| Artifact and requirement | Check and what it establishes | Reset and retry cost | What remains to assess |
|---|---|---|---|
| Report-summary prompt: return JSON only | Parse the complete response as one JSON value; this checks syntax and rejects surrounding prose | Reuse the saved prompt; each retry costs a model call plus parsing | Whether the values answer the request |
| The same report-summary prompt: preserve the report’s meaning | Compare the summary's claims and omissions with the saved report | Reuse the same report; each retry adds generation and source review | The reviewer needs criteria for faithfulness and important omissions |
| JSON schema requiring an `evidence` array | Validate required fields and their types | Revalidate saved outputs without regenerating them; cost depends on output size and schema | Whether the cited evidence supports the claim |
| Deterministic date formatter with a specified input format and timezone rule | Compare outputs with independently established expected strings for leap days, offsets and invalid inputs | Rerun saved cases; no model call is needed | Coverage beyond those cases and whether the chosen timezone rule serves the task |
| Deterministic program that summarizes reports by selecting sentences | Check that selected sentences occur in the report; separately review whether selection preserves qualifications | Rerun on saved reports; exact text checks can be automated, while reviewing meaning still takes work | Copying every sentence accurately does not establish that the selection is a faithful summary |

The first two rows use the same prompt but require different checks. The last row uses deterministic code and still needs semantic assessment. Conversely, parsing checks JSON syntax regardless of whether a prompt or a conventional program produced the text.

Schemas and tests can be used with either prompts or code. They are parts of a checking arrangement, not stages that necessarily replace the artifact being checked. A pass rate reports how often a check passed across the sampled runs; what that tells us about quality depends on what the check tests.

## Compare costs and guarantees separately

[Reference adoption, inspection cost and task adequacy are separate questions](./symbolic-form-holds-consumers-to-a-semantic-reference.md). A model package adopted as the language reference fixes semantics without supplying a check for the caller's task. A deterministic function can implement the wrong requirement exactly.

For a proposed change, name the requirement and compare:

- **Reset conditions:** which inputs and state must be restored to retry? A saved document is easy to reuse; a workflow that sends messages needs a test environment or control over those side effects.
- **Execution cost:** what does producing another candidate cost, including model calls, computation and tools?
- **Checking cost:** what can be checked automatically, and what needs source review or user feedback?
- **Strength of the check:** does it check the requirement itself, a limited property such as syntax, or a proxy such as agreement with a reviewer?

Code extraction can improve a particular arrangement. Replacing repeated model calls for date formatting with a tested function removes those calls and allows direct inspection of its formatting rules. The expected outputs still need an independent basis, and implementation and maintenance have costs. Keeping the same tests before and after extraction helps compare conformance without confusing a change in implementation with a change in the check.

## Placement follows the task and the evidence

[Tightening and relaxing](./codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) remain useful responses to evidence. Their value depends on what a particular change buys:

- Require a nonempty `evidence` array with citation fields when missing citations are an observed failure. The schema can enforce those fields; support for the claims still needs checking.
- Extract the date formatter when the rule is sufficiently specified and repeated use justifies implementation and maintenance. Stable outputs alone do not establish that the rule is right.
- Revise or relax a schema that rejects valid answers. For example, a schema requiring exactly one citation needs revision when a claim requires support from two sources.

A stable natural-language instruction can remain an appropriate implementation when its checks and operating costs meet the task's needs. The placement question is what a proposed change improves at acceptable cost. Moving toward code is one possible answer.

## Scope

“Gradient” names differences in how readily a task can be retried and assessed. It does not assign a universal order to artifact kinds. Arrangements can trade off execution cost, checking cost and strength of feedback; compare them against the same requirement and operating conditions.

---

Relevant Notes:

- [Retained system-definition artifacts enable persistent deployment-time adaptation](./retained-artifacts-enable-persistent-deployment-time-adaptation.md) — grounds: supplies the adaptation setting in which repeated checking matters
- [Codification and relaxing navigate the bitter lesson boundary](./codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) — extends: develops evidence-guided changes in how requirements are implemented
- [Oracle strength spectrum](./oracle-strength-spectrum.md) — contrasts: explores the quality of correctness signals; reset conditions and retry costs also need separate assessment
- [Symbolic form holds consumers to a semantic reference](./symbolic-form-holds-consumers-to-a-semantic-reference.md) — grounds: reference adoption is separate from inspection cost and from adequacy to the task
