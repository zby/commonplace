# Analysis of the top-level reference documents

Made on 2026-11-19 at the operator's request, covering the 30 top-level documents under `kb/reference/`. Five reading agents each read one group of documents in full and compared it with the places that could already hold the same content: `--help`, code, ADRs, skills, collection contracts, type specs and the validator. An agent (claude-fable-5-2) wrote this file from their reports. It did not re-check their line numbers; items they marked unverified are marked here.

The question for each document: who needs it, by what activation path does that reader reach it, what does it hold that exists nowhere else, and is it still true. See [README.md](./README.md) for the current framing and order of work.

## Authoring rules

Nine documents. Three hold rules a writer must apply that no route states in full: `link-vocabulary.md`, `validation-contract.md` and the collision ledger. The rest are descriptions or rationale whose binding parts already live in a skill, a collection contract, a type spec or the validator.

The validator enforces no link-label rule, and no review gate checks label authorisation. A link rule is applied only if a skill or contract states it.

| Document | What it is | On a route? | Duplicated | Unique content | Stale |
|---|---|---|---|---|---|
| `link-vocabulary.md` | approach, how to write a contract's outbound section, a label catalogue, lineage semantics | the approach and the articulation test are in `cp-skill-write` and `cp-skill-connect`, which both say no separate linking document is needed; lineage is a pointer only | about 45% | the classifying sequence for lineage, truth conditions per relation, footer placement, `Distilled into:` retirement; how to write an outbound section | `adapted-from` is defined "where authorized", and no collection authorises it |
| `validation-contract.md` | where findings come from, the base checks, schema limits, the unquoted-source limit | the validator prints the checks; the writer-facing parts are in contracts and `cp-skill-add-collection` | about 50% | the base-check list with severities, the bare-text opt-out, why base checks are not type-configurable | says "three sources" of a finding; the validator emits a fourth label, `[collection]`. Omits one base check |
| `collections-and-types.md` | how a location selects a contract and `type:` selects a spec | `cp-skill-write` restates the type-value rules; the validator enforces them | about 70% | two lifecycle exceptions for type eligibility; the schema `$ref` form | none found; `cp-skill-add-collection` reserves five special names where this lists six, and the skill is the stale side |
| `content-routing.md` | table from content kind to destination | `AGENTS.md` points to it for ambiguous placement; `cp-skill-add-collection` adds rows to it | about 50% | the "regenerable from" and "consumed by" columns; three rows | names no row for `kb/articles/`, `kb/agentic-systems/` or `kb/agentic-system-analyses/`; cites a heading that was renamed |
| `navigation.md` | the read path, `rg` recipes, future search ideas | `AGENTS.md` states the core rule; `cp-skill-connect` restates the recipes | about 55% | keep tags inline; do not broaden a theory lookup to sources | the by-tag recipe searches five collections; six participate |
| `collection-prototypes.md` | catalogue of copy-once starting contracts | no route; `cp-skill-add-collection` restates the one operative rule | about 70% | the template list; the experimental prototype | the list of seeded contracts omits the tag contract |
| `vocabulary-collision-ledger.md` | seven terms with two tolerated senses, each with a decision for new text | `AGENTS.md` mentions it without a read instruction; `cp-skill-write` does not | about 10% | all seven decisions | one provenance link to a deleted workshop |
| `vocabulary-unification-ledger.md` | one candidate unification | `AGENTS.md` only | none | the whole entry | none found (links not all opened) |
| `epistemic-stance.md` | the Popperian commitments the KB's assertions assume; a self-described stub | `AGENTS.md` names it; the applied rules are in the theory contract and ADR 066 | about 30% | the "not inherited" list; one citation rule | calls the theory contract the "notes contract" |

**Rules stated only in a free-standing document.** These are the rules an agent most likely does not apply:

- the lineage test: the classifying sequence, truth conditions, the mixed-artifact rule, footer placement and `Distilled into:` retirement;
- how to write a contract's outbound-links section;
- six of the seven collision-ledger decisions;
- keep tags inline, and do not broaden a theory lookup to sources;
- keep an interpreting report outside an ignore-marked subtree;
- three content-routing rows, reachable only through a conditional pointer.

**A constraint on moving.** `validation-contract.md` is a code dependency. `validation.py` requires `reference/validation-contract.md` as a pinned criterion, the analysis workflow's `plan.yaml` loads it, and three test fixtures copy it. It cannot move or go without a code change.

