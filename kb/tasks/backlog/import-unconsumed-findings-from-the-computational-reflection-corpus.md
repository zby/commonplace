# Import the unconsumed findings from the computational-reflection corpus

## Idea

Consume the parts of the seven computational-reflection ingests under `kb/sources/` that no note currently cites. An audit of the citation surface (2026-07-26) found that outside `kb/sources/` the corpus is cited by exactly two notes — `kb/notes/definitions/reflective-system.md` and `kb/notes/reflective-coverage-is-graded-across-representational-forms.md` — and both import definitions and taxonomy only. Four specific findings sit extracted in the ingests with no consumer:

- **The Brichau import, already queued at ingest time.** `kb/sources/brichau-et-al-2002-towards-linguistic-symbiosis.ingest.md` closes with a Recommended Next Action naming its target: add the syntactic-versus-semantic ("look" versus "feel") mapping distinction and the concrete mismatch inventory — result cardinality, argument binding, failure, control flow — to `kb/notes/unified-calling-conventions-enable-bidirectional-refactoring.md`. That note still cites neither Brichau nor Gybels. The unresolved cases (multi-way methods, multiple results) are the corpus's closest thing to a negative result: full reflection on both sides, and some mappings still did not close.
- **Maes's understandability warning, which cuts against one of our notes.** Maes 1988 holds that self-modification makes semantics more open-ended and *reduces* external understandability and control (printed pp. 2, 8). `kb/notes/reflection-may-lower-oversight-cost-when-its-rationale-is-faithful.md` argues nearly the opposite for artifact-level reflection and does not engage the classical prediction. Whether the note rebuts it (prose diffs carry rationale; 1980s self-representations did not) or must qualify against it is exactly the kind of tension the note should state.
- **Implicit versus explicit reflection as a frame for the retrieval wire.** Maes 1988 (printed pp. 17–18) separates interpreter-forced activation from program-invoked activation. Commonplace's retrieval wire is entirely explicit in this sense, which is one framing of `kb/notes/retrieval-failure-is-reflection-failure.md`; harness-enforced context loading would be the implicit analogue.
- **3-KRS granularity and interpreter-conferred force.** Maes 1987 (printed pp. 151–154) shows reflective behavior attachable per instance, message, or class, and a meta-object having force only because the interpreter's protocol consumes it. That is a precedent for typed frontmatter being operative only through a validator — the `kb/notes/definitions/behavioral-authority.md` point.

Two smaller items from Smith 1984 are recorded but lower value: the finite implementation of the reflective tower (meta-level regress is boundable), and his judgment that 3-Lisp's reflective access was *too* fine-grained (self-representation granularity can be overdone).

## Why

The corpus is load-bearing for the KB's foundations cluster and the outward article, but the KB currently draws on maybe a third of what the ingests extracted. Two of the four items are not additive detail — the Maes understandability warning is a live tension with a shipped note's central claim, and the Brichau mismatch inventory is evidence for the silent-failure risk at the prose-symbolic crossing that `kb/notes/definitions/codification.md` and the coverage note both assert. Leaving extracted-but-unconsumed findings in ingests is also the failure mode the KB names for itself: retrieval failure is reflection failure.

## Rough Scope

- Apply the Brichau and Gybels mapping distinction to `unified-calling-conventions-enable-bidirectional-refactoring.md`, with the mismatch inventory as the concrete content.
- Decide whether `reflection-may-lower-oversight-cost-when-its-rationale-is-faithful.md` rebuts or qualifies against Maes's understandability warning, and say so in the note with the citation.
- Assess whether implicit/explicit activation earns a place in `retrieval-failure-is-reflection-failure.md` or is only a framing device.
- Assess whether 3-KRS granularity strengthens `behavioral-authority.md` or duplicates what it already says.
- Run `cp-skill-connect` on each edited note.

## Why Not Now

None of it blocks anything. The definitional core the KB depends on is already imported and audited, and `kb/work/self-improvement-cluster-operationalization/external-theory-evaluation.md` scored that borrowing faithful. These are enrichment and one tension to resolve, not a correction to shipped claims.

## Trigger to Activate

Any of: work resumes on the self-improving-systems cluster or the outward article; the oversight-cost note goes to review and the missing engagement with Maes surfaces as a warning; or `unified-calling-conventions-enable-bidirectional-refactoring.md` is edited for any reason, at which point the queued Brichau import should ride along.
