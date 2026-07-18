# Review: frontmatter/title-as-claim

## titleclaim-A
### Findings
- Title "Index staleness" is a topic label, not a proposition. It names a subject area; it states nothing that could be true or false. The note carries the `title-as-claim` trait, and the body clearly argues a claim (the description even states it: a stale index suppresses search while absence degrades to search), but the title does not assert it.
## Result: WARN

## titleclaim-B
### Findings
- none — "Stale indexes are worse than no indexes" is a complete proposition that could be true or false, and it matches the note's central asymmetry argument.
## Result: PASS

## titleclaim-C
### Findings
- Title "Reflection and addressability" is an "X and Y" topic pairing, not an assertion. Nothing in the title could be true or false. The note carries the `title-as-claim` trait and the body defends a specific comparative claim (reflection's distinctive affordance is addressability, not compounding), but the title reads as a chapter heading.
## Result: WARN

## titleclaim-D
### Findings
- Title "KB index maintenance" is a category/topic name — a navigation-style heading, not a proposition. The trait promises a claim; the title states nothing that could be true or false, despite the body arguing a definite asymmetry claim.
## Result: WARN

## titleclaim-E
### Findings
- none — "Warranted autonomy is bounded by oracle domain" is a concrete proposition that could be true or false, and it is the thesis the body develops.
## Result: PASS

## titleclaim-F
### Findings
- Title "Addressability in self-improving systems" is a topic-scoping label ("X in Y"), not an assertion. It names where the discussion happens rather than stating anything that could be true or false, so it does not fulfill the `title-as-claim` trait's promise.
## Result: WARN