**Reading.** The operator's guess holds for most of this group: where a rule matters, a skill or contract already carries it, and the free-standing document is a description for a maintainer. The exceptions are the listed rules, which need a route, not a document.

## The command reference, `commands.md`

About 85 to 90% of its 43 kB restates `--help`, the CLI module docstrings, the review guide, or the analysis skill and ADRs. About 3 to 4 kB exists nowhere else. An [earlier documentation study](../../theory/evidence/seven-documentation-cases-left-routing-and-synthesis.md) already ruled "reduce and keep checked" for this file, and its own opening says it keeps only purpose and composition; the review and analysis sections have regrown past that.

| Section | Duplicated | What exists only here | Where it should go |
|---|---|---|---|
| intro; `init`; `source`; `verify-quotes`; the snapshot commands | all | nothing | nowhere |
| `status` | about 25% | the four parts of the report, stable next-action ids, the output schema name, "does not mutate, rank, schedule or become an authority" | the command's help |
| `validate` | about 70% | draft-in-role mode: the draft replaces the incumbent in memory, absent members are skipped, it refuses `--output`; handoff mode raises ingest warnings to failures | the `--role` and `--handoff` help, or `cp-skill-validate` |
| `relocate-note`, `relocate-directory` | all | nothing; the brief-sidecar behaviour is missing from help | one line in help |
| `promotion-candidates` | about 20% | the output path, ranking by incoming links, what is excluded | the command's help |
| `ingest-handoff` | about 85% | the three `prepare` refusals together; only the last run of an ingest is kept | the `prepare` help |
| `task` | about 50% | exit 1 versus 2; the worker's own report decides nothing | the module docstring, shown as help |
| `analysis` (11 kB) | about 55% | most of the low-level recovery surface: queue exit codes, target fields, `prepare`, `retry`, `acknowledge`, `reset` and `integrate` semantics. The subcommand help is bare usage | one or two sentences per subcommand in help |
| `review` | about 95% | nothing | nowhere |
| `revise` (17 kB) | about 95% | three small refusals | the matching help strings |
| "Generated indexes (no command)" | mechanism is elsewhere | that no rebuild command exists | one sentence in `navigation.md`, or nowhere |

**Stale.** It names a validation schema the code does not emit (`commonplace.validation.member.v1`; the code emits `commonplace.validation.role-draft.v1`). Its account of the rewrite workflow is an older design: source-reconstruction workers, `accept` or `block`, a role report passed as `kb-role`. The code has one writer and `pass`, `warn` or `fail`. One sentence still says "`run revise`".

**A gap in help.** The review CLI module has a 216-line docstring that `--help` does not show; help prints only a one-line description. Most of the `analysis` subcommands have no help description.

**Consumers that must be handled before deletion.**

- `AGENTS.md` points to it as the CLI reference.
- The analysis skill links `#commonplace-analysis` twice, for the batch input format and for low-level recovery. This is the only consumer that depends on unique content.
- `run-review-batches.md` links `#commonplace-review` as the full option reference; help replaces it.
- `cp-skill-health-check` uses the file as a smoke-test target for `commonplace-validate`.
- `test_command_catalogue_integrity.py` requires one `### commonplace-…` heading per published command.
- About 13 see-also links from reference documents, ADRs and proposals.

**Reading.** The operator's position holds: the file can go, once its unique 3 to 4 kB is in help. The reading agent recommended a 2 kB checked catalogue instead. The difference is whether a person needs a page listing the commands; `uv tool list` and help cover that.

## The review guide, `README-REVIEW-SYSTEM.md`

About 75 to 80% of its 63 kB restates `commands.md`, the CLI module docstring, `review-architecture.md` and five instructions. No agent running a review needs all of it. About 8 to 9 kB is unique. The guide agrees with the code better than its duplicates do.

Reader codes: **a** an agent running a review or revision, **b** an operator deciding what to run, **c** a maintainer of the review code.

