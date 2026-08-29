# What survived learned absorption in four technical episodes

## Headline finding

The examined record tells against treating retained, reviewed natural-language
theory as a historically protected survivor class.

Across the four episodes examined here, learned methods chiefly absorbed
components that estimated an answer or allocated search through
task-specific heuristics. They absorbed some such components even after the
components had been tested, tuned, and commercially deployed. The strongest
explicit survivors fall into two narrower classes:

1. **Boundary and authority inputs** define the task or supply information the
   system does not get to infer: the legal environment, objective, current
   observation, accepted record, or required output interface. The function
   must exist somewhere, but no particular file, component, or
   representational form is protected.
2. **Locally specified operators** have behavior that can be checked against a
   formal or physical specification within a stated domain: legal-move
   generation, bounded exact table lookup, a declared optimization problem,
   or an exact format check. Keeping the operator explicit can preserve a
   guarantee or lower cost, but the record supports only conditional survival.
   A later architecture can move, relax, or remove the operator.

This is my synthesis over the examined set, not a result stated by any one
source. It does not supply the proposed article with a broad disanalogy
between hand-crafted features and retained theory. It supplies a narrower
test. Commonplace's authoritative records, current state, and exact checks
have analogues among the survivors. Its semantic theories, instructions,
decompositions, and review rubrics remain exposed to the same empirical
comparison that displaced hand-built features.

## Examined set and method

I examined four episodes selected to cover the handoff's proposed cases and
one canonical vision transition:

- two-dimensional visual recognition and object detection;
- multiview three-dimensional vision and structure from motion;
- chess and general board-game engines; and
- automatic speech recognition.

This is a purposive set, not a random sample. Findings below apply to these
episodes only. “Still in use” means visible in an active official
implementation or a recent documented system as of 2026-08-29. That test
establishes existence, not prevalence. I trace components through successive
architectures because a component retained by the first learned replacement
can be absorbed by the next one.

I distinguish three facts that are easy to collapse:

- a *function* remains necessary;
- an *explicit component* currently performs that function; and
- a particular *artifact or representation* remains necessary.

Only the first follows from a task boundary. The second is an architectural
choice. The third requires separate evidence.

### The displaced vision era was commercial

The history cannot be framed as learning replacing unused academic ideas.
An industrial vision system inspected ignition parts on a General Motors
production line in 1977.[^gm-vision] A retrospective by one of the system's
developers reports that thirty Philco postal OCR machines were installed and
that the system processed billions of mail pieces in operation.[^postal-ocr]
Sony marketed consumer Cyber-shot cameras with face-detection functions in
2009.[^sony-camera] These sources are representative deployments, not a claim
about market prevalence. They are enough to rule out an academic-only
characterization.

## Episode results

| Episode | Structure displaced by learning | Explicit structure retained in a current or recent lineage | Adverse evidence against permanence |
|---|---|---|---|
| 2D recognition and detection | designed feature families, descriptors, part templates, and successive proposal/post-processing stages | task labels and output contract; architecture-specific decoding | R-CNN retained proposals and suppression; YOLO removed the proposal pipeline; DETR removed anchors and non-maximum suppression |
| Multiview 3D vision | some local features, matching heuristics, camera prediction, and triangulation stages | camera and observation models, geometric verification, global alignment, bundle adjustment in active hybrid systems | VGGSfM learns more of the pipeline; DUSt3R relaxes calibration and hard projective-camera prerequisites |
| Board-game engines | expert evaluation terms, move-ordering knowledge, and domain-specific search enhancements | explicit search, legal-move generation, rules or environment interface, and optional exact tablebases | AlphaZero removed more expert search machinery; MuZero learned the planning dynamics instead of receiving a rule simulator |
| Speech recognition | separate acoustic, pronunciation, phoneme, and language modules | model-specific signal representation, tokenizer, decoder/search, timestamp/alignment machinery, plus the input and output interfaces | raw-waveform encoders remove fixed spectral frontends; larger sequence models integrate language and alignment functions |

The table records components, not whole systems. Each episode contains hybrid
systems, and the boundary moved more than once.

