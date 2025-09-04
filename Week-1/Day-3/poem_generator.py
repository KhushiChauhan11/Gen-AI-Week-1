from transformers import pipeline

# Load a text generation model
generator = pipeline("text-generation", model="gpt2")

# Prompt
prompt = "Write a small poem about the ocean"

# Generate text
response = generator(prompt, max_length=50, num_return_sequences=1, pad_token_id=50256)

# Print the poem
print(response[0]["generated_text"])
