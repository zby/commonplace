# Workshop: theory-mediated methodology article

**Posed by:** the operator, 2026-08-26. Restructure [`kb/articles/reflective-self-improvement.md`](../../articles/theory-building-inside-the-system.md) — not discard it — into the third article pillar beside [the bitter-lesson article](../../articles/the-bitter-lesson-does-not-require-everything-to-live-in-weights.md) and [the human-inclusive revision article](../../articles/moving-revision-decisions-into-the-automatic-system.md): theory-mediated methodology, with Naur's *Programming as Theory Building* as the hook.

**The angle, as posed.** Naur: the programmer builds a theory of the part of the world a program handles, and the program alone cannot preserve it. LLMs change the second half: natural-language theories can become operative artifacts inside the system. An agent can use them to explain failures, derive changes, revise its assumptions, and progressively formalize what stabilizes. When the theories describe the system itself, theory building becomes a route to reflective self-improvement.

**Corrections settled in discussion (binding on the draft).**
- Do not say "LLMs let us write the theory down." Naur's first half stands: text does not carry the application judgment. What changed is that an interpreter with that judgment now sits inside the system.
- Do not say world knowledge was the missing piece, or that an LLM "falls outside" Naur's human/machine partition. An LLM is formal symbol manipulation on a computer — inside Naur's machine pole. His bridge to the human binding was that machine execution meant formulated criteria, true of the programs of his day; trained recognizers separated formal execution from formulated criteria. Basis: [Naur binds program theory to humans by equating machine execution with formulated criteria](../../notes/naur-equates-machine-execution-with-formulated-criteria.md).
- Keep the compounding tests and the accumulation-versus-compounding distinction from the current draft; shrink the six-system survey.

**What closes it.** The article rewritten and circulating as a draft under the articles contract, with the source notes list updated and the adjoiner consumed or explicitly left; this workshop then deleted.

## Status (2026-08-26, evening)

Draft rewritten in place, now at `kb/articles/theory-building-inside-the-system.md` (~4,850 words; validation passes). All nine outline sections are present; the adjoiner is consumed (Part 1 into §3, Part 2 into §8) and deleted. Kept from the old draft: compounding, the three tests, both experiments, the six-system evidence shrunk to one paragraph plus HyperAgents. Renamed to `kb/articles/theory-building-inside-the-system.md` (pure relocation, redirect kept). Remaining before closing: a review pass under the articles contract, and the three open items below.

## Status (2026-08-27, human-inclusive article reframed and renamed)

The human-inclusive hand-back was resolved the same way as theory-building: the operator judged the title-level claim dissolved (with maintainers inside the boundary, self-revision is the cheap case; the hard part is moving decisions into the automatic system). The article is now `kb/articles/moving-revision-decisions-into-the-automatic-system.md` (pure relocation commit 932acd9f; redirects for both old slugs). The six obligations are restated as the representation a revision decision needs before machinery can make it; the constitutional analogy is inverted to explain why the human case is cheap; the explanatory-reach and ADR cases now say which decisions moved (application, drafting, checking) and which did not (adoption); the two audit gaps are the two decisions that cannot move (admission — inputs unrepresented; model realization — record can be wrong); `broad` is path-relative readiness. The `final.txt` warrant/admission repair is retained. Packet `20260827T080424Z-0215dd` records the decision in Open items (schema admits no alternative state for a keep packet). Remaining hand-back: bitter-lesson (Memento-Skills grounding).

## Status (2026-08-27, theory-building reframed as reallocation)

The theory-building hand-back was resolved by the operator with an alternative the packet had not offered: the human-inclusive reading makes theory-holding cheap and the machine-only reading makes it unshowable, so the article now asks which *functions* of theory building the computational part supplies (option d). It declares the boundary (base model, artifacts, validators, agents, maintainers), decomposes Naur's capabilities into seven functions, and records their allocation in a table: apply / criticize / propose computational; derive computational-but-human-admitted; coherent modification, admission, and choice of demand human. The repair episode is the datum locating the boundary at coherent modification (Naur's third capability). A new closing section fixes the comparison grain, measures per human judgment not hours, pre-registers what would move a function, and leaves the contraction endpoint open. Operative, learned-state, and formalization sections reuse the pass's `final.txt` prose (closing had judged them strengthened); the friction-found reversal in the companion handoff is gone. The two citing articles and the README carry the allocation framing. Packet `20260827T080429Z-ea6772` recorded as alternative-applied. Grounding notes: `computationally-directed-self-improvement-is-a-reallocation`, `methodological-and-computational-closure-track-different-changes`, `measuring-autonomy-well-enough-to-see-it-improve-is-an-open-problem`, `increasing-computational-autonomy-relocates-human-effort`.

## Status (2026-08-27, full passes)

