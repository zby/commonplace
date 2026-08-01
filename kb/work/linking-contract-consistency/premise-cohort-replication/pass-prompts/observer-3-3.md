You are an independent observer in a frozen semantic-replication experiment.

Read only the packet files named in this prompt under the fixture root. Do not read any other files, inspect the Commonplace checkout, search the filesystem, or use the network. Do not infer or assign a relationship label. Do not discuss a taxonomy, prior policy, current footer, cohort, or expected result.

For each packet, return exactly one compact JSON object on one line with keys `id`, `assertion`, `follow`, `reconsider_rejected`, `reconsider_changed`, `edge_disposition`, `sentence`, `confidence`, and `justification`. Use the packet's neutral identifier. `confidence` must be `high`, `medium`, or `low`; `edge_disposition` must be one of `mechanically-discoverable`, `connective-prose-only`, or `no-useful-connection`. Do not wrap the JSONL in Markdown fences.

For each case: read Artifact A and Artifact B. Report (1) the particular assertion in A that makes B potentially relevant; (2) why a reader of A would follow B, if at all; (3) what the author of A should reconsider if B's central claim were rejected, and if B's contents, implementation, or availability materially changed, where applicable; (4) whether the relationship deserves a mechanically discoverable edge, belongs only in connective prose, or supplies no useful connection; (5) one short sentence with A as grammatical subject describing what A asserts about B; and (6) confidence with a concise justification grounded in both artifacts. Preserve uncertainty instead of guessing.

Packets for this pass:
- packets/case-1989c918c7946c.md
- packets/case-2632bc38d6c3e7.md
- packets/case-f88ac900b7b30e.md
- packets/case-30111db7b8e1ad.md
- packets/case-fa13dc1364da68.md
- packets/case-c3ffb8d4901349.md
- packets/case-3f238a6bfb20f0.md
- packets/case-f2af1a1b9045ca.md
- packets/case-c299eb39a9c550.md
- packets/case-9a724e4374e080.md
- packets/case-6152a54e6a18c8.md
- packets/case-15b46d34f5e07e.md
- packets/case-0f41b0d385292b.md
- packets/case-93f1ff2073f163.md
- packets/case-d45ce3e679afe0.md
- packets/case-394ae9372bce28.md
- packets/case-92aa92d533a0f1.md
- packets/case-41428517ec8382.md
- packets/case-a627c01cfeb3e0.md
- packets/case-cbbd1d7667e81e.md
- packets/case-c34b3568d535fc.md
- packets/case-5996d10a688230.md
- packets/case-5ca86f39e5b984.md
- packets/case-10d4bb9800d9e7.md
- packets/case-04324ff043d41a.md
- packets/case-cacf9c28c10bff.md
