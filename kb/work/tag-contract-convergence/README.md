# Tag contract convergence workshop

**Opened:** 2026-08-27

**Posed by:** the operator, after review of T1 in the system-contract consistency
workshop

**Audited starting commit:** `6660bd2ad0d53938551ac283f60463f3c3d91b8e`

**State:** active. The [readiness pass](./plans/00-readiness.md) fixed the
activation boundary, declaration syntax, resolver surface, transitional head
model, consumer ledger, and fixture. On 2026-09-25 it was rebaselined for
[ADR 086](../../reference/adr/086-projects-read-the-library-from-the-installed-package.md),
which removed the installed library copy and with it the multi-root design.
`kb/types/` is now a discovered collection and type specs reject tags
(commit `fd573556`). Later on 2026-09-25 the operator settled the design
(see [Decisions of 2026-09-25](#decisions-of-2026-09-25)): the finding trial
is replaced by the cleanup it would have motivated, the exact resolver is not
built, and heads move to a scaffolded `kb/tags/`. [ADR 089](../../reference/adr/089-tags-are-one-namespace-per-kb-with-heads-in-kb-tags.md)
adopts them, and the implementation landed the same day: participating
scope, the head requirement, heads relocated to `kb/tags/`, the scaffold,
and the docs sweep (see the [change packet](./adr-089-change-packet.md)).
On 2026-09-26 [ADR 090](../../reference/adr/090-one-completeness-mark-reaches-members-in-one-hop.md)
folded `complete` and `covered_by` into one mark meaning one-hop reach;
learning-theory carries it again. Remaining: retire the two tag proposals
through the proposal lifecycle, then close this workshop.

## Goal

Establish one coherent contract connecting:

1. what assigning a tag asserts;
2. which artifacts participate in tag membership;
3. how exact membership is resolved;
4. what a tag head provides;
5. what `complete` and `covered_by` authorize consumers to skip;
6. how every exact-membership consumer uses the same relation;
7. how a host project's tag space stays separate from the installed library's.

This workshop owns the tag subsystem redesign extracted from T1, and, since the
system-contract consistency workshop closed on 2026-09-25, T1's original
contradiction, witnesses, and final closure check in the [T1 closure
tracker](./plans/t1-tag-scope.md).

## Why this is a separate workshop

T1 is no longer one local contradiction repair. It joins tag semantics,
`kb-root` ownership, collection participation, exact resolution, validation,
publishing, navigation, installed projection, and migration. Keeping that
design here lets the consistency workshop ask where operative contracts
disagree while this workshop asks what coherent architecture replaces them.

## Starting witnesses

Both corpus witnesses below have since been repaired locally (see the
[rebaseline](./plans/00-readiness.md#rebaseline-for-adr-086-2026-09-25)). The
defect they exposed is latent, not gone: validation still checks one
collection, so Phase 3 acceptance uses a synthetic cross-collection witness.

- The [tag-readme type](../../types/tag-readme.md) and routing use unqualified
  membership language across collections, while current validation and
  generated augmentation enumerate one collection.
- [Trace-learning techniques in related
  systems](../../agent-memory-systems/trace-learning-techniques-in-related-systems.md)
  carries `learning-theory` without any child declared by the notes collection's
  [covered head](../../tags/learning-theory-README.md), yet that head validates.
- The complete [artifact-analysis head](../../tags/artifact-analysis-README.md)
  omits a live reference proposal under the proposed participating scope.
- Published tag footers can route across a collection boundary while the page
  reached is generated from a narrower membership set.

The full starting audit is in the [T1 closure tracker](./plans/t1-tag-scope.md).

## Design inputs, not authority

- [Tag scope is declared where membership claims are
  made](../../reference/proposals/tag-scope-is-declared-where-membership-claims-are-made.md)
- [Semantic contract for tags and tag
  heads](../../reference/proposals/semantic-contract-for-tags-and-tag-heads.md)
- [Link-following and search impose different metadata
  requirements](../../notes/link-following-and-search-impose-different-metadata-requirements.md)
- [Pointer design tradeoffs in progressive
  disclosure](../../notes/pointer-design-tradeoffs-in-progressive-disclosure.md)
- [Tag maintenance and derived
  browsing](../../reference/proposals/tag-maintenance-and-derived-browsing.md)
  — the Gwern-derived browsing and maintenance options; the source of the
  Phase 2 finding trial's grouped page

The recent Pirolli, Teevan, Tombros–Sanderson, Milo, and Luhmann ingests linked
from those inputs motivate a distinction among proximal cues, contextual local
navigation, and query-conditioned results. They concern humans, practitioner
method, or historical systems. They do not establish LLM-agent performance.

ADR 086 supersedes the tag proposals' embedded-root pruning and the former
parent workshop's disjoint-root design. The proposals remain unchanged until adoption
because this workshop does not make them operative authority.

## Working architecture

The adopting decision should begin from these narrow choices:

- One tag string has one canonical declared sense within one KB. A host
  project's `kb/` and the installed library are separate KBs; the library is
  read-only and validated in the source checkout.
- Membership ranges over the explicitly participating collections of one KB.
  Type specs never carry tags.
- A minimal canonical head is required from the first stable use in a
  participating collection. It may be small before it earns richer routing.
- Provisional vocabulary may exist only outside the participating library.
  Promotion into participating content must reuse or establish a canonical tag.
- Structure enforces one canonical declared sense. Whether an assignment
  satisfies that sense belongs to the write path and semantic review; schema
  validation cannot prove one-string-one-sense.
- `complete` and `covered_by` authorize skipping only exact membership
  resolution. They never authorize stopping task-level discovery.
- The exact resolver defaults to deterministic path, title, and description
  records. Query-conditioned ranking or summaries are later operations.
- Add no new tag relations without a demonstrated consumer. `covered_by`
  remains the only current typed routing relation.
- Canonical heads are the vocabulary registry. Do not add a second manually
  maintained known-tags list unless a concrete provisional-tag lifecycle needs
  one.
- Phase 3 activates these semantics once, with live participation declarations,
  mandatory transitional heads, every exact-membership consumer, and the
  accepted ADR. Phase 1 may land dormant resolver machinery; Phase 4 later
  changes head representation without changing membership.
- Usefulness is tested before correctness is enforced. The operator stopped
  using tags because tag pages did not help them find things (2026-09-25).
  The Phase 2 trial compares the current page, an exact listing, a Gwern-style
  grouped page, and no tag at all; its result decides how much contract and
  head work follows. Letting heads carry tags as related-topic links would
  change membership; if wanted, the ADR decides it.

These are workshop selections until an ADR adopts them.

## Decisions of 2026-09-25

Made by the operator in one working session, after the tag cleanup recorded in
commits `93dd08fb`, `5202c69d`, and `a92e33e0`. They supersede the bullets
above where the two differ.

- **Cleanup, not redesign, answers the usefulness question.** The operator's
  failures to find notes through tags were checked against their own
  examples. The notes were present and tagged; the miss was vocabulary
  (title, description, and head phrase did not carry the operator's label)
  and stale head text that misdescribed what a tag meant. No page shape
  fixes that, so the Phase 2 four-condition trial is not run. Gwern-style
  topic groups are redundant with child tags, which Commonplace already has;
  the grouping proposal stays open only as a split-candidate generator for
  tags over about 100 members, untriggered.
- **One namespace per KB; membership over declared participation.** A tag
  string has one sense within one KB. Every membership claim, mark, and
  generated listing ranges over the KB's participating library collections:
  in this checkout `notes`, `reference`, `instructions`,
  `agent-memory-systems`, `agentic-systems`. `work` and `sources` do not
  participate. Participation is declared in each collection's contract.
- **Heads live in `kb/tags/`, in Commonplace and in host projects.** A head is
  not a note by the notes contract, and members span collections, so the head
  sits in none of them. The hub becomes `kb/tags/README.md`. `commonplace-init`
  scaffolds `kb/tags/` with its contract; an empty collection means every tag
  is a keyword. No heads are scaffolded.
- **A tag without a head is a keyword.** Searchable, listed, but it carries no
  marks and makes no completeness claim. This settles the headless tags
  (`trace-learning`, which marks nearly a whole collection, among them)
  without forcing heads.
- **No cross-KB membership.** A host cannot be a member of a library tag; the
  library is read-only under ADR 086. A host may reuse a library tag string as
  its own tag. A union of two KBs' sweeps is an explicit query, not a claim.
- **The exact resolver is not built.** Agents rarely use tags (see the Phase 2
  plan's survey); the collector, validator, and site tail scanning the
  participating set is the whole consumer change. Phase 1 closes unbuilt.
- **Marks stay enforced-or-omitted and are not forced.** `covered_by` on
  `learning-theory` was restored and dropped again the same day because three
  fundamentals honestly carry no child; weak child tags and three-note tags
  are refused, as on 2026-08-31.
- **Two tag definitions fixed as an example of head cleanup.**
  `deploy-time-learning` names the phenomenon that deployment surprises and
  forces post-release change, historically the maintainers' work.
  `self-improving-systems` names systems that make such changes themselves;
  taking over that work is the natural pairing, stated in both heads and not
  part of either definition.

Remaining program: an ADR adopting the above and closing both tag proposals;
the collector, validator, and site-tail change to participating scope; the
`kb/tags/` contract, scaffold template, and relocation of the 21 heads and hub
as a pure relocation commit after the collector change lands; then the
independent cleanup.

## Staged program

0. [Readiness and execution inventory — complete](./plans/00-readiness.md)
1. [Semantic foundation and exact resolver](./plans/01-semantic-resolver.md)
2. [Finding trial: does any tag page help find things?](./plans/02-finding-trial.md)
3. [Consumer convergence and contract activation](./plans/03-consumer-convergence.md) — scope set by Phase 2
4. [Canonical heads and host migration](./plans/04-canonical-heads-migration.md) — scope set by Phase 2
5. [Independent metadata cleanup](./plans/05-cleanup-and-follow-up.md)

As of 2026-09-25 the plans are superseded by the decisions above: Phase 1
closes unbuilt, Phase 2 is replaced by the cleanup already committed, Phase 3
reduces to the ADR plus the participating-scope consumer change, and Phase 4
to the `kb/tags/` contract, scaffold, and relocation. The plan files are kept
as the record of the design space until the ADR lands. Source-family cleanup
is independent and must not enlarge the core adoption patch.

## External dependencies

None since the 2026-09-25 rebaseline. The former parent workshop's I1, I2, I3, and V1
findings (closed) no longer gate this program: there is no projected library copy to
migrate or validate, and Phase 4 uses `commonplace-init`'s existing migration
path for host projects.

## Evaluation boundary

The Phase 2 finding trial is a gate on scope, not on closure. It decides
whether tags are worth a contract at all and which tag page the contract should
serve. Its result is judged on the operator's real finding tasks, for the
operator and for fresh agents, measuring found targets, misses (including
relevant items outside the tag), items opened, and early stopping.

Structural closure then asks whether every exact-membership consumer that
survives Phase 2 resolves and uses the same eligible set, in the source
checkout and in a host project.

## Closure condition

Close and delete this workshop after:

- the Phase 2 finding trial has recorded its result and decision;
- an ADR adopts the tag contract that decision supports: at minimum one
  semantic, participation, and membership contract, plus the mark and head
  contract if tags remain a finding path;
- all surviving exact-membership consumers use the resolver;
- if heads survive, canonical heads and the source and host migrations pass
  their fixtures;
- the two proposals are retired through the normal proposal lifecycle;
- independent cleanup is completed or explicitly transferred;
- the [T1 closure tracker](./plans/t1-tag-scope.md)'s check passes;
- durable outcomes are linked from current navigation and this workshop has no
  remaining authority role.
