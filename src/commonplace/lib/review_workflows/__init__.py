"""Review workflows over the headless runtime, with plain result files instead of a store.

``results`` is the durable state: one file per reviewed (note, criterion)
pair carrying the hashes of the texts it was produced from, and the pure
freshness and status functions over those files. ``gates`` is the first
workflow: the gate sweep that asks a worker per stale pair and writes those
files.
"""
