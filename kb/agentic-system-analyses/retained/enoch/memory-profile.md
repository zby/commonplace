---
{
  "type": "agentic-system-analyses/types/agentic-system-memory-profile.md",
  "description": "Enoch memory comparison: retained facts, private identity, session access and opaque native context, task briefs, trace-derived evolution evidence and maintenance state.",
  "run-id": "AAS-2026-10-13-enoch-a73695a57e3b-01",
  "source-identity": "https://github.com/our-ark/enoch",
  "reviewed-boundary": "0934ad59bd253adfffb8263c65e4bf0f4e2d7a9f",
  "memory-comparison": {
    "version": 2,
    "scope": "Retained use-accumulated facts and metadata; installed private identity and its unresolved initialization; session access mappings and opaque native retained payloads; conversation/action/task journals and retry/publication state; retained task/backlog/cron briefs; evidence signals/checkpoints, candidates, curations, work artifacts and lineage inbox material, with their write, maintenance and later-consumer paths. Includes unresolved provider compaction, ancillary maintenance and deployment-specific plugin/profile state. Excludes static shipped prompts/body identity/skills, inference weights, generic permissions and repository software as storage merely because tasks can change it. Transient completion/diagnostic views are classified through their retained inputs/results and later-consumer routes, not as independent durable stores.",
    "axes": {
      "storage_substrate": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Long-term facts and their access/provenance metadata",
            "assessment": "known",
            "findings": [
              {
                "value": "files",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-long-term"
                ],
                "note": "The recorded operative object is retained in local JSON, JSONL or Markdown files; serialization is not a separate substrate."
              }
            ],
            "records": [
              "memory.md#mem-obj-long-term"
            ],
            "note": "The record identifies the file-backed object and its local persistence."
          },
          {
            "scope": "Installed private personal identity",
            "assessment": "known",
            "findings": [
              {
                "value": "files",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-self"
                ],
                "note": "The recorded operative object is retained in local JSON, JSONL or Markdown files; serialization is not a separate substrate."
              }
            ],
            "records": [
              "memory.md#mem-obj-self"
            ],
            "note": "The record identifies the file-backed object and its local persistence."
          },
          {
            "scope": "Codex and Claude native-session access mappings",
            "assessment": "known",
            "findings": [
              {
                "value": "files",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-codex-sessions"
                ],
                "note": "The recorded operative object is retained in local JSON, JSONL or Markdown files; serialization is not a separate substrate."
              }
            ],
            "records": [
              "memory.md#mem-obj-codex-sessions"
            ],
            "note": "The record identifies the file-backed object and its local persistence."
          },
          {
            "scope": "Conversation turn archives",
            "assessment": "known",
            "findings": [
              {
                "value": "files",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-conversation-logs"
                ],
                "note": "The recorded operative object is retained in local JSON, JSONL or Markdown files; serialization is not a separate substrate."
              }
            ],
            "records": [
              "memory.md#mem-obj-conversation-logs"
            ],
            "note": "The record identifies the file-backed object and its local persistence."
          },
          {
            "scope": "Task lifecycle journal",
            "assessment": "known",
            "findings": [
              {
                "value": "files",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-task-events"
                ],
                "note": "The recorded operative object is retained in local JSON, JSONL or Markdown files; serialization is not a separate substrate."
              }
            ],
            "records": [
              "memory.md#mem-obj-task-events"
            ],
            "note": "The record identifies the file-backed object and its local persistence."
          },
          {
            "scope": "Extracted evidence signals",
            "assessment": "known",
            "findings": [
              {
                "value": "files",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-evidence-signals"
                ],
                "note": "The recorded operative object is retained in local JSON, JSONL or Markdown files; serialization is not a separate substrate."
              }
            ],
            "records": [
              "memory.md#mem-obj-evidence-signals"
            ],
            "note": "The record identifies the file-backed object and its local persistence."
          },
          {
            "scope": "Evidence scan checkpoints",
            "assessment": "known",
            "findings": [
              {
                "value": "files",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-evidence-scans"
                ],
                "note": "The recorded operative object is retained in local JSON, JSONL or Markdown files; serialization is not a separate substrate."
              }
            ],
            "records": [
              "memory.md#mem-obj-evidence-scans"
            ],
            "note": "The record identifies the file-backed object and its local persistence."
          },
          {
            "scope": "Durable evolution candidates",
            "assessment": "known",
            "findings": [
              {
                "value": "files",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-evolve-candidate"
                ],
                "note": "The recorded operative object is retained in local JSON, JSONL or Markdown files; serialization is not a separate substrate."
              }
            ],
            "records": [
              "memory.md#mem-obj-evolve-candidate"
            ],
            "note": "The record identifies the file-backed object and its local persistence."
          },
          {
            "scope": "Semantic curation history",
            "assessment": "known",
            "findings": [
              {
                "value": "files",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-semantic-curation"
                ],
                "note": "The recorded operative object is retained in local JSON, JSONL or Markdown files; serialization is not a separate substrate."
              }
            ],
            "records": [
              "memory.md#mem-obj-semantic-curation"
            ],
            "note": "The record identifies the file-backed object and its local persistence."
          },
          {
            "scope": "Learning-artifact index and Markdown work records",
            "assessment": "known",
            "findings": [
              {
                "value": "files",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-learning-artifact"
                ],
                "note": "The recorded operative object is retained in local JSON, JSONL or Markdown files; serialization is not a separate substrate."
              }
            ],
            "records": [
              "memory.md#mem-obj-learning-artifact"
            ],
            "note": "The record identifies the file-backed object and its local persistence."
          },
          {
            "scope": "Lineage inbox source, assessment and adoption state",
            "assessment": "known",
            "findings": [
              {
                "value": "files",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-lineage-inbox"
                ],
                "note": "The recorded operative object is retained in local JSON, JSONL or Markdown files; serialization is not a separate substrate."
              }
            ],
            "records": [
              "memory.md#mem-obj-lineage-inbox"
            ],
            "note": "The record identifies the file-backed object and its local persistence."
          },
          {
            "scope": "Request-keyed action-recovery journal",
            "assessment": "known",
            "findings": [
              {
                "value": "files",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-obj-conversation-journal"
                ],
                "note": "The recorded operative object is retained in local JSON, JSONL or Markdown files; serialization is not a separate substrate."
              }
            ],
            "records": [
              "runtime.md#rt-obj-conversation-journal"
            ],
            "note": "The record identifies the file-backed object and its local persistence."
          },
          {
            "scope": "Retained task/backlog/cron briefs and retry/publication diagnostics/state",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-task-context",
              "runtime.md#rt-obj-validation-diagnostics",
              "workflow.md#wf-rte-review-handoff"
            ],
            "note": "Retention and later consumers are recorded, but these records do not specify all underlying storage parts; no substrate inferred from workflow terminology."
          },
          {
            "scope": "Provider-native session payload",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-native-context"
            ],
            "note": "External harness/service retention is recorded; its actual storage implementation is opaque. A local ID map does not classify that payload."
          },
          {
            "scope": "Deployment-specific extension/profile memory",
            "assessment": "uninspected",
            "findings": [],
            "records": [
              "runtime.md#rt-rte-extension-loading"
            ],
            "note": "Installed implementations and their retained objects are uninspected."
          }
        ],
        "records": [
          "memory.md#mem-obj-long-term",
          "memory.md#mem-obj-self",
          "memory.md#mem-obj-codex-sessions",
          "memory.md#mem-obj-conversation-logs",
          "memory.md#mem-obj-task-events",
          "memory.md#mem-obj-evidence-signals",
          "memory.md#mem-obj-evidence-scans",
          "memory.md#mem-obj-evolve-candidate",
          "memory.md#mem-obj-semantic-curation",
          "memory.md#mem-obj-learning-artifact",
          "memory.md#mem-obj-lineage-inbox",
          "runtime.md#rt-obj-conversation-journal",
          "memory.md#mem-obj-task-context",
          "runtime.md#rt-obj-validation-diagnostics",
          "workflow.md#wf-rte-review-handoff",
          "memory.md#mem-obj-native-context",
          "runtime.md#rt-rte-extension-loading"
        ],
        "note": "Local file objects are identified individually. External native payloads, scheduled/workflow storage details and plugin objects prevent complete inventory classification. Transient completion payloads are views of journals, not extra retained stores; model weights and static shipped code are excluded."
      },
      "representational_form": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Long-term fact text at startup model",
            "assessment": "known",
            "findings": [
              {
                "value": "natural-language",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-long-term",
                  "epistemic.md#epi-obj-memory-text"
                ],
                "note": "Prose is interpreted as text by the named model or human consumer."
              }
            ],
            "records": [
              "memory.md#mem-obj-long-term",
              "epistemic.md#epi-obj-memory-text"
            ],
            "note": "This classification covers the prose part, not its structured envelope."
          },
          {
            "scope": "Private identity rendered designation, values and care fields",
            "assessment": "known",
            "findings": [
              {
                "value": "natural-language",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-self"
                ],
                "note": "Prose is interpreted as text by the named model or human consumer."
              }
            ],
            "records": [
              "memory.md#mem-obj-self"
            ],
            "note": "This classification covers the prose part, not its structured envelope."
          },
          {
            "scope": "Logged message/reply text at feedback extraction",
            "assessment": "known",
            "findings": [
              {
                "value": "natural-language",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-conversation-logs",
                  "memory.md#mem-rte-evidence-update"
                ],
                "note": "Prose is interpreted as text by the named model or human consumer."
              }
            ],
            "records": [
              "memory.md#mem-obj-conversation-logs",
              "memory.md#mem-rte-evidence-update"
            ],
            "note": "This classification covers the prose part, not its structured envelope."
          },
          {
            "scope": "Task request/result and diagnostic prose at experience/repair consumers",
            "assessment": "known",
            "findings": [
              {
                "value": "natural-language",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-task-events",
                  "runtime.md#rt-obj-validation-diagnostics",
                  "runtime.md#rt-rte-task-work"
                ],
                "note": "Prose is interpreted as text by the named model or human consumer."
              }
            ],
            "records": [
              "memory.md#mem-obj-task-events",
              "runtime.md#rt-obj-validation-diagnostics",
              "runtime.md#rt-rte-task-work"
            ],
            "note": "This classification covers the prose part, not its structured envelope."
          },
          {
            "scope": "Evidence observation and desired-outcome prose at synthesis",
            "assessment": "known",
            "findings": [
              {
                "value": "natural-language",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-evidence-signals"
                ],
                "note": "Prose is interpreted as text by the named model or human consumer."
              }
            ],
            "records": [
              "memory.md#mem-obj-evidence-signals"
            ],
            "note": "This classification covers the prose part, not its structured envelope."
          },
          {
            "scope": "Candidate reasons/change/risk/test prose at curator and worker",
            "assessment": "known",
            "findings": [
              {
                "value": "natural-language",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-evolve-candidate",
                  "memory.md#mem-bap-candidate-guidance"
                ],
                "note": "Prose is interpreted as text by the named model or human consumer."
              }
            ],
            "records": [
              "memory.md#mem-obj-evolve-candidate",
              "memory.md#mem-bap-candidate-guidance"
            ],
            "note": "This classification covers the prose part, not its structured envelope."
          },
          {
            "scope": "Curation recommendation/removal guidance at presentation",
            "assessment": "known",
            "findings": [
              {
                "value": "natural-language",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-semantic-curation"
                ],
                "note": "Prose is interpreted as text by the named model or human consumer."
              }
            ],
            "records": [
              "memory.md#mem-obj-semantic-curation"
            ],
            "note": "This classification covers the prose part, not its structured envelope."
          },
          {
            "scope": "Learning-artifact work summary at declared descendant inspection",
            "assessment": "known",
            "findings": [
              {
                "value": "natural-language",
                "basis": "claimed",
                "records": [
                  "memory.md#mem-obj-learning-artifact"
                ],
                "note": "Prose is interpreted as text by the named model or human consumer."
              }
            ],
            "records": [
              "memory.md#mem-obj-learning-artifact"
            ],
            "note": "This classification covers the prose part, not its structured envelope."
          },
          {
            "scope": "Task brief at later worker invocation",
            "assessment": "known",
            "findings": [
              {
                "value": "natural-language",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-task-context",
                  "memory.md#mem-rte-task-snapshot"
                ],
                "note": "Prose is interpreted as text by the named model or human consumer."
              }
            ],
            "records": [
              "memory.md#mem-obj-task-context",
              "memory.md#mem-rte-task-snapshot"
            ],
            "note": "This classification covers the prose part, not its structured envelope."
          },
          {
            "scope": "Lineage source/assessment prose at adaptation consumer",
            "assessment": "known",
            "findings": [
              {
                "value": "natural-language",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-lineage-inbox",
                  "epistemic.md#epi-obj-lineage-assessment"
                ],
                "note": "Prose is interpreted as text by the named model or human consumer."
              }
            ],
            "records": [
              "memory.md#mem-obj-lineage-inbox",
              "epistemic.md#epi-obj-lineage-assessment"
            ],
            "note": "This classification covers the prose part, not its structured envelope."
          },
          {
            "scope": "Action journal reply/result prose at subsequent feedback",
            "assessment": "known",
            "findings": [
              {
                "value": "natural-language",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-obj-conversation-journal",
                  "runtime.md#rt-rte-chat-actions"
                ],
                "note": "Prose is interpreted as text by the named model or human consumer."
              }
            ],
            "records": [
              "runtime.md#rt-obj-conversation-journal",
              "runtime.md#rt-rte-chat-actions"
            ],
            "note": "This classification covers the prose part, not its structured envelope."
          },
          {
            "scope": "Fact IDs/types/confidence/time at validation and startup ordering",
            "assessment": "known",
            "findings": [
              {
                "value": "symbolic",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-long-term",
                  "epistemic.md#epi-obj-memory-metadata",
                  "memory.md#mem-rte-startup-context"
                ],
                "note": "Localized fields are interpreted under fixed validation, identity, state or selection rules."
              }
            ],
            "records": [
              "memory.md#mem-obj-long-term",
              "epistemic.md#epi-obj-memory-metadata",
              "memory.md#mem-rte-startup-context"
            ],
            "note": "Structured access/control part is separate from prose interpretation."
          },
          {
            "scope": "Private identity schema at validation/rendering",
            "assessment": "known",
            "findings": [
              {
                "value": "symbolic",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-self"
                ],
                "note": "Localized fields are interpreted under fixed validation, identity, state or selection rules."
              }
            ],
            "records": [
              "memory.md#mem-obj-self"
            ],
            "note": "Structured access/control part is separate from prose interpretation."
          },
          {
            "scope": "Session key/ID/version mapping at resume selection",
            "assessment": "known",
            "findings": [
              {
                "value": "symbolic",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-codex-sessions"
                ],
                "note": "Localized fields are interpreted under fixed validation, identity, state or selection rules."
              }
            ],
            "records": [
              "memory.md#mem-obj-codex-sessions"
            ],
            "note": "Structured access/control part is separate from prose interpretation."
          },
          {
            "scope": "Conversation refs and task event/status fields at scan selection",
            "assessment": "known",
            "findings": [
              {
                "value": "symbolic",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-conversation-logs",
                  "memory.md#mem-obj-task-events",
                  "memory.md#mem-rte-evidence-update"
                ],
                "note": "Localized fields are interpreted under fixed validation, identity, state or selection rules."
              }
            ],
            "records": [
              "memory.md#mem-obj-conversation-logs",
              "memory.md#mem-obj-task-events",
              "memory.md#mem-rte-evidence-update"
            ],
            "note": "Structured access/control part is separate from prose interpretation."
          },
          {
            "scope": "Evidence IDs/status/linkage and scan checkpoint markers",
            "assessment": "known",
            "findings": [
              {
                "value": "symbolic",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-evidence-signals",
                  "memory.md#mem-obj-evidence-scans"
                ],
                "note": "Localized fields are interpreted under fixed validation, identity, state or selection rules."
              }
            ],
            "records": [
              "memory.md#mem-obj-evidence-signals",
              "memory.md#mem-obj-evidence-scans"
            ],
            "note": "Structured access/control part is separate from prose interpretation."
          },
          {
            "scope": "Candidate status/score/IDs and curation reference/classification fields",
            "assessment": "known",
            "findings": [
              {
                "value": "symbolic",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-evolve-candidate",
                  "memory.md#mem-obj-semantic-curation",
                  "memory.md#mem-rte-candidate-curation"
                ],
                "note": "Localized fields are interpreted under fixed validation, identity, state or selection rules."
              }
            ],
            "records": [
              "memory.md#mem-obj-evolve-candidate",
              "memory.md#mem-obj-semantic-curation",
              "memory.md#mem-rte-candidate-curation"
            ],
            "note": "Structured access/control part is separate from prose interpretation."
          },
          {
            "scope": "Lineage assessment version and task/adoption state",
            "assessment": "known",
            "findings": [
              {
                "value": "symbolic",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-lineage-inbox",
                  "runtime.md#rt-rte-lineage-adoption"
                ],
                "note": "Localized fields are interpreted under fixed validation, identity, state or selection rules."
              }
            ],
            "records": [
              "memory.md#mem-obj-lineage-inbox",
              "runtime.md#rt-rte-lineage-adoption"
            ],
            "note": "Structured access/control part is separate from prose interpretation."
          },
          {
            "scope": "Learning-artifact index and source/changed-file fields",
            "assessment": "known",
            "findings": [
              {
                "value": "symbolic",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-learning-artifact"
                ],
                "note": "Localized fields are interpreted under fixed validation, identity, state or selection rules."
              }
            ],
            "records": [
              "memory.md#mem-obj-learning-artifact"
            ],
            "note": "Structured access/control part is separate from prose interpretation."
          },
          {
            "scope": "Action journal step state and retained publication revision/stage fields",
            "assessment": "known",
            "findings": [
              {
                "value": "symbolic",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-obj-conversation-journal",
                  "workflow.md#wf-rte-review-handoff"
                ],
                "note": "Localized fields are interpreted under fixed validation, identity, state or selection rules."
              }
            ],
            "records": [
              "runtime.md#rt-obj-conversation-journal",
              "workflow.md#wf-rte-review-handoff"
            ],
            "note": "Structured access/control part is separate from prose interpretation."
          },
          {
            "scope": "Provider-native stored transcript/checkpoints",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-native-context"
            ],
            "note": "Readable outputs do not establish the complete encoding, numerical content or summary alternatives."
          },
          {
            "scope": "Plugin/profile retained payloads",
            "assessment": "uninspected",
            "findings": [],
            "records": [
              "runtime.md#rt-rte-extension-loading"
            ],
            "note": "No deployed payload implementation is supplied."
          }
        ],
        "records": [
          "memory.md#mem-obj-long-term",
          "epistemic.md#epi-obj-memory-text",
          "memory.md#mem-obj-self",
          "memory.md#mem-obj-conversation-logs",
          "memory.md#mem-rte-evidence-update",
          "memory.md#mem-obj-task-events",
          "runtime.md#rt-obj-validation-diagnostics",
          "runtime.md#rt-rte-task-work",
          "memory.md#mem-obj-evidence-signals",
          "memory.md#mem-obj-evolve-candidate",
          "memory.md#mem-bap-candidate-guidance",
          "memory.md#mem-obj-semantic-curation",
          "memory.md#mem-obj-learning-artifact",
          "memory.md#mem-obj-task-context",
          "memory.md#mem-rte-task-snapshot",
          "memory.md#mem-obj-lineage-inbox",
          "epistemic.md#epi-obj-lineage-assessment",
          "runtime.md#rt-obj-conversation-journal",
          "runtime.md#rt-rte-chat-actions",
          "epistemic.md#epi-obj-memory-metadata",
          "memory.md#mem-rte-startup-context",
          "memory.md#mem-obj-codex-sessions",
          "memory.md#mem-obj-evidence-scans",
          "memory.md#mem-rte-candidate-curation",
          "runtime.md#rt-rte-lineage-adoption",
          "workflow.md#wf-rte-review-handoff",
          "memory.md#mem-obj-native-context",
          "runtime.md#rt-rte-extension-loading"
        ],
        "note": "Inspected prose and fixed-rule parts are split by consumption. Opaque native payloads and plugin state prevent complete coverage; distributed-parametric inference models are not themselves accumulated memory in this scope."
      },
      "lineage": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Model-final-reply facts",
            "assessment": "known",
            "findings": [
              {
                "value": "authored",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-memory-admission"
                ],
                "note": "The conversational model proposes the retained fact text; the store clips and merges it."
              }
            ],
            "records": [
              "memory.md#mem-rte-memory-admission"
            ],
            "note": "Known final-reply producer does not establish initial store provenance."
          },
          {
            "scope": "Logged conversations/task events and extracted signals/task briefs",
            "assessment": "known",
            "findings": [
              {
                "value": "trace-extracted",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-conversation-logs",
                  "memory.md#mem-obj-task-events",
                  "memory.md#mem-rte-evidence-update",
                  "memory.md#mem-rte-task-snapshot"
                ],
                "note": "Host recording and model extraction/summary derive these parts from conversation or task activity."
              }
            ],
            "records": [
              "memory.md#mem-obj-conversation-logs",
              "memory.md#mem-obj-task-events",
              "memory.md#mem-rte-evidence-update",
              "memory.md#mem-rte-task-snapshot"
            ],
            "note": "This covers recorded trace-derived paths, not arbitrary initial contents or opaque native checkpoints."
          },
          {
            "scope": "Evidence-derived and brainstorming candidate prose",
            "assessment": "known",
            "findings": [
              {
                "value": "authored",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-evidence-update",
                  "runtime.md#rt-rte-evolve-admission",
                  "memory.md#mem-obj-evolve-candidate"
                ],
                "note": "Models author proposals and reasons."
              },
              {
                "value": "trace-extracted",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-evidence-update",
                  "runtime.md#rt-rte-evolve-admission",
                  "memory.md#mem-obj-evolve-candidate"
                ],
                "note": "The evidence-fed candidate path derives proposals from retained conversation/task observations; brainstorming can also consume completed-work summaries."
              }
            ],
            "records": [
              "memory.md#mem-rte-evidence-update",
              "runtime.md#rt-rte-evolve-admission",
              "memory.md#mem-obj-evolve-candidate"
            ],
            "note": "Authored proposals and their trace-fed derivation coexist; theme-only brainstorming is not thereby trace-derived."
          },
          {
            "scope": "Published skill source and lineage inbox source excerpts",
            "assessment": "known",
            "findings": [
              {
                "value": "imported",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-skill-assessment",
                  "epistemic.md#epi-obj-published-skill",
                  "memory.md#mem-obj-lineage-inbox"
                ],
                "note": "Foreign skill snapshots and parent-change material enter assessment as external reference."
              }
            ],
            "records": [
              "memory.md#mem-rte-skill-assessment",
              "epistemic.md#epi-obj-published-skill",
              "memory.md#mem-obj-lineage-inbox"
            ],
            "note": "Import does not establish the original author or truth of the external content."
          },
          {
            "scope": "Skill and lineage assessment outputs",
            "assessment": "known",
            "findings": [
              {
                "value": "authored",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-skill-assessment",
                  "epistemic.md#epi-rte-lineage-assessment"
                ],
                "note": "Model judgments/reasons are admitted into candidates or the inbox."
              }
            ],
            "records": [
              "memory.md#mem-rte-skill-assessment",
              "epistemic.md#epi-rte-lineage-assessment"
            ],
            "note": "Assessment output is distinct from imported source."
          },
          {
            "scope": "Semantic curations",
            "assessment": "known",
            "findings": [
              {
                "value": "authored",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-semantic-curation",
                  "memory.md#mem-rte-candidate-curation"
                ],
                "note": "Semantic model authors recommendation and reasons."
              },
              {
                "value": "other-compiled",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-semantic-curation",
                  "memory.md#mem-rte-candidate-curation"
                ],
                "note": "A deterministic safe-candidate fallback can construct the retained recommendation."
              }
            ],
            "records": [
              "memory.md#mem-obj-semantic-curation",
              "memory.md#mem-rte-candidate-curation"
            ],
            "note": "Separate recorded producers retain their own derivation."
          },
          {
            "scope": "Access mappings, scan checkpoints, recovery/publication state and work-artifact index",
            "assessment": "known",
            "findings": [
              {
                "value": "other-compiled",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-codex-sessions",
                  "memory.md#mem-obj-evidence-scans",
                  "runtime.md#rt-obj-conversation-journal",
                  "workflow.md#wf-rte-review-handoff",
                  "memory.md#mem-obj-learning-artifact"
                ],
                "note": "Host code constructs access/control records and clipped indexed work artifacts from provider or workflow results."
              }
            ],
            "records": [
              "memory.md#mem-obj-codex-sessions",
              "memory.md#mem-obj-evidence-scans",
              "runtime.md#rt-obj-conversation-journal",
              "workflow.md#wf-rte-review-handoff",
              "memory.md#mem-obj-learning-artifact"
            ],
            "note": "Host-constructed fields do not establish semantic fidelity of clipped text."
          },
          {
            "scope": "Initial facts, arbitrary library replacements and private identity authorship",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-long-term",
              "memory.md#mem-obj-self",
              "memory.md#mem-rte-memory-admission"
            ],
            "note": "Initial authorship and caller provenance are unresolved; an install API is not proof of imported or human-authored content."
          },
          {
            "scope": "Known inputs to opaque provider-native context",
            "assessment": "partial",
            "findings": [
              {
                "value": "authored",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-native-context"
                ],
                "note": "Requests, injected authored text and replies enter the session."
              },
              {
                "value": "trace-extracted",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-native-context"
                ],
                "note": "Action receipts and session activity supply recorded context."
              }
            ],
            "records": [
              "memory.md#mem-obj-native-context"
            ],
            "note": "Known input origins do not resolve internal compaction or alternative checkpoint provenance."
          },
          {
            "scope": "Plugin state provenance",
            "assessment": "uninspected",
            "findings": [],
            "records": [
              "runtime.md#rt-rte-extension-loading"
            ],
            "note": "Installed producer implementations are uninspected."
          }
        ],
        "records": [
          "memory.md#mem-rte-memory-admission",
          "memory.md#mem-obj-conversation-logs",
          "memory.md#mem-obj-task-events",
          "memory.md#mem-rte-evidence-update",
          "memory.md#mem-rte-task-snapshot",
          "runtime.md#rt-rte-evolve-admission",
          "memory.md#mem-obj-evolve-candidate",
          "memory.md#mem-rte-skill-assessment",
          "epistemic.md#epi-obj-published-skill",
          "memory.md#mem-obj-lineage-inbox",
          "epistemic.md#epi-rte-lineage-assessment",
          "memory.md#mem-obj-semantic-curation",
          "memory.md#mem-rte-candidate-curation",
          "memory.md#mem-obj-codex-sessions",
          "memory.md#mem-obj-evidence-scans",
          "runtime.md#rt-obj-conversation-journal",
          "workflow.md#wf-rte-review-handoff",
          "memory.md#mem-obj-learning-artifact",
          "memory.md#mem-obj-long-term",
          "memory.md#mem-obj-self",
          "memory.md#mem-obj-native-context",
          "runtime.md#rt-rte-extension-loading"
        ],
        "note": "Known derivation paths coexist with unresolved initialization and provider transformations. No known model author upgrades opaque embedding/checkpoint provenance."
      },
      "behavioral_authority": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Fact prose at startup model",
            "assessment": "known",
            "findings": [
              {
                "value": "knowledge",
                "basis": "wired",
                "records": [
                  "memory.md#mem-bap-retained-facts",
                  "memory.md#mem-rte-startup-context"
                ],
                "note": "Rendered facts supply descriptive context; workflow_rule labels do not make them standing instructions."
              }
            ],
            "records": [
              "memory.md#mem-bap-retained-facts",
              "memory.md#mem-rte-startup-context"
            ],
            "note": "Model compliance and actual reliance remain unobserved."
          },
          {
            "scope": "Fact confidence/time metadata at startup selector",
            "assessment": "known",
            "findings": [
              {
                "value": "ranking",
                "basis": "wired",
                "records": [
                  "epistemic.md#epi-obj-memory-metadata",
                  "memory.md#mem-rte-startup-context"
                ],
                "note": "Retained confidence and update time determine relative order under the budget."
              }
            ],
            "records": [
              "epistemic.md#epi-obj-memory-metadata",
              "memory.md#mem-rte-startup-context"
            ],
            "note": "Ranking input need not be a learned ranking policy."
          },
          {
            "scope": "Private identity text at startup model",
            "assessment": "known",
            "findings": [
              {
                "value": "instruction",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-self"
                ],
                "note": "Rendered identity supplies standing designation, relationship, personality and care guidance below system/developer instructions."
              }
            ],
            "records": [
              "memory.md#mem-obj-self"
            ],
            "note": "This concerns installed private identity, not static body identity."
          },
          {
            "scope": "Conversation/task trace content at automatic extraction and brief generation",
            "assessment": "known",
            "findings": [
              {
                "value": "learning",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-evidence-update",
                  "memory.md#mem-rte-task-snapshot"
                ],
                "note": "Retained experience feeds automatic durable proposal or task-context updates."
              }
            ],
            "records": [
              "memory.md#mem-rte-evidence-update",
              "memory.md#mem-rte-task-snapshot"
            ],
            "note": "Learning authority at update consumer does not establish improved capacity."
          },
          {
            "scope": "Derived signals and candidate text at synthesis, curator and later worker",
            "assessment": "known",
            "findings": [
              {
                "value": "knowledge",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-evidence-signals",
                  "memory.md#mem-obj-evolve-candidate",
                  "memory.md#mem-bap-candidate-guidance",
                  "memory.md#mem-rte-evidence-update"
                ],
                "note": "Observations and reasons provide evidence/reference to subsequent models."
              },
              {
                "value": "learning",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-evidence-signals",
                  "memory.md#mem-obj-evolve-candidate",
                  "memory.md#mem-bap-candidate-guidance",
                  "memory.md#mem-rte-evidence-update"
                ],
                "note": "Signals and retained candidate context feed subsequent durable candidate or curation artifacts."
              },
              {
                "value": "instruction",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-evidence-signals",
                  "memory.md#mem-obj-evolve-candidate",
                  "memory.md#mem-bap-candidate-guidance",
                  "memory.md#mem-rte-evidence-update"
                ],
                "note": "Approved candidate change/risk/test context supplies directions for the later implementation task."
              }
            ],
            "records": [
              "memory.md#mem-obj-evidence-signals",
              "memory.md#mem-obj-evolve-candidate",
              "memory.md#mem-bap-candidate-guidance",
              "memory.md#mem-rte-evidence-update"
            ],
            "note": "These are separate update, reference and worker-guidance consumers; proposal retention is not deployment."
          },
          {
            "scope": "Task snapshot at later worker",
            "assessment": "known",
            "findings": [
              {
                "value": "knowledge",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-task-snapshot"
                ],
                "note": "Selected prior decisions and target context inform later work."
              },
              {
                "value": "instruction",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-task-snapshot"
                ],
                "note": "Retained brief carries intended outcome, constraints and exclusions into the worker request."
              }
            ],
            "records": [
              "memory.md#mem-rte-task-snapshot"
            ],
            "note": "Clipping and summary correctness are not independently verified."
          },
          {
            "scope": "Retained diagnostic prose at later repair-model invocation",
            "assessment": "known",
            "findings": [
              {
                "value": "knowledge",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-obj-validation-diagnostics",
                  "runtime.md#rt-rte-task-work"
                ],
                "note": "Recorded failed-check results supply bounded diagnostic evidence to the later repair model; they are reference for proposing repairs, not standing instructions or proof of overall correctness."
              }
            ],
            "records": [
              "runtime.md#rt-obj-validation-diagnostics",
              "runtime.md#rt-rte-task-work"
            ],
            "note": "This unit covers retained diagnostic prose consumed through head/tail excerpts on the bounded repair path, separately from doctor predicates and publication receipts. Complete diagnostic preservation and successful repair remain unestablished."
          },
          {
            "scope": "Activity summary injected into later chat-native context",
            "assessment": "known",
            "findings": [
              {
                "value": "knowledge",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-activity-sync"
                ],
                "note": "Operation summary is supplied as factual recent context, explicitly not a new user request."
              }
            ],
            "records": [
              "memory.md#mem-rte-activity-sync"
            ],
            "note": "Exact provider retention and reliable recall remain unresolved."
          },
          {
            "scope": "Session mapping/version, scan checkpoints and action/publication state at host",
            "assessment": "known",
            "findings": [
              {
                "value": "routing",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-codex-sessions",
                  "memory.md#mem-obj-evidence-scans",
                  "runtime.md#rt-obj-conversation-journal",
                  "workflow.md#wf-rte-review-handoff"
                ],
                "note": "Stored IDs, markers and stages choose native session, pending inputs, recovery or publication continuation."
              },
              {
                "value": "enforcement",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-codex-sessions",
                  "memory.md#mem-obj-evidence-scans",
                  "runtime.md#rt-obj-conversation-journal",
                  "workflow.md#wf-rte-review-handoff"
                ],
                "note": "Version mismatch declines native mapping; running action state prevents blind replay; captured revision/state checks can refuse resume."
              },
              {
                "value": "validation",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-codex-sessions",
                  "memory.md#mem-obj-evidence-scans",
                  "runtime.md#rt-obj-conversation-journal",
                  "workflow.md#wf-rte-review-handoff"
                ],
                "note": "Stored expected revision/state provides a criterion for captured-copy/resume conformity."
              }
            ],
            "records": [
              "memory.md#mem-obj-codex-sessions",
              "memory.md#mem-obj-evidence-scans",
              "runtime.md#rt-obj-conversation-journal",
              "workflow.md#wf-rte-review-handoff"
            ],
            "note": "Validation finding is local to publication expected-state checks, not every listed field."
          },
          {
            "scope": "Candidate scores/status, evidence linkage and curation results",
            "assessment": "known",
            "findings": [
              {
                "value": "ranking",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-candidate-curation",
                  "epistemic.md#epi-rte-evidence-synthesis",
                  "epistemic.md#epi-rte-candidate-removal",
                  "memory.md#mem-obj-semantic-curation"
                ],
                "note": "Scores and retained curator recommendation determine proposal priority/choice."
              },
              {
                "value": "routing",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-candidate-curation",
                  "epistemic.md#epi-rte-evidence-synthesis",
                  "epistemic.md#epi-rte-candidate-removal",
                  "memory.md#mem-obj-semantic-curation"
                ],
                "note": "Candidate/evidence status and links select actionable or unlinked inputs."
              },
              {
                "value": "validation",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-candidate-curation",
                  "epistemic.md#epi-rte-evidence-synthesis",
                  "epistemic.md#epi-rte-candidate-removal",
                  "memory.md#mem-obj-semantic-curation"
                ],
                "note": "Stored removal suggestion IDs/classification/refs constrain a linked removal request."
              },
              {
                "value": "enforcement",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-candidate-curation",
                  "epistemic.md#epi-rte-evidence-synthesis",
                  "epistemic.md#epi-rte-candidate-removal",
                  "memory.md#mem-obj-semantic-curation"
                ],
                "note": "Inactive status excludes proposals; mismatched removal linkage is refused."
              },
              {
                "value": "knowledge",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-candidate-curation",
                  "epistemic.md#epi-rte-evidence-synthesis",
                  "epistemic.md#epi-rte-candidate-removal",
                  "memory.md#mem-obj-semantic-curation"
                ],
                "note": "Retained curation reasons advise proposal/removal decisions."
              }
            ],
            "records": [
              "memory.md#mem-rte-candidate-curation",
              "epistemic.md#epi-rte-evidence-synthesis",
              "epistemic.md#epi-rte-candidate-removal",
              "memory.md#mem-obj-semantic-curation"
            ],
            "note": "Suggestions do not remove entries by themselves; actor labels do not authenticate human approval."
          },
          {
            "scope": "Lineage source/assessment and linked state",
            "assessment": "known",
            "findings": [
              {
                "value": "knowledge",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-lineage-inbox",
                  "runtime.md#rt-rte-lineage-adoption",
                  "epistemic.md#epi-rte-lineage-assessment"
                ],
                "note": "Source/assessment prose provides advisory adaptation reference."
              },
              {
                "value": "instruction",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-lineage-inbox",
                  "runtime.md#rt-rte-lineage-adoption",
                  "epistemic.md#epi-rte-lineage-assessment"
                ],
                "note": "Chosen adaptation request/context directs later task work."
              },
              {
                "value": "routing",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-lineage-inbox",
                  "runtime.md#rt-rte-lineage-adoption",
                  "epistemic.md#epi-rte-lineage-assessment"
                ],
                "note": "Linked/adopted/version state selects reassessment and suppresses duplicate queueing."
              },
              {
                "value": "enforcement",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-lineage-inbox",
                  "runtime.md#rt-rte-lineage-adoption",
                  "epistemic.md#epi-rte-lineage-assessment"
                ],
                "note": "Unassessed or linked status blocks the ordinary adoption enqueue."
              }
            ],
            "records": [
              "memory.md#mem-obj-lineage-inbox",
              "runtime.md#rt-rte-lineage-adoption",
              "epistemic.md#epi-rte-lineage-assessment"
            ],
            "note": "Stored adoption is not evidence of restarted use."
          },
          {
            "scope": "Learning-artifact advice at declared descendant reader",
            "assessment": "known",
            "findings": [
              {
                "value": "knowledge",
                "basis": "claimed",
                "records": [
                  "memory.md#mem-obj-learning-artifact"
                ],
                "note": "Work summaries are offered as reference for descendant inspection/adaptation."
              }
            ],
            "records": [
              "memory.md#mem-obj-learning-artifact"
            ],
            "note": "Only declared reader guidance, not a wired descendant invocation."
          },
          {
            "scope": "Native context internal part/consumer authority",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-native-context"
            ],
            "note": "Known injected text does not determine complete stored payload or provider authority construction."
          },
          {
            "scope": "Plugin retained state consumers",
            "assessment": "uninspected",
            "findings": [],
            "records": [
              "runtime.md#rt-rte-extension-loading"
            ],
            "note": "Installed consumers and forces are uninspected."
          }
        ],
        "records": [
          "memory.md#mem-bap-retained-facts",
          "memory.md#mem-rte-startup-context",
          "epistemic.md#epi-obj-memory-metadata",
          "memory.md#mem-obj-self",
          "memory.md#mem-rte-evidence-update",
          "memory.md#mem-rte-task-snapshot",
          "memory.md#mem-obj-evidence-signals",
          "memory.md#mem-obj-evolve-candidate",
          "memory.md#mem-bap-candidate-guidance",
          "runtime.md#rt-obj-validation-diagnostics",
          "runtime.md#rt-rte-task-work",
          "memory.md#mem-rte-activity-sync",
          "memory.md#mem-obj-codex-sessions",
          "memory.md#mem-obj-evidence-scans",
          "runtime.md#rt-obj-conversation-journal",
          "workflow.md#wf-rte-review-handoff",
          "memory.md#mem-rte-candidate-curation",
          "epistemic.md#epi-rte-evidence-synthesis",
          "epistemic.md#epi-rte-candidate-removal",
          "memory.md#mem-obj-semantic-curation",
          "memory.md#mem-obj-lineage-inbox",
          "runtime.md#rt-rte-lineage-adoption",
          "epistemic.md#epi-rte-lineage-assessment",
          "memory.md#mem-obj-learning-artifact",
          "memory.md#mem-obj-native-context",
          "runtime.md#rt-rte-extension-loading"
        ],
        "note": "Consumer-specific authority includes update learning, downstream context/guidance and executable selection controls. Provider/plugin effects and incomplete maintenance producers prevent complete enumeration. Static capability policy and activated source are not substituted for retained memory."
      },
      "write_agency": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Final-reply fact admission",
            "assessment": "known",
            "findings": [
              {
                "value": "automatic",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-memory-admission"
                ],
                "note": "Model proposes and software validates/merges without per-content human approval."
              }
            ],
            "records": [
              "memory.md#mem-rte-memory-admission"
            ],
            "note": "Explicit/high defaults do not establish manual admission."
          },
          {
            "scope": "Snapshot, activity injection, evidence scan/synthesis, brainstorming and curation writes",
            "assessment": "known",
            "findings": [
              {
                "value": "automatic",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-task-snapshot",
                  "memory.md#mem-rte-activity-sync",
                  "memory.md#mem-rte-evidence-update",
                  "memory.md#mem-rte-candidate-curation",
                  "runtime.md#rt-rte-evolve-admission"
                ],
                "note": "Model/software admit derived content without a fresh human content decision."
              }
            ],
            "records": [
              "memory.md#mem-rte-task-snapshot",
              "memory.md#mem-rte-activity-sync",
              "memory.md#mem-rte-evidence-update",
              "memory.md#mem-rte-candidate-curation",
              "runtime.md#rt-rte-evolve-admission"
            ],
            "note": "Operator workflow initiation is not manual admission of the resulting content."
          },
          {
            "scope": "Session mappings, raw journals, checkpoints, learning artifacts and workflow stages",
            "assessment": "known",
            "findings": [
              {
                "value": "automatic",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-codex-sessions",
                  "memory.md#mem-obj-conversation-logs",
                  "memory.md#mem-obj-task-events",
                  "memory.md#mem-obj-evidence-scans",
                  "memory.md#mem-obj-learning-artifact",
                  "runtime.md#rt-obj-conversation-journal",
                  "workflow.md#wf-rte-review-handoff"
                ],
                "note": "Host/provider results automatically update these retained records."
              }
            ],
            "records": [
              "memory.md#mem-obj-codex-sessions",
              "memory.md#mem-obj-conversation-logs",
              "memory.md#mem-obj-task-events",
              "memory.md#mem-obj-evidence-scans",
              "memory.md#mem-obj-learning-artifact",
              "runtime.md#rt-obj-conversation-journal",
              "workflow.md#wf-rte-review-handoff"
            ],
            "note": "Physical file I/O is not the basis; recorded host admission is."
          },
          {
            "scope": "Published skill and lineage assessment admission",
            "assessment": "known",
            "findings": [
              {
                "value": "automatic",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-skill-assessment",
                  "epistemic.md#epi-rte-lineage-assessment"
                ],
                "note": "Parsed model judgment is stored without per-content human approval."
              }
            ],
            "records": [
              "memory.md#mem-rte-skill-assessment",
              "epistemic.md#epi-rte-lineage-assessment"
            ],
            "note": "Source selection and later adaptation approval are separate decisions."
          },
          {
            "scope": "Automatic candidate-source retirement and model-issued removal/approval controls",
            "assessment": "known",
            "findings": [
              {
                "value": "automatic",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-candidate-curation",
                  "runtime.md#rt-rte-chat-actions",
                  "epistemic.md#epi-rte-candidate-removal"
                ],
                "note": "Source retirement is code controlled, and model-issued commands can reuse handlers admitting status changes."
              }
            ],
            "records": [
              "memory.md#mem-rte-candidate-curation",
              "runtime.md#rt-rte-chat-actions",
              "epistemic.md#epi-rte-candidate-removal"
            ],
            "note": "A human actor string alone does not classify all invocations as manual."
          },
          {
            "scope": "Explicit human-requested removal/adaptation selection",
            "assessment": "known",
            "findings": [
              {
                "value": "manual",
                "basis": "wired",
                "records": [
                  "epistemic.md#epi-rte-candidate-removal",
                  "runtime.md#rt-rte-lineage-adoption"
                ],
                "note": "The explicitly human-requested branch supplies a content-specific removal or selected adaptation approval decision."
              }
            ],
            "records": [
              "epistemic.md#epi-rte-candidate-removal",
              "runtime.md#rt-rte-lineage-adoption"
            ],
            "note": "Manual is local to the human-decision branch; generic handler invocation is not authenticated as that branch."
          },
          {
            "scope": "Initial content, explicit library fact replacement, identity install/clear and generic command callers",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-rte-memory-admission",
              "memory.md#mem-obj-self",
              "memory.md#mem-obj-long-term",
              "epistemic.md#epi-rte-memory-withdrawal"
            ],
            "note": "Caller identity/control is unspecified for these capability surfaces; no blanket human or automatic classification."
          },
          {
            "scope": "Provider-native compaction/checkpoint admission",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-native-context"
            ],
            "note": "Provider producer and any operator replacement controls are unresolved."
          },
          {
            "scope": "Deployment-specific plugin admissions",
            "assessment": "uninspected",
            "findings": [],
            "records": [
              "runtime.md#rt-rte-extension-loading"
            ],
            "note": "Installed admission mechanisms are uninspected."
          }
        ],
        "records": [
          "memory.md#mem-rte-memory-admission",
          "memory.md#mem-rte-task-snapshot",
          "memory.md#mem-rte-activity-sync",
          "memory.md#mem-rte-evidence-update",
          "memory.md#mem-rte-candidate-curation",
          "runtime.md#rt-rte-evolve-admission",
          "memory.md#mem-obj-codex-sessions",
          "memory.md#mem-obj-conversation-logs",
          "memory.md#mem-obj-task-events",
          "memory.md#mem-obj-evidence-scans",
          "memory.md#mem-obj-learning-artifact",
          "runtime.md#rt-obj-conversation-journal",
          "workflow.md#wf-rte-review-handoff",
          "memory.md#mem-rte-skill-assessment",
          "epistemic.md#epi-rte-lineage-assessment",
          "runtime.md#rt-rte-chat-actions",
          "epistemic.md#epi-rte-candidate-removal",
          "runtime.md#rt-rte-lineage-adoption",
          "memory.md#mem-obj-self",
          "memory.md#mem-obj-long-term",
          "epistemic.md#epi-rte-memory-withdrawal",
          "memory.md#mem-obj-native-context",
          "runtime.md#rt-rte-extension-loading"
        ],
        "note": "Automatic derived admission and an explicitly human decision branch coexist. Initialization, generic APIs, provider maintenance and plugins remain unresolved; no global manual-control guarantee follows from approval labels."
      },
      "curation_operations": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Fact duplicate merge/confidence raise and forgetting",
            "assessment": "known",
            "findings": [
              {
                "value": "dedup",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-memory-admission",
                  "memory.md#mem-rte-startup-context"
                ],
                "note": "Equal normalized fact text is merged, including refs/tags, rather than kept as duplicate entries."
              },
              {
                "value": "evolve",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-memory-admission",
                  "memory.md#mem-rte-startup-context"
                ],
                "note": "Duplicate admission revises metadata of an existing retained entry."
              },
              {
                "value": "promote",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-memory-admission",
                  "memory.md#mem-rte-startup-context"
                ],
                "note": "Raising existing confidence can raise its position in confidence-ordered startup selection."
              },
              {
                "value": "decay",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-memory-admission",
                  "memory.md#mem-rte-startup-context"
                ],
                "note": "Forgetting physically removes a selected fact from the retained store."
              }
            ],
            "records": [
              "memory.md#mem-rte-memory-admission",
              "memory.md#mem-rte-startup-context"
            ],
            "note": "Deletion does not remove logs or already delivered native context; duplicate merge is more than a primary-key collision check."
          },
          {
            "scope": "Conversation-to-task brief and task-history/completion reduction",
            "assessment": "known",
            "findings": [
              {
                "value": "consolidate",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-task-snapshot",
                  "memory.md#mem-obj-completion-evidence",
                  "memory.md#mem-rte-candidate-curation"
                ],
                "note": "Retained conversation and task history are selected/compressed into bounded briefs or reduced completion representations."
              }
            ],
            "records": [
              "memory.md#mem-rte-task-snapshot",
              "memory.md#mem-obj-completion-evidence",
              "memory.md#mem-rte-candidate-curation"
            ],
            "note": "Transformation wiring does not guarantee preservation of every condition or all old history."
          },
          {
            "scope": "Extracted observations from retained turns/task snapshots",
            "assessment": "known",
            "findings": [
              {
                "value": "consolidate",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-evidence-update",
                  "epistemic.md#epi-rte-evidence-scan"
                ],
                "note": "The extraction route reduces selected retained activity into observations and desired outcomes for later consumption."
              }
            ],
            "records": [
              "memory.md#mem-rte-evidence-update",
              "epistemic.md#epi-rte-evidence-scan"
            ],
            "note": "No guarantee of faithful semantics; possible extraction defects do not by themselves establish synthesize."
          },
          {
            "scope": "Candidate status withdrawal, retirement and latest-terminal reliance",
            "assessment": "known",
            "findings": [
              {
                "value": "invalidate",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-candidate-curation",
                  "epistemic.md#epi-rte-regression-status"
                ],
                "note": "Removed/retired candidates retain history but lose current eligibility; later terminal regression withdraws reliance on stale completion."
              },
              {
                "value": "evolve",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-candidate-curation",
                  "epistemic.md#epi-rte-regression-status"
                ],
                "note": "Retained task/candidate status is revised under implemented transitions."
              }
            ],
            "records": [
              "memory.md#mem-rte-candidate-curation",
              "epistemic.md#epi-rte-regression-status"
            ],
            "note": "Suggestions alone are not withdrawal, and a reverted status is not a repository revert."
          },
          {
            "scope": "Semantic novelty of generated candidates and curations",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "epistemic.md#epi-rte-evidence-synthesis",
              "epistemic.md#epi-rte-candidate-curation",
              "runtime.md#rt-rte-evolve-admission"
            ],
            "note": "A synthesis/brainstorming name and expected-benefit prose do not establish that an output claim is absent from inputs. Accepted records leave semantic relation indeterminate; synthesize is not asserted."
          },
          {
            "scope": "Scheduled-context refresh, lineage invalidation and promotion-producer maintenance",
            "assessment": "uninspected",
            "findings": [],
            "records": [
              "memory.md#mem-obj-task-context",
              "memory.md#mem-obj-lineage-inbox",
              "memory.md#mem-obj-completion-evidence",
              "memory.md#mem-rte-candidate-curation"
            ],
            "note": "Complete maintenance producers and refresh rules were not inspected; no complete operation set follows."
          },
          {
            "scope": "Native session compaction and alternative checkpoint transformation",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-native-context"
            ],
            "note": "Internal compaction, raw/derived alternatives and transformation control are uninspected."
          },
          {
            "scope": "Plugin memory maintenance",
            "assessment": "uninspected",
            "findings": [],
            "records": [
              "runtime.md#rt-rte-extension-loading"
            ],
            "note": "Installed transformations are uninspected."
          }
        ],
        "records": [
          "memory.md#mem-rte-memory-admission",
          "memory.md#mem-rte-startup-context",
          "memory.md#mem-rte-task-snapshot",
          "memory.md#mem-obj-completion-evidence",
          "memory.md#mem-rte-candidate-curation",
          "memory.md#mem-rte-evidence-update",
          "epistemic.md#epi-rte-evidence-scan",
          "epistemic.md#epi-rte-regression-status",
          "epistemic.md#epi-rte-evidence-synthesis",
          "epistemic.md#epi-rte-candidate-curation",
          "runtime.md#rt-rte-evolve-admission",
          "memory.md#mem-obj-task-context",
          "memory.md#mem-obj-lineage-inbox",
          "memory.md#mem-obj-native-context",
          "runtime.md#rt-rte-extension-loading"
        ],
        "note": "Implemented consolidation, merge/revision, salience raise, forgetting and history-preserving withdrawal are kept local. Semantic novelty, native compaction and ancillary maintenance prevent complete classification; route names do not establish synthesize."
      },
      "read_back_direction": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Startup fact/private-identity rendering",
            "assessment": "known",
            "findings": [
              {
                "value": "push",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-startup-context"
                ],
                "note": "New/uncontextualized session or absent Codex map triggers automatic retained-context supply without a consumer recall request."
              }
            ],
            "records": [
              "memory.md#mem-rte-startup-context"
            ],
            "note": "Both application and adapter injection layers are included; double delivery is possible."
          },
          {
            "scope": "Snapshot creation and later task delivery",
            "assessment": "known",
            "findings": [
              {
                "value": "pull",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-task-snapshot"
                ],
                "note": "The snapshot request asks the conversation runtime for relevant retained prior context."
              },
              {
                "value": "push",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-task-snapshot"
                ],
                "note": "Host later adds the retained brief to a separate worker request without that worker asking for recall."
              }
            ],
            "records": [
              "memory.md#mem-rte-task-snapshot"
            ],
            "note": "Requested summary return is pull, not an additional push; later worker supply is a separate operation."
          },
          {
            "scope": "Activity and scheduled evidence/curation inputs",
            "assessment": "known",
            "findings": [
              {
                "value": "push",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-activity-sync",
                  "memory.md#mem-rte-evidence-update",
                  "memory.md#mem-rte-candidate-curation"
                ],
                "note": "Host selects prior material and injects it into chat or isolated extraction/curation invocations."
              }
            ],
            "records": [
              "memory.md#mem-rte-activity-sync",
              "memory.md#mem-rte-evidence-update",
              "memory.md#mem-rte-candidate-curation"
            ],
            "note": "An upstream scan trigger is not a model request to recall the selected payload."
          },
          {
            "scope": "Named candidate/lineage approval context and administrative fact display",
            "assessment": "known",
            "findings": [
              {
                "value": "pull",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-memory-admission",
                  "memory.md#mem-obj-long-term",
                  "runtime.md#rt-rte-evolve-admission",
                  "runtime.md#rt-rte-lineage-adoption"
                ],
                "note": "Explicit commands request named retained candidate/assessment or memory status."
              },
              {
                "value": "push",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-memory-admission",
                  "memory.md#mem-obj-long-term",
                  "runtime.md#rt-rte-evolve-admission",
                  "runtime.md#rt-rte-lineage-adoption"
                ],
                "note": "Host supplies the selected approved candidate/assessment reasons to the later worker."
              }
            ],
            "records": [
              "memory.md#mem-rte-memory-admission",
              "memory.md#mem-obj-long-term",
              "runtime.md#rt-rte-evolve-admission",
              "runtime.md#rt-rte-lineage-adoption"
            ],
            "note": "The requested display is pull; subsequent unsolicited worker-context supply is push."
          },
          {
            "scope": "Native resume access and recovery/publication lookup",
            "assessment": "known",
            "findings": [
              {
                "value": "push",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-codex-sessions",
                  "runtime.md#rt-rte-chat-actions",
                  "workflow.md#wf-rte-review-handoff"
                ],
                "note": "Host automatically selects native session or retained journal/publication state for the continuing invocation."
              }
            ],
            "records": [
              "memory.md#mem-obj-codex-sessions",
              "runtime.md#rt-rte-chat-actions",
              "workflow.md#wf-rte-review-handoff"
            ],
            "note": "External native content selection remains unresolved separately."
          },
          {
            "scope": "Declared descendant learning-artifact inspection",
            "assessment": "known",
            "findings": [
              {
                "value": "pull",
                "basis": "claimed",
                "records": [
                  "memory.md#mem-obj-learning-artifact"
                ],
                "note": "Descendants are told to inspect the retained work/skill artifact on their own initiative."
              }
            ],
            "records": [
              "memory.md#mem-obj-learning-artifact"
            ],
            "note": "This is declared guidance only, not wired deployed read-back."
          },
          {
            "scope": "Provider-internal retained parts and reload alternatives",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-native-context"
            ],
            "note": "Resume wiring does not establish every internal request/delivery operation."
          },
          {
            "scope": "Plugin read-back",
            "assessment": "uninspected",
            "findings": [],
            "records": [
              "runtime.md#rt-rte-extension-loading"
            ],
            "note": "Installed read/selection paths are uninspected."
          }
        ],
        "records": [
          "memory.md#mem-rte-startup-context",
          "memory.md#mem-rte-task-snapshot",
          "memory.md#mem-rte-activity-sync",
          "memory.md#mem-rte-evidence-update",
          "memory.md#mem-rte-candidate-curation",
          "memory.md#mem-rte-memory-admission",
          "memory.md#mem-obj-long-term",
          "runtime.md#rt-rte-evolve-admission",
          "runtime.md#rt-rte-lineage-adoption",
          "memory.md#mem-obj-codex-sessions",
          "runtime.md#rt-rte-chat-actions",
          "workflow.md#wf-rte-review-handoff",
          "memory.md#mem-obj-learning-artifact",
          "memory.md#mem-obj-native-context",
          "runtime.md#rt-rte-extension-loading"
        ],
        "note": "Pull requests and independent automatic supplies coexist and are separated within chains. Opaque provider/plugin alternatives prevent a complete direction inventory."
      },
      "read_back_signal": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Startup injection trigger and confidence/date budget selection",
            "assessment": "known",
            "findings": [
              {
                "value": "coarse",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-startup-context"
                ],
                "note": "New-session/absent-map availability plus global confidence/date ordering and character budget selects retained facts and fixed identity fields."
              }
            ],
            "records": [
              "memory.md#mem-rte-startup-context"
            ],
            "note": "No query-conditioned semantic or lexical targeting is recorded; displayed IDs do not establish identifier selection."
          },
          {
            "scope": "Snapshot selection for retained worker brief",
            "assessment": "known",
            "findings": [
              {
                "value": "inferred-judgment",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-task-snapshot"
                ],
                "note": "On snapshot creation the conversation model selects relevant prior decisions/constraints from session context for later worker delivery."
              }
            ],
            "records": [
              "memory.md#mem-rte-task-snapshot"
            ],
            "note": "Trigger is task/backlog/cron creation; selector input is prior chat and summary objective; selected retained part is the bounded brief."
          },
          {
            "scope": "Activity summary selection at note flush",
            "assessment": "known",
            "findings": [
              {
                "value": "coarse",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-activity-sync"
                ],
                "note": "Host operation type and nonempty queued note select a clipped result summary."
              }
            ],
            "records": [
              "memory.md#mem-rte-activity-sync"
            ],
            "note": "Trigger is note flush; operation result and nonempty queued-note availability are selector inputs; delivered part is the clipped operation note, not the worker transcript. The conversation key routes that note to a consumer session; it does not identity-match retained note parts for delivery and establishes no identifier signal in this unit."
          },
          {
            "scope": "Evidence scan input/checkpoint selection",
            "assessment": "known",
            "findings": [
              {
                "value": "identifier",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-evidence-update",
                  "memory.md#mem-obj-evidence-scans"
                ],
                "note": "Processed conversation refs and per-task latest-event markers select unprocessed or changed retained trace parts."
              },
              {
                "value": "coarse",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-evidence-update",
                  "memory.md#mem-obj-evidence-scans"
                ],
                "note": "Batch threshold, status, reader limits and availability bound the selected trace/signals."
              }
            ],
            "records": [
              "memory.md#mem-rte-evidence-update",
              "memory.md#mem-obj-evidence-scans"
            ],
            "note": "Manual/due scan triggers selection from logged turns/task events; checkpoint identities do real filtering, unlike merely displayed refs."
          },
          {
            "scope": "Candidate/completion selection and downstream recommendation",
            "assessment": "known",
            "findings": [
              {
                "value": "coarse",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-candidate-curation",
                  "memory.md#mem-obj-semantic-curation"
                ],
                "note": "Actionable status, deterministic rank/source diversity and bounded latest-terminal completion select curator inputs."
              },
              {
                "value": "inferred-judgment",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-candidate-curation",
                  "memory.md#mem-obj-semantic-curation"
                ],
                "note": "Curator interprets candidate/completion prose to choose a retained candidate recommendation."
              },
              {
                "value": "identifier",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-candidate-curation",
                  "memory.md#mem-obj-semantic-curation"
                ],
                "note": "Stored recommendation or approved candidate ID selects the particular retained candidate delivered downstream."
              }
            ],
            "records": [
              "memory.md#mem-rte-candidate-curation",
              "memory.md#mem-obj-semantic-curation"
            ],
            "note": "Curator trigger is proposal construction; candidate/completion fields are inputs; selected retained parts are candidate snapshots and reasons. Semantic removal suggestions do not themselves delete."
          },
          {
            "scope": "Session and task/publication recovery matching",
            "assessment": "known",
            "findings": [
              {
                "value": "identifier",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-codex-sessions",
                  "runtime.md#rt-obj-conversation-journal",
                  "workflow.md#wf-rte-review-handoff"
                ],
                "note": "Application session key, request key or task/revision identity selects the corresponding retained mapping/journal/publication state."
              }
            ],
            "records": [
              "memory.md#mem-obj-codex-sessions",
              "runtime.md#rt-obj-conversation-journal",
              "workflow.md#wf-rte-review-handoff"
            ],
            "note": "Continuation/retry is trigger; matching identity selects operative retained state. Native internal payload selection is not inferred from this local match."
          },
          {
            "scope": "Provider-internal selection among retained transcript/checkpoints",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-native-context"
            ],
            "note": "Opaque payload and compaction prevent complete signal classification."
          },
          {
            "scope": "Plugin selection signals",
            "assessment": "uninspected",
            "findings": [],
            "records": [
              "runtime.md#rt-rte-extension-loading"
            ],
            "note": "Installed selectors and retained parts are uninspected."
          }
        ],
        "records": [
          "memory.md#mem-rte-startup-context",
          "memory.md#mem-rte-task-snapshot",
          "memory.md#mem-rte-activity-sync",
          "memory.md#mem-rte-evidence-update",
          "memory.md#mem-obj-evidence-scans",
          "memory.md#mem-rte-candidate-curation",
          "memory.md#mem-obj-semantic-curation",
          "memory.md#mem-obj-codex-sessions",
          "runtime.md#rt-obj-conversation-journal",
          "workflow.md#wf-rte-review-handoff",
          "memory.md#mem-obj-native-context",
          "runtime.md#rt-rte-extension-loading"
        ],
        "note": "Push selectors include coarse filters, real identity matches and model relevance judgment. No inferred lexical/embedding selector is established by the accepted records. That is not a bounded absence of such alternatives."
      },
      "trace_learning": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Automatic feedback/experience to signals/candidates to curator/worker",
            "assessment": "known",
            "findings": [
              {
                "value": "yes",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-evidence-update",
                  "memory.md#mem-obj-conversation-logs",
                  "memory.md#mem-obj-task-events",
                  "memory.md#mem-bap-candidate-guidance"
                ],
                "note": "Automatic trace-fed writes retain behavior-shaping observations/proposals that later curator and approved worker invocations consume."
              }
            ],
            "records": [
              "memory.md#mem-rte-evidence-update",
              "memory.md#mem-obj-conversation-logs",
              "memory.md#mem-obj-task-events",
              "memory.md#mem-bap-candidate-guidance"
            ],
            "note": "Wired retained guidance qualifies without installed software, improved capacity or observed benefit."
          },
          {
            "scope": "Conversation snapshot to retained task/backlog/cron brief to worker",
            "assessment": "known",
            "findings": [
              {
                "value": "yes",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-task-snapshot",
                  "memory.md#mem-obj-task-context"
                ],
                "note": "Recorded prior conversational experience is automatically summarized, retained and supplied as later worker context/guidance."
              }
            ],
            "records": [
              "memory.md#mem-rte-task-snapshot",
              "memory.md#mem-obj-task-context"
            ],
            "note": "Continuation/brief summaries qualify; fidelity and scheduled refresh are separate limits."
          },
          {
            "scope": "Operation-result activity note to chat session",
            "assessment": "partial",
            "findings": [
              {
                "value": "yes",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-activity-sync",
                  "memory.md#mem-obj-native-context"
                ],
                "note": "Automatic task/update summary delivery writes recent operational experience into a persistent chat session for later continuation."
              }
            ],
            "records": [
              "memory.md#mem-rte-activity-sync",
              "memory.md#mem-obj-native-context"
            ],
            "note": "Host chain is wired, but exact external retention/compaction and later use are uninspected."
          },
          {
            "scope": "Brainstorm candidates using completed-work summaries",
            "assessment": "partial",
            "findings": [
              {
                "value": "yes",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-rte-evolve-admission",
                  "memory.md#mem-obj-evolve-candidate"
                ],
                "note": "The completed-work-input branch automatically retains proposals later consumed by curator/worker."
              }
            ],
            "records": [
              "runtime.md#rt-rte-evolve-admission",
              "memory.md#mem-obj-evolve-candidate"
            ],
            "note": "Theme-only brainstorming is not converted to a trace-fed path; full original provenance of all completion inputs is unresolved."
          },
          {
            "scope": "Final-reply remembered facts and generic initial/library writes",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-rte-memory-admission",
              "memory.md#mem-obj-long-term",
              "memory.md#mem-obj-self"
            ],
            "note": "Automatic fact retention is known but complete original input/provenance is not; no blanket trace yes or no is inferred from a memory marker."
          },
          {
            "scope": "Learning-artifact descendant update",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-learning-artifact",
              "epistemic.md#epi-rte-learning-artifact"
            ],
            "note": "Trace-derived work record is retained, but concrete later behavior-shaping consumption is not wired in accepted records; declared inspection advice does not close that route."
          },
          {
            "scope": "Foreign-skill and lineage input history",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-rte-skill-assessment",
              "memory.md#mem-obj-lineage-inbox"
            ],
            "note": "Imported static skill content alone is not trace origin; full parent/source input content is not established enough for a complete trace-fed-route classification."
          },
          {
            "scope": "Native provider compaction/checkpoint alternatives",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-native-context"
            ],
            "note": "Automatic compaction and alternative retained outputs are uninspected; plain raw transcript accumulation is not itself a qualifying update."
          },
          {
            "scope": "Plugin trace-fed updates",
            "assessment": "uninspected",
            "findings": [],
            "records": [
              "runtime.md#rt-rte-extension-loading"
            ],
            "note": "Installed transformations/later consumers are uninspected."
          }
        ],
        "records": [
          "memory.md#mem-rte-evidence-update",
          "memory.md#mem-obj-conversation-logs",
          "memory.md#mem-obj-task-events",
          "memory.md#mem-bap-candidate-guidance",
          "memory.md#mem-rte-task-snapshot",
          "memory.md#mem-obj-task-context",
          "memory.md#mem-rte-activity-sync",
          "memory.md#mem-obj-native-context",
          "runtime.md#rt-rte-evolve-admission",
          "memory.md#mem-obj-evolve-candidate",
          "memory.md#mem-rte-memory-admission",
          "memory.md#mem-obj-long-term",
          "memory.md#mem-obj-self",
          "memory.md#mem-obj-learning-artifact",
          "epistemic.md#epi-rte-learning-artifact",
          "memory.md#mem-rte-skill-assessment",
          "memory.md#mem-obj-lineage-inbox",
          "runtime.md#rt-rte-extension-loading"
        ],
        "note": "Supported yes routes coexist with unresolved writes and consumers. No bounded absence records justify a local or global no; this axis is independent of demonstrated learning or self-improvement."
      },
      "trace_source": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Feedback-derived signals/candidates",
            "assessment": "known",
            "findings": [
              {
                "value": "session-logs",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-evidence-update",
                  "memory.md#mem-obj-conversation-logs"
                ],
                "note": "The original input is recorded user message/reply pairs from agent conversation, not event-streams merely because serialized as JSONL."
              }
            ],
            "records": [
              "memory.md#mem-rte-evidence-update",
              "memory.md#mem-obj-conversation-logs"
            ],
            "note": "User feedback and Enoch replies are mixed; later observations are not original event sources."
          },
          {
            "scope": "Experience-derived signals/candidates",
            "assessment": "partial",
            "findings": [
              {
                "value": "event-streams",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-evidence-update",
                  "memory.md#mem-obj-task-events"
                ],
                "note": "Host task lifecycle, validation, cancellation and regression events are discrete runtime activity records."
              }
            ],
            "records": [
              "memory.md#mem-rte-evidence-update",
              "memory.md#mem-obj-task-events"
            ],
            "note": "Recorded task result fields may include model/tool-origin material whose full source content is unresolved. Event grouping alone does not establish linked states/actions/outcomes as trajectories."
          },
          {
            "scope": "Conversation-to-task brief",
            "assessment": "known",
            "findings": [
              {
                "value": "session-logs",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-task-snapshot"
                ],
                "note": "Summary consumes prior same-session conversation and retains a selected brief for later work."
              }
            ],
            "records": [
              "memory.md#mem-rte-task-snapshot"
            ],
            "note": "No full transcript is passed to the worker; original source remains conversation rather than a new event stream."
          },
          {
            "scope": "Operation-result activity summary",
            "assessment": "partial",
            "findings": [
              {
                "value": "event-streams",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-activity-sync",
                  "runtime.md#rt-rte-software-update",
                  "workflow.md#wf-rte-review-handoff"
                ],
                "note": "Host update and work capture/publication outcomes trigger retained recent-activity notes."
              }
            ],
            "records": [
              "memory.md#mem-rte-activity-sync",
              "runtime.md#rt-rte-software-update",
              "workflow.md#wf-rte-review-handoff"
            ],
            "note": "Clipped operation results may contain other origins; complete original tool/session content is not recorded."
          },
          {
            "scope": "Brainstorm completed-work input",
            "assessment": "partial",
            "findings": [
              {
                "value": "event-streams",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-rte-evolve-admission",
                  "memory.md#mem-obj-task-events",
                  "memory.md#mem-obj-evolve-candidate"
                ],
                "note": "The recorded completed-work branch draws summaries of task operational outcomes into durable proposals."
              }
            ],
            "records": [
              "runtime.md#rt-rte-evolve-admission",
              "memory.md#mem-obj-task-events",
              "memory.md#mem-obj-evolve-candidate"
            ],
            "note": "Source context hash is not full raw input. Theme-only/static-skill inputs do not add a trace source; mixed historical provenance remains unresolved."
          },
          {
            "scope": "Unresolved fact, artifact-descendant, external assessment and native checkpoint write paths",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-rte-memory-admission",
              "memory.md#mem-obj-learning-artifact",
              "memory.md#mem-rte-skill-assessment",
              "memory.md#mem-obj-lineage-inbox",
              "memory.md#mem-obj-native-context"
            ],
            "note": "Qualification or full original input is unresolved for these included alternatives; no inferred tool-traces or trajectories value follows from a task label or provider output."
          },
          {
            "scope": "Plugin trace-source inputs",
            "assessment": "uninspected",
            "findings": [],
            "records": [
              "runtime.md#rt-rte-extension-loading"
            ],
            "note": "Installed qualifying writes and their original inputs are uninspected."
          }
        ],
        "records": [
          "memory.md#mem-rte-evidence-update",
          "memory.md#mem-obj-conversation-logs",
          "memory.md#mem-obj-task-events",
          "memory.md#mem-rte-task-snapshot",
          "memory.md#mem-rte-activity-sync",
          "runtime.md#rt-rte-software-update",
          "workflow.md#wf-rte-review-handoff",
          "runtime.md#rt-rte-evolve-admission",
          "memory.md#mem-obj-evolve-candidate",
          "memory.md#mem-rte-memory-admission",
          "memory.md#mem-obj-learning-artifact",
          "memory.md#mem-rte-skill-assessment",
          "memory.md#mem-obj-lineage-inbox",
          "memory.md#mem-obj-native-context",
          "runtime.md#rt-rte-extension-loading"
        ],
        "note": "Session logs and runtime event sources are supported locally. Partial mixed/opaque source inventories are retained; no claim of complete trace-source enumeration or inapplicability follows from known routes."
      }
    }
  }
}
---

