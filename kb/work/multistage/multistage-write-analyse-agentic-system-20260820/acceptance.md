Verdict: PROMOTE WITH NAMED CHANGES

Twelve required changes, enumerated in §5. All twelve are text-local: they add roughly ten lines, remove three, and reopen no design decision. None of them contradicts anything the six trials validated. If the maintainer applies them, the candidate may be promoted to `kb/instructions/analyse-agentic-system/SKILL.md` without a further trial; the two structural suggestions in §4E are follow-up work with their own trial, not conditions of this promotion.

Reviewed 2026-08-21 against `candidate.md` (199 lines, 4,451 words), `brief.md`, the six `trials/*/trial-notes.md` files, `kb/instructions/COLLECTION.md`, `kb/types/instruction.md`, `kb/instructions/analyse-external-system-epistemic-architecture.md`, then `trial-evaluation.md`, `README.md`, and targeted reads of `audit.md`.

**On the brief's own acceptance criterion.** `brief.md` says the instruction "passes only after cold trials cover at least: runtime only; runtime plus memory with no material epistemic transformation; runtime plus epistemic routes; and runtime plus both." That criterion is void rather than unmet: the user's 2026-08-21 decision removed the applicability gate, so the four combinations no longer name distinguishable execution paths. The substitute evidence — the re-run producing *differentiated* depth (brief memory, full epistemic) on one subject — is the right evidence for the rule that replaced it, and it is adequate. I record this so the gap between `brief.md` and the promoted artifact is on the record rather than looking like an unmet condition someone quietly dropped.

---

## 1. Phase-1 self-sufficiency findings

Formed from the candidate, the brief, the six trial notes, and the two contracts, before any evaluation prose was read.

### 1.1 Deterministic contract state

`commonplace-validate candidate.md` → schema PASS, **10 link-health warnings**, 0 fails. Title imperative, `description` trigger-shaped, `type` correct, `name` matching the target directory. Frontmatter is missing `allowed-tools`, `context`, `model` — the three fields `kb/instructions/COLLECTION.md` §Frontmatter names as what promoted skills add.

The candidate is the longest instruction in the collection: 4,451 words against 3,476 for `cp-skill-write-multistage` and 2,932 for the epistemic instruction it invokes. A full run loads ~7,400 words of instruction text before it reads a single source file.

### 1.2 What the revision passes genuinely fixed

Verified in the text, not taken on the author's word: `behavioral-authority` fully inlined with an example tuple and "apply them without opening any other document" (line 69); boundary-relative tier (50); the third boundary kind (30); `issues **or serves**` (25); the `ABS-*` register (86); amendments (90); the widened correction branch (88); proposal tags (84); worker-artifact-authoritative (96). Each closes a friction point a named trial hit. That is a real improvement record and I am not reopening any of it.

### 1.3 Where the candidate is not self-sufficient

A cold executor with this file and the sources hits these:

1. **Step 7.1's link does not resolve** — the single mandatory external read in the procedure. See §5.1.
2. **Undefined terms inside mandatory record fields.** Step 6.1 requires each retained part to record "representational form" and "any promotion path toward stronger form or force"; neither *representational form* nor the form/force ladder is defined anywhere in the candidate. Step 3's ownership table requires "generic identity, form, substrate"; *generic identity* is undefined. `COLLECTION.md` frontloading: "Define terms inline; don't assume the reader has loaded other KB documents." Raised as fractal F7 and re-run F6; unfixed.
3. **No run/result ID format** (step 1.1, made canonical by step 9, verified by step 10.1). Six trials minted six mutually incomparable identifiers.
4. **Three sentences that are diffs against a draft the reader never saw.** Line 113 "The branch is removed rather than relaxed for exactly this reason"; line 120 "This no longer decides whether the lens runs"; line 151 "which remains under trial". The last also imports workshop lifecycle state into a promoted artifact.
5. **Step 4.2 has no loop-individuation rule and no heterogeneous-split rule.** cc-dynamic F5 and gbrain F5 both improvised loop grain; seqthink A11 shows both lenses independently proposing the same container split because the runtime baseline — which owns generic identity and mints the IDs the lenses must extend — was never given the split rule that step 6.1 gives the memory lens.
6. **Step 7.4 over-specifies returns relative to the invoked procedure's early branches.** See §1.4.
7. **No rule for acquiring a named, pinned, absent dependency** (fractal F8) — the decision that set fractal's boundary kind.
8. **No rule for a negative live capture, or for a second source dated far outside the run cutoff** (cc-dynamic F1, F2).
9. **Mid-flight capacity failure** (gbrain F15): line 96 covers a worker that dies *after* writing output. GBrain's workers completed, returned, and were killed before anything reached disk; under a strict reading of the three-valued topology rule the correct action was to discard a completed analysis.
10. **Independent convergence has nowhere to go.** fractal F9, cc-dynamic, gbrain F14 and the re-run §4 each report that two isolated lenses reaching one fact from opposite directions was the most informative product of their reconciliation, and that step 8 tells them only to merge duplicates and preserve conflicts. Three orchestrators recorded it off-schema anyway.

