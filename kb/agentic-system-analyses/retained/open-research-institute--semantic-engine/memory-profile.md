---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "Semantic Engine memory profile: imported archives, SQLite document/chunk retrieval state and qualified canvas/Atlas alternatives."
run-id: "AAS-2026-10-17-semantic-engine-666c064cd8dc-01"
source-identity: "https://github.com/Open-Research-Institute/semantic-engine"
reviewed-boundary: "7e2481671cad01f0b4c89f2a1877d6733d7e552c"
memory-comparison:
  version: 2
  scope: "Downloaded archive files; retained SQLite roots, chunks, provenance, linkage and numerical embeddings; their admission, clearing and later query/derivation routes; generated canvas GeoJSON and its qualified browser consumer; potential Atlas-retained exports/topics and opaque downstream consumers. Initial preexisting vector provenance and external edit/admission alternatives remain unresolved. Excludes static shipped instructions/configuration as accumulated memory, transient query/comparison outputs, unused clustering results, scaffold UI state and external embedding-model weights not updated by inspected callers."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        -
          scope: "Downloaded archive files"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-archives"
              note: "Archive acquisition writes local JSON files."
          records:
            - "memory.md#mem-obj-archives"
          note: "The download implementation identifies local file retention; operation is not observed."
        -
          scope: "Derived canvas GeoJSON files"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-geojson"
                - "memory.md#mem-rte-canvas-display"
              note: "Projection affords a separate local GeoJSON artifact."
          records:
            - "memory.md#mem-obj-geojson"
            - "memory.md#mem-rte-canvas-display"
          note: "Current integration obstacles prevent treating the connected producer/consumer route as wired."
        -
          scope: "Root text, chunk text, offsets, provenance and chunk embeddings"
          assessment: "known"
          findings:
            -
              value: "sqlite"
              basis: "wired"
              records:
                - "memory.md#mem-obj-docs-content"
                - "memory.md#mem-obj-chunks-content"
                - "memory.md#mem-obj-docs-metadata"
                - "memory.md#mem-obj-chunks-embedding"
              note: "All four database parts reside in the dataset-selected SQLite file."
          records:
            - "memory.md#mem-obj-docs-content"
            - "memory.md#mem-obj-chunks-content"
            - "memory.md#mem-obj-docs-metadata"
            - "memory.md#mem-obj-chunks-embedding"
          note: "Vector encoding/coercion remains uncertain, not the declared database substrate."
        -
          scope: "Potential Atlas-retained payloads and requested topic outputs"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-atlas-export"
            - "epistemic.md#epi-rte-atlas-topics"
          note: "The inspected request does not establish remote persistence, storage substrate or later consumers; exporter initialization/schema defects also qualify reachability."
      records:
        - "memory.md#mem-obj-archives"
        - "memory.md#mem-obj-geojson"
        - "memory.md#mem-rte-canvas-display"
        - "memory.md#mem-obj-docs-content"
        - "memory.md#mem-obj-chunks-content"
        - "memory.md#mem-obj-docs-metadata"
        - "memory.md#mem-obj-chunks-embedding"
        - "memory.md#mem-rte-atlas-export"
        - "epistemic.md#epi-rte-atlas-topics"
      note: "Local files and SQLite cover the declared local inventory. Potential Atlas state remains opaque; numerical vectors do not imply a separate vector-store substrate."
    representational_form:
      assessment: "partial"
      units:
        -
          scope: "Archive tweet bodies and retained roots/chunks"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-archives"
                - "memory.md#mem-obj-docs-content"
                - "memory.md#mem-obj-chunks-content"
              note: "People interpret root text; the embedding model interprets chunk text."
          records:
            - "memory.md#mem-obj-archives"
            - "memory.md#mem-obj-docs-content"
            - "memory.md#mem-obj-chunks-content"
          note: "Text is classified separately from its JSON/SQL envelope."
        -
          scope: "Canvas GeoJSON text at map-label consumption"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-geojson"
                - "memory.md#mem-rte-canvas-display"
              note: "The qualified canvas route affords human interpretation of retained text as map labels."
          records:
            - "memory.md#mem-obj-geojson"
            - "memory.md#mem-rte-canvas-display"
          note: "The text form is identified, but database, representation and filename mismatches prevent upgrading its connected producer/consumer warrant to wired."
        -
          scope: "Archive JSON structure, chunk offsets/linkage and root access metadata"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-archives"
                - "memory.md#mem-obj-chunks-content"
                - "memory.md#mem-obj-docs-metadata"
              note: "Fixed parsing and lookup rules consume localized archive and database fields."
          records:
            - "memory.md#mem-obj-archives"
            - "memory.md#mem-obj-chunks-content"
            - "memory.md#mem-obj-docs-metadata"
          note: "Symbolic structure and linkage are separate from the natural-language content and dense embeddings."
        -
          scope: "Canvas GeoJSON geometry and IDs at map-placement/link consumers"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-geojson"
                - "memory.md#mem-rte-canvas-display"
              note: "Fixed geometry and outbound-link rules afford consumption of localized coordinates and IDs."
          records:
            - "memory.md#mem-obj-geojson"
            - "memory.md#mem-rte-canvas-display"
          note: "Numeric map coordinates have fixed geometric meaning rather than distributed embedding form; the connected route remains qualified by database, representation and filename mismatches."
        -
          scope: "Retained dense chunk embeddings at cosine-ranking consumption"
          assessment: "known"
          findings:
            -
              value: "parametric"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chunks-embedding"
                - "runtime.md#rt-bap-vector-ranking"
              note: "Distributed numerical representations influence similarity ranking, not provider weights."
          records:
            - "memory.md#mem-obj-chunks-embedding"
            - "runtime.md#rt-bap-vector-ranking"
          note: "Actual F32 normalization is unobserved; the dense representation and intended consumer are established."
        -
          scope: "Potential Atlas-retained payloads and requested topic outputs"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-atlas-export"
            - "epistemic.md#epi-rte-atlas-topics"
          note: "The inspected request does not establish remote persistence, representational form or later consumers; exporter initialization/schema defects also qualify reachability."
      records:
        - "memory.md#mem-obj-archives"
        - "memory.md#mem-obj-docs-content"
        - "memory.md#mem-obj-chunks-content"
        - "memory.md#mem-obj-geojson"
        - "memory.md#mem-rte-canvas-display"
        - "memory.md#mem-obj-docs-metadata"
        - "memory.md#mem-obj-chunks-embedding"
        - "runtime.md#rt-bap-vector-ranking"
        - "memory.md#mem-rte-atlas-export"
        - "epistemic.md#epi-rte-atlas-topics"
      note: "Separate text, symbolic access/display fields and dense numerical state. The external topic payload is not classified from its display/request label."
    lineage:
      assessment: "partial"
      units:
        -
          scope: "Archive files and source text admitted as roots"
          assessment: "known"
          findings:
            -
              value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-obj-archives"
                - "memory.md#mem-obj-docs-content"
                - "runtime.md#rt-rte-ingest-documents"
              note: "External archive/feed material enters local retention through download and loader normalization."
          records:
            - "memory.md#mem-obj-archives"
            - "memory.md#mem-obj-docs-content"
            - "runtime.md#rt-rte-ingest-documents"
          note: "Imported lineage does not resolve original authorship or source warrant."
        -
          scope: "Constructed roots, segmented chunks, generated metadata and subsequent embeddings"
          assessment: "known"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-docs-content"
                - "memory.md#mem-obj-chunks-content"
                - "memory.md#mem-obj-docs-metadata"
                - "runtime.md#rt-rte-embed-chunks"
                - "epistemic.md#epi-rte-source-reshaping"
              note: "Fixed concatenation/conversion, segmentation, generated fields and embedding computation derive retained parts from inputs."
          records:
            - "memory.md#mem-obj-docs-content"
            - "memory.md#mem-obj-chunks-content"
            - "memory.md#mem-obj-docs-metadata"
            - "runtime.md#rt-rte-embed-chunks"
            - "epistemic.md#epi-rte-source-reshaping"
          note: "This unit covers inspected subsequent derivation, not arbitrary preexisting vectors."
        -
          scope: "Canvas coordinates and copied text/IDs"
          assessment: "known"
          findings:
            -
              value: "other-compiled"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-geojson"
                - "memory.md#mem-rte-canvas-display"
              note: "PCA and field copying afford the derived display artifact."
          records:
            - "memory.md#mem-obj-geojson"
            - "memory.md#mem-rte-canvas-display"
          note: "Connection to current CLI state is qualified by database, representation and filename mismatches."
        -
          scope: "Initial content of arbitrary preexisting vector rows"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-chunks-embedding"
          note: "The report explicitly leaves initial vector provenance uninspected; a known re-embedding path cannot settle that provenance."
        -
          scope: "Potential Atlas-retained payloads and requested topic outputs"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-atlas-export"
            - "epistemic.md#epi-rte-atlas-topics"
          note: "The inspected request does not establish remote persistence, lineage or later consumers; exporter initialization/schema defects also qualify reachability."
      records:
        - "memory.md#mem-obj-archives"
        - "memory.md#mem-obj-docs-content"
        - "runtime.md#rt-rte-ingest-documents"
        - "memory.md#mem-obj-chunks-content"
        - "memory.md#mem-obj-docs-metadata"
        - "runtime.md#rt-rte-embed-chunks"
        - "epistemic.md#epi-rte-source-reshaping"
        - "memory.md#mem-obj-geojson"
        - "memory.md#mem-rte-canvas-display"
        - "memory.md#mem-obj-chunks-embedding"
        - "memory.md#mem-rte-atlas-export"
        - "epistemic.md#epi-rte-atlas-topics"
      note: "Imported source material and compiled derivatives coexist. Upstream authorship, preexisting vectors and external topics do not become authored or trace-extracted by inference."
    behavioral_authority:
      assessment: "partial"
      units:
        -
          scope: "Retained root content/provenance at terminal display and chunk content at embedding input"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-docs-content"
                - "memory.md#mem-obj-chunks-content"
                - "memory.md#mem-obj-docs-metadata"
                - "runtime.md#rt-rte-query-documents"
                - "runtime.md#rt-rte-embed-chunks"
              note: "Roots and labels supply informational reference; retained chunks supply source context for numerical derivation."
          records:
            - "memory.md#mem-obj-docs-content"
            - "memory.md#mem-obj-chunks-content"
            - "memory.md#mem-obj-docs-metadata"
            - "runtime.md#rt-rte-query-documents"
            - "runtime.md#rt-rte-embed-chunks"
          note: "These consumers do not grant instruction priority or factual warrant."
        -
          scope: "Stored chunk vectors at query SQL"
          assessment: "known"
          findings:
            -
              value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chunks-embedding"
                - "runtime.md#rt-bap-vector-ranking"
                - "runtime.md#rt-rte-query-documents"
              note: "Retained dense values determine relative candidate scores and root order."
          records:
            - "memory.md#mem-obj-chunks-embedding"
            - "runtime.md#rt-bap-vector-ranking"
            - "runtime.md#rt-rte-query-documents"
          note: "No retained ranking policy or trained scorer is required for ranking-input authority."
        -
          scope: "Chunk parent IDs at query root-reload consumer"
          assessment: "known"
          findings:
            -
              value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chunks-content"
                - "runtime.md#rt-rte-query-documents"
              note: "Retained parent linkage selects the root rows reloaded for terminal delivery."
          records:
            - "memory.md#mem-obj-chunks-content"
            - "runtime.md#rt-rte-query-documents"
          note: "This wired lookup effect is separate from canvas author filtering and numerical candidate ranking."
        -
          scope: "Root author fields at canvas projection-input filter"
          assessment: "known"
          findings:
            -
              value: "routing"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-docs-metadata"
                - "memory.md#mem-rte-canvas-display"
              note: "Author equality affords selection of the retained rows forming the projection input scope."
          records:
            - "memory.md#mem-obj-docs-metadata"
            - "memory.md#mem-rte-canvas-display"
          note: "The canvas route's database, representation and filename mismatches retain an afforded warrant; the wired query reload does not upgrade it."
        -
          scope: "Canvas retained text and link fields at browser display"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-geojson"
                - "memory.md#mem-rte-canvas-display"
              note: "Map labels and outbound source links afford informational display."
          records:
            - "memory.md#mem-obj-geojson"
            - "memory.md#mem-rte-canvas-display"
          note: "Requested and generated filenames differ; no connected display run is established."
        -
          scope: "Potential Atlas-retained payloads and requested topic outputs"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-atlas-export"
            - "epistemic.md#epi-rte-atlas-topics"
          note: "The inspected request does not establish remote persistence, behavioral authority or later consumers; exporter initialization/schema defects also qualify reachability."
      records:
        - "memory.md#mem-obj-docs-content"
        - "memory.md#mem-obj-chunks-content"
        - "memory.md#mem-obj-docs-metadata"
        - "runtime.md#rt-rte-query-documents"
        - "runtime.md#rt-rte-embed-chunks"
        - "memory.md#mem-obj-chunks-embedding"
        - "runtime.md#rt-bap-vector-ranking"
        - "memory.md#mem-rte-canvas-display"
        - "memory.md#mem-obj-geojson"
        - "memory.md#mem-rte-atlas-export"
        - "epistemic.md#epi-rte-atlas-topics"
      note: "Actual text, ranking and routing effects are separated by consumer. Geometric display placement alone is not a controlled authority value; no instruction, validation or learning force is inferred from mere retention."
    write_agency:
      assessment: "partial"
      units:
        -
          scope: "Archive download, root/chunk admission and subsequent embedding updates"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-archives"
                - "runtime.md#rt-rte-ingest-documents"
                - "runtime.md#rt-rte-embed-chunks"
              note: "Code selects and admits content after invocation without a per-content human decision."
          records:
            - "memory.md#mem-obj-archives"
            - "runtime.md#rt-rte-ingest-documents"
            - "runtime.md#rt-rte-embed-chunks"
          note: "Human source selection or starting a command does not make its subsequent admissions manual."
        -
          scope: "Dataset-wide replacement of retained vectors by null"
          assessment: "known"
          findings:
            -
              value: "manual"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-clear-embeddings"
              note: "The operator explicitly authorizes removal of the selected dataset's vector content."
          records:
            - "runtime.md#rt-rte-clear-embeddings"
          note: "This is a separately evidenced maintenance decision, not the null-row read selector."
        -
          scope: "Canvas GeoJSON replacement"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-canvas-display"
              note: "Fixed projection code admits coordinates and replaces its output without point-by-point operator approval."
          records:
            - "memory.md#mem-rte-canvas-display"
          note: "Operator initiation remains distinct from software admission; route connection is only afforded."
        -
          scope: "Initial admission of arbitrary preexisting vectors and external database-edit alternatives"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-chunks-embedding"
            - "runtime.md#rt-bap-operator-config"
          note: "Initial vector control is uninspected; generic external administration power does not establish a per-content operator decision."
        -
          scope: "Potential Atlas-retained payloads and requested topic outputs"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-atlas-export"
            - "epistemic.md#epi-rte-atlas-topics"
          note: "The inspected request does not establish remote persistence, write/admission control or later consumers; exporter initialization/schema defects also qualify reachability."
      records:
        - "memory.md#mem-obj-archives"
        - "runtime.md#rt-rte-ingest-documents"
        - "runtime.md#rt-rte-embed-chunks"
        - "runtime.md#rt-rte-clear-embeddings"
        - "memory.md#mem-rte-canvas-display"
        - "memory.md#mem-obj-chunks-embedding"
        - "runtime.md#rt-bap-operator-config"
        - "memory.md#mem-rte-atlas-export"
        - "epistemic.md#epi-rte-atlas-topics"
      note: "Known software admission and explicit manual clearing coexist. Initial vectors and external GUI/provider alternatives remain unresolved rather than inheriting one route's control."
    curation_operations:
      assessment: "partial"
      units:
        -
          scope: "Explicit forgetting of retained chunk vectors"
          assessment: "known"
          findings:
            -
              value: "decay"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-clear-embeddings"
                - "memory.md#mem-obj-chunks-embedding"
              note: "Clearing removes derived vectors and their retrieval eligibility; no former vector version is retained."
          records:
            - "runtime.md#rt-rte-clear-embeddings"
            - "memory.md#mem-obj-chunks-embedding"
          note: "This is forgetting, not invalidation with retained vector history. Source text surviving is not a history of the removed vector."
        -
          scope: "Replacement of a prior canvas projection file"
          assessment: "known"
          findings:
            -
              value: "evolve"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-canvas-display"
                - "memory.md#mem-obj-geojson"
              note: "The projection producer overwrites the same output artifact with recomputed coordinates and copied fields."
          records:
            - "memory.md#mem-rte-canvas-display"
            - "memory.md#mem-obj-geojson"
          note: "A supported replacement mechanism does not establish that a prior artifact existed or a run succeeded."
        -
          scope: "Text segmentation, primary ingestion, embedding generation and external administration"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-chunks-content"
            - "runtime.md#rt-rte-ingest-documents"
            - "runtime.md#rt-rte-embed-chunks"
            - "epistemic.md#epi-rte-source-reshaping"
          note: "Segmentation/acquisition/index generation alone do not establish a controlled curation operation over retained claims. RSS fallback metadata is produced during primary admission, not an established curator of retained entries."
        -
          scope: "Potential Atlas-retained payloads and requested topic outputs"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-atlas-export"
            - "epistemic.md#epi-rte-atlas-topics"
          note: "The inspected request does not establish remote persistence, curation transformations or later consumers; exporter initialization/schema defects also qualify reachability."
      records:
        - "runtime.md#rt-rte-clear-embeddings"
        - "memory.md#mem-obj-chunks-embedding"
        - "memory.md#mem-rte-canvas-display"
        - "memory.md#mem-obj-geojson"
        - "memory.md#mem-obj-chunks-content"
        - "runtime.md#rt-rte-ingest-documents"
        - "runtime.md#rt-rte-embed-chunks"
        - "epistemic.md#epi-rte-source-reshaping"
        - "memory.md#mem-rte-atlas-export"
        - "epistemic.md#epi-rte-atlas-topics"
      note: "Forgetting and afforded projection replacement are supported. No consolidation or synthesis is inferred from numerical encoding, primary acquisition, or the opaque topic request."
    read_back_direction:
      assessment: "partial"
      units:
        -
          scope: "Archive loading and embedding batches requested by operator-invoked commands"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-obj-archives"
                - "runtime.md#rt-rte-ingest-documents"
                - "runtime.md#rt-rte-embed-chunks"
              note: "The invoked loaders and embedding driver request the retained inputs they process."
          records:
            - "memory.md#mem-obj-archives"
            - "runtime.md#rt-rte-ingest-documents"
            - "runtime.md#rt-rte-embed-chunks"
          note: "Internal batching fulfils requested work; it is not unsolicited context injection."
        -
          scope: "Query selection, root reload and terminal delivery"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-query-documents"
                - "memory.md#mem-obj-docs-content"
              note: "A supplied query requests stored material; ranking and ID reload fulfil that request."
          records:
            - "runtime.md#rt-rte-query-documents"
            - "memory.md#mem-obj-docs-content"
          note: "Automatic scoring within the request is not a second push route."
        -
          scope: "Canvas projection input, browser whole-file fetch and Atlas export input"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-canvas-display"
                - "memory.md#mem-rte-atlas-export"
              note: "Operator projection/export and map-load requests read the selected corpus/file."
          records:
            - "memory.md#mem-rte-canvas-display"
            - "memory.md#mem-rte-atlas-export"
          note: "Username/author parameters select requested inputs; current integration remains qualified."
        -
          scope: "Potential Atlas-retained payloads and requested topic outputs"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-atlas-export"
            - "epistemic.md#epi-rte-atlas-topics"
          note: "The inspected request does not establish remote persistence, later read-back direction or later consumers; exporter initialization/schema defects also qualify reachability."
      records:
        - "memory.md#mem-obj-archives"
        - "runtime.md#rt-rte-ingest-documents"
        - "runtime.md#rt-rte-embed-chunks"
        - "runtime.md#rt-rte-query-documents"
        - "memory.md#mem-obj-docs-content"
        - "memory.md#mem-rte-canvas-display"
        - "memory.md#mem-rte-atlas-export"
        - "epistemic.md#epi-rte-atlas-topics"
      note: "All established local routes fulfil requests. Opaque Atlas consumers prevent a complete pull-only boundary or a system-wide absence of push."
    read_back_signal:
      assessment: "not-determinable"
      units:
        -
          scope: "Established request-driven archive, embedding, query, canvas and export input reads"
          assessment: "inapplicable"
          findings: []
          records:
            - "memory.md#mem-obj-archives"
            - "runtime.md#rt-rte-ingest-documents"
            - "runtime.md#rt-rte-embed-chunks"
            - "runtime.md#rt-rte-query-documents"
            - "memory.md#mem-rte-canvas-display"
            - "memory.md#mem-rte-atlas-export"
          note: "These are pull operations; push-selection signal is inapplicable within this local unit. Query cosine and map filenames do not establish a push signal."
        -
          scope: "Potential Atlas-retained payloads and requested topic outputs"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-atlas-export"
            - "epistemic.md#epi-rte-atlas-topics"
          note: "The inspected request does not establish remote persistence, push trigger, selector input and selected retained part or later consumers; exporter initialization/schema defects also qualify reachability."
      records:
        - "memory.md#mem-obj-archives"
        - "runtime.md#rt-rte-ingest-documents"
        - "runtime.md#rt-rte-embed-chunks"
        - "runtime.md#rt-rte-query-documents"
        - "memory.md#mem-rte-canvas-display"
        - "memory.md#mem-rte-atlas-export"
        - "epistemic.md#epi-rte-atlas-topics"
      note: "No positive push selector can be classified. The unresolved external consumer prevents making this axis inapplicable for the entire boundary."
    trace_learning:
      assessment: "not-determinable"
      units:
        -
          scope: "Inspected imported-document transformations, query, clearing and canvas/export drivers"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-archives"
            - "runtime.md#rt-rte-ingest-documents"
            - "runtime.md#rt-rte-embed-chunks"
            - "runtime.md#rt-rte-query-documents"
            - "runtime.md#rt-rte-clear-embeddings"
            - "memory.md#mem-rte-canvas-display"
            - "memory.md#mem-rte-atlas-export"
          note: "The records describe imported document derivation and no retained query/feedback updates, but declare no bounded trace-learning absence record. They establish neither a qualifying trace-fed write nor a profile-wide negative; actual external input contents and initialization are unresolved."
        -
          scope: "Potential Atlas-retained payloads and requested topic outputs"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-atlas-export"
            - "epistemic.md#epi-rte-atlas-topics"
          note: "The inspected request does not establish remote persistence, automatic trace-fed updates and later consumers or later consumers; exporter initialization/schema defects also qualify reachability."
      records:
        - "memory.md#mem-obj-archives"
        - "runtime.md#rt-rte-ingest-documents"
        - "runtime.md#rt-rte-embed-chunks"
        - "runtime.md#rt-rte-query-documents"
        - "runtime.md#rt-rte-clear-embeddings"
        - "memory.md#mem-rte-canvas-display"
        - "memory.md#mem-rte-atlas-export"
        - "epistemic.md#epi-rte-atlas-topics"
      note: "No controlled yes/no finding is established by canonical bounded trace-learning records. Numerical durability alone does not establish trace origin; opaque provider processing is not a negative."
    trace_source:
      assessment: "not-determinable"
      units:
        -
          scope: "Input provenance for any qualifying local trace-fed write"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-archives"
            - "memory.md#mem-obj-docs-content"
            - "memory.md#mem-obj-chunks-embedding"
            - "runtime.md#rt-rte-ingest-documents"
            - "runtime.md#rt-rte-embed-chunks"
          note: "No qualifying automatic trace-learning route is established. Imported tweets/feeds are not classified as session logs or event streams solely from container names, and initial vector provenance is unresolved."
        -
          scope: "Potential Atlas-retained payloads and requested topic outputs"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-atlas-export"
            - "epistemic.md#epi-rte-atlas-topics"
          note: "The inspected request does not establish remote persistence, original inputs to a qualifying trace-fed write or later consumers; exporter initialization/schema defects also qualify reachability."
      records:
        - "memory.md#mem-obj-archives"
        - "memory.md#mem-obj-docs-content"
        - "memory.md#mem-obj-chunks-embedding"
        - "runtime.md#rt-rte-ingest-documents"
        - "runtime.md#rt-rte-embed-chunks"
        - "memory.md#mem-rte-atlas-export"
        - "epistemic.md#epi-rte-atlas-topics"
      note: "Unresolved trace-learning coverage prevents inapplicability and prevents assigning trace sources from the imported corpus format."
