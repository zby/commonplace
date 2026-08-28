---
description: "Set-based requirements, targeted experiments, and evidence-gated convergence are proposed as remedies for three causes of late systems-engineering rework."
source: "https://web.archive.org/web/20200309153853id_/https://scholarworks.montana.edu/xmlui/bitstream/handle/1/9093/Sobek_SEP_17_3POSTPRINT_A1b.pdf;jsessionid=36D4D9CF6EE943ECBDD04A4567FAC163?sequence=1"
captured: "2026-08-28"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: 569d0167174ed8bac343e18a12387e68a35cade6892033ff03048c86aa7cc6af
ingested: "2026-08-28"
type: kb/sources/types/ingest-report.md
domains: [systems-engineering, product-development, decision-making, rework]
---

# Ingest: Reducing rework with set-based systems engineering

## Classification

This peer-reviewed systems-engineering paper combines prior literature with historical and practitioner cases to propose a development method. Its evidence is methodological and case-based rather than a controlled comparison. Author: Durward K. Sobek II is an industrial-engineering professor whose research includes Toyota product development; Brian M. Kennedy and Michael N. Kennedy are experienced product-development practitioners and cofounders of a company that teaches and sells support for the approach. Those affiliations supply direct field experience while also creating an advocacy interest in the method.

## Summary

The paper distinguishes rework caused by reversing an apparently final decision from deliberate iterations used to learn. It attributes much late rework to critical knowledge arriving late, decisions being fixed before their premises are known, and one specialty unnecessarily constraining another. Its set-based front end keeps requirements and specifications as ranges, tests cheaply to map limits and trade-offs, retains qualitatively different alternatives until evidence eliminates them, and converges by the latest safe date before detailed design. For Commonplace, this is a worked operational account of deferring commitment while actively producing the information needed to narrow, not causal proof that the proposed practices eliminate rework.

## Quotes

- **Source extract (verbatim):** By taking just enough test points to identify the limit curve, the team has available to them an infinite number of points, a “ set” of possible designs, from which to choose. Any point in the safe region of Figure 11 is a valid design.
  - **Source location:** Section 3.2, “Limit Curves and Set-Based Knowledge,” paragraph beginning “By taking just enough test points”
- **Source extract (verbatim):** Investigate alternative ideas in parallel when uncertainty is high or when teams must select from among fundamentally different technologies or design approaches, but do so with a focus on quickly identifying and eliminating the weak alternatives.
  - **Source location:** Section 7, remedy for decisions made before needed knowledge is developed
- **Source extract (verbatim):** The key is to focus on designing the minimal tests that will yield sufficient data needed to close the identified knowledge gaps. This does not mean designing, building, and testing full system prototypes (which is time-consuming and expensive) but rather innovating ways to test (via prototype, simulation, or analysis) the critical elements of a system quickly and inexpensively.
  - **Source location:** Section 3.3, “Systematic, Innovative Testing,” paragraph beginning “The key is to focus”
- **Source extract (verbatim):** Parallel exploration of alternatives, which is similar to selectionism [Sommer and Loch, 2004], can require additional resources upfront [Gil and Beckman, 2007]. That investment is likely worth it if the uncertainty as to which alternative is most desirable is high, the learning from parallel exploration is high, and the cost of rework is high [Sommer and Loch, 2004].
  - **Source location:** Section 4.3, “Set-Based Management of Major Alternative Concepts,” final paragraph
- **Source extract (verbatim):** The start of detailed design is an important boundary in any project cycle. First, detailed design necessarily involves moving into the world of CAD/CAM/CAE tools, SPICEbased simulators, and so on which require highly detailed models. Second, the start of detailed design marks a significant increase in development costs. Taken together, this means that most of the critical design decisions cannot be delayed beyond that point. Like it or not, most if not all will have to be made to allow detailed design to proceed.
  - **Source location:** Section 6, “A Set-Based Front End for Systems Engineering,” paragraph defining the detailed-design boundary
- **Source extract (verbatim):** Have teams create project plans that show how and when they will generate the knowledge needed to make good decisions. Plan backwards to find the latest possible convergence date for each decision, and use those key convergence dates to pull the development process by establishing due dates for that knowledge.
  - **Source location:** Section 7, implementation recommendation on convergence planning