### 1. Two-dimensional visual recognition and object detection

The older systems were not simply “rules instead of learning.” Viola and
Jones fixed a Haar-like feature family and cascade architecture, then used
AdaBoost to select and combine features.[^viola-jones] HOG fixed a gradient
histogram representation,[^hog] while the deformable-parts model combined
designed feature extraction and a designed part decomposition with
discriminative training.[^dpm] The relevant distinction is therefore not
hand-coded versus trained. It is which representational and pipeline choices
were fixed before end-task optimization.

The first deep detector did not absorb the whole pipeline. R-CNN replaced the
feature representation with a convolutional network and beat the then-strong
deformable-parts baseline, but retained Selective Search region proposals,
per-region scoring, bounding-box regression, and non-maximum suppression.[^rcnn]
YOLO then predicted boxes and class probabilities in one network evaluation,
removing the proposal-and-classify pipeline while retaining output decoding
and non-maximum suppression.[^yolo] DETR formulated detection as set
prediction with bipartite matching and removed anchors and non-maximum
suppression.[^detr] A 2024 real-time DETR lineage continued this end-to-end
direction.[^rtdetr]

**Episode result.** No perception-side component in this sequence earns a
stable survivor designation. Components that looked complementary at one
transition became substitution targets at the next. The task still supplies
what counts as an object, the training/evaluation labels, and an output
interface. Those are boundary conditions, not survivors of the old feature
pipeline. Even the choice of boxes rather than another output representation
is contingent on the task.

### 2. Multiview three-dimensional vision

The canonical incremental structure-from-motion pipeline made feature
extraction and matching, geometric verification, camera registration,
triangulation, and bundle adjustment separate components.[^sfm-revisited]
This episode initially appears to give a clean split: learned local features
replace SIFT-like frontends while projective geometry and bundle adjustment
remain explicit.

That split is real in an important current hybrid. COLMAP 4.1.1 was released
in July 2026, and its development documentation dated 2026-08-28 offers both
classic SIFT and learned ALIKED and LoMa extractors, neural LightGlue/LoMa
matchers, and the geometric reconstruction backend. Its 4.1 release also
added another explicit bundle-adjustment backend rather than removing bundle
adjustment.[^colmap-current] SuperGlue illustrates the same earlier boundary:
it learned matching priors between a deep local-feature frontend and a
geometric pose/optimization backend.[^superglue]

The boundary is nevertheless moving. VGGSfM makes camera prediction and
triangulation differentiable and learned while retaining differentiable
bundle adjustment.[^vggsfm] DUSt3R regresses pointmaps without requiring
known calibration or poses and deliberately relaxes hard projective-camera
constraints, while retaining a global alignment problem across views.[^dustr]

**Episode result.** Geometry has the strongest modular survival case in this
set, but not because a model is categorically unable to represent it. A
camera model and a bundle-adjustment objective give an explicit local
contract: residuals, constraints, and solver behavior can be inspected apart
from the learned feature predictor. That supports retaining an operator when
its assumptions fit and its guarantee/cost is valuable. It does not protect
the decomposition. DUSt3R shows that calibration and a hard projective-camera
pipeline can be traded for learned prediction and a different alignment
contract. Bundle adjustment itself is also not an exact oracle for scene
truth: its measurement model and initialization remain empirical choices.

### 3. Board-game engines

Deep Blue combined alpha-beta search with extensive chess-specific evaluation
features, search extensions, and databases.[^deep-blue] The same basic
transition is visible inside a continuing engine lineage. Stockfish's
classical evaluator computed a score from expert-designed chess concepts.
NNUE was added as its learned alternative in 2020 with an immediate measured
playing-strength gain, and the classical evaluator was removed in 2023.
Current Stockfish still feeds the learned evaluation into alpha-beta/PVS
search.[^stockfish-nnue]

