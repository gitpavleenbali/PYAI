# Copyright (c) 2026 openstackai Contributors
# Licensed under the MIT License

"""
openstackai CLI Module

Command-line interface for running and evaluating agents.

Inspired by Google ADK's `adk` CLI commands:
- adk run: Run an agent
- adk eval: Evaluate an agent
- adk deploy: Deploy to cloud
- adk web: Start web interface

Usage:
    # Run from command line
    openstackai run examples/basic_agent.py
    openstackai eval tests/math_tests.evalset.json --agent my_agent.py
    openstackai serve --port 8000

    # Or use as module
    python -m openstackai run agent.yaml

Commands:
    run     Run an agent interactively
    eval    Evaluate agent on test cases
    serve   Start API server
    init    Initialize a new agent project
    info    Show openstackai info
"""


# Lazy imports for CLI
def __getattr__(name):
    """Lazy load CLI components."""
    if name == "main":
        from .main import main

        return main
    elif name == "app":
        from .main import app

        return app
    elif name == "CLIApp":
        from .app import CLIApp

        return CLIApp
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


__all__ = [
    "main",
    "app",
    "CLIApp",
]
