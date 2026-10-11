# Audit an analysis

Determine how far a completed analysis can be trusted and what its session
traces teach us about the analysis process. Produce evidence that helps
maintainers distinguish local mistakes from recurring weaknesses and successful
safeguards—not a change proposal justified by one run.

Choose the inspection approach. Make consequential findings traceable to
evidence, distinguish observations from recommendations, and state what remains
unknown. Compare analysis timings across available runs to identify what drives
cost or delay, keeping differences in scope, worker profile, and parallelism
visible. Distinguish wall-clock duration from summed worker time; one run alone
does not establish a performance trend. A partial audit is useful if its limits
are clear.

Save the report under `reports/` and add it to the
[workshop's report list](./README.md). Include `run-id`, `method-commit`,
`source-revision`, and your own `reporter-profile` (harness, model, reasoning
effort; unknown where unavailable), distinct from the audited worker profile.
Leave the method, retained analysis, and run state unchanged.
