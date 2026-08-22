# Trial notes — cold run of `analyse-agentic-system` on `sequentialthinking`

**Trial apparatus. Not part of the instruction's logical result.** The result proper is
`RESULT.md` and the files it indexes.

Run: `AGS-20260821-sequentialthinking`. Executed 2026-08-21 against
`/home/zby/llm/servers/src/sequentialthinking` at `2ecb382`.

---

## A. Friction points — steps that were ambiguous, impossible, or forced improvisation

### A1. Step 1.2 — the clarifying sentence is attached to the wrong route for this case (moderate)

Step 1.2 offers two admission routes: (i) the named kinds (runtime, harness, orchestration
framework, agent operating layer), and (ii) "any narrower system whose deployed behavior
depends on model calls plus surrounding machinery."

`sequentialthinking` is clearly not of a named kind, so route (ii) is the only candidate. But
route (ii) says the system's behavior must *depend on model calls* — and this server makes no
model call and declares no `sampling` capability (`ABS-10`). Read tightly, route (ii) is about
systems that *issue* model calls.

The sentence that actually resolves my case is the next one: "A system of a named kind stays
in scope when the model call it serves runs outside its own boundary, including deterministic
machinery driven by a model that lives elsewhere." That is exactly this server. But it is
grammatically scoped to *"A system of a named kind"* — i.e. to route (i), which does not
apply here.

**What I did:** admitted the subject under route (ii), reading "depends on model calls" as
"depends on model calls, whether it issues them or serves them," and taking the
"deterministic machinery driven by a model that lives elsewhere" clause as the intended
sense. **Recommendation:** either widen that clause to cover both routes, or restate route
(ii) as "depends on model calls it issues *or serves*."

### A2. Steps 1.3–1.4 — no vocabulary for "complete artifact, partial loop" (moderate)

Step 1.4 offers a binary: a whole-system boundary, or a subsystem-only boundary that "must be
named as such" and "cannot support whole-system conclusions."

Neither fits. The server is a complete, independently distributed npm package — it is not a
subsystem of some larger inspected thing, and calling it "subsystem-only" would misdescribe
it. But the *behavior anyone cares about* — sequential reasoning — is produced by a loop
spanning host, model, and server, two-thirds of which is external.

**What I did:** improvised a third framing in the packet — "whole-artifact for the
distributed server; not whole-system for the reasoning loop" — and listed the model and host
as named exclusions with prevented conclusions. This worked well and I think it is the right
answer, but the instruction did not supply it. **Recommendation:** the boundary-kind
vocabulary would benefit from a "complete artifact whose material loop crosses declared
external dependencies" case, since this is the common shape for any MCP server, plugin, or
tool.

### A3. Step 3 — the tier can read stronger than the analysis's reach (moderate, but the instruction handles it)

The tier rule says to judge `code-grounded` over the loops the boundary includes, and that a
loop declared an external dependency "neither raises nor lowers the tier." Applied honestly,
this run is `code-grounded`: every included loop rests on inspected implementation.

The awkward consequence is that an analysis of a *thinking* tool is stamped `code-grounded`
while establishing nothing whatever about thinking. The instruction's limitation-pairing rule
catches this correctly, and I recorded it. But a reader who reads only the tier line gets a
stronger impression than the analysis supports. **Not a defect I had to work around** — the
mechanism exists — but the tier's headline placement in logical record 2, next to the
boundary, is doing less work than it appears to.

### A4. Step 2.4 — packet assembly reads as a loop-back (minor)

"Freeze the sources here; finalize the evidence packet after step 4" is unambiguous once you
read the whole paragraph, but it means logical records 3 and 4 cannot be written until after
logical record 5 exists in draft. I ran steps 2.1–2.3 → step 3 rules → step 4 baseline →
wrote the packet → wrote the runtime account file. No real friction; noting the ordering only
because a naive linear reading of step 9's record order would produce the wrong work order.

### A5. Step 5 memory trigger — the "ordinary current-run state" exclusion was the hard call (significant)

The memory/context trigger excludes "ordinary current-run state" from counting as read-back.
`thoughtHistory` is in-process, non-persistent, singleton, and dies with the process. That
looks a lot like current-run state.

The reason I judged it a trigger anyway: "run" for a stdio MCP server is the whole *host
session*, spanning arbitrarily many distinct `tools/call` invocations and potentially several
conversations. Material accumulated in call *n* does return to call *n+1*
(`Object.keys(branches)`, `thoughtHistory.length` at `index.ts:113-114`). Under the
definition's own words — "returns to a later invocation or action" — that is read-back, since
each tool call is a distinct invocation.

**The ambiguity is real:** "current-run state" is not defined against a unit, and for a
long-lived process serving many invocations, "the run" could mean the process or the
invocation. Choosing the invocation makes the lens applicable; choosing the process makes it
arguably inapplicable. Step 5's tie-breaker ("a candidate trigger means `applicable`, not
`uncertain`") pushed me to `applicable`, and that was the right call — the lens's actual
finding (total retention, near-nil return) is the most interesting result in the run and
would have been lost by exiting early. **Recommendation:** define the "current-run" unit, or
state explicitly that a process outliving the invocation makes its store read-back-capable.

