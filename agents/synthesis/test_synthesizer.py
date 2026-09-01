from agents.synthesis.synthesizer import SynthesisAgent


results = [
    "Research completed for: Python programming",
    "Analysis completed for: Python programming",
    "Verification completed for: Python programming",
]

agent = SynthesisAgent()

final_result = agent.synthesize(results)

print("\nFinal result:")
print(final_result)