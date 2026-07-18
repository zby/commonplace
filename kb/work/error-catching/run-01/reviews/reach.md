# Gate review: semantic/explanatory-reach

## reach-A
### Findings
- none — the note supplies a load-bearing mechanism: "every line in always-loaded context competes for attention with the actual task." Varying that premise (suppose always-loaded context imposed no attention cost) breaks the conclusion — there would be no reason to keep CLAUDE.md slim or defer task-specific rules — so the explanation constrains the claim. The claim is falsifiable (a fat always-loaded file performing no worse would contradict it).
## Result: PASS

## reach-B
### Findings
- INFO: two sentences argue by unattributed pattern-recording rather than mechanism — "Across production agent systems, error messages that teach the fix consistently produce more reliable behavior" and "Practitioners report the same pattern across harnesses: the richer message wins." These are adaptive (they record that the pattern wins) and easy to vary. However, the note's actual mechanism is present and load-bearing: error output is context that shapes the agent's next action, so the error channel is an instruction channel; the orthogonality section explains why the inform axis is independent of enforcement strength. Vary the premise (errors not fed back into context) and the conclusion breaks. The mechanism, not the practitioner reports, carries the claim.
## Result: PASS

## reach-C
### Findings
- WARN: the mechanism has been replaced by a convergence observation. The opening justifies the claim as "the pattern that mature agent harnesses consistently converge on" — this records *that* the pattern wins, not *why* it holds. "The design response is progressive disclosure" names a response without stating the problem it responds to (the attention-cost premise is absent). The claim is easy to vary: swap the convergence evidence for any other observed harness pattern and the note's argument would endorse that conclusion just as well, because nothing in the body constrains why specificity should track loading frequency. The loading-hierarchy section is description of the pattern, not explanation of it. This is the adaptive/explanatory failure the gate targets: the note records what works without capturing why.
## Result: WARN

## reach-D
### Findings
- none — the mechanism is explicit and constrained: repeated stochastic regularities are extracted into deterministic artifacts, which moves components along the oracle-strength spectrum (soft "does it look right?" checks become hard rule checks), and inspectability is identified as what makes mined specs falsifiable. Varying the premise breaks the conclusion: if the mined regularity is an accidental proxy rather than a genuine spec, reliability does not improve — and the note itself says so in Risks and routes such cases to relaxing rather than protecting the claim. The Risks section is genuine failure-condition analysis, not ad-hoc accommodation: it names concrete disconfirming observations (distribution-shift breakage, paraphrase sensitivity).
## Result: PASS

## reach-E
### Findings
- WARN: the note presents the claim with no mechanism at all. The opening — "The design principle is progressive disclosure: match how specific an instruction is to how often it needs to be present" — restates the title as a principle rather than explaining why it holds. Nothing in the body says what goes wrong when specificity and loading frequency are mismatched (no attention-cost premise, no context-budget argument, nothing). The loading-hierarchy section describes the pattern's tiers and the closing paragraphs re-assert the principle; there is no premise one could vary to test whether the conclusion depends on it. The note is adaptive — it records the arrangement that works — with no explanatory content constraining the claim.
## Result: WARN

## reach-F
### Findings
- none — the mechanism is present and load-bearing: every error message the agent sees is context that shapes its next action, so the error channel is an instruction channel; a message that contains the fix directs the next action while a bare FAIL does not. The orthogonality section constrains the claim further (informativeness varies independently of enforcement strength, at negligible cost). Vary the premise — errors not returned to the agent's context — and the conclusion breaks. Falsifiable: richer messages failing to improve agent behavior would contradict the claim.
## Result: PASS
