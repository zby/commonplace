# Readiness pass — Fix the activation boundary and execution inventory

**State:** complete on 2026-08-27. Core implementation remains gated by
minimal I3 logical-root semantics.

**Audited starting commit:** `6660bd2ad0d53938551ac283f60463f3c3d91b8e`

**Inventory basis:** the live 2026-08-27 worktree. Counts below are diagnostics,
not migration constants; every execution packet re-derives its inventory.

## Outcome

The four-phase program is coherent if Phase 1 lands only dormant resolution
machinery, Phase 2 is the single semantic activation boundary, and Phase 3 is a
later representation migration. An accepted ADR, live participation
declarations, new mark wording, and any consumer switch must not precede the
Phase 2 activation packet.

This pass also fixes the participation declaration, resolver surface,
transitional head identity, initial projection states, consumer ledger, and
cross-consumer fixture. The two older proposals remain design inputs. Their
optional-head and single-atomic-migration clauses are superseded by the choices
recorded here and must be dispositioned when the adopting ADR retires them.

## Activation boundary

### Phase 1 is dormant infrastructure

After minimal I3 lands, Phase 1 may add the pure Python resolver, transitional
head lookup, an unregistered command renderer, and fixture-only participation
declarations. It does not register or document the command, add participation
clauses to live collection contracts, change any binding tag or mark wording,
switch a consumer, enforce mandatory heads on the live corpus, or promote an
accepted ADR. The decision record remains a workshop draft during this phase.

Dormant Phase 1 code may land separately because no current behavior or reader
license depends on it. Its tests prove the candidate relation without claiming
that the source or installed product has adopted that relation.

### Phase 2 activates the contract once

Phase 2 is one activation packet containing:

- the accepted ADR;
- live collection participation declarations and their validation;
- root and schema authoring guidance;
- mandatory-head enforcement in the transitional representation;
- every exact-membership consumer switch;
- the two starting-witness dispositions; and
- source, installed, and multi-root acceptance through V1.

No merge or release boundary may expose only part of that list. Code and prose
may be reviewed as smaller commits before activation, but the operative state
changes together. This is the point at which the original T1 behavioral
contradiction closes.

### Phase 3 changes representation, not meaning

Phase 2 keeps the current head locations and resolves them through one
root-aware head API. Phase 3 atomically changes that API from legacy metadata
lookup to direct `kb/tags/<tag>-README.md` construction, moves every head,
removes the legacy identity fields and hub branches, and migrates source and
installed projections. It retains no legacy fallback. Because membership and
all consumers already resolve through package APIs, this later move does not
reopen tag semantics.

## Participation declaration

`COLLECTION.md` remains frontmatter-free. Every discovered collection carries
exactly one machine-read body section of this form:

```markdown
## Tag participation

**State:** `participating`
```

The allowed states are:

- `participating` — eligible ordinary artifacts enter this logical root's tag
  membership relation;
- `non-participating` — tags may exist for search or provisional work, but no
  artifact in the collection enters an exact membership claim; and
- `prohibited` — artifacts in the collection may not declare `tags` at all.

`prohibited` is initially reserved for the shared global type collection,
whose artifacts have no single tag-namespace owner. A root-owned collection
uses one of the other two states. Missing, duplicated, unknown, or malformed
state clauses fail validation.

A participating collection may repeat an exact collection-relative exclusion
line after the state:

```markdown
**Excluded subtree:** `proposals/archive/`
```

An excluded subtree is a literal directory prefix, not a glob. It uses POSIX
separators, ends in `/`, remains inside its collection, and contains no `.` or
`..` segment. A missing or non-directory target fails validation so a typo or
stale projection clause cannot silently widen membership. The initial source
use is `kb/reference/proposals/archive/`. I2 must omit or rewrite that line in a
projection where the directory is absent.

Package-wide artifact eligibility remains code-owned. The resolver prunes
validation-ignored and foreign-root subtrees and excludes `COLLECTION.md`, type
specifications, tag heads, generated or infrastructure artifacts, and replaced
archives. Collection clauses select participation and deliberate local
subtrees; they do not restate those package rules.

Every participation or exclusion edit invalidates all marked heads in the
logical root. Creation, deletion, or relocation of a collection requires an
explicit whole-head validation because the old declaration may no longer exist
to supply an impact edge.

## Resolver and command contract

Phase 1 adds `commonplace.lib.tag_membership`, with one immutable result for a
declared logical root:

- logical-root identity and physical boundary;
- deterministic participating-collection paths;
- deterministic `by_tag` membership; and
- member records containing repository-relative POSIX path, title, and
  description.

Tag keys and member records are ordered lexically; a member appears once per
tag. Frontmatter parse failures in an otherwise eligible artifact are resolver
errors, not silent omissions. Head existence and presentation do not affect the
membership set.

