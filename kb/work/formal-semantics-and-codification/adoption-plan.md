# Adoption plan

Drafted 2026-11-02 while the account and definitions were under Astra's final revisions. Part of the [workshop](./README.md). This file turns the [closure](./README.md#closure) clause and the [promotion checklist](./follow-up-library-changes.md#promotion-checklist) into an ordered sequence of commits with the files each one touches, so that promotion can be executed in one sitting once the operator authorizes it. Nothing here is authorized by the workshop itself; the sequence starts with the operator's decisions. File lists come from a search of the library on 2026-11-02 and should be re-run before execution.

## Step 0: approved execution choices

The account's content and the [presentation choices](./decisions-and-open-questions.md#approved-presentation-choices) are approved and are not reopened here. The promoted definitions carry no "Decisions and promotion" section; whatever is still genuinely open after promotion is recorded as a limit in the account's theory note. The operator approved all execution recommendations below on 2026-11-02, including Sol for bounded bulk work. These are execution decisions, not remaining approval gates:

1. **An ADR for retiring the phrase.** "Unique operational semantics" is a registered term with a collision-ledger row, and the library retired "distillation" through [ADR 053](../../reference/adr/053-retire-distillation-without-a-successor-term.md) and replaced "reach" through ADR 055. Recommended: one ADR, numbered at execution time (124 on 2026-11-02), that retires the phrase, names the successor wording, records why the formalizability conjecture behind it was wrong, and leaves the migrated-site inventory to the implementing commit messages. Promotion commits then carry `Decision: ADR 124`.
2. **Whether step 1 becomes its own note.** Recommended: yes, a short separate note; see step 2.
3. **The opacity note's new title.** Astra's proposal is "Opacity depends on the inspection question and budget". The rename is a relocation commit separate from the content edit.
4. **The side theory's destination.** Recommended: the log entry in step 5, not an unfinished proposal.
5. **The C11 behavior categories.** Recommended: a bounded ingest of WG14 N1570 sections 3.4.1 to 3.4.4 before promotion, so the four left-open cases rest on a retained quote rather than on the account's own statement. Sequenced in step 4.
6. **Delegation.** Astra proposes bounded extraction and migration batches to a worker with disjoint file ownership, keeping plan repair, integration, claim checks, commit ordering and closure. Within existing authority; the operator confirms.

## Order of extraction

The proposed form definition links the account's opacity section for the detailed treatment, and the account links step 1. Replacing the definitions first would leave a library note pointing into the workshop. So the durable notes come first: the formal-model note and the account (step 2), then the opacity note's content (step 4) if the definition is to point at it, and only then the definitions (step 1). The numbering below names the artifacts; the commit sequence at the end gives the order.

## Step 1: library definitions replaced in place

Both library files are replaced by the workshop texts, not relocated: the paths and inbound links stay, so no redirect and no relocation command is needed.

- `kb/theory/definitions/representational-form.md` takes the body of [the proposed form definition](./representational-form-definition.md). Keep the existing frontmatter and tags (`learning-theory`, `artifact-analysis`); rewrite the description to name the criterion and the opaque modifier. Drop the workshop header paragraph and the "Decisions and promotion" section. Repoint `./codification-definition.md` to `./codification.md`, the `../../theory/` prefixes to `./` or `../`, and the link to the account's opacity section to the promoted account note or the opacity note, whichever the approved placement makes the home of the detailed treatment. Add a footer link to the account note, labelled `grounds`, since the criterion and the modifier are derived there.
- `kb/theory/definitions/codification.md` takes the body of [the proposed codification definition](./codification-definition.md) the same way. Keep its tags, rewrite its description, drop its "Decisions and promotion" section, repoint `./representational-form-definition.md` to `./representational-form.md`, and add the same footer link to the account.
- The `AGENTS.md` vocabulary rows for Codification and Representational form keep their links. The Representational form row's gloss, "prompt is a consumption path, not a fourth form", stays true.

