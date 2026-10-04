# Quotation design review

Agent diagnosis, 2026-10-04, at the operator's request. It applies
[review design pressure behind recurring errors](../../../instructions/review-design-pressure-behind-recurring-errors.md)
to quotation errors in analysis runs. The result is a recommendation. It
authorizes no change.

## Recommendation

Let the worker write each quotation once, in its draft, as the passage and
its source path, and let one helper call complete every such quotation in the
draft. Remove the JSON batch mode. This is alternative S below. It answers
both pressures found here: the need to resolve many quotations in one call,
and the fragility of copying exact text between files and formats.

The operator first preferred removing the batch mode alone (alternative R),
then reconsidered because workers have a real need for a batch, and adopted S
on 2026-10-04. Implementation is commissioned by the
[plan](./quotations-completed-in-draft-plan.md).

Do not move to designation by line number now.

## The concrete situation

To quote, a worker does four things:

1. Reads the source and chooses a passage.
2. Copies the passage's text into a selection: a text file, or an entry in a
   JSON list for a batch.
3. Calls `commonplace-quote`, which locates the text in the frozen source and
   returns a citation with the exact text, path and line range.
4. Copies that citation into its report.

Code then matches every quotation in the submitted member against the source.

Steps 2 and 4 require the worker to reproduce source text exactly. Both pass
the text through the worker's tool-call encoding, and step 2 in batch mode adds
a JSON layer inside it. Source code is full of quotes, backslashes and
newlines, which each layer escapes differently.

## Observations

From the audits in `kb/work/analyse-agentic-system-amendments/`:

- Fresh run, epistemic: hand-written selections JSON was malformed; the first
  repair failed on the same file. A later selection did not occur verbatim,
  and its correction over-escaped newlines. The worker then used a literal
  text file and succeeded.
- Second run, memory: the helper returned a correct citation, and the draft
  altered `"\n"` to `"\\n"` when the worker inserted it. Acceptance refused
  the output. This is the only quotation failure that cost a refused output.
- Second run: two selection files written to wrong paths.
- Stopped Graphiti run: a batch entry without its key, and an empty selection.

A count over the retained worker traces of 2 and 3 October, made for this
review with a crude pattern match on helper calls and their outputs:

| Mode | Calls | Failed | Returned candidates | Succeeded |
|---|---:|---:|---:|---:|
| `--text-file`, one passage | 63 | 3 | 12 | 48 |
| `--selections`, JSON batch | 23 | 8 | 3 | 12 |

About 5% of single-passage calls failed, against about 35% of batch calls.
The traces may include sessions other than the two audited runs, and a batch
counts as failed when any entry failed, so the two rates are not strictly
comparable. The direction is clear enough to act on.

All final quotations in both accepted sets pass the source check. The cost of
these errors is failed tool calls and their repair inside already loaded
contexts, plus one refused output.

## Diagnosis

The worker rules name the batch mode as the way to request "many selections".
A worker that needs several quotations has a reason to use it: fewer tool
calls. That mode asks for source text inside JSON strings, written by hand
through a tool call. This is the design pressure: the convenient route is the
one with the most escaping.

This differs from the range case. Ranges were a shorthand the worker reached
for against a rule. Here the worker follows the documented route, and the
route itself is fragile. Nothing forbidden is attractive; something required
is hard.

The alteration at insertion is the same mechanism at step 4. The worker must
copy a block containing escape sequences through its edit tool.

These are inferences from tool calls and outputs. They do not establish what
any worker reasoned.

## What must survive

- Every quotation in an accepted member is verbatim text of the frozen source,
  with the correct path and line range.
- The analyst chooses the passage and judges whether it supports the finding.
- Code proves occurrence. Nobody formats a citation or computes a range by
  hand.
- A fabricated or misremembered quotation fails loudly.

The JSON batch format and the copying of the citation are not among these.
They can change.

## Why the batch exists

The batch mode was added on 2026-09-28 in commit `e984a4607`. Its message
records the reason: all six worker traces of the 2026-09-27 regression had
built a per-quotation subprocess loop by hand, and one such wrapper failed on
a valid response that listed two occurrences. The batch was meant to make one
call enough, so workers would stop writing loops.

So there are two pressures. Workers want to resolve several quotations with
few calls. The batch answered that with a format that is fragile to write.
Removing the batch removes the fragile format and leaves the first pressure
unanswered.

## Alternatives considered

**S. Quotations completed in the draft (recommended).** A citation today
is a blockquote of the source lines followed by an attribution line with
path, line range and revision. Under S the worker writes that blockquote
directly in its report, with the passage and an attribution that names only
the path:

```text
> for line in data:
>     file.write(json.dumps(line) + "\n")
> --- `run_benchmark.py`
```

One helper call on the draft finds each such passage in the frozen source and
rewrites the block with the exact source text, the line range and the
revision. A passage that does not occur is reported with its location in the
draft and left unchanged. A passage that occurs more than once is reported
with its candidate ranges, and the worker adds the chosen range to the
attribution; the helper checks that the text occurs there.

**Why the helper also replaces the quoted text.** Operator decision,
2026-10-04: keep the replacement. It is not needed for acceptance. Both the
helper's search and the acceptance check compare text with whitespace
collapsed (`normalize_text` and `match_quote` in
`src/commonplace/lib/quote_matching.py`), so a copy with different spacing is
found and accepted either way. The replacement serves three other purposes:

- *Fidelity for readers.* A published quotation shows the source's exact
  characters. Indentation carries meaning in languages such as Python, and
  an analyst's copy can lose it. Today this is guaranteed because code
  generates the whole block; the replacement keeps that guarantee.
