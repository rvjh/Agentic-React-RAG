"""
Docstring for src.nodes.react_node
This module defines the RAGNodes class, which is responsible for managing the nodes in a graph-based workflow. The RAGNodes class encapsulates the retriever and language model, providing methods to retrieve relevant documents and generate answers based on those documents. It serves as a central point for handling the interactions between the retriever and the language model within the graph structure.

"""

from typing import List, Optional
from src.state.rag_state import RagState

from langchain_core.documents import Document
from langchain_core.tools import Tool
from langchain_core.messages import HumanMessage
from langgraph.prebuilt import create_react_agent

## wiki tool
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.tools.wikipedia.tool import WikipediaQueryRun

class RAGNodes:
    """
    Docstring for RAGNodes
    This class is responsible for managing the nodes in a graph-based
    workflow. It encapsulates the retriever and language model, providing methods to retrieve relevant documents and generate answers based on those documents.
    """
    def __init__(self, retriever, llm):
        """
        Initializes the RAGNodes with a retriever and language model.
        """
        self.retriever = retriever
        self.llm = llm
        self.agent = create_react_agent(llm, [