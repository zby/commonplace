---
{
  "type": "agentic-system-analyses/types/agentic-system-memory-profile.md",
  "description": "OpenRSI memory profile of retained experiment journals, derived guidance, program stores and operator-training inputs at the frozen OpenMLE release.",
  "run-id": "AAS-2026-10-19-openrsi-4f870183cadd-01",
  "source-identity": "https://github.com/FrontisAI/OpenRSI",
  "reviewed-boundary": "71ae803a035d5e3b78c19fa49ed9f67d0550cbaa",
  "memory-comparison": {
    "version": 2,
    "scope": "Accumulated Gym preparation code/feedback and generated package artifacts; Evo journals, cards, strategy aggregates, separate summary caches and later operator selection; SFT/RL program databases, retained rollout/message datasets, derived experience and training-output parameters, including opaque external training/serving handoffs. Included but unresolved: Evo-local alternate database callers, full Gym metadata/package/report lifecycle, SFT alternative variants, RL helper/history-cache/restore paths and initial/replacement corpus or parameter provenance. Excludes shipped static skills/prompts/configuration as accumulated memory, unrelated runtime storage/permissions and fixed inference-provider internals not changed through these use paths. No exercised training-to-Evo deployment chain is assumed.",
    "axes": {
      "storage_substrate": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Evo journal, cards, board and rich-summary objects and checkpoints",
            "assessment": "known",
            "findings": [
              {
                "value": "in-memory",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-journal",
                  "memory.md#mem-obj-experience-card",
                  "memory.md#mem-obj-strategy-board",
                  "memory.md#mem-obj-rich-summary",
                  "memory.md#mem-rte-experience-cycle"
                ],
                "note": "Journal nodes and attached card/summary dictionaries retain search experience between invocations."
              },
              {
                "value": "files",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-journal",
                  "memory.md#mem-obj-experience-card",
                  "memory.md#mem-obj-strategy-board",
                  "memory.md#mem-obj-rich-summary",
                  "memory.md#mem-rte-experience-cycle"
                ],
                "note": "Journal JSONL, card JSON/JSONL, board JSON and node-keyed summary cache persist the corresponding parts."
              }
            ],
            "records": [
              "memory.md#mem-obj-journal",
              "memory.md#mem-obj-experience-card",
              "memory.md#mem-obj-strategy-board",
              "memory.md#mem-obj-rich-summary",
              "memory.md#mem-rte-experience-cycle"
            ],
            "note": "These named objects have explicit in-process and filesystem representations; separate caches are retained, not folded into journal-only recovery."
          },
          {
            "scope": "SFT and RL program stores, demonstration datasets and durable rollout logs",
            "assessment": "known",
            "findings": [
              {
                "value": "sqlite",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-sft-programs",
                  "memory.md#mem-obj-sft-messages",
                  "memory.md#mem-obj-rl-programs",
                  "memory.md#mem-rte-sft-reuse"
                ],
                "note": "SFT and RL ProgramDatabase rows persist programs, feedback and selection metadata."
              },
              {
                "value": "files",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-sft-programs",
                  "memory.md#mem-obj-sft-messages",
                  "memory.md#mem-obj-rl-programs",
                  "memory.md#mem-rte-sft-reuse"
                ],
                "note": "JSONL/Parquet datasets and durable result files retain messages and rollout evidence."
              },
              {
                "value": "in-memory",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-sft-programs",
                  "memory.md#mem-obj-sft-messages",
                  "memory.md#mem-obj-rl-programs",
                  "memory.md#mem-rte-sft-reuse"
                ],
                "note": "Training samples hold the message-derived token and mask representations."
              }
            ],
            "records": [
              "memory.md#mem-obj-sft-programs",
              "memory.md#mem-obj-sft-messages",
              "memory.md#mem-obj-rl-programs",
              "memory.md#mem-rte-sft-reuse"
            ],
            "note": "Inspected databases are distinct implementations; finalized messages and result logs have separate file persistence."
          },
          {
            "scope": "SFT training output checkpoints",
            "assessment": "known",
            "findings": [
              {
                "value": "files",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-cmp-sft-model"
                ],
                "note": "Training targets numerical checkpoint files under the configured output directory."
              },
              {
                "value": "model-weights",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-cmp-sft-model"
                ],
                "note": "The retained actor parameters are distributed numerical model state, not the text dataset encoding."
              }
            ],
            "records": [
              "runtime.md#rt-cmp-sft-model"
            ],
            "note": "Checkpoint storage and distributed parameter content are both recorded; an exact later endpoint installation is not."
          },
          {
            "scope": "RL actor/serving retained state and external provider storage",
            "assessment": "uninspected",
            "findings": [],
            "records": [
              "runtime.md#rt-cmp-rl-model",
              "runtime.md#rt-bap-training-parameters"
            ],
            "note": "The component establishes distributed parameters and integration, but exact optimizer/serving persistence and storage organization are uninspected."
          },
          {
            "scope": "Evo-local alternate database, Gym package lifecycle and remaining RL cache/restore surfaces",
            "assessment": "uninspected",
            "findings": [],
            "records": [
              "memory.md#mem-obj-journal",
              "runtime.md#rt-rte-gym-build",
              "memory.md#mem-rte-rl-reuse"
            ],
            "note": "The memory coverage inventory leaves Evo-local callers, full package maintenance and RL history/cache lifecycle uninspected. A filename or API label does not establish the operative substrate of every included part."
          }
        ],
        "records": [
          "memory.md#mem-obj-journal",
          "memory.md#mem-obj-experience-card",
          "memory.md#mem-obj-strategy-board",
          "memory.md#mem-obj-rich-summary",
          "memory.md#mem-rte-experience-cycle",
          "memory.md#mem-obj-sft-programs",
          "memory.md#mem-obj-sft-messages",
          "memory.md#mem-obj-rl-programs",
          "memory.md#mem-rte-sft-reuse",
          "runtime.md#rt-cmp-sft-model",
          "runtime.md#rt-cmp-rl-model",
          "runtime.md#rt-bap-training-parameters",
          "runtime.md#rt-rte-gym-build",
          "memory.md#mem-rte-rl-reuse"
        ],
        "note": "Files, process objects, SQLite and model weights are supported locally. Opaque serving state and untraced alternative lifecycle surfaces prevent complete storage classification; repository location of shipped code is not itself a repo memory finding."
      },
      "representational_form": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Retained plans, analysis, logs, summary fields and message text at model/training-input consumers",
            "assessment": "known",
            "findings": [
              {
                "value": "natural-language",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-journal",
                  "memory.md#mem-obj-experience-card",
                  "memory.md#mem-obj-rich-summary",
                  "memory.md#mem-obj-sft-messages",
                  "memory.md#mem-obj-sft-programs",
                  "memory.md#mem-obj-rl-programs"
                ],
                "note": "Plans, feedback and comparative summaries supply interpreted content to later consumers."
              }
            ],
            "records": [
              "memory.md#mem-obj-journal",
              "memory.md#mem-obj-experience-card",
              "memory.md#mem-obj-rich-summary",
              "memory.md#mem-obj-sft-messages",
              "memory.md#mem-obj-sft-programs",
              "memory.md#mem-obj-rl-programs"
            ],
            "note": "Readable text is classified independently of the symbolic wrapper and the later token encoding."
          },
          {
            "scope": "Retained code, identities, metrics, cards/board fields, role schemas and token/mask encodings",
            "assessment": "known",
            "findings": [
              {
                "value": "symbolic",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-journal",
                  "memory.md#mem-obj-experience-card",
                  "memory.md#mem-obj-strategy-board",
                  "memory.md#mem-obj-sft-messages",
                  "memory.md#mem-obj-sft-programs",
                  "memory.md#mem-obj-rl-programs"
                ],
                "note": "Localized program, metadata and token/mask units have explicit parser, selector or training-consumer rules."
              }
            ],
            "records": [
              "memory.md#mem-obj-journal",
              "memory.md#mem-obj-experience-card",
              "memory.md#mem-obj-strategy-board",
              "memory.md#mem-obj-sft-messages",
              "memory.md#mem-obj-sft-programs",
              "memory.md#mem-obj-rl-programs"
            ],
            "note": "Code is an example in parent prompts and symbolic source at execution; the training encoding is not a distributed weight representation."
          },
          {
            "scope": "SFT and RL operator parameter state",
            "assessment": "known",
            "findings": [
              {
                "value": "parametric",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-cmp-sft-model",
                  "runtime.md#rt-cmp-rl-model"
                ],
                "note": "Training targets numerical actor parameters; serving uses distributed model state."
              }
            ],
            "records": [
              "runtime.md#rt-cmp-sft-model",
              "runtime.md#rt-cmp-rl-model"
            ],
            "note": "Distributed-parametric form is established by the component records even though exact values and lineage are unavailable."
          },
          {
            "scope": "Uninspected Evo-local state, RL helper payload formatting, Gym metadata and alternative SFT collection consumers",
            "assessment": "uninspected",
            "findings": [],
            "records": [
              "memory.md#mem-rte-rl-reuse",
              "memory.md#mem-rte-sft-reuse",
              "runtime.md#rt-rte-gym-build",
              "memory.md#mem-obj-journal"
            ],
            "note": "Missing operative-part and final-consumer inspection prevents resolving every alternative form; a display summary does not classify an uninspected payload."
          }
        ],
        "records": [
          "memory.md#mem-obj-journal",
          "memory.md#mem-obj-experience-card",
          "memory.md#mem-obj-rich-summary",
          "memory.md#mem-obj-sft-messages",
          "memory.md#mem-obj-sft-programs",
          "memory.md#mem-obj-rl-programs",
          "memory.md#mem-obj-strategy-board",
          "runtime.md#rt-cmp-sft-model",
          "runtime.md#rt-cmp-rl-model",
          "memory.md#mem-rte-rl-reuse",
          "memory.md#mem-rte-sft-reuse",
          "runtime.md#rt-rte-gym-build"
        ],
        "note": "The supported forms coexist in different operative parts. Unknown payloads and uninspected consumption paths remain included rather than being inferred from inspected display strings."
      },
      "lineage": {
        "assessment": "partial",
        "units": [
          {
            "scope": "New model-authored candidate code, plans and comparative summary text on inspected production paths",
            "assessment": "known",
            "findings": [
              {
                "value": "authored",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-journal",
                  "memory.md#mem-obj-rich-summary",
                  "epistemic.md#epi-rte-summary-produce"
                ],
                "note": "Models propose program/plan and requested comparison text; software performs structural admission."
              }
            ],
            "records": [
              "memory.md#mem-obj-journal",
              "memory.md#mem-obj-rich-summary",
              "epistemic.md#epi-rte-summary-produce"
            ],
            "note": "This classifies the recorded production path, not the truth or inferential novelty of an actual response."
          },
          {
            "scope": "Execution-derived Evo cards and selected trace material in rich-summary production",
            "assessment": "known",
            "findings": [
              {
                "value": "trace-extracted",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-experience-card",
                  "memory.md#mem-rte-experience-cycle",
                  "memory.md#mem-obj-rich-summary"
                ],
                "note": "Cards derive selected outcome/history facts from attempts; summary production consumes recorded current/parent experiment material."
              }
            ],
            "records": [
              "memory.md#mem-obj-experience-card",
              "memory.md#mem-rte-experience-cycle",
              "memory.md#mem-obj-rich-summary"
            ],
            "note": "The derivation is recorded; original task data and model-weight provenance are separate unresolved units."
          },
          {
            "scope": "Deterministic strategy aggregates and message-to-token/mask conversion",
            "assessment": "known",
            "findings": [
              {
                "value": "other-compiled",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-strategy-board",
                  "memory.md#mem-obj-sft-messages",
                  "runtime.md#rt-rte-sft-training"
                ],
                "note": "Board statistics are computed from cards, and messages are compiled to token IDs and loss masks."
              }
            ],
            "records": [
              "memory.md#mem-obj-strategy-board",
              "memory.md#mem-obj-sft-messages",
              "runtime.md#rt-rte-sft-training"
            ],
            "note": "Aggregate computations and training encodings are distinct derivation paths from natural-language authoring."
          },
          {
            "scope": "Caller-supplied dataset acquisition at SFT launcher",
            "assessment": "known",
            "findings": [
              {
                "value": "imported",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-sft-messages",
                  "runtime.md#rt-rte-sft-training"
                ],
                "note": "The launcher accepts an externally selected JSONL/Parquet dataset rather than requiring the shipped selector output."
              }
            ],
            "records": [
              "memory.md#mem-obj-sft-messages",
              "runtime.md#rt-rte-sft-training"
            ],
            "note": "Import at this boundary does not establish the supplied dataset historical ancestry."
          },
          {
            "scope": "SFT rollout-derived selected demonstrations",
            "assessment": "known",
            "findings": [
              {
                "value": "trace-extracted",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-sft-messages",
                  "runtime.md#rt-rte-sft-training"
                ],
                "note": "Selectors reconstruct rollout/debug segments and produce message examples for subsequent training."
              }
            ],
            "records": [
              "memory.md#mem-obj-sft-messages",
              "runtime.md#rt-rte-sft-training"
            ],
            "note": "Recorded evolutionary segmentation supports extraction from rollout experience; arbitrary datasets and all collection variants retain separate uncertainty."
          },
          {
            "scope": "Initial corpus/model provenance, initial or externally replaced cache content and RL helper derivation details",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "runtime.md#rt-cmp-sft-model",
              "runtime.md#rt-cmp-rl-model",
              "memory.md#mem-obj-sft-messages",
              "memory.md#mem-obj-rich-summary",
              "memory.md#mem-rte-rl-reuse"
            ],
            "note": "Exact initial weights/corpus and full RL experience formatting are not supplied or inspected; cache identity does not prove historical authorship or freshness."
          },
          {
            "scope": "Evo-local database and untraced Gym metadata/SFT alternative production paths",
            "assessment": "uninspected",
            "findings": [],
            "records": [
              "memory.md#mem-obj-journal",
              "runtime.md#rt-rte-gym-build",
              "memory.md#mem-rte-sft-reuse"
            ],
            "note": "Their included provenance paths have not been traced; known derivations elsewhere do not resolve them."
          }
        ],
        "records": [
          "memory.md#mem-obj-journal",
          "memory.md#mem-obj-rich-summary",
          "epistemic.md#epi-rte-summary-produce",
          "memory.md#mem-obj-experience-card",
          "memory.md#mem-rte-experience-cycle",
          "memory.md#mem-obj-strategy-board",
          "memory.md#mem-obj-sft-messages",
          "runtime.md#rt-rte-sft-training",
          "runtime.md#rt-cmp-sft-model",
          "runtime.md#rt-cmp-rl-model",
          "memory.md#mem-rte-rl-reuse",
          "runtime.md#rt-rte-gym-build",
          "memory.md#mem-rte-sft-reuse"
        ],
        "note": "Authored, imported, trace-extracted and other-compiled paths have local witnesses. Historical provenance and opaque alternative derivations prevent an exhaustive lineage conclusion."
      },
      "behavioral_authority": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Retained parent code, feedback and selected summary text at subsequent proposal models",
            "assessment": "known",
            "findings": [
              {
                "value": "knowledge",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-operator-context",
                  "memory.md#mem-rte-sft-reuse",
                  "memory.md#mem-rte-rl-reuse",
                  "memory.md#mem-bap-experience-guidance"
                ],
                "note": "Later operators receive selected earlier attempts and comparisons as evidence or examples for the next proposal."
              }
            ],
            "records": [
              "memory.md#mem-rte-operator-context",
              "memory.md#mem-rte-sft-reuse",
              "memory.md#mem-rte-rl-reuse",
              "memory.md#mem-bap-experience-guidance"
            ],
            "note": "Advisory evidence/context, not guaranteed obedience or standing host instructions."
          },
          {
            "scope": "Retained metric, fitness, utility and family/error fields at parent and population selectors",
            "assessment": "known",
            "findings": [
              {
                "value": "ranking",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-journal",
                  "memory.md#mem-obj-experience-card",
                  "memory.md#mem-obj-strategy-board",
                  "memory.md#mem-rte-operator-context",
                  "memory.md#mem-rte-sft-reuse",
                  "memory.md#mem-rte-rl-reuse"
                ],
                "note": "Scores and derived utility metadata affect priority of prior programs and related experience."
              },
              {
                "value": "routing",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-journal",
                  "memory.md#mem-obj-experience-card",
                  "memory.md#mem-obj-strategy-board",
                  "memory.md#mem-rte-operator-context",
                  "memory.md#mem-rte-sft-reuse",
                  "memory.md#mem-rte-rl-reuse"
                ],
                "note": "Bug status, selected parents, ancestry and mode policy determine debug/improve/draft paths and their context inputs."
              }
            ],
            "records": [
              "memory.md#mem-obj-journal",
              "memory.md#mem-obj-experience-card",
              "memory.md#mem-obj-strategy-board",
              "memory.md#mem-rte-operator-context",
              "memory.md#mem-rte-sft-reuse",
              "memory.md#mem-rte-rl-reuse"
            ],
            "note": "Ranking concerns relative candidate priority; routing concerns which operation or context is used."
          },
          {
            "scope": "Retained validity/status fields at candidate eligibility filters",
            "assessment": "known",
            "findings": [
              {
                "value": "validation",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-operator-context",
                  "memory.md#mem-rte-rl-reuse",
                  "runtime.md#rt-rte-evo-generation"
                ],
                "note": "Finite-fitness/nonbuggy or active-success/debug predicates determine candidate eligibility."
              },
              {
                "value": "enforcement",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-operator-context",
                  "memory.md#mem-rte-rl-reuse",
                  "runtime.md#rt-rte-evo-generation"
                ],
                "note": "Software excludes candidates from the corresponding selected population/context when those predicates fail."
              }
            ],
            "records": [
              "memory.md#mem-rte-operator-context",
              "memory.md#mem-rte-rl-reuse",
              "runtime.md#rt-rte-evo-generation"
            ],
            "note": "This unit concerns stored node/program flags consumed by filters, not a claim that every evaluator output is trusted."
          },
          {
            "scope": "Retained experiment traces at derived-memory writers and demonstrations at supervised training inputs",
            "assessment": "known",
            "findings": [
              {
                "value": "learning",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-experience-card",
                  "memory.md#mem-obj-rich-summary",
                  "memory.md#mem-rte-experience-cycle",
                  "runtime.md#rt-rte-sft-training",
                  "runtime.md#rt-bap-training-parameters"
                ],
                "note": "Recorded experiment inputs feed retained cards/summaries for later guidance; demonstration messages feed the supervised parameter-update path."
              }
            ],
            "records": [
              "memory.md#mem-obj-experience-card",
              "memory.md#mem-obj-rich-summary",
              "memory.md#mem-rte-experience-cycle",
              "runtime.md#rt-rte-sft-training",
              "runtime.md#rt-bap-training-parameters"
            ],
            "note": "Trace-fed behavior-shaping updates and later advisory consumption are different consumers."
          },
          {
            "scope": "RL reward/sample inputs at the external numerical training consumer",
            "assessment": "partial",
            "findings": [
              {
                "value": "learning",
                "basis": "afforded",
                "records": [
                  "runtime.md#rt-rte-rl-training",
                  "runtime.md#rt-bap-training-parameters"
                ],
                "note": "Rollout rewards and logprobs are supplied for the intended RL parameter update."
              }
            ],
            "records": [
              "runtime.md#rt-rte-rl-training",
              "runtime.md#rt-bap-training-parameters",
              "runtime.md#rt-cmp-rl-model"
            ],
            "note": "Local reward/hook delivery is wired, but the actual external optimizer and exact subsequent checkpoint consumer are not inspected."
          },
          {
            "scope": "Exported quality reports at later consumers and untraced package/database/cache alternatives",
            "assessment": "uninspected",
            "findings": [],
            "records": [
              "epistemic.md#epi-obj-quality-scores",
              "epistemic.md#epi-rte-quality-recommendation",
              "runtime.md#rt-rte-gym-build",
              "memory.md#mem-rte-rl-reuse",
              "memory.md#mem-obj-journal"
            ],
            "note": "Recommendation arithmetic and CLI failure are immediate reporting effects, not established later-memory authority. Later report readers and remaining alternative consumers are uninspected."
          }
        ],
        "records": [
          "memory.md#mem-rte-operator-context",
          "memory.md#mem-rte-sft-reuse",
          "memory.md#mem-rte-rl-reuse",
          "memory.md#mem-bap-experience-guidance",
          "memory.md#mem-obj-journal",
          "memory.md#mem-obj-experience-card",
          "memory.md#mem-obj-strategy-board",
          "runtime.md#rt-rte-evo-generation",
          "memory.md#mem-obj-rich-summary",
          "memory.md#mem-rte-experience-cycle",
          "runtime.md#rt-rte-sft-training",
          "runtime.md#rt-bap-training-parameters",
          "runtime.md#rt-rte-rl-training",
          "runtime.md#rt-cmp-rl-model",
          "epistemic.md#epi-obj-quality-scores",
          "epistemic.md#epi-rte-quality-recommendation",
          "runtime.md#rt-rte-gym-build"
        ],
        "note": "Knowledge, ranking, routing, validation, enforcement and learning have consumer-specific witnesses. No instruction authority is inferred from the word guidance, and no authority is assigned to unconsumed metadata or static shipped instructions."
      },
      "write_agency": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Gym generated source/feedback, Evo journal/card/board/summary and inspected SFT/RL program admissions",
            "assessment": "known",
            "findings": [
              {
                "value": "automatic",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-rte-gym-build",
                  "memory.md#mem-rte-experience-cycle",
                  "memory.md#mem-obj-rich-summary",
                  "memory.md#mem-rte-sft-reuse",
                  "memory.md#mem-rte-rl-reuse"
                ],
                "note": "Software/model generation, derivation, structural checks and callback/database insertion decide retained content on these paths."
              }
            ],
            "records": [
              "runtime.md#rt-rte-gym-build",
              "memory.md#mem-rte-experience-cycle",
              "memory.md#mem-obj-rich-summary",
              "memory.md#mem-rte-sft-reuse",
              "memory.md#mem-rte-rl-reuse"
            ],
            "note": "Launch/configuration starts these workflows; it does not supply per-item human approval."
          },
          {
            "scope": "Shipped SFT selection/finalization transformations",
            "assessment": "known",
            "findings": [
              {
                "value": "automatic",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-rte-sft-training",
                  "memory.md#mem-obj-sft-messages"
                ],
                "note": "Score/token gates, normalization and deduplication admit or remove examples without a recorded per-example operator decision."
              }
            ],
            "records": [
              "runtime.md#rt-rte-sft-training",
              "memory.md#mem-obj-sft-messages"
            ],
            "note": "Filtering and dataset generation are software decisions even if a caller invokes the scripts."
          },
          {
            "scope": "Caller-selected initial datasets/model checkpoints and external replacements of retained cache or parameter content",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-sft-messages",
              "runtime.md#rt-cmp-sft-model",
              "runtime.md#rt-cmp-rl-model",
              "memory.md#mem-obj-rich-summary"
            ],
            "note": "Generic caller-selected paths and editable files do not establish a human content decision. Manual versus automatic admission and historical replacement control cannot be determined."
          },
          {
            "scope": "Evo-local database, other SFT variants and RL restore/cache admissions",
            "assessment": "uninspected",
            "findings": [],
            "records": [
              "memory.md#mem-obj-journal",
              "memory.md#mem-rte-sft-reuse",
              "memory.md#mem-rte-rl-reuse"
            ],
            "note": "Their admission controls remain uninspected, independently of the known callback and summary writers."
          }
        ],
        "records": [
          "runtime.md#rt-rte-gym-build",
          "memory.md#mem-rte-experience-cycle",
          "memory.md#mem-obj-rich-summary",
          "memory.md#mem-rte-sft-reuse",
          "memory.md#mem-rte-rl-reuse",
          "runtime.md#rt-rte-sft-training",
          "memory.md#mem-obj-sft-messages",
          "runtime.md#rt-cmp-sft-model",
          "runtime.md#rt-cmp-rl-model",
          "memory.md#mem-obj-journal"
        ],
        "note": "Automatic writes are established on named mechanisms. No manual finding is inferred from filesystem editing capability or an operator launching training; initial and replacement admissions remain unresolved."
      },
      "curation_operations": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Evo card/board reduction and bounded retained-summary display construction",
            "assessment": "known",
            "findings": [
              {
                "value": "consolidate",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-experience-card",
                  "memory.md#mem-obj-strategy-board",
                  "memory.md#mem-rte-experience-cycle",
                  "memory.md#mem-rte-operator-context",
                  "epistemic.md#epi-rte-summary-consume"
                ],
                "note": "Selected experiment facts, board aggregates and shortened prior summaries reduce existing retained claims for later use."
              }
            ],
            "records": [
              "memory.md#mem-obj-experience-card",
              "memory.md#mem-obj-strategy-board",
              "memory.md#mem-rte-experience-cycle",
              "memory.md#mem-rte-operator-context",
              "epistemic.md#epi-rte-summary-consume"
            ],
            "note": "These transformations select/compress existing recorded material; truncation defects do not create synthesis."
          },
          {
            "scope": "Model rich-summary transformation semantics",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-rich-summary",
              "epistemic.md#epi-rte-summary-produce"
            ],
            "note": "The route requests reusable summaries but no actual response establishes whether it only consolidates or creates a claim absent from inputs."
          },
          {
            "scope": "Aggregate board recomputation and RL surviving-row experience metadata update",
            "assessment": "known",
            "findings": [
              {
                "value": "evolve",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-strategy-board",
                  "memory.md#mem-rte-experience-cycle",
                  "memory.md#mem-obj-rl-programs",
                  "memory.md#mem-rte-rl-reuse"
                ],
                "note": "Board files are rewritten from accumulated cards and existing RL program metadata is merged with derived experience."
              }
            ],
            "records": [
              "memory.md#mem-obj-strategy-board",
              "memory.md#mem-rte-experience-cycle",
              "memory.md#mem-obj-rl-programs",
              "memory.md#mem-rte-rl-reuse"
            ],
            "note": "These revise existing derived entries; append-only creation of a new candidate is not by itself evolution."
          },
          {
            "scope": "SFT/RL fitness-based retention pruning",
            "assessment": "known",
            "findings": [
              {
                "value": "decay",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-sft-programs",
                  "memory.md#mem-obj-rl-programs",
                  "memory.md#mem-rte-sft-reuse",
                  "memory.md#mem-rte-rl-reuse"
                ],
                "note": "Configured top-k pruning forgets nonretained database rows for later database selection."
              }
            ],
            "records": [
              "memory.md#mem-obj-sft-programs",
              "memory.md#mem-obj-rl-programs",
              "memory.md#mem-rte-sft-reuse",
              "memory.md#mem-rte-rl-reuse"
            ],
            "note": "Pruning removes lower-priority retained rows on configured paths; it does not establish erasure from every log or snapshot."
          },
          {
            "scope": "SFT message finalization",
            "assessment": "known",
            "findings": [
              {
                "value": "dedup",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-rte-sft-training",
                  "memory.md#mem-obj-sft-messages"
                ],
                "note": "Finalization removes duplicate normalized message examples before the training dataset is consumed."
              }
            ],
            "records": [
              "runtime.md#rt-rte-sft-training",
              "memory.md#mem-obj-sft-messages"
            ],
            "note": "Normalized-message deduplication is separate from token-budget exclusion and checkpoint ID collision checks."
          },
          {
            "scope": "RL summary-helper semantics, Evo-local maintenance, Gym metadata lifecycle and untraced SFT variants",
            "assessment": "uninspected",
            "findings": [],
            "records": [
              "memory.md#mem-rte-rl-reuse",
              "memory.md#mem-obj-journal",
              "runtime.md#rt-rte-gym-build",
              "memory.md#mem-rte-sft-reuse"
            ],
            "note": "These unresolved transformations prevent an exhaustive operation inventory. No synthesize, invalidate or promote value is inferred merely from route names or claimed reusable experience."
          }
        ],
        "records": [
          "memory.md#mem-obj-experience-card",
          "memory.md#mem-obj-strategy-board",
          "memory.md#mem-rte-experience-cycle",
          "memory.md#mem-rte-operator-context",
          "epistemic.md#epi-rte-summary-consume",
          "memory.md#mem-obj-rich-summary",
          "epistemic.md#epi-rte-summary-produce",
          "memory.md#mem-obj-rl-programs",
          "memory.md#mem-rte-rl-reuse",
          "memory.md#mem-obj-sft-programs",
          "memory.md#mem-rte-sft-reuse",
          "runtime.md#rt-rte-sft-training",
          "memory.md#mem-obj-sft-messages",
          "memory.md#mem-obj-journal",
          "runtime.md#rt-rte-gym-build"
        ],
        "note": "Consolidation, revision, pruning and deduplication have distinct implemented witnesses. Model summary semantics and uninspected maintenance alternatives prevent complete classification; index rebuilds and primary-key checks are not counted."
      },
      "read_back_direction": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Software-selected previous-attempt supply to Gym retries and Evo/SFT/RL proposal models",
            "assessment": "known",
            "findings": [
              {
                "value": "push",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-rte-gym-build",
                  "memory.md#mem-rte-operator-context",
                  "memory.md#mem-rte-sft-reuse",
                  "memory.md#mem-rte-rl-reuse"
                ],
                "note": "Retry tails, selected parents and targeted memories are automatically supplied into later model invocations."
              }
            ],
            "records": [
              "runtime.md#rt-rte-gym-build",
              "memory.md#mem-rte-operator-context",
              "memory.md#mem-rte-sft-reuse",
              "memory.md#mem-rte-rl-reuse"
            ],
            "note": "The receiving model does not request these prior items; impending calls trigger host selection and injection."
          },
          {
            "scope": "Requested journal/card/cache restoration and training dataset read operations",
            "assessment": "known",
            "findings": [
              {
                "value": "pull",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-experience-cycle",
                  "memory.md#mem-obj-rich-summary",
                  "runtime.md#rt-rte-sft-training"
                ],
                "note": "Resume requests checkpoint/card/cache material; SFT rollout reads requested stored message samples from its data buffer."
              }
            ],
            "records": [
              "memory.md#mem-rte-experience-cycle",
              "memory.md#mem-obj-rich-summary",
              "runtime.md#rt-rte-sft-training"
            ],
            "note": "These are explicit loader/training-consumer requests for retained material, separated from subsequent prompt selection."
          },
          {
            "scope": "Evo-local callers, later Gym package/report consumers, SFT alternative search and RL restore/cache routes",
            "assessment": "uninspected",
            "findings": [],
            "records": [
              "memory.md#mem-obj-journal",
              "runtime.md#rt-rte-gym-build",
              "epistemic.md#epi-rte-quality-recommendation",
              "memory.md#mem-rte-sft-reuse",
              "memory.md#mem-rte-rl-reuse"
            ],
            "note": "No complete later-consumer inventory is established for these included parts; the known pull and push routes do not resolve them."
          }
        ],
        "records": [
          "runtime.md#rt-rte-gym-build",
          "memory.md#mem-rte-operator-context",
          "memory.md#mem-rte-sft-reuse",
          "memory.md#mem-rte-rl-reuse",
          "memory.md#mem-rte-experience-cycle",
          "memory.md#mem-obj-rich-summary",
          "runtime.md#rt-rte-sft-training",
          "memory.md#mem-obj-journal",
          "epistemic.md#epi-rte-quality-recommendation"
        ],
        "note": "Both directions occur at different operations in the chain. Fulfilling a load request is not an additional push, while automatic delivery to a model remains push even if host code used a database getter upstream."
      },
      "read_back_signal": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Impending Evo operator call: parent/ancestry/sibling and same-error targeting",
            "assessment": "known",
            "findings": [
              {
                "value": "identifier",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-operator-context",
                  "memory.md#mem-obj-journal",
                  "memory.md#mem-obj-experience-card"
                ],
                "note": "Actual parent/ancestry/sibling identity matches select retained program and card parts."
              },
              {
                "value": "coarse",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-operator-context",
                  "memory.md#mem-obj-journal",
                  "memory.md#mem-obj-experience-card"
                ],
                "note": "Optional whole-journal/base memory, recent-node fallback, inclusion switches and item/character caps select broad history slices rather than semantic matches."
              }
            ],
            "records": [
              "memory.md#mem-rte-operator-context",
              "memory.md#mem-obj-journal",
              "memory.md#mem-obj-experience-card"
            ],
            "note": "Trigger is improve/debug/crossover construction. Selector inputs include parent/node links and error signatures; selected retained nodes/cards and summary fields are delivered."
          },
          {
            "scope": "Gym retry tail supply",
            "assessment": "known",
            "findings": [
              {
                "value": "coarse",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-rte-gym-build"
                ],
                "note": "Recency-tail selection supplies a fixed slice of earlier attempt messages without content-based inference."
              }
            ],
            "records": [
              "runtime.md#rt-rte-gym-build"
            ],
            "note": "Trigger is failed preparation with retries remaining; selector takes the final two retained prepares messages and supplies their code/failure context."
          },
          {
            "scope": "SFT greedy and inspected RL parent-context selection",
            "assessment": "known",
            "findings": [
              {
                "value": "identifier",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-sft-reuse",
                  "memory.md#mem-rte-rl-reuse",
                  "memory.md#mem-obj-sft-programs",
                  "memory.md#mem-obj-rl-programs"
                ],
                "note": "Task identity matching scopes retained programs that can become delivered parent/context content."
              },
              {
                "value": "coarse",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-sft-reuse",
                  "memory.md#mem-rte-rl-reuse",
                  "memory.md#mem-obj-sft-programs",
                  "memory.md#mem-obj-rl-programs"
                ],
                "note": "Fixed fitness/status policy, draft/debug branches and population/item caps filter the available task history before delivery."
              }
            ],
            "records": [
              "memory.md#mem-rte-sft-reuse",
              "memory.md#mem-rte-rl-reuse",
              "memory.md#mem-obj-sft-programs",
              "memory.md#mem-obj-rl-programs"
            ],
            "note": "Trigger is a subsequent generation request. Same-task matching selects retained rows, then fitness/status/mode rules choose parent code and feedback; RL configured AIRA inference also selects related cards."
          },
          {
            "scope": "Full debug/crossover final templates, RL helper selection details, Evo-local and other collection/package/report alternatives",
            "assessment": "uninspected",
            "findings": [],
            "records": [
              "memory.md#mem-rte-operator-context",
              "memory.md#mem-rte-rl-reuse",
              "memory.md#mem-rte-sft-reuse",
              "runtime.md#rt-rte-gym-build",
              "epistemic.md#epi-rte-quality-recommendation",
              "memory.md#mem-obj-journal"
            ],
            "note": "Final payloads/selectors on these alternatives are not fully traced. No embedding, lexical-inference or model-judgment selector is inferred from textual storage, heuristic family labels or a model-generated summary."
          }
        ],
        "records": [
          "memory.md#mem-rte-operator-context",
          "memory.md#mem-obj-journal",
          "memory.md#mem-obj-experience-card",
          "runtime.md#rt-rte-gym-build",
          "memory.md#mem-rte-sft-reuse",
          "memory.md#mem-rte-rl-reuse",
          "memory.md#mem-obj-sft-programs",
          "memory.md#mem-obj-rl-programs",
          "epistemic.md#epi-rte-quality-recommendation"
        ],
        "note": "Identifier and coarse signals have actual push-selection witnesses with triggers, inputs and selected parts. Known pulls do not make signal inapplicable while unresolved alternative directions remain."
      },
      "trace_learning": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Evo execution-to-card/board and optional retained comparative-summary-to-later-operator chain",
            "assessment": "known",
            "findings": [
              {
                "value": "yes",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-experience-card",
                  "memory.md#mem-obj-strategy-board",
                  "memory.md#mem-obj-rich-summary",
                  "memory.md#mem-rte-experience-cycle",
                  "memory.md#mem-rte-operator-context",
                  "epistemic.md#epi-rte-summary-produce"
                ],
                "note": "Automatic trace-fed derivation/summary writes produce retained experience with a wired later proposal consumer."
              }
            ],
            "records": [
              "memory.md#mem-obj-experience-card",
              "memory.md#mem-obj-strategy-board",
              "memory.md#mem-obj-rich-summary",
              "memory.md#mem-rte-experience-cycle",
              "memory.md#mem-rte-operator-context",
              "epistemic.md#epi-rte-summary-produce"
            ],
            "note": "Recorded experiment activity feeds automatic retained behavior-shaping context; a later operator receives selected output. No observed benefit or semantic novelty is required."
          },
          {
            "scope": "Inspected SFT demonstration-production and supervised-consumer path",
            "assessment": "known",
            "findings": [
              {
                "value": "yes",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-sft-messages",
                  "runtime.md#rt-rte-sft-training",
                  "runtime.md#rt-bap-training-parameters"
                ],
                "note": "Selected stored rollout messages feed automatic training inputs targeting durable operator checkpoints."
              }
            ],
            "records": [
              "memory.md#mem-obj-sft-messages",
              "runtime.md#rt-rte-sft-training",
              "runtime.md#rt-bap-training-parameters"
            ],
            "note": "This is the rollout-derived route only. The arbitrary dataset alternative is not silently included in its ancestry."
          },
          {
            "scope": "RL surviving-row derived experience and subsequent AIRA-inference prompt consumption",
            "assessment": "known",
            "findings": [
              {
                "value": "yes",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-rl-programs",
                  "memory.md#mem-rte-rl-reuse"
                ],
                "note": "Automatic card/summary metadata updates from recorded attempts can reach later constructed operator prompts."
              }
            ],
            "records": [
              "memory.md#mem-obj-rl-programs",
              "memory.md#mem-rte-rl-reuse"
            ],
            "note": "The local retained-context route is distinct from the uninspected external numerical optimizer."
          },
          {
            "scope": "Arbitrary SFT corpus ancestry and exact external RL parameter-update/serving chain",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-sft-messages",
              "runtime.md#rt-cmp-rl-model",
              "runtime.md#rt-rte-rl-training",
              "runtime.md#rt-bap-training-parameters"
            ],
            "note": "Generic supplied datasets need not have trace ancestry; external optimizer and checkpoint handoffs prevent complete classification of these alternatives."
          },
          {
            "scope": "Evo-local database, remaining SFT variants, Gym downstream metadata/package and RL lifecycle/helper alternatives",
            "assessment": "uninspected",
            "findings": [],
            "records": [
              "memory.md#mem-obj-journal",
              "memory.md#mem-rte-sft-reuse",
              "runtime.md#rt-rte-gym-build",
              "memory.md#mem-rte-rl-reuse"
            ],
            "note": "No bounded absence records cover these included routes. They cannot receive local no findings merely because inspection is incomplete."
          }
        ],
        "records": [
          "memory.md#mem-obj-experience-card",
          "memory.md#mem-obj-strategy-board",
          "memory.md#mem-obj-rich-summary",
          "memory.md#mem-rte-experience-cycle",
          "memory.md#mem-rte-operator-context",
          "epistemic.md#epi-rte-summary-produce",
          "memory.md#mem-obj-sft-messages",
          "runtime.md#rt-rte-sft-training",
          "runtime.md#rt-bap-training-parameters",
          "memory.md#mem-obj-rl-programs",
          "memory.md#mem-rte-rl-reuse",
          "runtime.md#rt-cmp-rl-model",
          "runtime.md#rt-rte-rl-training",
          "memory.md#mem-obj-journal",
          "memory.md#mem-rte-sft-reuse",
          "runtime.md#rt-rte-gym-build"
        ],
        "note": "Supported local yes findings yield an existence finding, not full learning-inventory coverage or measured improvement. No local or system-wide no is warranted by the accepted records."
      },
      "trace_source": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Evo card/board and summary production from recorded attempts",
            "assessment": "known",
            "findings": [
              {
                "value": "tool-traces",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-experience-card",
                  "memory.md#mem-obj-strategy-board",
                  "memory.md#mem-obj-rich-summary",
                  "memory.md#mem-obj-journal",
                  "memory.md#mem-rte-experience-cycle",
                  "epistemic.md#epi-rte-summary-produce"
                ],
                "note": "Candidate execution outputs, status and feedback feed retained experience derivation and comparison."
              },
              {
                "value": "trajectories",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-experience-card",
                  "memory.md#mem-obj-strategy-board",
                  "memory.md#mem-obj-rich-summary",
                  "memory.md#mem-obj-journal",
                  "memory.md#mem-rte-experience-cycle",
                  "epistemic.md#epi-rte-summary-produce"
                ],
                "note": "Linked candidate/parent programs, actions and scored outcomes supply multi-step experiment experience to comparative memory construction."
              }
            ],
            "records": [
              "memory.md#mem-obj-experience-card",
              "memory.md#mem-obj-strategy-board",
              "memory.md#mem-obj-rich-summary",
              "memory.md#mem-obj-journal",
              "memory.md#mem-rte-experience-cycle",
              "epistemic.md#epi-rte-summary-produce"
            ],
            "note": "The original activity includes candidate execution requests/results and linked current/parent experiment states; JSON serialization does not add an event-stream source."
          },
          {
            "scope": "Rollout-derived SFT demonstration selection and training",
            "assessment": "known",
            "findings": [
              {
                "value": "session-logs",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-sft-messages",
                  "runtime.md#rt-rte-sft-training",
                  "runtime.md#rt-bap-training-parameters"
                ],
                "note": "Stored agent-work message conversations become supervised demonstrations."
              },
              {
                "value": "trajectories",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-sft-messages",
                  "runtime.md#rt-rte-sft-training",
                  "runtime.md#rt-bap-training-parameters"
                ],
                "note": "Evolutionary selection reconstructs linked root/debug-descendant segments and compares their endpoint/parent outcomes."
              }
            ],
            "records": [
              "memory.md#mem-obj-sft-messages",
              "runtime.md#rt-rte-sft-training",
              "runtime.md#rt-bap-training-parameters"
            ],
            "note": "Recorded messages and reconstructed root/debug-descendant segments are the supported content origins. This does not classify an arbitrary externally selected corpus."
          },
          {
            "scope": "RL retained experience update inputs",
            "assessment": "partial",
            "findings": [
              {
                "value": "tool-traces",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-rl-programs",
                  "memory.md#mem-rte-rl-reuse",
                  "runtime.md#rt-rte-rl-training"
                ],
                "note": "Recorded program execution status, output and reward facts feed surviving-row experience updates."
              }
            ],
            "records": [
              "memory.md#mem-obj-rl-programs",
              "memory.md#mem-rte-rl-reuse",
              "runtime.md#rt-rte-rl-training"
            ],
            "note": "Recorded execution/code feedback supports a tool-trace origin; full helper formatting and other mixed inputs remain uninspected."
          },
          {
            "scope": "Arbitrary SFT dataset origins, external RL training provenance and remaining included write alternatives",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-sft-messages",
              "runtime.md#rt-cmp-rl-model",
              "runtime.md#rt-rte-rl-training",
              "memory.md#mem-rte-sft-reuse",
              "memory.md#mem-rte-rl-reuse",
              "memory.md#mem-obj-journal",
              "runtime.md#rt-rte-gym-build"
            ],
            "note": "Opaque or untraced original inputs prevent a complete source inventory. No event-stream value follows merely from steps, timestamps or an activity wrapper."
          }
        ],
        "records": [
          "memory.md#mem-obj-experience-card",
          "memory.md#mem-obj-strategy-board",
          "memory.md#mem-obj-rich-summary",
          "memory.md#mem-obj-journal",
          "memory.md#mem-rte-experience-cycle",
          "epistemic.md#epi-rte-summary-produce",
          "memory.md#mem-obj-sft-messages",
          "runtime.md#rt-rte-sft-training",
          "runtime.md#rt-bap-training-parameters",
          "memory.md#mem-obj-rl-programs",
          "memory.md#mem-rte-rl-reuse",
          "runtime.md#rt-rte-rl-training",
          "runtime.md#rt-cmp-rl-model",
          "memory.md#mem-rte-sft-reuse",
          "runtime.md#rt-rte-gym-build"
        ],
        "note": "Session logs, tool traces and linked trajectories have scoped witnesses. Unresolved input provenance remains part of the inventory; trace source is not inapplicable when supported qualifying writes coexist with unresolved alternatives."
      }
    }
  }
}
---

