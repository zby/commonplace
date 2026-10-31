---
description: "Ledger of near collisions: terms that carry two senses the KB has judged weak enough to tolerate, with the decision a writer follows and the observation that would escalate each to a rename or definition"
type: types/note.md
---

# Vocabulary collision ledger

The vocabulary invariant says no unqualified term carries two load-bearing
senses across artifacts that can co-load; the rationale is in
[load-bearing vocabulary collisions should be prevented or visibly scoped at write time](../theory/vocabulary-collisions-prevented-at-write-time-not-read-time.md).
Not every double sense is load-bearing. This ledger records the ones judged
weak enough to tolerate, so that a writer choosing a term reads the decision
instead of re-deriving it, and so that the corpus audit the collision note
names as its detection instrument has a list of suspects.

A row is added when a workshop, review, or write finds two senses and decides
not to rename. A row is removed when the term is renamed, defined, or retired;
the commit that does so says why. The
[write-time collision controls proposal](./proposals/write-time-vocabulary-collision-controls.md)
leaves open whether reservation should be graded; this ledger is the
hand-curated form of the graded rows until a registry exists.

| Term | Senses and where each lives | Why the collision is weak | Decision for new text | Escalation trigger | Recorded |
|---|---|---|---|---|---|
| worker | Delegation: an agent that receives a packet and works inside a parent's authority (`AGENTS.md` Delegation, `kb/types/instruction.md`, skills). Ordinary: any resource-bounded person or agent doing work. | The senses sit on surfaces that rarely co-load (operating instructions versus theory), and the sentence usually disambiguates. | Use "worker" only in the delegation sense. For the ordinary sense write "actor" or the specific noun. | An instruction or theory note needs the ordinary sense as a load-bearing noun, or a misresolution is observed in a run. Renaming the delegation sense to "sub-agent" is not the fallback: an inventory (2026-10-30) found the delegation sense spans harness sub-agents and headless processes that ADR 086 and ADR 118 define as not sub-agents, with about 450 live lines, code identifiers and frozen `worker:` keys. A fallback needs a role word distinct from both. | 2026-10-30, `kb/work/open-ended-work-economics` |
| allocation | Function allocation: which decision-bearing functions humans or computation supply ([reallocation note](../theory/computationally-directed-self-improvement-is-a-reallocation.md)). Search allocation: distributing search across branches ([allocation note](../theory/open-ended-improvement-allocates-search-before-evaluation.md)). Effort allocation: dividing effort among investments. | All three allocate something, and naming the object disambiguates. | Always name the object: "function allocation", "search allocation", "effort allocation". | A bare "allocation" appears in a title, definition, or frontmatter description with one sense assumed. | 2026-10-30, same workshop |
| provisional | Technical: the status of a branch choice that backtracking can revoke ([backtracking note](../theory/backtracking-keeps-lightweight-search-control-provisional.md)). Everyday: hesitant or temporary, which the [tentative theory](../theory/definitions/tentative-theory.md) definition excludes from "tentative". | The technical use predicates a search judgment and is linked at its source. | Use "provisional" only of search judgments. Theories are "tentative"; retained commitments take no adjective. | "Provisional" is predicated of a theory or a retained commitment in a library note. | 2026-10-30, same workshop |
| operational | Codification: a *unique operational semantics* is a consequence relation fixed by an authoritative consumer's rules ([codification](../theory/definitions/codification.md), [representational form](../theory/definitions/representational-form.md)). Lineage: `operationalized-from`, the methodology-to-procedure edge ([ADR 054](./adr/054-add-adapted-from-and-operationalized-from-lineage-relations.md)). External: programming-language operational semantics, a rule-specified transition relation separate from any implementation ([Plotkin](../sources/plotkin-origins-of-sos.ingest.md)); operationalism, meaning by measuring operations ([operationalism](../sources/operationalism-sep.ingest.md)). Workshop-local: making knowledge usable for a task and executor, not adopted. | The KB senses sit in different slots: one inside a fixed phrase, one as a hyphenated link label. The external senses enter only through source ingests, which name their discipline. | Write the fixed phrase *unique operational semantics* whole, or say "consequences fixed by the consumer"; use `operationalized-from` only as a link label; gloss the external senses on first mention with the ingest. Do not use bare "operational" for the workshop sense. | A library note needs the workshop sense, or a reader confuses the codification criterion with Plotkin's. | 2026-10-31 |
