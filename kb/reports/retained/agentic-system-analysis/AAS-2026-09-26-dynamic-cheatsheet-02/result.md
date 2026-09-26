---
{
  "type": "types/agentic-system-analysis-result.md",
  "description": "Dynamic Cheatsheet workflow at a frozen source revision: caller-owned memory, automatic curation, execution controls and bounded warrant",
  "run-id": "AAS-2026-09-26-dynamic-cheatsheet-02",
  "system": "Dynamic Cheatsheet",
  "run-date": "2026-09-26",
  "result-disposition": "complete",
  "target-class": "workflow",
  "boundary-kind": "whole-system",
  "reviewed-boundary": "5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9",
  "analysis-cutoff": "2026-09-26",
  "evidence-tier": "code-grounded",
  "memory-comparison": {
    "scope": "Use-accumulated cheatsheets, earlier input/output and tool traces, imported seed/checkpoint state, retrieval vectors and index alignment, plus the bounded provider-native execution object, in the six advanced_generate variants and benchmark caller. Static templates and benchmark targets are context/evaluation evidence, not memory-profile members. Provider payloads and imported-vector production remain unknown.",
    "axes": {
      "storage_substrate": {
        "assessment": "partial",
        "values": [
          "files",
          "in-memory",
          "vector",
          "service-object"
        ],
        "evidence": {
          "files": {
            "basis": "observed",
            "records": [
              "CLM-4",
              "RTE-6"
            ],
            "note": "Pinned JSONL checkpoints retain cheatsheets and recorded prompts; the benchmark wires writing and resumption."
          },
          "in-memory": {
            "basis": "wired",
            "records": [
              "RTE-1",
              "RTE-2",
              "RTE-7"
            ],
            "note": "Caller lists, current cheatsheet strings and recursive message history persist between their named consumers."
          },
          "vector": {
            "basis": "wired",
            "records": [
              "OBJ-3",
              "RTE-3",
              "RTE-4"
            ],
            "note": "Imported numeric arrays support cosine ranking of retained previous solutions; no vector database is implied."
          },
          "service-object": {
            "basis": "wired",
            "records": [
              "OBJ-7",
              "RTE-8"
            ],
            "note": "OpenAI container creation returns an ID reused by generation requests in the benchmark run."
          }
        },
        "records": [
          "OBJ-1",
          "OBJ-2",
          "OBJ-3",
          "OBJ-7",
          "RTE-6",
          "CLM-4"
        ],
        "note": "The included provider-native retained payload is opaque; interface evidence does not close its internal alternatives."
      },
      "representational_form": {
        "assessment": "partial",
        "values": [
          "natural-language",
          "symbolic"
        ],
        "evidence": {
          "natural-language": {
            "basis": "observed",
            "records": [
              "CLM-4",
              "OBJ-1"
            ],
            "note": "Retained explanations are present in cheatsheets and in later recorded generator prompts."
          },
          "symbolic": {
            "basis": "wired",
            "records": [
              "OBJ-3",
              "OBJ-8",
              "OBJ-9"
            ],
            "note": "Numeric vectors and their array alignment, serialized checkpoint fields, and Python code in retained transcripts have explicit machine interpretation."
          }
        },
        "records": [
          "OBJ-1",
          "OBJ-2",
          "OBJ-3",
          "OBJ-7",
          "OBJ-8",
          "OBJ-9"
        ],
        "note": "The included provider-native retained payload is opaque; interface evidence does not close its internal alternatives. Returned text does not classify the service payload; no parametric memory is established."
      },
      "lineage": {
        "assessment": "partial",
        "values": [
          "trace-extracted",
          "imported",
          "authored"
        ],
        "evidence": {
          "trace-extracted": {
            "basis": "wired",
            "records": [
              "RTE-2",
              "RTE-3",
              "RTE-4"
            ],
            "note": "Curator inputs include generator trajectories and retained earlier solutions, and outputs become later cheatsheets."
          },
          "imported": {
            "basis": "wired",
            "records": [
              "OBJ-3",
              "RTE-6"
            ],
            "note": "The runner loads precomputed vectors, optional seed text, and prior-run checkpoints."
          },
          "authored": {
            "basis": "afforded",
            "records": [
              "RTE-11"
            ],
            "note": "The documented caller supplies arbitrary cheatsheet text or a pre-existing seed file; this affords original human-authored content without demonstrating its use."
          }
        },
        "records": [
          "RTE-2",
          "RTE-3",
          "RTE-4",
          "RTE-6",
          "RTE-11",
          "OBJ-7"
        ],
        "note": "The included provider-native retained payload is opaque; interface evidence does not close its internal alternatives. Imported vector production and seed authorship are not known; authored is a caller affordance, not a provenance claim about the supplied datasets."
      },
      "behavioral_authority": {
        "assessment": "partial",
        "values": [
          "knowledge",
          "instruction",
          "ranking"
        ],
        "evidence": {
          "knowledge": {
            "basis": "observed",
            "records": [
              "CLM-4",
              "RTE-2"
            ],
            "note": "Recorded next-step prompts contain retained solutions and explanations as reference material."
          },
          "instruction": {
            "basis": "wired",
            "records": [
              "OBJ-1",
              "RTE-2",
              "RTE-4"
            ],
            "note": "Retained strategies and step-by-step guides enter the user prompt and can prescribe how the generator tackles later problems."
          },
          "ranking": {
            "basis": "wired",
            "records": [
              "OBJ-3",
              "RTE-3",
              "RTE-4"
            ],
            "note": "Retained numeric vectors determine cosine order and top-k membership of past examples."
          }
        },
        "records": [
          "OBJ-1",
          "OBJ-2",
          "OBJ-3",
          "OBJ-7",
          "RTE-2",
          "RTE-3",
          "RTE-4",
          "CLM-4"
        ],
        "note": "The included provider-native retained payload is opaque; interface evidence does not close its internal alternatives. Prompt instructions are model-mediated, not enforcement. Evaluation targets are not supplied to the curator; no memory-based validation authority is established."
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
              "RTE-1",
              "RTE-2",
              "RTE-3",
              "RTE-4",
              "RTE-6"
            ],
            "note": "The runner captures results, invokes curator transformations and rewrites checkpoints automatically after each processed problem."
          },
          "manual": {
            "basis": "afforded",
            "records": [
              "RTE-11"
            ],
            "note": "An operator/caller can author seed text or replace the supplied cheatsheet before calling the documented interface; no manual editing UI or observed intervention is claimed."
          }
        },
        "records": [
          "RTE-1",
          "RTE-2",
          "RTE-3",
          "RTE-4",
          "RTE-6",
          "RTE-11",
          "OBJ-7"
        ],
        "note": "The included provider-native retained payload is opaque; interface evidence does not close its internal alternatives."
      },
      "curation_operations": {
        "assessment": "partial",
        "values": [
          "consolidate",
          "dedup",
          "evolve",
          "synthesize",
          "decay",
          "promote"
        ],
        "evidence": {
          "consolidate": {
            "basis": "wired",
            "records": [
              "RTE-2",
              "RTE-3",
              "RTE-4"
            ],
            "note": "Curator templates wired to regeneration ask for concise retention and removal of trivial details from existing memory."
          },
          "dedup": {
            "basis": "wired",
            "records": [
              "RTE-3"
            ],
            "note": "The retrieval-synthesis curator is explicitly told to remove duplicate entries and receives the previous cheatsheet."
          },
          "evolve": {
            "basis": "wired",
            "records": [
              "RTE-2",
              "RTE-3",
              "RTE-4"
            ],
            "note": "Templates request revisions to existing strategies; extracted output replaces the current cheatsheet."
          },
          "synthesize": {
            "basis": "wired",
            "records": [
              "RTE-2",
              "RTE-3",
              "RTE-4"
            ],
            "note": "Templates request new meta-strategies and generalized insights derived from solution experiences."
          },
          "decay": {
            "basis": "wired",
            "records": [
              "RTE-3"
            ],
            "note": "The curator is directed to discard low-value retained details and the regenerated sheet replaces current memory, so omitted details leave the active sheet."
          },
          "promote": {
            "basis": "wired",
            "records": [
              "RTE-2",
              "RTE-3"
            ],
            "note": "Curator instructions use usage counts to prioritize frequently used solutions in retained content; no deterministic counter or ranking consumer is implemented."
          }
        },
        "records": [
          "RTE-2",
          "RTE-3",
          "RTE-4",
          "OBJ-7"
        ],
        "note": "The included provider-native retained payload is opaque; interface evidence does not close its internal alternatives. These are wired model-mediated operations, not guaranteed semantic outcomes. Invalidation with an explicit withdrawal/history protocol is not established by wholesale replacement."
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
              "RTE-6"
            ],
            "note": "The benchmark runner explicitly opens an operator-selected seed/checkpoint to obtain retained state; the requesting consumer is the runner, not the generator model."
          },
          "push": {
            "basis": "observed",
            "records": [
              "CLM-4",
              "RTE-2"
            ],
            "note": "Later recorded generator prompts contain the prior sheet supplied automatically; retrieval and whole-history assembly provide further wired push witnesses."
          }
        },
        "records": [
          "RTE-2",
          "RTE-3",
          "RTE-4",
          "RTE-5",
          "RTE-6",
          "RTE-7",
          "RTE-8",
          "CLM-4"
        ],
        "note": "The included provider-native retained payload is opaque; interface evidence does not close its internal alternatives. The ordinary generator has no request-memory tool. Returning loaded state to its requesting runner is not an additional push; later automatic prompt construction is."
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
            "basis": "observed",
            "records": [
              "CLM-4",
              "RTE-2",
              "RTE-5"
            ],
            "note": "Recorded cumulative prompts include the entire current cheatsheet; full-history mode wires all available earlier pairs without relevance filtering."
          },
          "inferred-embedding": {
            "basis": "wired",
            "records": [
              "OBJ-3",
              "RTE-3",
              "RTE-4"
            ],
            "note": "Each new question triggers cosine similarity against previous question vectors and top-k pair delivery."
          },
          "inferred-judgment": {
            "basis": "wired",
            "records": [
              "RTE-3"
            ],
            "note": "Before generator execution, the retrieval-synthesis curator receives earlier memory plus the next question and selects/generalizes useful retained content into the supplied sheet."
          }
        },
        "records": [
          "RTE-2",
          "RTE-3",
          "RTE-4",
          "RTE-5",
          "RTE-7",
          "RTE-8",
          "CLM-4"
        ],
        "note": "The included provider-native retained payload is opaque; interface evidence does not close its internal alternatives. Array indexing realizes embedding selection, not a separate identifier signal. A requested seed path is not identifier-based push."
      },
      "trace_learning": {
        "assessment": "partial",
        "values": [
          "yes"
        ],
        "evidence": {
          "yes": {
            "basis": "wired",
            "records": [
              "RTE-2",
              "RTE-3",
              "RTE-4",
              "RTE-6"
            ],
            "note": "Automatic curator writes turn generator/tool traces into retained cheatsheets that later generator calls consume."
          }
        },
        "records": [
          "RTE-2",
          "RTE-3",
          "RTE-4",
          "RTE-7",
          "RTE-8"
        ],
        "note": "The included provider-native retained payload is opaque; interface evidence does not close its internal alternatives. Raw transcript capture, formatting and retrieval alone do not qualify, but opaque branches cannot erase the supported positive."
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
              "RTE-2",
              "RTE-3",
              "RTE-4"
            ],
            "note": "Curators read problem inputs with generated solution trajectories, including previous examples in retrieval-synthesis."
          },
          "tool-traces": {
            "basis": "wired",
            "records": [
              "RTE-7",
              "RTE-2",
              "RTE-3",
              "RTE-4"
            ],
            "note": "Local execution output is appended to accumulated generator output, which is passed to cumulative/hybrid curation or retained for later retrieval-synthesis."
          }
        },
        "records": [
          "RTE-2",
          "RTE-3",
          "RTE-4",
          "RTE-7",
          "RTE-8"
        ],
        "note": "The included provider-native retained payload is opaque; interface evidence does not close its internal alternatives. The provider path returns text only; complete native tool traces or session logs are not established."
      },
      "learning_scope": {
        "assessment": "partial",
        "values": [
          "cross-task",
          "per-task"
        ],
        "evidence": {
          "cross-task": {
            "basis": "wired",
            "records": [
              "RTE-1",
              "RTE-2",
              "RTE-3",
              "RTE-4"
            ],
            "note": "The benchmark carries learned sheets across distinct independently answered problem inputs; task here means an individual problem, not the dataset name."
          },
          "per-task": {
            "basis": "wired",
            "records": [
              "RTE-2",
              "RTE-12"
            ],
            "note": "Multiple cumulative rounds update and consume the sheet for the same input; the example notebook separately affords explicit same-problem caller repetition."
          }
        },
        "records": [
          "RTE-1",
          "RTE-2",
          "RTE-3",
          "RTE-4",
          "RTE-8",
          "RTE-12"
        ],
        "note": "The included provider-native retained payload is opaque; interface evidence does not close its internal alternatives. Cross-project learning is not established, and a reused container ID does not establish a learning horizon."
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
              "RTE-2",
              "RTE-3",
              "RTE-4"
            ],
            "note": "Cumulative/hybrid updates follow an answer within the benchmark loop; retrieval-synthesis derives guidance before the next answer. Same-problem rounds consume updates immediately."
          }
        },
        "records": [
          "RTE-2",
          "RTE-3",
          "RTE-4",
          "RTE-8"
        ],
        "note": "The included provider-native retained payload is opaque; interface evidence does not close its internal alternatives. Saving/reloading a learned sheet is persistence, not a separate staged learning transformation; embedding production is outside the learning boundary."
      },
      "distilled_form": {
        "assessment": "partial",
        "values": [
          "natural-language",
          "symbolic"
        ],
        "evidence": {
          "natural-language": {
            "basis": "observed",
            "records": [
              "CLM-4"
            ],
            "note": "Derived cheatsheets retain explanations and strategies and appear in later recorded prompts."
          },
          "symbolic": {
            "basis": "wired",
            "records": [
              "OBJ-1",
              "RTE-2",
              "RTE-3",
              "RTE-4"
            ],
            "note": "The connected curator templates expressly produce reusable code snippets and algorithms as cheatsheet content for later generator use."
          }
        },
        "records": [
          "OBJ-1",
          "RTE-2",
          "RTE-3",
          "RTE-4",
          "RTE-8",
          "CLM-4"
        ],
        "note": "The included provider-native retained payload is opaque; interface evidence does not close its internal alternatives. This form axis covers the same curator routes as trace learning, not raw JSON or retrieval vectors merely because they are symbolic."
      },
      "faithfulness_tested": {
        "assessment": "not-determinable",
        "values": [],
        "evidence": {},
        "records": [
          "RTE-9",
          "CLM-4",
          "CLM-5"
        ],
        "note": "Inspected accuracy scoring, illustrative repeated-input calls and retained prompts establish no controlled dependence test. Other stored experiments were not exhaustively assessed; neither yes nor a whole-boundary no is justified."
      }
    }
  }
}
---