### 1.4 Verification of the candidate's claims about the invoked procedure

All three claims the review brief asked me to test hold.

- **Architectural status vocabulary**: `implemented` / `observed, implementation uninspected` / `doctrine only` / `no route found within boundary` / `not determinable` (epistemic instruction lines 78–82). `implemented` does contrast with `doctrine only`, as candidate line 60 says.
- **Class for non-truth-apt updates**: `non-truth-apt policy/content update: <description>` (line 89), and its step 4 both instructs classification of every content-changing edge and carries an explicit clause for behavior/policy adaptation with no truth-apt object (line 168). The candidate's classify-only seam is accurate about its target.
- **Step 7.2's pass-list is sufficient to start it — but only just.** The invoked procedure's prerequisites list six items. 7.2 names direct analogues of four; it carries "the system's knowledge-production or warrant claims" only implicitly inside "the existing canonical records" (`CLM-*`), and "known evidence gaps" only inside the source register's `access gaps` field. Recoverable by a careful orchestrator, not stated. Naming `CLM-*` and the access gaps explicitly in 7.2 would cost four words; I do not make it blocking.
- **Step 7.4's demands are producible — on the main path.** Output 3 carries route function, architectural status, content/update relation and all three authorities; output 4 carries observed candidate state and the acceptance/retention/integration separation; output 1 carries missing-evidence→conclusion pairs. The exception is the early branches: the procedure's step-3 branches both end "Then stop" and legitimately emit the global no-candidate statement and an explicit no-claim comparison *instead of* output 4's states and a full ledger. Step 7.4 reads as a flat checklist. A cold orchestrator checking a correct branch-1 return against it will judge complete work incomplete and rerun a worker that did the right thing. See §5.6.

Also confirmed, and outside this instruction's power to fix: the invoked procedure's Branch 2 "Then stop" would literally discard implemented routes its own material-route rule already admitted (re-run F11). The workshop README already carries this as a pending upstream handoff with the correct diagnosis. Nothing further needed here.

### 1.5 Where the author's reasoning is needed to see why a rule is right

Two places, and by the brief's own test these are findings about the instruction, not about my inputs.

- **Line 122's "Hand the route to the invoked epistemic procedure anyway"** contradicts the sentence two lines above ("stays in the runtime account, and the scoping record names it for the orchestrator") unless the reader knows the second paragraph was added later to repair a wrapper/method conflict. As two adjacent paragraphs they read as a reversal, not a refinement.
- **Lines 113 and 120** are only intelligible as diffs against the removed applicability gate.

`trial-evaluation.md` confirms both: the removed-branch reason at line 113 was added deliberately, and the classify-only paragraph is the F1 repair. That the author's rationale is *correct* does not make the placement correct — a promoted instruction cannot carry its own changelog as load-bearing prose.

### 1.6 Testing the evaluation's rationale against phase 1

Read afterwards, its three post-trial rationales survive contact with my independent judgment. The rename argument ("a warning is the weakest instrument against a silent failure") matches what I found mechanically in §4A(i). The classify-only argument ("withholding leaves a silent hole in the invoked procedure's ledger") is verifiable directly against epistemic-instruction lines 89 and 168, and I verified it there before reading the rationale. The reading-order argument is self-evident from the text.

One evaluation-adjacent claim does **not** survive: `README.md` line 18 says the audit "verified all footer links". `audit.md` finding 6.2 shows what was actually verified — that the paths are workspace-root form and target no forbidden collection — and it explicitly notes "these would not resolve as plain relative links" before resolving to *keep*. The README's summary overstates it, and the deferred consequence is §5.1.

