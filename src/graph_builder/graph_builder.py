"""
Docstring for src.graph_builder.graph_builder

This module provides a function to build a graph from a list of documents.
The graph is represented as a dictionary where each key is a document ID and the value is a list of related document IDs.
"""

from typing import List, Dict
from pydantic import BaseModel
from langchain.schema import Document
from src.state.rag_state import RagState
from langchain_community.graphs import StateGraph
from langchain_community.graphs import END 
from src.nodes.nodes import RAGNodes

class GraphBuilder:
    """
    Docstring for GraphBuilder

    This class is responsible for building and managing the graph structure
    representing the relationships between documents and the RAG workflow.
    """
    def __init__(self, retriever, llm):
        """
        Initializes the GraphBuilder with a retriever and language model.
        """
        self.nodes = RAGNodes()
        self.graph = None

    def build(self):
        """
        Builds the graph based on the provided retriever and language model.
        """
        builder = StateGraph(RagState)

        builder.add_node("retriever", self.nodes.retrive_docs)
        builder.add_node("responder", self.nodes.generate_answer)

        ## entry point
        builder.set_entry_point("retriever")

        ## add edges
        builder.add_edge("retriever", "responder")
        builder.add_edge("responder", END)

        ## compile the graph
        self.graph = builder.compile()
        return self.graph
    
    def run(self, question: str)-> dict:
        """
        Runs the graph with the given question and returns the final state.

        :param question: The input question to be processed by the graph.
        :return: A dictionary containing the final state of the graph after execution.
        """
        if self.graph is None:
            raise ValueError("Graph is not built. Please call build() first.")
        
        initial_state = RagState(question=question)
        final_state = self.graph.invoke(initial_state)
        return final_state.dict()
    
    

