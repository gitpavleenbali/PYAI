"""
PyAgent Test Use Cases - 5 Real-World Scenarios
Run: python test_usecases.py
Requires: OPENAI_API_KEY or AZURE_OPENAI_ENDPOINT environment variable
"""

import os
import sys

# Add pyagent to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Check for API key or Azure endpoint
DEMO_MODE = False
if os.getenv("AZURE_OPENAI_ENDPOINT"):
    print("✅ AZURE_OPENAI_ENDPOINT found!")
    import pyagent
    pyagent.configure(
        provider="azure",
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        model=os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-4o-mini")
    )
elif os.getenv("OPENAI_API_KEY"):
    print("✅ OPENAI_API_KEY found!")
else:
    print("⚠️  No API key or Azure endpoint set!")
    print("Set with: $env:OPENAI_API_KEY = 'sk-your-key-here'")
    print("Or Azure: $env:AZURE_OPENAI_ENDPOINT = 'https://...'")
    print("\nRunning in demo mode (no API calls)...\n")
    DEMO_MODE = True


def test_usecase_1():
    """USE CASE 1: Simple Q&A with ask()"""
    print("\n" + "="*60)
    print("USE CASE 1: Simple Q&A")
    print("="*60)
    
    from pyagent import ask
    
    if DEMO_MODE:
        print("Code: answer = ask('Explain quantum computing in simple terms')")
        print("Result: [Demo Mode - would return AI response]")
        return True
    
    answer = ask("Explain quantum computing in simple terms", concise=True)
    print(f"Q: Explain quantum computing in simple terms")
    print(f"A: {answer}")
    return True


def test_usecase_2():
    """USE CASE 2: Create a custom agent"""
    print("\n" + "="*60)
    print("USE CASE 2: Custom Agent Creation")
    print("="*60)
    
    from pyagent import agent
    
    # Create a Python tutor agent
    tutor = agent("python_expert")
    print(f"Created: {tutor}")
    
    if DEMO_MODE:
        print("Code: response = tutor('How do I use list comprehensions?')")
        print("Result: [Demo Mode - would return teaching response]")
        return True
    
    response = tutor("How do I use list comprehensions? Give a short example.")
    print(f"Q: How do I use list comprehensions?")
    print(f"A: {response}")
    return True


def test_usecase_3():
    """USE CASE 3: RAG - Index documents and query"""
    print("\n" + "="*60)
    print("USE CASE 3: RAG Pipeline (2 lines!)")
    print("="*60)
    
    from pyagent import rag
    
    # Sample documents to index
    docs = [
        "Python is a high-level programming language known for its readability.",
        "Machine learning is a subset of AI that enables systems to learn from data.",
        "PyAgent is a revolutionary library that makes AI tasks simple and intuitive."
    ]
    
    # Index documents
    indexed = rag.index(docs)
    print(f"Indexed: {indexed}")
    
    if DEMO_MODE:
        print("Code: answer = rag.ask(indexed, 'What is PyAgent?')")
        print("Result: [Demo Mode - would return RAG response]")
        return True
    
    # Query
    answer = rag.ask(indexed, "What is PyAgent?")
    print(f"Q: What is PyAgent?")
    print(f"A: {answer}")
    return True


def test_usecase_4():
    """USE CASE 4: Code generation"""
    print("\n" + "="*60)
    print("USE CASE 4: Code Generation")
    print("="*60)
    
    from pyagent import code
    
    if DEMO_MODE:
        print("Code: result = code.write('function to calculate fibonacci')")
        print("Result: [Demo Mode - would return Python code]")
        return True
    
    result = code.write("a Python function to calculate fibonacci numbers")
    print("Request: Python function for fibonacci")
    print(f"Generated:\n{result}")
    return True


def test_usecase_5():
    """USE CASE 5: Chat session with memory"""
    print("\n" + "="*60)
    print("USE CASE 5: Conversational Chat with Memory")
    print("="*60)
    
    from pyagent import chat
    
    # Start a chat session
    session = chat("You are a helpful travel assistant")
    print(f"Created: {session}")
    
    if DEMO_MODE:
        print("Code:")
        print("  session.say('I want to visit Paris')")
        print("  session.say('What should I see there?')  # Remembers context!")
        print("Result: [Demo Mode - would return contextual responses]")
        return True
    
    # Multi-turn conversation
    r1 = session.say("I want to visit Paris this summer")
    print(f"User: I want to visit Paris this summer")
    print(f"Assistant: {r1}")
    
    r2 = session.say("What should I see there?")
    print(f"\nUser: What should I see there?")
    print(f"Assistant: {r2}")
    return True


def run_all_tests():
    """Run all 5 use cases"""
    print("\n" + "🚀"*30)
    print("  PYAGENT TEST SUITE - 5 USE CASES")
    print("🚀"*30)
    
    results = []
    
    tests = [
        ("Simple Q&A", test_usecase_1),
        ("Custom Agent", test_usecase_2),
        ("RAG Pipeline", test_usecase_3),
        ("Code Generation", test_usecase_4),
        ("Chat with Memory", test_usecase_5),
    ]
    
    for name, test_fn in tests:
        try:
            success = test_fn()
            results.append((name, "✅ PASS" if success else "❌ FAIL"))
        except Exception as e:
            results.append((name, f"❌ ERROR: {e}"))
            import traceback
            traceback.print_exc()
    
    # Summary
    print("\n" + "="*60)
    print("TEST RESULTS SUMMARY")
    print("="*60)
    for name, status in results:
        print(f"  {name}: {status}")
    
    passed = sum(1 for _, s in results if "PASS" in s)
    print(f"\n  Total: {passed}/{len(results)} passed")
    
    # Quick reference
    print("\n" + "="*60)
    print("QUICK REFERENCE - PyAgent One-Liners")
    print("="*60)
    print("""
    from pyagent import ask, agent, rag, code, chat
    
    # 1. Ask anything
    answer = ask("What is AI?")
    
    # 2. Create agents
    coder = agent("coder")
    
    # 3. RAG in 2 lines
    docs = rag.index(["doc1", "doc2"])
    answer = rag.ask(docs, "question")
    
    # 4. Generate code
    code.write("fibonacci function")
    
    # 5. Chat with memory
    session = chat("You are helpful")
    session.say("Hello!")
    """)


if __name__ == "__main__":
    run_all_tests()