---

## 2. Disposition A — untrialled text

### A(i) `implemented` → `afforded`: **fix before promotion** (keep the rename; add the guard)

The rename is **complete and consistent**. `grep -i "implement|afford"` over the whole candidate returns nine hits; every one is correct. `afforded` is the conclusion status (57, 116); `implemented` appears only as the invoked procedure's architectural status under its own name (60, 139); the remaining hits use "implementation" as an ordinary noun (41, 50, 51, 62, 178). Nothing still depends on the old term, and line 60's claim that the two sets "share no value" is now true where before the rename it was exactly false. I checked the full cross-product against the epistemic instruction's architectural statuses and observed candidate states: no exact collision remains (`uninspected` vs "observed, implementation uninspected" share a word, not a value).

I do not accept the evaluation's framing that moving it "is free". It is nearly free, with one residue: `afforded` is a word no trial output used, no worker has ever been asked to write, and whose natural-language pull is toward the wrong term — six trial artifacts say `implemented` throughout. The re-run named this collision "the one rule whose violation would be silent, invisible in the output, and fatal to the result's meaning". A rename removes the collision from the *text* but leaves the drift unguarded in the *output*, because step 10.1 verifies "source anchors and statuses" without enumerating them.

**Exact change:** in step 10.1, replace "source anchors and statuses" with "source anchors; every conclusion status is one of the seven values listed in step 3, and no record carries `implemented` as a conclusion status". Cost: one clause. It converts the instruction's most consequential silent-failure mode into a checkable item.

### A(ii) The classify-only seam: **reject** (not a real problem)

The substance is sound and I verified it independently of the author's account. The invoked procedure carries `non-truth-apt policy/content update` (line 89) and instructs classification of every content-changing edge with a named clause for adaptation lacking a truth-apt object (line 168), so "withholding one would leave a silent hole in its ledger" is a true statement about that document. Step 7.2's pass-list carries the classify-only routes, and step 7.4's "transformation class and route function" is satisfiable for such a route (`behavior/policy adaptation` + `non-truth-apt policy/content update`). The re-run's worker executed precisely this resolution successfully and reported it worked (F1). It is untrialled as *text* but field-tested as *behaviour*, which is the weaker but relevant evidence.

The only defect here is presentational adjacency — the "anyway" reading — which §5.12 fixes as part of removing the revision-history sentences.

### A(iii) Step 9's "reading order, not the writing order": **reject** (not a real problem)

Purely clarifying, cannot mislead, and it addresses an ordering confusion four independent trials reported (fractal F1, gbrain F7, seqthink A4, re-run F2). The one gap is that it explains only the record 2 / record 5 inversion and not the record 4 / record 5 inversion gbrain hit; that is a half-sentence a maintainer may add and I do not require it.

---

## 3. Disposition B — the seven items recorded for acceptance

Where an item is dispositioned "known limit", the durable home is a design proposal under `kb/reference/proposals/` (per its README contract), **not** this workshop — workshops are consumed and deleted, so a limit recorded only here evaporates at close. One proposal covering the residual gaps in this instruction is sufficient; it should also carry the §1.3 items 5, 7, 8, 9 and §1.3 item 10.

| Item | Disposition |
|---|---|
| **F3** — worker topology vs the step-7 method document | **fix before promotion** (§5.7) |
| **F4** — nothing bounds `ABS-*` inflation | **fix before promotion** (§5.8) |
| **F5** — crossing-loop fields under `complete artifact, partial loop` | **fix before promotion** (§5.9) |
| **F6** — "generic identity, form, substrate" undefined | **fix before promotion** (§5.3) |
| **F9** — run/result ID has no format | **fix before promotion** (§5.4) |
| **F12** — 7.1 "do not restate" vs 7.4's enumeration | **record as known limit** |
| **F14** — packet immutable or amendable | **fix before promotion** (§5.10) |

