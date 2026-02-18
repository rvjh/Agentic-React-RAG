"""
Docstring for src.state.rag_state

This module defines the RagState class, which is responsible for managing the state of a Retrieval-Augmented Generation (RAG) system. The RagState class encapsulates the retriever and the language model, allowing for efficient retrieval of relevant documents and generation of responses based on those documents. The class provides methods for retrieving relevant documents based on a query and generating responses using the language model. It also includes error handling to ensure that the retriever and language model are properly initialized before use.

"""

from typing import List
from pydantic import BaseModel
from langchain.schema import Document

class RagState(BaseModel):
    """
    Docstring for RagState
    This class is responsible for managing the state of a Retrieval-Augmented Generation (RAG) system.
    It encapsulates the retriever and the language model, allowing for efficient retrieval of relevant documents
    and generation of responses based on those documents.
    """
    question: str
    retrived_docs : List[Document] = []
    answer: str = ""
