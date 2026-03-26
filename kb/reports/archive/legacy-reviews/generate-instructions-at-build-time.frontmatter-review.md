<!-- REVIEW-METADATA
note-path: kb/notes/generate-instructions-at-build-time.md
last-full-review-note-sha: f4e57a1b148ac69cee43c1a0f1ef9df55b9057ff
last-full-review-note-commit: cc365676b30ed9f3d77958177ab9107a32e2f046
last-full-review-at: 2026-03-24T20:55:09+01:00
last-accepted-note-sha: cbe14ca72e67f652b7565ad2095c7b0ab79d6360
last-accepted-note-commit: 54940c69ea2daa628e8e28ba00f26e0f3b203f2a
last-accepted-at: 2026-03-25T09:26:20+01:00
last-acceptance-kind: trivial-change-ack
review-type: frontmatter-review
-->
=== FRONTMATTER REVIEW: generate-instructions-at-build-time.md ===

Checks applied: 4

WARN:
- [Description discrimination] The description "KB skills should be generated from templates at setup time, not parameterised with runtime variables — applying the general principle that indirection is costly in LLM instructions" largely restates the title with a grounding reference appended. The first clause ("generated from templates at setup time, not parameterised with runtime variables") is a paraphrase of the title. The appended principle ("indirection is costly") names the grounding note but doesn't add mechanism or scope. The body contains a stronger discriminator: "You pay the flexibility cost once at setup time, not on every use" — this explains WHY build-time generation wins (one-time cost vs. per-use cost). A description built around that mechanism, or around the constraining framing ("template is soft, generated output is hard"), would help an agent distinguish this note from the more general indirection-is-costly note in search results.
  Recommendation: Replace the description with one that leads with mechanism or scope — e.g., "Build-time template resolution pays the flexibility cost once; runtime variables impose interpretation overhead on every skill invocation. Applies the constraining gradient: soft template in, hard literal out."

INFO:
- [Title composability] The title is imperative ("Generate KB skills at build time, don't parameterise them"), which doesn't compose naturally with "since" or "because" — "since generate KB skills at build time" reads ungrammatically. A declarative form like "KB skills should be generated at build time not parameterised" would compose more smoothly. However, the imperative form is a defensible style choice for design-decision notes and the note's status is seedling, so this is flagged as INFO rather than WARN.

CLEAN:
- [Claim strength] The title asserts a specific design choice (build-time generation over runtime parameterisation) that is genuinely contestable — someone could reasonably argue runtime variables are simpler, require no build step, and keep the toolchain lighter. The note presents both alternatives and argues for one. Not a truism.
- [Title-body alignment] The body's core argument directly supports the title's claim: it presents runtime variables vs. build-time generation, explains why generation wins, and frames it as constraining. The "Installation-specific inputs" section extends the scope to values that vary between installations, but this is a natural elaboration of the same mechanism (template resolution from a different input source) rather than a drift to a different claim.

Overall: 1 warning, 1 info
===
