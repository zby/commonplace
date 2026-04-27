# Experiment Conclusion

This workshop does not support full automation yet.

The useful result is narrower but stronger: LLM-assisted editing improves when edits are made against an explicit contract and verified independently against that contract. The contract should expose the internal structures the text depends on, starting with claims but expanding lazily to definitions, assumptions, requirements, examples, evidence anchors, caveats, open gaps, section roles, presentation constraints, and evaluation criteria when failures show they are needed.

The loop should remain human-directed. Humans choose the active contract part, approve contract amendments, provide editorial direction, and decide warning-level tradeoffs. The model can propose candidates and verify contract preservation, but it should not silently revise the contract while pretending to edit prose.

The practical takeaway:

> We are not ready for autonomous writing revision, but contract-controlled human-directed editing is a useful primitive.

## Operational Shape

The next experiments should treat the workflow as three separable stages.

### 1. Construct The Contract

Before editing, create an explicit editing contract for the text. The contract starts sparse and names only the structures needed for the next editing goal.

Minimum contract:

- claim ledger: what the text must continue to say
- presentation constraints: how the text should be framed and what it should avoid
- rubric: what counts as improvement
- gap policy: how unsupported bridges, missing theory, or unclear commitments should be handled

Likely extensions to test:

- definitions
- assumptions
- requirements
- examples
- evidence anchors
- caveats
- section roles
- open questions
- evaluation criteria

The contract is not automatically correct. It needs explicit approval before it controls editing. Contract changes should happen in contract-editing mode, not silently during prose editing.

### 2. Edit With Saved Revisions

Editing should produce complete revision candidates, not invisible in-place changes. Each candidate should be saved so it can be compared against the current accepted state and against other candidates.

Each revision should record:

- candidate id
- active part: text, claims, presentation, rubric, gap policy, or another contract structure
- editorial direction
- base state
- changed state
- touched contract items
- brief rationale

This keeps the loop auditable. It also lets us compare candidate quality instead of relying on the last generated revision.

Forms to test:

- one editor produces one candidate
- several editors produce parallel candidates
- human side-loads a candidate
- editor revises only one selected section
- editor revises only one selected contract structure

### 3. Validate And Compare

Validation should be independent of editing. The verifier checks whether the candidate satisfies the frozen parts of the contract and whether it improves the selected goal.

Validation should answer:

- Did any protected claim, definition, requirement, assumption, or caveat change accidentally?
- Did the candidate improve the rubric target?
- Did it worsen a higher-priority criterion?
- Did it hide a theory gap instead of closing or extracting it?
- Did it preserve the intended section roles and presentation constraints?
- Is the candidate better than the current accepted state?
- If several candidates exist, which should be accepted, rejected, merged, or sent to human review?

The accepted candidate becomes the next state. Rejected candidates and verifier failures should be logged because they tell us which contract structures are missing or too weak.
