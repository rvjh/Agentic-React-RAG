"""
Docstring for vectorstore module in src.vectorstore.vectorstore
"""

from typing import List
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.schema import Document

class VectorStore:
    """
    Docstring for VectorStore

    This class is responsible for creating and managing vector stores for documents.
    It uses FAISS for vector storage and HuggingFaceEmbeddings for text embedding.
    """
    def __init__(self):
        """
        Docstring for __init__
        
        :param self: Description
        """
        self.embeddings = HuggingFaceEmbeddings()
        self.vector_store = None
        self.retriver = None

    def get_retriever(self, documents: List[Document]):
        """
        Docstring for get_retriever
        
        :param self: Description
        :param documents: List of Document objects to be used for creating the retriever
        :return: The retriever object created from the vector store
        """
        self.vector_store = FAISS.from_documents(documents, self.embeddings)
        self.retriever = self.vector_store.as_retriever()
        if self.retriver is None:
            raise ValueError("Retriever is not created successfully.")
        return self.retriever
    
    def retrieve(self, query: str, k: int = 4) -> List[Document]:
        """
        Docstring for retrieve
        
        :param self: Description
        :param query: The query string to retrieve relevant documents
        :param k: The number of documents to retrieve (default is 4)
        :return: A list of retrieved documents based on the query
        """
        if self.retriver is None:
            raise ValueError("Retriever is not created. Please call get_retriever() first.")
        return self.retriever.invoke(query)