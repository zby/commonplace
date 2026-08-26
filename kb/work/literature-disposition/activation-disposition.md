# Dated artifact disposition — contextual activation

**Disposition: Keep as the canonical read-back and activation synthesis. Decided
and executed 2026-08-26.** The comparison used full-text captures of
[Tulving and Pearlstone](../../sources/tulving-pearlstone-availability-versus-accessibility.ingest.md)
and [Gick and Holyoak](../../sources/gick-holyoak-analogical-problem-solving.ingest.md),
not an abstract-only publisher extraction.

| Test | Finding |
|---|---|
| Source overlap | Tulving and Pearlstone establish a narrower human storage-to-retrieval contrast: category cues improved immediate word recall, which they interpreted as stored information becoming accessible. Gick and Holyoak's Experiment IV reaches task use: 11 of 12 hinted participants produced the analogical solution, versus 3 of 15 without the hint, while story-gist recall did not differ significantly. The latter experiment cannot separate retrieval from salience after retrieval. Neither paper studies LLM agents or defines read-back. |
| Commonplace remainder | The [note](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) defines read-back as retained memory accumulated through use returning to a future action, excludes shipped static documentation, and separates that storage-to-context step from context-to-action activation. It combines that distinction with bounded LLM evidence and a four-rung evaluation ladder: existence, exposure, behavior change, and downstream benefit. The psychology papers supply antecedents for two narrower human contrasts, not this agent-specific synthesis. |
| Recovery and shape | A source pointer would lose the human-to-agent transfer and the operational boundary the agent-memory review contract uses. Extracting read-back into a separate definition would also split the relation that the current consumer needs: the type contract delegates both what counts as read-back and how it differs from activation. Search found no independent consumption pressure that offsets that extra hop. |
| Graph role | Measured 2026-08-26, 222 tracked library artifacts link to the note. Of those, all 158 agent-memory reviews use uniform tail links, so the raw count overstates rewiring complexity. The load-bearing definitional dependency is concentrated in the [review type](../../agent-memory-systems/types/agent-memory-system-review.md), the [collection index](../../agent-memory-systems/README.md), and the [framework design record](../../agent-memory-systems/review-framework-design.md). Keeping the path preserves both the cheap bulk links and the real contract dependency. |
| Execution | Commit `bcbde033` added the two primary ingests and bounded human-evidence paragraph without changing the note's path, title, or central claim. Grounding review accepted both new source routes, then exposed older scope mismatches elsewhere in the note: unsupported prevalence wording, an overbroad selection-signal description, and an example label that should have been an analogy. Those were narrowed, and `semantic/grounding-alignment` finished PASS with no stale pair in the `codex` partition. No inbound rewiring or retirement approval stop applied. |

This is another keep reached through a narrower human analogue. The inherited
literature explains retrieval accessibility and cued analogical use. The note
survives because it names the target-side transitions, defines the review
system's read-back boundary, and turns those distinctions into an evaluation
ladder. That result supports claim-level source comparison; it does not yet
establish a general disposition rule.
