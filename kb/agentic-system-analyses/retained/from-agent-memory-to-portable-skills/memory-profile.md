---
{
  "type": "agentic-system-analyses/types/agentic-system-memory-profile.md",
  "description": "Memory profile of From Agent Memory to Portable Skills: documented scoped trace distillation, retained skills, review and grounding repair.",
  "run-id": "AAS-2026-10-18-from-agent-memory-to-portable-skills-4a509c7732b1-01",
  "source-identity": "https://neo4j.com/blog/genai/from-agent-memory-to-portable-skills",
  "reviewed-boundary": "neo4j-article-2026-10-18-99f91d4da959",
  "memory-comparison": {
    "version": 2,
    "scope": "Included: scoped retained conversation/decision text, tool-call structure and opaque payloads, ontology/reference identities, derived graph and prose skill products, grounding, review and version metadata, and their documented admission/maintenance/later-consumer routes. Excluded: upstream ingestion implementation, enclosing host execution/context policy, transient Redis job state and synthesis buffers, and model weights with no established through-use memory update. Unknown backing provenance and payload forms, patch release and consumer selection remain included limits, not inferred absence.",
    "axes": {
      "storage_substrate": {
        "assessment": "known",
        "units": [
          {
            "scope": "Scoped conversation text, tool records including opaque payloads, and ontology entities",
            "assessment": "known",
            "findings": [
              {
                "value": "graph",
                "basis": "claimed",
                "records": [
                  "memory.md#mem-obj-memory-text",
                  "memory.md#mem-obj-tool-call",
                  "memory.md#mem-obj-memory-graph"
                ],
                "note": "Neo4j is the retained substrate, regardless of property encoding."
              }
            ],
            "records": [
              "memory.md#mem-obj-memory-text",
              "memory.md#mem-obj-tool-call",
              "memory.md#mem-obj-memory-graph"
            ],
            "note": "All three backing-input classes are described as workspace Neo4j graph material."
          },
          {
            "scope": "Derived skill graph, grounding and version relations, and packaged skill including prose fallback",
            "assessment": "known",
            "findings": [
              {
                "value": "graph",
                "basis": "claimed",
                "records": [
                  "runtime.md#rt-obj-procedure-graph",
                  "runtime.md#rt-obj-skill-package",
                  "runtime.md#rt-rte-skill-distillation",
                  "runtime.md#rt-rte-step-repair"
                ],
                "note": "The documented persistence stage writes both retained products into Neo4j."
              }
            ],
            "records": [
              "runtime.md#rt-obj-procedure-graph",
              "runtime.md#rt-obj-skill-package",
              "runtime.md#rt-rte-skill-distillation",
              "runtime.md#rt-rte-step-repair"
            ],
            "note": "The graph and packaged artifact are persisted in Neo4j; SKILL.md names an export format, not an independently evidenced filesystem store."
          }
        ],
        "records": [
          "memory.md#mem-obj-memory-text",
          "memory.md#mem-obj-tool-call",
          "memory.md#mem-obj-memory-graph",
          "runtime.md#rt-obj-procedure-graph",
          "runtime.md#rt-obj-skill-package",
          "runtime.md#rt-rte-skill-distillation",
          "runtime.md#rt-rte-step-repair"
        ],
        "note": "Known substrate classification for the documented retained inventory, not verified deployment. No retained filesystem copy is established by the export name. Redis jobs and transient synthesis buffers are not additional accumulated-memory objects."
      },
      "representational_form": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Conversation reasoning/messages and generated procedure, claims and step annotations at model/human consumers",
            "assessment": "known",
            "findings": [
              {
                "value": "natural-language",
                "basis": "claimed",
                "records": [
                  "memory.md#mem-obj-memory-text",
                  "runtime.md#rt-obj-skill-package",
                  "epistemic.md#epi-obj-claims",
                  "epistemic.md#epi-obj-step-annotations",
                  "runtime.md#rt-bap-skill-consumption"
                ],
                "note": "Input text supplies evidence; generated text supplies procedure and candidate assertions."
              }
            ],
            "records": [
              "memory.md#mem-obj-memory-text",
              "runtime.md#rt-obj-skill-package",
              "epistemic.md#epi-obj-claims",
              "epistemic.md#epi-obj-step-annotations",
              "runtime.md#rt-bap-skill-consumption"
            ],
            "note": "The described readable parts operate through human or model interpretation, including the prose branch."
          },
          {
            "scope": "Tool fixed-role fields, ontology/reference identities and skill topology/grounding at fixed-rule consumers",
            "assessment": "known",
            "findings": [
              {
                "value": "symbolic",
                "basis": "claimed",
                "records": [
                  "memory.md#mem-obj-tool-call",
                  "memory.md#mem-obj-memory-graph",
                  "runtime.md#rt-obj-procedure-graph",
                  "epistemic.md#epi-rte-source-check",
                  "runtime.md#rt-rte-drift-check",
                  "runtime.md#rt-rte-step-repair"
                ],
                "note": "Bindings, statuses, identity existence and survivor links have localized rule-governed consumers."
              }
            ],
            "records": [
              "memory.md#mem-obj-tool-call",
              "memory.md#mem-obj-memory-graph",
              "runtime.md#rt-obj-procedure-graph",
              "epistemic.md#epi-rte-source-check",
              "runtime.md#rt-rte-drift-check",
              "runtime.md#rt-rte-step-repair"
            ],
            "note": "These structural parts are distinguished from arbitrary payloads and descriptions."
          },
          {
            "scope": "Arbitrary retained tool input/output payloads and unspecified ontology properties",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-tool-call",
              "memory.md#mem-obj-memory-graph"
            ],
            "note": "Payload encoding and consumption are unspecified; graph properties alone do not establish symbolic form."
          }
        ],
        "records": [
          "memory.md#mem-obj-memory-text",
          "runtime.md#rt-obj-skill-package",
          "epistemic.md#epi-obj-claims",
          "epistemic.md#epi-obj-step-annotations",
          "runtime.md#rt-bap-skill-consumption",
          "memory.md#mem-obj-tool-call",
          "memory.md#mem-obj-memory-graph",
          "runtime.md#rt-obj-procedure-graph",
          "epistemic.md#epi-rte-source-check",
          "runtime.md#rt-rte-drift-check",
          "runtime.md#rt-rte-step-repair"
        ],
        "note": "Text and fixed-rule structure are classified separately. Opaque tool payloads and ontology property representations prevent complete coverage; no parametric retained-memory form is inferred from a synthesis model."
      },
      "lineage": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Recorded conversations, agent decisions and tool-execution traces as inputs to this distillation",
            "assessment": "partial",
            "findings": [
              {
                "value": "trace-extracted",
                "basis": "claimed",
                "records": [
                  "memory.md#mem-obj-memory-text",
                  "memory.md#mem-obj-tool-call"
                ],
                "note": "Recorded agent interactions and executions supply the retained input evidence."
              }
            ],
            "records": [
              "memory.md#mem-obj-memory-text",
              "memory.md#mem-obj-tool-call"
            ],
            "note": "Their activity origin is described, but original authorship, prior summarization and status-update provenance remain unresolved."
          },
          {
            "scope": "Derived topology, bindings and instruction package through the documented distillation path",
            "assessment": "known",
            "findings": [
              {
                "value": "trace-extracted",
                "basis": "claimed",
                "records": [
                  "runtime.md#rt-obj-procedure-graph",
                  "runtime.md#rt-rte-skill-distillation",
                  "runtime.md#rt-obj-skill-package"
                ],
                "note": "Scoped traces feed retained graph and instruction products."
              },
              {
                "value": "authored",
                "basis": "claimed",
                "records": [
                  "epistemic.md#epi-obj-claims",
                  "epistemic.md#epi-obj-step-annotations",
                  "runtime.md#rt-rte-skill-distillation"
                ],
                "note": "The model authors claims, names, descriptions and completion criteria."
              },
              {
                "value": "other-compiled",
                "basis": "claimed",
                "records": [
                  "runtime.md#rt-obj-procedure-graph",
                  "runtime.md#rt-rte-skill-distillation"
                ],
                "note": "Deterministic construction derives topology and bindings from recorded traces rather than model-authored topology."
              }
            ],
            "records": [
              "runtime.md#rt-obj-procedure-graph",
              "runtime.md#rt-obj-skill-package",
              "runtime.md#rt-rte-skill-distillation",
              "epistemic.md#epi-obj-claims",
              "epistemic.md#epi-obj-step-annotations"
            ],
            "note": "Known derivation path includes deterministic topology and model-written textual parts, not a claim about upstream historical completeness."
          },
          {
            "scope": "Ontology extraction and original admission/provenance of all backing material",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-memory-graph",
              "memory.md#mem-obj-memory-text",
              "memory.md#mem-obj-tool-call"
            ],
            "note": "The ontology extractor, complete source history and initial control are unspecified; extraction alone does not identify a controlled origin for every part."
          }
        ],
        "records": [
          "memory.md#mem-obj-memory-text",
          "memory.md#mem-obj-tool-call",
          "runtime.md#rt-obj-procedure-graph",
          "runtime.md#rt-obj-skill-package",
          "runtime.md#rt-rte-skill-distillation",
          "epistemic.md#epi-obj-claims",
          "epistemic.md#epi-obj-step-annotations",
          "memory.md#mem-obj-memory-graph"
        ],
        "note": "Derivation paths coexist: authored text and deterministic compilation both draw on traces. Initial source provenance is not resolved by a known downstream transformation."
      },
      "behavioral_authority": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Retained conversations and recorded execution outcomes at the distillation update consumer",
            "assessment": "known",
            "findings": [
              {
                "value": "knowledge",
                "basis": "claimed",
                "records": [
                  "memory.md#mem-obj-memory-text",
                  "memory.md#mem-obj-tool-call",
                  "runtime.md#rt-rte-skill-distillation"
                ],
                "note": "Selected records supply evidence and context for candidate construction."
              },
              {
                "value": "learning",
                "basis": "claimed",
                "records": [
                  "memory.md#mem-obj-memory-text",
                  "memory.md#mem-obj-tool-call",
                  "runtime.md#rt-rte-skill-distillation"
                ],
                "note": "Retained experience feeds automatic construction of durable behavior-shaping skill artifacts."
              },
              {
                "value": "ranking",
                "basis": "claimed",
                "records": [
                  "memory.md#mem-obj-tool-call",
                  "runtime.md#rt-rte-skill-distillation"
                ],
                "note": "Recorded outcomes and frequency-weighted recurring-action clusters influence pattern priority."
              }
            ],
            "records": [
              "memory.md#mem-obj-memory-text",
              "memory.md#mem-obj-tool-call",
              "runtime.md#rt-rte-skill-distillation"
            ],
            "note": "This unit is the described update use, distinct from downstream instruction use."
          },
          {
            "scope": "Graph identity and grounding at reference validation and repair consumers",
            "assessment": "known",
            "findings": [
              {
                "value": "validation",
                "basis": "claimed",
                "records": [
                  "memory.md#mem-obj-memory-graph",
                  "runtime.md#rt-obj-procedure-graph",
                  "epistemic.md#epi-rte-source-check",
                  "runtime.md#rt-rte-step-repair"
                ],
                "note": "Existence and surviving-grounding checks constrain admissible references and patches."
              },
              {
                "value": "enforcement",
                "basis": "claimed",
                "records": [
                  "runtime.md#rt-obj-procedure-graph",
                  "runtime.md#rt-rte-step-repair"
                ],
                "note": "No surviving grounding causes repair refusal, giving retained grounding an enforced veto on that patch."
              }
            ],
            "records": [
              "memory.md#mem-obj-memory-graph",
              "runtime.md#rt-obj-procedure-graph",
              "epistemic.md#epi-rte-source-check",
              "runtime.md#rt-rte-step-repair"
            ],
            "note": "The classified force concerns retained identities and survivor relations, not truth of synthesized claims."
          },
          {
            "scope": "Retained expected status and recorded current ToolCall status at governance comparison",
            "assessment": "known",
            "findings": [
              {
                "value": "validation",
                "basis": "claimed",
                "records": [
                  "memory.md#mem-obj-tool-call",
                  "runtime.md#rt-obj-procedure-graph",
                  "runtime.md#rt-rte-drift-check"
                ],
                "note": "Retained expected status supplies the criterion for the current-status comparison."
              }
            ],
            "records": [
              "memory.md#mem-obj-tool-call",
              "runtime.md#rt-obj-procedure-graph",
              "runtime.md#rt-rte-drift-check"
            ],
            "note": "The comparison checks status consistency; its downstream blocking effect is not established."
          },
          {
            "scope": "Pending skill and linked backing evidence at human review",
            "assessment": "known",
            "findings": [
              {
                "value": "knowledge",
                "basis": "claimed",
                "records": [
                  "runtime.md#rt-obj-skill-package",
                  "runtime.md#rt-rte-review-delivery",
                  "memory.md#mem-obj-memory-text"
                ],
                "note": "Retained steps and backing records supply material for review judgment."
              }
            ],
            "records": [
              "runtime.md#rt-obj-skill-package",
              "runtime.md#rt-rte-review-delivery",
              "memory.md#mem-obj-memory-text"
            ],
            "note": "The reviewer consults steps and evidence before the publication decision."
          },
          {
            "scope": "Published procedure and references at later host-model consumers",
            "assessment": "known",
            "findings": [
              {
                "value": "instruction",
                "basis": "claimed",
                "records": [
                  "runtime.md#rt-obj-skill-package",
                  "runtime.md#rt-bap-skill-consumption"
                ],
                "note": "The retained procedure directs later agent work."
              },
              {
                "value": "knowledge",
                "basis": "claimed",
                "records": [
                  "runtime.md#rt-obj-skill-package",
                  "runtime.md#rt-bap-skill-consumption"
                ],
                "note": "Reference material and claims accompany the procedure as context."
              }
            ],
            "records": [
              "runtime.md#rt-obj-skill-package",
              "runtime.md#rt-bap-skill-consumption",
              "runtime.md#rt-rte-review-delivery"
            ],
            "note": "Natural-language guidance does not grant tools or enforce compliance."
          },
          {
            "scope": "Review state, versions and drift flags at downstream delivery/selection consumers",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "runtime.md#rt-rte-review-delivery",
              "runtime.md#rt-rte-drift-check",
              "runtime.md#rt-rte-step-repair"
            ],
            "note": "Publication is the documented condition, but actual state enforcement, flag consultation, version resolution and withdrawal are unspecified. No routing or enforcement value is inferred for these opaque consumer mechanisms."
          }
        ],
        "records": [
          "memory.md#mem-obj-memory-text",
          "memory.md#mem-obj-tool-call",
          "runtime.md#rt-rte-skill-distillation",
          "memory.md#mem-obj-memory-graph",
          "runtime.md#rt-obj-procedure-graph",
          "epistemic.md#epi-rte-source-check",
          "runtime.md#rt-rte-step-repair",
          "runtime.md#rt-rte-drift-check",
          "runtime.md#rt-obj-skill-package",
          "runtime.md#rt-rte-review-delivery",
          "runtime.md#rt-bap-skill-consumption"
        ],
        "note": "Consumer-specific forces coexist without an implication from instructional delivery to enforcement or observed benefit. Metadata whose consequential consumer is unresolved remains unclassified."
      },
      "write_agency": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Software/model construction and gate admission to pending persistence",
            "assessment": "known",
            "findings": [
              {
                "value": "automatic",
                "basis": "claimed",
                "records": [
                  "runtime.md#rt-rte-skill-distillation",
                  "epistemic.md#epi-rte-source-check"
                ],
                "note": "Software filters and gates model/deterministic output before pending persistence."
              }
            ],
            "records": [
              "runtime.md#rt-rte-skill-distillation",
              "epistemic.md#epi-rte-source-check"
            ],
            "note": "Scope initiation is not a human decision approving each generated item."
          },
          {
            "scope": "Human initial publication approval or rejection",
            "assessment": "known",
            "findings": [
              {
                "value": "manual",
                "basis": "claimed",
                "records": [
                  "runtime.md#rt-rte-review-delivery"
                ],
                "note": "Human approval admits the skill to publication."
              }
            ],
            "records": [
              "runtime.md#rt-rte-review-delivery"
            ],
            "note": "The reviewer explicitly decides on the retained product, independently of who started the job."
          },
          {
            "scope": "Salvageable single-step grounding patch admission",
            "assessment": "known",
            "findings": [
              {
                "value": "automatic",
                "basis": "claimed",
                "records": [
                  "runtime.md#rt-rte-step-repair"
                ],
                "note": "Repair traversal and graph validation determine admission of the revised patch."
              }
            ],
            "records": [
              "runtime.md#rt-rte-step-repair"
            ],
            "note": "Software admits surviving-grounding changes or refuses unsupported repair; later patch publication is separate."
          },
          {
            "scope": "Backing-content initial admission, manual replacements and repaired-patch publication",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-memory-text",
              "memory.md#mem-obj-tool-call",
              "memory.md#mem-obj-memory-graph",
              "runtime.md#rt-rte-review-delivery",
              "runtime.md#rt-rte-step-repair"
            ],
            "note": "Initial acquisition control, direct edits/replacements and mandatory human patch approval are not specified."
          }
        ],
        "records": [
          "runtime.md#rt-rte-skill-distillation",
          "epistemic.md#epi-rte-source-check",
          "runtime.md#rt-rte-review-delivery",
          "runtime.md#rt-rte-step-repair",
          "memory.md#mem-obj-memory-text",
          "memory.md#mem-obj-tool-call",
          "memory.md#mem-obj-memory-graph"
        ],
        "note": "Automatic construction and repair coexist with manual initial publication; they do not settle upstream acquisition or alternate revision controls."
      },
      "curation_operations": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Recurring-action consolidation over retained scoped traces",
            "assessment": "known",
            "findings": [
              {
                "value": "consolidate",
                "basis": "claimed",
                "records": [
                  "runtime.md#rt-rte-skill-distillation"
                ],
                "note": "Recurring actions are combined into outcome-separated frequency-weighted patterns."
              }
            ],
            "records": [
              "runtime.md#rt-rte-skill-distillation"
            ],
            "note": "The described transformation clusters and reduces existing experience; intermediate cluster retention need not be established to classify the operation over retained inputs."
          },
          {
            "scope": "Single-step survivor/deletion cleanup and retained superseding patch",
            "assessment": "known",
            "findings": [
              {
                "value": "evolve",
                "basis": "claimed",
                "records": [
                  "runtime.md#rt-rte-step-repair"
                ],
                "note": "One step is re-grounded and a revised skill version is retained."
              },
              {
                "value": "invalidate",
                "basis": "claimed",
                "records": [
                  "runtime.md#rt-rte-step-repair"
                ],
                "note": "A patch supersedes the prior version, withdrawing its current-version role while preserving a version relation."
              }
            ],
            "records": [
              "runtime.md#rt-rte-step-repair"
            ],
            "note": "This classifies the described grounding/version transformation, not physical deletion of obsolete history."
          },
          {
            "scope": "Semantic contribution of model claims/topology and effects of drift flags on reliance",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "runtime.md#rt-rte-skill-distillation",
              "epistemic.md#epi-obj-claims",
              "runtime.md#rt-rte-drift-check",
              "runtime.md#rt-rte-step-repair"
            ],
            "note": "No claim/graph instance establishes a novel proposition for synthesis; flagging alone does not establish withdrawal. Deduplication, decay and tier promotion are not established by cluster names, source merges or publication."
          }
        ],
        "records": [
          "runtime.md#rt-rte-skill-distillation",
          "runtime.md#rt-rte-step-repair",
          "epistemic.md#epi-obj-claims",
          "runtime.md#rt-rte-drift-check"
        ],
        "note": "Consolidation and bounded revision are supported at claimed strength. Semantic synthesis, alternative transformations and downstream withdrawal remain unresolved rather than absent."
      },
      "read_back_direction": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Scope-requested retained-evidence retrieval and bounded synthesis delivery",
            "assessment": "known",
            "findings": [
              {
                "value": "pull",
                "basis": "claimed",
                "records": [
                  "runtime.md#rt-rte-skill-distillation",
                  "memory.md#mem-obj-memory-text",
                  "memory.md#mem-obj-tool-call",
                  "memory.md#mem-obj-memory-graph"
                ],
                "note": "Requested scope selects retained conversations/traces for construction."
              }
            ],
            "records": [
              "runtime.md#rt-rte-skill-distillation",
              "memory.md#mem-obj-memory-text",
              "memory.md#mem-obj-tool-call",
              "memory.md#mem-obj-memory-graph"
            ],
            "note": "The distiller fulfills a scope request; snippet filtering within that requested chain is not an additional unsolicited delivery."
          },
          {
            "scope": "Reviewer evidence access and MCP/REST published-package fetching",
            "assessment": "known",
            "findings": [
              {
                "value": "pull",
                "basis": "claimed",
                "records": [
                  "runtime.md#rt-rte-review-delivery",
                  "runtime.md#rt-bap-skill-consumption"
                ],
                "note": "A reviewer follows evidence and clients fetch retained published packages."
              }
            ],
            "records": [
              "runtime.md#rt-rte-review-delivery",
              "runtime.md#rt-bap-skill-consumption"
            ],
            "note": "These documented request/load routes have later consumer roles, not observed deployments."
          },
          {
            "scope": "Host skill loading, governance scheduling, repair invocation and downstream version/flag delivery alternatives",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "runtime.md#rt-rte-review-delivery",
              "runtime.md#rt-rte-drift-check",
              "runtime.md#rt-rte-step-repair"
            ],
            "note": "No independent unsolicited selector is described; host loading policy and governance/repair initiation are unresolved. This prevents a complete pull-only conclusion."
          }
        ],
        "records": [
          "runtime.md#rt-rte-skill-distillation",
          "memory.md#mem-obj-memory-text",
          "memory.md#mem-obj-tool-call",
          "memory.md#mem-obj-memory-graph",
          "runtime.md#rt-rte-review-delivery",
          "runtime.md#rt-bap-skill-consumption",
          "runtime.md#rt-rte-drift-check",
          "runtime.md#rt-rte-step-repair"
        ],
        "note": "Supported requested routes establish pull, not system-wide absence of push. Automatic delivery in fulfillment of a request is not counted again as push."
      },
      "read_back_signal": {
        "assessment": "not-determinable",
        "units": [
          {
            "scope": "Potential unsolicited host loading and governance/version delivery",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "runtime.md#rt-rte-review-delivery",
              "runtime.md#rt-rte-drift-check",
              "runtime.md#rt-rte-step-repair"
            ],
            "note": "Trigger, selector input and selected retained parts for a push route are not established. Scope IDs and evidence links on requested retrieval do not establish identifier-based push."
          }
        ],
        "records": [
          "runtime.md#rt-rte-review-delivery",
          "runtime.md#rt-rte-drift-check",
          "runtime.md#rt-rte-step-repair"
        ],
        "note": "Known pull routes cannot make the unresolved loading/maintenance alternatives inapplicable. No controlled push-selection signal is supported."
      },
      "trace_learning": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Automatic scoped trace distillation into durable procedure graph/package for later review and host guidance",
            "assessment": "known",
            "findings": [
              {
                "value": "yes",
                "basis": "claimed",
                "records": [
                  "runtime.md#rt-rte-skill-distillation",
                  "runtime.md#rt-obj-procedure-graph",
                  "runtime.md#rt-obj-skill-package",
                  "runtime.md#rt-bap-skill-consumption",
                  "memory.md#mem-obj-memory-text",
                  "memory.md#mem-obj-tool-call"
                ],
                "note": "Software/model transformation of agent activity produces retained behavior-shaping skills for later consumers; improvement and activation remain unobserved."
              }
            ],
            "records": [
              "runtime.md#rt-rte-skill-distillation",
              "runtime.md#rt-obj-procedure-graph",
              "runtime.md#rt-obj-skill-package",
              "runtime.md#rt-bap-skill-consumption",
              "memory.md#mem-obj-memory-text",
              "memory.md#mem-obj-tool-call"
            ],
            "note": "The documented raw-to-derived-to-later-consumer chain meets the write-route definition, including the prose alternative; human publication veto does not erase automatic pending-artifact construction."
          },
          {
            "scope": "Repair-derived behavior changes beyond grounding, alternate writers and upstream processing",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "runtime.md#rt-rte-step-repair",
              "memory.md#mem-obj-memory-text",
              "memory.md#mem-obj-tool-call",
              "memory.md#mem-obj-memory-graph"
            ],
            "note": "Grounding revision is documented, but original trace consumption and downstream behavior-shaping effects of every alternative update are not specified. No evidenced-absence record warrants a local no."
          }
        ],
        "records": [
          "runtime.md#rt-rte-skill-distillation",
          "runtime.md#rt-obj-procedure-graph",
          "runtime.md#rt-obj-skill-package",
          "runtime.md#rt-bap-skill-consumption",
          "memory.md#mem-obj-memory-text",
          "memory.md#mem-obj-tool-call",
          "runtime.md#rt-rte-step-repair",
          "memory.md#mem-obj-memory-graph"
        ],
        "note": "A claimed yes survives incomplete inventory coverage. This is not measured learning, parameter updating, autonomous publication or improvement of the distiller itself."
      },
      "trace_source": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Conversation, linked decision experience and tool execution supplied to qualifying skill construction",
            "assessment": "known",
            "findings": [
              {
                "value": "session-logs",
                "basis": "claimed",
                "records": [
                  "memory.md#mem-obj-memory-text",
                  "runtime.md#rt-rte-skill-distillation"
                ],
                "note": "Surrounding conversational messages from agent work feed synthesis."
              },
              {
                "value": "tool-traces",
                "basis": "claimed",
                "records": [
                  "memory.md#mem-obj-tool-call",
                  "runtime.md#rt-rte-skill-distillation"
                ],
                "note": "Recorded tool names, inputs, outputs and statuses feed construction."
              },
              {
                "value": "trajectories",
                "basis": "claimed",
                "records": [
                  "memory.md#mem-obj-memory-text",
                  "memory.md#mem-obj-tool-call",
                  "runtime.md#rt-rte-skill-distillation"
                ],
                "note": "AgentStep reasoning/action/result and its linked tool decisions provide multi-step recorded experience used to derive ordering and topology."
              }
            ],
            "records": [
              "memory.md#mem-obj-memory-text",
              "memory.md#mem-obj-tool-call",
              "runtime.md#rt-rte-skill-distillation"
            ],
            "note": "Classification follows the documented original content, not Redis transport or graph serialization."
          },
          {
            "scope": "Original provenance of ontology inputs, prior summaries and unresolved alternative updates",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-memory-graph",
              "memory.md#mem-obj-memory-text",
              "memory.md#mem-obj-tool-call",
              "runtime.md#rt-rte-step-repair"
            ],
            "note": "The extraction history and original sources of all mixed inputs are unspecified. Queue events do not establish event-stream learning inputs; repair provenance does not settle a separate trace-fed learning route."
          }
        ],
        "records": [
          "memory.md#mem-obj-memory-text",
          "memory.md#mem-obj-tool-call",
          "runtime.md#rt-rte-skill-distillation",
          "memory.md#mem-obj-memory-graph",
          "runtime.md#rt-rte-step-repair"
        ],
        "note": "The positive trace-fed route has classified conversational, tool and linked-experience sources. Mixed upstream provenance and other updates prevent complete enumeration; unresolved sources are not inapplicable."
      }
    }
  }
}
---

