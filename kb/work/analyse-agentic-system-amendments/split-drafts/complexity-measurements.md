# Complexity measurements for analyst jobs

Commissioned by the operator on 2026-10-03 to decide between shortening the
`kb/agentic-systems/` contract and splitting analyses into
`kb/agentic-system-analyses/`. Agent-measured. These are judgments under the
rules in [Counting rules](#counting-rules); every item behind a count is listed
in [complexity-measurements.json](./complexity-measurements.json). No run,
model call or workflow step was made.

## Result

The split has a measured complexity advantage over shortening for every
analyst role, but only on one measure, Concerns. Shortening reaches the
same Model-resolved reference counts. On Authority conflicts it falls short of
the split by one conflict per role. That conflict exists only if a permissive
link grammar counts as a conflict.

Primary roles, "incumbent / shortening / split". Incumbent means the current
contract as deployed: root doctrine requires it and packets omit it.

| Role | Concerns | Model-resolved references | Authority conflicts |
|---|---|---|---|
| boundary | 10 / 9 / 4 | 1 / 0 / 0 | 4 / 1 / 0 |
| runtime | 10 / 9 / 3 | 9 / 4 / 4 | 3 / 1 / 0 |
| memory | 10 / 9 / 3 | 9 / 4 / 4 | 4 / 2 / 1 |
| epistemic | 10 / 9 / 3 | 9 / 4 / 4 | 3 / 1 / 0 |

Secondary roles, same order:

| Role | Concerns | Model-resolved references | Authority conflicts |
|---|---|---|---|
| reconcile | 10 / 9 / 3 | 5 / 4 / 4 | 5 / 2 / 1 |
| verify | 10 / 9 / 3 | 6 / 5 / 5 | 4 / 1 / 0 |
| synthesize | 10 / 9 / 5 | 11 / 6 / 6 | 4 / 1 / 0 |
| verify-synthesis | 10 / 9 / 5 | 6 / 5 / 5 | 4 / 1 / 0 |

What these counts establish:

- **Concerns.** Shortening removes one activity of ten, note authoring. The
  split removes five to seven. Neither reaches the proposal's target of zero.
  The split keeps three activities from its own contract: method authoring for
  local types, retained and archive maintenance, and run-state conventions.
  Role files add one or two more that no contract change can remove. The
  boundary job reads publication metadata. The records contract has an archive
  clause. The overview type has publication and comparison-row rules.
- **Model-resolved references.** Shortening equals the split for every role.
  Both remove the same references: the contract lookup (packet entry) and four
  incumbent link and search instructions. Four to six references remain under
  both. They come from the root vocabulary rule and the shared records
  contract, not from any collection contract. They are the largest remaining
  source of references.
- **Authority conflicts.** Both candidates remove the root-rule conflict and the
  incumbent's evidence-line and note-promotion conflicts. Shortening keeps
  one conflict, CF-PRIOR. Its link grammar admits related accounts in
  `kb/agent-memory-systems/` and retained analyses, and the worker rules forbid
  reading them. The grammar permits these links and does not require them. If
  permissive grammar is not counted, shortening equals the split on conflicts.
  Two conflicts are the same under both candidates: memory's blocked-report
  rule against the worker rules, and reconciliation's set-directory link rule.
- **Packet entry alone** (Sol plan item 1 with the full incumbent contract)
  removes one reference and one conflict per role. It leaves all ten concerns.
  Primary roles go to 10 concerns, 0 or 8 references, and 2 or 3 conflicts.

Remaining complexity is in the task, not in the contract. The two
task-intrinsic measures are the same in shortening and the split.

| Role | Output obligations (incumbent / candidates) | Flagged publication or comparison only | Max composition depth (incumbent / candidates where different) | Obligations above depth two (incumbent / candidates) |
|---|---|---|---|---|
| boundary | 16 / 15 | 0 | 4 | 5 / 4 |
| runtime | 41 / 39 | 0 | 3 | 5 / 2 |
| memory | 62 / 60 | 14 | 4 | 10 / 7 |
| epistemic | 51 / 49 | 0 | 4 | 5 / 2 |
| reconcile | 20 / 19 | 2 | 5 | 7 / 7 |
| verify | 14 / 13 | 1 | 4 | 3 / 3 |
| synthesize | 18 / 16 | 2 | 5 / 4 | 4 / 3 |
| verify-synthesis | 11 / 10 | 1 | 5 | 1 / 1 |

The three largest task-intrinsic findings, with uncertainty:

1. **The memory comparison profile is a quarter of the memory job's
   obligations, and only comparison consumes it.** 14 of 60 memory
   obligations serve only cross-system comparison. They are the profile's
   scope, its ten axes, the axis field structure, scope agreement and
   Comparison rationale. No synthesis or overview rule reads the profile.
   Its consumers are `systems_matrix.py`, landscape synthesis and taxonomy
   refresh. The profile check is reconciliation's deepest obligation (five
   files) and one of verification's three deepest. In the records, three
   of the four findings returned to a memory analyst concern profile
   obligations: two in Dynamic Cheatsheet run -02 and one in Graphiti. Moving the
   profile to a coordinator or comparison step is the largest available
   reduction. That is a method change; the proposal does not decide it.
