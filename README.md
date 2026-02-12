<p align="center">
  <img src="https://img.shields.io/badge/PYAI-Intelligence%20Engine-blueviolet?style=for-the-badge&logo=python&logoColor=white" alt="PYAI"/>
</p>

<h1 align="center">🧠 PYAI</h1>
<h3 align="center">Three-Dimensional Intelligence Engine</h3>

<p align="center">
  <strong>The Intelligence Engine for Software Factories</strong><br/>
  <em>Build, Orchestrate, and Scale AI-Native Applications</em>
</p>

<p align="center">
  <a href="#-the-three-dimensions">Three Dimensions</a> •
  <a href="#-software-factories">Software Factories</a> •
  <a href="#-the-ecosystem">Ecosystem</a> •
  <a href="#-get-started">Get Started</a>
</p>

---

## 🎯 What is PYAI?

**PYAI is not just another AI library. It's an Intelligence Engine.**

While other frameworks help you *call* AI models, PYAI embeds intelligence *into* your software architecture. It's the foundation for building **Software Factories** — systems that don't just use AI, but think, adapt, and create.

> *"What SAS did for statistics, what pandas did for data, PYAI does for intelligence."*

---

## 🔺 The Three Dimensions

PYAI operates across **three dimensions of intelligence**, each building upon the last:

```
                    ┌─────────────────────────────────┐
                    │     DIMENSION 3: CREATION       │
                    │   Software Factory Intelligence  │
                    │ ┌─────────────────────────────┐ │
                    │ │ • Self-generating systems   │ │
                    │ │ • Code synthesis engines    │ │
                    │ │ • Autonomous development    │ │
                    │ └─────────────────────────────┘ │
                    └───────────────┬─────────────────┘
                                    │
                    ┌───────────────▼─────────────────┐
                    │    DIMENSION 2: ORCHESTRATION   │
                    │     Multi-Agent Intelligence     │
                    │ ┌─────────────────────────────┐ │
                    │ │ • Agent coordination        │ │
                    │ │ • Workflow automation       │ │
                    │ │ • Knowledge synthesis       │ │
                    │ └─────────────────────────────┘ │
                    └───────────────┬─────────────────┘
                                    │
                    ┌───────────────▼─────────────────┐
                    │     DIMENSION 1: COGNITION      │
                    │      Core AI Operations          │
                    │ ┌─────────────────────────────┐ │
                    │ │ • ask() • research()        │ │
                    │ │ • summarize() • analyze()   │ │
                    │ │ • extract() • generate()    │ │
                    │ └─────────────────────────────┘ │
                    └─────────────────────────────────┘
```

### Dimension 1️⃣ — Cognition
The foundation. Single-purpose AI operations that **just work**.

```python
from pyagent import ask, summarize, extract

# Instant intelligence
answer = ask("Explain quantum entanglement")
summary = summarize(long_document)
entities = extract(text, fields=["names", "dates", "amounts"])
```

### Dimension 2️⃣ — Orchestration
Coordinated intelligence. Multiple agents working in harmony.

```python
from pyagent import agent, workflow

# Specialized agents
researcher = agent(persona="researcher")
analyst = agent(persona="analyst")
writer = agent(persona="writer")

# Orchestrated workflow
report = workflow([
    researcher >> "Find latest AI trends",
    analyst >> "Analyze market impact",
    writer >> "Write executive summary"
])
```

### Dimension 3️⃣ — Creation
Self-generating systems. **The Software Factory.**

```python
from pyagent import factory

# The factory builds software
factory.create("Build a REST API for user management")
# → Generates models, routes, tests, documentation

factory.extend("Add authentication with JWT")
# → Intelligently extends existing codebase

factory.refactor("Convert to async architecture")
# → Transforms architecture while preserving logic
```

---

## 🏭 Software Factories

A **Software Factory** is a system that generates software, not just code snippets. PYAI provides the intelligence engine to build them.

### Traditional Development vs Software Factory

| Traditional | Software Factory |
|-------------|------------------|
| Write code manually | Describe what you need |
| Debug line by line | Self-healing systems |
| Copy-paste patterns | Intelligent pattern synthesis |
| Manual testing | Auto-generated test suites |
| Static architecture | Evolving, adaptive systems |

### The Intelligence Stack

```
┌──────────────────────────────────────────────────────────┐
│                    YOUR APPLICATION                       │
├──────────────────────────────────────────────────────────┤
│  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐     │
│  │ PyAgent │  │ PyFlow  │  │PyVision │  │ PyVoice │     │
│  │ Agents  │  │Workflow │  │ Vision  │  │  Audio  │     │
│  └────┬────┘  └────┬────┘  └────┬────┘  └────┬────┘     │
│       │            │            │            │           │
│  ┌────▼────────────▼────────────▼────────────▼────┐     │
│  │              PYAI INTELLIGENCE ENGINE           │     │
│  │  • Unified Memory  • Context Management         │     │
│  │  • Model Routing   • Intelligent Caching        │     │
│  └────────────────────────────────────────────────┘     │
├──────────────────────────────────────────────────────────┤
│         Azure OpenAI  |  OpenAI  |  Anthropic            │
└──────────────────────────────────────────────────────────┘
```

