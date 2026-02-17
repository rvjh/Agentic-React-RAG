# """
# Docstring for src.document_ingestion.document_processor

# DocumentProcessor is responsible for processing documents, including parsing, extracting metadata, and preparing the content for indexing or storage. It handles various document formats and ensures that the extracted information is structured and ready for further use in applications such as search engines, knowledge graphs, or content management systems.
# """

# from typing import List, Union
# from pathlib import Path
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain.schema import Document
# from langchain_community.document_loaders import(
#     WebBaseLoader,
#     PDFLoader,
#     TextLoader,
#     PyPDFDirectoryLoader,
# )

# class DocumentProcessor:
#     """
#     Docstring for DocumentProcessor

#     This class is responsible for processing documents, including parsing, extracting metadata, and preparing the content for indexing or storage. It handles various document formats and ensures that the extracted information is structured and ready for further use in applications such as search engines, knowledge graphs, or content management systems.
#     """
#     def __init__(self, chunk_size: int = 500, chunk_overlap: int = 100):
#         """ 
#         Initializes the DocumentProcessor with specified chunk size and overlap.

#         Args:
#             chunk_size (int): The size of each text chunk. Default is 500.
#             chunk_overlap (int): The number of overlapping characters between chunks. Default is 100.
#         """
#         self.chunk_size = chunk_size
#         self.chunk_overlap = chunk_overlap
#         self.text_splitter = RecursiveCharacterTextSplitter(chunk_size=self.chunk_size, chunk_overlap=self.chunk_overlap)

#     def load_from_url(self, url: str) -> List[Document]:
#         """
#         Loads a document from a URL.
        
#         Args:
#             url (str): The URL of the document to load.
#         Returns:
#             List[Document]: A list of Document objects containing the loaded content.
#         """
#         loader = WebBaseLoader(url)
#         documents = loader.load()
#         return documents
    
#     def load_from_pdf_dir(self, directory: Union[str, Path]) -> List[Document]:
#         """
#         Loads documents from a directory containing PDF files.
        
#         Args:
#             directory (Union[str, Path]): The path to the directory containing PDF files.
#         Returns:
#             List[Document]: A list of Document objects containing the loaded content.
#         """
#         loader = PyPDFDirectoryLoader(str(directory))
#         documents = loader.load()
#         return documents
    
#     def load_from_txt(self, file_path: Union[str, Path]) -> List[Document]:
#         """
#         Loads a document from a text file.
        
#         Args:
#             file_path (Union[str, Path]): The path to the text file.
#         Returns:
#             List[Document]: A list of Document objects containing the loaded content.
#         """
#         loader = TextLoader(str(file_path), encoding='utf-8')
#         documents = loader.load()
#         return documents
    
#     def load_from_pdf(self, file_path: Union[str, Path]) -> List[Document]:
#         """
#         Loads a document from a PDF file.
        
#         Args:
#             file_path (Union[str, Path]): The path to the PDF file.
#         Returns:
#             List[Document]: A list of Document objects containing the loaded content.
#         """
#         loader = PDFLoader(str(file_path))
#         documents = loader.load()
#         return documents
    
#     def load_documents(self, sources: List[str]) -> List[Document]:
#         """
#         Loads documents from a list of sources.
        
#         Args:
#             sources (List[str]): A list of source URLs or file paths.
#         Returns:
#             List[Document]: A list of Document objects containing the loaded content.
#         """
#         docs: List[Document] = []
#         for src in sources:
#             if src.startswith("http://") or src.startswith("https://"):
#                 docs.extend(self.load_from_url(src))
#             else:
#                 path = Path(src)

#                 if path.is_dir():
#                     docs.extend(self.load_from_pdf_dir(path))
#                 elif path.suffix.lower() == ".pdf":
#                     docs.extend(self.load_from_pdf(path))
#                 elif path.suffix.lower() == ".txt":
#                     docs.extend(self.load_from_txt(path))
#                 else:
#                     raise ValueError(f"Unsupported file format for source: {src}")
#         return docs

#     def split_documents(self, documents: List[Document]) -> List[Document]:
#         """
#         Splits a list of documents into smaller chunks.
#         Args:
#             documents (List[Document]): A list of Document objects to split.
#         Returns:
#             List[Document]: A list of Document objects containing the split content.
#         """
#         return self.text_splitter.split_documents(documents)
    
#     def process_url(self, urls: List[str]) -> List[Document]:
#         """
#         Processes documents from a list of URLs by loading and splitting them.
        
#         Args:
#             urls (List[str]): A list of URLs to process.
#         Returns:
#             List[Document]: A list of Document objects containing the processed content.
#         """
#         documents = self.load_documents(urls)
#         return self.split_documents(documents)
    


"""
Docstring for src.document_ingestion.document_processor

DocumentProcessor is responsible for processing documents, including parsing,
extracting metadata, and preparing the content for indexing or storage.
It handles various document formats and ensures that the extracted information
is structured and ready for further use in applications such as search engines,
knowledge graphs, or content management systems.
"""

from typing import List, Union
from pathlib import Path

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain_community.document_loaders import (
    WebBaseLoader,
    PyPDFLoader,      
    TextLoader,
    PyPDFDirectoryLoader,
)


class DocumentProcessor:
    """
    This class is responsible for processing documents, including parsing,
    extracting metadata, and preparing the content for indexing or storage.
    """

    def __init__(self, chunk_size: int = 500, chunk_overlap: int = 100):
        """
        Initializes the DocumentProcessor with specified chunk size and overlap.

        Args:
            chunk_size (int): The size of each text chunk.
            chunk_overlap (int): The number of overlapping characters between chunks.
        """
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap,
        )

    def load_from_url(self, url: str) -> List[Document]:
        """Load a document from a URL."""
        loader = WebBaseLoader(url)
        return loader.load()

    def load_from_pdf_dir(self, directory: Union[str, Path]) -> List[Document]:
        """Load all PDFs from a directory."""
        loader = PyPDFDirectoryLoader(str(directory))
        return loader.load()

    def load_from_txt(self, file_path: Union[str, Path]) -> List[Document]:
        """Load a text file."""
        loader = TextLoader(str(file_path), encoding="utf-8")
        return loader.load()

    def load_from_pdf(self, file_path: Union[str, Path]) -> List[Document]:
        """Load a single PDF file."""
        loader = PyPDFLoader(str(file_path))   # ✅ FIXED
        return loader.load()

    def load_documents(self, sources: List[str]) -> List[Document]:
        """
        Load documents from URLs, PDF files, TXT files, or directories of PDFs.
        """
        docs: List[Document] = []

        for src in sources:
            if src.startswith(("http://", "https://")):
                docs.extend(self.load_from_url(src))
                continue

            path = Path(src)

            if not path.exists():
                raise FileNotFoundError(f"Source not found: {src}")

            if path.is_dir():
                docs.extend(self.load_from_pdf_dir(path))
            elif path.suffix.lower() == ".pdf":
                docs.extend(self.load_from_pdf(path))
            elif path.suffix.lower() == ".txt":
                docs.extend(self.load_from_txt(path))
            else:
                raise ValueError(f"Unsupported file format for source: {src}")

        return docs

    def split_documents(self, documents: List[Document]) -> List[Document]:
        """Split documents into smaller chunks."""
        return self.text_splitter.split_documents(documents)

    def process_sources(self, sources: List[str]) -> List[Document]:
        """
        Load and split documents from mixed sources (URLs or file paths).
        """
        documents = self.load_documents(sources)
        return self.split_documents(documents)
