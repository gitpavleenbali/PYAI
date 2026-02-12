"""
PyAgent Real-World Integration Tests
=====================================

This script tests PyAgent with actual API calls.

Setup:
    # For OpenAI:
    $env:OPENAI_API_KEY = "sk-your-key"
    
    # For Azure OpenAI:
    $env:AZURE_OPENAI_API_KEY = "your-key"
    $env:AZURE_OPENAI_ENDPOINT = "https://your-resource.openai.azure.com/"
    $env:AZURE_OPENAI_DEPLOYMENT = "gpt-4o-mini"

Run:
    python test_real_world.py [openai|azure]
"""

import os
import sys
import time
from typing import Tuple

# Add pyagent to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def setup_provider(provider: str = "openai") -> Tuple[bool, str]:
    """Configure the provider and return (success, message)."""
    import pyagent
    
    if provider == "azure":
        api_key = os.environ.get("AZURE_OPENAI_API_KEY")
        endpoint = os.environ.get("AZURE_OPENAI_ENDPOINT")
        deployment = os.environ.get("AZURE_OPENAI_DEPLOYMENT", "gpt-4o-mini")
        
        if not endpoint:
            return False, "AZURE_OPENAI_ENDPOINT not set"
        
        # Support Azure AD authentication (no API key needed)
        if not api_key:
            try:
                from azure.identity import DefaultAzureCredential
                # Test if we can get a credential
                credential = DefaultAzureCredential()
                pyagent.configure(
                    provider="azure",
                    azure_endpoint=endpoint,
                    model=deployment
                )
                return True, f"Azure OpenAI (Azure AD auth): {endpoint}"
            except Exception as e:
                return False, f"Azure AD auth failed: {e}"
        else:
            pyagent.configure(
                provider="azure",
                api_key=api_key,
                azure_endpoint=endpoint,
                model=deployment
            )
            return True, f"Azure OpenAI (API key): {endpoint}"
        
    else:  # openai
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            return False, "OPENAI_API_KEY not set"
            
        pyagent.configure(
            provider="openai",
            api_key=api_key,
            model="gpt-4o-mini"
        )
        return True, "OpenAI configured"


def test_ask():
    """Test 1: Simple Q&A with ask()"""
    print("\n" + "="*60)
    print("TEST 1: ask() - Simple Question Answering")
    print("="*60)
    
    from pyagent import ask
    
    start = time.time()
    answer = ask("What is 2+2? Answer with just the number.")
    elapsed = time.time() - start
    
    print(f"Question: What is 2+2?")
    print(f"Answer: {answer}")
    print(f"Time: {elapsed:.2f}s")
    
    # Verify
    if "4" in answer:
        print("✅ PASS")
        return True
    else:
        print("❌ FAIL - Expected '4' in answer")
        return False


def test_ask_detailed():
    """Test 2: Detailed response"""
    print("\n" + "="*60)
    print("TEST 2: ask() - Detailed Response")
    print("="*60)
    
    from pyagent import ask
    
    start = time.time()
    answer = ask("Explain Python in 2 sentences", concise=True)
    elapsed = time.time() - start
    
    print(f"Question: Explain Python in 2 sentences")
    print(f"Answer: {answer[:200]}...")
    print(f"Time: {elapsed:.2f}s")
    
    if len(answer) > 20:
        print("✅ PASS")
        return True
    else:
        print("❌ FAIL - Response too short")
        return False


def test_agent():
    """Test 3: Create and use agent"""
    print("\n" + "="*60)
    print("TEST 3: agent() - Custom Agent")
    print("="*60)
    
    from pyagent import agent
    
    # Create a math tutor
    math_tutor = agent("You are a math tutor. Give brief, clear answers.")
    
    start = time.time()
    response = math_tutor("What is the square root of 144? Just the number.")
    elapsed = time.time() - start
    
    print(f"Agent: Math Tutor")
    print(f"Question: What is the square root of 144?")
    print(f"Response: {response}")
    print(f"Time: {elapsed:.2f}s")
    
    if "12" in response:
        print("✅ PASS")
        return True
    else:
        print("❌ FAIL - Expected '12' in response")
        return False