Stockfish 18, released in 2026, still contains explicit legal-move generation
and Syzygy WDL/DTZ tablebase probing.[^stockfish-source] These are stronger
survivors than search heuristics. Legal moves are decidable from the declared
rules. Within their bounded state space, tablebases return precomputed game
outcomes or distances rather than a statistical estimate. The tablebase is
optional, however: it survives because an exact bounded answer is useful and
cheap enough at probe time, not because play is impossible without it.

AlphaZero removed handcrafted evaluation, move ordering, and domain-specific
search enhancements across chess, shogi, and Go. It retained a general Monte
Carlo tree search and received the game rules and terminal outcome from an
external environment.[^alphazero] MuZero is the decisive adverse case for a
literal “the model cannot hold rules” claim: its planning model learned the
dynamics, reward, and value relevant to search without receiving the
environment's transition rules. The environment still supplied observations,
actions, and rewards.[^muzero]

**Episode result.** The declared game and objective must exist somewhere, but
their full transition implementation need not remain an explicit component
inside the planner. Exact legality and tablebase functions have a conditional
guarantee/cost case. Tree search is a different kind of survivor: it allocates
inference-time compute and remains only while that allocation beats the
available alternatives under the resource budget. The record does not make
search intrinsically permanent.

### 4. Automatic speech recognition

Deep Speech 2 replaced separate acoustic and pronunciation machinery with a
neural character predictor and collapsed much of the older pipeline, but its
“end-to-end” system still used spectrogram inputs, CTC, beam search, an n-gram
language model, and application-specific post-processing.[^deep-speech-2] Whisper
later integrated multilingual transcription, translation, language
identification, and timestamp prediction in one sequence-to-sequence model,
while retaining log-Mel spectrograms and a byte-level BPE tokenizer.[^whisper]

Those retained interfaces do not form a stable technical class. wav2vec 2.0
learned its feature encoder from raw waveform rather than requiring a fixed
spectral representation.[^wav2vec] Qwen3-ASR in 2026 integrates broad language
modeling with transcription and supplies a learned forced-aligner model for
timestamps across multiple languages, displacing more language-specific
alignment machinery while still exposing audio and text interfaces.[^qwen-asr]

**Episode result.** Phonemes, pronunciation dictionaries, a separate language
model, fixed signal transforms, tokenization, search, and post-processing can
all remain explicit in a particular architecture. The sequence provides no
evidence that any one of them must. The stable boundary is functional: a
current audio signal enters, a transcription objective defines success, and
the requested text/timestamps leave. Particular encodings and decoding
stages remain engineering choices.

## A checkable characterization over the examined set

The following is my inference from the four episodes. It is a proposed test
for a new component, not a prevalence claim.

### Class A: boundary or authority source

Ask: **If a model reproduced the component's content, would that reproduction
itself define the task, change the current world, or become the accepted
record?**

If no, the function is a boundary or authority source. Examples in the
examined set are game objectives, environment observations and rewards,
training/evaluation targets, current audio or images, and the output contract.
The content may be encoded or predicted inside a model, but task identity,
currentness, and authority still require an input or designation. Prediction:
the function persists somewhere across architectures, while its carrier and
location can change.

### Class B: locally specified operator

Ask: **Can the claimed behavior be checked against a specification over its
declared domain without using only end-task benchmark performance?**

Legal-move generation and bounded tablebase lookup clearly pass. A geometric
solver passes for conformity to its declared objective, although the fit of
the objective to scene truth remains empirical. Prediction: an explicit
operator has a conditional survival case when modular implementation gives a
better guarantee, audit trail, latency, or resource cost. It has no
presumption of permanence: an architecture can remove the need for the
operator, place it in training or verification, or learn an approximation and
retain only a check.

### Class C: empirical proxy or scaffold

Ask: **Is the component ultimately warranted by downstream task performance,
and does it estimate, represent, decompose, rank, or search for an answer?**

If yes, it competes directly with learned alternatives. Haar/HOG features,
part models, region proposals, handcrafted chess evaluation, matching
heuristics, pronunciation modules, fixed signal frontends, tokenizers, and
search policies land here. Prediction: the component receives no survival
presumption from being explicit, interpretable, tested, or currently useful.
Search can persist because inference-time compute is valuable, but that is a
contingent cost/performance result.

