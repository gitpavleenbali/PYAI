# 💾 Sessions Module

The **sessions/** module provides persistent storage for conversations and agent state.

---

## Module Overview

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': 'transparent', 'primaryTextColor': '#ffffff', 'primaryBorderColor': '#ffffff', 'lineColor': '#ffffff', 'secondaryColor': 'transparent', 'tertiaryColor': 'transparent', 'background': 'transparent', 'mainBkg': 'transparent', 'nodeBorder': '#ffffff', 'clusterBkg': 'transparent', 'clusterBorder': '#ffffff', 'titleColor': '#ffffff', 'edgeLabelBackground': 'transparent', 'nodeTextColor': '#ffffff'}}}%%
flowchart TB
    subgraph Sessions["sessions/ Module"]
        SM["SessionManager"] --> SS["SessionStore"]
        
        SS --> SQL["SQLiteSessionStore"]
        SS --> RD["RedisSessionStore"]
        SS --> MEM["MemorySessionStore"]
        
        S["Session"] --> MSG["Messages"]
        S --> META["Metadata"]
        S --> STATE["State"]
    end
```

---

## File Structure

```
src/pyai/sessions/
├── __init__.py
├── base.py          # Session and Store base classes
├── manager.py       # SessionManager
├── sqlite.py        # SQLite storage
├── redis.py         # Redis storage
└── memory.py        # In-memory storage
```

---

## SessionManager

Central interface for session management.

### Basic Usage

```python
from pyai.sessions import SessionManager, SQLiteSessionStore

# Create manager with SQLite storage
manager = SessionManager(
    store=SQLiteSessionStore("sessions.db")
)

# Create a session
session = manager.create_session(user_id="user123")

# Add messages
session.add_message("user", "Hello!")
session.add_message("assistant", "Hi there!")

# Save session
manager.save(session)

# Later: retrieve session
session = manager.get_session(session.session_id)
```

---

## Session Object

Represents a conversation session with full state.

```python
from pyai.sessions import Session

session = Session(
    session_id="sess_abc123",
    user_id="user123",
    metadata={"channel": "web", "language": "en"}
)

# Add messages
session.add_message("user", "What is PYAI?")
session.add_message("assistant", "PYAI is an intelligence engine.")

# Access messages
for msg in session.messages:
    print(f"{msg.role}: {msg.content}")

# Store custom state
session.set_state("last_topic", "PYAI")
topic = session.get_state("last_topic")

# Session info
print(session.created_at)
print(session.updated_at)
print(session.message_count)
```

---

## Storage Backends

### SQLiteSessionStore

Local file-based storage. Great for development and single-server deployments.

```python
from pyai.sessions import SQLiteSessionStore

store = SQLiteSessionStore(
    path="sessions.db",
    table_name="sessions"
)
```

### RedisSessionStore

Distributed storage for multi-server deployments.

```python
from pyai.sessions import RedisSessionStore

store = RedisSessionStore(
    url="redis://localhost:6379",
    prefix="pyai:sessions:",
    ttl=86400  # 24 hours
)
```

### MemorySessionStore

In-memory storage for testing and development.

```python
from pyai.sessions import MemorySessionStore

store = MemorySessionStore()  # Cleared on restart
```

---

## Storage Comparison

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': 'transparent', 'primaryTextColor': '#ffffff', 'primaryBorderColor': '#ffffff', 'lineColor': '#ffffff', 'secondaryColor': 'transparent', 'tertiaryColor': 'transparent', 'background': 'transparent', 'mainBkg': 'transparent', 'nodeBorder': '#ffffff', 'clusterBkg': 'transparent', 'clusterBorder': '#ffffff', 'titleColor': '#ffffff', 'edgeLabelBackground': 'transparent', 'nodeTextColor': '#ffffff'}}}%%
flowchart LR
    subgraph Backends["Storage Backends"]
        subgraph SQLite["SQLite"]
            SQ1["File-based"]
            SQ2["Single server"]
            SQ3["Zero setup"]
        end
        
        subgraph Redis["Redis"]
            R1["Distributed"]
            R2["Multi-server"]
            R3["TTL support"]
        end
        
        subgraph Memory["Memory"]
            M1["In-process"]
            M2["Testing"]
            M3["Fastest"]
        end
    end
```

| Feature | SQLite | Redis | Memory |
|---------|--------|-------|--------|
| Persistence | ✅ | ✅ | ❌ |
| Distributed | ❌ | ✅ | ❌ |
| Setup | Zero | Server needed | Zero |
| Speed | Fast | Very fast | Fastest |
| Use case | Dev, single server | Production | Testing |

---

## Using with Agents

```python
from pyai import Agent, Runner
from pyai.sessions import SessionManager, SQLiteSessionStore

# Setup
manager = SessionManager(store=SQLiteSessionStore("chat.db"))

# Create agent
agent = Agent(
    name="Assistant",
    instructions="You are helpful."
)

# Chat with session persistence
async def chat(user_id: str, message: str):
    # Get or create session
    sessions = manager.get_sessions_for_user(user_id)
    session = sessions[0] if sessions else manager.create_session(user_id)
    
    # Get history for context
    history = [
        {"role": msg.role, "content": msg.content}
        for msg in session.messages
    ]
    
    # Run agent with history
    result = await Runner.run_async(agent, message, history=history)
    
    # Store conversation
    session.add_message("user", message)
    session.add_message("assistant", result.final_output)
    manager.save(session)
    
    return result.final_output
```

---

## Session Lifecycle

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': 'transparent', 'primaryTextColor': '#ffffff', 'primaryBorderColor': '#ffffff', 'lineColor': '#ffffff', 'secondaryColor': 'transparent', 'tertiaryColor': 'transparent', 'background': 'transparent', 'mainBkg': 'transparent', 'nodeBorder': '#ffffff', 'clusterBkg': 'transparent', 'clusterBorder': '#ffffff', 'titleColor': '#ffffff', 'edgeLabelBackground': 'transparent', 'nodeTextColor': '#ffffff'}}}%%
stateDiagram-v2
    [*] --> Created: create_session()
    Created --> Active: add_message()
    Active --> Active: add_message()
    Active --> Saved: save()
    Saved --> Active: get_session()
    Active --> Archived: archive()
    Archived --> [*]: delete()
```

---

## Session Management

```python
# List user's sessions
sessions = manager.get_sessions_for_user("user123")

# Delete session
manager.delete(session_id)

# Archive old sessions
manager.archive_inactive(days=30)

# Clear all sessions
manager.clear_all()
```

---

## Custom Session Store

```python
from pyai.sessions import SessionStore, Session

class PostgresSessionStore(SessionStore):
    """PostgreSQL session storage."""
    
    def __init__(self, connection_string: str):
        self.db = connect(connection_string)
    
    async def save(self, session: Session) -> None:
        # Save to PostgreSQL
        pass
    
    async def get(self, session_id: str) -> Optional[Session]:
        # Retrieve from PostgreSQL
        pass
    
    async def delete(self, session_id: str) -> None:
        # Delete from PostgreSQL
        pass
    
    async def list_for_user(self, user_id: str) -> List[Session]:
        # List user's sessions
        pass
```

---

➡️ [[Evaluation-Module]] | [[Kernel-Module]] | [[Home]]
