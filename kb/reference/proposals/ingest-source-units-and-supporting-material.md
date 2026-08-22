---
description: "Proposal: decide whether an ingest names one source, a fixed paper-code pair, a co-equal bundle, or one primary source with role-labelled supporting material"
type: ../types/design-proposal.md
---

# Ingest source units and supporting material

An ingest currently looks singular but can depend on several external resources. Ordinary ingestion analyses one captured document. Code-grounded ingestion keeps that document as the primary source while inspecting one or more repositories. Directory ingestion can treat a repository, a paper with supplements, or grouped captures as one source unit. These paths have independently answered the same design question: what external material does one ingest describe?

This proposal makes that question explicit. It considers whether an ingest should remain single-source, admit one fixed companion, accept a co-equal set of URLs, centre one primary source with role-labelled supporting material, or represent each external resource in a separate ingest. It does not choose a field name or schema shape, decide whether snapshots are committed or local, or redesign the ingest report's prose sections.

## Current state (as of 2026-08-22)

- The [`ingest-report` type](../../sources/types/ingest-report.md) requires one `source_snapshot` string. The paired snapshot supplies the canonical source URL, capture metadata, and genre.
- [ADR 045](../adr/045-source-genre-is-a-single-open-field-on-the-snapshot.md) makes that snapshot the single ground truth for genre. The ingest restates the classification in prose but carries no second field.
- The ingest type optionally accepts `code_revisions`, an array of immutable GitHub commit URLs. Three current ingests use it.
- The [paper-with-code procedure](../../instructions/ingest-paper-with-code.md) explicitly treats the version-pinned paper as primary and inspected code as corroborating evidence. It may retain several repositories when they implement distinct claim-bearing parts. The procedure currently supports GitHub only.
- The [directory-ingest procedure](../../instructions/ingest-directory.md) treats one ephemeral, usually gitignored directory as a source unit. That directory may hold a repository, a paper with supplementary material, or grouped captures. The durable ingest records an upstream pin where one exists.
- Ordinary snapshots, repository checkouts, and grouped working copies therefore differ in storage and capture path, while their ingest reports share one type. No general relation says why an additional external resource belongs to the same ingest or what evidential role it plays.

## Problem

Resource cardinality and ingest identity have diverged. The required snapshot pointer says there is one source. The code-grounding field says the analysis may rely on several additional sources. The directory path can hide an arbitrary set behind one local root. A reader can recover the special code relation from the report section, but the general source unit remains implicit.

Replacing the singular pointer with an unrestricted URL list would expose cardinality without resolving identity. A paper, its implementation, its dataset, and an independent critique do not contribute in the same way. If they become co-equal members, it is unclear which one determines the title, author, genre, summary, and source-level limitations. It is also unclear whether the report may attribute a claim to the bundle without identifying which member supports it.

The opposite response—one ingest per URL—preserves attribution but can fragment one evidential object. A paper's released implementation often matters only because it confirms, qualifies, or fails to expose a mechanism claimed by the paper. Writing a standalone ingest for that repository can duplicate the paper analysis and obscure the corroborating relation that motivated inspecting the code.

The design must therefore distinguish two questions:

1. What gives the ingest its identity as a source analysis?
2. Which additional external resources may alter the warrant or interpretation of that analysis?

## Options

### 1. Preserve one source and keep specialized companion fields

Ordinary ingests continue to name one snapshot. Code-grounded ingests retain their dedicated repository-revision field and section. Other composite cases continue through directory ingestion or gain their own specialized fields when needed.

**Operativity path:** the current ingest type, ordinary skill, paper-with-code branch, and directory procedure remain the consumers. Validation checks each special field independently, and the relevant branch interprets its semantics.

This is the smallest change and keeps ordinary ingestion simple. Each new companion kind creates another branch and another way of expressing that several external resources form one evidential unit. The directory case remains opaque at the durable metadata surface.

### 2. Admit exactly one document and one implementation URL

A code-grounded ingest becomes an explicit pair: the document supplies the claims and the public repository supplies implementation evidence. Other multi-resource cases remain out of scope.

**Operativity path:** the code-grounding branch resolves both resources, locally materializes each through its existing adapter, and writes their stable identifiers into the ingest. The validator enforces the pair shape; the report writer keeps paper claims distinct from code inspection.

This matches the common paper-plus-repository case and is easy to explain. It is already narrower than current behavior: one paper may require several repositories, and implementation is not the only recurring companion candidate. A second repository would force arbitrary selection, an unstructured escape hatch, or another redesign.

### 3. Treat an ingest as a co-equal set of external resources

One ingest accepts any non-empty set of URLs or stable external identifiers. The set, rather than one member, is the source unit. A paper with code and a synthesis across several articles use the same structure.

**Operativity path:** the ingest skill dispatches each member to an appropriate local materializer, then writes one analysis over the set. Validation checks structural membership; the report must attribute claims and limitations to members because no current consumer can infer those relations from a bare set.

