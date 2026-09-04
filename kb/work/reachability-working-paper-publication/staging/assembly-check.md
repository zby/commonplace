# Assembly check (2026-09-04)

Status of each item in the staging README's assembly check after the
source-freshness and primary-reference pass. "Pending" items are the work that
remains before a release candidate can be tagged.

| Check | Status | Notes |
|---|---|---|
| Source tag and every component's mode recorded | mode: done; tag: pending | Modes are in the manifest. No tag exists; creating one is the freeze decision and needs the operator. |
| Exact snapshots reproduce their tagged sources | current source: done; tag: pending | Supplement E matches the live article at b772b67f after the declared mechanical transformations. It must still be regenerated from the release tag. |
| Adaptations have source-comparison review | done for source alignment | A, B, and D were compared with their declared sources on 2026-09-04. Appendix A's omitted theory-mediated source was restored; D differs only by its declared Appendix C pointer. |
| Main paper coherent with links disabled | done | [completeness-check.md](./completeness-check.md): ten of ten stated against b772b67f; one body-to-appendix routing choice remains. |
| Every load-bearing dependency discharged | done, pending operator review | Software house, representational form, and theory mediation are in A; the three Naur notes are in B; program theory's tests are in C; Gödel machine is in the body and E; the Commonplace comparison now names its evidence; the rest is summarized in the body or left as live links per the audit. |
| Direct scholarly references | done | [references.md](./references.md) has no verification markers, names all twenty compared constructions, and records the source or commit behind each code-inspected placement. |
| No placeholders or workshop-only links | pending at release | Only the deliberate paper-version, source-tag, status, and release-path fields remain pending. They must be resolved in the released package. |
| Operator approval of the body and lifecycle | pending | Not requested. |

## Remaining work before a tag

1. Operator review of the six paper-specific definitions (A.6, A.8 to A.11)
   and of Appendix C's eight conditions and accounting rules. Everything else
   depends on these holding.
2. Recheck every Supplement D row against the fixed-parametric-state criterion.
3. Decide whether the body should carry one sentence defining "adequate" or
   point to A.9 at first use.
4. Run the complete-package external-reader review with hyperlinks disabled.
5. Choose the paper version and tag name, tag, regenerate Supplement E from
   the tag, and fill the "pending" provenance fields.

## Consistency notes from this pass

- A.9 says an adequate state's changes "do not require later rescue". C.6 now
  defines rescue as a human act in an internal role after the start, so the two
  agree.
- The paper body's Schmidhuber quotation now carries its section location
  (§2.4), the one gap the completeness check found in the body itself.
- Appendix C item numbering: the comparison article had seven conditions; C.4
  has eight because "not one lucky path" is separated from "internal decisions
  stay internal". Supplement D's pointer does not depend on the numbering.
- Appendix A now names the theory-mediated learning note whose definition A.5
  adapts.
- Supplement D's twenty rows and References' twenty construction entries agree;
  the Commonplace entry names the retained evidence and the code-inspected
  placements record their pinned commits.
