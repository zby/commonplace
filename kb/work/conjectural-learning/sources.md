# Source register

Modern-paper coverage on 2026-09-19, including the expansion below: twelve
full texts, two author abstracts, and one bibliographic-only record.
Each ingest records source metadata and the SHA-256 of its paired snapshot.
Empty Quotes sections mean detailed source claims require those snapshots.

| Paper | Retained analysis and scope |
|---|---|
| Huang et al. 2025, *Automated Hypothesis Validation with Agentic Sequential Falsifications* | [POPPER ingest](../../sources/automated-hypothesis-validation-sequential-falsifications.ingest.md): arXiv v1, 65 pages |
| Thomas 2025, *Towards Error Centric Intelligence I, Beyond Observational Learning* | [Ingest](../../sources/error-centric-intelligence-beyond-observational-learning.ingest.md): arXiv v1, 33 pages |
| Mills & Lewis 2025, *Think Before You Act: Popperian Expectations for Adaptive Agents* | [Abstract ingest](../../sources/think-before-you-act-popperian-expectations-abstract.ingest.md): author-lab abstract, not the six-page paper |
| Salmani & Lewis 2025, *A Reflective Architecture for LLM-Based Systems* | [Abstract ingest](../../sources/reflective-architecture-llm-based-systems-abstract.ingest.md): author-lab abstract, not the eight-page paper |
| Zhang et al. 2025, *Exploring the role of large language models in the scientific method: from hypothesis to discovery* | [Ingest](../../sources/llms-scientific-method-hypothesis-to-discovery.ingest.md): publisher version of record, 2025-08-05, 15 pages |
| Mills & Lewis 2026, *Popperian Expectations for One-Shot Adaptation in Dynamic Environments* | [Conference listing](https://2026.acsos.org/details/acsos-2026-workshops/16/Popperian-Expectations-for-One-Shot-Adaptation-in-Dynamic-Environments): no substantive text, no ingest |
| İşcan 2026, *Scaffold, Not Vocabulary? A Controlled, Two-Tier, Pre-Registered Study of a Popperian Code-Generation Skill* | [Ingest](../../sources/scaffold-not-vocabulary-popperian-code-generation-skill.ingest.md): arXiv v1, 34 pages |

## 2026 expansion

All eight captures retain full PDF text. Detailed evidence and limitations
belong in the ingests; [comparison](./comparison.md) keeps only what matters
to this workshop.

| Paper | Retained analysis and version |
|---|---|
| Takahara & Mizoguchi, *Toward Auditable AI Scientists* | [HEP](../../sources/hypothesis-evolution-protocol-auditable-ai-scientists.ingest.md): arXiv 2607.09195v1 |
| Zeng et al., *Socratic agents for autonomous scientific discovery in high-dimensional physical systems* | [AHOIS](../../sources/socratic-agents-autonomous-scientific-discovery.ingest.md): arXiv 2606.26722v1 main paper; referenced supplement absent |
| İşcan, *Form, Not Content?* | [PoPE](../../sources/form-not-content-placebo-controlled-self-repair.ingest.md): arXiv 2607.12962v1 |
| Ríos-García et al., *AI scientists produce results without reasoning scientifically* | [Ingest](../../sources/ai-scientists-results-without-scientific-reasoning.ingest.md): arXiv 2604.18805v1 |
| İşcan, *Selection Without Signal, Recovery Through Expression* | [Ingest](../../sources/selection-without-signal-recovery-through-expression.ingest.md): arXiv 2606.16999v1 |
| Fa & Culjak, *Sound Agentic Science Requires Adversarial Experiments* | [Ingest](../../sources/sound-agentic-science-requires-adversarial-experiments.ingest.md): arXiv 2604.22080v2 |
| Bertolazzi, Tentori & Bernardi, *FALSIFYBENCH* | [Full-text ingest](../../sources/falsifybench-rule-discovery-games-full-text.ingest.md): arXiv 2606.04751v1; the [earlier abstract observation](../../sources/falsifybench-inductive-reasoning-rule-discovery-games.ingest.md) is preserved |
| Lu et al., *The Meta-Agent Challenge: Are Current Agents Capable of Autonomous Agent Development?* | [Ingest](../../sources/meta-agent-challenge-autonomous-agent-development.ingest.md): arXiv 2606.04455v1 |

## Access disposition

For the two IEEE papers, publisher pages required JavaScript verification and
PDF requests returned HTTP 418. Author pages supplied only abstracts and DOIs.
OpenAlex and Semantic Scholar exposed no open copy; Crossref supplied only
similarity-checking URLs. Ontario Tech repository, exact-title, author,
arXiv, and PDF searches found no accessible manuscript. This does not establish
that none exists.

For the 2026 paper, the conference listing, [SISSY programme](https://sissy-workshop.github.io/),
and [author news](https://www.trustworthyai.ca/news/john-ronika-nathan-and-peter-present-at-acsos-2026/)
confirmed presentation and authorship. The public programme repository had no
PDF; Crossref did not resolve an exact record. No authors were contacted.

Compare the two abstracts only at their stated scope; exclude the 2026 paper
from mechanism and outcome claims. New full-paper captures would be distinct
observations and reopen those comparisons. These gaps limit implementation
judgments, not the primary Popper foundation.

## Primary foundations

The paired snapshots of [A Realist View](../../sources/popper-a-realist-view-of-logic-physics-and-history-1966.ingest.md)
and [Conjectures and Refutations](../../sources/popper-conjectures-and-refutations.ingest.md)
were read at the locators in [Popper foundation](./popper-foundation.md).
[Epistemology Without a Knowing Subject](../../sources/popper-epistemology-without-a-knowing-subject-1968.ingest.md)
adds the complete 1968 publication, pp. 333–373, from the operator's downloaded
PDF. Eight verified extracts now ground formulation in language, informal
criticism, feedback to action, the distinction between potential
intelligibility and actual use, conscious criticism, and mutual criticism.
This is a third primary Popper observation, separate from the modern papers.
EITHER and FORTE supply the classical precedent cited in the drafts.

## Verification scope and limits

Source claims and identities were checked against the pinned snapshots during
ingestion. The eight expansion captures were analyzed by fresh source
workers; that is source analysis, not independent review of the workshop.
The access search above has not been repeated. No experiments have been
reproduced.

Eight retained extracts from the 1968 essay and two from *Conjectures and
Refutations* were added through the grounding workflow and checked against
the snapshots. The draft quotation audit checked every verbatim quotation
against retained extracts and locators. The 2026-09-21 capacity and
observer-access review also checked the relevant 1968 snapshot passages;
it did not recheck all source claims. Earlier reviews do not certify later
edits.

Workshop files, expansion ingests, and connection reports passed deterministic
validation at ingestion. Snapshot validation retains a known
`validation.schema.body-dates-1` false positive: the bibliography DOI
`10.1186/1471-2288-13-91` is mistaken for a date in *Scaffold, Not Vocabulary?*,
*Form, Not Content?*, and *Selection Without Signal*. Captured bytes were
preserved. Validation supplies no evidence for the workshop's empirical
conjectures.

Connection reports for the new ingests are in
`kb/reports/cache/connect/sources/`, named by source slug.
