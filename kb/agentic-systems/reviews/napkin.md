---
type: types/note.md
description: "Napkin's executable local memory access, host-driven distillation, and the limits of its benchmark and context claims"
generated-by: analyse-agentic-system
analysis-run: AAS-2026-09-27-napkin-05
source-identity: https://github.com/Michaelliv/napkin
reviewed-revision: "7582d6a46f5a11995956e60a59c41a5b242109f1"
analysis-result: kb/reports/retained/agentic-system-analysis/AAS-2026-09-27-napkin-05/result.md
analysis-result-sha256: 548c7be0916b0d9985a139877b699736e3ac2f699a2ceb291e7e1792d525e1b0
---

# Napkin: local memory with host-owned learning

Evidence basis: pinned TypeScript, bundled instructions and attributed benchmark reports at commit `7582d6a46f5a11995956e60a59c41a5b242109f1`, inspected on 2026-09-27. No Napkin execution was performed.

Napkin is a local memory tool with a CLI and SDK. It retains files, returns progressively more content on request, and supplies skills for an external agent to extract and maintain knowledge. The enclosing agent owns the sequence of requests and whether recalled material affects its next decision. The core returns data rather than running that agent loop. [Entry and SDK](https://github.com/Michaelliv/napkin/blob/7582d6a46f5a11995956e60a59c41a5b242109f1/src/sdk.ts)

## Storage, retrieval and control

An ordinary caller requests an overview, searches a topic, then reads a selected note. Search combines a lexical-engine score with logarithmic backlink count and normalized recency. It caps result count; read returns the full file. Overview depth and keyword options are not a whole-context token budget. Its keyword validation also has a fallback when no candidate passes the search probe. Thus progressive disclosure is an available calling pattern, not an enforced sequence or token limit. See the exact result's OBJ-3 and RTE-1. [Search](https://github.com/Michaelliv/napkin/blob/7582d6a46f5a11995956e60a59c41a5b242109f1/src/core/search.ts), [overview](https://github.com/Michaelliv/napkin/blob/7582d6a46f5a11995956e60a59c41a5b242109f1/src/core/overview.ts)

Notes, daily records, project context, canvas data, bookmarks and Base definitions persist in files. Base queries additionally compile note metadata into temporary in-memory SQLite tables and close them after the query; SQLite is an access structure, not the durable vault. Derived caches use paths and modification times, so they do not assure content identity after edits that preserve those values. [Base query](https://github.com/Michaelliv/napkin/blob/7582d6a46f5a11995956e60a59c41a5b242109f1/src/core/bases.ts), [fingerprint](https://github.com/Michaelliv/napkin/blob/7582d6a46f5a11995956e60a59c41a5b242109f1/src/utils/fingerprint.ts)

Mutation checks govern operation shape: create rejects collisions unless overwrite is requested; ordinary deletion moves notes to excluded `.trash`, while permanent deletion removes them. Injected SDK configuration is copied/frozen, and its setter refuses disk-based changes. These checks do not evaluate note truth or control an external editor. Package update separately delegates installation of the registry's latest release to npm. [Mutation](https://github.com/Michaelliv/napkin/blob/7582d6a46f5a11995956e60a59c41a5b242109f1/src/core/crud.ts), [configuration](https://github.com/Michaelliv/napkin/blob/7582d6a46f5a11995956e60a59c41a5b242109f1/src/core/config.ts), [update](https://github.com/Michaelliv/napkin/blob/7582d6a46f5a11995956e60a59c41a5b242109f1/src/commands/update.ts)

## Retained learning and warrant

The strongest supported learning contribution is the bundled distill workflow: session material becomes declarative notes, reasons and procedures for future project work. It searches before creating, integrates into existing notes, exposes contradictions and marks new generalizations:

> - **Mark synthesis.** A claim the session actually established needs no marker.
>   A generalization you are drawing gets a trailing `^[inferred]`.
> --- `skills/distill/SKILL.md:111-112` @ `7582d6a46f5a11995956e60a59c41a5b242109f1`

This establishes an afforded trace-learning route, not a wired or observed autonomous distiller. Tending likewise instructs a host to merge duplicates and repair structure, reserving template changes for a user. Link verification checks target resolution, not factual correctness. The theory-builder conditions have conditional, afforded support along the distill route; improved future capacity, reflection and full autonomous theory building remain uninspected. Retention alone does not establish acceptance or post-acceptance integration. [Distill](https://github.com/Michaelliv/napkin/blob/7582d6a46f5a11995956e60a59c41a5b242109f1/skills/distill/SKILL.md), [tend](https://github.com/Michaelliv/napkin/blob/7582d6a46f5a11995956e60a59c41a5b242109f1/skills/tend/SKILL.md)

Requested retrieval is wired pull. The documented every-session pinned `NAPKIN.md` convention supports afforded coarse push, with the actual host selector excluded. Design prose about a distill command and access-driven promotion is not implemented in the current core paths searched. The documented timer lives in an external pi extension. [Design](https://github.com/Michaelliv/napkin/blob/7582d6a46f5a11995956e60a59c41a5b242109f1/docs/agent-memory-progressive-disclosure.md), [external distillation](https://github.com/Michaelliv/napkin/blob/7582d6a46f5a11995956e60a59c41a5b242109f1/docs/distill.md)

## Evidence limits

The LongMemEval wrapper imports conversation rounds, invokes `pi`, and scores answers against dataset references. Normalized string matches can bypass its model judge; judge failure can fall back to token F1. Its required context extension is missing from the pinned tree. Reported benchmark scores therefore remain attributed bundle results, with no inspected retained evidence establishing recalled-content dependence or Napkin's causal contribution. Exact model weights, deployed permissions and host activation are also outside this boundary. [Benchmark implementation](https://github.com/Michaelliv/napkin/blob/7582d6a46f5a11995956e60a59c41a5b242109f1/bench/longmemeval-eval.ts)

The retained exact result named in frontmatter contains the complete route records, reconciled memory profile and limitations. Candidate-linked executions and an appropriate intervention/comparison would be needed to strengthen the learning and causal conclusions.
