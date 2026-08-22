# Atomic-claim assumptions and collection dependencies in the current full pass

## Question

Claims occur inside almost every kind of substantive text. An article, procedure, description, design proposal, or synthesis note can make claims that need grounding, qualification, and adversarial checking. That does not make the artifact itself an atomic claim. The inverse also matters: an artifact can be atomic around one system fact, decision, or outcome without being a transferable theory claim.

This audit therefore separates three questions about the current [full-improvement instruction](../../instructions/run-full-improvement-pass-on-note.md):

1. **Local claim review:** does a method inspect individual assertions wherever they occur?
2. **Artifact-level atomicity:** does a method assume that the artifact has one independently addressable contribution or commitment governing its structure, links, and continued existence—and does it then incorrectly assume that contribution must be a claim?
3. **Contract dependency:** which judgments depend on the target's collection, type, traits, or local framing, and are those inputs available early enough and guarded?

An atomic artifact can still contain premises, examples, qualifications, and consequences. Its atomicity lies in the intended import: another artifact can use it for one main contribution without inheriting an unrelated contribution. In a theory note that contribution may be a proposition; in reference it may be one shipped-system invariant or implemented decision. A composite artifact may have a unifying purpose or thesis, but its contribution depends on several claims or commitments and on the relationships among them. Summarizing a composite artifact in one sentence does not make it atomic.

## Result

The current pass couples two assumptions in its editorial core: the target is atomic, and its atomic contribution is a truth-apt central claim. That is stronger than merely checking the claims that occur in the text, and stronger than atomicity alone.

- The packet selects one artifact-supported `Update` sentence.
- Compression identifies one main claim and treats other claims as support, bloat, or split candidates.
- Critique and premise decomposition reconstruct one central commitment.
- Composition friction explicitly treats resolution into several claims as a filter failure.
- Reframing makes the title, thesis, and all other edits serve one claim.
- Merge and delete reasoning use the identity or failure of one central claim and mechanism.
- Connection work begins from a singular claim-and-mechanism summary.

This is a useful default for ordinary LLM-maintained theory notes. Atomic artifacts provide precise citation handles, make connections more discriminating, isolate warrants and revisions, and reduce the amount a consumer imports. Those benefits can also apply to an atomic reference document or decision record. What does not transfer automatically is the theory-note interpretation of the unit as a general claim with a claim title, premise tree, and explanatory-reach objective.

Commonplace already records the counterexample. The [notes contract](../../notes/COLLECTION.md) makes body composability the default, but explicitly exempts notes with the `synthesis` trait: they weave multiple cited claims into one argument and are cited as a unit. The [note type](../../types/note.md) says that this trait waives default body composability. The [article contract](../../articles/COLLECTION.md) likewise permits a self-standing explanation to carry multiple claims, mechanisms, evidence, and limits; it uses reader-facing headlines rather than claim titles and may put a case before an abstraction.

The needed generalization is therefore not “stop checking claims outside claim notes.” Local claim checks should remain available across artifact kinds. Nor is it “atomic means theoretical claim.” The needed boundary is: **derive composition shape separately from artifact function; do not impose atomicity from the presence of claims, and do not impose claim semantics merely because an artifact is atomic.**

## Where the current pass assumes atomicity

| Surface | Atomicity assumption | Effect on a legitimate composite artifact |
|---|---|---|
| Warranted contribution | `Update` is one artifact-supported sentence | Several primary updates or the relation among them must be collapsed into one privileged proposition. |
| Compression | One main claim determines whether every branch and detail earns its place | A component claim can be mislabeled as bloat even when its interaction with other claims is the artifact's contribution. |
| `critique-note` | Every mode has one central commitment | The method can attack claims, definitions, procedures, and descriptions, but it still reduces the artifact to one attack target. |
| Composition friction | The central claim must concretize in one sentence; several different claims mean failure | Legitimate plurality is reported as incoherence before the method asks whether the artifact is meant to be composite. |
| Premise decomposition | One central commitment owns one premise tree | A composite argument is forced into one tree instead of several claims plus the inferential relations that synthesize them. |
| Catalog review | Several ungated tests assume a core claim, supporting sections, and note-like title/body alignment | An artifact can receive atomic-note pressure even without `title-as-claim`; implicit `text` receives most of these gates. |
| Connect | The source is summarized through its claim, mechanism, implications, scope, and tensions | Candidate links are searched from one semantic handle instead of from a contribution map or several independently named claims. |
| Title reframe | Title and thesis are rewritten around one warranted claim; every other edit must serve it | Headline, synthesis, reference, or procedural titles are treated as failed claim titles, and secondary contributions lose standing. |
| Merge/delete | Duplicate identity is “the same claim and mechanism”; failure of the central commitment can retire the artifact | Composite identity, expository value, or a valuable synthesis relation can disappear from the disposition test. |
| Split/rehome | A separable transferable claim is extracted and the operational remainder is moved | The existence of more than one claim can become evidence for decomposition even when co-location is intentional. |
| Closing cycle | Final quality and contribution are compared against the same singular update and atomic methods | The closing run can confirm conformity to the wrong shape rather than detect that the edit destroyed a composite contribution. |

