# 🔗 Blueprint Module

The **blueprint/** module provides multi-agent orchestration with workflows, patterns, and pipelines.

---

## Module Overview

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': 'transparent', 'primaryTextColor': '#ffffff', 'primaryBorderColor': '#ffffff', 'lineColor': '#ffffff', 'secondaryColor': 'transparent', 'tertiaryColor': 'transparent', 'background': 'transparent', 'mainBkg': 'transparent', 'nodeBorder': '#ffffff', 'clusterBkg': 'transparent', 'clusterBorder': '#ffffff', 'titleColor': '#ffffff', 'edgeLabelBackground': 'transparent', 'nodeTextColor': '#ffffff'}}}%%
flowchart TB
    subgraph Blueprint["blueprint/ Module"]
        W["Workflow"] --> S["Step"]
        W --> WC["WorkflowContext"]
        
        P["Patterns"]
        P --> CP["ChainPattern"]
        P --> RP["RouterPattern"]
        P --> MP["MapReducePattern"]
        P --> SP["SupervisorPattern"]
        
        PL["Pipeline"] --> PS["PipelineStage"]
        
        O["Orchestrator"] --> W
        O --> P
    end
```

---

## File Structure

```
src/openstackai/blueprint/
├── __init__.py
├── workflow.py      # Workflow and Step classes
├── patterns.py      # Orchestration patterns
├── pipeline.py      # Pipeline processing
├── orchestrator.py  # High-level orchestration
└── blueprint.py     # Blueprint definitions
```

---

## Workflow

Multi-step agent processes with context sharing.

### Basic Workflow

```python
from openstackai import Agent
from openstackai.blueprint import Workflow, Step

# Create agents
researcher = Agent(name="Researcher", instructions="Find information")
writer = Agent(name="Writer", instructions="Write content")
editor = Agent(name="Editor", instructions="Polish content")

# Build workflow
workflow = (Workflow("ContentPipeline")
    .add_step(Step("research", researcher))
    .add_step(Step("write", writer))
    .add_step(Step("edit", editor))
    .build())

# Execute
result = await workflow.run("Write an article about AI")
```

### Workflow Architecture

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': 'transparent', 'primaryTextColor': '#ffffff', 'primaryBorderColor': '#ffffff', 'lineColor': '#ffffff', 'secondaryColor': 'transparent', 'tertiaryColor': 'transparent', 'background': 'transparent', 'mainBkg': 'transparent', 'nodeBorder': '#ffffff', 'clusterBkg': 'transparent', 'clusterBorder': '#ffffff', 'titleColor': '#ffffff', 'edgeLabelBackground': 'transparent', 'nodeTextColor': '#ffffff'}}}%%
flowchart LR
    subgraph Workflow["Workflow Execution"]
        I["Input"] --> S1["Step 1<br/>Researcher"]
        S1 --> S2["Step 2<br/>Writer"]
        S2 --> S3["Step 3<br/>Editor"]
        S3 --> O["Output"]
        
        C["Context"] -.-> S1
        C -.-> S2
        C -.-> S3
    end
```

---

## Step

Individual workflow step definition.

### Step Types

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': 'transparent', 'primaryTextColor': '#ffffff', 'primaryBorderColor': '#ffffff', 'lineColor': '#ffffff', 'secondaryColor': 'transparent', 'tertiaryColor': 'transparent', 'background': 'transparent', 'mainBkg': 'transparent', 'nodeBorder': '#ffffff', 'clusterBkg': 'transparent', 'clusterBorder': '#ffffff', 'titleColor': '#ffffff', 'edgeLabelBackground': 'transparent', 'nodeTextColor': '#ffffff'}}}%%
flowchart TB
    subgraph StepTypes["Step Types"]
        ST1["AGENT<br/>Run an agent"]
        ST2["SKILL<br/>Execute a skill"]
        ST3["FUNCTION<br/>Custom function"]
        ST4["CONDITION<br/>Branching"]
        ST5["PARALLEL<br/>Parallel execution"]
        ST6["LOOP<br/>Iteration"]
    end
```

### Step Configuration

```python
from openstackai.blueprint import Step, StepType

# Agent step
agent_step = Step(
    name="research",
    executor=researcher,
    step_type=StepType.AGENT
)

# Function step
def custom_process(context):
    return context.get("data").upper()

function_step = Step(
    name="process",
    executor=custom_process,
    step_type=StepType.FUNCTION
)

# Conditional step
condition_step = Step(
    name="check",
    executor=lambda ctx: ctx.get("approved"),
    step_type=StepType.CONDITION,
    on_true="approve_step",
    on_false="reject_step"
)
```

---

## WorkflowContext

Context passed through workflow steps.

```python
from openstackai.blueprint import WorkflowContext

context = WorkflowContext()

# Set/get values
context.set("key", "value")
value = context.get("key")

# Update multiple
context.update({"a": 1, "b": 2})

# Add to history
context.add_to_history("step1", result)

# Clone context
new_context = context.clone()
```

---

## Orchestration Patterns

### ChainPattern

Sequential execution through multiple agents.

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': 'transparent', 'primaryTextColor': '#ffffff', 'primaryBorderColor': '#ffffff', 'lineColor': '#ffffff', 'secondaryColor': 'transparent', 'tertiaryColor': 'transparent', 'background': 'transparent', 'mainBkg': 'transparent', 'nodeBorder': '#ffffff', 'clusterBkg': 'transparent', 'clusterBorder': '#ffffff', 'titleColor': '#ffffff', 'edgeLabelBackground': 'transparent', 'nodeTextColor': '#ffffff'}}}%%
flowchart LR
    subgraph Chain["Chain Pattern"]
        A1["Agent 1"] --> A2["Agent 2"] --> A3["Agent 3"]
    end
```

```python
from openstackai.blueprint import ChainPattern

chain = ChainPattern([
    researcher,
    writer,
    editor
])

result = await chain.run("Write about AI trends")
```

---

### RouterPattern

Intelligent routing to specialized agents.

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': 'transparent', 'primaryTextColor': '#ffffff', 'primaryBorderColor': '#ffffff', 'lineColor': '#ffffff', 'secondaryColor': 'transparent', 'tertiaryColor': 'transparent', 'background': 'transparent', 'mainBkg': 'transparent', 'nodeBorder': '#ffffff', 'clusterBkg': 'transparent', 'clusterBorder': '#ffffff', 'titleColor': '#ffffff', 'edgeLabelBackground': 'transparent', 'nodeTextColor': '#ffffff'}}}%%
flowchart TB
    subgraph Router["Router Pattern"]
        R["Router"] --> C["Code Agent"]
        R --> M["Math Agent"]
        R --> W["Writing Agent"]
        R --> D["Data Agent"]
    end
```

```python
from openstackai.blueprint import RouterPattern

router = RouterPattern()

# Add routes with keywords
router.add_route("code", coder, keywords=["python", "code", "function"])
router.add_route("math", calculator, keywords=["calculate", "math", "equation"])
router.add_route("write", writer, keywords=["write", "content", "article"])

# Or with custom classifier
router.add_route("code", coder, classifier=lambda q: "code" in q.lower())

# Execute - automatically routes
result = await router.run("Write a Python function")  # → coder
result = await router.run("Calculate 2+2")            # → calculator
```

---

### MapReducePattern

Parallel processing with result aggregation.

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': 'transparent', 'primaryTextColor': '#ffffff', 'primaryBorderColor': '#ffffff', 'lineColor': '#ffffff', 'secondaryColor': 'transparent', 'tertiaryColor': 'transparent', 'background': 'transparent', 'mainBkg': 'transparent', 'nodeBorder': '#ffffff', 'clusterBkg': 'transparent', 'clusterBorder': '#ffffff', 'titleColor': '#ffffff', 'edgeLabelBackground': 'transparent', 'nodeTextColor': '#ffffff'}}}%%
flowchart TB
    subgraph MapReduce["MapReduce Pattern"]
        I["Input"] --> M1["Mapper 1"]
        I --> M2["Mapper 2"]
        I --> M3["Mapper 3"]
        
        M1 --> R["Reducer"]
        M2 --> R
        M3 --> R
        
        R --> O["Output"]
    end
```

```python
from openstackai.blueprint import MapReducePattern

# Create mappers (parallel workers)
mappers = [
    Agent(name="Researcher1", instructions="Research topic A"),
    Agent(name="Researcher2", instructions="Research topic B"),
    Agent(name="Researcher3", instructions="Research topic C")
]

# Create reducer (synthesizer)
reducer = Agent(name="Synthesizer", instructions="Combine research")

pattern = MapReducePattern(
    mappers=mappers,
    reducer=reducer
)

result = await pattern.run("Research AI trends")
```

---

### SupervisorPattern

Manager-worker hierarchy.

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': 'transparent', 'primaryTextColor': '#ffffff', 'primaryBorderColor': '#ffffff', 'lineColor': '#ffffff', 'secondaryColor': 'transparent', 'tertiaryColor': 'transparent', 'background': 'transparent', 'mainBkg': 'transparent', 'nodeBorder': '#ffffff', 'clusterBkg': 'transparent', 'clusterBorder': '#ffffff', 'titleColor': '#ffffff', 'edgeLabelBackground': 'transparent', 'nodeTextColor': '#ffffff'}}}%%
flowchart TB
    subgraph Supervisor["Supervisor Pattern"]
        M["Manager"] --> W1["Worker 1"]
        M --> W2["Worker 2"]
        M --> W3["Worker 3"]
        
        W1 --> M
        W2 --> M
        W3 --> M
    end
```

```python
from openstackai.blueprint import SupervisorPattern

pattern = SupervisorPattern(
    manager=Agent(name="Manager", instructions="Coordinate and delegate"),
    workers=[
        Agent(name="Coder", instructions="Write code"),
        Agent(name="Tester", instructions="Write tests"),
        Agent(name="Reviewer", instructions="Review code")
    ]
)

result = await pattern.run("Build a REST API")
```

---

## Pipeline

Processing pipeline for data transformation.

```python
from openstackai.blueprint import Pipeline, PipelineStage

pipeline = Pipeline("DataPipeline")

# Add stages
pipeline.add_stage(PipelineStage(
    name="extract",
    processor=extract_data
))
pipeline.add_stage(PipelineStage(
    name="transform",
    processor=transform_data
))
pipeline.add_stage(PipelineStage(
    name="load",
    processor=load_data
))

# Execute
result = await pipeline.run(input_data)
```

---

## Complex Workflow Example

```python
from openstackai import Agent
from openstackai.blueprint import Workflow, Step, StepType

# Define agents
planner = Agent(name="Planner", instructions="Create project plans")
researchers = [
    Agent(name="TechResearcher", instructions="Research technology"),
    Agent(name="MarketResearcher", instructions="Research market")
]
writer = Agent(name="Writer", instructions="Write reports")
reviewer = Agent(name="Reviewer", instructions="Review and improve")

# Build complex workflow
workflow = (Workflow("ProjectResearch")
    # Phase 1: Planning
    .add_step(Step("plan", planner))
    
    # Phase 2: Parallel research
    .add_step(Step(
        "research",
        researchers,
        step_type=StepType.PARALLEL
    ))
    
    # Phase 3: Writing
    .add_step(Step("write", writer))
    
    # Phase 4: Review with condition
    .add_step(Step(
        "review",
        reviewer,
        step_type=StepType.CONDITION,
        on_true="finalize",
        on_false="write"  # Loop back if not approved
    ))
    
    # Phase 5: Finalize
    .add_step(Step("finalize", lambda ctx: ctx.get("report")))
    
    .build())
```

---

➡️ [[Skills-Module]] | [[Runner-Module]] | [[Home]]