Before commit, search both promoted files for `kb/work/` and `../../work/`; the result must be empty. Validate with `commonplace-validate kb/theory/definitions`. Both notes have freshness baselines; the change marks their review pairs stale, which is expected for a substantive revision and needs no acknowledgement before commit.

## Step 2: the account becomes a theory note

[Step 2 of the workshop](./symbolic-form-and-codification.md) is extracted to `kb/theory/` as a new note with a claim title. The current heading, "Symbolic form is a language close to a formal semantics, and codification is the move into it", already has the shape. What changes on extraction:

- Add note frontmatter: description, `type: types/note.md`, tags `learning-theory` and `artifact-analysis`. Both tags are marked `complete: true`, so each tag head must link the new note or a child head that covers it; add the note to `kb/tags/artifact-analysis-README.md` and `kb/tags/learning-theory-README.md`.
- Remove workshop apparatus: the "Workshop context" section, the "Four questions" section's references to the review files, the "Decisions and promotion" section (its surviving limits become a `## Scope` or `## Open Questions` section in the note's own voice), and the pointers to review files. Keep the hypothesis attributed to Astra, since the note records whose formulation was adopted.
- Repoint links: `./implementation-and-shared-semantics.md` is folded into the note or kept as a second note (see below); `./representational-form-definition.md` and `./codification-definition.md` become the library definitions; `./where-meaning-is-settled.md` becomes the proposal from step 5 or is dropped; `./tarski-thread.md` and `./probe-response-2026-11-01-astra.md` are workshop-only and their content must be carried into the note or the ingests before the workshop is deleted.
- Footer links, labelled: the two definitions as `defined-in`; [opacity is a scale threshold](../../theory/opacity-depends-on-the-inspection-question-and-budget.md) as `extends`; [agentic systems interpret underspecified instructions](../../theory/agentic-systems-interpret-underspecified-instructions.md) and [fix what the executor cannot determine](../../theory/fix-what-the-executor-cant-determine-not-what-it-will.md) as `grounds`; [progressive constraining](../../theory/progressive-constraining-commits-only-after-patterns-stabilize.md) as `extends`.
- Sources are chosen by the claims the note retains, not carried over wholesale. The theory contract ([ADR 082](../../reference/adr/082-grounding-is-bounded-on-the-artifact-by-unquoted-sources.md)) allows at most five distinct ingests cited without a verbatim quotation paired to each in the note itself, and a source cited as evidence must be hosted in a body sentence; a footer-only citation is not allowed. Quotes retained in the ingest do not discharge the limit. The account currently uses the Tarski 1944 paper and Truth and Proof, the Church–Turing entry, and the two obfuscation papers in its body; the repair and clarification ingests serve only the side theory and are not cited. If the obfuscation evidence moves to the opacity note under the approved placement, the account cites those two papers there by link rather than as sources. Where a source is kept without a paired quote, count it; where the count would exceed five, pair a quote or split the note.

[Step 1](./implementation-and-shared-semantics.md), that an implementation supplies a formal model and not proof of shared semantics, is a self-standing claim the account depends on. Recommended: a second, shorter theory note with its own claim title, linked from the account as `grounds`. Folding it into the account would make one long note carry two claims.

The [Tarski thread](./tarski-thread.md) has no library destination of its own. Its settled part is already in the account. Its library audit is executed in step 4. Its open part, semantic closure and universality, is recorded as a limit in the account's scope section and otherwise left in Git.

## Step 3: migration of the retired phrase

Each site is read for reliance on the formalizability conjecture before it is reworded. Sites found on 2026-11-02, outside the workshop and outside frozen or retained material:

| Site | Change |
|---|---|
| `kb/theory/definitions/constraining.md` | Misuse case and footer label: "where the artifact has a unique operational semantics" becomes "where the artifact's language has a formal semantics or is close to one"; the footer link for the criterion points to representational form, the link for the move stays on codification. |
| `kb/reference/vocabulary-collision-ledger.md` | The `operational` row loses its codification sense and its guidance changes as the [follow-up](./follow-up-library-changes.md#vocabulary-collision-ledger) states. |
| `kb/tags/constraining-README.md` | The codification entry's gloss. |
| `kb/theory/designing-agent-memory-systems.md` | "fixed by a deterministic consumer" is wrong under the new account, which permits stochastic references with declared variation; reword to "held to a reference". |
| `kb/theory/exact-implementation-does-not-validate-a-requirement.md` | Wording only. |
| `kb/theory/theory-and-methodology-form-a-two-layer-execution-system.md` | Wording only. |
| `kb/theory/natural-language-meaning-is-coordination-among-learned-approximations.md` | "a checker with a unique operational semantics sits outside every learner" becomes a checker the language's users hold consumers to; the claim survives. |
| `kb/theory/agentic-systems-interpret-underspecified-instructions.md` | The paragraph that locates the difference in a compiler's "aim" at a unique operational semantics is the old argument; rewrite it to the held-to-reference difference, in the same pass as the impossibility paragraph in step 4. |
| `kb/articles/bootstrapping-an-autonomous-theory-builder.md` | Wording only; articles are for external readers, so gloss the successor wording at first mention. |

Left as they are: the three source ingests that gloss the phrase (Church–Turing, Plotkin, operationalism) keep it as a historical reference; `kb/agent-memory-systems/` is frozen; the retained trial bundle under `kb/reports/retained/` and the packet snapshots under other workshops are records.

Library links that cite codification "for the test" and should cite representational form instead were searched for on 2026-11-02. Of twenty-one labelled footer links to codification in `kb/theory/`, all describe the move or the crossing, none the criterion. The only link to repoint is the one inside constraining, covered above. Re-run the search before execution:

```
rg -n -o "\[[^]]*\]\([^)]*definitions/codification\.md\) — [a-z-]+: [^\n]{0,120}" kb/theory kb/tags kb/reference kb/articles
```

## Step 4: follow-ups with their own targets

Each is a separate library revision, listed in [follow-up library changes](./follow-up-library-changes.md):

- `kb/theory/opacity-is-a-scale-threshold.md` takes the two further sources, the scoped definition, and the path-gap statement of the reference's form; the title claim narrows to one source among three, so the title itself may change, which is a relocation commit on its own. Add the two obfuscation ingests as `evidenced-by`.
- The impossibility paragraph in `agentic-systems-interpret-underspecified-instructions.md` and its repeat in `traditional-software-can-bracket-executor-conformance-llm-systems.md`, rewritten to the narrower claim with the three Tarski-related ingests cited.
- The `evidenced-by` links from the two meaning notes to the repair and clarification ingests, and the `compares-with` link between those ingests.
- The C11 behavior-category ingest, WG14 N1570 sections 3.4.1 to 3.4.4, bounded to those sections, done before the account is extracted so its four left-open cases cite a retained quote. It is the one follow-up that precedes promotion rather than following it.

## Step 5: the side theory

[Where natural-language meaning is settled](./where-meaning-is-settled.md) goes to `kb/theory/proposals/` as a theory proposal if it earns one, otherwise to `kb/log.md`. The [theory proposal type](../../theory/types/theory-proposal.md) requires a finished text that opens with the import, names its trigger and cost, and carries a description beginning with "Proposal:" and no tags. The present file is a workshop draft with suspended claims and open questions, so it does not pass as it stands. Recommended: the log, with a one-paragraph entry recording the four features and the claim the account retained from it, the direction of authority. Reopen as a proposal only when a note cannot state its claim without the mechanism.

## Step 6: closure

Workshop closure follows the closure protocol in [`kb/work/COLLECTION.md`](../COLLECTION.md), not the retire-artifact procedure, which excludes workshops: extract, verify the successors, remove inbound workshop references, delete the directory, remove the `kb/work/README.md` entry. No redirects, since no library artifact links into a workshop.

- Before deletion, `rg -l 'formal-semantics-and-codification' kb/` must return only files under `kb/work/` that are themselves being deleted or whose references are dispositioned below.
- The five review files, the probe question and answer, the evidence ledger and the Tarski thread stay in Git history; the promoted notes cite nothing in them.
- Two workshops were promised material from here, and a link to the account does not deliver it, because the account deliberately excludes it. Acceptance for each: the [ideal-interpreter workshop](../ideal-interpreter/README.md) receives the probe answer's six interpretation statuses, its ambiguity contract and its assessment design, either copied into a file it owns or recorded there as an explicit disposition not to take them; the [institution-theory workshop](../institution-theory-import/README.md) receives the Tarski audit's result, which step 4 executes in the impossibility paragraphs, as a pointer to the revised notes plus the audit's two limits (hedged consistency claim, no statement about execution). Deletion waits on both.

## Commit sequence

Each commit is complete on its own and validates on its own. Relocation commits carry no content edits.

1. The C11 ingest (step 4), so the account can cite it.
2. ADR retiring the phrase (`kb/reference/adr/`), with the ledger row revised in the same commit, since the ledger is the ADR's register. `Decision: ADR 124`.
3. The formal-model note and the account note added to `kb/theory/`, with the tag heads updated. Their links point only at library files and at each other.
4. Opacity note: relocation commit for the rename, then the content commit with the two further sources and the detailed treatment. Opacity goes before the definitions so the form definition can point at it.
5. The two definitions replaced in place, linking the account and the opacity note, with `AGENTS.md` untouched. `Decision: ADR 124`.
6. The phrase migration across the sites in step 3, one commit, subject stating the count migrated and the count kept.
7. The impossibility paragraphs and the ingest links, one commit.
8. Log entry for the side theory.
9. Handoffs to the two workshops (step 6), one commit.
10. Workshop deletion and index entry removal.

Trailers on every commit: `Workshop: kb/work/formal-semantics-and-codification`, `Model:` for an agent commit.

## Verification

- The validator takes one target per run. After commits 3 through 7 run `commonplace-validate kb/theory`, `commonplace-validate kb/tags`, `commonplace-validate kb/reference` and `commonplace-validate kb/articles` separately; after the opacity rename also `commonplace-validate redirects`. Links from the definitions and the account must resolve, and the two `complete: true` tag heads must reach the new notes.
- The boundary-case checks in the [register](./decisions-and-open-questions.md#review-checks-not-wording-decisions), run against the promoted texts: policy clause, schema field, tensor operand, adopted prompt, human approval input, and the compiled and neural implementations behind one API classify the same way in the definitions and the account.
- A final search for the retired phrase returns hits only on an explicit allowlist: the retirement ADR, the collision ledger's historical note if one is kept, the three ingests that gloss the phrase, `kb/agent-memory-systems/`, `kb/reports/retained/`, and other workshops' snapshot packets. Any other hit is a missed site.
- Freshness: the changed and new notes show as stale or unreviewed; schedule their review pairs through the review system rather than acknowledging them, since the changes are substantive.

## Execution authority and adjustments

The operator approved all six choices in step 0 on 2026-11-02. The file lists remain a snapshot and are searched again during execution. Source ingests must not mention workshops: remove workshop references from the seven affected ingests, including their occasion fields, preserving the substantive research questions and source quotations. This explicit cleanup overrides verbatim occasion retention for those fields; do not add a historical-workshop allowlist.

The ADR type excludes migration inventories from the ADR body: record migrated sites and counts in implementing commits instead. The parent retains integration, verification, commit ordering and closure; Sol workers own disjoint source, extraction, migration and handoff batches. Execution state is recorded in `execution-state.md` until closure.