# OpenRSI memory profile

## Comparison rationale

The profile classifies accepted records, not fresh source evidence. All positive
findings distinguish wired local mechanisms from the external RL training
consumer, whose parameter-update use is afforded by the integration rather than
an inspected optimizer. There are no observed or causally supported findings.
Every axis remains partial because its included inventory retains unresolved
alternatives; a positive witness does not establish complete enumeration.

The journal, cards, strategy board and rich-summary cache are different retained
parts. The source account records distinct persistence and recovery paths in
[MEM-OBJ-journal](memory.md#mem-obj-journal),
[MEM-RTE-experience-cycle](memory.md#mem-rte-experience-cycle) and
[MEM-OBJ-rich-summary](memory.md#mem-obj-rich-summary). Separate cache alternatives
are included without assuming content freshness or complete cross-file recovery.
The reconciliation supersedes EPI-OBJ-rich-summary with MEM-OBJ-rich-summary;
all object findings therefore use the latter canonical record. The epistemic
production/retention/consumption routes remain independently usable. The combined
EPI-OBJ-experience-card container was not superseded; this profile uses the
separate card and board records where their parts differ.

Knowledge at an operator prompt is different from learning authority at an
update consumer and executable source at a task executor. Parent program text
can supply examples while metrics rank it and status flags control eligibility.
These are distinct effects, not a blanket instruction or enforcement label on
all stored experience. See
[MEM-BAP-experience-guidance](memory.md#mem-bap-experience-guidance),
[RT-BAP-training-parameters](runtime.md#rt-bap-training-parameters) and
[RT-BAP-candidate-execution](runtime.md#rt-bap-candidate-execution).

Trace learning here denotes an automatic trace-fed retained update with a later
consumer, not improved capacity or accepted explanatory knowledge. The Evo
summary/card chain and RL retained-context chain qualify independently of
whether trained parameters are ever deployed to Evo. Model-summary novelty
remains unresolved: neither requested reusable experience nor failure to prove
entailment establishes synthesis. Deterministic reduction and truncation support
consolidation locally, without certifying faithful retention of qualifications.
See [EPI-RTE-summary-produce](epistemic.md#epi-rte-summary-produce) and
[EPI-RTE-summary-consume](epistemic.md#epi-rte-summary-consume).

The SFT launcher admits arbitrary caller-selected data. Its known rollout-derived
branch does not settle that alternative's historical lineage, trace origin or
human admission control. Likewise no manual finding follows just from editable
files, caller identity or a launch decision. Pruning is forgetting from the
inspected database, not historical invalidation of every copy. See
[RT-RTE-sft-training](runtime.md#rt-rte-sft-training),
[MEM-RTE-sft-reuse](memory.md#mem-rte-sft-reuse) and
[MEM-RTE-rl-reuse](memory.md#mem-rte-rl-reuse).

Pull describes requested restoration or sample reads; push describes the host's
selection and unsolicited supply of old work to the next proposal model. These
operations can coexist in one chain. Identifier findings refer to actual
parent/task matches selecting delivered content, not to a cache filename alone.
Coarse findings refer to tails, broad journal slices and fixed score/status/cap
filters, not inferred semantic similarity. Complete debug/crossover payloads,
RL helper details and untraced alternatives prevent a stronger direction or
signal inventory. See
[MEM-RTE-operator-context](memory.md#mem-rte-operator-context).

Quality reports are retained outputs, but their immediate recommendation/CLI
consumers do not establish a later accumulated-memory route. Their later
consumption remains unresolved rather than being assigned knowledge or enforcement
authority by analogy. See
[EPI-RTE-quality-recommendation](epistemic.md#epi-rte-quality-recommendation).
Static task skills are excluded from the comparison's accumulated-memory scope;
the inspected injector does not establish their trace-fed maintenance. See
[MEM-OBJ-task-skills](memory.md#mem-obj-task-skills).

Source-read log: none. This classification used only the supplied accepted
members and reconciliation; no frozen-source ambiguity required a direct read.
