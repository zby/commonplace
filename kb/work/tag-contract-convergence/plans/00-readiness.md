# Readiness pass — Fix the activation boundary and execution inventory

**State:** complete on 2026-08-27; rebaselined on 2026-09-25 for [ADR
086](../../../reference/adr/086-projects-read-the-library-from-the-installed-package.md).
Nothing gates Phase 1.

**Inventory basis:** the live 2026-09-25 worktree. Counts below are diagnostics,
not migration constants; every execution packet re-derives its inventory.

## Rebaseline for ADR 086 (2026-09-25)

The 2026-08-27 pass assumed that an initialized project holds two disjoint
`kb-root`s: the host `kb/` and a projected library copy under
`commonplace-library/kb/`. It therefore gated Phase 1 on I3's multi-root model
and Phase 3 on I1's upgrade and I2's projection machinery. ADR 086 removed the
library copy. Projects read the library in place from the installed package,
and the library is validated in the source checkout. This changes the plan:

- **One writable tag space per checkout.** The source checkout and each host
  project each have one `kb/`. The existing `project_paths.kb_root` is
  sufficient; the resolver needs no root-identity model.
- **The installed library is a read-only second target.** An agent in a host
  project can still read the library's tags and heads. The resolver can run
  over the installed library, but nothing validates or migrates there.
- **Marks stay true in the shipped subset.** The package ships `notes`,
  `reference`, `instructions`, and `types`, a subset of the source's
  participating collections. `complete` (the head links every member) and
  `covered_by` (every member carries a listed child tag) both stay true when
  members are removed. A mark validated in source therefore holds over the
  shipped library without install-side revalidation. A shipped head may link
  a source-only member; the build rewrites that link to a GitHub URL.
- **No `prohibited` participation state.** It existed only for type
  collections. `kb/types/` is now a discovered collection, and the `type-spec`
  schema rejects `tags` (commit `fd573556`). The global types collection
  declares `non-participating`.
- **I1, I2, I3, and V1 are no longer dependencies.** Phase 3's host migration
  uses `commonplace-init`'s existing migration path, which already rewrites
  type pointers and removes legacy library copies. Phase 2 validates each
  declared collection with `commonplace-validate` scopes; a whole-product
  validation command would be convenient but is not required.
- **Both starting witnesses have been repaired locally.** On 2026-08-31,
  `learning-theory-README.md` dropped its stale `covered_by` mark (commit
  `a21eac03`). The `artifact-analysis` head now links its one reference member.
  A 2026-09-25 recheck found no marked head that omits a member in another
  collection. The defect is latent: validation still checks one collection, so
  a new cross-collection omission would pass. Acceptance therefore needs a
  synthetic cross-collection witness rather than the live ones.

## Outcome

The four-phase program is coherent if Phase 1 lands only dormant resolution
machinery, Phase 2 is the single semantic activation boundary, and Phase 3 is a
later representation migration. An accepted ADR, live participation
declarations, new mark wording, and any consumer switch must not precede the
Phase 2 activation packet.

This pass fixes the participation declaration, resolver surface, transitional
head identity, participation matrix, consumer ledger, and cross-consumer
fixture. The two older proposals remain design inputs. Their optional-head,
single-atomic-migration, embedded-root, and shared-type clauses are superseded
by the choices recorded here. The adopting ADR must disposition those clauses
when it retires the proposals.

## Activation boundary

### Phase 1 is dormant infrastructure

Phase 1 may add the pure Python resolver, transitional head lookup, an
unregistered command renderer, and fixture-only participation declarations. It
does not register or document the command, add participation clauses to live
collection contracts, change any binding tag or mark wording, switch a
consumer, enforce mandatory heads on the live corpus, or promote an accepted
ADR. The decision record remains a workshop draft during this phase.

Dormant Phase 1 code may land separately because no current behavior or reader
license depends on it.

### Phase 2 activates the contract once

Phase 2 is one activation packet containing:

- the accepted ADR;
- live collection participation declarations, in source and in the init
  templates, and their validation;
