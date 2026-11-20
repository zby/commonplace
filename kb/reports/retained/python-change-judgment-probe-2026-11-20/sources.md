# Background sources

Captured 2026-11-20 with trafilatura into the ignored cache
`kb/sources/.snapshots/`. Full copies stay there. This file records what was
captured, so a run can state exactly which text a session received.

The release case sends its sessions the 3.15 page. Whether the walrus sessions
receive the specification part of PEP 572 is not yet decided by the operator;
at present they receive nothing.

| Snapshot file | Source | SHA-256 of the snapshot file | Proposed audience |
|---|---|---|---|
| `pep-572-assignment-expressions.md` | [PEP 572 – Assignment Expressions](https://peps.python.org/pep-0572/) | `ec8413dfdbdc8de8863bdb706c3cda8610040f05bc8f9ba55f04ebf11b41ee69` | Respondents: syntax, semantics and examples only. Coordinator: the whole document. |
| `python-3-8-whats-new.md` | [What's New In Python 3.8](https://docs.python.org/3/whatsnew/3.8.html) | `cd6c8208f8185681222befb2196da0edd6a9f3c7ab04c490a7c9ad5327b8fd78` | Coordinator. The assignment-expression section duplicates the PEP's facts. |
| `python-3-15-whats-new.md` | [What's new in Python 3.15](https://docs.python.org/3.15/whatsnew/3.15.html), released 2026-10-09 | `c6418b141caccfd833401f4914787527fd098555017f4809eefb1615972a1ad5` | Respondents in the release case, whole. Coordinator. |
| `python-3-11-whats-new.md` | [What's New In Python 3.11](https://docs.python.org/3/whatsnew/3.11.html) | `7e27f8533c0c44a1553531c1fa4fa71c0bd54cf9a1f59465aa7e7b6058691a3c` | Not used. The release case moved to 3.15. |
| `lwn-pep-572-decision-making.md` | [PEP 572 and decision-making in Python](https://lwn.net/Articles/757713/), Jake Edge, 2018-06-20 | `4b6c45856cff33a6386204d115491ef4c976c2e9a032d83ec41a4113d4ec57d2` | Coordinator only. |
| `guido-transfer-of-power-2018.md` | [Transfer of power](https://mail.python.org/pipermail/python-committers/2018-July/005664.html), Guido van Rossum, 2018-07-12 | `f0e44c055fc4e461970b84c529c5612740436debae2b5b4fcab3212ba0694743` | Coordinator only. |

## Repeatability

The sources are not kept in the repository. Only the address and hashes are.
The snapshot files are git-ignored, and several are large; the 3.15 page alone
is about 184 KB.

Each snapshot file is a short capture header followed by the extracted text.
The hash in the table above covers the whole file, including the header's
capture date, so a fresh capture never matches it. The body hash below covers
only the extracted text and is the one to compare.

Captured with Trafilatura 2.3.1 on 2026-11-20.

| Snapshot file | Body size in bytes | SHA-256 of the body |
|---|---|---|
| `pep-572-assignment-expressions.md` | 45503 | `1af1a6ad648ceae4acca65a2da8e4947ea1467a3e180aca392f858ce79c5ac2b` |
| `python-3-8-whats-new.md` | 130655 | `52dee53af01caaba40249cdf02d212a14502446a9c5d0bc81f2314d92a7cb57b` |
| `python-3-15-whats-new.md` | 183257 | `00063d1ce8425486b052c8600fba8c6b2454a2bbf447ce086be72346c0dc9062` |
| `python-3-11-whats-new.md` | 127576 | `850de99806d6f37676eedc9d1d58229392ae694c7f8ef0903023fb6d1b3b0ffb` |
| `lwn-pep-572-decision-making.md` | 12595 | `9f9426ae8479474f300ad35d859dd29945a9634ee04f7c98cc1417714e236f01` |
| `guido-transfer-of-power-2018.md` | 2929 | `36b06e22676abe7c16dfa4fcb5b89fe4909dc101a96e8f3c8d44ddb39c89444e` |

The body is everything after the line that closes the capture header.

What the hashes do and do not give:

- They let someone who holds a copy confirm it is the text recorded here.
- They do not let anyone rebuild the text. A new capture matches only if the
  page is unchanged and the extractor behaves the same. The documentation
  pages are edited after release, so a mismatch is likely over time.
- A later run should therefore record its own capture and hashes, and treat
  this manifest as the description of what the 2026-11-20 design would have
  sent.

## Known defects and gaps

- **The 3.15 capture has four empty sub-lists in its summary.** The headings
  "Interpreter improvements:", "Significant improvements in the standard
  library:" and "New typing features:" are followed by nothing, and "C API
  improvements:" is partial. The two summary paragraphs and all detailed
  sections are intact. A session reads the full sections, so nothing is
  missing, but the empty headings should be removed or the page recaptured
  before a run.
- **The 3.15 page is about 184 KB.** The whole page goes to each release
  session. Check that the chosen model's context holds it with room to spare.
- **The 3.11 capture has the same summary defect.** It is no longer used.
- **The LWN capture includes a subscription banner and trailing index links.**
  Harmless for the coordinator.
- **No account of how Python 3.15 was received.** None was looked for. The
  release is six weeks old; the coordinator gathers what exists at readout.
- **None of the documentation pages is a pinned revision.** The 3.8 and 3.11
  URLs point at the live documentation. The 3.15 URL names its version, but
  the page can still be edited. The hashes above fix what was captured.
