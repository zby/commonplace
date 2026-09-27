---
type: types/note.md
description: "Napkin's file-based agent memory, progressive retrieval and host-executed curation, with source-bounded limits on learning and benchmark claims."
generated-by: analyse-agentic-system
analysis-run: AAS-2026-09-27-napkin-04
source-identity: https://github.com/Michaelliv/napkin
reviewed-revision: "7582d6a46f5a11995956e60a59c41a5b242109f1"
analysis-result: kb/reports/retained/agentic-system-analysis/AAS-2026-09-27-napkin-04/result.md
analysis-result-sha256: "db2d565c46c319a1ecce235c0e12b167acc646d2567848f0170be7769a73360b"
---

# Napkin

Evidence basis: TypeScript implementation, shipped skills and attributed benchmark documentation at commit `7582d6a46f5a11995956e60a59c41a5b242109f1`, inspected on 2026-09-27. No runtime or causal experiment was performed.

Napkin is a local file-based memory surface for an external agent. Its CLI and SDK discover a vault, return overview/search/read results, and mutate retained content. The calling agent owns planning, model calls and the decision to use retrieved material. The shipped distill and tend skills add instructions for producing and maintaining knowledge; their execution depends on a host loading and following them. The separate Pi integration is outside this source boundary. See the [entry-point account](https://github.com/Michaelliv/napkin/blob/7582d6a46f5a11995956e60a59c41a5b242109f1/README.md) and the [exact analysis](../../reports/retained/agentic-system-analysis/AAS-2026-09-27-napkin-04/result.md).

## Runtime and memory

A requested overview includes NAPKIN.md and a folder map; search returns lexical results ranked with backlink and relative modification-time terms; a requested read returns the complete note. These package handlers are implemented. Agent-level read-back is an afforded pull route, not evidence of deployed automatic injection. The “always-loaded” context description means inclusion in requested overview inside this boundary. Neither NAPKIN.md nor full reads have an enforced token budget. Records RTE-1, OBJ-2 and OBJ-3 in the exact analysis retain the evidence.

The map probes candidate keywords against the same retrieval engine, but it can retain a fallback handle when none passes. Its “search-validated” description therefore does not guarantee that every handle retrieves the intended note. Search and overview caches use path/mtime fingerprints; edits preserving timestamps fall outside that freshness check. These are access structures, not semantic acceptance checks. [Search implementation](https://github.com/Michaelliv/napkin/blob/7582d6a46f5a11995956e60a59c41a5b242109f1/src/core/search.ts), [overview implementation](https://github.com/Michaelliv/napkin/blob/7582d6a46f5a11995956e60a59c41a5b242109f1/src/core/overview.ts).

Durable content includes Markdown notes, context, editable templates/folder descriptions, JSON canvases/bookmarks and YAML Bases. Bases derive a transient SQLite query table; this does not make SQLite a second durable store. Files contain prose and machine-interpreted fields/selectors. Requested auxiliary views extend the memory surface beyond Markdown search. The exact analysis integrates these alternatives into one comparison scope (OBJ-1, OBJ-7, OBJ-8, OBJ-9, OBJ-10 and RTE-10).

## Writing and revision

Distill asks a host agent to extract future-useful decisions, fixes and procedures from a working conversation, search before writing, merge related notes, retain reasons, expose contradictions and mark new generalizations as inferred. It affords trace-fed learning in the comparison vocabulary: permanent behavior-shaping notes can be read in later project tasks. This does not establish improved capacity attributable to criticism. Its invocation, semantic judgments and later adoption are not wired by the package. [Distill skill](https://github.com/Michaelliv/napkin/blob/7582d6a46f5a11995956e60a59c41a5b242109f1/skills/distill/SKILL.md).

Tend directs a host agent to select a few obvious link, tag, orphan or duplicate issues, skip uncertain changes, and propose template changes to the user. Executable file operations support the changes; the semantic safeguards remain policies. Default deletion moves a file to excluded trash, but overwrite does not preserve a prior version and exact paths can still reach trashed files. Regular note creation refuses collisions without overwrite; the separate Bases item writer bypasses that guard. [Tend skill](https://github.com/Michaelliv/napkin/blob/7582d6a46f5a11995956e60a59c41a5b242109f1/skills/tend/SKILL.md), [CRUD](https://github.com/Michaelliv/napkin/blob/7582d6a46f5a11995956e60a59c41a5b242109f1/src/core/crud.ts), [Bases operations](https://github.com/Michaelliv/napkin/blob/7582d6a46f5a11995956e60a59c41a5b242109f1/src/core/bases.ts).

Configuration can be supplied as a frozen SDK override, which rejects disk config-set operations for that instance. A separate update command installs npm's latest package. Neither admission path establishes evidence-based successor improvement. The file namespace is not a demonstrated isolation boundary; deployed host permissions and concurrency guarantees remain uninspected. See RTE-5 and RTE-6 in the exact analysis.

## What the evidence establishes

The strongest supported contribution is callable storage and selective access, with explicit curation instructions. Localized theory-like note content, content-sensitive use and contradiction-aware revision are afforded. An actual cycle in which formulated criticism shapes later work remains uninspected. Reflection is afforded for a complying host using vault diagnostics to revise the same vault; reflective criticism of Napkin's method and an autonomous theory builder are not established. A maintenance pathway is afforded, but actual self-improvement and learning need linked before/after and later-use evidence.

The documented 92%/91%/83% LongMemEval results concern Pi plus Napkin on Oracle/S/M. The harness imports raw conversation rounds, calls an external model, and scores answers against dataset references using shortcuts, a model judge or fallback token scoring. Those reports do not demonstrate distill/tend learning, dependence on recalled content, or a causal contribution of an individual component. The expected context extension is outside the pinned tree. [Benchmark report](https://github.com/Michaelliv/napkin/blob/7582d6a46f5a11995956e60a59c41a5b242109f1/bench/README.md), [evaluation implementation](https://github.com/Michaelliv/napkin/blob/7582d6a46f5a11995956e60a59c41a5b242109f1/bench/longmemeval-eval.ts).

## Scope

This assessment covers the current package, shipped skills and selected evaluation machinery. Host/plugin and provider internals, deployed operation and complete convenience-API correctness are excluded. A pinned host integration would clarify automatic delivery and permissions. Candidate-linked session-to-note-to-later-action traces and controlled capacity comparisons would clarify whether the afforded revision path learns.

---

- [Exact analysis and memory comparison](../../reports/retained/agentic-system-analysis/AAS-2026-09-27-napkin-04/result.md) — see-also: canonical records, source quotations, specialist integration and evidence limits
- [Theory builder](../../notes/definitions/theory-builder.md) — defined-in: separates localized content, consumption, criticism and iteration from learning
- [Reflective system](../../notes/definitions/reflective-system.md) — defined-in: the bounded self-representation and operation mapping
- [Self-improving system](../../notes/definitions/self-improving-system.md) — defined-in: distinguishes a standing pathway from exercised evidence-responsive self-change
