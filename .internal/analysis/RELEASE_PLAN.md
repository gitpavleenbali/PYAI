# PyAI v0.4.0 Release Plan

> **Sprint Duration:** February 2026  
> **Goal:** Close all critical gaps identified in competitor analysis  
> **Target:** Feature parity with ALL competitors + unique PyAI advantages  
> **Status:** ✅ COMPLETED - All Phase 1, 2, 3, and 4 features implemented

---

## 🎉 Release Completion Summary

**Version 0.4.0 is ready for release!**

### Phase 1 Features (v0.3.0)
| Feature | Status | Tests |
|---------|--------|-------|
| Runner Pattern (OpenAI) | ✅ Implemented | ✅ 29 tests |
| Agent Config YAML (Google ADK) | ✅ Implemented | ✅ 24 tests |
| Agents as Plugins (MS Semantic Kernel) | ✅ Implemented | ✅ 22 tests |
| OpenAPI Tools (Google ADK) | ✅ Implemented | ✅ 40 tests |
| Token Counting (Anthropic) | ✅ Implemented | ✅ 40 tests |
| src/ Layout Migration | ✅ Complete | N/A |
| Models Module Tests | ✅ Complete | ✅ 33 tests |
| Sessions Module Tests | ✅ Complete | ✅ 33 tests |
| Evaluation Module Tests | ✅ Complete | ✅ 36 tests |

### Phase 2 Features (v0.4.0)
| Feature | Status | Tests |
|---------|--------|-------|
| Tool Auto-Discovery (Strands) | ✅ Implemented | ✅ 12 tests |
| Context Caching (Google ADK) | ✅ Implemented | ✅ 7 tests |
| Session Rewind/Checkpoints | ✅ Implemented | ✅ 6 tests |
| Multimodal Vision (GPT-4o) | ✅ Implemented | ✅ 12 tests |
| Vector DB Connectors (5 DBs) | ✅ Implemented | ✅ 7 tests |

### Phase 3 Features (v0.4.0)
| Feature | Status | Tests |
|---------|--------|-------|
| A2A Protocol (Google ADK) | ✅ Implemented | ✅ 12 tests |
| Development UI (Workbench) | ✅ Implemented | ✅ 9 tests |
| Voice Streaming (OpenAI Realtime) | ✅ Implemented | ✅ 10 tests |

### Phase 4 Features (v0.4.0)
| Feature | Status | Tests |
|---------|--------|-------|
| Kernel Registry Pattern (MS Semantic Kernel) | ✅ Implemented | ✅ 35 tests |

**Total Test Count: 671 tests passing (636 core + 35 kernel)**

---

## Executive Summary

Based on our [Competitor Analysis](./COMPETITOR_ANALYSIS.md), we identified 25+ gaps against 5 major competitors:
- OpenAI Agents SDK (18.9k⭐)
- Anthropic SDK (2.8k⭐)
- Strands Agents (5.1k⭐)
- Google ADK (17.7k⭐)
- Microsoft Semantic Kernel (27.2k⭐)

This release plan systematically addresses each gap with implementation details, tests, and timeline.

---

## ✅ Phase 0: Already Completed (v0.2.0)

The following modules were created to address initial gaps:

| Module | Gap Addressed | Status | Tests |
|--------|--------------|--------|-------|
| `models/` | Multi-provider support (7 providers) | ✅ Done | ✅ 33 tests |
| `sessions/` | SQLite/Redis sessions | ✅ Done | ✅ 33 tests |
| `evaluation/` | Agent evaluation (like `adk eval`) | ✅ Done | ✅ 36 tests |
| `cli/` | CLI commands (`PyAI run/eval/serve`) | ✅ Done | ✅ Has tests |
| `code_executor/` | Safe code execution sandbox | ✅ Done | ✅ Has tests |
| `errors/` | Structured error hierarchy | ✅ Done | ✅ Has tests |

**All modules have comprehensive test coverage!**

---

