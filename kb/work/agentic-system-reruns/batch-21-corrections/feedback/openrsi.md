# Operator correction: OpenRSI default private-answer access

Explicit audit-assisted feedback: verify the challenge against frozen SRC-1. Correct only your assigned role through its normal draft/refusal-answer channel. Do not edit other roles, retained publications, method, source or state. Do not execute candidate code, tests or services, install dependencies or acquire sources.

The shipped default evaluation account omits candidate read access to nominally private answers. `OpenMLE-Gym/openmle-sandbox/README.md:80–109` runs submitted code and scoring on the same worker and describes `data/private` as a convention, not a security boundary. `node_workers/sandbox_builder/start_sandboxes.sh:150–154,177–181` mounts the shared root read-only, with selected writable subtrees. Read-only does not hide answer files.

Qualify `RT-RTE-sandbox-evaluation` and dependent evaluation/public assessments with this concrete default-route access possibility. Possible access is not observed leakage, a benchmark impact measurement or a claim about every deployment. Generic isolation/score-source uncertainty does not communicate this condition. Preserve supported alternatives and other qualifications. Supply the source-backed correction or a concrete refutation within the existing boundary.
