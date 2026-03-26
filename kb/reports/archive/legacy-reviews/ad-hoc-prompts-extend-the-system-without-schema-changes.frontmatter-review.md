<!-- REVIEW-METADATA
note-path: kb/notes/ad-hoc-prompts-extend-the-system-without-schema-changes.md
last-full-review-note-sha: 143d2abf2d6af423f8240836c5f934b89914e1db
last-full-review-note-commit: 2cc208c7d264b0834d0fe6c1fc666e16dbb15a41
last-full-review-at: 2026-03-24T14:34:00+01:00
last-accepted-note-sha: 143d2abf2d6af423f8240836c5f934b89914e1db
last-accepted-note-commit: 2cc208c7d264b0834d0fe6c1fc666e16dbb15a41
last-accepted-at: 2026-03-24T14:34:00+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: ad-hoc-prompts-extend-the-system-without-schema-changes.md ===

Checks applied: 4

CLEAN:
- [Description discrimination] Description "Any system with an LLM agent layer can absorb new requirements through natural language prompts without changing the deterministic base" adds scope (any system with an LLM agent layer, not just KBs) and mechanism (natural language prompts absorbing requirements into the deterministic base) beyond what the title carries. In a list of 5 results about prompt-based extension, this description distinguishes by naming the two-strata architecture and the absorption mechanism.
- [Title composability] "since ad hoc prompts extend the system without schema changes, we designed..." reads naturally as a sentence fragment. The title functions as a linkable claim.
- [Claim strength] "Ad hoc prompts extend the system without schema changes" is contestable — someone could argue prompts are ephemeral workarounds rather than genuine system extensions, or that schema changes are preferable for reliability. The claim is specific enough to carry information. Note is also marked `status: seedling`, which provides additional latitude.

INFO:
- [Title-body alignment] The title claims prompts "extend the system without schema changes," but the body argues a stronger thesis: that ad hoc prompts are sometimes *better* than formal types because they "carry judgment that type signatures can't express" (section "Prompts carry what types can't") and that this works because of homoiconicity. The title captures the weaker, necessary-condition claim (they can extend) while the body establishes the sufficient-condition claim (they should extend, in certain cases, because they carry what types can't). This is mild scope drift — the body's actual argument outgrows the title. If the note matures past seedling, consider whether the title should reflect the stronger claim, e.g., "ad hoc prompts carry what schema extensions cannot."

Overall: 0 warnings, 1 info
===
