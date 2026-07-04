# Gate Review: semantic/completeness-boundary-cases

## Verdict

WARN

## Findings

- WARN: The precedent framework stretches past the note's own grounding definition of homoiconicity. The note defines homoiconicity narrowly as shared representation with no type-level distinction between program and data (`kb/notes/llm-context-is-a-homoiconic-medium.md:11`). Lisp fits that definition (`...medium.md:15`), but Smalltalk is justified via live-image self-modification (`...medium.md:19`) and the "other homoiconic languages" bucket collapses Tcl/XSLT/Prolog under the looser criterion that the boundary between using and extending is fluid (`...medium.md:21`). Boundary cases like a live image or "everything is a string" do not map cleanly back to the note's own representation-based definition. The fix is scope clarification or compression, not adding more precedent categories.
- INFO: Mixed cases with partial structure fit the argument only with a narrower boundary statement. The note says system prompts, user messages, and tool outputs are all "just text" (`kb/notes/llm-context-is-a-homoiconic-medium.md:11`). The linked scoping note shows that role markers, delimiters, and ordering conventions do provide weak structure, even if they do not enforce isolation (`kb/notes/llm-context-is-composed-without-scoping.md:39`). The simplest case maps cleanly; adjacent cases with partial structure are still inside scope, but only if the claim is read as "no enforced program/data boundary at the model-attention layer," not "no structure at all."

## Boundary Cases Checked

- Simplest instance: plain prompt-plus-document text in one window. This maps cleanly to the note's definition.
- Extreme instance: contexts with role markers, delimiters, and typed tool interfaces. Coverage is possible but strained unless the scope is limited to the model-attention layer.
- Between-items case: markdown artifacts that are both content and executable handoff instructions. This maps cleanly and is the note's strongest example.
- Adjacent concept: systems that are live, reflective, or uniformly string-based without sharing Lisp-style code/data representation. These expose the precedent list's boundary problem.