2. **Record grammar is restated across files, and its lexical rules are the most
   frequent observed lapse.** Reconciliation has seven obligations above depth
   two. Amendment, supersession, split, part and unresolved-conflict rules each
   appear in the records contract, the reconciliation type and the job file.
   The no-range rule appears once, in the 13.7 KB records contract. Only the
   two verification job files restate it. Range lapses occurred in the epistemic job (both
   Dynamic Cheatsheet runs), in verify jobs before restatement, and in
   reconcile and synthesize after it. These lapses have depth one or two. I
   infer that salience at the point of writing explains them better than
   composition depth. Two runs on one source cannot test that inference.
3. **Theory and boundary obligations need files the packet does not supply.**
   The four registered definitions in the records contract are required by
   root doctrine and absent from every packet. Synthesis also needs
   `self-improving-system.md`, and verify needs boundary-kind semantics from the
   boundary contract. The one synthesis blocker in run -02 was a missing
   self-improvement assessment. That obligation needs `D:SI`, which the
   synthesizer must look up itself. The boundary's not-allowlist rule
   has depth four. The same rule is stated in the job, the boundary contract,
   the sources contract and the worker rules. The register-fidelity defect that
   survived run -02 concerns this obligation.

Measured versus inferred: all counts are measured under the stated rules. The
links between counts and observed failures are matches by obligation, not
causal attributions. No run loaded either candidate contract. In the two
Dynamic Cheatsheet runs no worker read the incumbent, so no record shows the
contract's content causing an analytical error.

## Inputs and read state

Read between 20:53 and 21:40 +02:00 on 2026-10-03. SHA-256 at first read:

| File | SHA-256 prefix |
|---|---|
| `report-collection-split-proposal.md` | `70fd3814` |
| `split-drafts/shortened-agentic-systems-contract.md` | `81b6d1fe` |
| `split-drafts/analysis-collection-contract.md` | `0dc0fd8f` |
| `split-drafts/contract-coverage-check.md` | `07abfae6` |
| `split-drafts/input-coverage.md` | `1882af13` |
| `split-drafts/input-measurements.json` | `86d038fa` |
| `kb/agentic-systems/COLLECTION.md` | `fb149cfc` |

Role-file hashes equal those in `input-measurements.json` (inputs commit
`2b7fe749`). Packet code: `src/commonplace/lib/agentic_workflow.py` at the
working tree of that commit. Outcome sources: [fresh-run audit](../fresh-run-audit.md),
[second-run audit](../second-run-audit.md),
[Sol run follow-up plan](../sol-run-follow-up-plan.md) and the two
trace-evidence files. Raw traces and run state were not read.

## Counting rules

**Mandatory input.** For a role and candidate, the mandatory input is:

- the job instruction;
- the read-first files that `AnalyseAgenticSystem.job()` adds for that role;
- the candidate's collection contract;
- the root `AGENTS.md` clauses that bind writers.

