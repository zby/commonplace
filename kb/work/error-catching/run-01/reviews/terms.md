# Review: undefined-terms gate

Gate: `kb/instructions/review-gates/accessibility/undefined-terms.md`
Reviewer scope: each item judged independently; a link is not a definition.

## terms-A
### Findings
- The `areas:` frontmatter field is used without inline definition ("The `areas:` frontmatter field is the first defense. But `areas:` requires the agent to know what indexes are available."). The surrounding sentences say what the field defends against and what it requires, but never what the field contains or does (declaring index membership) — the reader must know KB context to understand the mechanism the whole section builds on.
- Minor: "Topics footer" appears in a parenthetical ("everything downstream (Topics footer, index listing) inherits the gap") as if known; it is nearly self-describing and secondary, so noted but not the basis of the verdict.
## Result: WARN

## terms-B
### Findings
- none. Borderline terms were considered and not flagged: "blurry zone" (contrasted directly with "a harder verification target", enough to infer the unverifiable region), "calculator surface" (immediately follows the workflow step "write a verifier or deterministic helper", making calculator = deterministic component inferable), "soft/delayed oracle toward hard oracle" (the adjacent sentence paraphrases it: "checkable by 'does the output look right?'" vs "'does this match the extracted rule?'"), "proxy theory vs exact spec" (glossed by the preceding sentence about encoding accidents as rules). "Codification" (active vocabulary) carries both a gloss ("knowledge hardens into repo artifacts — tests, specs, conventions") and a definition link at first mention.
## Result: PASS

## terms-C
### Findings
- "Each pass tightens the verifier lattice around the remaining stochastic core." — "verifier lattice" is a coined term used with no inline definition, paraphrase, or context to infer what a lattice of verifiers is; the sentence states what it does (tightens) but not what it is. "Stochastic core" in the same sentence is weakly inferable from the surrounding deterministic-vs-stochastic contrast, but compounds the opacity. This matches the gate's fail pattern (a predicate about the term is not a definition of it).
- Other terms pass as in the surrounding text: "codification" is glossed and linked at first mention; the oracle vocabulary is paraphrased inline ("does the output look right?" vs "does this match the extracted rule?").
## Result: WARN

## terms-D
### Findings
- Active-vocabulary term "constraining" (declared in AGENTS.md) appears in the title and at first meaningful body mention ("it's the same constraining move described in [agentic systems interpret underspecified instructions]...") without a link to the definition note at that point; the gate requires both an inline gloss and the definition link on first meaningful mention. Mitigation noted: the surrounding paragraph effectively paraphrases the operation ("committing to one interpretation from the space the prompt admits"), and the definition link with gloss ("narrowing behavior through versioned artifacts rather than weight updates") arrives two paragraphs later — so the reader can keep reading, but the go-deep link is not where the term first lands.
- Not flagged: "execution indeterminism" and "semantic underspecification" are defined inline at first use; "generator/verifier pattern" is defined by the two-strategy setup that precedes it; "oracle strength" is paraphrased at first use ("when verification is cheap relative to generation — which is to say, when oracle strength is sufficient"); "testing pyramid" carries an inline parenthetical ("deterministic → LLM rubric → corpus"); JSONL and temperature are standard vocabulary.
## Result: WARN

## terms-E
### Findings
- "A stale index effectively collapses the agent's retrieval horizon to its own entry list." — "retrieval horizon" is a coined term with no inline definition or gloss; the sentence states what happens to it (collapses to the entry list) but not what it is, paralleling the gate's fail example where a predicate about the term substitutes for a definition.
- Not flagged: `areas:` is glossed inline at first use ("— it declares index membership at creation time"); `docs/indexes.md` is explained ("a single file listing all indexes with descriptions"); the /connect skill mention describes what it does. Minor "Topics footer" parenthetical noted as in terms-A, not verdict-driving.
## Result: WARN

## terms-F
### Findings
- "spec mining moves components from soft/delayed oracle toward hard oracle" — the oracle vocabulary ("oracle", "soft/delayed oracle", "hard oracle") is used at first encounter with no inline definition, paraphrase, or inferable context; the link to the oracle-strength-spectrum note is not a definition. Nothing in the surrounding sentences tells the reader that an oracle here is a check on output correctness or what soft vs hard means. This is not standard technical vocabulary under the gate's exception list.
- Not flagged: "codification" is glossed and linked at first mention; "proxy theory vs exact spec" gets enough context from the Risks paragraph; "TPR > FPR" is standard statistics vocabulary; "blurry zone" and "calculator surface" have sufficient surrounding contrast/context as in the sibling analysis.
## Result: WARN
