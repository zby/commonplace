"""Review workflows over the headless runtime, with plain result files instead of a store.

``criteria`` resolves criterion requests (catalog gates, bundles and the
``type``, ``collection`` and ``critique`` lenses) into the applicable (note,
criterion) pairs; a criterion is named by its artifact identity, so library
files of an installed project work as this checkout's kb/ does. ``outcomes``
is the strict result-line parser. ``results`` is the durable state: one file
per reviewed pair carrying the hashes of the texts it was produced from, and
the pure freshness, status and summary functions over those files. ``gates``
is the first workflow: the gate sweep that asks a worker per stale pair and
writes those files.
"""