- authoring guidance for tags and marks;
- mandatory-head enforcement in the transitional representation;
- every exact-membership consumer switch;
- the synthetic cross-collection witness; and
- source and fresh-install acceptance.

No commit on `main` may expose only part of that list. Code and prose may be
reviewed as smaller commits on a branch, but the operative state changes
together. This is the point at which the original T1 contradiction closes.

### Phase 3 changes representation, not meaning

Phase 2 keeps the current head locations and resolves them through one head
API. Phase 3 changes that API from legacy metadata lookup to direct
`kb/tags/<tag>-README.md` construction, moves every head, removes the legacy
identity fields and hub branches, and migrates host projects. It retains no
legacy fallback. Because membership and all consumers already resolve through
package APIs, this later move does not reopen tag semantics.

## Participation declaration

`COLLECTION.md` remains frontmatter-free. Every discovered collection carries
exactly one machine-read body section of this form:

```markdown
## Tag participation

**State:** `participating`
```

The allowed states are:

- `participating` — eligible ordinary artifacts enter the KB's tag membership
  relation;
- `non-participating` — tags may exist for search or provisional work, but no
  artifact in the collection enters an exact membership claim.

Missing, duplicated, unknown, or malformed state clauses fail validation. Type
specs cannot carry tags in any collection; the `type-spec` schema enforces
that, so no collection state is needed for it.

A participating collection may repeat an exact collection-relative exclusion
line after the state:

```markdown
**Excluded subtree:** `proposals/archive/`
```

An excluded subtree is a literal directory prefix, not a glob. It uses POSIX
separators, ends in `/`, remains inside its collection, and contains no `.` or
`..` segment. A missing or non-directory target fails validation so a typo or
stale clause cannot silently widen membership. The initial source use is
`kb/reference/proposals/archive/`. The shipped library keeps the line only
while the directory ships; the build must drop it otherwise.

Package-wide artifact eligibility remains code-owned. The resolver prunes
validation-ignored subtrees and excludes `COLLECTION.md`, type-definition
content, tag heads, generated or infrastructure artifacts, and replaced
archives. Collection clauses select participation and deliberate local
subtrees; they do not restate those package rules.

Every participation or exclusion edit invalidates all marked heads in the KB.
Creation, deletion, or relocation of a collection requires an explicit
whole-head validation because the old declaration may no longer exist to supply
an impact edge.

## Resolver and command contract

Phase 1 adds `commonplace.lib.tag_membership`, with one immutable result for a
KB directory:

- the KB directory resolved;
- deterministic participating-collection paths;
- deterministic `by_tag` membership; and
- member records containing KB-relative POSIX path, title, and description.

Tag keys and member records are ordered lexically; a member appears once per
tag. Frontmatter parse failures in an otherwise eligible artifact are resolver
errors, not silent omissions. Head existence and presentation do not affect the
membership set.

All Python consumers import this result. They do not execute a command or
reconstruct participating paths. A separate `resolve_tag_head` operation
supplies zero or one head for routing consumers.

The thin operator surface is:

```text
commonplace-tag-members TAG [--library]
```

Without a flag it resolves the project's `kb/`. `--library` resolves the
installed library instead; in the source checkout the two are the same
directory. There is no union mode. The command emits one JSON object per line
with exactly `path`, `title`, and `description`, in resolver order. A
zero-member query emits no records and exits successfully. Resolution or
declaration errors exit nonzero with the KB named. An agent that wants both
spaces calls the command twice and labels the result; neither KB's marks
transfer to the other.

No ranking, query-conditioned summary, synonym expansion, or relevance claim
belongs in this surface.

## Head registry and transition

Every tag assigned in participating content is stable and has exactly one
head. Provisional headless vocabulary is allowed only in non-participating
content. The head defines the tag's canonical sense and supplies its fixed
meaning, use, boundary, route, and stopping prefix; richer curation remains
optional.

During Phases 1 and 2, `resolve_tag_head` scans the KB for the existing
`tag-readme` type with `index_source: tag` and uses `index_key` as identity.
Duplicate identities fail. Phase 2 requires every participating tag to resolve
to one such head but leaves the files in their existing locations. The legacy
`tag-indexes` hub is not a tag head.

