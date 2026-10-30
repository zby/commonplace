# Vocabulary: the brief's terms against the KB's

Written 2026-10-30 before any draft, because
[load-bearing vocabulary collisions should be prevented at write time](../../theory/vocabulary-collisions-prevented-at-write-time-not-read-time.md):
natural language has no namespace, co-loaded notes merge senses silently, and
the remedy is one term per sense plus compounds for new senses. A new name
earns its place only where it reduces what a reader must extract
([minimum viable vocabulary](../../theory/minimum-viable-vocabulary-is-the-naming-set-that-most-reduces.md)).

Counts are files under `kb/theory`, `kb/reference`, `kb/types` and
`AGENTS.md` containing the term, from `rg -il` on 2026-10-30.

## Terms with a collision

| Brief's term | KB's existing sense | Collision | Decision |
|---|---|---|---|
| **commitment** ("provisional commitments about what to believe, investigate, construct, or pursue") | A retained resolution the evidence does not entail; becomes ground truth at commit ([commitment, not derivation](../../theory/commitment-not-derivation-creates-new-ground-truth.md)). Split into explanatory and constructive. | The brief's decisions about what to investigate or pursue are mostly not retained. The KB calls those [lightweight search control](../../theory/lightweight-search-control-does-not-license-adoption.md) or a branch choice. | **Keep the KB sense.** Write "search judgment" for an unretained decision about where effort goes, "commitment" only for a retained resolution. The thesis then reads: open-ended work is recursive search control over which commitments to develop, plus gated commitment when warrant arrives. |
| **provisional** ("provisional commitment") | Two uses. (1) The status of a search-control branch choice that backtracking can revoke ([backtracking keeps lightweight search control provisional](../../theory/backtracking-keeps-lightweight-search-control-provisional.md)). (2) Explicitly excluded from "tentative": a theory is tentative by status, not "provisional or hesitant in the everyday sense" ([tentative theory](../../theory/definitions/tentative-theory.md)). | "Provisional commitment" merges a search judgment with a retained commitment and sounds like a tentative theory. | **Drop the compound.** Theories are tentative; search judgments are provisional; retained commitments are revisable by supersession and need no adjective. |
| **allocation** ("resource allocation", "allocating bounded resources") | Assigning decision-bearing functions to humans or computation ([computationally directed self-improvement is a reallocation](../../theory/computationally-directed-self-improvement-is-a-reallocation.md)). Also "search allocation" for distributing search across branches ([open-ended improvement allocates search](../../theory/open-ended-improvement-allocates-search-before-evaluation.md)). | The brief means dividing effort among investments. Three senses would co-load. | **Use the compound "effort allocation"** for the brief's sense in all new text; leave the existing notes. "Search allocation" stays for the branch sense; it is a case of effort allocation and may be written as such. Do not rename the reallocation note. |
| **worker** ("bounded workers") | A delegated agent that receives a packet and works inside a parent's authority (`AGENTS.md` Delegation; `kb/types/instruction.md`; 74 files). | The brief means any resource-bounded agent, human or model, doing knowledge work. In Commonplace text "a bounded worker" reads as a sub-agent with a small context. | **Tolerated; recorded in the [collision ledger](../../reference/vocabulary-collision-ledger.md).** The general sense rarely needs a noun and the surfaces rarely co-load. Write "actor" (already used generally in [methodology closure](../../theory/a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md)) or the specific noun. The [inventory](./search/worker-rename-inventory.md) shows "sub-agent" is not a valid replacement for the delegation sense (headless workers are defined as not sub-agents), so a fallback rename would need a third role word. |
| **general computational environment** | Absent (0 files). Three neighbours, none the same thing. The [computational-model tag](../../tags/computational-model-README.md) covers how LLM programs execute (select/call form, scoping, scheduling): formal models of execution, not an endpoint. The [software house](../../theory/definitions/software-house.md) is the endpoint for one kind of work: developing software for external users. The [universal knowledge framework](../../theory/a-universal-knowledge-framework-demotes-content-taxonomies-to-defaults.md) note is about framework design (local contracts, guarded defaults), not about the environment's generality across kinds of work. Generality claims must declare a [universality axis](../../theory/universal-software-factory-needs-a-declared-universality-axis.md). | The brief's term names a fourth thing: an environment general across *kinds of knowledge work* (science, software, legal drafting, exploration), of which the software house would be the software-specific case. Nothing in the KB names that. | **Define it or do without it; do not use it undefined.** If the architecture-level proposal needs the endpoint named, write a definition note with its universality axis declared (the covered class of knowledge work, supplied inputs, adequacy relation, resource bounds), and relate it to the software house as a special case. If the proposal can state its conjecture as "the same support generalizes from theory building to other kinds of knowledge work" without naming the endpoint, do that and defer the term. Operator call on which. |
| **economic conjecture** (the guess that justifies investing) | Absent. The nearest is "expected marginal net return" in the [machinery-investment note](../../theory/an-optimal-long-run-learning-strategy-invests-in-its-own-machinery.md), used once. "Value" is taken: [coordination value](../../theory/definitions/coordination-value.md), [information value](../../theory/information-value-is-observer-relative.md), "selection values are not one number". | "Value conjecture" would collide with three value senses. | **Do not coin yet.** Write the plain phrase ("a guess about what an investment will return") until a note needs the term more than once. If one does, "return conjecture" is the candidate: "return" is already the machinery note's word. |
| **epistemic work** (the operator's term for the shared layer) | Absent (0 files). The KB has "knowledge work" (the declared objective in [Commonplace as an instrument](../../reference/commonplace-as-an-instrument.md); 6 files) and "theory building" (what a [theory builder](../../theory/definitions/theory-builder.md) does: propose, derive, criticize, blame, revise, select). | The claim "epistemic work is the shared layer of knowledge work" needs the layer named by a term distinct from "knowledge work". "Epistemic work" is undefined; "theory building" is registered but narrower in sound, though its operation list covers what the brief means. | **Operator call.** Recommended: "theory building". It is registered, its operations are listed, and the claim becomes Popperian in form: theory building is the layer every open-ended kind of knowledge work shares. If the operator means more than theory building (for example warrant tracking as a separate activity), "epistemic work" needs a definition note before use. |
| **routine** ("convert knowledge work into routine") | Ordinary English only (24 files: "routine cases", "routine reliance", "routine work"). The KB's technical names are for the operation, not the state: [constraining](../../theory/definitions/constraining.md) narrows a named consumer's interpretation space; [codification](../../theory/definitions/codification.md) is its symbolic region. | The operator's thesis uses "routine" as a state of work (performed by a named consumer without fresh judgment) that no KB term names. Semantic routine = natural-language-constrained work; symbolic routine = codified work. | **Operator call.** Option A: keep "routine" ordinary and write "constrained" and "codified" for the two states; precise, uses registered terms, clunky in the thesis sentence. Option B: define "routine" as the consumer-relative state that constraining produces, in a definition note, when the routine-conversion note survives its test. Recommended: A now, B only if the note is extracted and uses the word more than a few times. |

## Terms without a collision

| Brief's term | KB use | Note |
|---|---|---|
| open-ended | 67 files, one sense: consequential branches are generated during the process. | Matches the brief. |
| knowledge work | The declared objective's term. | Matches the brief's broad sense. |
| investment, invest | Ordinary, plus the compound **reflective investment** for method-level investment (machinery note). | Use the compound when the method level is meant. |
| bounded | "Bounded context", "bounded observer", "bounded model", "bounded evidence" are compounds with fixed senses. "Bounded resources" is ordinary. | Avoid "bounded worker" (above). |
| economic, economical | Ordinary (37 and 11 files). No layer or discipline is named "economics". | Keep ordinary. Do not write "the economic layer" as if it were a registered level; the library grounds allocation structurally (reconciliation, direction 2). |
| cumulative, accumulation | Technical in the accumulation notes ([accumulation counts dependence through the retained result](../../theory/accumulation-counts-dependence-through-the-retained-result.md)). | The brief's sense matches: later work depends on retained results. |
| conjecture | Popperian sense throughout. | Already separated in the framing: the workshop's hypotheses are conjectures; an actor's guesses about return are guesses. |
| tentative | Registered (tentative theory). | Use only for theories. |

## Defaults applied (2026-10-30, operator chose not to block on them)

1. **worker**: tolerated collision; "actor" or the specific noun in new text.
   Ledger row added.
2. **epistemic work → theory building** as the name of the shared layer.
   Reversed if a draft needs something theory building's operation list
   does not cover; then "epistemic work" gets a definition note first.
3. **routine**: ordinary word for now; "constrained" and "codified" name the
   two states. Define "routine" only if the routine-conversion note is
   extracted and uses it often.
4. **general computational environment**: not used. The architecture-level
   proposal states its conjecture as "the same support generalizes from
   theory building to other kinds of knowledge work". Define the endpoint
   with a universality axis only if the proposal cannot be stated without it.

## Where the applied decisions change existing workshop text

- `README.md`: "bounded workers", "a worker allocates effort", "provisional
  commitments" in the Goal; "Workers" in the brief summary.
- `reconciliation.md`: "worker" in several places; "value conjecture" in the
  direction 1 tension and the vocabulary section (which this file supersedes).
- `handoff.md` is verbatim and is not edited.

Applied 2026-10-30.
