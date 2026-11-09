---
description: "Commit-bound comparison of 243 current agentic-system analyses: memory admission, read-back, curation and trace-fed updates, with existence counts, grounded mechanisms and explicit coverage limits"
type: types/note.md
traits: [has-comparison, has-external-sources]
tags: [agent-memory]
---

# What the 243 current agentic-system analyses show about agent memory mechanisms (November 2026)

The current accepted analyses connect memory to more than reference retrieval.
Retained information also selects work, ranks candidates, gates admission and
feeds later updates. This snapshot compares those mechanisms at one frozen
evidence boundary. It asks how information enters memory, reaches later work,
is revised and changes through recorded activity—not which product is best.

Four contrasts organize the findings:

- **Admission:** 221 of 225 code-grounded sets wire at least one automatic
  admission mechanism. Explicit human content decisions are wired in 63;
  another 55 support manual admission only through claims or affordances.
  Starting a workflow is not approval of each resulting memory item.
- **Read-back:** both requested retrieval and unsolicited context supply are
  extensively wired. Inferred relevance is not required for context supply:
  availability, chronology and identifiers also select what reaches a model.
  Selection must be distinguished from delivery and actual reliance.
- **Curation:** revision, compression and forgetting have many recorded
  implementations. Creating a claim absent from the inputs—`synthesize` in
  this comparison—has only 12 strong system witnesses. Calling a model or
  naming an operation “synthesis” does not establish semantic novelty.
- **Trace-fed updates:** the same `trace_learning: "yes"` classification
  includes access counters, retained mistake-prevention rules and trained
  weights. These change different material and reach different consumers.
  The shared classification is not an ordering of capability or benefit.

These are **existence counts**, not prevalence estimates. They count systems
with a supported mechanism even when the rest of the inventory remains
unresolved. They do not establish how often the mechanism runs or works.

## Evidence boundary

- **Mode and selection:** current snapshot, all 243 accepted sets under
  `kb/agentic-system-analyses/retained/`, with no review filter. The successful
  builder supplies current membership and source-identity selection. Legacy
  reviews, archives, local runs, transfer advice and upstream sources supply
  no findings here.
- **Inputs commit:** `bf2da04db03fb4cb60be52d1bb04e638a79eda79`. It holds the
  retained members, contracts, reader and [synthesis instruction](../../instructions/synthesize-agent-memory-landscape/SKILL.md).
  Relevant input paths were clean and unchanged from that commit before
  writing. Output paths are not evidence inputs.
- **Matrix identity:** the successful `scripts/build_systems_matrix.py` build,
  without a review filter, recorded SHA-256
  `19da70a6ca54b9c659dd9d1bf734e5f46885325d48f58b40685eccea083ce0bc`.
  Its row identities, including manifest hashes, are the provenance used here.
  The public [memory matrix](./memory-systems.csv) and table are separately
  maintained outputs, not additional evidence.
- **Population and revision:** 225 code-grounded and 18 doc-grounded sets.
  All 243 profiles use `comparison_version` 2. Revision 2 measures human
  content-admission decisions, not generic caller identity; no revision-1
  write-agency values are pooled with it.
- **Boundary kinds:** code-grounded sets comprise 193 whole-system, 27
  complete-artifact/partial-loop and 5 subsystem-only boundaries. The
  doc-grounded split is 4, 12 and 2. Whole-system inclusion does not imply
  exhaustive inspection of every path.
- **Source cutoffs:** 2026-10-11 through 2026-11-09. Individual cutoffs and
  reviewed source revisions remain in the query ledger; this is not a
  simultaneous observation of deployed products.
- **Lens:** the ten axes of the [memory profile contract](../../../agentic-system-analyses/types/agentic-system-memory-profile.md).
  Units retain their scope, coverage, evidence basis and canonical records.
- **Verification:** local checking of selected retained members, profile units,
  canonical records and reconciliations. Selected directories were validated
  before reading members; the matrix builder validates population membership.
  Quantitative claims use the retained query output. No independent reviewer
  was commissioned.

## How to read the evidence

