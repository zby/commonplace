# Compact evidence retention for the premise-cohort replication

The complete local run occupies approximately 8.9 MB. About 7.3 MB (7.1 MiB on disk) is raw CLI event output: approximately 6.9 MB under `raw-observer/` and 363 KB under `raw-mapper/`. Those streams largely repeat packet or normalized response content and are useful mainly for reconstructing tool-read traces.

## Version-controlled evidence bundle

Retain every run artifact except the successful `raw-observer/` and `raw-mapper/` streams. Keep the two malformed mapper attempts and their stderr companions because the amendments and retry-sensitivity calculation depend on them. The resulting 141-file bundle is approximately 1.7 MB and preserves:

- the frozen protocol, prompts, pass prompts, model provenance, amendments, and post-run audit;
- the exact sanitized packets and their source/target transformation digests;
- all 234 normalized observer records and all 234 scored mapper records;
- the manifest, aggregation, full case ledger, parse-failure record, malformed mapper attempts, and result report;
- the synthetic sanitizer check and summarized read-trace audit.

This is enough to inspect every scored input and normalized answer, recompute the result and retry sensitivity, inspect the malformed mapper attempts, and identify the omitted successful raw outputs by digest. It is not enough to independently reconstruct every tool event; that limitation is stated in the result and post-run audit.

## Local-only evidence

Keep the ignored successful streams under `raw-observer/` and `raw-mapper/` locally until the workshop closes or the maintainer explicitly archives or discards them. `pass-provenance.jsonl` retains SHA-256 digests for the successful and failed raw streams, so any later copy can be checked against this run.

The run-local `.gitignore` prevents accidental staging of successful raw streams while allowing the two failed attempts into the compact bundle. It does not delete anything. If full trace-level auditability later becomes a requirement, remove the ignore rules and commit or externally archive the raw directories deliberately.
