# Examples

Learn openstackai through hands-on examples.

## Quick Examples

### One-Liner API

```python
from openstackai import ask, summarize, research

# Simple question
answer = ask("What is quantum computing?")

# Summarize text
summary = summarize("Long article text here...")

# Research a topic
report = research("AI trends 2026")
```

### Agent with Tools

```python
from openstackai import Agent, Runner

def get_weather(city: str) -> str:
    """Get weather for a city."""
    return f"Weather in {city}: Sunny, 72°F"

agent = Agent(
    name="WeatherBot",
    instructions="Help users with weather queries.",
    tools=[get_weather]
)

result = Runner.run_sync(agent, "What's the weather in Seattle?")
print(result.final_output)
```

### Multi-Agent Workflow

```python
from openstackai import Agent, Runner
from openstackai.blueprint import ChainWorkflow

researcher = Agent(
    name="Researcher",
    instructions="Research topics thoroughly."
)

writer = Agent(
    name="Writer",
    instructions="Write engaging articles."
)

workflow = ChainWorkflow([researcher, writer])
result = Runner.run_sync(workflow, "AI in healthcare")
```

## More Examples

- [Basic Agent](https://github.com/gitpavleenbali/PYAI/blob/master/examples/basic_agent.py)
- [Custom Skills](https://github.com/gitpavleenbali/PYAI/blob/master/examples/custom_skills.py)
- [Multi-Agent Workflow](https://github.com/gitpavleenbali/PYAI/blob/master/examples/multi_agent_workflow.py)
- [Research Assistant](https://github.com/gitpavleenbali/PYAI/blob/master/examples/smart_research_assistant.py)
