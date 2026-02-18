# ⚡ Runner Module

The **runner/** module provides execution control for agents with structured run management.

---

## Module Overview

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': 'transparent', 'primaryTextColor': '#ffffff', 'primaryBorderColor': '#ffffff', 'lineColor': '#ffffff', 'secondaryColor': 'transparent', 'tertiaryColor': 'transparent', 'background': 'transparent', 'mainBkg': 'transparent', 'nodeBorder': '#ffffff', 'clusterBkg': 'transparent', 'clusterBorder': '#ffffff', 'titleColor': '#ffffff', 'edgeLabelBackground': 'transparent', 'nodeTextColor': '#ffffff'}}}%%
flowchart TB
    subgraph Runner["runner/ Module"]
        R1["Runner"] --> R2["run_sync()"]
        R1 --> R3["run_async()"]
        R1 --> R4["run_stream()"]
        
        RC["RunConfig"] --> R1
        RX["RunContext"] --> R1
        RR["RunResult"] --> R1
        
        SR["StreamingRunner"] --> SS["Streaming Support"]
    end
```

---

## File Structure

```
src/openstackai/runner/
├── __init__.py
├── executor.py     # Main Runner class
└── streaming.py    # Streaming support
```

---

## Runner

The primary execution engine for agents.

### Basic Usage

```python
from openstackai import Agent, Runner

agent = Agent(
    name="Assistant",
    instructions="You are helpful."
)

# Synchronous execution
result = Runner.run_sync(agent, "Hello!")
print(result.final_output)

# Asynchronous execution
result = await Runner.run_async(agent, "Hello!")
```

### Execution Flow

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': 'transparent', 'primaryTextColor': '#ffffff', 'primaryBorderColor': '#ffffff', 'lineColor': '#ffffff', 'secondaryColor': 'transparent', 'tertiaryColor': 'transparent', 'background': 'transparent', 'mainBkg': 'transparent', 'nodeBorder': '#ffffff', 'clusterBkg': 'transparent', 'clusterBorder': '#ffffff', 'titleColor': '#ffffff', 'edgeLabelBackground': 'transparent', 'nodeTextColor': '#ffffff'}}}%%
sequenceDiagram
    participant User
    participant Runner
    participant Agent
    participant LLM
    participant Tools
    
    User->>Runner: run_sync(agent, input)
    Runner->>Runner: Create RunContext
    Runner->>Agent: execute(context)
    
    loop Turn Loop
        Agent->>LLM: generate()
        LLM-->>Agent: response
        
        alt Tool Calls
            Agent->>Tools: execute()
            Tools-->>Agent: result
        end
    end
    
    Agent-->>Runner: AgentResponse
    Runner-->>User: RunResult
```

---

## RunConfig

Configuration options for execution.

```python
from openstackai.runner import RunConfig

config = RunConfig(
    max_turns=10,           # Maximum iterations
    max_time=300.0,         # Timeout in seconds
    timeout_per_turn=60.0,  # Per-turn timeout
    stop_on_tool_error=False,
    verbose=True,           # Debug output
    trace_enabled=True,     # Enable tracing
    run_id="custom-id",     # Custom run ID
    metadata={              # Custom metadata
        "user_id": "123",
        "session": "abc"
    }
)

result = Runner.run_sync(agent, "Hello", config=config)
```

### Configuration Options

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `max_turns` | int | 10 | Max reasoning iterations |
| `max_time` | float | 300.0 | Total timeout (seconds) |
| `timeout_per_turn` | float | 60.0 | Per-turn timeout |
| `stop_on_tool_error` | bool | False | Stop on tool failure |
| `verbose` | bool | False | Debug output |
| `trace_enabled` | bool | True | Enable tracing |
| `run_id` | str | auto | Custom run identifier |
| `metadata` | dict | {} | Custom metadata |

---

## RunContext

Runtime context passed to agents during execution.

```python
from openstackai.runner import RunContext

context = RunContext(
    run_id="run-123",
    turn_count=0,
    variables={"user": "Alice"},
    history=[]
)

# Access during execution
elapsed = context.elapsed_time()
context.set_variable("key", "value")
value = context.get_variable("key")
```

---

## RunResult

Result of an agent execution.

```python
result = Runner.run_sync(agent, "Hello")

# Access result data
print(result.final_output)    # Final response text
print(result.run_id)          # Run identifier
print(result.status)          # RunStatus enum
print(result.turn_count)      # Number of turns
print(result.elapsed_time)    # Execution time
print(result.tool_calls)      # Tool invocations
print(result.metadata)        # Custom metadata
```

### RunResult Structure

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': 'transparent', 'primaryTextColor': '#ffffff', 'primaryBorderColor': '#ffffff', 'lineColor': '#ffffff', 'secondaryColor': 'transparent', 'tertiaryColor': 'transparent', 'background': 'transparent', 'mainBkg': 'transparent', 'nodeBorder': '#ffffff', 'clusterBkg': 'transparent', 'clusterBorder': '#ffffff', 'titleColor': '#ffffff', 'edgeLabelBackground': 'transparent', 'nodeTextColor': '#ffffff'}}}%%
flowchart TB
    subgraph RunResult["RunResult"]
        RR1["run_id: str"]
        RR2["status: RunStatus"]
        RR3["final_output: str"]
        RR4["turn_count: int"]
        RR5["elapsed_time: float"]
        RR6["tool_calls: List"]
        RR7["history: List"]
        RR8["metadata: Dict"]
    end
```

---

## RunStatus

Execution status enumeration.

```python
from openstackai.runner import RunStatus

# Possible statuses
RunStatus.QUEUED      # Not yet started
RunStatus.RUNNING     # In progress
RunStatus.COMPLETED   # Successfully finished
RunStatus.FAILED      # Error occurred
RunStatus.CANCELLED   # User cancelled
```

---

## Streaming

Stream responses in real-time.

```python
from openstackai import Agent, Runner

agent = Agent(name="Assistant", instructions="Be helpful")

# Stream response
async for chunk in Runner.run_stream(agent, "Tell me a story"):
    print(chunk, end="", flush=True)
```

### StreamingRunner

```python
from openstackai.runner import StreamingRunner

runner = StreamingRunner(agent)

async for event in runner.run("Write a poem"):
    if event.type == "text":
        print(event.content, end="")
    elif event.type == "tool_call":
        print(f"\n[Calling: {event.tool_name}]")
    elif event.type == "tool_result":
        print(f"[Result: {event.result}]")
```

---

## Advanced Patterns

### Multi-Turn Conversation

```python
from openstackai import Agent, Runner
from openstackai.runner import RunConfig

agent = Agent(name="Assistant", instructions="Be helpful")

# Multi-turn with context
context = []
while True:
    user_input = input("You: ")
    context.append({"role": "user", "content": user_input})
    
    result = Runner.run_sync(
        agent, 
        user_input,
        history=context
    )
    
    print(f"Agent: {result.final_output}")
    context.append({"role": "assistant", "content": result.final_output})
```

### Parallel Execution

```python
import asyncio
from openstackai import Agent, Runner

agents = [
    Agent(name="Agent1", instructions="..."),
    Agent(name="Agent2", instructions="..."),
    Agent(name="Agent3", instructions="...")
]

async def run_parallel():
    tasks = [
        Runner.run_async(agent, "Process this")
        for agent in agents
    ]
    results = await asyncio.gather(*tasks)
    return results

results = asyncio.run(run_parallel())
```

---

## Error Handling

```python
from openstackai import Agent, Runner
from openstackai.runner import RunStatus
from openstackai.errors import AgentError, TimeoutError

try:
    result = Runner.run_sync(agent, "Hello")
    
    if result.status == RunStatus.FAILED:
        print(f"Failed: {result.error}")
    elif result.status == RunStatus.COMPLETED:
        print(result.final_output)
        
except TimeoutError:
    print("Execution timed out")
except AgentError as e:
    print(f"Agent error: {e}")
```

---

➡️ [[Blueprint-Module]] | [[Core-Module]] | [[Home]]
