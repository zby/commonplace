---
source: https://arxiv.org/html/2603.27116v1
description: Formal no-escape theorem paper arguing semantic memory systems face interference-driven forgetting and false recall under finite effective dimensionality.
captured: 2026-04-10
capture: html-lynx
type: kb/sources/types/snapshot.md
tags: [academic-paper]
---

# The Price of Meaning: Why Every Semantic Memory System Forgets

Author: Sambartha Ray Barman, Andrey Starenky, Sofia Bodnar, Nikhil Narasimhan, Ashwin Gopinath
Source: https://arxiv.org/html/2603.27116v1
Date: 2026-03-28

   License: CC BY 4.0
   arXiv:2603.27116v1 [cs.AI] 28 Mar 2026

The Price of Meaning: Why Every Semantic Memory System Forgets

   Sambartha Ray Barman Sentra, 235 2nd Street, San Francisco, CA 94105, USA Andrey Starenky Sentra, 235 2nd
   Street, San Francisco, CA 94105, USA Sofia Bodnar Sentra, 235 2nd Street, San Francisco, CA 94105, USA Nikhil
   Narasimhan Sentra, 235 2nd Street, San Francisco, CA 94105, USA Ashwin Gopinath Corresponding author:
   agopi@mit.edu, ashwin@sentra.app Sentra, 235 2nd Street, San Francisco, CA 94105, USA Department of Mechanical
   Engineering, Massachusetts Institute of Technology, 77 Massachusetts Avenue, Cambridge, MA 02139, USA

Abstract

   Every major AI memory system in production today, from vector databases to RAG pipelines to the weights of
   large language models, organises information by meaning. That organisation is what makes these systems useful:
   it lets them generalise, draw analogies, and retrieve by concept rather than by keyword. But it comes at a
   price. We show that the same geometric structure that enables semantic generalisation also makes interference,
   forgetting, and false recall inescapable. Here we formalise and test that tradeoff for a broad class of
   semantically continuous kernel-threshold memories: systems whose retrieval score is a monotone function of an
   inner-product in a semantic feature space, whose representations are learned under a rate or distortion budget,
   and whose semantic manifold has finite local intrinsic dimension.

   Within this class, we derive four results. First, semantically useful representations have finite semantic
   effective rank. Second, finite local dimension implies positive competitor mass in retrieval neighbourhoods.
   Third, under growing memory, retention decays to zero; with power-law arrival statistics and population
   heterogeneity, this yields population-level power-law forgetting curves. Fourth, for associative lures
   satisfying a
   [MATH: <semantics><mi>δ</mi><annotation encoding="application/x-tex">\delta</annotation></semantics> :MATH]
   -convexity condition below the decision margin, false recall cannot be eliminated by threshold tuning within
   the same score family.

   We then test these predictions across five memory architectures: vector retrieval, graph memory,
   attention-based retrieval, BM25-based filesystem retrieval, and parametric memory. Pure semantic retrieval
   systems express the geometric vulnerability directly as forgetting and false recall. Systems with explicit
   reasoning can partially override these symptoms behaviourally, but convert smooth degradation into brittle
   failure modes. Systems that escape interference completely do so by sacrificing semantic generalisation.

   The result is not an argument against scale. It is an argument that scale alone is not enough. Making a vector
   database ten times larger, an LLM ten times bigger, or an embedding space ten times wider does not remove the
   interference; it moves the system along a tradeoff surface where forgetting and usefulness are coupled. For
   memory, progress requires not only scale but new architectures, training objectives, and
   interference-management mechanisms. The price of meaning is interference, and no architecture we tested avoids
   paying it.

   Organising memory by meaning makes forgetting and false recall inevitable. Scaling up does not fix it.

Introduction

   Every deployed retrieval-augmented generation system, every long-term agent memory, and every knowledge graph
   built on dense embeddings shares a design choice: organise information by meaning. Items that are semantically
   related sit near each other in representation space. This is what makes these systems capable of
   generalisation, analogy, and conceptual transfer rather than mere keyword lookup. But it also means that when
   the system tries to retrieve one memory, its semantic neighbours compete for the same retrieval slot. That
   competition is interference, and this paper asks whether any semantic memory system can avoid it.

   Our previous work, HIDE^3, showed that one simple retrieval architecture (cosine similarity over sentence
   embeddings) reproduces several canonical memory phenomena, including forgetting under interference (
   [MATH:
   <semantics><mrow><mi>b</mi><mo>=</mo><mrow><mn>0.460</mn><mo>±</mo><mn>0.183</mn></mrow></mrow><annotation
   encoding="application/x-tex">b=0.460\pm 0.183</annotation></semantics> :MATH]
   ), DRM-style false recall (
   [MATH: <semantics><mrow><mtext>FA</mtext><mo>=</mo><mn>0.583</mn></mrow><annotation
   encoding="application/x-tex">\text{FA}=0.583</annotation></semantics> :MATH]
   ), spacing effects, and tip-of-tongue states (
   [MATH: <semantics><mrow><mn>3.66</mn><mo>%</mo></mrow><annotation
   encoding="application/x-tex">3.66\%</annotation></semantics> :MATH]
   ). (We note that different dimensionality estimators yield different values for the same model (participation
   ratio
   [MATH: <semantics><mrow><mi></mi><mo>≈</mo><mn>158</mn></mrow><annotation encoding="application/x-tex">\approx
   158</annotation></semantics> :MATH]
   , Levina–Bickel
   [MATH: <semantics><mrow><mi></mi><mo>≈</mo><mn>10.6</mn></mrow><annotation encoding="application/x-tex">\approx
   10.6</annotation></semantics> :MATH]
   , PCA-projected
   [MATH: <semantics><mrow><mi></mi><mo>≈</mo><mn>16</mn></mrow><annotation encoding="application/x-tex">\approx
   16</annotation></semantics> :MATH]
   ), a discrepancy we reconcile in the Dimensionality section; all place these systems in the
   interference-vulnerable regime.) The natural objection is architectural: perhaps those phenomena are artefacts
   of one particular embedding-and-threshold system rather than consequences of semantically organised memory more
   broadly.

   This paper addresses that objection. We identify a theorem class, semantically continuous kernel-threshold
   memories, within which interference is not a bug of one architecture, but a structural consequence of semantic
   organisation under finite effective dimensionality. We then show empirically that related pressures appear
   across multiple modern memory architectures, even when their behavioural expression differs. This paper argues
   that within a broad and practically important theorem class, these phenomena follow from the structure of
   semantically organised retrieval itself.

   We call a memory system semantically useful if it supports retrieval by conceptual relatedness rather than
   exact lexical identity alone. This is a functional definition: the target regime is memory that supports
   inference, analogy, and conceptual transfer. The theorem developed here applies not to all possible memories,
   but to a specific class of semantically continuous retrieval systems.

   To obtain fully rigorous results, we make explicit the theorem class. Our proofs apply to semantically
   continuous kernel-threshold memories: systems whose retrieval rule is a monotone function of an inner-product
   score in a semantic feature space (Axiom A1), whose semantically useful representation is optimised under a
   rate or distortion budget (Axiom A3), and whose semantic manifold has finite local intrinsic dimension
   (Axiom A4). This class includes dense vector retrieval, embedding-based graph memory, and hidden-state
   similarity retrieval. Architectures equipped with an external symbolic verifier or exact episodic record fall
   outside this theorem class and are treated separately as behavioural workarounds rather than counterexamples.

   The claim is therefore not that every conceivable memory system must exhibit the same behavioural signatures.
   It is that a large and practically central class of modern memory systems inherits a common geometric
   vulnerability. Architectures can differ in how they express that vulnerability, and some can partially
   compensate for it behaviourally, but those compensations are not free.

   We close the gap with four theorems and a unifying No-Escape Theorem. Within the kernel-threshold theorem
   class, any system satisfying Axioms A1–A5 exhibits interference-driven forgetting, false recall, and partial
   retrieval states. The logical chain is: semantic kernel
   [MATH: <semantics><mo>+</mo><annotation encoding="application/x-tex">+</annotation></semantics> :MATH]
   rate-distortion optimality
   [MATH: <semantics><mo stretchy="false">⇒</mo><annotation
   encoding="application/x-tex">\Rightarrow</annotation></semantics> :MATH]
   finite semantic effective rank (Theorem 1)
   [MATH: <semantics><mo stretchy="false">⇒</mo><annotation
   encoding="application/x-tex">\Rightarrow</annotation></semantics> :MATH]
   positive cap mass (Theorem 2)
   [MATH: <semantics><mo>+</mo><annotation encoding="application/x-tex">+</annotation></semantics> :MATH]
   growing memory
   [MATH: <semantics><mo stretchy="false">⇒</mo><annotation
   encoding="application/x-tex">\Rightarrow</annotation></semantics> :MATH]
   inevitable forgetting (Theorem 3); power-law arrival
   [MATH: <semantics><mo>+</mo><annotation encoding="application/x-tex">+</annotation></semantics> :MATH]
   population heterogeneity
   [MATH: <semantics><mo stretchy="false">⇒</mo><annotation
   encoding="application/x-tex">\Rightarrow</annotation></semantics> :MATH]
   power-law forgetting curve. Independently: associative
   [MATH: <semantics><mi>δ</mi><annotation encoding="application/x-tex">\delta</annotation></semantics> :MATH]
   -convexity
   [MATH: <semantics><mo stretchy="false">⇒</mo><annotation
   encoding="application/x-tex">\Rightarrow</annotation></semantics> :MATH]
   lure inseparability under threshold tuning (Theorem 4) (Fig. 1). We verify every link empirically across five
   architecturally distinct memory systems: a vector database (BGE-large^21), an attention-based context window
   (Qwen2.5-7B^13), a filesystem agent memory with BM25
   [MATH: <semantics><mo>+</mo><annotation encoding="application/x-tex">+</annotation></semantics> :MATH]
   LLM re-ranking, a graph memory with PageRank (MiniLM^15; similar contrastive architectures underpin CLIP^14),
   and parametric knowledge in LLM weights. The effective dimensionality convergence (from
   [MATH:
   <semantics><mrow><msub><mi>d</mi><mtext>nom</mtext></msub><mo>=</mo><mrow><mn>3</mn><mo>,</mo><mn>584</mn></mro
   w></mrow><annotation encoding="application/x-tex">d_{\text{nom}}=3{,}584</annotation></semantics> :MATH]
   to
   [MATH: <semantics><mrow><msub><mi>d</mi><mtext>eff</mtext></msub><mo>=</mo><mn>17.9</mn></mrow><annotation
   encoding="application/x-tex">d_{\text{eff}}=17.9</annotation></semantics> :MATH]
   for Qwen hidden states) mirrors the low-dimensional structure in biological neural populations^19, 7.

   We emphasise what the theorem does not say. It bounds the existence of these phenomena, not their magnitude.
   Engineering can and should optimise parameters to minimise unwanted interference; the gap between “inevitable”
   and “catastrophic” is where engineering contributes. The forgetting exponent, the false alarm rate, and the TOT
   probability are continuous functions of system parameters; the theorem says these functions are bounded away
   from zero for systems in the kernel-threshold theorem class satisfying Axioms A1–A5. Murdock’s serial position
   effect^11, Cepeda et al.’s^6 distributed practice findings, Brown and McNeill’s^5 tip-of-tongue phenomenology,
   and Nadel and Moscovitch’s^12 consolidation theory all describe the same geometric substrate from different
   vantage points. The most important finding is not that all five architectures show the same phenomena (they do
   not, at the behavioural level) but that the geometric vulnerability holds across the tested architectures under
   the SPP formalism while the behavioural expression depends on whether the system can build workarounds. These
   workarounds are never free: they either convert graceful degradation into catastrophic failure, or sacrifice
   semantic usefulness entirely. We organise our findings into three architectural categories (pure geometric,
   reasoning-overlay, and systems outside the operative theorem regime) that make this tradeoff explicit.

Results

Mathematical framework: the no-escape theorem

Definition 1 (Semantic Proximity Property).

   A memory system
   [MATH: <semantics><mrow><mi class="ltx_font_mathcaligraphic">ℳ</mi><mo>=</mo><mrow><mo
   stretchy="false">(</mo><mi
   class="ltx_font_mathcaligraphic">𝒮</mi><mo>,</mo><mi>E</mi><mo>,</mo><mi>R</mi><mo>,</mo><mi>d</mi><mo
   stretchy="false">)</mo></mrow></mrow><annotation
   encoding="application/x-tex">\mathcal{M}=(\mathcal{S},E,R,d)</annotation></semantics> :MATH]
   with item set
   [MATH: <semantics><mi class="ltx_font_mathcaligraphic">𝒮</mi><annotation
   encoding="application/x-tex">\mathcal{S}</annotation></semantics> :MATH]
   , encoding function
   [MATH: <semantics><mrow><mi>E</mi><mo lspace="0.278em" rspace="0.278em">:</mo><mrow><mi
   class="ltx_font_mathcaligraphic">𝒮</mi><mo stretchy="false">→</mo><mi
   class="ltx_font_mathcaligraphic">𝒱</mi></mrow></mrow><annotation
   encoding="application/x-tex">E:\mathcal{S}\to\mathcal{V}</annotation></semantics> :MATH]
   into a Hilbert space
   [MATH: <semantics><mi class="ltx_font_mathcaligraphic">𝒱</mi><annotation
   encoding="application/x-tex">\mathcal{V}</annotation></semantics> :MATH]
   , retrieval function
   [MATH: <semantics><mi>R</mi><annotation encoding="application/x-tex">R</annotation></semantics> :MATH]
   , and proximity measure
   [MATH: <semantics><mi>d</mi><annotation encoding="application/x-tex">d</annotation></semantics> :MATH]
   , satisfies the Semantic Proximity Property (SPP) if for any semantically related pair
   [MATH: <semantics><mrow><mo
   stretchy="false">(</mo><msub><mi>s</mi><mi>i</mi></msub><mo>,</mo><msub><mi>s</mi><mi>j</mi></msub><mo
   stretchy="false">)</mo></mrow><annotation encoding="application/x-tex">(s_{i},s_{j})</annotation></semantics>
   :MATH]
   and unrelated pair
   [MATH: <semantics><mrow><mo
   stretchy="false">(</mo><msub><mi>s</mi><mi>i</mi></msub><mo>,</mo><msub><mi>s</mi><mi>k</mi></msub><mo
   stretchy="false">)</mo></mrow><annotation encoding="application/x-tex">(s_{i},s_{k})</annotation></semantics>
   :MATH]
   :
   [MATH: <semantics><mrow><mrow><mrow><mi>𝔼</mi><mo lspace="0em" rspace="0em">​</mo><mrow><mo
   stretchy="false">[</mo><mrow><mi>d</mi><mo lspace="0em" rspace="0em">​</mo><mrow><mo
   stretchy="false">(</mo><mrow><mi>E</mi><mo lspace="0em" rspace="0em">​</mo><mrow><mo
   stretchy="false">(</mo><msub><mi>s</mi><mi>i</mi></msub><mo
   stretchy="false">)</mo></mrow></mrow><mo>,</mo><mrow><mi>E</mi><mo lspace="0em" rspace="0em">​</mo><mrow><mo
   stretchy="false">(</mo><msub><mi>s</mi><mi>j</mi></msub><mo stretchy="false">)</mo></mrow></mrow><mo
   stretchy="false">)</mo></mrow></mrow><mo stretchy="false">]</mo></mrow></mrow><mo><</mo><mrow><mi>𝔼</mi><mo
   lspace="0em" rspace="0em">​</mo><mrow><mo stretchy="false">[</mo><mrow><mi>d</mi><mo lspace="0em"
   rspace="0em">​</mo><mrow><mo stretchy="false">(</mo><mrow><mi>E</mi><mo lspace="0em"
   rspace="0em">​</mo><mrow><mo stretchy="false">(</mo><msub><mi>s</mi><mi>i</mi></msub><mo
   stretchy="false">)</mo></mrow></mrow><mo>,</mo><mrow><mi>E</mi><mo lspace="0em" rspace="0em">​</mo><mrow><mo
   stretchy="false">(</mo><msub><mi>s</mi><mi>k</mi></msub><mo stretchy="false">)</mo></mrow></mrow><mo
   stretchy="false">)</mo></mrow></mrow><mo stretchy="false">]</mo></mrow></mrow></mrow><mo
   lspace="0em">.</mo></mrow><annotation
   encoding="application/x-tex">\mathbb{E}[d(E(s_{i}),E(s_{j}))]<\mathbb{E}[d(E(s_{i}),E(s_{k}))].</annotation></s
   emantics> :MATH]

   We verified SPP empirically for all five architectures using
   [MATH: <semantics><mn>143</mn><annotation encoding="application/x-tex">143</annotation></semantics> :MATH]
   sentence pairs from Wikipedia (
   [MATH: <semantics><mrow><mi>p</mi><mo><</mo><mn>0.001</mn></mrow><annotation
   encoding="application/x-tex">p<0.001</annotation></semantics> :MATH]
   , paired
   [MATH: <semantics><mi>t</mi><annotation encoding="application/x-tex">t</annotation></semantics> :MATH]
   -test, Cohen’s
   [MATH: <semantics><mrow><mi>d</mi><mo>></mo><mn>1.5</mn></mrow><annotation
   encoding="application/x-tex">d>1.5</annotation></semantics> :MATH]
   for all embedding architectures; Extended Data Fig. 14). We acknowledge that
   [MATH: <semantics><mn>143</mn><annotation encoding="application/x-tex">143</annotation></semantics> :MATH]
   pairs is a limited empirical base; the SPP verification serves as a sanity check that each architecture
   satisfies the minimal definition, not as proof that SPP holds for all possible inputs. The definition is
   deliberately minimal: we specify neither the encoding mechanism nor the similarity function, requiring only
   that the system places related items closer than unrelated ones.

   To obtain the formal results below, we introduce five axioms that define the kernel-threshold memory class.

Definition 2 (Axiom A1: Kernel-Threshold Retrieval).

   There exists a semantic feature map
   [MATH: <semantics><mrow><mi>ϕ</mi><mo lspace="0.278em" rspace="0.278em">:</mo><mrow><mi
   class="ltx_font_mathcaligraphic">𝒳</mi><mo stretchy="false">→</mo><mi
   class="ltx_font_mathcaligraphic">ℋ</mi></mrow></mrow><annotation
   encoding="application/x-tex">\phi:\mathcal{X}\to\mathcal{H}</annotation></semantics> :MATH]
   into a Hilbert space and a retrieval score
   [MATH: <semantics><mrow><mrow><mi>s</mi><mo lspace="0em" rspace="0em">​</mo><mrow><mo
   stretchy="false">(</mo><mi>q</mi><mo>,</mo><mi>x</mi><mo
   stretchy="false">)</mo></mrow></mrow><mo>=</mo><mrow><mi>g</mi><mo lspace="0em" rspace="0em">​</mo><mrow><mo
   stretchy="false">(</mo><msub><mrow><mo
   stretchy="false">⟨</mo><msub><mi>w</mi><mi>q</mi></msub><mo>,</mo><mrow><mi>ϕ</mi><mo lspace="0em"
   rspace="0em">​</mo><mrow><mo stretchy="false">(</mo><mi>x</mi><mo stretchy="false">)</mo></mrow></mrow><mo
   stretchy="false">⟩</mo></mrow><mi class="ltx_font_mathcaligraphic">ℋ</mi></msub><mo
   stretchy="false">)</mo></mrow></mrow></mrow><annotation encoding="application/x-tex">s(q,x)=g(\langle
   w_{q},\phi(x)\rangle_{\mathcal{H}})</annotation></semantics> :MATH]
   , where
   [MATH: <semantics><mi>g</mi><annotation encoding="application/x-tex">g</annotation></semantics> :MATH]
   is monotone increasing. Cosine similarity, dot-product retrieval, and linear probes on hidden states fit this
   form.

Definition 3 (Axiom A2: Semantic Sufficiency).

   There is a positive semidefinite semantic kernel
   [MATH: <semantics><mi>K</mi><annotation encoding="application/x-tex">K</annotation></semantics> :MATH]
   such that retrieval relevance is measurable with respect to the sigma-algebra generated by the semantic
   coordinates of
   [MATH: <semantics><mi>K</mi><annotation encoding="application/x-tex">K</annotation></semantics> :MATH]
   . Only the semantic component can improve Bayes retrieval risk.

Definition 4 (Axiom A3: Rate-Distortion Optimality).

   The encoder is optimal for retrieval risk under a rate or distortion budget
   [MATH: <semantics><mi>D</mi><annotation encoding="application/x-tex">D</annotation></semantics> :MATH]
   .

