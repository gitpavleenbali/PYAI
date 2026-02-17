# PyAI Architecture Knowledge Base

> **The Complete Engineering Blueprint for AI Agent Systems**  
> **Author:** Senior Cloud Architect & Tech Lead  
> **Date:** February 2026

---

## 1. What is PyAI?

### Vision
PyAI is a **pandas-for-AI-agents** library - making AI agent development as simple as data manipulation. Just as pandas revolutionized data science with simple one-liners, PyAI aims to democratize AI agent development.

### Core Philosophy

```
┌────────────────────────────────────────────────────────────────────────┐
│                        PyAI PHILOSOPHY                              │
├────────────────────────────────────────────────────────────────────────┤
│                                                                        │
│   "Make the simple things simple, and the complex things possible"     │
│                                                                        │
│   Level 1: One-liners for common tasks                                │
│            ask(), summarize(), extract(), translate()                  │
│                                                                        │
│   Level 2: Configurable agents for custom behaviors                   │
│            agent(), persona, memory, model                             │
│                                                                        │
│   Level 3: Enterprise patterns for production systems                 │
│            handoff, guardrails, trace, orchestrator                    │
│                                                                        │
│   Level 4: Framework integration for ecosystem compatibility          │
│            langchain, semantic_kernel, vector_db                       │
│                                                                        │
└────────────────────────────────────────────────────────────────────────┘
```

### The Three Dimensions

```
                    ┌─────────────────┐
                    │    PRODUCTS     │
                    │  (Integrations) │
                    │  ┌───────────┐  │
                    │  │LangChain  │  │
                    │  │SK Adapter │  │
                    │  │Vector DBs │  │
                    │  └───────────┘  │
                    └────────┬────────┘
                             │
        ┌────────────────────┼────────────────────┐
        │                    │                    │
        ▼                    ▼                    ▼
┌───────────────┐   ┌───────────────┐   ┌───────────────┐
│   PROCESSES   │   │     CORE      │   │  DISTRIBUTION │
│ (Orchestrator)│   │   PyAI     │   │   (PyPI)      │
│ ┌───────────┐ │   │ ┌───────────┐ │   │ ┌───────────┐ │
│ │ Task      │ │   │ │  easy/*   │ │   │ │ pip       │ │
│ │ Workflow  │ │   │ │  core/*   │ │   │ │ docs      │ │
│ │ Patterns  │ │   │ │  skills/* │ │   │ │ examples  │ │
│ └───────────┘ │   │ └───────────┘ │   │ └───────────┘ │
└───────────────┘   └───────────────┘   └───────────────┘
```

---

## 2. System Architecture

### High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                           USER APPLICATION                               │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│   from PyAI import ask, agent, summarize, extract                     │
│   result = ask("What is the meaning of life?")                           │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                         PyAI EASY MODULE                              │
│                                                                          │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐       │
│  │   ask    │ │summarize │ │ extract  │ │translate │ │ generate │       │
│  └────┬─────┘ └────┬─────┘ └────┬─────┘ └────┬─────┘ └────┬─────┘       │
│       └────────────┴────────────┴────────────┴────────────┘             │
│                                    │                                     │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐       │
│  │  agent   │ │   chat   │ │  code    │ │   rag    │ │ research │       │
│  └────┬─────┘ └────┬─────┘ └────┬─────┘ └────┬─────┘ └────┬─────┘       │
│       └────────────┴────────────┴────────────┴────────────┘             │
│                                    │                                     │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐                    │
│  │ handoff  │ │guardrails│ │   mcp    │ │  trace   │                    │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘                    │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                         LLM INTERFACE LAYER                              │
│                                                                          │
│  ┌─────────────────────────────────────────────────────────────────┐    │
│  │                        LLMInterface                               │    │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐            │    │
│  │  │  chat()  │ │complete()│ │ stream() │ │ embed()  │            │    │
│  │  └──────────┘ └──────────┘ └──────────┘ └──────────┘            │    │
│  └─────────────────────────────────────────────────────────────────┘    │
│                                    │                                     │
│                    ┌───────────────┴───────────────┐                    │
│                    ▼                               ▼                    │
│        ┌──────────────────┐             ┌──────────────────┐           │
│        │   OpenAI API     │             │  Azure OpenAI    │           │
│        │   gpt-4o         │             │  gpt-4o-mini     │           │
│        └──────────────────┘             └──────────────────┘           │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

