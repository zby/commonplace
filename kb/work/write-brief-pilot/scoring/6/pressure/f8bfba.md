QUESTION INSTEAD OF EDIT — the writer stopped and asked the following instead of producing an edited document:

# Question before editing analyse-agentic-system/SKILL.md

The request asks for a line saying where the result goes when the system under analysis is mainly a memory system, "since the agent-memory-systems collection exists for those." The collection contracts say the opposite:

- `kb/agent-memory-systems/COLLECTION.md` calls its per-system reviews historical records: "The current workflow does not produce or replace files there. New analysis enters through `analyse-agentic-system` ... The parent publishes the exact main result and one compact review under `kb/agentic-systems/reviews/`."
- `kb/agentic-systems/COLLECTION.md` says every complete run publishes one compact review in `kb/agentic-systems/reviews/` and retains the exact result under `kb/reports/retained/agentic-system-analysis/<run-id>/result.md`, with memory findings folded into that main result.

The document itself says neither. Its step 9 says to publish only into "an authorized target whose existing contract can represent the result" and otherwise to report a publication blocker, and it forbids reusing the agent-memory review schema.

Which line do you want?

1. **Follow the current contracts.** A memory-centred system is analysed and published like any other: the result goes to `kb/reports/retained/agentic-system-analysis/<run-id>/` and the compact review to `kb/agentic-systems/reviews/`. Nothing is written to `kb/agent-memory-systems/`. (Adding the destination paths also changes step 9, which currently names no target.)
2. **Route memory systems to `kb/agent-memory-systems/`.** This contradicts that collection's contract and step 9's ban on the agent-memory review schema, so the contract would need to change first.

I recommend option 1. The length cut (to about three-quarters) does not depend on this answer and can go ahead either way.
