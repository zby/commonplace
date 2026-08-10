# DSW talk — working outline and material selection

Imported conclusions from the planning session that scanned the KB. The talk is tighter than Commonplace itself: one practitioner story, with deeper theory only where it explains a design decision.

## Core claim

LLMs make it cheap to develop a knowledge base continuously, not merely search or summarize it. Reliability comes from a hybrid design: generated knowledge stays reviewable, stable and checkable rules move into deterministic machinery, and retrieval loads only what the current task needs.

The talk earns this claim through two observed Commonplace cases rather than a tour of its architecture or vocabulary. The vibe-noting case shows both useful semantic development and fluent failure. The tag-README case shows a trusted navigation promise becoming executable, reducing later retrieval work, and changing the system that produced it.

## Proposed 35-minute outline

| Time | Section | What happens |
|---|---|---|
| 0–3 min | Not search, but development | Open with the raw observation that became the vibe-noting note. An LLM-operated KB can preserve a thought and help develop it, not merely retrieve it later. State the short thesis; do not explain the architecture yet. |
| 3–8 min | Case 1: what the model added | Show the raw observation beside the first candidate artifact. Point to the useful additions: an explicit claim, a scope boundary, implications, and connections that make the thought inspectable beyond its original session. |
| 8–13 min | Case 1: fluency is not certification | Show the three later corrections: an omitted negative-compounding risk, an overstated grounding claim, and a reversed link mapping. Name reverse compression only after showing the failure. Use inspectability versus verifiability to explain why persistent artifacts improve augmentation without making semantic verification easy. Unresolved judgment returns to a human. |
| 13–19 min | Case 2: when a rule becomes software | A topical navigation page had grown to 18.8 KB and 55 entries, beyond credible manual maintenance of a completeness promise. Show the move from prose convention to explicit `complete`/`covered_by` marks and validator enforcement. The resulting check later exposed a member that the documented search recipe missed. Be explicit that a human noticed the original strain; the validator prevents silent recurrence rather than having discovered the problem. |
| 19–24 min | The KB must leave room for the task | Continue the same case: because a completeness claim is checked, later agents may safely stop searching that route. Generalize to descriptions, indexes, links, search, and progressive disclosure. Introduce the operational maxim: “Write for reuse; load for the task.” |
| 24–28 min | Self-hosting closes the loop | Trace the observed loop: operational strain → retrieved prior knowledge → revised type and methodology → schema and validator → changed validation and agent search behavior. Reveal the final feedback arrows in the visual spine. Do not introduce reflection or self-improvement vocabulary. |
| 28–30 min | Four things to try next week | Restate the four practices as actions. Then state the limits: semantic verification remains weak, full autonomous KB learning is unsolved, and Commonplace has not demonstrated recurrent autonomous compounding. End with the possibility of a notebook that improves how knowledge gets developed. |
| 30–35 min | Deliberate timing slack | Leave room for examples, pauses, transitions, and audience reaction. Do not fill this space with another concept. |

Design for about 29–30 minutes of authored material. The two concrete cases are the talk, not optional illustrations, so rehearsal variance belongs inside the remaining time.

## The four practitioner lessons (recurring structure of the middle)

1. **Use the LLM to develop knowledge, not merely draft prose.** Ask it to retrieve, distinguish, propose claims, test scope, find implications, and connect ideas.
2. **Treat fluent output as a candidate, not a certificate.** Separate generation from review, preserve provenance, distinguish candidates from promoted knowledge, and keep important decisions reviewable.
3. **When a rule becomes stable and checkable, move it into software.** Progress from interpreted convention to explicit data and deterministic enforcement only after the rule is understood; keep genuinely ambiguous judgment with the model or human.
4. **Write for reuse; load for the task.** Make artifacts inspectable and navigable when they enter or change in the KB, then load only what the current task needs.

Introduce each lesson as the conclusion of a case segment. Do not present the four as an abstract framework before the audience has seen the evidence.

