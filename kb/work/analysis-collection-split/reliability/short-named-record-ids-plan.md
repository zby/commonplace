# Short named record IDs implementation plan

## Commission

Converted on 2026-10-04 from an agent-drafted proposal, at the operator's
request. The operator decided to adopt named record IDs on the argument
below, without a trial run. This file is the commission for the executor the
operator launches on it. The launch is the authority to implement; this file
alone starts nothing.

It is separate from the [collection-split plan](../plan.md) and starts after
that plan's work is committed, because both change the record-parsing code.
It does not authorize an analysis run or the regeneration of any system.

## Intent

Analysts write exact record references when they analyse one record and fall
back to ordinary shorthand when they summarize a group. Numbered IDs invite
that shorthand: `MEM-OBJ-1 through MEM-OBJ-3` looks natural. The reference
scanner recognizes only its endpoints, so the phrase can pass while an
implied intermediate ID is undeclared. This checking gap was the recorded
reason for refusing ranges in [the earlier fix options](../../analyse-agentic-system-amendments/history/fix-options.md#a-targeted-repairs-id-grammar-unchanged).
The ban did not establish that grouping prose was analytically wrong.

Numbered IDs also carry no meaning, so every reference needs a lookup, and
a wrong number looks as valid as the right one.

Replace the numeric suffix with a short name. The purpose is threefold:

1. **Names remove numeric intervals.** Named endpoints may still describe a
   group in prose; code resolves the written IDs without expanding an interval.
2. **References carry their referent.** A reader of `MEM-OBJ-embeddings`
   does not look up a declaration to know what is meant. This lowers load
   most for reconciliation and verification, which read every member.
3. **A wrong reference is less likely and more visible.** Code can confirm
   that an ID resolves. It cannot confirm that the writer meant that record.

When a choice is not settled here, choose what keeps references exact and
identity stable, and what adds the least instruction text for workers.

## Why no trial run gates this

Named IDs have no allocated numeric interval whose intermediate references
escape checking. Named ranges remain permitted prose. Whether the grouping
supports its claim is a semantic review question, not a range-syntax refusal.
One uncontrolled run could not measure the other effects: range refusals
numbered a handful per audited run and varied between runs.
The new failure modes are mostly loud: a misspelled or
colliding name fails reference resolution and is refused. Every analysis is
about to be regenerated, so adopting before that avoids a second
regeneration or a corpus with two ID formats.

Naming reuses information already in the analysis. Components and objects
often have names in the analysed system; every record has an analyst-written
label in the heading `ID — Label`. An unidentified component can still have
a useful name drawn from its recorded role or label. The naming check below
tests whether these sources yield short, stable handles.

The evidence for the diagnosis is in the audits: the
[first Dynamic Cheatsheet audit](../../analyse-agentic-system-amendments/history/fresh-run-audit.md)
records three verification submissions refused for ranges and five ranges an
analyst repaired locally, with ranges appearing in coverage statements,
inventory summaries and grouped support. The
[second audit](../../analyse-agentic-system-amendments/history/second-run-audit.md)
records none in verification after local guidance, and ranges still written
in reconciliation, synthesis and the epistemic job. The first audit also
records a range-detector false positive on ordinary `to` relation prose,
which was subsequently corrected. These audits show syntax refusals and
repair costs; they do not show that every group reference was a faulty
analytical claim. Adopting names is a design argument, not an observed
reliability improvement.

## End state

- A record ID is `<analyst prefix>-<kind>-<name>`, for example
  `RT-OBJ-sheet`, `MEM-OBJ-embeddings`, `EPI-RTE-answer-scoring`. These are
  illustrations of the grammar, not declarations or a renaming map.
- Code accepts named IDs in declarations, annotations, references, part
  relations, amendments, supersessions and profile citations, and refuses
  numeric record suffixes in new members.
- The method's contracts, types, job instructions, templates and examples
  state the naming rules once and use named IDs throughout.
- Instruction text that existed only to prevent record ranges is removed or
  reduced to what `SRC-*` IDs still need.
- An unresolved reference is refused. A nearest-declared-ID hint is optional,
  as prioritized below.
- Frozen sets under `kb/agentic-systems/reports/` are byte for byte unchanged.
- Required tests and validation pass. A result record states what was done
  and what remains, and a decision record carries the revisit condition.

The first analysis run under named IDs is the outcome check. It needs its own
commission.

## The identity contract

**Grammar.** The name is one to three lowercase words joined by hyphens.
Each word starts with a letter and may contain digits. A word made only of
digits is refused, so no name can end in an allocated number. The analyst and
kind prefixes stay as they are.

**Where the name comes from.**

- *Components and operative objects* with an available source-native name
  take the analysed system's own name for the thing: a class, module, file, prompt, store or field. The system
  already solved that naming problem, and parallel analysts who name the same
  object from the same source will tend to converge, which makes a duplicate
  identity visible. Convert the source name by one rule: drop a file
  extension, split at case changes, underscores, dots and other separators,
  lowercase the words and join them with hyphens. A fragment made only of
  digits joins the word before it. `DynamicCheatsheet` gives
  `dynamic-cheatsheet`; `top_k_examples.py` gives `top-k-examples`; `GPT-4`
  gives `gpt4`. When the result has more than three words, keep the three
  that best distinguish the object.
- *Routes, claims, evidenced absences and behavioral-authority paths* are the
  analyst's constructs and have no source name. They take two or three words
  from the record's own label.
- *Generic or repeated source names*, such as `utils` or `client`, and one
  source object split into several records, take a qualifier from the source
  path or from the part's role. Never disambiguate with an allocated number.

When a component or object has no available source-native name, the analyst
chooses its name. Possible starting points are its recorded role, a related
input or a short form of its label. For example, the first retained set's
`RT-CMP-2` has an unknown embedding-producer identity; `embedding-producer`
is one possible handle. These are suggestions, not a prescribed fallback
or additional naming constraint.

**Stability.** The ID is a handle, not a description. It stays fixed when the
label, the findings or the assessment change, including across correction
rounds. Do not encode a conclusion, such as `validated-knowledge`, in an ID.
No step renames an ID, and reconciliation allocates none; both rules exist
today and stay.

**References.** Every written ID repeats the full declared ID. No aliases or
shortened prefixes. Named endpoints may describe a group, such as
`MEM-OBJ-sheet through MEM-OBJ-embeddings`; code resolves the written IDs
without inferring intervening members. `through`, dash ranges and ordinary
`to` relations between named endpoints are accepted in prose. Existing
single-ID fields and structured citation lists keep their contracts.
IDs are unique across the set. A
different prefix or name does not prove a different referent; identity
comparison remains the analysts' and reconciliation's work.

**Unambiguous tokens.** Code reads the longest hyphenated token as the
reference and resolves it whole. A word attached to an ID in prose, such as
`MEM-OBJ-sheet-based`, therefore fails resolution and is refused. One case
would resolve silently to the wrong record: a declared ID that equals
another declared ID plus a further word, such as `MEM-OBJ-sheet-cache`
beside `MEM-OBJ-sheet`. Code refuses that pair when the member is accepted,
before any other member cites it. The analyst prefix makes this a check
within one member. The refusal message states the rule; the worker contract
does not carry it.

**Source-register IDs.** `SRC-*` IDs stay numbered. Source ranges remain a
known error class and keep their check and guidance. Report them separately;
named record IDs do not address them.

## Boundaries

- **Analytical content is unchanged.** This changes how a record is named,
  not what counts as a record, as evidence, or who may amend what.
- **Naming stays with the analyst.** Choosing a name needs judgment. Code
  checks grammar, uniqueness, the token rule and reference resolution. It
  does not generate names. This is why the change is not part of
  the [code checks proposal](./remaining-code-checks-proposal.md).
- **No migration and no compatibility layer.** Frozen sets keep their
  numeric IDs and are not read as current sets. Do not build a rename tool or
  a reader for both formats without a demonstrated consumer.
- **Bounded growth of worker input.** The record-range guidance to remove
  is about four lines, and part of it stays for `SRC-*`, so the naming rules
  cannot fit in the space freed. State them once, in the shared record
  contract, and nowhere else. That contract may grow by at most about 700
  bytes net. No job instruction, worker-rules file or member type grows in
  net. Rules that code enforces with a self-explaining refusal, such as the
  token check, stay out of worker text. Measure the affected files before
  and after.
- **Coordinate with the collection-split work.** Start from its committed
  state. If its executor is still changing record code, wait or agree the
  order with the operator.
- **Repository rules apply**, as in the collection-split plan.

## Priorities and partial results

The naming check comes first, because it can end the work before anything is
built. Then the grammar and reference handling in code, with their tests:
without them nothing else can be checked. Then the shared record contract and
templates. Then the job instructions and the removal of range guidance. The
nearest-ID hint is last and can be left out.

If work stops early, leave required checks passing and the method internally
consistent: code and contracts must agree on one ID format. Record what
remains. A state where code accepts names and the contracts still teach
numbers is not acceptable.

## Supported route

One workable route. Take another if it reaches the end state inside the
boundaries, and say what you changed.

1. **Fixed: naming check before mutation.** Name every record of both
   retained Dynamic Cheatsheet sets under the identity contract, reading the
   frozen sets only. Use cited source-native names where available and the
   naming suggestions above where useful. Record the names and counts that
   needed a qualifier, dropped words from a longer source name, or used a
   name without an available source-native name. This is the
   cheapest test of the contract, so it runs before any code changes. A
   search on 2026-10-04 found 20 declarations in the newer set, 8 with
   labels of four or five words.
2. **Fixed: inventory before mutation.** Numeric patterns occur in the
   record grammar and range detection in `agentic_records.py`, in route and
   absence recognition there, in the shared record contract, member types and
   their templates, job instructions, schemas, the profile's record
   citations, the matrix reader and about 160 occurrences across the tests.
   Found by search on 2026-10-04; redo it. A missed pattern silently stops
   recognizing records.
3. Change the grammar and its fixtures. Cover named IDs, multiword names,
   duplicates, the token rule, digit-only words, misspellings, annotations,
   part relations, amendments, supersessions, profile citations, and source
   quotations staying outside identifier checks. Recognize whole candidate
   tokens before validating grammar, so malformed IDs are refused rather
   than silently omitted from the scan. Cover numeric suffixes, uppercase
   names and names exceeding the chosen word limit in declarations and prose.
   Confirm that named `through`, dash and `to` prose is accepted when its
   written IDs resolve; an undeclared endpoint still fails. Confirm that
   `SRC-*` range handling is unchanged.
4. Rewrite the identity section of the shared record contract with the
   contract above. Update types, templates and examples.
5. Update job instructions. Remove range guidance that named IDs make
   unnecessary; keep what `SRC-*` needs.
6. Add the nearest-declared-ID hint to the unresolved-reference refusal.
7. Re-measure, verify, write the decision record and the result record.

## Left to the executor

The exact regular expressions; the word limit, if three proves wrong against
real labels; further separators the conversion rule must split at, if real
source names show them; wording of the contract; how the nearest ID is chosen; test
structure; commit granularity.

## Return to the operator

Stop and ask when:

- records of some kind cannot be given clear, stable names within the chosen
  grammar, judged against the retained records; absence of a source-native
  name alone is not a stop condition;
- the token rule cannot be enforced without refusing ordinary prose;
- a consumer needs numeric and named IDs at once;
- the change would touch frozen sets or alter an analytical definition;
- the shared record contract would grow by more than the bound, or any
  other worker file would grow in net.

Otherwise proceed without asking.

## Verification

- `uv run pytest -q` and `uv run ruff check .` pass.
- Targeted `commonplace-validate` passes for the changed contracts, types and
  instructions.
- A fixture set built with named IDs passes set validation end to end,
  including the profile member's record citations.
- The naming check of step 1 is in the result record, with its names and
  counts. The frozen sets it read are unchanged.
- Bytes of the shared record contract and of each affected role file before
  and after, against the bound.

Fixtures show parser behavior. They do not show that analysts name well or
make fewer reference errors.

## Revisit condition

Carry this into the decision record with a literal `TODO` marker, as the
collection-split decision does.

**TODO: revisit named record IDs** after the first few analyses under them,
or earlier if one of these is observed:

- a group phrase or named range that leaves membership too vague for the
  claim being made;
- repeated refusals for misspelled or unresolved names;
- attempts to rename an ID after an interpretation changed, or IDs that
  encode a conclusion;
- names that made two different records look the same, or hid a duplicate;
- naming rules growing in the worker's input.

Count source-ID range refusals, unresolved or altered references, collisions,
and within-job repairs and retries separately. Record any semantic grouping
faults separately from syntax refusals; permitted named ranges are not errors
merely because they use `through` or a dash. The
alternative to weigh is numeric IDs with role-local range guidance and the
existing checks.
