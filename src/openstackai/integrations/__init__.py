"""
openstackai Integrations Module
============================

Connect openstackai to the broader AI ecosystem. Adapters for popular frameworks,
vector databases, and external services.

Supported Integrations:
- LangChain: Use LangChain tools/chains within openstackai
- Semantic Kernel: Microsoft's AI orchestration framework
- LlamaIndex: Advanced RAG and indexing
- Vector Databases: Pinecone, Weaviate, Chroma, Qdrant, FAISS
- MCP Servers: External MCP tool servers
- OpenAI Plugins: OpenAI plugin ecosystem
- Hugging Face: Models and datasets

Usage:
    >>> from openstackai.integrations import langchain, semantic_kernel, vector_db

    # Use LangChain tools in openstackai
    >>> tool = langchain.import_tool("serpapi")
    >>> agent = openstackai.agent("researcher", tools=[tool])

    # Connect to vector database
    >>> store = vector_db.connect("pinecone", index="my-index")
    >>> rag = openstackai.rag.with_store(store)
"""

from typing import Any, Dict, List, Optional

# Import submodules for easy access
from openstackai.integrations import langchain_adapter as langchain
from openstackai.integrations import semantic_kernel_adapter as semantic_kernel
from openstackai.integrations import vector_db

__all__ = [
    "langchain",
    "semantic_kernel",
    "vector_db",
]