## The two worked cases

### Case 1: vibe-noting

Use four pieces of slide-ready evidence, not the whole note:

- The raw human observation about code as a persistent artifact and a KB extending that property to knowledge work.
- The first candidate's genuine additions: the inspectability claim, the distinction between augmentation and automation, and the relationship to weak verification.
- The three review corrections: missing negative compounding, overstated grounding, and a reversed link relation.
- The retained artifact after correction, which a later session can inspect without replaying the conversation.

The case supports both sides of the argument. The model did more than expand prose, but the fluency of its first result did not certify the semantic changes. Show the before, candidate, and reviewed delta on screen; do not describe an inventory of Commonplace review passes.

### Case 2: the tag-README change

Translate the internal artifact into an ordinary practitioner problem first: a navigation page claims to cover every item in a category, so readers stop searching when they trust it. That promise becomes dangerous when manual maintenance no longer scales.

Show the observed sequence:

1. The `learning-theory` index reached 18.8 KB and 55 entries. A human noticed the strain; no validator detected an existing completeness failure.
2. The design split curated navigation from build-time complete listings and made any retained completeness or coverage promise explicit through `complete` and `covered_by` fields.
3. The same decision reached natural-language instruction, schema, validator, renderer, and tests. A declared mark now gives the promise deterministic consequences.
4. The new check later caught a block-style YAML member that the documented `rg` recipe had missed, causing the documentation to change.
5. Validation now rejects states it previously accepted, while the connection workflow may skip an exhaustive tag search when a checked completeness mark is present.

This one case carries the software-enforcement, context-loading, and self-hosting sections. Do not introduce a second example for each mechanism.

## The context constraint

Keep context efficiency as a main lesson, but present only the practitioner-level claim. Instructions, task state, retrieved knowledge, and reasoning compete within the same model context. More stored knowledge therefore does not imply that more knowledge should be loaded.

State the LLM-wiki-specific constraint:

> A knowledge system that helps by filling the context with knowledge can destroy the capacity needed to use that knowledge.

Then define the operational response:

- **Write for reuse:** when knowledge enters or changes, make its claim, scope, provenance, and useful connections inspectable; validate its structure and review consequential semantic changes. Reusable does not mean long or self-contained.
- **Load for the task:** use descriptions, indexes, pointers, search, links, and progressive disclosure to initially expose where to look, then load only the material the current task requires.

The tag-README case joins the two sides: work performed on the write path makes a later stopping decision safe on the load path. “Write for reuse; load for the task” is a presentation-level synthesis, not a formal Commonplace theorem.

## Material triage against the KB

| Idea | Function in this talk | Treatment |
|---|---|---|
| Vibe-noting | Demonstrates useful semantic development and its failure mode in one artifact | Central case; show the raw observation, candidate, and three review corrections |
| Inspectability vs verifiability | Explains why a KB improves continuity without making semantic truth mechanically decidable | One small diagram after the vibe-noting corrections |
| Reverse compression | Names the observed expansion failure | Introduce after the example; do not teach epiplexity |
| Generation versus review | Explains why candidate production and acceptance are separate | Show the actual delta; do not list named review passes |
| Progressive constraining | Explains why the tag rule moved into software only once its truth conditions were understood | Teach through the tag-README sequence; do not use the vocabulary on stage |
| Natural-language and symbolic artifacts | States the hybrid end state: semantic judgment remains interpreted while stable bookkeeping becomes executable | Conclude the tag-README section with this contrast |
| Context efficiency and progressive disclosure | Turns the checked navigation claim into a practical retrieval benefit | Main section, grounded in the tag-README case |
| Workshop versus library and authority paths | Supports the candidate-versus-promoted distinction | Use the distinction without teaching the storage or authority taxonomy |
| Generated views versus source of truth | Appears inside the tag-README redesign | Mention only what the worked sequence requires |
| Self-hosting | Closes the observed loop from operational strain to changed future behavior | Include for four minutes; avoid reflection theory and compounding claims |
| External fluency critiques, automatic review applications, and the 148-system survey | Corroborating or adjacent material | Cut from the main narrative; retain for Q&A |
| Deploy-time learning, activation versus storage, and error-correction asymmetry | Deeper theoretical explanations | Keep in speaker notes and linked material; do not name on stage |

