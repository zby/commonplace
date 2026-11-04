# Invariants under composition

## Parked question

Posed by the operator on 2026-11-04 while revising the near-decomposability account. The operator asked to park the ideas here, not begin the investigation.

How can we build larger systems from smaller components while preserving the properties the larger system relies on? What must be known, specified, enforced or checked at component boundaries?

The starting insight is that interactions need not be strong to break an important invariant. A decomposition adequate for predicting typical behavior may omit effects that matter for correctness. Locating a component to change and establishing that a change preserves required invariants are separate achievements.

This could inform how Commonplace composes instructions, tools, validators and maintenance workflows. It is not yet a theory or a proposed system change.

## Ideas to revisit

- Distinguish invariants, interface contracts, environmental assumptions, and probabilistic guarantees rather than treating every useful property as an invariant.
- Ask when component guarantees survive composition, including feedback and shared state.
- Relate near-decomposability to the cost of checking preservation, without assuming weak interactions guarantee it.
- Explore the operator's suggested connections to chaos, nonlinear systems and mathematical catastrophe theory. Determine which mechanisms actually apply; do not equate every threshold violation with chaos or catastrophe.
- Compare those connections with compositional verification, assume–guarantee and rely–guarantee reasoning, and robustness or small-gain conditions in control theory.
- Keep unsettled requirements distinct from violations of settled requirements. The JSON/exception example concerns the former; a system's failure to preserve an agreed invariant concerns the latter.

## Local starting points

- [Near-decomposability may make local inspection affordable](../../theory/near-decomposability-may-make-local-inspection-affordable.md): the invariant-preservation distinction that prompted this workshop.
- [Clear instructions can compose into an unsettled contract](../../theory/clear-instructions-can-compose-into-an-unsettled-contract.md): composition can leave the requirement itself unsettled.
- [Addressable theory](../../theory/definitions/addressable-theory.md): locating and revising parts.

## Unassessed reading leads

These locators were found in an initial search on 2026-11-04 before the operator asked to park the work. They are a reading queue, not source ingests or grounds for adopted claims. No literature review or transfer assessment has been completed.

- Abadi and Lamport, [Composing Specifications](https://www.microsoft.com/en-us/research/publication/composing-specifications/) and [Conjoining Specifications](https://www.microsoft.com/en-us/research/publication/conjoining-specifications/).
- Benveniste and co-authors, [Contracts for System Design](https://research-explorer.ista.ac.at/record/5677).
- Jiang, Teel and Praly, [Small-gain theorem for ISS systems and applications](https://web.ece.ucsb.edu/~teel/ECE236/jiang-teel-praly-1994).
- Lorenz, [Deterministic Nonperiodic Flow](https://doi.org/10.1175/1520-0469(1963)020%3C0130:DNF%3E2.0.CO;2).
- Zeeman, [Catastrophe Theory](https://imechanica.egr.uh.edu/sites/default/files/1976%20zeeman%20catastrophe%20theory.pdf).

## Resumption and closure

Resume substantive work only when the operator asks. No reading sequence, experiment or implementation is commissioned now.

If resumed, the useful outcome is a supported account of which composition obligations matter for agent-operated KBs, with worked cases and limits on any mathematical transfer. Close by extracting supported conclusions and necessary source records, or recording why no useful transfer survives, then removing the workshop and its index entry.
