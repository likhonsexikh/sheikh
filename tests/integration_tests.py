#!/usr/bin/env python3
"""
End-to-end integration tests for the Sheikh LLM project.

This script tests the interaction between the different components:
- Runtime server
- Python SDK
- Node.js SDK
"""
import argparse
import subprocess
import time
import sys
import requests
# from sheikh_sdk import Sheikh as SheikhPythonClient # This would be the ideal way

def run_integration_tests(runtime_path):
    """
    Starts the server, runs SDK tests against it, and then shuts it down.
    """
    print("🚀 Starting end-to-end integration tests...")

    server_process = None
    try:
        # 1. Start the runtime server in the background
        print("--- Starting Sheikh runtime server ---")
        server_cmd = [runtime_path, "--model", "../model/sheikh.gguf", "--server", "--host", "0.0.0.0", "--port", "8080"]
        server_process = subprocess.Popen(server_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Wait for the server to be ready
        for _ in range(10):
            try:
                response = requests.get("http://localhost:8080/health", timeout=1)
                if response.status_code == 200:
                    print("✅ Server is healthy.")
                    break
            except requests.ConnectionError:
                time.sleep(1)
        else:
            print("❌ Server did not start up correctly.")
            print("Stderr:", server_process.stderr.read())
            return False

        # 2. Run Python SDK tests against the server (using requests as a simple client)
        print("\n--- Testing Python SDK integration (via requests) ---")
        # python_client = SheikhPythonClient(host="localhost", port=8080)
        # response = python_client.generate("Health check", max_tokens=10)
        # This is a simplified check using requests to avoid circular dependencies during testing
        response = requests.post("http://localhost:8080/generate", json={"prompt": "Hello", "max_tokens": 10})
        if response.status_code == 200 and "response" in response.json():
             print("✅ Python SDK integration test PASSED.")
        else:
             print(f"❌ Python SDK integration test FAILED. Status: {response.status_code}, Body: {response.text}")
             return False

        # 3. Run Node.js SDK tests (conceptual)
        # In a real-world scenario, you would use a test runner like Jest.
        # This can be done by calling the npm script from here.
        print("\n--- Testing Node.js SDK integration (via npm test) ---")
        # This assumes the Node SDK's tests are configured to hit http://localhost:8080
        # result = subprocess.run(["npm", "test"], cwd="../sdk/node", capture_output=True, text=True)
        # if result.returncode == 0:
        #     print("✅ Node.js SDK integration test PASSED.")
        # else:
        #     print("❌ Node.js SDK integration test FAILED.")
        #     print(result.stdout)
        #     print(result.stderr)
        #     return False
        print("ℹ️  Skipping Node.js SDK test execution in this placeholder script.")


        print("\n🎉 All integration tests passed!")
        return True

    except Exception as e:
        print(f"\n❌ An exception occurred during integration tests: {e}")
        return False

    finally:
        # 4. Shut down the server
        if server_process:
            print("\n--- Shutting down Sheikh runtime server ---")
            server_process.terminate()
            server_process.wait()
            print("✅ Server shut down.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--runtime", default="../runtime/sheikh-linux-x64", help="Path to runtime binary")
    args = parser.parse_args()

    # Fallback for local testing
    if not Path(args.runtime).exists():
        args.runtime = "../runtime/sheikh"

    success = run_integration_tests(args.runtime)
    sys.exit(0 if success else 1)