This selection keeps the presentation from becoming "20 cool things in Commonplace."

## Visual spine

One evolving diagram, returned to repeatedly. The branches matter: reusable knowledge is not normally converted into a validator. Only a stable, checkable rule moves into deterministic machinery, which then constrains future artifacts.

```
rough observation
  ↓ LLM develops a candidate
candidate artifact
  ↓ review; unresolved choices return to a human
reusable knowledge
  ├─ task-scoped loading → future task → new observations ─┐
  └─ stable, checkable rule                                │
       ↓                                                   │
     schema / validator ── constrains future artifacts     │
                                                             └→ rough observation
```

Build it in stages: the main artifact path during vibe-noting, the stable-rule branch during the tag-README case, the task-scoped branch during the context section, and the return arrow during the self-hosting close. At the end: *“Because Commonplace is self-hosting, sometimes the task producing the next observation is Commonplace itself.”*

## Deliberate exclusions

Do not explain the whole theory behind each design choice. In particular:

- Do not inventory the review system. One candidate and its three corrections establish the separation between generation and review.
- Do not catalogue failure concepts. Demonstrate the failure, then name reverse compression.
- Do not tour types, schemas, validators, and generated indexes. Trace one promise as it acquires deterministic consequences.
- Do not teach the feasibility-versus-cost model of context. State that loaded material competes with the task, then show task-scoped loading.
- Do not introduce deploy-time learning, computational reflection, or the autonomous-compounding theory.
- Do not use the agent-memory survey as supporting spectacle. It is another talk.

The audience takeaway: "I can apply these patterns to my own LLM knowledge system next week." For the subset who notice the patterns imply a deeper theory of persistent LLM systems, Commonplace itself is the rabbit hole. This balance fits the DSW CFP: a concrete case study full of implementation lessons, where the deeper theoretical work is what makes the lessons unusually coherent.

---

- [vibe-noting](../../notes/vibe-noting.md) — evidenced-by: the central worked example; its own history shows both the useful transformation and errors later caught in review
- [Reverse compression is when LLM output expands without adding](../../notes/reverse-compression-is-when-llm-output-expands-without-adding.md) — rests-on: the fluency trap in the 8–12 min section
- [The tag-README change as an observed causal-connection trace](../../reference/tag-readme-trace-observed-causal-connection.md) — evidenced-by: the second worked example and its verified implementation timeline
- [The tag-README trace read as a self-improving loop](../../reference/tag-readme-trace-as-self-improving-loop.md) — rests-on: the calibrated self-hosting close
- [Context efficiency is the central design concern in agent systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) — rests-on: the context-budget section
- [Agent context is constrained by soft degradation, not hard token limits](../../notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md) — see-also: deeper context model retained for Q&A rather than taught on stage
- [Constraining](../../notes/definitions/constraining.md) — defined-in: the convention → schema → validator progression shown through examples
- [Progressive constraining commits only after patterns stabilize](../../notes/progressive-constraining-commits-only-after-patterns-stabilize.md) — grounds: why validators arrive late, not first
- [Scheduler–LLM separation exploits an error-correction asymmetry](../../notes/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) — see-also: underlying rationale retained for Q&A
- [A functioning KB needs a workshop layer, not just a library](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — draws-on: candidate-versus-promoted distinction used without the taxonomy
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) — see-also: cut from the talk, kept for Q&A
- [Deploy-time learning is the missing middle](../../notes/deploy-time-learning-is-the-missing-middle.md) — see-also: deeper interpretation not named on stage
