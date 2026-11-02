# Adoption plan

Drafted 2026-11-02 while the account and definitions were under Astra's final revisions. Part of the [workshop](./README.md). This file turns the [closure](./README.md#closure) clause and the [promotion checklist](./follow-up-library-changes.md#promotion-checklist) into an ordered sequence of commits with the files each one touches, so that promotion can be executed in one sitting once the operator authorizes it. Nothing here is authorized by the workshop itself; the sequence starts with the operator's decisions. File lists come from a search of the library on 2026-11-02 and should be re-run before execution.

## Step 0: decisions the operator makes before any edit

1. **Promote or reject.** The closure clause allows an explicit unresolved boundary or rejection instead of a forced replacement.
2. **The presentation choices** in the [question register](./decisions-and-open-questions.md#remaining-presentation-choices). Each has a recommendation; the promoted text is the decision, and the promoted definitions carry no open-questions section. Decisions that remain genuinely open move to the account's theory note as recorded limits.
3. **An ADR for retiring the phrase.** "Unique operational semantics" is a registered term with a collision-ledger row, and the library retired "distillation" through [ADR 053](../../reference/adr/053-retire-distillation-without-a-successor-term.md) and replaced "reach" through ADR 055. The same route is recommended here: one ADR that retires the phrase, names the successor wording, records why the formalizability conjecture behind it was wrong, and lists the sites migrated. Promotion commits then carry `Decision: ADR 1NN`.
4. **Where the detailed opacity treatment lives.** The register recommends a short definition in the form note and the mechanisms in the opacity note. That decides how much of the account's opacity section is duplicated into the note in step 3.

## Step 1: library definitions replaced in place

Both library files are replaced by the workshop texts, not relocated: the paths and inbound links stay, so no redirect and no relocation command is needed.

- `kb/theory/definitions/representational-form.md` takes the body of [the proposed form definition](./representational-form-definition.md). Keep the existing frontmatter and tags (`learning-theory`, `artifact-analysis`); rewrite the description to name the criterion and the opaque modifier. Drop the workshop header paragraph and the open-questions section. Repoint `./codification-definition.md` to `./codification.md` and the `../../theory/` prefixes to `./` or `../`. Add a footer link to the account note from step 2, labelled `grounds`, since the criterion and the modifier are derived there.
- `kb/theory/definitions/codification.md` takes the body of [the proposed codification definition](./codification-definition.md) the same way. Keep its tags, rewrite its description, repoint `./representational-form-definition.md` to `./representational-form.md`, and add the same footer link to the account.
- The `AGENTS.md` vocabulary rows for Codification and Representational form keep their links. The Representational form row's gloss, "prompt is a consumption path, not a fourth form", stays true.

Validate with `commonplace-validate kb/theory/definitions`. Both notes have freshness baselines; the change marks their review pairs stale, which is expected for a substantive revision and needs no acknowledgement before commit.

## Step 2: the account becomes a theory note

[Step 2 of the workshop](./symbolic-form-and-codification.md) is extracted to `kb/theory/` as a new note with a claim title. The current heading, "Symbolic form is a language close to a formal semantics, and codification is the move into it", already has the shape. What changes on extraction:

- Add note frontmatter: description, `type: types/note.md`, tags `learning-theory` and `artifact-analysis`. Both tags are marked `complete: true`, so each tag head must link the new note or a child head that covers it; add the note to `kb/tags/artifact-analysis-README.md` and `kb/tags/learning-theory-README.md`.
- Remove workshop apparatus: the "workshop draft" header, the "Four questions" section's references to the review files, the open-questions section (its surviving items become a `## Scope` or `## Open Questions` section in the note's own voice), and the pointers to review files. Keep the hypothesis attributed to Astra, since the note records whose formulation was adopted.
- Repoint links: `./implementation-and-shared-semantics.md` is folded into the note or kept as a second note (see below); `./representational-form-definition.md` and `./codification-definition.md` become the library definitions; `./where-meaning-is-settled.md` becomes the proposal from step 5 or is dropped; `./tarski-thread.md` and `./probe-response-2026-11-01-astra.md` are workshop-only and their content must be carried into the note or the ingests before the workshop is deleted.
- Footer links, labelled: the two definitions as `defined-in`; the seven ingests as `evidenced-by`, worded as qualifying where the ledger says so; [opacity is a scale threshold](../../theory/opacity-is-a-scale-threshold.md) as `extends`; [agentic systems interpret underspecified instructions](../../theory/agentic-systems-interpret-underspecified-instructions.md) and [fix what the executor cannot determine](../../theory/fix-what-the-executor-cant-determine-not-what-it-will.md) as `grounds`; [progressive constraining](../../theory/progressive-constraining-commits-only-after-patterns-stabilize.md) as `extends`.
- The theory collection's unquoted-source limit is five; the account cites only ingests with retained quotes, so it is within the limit, but check again after edits.

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
- The C11 behavior-category ingest, if the operator wants the left-open section grounded by a retained quote rather than by the account's own statement.

