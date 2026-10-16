---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: "browzy.ai memory comparison: retained sources, wiki/access structures, sessions, instructions, caches and interaction-derived outputs."
run-id: AAS-2026-10-15-browzy-ai-0a823a13a7b6-01
source-identity: "https://github.com/VihariKanukollu/browzy.ai"
reviewed-boundary: "56c253042041ee2f483a5e9b824174d746891cf4"
memory-comparison:
  version: 2
  scope: >-
    Material accumulated or changed through use: raw sources and images, wiki
    articles, SQLite source/search state, JSON index/backlinks, saved and live
    session turns reaching later calls, digest files and metadata, drafts,
    activity records, query/HTML caches, saved outputs and owner-edited schema.
    Includes their admission, maintenance and later-consumer paths. Provider-side
    use-dependent retention and personalization/history/autocomplete/cost state
    remain unresolved included alternatives. Excludes unchanged shipped prompts,
    comment-only schema defaults, bundled examples before admission, credentials,
    general runtime configuration, and a discarded compaction return. Static
    inference weights are not accumulated memory; possible provider-side changes
    through use are unresolved, not classified from the inference component alone.
  axes:
    storage_substrate:
      assessment: partial
      units:
        - scope: "Disk raw content/images, wiki Markdown, JSON manifest/index, session JSON, digests, drafts, logs, outputs and edited schema"
          assessment: known
          findings:
            - value: files
              basis: wired
              records: [memory.md#mem-obj-raw, memory.md#mem-obj-images, memory.md#mem-obj-wiki, memory.md#mem-obj-wiki-index, memory.md#mem-obj-sessions, memory.md#mem-obj-session-digest, memory.md#mem-obj-drafts, memory.md#mem-obj-activity-log, runtime.md#rt-rte-library-query, runtime.md#rt-obj-browzy-schema]
              note: "These retained objects have local file writers/readers; JSON and Markdown are encodings, not additional substrates."
          records: [memory.md#mem-obj-raw, memory.md#mem-obj-images, memory.md#mem-obj-wiki, memory.md#mem-obj-wiki-index, memory.md#mem-obj-sessions, memory.md#mem-obj-session-digest, memory.md#mem-obj-drafts, memory.md#mem-obj-activity-log, runtime.md#rt-rte-library-query, runtime.md#rt-obj-browzy-schema]
          note: "Covers the recorded disk inventory, including non-reinjected drafts and outputs."
        - scope: "SQLite sources, article copies and FTS5 access tables"
          assessment: known
          findings:
            - value: sqlite
              basis: wired
              records: [memory.md#mem-obj-raw, memory.md#mem-obj-articles-fts]
              note: "The concrete retained database is SQLite."
            - value: rdbms
              basis: wired
              records: [memory.md#mem-obj-articles-fts]
              note: "Article rows and their transactional relational database copy also establish the broader relational substrate."
          records: [memory.md#mem-obj-raw, memory.md#mem-obj-articles-fts]
          note: "FTS is lexical indexing, not vector storage."
        - scope: "Live session turns reused on later calls and process-local answer/HTML caches"
          assessment: known
          findings:
            - value: in-memory
              basis: wired
              records: [runtime.md#rt-rte-answer-question, memory.md#mem-obj-query-cache, memory.md#mem-obj-web-cache]
              note: "Host session state and Maps persist beyond their producing invocation within the process."
            - value: kv
              basis: wired
              records: [memory.md#mem-obj-query-cache, memory.md#mem-obj-web-cache]
              note: "Hashed query keys and URL keys select retained Map values; this finding concerns caches, not every session object."
          records: [runtime.md#rt-rte-answer-question, memory.md#mem-obj-query-cache, memory.md#mem-obj-web-cache]
          note: "Volatile retention is not disk persistence."
        - scope: "Use-dependent provider retention and uninspected personalization/history/autocomplete/cost state"
          assessment: uninspected
          findings: []
          records: [runtime.md#rt-cmp-llm-provider, memory.md#mem-obj-sessions, memory.md#mem-obj-activity-log]
          note: "Provider internals and the named host internals are not resolved by accepted records; their accumulated objects and substrates cannot be enumerated."
      records: [memory.md#mem-obj-raw, memory.md#mem-obj-articles-fts, memory.md#mem-obj-query-cache, memory.md#mem-obj-web-cache, memory.md#mem-obj-sessions, memory.md#mem-obj-activity-log, runtime.md#rt-cmp-llm-provider]
      note: "Recorded local stores are classified; unresolved included alternatives prevent complete inventory coverage."
    representational_form:
      assessment: partial
      units:
        - scope: "Source prose, image descriptions, article body/title/summary, messages, digests, drafts, cached answers/HTML text, logs, saved outputs and edited schema interpreted by models or people"
          assessment: known
          findings:
            - value: natural-language
              basis: wired
              records: [memory.md#mem-obj-raw, memory.md#mem-obj-images, memory.md#mem-obj-wiki, memory.md#mem-obj-sessions, memory.md#mem-obj-session-digest, memory.md#mem-obj-drafts, memory.md#mem-obj-query-cache, memory.md#mem-obj-web-cache, memory.md#mem-obj-activity-log, runtime.md#rt-obj-browzy-schema]
              note: "Text supplies content through interpretation; HTML syntax and metadata are assessed separately."
          records: [memory.md#mem-obj-raw, memory.md#mem-obj-wiki, memory.md#mem-obj-sessions, runtime.md#rt-obj-browzy-schema]
          note: "This unit covers readable text parts, not binary images or opaque provider payloads."
        - scope: "Manifest fields, roles/IDs/times, source lists, tags/backlinks, JSON index, SQL/FTS access structures and cache/HTML structural controls"
          assessment: known
          findings:
            - value: symbolic
              basis: wired
              records: [memory.md#mem-obj-raw, memory.md#mem-obj-wiki-index, memory.md#mem-obj-articles-fts, memory.md#mem-obj-sessions, memory.md#mem-obj-query-cache, memory.md#mem-obj-web-cache]
              note: "Fixed code rules consume localized identities, counts, timestamps and lexical structures. Numerical scores here are not distributed parameters."
          records: [memory.md#mem-obj-raw, memory.md#mem-obj-wiki-index, memory.md#mem-obj-articles-fts, memory.md#mem-obj-sessions, memory.md#mem-obj-query-cache, memory.md#mem-obj-web-cache]
          note: "Natural-language copies in SQL remain distinct from their symbolic access role."
        - scope: "Copied binary image payloads retained under raw/images"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-images]
          note: "The record distinguishes image bytes from text and weights, but establishes no controlled representational form for later visual consumption. A readable description cannot classify the image payload."
        - scope: "Provider-side accumulated state and uninspected host personalization/feedback parts"
          assessment: uninspected
          findings: []
          records: [runtime.md#rt-cmp-llm-provider, memory.md#mem-obj-sessions, memory.md#mem-obj-activity-log]
          note: "Inference models have parametric form, but that fact does not classify an uninspected use-dependent memory payload. Host internal forms are also unresolved."
      records: [memory.md#mem-obj-raw, memory.md#mem-obj-images, memory.md#mem-obj-articles-fts, memory.md#mem-obj-sessions, runtime.md#rt-cmp-llm-provider]
      note: "Mixed local text/access structures are split; binary and opaque alternatives prevent complete form coverage."
    lineage:
      assessment: partial
      units:
        - scope: "External source text/images/HTML admitted by ingestion or web-cache acquisition, and bundled articles admitted by demo seeding"
          assessment: partial
          findings:
            - value: imported
              basis: wired
              records: [memory.md#mem-obj-raw, memory.md#mem-obj-images, memory.md#mem-obj-web-cache, memory.md#mem-rte-demo-seeding]
              note: "Recorded acquisition imports external material or existing bundled articles."
          records: [memory.md#mem-obj-raw, memory.md#mem-obj-images, memory.md#mem-obj-web-cache, memory.md#mem-rte-demo-seeding]
          note: "The import path is known; initial external authorship, authenticity and bundled-article production remain unresolved."
        - scope: "Model image descriptions and long-source articles; deterministic short-source articles and derived index/backlink/search metadata"
          assessment: known
          findings:
            - value: authored
              basis: wired
              records: [epistemic.md#epi-rte-image-description, runtime.md#rt-rte-source-compilation]
              note: "Inference authors descriptions and long-source article proposals; this is not a finding of new true claims."
            - value: other-compiled
              basis: wired
              records: [epistemic.md#epi-rte-template-article, memory.md#mem-obj-wiki-index, memory.md#mem-obj-articles-fts]
              note: "Templates and access metadata are derived by code, independently of model authorship."
          records: [epistemic.md#epi-rte-image-description, runtime.md#rt-rte-source-compilation, epistemic.md#epi-rte-template-article, memory.md#mem-obj-wiki-index, memory.md#mem-obj-articles-fts]
          note: "Covers recorded local derivation paths, not original provenance of their imported premises."
        - scope: "Session digests and answer-derived drafts"
          assessment: known
          findings:
            - value: trace-extracted
              basis: wired
              records: [memory.md#mem-obj-session-digest, memory.md#mem-obj-drafts, runtime.md#rt-rte-insight-draft]
              note: "Summaries/proposals derive from conversational experience; draft input additionally includes wiki content."
            - value: authored
              basis: wired
              records: [runtime.md#rt-rte-session-digest, runtime.md#rt-rte-insight-draft]
              note: "Models author both outputs; trace extraction and authorship describe compatible derivation properties."
          records: [memory.md#mem-obj-session-digest, memory.md#mem-obj-drafts, runtime.md#rt-rte-session-digest, runtime.md#rt-rte-insight-draft]
          note: "These objects have different later-consumer coverage despite related origins."
        - scope: "Owner-edited schema, generated answers retained in sessions/cache/outputs, and host-authored activity records"
          assessment: known
          findings:
            - value: authored
              basis: wired
              records: [runtime.md#rt-rte-schema-change, runtime.md#rt-rte-answer-question, runtime.md#rt-rte-library-query, memory.md#mem-obj-activity-log]
              note: "Human schema editing, model answer authorship and software event-line authorship are distinct recorded producers."
          records: [runtime.md#rt-rte-schema-change, runtime.md#rt-rte-answer-question, runtime.md#rt-rte-library-query, memory.md#mem-obj-activity-log]
          note: "Raw saved turns mix user, model and host origins; saving a raw trace is not itself extraction."
        - scope: "Provider use-dependent state and uninspected personalization/feedback derivations"
          assessment: uninspected
          findings: []
          records: [runtime.md#rt-cmp-llm-provider, memory.md#mem-obj-sessions, memory.md#mem-obj-activity-log]
          note: "No accepted record resolves these production paths."
      records: [memory.md#mem-obj-raw, memory.md#mem-obj-wiki, memory.md#mem-obj-session-digest, memory.md#mem-obj-drafts, runtime.md#rt-cmp-llm-provider]
      note: "Known local imports and derivations coexist with unresolved initial provenance and included opaque alternatives."
    behavioral_authority:
      assessment: partial
      units:
        - scope: "Raw text to compiler; wiki text/history/schema to models; search snippets/cache answers/digest banner/activity display to people"
          assessment: known
          findings:
            - value: knowledge
              basis: wired
              records: [memory.md#mem-obj-raw, runtime.md#rt-bap-wiki-context, runtime.md#rt-rte-answer-question, memory.md#mem-rte-search-display, memory.md#mem-obj-query-cache, memory.md#mem-obj-session-digest, memory.md#mem-obj-activity-log]
              note: "Content supplies reference/context or a retained answer to its named consumer; delivery establishes neither truth nor compliance. Schema directions are classified separately."
            - value: instruction
              basis: wired
              records: [runtime.md#rt-bap-schema-instruction, runtime.md#rt-rte-schema-change]
              note: "Owner-edited schema supplies standing directions to later compiler/query inference."
          records: [memory.md#mem-obj-raw, runtime.md#rt-bap-wiki-context, runtime.md#rt-rte-answer-question, memory.md#mem-rte-search-display, memory.md#mem-obj-query-cache, memory.md#mem-obj-session-digest, memory.md#mem-obj-activity-log, runtime.md#rt-bap-schema-instruction]
          note: "Actual consumer paths are established, including human-only digest display; this does not attribute authority to unconsumed draft metadata."
        - scope: "Article text/tags/recency/backlinks and FTS copies at retrieval scoring"
          assessment: known
          findings:
            - value: ranking
              basis: wired
              records: [runtime.md#rt-rte-answer-question, memory.md#mem-obj-articles-fts, memory.md#mem-obj-wiki, memory.md#mem-obj-wiki-index]
              note: "Retained lexical content and metadata affect relative retrieval priority under fixed code."
          records: [runtime.md#rt-rte-answer-question, memory.md#mem-obj-articles-fts, memory.md#mem-obj-wiki-index]
          note: "Ranking is not factual validation."
        - scope: "Source membership/manifest, cache keys/generation/times, latest-session metadata and demo marker at code selectors"
          assessment: known
          findings:
            - value: routing
              basis: wired
              records: [runtime.md#rt-rte-source-compilation, memory.md#mem-obj-raw, memory.md#mem-obj-query-cache, memory.md#mem-obj-web-cache, memory.md#mem-obj-sessions, runtime.md#rt-rte-session-digest, memory.md#mem-rte-demo-seeding]
              note: "Retained IDs and controls select source eligibility, cached reuse, digest input/display and initialization branches."
            - value: enforcement
              basis: wired
              records: [runtime.md#rt-rte-source-compilation, memory.md#mem-rte-demo-seeding, memory.md#mem-obj-query-cache]
              note: "Represented source IDs skip compilation, the marker refuses repeat seeding, and expiry/generation controls refuse stale cache delivery on their bounded paths."
          records: [runtime.md#rt-rte-source-compilation, memory.md#mem-obj-query-cache, memory.md#mem-obj-web-cache, memory.md#mem-obj-sessions, memory.md#mem-rte-demo-seeding]
          note: "These are operational controls, not authorization principals or source-truth criteria."
        - scope: "Saved conversation at automatic digest transformation and retained question/answer at draft proposal generation"
          assessment: partial
          findings:
            - value: learning
              basis: wired
              records: [memory.md#mem-obj-sessions, runtime.md#rt-rte-session-digest, memory.md#mem-obj-session-digest]
              note: "Saved experience feeds a durable summary with a later human context channel; this update-consumer authority is distinct from the digest's downstream knowledge authority."
          records: [memory.md#mem-obj-sessions, runtime.md#rt-rte-session-digest, memory.md#mem-obj-session-digest, runtime.md#rt-rte-insight-draft, memory.md#mem-obj-drafts]
          note: "Draft production lacks an established later behavior-shaping consumer; optional digest-to-answer admission is incomplete. Neither establishes improved capacity."
        - scope: "Unconsumed draft/image/export parts, provider state and uninspected host personalization/feedback consumers"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-drafts, memory.md#mem-obj-images, memory.md#mem-obj-sessions, runtime.md#rt-rte-library-query, runtime.md#rt-cmp-llm-provider, memory.md#mem-obj-activity-log]
          note: "No consequential consumer is established for the first parts; provider/host internals are uninspected. No authority value follows merely from retention."
      records: [runtime.md#rt-bap-wiki-context, runtime.md#rt-bap-schema-instruction, runtime.md#rt-rte-source-compilation, memory.md#mem-obj-articles-fts, memory.md#mem-obj-session-digest, memory.md#mem-obj-drafts, runtime.md#rt-cmp-llm-provider]
      note: "Authority is local to actual consumers; parser gates and static linter code are not retained validation criteria. Unknown consumers prevent a complete authority inventory."
    write_agency:
      assessment: partial
      units:
        - scope: "Raw conversion/admission, parser/template wiki writes, metadata maintenance, host session/log/cache writes, digest/draft generation and demo seeding"
          assessment: known
          findings:
            - value: automatic
              basis: wired
              records: [runtime.md#rt-rte-source-compilation, epistemic.md#epi-rte-article-admission, memory.md#mem-rte-interactive-compile, memory.md#mem-rte-clipboard-capture, memory.md#mem-obj-sessions, memory.md#mem-obj-activity-log, memory.md#mem-obj-query-cache, memory.md#mem-obj-web-cache, runtime.md#rt-rte-session-digest, runtime.md#rt-rte-insight-draft, memory.md#mem-rte-demo-seeding]
              note: "Software/model admission occurs without a per-content human decision; source initiation and global clipboard opt-in do not make subsequent admission manual."
          records: [runtime.md#rt-rte-source-compilation, epistemic.md#epi-rte-article-admission, memory.md#mem-rte-interactive-compile, memory.md#mem-rte-clipboard-capture, memory.md#mem-obj-sessions, runtime.md#rt-rte-session-digest, runtime.md#rt-rte-insight-draft, memory.md#mem-rte-demo-seeding]
          note: "Partial skip is not passed as a compiler veto; a clipboard attempt need not successfully admit arbitrary strings."
        - scope: "Owner edits/replaces schema content"
          assessment: known
          findings:
            - value: manual
              basis: wired
              records: [runtime.md#rt-rte-schema-change]
              note: "The named owner supplies or edits the retained instruction content explicitly."
          records: [runtime.md#rt-rte-schema-change]
          note: "Excludes unchanged generated defaults; human-selected reset is replacement, not model self-revision."
        - scope: "Generic exported storage callers and initial external/bundled content production"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-raw, memory.md#mem-rte-demo-seeding, runtime.md#rt-rte-source-compilation]
          note: "Storage capability and imported authorship do not identify human versus software control at unspecified admission mechanisms. Known seeding remains automatic."
        - scope: "Provider-side use-dependent writes and host personalization/history/autocomplete/cost updates"
          assessment: uninspected
          findings: []
          records: [runtime.md#rt-cmp-llm-provider, memory.md#mem-obj-sessions, memory.md#mem-obj-activity-log]
          note: "These controls were not established in accepted records."
      records: [runtime.md#rt-rte-source-compilation, runtime.md#rt-rte-schema-change, runtime.md#rt-rte-session-digest, runtime.md#rt-rte-insight-draft, memory.md#mem-rte-demo-seeding, runtime.md#rt-cmp-llm-provider]
      note: "Known manual schema editing coexists with automatic host admission and unresolved other controls."
    curation_operations:
      assessment: partial
      units:
        - scope: "Saved conversation to retained digest and short-source prefix summary"
          assessment: known
          findings:
            - value: consolidate
              basis: wired
              records: [runtime.md#rt-rte-session-digest, memory.md#mem-obj-session-digest, epistemic.md#epi-rte-template-article]
              note: "Digest summarization and deterministic prefix/newline reduction produce reduced representations; fidelity and benefit remain unobserved."
          records: [runtime.md#rt-rte-session-digest, memory.md#mem-obj-session-digest, epistemic.md#epi-rte-template-article]
          note: "The discarded conversation-compactor return is excluded because no retained result reaches a later consumer."
        - scope: "Cache TTL/capacity/generation, saved-session pruning and bounded history eviction"
          assessment: known
          findings:
            - value: decay
              basis: wired
              records: [memory.md#mem-obj-query-cache, memory.md#mem-obj-web-cache, memory.md#mem-obj-sessions, runtime.md#rt-rte-answer-question]
              note: "Expiry, eviction and pruning forget entries or remove old turns from later input. Digest files are not pruned by the saved-session rule."
          records: [memory.md#mem-obj-query-cache, memory.md#mem-obj-web-cache, memory.md#mem-obj-sessions, runtime.md#rt-rte-answer-question]
          note: "These operations do not imply an evidence-based withdrawal protocol retaining history."
        - scope: "Exact-origin manifest replacement, daily digest-article replacement, marker-absent same-slug demo overwrite and owner schema edits"
          assessment: known
          findings:
            - value: evolve
              basis: wired
              records: [memory.md#mem-obj-raw, memory.md#mem-obj-session-digest, memory.md#mem-rte-demo-seeding, runtime.md#rt-rte-schema-change]
              note: "Recorded replacement mechanisms can revise existing retained entries; this does not establish semantic improvement or reliable long-source article merging."
          records: [memory.md#mem-obj-raw, memory.md#mem-obj-session-digest, memory.md#mem-rte-demo-seeding, runtime.md#rt-rte-schema-change]
          note: "Content replacement is distinct from index rebuilding and collision-renaming new proposals."
        - scope: "Long-source model compilation and crystallizer novelty/synthesis instruction"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-source-compilation, runtime.md#rt-rte-insight-draft, epistemic.md#epi-clm-compiler-preservation]
          note: "Guidance requests synthesis or novel connections, but no concrete output establishes a claim absent from inputs. Semantic preservation versus new claims is indeterminate; title-only old-corpus input and renaming also prevent inferring implemented merge/preservation from the prompt."
        - scope: "Provider-side and uninspected host personalization/feedback maintenance"
          assessment: uninspected
          findings: []
          records: [runtime.md#rt-cmp-llm-provider, memory.md#mem-obj-sessions, memory.md#mem-obj-activity-log]
          note: "Missing transformations prevent a complete curation inventory."
      records: [memory.md#mem-obj-session-digest, epistemic.md#epi-rte-template-article, memory.md#mem-obj-query-cache, memory.md#mem-obj-web-cache, memory.md#mem-obj-raw, runtime.md#rt-rte-insight-draft, runtime.md#rt-cmp-llm-provider]
      note: "Implemented reductions/replacements/forgetting are classified; requested synthesis remains unresolved. Duplicate detection, structural gates, reindexing and diagnostic suggestions alone establish no deduplication, promotion or history-preserving invalidation."
    read_back_direction:
      assessment: partial
      units:
        - scope: "Requested article retrieval, human search/log display, identical-key answer reuse and requested-URL HTML reuse"
          assessment: known
          findings:
            - value: pull
              basis: wired
              records: [runtime.md#rt-rte-answer-question, runtime.md#rt-rte-library-query, memory.md#mem-rte-search-display, memory.md#mem-obj-query-cache, memory.md#mem-obj-web-cache, memory.md#mem-obj-activity-log]
              note: "Code fulfills consumer requests for retained articles, snippets, answers, HTML or log lines. Delivery of that requested return is not another push."
          records: [runtime.md#rt-rte-answer-question, runtime.md#rt-rte-library-query, memory.md#mem-rte-search-display, memory.md#mem-obj-query-cache, memory.md#mem-obj-web-cache, memory.md#mem-obj-activity-log]
          note: "These request operations coexist with independent context-supply operations below."
        - scope: "Host-selected model context/history/schema, startup digest/banner input and post-answer source prefixes supplied to crystallizer"
          assessment: known
          findings:
            - value: push
              basis: wired
              records: [runtime.md#rt-rte-answer-question, runtime.md#rt-rte-schema-change, runtime.md#rt-rte-session-digest, runtime.md#rt-rte-insight-draft, memory.md#mem-obj-session-digest]
              note: "Host selectors supply retained parts to inference or startup display without a request by those consumers for the selected memory."
          records: [runtime.md#rt-rte-answer-question, runtime.md#rt-rte-schema-change, runtime.md#rt-rte-session-digest, runtime.md#rt-rte-insight-draft, memory.md#mem-obj-session-digest]
          note: "Question-driven retrieval is pull at the retrieval API and automatic supply at the answer model; startup digest display is a distinct human push."
        - scope: "Compilation request and host-selected raw/existing-article inputs supplied to the compiler model"
          assessment: known
          findings:
            - value: pull
              basis: wired
              records: [runtime.md#rt-rte-source-compilation, memory.md#mem-obj-raw]
              note: "The requested compile operation loads retained manifest, raw content and existing corpus material."
            - value: push
              basis: wired
              records: [runtime.md#rt-rte-source-compilation, memory.md#mem-obj-raw]
              note: "Host code selects eligible sources and supplies truncated raw content and old slug/title inventory to inference without a model request for those parts."
          records: [runtime.md#rt-rte-source-compilation, memory.md#mem-obj-raw]
          note: "Request fulfillment at storage and automatic supply at inference are separate operations in the same chain."
        - scope: "Draft/image/exported-output later consumers, optional digest query admission and provider/host opaque alternatives"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-drafts, memory.md#mem-obj-images, memory.md#mem-obj-sessions, runtime.md#rt-rte-library-query, memory.md#mem-obj-session-digest, runtime.md#rt-cmp-llm-provider, memory.md#mem-obj-activity-log]
          note: "Retention/capability alone supplies no direction; incomplete digest indexing and unresolved host/provider routes prevent complete coverage."
      records: [runtime.md#rt-rte-answer-question, runtime.md#rt-rte-library-query, runtime.md#rt-rte-session-digest, runtime.md#rt-rte-schema-change, memory.md#mem-obj-drafts, runtime.md#rt-cmp-llm-provider]
      note: "Both operation directions exist. Unestablished alternative read-back paths remain included rather than declared absent."
    read_back_signal:
      assessment: partial
      units:
        - scope: "Automatic wiki subset supplied to answer inference after a question"
          assessment: known
          findings:
            - value: inferred-lexical
              basis: wired
              records: [runtime.md#rt-rte-answer-question, memory.md#mem-obj-articles-fts, memory.md#mem-obj-wiki-index]
              note: "Question words drive FTS and lexical title/body/tag ranking of delivered article files."
            - value: coarse
              basis: wired
              records: [runtime.md#rt-rte-answer-question, memory.md#mem-obj-wiki-index]
              note: "Sparse-result fallback, availability, recency/backlinks and token/section limits also determine supplied context; they are not an embedding selector."
          records: [runtime.md#rt-rte-answer-question, memory.md#mem-obj-articles-fts, memory.md#mem-obj-wiki-index]
          note: "The ineffective matched-section branch does not erase the actual oversized-article selection route."
        - scope: "History and schema supplied automatically on applicable inference calls"
          assessment: known
          findings:
            - value: coarse
              basis: wired
              records: [runtime.md#rt-rte-answer-question, runtime.md#rt-rte-schema-change]
              note: "A question triggers role/recency/length selection of prior turns; prompt assembly triggers file-presence/noncomment/prefix selection of edited schema."
          records: [runtime.md#rt-rte-answer-question, runtime.md#rt-rte-schema-change]
          note: "A schema filename is not a targeted identity match among delivered memories."
        - scope: "Startup prior-session/digest selection and post-answer crystallizer article supply"
          assessment: known
          findings:
            - value: identifier
              basis: wired
              records: [runtime.md#rt-rte-session-digest, memory.md#mem-obj-sessions, memory.md#mem-obj-session-digest, runtime.md#rt-rte-insight-draft]
              note: "Startup matches latest saved-session ID to metadata and uses its digestPath; post-answer selected source slugs match wiki files whose prefixes go to crystallizer. These are actual selection matches."
            - value: coarse
              basis: wired
              records: [runtime.md#rt-rte-session-digest, runtime.md#rt-rte-insight-draft]
              note: "Startup requires missing digest/provider/three user turns and filters roles/text lengths for generation; crystallizer requires two loadable sources and limits five prefixes and answer length."
          records: [runtime.md#rt-rte-session-digest, memory.md#mem-obj-sessions, memory.md#mem-obj-session-digest, runtime.md#rt-rte-insight-draft]
          note: "Model novelty judgment disposes a new candidate; it is not an inferred-judgment selector of retained memory delivered on these paths."
        - scope: "Compiler-model input supply on requested compilation"
          assessment: known
          findings:
            - value: identifier
              basis: wired
              records: [runtime.md#rt-rte-source-compilation, memory.md#mem-obj-raw]
              note: "Existing article source-ID membership matches manifest source IDs to exclude already represented raw sources from the supplied input set."
            - value: coarse
              basis: wired
              records: [runtime.md#rt-rte-source-compilation]
              note: "The compile trigger also applies batch order/size, the short-source threshold, a 15,000-character raw prefix and a first-30 slug/title inventory."
          records: [runtime.md#rt-rte-source-compilation, memory.md#mem-obj-raw]
          note: "Identity-based eligibility and coarse prefix/batch selection are distinct; source IDs alone would not establish targeted supply without the membership predicate."
        - scope: "Provider/host opaque push alternatives and other unestablished later consumers"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-cmp-llm-provider, memory.md#mem-obj-activity-log, memory.md#mem-obj-sessions, memory.md#mem-obj-drafts]
          note: "Missing directions/selectors prevent a pull-only or complete signal conclusion for these included parts."
      records: [runtime.md#rt-rte-answer-question, runtime.md#rt-rte-schema-change, runtime.md#rt-rte-session-digest, runtime.md#rt-rte-insight-draft, runtime.md#rt-cmp-llm-provider]
      note: "Each positive belongs to an actual automatic supply operation; request keys on pull-only cache reads do not add identifier push."
    trace_learning:
      assessment: partial
      units:
        - scope: "Automatic saved-session digest write followed by startup human-banner context"
          assessment: known
          findings:
            - value: "yes"
              basis: wired
              records: [memory.md#mem-obj-sessions, runtime.md#rt-rte-session-digest, memory.md#mem-obj-session-digest]
              note: "Recorded turns feed automatic summary generation, file/meta retention and a later banner consumer. Human context is the supported horizon; automatic answer-model guidance is not established."
          records: [memory.md#mem-obj-sessions, runtime.md#rt-rte-session-digest, memory.md#mem-obj-session-digest]
          note: "Wiring is qualified by caught runtime-module failures and incomplete wiki indexing; success and improvement are unobserved."
        - scope: "Answer-derived draft write in the inspected terminal/crystallizer route"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-insight-draft, memory.md#mem-obj-drafts]
          note: "The scoped search establishes a writer without an established later adoption/retrieval consumer. Proposal retention alone cannot establish yes; no canonical bounded-absence record warrants no. Human promotion and external hosts remain unresolved."
        - scope: "Activity-log/system-notice feedback to inspected history/digest consumers"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-activity-log, memory.md#mem-rte-health-review, epistemic.md#epi-rte-issue-display]
          note: "Display consumers and filtering of system notices are established, but no automatic durable corrective update is established. Without a canonical bounded-absence record these limits do not warrant no."
        - scope: "Provider-side updates, other imported trace content and uninspected personalization/feedback writes"
          assessment: uninspected
          findings: []
          records: [runtime.md#rt-cmp-llm-provider, memory.md#mem-obj-raw, memory.md#mem-obj-sessions, memory.md#mem-obj-activity-log]
          note: "No supplied corpus or inspected internal write chain resolves additional qualifying routes; absence of adapter training calls is not system-wide absence."
      records: [runtime.md#rt-rte-session-digest, memory.md#mem-obj-session-digest, runtime.md#rt-rte-insight-draft, memory.md#mem-obj-drafts, memory.md#mem-obj-activity-log, runtime.md#rt-cmp-llm-provider]
      note: "A positive wired digest route coexists with unresolved other routes. Missing later consumers are limits, not canonical evidenced absences; the positive union cannot imply complete coverage or measured learning."
    trace_source:
      assessment: partial
      units:
        - scope: "Original input of qualifying session-digest update"
          assessment: known
          findings:
            - value: session-logs
              basis: wired
              records: [memory.md#mem-obj-sessions, runtime.md#rt-rte-session-digest, memory.md#mem-obj-session-digest]
              note: "Saved user/assistant conversational turns are the original input; user text remains full, assistant text is shortened, and system notices are omitted."
          records: [memory.md#mem-obj-sessions, runtime.md#rt-rte-session-digest, memory.md#mem-obj-session-digest]
          note: "JSON timestamps/roles do not add event-streams, tool-traces or trajectories."
        - scope: "Draft and activity/health feedback routes without established qualifying later consumers"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-insight-draft, memory.md#mem-obj-drafts, memory.md#mem-obj-activity-log, memory.md#mem-rte-health-review, epistemic.md#epi-rte-issue-display]
          note: "No qualifying automatic durable behavior-shaping chain is established here, but no canonical absence record completely resolves it. Their conversational/event inputs therefore add no trace-source finding and do not warrant inapplicability."
        - scope: "Other potential provider, imported-content and host personalization/feedback learning inputs"
          assessment: uninspected
          findings: []
          records: [runtime.md#rt-cmp-llm-provider, memory.md#mem-obj-raw, memory.md#mem-obj-sessions, memory.md#mem-obj-activity-log]
          note: "Unresolved qualifying writes and original inputs prevent classification; lack of an established route does not license inapplicability."
      records: [memory.md#mem-obj-sessions, runtime.md#rt-rte-session-digest, memory.md#mem-obj-session-digest, runtime.md#rt-cmp-llm-provider, memory.md#mem-obj-activity-log]
      note: "The known digest source is conversational; unknown alternative update inputs keep the axis partial."
---

# browzy.ai memory profile

## Comparison rationale

The local memory loop separates retained source text, Markdown articles, SQLite
search copies and JSON access metadata. Their substrates and consumers are not
interchangeable. In particular, temporary raw FTS rows can support human search
without a loadable wiki article. See [MEM-OBJ-raw](memory.md#mem-obj-raw),
[MEM-OBJ-wiki](memory.md#mem-obj-wiki),
[MEM-OBJ-articles-fts](memory.md#mem-obj-articles-fts) and
[MEM-OBJ-wiki-index](memory.md#mem-obj-wiki-index). Both SQLite and its broader
relational classification are retained; neither lexical FTS nor numeric backlink
scores establishes vector storage or parametric memory.

The schema finding concerns owner changes, not unchanged shipped instructions.
Its instruction authority and manual write control are independent of automatic
article, digest and draft admission. Preview/skip does not create a per-article
human veto. See [RT-RTE-schema-change](runtime.md#rt-rte-schema-change),
[RT-BAP-schema-instruction](runtime.md#rt-bap-schema-instruction),
[MEM-RTE-interactive-compile](memory.md#mem-rte-interactive-compile) and
[EPI-RTE-article-admission](epistemic.md#epi-rte-article-admission).

Read-back is split at the request and supply operations. Retrieval APIs fulfill
requests, while the host selects and supplies articles and recent turns to the
answer model. Startup digest selection and post-answer source-prefix selection
are separate pushes. Their actual ID matches support identifier selection;
requested cache keys alone do not. See
[RT-RTE-answer-question](runtime.md#rt-rte-answer-question),
[RT-RTE-library-query](runtime.md#rt-rte-library-query),
[RT-RTE-session-digest](runtime.md#rt-rte-session-digest) and
[RT-RTE-insight-draft](runtime.md#rt-rte-insight-draft).

The digest has a retained conversational summary and a later human banner
consumer. This supports a wired trace-learning path with knowledge authority at
the human display and learning authority at the trace-to-summary update. It does
not establish an integrated automatic answer-model memory loop, successful
execution or improved capacity. The attempted daily wiki write lacks immediate
index admission. Drafts have no established later adoption consumer in the
recorded search boundary. The separate compactor return is discarded and is not
retained memory. See [MEM-OBJ-session-digest](memory.md#mem-obj-session-digest),
[MEM-OBJ-drafts](memory.md#mem-obj-drafts),
[MEM-RTE-conversation-compaction](memory.md#mem-rte-conversation-compaction) and
[RT-RTE-session-digest](runtime.md#rt-rte-session-digest).

Consolidation does not require that a summary be perfectly faithful. Conversely,
a prompt requesting novel connections does not establish implemented synthesis
of a new claim. That transformation remains not determinable rather than being
classified from its requested behavior. Prefix summaries, replacement writes and forgetting have their own
implemented warrants. Index rebuilding, duplicate identification and health
suggestions do not by themselves establish deduplication or accepted correction.
See [EPI-RTE-template-article](epistemic.md#epi-rte-template-article),
[RT-RTE-insight-draft](runtime.md#rt-rte-insight-draft),
[MEM-OBJ-raw](memory.md#mem-obj-raw) and
[MEM-RTE-health-review](memory.md#mem-rte-health-review).

Reconciliation supersedes the epistemic raw-source and wiki-article objects with
the corresponding memory objects, and supersedes the epistemic compaction route
with the memory route. This profile uses those canonical declarations; the
supersessions change citation identity, not the positive values. The textual
image-description part remains distinct from the memory image container. No
supersession makes drafts equivalent to digests or search copies equivalent to
Markdown. See [MEM-OBJ-raw](memory.md#mem-obj-raw),
[MEM-OBJ-wiki](memory.md#mem-obj-wiki),
[MEM-RTE-conversation-compaction](memory.md#mem-rte-conversation-compaction),
[EPI-OBJ-image-description](epistemic.md#epi-obj-image-description) and
[MEM-OBJ-images](memory.md#mem-obj-images).

All ten axes retain incomplete inventory coverage. The accepted memory account
leaves profile/streak/history/autocomplete/cost internals unresolved, and the
provider component does not reveal use-dependent service state. Source origin
and unspecified storage callers also prevent stronger local classifications.
These gaps neither erase the inspected routes nor license complete-value
statistics. See [MEM-OBJ-sessions](memory.md#mem-obj-sessions),
[MEM-OBJ-activity-log](memory.md#mem-obj-activity-log),
[MEM-OBJ-raw](memory.md#mem-obj-raw) and
[RT-CMP-llm-provider](runtime.md#rt-cmp-llm-provider).

Source-read log: none. Classification used only the supplied accepted records,
annotations and reconciliation. No new source passages, records or execution
evidence were added.
