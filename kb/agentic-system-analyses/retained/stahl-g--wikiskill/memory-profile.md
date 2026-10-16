---
{
  "type": "agentic-system-analyses/types/agentic-system-memory-profile.md",
  "description": "WikiSkill memory profile: retained experience, Wiki lessons, procedural skills and control metadata, with unassessed research-controller alternatives.",
  "run-id": "AAS-2026-10-15-wikiskill-baafad05d35e-01",
  "source-identity": "https://github.com/Stahl-G/WikiSkill",
  "reviewed-boundary": "da6984caca09d5f81b2336cf3067b59c0c18bb1e",
  "memory-comparison": {
    "version": 2,
    "scope": "Retained product task evidence, optional traces, original feedback, journal-backed patterns and replay/adoption metadata; research raw/selected experience, Wiki pages/indexes, impact/proposal/checkpoint artifacts, SKILL text and named SKILL/PURPOSE mappings; inheritance and deployment copies/backups; their write, maintenance and later-consumer routes. Additional OfficeQA and Spreadsheet callable controllers remain included but unassessed. Excludes shipped static role/prompts, external model weights and host context management, and task corpora except retained experience used by these routes.",
    "axes": {
      "storage_substrate": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Inspected product retained patterns, original feedback, skill files, evidence payloads and journal metadata",
            "assessment": "known",
            "findings": [
              {
                "value": "files",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-patterns",
                  "memory.md#mem-obj-feedback",
                  "memory.md#mem-obj-skill",
                  "memory.md#mem-obj-experience",
                  "runtime.md#rt-obj-product-journal"
                ],
                "note": "Local JSON events, Markdown/UTF-8 text, output files and optional trace copies persist on the filesystem."
              }
            ],
            "records": [
              "memory.md#mem-obj-patterns",
              "memory.md#mem-obj-feedback",
              "memory.md#mem-obj-skill",
              "memory.md#mem-obj-experience",
              "runtime.md#rt-obj-product-journal"
            ],
            "note": "Encoding and hash links do not turn local files into a graph or database."
          },
          {
            "scope": "Research Wiki, impact history, raw/selected traces, named SKILL/PURPOSE mappings and checkpoints",
            "assessment": "known",
            "findings": [
              {
                "value": "files",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-research-wiki",
                  "memory.md#mem-obj-skill-impact",
                  "memory.md#mem-obj-research-evidence",
                  "memory.md#mem-obj-paper-skills",
                  "runtime.md#rt-rte-research-evolve",
                  "runtime.md#rt-rte-isolated-study"
                ],
                "note": "Markdown trees, JSON mappings, attempts, proposal caches and completion markers are local retained files."
              }
            ],
            "records": [
              "memory.md#mem-obj-research-wiki",
              "memory.md#mem-obj-skill-impact",
              "memory.md#mem-obj-research-evidence",
              "memory.md#mem-obj-paper-skills",
              "runtime.md#rt-rte-research-evolve",
              "runtime.md#rt-rte-isolated-study"
            ],
            "note": "Temporary staging is distinguished from persistent source artifacts."
          },
          {
            "scope": "Exported/installed deployment copy and restoration backup",
            "assessment": "known",
            "findings": [
              {
                "value": "files",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-rte-skill-install"
                ],
                "note": "Installer writes SKILL.md and backup/receipt files."
              }
            ],
            "records": [
              "runtime.md#rt-rte-skill-install"
            ],
            "note": "Filesystem deployment is wired; subsequent host consumption is only afforded."
          },
          {
            "scope": "Additional OfficeQA and Spreadsheet callable research controllers (officeqa/loop.py and spreadsheet/loop.py), including promotion and candidate-file resume alternatives",
            "assessment": "uninspected",
            "findings": [],
            "records": [
              "runtime.md#rt-rte-research-evolve",
              "runtime.md#rt-rte-isolated-study"
            ],
            "note": "The accepted epistemic coverage leaves these controllers unassessed; the named engine/study records do not enumerate them. Their storage_substrate cannot be inferred from the inspected routes."
          }
        ],
        "records": [
          "memory.md#mem-obj-patterns",
          "memory.md#mem-obj-feedback",
          "memory.md#mem-obj-skill",
          "memory.md#mem-obj-experience",
          "runtime.md#rt-obj-product-journal",
          "memory.md#mem-obj-research-wiki",
          "memory.md#mem-obj-skill-impact",
          "memory.md#mem-obj-research-evidence",
          "memory.md#mem-obj-paper-skills",
          "runtime.md#rt-rte-research-evolve",
          "runtime.md#rt-rte-isolated-study",
          "runtime.md#rt-rte-skill-install"
        ],
        "note": "All classified retained objects use files; the version-control repository is source distribution, not an evidenced operational memory substrate. Additional callable research controllers remain uninspected, so this is not complete system enumeration."
      },
      "representational_form": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Interpreted lesson, feedback, skill, purpose, narrative, rationale and visible trace text at model consumers",
            "assessment": "known",
            "findings": [
              {
                "value": "natural-language",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-patterns",
                  "memory.md#mem-obj-feedback",
                  "memory.md#mem-obj-skill",
                  "memory.md#mem-obj-research-wiki",
                  "memory.md#mem-obj-skill-impact",
                  "memory.md#mem-obj-research-evidence",
                  "memory.md#mem-obj-paper-skills",
                  "memory.md#mem-bap-wiki-authors"
                ],
                "note": "Model authors interpret lessons, feedback, narrated experience and purposes; task executors interpret SKILL bodies."
              }
            ],
            "records": [
              "memory.md#mem-obj-patterns",
              "memory.md#mem-obj-feedback",
              "memory.md#mem-obj-skill",
              "memory.md#mem-obj-research-wiki",
              "memory.md#mem-obj-skill-impact",
              "memory.md#mem-obj-research-evidence",
              "memory.md#mem-obj-paper-skills",
              "memory.md#mem-bap-wiki-authors"
            ],
            "note": "PURPOSE is omitted from task injection but available on the authoring route."
          },
          {
            "scope": "Journal replay, scores, pointers, hashes, source mappings, gate history and named mapping access structures",
            "assessment": "known",
            "findings": [
              {
                "value": "symbolic",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-obj-product-journal",
                  "memory.md#mem-obj-patterns",
                  "memory.md#mem-obj-feedback",
                  "memory.md#mem-obj-experience",
                  "memory.md#mem-obj-skill-impact",
                  "memory.md#mem-obj-paper-skills",
                  "runtime.md#rt-rte-research-evolve"
                ],
                "note": "Localized identifiers, numerical results, gate fields and integrity metadata have fixed code consumers."
              }
            ],
            "records": [
              "runtime.md#rt-obj-product-journal",
              "memory.md#mem-obj-patterns",
              "memory.md#mem-obj-feedback",
              "memory.md#mem-obj-experience",
              "memory.md#mem-obj-skill-impact",
              "memory.md#mem-obj-paper-skills",
              "runtime.md#rt-rte-research-evolve"
            ],
            "note": "The symbolic control path is separate from interpreted natural-language payloads."
          },
          {
            "scope": "Product output payloads and optional caller trace contents",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-experience"
            ],
            "note": "Outputs may be opaque binary; optional trace serialization and meaning are not fixed. The readable result row cannot classify the opaque payload."
          },
          {
            "scope": "Additional OfficeQA and Spreadsheet callable research controllers (officeqa/loop.py and spreadsheet/loop.py), including promotion and candidate-file resume alternatives",
            "assessment": "uninspected",
            "findings": [],
            "records": [
              "runtime.md#rt-rte-research-evolve",
              "runtime.md#rt-rte-isolated-study"
            ],
            "note": "The accepted epistemic coverage leaves these controllers unassessed; the named engine/study records do not enumerate them. Their representational_form cannot be inferred from the inspected routes."
          }
        ],
        "records": [
          "memory.md#mem-obj-patterns",
          "memory.md#mem-obj-feedback",
          "memory.md#mem-obj-skill",
          "memory.md#mem-obj-research-wiki",
          "memory.md#mem-obj-skill-impact",
          "memory.md#mem-obj-research-evidence",
          "memory.md#mem-obj-paper-skills",
          "memory.md#mem-bap-wiki-authors",
          "runtime.md#rt-obj-product-journal",
          "memory.md#mem-obj-experience",
          "runtime.md#rt-rte-research-evolve",
          "runtime.md#rt-rte-isolated-study"
        ],
        "note": "Natural-language and symbolic parts coexist; external inference weights are not accumulated WikiSkill memory and do not add parametric memory to this boundary. Additional callable research controllers remain uninspected, so this is not complete system enumeration."
      },
      "lineage": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Model-authored procedural lessons, proposals and named skill/purpose revisions",
            "assessment": "known",
            "findings": [
              {
                "value": "authored",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-patterns",
                  "memory.md#mem-obj-skill",
                  "memory.md#mem-obj-research-wiki",
                  "memory.md#mem-obj-paper-skills",
                  "memory.md#mem-rte-paper-adapters"
                ],
                "note": "Maintainer and Proposer author retained content through implemented role submissions."
              }
            ],
            "records": [
              "memory.md#mem-obj-patterns",
              "memory.md#mem-obj-skill",
              "memory.md#mem-obj-research-wiki",
              "memory.md#mem-obj-paper-skills",
              "memory.md#mem-rte-paper-adapters"
            ],
            "note": "Intended computational authorship does not authenticate arbitrary direct submissions."
          },
          {
            "scope": "Retained research instructions derived from selected execution experience",
            "assessment": "known",
            "findings": [
              {
                "value": "trace-extracted",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-research-evidence",
                  "memory.md#mem-obj-research-wiki",
                  "memory.md#mem-obj-paper-skills",
                  "runtime.md#rt-rte-research-evolve",
                  "runtime.md#rt-rte-isolated-study"
                ],
                "note": "Selected execution traces feed Wiki/skill authors and persisted procedural results."
              }
            ],
            "records": [
              "memory.md#mem-obj-research-evidence",
              "memory.md#mem-obj-research-wiki",
              "memory.md#mem-obj-paper-skills",
              "runtime.md#rt-rte-research-evolve",
              "runtime.md#rt-rte-isolated-study"
            ],
            "note": "Wiring establishes a derivation route, not that each actual assertion faithfully follows its source."
          },
          {
            "scope": "Copied initial skill, inherited knowledge and research template pages",
            "assessment": "known",
            "findings": [
              {
                "value": "imported",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-skill",
                  "memory.md#mem-obj-patterns",
                  "memory.md#mem-obj-feedback",
                  "memory.md#mem-obj-research-wiki",
                  "runtime.md#rt-rte-product-round"
                ],
                "note": "Initialization and inheritance copy existing caller or template content into operative memory."
              }
            ],
            "records": [
              "memory.md#mem-obj-skill",
              "memory.md#mem-obj-patterns",
              "memory.md#mem-obj-feedback",
              "memory.md#mem-obj-research-wiki",
              "runtime.md#rt-rte-product-round"
            ],
            "note": "Import is known; provenance before the copied object is not."
          },
          {
            "scope": "Generated indexes, impact projections, trimmed views and reconstructed controller state",
            "assessment": "known",
            "findings": [
              {
                "value": "other-compiled",
                "basis": "wired",
                "records": [
                  "epistemic.md#epi-rte-wiki-index",
                  "memory.md#mem-obj-skill-impact",
                  "memory.md#mem-obj-research-evidence",
                  "runtime.md#rt-obj-product-journal"
                ],
                "note": "Fixed code extracts headings/summaries, projects gate events, trims trace views and replays events."
              }
            ],
            "records": [
              "epistemic.md#epi-rte-wiki-index",
              "memory.md#mem-obj-skill-impact",
              "memory.md#mem-obj-research-evidence",
              "runtime.md#rt-obj-product-journal"
            ],
            "note": "Compilation does not add semantic warrant."
          },
          {
            "scope": "Pre-import origin of caller skills/feedback, template content and opaque task artifacts",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-skill",
              "memory.md#mem-obj-feedback",
              "memory.md#mem-obj-research-wiki",
              "memory.md#mem-obj-experience"
            ],
            "note": "The immediate import is recorded, but original authorship, trace origin and prior transformations are unresolved."
          },
          {
            "scope": "Additional OfficeQA and Spreadsheet callable research controllers (officeqa/loop.py and spreadsheet/loop.py), including promotion and candidate-file resume alternatives",
            "assessment": "uninspected",
            "findings": [],
            "records": [
              "runtime.md#rt-rte-research-evolve",
              "runtime.md#rt-rte-isolated-study"
            ],
            "note": "The accepted epistemic coverage leaves these controllers unassessed; the named engine/study records do not enumerate them. Their lineage cannot be inferred from the inspected routes."
          }
        ],
        "records": [
          "memory.md#mem-obj-patterns",
          "memory.md#mem-obj-skill",
          "memory.md#mem-obj-research-wiki",
          "memory.md#mem-obj-paper-skills",
          "memory.md#mem-rte-paper-adapters",
          "memory.md#mem-obj-research-evidence",
          "runtime.md#rt-rte-research-evolve",
          "runtime.md#rt-rte-isolated-study",
          "memory.md#mem-obj-feedback",
          "runtime.md#rt-rte-product-round",
          "epistemic.md#epi-rte-wiki-index",
          "memory.md#mem-obj-skill-impact",
          "runtime.md#rt-obj-product-journal",
          "memory.md#mem-obj-experience"
        ],
        "note": "Known immediate derivation paths do not resolve initial content provenance. Additional callable research controllers remain uninspected, so this is not complete system enumeration."
      },
      "behavioral_authority": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Patterns, research Wiki, original feedback, purposes and history at learning authors",
            "assessment": "known",
            "findings": [
              {
                "value": "knowledge",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-patterns",
                  "memory.md#mem-obj-feedback",
                  "memory.md#mem-obj-research-wiki",
                  "memory.md#mem-obj-paper-skills",
                  "memory.md#mem-obj-skill-impact",
                  "memory.md#mem-bap-wiki-authors"
                ],
                "note": "Retained text and history supply evidence, reference and authoring advice."
              },
              {
                "value": "instruction",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-patterns",
                  "memory.md#mem-obj-feedback",
                  "memory.md#mem-obj-research-wiki",
                  "memory.md#mem-obj-paper-skills",
                  "memory.md#mem-obj-skill-impact",
                  "memory.md#mem-bap-wiki-authors"
                ],
                "note": "Procedural guidance and explicit original requirements direct subsequent authors; requirements are requested as design constraints, not verified truths."
              }
            ],
            "records": [
              "memory.md#mem-obj-patterns",
              "memory.md#mem-obj-feedback",
              "memory.md#mem-obj-research-wiki",
              "memory.md#mem-obj-paper-skills",
              "memory.md#mem-obj-skill-impact",
              "memory.md#mem-bap-wiki-authors"
            ],
            "note": "Knowledge and instruction apply to the interpreted portions, not every metadata field."
          },
          {
            "scope": "Retained execution evidence and Wiki at automatic procedural-update consumers",
            "assessment": "known",
            "findings": [
              {
                "value": "learning",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-experience",
                  "memory.md#mem-obj-research-evidence",
                  "memory.md#mem-obj-patterns",
                  "memory.md#mem-obj-research-wiki",
                  "runtime.md#rt-rte-research-evolve",
                  "runtime.md#rt-rte-isolated-study",
                  "memory.md#mem-rte-paper-adapters"
                ],
                "note": "Retained experience and Wiki feed updates to durable Wiki pages or procedural skills."
              }
            ],
            "records": [
              "memory.md#mem-obj-experience",
              "memory.md#mem-obj-research-evidence",
              "memory.md#mem-obj-patterns",
              "memory.md#mem-obj-research-wiki",
              "runtime.md#rt-rte-research-evolve",
              "runtime.md#rt-rte-isolated-study",
              "memory.md#mem-rte-paper-adapters"
            ],
            "note": "Learning authority names the update consumer; it does not assert observed improved capacity."
          },
          {
            "scope": "Retained SKILL bodies at later task executors",
            "assessment": "known",
            "findings": [
              {
                "value": "instruction",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-skill",
                  "memory.md#mem-obj-paper-skills",
                  "runtime.md#rt-bap-skill-consumption"
                ],
                "note": "Selected procedural bodies enter later task payloads or system prompts, under host policy."
              }
            ],
            "records": [
              "memory.md#mem-obj-skill",
              "memory.md#mem-obj-paper-skills",
              "runtime.md#rt-bap-skill-consumption"
            ],
            "note": "PURPOSE does not accompany task injection; delivered instructions grant no new permissions."
          },
          {
            "scope": "Journal adoption/request metadata and research resume records at controllers",
            "assessment": "known",
            "findings": [
              {
                "value": "routing",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-obj-product-journal",
                  "runtime.md#rt-rte-product-round",
                  "runtime.md#rt-rte-research-evolve"
                ],
                "note": "Replayed phase/current-skill state and retained proposal/completion/outcome records select next work, incumbent and resume behavior."
              },
              {
                "value": "validation",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-obj-product-journal",
                  "runtime.md#rt-rte-product-round",
                  "runtime.md#rt-rte-research-evolve"
                ],
                "note": "Stored hashes and identities are criteria for artifact consistency and reuse."
              },
              {
                "value": "enforcement",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-obj-product-journal",
                  "runtime.md#rt-rte-product-round",
                  "runtime.md#rt-rte-research-evolve"
                ],
                "note": "Failed consistency checks refuse progression or changed checkpoint reuse."
              }
            ],
            "records": [
              "runtime.md#rt-obj-product-journal",
              "runtime.md#rt-rte-product-round",
              "runtime.md#rt-rte-research-evolve"
            ],
            "note": "These are retained control parts, not authority attributed to natural-language lessons."
          },
          {
            "scope": "Original explicit-intent source IDs at feedback finish",
            "assessment": "known",
            "findings": [
              {
                "value": "validation",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-feedback",
                  "runtime.md#rt-rte-feedback-gate"
                ],
                "note": "Recorded requirement-source IDs constrain admissible fulfillment checks."
              },
              {
                "value": "enforcement",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-feedback",
                  "runtime.md#rt-rte-feedback-gate"
                ],
                "note": "Unrecorded explicit-intent sources cause rejection of the submitted requirement checks."
              }
            ],
            "records": [
              "memory.md#mem-obj-feedback",
              "runtime.md#rt-rte-feedback-gate"
            ],
            "note": "Caller-provided fulfillment judgments remain unverified."
          },
          {
            "scope": "Opaque product outputs and optional traces at later authors",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-experience"
            ],
            "note": "The evidence route is known, but payload-specific authority cannot be classified from a result row alone."
          },
          {
            "scope": "Additional OfficeQA and Spreadsheet callable research controllers (officeqa/loop.py and spreadsheet/loop.py), including promotion and candidate-file resume alternatives",
            "assessment": "uninspected",
            "findings": [],
            "records": [
              "runtime.md#rt-rte-research-evolve",
              "runtime.md#rt-rte-isolated-study"
            ],
            "note": "The accepted epistemic coverage leaves these controllers unassessed; the named engine/study records do not enumerate them. Their behavioral_authority cannot be inferred from the inspected routes."
          }
        ],
        "records": [
          "memory.md#mem-obj-patterns",
          "memory.md#mem-obj-feedback",
          "memory.md#mem-obj-research-wiki",
          "memory.md#mem-obj-paper-skills",
          "memory.md#mem-obj-skill-impact",
          "memory.md#mem-bap-wiki-authors",
          "memory.md#mem-obj-experience",
          "memory.md#mem-obj-research-evidence",
          "runtime.md#rt-rte-research-evolve",
          "runtime.md#rt-rte-isolated-study",
          "memory.md#mem-rte-paper-adapters",
          "memory.md#mem-obj-skill",
          "runtime.md#rt-bap-skill-consumption",
          "runtime.md#rt-obj-product-journal",
          "runtime.md#rt-rte-product-round",
          "runtime.md#rt-rte-feedback-gate"
        ],
        "note": "Actual consumers distinguish authoring knowledge, update learning, downstream instruction and retained control forces; no ranking positive is established by staged-file availability. Additional callable research controllers remain uninspected, so this is not complete system enumeration."
      },
      "write_agency": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Role-produced Wiki/pattern edits, candidate submission and software successor admission",
            "assessment": "known",
            "findings": [
              {
                "value": "automatic",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-patterns",
                  "memory.md#mem-obj-research-wiki",
                  "memory.md#mem-obj-skill",
                  "memory.md#mem-obj-paper-skills",
                  "runtime.md#rt-rte-product-round",
                  "runtime.md#rt-rte-feedback-gate",
                  "runtime.md#rt-rte-research-evolve",
                  "runtime.md#rt-rte-isolated-study",
                  "memory.md#mem-rte-paper-adapters"
                ],
                "note": "Model/software admission does not require a separate human decision approving each retained item."
              }
            ],
            "records": [
              "memory.md#mem-obj-patterns",
              "memory.md#mem-obj-research-wiki",
              "memory.md#mem-obj-skill",
              "memory.md#mem-obj-paper-skills",
              "runtime.md#rt-rte-product-round",
              "runtime.md#rt-rte-feedback-gate",
              "runtime.md#rt-rte-research-evolve",
              "runtime.md#rt-rte-isolated-study",
              "memory.md#mem-rte-paper-adapters"
            ],
            "note": "Starting a run, configuring a scorer or supplying verdicts does not make subsequent content admission manual."
          },
          {
            "scope": "Derived context views, event/history writes and checkpoint persistence",
            "assessment": "known",
            "findings": [
              {
                "value": "automatic",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-obj-product-journal",
                  "memory.md#mem-obj-skill-impact",
                  "memory.md#mem-obj-research-evidence",
                  "runtime.md#rt-rte-research-evolve"
                ],
                "note": "Controller code generates projections, persists events and records checkpoint artifacts."
              }
            ],
            "records": [
              "runtime.md#rt-obj-product-journal",
              "memory.md#mem-obj-skill-impact",
              "memory.md#mem-obj-research-evidence",
              "runtime.md#rt-rte-research-evolve"
            ],
            "note": "Physical writes and content control are distinguished."
          },
          {
            "scope": "Initial skill/feedback/task-evidence supply, generic direct submissions, custom adapter initialization and deployment replacement",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-skill",
              "memory.md#mem-obj-feedback",
              "memory.md#mem-obj-experience",
              "memory.md#mem-obj-research-wiki",
              "runtime.md#rt-rte-skill-install"
            ],
            "note": "Generic callers and origin labels do not establish a human decision. A caller may be human or agent; no manual finding follows merely from an explicit replacement flag."
          },
          {
            "scope": "Additional OfficeQA and Spreadsheet callable research controllers (officeqa/loop.py and spreadsheet/loop.py), including promotion and candidate-file resume alternatives",
            "assessment": "uninspected",
            "findings": [],
            "records": [
              "runtime.md#rt-rte-research-evolve",
              "runtime.md#rt-rte-isolated-study"
            ],
            "note": "The accepted epistemic coverage leaves these controllers unassessed; the named engine/study records do not enumerate them. Their write_agency cannot be inferred from the inspected routes."
          }
        ],
        "records": [
          "memory.md#mem-obj-patterns",
          "memory.md#mem-obj-research-wiki",
          "memory.md#mem-obj-skill",
          "memory.md#mem-obj-paper-skills",
          "runtime.md#rt-rte-product-round",
          "runtime.md#rt-rte-feedback-gate",
          "runtime.md#rt-rte-research-evolve",
          "runtime.md#rt-rte-isolated-study",
          "memory.md#mem-rte-paper-adapters",
          "runtime.md#rt-obj-product-journal",
          "memory.md#mem-obj-skill-impact",
          "memory.md#mem-obj-research-evidence",
          "memory.md#mem-obj-feedback",
          "memory.md#mem-obj-experience",
          "runtime.md#rt-rte-skill-install"
        ],
        "note": "Known automatic role and controller paths coexist with unresolved caller-controlled admission; human authorship is not authenticated. Additional callable research controllers remain uninspected, so this is not complete system enumeration."
      },
      "curation_operations": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Replacement of current named product lessons, research pages and paper skill/Wiki passages",
            "assessment": "known",
            "findings": [
              {
                "value": "evolve",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-patterns",
                  "memory.md#mem-obj-research-wiki",
                  "memory.md#mem-obj-paper-skills",
                  "epistemic.md#epi-rte-paper-contract",
                  "memory.md#mem-rte-paper-adapters"
                ],
                "note": "Name replacement, full-page update and unique local patches revise existing retained entries."
              }
            ],
            "records": [
              "memory.md#mem-obj-patterns",
              "memory.md#mem-obj-research-wiki",
              "memory.md#mem-obj-paper-skills",
              "epistemic.md#epi-rte-paper-contract",
              "memory.md#mem-rte-paper-adapters"
            ],
            "note": "Patch reachability in the empty-skill one-round study is not inferred from the generic adapter capability."
          },
          {
            "scope": "Reduced retained trace views and generated research heading/summary views",
            "assessment": "known",
            "findings": [
              {
                "value": "consolidate",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-research-evidence",
                  "epistemic.md#epi-rte-wiki-index"
                ],
                "note": "Fixed selection/trimming and heading/summary extraction reduce existing retained content for later authors."
              }
            ],
            "records": [
              "memory.md#mem-obj-research-evidence",
              "epistemic.md#epi-rte-wiki-index"
            ],
            "note": "This classifies implemented reduced views, not a guarantee of semantic faithfulness."
          },
          {
            "scope": "Requested semantic consolidation of experience into reusable Wiki lessons",
            "assessment": "known",
            "findings": [
              {
                "value": "consolidate",
                "basis": "claimed",
                "records": [
                  "epistemic.md#epi-clm-wiki-lessons",
                  "memory.md#mem-obj-patterns"
                ],
                "note": "Source doctrine requests consolidation of experience; actual model input/output semantics were not inspected."
              }
            ],
            "records": [
              "epistemic.md#epi-clm-wiki-lessons",
              "memory.md#mem-obj-patterns"
            ],
            "note": "This requested semantic operation is claimed, not upgraded by deterministic view construction."
          },
          {
            "scope": "Semantic relation of model-produced lessons and procedural proposals to their inputs",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-patterns",
              "memory.md#mem-obj-research-wiki",
              "memory.md#mem-obj-skill",
              "epistemic.md#epi-rte-paper-contract"
            ],
            "note": "Accepted records leave reshaping, derivation and non-entailing conjecture unresolved. Neither synthesize nor dedup follows from the role name or schema."
          },
          {
            "scope": "Deployment-copy restoration relative to memory curation vocabulary",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "runtime.md#rt-rte-skill-install"
            ],
            "note": "Checked byte restoration/removal withdraws a deployment copy, not an evidenced historical invalidation of knowledge. No controlled curation value is established for this mechanism."
          },
          {
            "scope": "Additional OfficeQA and Spreadsheet callable research controllers (officeqa/loop.py and spreadsheet/loop.py), including promotion and candidate-file resume alternatives",
            "assessment": "uninspected",
            "findings": [],
            "records": [
              "runtime.md#rt-rte-research-evolve",
              "runtime.md#rt-rte-isolated-study"
            ],
            "note": "The accepted epistemic coverage leaves these controllers unassessed; the named engine/study records do not enumerate them. Their curation_operations cannot be inferred from the inspected routes."
          }
        ],
        "records": [
          "memory.md#mem-obj-patterns",
          "memory.md#mem-obj-research-wiki",
          "memory.md#mem-obj-paper-skills",
          "epistemic.md#epi-rte-paper-contract",
          "memory.md#mem-rte-paper-adapters",
          "memory.md#mem-obj-research-evidence",
          "epistemic.md#epi-rte-wiki-index",
          "epistemic.md#epi-clm-wiki-lessons",
          "memory.md#mem-obj-skill",
          "runtime.md#rt-rte-skill-install",
          "runtime.md#rt-rte-research-evolve",
          "runtime.md#rt-rte-isolated-study"
        ],
        "note": "Implemented evolution and reduced views are retained independently of uncertain semantic transformations; index rebuilding alone is not the warrant for consolidation. Additional callable research controllers remain uninspected, so this is not complete system enumeration."
      },
      "read_back_direction": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Automatic phase/round-specific selection for product and native role/task invocations",
            "assessment": "known",
            "findings": [
              {
                "value": "push",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-rte-product-round",
                  "runtime.md#rt-rte-native-handoff",
                  "memory.md#mem-obj-patterns",
                  "memory.md#mem-obj-feedback"
                ],
                "note": "After work issuance, code selects current patterns/feedback, current-round training evidence, history and candidate/incumbent for later consumers."
              }
            ],
            "records": [
              "runtime.md#rt-rte-product-round",
              "runtime.md#rt-rte-native-handoff",
              "memory.md#mem-obj-patterns",
              "memory.md#mem-obj-feedback"
            ],
            "note": "The work/status request is not a request identifying every selected retained part."
          },
          {
            "scope": "Automatic research/study learning and rollout context assembly",
            "assessment": "known",
            "findings": [
              {
                "value": "push",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-rte-research-evolve",
                  "runtime.md#rt-rte-isolated-study",
                  "memory.md#mem-obj-research-evidence",
                  "memory.md#mem-obj-research-wiki",
                  "memory.md#mem-obj-skill-impact",
                  "memory.md#mem-obj-paper-skills"
                ],
                "note": "Controller selects sampled evidence, incumbent, Wiki and impact summaries for role or task prompts."
              }
            ],
            "records": [
              "runtime.md#rt-rte-research-evolve",
              "runtime.md#rt-rte-isolated-study",
              "memory.md#mem-obj-research-evidence",
              "memory.md#mem-obj-research-wiki",
              "memory.md#mem-obj-skill-impact",
              "memory.md#mem-obj-paper-skills"
            ],
            "note": "Library adapter wiring does not establish default CLI activation."
          },
          {
            "scope": "Explicit staged-file requests by research learning models",
            "assessment": "known",
            "findings": [
              {
                "value": "pull",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-research-evidence",
                  "memory.md#mem-obj-research-wiki",
                  "memory.md#mem-rte-paper-adapters",
                  "runtime.md#rt-rte-isolated-study"
                ],
                "note": "Model read_file or equivalent exact-file reads return requested retained trace/page content."
              }
            ],
            "records": [
              "memory.md#mem-obj-research-evidence",
              "memory.md#mem-obj-research-wiki",
              "memory.md#mem-rte-paper-adapters",
              "runtime.md#rt-rte-isolated-study"
            ],
            "note": "A requested file return is not an additional push."
          },
          {
            "scope": "External host consumption after retained-skill export, installation or restoration",
            "assessment": "uninspected",
            "findings": [],
            "records": [
              "runtime.md#rt-rte-skill-install"
            ],
            "note": "Export/install/restore wire filesystem effects, not an independent later-consumer invocation. Future host consumption is afforded, but its request/selection/delivery operations are uninspected; neither pull nor push is established for that external route."
          },
          {
            "scope": "Additional OfficeQA and Spreadsheet callable research controllers (officeqa/loop.py and spreadsheet/loop.py), including promotion and candidate-file resume alternatives",
            "assessment": "uninspected",
            "findings": [],
            "records": [
              "runtime.md#rt-rte-research-evolve",
              "runtime.md#rt-rte-isolated-study"
            ],
            "note": "The accepted epistemic coverage leaves these controllers unassessed; the named engine/study records do not enumerate them. Their read_back_direction cannot be inferred from the inspected routes."
          }
        ],
        "records": [
          "runtime.md#rt-rte-product-round",
          "runtime.md#rt-rte-native-handoff",
          "memory.md#mem-obj-patterns",
          "memory.md#mem-obj-feedback",
          "runtime.md#rt-rte-research-evolve",
          "runtime.md#rt-rte-isolated-study",
          "memory.md#mem-obj-research-evidence",
          "memory.md#mem-obj-research-wiki",
          "memory.md#mem-obj-skill-impact",
          "memory.md#mem-obj-paper-skills",
          "memory.md#mem-rte-paper-adapters",
          "runtime.md#rt-rte-skill-install"
        ],
        "note": "Push selection and downstream on-demand pull occur in the same chains; requested work and requested files are not conflated. Additional callable research controllers remain uninspected, so this is not complete system enumeration."
      },
      "read_back_signal": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Product/native automatic learning-context and task-skill push",
            "assessment": "known",
            "findings": [
              {
                "value": "identifier",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-rte-product-round",
                  "runtime.md#rt-rte-native-handoff",
                  "memory.md#mem-obj-patterns",
                  "memory.md#mem-obj-feedback"
                ],
                "note": "Phase/round/request status and current-skill identity select current-round training records and the active candidate/incumbent."
              },
              {
                "value": "coarse",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-rte-product-round",
                  "runtime.md#rt-rte-native-handoff",
                  "memory.md#mem-obj-patterns",
                  "memory.md#mem-obj-feedback"
                ],
                "note": "All current patterns and all original feedback are included without topic relevance selection."
              }
            ],
            "records": [
              "runtime.md#rt-rte-product-round",
              "runtime.md#rt-rte-native-handoff",
              "memory.md#mem-obj-patterns",
              "memory.md#mem-obj-feedback"
            ],
            "note": "Trigger is work issuance; selectors use controller state, delivering evidence/history to authors or skill to executor."
          },
          {
            "scope": "Default research and isolated-study automatic evidence/context push",
            "assessment": "known",
            "findings": [
              {
                "value": "coarse",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-research-evidence",
                  "runtime.md#rt-rte-research-evolve",
                  "runtime.md#rt-rte-isolated-study",
                  "memory.md#mem-obj-research-wiki",
                  "memory.md#mem-obj-skill-impact"
                ],
                "note": "Learning triggers select bounded failures/successes, sorted eligible traces and fixed whole-Wiki/index/history portions; limits and trimming are coarse selection."
              },
              {
                "value": "identifier",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-research-evidence",
                  "runtime.md#rt-rte-research-evolve",
                  "runtime.md#rt-rte-isolated-study",
                  "memory.md#mem-obj-research-wiki",
                  "memory.md#mem-obj-skill-impact"
                ],
                "note": "Accepted/incumbent identity selects the retained skill inserted into subsequent task invocations or accepted skill mapping supplied to later authors."
              }
            ],
            "records": [
              "memory.md#mem-obj-research-evidence",
              "runtime.md#rt-rte-research-evolve",
              "runtime.md#rt-rte-isolated-study",
              "memory.md#mem-obj-research-wiki",
              "memory.md#mem-obj-skill-impact"
            ],
            "note": "Sampling by outcome and budgets is not embedding or lexical relevance retrieval. Optional exact-file pulls add no push signal."
          },
          {
            "scope": "External host discovery of installed retained skill",
            "assessment": "uninspected",
            "findings": [],
            "records": [
              "runtime.md#rt-rte-skill-install"
            ],
            "note": "Installation affords later host consumption but does not inspect its trigger or selector. No inferred-judgment or identifier push follows from a filename alone."
          },
          {
            "scope": "Additional OfficeQA and Spreadsheet callable research controllers (officeqa/loop.py and spreadsheet/loop.py), including promotion and candidate-file resume alternatives",
            "assessment": "uninspected",
            "findings": [],
            "records": [
              "runtime.md#rt-rte-research-evolve",
              "runtime.md#rt-rte-isolated-study"
            ],
            "note": "The accepted epistemic coverage leaves these controllers unassessed; the named engine/study records do not enumerate them. Their read_back_signal cannot be inferred from the inspected routes."
          }
        ],
        "records": [
          "runtime.md#rt-rte-product-round",
          "runtime.md#rt-rte-native-handoff",
          "memory.md#mem-obj-patterns",
          "memory.md#mem-obj-feedback",
          "memory.md#mem-obj-research-evidence",
          "runtime.md#rt-rte-research-evolve",
          "runtime.md#rt-rte-isolated-study",
          "memory.md#mem-obj-research-wiki",
          "memory.md#mem-obj-skill-impact",
          "runtime.md#rt-rte-skill-install"
        ],
        "note": "Known push signals name actual selected parts; opaque host discovery and unassessed controllers prevent complete selector coverage. Additional callable research controllers remain uninspected, so this is not complete system enumeration."
      },
      "trace_learning": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Default research trace-to-Wiki-to-skill and paper/study trace-fed durable instruction paths",
            "assessment": "known",
            "findings": [
              {
                "value": "yes",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-research-evidence",
                  "memory.md#mem-obj-research-wiki",
                  "memory.md#mem-obj-paper-skills",
                  "runtime.md#rt-rte-research-evolve",
                  "runtime.md#rt-rte-isolated-study",
                  "memory.md#mem-rte-paper-adapters"
                ],
                "note": "Execution experience feeds automatic Wiki/skill writes, with later Proposer or task-executor consumption wired."
              }
            ],
            "records": [
              "memory.md#mem-obj-research-evidence",
              "memory.md#mem-obj-research-wiki",
              "memory.md#mem-obj-paper-skills",
              "runtime.md#rt-rte-research-evolve",
              "runtime.md#rt-rte-isolated-study",
              "memory.md#mem-rte-paper-adapters"
            ],
            "note": "In the one-round study, Maintainer Wiki reaches Proposer and candidate reaches validation; no second deployed final-skill round is implied."
          },
          {
            "scope": "Product optional-trace-to-pattern/skill route",
            "assessment": "partial",
            "findings": [
              {
                "value": "yes",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-experience",
                  "memory.md#mem-obj-patterns",
                  "memory.md#mem-obj-skill",
                  "runtime.md#rt-rte-product-round"
                ],
                "note": "Optional task traces can feed automatic lesson and skill production for later invocations; trace supply and actual use remain conditional."
              }
            ],
            "records": [
              "memory.md#mem-obj-experience",
              "memory.md#mem-obj-patterns",
              "memory.md#mem-obj-skill",
              "runtime.md#rt-rte-product-round"
            ],
            "note": "A qualifying trace-fed update is wired when optional traces contain execution experience; outputs/scores/feedback alone do not establish universal trace origin."
          },
          {
            "scope": "Opaque caller-supplied experience and custom adapter alternatives",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-experience",
              "memory.md#mem-rte-paper-adapters",
              "runtime.md#rt-rte-research-evolve"
            ],
            "note": "Payload origin and alternative callback behavior are unresolved; no system-wide no or bounded absence is established."
          },
          {
            "scope": "Additional OfficeQA and Spreadsheet callable research controllers (officeqa/loop.py and spreadsheet/loop.py), including promotion and candidate-file resume alternatives",
            "assessment": "uninspected",
            "findings": [],
            "records": [
              "runtime.md#rt-rte-research-evolve",
              "runtime.md#rt-rte-isolated-study"
            ],
            "note": "The accepted epistemic coverage leaves these controllers unassessed; the named engine/study records do not enumerate them. Their trace_learning cannot be inferred from the inspected routes."
          }
        ],
        "records": [
          "memory.md#mem-obj-research-evidence",
          "memory.md#mem-obj-research-wiki",
          "memory.md#mem-obj-paper-skills",
          "runtime.md#rt-rte-research-evolve",
          "runtime.md#rt-rte-isolated-study",
          "memory.md#mem-rte-paper-adapters",
          "memory.md#mem-obj-experience",
          "memory.md#mem-obj-patterns",
          "memory.md#mem-obj-skill",
          "runtime.md#rt-rte-product-round"
        ],
        "note": "Positive trace-fed procedural updates do not require weight training, novel knowledge, observed compliance or demonstrated improvement. Additional callable research controllers remain uninspected, so this is not complete system enumeration."
      },
      "trace_source": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Default research selected linked execution experience",
            "assessment": "known",
            "findings": [
              {
                "value": "tool-traces",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-research-evidence",
                  "runtime.md#rt-rte-research-evolve"
                ],
                "note": "Recognized tool requests/results and execution feedback feed Wiki/skill authors."
              },
              {
                "value": "trajectories",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-research-evidence",
                  "runtime.md#rt-rte-research-evolve"
                ],
                "note": "Linked task execution, outcomes and selected success/failure cases feed procedural updates."
              }
            ],
            "records": [
              "memory.md#mem-obj-research-evidence",
              "runtime.md#rt-rte-research-evolve"
            ],
            "note": "These findings concern source content, not a JSON/event serialization label."
          },
          {
            "scope": "Paper/study visible-trace tool-receipt and session-item alternatives",
            "assessment": "partial",
            "findings": [
              {
                "value": "tool-traces",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-research-evidence",
                  "memory.md#mem-obj-paper-skills",
                  "memory.md#mem-rte-paper-adapters",
                  "runtime.md#rt-rte-isolated-study"
                ],
                "note": "Tool receipts and recorded command/output experience feed learning-role views."
              },
              {
                "value": "trajectories",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-research-evidence",
                  "memory.md#mem-obj-paper-skills",
                  "memory.md#mem-rte-paper-adapters",
                  "runtime.md#rt-rte-isolated-study"
                ],
                "note": "Case-linked execution and final prediction/outcome supply multi-step experience to automatic Wiki/skill authors."
              }
            ],
            "records": [
              "memory.md#mem-obj-research-evidence",
              "memory.md#mem-obj-paper-skills",
              "memory.md#mem-rte-paper-adapters",
              "runtime.md#rt-rte-isolated-study"
            ],
            "note": "Tool receipts and case-linked execution support the positive findings. The fallback is recorded only as visible session call/output items; accepted records do not establish conversational turns or fully classify that alternative's source content. Its session container does not warrant session-logs, and the unresolved fallback prevents complete unit coverage."
          },
          {
            "scope": "Product optional trace payloads and mixed imported/caller training evidence",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-experience",
              "memory.md#mem-obj-patterns",
              "memory.md#mem-rte-paper-adapters"
            ],
            "note": "Original activity content is not fixed by trace.txt or caller metadata. No event-streams value follows from journal wrapping, and no complete source classification is possible."
          },
          {
            "scope": "Additional OfficeQA and Spreadsheet callable research controllers (officeqa/loop.py and spreadsheet/loop.py), including promotion and candidate-file resume alternatives",
            "assessment": "uninspected",
            "findings": [],
            "records": [
              "runtime.md#rt-rte-research-evolve",
              "runtime.md#rt-rte-isolated-study"
            ],
            "note": "The accepted epistemic coverage leaves these controllers unassessed; the named engine/study records do not enumerate them. Their trace_source cannot be inferred from the inspected routes."
          }
        ],
        "records": [
          "memory.md#mem-obj-research-evidence",
          "runtime.md#rt-rte-research-evolve",
          "memory.md#mem-obj-paper-skills",
          "memory.md#mem-rte-paper-adapters",
          "runtime.md#rt-rte-isolated-study",
          "memory.md#mem-obj-experience",
          "memory.md#mem-obj-patterns"
        ],
        "note": "Trace-source findings attach only to qualifying automatic writes; ordinary static imports and integrity events are not automatically trace sources. Additional callable research controllers remain uninspected, so this is not complete system enumeration."
      }
    }
  }
}
---

