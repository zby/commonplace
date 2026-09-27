# Quote contract change packet

This packet audits the consumers of the quotation representation and matcher.
It is consumed by migration acceptance and the final cleanup check.

| Consumer or boundary | Change and verification |
|---|---|
| Authoritative declarations | Ingest type, source collection contract, analysis-result type and validation reference name unique occurrence and checked ranges. ADR draft records alternatives and limits. |
| Scope and enforcement | Prose assertions, ingest extracts and analysis quotes share matching. Plain explanatory examples and the decommissioning legacy-review collection acquire no new source-verification obligation. |
| Resolvers and validators | `quote_verification.py`, `validation.py`, `agentic_analysis.py` call the common matcher; prose and blockquote parsers emit `Citation`. The existing shape check reuses blockquote parsing. |
| Schemas | No schema field value changes. Quote bodies are text, checked by code rather than duplicated regex schema constraints. |
| Emitters | Grounding is the sole standing ingest-quote writer; its append template is updated. The corpus rewrite is temporary tooling, removed after its comparison is recorded. |
| Skills and procedures | Grounding, writing and analysis instructions name uniqueness/containment; grounding-alignment reads blockquote bodies and attribution context. Call arguments and route-result literals are unchanged. |
| Collection and type templates | Source collection, ingest type, analysis result type, and installed-project source template updated. |
| Control plane | No root AGENTS or scaffold control-plane quote syntax exists to change. |
| Reference and ADRs | Validation reference updated. Historical ADRs 073, 076 and 078 point to ADR 094; their historical text is retained. |
| Tests and fixtures | Existing ingest fixtures use attributed blocks. Matcher, parser, range, source-binding, publication and source-kind tests exercise the shared contract. |
| Published views | No ingest paths change. Proposal retirement adds a redirect and archive entry; workshop closure needs no redirect. |
| Byte pins | Ingest/snapshot identities unchanged. Current analysis results have synchronized local copies, report hashes, result hashes, review hashes, run-state receipts and live comparison-table hashes. Frozen comparison reports and superseded runs remain historical observations. |
| Old spellings | Searched `Source extract`, `Source location`, `_quote_citations`, `INGEST_QUOTE_RE`, `normalize_text`, and navigation-only range wording across runtime, tests, contracts and references. Historical proposals/ADRs and negative-test fixtures may retain old names. |
| Generated forms | Editable installation refreshed after source-collection template change. No new entry point or dependency. |
| Fresh install | Temporary-project probe receives the attributed-block source contract and validates a migrated ingest. |
| Existing installs | Init preserves authored ingests, so an old-form ingest remains untouched and fails the new quote-shape check. Conversion is an explicit content migration, not an init side effect. Second init is byte-idempotent. |
| Diagnostics | Occurrence failures report counts; supplied ranges enforce bounds and containment. Missing source bytes are source errors, not successful matches. Conditional ingest absence is informational. |
| Acceptance probe | `install-probe.json` records fresh/existing init behavior. The publication fixture rejects an in-bounds wrong specialist range and publishes unranged quotations after correction. |
| Drift guard | Tests compare three verifier outcomes for the same quote and region, inspect shared parser records, and check that attribution bytes and separate extracts cannot satisfy a note's quote. |
| Historical witnesses | Superseded analyses, frozen comparison trials, archived proposals and amended ADRs keep their original evidence or syntax. |
| Identity conventions | Ingests retain `<slug>.ingest.md` / `.snapshots/<slug>.md` pairing. Attribution code spans must name that exact snapshot and checksum. |
| Shared exclusions | Resolvers retain their existing contract scope; ingests inspect Quotes only, and prose examples inside fenced blocks are excluded. No collection-wide verification is added to legacy reviews. |
| Relocation effects | Only proposal archival changes a durable path. No quoted artifact is relocated. |
