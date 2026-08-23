# What these descriptions actually spare, and for whom

Measured 2026-08-23.

## The calculation

A cache is worth its maintenance when the work it spares, times how often that
work would otherwise happen, exceeds the cost of keeping it accurate. Every
term differs by consumer, so one disposition for both readers is unlikely to be
right.

## Sizes

| Subject | Source | Doc | Compression |
|---|---:|---:|---:|
| `src/commonplace/lib` | 160 KB, 20 files | `lib-modules.md` 21 KB | 7.6× |
| `src/commonplace/review` | 153 KB, 24 files | `review-architecture.md` 14 KB | 11.1× |
| `src/commonplace/freshness` | 40 KB, 11 files | `freshness-architecture.md` 6 KB | 6.7× |
| `src/commonplace/freshness` | 40 KB | `freshness-schemas.md` 3 KB | 13.3× |

Whole package: 463 KB, 13,218 lines, 85 files — roughly 115k tokens, so not
readable entire. But that is the wrong comparison.

## For an agent, the comparison is per-file, not per-subtree

An agent does not read `lib/`. It reads the one module it needs. `lib/` averages
8 KB per file, about 2k tokens.

So the real choice is: read `lib-modules.md` at 21 KB (~5k tokens), or read
`type_resolver.py` at 15 KB (~4k tokens) and have the authoritative answer.
Reading the doc costs *more* than reading the file it describes, and leaves the
agent with a copy rather than the truth.

The doc's remaining advantage is knowing *which* file to open. That is routing,
and it is already present: `lib-modules.md` opens with a nine-line module map,
roughly 1 KB. **The routing layer is about 4% of the doc and carries most of
the agent-facing value.** Routing plus one targeted file read costs ~2.3k
tokens against ~5k for the description, and ends on the source.

## Where the summary still earns its place

Not uniformly. `validation.py` is 38 KB — around 9.5k tokens — so a faithful
summary of it genuinely spares work an agent would otherwise repeat. The
break-even is module size: below roughly a doc's own length, read the source;
well above it, a summary compresses something real.

This makes the disposition per-region rather than per-artifact, and gives it a
cheap first cut: compare each described unit's size against the description of
it.

## For a human, the spared work is different

A human needs orientation — how the pieces fit, why the shape is what it is,
what the subsystem is for. That does not compress into a routing table, and it
is not recoverable by reading one file quickly, because the question is about
relations rather than any single module.

It also changes slowly. Architecture moves at a different rate than API detail,
so the human-facing narrative carries a much lower maintenance tax than the
per-module description that surrounds it today.

## The punchline

The co-maintenance tax is concentrated in the fast-changing per-module API
detail — which is precisely the part an agent does not need, because it can
read the source faster and get an authoritative answer.

The two low-tax, high-value layers are the routing map and the human-facing
narrative. Both are small. Both change slowly. They are currently bundled with
the expensive layer in the same artifacts.

Separating them is the candidate move, and it is not "delete the docs": it
keeps what each reader actually uses and stops paying for the part neither one
needs in prose form.

## Open

- Does the routing map need to be authored at all, or can it be generated from
  module docstrings and checked?
- Is the human narrative currently written anywhere, or would separating the
  layers reveal it was never there and has to be authored?
- What is the size threshold where a summary starts to pay? `validation.py` at
  38 KB is above it and an 8 KB average module is below it; the crossing point
  is unmeasured.
- Does the same split apply to `commands.md`, where the described unit is a CLI
  surface rather than a module, and `--help` output already exists?
