# RF-17 — Gate staleness declarations overstate runtime semantics

**State:** fixed 2026-08-27
**Repair shape:** contract cleanup or feature decision  
**Severity:** low

## Finding

The review-gate contract presents `staleness:` as the policy deciding when an
accepted review becomes stale. Forty-two live gates declare the field: forty-one
use `changed`, and title/body alignment uses `rewrite(0.5)`. Runtime freshness
does not read the field; every note or criterion text change is exact-hash stale.

## Evidence

- [The former review-gate type](../../types/review-gate.md) described
  `staleness: changed | always | ...` as operative policy.
- [Title/body alignment](../../instructions/review-gates/frontmatter/title-body-alignment.md)
  formerly declared `rewrite(0.5)`.
- Registered implementation search finds staleness decisions in hash comparison,
  not gate-frontmatter consumption.

## Why it matters

This is a false system-definition affordance. Authors can believe a policy is
enforced when it is only decorative metadata.

## Provisional repair direction

For the low-cost correction, make the contract state the current exact-change
semantics and remove or normalize unsupported values. Retain an extensible field
only if a concrete second policy has an accepted consumer and tests.

## Done when

- Every admitted value has one documented runtime meaning and consumer.
- The title/body gate no longer claims an unenforced threshold.
- Validator, type contract, gate files, and selector tests agree.

## Resolution

`changed` is now the only supported gate-staleness declaration. The review-gate
schema admits only that value, catalog resolution rejects missing or different
values, and the type and review-system contracts state that it names the
system-wide exact-text rule rather than a per-gate tuning surface. The
title/body-alignment gate now declares `changed`. Regression tests cover schema
and resolver rejection of `rewrite(0.5)` and prove that a single-character note
edit stales an accepted pair under the supported policy.
