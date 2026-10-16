---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "AI Agents in Depth memory profile: user facts, live context history, sequential checkpoints and retry-policy feedback, with other suite variants unresolved."
run-id: "AAS-2026-10-12-ai-agent-book-d56e8121d636-01"
source-identity: "https://github.com/bojieli/ai-agent-book"
reviewed-boundary: "dbc046eb896ac4e39aa19c7774c8bf49583b89a6"
memory-comparison:
  version: 2
  scope: "Included: accumulated user-memory notes/basic and advanced cards, raw persisted dialogue and optional opaque Dify history, live context-agent history and its material parts, sequential derived states/checkpoint controls and reused receipts, generated retry-policy candidates and rejected-check feedback; all other included suite memory alternatives remain unresolved. Excluded: static shipped prompts/rules/stable source as accumulated memory, inference weights without recorded through-use updates, unconsumed terminal reports and judge evidence as later-agent memory, and external reproduction/host deployment loops outside the frozen source."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        - scope: "User-memory note content and addressing metadata"
          assessment: "known"
          findings:
            - value: "in-memory"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-note"
              note: "The operative local object is a Python list or dictionary."
            - value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-note"
              note: "The object is persisted as per-user or per-case JSON and has a recorded reload/consumer route."
          records:
            - "memory.md#mem-obj-memory-note"
          note: "Local retained objects and file stores are inspected; optional remote history is split below."
        - scope: "Basic hierarchical memory cards"
          assessment: "known"
          findings:
            - value: "in-memory"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-cards"
              note: "The operative local object is a Python list or dictionary."
            - value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-cards"
              note: "The object is persisted as per-user or per-case JSON and has a recorded reload/consumer route."
          records:
            - "memory.md#mem-obj-memory-cards"
          note: "Local retained objects and file stores are inspected; optional remote history is split below."
        - scope: "Advanced category cards"
          assessment: "known"
          findings:
            - value: "in-memory"
              basis: "wired"
              records:
                - "memory.md#mem-obj-categories"
              note: "The operative local object is a Python list or dictionary."
            - value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-categories"
              note: "The object is persisted as per-user or per-case JSON and has a recorded reload/consumer route."
          records:
            - "memory.md#mem-obj-categories"
          note: "Local retained objects and file stores are inspected; optional remote history is split below."
        - scope: "Raw user-memory conversation turns"
          assessment: "known"
          findings:
            - value: "in-memory"
              basis: "wired"
              records:
                - "memory.md#mem-obj-conversation-turn"
              note: "The operative local object is a Python list or dictionary."
            - value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-conversation-turn"
              note: "The object is persisted as per-user or per-case JSON and has a recorded reload/consumer route."
          records:
            - "memory.md#mem-obj-conversation-turn"
          note: "Local retained objects and file stores are inspected; optional remote history is split below."
        - scope: "Sequential derived states and checkpoint controls/receipts"
          assessment: "known"
          findings:
            - value: "in-memory"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-states"
              note: "The operative local object is a Python list or dictionary."
            - value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-states"
              note: "The object is persisted as per-user or per-case JSON and has a recorded reload/consumer route."
          records:
            - "memory.md#mem-obj-memory-states"
          note: "Local retained objects and file stores are inspected; optional remote history is split below."
        - scope: "Live context-agent history and its PDF/currency/reply parts"
          assessment: "known"
          findings:
            - value: "in-memory"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-conversation-history"
                - "runtime.md#rt-rte-context-task"
              note: "The live list survives later tasks on the same agent and is selected for later calls."
          records:
            - "runtime.md#rt-obj-conversation-history"
            - "runtime.md#rt-rte-context-task"
          note: "Optional single-task report files are excluded here: no inspected reload consumer is recorded."
        - scope: "Retry-policy generated source and rejected-check feedback in the campaign"
          assessment: "known"
          findings:
            - value: "in-memory"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-policy-candidate"
              note: "Proposals and rejected history are retained between generation/evaluation invocations."
            - value: "files"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-policy-candidate"
                - "runtime.md#rt-obj-retry-policy"
              note: "Drivers retain candidate source, manifests and receipts; candidate content has an evaluator consumer."
          records:
            - "runtime.md#rt-rte-policy-candidate"
            - "runtime.md#rt-obj-retry-policy"
          note: "Stable shipped source is an input, not accumulated memory; live installation is not established."
        - scope: "Optional Dify retained dialogue index and consumed search payload"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-conversation-turn"
            - "memory.md#mem-rte-history-search"
          note: "Index requests carry text and metadata, but provider storage/embedding semantics and a shipped later model-search consumer are opaque. A vector store cannot be inferred from semantic-search parameters."
        - scope: "Other included suite memory routes: mem0, memobase, agentic-rag-for-user-memory, contextual-retrieval-for-user-memory; retrieval-pipeline, dense-embedding, sparse-embedding, structured-index, structured-knowledge-extraction, log-sanitization, agentic-rag, contextual-retrieval; other chapter loops, skills, fixtures and results."
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-trace-maintenance"
            - "memory.md#mem-rte-sequential-campaign"
          note: "These alternatives remain uninspected in the accepted memory inventory. Their storage and remote operative-state coverage cannot be enumerated or classified from directory names; no negative or complete-value conclusion follows."
      records:
        - "memory.md#mem-obj-memory-note"
        - "memory.md#mem-obj-memory-cards"
        - "memory.md#mem-obj-categories"
        - "memory.md#mem-obj-conversation-turn"
        - "memory.md#mem-obj-memory-states"
        - "runtime.md#rt-obj-conversation-history"
        - "runtime.md#rt-rte-context-task"
        - "runtime.md#rt-rte-policy-candidate"
        - "runtime.md#rt-obj-retry-policy"
        - "memory.md#mem-rte-history-search"
        - "memory.md#mem-rte-trace-maintenance"
        - "memory.md#mem-rte-sequential-campaign"
      note: "Positive classifications cover the named inspected routes only. Included alternatives remain unresolved; this is not a suite-complete inventory of values. Storage and remote operative-state coverage uncertainty is retained in the corresponding units."
    representational_form:
      assessment: "partial"
      units:
        - scope: "Note content versus UUID/tags/session/timestamps"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-note"
              note: "Content supplies model-interpreted information; JSON syntax does not turn factual values into executable policy."
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-note"
              note: "Addressing and control fields have localized rules at their local storage/resume consumers."
          records:
            - "memory.md#mem-obj-memory-note"
          note: "The two findings classify distinct operative parts/consumption paths, not one homogeneous representation."
        - scope: "Basic-card interpreted values versus path/source/time addressing"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-cards"
              note: "Content supplies model-interpreted information; JSON syntax does not turn factual values into executable policy."
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-cards"
              note: "Addressing and control fields have localized rules at their local storage/resume consumers."
          records:
            - "memory.md#mem-obj-memory-cards"
          note: "The two findings classify distinct operative parts/consumption paths, not one homogeneous representation."
        - scope: "Advanced interpreted facts/backstory versus category/key metadata"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-categories"
              note: "Content supplies model-interpreted information; JSON syntax does not turn factual values into executable policy."
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-categories"
              note: "Addressing and control fields have localized rules at their local storage/resume consumers."
          records:
            - "memory.md#mem-obj-categories"
          note: "The two findings classify distinct operative parts/consumption paths, not one homogeneous representation."
        - scope: "Raw dialogue text versus session/turn/time metadata"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-conversation-turn"
              note: "Content supplies model-interpreted information; JSON syntax does not turn factual values into executable policy."
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-conversation-turn"
              note: "Addressing and control fields have localized rules at their local storage/resume consumers."
          records:
            - "memory.md#mem-obj-conversation-turn"
          note: "The two findings classify distinct operative parts/consumption paths, not one homogeneous representation."
        - scope: "Sequential interpreted memory versus checkpoint status/signature/session/purpose controls"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-states"
              note: "Content supplies model-interpreted information; JSON syntax does not turn factual values into executable policy."
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-states"
              note: "Addressing and control fields have localized rules at their local storage/resume consumers."
          records:
            - "memory.md#mem-obj-memory-states"
          note: "The two findings classify distinct operative parts/consumption paths, not one homogeneous representation."
        - scope: "Context history prose and symbolic tool/role envelopes, including currency result"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-conversation-history"
                - "epistemic.md#epi-obj-pdf-result"
                - "epistemic.md#epi-obj-final-answer"
              note: "Task, PDF and assistant content are interpreted by a later model."
            - value: "symbolic"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-conversation-history"
                - "epistemic.md#epi-obj-currency-result"
              note: "Role/tool associations and numeric conversion dictionaries have fixed structural rules."
          records:
            - "runtime.md#rt-obj-conversation-history"
            - "epistemic.md#epi-obj-pdf-result"
            - "epistemic.md#epi-obj-currency-result"
            - "epistemic.md#epi-obj-final-answer"
          note: "The valid container remains alongside its epistemic parts."
        - scope: "Generated retry module and rejected feedback at different consumers"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-retry-policy"
                - "runtime.md#rt-bap-candidate-policy"
              note: "Candidate Python is compiled and its exported functions are called by the evaluator."
            - value: "natural-language"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-retry-policy"
                - "runtime.md#rt-rte-policy-candidate"
              note: "Comments, diagnosis and rejected reasons reach the coding model through interpretation."
          records:
            - "runtime.md#rt-obj-retry-policy"
            - "runtime.md#rt-rte-policy-candidate"
            - "runtime.md#rt-bap-candidate-policy"
          note: "Candidate evaluation is a later consumer, not stable production adoption."
        - scope: "Opaque optional Dify payload beyond transmitted text"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-history-search"
          note: "The inspected request/display does not expose provider embeddings or the operative returned payload lineage. No parametric-memory classification follows."
        - scope: "Other included suite memory routes: mem0, memobase, agentic-rag-for-user-memory, contextual-retrieval-for-user-memory; retrieval-pipeline, dense-embedding, sparse-embedding, structured-index, structured-knowledge-extraction, log-sanitization, agentic-rag, contextual-retrieval; other chapter loops, skills, fixtures and results."
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-trace-maintenance"
            - "memory.md#mem-rte-sequential-campaign"
          note: "These alternatives remain uninspected in the accepted memory inventory. Their operative payload forms and consumption paths cannot be enumerated or classified from directory names; no negative or complete-value conclusion follows."
      records:
        - "memory.md#mem-obj-memory-note"
        - "memory.md#mem-obj-memory-cards"
        - "memory.md#mem-obj-categories"
        - "memory.md#mem-obj-conversation-turn"
        - "memory.md#mem-obj-memory-states"
        - "runtime.md#rt-obj-conversation-history"
        - "epistemic.md#epi-obj-pdf-result"
        - "epistemic.md#epi-obj-currency-result"
        - "epistemic.md#epi-obj-final-answer"
        - "runtime.md#rt-obj-retry-policy"
        - "runtime.md#rt-rte-policy-candidate"
        - "runtime.md#rt-bap-candidate-policy"
        - "memory.md#mem-rte-history-search"
        - "memory.md#mem-rte-trace-maintenance"
        - "memory.md#mem-rte-sequential-campaign"
      note: "Positive classifications cover the named inspected routes only. Included alternatives remain unresolved; this is not a suite-complete inventory of values. Operative payload forms and consumption paths uncertainty is retained in the corresponding units."
    lineage:
      assessment: "partial"
      units:
        - scope: "Model-selected user facts and sequential replacement memories"
          assessment: "known"
          findings:
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-rte-trace-maintenance"
                - "memory.md#mem-rte-sequential-campaign"
              note: "Recorded dialogue sessions feed automatic retained fact/state production for later answer/update requests."
          records:
            - "memory.md#mem-rte-trace-maintenance"
            - "memory.md#mem-rte-sequential-campaign"
          note: "Extraction lineage is wired; fidelity and observed operation are not established."
        - scope: "Explicitly supplied CLI note content"
          assessment: "known"
          findings:
            - value: "authored"
              basis: "wired"
              records:
                - "memory.md#mem-rte-offline-maintenance"
              note: "The add/update commands admit explicitly supplied note text."
          records:
            - "memory.md#mem-rte-offline-maintenance"
          note: "This is a content derivation path, independent of whether a particular library caller is human."
        - scope: "Local raw conversational turns and fixture dialogue"
          assessment: "known"
          findings:
            - value: "authored"
              basis: "wired"
              records:
                - "memory.md#mem-obj-conversation-turn"
                - "memory.md#mem-rte-trace-maintenance"
              note: "The interactive route records user content and model-authored replies without extraction."
            - value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-obj-conversation-turn"
                - "memory.md#mem-rte-sequential-campaign"
              note: "Evaluation supplies external fixture histories to the local update route."
          records:
            - "memory.md#mem-obj-conversation-turn"
            - "memory.md#mem-rte-trace-maintenance"
            - "memory.md#mem-rte-sequential-campaign"
          note: "These local paths do not resolve original fixture authorship."
        - scope: "Context-history imported PDF, generated reply and computed conversion parts"
          assessment: "known"
          findings:
            - value: "imported"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-pdf-import"
              note: "PDF assertions enter the retained tool history from a file or URL."
            - value: "authored"
              basis: "wired"
              records:
                - "epistemic.md#epi-obj-final-answer"
                - "runtime.md#rt-rte-context-task"
              note: "Model reply content enters the history."
            - value: "other-compiled"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-currency-conversion"
              note: "Numeric observations are computed under the shipped conversion constants."
          records:
            - "runtime.md#rt-obj-conversation-history"
            - "epistemic.md#epi-rte-pdf-import"
            - "epistemic.md#epi-rte-currency-conversion"
            - "epistemic.md#epi-obj-final-answer"
          note: "The arithmetic derivation is not evidence of current financial source truth."
        - scope: "Metadata and deterministic consolidation products"
          assessment: "known"
          findings:
            - value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-note"
                - "memory.md#mem-obj-memory-cards"
                - "memory.md#mem-obj-categories"
              note: "Local code generates addressing/time/source metadata."
            - value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-rte-offline-maintenance"
              note: "Normalized equality, tags and timestamps determine consolidation winners and merged tags."
          records:
            - "memory.md#mem-obj-memory-note"
            - "memory.md#mem-obj-memory-cards"
            - "memory.md#mem-obj-categories"
            - "memory.md#mem-rte-offline-maintenance"
          note: "Distinct compiled paths share this unit only for lineage, not semantic warrant."
        - scope: "Retry proposal and rejected feedback derivation"
          assessment: "known"
          findings:
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-policy-candidate"
              note: "Diagnosis and failed-check summaries are derived from supplied failure experience and feed retained policy proposals."
            - value: "authored"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-policy-candidate"
                - "runtime.md#rt-obj-retry-policy"
              note: "Software or coding-model generation authors the retained replacement module."
          records:
            - "runtime.md#rt-rte-policy-candidate"
            - "runtime.md#rt-obj-retry-policy"
          note: "Deterministic and model-authored alternatives remain separate proposal paths; neither installs stable policy."
        - scope: "Preexisting user files, caller-supplied cards/updates and original fixtures"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-memory-note"
            - "memory.md#mem-obj-memory-cards"
            - "memory.md#mem-obj-categories"
            - "memory.md#mem-obj-conversation-turn"
            - "memory.md#mem-rte-sequential-campaign"
          note: "Accepted records leave initial file provenance and generic direct-input origins unresolved. Known later transformations cannot establish these initial lineages."
        - scope: "Optional Dify embeddings and external payload origins"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-history-search"
          note: "No provider snapshot establishes embedding derivation or external retained payload provenance."
        - scope: "Other included suite memory routes: mem0, memobase, agentic-rag-for-user-memory, contextual-retrieval-for-user-memory; retrieval-pipeline, dense-embedding, sparse-embedding, structured-index, structured-knowledge-extraction, log-sanitization, agentic-rag, contextual-retrieval; other chapter loops, skills, fixtures and results."
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-trace-maintenance"
            - "memory.md#mem-rte-sequential-campaign"
          note: "These alternatives remain uninspected in the accepted memory inventory. Their initial and alternative derivation paths cannot be enumerated or classified from directory names; no negative or complete-value conclusion follows."
      records:
        - "memory.md#mem-rte-trace-maintenance"
        - "memory.md#mem-rte-sequential-campaign"
        - "memory.md#mem-rte-offline-maintenance"
        - "memory.md#mem-obj-conversation-turn"
        - "runtime.md#rt-obj-conversation-history"
        - "epistemic.md#epi-rte-pdf-import"
        - "epistemic.md#epi-rte-currency-conversion"
        - "epistemic.md#epi-obj-final-answer"
        - "memory.md#mem-obj-memory-note"
        - "memory.md#mem-obj-memory-cards"
        - "memory.md#mem-obj-categories"
        - "runtime.md#rt-rte-policy-candidate"
        - "runtime.md#rt-obj-retry-policy"
        - "memory.md#mem-rte-history-search"
      note: "Positive classifications cover the named inspected routes only. Included alternatives remain unresolved; this is not a suite-complete inventory of values. Initial and alternative derivation paths uncertainty is retained in the corresponding units."
    behavioral_authority:
      assessment: "partial"
      units:
        - scope: "Retained notes/cards and live dialogue at answer/analysis models"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-bap-memory-context"
                - "runtime.md#rt-obj-conversation-history"
                - "runtime.md#rt-rte-context-task"
              note: "Rendered facts and prior exchanges supply interpretive context, not verified truth or enforced standing guidance."
          records:
            - "memory.md#mem-bap-memory-context"
            - "runtime.md#rt-obj-conversation-history"
            - "runtime.md#rt-rte-context-task"
          note: "Preference content in user-message context does not itself establish instruction authority."
        - scope: "Retained dialogue/current state at memory-update consumers"
          assessment: "known"
          findings:
            - value: "learning"
              basis: "wired"
              records:
                - "memory.md#mem-rte-trace-maintenance"
                - "memory.md#mem-rte-sequential-campaign"
              note: "Recorded experience and prior state feed automatic durable memory changes."
            - value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-rte-trace-maintenance"
                - "memory.md#mem-rte-sequential-campaign"
              note: "Prior facts also supply model-interpreted information during each update."
          records:
            - "memory.md#mem-rte-trace-maintenance"
            - "memory.md#mem-rte-sequential-campaign"
            - "memory.md#mem-bap-campaign-state"
          note: "Update-consumer learning authority and downstream answer knowledge are distinct paths; neither proves benefit."
        - scope: "Checkpoint controls and stored call results at resume host"
          assessment: "known"
          findings:
            - value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-rte-sequential-campaign"
                - "memory.md#mem-bap-campaign-state"
              note: "Status, session index, latest-state position and purpose select work or reused responses."
            - value: "validation"
              basis: "wired"
              records:
                - "memory.md#mem-rte-sequential-campaign"
              note: "Stored signature is a conformance criterion for resume."
            - value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-rte-sequential-campaign"
              note: "A signature mismatch rejects resume."
          records:
            - "memory.md#mem-obj-memory-states"
            - "memory.md#mem-rte-sequential-campaign"
            - "memory.md#mem-bap-campaign-state"
          note: "These forces belong to control metadata, not arbitrary memory fact values; fixture/prompt freshness remains unchecked."
        - scope: "Retained note content/tags/time and card identifiers at maintenance selectors"
          assessment: "known"
          findings:
            - value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-rte-offline-maintenance"
                - "memory.md#mem-rte-trace-maintenance"
              note: "IDs/paths identify mutation targets; content/tags and timestamps select query/consolidation results."
          records:
            - "memory.md#mem-rte-offline-maintenance"
            - "memory.md#mem-rte-trace-maintenance"
            - "memory.md#mem-obj-memory-note"
            - "memory.md#mem-obj-memory-cards"
            - "memory.md#mem-obj-categories"
          note: "Selection is supported; no retained learned ranking policy or relative relevance-score route is established here."
        - scope: "Rejected-check experience and candidate code at generation/evaluation consumers"
          assessment: "known"
          findings:
            - value: "learning"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-policy-candidate"
              note: "Rejected experience and diagnosis feed automatic retained behavior-shaping candidate source."
            - value: "knowledge"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-policy-candidate"
              note: "Rejected reasons and diagnosis supply contextual advice to the coding model."
            - value: "enforcement"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-retry-policy"
                - "runtime.md#rt-bap-candidate-policy"
              note: "Executed candidate retry/circuit rules permit or refuse retry/circuit behavior inside bounded evaluation."
          records:
            - "runtime.md#rt-rte-policy-candidate"
            - "runtime.md#rt-obj-retry-policy"
            - "runtime.md#rt-bap-candidate-policy"
          note: "The candidate rules have evaluator authority only; manifest eligibility does not extend them to live stable operation."
        - scope: "Optional Dify index/search output at a later model consumer"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-history-search"
          note: "Search requests mention reranking but no shipped later model-search consumer is recorded and provider scoring is opaque. Relative ranking authority of retained remote content is not established."
        - scope: "Other included suite memory routes: mem0, memobase, agentic-rag-for-user-memory, contextual-retrieval-for-user-memory; retrieval-pipeline, dense-embedding, sparse-embedding, structured-index, structured-knowledge-extraction, log-sanitization, agentic-rag, contextual-retrieval; other chapter loops, skills, fixtures and results."
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-trace-maintenance"
            - "memory.md#mem-rte-sequential-campaign"
          note: "These alternatives remain uninspected in the accepted memory inventory. Their actual consumers and forces cannot be enumerated or classified from directory names; no negative or complete-value conclusion follows."
      records:
        - "memory.md#mem-bap-memory-context"
        - "runtime.md#rt-obj-conversation-history"
        - "runtime.md#rt-rte-context-task"
        - "memory.md#mem-rte-trace-maintenance"
        - "memory.md#mem-rte-sequential-campaign"
        - "memory.md#mem-bap-campaign-state"
        - "memory.md#mem-obj-memory-states"
        - "memory.md#mem-rte-offline-maintenance"
        - "memory.md#mem-obj-memory-note"
        - "memory.md#mem-obj-memory-cards"
        - "memory.md#mem-obj-categories"
        - "runtime.md#rt-rte-policy-candidate"
        - "runtime.md#rt-obj-retry-policy"
        - "runtime.md#rt-bap-candidate-policy"
        - "memory.md#mem-rte-history-search"
      note: "Positive classifications cover the named inspected routes only. Included alternatives remain unresolved; this is not a suite-complete inventory of values. Actual consumers and forces uncertainty is retained in the corresponding units."
    write_agency:
      assessment: "partial"
      units:
        - scope: "Background extraction and model mutation admission"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-rte-trace-maintenance"
              note: "Model/software admits each mutation without per-content human approval."
          records:
            - "memory.md#mem-rte-trace-maintenance"
          note: "Manual process/save starts analysis; it does not make its ensuing fact admissions manual."
        - scope: "Sequential JSON state replacement and checkpoint admission"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-rte-sequential-campaign"
              note: "Host accepts parsed model replacement state; humans choose launch settings, not each retained fact."
          records:
            - "memory.md#mem-rte-sequential-campaign"
          note: "Judge grade reports results rather than vetoing prior memory admission."
        - scope: "Explicit human CLI content editing"
          assessment: "known"
          findings:
            - value: "manual"
              basis: "wired"
              records:
                - "memory.md#mem-rte-offline-maintenance"
              note: "An explicit operator add/update supplies or replaces retained note content."
          records:
            - "memory.md#mem-rte-offline-maintenance"
          note: "Manual is bounded to the operator route, not all calls to the manager."
        - scope: "Deterministic consolidation, eviction and raw interactive recording"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-rte-offline-maintenance"
              note: "Code chooses consolidation winners and evicts excess notes without per-winner approval."
            - value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-conversation-turn"
                - "memory.md#mem-rte-trace-maintenance"
              note: "The conversation route automatically records both dialogue sides."
          records:
            - "memory.md#mem-rte-offline-maintenance"
            - "memory.md#mem-obj-conversation-turn"
            - "memory.md#mem-rte-trace-maintenance"
          note: "Human dialogue authorship is separate from automatic recording/admission."
        - scope: "Retry candidate generation and artifact admission"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-policy-candidate"
              note: "Deterministic/model candidates and both accepted/rejected artifacts are retained by host code without per-candidate human approval."
          records:
            - "runtime.md#rt-rte-policy-candidate"
          note: "The launch is human-configured; production installation is not recorded."
        - scope: "Live context-history append"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-task"
                - "runtime.md#rt-obj-conversation-history"
              note: "Local loop appends messages and tool replies for later invocation."
          records:
            - "runtime.md#rt-rte-context-task"
            - "runtime.md#rt-obj-conversation-history"
          note: "No per-message approval is recorded."
        - scope: "Initial files and generic direct apply/update callers"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-memory-note"
            - "memory.md#mem-obj-memory-cards"
            - "memory.md#mem-obj-categories"
            - "memory.md#mem-rte-trace-maintenance"
            - "memory.md#mem-rte-offline-maintenance"
          note: "Caller-dependent initial content and exposed helper inputs do not identify human versus software control. Physical file I/O cannot decide admission agency."
        - scope: "Other included suite memory routes: mem0, memobase, agentic-rag-for-user-memory, contextual-retrieval-for-user-memory; retrieval-pipeline, dense-embedding, sparse-embedding, structured-index, structured-knowledge-extraction, log-sanitization, agentic-rag, contextual-retrieval; other chapter loops, skills, fixtures and results."
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-trace-maintenance"
            - "memory.md#mem-rte-sequential-campaign"
          note: "These alternatives remain uninspected in the accepted memory inventory. Their initial content and admission mechanisms cannot be enumerated or classified from directory names; no negative or complete-value conclusion follows."
      records:
        - "memory.md#mem-rte-trace-maintenance"
        - "memory.md#mem-rte-sequential-campaign"
        - "memory.md#mem-rte-offline-maintenance"
        - "memory.md#mem-obj-conversation-turn"
        - "runtime.md#rt-rte-policy-candidate"
        - "runtime.md#rt-rte-context-task"
        - "runtime.md#rt-obj-conversation-history"
        - "memory.md#mem-obj-memory-note"
        - "memory.md#mem-obj-memory-cards"
        - "memory.md#mem-obj-categories"
      note: "Positive classifications cover the named inspected routes only. Included alternatives remain unresolved; this is not a suite-complete inventory of values. Initial content and admission mechanisms uncertainty is retained in the corresponding units."
    curation_operations:
      assessment: "partial"
      units:
        - scope: "User-memory extracted facts and sequential replacement summaries"
          assessment: "known"
          findings:
            - value: "consolidate"
              basis: "wired"
              records:
                - "memory.md#mem-rte-trace-maintenance"
                - "memory.md#mem-rte-sequential-campaign"
              note: "Dialogue plus existing retained facts feed reduced standing facts/current memory for later consumption."
          records:
            - "memory.md#mem-rte-trace-maintenance"
            - "memory.md#mem-rte-sequential-campaign"
          note: "Wired extraction/replacement capacity does not prove faithful summarization; prompts alone do not establish novel-claim synthesis."
        - scope: "Offline note consolidation and write-side forgetting"
          assessment: "known"
          findings:
            - value: "dedup"
              basis: "wired"
              records:
                - "memory.md#mem-rte-offline-maintenance"
              note: "Normalized equal note content merges tags and keeps the newest version."
            - value: "consolidate"
              basis: "wired"
              records:
                - "memory.md#mem-rte-offline-maintenance"
              note: "The conflict pass reduces tag-grouped retained content to a newest winner."
            - value: "decay"
              basis: "wired"
              records:
                - "memory.md#mem-rte-offline-maintenance"
              note: "Superseded notes and excess oldest entries leave current retained storage."
          records:
            - "memory.md#mem-rte-offline-maintenance"
          note: "Recency-based selection is not semantic contradiction adjudication and no retained-history invalidation is established."
        - scope: "Interactive note/card replacement and deletion tools"
          assessment: "known"
          findings:
            - value: "evolve"
              basis: "wired"
              records:
                - "memory.md#mem-rte-trace-maintenance"
                - "memory.md#mem-obj-memory-cards"
                - "memory.md#mem-obj-categories"
              note: "Updates revise an existing addressed note/card; advanced cards are replaced rather than merged."
            - value: "decay"
              basis: "wired"
              records:
                - "memory.md#mem-rte-trace-maintenance"
              note: "Delete/clear removes current reliance by forgetting current entries, without a retained-history invalidation mechanism."
          records:
            - "memory.md#mem-rte-trace-maintenance"
            - "memory.md#mem-obj-memory-note"
            - "memory.md#mem-obj-memory-cards"
            - "memory.md#mem-obj-categories"
          note: "Already delivered live conversation can preserve old consequences; forgetting current entries is not universal withdrawal."
        - scope: "Sequential arbitrary replacement semantics"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-sequential-campaign"
            - "memory.md#mem-obj-memory-states"
          note: "JSON replacement is wired and consolidation is separately supported; mode requests and arbitrary output do not establish dedup, synthesis or preservation of conflict versions as implemented transformations."
        - scope: "Retry-policy candidate creation and retained rejected-check feedback"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-policy-candidate"
            - "runtime.md#rt-obj-retry-policy"
          note: "Exact-region generation creates a retained candidate from read-only shipped stable source, excluded from accumulated memory. It does not revise an existing accumulated candidate. Rejected feedback reaches later generation, but the records do not establish a controlled curation transformation over that retained feedback or another included memory entry. No curation value or bounded absence is established for this branch."
        - scope: "Other included suite memory routes: mem0, memobase, agentic-rag-for-user-memory, contextual-retrieval-for-user-memory; retrieval-pipeline, dense-embedding, sparse-embedding, structured-index, structured-knowledge-extraction, log-sanitization, agentic-rag, contextual-retrieval; other chapter loops, skills, fixtures and results."
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-trace-maintenance"
            - "memory.md#mem-rte-sequential-campaign"
          note: "These alternatives remain uninspected in the accepted memory inventory. Their implemented retained-content transformations cannot be enumerated or classified from directory names; no negative or complete-value conclusion follows."
      records:
        - "memory.md#mem-rte-trace-maintenance"
        - "memory.md#mem-rte-sequential-campaign"
        - "memory.md#mem-rte-offline-maintenance"
        - "memory.md#mem-obj-memory-note"
        - "memory.md#mem-obj-memory-cards"
        - "memory.md#mem-obj-categories"
        - "memory.md#mem-obj-memory-states"
        - "runtime.md#rt-rte-policy-candidate"
        - "runtime.md#rt-obj-retry-policy"
      note: "Positive classifications cover the named inspected routes only. Included alternatives remain unresolved; this is not a suite-complete inventory of values. Implemented retained-content transformations uncertainty is retained in the corresponding units."
    read_back_direction:
      assessment: "partial"
      units:
        - scope: "Conversation/analysis/context automatic prompt supply"
          assessment: "known"
          findings:
            - value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-rte-conversation-reload"
                - "memory.md#mem-rte-trace-maintenance"
                - "runtime.md#rt-rte-context-task"
              note: "A new chat/analysis/task triggers automatic insertion of retained facts or prior history without an item retrieval request."
          records:
            - "memory.md#mem-rte-conversation-reload"
            - "memory.md#mem-rte-trace-maintenance"
            - "runtime.md#rt-obj-conversation-history"
            - "runtime.md#rt-rte-context-task"
          note: "The user requests current work, not the particular retained items supplied by the host."
        - scope: "Sequential latest-state supply and checkpoint response reuse"
          assessment: "known"
          findings:
            - value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-rte-sequential-campaign"
              note: "Host selects latest state and stored purpose-labelled responses for later writer/answer or resumed work."
          records:
            - "memory.md#mem-rte-sequential-campaign"
            - "memory.md#mem-obj-memory-states"
          note: "Requested current evaluation is distinct from automatic selection of past material."
        - scope: "CLI query/show of retained user memory"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-rte-offline-maintenance"
              note: "The caller explicitly requests retained note/card material and receives matching/displayed content."
          records:
            - "memory.md#mem-rte-offline-maintenance"
          note: "The local request and requested return are one pull operation, not an extra push."
        - scope: "Rejected-control summary to subsequent coding proposal"
          assessment: "known"
          findings:
            - value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-policy-candidate"
              note: "Campaign automatically selects and inserts rejected-check history in its subsequent coding request."
          records:
            - "runtime.md#rt-rte-policy-candidate"
          note: "This is a within-campaign later invocation, not an installed successor reload."
        - scope: "History-search API and opaque Dify later consumption"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-history-search"
          note: "A storage/search API with unspecified caller does not establish the later consumer route. Neither an end-to-end pull nor a push can be classified from that capability alone."
        - scope: "Other included suite memory routes: mem0, memobase, agentic-rag-for-user-memory, contextual-retrieval-for-user-memory; retrieval-pipeline, dense-embedding, sparse-embedding, structured-index, structured-knowledge-extraction, log-sanitization, agentic-rag, contextual-retrieval; other chapter loops, skills, fixtures and results."
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-trace-maintenance"
            - "memory.md#mem-rte-sequential-campaign"
          note: "These alternatives remain uninspected in the accepted memory inventory. Their later-consumer routes and unresolved search consumers cannot be enumerated or classified from directory names; no negative or complete-value conclusion follows."
      records:
        - "memory.md#mem-rte-conversation-reload"
        - "memory.md#mem-rte-trace-maintenance"
        - "runtime.md#rt-obj-conversation-history"
        - "runtime.md#rt-rte-context-task"
        - "memory.md#mem-rte-sequential-campaign"
        - "memory.md#mem-obj-memory-states"
        - "memory.md#mem-rte-offline-maintenance"
        - "runtime.md#rt-rte-policy-candidate"
        - "memory.md#mem-rte-history-search"
      note: "Positive classifications cover the named inspected routes only. Included alternatives remain unresolved; this is not a suite-complete inventory of values. Later-consumer routes and unresolved search consumers uncertainty is retained in the corresponding units."
    read_back_signal:
      assessment: "partial"
      units:
        - scope: "All retained user facts and current-session raw history on chat"
          assessment: "known"
          findings:
            - value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-rte-conversation-reload"
                - "memory.md#mem-rte-trace-maintenance"
              note: "Chat/analysis trigger and enable flags supply all rendered memories; no item relevance query or enforced input token cap."
            - value: "identifier"
              basis: "wired"
              records:
                - "memory.md#mem-rte-conversation-reload"
              note: "Active-session identity matching selects raw turns delivered as history; user identity also scopes the reloaded retained store."
          records:
            - "memory.md#mem-rte-conversation-reload"
            - "memory.md#mem-rte-trace-maintenance"
          note: "Whole-store availability and actual identity-filtered raw-history selection are separate push operations."
        - scope: "Recent/unprocessed dialogue selection for background analysis"
          assessment: "known"
          findings:
            - value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-rte-trace-maintenance"
              note: "Interval/count and recent-tail window bound available transcript."
            - value: "identifier"
              basis: "wired"
              records:
                - "memory.md#mem-rte-trace-maintenance"
              note: "Processed turn-ID membership selects unprocessed retained turns delivered to analysis."
          records:
            - "memory.md#mem-rte-trace-maintenance"
          note: "IDs are marked before successful analysis; this selector is not a durability or correctness guarantee."
        - scope: "Live context-agent mode/history supply"
          assessment: "known"
          findings:
            - value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-task"
                - "runtime.md#rt-rte-context-ablation"
              note: "Configured mode includes or omits accumulated history/results without item-level semantic relevance targeting."
          records:
            - "runtime.md#rt-obj-conversation-history"
            - "runtime.md#rt-rte-context-task"
            - "runtime.md#rt-rte-context-ablation"
          note: "NO_HISTORY withholds stored memory; symbolic tool IDs are associations, not an evidenced identity-targeted relevance selector."
        - scope: "Sequential checkpoint and latest-state/receipt selection"
          assessment: "known"
          findings:
            - value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-rte-sequential-campaign"
              note: "Last-state position and session index choose the current memory wholesale."
            - value: "identifier"
              basis: "wired"
              records:
                - "memory.md#mem-rte-sequential-campaign"
              note: "Case/mode checkpoint identity, signature equality and successful-call purpose matching select reusable retained state/calls."
          records:
            - "memory.md#mem-rte-sequential-campaign"
            - "memory.md#mem-obj-memory-states"
          note: "Output token budget limits generated memory, not relevance selection of current-state input."
        - scope: "Rejected control feedback push"
          assessment: "known"
          findings:
            - value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-policy-candidate"
              note: "The campaign inserts its constructed rejected-history summary wholesale at the next coding request."
          records:
            - "runtime.md#rt-rte-policy-candidate"
          note: "The candidate hash is supplied metadata, not evidence of a hash-match selector for delivered feedback."
        - scope: "CLI request-driven query/show only"
          assessment: "inapplicable"
          findings: []
          records:
            - "memory.md#mem-rte-offline-maintenance"
          note: "Substring selection answers an explicit retained-material request. Push-signal classification is inapplicable to this pull operation, not to the broader mixed boundary."
        - scope: "Opaque history-search later-consumer branch"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-history-search"
          note: "Provider semantic/reranking parameters do not establish a consumed push payload or its operative selector. Known pull CLI routes do not resolve this alternative."
        - scope: "Other included suite memory routes: mem0, memobase, agentic-rag-for-user-memory, contextual-retrieval-for-user-memory; retrieval-pipeline, dense-embedding, sparse-embedding, structured-index, structured-knowledge-extraction, log-sanitization, agentic-rag, contextual-retrieval; other chapter loops, skills, fixtures and results."
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-trace-maintenance"
            - "memory.md#mem-rte-sequential-campaign"
          note: "These alternatives remain uninspected in the accepted memory inventory. Their actual automatic selectors and delivered parts cannot be enumerated or classified from directory names; no negative or complete-value conclusion follows."
      records:
        - "memory.md#mem-rte-conversation-reload"
        - "memory.md#mem-rte-trace-maintenance"
        - "runtime.md#rt-obj-conversation-history"
        - "runtime.md#rt-rte-context-task"
        - "runtime.md#rt-rte-context-ablation"
        - "memory.md#mem-rte-sequential-campaign"
        - "memory.md#mem-obj-memory-states"
        - "runtime.md#rt-rte-policy-candidate"
        - "memory.md#mem-rte-offline-maintenance"
        - "memory.md#mem-rte-history-search"
      note: "Positive classifications cover the named inspected routes only. Included alternatives remain unresolved; this is not a suite-complete inventory of values. Actual automatic selectors and delivered parts uncertainty is retained in the corresponding units."
    trace_learning:
      assessment: "partial"
      units:
        - scope: "Automatic user-memory dialogue extraction and later answer reload"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-rte-trace-maintenance"
                - "memory.md#mem-rte-conversation-reload"
              note: "Raw sessions feed automatic persisted fact updates; a later answer invocation receives derived context."
          records:
            - "memory.md#mem-rte-trace-maintenance"
            - "memory.md#mem-rte-conversation-reload"
          note: "This qualifies structurally despite swallowed save failures and absent observed benefit."
        - scope: "Sequential session-fed checkpoint memories and later writer/answer"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-rte-sequential-campaign"
                - "memory.md#mem-obj-memory-states"
              note: "Session traces automatically produce retained replacement states used by subsequent model invocations."
          records:
            - "memory.md#mem-rte-sequential-campaign"
            - "memory.md#mem-obj-memory-states"
          note: "Within-run and resumed consumption qualify; source-based judge grades need not feed a further update."
        - scope: "Automatic retry-policy candidate from supplied failure experience"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-policy-candidate"
                - "runtime.md#rt-obj-retry-policy"
                - "runtime.md#rt-bap-candidate-policy"
              note: "Synthetic failure trajectories and rejected-check experience feed automatic retained policy generation; candidate functions are consumed in later evaluation."
          records:
            - "runtime.md#rt-rte-policy-candidate"
            - "runtime.md#rt-obj-retry-policy"
            - "runtime.md#rt-bap-candidate-policy"
          note: "A durable formal behavior-shaping artifact qualifies without live installation; this does not establish exercised self-improvement or learned weights."
        - scope: "Live raw context-history capture without a recorded durable derived update"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-obj-conversation-history"
            - "runtime.md#rt-rte-context-task"
          note: "Raw logging and later visibility alone do not establish a durable trace-derived behavior-shaping write. No ABS record supports a local no; this route remains not-determinable for a stronger negative."
        - scope: "Generic initial/direct retained content and opaque remote branches"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-memory-note"
            - "memory.md#mem-obj-memory-cards"
            - "memory.md#mem-obj-categories"
            - "memory.md#mem-rte-history-search"
          note: "Initial/admission origins and remote update-to-later-consumer chains are unresolved. They cannot be made no by an inspected route elsewhere."
        - scope: "Other included suite memory routes: mem0, memobase, agentic-rag-for-user-memory, contextual-retrieval-for-user-memory; retrieval-pipeline, dense-embedding, sparse-embedding, structured-index, structured-knowledge-extraction, log-sanitization, agentic-rag, contextual-retrieval; other chapter loops, skills, fixtures and results."
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-trace-maintenance"
            - "memory.md#mem-rte-sequential-campaign"
          note: "These alternatives remain uninspected in the accepted memory inventory. Their qualifying automatic trace-fed writes cannot be enumerated or classified from directory names; no negative or complete-value conclusion follows."
      records:
        - "memory.md#mem-rte-trace-maintenance"
        - "memory.md#mem-rte-conversation-reload"
        - "memory.md#mem-rte-sequential-campaign"
        - "memory.md#mem-obj-memory-states"
        - "runtime.md#rt-rte-policy-candidate"
        - "runtime.md#rt-obj-retry-policy"
        - "runtime.md#rt-bap-candidate-policy"
        - "runtime.md#rt-obj-conversation-history"
        - "runtime.md#rt-rte-context-task"
        - "memory.md#mem-obj-memory-note"
        - "memory.md#mem-obj-memory-cards"
        - "memory.md#mem-obj-categories"
        - "memory.md#mem-rte-history-search"
      note: "Positive classifications cover the named inspected routes only. Included alternatives remain unresolved; this is not a suite-complete inventory of values. Qualifying automatic trace-fed writes uncertainty is retained in the corresponding units."
    trace_source:
      assessment: "partial"
      units:
        - scope: "User-memory extracted standing facts"
          assessment: "known"
          findings:
            - value: "session-logs"
              basis: "wired"
              records:
                - "memory.md#mem-rte-trace-maintenance"
                - "memory.md#mem-obj-conversation-turn"
              note: "Recorded user/assistant conversational turns are the original input to automatic fact extraction."
          records:
            - "memory.md#mem-rte-trace-maintenance"
            - "memory.md#mem-obj-conversation-turn"
          note: "Session/time metadata does not turn dialogue into event streams."
        - scope: "Sequential replacement states from fixture sessions"
          assessment: "known"
          findings:
            - value: "session-logs"
              basis: "wired"
              records:
                - "memory.md#mem-rte-sequential-campaign"
              note: "Each automatic replacement consumes one historical conversational session plus prior memory."
          records:
            - "memory.md#mem-rte-sequential-campaign"
            - "memory.md#mem-obj-memory-states"
          note: "Fixture provenance is unresolved but recorded content origin is dialogue, not a serialization-based event-stream classification."
        - scope: "Retry-policy diagnosis and rejected-check input to automatic candidate source"
          assessment: "known"
          findings:
            - value: "trajectories"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-policy-candidate"
              note: "Linked supplied retry failure cases record attempts/actions and failure outcomes used by diagnosis and generation."
            - value: "tool-traces"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-policy-candidate"
              note: "Recorded evaluator failed checks and rejection feedback from candidate execution enter the later coding request."
          records:
            - "runtime.md#rt-rte-policy-candidate"
            - "runtime.md#rt-obj-retry-policy"
          note: "The software-authored control and synthetic case provenance limit operational claims, not these content-origin classifications."
        - scope: "Other initial/direct content, live raw logging and optional remote updates"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-memory-note"
            - "memory.md#mem-obj-memory-cards"
            - "memory.md#mem-obj-categories"
            - "runtime.md#rt-obj-conversation-history"
            - "memory.md#mem-rte-history-search"
          note: "Qualifying automatic durable derived writes and original trace inputs are not established for these parts. Trace-source is unresolved, not inapplicable through another route’s bounded classification."
        - scope: "Other included suite memory routes: mem0, memobase, agentic-rag-for-user-memory, contextual-retrieval-for-user-memory; retrieval-pipeline, dense-embedding, sparse-embedding, structured-index, structured-knowledge-extraction, log-sanitization, agentic-rag, contextual-retrieval; other chapter loops, skills, fixtures and results."
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-trace-maintenance"
            - "memory.md#mem-rte-sequential-campaign"
          note: "These alternatives remain uninspected in the accepted memory inventory. Their original inputs to every qualifying and unresolved trace-fed write cannot be enumerated or classified from directory names; no negative or complete-value conclusion follows."
      records:
        - "memory.md#mem-rte-trace-maintenance"
        - "memory.md#mem-obj-conversation-turn"
        - "memory.md#mem-rte-sequential-campaign"
        - "memory.md#mem-obj-memory-states"
        - "runtime.md#rt-rte-policy-candidate"
        - "runtime.md#rt-obj-retry-policy"
        - "memory.md#mem-obj-memory-note"
        - "memory.md#mem-obj-memory-cards"
        - "memory.md#mem-obj-categories"
        - "runtime.md#rt-obj-conversation-history"
        - "memory.md#mem-rte-history-search"
      note: "Positive classifications cover the named inspected routes only. Included alternatives remain unresolved; this is not a suite-complete inventory of values. Original inputs to every qualifying and unresolved trace-fed write uncertainty is retained in the corresponding units."
