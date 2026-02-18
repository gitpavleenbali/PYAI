# 🧠 Core Module

The **core/** module provides the fundamental building blocks: Agent, Memory, LLM providers, and base components.

---

## Module Overview

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': 'transparent', 'primaryTextColor': '#ffffff', 'primaryBorderColor': '#ffffff', 'lineColor': '#ffffff', 'secondaryColor': 'transparent', 'tertiaryColor': 'transparent', 'background': 'transparent', 'mainBkg': 'transparent', 'nodeBorder': '#ffffff', 'clusterBkg': 'transparent', 'clusterBorder': '#ffffff', 'titleColor': '#ffffff', 'edgeLabelBackground': 'transparent', 'nodeTextColor': '#ffffff'}}}%%
flowchart TB
    subgraph Core["core/ Module"]
        subgraph Agent["Agent System"]
            A1["Agent"]
            A2["AgentConfig"]
            A3["AgentResponse"]
        end
        
        subgraph Memory["Memory System"]
            M1["Memory"]
            M2["ConversationMemory"]
            M3["VectorMemory"]
        end
        
        subgraph LLM["LLM Providers"]
            L1["LLMProvider"]
            L2["OpenAIProvider"]
            L3["AzureProvider"]
            L4["AnthropicProvider"]
            L5["OllamaProvider"]
        end
        
        subgraph Base["Base Components"]
            B1["BaseComponent"]
            B2["Executable"]
        end
    end
    
    Agent --> Memory
    Agent --> LLM
    Agent --> Base
```

---

## File Structure

```
src/openstackai/core/
├── __init__.py
├── agent.py        # Core Agent class
├── memory.py       # Memory implementations
├── llm.py          # LLM provider abstraction
├── base.py         # Base classes
└── cache.py        # Response caching
```

---

## Agent

The central orchestrator for AI agent behavior.

### Agent Class

```python
from openstackai import Agent
from openstackai.core import AgentConfig

# Basic agent
agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant."
)

# Full configuration
agent = Agent(
    name="ResearchAgent",
    instructions="You find and analyze information.",
    skills=[search_skill, summarize_skill],
    llm=azure_provider,
    memory=ConversationMemory(),
    config=AgentConfig(
        max_iterations=10,
        timeout_seconds=300.0,
        verbose=True,
        enable_memory=True
    )
)
```

### Agent Architecture

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': 'transparent', 'primaryTextColor': '#ffffff', 'primaryBorderColor': '#ffffff', 'lineColor': '#ffffff', 'secondaryColor': 'transparent', 'tertiaryColor': 'transparent', 'background': 'transparent', 'mainBkg': 'transparent', 'nodeBorder': '#ffffff', 'clusterBkg': 'transparent', 'clusterBorder': '#ffffff', 'titleColor': '#ffffff', 'edgeLabelBackground': 'transparent', 'nodeTextColor': '#ffffff'}}}%%
flowchart TB
    subgraph AgentInternal["Agent Internals"]
        I["Instructions"] --> E["Executor"]
        S["Skills"] --> E
        M["Memory"] --> E
        L["LLM"] --> E
        E --> R["Response"]
    end
```

### AgentConfig

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `max_iterations` | int | 10 | Max reasoning loops |
| `timeout_seconds` | float | 300.0 | Execution timeout |
| `verbose` | bool | False | Debug output |
| `enable_memory` | bool | True | Use memory |
| `enable_logging` | bool | True | Log operations |
| `retry_on_failure` | bool | True | Auto-retry |
| `max_retries` | int | 3 | Retry count |

### Agent Methods

```python
# Register skills
agent.register_skill(my_skill)

# Get skill
skill = agent.get_skill("search")

# List skills
skills = agent.available_skills

# Run agent (use Runner for full control)
from openstackai import Runner
result = Runner.run_sync(agent, "Find information about AI")
```

---

## Memory

Memory systems for conversation history and semantic retrieval.

### ConversationMemory

```python
from openstackai import ConversationMemory

memory = ConversationMemory(max_messages=100)

# Add messages
memory.add_user_message("Hello!")
memory.add_assistant_message("Hi there!")

# Get history
history = memory.get_messages()

# Clear
memory.clear()
```

### VectorMemory

```python
from openstackai import VectorMemory

memory = VectorMemory(
    embedding_model="text-embedding-3-small",
    similarity_threshold=0.7
)

# Store information
memory.store("Python is a programming language")
memory.store("openstackai is an intelligence engine")

# Retrieve relevant
results = memory.retrieve("What is openstackai?", top_k=5)
```

### Memory Architecture

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': 'transparent', 'primaryTextColor': '#ffffff', 'primaryBorderColor': '#ffffff', 'lineColor': '#ffffff', 'secondaryColor': 'transparent', 'tertiaryColor': 'transparent', 'background': 'transparent', 'mainBkg': 'transparent', 'nodeBorder': '#ffffff', 'clusterBkg': 'transparent', 'clusterBorder': '#ffffff', 'titleColor': '#ffffff', 'edgeLabelBackground': 'transparent', 'nodeTextColor': '#ffffff'}}}%%
flowchart LR
    subgraph MemoryTypes["Memory Types"]
        subgraph Conv["ConversationMemory"]
            C1["Messages List"]
            C2["Role Tracking"]
            C3["Window Limit"]
        end
        
        subgraph Vec["VectorMemory"]
            V1["Embeddings"]
            V2["Similarity Search"]
            V3["Semantic Retrieval"]
        end
    end
```

---

## LLM Providers

Multi-provider LLM abstraction layer.

### Provider Hierarchy

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': 'transparent', 'primaryTextColor': '#ffffff', 'primaryBorderColor': '#ffffff', 'lineColor': '#ffffff', 'secondaryColor': 'transparent', 'tertiaryColor': 'transparent', 'background': 'transparent', 'mainBkg': 'transparent', 'nodeBorder': '#ffffff', 'clusterBkg': 'transparent', 'clusterBorder': '#ffffff', 'titleColor': '#ffffff', 'edgeLabelBackground': 'transparent', 'nodeTextColor': '#ffffff'}}}%%
flowchart TB
    LP["LLMProvider<br/>(Abstract)"]
    
    LP --> OAI["OpenAIProvider"]
    LP --> AZ["AzureProvider"]
    LP --> ANT["AnthropicProvider"]
    LP --> OLL["OllamaProvider"]
```

### OpenAI Provider

```python
from openstackai.core.llm import OpenAIProvider

provider = OpenAIProvider(
    api_key="sk-...",
    model="gpt-4",
    temperature=0.7,
    max_tokens=1000
)

# Generate
response = await provider.generate("Hello!")

# Stream
async for chunk in provider.stream("Tell me a story"):
    print(chunk, end="")
```

### Azure OpenAI Provider

```python
from openstackai.core.llm import OpenAIProvider
from azure.identity import DefaultAzureCredential

# Azure AD authentication (recommended)
provider = OpenAIProvider(
    endpoint="https://your-resource.openai.azure.com/",
    deployment="gpt-4o-mini",
    credential=DefaultAzureCredential()
)

# Or with API key
provider = OpenAIProvider(
    endpoint="https://your-resource.openai.azure.com/",
    deployment="gpt-4o-mini",
    api_key="your-key"
)
```

### Anthropic Provider

```python
from openstackai.core.llm import AnthropicProvider

provider = AnthropicProvider(
    api_key="sk-ant-...",
    model="claude-3-opus-20240229"
)
```

### Ollama Provider (Local)

```python
from openstackai.core.llm import OllamaProvider

provider = OllamaProvider(
    host="http://localhost:11434",
    model="llama2"
)
```

---

## Base Components

### BaseComponent

```python
from openstackai.core.base import BaseComponent

class MyComponent(BaseComponent):
    def __init__(self, name: str):
        super().__init__(name=name)
        
    def process(self, data):
        # Implementation
        pass
```

### Executable Interface

```python
from openstackai.core.base import Executable

class MyExecutable(Executable):
    async def execute(self, input_data: Any) -> Any:
        # Async execution
        return result
```

---

## Cache

Response caching for efficiency.

```python
from openstackai.core.cache import ResponseCache

cache = ResponseCache(
    backend="redis",  # or "memory", "sqlite"
    ttl=3600          # 1 hour TTL
)

# Cache operations
cache.set("key", response)
cached = cache.get("key")
cache.invalidate("key")
```

---

## Integration Flow

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': 'transparent', 'primaryTextColor': '#ffffff', 'primaryBorderColor': '#ffffff', 'lineColor': '#ffffff', 'secondaryColor': 'transparent', 'tertiaryColor': 'transparent', 'background': 'transparent', 'mainBkg': 'transparent', 'nodeBorder': '#ffffff', 'clusterBkg': 'transparent', 'clusterBorder': '#ffffff', 'titleColor': '#ffffff', 'edgeLabelBackground': 'transparent', 'nodeTextColor': '#ffffff'}}}%%
sequenceDiagram
    participant User
    participant Agent
    participant Memory
    participant LLM
    participant Skills
    
    User->>Agent: run("query")
    Agent->>Memory: get_context()
    Memory-->>Agent: history
    Agent->>LLM: generate(prompt)
    LLM-->>Agent: response + tool_calls
    
    alt Has Tool Calls
        Agent->>Skills: execute(tool_call)
        Skills-->>Agent: result
        Agent->>LLM: generate(with_results)
        LLM-->>Agent: final_response
    end
    
    Agent->>Memory: store(conversation)
    Agent-->>User: AgentResponse
```

---

➡️ [[Runner-Module]] | [[Easy-Module]] | [[Home]]
