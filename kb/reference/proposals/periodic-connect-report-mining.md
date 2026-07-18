---
description: "Proposal: mine connect reports on a recurring cadence as a bulk-operation pipeline, automating the noticing-to-candidate triage step connect and kb/log.md leave unattended"
type: kb/types/note.md
traits: [design-proposal]
tags: [kb-maintenance]
---

# Periodic connect-report mining

`cp-skill-connect` writes one report per artifact and never reads the others. When several unrelated artifacts independently connect to the same hub note, or several reports hit the same maintenance gap, that convergence is real evidence for an unstated claim or a real systemic issue — but no single connect run is positioned to notice it, and nothing currently reads the reports as a set. `kb/log.md` exists to hold exactly this kind of cross-artifact observation, but it is hand-fed and, per [Where change candidates come from in Commonplace](../where-change-candidates-come-from-in-commonplace.md), "rarely used in practice." This proposal treats reading a window of connect reports for cross-report patterns as a recurring bulk operation, not an occasional manual exercise, and holds the design for when to run it, how to shard it, and who merges the results.

## Current state (as of 2026-07-18)

- Connect reports accumulate ungrouped under `kb/reports/connect/`; a sweep for reports dated within the last two weeks alone found 45.
- `kb/log.md` is a 23-line, hand-maintained, append-only file; its oldest entries date from early June 2026.
- One manual instance of the pattern this proposal generalizes ran today, in `kb/work/connect-report-mining/`: the 45 reports were split into 3 fixed batches of 15, one Sonnet subagent per batch extracted synthesis opportunities, recurring cross-report themes, systemic/maintenance issues, and candidate `kb/log.md` lines (~115-120k tokens and 2-2.5 minutes per batch), and the three raw-findings files were merged by hand into 10 deduped, ready-to-append log entries plus a triage table. No code was written; the pipeline was three parallel agent calls and one manual merge pass.
- `kb/work/bulk-operations`'s case-family list already names "connect maintenance triage" — scan generated reports, extract maintenance observations, classify each as done/open/moved/watch, promote only the durable residue — but scopes it to one report's Maintenance Observations section, not cross-report synthesis mining over a time window.
- [Where change candidates come from in Commonplace](../where-change-candidates-come-from-in-commonplace.md) names the gap directly: none of its four noticing channels — mechanical check, log, connect report, freshness status — "closes the loop unattended: promoting an entry from any of them into an actual candidate still needs an explicit maintenance or triage step nobody has automated."

## The design

Maps onto the bulk-operations pipeline (select, shard, execute, integrate, validate, close):

1. **Select** — connect reports written since the last mining run. Requires a bookkeeping marker; connect reports carry no freshness-registered lineage of their own today.
2. **Shard** — split the selection into fixed-size batches (15 was a comfortable single-subagent read in today's run). The boundary can be arbitrary (directory, count, ingest date) since the extraction schema is per-batch, not per-source-type.
3. **Execute** — one subagent per batch against a fixed extraction prompt: synthesis opportunities carried over, recurring cross-report themes, systemic/maintenance issues, candidate `kb/log.md` lines. Sonnet was sufficient today — this is read-and-compress work, not high-stakes judgment.
4. **Integrate** — merge the batch outputs, dedupe overlapping patterns across batches, and draft the final log entries. This is the step today's manual run actually needed a competent reader for: recognizing that "missing `.ingest.md`" flagged independently in two batches was one phenomenon, not two.
5. **Validate** — none beyond `kb/log.md`'s own convention (append-only, `CATEGORY: subject: observation`); there is no schema to check against.
6. **Close** — append accepted entries, delete batch scratch files, advance the last-mined marker.

## Free choices

- **Trigger.** Fixed cadence (weekly/biweekly) vs. a count threshold (every N new connect reports) vs. purely on-demand, with no scheduling at all. Today's run was ad hoc, triggered by direct request; at 45 reports in two weeks, a cadence trigger would already have fired several times had one existed.
- **Integrate-step ownership.** Agent-performed merge (fast, but an extraction prompt told to look for "recurring themes" will find weak ones under pressure to produce output) vs. human review before append (matches this KB's existing practice of gating batch KB mutations on human sign-off, at the cost of reintroducing the manual labor this proposal exists to remove).
- **Scope.** Connect reports only (today's instance) vs. widening to other `kb/reports/` subtrees that carry similar Maintenance-Observations-shaped sections (review reports, ingest reports) — widening multiplies the design surface before the narrow case has run twice.
- **Marker mechanism.** A plain marker file (last-mined date) vs. registering "the log is fresh with respect to connect reports" as a freshness target the way review pairs are — the latter turns the trigger into a `commonplace-freshness-status` query instead of a bespoke marker, but v1 freshness registers only `review-pair` targets today.

## Adoption criteria

Adopt as a skill or instruction — rather than repeating the workshop shape ad hoc — once the manual recipe has been run a second time and produces comparably durable output. This KB's own convention elsewhere is to wait for a second instance before naming or codifying a pattern, and today's run is the first. A second run is also the first real test of whether the integrate step's dedup judgment reduces to a fixed prompt or genuinely needs a fresh read each time.

## Risks

- **Manufactured convergence.** An extraction prompt instructed to look for cross-report patterns will surface marginal ones under pressure to produce output; without a skeptical integrate step, the log fills with noise rather than signal, undermining its own purpose.
- **Feeding a channel with no consumer.** `kb/log.md` is already underused on the read side — nobody currently sweeps it for entries ready to promote into notes. Automating the write side without addressing the read side turns a small hand-curated backlog into a larger unread one.
- **Standing cost for infrequent payoff.** Today's single pass spent roughly 350k subagent tokens across three batches to produce 10 log lines from two weeks of connect output. A recurring cadence multiplies that indefinitely against a log few people currently read.

---

Relevant Notes:

- [Where change candidates come from in Commonplace](../where-change-candidates-come-from-in-commonplace.md) — see-also: names the exact unautomated triage-step gap this proposal answers
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — rationale: this proposal is a concrete Search-stage mechanism for the loop that note defines
