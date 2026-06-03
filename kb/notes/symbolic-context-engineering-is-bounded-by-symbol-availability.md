---
description: "Symbolic context selection — matching on type, path, tag, tool, or event — can act only on an already-observable symbol; an operation's identifying symbol arrives by declaration, by the operation naming it, or by carryover from a prior one, so apparent anticipation is reaction to an earlier symbol. Producing context with no symbol available requires semantic inference."
type: kb/types/note.md
traits: [title-as-claim]
tags: [context-engineering, agent-memory]
status: current
---

# Symbolic context engineering is bounded by symbol availability
By _symbolic_ context engineering I mean **selecting what to load by matching codified features** — a type, path, tag, link label, tool name, event, or task mode — rather than _semantic_ selection by embedding similarity or an LLM judgment. It is attractive for the usual [codification](./definitions/codification.md) reasons: deterministic, cheap, reviewable. The symbol that matters throughout is the one identifying *this* instance — the discriminator for the specific destination, type, or task at hand; a coarse, always-present symbol such as a `Write` event routes only generic guidance and cannot stand in for it.

The bound is easiest to see in a concrete case. To write a note into a Commonplace collection — a `kb/` subtree with its own `COLLECTION.md` authoring contract and type spec — the system needs that contract, but it cannot load it until it knows _which_ collection and type. Often these are already declared — a user-supplied path, a target note, existing frontmatter — and the contract loads cleanly; the hard case is a fresh write where no destination or type has been fixed, because then they are settled only by the write the agent has not made yet. The general shape: a symbolic selector can act only on a symbol it can already see, and the symbol identifying _this_ instance is produced by the very operation the loading was meant to serve, so it does not exist until the agent emits it.

Symbolic selection is therefore **reactive**: it never fires for an instance it has no symbol for. A symbol can become available _early_, which makes some selection look like anticipation; it never anticipates the instance at runtime, because the symbol was emitted before the operation by one of three routes:

- the user or agent **declares** it — a session mode, an explicit target;
- a **prior operation** leaves it and its context already loaded;
- earlier **semantic** work compiles relevance into symbolic metadata — tags, a route table, a generated index — that later selection keys on.

That third route is genuine anticipation, but design-time — already completed before the symbolic selector runs.

The one thing it cannot do is produce context for an instance with *no* symbol — that requires inferring which instance it is, which is the semantic regime: embedding search or a side LLM call, fallible and costlier. In practice the two compose, symbolic features narrowing a candidate set that semantic ranking then orders.
## Where it shows up
The write path also illustrates the three routes and the discipline they imply: `cp-skill-write` runs no active discovery — link candidates come only from already-observable surfaces (the destination `dir-index.md`, loaded context, user-named targets), with active prospecting deferred to `cp-skill-connect` — and the collection symbol it needs arrives up front, just in time, or already-loaded from a prior write.

Memory systems that "push" before a query confirm the bound from the other side. [CrewAI](../agent-memory-systems/reviews/crewai-memory.md) and [REM](../agent-memory-systems/reviews/REM.md), two framework memory layers, inject only after a framework event hands them a payload — often the current query or task text — never from nothing. EQUIPA, a multi-agent orchestrator, shows the middle path: symbolic features narrow a set that semantic signals then rank. Pull-only tools like [cq](../agent-memory-systems/reviews/cq.md) and [Binder](../agent-memory-systems/reviews/binder.md) reach the agent only when called.
## Making a symbol available early
The practical question is how to emit the identifying symbol _before_ the operation, cheaply.

- **Durable task frames** carry a declared scope ahead of time — a saved report definition, a document-local contract (a Commonplace note's `type:` frontmatter names its governing type spec the moment the file is opened), a workflow mode, a session focus. Invoking or scheduling the frame lets the selector react to a scope declared earlier, distinct from both semantic retrieval and chat predeclaration; the scheduled report definitions in Atomic, a memory system whose saved reports run on a cron schedule, are the clearest case.
  
- **A rich interface** is itself such a frame: a GUI/TUI picker or mode toggle emits the symbol out-of-band, which is why the ceremony of predeclaring is mostly an artifact of single-channel chat. Absent a frame, just-in-time wins.
  
- **An evolved baseline** — core memory, playbooks, generated indexes, exported skills, or [always-loading a bounded set](./always-loaded-context-mechanisms-in-agent-harnesses.md) — doesn't beat the limit but lowers how often runtime selection is needed, moving the cost to standing context.
  
## Scope
An always-present symbol (an action-type trigger on any `Write`) buys only coarse relevance, not what this instance needs. None of this condemns symbolic selection — reliable selection once a symbol exists is what symbols are for. The bound is exact: selecting for an instance with no available symbol is the part out of reach.
## Relevant Notes
- [knowledge storage does not imply contextual activation](./knowledge-storage-does-not-imply-contextual-activation.md) — grounds: the activation gap this sharpens into a constraint on symbolic selection
  
- [agent statelessness means the context engine should inject context](./agent-statelessness-means-the-context-engine-should-inject-context.md) — contrasts: its open "how to identify what to inject" question — symbolically, only once a symbol is available
  
- [codification](./definitions/codification.md) — defined-in: symbolic context engineering is the codified selection regime whose reach this bounds
  
- [frontloading spares execution context](./frontloading-spares-execution-context.md) — contrasts: frontloading uses inputs known upstream of the call; this characterizes when the identifying symbol is or isn't upstream yet
  
- [agentic memory systems comparative review](../agent-memory-systems/agentic-memory-systems-comparative-review.md) — evidence: the cross-system push/pull split this generalizes
  
- [EQUIPA](../agent-memory-systems/reviews/equipa.md) — evidence: symbolic narrowing feeding semantic ranking, the mixed middle path
  
- [Atomic](../agent-memory-systems/reviews/atomic.md) — evidence: report definitions as the durable-task-frame case
