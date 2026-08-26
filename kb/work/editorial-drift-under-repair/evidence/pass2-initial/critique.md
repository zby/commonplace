<!-- copied from the gitignored kb/reports tree; original frontmatter retained below as data -->

```yaml
review_job_id: 8367
review_pair_id: 20833
note_path: kb/notes/naur-binds-theory-to-humans-via-premise-that-machines-follow-rules.md
criterion_path: kb/instructions/critique-note.md
model_partition: codex
runner: /root/initial_critique
runner_model: null
runner_effort: null
result_kind: report
outcome: null
completed_at: '2026-08-26T14:06:03+00:00'
```
# Critique: Naur binds program theory to humans through the premise that machines only follow rules

**Note:** kb/notes/naur-binds-theory-to-humans-via-premise-that-machines-follow-rules.md
**Central commitment:** Naur's argument binds program theory to humans only by assuming that every non-human interpreter follows formulable rules, and a trained LLM falls outside that assumed dichotomy because nobody formulated the criteria behind its similarity judgments.
**Critique mode:** claim
**Attack outcome:** lands

## Strongest case against it

A Naurian defender can argue that the proposed third category rests on an equivocation between *not hand-authored as an intelligible criterion* and *not determined by formulable rules*. An LLM's training examples do not remain its operative source of judgment at inference time. Training produces a finite numerical state, and the architecture, stored weights, tokenization, and inference algorithm formally determine a distribution over its next outputs. Sampling does not change the category: its transition probabilities and sampling rule are also formal. The resulting specification may be enormous and opaque to people, but opacity and impracticality are not in-principle informulability. A rule can be induced rather than individually chosen by its designer.

The source language supports this broader reading more strongly than the note acknowledges. Naur contrasts human access to similarity with what can be "determined by rules," describes computer execution as "formal symbol manipulation," and says the relevant criteria *cannot be formulated*, not merely that nobody happened to formulate them in semantic prose. The note repeatedly substitutes the weaker historical condition that the criteria were not formulated by anyone. Yet an LLM's learned parameters are literally encoded, and its judgment is produced by a formally specified computation over them. On Naur's terms, that makes the LLM a particularly complicated instance of the machine pole, not an interpreter outside the partition.

The appeal to supervised acquisition does not rescue the distinction. Naur's claim that a person acquires theory by doing under guidance does not imply that every mechanism trained from examples thereby acquires the non-rule-governed world-understanding that his use of Ryle requires. Example-based learning can yield a rule-governed classifier. Likewise, the fact that neural networks can recognize faces, tunes, or other patterns does not establish that they exercise the same capacity those examples were introduced to characterize; behavioral success on recognition is compatible with formal determination of each output.

This objection need not prove Naur's stronger thesis that no possible machine could possess theory. It is enough to defeat the note's stated counterexample: a current LLM does not show that the human-versus-formal-machine partition is non-exhaustive. Without a different account of why a completely specified learned computation is not rule-determined in Naur's relevant sense, the note has not shown that his argument fails to reach its trained interpreter.

## How the note engages it

Partially engaged. The section "A trained interpreter falls outside the partition" directly anticipates the observation that an LLM is computable and answers that Naur discusses formulability rather than computability. But it asserts rather than establishes the decisive step: that learned criteria are unformulated in the relevant sense even though the model state and inference operation can be finitely and formally specified. It also does not reconcile its narrow reading with Naur's explicit contrast between human judgment and a computer's formal symbol manipulation. The note therefore sees the objection but answers a weaker version in which "rule" means a compact, human-authored semantic criterion.

## Constructive findings

- Define whether "formulable rule" excludes a formally specified learned network, and justify that exclusion from Naur's text rather than from the fact that no person selected the weights individually.
- Separate three properties now run together: human-readable criteria, finite formal specification, and computability. The argument needs the first boundary, while the proposed LLM counterexample plainly satisfies at least the second.
- Either supply a reason that model execution is not rule-determined in Naur's sense or narrow the conclusion: Naur may leave possible non-human theory-holders unrefuted even though present LLMs do not themselves establish a third category.
- Treat learning from examples as evidence about acquisition history only; add an argument before inferring from that history to the learned interpreter's status as a theory-holder or non-rule-follower.

## Result: REPORT
