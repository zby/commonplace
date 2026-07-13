# Workshop: epistack-submission_for_fable

> **Fable scope:** This variant is scoped to the LHC and eggs cases only. The original workshop remains unchanged.
This workshop is building the entry to the FLF [Epistemic Case Study Competition](../../sources/epistemic-case-study-competition.md). **Due 19 July 2026**; opened 12 July, it has roughly six working days and closes at submission.

The two existing epistack workshops are inputs, not competitors to this one: [epistack-competition](../epistack-competition_for_fable/README.md) holds the two-repo protocol (framework here, casework in the sibling `epistack-casebooks`), and [epistack-framework-additions](../epistack-framework-additions_for_fable/README.md) holds the design menu of candidate additions. Neither decides what we submit. This workshop does.

## The pitch

**The Commonplace Casebook Protocol is a Structure-layer protocol for compounding epistemic investigations without flattening their arguments. Commonplace is its working reference implementation.**

This is one of the submission shapes the brief explicitly invites: a protocol enabling interoperability and compounding while preserving nuance, demonstrated on the cases and maintained as sources, users, and AI capabilities change. It also anchors the work in one named stack layer. The protocol structures how heterogeneous claims, positions, evidence, caveats, and subquestions connect; it does not force every dispute into one universal argument ontology.

The design rule is: **standardize the connective tissue, not the contested substance.** A conforming casebook standardizes source identity, artifact roles, relationship semantics, local contracts, validation, review state, and change semantics. Claims and justification remain in attributed prose, where differences in framing and scope stay visible.

### The protocol surface

- **Source identity and attribution** — citations resolve to retained snapshots with explicit capture fidelity.
- **Artifact identity and local contracts** — addressable Markdown artifacts declare their roles, while each collection declares the case-local grammar its artifacts obey.
- **Discourse and inference relationships** — labelled, contextual links expose positions, subquestions, evidence, objections, dependencies, caveats, and contested joints.
- **Non-flattening extension** — case-specific structures may be introduced locally without silently becoming universal framework concepts.
- **Deterministic conformance** — schemas, links, dates, and verbatim quotations are machine-checked; false assertions fail.
- **Semantic review** — truth, grounding, consistency, and completeness remain criterion- and snapshot-anchored LLM judgments rather than pretend-deterministic fields.
- **Maintenance and handoff** — source, artifact, criterion, and model changes expose targeted stale work another agent can discover and continue.

### Commonplace as the reference implementation

The implementation is running code, not a proposed format. `commonplace-validate` and `commonplace-verify-quotes` enforce referential claims ([ADR 046](../../reference/adr/046-verbatim-quotes-are-validated-against-their-cited-source.md)); collection and type contracts enforce the artifact grammar; snapshot-anchored review gates and model partitions preserve review provenance and freshness ([review system](../../reference/README-REVIEW-SYSTEM.md)). The welded-token form — `**Axis:** \`value\` — justification` — demonstrates how a machine-readable value can remain attached to the prose that earns it, with derived matrices checked rather than maintained as a second truth.

### Demonstration on the two cases

The sibling casebooks are conformance demonstrations, not experimental arms:

- **LHC** demonstrates a mostly settled conclusion whose dependency chain and speculative joints remain traversable.
- **Eggs** demonstrates competing syntheses across populations, outcomes, exposures, and caveats that must not be silently averaged.

The submission will show the same source → artifact → connection → validation → review → freshness workflow on both, plus one user question per case that the resulting structure makes easier to answer. Quote verification supplies the adversarial conformance example; the provenance matrix and correlated-evidence clusters are a supporting Assessment-layer demonstration if they land without displacing the protocol or write-up.

## Does it generalize — the transfer discipline

The second thing the judges say they care about, after *would this help someone reason about this case*, is *does it generalize*. So the entry has to say how we know which parts of this layer are forced by the problem and which are our taste. That is a section, and it is the right size for one.

**Unmarked design contingency is one barrier to knowledge artifacts compounding.** Three different things can emerge from a working session looking identical on disk:

- **Forced by the world** — you cannot cite more precisely than you captured.
- **Forced by this problem** — eggs needs population, outcome, and exposure distinctions because its syntheses answer different questions; LHC does not, because it has one safety review.
- **Freely chosen** — whether the grounding-layer marker is a prose word or a frontmatter field.

All three arrive as links and headings. Without explicit rationale, history, or an independent transfer case, their surface form does not reveal which parts would survive the trip. Commonplace's practice keeps them apart by giving each a **different home and a different promotion rule**: proposals carry literal `## Forces` and `## Free choices` sections; problem-local structure stays collection-local; transferable structure must *earn* promotion by surviving a second, differently-shaped case. The framework has applied this to itself — [ADR 042](../../reference/adr/042-register-becomes-a-default-profile-under-open-ended-text-contracts.md) demoted registers from universals to *default profiles*, keeping only the declared contract and answerability as universal ([the demotion note](../../notes/a-universal-knowledge-framework-demotes-content-taxonomies-to-defaults.md)).

Three things make this a bounded design rationale rather than an unsupported universality claim:

1. **The two implementations already differ locally.** The same protocol surface supports LHC and eggs while their discourse structures remain visibly case-specific. This demonstrates applicability across the supplied cases, not universal optimality — and two cases give exactly one transfer test, which puts correspondingly more of the generalization weight on the preregistered protocol in (2). The entry says so plainly.
2. **The protocol for measuring it properly, designed and unrun.** [replication-plan.md](./replication-plan.md) is a full clean-room convergence experiment: fix the contract in advance, build the same case with independent builders who never see each other's work, and score which structures converge (forced) and which diverge (chosen) against predictions sealed beforehand. It is designed, preregistered, and **we did not have the budget to run it in six days**. We publish it as a protocol, with the predictions sealed, and say plainly that it is untested.
3. **The negative results we kept.** The source-span locator was *not* built — the discipline stopped a structure that felt necessary and wasn't. The `source_type` gap recurred three times before earning promotion ([ADR 045](../../reference/adr/045-source-genre-is-a-single-open-field-on-the-snapshot.md)). Author-authority ranking is **rejected** below, on the record.

Sized to a section, this is an asset. Sized to the spine, it would be a plan that never shipped a tool.

## Evaluation boundary

- **The deliverable is the submission document.** The code is evidence for it. Nothing else in this workshop outranks getting the document written.
- **Casework stays in the sibling repo**, per the [existing protocol](../epistack-competition_for_fable/README.md). Framework changes land here.
- **No new framework machinery that a worked case hasn't earned.** Build-local-first still holds; the deadline is not a licence to ship speculative types.
- **Doctrine constraints are inputs, not open questions:** no stored confidence/authority scalars, adjudication stays a downstream labelled layer, frontmatter semantics stay type-owned.
- **Nothing here builds the generic bulk-operations layer.** It is planned, large, and not ready. The entry reports the requirement and stops.

## Build candidates

### Extract the standalone protocol and conformance guide (the main deliverable)

The repository already implements the protocol, but its normative surface is distributed across collection contracts, type specifications, ADRs, validators, and review documentation. Extract one submission-facing specification containing: scope; required artifact and source surfaces; relationship grammar; local-extension rules; deterministic-versus-semantic verification boundary; change/freshness semantics; a conformance checklist; and one worked path through each case.

The protocol document and runnable Commonplace walkthrough are the entry. New machinery is subordinate to making those two artifacts precise, inspectable, and usable by another investigator.

Two of the brief's assessment bullets the document answers **head-on rather than by omission**, or a judge reads the doctrine as "we don't do the hard part":

- **Calibration.** Attributed, snapshot-anchored, partition-scoped judgments *are* the calibration framework; the register-drift finding is the mechanistic argument for why scalar credences in frontmatter are an anti-pattern, not a deferred feature.
- **Cruxes.** Contested joints, `contradicts` edges, and attributed positions *are* crux mapping; the entry declines crux *scoring* and says why (the same shape-unknown argument that rejects authority ranking below).

And one judging question that gets its own explicit half-page rather than being scattered: **does it scale with AI/compute.** Model partitions mean a better model opens a new partition over the same criteria instead of invalidating the archive; criterion-anchored assays simply re-run; gates are cheap-to-add criteria files; the skills layer makes the whole workflow agent-operable. The story is strong and currently under-told.

