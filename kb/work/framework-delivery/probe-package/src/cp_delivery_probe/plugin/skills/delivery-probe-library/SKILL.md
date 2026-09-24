---
name: delivery-probe-library
description: Index of the delivery-probe library. Use when the user asks to follow, run, or look up a delivery-probe procedure, instruction, or type by name (for example "retire a widget" or "calibrate the gadget").
type: kb/types/instruction.md
---

# delivery-probe library

Find the entry the user asked for below, open it through the command given, and follow it.

- An instruction: run `cp-delivery-probe-instruction <name>` and read the file it prints.
- A type: run `cp-delivery-probe-library`, then read `types/<name>.md` under the root it prints.

Links inside a library file are relative to that file, and the printed path is a real path, so they resolve directly.

## Instructions

- `retire-widget` — procedure for retiring a widget
- `calibrate-gadget` — procedure for calibrating a gadget
- `shared-step` — a step other procedures include

## Types

- `probe-note` — the probe note type

If you cannot run commands, the same files are linked from this skill by relative paths, but those paths are relative to the skill's real directory. This skill may be a symlink, so resolve its real path before following them: [retire-widget](../../library/instructions/retire-widget.md), [calibrate-gadget](../../library/instructions/calibrate-gadget.md), [shared-step](../../library/instructions/shared-step.md), [probe-note](../../library/types/probe-note.md).