## ✅ Phase 1: Critical Gaps (High Priority) - COMPLETED

### 1.1 Structured Runner Pattern ✅
**Gap Source:** OpenAI Agents SDK  
**Status:** ✅ Implemented in `src/PyAI/runner/`

```python
# Implemented API
from PyAI import Runner, RunConfig, RunResult

config = RunConfig(max_turns=5, timeout=30)
result = Runner.run(agent, "Hello", config=config)
```

**Files Created:**
- [x] `src/PyAI/runner/executor.py` - Runner, RunConfig, RunResult
- [x] `src/PyAI/runner/streaming.py` - StreamingRunner
- [x] `tests/test_runner.py` - 29 tests

**Tests:** 29/29 passing

---

### 1.2 OpenAPI Tool Auto-Generation ✅
**Gap Source:** Google ADK  
**Status:** ✅ Implemented in `src/PyAI/openapi/`

```python
# Implemented API
from PyAI import OpenAPITools, create_tools_from_openapi

api = OpenAPITools("petstore.yaml", base_url="https://api.example.com")
tools = api.tools
result = api.call("listPets", limit=5)
```

**Files Created:**
- [x] `src/PyAI/openapi/parser.py` - OpenAPI spec parser
- [x] `src/PyAI/openapi/client.py` - HTTP client
- [x] `src/PyAI/openapi/tools.py` - Tool generation
- [x] `tests/test_openapi.py` - 40 tests

**Tests:** 40/40 passing

---

### 1.3 Agent Config (No-Code Agents) ✅
**Gap Source:** Google ADK  
**Status:** ✅ Implemented in `src/PyAI/config/`

```python
# Implemented API
from PyAI import load_agent, AgentBuilder, AgentConfig

# Load from YAML/JSON
agent = load_agent("agent.yaml")

# Or use builder
config = AgentConfig(
    name="helper",
    model="gpt-4",
    instructions="You are helpful"
)
agent = AgentBuilder.build(config)
```

**Files Created:**
- [x] `src/PyAI/config/schema.py` - Config schema validation
- [x] `src/PyAI/config/loader.py` - YAML/JSON loader
- [x] `src/PyAI/config/builder.py` - Agent builder
- [x] `tests/test_config.py` - 24 tests

**Tests:** 24/24 passing

---

### 1.4 Agents as Plugins Pattern ✅
**Gap Source:** Microsoft Semantic Kernel  
**Status:** ✅ Implemented in `src/PyAI/plugins/`

```python
# Implemented API
from PyAI import Plugin, PluginRegistry

# Create plugins
@plugin
class WeatherPlugin:
    @function(description="Get weather")
    def get_weather(self, city: str) -> str:
        return f"Weather in {city}: sunny"

# Register plugins
registry = PluginRegistry()
registry.register(WeatherPlugin())

# Use with agent
tools = registry.get_all_tools()
```

**Files Created:**
- [x] `src/PyAI/plugins/base.py` - Plugin base classes
- [x] `src/PyAI/plugins/registry.py` - Plugin registry
- [x] `src/PyAI/plugins/decorators.py` - @plugin, @function decorators
- [x] `src/PyAI/plugins/loader.py` - Plugin loading
- [x] `tests/test_plugins.py` - 22 tests

**Tests:** 22/22 passing

---

### 1.5 Token Counting Utility ✅
**Gap Source:** Anthropic SDK  
**Status:** ✅ Implemented in `src/PyAI/tokens/`

```python
# Implemented API
from PyAI import TokenCounter, count_tokens, calculate_cost, CostTracker

# Count tokens
counter = TokenCounter("gpt-4")
count = counter.count_messages(messages, completion="response")

# Calculate cost
cost = calculate_cost(count, model="gpt-4")
print(f"Cost: ${cost.total_cost:.4f}")

# Track costs over time
tracker = CostTracker("gpt-4")
tracker.add(1000, 500)  # input, output tokens
print(tracker.summary())
```

