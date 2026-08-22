# Commitment audit: draft.md (analyse-agentic-system SKILL.md, new write)

Audited artifact: `draft.md` against `claim-skeleton.md` (binding plan), `claim-disposition.md`, `reconstruction.md`, `brief.md`, `kb/instructions/COLLECTION.md`, `kb/types/instruction.md`, and targeted reads of the named sources. Findings are anchored; each recommends exactly one action.

Overall verdict on the writer's zero-`NEW COMMITMENT FOR AUDIT` claim: substantially accurate. The section-by-section comparison found no silently introduced thresholds or definitions and no reordered obligations. Two additions carry new force beyond the skeleton (findings 1.1 and 1.2); one is grounded, one needs a small alignment.

Reconciliation: all 27 findings disposed into `candidate.md` (2026-08-20). No finding required a user decision.

## Pass 1 — Claim delta (draft vs claim-skeleton)

### 1.1 Run-ID citation obligation strengthened
Status: resolved
Anchor: step 1.1, "Allocate one run/result ID before any analysis; every later record cites it."
The skeleton (§1) fixes only "Allocate one run/result ID before analysis"; the universal-citation obligation appears nowhere in the plan. Skeleton §9 requires only "one canonical result identity and resolvable IDs across physical parts," and the draft's own Verify bullet requires every lens record to cite the *source register*, not the run ID. This is a silently strengthened rule that creates per-record busywork the plan did not commit to.
Recommendation: clarify — either scope it to the skeleton's actual commitment (records belong to one run whose result carries the canonical identity) or deliberately adopt the stronger rule and say so in the workshop record.
Resolution: scoped to the skeleton's commitment. Candidate step 1.1 now reads "every record the run produces belongs to that run, and the emitted result carries the ID as its canonical identity" — membership plus canonical result identity, no per-record citation obligation. Basis: skeleton §1 and §9.

### 1.2 New prohibition "do not analyse from recollection"
Status: resolved
Anchor: Prerequisites, "If no source input is reachable at all, stop immediately and report the missing prerequisite; do not analyse from recollection."
Not in the skeleton, but grounded: `brief.md` excludes "claims beyond the declared evidence boundary," skeleton §2 requires a blocker report when no stable inspectable boundary exists, and the hard-fail-at-top prerequisite pattern is established collection practice. The prohibition operationalizes existing commitments rather than adding a new one.
Recommendation: keep — basis: brief scope exclusion; skeleton §2 blocker rule.
Resolution: kept unchanged in the candidate on the cited basis.

### 1.3 Added sentence "they do not change the tier silently"
Status: resolved
Anchor: step 3, Evidence vocabulary, "Mixed inspection gaps stay claim-local limitations; they do not change the tier silently."
The second clause is additional to skeleton §3 ("Mixed gaps remain claim-local limitations") but is entailed by the skeleton's no-silent-upgrade family (§3 "Never upgrade...", §7 "no silent evidence upgrade") and the brief's acceptance criteria.
Recommendation: keep — basis: skeleton §3 never-upgrade rule; brief acceptance criteria.
Resolution: kept unchanged in the candidate on the cited basis.

### 1.4 Added sentence on absent lens sections
Status: resolved
Anchor: step 5, "An absent lens section or file must never carry the disposition implicitly."
Not verbatim in skeleton §5, but a planned commitment: disposition A (applicability row: "Applicability is a routing result owned by the whole analysis, not an inference readers must make from an absent file or section"), reconstruction R6.8, and the brief's acceptance criterion "avoid making absent lens files carry hidden meaning."
Recommendation: keep — basis: disposition section A applicability row; brief acceptance criteria; R6.8.
Resolution: kept unchanged in the candidate on the cited basis.

