KB-specific terms used in this note: "select/call loop", "bounded calls", "bounded-context orchestration model", "decorrelated checks", "frame-local information", "clean context", "flat system", "lexical frames", "two-channel failure model".

**select/call loop** — introduced via a link in the first paragraph ("The select/call loop already builds this step"), never defined inline. Later uses ("the select/call loop" in the body) assume the reader has already loaded the linked note. The first mention provides no inline gloss, so a reader who hasn't read the linked note cannot follow the mechanism being described.

**decorrelated checks** — used in "The error correction framework requires decorrelated checks" with a link but no inline explanation. The phrase "the verifier's error modes must differ from the generator's" provides partial context immediately after, which is helpful, but "decorrelated" is this KB's framing and should be glossed on first use rather than relying on the reader to infer from the parenthetical.

**frame-local information** — appears in "the coordination guarantees note predicts contamination — frame-local information remaining globally visible" without any definition. "Frame" is part of this KB's vocabulary (bounded calls, clean frames) but "frame-local" is used as if already established.

**clean context** / **clean frames** — "operates on clean context" and "exploit clean frames recursively" in the body. These are KB-specific concepts used without inline definition or gloss after their first occurrence.

**two-channel failure model** — used multiple times (body, Open Questions) referring to Tu's framework. The note introduces it as "Tu's two-channel failure model (global drift = depth-driven, residual leaf errors = work-driven)" in the KB evidence section, which provides a definition. Subsequent uses are fine.

The most significant issue is **select/call loop**: used four times after the first linked mention, always as a known concept, never glossed. A reader encountering this note without the linked note context cannot follow the dependency argument.
