# Simplifications beyond mechanical offloading

- **Recorded:** 2026-09-29, at the operator's request after a discussion of the last two commits and similar possible simplifications.
- **Status:** agent proposals awaiting selection. Recording these does not commission implementation or extend the workshop's closure requirements.
- **Evidence boundary:** read-only inspection of commits `cb301b015fc392e097beec248e8aa49b1630c5b2` and `fd64693691fbc775b601f9f793449d1940493c99`, the skill, job instructions, report contracts, workflow code, and this workshop. The working tree was actively changing. Implementation observations below describe that inspection, not a completed audit of the eventual implementation.

## Direction

Remove decisions whose alternatives have no useful effect on the analysis, especially when later steps must reconcile those decisions. Moving a mechanism into code can make it cheaper and more reliable; changing the contract can make the mechanism unnecessary.

The two motivating commits illustrate this:

- `cb301b0`, “Name analysis runs after the source's repository,” derives the run slug from the source identity instead of the analyst's chosen system name.
- `fd64693`, “Propose lens-prefixed canonical record IDs,” records the proposal to keep specialist IDs canonical. The [proposal](../../reference/proposals/lens-prefixed-canonical-record-ids.md) describes a real run that failed during translation into a second namespace.

At inspection, the working tree was implementing the latter, including unchanged specialist members and amendments in the overview. Those changes are existing work, not new candidates here.

## Design space and required result

Working statement of the required result: produce a source-grounded account of one frozen target, inspect it through the runtime, memory, and epistemic perspectives, resolve their interactions, independently check the result, and publish an attributable, bounded conclusion.

| Dimension | Choices the design admits | What the result needs |
|---|---|---|
| Target and evidence | Whole system or mechanism; repository or capture | Keep these: they change what can be established |
| Identity | Independently chosen names and paths, or derived identities | One stable source identity; derive operational names |
| Analysis topology | Optional lenses, variable workers, fixed passes | Runtime plus both lenses; separate verification |
| Inspection depth | Preset modes or depth justified by findings | Enough inspection to support conclusions and exclusions |
| Record ownership | Proposals, central registration, distributed declarations | Each finding declared once by its author; stable references |
| Integration | Rewrite members, append amendments, preserve disagreements | An explicit account of the set's final conclusions |
| Correction | Specialist-specific negotiation or one bounded correction policy | Correct unsupported claims; preserve justified uncertainty |
| Publication | Independently composed summary or deterministic projection | A compact, faithful public account |
| Execution provenance | Worker-managed handoffs or workflow-managed records | Verifiable inputs, method, outputs, and completion |

Most removable flexibility appears in identity, handoffs, representation, and publication. Much of the necessary flexibility is in evidence and interpretation.

## Candidates

### 1. Write the public synthesis once

The overview's [Bounded synthesis contract](../../types/agentic-system-analysis-overview.md#bounded-synthesis) and the [review job](../../instructions/analyse-agentic-system/jobs/review.md) substantially overlap: both explain the system's operation, discriminating mechanisms, findings, and limits.

Make the overview contain a compact synthesis suitable for publication. Code renders that text, its description, evidence basis, and links into the public review. Verification then covers the actual published prose.

This removes a job and the opportunity for a second writer to strengthen, omit, or distort an already verified conclusion. It revisits backlog item 5 by changing the prose contract, making the body derivable rather than merely generating its frontmatter.

**Condition:** accept one account serving both purposes. If the public review needs a genuinely different audience or length, separate writing earns its place. Compare the two output needs before selecting this change.

### 2. Remove the separate scoping job

The [scoping job](../../instructions/analyse-agentic-system/jobs/scoping.md) chooses `brief` or `full`, but both lenses always run. It adds a serial handoff before specialists inspect their subject.

Let each lens state its inspected scope, trigger evidence, exclusions, and limitations in its own report. Give both the frozen boundary and runtime findings. Reconciliation checks whether the resulting coverage is adequate.

Consider dropping the `brief/full` distinction too: require relevant mechanisms to be addressed, with concise explanations where evidence is thin. Keep the scope record. This gives specialists responsibility for the scope they can defend.

**Tradeoff:** less advance control over effort. If an inspection budget is required, specify it separately. Selection should check that specialist-owned scope will not hide omissions that the separate job currently catches.

### 3. Make memory an ordinary workflow job