**Files Created:**
- [x] `src/PyAI/tokens/counter.py` - Token counting with tiktoken
- [x] `src/PyAI/tokens/cost.py` - Cost calculation
- [x] `tests/test_tokens.py` - 40 tests

**Tests:** 40/40 passing

---

## ✅ Phase 2: Important Gaps (Medium Priority) - COMPLETED

### 2.1 Tool Auto-Discovery from Directory ✅
**Gap Source:** Strands Agents  
**Status:** ✅ Implemented in `src/PyAI/tools/`

```python
# Implemented API
from PyAI import Agent, ToolDiscovery, ToolWatcher, tool, discover_tools

# Auto-discover tools from directory
tools = discover_tools("./my_tools/")

# Or use discovery class
discovery = ToolDiscovery()
discovery.scan("./my_tools/")
tools = discovery.get_all_tools()

# Hot-reload with watcher
watcher = ToolWatcher("./my_tools/")
watcher.on_change(lambda: print("Tools updated!"))
watcher.start()

# Create tools with decorator
@tool(name="my_tool", description="Does something")
def my_func(x: int) -> str:
    return str(x)
```

**Files Created:**
- [x] `src/PyAI/tools/base.py` - Tool class, @tool decorator, ToolResult
- [x] `src/PyAI/tools/discovery.py` - ToolDiscovery class
- [x] `src/PyAI/tools/watcher.py` - ToolWatcher with hot-reload
- [x] `src/PyAI/tools/__init__.py` - Module exports
- [x] `tests/test_phase2_phase3.py` - 12 tool tests

**Tests:** 12/12 passing

---

### 2.2 Context Caching ✅
**Gap Source:** Google ADK  
**Status:** ✅ Implemented in `src/PyAI/core/cache.py`

```python
# Implemented API
from PyAI import ContextCache, cache_context

# Create cache with TTL
cache = ContextCache(ttl=3600, max_entries=1000)

# Set/get values
cache.set("key", "value")
value = cache.get("key", default=None)

# Cache decorator
@cache.cached
def expensive_operation():
    return "result"

# Get cache stats
stats = cache.stats  # {"hits": 10, "misses": 2, "size": 5}
```

**Files Created:**
- [x] `src/PyAI/core/cache.py` - ContextCache, CacheEntry, @cached decorator
- [x] `tests/test_phase2_phase3.py` - 7 cache tests

**Tests:** 7/7 passing

---

### 2.3 Session Rewind ✅
**Gap Source:** Google ADK  
**Status:** ✅ Implemented in `src/PyAI/sessions/base.py`

```python
# Implemented API
from PyAI.sessions import Session, SessionCheckpoint

session = Session()
session.add_user_message("Hello")

# Create checkpoint
cp = session.checkpoint("before_research")

session.add_assistant_message("Response")
session.add_user_message("Follow up")

# Rewind to checkpoint
session.rewind_to_checkpoint(cp.id)
session.rewind_to_checkpoint_by_name("before_research")

# Or rewind N messages
session.rewind_n_messages(2)

# Get all checkpoints
checkpoints = session.get_checkpoints()
```

**Files Modified:**
- [x] `src/PyAI/sessions/base.py` - Added SessionCheckpoint, checkpoint(), rewind methods
- [x] `src/PyAI/sessions/__init__.py` - Export SessionCheckpoint
- [x] `tests/test_phase2_phase3.py` - 6 session checkpoint tests

**Tests:** 6/6 passing

---

### 2.4 Multimodal Support (Vision) ✅
**Gap Source:** Google ADK, MS Semantic Kernel  
**Status:** ✅ Implemented in `src/PyAI/multimodal/`

