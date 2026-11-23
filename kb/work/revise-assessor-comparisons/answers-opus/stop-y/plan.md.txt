purpose: "Agents and maintainers who design deployed learning loops should see why persisting content is not continual learning, and what such a loop must govern: selecting, validating and authorizing behaviour-changing writes, and coordinating them across the representational forms the system can change."
must-keep:
  - "Persistence alone does not create a governed behaviour-changing write: behavioral authority belongs to a consumption path, not to stored bytes."
  - "If prompts, tools, validators and runtime policy also determine behaviour, an updater restricted to weights freezes consequential choices outside its reach."
  - "Hand-authored changes are learning too: the software learns by selection that people perform on it."
passes: []
stop: >-
  Defect (two readings; claim wrong or unsupported). The claim is "Continual learning, as the field uses the term and as this note uses it, asks for more: the system does the selecting itself", together with the discriminator "A behaviour-changing write counts as continual learning when the system's own loop selects and retains it ... for retained candidates, search, reject-capable evaluation, and operative retention".
  The note's wording supports two readings of the title's "requires". Reading A, constitutive: ungoverned durable change is not continual learning. Then online gradient or replay/EWC-style continual learning is excluded, although the note's third paragraph calls it "parametric continual learning". Reading B, reliability: governance is what continual learning needs to be safe. Then direct updates count, and the discriminator paragraph overstates.
  The attribution to field usage is unsourced. The reports say it is false of the ML continual-learning literature, which centres on non-stationary streams and forgetting. This makes "requires" partly true by definition.
  Correcting this changes the thesis, the opening claim and possibly the title, so it is a rewrite, not a pass. The same rewrite should also re-ground or mark as conjecture the regression premise "continual adaptation compounds silent degradation", whose only citation (scheduler-LLM separation) does not support it (grounding-alignment fail).
  Reports:
  kb/reports/state/review/results/kb/theory/continual-learning-requires-governing-behaviour-changing-writes.md/kb/instructions/critique-note.md;
  kb/reports/state/review/results/kb/theory/continual-learning-requires-governing-behaviour-changing-writes.md/kb/instructions/premise-decomposition-gate.md;
  kb/reports/state/review/results/kb/theory/continual-learning-requires-governing-behaviour-changing-writes.md/kb/instructions/composition-friction-gate.md;
  kb/reports/state/review/results/kb/theory/continual-learning-requires-governing-behaviour-changing-writes.md/semantic/underspecified-assertions.md;
  kb/reports/state/review/results/kb/theory/continual-learning-requires-governing-behaviour-changing-writes.md/semantic/epistemic-status-blur.md;
  kb/reports/state/review/results/kb/theory/continual-learning-requires-governing-behaviour-changing-writes.md/semantic/grounding-alignment.md.
  Dependents rely on the system-selected discriminator and on the regression requirement. The role report's run directory is kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/role.
  The discriminator is relied on by kb/sources/hot-take-llm-can-jump.ingest.md and kb/sources/on-learning-how-to-learn-learning-strategies.ingest.md. kb/sources/hyra-2-next-step-for-auto-research.ingest.md cites human approval in a way the discriminator leaves open.
  The regression requirement is relied on by kb/sources/dfa-moe-dual-forgetting-vision-language-continual-learning.ingest.md, kb/sources/dual-nature-generalization-on-policy-distillation.ingest.md, kb/sources/merchantbench-long-term-coherence.ingest.md, kb/sources/harness-continual-learning-adaptation-beyond-model-parameters.ingest.md and kb/sources/long-horizon-agents-levels-ticks-cascaded-intelligence.ingest.md.
  A title change would reach all 48 linking files, and 18 of them are unseen.
  The operator must decide these dependents' changes too.
  Route: commonplace-revise rewrite kb/theory/continual-learning-requires-governing-behaviour-changing-writes.md --commission FILE, with the commission prepared using cp-skill-write-multistage.
