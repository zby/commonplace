---
description: "hyalo review: Rust CLI for structured Markdown vault search, mutation, linting, snapshot indexes, and Claude skill/rule integration"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
last-checked: "2026-06-04"
---

# hyalo

hyalo, from `ractive/hyalo`, is a Rust CLI for operating Markdown knowledgebases with YAML frontmatter. At the reviewed commit it turns a user-owned vault into a structured agent tool surface: agents can search by text, metadata, tags, links, headings, and tasks; mutate frontmatter, tags, task state, file locations, and links; lint schema and Markdown rules; maintain a snapshot index; and install Claude Code skills/rules that tell the host agent to prefer hyalo over raw file tools.

**Repository:** https://github.com/ractive/hyalo

**Reviewed commit:** [0ffb301484a41c434a50fd2ef58870676983b6ea](https://github.com/ractive/hyalo/commit/0ffb301484a41c434a50fd2ef58870676983b6ea)

**Source directory:** `related-systems/ractive--hyalo`

## Core Ideas

**The retained memory is the vault, not a service store.** hyalo operates on existing `.md` files with YAML frontmatter, tags, wikilinks, Markdown links, headings, and task checkboxes; `.hyalo.toml` declares the vault directory, schemas, saved views, lint rules, output preferences, and link options ([README.md](https://github.com/ractive/hyalo/blob/0ffb301484a41c434a50fd2ef58870676983b6ea/README.md), [.hyalo.toml](https://github.com/ractive/hyalo/blob/0ffb301484a41c434a50fd2ef58870676983b6ea/.hyalo.toml), [crates/hyalo-cli/src/cli/args.rs](https://github.com/ractive/hyalo/blob/0ffb301484a41c434a50fd2ef58870676983b6ea/crates/hyalo-cli/src/cli/args.rs)). This gives strong adoption affordances: the same files remain readable and editable outside hyalo.

**The agent interface is a deterministic CLI with structured envelopes.** Commands return successful JSON through a `{"results": ..., "total": ..., "hints": [...]}` envelope, errors through structured `error`/`path`/`hint`/`cause` fields when possible, and `--jq` operates over the full envelope ([crates/hyalo-cli/src/output.rs](https://github.com/ractive/hyalo/blob/0ffb301484a41c434a50fd2ef58870676983b6ea/crates/hyalo-cli/src/output.rs), [crates/hyalo-cli/src/cli/args.rs](https://github.com/ractive/hyalo/blob/0ffb301484a41c434a50fd2ef58870676983b6ea/crates/hyalo-cli/src/cli/args.rs), [crates/hyalo-cli/tests/e2e/errors.rs](https://github.com/ractive/hyalo/blob/0ffb301484a41c434a50fd2ef58870676983b6ea/crates/hyalo-cli/tests/e2e/errors.rs)). That makes hyalo closer to a typed shell API over a KB than to an opaque memory service.

**Context efficiency is scoped retrieval plus compact drill-down, not model summarization.** `find` can combine BM25 or regex text search with property, tag, title, section, task, broken-link, orphan, dead-end, sort, limit, and field-selection controls; the default fields include metadata, tags, sections, and links while tasks, typed properties, backlinks, and title are opt-in ([crates/hyalo-cli/src/cli/args.rs](https://github.com/ractive/hyalo/blob/0ffb301484a41c434a50fd2ef58870676983b6ea/crates/hyalo-cli/src/cli/args.rs), [crates/hyalo-core/src/filter/fields.rs](https://github.com/ractive/hyalo/blob/0ffb301484a41c434a50fd2ef58870676983b6ea/crates/hyalo-core/src/filter/fields.rs), [crates/hyalo-core/src/bm25.rs](https://github.com/ractive/hyalo/blob/0ffb301484a41c434a50fd2ef58870676983b6ea/crates/hyalo-core/src/bm25.rs)). The system bounds volume by explicit filters and limits, but complexity control still depends on the acting agent choosing good queries.

**The snapshot index is an access structure over the file store.** `create-index` scans the vault into MessagePack-serialized entries, link graph data, and optional BM25 index state; read-only commands can use that snapshot, and write commands patch entries after mutations so a long agent session does not keep consulting stale metadata ([crates/hyalo-core/src/index.rs](https://github.com/ractive/hyalo/blob/0ffb301484a41c434a50fd2ef58870676983b6ea/crates/hyalo-core/src/index.rs), [crates/hyalo-cli/src/commands/create_index.rs](https://github.com/ractive/hyalo/blob/0ffb301484a41c434a50fd2ef58870676983b6ea/crates/hyalo-cli/src/commands/create_index.rs), [crates/hyalo-cli/src/commands/mutation.rs](https://github.com/ractive/hyalo/blob/0ffb301484a41c434a50fd2ef58870676983b6ea/crates/hyalo-cli/src/commands/mutation.rs)). The index is not canonical memory; its value is fast, repeatable pull retrieval.

**Mutations preserve structure and surface errors early.** `mv` plans link rewrites, handles single and batch moves, updates self-links and relative links, rolls back on failure, and patches the snapshot index after successful moves; e2e tests cover representative link forms, topologies, move kinds, and post-move link health ([crates/hyalo-cli/src/commands/mv.rs](https://github.com/ractive/hyalo/blob/0ffb301484a41c434a50fd2ef58870676983b6ea/crates/hyalo-cli/src/commands/mv.rs), [crates/hyalo-cli/tests/e2e/mv_link_forms.rs](https://github.com/ractive/hyalo/blob/0ffb301484a41c434a50fd2ef58870676983b6ea/crates/hyalo-cli/tests/e2e/mv_link_forms.rs)). Frontmatter parsing rejects duplicate keys and parser bombs, write paths enforce a shared size budget, and malformed frontmatter is skipped with warnings rather than silently corrupting reads ([crates/hyalo-core/src/frontmatter/parse.rs](https://github.com/ractive/hyalo/blob/0ffb301484a41c434a50fd2ef58870676983b6ea/crates/hyalo-core/src/frontmatter/parse.rs), [crates/hyalo-core/src/frontmatter/mod.rs](https://github.com/ractive/hyalo/blob/0ffb301484a41c434a50fd2ef58870676983b6ea/crates/hyalo-core/src/frontmatter/mod.rs), [crates/hyalo-cli/src/output.rs](https://github.com/ractive/hyalo/blob/0ffb301484a41c434a50fd2ef58870676983b6ea/crates/hyalo-cli/src/output.rs)).

**Claude integration is generated instruction, not a hidden runtime.** `hyalo init --claude` installs generated skill and rule Markdown that tells Claude Code when and how to use hyalo; the `hyalo-tidy` skill prescribes a five-phase maintenance workflow using summary, snapshot indexes, git history, optional Claude memory inspection, lint, link repair, status updates, moves, and tag normalization ([README.md](https://github.com/ractive/hyalo/blob/0ffb301484a41c434a50fd2ef58870676983b6ea/README.md), [crates/hyalo-cli/templates/skill-hyalo.md](https://github.com/ractive/hyalo/blob/0ffb301484a41c434a50fd2ef58870676983b6ea/crates/hyalo-cli/templates/skill-hyalo.md), [crates/hyalo-cli/templates/skill-hyalo-tidy.md](https://github.com/ractive/hyalo/blob/0ffb301484a41c434a50fd2ef58870676983b6ea/crates/hyalo-cli/templates/skill-hyalo-tidy.md), [crates/hyalo-cli/templates/rule-knowledgebase.md](https://github.com/ractive/hyalo/blob/0ffb301484a41c434a50fd2ef58870676983b6ea/crates/hyalo-cli/templates/rule-knowledgebase.md)).

## Artifact analysis

- **Storage substrate:** `files` — The central retained artifacts are Markdown vault files, `.hyalo.toml`, generated Claude Markdown artifacts, and the optional `.hyalo-index` file; runtime Rust data structures and stdout envelopes are consumption surfaces over those files.
- **Representational form:** `prose` `symbolic` — Vault bodies, dogfood reports, skills, rules, and tidy reports are prose; YAML/TOML frontmatter, tags, task checkboxes, link graphs, schemas, saved views, lint rules, command flags, JSON envelopes, error objects, and snapshot/BM25 indexes are symbolic.
- **Lineage:** `authored` `imported` — Humans and agents author or import Markdown vault content; hyalo scans that content into derived metadata/index views and generated instruction files. I found dogfood reports and tidy instructions that inspect session-adjacent material, but no implemented Rust path that derives durable memory from raw session/tool traces.
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` — Notes and reports serve as knowledge; generated Claude skills/rules instruct tool choice; path, budget, parser, and mutation guards enforce structural constraints; links, tags, properties, saved views, hints, and file-input resolvers route access; lint/schema checks validate; BM25 and sort rules rank returned results.

**Markdown vault files.** A vault file bundles prose body content with symbolic frontmatter, tags, tasks, links, headings, and optional type fields. hyalo reads those parts as knowledge when returning file content, and as routing/validation/ranking handles when filtering, linting, moving, or building indexes.

**`.hyalo.toml` configuration.** The TOML file is a system-definition artifact: it scopes the vault, sets output and hint behavior, configures link handling, declares schemas and saved views, and controls lint rules ([.hyalo.toml](https://github.com/ractive/hyalo/blob/0ffb301484a41c434a50fd2ef58870676983b6ea/.hyalo.toml), [crates/hyalo-cli/src/config.rs](https://github.com/ractive/hyalo/blob/0ffb301484a41c434a50fd2ef58870676983b6ea/crates/hyalo-cli/src/config.rs)).

**Snapshot index.** `.hyalo-index` is a derived symbolic access structure with per-file properties, tags, sections, tasks, outbound links, a link graph, and optional persisted BM25 state. It can be patched after `set`, `remove`, `append`, `new`, `task`, `lint --fix`, and `mv`, but its authority is subordinate to the file store and can be rebuilt ([crates/hyalo-core/src/index.rs](https://github.com/ractive/hyalo/blob/0ffb301484a41c434a50fd2ef58870676983b6ea/crates/hyalo-core/src/index.rs), [crates/hyalo-cli/src/dispatch.rs](https://github.com/ractive/hyalo/blob/0ffb301484a41c434a50fd2ef58870676983b6ea/crates/hyalo-cli/src/dispatch.rs)).

**Command outputs and hints.** JSON/text envelopes and hints are transient behavior-shaping artifacts. They do not persist as memory, but they materially guide the next agent action by making totals, narrowed results, errors, and suggested follow-up commands machine-readable ([crates/hyalo-cli/src/hints.rs](https://github.com/ractive/hyalo/blob/0ffb301484a41c434a50fd2ef58870676983b6ea/crates/hyalo-cli/src/hints.rs), [crates/hyalo-cli/src/output.rs](https://github.com/ractive/hyalo/blob/0ffb301484a41c434a50fd2ef58870676983b6ea/crates/hyalo-cli/src/output.rs)).

**Generated Claude artifacts.** The generated `hyalo` skill, `hyalo-tidy` skill, and path-scoped rule are prose instructions with system-definition authority inside Claude Code. Their activation and obedience are host-agent behavior, but hyalo owns the templates and install/deinstall path ([crates/hyalo-cli/src/commands/init.rs](https://github.com/ractive/hyalo/blob/0ffb301484a41c434a50fd2ef58870676983b6ea/crates/hyalo-cli/src/commands/init.rs), [crates/hyalo-cli/templates/skill-hyalo.md](https://github.com/ractive/hyalo/blob/0ffb301484a41c434a50fd2ef58870676983b6ea/crates/hyalo-cli/templates/skill-hyalo.md)).

**Dogfood knowledgebase.** `hyalo-knowledgebase/` is authored project memory: iteration plans, completed iteration notes, research, decision logs, and dogfood reports. It is valuable evidence for the product's intended agent workflow, but in the inspected implementation it is not produced by an automatic trace-learning loop ([CLAUDE.md](https://github.com/ractive/hyalo/blob/0ffb301484a41c434a50fd2ef58870676983b6ea/CLAUDE.md), [hyalo-knowledgebase/decision-log.md](https://github.com/ractive/hyalo/blob/0ffb301484a41c434a50fd2ef58870676983b6ea/hyalo-knowledgebase/decision-log.md), [hyalo-knowledgebase/iterations/iteration-154-mv-index-patch.md](https://github.com/ractive/hyalo/blob/0ffb301484a41c434a50fd2ef58870676983b6ea/hyalo-knowledgebase/iterations/iteration-154-mv-index-patch.md)).

The promotion path is symbolic: prose files can gain stronger operational authority when frontmatter, tags, schemas, saved views, lint rules, links, generated rules, or command hints make them selectable, checkable, or actionable. hyalo supplies the machinery; humans or instructed agents decide what content deserves that promotion.

## Comparison with Our System

| Dimension | hyalo | Commonplace |
|---|---|---|
| Primary purpose | Operate arbitrary Markdown/frontmatter vaults from a CLI | Maintain a typed methodology KB and framework for agent-operated knowledge bases |
| Main substrate | User filesystem plus `.hyalo.toml` and optional `.hyalo-index` | Git-tracked KB collections, type specs, instructions, generated indexes, validation reports |
| Retrieval | Explicit commands: BM25, regex, metadata filters, links, headings, tasks, saved views | `rg`, indexes, links, reports, skills, collection/type contracts |
| Mutation | CLI-managed frontmatter, tag, task, link, file, lint-fix, and scaffold operations | File edits plus Commonplace commands for validation, indexes, reviews, snapshots, and note operations |
| Governance | TOML schemas, lint rules, path boundaries, budget checks, dry-runs, generated Claude guidance | Collection contracts, schemas, deterministic validation, semantic review, review gates, replacement workflow |

hyalo is one of the closest external cousins to Commonplace because both systems make ordinary files operational for agents. The difference is register and ownership. hyalo is a general tool layer for many vault shapes; Commonplace is a specific methodology KB whose collection contracts and type specs are themselves part of the knowledge architecture.

The strongest hyalo pattern is tool-mediated predictability. It gives agents narrow commands, shaped output, hints, dry-runs, and structural validation without requiring embeddings, a server, or an LLM judge. Commonplace has deeper content governance, but hyalo has a more polished shell API for agent navigation and mutation.

### Borrowable Ideas

**Consistent success and error envelopes.** Commonplace commands could expose a uniform `results`/`total`/`hints` shape and structured error fields. Ready for command surfaces that agents already parse.

**Snapshot query index with mutation patching.** Commonplace generated indexes are durable navigation artifacts; hyalo's session-oriented snapshot is a separate acceleration layer. Worth borrowing when repeated review/query loops become expensive, provided the index remains subordinate to source files.

**Schema scaffold followed by lint feedback.** `hyalo new` intentionally creates a skeleton that lint can guide the agent to fill. Commonplace could use the same loop for type-specific drafts, with semantic placeholders made explicit.

**Move operations that rewrite links and update access structures.** Commonplace already has relocation commands, but hyalo is a useful implementation reference for link-form preservation, ambiguity handling, dry-run output, rollback, and index patching.

**Generated host-agent instructions.** `hyalo init --claude` makes the tool teach the host agent how to use it. Commonplace could refresh local agent-facing rules from current collection/type contracts, while keeping them clearly generated.

**Do not borrow automatic semantic claims.** hyalo deliberately avoids automatic memory synthesis. For Commonplace, that restraint is a reminder to keep generated access structures and hints distinct from reviewed claims.

## Write side

**Write agency:** `manual` — hyalo changes retained artifacts only through explicit user or agent commands such as `init`, `set`, `remove`, `append`, `new`, `task`, `mv`, `links fix`, `links auto`, `tags rename`, `properties rename`, `views`, `types`, `lint --fix`, and Claude-template generation. The implementation performs structural work inside those commands, including atomic frontmatter rewrites, path validation, link rewrites, lint autofixes, and snapshot-index patching, but I found no autonomous curation operation over already stored memory.

Because write agency is manual-only under the current review taxonomy, there is no curation-operation lead line. Index rebuilds and index patching are access-structure upkeep; link repair, tag rename, file moves, and lint fixes are command-invoked structural maintenance rather than automatic `consolidate`, `dedup`, `evolve`, `synthesize`, `invalidate`, `decay`, or `promote` over memory content.

## Read-back

**Read-back:** `pull` — Retained vault content reaches an agent when the agent or user explicitly invokes hyalo commands such as `find`, `read`, `summary`, `backlinks`, `links`, `tags`, `properties`, or saved-view queries. Generated Claude skills and rules instruct the host agent to use those commands, but the retained vault content itself still enters context through deliberate lookup.

Selection is lexical, structural, and statistical. BM25 ranks full-text matches; regex handles literal body/title/property matching; property filters, tags, sections, tasks, links, backlinks, saved views, file lists, and limits bound result scope. Snapshot indexes accelerate the same pull path and can make repeated lookups cheaper, but they do not decide semantic relevance beyond the configured query mechanics.

Effective precision, recall, context dilution, and whether a host agent obeys the returned memory are not verified from code. The source includes extensive e2e and unit tests for command behavior, parsing, mutation safety, link forms, linting, envelopes, and index behavior, but I did not find with/without-memory ablations or post-answer audits of agent faithfulness.

## Curiosity Pass

**The "LLM Wiki" framing is operationally accurate but not cognitive.** hyalo makes an LLM-maintained wiki practical by giving agents reliable commands, but it does not decide what should be remembered or derive new claims from traces.

**The latest changes make the CLI more matrix-friendly for agents.** Error envelopes, frontmatter budgets, unified input counters, snapshot patching, and help examples are not glamorous, but they reduce the number of ambiguous shell states an agent must interpret.

**The dogfood KB is evidence, not implementation magic.** The repository uses its own knowledgebase heavily, including reports that drive iterations. That proves adoption pressure and design feedback, not automatic learning.

**Hints are a behavior-shaping API.** They are not memory, but they turn command results into suggested next commands. For an agent, this can matter as much as retrieval ranking.

**Schema authority remains local and configurable.** hyalo can enforce shape where a vault declares schemas, but it intentionally does not impose a universal ontology over notes. That flexibility is why it fits many vaults and why Commonplace still needs collection contracts.

## What to Watch

- Whether `hyalo-tidy` becomes a Rust subcommand or scheduled workflow that writes durable summaries from git/session/Claude-memory signals; that would reopen the trace-learning decision.
- Whether generated Claude integration grows event hooks or automatic context assembly rather than static skills/rules and explicit command use; that would change the read-back verdict.
- Whether `.hyalo-index` grows stronger provenance, invalidation, or locking guarantees; that would make it more directly borrowable as a Commonplace query cache.
- Whether schemas add cross-file constraints or body-section semantics beyond current lint checks; that would move hyalo closer to Commonplace's collection/type contract model.
- Whether vector or LLM-judged retrieval appears; that would add parametric or judgment-based ranking to the current symbolic/BM25 retrieval surface.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes hyalo's stored/indexed vault from explicit command lookup.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - grounds the split between Markdown files, TOML config, generated instructions, command envelopes, and snapshot indexes.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies vault notes, dogfood reports, command results, and lint reports as advisory remembered context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies schemas, lint rules, saved views, command implementations, generated Claude skills/rules, and snapshot indexes as behavior-shaping control surfaces.
- [Symbolic context engineering is bounded by symbol availability](../../notes/symbolic-context-engineering-is-bounded-by-symbol-availability.md) - explains why hyalo's frontmatter, tags, links, saved views, and file paths are the handles that make retrieval precise.
