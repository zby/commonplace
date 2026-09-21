# Draft accounting after second-check fixes

This record covers the current staged package on 2026-09-21, including the
colocated definition checks. It is accounting for migration review, not
authorization to edit the library. Counts use whitespace-delimited words over
complete files, including frontmatter and link footers; SHA-256 values cover
complete bytes. Bounded consumer edits and the companion promotion delta
remain unapplied and are not included.

## Source drift and current candidates

Thirteen originals still match the source hashes recorded when drafting began.
The analysis skill changed in the library on 2026-09-21 (`281532ed`, agent
memory analysis became a parent-commissioned instruction). The staged skill was
rebased on that version: its memory-specialist paragraph now matches the
library, and it differs only in the five ontology hunks. The skill row below
records the rebased original. The initial
per-author counts and independent-review hashes describe earlier draft bytes;
current candidate hashes below supersede them for accounting.

| Original | Recorded/current SHA-256 | Words | Candidate body or bodies | Candidate SHA-256 | Words |
|---|---|---:|---|---|---:|
| `kb/notes/definitions/theory-refinement.md` | `cd8d471d8a0f8573429acf35feba4afdad4378481660c8f16a49c6233ac69a1d` | 2,443 | `definitions/addressable-theory.md`; `definitions/conjectural-learning.md`; `definitions/tentative-theory.md` | `6976b5813eba7cec630f10959874b0fda18fa421a13b0bc0feeb2bdab52d3ddd`; `266656f57e1d9761a06cb484ea45ad8a1bc22dded424d6f3cdadd7002c827266`; `635c4e9fc4275d9fac149fd5b8530a8f143c65c8dff617adf077debb9a832baa` | 669; 1,623; 584 |
| `kb/notes/definitions/learning-by-theory-refinement.md` | `514768489bc85bf179a388e50da8e98f0905b18378329791ba2685abea004a85` | 1,008 | `notes/commonplace-studies-conjectural-learning-through-retained-theories.md` | `98b1f2e9304b5a93ef3e0e5afcf08fe7d7dd585272891e024cfdfab5602b94af` | 1,236 |
| `kb/notes/reflective-theory-refinement-has-three-separate-lineages.md` | `327d976fc90189ed588351fcb1ddae79565d0eb391d82b97756e02228a850149` | 1,810 | `rewrites/kb/notes/reflective-theory-refinement-has-three-separate-lineages.md` | `d90555fd73a4e85318d28de5563eb2ec6805a2f72284c91cb5a1d9833ec137b6` | 970 |
| `kb/notes/reflective-theory-refinement-needs-interpretation-and-retention.md` | `ee79a5fb55740cea0445367a625084c34e77cbacf8b51733663925366205131c` | 1,408 | `rewrites/kb/notes/reflective-theory-refinement-needs-interpretation-and-retention.md` | `e03936bbe216befee43f1dc0686e435f6326208911c3fefacdc42a6397a0483c` | 1,405 |
| `kb/notes/disconnected-witnesses-do-not-establish-a-causal-path-through-theory.md` | `b7713d0b52c0a355fbeeda9989677f784f992405254c15bd4d2f8f23e234d61b` | 865 | `rewrites/kb/notes/disconnected-witnesses-do-not-establish-a-causal-path-through-theory.md` | `adf6e8cc051b8393480af405300c143c03d2f5cb331f4268691e3bb5187b6e10` | 971 |
| `kb/notes/learning-by-theory-refinement-may-improve-sample-efficiency.md` | `1c82a7a7acaab785ef5de3a6b62e8cd6a0924475b6fd79f21bca60930ef4e1c7` | 3,315 | `rewrites/kb/notes/learning-by-theory-refinement-may-improve-sample-efficiency.md` | `2e28eb95469d78c80d6e86a450c66e703755259ceae24632c92f43a6d2404212` | 3,382 |
| `kb/notes/proposals/retained-theories-compared-with-retained-traces-under-resource-limits.md` | `98b349fc4ccfa177ef8825b09fc2f879ffbf9a87edcecce562fe1d532a4ee37b` | 3,451 | `rewrites/kb/notes/proposals/retained-theories-compared-with-retained-traces-under-resource-limits.md` | `6b7730042565d128bb1fc31a380d1e1db089487299e1f0ed5e17d0fe70680be4` | 1,543 |
| `kb/notes/definitions/theory-builder.md` | `29829e95a7c1ae0972b700a90e593a0c254e7a48a5b57eedece1a31aca74ddcd` | 1,903 | `rewrites/kb/notes/definitions/theory-builder.md` | `a7a600dcc0f66e3db7eb2db7474800ab7eed9304e76e6ed4a4157933dd7a9f09` | 1,978 |
| `kb/notes/definitions/reflective-theory-builder.md` | `f0d22844207f280063e7ca6867a45562d2d858a3ec15f1ecc381555017efc2c2` | 1,000 | `rewrites/kb/notes/definitions/reflective-theory-builder.md` | `354c47cc9de1751fd661b49ddcafe2e11b5a0b29313b668ae6b1ca3f925d61b5` | 1,104 |
| `kb/notes/evidence/three-2026-harnesses-retain-editable-rules-or-weights-not-rationale.md` | `b699380802792af88112f5d30833498d731c18d37c02f1290f49150572185885` | 1,264 | `rewrites/kb/notes/evidence/three-2026-harnesses-retain-editable-rules-or-weights-not-rationale.md` | `6775688e7f69bd7bb5f462a4edd45d3993b24b9961c26b0eb5af574268b5c778` | 1,489 |
| `kb/instructions/analyse-agentic-system/SKILL.md` | `009be45a65185d2646a7545a4b597a0c838c8f16b428618c50051f79aefdb096` | 4,321 | `rewrites/kb/instructions/analyse-agentic-system/SKILL.md` | `7ebf26d554308db149d93390d3d77b3909f16d36f9fdcba6b83c9187de99592b` | 4,635 |
| `kb/types/agentic-system-analysis-result.md` | `73f20334e9d288dc0b32647a4eaef60bcebaa73da6b4eb2708e3439c19c01f80` | 3,783 | `rewrites/kb/types/agentic-system-analysis-result.md` | `1a760014f9a2007c29d7ae1e94599da9f8022875848142673bfea3c9d3f9f2bd` | 3,976 |
| `kb/articles/learning-by-theory-refinement-with-fixed-models.md` | `63e3da875032faede95c4a1cfa32f97b770d99dbf2ce367f11ece12a9cf6af20` | 3,753 | `rewrites/kb/articles/learning-by-theory-refinement-with-fixed-models.md` | `2e7ca1c2fede9e2c7b74a6c99d1c77426f57c48af828391fb7c483b826fad99d` | 3,181 |
| `kb/articles/testing-the-theory-refinement-program.md` | `f9736b8227d5150112b5f06da1c16f1aa625c8cd44441d0e7770d0529d371a29` | 4,178 | `rewrites/kb/articles/testing-the-theory-refinement-program.md` | `7da720a1de64e596a669134e101fdecaf8a79a6be51275f5859c893988830640` | 5,089 |

