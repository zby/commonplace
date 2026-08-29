# Reports

Analytical outputs, evaluation records, and local operational evidence. Read
[COLLECTION.md](./COLLECTION.md) before adding an artifact: the first-level
directory is its retention contract.

| Area | Meaning |
|---|---|
| [`cache/`](./cache/README.md) | Ignored outputs that are safe to delete and regenerate. |
| [`state/`](./state/README.md) | Ignored operational evidence and state whose owning workflow controls cleanup. |
| [`retained/`](./retained/README.md) | Durable report records kept with the project. |
| [`types/`](./types/) | Collection-local report type contracts. |

The collection is excluded from the published site and its generated directory
indexes. Retained reports remain available in the repository and can be cited
when another artifact needs their exact record.
