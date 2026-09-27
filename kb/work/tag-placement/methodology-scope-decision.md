# Method-guided action: scope and placement

## Operator decision

On 2026-09-26 the operator accepted renaming methodology to
method-guided-action while keeping the narrower question: how an agent selects
or acquires a method, brings it into use, and lets it guide decisions,
including where that guidance ends. The previous name suggested a broader
subject than the head actually gathered.

The [renamed head](../../tags/method-guided-action-README.md) covers selection,
borrowing and transfer, activation, enforcement, and which choices a method
settles or leaves open. Definitions and worked cases qualify when they explain
one of those relations. Merely containing instructions or following a method
does not qualify.

The [actionable methodology definition](../../notes/definitions/actionable-methodology.md)
distinguishes intervention-relevant guidance from pure description. A method
can guide literature borrowing without the borrowed ontology itself being a
method. Selection and transfer checks are what qualify the literature-reuse
note.

The operator also accepted overlap with learning-theory. A note about the
relationship between theory and method qualifies here when it explains how
decisions move between following the method and reasoning beyond its coverage.
This supersedes the previous head's exclusive routing of their joint execution
to learning-theory, and the initial rejection of ADD-180 under that boundary.

## Dispositions

| Entry | Result under method-guided-action | Reason |
| --- | --- | --- |
| TP-038 | Retain assignment under renamed tag | The literature-reuse note tells ingestion to examine which cases shaped a distinction and whether it discriminates cases in the receiving problem. These are selection and transfer checks. |
| ADD-005 | Add tag | The fixed-model house note distinguishes available operations from missing procedures that must be retained and invoked. It explains how a method becomes usable. |
| ADD-008 | Add tag | The self-extension note examines which consequential choices a held method actually settles, rather than merely routing to an actor. |
| ADD-123 | Add tag | The closure comparison separates a method supplying decision criteria from computation supplying decisions. |
| ADD-124 | Add tag | The enforcement note explains activation and response as separate ways a method governs execution. |
| ADD-164 | Add tag | The specification-strategy note selects among methods according to when reliable understanding becomes available. |
| ADD-180 | Add tag; supersedes rejection | The two-layer note uses coverage tests to decide when to follow the method or fall back to theory, and verification to govern promotion into the method. |

## Existing membership check

All sixteen members present before the rename retain their assignments under
the new name. The six entries above account for the literature-reuse note and
five additions from the preceding pass. The other ten members fit as follows:

| Member | Inclusion basis |
| --- | --- |
| Actionable methodology | Defines when an operator can use a method's mapping to select interventions. |
| Capable agents need methodology selection | Explains choosing a governing method among incompatible approaches. |
| Borrowing through retained artifacts or weight activation | Compares two routes for making an external method operative. |
| Weight-resident methodologies | Explains activation through cues, including reconstruction limits and explicit loading. |
| Borrowed patterns and shared mechanisms | Bounds when a source practice can govern target work without fresh justification. |
| Source-adoption policy | Records the adoption gates used to select borrowed practices. |
| Alexander's patterns | Works through transferring pattern contracts and generative rules into KB design, with looser analogies marked. |
| Intent controlling local choices | Tests whether an intent changes admissible or preferred actions, a boundary on guidance controlling decisions. |
| Problem matches and method search | Separates candidate selection, transfer warrant, and checks for composing methods. |
| Reviewers sharing the field's prior | Explains a review method's limitation and criteria for interpreting and acting on its findings. |

The theory–methodology execution note becomes the seventeenth member. All
members are linked from the head. Their arguments are unchanged; edits to
member artifacts are confined to tags. Placement does not validate the factual
claims in those arguments. No parent-gap entry is closed by this rename or
addition.

## Navigation and verification

The tag landing and current workshop pointers use the new name. Both published
head paths, the older notes path and the tags path, redirect directly to the
new head. Original reviewer wording and the frozen placement baseline retain
the historical name. Stored placement reviews are unchanged; these dispositions
are not a fresh independent assay.

