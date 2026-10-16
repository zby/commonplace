---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "LLM Project Wiki runtime baseline: model-mediated bootstrap, wiki-first use, source sync, diff ingest and existing-vault repair."
run-id: AAS-2026-10-14-llm-project-wiki-c6c664168f3e-01
reviewed-boundary: "1fdfba9129a46afd18aa68a83f12d6716ab694c6"
---

# LLM Project Wiki runtime report

## Runtime account

The shipped system is a prompt package, not an executable wiki service. The user pastes `SETUP_PROMPT.md` into Claude Code at a consuming project's root. The host model is asked to create or repair files, including the commands and instructions used by later sessions. Both tracked files were read completely at the frozen commit; all source findings below use SRC-1's doctrine/design layer unless explicitly marked otherwise. No target execution was performed. Generated installations, host execution, activation and benefit remain unobserved, as specified in [the boundary](boundary.md#boundary-and-evidence).

### Ordinary bootstrap invocation

The user is the initiating principal; the project root supplies the filesystem scope, and the model infers the project identity and vault path. There is no shipped run identifier or transaction coordinator. The first branch checks for `Obsidian Vault/`: a missing directory selects [RT-RTE-vault-bootstrap](#rt-rte-vault-bootstrap); an existing directory selects [RT-RTE-gap-audit](#rt-rte-gap-audit). The instruction permits later placement adjacent to or inside the root, so the literal detection path is not evidence of universal existing-vault discovery (SRC-1, `SETUP_PROMPT.md`, Step 0 and Phase 1).

On the new-vault branch, the foreground model reads project instructions, existing memory and directory structure, answers five project-audit questions, then scaffolds Sources, Wiki, Templates, schema, index, log and health dashboard. It generates a project-adapted sync script and ingest command, is instructed to run sync, builds pages domain by domain, writes wiki-first rules into project instruction files, modifies optional status/milestone callers, sets tracking conventions, and finishes with a bootstrap log and self-audit. The next-step owner remains the host model; numbered phases and natural-language quality rules supply the decision policy. Filesystem and shell effects are exercised through the excluded Claude Code host, not through a shipped enforcement engine. The terminal product is the generated vault and support files, not a provider-returned structured result (SRC-1, `SETUP_PROMPT.md`, Phases 0–6).

The prompt requests parallel reading and scanning but specifies no delegated worker identities, isolated contexts or return aggregation. Selected-page loading is the explicit working-context mechanism in later use. It reduces requested raw-source reading by putting the index and compiled pages first; it does not specify trimming, host compaction or eviction. Project instruction loading and actual window contents remain host-dependent (SRC-1, `SETUP_PROMPT.md`, Phases 0, 4 and G3).

### Continuing work and alternate routes

[RT-RTE-wiki-lookup](#rt-rte-wiki-lookup) is the later question/edit path. A model uses the Semantic Lookup table, reads selected pages, and answers without raw-source reads where sufficient. An insufficient wiki permits source fallback and gap logging. A targeted edit permits source access and requests stale marking through a `source_file:` grep. `/status` adds another page-first consumer; `/phase-complete` requests stale marking and a sync reminder. These are generated instruction channels, not demonstrated callbacks that run after every host edit (SRC-1, `SETUP_PROMPT.md`, Phase 4).

[RT-RTE-source-sync](#rt-rte-source-sync) is a separate shell route, explicitly invoked by a user after significant commits or by the bootstrap model. It changes Sources, not the compiled Wiki. [RT-RTE-diff-ingest](#rt-rte-diff-ingest) then asks the model to select changed paths using Git, locate dependent pages with grep, read source and page, update changed sections and dates, resolve logged gaps and log the operation. The read-back design thereby joins shell copying to later model admission. It supplies no scheduler proving that either stage occurs after every edit (SRC-1, `README.md`, Ongoing maintenance; `SETUP_PROMPT.md`, Phases 2 and 4).

Three forcing cases qualify the strongest claims:

1. **Existing vault:** the setup skips the initial build and uses Phase G to patch pages, scripts and instruction wiring. This alternate route permits codebase scans and direct source reads, so wiki-first is not a universal source-access prohibition. It also permits manual copying into Sources (SRC-1, `SETUP_PROMPT.md`, Step 0 and G0–G7).
2. **Sync without successful copying:** the embedded pattern suppresses errors and appends `|| true` for memory, rules and design-doc copies, then prints completion. Its shell shape does not guarantee source completeness or freshness. G2's inventory/timestamp audit provides a separate requested recovery path (SRC-1, `SETUP_PROMPT.md`, Phase 2 and G2).
3. **Diff ingest and dry-run:** `git diff HEAD~1 --name-only` selects one Git comparison, not all stale pages or all unsynced changes. A stale page whose source does not appear in that comparison has no guaranteed refresh through this selector. Dry-run is specified as steps 1–2 only, while page mapping by grep is step 3; therefore the requested preview need not establish the full page-level write set. Phase G is the broader reconciliation route (SRC-1, `SETUP_PROMPT.md`, Phase 2 and G3).

These are source-text challenges, not observed failures. Complete reads of the two-file package found no shipped direct provider call, callback implementation, extension runtime, subprocess orchestrator or durable worker engine. The specified shell snippets and generated commands are material alternate effect paths. Their host permissions, concrete generated behavior and run outcomes remain outside the supplied evidence, not proven absent from installations.

### Guarantees and effect boundary

The capability surface requested by the prompt includes project reads, shell execution, vault writes and modification of project rules/commands. The current grant set is uninspected because no host session or permission configuration is supplied. The deployed isolation envelope is likewise uninspected; neither the Sources label nor vault placement is a sandbox. There is no basis here for attributing host approvals, delegation controls or provider-native tools to the package (SRC-1, `README.md`, Usage; `SETUP_PROMPT.md`, Phases 1–5).

| Load-bearing promise | Owner and enforcement point | Strength and covered paths | Alternate path / required external contract | Separate conclusions |
|---|---|---|---|---|
| Wiki is the primary reference | Host model interpreting generated CLAUDE.md/GEMINI.md rules; Phase 4 and G6 request wiring | policy; ordinary question/edit flow and optional status caller | Source fallback, audit and bootstrap intentionally read other material; requires host instruction loading and compliance | design conclusion status: claimed; operation conclusion status: uninspected |
| Sources are read-only to the LLM | Host model interpreting layer rules; README architecture | policy; ordinary compiled-page authoring | Bootstrap asks the model to run a copying script; G2 permits manual copy. Immutability cannot mean no filesystem changes. Requires disciplined separation of source reference and Wiki edits | design conclusion status: claimed; operation conclusion status: uninspected |
| Archived instruction copies are non-authoritative | Generated shell header on three Docs copies, then model interpretation | policy; Sources/Docs/CLAUDE.md, GEMINI.md and AGENTS.md | Rules/ and Memory/ copies have no such header in the example. Header insertion is not a host instruction-priority barrier | design conclusion status: claimed; operation conclusion status: uninspected |
| Code edits mark pages stale; ingest repairs them | Model follows grep and status-edit instructions, then operator/model runs sync and ingest | protocol; pages matching the documented path and selected later updates | Non-matching metadata, edits outside compliant sessions and broader history are not covered; requires correct mapping, Git state and subsequent invocation | design conclusion status: claimed; operation conclusion status: uninspected |
| Vault has valid schema and connected coverage | Bootstrap self-audit, Phase G checks, optional Dataview dashboard | best effort; requested inspections and fixes | G5's snippet checks only type/updated/status presence, not the required sources field or full frontmatter validity; requires model inspection beyond the snippet and plugin behavior | design conclusion status: claimed; operation conclusion status: uninspected |

Supporting claims and passages are retained in [RT-CLM-wiki-first](#rt-clm-wiki-first), [RT-CLM-sources-immutability](#rt-clm-sources-immutability) and [RT-CLM-audit-completeness](#rt-clm-audit-completeness). [RT-CMP-claude-code](#rt-cmp-claude-code) bounds model fixity. Admission and recovery are described per route below; memory-content revisions are left to the memory analysis.

## Shared records

### Components

#### RT-CMP-claude-code
Label: Claude Code model-mediated executor

Source-native identity: Claude Code, with Claude as the instructed executor; Gemini is an optional future instruction consumer. The language-model part is distributed-parametric, stored in provider-managed numerical parameters, with a host-mediated filesystem/shell interface whose implementation is excluded. SRC-1 names neither an exact model version nor parameter-update behavior. Parameters changing during operation: uninspected — provider internals are not supplied. Exact version pinned: no model pin in the package. Mutable endpoint resolving to another model: uninspected — no endpoint or provider routing configuration is supplied. These uncertainties prevent model-specific reproducibility, not analysis of the shipped instruction paths (SRC-1, `README.md`, Usage and Supported Stacks; `SETUP_PROMPT.md`, Your Task).

> The only requirement is that you are using **Claude Code** (the CLI or IDE extension).
> --- `README.md`

### Operative objects

#### RT-OBJ-setup-prompt
Label: Setup prompt

Source-native identity: `SETUP_PROMPT.md`. Natural-language procedural guidance with symbolic code examples, stored as tracked Markdown in the frozen Git source. The pasted message is current invocation input, not accumulated read-back. Its model-consumed text selects and guides generation; snippets describe possible shell effects rather than constituting a separately shipped runtime (SRC-1, `SETUP_PROMPT.md`).

> **How to use:** Paste this entire prompt into a Claude Code session opened at your project root.
> --- `SETUP_PROMPT.md`

#### RT-OBJ-schema
Label: Generated schema and maintenance conventions

Source-native identity: `schema.md`, a specified generated Markdown file in the vault. Its prose is natural-language maintenance policy; named frontmatter keys are symbolic data only where a fixed consumer such as a query checks them. Concrete content and schema enforcement are not shipped. The prompt requires page types, linking, code excerpts, operations, cadence, tags and log grammar; later maintenance is asked to read it first (SRC-1, `SETUP_PROMPT.md`, Phase 1 and G0).

> The governing document. A future LLM maintaining this wiki must read it first. It must define:
> --- `SETUP_PROMPT.md`

#### RT-OBJ-wiki-ingest
Label: Generated ingest command

Source-native identity: `.claude/commands/wiki-ingest.md`, a specified generated Markdown command file in the consuming project. Natural-language workflow and shell-command text guide a future model; shell fragments have symbolic execution semantics if passed to the host. Storage is a project file, not a command implementation shipped here. Its path does not establish host discovery or successful command activation (SRC-1, `SETUP_PROMPT.md`, Phase 2).

> ### Create `.claude/commands/wiki-ingest.md`
>
> Diff-based ingest workflow. Must document:
> --- `SETUP_PROMPT.md`

### Routes

#### RT-RTE-vault-bootstrap
Label: New-vault bootstrap

Endpoints/progression: user-pasted setup → directory detection → project audit → vault/support-file generation → initial sync → page build → project rule/command changes → log and self-audit. Owner: foreground host model under user initiation. Context includes project rules, memories, tree and source snapshots; action effects include project and vault writes plus requested shell execution. There is no specified transactional admission boundary (SRC-1, `SETUP_PROMPT.md`, Step 0 and Phases 0–6).

- design conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Generated vault, project support files and bootstrap log are requested; no fixed response envelope is specified.
- Later read-back: Generated pages, schema, index and rules are intended for later question and maintenance sessions.
- Delegated visibility: uninspected — parallel reads are requested but no worker handoff or isolated context protocol is defined.
- Selection predicate: Missing literal Obsidian Vault directory selects bootstrap; audit-derived domains and entity rules select pages.
- Invalidation or expiry: Later code edits should mark corresponding pages stale; source sync and ingest repair them.
- Activation or effect: Requested filesystem creation and instruction wiring; execution and subsequent behavior are not supplied.
- Evidence limits: Only the generation specification is present, not generated files, host traces or tested output.

Admission: model proposes and writes project-specific pages, scripts and rules using the supplied phases and existing project conventions. The user starts the workflow and is told afterward to commit; this is not per-content approval. No separate veto stage is specified. The host's ability to refuse writes is uninspected. Recovery is a later gap audit; no atomic rollback is specified. Mode: open project-specific construction, not a bounded experiment. Improvement trigger: missing vault. Answer oracle: no supplied expected output; project sources and audit questions are references to inspect, not an independent correctness oracle.

> **Do not proceed until you can answer all five.**
> --- `SETUP_PROMPT.md`

> 4. Commit the resulting Obsidian Vault/ directory to your repo
> --- `README.md`

#### RT-RTE-wiki-lookup
Label: Wiki-first question and edit

Endpoints/progression: project question/edit request → index intent table → Wiki pages → answer or targeted edit; insufficient coverage → source/memory fallback → gap note; code edit → page-path grep → stale marking. Owner: foreground model interpreting generated project rules. Context is requested page content, then fallback content if needed. The retained-effect boundary includes gap log and status changes; source edits remain consuming-project effects (SRC-1, `SETUP_PROMPT.md`, Phase 4).

- design conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Answer or completed project task, with requested stale/gap bookkeeping where applicable.
- Later read-back: Gap entries should reach ingest and audit; stale flags reach maintenance, status fallback and health queries.
- Delegated visibility: inapplicable — no delegated consumer is specified in this flow.
- Selection predicate: Model maps question/intent through Semantic Lookup and judges sufficiency; path grep selects pages after an edit.
- Invalidation or expiry: Code edits request status: stale; no automatic timeout or expiry is specified for answers.
- Activation or effect: Page-first decisions and bookkeeping are requested, not observed.
- Evidence limits: Generated rules and host instruction loading are not supplied; wiki correctness and actual source avoidance are unverified.

Admission: model judges coverage and writes gap/stale bookkeeping. There is no per-entry human approval rule. Guidance is the quoted fallback/stale protocol and the generated schema; no explicit rejection/rollback mechanism is specified. Mode: open user tasks. Trigger: insufficiency or code edit. Answer oracle: none supplied for model sufficiency judgment. Optional `/status` and `/phase-complete` callers use related page-first or stale-marking instructions, not an independently enforced route.

> **When the wiki is insufficient:**
> - Do the work using source as fallback
> - After completing the task, update memory per sync rules
> - Append a gap note to `<vault path>/log.md`:
> --- `SETUP_PROMPT.md`

#### RT-RTE-source-sync
Label: Project-to-Sources sync

Endpoints/progression: operator/bootstrap invocation of generated `scripts/sync-vault.sh` → rsync memory/rules/root/design docs → prepend warning to selected Docs copies → completion message. Shell is the executor; model adaptation and project paths determine the concrete script. State is project files, destination timestamps and header text. The example is symbolic Bash stored inside the prompt; concrete generated Bash is unavailable (SRC-1, `SETUP_PROMPT.md`, Phase 2).

- design conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Example prints a completion message asking for /wiki-ingest.
- Later read-back: Updated Sources copies are intended inputs to later ingest or audit, not necessarily consumed by sync itself.
- Delegated visibility: inapplicable — the example copies local files and defines no delegated worker.
- Selection predicate: Listed memory/rules/docs globs and existing root docs; rsync --update governs destination replacement.
- Invalidation or expiry: Later source changes require another invocation; copying does not itself refresh Wiki pages.
- Activation or effect: Requested filesystem copy and header insertion; the final print does not prove all copies succeeded.
- Evidence limits: Embedded example only; generated path adaptations, permissions and command results are unavailable.

Admission: once invoked, example shell rules admit selected copies without per-file human review. Human-authored and model-authored project content can both be copied; their provenance is unresolved for any installation. The header change is fixed software transformation, not semantic validation. Copy failures can be suppressed; G2 prescribes comparison and resync/manual copy as recovery. No versioned rollback is specified. Mode: operational sync, not an experiment. Trigger: initial build or later project updates. Answer oracle: inapplicable — no comparison against expected copied-content outcomes is specified.

> rsync -av --update .claude/memory/*.md "$VAULT_DIR/Sources/Memory/" 2>/dev/null || true
> --- `SETUP_PROMPT.md`

> echo "Sync complete. Run /wiki-ingest to propagate changes to Wiki/ pages."
> --- `SETUP_PROMPT.md`

#### RT-RTE-diff-ingest
Label: Diff-based ingest

Endpoints/progression: generated slash command invocation → Git changed paths → Sources mapping → grep-dependent Wiki pages → model section updates → open-gap resolution/new pages → ingest log. Host model owns selection interpretation and revisions, with Git/grep supporting candidate discovery. The command is requested Markdown guidance rather than inspected executable orchestration (SRC-1, `SETUP_PROMPT.md`, Phase 2).

- design conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Updated pages and ingest log; dry-run instead prints a would-be update list without edits.
- Later read-back: Revised Wiki pages reach later lookup; ingest/gap records reach later maintenance.
- Delegated visibility: inapplicable — no delegated execution or visibility contract is specified.
- Selection predicate: git diff HEAD~1 --name-only, project-to-Sources mapping, reference grep and open gaps; new entities can add pages.
- Invalidation or expiry: Updates bump updated:; exact status-reset logic is not specified in the seven-step list.
- Activation or effect: Requested knowledge revisions; delivery to later consumers and changed behavior remain unobserved.
- Evidence limits: No generated command or run verifies coverage; the one-commit selector is not a general freshness guarantee.

Admission: model proposes and admits section/page changes guided by changed source, current page, schema and gap entries. The user can choose dry-run, but the package specifies no post-preview approval gate and no per-change veto. Recovery/rollback of wrong updates is not specified; Phase G offers broader repair. Mode: open operational maintenance. Triggers: sync, stale-session start or merges according to the required schema cadence. Answer oracle: no independent expected revision is supplied; source content is a reference for model judgment.

> 4. Read changed source → read wiki page → update only changed sections → bump `updated:`
> 5. Check `log.md` for open `[gap]` entries and resolve them
> 6. Create new wiki pages for any new entities introduced by the changed sources
> 7. Append ingest entry to `log.md`
> --- `SETUP_PROMPT.md`

> Also document `dry-run` mode: steps 1–2 only, no edits, print would-be update list.
> --- `SETUP_PROMPT.md`

#### RT-RTE-gap-audit
Label: Existing-vault audit and repair

Endpoints/progression: existing-vault detection → schema/log/index reads → support wiring → source inventory/timestamps → code/wiki coverage → link/index checks → frontmatter checks → protocol wiring → audit log. Owner: foreground model; shell examples aid diagnosis but do not decide all repairs. Persistent effects include pages, Sources copies, scripts, commands and instruction rules. Context includes existing vault conventions, prior log and actual project evidence (SRC-1, `SETUP_PROMPT.md`, G0–G7).

- design conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Surgically patched installation and audit log with issues found/resolved.
- Later read-back: Changed rules/commands guide later sessions; repaired pages/index support lookup; schema and audit records remain available to maintenance.
- Delegated visibility: uninspected — parallel scans are requested without specifying separate workers or their returned material.
- Selection predicate: Existing vault; missing wiring, missing/outdated sources, uncovered/stale entities, unresolved links, schema violations and incomplete loop instructions.
- Invalidation or expiry: Timestamp comparisons and stale flags trigger repairs; repeated audits can revisit the installation.
- Activation or effect: Requested revision of knowledge and behavior-guiding support files; actual deployment and use are not demonstrated.
- Evidence limits: Checks are examples, not a complete validator; no audit run, generated fix or measured improvement is supplied.

Admission: model diagnoses, proposes and directly patches. G0 uses existing schema and records to avoid rediscovering deferred work. Templates guide page creation; the setup's architecture, heuristics and wiring checklist guide other revisions. User initiation and later committing fixes are separate from admission; no mandatory human approval of individual fixes or independent veto is specified. Existing content must not be rebuilt wholesale; no transaction or rollback mechanism is given. Mode: open repair against a checklist, not a curriculum or controlled experiment. Trigger: vault already exists. Answer oracle: shell checks and source comparisons expose reference evidence but no comprehensive expected-result oracle; model judgment supplies coverage and repair decisions.

> Run this phase when a vault already exists. Your job is to find everything that is missing, stale, broken, or not wired up correctly — then fix it. Work through each category below in order. Do not rebuild from scratch; patch surgically.
> --- `SETUP_PROMPT.md`

> For any source file that exists in the project but NOT in `Sources/`: run `sync-vault.sh` or manually copy it. If `sync-vault.sh` doesn't cover a file path it should, fix the script.
> --- `SETUP_PROMPT.md`

Method-revision assessment: this route can revise the installation's script coverage and behavioral instructions, not just external project documentation. It applies localized operational propositions such as wiki-first lookup and the stale/sync/ingest chain, and asks for structural criticism of missing parts. It does not prescribe testing the truth of the overarching wiki-first premise or retaining a claim/result/blame criticism of that premise. The repaired method files and audit summary persist; later use is intended but not observed.

- theory-builder conditions 1–4: condition 1 conclusion status: claimed — localized maintenance rules are required in generated files; concrete formulated content is unavailable. Condition 2 conclusion status: claimed — audit decisions are instructed to depend on schema and protocol content. Condition 3 conclusion status: uninspected — wiring-gap repair does not itself establish content-directed theoretical criticism with result and blame. Condition 4 conclusion status: uninspected — retained fixes/logs do not establish a subsequent criticism-dependent round.
- Addressability: required schema bullets and numbered rules make intended parts separately inspectable; actual generated granularity is uninspected.
- Persistence: files and logs target problems/sessions; actual persistence and later consumption are unobserved.
- learning: uninspected — improved future capacity and its attribution are not demonstrated by the prescribed repairs.
- Reflection: claimed — G1/G6 ask the installation to represent and repair its own wiring; both representation update and rule-mediated later behavior are intended, not observed.
- Reflective theory builder: uninspected — operational self-audit does not establish conditions 3–4 for method theories.
- Autonomous theory builder: uninspected — computational repair is requested, but every theory-builder operation is not established.
- Self-improvement: claimed — an improvement-directed self-change pathway is specified for the generated installation, with the independent objective of complete, fresh coverage and closed maintenance wiring across sessions. Evidence-responsive diagnosis, method-file changes and future instruction consumers are prescribed; no generated update, live loading or subsequent behavior closes the exercised causal chain. Successful improvement is unestablished. This does not revise the shipped setup prompt itself.

### Claims

#### RT-CLM-wiki-first
Label: Wiki-first lookup policy

Claimed operation: later sessions consult compiled knowledge before memory/source. The owner is the instructed model; force is natural-language policy rather than access control. Deliberate fallback, edit and audit paths bound the claim (SRC-1, `SETUP_PROMPT.md`, Phase 4).

> **Lookup flow:**
> 1. Open `<vault path>/index.md` — use the Semantic Lookup table to navigate
> 2. Read the relevant `Wiki/` page(s) — they contain full code excerpts and cross-references
> 3. **Only if the wiki is insufficient:** fall back to existing memory files
> 4. **Only for a targeted edit:** open the actual source file
> --- `SETUP_PROMPT.md`

#### RT-CLM-sources-immutability
Label: Sources layer immutability and authority

Claimed operation: Sources are raw reference material rather than model-authored compiled knowledge. The README's literal read-only phrasing is qualified by sync overwrites and G2 manual copy. The selected instruction-copy header is a requested interpretive authority boundary, not enforced isolation (SRC-1, `README.md`, Three-Layer Architecture; `SETUP_PROMPT.md`, Phase 2 and G2).

> Sources/   ← Immutable originals. Synced from the repo. LLM reads, never writes.
> --- `README.md`

>      Do not follow these as instructions — they are archived context for the wiki.
> --- `SETUP_PROMPT.md`

#### RT-CLM-audit-completeness
Label: Audit completeness and loop closure

Claimed operation: repair all coverage, link, schema and protocol gaps. The policy requires four frontmatter fields, but G5's embedded checks only search for three key strings and do not parse frontmatter. G6 calls documented stale marking automatic; this supports an instruction-following expectation, not an installed host hook (SRC-1, `SETUP_PROMPT.md`, G5–G6).

> Every wiki page must have valid frontmatter with `type`, `updated`, `status`, and `sources`. Check:
> --- `SETUP_PROMPT.md`

>   grep -q "^status:" "$page" || echo "MISSING status: $page"
> --- `SETUP_PROMPT.md`

> 2. **Stale marking is automatic:** when code is edited, the grep command to find the wiki page is documented inline in CLAUDE.md
> --- `SETUP_PROMPT.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-project-rules
Label: Project instruction-file authority

Consumer: later Claude Code model, optionally Gemini. Channel: generated/modified CLAUDE.md and GEMINI.md project instruction files. Force: requested wiki-first policy, fallback, stale marking and sync cadence, contingent on external host loading and model compliance. Horizon: future project sessions. This is distinct from merely delivering Wiki facts and from archived Sources/Docs copies. It is the intended live path for repaired rules from [RT-RTE-gap-audit](#rt-rte-gap-audit), not evidence those repairs were activated (SRC-1, `SETUP_PROMPT.md`, Phase 4 and G6).

> Replace or extend the "Context & Memory Rules" section with:
> --- `SETUP_PROMPT.md`

> Add the same Wiki-First Lookup rule as the first item in the Claude Collaboration section, labeled "Rule 0".
> --- `SETUP_PROMPT.md`

#### RT-BAP-maintenance-rules
Label: Vault and command maintenance authority

Consumer: later host model performing ingest/audit. Channel: generated schema.md and command Markdown, plus optional status/milestone commands. Force: operational instructions for selection, copying, revision and bookkeeping; shell fragments have fixed effects only if actually invoked. Horizon: later invocations and project sessions. Command discovery/loading and correct execution require the excluded host. Audit changes to these files are therefore potential changes to future behavior-determining machinery, not demonstrated activation (SRC-1, `SETUP_PROMPT.md`, Phases 1, 2, 4 and G0–G1).

> 1. Read `schema.md` — understand the conventions this vault was built with
> 2. Read `log.md` — find the most recent `ingest` timestamp and any open `[gap]` entries
> 3. Read `index.md` — understand what domains and pages exist
> --- `SETUP_PROMPT.md`

## Annotations

none