### Ship the quote verifier (DONE — 2026-07-12)

Shipped as [ADR 046](../../reference/adr/046-verbatim-quotes-are-validated-against-their-cited-source.md): `commonplace-validate` now resolves every `verbatim`-marked quotation against the source it links (a false claim **fails**), plus `commonplace-verify-quotes` for corpus sweeps. It runs as a generic body-content check alongside link health, not a type rule, because the trigger is the citation rather than the note's type.

Baseline on the two retained sibling casebooks: **40 match, 9 mismatch, 5 unresolved** across 54 candidates. The mismatches are real failures of the strict assertion — editorial omission, bracketed substitution, case changes, punctuation moved inside the quotation boundary. They are now the fix queue, not a rebuild-blocked write-off: with the rebuild off the critical path (below), **the 9 mismatches get repaired, and the repaired two-case corpus is what ships.** A submission whose citations pass its own checker is the point.

Shipping it surfaced an architectural gap worth naming in the entry. The schema already validates the note *body* — headings, links, dates — so the dividing line in validation is not frontmatter versus body. It is **dereferencing**: the schema cannot say *follow this path and look inside the artifact it names*. That makes link health and verbatim-quote resolution a distinct class of **referential** checks, whose ground truth lives in a second artifact, and which are hand-written imperative passes with no shared model, no shared severity policy, and no owner. The immediate divergence is fixed (both now share one code-fence primitive, after a fenced example was caught being scanned as a live claim), but the class still has no design. Logged to [kb-graph-loader](../kb-graph-loader/README.md), where it belongs — a referential check *is* a graph edge being resolved.

### The correlated-evidence matrix (supporting Assessment-layer demonstration)

**[assessment-machinery-line.md](./assessment-machinery-line.md).** The one assessment-layer bullet in the brief we can reach in the time, and both retained cases contain a textbook instance that is identified but unmapped. Correlated evidence takes a **different form in each case**:

- **LHC** — the whole safety case funnels through the cosmic-ray argument as a single load-bearing dependency; Ord–Hillerbrand–Sandberg is literally an out-of-model-error critique of exactly that.
- **Eggs** — industry funding (Barnard 2019).

The design move that makes this tractable: heterogeneous sources cannot be asked the same *content* questions — you cannot put a court filing and a nutrition meta-analysis on the same claim axis without manufacturing precision — but they share **uniform provenance facts**. Author, genre, data dependency, funder, citation chain, capture layer, primary/secondary standing. **Provenance is uniform even when content is not.** So the matrix's rows are sources and its axes are provenance and independence, and the correlated-evidence flag becomes a **computed cluster** rather than a prose caveat.

Build the smallest version that demonstrates the named Assessment requirement without delaying the protocol or submission. Reuse current artifacts where possible; do not build the generic bulk-operations layer. The preregistered code split is useful secondary evidence only if the retarget happens anyway.

Present the two instances as what they are. The eggs instance (shared funder across sources) is the closer fit to the correlated-evidence bullet; the LHC instance is a **single load-bearing dependency funnel**, not a multi-source cluster — real, and worth mapping, but the write-up must not sell the pair as a full independence-cluster mapping.

### Two cheap judge-facing artifacts

Both convert claims from asserted to shown at near-zero build cost; neither is new machinery.

- **The one-command adversarial demo.** The judge-facing path is: clone the casebooks, run `commonplace-verify-quotes` and `commonplace-validate`, and watch a deliberately broken citation **fail**. The full install (venv, direnv, `commonplace-init`, skills) is not "close to single click" and must not be the demo; package this short path explicitly in the submission and make it the first thing a judge can falsify themselves.
- **The hands-free transcript.** The brief wants graceful scaling toward hands-free operation; current evidence is one heavily-steering operator. Log one transcript of an agent running the source → note → validate → review loop on a single new source, unassisted, and include it. This is the cheapest possible conversion of the scaling story's weakest claim.

### Rebuild the two cases from scratch (designed, not run — published as a protocol)

