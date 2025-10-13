import torch
from transformers import pipeline

generator = pipeline(task="text-generation", model="openai-community/gpt", dtype=torch.float16, device=0)
output = generator("The future of AI is", max_length=50, do_sample=True)
print(output[0]["generated_text"])