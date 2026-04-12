# The LLM-specific angle

## Scope of the framing: open

The current commitment below is to derive each sub-discipline *for LLMs*. This scope is under active reconsideration and the workshop treats it as provisional.

The tension:

- **Broad framing** — The KB is LLM-operated, but the *value* of the knowledge it produces may be more general. Principles like reach, compression, load-time justification, and nameability-as-existence apply to any reader with bounded attention, not only to LLMs. On this framing the LLM is a **derivation context** — a stress test / limiting case that strips away human fallbacks (memory, perception, practice) and makes the structural core of knowledge management visible — rather than a scope limit on the resulting claims. The workshop would then produce general knowledge-management claims, with the LLM case cited as the sharpest test rather than as the audience. More ambitious. More honest about how the claims actually generalize. Opens the KB to human readers without footnotes.

- **Narrow framing** — Scoping every claim to LLM consumers keeps the workshop internally consistent. We never have to ask "does this transfer?" — the answer is always "out of scope." Cleaner, tighter, more immediately practical. Risks alienating human readers and pretends the derivation context is the scope.

- **Current lean** — toward the broad framing (it makes the work more universal and matches how the claims actually generalize), with the acknowledgement that the narrow framing may be more practical in the short term. The cost of the broad framing is the discipline of mapping each claim's reach explicitly, the same discipline `brainstorming-how-reach-informs-kb-design.md` already asks for.

**Resolution — deferred.** The choice is left open until the workshop has produced enough concrete claims to see which framing the claims themselves want. If most claims transfer cleanly, the broad framing was right and the narrow scope was underselling. If most claims turn out to be genuinely LLM-specific, the narrow framing was right and the broad one was over-ambitious.

**Working rule until resolved.** The angle document below commits to the narrow phrasing (*epistemology for LLMs*, etc.) as the working posture, but claims are to be tagged as they emerge:

- **llm-specific** — genuinely doesn't transfer (token bounds, no-weight-updates, session boundaries)
- **bounded-attention-general** — holds for any reader with bounded attention; LLM case sharpens it but doesn't own it
- **general** — transfers freely; the LLM case was just where we happened to notice it

The distribution of tags across concrete claims will tell us which framing the work actually supports, and the resolution can be made empirically rather than by upfront commitment.

## Commitment

This workshop does not borrow general philosophical theories of knowledge, being, and action wholesale. Philosophy has deep traditions in all three areas, but the LLM context changes the questions enough that classical answers don't translate directly.

Instead, the three content registers are treated as three **LLM-specific sub-disciplines**:

| Layer | Sub-discipline | Governs |
|---|---|---|
| Theory | **Epistemology for LLMs** | What can be known, how claims are justified, what transfers across contexts |
| Description | **Ontology for LLMs** | What exists in a system the agent can only read about, what counts as an entity, how identity survives change |
| Prescription | **Praxeology for LLMs** | What counts as action for an agent, how rules work for something that reads them fresh every time |

## Why this framing is the right one

The three classical sub-disciplines (what-can-be-known / what-exists / how-to-act) map onto the three content registers almost exactly. That's unlikely to be an accident — it suggests the content layering in a KB is tracking the same structure that forces philosophy into these three areas. Any system that reasons, represents, and acts in the world ends up needing all three, and needs them to be distinguishable.

But the LLM shifts every question:

- An LLM has no persistent memory between sessions. Knowledge that isn't in-context is functionally absent.
- An LLM doesn't perceive systems directly. What "exists" for it is what is nameable and retrievable.
- An LLM doesn't internalize habits. It executes rules it has just read.

So the classical questions arrive reshaped.

## Epistemology for LLMs

Classical: *What is knowledge? What justifies belief? What makes a claim true?*

Reshaped for LLMs:

