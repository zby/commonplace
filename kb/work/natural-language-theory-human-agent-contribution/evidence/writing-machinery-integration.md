# Writing-machinery integration record

Captured on 2026-08-18. This record preserves the first explicit attempt to carry the epistemology and the synthesis-to-atomic comparison back into an operative writing procedure.

## Trigger

After comparing the frozen synthesis note with the later atomic rewrite, the human requested a procedural change:

> OK - I think we should revise the muti stage write skill. Atomic notes are better than synteses so a step in the procedure should check what claims do we make and what we can fold them into existing notes, what warrants new notes and what is the central contribution. Maybe there should be user involved for the folding or when there are more than one new note to be produced.

The immediate analysis identified four process causes: the broad question was treated as one artifact; synthesis generated several independently citable claims; the `synthesis` trait was used as an exemption rather than an extraction signal; and the audit changed the governing title without regenerating the claim skeleton.

## Operative change

The canonical `cp-skill-write-multistage` instruction now inserts `claim-disposition.md` between source reconstruction and the claim skeleton. The new stage requires an inventory of candidate durable claims and assigns each one of these dispositions:

- `central contribution`
- `cite existing`
- `fold into existing`
- `separate new artifact`
- `support/example/scope only`
- `omit/retain in workshop`

For claim-bearing artifacts, the stage defaults to one proposition that another artifact can cite without inheriting an independent claim cluster. It permits synthesis only when the composition among already-citable components is itself the contribution. It requires a user decision before substantively folding a discovered claim into another existing artifact and when more than one independent new artifact is warranted. The skeleton, writer, auditor, acceptance reviewer, promotion conditions, and final verification now consume or check the disposition.

The before and after snapshots preserve the exact deployed text at the integration boundary:

- `cp-skill-write-multistage.before-claim-disposition.snapshot.md` — content SHA-256 `85df191ed69ff823feafb6479e64b5ac27fcc728ccd26d80e326526e5c66a269`
- `cp-skill-write-multistage.after-claim-disposition.snapshot.md` — content SHA-256 `34daf2e24f2a0f21c2c52debad7dba943f7a9a42dc4d588620411f0585defe5c`

## Checks

`commonplace-validate` passed the revised canonical skill cleanly. Two fresh read-only dry runs exercised its decision boundaries:

1. A topic-only request stopped before reconstruction because several materially different atomic contributions fit. It proposed alternatives and asked the user which should govern.
2. A request with a fixed central contribution reached claim disposition, retained one new atomic target, cited an existing explanatory-reach premise, treated mechanism and evidential limits as support/scope, and found no second artifact or fold requiring a user decision.

The generic Codex skill validator rejected repository-specific frontmatter keys that predated this edit; the Commonplace instruction schema, which governs this promoted skill, passed without warnings.

## Evidential status

This is evidence of installation and an explicit causal path from reflection on a theory-writing episode into writing machinery. It is not yet evidence that the revised machinery improves later writing. A later run must show that claim disposition changes an artifact decision and that the change makes a subsequent result more composable, reliable, cheaper to revise, or less dependent on human repair. Only that downstream comparison can supply the next compounding link.