# Dynamic Cheatsheet agentic-system analysis

## Run identity

**Run state:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-26-dynamic-cheatsheet-02/run-state.md`

**Generated review:** `kb/agentic-systems/reviews/dynamic-cheatsheet.md`

**Memory analysis report:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-26-dynamic-cheatsheet-02/memory-report.md`

**Memory analysis report SHA-256:** `9feb902e2205a16b737784756c56a997de79f91292a43dd06912da653d3a8083`

Run AAS-2026-09-26-dynamic-cheatsheet-02 opened 2026-09-26. These are intended destinations; run state separately declares publication completion. Fresh specialist input and method hashes matched on integration. No prior Commonplace analysis supplied evidence.

## Boundary and evidence

This code-grounded analysis explains how Dynamic Cheatsheet turns successive model outputs into later problem-solving context, and what controls its execution and reliance. Target is the whole Dynamic Cheatsheet workflow: all six advanced_generate variants, documented caller handoff, shipped benchmark loop, local execution and invoked provider execution. Whole-system refers to this workflow, not every standalone API of the bundled provider client.

Frozen source is https://github.com/suzgunmirac/dynamic-cheatsheet at `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`, default branch resolved 2026-09-26. Code/doctrine show wiring and intent; sampled source-native logs show recorded memory retention/delivery, without proof they were generated by this code revision. No live model experiment was run.

Excluded: independent client chat/web-search APIs not called by this workflow (no whole-client guarantees); provider internals (no isolation, payload, parameter fixity or native-learning completeness); external paper and live dataset/vector generation (no experiment reconstruction or provenance warrant); unsampled source-native experiments (no population estimate or blanket negative about faithfulness). Provider state remains an included opaque boundary object, so supported profile values retain partial coverage rather than silently excluding it. Static prompts and expected targets explain execution but are outside the use-accumulated memory profile. External dependencies include model endpoints, provider SDKs, local Python and packages, benchmark datasets, and imported embeddings.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | Git | `https://github.com/suzgunmirac/dynamic-cheatsheet` | `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9` | implementation | workflow, persistence, extraction, local execution, evaluation, invoked provider calls | `dynamic_cheatsheet/language_model.py:1-668`; `run_benchmark.py:1-327`; `dynamic_cheatsheet/utils/extractor.py:1-115`; `dynamic_cheatsheet/utils/execute_code.py:1-101`; `dynamic_cheatsheet/utils/evaluation.py:1-267`; `text_generation/simple_unified_client.py:395-431,534-583,909-974,1077-1210` | No provider internals or local deployment observed |
| SRC-2 | Git | `https://github.com/suzgunmirac/dynamic-cheatsheet` | `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9` | doctrine/design and attributed performance claims, distinguished on CLM-3 | README and all three prompt templates | `README.md:1-255`; `prompts/generator_prompt.txt:1-81`; `prompts/curator_prompt_for_dc_cumulative.txt:1-149`; `prompts/curator_prompt_for_dc_retrieval_synthesis.txt:1-146` | Intended criticism and gains do not establish semantic success or causal attribution |
| SRC-3 | Git | `https://github.com/suzgunmirac/dynamic-cheatsheet` | `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9` | retained observed artifacts; notebook code illustrates afforded continuation/evaluation | first three cumulative AIME rows, selected notebook cells | `results/AIME_2024/gpt-4o_DynamicCheatsheet_Cumulative.jsonl:1-3`; `ExampleUsage.ipynb:180-195,384-400`; `EvaluatingResults.ipynb:36-83` | Generating revision, complete experimental design and recalled-content dependence are unknown |

Operational access root was `/home/zby/llm/commonplace/related-systems/suzgunmirac--dynamic-cheatsheet`; only full-commit Git blobs/tree/searches supplied evidence. Local worktree and moving HEAD were never evidence. Source quotations below are retained once on their supporting canonical record.

## Shared records

### Components

#### CMP-1

The shared `LanguageModel` client serves both generator and curator; there is no separate critic endpoint. SRC-1 `dynamic_cheatsheet/language_model.py:76-113,411-431`.

