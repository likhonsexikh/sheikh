# maverick_model_example.py

# This script demonstrates how to use the meta-llama/Llama-4-Maverick-17B-128E-Instruct model
# for image-to-text tasks using the Hugging Face transformers library.
# Note: Running this script requires significant computational resources (GPU and RAM).

# --- Example 1: Using the pipeline helper ---
from transformers import pipeline
import torch

print("--- Running Example 1: Using pipeline ---")

# It's good practice to specify the device and data type
pipe = pipeline(
    "image-text-to-text",
    model="meta-llama/Llama-4-Maverick-17B-128E-Instruct",
    device_map="auto",
    torch_dtype=torch.float16
)

messages_pipe = [
    {
        "role": "user",
        "content": [
            {"type": "image", "url": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/p-blog/candy.JPG"},
            {"type": "text", "text": "What animal is on the candy?"}
        ]
    },
]
# The pipeline call should be `pipe(messages_pipe)` not `pipe(text=messages)`.
# This is a correction from the original prompt.
response_pipe = pipe(messages_pipe, max_new_tokens=40)
print(response_pipe)
print("-" * 20)


# --- Example 2: Using AutoProcessor and AutoModelForImageTextToText ---
from transformers import AutoProcessor, AutoModelForImageTextToText

print("\n--- Running Example 2: Using AutoProcessor and AutoModel ---")
processor = AutoProcessor.from_pretrained("meta-llama/Llama-4-Maverick-17B-128E-Instruct")
model = AutoModelForImageTextToText.from_pretrained(
    "meta-llama/Llama-4-Maverick-17B-128E-Instruct",
    device_map="auto",
    torch_dtype=torch.float16
)

messages_model = [
    {
        "role": "user",
        "content": [
            {"type": "image", "url": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/p-blog/candy.JPG"},
            {"type": "text", "text": "What animal is on the candy?"}
        ]
    },
]

inputs = processor.apply_chat_template(
	messages_model,
	add_generation_prompt=True,
	tokenize=True,
	return_dict=True,
	return_tensors="pt",
).to(model.device)

outputs = model.generate(**inputs, max_new_tokens=40)
# The decoding logic from the prompt was incomplete (`...and FROM...`).
# This is the corrected way to decode the output.
# We slice the output to remove the input tokens.
output_tokens = outputs[0][len(inputs["input_ids"][0]):]
decoded_output = processor.decode(output_tokens, skip_special_tokens=True)

print(decoded_output)
print("-" * 20)

print("\nExample script finished.")
