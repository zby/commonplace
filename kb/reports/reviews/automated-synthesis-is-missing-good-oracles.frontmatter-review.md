<!-- REVIEW-METADATA
note-path: kb/notes/automated-synthesis-is-missing-good-oracles.md
last-full-review-note-sha: be392eb67c054e0991008b89f0a6985709b9b191
last-full-review-note-commit: f9967a667eaaed2313fd2cb30df0f08ae49ecf18
last-full-review-at: 2026-03-24T20:53:43+01:00
last-accepted-note-sha: be392eb67c054e0991008b89f0a6985709b9b191
last-accepted-note-commit: f9967a667eaaed2313fd2cb30df0f08ae49ecf18
last-accepted-at: 2026-03-24T20:53:43+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: automated-synthesis-is-missing-good-oracles.md ===

Checks applied: 4

CLEAN:
- [Description discrimination] The description adds mechanism the title cannot carry: it names generation as the easy part and evaluation as the hard part, specifying that LLMs readily produce candidates but discriminating insight from noise is the bottleneck. An agent seeing five oracle-related results would immediately know this note is about the evaluation gap, not about oracle design or oracle strength.
- [Title composability] "since automated synthesis is missing good oracles, the system cannot run unsupervised" reads as a natural sentence fragment. The title composes well as a linkable clause.
- [Claim strength] The claim is specific and non-obvious. Someone could reasonably argue that LLM self-evaluation, embedding similarity, or composite weak signals already provide adequate oracles for synthesis. The note's `speculative` status is consistent with this being a genuine, contestable claim rather than a truism.
- [Title-body alignment] The body directly supports the title: it defines the oracle gap (extraction verification is cheaper than synthesis verification), surveys current systems showing synthesis works only when an oracle exists, explains why the oracle is hard to build (novelty + validity vs fidelity), and frames open questions around oracle construction. No drift detected.

Overall: CLEAN
===
