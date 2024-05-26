# document_processing.py
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_and_split_document(file_path, chunk_size=5000, chunk_overlap=0):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    loader = TextLoader(text)
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    texts = text_splitter.split_documents(documents)
    return texts
