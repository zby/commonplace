# Instruction Instructions

Use an instruction for prescriptive content: manual procedures, promoted skill bodies, wrapper prompts, and review gates.

## Frontmatter

- Set `type: instruction`.
- Write `description` as the trigger condition: when an agent should use this procedure.
- Promoted `SKILL.md` files may add skill runtime fields such as `name`, `allowed-tools`, `context`, `model`, `user-invocable`, and `argument-hint`.
- Review gates add gate fields: `gate_id`, `name`, `lens`, `watches`, and `staleness`. Use `requires_trait` or `requires-type` only when the gate applies to a narrower target set.

## Structure

- Start with an imperative or action-oriented title unless the runtime surface has its own required heading convention.
- Keep steps executable on first reading.
- State prerequisites, scope boundaries, decision points, and verification checks where they matter.
- Keep rationale minimal. Put durable reasoning in `kb/notes/` and link from there to the instruction when needed.

## Review Gates

Review gates are instructions for reviewers. When `gate_id` is present, include:

- `## Failure mode` — the failure the reviewer is looking for
- `## Test` — the concrete procedure for deciding PASS, WARN, or INFO