A **strong witness** has basis `wired`, `observed` or `causally supported` in a
code-grounded profile. `wired` means inspected code connects a mechanism, not
that it ran successfully. Each system counts once per value, regardless of
how many stores or routes support it. Both `known` and `partial` axes can
support a positive witness. **Weak-only** means that a value is present only
at `claimed` or `afforded` basis in that system; it is not added to the strong
count.

Missing values and unresolved units are not negatives. An `absent` assessment
needs bounded evidence. `inapplicable`, `uninspected` and `not-determinable`
are different limitations, not observed absence. A strong witness for one
unit does not upgrade a weaker unit with the same value.

### Complete-value distributions remain withheld

Answering “what share is pull-only?” requires `known` axis coverage and strong
evidence for **every** positive unit finding, not just the strongest witness
for each union value. Few code-grounded sets qualify:

| Axis | Eligible sets (of 225) |
|---|---:|
| Storage substrate | 36 |
| Representational form | 20 |
| Read-back signal | 17 |
| Read-back direction | 11 |
| Behavioral authority | 6 |
| Write agency | 2 |
| Curation operations | 1 |
| Trace learning | 1 |
| Lineage; trace source | 0 |

These assessed subsets do not stand in for the whole population. This snapshot
therefore gives no complete-value distribution or whole-population percentage
for any axis. Even a set with only files among its strong storage findings
need not be a files-only system: weak or unresolved alternatives remain.

<a id="every-positive-finding-is-static-wiring-or-weaker"></a>

### Wiring dominates; the observation exception is narrow

The 225 code-grounded profiles contain 9,379 `wired`, 849 `claimed`, 820
`afforded` and 2 `observed` findings. The 18 doc-grounded profiles separately
contain 43 `wired`, 567 `claimed` and 22 `afforded` findings. Neither tier has a
`causally supported` finding.

