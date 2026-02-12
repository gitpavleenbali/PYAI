"""
🐼🤖 PyAgent Demo - The Pandas of AI Agents

This demo showcases how simple AI development can be with PyAgent.
Each example demonstrates the revolutionary one-liner approach.

Prerequisites:
    pip install openai
    export OPENAI_API_KEY=sk-...
    
Or configure inline:
    import pyagent
    pyagent.configure(api_key="sk-...")
"""

import os
import sys

# Add the pyagent package to path for local testing
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

print("=" * 60)
print("🐼🤖 PyAgent Demo - The Pandas of AI Agents")
print("=" * 60)
print()

# Check if API key or Azure endpoint is set
DEMO_MODE = False
azure_endpoint = os.environ.get("AZURE_OPENAI_ENDPOINT")
api_key = os.environ.get("OPENAI_API_KEY")

if azure_endpoint:
    print(f"✅ Azure OpenAI configured: {azure_endpoint}")
    import pyagent
    pyagent.configure(
        provider="azure",
        azure_endpoint=azure_endpoint,
        model=os.environ.get("AZURE_OPENAI_DEPLOYMENT", "gpt-4o-mini")
    )
    print()
elif api_key:
    print("✅ OpenAI API key found! Running live demos...")
    print()
else:
    print("⚠️  No OPENAI_API_KEY or AZURE_OPENAI_ENDPOINT found.")
    print("   Set with: export OPENAI_API_KEY=sk-...")
    print("   Or Azure: export AZURE_OPENAI_ENDPOINT=https://...")
    print()
    print("   Running in DEMO MODE (showing API structure only)")
    print()
    DEMO_MODE = True

# =============================================================================
# Demo 1: Basic Imports
# =============================================================================
print("📦 Demo 1: Simple Imports")
print("-" * 40)

try:
    from pyagent import ask, research, summarize, translate, generate
    from pyagent import rag, fetch, analyze, code
    from pyagent import agent, chat
    print("✅ All imports successful!")
    print()
    print("Available one-liners:")
    print("  • ask()      - Ask anything, get answers")
    print("  • research() - Deep research on any topic")
    print("  • summarize()- Summarize text/files/URLs")
    print("  • extract()  - Extract structured data")
    print("  • generate() - Generate content/code")
    print("  • translate()- Translate between languages")
    print("  • chat()     - Interactive chat sessions")
    print()
    print("Available modules:")
    print("  • rag        - RAG operations")
    print("  • fetch      - Weather, news, stocks")
    print("  • analyze    - Data analysis")
    print("  • code       - Code operations")
    print()
except Exception as e:
    print(f"❌ Import error: {e}")
    sys.exit(1)

# =============================================================================
# Demo 2: The ask() Function
# =============================================================================
print("=" * 60)
print("🔮 Demo 2: ask() - The Simplest AI Function")
print("-" * 40)

print("""
Usage Examples:
    
    # Basic question
    answer = ask("What is Python?")
    
    # Detailed answer
    answer = ask("Explain machine learning", detailed=True)
    
    # Concise answer
    answer = ask("What is AI?", concise=True)
    
    # Formatted output
    tips = ask("5 Python tips", format="bullet")
    
    # JSON output
    data = ask("Generate user profile", as_json=True)
""")

if not DEMO_MODE:
    print("Live demo:")
    try:
        answer = ask("What is 2+2?", concise=True)
        print(f"  ask('What is 2+2?') → {answer}")
    except Exception as e:
        print(f"  Error: {e}")
print()

# =============================================================================
# Demo 3: RAG Module
# =============================================================================
print("=" * 60)
print("📚 Demo 3: rag - RAG in 2 Lines")
print("-" * 40)

print("""
Usage Examples:

    # One-line RAG
    answer = rag.ask("./docs", "What is the conclusion?")
    
    # Index once, query many times
    docs = rag.index("./documents")
    answer1 = docs.ask("What is the main finding?")
    answer2 = docs.ask("What methodology was used?")
    
    # From URL
    answer = rag.from_url("https://example.com", "Summarize this")
    
    # From raw text
    answer = rag.from_text(long_text, "What are the key points?")
""")

print("Creating a demo RAG index...")
try:
    # Create sample content for demo
    sample_text = """
    PyAgent is a revolutionary AI library. It provides pandas-like simplicity 
    for AI development. The main features include one-liner functions for 
    RAG, research, summarization, and more. The library supports OpenAI, 
    Anthropic, and Azure providers. The conclusion is that AI development 
    should be simple and accessible to everyone.
    """
    
    # Index and query
    docs = rag.index([sample_text])
    print(f"  ✅ Indexed: {docs}")
    
    if not DEMO_MODE:
        answer = docs.ask("What is the main conclusion?")
        print(f"  Question: 'What is the main conclusion?'")
        print(f"  Answer: {answer[:100]}...")
except Exception as e:
    print(f"  Note: {e}")
