"""
Docstring for src.nodes.nodes
This module defines the Nodes class, which is responsible for managing the nodes in a graph-based workflow. The Nodes class encapsulates the retriever and language model, providing methods to retrieve relevant documents and generate answers based on those documents. It serves as a central point for handling the interactions between the retriever and the language model within the graph structure.

"""

from src.state.rag_state import RagState

class RAGNodes:
    """
    Docstring for RAGNodes
    This class is responsible for managing the nodes in a graph-based workflow. It encapsulates the retriever and language model, providing methods to retrieve relevant documents and generate answers based on those documents.
    """
    def __init__(self, retriever, llm):
        """
        Initializes the RAGNodes with a retriever and language model.
        """
        self.retriever = retriever
        self.llm = llm

    def retrive_docs(self, state: RagState) -> RagState:
        """
        Docstring for retrive_docs

        :param self: Description
        :param state: RagState object
        :return: RagState object
        """

        docs = self.retriever.invoke(state.question)
        return RagState(
            question=state.question,
            retrived_docs=docs
        )
    
    def generate_answer(self, state: RagState) -> RagState:
        """
        Docstring for generate_answer

        :param self: Description
        :param state: RagState object
        :return: RagState object with generated answer
        """
        context = "\n\n".join([doc.page_content for doc in state.retrived_docs])
        prompt = f"Question: {state.question}\n\nContext: {context}\n\nAnswer:"
        answer = self.llm.invoke(prompt)
        return RagState(
            question=state.question,
            retrived_docs=state.retrived_docs,
            answer=answer
        )