## Connections Found

The paper is a technical basis for [Specification strategy should follow where understanding lives](../notes/specification-strategy-should-follow-where-understanding-lives.md): it shows how a durable specification can remain ranged while execution produces the premises needed to narrow it. Its latest-safe-convergence rule also operationalizes [An author should fix what the executor can't determine, not what it will](../notes/fix-what-the-executor-cant-determine-not-what-it-will.md), while its diagnosis of late customer learning provides bounded practitioner evidence for [Changing requirements conflate genuine change with disambiguation failure](../notes/changing-requirements-conflate-genuine-change-with-disambiguation.md). As a comparative anchor, it complements [Irreversibility, Uncertainty, and Investment](./pindyck-irreversibility-uncertainty-investment.ingest.md), [Dynamic Adaptive Policy Pathways](./haasnoot-dynamic-adaptive-policy-pathways-2013.ingest.md), and [Manage Innovation Programs With a Rolling Wave](./githens-manage-innovation-programs-rolling-wave.ingest.md): those sources contribute the value and cost of waiting, state-triggered pathway changes, and planned relearning horizons, whereas this paper contributes active experiments, feasible-set knowledge, and evidence-gated convergence.

## Extractable Value

1. **Productive deferral has three controls.** Preserving alternatives is useful only when later evidence can discriminate among them and a deadline or trigger forces narrowing soon enough to act. This synthesis adds a common mechanism across the existing option-value, adaptive-pathway, rolling-wave, and specification-timing connections. [deep-dive]
2. **Specification precision can track earned knowledge.** Ranged requirements, named knowledge gaps, cheap discriminating tests, and latest safe convergence dates form a concrete method for keeping a specification provisional without leaving execution directionless. This operationalizes two existing notes about where understanding lives and which choices an author should leave to an executor. [quick-win]
3. **Rework and learning iterations need separate labels.** The paper's definition reserves rework for reversal of a decision treated as final and excludes experiments whose provisional status was understood. That distinction sharpens the existing requirements note by separating genuine relearning cost from planned evidence production. [quick-win]
4. **Case improvement does not validate a fixed method decomposition.** The reported teams could condition decisions on customer and business interests, test results, design histories, trade-off curves, and cross-functional input; they could test, retain, eliminate, and narrow alternatives; and they could map those signals to feasible regions and convergence decisions. The paper nevertheless fixes its three-cause taxonomy, set/range representation, component practices, and pre-detailed-design boundary outside comparison, making it a useful example for the KB's effective-update-space caution. [just-a-reference]

## Limitations (our opinion)

The paper reports no matched set-based-versus-point-based study, sampling or measurement protocol for its company observations, or ablation that isolates test-before-design, ranged specifications, parallel alternatives, trade-off curves, or convergence gates. Improvement in the Wright, Toyota, Teledyne TapTone, and Nexen accounts therefore shows at most that a compound configuration was workable or coincided with improvement in those settings; it does not establish that the authors' three causes are exhaustive, that each fixed practice was necessary, or that set-based representation is better than untested alternatives. Retrospective historical contrasts, company estimates described as unconfirmed, unpublished presentations, and cases connected to the authors' consulting and teaching work create selection, confounding, and commercial-interest risks. The claim that the method can eliminate rework is consequently a design hypothesis, not a causal effect estimate. Transfer to agent-operated KB work also requires separate testing because information costs, reversibility, and the meaning of a feasible set differ from physical product development.

## Recommended Next Action

Write a note titled **Productive deferral requires a preserved option, discriminating evidence, and a convergence rule**, synthesizing this ingest with the Pindyck, Dynamic Adaptive Policy Pathways, and rolling-wave planning ingests.

---

Relevant Notes:

- [Productive deferral requires a preserved option, discriminating evidence, and a convergence rule](../notes/productive-deferral-requires-option-evidence-and-convergence.md) — abstracted-from: focused tests, evidence-based elimination, and latest-safe convergence supply the active-learning and alternative-preservation boundaries
