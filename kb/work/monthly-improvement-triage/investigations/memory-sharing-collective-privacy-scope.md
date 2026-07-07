# Investigation: Is "collective privacy" from the human-to-AI memory survey in scope?

## Origin

Carried forward from `kb/work/connect-maintenance-observations/README.md`, row:

> open | Memory-sharing privacy from the human-to-AI memory survey has no KB note. | Search found shared-memory mentions but no memory-sharing/privacy treatment. | Decide whether "collective privacy" is in scope for Commonplace or only source context.

This is a scope decision, not a note-worthiness decision: the first question is whether the topic belongs in Commonplace's KB at all.

## What I read

**Source**: `kb/sources/from-human-memory-to-ai-memory-survey-llm-memory-mechanisms.md` (full 341-line snapshot of the arXiv 3D-8Q memory survey), specifically Section 5 "Open Problems and Future Directions," subsections "From Exclusive Memory to Shared Memory" (lines 315-319) and "From Individual Privacy to Collective Privacy" (lines 321-325).

The shared-memory subsection describes a forward-looking vision: currently isolated per-system LLM memory becoming interconnected across domains (e.g., a medical LLM sharing memory with a finance LLM), improving efficiency and cross-domain knowledge transfer.

The collective-privacy subsection frames a shift in privacy focus: as data sharing increases, protection must move from safeguarding individually identifiable personal data to protecting *groups or communities* whose aggregated data gets used for group-level profiling, large-scale analysis, and prediction — raising concerns about excessive surveillance and group-level profiling, not just individual data leakage. It calls for techniques balancing data utility against privacy preservation as AI memory systems interconnect. This is explicitly aspirational, one paragraph, with no proposed mechanism, system, or evaluation.

**Ingest**: `kb/sources/from-human-memory-to-ai-memory-survey-llm-memory-mechanisms.ingest.md`, read in full. This ingest (dated 2026-06-09) already did serious extraction work on this survey and explicitly flagged this exact gap as Extractable Value item 6:

> "Named coverage gap: shared memory and collective privacy. ... nearest hits are about coordination and authority, not aggregated-data privacy. A candidate topic if cross-agent memory becomes in-scope for our methodology." — tagged `[deep-dive]`, the lowest-urgency extraction tier used in this ingest.

The ingest's Limitations section separately cautions that the survey's whole future-directions section (including this one) "is aspirational and should not be read as evidence those directions are tractable" — the survey organizes a field, it does not test anything.

The Recommended Next Action in the ingest explicitly deferred this: it authorized only a low-effort `evidence` edge addition to a different note (`three-space-agent-memory-echoes-tulvings-taxonomy`) and said not to pursue further synthesis beyond what's already flagged, unless a writer judges it adds value.

## Existing KB coverage checked

Searched `kb/agent-memory-systems/`, `kb/notes/agent-memory-README.md`, and `kb/notes/agent-memory-requirements/` for any existing treatment of multi-agent/multi-user memory sharing, access control, or privacy boundaries.

Found substantial existing coverage of the *access-control* angle, close to but distinct from "collective privacy":

- `kb/notes/agent-memory-requirements/make-authority-explicit.md` — has a dedicated section "Access Control, Tenancy, And Audit": "Write authority is incomplete if the system cannot say who may read which memory, which tenant or account owns it, and what provenance trail proves the operation happened." Cites SAGE (RBAC), OpenViking (account/user/agent scope in URIs), Hindsight (tenancy extensions, audit logging). Also has a "Team And Multi-Agent Topology" section distinguishing private notebooks, shared team knowledge, and promotion paths (WUPHF, cq).
- `kb/notes/agent-memory-requirements/serve-multiple-consumers.md` — covers multiple memory surfaces for different consumers, not privacy/access per se.

No note anywhere addresses "collective privacy" in the survey's specific sense: protecting a *group or population* from aggregate profiling/surveillance harms arising from cross-system data aggregation. The existing coverage is about artifact/memory-record authority (who may read/write a given memory record, tenant boundaries, audit trails) — a governance-of-artifacts question. The survey's concept is about a different kind of harm: statistical/inferential privacy loss to groups of people from aggregated personal data, independent of any single record's access control.

So the gap is real, but it sits one conceptual layer away from what the KB already has an opinion on.

## Scope argument

**For in-scope**: Commonplace's KB methodology explicitly covers memory-system design requirements (`agent-memory-requirements/`), and multi-agent/multi-tenant memory topology is already treated as a legitimate design axis (`make-authority-explicit.md`). If Commonplace-built KBs become genuinely multi-user or multi-agent-shared, "who can see what" is a real design question the KB should have an opinion on — arguably collective privacy is just a more specific instance of authority/access-control that could deserve its own requirements note.

**Against in-scope**: AGENTS.md's Scope section defines in-scope work as "Agent-operated knowledge base methodology: how to structure, write, connect, validate, review, and maintain knowledge artifacts for consumption by LLM agents," and explicitly excludes "General software engineering, learning theory, or cognitive science unless it directly informs KB design decisions." Collective privacy as the survey frames it is a data-protection/policy concept about *personal user data* aggregated across many people for profiling and surveillance — a data-privacy-law/ethics topic, not an artifact-governance topic. It is not about how to structure, write, link, or validate a knowledge artifact; it is about protecting third-party individuals whose personal information gets aggregated by AI memory systems. Commonplace's own KB is not a repository of personal/conversational user data about many individuals — it is a KB of design methodology notes. The already-existing `make-authority-explicit.md` coverage (who may read/write a memory record, tenancy, audit) is the correctly-scoped translation of "shared memory access" into KB-methodology terms; it stops at record-level authority and does not need to reach into aggregate-profiling/surveillance privacy theory to do its job. Extending into "collective privacy" as a distinct concept would import a policy/ethics framework that doesn't change how anyone builds or operates a KB — it fails the quality bar ("A design insight is worth a note when it changes how someone would build or operate a KB").

The topic is also, independently, speculative: it is one paragraph in a survey's aspirational future-directions section, explicitly called out by the ingest as not evidence of a tractable direction, and the ingest itself already tagged this as the lowest-priority `[deep-dive]` extraction, contingent on a scope decision that had not yet been made — i.e., the ingest correctly deferred rather than asserted this was actionable.

## Verdict

**SOURCE-ONLY-NO-NOTE**

Reasons:

1. The source and ingest already fully capture this content; nothing further needs to be preserved from the survey.
2. The KB-methodology-relevant version of "who can see a shared memory record" is already covered by `make-authority-explicit.md`'s "Access Control, Tenancy, And Audit" section (record-level authority, tenancy, audit trail) — that is the correct scope boundary.
3. "Collective privacy" specifically (protecting groups from aggregate profiling/surveillance harms from cross-system personal-data aggregation) is a data-privacy/policy topic about personal user data, not an artifact-governance or KB-structuring topic. It falls under AGENTS.md's exclusion of general topics "unless it directly informs KB design decisions," and it does not currently inform any KB design decision Commonplace needs to make.
4. The topic is speculative/aspirational in the source itself (one paragraph, no mechanism, explicitly future-facing), which independently argues against promoting it to a durable claim-shaped note now.

No KB note was written. `kb/work/connect-maintenance-observations/README.md` and `kb/work/monthly-improvement-triage/README.md` are left untouched per instructions — the coordinating session should mark this row closed with this investigation as the resolution (dismissed as out of scope).