### Module Structure

```
PyAI/
├── __init__.py              # Public API exports
├── py.typed                 # Type hints marker
│
├── easy/                    # Simple one-liner functions
│   ├── __init__.py
│   ├── ask.py               # ask() - basic Q&A
│   ├── summarize.py         # summarize() - text summarization
│   ├── extract.py           # extract() - structured data extraction
│   ├── translate.py         # translate() - language translation
│   ├── generate.py          # generate() - content generation
│   ├── chat.py              # chat() - conversational interface
│   ├── research.py          # research() - multi-source research
│   ├── code.py              # code() - code generation/explanation
│   ├── rag.py               # rag() - retrieval augmented generation
│   ├── agent_factory.py     # agent() - custom agent creation
│   ├── handoff.py           # handoff() - agent handoffs
│   ├── guardrails.py        # guardrails - input/output validation
│   ├── mcp.py               # mcp - Model Context Protocol
│   ├── trace.py             # trace - execution tracing
│   ├── config.py            # Global configuration
│   └── llm_interface.py     # LLM abstraction layer
│
├── core/                    # Foundation classes
│   ├── agent.py             # Agent base class
│   ├── base.py              # Abstract bases
│   ├── llm.py               # LLM provider abstraction
│   └── memory.py            # Memory/conversation management
│
├── skills/                  # Agent capabilities
│   ├── skill.py             # Skill base class
│   ├── tool_skill.py        # Tool-based skills
│   ├── action_skill.py      # Action-based skills
│   ├── registry.py          # Skill registry
│   └── builtin.py           # Built-in skills
│
├── instructions/            # Prompt engineering
│   ├── instruction.py       # Instruction class
│   ├── system_prompt.py     # System prompt builder
│   ├── context.py           # Context management
│   ├── persona.py           # Persona definitions
│   └── guidelines.py        # Behavior guidelines
│
├── blueprint/               # Agent design patterns
│   ├── blueprint.py         # Blueprint class
│   ├── orchestrator.py      # Multi-agent orchestration
│   ├── workflow.py          # Workflow definitions
│   ├── pipeline.py          # Processing pipelines
│   └── patterns.py          # Common patterns
│
├── orchestrator/            # Enterprise orchestration
│   └── __init__.py          # Task, Workflow, Patterns
│
├── integrations/            # External framework adapters
│   ├── langchain_adapter.py # LangChain integration
│   ├── semantic_kernel_adapter.py # SK integration
│   └── vector_db.py         # Vector database connectors
│
└── usecases/                # Industry templates
    ├── __init__.py          # General use cases
    └── industry.py          # Industry-specific agents
```

---

## 3. Data Flow Architecture

### Request Processing Flow