### 1.5 Added clause "a `consolidate` or `import` label never establishes semantic preservation"
Status: resolved
Anchor: step 6.5.
Grounded in reconstruction §3.4 (the memory type's `imported`/`consolidate` labels cannot be assumed semantically preserving; "never lets operational lineage imply semantic warrant") and disposition B (curation/lineage vs transformation row). A concretization, not a new commitment.
Recommendation: keep — basis: reconstruction §3.4 and R6.10; disposition B curation/transformation row.
Resolution: kept unchanged in the candidate on the cited basis.

### 1.6 Planned omissions: cold-trial cases and marker-classification table
Status: resolved
Anchor: draft as a whole (no promotion-trial section; no blocker/marker table).
The skeleton's four cold-trial cases and the marker table are workshop planning material. Disposition E explicitly routes trial evidence to "later workshop trial and acceptance artifacts... without becoming permanent executor-facing procedure text," and the skeleton classifies R6.18 as "blocking for promotion, not drafting." The skeleton's trailing publishable-limitations/blockers lists were correctly carried into draft step 9 rather than dropped.
Recommendation: keep — basis: disposition section E trial row; skeleton marker table R6.18.
Resolution: kept unchanged in the candidate on the cited basis; the cold trials remain a workshop stage on the exact candidate.

## Pass 2 — Artifact shape (vs claim-disposition)

### 2.1 One practical purpose, embed/invoke split realized as planned
Status: resolved
Anchor: opening paragraphs and steps 4, 6, 7 ("Run a mandatory runtime baseline... This skill owns the whole run..."; step 7.1 "Invoke [...] Do not copy or restate its... method").
The draft exposes exactly the disposition's single practical purpose (section A row 1), embeds the runtime and memory/context operations (section B preamble: embedded "because no library instruction is an adequate modular lens"), and invokes the epistemic instruction by path rather than copying it. The opening's ownership sentence ("Lens workers execute inside that ownership; they never establish their own boundary or publication") realizes disposition A worker row and B wrapper row.
Recommendation: keep — basis: disposition section B preamble and A rows 1, 9–10.
Resolution: kept; the candidate preserves the shape (ownership sentence lightly reworded only to introduce the orchestrator per finding 5.1).

### 2.2 No smuggled independent transferable claims
Status: resolved
Anchor: steps 4.1, 4.3 (runtime responsibility and anti-conflation rules), step 3 definitions.
The draft inlines only executable rules from the cite-existing theory notes and credits them through footer `rests-on` links, matching disposition D ("the instruction should inline only its executable questions"). No section states a transferable claim as an original contribution of this skill.
Recommendation: keep — basis: disposition section D rows and their "why this boundary is useful" columns.
Resolution: kept unchanged in the candidate on the cited basis.

### 2.3 "Tempting branches to omit" honored
Status: resolved
Anchor: whole draft, checked branch by branch.
Ranking/adoption/taxonomy prohibited (opening; step 4.4); no separate lens promotion and no copied epistemic procedure (steps 6–7); memory editorial/publication mechanics excluded (step 6.6); no schema/parser/matrix work and no memory-schema reuse (steps 9–10.3, incl. no mention of the `trace-learning`/`trace-derived` defect); no collection changes, corpus relocation, review replacement, or index maintenance anywhere; no source-specific commands or trial-domain values.
Recommendation: keep — basis: skeleton "Tempting branches to omit" list; disposition sections C and E.
Resolution: kept; the candidate introduces no omitted-branch content.

## Pass 3 — Grounding

### 3.1 Six footer note links: targets exist, annotations accurate
Status: resolved
Anchor: footer, all six `rests-on` entries.
All six files exist. Annotation checks: the runtime note does state the three causal responsibilities behind step 4; the orchestration note's description ("not ordered along a single ladder... vary independently") supports "why the runtime inventory stays open"; the governance note supports "governance surfaces are conditional, crosscutting inspections"; the memory-crosscutting note supports "memory is a lens inside system analysis"; the storage/activation note separates existence/read-back/activation as claimed for steps 3, 5, 6; the behavioral-authority definition is the consumer/channel/force path definition behind `BAP-*`.
Recommendation: keep — basis: inspected note descriptions and bodies; disposition section D cite-existing rows.
Resolution: kept; link texts corrected to the notes' actual titles under finding 6.4.

### 3.2 Epistemic invocation consistent with the invoked instruction
Status: resolved
Anchor: step 7.1–7.4; path `kb/instructions/analyse-external-system-epistemic-architecture.md`.
The path exists. The invoked instruction's "Scope and prerequisites" asks for exactly what step 7.2 passes (system and revision, declared scope, analysis question, source identities, claims, gaps), so the pass-list is sufficient to start it. Its scope branch ("general review with no knowledge-production question, stop") is satisfied because the wrapper passes a bounded epistemic subquestion. Step 7.3's "no system-wide epistemic grade" matches its output-6 rule; step 7.4's "three authority records kept separate" matches its ledger fields (epistemic authority, operational authority, behavioral-authority path). Its unnamed source-ID scheme admits adopting the orchestrator's `SRC-*` IDs, so "no parallel ID namespace" is enforceable.
Recommendation: keep — basis: inspected `kb/instructions/analyse-external-system-epistemic-architecture.md`; skeleton §7.
Resolution: kept unchanged in the candidate on the cited basis.

### 3.3 "episode status" is not the invoked method's vocabulary
Status: resolved
Anchor: step 7.4, "architectural status and episode status".
The invoked instruction's term is "observed candidate state" (its outputs 3–4); "episode status" appears nowhere in it. The phrase is the reconstruction's own summary word (§1.3 "episode evidence") carried through the skeleton. An executor mapping the invocation's returns must guess the correspondence.
Recommendation: clarify — use the invoked method's term ("architectural status and observed candidate state") so the required returns name fields the invoked instruction actually produces.
Resolution: candidate step 7.4 now requires "architectural status and observed candidate state", matching the invoked instruction's own output vocabulary.

### 3.4 Behavioral-authority definition adds "horizon" beyond the cited definition
Status: resolved
Anchor: step 3 Definitions, "**Behavioral authority**: one consumption path's consumer, channel, force, and horizon" together with footer link "Behavioral authority — rests-on: the consumer/channel/force path definition".
The linked definition note defines consumer, channel, and force only; horizon comes from the epistemic instruction's behavioral-authority path and was planned as a skill-side extension (disposition D: "the skill adds run-specific IDs and horizon"). The draft presents the four-part form as the definition, silently diverging from the vocabulary authority it cites.
Recommendation: clarify — one clause marking horizon as this run's extension (e.g. "consumer, channel, and force, plus this run's horizon field"), keeping the cited note authoritative for the term.
Resolution: candidate definition now reads "consumer, channel, and force — the cited definition fixes these three parts — plus this run's `horizon` field, a run-level extension recorded on each `BAP-*` path", keeping the note authoritative.

## Pass 4 — Specificity (load-bearing ambiguity only)

### 4.1 "central runtime account" is undefined and decides the tier
Status: resolved
Anchor: step 3, "the analysis is `code-grounded` only when implementation material was inspected to the depth of the central runtime account".
Reconstruction R6.3 demanded this mapping be defined; the skeleton answered with this phrase but never defined it, and no input fixes it. The tier assignment — the run's single overall evidence label — turns on it, so two executors can tier the same run differently. The nearest defined anchor is the draft's own step 4 (the runtime baseline).
Recommendation: clarify — tie it to step 4 explicitly, e.g. code-grounded only when the material loops recorded in the runtime baseline rest on inspected implementation.
Resolution: candidate tier rule now reads "`code-grounded` only when the material loops recorded in the step-4 runtime baseline rest on inspected implementation material"; the undefined phrase is gone.

### 4.2 "material loop" has no materiality test
Status: resolved
Anchor: step 4.2, "For each material loop, record...".
Step 4.4 gives a materiality rule for surfaces (alters the question, a control path, evidence strength, or a lens result) but no rule says which loops are material, and loop selection determines the entire runtime account's coverage. The skeleton has the same gap (R6.5 asked for the finite-baseline rule); this is a draft-level executability gap under the collection's precision test, not a writer deviation.
Recommendation: clarify — extend step 4.4's materiality test to loops, or state the loop-inclusion rule directly.
Resolution: candidate step 4.2 now closes with "A loop is material under the same test step 4.4 applies to other surfaces: include it when it alters the analysis question, a control path, evidence strength, or a lens result."

### 4.3 "sufficiently inspected boundary" vs the invoked method's recorded-search-boundary phrasing
Status: resolved
Anchor: step 3, `absent` — "not found inside a named, sufficiently inspected boundary".
The wording is the skeleton's, but the workshop's named source fixes a more executable formulation: the epistemic instruction records absences "within the recorded search boundary" — the executor names what was searched instead of self-certifying sufficiency. "Sufficiently" invites exactly the judgment the negative-finding rule is meant to externalize.
Recommendation: clarify — adopt the recorded/named search-boundary form ("not found within the named, recorded search boundary") consistent with the invoked method.
Resolution: candidate `absent` status now reads "not found within the named, recorded search boundary", aligned with the invoked method.

### 4.4 "evidence packet" contents never specified
Status: resolved
Anchor: step 2.4 "Prepare the evidence packet once"; step 7.2 and 7.5 consume it.
No input fixes packet contents (R6.12 left packet-vs-access open; the skeleton chose "packet plus frozen read-only boundary" without saying what the packet holds). An executor cannot prepare it without guessing, and packet content controls what lens workers can see. Minimal fix, no user decision needed: the draft already names the candidate contents in step 7.2.
Recommendation: clarify — one sentence in step 2.4, e.g. the packet comprises the source register, boundary declaration, canonical records to date, and the anchors relevant to each lens; anything further is a targeted read under step 2.4's rule.
Resolution: candidate step 2.4 now specifies "the packet comprises the source register, the boundary declaration, the canonical records registered so far, and the citation anchors relevant to each lens; anything beyond it is a targeted read under this step's rule."

## Pass 5 — Relevance and audience

### 5.1 "Orchestrator" used without introduction
Status: resolved
Anchor: step 3 ownership table ("Owner: Orchestrator") and step 2.4/7.4 ("returns to the orchestrator").
The term first appears as a table value with no definition; the opening speaks only of "this skill owns the whole run." A first-reading executor can infer that the orchestrator is the agent executing this skill, but the collection's frontloading rule says define terms inline rather than rely on inference.
Recommendation: clarify — one clause in the opening or step 1 ("the agent executing this skill — the orchestrator below — ...").
Resolution: candidate opening now states "The agent executing this skill is the orchestrator referred to below; lens workers execute inside its ownership and never establish their own boundary or publication."

(The other forward dependency found in this pass — "Lens workers" in step 2.4 governed by topology rules stated only in step 7.5 — is treated under writer-flag finding WF-a.)

## Pass 6 — Compression, prose, contract fit

### 6.1 Inline `— invokes:` mixes footer label grammar into an inline link
Status: resolved
Anchor: step 7.1, "Invoke [Analyse an external system's epistemic architecture](kb/instructions/analyse-external-system-epistemic-architecture.md) — invokes: run the accepted route-analysis method inside this run's boundary."
COLLECTION.md authorizes two link forms: inline "with a connective word that fits" and footer "`- [title](path) — label: context phrase`". "Invoke [title](path)" is already the authorized inline form carrying the `invokes` relation (and the link is a permitted context-transfer case); the appended "— invokes: ..." grafts footer grammar into a sentence and restates the verb.
Recommendation: clarify — drop the "— invokes: ..." tag; keep the imperative inline link and fold any needed context into the sentence.
Resolution: candidate step 7.1 drops the tag and folds the context in: "Invoke [title](path) to run the accepted route-analysis method inside this run's boundary."

### 6.2 Workspace-root link paths are the authorized form for promoted skills
Status: resolved
Anchor: all links, e.g. footer "(kb/notes/agent-runtime-analysis-should-separate-scheduling-context-state.md)" and step 7.1's `kb/instructions/...` path.
From the eventual directory `kb/instructions/analyse-agentic-system/`, these would not resolve as plain relative links — but COLLECTION.md's Promoted skills section explicitly requires this form: promoted skills "must not rely on on-disk location" and "should use stable workspace-root paths (`kb/notes/`, `kb/instructions/COLLECTION.md`)". The draft also links into no forbidden collection (no `kb/agent-memory-systems/`, `kb/agentic-systems/`, or `kb/work/` targets).
Recommendation: keep — basis: COLLECTION.md "Promoted skills" path rule and outbound-link scan rule.
Resolution: kept; the candidate retains workspace-root paths throughout, including the three added footer entries.

### 6.3 Frontmatter, title, description, and sections conform
Status: resolved
Anchor: frontmatter lines 1–5; H1 "Analyse an Agentic System"; Prerequisites/Steps/Verify sections.
`description` names the trigger condition as both contracts require; `type: kb/types/instruction.md` matches the template; the title is imperative and is the brief's fixed provisional title, corresponding to the skill name `analyse-agentic-system`; the default template's required sections are all present. (Field completeness for a promoted skill is WF-d.)
Recommendation: keep — basis: brief target section; COLLECTION.md title/description and template; kb/types/instruction.md frontmatter rules.
Resolution: kept; candidate adds only the WF-d fields (`user-invocable`, `argument-hint`) on top of the conforming set.

### 6.4 Two footer link titles diverge from the notes' actual titles
Status: resolved
Anchor: footer, "[Agent-runtime analysis should separate scheduling, context, and state]" and "[Runtime structure determines governance control surfaces]".
The notes' H1s are "Agent-runtime analysis should separate scheduling, context assembly, and external state" and "Runtime structure determines the control surfaces available to governance". The paraphrases are close but the link-text convention is `[title](path)`, and the second paraphrase drops the note's actual claim shape (structure determines which surfaces are *available*).
Recommendation: clarify — use the notes' own titles as link text.
Resolution: candidate footer uses both notes' exact H1 titles as link text; the three added packaging entries also use their notes' exact H1 titles (verified against the files).

### 6.5 Scoped repetition of the ranking/taxonomy prohibition
Status: resolved
Anchor: opening ("Do not produce product rankings, generic adoption advice, a universal taxonomy or maturity ladder...") and step 4.4 ("Do not turn this inventory into a universal taxonomy, fixed template, maturity ladder, ranking, or adoption advice.").
The repetition is scoped rather than redundant: the opening bounds the whole skill; step 4.4 bounds the specific temptation at the point where the surface inventory is built. Both instances are planned (brief exclusions; skeleton §4).
Recommendation: keep — basis: brief exclusions; skeleton §4 and "Tempting branches" list.
Resolution: kept unchanged in the candidate on the cited basis.

## Writer-flagged ambiguities

### WF-a Worker-topology/fallback rules placed in step 7 but scoped to any applicable lens
Status: resolved
Anchor: step 7.5, "Worker topology, for any applicable lens: ... If neither path can run an applicable lens, stop with an explicit capacity or dependency blocker..."
The placement faithfully mirrors skeleton §7, but the skeleton is a commitment plan, not a prose layout, and the disposition treats the fallback as run-level execution policy ("Worker topology is execution policy of the public workflow, not a semantic property of memory or epistemic analysis"). As drafted, an executor running the memory lens at step 6 — and one deciding how lens workers consume the packet at step 2.4 — has not yet read the rule that governs them; the sequential-execution and blocker branches also apply to step 6. This is an executability defect the reconciler can fix without user input.
Recommendation: clarify — move the topology/fallback rule to a run-level position (end of step 3, or a short rule before step 6) or add an explicit forward reference from steps 2.4 and 6; step 7 then keeps only the epistemic-specific packet-passing.
Resolution: candidate moves the rule to a "Worker topology" subsection at the end of step 3 (run-level, before both lenses, immediately after step 2's packet rules), scoped "any applicable lens (steps 6 and 7)"; step 7 now ends at item 4 with only the epistemic-specific packet-passing and return requirements.

### WF-b The step-1 `out of scope` early exit has no fixed field shape
Status: resolved
Anchor: step 1.2, "If not, exit early with an `out of scope` result and stop."
No workshop input fixes fields for this record: the brief's "explicit early exits" requirement and R6.8 concern the *lens* dispositions, whose shape the skeleton and draft do fix in step 5. The type spec directs authors to fix only what the executor cannot determine; an executor exiting at step 1.2 can state the subject, the scope test failed, and the stop without a schema, and inventing fields would be an unplanned commitment.
Recommendation: keep — basis: kb/types/instruction.md detail-level rule ("Fix only what the executor can't determine"); skeleton §1 (names the exit, fixes no fields); brief scope (early-exit shape mandated only for lenses).
Resolution: kept unshaped in the candidate on the cited basis.

### WF-c Two packaging-theory notes omitted from the footer
Status: resolved
Anchor: footer (six links; no link to `kb/notes/skills-are-instructions-plus-routing-and-execution-policy.md` or `kb/notes/frontloading-spares-execution-context.md`).
Disposition section D disposes both as `cite existing` with those notes as target paths (the frontloading row also names `kb/notes/model-resolved-indirection-adds-interpretation-work-to-llm-execution.md`; all three files exist). The writer's rationale — they ground the authoring-time embed/invoke choice, not the executor's procedure — is precisely the audience `rests-on` serves: COLLECTION.md says rests-on links are for "reviewers and developers updating the procedure, never executing agents." The embed/invoke split is the draft's most contestable structural choice, and its grounding is currently invisible to the meta-reader the label exists for.
Recommendation: ground — add footer `rests-on` entries for the packaging notes per disposition D (the skills-packaging note behind the SKILL.md form; the frontloading and model-resolved-indirection notes behind the embed-runtime/memory-vs-invoke-epistemic choice).
Resolution: candidate footer adds all three `rests-on` entries with the notes' exact H1 titles and context phrases naming what each grounds (SKILL.md packaging; embedded lens procedures; embed-versus-invoke interpretation cost).

### WF-d Frontmatter limited to `name`/`description`/`type`
Status: resolved
Anchor: frontmatter, lines 1–5.
COLLECTION.md says promoted skills "add skill-specific fields (`name`, `allowed-tools`, `context`, `model`)"; the type spec defers additional frontmatter to the runtime consumer. The writer is right that no input fixes *values* for `allowed-tools`/`context`/`model` — the operative precedent's values (`context: fork`, `model: opus` in `known-instructions/current-memory-review-skill.md`) belong to a different workflow and would be unsupported completions here. But that precedent also carries `user-invocable: true` and an `argument-hint`, and the brief's operativity section does fix the channel ("a local user-invocable skill" with explicit invocation; disposition A row 2 makes the channel a central contribution). Omitting the invocability field leaves the fixed channel unrealized; omitting the tool/context/model fields is a genuine promotion-stage decision.
Recommendation: clarify — add `user-invocable: true` (channel is fixed by the brief; field evidenced by the operative skill precedent) and consider an `argument-hint` for the system identifier; leave `allowed-tools`/`context`/`model` absent but record that deferral explicitly in the workshop README so promotion resolves it deliberately (R6.17 classifies operativity as blocking if unresolved at promotion).
Resolution: candidate frontmatter adds `user-invocable: true` and an `argument-hint` for the system identifier plus source input, and leaves `allowed-tools`/`context`/`model` absent; the deferral is recorded in the workshop README (promotion must resolve it explicitly).
