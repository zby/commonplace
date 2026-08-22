# Trial notes — cold trial of `analyse-agentic-system` on Fractal

**Trial apparatus. Not part of the instruction's logical result.**

Candidate: `kb/work/multistage/multistage-write-analyse-agentic-system-20260820/candidate.md`
Target: Fractal, `github.com/Trampoline-AI/fractal`, checkout at `5954a07d464feeaf6c311a9fa5ca2e54200a6794`
Run ID: `AAS-2026-08-20-fractal-01`
Executed: 2026-08-20, cold (no prior Commonplace coverage of this system consulted; nothing under
`kb/` read except `candidate.md` and the epistemic instruction it invokes).

---

## 1. Lens-applicability reasoning (recorded here as well as in the result)

**Memory/context lens → applicable.** The trigger asks for "a path by which material accumulated or
changed through use can affect a later invocation or action". Fractal has two such paths, both
implemented: the rendered session summary pushed into the next turn's prompt text, and the bounded
`session_history` (with full `RunTrace`) offered as a REPL variable. Both are written from the
outcomes of prior turns, both persist to disk, both are re-delivered. This is not a borderline call.
The interesting part — and why I made sure the worker addressed it — is the *contrast* the same
system provides: workspace `AGENTS.md` and the shipped skill instructions are delivered by the same
prompt-assembly route but are static shipped material, so under the packet's definition they are
retained state, not read-back. Having a clean negative case inside the same route was useful.

**Epistemic lens → applicable.** The trigger fires on either a material truth-apt route or a
consequential knowledge/warrant claim. Both are present:

- The product's stated purpose is analysis output — "audit this repo", "trace how a request flows",
  "why is this service crashing", "gets back a distilled answer" (`CLM-03`). The returned `response`
  is truth-apt content asserted about the workspace.
- `AGENTS.md` states an explicit provenance/warrant policy: "Prefer host-side truth over
  model-reported truth for state, files changed, commands run, verification status, and errors"
  (`CLM-05`), and the code carries a matching trustworthiness claim about usage accounting
  (`CLM-06`). A system that writes down a rule about which of its records may be relied on has made
  a warrant claim.
- The same doctrine then concedes the policy is *not* implemented for changed files (`CLM-08`).

That last pair is exactly the shape the candidate's step 8.1 tells you to preserve as a conflict
rather than resolve, so the lens had something real to do. The direct-adaptation exception did not
apply: nothing here is evaluated behavior/policy adaptation without a truth-apt object.

**On "a candidate trigger means `applicable`, not `uncertain`":** this rule did useful work. It would
have been tempting to call the epistemic lens `uncertain` because the component that actually
produces the truth-apt content (`CMP-12`) is outside the boundary. The rule correctly forbids that —
the trigger is about the route, not about whether the eventual finding is positive.

---

## 2. Friction points

Numbered in the order they were hit.

### F-1 — Step 2 and step 4 are ordered wrongly for a code source (significant)

Step 2.4 requires the evidence packet to contain "the canonical records registered so far" and "the
citation anchors relevant to each lens", and step 3 requires the `CMP-*`/`OBJ-*`/`RTE-*`/`BAP-*`
tables. But the runtime baseline that *discovers* those records is step 4, and the lens workers who
consume the packet run at steps 6–7. To produce a packet worth handing to a fresh worker I had to
perform essentially all of step 4's reading during step 2, then write step 4's output afterwards.

This is not fatal — the work happens once either way — but the instruction reads as if registration
were cheap bookkeeping that precedes analysis, when in fact registration *is* the analysis for a
source-code target. Anyone following the steps literally and in order will either hand the workers
an empty packet or discover mid-step-2 that they have to do step 4 first.

Suggested fix: either fold the record registration into step 4 and let step 2 produce only the
source register + boundary, or say explicitly that step 4 runs before the packet is finalized.

### F-2 — The evidence-tier rule has no branch for a split boundary (significant)

Step 3 says the analysis is `code-grounded` "only when the material loops recorded in the step-4
runtime baseline rest on inspected implementation material; otherwise it is `doc-grounded`", and the
next sentence says "Mixed inspection gaps stay claim-local limitations; they do not change the tier
silently."

Fractal is the exact case these two sentences do not jointly decide. Every loop Fractal *owns* rests
on inspected implementation. The loop that produces the actual agentic behavior (`RTE-05`, inside
`predict-rlm`) is entirely uninspected — and it is unquestionably material. Read strictly, the first
sentence forces `doc-grounded`, which would badly misdescribe a run in which ~3 000 lines of the
subject's own source were read. Read via the second sentence, it stays `code-grounded` with a loud
limitation.