The [memory instructions](../../instructions/analyse-agent-memory.md) describe a private handoff protocol: a dedicated input bundle, manual input and method hashes, completion notifications, and a returned path/hash/status summary. The workflow already tracks declared inputs and accepted output hashes.

Use the same input and completion contract for memory and epistemic workers. Remove manual notification and hashing duties where code supplies the guarantee. If provenance must survive outside operational state, code should export it into the retained set. Keep the specialized memory analysis and comparison fields.

**Condition:** inventory the guarantees before deleting protocol. Ensure all method and evidence inputs are declared and required provenance survives retention. This revisits item 12's memory-specific input assembly and overlaps the separate method follow-up's separation of content from execution accounting; coordinate ownership before implementation.

### 4. Use one correction policy across the set

At inspection, the workflow distinguished returns to the memory specialist from verification blockers and maintained separate memory and reconciliation counters. Reconsider whether this asymmetry still serves a purpose after the canonical-ID change.

A simpler policy could be:

1. Reconciliation resolves cross-member interpretation through amendments.
2. Missing evidence or necessary analysis returns to the responsible author.
3. Independent verification checks the assembled result.
4. One shared bound limits correction rounds.

Fix the three possible author destinations rather than building a configurable repair framework. The shared round bound already exists; the proposed reduction concerns correction routing and specialist-specific handling.

**Condition:** immutable initial reports need understandable amendments and a way to supply missing evidence. Revisit this after the current implementation completes a run; inspect actual correction needs before choosing which routes to retain.

### 5. Give workflow decisions one explicit representation

At inspection, a heading signalled “return to specialist,” and prose under `Blockers` was compared with `none` to decide whether to continue.

Require small structured fields for these decisions, such as a correction list and a blocker list, and derive narrative headings from them. Keep explanations as prose. Apply this only to fields code consumes.

This removes the freedom to express the same operational decision in different textual forms and prevents report formatting from accidentally selecting a workflow branch.

**Condition:** the structured fields must be authoritative; do not add a second independently authored representation of the decision. This is a narrow contract change, not a proposal to structure every analytical paragraph.

### 6. Normalize source identity once, before deriving paths

The filename commit fixes variation in system names. A URL's last segment still leaves ambiguity: different owners can have repositories with the same name, and different URL forms can identify the same repository.

For recognized repository inputs, derive a normalized identity once and use it throughout opening, boundary records, and publication. Keep the human-readable system name as a label.

Removing `review-path` is a possible follow-on, but first decide whether multiple analysed boundaries within one repository need distinct public reviews. That is a requirement question that filenames alone cannot settle. Preserve a workable identity contract for non-repository inputs.

## More aggressive cuts to defer

| Candidate | Simplification | Capability surrendered |
|---|---|---|
| Static analysis only | Remove dynamic probes and their execution preflight from the ordinary workflow | Direct observations of execution; claims must remain bounded accordingly |
| Failure receipt only | Retain a short receipt for blocked/out-of-scope targets instead of assembling an overview-only set | Uniform artifact shape across successful and unsuccessful runs |
| One source bundle per run | Prepare heterogeneous evidence before opening analysis | Convenient evidence acquisition during boundary work |

These narrow the product's capabilities. Defer them until the surrendered capabilities are shown to be unnecessary. The first would also supersede the workshop's proposed probe runner rather than add another implementation item.

## Preserve and evaluate

Preserve independent verification, frozen evidence, the distinction between uncertainty and absence, both analytical lenses, and publication consistency checks. Their complexity protects meaningful properties.

Suggested consideration order: one authored synthesis, ordinary memory job protocol, then lens-owned scoping. Reconsider correction routing after the current implementation completes a run. This is an agent recommendation, not an adopted build order.

For each candidate, state which decision, handoff, representation, or failure mode disappears, and which useful result becomes impossible. Before implementation, recheck the live contracts and use the workshop's existing design-proposal requirement for shipped-contract changes. Any evaluation must retain the workshop's stated boundary: a bundled method rerun cannot isolate the effect of each individual change.

Related reasoning: [Constraining and extraction can trade generality for reliability, speed, or cost](../../notes/constraining-and-extraction-both-trade-generality-for-reliability.md) and [Progressive constraining commits only after patterns stabilize](../../notes/progressive-constraining-commits-only-after-patterns-stabilize.md).
