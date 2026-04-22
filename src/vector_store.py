from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
import os


def create_faiss_index(documents, index_path="data/faiss_index"):
    """
    Create and persist FAISS vector store from documents.
    """
    os.makedirs(index_path, exist_ok=True)

    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001"
    )

    vectorstore = FAISS.from_documents(documents, embeddings)
    vectorstore.save_local(index_path)

    return vectorstore
    