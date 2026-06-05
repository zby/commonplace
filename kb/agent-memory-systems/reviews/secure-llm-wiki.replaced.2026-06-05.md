---
description: "secure-llm-wiki review: git-backed claim wiki with nonce-delimited extraction, trust tiers, adversarial write gates, and coarse query-time read-back"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: []
status: outdated
last-checked: "2026-06-03"
---

# Secure LLM-Wiki

> Replaced 2026-06-05. See [Secure LLM-Wiki](./secure-llm-wiki.md) for the current review.

Secure LLM-Wiki, from `NicoBleh/secure-llm-wiki`, is a Python CLI for building a persistent LLM-maintained claim wiki while treating prompt injection and source poisoning as the central architectural problem. It ingests files, folders, PDFs, or URLs; sanitizes and nonce-delimits source text; asks an extraction model for atomic claims; assigns trust tiers; runs a separate adversarial review model; gates writes; stores accepted/quarantined claims as Markdown with YAML frontmatter in a separate git repo; and loads accepted claims into a nonce-delimited query context.

**Repository:** https://github.com/NicoBleh/secure-llm-wiki

**Reviewed commit:** [dfbc60e37487b61e9a5cbce1271a13576a776d51](https://github.com/NicoBleh/secure-llm-wiki/commit/dfbc60e37487b61e9a5cbce1271a13576a776d51)

**Last checked:** 2026-06-03

## Core Ideas

**It compiles source documents into claim files instead of retrieving raw sources.** The README frames the system as an answer to classic RAG: source documents are processed once into a persistent linked wiki rather than re-scanned and handed to an LLM on every query ([README.md](https://github.com/NicoBleh/secure-llm-wiki/blob/dfbc60e37487b61e9a5cbce1271a13576a776d51/README.md)). The implementation narrows that wiki to `Claim` objects with text, source provenance, trust level, lifecycle status, gate history, supersession, and review notes ([src/secure_wiki/models.py](https://github.com/NicoBleh/secure-llm-wiki/blob/dfbc60e37487b61e9a5cbce1271a13576a776d51/src/secure_wiki/models.py)).

**The security boundary is enforced before, during, and after model calls.** The sanitizer removes zero-width/bidi characters and flags hidden HTML, hidden style, long base64, and broad instruction patterns before source text reaches the extractor ([src/secure_wiki/ingestion/sanitizer.py](https://github.com/NicoBleh/secure-llm-wiki/blob/dfbc60e37487b61e9a5cbce1271a13576a776d51/src/secure_wiki/ingestion/sanitizer.py)). Prompt builders wrap source, proposed claims, existing high-trust claims, and read-back wiki content in fresh nonce-delimited blocks; extraction and review responses must echo the nonce or fail closed ([src/secure_wiki/prompts.py](https://github.com/NicoBleh/secure-llm-wiki/blob/dfbc60e37487b61e9a5cbce1271a13576a776d51/src/secure_wiki/prompts.py), [src/secure_wiki/extraction/extractor.py](https://github.com/NicoBleh/secure-llm-wiki/blob/dfbc60e37487b61e9a5cbce1271a13576a776d51/src/secure_wiki/extraction/extractor.py), [src/secure_wiki/review/adversarial.py](https://github.com/NicoBleh/secure-llm-wiki/blob/dfbc60e37487b61e9a5cbce1271a13576a776d51/src/secure_wiki/review/adversarial.py)).

**The write gate is a deterministic authority boundary around LLM output.** `run_write_gate()` checks sanitizer flags, provenance completeness, trust-tier overwrite rules, adversarial review result, and duplicate/conflict similarity before any claim becomes active. Outcomes are `commit`, `quarantine`, or `escalate`; suspicious or conflicting claims are stored outside the active read path rather than silently discarded ([src/secure_wiki/gate/write_gate.py](https://github.com/NicoBleh/secure-llm-wiki/blob/dfbc60e37487b61e9a5cbce1271a13576a776d51/src/secure_wiki/gate/write_gate.py)).

**Trust is host-pattern policy plus claim metadata, not just prose advice.** Built-in and user YAML rules assign `trusted`, `semi-trusted`, or `untrusted` by host suffix, with tests for query-string and hostname-suffix trust-elevation attempts. The read path hard-filters untrusted claims even when the requested minimum trust is `untrusted` ([src/secure_wiki/trust/tiering.py](https://github.com/NicoBleh/secure-llm-wiki/blob/dfbc60e37487b61e9a5cbce1271a13576a776d51/src/secure_wiki/trust/tiering.py), [tests/test_trust_tiering.py](https://github.com/NicoBleh/secure-llm-wiki/blob/dfbc60e37487b61e9a5cbce1271a13576a776d51/tests/test_trust_tiering.py), [tests/test_read_hygiene.py](https://github.com/NicoBleh/secure-llm-wiki/blob/dfbc60e37487b61e9a5cbce1271a13576a776d51/tests/test_read_hygiene.py)).

**Context efficiency comes from compilation and trust filtering, not retrieval ranking.** Ingestion truncates source text to 8,000 characters for extraction, batch-reviews all claims from a source in one model call, computes embeddings in parallel, and reads only active trusted/semi-trusted claims into query context ([src/secure_wiki/__main__.py](https://github.com/NicoBleh/secure-llm-wiki/blob/dfbc60e37487b61e9a5cbce1271a13576a776d51/src/secure_wiki/__main__.py), [src/secure_wiki/read/hygiene.py](https://github.com/NicoBleh/secure-llm-wiki/blob/dfbc60e37487b61e9a5cbce1271a13576a776d51/src/secure_wiki/read/hygiene.py)). There is no query-time top-k retrieval over claims; a query session receives all claims that pass the coarse trust/status filter.

**The adoption surface is plain CLI plus inspectable files.** `secure-wiki init`, `ingest`, `list`, `context`, `query`, and `clear` operate over a local `wiki_data` repository. Accepted and quarantined claims are Markdown files with YAML frontmatter, while embeddings are colocated JSON cache files and trust rules are YAML ([src/secure_wiki/__main__.py](https://github.com/NicoBleh/secure-llm-wiki/blob/dfbc60e37487b61e9a5cbce1271a13576a776d51/src/secure_wiki/__main__.py), [src/secure_wiki/store/wiki_store.py](https://github.com/NicoBleh/secure-llm-wiki/blob/dfbc60e37487b61e9a5cbce1271a13576a776d51/src/secure_wiki/store/wiki_store.py), [src/secure_wiki/store/embedding_store.py](https://github.com/NicoBleh/secure-llm-wiki/blob/dfbc60e37487b61e9a5cbce1271a13576a776d51/src/secure_wiki/store/embedding_store.py)).

## Artifact analysis

- **Storage substrate:** `repo` - The central retained memory lives in a separate git repository rooted at `wiki_data`, with active claims under `pages/`, blocked or pending claims under `quarantine/`, and `trust_rules.yaml` as a user-editable policy file; embeddings are colocated JSON files under `wiki_data/embeddings/` but are described as reproducible and not git-tracked ([src/secure_wiki/store/wiki_store.py](https://github.com/NicoBleh/secure-llm-wiki/blob/dfbc60e37487b61e9a5cbce1271a13576a776d51/src/secure_wiki/store/wiki_store.py), [src/secure_wiki/store/embedding_store.py](https://github.com/NicoBleh/secure-llm-wiki/blob/dfbc60e37487b61e9a5cbce1271a13576a776d51/src/secure_wiki/store/embedding_store.py)).
- **Representational form:** `prose` `symbolic` `parametric` - Accepted memory is prose claim text wrapped in symbolic YAML frontmatter; policy is symbolic YAML; gate history and trust/status are symbolic fields; duplicate/conflict checks use distributed vector embeddings as an operational cache rather than the primary readable memory.
- **Lineage:** `authored` `imported` - Claim files derive from imported source documents, while trust rules, prompt builders, gate code, and user-editable policy are authored system-definition artifacts.
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` - Active claims are knowledge context; prompt builders instruct; gates and read hygiene enforce; trust/status route eligibility; sanitizer/adversarial/write gates validate; embeddings and similarity checks rank or compare candidates.

**Source texts.** Storage substrate: external files/URLs read at ingestion time, with local file and URL support plus PDF/HTML text extraction. Representational form: prose or semi-structured document text. Lineage: imported source material, truncated to `_MAX_CHARS` before extraction. Behavioral authority: untrusted knowledge-artifact input only; the prompt and sanitizer explicitly prevent it from becoming an instruction channel ([src/secure_wiki/__main__.py](https://github.com/NicoBleh/secure-llm-wiki/blob/dfbc60e37487b61e9a5cbce1271a13576a776d51/src/secure_wiki/__main__.py), [src/secure_wiki/prompts.py](https://github.com/NicoBleh/secure-llm-wiki/blob/dfbc60e37487b61e9a5cbce1271a13576a776d51/src/secure_wiki/prompts.py)).

**Claim markdown files.** Storage substrate: `wiki_data/pages/<claim_id>.md` for active claims and `wiki_data/quarantine/<claim_id>.md` for quarantined claims, each committed in the wiki git repo. Representational form: mixed prose body plus YAML frontmatter containing source, content hash, trust level, status, gate history, timestamps, and review notes. Lineage: LLM-extracted from a source text, then accepted, quarantined, or escalated by gate decisions. Behavioral authority: active files are knowledge artifacts for query answers; status/trust/gates also act as system-definition metadata because they decide whether a claim is eligible for read-back ([src/secure_wiki/models.py](https://github.com/NicoBleh/secure-llm-wiki/blob/dfbc60e37487b61e9a5cbce1271a13576a776d51/src/secure_wiki/models.py), [src/secure_wiki/store/wiki_store.py](https://github.com/NicoBleh/secure-llm-wiki/blob/dfbc60e37487b61e9a5cbce1271a13576a776d51/src/secure_wiki/store/wiki_store.py)).

**Trust rules and similarity thresholds.** Storage substrate: `wiki_data/trust_rules.yaml`, created at wiki initialization and loaded by trust-tiering. Representational form: symbolic YAML rules and numeric thresholds. Lineage: authored policy, with built-in domain defaults as fallback. Behavioral authority: system-definition artifact with routing/enforcement force; it controls source trust assignment and Gate 5 duplicate/conflict thresholds ([src/secure_wiki/store/wiki_store.py](https://github.com/NicoBleh/secure-llm-wiki/blob/dfbc60e37487b61e9a5cbce1271a13576a776d51/src/secure_wiki/store/wiki_store.py), [src/secure_wiki/trust/tiering.py](https://github.com/NicoBleh/secure-llm-wiki/blob/dfbc60e37487b61e9a5cbce1271a13576a776d51/src/secure_wiki/trust/tiering.py)).

**Embedding cache.** Storage substrate: `wiki_data/embeddings/<claim_id>.json`. Representational form: distributed-parametric vectors serialized as JSON. Lineage: derived from accepted claim text through the configured embedding client; deleted when corresponding claims are cleared. Behavioral authority: system-definition ranking/evaluation input for Gate 5 duplicate and conflict checks, not direct answer context ([src/secure_wiki/store/embedding_store.py](https://github.com/NicoBleh/secure-llm-wiki/blob/dfbc60e37487b61e9a5cbce1271a13576a776d51/src/secure_wiki/store/embedding_store.py), [src/secure_wiki/gate/write_gate.py](https://github.com/NicoBleh/secure-llm-wiki/blob/dfbc60e37487b61e9a5cbce1271a13576a776d51/src/secure_wiki/gate/write_gate.py)).

**Prompt builders and gate code.** Storage substrate: package source code. Representational form: symbolic Python plus prose prompts. Lineage: authored shipped system-definition artifacts. Behavioral authority: instruction, validation, and enforcement; these are not learned memories, but they define the channels by which imported source material may become retained memory and later context ([src/secure_wiki/prompts.py](https://github.com/NicoBleh/secure-llm-wiki/blob/dfbc60e37487b61e9a5cbce1271a13576a776d51/src/secure_wiki/prompts.py), [src/secure_wiki/gate/write_gate.py](https://github.com/NicoBleh/secure-llm-wiki/blob/dfbc60e37487b61e9a5cbce1271a13576a776d51/src/secure_wiki/gate/write_gate.py)).

**Promotion path.** Secure LLM-Wiki promotes imported source text into extracted claim objects, then into active git-tracked Markdown claims only after sanitizer, provenance, trust-tier, adversarial-review, and consistency gates pass. The route can also demote a candidate into quarantine or escalation. There is no implemented promotion command from quarantine back to active; the roadmap names that as a future gap ([docs/roadmap.md](https://github.com/NicoBleh/secure-llm-wiki/blob/dfbc60e37487b61e9a5cbce1271a13576a776d51/docs/roadmap.md)).

## Comparison with Our System

| Dimension | Secure LLM-Wiki | Commonplace |
|---|---|---|
| Primary purpose | Harden an LLM-maintained claim wiki against indirect prompt injection and source poisoning | Maintain a methodology KB for agents and maintainers |
| Main substrate | Separate local git repo with claim Markdown, quarantine files, YAML trust rules, and JSON embedding cache | Git-tracked Markdown collections, type specs, sources, indexes, validation, and review reports |
| Write path | LLM extraction plus sanitizer, trust, review, and consistency gates | Human/agent-authored artifacts plus collection contracts, schemas, deterministic validation, and semantic review |
| Read-back | Coarse trust/status-filtered context block loaded into CLI query sessions | Mostly explicit pull through search, indexes, links, skills, and review workflows |
| Governance | Security-first gate pipeline; quarantines suspicious claims before they become context | Type/register discipline, validation, source reviews, indexes, and archival replacement workflow |
| Context efficiency | Source-to-claim compilation and coarse trust filtering; no per-query retrieval budget | Progressive disclosure by description, index, link, collection, and file-level selection |

Secure LLM-Wiki is closest to Commonplace in its bias toward readable files, git auditability, provenance, and explicit artifact state. Its main divergence is authority: it lets an LLM create the retained claim body, then surrounds that creation with gates. Commonplace usually treats durable prose claims as authored/reviewed artifacts first and validates their metadata/structure afterward.

The interesting borrow is not "use an LLM to maintain a wiki"; it is the channel discipline around hostile source material. Secure LLM-Wiki assumes imported text is actively adversarial, prevents it from becoming a trusted instruction channel, and repeats that hygiene at read time. Commonplace has stronger source citation and review practice, but less explicit injection treatment when source snapshots or external text are loaded into an agent's context.

**Read-back:** `push` - Retained claims reach the query model because `secure-wiki query` builds a system prompt containing the entire eligible wiki context block before the user asks questions; `secure-wiki context` is a pull surface for humans/tools, but the acting query model receives memory by coarse session-level push.

**Read-back signal:** `coarse` - The query path loads the eligible wiki context block by status/trust hygiene rather than by per-question identifier or inferred relevance.

**Faithfulness tested:** `no` - The review cites read-hygiene and trust tests, but not a with/without ablation or behavioral faithfulness check proving the pushed context changes model behavior.

### Borrowable Ideas

**Nonce-delimited source and review envelopes.** Commonplace could use builder functions for source-review and ingest prompts that always wrap untrusted source text in unpredictable delimiters and verify structured response envelopes. Ready for snapshot/ingest paths where source text is copied into model context.

**Treat the write gate as the trust boundary, not the LLM prompt.** Secure LLM-Wiki makes model extraction advisory until deterministic gates accept the claim. Commonplace already has validation and semantic gates; the borrow is to make "source-derived candidate cannot become retained artifact until gate result exists" explicit for higher-risk ingest flows.

**Keep quarantine as a first-class retained lane.** Commonplace archives replaced reviews, but source-derived suspicious candidates usually disappear into reports or failed runs. A quarantine directory for rejected ingests could preserve forensic evidence without making it active KB context. Needs a concrete incident or source-poisoning workflow before adding.

**Strip forged trust markers at read time.** Secure LLM-Wiki tests that `[T]` inside claim text cannot impersonate system-assigned trust. Commonplace could apply the same principle to generated report markers, review statuses, and frontmatter-like strings copied from sources. Ready as a small parser/helper rule if repeated source injection appears.

**Host-pattern trust rules with safe suffix matching.** The trust registry's host-only matching and tests against query-string/domain-suffix bypasses are a good security baseline for URL-derived source trust. Commonplace could borrow the matching discipline for source snapshot classification, but the policy vocabulary should remain lighter unless automated trust routing grows.

## Write-side placement

**Write agency:** `automatic` `manual` — the review describes system-driven generation, extraction, consolidation, or update of retained artifacts rather than only manual authoring.

**Curation operations:** `dedup` `synthesize` `decay` `promote` — the existing review evidence identifies automatic store-changing operations matching these curation classes.

## Curiosity Pass

**The system is more claim store than wiki.** The README says linked Markdown wiki, but the inspected implementation stores one Markdown file per atomic claim with metadata. There is no implemented page graph, backlink structure, or higher-level synthesis layer in the reviewed code.

**The adversarial reviewer checks manipulation, not truth.** This is a sensible narrowing, but it means a cleanly phrased false claim from a semi-trusted source can pass the security gate if consistency checks do not catch it. The system protects channels better than epistemic correctness.

**Read-back is deliberately safe but context-heavy.** The query path loads all active trusted/semi-trusted claims matching the chosen minimum trust level. That avoids retrieval poisoning from raw sources, but it can still dilute context as the wiki grows because there is no top-k, topic, project, or source-scope selector.

**The sanitizer TODO is real.** `sanitize()` returns flags and the gate uses them, but the module still notes missing structured audit logging and an unresolved threshold policy comment ([src/secure_wiki/ingestion/sanitizer.py](https://github.com/NicoBleh/secure-llm-wiki/blob/dfbc60e37487b61e9a5cbce1271a13576a776d51/src/secure_wiki/ingestion/sanitizer.py)). The roadmap likewise plans an audit log, which would make the forensic story less dependent on stdout and commit messages ([docs/roadmap.md](https://github.com/NicoBleh/secure-llm-wiki/blob/dfbc60e37487b61e9a5cbce1271a13576a776d51/docs/roadmap.md)).

**Reset defaults favor privacy over audit history.** `clear --reset` wipes and re-initializes the wiki git repo unless `--keep-history` is passed. That is coherent for poisoned or sensitive claims, but it means "git as full forensic audit trail" has an operator-controlled escape hatch ([src/secure_wiki/store/wiki_store.py](https://github.com/NicoBleh/secure-llm-wiki/blob/dfbc60e37487b61e9a5cbce1271a13576a776d51/src/secure_wiki/store/wiki_store.py), [src/secure_wiki/__main__.py](https://github.com/NicoBleh/secure-llm-wiki/blob/dfbc60e37487b61e9a5cbce1271a13576a776d51/src/secure_wiki/__main__.py)).

## What to Watch

- Whether `secure-wiki promote` is implemented. That would close the current quarantine-to-active human review path and decide whether quarantine is merely storage or a governed workflow.
- Whether query-time selection is added. Topic/source/time scoping or retrieval over claim embeddings would change the system from coarse push to relevance-gated memory activation.
- Whether structured audit logs land. That would strengthen the forensic claim by retaining sanitizer flags, gate outcomes, model usage, and review decisions as machine-readable evidence.
- Whether user feedback on query answers becomes implemented. If ratings can mark contributing claims pending review, the system would start learning quality signals from use, but that would still be user-feedback-derived rather than agent-trace-derived learning.
- Whether claim-level citation tracking for query answers appears. That would connect read-back consumption to later governance and make failed answers actionable at the claim level.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - contrasts: Secure LLM-Wiki stores accepted claims durably, but activates them through coarse query-session context loading rather than relevance-gated selection.
- [Preserve evidence without loading history](../../notes/agent-memory-requirements/preserve-evidence-without-loading-history.md) - aligns: source URI, content hash, trust level, gate history, and git commits preserve audit evidence while read-back loads distilled claims.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - grounds: the review separates claim files, trust rules, embeddings, prompts, and gates by substrate, form, lineage, and authority.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: trust rules, gates, prompt builders, and read-time filters define what can become future context.
- [Symbolic context engineering is bounded by symbol availability](../../notes/symbolic-context-engineering-is-bounded-by-symbol-availability.md) - explains: Secure LLM-Wiki can filter by status/trust symbols it assigned, but has no implemented inferred per-question selector.
