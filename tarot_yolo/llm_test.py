from llama_cpp import Llama
import json

llm = Llama(model_path="tarot_yolo/models/llama-2-7b.Q3_K_S.gguf")

output = llm(
      "What do tarot layout of cards cups-page, cups-knight mean?", # Prompt
      max_tokens=128, # Generate up to 32 tokens, set to None to generate up to the end of the context window
      #stop=["Q:", "\n"], # Stop generating just before the model would generate a new question
      echo=True # Echo the prompt back in the output
) # Generate a completion, can also call create_completion
print(json.dumps(output['choices']))