This is the most general cardinality model. It removes the need to distinguish primary from supporting material before ingestion. It also erases the boundary between ingesting one externally recognizable work and authoring a multi-source synthesis. Classification, refresh, citation, and report scope become bundle-level design problems, increasing the risk that already long ingests grow into dossiers.

### 4. Centre one primary source and admit role-labelled supporting material

Exactly one external resource gives the ingest its identity. Zero or more additional resources may be attached when they help interpret, verify, qualify, or operationalize that primary source. Each supporting resource states why it belongs. An implementation repository is one supporting role rather than a separate ingest kind.

An incremental form separates the structural commitment from the supported semantics. [Codification](../../notes/definitions/codification.md) can fix the primary-plus-secondary cardinality now, because changing that symbolic shape later would require a schema and corpus migration. The first implementation can still recognize only implementation evidence. Its secondary list admits several repositories, while datasets, supplements, evaluation artifacts, critiques, and other possible roles remain undefined and unavailable. A future worked case would extend the role semantics and its consumer without replacing the container.

**Operativity path:** the primary source selects the ingest's title, classification, summary, and normal capture path. Initially, the code-grounding branch alone consumes secondary entries and applies commit-pinned inspection to each implementation source. The ingest skill supplies that material to the writer, while structural validation can require one primary, accept several secondaries, and restrict operative roles to those the system actually defines. Whether the asserted implementation relation is true remains an authoring judgment, not a schema verdict.

This preserves a simple ordinary case and generalizes the existing paper-code asymmetry. It can represent several repositories without making them co-authors of the paper's claims. It creates future extension space without speculating about future roles. Its main costs are committing early to the primary-secondary distinction and ensuring that a general-looking container does not imply support for undefined semantics.

### 5. Keep one ingest per external resource and connect them

Every URL or versioned external object receives its own ingest. A paper ingest links to a repository ingest, dataset ingest, supplement ingest, or critique ingest using an authored relation. Multi-source synthesis happens only in notes or reviews.

**Operativity path:** ordinary ingestion remains singular. Connection discovery and source-collection link conventions carry cross-source relationships; code grounding either consumes a separately ingested repository or becomes a deeper source review over both reports.

This gives every resource independent classification, refresh, and citation. It also charges full ingest overhead to materials that have no independent KB role and can split one code-grounding judgment across several files. The graph preserves the relationship only after both artifacts exist and the link is authored correctly.

## Forces

- **Source identity.** A reader should be able to say what work the ingest is about without reconstructing a bundle policy.
- **Claim attribution.** Additional resources must not lend their authority or fidelity to claims they do not support. Code availability can confirm implementation without reproducing reported outcomes.
- **Ordinary-case economy.** A single article or paper should not pay substantial schema or prose cost for composite cases.
- **Actual code cardinality.** The current procedure already admits several repositories when distinct claim-bearing components require them; an exact pair does not cover the shipped case.
- **Heterogeneous stability.** Papers can have versioned identifiers, repositories have commits, web pages have observation times, and datasets may have releases. One generic URL value does not make their refresh semantics identical.
- **Analysis boundary.** An ingest explains how a source fits the KB. Unrestricted co-equal inputs can turn it into the multi-source synthesis that belongs in a note, review, or workshop.
- **Independent reuse.** A repository or dataset sometimes deserves its own ingest because other artifacts will cite it directly. Requiring a separate ingest every time creates noise when the resource matters only as corroboration.
- **Local materialization.** Whether source bodies and checkouts are committed or locally cached is orthogonal to their durable identity. Any option must work when a fresh checkout has only external identifiers and must fetch material on demand.
- **Invalidation.** A change to supporting material may alter only one bounded judgment, while a change to the primary source can invalidate the ingest's identity-level summary and classification.
- **Early structure versus late semantics.** Cardinality becomes expensive to change once a schema, validator, and corpus consume it. The behavior of a new secondary role can remain late-bound until a worked case establishes what the role means and which consumer needs it.
- **Extension space versus false support.** A flexible list can reserve room without admitting an open vocabulary. An undefined entry must not look operative merely because it fits the container.
- **Global semantics.** If supporting roles become frontmatter values, their meanings belong to the ingest type contract rather than being reinterpreted by individual source collections.

## Free choices