## Step 5: the side theory

[Where natural-language meaning is settled](./where-meaning-is-settled.md) goes to `kb/theory/proposals/` as a theory proposal if it earns one, otherwise to `kb/log.md`. The [theory proposal type](../../theory/types/theory-proposal.md) requires a finished text that opens with the import, names its trigger and cost, and carries a description beginning with "Proposal:" and no tags. The present file is a workshop draft with suspended claims and open questions, so it does not pass as it stands. Recommended: the log, with a one-paragraph entry recording the four features and the claim the account retained from it, the direction of authority. Reopen as a proposal only when a note cannot state its claim without the mechanism.

## Step 6: closure

- Remove the workshop directory with the [retire-artifact](../../instructions/retire-artifact.md) procedure and remove its entry from `kb/work/README.md`. The five review files, the probe question and answer, the evidence ledger and the Tarski thread stay in Git history; the account's note cites nothing in them.
- The ideal-interpreter workshop and the institution-theory workshop were promised material from here (the interpretation statuses, the Tarski audit). Post the pointers to the promoted notes in their READMEs before deletion.

## Commit sequence

Each commit is complete on its own and validates on its own. Relocation commits carry no content edits.

1. ADR retiring the phrase (`kb/reference/adr/`), with the ledger row revised in the same commit, since the ledger is the ADR's register. `Decision: ADR 1NN`.
2. The two definitions replaced in place, with `AGENTS.md` untouched. `Decision: ADR 1NN`.
3. The account note and the step-1 note added to `kb/theory/`, with the tag heads updated. The definitions' footer links to the account go in this commit, not in commit 2, so commit 2 does not link a file that does not yet exist.
4. The phrase migration across the sites in step 3, one commit, subject stating the count migrated and the count kept.
5. Opacity note: relocation commit if the title changes, then the content commit.
6. The impossibility paragraphs and the ingest links, one commit.
7. Log entry for the side theory.
8. Workshop retirement and index entry removal.

Trailers on every commit: `Workshop: kb/work/formal-semantics-and-codification`, `Model:` for an agent commit.

## Verification

- `commonplace-validate kb/theory kb/tags kb/reference` after commits 2 through 6; links from the definitions and the account must resolve, and the two `complete: true` tag heads must reach the new notes.
- The boundary-case checks in the [register](./decisions-and-open-questions.md#review-checks-not-wording-decisions), run against the promoted texts: policy clause, schema field, tensor operand, adopted prompt, human approval input, and the compiled and neural implementations behind one API classify the same way in the definitions and the account.
- A final search for the retired phrase outside the ingests, the frozen collection and retained reports returns nothing.
- Freshness: the changed and new notes show as stale or unreviewed; schedule their review pairs through the review system rather than acknowledging them, since the changes are substantive.

## What this plan does not decide

Whether to promote, the presentation choices, the ADR number, the opacity note's new title, and whether step 1 becomes its own note are the operator's. The file lists are a snapshot and may have moved by execution time.