```
┌─────────────────────────────────────────────────────────────────────────┐
│                           REQUEST FLOW                                   │
└─────────────────────────────────────────────────────────────────────────┘

User Request
     │
     ▼
┌─────────────────────┐
│   Configuration     │─────────────────────────────────────────┐
│   (config.py)       │                                          │
└─────────┬───────────┘                                          │
          │                                                       │
          ▼                                                       │
┌─────────────────────┐                                          │
│   Input Guardrails  │◄────────────────────────────────────┐    │
│   (guardrails.py)   │                                      │    │
└─────────┬───────────┘                                      │    │
          │ PASS                                              │    │
          │                                                   │    │
          ▼                                                   │    │
┌─────────────────────┐                                      │    │
│   Tracing Start     │                                      │    │
│   (trace.py)        │                                      │    │
└─────────┬───────────┘                                      │    │
          │                                                   │    │
          ▼                                                   │    │
┌─────────────────────┐     ┌─────────────────────┐         │    │
│   Easy Function     │────►│   Agent Factory     │         │    │
│   (ask, summarize)  │     │   (agent_factory.py)│         │    │
└─────────┬───────────┘     └─────────┬───────────┘         │    │
          │                           │                       │    │
          │                           ▼                       │    │
          │                 ┌─────────────────────┐         │    │
          │                 │   SimpleAgent       │         │    │
          │                 │   - instructions    │         │    │
          │                 │   - memory          │         │    │
          │                 │   - model           │         │    │
          │                 └─────────┬───────────┘         │    │
          │                           │                       │    │
          └───────────────┬───────────┘                       │    │
                          │                                   │    │
                          ▼                                   │    │
                ┌─────────────────────┐                      │    │
                │   LLM Interface     │                      │    │
                │   (llm_interface.py)│                      │    │
                └─────────┬───────────┘                      │    │
                          │                                   │    │
          ┌───────────────┴───────────────┐                  │    │
          ▼                               ▼                   │    │
┌─────────────────────┐     ┌─────────────────────┐         │    │
│   Azure OpenAI      │     │   OpenAI            │         │    │
│   (AD Auth)         │     │   (API Key)         │         │    │
└─────────┬───────────┘     └─────────┬───────────┘         │    │
          │                           │                       │    │
          └───────────────┬───────────┘                       │    │
                          │                                   │    │
                          ▼                                   │    │
                ┌─────────────────────┐                      │    │
                │   LLM Response      │                      │    │
                └─────────┬───────────┘                      │    │
                          │                                   │    │
                          ▼                                   │    │
                ┌─────────────────────┐                      │    │
                │   Output Guardrails │◄─────────────────────┘    │
                │   (guardrails.py)   │                           │
                └─────────┬───────────┘                           │
                          │ PASS                                   │
                          │                                        │
                          ▼                                        │
                ┌─────────────────────┐                           │
                │   Tracing End       │◄──────────────────────────┘
                │   (trace.py)        │
                └─────────┬───────────┘
                          │
                          ▼
                ┌─────────────────────┐
                │   User Response     │
                └─────────────────────┘
```

### Multi-Agent Handoff Flow

```
┌─────────────────────────────────────────────────────────────────────────┐
│                       HANDOFF ARCHITECTURE                               │
└─────────────────────────────────────────────────────────────────────────┘

                          ┌─────────────────┐
                          │   User Input    │
                          └────────┬────────┘
                                   │
                                   ▼
                    ┌──────────────────────────┐
                    │     Triage Agent         │
                    │  "Route to appropriate   │
                    │   specialist"            │
                    └──────────────┬───────────┘
                                   │
           ┌───────────────────────┼───────────────────────┐
           │                       │                       │
           ▼                       ▼                       ▼
┌──────────────────┐   ┌──────────────────┐   ┌──────────────────┐
│  Sales Agent     │   │  Support Agent   │   │  Technical Agent │
│                  │   │                  │   │                  │
│  "I handle       │   │  "I handle       │   │  "I handle       │
│   pricing..."    │   │   issues..."     │   │   code..."       │
└──────────────────┘   └──────────────────┘   └──────────────────┘
           │                       │                       │
           └───────────────────────┼───────────────────────┘
                                   │
                                   ▼
                    ┌──────────────────────────┐
                    │   Final Response         │
                    │   (with handoff_log)     │
                    └──────────────────────────┘
```

---

## 4. Extension Points

### Custom Model Providers

```python
from PyAI.core.llm import LLMProvider

class CustomProvider(LLMProvider):
    def complete(self, prompt: str, **kwargs) -> LLMResponse:
        # Your implementation
        pass
    
    def chat(self, messages: list, **kwargs) -> LLMResponse:
        # Your implementation
        pass
```

### Custom Guardrails

```python
from PyAI import guardrails

@guardrails.validator("no_secrets")
def check_no_secrets(text: str) -> GuardrailResult:
    patterns = [r"password\s*[=:]\s*\S+", r"api_key\s*[=:]\s*\S+"]
    for pattern in patterns:
        if re.search(pattern, text, re.IGNORECASE):
            return GuardrailResult(passed=False, message="Secrets detected")
    return GuardrailResult(passed=True)
```

### Custom Skills

```python
from PyAI.skills import Skill, skill

@skill("web_search")
class WebSearchSkill(Skill):
    async def execute(self, query: str) -> str:
        # Search implementation
        return results
```

---

## 5. Security Architecture

