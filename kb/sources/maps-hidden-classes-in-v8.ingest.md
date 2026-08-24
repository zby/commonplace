---
description: "Official V8 walkthrough showing how Maps encode object layouts and how mutating a field compiled as constant invalidates dependent optimized code"
source: https://v8.dev/docs/hidden-classes
captured: "2026-08-19"
capture: web-fetch
genre: practitioner-report
snapshot_sha256: 4d72f508522e628f700218fb09f1fe199c04f7a020eb38ba6f6ee80142d0ec70
ingested: "2026-08-24"
type: kb/sources/types/ingest-report.md
domains: [object-shapes, hidden-classes, deoptimization, runtime-pricing]
---

# Ingest: Maps (Hidden Classes) in V8

## Classification

An official practitioner walkthrough of V8's object-layout structures and optimizer behavior, illustrated with diagrams, `d8` debug output, generated machine-code excerpts, and a deoptimization trace.
Author: The V8 project publishes the page without naming an individual author. Its official-project provenance makes it primary implementation testimony, but not an independent performance evaluation.

## Summary

V8 represents an object's property layout with a `Map`, whose descriptors record property names and locations and whose transitions encode the result of adding properties. Objects built in the same property order can share Maps and descriptor arrays, while divergent additions branch the transition structure and duplicate layout metadata. The walkthrough then shows TurboFan specializing a global field read: while the field remains constant, optimized code embeds its value; mutating that field produces a `field-const` trace that marks dependent optimized code for deoptimization; and subsequent optimization falls back to a Map-dependent backing-store load. Read this source for the concrete data structures and invalidation trace behind claims about runtime pricing, not for measurements of how frequent or costly these events are in production.

## Claims

No claims have been grounded yet.

## Connections Found

This source is the direct technical basis for the field-const runtime-charge example in [Domain pricing routes an exception to idealization assessment but does not decide it](../notes/domain-pricing-routes-an-exception-to-idealization-assessment.md): it shows an optimized assumption being invalidated and dependent code being deoptimized, but does not establish that the triggering behavior is rare or bounded. It also supplies implementation evidence for [Instantiation alone cannot model agent learning across sessions](../notes/instantiation-alone-cannot-model-agent-learning-across-sessions.md)'s old-shape specialization analogy by making the Map identity and invalidation dependency concrete. The broader [Fast properties in V8 ingest](./fast-properties-in-v8.ingest.md) is a companion account of HiddenClasses, inline caches, dictionary properties, and type pollution; this ingest owns the narrower Maps URL and trace rather than duplicating that broader role.

## Extractable Value

1. **V8 gives object layout a comparable runtime identity.** A `Map` is the first pointer in an object, while its descriptor information records which properties exist and where they live. This makes specialization on an object's shape a concrete dependency rather than only an analogy. [quick-win]
2. **Property order determines transition sharing.** Objects that add properties along the same path can share Maps and descriptor arrays, while adding a property in the middle of an established path creates a branch and can duplicate later structure. This qualifies any blanket claim that property addition itself is the priced event: predictable transitions are part of the optimized design. [quick-win]
3. **Descriptor sharing separates layout identity from repeated metadata.** Several Maps can share one ordered `DescriptorArray` while each Map limits how many descriptors belong to its shape. The mechanism is a compact example of representing related structural states through shared prefixes plus explicit boundaries. [just-a-reference]
4. **A changed field value can invalidate compiled code without changing the object's Map.** TurboFan first embeds a field value treated as constant; assigning a new value produces a `field-const` deoptimization trace, and reoptimization uses the existing Map and backing-store offset instead. This distinguishes field-assumption invalidation from shape transition and prevents the two costs from being collapsed. [quick-win]
5. **The trace demonstrates dependency invalidation, not the general adequacy of a fixed-shape idealization.** It establishes that V8 records and withdraws optimized assumptions when their basis changes. Whether such changes are frequent, bounded, or subordinate in a declared domain remains a separate assessment. [deep-dive]

## Limitations (our opinion)

The page is official implementation documentation and therefore strong evidence about the illustrated mechanisms, but it is a single maintainer-side walkthrough rather than a benchmark or systematic study. It reports no workload distribution, frequency, latency, memory cost, version comparison, competing-engine baseline, or production outcome. The page also warns that the internals are subject to change. Its examples therefore establish that a runtime charge exists, not how large or representative that charge is.

The sharpest trace concerns mutation of an existing field that TurboFan had treated as constant. That assignment invalidates a field-value assumption without demonstrating a Map transition. The later example says changing the global to an object of a different class also deoptimizes code, but the page does not demonstrate that every property addition, deletion, or shape change invalidates every dependent function. V8 deliberately supports and shares predictable transitions, so the source should not be generalized into a claim that all JavaScript mutation is exceptional or slow.

## Recommended Next Action

Update [Instantiation alone cannot model agent learning across sessions](../notes/instantiation-alone-cannot-model-agent-learning-across-sessions.md) to cite this ingest directly for its old-shape specialization analogy, while retaining the broader Fast Properties ingest for the surrounding runtime-cost account.
