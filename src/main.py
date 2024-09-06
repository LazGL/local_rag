from document_loader import load_documents_and_chunk
from indexer import create_embeddings_and_faiss_index
from generator import generate_response


def main():
    # Load and chunk documents
    print("Loading and chunking documents...")
    documents = load_documents_and_chunk("data/")
    
    # Create embeddings and FAISS index
    print("Creating embeddings and FAISS index...")
    vector_store = create_embeddings_and_faiss_index(documents)

    # User query
    user_query = input("Enter your question: ")
    
    # Search the vector store for relevant documents
    print("Searching for relevant documents...")
    search_results = vector_store.similarity_search(user_query, k=5)

    # Get the page content of the relevant documents
    retrieved_documents = [result.page_content for result in search_results]

    # Generate a response based on the retrieved documents
    print("Generating response...")
    response = generate_response(user_query, retrieved_documents)
    
    print("\nGenerated response:")
    print(response)

if __name__ == "__main__":
    main()