| Section | Size | Reader | Duplicated | What exists only here | Destination |
|---|---|---|---|---|---|
| intro | 1.6k | b | 80% | review is opt-in; no check runs it | overview |
| Concepts | 9.5k | a for selectors, c | 70% | the "do not conflate" table; tell the operator when a role report lists relied-on terms the brief lacks | selector list to `cp-skill-review`; the table to the overview; rest to architecture |
| Order of concerns | 1.9k | c | values are in each file's `depth:` | the depth table as one view; two type specs link this anchor | architecture, or the edit-operation type spec |
| Result files and freshness | 2.4k | a, c | 85% | results stay on the machine; a pair with rejections is asked alone | two lines to `cp-skill-review` |
| Reading status | 1.7k | a | 90% | five example invocations; current warnings are the fixing queue | `cp-skill-review` |
| Running a gate sweep | 1.5k | a | 95% | nothing | `run-review-batches.md` has it |
| Drafts, evidence and fixtures | 2.1k | c | 75% | two rules for draft criteria | help and architecture |
| Stops, retry and resume | 1.6k | a | 70% | controller failure; the no-progress stop; the bundle job name; a second process exits 2 | `run-review-batches.md` |
| Checkout guard | 1.0k | a, b | 85% | fixture trials are the exception | a sentence in each skill |
| Worker profiles | 0.7k | b, a | 90% | the Bash denial has not been observed to refuse a write | overview |
| Running a review from Pi | 2.8k | b, rarely | none | all of it | its own instruction, or `INSTALL.md` |
| Cost | 0.6k | b | 80% | pair stays the default because quality was not compared | overview; re-measure |
| Planning-free baseline | 1.1k | c | 95% | nothing | delete |
| One edit operation | 2.0k | c | 90% | code does not detect a change outside the items | `try` help |
| Improvement procedures | 11k | a, b | 85% | the procedure table; no procedure checks that an edit fixed its finding; carry-over identity rules | table to `cp-skill-revise` and overview; carry-over to the answers type spec |
| Revise runs and the continuation record | 5.5k | a | 85% | the outcome table; the "left when" table; the stop-to-command table | stop-to-command table to `cp-skill-revise`; kinds table to `continue-a-revise-pass.md` |
| Publication | 4.0k | a, b | 95% | nothing of substance | three sentences in `cp-skill-revise` and overview |
| Rewriting a note | 9.5k | a | 85% | the jobs table; `status` never lists this criterion as missing; the run directory file list | when to rewrite, to `cp-skill-revise`; the rest to the `rewrite.py` docstring |
| Operator-decision record | 1.9k | b, c | 95% | nothing | `decisions` help |
| Interpreting results | 0.4k | a, b | partly | review the diff, not the fixing agent's report | one line in each skill |
| Authoring a gate | 0.5k | c | all | nothing | delete; point to the type spec |

**Stale in the guide.** One sentence still gives `commonplace-review` the edit, improvement, rewrite and decision work that `commonplace-revise` now does. The profile list omits `neon`. The cost figure counts ten `prose` gates; seven exist now.

**Stale in its duplicates**, where the guide is right. `commands.md` describes the older rewrite design. `review-architecture.md` still says "behind one command, `commonplace-review`". `run-review-batches.md` calls critique the one report criterion; there are five. The `decisions` help omits the class `finding`. `AGENTS.md.template` still says "triage, ack, or sweep".

**Proposed skills.** The reading agent outlined both bodies.

- `cp-skill-review`, about 45 lines: what it does; pick the command; before launching, count the stale pairs and tell the operator; what a stopped run leaves; reading results; hand-off to `cp-skill-revise`.
- `cp-skill-revise`, about 60 lines: what may write the note; pick the procedure; it publishes without asking; what a stopped run leaves, with the stop-to-command table; decisions; the held candidate; the write brief; limits.

**Proposed overview for a person**, about 80 lines: what it does, what it may publish, when it needs a decision, what it costs, the "do not conflate" table, and pointers.

**Links that break.** Three anchors: `#order-of-concerns` from two type specs, and `#revise-runs-and-the-continuation-record` and `#rewriting-a-note` from `commands.md`. About 30 file-level links, including 11 ADRs and five redirects in `properdocs.yml`.

## The worked-case group, and the plans, briefs and records

No document in the group should become a general theory note as it stands. Wherever a general claim exists, a theory note already states it and the reference document cites that note. What remains after scoping is Commonplace's own selection or state. This supports the operator's view that generalizing would carry too many assumptions.

"Worked case" mixes three kinds.

