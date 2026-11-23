---
description: "Distinguishes a change that took effect from one that can happen again: a circuit can adjust a hidden gain twice, while a review bot can enforce a rule that bars further rule changes."
type: theory/types/structured-claim.md
traits: [title-as-claim, has-comparison, has-external-sources]
tags: [self-improving-systems, reflection, improvement-loop, learning-theory]
---

# A repeatable operative path keeps a redesign class open to revision

A change to a system matters only if it takes effect. It keeps that part of the system open to revision only if the route that produced it can produce another change of the same kind from the state it left. Call the kind of change a *redesign class*, such as "adjust this gain" or "change the review rules". For one redesign class, a path is **operative** when evidence leads to a change that is admitted, installed, and used by later operation. The path is **repeatable** when, after the change, it can still make another change of the same class to the result. A later episode in which the path changes the result again witnesses repeatability. A specified mechanism can support it in advance, within the mechanism's assumptions.

The test separates three cases that "the system can change itself" runs together. A part can be editable and never be changed by evidence. A change can be proposed and never installed. And a change can be installed and used, yet close the route to the next change.

## A worked sequence: an overshoot circuit

This is an invented illustration. A control circuit drives a motor using a gain held in a register that nothing outside the circuit can read. When a cycle overshoots its target, the circuit halves the gain. The gain starts at 8. Six questions follow the change.

1. **Representation: what part changes, and in what class?** The gain register, under the class "gain adjustment". The observer reads this from the circuit's design. The circuit has no model of its gain and exposes nothing; it only halves a number. Representation is the observer's identification of the changed part and how it acts on behavior. It does not require the system to inspect or describe itself.
2. **Determination: does evidence reach a process that produces a candidate?** A measured overshoot reaches the halving logic, which computes 4.
3. **Admission: what decides whether the candidate replaces the incumbent?** The circuit writes the new value only when overshoot exceeds a threshold. Computing 4 is not yet admitting it.
4. **Installation: does the candidate enter a live behavioral path?** The register now holds 4.
5. **Dependence: does later operation use it?** The next cycle drives the motor with gain 4.
6. **Continuity: can the path change the result again?** If that cycle overshoots, the same logic halves 4 to 2, and the following cycle uses 2. The second halving is a later episode, and it witnesses the path running from the state the first halving produced. The design supports the same conclusion in advance: while the halving logic and the writable register remain, every installed gain is open to another halving.

The verdict depends on the class. For gain adjustment, the path is operative and repeatable. For circuit redesign, such as changing the threshold, the halving rule, or what is measured, there is no path: nothing in the circuit can change those parts. A second halving shows that the circuit can change the gain again, not that it can change the rule that halves it.

The verdict does not depend on benefit. If the overshoots came from sensor noise, repeated halving may leave the motor too sluggish. The path repeats either way.

## A change that closes its own path

This is also an invented illustration, from a familiar workflow. A team's pull requests pass through a review bot that applies a rule file, and changes to the rule file go through the same bot. Someone proposes a new rule: reject any pull request that touches the rule file. Reviewers accept it, it is deployed, and the next week it rejects a pull request that tried to loosen another rule.

The first five questions pass. A concern led to the rule, review admitted it, the bot installed it, and a later rejection depended on it. Continuity fails for the class "changes to review rules" along this path, because the installed rule blocks every later change of that class. The rule file stays readable. An administrator might still edit it outside the bot, but that is a different path, and it has to be named and checked on its own. Earlier, while the rule was only a draft, it would have failed at admission: a proposed change is not an operative one. [An improvement can close the path to further improvement](./an-improvement-can-close-the-path-to-further-improvement.md) explains why a comparison of before and after performance can miss this loss.

## Evidence

**Tag-README verification in Commonplace.** The [tag-README trace](./evidence/tag-readme-trace-observed-causal-connection.md) records one real change in verification machinery. The `learning-theory` tag index had grown to 18.8 KB and 55 entries, and its promise to list every member could no longer be checked; a maintainer measured the size by hand. An agent drafted a split into two types. ADR 026 recorded the decision, and commits added a `complete` mark, schema support, validator checks, and tests, which the maintainer reviewed and merged. When the `learning-theory` head later adopted a coverage mark, the new check caught a member that the documented `rg` search had missed: a note whose tags used block-style YAML.

Read against the test, the redesign class is "how completeness of a tag head is verified". The ADR, review, and commits record determination, admission, and installation. The caught member shows dependence: a later operation used the installed check, and its result differed from the old search. The record does not show continuity. The catch is a use of the new check, not a second redesign of the check. A continuity witness would be a later change to the mark, schema, or validator made through the same route. The maintainer noticed the problem. An agent connected it to an earlier finding about incomplete indexes and drafted the split; the maintainer reviewed and merged the change. The decision, tests, and validator let a later maintainer trace the change without relying on either participant’s memory.

**Agno's improvement loop.** In a practitioner account, a coding agent derives probes from a target agent's specification and stored sessions, runs them against the live agent, and fixes failures: "It edits the agent code in agents/radar.py, restarts, and re-runs only what failed." ([source](../sources/how-to-recursively-improve-your-agents-2084301728363462919.ingest.md), verbatim) The walkthrough continues the loop "until every probe passes" ([source](../sources/how-to-recursively-improve-your-agents-2084301728363462919.ingest.md), verbatim). If the self-reported account is accurate, each edit after a restart applies to the target state the previous edit produced, so the loop repeats changes in one class: edits to the target agent's instructions, tools, parameters, and code. The account says nothing about changes to the coding agent, the probe derivation, the specification, the judge, or the platform. It shows target-side repeatability only. It neither shows that the surrounding method can be revised nor that it cannot.

