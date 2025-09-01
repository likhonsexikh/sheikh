#!/usr/bin/env python3
"""
Validates Sheikh model outputs for correctness and format compliance.
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path

def validate_model_outputs(model_path):
    """Run comprehensive model validation tests."""

    # Test cases for validation
    test_cases = [
        {
            "prompt": "Generate XML for a simple greeting",
            "expected_format": "xml",
            "validation": lambda x: x.startswith("<?xml") and "<greeting>" in x
        },
        {
            "prompt": "Create MDX component for a button",
            "expected_format": "mdx",
            "validation": lambda x: "export" in x and "Button" in x
        },
        {
            "prompt": "Write a simple function in Python",
            "expected_format": "code",
            "validation": lambda x: "def " in x and ":" in x
        }
    ]

    runtime_path = Path("../runtime/sheikh-linux-x64")
    if not runtime_path.exists():
        # Fallback for local testing if the cross-compiled binary doesn't exist
        runtime_path = Path("../runtime/sheikh")
        if not runtime_path.exists():
            print(f"❌ Runtime binary not found at {runtime_path} or ../runtime/sheikh-linux-x64")
            return False

    passed = 0
    total = len(test_cases)

    for i, test in enumerate(test_cases):
        print(f"\n🧪 Test {i+1}/{total}: {test['prompt'][:50]}...")

        try:
            # Run model with test prompt
            result = subprocess.run([
                str(runtime_path),
                "--model", str(model_path),
                "--prompt", test["prompt"],
                "--max-tokens", "200"
            ], capture_output=True, text=True, timeout=30)

            if result.returncode != 0:
                print(f"❌ Runtime error: {result.stderr}")
                continue

            output = result.stdout.strip()

            # Validate output format
            if test["validation"](output):
                print("✅ PASSED")
                passed += 1
            else:
                print(f"❌ FAILED - Output validation failed")
                print(f"Output: {output[:100]}...")

        except subprocess.TimeoutExpired:
            print("❌ FAILED - Timeout")
        except Exception as e:
            print(f"❌ FAILED - Exception: {e}")

    success_rate = passed / total
    print(f"\n📊 Results: {passed}/{total} tests passed ({success_rate:.1%})")

    if success_rate >= 0.8:  # 80% pass rate required
        print("✅ Model validation PASSED")
        return True
    else:
        print("❌ Model validation FAILED")
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="../model/sheikh.gguf", help="Path to model file")
    args = parser.parse_args()

    success = validate_model_outputs(args.model)
    sys.exit(0 if success else 1)
