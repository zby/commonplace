---
description: "A “Referenced by” list turns citations into clickable return paths. Those paths show who cited a note, not whom the note’s author chose to cite."
type: types/note.md
traits: [title-as-claim]
tags: [links]
---

# Inbound and outbound links serve asymmetric reader needs

Here *inbound* and *outbound* are relative to **one note**, not the whole website. Suppose a release checklist links to an approval policy. That single link is outbound from the checklist and inbound to the policy. Both pages are inside the same site.

## How an incoming citation becomes a link you can follow back

Suppose you are reading the policy and want to know which checklists use it. A site builder can scan the links in the source notes, group them by destination, and display **Referenced by: Release checklist** on the rendered policy page. You can now click from the policy back to the checklist.

That return link **is outbound from the displayed page**. It is not a citation written by the policy’s author. The checklist author chose the policy because it tells someone how to approve a release. The generated link answers a different question: *where is this policy cited?* If the checklist drops its citation, the return link disappears on the next build. The builder must count authored links, not its own generated return links, or it will report citations nobody wrote.

The policy author can also choose to link to the checklist as a worked example. That is a second editorial decision, worth making if the example helps readers understand the policy. It is not necessary merely to give them a way back.

## What a “Referenced by” list tells you

When revising a note, use the list to find passages worth reading:

- **Standing:** Is the note a premise of another argument or merely listed as further reading?
- **Grounding:** Do the citing sources offer independent evidence, or repeat the same assertion?
- **Impact:** Would a narrower claim invalidate a recommendation or exclude a cited example?
- **Tension:** Does another note dispute this claim, and if so, on what point?

The list locates those passages; their text answers the questions. The same information can be delivered in two ways: generate clickable return links when publishing a page, or search the source files for citations when a reader asks. Neither requires authors to maintain a reverse list. A maintenance sweep can also use the same data to find uncited notes without displaying a list on any page.
