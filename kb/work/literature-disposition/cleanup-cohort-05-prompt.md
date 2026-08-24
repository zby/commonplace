# Agent prompt — cleanup cohort 05

Self-contained. Point one agent at this file; it needs nothing else from this
conversation. Cohorts are disjoint on both notes and ingests, so all six run in
parallel with no coordination.

**Scope:** 5 targets, 5 ingests, 0.31 MB of snapshot. Five targets over five ingests.

---

Work cleanup cohort 05 in the Commonplace repository at
`/home/zby/llm/commonplace`.

Read `kb/work/literature-disposition/cleanup-cohort-05.md` for your frozen
targets, then `kb/work/literature-disposition/cleanup-procedure.md` — follow its
six steps and its **Executing a cohort** section, which carries the literal
grounding and re-ingest invocations.

**Do step 1 first and do it properly.** Inventory each target's load-bearing
claims *from the note itself, before opening any source*, and write them into the
manifest as `ID | target | claim as frozen | source-side need`. Use
`kb/work/literature-disposition/cleanup-cohort-01.md` as the shape. This ordering
is not bureaucracy: reading the source first lets its vocabulary decide what
counts as a claim, which is how an earlier pass over-attributed two claims it
later had to retract.

**The unit is one claim use, not one note.** A note with four load-bearing claims
produces four rows and can end with four different dispositions.

Three failure modes this work has already produced, in order of likelihood:

1. **Charitable over-attribution.** Thematic overlap is not support. If the
   source establishes something narrower than the note asserts, the disposition
   is `narrowed`, not `grounded`. Cohort 01 returned six narrowed and two
   contradicted out of eight uses, and **zero grounded as written** — that is the
   honest prior, not a target.
2. **Grounding from the ingest's analysis prose.** Only the checksum-verified
   snapshot establishes a source claim. Never derive a `Claims` entry from an
   ingest's existing Summary, Connections Found, or Extractable Value.
3. **Fragmenting extracts on wrapped lines.** A `pdftotext` snapshot wraps
   mid-sentence; verbatim matching normalizes whitespace, so quote the whole
   contiguous span with one locator rather than one fragment per line.

**Stay inside your manifest.** Do not ground, edit, or repair any note or ingest
not listed in it — other agents own those concurrently, and the disjointness is
what makes parallel work safe. If a target needs a source outside its listed
ingests, record a `literature handoff` and move on; do not capture it yourself.


Finish by filling the manifest's completion record: one row per claim use, with
disposition, target change, and validation result. The run is done when every row
has a terminal disposition or a named blocker. Commit your own manifest and
target repairs.

Report what you found — including any pressure toward claim IDs, duplicate
entries, or reconciliation. That is design evidence being collected deliberately:
the decision to ship no identity machinery rests on a two-entry run, and these
cohorts are its first real test.
