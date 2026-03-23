=== PROSE REVIEW: specification-strategy-should-follow-where-understanding-lives.md ===

Checks applied: 8

WARN:
- [Confidence miscalibration] The three-strategy taxonomy (spec-first / bidirectional spec / spec mining) is the note's own construction — it synthesizes two external sources and one internal note into a lifecycle framework — but it is presented with assertive framing throughout: "Spec-first is for ambiguity that can be resolved before execution," "Bidirectional spec is for ambiguity that is only exposed during execution," "The disagreement is usually a phase error." The note does hedge at the end ("a common maturation path, not a law"), but the body reads as established taxonomy rather than proposed framework. The strongest claim — "move the disambiguation burden to the earliest artifact that can carry it truthfully" — is flagged with "The strongest version of the claim:" which is good, but the section headings and topic sentences elsewhere treat the tripartite decomposition as given.
  Recommendation: Add a brief framing sentence early (e.g., after the opening paragraph) that signals this is a proposed decomposition synthesized from these sources, not a received taxonomy. The closing paragraph's hedges are appropriate but arrive too late to recalibrate a reader who has already absorbed the body as established fact.

- [Proportion mismatch] The core claim is in the title: specification strategy should follow where understanding lives. The section that carries this claim most directly is "The disagreement is usually a phase error," which delivers the synthesis and the strongest formulation. That section is roughly comparable in length to each of the three strategy sections (spec-first, bidirectional, spec mining). However, the "What this predicts" section — which restates the framework's implications as advocacy patterns and pathologies — is substantial (roughly a third of the total body) and largely recapitulates what the strategy sections already established about failure modes. The predictive value it adds is modest: it says each strategy fails when applied outside its zone, which each strategy section already stated in its "failure mode" paragraph.
  Recommendation: Consider whether "What this predicts" can be tightened. Each strategy section already names its failure mode; the predictions section could focus on the novel claim (the three-step maturation path and the "not a law" qualification) without re-listing the pathologies.

INFO:
- [Source residue] The note names "DeAngelis" (line 19) and "Augment" (lines 27, 31) as if readers know these references. "DeAngelis targets" and "Augment's pattern" and "Augment's 'directional decisions' requirement" are shorthand that works only if the reader has already read the linked sources. This is not quite domain-specific residue (the note's domain is specification strategy, and these are about specification strategy), but it is source-specific residue — the note's prose leans on proper names that carry no meaning for a reader who hasn't followed the links. The links themselves are present and correct, so this is a readability concern rather than a representational failure.

- [Redundant restatement] The opening of "The disagreement is usually a phase error" ("These strategies look like competing ideologies only if you assume a system should stay in one mode") partially restates the opening paragraph's claim ("They feel incompatible because they are choosing different storage locations for the same kind of work"). The two sentences make the same point from slightly different angles — incompatibility is illusory — but the repetition is mild and the synthesis section does immediately advance to new content (the numbered lifecycle sequence). Worth noting but not a structural problem.

CLEAN:
- [Pseudo-formalism] No formal notation, variables, or equation-like apparatus. The note uses prose throughout. Clean.

- [Orphan references] No unattributed specific numbers, percentages, or named studies. "DeAngelis" and "Augment" are both linked to their source ingests. The "relaxing-signals note" reference is linked. All empirical-sounding claims are either linked to sources or clearly positioned as the note's own framework. Clean.

- [Unbridged cross-domain evidence] The note stays within a single domain (specification strategy for agentic/LLM systems). The two external sources (DeAngelis on spec-first, Augment on bidirectional spec) are both about specification practices in the same domain the note addresses. Spec mining is linked to an internal note that is also in-domain. No cross-domain transfer without bridging. Clean.

- [Anthropomorphic framing] The note uses "the agent discovers real constraints" (line 27) and "the system does not yet know what to say" (line 35). "Discovers" is borderline but defensible — it describes the agent encountering constraints during execution, which is a process description rather than a mental-state attribution. "Does not yet know what to say" is slightly more anthropomorphic, but in context it means "the system lacks the information needed to produce a useful spec," which is a capacity claim rather than a cognitive one. Neither instance makes claims about the model's internals that the note doesn't intend. Clean.

Overall: 2 warnings, 2 info
===
