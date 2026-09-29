---
{
  "type": "types/agent-memory-analysis-report.md",
  "description": "PageIndex retained document indexes, caller transcript replay, metadata push and opaque cloud read boundaries",
  "run-id": "AAS-2026-09-28-pageindex-01",
  "source-identity": "https://github.com/VectifyAI/PageIndex",
  "reviewed-boundary": "619cbd89f6dd02681a8cfc5d00b1f9b4848e973e",
  "report-status": "complete",
  "canonical-register-sha256": "eb29d6220d31070e07653fd03982e1505ff83bfbd058915cd72f256e22b5285e",
  "worker-model": "unknown",
  "method-sha256": "bef249eb62e6a6af7bb822f385b5085a221a12eea0d50c1648e78b3da69889bf",
  "finalized-from": "1053fd28e361a1c661cdbe409f254e5d01eb8a120025ff24a03f1a59e03efb18",
  "memory-comparison": {
    "scope": "Local retained PDF page text, document metadata and hierarchical indexes; standalone retained-index optimization; requested reads, automatic metadata targeting and caller-owned replay; cloud document/folder objects and external-agent adapters only at the inspectable client boundary. Static prompts, transient indexing state and inaccessible hosted/model internals are not presumed memories.",
    "axes": {
      "storage_substrate": {
        "assessment": "partial",
        "values": [
          "files",
          "service-object",
          "in-memory"
        ],
        "evidence": {
          "files": {
            "basis": "wired",
            "records": [
              "OBJ-3",
              "RTE-6"
            ],
            "note": "Local document JSON and retained optimizer input/output files."
          },
          "service-object": {
            "basis": "wired",
            "records": [
              "OBJ-4",
              "RTE-11"
            ],
            "note": "Cloud document and folder identities are addressed through HTTP/MCP; server backing store is opaque."
          },
          "in-memory": {
            "basis": "afforded",
            "records": [
              "OBJ-5",
              "RTE-10"
            ],
            "note": "Caller can retain returned transcript lists and submit them on a later invocation; SDK does not persist them."
          }
        },
        "records": [
          "OBJ-3",
          "OBJ-4",
          "OBJ-5"
        ],
        "note": "Local files and caller replay are inspectable; cloud storage internals prevent a complete substrate set."
      },
      "representational_form": {
        "assessment": "partial",
        "values": [
          "natural-language",
          "symbolic"
        ],
        "evidence": {
          "natural-language": {
            "basis": "wired",
            "records": [
              "OBJ-3",
              "RTE-8",
              "RTE-9"
            ],
            "note": "Pages, summaries, titles and document descriptions reach model consumers."
          },
          "symbolic": {
            "basis": "wired",
            "records": [
              "OBJ-3",
              "RTE-8"
            ],
            "note": "Tree relationships, page spans and structured metadata govern reconstruction and selection."
          }
        },
        "records": [
          "OBJ-3",
          "OBJ-4",
          "OBJ-5"
        ],
        "note": "Cloud native content blocks and hosted processing remain opaque beyond the client boundary; readable stubs do not classify all payloads."
      },
      "lineage": {
        "assessment": "partial",
        "values": [
          "imported",
          "other-compiled",
          "authored"
        ],
        "evidence": {
          "imported": {
            "basis": "wired",
            "records": [
              "RTE-5"
            ],
            "note": "PDF text/bookmarks enter retained document objects."
          },
          "other-compiled": {
            "basis": "wired",
            "records": [
              "RTE-5",
              "RTE-6"
            ],
            "note": "Layout, index structure and model summaries derive from source documents and indexes, not action traces."
          },
          "authored": {
            "basis": "wired",
            "records": [
              "OBJ-3",
              "RTE-5",
              "OBJ-4"
            ],
            "note": "Caller-authored metadata and folder descriptions can be retained through the SDK."
          }
        },
        "records": [
          "RTE-5",
          "RTE-6",
          "OBJ-4"
        ],
        "note": "Cloud derivation is not inspectable. Raw replay transcripts do not establish trace-extracted derived memory."
      },
      "behavioral_authority": {
        "assessment": "partial",
        "values": [
          "knowledge",
          "routing",
          "ranking"
        ],
        "evidence": {
          "knowledge": {
            "basis": "wired",
            "records": [
              "RTE-8",
              "RTE-9"
            ],
            "note": "Pages and descriptions are supplied as evidence/context for answers."
          },
          "routing": {
            "basis": "wired",
            "records": [
              "RTE-8"
            ],
            "note": "Tree structure and summaries supply navigational context; page spans govern node-text reconstruction."
          },
          "ranking": {
            "basis": "wired",
            "records": [
              "RTE-8"
            ],
            "note": "Retained createdAt fields determine the order of local document discovery results."
          }
        },
        "records": [
          "RTE-8",
          "RTE-9",
          "RTE-11"
        ],
        "note": "Local document contents have evidential/navigational force; static grounding rules are excluded. Cloud consumed payload authority beyond the visible interfaces is unresolved."
      },
      "write_agency": {
        "assessment": "partial",
        "values": [
          "automatic",
          "manual"
        ],
        "evidence": {
          "automatic": {
            "basis": "wired",
            "records": [
              "RTE-5",
              "RTE-6"
            ],
            "note": "Once invoked, extraction, summary generation and optimizer transformations write without per-entry human authoring."
          },
          "manual": {
            "basis": "wired",
            "records": [
              "RTE-5",
              "RTE-7"
            ],
            "note": "Callers supply metadata and directly request deletion; these paths coexist with automatic extraction."
          }
        },
        "records": [
          "RTE-5",
          "RTE-6",
          "RTE-7",
          "RTE-11"
        ],
        "note": "External hosted write mechanisms are not visible. Human-triggered indexing is still automatic extraction."
      },
      "curation_operations": {
        "assessment": "partial",
        "values": [
          "consolidate",
          "dedup",
          "evolve",
          "decay"
        ],
        "evidence": {
          "consolidate": {
            "basis": "wired",
            "records": [
              "RTE-6"
            ],
            "note": "Standalone optimizer collapses retained tree substructure while preserving removed titles as key_items."
          },
          "dedup": {
            "basis": "wired",
            "records": [
              "RTE-6"
            ],
            "note": "Same-page frontier siblings with identical retrieval spans collapse into one retained index node."
          },
          "evolve": {
            "basis": "wired",
            "records": [
              "RTE-6"
            ],
            "note": "An existing retained structure can be refined with admitted child sections and written as an optimized replacement artifact."
          },
          "decay": {
            "basis": "wired",
            "records": [
              "RTE-7"
            ],
            "note": "Explicit document deletion forgets the local retained bundle, without history retention."
          }
        },
        "records": [
          "RTE-6",
          "RTE-7",
          "RTE-11"
        ],
        "note": "These positives concern retained-tree optimization and deletion, not first-time acquisition or filename collision handling. Hosted curation is unknown; generated summaries alone do not establish synthesis of new claims."
      },
      "read_back_direction": {
        "assessment": "partial",
        "values": [
          "pull",
          "push"
        ],
        "evidence": {
          "pull": {
            "basis": "wired",
            "records": [
              "RTE-8",
              "RTE-11"
            ],
            "note": "Model tool calls request stored outlines/pages; direct SDK reads and cloud retrieval are also requested."
          },
          "push": {
            "basis": "wired",
            "records": [
              "RTE-9"
            ],
            "note": "Built-in chat automatically supplies retained metadata selected by caller-provided document/folder identifiers before the model asks for it."
          }
        },
        "records": [
          "RTE-8",
          "RTE-9",
          "RTE-10",
          "RTE-11"
        ],
        "note": "Both directions are wired locally. Hosted server internals can add hidden read paths."
      },
      "read_back_signal": {
        "assessment": "partial",
        "values": [
          "identifier"
        ],
        "evidence": {
          "identifier": {
            "basis": "wired",
            "records": [
              "RTE-9"
            ],
            "note": "Chat trigger matches document IDs to retained metadata; cloud folder targeting matches an ID to a listed folder and supplies its retained name/description."
          }
        },
        "records": [
          "RTE-9",
          "RTE-11"
        ],
        "note": "This classifies push selection only. Model-chosen tool requests and size-limited requested responses are pull; cloud automatic selectors are unknown."
      },
      "trace_learning": {
        "assessment": "not-determinable",
        "values": [],
        "evidence": {},
        "records": [
          "ABS-1",
          "RTE-10",
          "RTE-11"
        ],
        "note": "No automatic trace-to-derived-durable-memory write was found in the local SDK paths. Included hosted branches are opaque, so a system-wide negative and its dependent classifications are unwarranted."
      },
      "trace_source": {
        "assessment": "not-determinable",
        "values": [],
        "evidence": {},
        "records": [
          "ABS-1",
          "RTE-10",
          "RTE-11"
        ],
        "note": "No automatic trace-to-derived-durable-memory write was found in the local SDK paths. Included hosted branches are opaque, so a system-wide negative and its dependent classifications are unwarranted."
      },
      "learning_scope": {
        "assessment": "not-determinable",
        "values": [],
        "evidence": {},
        "records": [
          "ABS-1",
          "RTE-10",
          "RTE-11"
        ],
        "note": "No automatic trace-to-derived-durable-memory write was found in the local SDK paths. Included hosted branches are opaque, so a system-wide negative and its dependent classifications are unwarranted."
      },
      "learning_timing": {
        "assessment": "not-determinable",
        "values": [],
        "evidence": {},
        "records": [
          "ABS-1",
          "RTE-10",
          "RTE-11"
        ],
        "note": "No automatic trace-to-derived-durable-memory write was found in the local SDK paths. Included hosted branches are opaque, so a system-wide negative and its dependent classifications are unwarranted."
      },
      "distilled_form": {
        "assessment": "not-determinable",
        "values": [],
        "evidence": {},
        "records": [
          "ABS-1",
          "RTE-10",
          "RTE-11"
        ],
        "note": "No automatic trace-to-derived-durable-memory write was found in the local SDK paths. Included hosted branches are opaque, so a system-wide negative and its dependent classifications are unwarranted."
      },
      "faithfulness_tested": {
        "assessment": "not-determinable",
        "values": [],
        "evidence": {},
        "records": [
          "ABS-2"
        ],
        "note": "Source inspection and reported benchmarks supply no retained execution evidence in this commission testing answer dependence on recalled content; no causal or observed claim is made."
      }
    }
  }
}
---

