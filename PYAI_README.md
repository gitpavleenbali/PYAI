# 🦜 PYAI - The Python AI Ecosystem

<div align="center">

**Building the Future of AI Development**

*An ecosystem of revolutionary Python libraries that make AI development as simple as it should be.*

[![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python&logoColor=white)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Made with ❤️](https://img.shields.io/badge/Made%20with-❤️-red.svg)](https://github.com/gitpavleenbali)

</div>

---

## 🌟 Vision

**PYAI** is an ecosystem of Python libraries designed to democratize AI development. Our mission is simple:

> *What SAS did for statistics, PYAI does for the GenAI era.*

We believe AI should be:
- **Simple** - One line to do complex tasks
- **Intuitive** - If you know Python, you know PYAI
- **Powerful** - Production-ready, not just demos
- **Accessible** - For everyone, not just ML engineers

---

## 📦 The Ecosystem

### 🐼 PyAgent
**The Pandas of AI Agents**

Build AI-powered applications in 3 lines or less.

```python
from pyagent import ask, agent, rag

# Ask anything
answer = ask("What is quantum computing?")

# Create expert agents
coder = agent(persona="coder")
code = coder("Write a fibonacci function")

# RAG in 2 lines
docs = rag.index(["doc1.pdf", "doc2.txt"])
answer = docs.ask("What is the main conclusion?")
```

**Features:**
- ✅ One-liner AI operations
- ✅ RAG in 2 lines (vs 50+ in other frameworks)
- ✅ Prebuilt agent personas
- ✅ Azure OpenAI + OpenAI + Anthropic support
- ✅ Full type hints

📚 [PyAgent Documentation →](./docs/QUICKSTART.md)

---

### 🔮 Coming Soon

| Library | Description | Status |
|---------|-------------|--------|
| **PyFlow** | Visual AI workflow builder | 🚧 Planned |
| **PyVision** | Computer vision made simple | 🚧 Planned |
| **PyVoice** | Speech & audio AI | 🚧 Planned |
| **PyData** | AI-powered data analysis | 🚧 Planned |

---

## 🚀 Quick Start

### Installation

```bash
# Install PyAgent
pip install pyagent

# Or with Azure support
pip install pyagent[azure]
```

### Configuration

```bash
# OpenAI
export OPENAI_API_KEY=sk-your-key

# Or Azure OpenAI
export AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
export AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
```

### Your First 3 Lines

```python
from pyagent import ask

answer = ask("Explain AI in simple terms")
print(answer)
```

---

## 🎯 Why PYAI?

### The Problem

Current AI frameworks are **too complex**:

```python
# Other frameworks: 50+ lines just for RAG
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

loader = TextLoader("document.txt")
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000)
texts = text_splitter.split_documents(documents)
embeddings = OpenAIEmbeddings()
db = Chroma.from_documents(texts, embeddings)
retriever = db.as_retriever()
qa = RetrievalQA.from_chain_type(llm=OpenAI(), retriever=retriever)
result = qa.run("What is the main point?")
# ... and this is the SHORT version!
```

### The PYAI Solution

```python
# PYAI: 2 lines
from pyagent import rag

answer = rag.ask("document.txt", "What is the main point?")
```

**That's it.** ✨

---

## 📊 Comparison

| Task | LangChain | LlamaIndex | AutoGen | **PYAI** |
|------|-----------|------------|---------|----------|
| Simple Q&A | 10+ lines | 8+ lines | 15+ lines | **1 line** |
| RAG Pipeline | 50+ lines | 30+ lines | 40+ lines | **2 lines** |
| Custom Agent | 25+ lines | 20+ lines | 35+ lines | **1 line** |
| Multi-turn Chat | 20+ lines | 15+ lines | 25+ lines | **3 lines** |
| Learning Curve | Steep | Moderate | Steep | **Flat** |

---

## 🏗️ Architecture

```
PYAI Ecosystem
├── pyagent/          # AI Agents & LLM Operations
│   ├── easy/         # Simple one-liner APIs
│   ├── core/         # Core components
│   ├── skills/       # Agent capabilities
│   ├── blueprint/    # Complex workflows
│   └── instructions/ # Prompt engineering
├── pyvision/         # Computer Vision (coming soon)
├── pyvoice/          # Speech & Audio (coming soon)
└── pyflow/           # Visual Workflows (coming soon)
```

---

## 🤝 Contributing

We welcome contributions! See [CONTRIBUTING.md](./docs/CONTRIBUTING.md) for guidelines.

### Development Setup

```bash
git clone https://github.com/gitpavleenbali/pyagent.git
cd pyagent
pip install -e ".[dev]"
```

---

## 📜 License

MIT License - see [LICENSE](./LICENSE) for details.

---

## 👤 Author

**Pavleen Bali**

- GitHub: [@gitpavleenbali](https://github.com/gitpavleenbali)
- Part of the PYAI Ecosystem

---

<div align="center">

**🦜 PYAI - Making AI Development Simple**

*Because AI shouldn't require a PhD.*

⭐ Star this repo if you find it useful!

</div>