Parameter-update conclusion status: uninspected for provider internals; no caller-side weight changes are established by these routes. Model identity conclusion status: wired as caller-provided endpoint/version string, not a weight hash. Generator and curator share the configured endpoint; an exact immutable model version is not guaranteed.

> client_kwargs = {"provider": provider, "model": model_id, "max_retries": 3, "retry_delay": 10}
> --- `dynamic_cheatsheet/language_model.py` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

#### CMP-2

Unidentified producer of imported question vectors. The runner only loads CSV values; neither producer identity nor training/encoding method is established. SRC-1 `run_benchmark.py:201-220`.

Producer identity and parameter fixity conclusion status: uninspected. Runtime cosine ranking is symbolic, not evidence of a second trained model in operation. The code loads imported vectors and does not explain their production.



### Operative objects

#### OBJ-1

Current cheatsheet string: heterogeneous explanatory prose, prescriptive strategies, worked examples and potentially Python snippets. Derived from generator traces or imported from a caller/file; held in caller memory, recorded in JSONL, and supplied as user-message reference/guidance. Counts and source-question tags are prompt conventions rather than checked metadata. SRC-1 `dynamic_cheatsheet/language_model.py:396-445,530-574,610-662`; SRC-2 `prompts/curator_prompt_for_dc_cumulative.txt:45-98`.

Implementation conclusion status: wired. Distinguish parts: explanations and worked mathematical claims are natural-language knowledge; prescriptive strategies are natural-language instruction; executable Python snippets are symbolic content. Item tags, counts and question references are readable text conventions, not an enforced schema. Whole-sheet replacement is the revision unit; content parts are inspectable in prose but do not have code-maintained identities. Rationale inside the sheet reaches later generator or curator context; CLM-4 observes one retained explanation. Full curator deliberation is not saved, so content criticism outside the extracted block need not survive. Template word limit is policy; there is no deterministic item or input-token budget in RTE-2, RTE-3, RTE-4 and RTE-5.

> N.B. Make sure that all information related to the cheatsheet is wrapped inside the <cheatsheet> block. The cheatsheet can be as long as circa 2000-2500 words.
> --- `prompts/curator_prompt_for_dc_cumulative.txt` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

>    - Only include solutions and strategies that have been tested and proven effective.
>    - Clearly state any assumptions, limitations, or dependencies (e.g., specific Python libraries or solution hacks).
> --- `prompts/curator_prompt_for_dc_cumulative.txt` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

> <memory_item>
> <description>
> [Briefly describe the problem context, purpose, and key aspects of the solution.] (Refence: Q1, Q2, Q6, etc.)
> </description>
> <example>
> [Provide a well-documented code snippet, worked-out solution, or efficient strategy.]
> </example>
> </memory_item>
> ** Count:  [Number of times this strategy has been used to solve a problem.]
> --- `prompts/curator_prompt_for_dc_cumulative.txt` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

> N.B. Keep in mind that once the cheatsheet is updated, any previous content not directly included will be lost and cannot be retrieved. Therefore, make sure to explicitly copy any (or all) relevant information from the previous cheatsheet to the new cheatsheet!!!
> --- `prompts/curator_prompt_for_dc_cumulative.txt` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

> - Carefully analyze both the question and cheatsheet before starting
> - Search for and identify any applicable patterns, strategies, or examples within the cheatsheet
> - Create a structured approach to solving the problem at hand
> - Review and document any limitations in the provided reference materials
> --- `prompts/generator_prompt.txt` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

#### OBJ-2

Earlier problem inputs and complete generator outputs. Raw reasoning/code/tool text is distinct from derived OBJ-1. Lists are aligned by index to a corpus, persisted as result fields and reconstructed on resume. Their consumer is full-history formatting, retrieval or retrieval-synthesis, as advisory examples. SRC-1 `run_benchmark.py:176-189,253-280`; `dynamic_cheatsheet/language_model.py:457-574`.





#### OBJ-3

Imported input vectors and their array alignment: numeric access metadata, not solutions or learned parameters. CSV to NumPy arrays, then in-memory cosine ranking of earlier solution pairs. CMP-2 provenance remains unknown. SRC-1 `run_benchmark.py:201-220`; `dynamic_cheatsheet/language_model.py:505-514,593-607`.





#### OBJ-4

Current generator output and extracted final answer. It contains accumulating local code/output text in RTE-7 but only provider-returned text in RTE-8. It becomes raw retained OBJ-2 and curator input, not automatically a verified solution. SRC-1 `dynamic_cheatsheet/language_model.py:174-288,419-423`.

Implementation conclusion status: wired. Distinct operative parts are candidate final answer, explanatory trajectory, generated Python block and returned computation text. Their origins and authority differ: Python can execute in RTE-7, while explanations and answers are model assertions and output text is evidence only for the executed encoded computation. The container is a return structure, not one undifferentiated epistemic object.



#### OBJ-5

Dataset targets and transient answer-evaluation result. Targets are saved beside outputs but not read back into the curator/generator. Current runner does not store the boolean `result` in the output dictionary. Not an operative memory-profile member. SRC-1 `run_benchmark.py:274-309`.

Implementation conclusion status: wired. The expected target is imported natural-language/symbolic answer content; the transient boolean score is symbolic evaluation output. They are separate parts: dataset target can judge the answer, whereas the score only updates a displayed count. Neither is a memory feedback input.



#### OBJ-6

Shipped generator/curator templates, loaded by the caller. Static method inputs outside the memory profile; they define what a generated sheet may contain and how the model is instructed to consume it. SRC-1 `run_benchmark.py:95-100`; SRC-2 `prompts/generator_prompt.txt:1-81`, `prompts/curator_prompt_for_dc_cumulative.txt:1-149`, `prompts/curator_prompt_for_dc_retrieval_synthesis.txt:1-146`.





#### OBJ-7

Provider-native execution state boundary. OpenAI creates a service container and reuses its identifier across benchmark problems; its internal retained payload is not exposed. Claude uses a sentinel enabling per-request native tools, not an established cross-query container. Visible returned text must not stand in for either provider's opaque state. SRC-1 `dynamic_cheatsheet/language_model.py:154-172,212-234`; `text_generation/simple_unified_client.py:1077-1210`.

Canonical amendment: earlier seed combined native sessions too broadly. Replace with two explicitly distinct interfaces: reused OpenAI container versus Claude per-request tool enabling. SRC-1 `dynamic_cheatsheet/language_model.py:154-172,212-234` supports this correction. Affected findings: RTE-8 and every partially covered comparison axis. Payload remains uninspected, and visible text does not classify it.



#### OBJ-8

local recursive execution conversation. Assistant code plus captured subprocess result and a continuation request are appended to the input message list. This is within-problem in-memory history and contributes to durable OBJ-4/OBJ-2 text; the temporary Python file itself is deleted. SRC-1 `dynamic_cheatsheet/language_model.py:249-284`; `dynamic_cheatsheet/utils/execute_code.py:75-101`.





#### OBJ-9

benchmark JSONL checkpoint and argument sidecar, distinct from their embedded content. It stores input/target, step prompts/outputs, current/new/final sheet and selected examples where the branch returns them. The argument sidecar controls resume checks; record position and list length control which problems are skipped and which sheet is restored. SRC-1 `run_benchmark.py:69-78,133-189,227-248,274-309`.





### Routes

#### RTE-1

Each benchmark problem invokes `advanced_generate`, supplies caller state, appends final output to history, saves returned fields and replaces caller sheet. Separate problems establish the cross-task horizon. SRC-1 `run_benchmark.py:231-280`.



>         generator_outputs_so_far.append(output_dict["final_output"])
>
>         outputs.append({
>             "input": current_input,
>             "target": original_target,
>             "raw_input": original_input,
>             **output_dict,
>         })
>         cheatsheet = output_dict["final_cheatsheet"]
> --- `run_benchmark.py` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

#### RTE-2

Cumulative: each round pushes the whole current sheet to the generator, optionally adds prior same-problem answer strings, then curates question + full generator output + old sheet. Extracted sheet replaces current state, is used by the next round/problem and is saved by RTE-6. SRC-1 `dynamic_cheatsheet/language_model.py:386-455`.

Implementation conclusion status: wired. Model-mediated proposal and correctness criticism are requested by OBJ-6; extractor admits any opening cheatsheet block, even without a closing tag. Missing opening tag falls back to old sheet. No independent semantic veto occurs in this route. Operator can choose prompts/state but is not consulted per update. Updated sheet is applied next same-input round or returned to caller for next problem. Rejection/rollback: parser fallback only; no item-level rollback, expiry or invalidation. Curator max output is twice ordinary max_tokens; nominal word budget remains prompt policy. Cumulative max(1,max_num_rounds) repeats the same question. With omitted benchmark curator path the actual template is literal `(empty)`; choosing the variant alone does not wire substantive criticism. All curation-operation classifications require supplying the inspected templates. Source SRC-1 `run_benchmark.py:95-100`; `dynamic_cheatsheet/language_model.py:386-455`; SRC-2 prompts quoted here.

>                 ## STEP 2: Run the cheatsheet extraction model with the generator output and the current cheatsheet
>                 cheatsheet_prompt = cheatsheet_template.replace("[[QUESTION]]", input_txt).replace("[[MODEL_ANSWER]]", generator_output).replace("[[PREVIOUS_CHEATSHEET]]", current_cheatsheet)
>
>                 cheatsheet_history = [{"role": "user", "content": cheatsheet_prompt}]
> --- `dynamic_cheatsheet/language_model.py` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

