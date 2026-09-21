# Preserve the definition checks after workshop closure

Operator decision, 2026-09-21: keep the checks beside the definition as plain
Markdown maintenance material. A short meta comment in the definition tells
editors to apply them when changing it. This replaces the earlier proposal to
put them in the instructions collection.

## Staged files and destinations

| Workshop file | Library destination |
|---|---|
| [Definition](../definitions/conjectural-learning.md) | `kb/notes/definitions/conjectural-learning.md` |
| [Checks and cases](../definitions/conjectural-learning-checks.md) | `kb/notes/definitions/conjectural-learning-checks.md` |

The definition contains an HTML maintenance comment pointing to its sibling.
The relative link survives promotion of both files together. The checks are
specific to this definition, with no instruction type or general procedure.
The published definition remains readable without opening the maintenance
material.

## Retained content

The checks file holds the six adopted tests, fourteen numbered cases, their
shared assumptions, and the definition's purpose. The tests and case table
were extracted without changing their wording or expected classifications.
The decision record now links to that maintained copy while retaining the
historical decisions. Keep case numbers stable and report changed assumptions
and classifications explicitly.

The cases cover selected boundaries of conjectural learning. Passing them
does not establish unchanged scope everywhere, including related builder or
reflection definitions. Report additional affected cases when a revision
exposes them.

## Closure and accounting

Promote the checks with the definition and verify their relative link before
deleting the workshop decision record. Historical deliberation remains in git.
Count the checks file as retained material, not disposable scaffolding or an
additional definition. The definition's reader-facing boundary examples stay
in place for now; the full numbered test table has one maintained home.

The writing-companion connection and possible use of review machinery remain
future design questions. This decision establishes only the colocated file
and maintenance comment; it adds no new type, discovery mechanism, or review
integration.