# WikiSkill memory profile

## Comparison rationale

All positive findings classify accepted implementation or doctrine records, not an observed run. Files contain interpreted procedural text and separately consumed symbolic metadata. Model weights belong to external inference components, not to the retained memory updated by WikiSkill. Whole-runtime permissions and packaged static role guidance therefore do not become memory-axis values.

The reconciliation supersedes the epistemic product-pattern declaration with [MEM-OBJ-patterns](memory.md#mem-obj-patterns). This profile cites that canonical object throughout. The product journal remains a distinct control container, and research Wiki, impact views and paper SKILL/PURPOSE mappings remain separate operative parts. Their different consumers prevent flattening them into a single instruction object.

Trace learning is a wired update path, not evidence of improved capacity. Selected experience can update Wiki, Wiki can shape a procedural proposal, and retained or candidate instructions can reach a later invocation. The study's Maintainer-to-Proposer bridge qualifies without inventing a second final-skill deployment. [MEM-OBJ-research-evidence](memory.md#mem-obj-research-evidence), [MEM-OBJ-paper-skills](memory.md#mem-obj-paper-skills) and [RT-RTE-isolated-study](runtime.md#rt-rte-isolated-study) retain those horizons. Opaque product output and optional trace origin remain unresolved rather than receiving a universal trace-source value.

Semantic consolidation requested of a model stays claimed. Deterministic reduced trace views and extracted summary views support a separate wired consolidation finding; replacement and local patches support evolution. No actual input/output semantic comparison establishes synthesis. Skill-gate rejection preserves Wiki rather than invalidating its claims. Deployment restoration changes checked bytes, not knowledge history. These distinctions follow [MEM-OBJ-research-evidence](memory.md#mem-obj-research-evidence), [EPI-RTE-wiki-index](epistemic.md#epi-rte-wiki-index), [EPI-RTE-paper-contract](epistemic.md#epi-rte-paper-contract) and [RT-RTE-skill-install](runtime.md#rt-rte-skill-install).

Each axis retains an uninspected unit for additional callable OfficeQA/Spreadsheet controllers, including promotion and candidate-file resume paths named in the accepted epistemic coverage. The broad engine/study records do not resolve those alternatives. That inventory limit prevents complete system classification even where every named inspected object uses files. Generic callers similarly prevent a manual write-agency finding, and an opaque output cannot inherit the representation or authority of its displayed result row. Uninspected host discovery does not acquire a push selector from the installed filename.

The paper/study trace-source unit retains tool-traces and trajectories but is partial: [MEM-OBJ-research-evidence](memory.md#mem-obj-research-evidence) names session call/output fallback items without establishing recorded conversational turns. No session-logs finding follows from the container name; the fallback's source content remains unresolved locally.

Export, installation and restoration are filesystem operations, not an independently wired pull read-back route. [RT-RTE-skill-install](runtime.md#rt-rte-skill-install) affords future host consumption without establishing its request, selector or delivery into a later invocation. That direction unit remains uninspected with no positive finding. The separate staged-file model pull remains wired on its own records.

No source files were read for this profile. All classifications use the supplied accepted records and annotations; no records, quotations or new evidence were added.
