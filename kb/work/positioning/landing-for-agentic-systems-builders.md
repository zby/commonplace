<!-- Draft (2026-07-04): second landing page — content-first framing for agentic-systems
builders. Sells the KB as a ready-to-use catalogue of problems and solutions; the framework
is the reveal, not the pitch. Complements the-knowledge-layer-for-ai-agents.md (framework-first,
for people who want to build their own KB). Same repo, two doors.
Updated 2026-07-04: usage section reframed as "interactive textbook that lives in your repo"
(install = clone/submodule + one CLAUDE.md routing line); reading path split out to
textbook-syllabus.md. Still missing: a published worked example of the point-it-at-your-code
loop (a transcript of the KB critiquing a real design).
Updated 2026-07-05: integration corrected from "next to your code" to inside-the-repo
placement (submodule or gitignored clone) — agent harnesses scope file access to the project
root, so a sibling directory costs a permission grant every session while a subdirectory
reads free. Routing line made concrete (names the path and entry file). Consumer-install
changes this implies (root-level reader entry, CLAUDE.md vendored-mode guard) tracked
separately. -->

# The hard problems of agentic systems, catalogued

The model is the part you don't control and mostly don't need to. What decides whether your agentic system works is everything around it: whether the right knowledge reaches the context window at the right time, whether the system learns from its deployment or repeats its mistakes, whether its memory can be trusted, and whether it fails loudly or silently. These problems recur in every agentic system ever built — and they have general formulations, and known solutions, scattered across hundreds of codebases, papers, and threads.

**This knowledge base catalogues those problems and their solutions in their most general formulations.** Not vendor takes, not framework tutorials — transferable claims about mechanisms, each stated as a sentence you can test against your own system.

## What's inside

- **220+ theory notes** on context engineering, agent memory, deploy-time learning, and failure modes. Each note's title is its claim; each carries a description, a reliability status, and labeled links to the claims that ground or contradict it.
- **141 code-grounded reviews of agent memory systems** — Mem0, Graphiti, Letta, Cognee, GBrain, and 136 more — classified on shared axes (storage substrate, lineage, behavioral authority, activation), plus [a comparative analysis of what the full matrix shows](../../agent-memory-systems/agentic-memory-systems-comparative-review.md). Code-grounded means we read the source, not the README.
- **Whole-system analyses** of agentic harnesses and orchestration layers — execution loops, control surfaces, learning loops.
- **A worked vocabulary** — distillation, constraining, codification, activation, deploy-time learning — so design conversations stop talking past each other.

Coverage today is deepest on the knowledge side of agentic systems: how agents get context, keep memory, learn from deployment, and fail. New areas are being added; the catalogue grows the way it was built — one reviewed claim at a time.

## An interactive textbook that lives in your repo

A textbook's failure mode is the shelf: the knowledge exists, but it's nowhere near the context window when the design decision gets made. This one installs where the decisions happen. Add it **inside** your repo — a git submodule, or a plain clone plus one `.gitignore` line — and put one routing line in your project's `CLAUDE.md` or `AGENTS.md`: *"For design decisions about agent context, memory, or learning, consult the knowledge base in `commonplace/kb/` first — start at `commonplace/kb/notes/tags-README.md`."* That's the whole integration. Inside the repo is load-bearing, not cosmetic: agent harnesses scope file access to the project root, so a sibling directory costs a permission prompt in every session, while a subdirectory is readable with none. Reading requires no tooling — the KB's commands and skills are for maintaining it, not consuming it. Plain markdown in git, written to be navigated by agents — claim-as-title headings, retrieval-oriented descriptions, curated indexes, typed links. No API, no service, no second runtime to trust.

Then it's interactive in three ways:

**Ask it.** Start from a design decision you're facing. Choosing a memory architecture? The comparative review shows that the real fork isn't storage format but [who decides what to remember, and whether memory ever reaches behavior](../../notes/knowledge-storage-does-not-imply-contextual-activation.md). Wondering why your agents don't improve? [Deploy-time learning is the missing middle](../../notes/deploy-time-learning-is-the-missing-middle.md) between retraining and prompting. Betting on in-context learning? [It presupposes context engineering](../../notes/in-context-learning-presupposes-context-engineering.md) — the selection machinery is the actual system. New to the field? [Follow the reading path](./textbook-syllabus.md) — a curated spine through the graph, one hour end to end.

**Point it at your code.** This is the move no paper textbook, course, or docs site can make: your agent holds the textbook and your codebase in the same context. "Does our memory design have [the cross-contamination failure the flat-memory note predicts](../../notes/flat-memory-predicts-specific-cross-contamination-failures-that-are.md)?" is now an answerable question about *your* system, with citations on one side and your source files on the other. The textbook reads your homework.

**Argue with it.** Every claim is stated to be contestable, carries its grounding, and marks its own confidence — seedling to current. If your production experience contradicts a note, that's not an attack on the textbook; that's how it gets its next edition. Open an issue.

## Why trust a catalogue

Because you can audit it. Every artifact here passed typed validation and review before it landed, every change to it is a git diff, and every claim links to what grounds it. The system reviews are grounded in source code you can go read. Where a claim is still speculative, its status says so — you always know what's load-bearing and what's a seedling.

And because the catalogue is used the way it recommends: this knowledge base is maintained by AI agents following a methodology that is itself part of the knowledge base. The comparative analysis of 141 memory systems was mostly agent-produced — an agent traversing linked reviews and finding the pattern. The catalogue about making agents knowledgeable is produced by agents made knowledgeable by it.

## Who this is for

Teams building agentic systems who are past the demo stage: you're deciding memory architecture, context strategy, or how your agents should learn from deployment, and you'd rather start from general formulations of the problem than rediscover it in production. Read first, no buy-in required.

If the catalogue proves useful and you want your *own* domain captured this way — your operational knowledge, typed, linked, review-gated, maintained by your agents — that's [Commonplace, the framework this knowledge base runs on](https://github.com/zby/commonplace).

---

[Read the comparative review →](../../agent-memory-systems/agentic-memory-systems-comparative-review.md)
[Browse by topic →](../../notes/tags-README.md)
[Browse the system reviews →](../../agent-memory-systems/README.md)