The earlier [split-and-rehome critique](../agent-note-improvement/case-01-llm-generation-relaxes-goals/instruction-split-rehome-critique.md) makes the model especially clear: identify the one main note, name its central claim, and route every other plausible idea to deletion, an open question, a new note, or the workshop. Its restraint is good—it says not to split merely to save every sentence—but its applicability condition is still “only one [idea] is strong enough to carry the current note.” It is an atomic-note repair, not a general document-shaping rule.

## Splitting is a conditional optimization

Splitting usually improves an atomic theory note when a branch has an independent claim because it gives that claim:

- its own retrieval and citation handle;
- an independently inspectable warrant and epistemic status;
- a separate review and revision lifecycle;
- more precise links; and
- a smaller import surface for downstream reasoning.

Those benefits explain why atomization is a strong default for an LLM-operated note graph. They do not establish that every artifact should be atomic. Splitting can also remove the property that makes a composite artifact valuable.

| Legitimate shape | Why several claims belong together | Appropriate split question |
|---|---|---|
| Synthesis note | The contribution is the integration, comparison, or consequence derived across cited component claims. Inline restatement is expected. | Does a component need to stand as a separately citable premise, or is it present to make the synthesis legible as a unit? |
| Article | Several claims, examples, mechanisms, and limits form one reader-facing explanatory path for an audience without KB context. | Would extraction improve the article's explanation, or merely send the reader away for a premise the article must explain locally? |
| Procedure | Multiple assertions and ordered steps jointly produce an outcome. Their unity is behavioral rather than propositional. | Can the branch execute or be maintained independently without breaking the end-to-end outcome? |
| Description or specification | Several facts jointly account for a referent or define a surface. | Does the subset describe a separately addressable referent or contract, with its own evidence and lifecycle? |
| Decision record or workshop analysis | Alternatives, evidence, and unresolved choices may need to remain together to preserve the decision surface. | Has a conclusion become durable and independently reusable, or is the relationship among live choices still the point? |

A general pass should recommend a split only when the candidate has an independent consumer or maintenance identity, not merely because it can be phrased as a distinct claim. Useful evidence includes a separate citation need, different warrant, different authority, different revision cadence, or a destination contract that gives the component an independent job. The pass should also state what contribution remains in the parent after extraction.

The notes contract already states a concise version of this rule: synthesis components should be extracted when they need to stand as citable premises. That is materially different from “extract every component claim.”

## Claim checking survives without atomicity

Local semantic review should not be gated on the whole artifact being atomic. For example:

- an article's empirical assertion can have a grounding mismatch;
- a procedure can overstate what following its steps guarantees;
- a description can blur observation and conjecture;
- a synthesis note can spread evidence for one component claim across another; and
- a design can leave a load-bearing assertion underspecified while correctly preserving its free choices.

Several catalog gates already operate at this level. `semantic/underspecified-assertions`, `semantic/grounding-alignment`, and `semantic/epistemic-status-blur` can inspect individual assertions without requiring one claim to own the artifact. The epistemic-status gate even says that one document may legitimately combine claims with different statuses; collapsing those statuses is the failure, not mixing them.

The current catalog has 42 gates. Seven are explicitly routed by `requires_trait: title-as-claim`, and one is routed to definitions. An implicit `text` artifact receives the other 34. Explicit routing therefore catches only part of the atomicity assumption:

- The seven title-as-claim gates are valid atomic-claim methods when the trait is warranted.
- Local prose and semantic gates are candidates for a shared claim-checking core.
- Ungated artifact-level tests such as `complexity/claim-to-section-ratio`, `prose/proportion-mismatch`, `frontmatter/title-body-alignment`, and `structural/general-before-specific` still carry profile or atomic-note assumptions.

`claim-to-section-ratio` does count several distinct claims, so it does not demand one claim literally. It still assumes that claims plus their support units justify the document's section structure. That can be a useful diagnostic, but its result cannot by itself say that a synthesis, article, procedure, or specification should be decomposed.

The gate schema can require a trait or type. It has no corresponding negative applicability rule such as “skip when `synthesis`.” More importantly, the direct compression, critique, friction, premise, connect, and synthesis calls do not use catalog applicability at all. Adding a trait exception only to the catalog would not remove the pass-wide atomicity assumption.

## Collection and contract dependency

### Dependency in the current procedure

| Dependency | Where it enters | Present problem |
|---|---|---|
| Source `COLLECTION.md` for connection routing | `cp-skill-connect` | This is an intrinsic dependency because the collection authorizes destination collections and link labels. It should remain. |
| Source collection and type for fit and disposition | Step 7 synthesis | It arrives after compression, critique, friction, premise decomposition, catalog review, and connect have already imposed their target model. |
| `kb/notes/COLLECTION.md` claim modality | Premise decomposition | It is hard-coded even for targets outside the notes collection and for procedure mode. |
| Type and collection conformance assays | Available in the review selector | The full pass requests seven catalog bundles instead of `--all-gates`, so it omits both conformance pairs in the initial and closing cycles. |
| Collection/type assumptions embedded in catalog criteria | Self-contained gate text | These are baked-in profile couplings, not live dependencies. A collection-contract edit does not stale their accepted results. |
| Collection, type, traits, and local framing used by synthesis | Packet reasoning | Only source and optional merge target are captured and guarded. A contract or framing change can invalidate the edit rationale while the source hash still matches. |

The collection dependency is thus both too late and incomplete. Moving the existing collection-fit paragraph to the start would help, but would not be enough. Preflight must use the contracts to select methods and interpret findings, and the packet must retain the inputs that materially authorized its transformation.

Catalog gates present a special constraint. Their criteria must remain self-contained because review freshness hashes the artifact and criterion, not an unrecorded live contract. Collection-wide conformance belongs in the existing collection-conformance pair. A profile-specific catalog gate should either encode its applicability explicitly or be routed by preflight; telling every gate worker to consult a changing `COLLECTION.md` would introduce an untracked freshness dependency.

### Collection does not decide atomicity alone

The relevant authority is a composition of contracts and local facts:

1. **Collection** supplies the local text contract: quality goal, lifecycle, link grammar, and broad mutation boundary.
2. **Type** supplies structural kind and semantic expectations.
3. **Traits** declare narrower review expectations and exceptions such as `title-as-claim` and `synthesis`.
4. **Local framing and artifact text** establish the immediate purpose, open choices, and whether the current shape is intentional.
5. **Composition shape** determines whether artifact-wide review may assume one commitment or must preserve several contributions and their relations.

The collections demonstrate why no one-field routing rule is sufficient:

- `kb/notes/` defaults toward claim titles and body-composable notes, but explicitly admits synthesis notes, multi-claim specs, definitions, indexes, and exploratory drafts as exceptions.
- `kb/articles/` is claim-bearing and permits composite expository artifacts. Its titles are headlines and its case-first order can be intentional.
- `kb/reference/` can contain atomic system-scoped accounts and decisions alongside composite architecture documents. Its local contract changes the evaluation objective and title grammar, not the number of contributions an artifact may contain.
- other descriptive collections can contain an argumentative analysis whose individual claims deserve strong review without converting the whole analysis into a premise-like note.
- `kb/work/` contains claims, designs, evidence, records, and decision surfaces under one heterogeneous workshop contract.
- `kb/instructions/` contains claims, but its artifact-level identity is an executable behavior whose edits can change the deployed procedure.

Collection is therefore a binding objective and a strong prior, not a complete atomicity classifier. Type alone also fails: the `note` type itself carries a `synthesis` exception, and the same general type can live under different collection contracts.