Under the incumbent, the contract is mandatory by `AGENTS.md` L138 although
the packet omits it. Under both candidates, the packet supplies the contract
as read-first, as `contract-coverage-check.md` and `implementation-plan.md`
specify. Task inputs (boundary, members) are data. They count only where a
rule makes the worker derive something from them. File abbreviations are in
the JSON `files` map: J job file, W worker rules, B/S/R boundary/sources/records
contracts, RT/MT/ET/CT/OT member types, C collection contract, A `AGENTS.md`,
`D:*` definition notes, LV link vocabulary.

**Concerns.** Count distinct activities, not clauses. An activity counts when
the mandatory input gives at least one rule for doing it and the role does not
perform it. The ten activities are A1 to A10 in the JSON. Not counted:

- statements that only tell the worker what to omit or who owns a task, because
  they govern the worker's own output;
- assembly mentions without a rule;
- `AGENTS.md` rules for other activities. About ten such groups (commits,
  tests, tags, mailbox and others) apply to every role in every candidate.
  The JSON lists them under `root_doctrine_concerns_constant`; they cannot
  differ between candidates.

**Model-resolved references.** Count each reference the worker must resolve to
act on a rule that applies to its own output. The three kinds are:

- a rule naming a file the packet does not supply;
- a path the worker must derive;
- a definition reachable only by a link.

A registered `AGENTS.md` term used technically counts, because `AGENTS.md`
L51-52 requires reading its linked definition. An unregistered linked term
counts only when the loaded text gives no usable definition. Not counted:

- links to files already in the packet;
- conditional routes whose condition never arises for the role;
- permissive link grammar.

**Authority conflicts.** Count pairs of loaded instructions that give different
answers to one question about this role's output, so the worker must choose. A
constraint enforced only by a validator is not a loaded instruction. I list
such constraints but do not count them.

**Output obligations.** Count one obligation per:

- required frontmatter field;
- required section or block;
- record kind's field set;
- controlled vocabulary;
- named cross-record or format constraint.

Conditional record fields and theory properties count once each. Consumers
are the downstream readers named in the inputs or code. The flag marks an
obligation whose only terminal consumer is publication or cross-system
comparison.

**Composition depth.** For each obligation, count the rule-bearing files the
worker must combine: method files, the collection contract when it states part
of the requirement, and definition notes that root doctrine requires.
A pointer that only routes to another file counts zero. Task data files and
`AGENTS.md` writing style are excluded from depth. The data files would add one
to three to cross-record obligations in all candidates alike.

## Measures per role

### Concerns

| Activity | Incumbent | Shortening | Split | Role files (all candidates) |
|---|---|---|---|---|
| A1 publication | L89-90, L99-131 | L35-38 | — | boundary J L16, L25 (`opening`); OT L52, L56-57 (synthesis roles) |
| A2 comparison reading | L9-15, L89-90, L128-130, L135 | L39-41 | — | OT L56-57 (synthesis roles) |
| A3 review/ordinary accounts | L22-23, L106-108, L117-118, L163-164, L173, L175-177 | L15, L36-37, L45-49, L75, L77-79 | — | — |
| A4 comparison writing | L23-24, L174 | L15-16 | — | — |
| A5 method authoring | L19-21, L26-74 | L14-20, L49-50, L56-57, L80 | L16, L32-34, L43 | — |
| A6 migration | L92-97 | L30-33 | — | — |
| A7 retained/archive | L85-90 | L27-30 | L20-22 | R L24-26 (all roles but boundary) |
| A8 transfer state | L159 | L61-62 | — | — |
| A9 run lifecycle | L78-83 | L22-25 | L15-16 (run state) | — |
| A10 note authoring | L172 | — | — | — |

Not counted as concerns, as stated mentions: memory J L89-90 ("publication
checks them again"), MT L15 (profile authoritative), memory J L44-45 (no
comparison needed), and the assembly mentions in the boundary, epistemic and
verify inputs. The proposal names `opening` and memory's publication mention.
I count `opening` because it makes the worker read publication metadata. The
memory mention is not counted because it governs the analyst's own checking.

