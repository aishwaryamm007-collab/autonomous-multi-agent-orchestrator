from agents.core.llm_service import LLMService


print("\n========== LLM CONNECTION TEST ==========")

llm_service = LLMService()

prompt = """
User goal: Research Python and Java.

Return a structured list of subtasks.
"""

try:
    result = llm_service.generate(prompt)

    print("\nLLM connection: PASS")
    print("\nGenerated result:")
    print(result)

except Exception as error:
    print("\nLLM connection: FAIL")
    print(f"Error: {error}")

print("\n========== TEST COMPLETE ==========")