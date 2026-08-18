---
gate_id: semantic/unwarranted-scope
name: Unwarranted scope
description: 'The central claim invites reliance over cases its support does not exercise, with no stated transfer relation and no conjecture marking on the surplus scope.'
type: kb/types/review-gate.md
lens: semantic
watches: [title, description, body]
staleness: changed
requires_trait: title-as-claim
---

## Failure mode

The central claim's scope — the class of cases over which the note invites reliance — extends beyond what its support actually exercises, and the note neither argues a transfer relation to the untested cases nor marks the surplus scope as conjecture. The mechanism can be genuine and the citations accurate; the failure is that support earned on specific cases is presented as covering a wider class. Warrant is support that licenses reliance on a specific claim over a specific domain: evidence earns the cases and failure modes it exercises, and reaching beyond them needs a stated reason.

This is a different threshold from `semantic/explanatory-reach`. That gate asks whether a criticizable mechanism exists — whether the claim *could* have reach. This gate asks whether the scope actually claimed is supported — whether the reliance invited is earned.

## Test

For the central claim (title, description, opening argument):

1. State the claimed scope: which cases, systems, or conditions would a reader take the claim to cover?
2. Inventory the support the note itself presents: derivation from stated premises or constraints, results inherited from linked work, direct evidence or worked cases, or an explicit conjecture marking. Judge what is on the page, not support that could be assembled.
3. State the exercised domain: the cases and failure modes that support actually covers. A derivation covers what its premises hold over; evidence covers the cases it examined.
4. If the claimed scope exceeds the exercised domain, look for a stated transfer relation — an argued reason the support reaches the surplus cases, such as coverage of the class, a sampling argument, an invariance, or a mechanism argued to be preserved across the class. Judge whether a relation is *stated and articulated*, not whether it is sufficient — sufficiency is domain-dependent and outside this gate.
5. Pass when any of these holds: the claimed scope matches the exercised domain; a transfer relation is stated for the surplus; or the surplus is explicitly conjectural — conjectural force stated in the title, description, opening, or a clearly named scope, hypotheses, or open-questions section counts.
6. Do not repair. Judge the support the note presents, not a narrower claim or a better transfer argument that would fix it.

WARN when the central claim invites reliance over cases its support does not exercise and neither a transfer relation nor a conjecture marking covers the surplus. INFO when a transfer relation is gestured at but not articulated, or when only a supporting (non-central) claim overreaches.

Do not flag here: a cited source misrepresented or stretched (`semantic/grounding-alignment` — that gate audits the claim-to-citation route; this one audits claimed scope against the union of presented support, including uncited derivation and argument); abstraction that widens the claim's vocabulary (`semantic/unearned-generality`); a scope left ambiguous between materially different readings (`semantic/underspecified-assertions` — ambiguity about *what is claimed* goes there; a scope that is broad but clearly stated is judged here); a conjecture presented as established fact (`semantic/epistemic-status-blur` — that is a status failure even when the scope is right).

## Example (fail)

Title: "Retrieval summaries degrade agent decisions."

The body reports two experiments where summarised retrieval hurt tool-choice accuracy in one coding harness with one model family, proposes a plausible information-loss mechanism, and cites both accurately. Nothing marks the headline as narrower than "agents" in general and nothing argues why two configurations reach other harnesses, tasks, or model families. Mechanism and citations pass their gates; the invited reliance is still unearned.

## Example (pass)

Title: "Retrieval summaries degrade agent decisions when the dropped detail is what the decision turns on."

Same experiments, but the claim's condition names the mechanism as the transfer relation — the effect is argued to follow wherever summarisation removes decision-relevant detail — and the Scope section states that breadth across model families is untested. The surplus scope is carried by a stated relation and an explicit boundary.

---

Relevant Notes:

- [Natural-language theories carry warrant claim by claim and scope by scope](../../../notes/natural-language-theories-carry-warrant-claim-by-claim.md) — rests-on: warrant attaches to claim-scope pairs, and transfer beyond the tested domain needs a justified relation
- [Derivation and inheritance give starting warrant; discriminating evidence or proof earns scope](../../../notes/derivation-and-inheritance-give-starting-warrant-earns-scope.md) — rests-on: the support routes and what domain each one earns
