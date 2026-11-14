---
type: types/type-spec.md
name: improvement-run-findings
description: "The review findings one improvement run read, each cited by the review launch that produced it and given a disposition"
schema: ./improvement-run-findings.schema.yaml
---

# Improvement run findings

The `findings.md` member of an [improvement run](./improvement-run.md): one
entry per finding the run read, or one per review result that has none.

Experimental, registered on 2026-11-14 for the first run of the improvement procedure. The design and its open choices are in the [run type draft](../../work/decision-lifecycle-evidence/improvement-run-type.md); the schema is a starting point and is expected to change.

Each entry cites the launch output that holds the finding: `atom` is the
criterion, `run` the review run directory, `launch` the launch in it, and
`output-sha256` the hash of that launch's output file. The shared result
store is not cited, because a later review replaces it. `text-sha256` is
the note text the review judged and `outcome` its verdict. `finding` quotes
or paraphrases the finding. `disposition` is `fixed` with the `strategy`
used, `open` with the `item` that carries it in the answers, or `none` for a
result without a finding to act on.

## Template

````markdown
---
type: reports/types/improvement-run-findings.md
description: "{Which findings the run read and what it did with each}"
note: {note path}
start-sha256: {sha256}
findings:
  - atom: {criterion id}
    run: {review run directory}
    launch: {launch id}
    output-sha256: {sha256}
    text-sha256: {sha256}
    outcome: warn
    finding: "{the finding}"
    disposition: open
    item: "{run directory}#{id}"
---

# {Title}

{Prose.}
````
