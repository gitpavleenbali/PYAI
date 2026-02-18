# Quick Start

Get up and running with openstackai in 5 minutes.

## Installation

```bash
pip install openstackai
```

For Azure OpenAI with Azure AD authentication:
```bash
pip install openstackai[azure]
```

## Configuration

Set your API keys:

```bash
# OpenAI
export OPENAI_API_KEY=sk-your-key

# Azure OpenAI (uses Azure AD - no API key needed!)
export AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
export AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
```

## Hello World

### One-Liner API

```python
from openstackai import ask

answer = ask("What is the capital of France?")
print(answer)  # Paris
```

### Agent with Tools

```python
from openstackai import Agent, Runner
from openstackai.skills import tool

@tool(description="Get weather for a city")
async def get_weather(city: str) -> str:
    return f"Weather in {city}: Sunny, 72°F"

agent = Agent(
    name="WeatherBot",
    instructions="Help users with weather information.",
    tools=[get_weather]
)

result = Runner.run_sync(agent, "What's the weather in Tokyo?")
print(result.final_output)
```

### RAG in 2 Lines

```python
from openstackai import rag

docs = rag.index("./documents")
answer = docs.ask("What is the main conclusion?")
```

## Next Steps

- [[Three Dimensions]] - Understand the openstackai architecture
- [[One-Liner APIs]] - Explore all easy/ module functions
- [[Agent Framework]] - Build sophisticated agents
- [[Multi-Agent Systems]] - Orchestrate teams of agents