```python
# Implemented API
from PyAI import Image, Audio, Video, MultimodalContent

# Create images
img = Image.from_file("photo.jpg")
img = Image.from_url("https://example.com/image.png")
img = Image.from_base64(data, media_type="image/png")

# Convert to provider formats
openai_format = img.to_openai_format()
anthropic_format = img.to_anthropic_format()

# Audio support
audio = Audio.from_file("speech.mp3")
audio = Audio.from_base64(data, format=AudioFormat.WAV)

# Compose multimodal content
content = (
    MultimodalContent()
    .add_text("What's in this image?")
    .add_image(img)
)
```

**Files Created:**
- [x] `src/PyAI/multimodal/image.py` - Image class with from_url, from_file, from_base64
- [x] `src/PyAI/multimodal/audio.py` - Audio class with format support
- [x] `src/PyAI/multimodal/video.py` - Video class with frame extraction
- [x] `src/PyAI/multimodal/content.py` - MultimodalContent builder
- [x] `src/PyAI/multimodal/__init__.py` - Module exports
- [x] `tests/test_phase2_phase3.py` - 12 multimodal tests

**Tests:** 12/12 passing

---

### 2.5 More Vector DB Connectors ✅
**Gap Source:** MS Semantic Kernel  
**Status:** ✅ Implemented in `src/PyAI/vectordb/`

```python
# Implemented API
from PyAI import (
    VectorStore, Document, SearchResult,
    MemoryVectorStore, ChromaStore, PineconeStore,
    WeaviateStore, QdrantStore
)

# In-memory store for testing
store = MemoryVectorStore()
store.add("doc1", "Hello world", {"source": "test"})
results = store.search("hello", k=3)

# ChromaDB
store = ChromaStore(collection="my-docs")

# Pinecone
store = PineconeStore(index="my-index", api_key="...")

# Weaviate
store = WeaviateStore(url="http://localhost:8080", class_name="Document")

# Qdrant
store = QdrantStore(url="http://localhost:6333", collection="docs")

# Unified interface
doc = Document.create("content", source="file.txt")
store.add_document(doc)
results = store.search("query", k=5)
```

**Files Created:**
- [x] `src/PyAI/vectordb/base.py` - VectorStore ABC, Document, SearchResult, embeddings
- [x] `src/PyAI/vectordb/memory.py` - MemoryVectorStore for testing
- [x] `src/PyAI/vectordb/chroma.py` - ChromaDB connector
- [x] `src/PyAI/vectordb/pinecone.py` - Pinecone connector
- [x] `src/PyAI/vectordb/weaviate.py` - Weaviate connector
- [x] `src/PyAI/vectordb/qdrant.py` - Qdrant connector
- [x] `src/PyAI/vectordb/__init__.py` - Module exports
- [x] `tests/test_phase2_phase3.py` - 7 vectordb tests

**Tests:** 7/7 passing

---

## ✅ Phase 3: Advanced Gaps (High Priority) - COMPLETED

### 3.1 A2A Protocol Support ✅
**Gap Source:** Google ADK  
**Status:** ✅ Implemented in `src/PyAI/a2a/`

```python
# Implemented API
from PyAI import (
    A2AServer, A2AClient, RemoteAgent, AgentCard,
    A2ATask, A2AResponse, AgentRegistry
)

# Create agent card
card = AgentCard(
    name="research-agent",
    description="Research assistant",
    skills=["research", "summarize"],
    url="https://agent.example.com"
)

# Server side
server = A2AServer(port=8000)
server.register(agent, card)
server.start()

# Client side
client = A2AClient("https://agent.example.com")
result = await client.send_task(A2ATask.from_text("Research AI"))

# Remote agent wrapper
remote = RemoteAgent.from_url("https://agent.example.com")
result = await remote.run("Do research")

# Agent discovery
registry = AgentRegistry.get_default()
agents = registry.discover_from_env()
```

**Files Created:**
- [x] `src/PyAI/a2a/protocol.py` - AgentCard, A2AMessage, A2ATask, A2AResponse
- [x] `src/PyAI/a2a/server.py` - A2AServer, A2AEndpoint
- [x] `src/PyAI/a2a/client.py` - A2AClient, RemoteAgent
- [x] `src/PyAI/a2a/registry.py` - AgentRegistry for discovery
- [x] `src/PyAI/a2a/__init__.py` - Module exports
- [x] `tests/test_phase2_phase3.py` - 12 A2A tests