**F12 rationale for the softer call.** This is a fuzziness, not a contradiction: 7.4 specifies the interface, 7.1 forbids duplicating the method, and the two are formally compatible. The re-run resolved it by erring toward including 7.4 in the worker brief, which is the *safe* error — the worker cannot otherwise know what the orchestrator will check. A rule that pushed the other way would be worse. Record it in the proposal, together with the observation that the safe default should eventually be stated. Note that §5.6 fixes a *different* problem in 7.4 (the early-branch hole), which is a correctness defect rather than fuzziness; do not conflate them.

---

## 4. Disposition C — the two claim-level items

### C(i) Memory exclusion per kind vs per instance: **fix before promotion**

Both trials are right about their own case, and they are not in conflict once the test is stated per instance rather than per artifact kind.

Swamp's evidence is genuine and I am not weakening it: swamp's ~1.1 MB bundled skill corpus is written *by the distribution*, never rewritten by swamp from anything swamp accumulated, so it is retained state under any formulation. GBrain's SkillOpt case is different in kind: the system itself rewrites SKILL.md bodies using measured scores from prior runs, and the rewritten file is then loaded into a later session's prompt. That is material accumulated through use returning to a later invocation — the definition's own words — arriving inside an artifact whose *kind* the exclusion list names. GBrain's executor invented the split (mutated instance = read-back, as-shipped instance = retained static) and it worked.

The per-kind list creates a false negative in exactly the class of system this skill exists to analyse: self-optimizing agent systems. A false negative here is worse than swamp's false positive, because the brief-output floor catches an over-scoped lens (it produces a short "retention total, retrieval nil" finding) but nothing catches a lens that never looked.

**Exact change:** in line 66, after "Static shipped material (documentation, tool specifications, installed skills) and ordinary current-run state are retained state, not read-back", insert: "The exclusion is per instance, not per kind: where the system itself rewrites such material using material accumulated through use, the rewritten instance is read-back and the as-shipped instance remains retained state; keep the two apart." This preserves the swamp case verbatim — nothing in swamp rewrites the corpus — and admits gbrain's.

### C(ii) Sampling/stopping rule for a very large subject: **reject the rule, fix the disclosure**

**Reject** the sampling or stopping rule. No trial produced evidence for a principled threshold, and an invented one would be an authoring-time snapshot of exactly the kind `kb/types/instruction.md` warns against ("Leave anything the executor can determine from the live system to the executor"). The instruction already carries the correct targeting mechanism: read what the *material loops* need, and mark the rest `uninspected`, which is what gbrain did. A file-count rule would be worse than the judgment it replaced.

**Fix** the real harm, which is not the sampling but the silence about it. GBrain's `code-grounded` tier rests on a self-selected sample and the tier line does not say so; seqthink A3 independently observed that "a reader who reads only the tier line gets a stronger impression than the analysis supports". **Exact change:** append to step 3's tier bullet: "When the boundary's material loops were established from a selected subset of a large source, the tier line names the selection basis and the uninspected remainder." One clause, and it makes the tier field comparable across executors, which is the property gbrain F12 actually put at risk.

---

## 5. Required changes, ordered by consequence

Each names the anchor text and the fix.

**5.1 — All ten markdown links are unresolvable from the promotion path.** Anchor: step 7.1 `Invoke [Analyse an external system's epistemic architecture](kb/instructions/analyse-external-system-epistemic-architecture.md)` and the nine footer entries `(kb/notes/...)`. The validator resolves link targets against the source file's parent (`src/commonplace/lib/validation.py:370-378`), so from `kb/instructions/analyse-agentic-system/SKILL.md` these resolve to `kb/instructions/analyse-agentic-system/kb/...` and miss — 10 warnings today and 10 after promotion. `audit.md` 6.2 considered this and resolved "keep", citing COLLECTION.md's promoted-skill rule; that rule is real but its two examples (`kb/notes/`, `kb/instructions/COLLECTION.md`) are bare paths in prose, not markdown links, and **no promoted skill in the collection uses root-style markdown links** — `cp-skill-write` uses relative links and `write-agent-memory-system-review` mixes relative links with bare code-span workspace paths; both validate clean. The step-7.1 case is not cosmetic: it is the one file the executor is required to open.

