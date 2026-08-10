# DSW talk — working outline and material selection

Imported conclusions from the planning session that scanned the KB. The talk is tighter than Commonplace itself: one practitioner story, with deeper theory only where it explains a design decision.

## Core claim

LLMs make it cheap to continuously develop a knowledge base, not merely search or summarize it. But because fluent generation can turn weak thinking into convincing artifacts, the useful system is a hybrid: LLMs do semantic work, deterministic machinery enforces what can be formalized, and context is carefully budgeted so the knowledge system does not displace the task it is supposed to help.

This incorporates the strongest material without making self-improvement, agent memory, context theory, and reflective systems separate topics.

## Proposed 35-minute outline

| Time | Section | What happens |
|---|---|---|
| 0–3 min | The LLM-wiki promise | Start with the simple idea: a wiki that an LLM can read, write, organize, connect and maintain. Traditional note-taking leaves huge amounts of maintenance to the human. LLMs radically lower this cost. |
| 3–8 min | The surprising part: developing ideas | The biggest value wasn't automatic filing. Show a real rough observation from Commonplace becoming something more explicit. For theory collections, the key representation is the claim: vague thought → candidate claim → scope → connections → criticism → revision. Clarify that not all Commonplace notes are claims. |
| 8–12 min | The trap: fluent writing can fake progress | Boretti, reverse compression, sycophancy, premature coherence. One sentence can become five polished paragraphs without gaining useful structure. The problem isn't just hallucination: the LLM can make unfinished thinking look finished. The vibe-noting note is the example — its own history demonstrates both the useful transformation and errors later caught in review. |
| 12–18 min | First response: put pressure on semantic changes | The improvement-pass idea. Generation and certification are separate. Compression review asks whether the artifact earns its context cost; semantic review checks grounding/consistency; critique attacks the claim; composition-friction tries concretization; connection-finding tests how it fits the rest of the KB. Some uncertainty is intentionally routed back to the human rather than automatically "resolved." |
| 18–23 min | Second response: stop using the LLM where software can do better | Typed artifacts, schemas, validators, structural requirements, generated indexes. The rule: don't ask the LLM to remember what you can check. Show the progression natural-language convention → structured field → schema → validator/code. This is the constraining spectrum in practical form, taught through examples, not vocabulary. |
| 23–28 min | The context-budget problem | The wiki itself competes with the user's task for the same context window, so "load the KB" is the wrong architecture. Read and write paths, selective retrieval and progressive disclosure: small routing information first, deeper material only when needed. Context feasibility is the binding constraint; instructions, user task, knowledge and reasoning compete for one attention budget. |
| 28–32 min | Why self-hosting matters | Commonplace is used to research and improve Commonplace. Its own failures generate observations; those become knowledge and sometimes methodology, schemas or validators; later agents operate under the revised system. Self-hosting turns the KB into a laboratory for these patterns. Do not introduce the full reflective-self-improvement theory. |
| 32–35 min | What we learned / boundaries | Summarize the engineering patterns and be explicit about what remains unsolved: semantic verification is weak, full autonomous KB learning is not solved, and Commonplace has not demonstrated recurrent autonomous compounding. End with the larger possibility: a notebook that helps improve not only what you know, but how your knowledge gets developed. |

Design for about 31–32 minutes of authored material — concrete examples always take longer than expected.

## The four practitioner lessons (recurring structure of the middle)

1. **Give the LLM semantic work, not just writing work.** Retrieve, distinguish, propose claims, find implications, challenge scope, connect ideas.
2. **Don't trust fluency as evidence of progress.** Use separate semantic pressures, preserve provenance, distinguish drafts from promoted knowledge, keep important decisions reviewable.
3. **Don't ask an LLM to enforce what software can check.** Types, schemas, structural validators, generated indexes and deterministic checks progressively remove bookkeeping from the model.
4. **Don't let the knowledge machinery consume the task's context.** Make the write side rich and the read side selective; use routing, indexes, links and progressive disclosure rather than front-loading the KB.

## The context-efficiency section stays a main section

Promoted from optional detail to one of the four engineering lessons. The strongest KB formulation: context isn't merely a cost — it has a feasibility face. As the usable context fills, competence can degrade, and you cannot necessarily compensate by paying for more inference. Unlike a normal computer with memory hierarchies, instructions, task state, retrieved knowledge and reasoning all occupy the same model context.

The LLM-wiki-specific constraint, stated memorably:

> A knowledge system that helps by filling the context with knowledge can destroy the capacity needed to use that knowledge.

So the architecture optimizes both sides:

- **Write path:** do the expensive work when knowledge enters or changes — turn raw material into inspectable artifacts, add metadata and links, validate structure, review semantic changes.
- **Read path:** make consumption cheap — indexes, descriptions, pointers, search, links and progressive disclosure let the agent initially see *where to look* rather than loading everything.

