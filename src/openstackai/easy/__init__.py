"""
openstackai Easy API - The Revolutionary Simple Interface

This module provides pandas-like simplicity for AI operations.
Import and use - no configuration required.

Examples:
    >>> from openstackai import ask, research, summarize
    >>> answer = ask("What is the capital of France?")
    >>> papers = research("machine learning trends 2024")
    >>> summary = summarize("https://example.com/article")
"""

import importlib

# Cache for loaded modules
_cache = {}


# Use lazy imports to avoid circular dependencies
def __getattr__(name):
    """Lazy import for submodules."""
    if name in _cache:
        return _cache[name]

    if name == "ask":
        from openstackai.easy.ask import ask as _ask

        _cache[name] = _ask
        return _ask
    elif name == "research":
        from openstackai.easy.research import research as _research

        _cache[name] = _research
        return _research
    elif name == "summarize":
        from openstackai.easy.summarize import summarize as _summarize

        _cache[name] = _summarize
        return _summarize
    elif name == "extract":
        from openstackai.easy.extract import extract as _extract

        _cache[name] = _extract
        return _extract
    elif name == "generate":
        from openstackai.easy.generate import generate as _generate

        _cache[name] = _generate
        return _generate
    elif name == "translate":
        from openstackai.easy.translate import translate as _translate

        _cache[name] = _translate
        return _translate
    elif name == "chat":
        from openstackai.easy.chat import chat as _chat

        _cache[name] = _chat
        return _chat
    elif name == "agent":
        from openstackai.easy.agent_factory import agent as _agent

        _cache[name] = _agent
        return _agent
    elif name == "rag":
        _mod = importlib.import_module("openstackai.easy.rag")
        _cache[name] = _mod
        return _mod
    elif name == "fetch":
        _mod = importlib.import_module("openstackai.easy.fetch")
        _cache[name] = _mod
        return _mod
    elif name == "analyze":
        _mod = importlib.import_module("openstackai.easy.analyze")
        _cache[name] = _mod
        return _mod
    elif name == "code":
        _mod = importlib.import_module("openstackai.easy.code")
        _cache[name] = _mod
        return _mod
    elif name == "configure":
        from openstackai.easy.config import configure as _configure

        _cache[name] = _configure
        return _configure
    elif name == "get_config":
        from openstackai.easy.config import get_config as _get_config

        _cache[name] = _get_config
        return _get_config
    raise AttributeError(f"module 'openstackai.easy' has no attribute '{name}'")


__all__ = [
    # Functions
    "ask",
    "research",
    "summarize",
    "extract",
    "generate",
    "translate",
    "chat",
    # Modules
    "rag",
    "fetch",
    "analyze",
    "code",
    # Factory
    "agent",
    # Config
    "configure",
    "get_config",
]
