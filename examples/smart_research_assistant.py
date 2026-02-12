"""
🧠 PyAgent Smart Research Assistant
====================================

This example demonstrates how to build a powerful AI-powered research
assistant using PyAgent's revolutionary simple API.

Features:
- 📚 Document analysis and Q&A (RAG)
- 🔍 Deep research on any topic
- 💻 Code generation and review
- 🎭 Role-based expert personas
- 💬 Interactive chat with memory

This showcases the TRUE POWER of PyAgent:
What would take 50+ lines in other frameworks takes just 2-3 lines here!

Usage:
    $env:AZURE_OPENAI_ENDPOINT = "https://openai-pyagent.openai.azure.com/"
    $env:AZURE_OPENAI_DEPLOYMENT = "gpt-4o-mini"
    python smart_research_assistant.py

Requirements:
    - PyAgent library
    - Azure OpenAI or OpenAI API key
"""

import os
import sys

# =============================================================================
# SETUP: Configure PyAgent with Azure OpenAI
# =============================================================================

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import ALL the amazing PyAgent functions
import pyagent
from pyagent import (
    ask,           # Ask any question
    research,      # Deep research on topics
    summarize,     # Summarize anything
    agent,         # Create custom AI agents
    chat,          # Interactive chat sessions
    code,          # Code operations
    rag,           # Document Q&A
    analyze,       # Data analysis
)

# Configure for Azure OpenAI
azure_endpoint = os.environ.get("AZURE_OPENAI_ENDPOINT")
if azure_endpoint:
    pyagent.configure(
        provider="azure",
        azure_endpoint=azure_endpoint,
        model=os.environ.get("AZURE_OPENAI_DEPLOYMENT", "gpt-4o-mini")
    )
    print("✅ Azure OpenAI configured\n")
elif os.environ.get("OPENAI_API_KEY"):
    print("✅ OpenAI API configured\n")
else:
    print("⚠️  No API configured!")
    sys.exit(1)


# =============================================================================
# FEATURE 1: Instant Research
# Deep research on any topic in ONE LINE!
# =============================================================================

def demo_research():
    """
    Demonstrate PyAgent's research() function.
    
    In other frameworks, this would require:
    - Setting up search APIs
    - Multiple LLM calls
    - Result aggregation
    - Custom prompt engineering
    
    In PyAgent? ONE LINE. 🚀
    """
    print("=" * 60)
    print("📚 FEATURE 1: Instant Research")
    print("=" * 60)
    
    topic = "Benefits of microservices architecture"
    print(f"\n🔍 Researching: {topic}")
    print("-" * 40)
    
    # ONE LINE to do deep research! 🎉
    result = research(topic, quick=True)
    
    print(f"\n📋 Summary:\n{result}")


# =============================================================================
# FEATURE 2: Document Q&A with RAG
# Index documents and query them - just 2 lines!
# =============================================================================

def demo_rag():
    """
    Demonstrate PyAgent's RAG (Retrieval-Augmented Generation) capabilities.
    
    Traditional RAG setup requires:
    - Document loaders (20+ lines)
    - Text splitters (10+ lines)
    - Embeddings setup (10+ lines)
    - Vector store (15+ lines)
    - Retrieval chain (15+ lines)
    Total: 70+ lines
    
    PyAgent? TWO LINES! 🔥
    """
    print("\n" + "=" * 60)
    print("📖 FEATURE 2: Document Q&A (RAG)")
    print("=" * 60)
    
    # Sample documents (in real use, these could be files or URLs)
    documents = [
        """
        PyAgent is a revolutionary Python library for AI development.
        It was created in 2026 to make AI accessible to everyone.
        The main philosophy is: complex AI tasks should be ONE LINE of code.
        PyAgent supports OpenAI, Anthropic, and Azure OpenAI providers.
        """,
        """
        Key features of PyAgent include:
        1. ask() - Ask any question and get intelligent answers
        2. research() - Deep research on any topic
        3. rag - Document Q&A with vector search
        4. agent() - Create custom AI agents with personas
        5. chat() - Interactive sessions with memory
        The library is designed for developers who want results, not boilerplate.
        """,
        """
        PyAgent vs Other Frameworks:
        - LangChain: 50+ lines for RAG vs PyAgent's 2 lines
        - LlamaIndex: Complex indexing vs PyAgent's simple index()
        - AutoGen: Multi-agent setup vs PyAgent's one-liner
        The goal is to be the "pandas of AI" - simple, powerful, intuitive.
        """
    ]
    
    print("\n📥 Indexing 3 documents...")
    
    # LINE 1: Index documents 
    docs = rag.index(documents)
    print(f"   ✅ Indexed: {docs}")
    
    # LINE 2: Ask questions!
    questions = [
        "What is PyAgent's main philosophy?",
        "How does PyAgent compare to LangChain?",
        "What providers does PyAgent support?"
    ]
    
    for q in questions:
        print(f"\n❓ Question: {q}")
        answer = docs.ask(q)
        print(f"💡 Answer: {answer}")


# =============================================================================
# FEATURE 3: Expert Agent Personas
# Create specialized AI assistants instantly
# =============================================================================

