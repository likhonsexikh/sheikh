#!/bin/bash
set -e

if [ -z "$1" ]; then
    echo "Usage: $0 <path_to_runtime_binary>"
    exit 1
fi

RUNTIME_PATH="$1"
MODEL_PATH="../model/sheikh.gguf"

if [ ! -f "$MODEL_PATH" ]; then
    echo "❌ Model file not found at $MODEL_PATH"
    echo "Please ensure you are running this script from the 'tests/' directory or adjust the path."
    exit 1
fi

echo "🧪 Running runtime functionality tests on '$RUNTIME_PATH'..."

# Test 1: Basic execution
echo "Test 1: Basic model loading and execution"
output=$("$RUNTIME_PATH" --model "$MODEL_PATH" --prompt "Hello" --max-tokens 10)
if [ $? -eq 0 ]; then
    echo "✅ Basic execution test passed"
else
    echo "❌ Basic execution test failed"
    exit 1
fi

# Test 2: Streaming mode
echo "Test 2: Streaming mode"
"$RUNTIME_PATH" --model "$MODEL_PATH" --prompt "Count to 5" --stream --max-tokens 50 > /tmp/stream_output
if grep -q "1" /tmp/stream_output && grep -q "2" /tmp/stream_output; then
    echo "✅ Streaming test passed"
else
    echo "❌ Streaming test failed"
    exit 1
fi

# Test 3: JSON output mode
echo "Test 3: JSON output validation"
output=$("$RUNTIME_PATH" --model "$MODEL_PATH" --prompt "Generate JSON with name and age" --format json --max-tokens 100)
if echo "$output" | python -m json.tool > /dev/null; then
    echo "✅ JSON output test passed"
else
    echo "❌ JSON output test failed"
    exit 1
fi

# Test 4: Memory usage check (Linux only)
if command -v free &> /dev/null; then
    echo "Test 4: Memory usage validation"
    memory_before=$(free -m | awk 'NR==2{print $3}')
    "$RUNTIME_PATH" --model "$MODEL_PATH" --prompt "Generate a longer response about AI" --max-tokens 500 > /dev/null
    memory_after=$(free -m | awk 'NR==2{print $3}')
    memory_used=$((memory_after - memory_before))

    if [ $memory_used -lt 2000 ]; then  # Less than 2GB
        echo "✅ Memory usage test passed (${memory_used}MB used)"
    else
        echo "❌ Memory usage test failed (${memory_used}MB used)"
        exit 1
    fi
else
    echo "⚠️ Skipping memory usage test (command 'free' not found, this is normal if not on Linux)"
fi

echo "🎉 All runtime tests passed!"
