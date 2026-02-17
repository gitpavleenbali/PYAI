"""
Skills Module - Composable capabilities and tool integrations

Skills define what an agent CAN DO. They are:
- Composable: Mix and match skills for different agents
- Executable: Each skill performs a specific action
- Describable: Skills describe themselves for LLM tool-use
- Chainable: Skills can call other skills

Skill Types:
- Skill: Base class for all skills
- ToolSkill: Wrapper for function-based tools
- ActionSkill: Discrete actions with inputs/outputs
- IntegrationSkill: External service integrations
"""

from pyagent.skills.action_skill import Action, ActionSkill, ActionType, action
from pyagent.skills.builtin import (
    CodeSkill,
    FileSkill,
    MathSkill,
    SearchSkill,
    WebSkill,
)
from pyagent.skills.registry import SkillRegistry
from pyagent.skills.skill import Skill, SkillParameter, SkillResult
from pyagent.skills.tool_skill import ToolSkill, tool

__all__ = [
    # Core
    "Skill",
    "SkillResult",
    "SkillParameter",
    "ToolSkill",
    "tool",
    "ActionSkill",
    "Action",
    "action",
    "ActionType",
    "SkillRegistry",
    # Built-in skills
    "SearchSkill",
    "CodeSkill",
    "FileSkill",
    "WebSkill",
    "MathSkill",
]
