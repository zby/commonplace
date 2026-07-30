# EPAM: transferable scan

**Status:** memory-first and source-ungrounded
**Recall confidence:** high

## Remembered model

EPAM—Elementary Perceiver and Memorizer—is an early Feigenbaum and Simon model of learning, recognition, and verbal or perceptual tasks. It incrementally constructs a discrimination net: tests on features route an input toward a learned image or chunk. When an input is not adequately recognized, learning adds a discrimination or modifies stored information. Later work connected this basic account to chunking and expertise.

EPAM's reusable lesson is austere: memory becomes useful by learning **which distinctions route cases differently**, not by retaining ever more undifferentiated descriptions.

## Provisional ontology

- **Stimulus/pattern:** the input to be recognized.
- **Feature test:** a question whose answer routes the pattern.
- **Discrimination net:** a branching recognition and retrieval structure.
- **Image:** retained information associated with a terminal or recognized category.
- **Learning operation:** addition of a test, branch, or image detail after recognition fails.
- **Chunk:** a familiar unit that can be treated as one item in later processing.
- **Confusion:** evidence that the current net lacks a decision-relevant distinction.

This treats categorization errors as structural diagnostics. If two cases that require different action reach the same leaf, the missing artifact is not more prose about both; it is a reliable discriminator.

## Transfer candidates

- **`EPAM-1` — make misrouting the trigger for vocabulary growth.** Add a new tag, type distinction, selector rule, or index branch when a real task confuses cases that demand different handling—not merely because a conceptual distinction can be named.
- **`EPAM-2` — record paired positive and negative examples.** A routing rule becomes meaningful through what it separates. Type and skill triggers should carry near-neighbor exclusions, not only prototypical matches.
- **`EPAM-3` — favor incremental index repair.** When retrieval fails, identify the earliest decision where the correct artifact became unreachable and repair that discrimination before redesigning the whole taxonomy.
- **`EPAM-4` — test path-length and inspection cost.** A correct but deep or badly ordered discrimination net can consume more context than flat search. Put high-information, cheap tests early when they preserve correctness.
- **`EPAM-5` — audit order effects.** Distinctions acquired from the first cases can bias all later placement. Replay a different case order or use adversarial near-neighbors to expose brittle early commitments.

## Method worth borrowing

Build routing evaluations from **confusion sets**: artifacts sharing surface vocabulary but requiring different operations, and artifacts using different vocabulary but requiring the same operation. Ask which minimal tests separate them. This turns a taxonomy discussion into an executable classification problem.

## Non-transfer and failure modes

- Tree routing forces one order and one path where a knowledge artifact may need many orthogonal access routes.
- The easiest observable discriminator may be a shortcut unrelated to the real mechanism.
- Incremental local patches can create a globally awkward net without periodic restructuring.
- Chunking improves access but can erase the internal evidence or variability required for later revision.

## Grounding questions

1. What learning operations does canonical EPAM actually permit?
2. How are images, chunks, and discrimination tests represented?
3. Which order effects and limits are acknowledged in EPAM studies?
4. How did later EPAM variants extend the original recognition model toward expertise?