**Tests:** 12/12 passing

---

### 3.2 Development UI ✅
**Gap Source:** Google ADK, Anthropic Workbench  
**Status:** ✅ Implemented in `src/PyAI/devui/`

```python
# Implemented API
from PyAI import DevUI, launch_ui, AgentDashboard, AgentDebugger

# Quick launch UI for agent
launch_ui(agent, port=8080)

# Custom UI with handler
ui = DevUI(title="My Agent", theme="dark")
ui.set_handler(lambda msg: agent.run(msg))
ui.start()

# Dashboard for metrics
dashboard = AgentDashboard()
dashboard.track(agent)
dashboard.record_run(
    input="Hello",
    output="Hi",
    started_at=datetime.utcnow(),
    ended_at=datetime.utcnow()
)
metrics = dashboard.get_metrics()

# Debugger with breakpoints
debugger = AgentDebugger()
bp_id = debugger.add_breakpoint("tool_call")
debugger.log(DebugEvent.RUN_START, {"input": "test"})
history = debugger.get_history()
```

**Files Created:**
- [x] `src/PyAI/devui/ui.py` - DevUI class, launch_ui() function
- [x] `src/PyAI/devui/dashboard.py` - AgentDashboard, AgentMetrics, RunRecord
- [x] `src/PyAI/devui/debugger.py` - AgentDebugger with breakpoints
- [x] `src/PyAI/devui/__init__.py` - Module exports
- [x] `tests/test_phase2_phase3.py` - 9 devui tests

**Tests:** 9/9 passing

---

### 3.3 Voice/Bidirectional Streaming ✅
**Gap Source:** OpenAI Realtime API, Strands, Google ADK  
**Status:** ✅ Implemented in `src/PyAI/voice/`

```python
# Implemented API
from PyAI import (
    VoiceSession, AudioStream, Transcriber, Synthesizer,
    AudioChunk, DuplexAudioStream
)

# Audio streaming
stream = AudioStream()
stream.add(AudioChunk(data=b"...", format=AudioFormat.PCM16))

# Duplex streaming
duplex = DuplexAudioStream()
duplex.send(chunk)
received = duplex.receive()

# Voice session
session = VoiceSession(
    model="gpt-4o-realtime",
    voice="alloy",
    on_transcript=lambda t: print(t),
    on_audio=lambda a: play(a)
)
await session.start()
await session.send_audio(audio_data)
await session.send_text("Hello")

# Speech-to-text
transcriber = Transcriber(model="whisper-1")
result = await transcriber.transcribe(audio_data)
print(result.text)

# Text-to-speech
synthesizer = Synthesizer(voice="nova")
audio = await synthesizer.synthesize("Hello world")
```

**Files Created:**
- [x] `src/PyAI/voice/stream.py` - AudioChunk, AudioStream, DuplexAudioStream
- [x] `src/PyAI/voice/session.py` - VoiceSession for real-time audio
- [x] `src/PyAI/voice/transcription.py` - Transcriber (Whisper)
- [x] `src/PyAI/voice/synthesis.py` - Synthesizer (OpenAI TTS)
- [x] `src/PyAI/voice/__init__.py` - Module exports
- [x] `tests/test_phase2_phase3.py` - 10 voice tests

**Tests:** 10/10 passing

---

### 3.4 Multi-Language SDKs
**Gap Source:** Google ADK, MS Semantic Kernel  
**Description:** TypeScript, Go SDKs  
**Effort:** Extreme (100+ hours each)  
**Timeline:** v1.0.0+

---

## 📋 Test Suite Requirements

### New Test Files Needed

