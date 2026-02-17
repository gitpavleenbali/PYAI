# 🔌 Kernel Module

The **kernel/** module provides Semantic Kernel-style service management for enterprise applications.

---

## Module Overview

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': 'transparent', 'primaryTextColor': '#ffffff', 'primaryBorderColor': '#ffffff', 'lineColor': '#ffffff', 'secondaryColor': 'transparent', 'tertiaryColor': 'transparent', 'background': 'transparent', 'mainBkg': 'transparent', 'nodeBorder': '#ffffff', 'clusterBkg': 'transparent', 'clusterBorder': '#ffffff', 'titleColor': '#ffffff', 'edgeLabelBackground': 'transparent', 'nodeTextColor': '#ffffff'}}}%%
flowchart TB
    subgraph Kernel["kernel/ Module"]
        K["Kernel"] --> SR["ServiceRegistry"]
        K --> FR["FilterRegistry"]
        K --> PR["PluginRegistry"]
        
        SR --> S1["LLM Services"]
        SR --> S2["Memory Services"]
        SR --> S3["Vector Services"]
        
        FR --> F1["Logging Filter"]
        FR --> F2["Validation Filter"]
        FR --> F3["Auth Filter"]
        
        C["KernelContext"] --> K
        IC["InvocationContext"] --> K
    end
```

---

## File Structure

```
src/pyai/kernel/
├── __init__.py
├── kernel.py        # Main Kernel class
├── services.py      # Service registry
├── filters.py       # Filter system
└── context.py       # Execution context
```

---

## Kernel

Central orchestration layer for AI applications.

### Basic Usage

```python
from pyai.kernel import Kernel

# Create kernel
kernel = Kernel()

# Add services
kernel.add_service(openai_provider, service_id="gpt4", is_default=True)
kernel.add_service(azure_provider, service_id="azure")
kernel.add_service(redis_memory, service_id="memory")

# Add plugins
kernel.add_plugin(WeatherPlugin())
kernel.add_plugin(SearchPlugin())

# Invoke function
result = await kernel.invoke("weather", "get_forecast", city="NYC")
```

### Kernel Architecture

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': 'transparent', 'primaryTextColor': '#ffffff', 'primaryBorderColor': '#ffffff', 'lineColor': '#ffffff', 'secondaryColor': 'transparent', 'tertiaryColor': 'transparent', 'background': 'transparent', 'mainBkg': 'transparent', 'nodeBorder': '#ffffff', 'clusterBkg': 'transparent', 'clusterBorder': '#ffffff', 'titleColor': '#ffffff', 'edgeLabelBackground': 'transparent', 'nodeTextColor': '#ffffff'}}}%%
flowchart TB
    subgraph KernelArch["Kernel Architecture"]
        App["Application"] --> K["Kernel"]
        
        K --> Services["Services"]
        K --> Plugins["Plugins"]
        K --> Filters["Filters"]
        
        Services --> LLM["LLM Providers"]
        Services --> Mem["Memory"]
        Services --> Vec["Vector Stores"]
        
        Plugins --> P1["Plugin A"]
        Plugins --> P2["Plugin B"]
        
        Filters --> F1["Pre-Filter"]
        Filters --> F2["Post-Filter"]
    end
```

---

## KernelBuilder

Fluent API for kernel construction.

```python
from pyai.kernel import KernelBuilder

kernel = (KernelBuilder()
    # Add LLM services
    .add_llm(
        openai_client,
        name="gpt4",
        is_default=True
    )
    .add_llm(
        azure_client,
        name="azure-gpt"
    )
    
    # Add memory
    .add_memory(
        redis_memory,
        name="cache"
    )
    
    # Add vector store
    .add_vector_store(
        chroma_db,
        name="vectors"
    )
    
    # Add plugins
    .add_plugin(WeatherPlugin())
    .add_plugin(SearchPlugin())
    
    # Add filters
    .add_filter(LoggingFilter())
    .add_filter(ValidationFilter())
    
    .build())
```

---

## ServiceRegistry

Manage and access services.

### Service Types

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': 'transparent', 'primaryTextColor': '#ffffff', 'primaryBorderColor': '#ffffff', 'lineColor': '#ffffff', 'secondaryColor': 'transparent', 'tertiaryColor': 'transparent', 'background': 'transparent', 'mainBkg': 'transparent', 'nodeBorder': '#ffffff', 'clusterBkg': 'transparent', 'clusterBorder': '#ffffff', 'titleColor': '#ffffff', 'edgeLabelBackground': 'transparent', 'nodeTextColor': '#ffffff'}}}%%
flowchart TB
    subgraph ServiceTypes["Service Types"]
        ST["ServiceType"]
        ST --> LLM["LLM<br/>Language models"]
        ST --> MEM["MEMORY<br/>Conversation storage"]
        ST --> VEC["VECTOR<br/>Vector databases"]
        ST --> EMB["EMBEDDING<br/>Text embeddings"]
        ST --> CUS["CUSTOM<br/>User-defined"]
    end
```

### Registry Operations

```python
from pyai.kernel import ServiceRegistry, Service, ServiceType

registry = ServiceRegistry()

# Register service
registry.register(Service(
    service_id="gpt4",
    service_type=ServiceType.LLM,
    instance=openai_client,
    is_default=True
))

# Get service
llm = registry.get("gpt4")
default_llm = registry.get_default(ServiceType.LLM)

# List services
all_services = registry.list_services()
llm_services = registry.list_by_type(ServiceType.LLM)
```

---

## FilterRegistry

Middleware for request/response processing.

### Filter Types

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': 'transparent', 'primaryTextColor': '#ffffff', 'primaryBorderColor': '#ffffff', 'lineColor': '#ffffff', 'secondaryColor': 'transparent', 'tertiaryColor': 'transparent', 'background': 'transparent', 'mainBkg': 'transparent', 'nodeBorder': '#ffffff', 'clusterBkg': 'transparent', 'clusterBorder': '#ffffff', 'titleColor': '#ffffff', 'edgeLabelBackground': 'transparent', 'nodeTextColor': '#ffffff'}}}%%
flowchart LR
    subgraph FilterFlow["Filter Flow"]
        R["Request"] --> PRE["Pre-Filters"]
        PRE --> E["Execution"]
        E --> POST["Post-Filters"]
        POST --> RES["Response"]
    end
```

### Creating Filters

```python
from pyai.kernel import Filter, FilterContext, FilterType

class LoggingFilter(Filter):
    """Log all kernel invocations."""
    
    filter_type = FilterType.PRE_AND_POST
    
    async def on_pre_invoke(self, context: FilterContext) -> FilterContext:
        print(f"Starting: {context.function_name}")
        context.start_time = time.time()
        return context
    
    async def on_post_invoke(self, context: FilterContext) -> FilterContext:
        elapsed = time.time() - context.start_time
        print(f"Completed: {context.function_name} in {elapsed:.2f}s")
        return context

class ValidationFilter(Filter):
    """Validate inputs before execution."""
    
    filter_type = FilterType.PRE
    
    async def on_pre_invoke(self, context: FilterContext) -> FilterContext:
        if not context.arguments.get("required_param"):
            raise ValueError("Missing required_param")
        return context
```

### Registering Filters

```python
kernel.add_filter(LoggingFilter())
kernel.add_filter(ValidationFilter())
kernel.add_filter(AuthenticationFilter(api_key="..."))
```

---

## KernelContext

Execution context for kernel operations.

```python
from pyai.kernel import KernelContext

# Create context
context = KernelContext(
    user_id="user123",
    session_id="session456",
    metadata={"source": "api"}
)

# Execute with context
result = await kernel.invoke(
    "weather",
    "get_forecast",
    context=context,
    city="NYC"
)
```

---

## Plugin System

### Creating Plugins

```python
from pyai.kernel import KernelPlugin
from pyai.skills import tool

class WeatherPlugin(KernelPlugin):
    """Weather information plugin."""
    
    name = "weather"
    description = "Get weather information"
    
    @tool(description="Get current weather")
    async def get_current(self, city: str) -> dict:
        return {"city": city, "temp": 72, "conditions": "Sunny"}
    
    @tool(description="Get weather forecast")
    async def get_forecast(self, city: str, days: int = 7) -> list:
        return [{"day": i, "temp": 70 + i} for i in range(days)]
```

### Plugin Registration

```python
# Register plugin
kernel.add_plugin(WeatherPlugin())

# Invoke plugin function
current = await kernel.invoke("weather", "get_current", city="NYC")
forecast = await kernel.invoke("weather", "get_forecast", city="NYC", days=5)
```

---

## Creating Agents with Kernel

```python
from pyai.kernel import Kernel

# Create kernel with services
kernel = (KernelBuilder()
    .add_llm(azure_client, name="azure", is_default=True)
    .add_memory(redis_memory)
    .add_plugin(WeatherPlugin())
    .add_plugin(SearchPlugin())
    .build())

# Create agent using kernel
agent = kernel.create_agent(
    name="Assistant",
    instructions="You are a helpful assistant.",
    plugins=["weather", "search"]
)

# Agent uses kernel services automatically
result = await agent.run("What's the weather in NYC?")
```

---

## Full Example

```python
from pyai.kernel import Kernel, KernelBuilder
from pyai.core.llm import OpenAIProvider
from pyai.sessions import RedisSessionStore

# Initialize services
openai = OpenAIProvider(api_key="...")
azure = OpenAIProvider(endpoint="...", deployment="...")
redis = RedisSessionStore(url="redis://localhost:6379")

# Build kernel
kernel = (KernelBuilder()
    .add_llm(openai, name="openai", is_default=True)
    .add_llm(azure, name="azure")
    .add_memory(redis, name="sessions")
    .add_plugin(WeatherPlugin())
    .add_plugin(SearchPlugin())
    .add_plugin(DatabasePlugin())
    .add_filter(LoggingFilter())
    .add_filter(AuthFilter(api_key="..."))
    .build())

# Use kernel
async def main():
    # Direct invocation
    weather = await kernel.invoke("weather", "get_current", city="NYC")
    
    # Create and run agent
    agent = kernel.create_agent(
        name="DataAssistant",
        instructions="Help with data queries",
        plugins=["database"]
    )
    
    result = await agent.run("What customers are in NYC?")
    print(result.final_output)
```

---

## Execution Flow

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': 'transparent', 'primaryTextColor': '#ffffff', 'primaryBorderColor': '#ffffff', 'lineColor': '#ffffff', 'secondaryColor': 'transparent', 'tertiaryColor': 'transparent', 'background': 'transparent', 'mainBkg': 'transparent', 'nodeBorder': '#ffffff', 'clusterBkg': 'transparent', 'clusterBorder': '#ffffff', 'titleColor': '#ffffff', 'edgeLabelBackground': 'transparent', 'nodeTextColor': '#ffffff'}}}%%
sequenceDiagram
    participant App
    participant Kernel
    participant PreFilter
    participant Plugin
    participant PostFilter
    
    App->>Kernel: invoke(plugin, function, args)
    Kernel->>PreFilter: on_pre_invoke()
    PreFilter-->>Kernel: context
    Kernel->>Plugin: execute(function, args)
    Plugin-->>Kernel: result
    Kernel->>PostFilter: on_post_invoke()
    PostFilter-->>Kernel: context
    Kernel-->>App: result
```

---

➡️ [[Sessions-Module]] | [[Skills-Module]] | [[Home]]