- Whether an ingest's source unit is necessarily centred on one primary work or may be a co-equal bundle.
- Whether the paper-plus-code case remains specialized, becomes the first instance of a general supporting-material relation, or is split into linked ingests.
- Whether initial adoption defines implementation as the only operative secondary role or waits for a non-code case before introducing the general container.
- Which later relations are distinct enough to change ingest behavior. Data, supplements, evaluation artifacts, and critiques are possibilities, not placeholder values or an adopted vocabulary.
- Whether unsupported roles are rejected, reserved but unusable, or permitted only in non-durable working context. Accepting them durably without a consumer would create inert metadata with misleading authority.
- Whether the eventual role vocabulary is closed, open with known values, or expressed through existing link relations. The same word should not silently acquire different semantics in metadata and prose.
- Whether supporting material must be named by an immutable revision when the upstream supports one, and what observation record is sufficient for mutable web sources.
- Whether genre and author signal describe only the primary source, every member independently, or the composite source unit.
- When supporting material becomes independently reusable enough to require its own ingest, and whether an already ingested resource may also appear as supporting material without duplicating analysis.
- How report prose attributes code-grounded findings, empirical results, and limitations to the member that warrants them without reintroducing a large manifest.
- Whether re-ingestion is selected at the whole-ingest level or can identify which member changed and scope reconsideration accordingly.
- How any adopted model composes with a separate decision to make snapshots and checkouts local-only. This proposal requires stable external handles but does not choose cache placement or retention.
- Whether the existing `code_revisions` surface is retained as a convenient projection, replaced by the general model, or rejected as a duplicate representation.
- Whether migration treats grouped directory ingests as one primary source with hidden internal files, several explicit supporting resources, or a distinct source-unit kind.

## Operativity and warrant

Every option changes behavior only when the ingest type, ingestion skills, and validators consume it. Metadata alone would be inert. Capture and checkout adapters determine how external identifiers become local reading material; the report-writing instruction determines how primary and supporting evidence affect prose; source extraction and re-ingestion commands consume the retained identifiers later.

Structural validation can check cardinality, required identifiers, revision syntax, and whether an additional member declares a role. It cannot establish that a repository implements the paper, that a dataset produced a reported result, or that two articles belong in one source unit. Those remain source-grounded judgments. Static code inspection can warrant implementation claims only to the inspected revision and cannot reproduce training, benchmark, throughput, or quality outcomes.

## Adoption criteria

- One ordinary article remains representable without empty companion structures or additional prose sections.
- The same design represents a paper with one repository and a paper with several repositories without arbitrary repository selection.
- If a general secondary container is adopted from code-grounding evidence alone, implementation is the only initially operative role. No non-code role is accepted merely to demonstrate generality.
- Adding a later role requires a worked case that defines its relation to the primary source, stable identity, materialization path, effect on report judgment, and mechanically checkable structure without replacing the primary-secondary container.
- The ingest has one unambiguous retrieval identity, or the co-equal alternative supplies an equally clear rule for title, genre, author, summary, and citation.
- Every additional resource has an explicit reason for inclusion, and report claims remain attributable to the resource that warrants them.
- An independent article comparison does not enter one ingest merely because arbitrary URL cardinality permits it; the design supplies a defensible boundary between supporting evidence and synthesis.
- The three current code-grounded ingests migrate without loss of repository pins, inspected-file citations, execution status, or paper-only claim boundaries.
- At least one current directory ingest tests whether its source unit stays opaque or decomposes into explicit external members.
- Re-ingestion can detect a changed member and state whether the whole analysis or only a bounded supporting judgment needs reconsideration.
- The design works with absent local material: stable external handles remain sufficient to attempt reconstruction, and failure to refetch is reported rather than hidden.
- Validators enforce only mechanically decidable structure. No successful validation is presented as evidence that a supporting relation or source claim is true.
- The choice does not require adopting a snapshot-retention policy or a broader ingest-prose redesign, though it remains compatible with both.

## Risks

- **Bundle creep.** A general supporting mechanism can become an invitation to accumulate every consulted URL in one report.
- **Primary-source fiction.** Some genuine source units may have no defensible primary member, and forcing one can hide joint authorship of the result.
- **Role laundering.** Labelling a repository `implementation` can sound like verification even when the association or mechanism was not inspected.
- **Premature vocabulary.** A role enum derived from paper-code cases may fit datasets, supplements, legal records, or discussion threads poorly.
- **False openness.** A structurally general list may lead authors to use undefined roles before any skill or reader gives those entries consistent consequences.
- **Structural overcommitment.** A primary-secondary shape preserves cardinality flexibility but may still be the wrong abstraction for a future genuinely co-equal source unit.
- **Duplicate analysis.** Allowing a resource both as supporting material and as an independent ingest can create two drifting accounts of its significance.
- **Hidden invalidation.** A mutable supporting source can change the warrant of a tracked ingest even when its primary source is stable.
- **Special-case persistence.** Keeping both a general supporting-material model and dedicated code fields can preserve two competing representations indefinitely.

---

Relevant Notes:

- [A citation cannot assert more fidelity than its capture preserved](../../notes/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md) — rests-on: each member keeps its own evidence boundary; membership in one ingest cannot raise source fidelity
- [ADR 045: source genre is a single open field on the snapshot](../adr/045-source-genre-is-a-single-open-field-on-the-snapshot.md) — compares-with: the current one-source authority allocation that a composite ingest model must preserve or supersede
- [Ingest report type](../../sources/types/ingest-report.md) — evidenced-by: the current singular snapshot pointer and specialized multi-repository revision field
- [Ingest a paper with code](../../instructions/ingest-paper-with-code.md) — procedure: the existing primary-paper, corroborating-code path and its multiple-repository case
- [Ingest a directory](../../instructions/ingest-directory.md) — procedure: the existing ephemeral multi-file source-unit path
