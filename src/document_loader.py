from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
import PyPDF2

def load_pdf(file_path):
    with open(file_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
    return text

def load_documents_and_chunk(directory):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500, chunk_overlap=100, separators=["."]
    )
    documents = []
    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            full_text = load_pdf(os.path.join(directory, filename))
            chunks = text_splitter.split_text(full_text)
            documents.extend(chunks)  # Split into chunks and extend the document list
    return documents