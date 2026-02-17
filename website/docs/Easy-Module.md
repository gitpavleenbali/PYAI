# 🎯 Easy Module

The **easy/** module provides one-liner APIs for common AI tasks. Zero configuration, instant results.

---

## Module Overview

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': 'transparent', 'primaryTextColor': '#ffffff', 'primaryBorderColor': '#ffffff', 'lineColor': '#ffffff', 'secondaryColor': 'transparent', 'tertiaryColor': 'transparent', 'background': 'transparent', 'mainBkg': 'transparent', 'nodeBorder': '#ffffff', 'clusterBkg': 'transparent', 'clusterBorder': '#ffffff', 'titleColor': '#ffffff', 'edgeLabelBackground': 'transparent', 'nodeTextColor': '#ffffff'}}}%%
flowchart TB
    subgraph Easy["easy/ Module"]
        subgraph Core["Core Functions"]
            A1["ask"]
            A2["research"]
            A3["summarize"]
            A4["extract"]
            A5["generate"]
            A6["translate"]
        end
        
        subgraph Data["Data Functions"]
            D1["fetch"]
            D2["analyze"]
            D3["rag"]
        end
        
        subgraph Code["Code Functions"]
            C1["code.write"]
            C2["code.review"]
            C3["code.debug"]
        end
        
        subgraph Advanced["Advanced"]
            V1["handoff"]
            V2["guardrails"]
            V3["trace"]
            V4["mcp"]
            V5["chat"]
        end
    end
```

---

## File Structure

```
src/pyai/easy/
├── __init__.py
├── ask.py              # Universal Q&A
├── research.py         # Deep research
├── summarize.py        # Summarization
├── extract.py          # Data extraction
├── generate.py         # Content generation
├── translate.py        # Translation
├── fetch.py            # Real-time data
├── analyze.py          # Data analysis
├── rag.py              # RAG system
├── code.py             # Code operations
├── chat.py             # Interactive chat
├── handoff.py          # Agent handoffs
├── guardrails.py       # Safety guards
├── trace.py            # Tracing/logging
├── mcp.py              # MCP protocol
├── agent_factory.py    # Quick agent creation
├── config.py           # Auto-configuration
└── llm_interface.py    # LLM abstraction
```

---

## Core Functions

### ask() — Universal Question Answering

```python
from pyai import ask

# Simple question
answer = ask("What is Python?")

# With options
answer = ask(
    "Explain quantum computing",
    detailed=True,        # Longer response
    format="bullet",      # Bullet points
    model="gpt-4"         # Specific model
)
```

**Parameters:**
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `question` | str | required | The question |
| `detailed` | bool | False | Longer response |
| `format` | str | None | "bullet", "numbered", "json" |
| `model` | str | auto | Model override |

---

### research() — Deep Topic Research

```python
from pyai import research

result = research("AI trends in enterprise software")

print(result.summary)      # Executive summary
print(result.key_points)   # List of key findings
print(result.insights)     # Strategic insights
print(result.sources)      # Referenced sources
```

**Returns:** `ResearchResult`
| Field | Type | Description |
|-------|------|-------------|
| `summary` | str | Executive summary |
| `key_points` | list | Key findings |
| `insights` | list | Strategic insights |
| `sources` | list | Source references |

---

### summarize() — Summarization

```python
from pyai import summarize

# Summarize text
summary = summarize(long_text)

# Summarize a file
summary = summarize("./report.pdf")
summary = summarize("./document.docx")

# Summarize a URL
summary = summarize("https://example.com/article")

# With length control
summary = summarize(text, length="brief")      # ~50 words
summary = summarize(text, length="detailed")   # ~300 words
```

---

### extract() — Structured Data Extraction

```python
from pyai import extract

# Extract specific fields
data = extract(
    invoice_text,
    fields=["invoice_number", "date", "total", "items"]
)

# Returns structured data
print(data["invoice_number"])  # "INV-2024-001"
print(data["total"])           # "1,234.56"
print(data["items"])           # [{"name": "Widget", "qty": 5}]

# With schema
from pydantic import BaseModel

class Person(BaseModel):
    name: str
    age: int
    city: str

person = extract(text, schema=Person)
```

---

### generate() — Content Generation

```python
from pyai import generate

# Generate different content types
blog = generate("Python async programming", type="article")
email = generate("thank you letter", type="email")
code = generate("fibonacci function", type="code")
sql = generate("users table with auth", type="sql")

# With customization
content = generate(
    "API documentation",
    type="markdown",
    style="technical",
    length="detailed"
)
```

---

### translate() — Translation

```python
from pyai import translate

# Simple translation
spanish = translate("Hello, how are you?", to="spanish")
japanese = translate("Hello", to="japanese")

# Auto-detect source language
result = translate("Bonjour le monde", to="english")
```

---

## Data Functions

### fetch — Real-time Data

```python
from pyai import fetch

# Weather
weather = fetch.weather("New York")
print(weather.temperature)
print(weather.conditions)

# News
news = fetch.news("artificial intelligence")
for article in news.articles:
    print(article.title)
    print(article.summary)

# Stock data
stock = fetch.stock("AAPL")
print(stock.price)
print(stock.change)

# Any URL
content = fetch.url("https://api.example.com/data")
```

---

### analyze — Data Analysis

```python
from pyai import analyze

# Sentiment analysis
sentiment = analyze.sentiment("I love this product!")
print(sentiment.score)      # 0.9
print(sentiment.label)      # "positive"

# Entity extraction
entities = analyze.entities(text)
for entity in entities:
    print(entity.text, entity.type)

# Topic classification  
topics = analyze.topics(document)
```

---

### rag — RAG System

```python
from pyai import rag

# Index documents
docs = rag.index("./documents/")
docs = rag.index(["doc1.pdf", "doc2.md"])

# Ask questions
answer = docs.ask("What is the main conclusion?")
answer = docs.ask("Summarize the findings")

# With sources
result = docs.ask("What are the recommendations?", return_sources=True)
print(result.answer)
print(result.sources)
```

**RAG Architecture:**

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': 'transparent', 'primaryTextColor': '#ffffff', 'primaryBorderColor': '#ffffff', 'lineColor': '#ffffff', 'secondaryColor': 'transparent', 'tertiaryColor': 'transparent', 'background': 'transparent', 'mainBkg': 'transparent', 'nodeBorder': '#ffffff', 'clusterBkg': 'transparent', 'clusterBorder': '#ffffff', 'titleColor': '#ffffff', 'edgeLabelBackground': 'transparent', 'nodeTextColor': '#ffffff'}}}%%
flowchart LR
    subgraph Index["Indexing"]
        D["Documents"] --> C["Chunking"]
        C --> E["Embedding"]
        E --> V["Vector Store"]
    end
    
    subgraph Query["Querying"]
        Q["Question"] --> QE["Query Embed"]
        QE --> S["Search"]
        S --> R["Retrieve"]
        R --> G["Generate"]
        G --> A["Answer"]
    end
    
    V --> S
```

---

## Code Functions

### code — Code Operations

```python
from pyai import code

# Write new code
api = code.write("REST API with CRUD operations")
function = code.write("async file downloader")

# Review existing code
review = code.review(my_code)
print(review.issues)         # List of issues
print(review.suggestions)    # Improvement suggestions
print(review.score)          # Quality score

# Debug errors
fix = code.debug("""
TypeError: 'NoneType' object is not subscriptable
At line 42: result = data['key']
""")
print(fix.explanation)
print(fix.solution)

# Refactor code
improved = code.refactor(
    old_code,
    goal="convert to async"
)

# Generate tests
tests = code.test(my_function)
```

---

## Advanced Functions

### handoff — Agent Handoffs

```python
from pyai import handoff, Agent

agent_a = Agent(name="Researcher")
agent_b = Agent(name="Writer")

# Transfer control with context
result = handoff(
    from_agent=agent_a,
    to_agent=agent_b,
    context={"research": research_data}
)
```

---

### guardrails — Safety Guards

```python
from pyai import guardrails

# Create guarded function
safe_ask = guardrails.wrap(
    ask,
    block_pii=True,           # Block PII
    block_harmful=True,       # Block harmful content
    max_tokens=1000,          # Limit response
    allowed_topics=["tech"]   # Topic filter
)

answer = safe_ask("Tell me about Python")
```

---

### trace — Tracing

```python
from pyai import trace

# Enable tracing
trace.enable()

# Run operations (automatically traced)
answer = ask("What is AI?")

# View traces
trace.show()

# Export traces
trace.export("traces.json")
```

---

### chat — Interactive Sessions

```python
from pyai import chat

# Start a chat session
session = chat.start()

# Conversation with memory
response1 = session.send("My name is Alice")
response2 = session.send("What's my name?")  # "Alice"

# End session
session.end()
```

---

## Flow Diagram

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': 'transparent', 'primaryTextColor': '#ffffff', 'primaryBorderColor': '#ffffff', 'lineColor': '#ffffff', 'secondaryColor': 'transparent', 'tertiaryColor': 'transparent', 'background': 'transparent', 'mainBkg': 'transparent', 'nodeBorder': '#ffffff', 'clusterBkg': 'transparent', 'clusterBorder': '#ffffff', 'titleColor': '#ffffff', 'edgeLabelBackground': 'transparent', 'nodeTextColor': '#ffffff'}}}%%
sequenceDiagram
    participant User
    participant Easy as easy/ Module
    participant Config as Auto-Config
    participant LLM as LLM Provider
    
    User->>Easy: ask("question")
    Easy->>Config: Detect provider
    Config-->>Easy: Provider config
    Easy->>Easy: Build prompt
    Easy->>LLM: API call
    LLM-->>Easy: Response
    Easy-->>User: Clean answer
```

---

➡️ [[Core-Module]] | [[Home]] | [[Quick-Start]]
