<!-- Frozen pre-revision copy of kb/instructions/cp-skill-write-multistage/SKILL.md from HEAD, captured 2026-08-18. Do not update this evidence file when the live skill changes. -->

---
name: cp-skill-write-multistage
description: Write or substantially rebuild one consequential KB artifact through a source-first, multi-stage workshop before promotion. Use when claims still need grounding or synthesis; avoid it for settled local edits.
type: kb/types/instruction.md
user-invocable: true
allowed-tools: Read, Edit, Write, Grep, Glob, Bash, Skill, Task
argument-hint: "[target path | collection/type/topic] [source paths or brief]"
context: fork
---

# cp-skill-write-multistage

## EXECUTE NOW

**Target and inputs: $ARGUMENTS**

Develop one substantive KB artifact through independent reconstruction, a claim skeleton, drafting, audit, and reconciliation. Keep every intermediate artifact under one `kb/work/` workshop. Do not add workflow-state fields to the target artifact's frontmatter, and do not write the target until promotion.

This workflow requires fresh sub-agent contexts. If the runtime cannot create them, initialize the workshop, record the limitation, and stop before source reconstruction. Do not imitate source-first independence in a context that has already read the incumbent draft.

## Step 1 - Resolve The Target And Contract

Determine whether this is:

- **Edit mode:** `$ARGUMENTS` identifies one existing Markdown artifact.
- **New-write mode:** `$ARGUMENTS` identifies a collection, type, topic, or intended path.

Resolve the target collection to a directory under `kb/` with a local `COLLECTION.md`, and read that file in full.

In edit mode, read `type:` from the incumbent frontmatter and open that type specification. If the file has frontmatter but no `type:`, stop and repair that structural problem first. If it has no frontmatter, treat it as implicit `text`; do not invent a type or type specification.

In new-write mode, default an unspecified collection and type to `kb/notes/` and `kb/types/note.md`. Confirm that the collection's `## Types` section offers the selected type. If a requested shorthand type is not offered, stop and list the available types. If the user supplied an explicit `kb/.../*.md` type path, open it and verify that it is a type specification before using it.

In new-write mode, run one targeted near-duplicate search using distinctive title or topic terms. Prefer revising a near-duplicate over creating another artifact. Derive a provisional lowercase-hyphenated target path with a filename of at most 70 characters from the requested title or topic before creating the workshop. Use this initial path as the immutable run key. Treat a user-supplied path as fixed unless it violates the collection or type contract; otherwise, if the final title changes the destination, update the current target in `README.md` without changing the run key.

In edit mode, read the incumbent in full, run one backlinks lookup, and preserve a copy as `original.md` in the workshop. Remove `user-verified` from the eventual candidate after any substantive edit unless the user explicitly re-verifies it.

When the task is a mechanical update, a local prose edit, or a straightforward write whose claims, evidence, and structure are already settled, stop and explain why the multistage path is unnecessary. Ask whether the user wants to continue with `cp-skill-write`, and invoke it only after explicit confirmation. When no library artifact is yet intended, explain that the task belongs in an exploratory workshop and ask before creating one.

## Step 2 - Create Or Resume The Workshop

Search `kb/work/` for an unfinished multistage workshop whose `README.md` contains the exact run key or current target path. If exactly one exists, resume it. If several exist, stop and ask which one to use. Otherwise create:

```text
kb/work/multistage-write-<short-topic>-<YYYYMMDD>/
```

If that directory already exists for another target, append the smallest available numeric suffix, beginning with `-2`.

Create `README.md` with:

- the immutable run key, current intended target path, mode, collection, and type;
- the workshop's source/input paths;
- a checklist for `brief.md`, `reconstruction.md`, `claim-skeleton.md`, `draft.md`, `audit.md`, `candidate.md`, conditional `acceptance.md`, and promotion;
- unresolved human decisions and blockers;
- whether acceptance review is required, not required, or complete.

The checklist and stage files are the workflow state. Do not introduce a `stage` frontmatter field. Mark a stage complete only after its file is non-empty, contains the required items for that step, and has no blocker that the next step would hide. If an upstream artifact changes, uncheck and regenerate every dependent stage before promotion.

Add a one-line entry for the active run to `kb/work/README.md`. Preserve unrelated edits in that file; if an overlapping uncommitted change makes the update unsafe, record the pending index update in the workshop `README.md` and report it rather than overwriting another agent's work.

## Step 3 - Write The Brief

Write `brief.md` before delegating any prose. Include only information fixed by the task:

