---
{
  "type": "types/agentic-system-analysis-result.md",
  "description": "Dynamic Cheatsheet whole-system runtime, memory and epistemic analysis at the pinned implementation; complete disposition",
  "run-id": "AAS-2026-09-27-dynamic-cheatsheet-03",
  "system": "Dynamic Cheatsheet",
  "run-date": "2026-09-27",
  "result-disposition": "complete",
  "target-class": "workflow",
  "boundary-kind": "whole-system",
  "reviewed-boundary": "5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9",
  "analysis-cutoff": "2026-09-27",
  "evidence-tier": "code-grounded",
  "memory-comparison": {
    "scope": "Retained cheatsheets, raw generated solutions, embedding access metadata, checkpoint/resume, all six advanced_generate branches, recursive local execution context, client conversation history, and visible native execution container reuse. Static prompt templates are producer/consumer doctrine, not learned memory. Provider payload internals and historical results are excluded, leaving opaque native memory effects explicit.",
    "axes": {
      "storage_substrate": {
        "assessment": "partial",
        "values": [
          "files",
          "in-memory",
          "service-object"
        ],
        "evidence": {
          "files": {
            "basis": "wired",
            "records": [
              "OBJ-8",
              "OBJ-9",
              "OBJ-10"
            ],
            "note": "JSONL checkpoints and embedding CSV are explicit files."
          },
          "in-memory": {
            "basis": "wired",
            "records": [
              "OBJ-7",
              "OBJ-8",
              "OBJ-9",
              "OBJ-11"
            ],
            "note": "Strings, output lists, embedding arrays and client messages persist in process."
          },
          "service-object": {
            "basis": "wired",
            "records": [
              "OBJ-6",
              "RTE-3"
            ],
            "note": "One container is created per benchmark and its ID supplied on later generator calls; contents uninspected."
          }
        },
        "records": [
          "OBJ-7",
          "OBJ-8",
          "OBJ-9",
          "OBJ-10",
          "OBJ-11",
          "OBJ-6"
        ],
        "note": "Local strings, arrays and JSONL files are wired; a reused service container is wired but its retained contents and additional substrates are opaque."
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
              "OBJ-7",
              "OBJ-8",
              "OBJ-9",
              "OBJ-10",
              "OBJ-6"
            ],
            "note": "Cheatsheet and trajectories are readable text; vector arrays and checkpoint structure are symbolic. Native container payload form remains unknown."
          },
          "symbolic": {
            "basis": "wired",
            "records": [
              "OBJ-7",
              "OBJ-8",
              "OBJ-9",
              "OBJ-10",
              "OBJ-6"
            ],
            "note": "Cheatsheet and trajectories are readable text; vector arrays and checkpoint structure are symbolic. Native container payload form remains unknown."
          }
        },
        "records": [
          "OBJ-7",
          "OBJ-8",
          "OBJ-9",
          "OBJ-10",
          "OBJ-6"
        ],
        "note": "Cheatsheet and trajectories are readable text; vector arrays and checkpoint structure are symbolic. Native container payload form remains unknown."
      },
      "lineage": {
        "assessment": "partial",
        "values": [
          "imported",
          "other-compiled",
          "trace-extracted",
          "authored"
        ],
        "evidence": {
          "imported": {
            "basis": "wired",
            "records": [
              "RTE-9",
              "OBJ-9"
            ],
            "note": "Runner imports seed text and precomputed embeddings."
          },
          "other-compiled": {
            "basis": "wired",
            "records": [
              "RTE-6",
              "RTE-7"
            ],
            "note": "Raw prior pairs are mechanically formatted into delivery text."
          },
          "trace-extracted": {
            "basis": "wired",
            "records": [
              "RTE-5",
              "RTE-8"
            ],
            "note": "Curator consumes generated solutions and produces retained cheatsheet content."
          },
          "authored": {
            "basis": "afforded",
            "records": [
              "RTE-10"
            ],
            "note": "set_history accepts caller-supplied messages, including manually authored material."
          }
        },
        "records": [
          "RTE-5",
          "RTE-6",
          "RTE-7",
          "RTE-8",
          "RTE-9",
          "RTE-10",
          "RTE-3"
        ],
        "note": "Curation extracts traces; retrieval mechanically assembles context; initial files and embeddings are imported. Caller-authored message history is afforded; native payload lineage unknown."
      },
      "behavioral_authority": {
        "assessment": "partial",
        "values": [
          "knowledge",
          "ranking"
        ],
        "evidence": {
          "knowledge": {
            "basis": "wired",
            "records": [
              "RTE-5",
              "RTE-6",
              "RTE-7",
              "RTE-8"
            ],
            "note": "Generator receives reference material and is instructed to inspect applicability and limitations."
          },
          "ranking": {
            "basis": "wired",
            "records": [
              "OBJ-9",
              "RTE-6"
            ],
            "note": "Cosine similarity orders past examples for automatic delivery."
          }
        },
        "records": [
          "RTE-5",
          "RTE-6",
          "RTE-7",
          "RTE-8",
          "RTE-10",
          "RTE-3"
        ],
        "note": "Cheatsheets and examples are advisory reference; embeddings determine similarity ranking. Native retained payload authority is unknown."
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
              "RTE-8",
              "RTE-9"
            ],
            "note": "Model output extraction, replacement and JSONL persistence run without approval."
          },
          "manual": {
            "basis": "afforded",
            "records": [
              "RTE-10"
            ],
            "note": "Caller can replace message history through set_history; no UI or reviewed editing workflow is established."
          }
        },
        "records": [
          "RTE-5",
          "RTE-8",
          "RTE-9",
          "RTE-10",
          "RTE-3"
        ],
        "note": "Curator updates and checkpoint writes are automatic. Direct message-history setting affords manual writes; provider-internal writes are not inspected."
      },
      "curation_operations": {
        "assessment": "partial",
        "values": [
          "evolve",
          "consolidate",
          "dedup",
          "synthesize",
          "promote"
        ],
        "evidence": {
          "evolve": {
            "basis": "wired",
            "records": [
              "RTE-5",
              "RTE-8"
            ],
            "note": "Existing cheatsheet is passed into curator and replaced by extracted result."
          },
          "consolidate": {
            "basis": "afforded",
            "records": [
              "CLM-3"
            ],
            "note": "Prompt directs concise retention and omission of redundant or trivial material."
          },
          "dedup": {
            "basis": "afforded",
            "records": [
              "CLM-3"
            ],
            "note": "Prompt directs removal of duplicate entries; no deterministic entry matcher."
          },
          "synthesize": {
            "basis": "afforded",
            "records": [
              "CLM-3"
            ],
            "note": "Prompt directs new meta-strategies from problem-solving experience; novelty not observed."
          },
          "promote": {
            "basis": "afforded",
            "records": [
              "CLM-3"
            ],
            "note": "Prompt asks usage counts to prioritize frequently used strategies; no independent counter enforcement."
          }
        },
        "records": [
          "RTE-5",
          "RTE-8",
          "CLM-3",
          "RTE-3"
        ],
        "note": "Whole-cheatsheet revision is wired. Prompt-directed consolidation, duplicate removal, new strategies and usage-based priority are afforded; execution compliance and native payload curation remain unverified."
      },
      "read_back_direction": {
        "assessment": "partial",
        "values": [
          "push"
        ],
        "evidence": {
          "push": {
            "basis": "wired",
            "records": [
              "RTE-5",
              "RTE-6",
              "RTE-7",
              "RTE-8",
              "RTE-10",
              "RTE-3"
            ],
            "note": "Runner automatically supplies memory to generator and curator; client chat automatically appends history. Native container retrieval direction is unresolved; get_history alone is a storage capability."
          }
        },
        "records": [
          "RTE-5",
          "RTE-6",
          "RTE-7",
          "RTE-8",
          "RTE-10",
          "RTE-3"
        ],
        "note": "Runner automatically supplies memory to generator and curator; client chat automatically appends history. Native container retrieval direction is unresolved; get_history alone is a storage capability."
      },
      "read_back_signal": {
        "assessment": "partial",
        "values": [
          "coarse",
          "inferred-embedding",
          "inferred-judgment"
        ],
        "evidence": {
          "coarse": {
            "basis": "wired",
            "records": [
              "RTE-5",
              "RTE-7",
              "RTE-10"
            ],
            "note": "Current sheet or all retained history is supplied on each call."
          },
          "inferred-embedding": {
            "basis": "wired",
            "records": [
              "RTE-6"
            ],
            "note": "Current input embedding ranks previous inputs and selects associated outputs."
          },
          "inferred-judgment": {
            "basis": "wired",
            "records": [
              "RTE-8"
            ],
            "note": "Curator receives next question, previous sheet and retrieved pairs, then selects material for generator context."
          }
        },
        "records": [
          "RTE-5",
          "RTE-6",
          "RTE-7",
          "RTE-8",
          "RTE-10",
          "RTE-3"
        ],
        "note": "Whole-sheet/history supply is coarse; cosine ranking targets examples; curator judges relevant retained material against next input. Native selector is unknown."
      },
      "trace_learning": {
        "assessment": "known",
        "values": [
          "yes"
        ],
        "evidence": {
          "yes": {
            "basis": "wired",
            "records": [
              "RTE-5",
              "RTE-8",
              "RTE-9"
            ],
            "note": "Automatic trace-fed cheatsheet production, cross-query delivery and file persistence establish yes regardless of opaque additional routes."
          }
        },
        "records": [
          "RTE-5",
          "RTE-8",
          "RTE-9"
        ],
        "note": "Automatic trace-fed cheatsheet production, cross-query delivery and file persistence establish yes regardless of opaque additional routes."
      },
      "trace_source": {
        "assessment": "partial",
        "values": [
          "trajectories",
          "tool-traces"
        ],
        "evidence": {
          "trajectories": {
            "basis": "wired",
            "records": [
              "RTE-5",
              "RTE-8"
            ],
            "note": "Problem-solving answers and rationale are curator input."
          },
          "tool-traces": {
            "basis": "wired",
            "records": [
              "RTE-2",
              "RTE-5"
            ],
            "note": "Local execution result is accumulated into generator_output, which cumulative curator reads."
          }
        },
        "records": [
          "RTE-5",
          "RTE-8",
          "RTE-2",
          "RTE-3"
        ],
        "note": "Generator solutions feed curation; local execution output is embedded in those solutions. Native execution details beyond returned text are opaque."
      },
      "learning_scope": {
        "assessment": "partial",
        "values": [
          "per-task",
          "cross-task"
        ],
        "evidence": {
          "per-task": {
            "basis": "wired",
            "records": [
              "RTE-5"
            ],
            "note": "max_num_rounds repeats one input with successive sheets."
          },
          "cross-task": {
            "basis": "wired",
            "records": [
              "RTE-5",
              "RTE-8",
              "RTE-9"
            ],
            "note": "Distinct benchmark questions consume earlier retained sheets; task means an individual problem, not a dataset label."
          }
        },
        "records": [
          "RTE-5",
          "RTE-8",
          "RTE-9",
          "RTE-3"
        ],
        "note": "Cumulative multi-round refinement reuses memory for one problem; runner and README pass it across independent problems. Additional native learning horizon unknown."
      },
      "learning_timing": {
        "assessment": "partial",
        "values": [
          "online"
        ],
        "evidence": {
          "online": {
            "basis": "wired",
            "records": [
              "RTE-5",
              "RTE-8",
              "RTE-3"
            ],
            "note": "Curator updates interleave with inference, before or after answers. No offline training claim follows from imported embeddings; native internals unknown."
          }
        },
        "records": [
          "RTE-5",
          "RTE-8",
          "RTE-3"
        ],
        "note": "Curator updates interleave with inference, before or after answers. No offline training claim follows from imported embeddings; native internals unknown."
      },
      "distilled_form": {
        "assessment": "partial",
        "values": [
          "natural-language",
          "symbolic"
        ],
        "evidence": {
          "natural-language": {
            "basis": "wired",
            "records": [
              "OBJ-7",
              "RTE-5",
              "RTE-8"
            ],
            "note": "Curator response is extracted and retained as readable cheatsheet text."
          },
          "symbolic": {
            "basis": "afforded",
            "records": [
              "CLM-3"
            ],
            "note": "Curator asks for reusable executable code; concrete generated payloads are excluded from inspection."
          }
        },
        "records": [
          "OBJ-7",
          "CLM-3",
          "RTE-5",
          "RTE-8",
          "RTE-3"
        ],
        "note": "Textual strategies are wired outputs; code snippets are explicitly afforded by curator and generator instructions. Native derivation forms remain unknown."
      },
      "faithfulness_tested": {
        "assessment": "not-determinable",
        "values": [],
        "evidence": {},
        "records": [
          "CLM-2"
        ],
        "note": "No retained executions were admitted. README accuracy claims and benchmark evaluation code do not test dependence on recalled content; excluded historical payloads prevent a global negative."
      }
    }
  }
}
---

