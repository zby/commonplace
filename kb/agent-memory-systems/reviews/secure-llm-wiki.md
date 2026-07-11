---
description: "Secure LLM-Wiki review: hardened claim-wiki pipeline with nonce-delimited extraction, trust tiers, adversarial review, write gates, quarantine, and coarse read-back"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
last-checked: "2026-06-05"
---

# Secure LLM-Wiki

Secure LLM-Wiki, from `NicoBleh/secure-llm-wiki`, is a Python CLI and local claim-wiki store for compiling untrusted files or URLs into persistent Markdown claims while defending the write path against indirect prompt injection and source poisoning. At the reviewed commit, the implemented system is not a general wiki editor: it is a guarded ingest/query pipeline with sanitizer, nonce-delimited LLM extraction, trust-tier assignment, independent adversarial review, embedding-backed consistency checks, git-backed claim storage, quarantine, and read-time context hygiene.

**Repository:** https://github.com/NicoBleh/secure-llm-wiki

**Reviewed commit:** [dfbc60e37487b61e9a5cbce1271a13576a776d51](https://github.com/NicoBleh/secure-llm-wiki/commit/dfbc60e37487b61e9a5cbce1271a13576a776d51)

**Last checked:** 2026-06-05

## Core Ideas

**The retained memory unit is an atomic claim with provenance and lifecycle state.** `Claim` stores text, source reference, trust level, claim id, ingestion time, status, passed gates, optional supersession, and review notes; `SourceRef` carries id, URI, section, and normalized source-content hash. This gives the wiki a smaller durable unit than page-level RAG chunks, but also means extraction quality determines what can later be recalled ([src/secure_wiki/models.py](https://github.com/NicoBleh/secure-llm-wiki/blob/dfbc60e37487b61e9a5cbce1271a13576a776d51/src/secure_wiki/models.py)).

**The write path is security-first and fail-closed.** Ingestion reads a file/URL/PDF/HTML source, sanitizes injection patterns and hidden payloads, constructs provenance, asks an extraction model for nonce-echoed JSON claims, computes embeddings when available, runs an independent batch adversarial review, and only then sends each claim through the write gate. Sanitizer flags, missing provenance, low-trust overwrite attempts, failed adversarial review, duplicate similarity, and conflict similarity can all prevent a normal commit ([src/secure_wiki/__main__.py](https://github.com/NicoBleh/secure-llm-wiki/blob/dfbc60e37487b61e9a5cbce1271a13576a776d51/src/secure_wiki/__main__.py), [src/secure_wiki/ingestion/sanitizer.py](https://github.com/NicoBleh/secure-llm-wiki/blob/dfbc60e37487b61e9a5cbce1271a13576a776d51/src/secure_wiki/ingestion/sanitizer.py), [src/secure_wiki/extraction/extractor.py](https://github.com/NicoBleh/secure-llm-wiki/blob/dfbc60e37487b61e9a5cbce1271a13576a776d51/src/secure_wiki/extraction/extractor.py), [src/secure_wiki/gate/write_gate.py](https://github.com/NicoBleh/secure-llm-wiki/blob/dfbc60e37487b61e9a5cbce1271a13576a776d51/src/secure_wiki/gate/write_gate.py)).

**Trust is a propagated metadata field, not a free-text assertion.** Sources are assigned trusted, semi-trusted, or untrusted by a user-prepended domain rule registry plus built-ins for MITRE, OWASP, arXiv, GitHub, and similar domains. Rules match hostnames, not arbitrary regexes over full URLs, and read-time formatting strips forged `[T]` / `[S]` / `[U]` markers from claim text before adding builder-owned trust prefixes ([src/secure_wiki/trust/tiering.py](https://github.com/NicoBleh/secure-llm-wiki/blob/dfbc60e37487b61e9a5cbce1271a13576a776d51/src/secure_wiki/trust/tiering.py), [src/secure_wiki/prompts.py](https://github.com/NicoBleh/secure-llm-wiki/blob/dfbc60e37487b61e9a5cbce1271a13576a776d51/src/secure_wiki/prompts.py), [tests/test_read_hygiene.py](https://github.com/NicoBleh/secure-llm-wiki/blob/dfbc60e37487b61e9a5cbce1271a13576a776d51/tests/test_read_hygiene.py)).

**The wiki store is a separate git repository with active and quarantined claims.** `WikiStore` defaults to `wiki_data/` or `$WIKI_DATA_PATH`, initializes `pages/`, `quarantine/`, `trust_rules.yaml`, and a git repo, writes Markdown files with YAML frontmatter, and commits each save/quarantine operation with source URI context. Embeddings live beside the wiki in `embeddings/<claim_id>.json`, but are explicitly not tracked as canonical Markdown pages ([src/secure_wiki/store/wiki_store.py](https://github.com/NicoBleh/secure-llm-wiki/blob/dfbc60e37487b61e9a5cbce1271a13576a776d51/src/secure_wiki/store/wiki_store.py), [src/secure_wiki/store/embedding_store.py](https://github.com/NicoBleh/secure-llm-wiki/blob/dfbc60e37487b61e9a5cbce1271a13576a776d51/src/secure_wiki/store/embedding_store.py), [tests/test_wiki_store.py](https://github.com/NicoBleh/secure-llm-wiki/blob/dfbc60e37487b61e9a5cbce1271a13576a776d51/tests/test_wiki_store.py)).

**Context efficiency is coarse filtering, not retrieval ranking.** Read-time loading filters by status and minimum trust, drops untrusted claims even when requested, wraps all admissible claims in a nonce-delimited context block, and adds source URI, section, ingestion time, and gates. This is safer than raw source replay and cheaper than scanning all original documents, but the query command loads all matching claims for the session; there is no top-k retrieval, semantic search over the wiki, token budget, or targeted instance match ([src/secure_wiki/read/hygiene.py](https://github.com/NicoBleh/secure-llm-wiki/blob/dfbc60e37487b61e9a5cbce1271a13576a776d51/src/secure_wiki/read/hygiene.py), [src/secure_wiki/__main__.py](https://github.com/NicoBleh/secure-llm-wiki/blob/dfbc60e37487b61e9a5cbce1271a13576a776d51/src/secure_wiki/__main__.py)).

## Artifact analysis

- **Storage substrate:** `files` `repo` — Retained state lives in local files: active claim Markdown under `pages/`, blocked claim Markdown under `quarantine/`, user trust rules in `trust_rules.yaml`, sidecar embedding JSON files, and Python code/tests in the source repository. The claim wiki itself is initialized as a separate git repo, giving each save/quarantine operation a commit history.
- **Representational form:** `prose` `symbolic` `parametric` — Claim text, source snippets, review reasons, prompts, and query answers are prose; YAML frontmatter, enums, trust rules, nonce envelopes, CLI options, JSON responses, gate decisions, and tests are symbolic; sidecar embedding vectors are parametric access/comparison artifacts used by the consistency gate.
- **Lineage:** `authored` `imported` — Code, prompts, tests, trust rules, and user trust overrides are authored system-definition artifacts. Claim files are imported/derived from external files, PDFs, HTML, or URLs through LLM extraction and review. I do not classify this as `trace-extracted`: the source evidence is ordinary documents and web content, not agent session logs, tool traces, event streams, trajectories, or rollouts.
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `validation` `ranking` `learning` — Active claims serve as knowledge for later answers; prompts, trust rules, and CLI defaults instruct the pipeline; the sanitizer, provenance checks, trust-tier gate, adversarial review, read-time untrusted floor, and deletion confirmations enforce boundaries; tests and gates validate writes/read hygiene; embedding similarity ranks candidate duplicates/conflicts for gate decisions; extraction learns/imports retained claims from source documents.

**Active and quarantined claim files.** Storage substrate: Markdown files in the wiki data repo. Representational form: prose claim body plus symbolic frontmatter for provenance, trust, status, gates, and ids. Lineage: imported/derived from a source section by extraction and write-gate processing. Behavioral authority: active files become admissible knowledge context; quarantined files are audit artifacts and do not enter normal read-back.

**Trust rules and gate policy.** Storage substrate: `trust_rules.yaml`, built-in rule lists, prompt builders, and write-gate code. Representational form: symbolic domain rules, thresholds, enums, and control flow plus prose comments/prompts. Lineage: authored. Behavioral authority: instruction, enforcement, validation, and ranking because they decide trust assignment, block/quarantine/escalate outcomes, and similarity thresholds.

**Read-time context block.** Storage substrate: assembled in memory from stored claim files. Representational form: prose claims with symbolic builder-owned trust markers and nonce delimiters. Lineage: derived view over active stored claims. Behavioral authority: knowledge context with a system note that explicitly denies instruction authority to the wiki content.

Promotion path: Secure LLM-Wiki has a strong candidate-to-active path: untrusted source text -> sanitized source -> nonce-verified extracted claims -> reviewed/gated pending claims -> active Markdown claim or quarantine/escalation. It does not promote claims into higher-order summaries, rules, or validators; higher authority comes from passing gates, not from synthesis across stored memory.

## Comparison with Our System

| Dimension | Secure LLM-Wiki | Commonplace |
|---|---|---|
| Primary purpose | Hardened claim wiki for untrusted source ingestion and later Q&A | Agent-operated methodology KB with typed Markdown artifacts, source captures, reviews, and validation |
| Canonical memory unit | Atomic claim Markdown file with provenance and status | Typed note/review/source/instruction artifacts with frontmatter, links, and collection contracts |
| Write governance | Sanitizer, nonce extraction, trust tiers, adversarial review, write gate, quarantine, git commits | Collection/type contracts, deterministic validation, semantic review gates, source citation rules, git history |
| Read path | Trust/status-filtered all-claims context block or printed context | Explicit search, indexes, links, skills, reports, and validation-driven navigation |
| Security emphasis | Prevent untrusted source text from becoming trusted persistent memory | Preserve fidelity, routing discipline, reviewability, and artifact validity across agent work |

Secure LLM-Wiki is closer to a security gate around knowledge acquisition than to Commonplace's broad library/workshop system. Its most relevant contribution is making the write boundary explicit: every imported source-derived claim has provenance, trust, review, and gate state before it can become active memory. Commonplace already has source capture and validation, but not a separate quarantine lane for source-derived claims before promotion into knowledge artifacts.

The main tradeoff is granularity. Secure LLM-Wiki's atomic claims are easy to gate and filter, but the system does not preserve rich page-level argument structure, link semantics, or collection-local conventions. Commonplace's artifacts carry more meaning per file, but that also makes automatic gate decisions harder: a note can contain many claims, roles, links, and caveats.

The read path is weaker than the write path. Secure LLM-Wiki can ensure only active trusted/semi-trusted claims are loaded, but it does not select for the user's actual question beyond the minimum-trust filter. Commonplace's lexical search and authored navigation are less security-hardened, but often more targeted.

### Borrowable Ideas

**Quarantine as a first-class write outcome.** Ready now. Commonplace source-ingest and review workflows could use a quarantined/candidate namespace for artifacts that failed source hygiene, citation grounding, or semantic review without deleting the evidence.

**Builder-owned trust markers.** Ready now. When Commonplace renders source-derived snippets into prompts or review bundles, trust/status labels should be generated outside the quoted content and stripped from source text to prevent label forgery.

**Nonce-delimited review prompts with echo checks.** Ready for model-mediated gates. Commonplace semantic review and ingestion prompts could borrow nonce echo verification where source text or review findings are passed through a model and later parsed as structured output.

**Separate active/quarantine git history for imported claims.** Needs a concrete use case. A separate repo is useful for a claim store with many small writes, but Commonplace's main KB already has repo history; a separate store would only pay off if imported claim atoms became numerous.

**Do not borrow all-claims read-back.** Needs targeted retrieval first. Trust filtering is necessary but not enough; Commonplace should avoid pushing an entire admissible memory set when a query-specific search surface can keep context smaller.

## Write side

**Write agency:** `manual` `automatic` — Users manually choose sources, trust overrides, resets, deletion commands, and trust-rule edits; the system automatically reads supported sources, extracts claims, computes embeddings when possible, reviews/gates each claim, commits active claims, quarantines blocked/escalated claims, and writes sidecar embeddings.

**Curation operations:** `none` — The automatic write path is acquisition plus admission control, not ongoing curation over existing memory. Gate 5 can detect likely duplicates or conflicts against existing claims and block/escalate the candidate, but I did not find automatic dedup merging, consolidation, in-place evolution, stale invalidation, decay, promotion, or synthesis across stored claims.

## Read-back

**Read-back:** `both` — `secure-wiki context` is explicit pull because it prints the stored wiki context for an operator or host process to use deliberately; `secure-wiki query` pushes the selected stored claims into the downstream LLM system context at query-session startup before user questions are answered.

**Read-back signal:** `coarse` — The push path is always-load over admissible claims, filtered by status, trust floor, and the hard exclusion of untrusted claims. It does not select for the question, source id, tags, embeddings, lexical relevance, or LLM judgment.

**Faithfulness tested:** `no` — The repository tests delimiter hygiene, trust filtering, marker-forgery stripping, and corpus stop gates, but I did not find a with/without memory ablation, perturbation test, or post-answer audit proving that pushed wiki context changes answers faithfully.

The read-back injection point is pre-invocation: `cmd_query()` calls `load_for_context()`, concatenates the system note, nonce-delimited context block, and query task prompt, then streams model answers to later questions. Authority at consumption is advisory evidence: `QUERY_TASK_PROMPT` tells the model to answer only from wiki context and cite source URIs, while the context system note says claims are high-quality evidence rather than instructions. That is stronger than ordinary notes as context, but it is not an enforced verifier after generation.

Selection scope is intentionally conservative but coarse. `load_for_context()` loads active claims by default, can include pending claims only if requested, and never includes untrusted claims even when the caller asks for `--min-trust untrusted`. This controls trust dilution but not token volume or relevance dilution as the wiki grows.

## Curiosity Pass

**The README's "all seven layers" claim is broadly grounded, but some layers are thin.** The sanitizer, extractor, trust tiering, review, write gate, store, and read hygiene all exist. The "wiki" layer, however, is a claim-file store rather than a linked Markdown wiki with pages, backlinks, summaries, or navigation.

**Gate 5 is a blocker, not a truth-maintenance system.** Similarity can quarantine duplicates or escalate conflicts, but the system does not mark old claims superseded, merge duplicates, or retain contradiction graphs. The `SUPERSEDED` enum exists, but I did not find a normal pipeline path that uses it.

**The security model protects persistence better than answer quality.** A poisoned source has several chances to be stopped before becoming active memory. Once active claims are loaded, answer quality depends on prompt following and source citation, not on a post-answer verifier.

**The extraction stage accepts legacy formats.** Nonce-echoed envelope output is the current path, but bare arrays and line-by-line JSON are still accepted with a warning. That is pragmatic for local models, yet it weakens the strictness of the nonce discipline relative to the prompts.

## What to Watch

- Whether query read-back gains lexical, embedding, or LLM-judged selection over active claims; that would move the system from coarse push toward targeted read-back and reduce context dilution.
- Whether `ClaimStatus.SUPERSEDED` becomes part of a real invalidation or replacement workflow; that would turn the write gate from admission control into truth maintenance.
- Whether quarantined/escalated claims get a human review command that can promote, reject, or edit them with preserved audit trail; without that, quarantine is a terminal holding area.
- Whether legacy extraction formats are removed or made explicitly lower-trust; that would strengthen the nonce-verified structured-output contract.
- Whether active claim files become linked wiki pages or grouped summaries; that would change the artifact from a claim database in Markdown into a navigable knowledge base.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: Secure LLM-Wiki stores durable claims, but only `query` pushes a coarse admissible set into a downstream model context.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: active claims, quarantined claims, trust rules, gate code, embeddings, and read-time context blocks carry different substrates, forms, lineage, and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: active claim files act as evidence/reference/context for later answers.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: prompts, trust rules, sanitizer, write gate, tests, and read-hygiene code shape future behavior with instruction, validation, and enforcement force.
- [Behavioral authority](../../notes/definitions/behavioral-authority.md) - clarifies: Secure LLM-Wiki separates advisory claim content from enforcing write/read policies.
- [Storage substrate](../../notes/definitions/storage-substrate.md) - relates: a separate git-backed wiki repo changes access, deletion, rollback, and audit properties.
