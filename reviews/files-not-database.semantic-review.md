<!-- REVIEW-METADATA
note-path: kb/notes/files-not-database.md
last-full-review-note-sha: 12339b1df086fa1d6e7a489f0153ec201eab4b24
last-full-review-note-commit: 5d0771d0710a683a620be574bcc3f3b86bbdb60b
last-full-review-at: 2026-03-23T09:32:55+01:00
last-accepted-note-sha: 12339b1df086fa1d6e7a489f0153ec201eab4b24
last-accepted-note-commit: 5d0771d0710a683a620be574bcc3f3b86bbdb60b
last-accepted-at: 2026-03-23T09:32:55+01:00
last-acceptance-kind: full-review
review-type: semantic-review
-->
=== SEMANTIC REVIEW: files-not-database.md ===

Claims identified: 15

**Claims extracted:**

1. [Intro bullet list] A database migration "replaces the entire tool chain" across four dimensions: versioning, browsing, agent access, infrastructure.
2. [Intro bullets — versioning] "Git gives branching, diffing, and history for free. Database versioning is either 'diffs in a table' (fragile, no branching) or 'shell out to git' (then why move?)."
3. [Koylanai reference] Koylanai's Personal Brain OS "arrived at the same conclusion independently: 80+ files in markdown, YAML, and JSONL, no database, no API keys, no build step."
4. [Premature schema commitment] "A database schema is a commitment to access patterns you don't yet understand."
5. [Premature schema commitment] "Files let you defer that commitment and constrain incrementally as you learn."
6. [Premature schema commitment] "This is the constrain/relax cycle applied to storage architecture."
7. [Premature schema commitment] "Once access patterns stabilize, a database may earn its place — either as a replacement or, more likely, as a derived layer alongside files."
8. [What actually breaks at scale] Exactly three things break at scale: finding things, too many files per directory, structured queries with scoring.
9. [What actually breaks at scale] "The pattern is: files as source of truth, derived indexes for capabilities files alone can't provide."
10. [What actually breaks at scale] "Cludebot's database stack ... the techniques worth borrowing from it (typed link semantics, contradiction surfacing, staleness decay) can all be implemented over files."
11. [Graphiti section] Graphiti's graph database dependency "is not incidental — it requires capabilities that files genuinely cannot replicate."
12. [Graphiti section] Three specific capabilities files cannot replicate: bi-temporal edge invalidation, community detection, hybrid graph+semantic retrieval.
13. [Graphiti section] "Systems that need temporal invalidation, automated graph analytics, or hybrid traversal+semantic queries have legitimate reasons to pay the database cost."
14. [Graphiti section] "Graphiti's use case (continuously streaming conversational data with contradictions over time) is genuinely different from ours (authored notes with explicit status transitions), and the architectural difference follows from the use case difference."
15. [Title] "Files beat a database for agent-operated knowledge bases."

---

WARN:
- [Completeness] The four-dimension tool-chain enumeration (versioning, browsing, agent access, infrastructure) claims "a database migration doesn't just change storage — it replaces the entire tool chain" then lists exactly four dimensions. This framing reads as exhaustive. But the note's own "What actually breaks at scale" section later identifies **query expressiveness** ("structured queries with scoring — the real gap") as the dimension where files are weakest. That dimension is absent from the opening comparison, which means a reader who takes the bullet list as the full picture gets a biased framing — the strongest database advantage is introduced only later and in the defensive position of "what breaks" rather than in the balanced comparison frame. The note would be more honest if the opening enumeration acknowledged the query dimension where databases win.

- [Completeness] The "What actually breaks at scale" section presents a closed list of three items. Boundary case: **concurrent multi-agent writes**. When multiple agents or processes write to the same file-based KB simultaneously, file locking, git merge conflicts, and race conditions become practical problems. Databases handle concurrent writes with transactions natively. The note never scopes its argument to single-agent use, yet concurrent write coordination is a real scaling pain that files handle poorly compared to databases. This is an omitted fourth scaling problem that falls within the note's own claimed scope (agent-operated knowledge bases can have multiple agents).

- [Grounding — scope mismatch] The note claims "the techniques worth borrowing from [Cludebot] (typed link semantics, contradiction surfacing, staleness decay) can all be implemented over files." The linked source (what-cludebot-teaches-us.md) is more nuanced. It explicitly places **graph-based retrieval** in a "watch for as the KB grows" category, saying "if the KB reaches 1000+ notes with dense cross-linking, navigating via link graph could outperform flat search." It similarly flags **co-retrieval reinforcement** (Hebbian learning on retrieval patterns) as requiring retrieval logging infrastructure that goes beyond files. The note cherry-picks three transferable techniques and claims "all" valuable patterns transfer, while the source itself identifies at least two techniques (graph traversal and co-retrieval reinforcement) that may not transfer to files at scale. The word "all" in the note overstates the source.

