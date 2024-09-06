from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

def create_embeddings_and_faiss_index(sentences):
    # Use Hugging Face model for embedding
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    
    # Create FAISS index from the text and embeddings
    vector_store = FAISS.from_texts(sentences, embeddings)
    
    return vector_store