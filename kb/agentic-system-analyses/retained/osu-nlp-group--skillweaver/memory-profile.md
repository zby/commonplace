---
{
  "type": "agentic-system-analyses/types/agentic-system-memory-profile.md",
  "description": "SkillWeaver memory comparison: retained procedural skills, documentation, metadata, experience artifacts and optional access cache at the frozen revision.",
  "run-id": "AAS-2026-10-14-skillweaver-c921cc7a5ed0-01",
  "source-identity": "https://github.com/OSU-NLP-Group/SkillWeaver",
  "reviewed-boundary": "f2a63d65d0f6ff46ac30e817cede8797f8f25b97",
  "memory-comparison": {
    "version": 2,
    "scope": "Includes live and checkpointed Python skill bodies, documentation/signatures, test/version/reference metadata, loaded semantic text, raw browser/action artifacts, selected trajectories, synthesis/success diagnostics, retained benchmark results and optional embedding access cache; includes their initial/imported and subsequent write/read paths. Excludes static shipped instructions as memory, provider parameters/internal retention, website/authentication state and external Browser-Use context management. Shipped skill content is an initial input with unresolved provenance, not observed learning.",
    "axes": {
      "storage_substrate": {
        "assessment": "known",
        "units": [
          {
            "scope": "Skill bodies, embedded documentation, function metadata and semantic text",
            "assessment": "known",
            "findings": [
              {
                "value": "files",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-code",
                  "memory.md#mem-obj-docstring",
                  "memory.md#mem-obj-metadata",
                  "memory.md#mem-obj-semantic-knowledge"
                ],
                "note": "Code, JSON metadata and semantic text persist in prefix files."
              },
              {
                "value": "in-memory",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-code",
                  "memory.md#mem-obj-docstring",
                  "memory.md#mem-obj-metadata",
                  "memory.md#mem-obj-semantic-knowledge"
                ],
                "note": "Live library strings, dictionaries and parsed functions carry the shared working library."
              }
            ],
            "records": [
              "memory.md#mem-obj-code",
              "memory.md#mem-obj-docstring",
              "memory.md#mem-obj-metadata",
              "memory.md#mem-obj-semantic-knowledge"
            ],
            "note": "Checkpoint files and live strings/dictionaries are separately supported substrates."
          },
          {
            "scope": "Raw observations/actions, selected episode, synthesis/success diagnostics and benchmark result artifacts",
            "assessment": "known",
            "findings": [
              {
                "value": "files",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-traces",
                  "epistemic.md#epi-rte-score-retention"
                ],
                "note": "Per-attempt artifacts and eval.json retain these parts."
              },
              {
                "value": "in-memory",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-traces",
                  "epistemic.md#epi-rte-score-retention"
                ],
                "note": "Lists, strings and result dictionaries precede persistence."
              }
            ],
            "records": [
              "memory.md#mem-obj-traces",
              "epistemic.md#epi-rte-score-retention"
            ],
            "note": "Disk artifacts and transient structures are recorded; evaluator entry defects do not erase local output wiring."
          },
          {
            "scope": "Optional exact-text embedding cache",
            "assessment": "known",
            "findings": [
              {
                "value": "in-memory",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-embedding-selection",
                  "runtime.md#rt-cmp-embed"
                ],
                "note": "Dense vectors are cached by input string."
              }
            ],
            "records": [
              "memory.md#mem-rte-embedding-selection",
              "runtime.md#rt-cmp-embed"
            ],
            "note": "This is a process-local cache, not a persisted vector database."
          }
        ],
        "records": [
          "memory.md#mem-obj-code",
          "memory.md#mem-obj-docstring",
          "memory.md#mem-obj-metadata",
          "memory.md#mem-obj-semantic-knowledge",
          "memory.md#mem-obj-traces",
          "epistemic.md#epi-rte-score-retention",
          "memory.md#mem-rte-embedding-selection",
          "runtime.md#rt-cmp-embed"
        ],
        "note": "The recorded inventory covers local retained content, diagnostics, scores and optional derived access cache. External model parameters and website state are not learned-library objects."
      },
      "representational_form": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Executable definitions, signatures, metadata, structured action records and score fields",
            "assessment": "known",
            "findings": [
              {
                "value": "symbolic",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-code",
                  "memory.md#mem-obj-docstring",
                  "memory.md#mem-obj-metadata",
                  "memory.md#mem-obj-traces",
                  "epistemic.md#epi-rte-score-retention"
                ],
                "note": "Python procedures, signatures, counters and serialized execution/check fields have localized fixed-rule consumers."
              }
            ],
            "records": [
              "memory.md#mem-obj-code",
              "memory.md#mem-obj-docstring",
              "memory.md#mem-obj-metadata",
              "memory.md#mem-obj-traces",
              "epistemic.md#epi-rte-score-retention"
            ],
            "note": "Fixed Python/schema/field consumers establish symbolic parts, not all content embedded in those structures."
          },
          {
            "scope": "Skill documentation, semantic text at its intended prompt path and textual episode/diagnostic reasoning",
            "assessment": "partial",
            "findings": [
              {
                "value": "natural-language",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-docstring",
                  "memory.md#mem-obj-semantic-knowledge",
                  "memory.md#mem-obj-traces"
                ],
                "note": "Explanations, usage reports, browser text and model reasoning are interpreted as context."
              }
            ],
            "records": [
              "memory.md#mem-obj-docstring",
              "memory.md#mem-obj-semantic-knowledge",
              "memory.md#mem-obj-traces"
            ],
            "note": "The intended semantic-text path is text context, but arbitrary loaded file content is not audited."
          },
          {
            "scope": "Optional cached dense embeddings",
            "assessment": "known",
            "findings": [
              {
                "value": "parametric",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-embedding-selection",
                  "runtime.md#rt-cmp-embed"
                ],
                "note": "Dense vectors encode description/task similarity; this is not a local weight update."
              }
            ],
            "records": [
              "memory.md#mem-rte-embedding-selection",
              "runtime.md#rt-cmp-embed"
            ],
            "note": "Numerical distributed representations are distinct from the symbolic cache keys."
          },
          {
            "scope": "Saved screenshots and visual observation payloads",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-traces"
            ],
            "note": "Images are retained, but records do not establish one of the three controlled consumption forms for their visual payload."
          }
        ],
        "records": [
          "memory.md#mem-obj-code",
          "memory.md#mem-obj-docstring",
          "memory.md#mem-obj-metadata",
          "memory.md#mem-obj-traces",
          "epistemic.md#epi-rte-score-retention",
          "memory.md#mem-obj-semantic-knowledge",
          "memory.md#mem-rte-embedding-selection",
          "runtime.md#rt-cmp-embed"
        ],
        "note": "Text, code, metadata and dense access representations are classified separately. Recorded screenshots do not have an established controlled form; arbitrary imported semantic payloads are unaudited."
      },
      "lineage": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Practice-derived skill bodies and documentation",
            "assessment": "known",
            "findings": [
              {
                "value": "trace-extracted",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-code",
                  "memory.md#mem-obj-docstring",
                  "runtime.md#rt-rte-skill-admission"
                ],
                "note": "Task experience feeds model synthesis into reusable code/documentation."
              }
            ],
            "records": [
              "memory.md#mem-obj-code",
              "memory.md#mem-obj-docstring",
              "runtime.md#rt-rte-skill-admission"
            ],
            "note": "The inspected builder derivation is distinct from arbitrary initial content."
          },
          {
            "scope": "Loaded initial library, documentation, metadata and semantic text",
            "assessment": "partial",
            "findings": [
              {
                "value": "imported",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-code",
                  "memory.md#mem-obj-docstring",
                  "memory.md#mem-obj-metadata",
                  "memory.md#mem-obj-semantic-knowledge"
                ],
                "note": "Caller-selected prefixes supply existing retained content."
              }
            ],
            "records": [
              "memory.md#mem-obj-code",
              "memory.md#mem-obj-docstring",
              "memory.md#mem-obj-metadata",
              "memory.md#mem-obj-semantic-knowledge"
            ],
            "note": "Import is established; original authorship, prior transformations and approval are not."
          },
          {
            "scope": "Automatically maintained test/version metadata",
            "assessment": "known",
            "findings": [
              {
                "value": "other-compiled",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-metadata",
                  "epistemic.md#epi-rte-tested-label"
                ],
                "note": "Software derives counters, references and events rather than importing a verified test history."
              }
            ],
            "records": [
              "memory.md#mem-obj-metadata",
              "epistemic.md#epi-rte-tested-label"
            ],
            "note": "Programmatic fields are compiled from update bookkeeping and the recorded test predicate."
          },
          {
            "scope": "Recorded browser/action experience and selected episode",
            "assessment": "known",
            "findings": [
              {
                "value": "trace-extracted",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-traces"
                ],
                "note": "Browser observations, generated actions and execution feedback are recorded as experience."
              },
              {
                "value": "other-compiled",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-traces",
                  "epistemic.md#epi-rte-trajectory-format"
                ],
                "note": "The formatter selects and serializes fields into an episode without a model-authored summary."
              }
            ],
            "records": [
              "memory.md#mem-obj-traces",
              "epistemic.md#epi-rte-trajectory-format"
            ],
            "note": "Raw recording and deterministic selective rendering are distinct derivations."
          },
          {
            "scope": "Success/synthesis diagnostics and benchmark score artifacts",
            "assessment": "known",
            "findings": [
              {
                "value": "other-compiled",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-traces",
                  "epistemic.md#epi-rte-score-retention",
                  "epistemic.md#epi-rte-success-check"
                ],
                "note": "Model/checker and scoring responses are assembled into retained result structures."
              }
            ],
            "records": [
              "memory.md#mem-obj-traces",
              "epistemic.md#epi-rte-score-retention",
              "epistemic.md#epi-rte-success-check"
            ],
            "note": "Recorded model/checker outputs and evaluator results are derived artifacts."
          },
          {
            "scope": "Optional embedding cache derivation",
            "assessment": "partial",
            "findings": [
              {
                "value": "other-compiled",
                "basis": "afforded",
                "records": [
                  "memory.md#mem-rte-embedding-selection",
                  "runtime.md#rt-cmp-embed"
                ],
                "note": "Provider vectors are computed from task/description strings and cached."
              }
            ],
            "records": [
              "memory.md#mem-rte-embedding-selection",
              "runtime.md#rt-cmp-embed"
            ],
            "note": "Text-to-vector generation and caching are afforded; provider representation provenance and exact version remain opaque."
          }
        ],
        "records": [
          "memory.md#mem-obj-code",
          "memory.md#mem-obj-docstring",
          "runtime.md#rt-rte-skill-admission",
          "memory.md#mem-obj-metadata",
          "memory.md#mem-obj-semantic-knowledge",
          "epistemic.md#epi-rte-tested-label",
          "memory.md#mem-obj-traces",
          "epistemic.md#epi-rte-trajectory-format",
          "epistemic.md#epi-rte-score-retention",
          "epistemic.md#epi-rte-success-check",
          "memory.md#mem-rte-embedding-selection",
          "runtime.md#rt-cmp-embed"
        ],
        "note": "Known subsequent derivations coexist with unresolved provenance of initial libraries/text and the external embedding representation."
      },
      "behavioral_authority": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Documentation at relevance/action models and registered controller descriptions",
            "assessment": "known",
            "findings": [
              {
                "value": "knowledge",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-docstring",
                  "runtime.md#rt-rte-native-task",
                  "runtime.md#rt-rte-browser-use"
                ],
                "note": "Descriptions supply task-relevant procedural advice and context."
              },
              {
                "value": "ranking",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-docstring",
                  "runtime.md#rt-rte-native-task"
                ],
                "note": "Retained descriptions influence relevance selection among functions."
              }
            ],
            "records": [
              "memory.md#mem-obj-docstring",
              "runtime.md#rt-rte-native-task",
              "runtime.md#rt-rte-browser-use"
            ],
            "note": "This is advisory content, not an enforced obligation to invoke a skill."
          },
          {
            "scope": "Existing skill source/documentation and retained episode at synthesis",
            "assessment": "known",
            "findings": [
              {
                "value": "learning",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-code",
                  "memory.md#mem-obj-docstring",
                  "memory.md#mem-obj-traces",
                  "runtime.md#rt-rte-skill-admission"
                ],
                "note": "Synthesis consumes experience and prior skills to produce later behavior-shaping artifacts."
              }
            ],
            "records": [
              "memory.md#mem-obj-code",
              "memory.md#mem-obj-docstring",
              "memory.md#mem-obj-traces",
              "runtime.md#rt-rte-skill-admission"
            ],
            "note": "Input experience and existing procedures shape a durable library update, separately from downstream execution."
          },
          {
            "scope": "Semantic text at task proposal and procedural synthesis",
            "assessment": "known",
            "findings": [
              {
                "value": "knowledge",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-semantic-knowledge",
                  "runtime.md#rt-rte-explore-practice"
                ],
                "note": "Loaded semantic text supplies context for proposed website tasks."
              },
              {
                "value": "learning",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-semantic-knowledge",
                  "runtime.md#rt-rte-skill-admission"
                ],
                "note": "The procedural update consumes semantic context while revising durable skills."
              }
            ],
            "records": [
              "memory.md#mem-obj-semantic-knowledge",
              "runtime.md#rt-rte-skill-admission",
              "runtime.md#rt-rte-explore-practice"
            ],
            "note": "Read-only semantic context is neither an automatically learned semantic store nor direct native action guidance."
          },
          {
            "scope": "Test/version metadata at visibility, synthesis inclusion and practice scheduler",
            "assessment": "known",
            "findings": [
              {
                "value": "enforcement",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-metadata",
                  "epistemic.md#epi-rte-tested-label"
                ],
                "note": "Counters enforce filtered presentation/inclusion, not a universal execution barrier."
              },
              {
                "value": "routing",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-metadata",
                  "runtime.md#rt-rte-explore-practice"
                ],
                "note": "Tested status determines eligibility and testing versus exploration paths."
              },
              {
                "value": "ranking",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-metadata",
                  "runtime.md#rt-rte-explore-practice"
                ],
                "note": "Version and interaction counts affect relative practice utility."
              }
            ],
            "records": [
              "memory.md#mem-obj-metadata",
              "epistemic.md#epi-rte-tested-label",
              "runtime.md#rt-rte-explore-practice"
            ],
            "note": "These are real policy effects even when the stored test label lacks execution coverage."
          },
          {
            "scope": "Selected episode at success judgment and benchmark scores at reporting",
            "assessment": "known",
            "findings": [
              {
                "value": "knowledge",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-traces",
                  "epistemic.md#epi-rte-success-check",
                  "epistemic.md#epi-rte-score-retention"
                ],
                "note": "Episode content supplies judgment evidence; retained scores supply reporting evidence."
              }
            ],
            "records": [
              "memory.md#mem-obj-traces",
              "epistemic.md#epi-rte-success-check",
              "epistemic.md#epi-rte-score-retention"
            ],
            "note": "Evidence/reporting paths do not grant generalized skill correctness."
          },
          {
            "scope": "Executable bodies at native and controller execution consumers",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-code",
              "runtime.md#rt-bap-library-execution"
            ],
            "note": "Records establish direct symbolic execution and website/host effects, but not standing instruction, action-permission control or another controlled authority solely from executable availability."
          },
          {
            "scope": "Optional embedding selection over retained description vectors",
            "assessment": "known",
            "findings": [
              {
                "value": "ranking",
                "basis": "afforded",
                "records": [
                  "memory.md#mem-rte-embedding-selection"
                ],
                "note": "Dot products order descriptions for top-five return."
              }
            ],
            "records": [
              "memory.md#mem-rte-embedding-selection"
            ],
            "note": "This API is afforded, with no shipped downstream agent caller established."
          },
          {
            "scope": "Export-only tool schemas, unused diagnostics and external planner continuation",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-docstring",
              "memory.md#mem-obj-traces",
              "runtime.md#rt-rte-browser-use"
            ],
            "note": "No recorded later consumer establishes further authority; external planning is outside inspected adapter internals."
          }
        ],
        "records": [
          "memory.md#mem-obj-docstring",
          "runtime.md#rt-rte-native-task",
          "runtime.md#rt-rte-browser-use",
          "memory.md#mem-obj-code",
          "memory.md#mem-obj-traces",
          "runtime.md#rt-rte-skill-admission",
          "memory.md#mem-obj-semantic-knowledge",
          "runtime.md#rt-rte-explore-practice",
          "memory.md#mem-obj-metadata",
          "epistemic.md#epi-rte-tested-label",
          "epistemic.md#epi-rte-success-check",
          "epistemic.md#epi-rte-score-retention",
          "runtime.md#rt-bap-library-execution",
          "memory.md#mem-rte-embedding-selection"
        ],
        "note": "Actual recorded consumers establish local forces. Executable procedures have operational effects not fully captured by this vocabulary; external planner internals and export-only consumers remain unresolved."
      },
      "write_agency": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Model synthesis plus software merge admission",
            "assessment": "known",
            "findings": [
              {
                "value": "automatic",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-rte-skill-admission",
                  "memory.md#mem-obj-code",
                  "memory.md#mem-obj-docstring"
                ],
                "note": "Model/software admit candidate skills; starting exploration is not manual content approval."
              }
            ],
            "records": [
              "runtime.md#rt-rte-skill-admission",
              "memory.md#mem-obj-code",
              "memory.md#mem-obj-docstring"
            ],
            "note": "Success judgment triggers bounded repair and unconditional final merge without per-candidate human approval."
          },
          {
            "scope": "Builder test-counter increments, merge resets and reference-discard initialization",
            "assessment": "known",
            "findings": [
              {
                "value": "automatic",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-metadata",
                  "epistemic.md#epi-rte-tested-label",
                  "runtime.md#rt-rte-explore-practice"
                ],
                "note": "Predicates, merge and loader options govern these mutations."
              }
            ],
            "records": [
              "memory.md#mem-obj-metadata",
              "epistemic.md#epi-rte-tested-label",
              "runtime.md#rt-rte-explore-practice"
            ],
            "note": "These software operations alter retained metadata independently of initial file provenance."
          },
          {
            "scope": "Raw artifact/diagnostic recording and benchmark result retention",
            "assessment": "known",
            "findings": [
              {
                "value": "automatic",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-traces",
                  "epistemic.md#epi-rte-score-retention"
                ],
                "note": "No per-record human admission is wired at these recording steps."
              }
            ],
            "records": [
              "memory.md#mem-obj-traces",
              "epistemic.md#epi-rte-score-retention"
            ],
            "note": "Runtime code records results when the relevant paths execute; benchmark enclosing-entry limits remain."
          },
          {
            "scope": "Optional embedding-cache insertion",
            "assessment": "known",
            "findings": [
              {
                "value": "automatic",
                "basis": "afforded",
                "records": [
                  "memory.md#mem-rte-embedding-selection",
                  "runtime.md#rt-cmp-embed"
                ],
                "note": "Cache insertion follows provider response, not operator approval."
              }
            ],
            "records": [
              "memory.md#mem-rte-embedding-selection",
              "runtime.md#rt-cmp-embed"
            ],
            "note": "On API invocation software caches returned vectors."
          },
          {
            "scope": "Initial code/documentation/metadata/semantic content, blanket test marking and separately supplied replacement checkpoints",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-code",
              "memory.md#mem-obj-docstring",
              "memory.md#mem-obj-metadata",
              "memory.md#mem-obj-semantic-knowledge",
              "epistemic.md#epi-rte-tested-label"
            ],
            "note": "Generic caller/file provenance does not identify the admission principal or prove manual approval. No manual finding follows from selecting a prefix at read time."
          }
        ],
        "records": [
          "runtime.md#rt-rte-skill-admission",
          "memory.md#mem-obj-code",
          "memory.md#mem-obj-docstring",
          "memory.md#mem-obj-metadata",
          "epistemic.md#epi-rte-tested-label",
          "runtime.md#rt-rte-explore-practice",
          "memory.md#mem-obj-traces",
          "epistemic.md#epi-rte-score-retention",
          "memory.md#mem-rte-embedding-selection",
          "runtime.md#rt-cmp-embed",
          "memory.md#mem-obj-semantic-knowledge"
        ],
        "note": "Automatic builder admissions and artifact capture are supported. Loading or invoking a generic public method does not establish a human per-content decision."
      },
      "curation_operations": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Same-name replacement of retained code and documentation",
            "assessment": "known",
            "findings": [
              {
                "value": "evolve",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-code",
                  "memory.md#mem-obj-docstring",
                  "epistemic.md#epi-rte-skill-merge"
                ],
                "note": "Replacement changes an existing retained function/docstring and resets its tested status."
              }
            ],
            "records": [
              "memory.md#mem-obj-code",
              "memory.md#mem-obj-docstring",
              "epistemic.md#epi-rte-skill-merge"
            ],
            "note": "Existing entries are revised by name; omitted entries remain. This establishes evolution independently of semantic novelty."
          },
          {
            "scope": "Raw episode to retained selected textual episode",
            "assessment": "known",
            "findings": [
              {
                "value": "consolidate",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-traces",
                  "epistemic.md#epi-rte-trajectory-format"
                ],
                "note": "The formatter reduces raw experience to initial observation and selected action/result fields, even though raw artifacts remain."
              }
            ],
            "records": [
              "memory.md#mem-obj-traces",
              "epistemic.md#epi-rte-trajectory-format"
            ],
            "note": "Selection reduces existing observations/actions without establishing novel propositions."
          },
          {
            "scope": "Semantic content of model-generated generalization and documentation revisions",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "runtime.md#rt-rte-skill-admission",
              "epistemic.md#epi-rte-skill-merge",
              "memory.md#mem-obj-docstring"
            ],
            "note": "Generalization is requested, but arbitrary candidate/input semantics do not establish consolidation versus synthesis on that content edge. No dedup, decay, promotion or durable invalidation is inferred from names, test resets or transient disabled names."
          }
        ],
        "records": [
          "memory.md#mem-obj-code",
          "memory.md#mem-obj-docstring",
          "epistemic.md#epi-rte-skill-merge",
          "memory.md#mem-obj-traces",
          "epistemic.md#epi-rte-trajectory-format",
          "runtime.md#rt-rte-skill-admission"
        ],
        "note": "Same-name evolution and selective episode consolidation are implemented. Novel-claim synthesis, requested usage documentation and blanket-marking control are not upgraded from intent or unresolved semantics."
      },
      "read_back_direction": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Native tasks, later builder iterations and Browser-Use adapter library reads",
            "assessment": "known",
            "findings": [
              {
                "value": "pull",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-rte-native-task",
                  "runtime.md#rt-rte-explore-practice",
                  "runtime.md#rt-rte-skill-admission",
                  "runtime.md#rt-rte-browser-use"
                ],
                "note": "Task/update/practice callers request retained library material for their current operation."
              }
            ],
            "records": [
              "runtime.md#rt-rte-native-task",
              "runtime.md#rt-rte-explore-practice",
              "runtime.md#rt-rte-skill-admission",
              "runtime.md#rt-rte-browser-use"
            ],
            "note": "Requests precede selection and delivery; assembly of requested library context is not an independent push."
          },
          {
            "scope": "Benchmark score aggregation and later prefix reload",
            "assessment": "known",
            "findings": [
              {
                "value": "pull",
                "basis": "afforded",
                "records": [
                  "epistemic.md#epi-rte-score-retention",
                  "runtime.md#rt-rte-benchmark-evaluation"
                ],
                "note": "Reporting and evaluation callers request retained results/library prefixes."
              }
            ],
            "records": [
              "epistemic.md#epi-rte-score-retention",
              "runtime.md#rt-rte-benchmark-evaluation"
            ],
            "note": "Local score-read/reload code exists; enclosing benchmark remains afforded because of entry defects."
          },
          {
            "scope": "Optional embedding selection, schema exports and artifact reconstruction capabilities",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-rte-embedding-selection",
              "memory.md#mem-obj-docstring",
              "memory.md#mem-obj-traces"
            ],
            "note": "Records establish request/return capabilities but no shipped later consumer invocation. That missing route prevents classification as pull or push; capability shape alone does not establish read-back."
          }
        ],
        "records": [
          "runtime.md#rt-rte-native-task",
          "runtime.md#rt-rte-explore-practice",
          "runtime.md#rt-rte-skill-admission",
          "runtime.md#rt-rte-browser-use",
          "epistemic.md#epi-rte-score-retention",
          "runtime.md#rt-rte-benchmark-evaluation",
          "memory.md#mem-rte-embedding-selection",
          "memory.md#mem-obj-docstring",
          "memory.md#mem-obj-traces"
        ],
        "note": "Established native, builder, adapter and benchmark consumer chains support pull. Optional selection/export/reconstruction capabilities lack a recorded later consumer invocation, leaving included direction coverage unresolved. External host retention is excluded, not classified."
      },
      "read_back_signal": {
        "assessment": "not-determinable",
        "units": [
          {
            "scope": "Established native, builder, adapter and benchmark library/context/result consumer chains",
            "assessment": "inapplicable",
            "findings": [],
            "records": [
              "runtime.md#rt-rte-native-task",
              "runtime.md#rt-rte-explore-practice",
              "runtime.md#rt-rte-skill-admission",
              "runtime.md#rt-rte-browser-use",
              "epistemic.md#epi-rte-score-retention",
              "runtime.md#rt-rte-benchmark-evaluation"
            ],
            "note": "These established consumer chains are request-directed, so push-signal classification is locally inapplicable. Relevance judgment and name matching within a request do not establish push."
          },
          {
            "scope": "Optional embedding selection, schema exports and artifact reconstruction capabilities",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-rte-embedding-selection",
              "memory.md#mem-obj-docstring",
              "memory.md#mem-obj-traces"
            ],
            "note": "No later consumer route is established. Its direction and any push trigger, selector input or selected retained part are unresolved, preventing either a signal value or inapplicability."
          }
        ],
        "records": [
          "runtime.md#rt-rte-native-task",
          "runtime.md#rt-rte-explore-practice",
          "runtime.md#rt-rte-skill-admission",
          "runtime.md#rt-rte-browser-use",
          "epistemic.md#epi-rte-score-retention",
          "memory.md#mem-rte-embedding-selection",
          "memory.md#mem-obj-docstring",
          "memory.md#mem-obj-traces"
        ],
        "note": "Established pull units have locally inapplicable push signals. Included capability-only alternatives lack later-consumer routes, so direction coverage is incomplete and axis-wide signal inapplicability is not established. No controlled signal value is supported for the unresolved alternatives."
      },
      "trace_learning": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Selected browser episode to synthesized skills/documentation to later native/controller consumers",
            "assessment": "known",
            "findings": [
              {
                "value": "yes",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-traces",
                  "runtime.md#rt-rte-skill-admission",
                  "memory.md#mem-obj-code",
                  "memory.md#mem-obj-docstring",
                  "runtime.md#rt-bap-library-execution"
                ],
                "note": "Automatic trace-fed synthesis installs procedures and guidance consumed in later tasks."
              }
            ],
            "records": [
              "memory.md#mem-obj-traces",
              "runtime.md#rt-rte-skill-admission",
              "memory.md#mem-obj-code",
              "memory.md#mem-obj-docstring",
              "runtime.md#rt-bap-library-execution"
            ],
            "note": "The durable behavior-shaping chain is wired; actual exercise and improvement are not observed."
          },
          {
            "scope": "Last-action result predicate to persistent test metadata to practice/visibility consumers",
            "assessment": "known",
            "findings": [
              {
                "value": "yes",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-metadata",
                  "epistemic.md#epi-rte-test-check",
                  "epistemic.md#epi-rte-tested-label"
                ],
                "note": "Recorded action source/results automatically change counters that affect later behavior."
              }
            ],
            "records": [
              "memory.md#mem-obj-metadata",
              "epistemic.md#epi-rte-test-check",
              "epistemic.md#epi-rte-tested-label"
            ],
            "note": "Qualifies as durable selection-policy adaptation, not evidence that the named skill executed."
          },
          {
            "scope": "Imported initial content and externally invoked blanket marking/replacement",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-code",
              "memory.md#mem-obj-docstring",
              "memory.md#mem-obj-metadata",
              "memory.md#mem-obj-semantic-knowledge",
              "epistemic.md#epi-rte-tested-label"
            ],
            "note": "Missing origin and admission control prevent deciding whether these alternative writes are automatic trace-fed learning routes."
          }
        ],
        "records": [
          "memory.md#mem-obj-traces",
          "runtime.md#rt-rte-skill-admission",
          "memory.md#mem-obj-code",
          "memory.md#mem-obj-docstring",
          "runtime.md#rt-bap-library-execution",
          "memory.md#mem-obj-metadata",
          "epistemic.md#epi-rte-test-check",
          "epistemic.md#epi-rte-tested-label",
          "memory.md#mem-obj-semantic-knowledge"
        ],
        "note": "The automatic episode-to-skill route qualifies architecturally without observed benefit. Automatic trace-conditioned metadata also shapes later selection. Arbitrary initial content and unknown external caller mutations do not inherit these findings."
      },
      "trace_source": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Procedural synthesis from selected browser experience",
            "assessment": "known",
            "findings": [
              {
                "value": "trajectories",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-traces",
                  "runtime.md#rt-rte-skill-admission",
                  "epistemic.md#epi-rte-trajectory-format"
                ],
                "note": "Linked browser states, actions and results supply multi-step experience."
              },
              {
                "value": "tool-traces",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-traces",
                  "runtime.md#rt-rte-skill-admission"
                ],
                "note": "Generated Python requests, outputs, warnings and exceptions are execution-feedback inputs."
              }
            ],
            "records": [
              "memory.md#mem-obj-traces",
              "runtime.md#rt-rte-skill-admission",
              "epistemic.md#epi-rte-trajectory-format"
            ],
            "note": "The actual formatted input includes initial state and action sequence with execution feedback; omitted later observations/recovery remain limits on evidence completeness."
          },
          {
            "scope": "Automatic tested-counter update",
            "assessment": "known",
            "findings": [
              {
                "value": "tool-traces",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-metadata",
                  "epistemic.md#epi-rte-test-check",
                  "epistemic.md#epi-rte-tested-label"
                ],
                "note": "Recorded action source and exception/recovery fields feed the persistent counter update."
              }
            ],
            "records": [
              "memory.md#mem-obj-metadata",
              "epistemic.md#epi-rte-test-check",
              "epistemic.md#epi-rte-tested-label"
            ],
            "note": "The predicate consumes last-action code and result fields, not the whole multi-step episode."
          },
          {
            "scope": "Unknown initial library/documentation/semantic provenance and external mutation origins",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-code",
              "memory.md#mem-obj-docstring",
              "memory.md#mem-obj-metadata",
              "memory.md#mem-obj-semantic-knowledge",
              "epistemic.md#epi-rte-tested-label"
            ],
            "note": "No original trace input or qualifying automatic write is established for these included alternatives."
          }
        ],
        "records": [
          "memory.md#mem-obj-traces",
          "runtime.md#rt-rte-skill-admission",
          "epistemic.md#epi-rte-trajectory-format",
          "memory.md#mem-obj-metadata",
          "epistemic.md#epi-rte-test-check",
          "epistemic.md#epi-rte-tested-label",
          "memory.md#mem-obj-code",
          "memory.md#mem-obj-docstring",
          "memory.md#mem-obj-semantic-knowledge"
        ],
        "note": "Sources are local to qualifying automatic writes; unknown initial provenance is retained rather than made inapplicable. Model responses are not automatically conversational session logs."
      }
    }
  }
}
---

