---
type: types/note.md
description: "Choose among Git parents, provenance records within commits, and external records by the dependency semantics and historical access the work requires."
traits: [title-as-claim, has-comparison, has-external-sources]
---

# Git-backed provenance depends on explicit contribution and dependency semantics

Git can preserve a declaration that a contribution used particular inputs. For that record to answer a provenance question, its consumers must know what counts as a contribution, which artifacts it identifies, and what its dependency links mean. When contribution dependencies fit Git's parent graph, parents can carry that meaning. When dependencies differ from editing ancestry, they need a distinguishable relation, stored within commits or outside them. The architectural choice follows from which relations the work needs to preserve.

## Start with the question the record must answer

Recorded provenance preserves what someone declared. Establishing that the declared inputs were actually used requires evidence or a trusted capture process. Git object identity does not supply that verification. Nor does recorded author text establish who controlled the name. These are separate obligations when causal provenance or authenticated attribution is required.

The weakest requirements are identities that distinguish the relevant artifacts, access to them for the promised use, and an interpretation of the declaration. Human inspection may use an informal convention; automated consumers need a representation they can interpret. Neither a machine-readable schema nor one contribution per commit is necessary for every provenance use.

Granularity follows the question. A commit can identify a contribution, but several contributions can share a snapshot and be distinguished by a path or record key. Whole-repository granularity can suffice for whole-repository questions. A document name may suffice for coarse credit; identifying the exact input version requires more. A branch name or unversioned URL alone cannot distinguish past versions when its referent changes. Replay demands still more: enough inputs and environment information to perform the replay.

The kind of Git object also matters. A blob identifies bytes without their path; a tree identifies a file hierarchy; a commit identifies a tree together with commit metadata and parents. Structured provenance can reside in tracked files or in the commit message. Both can be bound by commit identity, but a consumer reading only the checked-out files does not thereby receive message metadata. Tree identity alone does not bind the message.

## Three places to represent dependencies

**Use Git parents when contributions and dependencies fit the native graph.** This works when contribution units can be commit nodes and the intended relation is acyclic and commit-to-commit. Native ancestry traversal then follows the declared contribution dependencies. One contribution per commit is a sufficient mapping. Typed relations such as “corrects” or “evaluated with,” and policies selecting current conclusions, still require additional interpretation. Non-commit inputs may need another representation.

This choice changes the meaning of ancestry. An experiment committed after an unrelated typo repair need not depend on that repair as a research input. It may depend on a separately published dataset absent from repository ancestry. Editing predecessors and knowledge dependencies answer different questions. If both relations matter and differ, they must remain distinguishable. Assigning parents a research meaning also does not prove derivation: a parent edge remains a declaration unless checked.

**Put structured provenance inside ordinary commits when editing history should keep its own meaning.** File records or messages can identify contributions, their inputs, relation types, and supporting evidence while parents continue to represent editing ancestry. This accommodates several contributions per snapshot and dependencies that differ from edit order. Consumers must interpret the separate relation. A literal hash in a record does not become a Git parent edge, so ordinary ancestry traversal and retention do not automatically follow it. When the history of metadata corrections matters, each correction needs a recorded version.

**Use external provenance records when their scope or lifecycle needs independence from commits.** An external record can associate contributions with commit, tree, or blob identities while spanning repositories and non-Git artifacts. This fits provenance whose updates or queries should proceed independently of repository commits. The external assertions and their target evidence both need suitable identification and retention. An immutable target hash does not make the assertion immutable, authenticated, or available. A mutable record can suffice for current-state questions; historical inspection requires versioned assertions or equivalent history.

These arrangements can be combined: parents might represent immediate derivation while separate records express corrections or dataset dependencies. Their selecting conditions concern representational fit, not a measured ranking of performance or reliability.

## Identity does not ensure continued access or current authority

An exact hash preserves identity information, not the referenced evidence's availability. The following bounded local probe illustrates the distinction. On 2026-09-18, an isolated Git 2.43.0 SHA-1 repository produced these results:

- Changing only a commit message changed the commit ID while preserving its tree ID.
- `git commit-tree` accepted an independently chosen tree with a nominated parent.
- Moving a ref left its old commit object intact. After explicit reflog expiration and pruning, that otherwise unreferenced object disappeared.
- A contribution retained by a ref and its native parent survived pruning. An otherwise unreferenced commit named only in message and file text disappeared and was absent from the ancestry walk.

Thus a separate dependency relation needs its own retention treatment when later inspection is promised. Keeping refs to required contributions, including leaves, is one sufficient arrangement; adequate archives can serve the same purpose.

A correction can be a new contribution declaring that it supersedes an older one. Historical queries can still inspect the old bytes, provided they are retained. Deciding which declaration currently governs requires a consumer rule. An append-only accepted history is therefore a policy over records and references, not a consequence of content addressing. Rewriting history matters when it breaks promised access to earlier identities; provenance does not impose a universal ban on rewriting.

[Agora's documented design](../sources/agora-git-as-shared-memory-for-collective-autoresearch.ingest.md) provides a bounded witness: it assigns “builds on” meaning to Git parent edges and keeps accepted contributions reachable through canonical contribution refs. This demonstrates a described choice of dependency semantics together with an explicit retention mechanism. Those source statements do not establish where its metadata is stored or whether every declared dependency is true.

## Scope

The argument assumes object identities distinguish the relevant bytes and evidence remains available for the required interval. The local probe establishes narrow object behavior; it does not establish collision resistance, authentication, production retention defaults, concurrency safety, or performance. The architectural comparison is conditional reasoning, not evidence that one arrangement produces better research.

If another content-addressed store already supplies adequate identity, retention, and interpreted dependency records, Git adds no missing provenance semantics. Git becomes useful where its repository snapshots, native ancestry, and existing tooling match the work. The required semantics do not by themselves select a schema, server, or storage product.