# Dynamic Cheatsheet agentic-system analysis

## Run identity

**Run state:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-27-dynamic-cheatsheet-03/run-state.md`

**Generated review:** `kb/agentic-systems/reviews/dynamic-cheatsheet.md`

**Memory analysis report:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-27-dynamic-cheatsheet-03/memory-report.md`
**Memory analysis report SHA-256:** `7c022851affb0d699e15c501da7e45a81570800e4cdb7ba2ad57dc336ae7ae23`

Run AAS-2026-09-27-dynamic-cheatsheet-03; intended destinations above do not themselves declare publication. Coordinator exact model identity: unknown; commissioned specialist selection: gpt-6-astra, actual worker-reported model identity unknown. Trace locations unavailable.

## Boundary and evidence

Evidence basis: commit-addressed Python implementation and shipped prompt/README text at `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`, inspected on 2026-09-27; no target execution or historical result analysis. This is a whole-system analysis of the Dynamic Cheatsheet workflow/runtime client, intended to establish its implemented responsibilities and the warrant of its adaptive-memory claims. It includes the benchmark entry point, all six `advanced_generate` approaches, local code execution, selected provider adapters and native code tools, prompt templates, answer extraction, task evaluation, and the separate documented client-history API. The latter is afforded to direct client callers, not a hidden benchmark memory channel. The enclosing human chooses task, model, templates and capability flags; scheduling inside a run is sequential Python control flow.

External model reasoning and provider execution internals are excluded: their opacity prevents verified criticism, activation, weight-fixity and isolation conclusions. Live datasets, paper contents and historical result payloads are excluded: reported gains remain attributed claims. Generic web-search convenience APIs not called by the selected LanguageModel entry path, notebook execution, unused evaluators and standalone legacy judging utilities are not operationally traced; this prevents claims about every possible direct use of the vendored client, not coverage of the six shipped approach branches. The separate client-history route includes its automatic conversation assembly; optional web-search acquisition through that client is unassessed and is excluded from the memory profile’s write/content claims. No source worktree or current HEAD supplied evidence. Dependencies include Python, provider SDKs and credentials, numerical/tokenizer/data libraries, local datasets or the remotely loaded GameOf24 dataset, and precomputed embeddings for retrieval approaches. Actual installed versions and credentials were not inspected.

## Source register