### Reference supplies atomic non-theory cases

The [reference contract](../../reference/COLLECTION.md) asks for fidelity to the shipped Commonplace system, economy, and topical titles by default. None of those clauses requires a reference document to be composite.

- [The collection–type split is asymmetric](../../reference/collections-never-own-frontmatter-semantics.md) is organized around one bounded system invariant: collection contracts never own frontmatter semantics. Its reasoning and examples support that one reference-scoped commitment.
- [Full improvement pass closure](../../reference/full-improvement-pass-closure.md) records one shipped closure rule and its calibration boundary: reassess final bytes once, retain residual findings, and do not claim convergence.
- An [ADR](../../reference/types/adr.md) is atomic around one implemented architectural decision even though its body also carries context, alternatives, and consequences.

These artifacts can benefit from a small import surface, branch detection, precise connections, and independent maintenance—the same structural advantages sought by atomic theory notes. Their review semantics differ:

- fidelity to implementation or decision history replaces cross-system explanatory reach;
- a topical or numbered title can be correct even when the body has one central commitment;
- a discrepancy with the shipped referent or recorded decision is the primary defeater;
- duplicate identity is the same system fact, contract surface, or decision, not necessarily the same general claim and mechanism; and
- a split is warranted by a separately addressable referent or decision, not merely a second true assertion.

Reference therefore supplies the missing cross-product case: `description/decision + atomic`. It shows why the generalized pass cannot use a single “atomic-claim” route.

## A better factoring boundary

The shared pass should resolve two independent routing axes before expensive review:

```text
artifact function: claim | definition | procedure | description | design | exposition | ...
composition shape: atomic | composite | undetermined
```

These are not aliases. A claim-bearing article may be `exposition + composite`; a normal theory note may be `claim + atomic`; a synthesis note may be `claim/argument + composite`; a reference invariant may be `description + atomic`; an ADR may be `decision + atomic`; and a procedure may have one intended outcome without being a truth-apt claim.

### Shared shell

- target capture and immutable start-state identity;
- collection, type, trait, lifecycle, local-frame, and authority preflight;
- local assertion checks for grounding, scope, epistemic status, ambiguity, and link accuracy;
- report-only assessment before mutation;
- abstention when function or composition shape is underdetermined;
- guarded mutation barrier and final-byte reassessment; and
- explicit authority for destructive or relocating dispositions.

### Atomic shape adapter

- one primary contribution, named in the artifact function's own terms;
- branch and proportion checks relative to that contribution;
- artifact-level critique and disposition around one contribution identity;
- duplicate detection using the function's identity rule; and
- split recommendations for branches with independent use or maintenance identity.

### Composite shape adapter

Instead of manufacturing one `Update`, record:

- the artifact's unifying purpose or thesis;
- its primary claims or commitments;
- the relations among them that make their co-location valuable;
- the warrant and epistemic status of each load-bearing claim;
- which components already have or need independent citation identities; and
- what would be lost if the artifact were split.

Single-commitment methods can still run inside a composite artifact, but only against a named component. Composition friction should not report “several claims” as failure when plurality is declared. Premise decomposition should produce separate trees or a synthesis-level dependency map. Compression should ask whether a passage serves the integration or reader path, not only whether it supports one main claim.

### Function adapters

Composition shape decides how many primary contributions the pass must preserve. Artifact function decides how each contribution is tested and repaired.

- **Claim:** test truth, warrant, scope, modality, premises, and inferential joints; use claim-title and claim/mechanism identity only when the contract and traits authorize them.
- **Description:** test fidelity, coverage, evidence boundaries, and discrepancies against the referent; preserve descriptive scope even when a broader theory is plausible.
- **Decision:** test the chosen outcome, forces, alternatives, consequences, status, and operativity path; preserve numbered ADR title grammar.
- **Procedure:** test whether the ordered behavior produces the stated outcome under its declared conditions.
- **Exposition:** test the reader's explanatory path, including whether locally repeated claims and examples are necessary for self-standing understanding.

The current pass is not merely an atomic shape adapter. It is mostly the `claim + atomic` cell with a few partially routed methods. Generalizing it requires factoring both dimensions.

This factoring keeps the advantages of atomic notes without turning them into a universal ontology of documents.

## Guarding implications