Explicit validation of all edited Markdown artifacts, `commonplace-validate
tags`, and `commonplace-validate redirects` completed with zero failures and
zero warnings. The head retains its validated completeness mark. No live
member carries the old tag, and no current Markdown link targets the old head.
The missing-baseline report lists no target for the renamed head, so no
baseline retirement is needed.

Status counts remain 35 original assignment findings resolved and 33 open;
eight addition entries accepted and 198 open; 128 parent-gap entries open.
`git diff --check` passed. `uv run pytest` completed: 842 passed.

## Input versions

SHA-256 of all seventeen live members after metadata edits and the resulting
head. The definition used to interpret the boundary is itself a member.

| Input | SHA-256 |
| --- | --- |
| `kb/notes/a-fixed-model-house-must-retain-missing-procedures-for-theory-use.md` | `66c1fd1e697cf0c41f3ecbc8a81fbfa1645a672ea56837408326d10589bb272e` |
| `kb/notes/a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md` | `8eeea45ae5bce5cc77c6537a799979e2d340edd6b62a2ba6f1598c95dcdae3a5` |
| `kb/notes/alexander-patterns-and-knowledge-system-design.md` | `00e00951614c55e47736902034f5977b2b1f1352c802bb4275164135c5f76e5e` |
| `kb/notes/borrowed-patterns-transfer-only-over-shared-mechanism.md` | `9108da387448a621337956f590ccc1e3ca9c7a0b4bedda385e0e4efe0415beaf` |
| `kb/notes/borrowing-can-operate-through-retained-artifacts-or-weight-activation.md` | `1543485cd2acfe97d9a65022fafdca3dbc051f6d9dbf77c3bc55ddea8e0e0384` |
| `kb/notes/capable-agents-need-methodology-selection.md` | `bf10a2168cca54172e85b6783787f470bc4cbd9491e2fb424cc74b23cc58e732` |
| `kb/notes/definitions/actionable-methodology.md` | `b631e54422b8b34f9649f38b226636cbbc4df6878b6dfe9e145f51e70ff3c4d9` |
| `kb/notes/intent-controls-choices-by-distinguishing-live-alternatives.md` | `c3cef736675b8a66b94d444576d0e21f34d1e7d32d630a2d0d8b6e7a8b720256` |
| `kb/notes/literature-reuse-can-reverse-a-papers-hierarchy-of-contributions.md` | `c0cbe3cb4d9e93eeabceb59c6fda47f06a3859ec709393c02985da1b07534ee5` |
| `kb/notes/methodological-and-computational-closure-track-different-changes.md` | `dbf01144159d1030fe0581a6035bf28d36f4d3cb26e569cea58a1aeb0d818594` |
| `kb/notes/methodology-enforcement-is-constraining.md` | `48cd59d184db73274ce5af1c141997002b84e9ba8bd88f99ebf7e960a4c6f2b2` |
| `kb/notes/problem-matches-guide-method-search-mechanism-matches-bound-transfer.md` | `1512143c76a4cba8696c2aa78ccc6154c5a63a80fe9bc9a830890346e2fa5a85` |
| `kb/notes/reviewers-share-the-fields-prior-so-interpret-findings-by-stance.md` | `cecb65b6d6a6b39b88e550437abc89a5c5e1705177d31095bd1db16c53857bbd` |
| `kb/notes/specification-strategy-should-follow-where-understanding-lives.md` | `09a314541de671c6d652825fa444f09b040fc74b2383a53c733b7ad828019c53` |
| `kb/notes/theory-and-methodology-form-a-two-layer-execution-system.md` | `48d21651109067bbc808c063827c8a6f3b32da8bdf3f63c57e3bc393d2b8dd8c` |
| `kb/notes/weight-resident-methodologies-compress-behavior-in-context.md` | `e324a759d9af123e67f1dda5b4fec4b5b03f61563386e758b04b9ef1980602c7` |
| `kb/reference/source-adoption-policy.md` | `9084c26de94f7a2bd2b5d0b532462ecc866bea88d08ef6205c8e01afd1753d2a` |
| `kb/tags/method-guided-action-README.md` | `b79f20c5b7377523469822cfa6a6f1312d7c6c642c1948c833a5ccbc619a1453` |
