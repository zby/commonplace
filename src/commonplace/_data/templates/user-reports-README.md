# Reports

Analytical outputs, evaluation records, and local operational evidence. Read
[COLLECTION.md](./COLLECTION.md) before adding an artifact: the first-level
directory is its retention contract.

| Area | Meaning |
|---|---|
| [`cache/`](./cache/README.md) | Ignored outputs safe to delete and regenerate. |
| [`state/`](./state/README.md) | Ignored operational evidence and state with workflow-owned cleanup. |
| [`retained/`](./retained/README.md) | Durable report records kept with the project. |
| [`types/`](./types/) | Collection-local report type contracts. |