All Python consumers import this result. They do not execute a command or
reconstruct participating paths. A separate root-aware `resolve_tag_head`
operation supplies zero or one head for routing consumers.

The thin operator surface is:

```text
commonplace-tag-members TAG --root LOGICAL_ROOT_PATH
```

`--root` is required and must select one I3-declared logical root. The command
has no repository-wide fallback and no cross-root union mode. It emits one JSON
object per line with exactly `path`, `title`, and `description`, in resolver
order. A zero-member query emits no records and exits successfully. Resolution
or declaration errors exit nonzero with the bounded root named. Cross-root
navigation invokes the command once per root and labels the union; neither
root's marks transfer to that union.

No ranking, query-conditioned summary, synonym expansion, or relevance claim
belongs in this surface.

## Head registry and transition

Every tag assigned in participating content is stable and has exactly one
head. Provisional headless vocabulary is allowed only in non-participating
content. The head defines the tag's canonical sense and supplies its fixed
meaning, use, boundary, route, and stopping prefix; richer curation remains
optional.

During Phases 1 and 2, `resolve_tag_head` scans root-owned artifacts for the
existing `tag-readme` type with `index_source: tag` and uses `index_key` as
identity. Duplicate identities fail. Phase 2 requires every participating tag
to resolve to one such head but leaves the files in their existing locations.
The legacy `tag-indexes` hub is not a tag head.

Phase 3 changes the implementation to direct construction of
`<root>/tags/<tag>-README.md`, derives identity from the filename, and removes
`index_source` and `index_key`. Canonical resolution and relocation land
together; metadata scanning does not survive as compatibility code.

Root-owned non-participating artifacts may route a known tag to that root's
head even though they are not members. A headless provisional tag renders as
plain text. Source topic tags may therefore remain search and routing cues;
the separate Phase 4 cleanup removes only redundant source-family values.

## Initial participation matrix

This table supplies migration inputs. Runtime discovery consumes declarations,
not this list or a fixed collection count.

| Projection/root | Participating | Non-participating | Prohibited |
|---|---|---|---|
| Source Commonplace root | `notes`, `reference` except `proposals/archive/`, `instructions`, `agent-memory-systems`, `agentic-systems`, `articles` | `sources`, `work`, later `tags` | none inside the root; `kb/types/` is the separate support root |
| Fresh host root | `notes`, `reference`, `instructions`; every user-created collection must choose explicitly | `sources`, `work`, `tags` | none inside the root |
| Installed Commonplace library root | projected `notes`, `reference`, `instructions`; any later projected participating collection carries its declaration | projected `sources`, `tags` | none inside the root |
| Shared-types support root | none | none | `kb/types/` |

An omitted source collection has no declaration in that projection and is not
an error. A concrete discovered root-owned collection with no declaration is
an error.

## Live head audit

Applying the existing collection tag parser to the six proposed participating
collections, then removing `kb/reference/proposals/archive/`, found 24
member-bearing tags and 20 per-tag heads in the live worktree. Four tags are
headless:

| Tag | Current participating members | Activation disposition |
|---|---:|---|
| `trace-learning` | 104 | Retain and create a minimal head; this choice is already fixed. |
| `review-system` | 2 | Confirm the predicate, then create a head or replace/remove both assignments. |
| `agent-runtime` | 1 | Confirm the predicate, then create a head or replace/remove the assignment. |
| `tags` | 1 | Confirm the predicate, then create a head or replace/remove the assignment. |

The activation invariant is not "24 heads." Phase 2 re-derives every tag in
participating content and dispositions every headless value. It may establish a
minimal head, reuse a better existing tag, or remove a bad assignment; it may
not activate with a headless participating tag.

## Consumer ledger

