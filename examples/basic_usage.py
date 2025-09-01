# examples/basic_usage.py

from sheikh_sdk import Sheikh

def main():
    """
    A basic example of how to use the Sheikh Python SDK.
    """
    print("Loading Sheikh model...")
    # This assumes the SDK can load a local model or connect to a running instance.
    # The exact API may differ.
    try:
        model = Sheikh.load(model_path="../model/sheikh.gguf")

        prompt = "Generate a simple XML document for a book."
        print(f"Prompt: {prompt}")

        response = model.generate(prompt, max_tokens=100)

        print("\n--- Model Response ---")
        print(response)
        print("----------------------")

    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please ensure the model file exists and the runtime is correctly configured.")

if __name__ == "__main__":
    main()
