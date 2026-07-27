# Migration plan

This is a classification-led migration, not a global replacement.

## 1. Fix the decision rule

Apply this order to each occurrence:

1. Use the precise artifact name when it is available: **note**, **policy**, **instruction**, **memory record**, **review document**, or another concrete noun.
2. Use **prompt** when the sentence concerns material actually supplied, or explicitly assembled to be supplied, as model input.
3. Use **natural-language artifact**, **natural-language form**, **natural-language content**, or **natural-language instruction** when the representational category matters.
4. Preserve **prose** when it has an editorial meaning, occurs in a quotation or historical record, or names existing review machinery.

This ordering prevents both weak abstractions and overuse of **prompt**. A precise noun is better when the category adds nothing; **prompt** is better when the consumption path is the point; the broader natural-language term remains necessary for the representational distinction.

## 2. Build the migration ledger

Create `migration-ledger.md` with one row per category-bearing occurrence. This table is the migration's control surface and final deliverable:

| id | location | current wording | classification | replacement | rationale | implementation | verification |
|---|---|---|---|---|---|---|---|
| stable row id | `path:line` | quoted phrase | precise noun / prompt / natural-language term / preserve prose | proposed wording | why this category applies | pending / changed / preserved | pending / verified |

Seed the ledger from exact `prose artifact(s)` hits. Then expand it to technical compounds and contrasts such as `prose form`, `prose/symbolic`, `prose instruction`, `prose record`, and `prose-to-code`. Do not inventory every ordinary use of the word until the targeted categories are covered; the final residual audit catches the remainder.

If one table becomes unwieldy, keep `migration-ledger.md` as a manifest and split the rows into linked batch tables. Row IDs remain globally unique, every occurrence belongs to exactly one batch, and batches own non-overlapping file sets so one file is never edited by two subagents. The manifest records the batch links and reconciled totals; verification may proceed batch by batch but must finish with a whole-ledger coverage check.

Keep [lessons-learned.md](./lessons-learned.md) available during the migration so useful methodological observations are not lost. Let the work determine what is worth recording and what shape any reusable methodology should take.

## 3. Migrate the vocabulary spine

Change the artifacts that define or govern the category before changing their dependents:

1. `AGENTS.md`
2. `kb/notes/definitions/representational-form.md`
3. `kb/notes/axes-of-artifact-analysis.md`
4. `kb/notes/definitions/codification.md`
5. `kb/notes/definitions/constraining.md`
6. `kb/notes/definitions/reach-assessment.md`

This pass establishes **natural-language / symbolic / distributed-parametric** as the canonical contrast and records **prompt** as a consumption-path shorthand, not a fourth form or a synonym for every natural-language artifact.

## 4. Migrate dependent artifacts by cohort

Process the maintained library in small groups so each diff can be judged in context:

1. theory notes;
2. current reference documentation and ADRs;
3. instructions and type guidance;
4. agent-memory-system and agentic-system reviews.

Preserve each external system's actual architecture. A stored memory record is not necessarily a prompt; a generated system message or assembled model-input view is. Where an artifact has mixed operative parts, name the natural-language and symbolic parts separately.

Do not edit captured sources, generated reports, or historical workshop outputs as part of these cohorts. If a maintained artifact quotes or discusses their old wording, distinguish the quoted source vocabulary from Commonplace's current vocabulary.

In particular, preserve the historical terminology in both captured versions of **Where It Lives Is Not What It Is**. Any future terminology revision to that article is a separate editorial decision, not a mechanical consequence of this corpus migration.

Split each cohort into semantic and simple bulk cases. The primary agent keeps cases that require category judgment, alter a claim, touch the vocabulary spine, or interact with mixed operative parts. Pre-classified cases whose replacement follows directly from the ledger may be assigned to Luna subagents as non-overlapping file batches.

For Luna batches:

- give each subagent an explicit file list and ledger row IDs;
- do not let two subagents edit the same file;
- have subagents edit their assigned files and report the completed row IDs and any cases they declined as ambiguous;
- keep the primary agent responsible for the shared ledger, integration review, and reclassification of declined cases.

The subagents execute already-decided replacements; they do not expand the migration scope or invent new category rules.

## 5. Audit residual uses of prose

Run a broad `prose` search after the targeted migration and classify every remaining hit in maintained library artifacts. Expected valid survivors include:

- clear prose, body prose, in-prose links, and other editorial uses;
- the prose review bundle and named prose gates;
- quotations and faithful descriptions of source terminology;
- historical ADR or experiment wording whose alteration would erase provenance.

Add non-obvious deliberate survivors to the ledger. The goal is an explainable residual set, not zero occurrences of the ordinary word.

## 6. Validate semantic and structural integrity

For each cohort:

- inspect the diff for changes in meaning, not just vocabulary;
- run `commonplace-validate` on every changed KB artifact;
- run `git diff --check`;
- rerun the targeted and residual searches;
- review the vocabulary spine against one question: did any edit collapse the broad category “interpreted as natural language” into the narrower path “sent to a model”?

Run the full test suite only if implementation, schemas, validation behavior, or other executable surfaces change. Pure terminology edits still require deterministic KB validation and link checking.

## 7. Extract durable results

Record the durable rationale in an ADR or in an explicit revision rationale attached to the representational-form definition. It must preserve the decision rule and explain why **prompt** is narrower than **natural-language artifact**.

Before closure, review the lessons that accumulated and extract any durable methodology they genuinely support. A later `symbolic`/`programmatic` investigation should be able to reuse that result without depending on this workshop.

Do not delete the workshop yet: the completed migration table remains available for the terminal verification pass.

## 8. Verify the completed table

The last step of the migration run is a fresh verification of the produced table against the resulting corpus. For every row, confirm that:

- the recorded location and classification cover the original occurrence;
- the implemented wording matches the recorded disposition;
- intentional survivors still satisfy an allowed residual class;
- changed files pass deterministic validation;
- targeted and broad residual searches reveal no unrecorded in-scope category uses.

Mark a row `verified` only from this pass, not merely because its implementing agent reported completion. If verification finds an error or missing occurrence, reopen the affected rows, correct the corpus or table, and rerun the verification; the terminal successful action remains verification of the whole table.

Workshop closure—deleting this directory and removing its active-workshop entry—follows acceptance of the verified result rather than being folded into the migration run.

Suggested commit boundaries:

1. canonical vocabulary spine and durable decision;
2. dependent library migration;
3. residual audit, deliberate exceptions, and final table verification.