| Test File | Module | Priority |
|-----------|--------|----------|
| `tests/test_models.py` | models/ | High |
| `tests/test_sessions.py` | sessions/ | High |
| `tests/test_evaluation.py` | evaluation/ | High |
| `tests/test_cli.py` | cli/ | Medium |
| `tests/test_code_executor.py` | code_executor/ | Medium |
| `tests/test_errors.py` | errors/ | Low |
| `tests/test_runner.py` | core/runner | High |
| `tests/test_openapi_tools.py` | tools/openapi | High |
| `tests/test_agent_config.py` | config/ | High |
| `tests/test_agent_plugins.py` | core/plugins | High |
| `tests/test_tokens.py` | utils/tokens | Low |

---

## 📁 Project Structure Recommendation

### Question: Should we use `src/` folder?

**Analysis:**

| SDK | Uses src/ | Structure |
|-----|-----------|-----------|
| OpenAI Agents | ✅ Yes | `src/agents/` |
| Google ADK | ✅ Yes | `src/google/adk/` |
| Strands | ✅ Yes | `src/strands/` |
| Anthropic SDK | ✅ Yes | `src/anthropic/` |
| MS Semantic Kernel | ✅ Yes | `python/semantic_kernel/` |

**Recommendation:** **YES**, adopt `src/` layout for:
1. Industry standard (all competitors use it)
2. Cleaner separation of source from tests/docs
3. Better packaging hygiene
4. Avoids accidental local imports during testing

**Proposed New Structure:**
```
pyai/
├── src/
│   └── PyAI/
│       ├── __init__.py
│       ├── core/
│       ├── easy/
│       ├── models/
│       ├── sessions/
│       ├── evaluation/
│       ├── cli/
│       ├── tools/       # NEW
│       ├── config/      # NEW
│       ├── utils/       # NEW
│       └── ...
├── tests/
├── docs/
├── examples/
├── analysis/
├── architecture/
├── pyproject.toml
└── README.md
```

**Migration Steps:**
1. Create `src/` directory
2. Move `PyAI/` into `src/`
3. Update `pyproject.toml` for src layout
4. Update all imports in tests
5. Verify tests pass

---

## 🚀 Implementation Order

### Sprint 1: Foundation & Tests (2-3 hours)
1. [ ] Write tests for existing modules (models, sessions, evaluation)
2. [ ] Migrate to `src/` layout
3. [ ] Verify all tests pass

### Sprint 2: Critical Features (4-6 hours)
1. [ ] Implement Runner pattern
2. [ ] Implement Agent Config (YAML/JSON)
3. [ ] Implement Agents as Plugins
4. [ ] Write tests for each

### Sprint 3: Tools & Utilities (3-4 hours)
1. [ ] Implement OpenAPI tool generation
2. [ ] Implement Token counting
3. [ ] Implement Tool auto-discovery
4. [ ] Write tests for each

### Sprint 4: Advanced Features (4-5 hours)
1. [ ] Implement Context caching
2. [ ] Implement Session rewind
3. [ ] Add more vector DB connectors
4. [ ] Write tests for each

### Sprint 5: Multimodal & Polish (4-5 hours)
1. [ ] Implement Vision support
2. [ ] Update competitor analysis
3. [ ] Update documentation
4. [ ] Full test suite run

---

## 📊 Success Metrics

After completing this release:

| Metric | Before | After |
|--------|--------|-------|
| Features vs OpenAI Agents | 75% | 95% |
| Features vs Google ADK | 60% | 90% |
| Features vs MS SK | 70% | 95% |
| LLM Providers Supported | 2 | 7+ |
| Session Backends | 1 | 3 |
| Test Coverage | ~50% | 85%+ |
| CLI Commands | 0 | 5+ |

---

## 🎯 Definition of Done

A feature is complete when:
1. ✅ Code implemented
2. ✅ Unit tests written and passing
3. ✅ Documentation updated
4. ✅ Example added to examples/
5. ✅ No regressions in existing tests

---

*Document Version: 1.0*  
*Created: February 2026*