This test classifies an operative part, not a file type. A single artifact can
contain an authoritative commitment, an empirical theory, and exact syntax;
those parts land in different classes.

## Test of the substitute/complement hypothesis

The proposed substitute/complement distinction is directionally useful only
after narrowing “cannot hold.”

- It works for **authority and current state**. A parameterized model may
  reproduce a policy or remember an old observation, but reproduction does
  not adopt the policy or observe a changed world.
- It sometimes works for **locally specified exactness**. An explicit legal
  move check or tablebase can complement a learned evaluator by giving a
  guarantee over a bounded domain. The reason to retain it is comparative
  warrant and cost, not representational incapacity.
- It fails as a literal limit on **rules, geometry, signal processing, or
  encoding**. MuZero learned planning dynamics, DUSt3R relaxed an explicit
  camera model, and wav2vec 2.0 learned from waveform. Those examples show
  that a learned system can internalize or route around structure previously
  supplied as a component.
- It does not protect **tested structure**. Stockfish's classical evaluation
  was continuously tested and tuned, and the old vision systems were
  benchmark-tested and deployed. A reject-capable test can select the learned
  replacement. It improves the production method; it does not guarantee that
  the selected structure remains explicit.

A version supported by this set is therefore: *empirical substitutes are
exposed to learned replacement; boundary/authority functions must remain
somewhere; locally specified operators survive only while their modular
guarantee or economics beats integration.*

## Strongest counter-characterization

**The apparent survivors are merely the current edge of architectural
absorption, not an epistemically distinct class.**

The same record supports this hostile reading. R-CNN left proposals and
non-maximum suppression, then YOLO and DETR removed them. Hybrid 3D systems
left geometry explicit, then VGGSfM and DUSt3R learned or relaxed more of it.
Deep Speech 2 left a signal transform, external language model, search, and
post-processing, while later systems integrated adjacent functions. AlphaZero
left explicit rules in its planner; MuZero learned planning dynamics. What
remains can be explained by training data, differentiability, compute,
latency, liability, and implementation maturity at a given date.

On this account, Class A is only a restatement that every evaluated system has
an environment and objective, not evidence for retaining a knowledge
artifact. Class B survives because a small exact component is currently cheap
and reliable, not because it occupies a permanent representational niche.
Successive systems may shrink it to an interface or verifier. This
counter-characterization fits every examined episode. The record cannot
decide between permanent complementarity and a moving engineering frontier;
it can only reject claims of permanence based on present retention.

## Comparison with Commonplace artifact kinds

This comparison uses Commonplace's own distinction between a
[knowledge artifact](../../notes/definitions/knowledge-artifact.md) and a
[system-definition artifact](../../notes/definitions/system-definition-artifact.md),
and its warning that content kind, lineage, and authority are separate
[classification axes](../../notes/artifact-classification-separates-content-kind-lineage-and-authority.md).
It classifies operative parts rather than granting a status to Markdown,
code, or any whole collection.

