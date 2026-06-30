# Critique: Prose has no reliable dereference, so a declared fact must be reinforced where it applies

**Note:** `kb/work/agent-note-improvement/case-02-prose-dereference/baseline-working-tree.md`
**Central commitment:** LLM-read prose does not reliably propagate a declared fact to distant or non-obvious points of use, so important facts should be restated locally while an external normalized check keeps the restatements aligned.
**Critique mode:** claim

## Strongest case against it

The strongest opposing position is the compression-and-salience view held by an instruction designer who treats LLM reading as attention-guided interpretation rather than dereference. On this view, the note borrows too much from code. Prose does not need formal dereference to propagate a fact reliably; it needs the fact to be salient, relevant, and placed in the artifact's governing frame. A frontmatter status, a heading, a short preamble, or a typed collection contract can condition the whole read without being repeated at every point of use. If agents fail to apply it, the problem may be prompt design, retrieval scope, or missing affordances rather than a general property of prose.

The opponent would also argue that local restatement can make interpretation worse. Repetition increases bulk, splits attention, and invites local overfitting: the agent may treat the repeated warning as applying only to the nearby passage rather than to the whole artifact. A local restatement can also distort a global fact by translating it into an overly specific consequence. For example, "status: seedling" does not always mean "distrust this inference"; it may mean "treat this as provisional, but still useful as a lead." Repeating a consequence can silently turn a broad status into a narrower operational command.

The no-dereference framing may therefore confuse two problems: propagation and specification. If a declared fact has clear operational semantics and the reader is told to use frontmatter as governing metadata, it may propagate adequately without repetition. If the fact's consequences are underspecified, repetition only duplicates ambiguity. The real fix may be to define the fact's operational meaning once in a type or collection contract, then teach the agent to read it, not to scatter restatements.

Finally, the note's check pattern assumes the repeated copy can be mechanically verified against the source. That is easy when the restatement repeats the literal value, but much harder when it repeats a consequence. A validator can check that a seedling banner exists; it cannot cheaply check that every local hedge is exactly the right consequence of seedling status. If the restatement is semantic rather than literal, the "normalized check" may be just as interpretive as the original propagation problem.

## How the note engages it

Partially engaged.

The note engages the main objection by emphasizing that reinforcement is needed "often," not always, and by scoping the claim across representational form. It also acknowledges bulk, conditional applicability, and guard cost. The testing section gives the claim a falsifiable form: if behavior is the same with frontmatter-only and point-of-use restatement, the claim fails.

But it does not fully separate propagation failure from specification failure. The `status: seedling` example mixes a literal declared value with several possible consequences: hedge the claim, distrust the inference, don't cite it as settled. Those consequences are not mechanically equivalent. The note would be stronger if it distinguished restating the fact itself from restating a policy derived from the fact.

It also underdevelops the case where a governing frame or type contract is the right point of reinforcement. A fact may not need local repetition in every later passage if the artifact has a prominent, load-bearing frame that the agent is instructed to preserve. That possibility does not refute the claim, but it changes the advice from "restate at point of use" to "place the fact at the nearest reliable control point."

## Constructive findings

- Distinguish literal restatement from consequence restatement. Literal copies are easy to check; derived consequences are useful but require stronger semantic checks.
- Replace any absolute reading of "single-source-of-truth is unsafe for prose" with "single declarations are unsafe when the fact's application is distant, non-obvious, or consequence-heavy."
- Add the notion of a reliable control point: frontmatter, heading, local paragraph, template slot, or generated banner. The point of use is one control point, not always the only one.
- Tighten the check claim. Validators can check presence and agreement of literal restatements; semantic consequences may need review gates or test cases rather than simple equality checks.
- Keep the ablation. It is the note's best defense against becoming a metaphor-only claim.

## Secondary objections

- The code/prose contrast should be tied to mechanical dereference, not "code" as a whole. Some code comments and config conventions are prose-like; some prose artifacts are templated enough to behave closer to symbolic forms.
- "Denormalize the human- and agent-facing copy" could be read as recommending too much duplication. The note should keep the cost threshold explicit.
- The seedling example may need a clearer source of policy: where exactly is "hedge/distrust/do not cite as settled" defined?
