# Remote KB access via GitHub and the rendered site

Posed by the operator on 2026-11-26. [README.md](../../../README.md) and [the site homepage](../../index.md) already invite readers and external agents to consult Commonplace through its GitHub repository or the rendered HTML site (`https://zby.github.io/commonplace/`) without installing or cloning anything. This workshop investigates where that remote read path breaks down and which changes actually improve it for external agents and human visitors.

## Starting point

Commonplace's discovery architecture ([ADR 025](../../reference/adr/025-complete-generated-indexes-are-build-time-only.md), [ADR 140](../../reference/adr/140-tag-heads-are-selective.md)) assumes a local clone where agents combine curated heads with scoped `rg`, while human readers browse the ProperDocs build. Remote consumers lose `rg` on GitHub and encounter a rendered site whose search, navigation, and generated tag tails treat roughly 520 core KB pages alongside more than 5,300 bulk, in-flight, or historical pages.

See [initial-analysis.md](./initial-analysis.md) for the baseline inventory of current files, observed GitHub/site friction points, and candidate improvements split by consumer (external agents, human web readers, and GitHub browsers).

## Frozen memory survey: what still links there?

The [inbound-link inventory](./legacy-memory-inbound-links.tsv) records the checkout at `7721cc141`, before changing the entry links. Of 175 tracked Markdown pages in the survey, 76 received a relative Markdown link from a tracked Markdown file outside the collection. Of those, 49 were linked from theory, notes, articles, tags, reference, instructions, types, or agentic systems. Each row lists the distinct referring files; the CSV and schema have rows too, outside the page count. The scan uses Commonplace’s authored inline-link parser, not web traffic or a search for all path mentions. A zero does not rule out dependencies inside the archive, published redirects, code, or external citations.

## Scope and boundaries

- Keep one authoritative source of truth in authored Markdown; prefer build-time materializations over committed generated files ([ADR 025](../../reference/adr/025-complete-generated-indexes-are-build-time-only.md), [design for the first-time human, except on access cost](../../theory/design-for-the-first-time-human-except-on-access-cost.md)).
- Do not commit to larger site machinery (such as a replacement search engine, backlink rendering, or machine-readable catalogs) solely on speculation; test the current remote read path with concrete consultation tasks first so observed failure modes decide what earns implementation.
- Coordinate with [documentation-consolidation](../documentation-consolidation/README.md) on shared landing and overview surfaces and with [backlink-surfacing](../../reference/proposals/backlink-surfacing.md) if inbound-link rendering is picked up.

## Closure

Close when observed remote-use tests (at least one external-agent consultation without a local clone and a review of human entry/search flows) have identified the load-bearing bottlenecks, accepted fixes have landed in the repository or ProperDocs build, any durable design choices have been recorded in `kb/reference/` or `kb/theory/`, and unchosen candidates have been explicitly deferred or dropped.

---

Relevant Notes:

- [initial-analysis.md](./initial-analysis.md) — produces: baseline inventory of KB file counts, remote-access gaps, and candidate improvements
- [Design for the first-time human, except on access cost](../../theory/design-for-the-first-time-human-except-on-access-cost.md) — rests-on: frames remote HTML and GitHub access as distinct consumer access paths over one authority
- [ADR 025 — complete generated indexes are build-time only](../../reference/adr/025-complete-generated-indexes-are-build-time-only.md) — rests-on: establishes the local `rg` vs. build-time listing split whose remote assumptions this workshop examines
- [ADR 011 — notes must be accessible to external readers](../../reference/adr/011-notes-must-be-accessible-to-external-readers.md) — see-also: prose-level counterpart to the navigation and discovery questions studied here
- [Documentation site](../../reference/documentation-site.md) — draws-on: current ProperDocs build structure and landing-page inventory
- [Backlink surfacing](../../reference/proposals/backlink-surfacing.md) — see-also: existing unimplemented proposal for build-time inbound links on the web view
