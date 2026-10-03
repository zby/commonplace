# Compare contract input costs

## Result

The split report contract is **2,249 bytes**; shortening the existing
contract produces **4,939 bytes**, against **13,727 bytes**
currently. Shortening saves **8,788 bytes** per mandatory collection read;
the split saves a further **2,690 bytes**. Shortening captures
**76.6%** of the split's collection-byte reduction.

The split's additional reduction is **3.7–9.3%** of the
shortened method-file packet, depending on role. In the saved-packet comparison
below it is **1.5–8.5%**. The smaller ownership boundary remains a
separate advantage; the coverage audit also counts 12 unrelated rule groups in
shortening versus three in the split draft. Neither has a literal zero count; these measurements do not establish better analysis.

## Measurement and provenance

See [coverage check](./contract-coverage-check.md) for clause dispositions and
[input measurements](./input-measurements.json) for paths, UTF-8 bytes and SHA-256s.
Measured against current files at the recorded input commit plus workshop drafts.
Each distinct required file is counted once per packet. No moved rule is placed
in another always-loaded worker file: shared role contracts are held unchanged.

These are file-byte costs, not tokens or observed read calls. Common root/harness
context, conditionally followed definitions, source inspection, tool results and
future retries are excluded. The collection contract is mandatory under root
writer doctrine, although current code does not supply it. Every alternative
requires repairing that delivery gap; omission is not counted as a valid saving.

The earlier **1,749-byte** split draft had scope/title/link/loading gaps. The
coverage check explains the repairs reflected in the new size. The split
existing-owner contract is **4,443 bytes**;
workers do not load it just because their method instructions live there.
Maintenance and publication drafts are coordinator/author inputs, not worker
read-first inputs.

## Per-role mandatory method reads

Sources: `AnalyseAgenticSystem` role constructors and `job` in
`src/commonplace/lib/agentic_workflow.py`. Counts include the job instruction,
worker rules, explicitly supplied shared contracts and member types. All eight
roles write collection working artifacts, including fragments, and need the
collection contract. Role-specific repair/return stages reuse these method files.

| Role | Existing role files | Current contract | Shortening | Split |
|---|---:|---:|---:|---:|
| boundary | 24,117 | 37,844 | 29,056 | 26,366 |
| runtime | 33,203 | 46,930 | 38,142 | 35,452 |
| memory | 47,993 | 61,720 | 52,932 | 50,242 |
| epistemic | 44,544 | 58,271 | 49,483 | 46,793 |
| reconcile | 67,254 | 80,981 | 72,193 | 69,503 |
| verify | 68,664 | 82,391 | 73,603 | 70,913 |
| synthesize | 37,724 | 51,451 | 42,663 | 39,973 |
| verify-synthesis | 37,314 | 51,041 | 42,253 | 39,563 |

## Saved-packet replay

Local state still retains the latest prompt for 14 job names from
`AAS-2026-10-03-dynamic-cheatsheet-02`. These include correction stages and repair
prompts with explicit `previous-output` reads. For each, count the saved prompt,
its named instruction/read-first files, named task reads and explicit repair
baseline, using their current bytes. Add each candidate collection contract.
All named files exist. This counts the complete finite file-read list found in
that saved invocation, including task material, rather than method files alone.

This is a controlled replay of declared inputs, not the exact historical worker
context: prompts can have been overwritten by retries, dependencies can reflect
later accepted outputs, and current method files differ from the run's method.
The run originally had more attempts than the 14 retained prompts. Do not sum
these rows as its historical consumption. No source checkout is read or run.
Relocated path lengths, new prompt batching and publication-specific changes to
member types are not projected; those require measurements after implementation.
Holding them constant isolates the collection-contract contribution.

| Saved job | Current contract | Shortening | Split |
|---|---:|---:|---:|
| boundary | 40,585 | 31,797 | 29,107 |
| epistemic | 93,845 | 85,057 | 82,367 |
| memory-0 | 136,025 | 127,237 | 124,547 |
| memory-1 | 157,803 | 149,015 | 146,325 |
| reconcile-0 | 175,307 | 166,519 | 163,829 |
| reconcile-1 | 184,849 | 176,061 | 173,371 |
| reconcile-2 | 186,560 | 177,772 | 175,082 |
| runtime | 56,373 | 47,585 | 44,895 |
| synthesize | 159,037 | 150,249 | 147,559 |
| synthesize-1 | 161,997 | 153,209 | 150,519 |
| verify-1 | 184,749 | 175,961 | 173,271 |
| verify-2 | 184,749 | 175,961 | 173,271 |
| verify-synthesis | 158,320 | 149,532 | 146,842 |
| verify-synthesis-1 | 159,498 | 150,710 | 148,020 |

## What is established

The coverage audit shows how shared authoring rules and removed operational
rules reach their appropriate consumers. Both candidate contracts supply explicit
conditional maintenance loading; only the shortening/split existing-owner author
needs the additional theory-account rule for ordinary authored analyses.
Analytical jobs already receive that record contract.

Shortening avoids the report/type/pin/redirect migration while obtaining most of
the measured reduction. Prefer it if that reduction meets the operator's goal.
Choose the split if the smaller per-role input and separation from unrelated rule
growth justify its migration and cross-collection method dependencies.

Neither alternative is ready to deploy by copying one file: promote maintenance
routes and add the chosen contract to job read-first/hashed inputs. The split
also needs publication/type/consumer changes and bounded migration adoption.
Publication by reference remains a separate choice, available in either layout.
A live evaluation, source-reading cost and actual quality outcomes remain outside
this authorized check.
