"Hygienic macros" in "the same problem Scheme's hygienic macros solve for code generation" is used without definition. A reader unfamiliar with Scheme's macro system cannot infer what "hygienic" means in this context or how hygienic macros solve the capture problem the note just described.

"Condition/restart systems" in "This connects to condition/restart systems in Common Lisp" is used without definition. The reader gets no hint of what these systems do or why they're analogous to stack unwinding for error recovery.

Suggested fixes:
- For hygienic macros: "the same problem Scheme solves with hygienic macros, which automatically rename variables to prevent accidental capture during code generation"
- For condition/restart systems: "This connects to Common Lisp's condition/restart system, which lets a caller define recovery strategies that a failing callee can invoke without unwinding the entire stack"