### A6. Step 7 — invoking the epistemic instruction by path, from a fresh worker (minor)

Step 3's worker topology prefers fresh workers consuming "only the prepared evidence packet
and the frozen read-only boundary." Step 7 requires invoking a separate instruction file. A
fresh worker executing step 7 must therefore read a file *outside* the evidence packet — the
method document itself. This is obviously intended, but the two rules sit in tension as
written, and under this trial's cold-isolation constraint I had to explicitly authorize that
one extra read in the worker's brief.

### A7. Step 7.3's `implemented`/`implemented` collision is a genuine trap (minor, well-handled)

The instruction flags it explicitly and I passed the warning verbatim into the epistemic
worker's brief. Worth noting that the flag was *necessary* — the two vocabularies are
adjacent enough that a worker holding both schemas would plausibly merge them without the
warning.

### A8. No canonical namespace for a lens finding that is neither a new object nor a correction (significant)

Step 3's canonical-record table has six kinds: `CMP-*`, `OBJ-*`, `RTE-*`, `CLM-*`, `ABS-*`,
`BAP-*`. Step 3 also says "Any new material record returns to the orchestrator for one canonical
ID," and separately provides a correction branch for a record found *wrong*.

Five of the epistemic lens's six proposals fit neither slot. "The rejection message asserts a
type error for `thought: ""`, and that assertion is false" is a material finding — it changes the
warrant of a route's output — but it is not a new component, object, route, claim, absence, or
authority path, and it does not make any registered record wrong. Same for the render/state
divergence, the `totalThoughts` lineage break, the process-scope warrant limit, and the version
divergence.

**What I did:** routed all five to *amendments* on the registered records they attach to (A1–A5
in `reconciliation.md` §8.2), each with a superseded value and an evidence anchor, so they remain
citable through the record they annotate. This worked, but I chose it — the instruction does not
say where such findings go. **Recommendation:** either state that findings-about-records are
registered as amendments to those records, or add a finding namespace. Silently, this is the
single most common shape of lens return in this run: 5 of 10 proposals.

### A9. The wrong/incomplete binary in step 3's correction branch is too coarse (moderate)

Step 3: "A lens that finds a registered record *wrong* — not merely incomplete — returns the
correction with its evidence anchor instead of re-inventorying."

Both of the errors a lens caught in my own records sit between those poles. My packet §4d put
`CLM-5` wholly in the voice-ambiguous set when its README anchor sits in the same Features list I
had already classified as system voice — a misclassification by my own stated criterion, but the
record was not *false*, just wrongly sorted. My runtime account said a rejected call "is not
appended… state and history stay clean" without scoping it to validation throws, which is true as
far as it goes and misleading past that point.

Under a strict reading of "wrong, not merely incomplete", neither triggers the correction branch —
and both needed correcting. The epistemic lens handled this well by referring `CLM-5` to me
explicitly rather than deciding it, but that was the worker exercising judgement the instruction
did not supply. **Recommendation:** widen the branch to cover a record that is misleading as
scoped, not only one that is false.

### A10. Step 7.3's "no parallel ID namespace" vs the epistemic method's own schemas (minor)

