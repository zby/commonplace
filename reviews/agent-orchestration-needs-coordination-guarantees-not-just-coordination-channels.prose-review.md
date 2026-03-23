=== PROSE REVIEW: agent-orchestration-needs-coordination-guarantees-not-just-coordination-channels.md ===

Checks applied: 8

WARN:
- [Proportion mismatch] The opening paragraph promises four failure modes ("corrupting shared meaning, diverging from peers, amplifying a bad result, or diffusing responsibility downstream"), and the summary table lists four rows. But "Failure modes by composition" develops only three (contamination, inconsistency, amplification) in one paragraph each. The fourth — accountability vacuum — appears two sections later under "The design implication" and gets two full paragraphs plus a connection to the verification-boundary note. The load-bearing claim is that all four are "manifestations of one failure schema," yet the fourth receives substantially more development than the other three combined and is structurally separated from its peers. A reader encountering the table first may wonder why one row got a subsection under "design implication" while the others were handled above.
  Recommendation: Either move the accountability-vacuum subsection up into "Failure modes by composition" as a fourth peer entry (keeping it proportional to the others), or trim its development to match the other three and extract the extended liability-firebreak and verification-boundary discussion into a dedicated note.

- [Confidence miscalibration] The four-row failure schema (contamination / inconsistency / amplification / accountability vacuum) is the note's own synthesis across four separate sources. It is presented with assertive framing: "These are not four names for one bug. They are manifestations of one failure schema — **uncoordinated composition**." The closing paragraph hedges well ("The unification claim is limited but useful"), but the body — especially the table and the bold "uncoordinated composition" label — reads as established taxonomy rather than proposed decomposition. For a seedling note introducing its own framework, the assertive middle sits in tension with the hedged close.
  Recommendation: Add a brief framing sentence before or after the table acknowledging that this decomposition is the note's own proposal: e.g., "One way to map these cases:" before the table. The closing hedge is good; the gap is in the body where the framework is introduced.

INFO:
- [Source residue] "spooky action at a distance" in the contamination subsection is a quantum-mechanics metaphor. It is well-understood in software engineering as informal shorthand for non-local effects, so it is not strictly residue — but it is the only figurative language in an otherwise technical note, which makes it slightly incongruent in register.

CLEAN:
- [Pseudo-formalism] The only structured apparatus is the four-row summary table, which maps composition mode to missing primitive to failure mode. Each cell is a concrete architectural concept, not a symbolic variable. The table compresses information that would be harder to compare in prose. No decorative notation found.
- [Orphan references] All empirical or conceptual claims are traced to linked notes or ingested sources (scoping note, memory-architecture ingest, synthesis note, Tomasev et al. delegation paper). No unattributed figures, percentages, or named studies.
- [Unbridged cross-domain evidence] All cited sources are from the agent/LLM architecture domain. The Tomasev et al. paper addresses AI delegation; the memory-architecture source addresses multi-agent memory. No cross-domain transfer requiring a bridge sentence.
- [Redundant restatement] "The shared question" section opens by referencing the design-space note and restating the form/guarantee distinction, but it does so in one sentence and immediately adds a new directive ("ask what coordination guarantee matches that composition mode"). The restatement is functional transition, not redundant setup.
- [Anthropomorphic framing] "the system believes false things" appears once, inside a deliberate contrast explaining what accountability failure is NOT ("The bad outcome is not 'the system believes false things' ... but 'no one in the chain is clearly answerable'"). This is metalinguistic use, not an anthropomorphic claim. "Agents diverge" uses "agents" as the standard term of art. No problematic anthropomorphism found.

Overall: 2 warnings, 1 info
===