# PageIndex memory specialist report

## Boundary and evidence

This is the fresh memory/context pass for the frozen PageIndex commission. The source is `https://github.com/VectifyAI/PageIndex` at `619cbd89f6dd02681a8cfc5d00b1f9b4848e973e`, cutoff 2026-09-28. The boundary is a memory/knowledge/context-engineering system, complete artifact but partial loop. Conclusions are code-grounded wiring, with source-native design claims separately attributed. No execution evidence was produced.

Commission provenance: SRC-1 is the implementation layer of that repository and revision, scoped to `pageindex/`, `run_pageindex.py`, tests as implementation evidence, and `pyproject.toml`. SRC-2 is doctrine/design at the same identity and revision, scoped to `README.md`, `pageindex/flash/README.md`, docstrings and prompts. These are provenance references, not new source declarations.

Inspected through commit-addressed Git reads: SRC-1 `pageindex/local_store.py`, `pageindex/local_api.py`, `pageindex/agent_tools.py`, `pageindex/local_chat.py`, `pageindex/client.py`, `pageindex/cloud_api.py`, `pageindex/flash/api.py`, `pageindex/page_index_classic.py`, `pageindex/tree_optimize.py`, `pageindex/utils.py`, and the three adapters `pageindex/integrations/openai_agents.py`, `pageindex/integrations/anthropic_sdk.py`, `pageindex/integrations/claude_agent_sdk.py`. SRC-2 inspection covered the introductory/quickstart claims in `README.md`, Flash's construction description in `pageindex/flash/README.md`, and the inspected executable paths' prompts/docstrings. Searches of `pageindex/chat_stream.py` also covered persistence/compaction terms. Source quotation selections came only from delivered bounded spans; truncated broad reads were not used for omitted-span conclusions.

Included: standard and Flash acquisition, index optimization, retained pages/tree/metadata, deletion, direct SDK reads, built-in chat, caller-controlled replay, client-visible cloud objects, and external SDK adapters. Hosted service internals, model processing, external linked benchmarks and deployment permissions are excluded; they prevent claims of complete hosted persistence, selection, transformation, semantic accuracy or deployment enforcement. Prior analyses and audits were not loaded.

## Core ideas

PageIndex keeps the source pages separate from a navigational tree. The persisted tree drops duplicated node text, and later node reads reconstruct it from page spans. Summaries and descriptions help models choose where to read; page content remains available separately. This is document-derived memory rather than demonstrated experience-derived learning (OBJ-3, RTE-5, RTE-8).

Flash's initial tree comes from PDF structure/layout, but the default managed path also refines it and generates summaries with models. Standard construction uses the model to form/check a TOC, repair criticized title/page assertions and retry with the current candidate and remaining errors before deterministic merge and summary generation. This is a narrow candidate-map criticism loop even though its method rules are fixed; exhausted repairs can still return an imperfect map. The distinction matters: a claim that tree extraction is model-free cannot cover all construction lanes. The standalone optimizer also admits changes to an already retained JSON index, giving an actual maintenance path beyond first-time acquisition (RTE-5, RTE-6).

Read-back has two different operations. Models pull requested outlines and pages through tools. Separately, built-in chat pushes retained document/folder metadata into the first user message using upstream caller IDs. That second route is real identifier-selected push, even though document targeting originates with an operator. The requested page responses' character budget is not a second push selector (RTE-8, RTE-9).

Curiosity correction: "semantic" tool descriptions are not evidence for a local ranker. Local relevance sort/query is rejected, and discovery is time-ordered; the model is expected to compare names/descriptions. Likewise, the tree's JSON shape is symbolic structure in files, not evidence for a graph database. Transcript "memory" is an afforded caller replay contract, not an SDK durable session store or automatic compaction (RTE-8, RTE-10, ABS-1).