| Source ID | Kind | Identity/location | Revision | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | Git | `https://github.com/suzgunmirac/dynamic-cheatsheet`; access root `/home/zby/llm/commonplace/related-systems/suzgunmirac--dynamic-cheatsheet` | `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9` | Implementation: Python; doctrine/design: prompt templates; reported operation: README performance bullets | `run_benchmark.py`, `dynamic_cheatsheet/language_model.py`, `dynamic_cheatsheet/utils/execute_code.py`, `dynamic_cheatsheet/utils/extractor.py`, task-used branches of `dynamic_cheatsheet/utils/evaluation.py`, selected initialization/message-provider/code-tool and chat/history routes in `text_generation/simple_unified_client.py`, `prompts/generator_prompt.txt`, both `prompts/curator_prompt_for_dc_cumulative.txt` and `prompts/curator_prompt_for_dc_retrieval_synthesis.txt`, `README.md`; specialist additionally inspected source cells only in `ExampleUsage.ipynb` | Generated quotations below bind full source paths and commit; [repository at pin](https://github.com/suzgunmirac/dynamic-cheatsheet/tree/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9) | No observed target run or causal experiment. External providers, live data, paper and historical result payloads cannot support stronger conclusions. |

## Shared records

### Components

### CMP-1 — Generator and curator language model

One `LanguageModel` instance supplies both roles, with the same provider/model selection and extra API parameters. Representational form: distributed-parametric; substrate: external provider service or configured local Ollama endpoint. Endpoint selection conclusion status: wired; exact parameter-version pinning conclusion status: uninspected. A model-name string, even one containing a date, is not inspected weight identity. Inference-only operation conclusion status: wired for the inspected request/curation call paths; provider-side parameter changes remain uninspected. Generator and curator are successive calls, not independently scheduled agents. Evidence: SRC-1 `dynamic_cheatsheet/language_model.py` and `text_generation/simple_unified_client.py`.

> client_kwargs = {"provider": provider, "model": model_id, "max_retries": 3, "retry_delay": 10}
> --- `dynamic_cheatsheet/language_model.py:91-91` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

### CMP-2 — Precomputed embedding producer

The runtime imports input/embedding rows, then computes cosine similarity locally; it issues no embedding-generation call on the inspected benchmark path. Representational form of the producing model and exact producer identity: uninspected. The shipped vector values are numerical access data, not runtime-updated model parameters. Consequently neither a fixed embedding model nor an online parametric learning component is established. Evidence: SRC-1 `run_benchmark.py`, `dynamic_cheatsheet/language_model.py`; memory route records below retain selection evidence.

### Operative objects

### OBJ-1 — Current problem and expected target

The problem is natural-language input, retained in memory and benchmark JSONL; a supplied dataset target is a separate oracle field stored with that input. The generator receives the current question, not the `target` field. The benchmark evaluator receives the target after generation for applicable tasks. Acquisition conclusion status: wired. Source warrant of dataset targets: uninspected. Evidence: SRC-1 `run_benchmark.py`.

### OBJ-2 — Generator solution and extracted answer

Natural-language reasoning can contain symbolic Python; answer extraction produces a string. In-memory output and subsequent checkpoint fields retain the text. The wrapper returns `final_output`, `final_answer`, steps and branch-specific memory. Extraction is a formatting operation, not semantic acceptance. Implementation conclusion status: wired. Evidence: SRC-1 `dynamic_cheatsheet/language_model.py`, `dynamic_cheatsheet/utils/extractor.py`.

> txt = response.split("<answer>")[-1].strip()
>             txt = txt.split("</answer>")[0].strip()
> --- `dynamic_cheatsheet/utils/extractor.py:27-28` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

### OBJ-3 — Shipped generator and curator instructions

Authored natural-language files are static guidance, not accumulated memory. The generator is told to use references, explain reasoning and inspect limitations. Curator instructions ask for correctness assessment, reusable strategies, examples, assumptions and usage counts. They prescribe how to rewrite retained memory but are not themselves revised by the inspected workflow. Instruction delivery conclusion status: wired; compliance conclusion status: uninspected. Evidence: SRC-1 all three `prompts/` files.

See OBJ-7 for the retained generator-use excerpt.

> Before updating the cheatsheet, however, you should first assess the correctness of the provided solution and strategically incorporate code blocks, insights, and solutions into the new cheatsheet. Always aim to preserve and keep correct, useful, and illustrative solutions and strategies for future cheatsheets.
> --- `prompts/curator_prompt_for_dc_cumulative.txt:18-18` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

> - If a better approach than a previously recorded one is found, replace the old version.
> --- `prompts/curator_prompt_for_dc_retrieval_synthesis.txt:44-44` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

### OBJ-4 — Local code execution feedback

Extracted Python is symbolic code in a temporary file. The utility returns text containing stdout, stderr-derived error, timeout notice or no-output notice; the generator receives that text as conversational context. It supplies evidence of executing that program, not a certification of its model, assumptions or solution. Implementation conclusion status: wired. Evidence: SRC-1 `dynamic_cheatsheet/utils/execute_code.py`, `dynamic_cheatsheet/language_model.py`.

### OBJ-5 — Benchmark correctness result

Boolean result and scalar counters held in memory and printed after generation. Expected dataset answers or task constraints define its domain; no computed result field is added to each checkpoint record. This scores answers, not cheatsheet claims or provenance. Implementation conclusion status: wired. Evidence: SRC-1 `run_benchmark.py`, `dynamic_cheatsheet/utils/evaluation.py`.

### OBJ-6 — Provider code-execution handle

OpenAI container identifier is symbolic service access state on the wrapper instance; Claude uses a sentinel enabling a per-request native tool. The benchmark creates it once when requested. Server contents, continuation semantics and expiry are uninspected. The JSONL resume route does not restore this handle. Implementation conclusion status: wired; deployed isolation conclusion status: uninspected. Evidence: SRC-1 `dynamic_cheatsheet/language_model.py`, `text_generation/simple_unified_client.py`.

Specialist integration on OBJ-6: 
One OpenAI container ID is created per benchmark run and repeatedly supplied to generator requests. The object is a service container; its actual retained files/state, duration and later accesses are opaque within source access. Claude uses a sentinel and per-call native tool enablement, not the same explicit reused server-container handle. Curator calls do not enable native execution. Evidence: SRC-1 `run_benchmark.py`, `dynamic_cheatsheet/language_model.py`, `text_generation/simple_unified_client.py`.

> "tools": [{"type": "code_interpreter", "container": container_id}],
> --- `text_generation/simple_unified_client.py:1131-1131` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

### OBJ-7 — Cheatsheet text

Derived, behavior-shaping natural-language reference, optionally containing symbolic code, retained in a Python string and checkpoint fields. The generator and curator consume its readable content, not a separate summary. Advisory knowledge authority; a strategy in imperative wording is still supplied as reference, not enforced. Whole-sheet replacement gives the model freedom to revise or discard entries without stable identifiers. Evidence: SRC-1 `dynamic_cheatsheet/language_model.py`, `prompts/generator_prompt.txt`.

> - Carefully analyze both the question and cheatsheet before starting
> - Search for and identify any applicable patterns, strategies, or examples within the cheatsheet
> --- `prompts/generator_prompt.txt:11-12` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

### OBJ-8 — Generated solution history

Raw per-problem trajectories in `generator_outputs_so_far`, with question texts supplied from the corpus. These can include reasoning, code and local tool output. Lists live in memory; final outputs and richer steps are saved in JSONL. Cumulative curation consumes the current trajectory, retrieval and full-history routes consume prior trajectories. Scores are not a separately retained learning input. Evidence: SRC-1 `run_benchmark.py`, `dynamic_cheatsheet/language_model.py`.

> generator_outputs_so_far.append(output_dict["final_output"])
> 
>         outputs.append({
>             "input": current_input,
>             "target": original_target,
>             "raw_input": original_input,
>             **output_dict,
>         })
>         cheatsheet = output_dict["final_cheatsheet"]
> --- `run_benchmark.py:272-280` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

### OBJ-9 — Input embeddings and corpus alignment

Imported CSV embeddings become a numeric NumPy array, with question text used to reorder rows into dataset order. This is symbolic access metadata for ranking rather than a vector database or learned model-weight update. Embeddings are not generated during the inspected run. Evidence: SRC-1 `run_benchmark.py`.

> df = pd.read_csv(embeddings_path)
>         questions = df["input"].tolist()
>         embeddings = df["embedding"].apply(ast.literal_eval)
>         embeddings = np.array(embeddings.tolist())  # (N, embedding_dim)
> --- `run_benchmark.py:211-214` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

### OBJ-10 — Benchmark checkpoint and parameter files

JSONL keeps current/final sheets, raw outputs, answer fields and step records; a parameter JSON keeps run arguments, including loaded templates. After every example the complete output list is rewritten for recovery. Later resume reads `final_cheatsheet` and `final_output`; earlier saved sheets are history, not an automatic rollback mechanism. Evidence: SRC-1 `run_benchmark.py`; quoted resume route RTE-9.

### OBJ-11 — In-process conversation history

The provider client exposes a mutable message list through chat, set_history, get_history and reset_history. Text content is conversational evidence; role structure is symbolic metadata. Separate from benchmark checkpoints. LanguageModel calls `generate_from_messages`, which does not use this client's history management. Evidence: SRC-1 `text_generation/simple_unified_client.py`.


### Routes

### RTE-1 — Generate and return a problem solution

Trigger/principal: external caller invokes `advanced_generate`, or the benchmark loop invokes it for the next item. Python selects a named approach; CMP-1 selects response content under OBJ-3 plus the assembled question/memory. The ordinary baseline has one user message, calls the provider, extracts OBJ-2 and returns the result dictionary. Other approaches attach memory routes below; curator writes are separate from answer generation. `max_num_rounds` repeats only the cumulative branch; the hybrid branch is one generator/curator cycle. Owner: synchronous wrapper. Effects: provider request, potential RTE-2 or RTE-3, returned answer. Product admission: extraction of a final-answer string, with a placeholder on extraction failure; no correctness veto. Guidance: static problem-solving instructions and dynamic strategies; parameters do not change locally. Recovery: empty provider response becomes placeholder text; provider errors are retried then raised, rather than silently replaced with a correct answer. Human intervention is configuration or external rerun, not a required per-answer approval.

Immediate return: structured result. Later read-back: stored output can enter the memory routes; bare baseline generation does not itself maintain cross-call history. Delegated visibility: provider sees supplied messages, not automatic filesystem access. Selector: approach name; no expiry or invalidation on answer text. Activation/effect: request and return are wired; any benefit attributable to memory is uninspected. Guarantee owner/enforcement: Python branch and extractor; strength: protocol for formatting, no claimed semantic guarantee. External contract: API availability and response shape. Evidence: SRC-1 `dynamic_cheatsheet/language_model.py`, `text_generation/simple_unified_client.py`, `dynamic_cheatsheet/utils/extractor.py`.

> for attempt in range(self.max_retries):
>             try:
>                 return func(*args, **kwargs)
> --- `text_generation/simple_unified_client.py:412-414` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

### RTE-2 — Execute generated Python locally and ask for continuation

Trigger: generated text contains the execution flag after a fenced block and `allow_code_execution` is true. The generator proposes code; wrapper syntax/flag checks decide execution; the OS executes `python3` with inherited process privileges. There is no per-snippet human veto on this path. Local helper rewrites an eligible final line as `print(...)`, executes with a three-second default timeout, kills the immediate process on timeout, removes its temporary file, and returns feedback OBJ-4. The wrapper adds assistant/user messages and recursively calls CMP-1. The `current_depth <= max_depth_num_rounds` check occurs after execution: with default starting depth one and maximum three, a fourth flagged output can still execute before return. At that final branch accumulated text also duplicates the just-executed block. The warning to stop execution is a prompt policy, not an execution cap.

Immediate return: feedback then accumulated generator output. Persistence: conversation within one invocation; complete output can later enter memory. Delegated visibility: subprocess inherits environment and filesystem permissions; exact deployed restrictions uninspected. Selection: first Python block extracted from pre-flag text, not a proof or approval check. No reusable invalidation mechanism applies to executed effects; temporary-file deletion does not undo them. Activation/effect conclusion status: wired; process isolation is not established by timeout. Guarantee owner/enforcement: helper timeout; strength: best effort runtime bound on immediate process, not a sandbox or descendant cleanup contract. Required external contract: OS/process permissions and installed Python/packages. Guidance is OBJ-3's static execution protocol and the model-generated program; code is a proposed work product, not an automatically installed runtime revision. Criticism can be formulated after errors in model continuation, but no observed criticism or improved capacity is established. Evidence: SRC-1 `dynamic_cheatsheet/language_model.py`, `dynamic_cheatsheet/utils/execute_code.py`.

> process = Popen(["python3", temp_file.name], stdout=PIPE, stderr=PIPE)
>         stdout, stderr = process.communicate(timeout=timeout)
> --- `dynamic_cheatsheet/utils/execute_code.py:83-84` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

> if current_depth <= max_depth_num_rounds:
>                     warning_txt = ""
> --- `dynamic_cheatsheet/language_model.py:264-265` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

Memory-specific continuation on RTE-2: 
Implementation conclusion status: wired. Local flagged code execution appends execution output to generated text and conversation, then recursively continues generation up to the configured depth rule. That accumulated final output feeds the curator and checkpoint. Thus tool-traces join trajectories on the trace-learning source axis. The temporary history alone is context retention, not distilled learning. Native execution returns text through a distinct provider path; unreturned tool payloads are not available to the curator. Evidence: SRC-1 `dynamic_cheatsheet/language_model.py`.

> current_output = f"{output_prefix}\n{code_execution_flag}\n\n{executed_code}"
>                 final_output = f"{final_output}\n\n{current_output}".strip()
> --- `dynamic_cheatsheet/language_model.py:260-261` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

### RTE-3 — Delegate code execution to a provider tool

Trigger: caller chooses interpreter mode and a container/sentinel exists. `advanced_generate` disables the local subprocess path, then `generate` calls the OpenAI Responses code-interpreter tool or Claude native execution tool. Python selects the provider branch; provider/model controls execution inside that service. Return: extracted provider text, with placeholder on empty response. Persistence: OpenAI handle reused by the wrapper across benchmark questions; Claude sentinel enables tools but does not itself prove cross-call sandbox continuity. Read-back of hidden server state, exact execution feedback preservation and expiry are uninspected; visible returned text can feed memory. Grant set: explicitly supplied code tool; provider internals and arbitrary extra kwargs are external configuration, not a uniform isolation guarantee. Failure: retry wrapper raises after exhaustion; no local rollback of remote effects. Guarantee strength: protocol for choosing the local-versus-native route; provider isolation is an external contract, not verified deployment evidence. If interpreter mode is requested without a handle through direct API use, local execution is disabled but the native branch is not entered. Evidence and implementation conclusion status: wired, SRC-1 `dynamic_cheatsheet/language_model.py`, `text_generation/simple_unified_client.py`.

> if use_code_interpreter:
>             allow_code_execution = False
> --- `dynamic_cheatsheet/language_model.py:348-349` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

See OBJ-6 for the retained tool request excerpt.

> code_execution_tool = {"type": "code_execution_20250825", "name": "code_execution"}
> --- `text_generation/simple_unified_client.py:1191-1191` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

Memory-specific native reuse on RTE-3: 
Implementation conclusion status: wired. Operator enables code interpreter; runner creates a container; generator supplies its ID to Responses calls for subsequent problems. Explicit local tool execution is disabled for that path. The supplied ID proves reuse of an execution resource; it does not prove which payload persists, whether a later model requests stored content, or a particular memory influence. Classifications retain the visible service-object and leave provider-internal memory operations unresolved. Evidence: SRC-1 `run_benchmark.py`, `dynamic_cheatsheet/language_model.py`, `text_generation/simple_unified_client.py`; quote on object OBJ-6.

### RTE-4 — Score completed benchmark answers

Trigger: benchmark has already generated an answer and adopted its returned cheatsheet. Python selects the task evaluator. Answer oracle: dataset target for AIME, GPQA, MMLU and equation balancing; GameOf24 uses the input numbers plus value-24/rule checks. The dataset/provider of reference answers is external to generation; source truth of those labels is uninspected. Matching/format heuristics or arithmetic execution yield OBJ-5, update printed counters, and the loop saves output. The result has no veto over memory adoption and is not passed into the next curator call. The reference target is stored in the checkpoint, but resumed memory uses final output/cheatsheet rather than that target. The evaluation helper itself uses Python `eval` on answer expressions for GameOf24 and equation balancing; disabling generation-time code execution does not disable this separate evaluator path.

Immediate return: boolean and printed aggregate. Later read-back: no score consumption into generation on inspected path; raw target remains available in checkpoint. Delegated visibility: local evaluator sees answer/target; external model does not receive the target through these call arguments. Selector: task name. No expiry or invalidation of memory follows a failed score. Effect: counters and output, not epistemic acceptance of strategies. Guarantee owner/enforcement: evaluator; strength: task-specific heuristic/check, with uninspected runtime outcomes; no process or memory correctness guarantee. Admission/revision of memory: inapplicable to this route; product judgment does not become selection of a successor cheatsheet. Evidence and implementation conclusion status: wired, SRC-1 `run_benchmark.py`, `dynamic_cheatsheet/utils/evaluation.py`.

See OBJ-8 for the retained assignment-before-evaluation excerpt.

> if result:
>             correct_so_far += 1
>         total_so_far += 1
> --- `run_benchmark.py:301-303` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

> value = eval(clean_output)
>         if not (abs(value - 24) < 1e-3):
>             return False
> --- `dynamic_cheatsheet/utils/evaluation.py:60-62` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

### RTE-5 — Cumulative update and replay

Implementation conclusion status: wired. Trigger: each input, and each configured refinement round on that input. The generator receives the entire existing sheet. A second call receives question, full generator output and old sheet through the curator template. Extracted new text replaces the string; the next round or next benchmark question receives it. With multiple rounds, earlier answers can additionally be appended to generator context. Persistence is in-memory immediately and through runner JSONL after the example. This is online trace learning at both per-task and cross-task horizons. No approval; extraction fallback retains the previous sheet. Missing content is withdrawn from the active sheet but no invalidation ledger is maintained. Evidence: SRC-1 `dynamic_cheatsheet/language_model.py`, `run_benchmark.py`.

> new_cheatsheet = extract_cheatsheet(response=cheatsheet_output, old_cheatsheet=current_cheatsheet)
>                 cheatsheet = new_cheatsheet
> --- `dynamic_cheatsheet/language_model.py:434-435` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

The hybrid `DynamicCheatsheet_CumulativeRetrieval` branch adds selected prior pairs to the generator sheet, then applies the same post-answer curator update. Its code does one generator/curator pair and does not iterate `max_num_rounds`; it therefore does not inherit the cumulative branch's multi-round behavior merely from its name. Curator sees the generator output and current sheet, not the raw retrieved section as a separate template input.

Owner and executor: sequential Python plus CMP-1. Immediate return is answer and replacement sheet; later generator/curator sees the retained sheet. Selection is whole-sheet supply. No expiry; omission on rewrite removes active content. Model proposes and judges according to OBJ-3; extractor admits and can only fall back on formatting failure, not veto an unsound strategy. Guarantee strength: best-effort prompt policy, no semantic invariant. Local persistence does not prove activation. Guidance can state solutions, algorithms and assumptions as tentative theories; applicability and reasons may survive inside the sheet. Theory-builder conditions 1–4: localized content afforded; content-guided consumption afforded (delivery wired); formulated content-directed criticism and resulting revision uninspected; memory iteration wired but iteration of a criticism result uninspected. Learning attributable to criticism: uninspected. Addressability is whole-sheet text with prompt-afforded finer items. Persistence is within rounds, across distinct questions and through checkpoint continuation. No independent answer oracle is supplied to this update; RTE-4 has the separate benchmark oracle. Human role is initial configuration, not a required update operation.

### RTE-6 — Embedding-selected prior examples

Implementation conclusion status: wired. Trigger: each direct-retrieval, retrieval-synthesis or hybrid input. Selector input is the current input embedding and all earlier embeddings; cosine similarity and descending argsort select at most retrieve_top_k prior pairs. Default k is 3. Runtime delivery is push to generator or curator, with no model-issued retrieval request. Pairs are displayed least-similar first so the closest is last. The score ranks content; it is not evidence of correctness. The corpus-to-embedding equality lookup is alignment, not a separate identifier-targeted read-back route. Evidence: SRC-1 `dynamic_cheatsheet/language_model.py`.

> similarities = cosine_similarity([current_original_input_embedding], prev_original_input_embeddings)
>                 top_k_indices = np.argsort(similarities[0])[::-1][:retrieve_top_k]
>                 top_k_original_inputs = [original_input_corpus[i] for i in top_k_indices]
>                 top_k_original_outputs = [generator_outputs_so_far[i] for i in top_k_indices]
> --- `dynamic_cheatsheet/language_model.py:510-513` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

Owner: Python selector; effect boundary: prompt assembly. Immediate return is selected pairs and scores, later delivered automatically. Delegated visibility is selected text and displayed similarity, not the complete corpus by filesystem access. No expiry or correctness invalidation; all prior indexed inputs remain eligible. No content revision admitted here; guidance is static critical-use prose. Guarantee strength: algorithmic top-k selection given aligned arrays, not correctness or relevance. Activation/benefit uninspected; malformed arrays remain caller/loader errors.

### RTE-7 — Full-history and empty-memory controls

Implementation conclusion status: wired. FullHistoryAppending formats every previous input/output pair into the generator's cheatsheet slot and returns that same formatted text. This is coarse automatic supply and mechanical compilation, not trace learning by itself. No curation or size trimming occurs. The default branch substitutes `(empty)` and returns no sheet; raw result logging alone does not make that branch learned memory. Evidence: SRC-1 `dynamic_cheatsheet/language_model.py`.

> for i, (previous_input_txt, previous_output_txt) in enumerate(zip(original_input_corpus, generator_outputs_so_far)):
> --- `dynamic_cheatsheet/language_model.py:464-464` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

Owner: branch code. Immediate return: answer and formatted history, or no sheet for default. Later read-back: all accumulated pairs in full history; default has none. Delegated visibility: assembled prompt only. Selector: all prior pairs, without invalidation or expiry; no curation admission or criticism iteration is established by raw accumulation. Guarantee strength: deterministic assembly under valid caller inputs, no semantic guarantee. API/provider failures propagate through RTE-1; context-window fit is not guaranteed.

### RTE-8 — Retrieval-synthesis update before answering

Implementation conclusion status: wired. Curator receives retrieved old trajectories, next input and previous sheet; the selected/rewritten sheet goes immediately to the generator and becomes the runner's next carried sheet. This is model-judgment push selection as well as online trace-fed rewriting. The initial example can yield a sheet without prior traces, but later examples supply them. If extraction fails, fallback is the raw formatted retrieved pairs, not the previous sheet. `new_cheatsheet` is null in the single saved step, but `current_cheatsheet` and `final_cheatsheet` contain the synthesis; null does not mean curation never occurred. Evidence: SRC-1 `dynamic_cheatsheet/language_model.py`, `prompts/curator_prompt_for_dc_retrieval_synthesis.txt`.

> cheatsheet_prompt = cheatsheet_template.replace("[[PREVIOUS_INPUT_OUTPUT_PAIRS]]", curated_cheatsheet)
>                 cheatsheet_prompt = cheatsheet_prompt.replace("[[NEXT_INPUT]]", input_txt)
>                 cheatsheet_prompt = cheatsheet_prompt.replace("[[PREVIOUS_CHEATSHEET]]", previous_cheatsheet)
> --- `dynamic_cheatsheet/language_model.py:533-535` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

Owner: CMP-1 proposes selected/rewritten content; Python performs extraction and later adoption. Immediate return includes synthesized current/final sheet and answer; next benchmark invocation supplies the prior sheet. Delegated visibility: curator sees selected examples, previous sheet and next question. Selection: embedding then model judgment, with no correctness filter or expiry. Rejection/recovery is formatting fallback to assembled examples; no automatic rollback. Guidance is OBJ-3, with reference to existing strategies, performance judgment, generalization and replacement. Whole-sheet explanations may persist, but full curator deliberation does not. Theory-builder conditions 1–4: localized content afforded; semantic consumption afforded with delivery wired; actual formulated criticism and linked revision uninspected; persistence/iteration of rewritten text wired while criticism-result uptake uninspected. Learning attributable to criticism uninspected. Persistence crosses later independent questions; addressability remains whole-sheet replacement with prompt-defined items. No external answer oracle guides this update; rejection of inferior methods is left to the model. Guarantee strength: prompt policy and formatting protocol, not semantic acceptance.

### RTE-9 — Seed import, persistence and resume

Implementation conclusion status: wired. Operator may select an initial text file, which is loaded without content validation. Runner then automatically carries returned sheets and outputs and rewrites JSONL after each problem. Resume loads all old rows, selects the last final sheet, rebuilds raw output history, and skips len(outputs) examples. This establishes cross-process recovery of memory, not cross-project learning. Path-specified import is not a model pull request. Evidence: SRC-1 `run_benchmark.py`.

> if args.initialize_cheatsheet_path is not None:
>         with open(args.initialize_cheatsheet_path, "r") as file:
>             cheatsheet = file.read()
> --- `run_benchmark.py:172-174` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

> last_cheatsheet = outputs[-1].get("final_cheatsheet")
>         if last_cheatsheet is not None:
>             cheatsheet = last_cheatsheet
> 
>         generator_outputs_so_far = [output["final_output"] for output in outputs]
> --- `run_benchmark.py:185-189` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

Resume compares generator_prompt_path, temperature, execute_python_code, task, model_name, approach_name and max_num_rounds. It does not compare all consequential settings, such as no_shuffle, retrieve_top_k, actual prompt bytes, embeddings or native execution choice. It assumes dataset/order compatibility. Changing ordering can associate old outputs with different current input positions; inspection establishes this missing check, not an observed corrupt run. The native container is recreated rather than restored by this route.

Owner: operator selects path/configuration, runner reads and writes files. Immediate return: loaded sheet/history or persisted JSONL; later consumer is generator/curator via other routes. Delegated visibility: models receive selected text, not all checkpoint metadata. Selection: specified seed path or last checkpoint row; this is recovery selection, not a model memory request. No expiry or automatic rejection of stale context. Admission of imported knowledge is direct loading; content/rationale may be externally authored and is not validated. No model-written method or production-machinery update is performed. Recovery is caller-initiated continuation, not transactional rollback. Guarantee strength: limited parameter equality checks; requires dataset ordering and external file integrity. File/parse failures propagate. Activation and reliable crash durability uninspected.

### RTE-10 — Provider-client chat history

Implementation conclusion status: afforded. Documented caller uses chat to send conversational messages; chat appends both user and assistant text. The next generate call automatically extends its message list with retained self.messages. This is an afforded caller route with wired internal automatic supply, not wired benchmark use. set_history allows caller replacement; reset_history clears it. get_history exposes a copy but no named downstream consumer makes that storage accessor a separate pull route. Raw conversational retention supplies no derived trace-learning artifact. Evidence: SRC-1 `text_generation/simple_unified_client.py`.

> messages.extend(self.messages)
>         messages.append({"role": "user", "content": prompt})
> --- `text_generation/simple_unified_client.py:481-482` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

Owner: caller chooses chat/set/reset; client automatically assembles and appends history. Current answer returns immediately; subsequent chat/generate reads all saved messages without budget-based trimming. Provider sees the assembled history; default benchmark generate_from_messages does not consume it. Caller set_history directly admits replacement content, reset_history withdraws it; there is no semantic veto, expiry or rollback. Guidance is conversational input/optional static system instruction, not distilled learned theory. Raw retention does not satisfy trace-learning transformation. Guarantee strength: in-process list copying and assembly only. Provider failures propagate and completed chat appends after response; activation or benefit uninspected.


### Claims

### CLM-1 — Learning without label feedback

Conclusion status: claimed. README says zero-shot performance improvement and experience-driven learning. The code supports automated curation without benchmark-target feedback to the curator, but benchmark assessment does use targets. Label-free updating is therefore different from label-free evaluation. Evidence: SRC-1 `README.md`, RTE-4 and memory routes.

> * **Zero-Shot Learning**: Improves performance without ground-truth labels or human feedback
> * **Experience-Driven Learning**: Bridges the gap between isolated inference events and cumulative learning
> --- `README.md:20-21` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

### CLM-2 — Reported accuracy gains

Conclusion status: claimed. README attributes more than doubled AIME accuracy to retained algebraic insights and reports other benchmark gains. This run did not inspect historical result payloads, the external paper, or a controlled experiment, so it neither reproduces these numbers nor establishes criticism or any one memory mechanism as the cause. Evidence: SRC-1 `README.md`.

> * **Mathematics**: Claude 3.5 Sonnet's accuracy more than doubled on AIME math exams by retaining algebraic insights
> --- `README.md:25-25` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

### CLM-3 — Curator doctrine and its admission limits

Doctrine conclusion status: claimed. Loaded templates direct correctness assessment, concise retention, duplicate removal, new strategies, replacement of inferior methods, and usage-based priority. Their admission into model context affords these curation operations; completion and accuracy are unobserved. No code recognizes memory_item entries or verifies counts. Evidence: SRC-1 `prompts/curator_prompt_for_dc_cumulative.txt`, `prompts/curator_prompt_for_dc_retrieval_synthesis.txt`.

> Continuous Refinement & Optimization:
> - Improve existing strategies by incorporating more efficient, elegant, or generalizable techniques.
> - Remove duplicate entries or rephrase unclear explanations for better readability.
> - Introduce new meta-strategies based on recent problem-solving experiences.
> --- `prompts/curator_prompt_for_dc_retrieval_synthesis.txt:18-21` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

> 4. Implement a Usage Counter
>    - Each entry must include a usage count: Increase the count every time a strategy is successfully used in problem-solving.
>    - Use the count to prioritize frequently used solutions over rarely applied ones.
> --- `prompts/curator_prompt_for_dc_cumulative.txt:60-62` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

The cumulative template asks for assumptions and limitations, descriptions, annotated examples and solution explanations. This affords retained reasons and scope conditions, but does not require a change justification or persist curator deliberation outside the extracted sheet. Generator and later curator receive any such rationale retained inside it; omitted reasoning has no read-back route. Evidence: SRC-1 `prompts/curator_prompt_for_dc_cumulative.txt`, `dynamic_cheatsheet/language_model.py`.

> - Clearly state any assumptions, limitations, or dependencies (e.g., specific Python libraries or solution hacks).
> --- `prompts/curator_prompt_for_dc_cumulative.txt:25-25` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

### Evidenced absences

### ABS-1 — No semantic admission or automatic rollback in inspected curation

Conclusion status: absent. Bounded search/read: every advanced_generate approach, full extract_cheatsheet function and runner update/evaluation/resume code. The extractor selects text following an opening tag, splits at a closing tag if present, and otherwise retains old_cheatsheet only when the opening tag is absent or an exception occurs. A missing closing tag or an empty block can still be accepted. No checked truth, source reference, memory-entry schema, usage counter, benchmark success or human approval guards replacement. Previous checkpoint states exist but no rollback selector is wired. This absence does not claim provider internals lack controls. Evidence: SRC-1 `dynamic_cheatsheet/utils/extractor.py`, `dynamic_cheatsheet/language_model.py`, `run_benchmark.py`.

> if "<cheatsheet>" in response:
>         try:
>             txt = response.split("<cheatsheet>")[1].strip()
>             txt = txt.split("</cheatsheet>")[0].strip()
>             return txt
>         except:
>             return old_cheatsheet
>     else:
>         return old_cheatsheet
> --- `dynamic_cheatsheet/utils/extractor.py:78-86` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`


### Behavioral-authority paths

### BAP-1 — Static templates to model

Consumer CMP-1, channel user-message prompt, force instruction/advice, horizon current generator or curator invocation. Code guarantees string assembly, not model obedience. Evidence: SRC-1 `dynamic_cheatsheet/language_model.py`, OBJ-3, RTE-1. Conclusion status: wired.

### BAP-2 — Model code to local or remote executor

Consumer local Python or provider code tool, channel extracted program or API tool request, force execution permission, horizon one invocation plus its external effects. Local grants follow process privileges; server grants are provider-defined. Evidence: SRC-1 `dynamic_cheatsheet/language_model.py`, `dynamic_cheatsheet/utils/execute_code.py`, `text_generation/simple_unified_client.py`; RTE-2 and RTE-3. Conclusion status: wired.

### BAP-3 — Evaluator result to benchmark counters

Consumer benchmark loop, channel boolean, force counting/reporting, horizon current benchmark continuation. No authority to accept or veto memory updates. Evidence: SRC-1 `run_benchmark.py`, RTE-4. Conclusion status: wired.

### BAP-4 — Accumulated memory to generator and curator

Consumer CMP-1; user-message channel; force advisory knowledge for sheets/history, ranking for embeddings; horizon current and later calls connected by RTE-5, RTE-6, RTE-7, RTE-8, RTE-9, and the separately afforded RTE-10. Source: SRC-1 and these routes. Conclusion status: wired for benchmark supply, afforded for documented client use. Selection does not certify truth; actual activation uninspected. Provider container reuse under RTE-3 is a separate opaque authority path, not inferred to share this knowledge force.


## Runtime account

An operator chooses a model and approach, loads prompt files and tasks, and optionally restores a checkpoint or creates a provider tool session. Each dataset item becomes a question. The ordinary cumulative path presents the current cheatsheet to the generator, optionally receives execution feedback, extracts an answer, asks the same model to revise the cheatsheet, adopts its formatted output, then scores and checkpoints the answer. This ordering matters: the evaluator does not supervise the adaptive memory. Retrieval branches select earlier input/output pairs by cosine similarity; retrieval-synthesis calls a curator before answering, while the hybrid combines cumulative strategies with selected examples and curates after answering. Full history bypasses curation; default bypasses memory. The wrapper is a returning computation for direct callers, while the benchmark owns sequential cross-question persistence and resume.

The run has multiple operating modes: direct open caller requests, and bounded benchmark experiments. The benchmark's task references govern score reporting only; direct calls have no answer oracle supplied by the wrapper. Within generation/curation, CMP-1 proposes and assesses content; Python chooses branches, executes configured effects, parses output and installs the next string. No runtime human approval is required after configuration. Operators can select alternative templates or starting memory externally; the inspected loop does not rewrite its own Python, templates or provider selection. These roles establish computational scheduling, not autonomous theory-building without evidence for criticism and uptake.

Static forcing cases checked: (1) malformed/absent cheatsheet markup falls back to old or assembled retrieval context, while merely seeing an opening tag can admit malformed/truncated content; (2) local recursion checks its bound after execution, so a warning is not the last possible execution; (3) interpreter mode and local execution flags have different boundaries, and task scoring can still call `eval`; (4) resumed memory restores text/history but not the provider container or verified agreement with every prior setting. Missing embeddings fail retrieval entry before model calls; first retrieval item has no prior examples. Hybrid ignores cumulative refinement-round repetition. None of these traces establishes a live incident or quantitative failure rate.

Capability surface: model API, optional local or provider-native Python, templates, memory initialization, checkpoint load/save, and selected provider kwargs. Current grant set is deployment-selected; this source inspection did not inspect secrets or run API calls. Deployed isolation envelope is uninspected. The local subprocess is not an application sandbox; the native service is not evidence of the local evaluator's safety. Providers and external API contracts can change independently of this fixed source pin.

Execution preflight disposition: **no dynamic check planned**. Considered a mock trace of recursion/markup and a real benchmark/retrieval run. Static branches directly establish the control-flow claims; a live benchmark would need provider credentials, dependencies and dataset state and would not alone isolate memory benefit. No target code, external service, generated snippet or evaluator was executed. Therefore there are no observed-run probe capsules and no claimed causal findings.

## Lens scoping

### Memory/context scope

Depth: full. Trigger: CLM-1, CLM-2 and source-visible cumulative/retrieval branches. Scope: specialist's retained cheatsheet/history/checkpoint and access structures, all six approach alternatives and resume, with visible provider-container reuse included and its internal payload left opaque in the profile. Exact frozen source and report identities appear in Run identity. All memory routes below are source-checkable; static prompts are outside accumulated-memory classification.

### Epistemic scope

Depth: full. Trigger: CLM-1, CLM-2, OBJ-3's correctness and transferable-strategy instructions, RTE-2's execution feedback and RTE-4's answer scoring. Inspected boundary: SRC-1 and the shared objects/routes, including all memory branches. Question: which content is generated, checked, admitted and used, and does any observed candidate earn an evidence-consuming acceptance transition? Provider reasoning, paper and historical result payloads are uninspected; this prevents candidate-level criticism, observed acceptance and causal learning claims. Runtime-only provider/selection plumbing is classify-only where it changes no truth-apt content.

## Lens outputs

### Memory/context lens

The recurrent memory is chiefly a replaceable text sheet, not a database of independently maintained entries. A curator receives model solutions and the current sheet; its extracted response becomes the next sheet. The runner carries that sheet across distinct problems and persists it with raw outputs. The object OBJ-7 and routes RTE-5, RTE-8, RTE-9 establish this chain.

Retrieval adds a separate access structure: precomputed input embeddings rank earlier inputs and select their generated solutions. Direct retrieval sends these pairs to the generator; retrieval-synthesis sends them, the previous sheet and the next question to the curator first. Hybrid retrieval combines the current sheet and selected pairs before answering, then updates the sheet. Thus retrieval-synthesis is also recurrent, despite the shorthand “custom cheatsheet per query.” See routes RTE-6 and RTE-8.

Selection reduces delivered examples to top-k but still compares against all earlier input embeddings and sorts their similarities. Full-history appending grows with the complete prior solution list. Neither route trims source text to a token budget. Curator generation is capped at twice generator max_tokens, while the shipped instruction suggests roughly 2000–2500 words; this is not an enforced input-memory size bound. The GPT-4o tokenizer utility does not gate these delivery paths.

Source trust is delegated to the models. The curator is told to assess correctness and preserve useful material; retrieved examples warn that prior solutions may be wrong. Code admits extracted text without correctness, provenance or usage-count validation. Benchmark scoring occurs after curation and does not determine admission. Local execution output may inform the generator and then curator, but a benchmark target is not included in either prompt by the inspected runner. See records CLM-3 and ABS-1.

The acquired raw material is a current generated solution, potentially including local tool output (objects OBJ-8, routes RTE-2 and RTE-5). Curation automatically converts it to the reusable sheet (OBJ-7); runner persistence and resume (RTE-9) make it available beyond the call. Retrieval-synthesis uses earlier generated solutions as trace inputs and revises against the next question (RTE-8). Direct retrieval and full-history assemble raw material without independently establishing distilled learning.

Manually supplied seed files and message-history replacement are separate authoring/import surfaces. They do not imply a review or adoption UI. Neither the benchmark result nor the initial-file load gives individual entries stable provenance: prompt-requested Q references and usage counts remain text. The current generator question is numbered, while retrieval display numbers examples locally; provenance labels are not validated against dataset identity.

Derived sheets can retain reasons within descriptions, assumptions and worked examples. Subsequent generator and curator calls read the whole sheet, including those reasons if present. Full curator responses are not retained in the returned result: only extracted sheets survive. There is no guaranteed separate record explaining why a revision occurred. This is a restriction on retained diagnosis, not proof that the model performs no content-directed criticism. The templates explicitly request correctness assessment and improvements; actual criticism and its uptake require admitted execution evidence.

The named model consumers are the generator and curator. In cumulative operation the trigger is the next round or question and selection is the entire current sheet; in direct retrieval it is cosine-ranked prior pairs; in retrieval-synthesis it includes curator judgment conditioned on the next question; in full-history it is all prior pairs. All are supplied automatically as user-message content via template substitution. The generator is asked to find relevant parts and verify limitations, but delivery alone does not establish activation or benefit.

No inspected ordinary branch gives the generator a retrieval tool or requires it to request memory. The API caller requesting an answer is not the memory consumer issuing a retrieval request. The separate documented client chat interface retains and supplies history; history getter availability is insufficient to assert a downstream pull route. Native execution may have additional retrieval semantics, but the reused container reference alone does not establish them.

The k budget limits example count, not their token volume. Cumulative and full-history context lack a hard retained-input budget; curator max output tokens and suggested words constrain only production. Checkpoint files grow with all completed rows and are rewritten after each example. Source inspection establishes these scaling mechanisms; no latency, memory-size or quality measurements were run.

The fourteen-axis profile uses the same boundary as these records. Numeric embeddings are symbolic access metadata stored as CSV/arrays, not model weights, a vector database or proof of parametric learning. Sheets are knowledge because the consumer treats them as reference material requiring relevance and correctness checks; shipped static generator/curator instructions are excluded from the memory authority union.

Known trace_learning yes follows from routes RTE-5, RTE-8 and RTE-9, independently of the unknown native branch. Scope is both per-task and cross-task: max_num_rounds repeats a problem, while the benchmark passes memory across different problems. The runner's dataset label `task` does not collapse those distinct problem horizons. Timing is online for both qualifying curation routes; no offline learning is inferred from imported embeddings or resume.

Curation values beyond evolve are marked afforded because prompts request the operations and invoke a capable curator, but their successful execution is not inspected. Symbolic distilled content is likewise afforded by explicit code-snippet requests. This preserves positive capability without converting prompt intentions into observed payloads. Coarse, inferred-embedding and inferred-judgment selectors have concrete wired witnesses. The last refers to curator selection of retained material for the upcoming generator question, not an assertion that every generated judgment is correct.

Partial coverage is deliberate where opaque native execution memory could add values. It does not weaken wired local witnesses. A service container identifier establishes resource reuse, not an entire payload ontology. Faithfulness is unknown because the admitted evidence lacks retained executions testing dependence; README accuracy claims do not close that gap.

### Epistemic lens

#### 1. Source-and-claim boundary

Dynamic Cheatsheet at the frozen revision in SRC-1; assessed families: answer generation, tool feedback, trace curation, retrieval, formatting admission, persistence/resume and benchmark evaluation. Boundary and exclusions are unchanged. CLM-1 and CLM-2 are claims, not acceptance evidence. No candidate instance or target run was inspected, so every candidate observation field below is **no instance observed**.

#### 2. Epistemic-object inventory

OBJ-1 supplies acquired task content and reference targets; its source warrant is unknown. OBJ-2 can contain new truth-apt answers, explanations and executable proposals. OBJ-3 is static operational instruction, not a produced candidate. OBJ-4 is execution evidence whose warrant is confined to the executed program/environment, not its assumptions. OBJ-5 is a task-domain score, not a memory endorsement. OBJ-6 carries service access identity, no truth-apt candidate. Retained memory, history and vectors are addressed under their canonical records below: strategies can be ampliative conjectures; history preserves model assertions rather than validated facts; embeddings select related records without conferring warrant. See canonical objects for form, lineage, producer, consumer and source anchors.

#### 3. Authority-route ledger

Each following function has architectural status **implemented** unless explicitly qualified. Observed candidate state remains **no instance observed** independently. Source: SRC-1 and the named canonical record anchors. Canonical records own endpoints, context and generic progression.

| Route/function | Content/update relation and check target | Evaluator/condition and timing | Result, force and authority | Claim and limit |
|---|---|---|---|---|
| RTE-1 — content transformation | Ampliative conjecture for proposed answers/strategies; individual derivation versus conjecture indeterminate without content | CMP-1 under OBJ-3 at generation | Produces OBJ-2, not an accepted theorem; prompt influence BAP-1 | CLM-1; inference fluency does not certify answer truth |
| RTE-1 — operational admission/selection/consumption | No content change beyond extraction; target answer text | Delimiter/fallback parser at return | Permits answer to return and enter history; no semantic veto | CLM-1; formatting does not establish acceptance |
| RTE-2 — check/evidence production | Program execution; truth-apt outcome scoped to program/environment | Local Python after a flagged block | Produces OBJ-4 and can affect continuation; BAP-2 | No claim of formal proof; assumptions, safety and causal correctness remain untested |
| RTE-3 — check/evidence production | Tool computation; internal evidence preservation indeterminate | Provider tool per configured call | Permits remote computation and returns extracted text; BAP-2 | Provider internals and result completeness uninspected |
| RTE-4 — check/evidence production | No candidate content change; target OBJ-2 task answer | Reference label or arithmetic constraints, after memory adoption | Produces OBJ-5 scoped answer judgment | CLM-2; no authority over strategy generalization |
| RTE-4 — disposition/acceptance | No content change; benchmark answer classification | Task-specific boolean increments score | Reporting authority BAP-3; no subsequent memory acceptance or integration | CLM-1; labels are available to evaluation, not the inspected curation input |

| RTE-5 and RTE-8 — content transformation | Indeterminate mix of reshaping, derivation and ampliative conjecture in OBJ-7 | CMP-1 under curator instructions; after solving or before next question | Proposes rewritten strategies and examples; BAP-4 | CLM-1, CLM-3; novelty/preservation and actual criticism are not observed |
| RTE-5 and RTE-8 — disposition/acceptance | No content change; target extracted sheet | Opening-tag extraction, not semantic criterion | Installs text for use; BAP-4; ABS-1 bounds absence of a separate semantic gate | CLM-3; operational admission is not epistemic acceptance |
| RTE-6 — operational admission/selection/consumption | No change to selected original assertions; target OBJ-8 via OBJ-9 | Cosine similarity, prior-only top-k, per question | Ranking and advisory delivery BAP-4 | CLM-1; similarity does not warrant truth |
| RTE-7 — content transformation | Non-ampliative reshaping of OBJ-8 into prompt text | Mechanical full-history formatting | Supplies raw assertions BAP-4; default bypasses this | CLM-1; retention alone is not learning |
| RTE-9 — retention | No content change; OBJ-7 and OBJ-8 stored in OBJ-10 | Runner after item generation | Persists text for recovery; no epistemic acceptance | CLM-1; earlier entries are not a rollback policy |
| RTE-9 — lineage/freshness/recovery | Acquisition/import of saved text | Operator path plus last-row selection and limited config check | Restores active context BAP-4 | CLM-1; unverified ordering/prompt identity limits applicability |
| RTE-10 — retention | Acquisition/import into OBJ-11 | Caller invokes chat/set_history; client saves text | Afforded external entry, implemented retention | No derived-learning claim |
| RTE-10 — operational admission/selection/consumption | No content change to OBJ-11 | Client assembles saved messages on next call | Advisory context BAP-4, no semantic criterion | Getter alone does not establish pull |


Curator correctness instructions are wired model judgment, not a separate answer oracle. They can guide rejection or revision in generated text. Parsing admits the resulting memory regardless of a separately recorded pass/fail judgment. Criticism and admission therefore must not be conflated: the model can formulate criticism, while the code neither requires a criticism record nor verifies its relation to the selected revision.

#### 4. Per-object lifecycle disposition

For OBJ-2, proposed solutions may be ampliative or derived; which is indeterminate without an instance. The wired routes supply generation and possible program execution, followed by benchmark answer assessment when applicable. They do not establish a tested general explanation or verified memory strategy. Observed candidate state: no instance observed for every phase. RTE-4 supplies only its task-answer check domain; no post-acceptance strategy integration is established.

For OBJ-7 strategy candidates via RTE-5 and RTE-8, observation inputs and curator generation/rewriting routes are implemented, and reuse is implemented. Prompted correctness assessment or comparison can be a test/evidence operation, but a candidate-linked criticism, derived consequence, accepted scope and resulting change are not determinable from code alone. Operational retention precedes any independently evidenced acceptance. Consequently discovery lifecycle acceptance and post-acceptance integration are not established; for all phases the observed candidate state is no instance observed. The uninspected content can include non-ampliative consolidation, entailed calculation or ampliative strategy claims; no single transformation type is imposed on every returned string.

For OBJ-1 the transformation is acquisition/import, discovery lifecycle not applicable; warrant rests on external task/target provenance. OBJ-4 is generated execution evidence, with entailment limited by program semantics and faithful interpretation. OBJ-5 is derived score under task-specific code, with source-truth and encoding limits. OBJ-8 raw history, OBJ-10 checkpoint read-back and OBJ-11 client conversation preserve model-assertion lineage through RTE-6, RTE-7, RTE-9 and RTE-10; acquisition/reshaping is non-ampliative and the discovery lifecycle is not applicable to storage alone. OBJ-9 numerical access metadata ranks inputs through RTE-6 without candidate truth-apt output; no lifecycle record for OBJ-9: relevant update route RTE-6. No lifecycle record for OBJ-3: no candidate truth-apt output for this object; relevant direct-adaptation or update routes: RTE-1. No lifecycle record for OBJ-6: no candidate truth-apt output for this object; relevant direct-adaptation or update routes: RTE-3.

#### 5. System-claim versus route comparison

| Claim | Doctrine and implementation | Observed/causal support | Supported conclusion and mismatch |
|---|---|---|---|
| CLM-1 | Curation and read-back are implemented; RTE-4 is separate label-based assessment | No inspected run or intervention | Label-free memory updating is wired; learning through criticism and improved future capacity remain uninspected |
| CLM-2 | README reports accuracy gains; benchmark can compare approaches using task scores | Historical outputs and study design excluded | Reported gains remain claimed; no attribution to curator, retrieval, code execution or theory criticism established |

#### 6. Bounded conclusion

The implementation produces candidate answers and strategies, preserves prior model text, and gives later calls access to it. Program feedback and task scores have distinct domains and forces. Nothing about operational memory retention alone licenses a claim as true. Conversely, lack of a deterministic memory validator does not establish absence of model criticism: the prompts explicitly request assessment, while actual formulated criticism and uptake remain uninspected. The analysis establishes an improvement-directed context-update pathway, not observed epistemic acceptance or causal learning.

## Reconciliation

Fresh specialist report identity, complete status, input/method digests, source pin and report hash were verified. The report is provenance, not independent semantic clearance. No substantive conflicts require reanalysis. Exact proposal mappings:

| Specialist proposal | Canonical record | Disposition |
|---|---|---|
| MEM-OBJ-1 | OBJ-7 | Registered with proposed scope and status preserved |
| MEM-OBJ-2 | OBJ-8 | Registered with proposed scope and status preserved |
| MEM-OBJ-3 | OBJ-9 | Registered with proposed scope and status preserved |
| MEM-OBJ-4 | OBJ-10 | Registered with proposed scope and status preserved |
| MEM-OBJ-5 | OBJ-11 | Registered with proposed scope and status preserved |
| MEM-OBJ-6 | OBJ-6 | Merged into same referent; retained memory-specific evidence and limits |
| MEM-RTE-1 | RTE-5 | Registered with proposed scope and status preserved |
| MEM-RTE-2 | RTE-6 | Registered with proposed scope and status preserved |
| MEM-RTE-3 | RTE-7 | Registered with proposed scope and status preserved |
| MEM-RTE-4 | RTE-8 | Registered with proposed scope and status preserved |
| MEM-RTE-5 | RTE-9 | Registered with proposed scope and status preserved |
| MEM-RTE-6 | RTE-2 | Merged into same referent; retained memory-specific evidence and limits |
| MEM-RTE-7 | RTE-10 | Registered with proposed scope and status preserved |
| MEM-RTE-8 | RTE-3 | Merged into same referent; retained memory-specific evidence and limits |
| MEM-CLM-1 | CLM-3 | Registered with proposed scope and status preserved |
| MEM-CLM-2 | CLM-2 | Merged into same referent; retained memory-specific evidence and limits |
| MEM-ABS-1 | ABS-1 | Registered with proposed scope and status preserved |

Integration issues disposed: retrieval-synthesis includes the prior sheet, falls back to retrieved examples, and uses a null step new_cheatsheet despite synthesis (RTE-8). Hybrid single-round behavior remains distinct (RTE-5). Resume checks and recreated container limits remain explicit (RTE-9, RTE-3). The documented client-history route is included as afforded external use, not benchmark wiring (RTE-10). Native container payload uncertainty is included in profile scope and partial assessments, rather than excluded to force complete sets (OBJ-6, RTE-3). Rationale can persist only inside extracted sheets; missing separate deliberation does not prove absent criticism (CLM-3, RTE-5, RTE-8). Profile values, evidence bases, coverage and uncertainties were adopted unchanged after exact ID mapping. Shared local/native execution records retain coordinator control-flow details and specialist memory effects without duplicate generic routes. Independent overlap on adoption-before-scoring and hybrid rounds is treated as corroborating inspection, not independent empirical evidence. No report bytes or citations were modified.


## Bounded synthesis

Dynamic Cheatsheet changes the context of future model calls by retaining and revising material derived from earlier problem solving. Its strongest implementation contribution is a complete local route from question, through solution and optional computation, to renewed cheatsheet and later question; retrieval and hybrid variants change which experience is presented. Benchmark persistence makes this useful beyond one API response. Its main admission boundary is text extraction and caller scheduling, while the correctness evaluator runs after the memory successor has already been chosen.

The important tradeoff is source-native: concise curator output can preserve reusable strategies and code, but whole-string replacement depends on the model preserving useful material and distinguishing sound from unsound solutions. Retrieval selects by question similarity, not answer correctness. Full history avoids curator loss but expands context. All routes can deliver accumulated text without establishing that a particular later answer depended on it or improved because of it.

Under the [theory-builder definition](../../../../notes/definitions/theory-builder.md), the four conditions remain separate. Localized proposed solutions and strategies are afforded in natural-language/code units; content-guided use is afforded by generator instructions, with delivery wired and actual activation uninspected. Content-directed criticism is afforded by correctness/limitation/replacement instructions, but a formulated challenge to an identified theory and resulting revision or changed reliance is uninspected. Iteration of rewritten memory is wired, while iteration specifically carrying the result of criticism is uninspected. Membership as an exercised theory builder is therefore uninspected, not established by trace-learning classification. Addressability is at least a whole cheatsheet as editable text; prompt-defined items, examples and assumptions afford finer parts but no stable entry identity or patch operation is enforced. Persistence covers retained text across rounds, questions and checkpoint continuation, not an observed retained criticism record.

Learning has a supported implementation precursor—automatic trace-derived context and later delivery—and reported performance claims, but no inspected comparison attributes improved capacity to criticism of consumed theories. Conclusion status for such learning: uninspected. [Self-improvement](../../../../notes/definitions/self-improving-system.md) has an afforded, improvement-directed pathway at the composite wrapper/model/memory boundary; observed evidence-responsive changes causing better later operation are uninspected. The word “improving” in the objective does not establish successful improvement.

[Reflection](../../../../notes/definitions/reflective-system.md) is afforded for selected aspects: previous solution behavior and strategy text can be represented to the curator, revised and supplied back to the generator. The inspected evidence establishes the text route, not a verified two-way semantic representation or its actual causal effect; exercised reflection is uninspected. Reflective theory-building about its own curation standards and runtime machinery is uninspected: shipped method templates and Python remain externally authored. Computational ownership is wired for proposing output, prompted assessment, text admission and scheduling; autonomous theory-builder membership remains uninspected because actual criticism, blame assignment and uptake are not established. None of these properties is inferred from another.

A sequential benchmark with comparable questions can use this architecture to carry context forward. An isolation-sensitive deployment needs to assess the actual executor and evaluator paths separately. A long-running application needs caller-owned checkpoint/configuration integrity and context budgets beyond prompt advice. Candidate-linked traces showing strategy use, criticism, revision and next-round use would strengthen theory-builder conclusions; a controlled retained-memory intervention with matched model/tool conditions would address activation and learning; provider and environment evidence would address deployment guarantees.

## Limitations

| Limitation | Affected IDs | Inspected boundary | Conclusion prevented | Resolving evidence |
|---|---|---|---|---|
| No runtime or intervention | SRC-1, CMP-1, CLM-1, CLM-2 | Static source and doctrine only | Observed activation, causal benefit, formulated criticism and learned capacity | Candidate-linked execution and controlled memory comparison |
| Provider internals and exact model weights opaque | CMP-1, RTE-3, OBJ-6 | Request construction and returned text | Exact parameter fixity, tool state continuity/isolation and hidden feedback completeness | Versioned provider records and deployed traces |
| External dataset/source truth unavailable | OBJ-1, RTE-4 | Loader and evaluator wiring | Reference correctness and general problem-solving validity | Dataset provenance and task-domain audit |
| Historical results and paper excluded | CLM-2 | README reports only | Reproduced performance or mechanism-level attribution | Frozen experiment outputs and full comparison design |
| Unused standalone client/notebook/evaluator entry points not traced | SRC-1 | Selected shipped workflow entry paths | Universal claims over every direct client invocation | Separately bounded inspection of those APIs |

| Opaque memory payload and unaudited curation | OBJ-6, OBJ-7, CLM-3, RTE-3, RTE-5, RTE-8 | Local source-visible text and native handle reuse | Complete memory value sets, actual counts, retained rationale content, reliable curation | Candidate payloads and provider state traces |


## Verification and blockers

### Semantic verification

Checked all six approach branches, source pin/origin, ordinary invocation and four static forcing cases. Component identity, external oracles, proposal/admission roles, local and provider execution boundaries, memory read-back, conditional grants and return/recovery are distinguished. No target runtime was executed. Quote blocks are generated from the frozen commit; canonical records retain each adopted passage once. The epistemic overlay distinguishes implementation from observation and memory admission from warrant. Checked every included trace-fed write: RTE-5 cumulative and hybrid post-answer curation, RTE-8 retrieval-synthesis, and RTE-9 persistence. Their union supports online trajectories/tool-traces and per-task/cross-task horizons; raw history and ephemeral local continuation alone were not reclassified as distilled learning. RTE-5 and RTE-7 provide whole-sheet/history coarse supply; RTE-6 uses current-input embeddings to select prior pairs; RTE-8 uses next-question-conditioned curator selection. The consumer, trigger, selector input and selected retained part are explicit. RTE-10 is afforded direct client use with wired internal supply; RTE-3 native internals remain opaque and keep the profile partial. Known trace-learning yes is existential and does not erase these gaps. Faithfulness remains not-determinable. Every mapped target is declared uniquely, all fourteen axes retain their evidence/coverage distinction, and no value is strengthened from the specialist report.

### Deterministic validation

Exact target: `kb/reports/state/agentic-system-analysis/AAS-2026-09-27-dynamic-cheatsheet-03/result.md`; `commonplace-validate --full` passed; the final corrected bytes are validated again before publication. No validation receipt or semantic review-job state is retained here.

### Blockers

none