### Model-resolved references

| ID | Roles | Candidates | Reference |
|---|---|---|---|
| REF-COLL | all | incumbent | `AGENTS.md` L138 needs the target `COLLECTION.md`; the packet omits it, so the worker derives the path |
| REF-TB, REF-AT, REF-RF, REF-ER | all but boundary | all | Registered terms theory builder, addressable theory, representational form and explanatory reach (R L115, L193, L211, L218-221); definitions not in any packet |
| REF-SI | synthesize, verify-synthesis | all | OT L87 self-improving link, no inline definition |
| REF-BK | verify | all | whole-system and coverage-table semantics in B L40-57, not in the verify packet |
| REF-SETLINK | synthesize | all | member links resolved from a retained directory that does not yet exist (J L48-49) |
| REF-INC-LINKNOTES, -SEARCHNOTES, -SCANREF, -LV | runtime, memory, epistemic, synthesize | incumbent | incumbent L157, L172, L176, L168 |

### Authority conflicts

| ID | Roles | Candidates | Pair |
|---|---|---|---|
| CF-READ | all | incumbent | `AGENTS.md` L138 against the packet list and W L36-40 (do not reconstruct paths). `AGENTS.md` L157-158 offers a third reading |
| CF-PRIOR | all | incumbent, shortening | incumbent L173-174 or shortening L75-76 link grammar against W L141-153 prior-analysis prohibition |
| CF-PROMOTE | all | incumbent | incumbent L172 (promote a claim to `kb/notes/`) against W L51-60 write scope |
| CF-EVLINE | boundary, reconcile, verify, synthesize, verify-synthesis | incumbent | incumbent L135 evidence-basis line against "exactly these sections" grammars |
| CF-SETLINK | reconcile | all | contract `kb/notes/` link grammar against CT L51-52 set-directory links |
| CF-BLOCKED | memory | all | MT L29-36 blocked report against W L36-41 problem report |

Not counted, listed as a validator-only constraint: every contract, including
the split draft (L38, L41), permits local links to `kb/sources/` or
`kb/notes/`. `agentic_set_member_link_failures` refuses any local link that
leaves the set directory for runtime, memory, epistemic, reconciliation and
synthesis outputs.

### Output obligations and composition depth

The JSON `obligations` lists every obligation with its sources, files, consumer
and flag. The incumbent adds two obligations to each record-declaring analyst
and one or two to other roles: the evidence-basis line and the link to defining
notes. It also adds itself as a file to up to five theory obligations per analyst,
to boundary's evidence tier and to synthesis's theory statements.
The candidates differ only in which contract line states the native-operation
and transfer-exclusion rules. Both rules have the same depth under both
candidates.

Obligations above depth two under both candidates:

- boundary: disposition (3), Boundary and evidence (3), Source register (3),
  not-allowlist (4).
- runtime: Runtime account (3), guarantee fields (3).
- memory: component and object fields (3 each), `representational_form` axis
  (3), axis field structure (3), Boundary and evidence (4), Read-back (3),
  Integration issues (3).
- epistemic: object fields (3), Source-and-claim boundary (4).
- reconcile: amendment, supersession, split, part, missing part, unresolved
  conflict (3 each), profile check (5).
- verify: record verification content (3), profile check (4), problem versus
  blocker (3).
- synthesize: theory statements (4), organization (3), amended records (3).
- verify-synthesis: type conformance (5).

Flagged obligations: memory's 14 profile obligations (comparison).
Reconciliation's and verification's profile checks (comparison).
Reconciliation's set-directory links and synthesis's set-directory links
(publication or retention move). Standalone readability in synthesis and
verify-synthesis (publication; the stated reason is the generated review). No
boundary, runtime or epistemic obligation is flagged.

## Interference check

`contract-coverage-check.md` counts 12 rule groups without a worker-output
decision in shortening and 3 in the split. Every group it lists is present
in the drafts as described. It misses some groups.

