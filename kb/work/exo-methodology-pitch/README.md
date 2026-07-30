# Exo can remember everything. What should become a lesson?

Exo has built an unusually strong substrate for learning. It keeps the full record of what happened, lets the agent save facts and skills, and can preserve successful changes as tools, tests, prompts, or code. ExoWorker even supplies a simple rule of thumb: lasting fact → memory, reusable playbook → skill, repeated helper → tool.

That makes the next question unavoidable:

> Which experiences are worth turning into lessons?

Retain too little and the model keeps re-deriving the same conclusions from code and history. Retain too much and the system builds a second, noisier history — full of plausible summaries that consume context, grow stale, and acquire authority they never earned.

The missing layer is not another memory store. It is an explicit, improvable policy for what deserves to be kept, in what form, with what authority, and for how long. We call that a theory of promotion: what gets promoted from the record into a lesson.

## A concrete case

Suppose Exo hits the same integration failure twice and installs a managed tool that prevents it. The tool preserves exact behavior. The registry records its source, pinned to an exact commit. The event log preserves the failures and the installation.

None of those artifacts decides what the future should inherit from the episode:

- Was this a provider-specific workaround or a general integration rule?
- Should it apply whenever a similar error appears, or only under the original configuration?
- Is the reusable result the example, a short claim, a playbook, a test, or the tool itself?
- What change should make Exo reconsider or retire it?

A capable model can answer these questions just in time. But if the questions recur, the system pays again each time it selects the evidence and reconstructs the answer — and can produce a different answer each time.

## Sometimes the evidence cannot give the lesson back

There is a harder case than expensive re-derivation. Suppose that tool caps concurrent requests at 12. That number could be a permanent safety ceiling, or temporary tuning for one provider's quota. The code is identical either way, and every past run looks the same either way. But when the provider raises its limits, the two readings demand opposite responses. If nobody recorded which was meant, no future model — however capable — can recover the intent from the evidence. It can only invent a plausible one.

So retained lessons come in two kinds: **caches**, conclusions that could be re-derived but are kept because re-deriving is costly or unstable, and **commitments**, decisions the evidence can never give back. They need different maintenance rules: a stale cache can be discarded and rebuilt; a lost commitment is gone.

## The claim

> Write a lesson down when it will be needed again and re-deriving it costs more than keeping it current — or when it records a decision that nothing else can recover.

And choose its form by the work it does:

> **episodes for evidence · natural language for reusable meaning · code for exact behavior**

Keep the episode when its detail is the value. Write a conclusion in natural language when a mechanism should recur, transfer, or stay open to criticism and revision. Codify it when the useful part can be stated and checked mechanically. Record adopted decisions, because the evidence cannot recover them.

Do not write down one-off interpretations, cheap deductions, generic summaries, or conclusions likely to expire before reuse. Natural language is not the default destination for every trace. It is the form for conclusions the model can state and use but the system cannot yet turn into a test, schema, or program.

## What we'd add

Exo can already write lessons into memory and skills. The proposal is to make the selection policy itself explicit and improvable: a maintained theory of promotion, plus enough structure on each retained conclusion — its evidence, trigger, scope, and current status — that Exo can later criticize, rescope, supersede, retire, or codify it as the system changes.

That proposal may lose. Exo's existing heuristics, raw episodes, tools, and capable models may reconstruct the right lesson cheaply enough. A maintained lesson store may instead become expensive, distracting, or confidently stale. Those outcomes would narrow or defeat the argument.

## Think first, then verify it your way

You have the pitch; form your own view before opening the supporting documents. Then use your own agents, tools, and preferred methods to verify or attack it. The supporting documents expose our reasoning and evidence; they deliberately do not prescribe a verification protocol:

- [Detailed argument](./argument.md) — the promotion theory in full, the three retained forms, Exo-shaped cases, the minimal proposal, and claim limits
- [Evidence and counterevidence](./evidence.md) — pinned Exo and ExoWorker facts, supporting theory, positive and adverse results, open gaps, and falsifiers

This pitch comes out of [Commonplace](https://github.com/zby/commonplace), a framework for agent-operated knowledge bases. Commonplace is both a theory and a working system: a body of claims about knowledge retention that we hope hold beyond our own tooling, entangled with the design choices that test them. As an implementation it is only one candidate for the missing layer — the argument does not require adopting it. Exo's own memory, skills, event records, or another store entirely could implement the same capability.

---

*Workshop status: closes when the pitch has survived or failed independent criticism, the durable conclusions are extracted into the library, and we decide whether to bring the argument to Exo.*
