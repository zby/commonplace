# Admission to the main record: a bounded design-space map

## Purpose and status

Understand what particular retention commitments buy and oblige us to do, so
we can choose reasonably for concrete work and reconsider the choice later.
This is a preliminary map, not an optimal policy, an exhaustive enumeration or
a measured cost model. The [workshop framing](./README.md) fixes the commission
and completion conditions.

Here, the **main record** is the deliberately retained Git-backed project record:
versioned files and commit messages. Current files and Git history are not
independent stores. Untracked material can remain useful for some time; tracked
material need not remain in the current tree forever.

## Binding investigation boundaries

The [framing's fixed boundaries](./README.md#fixed-boundaries) govern every option
below. Harness traces are trusted as complete and temporarily available; their
rules are not ours to change. We do not build duplicate primary process records.
Additional caches must justify the extraction work they save. Retained artifacts
must serve their intended uses after trace deletion, although they can depend on
other durably retained material. These are working premises, not findings this
map must establish.

## The economic question

> What additional value would admitting this material to the main record provide,
> compared with using the trace, keeping a working copy, recreating a useful
> product, or retaining only the contribution its use produces?

Three corrections from the operator govern this comparison:

- **Possible usefulness does not distinguish what to retain.** Almost anything
  might help a future debugging investigation. Naming that possibility does not
  justify a second record when the trace already contains the information.
- **Duration alone is insufficient.** Low-value material can remain potentially
  useful for years without earning Git admission. High-value lasting use can
  justify a retained artifact rather than an indefinitely maintained cache.
- **Use can consume an intermediate's value.** A report may earn its production
  cost by helping produce a committed result, without earning separate retention.
  Assess its remaining uses after that contribution has been incorporated.

Conversely, incorporation does not prove that every important use is covered.
The result may omit a rejected alternative, original expectation, constraint or
reason. Ask whether that information warrants durable extraction, not whether
one can imagine any use for it. A rare but consequential use can justify
retention; frequency alone is not the test.

## Commitments and consequences

Rows describe choices that can be combined, not exclusive boxes into which every
file must fit. Their value depends on the particular use and available access
routes.

| Commitment | Potential benefit | Cost, obligation or accepted loss | Interaction and reversibility |
|---|---|---|---|
| Leave the information only in the trace | No additional recording or curation work | Later discovery and extraction; accept loss of the recovery option when the harness deletes it | Extraction remains possible while the trace exists; deletion can make the decision irreversible |
| Keep a working file or cache | Avoid repeated extraction; provide a directly usable product | Preparation, checking, finding the cache, staleness and disposal | No duty of trace-independent durability by default; promotion later may require more than copying the file |
| Incorporate the contribution into a maintained artifact | Preserve the useful result without a separate intermediate | Determine which remaining uses the result does not support | The intermediate can still be recovered from the trace during its availability; its final contribution need not preserve all reasoning |
| Retain a selected account in Git | Durable, clearer or cheaper access to worthwhile knowledge | Extraction and checking; enough retained context and evidence to support the intended use without traces | Selection can omit material needed by a later, different use; some losses become irreversible after trace deletion |
| Retain the whole intermediate as a bounded artifact | Preserve detail and reduce selective extraction | Explain its purpose, status and context; pay discovery and interpretation costs | It still must be useful without the trace; keeping an intermediate is not permission for a parallel exhaustive process archive |
| Retain an account in a commit message or only in history | Associate it with change or preserve it without a permanent current file | A usable route to the right commit, references and later updates | Depends on retained history; squashing may preserve the final tree but lose the needed account |
| Recreate a product when needed | Avoid carrying a separate product between uses | New production and checking cost; changed models, methods or sources may yield another answer | Appropriate when a useful replacement suffices, not when the exact historical result is needed |

A cache can remain dependent on the trace if that fits its declared function.
A retained artifact cannot leave an indispensable reason or observation solely
behind a trace link. Promotion therefore creates an information obligation,
not just a path or Git-status change. Optional trace provenance can remain.

Keeping the whole intermediate and retaining a selected account are both
legitimate candidates. Neither completeness nor brevity is automatically
cheaper for the intended reader.

## When to extract is a separate choice

| Commitment | What it offers | What it costs or risks |
|---|---|---|
| Extract when a concrete need appears | Avoid processing material nobody uses | Expensive or delayed recovery; the trace may already have expired |
| Prepare selected auxiliary information during work | Use available context to reduce later extraction effort | Adds work before future demand is known; must not turn into mandatory duplicate session accounts |
| Mine selected traces proactively | Recover potentially valuable information before deletion or before a reader knows to ask | Selection, processing and checking costs, including runs that yield nothing worth retaining |
| Mine routinely across a broad class of sessions | More systematic opportunity to find useful material | Recurring cost and weak-signal volume; requires a sufficiently valuable use and a proportionate selection method |

Routine mining is not entailed by durable retention, and mining need not produce
a cache before producing a retained artifact. No mining schedule or programme
is selected. Different tasks may warrant different timing.

## What belongs in the comparison

### Intended use and additional value

Name the consumer and future operation: ordinary reading, implementation,
revision, debugging, audit or reconsideration. Ask what additional Git admission
supplies over the trace and available working copy: cheaper access, clearer
interpretation, portability, direct use, a stable reference or longer retention.
A committed file nobody can find may add little. A well-indexed trace may suffice
for one use while a selected account materially improves another.

### Costs under our control

Take harness capture and deletion rules as given. Count the costs of extraction,
checking, description, storage and transfer; discovery, reading and reconstruction;
maintenance, references and cleanup; regeneration and failed recovery; and
misleading duplicates or stale accounts. Respect privacy, licensing and access
restrictions when extracting into a more widely available record.

Do not charge every cost to every option. A historical record need not be
maintained like a current instruction. Material only in history need not clutter
ordinary file search. Traces are not free to search just because capture already
happens. Production cost already incurred is not itself a reason to retain an
output; the prospective cost of producing a needed replacement can matter.

### What may be lost

Recovery from a trace and regeneration are different. A new model run may not
reproduce an old candidate. Current access to an external source may not recover
a prior observation. Establish whether the intended use needs historical evidence,
a functionally equivalent product or a current answer.

Selection can lose expectations, contrary outcomes or consequential operator
contributions. Preserve these when the retained use requires them. Do not replace
contemporaneous evidence with a retrospective explanation presented as the
original reason. Equally, do not preserve everything merely to avoid specifying
the retained artifact's intended use.

### Authority and status

Producing, applying and retaining a result need not have the same authority.
A rejected candidate can earn retention as evidence; an adopted edit can leave
its intermediates outside Git. A commitment to retention must make the artifact's
status intelligible, not imply truth, adoption, implementation or observed benefit
merely from its presence. Authority can be granted conditionally in advance; the
map does not introduce a fresh human gate for every operation.

### Decision cost and uncertainty

Per-item deliberation can cost more than it saves. Narrow class-level defaults
may reduce that cost, but need reasons and exceptions rather than hypothetical
future-use arguments for every file. Repeated expensive reconstruction, unused
retained outputs or investigations blocked after expiry can motivate revision.
Collecting such evidence also costs work; no telemetry system is implied.

Use qualitative judgments when evidence does not support estimates. State
consequential uncertainty and acceptable losses. A reasonable local choice does
not need to dominate every plausible alternative or generalize to every workflow.

## Concrete starting cases

| Case | Choice to examine | Boundary on the conclusion |
|---|---|---|
| Connect report after link authoring | Keep as cache, extract an independently useful finding, or leave the process account in its trace | Authored links may consume the report's primary value; that does not settle every later research use |
| Revision candidate after publication | Whether the candidate/report/diff has an independent retained use beyond the final text and trace | Inspection and publication roles do not alone justify Git retention afterward |
| Ingest candidate during the refactoring | What, if anything, to retain beyond the tracked ingest and trace | Candidate checking and guarded replacement do not decide retention of intermediate material |
| Decision worth reconsidering later | What account must survive, then which existing file or Git route serves it | See the [carrier comparison](./git-and-retained-artifacts.md); equivalent content is required for a fair comparison |

These are unexecuted design comparisons, not observed optimal arrangements.
Agentic-system analysis remains outside the starting set because its worktree
and automatic merge have a different integration model.

## How much resolution is enough?

For a selected case, record the use, plausible alternatives, consequential
benefits and obligations, assumptions, reversibility and remaining uncertainty.
A justified provisional choice—or keeping the current arrangement—is enough
when further investigation is not worth its expected decision value. State what
would warrant reopening it.

The open work is to apply this map to real choices, not expand it indefinitely.
Before any new experiment, identify a consequential question that ordinary-use
evidence or mechanism inspection cannot settle. General retention policy remains
coordinated with the lineage-mechanisms workshop; no policy or implementation is
adopted by this map.