| Candidate | Audit | Missing, not foldable | Granularity only | My count |
|---|---:|---|---|---:|
| Shortening | 12 | layout migration (L30-33); run method commit (L24-25); retained naming and new-run correction (L27-28); comparison-reader rules and trial clearance (L39-41); local retained-analysis links (L76) | reviews/comparisons placement (L14-16); validation marker (L22-23); instruction-authoring conventions (L49-50); ordinary descriptions (L48-49) | 17 at audit granularity, 21 at mine |
| Split | 3 | local-type link rule (L43); area roles (L26-27) | retained frozen (L20-21), foldable into the archive row | 5 at audit granularity, 6 at mine |

Clauses addressing other artifact classes, counted by sentence or list item.
Routing exclusions that govern the worker's own omissions are not counted.

- **Shortening: 27.** L14, L15-16, L16-17, L17-18, L19, L20 (two), L24-25,
  L27-28, L35, L36 (two), L36-37, L37-38, L40, L40-41, L45, L46-47, L48-49,
  L49-50, L56-57, L61-62, L75, L77, L78, L79, L80.
- **Split: 4.** L6, L15-16, L33-34, L43. All four concern run state and local
  types, which the split collection itself owns.

Neither count is zero, so the proposal's rule prefers the split. The split's
residual can move to type specs. The shortening's residual needs a new route
for reviews, comparisons and method rules.

## Literal-path check

From `agentic_workflow.py` L744-820 and `workflow/job.py` and
`workflow/engine.py`:

- The prompt names the job instruction literally ("Follow <path>").
- Read-first is worker rules plus the role's extras, as absolute paths.
- Task inputs are absolute paths.
- All three groups are in `Job.inputs`. `engine.input_state` hashes their
  bytes through `_files_state`.

Inputs that do not reach the worker as literal paths or do not participate in
hashes:

| Input | Literal path | Hashed | Candidates affected |
|---|---|---|---|
| Collection contract | no | no | incumbent as deployed. Both drafts specify read-first and hashed inputs; code is not changed |
| `AGENTS.md` | no (harness-loaded) | no | all |
| Registered definitions TB, AT, RF, ER | no | no | all record roles |
| `self-improving-system.md` | no | no | synthesis roles |
| Boundary contract for verify | no | no | verify |
| Member schemas (`*.schema.yaml`) and overview schema enums used by validators | no | no (validators are outside input state by design) | all; the fresh-run runtime worker read a schema to repair |
| Run state | literal parameter | no (explicitly mutable, L760) | all |
| Frozen checkout | literal parameter | no (pinned by commit, not bytes) | all |
| Link vocabulary | no | no | incumbent analysts and synthesis (L157 makes linking mandatory) |
| Method maintenance | no | no | conditional route; correct by design for workers |

The split additionally changes the type paths that `TYPES` builds. Those stay
literal and hashed once the constants change.

## Outcome baseline

Sources: the fresh-run audit (run -01, 13 sessions), the second-run audit
(run -02, 17 sessions) and the Sol plan (Graphiti run -05, stopped). Counts
are failures named in those records. They are not complete error censuses.

| Role | Refused submissions | Self-validation failures | Failed reads or paths | Returned findings against the role | Rules read, not applied | Survived publication |
|---|---|---|---|---|---|---|
| boundary | 0 | 0 | -05: quote batch key | 0 | -02: truncated read not reread | -01: whole-system label over an allowlist; -02: register overstates inspection |
| runtime | 0 | -01: 1 draft (headings, order) | -02: duplicated scratch path | 0 | -01: type template headings | — |
| memory | -02: 1 (quote altered) | -01: 2; -02: 2 (delimiter; 6 part fields, validation pending) | -05: contract guessed path, guessed source path, empty quote | -02: 2 profile support; -05: decay axis, combined property parts | Part of grammar (-01, -02, first repair reintroduced it); validation pending (-01, -02) | -02: duplicate identity MEM-OBJ-1 |
| epistemic | 0 | -01: 2; -02: 1 | -01: malformed selection JSON (2 commands), non-verbatim selection; -02: `/tmp` selection; -05: contract guessed path, guessed source path | -01: EPI-OBJ-8 containment; -02: evaluator file outside coverage; -05: identifier, ledger and claim-column amendments | ranges (-01, -02); controlled route-function values (-01, -02); scratch rule (-02) | — |
| reconcile | -02: 1 (range) | not recorded | 0 | -01: missed containment (verifier blocker) | range (-02) | -02: duplicate identity missed by 3 rounds |
| verify | -01: 2 (ranges) | n/a | -01: reconstructed type path, fabricated source path, 2 duplicated-segment reads | 0 | ranges (-01) | -02: duplicate identity missed by 2 verifiers |
| synthesize | -02: 1 (range) | n/a | -01: workdir missing slash | -02: missing self-improvement assessment | range (-02) | — |
| verify-synthesis | -01: 1 (ranges) | n/a | -01: JavaScript syntax error | 0 | ranges (-01); truncation recovery incomplete (-01 retry) | — |