| Commonplace operative part | Class under the characterization | Comparison with the examined record |
|---|---|---|
| Adopted ADR choices, collection/type contracts, declared objectives, permissions, and accepted baselines | A: boundary/authority | Their content can be reproduced, but reproduction does not perform the adoption or establish which version is current. The authority function persists unless governance is redesigned; the file format does not. This matches [commitment, not derivation, creates new ground truth](../../notes/commitment-not-derivation-creates-new-ground-truth.md) and [parametric reproduction cannot replace an authoritative record](../../notes/parametric-reproduction-cannot-replace-an-authoritative-record.md). |
| Source snapshots, citations, and provenance records | A for exact historical identity; C for semantic interpretation | If audit and contestability remain requirements, exact source bytes and lineage must stay externally addressable. A model may absorb their semantic content without becoming the source or retaining its provenance. |
| Current observations, measurements, review results, and operational store state | A: current-state input/record | Unobserved current facts require a channel or record. Their schema and storage engine remain replaceable. |
| Schemas, parsers, deterministic validators, exact commands, and mechanically generated marks | B where the criterion is locally decidable | An explicit implementation can provide inspectable conformance and reproducibility. That is a conditional implementation case, not validation of the requirement itself; see [exact implementation does not validate a requirement](../../notes/exact-implementation-does-not-validate-a-requirement.md). |
| Tests, gates, critics, and evaluators | Split B/C | A syntax check or executable oracle can be locally specified. A semantic rubric or model judge is an empirical predictor of acceptance and remains exposed. Passing either test does not protect the tested artifact from a better replacement. |
| Natural-language definitions, mechanisms, theories, and syntheses | Usually C for their semantic role | Their value is whether they improve interpretation and decisions. Review can increase current warrant, but the examined history gives no reason that reviewed semantic structure must remain explicit. A section that also records an adopted decision or source identity must be classified separately. |
| Skills, prompts, routing rules, decompositions, and prose instructions | Usually C; A where text itself constitutes policy or an interface | As methods for eliciting model behavior, they are empirical scaffolds. Search-selected production is compatible with replacing them. Only an adopted constraint or required interface has the stronger authority status. |
| Program code | Split A/B/C by function | Symbolic form alone does not protect code. A rule declaration may define a boundary, a validator may implement a local check, and a heuristic scheduler may be an empirical scaffold. |
| Indexes, summaries, embeddings, caches, and other derived navigation | Usually C and regenerable | Retention is justified by current retrieval quality and recomputation cost. These are close analogues of pipeline scaffolding, not historical survivors by kind. |

The local definition of a [retained artifact](../../notes/definitions/retained-artifact.md)
therefore does not determine its side of the boundary. Retention describes
availability across calls; it does not establish authority, exactness, or
comparative value. Likewise, the claim that
[machinery persists by warrant](../../notes/machinery-persists-by-warrant-not-position-in-a-reflective-loop.md)
is compatible with replacement: a later comparison can withdraw the warrant
for the incumbent machinery.

## What this permits the article to say

The historical record examined here does **not** support this premise:

> Commonplace's retained natural-language theories differ in kind from the
> hand-built structure that learned systems absorbed because the theories have
> survived a reject-capable review process.

The review process can select useful theory, just as benchmarks and game
testing selected useful components in the older systems. It can also select a
learned replacement. Most semantic notes and instructions remain in Class C
unless a comparison shows that retaining them improves the declared outcome.

A narrower premise is consistent with the record:

> A mixed system may need explicit channels for authoritative commitments and
> current state, and may retain locally specified operators when their
> guarantees or economics justify modularity. Its semantic theory and
> scaffolding receive no exemption from empirical replacement.

That statement is a characterization of the examined history and a mapping,
not evidence that Commonplace has chosen the right artifacts or that its
current allocation will persist.

## Confidence and limits

- **High confidence** in the component histories reported for the four
  episodes: each transition is documented by a primary paper, and claims of
  current retention use official documentation or source.
- **Moderate confidence** in the three-class characterization. It explains the
  examined cases and yields a checkable question, but the set was purposive
  and small.
- **Low confidence** in any permanence forecast. The successive-absorption
  counter-characterization fits the same evidence, and future architectures
  can move present boundaries.

No paywalled or uncapturable source is load-bearing here. The commercial
deployment examples establish existence, not a survey of commercial use. The
current implementation checks establish that a component is available in an
active lineage, not its usage share. No source found could settle whether
today's explicit complement remains explicit indefinitely; that is not a
historical fact available in 2026.

## Sources

