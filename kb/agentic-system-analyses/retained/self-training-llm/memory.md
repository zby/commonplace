---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Self-Training-LLM memory: persisted training candidates, score-driven parameter updates, evaluation caches and bounded per-call context."
run-id: AAS-2026-10-15-self-training-llm-5b5ee621bde2-01
source-identity: "https://github.com/wj210/Self-Training-LLM"
reviewed-boundary: "97839b29d0fd8bb474f5549fa3e9d6ca504732e0"
---

# Self-Training-LLM memory report

## Boundary and evidence

The memory boundary is the shipped improvement workflow's retained documents, generated questions/answers, derived scores, trained parameters, evaluation artifacts and exposed topic-cache helpers. It follows the whole-system builder boundary in `boundary.md`, not a conversational-memory interpretation. Source evidence is SRC-1 at commit `97839b29d0fd8bb474f5549fa3e9d6ca504732e0`. There are no supplied weights, generated files, provider transcripts or executed-run observations. Local files establish implementation, not exercised learning or factual correctness.

Direct inspection covered `uncertainty/wiki_generation.py` completely; `uncertainty/topic_generator.py` completely; the selection, persistence and formatting branches in `uncertainty/train.py`, `uncertainty/data_utils.py`, `uncertainty/utils.py`, `uncertainty/self_learning_training.py`; generation/evaluation drivers completely; scoring and judge-cache branches in `uncertainty/scorer.py`; prompt formatters in `uncertainty/templates.py`; all four shell launchers; TinyLlama and Wikipedia configurations and both trainer configurations. These are implementation evidence. Runtime findings are supplied evidence where linked below, and do not substitute for direct inspection of the additional parts. Other model configurations and shipped example-list bodies were not comprehensively read by this member; no claim about their individual content or equivalence follows. External dataset/provider/framework internals and compiled caches remain excluded as in the boundary.

### Coverage inventory

