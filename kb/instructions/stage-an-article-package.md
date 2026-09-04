---
description: "Use when a kb/articles draft is to be prepared for publication as a paper package whose every dependency is bound inside the package; runs without operator input and reports the free variables it could not bind"
type: kb/types/instruction.md
---

# Stage an article package

Make an article's paper package a conceptual closure: every term, claim, and
source the body depends on is bound inside the package or to a primary
external source, so that a reader with links disabled can evaluate every
claim and nothing the paper means is fixed only by a live KB note that may
later change.

A **free variable** is a dependency of the body whose binding lies outside
the package: a term defined only in a KB note, a claim supported only by a
linked note, a coined term nothing defines, a companion article that is not
itself frozen, or an external claim with no primary source. Staging binds
each one or reports it. The procedure never narrows or rewrites a claim to
remove a dependency; that is the operator's decision, and the closure report
is where it is requested.

## Prerequisites

- The article is at `kb/articles/{slug}.md`, declares
  `type: kb/articles/types/article.md`, and `commonplace-validate kb/articles/{slug}.md`
  reports no failures.
- `python3 scripts/article_dependency_inventory.py` exists in the checkout.
- The working tree is clean for `kb/articles/` and `kb/work/staging/{slug}/`.

## Package layout

All output goes to `kb/work/staging/{slug}/`. If the directory exists, delete
it first: a package is regenerated from the current article, never patched.

| File | Content |
|---|---|
| `README.md` | article path, source commit, staging date, closure status, file list |
| `inventory.md` | the script's inventory with the `binding` column filled |
| `{slug}-appendix-a-definitions.md` | compressed definitions |
| `{slug}-appendix-b-arguments.md` | compressed arguments for cited claims |
| `{slug}-appendix-c-protocols.md` | canonical full statement of any obligations, conditions, or test protocol the body lists; omitted when the body has none |
| `{slug}-references.md` | primary sources |
| `link-map.md` | body link → package anchor, applied at publication |
| `closure-check.md` | result of the closure tests and the list of free variables |

Appendix and reference files carry frontmatter `type: kb/articles/types/article.md`,
the article's `status` and `byline`, and a `description` naming the paper they
belong to. File names are final: publication moves them into `kb/articles/`
unchanged.

## Steps

1. **Record the source.** Create the directory. Write `README.md` with the
   article path, `git rev-parse HEAD`, and the date. Every provenance line
   below uses this commit.

2. **Inventory.** Run
   `python3 scripts/article_dependency_inventory.py kb/articles/{slug}.md > kb/work/staging/{slug}/inventory.md`.
   The inventory lists every outbound link with its target kind and carrying
   sentence, every term the body introduces in emphasis, and every KB
   definition-note title the body uses without a link.

3. **Classify each inventory row.** Fill the `binding` column with exactly
   one of `body`, `A`, `B`, `C`, `R`, `companion`, `onward`, `ordinary`, or
   `free`, by these rules in order:
   - The draft banner link and any link in a closing "where to go next"
     section: `onward`.
   - A link whose carrying sentence directs the reader elsewhere for more
     ("the fuller argument", "the companion map compares", "see") and would
     stay a complete, supported sentence with the link text read as plain
     prose: `onward`.
   - Target kind `definition-note`, or link text that is a term rather than
     a claim: `A`.
   - Target kind `source`, or an external link that attributes a claim:
     `R`.
   - Target kind `article`: `companion` if that article has
     `status: working-paper` or `status: published`, or if its own package
     is being staged in the same run; otherwise `free`, with the note
     "companion not frozen".
   - Target kind `note` or `reference` whose link text or carrying sentence
     asserts something the body relies on: `B`. If the body itself gives the
     argument in full and the link only credits it: `onward`.
   - Target kind `missing` or `workshop`: `free`.
   - An emphasized term whose carrying sentence or paragraph states what it
     means, and every bold claim label that names its own paragraph: `body`.
   - Any other emphasized term: `A`, defined from the body's usage.
   - An unlinked definition term used in the KB's sense, meaning the body
     relies on a distinction the note draws: `A`. Used in ordinary English:
     `ordinary`.
   - A claim the body asserts on its own authority, with no link, named
     source, named system, or companion behind it: `body`. It is the paper's
     claim and review judges it; staging does not demand evidence for it.

