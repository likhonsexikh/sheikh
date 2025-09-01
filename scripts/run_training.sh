#!/bin/bash
# scripts/run_training.sh

# This script is a wrapper around the 'autotrain spacerunner' command
# to make it easier to launch fine-tuning jobs on Hugging Face Spaces.

set -e

# --- Configuration (can be overridden by environment variables) ---
# Your Hugging Face username or organization name.
# Example: export HF_USERNAME="my-user"
HF_USERNAME="${HF_USERNAME:-your-hf-username}"

# The name for your training project on the Hub.
# Example: export PROJECT_NAME="my-cool-finetune"
PROJECT_NAME="${PROJECT_NAME:-maverick-finetuning-job}"

# The path to your training project directory.
SCRIPT_PATH="${SCRIPT_PATH:-./maverick_finetuning}"

# The Hugging Face backend to use. Fine-tuning requires a GPU.
# 'spaces-a10g-small' is a good starting point.
# Example: export BACKEND="spaces-a10g-large"
BACKEND="${BACKEND:-spaces-a10g-small}"

# Any additional arguments to pass to the training script.
# All arguments passed to this script will be forwarded.
# Example: ./scripts/run_training.sh --epochs 3 --learning_rate 1e-5
EXTRA_ARGS="$@"

# --- Script ---

# Check for Hugging Face token
if [ -z "$HF_TOKEN" ]; then
    echo "❌ Error: HF_TOKEN environment variable is not set."
    echo "Please set your Hugging Face write token, e.g.:"
    echo "export HF_TOKEN='your_token_here'"
    exit 1
fi

echo "--- Launching AutoTrain SpaceRunner for Fine-Tuning ---"
echo "Project Name: $PROJECT_NAME"
echo "Username:     $HF_USERNAME"
echo "Backend:      $BACKEND"
echo "Script Path:  $SCRIPT_PATH"
echo "Extra Args:   $EXTRA_ARGS"
echo "---------------------------------------------------------"

# Ensure autotrain-advanced is installed
if ! command -v autotrain &> /dev/null; then
    echo "autotrain-advanced not found. Installing..."
    pip install -q -U autotrain-advanced
fi

# Convert extra args to the format autotrain expects (semicolon-separated key-value pairs)
# Example: --epochs 3 --foo bar -> epochs=3;foo=bar
AUTOTRAIN_ARGS=$(echo "$EXTRA_ARGS" | sed 's/--//g' | sed 's/ /=/g' | tr '\n' ';' | sed 's/ ;/;/g' | sed 's/;$//')

# Run the spacerunner command
autotrain spacerunner \
    --project-name "$PROJECT_NAME" \
    --script-path "$SCRIPT_PATH" \
    --username "$HF_USERNAME" \
    --token "$HF_TOKEN" \
    --backend "$BACKEND" \
    --args "$AUTOTRAIN_ARGS"

echo ""
echo "✅ SpaceRunner job launched successfully."
echo "Monitor the progress at the URL provided in the output above."