# From Agent Memory to Portable Skills memory profile

## Comparison rationale

All findings retain claimed strength: the accepted records describe an article-level design, not inspected implementation or observed use. Coverage assessments therefore describe classification within named scopes, not strength of proof. The Neo4j package is not assigned files merely because its export is called SKILL.md. The structural graph and readable procedure have different consumption paths; arbitrary tool payloads stay unresolved. See [MEM-OBJ-tool-call](memory.md#mem-obj-tool-call), [RT-OBJ-procedure-graph](runtime.md#rt-obj-procedure-graph) and [RT-OBJ-skill-package](runtime.md#rt-obj-skill-package).

The learning authority of recorded experience belongs at the distillation update consumer; instructional authority belongs to the later host. Automatic production of a durable instruction artifact supports trace learning even though a human separately approves initial publication. Neither that classification nor the presence of source references establishes semantic warrant, exercised capacity improvement or parameter learning. See [RT-RTE-skill-distillation](runtime.md#rt-rte-skill-distillation), [RT-RTE-review-delivery](runtime.md#rt-rte-review-delivery), [RT-BAP-skill-consumption](runtime.md#rt-bap-skill-consumption) and [RT-CMP-llm](runtime.md#rt-cmp-llm).

Consolidation is the described reduction of recurring retained activity. Deterministic topology and model authorship are separate derivation contributions, not proof of entailment or a novel claim. Source-survivor repair evolves grounding and supersedes a version; contradiction flagging alone does not demonstrate revocation. The meaning of generated claims remains unresolved, as does whether installed consumers receive a revised version. See [EPI-OBJ-claims](epistemic.md#epi-obj-claims), [RT-RTE-step-repair](runtime.md#rt-rte-step-repair) and [RT-RTE-drift-check](runtime.md#rt-rte-drift-check).

Requested evidence selection and client fetching support pull. The document does not settle every host-loading or governance trigger, so signal coverage is not-determinable rather than inapplicable. An evidence-link identity on a requested read is not a push signal. See [RT-RTE-review-delivery](runtime.md#rt-rte-review-delivery) and [RT-RTE-skill-distillation](runtime.md#rt-rte-skill-distillation).

Reconciliation establishes no supersessions: scoped-input and package containers remain valid beside their parts. Consequently no citation or value was redirected. No source files were read for this classification; all warrants come from the supplied accepted records and their annotations. Model storage and parameter lifecycle remain outside the through-use memory inventory rather than being inferred from model inference.