*Fix:* step 7.1 — drop the markdown link and name the path in a code span: "Invoke the procedure in `kb/instructions/analyse-external-system-epistemic-architecture.md` to run the accepted route-analysis method inside this run's boundary." A bare workspace-root path resolves for the executor from the repo root in both the `kb/` copy and the compiled/symlinked skill copy, which is exactly what COLLECTION.md's promoted-skill rule is protecting. Footer — convert the nine `rests-on` entries to file-relative form (`../../notes/...`, `../../notes/definitions/behavioral-authority.md`), matching `cp-skill-write`; these serve meta-readers, whom COLLECTION.md directs to `kb/instructions/` as "the searchable source surface". Result: 0 link warnings, and the load-bearing pointer survives compilation.

**5.2 — Frontmatter: `allowed-tools`, `context`, `model`.** See §6 for values and justification. COLLECTION.md §Frontmatter names exactly these three (with `name`) as what a promoted skill adds; omitting three of four is a contract deviation, and `README.md` line 22 already classifies it as blocking at promotion.

**5.3 — Three undefined terms sit inside mandatory record fields.** Anchors: step 3 table, "Orchestrator/runtime owns generic identity, form, substrate"; step 6.1, "storage substrate, representational form, ... and any promotion path toward stronger form or force". *Fix:* define all three inline in one added sentence each — generic identity as what the thing is and what it is made of, independent of any lens's annotations (the reading re-run F6 guessed and which worked); representational form as how the retained content is encoded and consumed (natural-language, symbolic, distributed-parametric, or mixed); and either define the form/force ladder in one clause or delete the "promotion path" field, which fractal passed to its worker verbatim and could not ground. The collection's precision test — "Could an agent with no prior context execute each step without asking a clarifying question?" — currently fails on all three.

**5.4 — Run/result ID has no template.** Anchor: step 1.1 "Allocate one run/result ID before any analysis"; step 9 makes it the canonical identity; step 10.1 verifies "unique, resolving IDs" against no registry. Raised in four trials, and six trials produced six formats. `kb/types/instruction.md` places "arbitrary choices (paths, names, templates)" squarely in what the author must fix; a naming template cannot be determined from the live system. *Fix:* one clause in 1.1 giving the form, e.g. "Use `AAS-<YYYY-MM-DD>-<system-slug>-<nn>`, where `nn` disambiguates runs against the same system on the same date."

**5.5 — Step 10.1 does not enumerate the conclusion statuses.** The §2A(i) guard on the untrialled rename. Exact wording there.

**5.6 — Step 7.4's required returns have no early-branch clause.** Anchor: "Require linked returns: material objects, routes, and claims by canonical ID; transformation class and route function; architectural status and observed candidate state; ...". Verified against the invoked procedure: both of its step-3 branches end "Then stop" and correctly substitute the global no-candidate statement and an explicit no-claim comparison. Applied as a flat checklist, 7.4 marks a correct branch return incomplete and triggers a rerun. *Fix:* append "— or, where the invoked procedure takes one of its early branches, that branch's own required substitutes (the no-candidate statement and the explicit no-claim comparison), which satisfy this requirement."

**5.7 — Worker topology contradicts step 7 for the preferred topology (re-run F3, seqthink A6).** Anchor: line 94, "Prefer fresh worker contexts that consume only the prepared evidence packet and the frozen read-only boundary." Step 7 requires reading the invoked method document, which is neither. Two trials had to explicitly authorize the read in a worker brief. *Fix:* "...consume only the prepared evidence packet, the frozen read-only boundary, and any method document this instruction directs them to execute." Note the "only" is doing real work elsewhere and must survive — this narrows the exception to method documents this instruction names, not to evidence.

**5.8 — Nothing bounds `ABS-*` inflation (re-run F4).** Anchor: line 86. The disciplining rule already exists implicitly in the same sentence ("the conclusion the absence prevents or supports"). *Fix:* make it a condition rather than a field — "Register an absence only when it bounds a conclusion someone would otherwise draw; an absence that prevents nothing has no reason to exist." For any system infinitely many things are absent, and the result's readability is what pays.

**5.9 — No rule for recording a crossing loop's fields (re-run F5).** Anchor: step 4.2's fixed ten-field record, against the step-1.4 boundary kind `complete artifact, partial loop`. That boundary kind was added precisely because this shape recurs — it is the ordinary case for MCP servers, plugins, and host-dependent tools, which is a large share of what this skill will be pointed at. The one trial that hit it improvised correctly; the next executor gets no help. *Fix:* one sentence in 4.2 — "For a loop crossing a declared external dependency, record what the in-boundary artifact contributes to each field, mark the remainder as owned by the named external participant, and do not infer that participant's policy; append the limitation naming the conclusions the crossing prevents."