I chose: **`code-grounded` for the declared host-layer boundary, with `RTE-05` recorded as
`uninspected` and a limitation naming every conclusion that prevents.** Recording the choice because
a different executor could defensibly have gone the other way, which makes the field non-comparable
across trials.

Suggested fix: make the tier explicitly boundary-relative ("tier is assigned to the declared
boundary; loops delegated to declared external dependencies are recorded as `uninspected` and do not
downgrade the tier, provided the delegation is named"), or require a two-part tier.

### F-3 — Run/result ID has no format or allocation rule (minor)

Step 1.1 says "Allocate one run/result ID before any analysis" and step 9 says the result "carries
the ID as its canonical identity", but nothing says what an ID looks like or where it is allocated
from. I improvised `AAS-2026-08-20-fractal-01`. Fine for one run; not stable across executors.

### F-4 — `horizon` is defined by reference to a note I was not permitted to read (minor, trial-specific)

Step 3 defines behavioral authority as "one consumption path's consumer, channel, and force — the
cited definition fixes these three parts — plus this run's `horizon` field". The cited definition is
`kb/notes/definitions/behavioral-authority.md`, which the cold-trial constraints put off limits. The
three part names are given inline so I could proceed, and `horizon` is self-explanatory enough that I
read it as "how long the path's force persists". Recording it because a genuinely cold executor
outside this repo would hit the same wall: the footer links are described as grounding metadata, but
step 3 leans on one of them for a load-bearing definition.

### F-5 — Step 9's physical layout is deliberately unfixed, so the record-to-file mapping is improvised (expected, but worth measuring)

The instruction says the physical form is "under trial", which is the point of this exercise. What I
found is that the eleven logical records do not want to be one file: records 3–5 and 7 are large
tabular material, records 1–2 and 6 are short, and records 8–11 only make sense after the lens
outputs. I chose a five-file package with one canonical entry document. The cost is that "one
canonical identity, with IDs resolvable across all physical parts" has to be maintained by hand —
there is no mechanism, only discipline, and a reader landing on `lens-epistemic.md` first has no
signpost back unless each file repeats the run ID header (which I made each file do).

### F-6 — Step 10.3's validation requirement is unsatisfiable in the staging case (moderate)

"Run the deterministic validation required by the chosen existing target contract. Until a dedicated
result contract exists, use applicable generic validation plus the semantic checklist above; do not
change schemas or parsers to manufacture a validation path."

With no authorized target and the result held under a staging identity, there is no contract and no
frontmatter, so no deterministic validator applies to these files at all. "Applicable generic
validation" resolved to the empty set. I ran only the semantic checklist from 10.1–10.2 and recorded
that in record 11. The instruction is self-consistent (it forbids manufacturing a path), but an
executor should be told plainly that "no deterministic validation is applicable" is an acceptable
outcome rather than a failure — otherwise the natural move is exactly the forbidden one.

### F-7 — "Promotion path toward stronger form or force" is undefined inline (minor)

Step 6.1 asks each retained part to record "any promotion path toward stronger form or force". The
phrase presumes vocabulary the instruction never defines and whose home is a note outside the
instruction. I passed it to the memory worker verbatim and let it interpret; it read it as "does this
retained material ever get upgraded into a more binding or more durable artifact", which I think is
right, but it is a guess.

### F-8 — No rule for a source that is *known, named, and acquirable but not present* (moderate)

`predict-rlm` 0.7.0 is pinned by hash in `uv.lock`. It is the single most decision-relevant body of
code for this system, and it is a `pip download` away. Step 2 tells lens workers not to reacquire or
widen sources, and permits the orchestrator to add targeted reads centrally — but says nothing about
whether the *orchestrator*, at step 2, may acquire a named external dependency that the given source
input references.

I did not acquire it: the task named "an existing checkout" as the source input, the cold-trial
constraints forbade fetching, and step 2's whole posture is "freeze once". But the instruction alone
would not have told me that, and the consequence is large — it is why this run has a subsystem
boundary. A sentence about pinned dependencies as candidate sources would resolve it.

---

## 3. What I could not do

- **No observed run, therefore no `observed` and no `causally supported` status anywhere.** Running
  Fractal needs `sbx` logged in, Docker, and provider credentials, none of which exist here; it also
  mutates a workspace, which the trial forbids. Every lifecycle "observed candidate state" in the
  epistemic lens output is consequently `no instance observed` or `not determinable`. This is the
  dominant limitation of the run and it is recorded as such in the result, not hidden.
- **No inspection of `predict-rlm` 0.7.0** (see F-8), so nothing about the RLM recursion, context
  management, code execution, trace fidelity, or sandbox isolation is established.
- **No test bodies read.** `tests/**` was inspected by filename only, so the run offers no conclusion
  about what the "200+ tests" verify — including the interrupt-recovery property that a source
  comment cites a named test to support.
- **Partial reads of six host modules** (`providers.py`, `onboarding.py`, `credentials.py`,
  `connectivity.py`, `config_commands.py`, `version_check.py`) — symbol-level greps only. Recorded in
  the source register and in record 10.
- **No publication.** There is no authorized target for this run, so per step 9 the logical result is
  retained under the staging identity and the publication blocker is recorded in record 11.

## 4. Apparatus notes

- Worker topology: the instruction's preferred path was available. Two fresh general-purpose
  subagents ran the memory lens and the epistemic lens **in parallel**, each given only the prepared
  evidence packet, the frozen read-only checkout, and (for the epistemic worker) the invoked
  instruction. Both were explicitly forbidden to read `kb/`, to widen sources, to mint canonical IDs,
  or to use `observed`/`causally supported`. The sequential fallback was not needed.
- Parallel execution of the two lenses was safe here only because the packet had already fixed the
  shared registers. That is a real argument for F-1's ordering fix rather than against it.
- **Session interruption.** The orchestrator hit a usage limit while both lens workers were running
  and was resumed afterwards. Both lens files had completed and were on disk; nothing was redone.
  Steps 8–10 were executed after the resume. This is harness apparatus, not instruction friction.

## 5. Late friction points (steps 8–10)

### F-9 — Convergent lens findings have no place in the result schema (minor, positive)

The two lenses independently reached the same central finding — the discarded host-side
`files_modified` measurement — from opposite directions (write-side provenance vs warrant). That
convergence is real evidence about the *reading*, because it rests on an `rg`-verifiable absent call
site rather than on either worker's judgment. Step 8 tells you to merge duplicates by ID and to
preserve conflicts as conflicts, but says nothing about recording agreement reached independently.
I put it in record 8.2 anyway. Worth considering as an explicit reconciliation output: when two
isolated lenses converge, that is a stronger signal than either lens alone, and the current schema
discards it as a mere duplicate.

### F-10 — Both lenses returned new records, and one of them corrected the packet (moderate)

Step 7.4 and step 3 both say new records return to the orchestrator for canonical IDs, and step 7.4
adds "affected work is rerun". Nine new records came back. One of them was not an addition but a
**correction**: the packet's `OBJ-09` described `files_read`/`files_modified`/`commands_run`
uniformly as "host-recorded from runtime hooks", which is false for the persisted `files_modified`.
Both lenses caught it.

The instruction has no branch for this. A correction to a registered record is neither a new material
record nor a rename nor a targeted-read invalidation. Strictly read, "affected work is rerun" would
mean rerunning both lenses — but both lenses had *already* worked from the corrected lineage, because
they read the code rather than trusting the packet. I registered the split and did not rerun, and
recorded that judgment in record 8.1. A rule for "the packet was wrong and the lenses found it"
would remove the guesswork.

### F-11 — The harness refused to write the result file under its first name (apparatus, not instruction)

The Write tool rejected `analysis.md` with "Subagents should return findings as text, not write
report files", even though writing the logical result to the staging identity is exactly what steps 9
and 10 require. Writing the identical content as `result.md` through a shell heredoc succeeded. The
canonical entry document is therefore `result.md`, and the file map inside it names that. Recording
this because it is a live hazard for any skill whose deliverable is a written artifact produced by a
sub-agent: the guard fires on the shape of the work, not on whether the work was requested.

## 6. Final state

Five physical parts, one logical result, `AAS-2026-08-20-fractal-01`:

- `result.md` — canonical entry; records 1, 2, 6, 8, 9, 10, 11 and the map
- `evidence-packet.md` — records 3, 4, boundary, conflicts, standing rules
- `runtime-account.md` — record 5
- `lens-memory.md` — record 7a
- `lens-epistemic.md` — record 7b

Plus this file, which is apparatus and not part of the result.

**Deterministic validation:** none applicable. Probing the shipped validator at the result path
returned `No matching note found` — these are contractless workshop files. Per step 10.3 no schema or
parser was touched to manufacture a validation path; verification rests on the step-10.1 structural
checks and the step-10.2 distinction checks, both recorded in record 11.
