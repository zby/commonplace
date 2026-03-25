<!-- REVIEW-METADATA
note-path: kb/notes/programming-patterns-get-a-fast-pass-but-other-borrowed-ideas-must-earn-first-principles-support.md
last-full-review-note-sha: 3fc9110433027256dc3f23f025e79e3bbb7bbd23
last-full-review-note-commit: 8155ada39cf93a9f62e3baa54e38ae42663d9b5a
last-full-review-at: 2026-03-25T09:27:18+01:00
last-accepted-note-sha: 3fc9110433027256dc3f23f025e79e3bbb7bbd23
last-accepted-note-commit: 8155ada39cf93a9f62e3baa54e38ae42663d9b5a
last-accepted-at: 2026-03-25T09:27:18+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: programming-patterns-get-a-fast-pass-but-other-borrowed-ideas-must-earn-first-principles-support.md ===

Checks applied: 4

INFO:
- [description-discrimination] The description's first clause ("We borrow from any source but adopt based on first-principles support") restates the title without adding value. The second clause ("because the bet is that knowledge bases are a new kind of software system") does add mechanism — it names the underlying bet that justifies the asymmetry. A tighter description would drop the restatement and lead with the mechanism, e.g.: "The bet is that agents interpreting prompts are structurally similar to interpreters running code — if that holds, programming patterns transfer by mechanism, not analogy. Other domains (cognitive science, law) need independent first-principles justification."
  Recommendation: Rewrite to lead with the mechanism and drop the title restatement.

- [title-body-alignment] The title frames a binary split (programming fast pass vs. first-principles bar for everything else), but the body establishes a four-path taxonomy: programming fast pass, first-principles adoption, legal drafting as untested hypothesis, and empirical observation as a non-borrowing path entirely. The last two categories don't fit neatly under "must earn first-principles support." This is mild — the title captures the primary insight — but a reader following the title's framing may be surprised by the scope of the body.
  Recommendation: No action needed for a seedling. If promoted, consider whether the title should signal the richer taxonomy or whether the body should be split.

CLEAN:
- [title-composability] "since programming patterns get a fast pass but other borrowed ideas must earn first-principles support, we designed..." reads naturally as a sentence fragment. The title works as a linkable prose element.
- [claim-strength] The claim is specific and contestable — someone could argue programming patterns are the worst analogy for natural-language knowledge systems, or that cognitive science deserves the fast pass instead. The asymmetry the title asserts is a genuine design bet, not a truism.

Overall: 0 warnings, 2 info
===