4. **Write Appendix A.** For each `A` row, in the body's order of first use:
   1. Find every occurrence of the term in the body.
   2. From the source note take the definiens and only those qualifications
      that some occurrence depends on. Omit examples unless an occurrence
      depends on one. Omit the note's scope, history, and neighbouring
      distinctions.
   3. Write one paragraph of at most 120 words under `### {Term}`.
   4. Check each occurrence: can its truth conditions be decided from the
      entry alone? If not, extend the entry, to at most 200 words. If it
      still cannot, mark the row `free` with the failing occurrence.
   5. If the body glosses the term inline in a way the entry contradicts,
      mark the row `free` with both wordings; do not choose between them.
   6. End the entry with a provenance line: `Adapted from {note path} at
      {commit}; the live note may have changed.` For a term with no source
      note: `Paper-native; defined from the body's usage.`

5. **Write Appendix B.** For each `B` row: state the claim as the body uses
   it, then the steps of the argument that claim needs and no more, at most
   250 words, citing primary sources directly where the note cites them.
   Test: the carrying sentence, with the link text read as plain prose, is
   supported by the entry. End with the same provenance line as Appendix A.

6. **Write Appendix C** when the body lists obligations, conditions, or a
   test protocol. Copy the body's list as the summary and give the canonical
   full statement under it, adding every condition the body states in prose
   elsewhere but omits from the list. The body's list is then the summary and
   the appendix the authority. Omit the file otherwise.

7. **Write References.** One entry per `R` row and per person or work the
   body names as the origin of a claim: author, title, year, and locator.
   Give the KB ingest path on a following line as provenance only. Retain
   every verbatim quotation in the body as a quoted entry with its locator.

8. **Write the link map.** One row per `A`, `B`, `C`, `R`, and `companion`
   link: the body link as written → the package file and heading anchor.
   `onward` links are listed as unchanged.

9. **Closure check.** Run all five tests and write `closure-check.md`.
   1. Inventory: every row has a binding; list the `free` rows.
   2. Links-disabled reading: run
      `python3 scripts/article_dependency_inventory.py kb/articles/{slug}.md --strip-links`
      and hand its output, the appendices, and the references to a fresh
      sub-agent with this packet: "You are an external technical reader.
      Using only this material, list (a) every term whose meaning you cannot
      fix from the material and (b) every claim the body attributes to a
      source, a named system, a companion article, or a linked note whose
      support you cannot find in the material. Do not list claims the paper
      makes on its own authority, and do not evaluate any claim. Quote the
      sentence for each item." For each item returned: if it matches a
      bound row, the entry is inadequate; fix the entry. If it matches no
      row, add it to the inventory: a term is bound `A` by step 4 from the
      body's usage, and becomes `free` only when the usage does not fix its
      meaning; an attributed claim is bound by the step 3 rules or is
      `free`. Rerun the reading once after fixes; report anything still
      returned.
   3. Placeholders: no `TODO`, `TBD`, `{`, or empty section in any package
      file; no link from an appendix or reference file into `kb/work/`.
   4. Provenance: every Appendix A and B entry ends with a provenance line
      naming the source commit.
   5. `commonplace-validate` on each package file reports no failures. The
      validator does not accept the staging directory as a target.

10. **Report.** Write the result as the first line of `closure-check.md`:
    `Closure: reached` or `Closure: not reached`. Under it, one row per free
    variable with the decision it needs: narrow the claim, write the missing
    definition note, stage the companion, supply a primary source, or resolve
    the inline gloss. Copy the status line into `README.md`. Commit the
    package directory alone, subject "Stage the {slug} package", body naming
    the source commit and the closure status.

## Scope

- Do not edit the article body. A body change that closure requires is a
  free variable for the operator; the only body edits staging prescribes are
  the link retargets in `link-map.md`, applied at publication.
- Do not stage supplements. A long companion document the paper cites is a
  `companion` row and is staged as its own package.
- Do not regenerate a package for an article whose status is `published`;
  its package is frozen with it.

## Verify

- `kb/work/staging/{slug}/` contains every file in the layout that applies,
  and nothing else.
- `inventory.md` has no empty `binding` cell.
- `closure-check.md` opens with the status line, and every `free` row in the
  inventory appears under it with a decision.
- The package is committed on its own.

## At publication

Publication of the article ([Publish an article](./publish-an-article.md))
consumes a package whose status is `Closure: reached`: it moves the appendix
and reference files into `kb/articles/`, applies `link-map.md` to the body,
and deletes the staging directory.
