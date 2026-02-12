# 📝 Changelog

All notable changes to PyAgent will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.1.0] - 2026-02-12

### 🎉 Initial Release - "The Pandas of AI"

This is the first public release of PyAgent, the revolutionary AI library that makes complex AI tasks as simple as pandas operations.

### Added

#### One-Liner Functions
- `ask()` - Ask any question, get intelligent answers
- `research()` - Deep research on any topic
- `summarize()` - Summarize text, files, or URLs
- `extract()` - Extract structured data from text
- `generate()` - Generate content of various types
- `translate()` - Translate between languages
- `chat()` - Interactive chat sessions with memory
- `agent()` - Create custom AI agents

#### Modules
- `rag` - RAG operations in 2 lines
  - `rag.index()` - Index documents
  - `rag.ask()` - Query documents
  - `rag.from_url()` - RAG from URL
  - `rag.from_text()` - RAG from text
  
- `fetch` - Real-time data fetching
  - `fetch.weather()` - Get weather data
  - `fetch.news()` - Get news articles
  - `fetch.stock()` - Get stock data
  - `fetch.crypto()` - Get cryptocurrency data
  - `fetch.facts()` - Get facts on topics
  
- `analyze` - Data and text analysis
  - `analyze.data()` - Analyze DataFrames/dicts
  - `analyze.text()` - Analyze text content
  - `analyze.sentiment()` - Sentiment analysis
  - `analyze.compare()` - Compare items
  
- `code` - Code operations
  - `code.write()` - Generate code
  - `code.review()` - Review code quality
  - `code.debug()` - Debug errors
  - `code.explain()` - Explain code
  - `code.refactor()` - Refactor code
  - `code.convert()` - Convert between languages

#### Core Features
- Zero-configuration setup (auto-detects API keys)
- Multi-provider support (OpenAI, Anthropic, Azure)
- Full type hints with `.pyi` stub files
- Lazy imports for fast startup
- Sensible defaults for all operations

#### Prebuilt Agent Personas
- `coder` - Expert programmer
- `researcher` - Academic researcher
- `writer` - Content writer
- `analyst` - Data analyst
- `teacher` - Patient educator
- `advisor` - Strategic advisor
- `critic` - Constructive critic
- `creative` - Creative thinker
- `editor` - Content editor
- `python_expert` - Python specialist

#### Infrastructure
- Configuration management with `configure()`
- Environment variable support
- Azure OpenAI integration
- Comprehensive error handling

### Technical Details

- **Python Version**: 3.9+
- **Dependencies**: openai, anthropic (optional), pydantic
- **License**: MIT

---

## [Unreleased]

### Planned Features
- Async/await support for all functions
- Streaming responses
- Custom skill plugins
- Agent memory persistence
- Multi-agent orchestration
- Local LLM support (Ollama, llama.cpp)
- Web UI for agent management
- MCP (Model Context Protocol) integration

---

## Migration Guide

### From LangChain

```python
# Before (LangChain)
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

llm = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
template = PromptTemplate(input_variables=["q"], template="{q}")
chain = LLMChain(llm=llm, prompt=template)
result = chain.run("What is AI?")

# After (PyAgent)
from pyagent import ask
result = ask("What is AI?")
```

### From LlamaIndex

```python
# Before (LlamaIndex)
from llama_index import VectorStoreIndex, SimpleDirectoryReader

documents = SimpleDirectoryReader("./docs").load_data()
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()
response = query_engine.query("What is the summary?")

# After (PyAgent)
from pyagent import rag
response = rag.ask("./docs", "What is the summary?")
```

---

## Version History

| Version | Date | Highlights |
|---------|------|------------|
| 0.1.0 | 2026-02-12 | Initial release with full easy API |

---

*For feature requests or bug reports, please visit our [GitHub Issues](https://github.com/pyagent/pyagent/issues).*