def test_chat():
    """Test 4: Chat session with memory"""
    print("\n" + "="*60)
    print("TEST 4: chat() - Chat Session with Memory")
    print("="*60)
    
    from pyagent import chat
    
    session = chat("You are a helpful assistant. Be very brief.")
    
    # First message - introduce name
    response1 = session.say("My name is Alex. Remember that.")
    print(f"User: My name is Alex.")
    print(f"Assistant: {response1[:100]}")
    
    # Second message - test memory
    start = time.time()
    response2 = session.say("What is my name?")
    elapsed = time.time() - start
    
    print(f"\nUser: What is my name?")
    print(f"Assistant: {response2}")
    print(f"Time: {elapsed:.2f}s")
    
    if "alex" in response2.lower():
        print("✅ PASS - Memory working!")
        return True
    else:
        print("❌ FAIL - Did not remember name")
        return False


def test_rag():
    """Test 5: RAG Pipeline"""
    print("\n" + "="*60)
    print("TEST 5: rag - RAG Pipeline")
    print("="*60)
    
    from pyagent import rag
    
    # Sample documents
    documents = [
        "PyAgent is a revolutionary AI library created in 2026.",
        "PyAgent makes AI development as simple as using pandas.",
        "The main feature of PyAgent is one-liner functions for complex AI tasks.",
        "PyAgent supports OpenAI, Anthropic, and Azure OpenAI providers."
    ]
    
    # Index
    print("Indexing 4 documents...")
    indexed = rag.index(documents)
    print(f"Indexed: {indexed}")
    
    # Query
    start = time.time()
    answer = indexed.ask("What year was PyAgent created?")
    elapsed = time.time() - start
    
    print(f"\nQuestion: What year was PyAgent created?")
    print(f"Answer: {answer}")
    print(f"Time: {elapsed:.2f}s")
    
    if "2026" in answer:
        print("✅ PASS")
        return True
    else:
        print("❌ FAIL - Expected '2026' in answer")
        return False


def run_all_tests(provider: str = "openai"):
    """Run all real-world tests."""
    print("\n" + "🚀"*30)
    print("  PYAGENT REAL-WORLD INTEGRATION TESTS")
    print("🚀"*30)
    
    # Setup
    success, message = setup_provider(provider)
    print(f"\nProvider: {provider.upper()}")
    print(f"Status: {message}")
    
    if not success:
        print(f"\n❌ Cannot run tests: {message}")
        print("\nSetup instructions:")
        print("  For OpenAI:  $env:OPENAI_API_KEY = 'sk-your-key'")
        print("  For Azure:   $env:AZURE_OPENAI_API_KEY = 'your-key'")
        print("               $env:AZURE_OPENAI_ENDPOINT = 'https://...'")
        return
    
    print("\n" + "-"*60)
    
    # Run tests
    tests = [
        ("Simple Q&A", test_ask),
        ("Detailed Response", test_ask_detailed),
        ("Custom Agent", test_agent),
        ("Chat with Memory", test_chat),
        ("RAG Pipeline", test_rag),
    ]
    
    results = []
    for name, test_fn in tests:
        try:
            passed = test_fn()
            results.append((name, passed))
        except Exception as e:
            print(f"❌ ERROR: {e}")
            import traceback
            traceback.print_exc()
            results.append((name, False))
    
    # Summary
    print("\n" + "="*60)
    print("TEST RESULTS SUMMARY")
    print("="*60)
    
    passed = 0
    for name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"  {name}: {status}")
        if result:
            passed += 1
    
    print(f"\n  Total: {passed}/{len(results)} passed")
    
    if passed == len(results):
        print("\n🎉 All tests passed! PyAgent is working correctly.")
    else:
        print(f"\n⚠️  {len(results) - passed} test(s) failed.")


if __name__ == "__main__":
    # Get provider from command line
    provider = "openai"
    if len(sys.argv) > 1:
        provider = sys.argv[1].lower()
        if provider not in ["openai", "azure"]:
            print(f"Unknown provider: {provider}")
            print("Usage: python test_real_world.py [openai|azure]")
            sys.exit(1)
    
    run_all_tests(provider)
