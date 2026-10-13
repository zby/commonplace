# Accepted partial outcomes and target release

## Decision and scope

The operator asked whether held analyses contain substantial accepted outcomes,
then initially directed release before verification. The operator refined that
direction: leave the six verification-stage holds unchanged and release only
the remaining cases without substantial accepted analysis.
This inventory covers the 17 targets held after rolling-07. "Reached
verification" means the independent `report-verification` model job was opened,
even if its worker failed. Deterministic boundary/report checks are not that
verification stage. Use the latest assigned run, not a predecessor already
designated for replacement.

**Release nine targets to pending, eligible for fresh reruns. Keep the six
verification-stage holds unchanged. Also keep ACE and ai-memex-cli held because
they retain substantial accepted analysis before verification.** Preserve every existing run and its partial outputs.
Release is target scheduling disposition, not permission to resume, alter or
discard a failed run. The reload dispatch stop remains in force; this decision
launches nothing. No recovery method was implemented or exercised.

Academic Research Skills' source-exposure evidence remains a constraint on
source-first execution; release does not waive isolation. ACE's open
reconciliation attempt remains unsettled; its hold and prior-worker-status
requirement remain unchanged. Before assigning a fresh run, reconcile writer ownership
and avoid any overlapping publication destination.

## What is already accepted

Eight targets retain substantial analysis beyond source-boundary work:

| Target | Installed analytical members | Latest stage reached | Disposition |
|---|---|---|---|
| ACE | Runtime, memory, epistemic, workflow | Reconciliation attempt open | Keep held; substantial accepted work and unresolved prior ownership |
| ai-memex-cli | Runtime | Specialist round; epistemic worker failed | Keep held; substantial accepted runtime analysis |
| Archie | Runtime, memory, epistemic, workflow, reconciliation | Report verification failed | Keep held |
| arsumbris | Runtime, memory, epistemic, workflow, reconciliation | Report verification failed | Keep held |
| Auto-claude-code-research-in-sleep | Runtime, memory, epistemic, workflow, reconciliation | Report verification failed | Keep held |
| auto-harness | Runtime, memory, epistemic, workflow, reconciliation | Report verification failed | Keep held |
| AI-Context-OS | Runtime, memory, epistemic, workflow, reconciliation, report verification, memory profile, profile verification | Synthesis failed | Keep held; strongest retained progress |
| Agent Skills for Context Engineering | Historical inspection records runtime, memory, epistemic, workflow, reconciliation, report verification and memory profile | Profile verification failed | Keep held and reserved; current state not inspected |

Boundary is also installed for every target in this table. ACE's four main
reports total about 132 KB; ai-memex-cli's runtime report is about 45 KB.
The four targets stopped at report verification each have four main reports
plus a reconciliation report. AI-Context-OS has passed both independent
verification stages but lacks synthesis/publication.

Six other targets have only an accepted boundary: Academic Research Skills,
Apache Maka, Autocontext, AutoSci, Beever Atlas and Binder. All six are released
for fresh reruns. Their boundary documents are about 15–19 KB each (rounded),
but source inventory is not a completed system analysis.

Three targets have no installed accepted member in the latest assignment:
Agentic Harness Engineering, Amazon Science SAGE and browzy.ai. The first two
failed at boundary; browzy.ai has no discoverable run. All three are released.
Agentic Harness Engineering's older run reached report verification, but the
operator already designated that predecessor for fresh replacement; its latest
replacement failed at boundary. Both worktrees remain preserved.

## Acceptance and inspection limits

"Accepted" here means an engine judgment installed that exact member and its
acceptance was not listed stale by the retained inspection. For the 15
non-reserved runs with known identities, current artifact bytes were compared
against retained member SHA-256 digests. Every installed member matched. Each
had at least one accepted judgment for the same role/version whose identifier
was absent from the retained stale-acceptance list. Historical stale checks were
not counted as current acceptance. Judgment evidence is in each run's
`state/judgments/`; installed Markdown is in `artifact/`.

This is an inventory of preserved work, not a new substantive audit or a proof
that all worker obligations were fulfilled. Many acceptances are deterministic
schema/relation checks, not independent semantic verification. No target has a
published, audited and integrated result from these held runs. Uninstalled
candidate files were not counted as accepted outcomes.

Agent Skills remains reserved to its reported owner. Only its retained
inspection and the existing retrospective were used; no potentially changing
worktree files were read. Its historical membership does not discharge the
retrospective's epistemic/content-validation concerns or certify current state.
ACE's recorded open attempt does not establish current worker ownership.
No commands advanced an analysis, judged a new candidate or launched an agent.

## Evidence locators

The retained inspections identify absolute artifact paths, run identifiers,
member digests, attempts and stale acceptances:

- [Academic Research Skills](./batch-02-academic-research-skills-inspect.json)
- [ACE](./batch-03-ace-inspect.json)
- [Agent Skills](./batch-03-agent-skills-for-context-engineering-inspect.json), with [retrospective](./audits/path-confusion-agent-skills.md)
- [Agentic Harness Engineering replacement](./rolling-05-harness-engineering-inspect.json), with [predecessor disposition](./rolling-04.md)
- [AI-Context-OS](./rolling-05-ai-context-os-inspect.json)
- [ai-memex-cli](./rolling-05-ai-memex-cli-inspect.json)
- [Amazon Science SAGE](./rolling-06-amazon-science-sage-inspect.json)
- [Apache Maka](./rolling-06-apache-maka-inspect.json)
- [Archie](./rolling-06-archie-inspect.json)
- [arsumbris](./rolling-06-arsumbris-inspect.json)
- [Auto-claude-code-research-in-sleep](./rolling-07-auto-claude-code-research-in-sleep-inspect.json)
- [auto-harness](./rolling-07-auto-harness-inspect.json)
- [Autocontext](./rolling-07-autocontext-inspect.json)
- [AutoSci](./rolling-07-autosci-inspect.json)
- [Beever Atlas](./rolling-07-beever-atlas-inspect.json)
- [Binder](./rolling-07-binder-inspect.json)
- [browzy.ai preparation and no-run reconciliation](./rolling-07.md#outcome-browzyai)

Resulting corpus scheduling status: **17 complete, 181 pending, eight held**.
No active assignment or integration backlog. This supersedes the 17-held
scheduling checkpoint, not its historical execution facts or preserved failures.
