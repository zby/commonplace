# Installed Collection Routing

Workshop for deciding how installed Commonplace projects should expose collection structure to both agents and Python tooling without depending on harness-specific startup files.

The current direction is to keep collection identity filesystem-based: a collection is a direct child of `kb/` with a local `COLLECTION.md`. Installed Commonplace library collections should therefore be top-level `cmpl-*` collections, while `kb/README.md` carries canonical routing guidance that agents can read and later frontload into their own startup files if useful.

This workshop closes when the design is either implemented or promoted into an ADR/reference note with an implementation issue or plan.