def demo_agents():
    """
    Demonstrate PyAgent's agent() function with different personas.
    
    PyAgent comes with prebuilt personas:
    - coder: Expert programmer
    - researcher: Academic researcher
    - writer: Content writer
    - analyst: Data analyst
    - teacher: Patient educator
    
    Creating a specialized agent? ONE LINE! 🎯
    """
    print("\n" + "=" * 60)
    print("🤖 FEATURE 3: Expert Agent Personas")
    print("=" * 60)
    
    # Create different expert agents - each is ONE LINE!
    
    # 1. Code Expert
    print("\n👨‍💻 Code Expert Agent")
    print("-" * 40)
    coder = agent(persona="coder")
    response = coder("Write a Python one-liner to reverse a string")
    print(f"Response: {response}")
    
    # 2. Teacher Agent
    print("\n👩‍🏫 Teacher Agent")
    print("-" * 40)
    teacher = agent(persona="teacher")
    response = teacher("Explain recursion to a beginner in 2 sentences")
    print(f"Response: {response}")
    
    # 3. Custom Agent with memory
    print("\n🎭 Custom Agent with Memory")
    print("-" * 40)
    assistant = agent(
        "You are a friendly startup advisor. Be concise and actionable.",
        name="StartupCoach"
    )
    
    # The agent remembers previous messages!
    assistant("I'm building an AI startup")
    response = assistant("What should be my first priority?")
    print(f"Response: {response}")


# =============================================================================
# FEATURE 4: AI-Powered Code Review
# Get code reviewed instantly
# =============================================================================

def demo_code_review():
    """
    Demonstrate PyAgent's code module for code operations.
    
    Features:
    - code.write() - Generate code from description
    - code.review() - Review code for issues
    - code.debug() - Debug error messages
    - code.explain() - Explain complex code
    - code.refactor() - Improve code quality
    """
    print("\n" + "=" * 60)
    print("💻 FEATURE 4: AI Code Operations")
    print("=" * 60)
    
    # Generate code
    print("\n🔨 Generating code...")
    generated = code.write(
        "a function that checks if a number is prime",
        language="python"
    )
    print(f"Generated Code:\n{generated}")
    
    # Review code
    print("\n🔍 Reviewing code...")
    sample_code = """
def calc(x, y):
    result = x + y
    result = result * 2
    return result
    """
    review_result = code.review(sample_code)
    print(f"Review Score: {review_result.score}/10")
    print(f"Suggestions: {review_result.suggestions}")


# =============================================================================
# FEATURE 5: Interactive Chat Session
# Conversational AI with persistent memory
# =============================================================================

def demo_chat():
    """
    Demonstrate PyAgent's chat() for interactive sessions.
    
    Key feature: The chat session REMEMBERS context!
    This is what makes it powerful for multi-turn conversations.
    """
    print("\n" + "=" * 60)
    print("💬 FEATURE 5: Interactive Chat with Memory")
    print("=" * 60)
    
    # Create a chat session - ONE LINE!
    session = chat("You are a helpful Python tutor. Be concise.")
    
    # Have a multi-turn conversation
    conversations = [
        "What's the difference between a list and tuple?",
        "Show me an example of each",  # It remembers we're talking about lists/tuples!
        "Which one is faster?"         # Still in context!
    ]
    
    for user_message in conversations:
        print(f"\n👤 User: {user_message}")
        response = session.say(user_message)
        print(f"🤖 Tutor: {response}")


# =============================================================================
# FEATURE 6: Sentiment Analysis
# Analyze text sentiment instantly
# =============================================================================

def demo_sentiment():
    """
    Demonstrate PyAgent's analyze module for text analysis.
    """
    print("\n" + "=" * 60)
    print("📊 FEATURE 6: Sentiment Analysis")
    print("=" * 60)
    
    texts = [
        "PyAgent is absolutely amazing! Best library I've ever used!",
        "The documentation could use some improvements.",
        "I love how simple it makes AI development."
    ]
    
    for text in texts:
        print(f"\n📝 Text: {text[:50]}...")
        result = analyze.sentiment(text)
        
        # Handle both dict and object return types
        if isinstance(result, dict):
            sentiment = result.get("sentiment", "unknown")
            score = result.get("score", 0.0)
        else:
            sentiment = result.sentiment
            score = result.score
            
        emoji = "😊" if sentiment == "positive" else "😐" if sentiment == "neutral" else "😞"
        print(f"   Sentiment: {emoji} {sentiment} (score: {score:.2f})")


# =============================================================================
# MAIN: Run All Demos
# =============================================================================

def main():
    """Run the complete Smart Research Assistant demo."""
    print("🧠" * 30)
    print("   PYAGENT SMART RESEARCH ASSISTANT")
    print("🧠" * 30)
    
    # Run all feature demos
    demo_research()
    demo_rag()
    demo_agents()
    demo_code_review()
    demo_chat()
    demo_sentiment()
    
    # Summary
    print("\n" + "=" * 60)
    print("🎉 DEMO COMPLETE!")
    print("=" * 60)
    print("""
What you've seen:
  ✓ research()  - Deep research in ONE line
  ✓ rag         - Document Q&A in TWO lines
  ✓ agent()     - Expert personas in ONE line
  ✓ code.*      - Code operations instantly
  ✓ chat()      - Conversations with memory
  ✓ analyze.*   - Text analysis made simple

This is the PyAgent difference:
  Traditional frameworks: 100+ lines of boilerplate
  PyAgent: 1-3 lines per feature 🚀

🐼🤖 PyAgent - The Pandas of AI Development
    """)


if __name__ == "__main__":
    main()
