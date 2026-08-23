# What these descriptions spare here

Local application. The general model — that human recompute is dear and rare
while agent recompute is cheap and constant, so audience segmentation turns on
magnitudes rather than principle — lives in
[the note](../../notes/human-recompute-is-dear-and-rare-agent-recompute-is-cheap-and-constant.md).
This file supplies Commonplace's magnitudes and the disposition that follows
from them. It does not re-derive the model.

## The magnitudes

| Subject | Source | Doc | Compression |
|---|---:|---:|---:|
| `src/commonplace/lib` | 160 KB, 20 files | `lib-modules.md` 21 KB | 7.6x |
| `src/commonplace/review` | 153 KB, 24 files | `review-architecture.md` 14 KB | 11.1x |
| `src/commonplace/freshness` | 40 KB, 11 files | `freshness-architecture.md` 6 KB | 6.7x |
| `src/commonplace/freshness` | 40 KB | `freshness-schemas.md` 3 KB | 13.3x |

Whole package: about 460 KB across 85 modules, averaging roughly 5 KB. Reader
turnover on the human side is close to zero — one long-tenured maintainer, plus
infrequent outside readers. On the agent side it is unbounded: every session is
a new reader.

## Correcting an earlier argument in this workshop

An earlier version of this file argued that reading `lib-modules.md` at 21 KB
costs more than reading the 15 KB module it describes, so the doc loses on
tokens alone. That comparison was unfair: an agent can read just the doc's
section on the module it cares about, perhaps 2 KB, and on that basis the doc
wins comfortably.

The argument that survives is about sufficiency, not size. **A summary is
enough only for questions where approximate knowledge suffices.** For anything
requiring accuracy — changing the code, debugging it, checking a signature —
the source read happens regardless, and the doc read is additive cost rather
than a substitute. The questions a summary genuinely closes are orientation
questions: which module owns this, where should I look. That is routing.

## Selective doc reading against selective source reading

The sufficiency argument above still understated the case, because it compared
a doc *section* against a whole source file. Agents read source selectively
too — grep a symbol, read one function — so the fair comparison is selective
against selective.

Measured on `type_resolver`:

| | bytes | authoritative? |
|---|---:|---|
| `lib-modules.md` section on the module | 3,657 | no |
| the module itself | 15,052 | yes |
| median function in it | 773 | yes |

Answering a symbol-level question — what does `validate_type_eligibility` do —
costs about 3,657 bytes from the doc, because its section is the smallest unit
the prose offers, and yields an approximate answer. From source it costs a grep
plus 1,530 bytes, and yields the truth. **Selective source reading is both
cheaper and correct.**

### The mechanism is addressability, not size

Source is addressable at symbol granularity: a name is a search key, so the
reader can select exactly the function it needs. Prose is addressable only at
heading granularity, so the smallest selectable unit is a section covering a
whole module.

The source therefore supports finer selection than the document does, and the
advantage grows as the question gets more specific. This is why the compression
ratios above are misleading: they compare whole artifacts, but neither reader
consumes whole artifacts, and the two are not selectable at the same grain.

### What follows

A summary earns its place exactly where **the content has no locus in the
source that a search could find**. An invariant spanning four modules has no
symbol. A layering rule has no symbol. A protocol ordering has no symbol. That
is the sharper reason such content is irrecoverable — not merely that it spans
files, but that nothing in the files is the thing to look for.

The operational test is one question: *what would I grep for?* If there is an
answer, read the source. If there is not, that is the content worth authoring.

## What the products come to here

**Per-module description.** Agent value is near zero: the questions it closes
are routing questions, and routing is already available more cheaply. Human
value is also near zero, because the resident reader has long since paid the
recompute and retains it. Two low products, and a maintenance term paid on
every commit that touches the code.

**Routing.** High value per token for agents, and the cheapest layer in the
system. Already present twice over: `lib-modules.md` opens with a nine-line
module map, and 83 of 85 modules carry a docstring saying nearly the same thing
in nearly the same words. `lib/` is 20 of 20.

**Within-file navigation.** Already in the files. `validation.py` carries 31
comment blocks, several citing the ADR whose decision the code implements.

**Cross-module invariants.** Recompute cost is not merely high but unbounded,
because the content is not recoverable from the source at any price — see the
correction below. Both products are therefore high, and this is the layer worth
authoring.