| Kind | Documents | Recommendation |
|---|---|---|
| declarations that other notes cite | `commonplace-declared-frame.md`, `source-adoption-policy.md`, the objective stated in `commonplace-as-an-instrument.md`; `epistemic-stance.md` from the authoring group is the same kind | keep together, under a name such as `declarations/` |
| assessments of the repository against a theory, for a human reader | `commonplace-as-an-instrument.md`, `where-change-candidates-come-from-in-commonplace.md` | a worked-case directory |
| one application of a theory to one trace | `tag-readme-trace-as-self-improving-loop.md` | move to `kb/theory/evidence/`, where its two sibling notes already are |
| ordinary system description | `design-rationale-management.md`, `agent-memory-coverage.md`, `collections-never-own-frontmatter-semantics.md` | stay with system reference; merge the last into `collections-and-types.md` |

Per document:

| Document | Current? | Who cites it | Note |
|---|---|---|---|
| `commonplace-as-an-instrument.md` | yes | two proposals cite it as the declared objective; four theory or source notes | about 25% overlap with `design-rationale-management.md` |
| `commonplace-declared-frame.md` | yes | three theory notes and a tag head, as a declaration | under 10% duplicated |
| `tag-readme-trace-as-self-improving-loop.md` | yes; a historical trace | the most theory-linked of the group | about 40% overlap with the reflective-system evidence note (an estimate) |
| `where-change-candidates-come-from-in-commonplace.md` | one stale claim: it calls `kb/log.md` rarely used, and the log has recent entries | the ADR type spec, one proposal, theory notes | a catalogue of local mechanisms |
| `design-rationale-management.md` | yes; two TODOs open | ADR 077, `content-routing.md`, four theory notes | about 30% overlap with `content-routing.md` |
| `source-adoption-policy.md` | mostly; one link label is out of date | five theory notes cite it as the adopted filter; the reference index omits it | the general discriminator is already a theory note |
| `agent-memory-coverage.md` | partly stale: it names status fields the note schema forbids, and an index refresh that no command performs | one theory note, `navigation.md`, the gap plan | needs a refresh |
| `collections-never-own-frontmatter-semantics.md` | one stale example: `source_type` was replaced by `genre` | ADR 045 and proposals use it as a design guard | has a general claim no theory note states; extraction is possible, low value |

**What removal would lose.**

| Document | Verdict | What is lost | Links that break |
|---|---|---|---|
| `commonplace-agent-memory-gap-plan.md` | delete | the eleven-step order with its justification and the done-when criteria. No step shipped as written; unchanged since April; half of it quotes the coverage map | the reference index, one theory note, one ingest |
| `agentic-system-analysis-design-brief.md` | merge, do not delete | five evaluation priorities and the statement that roles and budgets are means, not architecture. They appear nowhere else. `maintain-analysis-method.md` requires reading the brief before a method change | six, including that instruction and the analysis collection contract |
| `harness-sub-agent-model-selection-regression.md` | delete | the job range, the pair count and the dated behaviour table. The lesson survives in code, ADR 127 and a retained audit | ADR 067 and the reference index |

**Reading.** The operator's positions hold with one exception: the design brief is on a route and holds direction that only it records. Its content should move into the instruction or contract that requires it before the file goes.

## Architecture

The operator's hypothesis was that these documents mostly repeat ADRs. It holds for about half the group. It does not hold for the three that matter most, where the current state is several ADRs composed and no single ADR is current.

- **Review.** ADR 127's decision text still describes `run gates`, `run full-pass`, an `approve` command and continuing a run by repeating the command. ADRs 132, 133 and 135 to 139 each replace clauses of it. A reader of ADR 127 alone gets a system that no longer exists.
- **Installation.** ADR 086 still says global types are bare names. The current rule needs ADR 088 on top.
- **What competes with these documents is mostly code docstrings**, not ADRs. The CLI module and the `results`, `gates` and `library` modules already hold much of the current composed state.

So "mostly duplicated from ADRs" is not right. "Mostly recoverable from ADRs plus docstrings, with a few unique rules" is.