---

## 📦 The Ecosystem

### 🐼 PyAgent — *Available Now*
**The Pandas of AI Agents**

Build AI-powered applications in 3 lines or less. The most accessible AI agent framework ever created.

```python
from pyagent import ask, agent, rag

# One-liner AI
answer = ask("What is the meaning of life?")

# Expert agents
coder = agent(persona="coder")
solution = coder("Optimize this algorithm for O(log n)")

# RAG in 2 lines
knowledge = rag.index(["research/*.pdf"])
insight = knowledge.ask("What are the key findings?")
```

[📚 PyAgent Documentation](./docs/QUICKSTART.md) | [🚀 API Reference](./docs/API_REFERENCE.md)

#### Key Modules

| Module | Description |
|--------|-------------|
| **easy/** | One-liner functions: `ask()`, `research()`, `summarize()`, `generate()`, `translate()`, `extract()`, `code()` |
| **integrations/** | Connect to LangChain, Semantic Kernel, Azure AI Search, Pinecone, ChromaDB, FAISS, Qdrant |
| **orchestrator/** | Workflow management, task scheduling, multi-agent patterns (supervisor, consensus, debate) |
| **usecases/** | Pre-built templates: Customer Service, Sales, Development, Gaming, Telecom, Healthcare, Finance |
| **core/** | Agent engine, memory management, LLM abstraction |
| **skills/** | Extensible skill system for agent capabilities |

#### Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                          PyAgent                                 │
├─────────────────────────────────────────────────────────────────┤
│  ┌──────────────────────────────────────────────────────────┐  │
│  │                      easy/                                │  │
│  │  ask() chat() research() summarize() generate() code()   │  │
│  │  extract() analyze() translate() rag() handoff() mcp()   │  │
│  └──────────────────────────────────────────────────────────┘  │
├─────────────────────────────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐         │
│  │ integrations │  │ orchestrator │  │   usecases   │         │
│  │  LangChain   │  │   Workflow   │  │  Templates   │         │
│  │Semantic Kern │  │  Scheduler   │  │  Telecom     │         │
│  │ Vector DBs   │  │   Patterns   │  │  Finance     │         │
│  └──────────────┘  └──────────────┘  └──────────────┘         │
├─────────────────────────────────────────────────────────────────┤
│  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────────────┐   │
│  │  core   │  │ skills  │  │blueprint│  │  instructions   │   │
│  └─────────┘  └─────────┘  └─────────┘  └─────────────────┘   │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                            ▼
         ┌─────────────────────────────────────┐
         │    Azure OpenAI | OpenAI | Claude   │
         └─────────────────────────────────────┘
```

---

### 🔌 Integrations

Connect PyAgent to your existing AI ecosystem:

```python
from pyagent.integrations import langchain, semantic_kernel, vector_db

# Import LangChain tools
search = langchain.import_tool("serpapi")

# Create Semantic Kernel
kernel = semantic_kernel.create_kernel(provider="azure", deployment="gpt-4o")

# Connect to vector stores
store = vector_db.connect("azure_ai_search", endpoint="...", index="docs")
```

| Integration | Features |
|-------------|----------|
| **LangChain** | Import tools, chains, retrievers; Export agents |
| **Semantic Kernel** | Create kernels, import plugins, execute plans |
| **Azure AI Search** | Enterprise search with hybrid retrieval |
| **Pinecone** | Scalable cloud vector database |
| **ChromaDB** | Open-source embedding database |
| **FAISS** | Fast in-memory similarity search |
| **Qdrant** | High-performance vector search |

---

### 🎭 Multi-Agent Patterns

Enterprise-ready multi-agent orchestration:

```python
from pyagent.orchestrator import AgentPatterns
from pyagent import agent

# Supervisor pattern
result = AgentPatterns.supervisor(
    task="Write a research report",
    agents=[researcher, writer, editor],
    supervisor_instructions="Coordinate the team"
)

# Consensus pattern (voting)
decision = AgentPatterns.consensus(
    task="Should we approve this feature?",
    agents=[security_expert, ux_expert, perf_expert],
    threshold=0.66
)

# Debate pattern
verdict = AgentPatterns.debate(
    topic="AI open-source vs proprietary",
    pro_agent=advocate,
    con_agent=skeptic,
    judge=arbiter
)
```

---

### 📦 Ready-to-Use Templates

Pre-built agents for common scenarios:

```python
from pyagent.usecases import customer_service, development
from pyagent.usecases.industry import telecom, healthcare, finance

# Customer support
support = customer_service.support_agent(company_name="Acme Inc")

# Code review
reviewer = development.code_reviewer(languages=["Python", "JavaScript"])

# Industry-specific
plan_advisor = telecom.plan_advisor(carrier_name="MobileNet")
banking = finance.banking_assistant(bank_name="First Bank")
scheduler = healthcare.appointment_scheduler(facility="City Hospital")
```

---

### 🔮 Coming Soon

| Library | Purpose | Dimension |
|---------|---------|-----------|
| **PyFlow** | Visual AI workflow orchestration | 2 |
| **PyVision** | Computer vision made simple | 1 |
| **PyVoice** | Speech & audio intelligence | 1 |
| **PyFactory** | Software generation engine | 3 |
| **PyMind** | Autonomous reasoning systems | 3 |

---

## 🚀 Get Started

### Installation

```bash
# Basic install
pip install pyagent

# With OpenAI support
pip install pyagent[openai]

# With Azure support (recommended for enterprise)
pip install pyagent[azure]

# With LangChain integration
pip install pyagent[langchain]

# With Semantic Kernel integration
pip install pyagent[semantic-kernel]

# With vector database support
pip install pyagent[vector]

# Full installation (all features)
pip install pyagent[all]
```

### Installation Extras

| Extra | Includes |
|-------|----------|
| `openai` | OpenAI SDK |
| `anthropic` | Anthropic Claude SDK |
| `azure` | Azure Identity, AI Search, OpenAI |
| `langchain` | LangChain integration |
| `semantic-kernel` | Microsoft Semantic Kernel |
| `vector` | ChromaDB, FAISS, Pinecone, Qdrant |
| `web` | Web scraping (aiohttp, requests, beautifulsoup) |
| `docs` | Document processing (PDF, DOCX) |
| `all` | Everything above |
| `dev` | Development tools (pytest, black, mypy) |

### Configuration

```bash
# OpenAI
export OPENAI_API_KEY=sk-your-key

# Azure OpenAI (with Azure AD - recommended)
export AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
export AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
```

### Hello, Intelligence

```python
from pyagent import ask

# Your first intelligent operation
answer = ask("What makes PYAI revolutionary?")
print(answer)
# → "PYAI is revolutionary because it embeds intelligence into 
#    software architecture across three dimensions, enabling 
#    the creation of self-generating software factories..."
```

---

## 🧬 Design Philosophy

### 1. **Intelligence as Infrastructure**
AI shouldn't be bolted on — it should be woven in. PYAI treats intelligence as a first-class architectural component.

### 2. **Progressive Complexity**
Start with one line. Scale to software factories. Same API, same patterns, infinite scale.

```python
# Level 1: One line
answer = ask("Translate to French: Hello")

# Level 2: Agent
translator = agent(persona="translator", languages=["fr", "de", "es"])
result = translator("Translate to all languages: Hello")

# Level 3: Factory
factory.create("Build a multi-language translation service with API")
```

### 3. **Zero Friction**
No boilerplate. No ceremony. If it takes more than 3 lines for a common task, we failed.

### 4. **Production Ready**
Type hints. Error handling. Retry logic. Rate limiting. Caching. Built in, not bolted on.

---

## 🔥 Why PYAI?

| Other Frameworks | PYAI |
|-----------------|------|
| 50 lines for RAG | 2 lines |
| Agent = configuration hell | `agent(persona="coder")` |
| Memory = complex setup | Built-in, automatic |
| Workflows = YAML nightmares | Python functions |
| "Hello World" = 30 minutes | "Hello World" = 30 seconds |

---

## 🌍 The Vision

We're building the **operating system for intelligent software**.

```
2024: PyAgent launches → Simple AI operations
2025: PyFlow launches  → Orchestrated intelligence  
2026: PyFactory       → Software Factories emerge
2027: PyMind          → Autonomous development
2030: ???             → Software that writes itself
```

**This is not hype. This is the roadmap.**

---

## 👥 Community

- 📖 [Documentation](./docs/)
- 🐛 [Report Issues](https://github.com/gitpavleenbali/PYAI/issues)
- 💡 [Feature Requests](https://github.com/gitpavleenbali/PYAI/discussions)
- 🤝 [Contributing Guide](./docs/CONTRIBUTING.md)

---

## 📜 License

MIT License — Build freely, build boldly.

---

<p align="center">
  <strong>PYAI</strong><br/>
  <em>Intelligence, Embedded.</em>
</p>

<p align="center">
  <sub>Built with 🧠 by the PYAI team</sub>
</p>
