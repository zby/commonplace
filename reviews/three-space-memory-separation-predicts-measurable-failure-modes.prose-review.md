=== PROSE REVIEW: three-space-memory-separation-predicts-measurable-failure-modes.md ===

Checks applied: 8

WARN:
- [Source residue] The note references stale paths from a previous project structure: "`docs/notes/`, `arscontexta/self/`, `arscontexta/ops/`" (line 21) and repeats them in "What counts as evidence" (lines 46, 50). These paths no longer exist in the current project (the related-systems review of arscontexta explicitly notes they are stale). A reader encountering this note for the first time has no way to run the proposed observation protocol because the concrete system it targets has been reorganized. The paths now function as source residue from an earlier project state rather than actionable references.
  Recommendation: Update the concrete paths to the current project structure (`kb/notes/`, etc.) or abstract them to description ("the knowledge directory, the self directory, the operational directory") so the observation protocol remains runnable regardless of future reorganization.

- [Source residue] The note says "we already run a system" and "watch for evidence of the failure modes during normal use" (line 21, line 25). The first-person plural and present-tense framing assumes a specific operational context (an earlier version of this project) that no longer matches. This is temporal residue rather than domain residue, but the effect is the same: the note reads as a work-in-progress memo from a specific moment rather than a durable knowledge artifact.
  Recommendation: Either update the observation protocol to reference the current system, or reframe it as a general protocol that any three-space system could use. If the observation window has passed without yielding data, note that in the text.

INFO:
- [Proportion mismatch] The title claims the note is about "measurable failure modes," and the most important section for that claim is "What counts as evidence" (which operationalizes what measurement means). That section gets 3 short paragraphs. The "Observation protocol" section, which is essentially a checklist of questions, gets comparable space. The sections are reasonably balanced, but "What counts as evidence" could be developed further — specifically the "against" and "boring explanation" cases deserve the same concrete-path treatment that the "for" case receives. This is mild enough to be INFO rather than WARN.

- [Confidence miscalibration] The note attributes the three-space model to Cornelius and frames it as a claim to be validated, which is well-calibrated. However, the failure mode descriptions in section "The predicted failure modes" use direct declarative language ("Session observations, processing notes, and transient friction reports appear alongside durable knowledge") that reads as reporting observed facts rather than predicted consequences. Since these are predictions to be tested (the note's own framing), the language could be slightly more conditional. This is a minor calibration gap — the section heading "predicted" does some work, but the body paragraphs don't carry that framing.

CLEAN:
- [Pseudo-formalism] No formal notation, variables, or equations appear in the note. The argument is carried entirely in prose and structured lists. Nothing to flag.

- [Orphan references] The note cites "Cornelius, Agentic Note-Taking #19" as the source for the three-space claim, and the companion note (three-space-agent-memory-maps-to-tulving-taxonomy.md) provides the full URL. The "50+ notes" figure in the open questions section is explicitly framed as a speculative threshold ("We may need 50+ notes before search pollution is measurable"), not as an empirical claim. No unsourced data points or specific studies appear.

- [Unbridged cross-domain evidence] The Tulving taxonomy reference (line 50, "The Tulving mapping adds no explanatory power beyond 'keep your folders tidy'") is used skeptically rather than as supporting evidence. The note questions whether the cognitive science analogy earns its keep, which is the opposite of unbridged transfer. The companion note handles the Tulving mapping in detail; this note only references it to raise the "boring explanation" alternative.

- [Redundant restatement] Each section opens with new material. "The predicted failure modes" introduces the three categories. "Observation protocol" introduces the checklist methodology. "What counts as evidence" introduces the evaluation criteria. "Open questions" introduces unresolved issues. No section restates a prior section's conclusion before beginning its own contribution.

- [Anthropomorphic framing] The note uses "the agent searches," "the agent re-derives," and "the agent starts a new session" — these describe observable agent behaviors (executing searches, recomputing, initializing) rather than attributing mental states. No instances of "knows," "understands," "believes," or "possesses knowledge" applied to the agent. Clean.

Overall: 2 warnings, 2 info
===
