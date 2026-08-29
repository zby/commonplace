# Report cache

Replaceable report views. Payloads in this directory are ignored and may be
deleted when space or freshness warrants it; their authoritative inputs and
producing operation must exist elsewhere.

Current producers include:

- `cp-skill-connect` → `connect/`
- the critique pass → `critique/`
- the composition-friction gate → `friction/`
- the premise-decomposition gate → `premise-decomposition/`
- `commonplace-promotion-candidates` → `promotion-candidates.md`

Generated does not by itself mean cacheable. Outputs carrying unresolved
dispositions, unique judgments, or live protocol state belong in
[`../state/`](../state/README.md).