**Six reported self-improvement paths.** The [six-path inventory](./evidence/six-reported-self-improvement-paths-expose-bounded-redesign-surfaces.md) separates declared editability, installation, and later use. Accumulated Behavioral Rules installs and loads a rule file, but without a no-rule baseline or per-rule isolation it does not establish dependence. HyperAgents comes closest to a continuity witness among the six: selected descendants' revised task and meta-agent code becomes the program that later generations modify and evaluate. That evidence covers task and meta-agent code. Evaluation and the outer archive loop stay outside the editable program, so the same runs establish nothing about those classes.

## Reasoning

The first question fixes what the reader is testing: can the circuit change the gain, or can it change the halving rule? Naming that distinction is the reader’s task, not a step the circuit performs. The remaining questions ask what actually produces the change and whether it can happen again. Without determination, evidence does not reach the change. Without admission, a candidate never displaces the incumbent. Without installation and dependence, the change never alters operation. Continuity asks whether the transition left the path usable for the next change.

Repeatability differs from five properties it is often confused with.

- **Editability.** A repository writable everywhere marks only the outer limit of what could change. A path establishes change only for the parts it actually reaches.
- **Inspectability.** The circuit is repeatable while exposing nothing, and the review bot's rules remain readable after its path closes. Inspection helps an observer check a path and helps people repair it, but it is neither necessary nor sufficient for repeatability. Complete inspectability of a system does not keep a path open if a revision disables admission or installation.
- **Benefit.** A path can repeatedly apply a bad criterion, as the noisy-sensor circuit does.
- **Autonomy.** People can carry out steps of the path, as in the tag-README case. Drawing the system boundary around a maintainer does not by itself establish a retained route, though. A maintainer who notices a problem, patches code from memory, and leaves only the patch has changed a system that includes them. The next maintainer cannot recover what evidence prompted the change, what admitted it, or how to challenge the result. General human capability supplied the missing steps; nothing retained them. An organization can retain such a route through issues, design records, review criteria, CI, and deployment. [Methodological and computational closure track different changes](./methodological-and-computational-closure-track-different-changes.md) treats who performs the steps as a separate question.
- **Compounding.** [Compounding](./compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md) asks whether an earlier change helped produce a later improvement. Repeatability asks only whether the next change can happen; the second halving does not need the first to have helped.

Continuity does not require a permanently fixed controller. The condition that admits changes may itself be replaced, provided the successor keeps or installs another route for the same class. In a [Gödel machine](./goedel-machines-are-a-proof-governed-case-of-self-modification.md), a licensed rewrite may replace the proof searcher that licenses rewrites; the path stays open only if the successor keeps a mechanism for another licensed rewrite.

## Caveats

- A later episode and a specified mechanism give different evidence. The episode witnesses continuity for one successor. The mechanism supports applicability to every successor only within its stated assumptions; the circuit argument fails if the register stops being writable. Neither supports a claim beyond the named class.
- The overshoot circuit and the review bot are invented. They show how the test applies; they are not observations.
- The evidence is asymmetric. The published papers describe their experimental paths, while Commonplace is read from a longitudinal repository record. Conclusions concern the classes those records establish, not whether the research teams had unreported version control, review, or CI.
- A part outside every path is not thereby a defect. A hidden evaluator may resist objective hacking, and a frozen controller may bound compute; [machinery persists by warrant, not position, in a reflective loop](./machinery-persists-by-warrant-not-position-in-a-reflective-loop.md).

---

Relevant Notes:

- [Tag-README trace](./evidence/tag-readme-trace-observed-causal-connection.md) — abstracted-from: the installed verification change and its later use, without a second redesign
- [Six reported self-improvement paths](./evidence/six-reported-self-improvement-paths-expose-bounded-redesign-surfaces.md) — abstracted-from: separates editability, installation, and later use across six reported paths
- [How to recursively improve your agents](../sources/how-to-recursively-improve-your-agents-2084301728363462919.ingest.md) — evidenced-by: bounds the target-side repetition case; says nothing about the surrounding method
- [An improvement can close the path to further improvement](./an-improvement-can-close-the-path-to-further-improvement.md) — extends: explains why an improvement comparison can miss a closed path
- [Learning inside a fixed decomposition inherits its mistakes](./learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) — grounds: explains why change inside supplied parts cannot repair an omission outside them
- [An omitted improvement-loop function and a frozen one need different repairs](./an-omitted-loop-function-and-a-frozen-one-need-different-repairs.md) — extends: classifies the fixed placements exposed once the revision boundary is located
- [Reflection buys addressability](./reflection-buys-addressability.md) — contrasts: addressability helps an observer check and repair a path but does not by itself keep it open
- [Methodological and computational closure track different changes](./methodological-and-computational-closure-track-different-changes.md) — contrasts: separates retained decision machinery from who executes it
- [Compounding is tested in later improvement, not by the accepting metric](./compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md) — contrasts: tests whether a retained change helps later improvement, not whether another change can happen
