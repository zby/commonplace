---
description: "Decorrelating reviewers removes the author's errors, not the field's; plural judges converge on consensus exactly where a claim is original, so stance per claim must be declared before review and findings triaged by it"
type: kb/types/note.md
traits: [title-as-claim]
tags: [foundations, methodology]
---

# Decorrelated reviewers still share the field's prior, so declare which claims you will defend

Decorrelated review — a fresh critic, a clean-context judge, a second model — removes the errors that came from the author's own reasoning trace. It does not remove the errors that come from the field. Judges drawn from one training distribution, or one discipline, carry the same consensus prior, and a verdict is evidence weighed against that prior. On the component of a claim the prior determines, N such judges are not N independent draws. [Error correction works with above-chance oracles and decorrelated checks](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md); a shared prior is a correlated error term that decorrelation of the *proposer* leaves untouched.

The consequence is not uniform. Where a claim uses a source on its consensus reading, the judges agree with the author and the review is cheap. Where a claim contests the consensus reading, the judges converge on the consensus and propose the reversal. Review pressure therefore concentrates on the most original claims, and a vote cannot tell "original" from "wrong" there — both look the same to a judge whose prior is the field's.

## Declare the stance before review

Because reviewers cannot reconstruct which claims the author means to defend — that is purpose, held upstream and not derivable from the artifacts, [since intent-framed delegation is a control regime](./intent-framed-delegation-is-a-control-regime-not-a-short-prompt.md) — the stance has to be written down before the review runs. Two stances suffice:

- **Divergence.** The author contests the consensus reading and will pay for the claim. Pushback is predicted. A reversal is accepted only when it supplies a new object-level argument — a premise the author's argument lacked, a counterexample it did not survive. A reversal that restates the consensus conclusion is the predicted event, and it is not evidence.
- **Support.** The source or claim is used on its consensus reading because of what it supplies. Reviewer narrowing is accepted by default: nothing the author defends lives there, so the narrowing costs no content the author cares about.

Triage then runs stance-first: at a support claim, accept a finding unless it is factually wrong about the source; at a divergence claim, ask whether the finding adds a premise. This is a rule for allocating the check, not for deference. Divergence claims are not more likely to be true because they are original; they are the claims for which plural judgment is uninformative, so the remaining checks — an object-level refuter stated in advance, and later exposure to evidence the author did not produce — have to carry the weight.

Seen from the repair side, this is why [narrowing bought to survive review is paid for in content](./narrowing-bought-to-survive-review-is-paid-for-in-content.md): review pressure pushes hardest exactly where narrowing costs most. Stance makes the two cases separable. Accepting narrowing on a support claim is ordinary repair; accepting it on a divergence claim is the loss that note describes.

## A witness

A clean-context audit of a source register in this repository, run in 2026, sorted its findings this way without being told to. It narrowed four support rows — an organizational-learning source, a philosophy-of-science source, a function-allocation taxonomy, a human-factors precedent — on grounds faithful to the ingests, and every narrowing was taken. It also proposed reversing the two rows where the series contests the consensus reading of its sources, Naur's human binding and the Bitter Lesson's weights-only extrapolation, by reading the consensus conclusion as the source's generating condition. Neither reversal added a premise; both restated the consensus. They were declined as predicted, and the register now carries the stance per row so the next audit is triaged the same way.

## Guards

The stance list is itself capturable: declare every claim a divergence and the work is immune to review. Two guards keep it honest. A divergence claim must carry its object-level argument and a stated refuter in the artifact — it cannot be defended by stance alone. And the list should be short; a program with many divergences has not chosen its battles, and each undeclared or over-declared divergence is a place where review either bites where it should not or is waved away where it should bite.

## Scope

- The claim holds where the judges share a training distribution or a disciplinary consensus. Judges from genuinely different traditions decorrelate part of the prior; how much is an open question below.
- Loading the author's theory into the judge's context reduces convergence on the proposer's blind spots and may reduce convergence on consensus, but the prior sits in weights, not in context, so this is a partial remedy at best.
- The rule presupposes a declared program. Where the author has no stated purpose there is no stance to declare, and review pressure toward consensus operates unchecked.
- Human peer review has the same structure; the note is stated for agent-run review because that is where the mechanism was observed and where the remedy is cheap to install.

## Open Questions

- Whether judges from different training corpora measurably decorrelate the consensus prior, or whether the corpora overlap enough that model diversity buys little at divergence points.
- Whether a judge with the author's argument loaded reverses divergence claims less often than a bare judge, holding the finding's factual quality fixed.

---

Relevant Notes:

- [Error correction works with above-chance oracles and decorrelated checks](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — grounds: the independence condition a shared prior violates on the component it determines
- [Mechanistic constraints make Popperian KB recommendations actionable](./mechanistic-constraints-make-popperian-kb-recommendations-actionable.md) — grounds: why a correlated check is not criticism, extended here from same-prompt re-reading to same-prior judging
- [Narrowing bought to survive review is paid for in content](./narrowing-bought-to-survive-review-is-paid-for-in-content.md) — extends: the repair-side cost this note's stance declaration makes separable from ordinary repair
- [Intent-framed delegation is a control regime; prompt length does not establish it](./intent-framed-delegation-is-a-control-regime-not-a-short-prompt.md) — grounds: purpose is held upstream and cannot be reconstructed by the executor, which is why stance must be declared rather than inferred
- [Problem matches guide method search; mechanism matches bound transfer](./problem-matches-guide-method-search-mechanism-matches-bound-transfer.md) — enables: the source-register form in which a stance per row is cheapest to declare