---

# Semantic Engine memory profile

## Comparison rationale

Canvas label text, geometry/IDs and author-filter routing retain separate afforded findings from the wired archive/SQLite text, symbolic fields and query parent-ID reload. Their controlled values remain supported, but each finding carries its own local route warrant. The qualified canvas producer/consumer in [MEM-RTE-canvas-display](memory.md#mem-rte-canvas-display) cannot inherit the stronger basis of [RT-RTE-query-documents](runtime.md#rt-rte-query-documents).

The inventory separates local retained parts from potential Atlas state. SQLite is the substrate even where its payload is a dense vector. Dense vectors receive the parametric form classification without attributing updates to model weights. Actual binary conversion remains unresolved in [MEM-OBJ-chunks-embedding](memory.md#mem-obj-chunks-embedding); that limits interoperability, not the identification of the ranking consumer.

Reconciliation supersedes the four epistemic document/chunk object declarations with their memory counterparts. This profile cites those canonical memory records. The valid runtime container and the separate canvas/Atlas route parts remain; no supersession upgrades an afforded connected display route to wired operation. The topic request remains an opaque alternative under [EPI-RTE-atlas-topics](epistemic.md#epi-rte-atlas-topics), not evidence of synthesized retained claims.

Explicit vector clearing is manual authorization of removal, while ingestion and embedding admit their results automatically. Clearing forgets the vectors without retaining their history, so decay is narrower and better supported than invalidate. The surviving document text is a different operative part, not the removed vector's history. See [RT-RTE-clear-embeddings](runtime.md#rt-rte-clear-embeddings). Replacing a derived map artifact supports afforded evolution; numerical projection alone supports neither consolidation of claims nor synthesis.

Ranking and root reload occur inside a requested query. They are not push simply because code selects and delivers the response. Likewise, a username-named map file is requested whole, not matched to an automatic context-injection trigger. The known local pull units therefore have no applicable push signal, but opaque remote consumers prevent a whole-boundary inapplicability finding. See [RT-RTE-query-documents](runtime.md#rt-rte-query-documents) and [MEM-RTE-canvas-display](memory.md#mem-rte-canvas-display).

Trace learning and trace source remain not determinable rather than importing a system-wide negative from the prose. The accepted set contains no canonical bounded trace-learning absence declaration, and external topic/initialization alternatives are unresolved. The factual-acceptance absence is about a different property and supplies no such warrant. A future positive would need original trace inputs, automatic durable admission and a later behavior-shaping consumer in accepted records. Missing executions independently prevent observed or causal findings; they do not weaken the inspected local wiring into mere claims.

Source-read log: none. Classification used only the supplied accepted members and reconciliation; no target-source read or additional evidence was required.
