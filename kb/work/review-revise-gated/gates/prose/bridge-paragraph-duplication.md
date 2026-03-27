---
gate_id: prose/bridge-paragraph-duplication
name: Bridge paragraph duplication
lens: prose
watches: [body]
staleness: changed
---

## Failure mode

A transition paragraph at the end of one section previews exactly what the next section then enumerates. The reader gets the same content twice — once as preview, once as the section's own development.

## Test

Check the last paragraph before each section heading. Does it summarize or preview what the following section will cover? Then read the following section. If the preview and the section's own content cover the same ground, the preview is redundant.

Report all instances. A one-sentence transition is fine. A full paragraph that duplicates the next section's enumeration is not.

## Example (fail)

A paragraph says "The conflation arises when higher-level interfaces package bounded calls as chat sessions or framework-managed tool loops" — then the next section enumerates chat sessions, framework-owned tool loops, and continuing agent sessions as the three problem sources. The paragraph and the section cover the same ground.
