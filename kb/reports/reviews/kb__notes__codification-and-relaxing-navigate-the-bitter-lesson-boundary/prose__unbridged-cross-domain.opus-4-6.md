## Result: WARN

One partially unbridged cross-domain transfer.

### Induction bias results (sequence models) to arithmetic-regime codification (general methodology)

The Ebrahimi et al. results are specifically about calculator-class state tracking with transformer architectures. The note's conclusion generalizes to all arithmetic-regime codification:

> "This means codification bets in the arithmetic regime are not merely safe-for-now; the step-by-step structure that codification encodes is the kind of regularity that persists under scaling."

The implicit bridge is: calculator-class tasks are an instance of the arithmetic regime, so findings there should transfer. But this transfer needs an explicit statement of why calculator-class results represent the arithmetic regime generally. Calculator tasks have a specific property (algorithmically determined solutions with fixed-step structure) that makes them arithmetic-regime exemplars — but the note doesn't state this, so the reader must reconstruct the shared mechanism.

A sentence like "Calculator-class tasks are paradigmatic arithmetic-regime problems — the spec exhausts the problem space — so the permanence of induction bias there provides evidence for the regime as a whole" would bridge the gap.

### Epiplexity framework — adequately bridged

The Finzi et al. transfer (information theory to codification methodology) is adequately bridged. The note states the shared mechanism: epiplexity distinguishes learnable structure from observer-relative artefacts, and codification bets are about whether a pattern is real or accidental. The informational concept maps directly onto the engineering decision.
