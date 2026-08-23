# These descriptions are not stale, and that changes the question

Measured 2026-08-23. Small sample; see limits.

## What was expected

The workshop opened on the premise that these artifacts sit in the state
enforce-or-omit forbids: hand-maintained copies of recomputable truth, trusted
by consumers, drifting silently. Staleness was the hazard, and disposition was
the remedy.

## What the repository shows

Lag between each description and the code it describes, in commits touching
that code since the doc was last touched:

| Description | Code | Lag |
|---|---|---:|
| `lib-modules.md` | `src/commonplace/lib` | 2 |
| `commands.md` | `src/commonplace` | 3 |
| `storage-architecture.md` | `src/commonplace` | 3 |
| `architecture.md` | `src/commonplace` | 0 |
| `review-architecture.md` | `src/commonplace/review` | 0 |
| `freshness-architecture.md` | `src/commonplace/freshness` | 0 |
| `freshness-schemas.md` | `src/commonplace/freshness` | 0 |

They are current. More telling, they are largely updated *in the same commit as
the code*. Of the last five commits touching each of four sampled docs:
`lib-modules.md` 5/5 with code, `commands.md` 3/5, `review-architecture.md`
2/5, `storage-architecture.md` 2/5.

That is disciplined co-maintenance, not periodic catch-up.

## What this does to the framing

**The hazard argument does not currently bite.** Enforce-or-omit rests on a
false copy silently suppressing the read that would expose it. These copies are
not false. The rule's asymmetry is still correct in principle and still says an
unchecked copy is one missed edit from the bad state — but the observed system
is not in that state, and a disposition sold as fixing rot would be solving a
problem the repository does not have.

**The cost argument survives, and it is the real one.** These stay current
because a maintenance tax is paid on every code change that touches them. The
question is not "how do we stop these from rotting" but **"agents pay a
recurring co-maintenance tax; which disposition reduces it without losing what
the descriptions provide?"**

**That re-ranks the four dispositions.**

- **Generate** looks stronger than before, not weaker. If a doc is mechanically
  derivable and is currently kept in sync by hand on every commit, generation
  removes a recurring cost rather than merely preventing a hypothetical drift.
- **Register for staleness** looks weaker. A staleness signal mostly fires on
  drift the co-maintenance discipline already catches. Its residual value is
  the catch-up cases below.
- **Minimize** is now about shrinking the taxed surface, not about deleting
  rot.
- **Author only irrecoverable content** is unchanged and still applies to the
  level-native halves.

## Drift does occur and gets swept

Doc-only commits exist alongside the co-maintained ones, and two name the
problem outright: `Plan contract repairs and close command catalogue drift`
(2026-08-19) and `Migrate dependent artifacts to natural-language terminology`
(2026-07-27). So the tax is sometimes paid late, in a cleanup pass. That is the
residual case a staleness signal would serve, and it is worth sizing before
concluding registration has no value.

## Limits

- Commit-level lag is a proxy for content accuracy. A doc touched in the same
  commit as the code may still have been updated incompletely; only reading
  both settles that.
- Four docs sampled at five commits each for the co-maintenance figure.
- `architecture.md` shows zero lag partly because it was touched today by
  unrelated work in this session.
- Nothing here measures whether the descriptions are *correct*, only whether
  they are *tended*.

## What to do next with this

The recovery test — attempt regeneration per region and inspect fidelity — is
still the right discriminator, but its purpose has shifted. It is no longer
looking for rot. It is establishing which regions could be generated, so the
co-maintenance tax on those regions can be removed outright.