`run-full-improvement-pass-on-note.md` was run on four of the six articles (session limit stopped it before `when-systems-learn-theories-about-themselves` and `continual-learning-outside-the-weights`). Method coverage was complete for all four. Results: `theory-building`, `what-makes-human-inclusive`, and `the-bitter-lesson` each reached closing and were **handed back** (live text rolled back; each pass's `final.txt` edit set is retained under `kb/reports/full-pass/<name>/` and judged to strengthen or preserve the update, so it is reusable once the author decision is made). Author decisions pending: theory-building — whether "inside the system" includes the maintainer and admission workflow; human-inclusive — whether a represented authorization path is *necessary* or a governance ideal (and whether "broad" addressability is evidentially settled); bitter-lesson — the Memento-Skills acceptance-mechanism cell.

`what-bound-naurs-theory-to-programmers` ended `revise` and was **accepted with candidate claim 2** (packet `20260827T080417Z-76a3c9` resolved). The article now declares both readings of "formulated criteria" and takes the rubric reading with textual reasons, concedes that under the formal reading nothing has come apart, bounds the bridge premise to the programs Naur describes (the Neocognitron predates 1985), answers the independent-bearer objection by routing it to the three tests, downgrades the LLM sentence to "the same formal kind," and reframes the episode as a failure of Naur's *third* test with the purpose present in the inputs (the pass had defeated "in none of its inputs"). The four citers in the brief's scope (README, theory-building intro, when-systems-learn, continual-learning) were reconciled to "candidate holder that Naur's tests must vet."

Next: run the two missing passes; decide the three hand-back questions and reapply the retained `final.txt` edits.

## Status (2026-08-27, third pass): the Naur argument is its own article

The operator judged the constructive article still too long and wanted the disagreement with Naur — where the pushback will land — separated from what results from it. Split again:

- `kb/articles/what-bound-naurs-theory-to-programmers.md` (~2,600 words, new) — Naur's thesis both halves, what a theory is (Popper), why the binding held and what changed (with Naur's three tests), the self-witnessed repair episode, pre-registering the tests, doorway to the constructive article.
- `kb/articles/theory-building-inside-the-system.md` (~2,100 words) — takes the Naur article as premise: operative arrangements, held theory → learned state, formalization and proof, the direction caveat, doorway to the reflective article.
- `kb/articles/when-systems-learn-theories-about-themselves.md` unchanged in content; its companion links now distinguish the two.

Reading order: Naur → theory building → when systems learn. Both new drafts validate clean.

**Fourth article (2026-08-27):** `kb/articles/continual-learning-outside-the-weights.md` (~3,400 words) — the disagreement with Sutton and Javed, argued as "there is a second substrate", not "their program is wrong". Accepts the big-world premise, "weights never change" as description, and the what-keeps-knowledge-correct question; parts from one inference (concepts formed by weight learning ⇒ must continue by weight learning); describes the frozen-interpreter-over-artifact-layer substrate and three things it answers (named concepts as artifacts, explicit coherence maintenance, deployment-local learning); learn-a-model-and-plan in the artifact layer with its dependency stated; four mechanism limits plus the human-in-loop difference of aim; the comparative test. Grounded on seven retained quotes in the Sutton/Javed ingest (added via cp-skill-ground on 2026-08-27). Reading order is now Naur → theory building → when systems learn → outside the weights.

## Status (2026-08-27, later): split into two articles