- What counts as knowledge for an agent that will only see a subset of it, and which subset matters?
- When is a claim **transferable** across contexts the agent will encounter? (Deutsch's *reach* is an epistemology-for-LLMs concept. It measures how many future contexts one compressed claim serves.)
- What is justification, when the agent cannot re-derive under budget? (Probably: cached trust — trust in a source, trust in an argument structure that survives truncation.)
- How does context compression interact with truth preservation? When does distillation lose the thing that made the claim true?
- What breaks silently when a high-reach claim is revised? (This is the maintenance-asymmetry observation from `brainstorming-how-reach-informs-kb-design.md`.)
- What is a belief, for an agent whose beliefs are literally the tokens currently loaded?

Sample concepts that may need invention: *context-resident knowledge*, *load-time justification*, *compression-preserving vs compression-breaking claims*.

## Ontology for LLMs

Classical: *What exists? What are the categories of being? What makes X the same X over time?*

Reshaped for LLMs:

- What exists in a system, for an agent that only reads about it, is what can be **named** and **loaded**. Nameability is existence.
- What are the right categories for carving up a system the agent doesn't perceive directly? Type systems are an ontology choice.
- How does identity work across refactors? (A function is "the same function" if call sites still resolve. A note is "the same note" if its links still point to it. Identity is maintained by the referencing graph, not by internal continuity.)
- What's the right granularity of named things — one file, one symbol, one subsystem? Granularity determines what can be referenced.
- What does "complete" mean for a description? Completeness is relative to the query set the agent will actually run.
- What is existence-by-description vs existence-by-execution? The agent experiences the system through its documentation; the real system may differ.

Sample concepts that may need invention: *retrieval-grounded existence*, *reference-maintained identity*, *query-relative completeness*.

## Praxeology for LLMs

Classical: *What is rational action? What are the general patterns of efficient work?*

The strongest precedent here is **Kotarbiński's praxiology** (Polish school, *Traktat o dobrej robocie*, 1955), not Mises. Kotarbiński explicitly theorized the general structure of efficient action — economization, instrumentation, the preparation / execution split, typical errors of action — rather than treating action as a sub-topic of economics. That framing fits tool-using agents better than any other philosophical tradition we know of.

Reshaped for LLMs:

- What is an action, for an agent that acts only by emitting text and calling tools?
- How does means-end reasoning happen within a single context window? (Means must also be context-resident.)
- What is a rule, for an agent that must read the rule every time it applies? (Rules must be *short enough to load* and *unambiguous on first reading* — no appeal to practice.)
- Why does instruction specificity matter more than in human praxeology? Because no internalization — the agent never gets "used to" a rule.
- What's the analogue of a habit? Probably: always-loaded context. Habits live in the loading hierarchy, not in weights.
- What are the typical errors of LLM action — tool-loop drift, under-specified goals, over-general instructions, cargo-cult procedure following — and are they covered by existing praxeological concepts, or do they need new ones?
- What does *economization* mean when the scarce resource is tokens, not time or energy?

Sample concepts that may need invention: *read-time rule following*, *tokenized economization*, *loadable habits*, *instruction-as-action*.

## What this commits us to

1. **Read classical philosophy selectively.** The parts that keep their meaning when knowledge is context-loaded rather than head-stored — those are useful. Parts that assume internalization, perception, continuity of self — those need to be rewritten, not copied.
2. **Invent concepts where the classical ones break.** Don't force-fit. Naming a gap is progress.
3. **Resist merging the three disciplines.** They govern different layers, with different quality criteria. Epistemology evaluates theories on reach. Ontology evaluates descriptions on fidelity. Praxeology evaluates prescriptions on executability. Mixing them is what produces the current confusion about what WRITING.md should contain.
4. **Tie back to the linking topology.** The asymmetry (theories don't link down) should be derivable from the sub-disciplines: an epistemological claim that depends on a particular ontology has leaked between layers and becomes unstable. Ideally the linking rules fall out of the disciplines rather than being stipulated.

## Open questions

1. **Is there a fourth sub-discipline we need?** Ethics / values? The `KB Goals` section of commonplace is normative — is that a fourth layer (axiology) or a sub-part of praxeology?
2. **Where does logic sit?** Logic governs inference across all three registers. Is it a foundation, a cross-cut, or its own layer?
3. **Where does philosophy of language sit?** Meaning, reference, speech acts cut across all three. Speech-act theory in particular maps suspiciously well onto the theory/description/prescription split (assertive / representative / directive).
4. **Can praxeology-for-LLMs ground in Kotarbiński?** Or do we need to develop it mostly from scratch, using Kotarbiński as a structural precedent rather than a source of claims?
5. **Does the linking asymmetry have a classical analogue?** Candidates: Hume's is/ought gap, the autonomy of the theoretical from the practical, Carnap's framework-relativity. If one of these fits, it strengthens the case that the three-layer structure is real and not parochial.
6. **If the broad framing wins, what's the right name for the scope?** "For stateless readers," "for bounded-attention readers," "for documentation-mediated agents" are all candidates. Each carves differently. (See the *Scope of the framing: open* section at the top — this question only becomes live if that scope resolves broad.)

## Relation to the other workshops

- `philosophy-borrowing/` is already evaluating Peirce, Quine, Carnap, speech act theory. This workshop's commitment says: don't import, re-derive for LLMs. Philosophy-borrowing should probably be re-scoped accordingly, or at minimum coordinate on what "borrowing" means here.
- `system-documentation/` is the commonplace-specific instance. Once the three disciplines are named, that workshop's conclusions should re-derive cleanly.