>                 # Extract the new cheatsheet from the output (if present); otherwise, return the old cheatsheet
>                 new_cheatsheet = extract_cheatsheet(response=cheatsheet_output, old_cheatsheet=current_cheatsheet)
>                 cheatsheet = new_cheatsheet
> --- `dynamic_cheatsheet/language_model.py` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

>                 cheatsheet_output = self.generate(
>                     history=cheatsheet_history,
>                     temperature=temperature,
>                     max_tokens=2 * max_tokens,
>                     allow_code_execution=False,
>                 )
> --- `dynamic_cheatsheet/language_model.py` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

> Before updating the cheatsheet, however, you should first assess the correctness of the provided solution and strategically incorporate code blocks, insights, and solutions into the new cheatsheet. Always aim to preserve and keep correct, useful, and illustrative solutions and strategies for future cheatsheets.
> --- `prompts/curator_prompt_for_dc_cumulative.txt` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

>     if "<cheatsheet>" in response:
>         try:
>             txt = response.split("<cheatsheet>")[1].strip()
>             txt = txt.split("</cheatsheet>")[0].strip()
>             return txt
>         except:
>             return old_cheatsheet
>     else:
>         return old_cheatsheet
> --- `dynamic_cheatsheet/utils/extractor.py` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

>                 # If there are previous answers, add them to the cheatsheet content for the generator
>                 if round_idx > 0 and add_previous_answers_to_cheatsheet:
>                     previous_answers_txt = f"PREVIOUS ANSWERS:\n{'; '.join(previous_answers)}"
>                     generator_cheatsheet_content = f"{generator_cheatsheet_content}\n\n{previous_answers_txt}"
>
>                 generator_prompt = generator_template.replace("[[QUESTION]]", input_txt).replace("[[CHEATSHEET]]", generator_cheatsheet_content)
> --- `dynamic_cheatsheet/language_model.py` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

#### RTE-3

Retrieval-only and retrieval-synthesis: before answering, cosine top-k selection formats earlier pairs. Retrieval-only directly pushes formatted raw history; synthesis also sends that history, the prior sheet and next question to the curator, and pushes its extracted output. Extraction failure falls back to retrieved pairs, not to the previous cumulative sheet. SRC-1 `dynamic_cheatsheet/language_model.py:503-575`.

Implementation conclusion status: wired. Preserve two branches: raw retrieval only formats pairs; retrieval-synthesis also proposes a replacement sheet from current question, previous sheet and selected traces. Selector scans cosine scores, sorts all previous candidates and takes top-k (default 3), reverses delivery order; no correctness predicate or input-token filter. The synthesis model owns content selection and revision; parser owns operational admission with retrieved-pair fallback. Similarity is not warrant. Pre-answer curation supplies inferred-judgment push for this branch only. Guidance, human role, no semantic veto and whole-sheet replacement match RTE-2; missing closing tag is not rejected. No expiry or item withdrawal protocol. Previous sheet still reaches curator even if examples are limited. Source SRC-1 `dynamic_cheatsheet/language_model.py:503-575`.

>             current_original_input_embedding = original_input_embeddings[-1]
>             prev_original_input_embeddings = original_input_embeddings[:-1]
>
>             # Retrieve the most similar k input-output pairs from the previous inputs and outputs
>             if len(prev_original_input_embeddings) > 0:
>                 similarities = cosine_similarity([current_original_input_embedding], prev_original_input_embeddings)
>                 top_k_indices = np.argsort(similarities[0])[::-1][:retrieve_top_k]
>                 top_k_original_inputs = [original_input_corpus[i] for i in top_k_indices]
>                 top_k_original_outputs = [generator_outputs_so_far[i] for i in top_k_indices]
>                 top_k_similar_values = similarities[0][top_k_indices]
> --- `dynamic_cheatsheet/language_model.py` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

>             # For RetrievalSynthesis, run the curator to synthesize a better cheatsheet
>             previous_cheatsheet = cheatsheet
>             if approach_name == "DynamicCheatsheet_RetrievalSynthesis":
>                 cheatsheet_prompt = cheatsheet_template.replace("[[PREVIOUS_INPUT_OUTPUT_PAIRS]]", curated_cheatsheet)
>                 cheatsheet_prompt = cheatsheet_prompt.replace("[[NEXT_INPUT]]", input_txt)
>                 cheatsheet_prompt = cheatsheet_prompt.replace("[[PREVIOUS_CHEATSHEET]]", previous_cheatsheet)
>                 cheatsheet_history = [{"role": "user", "content": cheatsheet_prompt}]
>                 cheatsheet_output = self.generate(
>                     history=cheatsheet_history,
>                     temperature=temperature,
>                     max_tokens=2 * max_tokens,
>                     allow_code_execution=False,
>                 )
>                 new_cheatsheet = extract_cheatsheet(response=cheatsheet_output, old_cheatsheet=curated_cheatsheet)
>                 curated_cheatsheet = new_cheatsheet
> --- `dynamic_cheatsheet/language_model.py` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

> Selective Knowledge Retention:
> - Preserve only high-value strategies, code blocks, insights, and reusable patterns that significantly contribute to problem-solving.
> - Discard redundant, trivial, or highly problem-specific details that do not generalize well.
> - Ensure that previously effective solutions remain accessible while incorporating new, superior methods.
>
> Continuous Refinement & Optimization:
> - Improve existing strategies by incorporating more efficient, elegant, or generalizable techniques.
> - Remove duplicate entries or rephrase unclear explanations for better readability.
> - Introduce new meta-strategies based on recent problem-solving experiences.
> --- `prompts/curator_prompt_for_dc_retrieval_synthesis.txt` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

> 4. Implement a Usage Counter
>    - Each entry must include a usage count: Increase the count every time a strategy is successfully used in problem-solving.
>    - Use the count to prioritize frequently used solutions over rarely applied ones.
> --- `prompts/curator_prompt_for_dc_retrieval_synthesis.txt` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

>             # Add the previous input-output pairs to the cheatsheet (reverse order so most similar is last/closest to the question)
>             for i, (previous_input_txt, previous_output_txt, similarity) in enumerate(zip(top_k_original_inputs[::-1], top_k_original_outputs[::-1], top_k_similar_values[::-1])):
>                 curated_cheatsheet += f"#### Previous Input #{i+1} (Similarity: {similarity:.2f}):\n\n{previous_input_txt}\n\n#### Model Solution to Previous Input  #{i+1}:\n\n{previous_output_txt}\n---\n---\n\n"
> --- `dynamic_cheatsheet/language_model.py` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

#### RTE-4

Hybrid: current sheet plus top-k earlier examples are pushed to generator; current input/output plus the original current sheet then feed post-answer curation. Retrieved examples are not separately passed to this curator, though their influence can appear in generator output. SRC-1 `dynamic_cheatsheet/language_model.py:577-662`.

Implementation conclusion status: wired. Generator receives coarse whole sheet plus embedding-selected examples; one generator call then curator. Proposal guidance is the supplied cumulative template, operational admission uses extractor, veto is only parse fallback, recovery is prior sheet on extraction failure. Returned new sheet is retained and used later. It does not implement cumulative multiple-round loop despite shared max_num_rounds argument. Current sheet goes directly to curator, retrieved examples only through their possible influence on generator output. No expiry/invalidation or independent semantic acceptance. Source SRC-1 `dynamic_cheatsheet/language_model.py:577-662`.



#### RTE-5

Full history: every call formats all previous paired inputs/outputs as `curated_cheatsheet`, pushes them to generator and returns that formatted string. There is no learned derivation or relevance filter in this formatting. SRC-1 `dynamic_cheatsheet/language_model.py:457-501`.

Implementation conclusion status: wired. Source-native variable name curated_cheatsheet denotes deterministic formatting, not learning. Trigger every call, selector all available paired inputs/outputs, consumer generator, channel user message. Immediate formatted return may be saved, but later calls rebuild from raw history. No quality gate, budget filter, expiry or invalidation; learned-curation analysis inapplicable because content is not revised.

>                 top_k_original_inputs = original_input_corpus[:length_of_history]
>                 top_k_original_outputs = generator_outputs_so_far
>
>                 curated_cheatsheet = "### PREVIOUS SOLUTIONS (START)\n\n"
>                 for i, (previous_input_txt, previous_output_txt) in enumerate(zip(original_input_corpus, generator_outputs_so_far)):
>                     curated_cheatsheet += f"#### Previous Input #{i+1}:\n\n{previous_input_txt}\n\n#### Model Solution to Previous Input #{i+1}:\n\n{previous_output_txt}\n---\n---\n\n"
>                 curated_cheatsheet += "#### PREVIOUS SOLUTIONS (END)"
> --- `dynamic_cheatsheet/language_model.py` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

#### RTE-6

Every completed problem rewrites a JSONL checkpoint. At startup, runner requests optional seed file and selected checkpoint; resume restores last non-null `final_cheatsheet` and all `final_output` values, then skips `len(outputs)` problems. Later prompts receive restored content through RTE-2, RTE-3, RTE-4 or RTE-5. This is wired runner pull followed by automatic model push. SRC-1 `run_benchmark.py:69-78,133-189,197-220,227-248,308-315`.

Implementation conclusion status: wired. The runner explicitly requests seed/checkpoint files (pull); automatic prompt supply afterward belongs to other routes (push). Whole JSONL file is rewritten after every example; prior step sheets remain inspectable. Resume selects last non-null final sheet and rebuilds generator outputs by list order, then skips len(outputs). Compatibility check omits no_shuffle, retrieval count, native container and some prompt/model settings; it does not prove restored output/corpus/vector alignment. A changed order setting can misalign them. Native container is created before resume and is not restored from checkpoint. Recovery is best effort, no transaction or effect rollback guarantee. Seed provenance is unchecked. No automatic recovery of omitted older sheet entries or automatic expiry is wired. Source SRC-1 `run_benchmark.py:115-118,133-189,197-248,308-315`.

