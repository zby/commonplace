---
type: types/note.md
description: "Napkin's file memory, requested disclosure, native access structures and optional agent distillation at a pinned package boundary."
generated-by: analyse-agentic-system
analysis-run: AAS-2026-09-26-napkin-03
source-identity: https://github.com/Michaelliv/napkin
reviewed-revision: "7582d6a46f5a11995956e60a59c41a5b242109f1"
analysis-result: kb/reports/retained/agentic-system-analysis/AAS-2026-09-26-napkin-03/result.md
analysis-result-sha256: "1c4b625211fa033130d7ea2533c214f5e5e791d07707ad96ec8aa34f9e835c53"
---

# Napkin

Evidence basis: pinned source code, shipped skills/design text and separately labelled benchmark reports, inspected on 2026-09-26 at `7582d6a46f5a11995956e60a59c41a5b242109f1`.

Napkin is a local file knowledge system whose CLI and SDK return memory to a requesting human or agent. The package owns file operations and access construction; the consuming host owns model calls, context admission and subsequent action. Its optional distill and tend skills prescribe semantic work without implementing the enclosing agent. This is a complete package analysis with a partial agent loop, not an observation of a deployed host.

## Operation and memory

The ordinary progression is overview, search, then read. CLI wrappers and SDK methods use the same core. Search combines a native lexical score with logarithmic backlinks and relative modification time; a read returns full stored text. An overview includes the mutable NAPKIN.md context note, folder structure and derived search handles. These are requested returns, so the package supports pull read-back. Calling the context note “always loaded” does not establish a local startup injection route. [Pinned search implementation](https://github.com/Michaelliv/napkin/blob/7582d6a46f5a11995956e60a59c41a5b242109f1/src/core/search.ts), [overview implementation](https://github.com/Michaelliv/napkin/blob/7582d6a46f5a11995956e60a59c41a5b242109f1/src/core/overview.ts).

Memory comprises Markdown/frontmatter, context text, JSON access caches and edited auxiliary files. Canvas relations and bookmarks are file-backed; Base views compile retained definitions and vault metadata into transient in-memory SQLite, query it and close it. Thus the full access boundary includes files, in-memory structures and SQLite, rather than treating the main note format as the entire storage inventory. Access metadata and definitions exercise ranking and routing authority; returned prose is advisory knowledge. [Base implementation](https://github.com/Michaelliv/napkin/blob/7582d6a46f5a11995956e60a59c41a5b242109f1/src/utils/bases.ts).

Direct content editing and automatic cache rebuilding are implemented. Existing-file creation rejects unless overwrite is explicit; default deletion moves to .trash, while a permanent branch removes the file. The trash operation is limited recovery, not revision history. Caches use path and modification-time fingerprints, so content changes preserving those values can evade freshness checks. These are static implementation findings, not reproduced failures. [CRUD](https://github.com/Michaelliv/napkin/blob/7582d6a46f5a11995956e60a59c41a5b242109f1/src/core/crud.ts), [fingerprinting](https://github.com/Michaelliv/napkin/blob/7582d6a46f5a11995956e60a59c41a5b242109f1/src/utils/fingerprint.ts).

## Distillation, criticism and authority

The distill skill directs an external agent to retain useful session discoveries, search existing notes, merge or create, preserve reasons and mark new generalizations. Its merge rule makes disagreement visible:

> Integrate — don't append a dated "update" section to the bottom. Fold new
> information into the sections where it belongs. If the new finding contradicts
> the note, say so in the note explicitly rather than silently keeping both.
> --- https://github.com/Michaelliv/napkin/blob/7582d6a46f5a11995956e60a59c41a5b242109f1/skills/distill/SKILL.md

That affords localized explanations, content-sensitive comparison and revision. Files can retain the resulting note and rationale for later reads. Actual criticism, next-round uptake and improved future capacity remain unobserved. The memory profile therefore records trace learning as **afforded**, not wired: session material may become durable prose for later project tasks, during a conversation or at its end. Automatic index compilation independently supports a **wired** automatic-write value; it cannot strengthen semantic extraction.

Tend prescribes small repairs, duplicate merges and retirement, while reserving new template schemas for the user. These instructions supply policy-level trust and work limits; the CLI does not enforce the skill's semantic judgments. Link resolution checks references, not the truth of an explanation. No complete working theory builder, reflective theory builder or autonomous learner is demonstrated by the package. Narrow access-state reflection is implemented through file changes, cache representations and subsequent search behavior; this does not establish criticism of the system's own methods. [Tend skill](https://github.com/Michaelliv/napkin/blob/7582d6a46f5a11995956e60a59c41a5b242109f1/skills/tend/SKILL.md).

## Assessment boundary

The package's useful distinction is between implemented memory access and optional semantic processing. Progressive disclosure reduces selection work, but reported token estimates are not hard total budgets, and overview keyword probing has a fallback that prevents a universal retrieval guarantee. The npm update route installs the publisher's latest artifact; success means installation succeeded, not that the package evaluated an improvement. [Update implementation](https://github.com/Michaelliv/napkin/blob/7582d6a46f5a11995956e60a59c41a5b242109f1/src/commands/update.ts).

Benchmark documents report agent-plus-Napkin retrieval outcomes, and the harness constructs fixtures and scores answers against supplied references. Those aggregate reports do not isolate a memory component's causal effect or establish dependence on recalled content. LongMemEval's lack of learned preprocessing still includes raw-turn partitioning and timestamps; other fixture paths import different material. Faithfulness remains not-determinable from the retained evidence. [Benchmark harness](https://github.com/Michaelliv/napkin/blob/7582d6a46f5a11995956e60a59c41a5b242109f1/bench/longmemeval-eval.ts).

## Scope

External hosts, provider and native-search internals, actual user vaults and deployment runs are excluded. A pinned host trace could establish automatic delivery or skill execution; candidate-linked criticism and later use could establish theory-builder iteration; a controlled recalled-content intervention could test dependence and benefit. No dynamic test was run for this analysis.

The [exact retained result](../../reports/retained/agentic-system-analysis/AAS-2026-09-26-napkin-03/result.md) holds canonical records, per-value comparison evidence, both lenses and the full limitation account.

---

- [Theory builder](../../notes/definitions/theory-builder.md) — defined-in: separates localized content, consumption, criticism and iteration from improved capacity
- [Reflective system](../../notes/definitions/reflective-system.md) — defined-in: bounds reflection to represented aspects and their operative connection
- [Self-improving system](../../notes/definitions/self-improving-system.md) — defined-in: distinguishes evidence-responsive operative change from file retention or installation