# Enoch memory profile

## Comparison rationale

This profile classifies accepted records, not additional source evidence. All positive findings concern wired implementation except the explicitly claimed learning-artifact descendant route. None asserts observed activation, faithful model interpretation, improved future capacity or causal benefit. Coverage remains partial on every axis because included native payloads and deployment-specific state are unresolved, not because source-only evidence cannot establish wired capacity.

The local JSON/JSONL/Markdown inventory supports files, not a database, repository or vector substrate merely from serialization or task repository use. Session ID mappings are access metadata; they do not reveal native storage or representational form. Static shipped instructions and external inference weights are not use-accumulated memory. See [MEM-OBJ-codex-sessions](memory.md#mem-obj-codex-sessions), [MEM-OBJ-native-context](memory.md#mem-obj-native-context) and [RT-RTE-extension-loading](runtime.md#rt-rte-extension-loading).

Authority follows the actual consumer. Descriptive facts supply knowledge; confidence/time fields supply ranking; private identity supplies standing guidance. Trace inputs supply learning authority at automatic update consumers, while derived reasons and briefs supply knowledge or directions downstream. Stored checkpoints, statuses and reference agreement govern routing, eligibility and validation. Retained failed-check diagnostic prose supplies knowledge to a later repair model through bounded excerpts, separately from the doctor check's publication gate and review receipts; see [RT-OBJ-validation-diagnostics](runtime.md#rt-obj-validation-diagnostics) and [RT-RTE-task-work](runtime.md#rt-rte-task-work). Unconsumed provenance has no inferred authority. See [MEM-RTE-startup-context](memory.md#mem-rte-startup-context), [MEM-RTE-evidence-update](memory.md#mem-rte-evidence-update), [MEM-RTE-task-snapshot](memory.md#mem-rte-task-snapshot), [MEM-RTE-candidate-curation](memory.md#mem-rte-candidate-curation) and [WF-RTE-review-handoff](workflow.md#wf-rte-review-handoff).

Admission is independent of authorship and I/O. Model-final fact saves and derived proposal/brief writes are automatic even when a human starts their workflows. The explicit human-requested branch is manual only at its own content-specific decision. Generic callers and human actor labels do not authenticate such a decision. Private identity installation, initial contents and provider checkpoint replacements remain unresolved. See [MEM-RTE-memory-admission](memory.md#mem-rte-memory-admission), [MEM-OBJ-self](memory.md#mem-obj-self) and [EPI-RTE-candidate-removal](epistemic.md#epi-rte-candidate-removal).

Curation follows transformations, not route names. Bounded summaries/extraction consolidate; normalized-text merges deduplicate and revise metadata; increased confidence can promote startup salience; physical forgetting removes facts; candidate retirement and later regression invalidate reliance while retaining history. A command named synthesis does not establish a new claim absent from inputs. Accepted epistemic records retain indeterminate semantic relations, so synthesize is unresolved rather than asserted. See [MEM-RTE-memory-admission](memory.md#mem-rte-memory-admission), [MEM-RTE-task-snapshot](memory.md#mem-rte-task-snapshot), [MEM-RTE-candidate-curation](memory.md#mem-rte-candidate-curation) and [EPI-RTE-evidence-synthesis](epistemic.md#epi-rte-evidence-synthesis).

Read-back chains separate a requested summary/display from automatic later supply. Startup is coarse availability/rank/budget selection, not identifier targeting merely because IDs appear in text. Activity-note flush selects a nonempty clipped operation summary coarsely; its conversation key identifies the receiving session, not which retained note parts to deliver, so that route carries no identifier signal. Actual session/checkpoint/candidate identity matches do select operative retained parts. Model selection of relevant prior context and candidate recommendation supplies inferred judgment. Native internal selectors remain opaque. See [MEM-RTE-startup-context](memory.md#mem-rte-startup-context), [MEM-RTE-task-snapshot](memory.md#mem-rte-task-snapshot), [MEM-RTE-evidence-update](memory.md#mem-rte-evidence-update) and [MEM-RTE-candidate-curation](memory.md#mem-rte-candidate-curation).

The trace-learning union retains yes from automatic retained task briefs and trace-fed proposals; activity and brainstorming branches keep their own provider/mixed-input limits. Conversation messages remain session-log sources, while task lifecycle and operation outcomes supply event sources. Neither a learning-artifact label nor raw-log retention closes a later-consumer route. No no finding or inapplicable trace-source unit is inferred from missing observation. See [MEM-RTE-evidence-update](memory.md#mem-rte-evidence-update), [MEM-RTE-task-snapshot](memory.md#mem-rte-task-snapshot), [MEM-RTE-activity-sync](memory.md#mem-rte-activity-sync), [MEM-OBJ-learning-artifact](memory.md#mem-obj-learning-artifact) and [RT-RTE-evolve-admission](runtime.md#rt-rte-evolve-admission).

Reconciliation supersedes the duplicate epistemic EvidenceSignal, SemanticCuration and LearningArtifact objects with their memory declarations, and the epistemic published-skill route with the memory route. This profile cites those canonical destinations; the supersessions change identity, not evidence strength or semantic warrant. Valid containers and their distinct parts remain separate, including remembered text/metadata, candidate drafts versus durable candidates, and lineage assessment versus inbox. No supersession upgrades a classification or removes an opaque alternative.

Source-read log: none. No source ambiguity required a direct read; classifications use only the supplied accepted members and reconciliation. Missing native checkpoint contents/control, initial-content principals, promotion producers, scheduled-context refresh, lineage invalidation and installed plugin implementations prevent stronger coverage, without erasing the positive local mechanisms.
