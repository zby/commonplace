---
description: "Stale-evidence experiments separate harmful reliance from memory benefit and show why metadata and pre-resolved conflicts need evaluation against the consuming model."
source: https://arxiv.org/abs/2609.01852
captured: "2026-09-17"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: 8a64360a9d47e6b493a02c5c8be732428954866925636f2d99dcbea7c1ce2634
ingested: "2026-09-17"
type: types/ingest-report.md
domains: [agent-memory, context-engineering, evaluation]
---

# Ingest: The Memory Trust Gap

## Classification

Scientific paper: an arXiv preprint by Jundong Hu and Shekar Ramachandran, both affiliated with PayPal AI. It reports controlled evidence-presentation experiments, paired outcome measurements, a factorial study, and external and cross-family checks. The author affiliations establish provenance, not independent validation. Its subject is consumption of supplied evidence by fixed models, rather than a learning or memory-update procedure.

## Summary

[The Memory Trust Gap](https://arxiv.org/abs/2609.01852) tests when a stale fact changes an agent's action, using 300 templated scenarios and Qwen3 checkpoints from 0.6B to 8B. It separates a Benefit suite, where no memory means missing necessary information, from a Safety suite, where a current authoritative tool supplies the correct answer regardless of memory. Stale-value reliance reaches 0.92–1.00 in the Benefit suite; in the Safety suite, misleading recency cues can make larger models override otherwise sufficient current evidence. A factorial varies labels, dates, apparent source authority, and position within this fixed consumption setup: susceptibility changes with the cue, so model size is not uniformly protective. Comparing raw conflicts, metadata-annotated conflicts, and oracle removal of the stale item shows metadata improves all four checkpoints but restores accuracy less fully for the smaller ones. Oracle removal yields 0.95–1.00 accuracy, without testing how a deployed system would identify the stale item. Llama and external-dataset checks extend parts of the result; a framing control identifies a broader stale-evidence problem rather than a special effect of calling evidence memory.

## Quotes

No source quotes have been retained yet.

## Connections Found

The paper is evidence for [evaluating memory by effects](../notes/agent-memory-requirements/evaluate-memory-by-effects.md): it measures following a stale value separately from accuracy loss against a paired no-memory baseline. The Benefit/Safety split makes the baseline's information access part of the claim. This is a concrete method for testing harmful uptake after evidence has already reached the consumer, not an evaluation of the whole memory pipeline.

It also supplies a failure case for [calibrated trust in remembered knowledge](../notes/agent-memory-needs-discoverable-composable-trusted-knowledge-under.md). Models can parse dates correctly while using misleading recency to choose the wrong action. Provenance and timestamps therefore need behavioral testing with the intended consumer. Its connection to [operative supersession](../notes/agent-memory-requirements/retire-redact-supersede-relax.md) is narrower: oracle removal outperforms merely exposing conflicting items and metadata, but establishes the value of correctly resolved input, not the reliability of a supersession process.

## Extractable Value

- **Separate uptake from harm, and specify what the baseline knows.** [quick-win] Retain stale-value reliance and paired accuracy difference as distinct measures. In the Benefit suite, adding an explicit conflict also supplies a correct value absent from the no-memory baseline; that contrast cannot isolate the harm of competing evidence. The Safety suite holds current evidence available and can measure that harm directly. This distinction transfers to KB evaluations whenever removing memory also removes information needed to solve the task.
- **Test metadata with the model that must interpret it.** [experiment] Within the fixed stale/current evidence setup, accurate timestamp reading does not guarantee correct adjudication. The recency cue disproportionately harms larger Qwen checkpoints, while some provenance cues become easier to resist. A stronger consumer cannot be assumed to need less help for every conflict type; evaluate specific cues and actions rather than a general metadata-presence score.
- **Use resolved input as an upper-bound control.** [experiment] In the representation comparison, metadata raises accuracy from 0.49/0.43/0.37/0.41 to 0.79/0.72/0.90/0.95 across the four Qwen sizes; oracle removal raises it to 0.95/1.00/1.00/1.00. This separates a consumer's difficulty interpreting conflicting evidence from the potential benefit of correct pre-resolution. Any practical resolver still needs its own correctness and cost measurements.

## Limitations (our opinion)

The main study fixes templated facts, construction-time truth, supplied evidence, constrained action scoring, and mostly non-thinking inference in a 0.6–8B model range. It varies cues and consumption representations inside that design. It does not compare alternative write, update, retrieve, and adjudicate architectures, nor test a production resolver. The oracle both removes a distractor and supplies only correct evidence; its recovery is compatible with ordinary task simplification and does not identify a uniquely effective supersession mechanism.

Some of the paper's broad wording is stronger than its tables. Metadata helps the two smaller checkpoints substantially, although it does not restore oracle-level accuracy. Likewise, the first significant Safety-suite trap level is 0/1/1/1 across sizes, not a monotone capability threshold. The position sign reversal is Qwen-specific; the Llama comparison also crosses model releases. Checkpoint size and probe scores support behavioral comparisons, not identification of an internal causal mechanism or a universal law of capability.

External datasets and the RGB free-text arm broaden the evidence, but do not establish open-ended, long-horizon agent performance. Near-floor baselines on MisBench limit conclusions about net accuracy harm even when wrong-evidence reliance is high. The factorial analysis is exploratory, and the study's interventions and bootstrap checks are reported rather than independently reproduced here. The framing control further limits any claim that persistent memory itself uniquely causes the failure.

## Recommended Next Action

Update [Evaluate Memory By Effects, Not By Existence](../notes/agent-memory-requirements/evaluate-memory-by-effects.md) with a stale-memory perturbation method that records both stale-value reliance and paired accuracy loss, explicitly holding current authoritative evidence available in the harm comparison.