Cloud tools are dynamically discovered and native adapters can deliver content blocks to models that plain-string wrappers render differently. A text display or process trace cannot establish the form, authority or selectors of every cloud payload. The comparison profile therefore keeps supported local positives while marking opaque included branches incomplete (OBJ-4, RTE-11).

## Shared records

### Components

None declared in this member. CMP-1 and enclosing RTE-1 retain their commissioned identities; no component-level inference is needed for the comparison profile.

### Operative objects

#### OBJ-3 — Local retained document bundle and index files

Conclusion status: wired. Source: SRC-1 `pageindex/local_store.py`, `pageindex/local_api.py`, `pageindex/tree_optimize.py`.

The SDK retains `tree.json`, `pages.json`, and `doc.json` under a document ID, with a reconstructible `manifest.json` cache of metadata. Page text is imported from PDF extraction; tree nodes, spans, summaries and document description are compiled from the document; caller metadata is authored. Natural-language operative parts are pages/titles/summaries/descriptions, symbolic parts are node relationships/page spans/IDs/status and metadata fields. Storage substrate is files. The standalone optimizer accepts a retained JSON structure and emits another JSON structure; it does not automatically replace the SDK store.

Consumers are RTE-8 and RTE-9, with knowledge/routing/ranking force detailed there. Document metadata is not a stored instruction registry; guidance surrounding it is generated or static. Atomic replacement is per JSON file, not a demonstrated multi-file transaction. Store reads can treat unreadable JSON as absent; listing can rebuild the manifest. There is no retention time-to-live in these paths. Deletion is RTE-7. Original PDF bytes are not copied into this SDK bundle.

> _write_json_atomic(doc_dir / "tree.json", tree)
>         _write_json_atomic(doc_dir / "pages.json", pages)
>         _write_json_atomic(doc_dir / "doc.json", meta)
> --- `pageindex/local_store.py:120-122` @ `619cbd89f6dd02681a8cfc5d00b1f9b4848e973e`

Caller metadata survives admission into the record:

> "metadata": metadata,
>                 "mode": mode,
> --- `pageindex/local_api.py:169-170` @ `619cbd89f6dd02681a8cfc5d00b1f9b4848e973e`

#### OBJ-4 — Client-addressed cloud document and folder objects

Conclusion status: wired. Source: SRC-1 `pageindex/cloud_api.py`, `pageindex/agent_tools.py`, `pageindex/integrations/anthropic_sdk.py`.

The client addresses cloud document metadata/tree/OCR/retrieval objects and folder metadata by service identity. Storage substrate at this boundary is service-object; physical backend and full payload form/lineage remain uninspected. Caller-authored JSON metadata can accompany document upload, and folder creation accepts name and description. Names/descriptions/IDs visible in targeting are natural-language/symbolic parts. This does not classify opaque native image or other MCP content, nor all hosted derived state. Own-model consumers are wired through RTE-11; hosted chat internals are not visible.

> response = requests.get(
>             f"{self.BASE_URL}/doc/{_enc(doc_id)}/metadata/",
>             headers=self._headers(),
>             timeout=30
>         )
> --- `pageindex/cloud_api.py:419-423` @ `619cbd89f6dd02681a8cfc5d00b1f9b4848e973e`

#### OBJ-5 — Caller-owned conversation history

Conclusion status: afforded. Source: SRC-1 `pageindex/local_chat.py`, SRC-2 `pageindex/client.py`.

Responses returns complete new transcript items, including executed tool outputs; Messages returns appendable new messages. These lists contain natural-language content and symbolic tool/message envelopes. They are raw invocation outputs imported into a later call, not a derived memory extraction. Caller-held in-memory lists can span invocations; disk retention and task horizon are the caller's responsibility. RTE-10 wires receipt of supplied history but leaves the actual cross-call retention loop afforded. No SDK persistence, summary artifact or automatic rewrite is established by the word "memory" in the docstring.

> Append the returned ``items`` to your next call's ``input`` verbatim
>         to keep provider prompt-cache prefix continuity and the agent's
>         memory of what it already read.
> --- `pageindex/client.py:1690-1692` @ `619cbd89f6dd02681a8cfc5d00b1f9b4848e973e`

### Routes

#### RTE-5 — Acquire and compile a local document index

Implementation conclusion status: wired. Source: SRC-1 `pageindex/local_api.py`, `pageindex/page_index_classic.py`, `pageindex/flash/api.py`, `pageindex/utils.py`.

Trigger/owner: caller invokes local `submit_document` with PDF and optional metadata; LocalAPI owns extraction, mode selection and save. Producer: PyPDF2 page extraction plus standard model-based construction or Flash layout/bookmark extraction, optimization and summary routines. Retained input: caller's PDF; output/persistence: OBJ-3 under a new UUID and unique name. Immediate return is document ID/name. Later read-back is RTE-8 and RTE-9, across later questions and invocations, until deletion. Delegated visibility: model calls see relevant pages, child summaries or a cleaned tree, not an automatically complete document bundle. Selection predicate: submitted PDF and mode, with summary inputs shaped by node spans; no retrieval query or execution trace feeds the write. Activation/effect: persisted records are wired to later readers; improved answers are unobserved.

Admission and recovery: reject missing/non-PDF/blank source, invalid metadata, unsupported local options, empty standard structure, Flash unreadable/large flat fallback, and out-of-bounds tree pages. Summary generation may leave individual failures empty, but all-model failure is rejected; a document-description prompt rejected with HTTP 400 may leave an empty description. Final name check/save runs under the store lock where available. Rejection before save leaves no completed new record; writes are atomic per file, with no general rollback transaction demonstrated. Re-upload creates another ID/name rather than revising an existing SDK entry.

Guidance and retained reasons: standard TOC prompts and fixed checks ask the model to construct/verify document structure; Flash layout rules establish the initial tree, then the optimizer's fixed page-cost rule refines it. Leaf summaries describe page content; parent summaries consume child summaries plus up to three leading pages. Short Flash leaves under the default 200-token threshold reuse raw text; model summaries are asked for 150 words by default, not deterministically clipped to that many. A one-sentence description derives from the cleaned structure. Stored artifacts retain source-derived titles/spans/summaries and caller metadata, not a rationale for why summary claims should be trusted. Their fields are individually inspectable, but the SDK offers no patch-in-place document editing route here.

Decision roles and operating mode: this is a caller-triggered batch indexing operation. The caller chooses source PDF, mode and configuration; computation proposes and admits each index entry without an internal human review step. Standard proposal roles are the configured model constructing title/page candidates and the fixer proposing replacement physical indices. The verifier model decides whether a proposed title appears/starts on its asserted page; controller code turns these answers into admission, retry, fallback or failure. Flash proposal roles are layout/bookmark extraction and optional model refinement, with deterministic structure/cost checks; its summary model proposes descriptions. Final local veto roles are input, structure, summary-failure and page-bound checks. The standard content checker has source page text as an answer oracle, and the fixer receives neighboring pages bounded by currently accepted entries. Neither has a retained gold TOC, independent downstream QA oracle, nor guaranteed error-free source extraction. Model agreement is an interpreted judgment, distinct from codified page-bound checks.

