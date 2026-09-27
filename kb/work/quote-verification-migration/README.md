# Quote verification migration

## Commission and intended outcome

On 2026-09-27 the operator commissioned this workshop to implement the
[quote occurrence location and verification proposal](../../reference/proposals/quote-occurrence-location-and-verification.md)
after reviewing and revising it the same day. The proposal's recommended
candidate is: one shared matching core consumed by the existing quote
checkers, with a uniqueness rule and a containment rule for optional ranges;
ingest extracts rewritten from the `Source extract (verbatim)` list item into
the attributed blockquote form the analysis results already use; normalization
chosen by source kind; and an optional version binding in the shared citation
record that KB citations leave empty. The proposal holds the design, its
measurements and its rejected options. This workshop holds the work of
carrying it out and the records that work produces before an ADR exists.

The intended outcome is that every tracked quotation under the three contracts
passes the stronger verification, that two parsers and one matcher replace
three of each, and that the change is recorded as an ADR adopting the proposal
and amending [ADR 073](../../reference/adr/073-untracked-source-snapshots-require-ingest-grounding.md),
whose Quotes section contract names the list-item form.

## Sequencing

The proposal allows the shared core to land before the ingest rewrite, since
the core fixes the observed problem by itself. The stages below follow that
order. Code stages are ordinary commits with tests and need no workshop
record; the records this workshop owns are named under each stage that
produces one.

1. **Shared core.** Extract one matching function from
   `quote_verification.py`, `validation.py` and `agentic_analysis.py`; split the
   prose checker's fused parse, resolve and match function so both parsers
   yield the shared record; add the uniqueness and containment rules; choose
   normalization by source kind. Tests per the proposal's acceptance evidence.
2. **Sweep over notes and analysis results.** Run the new core over the
   tracked corpus under the existing syntax. Record: the failure list with a
   disposition per case, and for each edited citation whether the citation
   alone changed or the claim did. Refresh only the hashes those edits touch.
3. **Emphasis decision.** Inspect the 10 ingest extracts whose match depends
   on emphasis stripping and decide whether snapshots of code repositories use
   the code normalization rule. Record: the decision and the cases.
4. **Ingest rewrite.** Script the Quotes-section rewrite for the 158 ingests
   with extracts, changing no quoted bytes. Record: the pre- and post-rewrite
   match comparison for the ingests and for every note that cites them. Amend
   the ingest type template, the grounding skill's append step, and the
   ingest checker.
5. **Legacy review quotes.** Run the blockquote parser and resolver over the
   29 `> ---` quotes under `kb/agent-memory-systems/`. Record: which resolve
   against their pinned GitHub blobs and the disposition of any that do not.
6. **ADR.** Write the ADR adopting the proposal and amending ADR 073, archive
   the proposal per the design-proposal lifecycle, and close this workshop.

## Coordination

The [agentic-analysis-output-documents](../agentic-analysis-output-documents/README.md)
workshop is redesigning the analysis result format. Stage 2's sweep over
analysis results should run on the format that will survive, and any edits it
makes to retained results must not race that workshop's rewrites. Before
stage 2 touches a retained result, agree with that workshop which lands first
for the affected runs, or restrict stage 2 to reporting until the format
settles. The other stages do not touch analysis results.

The measurements the proposal rests on were taken on 2026-09-27 over the
tracked corpus. If stages 2 or 4 run much later, rerun the measurement first;
the counts in the proposal's current-state section are anchors, not
guarantees.

## Closing condition

The ADR is written, the stage 2 and stage 5 failure lists are empty or every
remaining item is explicitly deferred with a reason, the stage 4 comparison
shows no lost matches beyond the measured repeats, and every affected hash
record agrees. Then delete this directory and remove its entry from
`kb/work/README.md`.