### Authentication Flow (Azure)

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    AZURE AD AUTHENTICATION                               │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────┐                          ┌─────────────────┐
│                 │  1. Request Token        │                 │
│   PyAI App   │ ─────────────────────►   │   Azure AD      │
│                 │                          │                 │
│                 │  2. Access Token         │                 │
│                 │ ◄─────────────────────   │                 │
└────────┬────────┘                          └─────────────────┘
         │
         │ 3. API Call with Bearer Token
         │
         ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                    AZURE OPENAI SERVICE                                  │
│  ┌─────────────────┐                                                    │
│  │ Validate Token  │                                                    │
│  │ Check RBAC      │                                                    │
│  │ Process Request │                                                    │
│  └─────────────────┘                                                    │
└─────────────────────────────────────────────────────────────────────────┘
```

### Guardrails Security

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    SECURITY GUARDRAILS                                   │
└─────────────────────────────────────────────────────────────────────────┘

INPUT                     PROCESSING                    OUTPUT
  │                           │                           │
  ▼                           │                           ▼
┌───────────────┐            │            ┌───────────────┐
│ no_pii        │            │            │ filter_output │
│ - SSN         │            │            │ - redact_pii  │
│ - Email       │            │            │ - clean_html  │
│ - Phone       │            │            │ - sanitize    │
├───────────────┤            │            ├───────────────┤
│ no_injection  │            │            │ no_secrets    │
│ - Jailbreak   │     ┌──────┴──────┐    │ - API keys    │
│ - Override    │     │    LLM      │    │ - Passwords   │
│ - DAN mode    │────►│  Processing │───►│ - Tokens      │
├───────────────┤     └─────────────┘    ├───────────────┤
│ no_harmful    │                        │ length_limit  │
│ - Violence    │                        │ - Truncate    │
│ - Hate        │                        │ - Summarize   │
└───────────────┘                        └───────────────┘
```

---

## 6. Deployment Patterns

### Development Setup

```bash
# Clone and setup
git clone https://github.com/gitpavleenbali/PyAI.git
cd PyAI
pip install -e ".[dev]"

# Configure Azure
export AZURE_OPENAI_ENDPOINT="https://your-resource.openai.azure.com"
export AZURE_OPENAI_DEPLOYMENT="gpt-4o-mini"
az login

# Run tests
pytest tests/ -v
```

### Production Deployment

```yaml
# Azure Container Apps
apiVersion: apps/v1
kind: Deployment
metadata:
  name: PyAI-service
spec:
  replicas: 3
  template:
    spec:
      containers:
      - name: PyAI
        image: your-registry/PyAI:latest
        env:
        - name: AZURE_OPENAI_ENDPOINT
          valueFrom:
            secretKeyRef:
              name: azure-secrets
              key: endpoint
```

---

## 7. Performance Considerations

### Caching Strategy

```
┌─────────────────────────────────────────────────────────────────────────┐
│                       CACHING ARCHITECTURE                               │
└─────────────────────────────────────────────────────────────────────────┘

Request ──► Hash(prompt + model + params)
                      │
                      ▼
               ┌──────────────┐
               │ Cache Lookup │
               └──────┬───────┘
                      │
            ┌─────────┴─────────┐
            │                   │
         HIT ▼                  ▼ MISS
    ┌──────────────┐    ┌──────────────┐
    │ Return       │    │ LLM Call     │
    │ Cached       │    │ Store Result │
    └──────────────┘    └──────────────┘
```

### Rate Limiting

```python
# Built into LLM interface
llm = LLMInterface(
    rate_limit="60/minute",
    retry_strategy="exponential_backoff",
    timeout=30
)
```

---

## 8. Observability

### Tracing Integration

```
┌─────────────────────────────────────────────────────────────────────────┐
│                      TRACE/SPAN HIERARCHY                                │
└─────────────────────────────────────────────────────────────────────────┘

agent_run (span)
├── guardrails_input (span)
│   ├── no_pii (event)
│   └── no_injection (event)
├── llm_call (span)
│   ├── request (event)
│   ├── tokens: {input: 100, output: 50}
│   └── response (event)
├── tool_execution (span)
│   └── search_web (event)
├── guardrails_output (span)
│   └── filter_output (event)
└── response (span)
```

---

*This document is maintained by the PyAI Architecture Team and updated with each major release.*