Phase 3 changes the implementation to direct construction of
`kb/tags/<tag>-README.md`, derives identity from the filename, and removes
`index_source` and `index_key`. Canonical resolution and relocation land
together; metadata scanning does not survive as compatibility code.

Non-participating artifacts may route a known tag to its head even though they
are not members. A headless provisional tag renders as plain text. Source
topic tags may therefore remain search and routing cues; the separate Phase 4
cleanup removes only redundant source-family values.

A host tag with the same string as a library tag is a separate tag in the
host's own space. Whether a headless host tag may route to the library's head
is open for the ADR; the default is plain text, because the host has not
adopted the library's sense.

## Participation matrix

This table supplies migration inputs. Runtime discovery consumes declarations,
not this list or a fixed collection count.

| KB | Participating | Non-participating |
|---|---|---|
| Source checkout `kb/` | `notes`, `reference` except `proposals/archive/`, `instructions`, `agent-memory-systems`, `agentic-systems`, `articles` | `sources`, `work`, `reports`, `types`, later `tags` |
| Fresh host `kb/` | `notes`, `reference`, `instructions`; every user-created collection must choose explicitly | `sources`, `work`, `reports`, later `tags` |
| Installed library (read-only) | shipped `notes`, `reference`, `instructions`, carrying their source declarations | shipped `types`, later `tags` |

A concrete collection discovered inside a KB with no declaration is an error.

## Live head audit

Applying the existing tag parser to the six participating source collections,
then removing `kb/reference/proposals/archive/`, found 26 member-bearing tags
and 20 per-tag heads on 2026-09-25. Six tags are headless:

| Tag | Participating members | Activation disposition |
|---|---:|---|
| `trace-learning` | 105 | Retain and create a minimal head; this choice is already fixed. |
| `methodology` | 6 | Confirm the predicate, then create a head or replace/remove the assignments. |
| `review-system` | 2 | Confirm the predicate, then create a head or replace/remove both assignments. |
| `agent-runtime` | 1 | Confirm the predicate, then create a head or replace/remove the assignment. |
| `planning` | 1 | Confirm the predicate, then create a head or replace/remove the assignment. |
| `tags` | 1 | Confirm the predicate, then create a head or replace/remove the assignment. |

The activation invariant is not a head count. Phase 2 re-derives every tag in
participating content and dispositions every headless value. It may establish a
minimal head, reuse a better existing tag, or remove a bad assignment; it may
not activate with a headless participating tag.

## Consumer ledger

