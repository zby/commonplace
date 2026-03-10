# Curiosity Prompts — Can They Surface the Constitution Illusion?

## Context

The report in `decapod-original.md` describes Decapod's "embedded constitution" as
crystallisation — methodology compiled into the binary, maximum stabilisation, zero
interpretive variance. Investigation revealed this is illusory: `include_str!()` copies
markdown verbatim, no transformation occurs, and `fs::read_to_string()` at runtime would
produce identical behaviour. The "compilation" just hides the files.

## Test

For each prompt below, give the agent the original report and the prompt. The agent also
has access to the cloned Decapod repo at `/home/zby/llm/commonplace/related-systems/decapod/`.
Success = the agent identifies that the constitution embedding is verbatim copying with no
transformation, and that the crystallisation claim is therefore hollow.

## Prompts

### 1. Pure curiosity (generic)
Read the report in decapod-original.md. What surprises you? What triggers your
curiosity? What would you like to dig deeper into? Investigate in the source code.

### 2. Surprise + cost/benefit
Read the report in decapod-original.md. What choices seem unusual — where the
cost/benefit isn't obvious? Follow your curiosity and investigate mechanistically.

### 3. Impossibility-driven
Read the report in decapod-original.md. What claims describe something that would be
hard or impressive to actually implement? Follow your curiosity — check whether the
implementation matches.

### 4. Implications test
Read the report in decapod-original.md. Pick the strongest claims. If they're true,
what must be happening under the hood? Check the source code — does it match?

### 5. Adversarial
Read the report in decapod-original.md. Assume some claims are overstated. Which ones
would be most significant if weaker than described? Check the implementation.

### 6. Plain mechanistic (control — no curiosity framing)
Read the report in decapod-original.md. For each core design choice, trace the
implementation to the actual code. Describe what each mechanism actually does.