INFO:
- [Completeness — Graphiti boundary] The three capabilities listed as things "files genuinely cannot replicate" (bi-temporal edge invalidation, community detection, hybrid graph+semantic retrieval) are presented as a definitive boundary. The Graphiti ingest source also discusses **automated entity deduplication** across the graph (merging "John" and "Dr. Smith" as the same entity using graph context) and **contradiction resolution through temporal supersession** as pipeline capabilities. These might be argued as applications of the listed capabilities rather than independent ones, but the note's phrasing ("it requires capabilities that files genuinely cannot replicate") reads as an exhaustive boundary claim. The actual boundary between what files can and cannot do may be broader than the three items listed.

- [Grounding — vocabulary mismatch] The note says files let you "constrain incrementally" and calls the progression from raw markdown to derived indexes "the constrain/relax cycle applied to storage architecture." The linked constraining.md defines constraining as "narrowing the interpretation space — reducing the range of valid interpretations an underspecified spec admits." Adding queryable structure (frontmatter, grep patterns, derived indexes) to a file-based KB is not straightforwardly about narrowing interpretation space; it is about adding access machinery. The metaphor works if "interpretation space" is stretched to mean "the set of operations the storage medium affords," but that is an extension of the concept beyond its home definition. The link is reasonable and the analogy is productive, but the confident identification ("This is the constrain/relax cycle") overstates the mapping's precision.

- [Grounding — evidence strength] The note says Koylanai "arrived at the same conclusion independently." The linked ingest (koylanai-personal-brain-os.ingest.md) classifies this source as "self-report only" and its Limitations section warns: "We have a snapshot of an X article, not the repository, file tree, prompts, or logs of the underlying system." The convergence evidence is real — an independent practitioner describing the same architectural bet — but the note presents it without flagging the evidence quality. The ingest's own caveats suggest the signal is weaker than the note's unqualified framing implies.

- [Internal consistency — title vs. body] The title claims "Files beat a database for agent-operated knowledge bases" without qualification. The body's conclusion is more nuanced: "files remain the right choice for authored, agent-navigated knowledge where versioning, inspectability, and zero infrastructure matter most" and "systems that need temporal invalidation, automated graph analytics, or hybrid traversal+semantic queries have legitimate reasons to pay the database cost." Graphiti-based systems are also agent-operated knowledge bases, yet the note concedes they legitimately need databases. The title's unqualified scope is mildly inconsistent with the body's narrower conclusion. This is managed well within the text but the title — which is the claim that travels when linked from other notes — carries the broader framing.

PASS:
- [Grounding — Graphiti] The three database capabilities attributed to Graphiti (bi-temporal edge invalidation, community detection, hybrid graph+semantic retrieval) all check out against the Graphiti ingest source, which describes valid_at/invalid_at timestamps, label propagation for community detection, and hybrid search combining semantic + BM25 + graph traversal. The note accurately represents Graphiti's capabilities and correctly identifies them as things files cannot replicate.

- [Grounding — Fintool] The Relevant Notes section cites Fintool as validating "at commercial scale: S3 as source of truth with Lambda-synced PostgreSQL as derived index." The Fintool ingest confirms this precisely: the architecture uses S3 as source of truth with Lambda-synced PostgreSQL for queries, paying users, 11-nines durability. The note's claim that the "derived indexes for capabilities files alone can't provide" pattern matches Fintool's architecture is accurate and appropriately scoped.

- [Grounding — Koylanai factual accuracy] The specific factual claims about Koylanai (80+ files, markdown/YAML/JSONL formats, no database, no API keys, no build step) all appear in the ingest source. The attribution of facts is accurate even if the evidence-strength framing is optimistic (flagged as INFO above).

- [Internal consistency — schema commitment argument] The argument that "a database schema is a commitment to access patterns you don't yet understand" is internally consistent with the incremental constraining narrative. The four-step progression (raw markdown, frontmatter conventions, grep queries, derived indexes) is presented consistently, and the "not a files-forever position" qualifier is maintained from the schema commitment section through to the Graphiti section. The note does not contradict itself on this central point.

- [Internal consistency — Graphiti section vs. main argument] The Graphiti section concedes database legitimacy without undermining the main argument. The note distinguishes its use case (authored notes, explicit status transitions) from Graphiti's (streaming conversational data, temporal contradictions) and argues the architectural difference follows from the use case difference. This is internally coherent — the concession is explained rather than simply asserted, and the scope restriction is maintained.

- [Completeness — incremental constraining sequence] The four-step progression (raw markdown, frontmatter conventions, grep-based queries, derived indexes) was tested against boundary cases: a KB that starts with structured data rather than prose, and a KB where access patterns are known from day one (e.g., migrating an existing database-backed system to files). The sequence holds for the first case. For the second, the note's argument weakens — if you already know your access patterns, the "premature commitment" argument loses force — but this is outside the note's stated scope of "when a project is young." The boundary is acknowledged implicitly.

Overall: 3 warnings, 4 info
===