**[replication-plan.md](./replication-plan.md).** This was the plan's centre of mass and it should not have been. It is an *experiment about* a tool, not a tool — it answers "does it generalize," and only indirectly, while three of the four things the judges say they care about go unaddressed by it. It also consumes the two days the write-up needs.

It comes off the critical path. It ships as a **designed-but-unrun protocol**: contract frozen, predictions sealed, clean-room conditions specified, measurement decided in advance. That is an honest and useful artifact — the brief asks entrants to "make clear where design choices are uncertain," and a preregistered protocol we did not run is a sharper statement of uncertainty than a result we could have narrated our way into.

### Author-authority ranking (rejected — and the rejection is entry material)

The [authority-ranking workshop](../authority-ranking/README.md) says the order shape itself is unknown: possibly partial, possibly domain-conditional, non-additive under independence. Six days will not settle that.

The rejection is **the discipline in the negative** and belongs in the submission as such. We decline to build a structure whose shape we have not established — exactly the restraint we are indicting other approaches for lacking. A half-built scalar rank would hand a judge the precise flattening critique this entry exists to make.

## Plan

Days are working days from 12 July; submission 19 July.

| Days | Work |
|---|---|
| 1 | **DONE.** Quote verifier shipped ([ADR 046](../../reference/adr/046-verbatim-quotes-are-validated-against-their-cited-source.md)) |
| 1–2 | **Extract the protocol.** Write the standalone normative specification, conformance checklist, and exact runnable workflow. Freeze the submission claim around the Structure layer and reference implementation |
| 1–3 | **Build the two-case demonstration.** Fix the 9 quotation mismatches, rerun validation cleanly, and produce a requirements/results table plus one navigational walkthrough per case |
| 3 | **Cheap judge-facing evidence.** Package the one-command adversarial demo (clone → verify-quotes → planted failure fails) and log one hands-free transcript of the source→note→validate→review loop on a new source |
| 2–3 | **Optional supporting assessment.** Build only the minimum correlated-evidence matrix that can run on the available case artifacts; cut it if it threatens protocol clarity or writing time ([assessment-machinery-line.md](./assessment-machinery-line.md)) |
| 4–6 | **Write and package the submission.** Lead on the protocol, demonstrate the reference implementation, answer the calibration and crux bullets head-on, include the unrun replication protocol as future evaluation, run adversarial review **and a naive-reader pass** (the judge will never open the repo, and the house style is dense), and preserve a full day of buffer |

**Priority if the days run out.** Protect, in order: the submission document; the standalone protocol and conformance guide; clean demonstrations on both cases; the quote-verification walkthrough (the one-command demo path travels with it); the hands-free transcript; then the correlated-evidence matrix. Cut the matrix first, the transcript second, before weakening the two-case protocol demonstration or losing writing/review time. Do not begin the independent-builder experiment or generic bulk-operations layer.

## Entry material we already have and should not hide

The repo's own working record is evidence, not embarrassment. The sibling repo's `backlog-to-commonplace.md` (append-only, with Outcome lines showing what earned promotion and what did not), this repo's open workshops, the `## Forces` / `## Free choices` sections in proposals, and [rejected-candidates](../epistack-framework-additions_for_fable/rejected-candidates.md) are the audit trail showing the boundary between forced and chosen being drawn in real time by people who did not yet know the answer.

Two items in particular:

- **The quote-verifier proposal admits in writing that it "did not originate from a felt friction case"** — the discipline catching its own violation on the page, before the prototype supplied the missing evidence. Do not tidy this away; it is the strongest honesty signal in the entry.
- **The register-drift experiment** — an assumption ("contradictions get silently averaged") tested and found wrong in an instructive way, with a blind judge, a declared confound, and an n=2 caveat. It promoted to [context contamination operates below an agent's compliance reasoning](../../notes/context-contamination-operates-below-an-agents-compliance-reasoning.md).

## What closes it

The submission is sent by 19 July with a protocol specification, reference-implementation walkthrough, two-case conformance evidence, and explicit limitations. Then: promote the protocol and any durable implementation conclusions into `kb/reference/` and `kb/notes/`, fold the predecessor workshops into whatever survives, and delete this directory.
