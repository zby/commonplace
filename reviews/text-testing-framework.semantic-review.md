=== SEMANTIC REVIEW: text-testing-framework.md ===

Claims identified: 15

Key claims:
1. "Software tests work because there's a spec, even if it's implicit" (Section 1)
2. "Free text can have specs too" (Section 1)
3. Six contract types enumerated: structural, audience, tone/voice, safety/privacy, truthfulness, actionability (Section 1)
4. Three-level test pyramid: Level A (deterministic), Level B (LLM rubric), Level C (cross-model/adversarial) (Section 2)
5. Level A is "fast, cheap, reliable"; Level B is "medium cost, high coverage"; Level C is "slower, higher confidence" (Section 2)
6. Four metamorphic test types: paraphrase, summarization, reformat invariance, reverse test (Section 3)
7. Four-step claim extraction + verification process (Section 3)
8. Six corpus compatibility checks (Section 4)
9. Five-stage production workflow (Section 5)
10. Four failure modes (Section 6)
11. Minimal starting checklist for single-note and corpus (Section 7)
12. The note is "source material" received 2026-02-21 (intro)
13. automated-tests-for-text.md is "the distilled observation" of this note (intro)

---

WARN:
- [Completeness] The six contract types in Section 1 omit an **accessibility contract** (readability level, alt text for images, plain-language requirements). The note frames contracts as text "specs" that parallel software specs, and accessibility is a standard dimension of text specifications in professional writing and publishing. Its absence means the enumeration, while useful, is incomplete as a reference framework for the space it claims to cover.

- [Completeness] The test pyramid (Section 2) places "cross-model / adversarial checks" at Level C but describes them as "slower, higher confidence." Adversarial prompting does not inherently yield higher confidence than LLM rubric grading — it probes for failure modes rather than measuring quality. Adversarial tests are better understood as complementary to rubric grading (finding failure cases the rubric misses) rather than as a strictly higher tier in a pyramid. The pyramid metaphor suggests each level subsumes or extends the one below, but adversarial checks serve a different function (stress-testing vs. scoring). This strains the pyramid analogy at Level C.

- [Completeness] The failure modes in Section 6 list four items but omit **false positives / over-flagging** — where deterministic or LLM checks reject good text. The note mentions "over-testing early" as a failure mode, but that concerns test suite scope, not individual check accuracy. In a production workflow where checks gate publication (Section 5), false positive rates matter as much as false negatives. The enumeration of failure modes is incomplete for its stated purpose.

- [Completeness] Section 4 ("Compatibility with a collection of texts") lists six corpus-level checks but omits **versioning / temporal consistency** — whether a new note is consistent with the current version of referenced notes rather than outdated versions. The note's own Section 5 mentions "regression suite with golden notes," implying temporal awareness, but the corpus compatibility checks in Section 4 don't account for temporal drift explicitly.

INFO:
- [Completeness] The contracts in Section 1 are described as examples ("for example") rather than as an exhaustive enumeration. This softens the completeness concern, but since the note frames itself as a "reference framework" (description field) and a "full framework" (intro), readers may treat the list as more comprehensive than intended. The gap between the "reference framework" framing and the "for example" qualifier could mislead.

- [Completeness] Section 3 ("Testing meaning indirectly") sits outside the three-level pyramid from Section 2. Metamorphic tests and claim extraction could belong to Level B (LLM rubric) or Level C (cross-model), but the note presents them as a separate section. This creates ambiguity about whether Section 3 is a fourth level, a cross-cutting concern, or a detailed elaboration of Levels B and C. For a reference framework, the relationship between Sections 2 and 3 is underspecified.

- [Completeness] The minimal starting checklist (Section 7) includes "clarity rubric" and "main point in first 2 sentences" for single-note checks, which are Level B (LLM rubric) checks — not Level A deterministic. But Section 5's production workflow puts only "deterministic + basic rubric" in CI unit tests. The minimal checklist therefore implies deploying LLM rubric checks from the start, which may conflict with the failure mode advice "over-testing early" (Section 6). The tension is not a contradiction but could use explicit acknowledgment.

- [Grounding alignment] The intro states automated-tests-for-text.md is "the distilled observation" of this note. The distilled note covers the same three-level structure but adds material not present in this source note: it connects the framework to document types, the type system, the artifact testing vs. prompt testing distinction, and the "build from failures" principle. The distilled note is therefore not purely a distillation of this source — it synthesizes this framework with other KB concepts. The "distilled observation" label understates the synthesis involved.

- [Internal consistency] The production workflow (Section 5) lists "CI integration tests — contradiction, taxonomy, duplication" at stage 3, positioning these as CI-level automation. But Section 6 warns "corpus checks miss context" as a failure mode. The workflow doesn't indicate that stage 3 is known to be unreliable, which could lead implementers to trust corpus-level CI checks more than the failure modes section suggests they should.

PASS:
- [Internal consistency] The three-level pyramid (Section 2) is internally consistent: the levels increase in cost and complexity. Level A items are all deterministic/regex-checkable; Level B items require LLM judgment; Level C items require multiple models or adversarial setups. No item is misplaced across levels.
- [Internal consistency] The contract types (Section 1) are non-overlapping. Each covers a distinct dimension of text quality: structure, audience, tone, safety, truth, action. No two contracts claim the same territory.
- [Internal consistency] The production workflow (Section 5) correctly sequences the pyramid levels: deterministic first (pre-commit), rubric second (CI unit), corpus third (CI integration), human last. This matches the cost/speed ordering from Section 2.
- [Internal consistency] The note's self-description as "source material" / "reference framework" is consistent with its structure: it presents a comprehensive framework without arguing for it or connecting it to other KB concepts. The distilled note (automated-tests-for-text.md) is where the argumentative work happens, which matches the stated relationship.
- [Grounding alignment] The link to automated-tests-for-text.md was followed and checked. The distilled note accurately reflects the pyramid structure and contract-based approach from this source note. No misattribution detected in the reverse direction.

Overall: 4 warnings, 4 info
===