The standard candidate is an explicit map asserting that a named section appears or starts on a physical page. `check_title_appearance` tests exactly that content. Its prompt requests a reason and yes/no answer, but its returned record drops model `thinking`, keeping item identity, answer, title and page. Negative answers blame the candidate location and select it for repair; the code does not diagnose whether the source extraction, model checker or auxiliary assumptions caused the discrepancy. Fixes propose another location from a bounded source span, recheck it, and update the TOC only when the checker says yes.

> Your job is to check if the given section appears or starts in the given page_text.
> --- `pageindex/page_index_classic.py:91-91` @ `619cbd89f6dd02681a8cfc5d00b1f9b4848e973e`

> return {'list_index': item['list_index'], 'answer': answer, 'title': title, 'page_number': page_number}
> --- `pageindex/page_index_classic.py:113-113` @ `619cbd89f6dd02681a8cfc5d00b1f9b4848e973e`

> check_item = incorrect_item.copy()
>         check_item['physical_index'] = physical_index_int
>         check_result = await check_title_appearance(check_item, page_list, start_index, model)
> --- `pageindex/page_index_classic.py:992-994` @ `619cbd89f6dd02681a8cfc5d00b1f9b4848e973e`

> if result['is_valid']:
>             # Add bounds checking to prevent IndexError
>             list_idx = result['list_index']
>             if 0 <= list_idx < len(toc_with_page_number):
>                 toc_with_page_number[list_idx]['physical_index'] = result['physical_index']
> --- `pageindex/page_index_classic.py:1018-1022` @ `619cbd89f6dd02681a8cfc5d00b1f9b4848e973e`

The controller verifies the candidate and accepts a fully checked result, attempts up to three repair rounds when successful-check accuracy exceeds 0.6 with remaining errors, or changes construction strategy on the other branches (with-page-number TOC to no-page-number TOC to no-TOC, then failure). Crucially, after repair it returns the TOC even if `incorrect_results` remains nonempty. Failed checker calls are omitted from the successful-call accuracy denominator; exceptions from individual repairs are omitted from that repair's result list. These are bounded best-effort acceptance rules, not an invariant that every retained title/page assertion was verified. Final local page bounds do not repair this semantic gap.

> current_toc, current_incorrect = await fix_incorrect_toc(current_toc, page_list, current_incorrect, start_index, model, logger)
> --- `pageindex/page_index_classic.py:1053-1053` @ `619cbd89f6dd02681a8cfc5d00b1f9b4848e973e`

> if accuracy > 0.6 and len(incorrect_results) > 0:
>         toc_with_page_number, incorrect_results = await fix_incorrect_toc_with_retries(toc_with_page_number, page_list, incorrect_results,start_index=start_index, max_attempts=3, model=opt.model, logger=logger)
>         return toc_with_page_number
> --- `pageindex/page_index_classic.py:1156-1158` @ `619cbd89f6dd02681a8cfc5d00b1f9b4848e973e`

Theory-builder conditions 1–4, assessed separately for the standard candidate map rather than the fixed method:

- Condition 1 conclusion status: wired. Candidate title/physical-index entries localize assertions about document organization and expose each title and page for revision. This is the narrow factual-map reading of formulated theory; it does not assert explanatory generalization beyond this PDF.
- Condition 2 conclusion status: wired. Verification selects source pages from what each entry asserts; repair bounds depend on neighboring entries treated as correct; post-processing turns accepted locations into navigable spans. Thus the map's stated contents guide decisions, rather than merely being stored. Later QA use is separately wired in RTE-8, without observed dependence.
- Condition 3 conclusion status: wired. A stated negative appearance verdict challenges a particular title/page assertion, causes candidate-location repair and can change the retained map. This is content-directed criticism of candidate content under an unchanged method. The checker may be wrong, and its explanatory `thinking` is not retained by the return path; neither caveat erases the implemented verdict-to-revision mechanism.
- Condition 4 conclusion status: wired. The current corrected TOC and remaining incorrect-item records feed subsequent repair rounds; verification results also select construction fallback. Feedback therefore shapes the next round inside one indexing run. This does not establish criticism retained across separate runs: the SDK persists the resulting map, not a reusable archive of verifier reasoning.

These four wired findings establish a narrow, batch candidate-map criticism/revision loop on the standard branch under that explicit factual-map interpretation. They supersede this report's earlier collective inapplicable assessment. They do not transfer automatically to Flash initial layout extraction or to the fixed indexing method itself. For Flash initial extraction, condition 1 is wired (localized candidate nodes), condition 2 is wired (nodes govern summaries/refinement), condition 3 is uninspected beyond the explicitly inspected optimizer checks in RTE-6, and condition 4 is uninspected for any additional content-criticism iteration; layout heuristics alone do not settle these last conditions.

Addressability: individual title/page assertions are inspectable and revisable; verifier rationale is not preserved in returned criticism records. Persistence: current candidates and error lists span repair rounds, final indexes span later invocations, but later readers receive no retained model rationale. Autonomous qualifier conclusion status: wired for the narrow standard candidate-map loop, whose internal proposal, criticism, repair and admission roles are computational once the external caller supplies source/configuration. This is not a reliability claim or an autonomous choice of problems. Learning conclusion status: uninspected at the future-answer-capacity boundary; no retained execution evidence establishes better answers or attributes improvement to criticism. Reflection conclusion status: absent within these inspected acquisition functions: the represented object is the submitted document, and the loop does not criticize or revise its own method texts. Reflective theory-builder qualifier conclusion status: absent for the same bounded method-update reason.

> self._store.save_document(
>                 doc_id, meta, remove_fields(structure, fields=["text"]), pages)
> --- `pageindex/local_api.py:172-173` @ `619cbd89f6dd02681a8cfc5d00b1f9b4848e973e`

> result = extract_toc(_validate_pdf(pdf), use_embedded_toc=use_embedded_toc)
> --- `pageindex/flash/api.py:190-190` @ `619cbd89f6dd02681a8cfc5d00b1f9b4848e973e`

> listing = json.dumps(
>             [{'title': c.get('title', ''), 'summary': c.get('summary', '')} for c in children],
>             ensure_ascii=False)
> --- `pageindex/utils.py:1003-1005` @ `619cbd89f6dd02681a8cfc5d00b1f9b4848e973e`

#### RTE-6 — Refine an already retained tree artifact

Implementation conclusion status: wired. Source: SRC-1 `pageindex/tree_optimize.py`, `pageindex/flash/api.py`.

Trigger/owner: standalone optimizer CLI accepts `--structure` and PDF; Python entry point also accepts a loaded structure or JSON path. Producer: deterministic merge plus optional model child proposals, scored by fixed worst-case page-search cost. Retained input: a tree file and source PDF, optionally a per-page headings cache. Proposed change: collapse subtrees, merge same-page frontier siblings, or expand a node into admitted subsections. Persistence/immediate return: CLI writes an optimized tree and optional decision log; Python mutates/returns the document in memory and needs caller persistence. Default CLI output is another file; original survives unless caller chooses an overlapping output path. The SDK's Flash lane runs this optimizer before RTE-5 persistence; that first-time construction branch alone would not establish retained-memory curation.

