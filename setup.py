#!/usr/bin/env python
"""
PyAI - The Pandas of AI Agents
=================================

Backwards-compatible setup.py for pip install.
Configuration is primarily in pyproject.toml.

Installation:
    pip install .                    # Basic install
    pip install .[openai]            # With OpenAI
    pip install .[azure]             # With Azure
    pip install .[all]               # Everything
    pip install -e .[dev]            # Development mode
"""

from setuptools import setup, find_packages

if __name__ == "__main__":
    setup(
        packages=find_packages(exclude=["tests*", "examples*", "docs*"]),
        package_data={
            "pyai": ["py.typed", "*.pyi", "README.md", "**/README.md"],
        },
        include_package_data=True,
        zip_safe=False,
    )
