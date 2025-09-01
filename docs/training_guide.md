# Training Guide

This guide explains how to launch custom training jobs for the Sheikh LLM model using Hugging Face's AutoTrain SpaceRunner.

## Overview

We have integrated a workflow that allows you to launch a training job on a Hugging Face Space directly from this repository. This is useful for fine-tuning the model on your own data.

The core of this system is the `autotrain spacerunner` command, which packages up a project directory and runs a `script.py` file on a remote machine.

## Preparing Your Training Data

Before you can launch a training job, you need to prepare your dataset and upload it to the Hugging Face Hub. The training script in the `/training` directory is a template that expects to load a dataset from the Hub. You will need to modify `training/script.py` to point to your specific dataset.

## Launching a Training Job

There are two ways to launch a training job:

### 1. Using the Manual GitHub Workflow (Recommended)

This is the easiest way to start a training job.

1.  Navigate to the **Actions** tab of this repository.
2.  In the left sidebar, click on the **Manual AutoTrain Training Job** workflow.
3.  Click the **Run workflow** dropdown button.
4.  You can choose the `backend` (the type of machine to run on) and provide a unique `project_name` for the job.
5.  Click the green **Run workflow** button.

The workflow will start, and you can monitor its progress in the Actions tab. It will provide a link to the Hugging Face Space where the training is running.

### 2. Using the Local Script

You can also launch a training job from your local machine.

1.  **Set your Hugging Face Token**:
    Make sure your `HF_TOKEN` environment variable is set.
    ```bash
    export HF_TOKEN='your_hf_write_token'
    ```

2.  **Run the script**:
    Execute the `run_training.sh` script from the root of the repository.
    ```bash
    bash scripts/run_training.sh
    ```
    You can modify the script to change the project name, backend, etc.

## Customizing the Training

To customize the training process, you can edit the files in the `/training` directory:

-   **`training/script.py`**: This is the main training script. You can modify it to use your own dataset, change training arguments, and customize the model saving logic.
-   **`training/requirements.txt`**: Add any Python dependencies your training script needs.