| Consumer class | Current operative surface | Required disposition | Guard |
|---|---|---|---|
| Collection discovery | `src/commonplace/lib/project_paths.py` | Already discovers `kb/types/` (commit `fd573556`). Parse participation clauses from discovered collections. | Discovery and declaration tests. |
| Membership enumeration | `src/commonplace/lib/index_generated.py` | Move eligibility and `by_tag` assembly into the resolver; leave generation as a consumer. | Unit tests compare exact records and ordering. |
| Operator command | No current exact-membership command | Build and test the renderer in Phase 1; register and document `commonplace-tag-members` in Phase 2 without adding a second resolver. | `pyproject.toml`, `kb/reference/commands.md`, CLI tests. |
| Mark validation | `src/commonplace/lib/validation.py` | Check `complete` and `covered_by` over resolver membership for the whole KB. | `tests/commonplace/lib/test_validation_tag_readme.py`. |
| Impact expansion | `ValidationRun.impacted_marked_tag_readmes` in `validation.py` | Eligible tag edits affect their heads anywhere in the KB; declaration edits affect every marked head. | Tests for member, participation, exclusion, creation, deletion, and relocation changes. |
| Generated tag-page tail | `src/commonplace/docs/properdocs_hooks.py`; `index_generated.py` | Generate uncurated members from the same resolver result. | ProperDocs tests compare the shared fixture's member paths. |
| Footer routing | `_find_tag_index` in `properdocs_hooks.py` | Use `resolve_tag_head`, including for non-participating artifacts. | Headed and headless build cases. |
| Connect discovery and skip license | `kb/instructions/cp-skill-connect/SKILL.md` | Read heads; call `commonplace-tag-members` for exact fallback; keep task discovery open after a mark skip. | Skill text review; the installed stub points at the same file. |
| Agent recipes | `AGENTS.md`, `AGENTS.md.template`, `kb/reference/navigation.md`, the generated `.commonplace/library.md` | Replace path-list `rg` recipes with the command; use `--library` for library tags and label a two-space result as navigation only. | Template/init fixture plus lexical guard against the retired recipes. |
| Mark and head authoring | `kb/types/tag-readme.md`, its schema, `kb/instructions/maintain-curated-indexes.md` | State KB-wide mark semantics, mandatory stable heads, and transitional identity; keep the old identity fields until Phase 3. | Type/schema tests and maintenance examples. |
| Tag assignment grammar | `kb/types/note-base.schema.yaml`, authoring instructions, collection clauses | Enforce the token grammar structurally and semantic reuse through the write path and review. | Schema fixtures cover `tags` and `covered_by`; semantic review remains non-deterministic. |
| Legacy hub and generated-index branches | `kb/types/generated-index.*`, tag-readme schema, generation/validation branches | Retain through Phase 2; remove only with the Phase 3 move. | Phase 3 lexical absence checks. |
| Review population | `src/commonplace/review/review_target_selector.py` and review-sweep procedures | Phase 2 preserves current heads; Phase 3 adds `kb/tags/` to the reviewable set before moving heads. | Selector tests prove heads remain reviewable across the move. |
| Library build and init | `hatch_build.py` `SHIPPED`, `scaffold_manifest.py`, `commonplace-init` migrations, `library.md` entry points | Phase 2 ships the declarations and scaffolds host declarations. Phase 3 ships `tags/`, scaffolds an empty host `kb/tags/`, moves host heads in an init migration, and repoints the library's navigation entry point. | Build test, init tests on fresh and pre-move host fixtures. |
| Published paths | `properdocs.yml` redirect map and build configuration | Phase 2 changes semantics at old URLs; Phase 3 records redirects for every moved head and the retired hub. | Site build and redirect validation. |
| Machine classification using one tag | `src/commonplace/lib/systems_matrix.py` and agent-memory review contracts | Continue reading `trace-learning` directly; this is predicate parity, not general membership recovery. | Independent Phase 4 packet. |

The implementation packet reruns lexical search over code, instructions,
templates, package data, and tests before claiming this ledger complete. A new
consumer is added by role, not hidden under an existing filename entry.

## Cross-consumer fixture

Build one reusable fixture KB with:

- a `notes` member and a `reference` member carrying `shared-topic`;
- a `reference/proposals/archive/` artifact carrying the same tag;
- a `work` artifact carrying the same tag;
- a validation-ignored participating subtree carrying the same tag;
- a head for `shared-topic` in `notes`, marked `complete` while linking only the
  `notes` member, which must fail, and then repaired — this is the synthetic
  cross-collection witness;
- a tagged type spec as a schema-rejected negative case;
- one participating collection with a missing declaration;
- one malformed exclusion and one participation change; and
- a tag with zero members.

Expected membership contains exactly the two library members. It contains no
archive, work, ignored, or type artifacts. A second fixture directory stands in
for the installed library through `COMMONPLACE_LIBRARY_ROOT`; `--library`
resolves it independently and neither KB's marks apply to the other.

Run the same fixture through the Python resolver, command renderer, mark
validator, impact expansion, ProperDocs augmentation and footer routing, and
recipe contract tests. Every consumer uses one shared expected ordered record
set. The zero-member command returns an empty bounded result; no shell fallback
is invoked.

## Execution gates

- Phase 1 has no external gate.
- Phase 2 activates only after the resolver contract is stable.
- Phase 3 starts only after Phase 2 converges consumers.
- Phase 4 cleanup may run independently now. The navigation and browsing
  trials wait for exact resolution and canonical heads and remain outside
  structural closure.
