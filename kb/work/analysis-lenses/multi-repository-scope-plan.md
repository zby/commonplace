# Plan: bound analysis of a multi-repository system

## Commission and decision

Decide how to analyse a system whose consequential mechanisms span linked
repositories without turning each analysis into recursive dependency acquisition
or multiplying the full workflow unnecessarily. The operator commissioned this
plan on 2026-10-11, naming Ars Umbris as the case and emphasizing the balance
between useful coverage and added complexity.

The goals remain mapping the design space and finding mechanisms worth assessing
for Commonplace. Preserve the stabilized analytical roles, verification,
correction and publication machinery wherever possible. Single-repository
analysis remains the default. This plan commissions a design comparison, not
bundle support, source-ID removal or an Ars Umbris analysis run.

Produce one recommendation in `multi-repository-scope-comparison.md` in this
workshop. Return to the operator before acquisition, implementation or trials.
Retaining single-repository runs with explicit external limits is a valid result.

## Inputs and authority

Read `AGENTS.md`, [the work collection contract](../COLLECTION.md),
[workshop framing](./README.md), [design direction](./design-direction.md), and
[the analysis design brief](../../reference/agentic-system-analysis-design-brief.md).
Read the live boundary contract, boundary job, source acquisition/freezing,
quotation resolution and publication contracts as needed to establish the
current one-source guarantee and its consumers. Before recommending method
edits, read [method maintenance](../../agentic-system-analyses/instructions/maintain-analysis-method.md).

Use local stored Git objects read-only. The intake inspection located:

- Entry identity: `https://github.com/arsumbris/arsumbris`.
- Local Git repository: `related-systems/arsumbris--arsumbris`.
- Entry commit inspected: `a9f6cceedb191b8504443222d55d3106f9f36ba9`.
- Starting documents at that commit: `README.md`, `INSTALL.md`, `VERSION.md`,
  `au-engine.md`, `au-host.md`, `au-mcp.md`.
- Candidate component repositories already present under `related-systems/`:
  `arsumbris--au-engine`, `arsumbris--au-mcp`, `arsumbris--au-mcp-sdk`,
  `arsumbris--au-mcp-core`, adapters and `arsumbris--au-defaults`.

These are locators and inspection leads, not a commissioned source bundle or an
assertion that their current HEADs form a coherent release. Some local working
folders contain only `.git`; inspect committed objects without materializing,
resetting or altering the checkout. Resolve any abbreviated release commit to a
full commit using available objects and record it. If unavailable, report the
gap; do not fetch, clone, install dependencies or execute source code.

Permitted writes are the comparison, small evidence extracts under this
workshop's `measurements/`, and its README navigation. No other writer or
subagent is commissioned by this plan. Preserve concurrent unrelated work.
All method/code/schema files, source repositories, retained analyses and run state
are read-only. No analysis run, network acquisition, integration, source-ID
migration, staging, commit or worktree disposal is authorized.

## 1. Establish a useful system slice

Start with the entry documents and release description. Determine which linked
repositories are components of the shipped system, which are optional capabilities,
and which are ordinary dependencies, examples or references. Do not equate a link
with evidence-boundary membership.

Propose one bounded question or set of closely related questions useful for
Commonplace's design-space understanding. Trace enough manifests, contracts and
callers to identify the minimum component set needed to answer it. For each
candidate component, record its responsibility, exact available revision, the
claim it would support, and what becomes unknown if it is excluded.

Check release coherence using the entry repository's version information and
actual component dependencies. Do not mix arbitrary branch tips and call the
result a release. A tag is a discovery aid; full commits are the evidence pins.
Distinguish documented composition from implementation wiring and observed
execution. Do not build an exhaustive inventory of the entire ecosystem.

Stop this scoping pass once it discriminates the options below. If choosing the
question or component set requires a consequential operator preference that the
standing goals cannot resolve, return that choice rather than expanding scope.

## 2. Compare separate runs with a fixed repository bundle

Compare at least:

| Option | Question to resolve |
|---|---|
| One component run with external limits | Does it answer the selected design question usefully without inspecting linked implementations? |
| Separate component runs | Do independent accounts justify repeated workflow cost, and what additional work would establish cross-component claims? |
| One explicitly frozen bundle | Can the selected components share one run boundary while preserving source and publication guarantees at acceptable implementation cost? |

A bundle candidate means a finite, explicitly approved mapping from named
component roots to repository identities and full commits. It does not mean
arbitrary multiple sources, recursive dependency traversal or worker-controlled
acquisition. Finding another repository should yield a limit or a request to
revise the boundary, not silently extend the run.

For separate runs, identify whether components themselves fit the analysis
boundary and whether a separately commissioned composition assessment is needed.
Do not infer integration behavior merely because each component has an accepted
analysis. Count repeated boundary, verification, profile, synthesis and operator
reading work; do not invent timing estimates or assume every repository needs
all the same depth.

For a bundle, examine the minimum changes to intake, source preparation, worker
paths, quotation resolution, validation, provenance and publication identity.
Keep dependency installation and target execution outside the proposal. Explain
how source revisions remain verifiable, how partial acquisition fails safely,
and what stable public identity would represent the selected system or slice.
Compare the implementation burden with the repeated-run burden rather than
assuming one must be cheaper.

## 3. Resolve citation and source-register implications

The immediate quotation convention is path-only, with the frozen boundary
supplying source identity/revision. Do not reintroduce repeated commits or
arbitrary source IDs merely because several repositories exist.

Test whether namespaced paths such as `au-mcp/src/example.ts` plus a pinned
component manifest would disambiguate citations. Inspect collision, path escape,
missing component and explicit wrong-revision behavior. Distinguish a physical
repository component from evidence-layer/scope metadata and analyst record IDs.

Audit the current `SRC-*` consumers before proposing their removal. Determine
which checks protect real provenance or reference invariants and which only
maintain labels. Preserve useful inspected-scope, evidence-layer and access-gap
information regardless of identifier choice. Keep analyst record IDs unchanged.
Historical retained analyses must remain unchanged; identify consequences for
reading or validating them instead of assuming a mass rewrite is acceptable.

This section supplies a decision about source representation, not permission to
implement it. Do not expand the generic engine merely to preserve a hypothetical
multi-source capability with no consumer.

## Deliverable, acceptance and return

Keep the comparison operator-facing and bounded. Include:

- The selected Ars Umbris question and component map, with exact evidence pins
  and unresolved release/availability gaps.
- What each option can establish and what remains outside its boundary.
- Expected investigation, repetition and implementation costs, without false
  numerical precision.
- A recommended default and exception policy, including who approves membership
  and what happens when a worker discovers another repository.
- The citation/source-ID decision and its actual consumers.
- Change footprint separated into instructions/types, plan/layout,
  analysis-specific code and generic engine; name tests that would be needed.
- Risks, evidence against the recommendation, and the smallest next decision or
  separately authorized trial. No new acquisition is a prerequisite by default.

A partial comparison is acceptable when missing objects or unchosen scope prevent
a stronger answer. Name the prevented conclusion. Success is a useful coverage
and complexity decision, not complete ecosystem enumeration.

Add the comparison to the workshop README, validate all changed Markdown with
`commonplace-validate`, and inspect `git diff --check`, status and diff. Return
findings and validation results without committing or changing the live method.
