# Fine-Tuning Guide

This guide explains how to launch custom fine-tuning jobs for models like `meta-llama/Llama-4-Maverick-17B-128E-Instruct` using this repository's integrated workflow with Hugging Face's AutoTrain SpaceRunner.

## Overview

We have set up a complete project for fine-tuning the Maverick model in the `/maverick_finetuning` directory. This includes a training script, a configuration file, and dependency management.

The system uses `autotrain spacerunner` to execute this fine-tuning project on a remote Hugging Face Space, which is ideal for long-running, GPU-intensive tasks.

## The Fine-Tuning Project (`/maverick_finetuning`)

-   **`script.py`**: The main training script. It's a template that handles loading the Maverick model, applying PEFT (LoRA) for efficient tuning, and using the `transformers` Trainer. **You must adapt this script to load your own dataset.**
-   **`config.json`**: Contains all the key hyperparameters for training, such as learning rate, batch size, and epochs. You can modify this file to experiment with different settings.
-   **`requirements.txt`**: Lists all the necessary Python packages for the fine-tuning job.

## Launching a Fine-Tuning Job

### Prerequisites

-   **A Hugging Face Account**: You need an account to use Spaces and the Hub.
-   **A Hugging Face Token**: You must have a Hugging Face User Access Token with `write` permissions. Set it as an environment variable:
    ```bash
    export HF_TOKEN='your_hf_write_token'
    ```
-   **A Fine-Tuning Dataset**: You must have a dataset suitable for the model, uploaded to the Hugging Face Hub. You will need to edit `maverick_finetuning/script.py` to point to your dataset.

### Option 1: Manual GitHub Workflow (Recommended)

1.  Navigate to the **Actions** tab of this repository.
2.  In the left sidebar, click on the **Manual AutoTrain Training Job** workflow.
3.  Click the **Run workflow** dropdown button.
4.  Choose a GPU-enabled `backend` (e.g., `spaces-a10g-small`).
5.  Provide a unique `project_name` for the job.
6.  Click **Run workflow**.

### Option 2: Local Script

You can also launch a job from your local machine using the helper script.

```bash
# Run with default settings
bash scripts/run_training.sh

# Override settings with environment variables
export BACKEND="spaces-a10g-large"
export PROJECT_NAME="my-awesome-finetune"
bash scripts/run_training.sh

# Pass extra arguments to the training script
bash scripts/run_training.sh --hf_hub_repo_id my-finetuned-model
```

---

## Automated Fine-Tuning Workflow

In addition to the manual methods, this repository is equipped with a fully automated fine-tuning workflow (`.github/workflows/automated_finetuning.yml`).

### Triggers

This workflow is automatically triggered by either of the following events:

1.  **A push to the `main` branch that includes changes inside the `/data` directory.** This allows you to trigger a new training run by simply updating your dataset.
2.  **A new version tag is pushed** (e.g., `v1.3.0`). This ensures that a new model is trained and validated as part of the release process.

### Process

When triggered, the workflow will:

1.  **Validate the dataset** (this is a placeholder step).
2.  **Launch an AutoTrain SpaceRunner job** using the settings in `scripts/run_training.sh`.
3.  **Send a notification** on success or failure (this is a placeholder step).

This automation ensures that your models are always kept up-to-date with your latest data and code, creating a true CI/CD for ML pipeline.