print()

# =============================================================================
# Demo 4: fetch Module
# =============================================================================
print("=" * 60)
print("🌤️ Demo 4: fetch - Real-time Data")
print("-" * 40)

print("""
Usage Examples:

    # Weather
    weather = fetch.weather("Tokyo")
    print(weather.temperature, weather.conditions)
    
    # News
    news = fetch.news("AI technology")
    for article in news:
        print(article.title)
    
    # Stocks
    stock = fetch.stock("AAPL")
    print(stock.price, stock.change_percent)
    
    # Crypto
    btc = fetch.crypto("BTC")
    print(btc.price)
""")

if not DEMO_MODE:
    print("Live demo:")
    try:
        weather = fetch.weather("New York")
        print(f"  fetch.weather('New York') → {weather}")
    except Exception as e:
        print(f"  Error: {e}")
print()

# =============================================================================
# Demo 5: agent() Factory
# =============================================================================
print("=" * 60)
print("🤖 Demo 5: agent() - Create Custom Agents")
print("-" * 40)

print("""
Usage Examples:

    # Custom agent
    coder = agent("You are an expert Python developer")
    code = coder("Write a function to parse JSON")
    
    # Prebuilt personas
    researcher = agent(persona="researcher")
    result = researcher("Research quantum computing")
    
    # Available personas:
    #   - coder, researcher, writer, analyst
    #   - teacher, advisor, critic, creative, editor
    
    # Agent with memory
    assistant = agent("You are helpful", memory=True)
    assistant("My name is John")
    assistant("What's my name?")  # Remembers: "John"
""")

print("Creating demo agents...")
try:
    coder_agent = agent(persona="coder")
    print(f"  ✅ Created: {coder_agent}")
    
    researcher_agent = agent(persona="researcher")
    print(f"  ✅ Created: {researcher_agent}")
    
    custom_agent = agent("You are a helpful math tutor", name="MathTutor")
    print(f"  ✅ Created: {custom_agent}")
except Exception as e:
    print(f"  Note: {e}")
print()

# =============================================================================
# Demo 6: code Module
# =============================================================================
print("=" * 60)
print("💻 Demo 6: code - AI Code Operations")
print("-" * 40)

print("""
Usage Examples:

    # Write code
    python_code = code.write("function to calculate factorial")
    
    # Review code
    review = code.review(my_code)
    print(review.score, review.issues)
    
    # Debug errors
    fix = code.debug("TypeError: cannot unpack...")
    
    # Explain code
    explanation = code.explain(complex_function)
    
    # Refactor
    improved = code.refactor(old_code, goal="readability")
    
    # Convert between languages
    js_code = code.convert(py_code, from_lang="python", to_lang="javascript")
""")

if not DEMO_MODE:
    print("Live demo:")
    try:
        generated = code.write("hello world function", language="python")
        print(f"  code.write('hello world') →")
        print(f"    {generated[:100]}...")
    except Exception as e:
        print(f"  Error: {e}")
print()

# =============================================================================
# Demo 7: chat() Sessions
# =============================================================================
print("=" * 60)
print("💬 Demo 7: chat() - Interactive Sessions")
print("-" * 40)

print("""
Usage Examples:

    # Create a session
    session = chat(persona="teacher")
    
    # Have a conversation (context is remembered!)
    session("What is machine learning?")
    session("Give me an example")     # Remembers it's about ML
    session("How do I learn it?")     # Still has full context
    
    # Custom system message
    session = chat("You are a pirate. Speak like one!")
    session("Hello!")  # "Ahoy, matey!"
""")

print("Creating demo chat session...")
try:
    session = chat(persona="teacher")
    print(f"  ✅ Created: {session}")
    print("  Session can remember conversation context!")
except Exception as e:
    print(f"  Note: {e}")
print()

# =============================================================================
# Summary
# =============================================================================
print("=" * 60)
print("🎉 PyAgent Demo Complete!")
print("=" * 60)
print()
print("What you've seen:")
print("  ✓ One-liner imports for all AI operations")
print("  ✓ RAG in 2 lines (vs 15+ with other frameworks)")
print("  ✓ Real-time data fetching (weather, news, stocks)")
print("  ✓ Custom agents with prebuilt personas")
print("  ✓ Code operations (write, review, debug)")
print("  ✓ Interactive chat with memory")
print()
print("Comparison:")
print("  | Task              | LangChain | PyAgent |")
print("  |-------------------|-----------|---------|")
print("  | RAG               | 15+ lines | 2 lines |")
print("  | Research Agent    | 25+ lines | 1 line  |")
print("  | Weather Fetch     | 20+ lines | 1 line  |")
print()
print("🐼 PyAgent - Because AI development should be as simple as pandas!")
print()

if DEMO_MODE:
    print("To run with live AI:")
    print("  export OPENAI_API_KEY=sk-...")
    print("  python demo.py")
