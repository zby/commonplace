# Integrate the cleared new-source publications

## Outcome and authority

On 2026-10-15 the operator requested integration of analyses cleared with limits,
fresh batches for failures that a rerun could plausibly fix, and then audits of
the 61 new publications. This record covers integration only. The
[prior audit closure](./unintegrated-audit-inventory.md) remains a fixed-cutoff
historical record, not a live inventory.

**32 new-source publications integrated unchanged.** The origin corpus now has
**70 retained analysis sets**. The [checklist](./systems.md) records each new
run's overview, exact-run audit and integration commit. All prior audit limits
remain limits; integration does not certify unavailable worker behavior.

Of the prior audit's 38 positive dispositions, six are older alternatives for
Dynamic Cheatsheet or Letta Code, not new-source coverage. Their existing
incumbents remain unchanged. The operator did not select a replacement among
competing positive runs. All **13 exact-run semantic holds** remain held.
Neither held outputs nor frozen methods or sources were edited.

## Integration evidence

Integration ran sequentially between **2026-10-15T07:01:11Z** and
**07:01:42Z**, starting from `b9e0e0c1148ccd909345a928106041ee11ed4a0a`.
The first publication integration is
`bb6cef032925bae0f03c5675c09336f9e5725b5f`; the last is
`26c5bf9df8ca39166fd6bdc39476689dad437cb5`.

For each run the coordinator checked its published file set and SHA-256 map
against the completed publication effect, then called its prepared
`commonplace-analysis integrate <run-id> --model openai/gpt-6.1-sol` from that
worktree with its own command prefix. Each command returned zero. The origin
was clean after each integration. No publication was installed by file copying.

All **416 files across the 32 publications** were checked against their expected
SHA-256 values in the resulting main commits and again in the current origin
files. Every corresponding checklist commit abbreviation was checked against
the recorded full commit. There were no mismatches.

The per-run machine ledger retains worktree and method identities, audit and
publication paths, complete expected hash maps, before/after main commits,
command stdout/stderr, exit status and integration disposition:

```text
/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/integration-audited-2026-10-15.json
SHA-256: 33e0d5545b5b76b6d48d6d915b0214d835ff1ae32dfffdeb48181c94720c67f0
```

Eight pinned method revisions occur in the integrated runs. Each integration
used that run's environment rather than assuming the origin's current command
version could reproduce its publication.

## Validation and limits

`commonplace-validate kb/agentic-system-analyses/retained` reported **70 sets,
zero failures and zero warnings**. It also emitted **208 source-unavailable
notices** for previously archived source checkouts. This is structural validation,
not renewed verification of quotations against absent local source bytes.
The [storage record](./worktree-storage.md) retains archive and original-path
restoration evidence; restore the relevant pinned source before claiming a fresh
quotation check for those sets. The new integrations' pinned source worktrees
were not removed.

The integration did not resume failed runs, clear semantic holds, substitute
older alternatives, launch reruns, migrate publication namespaces, rebuild
comparisons, or push. Audit authority for the next 61 publications is separate
from permission to integrate their eventual positive results.