The first two originals jointly feed the three definitions and research
companion. The checks below are retained workshop material newly destined for
the library, not an additional definition or disposable scaffolding.

| Additional retained artifact | SHA-256 | Words |
|---|---|---:|
| `definitions/conjectural-learning-checks.md` | `011cfb3343e2d4fca27ff6d9b1730ad89052313a2d47fa6c21b677dc022004b8` | 1,112 |

## Simplification accounting

| Measure | Words |
|---|---:|
| Core baseline: two old definitions plus lineage | 5,261 |
| Three new definitions, research companion, and new lineage | 5,082 |
| Core including the retained checks | 6,194 |
| All fourteen originals | 34,502 |
| Sixteen replacement bodies before checks | 33,835 |
| Full seventeen-file candidate package | 34,947 |
| Net library word change, including checks | **+445** |

The sixteen replacement bodies are 667 words shorter than the
originals. Retaining the 1,112-word checks file makes the full package
445 words longer. The earlier claim of a 1,640-word net reduction
no longer describes the current package. Restored qualifications and preserved
checks are counted rather than dropped to maintain that claim. The core
without checks is 179 words shorter; including checks it is 933 words longer.

The core moves from four defined concepts to three, but from two definition
files to three. The research companion, lineage note, and checks file are not
definitions. Builder definitions remain two files and two concepts; the
approved reflective-builder scope difference is documented separately.
Classical repair remains a bounded precedent rather than the genus definition.
The package therefore reduces defined concepts and departure apparatus, but
does not reduce file count or total library words. Migration review must assess
that tradeoff against the workshop simplification requirement.