## Disposition

Follows from the model plus the two local magnitudes: sources are small, and
human reader turnover is near zero.

| Layer | Disposition |
|---|---|
| Per-module description | Drop |
| Module routing map | Generate from docstrings, or drop as redundant with them |
| Within-file navigation | Nothing to do |
| Import and call structure | Do not author; mechanically recoverable |
| Cross-module invariants, layering, protocol | Keep and author well |
| Orientation for first contact | Already scoped: README, `kb/index.md`, collection landings, `kb/articles/` |

The disposition depends on those magnitudes and does not transfer. A project
with large modules, or with reader turnover on the human side, would land
differently under the same model.

## Promotion candidates

Two claims here look general rather than local, and neither is in the note:

- **Addressability sets the granularity of selective reading, and source is
  finer-grained than prose about it.** A symbol is a search key; a prose
  section is the smallest unit a document offers. So selective source reading
  beats selective doc reading on cost and on correctness, and the margin grows
  with question specificity. This looks like the strongest candidate here.
- A summary earns its place exactly where the content has no locus in the
  source a search could find — the operational test being "what would I grep
  for?"
- A summary substitutes for source only on questions where approximate
  knowledge suffices; for accuracy-requiring questions it is additive cost.
- Relations split into mechanically recoverable structure and irrecoverable
  invariants, and only the second is worth authoring.

## Open

- Does the routing map need authoring at all, or is a generated-and-checked
  map from docstrings strictly better?
- What is the size threshold where a summary starts to pay for an
  accuracy-requiring question? `validation.py` at 38 KB may be above it.
- Does the same split apply to `commands.md`, where the unit is a CLI surface
  and `--help` already exists?

---

# Correction: relations are not a human-only need

Added 2026-08-23, after the objection that agents need cross-module
documentation too. The objection holds, and the earlier split was wrong.

## Why "read the source" does not reach relations

Reading `type_resolver.py` tells an agent what that module does. It does not
tell it that collection discovery in `project_paths.py` determines which type
specs are in scope, or that `validation.py` depends on the resolution order.
Relations live between files, so recovering them means reading several and
inferring — the expensive case, not the cheap one.

The change loop needs them most: what breaks if this signature moves, which
subsystem owns this concern, what invariant am I about to violate. That is the
question an agent cannot answer from the file in front of it.

## But relations split into two kinds, and only one is worth authoring

**Mechanically recoverable.** Imports, call structure, which module references
which. A `grep` over import statements reconstructs the static dependency graph
cheaply and authoritatively. Authoring this is the same duplication as the
routing map.

**Not recoverable.** Invariants that span modules, layering rules ("this may
import that, never the reverse"), protocol and sequencing facts, and why a
boundary sits where it does. `review-architecture.md`'s canonical-state versus
derived-output distinction and its finalization invariants are this kind. No
amount of reading the files yields the rule, because the rule is what the files
were written to satisfy — it is the generator content, sitting inside artifacts
this workshop had classified as cache.

## Revised disposition

| Layer | Recoverable? | Disposition |
|---|---|---|
| Per-module description | Yes — docstrings say nearly the same words | Drop |
| Module routing map | Yes — derivable from docstrings | Generate or drop |
| Within-file navigation | Already in-file | Nothing to do; `validation.py` carries 31 comment blocks, several citing ADRs |
| Import/call structure | Yes — mechanically | Do not author |
| Cross-module invariants, layering, protocol | **No** | **Keep and author well; needed by agents and humans alike** |
| Orientation narrative | No | Keep; overlaps heavily with the row above |

The earlier framing had the last two rows as a human concession. They are the
load-bearing content for both readers, and they are the part currently diluted
by the four rows above them.

## What this does to the tax argument

The tax was never on the valuable layer. Cross-module invariants change at
architecture speed, not commit speed. What is being co-maintained on every
commit is the per-module detail that duplicates docstrings — so removing it
takes the tax to near zero without touching anything a reader needs.

## Side evidence for the parked ADR workshop

`validation.py`'s comments cite ADR 026 at the site the decision constrains.
That is the "enforced decision needs no consultation" pattern already happening
in practice, unprompted. Worth sampling more broadly when that workshop resumes:
the routable ADR residue may be smaller than assumed.
