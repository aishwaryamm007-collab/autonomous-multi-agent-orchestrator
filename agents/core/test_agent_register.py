from agents.core.agent_registry import AgentRegistry


def research_function():
    return "research"


def analysis_function():
    return "analysis"


registry = AgentRegistry()

registry.register("research", research_function)
registry.register("analysis", analysis_function)

print("Available capabilities:")
print(registry.capabilities())

research_agent = registry.get("research")

print("\nResearch agent result:")
print(research_agent())