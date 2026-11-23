# Workflow state

Use this collection to inspect or continue a workflow; see the [collection contract](./COLLECTION.md) for ownership and cleanup. Citable reports belong in the [reports collection](../reports/README.md).

Search `data/current/<workflow>/` for new runs. The main repository ignores `data/`; a clean clone need not contain it. When the separate state checkout is present, siblings of `current/` hold historical records. They retain their original paths in the text and are not resumable runs.
