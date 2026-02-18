<p align="center">
  <img src="https://img.shields.io/badge/openstackai-Intelligence%20Engine-blueviolet?style=for-the-badge&logo=python&logoColor=white" alt="openstackai"/>
</p>

<h1 align="center">🧠 openstackai</h1>
<h3 align="center">Three-Dimensional Intelligence Engine</h3>

<p align="center">
  <strong>The Intelligence Engine for Software Factories</strong><br/>
  <em>Build, Orchestrate, and Scale AI-Native Applications</em>
</p>

<p align="center">
  <a href="https://pypi.org/project/openstackai/"><img src="https://img.shields.io/pypi/v/openstackai" alt="PyPI"/></a>
  <a href="https://python.org/"><img src="https://img.shields.io/badge/python-3.10+-green" alt="Python"/></a>
  <a href="https://github.com/gitpavleenbali/PYAI"><img src="https://img.shields.io/badge/tests-671%20passing-brightgreen" alt="Tests"/></a>
  <a href="https://github.com/gitpavleenbali/PYAI/blob/master/LICENSE"><img src="https://img.shields.io/badge/license-MIT-yellow" alt="License"/></a>
  <a href="https://gitpavleenbali.github.io/PYAI/"><img src="https://img.shields.io/badge/docs-website-blue" alt="Documentation"/></a>
</p>

---

## 🚀 Quick Start

```bash
pip install openstackai
```

### One-Line AI Operations

```python
from openstackai import ask, summarize, research

# Ask anything
answer = ask("What is machine learning?")

# Summarize documents
summary = summarize("Long document text...")

# Research topics
report = research("Latest AI trends 2026")
```

### Build AI Agents

```python
from openstackai import Agent, Runner

agent = Agent(
    name="Assistant",
    instructions="You are a helpful AI assistant."
)

result = Runner.run_sync(agent, "Hello!")
print(result.final_output)
```

### Multi-Agent Workflows

```python
from openstackai import Agent, Runner
from openstackai.blueprint import ChainWorkflow

researcher = Agent(name="Researcher", instructions="Research topics")
writer = Agent(name="Writer", instructions="Write articles")

workflow = ChainWorkflow([researcher, writer])
result = Runner.run_sync(workflow, "AI in healthcare")
```

---

## ✨ Key Features

| Feature | Description |
|---------|-------------|
| **🎯 Simple APIs** | One-liner functions: `ask()`, `summarize()`, `research()`, `extract()`, `generate()` |
| **🤖 Agent Framework** | Full agent system with `Agent`, `Runner`, memory, and context passing |
| **🔗 Multi-Agent** | Orchestration patterns: Chain, Supervisor, Swarm, Tree of Thoughts |
| **🔌 Multi-Provider** | OpenAI, Azure OpenAI, Anthropic, Ollama, Gemini, Groq |
| **📊 Vector DBs** | ChromaDB, Pinecone, Qdrant, Weaviate integration |
| **🏢 Enterprise** | Azure AD auth, sessions, guardrails, evaluation, tracing |
| **🧩 Extensible** | Custom skills, OpenAPI tools, A2A protocol, plugins |
| **🎙️ Multimodal** | Vision, audio, document understanding |

---

## 🔌 Supported Providers

| Provider | Status | Authentication |
|----------|--------|----------------|
| **OpenAI** | ✅ Full Support | API Key |
| **Azure OpenAI** | ✅ Full Support | API Key / Azure AD |
| **Anthropic Claude** | ✅ Full Support | API Key |
| **Ollama** | ✅ Full Support | Local / Remote |
| **Google Gemini** | ✅ Full Support | API Key |
| **Groq** | ✅ Full Support | API Key |

---

## 📦 Module Overview

| Module | Purpose |
|--------|---------|
| `openstackai.easy` | One-liner AI functions |
| `openstackai.core` | Agent, LLM providers, memory |
| `openstackai.runner` | Agent execution engine |
| `openstackai.blueprint` | Workflows & orchestration patterns |
| `openstackai.skills` | Tools and skills system |
| `openstackai.sessions` | SQLite/Redis session storage |
| `openstackai.vectordb` | Vector database connectors |
| `openstackai.evaluation` | Agent evaluation framework |
| `openstackai.openapi` | OpenAPI tool generation |
| `openstackai.multimodal` | Vision, audio support |
| `openstackai.a2a` | Agent-to-Agent protocol |

---

## 🔧 Configuration

### Environment Variables

```bash
# OpenAI
export OPENAI_API_KEY="sk-..."

# Azure OpenAI
export AZURE_OPENAI_ENDPOINT="https://your-resource.openai.azure.com/"
export AZURE_OPENAI_DEPLOYMENT="gpt-4o-mini"
export AZURE_OPENAI_API_KEY="..."  # Or use Azure AD

# Anthropic
export ANTHROPIC_API_KEY="sk-ant-..."
```

### YAML Agent Configuration

```yaml
# research_agent.yaml
name: "Research Agent"
instructions: "You are an expert researcher."
provider: "openai"
model: "gpt-4o-mini"
skills:
  - web_search
  - summarize
```

```python
from openstackai.config import AgentConfig
agent = AgentConfig.from_yaml("research_agent.yaml").create_agent()
```

---

## 📚 Documentation

- **📖 Full Documentation**: [gitpavleenbali.github.io/PYAI](https://gitpavleenbali.github.io/PYAI/)
- **📘 GitHub Repository**: [github.com/gitpavleenbali/PYAI](https://github.com/gitpavleenbali/PYAI)
- **📋 Changelog**: [Changelog](https://gitpavleenbali.github.io/PYAI/docs/Changelog)
- **🏗️ Architecture**: [Architecture Guide](https://gitpavleenbali.github.io/PYAI/docs/Architecture)

---

## 🤝 Contributing

Contributions are welcome! See our [Contributing Guide](https://github.com/gitpavleenbali/PYAI/blob/master/docs/CONTRIBUTING.md).

---

## 📄 License

MIT License - see [LICENSE](https://github.com/gitpavleenbali/PYAI/blob/master/LICENSE) for details.

---

<p align="center">
  <strong>Built with ❤️ for the AI community</strong><br/>
  <em>openstackai - The Intelligence Engine for Software Factories</em>
</p>
