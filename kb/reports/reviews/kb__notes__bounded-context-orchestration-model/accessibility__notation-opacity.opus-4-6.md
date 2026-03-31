The note defines its own notation explicitly in "The select/call loop" section:

- `K` is defined: "Let: `K` be the scheduler's full symbolic state — source artifacts plus everything prior calls have produced"
- `t` is defined: "the task type of the next call"
- `M` is defined: "the maximum effective context budget for one call"
- `||P||_t` is defined: "the effective cost of prompt `P` for task type `t`"
- `select(K)` and `call(P)` are defined via the pseudocode block

All notation is defined within this note. The note uses notation extensively in formal arguments and pseudocode, which is the appropriate context for retaining it rather than replacing with plain language.

One borderline case: the opening section uses "bounded LLM calls" before defining the notation — but this uses plain language, not notation, so no issue.

pass
