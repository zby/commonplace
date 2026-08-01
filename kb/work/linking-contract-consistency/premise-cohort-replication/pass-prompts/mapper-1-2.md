You are an independent mapper in a frozen semantic-replication experiment.

Read only the frozen Stage-1 observation file named in this prompt under the fixture root. Do not read any artifact packet, the Commonplace checkout, the filesystem beyond that file, or the network. Do not infer cohort, current label, prior disposition, or production authorization.

Map every observation to exactly one neutral class. Return exactly one compact JSON object per observation on one line with keys `id`, `class`, `confidence`, and `explanation`. `class` must be one of C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12, C13, C14, or C15. `confidence` must be `high`, `medium`, or `low`. Do not use the eventual production identifier. Do not wrap JSONL in Markdown fences. Preserve C15 when the observation is insufficient.

Class definitions:
C1 — theoretical dependence: A is an assertion whose truth or applicability takes B as an assumption or condition; rejecting B reopens whether A holds or applies. B is not merely evidence, explanation, operating path, or prior operational requirement.
C2 — explanation: B supplies the account or principle explaining why or how A occurs or holds.
C3 — operation: A's effect is literally produced through the process, component, control path, artifact, or rule in B.
C4 — design dependence: A is a design, rule, description, procedure, or system-definition artifact shaped or justified by theory in B.
C5 — prerequisite: B must be available, true, or completed before A works, but is neither A's theoretical premise, explanatory account, nor operating path.
C6 — target evidence: An observation or case in B corroborates, qualifies, or bounds A.
C7 — source evidence: A is an observation or case bearing materially on an assertion in B.
C8 — development: A develops, specializes, or carries B's argument further.
C9 — exemplification: A is a worked instance of B's more general claim.
C10 — definition: B defines a term materially used by A.
C11 — contrast or incompatibility: A and B are meaningfully contrasting or conflicting claims.
C12 — another formal relation: another recurring formal relationship is better; name it and state its reader and revision consequences.
C13 — connective prose only: the local relationship is useful but does not earn a mechanically discoverable edge.
C14 — no useful connection: the proposed edge fails the articulation test or adds no useful traversal.
C15 — insufficient observation: the frozen observation does not contain enough information to distinguish the relevant classes without reopening the artifacts.

Frozen observation file for this pass:
observations/pass-1-2.jsonl
