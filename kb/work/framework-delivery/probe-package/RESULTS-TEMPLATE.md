# Delivery probe results: <harness>

- Harness and version:
- Model:
- Operating system:
- uv and Python versions:
- Tester (agent or person) and date:
- Probe package revision (see PROTOCOL.md):

## Harness facts

- Instruction file it loads (AGENTS.md, CLAUDE.md, other):
- Can the agent run shell commands?
- Can the agent read files outside the project, and under what setting?
- Agent Skills support and skill directories (project, user):
- Does it follow symlinked skill directories?
- Plugin or extension mechanism, and does it copy or serve in place?

## Cases

| Case | Result (pass / fail / not applicable) | What happened | Prompts or denials |
|---|---|---|---|
| 0 Install | | | |
| 1 Base layer | | | |
| 2 Read permission | | | |
| 3 Skills (link) | | | |
| 3 Skills (copy) | | | |
| 4 Router skill | | | |
| 5 Upgrade, same Python | | | |
| 5 Upgrade, Python change | | | |
| 6 Harness plugin | | | |
| 7 Editable install | | | |

## Modifications to the package

For each change: what, why the harness needed it, and the diff or exact description. Write "none" if you ran it unmodified.

## Consequences for the design

What the working design must change, or assume, for this harness. Mark each point as observed or inferred.

## Cleanup

What you installed or changed, and confirmation that it was undone.
