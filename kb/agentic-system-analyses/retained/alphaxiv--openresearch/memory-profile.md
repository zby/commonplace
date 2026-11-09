---
{
  "type": "agentic-system-analyses/types/agentic-system-memory-profile.md",
  "description": "OpenResearch memory profile: retained research/session state, continuation summaries, reusable instructions and later-consumer routes, with opaque native and untraced lifecycle alternatives.",
  "run-id": "AAS-2026-10-20-openresearch-62725ad1cd0a-01",
  "source-identity": "https://github.com/alphaXiv/OpenResearch",
  "reviewed-boundary": "2c45ff3183b494aac4001bd44eefbe57a3c249ae",
  "memory-comparison": {
    "version": 2,
    "scope": "ORX retained transcript and session/goal/bootstrap state; provider-native session/checkpoint references and opaque retained payloads; experiment descriptions, organization, branches, run metadata/source archives/logs; project artifacts and uploaded/discovered reusable skills; their admission, maintenance and later-consumer routes. Includes unresolved demo/legacy seed, literature-cache, remote-log and platform lifecycle alternatives retained by the accepted inventory. Excludes static shipped instructions as such, ordinary non-retained turn state, external inference weights without an established memory update route, and release binaries/update caches as production machinery rather than accumulated research/session memory. Dynamic project-orientation facts are included separately from static playbook instructions.",
    "axes": {
      "storage_substrate": {
        "assessment": "partial",
        "units": [
          {
            "scope": "ORX transcript, session/bootstrap/goal, experiment/description and run metadata",
            "assessment": "known",
            "findings": [
              {
                "value": "sqlite",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-chat-messages",
                  "memory.md#mem-obj-bootstrap-context",
                  "memory.md#mem-obj-session-goal",
                  "memory.md#mem-obj-experiment-tree",
                  "epistemic.md#epi-obj-experiment-description",
                  "runtime.md#rt-rte-experiment-run"
                ],
                "note": "Persisted rows, not native model state."
              }
            ],
            "records": [
              "memory.md#mem-obj-chat-messages",
              "memory.md#mem-obj-bootstrap-context",
              "memory.md#mem-obj-session-goal",
              "memory.md#mem-obj-experiment-tree",
              "epistemic.md#epi-obj-experiment-description",
              "runtime.md#rt-rte-experiment-run"
            ],
            "note": "These recorded parts use the ORX SQLite Store."
          },
          {
            "scope": "Retained run logs, artifact files, uploaded skill folders and run source archives",
            "assessment": "known",
            "findings": [
              {
                "value": "files",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-run-log",
                  "memory.md#mem-obj-project-artifacts",
                  "runtime.md#rt-rte-skill-upload",
                  "runtime.md#rt-obj-source-snapshot"
                ],
                "note": "Plain logs/artifacts, managed skill folders and content-addressed archives."
              }
            ],
            "records": [
              "memory.md#mem-obj-run-log",
              "memory.md#mem-obj-project-artifacts",
              "runtime.md#rt-rte-skill-upload",
              "runtime.md#rt-obj-source-snapshot"
            ],
            "note": "These parts have concrete filesystem persistence."
          },
          {
            "scope": "Experiment branches and committed research code",
            "assessment": "known",
            "findings": [
              {
                "value": "repo",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-experiment-tree",
                  "runtime.md#rt-obj-source-snapshot"
                ],
                "note": "Repository commits/branches retain executable research variants."
              }
            ],
            "records": [
              "memory.md#mem-obj-experiment-tree",
              "runtime.md#rt-obj-source-snapshot"
            ],
            "note": "Git branch/code persistence is distinct from the SQLite organization rows."
          },
          {
            "scope": "Provider-native session stores",
            "assessment": "partial",
            "findings": [
              {
                "value": "files",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-native-session"
                ],
                "note": "Claude isolated native state has a filesystem root."
              },
              {
                "value": "sqlite",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-native-session"
                ],
                "note": "OpenCode isolated native state is located at opencode.db."
              }
            ],
            "records": [
              "memory.md#mem-obj-native-session"
            ],
            "note": "Known store roots do not enumerate every provider payload or database format."
          },
          {
            "scope": "Literature-cache, demo/legacy seed initialization, remote-log and platform persistence alternatives",
            "assessment": "uninspected",
            "findings": [],
            "records": [
              "memory.md#mem-obj-bootstrap-context",
              "memory.md#mem-obj-run-log",
              "memory.md#mem-obj-project-artifacts",
              "runtime.md#rt-rte-skill-upload"
            ],
            "note": "Accepted inventory leaves these included lifecycle surfaces untraced; no complete storage union is established."
          }
        ],
        "records": [
          "memory.md#mem-obj-chat-messages",
          "memory.md#mem-obj-bootstrap-context",
          "memory.md#mem-obj-session-goal",
          "memory.md#mem-obj-experiment-tree",
          "epistemic.md#epi-obj-experiment-description",
          "runtime.md#rt-rte-experiment-run",
          "memory.md#mem-obj-run-log",
          "memory.md#mem-obj-project-artifacts",
          "runtime.md#rt-rte-skill-upload",
          "runtime.md#rt-obj-source-snapshot",
          "memory.md#mem-obj-native-session"
        ],
        "note": "Known local SQLite, filesystem and repository witnesses coexist with incomplete native and other included persistence coverage. External inference weights and the release executable are not classified as accumulated memory merely because they are stored."
      },
      "representational_form": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Bootstrap prose, goal, description, report prose, retained skill instruction bodies and readable transcript text",
            "assessment": "known",
            "findings": [
              {
                "value": "natural-language",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-bootstrap-context",
                  "memory.md#mem-obj-session-goal",
                  "epistemic.md#epi-obj-experiment-description",
                  "memory.md#mem-obj-project-artifacts",
                  "runtime.md#rt-rte-skill-upload",
                  "memory.md#mem-obj-chat-messages",
                  "memory.md#mem-rte-turn-context"
                ],
                "note": "Models/humans interpret prior context, instructions and evidence text."
              }
            ],
            "records": [
              "memory.md#mem-obj-bootstrap-context",
              "memory.md#mem-obj-session-goal",
              "epistemic.md#epi-obj-experiment-description",
              "memory.md#mem-obj-project-artifacts",
              "runtime.md#rt-rte-skill-upload",
              "memory.md#mem-obj-chat-messages",
              "memory.md#mem-rte-turn-context"
            ],
            "note": "Only the named textual parts and their interpreted consumption paths are classified."
          },
          {
            "scope": "Session/branch/run selectors, tree organization, source-selection metadata and parsed chart data",
            "assessment": "known",
            "findings": [
              {
                "value": "symbolic",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-chat-messages",
                  "memory.md#mem-obj-experiment-tree",
                  "runtime.md#rt-obj-source-snapshot",
                  "runtime.md#rt-rte-run-wakeup",
                  "epistemic.md#epi-rte-chart-render"
                ],
                "note": "These localized units have program-defined selection, organization and rendering rules."
              }
            ],
            "records": [
              "memory.md#mem-obj-chat-messages",
              "memory.md#mem-obj-experiment-tree",
              "runtime.md#rt-obj-source-snapshot",
              "runtime.md#rt-rte-run-wakeup",
              "epistemic.md#epi-rte-chart-render"
            ],
            "note": "Fixed consumers act on IDs, flags, archive metadata and numerical/chart fields."
          },
          {
            "scope": "Arbitrary tool bodies, binary artifacts and native context payloads",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-chat-messages",
              "memory.md#mem-obj-project-artifacts",
              "memory.md#mem-obj-native-session"
            ],
            "note": "Display text and file names do not determine consumed binary/native payload form; no parametric classification is inferred from a models folder."
          },
          {
            "scope": "Additional untraced seed and native-discovered support content",
            "assessment": "uninspected",
            "findings": [],
            "records": [
              "memory.md#mem-obj-bootstrap-context",
              "runtime.md#rt-rte-skill-upload"
            ],
            "note": "The accepted records do not classify all seed/support-file contents or their actual native consumers."
          }
        ],
        "records": [
          "memory.md#mem-obj-bootstrap-context",
          "memory.md#mem-obj-session-goal",
          "epistemic.md#epi-obj-experiment-description",
          "memory.md#mem-obj-project-artifacts",
          "runtime.md#rt-rte-skill-upload",
          "memory.md#mem-obj-chat-messages",
          "memory.md#mem-rte-turn-context",
          "memory.md#mem-obj-experiment-tree",
          "runtime.md#rt-obj-source-snapshot",
          "runtime.md#rt-rte-run-wakeup",
          "epistemic.md#epi-rte-chart-render",
          "memory.md#mem-obj-native-session"
        ],
        "note": "Textual and symbolic parts are split by consumption; opaque native/binary content prevents complete form coverage. Inference components are outside this accumulated-memory inventory, not evidence for parametric retained updates."
      },
      "lineage": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Explicitly supplied goals, free-form experiment notes and authored report/code portions",
            "assessment": "known",
            "findings": [
              {
                "value": "authored",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-session-goal",
                  "epistemic.md#epi-obj-experiment-description",
                  "memory.md#mem-obj-project-artifacts",
                  "memory.md#mem-obj-experiment-tree"
                ],
                "note": "Caller/agent/user supplies guidance, descriptions, research files and branch changes."
              }
            ],
            "records": [
              "memory.md#mem-obj-session-goal",
              "epistemic.md#epi-obj-experiment-description",
              "memory.md#mem-obj-project-artifacts",
              "memory.md#mem-obj-experiment-tree"
            ],
            "note": "This unit covers the named authored portions, not every artifact producer."
          },
          {
            "scope": "Fallback compaction summary from recorded session work",
            "assessment": "known",
            "findings": [
              {
                "value": "trace-extracted",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-chat-compaction",
                  "memory.md#mem-obj-bootstrap-context",
                  "memory.md#mem-obj-chat-messages"
                ],
                "note": "Flattened messages and prior seed feed a model-produced continuation summary."
              }
            ],
            "records": [
              "memory.md#mem-rte-chat-compaction",
              "memory.md#mem-obj-bootstrap-context",
              "memory.md#mem-obj-chat-messages"
            ],
            "note": "The transformation and retained summary have an explicit raw-to-derived chain."
          },
          {
            "scope": "Source archives and project-orientation counts derived from retained project state",
            "assessment": "known",
            "findings": [
              {
                "value": "other-compiled",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-obj-source-snapshot",
                  "runtime.md#rt-obj-playbook",
                  "memory.md#mem-obj-experiment-tree"
                ],
                "note": "Archives package selected committed code; orientation renders stored counts/command presence."
              }
            ],
            "records": [
              "runtime.md#rt-obj-source-snapshot",
              "runtime.md#rt-obj-playbook",
              "memory.md#mem-obj-experiment-tree"
            ],
            "note": "These deterministic derivations do not establish a new scientific claim."
          },
          {
            "scope": "Uploaded reusable skill content entering managed distribution",
            "assessment": "known",
            "findings": [
              {
                "value": "imported",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-rte-skill-upload"
                ],
                "note": "Uploaded UTF-8 skill/archive content is copied into later native skill directories."
              }
            ],
            "records": [
              "runtime.md#rt-rte-skill-upload"
            ],
            "note": "Classification concerns entry from uploaded source into managed copies, not original author provenance."
          },
          {
            "scope": "Native session origin, initial/legacy/demo bootstrap, arbitrary artifact provenance and discovered skills",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-native-session",
              "memory.md#mem-obj-bootstrap-context",
              "memory.md#mem-obj-project-artifacts",
              "runtime.md#rt-rte-skill-upload"
            ],
            "note": "Some later native-turn/compaction lineage is recorded, but initial/imported provenance and opaque checkpoint production are unresolved."
          },
          {
            "scope": "Raw transcript/log capture derivation and untraced literature/remote lifecycle alternatives",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-chat-messages",
              "memory.md#mem-obj-run-log"
            ],
            "note": "Records identify user/harness/program origins and capture, but do not establish a single derivation classification for every raw or externally supplied part."
          }
        ],
        "records": [
          "memory.md#mem-obj-session-goal",
          "epistemic.md#epi-obj-experiment-description",
          "memory.md#mem-obj-project-artifacts",
          "memory.md#mem-obj-experiment-tree",
          "memory.md#mem-rte-chat-compaction",
          "memory.md#mem-obj-bootstrap-context",
          "memory.md#mem-obj-chat-messages",
          "runtime.md#rt-obj-source-snapshot",
          "runtime.md#rt-obj-playbook",
          "runtime.md#rt-rte-skill-upload",
          "memory.md#mem-obj-native-session",
          "memory.md#mem-obj-run-log"
        ],
        "note": "Supported authored, imported, compiled and trace-derived paths remain local; original provenance and native payload derivation cannot be inferred from known fallback lineage."
      },
      "behavioral_authority": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Continuation summary and selected transcript/log/report/description evidence at later model or human readers",
            "assessment": "known",
            "findings": [
              {
                "value": "knowledge",
                "basis": "wired",
                "records": [
                  "memory.md#mem-bap-bootstrap-injection",
                  "memory.md#mem-obj-chat-messages",
                  "memory.md#mem-rte-log-retrieval",
                  "memory.md#mem-obj-project-artifacts",
                  "epistemic.md#epi-rte-description-store",
                  "memory.md#mem-rte-turn-context"
                ],
                "note": "Later consumers receive context, evidence and notes through prepared text, CLI or requested file access."
              }
            ],
            "records": [
              "memory.md#mem-bap-bootstrap-injection",
              "memory.md#mem-obj-chat-messages",
              "memory.md#mem-rte-log-retrieval",
              "memory.md#mem-obj-project-artifacts",
              "epistemic.md#epi-rte-description-store",
              "memory.md#mem-rte-turn-context"
            ],
            "note": "Prior context and evidence support interpretation, not hard permission controls."
          },
          {
            "scope": "Persisted goal and slash-selected reusable skill instructions at ordinary native turn composition",
            "assessment": "known",
            "findings": [
              {
                "value": "instruction",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-session-goal",
                  "memory.md#mem-rte-turn-context",
                  "runtime.md#rt-rte-skill-upload"
                ],
                "note": "Goal wrapper and selected skill bodies tell the model what to do."
              }
            ],
            "records": [
              "memory.md#mem-obj-session-goal",
              "memory.md#mem-rte-turn-context",
              "runtime.md#rt-rte-skill-upload"
            ],
            "note": "This unit concerns delivered standing directions; native discretionary loading is a separate uncertainty."
          },
          {
            "scope": "Raw session records and previous bootstrap at the fallback-summary update consumer",
            "assessment": "known",
            "findings": [
              {
                "value": "learning",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-chat-compaction",
                  "memory.md#mem-obj-chat-messages",
                  "memory.md#mem-obj-bootstrap-context"
                ],
                "note": "Recorded experience feeds an update to a continuation artifact later consumed as context."
              }
            ],
            "records": [
              "memory.md#mem-rte-chat-compaction",
              "memory.md#mem-obj-chat-messages",
              "memory.md#mem-obj-bootstrap-context"
            ],
            "note": "Automatic summary production creates retained behavior-shaping context, without demonstrating improved capacity."
          },
          {
            "scope": "Retained session/native IDs, parent leaves, branch source and run subscriptions at code selectors",
            "assessment": "known",
            "findings": [
              {
                "value": "routing",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-native-session",
                  "memory.md#mem-rte-branch-context",
                  "memory.md#mem-rte-turn-context",
                  "runtime.md#rt-obj-source-snapshot",
                  "runtime.md#rt-rte-run-wakeup"
                ],
                "note": "Metadata chooses resume/reseed, ancestry, executable source and the session/run receiving wake-up."
              }
            ],
            "records": [
              "memory.md#mem-obj-native-session",
              "memory.md#mem-rte-branch-context",
              "memory.md#mem-rte-turn-context",
              "runtime.md#rt-obj-source-snapshot",
              "runtime.md#rt-rte-run-wakeup"
            ],
            "note": "Access/continuation metadata has a different consumer from semantic content."
          },
          {
            "scope": "Experiment archive/parent metadata at later tree/navigation consumers",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-experiment-tree",
              "epistemic.md#epi-rte-tree-organize"
            ],
            "note": "The records establish hiding/restoration and changed comparison context, but no relative-priority consumer or effect. These facts alone establish neither ranking nor another controlled authority value for this unit; the ledger's ranking-visibility wording does not supply the missing mechanism."
          },
          {
            "scope": "Opaque native payload effects, arbitrary artifact consumers, discovered-skill loading and untraced alternatives",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-native-session",
              "memory.md#mem-obj-project-artifacts",
              "runtime.md#rt-rte-skill-upload"
            ],
            "note": "Native loading and opaque content effects are not determined by ORX display/distribution; broader enforcement, validation or instruction force cannot be inferred."
          }
        ],
        "records": [
          "memory.md#mem-bap-bootstrap-injection",
          "memory.md#mem-obj-chat-messages",
          "memory.md#mem-rte-log-retrieval",
          "memory.md#mem-obj-project-artifacts",
          "epistemic.md#epi-rte-description-store",
          "memory.md#mem-rte-turn-context",
          "memory.md#mem-obj-session-goal",
          "runtime.md#rt-rte-skill-upload",
          "memory.md#mem-rte-chat-compaction",
          "memory.md#mem-obj-bootstrap-context",
          "memory.md#mem-obj-native-session",
          "memory.md#mem-rte-branch-context",
          "runtime.md#rt-obj-source-snapshot",
          "runtime.md#rt-rte-run-wakeup",
          "memory.md#mem-obj-experiment-tree",
          "epistemic.md#epi-rte-tree-organize"
        ],
        "note": "Known knowledge, instruction, learning and routing paths have distinct actual consumers. Archive/parent visibility and comparison effects do not establish ranking. Static shipped result criteria and current renderer validation are not automatically retained-memory validation criteria; provider-native authority remains unresolved."
      },
      "write_agency": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Native-event transcript admission, fallback summary reseed, supervised log capture and managed skill-upload admission",
            "assessment": "known",
            "findings": [
              {
                "value": "automatic",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-chat-messages",
                  "memory.md#mem-rte-chat-compaction",
                  "memory.md#mem-obj-run-log",
                  "runtime.md#rt-rte-skill-upload"
                ],
                "note": "Starting a turn, compact request or upload is not approval of each subsequently produced/admitted content item."
              }
            ],
            "records": [
              "memory.md#mem-obj-chat-messages",
              "memory.md#mem-rte-chat-compaction",
              "memory.md#mem-obj-run-log",
              "runtime.md#rt-rte-skill-upload"
            ],
            "note": "Software/model admits these retained results without mandatory per-content human approval."
          },
          {
            "scope": "Explicit human UI user-message submission",
            "assessment": "known",
            "findings": [
              {
                "value": "manual",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-chat-messages",
                  "runtime.md#rt-rte-chat-turn"
                ],
                "note": "Explicit user decision supplies this retained input message."
              }
            ],
            "records": [
              "memory.md#mem-obj-chat-messages",
              "runtime.md#rt-rte-chat-turn"
            ],
            "note": "The ordinary UI user supplies the message content, separate from subsequent native output."
          },
          {
            "scope": "Goals, description replacement, artifact/file authorship and generic branch/seed callers",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-session-goal",
              "epistemic.md#epi-rte-description-store",
              "memory.md#mem-rte-artifact-access",
              "memory.md#mem-rte-branch-context",
              "memory.md#mem-obj-bootstrap-context"
            ],
            "note": "Human/API/caller identities are mixed or generic. OS persistence and caller ownership do not determine per-content human decision for every admission mechanism."
          },
          {
            "scope": "Native checkpoint admission, discovered-skill initialization and other included lifecycle alternatives",
            "assessment": "uninspected",
            "findings": [],
            "records": [
              "memory.md#mem-obj-native-session",
              "runtime.md#rt-rte-skill-upload",
              "memory.md#mem-obj-bootstrap-context",
              "memory.md#mem-obj-run-log"
            ],
            "note": "Provider-internal admission and untraced initialization/remote paths prevent a complete agency inventory."
          }
        ],
        "records": [
          "memory.md#mem-obj-chat-messages",
          "memory.md#mem-rte-chat-compaction",
          "memory.md#mem-obj-run-log",
          "runtime.md#rt-rte-skill-upload",
          "runtime.md#rt-rte-chat-turn",
          "memory.md#mem-obj-session-goal",
          "epistemic.md#epi-rte-description-store",
          "memory.md#mem-rte-artifact-access",
          "memory.md#mem-rte-branch-context",
          "memory.md#mem-obj-bootstrap-context",
          "memory.md#mem-obj-native-session"
        ],
        "note": "The known automatic mechanisms and explicit human message input do not resolve generic caller or opaque-provider admission control. Authorship, starting a workflow and physical file I/O are kept separate from admission."
      },
      "curation_operations": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Fallback summary reseed over recorded messages and previous bootstrap",
            "assessment": "known",
            "findings": [
              {
                "value": "consolidate",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-chat-compaction",
                  "memory.md#mem-obj-bootstrap-context"
                ],
                "note": "Bounded flattened history plus previous seed becomes reduced continuation prose."
              }
            ],
            "records": [
              "memory.md#mem-rte-chat-compaction",
              "memory.md#mem-obj-bootstrap-context"
            ],
            "note": "Implemented compression of existing work context, without semantic-preservation observation."
          },
          {
            "scope": "Whole-content description and uploaded-skill replacement",
            "assessment": "known",
            "findings": [
              {
                "value": "evolve",
                "basis": "wired",
                "records": [
                  "epistemic.md#epi-rte-description-store",
                  "runtime.md#rt-rte-skill-upload"
                ],
                "note": "A later description set or same-name skill upload replaces existing retained content."
              }
            ],
            "records": [
              "epistemic.md#epi-rte-description-store",
              "runtime.md#rt-rte-skill-upload"
            ],
            "note": "Replacement revises retained entries rather than merely rebuilding an index."
          },
          {
            "scope": "Host session deletion, artifact deletion and removed managed-skill pruning",
            "assessment": "known",
            "findings": [
              {
                "value": "decay",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-chat-messages",
                  "memory.md#mem-rte-artifact-access",
                  "runtime.md#rt-rte-skill-upload"
                ],
                "note": "Deletion/pruning removes retained material from future reads on the inspected surfaces."
              }
            ],
            "records": [
              "memory.md#mem-obj-chat-messages",
              "memory.md#mem-rte-artifact-access",
              "runtime.md#rt-rte-skill-upload"
            ],
            "note": "Forgetting is local to ORX/files/managed distribution; it does not prove erasure from native or exported copies."
          },
          {
            "scope": "Winner becomes next-round parent under experiment-tree instructions",
            "assessment": "known",
            "findings": [
              {
                "value": "promote",
                "basis": "claimed",
                "records": [
                  "epistemic.md#epi-rte-winner-promotion"
                ],
                "note": "Selected winning retained code is raised to the parent for later rounds."
              }
            ],
            "records": [
              "epistemic.md#epi-rte-winner-promotion"
            ],
            "note": "The operation is prescribed rather than a wired automatic scientific selector."
          },
          {
            "scope": "Native compaction, opaque artifacts and other untraced maintenance",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-native-session",
              "memory.md#mem-rte-chat-compaction",
              "memory.md#mem-obj-project-artifacts"
            ],
            "note": "Native summarization is invoked, but the actual retained transformation is opaque; no deduplication, synthesis or invalidation conclusion follows. Archive visibility is not claim withdrawal."
          }
        ],
        "records": [
          "memory.md#mem-rte-chat-compaction",
          "memory.md#mem-obj-bootstrap-context",
          "epistemic.md#epi-rte-description-store",
          "runtime.md#rt-rte-skill-upload",
          "memory.md#mem-obj-chat-messages",
          "memory.md#mem-rte-artifact-access",
          "epistemic.md#epi-rte-winner-promotion",
          "memory.md#mem-obj-native-session",
          "memory.md#mem-obj-project-artifacts"
        ],
        "note": "Consolidation, replacement and local forgetting are wired; winner promotion retains its doctrine-only basis. Native opacity and incomplete maintenance coverage prevent complete enumeration. Log preview is delivery clipping, not a retained consolidation write."
      },
      "read_back_direction": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Requested retained log/file/description access and caller-selected branch continuation",
            "assessment": "known",
            "findings": [
              {
                "value": "pull",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-log-retrieval",
                  "memory.md#mem-rte-artifact-access",
                  "epistemic.md#epi-rte-description-store",
                  "memory.md#mem-rte-branch-context"
                ],
                "note": "Run/file/experiment identity and branch selection fulfill explicit access requests."
              }
            ],
            "records": [
              "memory.md#mem-rte-log-retrieval",
              "memory.md#mem-rte-artifact-access",
              "epistemic.md#epi-rte-description-store",
              "memory.md#mem-rte-branch-context"
            ],
            "note": "Consumer/caller requests the retained material or continuation."
          },
          {
            "scope": "Ordinary turn automatic prior-context, goal, shell-history and dynamic project orientation supply",
            "assessment": "known",
            "findings": [
              {
                "value": "push",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-turn-context",
                  "memory.md#mem-obj-session-goal",
                  "memory.md#mem-bap-bootstrap-injection",
                  "runtime.md#rt-obj-playbook",
                  "runtime.md#rt-rte-chat-turn"
                ],
                "note": "Code gates bootstrap, selects shell ancestry and supplies goal/project orientation; spawn refresh differs from resident reread."
              }
            ],
            "records": [
              "memory.md#mem-rte-turn-context",
              "memory.md#mem-obj-session-goal",
              "memory.md#mem-bap-bootstrap-injection",
              "runtime.md#rt-obj-playbook",
              "runtime.md#rt-rte-chat-turn"
            ],
            "note": "A new ordinary turn triggers retained-context supply without a separate request for those retained parts."
          },
          {
            "scope": "Subscribed run completion delivery",
            "assessment": "known",
            "findings": [
              {
                "value": "push",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-rte-run-wakeup"
                ],
                "note": "Status-only notification is unsolicited at the later invocation, not an automatic full-log retrieval."
              }
            ],
            "records": [
              "runtime.md#rt-rte-run-wakeup"
            ],
            "note": "Prior opt-in sets selection input; later completion starts a hidden turn automatically."
          },
          {
            "scope": "Explicit slash skill selection and managed native file availability",
            "assessment": "partial",
            "findings": [
              {
                "value": "pull",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-turn-context",
                  "runtime.md#rt-rte-skill-upload"
                ],
                "note": "Caller slash tokens request the selected retained skill content."
              }
            ],
            "records": [
              "memory.md#mem-rte-turn-context",
              "runtime.md#rt-rte-skill-upload"
            ],
            "note": "Slash expansion fulfills the selected instruction request; native discovery/loading is not fully traced."
          },
          {
            "scope": "Native resume/internal selection, opaque artifact consumption and untraced read alternatives",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-native-session",
              "memory.md#mem-obj-project-artifacts",
              "memory.md#mem-obj-bootstrap-context"
            ],
            "note": "ORX resume wiring is known, but all native selector/request chains and opaque consumed parts are not established."
          }
        ],
        "records": [
          "memory.md#mem-rte-log-retrieval",
          "memory.md#mem-rte-artifact-access",
          "epistemic.md#epi-rte-description-store",
          "memory.md#mem-rte-branch-context",
          "memory.md#mem-rte-turn-context",
          "memory.md#mem-obj-session-goal",
          "memory.md#mem-bap-bootstrap-injection",
          "runtime.md#rt-obj-playbook",
          "runtime.md#rt-rte-chat-turn",
          "runtime.md#rt-rte-run-wakeup",
          "runtime.md#rt-rte-skill-upload",
          "memory.md#mem-obj-native-session",
          "memory.md#mem-obj-project-artifacts",
          "memory.md#mem-obj-bootstrap-context"
        ],
        "note": "Both pull and push are supported within their own chains. Requested return is not counted as push merely because software delivers it; incomplete native/alternative coverage prevents a complete read-back inventory."
      },
      "read_back_signal": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Bootstrap/goal/project orientation supply at ordinary turn or spawn",
            "assessment": "known",
            "findings": [
              {
                "value": "coarse",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-turn-context",
                  "memory.md#mem-obj-session-goal",
                  "memory.md#mem-bap-bootstrap-injection",
                  "runtime.md#rt-obj-playbook"
                ],
                "note": "Availability and native-session absence select seed/goal/orientation rather than content-relevance matching."
              }
            ],
            "records": [
              "memory.md#mem-rte-turn-context",
              "memory.md#mem-obj-session-goal",
              "memory.md#mem-bap-bootstrap-injection",
              "runtime.md#rt-obj-playbook"
            ],
            "note": "Trigger is ordinary preparation/spawn; presence/native-ID gating and project state select the supplied retained parts."
          },
          {
            "scope": "Composer-shell ancestry selection and branch-selected parent context supplied to later turns",
            "assessment": "known",
            "findings": [
              {
                "value": "identifier",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-turn-context",
                  "memory.md#mem-rte-branch-context"
                ],
                "note": "Parent/message/leaf identity matches select delivered ancestry and shell records; these are not just labels on a requested file."
              }
            ],
            "records": [
              "memory.md#mem-rte-turn-context",
              "memory.md#mem-rte-branch-context"
            ],
            "note": "Ordinary composition/side-session preparation uses current ancestry or fixed parent leaf to select actual retained records."
          },
          {
            "scope": "Run-wake status notification",
            "assessment": "known",
            "findings": [
              {
                "value": "identifier",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-rte-run-wakeup"
                ],
                "note": "Run/session subscription identity targets the retained status supplied to the resumed model."
              },
              {
                "value": "coarse",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-rte-run-wakeup"
                ],
                "note": "Readiness/status and idleness filter delivery separately from identity targeting."
              }
            ],
            "records": [
              "runtime.md#rt-rte-run-wakeup"
            ],
            "note": "Trigger is ready subscribed run plus idle session; subscription/session/run identity chooses delivered status."
          },
          {
            "scope": "Requested log, artifact, description and slash-skill return operations",
            "assessment": "inapplicable",
            "findings": [],
            "records": [
              "memory.md#mem-rte-log-retrieval",
              "memory.md#mem-rte-artifact-access",
              "epistemic.md#epi-rte-description-store",
              "memory.md#mem-rte-turn-context"
            ],
            "note": "These particular operations fulfill explicit requests; their file/run/name identifiers alone do not establish push signals."
          },
          {
            "scope": "Provider-native context selection and other untraced push alternatives",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-native-session",
              "memory.md#mem-rte-chat-compaction",
              "runtime.md#rt-rte-skill-upload",
              "memory.md#mem-obj-bootstrap-context"
            ],
            "note": "Opaque native retained payload selectors, discovered-skill loading and untraced seed paths prevent complete push-signal classification."
          }
        ],
        "records": [
          "memory.md#mem-rte-turn-context",
          "memory.md#mem-obj-session-goal",
          "memory.md#mem-bap-bootstrap-injection",
          "runtime.md#rt-obj-playbook",
          "memory.md#mem-rte-branch-context",
          "runtime.md#rt-rte-run-wakeup",
          "memory.md#mem-rte-log-retrieval",
          "memory.md#mem-rte-artifact-access",
          "epistemic.md#epi-rte-description-store",
          "memory.md#mem-obj-native-session",
          "memory.md#mem-rte-chat-compaction",
          "runtime.md#rt-rte-skill-upload",
          "memory.md#mem-obj-bootstrap-context"
        ],
        "note": "Known push branches use coarse gates and actual identity/ancestry matching. Pull-only operations have local inapplicability, not a system-wide inapplicable signal axis; no lexical or embedding selector is established."
      },
      "trace_learning": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Automatic fallback compaction summary retained as bootstrap and delivered to a later invocation",
            "assessment": "known",
            "findings": [
              {
                "value": "yes",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-chat-compaction",
                  "memory.md#mem-obj-bootstrap-context",
                  "memory.md#mem-obj-chat-messages",
                  "memory.md#mem-bap-bootstrap-injection"
                ],
                "note": "This automatic trace-fed continuation-artifact write qualifies even though compact is user-triggered and improvement is unobserved."
              }
            ],
            "records": [
              "memory.md#mem-rte-chat-compaction",
              "memory.md#mem-obj-bootstrap-context",
              "memory.md#mem-obj-chat-messages",
              "memory.md#mem-bap-bootstrap-injection"
            ],
            "note": "Raw messages/previous seed feed a nonempty model summary, SQLite retention, native-ID clearing and later context delivery."
          },
          {
            "scope": "Persisted branch/ACP and legacy side-chat transcript bootstrap produced for later continuation",
            "assessment": "known",
            "findings": [
              {
                "value": "yes",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-branch-context",
                  "memory.md#mem-obj-bootstrap-context",
                  "memory.md#mem-obj-chat-messages",
                  "memory.md#mem-bap-bootstrap-injection"
                ],
                "note": "Selected recorded activity becomes retained context-shaping seed without per-summary human approval."
              }
            ],
            "records": [
              "memory.md#mem-rte-branch-context",
              "memory.md#mem-obj-bootstrap-context",
              "memory.md#mem-obj-chat-messages",
              "memory.md#mem-bap-bootstrap-injection"
            ],
            "note": "Automatic flattening/reseed retains selected session work for a later native invocation; this is not only raw-log storage."
          },
          {
            "scope": "Native compaction/checkpoint transformations",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-native-session",
              "memory.md#mem-rte-chat-compaction"
            ],
            "note": "Native checkpoint payload and precise transformation are opaque; fallback evidence cannot classify this alternative."
          },
          {
            "scope": "Initial/demo seeds, arbitrary report/skill derivations, remote and other untraced lifecycle routes",
            "assessment": "uninspected",
            "findings": [],
            "records": [
              "memory.md#mem-obj-bootstrap-context",
              "memory.md#mem-obj-project-artifacts",
              "runtime.md#rt-rte-skill-upload",
              "memory.md#mem-obj-run-log"
            ],
            "note": "Detailed trace origin and automatic derived-write/later-consumer chains are not established. Raw log retention alone does not establish learning and no bounded absence record warrants a local no."
          }
        ],
        "records": [
          "memory.md#mem-rte-chat-compaction",
          "memory.md#mem-obj-bootstrap-context",
          "memory.md#mem-obj-chat-messages",
          "memory.md#mem-bap-bootstrap-injection",
          "memory.md#mem-rte-branch-context",
          "memory.md#mem-obj-native-session",
          "memory.md#mem-obj-project-artifacts",
          "runtime.md#rt-rte-skill-upload",
          "memory.md#mem-obj-run-log"
        ],
        "note": "The supported system union includes yes with wired basis, but coverage remains partial. No local or system-wide no is asserted: no accepted evidenced-absence record covers the unresolved alternatives. Trace learning here does not mean observed improvement, parameter training or self-improvement."
      },
      "trace_source": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Session-message input to fallback summary and selected-path bootstrap retention",
            "assessment": "known",
            "findings": [
              {
                "value": "session-logs",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-chat-compaction",
                  "memory.md#mem-obj-chat-messages",
                  "memory.md#mem-rte-branch-context",
                  "memory.md#mem-obj-bootstrap-context"
                ],
                "note": "Flattened retained user/assistant work-session messages feed summary/reseed."
              }
            ],
            "records": [
              "memory.md#mem-rte-chat-compaction",
              "memory.md#mem-obj-chat-messages",
              "memory.md#mem-rte-branch-context",
              "memory.md#mem-obj-bootstrap-context"
            ],
            "note": "Recorded conversational turns supply the inspected qualifying writes."
          },
          {
            "scope": "Recorded tool-label/status, prompt-resolution and shell-execution evidence included in qualifying snapshots",
            "assessment": "known",
            "findings": [
              {
                "value": "tool-traces",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-chat-messages",
                  "memory.md#mem-rte-chat-compaction",
                  "memory.md#mem-rte-branch-context",
                  "memory.md#mem-rte-turn-context"
                ],
                "note": "Flattening retains tool title/status and prompt information; session records can also carry shell feedback."
              }
            ],
            "records": [
              "memory.md#mem-obj-chat-messages",
              "memory.md#mem-rte-chat-compaction",
              "memory.md#mem-rte-branch-context",
              "memory.md#mem-rte-turn-context"
            ],
            "note": "Classification covers included activity evidence, not omitted full tool bodies."
          },
          {
            "scope": "Earlier/demo bootstrap and opaque native checkpoint input mixtures",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-bootstrap-context",
              "memory.md#mem-obj-native-session",
              "memory.md#mem-rte-chat-compaction"
            ],
            "note": "Earlier bootstrap is fed into repeated summaries but its complete original provenance, including demo seed and native inputs, is unresolved."
          },
          {
            "scope": "Potential trace-fed artifacts/skills and untraced remote lifecycle sources",
            "assessment": "uninspected",
            "findings": [],
            "records": [
              "memory.md#mem-obj-project-artifacts",
              "runtime.md#rt-rte-skill-upload",
              "memory.md#mem-obj-run-log"
            ],
            "note": "No complete qualifying update chain/source inventory is recorded for these alternatives. No event-stream or trajectory value is inferred merely from timestamps or linked branch metadata."
          }
        ],
        "records": [
          "memory.md#mem-rte-chat-compaction",
          "memory.md#mem-obj-chat-messages",
          "memory.md#mem-rte-branch-context",
          "memory.md#mem-obj-bootstrap-context",
          "memory.md#mem-rte-turn-context",
          "memory.md#mem-obj-native-session",
          "memory.md#mem-obj-project-artifacts",
          "runtime.md#rt-rte-skill-upload",
          "memory.md#mem-obj-run-log"
        ],
        "note": "Session logs and tool traces are supported original content types on qualifying writes; mixed prior seeds/native input uncertainty prevents complete trace-source coverage. This axis is not inapplicable because qualifying trace learning is wired."
      }
    }
  }
}
---