- *One form per passage.* The same passage quoted by two analysts, or in two
  runs, yields identical bytes. Differences between runs then reflect changes
  in the analysis, not in how someone copied text.
- *Agreement with the cited range.* The block shows exactly the text at the
  line range in its attribution.

The replacement changes whitespace only. It never corrects wrong text: a
passage that differs from the source in any other character is not found, is
reported, and is left as the worker wrote it. This limit is what keeps a
misremembered quotation a loud failure, and the helper must not relax it.

What this removes: selection files, keys, the JSON batch, the rule about
where selection files live, and the copying of a citation into the report.
The passage is typed once, in the place it is used. The draft is the batch.
What it keeps: the worker chooses the passage, a misremembered quotation
fails loudly, and code computes every range. An escaping slip such as the
altered `"\n"` shows up as "not found" when the worker runs the helper,
before submission, instead of as a refused output.

Cost: one new helper mode that edits the worker's draft in place, which must
leave completed citations and all other text untouched. It can be tested
without a model: strip the range and revision from every citation in the
retained members, run the helper, and require byte-identical members back.
Remaining risk: the passage still passes through the worker's write tool
once, as all report text does.

**R. Remove the batch mode.** Delete `--selections` from the
helper, the worker rules and the command reference; no other consumer was
found by search. One call per quotation, with a literal text file, is the
route that failed about 5% of the time against 35% for the batch. It removes
a format, an option and a paragraph of rules. Cost: more helper calls per
job; workers already made 63 single calls against 23 batch calls in the
traces counted. Known risk: workers may again build their own loops, as they
did before the batch existed. Do not answer that with a rule against loops;
that would be enforcement against a real need. If loops reappear, the
smallest answer is to let the single-passage form accept several text files
in one call, which adds no file format.

**A. Batch without source text in JSON (not chosen).** The operator judged
this added complexity for a mode that can be removed. The worker would
still supply each passage's text, but as literal text, not as a JSON string.
One plain file would hold all selections, each under a header line giving its
key and source path:

```text
=== write-jsonl | run_benchmark.py
f.write(json.dumps(row) + "\n")
=== openai-limit | text_generation/simple_unified_client.py
max_tokens=min(max_tokens, 4096),
```

The passage is written exactly as it appears in the source, with no escaping
for the batch format. Code splits the file on header lines. One write and one
helper call serve many selections, so the batch keeps its saving in tool
calls. A directory of one text file per selection would also remove the JSON
layer, but costs one write per selection. The worker that failed with JSON
succeeded with a literal text file; this makes literal text the only route.
Cost: a change to the helper's batch input and one paragraph of worker rules.
Remaining risk: the file still passes through the worker's write tool once,
which is the route with the 5% failure rate, and a source line that itself
starts with the header marker would need a different marker.

**B. Code inserts the citation.** The worker writes a marker with the
selection's key where the quotation belongs and runs the helper with an option
that replaces each marker in its draft with the generated citation. The
worker runs this before submitting, so the submitted member is still exactly
what acceptance judges. The citation's bytes never pass through the worker's
edit tool. Cost: a helper option and a rule. New risk: an unfilled marker in
a submitted member, which a check can refuse by name.

**C. Designate by position.** The worker names a path and a line range, and
code extracts the text. This removes step 2 entirely: no retyped text, no
escaping, no empty selection and no ambiguity between occurrences. I do not
recommend it now, for two reasons. First, it weakens the last invariant:
today a wrong selection fails because the text is not found, while a wrong
line range returns a genuine passage that may not be the intended one. The
error becomes quiet. Second, it needs line numbers the worker can trust. In
the retained Pi trace, file reads returned text without line numbers, so the
worker would compute them, which the current rule forbids for good reason.

**D. Repair escape-only differences at acceptance.** When a submitted
quotation differs from the source at its cited range only by escaping, code
regenerates it. This supports the behavior instead of preventing it. It is
cheaper than B but makes the cited range authoritative over the quoted text,
which hides a hand-edited range. B achieves the same without that.

**E. Keep the design and document the batch shape.** This is item 2 of the
Sol run follow-up plan: one valid example beside `--selections`. It helps
with the missing key. It does not address escaping, which caused most batch
failures.

## Trade-off that matters

S and R both remove the fragile JSON format. R leaves the need for a batch
unanswered and costs a call per quotation. S answers it with one call per
draft, at the cost of a helper that edits the draft. A and B reach a similar
result with more parts: a selections file, keys and markers. Designation by position removes more errors but trades a loud failure
for a possibly quiet one.

## Limits and what would change this

- The counts come from a crude pattern over traces that may include other
  sessions. A proper count per run and per job would firm up the 35% figure.
- Candidates responses are 17% of calls. Each costs a second call. They are
  the designed answer to ambiguity, not errors, and no option here reduces
  them. If they prove costly, a short position hint beside the text, used
  only to pick among occurrences, would address them without weakening the
  text check.
- If workers still fail single-passage selections at a material rate,
  the retyping itself is the problem, and C with a numbered view supplied by
  the helper becomes worth designing.
- If the first runs after the collection split show no refused outputs for
  quotations, B is not worth building.

## Relation to other work

Removing the batch replaces item 2 of the Sol run follow-up plan, which
documents the JSON shape. B is an instance of [code-owned bookkeeping](./code-owned-bookkeeping-proposal.md):
code handles exact text, the worker handles choice. Named record IDs do not
affect either.
