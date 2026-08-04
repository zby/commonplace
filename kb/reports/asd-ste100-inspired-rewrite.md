# ASD-STE100-inspired rewrite experiment

This report records what the rewrite experiment learns. It does not define the rewrite procedure. The operative instruction is `kb/instructions/asd-ste100-inspired-rewrite.md`.

The reference point is [ASD-STE100 Simplified Technical English, Issue 9](https://www.asd-ste100.org/assets/files/ASD-STE100_ISSUE9.pdf). The experiment is inspired by the standard and does not claim compliance.

## Starting departures from ASD-STE100

- Do not enforce the approved-word dictionary. Commonplace depends on a specialized theoretical vocabulary.
- Do not impose a fixed sentence or paragraph length. Shortness is a preference, not a limit.
- Prefer active voice, but preserve passive voice when the actor is unknown, irrelevant, or less important than the relation.
- Permit `-ing` forms, complex verb forms, and multi-word terms when they carry necessary meaning.
- Preserve titles, headings, frontmatter, links, code, quotations, and registered identifiers during the initial body-prose experiment.
- Preserve semantic content whenever a style preference conflicts with it.
- Do not copy the standard's dictionary or substantial rule text into the repository. Record local rules in original, paraphrased language.

## Ideas to test later

- Compare body-only rewriting with separate title-and-description rewriting.
- Test whether the rewrite improves extraction of claims, mechanisms, and scope boundaries.
- Measure token count as well as correctness; shorter sentences can make a note longer.
- Compare results in isolated-note and crowded multi-note contexts.
- Track recurring departures before adding or removing any rule from the instruction.

## Per-use log

Add one entry after each rewrite:

```markdown
### YYYY-MM-DD — <note path>

- Changes: <what the rewrite changed>
- Departures: <which style pressure was not followed and why>
- Observed effects: <helpful, harmful, or uncertain effects>
- Ideas: <possible changes to the experiment; write "none" if there are none>
- Disposition: <kept, partially kept, or reverted>
```

### 2026-08-04 — kb/notes/frontloading-spares-execution-context.md

- Changes: Split dense causal and contrastive sentences, made actors explicit, and added short logical transitions while preserving the claim, examples, boundaries, and terminology.
- Departures: Retained specialized terms, passive constructions, parenthetical qualifications, long lists, and the original linked footer where changing them could reduce precision or alter registered relationships.
- Observed effects: The distinction between instruction size and realized execution context became easier to scan, and the rewrite made the validity and stopping conditions more explicit. But sentence splitting added repetition and weakened some semantic connections. Independent reviews found five concrete failures: the opening lost definitional force and moved the temporal qualifier; an appositive definition became a separate consequence; one list item lost parallelism and weakened a defining restriction; `enough` stopped qualifying all refresh alternatives; and the codification condition briefly detached assigned consequences from the symbolic artifact. The corrected draft was still 3.7% longer than the original.
- Ideas: Treat sentence syntax as semantic content. When a sentence is split, explicitly restate the definition, attachment, shared qualifier, or other relation that the original syntax carried. Compare any comprehension gain against increased token count.
- Disposition: Reverted. Local improvements did not justify the remaining attachment errors and added length.

### 2026-08-04 — kb/notes/frontloading-spares-execution-context.md (second split-preservation pass)

- Changes: Split selected dense sentences, made several causes and contrasts explicit, and used active voice where the actor was clear. Explicitly restated the opening definition's input restriction, the parent-to-sub-agent cause, the shared refresh sufficiency requirement, and the codification condition.
- Departures: Kept specialized vocabulary, the static list, the linked footer, and several longer or passive sentences. In particular, kept the operation-and-complexity apposition, validity-window definition, stable-contract apposition, and constitutive causal clause intact when splitting could weaken their relations. Repeated the refresh qualifier across all alternatives even though this added words.
- Observed effects: The selected splits make the procedure-cost chain, pointer example, consumer-relative boundary, stopping condition, and architecture mechanism easier to scan. The revised preservation rules prevented the first pass's known attachment failures: definitional force and timing remain explicit, appositive identities remain attached, the static list remains parallel, `enough` applies to every refresh alternative, and formal semantics or assigned consequences still modify the symbolic artifact. The note grew from 1,028 to 1,078 words, an increase of 50 words (4.9%).
- Ideas: Compare the easier scanning against the 4.9% size increase in an extraction or comprehension test. Test whether repeated shared qualifiers improve reliable extraction enough to justify their token cost.
- Disposition: Kept.
