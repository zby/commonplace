# Commit / wait / probe behavioral assay

## Question

Does the real-options wording bundle added to
`kb/instructions/invert-solution-shaped-requests.md` improve an agent's choice
among direct action, commitment, passive waiting, a bounded probe, and decline?
The comparison is the behavior-bearing Step 6 and `## Verify` delta introduced
by commit `16be19f9f78795add7489511ed104ed5cef1ce7e`, against the immediately
preceding wording at `2e50f96eb1f2828ae67f882bc5fd90cf9a17db24`.

This assay can identify only the effect of that wording bundle in the tested
packets. It cannot isolate one sentence, establish real-options theory, or
predict behavior in other models, tasks, harnesses, or instruction surfaces.

## Design fixed before dispatch

- Eight cases cross reversal cost, later discriminating information,
  opportunity expiry or current benefit, availability of a cheap bounded
  probe, and owned versus unowned coarse future work.
- Two opaque conditions use identical current instruction text except for the
  behavior-bearing Step 6 and verification bundle. The control restores the
  pre-change least-commitment wording and omits the new option branch. The
  treatment retains the current conditional comparison.
- One fresh `gpt-5.6-sol` planner at medium reasoning handles each
  `(case, condition)` cell. It sees one self-contained packet, writes one
  disjoint JSON response, receives no parent conversation, and may not inspect
  the repository or delegate.
- Dispatch order is deterministic but condition-opaque. One execution per cell
  makes this a bounded discrimination smoke test, not a variance estimate.
- A different fresh judge receives shuffled anonymous responses with the
  predeclared rubric. It does not receive the condition mapping.

The generator verifies the current instruction against SHA-256
`08b7779e12b8cc45b0fd78dc0784f187a1e9f7a88b20c2c614b34daf0cd08733`
before producing packets. Generated packet hashes and the opaque codebook are
retained under `generated/`.

## Measures

The primary measure is exact posture accuracy against the predeclared case
answer: `direct`, `commit`, `wait`, `probe`, or `decline`.

Secondary checks ask whether the response:

- avoids option analysis when the choice is cheap and reversible;
- avoids false waiting or probing when no later input can discriminate;
- names the preserved alternative, discriminating input, opportunity status,
  delay or probe cost, and return rule when it waits or probes; and
- rejects an unowned “decide later” placeholder rather than presenting it as
  productive deferral.

## Interpretation rule

Call the treatment a **positive directional signal** only if it gets at least
two more of the eight postures right than the control, introduces no new miss
on a safety-critical case, and does not increase false deferral. Call it a
**negative directional signal** if it gets at least two fewer right or adds a
false deferral on a safety-critical case. Otherwise call the primary contrast
**inconclusive**. Secondary completeness can explain the contrast but cannot
reverse this rule.

No result from this one-run, one-model assay warrants a generic planner,
schema, validator, or claim that the combined methodology improves LLM-agent
outcomes. A positive result supports retaining and testing this exact wording
bundle; a negative result reopens its wording; an inconclusive result records
the measured behavior without inventing an effect.

## Completed result

The run was inconclusive and not decision-useful: treatment posture accuracy
was 8/8 against control accuracy of 7/8, below the preregistered two-case
threshold. See the compact [evidence record](./report.md) for the retained
result and the changes required before repeating it.

## Commands

```bash
python3 kb/reports/planning-delegation-theory/commit-wait-probe-assay/run_assay.py generate
python3 kb/reports/planning-delegation-theory/commit-wait-probe-assay/run_assay.py build-judge
python3 kb/reports/planning-delegation-theory/commit-wait-probe-assay/run_assay.py score
```

Planner and judge execution is intentionally performed by fresh harness
sub-agents rather than by the script. The script only freezes packets, verifies
outputs, joins the opaque codebook after judgment, and computes descriptive
scores.
