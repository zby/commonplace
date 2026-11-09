---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Runtime baseline of team-ai-workflows: skill installation, Git-driven admission and lexical knowledge retrieval at the frozen commit."
run-id: AAS-2026-11-09-team-ai-workflows-c00fb85f7ed1-01
reviewed-boundary: "9aebd7a6c2803da450904eb5621ae5439508ff94"
---

# team-ai-workflows runtime report

## Runtime account

### Consequential work and responsibility boundary

The shipped system distributes model-facing skills and Markdown knowledge through a repository. It does not implement an enclosing agent loop. Claude Code interprets the skills, generates search keywords, executes tools and synthesizes answers. Shell code installs links; Python searches text. The ordinary path is clone → start Claude Code inside the repository → `/team-setup` → restart session → invoke `/docs-grep` from a project with a question → generate keywords → run search → read ranked files → answer with paths, optionally searching again. Installation, subsequent synchronization, retrieval and repository-content admission are separated in [RT-RTE-machine-setup](#rt-rte-machine-setup), [RT-RTE-skill-sync](#rt-rte-skill-sync), [RT-RTE-knowledge-search](#rt-rte-knowledge-search) and [RT-RTE-repository-admission](#rt-rte-repository-admission).

SRC-1, `README.md`, states the claimed work:

> A template for distributing **Claude Code skills** and a **team knowledge base** through a single git repository.
> --- `README.md`

The model-dependent operations are natural-language requests, not algorithmic guarantees. Keyword generation and answer grounding depend on the external host/model [RT-CMP-claude-code](#rt-cmp-claude-code); the Python executor neither calls a provider nor checks the answer. All conclusions here concern implementation or declared workflow. No supplied run trace or causal experiment establishes successful installation, discovery, model compliance, improved answers or benefit. Inspected source coverage includes the boundary's registered implementation paths, the README, both skills and all three sample knowledge files. These are SRC-1 implementation and doctrine/design, not additional sources or observed runs.

### Ordinary retrieval loop

The user owns the question and starts an open-ended lookup. The host owns next-step selection under the docs-grep instructions: derive 4–8 keywords, run the Python command, read top files, answer with relative paths, and revise keywords when hits appear weak. There is no fixed retry budget, expected answer, automated sufficiency score or independent answer oracle. File ranking is lexical, not model judgment: distinct lowercase keyword strings matched first, then the count of matching keyword entries across lines, then path order. A keyword occurring repeatedly on one line still contributes only once per argument entry to that line's hit count. Duplicate arguments can inflate total hits without adding distinct kinds. The script imposes no 4–8 count check; any nonblank arguments are accepted (SRC-1, `skills/docs-grep/scripts/docs_search.py`).

The search's current-run state is a result list built from readable `*.md` descendants of the resolved sources directory. It returns at most 15 file paths with at most two 100-character line previews each. The host must separately read full files; search output is not the full selected document set. This is a bounded delivery mechanism for search results, not context compaction, a subagent frame or a retained summary. No session-window eviction/reload implementation is supplied. The host's full-file tool access and context lifecycle are outside this source; the prompt does not limit reading to the previews or prove subsequent use. Corpus writes and memory revision are left to the memory analysis.

The search process uses filesystem access under the invoking principal, not a credential or capability broker supplied by this repository. Its intended effect is read-only lookup and stdout; full-file reads and answer production are host actions. No prompt-specific sandbox, model/provider selection or tool-approval implementation is supplied. The current grant set and deployed isolation envelope therefore cannot be inferred from these programs. Script path conventions and instructions are not permission boundaries (SRC-1, `skills/docs-grep/SKILL.md`, `skills/docs-grep/scripts/docs_search.py`).

### Installation, change admission and later operation

Setup asks the host to synchronize per-skill links, install a post-merge hook and edit the user's settings. The hook points back into the checkout rather than containing its own synchronization algorithm. Links expose current directories, not immutable snapshots. Repository changes can therefore alter later skill instructions or executable scripts without replacing an existing valid link. A skill-folder name is the linkage identity; no content hash, signature or version is checked by synchronization. Documentation delegates content edits to team adopters. These paths admit instructions, knowledge, additional skills and script changes through repository editing and Git distribution, not through an automatic model-training pipeline (SRC-1, `README.md`, `.claude/skills/team-setup/scripts/sync_user_skills.sh`, `.claude/skills/team-setup/scripts/post-merge`).

The only explicit interactive vetoes in setup concern conflicting personal skill names and overwriting a different existing hook. Setup also asks that unrelated settings be preserved. Those are requests to the host, not guards enforced by the shell script. Starting setup does not establish per-content approval of every later Git update. The link consumer's force and horizon are recorded in [RT-BAP-user-skills](#rt-bap-user-skills).

### Forcing cases and load-bearing guarantees

Four source-inspected forcing cases qualify the ordinary path; none was executed:

1. **Existing entries versus team updates.** A valid existing entry at a skill name is counted as kept whether it is the desired link, another link or a real directory. Only setup's later human-mediated conflict procedure can replace a personal directory. The unattended hook does not ask. Broken-link cleanup scans the whole user skills directory, not a registry of this repository's links. Thus synchronization is not ownership-scoped reconciliation and does not guarantee every team version becomes active (SRC-1, `.claude/skills/team-setup/scripts/sync_user_skills.sh`).
2. **Partial failure versus reported success.** Missing source directory exits 1. Individual link-creation failures emit an error, but the synchronizer finishes with exit 0; the post-merge hook also explicitly exits 0. This defeats an interpretation that a successful hook status proves installation succeeded. Counts and printed errors support inspection, not transactional recovery. No rollback is implemented for already completed filesystem changes (same script and `post-merge`).
3. **Configured root versus fallback.** A nonempty `TEAM_WORKFLOWS_DIR` wins if its `sources` child is a directory; its repository identity is not verified. Otherwise the search resolves its own real path and uses the fourth parent. A configured alternate corpus is a reachable input branch, not excluded by the self-location behavior. A missing final sources directory is a nonzero error, whereas zero matches is exit 0 (SRC-1, `skills/docs-grep/scripts/docs_search.py`).
4. **Skill-mediated lookup versus direct search.** Direct invocation of the Python CLI bypasses keyword-generation and citation instructions. Empty input exits 1; readable Markdown is searched with any other accepted keywords; individual `OSError` reads are skipped; no results returns a retry suggestion without retrying. The model-mediated weakness/retry loop is not implemented inside Python. Search limits constrain emitted previews, not host full-file access or model compliance (SRC-1, `skills/docs-grep/SKILL.md`, `skills/docs-grep/scripts/docs_search.py`).

The distributed-use claim has owner: the setup protocol and external Claude Code discovery. Its enforcement points are filesystem links and the requested settings/hook writes. Guarantee strength: **protocol**, not invariant. It covers the prescribed setup and installed hook path, contingent on writable user directories, Git hook invocation, successful commands, host skill discovery and a restart. Alternate direct script invocation, preexisting name collisions, manual settings changes and uninstalled hooks are not covered. Implementation conclusion status: wired for the shell mechanisms; operation conclusion status: uninspected. The model-facing setup steps themselves have claimed rather than enforced completion. The README's broad platform and every-project claims remain deployment claims, not verified guarantees.

Search ordering and preview limits have owner: the Python program; enforcement point: result sorting and output slicing. Guarantee strength: **invariant** within that routine for successfully read files and emitted output. Implementation conclusion status: wired; operation conclusion status: uninspected. These controls do not cover full-file host reads, all relevant knowledge being found, citation correctness, alternate tool calls or host/provider context handling. The required external contract is that the host executes the requested script and makes relevant files readable. The answer-grounding request has owner: the skill/host; enforcement point: natural-language instructions only; guarantee strength: **policy**. Implementation conclusion status: claimed; operation conclusion status: uninspected.

## Shared records

### Components

#### RT-CMP-claude-code
Label: Claude Code host and model

Source-native identity: Claude Code is the external skill runner named in SRC-1, `README.md`. Its model-dependent keyword and answer work is requested in `skills/docs-grep/SKILL.md`. Representational form: opaque distributed-parametric model processing consumes natural-language skill/question/file text; host discovery and execution rules are not supplied. Storage substrate: external host/provider model storage, inaccessible here. Parameters changing during operation: uninspected; no model mutation mechanism is supplied by these search/setup scripts. Exact model version: not pinned in the inspected skills or README. Mutable endpoint resolving to another model: uninspected; no provider endpoint is specified. This is an external execution dependency, not evidence of a locally embedded model or a particular deployed grant set.

> | [Claude Code](https://docs.claude.com/en/docs/claude-code/overview) | Runs the skills (the core tool) |
> --- `README.md`

### Operative objects

#### RT-OBJ-skill-links
Label: User-level skill links

Source-native identity: `~/.claude/skills/<name>` entries targeting repository `skills/<name>`. Representational form: symbolic filesystem references. Storage substrate: user's filesystem, symlinks on non-Windows branches and junctions in the Windows branch. Existing entries are not verified as team-owned. Links expose mutable checkout content; they neither copy nor pin the linked skill. SRC-1, `.claude/skills/team-setup/scripts/sync_user_skills.sh`, implementation:

> SRC="$REPO/skills"
> DST="$HOME/.claude/skills"
> --- `.claude/skills/team-setup/scripts/sync_user_skills.sh`

> ln -s "${d%/}" "$entry" \
> --- `.claude/skills/team-setup/scripts/sync_user_skills.sh`

#### RT-OBJ-docs-grep
Label: docs-grep instructions

Source-native identity: `skills/docs-grep/SKILL.md`. Representational form: natural-language procedure with an embedded symbolic shell command; the model interprets the procedure and the shell consumes the command when executed. Storage substrate: tracked Markdown exposed through the per-skill link. No specialized host enforcement of the procedure is present in the repository. SRC-1, `skills/docs-grep/SKILL.md`, doctrine/design:

> Derive 4–8 search keywords from the question. Include synonyms, abbreviations, and both English and native-language variants where relevant.
> --- `skills/docs-grep/SKILL.md`

> Read the top-ranked files and answer the question. Cite the relative paths of the files you used. If the hits look weak, adjust the keywords and repeat Step 2.
> --- `skills/docs-grep/SKILL.md`

### Routes

#### RT-RTE-machine-setup
Label: Machine setup protocol

Endpoints/progression: user starts Claude Code inside the repository and invokes `/team-setup`; the host resolves the root, invokes synchronization, installs the hook, writes settings, lists results and asks for a restart. Owner: user initiates; host interprets natural-language steps and executes filesystem commands. Context: repository cwd, user home/settings, existing links and hook. State/action effects: user-level links, copied executable hook and environment setting. SRC-1, `.claude/skills/team-setup/SKILL.md`, doctrine/design; synchronization implementation is separately recorded below.

- implementation conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: requested report of created/removed/kept counts, hook status, environment value and restart instruction.
- Later read-back: requested settings value supplies later search-root resolution; installed links and hook are consumed by host discovery and Git respectively, contingent on external contracts.
- Delegated visibility: inapplicable — no separate worker invocation is specified; the same host is asked to run shell actions.
- Selection predicate: every skill directory for linking; differing existing hook and personal directory conflicts receive special human-confirmation instructions.
- Invalidation or expiry: manual deletion/replacement or broken-link cleanup; no time-based expiry. A restart is requested for discovery.
- Activation or effect: requested installation and configuration; neither completed writes nor successful later skill activation are observed.
- Evidence limits: a skill procedure is not executable enforcement of confirmation, preservation or verification; host implementation and local state are outside SRC-1.

Admission roles: the host proposes installation actions under fixed instructions. The human can reject replacing a conflicting personal skill or overwriting a different hook. There is no supplied independent answer oracle. Operating mode: interactive one-time setup, rerunnable for repair, not an improvement experiment. Proposed changes are link/hook/settings installation. Recovery guidance offers a manual copy command if hook installation fails; a header in the hook says rerunning setup restores it. No transactional rollback of settings or partial link changes is specified. The instruction to preserve all existing settings keys has policy strength only.

> If present with different content: another hook may be installed — confirm the overwrite with AskUserQuestion
> --- `.claude/skills/team-setup/SKILL.md`

> Add to the `env` block of `~/.claude/settings.json` (always preserve every existing key when writing the file back):
> --- `.claude/skills/team-setup/SKILL.md`

#### RT-RTE-skill-sync
Label: Link synchronization and post-merge update

Endpoints/progression: explicit shell invocation during setup, direct manual invocation, or installed Git post-merge hook → locate repository relative to script → create destination → remove unreachable entries → link source child directories lacking an existing entry → print counts. Owner: shell code under the invoking user. Context/state: filesystem, platform detection and `HOME`; no model call in the script. The hook delegates by executing the repository script, not by creating a subagent. SRC-1, `.claude/skills/team-setup/scripts/sync_user_skills.sh` and `.claude/skills/team-setup/scripts/post-merge`, implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: count summary plus individual created/removed/error messages; missing source exits 1 but ordinary completion exits 0 even after individual failures. Hook returns 0 independently.
- Later read-back: user-level links provide later host access to checkout skill content; the hook executes the current checkout synchronizer after later merges.
- Delegated visibility: inapplicable — child shell execution shares filesystem effects and stdout, not an isolated model context.
- Selection predicate: cleanup scans listed destination entries lacking reachable targets; creation iterates `skills/*/`, keeping any existing entry. It does not validate `SKILL.md` or ownership.
- Invalidation or expiry: broken links may be removed on the next synchronization; valid existing entries remain untouched, with no content/version expiry.
- Activation or effect: creates filesystem links or junctions and removes broken entries; subsequent model discovery remains external and unobserved.
- Evidence limits: no run or platform tests supplied; shell listing splits names on whitespace during cleanup; the claimed idempotence is not a proof of complete safe reconciliation.

Admission: folder additions become candidate skill links; code admits them by directory existence/name availability, without per-content human review. An existing entry vetoes replacement mechanically. Rejection/recovery is nontransactional: errors are printed, completed changes remain, and rerunning may retry. Guidance is the shipped one-link-per-skill convention. No answer oracle or improvement-selection loop is involved; this is deterministic installation maintenance. The live checkout supplies both instructions and executable code, so changing a linked file is not mediated by this link-creation gate.

> if [ -e "$entry" ]; then
>         kept=$((kept + 1))
> --- `.claude/skills/team-setup/scripts/sync_user_skills.sh`

> echo "sync done: created=$created removed=$removed kept=$kept"
> exit 0
> --- `.claude/skills/team-setup/scripts/sync_user_skills.sh`

> "$(git rev-parse --show-toplevel)/.claude/skills/team-setup/scripts/sync_user_skills.sh"
> exit 0
> --- `.claude/skills/team-setup/scripts/post-merge`

#### RT-RTE-knowledge-search
Label: Keyword search and host answer loop

Endpoints/progression: question → model-derived keywords → Python root resolution and Markdown traversal → lexical ranking and previews → host full-file reads → answer or revised keywords. Direct CLI entry skips the first and last model-dependent stages. Owner: user supplies problem; model proposes keywords, judges hit weakness and selects files; Python performs fixed ranking. Working state: keywords, per-file counts, previews, result list and host-visible tool output. File-selection and answer decisions beyond ranking remain host interpretation, not a code-enforced retrieval policy. SRC-1, `skills/docs-grep/SKILL.md`, doctrine/design, and `skills/docs-grep/scripts/docs_search.py`, implementation.

- implementation conclusion status: wired
- instruction conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: up to 15 ranked relative paths, scores and two short previews per file; error/usage with exit 1, or no-match message with exit 0. The requested terminal host output is an answer citing files.
- Later read-back: accumulated corpus content is selected for a consumer invocation through lexical search and requested full-file reads; this route itself does not persist queries, answers or summaries. Memory lineage and corpus revision are not established by search execution.
- Delegated visibility: inapplicable — subprocess output returns to the host; no distinct model worker or selective subagent return is specified.
- Selection predicate: nonblank CLI arguments; valid configured sources directory before real-path fallback; readable recursive `*.md`; lowercase substring hits; descending distinct keywords, descending keyword-line matches, lexical path tiebreak; output truncated to 15 files.
- Invalidation or expiry: results rebuilt for each invocation; unreadable files skipped; no cache/TTL. Host session retention and compaction remain uninspected.
- Activation or effect: Python is wired to emit selected material; host is instructed to read and use it. No trace establishes that delivered text changed an answer.
- Evidence limits: previews are incomplete, missing/unreadable content is not reported per file, lexical relevance is not answer correctness, and host retry/citation compliance is unobserved.

Decision policy: Python code provides symbolic ranking; the prompt provides natural-language query-expansion and relevance judgment. Proposer: model for keywords and answer. Decider/veto: model judges whether to retry; user can supply another question, but no explicit per-answer human approval gate is prescribed. Answer oracle: none supplied; the corpus is consulted material, not a separately defined expected answer. Operating mode: open questions, not bounded experiments or a curriculum. This is a lookup workflow, not an admission mechanism for changed knowledge or code.

> if env:
>         p = Path(env)
>         if (p / "sources").is_dir():
>             return p
> --- `skills/docs-grep/scripts/docs_search.py`

> here = Path(__file__).resolve()
>     return here.parents[3]
> --- `skills/docs-grep/scripts/docs_search.py`

> except OSError:
>             continue
> --- `skills/docs-grep/scripts/docs_search.py`

> results.sort(key=lambda r: (-r[0], -r[1], str(r[2])))
> --- `skills/docs-grep/scripts/docs_search.py`

> for kinds, hits, path, previews in results[:TOP_N]:
> --- `skills/docs-grep/scripts/docs_search.py`

#### RT-RTE-repository-admission
Label: Team repository customization and distribution

Endpoints/progression: adopter edits skills and knowledge in the repository; Git distribution places changed files in users' checkouts; linked skill files and search reads expose them to later consumers. Owner: human team/adopter in the README's stated workflow; Git transports changes. Actual author identity, review policy and repository permissions are not supplied. Proposed changes can be additional skill instructions/executables and replacement knowledge files. SRC-1, `README.md`, doctrine/design; link and search consumers are implemented by the preceding routes.

- implementation conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: changed checkout files; new link creation depends on synchronization, whereas edits under valid links need no relinking.
- Later read-back: skill discovery and scripts consume checkout content; search reads current corpus files, with actual host interpretation unobserved.
- Delegated visibility: uninspected — team collaboration and review arrangements are not described beyond repository hosting and distribution.
- Selection predicate: author chooses content; synchronization selects directories by existence and name, search selects Markdown by lexical matching. Git review/merge policy is not supplied.
- Invalidation or expiry: manual replacement/deletion through repository changes; no content TTL or shipped semantic rollback mechanism. Git recovery practices are external and unobserved.
- Activation or effect: capability/instruction/knowledge changes can reach later host operation through links and filesystem reads, without proving discovery, compliance or improvement.
- Evidence limits: this is documented customization plus implemented consumers, not an observed maintenance episode, automatic trace-fed update, or demonstrated self-improvement.

Admission roles: team author proposes/edits; actual merge approver and veto holder are unresolved. No software content evaluator or expected-answer oracle is shown for this path. Operating mode: ordinary repository customization and update distribution, not measured candidate competition. Guidance says to add skills and replace sample knowledge; sample writing tips recommend focused files and symptom wording. What persists is repository text/code, not model parameters. Rejection and rollback policies are not specified; file editing/replacement is possible but no exercised repair is evidenced. These operational instructions are not evidence of a route that formulates, criticizes and iteratively revises explanatory theories; no theory-builder or learning claim is made here.

> 2. Add your own skills under `skills/<skill-name>/SKILL.md`
> 3. Replace the samples in `sources/` with your team's knowledge (docs copies, API references, first-hand tips)
> --- `README.md`

> - Write pitfalls as "symptom -> cause -> fix", because people search by the symptom's wording
> --- `sources/tips/writing-knowledge.md`

### Claims

#### RT-CLM-machine-distribution
Label: Machine-wide skill distribution claim

Claimed operation: after setup and restart, skills work in every project; updates require only a pull. SRC-1, `README.md` and `.claude/skills/team-setup/SKILL.md`, doctrine/design. The implemented link and hook paths support distribution affordances, not successful host discovery in every context or robust handling of every update. Collisions, partial failures and dependency contracts are bounded above.

> - Skills are injected into the user level (`~/.claude/skills`) as one link per skill, so they work **in every project on the machine**
> --- `README.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-user-skills
Label: Linked skill instructions to host behavior

Consumer: Claude Code's external skill loader/model, then shell/Python executors when the host calls tools. Channel: user-level link to the repository skill directory; natural-language procedure supplies model guidance and embedded command text supplies tool invocations. Force: requested procedural guidance, not a repository-enforced permission policy; actual precedence against other host instructions is uninspected. Horizon: later sessions/projects on that machine, contingent on discovery and restart, until link/content/configuration changes. This is an afforded behavioral-authority path, not observed activation. SRC-1, `.claude/skills/team-setup/SKILL.md`, `skills/docs-grep/SKILL.md`, and `.claude/skills/team-setup/scripts/sync_user_skills.sh`.

> This links every skill under `skills/` into `~/.claude/skills/<name>` (idempotent — safe to re-run any time):
> --- `.claude/skills/team-setup/SKILL.md`

The search skill's actual procedural content and consumer decisions are retained in [RT-OBJ-docs-grep](#rt-obj-docs-grep) and [RT-RTE-knowledge-search](#rt-rte-knowledge-search). Link presence establishes reachability under the stated host contract, not compliance or improved capacity.

## Annotations

none
