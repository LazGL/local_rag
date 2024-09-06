from transformers import pipeline
import torch

# Check if MPS is available and set the device accordingly
if torch.backends.mps.is_available():
    device = torch.device("mps")
    print("Using MPS backend")
else:
    device = torch.device("cpu")
    print("MPS not available. Using CPU instead.")

# Initialize the text-generation model and pass the device
generator = pipeline("text-generation", model="gpt2", device=device)

def generate_response(user_query, retrieved_documents):
    # Combine retrieved documents into a single context
    context = " ".join(retrieved_documents)
    
    # Generate a response 
    response = generator(
        f"Question: {user_query}\nContext: {context}", 
        max_new_tokens=50, 
        num_return_sequences=1, 
        truncation=True, 
        clean_up_tokenization_spaces=True
    )
    
    return response[0]['generated_text']