**5.10 — The frozen packet's mutability is unstated (re-run F14).** Anchor: step 2.4 "Freeze the sources here". The correction branch at line 88 already implies amendability ("reruns only the work that relied on it"), but the rule is never stated, and the re-run had to run a post-hoc check after amending a packet a live worker was reading. *Fix:* "The packet is amendable as corrections arrive; a correction registered while a worker is in flight is checked against that worker's return on receipt, and only findings that rested on the superseded text are redone." This composes with the correction branch rather than adding a new mechanism.

**5.11 — Memory exclusion needs the per-instance clause.** §4C(i), exact wording there.

**5.12 — Three revision-history sentences must go, and the classify-only adjacency with them.** Anchors: line 113 "The branch is removed rather than relaxed for exactly this reason"; line 120 "This no longer decides whether the lens runs; it scopes what the lens treats as its objects"; line 151 "which remains under trial". *Fix:* keep every rule, delete the diff framing. Line 113 keeps its consequence clause ("an exit that means 'we could not tell' reads to every later reader as 'there is nothing there'") and loses the removal history. Line 120 becomes a plain statement of what the exception does ("The exception scopes what the lens treats as its objects; it does not decide whether the lens runs"), which also removes the "anyway" reversal in 122 — merge 120 and 122 into one paragraph so the exception and its hand-over read as one rule. Line 151 drops "which remains under trial" and keeps "this instruction deliberately does not fix the physical layout". A promoted instruction that carries its own changelog spends the executor's context on history it cannot use.

---

## 6. Disposition D — frontmatter

**Resolved with named values.** The deferral was correct while no workshop input fixed them; six trials now fix them by observation, so deferring again would be deferring past the evidence.

```yaml
allowed-tools: Read, Write, Grep, Glob, Bash, Task
context: fork
model: opus
```

- **`allowed-tools`** — every trial exercised exactly this set: `Read`/`Grep`/`Glob` for frozen-source inspection, `Bash` for revision pinning and `rg` sweeps (fractal also wrote its result through a shell heredoc), `Write` for the result package, and `Task` for the fresh lens workers. `Task` is the load-bearing one: without it the instruction's *preferred* topology (line 94) is silently unavailable and every run degrades to the sequential fallback — which swamp's run shows costs fresh-context lens isolation, the property three trials identified as producing their strongest independently-derived findings. Denying `Write` would be worse than it looks: fractal F11 records the harness refusing a sub-agent's `Write` of a report file, so the orchestrator must hold `Write` itself.
- **`context: fork`** — matches the operative precedent's field usage, and it is the direct answer to §7's density question: a forked context means the 4,451-word body plus a multi-worker run does not compete with whatever the invoking session already holds. This is a values choice, not a copy: the precedent's `fork` is justified by its own workflow, and this one is justified by run length and worker fan-out.
- **`model: opus`** — the one field with thinner evidence, and I am naming it rather than deferring. The trials that record a model ran on `claude-opus-5`/`claude-opus-5[1m]` (cc-dynamic explicitly; `README.md` line 103 records the trial-pool decision as `claude-opus-5` for all of them), and none ran on a smaller model. The re-run identified the `afforded`/`implemented` discipline as the one rule whose violation is silent, and §5.5's guard reduces but does not remove that reliance on executor care. **A cheaper default is untested**: if the maintainer wants `sonnet`, that needs one trial on a subject with both a crossing loop and a warrant claim before the field is changed. I am not making that trial a promotion condition.

`user-invocable: true` and `argument-hint` are already present and correct.

---

## 7. Disposition E — length and density

**Judgment: not too long for the case it was designed for; too dense to execute reliably outside it — and `context: fork` is the disposition, not a rewrite.**

The favourable-case evidence is strong: six for six completed, including two runs interrupted by usage limits mid-flight and resumed. No trial reported abandoning a step for length, and three named the frontloading (steps 3–4) as what made reconciliation cheap. Cutting the frontloading to reduce length would destroy the thing the trials actually validated.

The unfavourable cases:

- **Mid-session invocation.** This is not really a length problem; it is a shape problem. The instruction owns a whole run — source freeze, ID namespace, two spawned workers, reconciliation, an eleven-record result. Invoking it inside a session already holding other work is unsound at any length, because the run's registers would share context with unrelated state. `context: fork` makes the correct behaviour the default rather than something the invoker has to know. With that field set, I consider this case disposed.
- **A less capable model.** No evidence exists. `model: opus` pins it; §6 states what would be needed to change it.
- **The compound load.** Worth stating plainly because nothing else in the workshop does: a full run loads the candidate (4,451 words) *and* the invoked epistemic instruction (2,932), plus per-worker briefs that all six trials built by restating step 3's rules. That is the real density figure, and it is the largest in the collection by a wide margin.

**Recommended, not required (needs its own trial — do not fold it into this promotion):** extract step 3 — evidence vocabulary, definitions, canonical records and ownership, worker topology — into a bundled `records-and-vocabulary.md` in the skill directory, handed to workers verbatim. Every trial reconstructed exactly that bundle by hand into worker prompts; the seqthink trial reports the packet-as-one-file handoff being "cheap to enforce" precisely because it was one path. COLLECTION.md authorizes this link class ("Context-transfer — sub-agent invocations"). The gain is that the orchestrator body drops to ~150 lines and workers stop receiving a paraphrase of the rules. The risk is that a rules file the orchestrator no longer reads inline is a rules file the orchestrator stops applying, which is why it needs a trial rather than an edit.

---

## 8. Known limits to record in a `kb/reference/proposals/` design proposal

Not blocking; they must survive the workshop's deletion.

1. **F12** — the 7.1/7.4 boundary, with the note that erring toward including 7.4 in the worker brief is the safe default.
2. **Independent lens convergence has no schema slot** (fractal F9, gbrain F14, cc-dynamic, re-run §4). Three trials called it their most informative reconciliation output and recorded it off-schema. If the maintainer wants it now, the one-clause version is: in step 8.1, after "preserve anchored evidence conflicts as conflicts", add "and record independently convergent findings as convergence, naming the two derivations". I leave it a limit rather than a required change only because it adds a result record no trial produced under instruction.
3. **Dotted sub-anchors** (seqthink A10, "noted, not applied") — `OBJ-3.thought`, `RTE-4 (a)/(b)/(c)` extend rather than parallel the namespace, and a worker without that instinct will either violate 7.3 or violate the invoked method's split rule.
4. **Loop individuation and the runtime baseline's missing split rule** (§1.3 item 5) — the split rule arguably belongs in 4.2, since the baseline mints the IDs the lenses must extend.
5. **Named, pinned, acquirable but absent dependency** (fractal F8) — decides boundary kind.
6. **Negative live capture; evidence cutoff vs run date** (cc-dynamic F1, F2).
7. **Mid-flight capacity failure** (gbrain F15) — line 96 covers a worker dying after writing; not one killed after returning but before writing.
8. **Step 7.2's implicit prerequisites** (§1.4) — `CLM-*` and per-source `access gaps` carry two of the invoked procedure's six prerequisites without saying so.
9. **`README.md` line 18 overstates the audit's link verification** — correct the workshop record, or let it go with the workshop; either way do not carry the claim forward into a promotion note.

The upstream Branch 2 "Then stop" repair is already correctly recorded in `README.md` pending handoffs; no action needed here.

---

## 9. Explicitly not required

- The rename to `afforded` — keep it.
- Any change to the five items in "What the trials validate" that are byte-identical to trialled text: the mandatory-runtime-baseline ordering, the never-upgrade list, the static-shipped-material exclusion's *swamp-facing* half, "a candidate trigger means `applicable`", and "successful knowledge production is never a prerequisite".
- The correction branch's "misclassified by the very criterion the record states" clause — the re-run's evidence that it rescued the headline finding is the single best-grounded fact in the trial record. Do not trim it.
- A sampling rule (§4C(ii)).
- The step-3 extraction (§7) — recommended follow-up, not a promotion condition.

## 10. Questions for the user

None blocking. One optional, if a cheaper default matters: **ask user** — should `model` be `opus` (named here, backed by six opus trials) or should a `sonnet` trial be commissioned before promotion? I have set `opus` and treated the sonnet question as post-promotion work.