The operator decided to split by thesis at the reflective turn, after two external comment rounds that agreed on the seam and disagreed on where the self-witnessed episode goes (kept in the Naur article: it tests that article's claim on its own machinery, and this settles the first open item below).

- `kb/articles/theory-building-inside-the-system.md` (~4,200 words) — the Naur argument: both halves, what a theory is, why the binding held and what changed, operative arrangements, held theory → learned state (theory-mediated learning, without the property taxonomy), formalization and proof, the self-witnessed repair episode, a one-paragraph direction caveat, pre-registering Naur's tests, and a doorway to the reflective case.
- `kb/articles/when-systems-learn-theories-about-themselves.md` (~3,400 words, new) — theory-mediated / reflective / self-improving as independent properties, the pairwise table, what explicit theory adds (Argyris, decomposition, addressability), the minimum architecture (three conditions, the evaluator, Gödel), evidence (Tuesday rule, compounding, three tests, Ashby, reported systems, HyperAgents, the three 2026 harnesses in one paragraph), Commonplace as a partial realization, direction, and the two experiments. The old `reflective-self-improvement` and `what-makes-a-system-self-improving` redirects now point here.
- `kb/notes/evidence/three-2026-harnesses-retain-rules-or-weights-not-a-revisable-theory.md` (new) — the full Prime Agent / Recuris / Apodex reading with the retained quotes; both articles cite it rather than carry it.

Both drafts validate clean. Remaining: the review pass under the articles contract on both, and the two open items still open below (title — now moot for article 1, which kept its title; the un-homed direction note).

## Status (2026-08-27)

Revised after an external round of comments (ChatGPT, relayed by the operator; adopted selectively) and three new harness ingests. Changes: the thesis now runs Naur → interpreter inside the system → **theory-mediated learning** as the general architecture, with theory-mediated methodology as this project's realization; a new section *From held theory to learned state* makes the `failure → theory revision → derived patch` step explicit and introduces the three independent properties (theory-mediated, reflective, self-improving) after the argument rather than before it; "cannot be written down" is restated as "propositions about a theory do not transfer possession of it"; Popper compressed to two paragraphs; a new short section on formalization and proof (verification moves the open question to the theory–model correspondence); a new *Three recent harnesses on the grid* subsection positions Prime Agent (R+S, no gate, no theory), Recuris (R+S with a fixed gate; retained state accumulates and cannot be rescoped), and Apodex (parametric retention, not a loop), with Sutton/Javed as the weights-side counterpoint. ~7,150 words; validation passes. Not adopted: editing for quotable sentences (contract defers memorability to a later pass). Remaining: the review pass under the articles contract, and the three open items below.

## Outline

Working title: *Theory building inside the system*. Subtitle candidate: *how natural-language theories become operative, and when that is reflective self-improvement*.

1. **Naur's thesis, both halves.** Programming builds a theory — a capacity to map program to world, justify each part, and extend it by judging a new demand's similarity to what exists. Artifacts are secondary; the theory "could not conceivably be expressed" and is bound to human beings; a program whose theory-holders are gone is dead though it still runs. State both halves at full strength before touching either. *Sources:* Naur ingest (19 quotes).

2. **What a theory is here — Popper.** Theories as exosomatic artefacts, "organs evolving outside our skins"; objective in that their logical consequences exceed what any producer grasps ("the person who produces a theory may very often not understand it"); consumed by criticizing, changing, replacing (`P1 → TT → EE → P2`). Naur himself gives Ryle's theory its "defensible philosophical standing" by calling it a Popperian World 3 object — then denies it can be expressed. The article sits inside Popper's frame and treats Naur as the objection raised within it. *Sources:* Popper 1966 ingest (8 quotes; note it never uses the "World 3" label — attribute the label to Naur's citation of *The Self and Its Brain*). *Notes:* discovery-lifecycle; theory-warrant-tracked-at-the-finest-granularity.

3. **Why the binding held, and what changed.** The basis note's argument: inexpressibility targets formulated criteria; the bridge to humans is that a program executes formulated criteria; accurate in 1985; trained recognizers separate execution from formulated criteria on Naur's own examples (faces, tunes, wine). Merge the adjoiner's Part 1 here: reflective systems existed for decades with the causal wire and no evaluator; the missing resource was judgment over a declared objective, which is the same application judgment Naur located in the programmer. Proof / benchmark / LLM judgment as the regimes. *Sources:* basis note; adjoiner Part 1 (consumed, file deleted). *Notes:* goedel-machines; reflection-buys-addressability.

4. **Operative, not documentary — Argyris and the consumption path.** Espoused theory versus theory-in-use: a retained theory is operative only through what consumes it with binding force. What makes a natural-language theory a theory-in-use in an agent system: routing and loading (context engineering), skills derived from theory (two-layer execution: methodology as the fast path, theory as live fallback, promotion by recurrence), codification once stable (the prototype note: cheap to reject while in prose, expensive once bound). Craik supplies why holding a model pays — try alternatives on the model before the world — cited with the `(snapshot required)` marker. **This section is where "theory-mediated methodology" gets defined.** *Sources:* Argyris ingest (9 quotes: theories-in-use, single/double loop, self-sealing); Craik ingest (marker only). *Notes:* an-action-model-matters-only-through-its-consumption-path; theory-and-methodology-form-a-two-layer-execution-system; a-natural-language-theory-is-a-prototype-codified-or-rejected; definitions/system-definition-artifact.

5. **The reflective turn.** When the retained theory is about the system's own operation. Argyris's double loop — questioning the governing objectives and policies rather than correcting within them — is the revision of the decomposition, not optimization inside it (learning-inside-a-fixed-decomposition). Conditions: membership, interpretation, retention (theory-mediated-self-improvement note), plus Naur's three tests on any interpreter-plus-artifact composite: program-specific acquisition, provision of premises the interpreter cannot regenerate, dispositional reliability. *Notes:* theory-mediated-self-improvement-needs-interpretation-and-retention; design-rationale-must-preserve-unregenerable-decision-premises; definitions/reflective-system; learning-inside-a-fixed-decomposition-inherits-its-mistakes. *Source bound:* Argyris's retained text says double-loop *questions* governing variables; that it *changes* them is our reading.

6. **What counts as evidence — kept from the current draft.** Accumulation versus compounding; the three diagnostic tests (occurrence, revision surface, compounding); the later-episode protocol. Ashby as the theory-free contrast: ultrastability is operative and non-cumulative, adaptation with no theory to revise. The six-system table shrinks to one paragraph and a pointer to the evidence notes; HyperAgents as the closest later-episode test, one paragraph; the Gödel machine as the judgment-free limit case. *Notes:* improvements-can-accumulate-without-compounding; compounding-is-tested-in-later-improvement; accumulation-counts-dependence-through-the-retained-result; evidence/six-reported-self-improvement-paths. *Sources:* Ashby ingest; existing system ingests.

7. **Commonplace as testbed, with its own episode as witness.** What can be shown: installation and reuse; the behavioral-authority model exposed and made a revision target; tag-README marks as convention codified into validation. What cannot: a traced case of a retained theory producing a later improvement. Then the Naur note's own history as a worked case of the article's claim applied to the article's machinery: two full passes were right as critique and drifted as repair; the repair needed the note's theory, which no pass input carried; one operator sentence supplied it each time. In Argyris's terms the pass does single-loop repair within the gates and its self-assessment is self-sealing. In Naur's, the pass is group B. Keep this to one section; it is evidence about one note. *Workshop:* [popperian-maintenance-episode, fifth episode](../popperian-maintenance-episode/fifth-episode-critique-without-repair.md). *Notes:* evidence/commonplace-as-a-reflective-system; evidence/tag-readme-trace-observed-causal-connection; reference/proposals/revise-behavioral-authority-decomposition.

8. **The remaining frontier — direction.** Adjoiner Part 2: LLMs propose and judge; choosing what to work on under a fuzzy objective stays human. This is Naur's third capability — judging a *new demand's* similarity to what exists — at the level of the system's own agenda. Self-direction is cheap exactly where the objective is narrow (DGM); keeping it broad keeps direction human. *Sources:* adjoiner Part 2 (consumed, file deleted); DGM ingest. *Notes:* a-proximate-target-is-checked-for-achievement-not-for-warrant; self-improvement-is-relative-to-a-declared-objective.

9. **What remains to test.** The two experiments from the current draft, unchanged in substance: the objective-level ablation and the later-episode comparison with frozen-artifact and simpler-memory variants, tasks requiring decomposition revision. Add: the Naur tests as pre-registration criteria for what would count as a composite holding a theory.

## From the current draft: keep, shrink, cut

| Current section | Disposition |
|---|---|
| TL;DR | rewrite around the new spine; keep the honesty about untraced compounding |
| Compounding is the payoff | keep (→ §6) |
| Three diagnostic tests | keep (→ §6) |
| Why reflection matters: the revision surface | keep the decomposition argument (→ §5); the harness-optimizer example moves to §6 |
| Evidence from reported systems (two tables) | shrink to one paragraph + pointer; HyperAgents paragraph kept (→ §6) |
| A proof-governed limit case | keep, one paragraph (→ §3 or §6) |
| Commonplace as a human-inclusive testbed | keep, add the fifth-episode witness (→ §7) |
| What remains to test | keep (→ §9) |
| Where to go next | rewrite pointers |

## Source and grounding status

| Source | Role | Quotes retained |
|---|---|---|
| Naur, *Programming as Theory Building* | hook, both halves, three tests | 19 |
| Popper, *A Realist View of Logic, Physics, and History* | what a theory is; consumption as criticism | 8 (no "World 3" label in this text) |
| Argyris, *Organizational Learning and MIS* | espoused/theory-in-use; single/double loop; self-sealing | 9 (OCR artifacts preserved; "changes" governing variables is our reading) |
| Craik, *Hypothesis on the Nature of Thought* | why a model pays | none — `(snapshot required)` marker; two-column OCR interleaving |
| Ashby, *Design for a Brain* | theory-free contrast | see ingest |
| Pearl 1994 | codification end, if §4 needs it | see ingest |
| AutoSaddler, OpenWiki | systems-table candidates only | see ingests |

## Open

- Whether §7's self-witness belongs in an outward-facing article at all, or only as a pointer to the workshop. Argument for: it is the one place the article's claim is tested on its own machinery. Argument against: it is one note, one day.
- Whether the Popper frame displaces "reflective self-improvement" from the title. The pillar is theory-mediated methodology; reflection is the case where it turns on the system itself.
- The adjoiner's candidate note ("LLMs supply the proposer and the judge; direction under a fuzzy objective is the remaining human function") still has no home; §8 of the draft consumed the argument into the article without a note, and the adjoiner file is deleted. If the claim is wanted as a note, the article's §8 is now the source text.