[^gm-vision]: Author not listed, “General Motors Uses Computer Vision to Inspect Electronic Ignition Parts,” *Information Display*, Society for Information Display, 1977. [DOI 10.1002/j.2637-496X.1977.tb01422.x](https://doi.org/10.1002/j.2637-496X.1977.tb01422.x).

[^postal-ocr]: Thomas J. Hartley, “Tales from the Vault: ‘P’ Picker Led to Postal OCR System,” *IEEE Life Members*, IEEE, 2026. <https://life.ieee.org/2026/06/tales-from-the-vault-p-picker-led-to-postal-ocr-system/>.

[^sony-camera]: Sony Corporation, “Sony to Showcase Latest DI Products at ‘PMA 2009’ Exhibition,” Sony Group press release, 2009. <https://www.sony.com/en/SonyInfo/News/Press/200903/09-031E/>.

[^viola-jones]: Paul Viola and Michael J. Jones, “Robust Real-Time Face Detection,” *International Journal of Computer Vision* 57(2), Springer, 2004, pp. 137–154. [DOI 10.1023/B:VISI.0000013087.49260.FB](https://doi.org/10.1023/B:VISI.0000013087.49260.FB).

[^hog]: Navneet Dalal and Bill Triggs, “Histograms of Oriented Gradients for Human Detection,” *Proceedings of the IEEE Computer Society Conference on Computer Vision and Pattern Recognition*, IEEE, 2005. [DOI 10.1109/CVPR.2005.177](https://doi.org/10.1109/CVPR.2005.177).

[^dpm]: Pedro F. Felzenszwalb, Ross B. Girshick, David McAllester, and Deva Ramanan, “Object Detection with Discriminatively Trained Part-Based Models,” *IEEE Transactions on Pattern Analysis and Machine Intelligence* 32(9), IEEE, 2010, pp. 1627–1645. [DOI 10.1109/TPAMI.2009.167](https://doi.org/10.1109/TPAMI.2009.167).

[^rcnn]: Ross Girshick, Jeff Donahue, Trevor Darrell, and Jitendra Malik, “Rich Feature Hierarchies for Accurate Object Detection and Semantic Segmentation,” *Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition*, IEEE/CVF, 2014. <https://openaccess.thecvf.com/content_cvpr_2014/papers/Girshick_Rich_Feature_Hierarchies_2014_CVPR_paper.pdf>.

[^yolo]: Joseph Redmon, Santosh Divvala, Ross Girshick, and Ali Farhadi, “You Only Look Once: Unified, Real-Time Object Detection,” *Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition*, IEEE/CVF, 2016. <https://openaccess.thecvf.com/content_cvpr_2016/papers/Redmon_You_Only_Look_CVPR_2016_paper.pdf>.

[^detr]: Nicolas Carion, Francisco Massa, Gabriel Synnaeve, Nicolas Usunier, Alexander Kirillov, and Sergey Zagoruyko, “End-to-End Object Detection with Transformers,” *Computer Vision – ECCV 2020*, Springer, 2020. <https://arxiv.org/abs/2005.12872>.

[^rtdetr]: Yian Zhao et al., “DETRs Beat YOLOs on Real-time Object Detection,” *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*, IEEE/CVF, 2024. <https://openaccess.thecvf.com/content/CVPR2024/papers/Zhao_DETRs_Beat_YOLOs_on_Real-time_Object_Detection_CVPR_2024_paper.pdf>.

[^sfm-revisited]: Johannes L. Schönberger and Jan-Michael Frahm, “Structure-From-Motion Revisited,” *Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition*, IEEE/CVF, 2016. <https://openaccess.thecvf.com/content_cvpr_2016/papers/Schonberger_Structure-From-Motion_Revisited_CVPR_2016_paper.pdf>.

[^colmap-current]: COLMAP Development Team, “COLMAP 4.1.1,” official release, 2026, and “Feature Extraction and Matching,” COLMAP 4.2.0.dev0 documentation, revision `6c5b1dd`, 2026-08-28. <https://github.com/colmap/colmap/releases/tag/4.1.1>; <https://colmap.github.io/features.html>.

[^superglue]: Paul-Edouard Sarlin, Daniel DeTone, Tomasz Malisiewicz, and Andrew Rabinovich, “SuperGlue: Learning Feature Matching with Graph Neural Networks,” *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*, IEEE/CVF, 2020. <https://openaccess.thecvf.com/content_CVPR_2020/papers/Sarlin_SuperGlue_Learning_Feature_Matching_With_Graph_Neural_Networks_CVPR_2020_paper.pdf>.

[^vggsfm]: Jianyuan Wang, Nikita Karaev, Christian Rupprecht, and David Novotny, “VGGSfM: Visual Geometry Grounded Deep Structure From Motion,” *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*, IEEE/CVF, 2024. <https://openaccess.thecvf.com/content/CVPR2024/papers/Wang_VGGSfM_Visual_Geometry_Grounded_Deep_Structure_From_Motion_CVPR_2024_paper.pdf>.

[^dustr]: Shuzhe Wang, Vincent Leroy, Yohann Cabon, Boris Chidlovskii, and Jérôme Revaud, “DUSt3R: Geometric 3D Vision Made Easy,” *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*, IEEE/CVF, 2024. <https://openaccess.thecvf.com/content/CVPR2024/papers/Wang_DUSt3R_Geometric_3D_Vision_Made_Easy_CVPR_2024_paper.pdf>.

[^deep-blue]: Murray Campbell, A. Joseph Hoane Jr., and Feng-hsiung Hsu, “Deep Blue,” *Artificial Intelligence* 134(1–2), Elsevier, 2002, pp. 57–83. <https://research.ibm.com/publications/deep-blue>.

[^stockfish-nnue]: Stockfish Developers, “Introducing NNUE Evaluation,” official Stockfish project blog, 2020, and “Classical versus NNUE evaluation,” *Stockfish Docs*, 2026. <https://stockfishchess.org/blog/2020/introducing-nnue-evaluation/>; <https://official-stockfish.github.io/docs/stockfish-wiki/Advanced-topics.html#classical-versus-nnue-evaluation>.

[^stockfish-source]: Stockfish Developers, *Stockfish 18 source*, official project release, 2026: `movegen.cpp` and `syzygy/tbprobe.cpp`. <https://github.com/official-stockfish/Stockfish/blob/sf_18/src/movegen.cpp>; <https://github.com/official-stockfish/Stockfish/blob/sf_18/src/syzygy/tbprobe.cpp>.

[^alphazero]: David Silver et al., “A General Reinforcement Learning Algorithm that Masters Chess, Shogi, and Go through Self-Play,” *Science* 362(6419), American Association for the Advancement of Science, 2018, pp. 1140–1144. [DOI 10.1126/science.aar6404](https://doi.org/10.1126/science.aar6404); [author manuscript](https://discovery.ucl.ac.uk/10069050/1/alphazero_preprint.pdf).

[^muzero]: Julian Schrittwieser et al., “Mastering Atari, Go, Chess and Shogi by Planning with a Learned Model,” *Nature* 588, Springer Nature, 2020, pp. 604–609. [DOI 10.1038/s41586-020-03051-4](https://doi.org/10.1038/s41586-020-03051-4); <https://arxiv.org/abs/1911.08265>.

[^deep-speech-2]: Dario Amodei et al., “Deep Speech 2: End-to-End Speech Recognition in English and Mandarin,” *Proceedings of the 33rd International Conference on Machine Learning*, PMLR 48, 2016, pp. 173–182. <https://proceedings.mlr.press/v48/amodei16.html>.

[^whisper]: Alec Radford, Jong Wook Kim, Tao Xu, Greg Brockman, Christine McLeavey, and Ilya Sutskever, “Robust Speech Recognition via Large-Scale Weak Supervision,” *Proceedings of the 40th International Conference on Machine Learning*, PMLR 202, 2023, pp. 28492–28518. <https://proceedings.mlr.press/v202/radford23a.html>.

[^wav2vec]: Alexei Baevski, Yuhao Zhou, Abdelrahman Mohamed, and Michael Auli, “wav2vec 2.0: A Framework for Self-Supervised Learning of Speech Representations,” *Advances in Neural Information Processing Systems* 33, NeurIPS, 2020. <https://papers.nips.cc/paper/2020/hash/92d1e1eb1cd6f9fba3227870bb6d7f07-Abstract.html>.

[^qwen-asr]: Xian Shi et al., “Qwen3-ASR Technical Report,” arXiv:2601.21337v2, 2026. [DOI 10.48550/arXiv.2601.21337](https://doi.org/10.48550/arXiv.2601.21337).