Admission: model titles must appear in normalized page text, pages must lie inside the span, ordering must not reverse, and duplicates/parent title are filtered. Candidates from the model and optional cached headings are costed; expansion requires lower cost and minimum gain. Merge keeps removed titles in `key_items`, while same-page siblings collapse to one node with the title union. This supports consolidate, dedup and evolve over retained index artifacts. It does not establish synthesis of new substantive claims or deduplication across documents.

> if normalize(title) not in normalize(pages[page - 1]):
>             continue                     # the heading must be printed on that page
> --- `pageindex/tree_optimize.py:643-644` @ `619cbd89f6dd02681a8cfc5d00b1f9b4848e973e`

> keep = cost < span and ratio >= args.min_gain_ratio
> --- `pageindex/tree_optimize.py:727-727` @ `619cbd89f6dd02681a8cfc5d00b1f9b4848e973e`

> keeper["key_items"] = titles
>             keeper["title"] = union_title(titles, keeper)
> --- `pageindex/tree_optimize.py:522-523` @ `619cbd89f6dd02681a8cfc5d00b1f9b4848e973e`

Guidance: fixed page-cost equations and a section-extraction prompt shape proposals. Assumptions include one page of routing cost and worst-branch page scanning as a proxy; numeric knobs expose these assumptions, and JSON nodes expose revision units. The optimized artifact retains the tree and key_items; optional logs retain operations, considered scores, model and ID mapping. SDK Flash keeps metrics in its intermediate result but LocalAPI saves only the selected structure/description/pages; no later chat reader of optimizer reasons is wired. Retained reasons are therefore optional diagnostic artifacts, not demonstrated later guidance.

Progression/recovery: merge and expand iterate up to three rounds by default; frozen nodes avoid reversal, and a no-change round stops. Local prompt failures can keep a node collapsed; unrecoverable provider failures abort. Structural new issues are reported, and the CLI still writes its result rather than using that list as a universal veto. Later consumer is an explicitly opted-in caller of the output artifact; no automatic SDK replacement or later QA consumption of this standalone output is shown. Delegated visibility is source page excerpts/heading proposals, not the full historical decision log. Selection predicate is fixed cost/span/heading tests; invalidation/expiry requires operator replacement/deletion. Activation is the wired artifact rewrite, with later retrieval improvement unobserved.

Decision roles and operating mode: caller-triggered batch refinement, or an automatic construction substep in Flash. The caller chooses the input tree/PDF and numeric knobs. Model and optional cached heading entries propose child sections; deterministic rules validate titles/pages/order and score candidates; controller code selects the cheapest candidate, admits qualifying expansion, decides merges and freezes nodes. Veto roles are the heading/page validators, gain rule and provider-failure handling. Structural-issue reporting is not a universal output veto. Answer-oracle access: source page text supports literal heading checks; fixed page-cost equations supply the optimization proxy. No downstream QA answer oracle or measured real model retrieval cost is consulted.

Theory-builder conditions 1–4 for the optimizer's method, individually: condition 1 conclusion status is wired (localized equations/prompts); condition 2 conclusion status is wired (they govern admission); condition 3 conclusion status is absent within the inspected route (no criticism or revision of those rules); condition 4 conclusion status is absent for criticism-driven method iteration (candidate refinement under unchanged rules does not establish it).

Candidate structural content has a separate assessment. Condition 1 conclusion status: wired, because proposed title/page entries state inspectable assertions. Condition 2 conclusion status: wired, because those assertions determine source matching, child spans and routing-cost calculation. Condition 3 conclusion status: wired for the codified rejection of a claimed heading absent from its asserted page or outside its permitted span; failed candidates lose reliance. The separate cost score selects among structures but is not by itself content criticism. Condition 4 conclusion status: absent within this inspected heading-check mechanism: rejected title assertions and criticism are not retained and returned to the proposer for the next round. Repeated cost-based merge/expand does not establish criticism-driven iteration of those rejected assertions. Model-internal criticism and reasoning remain uninspected. The standalone optimizer is therefore not established as a complete candidate theory-builder by these checks alone.

Autonomous qualifier conclusion status: inapplicable to a demonstrated complete optimizer theory-builder, which is not established here; the narrower role account does establish fully computational internal refinement after caller initiation. Learning conclusion status: uninspected at the future-QA boundary; no retained execution evidence establishes improved answer capacity, and analytic cost reduction is a proxy. Reflection conclusion status: absent for method revision in the inspected optimizer; reflective theory-builder qualifier conclusion status: absent because its method is not the object of a wired criticism/update loop.

> refined = dict(original)
>     refined["structure"] = structure
>     json.dump(refined, open(out_path, "w"), indent=2, ensure_ascii=False)
> --- `pageindex/tree_optimize.py:992-994` @ `619cbd89f6dd02681a8cfc5d00b1f9b4848e973e`

#### RTE-7 — Explicit deletion and management gating

Implementation conclusion status: wired. Source: SRC-1 `pageindex/local_store.py`, `pageindex/local_api.py`, `pageindex/agent_tools.py`, `pageindex/cloud_api.py`.

Trigger/owner: caller invokes delete by ID, or an externally configured agent receives management tools and invokes remove by names. Proposed change is removal of OBJ-3; cloud DELETE forwards the request for OBJ-4 with server semantics opaque. Admission/rejection: local safe-ID checks and existence validation; the tool validates the entire names list and maximum ten names, resolves names, then deletes individually with per-document outcomes. The local management description asks for explicit naming and confirmation, but the function does not inspect a confirmation token. Default tool registration omits management; built-in RTE-1 uses that read subset. External adapters can opt into management. This is a registration gate plus a policy instruction, not demonstrated human approval enforcement.

Immediate return/delivery: success/error or per-document results. Persistence: local marker and directory removal plus manifest update; no retained tombstone/history. Later reads stop finding the object. Curation maps to decay (forgetting), not invalidate, whose contract retains history. Rollback/recovery: no undo; surviving source PDF can be re-indexed as a new object. Delegated visibility is identifiers and outcomes, not deleted contents. Selection is exact IDs or resolved names; activation is wired deletion; deployed agent invocation is only afforded. Retention horizon ends at this operation, not age/importance thresholds.

Decision roles and operating mode: direct deletion is an externally chosen imperative operation; management-tool deletion is an agent-call affordance enabled by the caller. The caller or external agent proposes the IDs/names to remove; local validation and name resolution decide admissibility, then the store executes deletion. Validators and missing-document checks can veto; no semantic decision-maker checks whether the contents should be forgotten. The optional tool policy asks the agent to obtain human confirmation, without verifying that choice inside the delete function. Answer-oracle access is limited to object existence, argument validity and filesystem/API outcomes; there is no truth or future-utility oracle for deletion.

