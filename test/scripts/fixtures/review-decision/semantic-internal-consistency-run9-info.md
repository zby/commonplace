# Gate Review: semantic/internal-consistency

- Note: `kb/notes/llm-context-is-a-homoiconic-medium.md`
- Outcome: INFO

No direct pairwise contradiction across sections was found. The note's main tension is definition drift.

## Finding 1

**Severity:** INFO

The definition of "homoiconicity" drifts between the opening and the precedent survey.

The introduction defines it narrowly: program and data share one representation, with no type-level distinction. The body then broadens the term to cover several different mechanisms:

- Lisp: code/data sameness
- Emacs: same language for system and extensions
- Smalltalk: live-image self-modification
- Tcl / XSLT / Prolog / Rebol: broader fluidity between representation and execution

Those examples point in a related direction, but they are not interchangeable under the note's own initial definition. The summary claim, "blurring the boundary between using and extending," compresses these distinct mechanisms into one label.

## Finding 2

**Severity:** INFO

The prompt-injection paragraph shifts vocabulary in a way that could read as conceptual slippage.

Earlier sections argue for "no type-level distinction." The injection section says the boundary is "conventional, not enforced." Those are close, but not identical. A conventional boundary still exists; it is just weak. That wording is easier to reconcile with injection-style analogies than with the note's stronger opening claim.

This does not create a hard contradiction, but the note would be more internally consistent if it chose one of two positions and held it throughout:

- strict sameness of representation, or
- weak/conventional separation that fails under composition
