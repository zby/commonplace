# Code quality: what Commonplace covers and what it leaves to others

## Goal

Decide how far Commonplace goes on code quality, and take what its
natural-language improvement work can learn from a code-quality tool.

The operator posed this on 2026-11-16 in two steps. First: Commonplace
doctrine mixes code and natural-language instructions, so code quality should
matter; the automatic improvement procedures being built for texts
([ADR 135](../../reference/adr/135-improvement-procedures-are-three-plans-on-one-runner.md),
developed in [decision-lifecycle-evidence](../decision-lifecycle-evidence/README.md))
could perhaps be used for code too. Second, the same day, while the first
analysis was running: maybe Commonplace should focus on the natural-language
part and let others cover the coding part.

The second remark is a tentative direction, not a decision. This workshop
holds the question open until the operator settles it.

[Desloppify](https://github.com/peteromallet/desloppify) is the commissioned
first case. Its reading is in the [desloppify analysis](./desloppify-analysis.md).

## The three positions

- **A. Extend the improvement procedures to code.** Code review operations and
  code edit operations become atoms on the same runner.
- **B. Leave code quality to external tools.** Commonplace keeps what it has:
  the [review code](../../instructions/review-code.md) instruction for changes,
  and the one-off [code simplification backlog](../code-simplification/README.md).
  A consuming project installs a tool such as desloppify if it wants more.
- **C. Cover only the seam between code and instructions.** Commonplace adds
  operations only for defects that exist because a system is defined in both
  forms, which no code-quality tool looks for.

## Agent's recommendation, awaiting the operator

B for general code quality, with C as the only candidate for new work. This is
the agent's proposal. The operator has not adopted it.

Reasons:

- General software engineering is outside this KB's declared scope unless it
  directly informs KB design. Dead code, duplication, complexity and naming
  inside one language are general software engineering. Desloppify ships about
  1,460 Python files of detectors, language plugins and queue machinery for
  them. Rebuilding any part of that is cost without a doctrinal reason.
- The text procedures are still being settled. Their atoms landed between
  2026-11-14 and 2026-11-16, and their declarations are expected to be wrong
  in places until runs correct them. A second domain now would double the
  surface before the first has run data.
- Code and prose differ where the procedures are most careful. The runner
  stops for the operator's approval of the exact final text because nothing
  executable shows that a text edit kept its meaning. Code has tests. A code
  procedure built on the text runner would inherit a stop it mostly does not
  need and lack the test step it does need.
- The seam is the part of the doctrine no outside tool covers. Candidate
  defects: an instruction that describes behaviour the code no longer has; one
  concept named differently in prose and code
  ([ADR 116](../../reference/adr/116-one-word-per-concept-across-prose-and-code.md));
  an instruction step that is performed the same way every time and could be
  code ([codification](../../theory/definitions/codification.md)); a Python
  check that repeats what a schema or an instruction already enforces. These
  are candidates from reading, not observed defect counts.

What would change the recommendation: evidence that external tools do poorly
on a codebase like this one, where much behaviour lives in instructions and
the Python is the smaller part. The probe below tests that.

## Next steps

Each is a proposal. None is commissioned.

1. **Operator decides among A, B and C**, or asks for the probe first.
2. **Probe: run desloppify on `src/commonplace/` as an ordinary user.** Compare
   its findings with the [code simplification backlog](../code-simplification/README.md),
   which a four-agent review produced independently on 2026-09-28. Three
   outcomes matter: findings the backlog lacks, backlog items it misses, and
   findings that are wrong because the tool cannot see that an instruction
   file is the caller or the contract. The third kind is direct evidence for
   C. This needs the operator's go-ahead: it installs a third-party package,
   and the subjective review phase launches paid subagents. The mechanical
   scan alone is cheap and may be enough for a first look.
3. **Route the transfers.** The analysis lists six mechanisms that bear on the
   text procedures. Each goes to the workshop that owns the matter, or is
   dropped with a reason. None is adopted by being listed.
4. **If C is chosen**, write a design proposal under `kb/reference/proposals/`
   for seam operations, starting from one defect kind with observed instances.

## Evidence boundary

The desloppify analysis is a direct reading of a local clone at one commit by
one agent. It is not a retained analysis under `kb/agentic-system-analyses/`.
The commissioned `commonplace-analysis analyse` run stopped at preparation on
2026-11-16 because `AGENTS.md` had uncommitted changes, and the method forbids
choosing another revision without the operator. A retained analysis can still
be run once the checkout is clean; whether it is worth its cost is the
operator's choice.

Nothing here measures desloppify's effect on any codebase. Its claims about
score honesty are its authors' claims.

## Scope and coordination

This commission permits design work in this directory and its entry in the
active list. It does not authorize installing or running desloppify, paid
workers, code changes or new operations.

- [decision-lifecycle-evidence](../decision-lifecycle-evidence/README.md)
  owns the atoms, the grouping and calibration from operator decisions.
- [stochastic-operation-testing](../stochastic-operation-testing/README.md)
  owns evaluation cases and measurement.
- [code-simplification](../code-simplification/README.md) owns the current
  code backlog. This workshop does not add items to it.

## Completion

Close when the operator has chosen among A, B and C and each listed transfer
has an owner or a recorded reason for dropping it. If the choice is B, the
durable result is a short scope statement in the place the operator names. If
it is C or A, the result is a design proposal, and its development moves to
that proposal. Then delete this directory and its active-list entry.
