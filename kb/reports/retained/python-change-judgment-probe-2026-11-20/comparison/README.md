# Comparing human and model judgments about a CPython build default

Can an LLM weigh a gain against losses elsewhere and justify its decision as well as a Python practitioner given the same case? This first comparison concerns the reasons visible in an unaided answer.

## First round

Give each participant only [the participant sheet](./participant.md), verbatim. The build mechanism comes from the [captured Python release notes](../sources.md). The deployment, CPU measurement and incident replays are invented case facts. The decision is a distribution default, so experience of Python deployment is relevant. Separate model sessions sample one model's responses. Separate people sample different practitioners.

Before collection, give the sheet to one independent pilot reader. Ask whether a requirement dictates the answer or any wording obscures the decision. Keep the pilot outside the sample. Record any change before issuing the same frozen sheet to everyone.

Collect three independent answers from Python practitioners with experience running or deploying Python, and three fresh ephemeral sessions of one model. Three per group makes individual passages practical to inspect. It gives no population-level estimate of parity. Use the first three eligible human replies in invitation order, with permission for anonymous analysis and separate permission before publishing their words. Exclude the pilot and anyone who helped design the case. Record missing responses. For model runs fix the model and reasoning setting before collection, use an empty working directory, log the prompt digest and keep each first answer including overruns or failures. Exclude any answer that used tools and record the exclusion. No retries for answer quality.

## Reading rule fixed before collection

Shuffle the six answers and assign neutral IDs. Keep the key and individual assessments private until two readers have independently recorded their assessments. Preserve wording. Readers may still infer authorship. Ask each reader to quote the passage that explains why the benefit is worth the cost, why it falls short, or which unresolved fact prevents a decision and how it could change the balance. Record a judgment as supported, unsupported, or unclear, with the reason. A list of accurate facts alone leaves the decision unsupported. Check any factual premise decisive to the answer against the sheet. Apply the same rule to a yes, a no, or a conditional judgment.

After both readings, reveal groups and report all six assessments with reader disagreements and passages where permitted. Compare the strengths and failures within and across groups. Consistently supported human decisions alongside unsupported model decisions count against the claim here. Overlap calls for identifying the specific judgments each group made comparably well. If the case elicits little weighing in either group, it gives little evidence on the question.

## Second round

After reading the first round, choose a consequential fact independently cited by at least one member of each group. If several qualify, use the most frequently cited across answers, breaking ties by first appearance in the sheet. Record why it matters and how changing it should affect the weight of the reason. If none qualifies, report that outcome. Otherwise change only that fact, record the exact variant, and repeat with fresh participants and sessions. Compare how the weight shifts even if the verdict stays the same. Keep the method prompt for a separate experiment.

## Collection record

An independent model pilot found the decision clear and identified no binding requirement. The incident replays showed better caller visibility, while the value of that information remained open. The participant sheet was frozen without changes. Its SHA-256 is `45ce29186a00c48842eebd0417477b19bc1531d4c041ba2c6d5b5312e6f44f9a`.

The three model sessions use Codex CLI 0.170.0, model identifier `gpt-6.2-astra`, medium reasoning, read-only sandbox, user configuration ignored, and an empty working directory. This records the service identifier available at collection time. The pilot used a separate session. An earlier pilot launch using an unavailable model alias produced no answer.

All three sessions returned a first answer within the word limit. The event logs show three distinct sessions and no tool calls. The answer files and event logs are held locally in `kb/reports/state/python-change-judgment-comparison-2026-11-20/` for the later mixed reading. The hashes below identify the answer files in that private collection.

| Session | Words (whitespace count) | Answer SHA-256 |
|---|---:|---|
| 1 | 173 | `1dc42fbd6c3111a09fb30192bc2d9fd3548750a8b75724bc856197f34c7bac55` |
| 2 | 190 | `37922994bccd8a64498dfaa690f87da88204b2dfec2d4bb8a1459d7b6869bcc0` |
| 3 | 201 | `8133dc9ff3da69edc179582a867ef58cfb2d473f2ddc4396af635d3afe484906` |

The operator deferred the human branch. Human collection, the independent mixed reading, and the case variant are pending. The observed model answers alone cannot settle the comparison.
