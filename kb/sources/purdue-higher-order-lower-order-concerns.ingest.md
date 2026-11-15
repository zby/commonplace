---
description: "Purdue OWL prioritizes big-picture revision while allowing surface-first exceptions; useful for separating concern priority from invalidation and option-count ordering."
source: https://owl.purdue.edu/owl/general_writing/mechanics/hocs_and_locs.html
captured: "2026-11-13"
capture: trafilatura
capture_scope: full-source
genre: official-statement
snapshot_sha256: 6b53eb2ba265e7a57f404dccc45bd23a5bec40b44a52b44058bc0e14e9aae06d
ingested: "2026-11-13"
occasion: "How should Commonplace order revision concerns, and does ordering by what a change invalidates differ from ordering by degrees of freedom?"
type: types/ingest-report.md
domains: [revision-priority, higher-order-concerns, lower-order-concerns]
---

# Ingest: Higher Order Concerns (HOCs) and Lower Order Concerns (LOCs)

## Classification

Institutional writing guidance issued by Purdue OWL, rather than a study comparing revision schedules. Author: The Writing Lab & The OWL at Purdue and Purdue University. Its institutional authorship establishes the provenance of the advice, not experimental support for its effectiveness.

## Summary

Purdue OWL recommends addressing higher-order concerns—thesis or focus, audience and purpose, organization, and development—before lower-order concerns such as sentence structure, punctuation, word choice, and spelling. This is a default priority, not a rigid sequence: experienced writers may move between levels, and lower-order errors should be addressed first when they prevent readers from reaching the thesis. The page supplies practical checks, including summarizing the thesis in one sentence, outlining paragraph topics, asking a reader to forecast the next paragraph, identifying missing support, and tracking recurring surface errors. It offers no comparative results on the effectiveness of different revision orders.

## Quotes

> When you are revising your papers, not every element of your work should have equal priority. The most important parts of your paper, often called "Higher Order Concerns (HOCs)," are the "big picture" elements such as thesis or focus, audience and purpose, organization, and development. After you have addressed these important elements, you can then turn your attention to the "Lower Order Concerns (LOCs)," such as sentence structure and grammar.
> --- `kb/sources/.snapshots/purdue-higher-order-lower-order-concerns.md` @ `sha256:6b53eb2ba265e7a57f404dccc45bd23a5bec40b44a52b44058bc0e14e9aae06d`

> Keep in mind, however, that moving between HOCs and LOCs might be a natural process for you. Experienced writers may begin with HOCs and dip into the LOCs as they revise. Inexperienced writers may revise systematically through the HOCs and then the LOCs. In addition, LOCs, such as punctuation and spelling, may affect HOCs. For example, if the first sentence of your introductory paragraph is riddled with punctuation and spelling errors, readers may not move far enough into your work to get to your thesis statement. In these cases, you should address LOCs first.
> --- `kb/sources/.snapshots/purdue-higher-order-lower-order-concerns.md` @ `sha256:6b53eb2ba265e7a57f404dccc45bd23a5bec40b44a52b44058bc0e14e9aae06d`

## Connections Found

The source is a qualifying reference for the revision-order question in [One improvement procedure over atomic instructions](../reference/proposals/one-improvement-procedure-over-atomic-instructions.md). That proposal orders work by the risk that a higher-order change will discard lower-order editing. Purdue supplies a related concern hierarchy, but does not state that invalidation rationale. Its categories also differ: organization is explicitly higher-order, whereas the proposal places flow among lower-order concerns. These categories need an explicit mapping, not an assumption that the same labels mean the same thing.

The comparison with [Solve low-degree-of-freedom subproblems first](../theory/solve-low-degree-of-freedom-subproblems-first-to-avoid-blocking.md) separates two local ordering mechanisms. The theory note prioritizes decisions with few viable alternatives to preserve options. The proposal prioritizes decisions whose changes could invalidate later work to avoid wasted edits. A thesis with many viable revisions can still invalidate substantial sentence editing; that illustrative case makes the criteria logically distinct, not empirically ranked. Purdue neither counts alternatives nor compares these mechanisms. Its reader-access exception adds another consideration: surface repair may be necessary before substantive communication can succeed.

## Extractable Value

1. **Separate invalidation risk from remaining alternatives.** These can rank the same revision differently: a flexible thesis decision may invalidate much prose, while a tightly constrained spelling correction may invalidate none. This is our comparison with the local ordering accounts, not a result established by Purdue. Commonplace should state which mechanism a revision rule serves rather than infer one from the other. [quick-win]
2. **Preserve the conditional priority rule.** Purdue supports a big-picture-first default with interleaving and reader-access exceptions, not an unconditional ban on early surface repair. A Commonplace procedure borrowing this guidance should identify when an obstructing surface defect warrants early attention. Whether this improves agent editing remains untested here. [quick-win]
3. **Map concern categories by their contents.** Purdue's inclusion of organization among higher-order concerns prevents treating all framing and flow work as lower-order merely because it concerns presentation. The proposal's existence, boundary, and placement checks are local extensions, not categories supplied by this page. [quick-win]

## Limitations (our opinion)

The page gives authoritative institutional advice, but no independent verification, comparative study, or measured revision outcomes. Its claims about experienced and inexperienced writers do not establish which schedule works best, or under what task conditions. The reader-access example explains a concrete exception to big-picture priority; it does not establish a general cost model for ordering edits. The page neither evaluates downstream invalidation nor estimates degrees of freedom. It therefore cannot settle conflicts between those local heuristics, and its advice to human writers does not establish an effective schedule for agents. The proposed Commonplace mapping is analytical transfer, not a source finding.

## Recommended Next Action

Revise the default-composition section of `kb/reference/proposals/one-improvement-procedure-over-atomic-instructions.md` to distinguish its downstream-invalidation rationale from low-degree-of-freedom ordering, explicitly map organization and flow against Purdue's categories, and preserve Purdue's reader-access exception when describing the borrowed priority rule.

---

Relevant Notes:

- [Purdue OWL: Higher Order Concerns and Lower Order Concerns](https://owl.purdue.edu/owl/general_writing/mechanics/hocs_and_locs.html) — derived-from: institutional revision guidance, including interleaving and lower-order-first exceptions
- [Solve low-degree-of-freedom subproblems first](../theory/solve-low-degree-of-freedom-subproblems-first-to-avoid-blocking.md) — compares-with: option preservation differs from concern priority and downstream invalidation
- [One improvement procedure over atomic instructions](../reference/proposals/one-improvement-procedure-over-atomic-instructions.md) — see-also: local proposal whose default ordering needs an explicit mapping to the source's categories and exceptions
