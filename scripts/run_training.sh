#!/bin/bash
# scripts/run_training.sh

# This script is a wrapper around the 'autotrain spacerunner' command
# to make it easier to launch training jobs on Hugging Face Spaces.

set -e

# --- Configuration ---
# Your Hugging Face username or organization name.
# Replace this with your actual username or organization.
HF_USERNAME="your-hf-username"

# The name for your training project on the Hub. This will be the name of the private space.
PROJECT_NAME="sheikh-llm-training-job"

# The path to your training project directory, relative to where this script is run.
# Assumes you run this from the root of the repo, e.g., `bash scripts/run_training.sh`
SCRIPT_PATH="./training"

# The Hugging Face backend to use for the training job.
# For free tier, use "spaces-cpu-basic". For GPUs, use "spaces-a10g-small", etc.
BACKEND="spaces-cpu-basic"

# --- Script ---

# Check for Hugging Face token
if [ -z "$HF_TOKEN" ]; then
    echo "❌ Error: HF_TOKEN environment variable is not set."
    echo "Please set your Hugging Face write token, e.g.:"
    echo "export HF_TOKEN='your_token_here'"
    exit 1
fi

echo "--- Launching AutoTrain SpaceRunner ---"
echo "Project Name: $PROJECT_NAME"
echo "Username:     $HF_USERNAME"
echo "Backend:      $BACKEND"
echo "Script Path:  $SCRIPT_PATH"
echo "---------------------------------------"

# Ensure autotrain-advanced is installed
if ! command -v autotrain &> /dev/null; then
    echo "autotrain-advanced not found. Installing..."
    pip install -q -U autotrain-advanced
fi

# Run the spacerunner command
autotrain spacerunner \
    --project-name "$PROJECT_NAME" \
    --script-path "$SCRIPT_PATH" \
    --username "$HF_USERNAME" \
    --token "$HF_TOKEN" \
    --backend "$BACKEND" \
    --args "push_to_hub" # Pass --push_to_hub as a store_true argument

echo ""
echo "✅ SpaceRunner job launched successfully."
echo "Monitor the progress at the URL provided in the output above."
