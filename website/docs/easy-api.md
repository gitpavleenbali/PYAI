# Easy API

The Easy API provides one-liner functions for common AI tasks.

## Functions

### ask

```python
from openstackai import ask

answer = ask("What is machine learning?")
```

### chat

```python
from openstackai import chat

# Single turn
response = chat("Hello!")

# With context
response = chat("What's 2+2?", context="You are a math tutor.")
```

### summarize

```python
from openstackai import summarize

summary = summarize("Long document text...")
```

### analyze

```python
from openstackai import analyze

analysis = analyze("Product review text...", analysis_type="sentiment")
```

### extract

```python
from openstackai import extract

data = extract("Invoice #123, Amount: $500", schema={"invoice": str, "amount": str})
```

### translate

```python
from openstackai import translate

french = translate("Hello world", target_language="French")
```

### code

```python
from openstackai import code

python_code = code("function to calculate factorial", language="python")
```

### generate

```python
from openstackai import generate

content = generate("blog post about AI", format="markdown")
```

### fetch

```python
from openstackai import fetch

data = fetch("weather in Seattle")
```

### research

```python
from openstackai import research

report = research("Latest AI trends 2026")
```

### rag

```python
from openstackai import rag

# Query with document context
answer = rag("What is openstackai?", documents=["openstackai is a Python SDK..."])
```

See individual function docs for detailed usage.