Definition 5 (Axiom A4: Local Regularity).

   The pushforward measure
   [MATH: <semantics><mrow><mi>μ</mi><mo>=</mo><mrow><msub><mi>ϕ</mi><mi mathvariant="normal">#</mi></msub><mo
   lspace="0em" rspace="0em">​</mo><msub><mi>P</mi><mi>X</mi></msub></mrow></mrow><annotation
   encoding="application/x-tex">\mu=\phi_{\#}P_{X}</annotation></semantics> :MATH]
   on the semantic manifold is locally Ahlfors regular of intrinsic dimension
   [MATH: <semantics><msub><mi>d</mi><mi>loc</mi></msub><annotation
   encoding="application/x-tex">d_{\mathrm{loc}}</annotation></semantics> :MATH]
   : for
   [MATH: <semantics><mi>μ</mi><annotation encoding="application/x-tex">\mu</annotation></semantics> :MATH]
   -almost every anchor
   [MATH: <semantics><mi>z</mi><annotation encoding="application/x-tex">z</annotation></semantics> :MATH]
   ,
   [MATH: <semantics><mrow><mrow><msub><mi>c</mi><mn>1</mn></msub><mo lspace="0em"
   rspace="0em">​</mo><msup><mi>r</mi><msub><mi>d</mi><mi>loc</mi></msub></msup></mrow><mo>≤</mo><mrow><mi>μ</mi><
   mo lspace="0em" rspace="0em">​</mo><mrow><mo stretchy="false">(</mo><mrow><mi>B</mi><mo lspace="0em"
   rspace="0em">​</mo><mrow><mo stretchy="false">(</mo><mi>z</mi><mo>,</mo><mi>r</mi><mo
   stretchy="false">)</mo></mrow></mrow><mo
   stretchy="false">)</mo></mrow></mrow><mo>≤</mo><mrow><msub><mi>c</mi><mn>2</mn></msub><mo lspace="0em"
   rspace="0em">​</mo><msup><mi>r</mi><msub><mi>d</mi><mi>loc</mi></msub></msup></mrow></mrow><annotation
   encoding="application/x-tex">c_{1}r^{d_{\mathrm{loc}}}\leq\mu(B(z,r))\leq
   c_{2}r^{d_{\mathrm{loc}}}</annotation></semantics> :MATH]
   for
   [MATH:
   <semantics><mrow><mn>0</mn><mo><</mo><mi>r</mi><mo><</mo><msub><mi>r</mi><mn>0</mn></msub></mrow><annotation
   encoding="application/x-tex">0<r<r_{0}</annotation></semantics> :MATH]
   .

Definition 6 (Axiom A5: Associative Convexity).

   For studied items
   [MATH: <semantics><mrow><mo stretchy="false">{</mo><msub><mi>x</mi><mn>1</mn></msub><mo>,</mo><mi
   mathvariant="normal">…</mi><mo>,</mo><msub><mi>x</mi><mi>k</mi></msub><mo
   stretchy="false">}</mo></mrow><annotation
   encoding="application/x-tex">\{x_{1},\ldots,x_{k}\}</annotation></semantics> :MATH]
   , an associative lure
   [MATH: <semantics><mi>c</mi><annotation encoding="application/x-tex">c</annotation></semantics> :MATH]
   is
   [MATH: <semantics><mi>δ</mi><annotation encoding="application/x-tex">\delta</annotation></semantics> :MATH]
   -convex if
   [MATH: <semantics><mrow><msub><mrow><mo stretchy="false">‖</mo><mrow><mrow><mi>ϕ</mi><mo lspace="0em"
   rspace="0em">​</mo><mrow><mo stretchy="false">(</mo><mi>c</mi><mo stretchy="false">)</mo></mrow></mrow><mo
   rspace="0.055em">−</mo><mrow><msub><mo>∑</mo><mi>i</mi></msub><mrow><msub><mi>a</mi><mi>i</mi></msub><mo
   lspace="0em" rspace="0em">​</mo><mi>ϕ</mi><mo lspace="0em" rspace="0em">​</mo><mrow><mo
   stretchy="false">(</mo><msub><mi>x</mi><mi>i</mi></msub><mo
   stretchy="false">)</mo></mrow></mrow></mrow></mrow><mo stretchy="false">‖</mo></mrow><mi
   class="ltx_font_mathcaligraphic">ℋ</mi></msub><mo>≤</mo><mi>δ</mi></mrow><annotation
   encoding="application/x-tex">\|\phi(c)-\sum_{i}a_{i}\phi(x_{i})\|_{\mathcal{H}}\leq\delta</annotation></semanti
   cs> :MATH]
   for some convex weights
   [MATH: <semantics><mrow><msub><mi>a</mi><mi>i</mi></msub><mo>≥</mo><mn>0</mn></mrow><annotation
   encoding="application/x-tex">a_{i}\geq 0</annotation></semantics> :MATH]
   ,
   [MATH:
   <semantics><mrow><mrow><msub><mo>∑</mo><mi>i</mi></msub><msub><mi>a</mi><mi>i</mi></msub></mrow><mo>=</mo><mn>1
   </mn></mrow><annotation encoding="application/x-tex">\sum_{i}a_{i}=1</annotation></semantics> :MATH]
   .

Theorem 1 (Semantic Spectral Bound; proof sketch).

   Let
   [MATH: <semantics><mi>K</mi><annotation encoding="application/x-tex">K</annotation></semantics> :MATH]
   be the semantic kernel with Mercer eigenpairs
   [MATH: <semantics><mrow><mo
   stretchy="false">(</mo><msub><mi>λ</mi><mi>j</mi></msub><mo>,</mo><msub><mi>ψ</mi><mi>j</mi></msub><mo
   stretchy="false">)</mo></mrow><annotation
   encoding="application/x-tex">(\lambda_{j},\psi_{j})</annotation></semantics> :MATH]
   . Under Axioms A1–A3, for every optimal encoder under distortion budget
   [MATH: <semantics><mi>D</mi><annotation encoding="application/x-tex">D</annotation></semantics> :MATH]
   , there exists a threshold
   [MATH: <semantics><mrow><mi>γ</mi><mo lspace="0em" rspace="0em">​</mo><mrow><mo
   stretchy="false">(</mo><mi>D</mi><mo stretchy="false">)</mo></mrow></mrow><annotation
   encoding="application/x-tex">\gamma(D)</annotation></semantics> :MATH]
   such that the encoder factors through the truncated semantic statistic
   [MATH: <semantics><mrow><mrow><msub><mi mathvariant="normal">Φ</mi><mi>γ</mi></msub><mo lspace="0em"
   rspace="0em">​</mo><mrow><mo stretchy="false">(</mo><mi>x</mi><mo
   stretchy="false">)</mo></mrow></mrow><mo>=</mo><msub><mrow><mo
   stretchy="false">(</mo><mrow><msqrt><msub><mi>λ</mi><mi>j</mi></msub></msqrt><mo lspace="0em"
   rspace="0em">​</mo><msub><mi>ψ</mi><mi>j</mi></msub><mo lspace="0em" rspace="0em">​</mo><mrow><mo
   stretchy="false">(</mo><mi>x</mi><mo stretchy="false">)</mo></mrow></mrow><mo
   stretchy="false">)</mo></mrow><mrow><msub><mi>λ</mi><mi>j</mi></msub><mo>></mo><mrow><mi>γ</mi><mo lspace="0em"
   rspace="0em">​</mo><mrow><mo stretchy="false">(</mo><mi>D</mi><mo
   stretchy="false">)</mo></mrow></mrow></mrow></msub></mrow><annotation
   encoding="application/x-tex">\Phi_{\gamma}(x)=(\sqrt{\lambda_{j}}\psi_{j}(x))_{\lambda_{j}>\gamma(D)}</annotati
   on></semantics> :MATH]
   . The semantically useful effective dimension obeys
   [MATH:
   <semantics><mrow><msub><mi>d</mi><mi>eff</mi></msub><mo>≤</mo><mrow><msub><mi>r</mi><mi>eff</mi></msub><mo
   lspace="0em" rspace="0em">​</mo><mrow><mo stretchy="false">(</mo><mrow><mi>γ</mi><mo lspace="0em"
   rspace="0em">​</mo><mrow><mo stretchy="false">(</mo><mi>D</mi><mo stretchy="false">)</mo></mrow></mrow><mo
   stretchy="false">)</mo></mrow></mrow><mo>≤</mo><mrow><mi mathvariant="normal">#</mi><mo lspace="0em"
   rspace="0em">​</mo><mrow><mo stretchy="false">{</mo><mi>j</mi><mo lspace="0.278em"
   rspace="0.278em">:</mo><mrow><msub><mi>λ</mi><mi>j</mi></msub><mo>></mo><mrow><mi>γ</mi><mo lspace="0em"
   rspace="0em">​</mo><mrow><mo stretchy="false">(</mo><mi>D</mi><mo
   stretchy="false">)</mo></mrow></mrow></mrow><mo stretchy="false">}</mo></mrow></mrow></mrow><annotation
   encoding="application/x-tex">d_{\mathrm{eff}}\leq
   r_{\mathrm{eff}}(\gamma(D))\leq\#\{j:\lambda_{j}>\gamma(D)\}</annotation></semantics> :MATH]
   . Nominal dimension can grow without changing the semantically useful effective rank. For natural language,
   empirical measurements yield
   [MATH: <semantics><mrow><msub><mi>d</mi><mi>intrinsic</mi></msub><mo>≈</mo><mn>10</mn></mrow><annotation
   encoding="application/x-tex">d_{\mathrm{intrinsic}}\approx 10</annotation></semantics> :MATH]
   –
   [MATH: <semantics><mn>50</mn><annotation encoding="application/x-tex">50</annotation></semantics> :MATH]
   ^8; this is an observed range, not a mathematical consequence.

   Proof sketch. Mercer decomposition of
   [MATH: <semantics><mi>K</mi><annotation encoding="application/x-tex">K</annotation></semantics> :MATH]
   yields the semantic statistic. By Blackwell sufficiency, nuisance directions independent of relevance given the
   semantic coordinates cannot reduce Bayes retrieval risk. Reverse water-filling under the distortion budget
   retains only spectral modes above
   [MATH: <semantics><mrow><mi>γ</mi><mo lspace="0em" rspace="0em">​</mo><mrow><mo
   stretchy="false">(</mo><mi>D</mi><mo stretchy="false">)</mo></mrow></mrow><annotation
   encoding="application/x-tex">\gamma(D)</annotation></semantics> :MATH]
   . Full proof in Supplementary §S2.
   [MATH: <semantics><mi mathvariant="normal">□</mi><annotation
   encoding="application/x-tex">\square</annotation></semantics> :MATH]

Theorem 2 (Positive Cap Mass).

   Under Axioms A1 and A4, for any anchor
   [MATH: <semantics><mi>z</mi><annotation encoding="application/x-tex">z</annotation></semantics> :MATH]
   and sufficiently small retrieval radius
   [MATH: <semantics><mi>θ</mi><annotation encoding="application/x-tex">\theta</annotation></semantics> :MATH]
   ,
   [MATH: <semantics><mrow><mrow><msubsup><mi>c</mi><mn>1</mn><mo>′</mo></msubsup><mo lspace="0em"
   rspace="0em">​</mo><msup><mi>θ</mi><mrow><msub><mi>d</mi><mi>loc</mi></msub><mo lspace="0em"
   rspace="0em">​</mo><mrow><mo stretchy="false">(</mo><mi>z</mi><mo
   stretchy="false">)</mo></mrow></mrow></msup></mrow><mo>≤</mo><mrow><mi>μ</mi><mo lspace="0em"
   rspace="0em">​</mo><mrow><mo stretchy="false">(</mo><mrow><mi>C</mi><mo lspace="0em"
   rspace="0em">​</mo><mrow><mo stretchy="false">(</mo><mi>z</mi><mo>,</mo><mi>θ</mi><mo
   stretchy="false">)</mo></mrow></mrow><mo
   stretchy="false">)</mo></mrow></mrow><mo>≤</mo><mrow><msubsup><mi>c</mi><mn>2</mn><mo>′</mo></msubsup><mo
   lspace="0em" rspace="0em">​</mo><msup><mi>θ</mi><mrow><msub><mi>d</mi><mi>loc</mi></msub><mo lspace="0em"
   rspace="0em">​</mo><mrow><mo stretchy="false">(</mo><mi>z</mi><mo
   stretchy="false">)</mo></mrow></mrow></msup></mrow></mrow><annotation
   encoding="application/x-tex">c_{1}^{\prime}\theta^{d_{\mathrm{loc}}(z)}\leq\mu(C(z,\theta))\leq
   c_{2}^{\prime}\theta^{d_{\mathrm{loc}}(z)}</annotation></semantics> :MATH]
   . Every admissible retrieval neighbourhood has strictly positive competitor mass.

Theorem 3 (Inevitable Forgetting Under Growing Memory).

   Under Axioms A1 and A4, if competitor arrivals form a marked point process with cumulative intensity
   [MATH: <semantics><mrow><mrow><msub><mi mathvariant="normal">Λ</mi><mi>x</mi></msub><mo lspace="0em"
   rspace="0em">​</mo><mrow><mo stretchy="false">(</mo><mi>t</mi><mo stretchy="false">)</mo></mrow></mrow><mo
   rspace="0.111em">=</mo><mrow><msubsup><mo>∫</mo><mn>0</mn><mi>t</mi></msubsup><mrow><msub><mi>λ</mi><mi>x</mi><
   /msub><mo lspace="0em" rspace="0em">​</mo><mrow><mo stretchy="false">(</mo><mi>u</mi><mo
   stretchy="false">)</mo></mrow><mo lspace="0.170em" rspace="0em">​</mo><mrow><mo
   rspace="0em">𝑑</mo><mi>u</mi></mrow></mrow></mrow></mrow><annotation
   encoding="application/x-tex">\Lambda_{x}(t)=\int_{0}^{t}\lambda_{x}(u)\,du</annotation></semantics> :MATH]
   , then retention for item
   [MATH: <semantics><mi>x</mi><annotation encoding="application/x-tex">x</annotation></semantics> :MATH]
   is
   [MATH: <semantics><mrow><mrow><msub><mi>R</mi><mi>x</mi></msub><mo lspace="0em" rspace="0em">​</mo><mrow><mo
   stretchy="false">(</mo><mi>t</mi><mo
   stretchy="false">)</mo></mrow></mrow><mo>=</mo><mrow><mi>exp</mi><mo>⁡</mo><mrow><mo
   stretchy="false">(</mo><mrow><mo>−</mo><mrow><mi>μ</mi><mo lspace="0em" rspace="0em">​</mo><mrow><mo
   stretchy="false">(</mo><msub><mi>C</mi><mi>x</mi></msub><mo stretchy="false">)</mo></mrow><mo lspace="0em"
   rspace="0em">​</mo><msub><mi mathvariant="normal">Λ</mi><mi>x</mi></msub><mo lspace="0em"
   rspace="0em">​</mo><mrow><mo stretchy="false">(</mo><mi>t</mi><mo
   stretchy="false">)</mo></mrow></mrow></mrow><mo stretchy="false">)</mo></mrow></mrow></mrow><annotation
   encoding="application/x-tex">R_{x}(t)=\exp(-\mu(C_{x})\Lambda_{x}(t))</annotation></semantics> :MATH]
   . If
   [MATH: <semantics><mrow><mrow><msub><mi mathvariant="normal">Λ</mi><mi>x</mi></msub><mo lspace="0em"
   rspace="0em">​</mo><mrow><mo stretchy="false">(</mo><mi>t</mi><mo stretchy="false">)</mo></mrow></mrow><mo
   stretchy="false">→</mo><mi mathvariant="normal">∞</mi></mrow><annotation
   encoding="application/x-tex">\Lambda_{x}(t)\to\infty</annotation></semantics> :MATH]
   , then
   [MATH: <semantics><mrow><mrow><msub><mi>R</mi><mi>x</mi></msub><mo lspace="0em" rspace="0em">​</mo><mrow><mo
   stretchy="false">(</mo><mi>t</mi><mo stretchy="false">)</mo></mrow></mrow><mo
   stretchy="false">→</mo><mn>0</mn></mrow><annotation encoding="application/x-tex">R_{x}(t)\to
   0</annotation></semantics> :MATH]
   .

Corollary 4 (Stretched Exponential Per-Item Retention).

   If
   [MATH: <semantics><mrow><mrow><msub><mi>λ</mi><mi>x</mi></msub><mo lspace="0em" rspace="0em">​</mo><mrow><mo
   stretchy="false">(</mo><mi>t</mi><mo
   stretchy="false">)</mo></mrow></mrow><mo>=</mo><mrow><msub><mi>λ</mi><mrow><mn>0</mn><mo>,</mo><mi>x</mi></mrow
   ></msub><mo lspace="0em"
   rspace="0em">​</mo><msup><mi>t</mi><mrow><mo>−</mo><mi>α</mi></mrow></msup></mrow></mrow><annotation
   encoding="application/x-tex">\lambda_{x}(t)=\lambda_{0,x}t^{-\alpha}</annotation></semantics> :MATH]
   with
   [MATH: <semantics><mrow><mn>0</mn><mo><</mo><mi>α</mi><mo><</mo><mn>1</mn></mrow><annotation
   encoding="application/x-tex">0<\alpha<1</annotation></semantics> :MATH]
   , then
   [MATH: <semantics><mrow><mrow><msub><mi>R</mi><mi>x</mi></msub><mo lspace="0em" rspace="0em">​</mo><mrow><mo
   stretchy="false">(</mo><mi>t</mi><mo
   stretchy="false">)</mo></mrow></mrow><mo>=</mo><mrow><mi>exp</mi><mo>⁡</mo><mrow><mo
   stretchy="false">(</mo><mrow><mo>−</mo><mrow><msub><mi>c</mi><mi>x</mi></msub><mo lspace="0em"
   rspace="0em">​</mo><msup><mi>t</mi><mrow><mn>1</mn><mo>−</mo><mi>α</mi></mrow></msup></mrow></mrow><mo
   stretchy="false">)</mo></mrow></mrow></mrow><annotation
   encoding="application/x-tex">R_{x}(t)=\exp(-c_{x}t^{1-\alpha})</annotation></semantics> :MATH]
   where
   [MATH: <semantics><mrow><msub><mi>c</mi><mi>x</mi></msub><mo>=</mo><mrow><mrow><mi>μ</mi><mo lspace="0em"
   rspace="0em">​</mo><mrow><mo stretchy="false">(</mo><msub><mi>C</mi><mi>x</mi></msub><mo
   stretchy="false">)</mo></mrow><mo lspace="0em"
   rspace="0em">​</mo><msub><mi>λ</mi><mrow><mn>0</mn><mo>,</mo><mi>x</mi></mrow></msub></mrow><mo>/</mo><mrow><mo
   stretchy="false">(</mo><mrow><mn>1</mn><mo>−</mo><mi>α</mi></mrow><mo
   stretchy="false">)</mo></mrow></mrow></mrow><annotation
   encoding="application/x-tex">c_{x}=\mu(C_{x})\lambda_{0,x}/(1-\alpha)</annotation></semantics> :MATH]
   . This is a stretched exponential, not a power law, for any individual item.

Proposition 5 (Population Power Law from Heterogeneity).

   If the item-specific scale
   [MATH: <semantics><msub><mi>c</mi><mi>x</mi></msub><annotation
   encoding="application/x-tex">c_{x}</annotation></semantics> :MATH]
   has a density regularly varying at zero,
   [MATH: <semantics><mrow><mrow><mi>g</mi><mo lspace="0em" rspace="0em">​</mo><mrow><mo
   stretchy="false">(</mo><mi>c</mi><mo stretchy="false">)</mo></mrow></mrow><mo>∼</mo><mrow><mi>κ</mi><mo
   lspace="0em"
   rspace="0em">​</mo><msup><mi>c</mi><mrow><mi>β</mi><mo>−</mo><mn>1</mn></mrow></msup></mrow></mrow><annotation
   encoding="application/x-tex">g(c)\sim\kappa c^{\beta-1}</annotation></semantics> :MATH]
   as
   [MATH: <semantics><mrow><mi>c</mi><mo stretchy="false">↓</mo><mn>0</mn></mrow><annotation
   encoding="application/x-tex">c\downarrow 0</annotation></semantics> :MATH]
   , then the population-averaged retention obeys
   [MATH: <semantics><mrow><mrow><mover accent="true"><mi>R</mi><mo stretchy="true">¯</mo></mover><mo lspace="0em"
   rspace="0em">​</mo><mrow><mo stretchy="false">(</mo><mi>t</mi><mo
   stretchy="false">)</mo></mrow></mrow><mo>∼</mo><mrow><mi>κ</mi><mo lspace="0em" rspace="0em">​</mo><mi
   mathvariant="normal">Γ</mi><mo lspace="0em" rspace="0em">​</mo><mrow><mo stretchy="false">(</mo><mi>β</mi><mo
   stretchy="false">)</mo></mrow><mo lspace="0em"
   rspace="0em">​</mo><msup><mi>t</mi><mrow><mo>−</mo><mrow><mi>β</mi><mo lspace="0em"
   rspace="0em">​</mo><mrow><mo stretchy="false">(</mo><mrow><mn>1</mn><mo>−</mo><mi>α</mi></mrow><mo
   stretchy="false">)</mo></mrow></mrow></mrow></msup></mrow></mrow><annotation
   encoding="application/x-tex">\overline{R}(t)\sim\kappa\Gamma(\beta)t^{-\beta(1-\alpha)}</annotation></semantics
   > :MATH]
   . The population forgetting exponent is
   [MATH: <semantics><mrow><mi>b</mi><mo>=</mo><mrow><mi>β</mi><mo lspace="0em" rspace="0em">​</mo><mrow><mo
   stretchy="false">(</mo><mrow><mn>1</mn><mo>−</mo><mi>α</mi></mrow><mo
   stretchy="false">)</mo></mrow></mrow></mrow><annotation
   encoding="application/x-tex">b=\beta(1-\alpha)</annotation></semantics> :MATH]
   .

   Interpretation. Individual items forget by a stretched exponential; population heterogeneity turns this into a
   power law. Geometry determines the hazard scale (
   [MATH: <semantics><mrow><mi>μ</mi><mo lspace="0em" rspace="0em">​</mo><mrow><mo
   stretchy="false">(</mo><msub><mi>C</mi><mi>x</mi></msub><mo stretchy="false">)</mo></mrow></mrow><annotation
   encoding="application/x-tex">\mu(C_{x})</annotation></semantics> :MATH]
   ), the environment determines the time dependence (
   [MATH: <semantics><mi>α</mi><annotation encoding="application/x-tex">\alpha</annotation></semantics> :MATH]
   ), and population heterogeneity (
   [MATH: <semantics><mi>β</mi><annotation encoding="application/x-tex">\beta</annotation></semantics> :MATH]
   ) determines the asymptotic forgetting exponent. The exponent
   [MATH: <semantics><mi>α</mi><annotation encoding="application/x-tex">\alpha</annotation></semantics> :MATH]
   is corpus-dependent: Anderson & Schooler^2 reported
   [MATH: <semantics><mrow><mi>α</mi><mo>=</mo><mn>0.513</mn></mrow><annotation
   encoding="application/x-tex">\alpha=0.513</annotation></semantics> :MATH]
   on newspaper text; we measure
   [MATH: <semantics><mrow><mi>α</mi><mo>=</mo><mn>0.459</mn></mrow><annotation
   encoding="application/x-tex">\alpha=0.459</annotation></semantics> :MATH]
   on Wikipedia. Both place
   [MATH: <semantics><mi>b</mi><annotation encoding="application/x-tex">b</annotation></semantics> :MATH]
   in the
   [MATH: <semantics><mrow><mo stretchy="false">[</mo><mn>0.3</mn><mo>,</mo><mn>0.6</mn><mo
   stretchy="false">]</mo></mrow><annotation encoding="application/x-tex">[0.3,0.6]</annotation></semantics>
   :MATH]
   range for reasonable
   [MATH: <semantics><mi>β</mi><annotation encoding="application/x-tex">\beta</annotation></semantics> :MATH]
   .

Theorem 6 (Inseparability of Associative Lures).

   Under Axioms A1 and A5, let
   [MATH: <semantics><mi>c</mi><annotation encoding="application/x-tex">c</annotation></semantics> :MATH]
   be a
   [MATH: <semantics><mi>δ</mi><annotation encoding="application/x-tex">\delta</annotation></semantics> :MATH]
   -convex lure for studied items
   [MATH: <semantics><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>,</mo><mi
   mathvariant="normal">…</mi><mo>,</mo><msub><mi>x</mi><mi>k</mi></msub></mrow><annotation
   encoding="application/x-tex">x_{1},\ldots,x_{k}</annotation></semantics> :MATH]
   . If each studied item is accepted with margin
   [MATH: <semantics><mrow><mi>m</mi><mo>></mo><mn>0</mn></mrow><annotation
   encoding="application/x-tex">m>0</annotation></semantics> :MATH]
   , i.e.
   [MATH: <semantics><mrow><mrow><msub><mi>f</mi><mi>q</mi></msub><mo lspace="0em" rspace="0em">​</mo><mrow><mo
   stretchy="false">(</mo><msub><mi>x</mi><mi>i</mi></msub><mo
   stretchy="false">)</mo></mrow></mrow><mo>≥</mo><mrow><mi>τ</mi><mo>+</mo><mi>m</mi></mrow></mrow><annotation
   encoding="application/x-tex">f_{q}(x_{i})\geq\tau+m</annotation></semantics> :MATH]
   for all
   [MATH: <semantics><mi>i</mi><annotation encoding="application/x-tex">i</annotation></semantics> :MATH]
   , then
   [MATH: <semantics><mrow><mrow><msub><mi>f</mi><mi>q</mi></msub><mo lspace="0em" rspace="0em">​</mo><mrow><mo
   stretchy="false">(</mo><mi>c</mi><mo
   stretchy="false">)</mo></mrow></mrow><mo>≥</mo><mrow><mrow><mi>τ</mi><mo>+</mo><mi>m</mi></mrow><mo>−</mo><mi>δ
   </mi></mrow></mrow><annotation encoding="application/x-tex">f_{q}(c)\geq\tau+m-\delta</annotation></semantics>
   :MATH]
   . If
   [MATH: <semantics><mrow><mi>δ</mi><mo><</mo><mi>m</mi></mrow><annotation
   encoding="application/x-tex">\delta<m</annotation></semantics> :MATH]
   , the lure is also accepted. If
   [MATH: <semantics><mrow><mi>δ</mi><mo>=</mo><mn>0</mn></mrow><annotation
   encoding="application/x-tex">\delta=0</annotation></semantics> :MATH]
   , no threshold in this score family that accepts all studied items can reject the lure.

   Proof.
   [MATH: <semantics><mrow><mrow><msub><mi>f</mi><mi>q</mi></msub><mo lspace="0em" rspace="0em">​</mo><mrow><mo
   stretchy="false">(</mo><mi>c</mi><mo stretchy="false">)</mo></mrow></mrow><mo>=</mo><mrow><mo
   stretchy="false">⟨</mo><msub><mi>w</mi><mi>q</mi></msub><mo
   rspace="0em">,</mo><mrow><mrow><msub><mo>∑</mo><mi>i</mi></msub><mrow><msub><mi>a</mi><mi>i</mi></msub><mo
   lspace="0em" rspace="0em">​</mo><mi>ϕ</mi><mo lspace="0em" rspace="0em">​</mo><mrow><mo
   stretchy="false">(</mo><msub><mi>x</mi><mi>i</mi></msub><mo
   stretchy="false">)</mo></mrow></mrow></mrow><mo>+</mo><mi>ε</mi></mrow><mo stretchy="false">⟩</mo></mrow><mo
   rspace="0.111em">=</mo><mrow><mrow><msub><mo>∑</mo><mi>i</mi></msub><mrow><msub><mi>a</mi><mi>i</mi></msub><mo
   lspace="0em" rspace="0em">​</mo><msub><mi>f</mi><mi>q</mi></msub><mo lspace="0em" rspace="0em">​</mo><mrow><mo
   stretchy="false">(</mo><msub><mi>x</mi><mi>i</mi></msub><mo
   stretchy="false">)</mo></mrow></mrow></mrow><mo>+</mo><mrow><mo
   stretchy="false">⟨</mo><msub><mi>w</mi><mi>q</mi></msub><mo>,</mo><mi>ε</mi><mo
   stretchy="false">⟩</mo></mrow></mrow><mo
   rspace="0.111em">≥</mo><mrow><mrow><msub><mo>∑</mo><mi>i</mi></msub><mrow><msub><mi>a</mi><mi>i</mi></msub><mo
   lspace="0em" rspace="0em">​</mo><mrow><mo stretchy="false">(</mo><mrow><mi>τ</mi><mo>+</mo><mi>m</mi></mrow><mo
   stretchy="false">)</mo></mrow></mrow></mrow><mo>−</mo><mrow><mrow><mo
   stretchy="false">‖</mo><msub><mi>w</mi><mi>q</mi></msub><mo stretchy="false">‖</mo></mrow><mo lspace="0em"
   rspace="0em">​</mo><mrow><mo stretchy="false">‖</mo><mi>ε</mi><mo
   stretchy="false">‖</mo></mrow></mrow></mrow><mo>≥</mo><mrow><mrow><mi>τ</mi><mo>+</mo><mi>m</mi></mrow><mo>−</m
   o><mi>δ</mi></mrow></mrow><annotation encoding="application/x-tex">f_{q}(c)=\langle
   w_{q},\sum_{i}a_{i}\phi(x_{i})+\varepsilon\rangle=\sum_{i}a_{i}f_{q}(x_{i})+\langle
   w_{q},\varepsilon\rangle\geq\sum_{i}a_{i}(\tau+m)-\|w_{q}\|\|\varepsilon\|\geq\tau+m-\delta</annotation></seman
   tics> :MATH]
   .
   [MATH: <semantics><mi mathvariant="normal">□</mi><annotation
   encoding="application/x-tex">\square</annotation></semantics> :MATH]

   SPP alone guarantees semantic proximity but not threshold inseparability. The
   [MATH: <semantics><mi>δ</mi><annotation encoding="application/x-tex">\delta</annotation></semantics> :MATH]
   -convexity condition (A5) is stronger and empirically testable: for all 24 DRM lures, the convex-hull
   reconstruction error
   [MATH: <semantics><msup><mi>δ</mi><mo>∗</mo></msup><annotation
   encoding="application/x-tex">\delta^{*}</annotation></semantics> :MATH]
   is smaller than the observed decision margin
   [MATH: <semantics><mi>m</mi><annotation encoding="application/x-tex">m</annotation></semantics> :MATH]
   , confirming the theorem’s premise.

Theorem 7 (No Escape for Kernel-Threshold Memory).

   Under Axioms A1–A5: (1) the semantically useful representation has effective rank controlled by the semantic
   operator spectrum; (2) every admissible retrieval neighbourhood has positive competitor mass; (3) under growing
   memory, retention decays to zero; (4) for
   [MATH: <semantics><mi>δ</mi><annotation encoding="application/x-tex">\delta</annotation></semantics> :MATH]
   -convex associative lures with
   [MATH: <semantics><mi>δ</mi><annotation encoding="application/x-tex">\delta</annotation></semantics> :MATH]
   below the decision margin, false recall cannot be eliminated by threshold tuning within the same score family.
   Any architecture that simultaneously eliminates interference-driven forgetting and associative false recall
   must either abandon semantic continuity and kernel-threshold retrieval, add an external symbolic verifier or
   exact episodic record, or send the semantic effective rank to infinity.

The no-escape theorem operates at two levels

   The geometric level appears universal under the SPP formalism; the behavioural level is
   architecture-dependent. The distinction between these two levels is the paper’s central contribution beyond
   HIDE. At the geometric level, every system satisfying Axioms A1–A4 has low semantic effective rank,
   non-negligible spherical cap volumes, and representation-space vulnerability to interference. This is derived
   under stated assumptions and empirically confirmed in all five architectures. At the behavioural level, the
   manifestation depends on whether the architecture can build a workaround, and what that workaround costs.

   We organize the five architectures into three categories based on how the geometric vulnerability manifests
   behaviourally. Category 1 (pure geometric systems: vector database, graph memory) expresses the vulnerability
   directly: the geometry IS the behaviour. Category 2 (reasoning-overlay systems: attention memory, parametric
   memory) possesses the geometric vulnerability but can partially override it behaviourally, at the cost of
   converting graceful degradation into catastrophic failure. Category 3 (SPP-violating systems: filesystem/BM25)
   escapes the vulnerability entirely by abandoning semantic organisation. The remainder of this section reports
   results for each.

   The five architectures split into three categories:

   Category 1: Pure geometric systems (vector database, graph memory). The geometry IS the behaviour. These
   systems exhibit smooth power-law forgetting (
   [MATH: <semantics><mrow><mi>b</mi><mo>=</mo><mn>0.440</mn></mrow><annotation
   encoding="application/x-tex">b=0.440</annotation></semantics> :MATH]
   ,
   [MATH: <semantics><mn>0.478</mn><annotation encoding="application/x-tex">0.478</annotation></semantics> :MATH]
   ), robust DRM false recall (
   [MATH: <semantics><mrow><mtext>FA</mtext><mo>=</mo><mn>0.583</mn></mrow><annotation
   encoding="application/x-tex">\text{FA}=0.583</annotation></semantics> :MATH]
   ,
   [MATH: <semantics><mn>0.208</mn><annotation encoding="application/x-tex">0.208</annotation></semantics> :MATH]
   ), the spacing effect (long
   [MATH: <semantics><mo>></mo><annotation encoding="application/x-tex">></annotation></semantics> :MATH]
   massed), and TOT states (
   [MATH: <semantics><mrow><mn>2.0</mn><mo>%</mo></mrow><annotation
   encoding="application/x-tex">2.0\%</annotation></semantics> :MATH]
   ,
   [MATH: <semantics><mrow><mn>2.8</mn><mo>%</mo></mrow><annotation
   encoding="application/x-tex">2.8\%</annotation></semantics> :MATH]
   ). No escape at either level.

   Category 2: Systems with explicit reasoning overlays (attention memory, parametric memory). The geometric
   vulnerability exists (
   [MATH: <semantics><mrow><msub><mi>d</mi><mtext>eff</mtext></msub><mo>=</mo><mn>17.9</mn></mrow><annotation
   encoding="application/x-tex">d_{\text{eff}}=17.9</annotation></semantics> :MATH]
   , lures within caps), but the system can reason its way around it behaviourally. The LLM correctly rejects DRM
   lures by parsing word lists (
   [MATH: <semantics><mrow><mtext>FA</mtext><mo>=</mo><mn>0.000</mn></mrow><annotation
   encoding="application/x-tex">\text{FA}=0.000</annotation></semantics> :MATH]
   ). However, interference manifests differently: the attention architecture shows a phase transition (perfect
   accuracy
   [MATH: <semantics><mo stretchy="false">→</mo><annotation
   encoding="application/x-tex">\to</annotation></semantics> :MATH]
   catastrophic failure at
   [MATH: <semantics><mrow><mi></mi><mo>∼</mo><mn>100</mn></mrow><annotation encoding="application/x-tex">\sim
   100</annotation></semantics> :MATH]
   competitors), and parametric memory shows monotonically decreasing accuracy with neighbour density (
   [MATH: <semantics><mrow><mn>1.000</mn><mo stretchy="false">→</mo><mn>0.113</mn></mrow><annotation
   encoding="application/x-tex">1.000\to 0.113</annotation></semantics> :MATH]
   ,
   [MATH: <semantics><mrow><mi>b</mi><mo>=</mo><mn>0.215</mn></mrow><annotation
   encoding="application/x-tex">b=0.215</annotation></semantics> :MATH]
   on PopQA). The workaround converts graceful degradation into catastrophic failure.

   Category 3: Systems that abandon SPP (filesystem/BM25 keyword retrieval). BM25 produces
   [MATH: <semantics><mrow><mi>b</mi><mo>=</mo><mn>0.000</mn></mrow><annotation
   encoding="application/x-tex">b=0.000</annotation></semantics> :MATH]
   ,
   [MATH: <semantics><mrow><mtext>FA</mtext><mo>=</mo><mn>0.000</mn></mrow><annotation
   encoding="application/x-tex">\text{FA}=0.000</annotation></semantics> :MATH]
   , no spacing effect, yielding complete immunity. But SPP correlation is
   [MATH: <semantics><mrow><mi>r</mi><mo>=</mo><mn>0.210</mn></mrow><annotation
   encoding="application/x-tex">r=0.210</annotation></semantics> :MATH]
   and semantic retrieval agreement is
   [MATH: <semantics><mrow><mn>15.5</mn><mo>%</mo></mrow><annotation
   encoding="application/x-tex">15.5\%</annotation></semantics> :MATH]
   . It escaped interference by escaping usefulness. This IS the no-escape theorem in action.

Interference produces power-law forgetting in every SPP system

   In the architectures where temporal interference is expressed through graded retrieval competition, the
   forgetting exponent depends on competitor count and environmental arrival statistics. For the vector database
   (Architecture 1),
   [MATH:
   <semantics><mrow><mi>b</mi><mo>=</mo><mrow><mn>0.440</mn><mo>±</mo><mn>0.030</mn></mrow></mrow><annotation
   encoding="application/x-tex">b=0.440\pm 0.030</annotation></semantics> :MATH]
   (
   [MATH: <semantics><mrow><msup><mi>R</mi><mn>2</mn></msup><mo>=</mo><mn>0.570</mn></mrow><annotation
   encoding="application/x-tex">R^{2}=0.570</annotation></semantics> :MATH]
   ,
   [MATH: <semantics><mrow><mi>n</mi><mo>=</mo><mn>5</mn></mrow><annotation
   encoding="application/x-tex">n=5</annotation></semantics> :MATH]
   seeds) at
   [MATH: <semantics><mrow><mn>10</mn><mo>,</mo><mn>000</mn></mrow><annotation
   encoding="application/x-tex">10{,}000</annotation></semantics> :MATH]
   competitors with power-law temporal decay (
   [MATH: <semantics><mrow><mi>ψ</mi><mo>=</mo><mn>0.5</mn></mrow><annotation
   encoding="application/x-tex">\psi=0.5</annotation></semantics> :MATH]
   ,
   [MATH: <semantics><mrow><mi>β</mi><mo>=</mo><mn>0.20</mn></mrow><annotation
   encoding="application/x-tex">\beta=0.20</annotation></semantics> :MATH]
   ), matching HIDE’s
   [MATH: <semantics><mrow><mi>b</mi><mo>=</mo><mn>0.460</mn></mrow><annotation
   encoding="application/x-tex">b=0.460</annotation></semantics> :MATH]
   to within one standard error. At zero competitors,
   [MATH: <semantics><mrow><mi>b</mi><mo><</mo><mn>0.01</mn></mrow><annotation
   encoding="application/x-tex">b<0.01</annotation></semantics> :MATH]
   : without interference, there is no forgetting. This is not a subtle distinction: the identical encoding
   function without competitors yields
   [MATH: <semantics><mi>b</mi><annotation encoding="application/x-tex">b</annotation></semantics> :MATH]
   more than forty times smaller.

   The graph memory (Architecture 4, MiniLM + PageRank) produces
   [MATH:
   <semantics><mrow><mi>b</mi><mo>=</mo><mrow><mn>0.478</mn><mo>±</mo><mn>0.028</mn></mrow></mrow><annotation
   encoding="application/x-tex">b=0.478\pm 0.028</annotation></semantics> :MATH]
   at
   [MATH: <semantics><mrow><mn>10</mn><mo>,</mo><mn>000</mn></mrow><annotation
   encoding="application/x-tex">10{,}000</annotation></semantics> :MATH]
   competitors, squarely in the human range despite an entirely different retrieval mechanism. The parametric
   architecture (Architecture 5, Qwen2.5-7B) confirms interference in model weights via the PopQA dataset (
   [MATH: <semantics><mrow><mn>14</mn><mo>,</mo><mn>267</mn></mrow><annotation
   encoding="application/x-tex">14{,}267</annotation></semantics> :MATH]
   questions): accuracy decreases monotonically from
   [MATH: <semantics><mn>1.000</mn><annotation encoding="application/x-tex">1.000</annotation></semantics> :MATH]
   (fewer than
   [MATH: <semantics><mn>50</mn><annotation encoding="application/x-tex">50</annotation></semantics> :MATH]
   near neighbours) to
   [MATH: <semantics><mn>0.257</mn><annotation encoding="application/x-tex">0.257</annotation></semantics> :MATH]
   (
   [MATH: <semantics><mn>50</mn><annotation encoding="application/x-tex">50</annotation></semantics> :MATH]
   –
   [MATH: <semantics><mn>200</mn><annotation encoding="application/x-tex">200</annotation></semantics> :MATH]
   ),
   [MATH: <semantics><mn>0.170</mn><annotation encoding="application/x-tex">0.170</annotation></semantics> :MATH]
   (
   [MATH: <semantics><mn>200</mn><annotation encoding="application/x-tex">200</annotation></semantics> :MATH]
   –
   [MATH: <semantics><mn>500</mn><annotation encoding="application/x-tex">500</annotation></semantics> :MATH]
   ), and
   [MATH: <semantics><mn>0.113</mn><annotation encoding="application/x-tex">0.113</annotation></semantics> :MATH]
   (more than
   [MATH: <semantics><mrow><mn>1</mn><mo>,</mo><mn>000</mn></mrow><annotation
   encoding="application/x-tex">1{,}000</annotation></semantics> :MATH]
   ). Power-law fit:
   [MATH: <semantics><mrow><mi>b</mi><mo>=</mo><mn>0.215</mn></mrow><annotation
   encoding="application/x-tex">b=0.215</annotation></semantics> :MATH]
   ,
   [MATH: <semantics><mrow><msup><mi>R</mi><mn>2</mn></msup><mo>=</mo><mn>0.501</mn></mrow><annotation
   encoding="application/x-tex">R^{2}=0.501</annotation></semantics> :MATH]
   . Geometry plus power-law arrival gives stretched-exponential retention for individual items (Corollary 4). The
   empirically observed power law (
   [MATH: <semantics><mrow><mi>b</mi><mo>=</mo><mn>0.440</mn></mrow><annotation
   encoding="application/x-tex">b=0.440</annotation></semantics> :MATH]
   –
   [MATH: <semantics><mn>0.478</mn><annotation encoding="application/x-tex">0.478</annotation></semantics> :MATH]
   ) emerges after averaging over item-level heterogeneity in interference scale (Proposition 5), a standard
   scale-mixture mechanism.

   The attention architecture (Architecture 2, Qwen2.5-7B context window) reveals a qualitatively different
   failure mode that power-law fitting cannot capture. Rather than smooth degradation, accuracy undergoes a phase
   transition: near-perfect retrieval with fewer than
   [MATH: <semantics><mn>100</mn><annotation encoding="application/x-tex">100</annotation></semantics> :MATH]
   competitors collapses to near-zero at
   [MATH: <semantics><mrow><mn>200</mn><mo>+</mo></mrow><annotation
   encoding="application/x-tex">200+</annotation></semantics> :MATH]
   . A logistic fit
   [MATH: <semantics><mrow><mrow><mi>R</mi><mo lspace="0em" rspace="0em">​</mo><mrow><mo
   stretchy="false">(</mo><mi>n</mi><mo
   stretchy="false">)</mo></mrow></mrow><mo>=</mo><mrow><mn>1</mn><mo>/</mo><mrow><mo
   stretchy="false">(</mo><mrow><mn>1</mn><mo>+</mo><mrow><mi>exp</mi><mo>⁡</mo><mrow><mo
   stretchy="false">(</mo><mrow><mi>k</mi><mo lspace="0em" rspace="0em">​</mo><mrow><mo
   stretchy="false">(</mo><mrow><mi>n</mi><mo>−</mo><msub><mi>n</mi><mn>0</mn></msub></mrow><mo
   stretchy="false">)</mo></mrow></mrow><mo stretchy="false">)</mo></mrow></mrow></mrow><mo
   stretchy="false">)</mo></mrow></mrow></mrow><annotation
   encoding="application/x-tex">R(n)=1/(1+\exp(k(n-n_{0})))</annotation></semantics> :MATH]
   captures this cliff accurately (
   [MATH: <semantics><mrow><msub><mi>n</mi><mn>0</mn></msub><mo>≈</mo><mn>120</mn></mrow><annotation
   encoding="application/x-tex">n_{0}\approx 120</annotation></semantics> :MATH]
   ,
   [MATH: <semantics><mrow><mi>k</mi><mo>≈</mo><mn>0.03</mn></mrow><annotation
   encoding="application/x-tex">k\approx 0.03</annotation></semantics> :MATH]
   ). The distinction is itself informative: Category 1 systems degrade continuously (power law), while Category 2
   systems hold perfectly then fail discontinuously (sigmoid). These are qualitatively different failure
   signatures of the same underlying geometric vulnerability. The connection is precise: attention over a finite
   context window performs implicit nearest-neighbour search with a hard capacity limit. Below that limit, the
   reasoning overlay can compensate for geometric interference by attending selectively to relevant tokens. Above
   it, the
   [MATH: <semantics><mi>θ</mi><annotation encoding="application/x-tex">\theta</annotation></semantics> :MATH]
   -cap of competitors saturates the attention budget and the system collapses. The sigmoid inflection point (
   [MATH: <semantics><mrow><msub><mi>n</mi><mn>0</mn></msub><mo>≈</mo><mn>120</mn></mrow><annotation
   encoding="application/x-tex">n_{0}\approx 120</annotation></semantics> :MATH]
   ) marks the competitor count at which the attention capacity can no longer absorb the geometric interference
   predicted by Theorem 2. The filesystem architecture (Architecture 3, BM25) shows
   [MATH: <semantics><mrow><mi>b</mi><mo>=</mo><mn>0.000</mn></mrow><annotation
   encoding="application/x-tex">b=0.000</annotation></semantics> :MATH]
   (zero forgetting) because keyword matching bypasses semantic similarity entirely. But this immunity costs
   usefulness: BM25 retrieval agrees with cosine similarity on only
   [MATH: <semantics><mrow><mn>15.5</mn><mo>%</mo></mrow><annotation
   encoding="application/x-tex">15.5\%</annotation></semantics> :MATH]
   of queries.

False recall is geometrically inevitable but behaviourally overridable

   We did not build a false memory system; we found one in the geometry of every architecture. The DRM
   experiment^16 tests false recognition of semantic lures. For the vector database,
   [MATH: <semantics><mrow><mtext>FA</mtext><mo>=</mo><mn>0.583</mn></mrow><annotation
   encoding="application/x-tex">\text{FA}=0.583</annotation></semantics> :MATH]
   at
   [MATH: <semantics><mrow><mi>θ</mi><mo>=</mo><mn>0.864</mn></mrow><annotation
   encoding="application/x-tex">\theta=0.864</annotation></semantics> :MATH]
   (the BGE-large-calibrated threshold where unrelated
   [MATH: <semantics><mrow><mtext>FA</mtext><mo>=</mo><mn>0</mn></mrow><annotation
   encoding="application/x-tex">\text{FA}=0</annotation></semantics> :MATH]
   ), matching HIDE exactly. For the graph memory,
   [MATH: <semantics><mrow><mtext>FA</mtext><mo>=</mo><mn>0.208</mn></mrow><annotation
   encoding="application/x-tex">\text{FA}=0.208</annotation></semantics> :MATH]
   at
   [MATH: <semantics><mrow><mi>θ</mi><mo>=</mo><mn>0.82</mn></mrow><annotation
   encoding="application/x-tex">\theta=0.82</annotation></semantics> :MATH]
   . The nearly
   [MATH: <semantics><mrow><mn>3</mn><mo lspace="0.222em">×</mo></mrow><annotation
   encoding="application/x-tex">3\times</annotation></semantics> :MATH]
   difference between the two Category 1 architectures reflects different threshold calibrations and different
   semantic clustering geometries: BGE-large’s contrastive training produces tighter semantic clusters than
   MiniLM, placing lures closer to studied items relative to the threshold. Both rates substantially exceed what
   any SPP-free system could produce (
   [MATH: <semantics><mrow><mtext>FA</mtext><mo>=</mo><mn>0</mn></mrow><annotation
   encoding="application/x-tex">\text{FA}=0</annotation></semantics> :MATH]
   ), and the spherical cap analysis confirms that all
   [MATH: <semantics><mrow><mn>24</mn><mo>/</mo><mn>24</mn></mrow><annotation
   encoding="application/x-tex">24/24</annotation></semantics> :MATH]
   lures across both architectures lie within the predicted cap intersection of their studied associates.
   Theorem 6 is confirmed without exception.

   For the LLM architectures (attention, parametric),
   [MATH: <semantics><mrow><mtext>FA</mtext><mo>=</mo><mn>0.000</mn></mrow><annotation
   encoding="application/x-tex">\text{FA}=0.000</annotation></semantics> :MATH]
   at the behavioural level: the model correctly identifies that “sleep” was not in the word list. But this does
   not violate the theorem. The theorem applies to the representation geometry, and the geometric prediction
   holds: lures are indistinguishable from studied items in the hidden-state space. The behavioural override
   requires explicit list-checking, a reasoning capability that operates on top of the geometric vulnerability,
   not in place of it. A system without this reasoning layer (e.g., a vector database, a knowledge graph, or a
   retrieval pipeline) has no such override. The DRM result has the same important asymmetry noted in HIDE: it
   requires no boundary conditions. Forgetting requires competitors. False recall requires only the geometry of
   meaning. SPP alone guarantees semantic proximity but not threshold inseparability. The formal guarantee
   requires the stronger
   [MATH: <semantics><mi>δ</mi><annotation encoding="application/x-tex">\delta</annotation></semantics> :MATH]
   -convexity condition (Axiom A5, Theorem 6), which we verify empirically: for all
   [MATH: <semantics><mn>24</mn><annotation encoding="application/x-tex">24</annotation></semantics> :MATH]
   DRM lures, the convex-hull reconstruction error
   [MATH: <semantics><msup><mi>δ</mi><mo>∗</mo></msup><annotation
   encoding="application/x-tex">\delta^{*}</annotation></semantics> :MATH]
   is smaller than the observed decision margin
   [MATH: <semantics><mi>m</mi><annotation encoding="application/x-tex">m</annotation></semantics> :MATH]
   .

   A natural question arises: if LLMs escape DRM false recall via explicit reasoning (FA
   [MATH: <semantics><mrow><mi></mi><mo>=</mo><mn>0.000</mn></mrow><annotation
   encoding="application/x-tex">=0.000</annotation></semantics> :MATH]
   ), why do humans, who also reason, show FA
   [MATH: <semantics><mrow><mi></mi><mo>≈</mo><mn>0.55</mn></mrow><annotation encoding="application/x-tex">\approx
   0.55</annotation></semantics> :MATH]
   ? The answer has two parts. First, human source monitoring is not a separate symbolic layer operating on top of
   the memory system; it shares the same geometric substrate, so the lure’s representation is already
   indistinguishable from studied items before the monitoring system engages. The LLM, by contrast, has access to
   the literal token sequence in its context window, a symbolic record external to the embedding space that
   permits exact matching. Human episodic memory has no such external record. Second, explicit source monitoring
   in humans is metabolically expensive and is not automatically deployed during recognition tasks; the DRM
   paradigm exploits precisely this.

The spacing effect reflects temporal interference geometry

   In architectures where temporal interference is expressed through graded retrieval competition, distributed
   practice beats massed practice. For the vector database with
   [MATH: <semantics><mrow><mn>10</mn><mo>,</mo><mn>000</mn></mrow><annotation
   encoding="application/x-tex">10{,}000</annotation></semantics> :MATH]
   distractors and age-proportional noise (
   [MATH: <semantics><mrow><mi>σ</mi><mo>=</mo><mn>0.25</mn></mrow><annotation
   encoding="application/x-tex">\sigma=0.25</annotation></semantics> :MATH]
   ): massed
   [MATH:
   <semantics><mrow><mi></mi><mo>=</mo><mrow><mn>0.360</mn><mo>±</mo><mn>0.022</mn></mrow></mrow><annotation
   encoding="application/x-tex">=0.360\pm 0.022</annotation></semantics> :MATH]
   , long-spacing
   [MATH:
   <semantics><mrow><mi></mi><mo>=</mo><mrow><mn>0.902</mn><mo>±</mo><mn>0.039</mn></mrow></mrow><annotation
   encoding="application/x-tex">=0.902\pm 0.039</annotation></semantics> :MATH]
   (Cohen’s
   [MATH: <semantics><mrow><mi>d</mi><mo>=</mo><mn>24.6</mn></mrow><annotation
   encoding="application/x-tex">d=24.6</annotation></semantics> :MATH]
   ,
   [MATH: <semantics><mrow><mi>n</mi><mo>=</mo><mn>5</mn></mrow><annotation
   encoding="application/x-tex">n=5</annotation></semantics> :MATH]
   seeds). The mechanism is geometric: spaced repetitions create traces at different temporal positions; massed
   traces are uniformly old (
   [MATH: <semantics><mrow><mi></mi><mo>∼</mo><mn>30</mn></mrow><annotation encoding="application/x-tex">\sim
   30</annotation></semantics> :MATH]
   days) and uniformly degraded. For the graph memory: long
   [MATH: <semantics><mrow><mi></mi><mo>=</mo><mn>0.996</mn></mrow><annotation
   encoding="application/x-tex">=0.996</annotation></semantics> :MATH]
   , massed
   [MATH: <semantics><mrow><mi></mi><mo>=</mo><mn>0.920</mn></mrow><annotation
   encoding="application/x-tex">=0.920</annotation></semantics> :MATH]
   , same direction, smaller magnitude.

   The attention architecture shows the opposite pattern: massed
   [MATH: <semantics><mrow><mi></mi><mo>=</mo><mn>1.000</mn></mrow><annotation
   encoding="application/x-tex">=1.000</annotation></semantics> :MATH]
   , all spaced conditions
   [MATH: <semantics><mrow><mi></mi><mo>=</mo><mn>0.000</mn></mrow><annotation
   encoding="application/x-tex">=0.000</annotation></semantics> :MATH]
   . This is an architectural capacity artefact, not a refutation of the spacing prediction: the context window
   imposes a hard limit on token distance, and spaced repetitions with intervening fillers push the target beyond
   the attention horizon. The result does not bear on the geometric spacing prediction; it reveals instead how
   context-window limits create a different interference geometry, relocating interference from the temporal
   domain to the capacity domain. The filesystem (BM25) shows all conditions at
   [MATH: <semantics><mn>1.000</mn><annotation encoding="application/x-tex">1.000</annotation></semantics> :MATH]
   ; keyword matching is unaffected by spacing. Both “failures” are informative: they reveal the specific
   architectural constraints that determine how the geometric vulnerability manifests behaviourally.

The dimensionality convergence

   The label “3,584-dimensional” is, in a functionally meaningful sense, a misnomer. Despite nominal
   dimensionalities spanning an order of magnitude (
   [MATH: <semantics><mn>384</mn><annotation encoding="application/x-tex">384</annotation></semantics> :MATH]
   for MiniLM to
   [MATH: <semantics><mrow><mn>3</mn><mo>,</mo><mn>584</mn></mrow><annotation
   encoding="application/x-tex">3{,}584</annotation></semantics> :MATH]
   for Qwen2.5 hidden states), effective dimensionality converges dramatically. BGE-large:
   [MATH: <semantics><mrow><msub><mi>d</mi><mtext>eff</mtext></msub><mo>=</mo><mn>158</mn></mrow><annotation
   encoding="application/x-tex">d_{\text{eff}}=158</annotation></semantics> :MATH]
   (participation ratio),
   [MATH: <semantics><mrow><msub><mi>d</mi><mtext>eff</mtext></msub><mo>=</mo><mn>10.6</mn></mrow><annotation
   encoding="application/x-tex">d_{\text{eff}}=10.6</annotation></semantics> :MATH]
   (Levina–Bickel^8). MiniLM:
   [MATH: <semantics><mrow><msub><mi>d</mi><mtext>eff</mtext></msub><mo>=</mo><mn>127</mn></mrow><annotation
   encoding="application/x-tex">d_{\text{eff}}=127</annotation></semantics> :MATH]
   . Qwen2.5-7B hidden states:
   [MATH: <semantics><mrow><msub><mi>d</mi><mtext>eff</mtext></msub><mo>=</mo><mn>17.9</mn></mrow><annotation
   encoding="application/x-tex">d_{\text{eff}}=17.9</annotation></semantics> :MATH]
   , a
   [MATH: <semantics><mn>200</mn><annotation encoding="application/x-tex">200</annotation></semantics> :MATH]
   -fold compression. The Levina–Bickel estimator, which measures local manifold dimensionality, gives
   [MATH: <semantics><mrow><msub><mi>d</mi><mtext>eff</mtext></msub><mo>≈</mo><mn>10</mn></mrow><annotation
   encoding="application/x-tex">d_{\text{eff}}\approx 10</annotation></semantics> :MATH]
   –
   [MATH: <semantics><mn>15</mn><annotation encoding="application/x-tex">15</annotation></semantics> :MATH]
   across all models, consistent with the rate-distortion bound (Theorem 1). Biological neural populations operate
   at estimated
   [MATH: <semantics><mrow><msub><mi>d</mi><mtext>eff</mtext></msub><mo>=</mo><mn>100</mn></mrow><annotation
   encoding="application/x-tex">d_{\text{eff}}=100</annotation></semantics> :MATH]
   –
   [MATH: <semantics><mn>500</mn><annotation encoding="application/x-tex">500</annotation></semantics> :MATH]
   ^19, 7, placing them near the transition zone. The convergence is not coincidental: any SPP-satisfying encoding
   must concentrate variance in the
   [MATH: <semantics><mrow><mi></mi><mo>∼</mo><mn>10</mn></mrow><annotation
   encoding="application/x-tex">{\sim}10</annotation></semantics> :MATH]
   –
   [MATH: <semantics><mn>50</mn><annotation encoding="application/x-tex">50</annotation></semantics> :MATH]
   semantically meaningful directions.

   A note on estimator discrepancy is warranted. HIDE reported
   [MATH: <semantics><mrow><msub><mi>d</mi><mtext>eff</mtext></msub><mo>≈</mo><mn>16</mn></mrow><annotation
   encoding="application/x-tex">d_{\text{eff}}\approx 16</annotation></semantics> :MATH]
   for BGE-large; this paper reports
   [MATH: <semantics><mrow><msub><mi>d</mi><mtext>eff</mtext></msub><mo>=</mo><mn>158</mn></mrow><annotation
   encoding="application/x-tex">d_{\text{eff}}=158</annotation></semantics> :MATH]
   (participation ratio) and
   [MATH: <semantics><mrow><msub><mi>d</mi><mtext>eff</mtext></msub><mo>=</mo><mn>10.6</mn></mrow><annotation
   encoding="application/x-tex">d_{\text{eff}}=10.6</annotation></semantics> :MATH]
   (Levina–Bickel) for the same model. The discrepancy is methodological, not contradictory. The participation
   ratio measures global variance concentration (how many dimensions carry substantial eigenvalue mass) and is
   sensitive to the long tail of small but non-zero eigenvalues. The Levina–Bickel estimator measures local
   manifold dimensionality (the number of directions along which the data actually varies in a neighbourhood).
   HIDE’s value of
   [MATH: <semantics><mrow><mi></mi><mo>≈</mo><mn>16</mn></mrow><annotation encoding="application/x-tex">\approx
   16</annotation></semantics> :MATH]
   was computed on PCA-projected embeddings, which truncates the tail. For the interference theorems, the
   Levina–Bickel estimate (
   [MATH: <semantics><mrow><mi></mi><mo>≈</mo><mn>10</mn></mrow><annotation encoding="application/x-tex">\approx
   10</annotation></semantics> :MATH]
   –
   [MATH: <semantics><mn>15</mn><annotation encoding="application/x-tex">15</annotation></semantics> :MATH]
   ) is the governing quantity, and the reason is mathematical, not merely methodological: interference occurs in
   local neighbourhoods (the
   [MATH: <semantics><mi>θ</mi><annotation encoding="application/x-tex">\theta</annotation></semantics> :MATH]
   -cap of Theorem 2), and the crowding within these neighbourhoods is determined by the local manifold
   dimensionality, not by the global variance spread. The participation ratio captures the latter; Levina–Bickel
   captures the former. Plugging
   [MATH: <semantics><mrow><msub><mi>d</mi><mtext>eff</mtext></msub><mo>=</mo><mn>158</mn></mrow><annotation
   encoding="application/x-tex">d_{\text{eff}}=158</annotation></semantics> :MATH]
   into the spherical cap formula would dramatically underestimate interference, because the global variance
   includes dimensions along which nearby items do not actually vary. The correct input to Theorem 2 is the local
   intrinsic dimensionality (
   [MATH: <semantics><mrow><mi></mi><mo>≈</mo><mn>10</mn></mrow><annotation encoding="application/x-tex">\approx
   10</annotation></semantics> :MATH]
   –
   [MATH: <semantics><mn>15</mn><annotation encoding="application/x-tex">15</annotation></semantics> :MATH]
   ), and all three estimators confirm that this value places these systems in the interference-vulnerable regime
   (
   [MATH: <semantics><mrow><msub><mi>d</mi><mtext>eff</mtext></msub><mo><</mo><mn>100</mn></mrow><annotation
   encoding="application/x-tex">d_{\text{eff}}<100</annotation></semantics> :MATH]
   ).

Tested interventions reveal a usefulness-immunity tradeoff

   Every cure for memory’s “flaws” either fails or kills the patient.

   Solution 1: Increase nominal dimensionality. Zero-padding BGE-large from
   [MATH: <semantics><mrow><mn>1</mn><mo>,</mo><mn>024</mn></mrow><annotation
   encoding="application/x-tex">1{,}024</annotation></semantics> :MATH]
   to
   [MATH: <semantics><mrow><mn>4</mn><mo>,</mo><mn>096</mn></mrow><annotation
   encoding="application/x-tex">4{,}096</annotation></semantics> :MATH]
   dimensions:
   [MATH: <semantics><mi>b</mi><annotation encoding="application/x-tex">b</annotation></semantics> :MATH]
   stays at
   [MATH: <semantics><mrow><mi></mi><mo>∼</mo><mn>0.31</mn></mrow><annotation
   encoding="application/x-tex">{\sim}0.31</annotation></semantics> :MATH]
   because
   [MATH: <semantics><msub><mi>d</mi><mtext>eff</mtext></msub><annotation
   encoding="application/x-tex">d_{\text{eff}}</annotation></semantics> :MATH]
   is unchanged (
   [MATH: <semantics><mn>124</mn><annotation encoding="application/x-tex">124</annotation></semantics> :MATH]
   in both cases). Only PCA reduction to
   [MATH: <semantics><mn>64</mn><annotation encoding="application/x-tex">64</annotation></semantics> :MATH]
   dimensions changes
   [MATH: <semantics><mi>b</mi><annotation encoding="application/x-tex">b</annotation></semantics> :MATH]
   (
   [MATH: <semantics><mn>0.370</mn><annotation encoding="application/x-tex">0.370</annotation></semantics> :MATH]
   ), by genuinely reducing the space, not by padding it.

   Solution 2: BM25 keyword retrieval. Eliminates DRM false recall (
   [MATH: <semantics><mrow><mtext>FA</mtext><mo>=</mo><mn>0</mn></mrow><annotation
   encoding="application/x-tex">\text{FA}=0</annotation></semantics> :MATH]
   ) and forgetting (
   [MATH: <semantics><mrow><mi>b</mi><mo>=</mo><mn>0</mn></mrow><annotation
   encoding="application/x-tex">b=0</annotation></semantics> :MATH]
   ). But semantic retrieval agreement:
   [MATH: <semantics><mrow><mn>15.5</mn><mo>%</mo></mrow><annotation
   encoding="application/x-tex">15.5\%</annotation></semantics> :MATH]
   . This is Architecture 3’s result rephrased as a solution.

   Solution 3: Orthogonalisation. Gram–Schmidt reduces interference to zero (mean off-diagonal cosine
   [MATH:
   <semantics><mrow><mi></mi><mo><</mo><msup><mn>10</mn><mrow><mo>−</mo><mn>4</mn></mrow></msup></mrow><annotation
   encoding="application/x-tex"><10^{-4}</annotation></semantics> :MATH]
   ) but nearest-neighbour accuracy drops to
   [MATH: <semantics><mrow><mn>0.0</mn><mo>%</mo></mrow><annotation
   encoding="application/x-tex">0.0\%</annotation></semantics> :MATH]
   . Random projection to
   [MATH: <semantics><mn>256</mn><annotation encoding="application/x-tex">256</annotation></semantics> :MATH]
   dimensions preserves
   [MATH: <semantics><mrow><mn>68</mn><mo>%</mo></mrow><annotation
   encoding="application/x-tex">68\%</annotation></semantics> :MATH]
   accuracy but
   [MATH: <semantics><mrow><msub><mi>d</mi><mtext>eff</mtext></msub><mo>=</mo><mn>77</mn></mrow><annotation
   encoding="application/x-tex">d_{\text{eff}}=77</annotation></semantics> :MATH]
   , still in the interference regime.

   Solution 4: Memory compression. At
   [MATH: <semantics><mn>50</mn><annotation encoding="application/x-tex">50</annotation></semantics> :MATH]
   clusters:
   [MATH: <semantics><mrow><mi>b</mi><mo>=</mo><mn>0.432</mn></mrow><annotation
   encoding="application/x-tex">b=0.432</annotation></semantics> :MATH]
   , retrieval accuracy
   [MATH: <semantics><mrow><mi></mi><mo>=</mo><mn>0.988</mn></mrow><annotation
   encoding="application/x-tex">=0.988</annotation></semantics> :MATH]
   . At
   [MATH: <semantics><mrow><mn>2</mn><mo>,</mo><mn>500</mn></mrow><annotation
   encoding="application/x-tex">2{,}500</annotation></semantics> :MATH]
   clusters:
   [MATH: <semantics><mrow><mi>b</mi><mo>=</mo><mn>0.163</mn></mrow><annotation
   encoding="application/x-tex">b=0.163</annotation></semantics> :MATH]
   , accuracy
   [MATH: <semantics><mrow><mi></mi><mo>=</mo><mn>0.928</mn></mrow><annotation
   encoding="application/x-tex">=0.928</annotation></semantics> :MATH]
   . The tradeoff is monotonic: you can reduce
   [MATH: <semantics><mi>b</mi><annotation encoding="application/x-tex">b</annotation></semantics> :MATH]
   by compressing, but you lose specific-fact retrieval.

   Every solution traces a strict Pareto frontier between interference immunity and semantic usefulness.
   Compression at
   [MATH: <semantics><mrow><mi>k</mi><mo>=</mo><mrow><mn>2</mn><mo>,</mo><mn>500</mn></mrow></mrow><annotation
   encoding="application/x-tex">k=2{,}500</annotation></semantics> :MATH]
   achieves
   [MATH: <semantics><mrow><mi>b</mi><mo>=</mo><mn>0.163</mn></mrow><annotation
   encoding="application/x-tex">b=0.163</annotation></semantics> :MATH]
   with
   [MATH: <semantics><mrow><mn>92.8</mn><mo>%</mo></mrow><annotation
   encoding="application/x-tex">92.8\%</annotation></semantics> :MATH]
   accuracy, a potentially acceptable engineering compromise for specific applications, but not mathematical
   immunity. The theorem does not claim that interference cannot be reduced; it claims it cannot be eliminated
   without sacrificing SPP. The tradeoff frontier itself is the No-Escape Theorem in empirical form.

Discussion

   We use strong language at points because the claim is structural: within the theorem class, the tradeoff is not
   an empirical accident but a consequence of the retrieval geometry.

   The central result of this paper is that semantically organised memory has a structural vulnerability to
   interference, and that this vulnerability appears at two levels. At the geometric level, semantically useful
   representations with finite effective rank create retrieval neighbourhoods with non-zero competitor mass and
   non-trivial lure overlap. At the behavioural level, different architectures express that vulnerability
   differently. Pure retrieval systems express it directly as smooth forgetting and false recall; systems with
   explicit reasoning can partially compensate, but often replace graceful degradation with brittle failure modes;
   systems that avoid the vulnerability entirely do so by giving up semantic generalisation.

   The broader implication is a limit on the naive reading of the Bitter Lesson for memory systems. The Bitter
   Lesson correctly emphasises the long-run power of general methods plus computation. Our result does not argue
   against that principle. It argues that within semantically organised memory, scale alone is not sufficient. The
   same geometry that enables semantic generalisation also creates representational crowding, competitor mass, and
   lure proximity. Therefore larger models and more data may improve performance, but they do not in themselves
   remove interference as a class of phenomena. Beyond a point, memory requires architectural innovation, not
   scale alone. The comparison across architectures is best read as a map of how a shared geometric pressure
   manifests across architectures, not as a single unified leaderboard.

   The resolution of the interference-versus-decay debate^20, 4 is now concrete. Decay alone produces
   [MATH: <semantics><mrow><mi>b</mi><mo><</mo><mn>0.01</mn></mrow><annotation
   encoding="application/x-tex">b<0.01</annotation></semantics> :MATH]
   ; interference produces
   [MATH: <semantics><mrow><mi>b</mi><mo>=</mo><mn>0.440</mn></mrow><annotation
   encoding="application/x-tex">b=0.440</annotation></semantics> :MATH]
   –
   [MATH: <semantics><mn>0.478</mn><annotation encoding="application/x-tex">0.478</annotation></semantics> :MATH]
   in the human range. Geometry plus power-law arrival gives stretched-exponential retention for individual items.
   The empirically observed power law emerges after averaging over item-level heterogeneity in interference scale,
   a standard scale-mixture mechanism (Proposition 5). This sharpens rather than weakens the theory: it identifies
   exactly which part of the forgetting law is geometric (the hazard scale
   [MATH: <semantics><mrow><mi>μ</mi><mo lspace="0em" rspace="0em">​</mo><mrow><mo
   stretchy="false">(</mo><msub><mi>C</mi><mi>x</mi></msub><mo stretchy="false">)</mo></mrow></mrow><annotation
   encoding="application/x-tex">\mu(C_{x})</annotation></semantics> :MATH]
   ), which part is environmental (
   [MATH: <semantics><mi>α</mi><annotation encoding="application/x-tex">\alpha</annotation></semantics> :MATH]
   ), and which part is population-level (
   [MATH: <semantics><mi>β</mi><annotation encoding="application/x-tex">\beta</annotation></semantics> :MATH]
   ). The parametric result is perhaps the most striking: Qwen2.5-7B’s accuracy on factual questions drops from
   [MATH: <semantics><mn>1.000</mn><annotation encoding="application/x-tex">1.000</annotation></semantics> :MATH]
   to
   [MATH: <semantics><mn>0.113</mn><annotation encoding="application/x-tex">0.113</annotation></semantics> :MATH]
   as the density of semantically similar facts in the training corpus increases. This is interference in model
   weights: not in an external store, not in a context window, but in the parameters themselves. The complementary
   learning systems hypothesis^10 can be reinterpreted: fast hippocampal encoding and slow neocortical
   consolidation manage the interference-usefulness tradeoff, they do not eliminate interference. Even the brain’s
   most sophisticated consolidation mechanism (replay-guided refinement with importance weighting^10) does not
   escape interference; it manages the position on the tradeoff frontier that the no-escape theorem establishes.
   We note that the cited
   [MATH: <semantics><mrow><msub><mi>d</mi><mtext>eff</mtext></msub><mo>=</mo><mn>100</mn></mrow><annotation
   encoding="application/x-tex">d_{\text{eff}}=100</annotation></semantics> :MATH]
   –
   [MATH: <semantics><mn>500</mn><annotation encoding="application/x-tex">500</annotation></semantics> :MATH]
   range derives from visual cortex recordings^19, 7. Memory-related structures (hippocampus, entorhinal cortex)
   may have different effective dimensionalities; hippocampal place cells, for instance, are thought to operate in
   lower-dimensional manifolds. The interference prediction holds for any
   [MATH: <semantics><msub><mi>d</mi><mtext>eff</mtext></msub><annotation
   encoding="application/x-tex">d_{\text{eff}}</annotation></semantics> :MATH]
   below
   [MATH: <semantics><mrow><mi></mi><mo>∼</mo><mn>100</mn></mrow><annotation
   encoding="application/x-tex">{\sim}100</annotation></semantics> :MATH]
   , so the conclusion is robust to variation in the biological estimate.

   The DRM result has an asymmetry first noted in HIDE that the two-level framework clarifies. False recall
   requires no boundary conditions: it holds for noiseless, competitor-free systems (Theorem 6). This makes it
   more fundamental than forgetting. LLMs equipped with explicit list-checking or an external symbolic record do
   not refute the theorem; they instantiate a behavioural workaround outside the pure kernel-threshold retrieval
   class. The theorem concerns the semantic memory substrate. Workarounds can route around its vulnerabilities,
   but only by adding an auxiliary mechanism not described by the substrate alone. Production systems that rely on
   semantically continuous retrieval are expected to inherit related pressures. The implication is that complete
   immunity to false recall typically requires leaving the semantic retrieval regime or adding external
   verification^16.

   The parametric TOT rate (
   [MATH: <semantics><mrow><mn>69</mn><mo>%</mo></mrow><annotation
   encoding="application/x-tex">69\%</annotation></semantics> :MATH]
   ) deserves explicit discussion. This rate (
   [MATH: <semantics><mrow><mn>18</mn><mo lspace="0.222em">×</mo></mrow><annotation
   encoding="application/x-tex">18\times</annotation></semantics> :MATH]
   the human baseline and
   [MATH: <semantics><mrow><mn>34</mn><mo lspace="0.222em">×</mo></mrow><annotation
   encoding="application/x-tex">34\times</annotation></semantics> :MATH]
   the vector database rate) reflects a systemic property of parametric models (not specific to Qwen): all such
   models store facts as superposed weight-space associations. When queried, multiple associations activate
   simultaneously, producing partial retrieval at far higher rates than architectures with explicit, separated
   memory stores. The operational definition of TOT transfers imperfectly to parametric systems: “correct category
   but wrong specific answer” captures a different failure mode than the phenomenological tip-of-tongue experience
   in humans. The elevated rate is thus informative about the geometry of weight-space retrieval rather than
   directly comparable to human TOT rates. We flag this definitional caveat explicitly: the parametric TOT entry
   in Figure 7 should be interpreted with caution, as it reflects a categorically different operational definition
   from the phenomenological TOT experience measured in humans and the geometric near-miss definition used for
   embedding architectures.

   One consideration not addressed by the five-architecture survey is hybrid retrieval: most production systems
   combine architectures (e.g., BM25 keyword pre-filtering followed by dense vector re-ranking). Such systems
   attempt to navigate the tradeoff frontier by falling back on Category 3 retrieval (keyword matching) when
   Category 1 retrieval (semantic similarity) suffers geometric interference. However, combining them does not
   violate the No-Escape Theorem; it builds a routing layer between a system that forgets and a system that cannot
   generalise. The semantic component remains subject to Theorems 1–4 whenever it is invoked, and the keyword
   component contributes only non-semantic retrieval when it is. The hybrid reduces the frequency of interference
   events at the cost of reducing the frequency of semantic generalisation, another point on the tradeoff
   frontier, not an escape from it.

   Several anticipated objections deserve response. First, one might argue SPP is too weak. Any stronger
   definition implies SPP as a special case; the theorem applies a fortiori. Second, Theorem 1 might appear to
   prove only finiteness. The rate-distortion argument^18, 1 proves smallness: intrinsic dimensionality
   [MATH: <semantics><mrow><mi></mi><mo>∼</mo><mn>10</mn></mrow><annotation
   encoding="application/x-tex">{\sim}10</annotation></semantics> :MATH]
   –
   [MATH: <semantics><mn>50</mn><annotation encoding="application/x-tex">50</annotation></semantics> :MATH]
   ^8 bounds
   [MATH: <semantics><msub><mi>d</mi><mtext>eff</mtext></msub><annotation
   encoding="application/x-tex">d_{\text{eff}}</annotation></semantics> :MATH]
   regardless of hardware. Third, the exponential-to-power-law conversion relies on Anderson–Schooler statistics,
   which we verify (
   [MATH: <semantics><mrow><mi>α</mi><mo>=</mo><mn>0.459</mn></mrow><annotation
   encoding="application/x-tex">\alpha=0.459</annotation></semantics> :MATH]
   ). Fourth, we use spherical caps, not convex hulls; the distinction matters for angular similarity. Fifth,
   attention is not cosine similarity, but SPP is the key property, verified for all architectures (
   [MATH: <semantics><mrow><mi>p</mi><mo><</mo><mn>0.001</mn></mrow><annotation
   encoding="application/x-tex">p<0.001</annotation></semantics> :MATH]
   ). Sixth, LLM DRM confounds parametric and episodic memory; this is precisely why the two-level framework
   matters. Seventh, the connection to bias-variance tradeoff is real but our contribution is specific
   quantitative predictions from first principles.

Implications for system design

   The no-escape theorem translates into specific, actionable predictions for retrieval system engineers. First,
   the severity of forgetting, captured by the prefactor
   [MATH: <semantics><mrow><mi>A</mi><mo>=</mo><mrow><mrow><mrow><msub><mi>p</mi><mtext>near</mtext></msub><mo
   lspace="0em" rspace="0em">​</mo><mrow><mo stretchy="false">(</mo><msub><mi>d</mi><mtext>eff</mtext></msub><mo
   rspace="0.055em" stretchy="false">)</mo></mrow></mrow><mo
   rspace="0.222em">⋅</mo><msub><mi>λ</mi><mn>0</mn></msub></mrow><mo>/</mo><mrow><mo
   stretchy="false">(</mo><mrow><mn>1</mn><mo>−</mo><mi>α</mi></mrow><mo
   stretchy="false">)</mo></mrow></mrow></mrow><annotation
   encoding="application/x-tex">A=p_{\text{near}}(d_{\text{eff}})\cdot\lambda_{0}/(1-\alpha)</annotation></semanti
   cs> :MATH]
   , scales with
   [MATH: <semantics><msub><mi>p</mi><mtext>near</mtext></msub><annotation
   encoding="application/x-tex">p_{\text{near}}</annotation></semantics> :MATH]
   : for a database with
   [MATH: <semantics><mrow><msub><mi>d</mi><mtext>eff</mtext></msub><mo>≈</mo><mn>16</mn></mrow><annotation
   encoding="application/x-tex">d_{\text{eff}}\approx 16</annotation></semantics> :MATH]
   and
   [MATH: <semantics><mrow><mn>10</mn><mo>,</mo><mn>000</mn></mrow><annotation
   encoding="application/x-tex">10{,}000</annotation></semantics> :MATH]
   entries,
   [MATH: <semantics><mi>A</mi><annotation encoding="application/x-tex">A</annotation></semantics> :MATH]
   reaches values consistent with the empirically observed
   [MATH: <semantics><mrow><mi>b</mi><mo>≈</mo><mn>0.44</mn></mrow><annotation
   encoding="application/x-tex">b\approx 0.44</annotation></semantics> :MATH]
   over realistic time windows. Retrieval accuracy will degrade as a power law with database age; re-ranking,
   metadata filters, and structured memory can materially change behaviour, but within the kernel-threshold class
   they navigate the tradeoff frontier rather than escaping it. Second, any SPP-satisfying retrieval system will
   produce false positives for semantically associated queries at rates comparable to its true positive rate; the
   DRM prediction applies directly to production RAG systems. Third, increasing nominal dimensionality is provably
   not a solution (Solution 1): only training objectives that genuinely increase the effective rank of stored
   representations (a target that current contrastive objectives do not optimise for, and which the low intrinsic
   dimensionality of natural language makes difficult to achieve) can reduce interference. The gap between
   “inevitable” and “catastrophic” is where engineering contributes: optimising noise parameters, managing
   competitor density through intelligent caching, and designing consolidation strategies that navigate the
   compression–fidelity frontier (Solution 4).

   The standard engineering response to forgetting and false recall is to treat them as bugs and try to fix them.
   Our results suggest they are not bugs. They are the cost of admission. Any memory system that organises
   information by meaning will, as it grows, forget old items through interference and falsely recognise items it
   never stored. These are not signs of a broken system; they are signs of a system that is doing what it was
   designed to do, namely represent meaning geometrically, under the constraints that geometry imposes. Systems
   can mitigate interference, reroute around it, or trade semantic capability for robustness, but within the
   kernel-threshold regime they cannot eliminate it for free. The price of meaning is interference. Within this
   theorem class, there is no escape.

Methods

Models and architectures

   Five memory architectures were implemented. Architecture 1 (Vector Database): BAAI/bge-large-en-v1.5^21 (
   [MATH: <semantics><mrow><mn>1</mn><mo>,</mo><mn>024</mn></mrow><annotation
   encoding="application/x-tex">1{,}024</annotation></semantics> :MATH]
   dim, MIT licence). Cosine similarity retrieval with temporal decay
   [MATH: <semantics><mrow><mrow><mi>S</mi><mo lspace="0em" rspace="0em">​</mo><mrow><mo
   stretchy="false">(</mo><mi>t</mi><mo stretchy="false">)</mo></mrow></mrow><mo>=</mo><msup><mrow><mo
   stretchy="false">(</mo><mrow><mn>1</mn><mo>+</mo><mrow><mi>β</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>t</mi></mrow></mrow><mo
   stretchy="false">)</mo></mrow><mrow><mo>−</mo><mi>ψ</mi></mrow></msup></mrow><annotation
   encoding="application/x-tex">S(t)=(1+\beta t)^{-\psi}</annotation></semantics> :MATH]
   ,
   [MATH: <semantics><mrow><mi>β</mi><mo>=</mo><mn>0.20</mn></mrow><annotation
   encoding="application/x-tex">\beta=0.20</annotation></semantics> :MATH]
   ,
   [MATH: <semantics><mrow><mi>ψ</mi><mo>=</mo><mn>0.5</mn></mrow><annotation
   encoding="application/x-tex">\psi=0.5</annotation></semantics> :MATH]
   . Age-proportional noise:
   [MATH: <semantics><mrow><mi class="ltx_mathvariant_bold-italic"
   mathvariant="bold-italic">ϵ</mi><mo>=</mo><mrow><mrow><mo stretchy="false">(</mo><mrow><mrow><mi>σ</mi><mo
   lspace="0em"
   rspace="0em">​</mo><msqrt><mrow><mi>a</mi><mo>+</mo><mn>0.01</mn></mrow></msqrt></mrow><mo>/</mo><msqrt><mi>d</
   mi></msqrt></mrow><mo stretchy="false">)</mo></mrow><mo lspace="0em"
   rspace="0em">​</mo><mi>𝐳</mi></mrow></mrow><annotation
   encoding="application/x-tex">\boldsymbol{\epsilon}=(\sigma\sqrt{a+0.01}/\sqrt{d})\mathbf{z}</annotation></seman
   tics> :MATH]
   ,
   [MATH: <semantics><mrow><mi>σ</mi><mo>=</mo><mn>0.5</mn></mrow><annotation
   encoding="application/x-tex">\sigma=0.5</annotation></semantics> :MATH]
   . Stored in HIDESpace^3. Architecture 2 (Attention Memory): Qwen2.5-7B-Instruct^13 (Apache 2.0, fp16). Facts in
   context window; retrieval via generation. Proximity: cosine of middle-layer hidden states (
   [MATH: <semantics><mrow><mi>d</mi><mo>=</mo><mrow><mn>3</mn><mo>,</mo><mn>584</mn></mrow></mrow><annotation
   encoding="application/x-tex">d=3{,}584</annotation></semantics> :MATH]
   ). Architecture 3 (Filesystem Memory): JSON records. BM25 keyword search (rank_bm25, top-
   [MATH: <semantics><mn>50</mn><annotation encoding="application/x-tex">50</annotation></semantics> :MATH]
   )
   [MATH: <semantics><mo stretchy="false">→</mo><annotation
   encoding="application/x-tex">\to</annotation></semantics> :MATH]
   Qwen2.5-7B relevance re-ranking (
   [MATH: <semantics><mn>1</mn><annotation encoding="application/x-tex">1</annotation></semantics> :MATH]
   –
   [MATH: <semantics><mn>10</mn><annotation encoding="application/x-tex">10</annotation></semantics> :MATH]
   scale, normalised to
   [MATH: <semantics><mrow><mo stretchy="false">[</mo><mn>0</mn><mo>,</mo><mn>1</mn><mo
   stretchy="false">]</mo></mrow><annotation encoding="application/x-tex">[0,1]</annotation></semantics> :MATH]
   ). Architecture 4 (Graph Memory): all-MiniLM-L6-v2^15 (
   [MATH: <semantics><mn>384</mn><annotation encoding="application/x-tex">384</annotation></semantics> :MATH]
   dim, Apache 2.0). Edges if cosine
   [MATH: <semantics><mrow><mi></mi><mo>></mo><mn>0.7</mn></mrow><annotation
   encoding="application/x-tex">>0.7</annotation></semantics> :MATH]
   ; retrieval via personalised PageRank (
   [MATH: <semantics><mrow><mi>α</mi><mo>=</mo><mn>0.85</mn></mrow><annotation
   encoding="application/x-tex">\alpha=0.85</annotation></semantics> :MATH]
   ). Architecture 5 (Parametric Memory): Qwen2.5-7B-Instruct. Knowledge in weights; probed via direct Q&A without
   RAG.

Forgetting experiments

   Embedding architectures (1, 4):
   [MATH: <semantics><mn>100</mn><annotation encoding="application/x-tex">100</annotation></semantics> :MATH]
   target facts from Wikipedia,
   [MATH: <semantics><mrow><msub><mi>n</mi><mtext>near</mtext></msub><mo>∈</mo><mrow><mo
   stretchy="false">{</mo><mn>0</mn><mo>,</mo><mn>10</mn><mo>,</mo><mn>50</mn><mo>,</mo><mn>100</mn><mo>,</mo><mn>
   200</mn><mo>,</mo><mn>500</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>000</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>000</
   mn><mo>,</mo><mn>10</mn><mo>,</mo><mn>000</mn><mo stretchy="false">}</mo></mrow></mrow><annotation
   encoding="application/x-tex">n_{\text{near}}\in\{0,10,50,100,200,500,1{,}000,5{,}000,10{,}000\}</annotation></s
   emantics> :MATH]
   competitors. Targets and competitors stored in HIDESpace. Query with noise-corrupted target embedding;
   retrieval with temporal decay. Accuracy measured at
   [MATH: <semantics><mn>10</mn><annotation encoding="application/x-tex">10</annotation></semantics> :MATH]
   age bins over
   [MATH: <semantics><mn>30</mn><annotation encoding="application/x-tex">30</annotation></semantics> :MATH]
   simulated days. Power-law fit:
   [MATH: <semantics><mrow><mrow><mi>R</mi><mo lspace="0em" rspace="0em">​</mo><mrow><mo
   stretchy="false">(</mo><mi>t</mi><mo stretchy="false">)</mo></mrow></mrow><mo>=</mo><mrow><mi>a</mi><mo
   lspace="0.222em"
   rspace="0.222em">⋅</mo><msup><mi>t</mi><mrow><mo>−</mo><mi>b</mi></mrow></msup></mrow></mrow><annotation
   encoding="application/x-tex">R(t)=a\cdot t^{-b}</annotation></semantics> :MATH]
   ^17. Decay parameter
   [MATH: <semantics><mrow><mi>β</mi><mo>=</mo><mn>0.20</mn></mrow><annotation
   encoding="application/x-tex">\beta=0.20</annotation></semantics> :MATH]
   calibrated via sweep
   [MATH: <semantics><mrow><mo stretchy="false">[</mo><mn>0.01</mn><mo>,</mo><mn>0.5</mn><mo
   stretchy="false">]</mo></mrow><annotation encoding="application/x-tex">[0.01,0.5]</annotation></semantics>
   :MATH]
   to match HIDE (
   [MATH: <semantics><mrow><mi>b</mi><mo>=</mo><mn>0.460</mn></mrow><annotation
   encoding="application/x-tex">b=0.460</annotation></semantics> :MATH]
   ). Attention architecture (2):
   [MATH: <semantics><mn>50</mn><annotation encoding="application/x-tex">50</annotation></semantics> :MATH]
   target facts
   [MATH: <semantics><mo>×</mo><annotation encoding="application/x-tex">\times</annotation></semantics> :MATH]
   [MATH: <semantics><mn>5</mn><annotation encoding="application/x-tex">5</annotation></semantics> :MATH]
   positions
   [MATH: <semantics><mo>×</mo><annotation encoding="application/x-tex">\times</annotation></semantics> :MATH]
   [MATH: <semantics><mn>7</mn><annotation encoding="application/x-tex">7</annotation></semantics> :MATH]
   [MATH: <semantics><msub><mi>n</mi><mtext>near</mtext></msub><annotation
   encoding="application/x-tex">n_{\text{near}}</annotation></semantics> :MATH]
   values
   [MATH: <semantics><mo>×</mo><annotation encoding="application/x-tex">\times</annotation></semantics> :MATH]
   [MATH: <semantics><mn>5</mn><annotation encoding="application/x-tex">5</annotation></semantics> :MATH]
   seeds. Context: system prompt
   [MATH: <semantics><mo>+</mo><annotation encoding="application/x-tex">+</annotation></semantics> :MATH]
   numbered facts
   [MATH: <semantics><mo>+</mo><annotation encoding="application/x-tex">+</annotation></semantics> :MATH]
   question. Age
   [MATH: <semantics><mo>=</mo><annotation encoding="application/x-tex">=</annotation></semantics> :MATH]
   position-normalised to
   [MATH: <semantics><mn>30</mn><annotation encoding="application/x-tex">30</annotation></semantics> :MATH]
   -day scale. Parametric architecture (5): PopQA dataset^9 (
   [MATH: <semantics><mrow><mn>14</mn><mo>,</mo><mn>267</mn></mrow><annotation
   encoding="application/x-tex">14{,}267</annotation></semantics> :MATH]
   questions). Neighbour density: BGE-large cosine
   [MATH: <semantics><mrow><mi></mi><mo>></mo><mn>0.4</mn></mrow><annotation
   encoding="application/x-tex">>0.4</annotation></semantics> :MATH]
   to Wikipedia corpus. Binned:
   [MATH: <semantics><mrow><mo stretchy="false">{</mo><mn>0</mn></mrow><annotation
   encoding="application/x-tex">\{0</annotation></semantics> :MATH]
   –
   [MATH: <semantics><mrow><mn>50</mn><mo>,</mo><mn>50</mn></mrow><annotation
   encoding="application/x-tex">50,50</annotation></semantics> :MATH]
   –
   [MATH: <semantics><mrow><mn>200</mn><mo>,</mo><mn>200</mn></mrow><annotation
   encoding="application/x-tex">200,200</annotation></semantics> :MATH]
   –
   [MATH: <semantics><mrow><mn>500</mn><mo>,</mo><mn>500</mn></mrow><annotation
   encoding="application/x-tex">500,500</annotation></semantics> :MATH]
   –
   [MATH: <semantics><mrow><mn>1</mn><mo>,</mo><mn>000</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>000</mn><mo
   rspace="0em">+</mo><mo stretchy="false">}</mo></mrow><annotation
   encoding="application/x-tex">1{,}000,1{,}000+\}</annotation></semantics> :MATH]
   . Power-law fit on bin-accuracy curve. Filesystem (3): BM25 retrieval of target among competitors; LLM
   re-ranking of top-
   [MATH: <semantics><mn>50</mn><annotation encoding="application/x-tex">50</annotation></semantics> :MATH]
   .

DRM false memory

   All
   [MATH: <semantics><mn>24</mn><annotation encoding="application/x-tex">24</annotation></semantics> :MATH]
   published lists^16 (
   [MATH: <semantics><mn>15</mn><annotation encoding="application/x-tex">15</annotation></semantics> :MATH]
   studied
   [MATH: <semantics><mo>+</mo><annotation encoding="application/x-tex">+</annotation></semantics> :MATH]
   [MATH: <semantics><mn>1</mn><annotation encoding="application/x-tex">1</annotation></semantics> :MATH]
   critical lure). Embedding architectures: Centroid similarity. Threshold sweep
   [MATH: <semantics><mrow><mi>θ</mi><mo>∈</mo><mrow><mo
   stretchy="false">[</mo><mn>0.50</mn><mo>,</mo><mn>0.95</mn><mo stretchy="false">]</mo></mrow></mrow><annotation
   encoding="application/x-tex">\theta\in[0.50,0.95]</annotation></semantics> :MATH]
   , step
   [MATH: <semantics><mn>0.01</mn><annotation encoding="application/x-tex">0.01</annotation></semantics> :MATH]
   . For BGE-large:
   [MATH: <semantics><mrow><mtext>FA</mtext><mo>=</mo><mn>0.583</mn></mrow><annotation
   encoding="application/x-tex">\text{FA}=0.583</annotation></semantics> :MATH]
   at
   [MATH: <semantics><mrow><mi>θ</mi><mo>=</mo><mn>0.864</mn></mrow><annotation
   encoding="application/x-tex">\theta=0.864</annotation></semantics> :MATH]
   . For MiniLM:
   [MATH: <semantics><mrow><mtext>FA</mtext><mo>=</mo><mn>0.208</mn></mrow><annotation
   encoding="application/x-tex">\text{FA}=0.208</annotation></semantics> :MATH]
   at
   [MATH: <semantics><mrow><mi>θ</mi><mo>=</mo><mn>0.82</mn></mrow><annotation
   encoding="application/x-tex">\theta=0.82</annotation></semantics> :MATH]
   . LLM architectures: Prompt with word list; query “Was WORD in the list? yes/no.” Parse first yes/no.
   [MATH: <semantics><mn>24</mn><annotation encoding="application/x-tex">24</annotation></semantics> :MATH]
   lists
   [MATH: <semantics><mo>×</mo><annotation encoding="application/x-tex">\times</annotation></semantics> :MATH]
   [MATH: <semantics><mn>5</mn><annotation encoding="application/x-tex">5</annotation></semantics> :MATH]
   seeds.

Spacing, TOT, dimensionality

   Spacing:
   [MATH: <semantics><mn>100</mn><annotation encoding="application/x-tex">100</annotation></semantics> :MATH]
   facts,
   [MATH: <semantics><mn>3</mn><annotation encoding="application/x-tex">3</annotation></semantics> :MATH]
   repetitions,
   [MATH: <semantics><mn>4</mn><annotation encoding="application/x-tex">4</annotation></semantics> :MATH]
   conditions (massed:
   [MATH: <mn>0</mn> :MATH]
   –
   [MATH: <semantics><mn>120</mn><annotation encoding="application/x-tex">120</annotation></semantics> :MATH]
   s; short:
   [MATH: <mn>0</mn> :MATH]
   –
   [MATH: <semantics><mn>2</mn><annotation encoding="application/x-tex">2</annotation></semantics> :MATH]
   h; medium:
   [MATH: <mn>0</mn> :MATH]
   –
   [MATH: <semantics><mn>2</mn><annotation encoding="application/x-tex">2</annotation></semantics> :MATH]
   d; long:
   [MATH: <mn>0</mn> :MATH]
   –
   [MATH: <semantics><mn>2</mn><annotation encoding="application/x-tex">2</annotation></semantics> :MATH]
   w). Test at
   [MATH: <semantics><mrow><mi>t</mi><mo>=</mo><mn>30</mn></mrow><annotation
   encoding="application/x-tex">t=30</annotation></semantics> :MATH]
   d.
   [MATH: <semantics><mrow><mn>10</mn><mo>,</mo><mn>000</mn></mrow><annotation
   encoding="application/x-tex">10{,}000</annotation></semantics> :MATH]
   distractors,
   [MATH: <semantics><mrow><mi>σ</mi><mo>=</mo><mn>0.25</mn></mrow><annotation
   encoding="application/x-tex">\sigma=0.25</annotation></semantics> :MATH]
   . TOT: Embedding architectures: PCA to
   [MATH: <semantics><mn>96</mn><annotation encoding="application/x-tex">96</annotation></semantics> :MATH]
   dim, query noise
   [MATH:
   <semantics><mrow><mi>σ</mi><mo>=</mo><mrow><mn>1.5</mn><mo>/</mo><msqrt><mn>96</mn></msqrt></mrow></mrow><annot
   ation encoding="application/x-tex">\sigma=1.5/\sqrt{96}</annotation></semantics> :MATH]
   . TOT: correct rank
   [MATH: <semantics><mn>2</mn><annotation encoding="application/x-tex">2</annotation></semantics> :MATH]
   –
   [MATH: <semantics><mn>20</mn><annotation encoding="application/x-tex">20</annotation></semantics> :MATH]
   with top-
   [MATH: <semantics><mn>1</mn><annotation encoding="application/x-tex">1</annotation></semantics> :MATH]
   sim
   [MATH: <semantics><mrow><mi></mi><mo>></mo><mn>0.5</mn></mrow><annotation
   encoding="application/x-tex">>0.5</annotation></semantics> :MATH]
   . LLM: partial-domain match in generated answer. Dimensionality: Participation ratio on covariance of
   [MATH: <semantics><mrow><mn>10</mn><mo>,</mo><mn>000</mn></mrow><annotation
   encoding="application/x-tex">10{,}000</annotation></semantics> :MATH]
   Wikipedia embeddings. Levina–Bickel two-nearest-neighbour estimator^8.
   [MATH: <semantics><msub><mi>d</mi><mn>95</mn></msub><annotation
   encoding="application/x-tex">d_{95}</annotation></semantics> :MATH]
   ,
   [MATH: <semantics><msub><mi>d</mi><mn>99</mn></msub><annotation
   encoding="application/x-tex">d_{99}</annotation></semantics> :MATH]
   : components for
   [MATH: <semantics><mrow><mn>95</mn><mo>%</mo></mrow><annotation
   encoding="application/x-tex">95\%</annotation></semantics> :MATH]
   /
   [MATH: <semantics><mrow><mn>99</mn><mo>%</mo></mrow><annotation
   encoding="application/x-tex">99\%</annotation></semantics> :MATH]
   variance.

Solution analysis

   Solution 1: PCA to
   [MATH: <semantics><mrow><mo
   stretchy="false">{</mo><mn>64</mn><mo>,</mo><mn>128</mn><mo>,</mo><mn>256</mn><mo>,</mo><mn>512</mn><mo
   stretchy="false">}</mo></mrow><annotation
   encoding="application/x-tex">\{64,128,256,512\}</annotation></semantics> :MATH]
   , zero-pad to
   [MATH: <semantics><mrow><mo
   stretchy="false">{</mo><mn>2</mn><mo>,</mo><mn>048</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>096</mn><mo
   stretchy="false">}</mo></mrow><annotation
   encoding="application/x-tex">\{2{,}048,4{,}096\}</annotation></semantics> :MATH]
   . Each:
   [MATH: <semantics><msub><mi>d</mi><mtext>eff</mtext></msub><annotation
   encoding="application/x-tex">d_{\text{eff}}</annotation></semantics> :MATH]
   [MATH: <semantics><mo>+</mo><annotation encoding="application/x-tex">+</annotation></semantics> :MATH]
   Ebbinghaus at
   [MATH: <semantics><mrow><mn>5</mn><mo>,</mo><mn>000</mn></mrow><annotation
   encoding="application/x-tex">5{,}000</annotation></semantics> :MATH]
   competitors. Solution 2: BM25 retrieval; DRM, Ebbinghaus; semantic agreement with cosine NN. Solution 3:
   Gram–Schmidt (
   [MATH: <semantics><mn>500</mn><annotation encoding="application/x-tex">500</annotation></semantics> :MATH]
   vectors), random projection (
   [MATH: <semantics><mrow><mo
   stretchy="false">{</mo><mn>32</mn><mo>,</mo><mn>64</mn><mo>,</mo><mn>128</mn><mo>,</mo><mn>256</mn><mo
   stretchy="false">}</mo></mrow><annotation
   encoding="application/x-tex">\{32,64,128,256\}</annotation></semantics> :MATH]
   dims). Solution 4: MiniBatchKMeans at
   [MATH: <semantics><mrow><mo
   stretchy="false">{</mo><mn>50</mn><mo>,</mo><mn>100</mn><mo>,</mo><mn>250</mn><mo>,</mo><mn>500</mn><mo>,</mo><
   mn>1</mn><mo>,</mo><mn>000</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>500</mn><mo
   stretchy="false">}</mo></mrow><annotation
   encoding="application/x-tex">\{50,100,250,500,1{,}000,2{,}500\}</annotation></semantics> :MATH]
   clusters; Ebbinghaus before/after.

Statistical analysis and reproducibility

   All experiments:
   [MATH: <semantics><mn>5</mn><annotation encoding="application/x-tex">5</annotation></semantics> :MATH]
   seeds
   [MATH: <semantics><mrow><mo
   stretchy="false">[</mo><mn>42</mn><mo>,</mo><mn>123</mn><mo>,</mo><mn>456</mn><mo>,</mo><mn>789</mn><mo>,</mo><
   mn>1024</mn><mo stretchy="false">]</mo></mrow><annotation
   encoding="application/x-tex">[42,123,456,789,1024]</annotation></semantics> :MATH]
   . Bootstrap
   [MATH: <semantics><mrow><mn>95</mn><mo>%</mo></mrow><annotation
   encoding="application/x-tex">95\%</annotation></semantics> :MATH]
   CI from
   [MATH: <semantics><mrow><mn>10</mn><mo>,</mo><mn>000</mn></mrow><annotation
   encoding="application/x-tex">10{,}000</annotation></semantics> :MATH]
   resamples. Cohen’s
   [MATH: <semantics><mi>d</mi><annotation encoding="application/x-tex">d</annotation></semantics> :MATH]
   for spacing. One-sided Wilcoxon for ordering. SPP: paired
   [MATH: <semantics><mi>t</mi><annotation encoding="application/x-tex">t</annotation></semantics> :MATH]
   -test,
   [MATH: <semantics><mrow><mi>p</mi><mo><</mo><mn>0.001</mn></mrow><annotation
   encoding="application/x-tex">p<0.001</annotation></semantics> :MATH]
   . Anderson–Schooler: power-law fit to inter-arrival distribution at cosine threshold
   [MATH: <semantics><mn>0.5</mn><annotation encoding="application/x-tex">0.5</annotation></semantics> :MATH]
   (
   [MATH: <semantics><mrow><mi>α</mi><mo>=</mo><mn>0.459</mn></mrow><annotation
   encoding="application/x-tex">\alpha=0.459</annotation></semantics> :MATH]
   ,
   [MATH: <semantics><mrow><msup><mi>R</mi><mn>2</mn></msup><mo>=</mo><mn>0.952</mn></mrow><annotation
   encoding="application/x-tex">R^{2}=0.952</annotation></semantics> :MATH]
   ). All code, configs, and results in JSON in the reproducibility package. Single NVIDIA A100-SXM4-80GB;
   [MATH: <semantics><mrow><mi></mi><mo>∼</mo><mn>10</mn></mrow><annotation
   encoding="application/x-tex">{\sim}10</annotation></semantics> :MATH]
   GPU-hours total.

Calibration of decay parameter

   The temporal decay parameter
   [MATH: <semantics><mrow><mi>β</mi><mo>=</mo><mn>0.20</mn></mrow><annotation
   encoding="application/x-tex">\beta=0.20</annotation></semantics> :MATH]
   was calibrated via sweep over
   [MATH: <semantics><mrow><mo stretchy="false">[</mo><mn>0.01</mn><mo>,</mo><mn>0.5</mn><mo
   stretchy="false">]</mo></mrow><annotation encoding="application/x-tex">[0.01,0.5]</annotation></semantics>
   :MATH]
   to match HIDE’s
   [MATH: <semantics><mrow><mi>b</mi><mo>=</mo><mn>0.460</mn></mrow><annotation
   encoding="application/x-tex">b=0.460</annotation></semantics> :MATH]
   . This calibration ensures comparability with the predecessor study but means the absolute value of
   [MATH: <semantics><mi>b</mi><annotation encoding="application/x-tex">b</annotation></semantics> :MATH]
   is partially fitted. The qualitative conclusions (that interference produces forgetting and that the exponent
   increases with competitor count) do not depend on the specific value of
   [MATH: <semantics><mi>β</mi><annotation encoding="application/x-tex">\beta</annotation></semantics> :MATH]
   .

Relationship to prior work

   This paper extends HIDE^3 in three ways: (a) the mathematical framework (Theorems 1–4, the corollary,
   proposition, and the No-Escape Theorem) is entirely new (HIDE argued from empirical convergence; this paper
   argues from formal derivation under stated assumptions); (b) four of the five architectures are new (only the
   vector database replicates HIDE’s setup, serving as a calibration condition); (c) the two-level framework
   (geometric vs. behavioural) and the three-category taxonomy are new contributions that resolve the
   architectural objection HIDE left open. The Ebbinghaus baseline comparison (
   [MATH: <semantics><mrow><mi>b</mi><mo>=</mo><mn>0.440</mn></mrow><annotation
   encoding="application/x-tex">b=0.440</annotation></semantics> :MATH]
   vs. HIDE’s
   [MATH: <semantics><mn>0.460</mn><annotation encoding="application/x-tex">0.460</annotation></semantics> :MATH]
   ) uses the same protocol and models as HIDE to enable direct comparison; all other results are independent.

Data Availability

   All datasets publicly available: Wikipedia (wikimedia/wikipedia, CC BY-SA 3.0), DRM word lists (public
   domain^16), PopQA^9 (open).

Code Availability

   Code, configuration files, raw results, and reproduction scripts available at
   https://github.com/Dynamis-Labs/no-escape.

Acknowledgements

   Computational experiments and manuscript preparation were assisted by Claude (Anthropic).

Author Contributions

   A.G. conceived the project, developed the theoretical framework and designed the experiments. A.G, A.S.,
   S.R.B., S.B., and N.N. contributed to implementation, experimental execution and manuscript preparation.

Competing Interests

   The authors have financial interests in Dynamis Labs, Inc.

References

     * S. Amari and H. Nagaoka (2000) Methods of information geometry. American Mathematical Society. Cited by:
       Discussion.
     * J. R. Anderson and L. J. Schooler (1991) Reflections of the environment in memory. Psychological Science 2,
       pp. 396–408. Cited by: Mathematical framework: the no-escape theorem.
     * S. R. Barman, A. Starenky, S. Bodnar, N. Narasimhan, and A. Gopinath (2026) The geometry of forgetting.
       arXiv preprint arXiv:submit/7411865 [cs.AI]. Note: HIDE paper Cited by: Introduction, Models and
       architectures, Relationship to prior work.
     * R. A. Bjork and E. L. Bjork (1992) A new theory of disuse and an old theory of stimulus fluctuation. In
       From Learning Processes to Cognitive Processes: Essays in Honor of William K. Estes, A. F. Healy, S. M.
       Kosslyn, and R. M. Shiffrin (Eds.), pp. 35–67. Cited by: Discussion.
     * R. Brown and D. McNeill (1966) The “tip of the tongue” phenomenon. Journal of Verbal Learning and Verbal
       Behavior 5, pp. 325–337. Cited by: Introduction.
     * N. J. Cepeda, H. Pashler, E. Vul, J. T. Wixted, and D. Rohrer (2006) Distributed practice in verbal recall
       tasks: a review and quantitative synthesis. Psychological Bulletin 132, pp. 354–380. Cited by:
       Introduction.
     * P. Gao, E. Trautmann, B. Yu, G. Santhanam, S. Ryu, K. Shenoy, and S. Ganguli (2017) A theory of
       multineuronal dimensionality, dynamics and measurement. bioRxiv. External Links: Document Cited by:
       Introduction, Figure 5, Figure 5, The dimensionality convergence, Discussion.
     * E. Levina and P. J. Bickel (2005) Maximum likelihood estimation of intrinsic dimension. Advances in Neural
       Information Processing Systems 17. Cited by: The dimensionality convergence, Discussion, Spacing, TOT,
       dimensionality, Theorem 1.
     * A. Mallen, A. Asai, V. Zhong, R. Das, D. Khashabi, and H. Hajishirzi (2023) When not to trust language
       models: investigating effectiveness of parametric and non-parametric memories. arXiv preprint
       arXiv:2212.10511. Cited by: Forgetting experiments, Data Availability.
     * J. L. McClelland, B. L. McNaughton, and R. C. O’Reilly (1995) Why there are complementary learning systems
       in the hippocampus and neocortex. Psychological Review 102, pp. 419–457. Cited by: Discussion, Discussion.
     * B. B. Murdock (1962) The serial position effect of free recall. Journal of Experimental Psychology 64,
       pp. 482–488. Cited by: Introduction.
     * L. Nadel and M. Moscovitch (1997) Memory consolidation, retrograde amnesia and the hippocampal complex.
       Current Opinion in Neurobiology 7, pp. 217–227. Cited by: Introduction.
     * Qwen Team (2024) Qwen2.5: a party of foundation models. arXiv preprint arXiv:2412.15115. Cited by:
       Introduction, Models and architectures.
     * A. Radford, J. W. Kim, C. Hallacy, A. Ramesh, G. Goh, S. Agarwal, G. Sastry, A. Askell, P. Mishkin, J.
       Clark, G. Krueger, and I. Sutskever (2021) Learning transferable visual models from natural language
       supervision. In Proceedings of ICML, Cited by: Introduction.
     * N. Reimers and I. Gurevych (2019) Sentence-BERT: sentence embeddings using Siamese BERT-networks. In
       Proceedings of EMNLP-IJCNLP, pp. 3982–3992. Cited by: Introduction, Models and architectures.
     * H. L. Roediger and K. B. McDermott (1995) Creating false memories: remembering words not presented in
       lists. Journal of Experimental Psychology: Learning, Memory, and Cognition 21, pp. 803–814. Cited by: False
       recall is geometrically inevitable but behaviourally overridable, Discussion, DRM false memory, Data
       Availability.
     * C. E. Shannon (1948) A mathematical theory of communication. Bell System Technical Journal 27, pp. 379–423.
       Cited by: Forgetting experiments.
     * C. E. Shannon (1959) Coding theorems for a discrete source with a fidelity criterion. IRE National
       Convention Record 7, pp. 142–163. Cited by: Discussion.
     * C. Stringer, M. Pachitariu, N. Steinmetz, C. B. Reddy, M. Carandini, and K. D. Harris (2019)
       High-dimensional geometry of population responses in visual cortex. Nature 571, pp. 361–365. Cited by:
       Introduction, Figure 5, Figure 5, The dimensionality convergence, Discussion.
     * J. T. Wixted (1991) On the form of forgetting. Psychological Science 2, pp. 409–415. Cited by: Discussion.
     * S. Xiao, Z. Liu, P. Zhang, and N. Muennighoff (2023) C-pack: packaged resources for general Chinese
       embeddings. arXiv preprint arXiv:2309.07597. Cited by: Introduction, Models and architectures.

Figures

   Refer to caption Figure 1: The No-Escape Theorem: logical structure (paper roadmap). This figure maps the
   paper’s argument. Under the kernel-threshold theorem class (Axioms A1–A5): the semantic kernel and
   rate-distortion optimality yield finite semantic effective rank (Theorem 1); local regularity yields positive
   cap mass (Theorem 2); growing memory yields inevitable forgetting (Theorem 3), with power-law arrival and
   population heterogeneity producing power-law forgetting curves. Independently, associative
   [MATH: <semantics><mi>δ</mi><annotation encoding="application/x-tex">\delta</annotation></semantics> :MATH]
   -convexity yields lure inseparability (Theorem 4). No architecture within this class avoids these consequences
   without abandoning semantic continuity or adding an external symbolic verifier. Each arrow represents a step
   derived under stated assumptions and supported by empirical tests across the architectures studied here. Refer
   to caption Figure 2: Interference produces forgetting across architecturally distinct memory systems. a, Vector
   DB and b, Graph show smooth power-law forgetting curves converging toward the human range (
   [MATH: <semantics><mrow><mi>b</mi><mo>≈</mo><mn>0.3</mn></mrow><annotation
   encoding="application/x-tex">b\approx 0.3</annotation></semantics> :MATH]
   –
   [MATH: <semantics><mn>0.7</mn><annotation encoding="application/x-tex">0.7</annotation></semantics> :MATH]
   , red dashed). c, Attention shows a phase transition (logistic fit:
   [MATH: <semantics><mrow><msub><mi>n</mi><mn>0</mn></msub><mo>≈</mo><mn>120</mn></mrow><annotation
   encoding="application/x-tex">n_{0}\approx 120</annotation></semantics> :MATH]
   ,
   [MATH: <semantics><mrow><mi>k</mi><mo>≈</mo><mn>0.03</mn></mrow><annotation
   encoding="application/x-tex">k\approx 0.03</annotation></semantics> :MATH]
   ; power-law fitting is inappropriate for this sigmoid failure mode). d, Filesystem (BM25) shows
   [MATH: <semantics><mrow><mi>b</mi><mo>=</mo><mn>0</mn></mrow><annotation
   encoding="application/x-tex">b=0</annotation></semantics> :MATH]
   (no semantic interference). e, Parametric (PopQA) shows monotonic accuracy decline with neighbour density.
   Category 1 systems degrade continuously; Category 2 systems fail discontinuously.
   [MATH: <semantics><mrow><mi>n</mi><mo>=</mo><mn>5</mn></mrow><annotation
   encoding="application/x-tex">n=5</annotation></semantics> :MATH]
   seeds throughout. Refer to caption Figure 3: The forgetting exponent depends on competitor count, not
   architecture. Forgetting exponent
   [MATH: <semantics><mi>b</mi><annotation encoding="application/x-tex">b</annotation></semantics> :MATH]
   vs. number of near competitors for embedding architectures (Vector DB, Graph) with human reference (
   [MATH: <semantics><mrow><mi>b</mi><mo>≈</mo><mn>0.5</mn></mrow><annotation
   encoding="application/x-tex">b\approx 0.5</annotation></semantics> :MATH]
   , dashed). Both converge toward the human range at high competitor counts. Shaded: bootstrap
   [MATH: <semantics><mrow><mn>95</mn><mo>%</mo></mrow><annotation
   encoding="application/x-tex">95\%</annotation></semantics> :MATH]
   CI,
   [MATH: <semantics><mrow><mi>n</mi><mo>=</mo><mn>5</mn></mrow><annotation
   encoding="application/x-tex">n=5</annotation></semantics> :MATH]
   seeds. Refer to caption Figure 4: False recall is geometrically inevitable. a, Hit rate, lure false alarm rate,
   and unrelated FA for all five architectures and human data. Embedding architectures show elevated lure FA; LLM
   architectures show FA
   [MATH: <semantics><mrow><mi></mi><mo>=</mo><mn>0</mn></mrow><annotation
   encoding="application/x-tex">=0</annotation></semantics> :MATH]
   at behavioural level (explicit list-checking). b, Lure FA rates compared directly. The geometric prediction (
   [MATH: <semantics><mrow><mn>24</mn><mo>/</mo><mn>24</mn></mrow><annotation
   encoding="application/x-tex">24/24</annotation></semantics> :MATH]
   lures within spherical caps) holds for all architectures regardless of behavioural output.
   [MATH: <semantics><mrow><mi>n</mi><mo>=</mo><mn>5</mn></mrow><annotation
   encoding="application/x-tex">n=5</annotation></semantics> :MATH]
   seeds,
   [MATH: <semantics><mn>24</mn><annotation encoding="application/x-tex">24</annotation></semantics> :MATH]
   DRM lists. Refer to caption Figure 5: Effective dimensionality converges far below nominal regardless of
   architecture.
   [MATH: <semantics><msub><mi>d</mi><mtext>eff</mtext></msub><annotation
   encoding="application/x-tex">d_{\text{eff}}</annotation></semantics> :MATH]
   (participation ratio) vs.
   [MATH: <semantics><msub><mi>d</mi><mtext>nom</mtext></msub><annotation
   encoding="application/x-tex">d_{\text{nom}}</annotation></semantics> :MATH]
   for all five architectures. Grey: biological range (
   [MATH: <semantics><mrow><msub><mi>d</mi><mtext>eff</mtext></msub><mo>=</mo><mn>100</mn></mrow><annotation
   encoding="application/x-tex">d_{\text{eff}}=100</annotation></semantics> :MATH]
   –
   [MATH: <semantics><mn>500</mn><annotation encoding="application/x-tex">500</annotation></semantics> :MATH]
   ^19, 7). Qwen hidden states (
   [MATH:
   <semantics><mrow><msub><mi>d</mi><mtext>nom</mtext></msub><mo>=</mo><mrow><mn>3</mn><mo>,</mo><mn>584</mn></mro
   w></mrow><annotation encoding="application/x-tex">d_{\text{nom}}=3{,}584</annotation></semantics> :MATH]
   ) compress to
   [MATH: <semantics><mrow><msub><mi>d</mi><mtext>eff</mtext></msub><mo>=</mo><mn>17.9</mn></mrow><annotation
   encoding="application/x-tex">d_{\text{eff}}=17.9</annotation></semantics> :MATH]
   , a
   [MATH: <semantics><mrow><mn>200</mn><mo lspace="0.222em">×</mo></mrow><annotation
   encoding="application/x-tex">200\times</annotation></semantics> :MATH]
   reduction. All architectures cluster below the interference threshold. Refer to caption Figure 6: No proposed
   solution achieves both immunity and usefulness. Every solution that reduces interference moves along a tradeoff
   frontier toward reduced usefulness; no solution escapes the frontier itself. This is the empirical corollary to
   Theorem 1. a, Zero-padding does not reduce
   [MATH: <semantics><mi>b</mi><annotation encoding="application/x-tex">b</annotation></semantics> :MATH]
   (
   [MATH: <semantics><msub><mi>d</mi><mtext>eff</mtext></msub><annotation
   encoding="application/x-tex">d_{\text{eff}}</annotation></semantics> :MATH]
   unchanged). b, BM25 eliminates false recall but semantic agreement drops to
   [MATH: <semantics><mrow><mn>15.5</mn><mo>%</mo></mrow><annotation
   encoding="application/x-tex">15.5\%</annotation></semantics> :MATH]
   . c, Gram–Schmidt eliminates interference; semantic accuracy
   [MATH: <semantics><mrow><mi></mi><mo>=</mo><mrow><mn>0</mn><mo>%</mo></mrow></mrow><annotation
   encoding="application/x-tex">=0\%</annotation></semantics> :MATH]
   . d, Compression reduces
   [MATH: <semantics><mi>b</mi><annotation encoding="application/x-tex">b</annotation></semantics> :MATH]
   but degrades retrieval. Refer to caption Figure 7: Architecture comparison across four memory phenomena.
   Heatmap of forgetting exponent
   [MATH: <semantics><mi>b</mi><annotation encoding="application/x-tex">b</annotation></semantics> :MATH]
   , DRM lure FA, spacing Cohen’s
   [MATH: <semantics><mi>d</mi><annotation encoding="application/x-tex">d</annotation></semantics> :MATH]
   , and TOT rate for all five architectures and human reference. The three prototypical behavioural categories
   are visible: pure geometric (top two rows), reasoning overlay (middle), SPP-violating (bottom). Dashes indicate
   metrics not measurable for that architecture (attention
   [MATH: <semantics><mi>b</mi><annotation encoding="application/x-tex">b</annotation></semantics> :MATH]
   : sigmoid, not power-law; parametric spacing: no controlled paradigm). ^†Parametric TOT (
   [MATH: <semantics><mrow><mn>69</mn><mo>%</mo></mrow><annotation
   encoding="application/x-tex">69\%</annotation></semantics> :MATH]
   ) uses a different operational definition than human/embedding TOT and is not directly comparable (see
   Discussion). Metrics are architecture-specific and not all directly numerically comparable (see Methods for
   protocol differences).

Supplementary Information

   Table 1: Hyperparameters for all architectures and experiments.
                                    Parameter                          Value Description
   Seeds
   [MATH: <semantics><mrow><mo maxsize="0.900em" minsize="0.900em">[</mo><mn mathsize="0.900em">42</mn><mo
   mathsize="0.900em">,</mo><mn mathsize="0.900em">123</mn><mo mathsize="0.900em">,</mo><mn
   mathsize="0.900em">456</mn><mo mathsize="0.900em">,</mo><mn mathsize="0.900em">789</mn><mo
   mathsize="0.900em">,</mo><mn mathsize="0.900em">1024</mn><mo maxsize="0.900em"
   minsize="0.900em">]</mo></mrow><annotation
   encoding="application/x-tex">[42,123,456,789,1024]</annotation></semantics> :MATH]
          Random seeds
   Bootstrap
   [MATH: <semantics><mrow><mn mathsize="0.900em">10</mn><mo mathsize="0.900em">,</mo><mn
   mathsize="0.900em">000</mn></mrow><annotation encoding="application/x-tex">10{,}000</annotation></semantics>
   :MATH]
   Resamples for
   [MATH: <semantics><mrow><mn mathsize="0.900em">95</mn><mo mathsize="0.900em">%</mo></mrow><annotation
   encoding="application/x-tex">95\%</annotation></semantics> :MATH]
   CI
   Decay
   [MATH: <semantics><mi mathsize="0.900em">β</mi><annotation
   encoding="application/x-tex">\beta</annotation></semantics> :MATH]
   [MATH: <semantics><mn mathsize="0.900em">0.20</mn><annotation
   encoding="application/x-tex">0.20</annotation></semantics> :MATH]
          Temporal decay rate (calibrated)
   Decay
   [MATH: <semantics><mi mathsize="0.900em">ψ</mi><annotation
   encoding="application/x-tex">\psi</annotation></semantics> :MATH]
   [MATH: <semantics><mn mathsize="0.900em">0.50</mn><annotation
   encoding="application/x-tex">0.50</annotation></semantics> :MATH]
          Temporal decay exponent
   Noise
   [MATH: <semantics><mi mathsize="0.900em">σ</mi><annotation
   encoding="application/x-tex">\sigma</annotation></semantics> :MATH]
   (Ebb.)
   [MATH: <semantics><mn mathsize="0.900em">0.50</mn><annotation
   encoding="application/x-tex">0.50</annotation></semantics> :MATH]
          Ebbinghaus query noise
   Noise
   [MATH: <semantics><mi mathsize="0.900em">σ</mi><annotation
   encoding="application/x-tex">\sigma</annotation></semantics> :MATH]
   (Sp.)
   [MATH: <semantics><mn mathsize="0.900em">0.25</mn><annotation
   encoding="application/x-tex">0.25</annotation></semantics> :MATH]
          Spacing noise
          TOT PCA dim
   [MATH: <semantics><mn mathsize="0.900em">96</mn><annotation
   encoding="application/x-tex">96</annotation></semantics> :MATH]
          PCA reduction for TOT
   TOT noise
   [MATH: <semantics><mrow><mn mathsize="0.900em">1.5</mn><mo maxsize="0.900em" minsize="0.900em" stretchy="true"
   symmetric="true">/</mo><msqrt><mn mathsize="0.900em">96</mn></msqrt></mrow><annotation
   encoding="application/x-tex">1.5/\sqrt{96}</annotation></semantics> :MATH]
          Query noise for TOT
   PageRank
   [MATH: <semantics><mi mathsize="0.900em">α</mi><annotation
   encoding="application/x-tex">\alpha</annotation></semantics> :MATH]
   [MATH: <semantics><mn mathsize="0.900em">0.85</mn><annotation
   encoding="application/x-tex">0.85</annotation></semantics> :MATH]
          Damping factor
          Edge threshold
   [MATH: <semantics><mn mathsize="0.900em">0.70</mn><annotation
   encoding="application/x-tex">0.70</annotation></semantics> :MATH]
          Graph cosine cutoff
   BM25 top-
   [MATH: <semantics><mi mathsize="0.900em">k</mi><annotation
   encoding="application/x-tex">k</annotation></semantics> :MATH]
   [MATH: <semantics><mn mathsize="0.900em">50</mn><annotation
   encoding="application/x-tex">50</annotation></semantics> :MATH]
          Filesystem candidates
          PopQA threshold
   [MATH: <semantics><mn mathsize="0.900em">0.40</mn><annotation
   encoding="application/x-tex">0.40</annotation></semantics> :MATH]
          Cosine threshold for neighbours
   Table 2: Dataset details.
   Dataset Source Size Licence Use
   Wikipedia wikimedia/wikipedia
   [MATH: <semantics><mrow><mn mathsize="0.900em">20</mn><mo mathsize="0.900em">,</mo><mn
   mathsize="0.900em">000</mn></mrow><annotation encoding="application/x-tex">20{,}000</annotation></semantics>
   :MATH]
   sent. CC BY-SA 3.0 All experiments
   DRM lists Roediger & McDermott
   [MATH: <semantics><mn mathsize="0.900em">24</mn><annotation
   encoding="application/x-tex">24</annotation></semantics> :MATH]
   lists Public domain False memory
   PopQA akariasai/PopQA
   [MATH: <semantics><mrow><mn mathsize="0.900em">14</mn><mo mathsize="0.900em">,</mo><mn
   mathsize="0.900em">267</mn></mrow><annotation encoding="application/x-tex">14{,}267</annotation></semantics>
   :MATH]
   Q&A Open Parametric interf.
   Table 3: Per-architecture results summary (
   [MATH: <semantics><mrow><mi>n</mi><mo>=</mo><mn>5</mn></mrow><annotation
   encoding="application/x-tex">n=5</annotation></semantics> :MATH]
   seeds unless noted).
   Ebb.
   [MATH: <semantics><mi>b</mi><annotation encoding="application/x-tex">b</annotation></semantics> :MATH]
   DRM FA Spacing L/M TOT
   [MATH: <semantics><msub><mi mathsize="0.900em">d</mi><mtext class="ltx_mathvariant_bold"
   mathsize="0.900em">eff</mtext></msub><annotation
   encoding="application/x-tex">d_{\text{eff}}</annotation></semantics> :MATH]
   Vector DB
   [MATH: <semantics><mrow><mn mathsize="0.900em">0.440</mn><mo mathsize="0.900em">±</mo><mn
   mathsize="0.900em">0.030</mn></mrow><annotation encoding="application/x-tex">0.440\pm
   0.030</annotation></semantics> :MATH]
   [MATH: <semantics><mn mathsize="0.900em">0.583</mn><annotation
   encoding="application/x-tex">0.583</annotation></semantics> :MATH]
   [MATH: <semantics><mrow><mn mathsize="0.900em">0.90</mn><mo maxsize="0.900em" minsize="0.900em" stretchy="true"
   symmetric="true">/</mo><mn mathsize="0.900em">0.36</mn></mrow><annotation
   encoding="application/x-tex">0.90/0.36</annotation></semantics> :MATH]
   [MATH: <semantics><mn mathsize="0.900em">0.020</mn><annotation
   encoding="application/x-tex">0.020</annotation></semantics> :MATH]
   [MATH: <semantics><mn mathsize="0.900em">158</mn><annotation
   encoding="application/x-tex">158</annotation></semantics> :MATH]
   Graph
   [MATH: <semantics><mrow><mn mathsize="0.900em">0.478</mn><mo mathsize="0.900em">±</mo><mn
   mathsize="0.900em">0.028</mn></mrow><annotation encoding="application/x-tex">0.478\pm
   0.028</annotation></semantics> :MATH]
   [MATH: <semantics><mn mathsize="0.900em">0.208</mn><annotation
   encoding="application/x-tex">0.208</annotation></semantics> :MATH]
   [MATH: <semantics><mrow><mn mathsize="0.900em">1.00</mn><mo maxsize="0.900em" minsize="0.900em" stretchy="true"
   symmetric="true">/</mo><mn mathsize="0.900em">0.92</mn></mrow><annotation
   encoding="application/x-tex">1.00/0.92</annotation></semantics> :MATH]
   [MATH: <semantics><mn mathsize="0.900em">0.028</mn><annotation
   encoding="application/x-tex">0.028</annotation></semantics> :MATH]
   [MATH: <semantics><mn mathsize="0.900em">127</mn><annotation
   encoding="application/x-tex">127</annotation></semantics> :MATH]
   Attention phase trans.
   [MATH: <semantics><msup><mn mathsize="0.900em">0.000</mn><mo mathsize="0.900em">†</mo></msup><annotation
   encoding="application/x-tex">0.000^{\dagger}</annotation></semantics> :MATH]
   [MATH: <semantics><mrow><mn mathsize="0.900em">0.00</mn><mo maxsize="0.900em" minsize="0.900em" stretchy="true"
   symmetric="true">/</mo><mn mathsize="0.900em">1.00</mn></mrow><annotation
   encoding="application/x-tex">0.00/1.00</annotation></semantics> :MATH]
   [MATH: <semantics><mn mathsize="0.900em">0.210</mn><annotation
   encoding="application/x-tex">0.210</annotation></semantics> :MATH]
   [MATH: <semantics><mn mathsize="0.900em">17.9</mn><annotation
   encoding="application/x-tex">17.9</annotation></semantics> :MATH]
   Parametric
   [MATH: <semantics><msup><mn mathsize="0.900em">0.215</mn><mo mathsize="0.900em">∗</mo></msup><annotation
   encoding="application/x-tex">0.215^{*}</annotation></semantics> :MATH]
   [MATH: <semantics><msup><mn mathsize="0.900em">0.000</mn><mo mathsize="0.900em">†</mo></msup><annotation
   encoding="application/x-tex">0.000^{\dagger}</annotation></semantics> :MATH]
   —
   [MATH: <semantics><mn mathsize="0.900em">0.690</mn><annotation
   encoding="application/x-tex">0.690</annotation></semantics> :MATH]
   [MATH: <semantics><mn mathsize="0.900em">17.9</mn><annotation
   encoding="application/x-tex">17.9</annotation></semantics> :MATH]
   Filesystem
   [MATH: <semantics><mn mathsize="0.900em">0.000</mn><annotation
   encoding="application/x-tex">0.000</annotation></semantics> :MATH]
   [MATH: <semantics><mn mathsize="0.900em">0.000</mn><annotation
   encoding="application/x-tex">0.000</annotation></semantics> :MATH]
   [MATH: <semantics><mrow><mn mathsize="0.900em">1.00</mn><mo maxsize="0.900em" minsize="0.900em" stretchy="true"
   symmetric="true">/</mo><mn mathsize="0.900em">1.00</mn></mrow><annotation
   encoding="application/x-tex">1.00/1.00</annotation></semantics> :MATH]
   [MATH: <semantics><mn mathsize="0.900em">0.010</mn><annotation
   encoding="application/x-tex">0.010</annotation></semantics> :MATH]
   [MATH: <semantics><mn mathsize="0.900em">158</mn><annotation
   encoding="application/x-tex">158</annotation></semantics> :MATH]
   Human
   [MATH: <semantics><mrow><mi></mi><mo mathsize="0.900em">∼</mo><mn mathsize="0.900em">0.5</mn></mrow><annotation
   encoding="application/x-tex">{\sim}0.5</annotation></semantics> :MATH]
   [MATH: <semantics><mrow><mi></mi><mo mathsize="0.900em">∼</mo><mn
   mathsize="0.900em">0.55</mn></mrow><annotation encoding="application/x-tex">{\sim}0.55</annotation></semantics>
   :MATH]
   L
   [MATH: <semantics><mo mathsize="0.900em">></mo><annotation
   encoding="application/x-tex">></annotation></semantics> :MATH]
   M
   [MATH: <semantics><mrow><mi></mi><mo mathsize="0.900em">∼</mo><mn
   mathsize="0.900em">0.037</mn></mrow><annotation
   encoding="application/x-tex">{\sim}0.037</annotation></semantics> :MATH]
   [MATH: <semantics><mn mathsize="0.900em">100</mn><annotation
   encoding="application/x-tex">100</annotation></semantics> :MATH]
   –
   [MATH: <semantics><mn mathsize="0.900em">500</mn><annotation
   encoding="application/x-tex">500</annotation></semantics> :MATH]
   ^∗PopQA interference
   [MATH: <semantics><mi>b</mi><annotation encoding="application/x-tex">b</annotation></semantics> :MATH]
   (binned neighbour density), not controlled Ebbinghaus paradigm; not directly
   comparable to embedding-architecture
   [MATH: <semantics><mi>b</mi><annotation encoding="application/x-tex">b</annotation></semantics> :MATH]
   values. ^†Behavioural; geometric prediction holds (
   [MATH: <semantics><mrow><mn>24</mn><mo>/</mo><mn>24</mn></mrow><annotation
   encoding="application/x-tex">24/24</annotation></semantics> :MATH]
   caps).
   Table 4: Effective dimensionality per architecture.
   Architecture
   [MATH: <semantics><msub><mi mathsize="0.900em">d</mi><mtext mathsize="0.900em">nom</mtext></msub><annotation
   encoding="application/x-tex">d_{\text{nom}}</annotation></semantics> :MATH]
   [MATH: <semantics><msub><mi mathsize="0.900em">d</mi><mtext mathsize="0.900em">eff</mtext></msub><annotation
   encoding="application/x-tex">d_{\text{eff}}</annotation></semantics> :MATH]
   (PR)
   [MATH: <semantics><msub><mi mathsize="0.900em">d</mi><mtext mathsize="0.900em">eff</mtext></msub><annotation
   encoding="application/x-tex">d_{\text{eff}}</annotation></semantics> :MATH]
   (LB)
   [MATH: <semantics><msub><mi mathsize="0.900em">d</mi><mn mathsize="0.900em">95</mn></msub><annotation
   encoding="application/x-tex">d_{95}</annotation></semantics> :MATH]
   [MATH: <semantics><msub><mi mathsize="0.900em">d</mi><mn mathsize="0.900em">99</mn></msub><annotation
   encoding="application/x-tex">d_{99}</annotation></semantics> :MATH]
   Vector DB (BGE-large)
   [MATH: <semantics><mrow><mn mathsize="0.900em">1</mn><mo mathsize="0.900em">,</mo><mn
   mathsize="0.900em">024</mn></mrow><annotation encoding="application/x-tex">1{,}024</annotation></semantics>
   :MATH]
   [MATH: <semantics><mn mathsize="0.900em">158</mn><annotation
   encoding="application/x-tex">158</annotation></semantics> :MATH]
   [MATH: <semantics><mn mathsize="0.900em">10.6</mn><annotation
   encoding="application/x-tex">10.6</annotation></semantics> :MATH]
   [MATH: <semantics><mn mathsize="0.900em">404</mn><annotation
   encoding="application/x-tex">404</annotation></semantics> :MATH]
   [MATH: <semantics><mn mathsize="0.900em">642</mn><annotation
   encoding="application/x-tex">642</annotation></semantics> :MATH]
   Graph (MiniLM)
   [MATH: <semantics><mn mathsize="0.900em">384</mn><annotation
   encoding="application/x-tex">384</annotation></semantics> :MATH]
   [MATH: <semantics><mn mathsize="0.900em">127</mn><annotation
   encoding="application/x-tex">127</annotation></semantics> :MATH]
   —
   [MATH: <semantics><mn mathsize="0.900em">237</mn><annotation
   encoding="application/x-tex">237</annotation></semantics> :MATH]
   [MATH: <semantics><mn mathsize="0.900em">309</mn><annotation
   encoding="application/x-tex">309</annotation></semantics> :MATH]
   Attention (Qwen)
   [MATH: <semantics><mrow><mn mathsize="0.900em">3</mn><mo mathsize="0.900em">,</mo><mn
   mathsize="0.900em">584</mn></mrow><annotation encoding="application/x-tex">3{,}584</annotation></semantics>
   :MATH]
   [MATH: <semantics><mn mathsize="0.900em">17.9</mn><annotation
   encoding="application/x-tex">17.9</annotation></semantics> :MATH]
   — — —
   Parametric (Qwen)
   [MATH: <semantics><mrow><mn mathsize="0.900em">3</mn><mo mathsize="0.900em">,</mo><mn
   mathsize="0.900em">584</mn></mrow><annotation encoding="application/x-tex">3{,}584</annotation></semantics>
   :MATH]
   [MATH: <semantics><mn mathsize="0.900em">17.9</mn><annotation
   encoding="application/x-tex">17.9</annotation></semantics> :MATH]
   — — —
   Filesystem (BGE-large)
   [MATH: <semantics><mrow><mn mathsize="0.900em">1</mn><mo mathsize="0.900em">,</mo><mn
   mathsize="0.900em">024</mn></mrow><annotation encoding="application/x-tex">1{,}024</annotation></semantics>
   :MATH]
   [MATH: <semantics><mn mathsize="0.900em">158</mn><annotation
   encoding="application/x-tex">158</annotation></semantics> :MATH]
   [MATH: <semantics><mn mathsize="0.900em">10.6</mn><annotation
   encoding="application/x-tex">10.6</annotation></semantics> :MATH]
   [MATH: <semantics><mn mathsize="0.900em">404</mn><annotation
   encoding="application/x-tex">404</annotation></semantics> :MATH]
   [MATH: <semantics><mn mathsize="0.900em">642</mn><annotation
   encoding="application/x-tex">642</annotation></semantics> :MATH]
   Table 5: Solution analysis data points.
   Solution Configuration
   [MATH: <semantics><mi mathsize="0.900em">b</mi><annotation
   encoding="application/x-tex">b</annotation></semantics> :MATH]
   Accuracy
   1: High dim PCA
   [MATH: <semantics><mrow><mi mathsize="0.900em">d</mi><mo mathsize="0.900em">=</mo><mn
   mathsize="0.900em">64</mn></mrow><annotation encoding="application/x-tex">d=64</annotation></semantics> :MATH]
   [MATH: <semantics><mn mathsize="0.900em">0.370</mn><annotation
   encoding="application/x-tex">0.370</annotation></semantics> :MATH]
   reduced
   Original
   [MATH: <semantics><mrow><mi mathsize="0.900em">d</mi><mo mathsize="0.900em">=</mo><mrow><mn
   mathsize="0.900em">1</mn><mo mathsize="0.900em">,</mo><mn mathsize="0.900em">024</mn></mrow></mrow><annotation
   encoding="application/x-tex">d=1{,}024</annotation></semantics> :MATH]
   [MATH: <semantics><mn mathsize="0.900em">0.831</mn><annotation
   encoding="application/x-tex">0.831</annotation></semantics> :MATH]
   baseline
   Zero-pad
   [MATH: <semantics><mrow><mi mathsize="0.900em">d</mi><mo mathsize="0.900em">=</mo><mrow><mn
   mathsize="0.900em">2</mn><mo mathsize="0.900em">,</mo><mn mathsize="0.900em">048</mn></mrow></mrow><annotation
   encoding="application/x-tex">d=2{,}048</annotation></semantics> :MATH]
   [MATH: <semantics><mn mathsize="0.900em">0.332</mn><annotation
   encoding="application/x-tex">0.332</annotation></semantics> :MATH]
   baseline
   Zero-pad
   [MATH: <semantics><mrow><mi mathsize="0.900em">d</mi><mo mathsize="0.900em">=</mo><mrow><mn
   mathsize="0.900em">4</mn><mo mathsize="0.900em">,</mo><mn mathsize="0.900em">096</mn></mrow></mrow><annotation
   encoding="application/x-tex">d=4{,}096</annotation></semantics> :MATH]
   [MATH: <semantics><mn mathsize="0.900em">0.308</mn><annotation
   encoding="application/x-tex">0.308</annotation></semantics> :MATH]
   baseline
   2: BM25 Full BM25
   [MATH: <semantics><mn mathsize="0.900em">0.000</mn><annotation
   encoding="application/x-tex">0.000</annotation></semantics> :MATH]
   [MATH: <semantics><mrow><mn mathsize="0.900em">15.5</mn><mo mathsize="0.900em">%</mo></mrow><annotation
   encoding="application/x-tex">15.5\%</annotation></semantics> :MATH]
   3: Gram–Schmidt
   [MATH: <semantics><mn mathsize="0.900em">500</mn><annotation
   encoding="application/x-tex">500</annotation></semantics> :MATH]
   vectors
   [MATH: <semantics><mn mathsize="0.900em">0.000</mn><annotation
   encoding="application/x-tex">0.000</annotation></semantics> :MATH]
   [MATH: <semantics><mrow><mn mathsize="0.900em">0.0</mn><mo mathsize="0.900em">%</mo></mrow><annotation
   encoding="application/x-tex">0.0\%</annotation></semantics> :MATH]
   4: Compression
   [MATH: <semantics><mrow><mi mathsize="0.900em">k</mi><mo mathsize="0.900em">=</mo><mn
   mathsize="0.900em">50</mn></mrow><annotation encoding="application/x-tex">k=50</annotation></semantics> :MATH]
   [MATH: <semantics><mn mathsize="0.900em">0.432</mn><annotation
   encoding="application/x-tex">0.432</annotation></semantics> :MATH]
   [MATH: <semantics><mrow><mn mathsize="0.900em">98.8</mn><mo mathsize="0.900em">%</mo></mrow><annotation
   encoding="application/x-tex">98.8\%</annotation></semantics> :MATH]
   [MATH: <semantics><mrow><mi mathsize="0.900em">k</mi><mo mathsize="0.900em">=</mo><mn
   mathsize="0.900em">500</mn></mrow><annotation encoding="application/x-tex">k=500</annotation></semantics>
   :MATH]
   [MATH: <semantics><mn mathsize="0.900em">0.254</mn><annotation
   encoding="application/x-tex">0.254</annotation></semantics> :MATH]
   [MATH: <semantics><mrow><mn mathsize="0.900em">95.6</mn><mo mathsize="0.900em">%</mo></mrow><annotation
   encoding="application/x-tex">95.6\%</annotation></semantics> :MATH]
   [MATH: <semantics><mrow><mi mathsize="0.900em">k</mi><mo mathsize="0.900em">=</mo><mrow><mn
   mathsize="0.900em">2</mn><mo mathsize="0.900em">,</mo><mn mathsize="0.900em">500</mn></mrow></mrow><annotation
   encoding="application/x-tex">k=2{,}500</annotation></semantics> :MATH]
   [MATH: <semantics><mn mathsize="0.900em">0.163</mn><annotation
   encoding="application/x-tex">0.163</annotation></semantics> :MATH]
   [MATH: <semantics><mrow><mn mathsize="0.900em">92.8</mn><mo mathsize="0.900em">%</mo></mrow><annotation
   encoding="application/x-tex">92.8\%</annotation></semantics> :MATH]

Extended Data

   Refer to caption Figure 8: Extended Data Fig. 1: The five memory architectures. Each architecture implements a
   fundamentally different storage and retrieval mechanism: cosine similarity (Vector DB), attention over context
   (Attention), BM25
   [MATH: <semantics><mo>+</mo><annotation encoding="application/x-tex">+</annotation></semantics> :MATH]
   LLM re-ranking (Filesystem), personalised PageRank (Graph), and parametric knowledge in weights (Parametric).
   Despite architectural diversity, all except Filesystem strongly satisfy SPP (
   [MATH: <semantics><mrow><mi>p</mi><mo><</mo><mn>0.001</mn></mrow><annotation
   encoding="application/x-tex">p<0.001</annotation></semantics> :MATH]
   ).
   [MATH: <semantics><mrow><mi>n</mi><mo>=</mo><mn>143</mn></mrow><annotation
   encoding="application/x-tex">n=143</annotation></semantics> :MATH]
   sentence pairs per architecture. Refer to caption Figure 9: Extended Data Fig. 2: Vector Database full results.
   a, Forgetting exponent
   [MATH: <semantics><mi>b</mi><annotation encoding="application/x-tex">b</annotation></semantics> :MATH]
   at each competitor count, showing monotonic increase. b, DRM hit rate, lure FA, and unrelated FA. c, Spacing
   retention: long
   [MATH: <semantics><mrow><mi></mi><mo>=</mo><mn>0.902</mn></mrow><annotation
   encoding="application/x-tex">=0.902</annotation></semantics> :MATH]
   , massed
   [MATH: <semantics><mrow><mi></mi><mo>=</mo><mn>0.360</mn></mrow><annotation
   encoding="application/x-tex">=0.360</annotation></semantics> :MATH]
   . d, Eigenvalue spectrum (
   [MATH: <semantics><mrow><msub><mi>d</mi><mtext>eff</mtext></msub><mo>=</mo><mn>158</mn></mrow><annotation
   encoding="application/x-tex">d_{\text{eff}}=158</annotation></semantics> :MATH]
   ). Error bars: bootstrap
   [MATH: <semantics><mrow><mn>95</mn><mo>%</mo></mrow><annotation
   encoding="application/x-tex">95\%</annotation></semantics> :MATH]
   CI,
   [MATH: <semantics><mrow><mi>n</mi><mo>=</mo><mn>5</mn></mrow><annotation
   encoding="application/x-tex">n=5</annotation></semantics> :MATH]
   seeds. Refer to caption Figure 10: Extended Data Fig. 3: Graph Memory full results. a,
   [MATH: <semantics><mrow><mi>b</mi><mo>=</mo><mn>0.478</mn></mrow><annotation
   encoding="application/x-tex">b=0.478</annotation></semantics> :MATH]
   at
   [MATH: <semantics><mrow><mn>10</mn><mo>,</mo><mn>000</mn></mrow><annotation
   encoding="application/x-tex">10{,}000</annotation></semantics> :MATH]
   competitors. b, DRM lure FA
   [MATH: <semantics><mrow><mi></mi><mo>=</mo><mn>0.208</mn></mrow><annotation
   encoding="application/x-tex">=0.208</annotation></semantics> :MATH]
   at
   [MATH: <semantics><mrow><mi>θ</mi><mo>=</mo><mn>0.82</mn></mrow><annotation
   encoding="application/x-tex">\theta=0.82</annotation></semantics> :MATH]
   . c, Spacing: long
   [MATH: <semantics><mrow><mi></mi><mo>=</mo><mn>0.996</mn></mrow><annotation
   encoding="application/x-tex">=0.996</annotation></semantics> :MATH]
   , massed
   [MATH: <semantics><mrow><mi></mi><mo>=</mo><mn>0.920</mn></mrow><annotation
   encoding="application/x-tex">=0.920</annotation></semantics> :MATH]
   . d, Eigenvalue spectrum (
   [MATH: <semantics><mrow><msub><mi>d</mi><mtext>eff</mtext></msub><mo>=</mo><mn>127</mn></mrow><annotation
   encoding="application/x-tex">d_{\text{eff}}=127</annotation></semantics> :MATH]
   ).
   [MATH: <semantics><mrow><mi>n</mi><mo>=</mo><mn>5</mn></mrow><annotation
   encoding="application/x-tex">n=5</annotation></semantics> :MATH]
   seeds. Refer to caption Figure 11: Extended Data Fig. 4: Attention Memory full results. a, Phase transition:
   near-perfect accuracy at
   [MATH: <semantics><mrow><msub><mi>n</mi><mtext>near</mtext></msub><mo><</mo><mn>100</mn></mrow><annotation
   encoding="application/x-tex">n_{\text{near}}<100</annotation></semantics> :MATH]
   , then catastrophic collapse (logistic fit:
   [MATH: <semantics><mrow><msub><mi>n</mi><mn>0</mn></msub><mo>≈</mo><mn>120</mn></mrow><annotation
   encoding="application/x-tex">n_{0}\approx 120</annotation></semantics> :MATH]
   ,
   [MATH: <semantics><mrow><mi>k</mi><mo>≈</mo><mn>0.03</mn></mrow><annotation
   encoding="application/x-tex">k\approx 0.03</annotation></semantics> :MATH]
   ; power-law fitting is inappropriate for this sigmoid failure mode;
   [MATH: <semantics><mi>y</mi><annotation encoding="application/x-tex">y</annotation></semantics> :MATH]
   -axis values reflect interference severity, not power-law exponents). b, DRM FA
   [MATH: <semantics><mrow><mi></mi><mo>=</mo><mn>0</mn></mrow><annotation
   encoding="application/x-tex">=0</annotation></semantics> :MATH]
   at behavioural level (geometric prediction holds:
   [MATH: <semantics><mrow><mn>24</mn><mo>/</mo><mn>24</mn></mrow><annotation
   encoding="application/x-tex">24/24</annotation></semantics> :MATH]
   lures within caps). c, Spacing: architectural capacity artefact: massed
   [MATH: <semantics><mrow><mi></mi><mo>=</mo><mn>1.0</mn></mrow><annotation
   encoding="application/x-tex">=1.0</annotation></semantics> :MATH]
   , spaced
   [MATH: <semantics><mrow><mi></mi><mo>=</mo><mn>0.0</mn></mrow><annotation
   encoding="application/x-tex">=0.0</annotation></semantics> :MATH]
   (context-window limit relocates interference to capacity domain). d,
   [MATH: <semantics><mrow><msub><mi>d</mi><mtext>eff</mtext></msub><mo>=</mo><mn>17.9</mn></mrow><annotation
   encoding="application/x-tex">d_{\text{eff}}=17.9</annotation></semantics> :MATH]
   from
   [MATH:
   <semantics><mrow><msub><mi>d</mi><mtext>nom</mtext></msub><mo>=</mo><mrow><mn>3</mn><mo>,</mo><mn>584</mn></mro
   w></mrow><annotation encoding="application/x-tex">d_{\text{nom}}=3{,}584</annotation></semantics> :MATH]
   , a
   [MATH: <semantics><mrow><mn>200</mn><mo lspace="0.222em">×</mo></mrow><annotation
   encoding="application/x-tex">200\times</annotation></semantics> :MATH]
   compression.
   [MATH: <semantics><mrow><mi>n</mi><mo>=</mo><mn>5</mn></mrow><annotation
   encoding="application/x-tex">n=5</annotation></semantics> :MATH]
   seeds. Refer to caption Figure 12: Extended Data Fig. 5: Parametric Memory full results. PopQA interference:
   accuracy drops from
   [MATH: <semantics><mn>1.000</mn><annotation encoding="application/x-tex">1.000</annotation></semantics> :MATH]
   (
   [MATH: <semantics><mrow><mi></mi><mo><</mo><mn>50</mn></mrow><annotation
   encoding="application/x-tex"><50</annotation></semantics> :MATH]
   neighbours) to
   [MATH: <semantics><mn>0.113</mn><annotation encoding="application/x-tex">0.113</annotation></semantics> :MATH]
   (
   [MATH: <semantics><mrow><mi></mi><mo>></mo><mrow><mn>1</mn><mo>,</mo><mn>000</mn></mrow></mrow><annotation
   encoding="application/x-tex">>1{,}000</annotation></semantics> :MATH]
   neighbours). Power-law fit
   [MATH: <semantics><mrow><mi>b</mi><mo>=</mo><mn>0.215</mn></mrow><annotation
   encoding="application/x-tex">b=0.215</annotation></semantics> :MATH]
   . DRM FA
   [MATH: <semantics><mrow><mi></mi><mo>=</mo><mn>0</mn></mrow><annotation
   encoding="application/x-tex">=0</annotation></semantics> :MATH]
   behaviourally. TOT
   [MATH: <semantics><mrow><mi></mi><mo>=</mo><mrow><mn>69</mn><mo>%</mo></mrow></mrow><annotation
   encoding="application/x-tex">=69\%</annotation></semantics> :MATH]
   , a very high partial retrieval rate.
   [MATH: <semantics><mrow><msub><mi>d</mi><mtext>eff</mtext></msub><mo>=</mo><mn>17.9</mn></mrow><annotation
   encoding="application/x-tex">d_{\text{eff}}=17.9</annotation></semantics> :MATH]
   .
   [MATH: <semantics><mrow><mi>n</mi><mo>=</mo><mn>3</mn></mrow><annotation
   encoding="application/x-tex">n=3</annotation></semantics> :MATH]
   seeds for PopQA. Refer to caption Figure 13: Extended Data Fig. 6: Filesystem Memory full results. BM25 keyword
   retrieval:
   [MATH: <semantics><mrow><mi>b</mi><mo>=</mo><mn>0.000</mn></mrow><annotation
   encoding="application/x-tex">b=0.000</annotation></semantics> :MATH]
   (no forgetting), FA
   [MATH: <semantics><mrow><mi></mi><mo>=</mo><mn>0</mn></mrow><annotation
   encoding="application/x-tex">=0</annotation></semantics> :MATH]
   (no false recall), all spacing conditions
   [MATH: <semantics><mrow><mi></mi><mo>=</mo><mn>1.0</mn></mrow><annotation
   encoding="application/x-tex">=1.0</annotation></semantics> :MATH]
   . SPP correlation
   [MATH: <semantics><mrow><mi>r</mi><mo>=</mo><mn>0.210</mn></mrow><annotation
   encoding="application/x-tex">r=0.210</annotation></semantics> :MATH]
   ; BM25 weakly satisfies semantic proximity. This architecture demonstrates Solution 2: immunity at the cost of
   usefulness. Refer to caption Figure 14: Extended Data Fig. 7: SPP verification. Mean similarity for related
   pairs (same article) vs. unrelated pairs (different articles) across all five architectures. All satisfy SPP (
   [MATH: <semantics><mrow><mi>p</mi><mo><</mo><mn>0.001</mn></mrow><annotation
   encoding="application/x-tex">p<0.001</annotation></semantics> :MATH]
   ), with embedding architectures showing stronger separation.
   [MATH: <semantics><mrow><mi>n</mi><mo>=</mo><mn>143</mn></mrow><annotation
   encoding="application/x-tex">n=143</annotation></semantics> :MATH]
   pairs. Refer to caption Figure 15: Extended Data Fig. 8: Spherical cap verification. a, Analytical cap volume
   (fraction of sphere) vs. dimension for five cap half-angles
   [MATH: <semantics><mrow><mi>θ</mi><mo>∈</mo><mrow><mo
   stretchy="false">{</mo><msup><mn>10</mn><mo>∘</mo></msup><mo>,</mo><msup><mn>20</mn><mo>∘</mo></msup><mo>,</mo>
   <msup><mn>30</mn><mo>∘</mo></msup><mo>,</mo><msup><mn>45</mn><mo>∘</mo></msup><mo>,</mo><msup><mn>60</mn><mo>∘<
   /mo></msup><mo stretchy="false">}</mo></mrow></mrow><annotation
   encoding="application/x-tex">\theta\in\{10^{\circ},20^{\circ},30^{\circ},45^{\circ},60^{\circ}\}</annotation></
   semantics> :MATH]
   , showing exponential collapse with increasing
   [MATH: <semantics><mi>d</mi><annotation encoding="application/x-tex">d</annotation></semantics> :MATH]
   . Shaded region marks the interference regime (
   [MATH: <semantics><mrow><msub><mi>d</mi><mtext>eff</mtext></msub><mo>≈</mo><mn>10</mn></mrow><annotation
   encoding="application/x-tex">d_{\text{eff}}\approx 10</annotation></semantics> :MATH]
   –
   [MATH: <semantics><mn>50</mn><annotation encoding="application/x-tex">50</annotation></semantics> :MATH]
   ) where all tested architectures operate. b, Monte Carlo verification: simulated vs. analytical cap volume on
   log–log axes for the
   [MATH: <semantics><mn>7</mn><annotation encoding="application/x-tex">7</annotation></semantics> :MATH]
   (
   [MATH: <semantics><mi>d</mi><annotation encoding="application/x-tex">d</annotation></semantics> :MATH]
   ,
   [MATH: <semantics><mi>θ</mi><annotation encoding="application/x-tex">\theta</annotation></semantics> :MATH]
   ) combinations where the Monte Carlo sample detected non-zero signal. Six of seven points fall within
   [MATH: <semantics><mrow><mo>±</mo><mrow><mn>20</mn><mo>%</mo></mrow></mrow><annotation
   encoding="application/x-tex">\pm 20\%</annotation></semantics> :MATH]
   of the
   [MATH: <semantics><mrow><mi>y</mi><mo>=</mo><mi>x</mi></mrow><annotation
   encoding="application/x-tex">y=x</annotation></semantics> :MATH]
   line; the single outlier (
   [MATH: <semantics><mrow><mi>d</mi><mo>=</mo><mn>8</mn></mrow><annotation
   encoding="application/x-tex">d=8</annotation></semantics> :MATH]
   ,
   [MATH: <semantics><mrow><mi>θ</mi><mo>=</mo><msup><mn>20</mn><mo>∘</mo></msup></mrow><annotation
   encoding="application/x-tex">\theta=20^{\circ}</annotation></semantics> :MATH]
   , ratio
   [MATH: <semantics><mrow><mi></mi><mo>=</mo><mn>0.48</mn></mrow><annotation
   encoding="application/x-tex">=0.48</annotation></semantics> :MATH]
   ) reflects finite-sample resolution at analytical volume
   [MATH: <semantics><mrow><mi></mi><mo>≈</mo><mrow><mn>8</mn><mo lspace="0.222em"
   rspace="0.222em">×</mo><msup><mn>10</mn><mrow><mo>−</mo><mn>5</mn></mrow></msup></mrow></mrow><annotation
   encoding="application/x-tex">\approx 8\times 10^{-5}</annotation></semantics> :MATH]
   , not analytical error. Marker shape encodes dimension; colour encodes
   [MATH: <semantics><mi>θ</mi><annotation encoding="application/x-tex">\theta</annotation></semantics> :MATH]
   (matching a). Confirms Theorem 2. Refer to caption Figure 16: Extended Data Fig. 9: Reproducibility across
   seeds. Per-seed values of
   [MATH: <semantics><mi>b</mi><annotation encoding="application/x-tex">b</annotation></semantics> :MATH]
   , DRM lure FA, and
   [MATH: <semantics><msub><mi>d</mi><mtext>eff</mtext></msub><annotation
   encoding="application/x-tex">d_{\text{eff}}</annotation></semantics> :MATH]
   for Vector DB and Graph architectures. Low variance confirms reproducibility.
   [MATH: <semantics><mrow><mi>n</mi><mo>=</mo><mn>5</mn></mrow><annotation
   encoding="application/x-tex">n=5</annotation></semantics> :MATH]
   seeds. Refer to caption Figure 17: Extended Data Fig. 10: Full solution analysis. a,
   [MATH: <semantics><mi>b</mi><annotation encoding="application/x-tex">b</annotation></semantics> :MATH]
   vs. nominal dimensionality. b, BM25 immunity vs. usefulness. c, Orthogonalisation methods. d, Compression:
   [MATH: <semantics><mi>b</mi><annotation encoding="application/x-tex">b</annotation></semantics> :MATH]
   (blue) and accuracy (red) vs. cluster count. Every solution traces a tradeoff; none achieves both immunity and
   usefulness.