The epistemic method's output-2 and output-4 schemas require object IDs, and its ledger requires
route IDs. Step 7.3 forbids a parallel ID namespace. The worker resolved this by citing canonical
IDs directly and, where the method's split rule required separating a heterogeneous registered
object, using dotted sub-anchors — `OBJ-3.thought`, `OBJ-6.derived`, `RTE-4 (a)/(b)/(c)`. That is
the right answer and it extends rather than parallels the namespace, but again the instruction did
not authorize it; a worker without that instinct would either mint `O1`/`R1` IDs (violating 7.3)
or fail to split (violating the method's own rule).

### A11. The runtime baseline under-split containers from their derived views (moderate, self-inflicted)

Both lenses independently needed a split I had not made: `OBJ-4` bundles an array of records whose
content has **no consumer at all** with a cardinality projection whose consumer is the model. Same
for `OBJ-5` and its key set. The memory lens proposed the split from the read-back definition; the
epistemic lens hit it from the warrant-domain side. I registered `OBJ-11` and `OBJ-12` at
reconciliation.

Step 6.1 tells the *memory lens* to split bundled artifacts on differing consumer or authority
path. Step 4.2 gives the runtime baseline no equivalent instruction. Since the runtime baseline
owns generic identity and mints the IDs the lenses must extend, the split rule arguably belongs
there too — otherwise every lens has to propose the same split independently, which is exactly
what happened.

### A12. What worked, recorded because trials should register successes too

- **The frozen packet plus fresh workers plus lens-local proposal tags did their job.** The two
  lenses reached the same core facts by different routes — degenerate read-back, branch labels as
  the one returning accumulated text, retention-without-retrieval — without seeing each other's
  work. `MEM-1` and `EPI-1` name entirely different things; had workers minted canonical IDs, those
  two would have collided on `1`, which is precisely the failure step 3 predicts.
- **`CLM-*` being orchestrator-owned paid off concretely.** The epistemic lens proposed `EPI-6`
  from the tool-string anchors it had; registering it centrally as `CLM-11` let me attach the
  README system-voice anchor (`SRC-2:11`) the worker's brief had not surfaced, which turns a
  second-person claim into an unambiguous one and strengthens the mismatch.
- **The `implemented`/`implemented` warning in step 7.3 was load-bearing.** Passed verbatim into
  the worker brief, it produced an explicit vocabulary-separation section at the top of the lens
  file. I do not think it would have happened unprompted.
- **Step 8.1's "never resolve a conflict by selecting the strongest-sounding status"** was tested
  by the voice ambiguity (C1). The tempting resolution — read the claims as predicating of the
  model, so nothing is a mismatch — is exactly the strongest-sounding-status move, and the rule
  blocked it.

---

## B. Lens-applicability reasoning (as required by the trial brief)

Both dispositions and their full rationales are recorded in `lens-dispositions.md`, which is
the result-proper record. Summarizing the reasoning path here:

**Memory/context — `applicable`.** Decided on the `index.ts:113-114` read sites. Two values
derived from accumulated state (`Object.keys(branches)`, `thoughtHistory.length`) are
returned to the host on every call, so material accumulated through use reaches a later
invocation. See A5 for the one genuinely contestable step. The static tool descriptor was
correctly *not* used as a trigger — the definition excludes shipped tool specifications by
name.

**Epistemic — `applicable`.** Overdetermined; either half of the trigger fires alone. (a) The
`thought` field carries unconstrained natural language documented as including "Hypothesis
generation" and "Hypothesis verification" — truth-apt. (b) The README claims, in the system's
own voice, that the server's features include "Generate and verify solution hypotheses"
(`CLM-4`), and the tool description claims verification and a correct answer
(`CLM-2`, `CLM-3`) — consequential warrant claims. The direct-adaptation exception was
checked and does not apply, since both a truth-apt object and warrant claims are present.
Step 5's "even when the eventual finding is failure or absence" clause was decisive in not
treating the likely absence-shaped result as a reason to exit.

**Neither disposition was reached by expecting a particular finding.** In both cases the
trigger fired on inspected evidence and the finding came afterward.

---

## C. Things I could not do

1. **No `observed` or `causally supported` status anywhere in the run.** `ABS-8`: the boundary
   contains four files and no test, fixture, trace, or log. Running the server to produce an
   observed trace would have required installing dependencies into the checkout, which the
   trial brief forbids (do not mutate the checkout) and which step 2 forbids anyway (no
   source widening). Every finding in this run is capped at `implemented` or `claimed`.
2. **`SRC-6` (`@modelcontextprotocol/sdk` 0.5.0) was never inspected** — `node_modules/` is
   absent from the checkout and fetching it was not permitted. Recorded as an access gap with
   its prevented conclusions, not as an absence.
3. **No publication.** The trial brief states no authorized target exists; I applied step
   9's publication rule, retained the result under the staging identity, and recorded the
   blocker in `RESULT.md` §11.
4. **No deterministic validation.** Step 10.3's explicit branch applies: no authorized target
   contract, therefore no deterministic validation. I recorded `no deterministic validation
   applicable` plus the semantic checklist result, and did not adopt an unrelated contract to
   manufacture a validation path.

---

## D. Notes on physical layout (step 9 leaves this under trial)

I chose a **package of seven files** with `RESULT.md` as the canonical index naming one
canonical location per logical record. Observations for the layout question:

- The split paid off for the **worker handoff**: `evidence-packet.md` (records 1–4) is
  exactly the artifact step 3's worker topology describes, and being able to hand a worker
  one file path rather than a reconstructed briefing made the frozen-packet rule cheap to
  enforce. A single-file layout would have forced me to either paste the packet into each
  worker brief or give workers the whole result-in-progress, and the second option leaks one
  lens's findings into the other.
- The cost is that record 2 (boundary/revision/tier) is duplicated in summary form in
  `RESULT.md`. Step 9 permits a pointer; I used a pointer plus a short restatement, which
  risks drift if the two are ever edited independently.
- `ABS-*` and `BAP-*` living in the packet rather than in a lens file was right: both lenses
  referenced them and neither owned them.
- **The layout needs somewhere for amendments to live, and `reconciliation.md` became it.**
  Logical record 4 (shared canonical records) ended up split across two files: the packet's
  originals and the reconciliation's registrations and amendments. `RESULT.md` §0 handles this by
  naming both as the canonical location for record 4, which step 9 permits. But a reader now has
  to consult two places to get the current state of, say, `BAP-4`. A single-file layout would
  have let me edit the record in place; the package forced an append-only amendment log. That is
  arguably better for audit — the superseded value survives — and worse for reading. Worth an
  explicit decision rather than falling out of the layout.
- Seven files was about right for a system this small. A larger target would likely want the
  runtime account split by loop, and the amendment log would grow enough to want its own file.