Presentation-level maxim, companion to the validator maxim: **"Write rich; read selectively."** This is a synthesis of several KB ideas, not a formal Commonplace theorem — do not present it as one.

## Material triage against the KB

| Idea | Value for this talk | Recommendation |
|---|---|---|
| Inspectability vs verifiability | Excellent — explains why a KB can improve augmentation even though knowledge work lacks code-like tests; vibe-noting separates the two axes | Include, probably one diagram during the failure/review section |
| Context efficiency / progressive disclosure | Excellent and directly relevant to using an LLM wiki in practice | Include as a main section |
| Constraining / codification gradient | Explains why schemas and validators are not random hacks | Include implicitly through concrete examples; don't teach the vocabulary |
| Natural language + symbolic artifacts as hybrid end state | Strong — judgment vs bookkeeping; NL and code co-evolve rather than everything becoming code | Include as the conclusion of the validator section |
| Workshop vs library | Very relevant to avoiding premature promotion; rough work has weaker authority than durable knowledge | Mention briefly as one practical trick |
| Authority and promotion paths | Strong theoretically: observations shouldn't silently become claims, claims shouldn't silently become instructions or validators | Use the idea without the taxonomy |
| Generated views vs source of truth | Great engineering practice: indexes/matrices rebuildable from canonical artifacts | One concrete example in the deterministic-machinery section |
| Deploy-time learning | Powerful explanation of why durable NL and symbolic artifacts matter across sessions | Don't name it until the closing — it opens another theoretical branch |
| Self-hosting / reflection / compounding | Distinctive; evidence supports installed/reused revisions but not recurrent compounding | 3–4 minutes near the end |
| 148-system agent-memory survey | Strong evidence, interesting on its own | Mostly cut — one sentence that broader survey work reinforced the context-efficiency concern; this is another talk |
| Automatic structured reviews | Good evidence that LLMs can do constrained semantic transformations | Cut from main narrative; Q&A or one "other applications" sentence |
| Raw accumulation is not usable memory / activation vs storage | Deep, but shifts the talk toward agent-memory architecture | Cut unless needed for a question |
| Error-correction asymmetry / symbolic scheduler model | Strong theory for why bookkeeping belongs outside the LLM | Underlying rationale only; don't derive it on stage |

This selection keeps the presentation from becoming "20 cool things in Commonplace."

## Visual spine

One evolving diagram, returned to repeatedly:

```
rough human thought
  ↓ LLM semantic transformation
candidate artifact
  ↓ semantic pressure / review
reviewed knowledge
  ↓ constrain what is mechanically understood
schema / validator / generated machinery
  ↓ selective read path
small relevant context for a future task
  ↓ task produces new observations
back into the system
```

At the very end, animate the last arrow back to the top: *"Because Commonplace is self-hosting, sometimes the task being improved is Commonplace itself."* The self-improvement angle then appears as the natural closure of the talk rather than as a second thesis.

## Deliberate exclusions

Do not explain the whole theory behind each design choice. Say context is scarce, therefore progressive disclosure — without the computational model of bounded LLM calls. Show stable constraints migrating into validators — without the full theory of representational-form co-evolution. Show the self-hosting loop — without defining computational reflection.

The audience takeaway: "I can apply these patterns to my own LLM knowledge system next week." For the subset who notice the patterns imply a deeper theory of persistent LLM systems, Commonplace itself is the rabbit hole. This balance fits the DSW CFP: a concrete case study full of implementation lessons, where the deeper theoretical work is what makes the lessons unusually coherent.

---

- [vibe-noting](../../notes/vibe-noting.md) — evidenced-by: the central worked example; its own history shows both the useful transformation and errors later caught in review
- [Reverse compression is when LLM output expands without adding](../../notes/reverse-compression-is-when-llm-output-expands-without-adding.md) — rests-on: the fluency trap in the 8–12 min section
- [Context efficiency is the central design concern in agent systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) — rests-on: the context-budget section
- [Agent context is constrained by soft degradation, not hard token limits](../../notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md) — grounds: the feasibility face of context
- [Constraining](../../notes/definitions/constraining.md) — defined-in: the convention → schema → validator progression shown through examples
- [Progressive constraining commits only after patterns stabilize](../../notes/progressive-constraining-commits-only-after-patterns-stabilize.md) — grounds: why validators arrive late, not first
- [Scheduler–LLM separation exploits an error-correction asymmetry](../../notes/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) — rests-on: underlying rationale for the deterministic-machinery lesson (not derived on stage)
- [A functioning KB needs a workshop layer, not just a library](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — draws-on: the workshop-vs-library practical trick
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) — see-also: cut from the talk, kept for Q&A
- [Deploy-time learning is the missing middle](../../notes/deploy-time-learning-is-the-missing-middle.md) — see-also: named only in the closing, if at all
