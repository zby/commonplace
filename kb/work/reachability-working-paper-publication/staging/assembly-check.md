# Assembly check (2026-09-03)

Status of each item in the staging README's assembly check, after the first
full staging pass. "Pending" items are the work that remains before a release
candidate can be tagged.

| Check | Status | Notes |
|---|---|---|
| Source tag and every component's mode recorded | mode: done; tag: pending | Modes are in the manifest. No tag exists; creating one is the freeze decision and needs the operator. |
| Exact snapshots reproduce their tagged sources | pending | Supplement E was generated from the working tree at 8feceff2 and must be regenerated from the tag. |
| Adaptations have source-comparison review | pending | A, B, and D have not been read against their sources by anyone but their author. |
| Main paper coherent with links disabled | done | [completeness-check.md](./completeness-check.md): ten of ten stated; two notes. |
| Every load-bearing dependency discharged | done, pending review | Software house and representational form in A; the three Naur notes in B; program theory's tests in C; Gödel machine in the body and E; the rest summarized in the body or left as live links per the audit. |
| Direct scholarly references | pending | [references.md](./references.md) is complete for every entry the KB can support; every remaining gap carries a [verify] marker. |
| No placeholders or workshop-only links | pending at release | Staging files carry "pending" fields and [verify] markers by design. They must be gone from the released package. |
| Operator approval of the body and lifecycle | pending | Not requested. |

## Remaining work before a tag

1. Operator review of the six paper-specific definitions (A.6, A.8 to A.11)
   and of Appendix C's eight conditions and accounting rules. Everything else
   depends on these holding.
2. Resolve the [verify] markers in references.md against primary sources.
3. Recheck every Supplement D row against the fixed-parametric-state criterion
   and record the source or commit behind each code-inspected placement.
4. Decide whether the body should carry one sentence defining "adequate" or
   point to A.9 at first use.
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
