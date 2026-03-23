=== PROSE REVIEW: subtasks-that-need-different-tools-force-loop-exposure-in-agent-frameworks.md ===

Checks applied: 8

WARN:
- [Confidence miscalibration] The note presents its own analytical framework — the claim that differing capability surfaces force loop exposure, that sub-agents are the "dominant mechanism," and that tool removal creates incoherence — using assertive language throughout. "This is not a bookkeeping problem that tool wrappers can absorb," "You cannot cleanly shrink a context's action alphabet," "That asymmetry is why sub-agents keep winning over in-place tool mutation." These are stated as established facts, but they are the note's own constructions. No sources are cited for any of these claims. The note's status is `seedling`, yet the prose reads as settled argument. The asymmetry claim about tool removal (models lose coherent reasoning about prior actions when tools disappear) is particularly strong — it asserts a specific failure mode of LLM cognition without grounding.
  Recommendation: Soften the strongest assertions to match the seedling status. "You cannot cleanly shrink a context's action alphabet" could become "shrinking a context's action alphabet is problematic because..." The tool-removal incoherence claim should either be grounded with a citation or example, or hedged as an observed tendency rather than a categorical impossibility.

- [Proportion mismatch] The note's title claim is about subtasks with different tools forcing loop exposure. The core argument for this — paragraphs 1-3 (capability surfaces differ, this requires fresh calls, framework-owned loops respond awkwardly) — gets roughly 150 words of development. The tool-removal discussion in paragraph 5 ("A programmer may want to change the tool surface mid-task...") gets roughly 130 words and introduces a substantially different argument (dynamic tool mutation within a single task, not cross-subtask dispatch). The tool-removal asymmetry argument is interesting but it is a second, independent reason for sub-agents, not a development of the title claim. It receives nearly equal treatment to the title's core argument, which dilutes the note's focus.
  Recommendation: Consider whether the tool-removal asymmetry argument belongs in a separate note (e.g., "removing tools from an active context creates incoherence that addition does not"). The current note could then link to it as supporting evidence. Alternatively, if keeping it here, make the structural relationship explicit: "Beyond cross-subtask dispatch, there is a second force that favors sub-agents..."

INFO:
- [Source residue] The examples in paragraph 2 — "A research child may need `{search, summarize}`. An implementation child may need `{read_file, patch_file, run_test}`. A review child may need `{read_file, compare, submit_review}`" — are drawn from software-engineering agent workflows. The note's title and framing claim generality about "agent frameworks" broadly, not specifically coding agents. These examples are not explicitly framed as illustrative ("for instance," "in a typical software workflow"); they read as the canonical case. This is mild — the examples are plausible and readable — but a reader working on, say, a multi-step data-analysis agent or a dialogue agent would need to do the mapping themselves.

- [Redundant restatement] The final paragraph partially restates the conclusion already reached in paragraph 4 ("The clean response is to spawn a sub-agent..."). Paragraph 6 opens with "So loop exposure is the general property" and then re-derives why sub-agents win, covering ground already established. The new content in paragraph 6 — the framing of "the decisive question" — is genuinely additive, but it is wrapped in restatement of prior conclusions. This is mild because the paragraph also serves as a summary that pulls the two threads (cross-subtask dispatch and tool removal) together.

CLEAN:
- [Pseudo-formalism] No formal notation, equations, or variable names are used. The note uses informal set notation (`{search, summarize}`) purely as compact enumeration of tool names, which is appropriate shorthand rather than pseudo-formal apparatus.

- [Orphan references] No unsourced empirical claims, specific numbers, percentages, or named studies appear. All claims are analytical rather than empirical. The note avoids making grounding-dependent assertions.

- [Unbridged cross-domain evidence] No cross-domain evidence is cited. The note's claims stay within the agent-frameworks domain throughout. The linked notes are in the same domain.

- [Anthropomorphic framing] The note uses "The model has memories of calling those tools" in paragraph 5, which borders on anthropomorphic ("memories"). However, in context this refers to the literal conversation history containing prior tool-call records, not to a human-like memory faculty. The rest of the note uses precise technical language: "the model sees new affordances," "attempt to call them again," "lose coherent reasoning." These describe observable behavior rather than attributing mental states. The "memories" usage is defensible but worth noting — "the conversation history contains records of calling those tools" would be more precise.

Overall: 2 warnings, 2 info
===