Guidance is the tool's deletion policy; what persists is removal, not a formulated replacement theory. Theory-builder condition 1 conclusion status: inapplicable (the command is not a candidate theory). Condition 2 conclusion status: inapplicable to theory consumption, although command arguments direct the operation. Condition 3 conclusion status: inapplicable (argument checks do not criticize a document claim). Condition 4 conclusion status: inapplicable (per-document outcomes are returned, with no criticism/revision cycle). Learning conclusion status: inapplicable to this bare deletion mechanism. Reflection conclusion status: inapplicable to method self-revision. Autonomous qualifier conclusion status: inapplicable to a theory-builder on this route; execution is computational after an external decision, and the external management agent's decision process is uninspected. No human-approval enforcement or autonomous policy for forgetting is inferred.

> if doc_dir.is_dir():
>             shutil.rmtree(doc_dir, ignore_errors=True)
>         manifest = self._read_manifest()
>         if manifest.pop(doc_id, None) is not None:
>             self._write_manifest(manifest)
> --- `pageindex/local_store.py:181-185` @ `619cbd89f6dd02681a8cfc5d00b1f9b4848e973e`

> return _READ_TOOLS + (_MANAGEMENT_TOOLS if include_management else ())
> --- `pageindex/agent_tools.py:1190-1190` @ `619cbd89f6dd02681a8cfc5d00b1f9b4848e973e`

#### RTE-8 — Pull discovery, outlines and page content

Implementation conclusion status: wired. External caller usage conclusion status: afforded. Source: SRC-1 `pageindex/agent_tools.py`, `pageindex/local_api.py`, `pageindex/local_chat.py`, `pageindex/integrations/openai_agents.py`, `pageindex/integrations/anthropic_sdk.py`.

Trigger: a model in enclosing RTE-1 requests browse/metadata/outline/page tools; direct SDK callers can request tree/OCR/metadata. Selector/producer: local implementations resolve exact document name within any transient allowed-ID scope, then requested part or page ranges. Retained inputs: OBJ-3. Persistence: this read makes no content write; manifest repair is a cache effect. Delivery/immediate return is a JSON tool result, converted through SDK adapters to model tool content; direct APIs return structured data. Later consumer is the answer model or explicit caller. Knowledge force belongs to page content, routing force to tree summaries/structure and page spans, ranking force to metadata timestamps ordering discovery. These are wired delivery and selection paths, not demonstrated answer dependence.

Local browse is newest-first and paginated (tool limit clamped to 1–50); a requested query/relevance sort is rejected. Outline reads use the stored tree without text, normalize its structure, and paginate at a nominal 95,000-character payload budget. Page reads fetch stored page OCR and select requested page numbers; at least the first selected page is returned even if oversized, so the budget is soft. Omitted pages receive follow-up guidance. Direct get_tree can reconstruct all node text from stored pages; its wire shape changes page-span fields, unlike raw_tree used by local tools. No embedding index or semantic ranker is implemented in these inspected local calls.

> metas = sorted(self._store.list_metas(), key=lambda m: m.get("id") or "")
>         metas.sort(key=lambda m: m.get("createdAt") or "", reverse=True)
> --- `pageindex/local_api.py:372-373` @ `619cbd89f6dd02681a8cfc5d00b1f9b4848e973e`

> "Relevance ranking is not supported in local mode yet — use "
>             "the default time sort.", None,
> --- `pageindex/agent_tools.py:742-743` @ `619cbd89f6dd02681a8cfc5d00b1f9b4848e973e`

> formatted = _format_structure(tree)
>     chunks = _split_structure(formatted, _CHAR_BUDGET)
> --- `pageindex/agent_tools.py:957-958` @ `619cbd89f6dd02681a8cfc5d00b1f9b4848e973e`

> if not included or budget - size >= 0:
>             content.append(entry)
>             included.append(page)
>             budget -= size
>         else:
>             remaining.append(page)
> --- `pageindex/agent_tools.py:1087-1092` @ `619cbd89f6dd02681a8cfc5d00b1f9b4848e973e`

Delegated visibility is the requested discovery window, outline part or pages; a model need not see the whole library/content. The instruction to inspect structure first for documents over 20 pages is policy, not a code prerequisite in get_page_content. Selection is a response to a consumer request: reasoning by the requesting model does not turn it into push. The document's deletion is the invalidation boundary; no session cache guarantees continued availability. Fixed tool guidance is not accumulated memory and is excluded from the authority axis. No claim of content trust or citation correctness follows from JSON validation.

#### RTE-9 — Push retained targeting metadata before chat

Implementation conclusion status: wired. Source: SRC-1 `pageindex/agent_tools.py`, `pageindex/local_chat.py`.

Trigger/owner: built-in chat starts with caller-provided doc_id and/or cloud folder_id. Selector input is those IDs, not model judgment. Selected retained parts: fetched document metadata (including generated description and caller metadata) and, for a non-root cloud folder, the exact matching folder's name/ID/description. Missing documents/folder fail. Producer renders the metadata with a fixed directive to use the named documents/folder. Delivery: a leading user-role message before supplied conversation in chat-completions, Responses and Messages lanes. This is automatic supply to the answer model without its request. Separate direct document_context calls return the same block on request; that afforded caller route is pull.

> for one_id in doc_ids:
>         try:
>             details.append(client.get_document(one_id))
> --- `pageindex/agent_tools.py:1710-1712` @ `619cbd89f6dd02681a8cfc5d00b1f9b4848e973e`

> folders = client.list_folders().get("folders") or []
>     folder = next((f for f in folders if f.get("id") == folder_id), None)
> --- `pageindex/agent_tools.py:1754-1755` @ `619cbd89f6dd02681a8cfc5d00b1f9b4848e973e`

> block = targeting_block(client, doc_id, folder_id)
>     items = ([{"role": "user", "content": block}] if block else []) + history
> --- `pageindex/local_chat.py:646-647` @ `619cbd89f6dd02681a8cfc5d00b1f9b4848e973e`

Persistence is in OBJ-3/OBJ-4; rendered message is current-call state. Metadata has knowledge/navigation relevance, while surrounding instruction is fixed wrapper text rather than a learned instruction. The match warrants identifier push, even though an upstream operator determines the identifier. Root/empty folder triggers no folder block, and omitted doc_id triggers no document block: there is no unrequested full-library dump. There is no explicit character budget for the targeting block in these functions. Delegated visibility includes complete returned document metadata, or the selected folder fields; page contents are not automatically supplied. Expiry follows the source object on later calls. Activation/answer effect is unobserved; local transient tool allowlists constrain available documents separately, while cloud targeting is not proof of server access restriction.

#### RTE-10 — Replay caller-held raw conversation

Implementation conclusion status: wired. Cross-invocation retention conclusion status: afforded. Source: SRC-1 `pageindex/local_chat.py`, SRC-2 `pageindex/client.py`.

Trigger: caller passes previous messages/items as the next chat input. Producer/selector: caller retains and appends history; SDK accepts those supplied items, adds current targeting, and gives them to the same enclosing RTE-1 consumers. Immediate return: new Responses transcript items or Messages sequence; chat-completions provides its simpler text/history surface. Persistence: only supplied/returned in-memory values are established; caller must close the retention loop. There is no automatic history fetch selector, history store, or derived continuation summary in these local paths. Thus replay is not another local push selector over an SDK store. Consumer knowledge/context authority is afforded across calls; any system/developer content supplied by the caller remains a separate explicit input channel, not discovered memory.