Textual overlap, computed by concatenating the table rows in order and appending
the checks, then applying `difflib.SequenceMatcher` to whitespace tokens with
`autojunk=False`: 19,623 retained, 14,876 removed, and
15,321 added. These are text counts, not claim counts; links and
frontmatter participate. Retained workshop checks count as added library text.

## Final paths

| Intended final path | Slug characters |
|---|---:|
| `kb/notes/definitions/addressable-theory.md` | 18 |
| `kb/notes/definitions/conjectural-learning.md` | 20 |
| `kb/notes/definitions/tentative-theory.md` | 16 |
| `kb/notes/definitions/conjectural-learning-checks.md` | 27 |
| `kb/notes/commonplace-studies-conjectural-learning-through-retained-theories.md` | 66 |
| `kb/notes/conjectural-learning-has-distinct-precedents.md` | 44 |
| `kb/notes/a-complete-theory-path-does-not-establish-improved-capacity.md` | 59 |
| `kb/notes/disconnected-witnesses-do-not-establish-a-causal-path-through-theory.md` | 68 |
| `kb/notes/retained-theories-may-improve-sample-efficiency.md` | 47 |
| `kb/notes/proposals/retained-theories-compared-with-retained-traces-under-resource-limits.md` | 69 |
| `kb/notes/definitions/theory-builder.md` | 14 |
| `kb/notes/definitions/reflective-theory-builder.md` | 25 |
| `kb/notes/evidence/rules-weights-and-missing-rationale-do-not-settle-conjectural-learning.md` | 70 |
| `kb/instructions/analyse-agentic-system/SKILL.md` | 5 |
| `kb/types/agentic-system-analysis-result.md` | 30 |
| `kb/articles/conjectural-learning-with-fixed-models.md` | 38 |
| `kb/articles/testing-the-conjectural-learning-program.md` | 40 |

## Verification

Before the follow-up review, all seventeen candidate files and twenty changed
workshop records passed
individual `commonplace-validate <explicit-file> --full` runs cleanly: 37 files,
no warnings or failures. Typed drafts also passed local link and schema checks.
The follow-up changed the sample-efficiency example and preserved the failed-test
constraint in both articles; all eleven affected bodies and records passed
explicit-path full validation cleanly. No pytest or experiment run is
appropriate for these Markdown-only changes.

The six definition checks and fourteen cases retain their expected
classifications. The second-check fixes add no membership condition. The
earlier approved reflective-builder scope difference remains recorded in the
decision record; unchanged learning cases do not erase that difference.

A direct comparison with the original testing supplement confirms that its
adopted hypotheses and refuters, ten protocol declarations, and run-path
account are unchanged apart from link rebasing and whitespace. Parent review
checked the integrated edits; the reconstruction and codification fixes also
received a separate read-only check. Earlier full-package independent reviews
are historical evidence, not reviews of these newly changed bytes.

## Remaining migration work

- Apply the companion promotion delta from workshop remnants and the exact
  bounded consumer edits, including the codification paragraph, builder gloss,
  and reflective-system recurrence label. Recompute totals after those edits.
- Land the evidence and disconnected-witness bodies at their current library
  paths before the pure evidence-note relocation, as stated in the closure plan.
- Rebase workshop links, repair final names and fragments, and update navigation
  and redirects. Validate the resulting library files.
- Resolve source-commentary updates and minimal peer-workshop reference repairs
  under the later migration commission. No peer experiment is redesigned.
- Promote the checks beside the definition before deleting workshop scaffolding.
- The four RSI ingests are now retained in separate commit `b1cf00c6`; their
  earlier untracked-source blocker is resolved. This pass leaves them unchanged.
