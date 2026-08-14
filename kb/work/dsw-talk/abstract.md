# DSW submission — abstract

Locked title:

> **Strange-Loop Knowledge Base: An LLM Wiki That Rewrites Its Own Rules**

Uses the exact searchable phrase "LLM wiki". Headline is self-hosting framed as a strange loop: a wiki *about* building wikis, operated by the agents that read it, so its output can be a change to its own rules. Sells the intrigue of a system revising its own method without implying autonomy — the honesty line (a human is in every loop; no demonstrated autonomous compounding) is held inside the abstract and the talk.

Title variant considered: *The Strange-Loop LLM Wiki: A Knowledge Base That Rewrites Its Own Rules* — puts "LLM wiki" earlier but stacks three nouns.

## Abstract (~180 words)

Most knowledge bases are about something else. Commonplace is about *how to build knowledge bases* — and, under human direction, it's operated by the same LLM agents that read it. So when its own method strains, the system can rewrite the method.

I'll trace one such loop end to end. A navigation page promised to list everything in a category; readers trusted it and stopped searching — until manual upkeep quietly stopped scaling. The agents retrieved the relevant design notes, revised the type contract, and turned a prose convention into a schema and a validator, which immediately caught a real gap the hand-maintained recipe had missed and changed how future agents search. The knowledge base improved the rules that govern the knowledge base.

I'll show why that strange loop is possible, what makes it reliable — reviewable generation, deterministic rules, task-scoped loading — and, carefully, where the honesty line runs: a human is in every loop. This is self-hosting, not autonomous self-improvement, and I'll mark exactly which arrows still need a person.

## Takeaways (if a separate field)

- Use the LLM to *develop* knowledge — retrieve, distinguish, propose, test scope, connect — not just draft prose.
- Treat fluent output as a candidate, not a certificate: separate generation from review.
- Move a rule into code only once it's stable and checkable; keep genuine judgment with the human or model.
- **Write for reuse; load for the task** — the context you fill is the capacity you spend.

## Audience / level

Data & ML engineers and practitioners building LLM-backed knowledge or RAG systems. Intermediate. No Commonplace-specific background assumed. Talk length: 35 min.

## Open format questions (resolve against the actual CFP form)

- Abstract word/character cap — current draft is ~180 words; can trim to a ~50-word version if the form is tight.
- Are title / abstract / takeaways / bio / talk-length separate fields or one blob?
- Shorter title fallback: *"The Strange-Loop Wiki: When an LLM Knowledge Base Edits Its Own Rules."*

## Alternate: the "drowning" (context-paradox) version

Kept live in case the CFP or reviewer response favors a problem-first hook the audience already feels ("my RAG context is bloated") over the more thought-provoking self-hosting frame.

Title:

> **The LLM Wiki Paradox: When Filling the Context Drowns the Agent**

Abstract:

> The obvious way to build an LLM wiki: store everything, retrieve it, pour it into the context. But context is shared space — instructions, task state, retrieved knowledge, and the model's own reasoning all compete for the same room. Fill it with knowledge and the agent drowns: full of facts, with nothing left to think with. More stored knowledge never means more should be loaded.
>
> This is a practitioner's field report from Commonplace, an LLM-operated but human-directed knowledge base. Through two worked cases — one where the model genuinely sharpened a rough idea, and one where its fluent output quietly got three things wrong — I'll show why reliability comes from a hybrid design: generated knowledge stays reviewable, stable and checkable rules move into deterministic code, and retrieval loads only what the task in front of it needs.
>
> You'll leave with four patterns for your own LLM knowledge system — starting with "write for reuse; load for the task" — and an honest map of what still doesn't work.

Trade-off: *drowning* leads with a problem the audience already has (max "apply next week" pull, lower ceiling); *strange loop* leads with a rarer idea (higher ceiling, narrower hook, constant discipline not to over-claim autonomy). Whichever is the headline, the other becomes a section in the talk.

## Rejected title variants (for reference)

- *The LLM Wiki Paradox: When Filling the Context Empties the Agent* — "empties" can misparse as *lost knowledge*.
- *…Starves the Agent* — the agent is flooded, not deprived.
- *The Wiki That Improves Itself* — "improves itself" reads as autonomous; over-claims the honesty line.
