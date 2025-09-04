# explain_rainbow.py
from transformers import pipeline
import torch

def main():
    prompt = "Explain how rainbows are formed"

    # choose device: GPU (cuda) if available, else CPU
    device = 0 if torch.cuda.is_available() else -1

    # model choice: "gpt2" is small and runs on CPU; swap for a larger model if you have GPU
    model_name = "gpt2"  

    generator = pipeline("text-generation", model=model_name, device=device)

    # generate text
    out = generator(
        prompt,
        max_new_tokens=150,   # how much text to generate
        do_sample=True,
        temperature=0.7,
        top_p=0.95,
        num_return_sequences=1,
        pad_token_id=50256    # avoids warning with gpt2
    )

    # print the generated text
    print("\n=== Prompt ===\n", prompt)
    print("\n=== Response ===\n", out[0]["generated_text"].strip())

if __name__ == "__main__":
    main()