> transcript = result.to_input_list()[len(items):]
>         return envelope(transcript, result.raw_responses)
> --- `pageindex/local_chat.py:1133-1134` @ `619cbd89f6dd02681a8cfc5d00b1f9b4848e973e`

Native Responses preserves executed tool outputs in `items` even though `output` omits them. Messages captures tool-runner history and removes unexecuted tool_use blocks from appendable history; this is protocol reconstruction, not summary learning. Provider cache keys/marks route a stable supplied prefix and newest message; they do not retrieve hidden conversation history on behalf of an absent caller. The cache's service-side representation, persistence duration and implementation are excluded provider internals. No learned parameters or automatic trace-fed derived durable write is established. Selection predicate is caller-provided list order, budget is provider context plus the enclosing turn/output controls, and expiry is caller disposal. Delegated visibility is supplied history; effect beyond delivery is unobserved.

#### RTE-11 — Cloud reads and external model adapters

Implementation conclusion status: wired. External-agent use conclusion status: afforded. Source: SRC-1 `pageindex/cloud_api.py`, `pageindex/agent_tools.py`, `pageindex/integrations/openai_agents.py`, `pageindex/integrations/anthropic_sdk.py`, `pageindex/integrations/claude_agent_sdk.py`.

Trigger: explicit SDK read/retrieval/chat call or a model tool invocation. Input is OBJ-4 by document/retrieval/folder identity and query. Cloud REST returns JSON and accepts upload/delete/folder creation; retrieval submission produces an ID used for polling. Its internal selection and write pipeline are opaque. Own-model chat discovers live MCP schemas/instructions and routes tool invocations through the bridge. The default cloud endpoint is read-gated; management is caller opt-in. Do not equate that client endpoint choice with demonstrated deployment authorization.

> return [(str(meta.get("name") or "tool"),
>                  meta.get("description") or "",
>                  copy.deepcopy(meta.get("inputSchema"))
>                  or {"type": "object", "properties": {}},
>                  _bridge_invoker(bridge, str(meta.get("name") or "tool"),
>                                  meta.get("inputSchema") or {}))
>                 for meta in tools_meta]
> --- `pageindex/agent_tools.py:1539-1545` @ `619cbd89f6dd02681a8cfc5d00b1f9b4848e973e`

OpenAI tools convert native MCP results through its SDK; Anthropic tools convert every MCP content block; Claude's local adapter returns blocks unchanged and its cloud adapter returns remote MCP configuration. Plain Python functions instead render results as text and image size stubs, which cannot classify what native model consumers receive. Hosted OpenAI MCP can connect from the provider side and Claude agents can connect directly, so the Python text renderer is not the universal consumption boundary.

> content = [mcp_content(block) for block in result.content]
>             if is_error:
>                 raise ToolError(content)
>             return content
> --- `pageindex/integrations/anthropic_sdk.py:62-65` @ `619cbd89f6dd02681a8cfc5d00b1f9b4848e973e`

Delivery/later consumer: local own-model RTE-1 is wired to native tools; external agent configurations are afforded; managed cloud chat's consumer is behind the service. Immediate results are the API envelope or content blocks. Persistence, internal invalidation, budgets and automatic selectors on the hosted branch are uninspected. Visible pull requests and RTE-9 metadata push retain their positive classifications; no hidden inference-embedding/judgment selector is asserted. Admission of cloud upload/create/delete is HTTP success/failure at this boundary, with internal validation/rollback uninspected. Guidance is live service tool metadata/instructions plus SDK configuration; its dynamic update is not evidence of trace learning. Decision roles and operating mode at the inspectable boundary: external caller or tool-using agent proposes upload, folder creation or deletion; SDK argument validation can veto malformed local arguments and the HTTP/MCP response decides whether the client treats the request as successful. The service's proposal/decision/veto roles are uninspected. Direct API calls are caller-triggered operations; own-model/external-agent tool calls are request-response operations inside the consumer loop; hosted internal operating mode is uninspected. Answer-oracle access: the client sees transport status and returned service payloads, not a gold answer, a hosted verifier's inputs or an independent semantic oracle. Server admission, rollback and internal persistence remain uninspected.

Hosted theory-builder condition 1 conclusion status: uninspected (no hosted retained theory content has been established). Condition 2 conclusion status: uninspected (hosted content-dependent decision paths are not exposed). Condition 3 conclusion status: uninspected (hosted criticism/admission logic is unavailable). Condition 4 conclusion status: uninspected (hosted feedback iteration is unavailable). Learning conclusion status: uninspected; reflection conclusion status: uninspected; autonomous qualifier conclusion status: uninspected for the hosted mechanisms. Visible client automation and live schema discovery establish none of those qualifiers.

### Claims

None declared in this member. CLM-1 and CLM-2 remain source claims owned by the coordinator. The memory inspection limits blanket readings of model-free extraction, local semantic ranking and explainability without re-declaring those IDs.

### Evidenced absences

#### ABS-1 — No local automatic trace-to-derived durable memory route found

Conclusion status: absent, bounded to SRC-1 `pageindex/local_chat.py`, `pageindex/client.py`, `pageindex/local_api.py`, `pageindex/local_store.py`, `pageindex/chat_stream.py`, `pageindex/tree_optimize.py`, `pageindex/utils.py` at the reviewed commit. Searched terms included compact, session, memory, checkpoint, transcript, save and persist; inspected store writers, index/summary inputs, history preparation/return and optimization logs. The retained store write is RTE-5; the derived inputs are PDFs/indexes. RTE-6 optionally stores decision logs but no later transformation consumes those logs into behavior-shaping guidance. RTE-10 returns raw transcripts to the caller without storing or summarizing them. Those positive path accounts and their quotes support this negative; static prompts and provider cache marks are not substitute trace-write witnesses.

This rules out asserting a local automatic continuation-summary or experience-distillation route in the inspected SDK, not trace learning in excluded model/hosted internals or arbitrary applications built on these APIs. Because client-visible cloud routes are included but their internals are opaque, the aggregate trace axes remain not-determinable; no partial boolean no is asserted.

#### ABS-2 — No retained dependence-on-recall execution evidence in this pass

Conclusion status: absent, bounded to the commissioned source-only inspection and inspected SRC-2 `README.md` benchmark claims, plus implementation paths SRC-1 `pageindex/local_chat.py` and `pageindex/agent_tools.py`. This worker neither executed nor received a probe contrasting answers with and without recalled contents. Tests, claims of grounding, source references and analytic search cost are not retained evidence that answers depend on recalled information. Excluded linked benchmark repositories cannot repair this gap. The prevented conclusion is observed/causal faithfulness tested, not an assertion that PageIndex has never tested recall externally. RTE-8's wired delivery is the strongest consumer finding here.

### Behavioral-authority paths

None separately declared. RTE-8, RTE-9, RTE-10 and RTE-11 identify the actual channels, consumers, force and horizon directly.

