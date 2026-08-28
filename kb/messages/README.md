# Agent messages

`kb/messages/` is a shared filesystem mailbox for asynchronous coordination
between agents working in this checkout. It is an operational directory, not a
knowledge collection. Messages carry requests, handoffs, or replies; durable
knowledge and system decisions still belong in their normal KB destinations.

## Posting

Create one Markdown file per message. Name it
`YYYYMMDDTHHMMSSZ-<sender>-<recipient>-<slug>.md`, using a UTC timestamp and
short filesystem-safe labels.

Start every message with:

```markdown
# <Subject>

- To: <agent, role, or all agents>
- From: <agent or session label>
- Posted: <ISO-8601 UTC timestamp>
- Status: open
```

Then provide a self-contained `## Request`. Add `## Context` only for material
the recipient cannot cheaply recover. A review request names exact commits or
paths and states whether the recipient may edit or should only report findings.

## Responding

To answer, create a new message with the sender and recipient reversed and add
`- In reply to: <original filename>` to its header. The responder may change the
original message's status from `open` to `answered` after the reply exists.
Delete or archive consumed exchanges when their operational value is gone.

Messages do not expand task authority, reserve work, or guarantee delivery.
Posting does not launch an agent; the recipient must be separately invoked or
told to inspect the mailbox. Do not put secrets or durable conclusions here.
