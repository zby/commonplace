=== PROSE REVIEW: memory-management-policy-is-learnable-but-oracle-dependent.md ===

Checks applied: 8

WARN:
- [Confidence miscalibration] The note presents its own analytical frameworks as established fact rather than proposed interpretation. "Memory management decomposes into selection and distillation" (takeaway 1) is the note's own mapping of AgeMem operations onto KB vocabulary, but it is stated as a discovery ("What AgeMem teaches us"). Similarly, "Composition policy is the hard part" (takeaway 2) asserts a general principle from one system's results. The reach-gradient analysis ("None of this produces knowledge with reach") and the classification of LTM Add as "accumulation at the low-reach end" are the note's own theoretical framing applied to AgeMem, not claims AgeMem itself makes.
  Recommendation: Reframe takeaways as proposed interpretations: "AgeMem suggests that memory management decomposes into..." or "One reading of AgeMem's results is that composition policy is the hard part." In the body, flag the reach-gradient analysis as the note's interpretation: "In this KB's terms, AgeMem's LTM Add is accumulation at the low-reach end" (which the note partly does, but inconsistently).

- [Proportion mismatch] The core claim is in the title: memory management policy is learnable but oracle-dependent. The oracle-dependence argument ("Why it works: the oracle") gets one short paragraph. The substrate comparison ("How it stores what it learns: split substrate") gets three substantial paragraphs, and the comparison section ("Comparison to KB learning") gets three more. The oracle section carries the title's load but is the thinnest section in the note. The split-substrate discussion, while valuable, is a secondary observation that dominates the note's real estate.
  Recommendation: Develop the oracle section — it currently states that task completion is a clear signal but doesn't explore what makes an oracle "clear" in general terms (binary vs. graded, immediate vs. delayed, intrinsic vs. extrinsic). This would strengthen the title claim and make the comparison section's "the KB lacks an oracle" argument more precise.

INFO:
- [Source residue] The note is about AgeMem and explicitly frames itself as an analysis of that system, so AgeMem-specific terminology (ALFWorld, HotpotQA, GRPO, step-wise advantage broadcasting) is expected. However, the phrase "boiling cauldron" appears twice ("the boiling cauldron's mutations," "the boiling cauldron's 'mutations differ on two axes' analysis") without introduction or link. A reader encountering this note without prior context would not know what the boiling cauldron refers to. This is residue from the KB's internal vocabulary rather than from the AgeMem source.
  Recommendation: Either link "boiling cauldron" to its defining note or replace it with a brief inline explanation on first use.

- [Anthropomorphic framing] The note uses "AgeMem learns," "AgeMem succeeds," and "AgeMem confirms" throughout. Since AgeMem is a system (not a model), attributing learning and success to it is standard engineering language. One borderline case: "the LLM's own instruction-following attempts" — this is precise enough (instruction-following is a behavioral description). No action needed, but flagging for awareness.

CLEAN:
- [Pseudo-formalism] No formal notation, equations, or symbolic apparatus appears in the note. The analysis is conducted entirely in prose. The note uses bold text for emphasis but not as pseudo-formal decoration. Check passes cleanly.

- [Orphan references] Specific numbers are cited with clear provenance: "23-49% improvement" and "8-9 percentage points" come from AgeMem (linked in the opening). "Add operations from 0.92 to 1.64 per episode" is attributed to post-training AgeMem agents. "Six memory operations" are named explicitly. All empirical claims trace to the linked ingest. No orphan figures detected.

- [Unbridged cross-domain evidence] The note's evidence comes from AgeMem (a machine learning system) and is applied to KB design (also a machine learning/knowledge management domain). The note explicitly bridges the transfer in the "Comparison to KB learning" section by naming what transfers and what doesn't: "AgeMem's policy learns which facts help complete tasks. The KB needs a policy that learns which connections help answer questions that haven't been asked yet." The note also flags where the analogy breaks down. No unbridged transfers detected.

- [Redundant restatement] Sections open with new content rather than restating prior conclusions. "What it accumulates: facts without reach" does not re-explain the policy/operations distinction from the prior section. "Comparison to KB learning" introduces the oracle gap rather than restating what the oracle is. The note reads as a progressive argument without redundant bridges.

Overall: 2 warnings, 2 info
===
