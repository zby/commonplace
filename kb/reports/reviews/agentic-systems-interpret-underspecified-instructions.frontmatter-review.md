<!-- REVIEW-METADATA
note-path: kb/notes/agentic-systems-interpret-underspecified-instructions.md
last-full-review-note-sha: 696ef4210017555cd601468321ede172ef3d838a
last-full-review-note-commit: fd0b8fb01d3e8c63e580847019636c0e1e2eff01
last-full-review-at: 2026-03-24T14:34:00+01:00
last-accepted-note-sha: 696ef4210017555cd601468321ede172ef3d838a
last-accepted-note-commit: fd0b8fb01d3e8c63e580847019636c0e1e2eff01
last-accepted-at: 2026-03-24T14:34:00+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: agentic-systems-interpret-underspecified-instructions.md ===

Checks applied: 4

CLEAN:
- [Description discrimination] The description adds mechanism well beyond the title: it names the two distinct properties (semantic underspecification and execution indeterminism), identifies which is deeper, introduces the spec-to-program projection model, and names the obscuring dynamic between the two phenomena. An agent seeing this among 5 search results would immediately know this is the theoretical two-phenomena framing, not a generic note about agentic systems or prompt engineering.
- [Title composability] "since agentic systems interpret underspecified instructions, we designed..." reads naturally as a sentence fragment. The title functions well as a linkable prose element.
- [Claim strength] The framing of LLM behavior as "interpretation of underspecified instructions" is genuinely contestable. Many practitioners treat LLM outputs as stochastic outputs of a fixed program -- the "interpret" and "underspecified" framing is a specific theoretical commitment that someone could reasonably argue against (e.g., by arguing LLMs are better modeled as noisy function approximators, not interpreters).

INFO:
- [Title-body alignment] The title foregrounds semantic underspecification ("interpret underspecified instructions") but the body's central argument is a two-phenomena distinction: underspecification vs. indeterminism, with the claim that indeterminism obscures the deeper difference. The two-phenomena separation, the obscuring dynamic, the spec-to-program projection model, and the constraining/relaxing framework are all major body contributions that the title doesn't signal. The title names the more important half accurately, so this is not a misalignment -- but the body establishes significantly more than the title promises, functioning as a theoretical framework note rather than a single-claim note. If the note were titled to signal the two-phenomena distinction (e.g., "semantic underspecification is the deeper difference in agentic systems, not indeterminism"), the title would better predict the body's actual argument.

Overall: 0 warnings, 1 info
===