| Document | Kind | Reached by | Composition of several ADRs | Single ADR or code | Unique | Stale | Recommendation |
|---|---|---|---|---|---|---|---|
| `architecture.md` | architecture | the reference index, a tag head, about 40 retained analyses that cite it as the baseline; not named in `AGENTS.md` | 20% | 70% (ADR 086, `library.py`) | 10% | omits the `kb/tags/` collection | keep as the seed of one high-level document; shrink the ADR 086 restatement |
| `storage-architecture.md` | architecture | `AGENTS.md`, `navigation.md`, and a code error message that cites one of its headings | 50% | 20% | 25% | none found | keep |
| `review-architecture.md` | architecture at the top; the ownership section has become a behaviour specification | `AGENTS.md`, the review guide, two type specs, ten ADRs | 45% | 50% | under 5% | says "behind one command"; names one entry module; keeps cutover steps | shrink to about 100 lines; add a table of which ADR 127 clauses survive |
| `workflow-architecture.md` | one cross-workflow invariant, 13 lines | the reference index only | none | 60% (ADR 138) | 40% | none | merge into the high-level document |
| `instruction-generation.md` | a code inventory inside a theory-application wrapper | `architecture.md`, a tag head, one theory note | none | 85% (`scaffold_manifest.py`, ADRs 086 and 027) | 15% | omits `kb/tags` and other scaffolded files; cites a superseded ADR (not verified) | delete after moving the unique lines |
| `documentation-site.md` | a publishing contract and checklist, not architecture | the articles contract, `storage-architecture.md` | none | 40% (the docs hook, ADR 025) | 60% | the collection list is incomplete | keep as a focused document outside this group |
| `control-plane-goals.md` | a theory-application note with one real invariant | `cp-skill-connect`, `link-vocabulary.md`, one theory note | none | 80% (the template, `INSTALL.md`, `AGENTS.md`) | one rule | says five subsections where the template has three; calls a shipped section optional | delete after moving the invariant and one table |
| `scenario-architecture.md` | a worked case for a theory note | the theory note it instantiates | none | 90% | a worked example | describes evaluation tooling that was not found | delete; move the step table into the theory note |

**Rules found in these documents and in no ADR or code comment.** These must not be lost:

- editing the root delegation rule must open a recorded search and review of the instructions that commission workers (`control-plane-goals.md`);
- snapshots live in a private repository, collaborators without access work in a degraded mode, and no handover procedure exists (`storage-architecture.md`);
- the landing-page inventory, and that the root README and `kb/index.md` share a lede kept in step by hand (`documentation-site.md`);
- the handoff test: can a fresh process tell what it may do, to which version, and what has already happened (`workflow-architecture.md`);
- the staleness check runs when a command runs, not when an agent reads, so an agent can read the old library root after an install switch (`architecture.md`);
- the "maintenance scope" sections, which say what does and does not require a document edit.

**Proposed shape.** One high-level document with eight sections: surfaces and ownership; reaching the library; identity across source and install; the control plane; storage authority; the code and worker split with coordination between runs; decision chains, naming for each area the ADRs in force and which clauses were amended; and maintenance scope. Two focused documents stay beside it, `storage-architecture.md` and a shrunk `review-architecture.md`, because `AGENTS.md` names both.

**Not verified.** Whether one rule in `review-architecture.md` (when two runs review one pair, the later write stands) appears in an ADR. Whether `kb/reports/state/README.md` still describes the retired full-pass and fix procedures.

## Findings across the groups

1. **Duplication is high, and the duplicate is often the stale copy.** The two manuals are 75 to 90% duplicated. In several cases the reference copy is wrong and the code or help is right: the rewrite workflow in `commands.md`, a schema name, "one command" in `review-architecture.md`, three scaffold inventories. Prose that copies behaviour drifts.
2. **Help is weaker than the prose it would replace.** The review CLI's 216-line docstring is not shown by `--help`. Most `commonplace-analysis` subcommands have no help description. Deleting `commands.md` first requires moving about 4 kB into help.
3. **The current state is not in the ADRs.** For review and installation, an agent that reads only ADRs reads superseded clauses. Something must say which clauses are in force.
4. **A rule is applied when a route or a check carries it.** Each group has rules stated only in a free-standing document: the lineage test, six collision-ledger decisions, the root-delegation search, three routing rows.
5. **Documents the operator would remove have live consumers.** `validation-contract.md` is pinned by code and by the analysis plan. The analysis design brief is a required read in an instruction. A code error message cites a heading of `storage-architecture.md`. A test reads `commands.md`.
6. **Nothing needs to become a new theory note.** One note belongs in `kb/theory/evidence/`.
7. **About 20 concrete stale statements were found** across the 30 documents. They are listed per group above and are fixable independently of any reorganisation.

## Limits of this analysis

Each group was read by one agent, once. Duplication shares are estimates from reading, not measurements. The writer of this file did not re-check line references. Items marked "not verified" were not checked by anyone. `kb/instructions/`, the type specs, `INSTALL.md` and the live proposals were used as comparison points and were not themselves analysed. No session trace was examined, so the claims about what agents read rest on one session and one observation by the operator.