- the question or decision the artifact must address;
- intended audience and what the reader should understand, infer, or do;
- target claim or purpose supplied by the user, without expanding it;
- scope, exclusions, required terminology, and collection/type constraints;
- source and evidence paths available to the run;
- user directions and retained intent supplied to the run, with each memory input's source, subject, scope, and authoritative or advisory role, distinguishing inputs that can select intent from evidence that can warrant claims;
- known uncertainties, missing evidence, and decisions reserved for the user.

Repository and collection contracts may supply the register, acceptable contribution class, and a default audience. They do not by themselves select the artifact's governing question, claim, or purpose. Carry choices already fixed by the task, incumbent artifact, or supplied retained intent into the brief without asking the user to restate them. Current user direction prevails. If retained intent conflicts with the incumbent or another applicable input and no explicit precedence resolves the conflict, leave the choice unresolved. Do not treat remembered intent as meaning extracted from the bare request, model prior, or factual warrant. This skill consumes memory supplied through the retained-intent input but does not search raw interaction history itself.

If several materially different contributions still fit, record `DECISION NEEDED: intended contribution (specification gap)` in `brief.md` and the workshop `README.md`, then stop before reconstruction. A stronger model may use supplied context better, but greater capability does not make one of several compatible commissions authoritative. Source reconstruction must not choose the commission.

Acquire or ingest every named input needed to answer the governing question before continuing. Do not use search snippets as evidence. Missing intent is **blocking** when it leaves materially different commissions open. Missing evidence is **blocking** when the artifact cannot answer its governing question without asserting the missing claim. Pause at this step for either kind of blocker. A gap is **non-blocking** when the claim can be omitted or the uncertainty can honestly remain part of the final artifact; record it for reconstruction.

## Step 4 - Reconstruct From Sources In A Fresh Context

Launch one fresh, single-use sub-agent. Give it only `brief.md` and the exact source/evidence paths listed there. Do not give it `original.md`, any prior draft, or conclusions from another reviewer. Tell it not to search for or read those files.

Have it write `reconstruction.md` containing:

- the material facts, mechanisms, distinctions, quantities, and definitions supported by the inputs;
- the source or user direction supporting each material item;
- conflicts among inputs and differences in evidential strength;
- inferences stated as inferences rather than source facts;
- unresolved questions and explicit `EVIDENCE NEEDED`, `DEFINE`, or `DECISION NEEDED` markers where appropriate;
- details that are available but irrelevant to the target question, so they are not reintroduced merely because they are concrete.

Keep the reconstruction proportional to the inputs. Do not repeat the same limitation under several headings, derive unrequested statistics, or enumerate unavailable details that do not affect the target claim. Do not ask for polished prose. The reconstruction is an independent account against which later prose can be audited.

## Step 5 - Build The Claim Skeleton In A Fresh Context

Launch a new single-use sub-agent with `brief.md` and `reconstruction.md`. It may read a named source only to resolve an explicit reconstruction ambiguity. It must not read `original.md` or any draft.

Have it write `claim-skeleton.md` as a compact ordered plan containing:

- one governing claim, question, or practical purpose;
- the work each section or paragraph must perform;
- each material assertion, its scope and confidence, and its evidential basis;
- the inferential links needed to move from evidence to conclusion;
- definitions or comparisons needed for truth conditions;
- unresolved markers, each classified as blocking, omittable, or suitable for an explicit published limitation or open question;
- tempting but irrelevant branches to omit.

Every planned paragraph must change what the reader understands, infers, or can do. Do not add setup, summary, or praise merely to make the artifact sound complete.

Do not proceed while a blocking marker remains. For each non-blocking marker, either omit the dependent claim or explicitly authorize its conversion into a published uncertainty, limitation, or open question. Update the workshop checklist and resume from reconstruction when new evidence changes the skeleton.

## Step 6 - Draft In A Fresh Context

Launch a new single-use writer with `brief.md`, `reconstruction.md`, `claim-skeleton.md`, and the target collection/type contracts. Do not give it `original.md`.

Have it write `draft.md`. Require it to:

- realize the skeleton rather than discover new claims through fluent prose;
- preserve qualifiers, scope, uncertainty, and source distinctions;
- name mechanisms, comparison bases, and applicable scope where they affect the claim;
- express authorized uncertainty in reader-facing prose, but never copy workshop markers such as `EVIDENCE NEEDED` or `DECISION NEEDED` into the draft;
- use the simplest structure and language that carry the argument;
- omit frontmatter fields that the collection/type contract does not authorize.

The writer must not silently introduce a new commitment. When the prose appears to need one, insert `NEW COMMITMENT FOR AUDIT:` with the proposed claim instead of treating it as established.

## Step 7 - Audit Commitments Before Polishing

