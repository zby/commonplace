---
name: verify
description: Use for an operator-requested, one-shot check of a named target with a named model unavailable through the native worker facility.
type: types/instruction.md
---

# Verify

Use the native facility if it offers the requested model. Do not substitute a shell launch for a denied approval, exhausted budget, or missing operator choice. This checkout trial is the narrow exception in [ADR 086](../../reference/adr/086-projects-read-the-library-from-the-installed-package.md).

1. Confirm the target, lens and named profile. Use this command only if the brief, material inspected and answer may be public. Write a brief with the request, constraints, target paths and lens, not your conclusions. Ask for numbered findings with a location, problem and suggested fix, or an explicit statement that there are none.
2. Run `commonplace-sub-worker run --profile NAME --brief PATH` once from the checkout. Allow enough shell time for the call; where necessary run it as a background shell job, retain its exit status and JSON and wait for that same job. The command needs network access and writable harness state. Do not retry on a timeout or launch another worker to poll. On a nonzero exit stop and report the result; do not revert checkout changes.
3. On a review-only request, report the checked findings without editing. On an editing task apply only local fixes you can check against the target or its source. Give a reason for each declined finding and escalate anything that changes direction, conflicts with the commission or remains consequentially disputed. Report counts and list the declined and escalated findings. A model check does not grant human verification.
