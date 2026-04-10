# Related-System Instructions

Use this type for an external-system review that compares another system with ours.

- The opening paragraph should say what the system is, what it is for, and who built it.
- `Core Ideas` should focus on mechanisms and design choices, not feature lists. Bolded lead phrases help scanning.
- `Comparison with Our System` should name concrete alignments, divergences, and tradeoffs.
- `Borrowable Ideas` is the most important section. For each idea, say what it would look like in our system and whether it is ready to borrow now or needs a use case first.
- `Curiosity Pass` is the second-pass review. Re-read the draft and look for surprising claims, simpler alternatives, and mechanisms that sound more powerful than they really are.
- For each strong claim in `Core Ideas`, ask:
  - what property does this produce?
  - does the mechanism transform the data, or just relocate it?
  - what simpler alternative might achieve the same result?
  - what could this mechanism actually achieve, even if it worked perfectly?
- `What to Watch` should track future changes in the reviewed system that might affect our design.
- Update `last-checked` when you substantially re-review the system.
