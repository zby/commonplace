# Śniadanie AI: five-minute Commonplace demo

## Commission and outcome

Posed by the operator on 2026-11-11: prepare another Śniadanie AI submission as a five-minute demonstration, not a slide presentation. Lead with Commonplace as a usable LLM wiki. Introduce the research question as an additional reason for building it, not something users must believe to use it.

This workshop prepares a smooth, rehearsed demonstration of collections, types, and the theory collection's methods: claim titles, a link language, and a philosophy-informed quality goal. It closes after delivery and retention of useful feedback, or explicit cancellation. Do not infer why the earlier submission was rejected. The [DSW material](../dsw-talk/README.md) is related preparation, not an identified copy of that meetup submission.

## Audience promise

An agent-operated wiki can have explicit rules for what knowledge is worth keeping, how it is expressed, and how it connects. Different collections can have different methods. The theory collection is our most developed example, not a universal template for all knowledge.

Show the machinery working on one deliberately constructed note. Label the example as staged; it is neither a naturally occurring failure nor evidence of improved learning or retrieval performance.

## Five-minute run-through

| Time | Action | Point to say |
|---|---|---|
| 0:00–0:30 | Open the wiki and explain the task | Commonplace helps an agent retain and develop knowledge beyond a chat; the research hypothesis is optional for users. |
| 0:30–1:15 | Open the corrected demo note and its two labelled links | A claim title exposes the argument before opening the file. Links distinguish a premise from a further development, rather than merely saying “related.” |
| 1:15–2:00 | Load the missing-description state; validate; restore the description | A type has exact requirements that code can check. |
| 2:00–3:30 | Show the structurally valid but overclaiming state; show one semantic review; correct the title | Passing structural validation does not mean the title's claim is supported. Semantic review requires model judgment. |
| 3:30–4:30 | Point to the theory collection's quality goal | Prefer explanations with broader supported application and explicit limits, not just longer or more polished notes. |
| 4:30–5:00 | Generalize and close | Other collections can develop different rules. Research question: can retaining criticism and revised methods improve what agents can do later, without changing model weights? |

If behind schedule, cut the live semantic call and show its previously captured result. Never cut the distinction between structural validity and supported content. Keep the final research question to one sentence.

## Demonstration files

- [demo.md](./demo.md): corrected, structurally valid starting and finishing state. This is a staged workshop note, not adopted theory.
- `01-missing-description.md.txt`: intentionally missing a required field; also carries the exaggerated title used in the next step.
- `02-overclaim.md.txt`: restores the description but leaves an unsupported universal title. Expected to pass structural validation; intended to attract a title–body alignment finding.

The faulty states are stored as `.txt` templates so routine Markdown validation does not encounter a permanently broken artifact. Copy them onto `demo.md` only for rehearsal or delivery. Keep this README open as the run sheet. Do not modify library notes for the demo.

The only change between the two faulty states is the required description. The only substantive change from the second faulty state to the corrected state is the H1 title. This isolates what each check demonstrates.

## Commands and reset

Run commands from the repository root. Before starting, keep a byte-for-byte backup of the corrected note outside the checkout:

```bash
cp kb/work/sniadanie-ai-demo/demo.md /tmp/commonplace-sniadanie-demo-corrected.md
```

Use that backup only for this rehearsal; recreate it from the corrected file before a new run. Do not overwrite it while a faulty state is loaded.

### Structural failure

```bash
cp kb/work/sniadanie-ai-demo/01-missing-description.md.txt kb/work/sniadanie-ai-demo/demo.md
commonplace-validate kb/work/sniadanie-ai-demo/demo.md
```

Expected: missing required description. The nonzero exit is intentional. Then restore the description by loading the next state:

```bash
cp kb/work/sniadanie-ai-demo/02-overclaim.md.txt kb/work/sniadanie-ai-demo/demo.md
commonplace-validate kb/work/sniadanie-ai-demo/demo.md
```

Expected: structural pass, despite the unsupported title. Say: “The document is well formed; that does not make its claim true.”

### One semantic check

```bash
commonplace-review run gates kb/work/sniadanie-ai-demo/demo.md --criteria frontmatter/title-body-alignment
```

The [criterion](../../instructions/review-gates/frontmatter/title-body-alignment.md) asks whether the body supports the H1's claim and scope. Intended finding: the body discusses selecting relevant context, not a guarantee that every additional note improves every answer.

This command is a real model call and may cost money. It has not been run as part of saving this plan. Rehearse before relying on it; do not promise a particular verdict. Save the actual result path and elapsed time below. Do not invent output or quietly substitute an unrelated review. Prefer showing the prepared review during delivery; a live call is optional only after timing it. An unchanged pair may reuse a fresh result rather than launch a new call; disclose that if relevant.

Restore the corrected title:

```bash
cp /tmp/commonplace-sniadanie-demo-corrected.md kb/work/sniadanie-ai-demo/demo.md
commonplace-validate kb/work/sniadanie-ai-demo/demo.md
```

A review of the faulty title no longer describes the corrected note; do not present it as a current verdict. A second review is optional in rehearsal, not needed in the five-minute demo.

## Collection method: what to show

The [theory collection contract](../../theory/COLLECTION.md) supplies the local writing and linking rules. The [note type](../../types/note.md) supplies the document contract. Do not conflate a collection's method with a type's required fields.

- **Claim titles:** contrast “Context management” with the corrected demo title. Explain scanning and connecting as intended benefits, not measured results of this staged example. See [the title-as-claim explanation](../../theory/title-as-claim-enables-traversal-as-reasoning.md).
- **Link language:** the demo uses `grounds` for a premise and `extends` for further development. Open one destination if time permits; do not tour the vocabulary.
- **Quality criterion:** [explanatory-reach](../../theory/first-principles-reasoning-selects-for-explanatory-reach-over.md) means seeking a general formulation supported by its argument, with boundaries mapped. Present it as a philosophy-informed direction for writing and criticism, not a numerical value function. Title alignment is one supporting check, not a measure of the entire goal.
- **Other collections:** architecture decisions might prioritize recoverable alternatives and constraints; customer research might prioritize attribution and separating observation from interpretation. These are possible methods to develop, not equally mature shipped packages.

## Rehearsal and acceptance

- [ ] Confirm meetup language and adapt spoken narration; five minutes is the fixed budget.
- [ ] Inspect the corrected note and linked destinations for readable projection size.
- [ ] Reproduce the expected missing-description failure and the overclaim state's structural pass.
- [ ] Run the single semantic review on the overclaim state; inspect whether its actual finding is useful and accurate.
- [ ] Record result path, model/profile, and elapsed time; keep the output ready to open without networking.
- [ ] If the review misses the mismatch, inspect the finding and input before revising the staged example; do not fabricate a successful detection. Stop and choose a different demonstration if it cannot be made reliable without misleading the audience.
- [ ] Rehearse the complete sequence inside five minutes, including file switching.
- [ ] Restore `demo.md` to the corrected state after every rehearsal, including interrupted runs.
- [ ] Check the final diff; no adopted theory, runtime, or earlier talk materials should be changed.

Rehearsal record: deterministic checks recorded in `checks.md`; semantic result, timing, spoken-language script, and delivery outcome remain pending.

## Scope of further work

Preparation may revise the demo fixtures, run sheet, and rehearsal record inside this workshop. Use the existing review machinery; do not change validators or review criteria to make the demo pass. No delegation, submission to organizers, package installation, or changes to research claims are commissioned here. If a real framework defect blocks the demo, record it and ask before expanding scope.