>         args_keys = ["generator_prompt_path", "temperature", "execute_python_code", "task", "model_name", "approach_name", "max_num_rounds"]
>
>         for key in args_keys:
>             if getattr(args, key) != previous_run_params.get(key):
>                 raise ValueError(f"The provided argument '{key}' is inconsistent with the previous run. Previous value: {previous_run_params.get(key)}, current value: {getattr(args, key)}.")
> --- `run_benchmark.py` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

>     # Initialize the cheatsheet
>     cheatsheet = "(empty)"
>     if args.initialize_cheatsheet_path is not None:
>         with open(args.initialize_cheatsheet_path, "r") as file:
>             cheatsheet = file.read()
>
>     # Initialize the outputs and the generator outputs so far
>     outputs = []
>     generator_outputs_so_far = []
>     if args.continue_from_last_run_path:
>         # Load the previous run
>         with open(args.continue_from_last_run_path, "r") as file:
>             outputs = [json.loads(line) for line in file.readlines()]
>
>         # Load the previous cheatsheet from the last output (if available)
>         last_cheatsheet = outputs[-1].get("final_cheatsheet")
>         if last_cheatsheet is not None:
>             cheatsheet = last_cheatsheet
>
>         generator_outputs_so_far = [output["final_output"] for output in outputs]
> --- `run_benchmark.py` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

#### RTE-7

Generator output ending in a code fence before the execution marker triggers local Python execution. Captured result enters OBJ-8 and accumulated output; recursive generation consumes it. It becomes trace-learning input only when a subsequent curator reads the accumulated output. SRC-1 `dynamic_cheatsheet/language_model.py:249-288`; `dynamic_cheatsheet/utils/execute_code.py:28-59,75-101`.

Implementation conclusion status: wired. Local wrapper detects execution marker after a closed code fence, extracts first Python block, may add print, executes with inherited host process privileges, and returns stdout/stderr into next model call and accumulated transcript. Timeout kills direct process after 3 seconds and deletes temporary file; host isolation and process-tree cleanup are not guaranteed. Execution occurs before the recursion-depth check: default depth 1 and max 3 can execute at depth 4 before returning. Last-round warning is policy, not a denial check. This is static control-flow inference, not observed execution. No human approval per block, no rollback of external effects. Immediate transcript consumption is wired; durable learning occurs only if a curator later consumes the transcript. No independent expiration beyond local call lifetime. Source SRC-1 `dynamic_cheatsheet/language_model.py:249-288`; `dynamic_cheatsheet/utils/execute_code.py:28-101`.

>                 current_output = f"{output_prefix}\n{code_execution_flag}\n\n{executed_code}"
>                 final_output = f"{final_output}\n\n{current_output}".strip()
> --- `dynamic_cheatsheet/language_model.py` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