## Write side

RTE-5 imports PDF content and automatically compiles a new local bundle. Manual metadata authoring does not turn all index generation into manual writing. Standard and Flash have materially different proposal mechanisms but converge on the same local persistence admission. Name collision avoidance is not content deduplication. Summaries are document-derived compression and description, not evidence of new synthesized claims or trace distillation.

RTE-6 is the retained-artifact maintenance route: it reads a saved index, changes its granularity, and can write a new index. Keeping key_items preserves removed titles, not all decision reasons. Optional operation logs have no wired read-back into future optimization guidance or answers. The local SDK does not expose a semantic edit/patch-document operation in the inspected API; replacing the PDF requires another submission or an out-of-band store edit, the latter outside the managed surface. RTE-7 explicitly forgets an object and retains no history for invalidate. Cloud admission is only visible at HTTP/MCP boundaries.

No local trace-to-summary-to-later-consumer chain was found. The alternative continuation forms are raw Responses items, Messages messages and caller user/assistant history; their local round-trip needs caller retention. No task, project or offline/online learning horizon can be assigned to an absent local derived write, and hosted opacity prevents system-wide negative classification (ABS-1).

## Read-back

RTE-8 returns requested source material to a concrete model consumer in RTE-1. Outline summaries support the model's page choice; the tool executes explicit requested ranges. Display guidance and citations are not demonstrated activation or benefit. RTE-9 is the distinct automatic supply: its upstream IDs match retained metadata and the chat prologue pushes it into user-role context. There is no extra coarse push classification for requested browse windows or response budgets. Local order-by-time is ranking metadata, not inferred-lexical push selection.

RTE-10 provides the caller with an appendable trace and accepts it later; caller replay is afforded, not a durable SDK session. RTE-11 preserves native content on SDK integrations while plain wrappers can render stubs. Cloud retrieval responses are requested returns; without hosted source, their internal selectors, transformations and full payload forms are unknown.

## Comparison rationale

The profile unions operative parts rather than treating tree shape as the whole memory system. Files hold the local page/tree/meta bundle and optimizer products; cloud identities warrant service-object at the client boundary; caller history supports afforded in-memory retention. Natural-language content and symbolic access structure coexist. Imported pages, compiled indexes and authored metadata all have concrete routes; none requires trace-extracted lineage.

Curation positives have specific witnesses: retained-tree collapse, same-page redundancy removal and expansion in RTE-6, plus deletion in RTE-7. First-time tree creation does not supply these classifications. Model summaries are asked to describe source contents, so synthesize is not asserted from model authorship alone. Routing/ranking concern actual navigational/index metadata consumers, while static instructions and transient doc allowlists do not inflate memory authority into instruction or enforcement.

Both pull and push are wired. The only supported automatic push signal is identifier, for document/folder metadata; model reasoning about requested tool results is not a hidden push signal. Cloud opacity leaves all open positive sets partial. The absent local trace learner does not settle the included hosted routes, so trace-learning and its dependent axes are not-determinable rather than an unsupported global no. Faithfulness needs retained execution evidence testing dependence on recall; this source-only pass supplies none (ABS-2).

## Integration issues

Proposed operative objects: OBJ-3 local document bundle/index files; OBJ-4 client-visible cloud document/folder objects; OBJ-5 caller-owned raw conversation. Proposed routes: RTE-5 local acquisition, RTE-6 retained-index refinement, RTE-7 deletion, RTE-8 requested reads, RTE-9 metadata push, RTE-10 caller replay, RTE-11 cloud/adapters. Proposed absences: ABS-1 bounded missing local trace learning; ABS-2 missing retained dependence-on-recall execution evidence. Each needs exact-token canonical mapping. No component, claim or behavioral-authority-path proposals are needed.

RTE-1 remains the enclosing chat loop and CMP-1 the configurable remote model component. The coordinator should keep their generic identity unchanged. Potential overlap with runtime findings is confined to optimizer admission and cloud adapters: use this member's retained-object/write/read facts, then annotate coordinator-owned decision-role findings without duplicate quotations. No seeded source fact required amendment. Revision of this specialist report changes the earlier RTE-5 collective inapplicable theory-builder judgment: conditions 1, 2, 3 and 4 are individually wired for the standard title/page candidate map, with the factual-map interpretation and acceptance/rationale limits stated in that record. Fixed method rules did not justify excluding candidate-content criticism. RTE-6 now separates fixed-method conditions from candidate heading criticism and its missing retained-feedback iteration. RTE-5, RTE-6, RTE-7 and RTE-11 now explicitly identify proposal/decision/veto roles, oracle access, operating mode and separate autonomy/learning/reflection findings. Six new generated classic-source quotations support consequential checking, repair admission, iteration, rationale loss and residual-error acceptance; no new record IDs or profile values were introduced.

Unresolved but nonblocking: hosted storage, derivation, selectors, trace learning and payload form are not visible; profile partial/not-determinable assessments retain that scope limit. Standalone optimized output is not automatically installed into the SDK store, so its later deployment remains afforded. Actual third-party runners and provider caches can add state or compaction, but this source pin does not expose those internals. All conclusions needed for the bounded handoff are available; no scope expansion is requested.

## Limitations and checks

The runtime did not expose an exact model identifier; worker-model is unknown. No prior-analysis exposure occurred, no source worktree was used as evidence, and no delegated or publication action was taken. No dynamic check was planned: the task establishes source wiring, while real answer dependence would require a separately authorized retained execution comparison. No observed activation, real-world accuracy, learned parameter update or hosted implementation claim is made.

Input and method hashes were recorded before analysis and rechecked unchanged after drafting. Local report validation uses `commonplace-validate --full` against this exact report; the final correction pass records its result below. Source quote blocks were generated with commonplace-quote from the frozen run state and inserted unchanged. Validation establishes structural conformance, not independence or semantic correctness of the integrated set.

Deterministic validation: `commonplace-validate --full` on this report passed cleanly (exit 0), with no warnings or failures; all fourteen axes, declared references and 29 generated quote blocks passed. Input SHA-256 remained `eb29d6220d31070e07653fd03982e1505ff83bfbd058915cd72f256e22b5285e`; method SHA-256 remained `bef249eb62e6a6af7bb822f385b5085a221a12eea0d50c1648e78b3da69889bf`.

## Amendments

Amendment: RTE-5 — The specialist corrected its preliminary collective inapplicable assessment to separate wired findings for conditions 1, 2, 3 and 4 on the standard title/page candidate map. Source: SRC-1 `pageindex/page_index_classic.py`; scope and rationale limits are those of the revised local report. This affects the narrow candidate-map theory-builder finding, not the memory-comparison profile or a learning claim.

Amendment: RTE-6 — The specialist separated criticism of candidate heading assertions from its earlier method-only assessment. Source: SRC-1 `pageindex/tree_optimize.py`; candidate conditions 1, 2 and 3 are wired, while condition 4 is absent in the inspected rejected-heading feedback mechanism. The unchanged-method assessment remains scoped to the method. This affects the theory-route interpretation, not the curation values.
