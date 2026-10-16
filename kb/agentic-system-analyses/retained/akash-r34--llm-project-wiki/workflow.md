---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "LLM Project Wiki's new-vault bootstrap workflow, delivery checks and later gap recovery."
run-id: AAS-2026-10-14-llm-project-wiki-c6c664168f3e-01
reviewed-boundary: "1fdfba9129a46afd18aa68a83f12d6716ab694c6"
---

# LLM Project Wiki workflow report

## Workflow account

### Selection and evidence limit

The representative workflow is new-vault bootstrap, from a user-pasted setup request to a generated vault and project instruction wiring. It is selected because Phases 0–6 supply an ordered, connected production path with explicit prerequisites and final checks, rather than merely listing capabilities. Its canonical route is [RT-RTE-vault-bootstrap](runtime.md#rt-rte-vault-bootstrap). Later ingest and gap audit are recovery/consumption paths, not assumed steps completed during the initial run.

The evidence is SRC-1's doctrine/design layer at the frozen commit: complete reads of `README.md` and `SETUP_PROMPT.md`. These introduce no additional source paths beyond [the boundary](boundary.md#boundary-and-evidence). The repository ships neither a generated vault nor a host trace. All handoffs, checks and outputs below are prescribed; no successful execution, cross-session reload or improved task performance is established.

### Request, branch and prerequisite

The user opens Claude Code at the project root and pastes the setup prompt. This supplies the procedure and project filesystem context, not a preselected entity list or expected-result artifact. The foreground model owns the next step throughout. Step 0 checks the literal `Obsidian Vault/` directory: absence selects bootstrap; presence diverts to Phase G and prohibits wholesale recreation. This is directory-based routing, not a test that an existing installation is valid (SRC-1, `SETUP_PROMPT.md`, Step 0).

Phase 0 requires reading project instruction files, existing memory and the directory tree, then answering five questions about project purpose, subsystems, entities, architecture and existing documentation. The model judges whether it can answer; the instruction can block progression but supplies no independent evaluator or machine-enforced gate. [RT-RTE-vault-bootstrap](runtime.md#rt-rte-vault-bootstrap) retains the exact “Do not proceed” prerequisite (SRC-1, `SETUP_PROMPT.md`, Phase 0).

Parallel work here means requested parallel reads, not an established delegation protocol:

> Before creating any files, read and understand the project. Run these in parallel:
> --- `SETUP_PROMPT.md`

No separate worker identity, task envelope, isolated context, returned report or aggregation rule is specified in these phases. Claude Code supplies the excluded read/write/shell execution machinery. The user delegates the project-specific construction to the foreground model; the prompt does not establish further agent delegation (SRC-1, `SETUP_PROMPT.md`, Phases 0–6).

### From audit findings to persistent pages

Phase 1 turns the audit into a project-named vault, containing Sources, Wiki, Templates, schema, index, log and health dashboard. The handoff is within one model-directed procedure: audit findings guide project-specific paths and page conventions. The generated schema defines required frontmatter, linking, excerpts, operations, ingest cadence and log grammar; it is intended as the first read for future maintainers, as recorded in [RT-OBJ-schema](runtime.md#rt-obj-schema). The index is to supply both an intent-to-page table and a full table of contents (SRC-1, `SETUP_PROMPT.md`, Phase 1).

Phase 2 asks the model to generate an adapted shell sync script and run it immediately. This is a handoff from model-selected paths to shell copying, then back to the model reading retained Sources. Copying changes the raw reference layer, not the compiled Wiki; the completion message asks for ingest. [RT-RTE-source-sync](runtime.md#rt-rte-source-sync) retains the snippet and its limits. Suppressed copy failures mean this handoff does not guarantee complete inputs (SRC-1, `SETUP_PROMPT.md`, Phase 2).

Phase 3 requests a full read of Sources and domain-by-domain compilation. The audit selects 4–8 domains; each gets an overview and concrete artifacts get entity pages. Page rules require exact source paths, signatures, schemas, non-obvious logic, constraints and cross-references. Gap signals can add pages. This is model judgment under the supplied conventions, not deterministic extraction or a human-approved page set (SRC-1, `SETUP_PROMPT.md`, Phase 3).

> Every entity page should have ≥ 3 inbound wikilinks from other wiki pages. No orphans. After finishing each domain, do a quick orphan check before moving on.
> --- `SETUP_PROMPT.md`

This intermediate check can identify missing links before the next domain. The same foreground model authors and checks the pages; no independent critic or compulsory rejection of an incorrect page is specified. Missing generated files prevent assessing actual coverage or whether the requested excerpts match the project.

### Wiring the later consumer and declaring delivery

Phase 4 modifies project instructions to request index-first navigation, relevant Wiki reads, insufficiency fallback and stale marking after code edits. Optional Gemini, memory-sync, status and milestone callers get corresponding rules. This hands the generated knowledge to future sessions through filesystem artifacts and behavior-guiding project files, not by transferring the current model context. The canonical authority channel is [RT-BAP-project-rules](runtime.md#rt-bap-project-rules); actual host loading and compliance remain uninspected (SRC-1, `SETUP_PROMPT.md`, Phase 4).

Phase 5 specifies tracking Wiki and Sources while ignoring per-machine Obsidian state, plus user and plugin manuals. Phase 6 appends a bootstrap log with source inventory, domain counts and a result line, then asks for a self-audit:

> Then run a self-audit:
> 1. Every entity in the codebase has a wiki page (or a gap note if not yet built)
> 2. Every wiki page has `[[wikilinks]]` to ≥ 2 other pages
> 3. Every wiki page appears in `index.md`
> 4. `schema.md`, `log.md`, `index.md` are all complete
> 5. `sync-vault.sh` runs without errors
> 6. `CLAUDE.md` Rule 1 points to the wiki
> --- `SETUP_PROMPT.md`

The checks can expose uncovered entities, disconnected pages, missing navigation, incomplete support files, sync errors or missing consumer wiring. They are not a separate admission barrier: the pages are already written and the bootstrap log precedes the self-audit. A coverage gap note is expressly permitted instead of a completed entity page. The prompt gives no automatic rollback, fixed pass/fail response envelope or mandatory human veto before writes. The model must interpret and act on the checks; no successful check result is supplied (SRC-1, `SETUP_PROMPT.md`, Phase 6).

The prescribed delivered result is the generated vault plus support scripts, commands, instructions, manuals and bootstrap record. The README then asks the user to commit the vault. Committing is an operator follow-up, not evidence of per-page approval or successful future consumption; [RT-RTE-vault-bootstrap](runtime.md#rt-rte-vault-bootstrap) retains that usage instruction (SRC-1, `README.md`, Usage).

### Failure and recovery paths

The quality bar supplies a concrete insufficiency test: can a future session answer the listed project questions using Wiki alone? A source read needed to answer exposes a gap, not a verified answer oracle:

> If any question requires opening a source file to answer, that's a gap. File it in `log.md`.
> --- `SETUP_PROMPT.md`

During later tasks the model may use source fallback, complete the task, update memory and append a gap note. The gap log carries the missing topic to a later maintenance invocation, rather than aborting the user's task. This branch is [RT-RTE-wiki-lookup](runtime.md#rt-rte-wiki-lookup). Source edits instead request path-grep selection and `status: stale`; no installed edit hook is supplied (SRC-1, `SETUP_PROMPT.md`, Phase 4).

The user/model then invokes sync and [RT-RTE-diff-ingest](runtime.md#rt-rte-diff-ingest). Ingest receives changed paths, Sources mappings, matching pages and open gaps, updates sections and dates, creates pages for new entities and logs the result. That record retains the ordered steps and dry-run clause. The single `HEAD~1` comparison is not a complete stale-page reconciliation; dry-run stops before the page grep and is not a mandatory approval gate. Wrong revisions have no specified rollback protocol (SRC-1, `SETUP_PROMPT.md`, Phase 2).

Re-pasting setup with an existing vault selects [RT-RTE-gap-audit](runtime.md#rt-rte-gap-audit), the broader repair path. The foreground model reads schema/log/index, fixes missing wiring, compares Sources inventory and timestamps, reconciles code entities with Wiki, repairs links/index/frontmatter and closes protocol gaps before logging the audit. G2 specifically allows resync/manual copy and script repair, so it can recover missing copied inputs. Existing material must be patched surgically, not rebuilt. Runtime records retain the repair mandate and copy-recovery passage; its audit-completeness claim also bounds the partial frontmatter snippet (SRC-1, `SETUP_PROMPT.md`, G0–G7).

These are prescribed recoveries across invocations, not evidence that a failed bootstrap resumes automatically. Completion messages, updated dates and audit logs alone establish neither source completeness nor correct answers.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

none declared in this member

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-vault-bootstrap](runtime.md#rt-rte-vault-bootstrap)

Workflow role: representative production route. Phase ordering carries audit findings into paths, conventions, copied inputs, pages and consumer wiring; it does not specify separate worker returns. Phase 0's five-answer prerequisite and Phase 3's domain orphan checks precede final self-audit. Admission remains model-directed writing; the final audit follows the bootstrap log and permits gap notes for unbuilt entities. Delivery is the generated installation and records, with committing left to the user. These workflow conclusions are claimed design, with operation uninspected (SRC-1, `SETUP_PROMPT.md`, Phases 0–6; `README.md`, Usage).

#### On [RT-RTE-gap-audit](runtime.md#rt-rte-gap-audit)

Workflow role: explicit later repair alternative, not an automatic exception handler for bootstrap. Existing-vault detection transfers the foreground model to ordered G0–G7 diagnosis and surgical patching. G1 requires missing infrastructure fixes before G2; G2 can repair the copying mechanism as well as missing snapshots. G7 records issues and resolutions only after the repair categories. The repair mandate and copy-recovery passage are retained in the runtime record; no executed recovery or subsequent consumer behavior is supplied (SRC-1, `SETUP_PROMPT.md`, Step 0 and G0–G7).