| Entry point or operation | Source paths, SRC-1 | Records and inspection basis | Limit and conclusion prevented |
|---|---|---|---|
| Shell dispatch, generation CLI, document-cache build/reload | `script/wiki_ques_gen.sh`, `uncertainty/wiki_generation.py`, `uncertainty/data_utils.py` | Direct; [MEM-OBJ-topic-docu](#mem-obj-topic-docu), [RT-RTE-data-generation](runtime.md#rt-rte-data-generation) | Fresh-start defects in runtime still apply; cannot assert turnkey completion. |
| Question/test JSONL and context-label creation/reload | `uncertainty/wiki_generation.py`, `uncertainty/topic_generator.py` | Direct; [MEM-OBJ-questions](#mem-obj-questions), [MEM-OBJ-test](#mem-obj-test), [MEM-OBJ-context-answer](#mem-obj-context-answer) | Existence/count reuse does not establish provenance or quality. |
| Self/GPT labels, raw samples, alternate-generator remapping, rescoring | `uncertainty/wiki_generation.py`, `uncertainty/scorer.py`, `uncertainty/data_utils.py` | Direct; [MEM-OBJ-answer-content](#mem-obj-answer-content), [MEM-OBJ-answer-scores](#mem-obj-answer-scores) | Provider-object compatibility and branch success unobserved. |
| SFT/DPO filtering, preference selection, context addition, parameter save/merge | `script/train.sh`, `uncertainty/train.py`, `uncertainty/self_learning_training.py` | Direct; annotations on [RT-RTE-model-training](runtime.md#rt-rte-model-training), [RT-CMP-causal-model](runtime.md#rt-cmp-causal-model) | Score-based admission is not factual validation; no judge veto. |
| Direct checkpoint/TGI inference, known-subset persistence, RAG context | `script/tgi.sh`, `script/testing.sh`, `uncertainty/generate_response.py` | Direct; [MEM-OBJ-known](#mem-obj-known), [MEM-OBJ-responses](#mem-obj-responses), [RT-RTE-response-generation](runtime.md#rt-rte-response-generation) | Endpoint weight identity is external to the client; RAG is stored-document inclusion, not vector search. |
| Pairwise evaluation, cache hit/miss, failed-reply omission, results append | `uncertainty/pairwise_eval.py`, `uncertainty/scorer.py` | Direct; [MEM-OBJ-judge-cache](#mem-obj-judge-cache), [MEM-OBJ-results](#mem-obj-results), [RT-RTE-pairwise-evaluation](runtime.md#rt-rte-pairwise-evaluation) | No supplied results or automatic training consumption. |
| Exposed WordNet, embedding, view-ranking and cached topic/split helpers | `uncertainty/topic_generator.py`, `uncertainty/data_utils.py` | Direct; [MEM-CMP-topic-embedder](#mem-cmp-topic-embedder), [MEM-OBJ-topic-caches](#mem-obj-topic-caches) | Active `get_wiki` calls predefined selection instead. Helper availability is not an exercised semantic-memory route; FAISS import is commented. |
| Prompt construction, sentence cleanup, document chunking, NLI truncation | `uncertainty/templates.py`, `uncertainty/utils.py`, `uncertainty/data_utils.py`, `uncertainty/scorer.py` | Direct; annotations on [RT-RTE-data-generation](runtime.md#rt-rte-data-generation) and [RT-RTE-response-generation](runtime.md#rt-rte-response-generation) | No growing transcript was inspected; these are per-call context controls. |
| Other public dataset-loading helpers | `uncertainty/data_utils.py` | Direct `load_train_ds` and `get_wiki` dispatch inspection; [RT-RTE-model-training](runtime.md#rt-rte-model-training) | Non-Wikipedia SFT options import external datasets; no endogenous retained-memory lineage inferred for those datasets. Unrelated test-data helper bodies not comprehensively inspected. |

The Python/shell search for topic-helper call sites and tool/hook terms found the topic alternatives inside `topic_generator.py` and the commented `get_top_articles` call in `get_wiki`. The inspected launchers dispatch the four stages; no model-selected tool registration or hook-driven retrieval was identified in these dispatch paths. This bounded search is not a claim about external libraries or serving internals (SRC-1, `script/`, `uncertainty/data_utils.py`, `uncertainty/topic_generator.py`).

## Core ideas

1. **Files carry the training experience; parameters carry its later generative effect.** Generated text and classifier-derived scores persist together, but play different roles. Training uses scores to select examples and then strips them from the actual DPO trainer input. Later inference loads weights, not the scoring reasons. See [MEM-OBJ-answer-content](#mem-obj-answer-content), [MEM-OBJ-answer-scores](#mem-obj-answer-scores) and [RT-BAP-checkpoint-consumption](runtime.md#rt-bap-checkpoint-consumption).
2. **Context is deliberately unequal across consumers.** Question generation sees chunks; reference answers can see documents; raw answer samples do not; ordinary trained-model evaluation omits documents while RAG supplies them. Classifier truncation and fixed examples further constrain visibility. These are separate call frames, not transcript summarization ([RT-RTE-data-generation](runtime.md#rt-rte-data-generation), [RT-RTE-response-generation](runtime.md#rt-rte-response-generation)).
3. **Retention is mostly path/existence based.** Cached documents, questions, labels, subsets and judge outcomes can survive changed configuration. The final answer file is rescored and overwritten rather than maintained as an immutable derivation history. Scores are not reasons, and dataset labels such as `gold`, `known` and `oracle` do not certify truth ([MEM-OBJ-answer-scores](#mem-obj-answer-scores), [MEM-OBJ-judge-cache](#mem-obj-judge-cache), [MEM-OBJ-known](#mem-obj-known)).
4. **Admission is automated within operator-launched stages.** The operator selects flags and paths, but code/model checks admit individual records. Direct content editing is possible through mutable files, not a shipped review UI or per-record approval protocol. Authorship, software admission and physical file writing must remain separate ([RT-RTE-model-training](runtime.md#rt-rte-model-training)).

## Shared records

### Components

#### MEM-CMP-topic-embedder
Label: SentenceTransformer topic embedder

Source-native identity: `SentenceTransformer("sentence-transformers/all-MiniLM-L12-v2")` in `get_embedding`, `get_related_topics` and `get_related_topics_for_all`. Representational form: distributed-parametric weights; substrate: external downloaded model and CPU/GPU memory. The inspected helpers encode text without a training update. Exact weights are not pinned to an immutable model revision. No HTTP serving endpoint is used here; upstream identifier resolution can change downloaded weights. WordNet's helper instead accepts an arbitrary caller-supplied `embedder`, whose identity and initialization are unresolved. This prevents asserting one shared embedding space for every exposed helper (SRC-1, `uncertainty/topic_generator.py`).

Distinct from all five supplied runtime model components: this model supplies numerical topic representations, not generation, NLI classification or judging. Closest context is [RT-RTE-data-generation](runtime.md#rt-rte-data-generation); the active predefined-topic branch does not call this embedder.

> def get_embedding(topic_list,embedding_path,truncate=False):
>     embedder = SentenceTransformer("sentence-transformers/all-MiniLM-L12-v2", device="cuda")
> --- `uncertainty/topic_generator.py`

### Operative objects

#### MEM-OBJ-topic-docu
Label: Accepted title-to-document cache

Source-native identity: `topic2docu` serialized at `data/embeddings/accepted_topic_doc.pkl`. Storage: local pickle file; content form: natural-language article text, with symbolic title keys used for exact lookup. This is imported source content, not a model-experience trace or a vector store despite the directory name. The producer loads configured Wikipedia training data and retains articles above 512 whitespace words. On reuse it trusts the existing pickle. `get_predefined_topics` selects titles from shipped lists, removes reference/see-also tail sections, then generation chunks the selected documents. The model receives chunk text, not the complete cached corpus. No immutable per-document source ID or content-refresh policy is written with the mapping (SRC-1, `uncertainty/wiki_generation.py`, `uncertainty/topic_generator.py`, `configs/data/wiki.yaml`).

Distinct retained object, not a duplicate of the procedural [RT-RTE-data-generation](runtime.md#rt-rte-data-generation); runtime declares no operative objects.

> if len(d['text'].split()) > 512:
>     topic2docu[d['title']] = d['text']
> --- `uncertainty/wiki_generation.py`

#### MEM-OBJ-questions
Label: Persisted generation questions

Source-native identity: `question_path`, default `data/wiki/questions.jsonl`. Local JSONL; natural-language instruction/document fields plus symbolic topic/category fields. Model-authored questions derive from selected document chunks and three sampled shipped examples. Code admits a question through lexical checks, a local duplicate set and up to three attempts; file existence later bypasses generation. The file retains question, chunk, topic and category, not the provider conversation or why a question passed checks. Reused questions feed answer generation. Context-label successes can be excluded from the remaining question list without deleting them from this file (SRC-1, `uncertainty/wiki_generation.py`, `uncertainty/utils.py`, `configs/model/tinyllama.yaml`). Distinct artifact produced by [RT-RTE-data-generation](runtime.md#rt-rte-data-generation).

> print ('Questions already existed, skipping question generating....')
> with open(question_path,'r') as f:
>     unique_qns = [json.loads(l) for l in f]
> --- `uncertainty/wiki_generation.py`

#### MEM-OBJ-context-answer
Label: Context-conditioned auxiliary SFT labels

Source-native identity: `context_ans` / `context_answer_path`, default `data/wiki/context_answer.jsonl`. Local JSONL; natural-language question/document/answer plus symbolic topic/category. In self SFT generation with reference-as-chosen, a shuffled third of questions is proposed to the OpenAI answer helper with documents. `None` results are excluded and successful questions removed from the other label stream; existing context labels reconstruct that exclusion. Training reloads the file, embeds its document in the instruction and concatenates it with ordinary SFT data. This has a different acquisition and consumer transformation from the self-model label file, so it is separate from [MEM-OBJ-answer-content](#mem-obj-answer-content). Both relate to [RT-RTE-data-generation](runtime.md#rt-rte-data-generation) and [RT-RTE-model-training](runtime.md#rt-rte-model-training), not duplicate route identities. No human approval of each label is requested (SRC-1, `uncertainty/wiki_generation.py`, `uncertainty/train.py`).

> context_success_qn = set([c['instruction'] for c in context_ans])
> unique_qns = [q for q in unique_qns if q['instruction'] not in context_success_qn]
> --- `uncertainty/wiki_generation.py:365-367`

#### MEM-OBJ-test
Label: Held-out question and reference-response file

Source-native identity: `test_ds` at configured `test_dataset_path`, ordinarily `data/wiki/test.jsonl`. Local JSONL; natural-language question, document chunk and optional `greedy_response`, with symbolic category/topic. GPT-4 proposes test questions; GPT-3.5 proposes greedy responses from question-only input. Code writes successful answer records, checks file count and first-record answer presence on reuse. This is generated evaluation material, not certified answers. Fresh empty-list indexing prevents an unconditional initialization account; see supplied [RT-RTE-data-generation](runtime.md#rt-rte-data-generation). Later response generation reads questions, RAG also reads documents, judging reads documents, and evaluation's `oracle` mode reads the generated response. These differ in authority: inference context versus ranking reference versus comparison answer (SRC-1, `uncertainty/wiki_generation.py`, `uncertainty/generate_response.py`, `uncertainty/pairwise_eval.py`). Distinct object spanning generation and evaluation, not part of exactly one supplied route.

> qn_msg = [{'role':'user','content':tp['instruction']}]
> test_ans,cost = openai_call(question_model,
>                         qn_msg,
>                         max_tokens=gen_kwargs['gold_answer']['max_new_tokens'],
>                         temperature=0.)
> --- `uncertainty/wiki_generation.py`

#### MEM-OBJ-answer-content
Label: Retained reference and sampled answer content

Source-native identity: `gold_ans_content` and answer-file `ans_dict` text-bearing fields, especially `gold_answer`, `gold_answer_sample` and `raw_answer_sample`. Substrate: SFT/DPO pickle files; GPT label alternatives use `data/wiki/{gpt_model}_answers.jsonl`. Form: natural-language answers and documents, symbolic field structure; generated-output objects may also contain token/log-probability details. Those payload details are not equivalent to the extracted `generated_text` display. The source shows how consumers extract text, not supplied bytes proving a particular pickle representation.

Lineage: cleaned self-model labels or OpenAI labels; DPO document-conditioned references plus context-free raw samples. Text cleanup may trim an incomplete last sentence or reject duplicated/empty/unhelpful answers. For non-self answer generators, another answer file can supply `raw_answer_sample` by exact instruction matching. This is reused model output, not newly sampled evidence; unmatched target questions disappear in `map_list_of_dicts`. An existing main answer file is reloaded and rescored, not necessarily regenerated. SFT consumes labels; DPO consumes selected chosen/rejected text. See [RT-RTE-data-generation](runtime.md#rt-rte-data-generation) and [RT-RTE-model-training](runtime.md#rt-rte-model-training), which are procedures rather than these objects (SRC-1, `uncertainty/wiki_generation.py`, `uncertainty/data_utils.py`, `uncertainty/utils.py`, `uncertainty/scorer.py`).

> source_map = {s[compare_key]:s[map_key] for s in source}
> new_target = []
> for t in target:
>     t_key_value = t[compare_key]
>     if t_key_value in source_map:
>         t[map_key] = source_map[t_key_value]
>         new_target.append(t)
> return new_target
> --- `uncertainty/data_utils.py`

#### MEM-OBJ-answer-scores
Label: Stored question and answer selection scores

Source-native identity: `question_hallucination`, `gold_answer_scores`, `hallucination`, `all_hallu_scores`, and alternate `confidence`, `self_reflect_score`, `consistency_score`, `all_nli_scores`, `entropy`, `semantic_clusters`, `all_cluster_entropies`. Storage: fields in local answer pickle records. Form: symbolic numeric scores/arrays, cluster membership and lookup structure; clustered answer text remains natural language. NLI weights are a separate distributed-parametric component, [RT-CMP-nli-model](runtime.md#rt-cmp-nli-model). These scores are derived memory rather than raw output traces. The question-quality transformation renames its score to distinguish it from subsequent raw-answer scoring. The final merge preserves answer fields and derived scores, then overwrites the answer file (SRC-1, `uncertainty/wiki_generation.py`, `uncertainty/scorer.py`).

At the training consumer, scores control question eligibility and chosen/rejected selection. They are not factual proof or formulated criticisms. Actual DPO trainer input contains only formatted prompt/chosen/rejected, so score lineage and documents are not supplied as reasons to optimization. The durable weights likewise have no inspected reason-retrieval interface. Scores remain inspectable in the source dataset if it survives overwrites; a checkpoint does not certify their provenance. Distinct part from text content above: same file, different consumer authority and transformation. Closest supplied account is [RT-RTE-model-training](runtime.md#rt-rte-model-training); no supplied operative-object counterpart.

> question_key = 'question_hallucination'
> for q in scored_qns:
>     q[question_key] = q.pop(score_key) # change to new key to not confuse with answer hallucination later.
> --- `uncertainty/wiki_generation.py`

> return HFDataset.from_dict({
>     'prompt': prompt,
>     'chosen': chosen,
>     'rejected': rejected,
> })
> --- `uncertainty/self_learning_training.py`

#### MEM-OBJ-known
Label: Persisted known-question evaluation subset

Source-native identity: `knwn_ds_path`, `data/wiki/{model_name}_known.jsonl`. Storage: local JSONL; natural-language instruction/document plus symbolic category. On first request, code selects SelfCheckGPT `known` records at threshold 0.5 from self DPO answers, shuffles and caps at 200, then strips answers/scores. Later requests reuse the file so comparisons can share the subset. It is not a query-specific retrieval index or independently verified knowledge inventory. It supplies questions to response generation and documents to the evaluator, not selection reasons (SRC-1, `uncertainty/generate_response.py`, `uncertainty/pairwise_eval.py`, `uncertainty/utils.py`). Distinct object retained by [RT-RTE-response-generation](runtime.md#rt-rte-response-generation).

> test_ds = return_question_type(test_ds,'SelfCheckGPT','known',0.5) # return known
> random.shuffle(test_ds)
> test_ds = test_ds[:200]
> test_ds = [{'instruction':x['instruction'],'category':x['category'],'document':x['document']} for x in test_ds]
> --- `uncertainty/generate_response.py`

#### MEM-OBJ-responses
Label: Saved model responses for later comparison

Source-native identity: `response_list` at derived `response_path`. Local JSONL; natural-language instruction and `greedy_response`. These are generated-output traces, not a derived instruction store. Ordinary response generation has sampled outputs disabled. Each invocation overwrites the derived response path; the file does not record a weight digest or endpoint attestation. Pairwise evaluation joins response files by exact instruction, not semantic similarity; `oracle` substitutes test-file responses. This artifact has comparison-input authority, not automatic checkpoint-admission authority. Distinct from [MEM-OBJ-test](#mem-obj-test) because producer, overwrite path and consumer role differ. It spans [RT-RTE-response-generation](runtime.md#rt-rte-response-generation) and [RT-RTE-pairwise-evaluation](runtime.md#rt-rte-pairwise-evaluation) (SRC-1, `uncertainty/generate_response.py`, `uncertainty/pairwise_eval.py`).

> with open(response_path,'w') as f:
>     for response in response_list:
>         f.write(json.dumps(response)+'\n')
> --- `uncertainty/generate_response.py`

#### MEM-OBJ-judge-cache
Label: Reloadable pairwise outcome cache

Source-native identity: `LLMJudge.cache`, persisted in `llm_judge_cache/{engine}.pkl`. Local pickle; symbolic mapping from full first-order formatted user-message text to `win`, `lose` or `tie`. The key contains question, document and response text; it is content identity, not access-frequency metadata. It excludes the system prompt, provider weight revision and timestamp. Values are derived from two parsed model choices, not retained judge reasons or full provider replies. Cache construction reloads the file; evaluation uses exact prompt-key hits to bypass new calls. Valid new results update and save it; failed results are omitted rather than cached as defeats. No automatic TTL or withdrawal of stale entries is implemented in these methods (SRC-1, `uncertainty/scorer.py`). Distinct retained object within the supplied [RT-RTE-pairwise-evaluation](runtime.md#rt-rte-pairwise-evaluation) account, not a duplicate route.

> if eval_prompt[0][-1]['content'] not in self.cache:
>     all_messages.append({'message':eval_prompt,'correct_order':correct_order,'wrong_order':wrong_order,'instruction':instruction})
> else:
>     results.append(self.cache[eval_prompt[0][-1]['content']])
> --- `uncertainty/scorer.py`

#### MEM-OBJ-results
Label: Appended aggregate evaluation results

Source-native identity: `config.result_path` under `test_results/`. Local text file; natural-language labels with symbolic numerical aggregates. The evaluator derives win/tie/lose proportions from counted outcomes, writes cost/no-count and generation-length statistics, and writes disabled-hallucination placeholders as zeros. It appends rather than replacing previous aggregates. These are terminal reports in the inspected drivers; a later human reader is possible, but no actual human decision or automatic trainer consumer is supplied. Distinct from per-comparison cache and response traces; closest supplied route is [RT-RTE-pairwise-evaluation](runtime.md#rt-rte-pairwise-evaluation), whose evidence includes the disabled scoring branch (SRC-1, `uncertainty/pairwise_eval.py`).

> with open(config.result_path,'a') as f:
>     f.write(f'\n************ Base model: {base_model_name}, Eval model: {eval_model_name}{path_flag} ************\n')
> --- `uncertainty/pairwise_eval.py`

#### MEM-OBJ-topic-caches
Label: Alternative topic-helper retained parts

Source-native identity and split parts (SRC-1, `uncertainty/topic_generator.py`):

| Part | Substrate and form | Lineage, control and consumer | Limits |
|---|---|---|---|
| `wordnet_data.pkl`: `all_nouns` | Local pickle; natural-language noun/definition strings | WordNet synsets → deduplicated strings; helper reloads or builds; generic caller receives mapping | Caller-supplied embedder and later downstream caller unresolved; storage capability, not wired workflow retrieval. |
| `wordnet_data.pkl`: `all_embeddings` | Same pickle; distributed-parametric dense numerical representation | Supplied embedder encodes noun strings; no in-helper training | Initial model identity and revision unknown; text is not a complete readable rendering of vectors. |
| `wikiviews.pkl` | Local pickle; symbolic article-to-average-view counts | Wikimedia daily responses aggregated by `get_top_articles`; later helper calls reload | Counts rank popularity, not correctness; live API evidence not acquired. |
| `wiki_embeddings.pkl` / arbitrary `embedding_path` | Local pickle; distributed-parametric vectors with separate symbolic topic alignment; `get_embedding` initially saves a dictionary | Topic strings → SentenceTransformer → inner-product index in related-topic helpers | `get_top_articles` overwrites its generated embedding dictionary with the array; reconstruction depends on topic order. Length assertion cannot prove semantic alignment. |
| `category_topics_{num_topics}.pkl` | Local pickle; symbolic category/title lists | Nearest-topic selection from views-intersected titles; cache reloaded by helper | Not called by active `get_wiki`; FAISS symbol unresolved with commented import. |
| `train_test_topics.pkl` | Local pickle; symbolic train/test topic lists | Random eligible article split; subsequent helper calls reuse file | Fixed path omits current topic counts/config; no enforced invalidation or provenance match. |

These are separate operative parts because their forms, admission and consumers differ. They are grouped only as an explicit inventory of an inactive alternative family, not asserted to share a lifecycle. Model-derived vectors can select topic identities but are not model-readable prose. Exposed helper selection uses query-topic embeddings and a nearest-neighbor count, not foreground-agent demand or push injection. Physical writes and selection are software-controlled; no per-item human review is requested. Their initialization depends on external datasets/services or a supplied embedder. No evidence establishes a deployed caller outside the inspected workflow. This family is distinct from the actual title/document cache [MEM-OBJ-topic-docu](#mem-obj-topic-docu) and the predefined-topic [RT-RTE-data-generation](runtime.md#rt-rte-data-generation) route.

> # selected_topics,topic2docu,test_topics = get_top_articles(num_topics,topic2docu,num_test_topics)
> selected_topics,topic2docu,test_topics = get_predefined_topics(num_topics,topic2docu,num_test_topics,existing_test_topics)
> --- `uncertainty/data_utils.py`

### Routes

none declared in this member

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-CMP-causal-model](runtime.md#rt-cmp-causal-model)

Memory-specific lineage: retained generated answers → software-selected labels/preferences → SFT/DPO optimization → saved weights, optionally adapter then merged model. Parameters have distributed-parametric form; disk directory and live model memory are substrates. The checkpoint is a derived behavior-shaping result, not a readable summary of experience. Exact dataset/score reasons do not survive as trainer input metadata in the DPO conversion quoted under [MEM-OBJ-answer-scores](#mem-obj-answer-scores). Later answer generation consumes the weights; there is no inspected rationale read-back from them. Consumer authority is numerical generation, distinct from the scoring rules' authority over training admission (SRC-1, `uncertainty/self_learning_training.py`, `uncertainty/train.py`, `uncertainty/generate_response.py`). Fixity and TGI uncertainty remain as declared in runtime.

#### On [RT-RTE-data-generation](runtime.md#rt-rte-data-generation)

Write agency: models author questions and answers, Python performs physical writes and admits results through lexical tests, cleanup and scoring success. Starting the workflow is not human approval of its individual contents. Existing artifact initialization is not authenticated; known later operations include answer reload, text extraction, score replacement and cross-generator remapping. Raw model outputs and derived scores are split in [MEM-OBJ-answer-content](#mem-obj-answer-content) and [MEM-OBJ-answer-scores](#mem-obj-answer-scores). File presence is a selector input, not evidence of freshness or source trust (SRC-1, `uncertainty/wiki_generation.py`).

Context control: code constructs separate question/answer/NLI calls. It retains article header text while forming bounded chunks, skips sentences longer than the chunk target, and caps chunk count; a sentence plus header can exceed the nominal target, so 512 is not a proven universal full-prompt budget. Question calls add three randomly selected shipped examples; base labels use up to ten; DPO uses no examples. Document omission is consumer-specific as runtime establishes. NLI sentence/reference pairs truncate at 512 tokens. Only generated/scored returns escape each thread-call frame; no removed conversation turns or summary checkpoint is later restored by this mechanism. Original documents remain on disk, but reachability requires the explicit file/topic route, not a model-followable context pointer (SRC-1, `uncertainty/data_utils.py`, `uncertainty/wiki_generation.py`, `uncertainty/scorer.py`).

> if length > max_length:
>     continue
> --- `uncertainty/data_utils.py`

#### On [RT-RTE-model-training](runtime.md#rt-rte-model-training)

Memory consumers: SFT label loader renames `gold_answer` to `answer`; ordinary SFT formatting keeps instruction/answer, not record documents. The auxiliary context stream explicitly embeds documents first. DPO uses stored selection scores and drops invalid pairs, optionally rejects large chosen/rejected length differences, then strips the result to prompt/chosen/rejected. These latter examples are current-run derived state; the saved parameter product is durable. Numeric rejection scores are not prose criticism (SRC-1, `uncertainty/train.py`, `uncertainty/data_utils.py`, `uncertainty/self_learning_training.py`).

The trace-fed update has mixed origin: imported Wikipedia plus shipped examples, generated questions/answers and NLI/provider-derived scores. Guidance is fixed code/prompts and configured optimization; neither source prompts nor selection methods are rewritten by training. The selector can reject individual examples; it does not require independently certified correct answers. Operating mode is an operator-selected bounded curriculum. Threshold bypass and forced reference choice remain as runtime declares. Improved future capacity is uninspected; parameter updating alone does not establish benefit (SRC-1, `uncertainty/train.py`, `uncertainty/scorer.py`).

Retention/recovery: configured overwriting and save limits govern checkpoints; optional non-last-only selection can load the best validation-loss model. PEFT merging destroys adapter-named files after loading the adapter and saving merged weights. That is artifact transformation and cleanup, not evaluation-driven withdrawal or guaranteed rollback. Trainer defaults include SFT sequence length 1024 and DPO prompt/total limits 128/512; actual truncation semantics belong to external trainer implementation (SRC-1, `configs/training/sft_trainer.yaml`, `configs/training/dpo_trainer.yaml`, `uncertainty/self_learning_training.py`).

> for os_file in os.listdir(saved_model_path): # remove the adapter files.
>     if Accelerator().is_main_process:
>         if 'adapter' in os_file:
>             os.remove(os.path.join(saved_model_path, os_file))
> merged_model.save_pretrained(saved_model_path)
> --- `uncertainty/self_learning_training.py`

#### On [RT-RTE-response-generation](runtime.md#rt-rte-response-generation)

Read-back direction: operator request → configured file/model selection → code loading/batching → explicit model input. No independently triggered unsolicited memory supply is evidenced. Selection targets model paths by flags, known/test files by mode and records by batch, not semantic relevance to a new user query. RAG supplies the current test record's retained document; ordinary SFT/DPO supplies instruction only; base adds the first five shipped examples, despite a category argument. The latter are static source, not accumulated memory. TGI's configured input/total-token ceilings are 3500/4096; they do not prove the client's prompts fit (SRC-1, `uncertainty/generate_response.py`, `script/tgi.sh`).

> def get_few_shot_instrs(category,max_few_shots=5):
>     return [{'instruction':format_answer(f['instruction'],base=True),'answer':f['answer']} for f in generation_examples[:max_few_shots]]
> --- `uncertainty/generate_response.py`

Known-subset answers and scores are discarded at subset persistence; selected instructions/documents survive. Saved response text is later comparison input, not an executable command or an autonomous memory-write instruction ([MEM-OBJ-known](#mem-obj-known), [MEM-OBJ-responses](#mem-obj-responses)). Weight selection and endpoint authority retain runtime's operator contract.

#### On [RT-RTE-pairwise-evaluation](runtime.md#rt-rte-pairwise-evaluation)

Cache read-back: the explicit evaluation request supplies question, document and response pair; code formats both orders, checks exact first-order user-message identity, and delivers cached outcome labels directly to aggregation. GPT-4o sees only uncached formatted comparisons, not the cache, dataset history or model weights. The cache's consumer treats a stored result as equivalent to a fresh result without rechecking the system prompt or provider revision. This is symbolic evaluation reuse, not natural-language memory injected into future answer generation. New replies get at most three attempts per order and three response tokens; only valid two-order results enter cache. Failures increase no-count and do not withdraw a checkpoint or remove an earlier training example (SRC-1, `uncertainty/scorer.py`, `uncertainty/pairwise_eval.py`).

Persisted cache labels omit replies, reasons and token usage; report aggregates lose per-instruction linkage. Appended results have no automatic training consumer in the inspected stages. An operator may interpret them, but that behavior is unobserved ([MEM-OBJ-judge-cache](#mem-obj-judge-cache), [MEM-OBJ-results](#mem-obj-results)).

## Write side

The implemented chain is imported documents → generated questions and raw/cleaned answers → stored scores → selected trainer examples → changed parameters → operator-selected inference. The operative parts above locate storage and lineage; annotations identify the different consumers and their authority. This is a trace-fed durable parameter update pathway, not mere log retention. The supplied runtime already bounds it as wired rather than exercised improvement ([RT-RTE-model-training](runtime.md#rt-rte-model-training), [RT-BAP-checkpoint-consumption](runtime.md#rt-bap-checkpoint-consumption)).

Acquisition and content admission differ. The operator selects dataset/model/flags; the Wikipedia cache admits by length; question generation admits by checks/retries; answer generation cleans or excludes failed values; scoring excludes exceptions/empty outputs; training applies threshold/pair rules; judge caching admits only parsed outcomes. All are code/model admission after launch, without per-content human approval. Mutable JSONL/pickle files can be supplied or replaced outside these producers, but the inspected code does not authenticate such edits or expose a review-and-approve protocol. Pickle loading uses host deserialization authority, not a content-safety boundary (SRC-1, `uncertainty/wiki_generation.py`, `uncertainty/train.py`, `uncertainty/scorer.py`).

Maintenance is mainly reuse, overwrite, omission and adapter cleanup. Rescoring can replace score fields and omit formerly retained records when scoring fails. Cross-generator mapping can omit unmatched questions. Training rejection need not delete the source record. Evaluation failure changes counted outcomes, not model admission. Checkpoint save limits and adapter merging differ from revoking a previously served model. There is no inspected propagation from an adverse judge outcome to automatic data retraction, checkpoint rollback or endpoint replacement in these four stage drivers (SRC-1, `uncertainty/wiki_generation.py`, `uncertainty/data_utils.py`, `uncertainty/train.py`, `uncertainty/self_learning_training.py`, `uncertainty/pairwise_eval.py`).

Raw text and derivation metadata can survive together in answer pickle files, but selected DPO examples and saved weights do not retain inspectable reasons for each preference. Alternative parameter checkpoints preserve numerical states, not summaries that can reconstruct deleted conversation turns. TensorBoard reporting/prints are diagnostics here; no inspected read-back turns them into future context or selection instructions (SRC-1, `uncertainty/self_learning_training.py`, `configs/training/sft_trainer.yaml`, `configs/training/dpo_trainer.yaml`).

## Read-back

| Retained material | Trigger and selector | Delivery and later consumer | Authority and budget |
|---|---|---|---|
| Accepted documents/questions/context labels/answer files | New generation invocation; existence checks, exact topic/instruction lookup, optional alternate-generator match | File loading into producer; selected chunks/text into individual model/scorer calls | Content guides questions/answers; scores control later admission. Chunk and example limits are above; no overall source-coverage guarantee. |
| Stored labels/scores | New training invocation; flags/thresholds/pair selector, with runtime's bypass cases | SFT text or DPO prompt/chosen/rejected dataset to trainer | Optimization reference, not factual certification; configured trainer lengths bound input subject to external implementation. |
| Saved model/adapters | New inference or generation invocation; configured path, or operator-selected server | Distributed-parametric weights to local loader/TGI | Numerical generation authority; no score/rationale retrieval. TGI identity is not client-enforced. |
| Test/known documents and questions | New response invocation; file-mode selection and batches | Instruction, optional record document, static examples into answer model | Natural-language influence only; ordinary SFT/DPO omits documents. |
| Responses/test reference answers | New pairwise-evaluation invocation; exact instruction join, optional `oracle` | Question/document/response pair into judge | Requested truthfulness/relevance ranking; no certified expected label. |
| Judge cache | Evaluation request; exact first-order formatted user-text match | Stored label straight to result aggregation | Fixed symbolic classification without fresh provider judgment; no TTL or revision match. |
| Alternative topic-helper caches | Explicit helper call; file existence, category or query topics and neighbor count | Arrays/title lists to helper caller or selection code | Numerical similarity/popularity can select topics; active stage wiring is not established. |

These routes are request-driven loading/selection. File identifiers prove addressing, not targeted relevance selection. The semantic helper does implement relevance selection over topic vectors, but has no demonstrated active workflow caller. No independent push route into a foreground conversation follows from its existence. Full documents and traces omitted from one call remain reachable only where a later explicit file-reading branch retains them; discarded sentence tails and dropped response reasons have no automatic reload route in the inspected functions (SRC-1, `uncertainty/topic_generator.py`, `uncertainty/wiki_generation.py`, `uncertainty/generate_response.py`, `uncertainty/scorer.py`).

## Integration issues

- **Additional concrete selection limitation, not a conflicting runtime identity:** [MEM-OBJ-answer-content](#mem-obj-answer-content) establishes that alternate-generator remapping silently keeps only instruction matches. `map_success` can become true after an empty successful mapping, so a completed mapping is not proof of complete question coverage. This qualifies the retained-data account in [RT-RTE-data-generation](runtime.md#rt-rte-data-generation) (SRC-1, `uncertainty/wiki_generation.py`, `uncertainty/data_utils.py`).
- **Question-filtered data-path mismatch:** generation adds `_qf` to `answer_path` when question filtering is enabled, but DPO training's question-filtering branch changes `path_flag`, not `dataset_path`. With unmodified TinyLlama config, those flags alone do not wire training to the generated `_qf` data file. A separately populated unsuffixed dataset or operator configuration edit is required. This supplements, rather than replaces, [RT-RTE-data-generation](runtime.md#rt-rte-data-generation) and [RT-RTE-model-training](runtime.md#rt-rte-model-training); it prevents assuming their similarly labeled paths share exact dataset lineage (SRC-1, `uncertainty/wiki_generation.py`, `uncertainty/train.py`, `configs/model/tinyllama.yaml`).

> if args.question_filtering:
>     model_name += '_qf'
>     answer_path= answer_path.replace('.pkl','_qf.pkl')
> --- `uncertainty/wiki_generation.py`

> dataset_path = config.dpo_answer_path.format(answer_generator=args.answer_generator)
> if args.question_filtering: # is referring to the sft model.
>     path_flag += '_qf'
> --- `uncertainty/train.py`

- **Alternative helper uncertainty:** [MEM-OBJ-topic-caches](#mem-obj-topic-caches) retains the unused FAISS dependency, caller-supplied WordNet embedder and embedding/topic-alignment limits. No active semantic-topic retrieval or benefit can be attributed to [RT-RTE-data-generation](runtime.md#rt-rte-data-generation) from these helpers. They are available source, not missing access (SRC-1, `uncertainty/topic_generator.py`, `uncertainty/data_utils.py`).
- **No duplicate declarations identified:** runtime declares model components, broad stage routes and one parameter-authority path; this report annotates those identities rather than redeclaring them. Its topic embedder and retained operative objects have no supplied identity counterpart. Epistemic/workflow peers were not supplied; possible overlap with their later object declarations cannot be resolved here.
- **Unresolved actual lineage/activation:** generated files, exact weight versions, TGI server selection and provider behavior were not supplied. Therefore [MEM-OBJ-answer-content](#mem-obj-answer-content), [MEM-OBJ-answer-scores](#mem-obj-answer-scores), [MEM-OBJ-judge-cache](#mem-obj-judge-cache) and [RT-BAP-checkpoint-consumption](runtime.md#rt-bap-checkpoint-consumption) support source-wired retention and authority, not exercised learning, checkpoint causality or measured factual improvement. No source-boundary change is needed to retain these limits.

## Limitations and checks

Source HEAD was rechecked as `97839b29d0fd8bb474f5549fa3e9d6ca504732e0`. Identity and scope were compared with the supplied boundary/runtime and local member/record contracts. No target code, examples, tests, service requests or model calls were executed. Inspection challenged turnkey reuse, semantic-retrieval labels, complete dataset matching, strict chunk budgets and path identity; counterexamples are retained beside their claims.

There is no evidence of exercised or beneficial parameter learning, served checkpoint identity, reliable provider judgments or complete source coverage within model windows. Available but unread example bodies and nonprimary configurations are not access gaps or absence evidence. External initial weights, datasets and provider state remain opaque at this boundary; implemented local transformations remain inspectable despite that opacity.

Deterministic validation: the required `commonplace-run validate-output` invocation passed the member content check. It reported that invocation residue was not checked. A form/quotation pass does not establish semantic correctness, claim support or job acceptance.
