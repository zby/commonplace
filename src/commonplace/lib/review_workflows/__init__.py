"""Review workflows over the headless runtime, with plain result files instead of a store.

``criteria`` resolves criterion requests (catalog gates, bundles and the
``type``, ``collection`` and ``critique`` lenses) into the applicable (note,
criterion) pairs; a criterion is named by its artifact identity, so library
files of an installed project work as this checkout's kb/ does. ``results``
is the durable state: one file per reviewed pair carrying the hashes of the
texts it was produced from, and the pure freshness, status and summary
functions over those files. ``gates`` is the gate sweep that asks workers for
the stale pairs, one call per pair or per note and bundle, and writes those
files. ``edit_operations`` runs one edit operation on one text. ``revise`` is
the one runner of the improvement procedures: it executes a plan of edit
operations to its first stop, publishes what it applied and records the
work left in a continuation record. ``decisions`` keeps and lists the
operator's answers files and the runs' publications.
"""
