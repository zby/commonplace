INFO

The ASCII diagram comparing ephemeral and accumulating pipelines is minimal and clarifying:

```
Ephemeral:     generate -> execute -> discard
Accumulating:  generate -> execute -> save -> test -> version -> reuse
```

Deleting it would lose the at-a-glance comparison of pipeline lengths. It is doing real work (showing the structural difference in steps), not decorating prose. No equations or formal notation present.