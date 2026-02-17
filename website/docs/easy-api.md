# Easy API

The Easy API provides one-liner functions for common AI tasks.

## Functions

### ask

```python
from pyai import ask

answer = ask("What is machine learning?")
```

### chat

```python
from pyai import chat

# Single turn
response = chat("Hello!")

# With context
response = chat("What's 2+2?", context="You are a math tutor.")
```

### summarize

```python
from pyai import summarize

summary = summarize("Long document text...")
```

### analyze

```python
from pyai import analyze

analysis = analyze("Product review text...", analysis_type="sentiment")
```

### extract

```python
from pyai import extract

data = extract("Invoice #123, Amount: $500", schema={"invoice": str, "amount": str})
```

### translate

```python
from pyai import translate

french = translate("Hello world", target_language="French")
```

### code

```python
from pyai import code

python_code = code("function to calculate factorial", language="python")
```

### generate

```python
from pyai import generate

content = generate("blog post about AI", format="markdown")
```

### fetch

```python
from pyai import fetch

data = fetch("weather in Seattle")
```

### research

```python
from pyai import research

report = research("Latest AI trends 2026")
```

### rag

```python
from pyai import rag

# Query with document context
answer = rag("What is PyAI?", documents=["PyAI is a Python SDK..."])
```

See individual function docs for detailed usage.