Both observed findings concern **llm-wiki-newsroom's experiment artifacts**:
natural-language judgments and symbolic score/manifest fields at a later
analysis consumer. The [experiment-ledger object](../../../agentic-system-analyses/retained/alfadur7--llm-wiki-newsroom/epistemic.md#epi-obj-experiment-ledger)
and [judge-measurement route](../../../agentic-system-analyses/retained/alfadur7--llm-wiki-newsroom/epistemic.md#epi-rte-judge-measurement)
retain sampled labels and scores, not an independently authenticated
production memory run. The reference labels are model judgments; hidden
scorer/questions and missing originals limit replication and attribution.
The observations do not establish deployed memory activation, improved
answers or a reviewer-family effect.

## Strong existence counts by axis

Every count below has denominator **225 code-grounded sets, revision 2**.
Counts overlap across values. Weak-only columns show selected frequent gaps;
the ledger retains every value and every excluded run.

| Axis | Axis assessment | Strong existence counts | Selected weak-only counts |
|---|---|---|---|
| Storage substrate | partial 168, known 56, not-determinable 1 | files 204, in-memory 107, sqlite 77, vector 60, repo 45, graph 34, rdbms 34, service-object 16, kv 14, model-weights 7 | repo 16, files 5, service-object 4 |
| Representational form | partial 195, known 30 | symbolic 221, natural-language 209, parametric 100 | natural-language 14, parametric 3, symbolic 3 |
| Lineage | partial 224, known 1 | other-compiled 212, imported 200, trace-extracted 176, authored 131 | authored 48, trace-extracted 23 |
| Behavioral authority | partial 209, known 15, not-determinable 1 | routing 211, knowledge 204, enforcement 190, ranking 183, validation 175, learning 151, instruction 116 | instruction 45, learning 31 |
| Write agency | partial 222, known 3 | automatic 221, manual 63 | manual 55, automatic 4 |
| Curation operations | partial 223, known 2 | evolve 184, consolidate 153, decay 134, invalidate 113, dedup 79, promote 59, synthesize 12 | consolidate 42, evolve 31, dedup 24 |
| Read-back direction | partial 196, known 29 | pull 216, push 179 | pull 9, push 7 |
| Read-back signal | partial 166, not-determinable 21, known 19, uninspected 10, inapplicable 9 | coarse 171, identifier 131, inferred-lexical 44, inferred-embedding 36, inferred-judgment 25 | coarse 5, identifier 3, inferred-judgment 2 |
| Trace learning | partial 187, not-determinable 36, known 1, uninspected 1 | yes 160; local unit no in 6, system-union no in 1 | yes 26 |
| Trace source | partial 176, not-determinable 47, inapplicable 1, uninspected 1 | session-logs 107, tool-traces 97, event-streams 46, trajectories 25 | session-logs 24, tool-traces 16 |

**Storage is not representation.** Files have strong witnesses in 204 sets;
123 wire at least one database-type substrate (sqlite, rdbms, vector, graph or
kv). A set can occur in both counts. In 36 sets files are the only *strongly
reported* substrate, not necessarily the only substrate. Text, fixed-rule
metadata and dense numerical representations can coexist within one store.

**Authority is consumer-relative.** Retained material supplies reference
knowledge, but it also routes, ranks, validates and enforces. Those values do
not imply that retained prose itself has veto power: symbolic state consumed
by code and advice interpreted by a model are different paths. Instruction
has 116 strong witnesses and 45 weak-only witnesses, illustrating the gap
between requested standing guidance and a traced consumer.

<a id="write-admission-automatic-is-near-universal-manual-is-often-instructed-not-wired"></a>

## Admission: human decisions, model proposals and software gates differ

Manual admission appears at some basis in 118 of 225 code-grounded sets. It
has a strong witness in 63 and only weak support in 55. These are positive
memberships, not a count of systems lacking human control. Of 1,250
write-agency units, 302 are `not-determinable` and 124 `uninspected`; a generic
API caller often leaves the content decision unresolved.

**CQ separates instructed approval from handler enforcement.** Its shipped
skill makes user approval a precondition of interactive `propose`. The
[approval claim](../../../agentic-system-analyses/retained/mozilla-ai--cq/runtime.md#rt-clm-proposal-approval)
classifies this as policy with afforded implementation. The
[proposal route](../../../agentic-system-analyses/retained/mozilla-ai--cq/runtime.md#rt-rte-knowledge-proposal)
checks structure and credentials, not approval; headless guidance permits
model judgment under separate conditions. This does not establish a universal
human gate, nor does a generic direct call establish automatic authorship.

**cass_memory_system wires a real but scoped human decision.** The
[trauma-admission route](../../../agentic-system-analyses/retained/dicklesworthstone--cass_memory_system/memory.md#mem-rte-trauma-admission)
asks whether to add a displayed candidate batch to a permanent safety
blocklist. That batch decision supports manual admission. Generic add/import
callers remain unresolved, while other reflection and curation writes can be
automatic. The human branch does not certify every future memory write.

**pi-self-learning shows why invocation and admission must be separated.**
Automatic task-end reflection and `/learning-now` use the same
[proposal/parse/write route](../../../agentic-system-analyses/retained/mcollina--pi-self-learning/runtime.md#rt-rte-task-reflection).
A model receives selected branch activity and proposes mistakes/fixes;
software accepts nonempty parsed lists and writes journals and derived rules.
Manual invocation does not make each generated item manually admitted.
Structural admission can reject malformed output without detecting a
plausible false lesson. No prevention benefit is observed.

<a id="read-back-push-usually-selects-coarsely"></a>

## Read-back: unsolicited supply need not infer relevance

Pull has strong witnesses in 216 of 225 sets; push in 179. Here **pull**
fulfills a consumer's request for retained material. **Push** selects and
supplies retained material without that request. Delivery by code alone does
not make a requested result push.

Among the 179 strong push sets, 71 also have a strong inferred selector
(lexical, embedding or model judgment). The other 108 have strong
coarse/identifier signals but no strong inferred finding. Partial coverage
and weak alternatives prevent calling those 108 exclusively coarse systems.
Only 4 sets establish a complete, strongly evidenced pull-only direction
inventory. A relevance-ranked pull result is not evidence of relevance-based
push.

Three routes expose distinct selection and consumption boundaries:

- **Hindsight:** a `UserPromptSubmit` hook derives a recall query from the
  prompt, filters scores and emits formatted retained text as
  `additionalContext` ([RT-RTE-claude-hooks](../../../agentic-system-analyses/retained/vectorize-io--hindsight/runtime.md#rt-rte-claude-hooks)).
  The [profile](../../../agentic-system-analyses/retained/vectorize-io--hindsight/memory-profile.md)
  records embedding and cross-encoder-judgment selection for this route,
  while keeping unresolved retrieval arms and other integrations separate.
  Emitted context is not evidence of host reliance or complete transcript
  delivery.
- **A-MEM:** new-note ingestion supplies up to five embedding-selected
  retained neighbors to its own evolution model, which can revise links,
  tags and contexts ([RT-RTE-neighbor-evolution](../../../agentic-system-analyses/retained/wujiangxu--a-mem-sys/runtime.md#rt-rte-neighbor-evolution)).
  This push consumer maintains memory; it is not an answering agent.
  Partial mutation and uncertain snapshot refresh prevent a universal
  synchronized-read guarantee.
- **pi-self-learning:** the next-agent-start hook selects available core and
  optional dated files, plus recent process notes. Selection follows flags,
  chronology, counts and prefix caps, not the user's query
  ([RT-RTE-context-injection](../../../agentic-system-analyses/retained/mcollina--pi-self-learning/runtime.md#rt-rte-context-injection)).
  Long-term memory is named by path rather than automatically bundled.
  Later sections can disappear under character caps; process notes have a
  separate cap boundary. “Strict” consultation requests are not enforced
  reads.

These examples distinguish the selector, selected retained part, actual
recipient and surviving payload. Storage availability does not guarantee that
all reasons or conditions reach the next consumer. The focused
[read-back comparison](./read-back-mechanisms.md) examines that question in
more detail.

<a id="curation-revision-and-forgetting-are-common-synthesis-is-rare"></a>

## Curation: changing retained content does not certify new knowledge

Revision (`evolve`) has strong witnesses in 184 of 225 sets; consolidation in
153, decay in 134 and invalidation in 113. There are 147 sets with three to
seven strong operation values. These memberships describe recorded
transformations, not exhaustive maintenance inventories.

The 12 strong `synthesize` witnesses are Agent-R, cass_memory_system, deja-vu,
DocMason, eal-bench, Engraph, Kompl, LACP, Sparks, Swamp, VLM-wiki and Zikkaron.
Another 8 sets support that value only weakly. Under the contract, synthesis
creates a claim absent from its inputs; extraction, compression, index
rebuilding and requested model behavior do not alone establish it.

In **cass_memory_system**, harmful feedback crossing a threshold can turn an
eligible positive playbook rule into a new avoidance rule and deprecate the
original. The [curator-inversion record](../../../agentic-system-analyses/retained/dicklesworthstone--cass_memory_system/epistemic.md#epi-rte-curator-inversion)
gives the code deduction `Use cache` → `AVOID: cache. Marked harmful 3 times`.
This is policy synthesis, not accepted causal knowledge that avoiding cache
works. Synthesis need not involve model inference.

Conversely, **Signet's aggregate recall** requests model-authored notes and
can save eligible output by default without a maintenance pass
([MEM-RTE-aggregate-recall](../../../agentic-system-analyses/retained/signet-ai--signetai/memory.md#mem-rte-aggregate-recall)).
It links evidence, deduplicates or refreshes a note and attempts embedding;
prior aggregate notes are excluded from aggregate searches to limit recursive
reuse. But its [save guard](../../../agentic-system-analyses/retained/signet-ai--signetai/epistemic.md#epi-rte-aggregate-guard)
checks evidence eligibility and output surface form, not proposition-level
entailment. [Retention](../../../agentic-system-analyses/retained/signet-ai--signetai/epistemic.md#epi-rte-aggregate-retention)
can survive embedding failure, and an unsaved result can still be returned.
The profile supports deduplication and evolution without inferring semantic
novelty from the “synthesis” prompt. Recall here can write memory; neither
saving nor source linkage confers a truth warrant.

Revision and withdrawal also have consumer-specific horizons. Changing a
current row does not by itself retract already delivered context or external
copies. The focused [correction comparison](./correction-propagation.md)
separates those propagation mechanisms; no population frequency follows from
the examples selected here.

<a id="trace-learning-widely-wired-uneven-in-depth"></a>

## Trace learning: one classification, different durable changes

Trace learning in this profile means automatic trace-fed writes producing
durable behavior-shaping artifacts or learned parameters. It does not require
new knowledge or observed improvement. There are 160 strong `"yes"` witnesses
among 225 code-grounded sets, plus 26 weak-only witnesses. Session logs,
tool traces, events and trajectories supply different update inputs; their
strong memberships are 107, 97, 46 and 25 respectively. These values can overlap
and do not inventory every source in a partial boundary.

Four strong `"yes"` sets also wire model-weight storage: AgentFly,
Amazon Science's SAGE, Self-Training-LLM and SkillRL. This co-occurrence does not classify every
learning route in those systems as weight training. The retained records are
needed to distinguish what changes:

- **REM changes selection metadata.** Retrieval asynchronously increments a
  durable count that can add a capped bonus to later rankings
  ([MEM-OBJ-retrieval-count](../../../agentic-system-analyses/retained/satyammistari--rem/memory.md#mem-obj-retrieval-count)).
  This is use-fed feedback, not a checked outcome or model training.
  Its proposed semantic write-back is a different route: the shipped Go
  router lacks the accepting endpoints
  ([RT-ABS-writeback-routes](../../../agentic-system-analyses/retained/satyammistari--rem/runtime.md#rt-abs-writeback-routes)).
  A local learning `"no"` for that branch coexists with a system `"yes"`
  from the counter and other wired paths. Updates can fail silently; no
  ranking improvement is observed.
- **pi-self-learning changes retained advice.** Selected session activity
  becomes mistakes/fixes, journals and scored rules for later context. Its
  structural gate does not evaluate whether the lesson prevents recurrence.
  This route is distinct from REM's fixed numerical ranking feedback and
  from provider parameter training.
- **SkillRL changes instructions and parameters on separate routes.**
  [Validation failures](../../../agentic-system-analyses/retained/aiming-lab--skillrl/runtime.md#rt-rte-validation-admission)
  can produce new skills admitted to a training bank after structural checks.
  The proposer receives bounded failure excerpts and titles, not full bank
  principles. Separately, [reward-driven policy updates](../../../agentic-system-analyses/retained/aiming-lab--skillrl/runtime.md#rt-rte-policy-update)
  change actor parameters. Bank persistence/resume and numerical checkpoint
  recovery are not one coupled guarantee. Neither route establishes better
  later actions here.
- **A-MEM prevents an invalid inference from automatic revision.** Neighbor
  evolution is automatic, but the original input is not established as an
  activity trace. Its trace-learning axis remains `not-determinable`.
  A [bounded absence](../../../agentic-system-analyses/retained/wujiangxu--a-mem-sys/memory.md#mem-abs-usage-feedback)
  establishes that shipped paths do not update usage/history fields; it does
  not rule out caller-supplied experiences or all trace-fed writes.

### Local negatives and a bounded system negative

Six sets retain a strong local unit `"no"`: EchoWiki, ModularRSI, Phantom, REM,
secure-llm-wiki and team-ai-workflows. Only **team-ai-workflows** has a known
whole scoped learning inventory supporting the system-union `"no"`.
Its [absence record](../../../agentic-system-analyses/retained/umezy--team-ai-workflows/memory.md#mem-abs-trace-update)
covers all shipped corpus acquisition, lookup and access-maintenance paths:
search reads files and prints results; synchronization changes access links;
no automatic query/answer/feedback-to-retained-content route is shipped.
Manual experience-derived authoring, external host/provider updates and
adopter additions remain outside that negative.

The other five local negatives do not become system-wide absence. A `"yes"`
elsewhere or unresolved included coverage prevents that inference. Likewise,
the 36 `not-determinable` and one `uninspected` code-grounded learning axes are
not negative observations.

The broad `"yes"` category cannot answer whether counters, summaries, rules or
weight updates produce greater benefit. Selected records support the
contrasts above. Population counts by those finer mechanisms would require a
systematic classification with unresolved cases retained, not classification
by missing prose mentions.

## Doc-grounded tier: designs remain distinct from implementation

The 18 doc-grounded sets are AgeMem, aide2, arsumbris,
claude-code-dynamic-workflows, context-constitution, From Agent Memory to
Portable Skills, incremental-self-improvement, interview-doc-agent,
IsaacCLupus_mnemosyn_spec, llm-context-base, llm-project-wiki, nimbalyst-wiki,
pm-llm-wiki, Prove2Me_workspace, recall (parcha-skills), sig-releases,
trajectory-informed-memory-generation and wikiskill. Thirteen carry claimed
trace-learning `"yes"` findings, none a strong `"yes"`. They do not enter the
225-set implementation counts.

A doc-grounded boundary can contain narrow code-inspected or executable
configuration findings: the tier is the account's overall evidence boundary,
not a basis assigned uniformly to every finding. The ledger retains all 43
`wired` labels in this tier without promoting the documented systems to
code-grounded or assuming successful execution.

Two designs illustrate what the tier can contribute without that promotion:

- **AgeMem** describes conversation-to-store updates, replacement summaries
  consumed by later invocations and GRPO policy updates. The canonical
  [store-maintenance](../../../agentic-system-analyses/retained/2601-01885v1/memory.md#mem-rte-store-maintenance),
  [summary](../../../agentic-system-analyses/retained/2601-01885v1/runtime.md#rt-rte-context-summary)
  and [policy-update](../../../agentic-system-analyses/retained/2601-01885v1/runtime.md#rt-rte-policy-update)
  records support these as claimed design from the captured paper, not
  inspected executor behavior. Summary fidelity, checkpoint lineage and
  production loading remain unresolved. A shared trajectory score does not
  identify the contribution of each memory action.
- **Nimbalyst Wiki** prescribes capturing decisions, rejected alternatives
  and reasons from sessions into subject pages, then reading a few full pages
  because reasoning surrounds the marks
  ([RT-RTE-session-capture](../../../agentic-system-analyses/retained/nimbalyst--nimbalyst-wiki/runtime.md#rt-rte-session-capture),
  [RT-RTE-wiki-recall](../../../agentic-system-analyses/retained/nimbalyst--nimbalyst-wiki/runtime.md#rt-rte-wiki-recall)).
  Ordinary additions are agent-admitted without per-edit approval; destructive
  changes have separately scoped approval rules. CLI, host and service
  implementations are external to the frozen plugin. This supports a
  claimed trace-fed path and whole-page recall policy, not verified
  persistence, compliance or prevention of decision reversals.

## Example provenance

Member links above name supporting sections and canonical IDs. The following
identities come from the frozen matrix's manifest fields.
Full source identities, reviewed revisions, member paths and hashes also
remain in the ledger. Hashes identify `ARTIFACT.yaml`, not an upstream source
commit. Each example uses the accepted member at the inputs commit.

| Example | Run ID | Manifest SHA-256 |
|---|---|---|
| A-MEM | `AAS-2026-10-16-a-mem-sys-eff95cd80440-01` | `16fad56f4a88e833d4c0f5ffa129af99bca8a0383acbd6799d2dc99b28cd2f28` |
| cass_memory_system | `AAS-2026-10-13-cass-memory-system-30c18219cf68-01` | `2dcdb811124058cacf2dcde3b50b127dc826f2a8e603fb06ef92531b910c4729` |
| CQ | `AAS-2026-10-14-cq-8fb3dc41c334-01` | `8d2fcd66aa8707273424c810f716e9203b9f7c90be7296a5b1a10666c7d415aa` |
| Hindsight | `AAS-2026-10-14-hindsight-34c2ca821edf-01` | `3e9e67f75bff2a28a6ffc32ceb894615058008641f960da1e24bc9d70fb38579` |
| llm-wiki-newsroom | `AAS-2026-11-08-llm-wiki-newsroom-ea04687a5ff6-01` | `f16203ad8057cd9261819ac693dfc60e5eadd949f04f1afb80834032daf05bf0` |
| pi-self-learning | `AAS-2026-10-15-pi-self-learning-1a318610d4b1-01` | `903a6b625bf0d805a25d222dec241e857cf9bf8d0fe8677b009ff5e1832e0984` |
| REM | `AAS-2026-10-14-rem-a81fdc774400-01` | `0e45470aeb4b227b6deb7877ab75e9cc4db0199c9c6cf5aa590506243d3a3dee` |
| Signet | `AAS-2026-10-14-signetai-64f703d83203-01` | `4eb6367fe3884963d0c083b7c276bef866a089d4bcc8a1f0680bf1d7401bece9` |
| SkillRL | `AAS-2026-10-14-skillrl-0dba0e1c895e-01` | `9771fa25ae76ce88c6efdfc88fb4e126b1abe0bd3fac23ae510761d4acb361f4` |
| team-ai-workflows | `AAS-2026-11-09-team-ai-workflows-c00fb85f7ed1-01` | `3bbf81f1b11585b33fbc615ee2c7dcc994fee3f77782075805ecba7cd11b7c40` |
| AgeMem | `AAS-2026-10-12-2601-01885v1-32274e5bddc1-01` | `ec5ef488e3864432af6583e3410daeba596badd0839a85b58c257f4f7322306e` |
| Nimbalyst Wiki | `AAS-2026-11-08-nimbalyst-wiki-d9ff54186a76-01` | `0d48a874284207505fa604f5447fc3c1798179c57f4b9a10110f08cf90562a4f` |

## Withheld conclusions and evidence gaps

- **Prevalence, exclusivity and rankings:** incomplete inventories prevent
  population shares or claims such as “only pull,” “no human control” or
  “files only” from missing positive witnesses. Named mechanisms establish
  examples, not prevalence of unstructured properties.
- **Activation and benefit:** wiring, delivery, model instructions, retained
  scores and experiment artifacts do not by themselves establish successful
  deployed use or improved task outcomes. No profile finding is causally
  supported.
- **Semantic novelty and warrant:** generated prose can compress, derive or
  invent. Without proposition-level input/output evidence, a model call does
  not settle which. Structural admission and provenance are not truth tests.
- **Consumer completeness:** truncation, optional context paths, separate
  stores and residual copies limit universal fidelity and withdrawal claims.
  No cross-system correction-coverage rate is inferred.
- **Retained-set limits:** partial units, opaque dependencies and verification
  limits remain operative. CQ and cass_memory_system retain coarse-part
  declaration issues outside the selected admission/inversion mechanisms;
  pi-self-learning retains a registration-count disagreement, not a disputed
  reflection route. Those issues are not repaired or silently generalized
  away here.
- **Source-byte verification:** selected validation logs include notices that
  some pinned source checkouts are unavailable for quotation checking. This
  synthesis checks committed accepted records, not upstream source bytes;
  it makes no fresh quotation-authentication claim or population-wide count
  of those notices.
- **Change over time:** this is one current snapshot. Counts do not establish
  growth, adoption trends or improvement relative to an older population.
  Historical outputs remain separate and are not pooled.
- **Commonplace advice:** design recommendations and transfer judgments are
  outside this public comparison.

## Query ledger

Executable queries and dated outputs are retained in
`scripts/memory_landscape_queries/`. `refresh.py` uses the existing unit decoder
and strong-basis helper. Its `outputs-2026-11-09/snapshot.json` records revision
and tier strata, field names, tests, basis filters, numerator, denominator,
included runs and exclusions. Every assessment category is retained separately.
`evidence.py` extracts selected committed record sections and profile units
for semantic checking; it acquires no upstream evidence.

| Query family | Membership or coverage test | Published use |
|---|---|---|
| Population | revision/tier split; boundary-kind and cutoff census | Evidence boundary |
| Axis existence | any strong unit witness for value; each system once | Ten-axis table |
| Weak-only | value present, no strong unit witness | Ten-axis table and admission contrast |
| Complete eligibility | known axis; every positive unit finding strong | Withheld distributions |
| Basis census | every finding, separately by tier | Wiring/observation boundary |
| Manual admission | manual at any basis versus strong | 118 / 63 / 55 of 225 |
| Push selection | strong push with any strong inferred signal; separately no strong inferred signal | 71 / 108 of 179 push sets |
| Complete pull-only | known direction, strong set exactly pull, every finding strong | 4 of 225 |
| Storage | strong files set exactly `{files}`; any strong database-type substrate | 36 reported strong-only files; 123 with database witness |
| Curation | any strong synthesize; three to seven strong operation values | 12; 147 of 225 |
| Trace learning | strong yes/units; local no retained apart from system unions; strong yes plus model-weights | 160 yes; 6 local no; 1 system no; 4 weight co-occurrences |

The query results come from the frozen matrix; smoke checks cover ledger
structure and membership consistency. Historical `outputs-2026-10-22/` remain
separate; this snapshot makes no numerical change claim against them.