The [full-pass report type](../../reports/types/full-pass-report.md) captures the source and, for a merge, the merge target. It does not capture the governing collection contract, type contract, traits as interpreted at preflight, or a workshop framing file used to determine function and composition shape.

That creates a time-of-check/time-of-use gap. A packet may recommend a split under one body-composability rule; the collection or type contract may change to recognize a composite shape; the source bytes remain identical; and `commonplace-guard-full-pass-report` still passes. The same risk applies when an article lifecycle state or local workshop decision changes what edits are authorized.

Only dependencies that materially select a method, edit, or disposition need packet identity. The analysis does not yet decide whether to capture full contract bytes, record their hashes, or represent their relevant decisions directly. It does establish that calling only source and merge target the complete guarded-input set understates the current reasoning dependency.

## Best next comparisons

The next cases should test both axes independently:

1. **Atomic theory note:** establish that the existing split and central-claim methods retain their benefits under their intended default.
2. **Atomic reference document or ADR:** hold atomicity constant while changing function and collection objective; retain atomic compression benefits without claim-title or explanatory-reach pressure.
3. **`synthesis` theory note:** hold the theoretical collection constant while changing composition shape; test whether the pass misreads component claims as branches.
4. **Composite article:** test local claim review while withholding claim-title, atomic split, and general-before-specific assumptions.

Two paired comparisons now isolate the dimensions. An atomic note and a synthesis-trait note in `kb/notes/` hold the collection contract constant and vary shape. An atomic theory note and atomic reference document hold shape approximately constant while varying function, scope, title grammar, and quality objective.

## Working conclusions

- Claims should be checked wherever they occur; this does not imply that every artifact is one claim.
- Atomicity is independent of claim function: reference descriptions and ADRs can be atomic without being transferable theory claims.
- The current full pass treats one central claim as the artifact's identity in enough places that it remains a `claim + atomic` theory-note pass, not a general atomic-artifact pass.
- Atomic notes are a valuable default for graph addressability and LLM maintenance, but splitting is justified by independent use and maintenance, not by claim plurality alone.
- The existing `synthesis` trait is a first-class counterexample to universal atomization, and current full-pass routing does not honor it.
- Articles provide collection-level counterexamples when they are intentionally composite: they remain claim-bearing while using headlines and sometimes case-first exposition.
- Collection conformance must enter before method selection and again at closing, but collection alone cannot determine composition shape.
- Any contract or framing input that materially authorizes a split, reframe, or disposition must be represented in the guarded packet dependency.

These are analysis results, not yet a choice between one routed workflow, several adapters, separate procedures, or an intentionally atomic-note-only full pass.

## Evidence used

- [Case 01](./case-01-workshop-experiment-design.md) — observed cross-contract failure and useful mechanical behavior.
- [Run a full improvement pass on one note](../../instructions/run-full-improvement-pass-on-note.md) — current orchestration, synthesis, disposition, and closing contract.
- [Split and rehome critique](../agent-note-improvement/case-01-llm-generation-relaxes-goals/instruction-split-rehome-critique.md) — explicit one-main-note decomposition model behind the current split pressure.
- [Notes collection contract](../../notes/COLLECTION.md) and [note type](../../types/note.md) — body-composability default and the explicit `synthesis` exception.
- [Article collection contract](../../articles/COLLECTION.md) — valid multi-claim, headline-titled, case-first expository shape.
- [Reference collection contract](../../reference/COLLECTION.md), [collection–type boundary](../../reference/collections-never-own-frontmatter-semantics.md), [full-pass closure](../../reference/full-improvement-pass-closure.md), and [ADR type](../../reference/types/adr.md) — atomic, system-scoped description and decision cases under the non-notes local contract.
- [Review-gate type](../../types/review-gate.md) — current positive applicability fields and self-contained freshness requirement.
- [Collection-conformance decision](../../reference/adr/041-collection-conformance-reviews-use-collection-md-as-the-gate.md) — existing factored collection dependency the full pass does not request.
- [Collections and types](../../reference/collections-and-types.md) — the orthogonal collection/type model.

---

Workshop outputs:

- [Artifact function as a routing field](../../reference/proposals/artifact-function-as-a-routing-field.md) — produces: turns the function-versus-composition finding into a finished, undecided design with carrier, resolution, operativity, and adoption options
