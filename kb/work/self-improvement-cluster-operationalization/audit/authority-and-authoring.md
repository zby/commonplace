# Audit: authority, routing, and authoring

## Authority map

`AGENTS.md` is the broadest behavioral authority in the checkout. Collection contracts narrow it by location; type specifications constrain artifact form; selected instructions and skills impose task-specific procedures. Deterministic code can enforce only the subset represented in schemas or explicit checks. This layered structure is coherent and usually makes force legible.

The cluster is absent from that map. Searches across `AGENTS.md`, its template, collection contracts, `kb/types/`, `kb/instructions/`, and `src/commonplace/` found no route to the cluster and no `operationalized-from` lineage for it. The current authority paths are therefore user invocation and accidental link discovery. Neither reliably loads the theory when an instruction, validator, type, collection contract, or root agent rule changes.

Disposition: the later digest should be a bounded fast path, linked `operationalized-from` the cluster and routed from `AGENTS.md` for covered behavior-authority changes. Out-of-coverage cases must fall back to the live theory. The audit does not pre-empt the workshop's authority-path decision by installing that route now.

## Collection and type contracts

The collection contracts state audience, membership, lifecycle, and local conventions well enough to constrain agents that load them. The weakest channel is not wording but discovery: recursive collection scope depends on the agent actually loading the applicable contract. Root routing mitigates this, but no machine check proves every agent did so.

Type specifications correctly split semantic definitions from YAML-enforceable structure. That split respects oracle warrant. A schema can establish field presence, allowed values, and shape; it cannot establish whether a title is a good claim or whether prose has explanatory reach.

No type or collection change was warranted by the cluster audit. Collection-contract freshness remains a separate, already-proposed substrate problem rather than something to solve by pretending these files are ordinary note criteria.

## Authoring instructions

Once selected, authoring skills are strong retrieval wires: they specify target, prerequisites, steps, validation, and outputs. Three operativity defects were repaired:

1. `cp-skill-health-check` and `write-instruction` pointed to `src/commonplace/cli/init_project.py` (and in one case a nonexistent `PROMOTED_SKILLS`) as promotion authority. The actual retained authority is `MANIFEST.promoted_skills` in `src/commonplace/scaffold_manifest.py`.
2. `cp-skill-convert` assigned semantic trait and title-quality judgment to `cp-skill-validate`. The validator explicitly performs deterministic checks and does not infer missing semantic commitments. The instruction now assigns those judgments to the writer or human review.
3. Fourteen instruction descriptions exceeded the deterministic description-length rule. Because descriptions are the selection surface for agents, these were retrieval defects, not cosmetic warnings. They were shortened without changing procedure semantics.

## Channel portability

The root contract explicitly supports native Windows source checkouts, but several promoted skills show unqualified Bash pipelines, command substitution, `wc`, or POSIX path idioms. A skill selected in PowerShell can therefore fail before its substantive procedure begins. This is a consumer/channel mismatch: the semantic instruction is sound, but its command channel is narrower than the declared execution frame.

The repair spans multiple skills and requires a convention, not scattered substitutions. It is dispositioned as [make promoted skill commands channel-portable](../windows-portability-for-promoted-skills.md).

## Loop classification

- Routing, descriptions, and links implement **search/addressability**.
- Authoring procedures generate candidate artifacts and therefore implement **search/generation** until a distinct validation or human decision occurs.
- Schemas and deterministic checks can implement **evaluation** only inside their mechanically decidable domain.
- Saving or committing an authored artifact implements **retention**; frontmatter and collection placement make the retained commitment retrievable.

This classification is why precise descriptions and correct authority pointers matter: a procedure that exists but is not selected—or selects the wrong authority—does not participate in the system's operative improvement pathway.