>                     new_messages = [
>                         {"role": "assistant", "content": current_output},
>                         {"role": "user", "content": f"Proceed with any additional steps required and provide the completed solution. If everything is already complete, type FINAL ANSWER and submit it in the expected format. If you are stuck, please try alternative methods to solve the problem and provide the final solution.{warning_txt}"}
>                     ]
>                     history += new_messages
>                     return self.generate(
>                         history=history,
> --- `dynamic_cheatsheet/language_model.py` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

>     finally:
>         os.remove(temp_file.name)
>
>     return captured_output
> --- `dynamic_cheatsheet/utils/execute_code.py` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

> process = Popen(["python3", temp_file.name], stdout=PIPE, stderr=PIPE)
>         stdout, stderr = process.communicate(timeout=timeout)
> --- `dynamic_cheatsheet/utils/execute_code.py` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

> if current_depth <= max_depth_num_rounds:
> --- `dynamic_cheatsheet/language_model.py` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

#### RTE-8

Native execution flag and configured container/sentinel select provider-native generation. OpenAI requests reference the same created container; Claude requests add a tool definition. Only output text returns to OBJ-4. Selection, retention and transformations within provider state are unknown. SRC-1 `run_benchmark.py:115-118`; `dynamic_cheatsheet/language_model.py:212-234`; `text_generation/simple_unified_client.py:1077-1210`.

Implementation conclusion status: wired at interface only. Operator enables native mode and benchmark initializes service handle; OpenAI ID is reused, Claude sentinel only selects per-request native tool. Native execution branch depends on use_code_interpreter and container_id, independently of allow_code_execution. Native mode disables local execution in advanced_generate. Required external contract is provider tool execution and retention; payload, inner selection, expiry, isolation, effects and recovery remain uninspected. Returned text reaches generator-output/curator path; no full native trace is exposed. No own retention guarantee follows from a reused handle. Source SRC-1 `dynamic_cheatsheet/language_model.py:157-172,212-234,347-349`; `text_generation/simple_unified_client.py:1077-1210`.

>         params: Dict[str, Any] = {
>             "model": self.model,
>             "input": messages,
>             "tools": [{"type": "code_interpreter", "container": container_id}],
>         }
> --- `text_generation/simple_unified_client.py` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

>         def _call():
>             response = self.openai_client.responses.create(**params)
>             return response.output_text
> --- `text_generation/simple_unified_client.py` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

>             # Extract text from content blocks
>             text_parts = []
>             for content_block in response.content:
>                 if content_block.type == "text":
>                     text_parts.append(content_block.text)
>             return "".join(text_parts) if text_parts else ""
> --- `text_generation/simple_unified_client.py` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

#### RTE-9

After generator/curator completion, task-specific answer evaluation updates printed totals. Evaluation is outside the memory adoption loop and does not gate the saved sheet. SRC-1 `run_benchmark.py:274-309`.

Implementation conclusion status: wired. Target is final answer, evaluator is task-specific Python comparison against dataset target or GameOf24 arithmetic/number-use constraints. Model judgment alone is not the oracle; external target provider is loaded dataset. Scoring comes after sheet adoption and has no veto, revision or next-round feedback edge. Current output dictionary retains target but not result boolean. Separate execution surface: GameOf24 and equation balancer use eval on generated expression; disabling generator local code does not disable this evaluator. Result warrants only predicate match in that task domain, not correctness of reasoning, stored strategy or transfer. Immediate printed score; no memory read-back, invalidation or authority to admit future memory. Source SRC-1 `run_benchmark.py:274-315`; `dynamic_cheatsheet/utils/evaluation.py:47-81,102-112,151-170,173-267`.

>         if args.task == "GameOf24":
>             result = eval_for_GameOf24(original_input, final_answer)
>         elif args.task in ["AIME_2025", "AIME_2024", "AIME_2020_2024"]:
>             result = eval_for_exact_matching_with_no_punctuation(final_answer.lower(), original_target.lower())
>         elif args.task in ["GPQA_Diamond", "MMLU_Pro_Engineering", "MMLU_Pro_Physics"]:
>             result = eval_for_multiple_choice(current_input, final_answer, original_target)
>         elif args.task == "MathEquationBalancer":
>             result = eval_equation_balancer(None, final_answer, original_target)
> --- `run_benchmark.py` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

> value = eval(clean_output)
> --- `dynamic_cheatsheet/utils/evaluation.py` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

> if result:
>             correct_so_far += 1
>         total_so_far += 1
> --- `run_benchmark.py` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

#### RTE-10

Default: constructs generator prompt with literal `(empty)` cheatsheet and returns no learned sheet. Local execution can still build within-problem history, and native execution can reference provider state. Consequently no cheatsheet is narrower than no memory whatsoever. SRC-1 `dynamic_cheatsheet/language_model.py:351-384`.

Implementation conclusion status: wired. No sheet update route; empty prompt slot and final_cheatsheet None. Local execution conversation or native execution state can still exist. Terminal answer extraction and output persistence are shared with other branches; no curator admission or learned-sheet read-back. Source SRC-1 `dynamic_cheatsheet/language_model.py:351-384`.



#### RTE-11

external caller/seed authoring affordance. README documents explicit passing and reuse of caller cheatsheet strings and a pre-existing seed path. The caller can author/replace such text; benchmark import is wired, while actual manual authoring is only afforded. No automatic discovery, human editor UI or authenticated provenance check is shown. SRC-2 `README.md:100-120,218-219`; SRC-1 `dynamic_cheatsheet/language_model.py:290-307,323-341`; `run_benchmark.py:170-174`.

Conclusion status: afforded for manual/original authorship; wired only for explicit input acceptance. Caller can replace supplied state, reject returned state, edit a seed, or pass previous result onward. Responsibility horizon ends at return unless caller persists/reuses it. No human edit interface, provenance validator or deployed manual intervention observed. No automatic expiry; caller owns withdrawal and backup. This does not make manual write agency wired.



#### RTE-12

explicit caller repetition of the same problem with newly learned cheatsheet, distinct from cross-problem iteration. Notebook cells 8 and 12 pass unchanged `input_txt` and prior `final_cheatsheet`; an afforded per-task learning continuation. RTE-2 independently wires multiple same-input rounds in code. SRC-3 `ExampleUsage.ipynb:180-195,384-400`; SRC-1 `dynamic_cheatsheet/language_model.py:396-437`.

Conclusion status: afforded for documented repeated-input caller continuation; independent wired per-task witness remains RTE-2. Caller repeats same input and explicitly passes prior returned sheet. No automatic scheduler or separate learned transform here; the existing cumulative route executes. Caller decides retention/rejection, with recovery and termination at its discretion.



### Claims

#### CLM-1

Claim conclusion status: claimed. The README describes persistent evolving inference-time memory and strategies reused without parameter modification. RTE-1, RTE-2, RTE-3, RTE-4 and RTE-6 support explicit state reuse; provider parameter fixity and improved capacity require separate evidence. SRC-2 `README.md:7-21`.





#### CLM-2

Claim conclusion status: claimed. The project claims improvement without ground-truth labels or human feedback. Curator inputs omit benchmark targets, while RTE-9 uses targets for reporting; this bounds the claim to adaptation rather than evaluation. SRC-2 `README.md:20`; SRC-1 `run_benchmark.py:253-309`.



> * **Zero-Shot Learning**: Improves performance without ground-truth labels or human feedback
> --- `README.md` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

#### CLM-3

Claim conclusion status: claimed. README reports gains across mathematics, puzzles, arithmetic and knowledge-intensive tasks. This analysis neither reproduces those gains nor treats the sampled wrong-answer trace as a population estimate. Source-reported improvement is the strongest performance evidence here; component attribution, deployment transfer and criticism-attributable learning remain uninspected. SRC-2 `README.md:23-30`.



> * **Mathematics**: Claude 3.5 Sonnet's accuracy more than doubled on AIME math exams by retaining algebraic insights
> --- `README.md` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

#### CLM-4

Retained evidence: SRC-3 `results/AIME_2024/gpt-4o_DynamicCheatsheet_Cumulative.jsonl:1-3`. Operation conclusion status: `observed`. Row 1 answer 15 differs from target 315 and retains the 15-rectangle rule; row 2's first generator prompt contains the full row 1 final sheet, and row 3's contains the full row 2 final sheet. Explanatory text is present in both retained and later supplied contexts. Current-code provenance and actual model dependence are unestablished.

Coordinator verified row 1 final_answer 15 versus target 315, row 2 and row 3 contain the complete prior final sheet in their first generator_prompt. Row 1 sheet length 2040 characters and explanatory sentence are retained. This is source-artifact inspection, not a new runtime probe or proof of generating revision. Operation conclusion status: observed for persistence and recorded delivery only; activation and resulting error causation remain uninspected.

> "final_answer": "15"
> --- `results/AIME_2024/gpt-4o_DynamicCheatsheet_Cumulative.jsonl` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

> "target": "315"
> --- `results/AIME_2024/gpt-4o_DynamicCheatsheet_Cumulative.jsonl` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

> Thus, the total number of rectangles is 15.
> --- `results/AIME_2024/gpt-4o_DynamicCheatsheet_Cumulative.jsonl` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

> This formula excludes the edges of the polygon and self-connections.
> --- `results/AIME_2024/gpt-4o_DynamicCheatsheet_Cumulative.jsonl` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

#### CLM-5

Bounded evidence assessment: SRC-2 `README.md:23-28`; SRC-3 `ExampleUsage.ipynb:180-195,384-400`, `EvaluatingResults.ipynb:36-83`. Repeating the same problem and reporting correctness is illustrative evidence; benchmark aggregation scores answers. None of these inspected surfaces establishes a controlled recalled-content dependence test. Other retained experiments were not exhaustively tested, so faithfulness remains not determinable.

Conclusion status: uninspected for a whole-boundary faithfulness experiment. Inspected notebooks and scoring code are not a recalled-content intervention/comparison. Their code and example repetition afford evaluation but do not establish actual dependence on recalled material. No global absence claim over all results is made.



### Evidenced absences

None asserted as global absences. Negative controls and unknowns are scoped on the admitting route and limitations. In particular unsampled logs and opaque provider execution prevent blanket absent classifications.

### Behavioral-authority paths

| ID | Consumer | Channel | Force | Horizon and evidence |
|---|---|---|---|---|
| BAP-1 | generator | user-message cheatsheet slot | advisory knowledge plus model-mediated instruction, not enforcement | one call, repeated across same-input rounds and independent problems by RTE-2, RTE-3, RTE-4, RTE-5; wired, with recorded delivery observed in CLM-4; SRC-1 `dynamic_cheatsheet/language_model.py:396-418,457-627` |
| BAP-2 | curator | user-message old sheet, question and trajectories | proposal/criticism instruction from static template, retained sheet supplies guidance | one revision, resulting text may outlive it via RTE-6; wired; SRC-1 `dynamic_cheatsheet/language_model.py:422-435,530-544,630-641` |
| BAP-3 | retrieval selector | numeric arrays | executable ranking | current top-k context selection, not truth warrant; wired; SRC-1 `dynamic_cheatsheet/language_model.py:505-524,593-607` |
| BAP-4 | local executor or remote tool | model-generated Python/local marker or provider tool request | local execution permission under caller grant, remote authority under provider contract | immediate effects, no effect rollback; wired interface, deployed isolation uninspected; SRC-1 `dynamic_cheatsheet/language_model.py:212-284` |
| BAP-5 | reporting runner | task-specific boolean result | updates printed correctness totals only | current experiment, no memory admission veto; wired; SRC-1 `run_benchmark.py:290-309` |

## Runtime account

An operator chooses task, model, prompt files, variant and execution settings. The runner loads a dataset, recreates its order (seed 10 unless no_shuffle), optionally restores state, and iterates problems. Each call receives current question and relevant old sheets/outputs. A configured generator proposes a solution; optional local or remote code execution supplies computational output. Depending on variant, curator runs before or after generation. The wrapper returns final answer, output and memory; the runner adopts the sheet, evaluates the answer, records results and advances. SRC-1 `run_benchmark.py:81-118,124-280,290-327` supplies this progression.

The Python caller owns scheduling and state; model roles own generated content, not next-step dispatch. There is no per-question human admission decision. External direct callers own state beyond return; the README demonstrates explicitly returning the previous final sheet. Model identity is configured endpoint text, output identity is timestamp/path and list position. Coordination is sequential. Generator/curator communicate through returned strings and prompts, not autonomous delegation. Provider failures retry three times with ten-second waits then raise; persisted checkpoint permits selected restart but cannot roll back executed effects. SRC-1 `dynamic_cheatsheet/language_model.py:91-113`; `text_generation/simple_unified_client.py:395-431`.

Material alternate paths are all represented: empty-sheet default RTE-10; full-history RTE-5; raw retrieval and retrieval-synthesis branches RTE-3; hybrid RTE-4; caller/seed RTE-11; repeated-input RTE-12; checkpoint RTE-6; local RTE-7 and provider-native RTE-8. Context selection, immediate return, later read-back, expiry and recovery are recorded on those routes. No delegated worker exists in this workflow; provider visibility ends at request/returned text and remains explicitly opaque.

The automatic proposal/admission path is bounded experiment or caller-invoked problem solving, not an open-ended autonomous service. Improvement is triggered by another answer or next-question synthesis. Human chooses methods and inputs; computation generates, criticizes under prompts, parses, replaces, persists and selects successor context. No supplied answer oracle reaches curator; benchmark targets and GameOf24 constraints belong to RTE-9 reporting. Model opinion alone is not an answer oracle. The curator may decline changes in its text, but parser has no semantic veto; caller can reject a returned sheet outside automatic runner progression.

Guarantee owner and scope: local code permission gate belongs to LanguageModel.generate; it covers marker-triggered local execution, not RTE-9 eval or native tool execution. The three-second timeout belongs to subprocess.communicate, not all descendants or provider work. Whole-sheet fallback belongs to extractor and only protects missing opening block/extraction exceptions, not wrong content. Prompt word budgets, correctness requests and last-round warnings are policies, not invariants. Provider-side isolation/persistence requires an external contract not inspected here. Current grant set is configured flags and process/API credentials; actual deployment isolation is uninspected. This separates executable capability from a particular operator's grant.

Three forcing cases were inspected statically: missing/malformed curator tags; code execution at the recursion boundary; disabled generator execution with benchmark eval still enabled. Resume-order mismatch was also traced through RTE-6. Conditional source paths directly establish the limited controls; live API probes would add stochastic execution without settling these code facts. No dynamic check planned. No target checks were attempted; source inspection/validation is not a runtime probe.

Theory-route guidance and conditions 1–4, separately from memory normalization:

| Property | Conclusion status | Evidence and boundary |
|---|---|---|
| Condition 1, localized content | observed | CLM-4 retains an explicit mathematical strategy and rationale as text in OBJ-1; entire sheet is a content-carrying unit, with readable sections/items but no enforced claim identities |
| Condition 2, consumption through what it says | wired | RTE-2, RTE-3 and RTE-4 pass content under instructions to inspect/apply strategies, BAP-1; CLM-4 observes delivery, not actual semantic activation |
| Condition 3, content-directed criticism with revision or changed reliance | wired | intended templates instruct correctness assessment, limitations and replacement by better strategy; connected curator produces replacement sheet. This is a wired model-mediated attempt, not observed formulated successful criticism; wrong retention in CLM-4 prevents treating it as a reliable gate |
| Condition 4, kept criticism result shapes later round | wired | RTE-2, RTE-3 and RTE-4 retain the proposed revised sheet for later consumption and RTE-6 persists it; attribution of a particular retained edit to actual criticism remains uninspected |
| Persistence | observed | CLM-4 shows sheet and explanation carried across distinct problems; RTE-2 wires same-problem rounds and RTE-6 wires cross-run resume. Curator reasoning outside extracted sheet is not retained |
| Addressability | observed | readable strategy/explanation text in CLM-4; program treats entire sheet as replaceable unit. Prompt item labels afford finer organization but not independent identity/history |
| Learning | claimed | CLM-3 source-reported improved task performance is positive but not attributed by inspected comparison to criticism of a consumed theory. Current wiring and trace_learning classification alone cannot establish improved capacity |
| Reflective operation | wired | generated descriptions of own problem-solving enter later method selection through BAP-1 and BAP-2; behavior can change recorded content and content is supplied to later behavior. Actual causal activation remains uninspected |
| Reflective theory-builder qualifier | uninspected | static curator/generator method templates are not shown undergoing their own criticism/revision; the reflected problem-solving strategy is not the entire builder method |
| Autonomous internal operations | wired | after human task/model/template choice, generator, curator, parser, state successor and benchmark scheduler are computational within this workflow; provider internals remain excluded |
| Self-improvement | claimed | source reports better subsequent problem-solving; memory rewriting and later use are wired and sampled delivery observed, but benefit attributable to these changes is not established here |

This supports a wired theory-building pathway under the inspected prompt configuration, with its candidate content and delivery observed. It does not establish an observed complete criticism episode or observed learning. Each status above applies to its own condition, not its neighbors.

## Lens scoping

### Memory/context scope

Trigger evidence: SRC-1, SRC-2 and CLM-1. Full depth: use-accumulated OBJ-1, OBJ-2, OBJ-3, OBJ-7, OBJ-8 and OBJ-9, through RTE-1, RTE-2, RTE-3, RTE-4, RTE-5, RTE-6, RTE-7, RTE-8, RTE-11 and RTE-12. OBJ-4 becomes trace input. All variants, seed/import and opaque native execution remain accounted for; OBJ-5 and OBJ-6 are excluded from memory values as targets/static methods. Curated retained context is the system's central mechanism, warranting full rather than brief depth.

### Epistemic scope

Trigger evidence: curator verified-solution language in SRC-2, CLM-2, CLM-3 and the model/execution/scoring routes in SRC-1. Full depth over solution/strategy production, criticism, retention, answer checking and operational admission in RTE-2, RTE-3, RTE-4, RTE-6, RTE-7, RTE-8 and RTE-9, with contextual selection through RTE-5 and RTE-11. OBJ-1, OBJ-2, OBJ-3, OBJ-4, OBJ-5, OBJ-6, OBJ-7, OBJ-8 and OBJ-9 are disposed below individually. Provider content remains bounded as unknown. Strong accuracy claims and explicit criticism instructions require full warrant analysis.

## Lens outputs

### Memory/context lens

The fresh specialist inventoried caller-held sheets, raw outputs, vector access metadata, checkpoints and local/provider execution state. Its adopted canonical records preserve all substantive distinctions: automatic curator writes versus raw history formatting, post-answer versus pre-answer synthesis, same-problem rounds versus independent problem succession, explicit file pull versus automatic model push, and direct caller affordances versus code wiring. CLM-4 provides a narrow observed retention/delivery witness. Actual dependence and benefit remain separate.

The integrated profile preserves each value's basis. Manual authoring and authored lineage remain afforded at RTE-11; automatic state import does not strengthen them. Observed files/prose/push have CLM-4 witnesses; code/native interfaces and model-mediated curation remain wired. Prompt-supplied curation intends consolidation, deduplication, evolution, synthesis, forgetting and salience promotion, without guaranteeing each semantic operation succeeds. Raw history and retrieved-pair formatting do not qualify as trace learning. Curation must use the intended templates: the runner's absent curator-path default is `(empty)`.

RTE-2 and RTE-4 derive guidance after answers; RTE-3 synthesis derives it before next answer using old traces and sheet. These trace-fed writes all have later consumers and checkpoint retention. They support trajectories/tool-traces, online timing, per-task and cross-task scopes, and natural-language/symbolic distilled content. RTE-7 contributes tool traces when curator consumes accumulated output; raw continuation alone is not another derived-memory route. Imported vectors do not establish offline learning; checkpoint reload does not create staged learning. Opaque native state prevents complete coverage of these axes while preserving supported positives.

For push, current sheet/all history select coarsely at each generator call; current/prior vectors select top-k earlier pairs automatically; pre-answer synthesis uses model judgment with next question to select/regenerate retained guidance. None is an identifier signal merely because array indices or question references exist. Runner-selected seed/checkpoint requests are pull. No generator memory-request tool is wired in inspected paths. Retention/rationale availability are observed, faithful activation is not determinable from selected logs/notebooks, and no uninspected global negative is substituted.

### Epistemic lens

The invoked epistemic procedure is applied as six sparse blocks over canonical records.

**1. Source-and-claim boundary.** SRC-1 implementation, SRC-2 doctrine/reported claims and SRC-3 retained candidates share the full pin. Question: which checks warrant reliance on answers and future strategies? Material families are acquisition, generation/criticism, execution, selection, operational admission, persistence and scoring. Independent provider internals and unsampled experiments are unassessed; CLM-1, CLM-2 and CLM-3 retain the relevant claims.

**2. Epistemic-object inventory.** OBJ-1 has explanatory claims, prescriptions and code as separately described parts; OBJ-2 contains raw prior assertions/trajectories; OBJ-3 is numeric selection metadata; OBJ-4 separates current answer, explanation, executable code and computation output; OBJ-5 separates external target and transient evaluation; OBJ-6 is static procedural guidance; OBJ-7 is opaque native payload; OBJ-8 is local conversation; OBJ-9 is serialization/access structure. Their generic identities and sources remain on the shared records, not redefined here. Generated truth claims do not inherit truth from their storage field or model fluency.

**3. Authority-route ledger.** All implemented rows below have architectural status `implemented`; provider internal checks remain `not determinable`. Observed candidate states are separately handled in block 4.

| Route/function | Target and content relation | Evaluator/condition, timing and result | Epistemic license | Operational and behavioral force | Evidence and mismatch |
|---|---|---|---|---|---|
| RTE-2, RTE-3 synthesis, RTE-4: content transformation | OBJ-1 strategies; intended ampliative conjecture plus reshaping, individual semantic preservation may be indeterminate | same model under curator prompt before/after answer; outputs replacement text | proposed generalization, no independent truth acceptance | creates successor proposal, BAP-2 | SRC-1 `dynamic_cheatsheet/language_model.py:422-435,530-544,630-641`; CLM-1 and CLM-2; verified-solution rhetoric exceeds semantic gate |
| RTE-2, RTE-3 synthesis, RTE-4: check/evidence production | correctness/usefulness of existing solutions and strategies | curator instruction requests criticism; local execution disabled for curator; model opinion may revise content | judgment only, not external oracle | influences proposed replacement, BAP-2 | SRC-2 curator quotes on RTE-2, RTE-3; actual criticism transcript not retained |
| RTE-2, RTE-3 synthesis, RTE-4: operational admission | OBJ-1 text; no further content change | extractor opening-tag split or fallback | no correctness license | becomes active successor, BAP-1; no semantic veto | SRC-1 `dynamic_cheatsheet/utils/extractor.py:62-86`; CLM-4 shows wrong retention |
| RTE-3, RTE-4, RTE-5: operational selection/consumption | OBJ-2 examples and OBJ-3; no semantic content change before synthesis | cosine top-k or all prior pairs on new call | similarity/availability only | supplies generator or curator context, BAP-1, BAP-3 | SRC-1 `dynamic_cheatsheet/language_model.py:457-627`; does not rank correctness |
| RTE-6: retention | OBJ-1, OBJ-2 via OBJ-9; serialization reshapes, no new truth | after completed example | preserves assertions with original unknown warrant | persistence and later resume, no acceptance | SRC-1 `run_benchmark.py:69-78,308-315` |
| RTE-6: lineage/freshness/recovery | imported seed/history, acquisition/import | requested files and partial argument equality at startup | source text preserved; alignment not guaranteed | restores successor context, BAP-1 | SRC-1 `run_benchmark.py:133-220`; no_shuffle mismatch remains possible |
| RTE-7: check/evidence production | OBJ-4 encoded calculation; executable derivation within Python domain | local interpreter output or exception on model request | result of encoded calculation, not warrant for original premises or applicability | returned to continued solver, BAP-4 then BAP-1 | SRC-1 `dynamic_cheatsheet/utils/execute_code.py:28-101`; model selects interpretation |
| RTE-8: operational execution | OBJ-7 and output text, internal content transformation indeterminate | provider tools when native flag/handle selected | unknown inner warrant | provider effects, returned text to solver, BAP-4 | SRC-1 `text_generation/simple_unified_client.py:1077-1210`; remote protocol uninspected |
| RTE-9: check/evidence production | OBJ-4 final answer against OBJ-5 target/predicate; derived boolean | deterministic task evaluator after sheet adoption | match to benchmark reference/constraint, no reasoning or transfer license | creates report result, BAP-5 | SRC-1 `run_benchmark.py:290-299`; CLM-2 narrowed to learning inputs |
| RTE-9: operational reporting | OBJ-5 score; no content change to strategy | boolean increments counter | no additional license | display only, no gate or successor feedback | SRC-1 `run_benchmark.py:301-309` |

**4. Per-object lifecycle disposition.** OBJ-1 contains a sampled mathematical claim extending a solution into a reusable strategy; its generalization is an ampliative candidate, while other sheet parts can reshape input. Observation and conjecture architecture are implemented through RTE-2, RTE-3 and RTE-4; sampled candidate state is `phase evidenced` for existence and recorded retention, not proof of current-code provenance. Consequence derivation and content-directed criticism are model-mediated; candidate state `not determinable` for a criticism episode because curator reasoning is unavailable. Candidate correctness acceptance architecture is `not determinable` at model judgment and no independent route is found in extractor/runner boundary; candidate acceptance state `not determinable`. Its operational retention and subsequent prompt delivery are `phase evidenced` by CLM-4. Post-acceptance lifecycle integration is `not determinable`, because no acceptance decision licenses this claim for a stated scope; retention is not relabelled integration.

OBJ-2: acquisition/import and formatting; discovery lifecycle not applicable. Warrant of source solutions is unknown and can be wrong (CLM-4). OBJ-4: transformation indeterminate between checked derivation and model conjecture, depending particular explanation; the sampled final-answer artifacts do not prove that all reasoning is warranted. RTE-7 can test encoded computations; RTE-9 can judge final answer, with no license for reasoning. OBJ-5 target: acquisition/import; score: symbolic predicate derivation under evaluator semantics, not broader truth warrant; discovery lifecycle not applicable. OBJ-3: no candidate truth-apt output for numeric access metadata; relevant route RTE-3, RTE-4 ranking. OBJ-6: no generated candidate lifecycle for static procedural instructions; they guide RTE-2, RTE-3, RTE-4. OBJ-7: contents and transformations indeterminate, so no complete epistemic object classification; RTE-8 interface cannot settle its lifecycle. OBJ-8 and OBJ-9: retention/serialization of constituent assertions already disposed under OBJ-1, OBJ-2 and OBJ-4; no new ampliative claim solely from conversation append or checkpoint creation.

**5. Claim versus route comparison.** CLM-1 has wired state reuse plus observed historical retention/delivery (CLM-4), no guaranteed activation. CLM-2 matches absence of target in curator inputs, while independent benchmark evaluation explicitly has an answer oracle. CLM-3 retains source-reported gains, but sampled traces and notebook aggregation do not reproduce a controlled comparison or isolate criticism, code tools, extra calls and memory. No causal support is claimed for those performance explanations.

**6. Bounded conclusion.** The workflow acquires prior outputs, proposes generalized guidance, requests criticism, replaces text and supplies it to later problem-solving. None of this alone licenses retained claims as accepted knowledge. Executed calculations and benchmark matches have their own narrow scopes. The observed wrong-answer retention is a direct counterexample to guaranteed filtering in the recorded run, not a proof that all guidance is false or learning is impossible. Criticism-attributable capacity improvement, faithful recalled-content use and provider-native warrant remain unresolved.

## Reconciliation

| Specialist proposal | Accepted canonical record | Disposition |
|---|---|---|
| MEM-OBJ-1 | OBJ-8 | local recursive conversation separated from learned sheet and raw cross-problem history |
| MEM-OBJ-2 | OBJ-9 | checkpoint/argument structure separated from embedded content |
| MEM-RTE-1 | RTE-11 | manual authoring remains afforded, automatic import separately wired |
| MEM-RTE-2 | RTE-12 | explicit same-problem caller continuation afforded; RTE-2 remains wired witness |
| MEM-CLM-1 | CLM-4 | sampled mistaken-solution retention and later prompt delivery accepted at observed layer, generating revision unknown |
| MEM-CLM-2 | CLM-5 | faithfulness not determinable; no exhaustive negative promoted |

All exact identifier tokens were mapped once. No ID changed referent. OBJ-7 amendment preserves OpenAI handle reuse versus Claude per-request tool enabling. OBJ-5 amendment separates saved target from transient unsaved score; no feedback edge was invented. RTE-3 retains raw and synthesized branches and previous-sheet input, with retrieved-pair fallback; RTE-5 is formatting. RTE-6 preserves ordering/alignment and native-session recovery limits. The template-dependent curation caveat is attached to RTE-2 and the profile interpretation. Rationale can survive inside sheet; criticism outside it need not. All nine specialist integration issues are resolved by these canonical records; none requires a stronger status or a new input boundary.

Memory owns comparison classifications and memory revisions; baseline owns external execution/control and epistemic overlay. Parent independently traced scoring before report receipt, agreeing with specialist that evaluation is not admission; this is limited independent convergence on that route, not semantic clearance of the full profile. No other independent agreement is inferred from shared sources.

## Bounded synthesis

Dynamic Cheatsheet implements caller-owned iterative context: solve, propose a replacement cheatsheet, retain it, and supply it to another round or problem. Retrieval adds automatic selection of earlier problem/solution pairs, and retrieval-synthesis generates guidance before answering. Full-history and raw-retrieval variants keep earlier outputs without automatic distillation. The executable design is small and largely sequential; generator and curator share a provider endpoint, while Python controls the loop.

Its strongest inspected operational contribution is concrete retained context across problems, including explanatory text. Source-native records show a previous sheet in the next prompt. Source-reported benchmark improvements are positive performance claims, but this analysis does not independently establish their causal source. The same retained record demonstrates a wrong solution surviving curation, so semantic screening remains model-mediated. Test-time trace learning is wired as retained derived guidance; improved capacity attributable to criticism remains a separate claimed outcome.

For a sequential experiment using supplied templates, memory update and reuse require little machinery. For correctness-sensitive retained strategies, extractor success and model confidence supply no independent warrant; benchmark correctness is reported after adoption. For resumed or remote-execution scenarios, restored files do not reproduce input alignment or native service state automatically. Local execution flags and timeouts are scoped controls; provider tools and benchmark eval are different effect paths.

The four theory-builder conditions have a wired path, with localized content and retention observed; actual content-directed criticism and causal activation remain uninspected at instance level. Reflection on prior problem-solving and computational internal progression are wired independently of that evidence gap. Reflection on the builder's own static method texts is uninspected. Self-improvement and learning retain claim status for benefits beyond the inspected retention/reuse mechanism; none is inferred solely from a changing sheet.

A recorded criticism that identifies a strategy error, changes or re-tests it and supplies the surviving result to later use would strengthen the theory-path finding. A controlled recalled-content intervention with retained traces and matched tools/call budgets would strengthen activation and benefit claims. Provider payload/lifecycle evidence would close partial profile axes. A semantic admission gate or verified resume alignment would change the corresponding architecture assessment. These are evidence/system changes that would alter conclusions, not adoption recommendations.

## Limitations

| Limitation | Affected IDs | Inspected boundary | Conclusion prevented | Resolving evidence |
|---|---|---|---|---|
| Opaque provider weights and state | CMP-1, OBJ-7, RTE-8 | request interfaces and returned text | exact parameter fixity, native memory completeness, isolation and learning routes | pinned provider contract plus inspectable payload/operation traces |
| Imported vector production unknown | CMP-2, OBJ-3 | CSV loader/alignment | embedding provenance, training or offline-learning classification | immutable production artifacts |
| Historical sample only | SRC-3, CLM-4, CLM-5 | three AIME records and selected cells | current-code provenance, population accuracy and whole-corpus faithfulness negative | provenance-bound broader retained experiments |
| No controlled performance/activation comparison | CLM-3, CLM-5, BAP-1 | README claims and sampled delivery | criticism-attributable learning or individual recalled-content effect | controlled intervention with full design/trace evidence |
| Model-mediated criticism and template dependence | OBJ-1, OBJ-6, RTE-2, RTE-3, RTE-4 | prompt calls and extracted text | guaranteed filtering, per-entry curation success or complete observed theory-building episode | retained critic output, explicit content-directed test and later uptake |
| Resume alignment/native restoration incomplete | RTE-6, OBJ-9 | selected argument checks and recreated corpus | equivalent resumed execution | aligned versioned corpus/options and service recovery evidence |
| Host/provider deployment uninspected | RTE-7, RTE-8, RTE-9 | executable effect paths | actual operational grant/isolation or effect rollback | inspected deployment and runtime evidence |

## Verification and blockers

### Semantic verification

Checked profile scope against OBJ-1, OBJ-2, OBJ-3, OBJ-7, OBJ-8, OBJ-9 and all six variants. Opaque native payload remains included and prevents complete aggregate coverage; visible text does not classify it. Static templates and scoring are context, not counted memory. Per-value witnesses preserve observed historical delivery, wired automatic routes and afforded manual authoring separately. No axis-level basis substitutes for value-level evidence.

Checked trace-fed writes RTE-2, RTE-3 synthesis, RTE-4 with source/horizon/timing/form; raw RTE-3 retrieval, RTE-5 formatting and RTE-7 continuation do not become independent learned transforms. RTE-7 tool output feeds qualifying curators; RTE-8 hidden transformations remain unknown. Same-input rounds justify per-task, independent problem progression cross-task, both online; checkpoint import and vector production do not justify staged/offline learning. Distilled symbolic form refers to prompted code snippets, not merely JSON metadata.

Checked push consumers/triggers/selector inputs/selected parts in RTE-2, RTE-3, RTE-4 and RTE-5. Coarse whole-sheet/history, embedding top-k and pre-answer model judgment remain distinct; requested file load is pull and no identifier-based push is inferred. Source amendments preserve identities. Canonical records carry quotes once and overlays reference them. Coordinator rechecked CLM-4 pinned row values and complete-sheet carry-forward. Claim-level improvement remains separate from wiring, observed artifacts and causality. No material semantic conflict remains unresolved; partial/unknown coverage is explicit.

### Deterministic validation

Validation target: `kb/reports/state/agentic-system-analysis/AAS-2026-09-26-dynamic-cheatsheet-02/result.md`. `commonplace-validate --full` passed cleanly: schema, canonical references, all fourteen per-value comparison axes and quote-anchor structure. Publication separately checks exact quoted source text against the frozen source.

### Blockers

None.
