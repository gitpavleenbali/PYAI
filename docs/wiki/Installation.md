# Installation

Multiple installation options to fit your needs.

---

## Basic Installation

```bash
pip install pyagent
```

---

## With Specific Providers

### OpenAI
```bash
pip install pyagent[openai]
```

### Anthropic Claude
```bash
pip install pyagent[anthropic]
```

### Azure OpenAI (Recommended for Enterprise)
```bash
pip install pyagent[azure]
```

Includes:
- Azure Identity (Azure AD authentication)
- Azure AI Search integration
- OpenAI SDK for Azure

---

## With Integrations

### LangChain
```bash
pip install pyagent[langchain]
```

### Microsoft Semantic Kernel
```bash
pip install pyagent[semantic-kernel]
```

### Vector Databases
```bash
pip install pyagent[vector]
```

Includes: ChromaDB, FAISS, Pinecone, Qdrant

### Web & Documents
```bash
pip install pyagent[web]      # aiohttp, requests, beautifulsoup
pip install pyagent[docs]     # PDF, DOCX processing
```

---

## Full Installation

```bash
pip install pyagent[all]
```

Installs everything: all providers, integrations, and utilities.

---

## Development Installation

```bash
pip install pyagent[dev]
```

Includes: pytest, black, ruff, mypy, pre-commit

---

## Installation Extras Summary

| Extra | Packages Included |
|-------|-------------------|
| `openai` | OpenAI SDK |
| `anthropic` | Anthropic Claude SDK |
| `azure` | Azure Identity, AI Search, OpenAI |
| `langchain` | LangChain integration |
| `semantic-kernel` | Microsoft Semantic Kernel |
| `vector` | ChromaDB, FAISS, Pinecone, Qdrant |
| `web` | aiohttp, requests, beautifulsoup4 |
| `docs` | pypdf, python-docx |
| `all` | Everything above |
| `dev` | pytest, black, ruff, mypy |

---

## From Source

```bash
git clone https://github.com/gitpavleenbali/PYAI.git
cd PYAI
pip install -e ".[dev]"
```

---

## Verify Installation

```python
import pyagent
print(pyagent.__version__)  # 0.4.0
```

---

## Next Steps

- [[Configuration]] - Set up API keys
- [[Quick Start]] - Your first PYAI program