# SkillWeaver memory profile

## Comparison rationale

This profile classifies accepted records, not source files or observed runs. The library is executable Python plus a separate readable documentation channel. Checkpoint files do not make the store a repository or vector database; dense vectors in the optional process cache supply parametric access representations, not updated provider weights ([MEM-OBJ-code](memory.md#mem-obj-code), [MEM-OBJ-docstring](memory.md#mem-obj-docstring), [MEM-RTE-embedding-selection](memory.md#mem-rte-embedding-selection)).

Reconciliation supersedes the epistemic skill-code, skill-docstring, function-metadata and semantic-knowledge object declarations with their memory counterparts. All object citations here use those canonical memory declarations. The selected episode and success/benchmark results remain distinct parts of the larger trace/diagnostic inventory; their local routes retain their own evidence strength. In particular, local score retention wiring does not upgrade the defective enclosing benchmark invocation ([MEM-OBJ-traces](memory.md#mem-obj-traces), [EPI-RTE-score-retention](epistemic.md#epi-rte-score-retention), [RT-RTE-benchmark-evaluation](runtime.md#rt-rte-benchmark-evaluation)).

The trace-learning positives concern durable behavior-shaping writes, not demonstrated improvement. Synthesis learns into code/documentation; the test shortcut instead changes persistent selection metadata. A syntactic call in a dead branch can pass that shortcut without executing the function. Later policy force remains real despite this evidential weakness ([RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission), [EPI-RTE-test-check](epistemic.md#epi-rte-test-check), [EPI-RTE-tested-label](epistemic.md#epi-rte-tested-label)). Original browser experience supports trajectories and tool traces, not a further event-stream or session-log value merely because metadata stores events or models generated reasoning.

Existing source and experience have learning authority at synthesis; readable descriptions have knowledge and ranking authority at task consumers. Direct executable effects do not by themselves prove one of the controlled authority values, so that consumer remains locally not determinable rather than receiving an invented execution value. Stored reasons are not automatically future guidance: synthesis diagnostics are not reloaded, while documentation may preserve reasons only if the model actually writes them ([MEM-OBJ-code](memory.md#mem-obj-code), [MEM-OBJ-docstring](memory.md#mem-obj-docstring), [MEM-OBJ-traces](memory.md#mem-obj-traces)).

Same-name replacement establishes evolution. Selective serialization establishes consolidation even with raw files retained. Prompted generalization does not establish a novel claim; the generated content relation is indeterminate without candidate/input instances. These limits prevent a synthesis finding without suppressing known evolution ([EPI-RTE-trajectory-format](epistemic.md#epi-rte-trajectory-format), [EPI-RTE-skill-merge](epistemic.md#epi-rte-skill-merge)).

The supported read-back findings are pull for established native, builder, adapter and benchmark consumer chains; direction coverage remains partial. Model relevance selection within a consumer request is not independent push, and a function name or checkpoint prefix is not a push signal. Optional embedding selection, schema exports and artifact reconstruction establish capabilities without a recorded later consumer invocation. Their request/return shape therefore establishes neither pull nor push. Push signals are locally inapplicable for the established pull chains, but the unresolved alternatives prevent axis-wide inapplicability; the signal axis is not determinable. External host memory handling remains excluded explicitly, not resolved by the native route ([RT-RTE-native-task](runtime.md#rt-rte-native-task), [RT-RTE-explore-practice](runtime.md#rt-rte-explore-practice), [RT-RTE-browser-use](runtime.md#rt-rte-browser-use), [RT-RTE-benchmark-evaluation](runtime.md#rt-rte-benchmark-evaluation), [MEM-RTE-embedding-selection](memory.md#mem-rte-embedding-selection), [MEM-OBJ-docstring](memory.md#mem-obj-docstring), [MEM-OBJ-traces](memory.md#mem-obj-traces)).

Unknown initial content provenance and caller control prevent complete lineage, write-agency and trace-route coverage. No manual admission is inferred from starting a workflow or choosing a file. Images and arbitrary semantic payloads prevent a complete form classification. No absence of learning is inferred from an unchanged semantic field, and no observed operation or causal benefit is inferred from wiring ([MEM-OBJ-semantic-knowledge](memory.md#mem-obj-semantic-knowledge), [MEM-OBJ-metadata](memory.md#mem-obj-metadata), [MEM-OBJ-traces](memory.md#mem-obj-traces)).

Source-read log: none. No frozen-source ambiguity required a direct source read; all warrants remain in the supplied accepted records.