All sessions in -01 and -02 also returned `r.output` instead of the complete
command result, against W L66-97.

Matches to the measures, where supportable:

- **Model-resolved references.** REF-COLL matches the two Graphiti wrong-path
  reads exactly, and CF-READ matches the 30 Dynamic Cheatsheet sessions that
  skipped the contract. Both candidates as designed remove both. The other
  path failures were transcription errors of literal supplied paths, so
  literal supply does not prevent every path failure.
- **Concerns and the remaining conflicts.** No record matches them. No Dynamic
  Cheatsheet worker loaded the contract. The Graphiti analysts read it whole,
  but the plan records no consequence. CF-BLOCKED was never exercised. The
  records are too thin to test whether concerns degrade analyst output.
- **Output obligations.** Lexical lapses fall on depth-one and depth-two
  obligations: no-ranges, route-function values, Part of grammar, validation
  pending, template headings and quote literalness. Semantic findings fall on
  depth-three-and-above or flagged obligations:
  - containment and identity: REC-partof, REC-supersession, VER-content;
  - profile support and decay: MEM-axis-fields, curation axis (flagged);
  - coverage: EPI-block1, BND-not-allowlist;
  - theory: SYN-theory.

  The duplicate identity also involves MEM-overlap (depth two). This split is
  an observation over three runs and one model family per run. It is not a
  test.

## Deviations and limits

- **Incumbent variants.** The incumbent is reported as deployed, with the
  contract mandatory but unsupplied. The Result also gives incumbent plus
  packet entry. Alternative: count only packet-supplied files for the
  incumbent. Its concerns would then fall to 1-3 per role, below both
  candidates, and CF-READ would remain. The proposal and coverage check reject
  omission as a saving, so I did not use this reading.
- **Concerns unit.** I counted activities, as the measure says. Counting
  clauses instead gives the interference-check numbers: 27 for shortening, 4
  for the split. Treating `opening` as data rather than a publication rule
  lowers boundary by one in every candidate.
- **Permissive link grammar.** I counted CF-PRIOR as a conflict. Not counting
  it makes shortening equal the split on all three measures for boundary,
  runtime and epistemic. Memory would then be 1/1 on conflicts. Concerns would
  still differ.
- **Definition references.** I counted registered definitions as references
  because `AGENTS.md` L51-52 requires reading them. Not counting them lowers
  references by four for record roles in all candidates. It does not change
  the comparison.
- **Root doctrine in context.** I did not verify from traces that `AGENTS.md`
  was in every worker's context; I relied on the proposal's statement.
- **Composition depth** excludes task data and counts definition notes only
  where root doctrine requires them.
- **Obligation granularity** is my choice: for example, one obligation per
  memory axis, and one per record kind. Another reasonable granularity would
  change totals, not the candidate comparison. The candidates differ by the two
  incumbent-only obligations alone.
- **Graphiti run** used a different model and worktree, and its code changed
  during the run. Its correction worker's malformed YAML frontmatter is not in
  the outcome table because the plan does not name that worker's role; the plan's
  pointer to the memory job suggests the memory correction round.
- **Not verified.** Both candidates' packet changes (read-first entry and
  hashing) exist only as drafts. Validator behaviour on links was read from
  code and not exercised.
