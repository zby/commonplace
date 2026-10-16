---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "o-o runtime baseline: local polyglot document updates, external Claude dispatch, library drivers and change admission at the frozen commit."
run-id: AAS-2026-10-15-o-o-b6fd0055e5c1-01
reviewed-boundary: b0d5063e37b4eafdbc23c1899a31f1836168b989
---

# o-o runtime report

## Runtime account

### Work, entry and ordinary invocation

o-o maintains local research articles as HTML/bash polyglots. A person reads the same file in a browser or runs it with Bash to request an update. A shipped index also creates documents, drives batch updates and rebuilds library navigation. The local shell is a workflow driver, not an implementation of the model/tool loop. All findings below use SRC-1 at the frozen revision; code passages establish implementation, contracts establish requested agent behavior, and README statements establish declared intent. No target was executed and no supplied execution trace establishes activation or benefit. See [RT-CLM-living-document](#rt-clm-living-document).

For an ordinary invocation, a user runs `bash example/anthropic-leadership.o-o.html`. The quoted heredoc makes Bash skip the HTML. The preamble enables `set -euo pipefail` and derives `SELF`, `SELF_DIR` and `SELF_NAME` from the invoked file. File basename, rather than a type field, decides whether the default action rebuilds an index (`index*`) or updates an article. Article dispatch first extracts the first matching freshness fields. Empty or unparsable dates lead toward an update; a parsed age below the configured interval skips it. `--force` bypasses this gate. No timer wakes the document: scheduling is an external responsibility, and cron/Actions remain README roadmap items. SRC-1: `example/index.o-o.html`, `README.md`; [RT-RTE-document-update](#rt-rte-document-update).

The shell extracts the first `max_cost_usd`, falling back to 0.50, and builds a fixed natural-language prompt naming the absolute document path. It does not put the full article into the initial prompt. The prompt tells Claude to read the contract, consult the date and modify only article and state blocks. The shell launches `claude -p`, supplies the allowed-tool string and budget flag, and optionally appends `--model`. Only Claude is implemented as a backend; an unknown agent or missing executable exits with an error. The inherited working directory and external CLI configuration are not reset by o-o. Resolving the file path is not isolation of the agent process. SRC-1: `example/index.o-o.html`; [RT-CMP-claude](#rt-cmp-claude).

The external agent owns the next research, source-selection and edit decisions. The document supplies subject, scope, audience, tone, research intents, required sections, domain preferences/denials, image rules and output conventions. The ordinary contract asks it to read prior sources and facts, focus on changes since `as_of`, or enrich images, links and context if little changed. It requests inline references, manifest version/date changes, source-cache maintenance and a changelog append. These are instructions interpreted by the model, not shell-validated transformations. Model tools, subprocess behavior and provider internals remain outside the inspected implementation. SRC-1: `example/anthropic-leadership.o-o.html`, `example/index.o-o.html`.

Edits take effect in the original file; there is no intermediate candidate/accept transaction in the update driver. After Claude returns successfully, the shell prints completion. That message does not inspect the resulting file, citations, JSON validity, source-policy compliance or article accuracy. A failed invocation can leave partial edits; `set -e` is failure propagation, not rollback. The generated files and update driver contain no automatic restore step. A user may rerun, force an update or repair the file, but recovery success is unobserved. SRC-1: `example/index.o-o.html`; [RT-RTE-document-update](#rt-rte-document-update).

The terminal product is a changed local document, not merely the CLI's text response. The browser consumes HTML, parses the manifest to fill title/date/version, constructs a TOC and citation links, and displays the contract on badge click. It stores a theme preference in browser localStorage; this is UI state, not research memory. Browser rendering and index extraction are distinct consumers of the retained document. Source-cache revision semantics are left to the memory analyst; this report establishes only the shell-to-agent request and later consumer entry points. SRC-1: `example/index.o-o.html`; [RT-RTE-library-read](#rt-rte-library-read).

### Four forcing cases and their limits

1. **Fresh article versus forced update.** The same file skips dispatch when its parsed age is below the interval, but `--force` intentionally disables that condition. A batch call first checks dates itself and then launches each eligible file's Bash path. Batch uses age `>` for eligibility while the direct skip test uses age `<`; the exact threshold is not identical. Thus freshness is a local spend-avoidance gate, not a global invariant that a document cannot be updated early. SRC-1: `example/index.o-o.html`; [RT-RTE-batch-create](#rt-rte-batch-create).
2. **Edit instruction versus shell-capable delegate.** Both the prompt's section restrictions and the tool list reach the same external process. The grant request includes Bash, and the prompt explicitly suggests curl, image conversion and file removal. An instruction to use Edit does not prove that all writes pass through section-aware checks. The o-o driver does not interpose on Bash, Edit or web results; host permissions and approvals are external. This qualifies any claim that the update cannot modify shared machinery or arbitrary local files. SRC-1: `example/index.o-o.html`; [RT-BAP-update-prompt](#rt-bap-update-prompt).
3. **Ordinary enrichment versus sentinel restraint.** The ordinary contract asks for enrichment when little news exists, whereas the shipped AGI and incarceration contracts ask for concise non-event reports and comprehensive coverage only after an event. These are different research modes of the same dispatch, not separate code branches. The agent evaluates the event against external evidence; there is no supplied expected-answer oracle or deterministic event detector. SRC-1: `example/anthropic-leadership.o-o.html`, `example/agi-declared.o-o.html`, `example/trump-incarceration.o-o.html`; [RT-RTE-document-update](#rt-rte-document-update).
4. **Agent preservation rule versus explicit machinery propagation.** An article update is asked to preserve shell/JS/CSS, but an operator can edit one file and run `--sync shell` or `--sync all`. The source file's marked block then replaces sibling blocks without a diff-approval gate. Any sibling can be the canonical source for that invocation. New documents also copy the invoking file's shared blocks. This is a shipped admission route for future execution machinery, not evidence of autonomous improvement. SRC-1: `example/index.o-o.html`, `README.md`; [RT-RTE-code-sync](#rt-rte-code-sync).

These static forcing cases challenge control coverage; none is an executed experiment. The material inspected paths are direct article dispatch, generated-document dispatch, batch child processes, direct configuration edits, shared-code synchronization, browser read and index rebuild. The only model call exposed by the driver is the external CLI. Provider-native tools, callbacks, internal subagents, context compaction, session retention, permission escalation and remote workers inside Claude Code remain uninspected rather than absent. No o-o-specific alternative model loop is established. SRC-1: `example/index.o-o.html`.

### Guarantee scope and enforcement

| Load-bearing guarantee or policy | Owner and enforcement point | Strength and covered paths | Alternate paths and required external contract | Separate conclusions |
|---|---|---|---|---|
| Skip fresh articles | o-o shell `check_freshness`; batch eligibility precheck | policy; ordinary default article update and batch selection | `--force`, direct file editing and other actions bypass it; depends on usable metadata and host date utilities | implementation conclusion status: wired; operation conclusion status: uninspected |
| Limit spending to the requested budget | o-o passes `--max-budget-usd`; external Claude owns billing enforcement | policy at the o-o boundary; direct and child article dispatch | shell work outside Claude and external CLI semantics are not covered; needs the installed CLI/provider budget contract | implementation conclusion status: wired; operation conclusion status: uninspected |
| Preserve machinery and edit only content/state | o-o prompt and contract; external agent is requested to comply | best effort; dispatched article maintenance | Bash access and direct operator/config/sync writes do not pass a section validator; needs compliant agent behavior and any external host restriction | implementation conclusion status: wired; operation conclusion status: uninspected |
| Offline-style browser presentation | generated HTML CSP and embedded resources; browser enforces CSP | policy; browser resource loading, not Bash research | inline script/style remain allowed; links can navigate; downloaded research/images occur in the shell-capable agent; depends on browser behavior | implementation conclusion status: wired; operation conclusion status: uninspected |

The capability surface requested from Claude is Bash, Read, Edit, WebSearch and WebFetch. The current effective grant set is uninspected because installed CLI settings and permission state are not supplied. The deployed isolation envelope is likewise uninspected: no container, filesystem sandbox or network confinement is established by the o-o command. The browser CSP is not a sandbox for the update process. SRC-1: `example/index.o-o.html`.

## Shared records

### Components

#### RT-CMP-claude
Label: Claude-backed research executor

Source-native identity: the `claude` executable selected from PATH, with optional `--model`. Its client is an external process; the model behind it is distributed-parametric, stored by an external runtime/provider rather than in an o-o artifact. Exact parameters, storage and internal context handling are uninspected. Parameter changes during operation are uninspected; there is no local training step in the inspected dispatch. The exact model version is not pinned. An omitted model uses the external default, and a supplied name may be an alias; whether a mutable endpoint resolves to another version depends on the external CLI/provider. SRC-1: `example/index.o-o.html`.

>       if [[ -n "$MODEL" ]]; then
>         claude_args+=(--model "$MODEL")
>       fi
> --- `example/index.o-o.html`

### Operative objects

#### RT-OBJ-shared-shell
Label: Marked shared shell block

Source-native identity: `OO:SHELL:START` through `OO:SHELL:END` in each `.o-o.html` file. Representational form: symbolic Bash consumed under fixed shell rules, including a template that emits further code and natural-language agent instructions. Storage substrate: local text files, copied at generation and explicitly synchronized between siblings. This record denotes the executable block, not the separately retained research cache, article, manifest or document-specific contract. SRC-1: `example/index.o-o.html`.

>   # Assemble: content before marker + canonical section + content after marker
> --- `example/index.o-o.html`

The code consumer is a later Bash invocation; browser JavaScript/CSS are separate marked blocks synchronized by the same driver. See [RT-RTE-code-sync](#rt-rte-code-sync).

### Routes

#### RT-RTE-document-update
Label: Dispatch research and admit document edits

Endpoints and progression: user Bash invocation → freshness gate → budget extraction and prompt → external Claude process → tool-mediated edits to the same file → browser or future update invocation. Owner: shell for dispatch, external agent for research and edits. Context begins with the path and fixed instructions; file contents and web evidence enter only if the agent reads/fetches them. File identity is absolute `SELF`; no o-o session or research-task ID is added. SRC-1: `example/index.o-o.html`, `example/anthropic-leadership.o-o.html`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Claude's inherited output and exit result, followed on success by the shell completion message; the consequential result is the in-place file edit.
- Later read-back: the contract requests reuse of manifest and cache on future updates; browser and index consumers read the changed file through their own rules.
- Delegated visibility: the prompt supplies an absolute path and asks the external agent to read the whole file; requested tools expose research and local I/O, subject to uninspected host permissions.
- Selection predicate: default non-index action, stale/empty/unparsable date or force; the agent then selects evidence using document research guidance.
- Invalidation or expiry: freshness interval controls dispatch, not automatic deletion of retained content; source validity is delegated to the agent.
- Activation or effect: shell wiring requests research and direct editing; successful compliance and effects on later behavior are not observed.
- Evidence limits: source establishes dispatch and instructions, not the external tool loop, actual permission grants, factual correctness, costs or incremental-reuse benefit.

Admission: the user starts the workflow but does not approve each proposed edit. The external agent proposes/selects research claims and physically writes them via tools; admission is direct mutation, with no o-o review callback or post-edit acceptance test in this route. The agent can decline a source or skip an oversized image under guidance; the shell can fail before/at dispatch but does not veto individual factual edits. No automated rollback is implemented in this route. Operating mode: open-ended web research, either ordinary incremental enrichment or contract-defined sentinel monitoring. Answer oracle: none supplied; source preferences and the model's judgment are not reference answers. Guidance and persistence: the static maintenance procedure and topic configuration guide changed article/state blocks; procedure revision is not requested. Theory revision is not established merely by research prose generation. SRC-1: `example/index.o-o.html`, `example/anthropic-leadership.o-o.html`, `example/agi-declared.o-o.html`, `example/trump-incarceration.o-o.html`.

> Use the Edit tool to modify specific parts of the file in-place.
> Only modify: <article> content, oo-manifest, oo-source-cache, oo-changelog.
> Do NOT touch CSS, JavaScript, the shell preamble, or structural HTML outside <article>.
> --- `example/index.o-o.html`

>       "3. Read the oo-source-cache JSON block to see what sources and facts were gathered previously. Build on prior research, do not start from scratch.",
> --- `example/anthropic-leadership.o-o.html:428-428`

>     "sentinel": "This is a SENTINEL document. The core event (a major AI company or lab credibly declaring they have achieved AGI) has NOT yet occurred as of the document creation. Your job is to track developments TOWARD this event. Do NOT write a generic AI history explainer or pad the article with filler. If no credible AGI declaration has been made, the article should be concise: state clearly that it has not happened yet, note which companies/labs are closest and what benchmarks they cite, and what a credible declaration would require. When a declaration DOES occur, provide comprehensive breaking coverage.",
> --- `example/agi-declared.o-o.html`

#### RT-RTE-batch-create
Label: Library creation and batch invocation

Endpoints: index CLI → generated local article and first Bash invocation, or recursive discovery → sequential eligible-file Bash invocations → index rebuild after updates. Owner: index shell; user chooses title/scope and optionally audience/tone/budget interactively. Generation copies shared code and emits a default contract, empty cache/changelog and version-zero manifest. The index class is selected by `index*` basename. SRC-1: `example/index.o-o.html`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: creation/update progress; generation persists the new file before first research; batch reports a count and rebuilds the index if at least one file was processed.
- Later read-back: generated articles enter subsequent Bash/browser paths; refreshed metadata enters index rebuild and later viewing.
- Delegated visibility: each child gets its own file path via its embedded dispatch; batch does not concatenate article bodies into one model prompt.
- Selection predicate: creation requires an index entry and unused slug path; batch recursively finds `.o-o.html` files except SELF and selects missing/invalid dates, age above interval or force.
- Invalidation or expiry: freshness determines each batch candidate; creation rejects an already-existing path rather than replacing it.
- Activation or effect: code emits files, runs child Bash processes and rebuilds navigation after eligible updates; actual executions remain unobserved.
- Evidence limits: batch count reflects completed child commands, not verified research quality; inherited host context, failures and partial file edits are not isolated per document by o-o.

Admission: the person supplies creation parameters; code emits a template without content approval, then [RT-RTE-document-update](#rt-rte-document-update) owns research admission. Batch selection is deterministic metadata processing, not candidate quality evaluation. Operating mode: requested creation or bounded directory traversal; no answer oracle. Recovery: existing-file guard prevents intended overwrite at creation; a first-update failure can leave the generated stub. Sequential child failure under strict shell mode can interrupt remaining updates; there is no batch transaction or per-file retry. The parent does not forward its `--model` or `--agent` flags to children: child calls carry only optional `--force`, so direct model override is not a batch-wide guarantee. SRC-1: `example/index.o-o.html`.

>       if [[ "$force" -eq 1 ]]; then
>         bash "$file" --force
>       else
>         bash "$file"
>       fi
> --- `example/index.o-o.html`

#### RT-RTE-contract-edit
Label: Operator configuration admission

Endpoints: explicit `--set`, `--add` or `--remove` → Perl text substitutions → same file → later agent or freshness/budget consumer. Owner/proposer/decider: invoking operator, with deterministic code applying requested strings. These commands do not call the model or require a research update first. SRC-1: `example/index.o-o.html`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: printed field/array modification message and direct file mutation.
- Later read-back: subsequent dispatch extracts changed budget/interval; subsequent research reads changed identity, intents or required sections.
- Delegated visibility: changes reach the agent only through a later read of the document, not as a live session update.
- Selection predicate: CLI action and allowed field names; array commands reject index-class files.
- Invalidation or expiry: values persist until another edit; no freshness reset or configuration version transition is required.
- Activation or effect: literal replacement makes changed guidance available; actual later behavioral dependence is unobserved.
- Evidence limits: regex editing is not JSON-schema validation; a success message alone does not prove a valid intended replacement.

Admission/rejection: CLI guards reject missing/unknown keys; no semantic approval step or automatic rollback follows accepted strings. `remove_from_array` chooses the array name but its removal expression filters matching whole lines across the file, so it is not a strictly array-local semantic editor. Operating mode: direct operator configuration, no answer oracle. Guidance: operator-selected identity/research constraints and scalar settings persist as future instructions/control inputs, not as evidence of autonomous method revision. SRC-1: `example/index.o-o.html`.

>   # Remove line matching the exact value
>   perl -i -ne 'print unless /^\s*"\Q'"$value"'\E"\s*,?\s*$/' "$SELF"
> --- `example/index.o-o.html`

#### RT-RTE-code-sync
Label: Shared machinery admission

Endpoints: operator edits invoking file → chooses `css`, `js`, `shell` or `all` → code copies marked blocks to immediate sibling `.o-o.html` files → later Bash/browser consumers. Owner: local operator chooses source and section; code applies it. Shell changes alter future creation, research dispatch and library operations. Browser changes alter presentation/consumption. SRC-1: `example/index.o-o.html`, `README.md`; object [RT-OBJ-shared-shell](#rt-obj-shared-shell).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: per-file sync/skip output and sibling replacements via temporary file plus rename.
- Later read-back: later shell/browser invocations consume the replacement code; future generation copies the invoking file's current shared blocks.
- Delegated visibility: inapplicable — synchronization itself is local code copying, not model delegation.
- Selection predicate: selected marker pair in SELF and each immediate sibling; siblings without markers are skipped; `all` runs CSS, JS then shell.
- Invalidation or expiry: replacement supersedes prior marked blocks without version negotiation; CSS sync also removes/reinjects custom styles according to local `oo.css` availability.
- Activation or effect: copied code becomes executable/presentational input on later invocations; no run evidence establishes actual exercise.
- Evidence limits: marker presence is not code validation; per-file rename is not an atomic library-wide rollout or rollback.

Admission: user-authored changes enter through explicit propagation, not model-generated patches or operational feedback. The code can reject an unknown section or missing source markers and skip unmarked destinations, but does not compare behavior, request confirmation or test the replacement. Recovery requires an external restore/manual correction; previous blocks are not retained by this mechanism. Operating mode: explicit maintenance command; no answer oracle. The guidance is the invoking file's block content and the operator's section choice; that code persists in recipients. There is no evidence-responsive self-improvement claim in this route. SRC-1: `example/index.o-o.html`.

>       sed -n "${start_line},${end_line}p" "$SELF"
>       tail -n +$((f_end + 1)) "$file"
>     } > "${file}.tmp" && mv "${file}.tmp" "$file"
> --- `example/index.o-o.html`

#### RT-RTE-library-read
Label: Index projection and browser consumption

Endpoints: default index Bash invocation → recursive file scan → extracted metadata/excerpt → rewritten index HTML; browser opening → DOM rendering, manifest parsing, navigation and optional contract display. Owners: shell extraction and browser JS rules; user initiates rebuild/read. SRC-1: `example/index.o-o.html`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: index scan count/progress or rendered article/library UI.
- Later read-back: persisted index projection is consumed on future browser opens; browser theme is separately reloaded from localStorage.
- Delegated visibility: inapplicable — this route has no model delegate.
- Selection predicate: recursively found `.o-o.html` files except SELF; first regex matches for title/version/date, first paragraph excerpt, and top eight cards sorted by date; browser reads IDs and article headings/references.
- Invalidation or expiry: index rebuild replaces the marked projection; UI search/sort affects current DOM only; freshness badges do not schedule research.
- Activation or effect: consumer rules are wired to render metadata/navigation; index does not deliver full cached research facts or validate them.
- Evidence limits: no browser run was supplied; index projection is lossy and not an accuracy assessment or complete document mirror.

Index file links use `basename` despite recursive discovery, so nested-directory discovery does not by itself establish correct nested links. Browser contract display reads human-visible fields, not a complete enforcement policy. Neither index listing nor citation-link generation establishes research warrant. SRC-1: `example/index.o-o.html`.

>     var data=JSON.parse(me.textContent);
>     d.getElementById('doc-title').textContent=data.title||'Living Article';
>     d.getElementById('doc-asof').textContent=data.as_of||'\u2014';
>     d.getElementById('doc-version').textContent=data.version||'0';
> --- `example/index.o-o.html`

### Claims

#### RT-CLM-living-document
Label: Self-updating living document claim

Claimed operation: one file is readable in a browser and updateable through Bash, which launches a research agent for in-place web-informed editing. The wording does not establish a scheduler, successful operation, learning or improved quality. The source-level implementation is described in [RT-RTE-document-update](#rt-rte-document-update); automation still needs an invocation. SRC-1: `README.md`.

> Each `.o-o.html` file is a self-updating living document — open it in a browser to read, run it with `bash` to update.
> --- `README.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-update-prompt
Label: Update prompt authority channel

Consumer: external Claude agent. Channel: `claude -p` prompt carrying SELF and imperative task instructions, followed by agent-requested file reads. Force: natural-language task guidance rather than a section-restricted file-write capability. Horizon: one dispatched invocation; unchanged embedded shell instructions are reconstructed on later invocations. The document-specific contract supplements this prompt; retained cache authority is left to the memory account. SRC-1: `example/index.o-o.html`.

>       local -a claude_args=(
>         -p "$prompt"
>         --allowed-tools "Bash,Read,Edit,WebSearch,WebFetch"
>         --max-budget-usd "$budget"
>       )
> --- `example/index.o-o.html`

The capability request and preservation instruction coexist. Host enforcement and whether untrusted retrieved text affects behavior remain uninspected; no universal prompt-injection defense is inferred.

## Annotations

none
