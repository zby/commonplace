=== FRONTMATTER REVIEW: baseline.md ===
Checks applied: 4

WARN:
(none)

INFO:
- [description-discrimination] The description's second clause ("chat and framework-owned tool loops conflate them by making session history the default next context") partially restates the title. The first clause saves it by surfacing the store-vs-load separation as the key mechanism, which is genuine retrieval value not present in the title. Borderline pass — a tighter description could replace the second clause with an implication (e.g., what goes wrong when the conflation happens).

CLEAN:
- [title-composability] "Session history should not be the default next context" reads naturally inside sentence frames ("since session history should not be the default next context..." / "because session history should not be the default next context..."). Works as a linkable prose fragment.
- [claim-strength] The claim is contestable: many frameworks and practitioners default to session history precisely because it preserves maximum information with minimal design effort. The note itself acknowledges the trade-off, making the opposing position explicit rather than straw-manned.
- [title-body-alignment] The body directly supports the title's claim. It explains where the problem appears (chat sessions, tool loops, continuing sessions), why transcript inheritance is attractive early, why it breaks down for orchestration, and proposes artifact-first loading as the alternative. The body is broader than the title (covering nuanced cases like Slate episodes and the exploratory-default argument), but this is elaboration within scope, not drift.

Overall: 0 warnings, 1 info
===
