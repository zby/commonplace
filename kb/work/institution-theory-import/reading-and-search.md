# Reading and search record

Initial pass: 2026-09-19. This is a selective working bibliography, not a systematic review or a set of tracked ingests. Reading depth below is literal: inspecting relevant sections does not mean checking every proof. Source claims and proposed Commonplace uses are separated. Before durable promotion, retain the necessary source evidence through the source workflow.

## Linked sources

### 1. Goguen and Burstall — Institutions: Abstract Model Theory for Specification and Programming (1992)

[Paper, university-hosted copy](https://courses.grainger.illinois.edu/cs522/sp2016/InstitutionsAbstractModelTheory.pdf); [DOI](https://doi.org/10.1145/147508.147524).

**Read:** abstract and opening sections, journal pp. 95–98, in the initiating conversation; repeat access was intermittent. The author's linked copy is PostScript, unsupported by the browser reader. Later proofs have not been checked.

**Source:** A logic-independent treatment of specification built around signatures, sentences, models, and satisfaction invariant under signature change. The introduction separates specification languages from programming languages and motivates structuring specifications across different logics.

**Candidate use:** Establish the distinction between a specification's class of conforming realizations and an interpreter's choice of realization. The natural-language satisfaction relation remains something we must justify, not something supplied by the framework.

### 2. Diaconescu — Institution Theory

[Author's exposition in the Internet Encyclopedia of Philosophy](https://iep.utm.edu/insti-th/).

**Read:** §§1–2 and §3a–b, including the signature, sentence, model, satisfaction, and semantic-consequence definitions. Used as orientation; primary papers remain the grounding route for adoption.

**Source:** Sentence translation follows signature maps while model reduction runs oppositely. Categories and functors contribute coherence requirements beyond a binary satisfaction relation. The satisfaction condition is an equivalence. A theory's models and the sentences shared by a model class form a Galois connection.

**Candidate use:** A precise checklist for preventing a vocabulary analogy from being mistaken for an institutional construction. The Galois connection concerns semantic consequence under a fixed relation; it does not supply inductive warrant from observed examples.

### 3. Goguen — Institutions (author's project page, last modified 2006)

[Working current host](https://cseweb.ucsd.edu/~goguen/projs/inst.html).

**Read:** motivation, introduction, and annotated local bibliography. Wikipedia's older UCSD hostname failed; the current host succeeded.

**Source:** Goguen explicitly connects institutions to cognitive semantics, ontologies, and theory modularization. The bibliography points to information integration, semiotics, and several distinct notions of mappings between institutions.

**Candidate use:** Follow the author's cognitive-semantic work before asserting that our analogy is novel. Do not copy the page's formulas uncritically: some displayed directions and explanatory prose appear inconsistent. Check formal definitions against the papers.

### 4. Mossakowski, Goguen, Diaconescu, and Tarlecki — What is a Logic?

[Author-hosted manuscript](https://cseweb.ucsd.edu/~goguen/pps/nel05.pdf). Wikipedia cites the 2007 second-edition chapter; the host bibliography describes a 2005 version. The read artifact is the linked manuscript, not a verified match to the later edition.

**Read:** abstract, introduction, and the equivalence/skeleton passage around manuscript p. 9; not the full invariant proofs.

**Source:** The paper proposes equivalence classes of institutions as logics and distinguishes variants with different sentence/model structure. Proof structure can be added; it is not identical to the underlying satisfaction relation.

**Candidate use:** Keep semantic conformance, derivability, and operational checking separate. Do not require a proof-producing interpreter merely because we borrow model-theoretic vocabulary.

### 5. Goguen — Information Integration in Institutions

[Author-hosted manuscript](https://cseweb.ucsd.edu/~goguen/pps/ifi04.pdf), reached through source 3.

**Read:** introduction, database construction around manuscript pp. 26–27, and opening of §3.7, Cognitive Semantics. Remaining constructions and proofs are not audited; publication-version identity remains to be pinned.

**Source:** The paper connects institutional methods with information flow, formal concept analysis, and cognitive semantics. It explicitly declines to identify its mathematical objects with fully adequate representations of human concepts. The cognitive section uses small relational theories for conceptual spaces; semiotic extensions add structure and priorities.

**Candidate use:** A direct precedent for selectively formalizing concepts and their integration. Its explicit adequacy limit supports keeping the human/agent task of choosing a representation outside the formal guarantee.

### Linked papers still at discovery depth

- Goguen and Roşu, [Institution Morphisms (2002)](https://experts.illinois.edu/en/publications/institution-morphisms/): author-university abstract read. The author-linked full text is PostScript. Read the full paper before choosing between morphism and comorphism conventions for a cross-logic translation.
- Sannella and Tarlecki, [Specifications in an Arbitrary Institution (1988)](https://www.sciencedirect.com/science/article/pii/0890540188900089): publisher abstract read. Relevant for specification operations, proof rules, parameterization, and development. No detailed refinement claim rests on it yet.

## Wider search: direct precedents and adjacent alternatives

### 6. Fernando — Types from Frames as Finite Automata (2016)

[Author-hosted published chapter](https://www.scss.tcd.ie/Tim.Fernando/FSM4SAS/E15/fg.pdf), LNCS 9804, pp. 19–40, DOI 10.1007/978-3-662-53042-9_2.

**Read:** abstract, introductory framing, institution/satisfaction passage on printed p. 37, and conclusion on pp. 38–39. Full automata development has not been checked.

**Source:** Constructs an institution for a bounded account of frame semantics. Finite alphabets and associated languages permit variation in descriptive granularity. The institutional construction separates background requirements from a sentence and explicitly checks a satisfaction equivalence using an earlier result.

**Candidate use:** Strongest concrete precedent found in this pass for institution theory applied to natural-language semantics. It demonstrates a scoped construction, not a semantics of unrestricted instructions or a conformance oracle for LLMs. Study its choice of signatures before treating whole prompts as signatures.

**Related lead:** Fernando's *Signatures as Open-Ended Types* (2014), discovered in [conference proceedings](https://citeseerx.ist.psu.edu/document?doi=dde5f9066eacb04f17ba4c25266bc58068bb8df1&repid=rep1&type=pdf). Search extract only: strings and records represent time-as-change and variable adicity. Prefer the inspected 2016 chapter for current claims.

### 7. Copestake, Flickinger, Sag, and Pollard — Minimal Recursion Semantics: An Introduction

[Author-hosted September 1999 draft](https://www.cl.cam.ac.uk/~aac10/papers/newmrs.pdf). A later journal article exists; do not silently cite this draft as that version.

**Read:** abstract and introduction, draft pp. 1–2.

**Source:** MRS represents semantic structures while leaving scope distinctions unresolved and permitting later resolution. The authors describe it as a meta-level representation language rather than a semantic theory in itself. Scope sometimes need not be resolved for the application.

**Candidate use:** Preserve consequential alternatives explicitly instead of assuming that every successful interpreter must choose one complete reading. Scope ambiguity is narrower than the KB's current use of underspecification; it does not cover every open design choice or vague adjective.

### 8. Gómez Álvarez and Bennett — Dealing with Conceptual Indeterminacy: A Framework based on Supervaluation Semantics (2018)

[Workshop paper](https://ceur-ws.org/Vol-2237/womocoe-paper-1.pdf).

**Read:** abstract and §5's standpoint syntax/semantics, especially §§5.1–5.3.

**Source:** A standpoint selects a nonempty set of precisifications; a claim can hold across all compatible precisifications, while a sharper standpoint restricts that set. The paper marks completeness of its proof system as unfinished work.

**Candidate use:** Represent variation in interpretation conventions separately from variation among implementations under one convention. This can express definitely conforming, definitely excluded, and reading-dependent cases once admissible precisifications are supplied. It does not determine their admissibility for Commonplace.

**Later lead:** [How to Agree to Disagree: Managing Ontological Perspectives using Standpoint Logic (2022)](https://arxiv.org/abs/2206.06793), abstract read. Investigate its decidable fragments if a concrete reasoning task emerges; do not generalize fragment results to unrestricted first-order logic.

### 9. Goguen — Semiotics, Compassion and Value-Centered Design

[Author-hosted article](https://cseweb.ucsd.edu/~goguen/papers/reading.html).

**Read:** introduction and §2, Algebraic Semiotics; publication identity/date still needs verification for durable citation.

**Source:** Semiotic morphisms preserve selected properties of structured sign systems and may be partial. Context and human interpretation remain necessary to deploy the formalism. A table of contents illustrates useful preservation of organization while omitting content.

**Candidate use:** Potentially better than full satisfaction equivalence for summaries, indexes, and task-shaped extraction. A preservation contract must name what matters to the consumer. This is adjacent to institution theory, not permission to call every lossy rewrite an institution morphism.

### 10. Veltman — Defaults in Update Semantics (1996)

[Author-uploaded text and abstract](https://www.researchgate.net/publication/225817706_Defaults_in_Update_Semantics); [PDF mirror](https://www.blutner.de/Logica/Texte/dius.pdf), DOI 10.1007/BF00248150.

**Read:** abstract and indexed opening passage (§1.1) of the author-uploaded text. PDF reader access was intermittent and did not support a reliable section read.

**Source:** Treats default reasoning through update semantics. The opening distinguishes additive updates from broader possibilities and discusses reference and presupposition as difficulties for a simple addition picture.

**Candidate use:** A comparator when extra context revises a reading rather than merely extending notation or adding a fixed constraint. Keep as a targeted next read, not an established explanation of LLM context effects.

## Search record and selection

Queries included `Institution morphisms Goguen Rosu pdf`, `Specifications in an arbitrary institution pdf`, `Goguen institutions natural language semantics semiotics context`, `natural language underspecified semantics supervaluation institution theory`, `Minimal Recursion Semantics Copestake Flickinger Pollard Sag 2005 pdf`, `Veltman 1996 defaults update semantics pdf`, `institution natural language semantics Goguen`, `standpoint logic semantic variability decidability`, and `Tim Fernando institution types natural language 2014`.

Selection followed three questions: is there a direct natural-language institutional construction; what distinguishes open realizations from open readings; and what accounts for context or selective preservation? Author-hosted papers, publisher abstracts, and research proceedings were preferred. The broad search also returned distributional vector semantics and ML pipeline underspecification; these were left out because they address different relations from instruction conformance. Recent defeasible standpoint papers remain search leads only; recency alone did not justify extending this pass.

## Read next only to resolve a named question

| Question | Best next source/action |
|---|---|
| How can a bounded semantic background form a signature? | Work through Fernando §4 and its dependence on earlier facts |
| What exactly must a cross-logic translation preserve? | Obtain and read Goguen–Roşu's full morphisms paper |
| Which specification changes are refinements? | Read Sannella–Tarlecki beyond the abstract |
| Can context revision fit our proposed maps? | Read Veltman §1 and test an explicit default-retraction example |
| How should competing public readings be represented? | Compare the standpoint construction with one real ambiguous Commonplace instruction |

Stop expanding the bibliography when the next source does not discriminate between candidate imports. The [assessment](./import-assessment.md) supplies the first bounded case.