---

# AI Agents in Depth memory profile

## Comparison rationale

This is a partial comparison of separate workflows, not a shared suite runtime. All positive bases are implementation wiring, not observed operation or demonstrated benefit. The unresolved alternatives in every axis preserve the accepted memory inventory; no directory name supplies a storage or learning value. There are no supersessions: reconciliation preserves the context container and its epistemic parts and finds distinct identities rather than replacements.

JSON is not a behavioral form. Facts/backstories are natural-language information at model consumers, while addresses, resume controls and executable policy have symbolic consumers. The PDF and currency parts of [RT-OBJ-conversation-history](runtime.md#rt-obj-conversation-history) retain their different derivation paths through [EPI-RTE-pdf-import](epistemic.md#epi-rte-pdf-import) and [EPI-RTE-currency-conversion](epistemic.md#epi-rte-currency-conversion). Shipped model weights and static instructions do not become accumulated memory merely because they participate in inference.

Update and downstream forces differ. [MEM-RTE-trace-maintenance](memory.md#mem-rte-trace-maintenance) and [MEM-RTE-sequential-campaign](memory.md#mem-rte-sequential-campaign) consume dialogue to produce durable context; the derived output supplies knowledge to later answering calls. The trace-learning positives identify this automatic write chain, not improved capacity, accepted truth or parametric training. Initial files, direct-helper caller control and provider payload provenance remain unresolved. No bounded absence records justify a trace-learning no.

The deterministic consolidation in [MEM-RTE-offline-maintenance](memory.md#mem-rte-offline-maintenance) reduces existing claims, deduplicates normalized equal text and forgets superseded/excess notes. It does not validate contradiction, synthesize new claims or retain an invalidation history. Interactive replacements support evolve. Arbitrary sequential JSON output does not establish every requested semantic transformation. Retry-policy generation in [RT-RTE-policy-candidate](runtime.md#rt-rte-policy-candidate) creates retained candidate source from the read-only shipped stable input identified by [RT-OBJ-retry-policy](runtime.md#rt-obj-retry-policy). That static input is excluded from accumulated memory; changing its rule while creating a candidate does not establish evolve over an existing retained memory entry. Retention of candidates and reuse of rejected feedback do not establish a controlled curation operation over those objects. This branch therefore has no positive curation finding and remains not-determinable, without withdrawing interactive evolve or retry-policy trace learning.

The pull CLI and automatic context supply coexist. [MEM-RTE-conversation-reload](memory.md#mem-rte-conversation-reload) selects all facts coarsely but identity-filters active-session history; recent processing additionally matches processed turn IDs. [MEM-RTE-sequential-campaign](memory.md#mem-rte-sequential-campaign) uses checkpoint identity/signature/purpose to reuse retained work and selects latest memory wholesale. A requested query return is not a second push. [MEM-RTE-history-search](memory.md#mem-rte-history-search) remains a capability with no established shipped model consumer; semantic-search/reranking settings do not establish vector storage, parametric payload form or end-to-end read-back.

[RT-RTE-policy-candidate](runtime.md#rt-rte-policy-candidate) supplies a separate trace-fed behavior-shaping artifact: retained candidate source is consumed by evaluator function calls, while rejected reasons reach a later coding request. Synthetic trajectories and rejected evaluator feedback retain their respective trajectory and tool-trace origins. This structural yes does not install a successor or close a self-improvement attribution chain. Candidate enforcement is bounded to [RT-BAP-candidate-policy](runtime.md#rt-bap-candidate-policy); eligibility and artifact delivery do not imply stable deployment.

Source-read log: no source files were read. Classification used only the supplied accepted members, their governing types/contracts and reconciliation. Missing recorded facts were retained as coverage limits, not filled by new evidence.
