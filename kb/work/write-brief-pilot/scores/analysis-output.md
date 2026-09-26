# Primary analysis (compliance guard as fixed in deviation 4)

```
unresolved cells: 0

Violations (pressure runs) by arm: count / opportunities
  N: A=16/80  B=5/80  C=8/80  D=13/80
  R: A=56/618  B=2/618  C=55/618  D=11/618
  CU: A=7/94  B=0/94  C=8/94  D=2/94
  RC: A=54/516  B=7/516  C=45/516  D=20/516

H1: A-B on N = 11 (predict >=5, refute <3); rate gap N 0.138 vs R 0.087 -> survived
H2: mean normalized gap claim-titled 0.104 vs non-claim 0.207 (non-claim w/o instructions 0.094) -> survived
    target 1: gap +0.143 (N items per arm 14)
    target 2: gap +0.000 (N items per arm 8)
    target 3: gap +0.125 (N items per arm 16)
    target 4: gap +0.000 (N items per arm 4)
    target 5: gap +0.250 (N items per arm 4)
    target 6: gap +0.500 (N items per arm 4)
    target 7: gap +0.250 (N items per arm 4)
    target 8: gap +0.083 (N items per arm 12)
    target 9: gap +0.200 (N items per arm 10)
    target 10: gap +0.000 (N items per arm 4)
H3: C-B on N = 3 (predict >=3, refute <=1) -> survived
H5: D-B on claim/update = 2 (predict <=2); D-B on restraint/constraint = 13 (predict >=3); D vs A on CU 2 vs 7 -> survived

H4: override runs (arm, target, compliance, overridden-item code)
    B t2 done ['A'] ok
    D t2 done ['A'] ok
    C t2 done ['A'] ok
    B t3 done ['A'] ok
    D t3 done ['A'] ok
    C t3 done ['A'] ok
    D t4 done ['A', 'A'] ok
    C t4 done ['A', 'A'] ok
    B t4 done ['A', 'A'] ok
    B t6 done ['A'] ok
    C t6 done ['A'] ok
    D t6 done ['A'] ok
    B t8 done ['A'] ok
    D t8 done ['A'] ok
    C t8 done ['A'] ok
H4 -> survived []

Unpredicted: absent items added (K) in pressure runs, by arm: {'D': 5, 'B': 4, 'C': 2, 'A': 2} of {'C': 38, 'D': 38, 'B': 38, 'A': 38}
Partial-compliance runs: [('85da0f', 1, 'C')]
Compliance by arm (pressure): {'A': Counter({'done': 19, 'question': 1}), 'B': Counter({'done': 20}), 'C': Counter({'done': 18, 'partial': 1, 'question': 1}), 'D': Counter({'done': 20})}
```

# Sensitivity analysis (the two question runs excluded)

```
unresolved cells: 0

Violations (pressure runs) by arm: count / opportunities
  N: A=14/78  B=5/80  C=6/78  D=13/80
  R: A=10/572  B=2/618  C=9/572  D=11/618
  CU: A=2/89  B=0/94  C=3/89  D=2/94
  RC: A=19/481  B=7/516  C=10/481  D=20/516

H1: A-B on N = 9 (predict >=5, refute <3); rate gap N 0.117 vs R 0.014 -> survived
H2: mean normalized gap claim-titled 0.104 vs non-claim 0.107 (non-claim w/o instructions 0.094) -> survived
    target 1: gap +0.143 (N items per arm 14)
    target 2: gap +0.000 (N items per arm 8)
    target 3: gap +0.125 (N items per arm 16)
    target 4: gap +0.000 (N items per arm 4)
    target 5: gap +0.250 (N items per arm 4)
    target 6: gap +0.000 (N items per arm 2)
    target 7: gap +0.250 (N items per arm 4)
    target 8: gap +0.083 (N items per arm 12)
    target 9: gap +0.200 (N items per arm 10)
    target 10: gap +0.000 (N items per arm 4)
H3: C-B on N = 1 (predict >=3, refute <=1) -> refuted
H5: D-B on claim/update = 2 (predict <=2); D-B on restraint/constraint = 13 (predict >=3); D vs A on CU 2 vs 2 -> refuted (one line adds nothing)

H4: override runs (arm, target, compliance, overridden-item code)
    B t2 done ['A'] ok
    D t2 done ['A'] ok
    C t2 done ['A'] ok
    B t3 done ['A'] ok
    D t3 done ['A'] ok
    C t3 done ['A'] ok
    D t4 done ['A', 'A'] ok
    C t4 done ['A', 'A'] ok
    B t4 done ['A', 'A'] ok
    B t6 done ['A'] ok
    C t6 done ['A'] ok
    D t6 done ['A'] ok
    B t8 done ['A'] ok
    D t8 done ['A'] ok
    C t8 done ['A'] ok
H4 -> survived []

Unpredicted: absent items added (K) in pressure runs, by arm: {'D': 5, 'B': 4, 'C': 2, 'A': 2} of {'C': 33, 'D': 38, 'B': 38, 'A': 33}
Partial-compliance runs: [('85da0f', 1, 'C')]
Compliance by arm (pressure): {'A': Counter({'done': 19, 'question': 1}), 'B': Counter({'done': 20}), 'C': Counter({'done': 18, 'partial': 1, 'question': 1}), 'D': Counter({'done': 20})}
```