Launch a new single-use auditor. Give it `brief.md`, `reconstruction.md`, `claim-skeleton.md`, `draft.md`, the relevant contracts and sources, and `original.md` in edit mode.

Have it write `audit.md` with anchored findings. Each finding begins with `Status: open` and recommends one action: `keep`, `remove`, `ground`, `clarify`, or `ask user`. `Keep` means that the cited draft text is already justified; the finding must name that basis. Audit in this order:

1. **Claim delta:** identify every draft commitment absent from the skeleton, every planned commitment omitted or altered, and every change in causality, scope, confidence, quantity, or recommendation. In edit mode, also identify incumbent commitments the draft drops or changes.
2. **Grounding:** check material assertions against the reconstruction and sources. Distinguish source fact, user direction, inference, and unsupported completion.
3. **Specificity:** flag ambiguity that changes truth conditions, support, or implications. Ask for mechanism, comparison basis, or scope only where it is load-bearing; do not demand decorative detail.
4. **Relevance and audience:** flag undefined dependencies, displaced implications, irrelevant facts, and paragraphs that do no new work.
5. **Compression and prose:** only after the content audit, identify repetition, filler, unnecessary framing, and sentences whose syntax hides the claim.

Do not rewrite the draft in the audit. If a correct recommendation requires evidence or intent not present in the inputs, use `ask user` rather than guessing.

## Step 8 - Reconcile Into A Candidate

The orchestrating agent reads all workshop artifacts and writes `candidate.md` as a complete target artifact, including valid frontmatter when the selected type uses it. Preserve frontmatter-free implicit `text` as frontmatter-free text.

Resolve every audit finding explicitly in `audit.md`: add `Status: resolved` and a `Resolution:` naming the candidate change or the reason the text was kept. Use `Status: blocked` when evidence or a user decision is still missing. Do not promote while any finding remains open or blocked.

When reconciliation changes the governing claim or introduces material evidence not covered by `reconstruction.md`, return to Step 4. When it changes only ordering or expression, continue.

For public-facing, high-stakes, causal, or quantitative work—or whenever the audit found material drift—launch one final fresh acceptance reviewer. Give it `brief.md`, `reconstruction.md`, `claim-skeleton.md`, `audit.md`, `candidate.md`, the relevant contracts and sources, and `original.md` in edit mode. Have it write `acceptance.md` with `Verdict: PASS` or `Verdict: BLOCK` followed by anchored blockers only. Reconcile a block and rerun once, replacing `acceptance.md` with the current verdict; if material disagreement remains, ask the user. When review is not required, mark it `not required` in `README.md`.

## Step 9 - Promote And Validate

Promote only when:

- all workshop blockers and unintended unresolved markers are gone;
- each material commitment has an authorized basis, with inferences, uncertainties, and open work labeled appropriately;
- the candidate follows the collection and type contracts;
- every audit finding is resolved;
- any required acceptance review passes.

Identify each focused local source whose collection authorizes a source-to-target lineage footer. Validate it in its current state, and preserve a workshop copy of every source that will change. If a source is already invalid, stop before promotion.

Before writing, verify the candidate's frontmatter when applicable, required sections, and relative links as they will resolve from the target directory. Write `candidate.md` to the resolved target path. Preserve valid incumbent metadata and links unless the revision requires changing them. For a new artifact, derive a lowercase hyphenated filename of at most 70 characters from its title unless the user supplied a path. Never grant `user-verified` implicitly.

Run:

```bash
commonplace-validate path/to/target.md
```

Fix validation failures immediately. If they cannot be fixed within the established claim and contract, restore `original.md` byte-for-byte in edit mode or remove the newly created target in new-write mode, retain the workshop, and report the blocker.

After the target validates, add the authorized lineage footers and validate every changed source. Do not add a target-to-source lineage footer merely for symmetry. If a lineage edit cannot be made valid, restore every changed source and the target to their pre-promotion state, retain the workshop, and report the blocker.

After successful validation, remove the exact completed workshop directory and its `kb/work/README.md` entry unless the user asked to inspect or retain the run as an experiment or audit record. If retained as continuing work, mark its state in `README.md` and keep its index entry. Report what was removed or retained. Suggest `cp-skill-connect` for broader graph discovery.

## Verify

- The target remained untouched until a reconciled candidate was ready.
- Source reconstruction occurred in a fresh context that never saw the incumbent or draft.
- The skeleton preceded prose and every material draft addition was audited.
- Missing knowledge remained visible instead of becoming plausible filler.
- Content review preceded compression and sentence polish.
- Workflow state lives only in the workshop, not in library frontmatter.
- The promoted artifact passes deterministic validation.
