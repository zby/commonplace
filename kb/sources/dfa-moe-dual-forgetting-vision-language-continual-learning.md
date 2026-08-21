---
source: https://github.com/RL-MIND/DFA-MoE
description: "Official DFA-MoE implementation and evaluation workflow distinguishing incremental-knowledge forgetting from erosion of a vision-language model's pre-trained zero-shot capability."
captured: 2026-08-21
capture: web-fetch
genre: code-repository
type: kb/sources/types/snapshot.md
---

# DFA-MoE: Tackling Dual Forgetting in Vision-Language Continual Learning

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-red.svg)](https://pytorch.org/)

Official PyTorch implementation of the paper "Don't Forget Why You Started: Tackling Dual Forgetting in Vision-Language Continual Learning" ICML2026.

## Abstract

Vision-Language Models (VLMs) are strong continual learners, but standard class-incremental learning often damages the pre-trained vision-language alignment that underpins zero-shot generalization. This repository studies that dual-forgetting problem from two perspectives: Incremental Knowledge Forgetting (IKF), which harms previously learned classes, and Pre-trained Knowledge Forgetting (PKF), which erodes the original zero-shot capabilities of the VLM. To address this issue, we implement the Dual-Forgetting-Aware Class-Incremental Learning (DFA-CIL) framework, the Similarity-Calibrated Retention (SCR) metric, and DFA-MoE, a functionally heterogeneous PEFT method that decouples alignment preservation from task adaptation.

![Introduction](docs/intro.png)

## Key Contributions

- Dual-forgetting evaluation for VLM continual learning through the DFA-CIL protocol.
- Similarity-Calibrated Retention (SCR) utilizing similarity based weight to disentangle genuine foundational retention from the confounding effects of positive transfer.
- DFA-MoE with two functional pathways:
  - Alignment Pathway: task-agnostic contrastive expert for PKF mitigation.
  - Plasticity Pathway: task-specific experts with classification and auxiliary contrastive learning for IKF mitigation.
  - Hierarchical routing with an inner router over task-specific experts and an outer router balancing alignment and plasticity outputs.

## Installation

### Setup Environment

```bash
git clone https://github.com/RL-MIND/DFA-MoE
cd DFA_MoE
pip install -r requirements.txt
```

## Supported Downstream Datasets

The current `configs/class` directory provides downstream class-incremental configs for the following dataset indices. These indices are the values used in `+train_dataset=[id]`.

- `0`: `FGVCAircraft`
- `1`: `Caltech101`
- `2`: `CIFAR100`
- `3`: `DescribableTextures`
- `4`: `EuroSAT`
- `5`: `OxfordFlowers`
- `6`: `Food101`
- `7`: `MNIST`
- `8`: `OxfordPets`
- `9`: `StanfordCars`
- `10`: `SUN397`
- `11`: `Country211`
- `14`: `GTSRB`
- `15`: `RESISC45`
- `16`: `FER2013`
- `17`: `UCF101`
- `18`: `CIFAR10`
- `19`: `STL10`
- `20`: `VOC2007`
- `21`: `ImageNetR`
- `22`: `KittiDistance`
- `24`: `CLEVRCount`

The datasets pool also contains:

- `12`: `SST2`
- `13`: `HatefulMemes`
- `23`: `PCam`

These datasets are not supported as `--downstream-dataset` for `calculate_sim.py` because they are binary classification datasets.

## Data Preparation

We will soon release all the datasets used in this work at [google drive](https://drive.google.com/drive/folders/1DxD6MixpyTcsLSv8Gah5V0Cp3yMupYZO?usp=sharing).

1. Download or prepare the datasets under a common `dataset_root`.
2. Update `dataset_root` in the command line when launching experiments.
3. Choose the dataset-specific config from `configs/class/`.

Example dataset config files:

- `configs/class/eurosat.yaml`
- `configs/class/flower.yaml`
- `configs/class/cifar100.yaml`
- `configs/class/aircraft.yaml`

## Quick Start

### Train a DFA-CIL Run

Example: EuroSAT with 5 class-incremental splits.

```bash
python main.py \
  --config-path ./configs/class \
  --config-name eurosat.yaml \
  dataset_root="/path/to/data" \
  +train_dataset=[4] \
  +cil_splits=[5]
```

Example: OxfordFlowers with 17 splits.

```bash
python main.py \
  --config-path ./configs/class \
  --config-name flower.yaml \
  dataset_root="/path/to/data" \
  +train_dataset=[5] \
  +cil_splits=[17]
```


## Important Configuration Options

This project uses Hydra-based configuration. Key parameters include:

```yaml
model_name: "ViT-B/16"
prompt_template: "a bad photo of a {}."

batch_size: 128
weight_decay: 0.0
ls: 0.0

epochs_a: 1
epochs_b: 1

lr_e1: 1.0e-5
lr_e2: 5.0e-4
text_lr_e2: 1.0e-5
lr_e2_router: 1.0e-3
lr_top_router: 1.0e-5

tau_con: 0.15
tau_b_con: 0.17
lambda_b_con: 0.001

num_task_experts: 2
e2_top_k: 2
moco_queue_size: 128
```

## Pre-task Zero-shot Baseline

To compute SCR correctly, the metric log must contain the original CLIP zero-shot baseline `A_k^0`. Enable this by setting:

```yaml
pre_task_zero_shot_eval: true
zero_shot_eval: true
```

or from the command line:

```bash
python main.py \
  --config-path ./configs/class \
  --config-name eurosat.yaml \
  dataset_root="/path/to/data" \
  +train_dataset=[4] \
  +cil_splits=[5] \
  pre_task_zero_shot_eval=true \
  zero_shot_eval=true
```

This writes a `task: -1` entry with `zs_pre` into `metrics.json`, which is required by `calculate_SCR.py`.

## SCR Evaluation Workflow

### Step 1: Run continual learning and save `metrics.json`

Run `main.py` with `pre_task_zero_shot_eval=true` and `zero_shot_eval=true`.

### Step 2: Generate the similarity matrix

Example: EuroSAT with 5 splits.

```bash
python calculate_sim.py \
  --dataset-root "/path/to/data" \
  --downstream-dataset EuroSAT \
  --cil-split 5 \
  --output eurosat_similarity.json
```

This script:

- uses the original frozen CLIP model,
- produces a task-to-upstream similarity matrix for SCR.

### Step 3: Compute SCR

```bash
python calculate_SCR.py \
  --metric-path /path/to/metrics.json \
  --sim-json /path/to/eurosat_similarity_sim.json
```

`calculate_SCR.py` now strictly requires:

- a `task: -1` row with non-empty `zs_pre`,
- per-task `zs` results in `metrics.json`,
- a similarity JSON generated by `calculate_sim.py`.

## Reference Script

The repository also contains `run.sh` as a reference batch script.

## Notes

- `main.py`, `calculate_sim.py`, and `calculate_SCR.py` are the recommended entry points for experiments and evaluation.

## Citation

If you find this repository useful in your research, please cite the paper:

```bibtex
@inproceedings{kang2026dont,
  title={Don't Forget Why You Started: Tackling Dual Forgetting in Vision-Language Continual Learning},
  author={Kang, Borui and Gu, Jinrui and Feng, Tao and Fan, Qi and Shi, Yinghuan and Wang, Lei and Li, Wenbin and Gao, Yang},
  booktitle={Proceedings of the 43rd International Conference on Machine Learning},
  year={2026}
}
```

## Acknowledgement

This repository is built upon and modified from [MoE-Adapters4CL](https://github.com/JiazuoYu/MoE-Adapters4CL). We thank the original authors for making their code publicly available.

The dataset processing pipeline in this repository is also based on [DIKI](https://github.com/lloongx/DIKI). We thank the authors for releasing their implementation.
