from agents.core.agent_registry import AgentRegistry


class TestAgent:
    """Simple test agent."""

    def execute(self, task):
        return "Test agent executed"


registry = AgentRegistry()

test_agent = TestAgent()

# Register agent
registry.register("test", test_agent)

print("\n========== AGENT REGISTRY TEST ==========")

# Test get()
agent = registry.get("test")

if agent is test_agent:
    print("Register and get: PASS")
else:
    print("Register and get: FAIL")

# Test capabilities()
capabilities = registry.capabilities()

print(f"Capabilities: {capabilities}")

if "test" in capabilities:
    print("Capabilities listing: PASS")
else:
    print("Capabilities listing: FAIL")

# Test unknown capability
unknown_agent = registry.get("unknown")

if unknown_agent is None:
    print("Unknown capability handling: PASS")
else:
    print("Unknown capability handling: FAIL")

print("========== TEST COMPLETE ==========")