# OpenResearch memory profile

## Comparison rationale

The comparison covers accumulated research and session material, not every byte the runtime stores. SQLite transcript rows, native session payloads and bootstrap prose are distinct. A readable transcript does not resolve a native checkpoint's form, provenance, selector or update semantics. Known local facts therefore coexist with unresolved alternatives rather than licensing complete axis inventories; see [MEM-OBJ-native-session](memory.md#mem-obj-native-session), [MEM-OBJ-chat-messages](memory.md#mem-obj-chat-messages) and [MEM-OBJ-bootstrap-context](memory.md#mem-obj-bootstrap-context). The accepted inventory also leaves literature-cache, remote and platform lifecycle details untraced. These are coverage limits, not evidenced absences.

Fallback compaction is the strongest recorded trace-learning witness. The automatic chain retains a summary of bounded recorded session work and prior seed, then supplies it to a later invocation. User initiation does not make admission of the generated summary manual. This is consolidation and trace learning under the comparison contract, without observed improvement or reliable preservation of reasons. Selected-path ACP/side bootstrap is another retained continuation representation of recorded activity; ordinary transient recovery text alone is not a separate retained write. See [MEM-RTE-chat-compaction](memory.md#mem-rte-chat-compaction), [MEM-RTE-branch-context](memory.md#mem-rte-branch-context) and [MEM-BAP-bootstrap-injection](memory.md#mem-bap-bootstrap-injection). Earlier seeds and native checkpoints remain separate uncertainty units. Learning authority at the summary-update consumer and knowledge authority at the later model consumer are different paths.

Requested log/file/description returns are pull. Ordinary goal/seed/shell-context supply and subscribed wake-up are push operations within longer chains. Run identity on a requested log is not a push signal. Subscription identity and ancestry matching do select delivered retained parts; availability, readiness and budget gates remain coarse selectors. Slash expansion fulfills a caller-selected instruction request, while native skill discovery/loading stays unresolved. See [MEM-RTE-turn-context](memory.md#mem-rte-turn-context), [MEM-RTE-log-retrieval](memory.md#mem-rte-log-retrieval), [RT-RTE-run-wakeup](runtime.md#rt-rte-run-wakeup) and [RT-RTE-skill-upload](runtime.md#rt-rte-skill-upload).

Deletion/pruning supports only local forgetting; it does not retract exported or already delivered content. Description/skill replacement supports evolution without implying synthesis. Archive flags affect visibility rather than evidential reliance. Visibility and changed comparison context do not establish relative priority, so the archive/parent authority unit emits no controlled finding. The records do not support ranking at that consumer, despite the epistemic ledger's wording. Winner promotion is retained only at its claimed instructional basis, not upgraded by wired branch/run primitives. See [MEM-RTE-artifact-access](memory.md#mem-rte-artifact-access), [EPI-RTE-description-store](epistemic.md#epi-rte-description-store), [EPI-RTE-tree-organize](epistemic.md#epi-rte-tree-organize) and [EPI-RTE-winner-promotion](epistemic.md#epi-rte-winner-promotion). Static renderer validation does not establish that retained memory itself supplies a validation criterion; see [EPI-RTE-chart-render](epistemic.md#epi-rte-chart-render).

Reconciliation resolves the duplicate epistemic run-log and research-output objects to the memory run-log and project-artifact declarations. It also resolves epistemic/workflow log-preview routes to the memory log-retrieval declaration, and epistemic artifact retention to memory artifact access. All profile citations use those canonical declarations. Description, tree organization and chart production remain distinct, as do turn composition and its enclosing turn route. These identity resolutions change no evidence basis.

No source files were read for this profile. All classifications use the supplied accepted records and their retained passages. Wired findings establish implemented routes, not exercised behavior, semantic correctness, model compliance or causal benefit. No bounded absence record supports trace-learning no, nor complete absence of any curation or authority value.