| Consumer class | Current operative surface | Required disposition | Projection or guard |
|---|---|---|---|
| Root and collection discovery | `src/commonplace/lib/project_paths.py`; `src/commonplace/scaffold_manifest.py` | Consume I3 logical-root and collection objects; do not infer ownership from depth. | I3 manifest/discovery parity and source/install root fixtures. |
| Membership enumeration | `src/commonplace/lib/index_generated.py` | Move eligibility and `by_tag` assembly into the resolver; leave generation as a consumer. | Unit tests compare exact records and ordering. |
| Operator command | No current exact-membership command | Build and test the renderer in Phase 1; register and document `commonplace-tag-members` in the Phase 2 activation without adding a second resolver. | `pyproject.toml`, `kb/reference/commands.md`, CLI tests, and command-catalogue parity. |
| Mark validation | `src/commonplace/lib/validation.py` | Check `complete` and `covered_by` over resolver membership for the head's root. | `tests/commonplace/lib/test_validation_tag_readme.py`. |
| Impact expansion | `ValidationRun.impacted_marked_tag_readmes` in `validation.py` | Resolve heads root-wide; eligible tag edits affect their heads, while declaration edits affect every marked head. | Tests for member, participation, exclusion, creation, deletion, and relocation changes. |
| Generated tag-page tail | `src/commonplace/docs/properdocs_hooks.py`; `index_generated.py` | Generate uncurated members from the same resolver result. | ProperDocs tests compare the shared fixture's member paths. |
| Footer routing | `_find_tag_index` in `properdocs_hooks.py` | Use `resolve_tag_head`; route within the artifact's logical root, including declared non-participating artifacts. | Headed, headless, host, vendored, and foreign-root build cases. |
| Connect discovery and skip license | `kb/instructions/cp-skill-connect/SKILL.md` | Read root-global heads; call `commonplace-tag-members` for exact fallback; scope marks to one root and keep task discovery open. | Source skill and promoted installed copies must match. |
| Agent recipes | `AGENTS.md`, `AGENTS.md.template`, `kb/reference/navigation.md` | Replace path-list `rg` recipes with one command call per root; label cross-root unions as navigation only. | Template/init fixture plus lexical guard against the retired recipes. |
| Mark and head authoring | `kb/types/tag-readme.md`, its schema, `kb/instructions/maintain-curated-indexes.md` | State projection-relative mark semantics, mandatory stable heads, and transitional identity; keep the old identity fields until Phase 3. | Type/schema tests and maintenance examples. |
| Tag assignment grammar | `kb/types/note-base.schema.yaml`, root authoring instructions, collection clauses | Enforce the token grammar structurally and semantic reuse through the write path/review. | Schema fixtures cover `tags` and `covered_by`; semantic review remains non-deterministic. |
| Legacy hub and generated-index branches | `kb/types/generated-index.*`, tag-readme schema, generation/validation branches | Retain through Phase 2; remove only with the Phase 3 move. | Phase 3 lexical absence checks. |
| Review population | `src/commonplace/review/review_target_selector.py` and review-sweep procedures | Phase 2 preserves current heads; Phase 3 adds `kb/tags/` to reviewable roots before moving them. | Selector tests prove heads remain reviewable across the move. |
| Distribution and upgrades | `ScaffoldManifest`, package data, init tests, projected instructions and skills | Consume I2's projection and I1's ownership-aware migration; do not add a tag-specific updater. | Fresh and pre-adoption upgraded fixtures converge on framework-owned paths. |
| Published paths | `properdocs.yml` redirect map and build configuration | Phase 2 changes semantics at old URLs; Phase 3 records redirects for every moved head and the retired hub. | Site build and redirect validation. |
| Machine classification using one tag | `src/commonplace/lib/systems_matrix.py` and agent-memory review contracts | Continue reading `trace-learning` directly; this is predicate parity, not general membership recovery. | Independent Phase 4 schema/type/template/skill/tests packet. |

The implementation packet reruns lexical search over code, instructions,
templates, package data, and tests before claiming this ledger complete. A new
consumer is added by role, not hidden under an existing filename entry.

## Cross-consumer fixture

Build one reusable multi-root fixture after I3 supplies the root object. It has:

- a host `notes` member and host `reference` member carrying `shared-topic`;
- a host `reference/proposals/archive/` artifact carrying the same tag;
- a host `work` artifact carrying the same tag;
- a validation-ignored participating subtree carrying the same tag;
- a host head for `shared-topic`, initially incomplete and then repaired;
- an embedded Commonplace root with its own `notes` and `reference` members and
  its own head for the same string;
- a tagged shared-type artifact as a prohibited negative case;
- one participating collection with a missing declaration;
- one malformed exclusion and one participation change; and
- a tag with zero members.

Expected host membership contains exactly the two host library members.
Expected embedded membership contains exactly the embedded members. Neither
set contains archive, work, ignored, shared-type, or other-root artifacts. An
explicit navigation union contains both sets but licenses neither head's marks
across the root boundary.

Run the same fixture through the Python resolver, command renderer, mark
validator, impact expansion, ProperDocs augmentation and footer routing, and
connect/recipe contract tests. Every consumer uses one shared expected ordered
record set rather than maintaining an independent fixture inventory. The
zero-member command returns an empty bounded result; no shell fallback is
invoked.

In addition, retain integration assertions for the live `learning-theory` and
`artifact-analysis` witnesses and for source, fresh-install, and upgraded
projections. The synthetic fixture proves parity; the retained witnesses prove
that the original contradiction actually closes.

## Execution gates

- Phase 1 starts only after I3 exposes root identity, boundary, ownership, and
  recursive collection discovery including shared types.
- Phase 2 activates only after the resolver contract is stable and V1 can run
  every declared source and installed scope without fail-fast behavior.
- Phase 3 starts only after Phase 2 converges consumers and I1/I2 expose the
  generic upgrade and projection mechanisms.
- Phase 4 cleanup may run independently now. The agent-navigation experiment
  waits for exact resolution and canonical heads and remains outside structural
  closure.
