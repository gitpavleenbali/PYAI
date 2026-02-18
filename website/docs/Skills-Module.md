# 🛠️ Skills Module

The **skills/** module provides the tools and capabilities system for agents.

---

## Module Overview

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': 'transparent', 'primaryTextColor': '#ffffff', 'primaryBorderColor': '#ffffff', 'lineColor': '#ffffff', 'secondaryColor': 'transparent', 'tertiaryColor': 'transparent', 'background': 'transparent', 'mainBkg': 'transparent', 'nodeBorder': '#ffffff', 'clusterBkg': 'transparent', 'clusterBorder': '#ffffff', 'titleColor': '#ffffff', 'edgeLabelBackground': 'transparent', 'nodeTextColor': '#ffffff'}}}%%
flowchart TB
    subgraph Skills["skills/ Module"]
        T["@tool decorator"] --> TR["ToolRegistry"]
        
        S["Skill"] --> SR["SkillRegistry"]
        
        B["Built-in Skills"]
        B --> BS1["SearchSkill"]
        B --> BS2["CodeSkill"]
        B --> BS3["FileSkill"]
        B --> BS4["WebSkill"]
        B --> BS5["MathSkill"]
        
        AS["ActionSkill"] --> S
        TS["ToolSkill"] --> S
    end
```

---

## File Structure

```
src/openstackai/skills/
├── __init__.py
├── skill.py          # Base Skill class
├── tool_skill.py     # Tool decorator
├── action_skill.py   # Action-based skills
├── builtin.py        # Built-in skills
└── registry.py       # Skill registry
```

---

## @tool Decorator

The simplest way to create agent tools.

### Basic Usage

```python
from openstackai.skills import tool

@tool(description="Get the current weather for a city")
async def get_weather(city: str) -> str:
    """Get weather information."""
    # Implementation
    return f"Weather in {city}: Sunny, 72°F"

@tool(description="Calculate the sum of two numbers")
async def add(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b
```

### With Schema

```python
from openstackai.skills import tool
from pydantic import BaseModel, Field

class SearchParams(BaseModel):
    query: str = Field(description="Search query")
    max_results: int = Field(default=10, description="Maximum results")

@tool(
    description="Search the web",
    schema=SearchParams
)
async def web_search(query: str, max_results: int = 10) -> list:
    """Search the web for information."""
    # Implementation
    return [{"title": "Result 1", "url": "..."}]
```

### Tool Registration

```python
from openstackai import Agent

# Create agent with tools
agent = Agent(
    name="Assistant",
    instructions="You are helpful.",
    tools=[get_weather, add, web_search]
)
```

---

## Tool Execution Flow

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': 'transparent', 'primaryTextColor': '#ffffff', 'primaryBorderColor': '#ffffff', 'lineColor': '#ffffff', 'secondaryColor': 'transparent', 'tertiaryColor': 'transparent', 'background': 'transparent', 'mainBkg': 'transparent', 'nodeBorder': '#ffffff', 'clusterBkg': 'transparent', 'clusterBorder': '#ffffff', 'titleColor': '#ffffff', 'edgeLabelBackground': 'transparent', 'nodeTextColor': '#ffffff'}}}%%
sequenceDiagram
    participant Agent
    participant LLM
    participant Tool
    
    Agent->>LLM: Generate with tools
    LLM-->>Agent: Response + tool_call
    Agent->>Tool: Execute function
    Tool-->>Agent: Result
    Agent->>LLM: Continue with result
    LLM-->>Agent: Final response
```

---

## Skill Class

For more complex, stateful tools.

```python
from openstackai.skills import Skill

class DatabaseSkill(Skill):
    """Skill for database operations."""
    
    name = "database"
    description = "Query and modify database"
    
    def __init__(self, connection_string: str):
        super().__init__()
        self.connection = self._connect(connection_string)
    
    async def execute(self, action: str, **params) -> Any:
        if action == "query":
            return await self._query(params["sql"])
        elif action == "insert":
            return await self._insert(params["table"], params["data"])
    
    def get_tools(self) -> list:
        """Return tools exposed by this skill."""
        return [
            self._create_tool("query", "Execute SQL query"),
            self._create_tool("insert", "Insert data")
        ]
```

---

## SkillRegistry

Manage and discover skills.

```python
from openstackai.skills import SkillRegistry

registry = SkillRegistry()

# Register skills
registry.register(DatabaseSkill("..."))
registry.register(WebSearchSkill())

# Get skill
db_skill = registry.get("database")

# List all skills
all_skills = registry.list_skills()

# Get all tools
all_tools = registry.get_all_tools()
```

---

## Built-in Skills

### SearchSkill

```python
from openstackai.skills.builtin import SearchSkill

search = SearchSkill(
    api_key="...",
    engine="google"  # or "bing", "duckduckgo"
)

results = await search.search("Python tutorials")
```

### CodeSkill

```python
from openstackai.skills.builtin import CodeSkill

code = CodeSkill()

# Execute code safely
result = await code.execute("""
def fibonacci(n):
    if n <= 1: return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))
""")
```

### FileSkill

```python
from openstackai.skills.builtin import FileSkill

file = FileSkill(base_path="./workspace")

# Read file
content = await file.read("document.txt")

# Write file
await file.write("output.txt", content)

# List directory
files = await file.list("./")
```

### WebSkill

```python
from openstackai.skills.builtin import WebSkill

web = WebSkill()

# Fetch URL
html = await web.fetch("https://example.com")

# Extract text
text = await web.extract_text("https://example.com")
```

### MathSkill

```python
from openstackai.skills.builtin import MathSkill

math = MathSkill()

# Calculate
result = await math.calculate("2 + 2 * 3")

# Symbolic math
solution = await math.solve("x^2 + 2x + 1 = 0")
```

---

## Creating Custom Skills

### Simple Tool

```python
from openstackai.skills import tool

@tool(description="Get stock price")
async def get_stock_price(symbol: str) -> dict:
    """Fetch current stock price."""
    # API call
    return {"symbol": symbol, "price": 150.0, "change": "+2.5%"}
```

### Complex Skill Class

```python
from openstackai.skills import Skill, tool
from typing import List, Dict, Any

class CRMSkill(Skill):
    """Customer relationship management skill."""
    
    name = "crm"
    description = "Manage customer data and interactions"
    
    def __init__(self, api_url: str, api_key: str):
        super().__init__()
        self.api_url = api_url
        self.api_key = api_key
    
    @tool(description="Search for customers")
    async def search_customers(
        self, 
        query: str, 
        limit: int = 10
    ) -> List[Dict]:
        """Search customer database."""
        # Implementation
        return [{"id": 1, "name": "John Doe"}]
    
    @tool(description="Get customer details")
    async def get_customer(self, customer_id: int) -> Dict:
        """Get customer by ID."""
        return {"id": customer_id, "name": "John", "email": "..."}
    
    @tool(description="Create new customer")
    async def create_customer(
        self, 
        name: str, 
        email: str, 
        phone: str = None
    ) -> Dict:
        """Create a new customer record."""
        return {"id": 123, "name": name, "created": True}
```

---

## Skill Architecture

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': 'transparent', 'primaryTextColor': '#ffffff', 'primaryBorderColor': '#ffffff', 'lineColor': '#ffffff', 'secondaryColor': 'transparent', 'tertiaryColor': 'transparent', 'background': 'transparent', 'mainBkg': 'transparent', 'nodeBorder': '#ffffff', 'clusterBkg': 'transparent', 'clusterBorder': '#ffffff', 'titleColor': '#ffffff', 'edgeLabelBackground': 'transparent', 'nodeTextColor': '#ffffff'}}}%%
flowchart TB
    subgraph SkillArch["Skill Architecture"]
        A["Agent"]
        
        subgraph Registry["SkillRegistry"]
            S1["Skill 1"]
            S2["Skill 2"]
            S3["Skill 3"]
        end
        
        subgraph Tools["Tools"]
            T1["tool_1()"]
            T2["tool_2()"]
            T3["tool_3()"]
        end
        
        A --> Registry
        Registry --> Tools
    end
```

---

## Best Practices

### 1. Clear Descriptions

```python
# Good
@tool(description="Get the current temperature in Fahrenheit for a city")
async def get_temperature(city: str) -> float: ...

# Bad
@tool(description="temp")
async def get_temp(c: str): ...
```

### 2. Type Hints

```python
# Good - LLM understands parameters
@tool(description="Calculate compound interest")
async def compound_interest(
    principal: float,
    rate: float,
    years: int,
    compounds_per_year: int = 12
) -> float: ...
```

### 3. Error Handling

```python
@tool(description="Fetch URL content")
async def fetch_url(url: str) -> str:
    try:
        response = await client.get(url)
        return response.text
    except Exception as e:
        return f"Error fetching URL: {e}"
```

---

➡️ [[Kernel-Module]] | [[Blueprint-Module]] | [[Home]]
